"""Tests for certificate expiry checks."""

from __future__ import annotations

import base64
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from tools.lotl.cert_expiry import (
    certificate_der_b64_errors,
    certificate_pem_errors,
    certificate_validity_errors,
    check_published_lotl_certificates,
    check_tl_entries_certificates,
    load_lotl_json,
    load_x509_certificate,
    run_expiry_checks,
)
from tools.lotl.tests.conftest import make_self_signed_cert_pem


def _der_b64(pem: str) -> str:
    cert = x509.load_pem_x509_certificate(pem.encode(), default_backend())
    return base64.b64encode(cert.public_bytes(serialization.Encoding.DER)).decode()


def _lotl_with_certs(signing_pem: str, pointer_pem: str) -> dict:
    signing_b64 = _der_b64(signing_pem)
    pointer_b64 = _der_b64(pointer_pem)
    header = json.dumps({"alg": "ES256", "x5c": [signing_b64]})
    protected = base64.urlsafe_b64encode(header.encode()).decode().rstrip("=")
    return {
        "signature": {"protected": protected, "signature": "x"},
        "LoTE": {
            "ListAndSchemeInformation": {
                "PointersToOtherLoTE": [
                    {
                        "LoTELocation": "https://example.com/wallet/tl.xml",
                        "ServiceDigitalIdentities": [
                            {"X509Certificates": [{"val": pointer_b64}]}
                        ],
                        "LoTEQualifiers": [
                            {
                                "LoTEType": (
                                    "http://uri.etsi.org/19602/LoTEType/"
                                    "EUWalletProvidersList"
                                ),
                                "SchemeOperatorName": [
                                    {"lang": "en", "value": "Example TLP"}
                                ],
                            }
                        ],
                    }
                ]
            }
        },
    }


def test_valid_pem_has_no_errors(valid_cert_pem: str) -> None:
    assert certificate_pem_errors(valid_cert_pem, "test") == []


def test_expired_pem_reports_expiry(expired_cert_pem: str) -> None:
    errors = certificate_pem_errors(expired_cert_pem, "wallet pointer")
    assert len(errors) == 1
    assert "expired" in errors[0]
    assert "wallet pointer" in errors[0]


def test_unparseable_pem_reports_parse_error() -> None:
    pem = "-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----\n"
    errors = certificate_pem_errors(pem, "trust_anchor")
    assert errors
    assert "cannot parse" in errors[0]


def test_not_yet_valid_certificate() -> None:
    pem = make_self_signed_cert_pem(not_before_days=1, not_after_days=30).decode()
    errors = certificate_pem_errors(pem, "future cert")
    assert any("not yet valid" in e for e in errors)


def test_load_der_certificate(valid_cert_pem: str) -> None:
    cert = load_x509_certificate(valid_cert_pem)
    der = cert.public_bytes(serialization.Encoding.DER)
    loaded = load_x509_certificate(der)
    assert loaded.serial_number == cert.serial_number


def test_validity_errors_respect_injected_now(valid_cert_pem: str) -> None:
    cert = load_x509_certificate(valid_cert_pem)
    future = datetime.now(timezone.utc) + timedelta(days=400)
    errors = certificate_validity_errors(cert, "aging cert", now=future)
    assert any("expired" in e for e in errors)


def test_check_tl_entries_expired(
    tmp_path: Path, expired_cert_pem: str
) -> None:
    (tmp_path / "wallet-provider").mkdir()
    (tmp_path / "wallet-provider" / "idunion.json").write_text(
        json.dumps({
            "tl_url": "https://example.com/tl.xml",
            "trust_anchor": expired_cert_pem,
        })
    )
    errors = check_tl_entries_certificates(tmp_path)
    assert errors
    assert any("expired" in e for e in errors)
    assert any("idunion.json" in e for e in errors)


def test_check_tl_entries_skips_invalid_type(
    tmp_path: Path, valid_cert_pem: str
) -> None:
    (tmp_path / "not-a-tl-type").mkdir()
    (tmp_path / "not-a-tl-type" / "x.json").write_text(
        json.dumps({"tl_url": "https://x", "trust_anchor": valid_cert_pem})
    )
    assert check_tl_entries_certificates(tmp_path) == []


def test_check_tl_entries_missing_dir() -> None:
    errors = check_tl_entries_certificates("/nonexistent/tl-entries")
    assert errors
    assert "not found" in errors[0].lower()


def test_check_tl_entries_invalid_json(tmp_path: Path) -> None:
    (tmp_path / "pid-provider").mkdir()
    (tmp_path / "pid-provider" / "bad.json").write_text("not-json")
    errors = check_tl_entries_certificates(tmp_path)
    assert any("invalid JSON" in e for e in errors)


