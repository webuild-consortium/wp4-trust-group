"""Tests for create_signing_cert module."""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from tools.lotl.create_signing_cert import (
    _print_cert_diagnostic,
    create_lotl_signing_cert,
    main,
)


def test_create_lotl_signing_cert_returns_pem(tmp_path: Path) -> None:
    """create_lotl_signing_cert returns key and cert PEM bytes."""
    key_pem, cert_pem = create_lotl_signing_cert(
        scheme_territory="EU",
        scheme_operator_name="Test TLP",
        output_dir=tmp_path,
        key_path=tmp_path / "key.pem",
        cert_path=tmp_path / "cert.pem",
    )
    assert b"-----BEGIN EC PRIVATE KEY-----" in key_pem or b"-----BEGIN PRIVATE KEY-----" in key_pem
    assert b"-----END EC PRIVATE KEY-----" in key_pem or b"-----END PRIVATE KEY-----" in key_pem
    assert b"-----BEGIN CERTIFICATE-----" in cert_pem
    assert b"-----END CERTIFICATE-----" in cert_pem
    assert (tmp_path / "key.pem").exists()
    assert (tmp_path / "cert.pem").exists()


def test_create_lotl_signing_cert_subject_issuer(tmp_path: Path) -> None:
    """Certificate has correct Subject DN per ETSI TS 119 612."""
    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization

    _, cert_pem = create_lotl_signing_cert(
        scheme_territory="IT",
        scheme_operator_name="Example TLP",
        output_dir=tmp_path,
        cert_path=tmp_path / "cert.pem",
    )
    cert = x509.load_pem_x509_certificate(cert_pem, default_backend())
    subject = cert.subject
    issuer = cert.issuer
    attrs = {attr.oid._name: attr.value for attr in subject}
    assert attrs["countryName"] == "IT"
    assert attrs["organizationName"] == "Example TLP"
    assert subject == issuer  # self-signed


def test_create_lotl_signing_cert_extensions(tmp_path: Path) -> None:
    """Certificate has ETSI-required extensions."""
    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
    from cryptography.x509.oid import ExtensionOID

    _, cert_pem = create_lotl_signing_cert(
        scheme_territory="EU",
        scheme_operator_name="Test",
        output_dir=tmp_path,
    )
    cert = x509.load_pem_x509_certificate(cert_pem, default_backend())
    ext = cert.extensions

    ku = ext.get_extension_for_oid(ExtensionOID.KEY_USAGE).value
    assert ku.digital_signature
    assert ku.content_commitment

    bc = ext.get_extension_for_oid(ExtensionOID.BASIC_CONSTRAINTS).value
    assert bc.ca is False

    ski = ext.get_extension_for_oid(ExtensionOID.SUBJECT_KEY_IDENTIFIER)
    assert ski.value.digest is not None


def test_create_lotl_signing_cert_no_paths(tmp_path: Path) -> None:
    """create_lotl_signing_cert works without writing files."""
    key_pem, cert_pem = create_lotl_signing_cert(
        scheme_territory="EU",
        scheme_operator_name="Test",
        output_dir=tmp_path,
    )
    assert len(key_pem) > 0
    assert len(cert_pem) > 0
    assert not (tmp_path / "lotl_signing_key.pem").exists()


def test_main_cli(monkeypatch: pytest.MonkeyPatch) -> None:
    """main() runs CLI and prints usage."""
    with tempfile.TemporaryDirectory() as d:
        monkeypatch.setattr("sys.argv", ["create_signing_cert", "-o", d, "-n", "CLI Test"])
        assert main() == 0


def test_main_cli_custom_args(monkeypatch: pytest.MonkeyPatch) -> None:
    """main() accepts custom args."""
    with tempfile.TemporaryDirectory() as d:
        monkeypatch.setattr(
            "sys.argv",
            [
                "create_signing_cert",
                "-o", d,
                "-t", "DE",
                "-n", "German TLP",
                "--key-file", "mykey.pem",
                "--cert-file", "mycert.pem",
            ],
        )
        assert main() == 0
        assert (Path(d) / "mykey.pem").exists()
        assert (Path(d) / "mycert.pem").exists()


def test_print_cert_diagnostic_openssl(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """_print_cert_diagnostic prints OpenSSL text and raw PEM when openssl succeeds."""
    _, cert_pem = create_lotl_signing_cert(
        scheme_territory="EU",
        scheme_operator_name="Test",
        output_dir=tmp_path,
        cert_path=tmp_path / "cert.pem",
    )
    _print_cert_diagnostic(tmp_path / "cert.pem", cert_pem)
    out = capsys.readouterr().out
    assert "--- Certificate (diagnostic ASN / OpenSSL text) ---" in out
    assert "--- Certificate (raw PEM) ---" in out
    assert "-----BEGIN CERTIFICATE-----" in out
    assert "Subject:" in out or "C = EU" in out


def test_print_cert_diagnostic_fallback(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """_print_cert_diagnostic uses Python fallback when openssl fails."""
    _, cert_pem = create_lotl_signing_cert(
        scheme_territory="IT",
        scheme_operator_name="Fallback Test",
        output_dir=tmp_path,
        cert_path=tmp_path / "cert.pem",
    )
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1, stdout="")
        _print_cert_diagnostic(tmp_path / "cert.pem", cert_pem)
    out = capsys.readouterr().out
    assert "Subject: CN=" in out or "Subject:" in out
    assert "Fallback Test" in out
    assert "-----BEGIN CERTIFICATE-----" in out
