"""Tests for CLI."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[3]  # wp4-trust-group root


def test_cli_validate_only(tmp_path: Path, valid_cert_pem: str) -> None:
    """--validate-only runs without signing key."""
    import json

    (tmp_path / "pid-provider").mkdir()
    (tmp_path / "pid-provider" / "x.json").write_text(
        json.dumps({
            "tl_url": "https://example.com/tl.json",
            "trust_anchor": valid_cert_pem,
        })
    )
    env = {**os.environ, "PYTHONPATH": str(PROJECT_ROOT)}
    result = subprocess.run(
        [sys.executable, "-m", "tools.lotl", "--validate-only", "--tl-entries-dir", str(tmp_path), "--output-dir", str(tmp_path)],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        env=env,
    )
    assert result.returncode == 0, (result.stdout, result.stderr)


def test_cli_help() -> None:
    """--help works."""
    env = {**os.environ, "PYTHONPATH": str(PROJECT_ROOT)}
    result = subprocess.run(
        [sys.executable, "-m", "tools.lotl", "--help"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        env=env,
    )
    assert result.returncode == 0, (result.stdout, result.stderr)
    assert "tl-entries-dir" in result.stdout


def test_cli_main_invocation(tl_entries_dir: Path) -> None:
    """CLI main() can be invoked directly."""
    from tools.lotl.cli import main

    exit_code = main([
        "--validate-only",
        "--tl-entries-dir", str(tl_entries_dir),
        "--output-dir", str(tl_entries_dir),
    ])
    assert exit_code == 0


def test_cli_inline_pem_path_nonexistent(tl_entries_dir: Path, signing_key_and_cert) -> None:
    """CLI with non-existent path returns path as-is (_load_pem_from_env_or_path fallback)."""
    from tools.lotl.cli import main

    _, cert_path = signing_key_and_cert
    # Non-existent path: p.exists() is False, returns path_arg (inline PEM path)
    exit_code = main([
        "--signing-key", "/nonexistent/key.pem",
        "--signing-cert", str(cert_path),
        "--tl-entries-dir", str(tl_entries_dir),
        "--output-dir", str(tl_entries_dir),
    ])
    assert exit_code != 0  # Produce fails with invalid key


def test_cli_check_expiry_passes(tl_entries_dir: Path) -> None:
    """--check-expiry succeeds when all entry certificates are valid."""
    from tools.lotl.cli import main

    exit_code = main([
        "--check-expiry",
        "--tl-entries-dir", str(tl_entries_dir),
    ])
    assert exit_code == 0


def test_cli_check_expiry_fails_on_expired(
    tmp_path: Path, expired_cert_pem: str
) -> None:
    """--check-expiry fails when a trust_anchor is expired."""
    import json

    from tools.lotl.cli import main

    (tmp_path / "wallet-provider").mkdir()
    (tmp_path / "wallet-provider" / "expired.json").write_text(
        json.dumps({
            "tl_url": "https://example.com/tl.xml",
            "trust_anchor": expired_cert_pem,
        })
    )
    exit_code = main([
        "--check-expiry",
        "--tl-entries-dir", str(tmp_path),
    ])
    assert exit_code == 1


def test_cli_check_expiry_nothing_to_check(tmp_path: Path) -> None:
    """--check-expiry with no sources exits 1."""
    from tools.lotl.cli import main

    missing = tmp_path / "does-not-exist"
    exit_code = main([
        "--check-expiry",
        "--tl-entries-dir", str(missing),
    ])
    assert exit_code == 1


def test_cli_check_expiry_published_lotl(
    tmp_path: Path, valid_cert_pem: str
) -> None:
    """--check-expiry --lotl-json inspects pointer and signing certificates."""
    import base64
    import json

    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
    from tools.lotl.cli import main

    cert = x509.load_pem_x509_certificate(
        valid_cert_pem.encode(), default_backend()
    )
    der_b64 = base64.b64encode(
        cert.public_bytes(serialization.Encoding.DER)
    ).decode()
    header = json.dumps({"alg": "ES256", "x5c": [der_b64]})
    protected = base64.urlsafe_b64encode(header.encode()).decode().rstrip("=")
    lotl = {
        "signature": {"protected": protected, "signature": "x"},
        "LoTE": {
            "ListAndSchemeInformation": {
                "PointersToOtherLoTE": [
                    {
                        "LoTELocation": "https://example.com/tl.xml",
                        "ServiceDigitalIdentities": [
                            {"X509Certificates": [{"val": der_b64}]}
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
    lotl_path = tmp_path / "list_of_trusted_lists.json"
    lotl_path.write_text(json.dumps(lotl))
    exit_code = main([
        "--check-expiry",
        "--tl-entries-dir", str(tmp_path / "missing-entries"),
        "--lotl-json", str(lotl_path),
    ])
    assert exit_code == 0
