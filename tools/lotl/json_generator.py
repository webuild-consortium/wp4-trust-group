"""Generate LoTL in JSON format (ETSI TS 119 602-1 / ``1960201`` JSON schema shape).

Output is a root object ``{"LoTE": { ... }}`` with ``ListAndSchemeInformation`` using
PascalCase property names, ``PointersToOtherLoTE`` for participant TL references, and
``DistributionPoints`` as an array of URI strings. Aligned with
``github.com/sirosfoundation/g119612`` ``pkg/etsi119602`` types.
"""

from __future__ import annotations

import base64
from calendar import monthrange
from datetime import datetime, timezone
from typing import Any

from tools.lotl.settings import (
    LOTL_JSON_FILENAME,
    LOTL_LOTE_TYPE_URI,
    TL_TYPE_TO_REFERENCE_URI,
)
from tools.lotl.tl_entry import TLEntry


def _pem_cert_to_x509_val_b64(pem: str) -> str | None:
    """DER-encode X.509 PEM and return base64 for ``PKIOb.val``."""
    if not pem or "BEGIN CERTIFICATE" not in pem:
        return None
    try:
        from cryptography import x509
        from cryptography.hazmat.primitives import serialization

        cert = x509.load_pem_x509_certificate(pem.encode("utf-8"))
        der = cert.public_bytes(serialization.Encoding.DER)
        return base64.b64encode(der).decode("ascii")
    except Exception:
        return None


def _service_digital_identities_for_entry(entry: TLEntry) -> list[dict[str, Any]]:
    """Build ``ServiceDigitalIdentities`` from ``trust_anchor`` (PEM), if valid."""
    val = _pem_cert_to_x509_val_b64(entry.trust_anchor)
    if not val:
        return []
    return [{"X509Certificates": [{"val": val}]}]


def _lote_qualifier(
    entry: TLEntry,
    mime_type: str = "application/json",
) -> dict[str, Any]:
    ref = TL_TYPE_TO_REFERENCE_URI[entry.tl_type]
    meta = entry.metadata or {}
    op_name = meta.get("operator_name", entry.participant_id)
    territory = meta.get("country", "EU")
    return {
        "LoTEType": ref,
        "SchemeOperatorName": [{"lang": "en", "value": str(op_name)}],
        "SchemeTerritory": str(territory),
        "MimeType": mime_type,
    }


def _pointers_for_entry(entry: TLEntry) -> list[dict[str, Any]]:
    """Build ``OtherLoTEPointer`` objects for one TL entry (JSON and optional XML)."""
    sdi = _service_digital_identities_for_entry(entry)
    if not sdi:
        raise ValueError(
            f"TL entry {entry.participant_id!r} must provide a valid X.509 trust_anchor"
        )
    json_loc = entry.get_tl_url_json()
    out: list[dict[str, Any]] = [
        {
            "LoTELocation": json_loc,
            "ServiceDigitalIdentities": sdi,
            "LoTEQualifiers": [_lote_qualifier(entry, "application/json")],
        }
    ]
    xml_loc = entry.get_tl_url_xml()
    if xml_loc != json_loc:
        out.append(
            {
                "LoTELocation": xml_loc,
                "ServiceDigitalIdentities": sdi,
                "LoTEQualifiers": [_lote_qualifier(entry, "application/xml")],
            }
        )
    return out


def _default_distribution_uris(
    scheme_information_uri: str,
) -> list[str]:
    base = scheme_information_uri.rstrip("/")
    return [f"{base}/{LOTL_JSON_FILENAME}"]


def _add_months_safe_utc(dt: datetime, months: int) -> datetime:
    """Add months with year carry and day clamping."""
    month_index = (dt.month - 1) + months
    year = dt.year + (month_index // 12)
    month = (month_index % 12) + 1
    day = min(dt.day, monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def generate_lotl_json(
    entries: list[TLEntry],
    sequence_number: int = 1,
    scheme_operator_name: str = "WE BUILD WP4 Trust Group",
    scheme_name: str = "WP4 List of Trusted Lists",
    scheme_information_uri: str = "https://webuild-consortium.github.io/wp4-trust-group/",
    distribution_point_uris: list[str] | None = None,
) -> dict[str, Any]:
    """Generate unsigned LoTE JSON (LoTL) per TS 119 602-1 JSON schema root shape.

    Returns a ``{"LoTE": {"ListAndSchemeInformation": ...}}`` document. ``LOTETag``
    is an XML attribute only; it is not included in JSON (same as g119612).
    """
    now = datetime.now(timezone.utc)
    issue_dt = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    next_update = _add_months_safe_utc(now, 6).strftime("%Y-%m-%dT%H:%M:%SZ")

    pointers: list[dict[str, Any]] = []
    for entry in entries:
        pointers.extend(_pointers_for_entry(entry))

    dist: list[str] = (
        list(distribution_point_uris)
        if distribution_point_uris is not None
        else _default_distribution_uris(scheme_information_uri)
    )

    list_and_scheme: dict[str, Any] = {
        "LoTEVersionIdentifier": 1,
        "LoTESequenceNumber": sequence_number,
        "LoTEType": LOTL_LOTE_TYPE_URI,
        "SchemeOperatorName": [{"lang": "en", "value": scheme_operator_name}],
        "SchemeOperatorAddress": {
            "SchemeOperatorPostalAddress": [
                {
                    "lang": "en",
                    "StreetAddress": "Not specified",
                    "Country": "EU",
                }
            ],
            "SchemeOperatorElectronicAddress": [
                {"lang": "en", "uriValue": scheme_information_uri}
            ],
        },
        "SchemeName": [{"lang": "en", "value": scheme_name}],
        "SchemeInformationURI": [
            {"lang": "en", "uriValue": scheme_information_uri}
        ],
        "StatusDeterminationApproach": (
            "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate"
        ),
        "SchemeTerritory": "EU",
        "ListIssueDateTime": issue_dt,
        "NextUpdate": next_update,
        "DistributionPoints": dist,
        "PointersToOtherLoTE": pointers,
    }

    return {"LoTE": {"ListAndSchemeInformation": list_and_scheme}}
