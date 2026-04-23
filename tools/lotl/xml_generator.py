"""Generate LoTL in XML format (TS 119 612 ListOfTrustedLists structure)."""

from datetime import datetime, timezone
from typing import Any

from lxml import etree

from tools.lotl.tl_entry import TLEntry

NS_TSL = "http://uri.etsi.org/19612/v2.4.1#"
NS_DS = "http://www.w3.org/2001/04/xmldsig-more#"
NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
NS_XML = "http://www.w3.org/XML/1998/namespace"

NAMESPACES = {
    None: NS_TSL,
    "xsi": NS_XSI,
}


def _make_elem(tag: str, parent: etree._Element | None = None, **attrib: str) -> etree._Element:
    """Create an element in the TSL namespace."""
    if "}" in tag:
        ns, local = tag.split("}", 1)
        elem = etree.Element(tag, **attrib)
    else:
        elem = etree.Element(f"{{{NS_TSL}}}{tag}", **attrib)
    if parent is not None:
        parent.append(elem)
    return elem


def _add_text_elem(parent: etree._Element, tag: str, text: str, lang: str = "en") -> None:
    """Add a multilingual text element."""
    elem = _make_elem(tag, parent)
    elem.text = text
    elem.set(f"{{{NS_XML}}}lang", lang)


def generate_lotl_xml(
    entries: list[TLEntry],
    sequence_number: int = 1,
    scheme_operator_name: str = "WE BUILD WP4 Trust Group",
    scheme_name: str = "WP4 List of Trusted Lists",
    scheme_information_uri: str = "https://webuild-consortium.github.io/wp4-trust-group/",
) -> bytes:
    """Generate LoTL as XML (unsigned).

    Structure follows TS 119 612 ListOfTrustedLists / SIE pattern.
    """
    now = datetime.now(timezone.utc)
    issue_dt = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    next_update = now.replace(month=min(now.month + 6, 12) or 12).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    root = _make_elem("TrustServiceStatusList")
    root.set("Id", "lotl-1")  # Required for signxml enveloped signature reference
    root.set(f"{{{NS_XSI}}}schemaLocation", f"{NS_TSL} https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd")

    scheme_info = _make_elem("SchemeInformation", root)
    _make_elem("TSLVersionIdentifier", scheme_info).text = "6"
    _make_elem("TSLSequenceNumber", scheme_info).text = str(sequence_number)
    _make_elem("TSLType", scheme_info).text = "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric"

    op_name = _make_elem("SchemeOperatorName", scheme_info)
    _add_text_elem(op_name, "Name", scheme_operator_name)

    op_addr = _make_elem("SchemeOperatorAddress", scheme_info)
    postal = _make_elem("PostalAddresses", op_addr)
    pa = _make_elem("PostalAddress", postal)
    _make_elem("StreetAddress", pa).text = "N/A"
    _make_elem("Locality", pa).text = "N/A"
    _make_elem("PostalCode", pa).text = "N/A"
    _make_elem("CountryName", pa).text = "EU"
    elec = _make_elem("ElectronicAddress", op_addr)
    uri_elem = _make_elem("URI", elec)
    uri_elem.text = scheme_information_uri

    scheme_name_elem = _make_elem("SchemeName", scheme_info)
    _add_text_elem(scheme_name_elem, "Name", scheme_name)

    _make_elem("SchemeInformationURI", scheme_info).text = scheme_information_uri
    _make_elem("StatusDeterminationApproach", scheme_info).text = "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate"
    _make_elem("SchemeTypeCommunityRules", scheme_info).text = "http://uri.etsi.org/TrstSvc/TrustedList/SchemeTypeCommunityRules/EU"
    _make_elem("SchemeTerritory", scheme_info).text = "EU"
    _make_elem("ListIssueDateTime", scheme_info).text = issue_dt
    _make_elem("NextUpdate", scheme_info).text = next_update

    dist_points = _make_elem("DistributionPoints", scheme_info)
    for entry in entries:
        dp = _make_elem("DistributionPoint", dist_points)
        uri_elem = _make_elem("URI", dp)
        uri_elem.text = entry.tl_url

    return etree.tostring(
        root,
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
        method="xml",
    )
