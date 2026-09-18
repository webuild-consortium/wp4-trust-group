"""Generate LoTL in XML format (TS 119 612 compiled list / EUlistofthelists).

Emits every scheme information field TS 119 612 clause 5.3 marks "shall be present",
plus DistributionPoints (clause 5.3.16). Pointer qualifiers are TSLType,
SchemeOperatorName, SchemeTerritory and MimeType.
"""

from datetime import datetime, timezone
from typing import Any

from lxml import etree  # nosec B410

from tools.lotl.json_generator import (
    _add_months_safe_utc,
    _electronic_address_uris,
    _pointers_for_entry,
)
from tools.lotl.settings import (
    LOTL_HISTORICAL_INFORMATION_PERIOD,
    LOTL_OPERATOR_EMAIL,
    LOTL_OPERATOR_POSTAL_ADDRESS,
    LOTL_OPERATOR_WEBSITE,
    LOTL_SCHEME_RULES_URI,
    LOTL_SCHEME_TERRITORY,
    LOTL_STATUS_DETN_URI,
    LOTL_TSL_TYPE_URI,
    LOTL_XML_FILENAME,
    NS_TSL,
    NS_TSL_ADDITIONAL,
    TSL_TAG_URI,
    TSL_XSD_SCHEMA_LOCATION,
)
from tools.lotl.tl_entry import TLEntry

NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
NS_XML = "http://www.w3.org/XML/1998/namespace"

# Declared once on the root, so no element carries a generated ns0/ns1 prefix.
NAMESPACES = {
    None: NS_TSL,
    "tslx": NS_TSL_ADDITIONAL,
    "xsi": NS_XSI,
}


def _make_elem(tag: str, parent: etree._Element | None = None, **attrib: str) -> etree._Element:
    """Create an element in the TSL namespace."""
    elem = etree.Element(f"{{{NS_TSL}}}{tag}", **attrib)
    if parent is not None:
        parent.append(elem)
    return elem


def _add_name(parent: etree._Element, tag: str, text: str, lang: str = "en") -> None:
    """Add an InternationalNamesType wrapper with a multilingual Name child."""
    wrapper = _make_elem(tag, parent)
    name = _make_elem("Name", wrapper)
    name.text = text
    name.set(f"{{{NS_XML}}}lang", lang)


def _add_lang_uri(parent: etree._Element, href: str, lang: str = "en") -> None:
    """Add a NonEmptyMultiLangURIType URI child."""
    uri = _make_elem("URI", parent)
    uri.text = href
    uri.set(f"{{{NS_XML}}}lang", lang)


def _add_plain_uri(parent: etree._Element, href: str) -> None:
    """Add a NonEmptyURIType URI child (no xml:lang)."""
    uri = _make_elem("URI", parent)
    uri.text = href


def _add_other_information(parent: etree._Element, child: etree._Element) -> None:
    oi = _make_elem("OtherInformation", parent)
    oi.append(child)


def _add_other_tsl_pointer(parent: etree._Element, pointer: dict[str, Any]) -> None:
    """Emit one OtherTSLPointer from a JSON-shaped pointer dict."""
    otp = _make_elem("OtherTSLPointer", parent)

    sdis_el = _make_elem("ServiceDigitalIdentities", otp)
    for sdi in pointer["ServiceDigitalIdentities"]:
        sdi_el = _make_elem("ServiceDigitalIdentity", sdis_el)
        for cert in sdi.get("X509Certificates", []):
            digital_id = _make_elem("DigitalId", sdi_el)
            x509 = _make_elem("X509Certificate", digital_id)
            x509.text = cert["val"]

    loc = _make_elem("TSLLocation", otp)
    loc.text = pointer["LoTELocation"]

    addl = _make_elem("AdditionalInformation", otp)
    for q in pointer.get("LoTEQualifiers", []):
        tsl_type = _make_elem("TSLType")
        tsl_type.text = q["LoTEType"]
        _add_other_information(addl, tsl_type)

        son = _make_elem("SchemeOperatorName")
        for n in q.get("SchemeOperatorName", []):
            name = _make_elem("Name", son)
            name.text = str(n.get("value", ""))
            name.set(f"{{{NS_XML}}}lang", str(n.get("lang", "en")))
        _add_other_information(addl, son)

        territory = q.get("SchemeTerritory")
        if territory:
            st = _make_elem("SchemeTerritory")
            st.text = str(territory)
            _add_other_information(addl, st)

        mime = etree.Element(f"{{{NS_TSL_ADDITIONAL}}}MimeType")
        mime.text = q["MimeType"]
        _add_other_information(addl, mime)


