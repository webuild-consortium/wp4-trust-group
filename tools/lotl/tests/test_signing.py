"""Tests for XAdES and JAdES signing."""

import json
from pathlib import Path

import pytest

from tools.lotl.jades_signer import sign_json, verify_json
from tools.lotl.tests.mocks.tl_factory import make_mock_lotl_json
from tools.lotl.xades_signer import sign_xml, verify_xml

# Use xml_generator for XML content
from tools.lotl.xml_generator import generate_lotl_xml
from tools.lotl.tl_entry import TLEntry


def test_jades_sign_and_verify(signing_key_and_cert: tuple[Path, Path]) -> None:
    """JAdES sign and verify round-trip."""
    key_path, cert_path = signing_key_and_cert
    payload = make_mock_lotl_json(sequence=1)
    signed = sign_json(payload, key_path, cert_path)
    assert "signature" in signed
    verified = verify_json(signed)
    assert "signature" not in verified
    assert verified["LoTE"]["ListAndSchemeInformation"]["LoTESequenceNumber"] == 1


def test_xades_sign_and_verify(signing_key_and_cert: tuple[Path, Path]) -> None:
    """XAdES sign and verify round-trip."""
    key_path, cert_path = signing_key_and_cert
    entries: list[TLEntry] = []
    xml_bytes = generate_lotl_xml(entries, sequence_number=1)
    signed = sign_xml(xml_bytes, key_path, cert_path)
    assert b"Signature" in signed
    # Use cert as CA for self-signed test cert (with required extensions)
    verified = verify_xml(signed, ca_pem_file=cert_path)
    assert verified


def test_jades_verify_invalid_fails() -> None:
    """Verify tampered payload fails."""
    payload = {"x": 1, "signature": {"protected": {}, "signature": "bad", "header": {"x5c": []}}}
    with pytest.raises(ValueError):
        verify_json(payload)
