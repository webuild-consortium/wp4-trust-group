"""Fail LoTL validation and publication when any X.509 certificate is expired."""

from __future__ import annotations

import base64
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from urllib.error import URLError
from urllib.request import Request, urlopen

from cryptography import x509
from cryptography.hazmat.backends import default_backend

from tools.lotl.log import get_logger
from tools.lotl.pem_util import normalize_pem_for_ci
from tools.lotl.settings import VALID_TL_TYPES

logger = get_logger(__name__)

_DEFAULT_FETCH_TIMEOUT = 30


def _now_utc(now: Optional[datetime] = None) -> datetime:
    if now is None:
        return datetime.now(timezone.utc)
    if now.tzinfo is None:
        return now.replace(tzinfo=timezone.utc)
    return now.astimezone(timezone.utc)


def _cert_instant(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def _not_before(cert: x509.Certificate) -> datetime:
    instant = getattr(cert, "not_valid_before_utc", None)
    return _cert_instant(instant if instant is not None else cert.not_valid_before)


def _not_after(cert: x509.Certificate) -> datetime:
    instant = getattr(cert, "not_valid_after_utc", None)
    return _cert_instant(instant if instant is not None else cert.not_valid_after)


def load_x509_certificate(data: str | bytes) -> x509.Certificate:
    """Load a single X.509 certificate from PEM or DER bytes."""
    if isinstance(data, str):
        raw = normalize_pem_for_ci(data).encode("utf-8")
    else:
        raw = data
        if raw.lstrip().startswith(b"-----BEGIN"):
            raw = normalize_pem_for_ci(raw.decode("utf-8")).encode("utf-8")
    if b"-----BEGIN" in raw:
        return x509.load_pem_x509_certificate(raw, default_backend())
    return x509.load_der_x509_certificate(raw, default_backend())


def certificate_validity_errors(
    cert: x509.Certificate,
    label: str,
    now: Optional[datetime] = None,
) -> list[str]:
    """Return errors if *cert* is not yet valid or has expired."""
    instant = _now_utc(now)
    not_before = _not_before(cert)
    not_after = _not_after(cert)
    errors: list[str] = []
    subject = cert.subject.rfc4514_string()
    if instant < not_before:
        errors.append(
            f"{label}: certificate is not yet valid "
            f"(notBefore {not_before.isoformat()}, subject={subject})"
        )
    if instant > not_after:
        errors.append(
            f"{label}: certificate expired on {not_after.isoformat()} "
            f"(subject={subject})"
        )
    return errors


def certificate_pem_errors(
    pem: str | bytes,
    label: str,
    now: Optional[datetime] = None,
) -> list[str]:
    """Parse PEM/DER and return parse or validity errors."""
    try:
        cert = load_x509_certificate(pem)
    except ValueError as exc:
        return [f"{label}: cannot parse X.509 certificate: {exc}"]
    return certificate_validity_errors(cert, label, now=now)


def certificate_der_b64_errors(
    der_b64: str,
    label: str,
    now: Optional[datetime] = None,
) -> list[str]:
    """Parse a standard-base64 DER certificate and return validity errors."""
    try:
        der = base64.b64decode(der_b64)
        cert = x509.load_der_x509_certificate(der, default_backend())
    except (ValueError, TypeError) as exc:
        return [f"{label}: cannot parse X.509 certificate: {exc}"]
    return certificate_validity_errors(cert, label, now=now)


def check_tl_entries_certificates(
    tl_entries_dir: str | Path,
    now: Optional[datetime] = None,
) -> list[str]:
    """Check every trust_anchor PEM under lotl/tl_entries/."""
    errors: list[str] = []
    root = Path(tl_entries_dir)
    if not root.exists():
        return [f"Directory not found: {root}"]

    for tl_type_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        if tl_type_dir.name not in VALID_TL_TYPES:
            continue
        for json_file in sorted(tl_type_dir.glob("*.json")):
            try:
                data = json.loads(json_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{json_file}: invalid JSON: {exc}")
                continue
            if not isinstance(data, dict):
                errors.append(f"{json_file}: TL entry must be a JSON object")
                continue
            pem = data.get("trust_anchor")
            if not isinstance(pem, str) or not pem.strip():
                errors.append(f"{json_file}: missing trust_anchor certificate")
                continue
            errors.extend(
                certificate_pem_errors(pem, f"{json_file} trust_anchor", now=now)
            )
    return errors


def _b64url_json(protected: str) -> dict[str, Any]:
    pad = "=" * (-len(protected) % 4)
    raw = base64.urlsafe_b64decode(protected + pad)
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise ValueError("JAdES protected header is not a JSON object")
    return parsed


def load_lotl_json(source: str, timeout: int = _DEFAULT_FETCH_TIMEOUT) -> dict[str, Any]:
    """Load a LoTL JSON document from a filesystem path or http(s) URL."""
    if source.startswith("http://") or source.startswith("https://"):
        req = Request(source, headers={"User-Agent": "WP4-LoTL-ExpiryCheck/1.0"})
        try:
            with urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except (URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
            raise ValueError(f"Failed to load LoTL JSON from {source}: {exc}") from exc
        if not isinstance(payload, dict):
            raise ValueError(f"LoTL JSON from {source} is not an object")
        return payload

    path = Path(source)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Failed to load LoTL JSON from {source}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"LoTL JSON from {source} is not an object")
    return payload


def check_published_lotl_certificates(
    lotl: dict[str, Any],
    now: Optional[datetime] = None,
) -> list[str]:
    """Check the LoTL signing certificate and every pointer trust anchor."""
    errors: list[str] = []

    signature = lotl.get("signature")
    if isinstance(signature, dict):
        protected = signature.get("protected")
        if isinstance(protected, str) and protected:
            try:
                header = _b64url_json(protected)
            except (ValueError, json.JSONDecodeError) as exc:
                errors.append(f"LoTL signing certificate: cannot parse JAdES protected header: {exc}")
            else:
                x5c = header.get("x5c") or []
                if not x5c:
                    errors.append("LoTL signing certificate: JAdES protected header has no x5c")
                for index, der_b64 in enumerate(x5c):
                    if not isinstance(der_b64, str):
                        errors.append(f"LoTL signing certificate (x5c[{index}]): not a string")
                        continue
                    errors.extend(
                        certificate_der_b64_errors(
                            der_b64,
                            f"LoTL signing certificate (x5c[{index}])",
                            now=now,
                        )
                    )

    lote = lotl.get("LoTE")
    lasi: dict[str, Any] = {}
    if isinstance(lote, dict):
        raw_lasi = lote.get("ListAndSchemeInformation")
        if isinstance(raw_lasi, dict):
            lasi = raw_lasi
    pointers = lasi.get("PointersToOtherLoTE") or []
    if not isinstance(pointers, list):
        return errors

    for pointer in pointers:
        if not isinstance(pointer, dict):
            continue
        location = pointer.get("LoTELocation", "unknown")
        quals = pointer.get("LoTEQualifiers") or []
        first_qual = quals[0] if quals and isinstance(quals[0], dict) else {}
        operator = "?"
        names = first_qual.get("SchemeOperatorName") or []
        if names and isinstance(names[0], dict):
            operator = names[0].get("value") or "?"
        lote_type = str(first_qual.get("LoTEType") or "?").rsplit("/", 1)[-1]
        label_base = f"pointer {operator} {lote_type} ({location})"

        for sdi in pointer.get("ServiceDigitalIdentities") or []:
            if not isinstance(sdi, dict):
                continue
            for index, cert_obj in enumerate(sdi.get("X509Certificates") or []):
                der_b64 = cert_obj.get("val") if isinstance(cert_obj, dict) else None
                if not isinstance(der_b64, str) or not der_b64:
                    errors.append(f"{label_base} cert[{index}]: missing certificate value")
                    continue
                errors.extend(
                    certificate_der_b64_errors(
                        der_b64,
                        f"{label_base} cert[{index}]",
                        now=now,
                    )
                )
    return errors


def run_expiry_checks(
    tl_entries_dir: Optional[str | Path] = None,
    lotl_json_source: Optional[str] = None,
    signing_cert_pem: Optional[str | bytes] = None,
    now: Optional[datetime] = None,
) -> list[str]:
    """Run the configured expiry checks and return every error found."""
    errors: list[str] = []
    if tl_entries_dir is not None:
        errors.extend(check_tl_entries_certificates(tl_entries_dir, now=now))
    if lotl_json_source:
        try:
            lotl = load_lotl_json(lotl_json_source)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            errors.extend(check_published_lotl_certificates(lotl, now=now))
    if signing_cert_pem:
        errors.extend(
            certificate_pem_errors(
                signing_cert_pem,
                "LoTL signing certificate",
                now=now,
            )
        )
    return errors