def _default_distribution_uris(scheme_information_uri: str) -> list[str]:
    base = scheme_information_uri.rstrip("/")
    return [f"{base}/{LOTL_XML_FILENAME}"]


def generate_lotl_xml(
    entries: list[TLEntry],
    sequence_number: int = 1,
    scheme_operator_name: str = "WE BUILD WP4 Trust Group",
    scheme_name: str = "WP4 List of Trusted Lists",
    scheme_information_uri: str = "https://webuild-consortium.github.io/wp4-trust-group/",
    distribution_point_uris: list[str] | None = None,
    scheme_operator_email: str = LOTL_OPERATOR_EMAIL,
    scheme_operator_website: str = LOTL_OPERATOR_WEBSITE,
    scheme_operator_postal_address: dict[str, str] | None = None,
) -> bytes:
    """Generate LoTL as unsigned TS 119 612 XML (compiled list of pointers).

    Structure follows TrustServiceStatusList with TSLType EUlistofthelists and
    PointersToOtherTSL. Member list URLs and signing certificates come from the
    same pointer construction as the JSON generator.
    """
    now = datetime.now(timezone.utc)
    issue_dt = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    next_update = _add_months_safe_utc(now, 6).strftime("%Y-%m-%dT%H:%M:%SZ")

    root = etree.Element(f"{{{NS_TSL}}}TrustServiceStatusList", nsmap=NAMESPACES)
    root.set("Id", "lotl-1")
    root.set("TSLTag", TSL_TAG_URI)
    root.set(
        f"{{{NS_XSI}}}schemaLocation",
        f"{NS_TSL} {TSL_XSD_SCHEMA_LOCATION}",
    )

    scheme_info = _make_elem("SchemeInformation", root)
    _make_elem("TSLVersionIdentifier", scheme_info).text = "6"
    _make_elem("TSLSequenceNumber", scheme_info).text = str(sequence_number)
    _make_elem("TSLType", scheme_info).text = LOTL_TSL_TYPE_URI

    _add_name(scheme_info, "SchemeOperatorName", scheme_operator_name)

    op_addr = _make_elem("SchemeOperatorAddress", scheme_info)
    postal = _make_elem("PostalAddresses", op_addr)
    pa = _make_elem("PostalAddress", postal)
    pa.set(f"{{{NS_XML}}}lang", "en")
    address = scheme_operator_postal_address or LOTL_OPERATOR_POSTAL_ADDRESS
    for tag in ("StreetAddress", "Locality", "PostalCode", "CountryName"):
        if address.get(tag):
            _make_elem(tag, pa).text = address[tag]
    elec = _make_elem("ElectronicAddress", op_addr)
    for href in _electronic_address_uris(scheme_operator_email, scheme_operator_website):
        _add_lang_uri(elec, href)

    _add_name(scheme_info, "SchemeName", f"{LOTL_SCHEME_TERRITORY}:{scheme_name}")

    scheme_uri = _make_elem("SchemeInformationURI", scheme_info)
    _add_lang_uri(scheme_uri, scheme_information_uri)

    _make_elem("StatusDeterminationApproach", scheme_info).text = LOTL_STATUS_DETN_URI

    rules = _make_elem("SchemeTypeCommunityRules", scheme_info)
    _add_lang_uri(rules, LOTL_SCHEME_RULES_URI)

    _make_elem("SchemeTerritory", scheme_info).text = LOTL_SCHEME_TERRITORY

    policy = _make_elem("PolicyOrLegalNotice", scheme_info)
    notice = _make_elem("TSLLegalNotice", policy)
    notice.text = scheme_name
    notice.set(f"{{{NS_XML}}}lang", "en")

    _make_elem("HistoricalInformationPeriod", scheme_info).text = str(
        LOTL_HISTORICAL_INFORMATION_PERIOD
    )

    pointers: list[dict[str, Any]] = []
    for entry in entries:
        pointers.extend(_pointers_for_entry(entry))
    if pointers:
        ptrs_el = _make_elem("PointersToOtherTSL", scheme_info)
        for pointer in pointers:
            _add_other_tsl_pointer(ptrs_el, pointer)

    _make_elem("ListIssueDateTime", scheme_info).text = issue_dt
    next_el = _make_elem("NextUpdate", scheme_info)
    _make_elem("dateTime", next_el).text = next_update

    dist = (
        list(distribution_point_uris)
        if distribution_point_uris is not None
        else _default_distribution_uris(scheme_information_uri)
    )
    dist_el = _make_elem("DistributionPoints", scheme_info)
    for href in dist:
        _add_plain_uri(dist_el, href)

    etree.cleanup_namespaces(root, top_nsmap=NAMESPACES)
    return etree.tostring(
        root,
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
        method="xml",
    )
