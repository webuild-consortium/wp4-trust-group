"""Tests for publishing the LoTL signing public key."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from jwcrypto import jwk, jws
from lxml import html

from tools.lotl.build_pages import build_pages
from tools.lotl.jades_signer import sign_json
from tools.lotl.producer import produce
from tools.lotl.xades_signer import verify_xml


@pytest.fixture
def signed_lotl(tl_entries_dir, tmp_path, signing_key_and_cert):
    key_path, cert_path = signing_key_and_cert
    output = tmp_path / "lotl"
    assert produce(tl_entries_dir, output, key_path.read_text(), cert_path.read_text()) == 0
    return output, key_path, cert_path


def test_build_page_and_public_files_match_signed_artifacts(signed_lotl, tmp_path, monkeypatch):
    lotl, key_path, cert_path = signed_lotl
    output = tmp_path / "pages"
    template = Path("lotl/pages/index.html")
    # Even if the certificate input contains extra private-key material, only
    # re-serialized public information may be published.
    monkeypatch.setenv("LOTL_SIGNING_CERT", cert_path.read_text() + key_path.read_text())
    subprocess.run(
        [
            sys.executable, "-m", "tools.lotl.build_pages",
            "--template", str(template),
            "--signed-json", str(lotl / "list_of_trusted_lists.json"),
            "--output-dir", str(output),
        ],
        check=True, capture_output=True, text=True,
    )

    cert = x509.load_pem_x509_certificate(cert_path.read_bytes())
    public_key = cert.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
    )
    page = (output / "index.html").read_text(encoding="utf-8")
    assert public_key.decode("ascii").strip() in page
    assert cert.fingerprint(hashes.SHA256()).hex().upper() in page
    assert cert.not_valid_after_utc.strftime("%Y-%m-%d %H:%M:%S UTC") in page
    document = html.fromstring(page)
    assert document.xpath('//a[@href="lotl-signing-cert.pem"]')
    assert document.xpath('//a[@href="lotl-signing-public-key.pem"]')
    assert "LOTL_SIGNING_" not in page
    assert (output / "lotl-signing-cert.pem").read_bytes() == cert_path.read_bytes()
    assert (output / "lotl-signing-public-key.pem").read_bytes() == public_key
    for path in output.iterdir():
        assert b"PRIVATE KEY" not in path.read_bytes()

    token = jws.JWS()
    token.deserialize((lotl / "list_of_trusted_lists.jws").read_text(encoding="ascii"))
    token.verify(jwk.JWK.from_pem(public_key))
    assert verify_xml((lotl / "list_of_trusted_lists.xml").read_bytes(), cert_pem=cert_path)


def test_build_page_rejects_mismatched_certificate(signed_lotl, tmp_path, valid_cert_pem):
    lotl, _, _ = signed_lotl
    with pytest.raises(ValueError, match="does not match"):
        build_pages(
            Path("lotl/pages/index.html"), lotl / "list_of_trusted_lists.json",
            tmp_path / "pages", valid_cert_pem.encode(),
        )
    assert not (tmp_path / "pages").exists()


def test_build_page_rejects_tampering_and_missing_placeholder(signed_lotl, tmp_path):
    lotl, _, cert_path = signed_lotl
    source = lotl / "list_of_trusted_lists.json"
    payload = json.loads(source.read_text())
    payload["LoTE"]["ListAndSchemeInformation"]["LoTESequenceNumber"] += 1
    source.write_text(json.dumps(payload))
    with pytest.raises(jws.InvalidJWSSignature, match="Verification failed"):
        build_pages(Path("lotl/pages/index.html"), source, tmp_path / "pages", cert_path.read_bytes())
    assert not (tmp_path / "pages").exists()

    # Restore a valid signature and use a broken page template.
    key_path = signed_lotl[1]
    source.write_text(json.dumps(sign_json({"test": True}, key_path, cert_path)))
    template = tmp_path / "template.html"
    template.write_text("missing placeholders")
    with pytest.raises(ValueError, match="placeholder"):
        build_pages(template, source, tmp_path / "pages", cert_path.read_bytes())
    assert not (tmp_path / "pages").exists()


def test_build_page_cli_requires_certificate(signed_lotl, tmp_path):
    lotl, _, _ = signed_lotl
    env = dict(os.environ)
    env.pop("LOTL_SIGNING_CERT", None)
    result = subprocess.run(
        [
            sys.executable, "-m", "tools.lotl.build_pages",
            "--template", "lotl/pages/index.html",
            "--signed-json", str(lotl / "list_of_trusted_lists.json"),
            "--output-dir", str(tmp_path / "pages"),
        ],
        capture_output=True, text=True, env=env,
    )
    assert result.returncode != 0
    assert "LOTL_SIGNING_CERT must contain" in result.stderr
