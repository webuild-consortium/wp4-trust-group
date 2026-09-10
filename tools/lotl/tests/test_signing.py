"""Tests for XAdES and JAdES signing."""

import base64
import json
from pathlib import Path

import pytest
from lxml import etree

from tools.lotl.jades_signer import sign_json, verify_json
from tools.lotl.tests.mocks.tl_factory import make_mock_lotl_json
from tools.lotl.xades_signer import EXC_C14N, sign_xml, verify_xml

# Use xml_generator for XML content
from tools.lotl.xml_generator import generate_lotl_xml
from tools.lotl.tl_entry import TLEntry


def test_jades_sign_and_verify(signing_key_and_cert: tuple[Path, Path]) -> None:
    """JAdES sign and verify round-trip."""
    key_path, cert_path = signing_key_and_cert
    payload = make_mock_lotl_json(sequence=1)
    signed = sign_json(payload, key_path, cert_path)
    assert "signature" in signed

    sig = signed["signature"]

    # RFC 7515 §7.2.2: protected must be a base64url string, not a dict
    assert isinstance(sig["protected"], str), "protected must be a base64url string per RFC 7515 §7.2.2"

    # Decode protected header and verify iat is present as integer (TS 119 182-1 §5.1.11)
    padding = (4 - len(sig["protected"]) % 4) % 4
    header = json.loads(base64.urlsafe_b64decode(sig["protected"] + "=" * padding))
    assert "iat" in header, "iat must be present in protected header (TS 119 182-1 §5.1.11)"
    assert isinstance(header["iat"], int), "iat must be an integer Unix timestamp"
    assert header["iat"] > 0

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


def test_xades_verify_requires_trust_anchor(signing_key_and_cert: tuple[Path, Path]) -> None:
    """Without an anchor signxml falls back to the certifi CA bundle.
    """
    key_path, cert_path = signing_key_and_cert
    signed = sign_xml(generate_lotl_xml([], sequence_number=1), key_path, cert_path)

    with pytest.raises(ValueError, match="trust anchor"):
        verify_xml(signed)

    # Either anchor on its own is accepted.
    assert verify_xml(signed, cert_pem=cert_path.read_bytes())
    assert verify_xml(signed, ca_pem_file=cert_path)


def test_jades_verify_invalid_fails() -> None:
    """Verify tampered payload fails."""
    payload = {"x": 1, "signature": {"protected": {}, "signature": "bad", "header": {"x5c": []}}}
    with pytest.raises(ValueError):
        verify_json(payload)


DS = "http://www.w3.org/2000/09/xmldsig#"
XADES = "http://uri.etsi.org/01903/v1.3.2#"
NS = {"ds": DS, "xades": XADES}
TSL_MIME_TYPE = "application/vnd.etsi.tsl+xml"


@pytest.fixture
def signed_lotl(signing_key_and_cert: tuple[Path, Path]) -> etree._Element:
    """A signed LoTL, parsed, for structural assertions."""
    key_path, cert_path = signing_key_and_cert
    xml_bytes = generate_lotl_xml([], sequence_number=1)
    return etree.fromstring(sign_xml(xml_bytes, key_path, cert_path))


def test_xades_has_qualifying_properties(signed_lotl: etree._Element) -> None:
    """ds:Object with QualifyingProperties

    EN 319 132-1 v1.3.1 clause 6.3 note 1 puts all qualifying properties in one
    QualifyingProperties element inside a ds:Object child of the signature.
    """
    assert len(signed_lotl.findall(".//ds:Object", NS)) == 1
    assert len(signed_lotl.findall(".//xades:QualifyingProperties", NS)) == 1
    assert len(signed_lotl.findall(".//xades:SignedProperties", NS)) == 1


