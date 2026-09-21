"""Tests for LoTL profile rules: pointer MimeType, operator address, scheme name."""

import pytest
from lxml import etree

from tools.lotl.json_generator import generate_lotl_json
from tools.lotl.lote_validate import validate_lote_json
from tools.lotl.lotl_profile import (
    electronic_address_errors,
    pointer_mime_type_errors,
    postal_address_errors,
    scheme_name_errors,
)
from tools.lotl.settings import (
    MIME_LOTE_JSON,
    MIME_LOTE_XML,
    MIME_TSL_XML,
    NS_TSL,
    NS_TSL_ADDITIONAL,
    TSL_TYPE_EU_GENERIC,
)
from tools.lotl.tl_entry import TLEntry
from tools.lotl.xml_generator import generate_lotl_xml
from tools.lotl.xml_validate import validate_lotl_xml, validate_lotl_xml_semantics

NS = {"tsl": NS_TSL, "tslx": NS_TSL_ADDITIONAL}


def _entry(sample: TLEntry, tl_type: str, tl_url: str) -> TLEntry:
    return TLEntry(
        tl_type=tl_type,
        participant_id=sample.participant_id,
        tl_url=tl_url,
        trust_anchor=sample.trust_anchor,
        metadata=sample.metadata,
    )


def _qeaa(sample: TLEntry) -> TLEntry:
    return _entry(sample, "qeaa-provider", "https://example.com/NXD-TL-QEAA.xml")


def _qualifiers(doc: dict) -> list[dict]:
    ptrs = doc["LoTE"]["ListAndSchemeInformation"]["PointersToOtherLoTE"]
    return [p["LoTEQualifiers"][0] for p in ptrs]


def test_json_and_xml_urls_get_their_own_mime_type(sample_tl_entry: TLEntry) -> None:
    quals = _qualifiers(generate_lotl_json([sample_tl_entry]))
    assert [q["MimeType"] for q in quals] == [MIME_LOTE_JSON, MIME_LOTE_XML]
    assert all(
        set(q) == {"LoTEType", "SchemeOperatorName", "SchemeTerritory", "MimeType"} for q in quals
    )


def test_xml_only_lote_is_one_xml_pointer(sample_tl_entry: TLEntry) -> None:
    entry = _entry(sample_tl_entry, "pid-provider", "https://example.com/etsi/tl.xml")
    (qualifier,) = _qualifiers(generate_lotl_json([entry]))
    assert qualifier["MimeType"] == MIME_LOTE_XML


def test_qeaa_trusted_list_is_tsl_xml(sample_tl_entry: TLEntry) -> None:
    (qualifier,) = _qualifiers(generate_lotl_json([_qeaa(sample_tl_entry)]))
    assert qualifier["LoTEType"] == TSL_TYPE_EU_GENERIC
    assert qualifier["MimeType"] == MIME_TSL_XML


@pytest.mark.parametrize(
    ("tl_type", "url"),
    [
        ("qeaa-provider", "https://example.com/tl.json"),
        ("pid-provider", "https://example.com/tl"),
    ],
)
def test_underivable_mime_type_is_rejected(
    sample_tl_entry: TLEntry, tl_type: str, url: str
) -> None:
    with pytest.raises(ValueError, match="MimeType"):
        generate_lotl_json([_entry(sample_tl_entry, tl_type, url)])


def test_xml_pointer_qualifiers(sample_tl_entry: TLEntry) -> None:
    """TS 119 612 clause 5.3.13 c) qualifiers, except scheme type/community/rules."""
    xml = generate_lotl_xml([_qeaa(sample_tl_entry)])
    info = etree.fromstring(xml).find(
        ".//tsl:OtherTSLPointer/tsl:AdditionalInformation", namespaces=NS
    )
    assert [etree.QName(oi[0]).localname for oi in info] == [
        "TSLType",
        "SchemeOperatorName",
        "SchemeTerritory",
        "MimeType",
    ]
    assert info.findtext("tsl:OtherInformation/tslx:MimeType", namespaces=NS) == MIME_TSL_XML
    assert validate_lotl_xml(xml) == []


def test_xml_declares_namespaces_once_on_root(sample_tl_entry: TLEntry) -> None:
    xml = generate_lotl_xml([sample_tl_entry])
    assert b"ns0" not in xml
    assert xml.count(b"xmlns:tslx=") == 1