def test_check_tl_entries_missing_trust_anchor(tmp_path: Path) -> None:
    (tmp_path / "pid-provider").mkdir()
    (tmp_path / "pid-provider" / "x.json").write_text(
        json.dumps({"tl_url": "https://example.com/tl.json"})
    )
    errors = check_tl_entries_certificates(tmp_path)
    assert any("missing trust_anchor" in e for e in errors)


def test_published_lotl_valid(valid_cert_pem: str) -> None:
    lotl = _lotl_with_certs(valid_cert_pem, valid_cert_pem)
    assert check_published_lotl_certificates(lotl) == []


def test_published_lotl_expired_pointer(
    valid_cert_pem: str, expired_cert_pem: str
) -> None:
    lotl = _lotl_with_certs(valid_cert_pem, expired_cert_pem)
    errors = check_published_lotl_certificates(lotl)
    assert any("pointer" in e and "expired" in e for e in errors)
    assert any("EUWalletProvidersList" in e for e in errors)


def test_published_lotl_expired_signer(
    valid_cert_pem: str, expired_cert_pem: str
) -> None:
    lotl = _lotl_with_certs(expired_cert_pem, valid_cert_pem)
    errors = check_published_lotl_certificates(lotl)
    assert any("signing certificate" in e and "expired" in e for e in errors)


def test_published_lotl_bad_protected_header() -> None:
    lotl = {"signature": {"protected": "%%%not-base64%%%"}}
    errors = check_published_lotl_certificates(lotl)
    assert any("protected header" in e for e in errors)


def test_published_lotl_missing_x5c(valid_cert_pem: str) -> None:
    header = json.dumps({"alg": "ES256"})
    protected = base64.urlsafe_b64encode(header.encode()).decode().rstrip("=")
    lotl = _lotl_with_certs(valid_cert_pem, valid_cert_pem)
    lotl["signature"]["protected"] = protected
    errors = check_published_lotl_certificates(lotl)
    assert any("no x5c" in e for e in errors)


def test_published_lotl_missing_pointer_value(valid_cert_pem: str) -> None:
    lotl = _lotl_with_certs(valid_cert_pem, valid_cert_pem)
    lotl["LoTE"]["ListAndSchemeInformation"]["PointersToOtherLoTE"][0][
        "ServiceDigitalIdentities"
    ][0]["X509Certificates"] = [{}]
    errors = check_published_lotl_certificates(lotl)
    assert any("missing certificate value" in e for e in errors)


def test_der_b64_unparseable() -> None:
    errors = certificate_der_b64_errors("$$$$", "pointer cert")
    assert errors
    assert "cannot parse" in errors[0]


def test_load_lotl_json_from_file(tmp_path: Path, valid_cert_pem: str) -> None:
    path = tmp_path / "lotl.json"
    path.write_text(json.dumps(_lotl_with_certs(valid_cert_pem, valid_cert_pem)))
    loaded = load_lotl_json(str(path))
    assert "signature" in loaded


def test_load_lotl_json_missing_file() -> None:
    with pytest.raises(ValueError, match="Failed to load"):
        load_lotl_json("/nonexistent/lotl.json")


def test_load_lotl_json_from_url(valid_cert_pem: str) -> None:
    payload = json.dumps(_lotl_with_certs(valid_cert_pem, valid_cert_pem)).encode()

    class _Resp:
        def read(self) -> bytes:
            return payload

        def __enter__(self) -> "_Resp":
            return self

        def __exit__(self, *args: object) -> None:
            return None

    with patch("tools.lotl.cert_expiry.urlopen", return_value=_Resp()):
        loaded = load_lotl_json("https://example.com/list_of_trusted_lists.json")
    assert "LoTE" in loaded


def test_load_lotl_json_url_failure() -> None:
    from urllib.error import URLError

    with patch(
        "tools.lotl.cert_expiry.urlopen",
        side_effect=URLError("down"),
    ):
        with pytest.raises(ValueError, match="Failed to load"):
            load_lotl_json("https://example.com/list_of_trusted_lists.json")


def test_run_expiry_checks_combines_sources(
    tmp_path: Path, valid_cert_pem: str, expired_cert_pem: str
) -> None:
    (tmp_path / "wallet-provider").mkdir()
    (tmp_path / "wallet-provider" / "ok.json").write_text(
        json.dumps({
            "tl_url": "https://example.com/tl.xml",
            "trust_anchor": valid_cert_pem,
        })
    )
    lotl_path = tmp_path / "lotl.json"
    lotl_path.write_text(json.dumps(_lotl_with_certs(valid_cert_pem, expired_cert_pem)))
    errors = run_expiry_checks(
        tl_entries_dir=tmp_path,
        lotl_json_source=str(lotl_path),
        signing_cert_pem=valid_cert_pem,
    )
    assert any("pointer" in e and "expired" in e for e in errors)


def test_run_expiry_checks_bad_lotl_source() -> None:
    errors = run_expiry_checks(lotl_json_source="/no/such/lotl.json")
    assert errors
    assert "Failed to load" in errors[0]
