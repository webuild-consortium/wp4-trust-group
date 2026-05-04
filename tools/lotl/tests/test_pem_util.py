"""Tests for PEM normalization from CI secrets."""

from pathlib import Path

from jwcrypto import jwk

from tools.lotl.pem_util import normalize_pem_for_ci


def test_normalize_literal_newline_escapes(signing_key_and_cert: tuple[Path, Path]) -> None:
    """GitHub-style single-line secret with \\n sequences loads as PEM."""
    key_path, cert_path = signing_key_and_cert
    key_pem = key_path.read_text()
    cert_pem = cert_path.read_text()
    key_esc = key_pem.replace("\n", "\\n")
    cert_esc = cert_pem.replace("\n", "\\n")
    key_norm = normalize_pem_for_ci(key_esc)
    cert_norm = normalize_pem_for_ci(cert_esc)
    jwk.JWK.from_pem(key_norm.encode("utf-8"))
    jwk.JWK.from_pem(cert_norm.encode("utf-8"))


def test_normalize_idempotent_multiline(signing_key_and_cert: tuple[Path, Path]) -> None:
    """Second application does not change the first (line endings + outer strip only)."""
    key_path, _ = signing_key_and_cert
    key_pem = key_path.read_text()
    once = normalize_pem_for_ci(key_pem)
    assert normalize_pem_for_ci(once) == once


def test_normalize_strips_bom_and_quotes() -> None:
    pem = "-----BEGIN X-----\na\n-----END X-----"
    assert normalize_pem_for_ci("\ufeff" + pem) == pem
    assert normalize_pem_for_ci(f'"{pem}"') == pem
    assert normalize_pem_for_ci(f"'{pem}'") == pem


def test_normalize_crlf() -> None:
    pem = "-----BEGIN X-----\r\nline\r\n-----END X-----"
    assert normalize_pem_for_ci(pem) == "-----BEGIN X-----\nline\n-----END X-----"


def test_normalize_non_pem_passthrough() -> None:
    assert normalize_pem_for_ci("  hello  ") == "hello"