def test_operator_address_and_scheme_name(sample_tl_entry: TLEntry) -> None:
    root = etree.fromstring(
        generate_lotl_xml(
            [sample_tl_entry],
            scheme_operator_email="help@example.org",
            scheme_operator_website="https://example.org/contact",
        )
    )
    uris = [
        u.text
        for u in root.findall(
            ".//tsl:SchemeOperatorAddress/tsl:ElectronicAddress/tsl:URI", namespaces=NS
        )
    ]
    assert uris == ["mailto:help@example.org", "https://example.org/contact"]
    assert root.findtext(".//tsl:PostalAddress/tsl:StreetAddress", namespaces=NS) != "N/A"
    assert (
        root.findtext("tsl:SchemeInformation/tsl:SchemeName/tsl:Name", namespaces=NS)
        == "EU:WP4 List of Trusted Lists"
    )

    lasi = generate_lotl_json([sample_tl_entry])["LoTE"]["ListAndSchemeInformation"]
    eaddr = lasi["SchemeOperatorAddress"]["SchemeOperatorElectronicAddress"]
    assert eaddr[0]["uriValue"].startswith("mailto:")
    assert eaddr[1]["uriValue"].startswith("https://")
    assert lasi["SchemeName"][0]["value"] == "EU:WP4 List of Trusted Lists"


def test_xml_validator_rejects_profile_violations(sample_tl_entry: TLEntry) -> None:
    root = etree.fromstring(generate_lotl_xml([sample_tl_entry]))
    si = root.find("tsl:SchemeInformation", namespaces=NS)
    elec = si.find("tsl:SchemeOperatorAddress/tsl:ElectronicAddress", namespaces=NS)
    elec.remove(elec[0])
    si.find(".//tsl:PostalAddress/tsl:StreetAddress", namespaces=NS).text = "N/A"
    si.find("tsl:SchemeName/tsl:Name", namespaces=NS).text = "WP4 List of Trusted Lists"
    root.find(".//tslx:MimeType", namespaces=NS).text = "text/plain"

    joined = " ".join(validate_lotl_xml_semantics(root))
    assert "5.3.5.2" in joined
    assert "5.3.5.1" in joined
    assert "5.3.6" in joined
    assert "'text/plain'" in joined


def test_json_validator_rejects_profile_violations(sample_tl_entry: TLEntry) -> None:
    doc = generate_lotl_json([sample_tl_entry])
    lasi = doc["LoTE"]["ListAndSchemeInformation"]
    lasi["SchemeOperatorAddress"]["SchemeOperatorElectronicAddress"].pop(0)
    lasi["SchemeOperatorAddress"]["SchemeOperatorPostalAddress"][0]["StreetAddress"] = (
        "Not specified"
    )
    lasi["SchemeName"][0]["value"] = "WP4 List of Trusted Lists"
    _qualifiers(doc)[0]["MimeType"] = MIME_TSL_XML

    joined = " ".join(validate_lote_json(doc))
    assert "5.3.5.2" in joined
    assert "5.3.5.1" in joined
    assert "5.3.6" in joined
    assert "points to a TS 119 602 LoTE" in joined


def test_json_validator_rejects_empty_electronic_address(sample_tl_entry: TLEntry) -> None:
    doc = generate_lotl_json([sample_tl_entry])
    doc["LoTE"]["ListAndSchemeInformation"]["SchemeOperatorAddress"][
        "SchemeOperatorElectronicAddress"
    ] = []
    assert any("mailto" in e for e in validate_lote_json(doc))


def test_validators_require_tsl_mime_type_for_qeaa(sample_tl_entry: TLEntry) -> None:
    entry = _qeaa(sample_tl_entry)
    doc = generate_lotl_json([entry])
    _qualifiers(doc)[0]["MimeType"] = MIME_LOTE_XML
    assert any("points to a TS 119 612 trusted list" in e for e in validate_lote_json(doc))

    root = etree.fromstring(generate_lotl_xml([entry]))
    root.find(".//tslx:MimeType", namespaces=NS).text = MIME_LOTE_XML
    errors = validate_lotl_xml_semantics(root)
    assert any("points to a TS 119 612 trusted list" in e for e in errors)


def test_electronic_address_rules() -> None:
    assert electronic_address_errors(["mailto:a@b.eu", "https://b.eu", "tel:+3221234"], "E") == []
    assert electronic_address_errors(["https://b.eu", "mailto:a@b.eu"], "E")
    assert electronic_address_errors(["mailto:a@b.eu", "https://b.eu", "+3221234"], "E")
    assert electronic_address_errors(["mailto:a@b.eu", "https://b.eu", "tel:1", "tel:2"], "E")


def test_postal_address_rules() -> None:
    assert postal_address_errors({"StreetAddress": "Rue 1", "CountryName": "BE"}, "P") == []
    assert postal_address_errors({"CountryName": "Belgium"}, "P")
    assert postal_address_errors({"Locality": None}, "P")


def test_scheme_name_rules() -> None:
    assert scheme_name_errors(["EU:Name"], "EU") == []
    assert scheme_name_errors(["EU:"], "EU")
    assert scheme_name_errors([], "EU")


def test_pointer_mime_type_with_unknown_list_type_checks_value_only() -> None:
    assert pointer_mime_type_errors("P", "https://example.com/type", [MIME_LOTE_JSON]) == []
    assert pointer_mime_type_errors("P", None, ["text/plain"])
