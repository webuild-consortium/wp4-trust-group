"""Tests for XML generator (TS 119 612 compiled LoTL)."""

import pytest
from lxml import etree

from tools.lotl.settings import (
    LOTL_HISTORICAL_INFORMATION_PERIOD,
    LOTL_SCHEME_RULES_URI,
    LOTL_TSL_TYPE_URI,
    LOTL_XML_FILENAME,
    NS_TSL,
    NS_TSL_ADDITIONAL,
    TSL_TAG_URI,
)
from tools.lotl.tl_entry import TLEntry
from tools.lotl.xml_generator import generate_lotl_xml

NS = {"tsl": NS_TSL, "tslx": NS_TSL_ADDITIONAL}
NS_XML = "http://www.w3.org/XML/1998/namespace"


def _root(xml: bytes) -> etree._Element:
    return etree.fromstring(xml)


def test_generate_empty() -> None:
    """Generate LoTL XML with no entries (unsigned compiled-list skeleton)."""
    xml = generate_lotl_xml([], sequence_number=1)
    root = _root(xml)
    assert root.tag == f"{{{NS_TSL}}}TrustServiceStatusList"
    assert root.get("Id") == "lotl-1"
    assert root.get("TSLTag") == TSL_TAG_URI
    assert root.findtext("tsl:SchemeInformation/tsl:TSLSequenceNumber", namespaces=NS) == "1"
    assert root.findtext("tsl:SchemeInformation/tsl:TSLType", namespaces=NS) == LOTL_TSL_TYPE_URI
    assert root.find("tsl:SchemeInformation/tsl:PointersToOtherTSL", namespaces=NS) is None
    assert root.find("tsl:TrustServiceProviderList", namespaces=NS) is None


def test_generate_with_entries(sample_tl_entry: TLEntry) -> None:
    """Member TLs become OtherTSLPointer, not DistributionPoint."""
    xml = generate_lotl_xml([sample_tl_entry], sequence_number=2)
    root = _root(xml)
    assert root.findtext("tsl:SchemeInformation/tsl:TSLSequenceNumber", namespaces=NS) == "2"
    assert root.findtext("tsl:SchemeInformation/tsl:TSLType", namespaces=NS) == LOTL_TSL_TYPE_URI
    assert (
        root.findtext(
            "tsl:SchemeInformation/tsl:SchemeTypeCommunityRules/tsl:URI",
            namespaces=NS,
        )
        == LOTL_SCHEME_RULES_URI
    )
    assert (
        root.findtext(
            "tsl:SchemeInformation/tsl:HistoricalInformationPeriod",
            namespaces=NS,
        )
        == str(LOTL_HISTORICAL_INFORMATION_PERIOD)
    )

    scheme_uri = root.find(
        "tsl:SchemeInformation/tsl:SchemeInformationURI/tsl:URI", namespaces=NS
    )
    assert scheme_uri is not None
    assert scheme_uri.get(f"{{{NS_XML}}}lang") == "en"

    eaddr = root.find(
        "tsl:SchemeInformation/tsl:SchemeOperatorAddress/tsl:ElectronicAddress/tsl:URI",
        namespaces=NS,
    )
    assert eaddr is not None
    assert eaddr.text.startswith("https://")
    assert eaddr.get(f"{{{NS_XML}}}lang") == "en"

    next_dt = root.findtext(
        "tsl:SchemeInformation/tsl:NextUpdate/tsl:dateTime", namespaces=NS
    )
    assert next_dt and next_dt.endswith("Z")

    pointers = root.findall(
        "tsl:SchemeInformation/tsl:PointersToOtherTSL/tsl:OtherTSLPointer",
        namespaces=NS,
    )
    assert len(pointers) == 2
    locations = [p.findtext("tsl:TSLLocation", namespaces=NS) for p in pointers]
    assert sample_tl_entry.get_tl_url_json() in locations
    assert sample_tl_entry.get_tl_url_xml() in locations

    certs = root.findall(".//tsl:X509Certificate", namespaces=NS)
    assert certs and all((c.text or "").strip() for c in certs)

    tsl_types = [
        t.text
        for t in root.findall(
            ".//tsl:AdditionalInformation/tsl:OtherInformation/tsl:TSLType",
            namespaces=NS,
        )
    ]
    assert "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList" in tsl_types

    mimes = [
        m.text
        for m in root.findall(
            ".//tsl:AdditionalInformation/tsl:OtherInformation/tslx:MimeType",
            namespaces=NS,
        )
    ]
    assert "application/json" in mimes
    assert "application/xml" in mimes

    dps = [
        u.text
        for u in root.findall(
            "tsl:SchemeInformation/tsl:DistributionPoints/tsl:URI", namespaces=NS
        )
    ]
    assert any((u or "").endswith(LOTL_XML_FILENAME) for u in dps)
    assert sample_tl_entry.tl_url not in dps
    assert sample_tl_entry.get_tl_url_xml() not in dps
    assert root.find(".//tsl:DistributionPoint", namespaces=NS) is None
    assert root.find("tsl:TrustServiceProviderList", namespaces=NS) is None


def test_generate_custom_distribution_points(sample_tl_entry: TLEntry) -> None:
    """Caller-supplied distribution URIs are used as-is."""
    xml = generate_lotl_xml(
        [sample_tl_entry],
        sequence_number=1,
        distribution_point_uris=[
            "https://example.test/list_of_trusted_lists.xml",
        ],
    )
    root = _root(xml)
    dps = [
        u.text
        for u in root.findall(
            "tsl:SchemeInformation/tsl:DistributionPoints/tsl:URI", namespaces=NS
        )
    ]
    assert dps == ["https://example.test/list_of_trusted_lists.xml"]


def test_generate_rejects_missing_trust_anchor(sample_tl_entry: TLEntry) -> None:
    """Pointer construction requires a usable X.509 trust_anchor."""
    bad = TLEntry(
        tl_type=sample_tl_entry.tl_type,
        participant_id=sample_tl_entry.participant_id,
        tl_url=sample_tl_entry.tl_url,
        trust_anchor="not-a-cert",
        metadata=sample_tl_entry.metadata,
    )
    with pytest.raises(ValueError, match="trust_anchor"):
        generate_lotl_xml([bad], sequence_number=1)
