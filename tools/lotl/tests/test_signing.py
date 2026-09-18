"""Tests for XAdES and JAdES signing."""

import base64
import copy
import json
from pathlib import Path

import pytest
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
from lxml import etree

from signxml.exceptions import InvalidSignature

from tools.lotl.jades_signer import sign_json, verify_json
from tools.lotl.tests.mocks.tl_factory import make_mock_lotl_json
from tools.lotl.xades_signer import EXC_C14N, _parse, sign_xml, verify_xml

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
from tools.lotl.settings import NS_TSL as TSL
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


def test_xades_parser_rejects_external_entities(tmp_path: Path) -> None:
    """A LoTL may come from a remote publisher: no XXE, no entity expansion."""
    secret = tmp_path / "secret.txt"
    secret.write_text("classified")

    xxe = f"""<?xml version="1.0"?>
<!DOCTYPE TrustServiceStatusList [ <!ENTITY xxe SYSTEM "file://{secret}"> ]>
<TrustServiceStatusList Id="lotl">&xxe;</TrustServiceStatusList>""".encode()

    try:
        root = _parse(xxe)
    except etree.XMLSyntaxError:
        return  # The undefined entity was refused outright, which is also fine.
    assert "classified" not in (etree.tostring(root, encoding="unicode"))


def _take_document_reference(root: etree._Element) -> etree._Element:
    """Detach the ds:Reference covering the list from SignedInfo and return it."""
    signed_info = root.find(f"{{{DS}}}Signature/{{{DS}}}SignedInfo")
    document_reference = next(
        r
        for r in signed_info.findall(f"{{{DS}}}Reference")
        if r.get("URI") == f"#{root.get('Id')}"
    )
    signed_info.remove(document_reference)
    return document_reference


def _resign(root: etree._Element, key_path: Path) -> bytes:
    """Recompute ds:SignatureValue after SignedInfo was edited.

    ECDSA P-256, and XMLDSig wants the raw r||s pair rather than the DER structure.
    """
    signature = root.find(f"{{{DS}}}Signature")
    c14n = etree.tostring(
        signature.find(f"{{{DS}}}SignedInfo"), method="c14n", exclusive=True
    )
    key = serialization.load_pem_private_key(key_path.read_bytes(), password=None)
    r, s = decode_dss_signature(key.sign(c14n, ec.ECDSA(hashes.SHA256())))
    raw = r.to_bytes(32, "big") + s.to_bytes(32, "big")
    signature.find(f"{{{DS}}}SignatureValue").text = base64.b64encode(raw).decode()
    return etree.tostring(root)


def _resign_with_document_reference_last(signed: bytes, key_path: Path) -> bytes:
    """Re-sign a LoTL with the document ds:Reference moved to the end.

    Reference order is the publisher's choice, and a validly signed list may put
    the reference covering the list itself anywhere among the others.
    """
    root = etree.fromstring(signed)
    signed_info = root.find(f"{{{DS}}}Signature/{{{DS}}}SignedInfo")
    signed_info.append(_take_document_reference(root))
    return _resign(root, key_path)


def _resign_without_document_reference(signed: bytes, key_path: Path) -> bytes:
    """Re-sign a LoTL whose signature no longer covers the list itself."""
    root = etree.fromstring(signed)
    _take_document_reference(root)
    return _resign(root, key_path)


def test_xades_verify_returns_the_list_not_a_fragment(
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """The reference covering the root is chosen by Id, not by position.

    signxml returns one result per ds:Reference, so results[0] is whichever
    reference the publisher happened to put first -- here, SignedProperties.
    """
    key_path, cert_path = signing_key_and_cert
    signed = sign_xml(generate_lotl_xml([], sequence_number=1), key_path, cert_path)
    reordered = _resign_with_document_reference_last(signed, key_path)

    verified = etree.fromstring(verify_xml(reordered, ca_pem_file=cert_path))
    assert verified.tag == f"{{{TSL}}}TrustServiceStatusList", (
        f"verify returned {verified.tag}, not the trusted list"
    )
    assert verified.get("Id") == etree.fromstring(signed).get("Id")


def test_xades_verify_rejects_a_second_signature(
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """TS 119 612 Annex B.0 binds the schema: ds:Signature has maxOccurs="1".

    signxml verifies only the first ds:Signature, so a stapled-on second one
    would otherwise pass unnoticed.
    """
    key_path, cert_path = signing_key_and_cert
    signed = sign_xml(generate_lotl_xml([], sequence_number=1), key_path, cert_path)

    root = etree.fromstring(signed)
    root.append(copy.deepcopy(root.find(f"{{{DS}}}Signature")))

    with pytest.raises(InvalidSignature, match="exactly one signature"):
        verify_xml(etree.tostring(root), ca_pem_file=cert_path)


def test_xades_verify_requires_a_root_id(
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """Annex B.1.0 rule 2b: without an Id, no ds:Reference can name the list."""
    key_path, cert_path = signing_key_and_cert
    signed = sign_xml(generate_lotl_xml([], sequence_number=1), key_path, cert_path)

    root = etree.fromstring(signed)
    del root.attrib["Id"]

    with pytest.raises(InvalidSignature, match="no Id"):
        verify_xml(etree.tostring(root), ca_pem_file=cert_path)


def test_xades_verify_requires_a_reference_covering_the_list(
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """Annex B.1.0 rule 2: references over the signature's own properties only,
    however valid each digest is, sign nothing about the list."""
    key_path, cert_path = signing_key_and_cert
    signed = sign_xml(generate_lotl_xml([], sequence_number=1), key_path, cert_path)
    uncovered = _resign_without_document_reference(signed, key_path)

    with pytest.raises(InvalidSignature, match="covering the trusted list"):
        verify_xml(uncovered, ca_pem_file=cert_path, expect_references=2)


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
