"""Tests for unsigned LoTL XML validation (XSD + semantics)."""

from lxml import etree

from tools.lotl.settings import LOTL_TSL_TYPE_URI, NS_TSL
from tools.lotl.tl_entry import TLEntry
from tools.lotl.xml_generator import generate_lotl_xml
from tools.lotl.xml_validate import (
    get_tsl_xsd_path,
    validate_against_xsd,
    validate_lotl_xml,
    validate_lotl_xml_semantics,
)

NS = {"tsl": NS_TSL}


def test_validate_empty_lotl_fails_missing_pointers() -> None:
    xml = generate_lotl_xml([], sequence_number=1)
    errors = validate_lotl_xml(xml)
    assert any("OtherTSLPointer" in e for e in errors)


def test_validate_sample_entries_passes(sample_tl_entry: TLEntry) -> None:
    xml = generate_lotl_xml([sample_tl_entry], sequence_number=2)
    assert validate_lotl_xml(xml) == []


def test_xsd_accepts_generated_lotl(sample_tl_entry: TLEntry) -> None:
    xml = generate_lotl_xml([sample_tl_entry], sequence_number=1)
    assert get_tsl_xsd_path().is_file()
    assert validate_against_xsd(xml) == []


def test_validate_rejects_wrong_tsl_type(sample_tl_entry: TLEntry) -> None:
    root = etree.fromstring(generate_lotl_xml([sample_tl_entry], sequence_number=1))
    tsl_type = root.find("tsl:SchemeInformation/tsl:TSLType", namespaces=NS)
    assert tsl_type is not None
    tsl_type.text = "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric"
    errors = validate_lotl_xml(etree.tostring(root))
    assert any("EUlistofthelists" in e or LOTL_TSL_TYPE_URI in e for e in errors)


def test_validate_rejects_tsp_list(sample_tl_entry: TLEntry) -> None:
    root = etree.fromstring(generate_lotl_xml([sample_tl_entry], sequence_number=1))
    etree.SubElement(root, f"{{{NS_TSL}}}TrustServiceProviderList")
    errors = validate_lotl_xml_semantics(root)
    assert any("TrustServiceProviderList" in e for e in errors)


def test_validate_rejects_unknown_pointer_type(sample_tl_entry: TLEntry) -> None:
    root = etree.fromstring(generate_lotl_xml([sample_tl_entry], sequence_number=1))
    tsl_type = root.find(
        ".//tsl:AdditionalInformation/tsl:OtherInformation/tsl:TSLType",
        namespaces=NS,
    )
    assert tsl_type is not None
    tsl_type.text = "https://example.com/unknown-type"
    errors = validate_lotl_xml_semantics(root)
    assert any("not a known" in e for e in errors)


def test_validate_rejects_malformed_xml() -> None:
    errors = validate_lotl_xml(b"<not-xml")
    assert any("not well-formed" in e for e in errors)


def test_validate_rejects_wrong_root() -> None:
    errors = validate_lotl_xml_semantics(etree.fromstring(b"<foo/>"))
    assert any("Root element" in e for e in errors)


def test_xsd_missing_file_reports_error(monkeypatch, tmp_path) -> None:
    from tools.lotl import xml_validate

    monkeypatch.setattr(xml_validate, "get_tsl_xsd_path", lambda: tmp_path / "missing.xsd")
    errors = validate_against_xsd(b"<TrustServiceStatusList/>")
    assert any("not found" in e for e in errors)


def test_xsd_rejects_missing_required_attribute(sample_tl_entry: TLEntry) -> None:
    root = etree.fromstring(generate_lotl_xml([sample_tl_entry], sequence_number=1))
    del root.attrib["TSLTag"]
    errors = validate_against_xsd(etree.tostring(root))
    assert errors
    assert any("TSLTag" in e or "XSD:" in e for e in errors)


def test_semantics_cover_required_lotl_fields(sample_tl_entry: TLEntry) -> None:
    root = etree.fromstring(generate_lotl_xml([sample_tl_entry], sequence_number=1))
    del root.attrib["Id"]
    del root.attrib["TSLTag"]
    hip = root.find("tsl:SchemeInformation/tsl:HistoricalInformationPeriod", namespaces=NS)
    assert hip is not None
    hip.text = "0"
    next_el = root.find("tsl:SchemeInformation/tsl:NextUpdate", namespaces=NS)
    assert next_el is not None
    for child in list(next_el):
        next_el.remove(child)
    dps = root.find("tsl:SchemeInformation/tsl:DistributionPoints", namespaces=NS)
    assert dps is not None
    for child in list(dps):
        dps.remove(child)
    loc = root.find(".//tsl:TSLLocation", namespaces=NS)
    assert loc is not None
    loc.text = ""
    cert = root.find(".//tsl:X509Certificate", namespaces=NS)
    assert cert is not None
    cert.text = ""
    mime = root.find(
        ".//tsl:AdditionalInformation/tsl:OtherInformation/{http://uri.etsi.org/02231/v2/additionaltypes#}MimeType",
        namespaces=NS,
    )
    if mime is not None:
        mime.text = ""
    errors = validate_lotl_xml_semantics(root)
    joined = " ".join(errors)
    assert "Id" in joined
    assert "TSLTag" in joined
    assert "HistoricalInformationPeriod" in joined
    assert "NextUpdate" in joined
    assert "DistributionPoints" in joined
    assert "TSLLocation" in joined
    assert "X509Certificate" in joined
