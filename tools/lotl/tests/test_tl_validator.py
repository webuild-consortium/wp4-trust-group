"""Tests for tl_validator (fetch and validate TL)."""

import json
from unittest.mock import patch

import pytest

from tools.lotl.jades_signer import sign_json
from tools.lotl.tests.mocks.tl_factory import make_mock_lotl_json
from tools.lotl.tl_entry import TLEntry
from tools.lotl.tl_validator import (
    fetch_tl,
    validate_tl_entry,
    validate_tl_signature_json,
    validate_tl_signature_xml,
)
from tools.lotl.xml_generator import generate_lotl_xml
from tools.lotl.xades_signer import sign_xml


def test_validate_tl_signature_json_valid(signing_key_and_cert) -> None:
    """Valid JAdES signature passes."""
    key_path, cert_path = signing_key_and_cert
    payload = make_mock_lotl_json()
    signed = sign_json(payload, key_path.read_bytes(), cert_path.read_bytes())
    valid, err = validate_tl_signature_json(json.dumps(signed), cert_path.read_text())
    assert valid
    assert not err


def test_validate_tl_signature_json_invalid() -> None:
    """Invalid JSON signature fails."""
    valid, err = validate_tl_signature_json(
        '{"x":1}', "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----"
    )
    assert not valid
    assert err


def test_validate_tl_signature_xml_valid(signing_key_and_cert) -> None:
    """Valid XAdES signature passes."""
    key_path, cert_path = signing_key_and_cert
    xml = generate_lotl_xml([], sequence_number=1)
    signed = sign_xml(xml, key_path, cert_path)
    valid, err = validate_tl_signature_xml(signed, cert_path.read_text())
    assert valid
    assert not err


def test_validate_tl_entry_no_fetch(sample_tl_entry: TLEntry) -> None:
    """validate_tl_entry with fetch_and_validate=False passes."""
    valid, errors = validate_tl_entry(sample_tl_entry, fetch_and_validate=False)
    assert valid
    assert not errors


@patch("tools.lotl.tl_validator.fetch_tl")
def test_validate_tl_entry_fetch_fails(mock_fetch, sample_tl_entry: TLEntry) -> None:
    """validate_tl_entry when fetch fails returns invalid."""
    mock_fetch.return_value = (None, None, None)
    valid, errors = validate_tl_entry(sample_tl_entry, fetch_and_validate=True)
    assert not valid
    assert any("Failed to fetch" in e for e in errors)