def test_xades_references_all_declare_transforms(signed_lotl: etree._Element) -> None:
    """TS 119 612 Annex B.1.0 rule 3 / EN 319 132-1 Table 2.

     _add_reference_to_signed_info override
    """
    references = signed_lotl.findall(".//ds:SignedInfo/ds:Reference", NS)
    assert len(references) == 3, "expected document, SignedProperties and KeyInfo"
    for reference in references:
        assert reference.find("ds:Transforms", NS) is not None, (
            f"ds:Reference URI={reference.get('URI')} declares no ds:Transforms"
        )


def test_xades_document_reference_targets_the_root(signed_lotl: etree._Element) -> None:
    """TS 119 612 Annex B.1.0 rules 2, 2a and 2b.

    The reference over the list must name the TrustServiceStatusList (not URI="")
    """
    root_id = signed_lotl.get("Id")
    assert root_id, "root element carries no Id to reference"

    references = signed_lotl.findall(".//ds:SignedInfo/ds:Reference", NS)
    document_references = [r for r in references if r.get("URI") == f"#{root_id}"]
    assert len(document_references) == 1, f"no ds:Reference targets #{root_id}"

    transforms = document_references[0].findall("ds:Transforms", NS)
    assert len(transforms) == 1, "rule 2a: exactly one ds:Transforms"
    algorithms = [t.get("Algorithm") for t in transforms[0].findall("ds:Transform", NS)]
    assert algorithms == [
        "http://www.w3.org/2000/09/xmldsig#enveloped-signature",
        EXC_C14N,
    ], f"rule 2b: enveloped then exclusive c14n, got {algorithms}"


def test_xades_canonicalization_is_exclusive(signed_lotl: etree._Element) -> None:
    """TS 119 612 Annex B.1.0 rule 3, and EN 319 132-1 Table 2 note e"""
    methods = signed_lotl.findall(".//ds:SignedInfo/ds:CanonicalizationMethod", NS)
    assert len(methods) == 1
    assert methods[0].get("Algorithm") == EXC_C14N


def test_xades_sign_requires_root_id(signing_key_and_cert: tuple[Path, Path]) -> None:
    """A root without an Id yields URI="", which Annex B.1.0 rule 2 disallows."""
    key_path, cert_path = signing_key_and_cert
    without_id = b'<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#"/>'

    with pytest.raises(ValueError, match="Id attribute"):
        sign_xml(without_id, key_path, cert_path)


def test_xades_signing_time_is_utc_without_fraction(signed_lotl: etree._Element) -> None:
    """TS 119 612 clause 5.1.3: trailing "Z", no fractional seconds."""
    signing_times = signed_lotl.findall(".//xades:SigningTime", NS)
    assert len(signing_times) == 1
    value = signing_times[0].text
    assert value.endswith("Z"), value
    assert "." not in value, value


def test_xades_signing_certificate_v2(signed_lotl: etree._Element) -> None:
    """Table 2 requires SigningCertificateV2; notes i and j constrain its content."""
    certs_v2 = signed_lotl.findall(".//xades:SigningCertificateV2", NS)
    assert len(certs_v2) == 1
    assert not signed_lotl.findall(".//xades:SigningCertificate", NS), "legacy form"
    for cert in signed_lotl.findall(".//xades:SigningCertificateV2/xades:Cert", NS):
        assert "URI" not in cert.keys(), "note i: xades:Cert shall carry no @URI"
    assert not signed_lotl.findall(".//xades:IssuerSerialV2", NS), "note j"


def test_xades_data_object_format(signed_lotl: etree._Element) -> None:
    """Table 2 note k, with the media type TS 119 612 clause 6.2.2 registers."""
    formats = signed_lotl.findall(".//xades:DataObjectFormat", NS)
    assert len(formats) == 1
    assert formats[0].findtext("xades:MimeType", namespaces=NS) == TSL_MIME_TYPE

    # ObjectReference must point at a real ds:Reference (EN 319 132-1 clause 5.2.4).
    target = formats[0].get("ObjectReference")
    assert target.startswith("#")
    referenced = [r.get("Id") for r in signed_lotl.findall(".//ds:Reference", NS)]
    assert target[1:] in referenced
