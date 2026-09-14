"""Validate unsigned LoTL XML (TS 119 612 compiled list).

Semantic checks mirror ``lote_validate.py`` for the JSON LoTE. XSD validation
uses the vendored ``19612_xsd.xsd`` (offline imports: ``xml.xsd``,
``xmldsig-core-schema.xsd``).
"""

from __future__ import annotations

from pathlib import Path

from lxml import etree

from tools.lotl.settings import (
    LOTL_HISTORICAL_INFORMATION_PERIOD,
    LOTL_SCHEME_RULES_URI,
    LOTL_TSL_TYPE_URI,
    LOTL_XML_FILENAME,
    NS_TSL,
    NS_TSL_ADDITIONAL,
    TL_TYPE_TO_REFERENCE_URI,
    TSL_TAG_URI,
)

NS = {"tsl": NS_TSL, "tslx": NS_TSL_ADDITIONAL}
NS_XML = "http://www.w3.org/XML/1998/namespace"


def get_schemas_dir() -> Path:
    return Path(__file__).resolve().parent / "schemas"


def get_tsl_xsd_path() -> Path:
    return get_schemas_dir() / "19612_xsd.xsd"


def _safe_parse(xml_content: bytes) -> etree._Element:
    parser = etree.XMLParser(
        resolve_entities=False,
        load_dtd=False,
        no_network=True,
        huge_tree=False,
    )
    return etree.fromstring(xml_content, parser=parser)


def validate_against_xsd(xml_content: bytes) -> list[str]:
    """Validate ``xml_content`` against the vendored TS 119 612 XSD."""
    xsd_path = get_tsl_xsd_path()
    if not xsd_path.is_file():
        return [f"TS 119 612 XSD not found: {xsd_path}"]
    try:
        parser = etree.XMLParser(
            resolve_entities=False,
            load_dtd=False,
            no_network=True,
            huge_tree=False,
        )
        schema_doc = etree.parse(str(xsd_path), parser)
        schema = etree.XMLSchema(schema_doc)
        doc = _safe_parse(xml_content)
        if not schema.validate(doc):
            return [f"XSD: {e.message}" for e in schema.error_log]
    except etree.XMLSchemaParseError as e:
        return [f"Failed to load TS 119 612 XSD: {e}"]
    except etree.XMLSyntaxError as e:
        return [f"XML is not well-formed: {e}"]
    return []


def validate_lotl_xml_semantics(root: etree._Element) -> list[str]:
    """LoTL-specific checks on a parsed TrustServiceStatusList."""
    err: list[str] = []
    expected_tag = f"{{{NS_TSL}}}TrustServiceStatusList"
    if root.tag != expected_tag:
        return [f"Root element must be {expected_tag}, got {root.tag}"]

    if root.get("TSLTag") != TSL_TAG_URI:
        err.append(f"TrustServiceStatusList/@TSLTag must be {TSL_TAG_URI!r}")
    if not root.get("Id"):
        err.append("TrustServiceStatusList/@Id is required for the enveloped signature")

    tsl_type = root.findtext("tsl:SchemeInformation/tsl:TSLType", namespaces=NS)
    if tsl_type != LOTL_TSL_TYPE_URI:
        err.append(
            f"TSLType must be {LOTL_TSL_TYPE_URI!r} for this LoTL producer "
            f"(got {tsl_type!r})"
        )

    rules = root.findtext(
        "tsl:SchemeInformation/tsl:SchemeTypeCommunityRules/tsl:URI",
        namespaces=NS,
    )
    if rules != LOTL_SCHEME_RULES_URI:
        err.append(
            f"SchemeTypeCommunityRules URI must be {LOTL_SCHEME_RULES_URI!r} "
            f"(got {rules!r})"
        )

    scheme_uri = root.find(
        "tsl:SchemeInformation/tsl:SchemeInformationURI/tsl:URI",
        namespaces=NS,
    )
    if scheme_uri is None or not (scheme_uri.text or "").strip():
        err.append("SchemeInformationURI must contain a multilingual URI")
    elif scheme_uri.get(f"{{{NS_XML}}}lang") is None:
        err.append("SchemeInformationURI/URI must carry xml:lang")

    eaddr = root.find(
        "tsl:SchemeInformation/tsl:SchemeOperatorAddress/tsl:ElectronicAddress/tsl:URI",
        namespaces=NS,
    )
    if eaddr is None or not (eaddr.text or "").strip():
        err.append("ElectronicAddress must contain a URI (mailto: or https:)")
    else:
        href = eaddr.text.strip()
        if not (href.startswith("mailto:") or href.startswith("http://") or href.startswith("https://")):
            err.append(
                "ElectronicAddress URI must be a mailto: address or a web site "
                f"(Annex B.0), got {href!r}"
            )
        if eaddr.get(f"{{{NS_XML}}}lang") is None:
            err.append("ElectronicAddress/URI must carry xml:lang")

    hip = root.findtext(
        "tsl:SchemeInformation/tsl:HistoricalInformationPeriod",
        namespaces=NS,
    )
    if hip != str(LOTL_HISTORICAL_INFORMATION_PERIOD):
        err.append(
            f"HistoricalInformationPeriod must be {LOTL_HISTORICAL_INFORMATION_PERIOD} "
            f"(got {hip!r})"
        )

    next_dt = root.findtext(
        "tsl:SchemeInformation/tsl:NextUpdate/tsl:dateTime",
        namespaces=NS,
    )
    if not next_dt:
        err.append("NextUpdate must contain a dateTime child")

    if root.find("tsl:TrustServiceProviderList", namespaces=NS) is not None:
        err.append(
            "This LoTL producer must not include TrustServiceProviderList "
            "(compiled list of pointers only)"
        )

    dps = root.findall("tsl:SchemeInformation/tsl:DistributionPoints/tsl:URI", namespaces=NS)
    if not dps:
        err.append("DistributionPoints must list this LoTL's own publication URI")
    else:
        for i, uri in enumerate(dps):
            text = (uri.text or "").strip()
            if not text:
                err.append(f"DistributionPoints/URI[{i}] must be a non-empty URI")
        if not any(
            (u.text or "").rstrip("/").endswith(LOTL_XML_FILENAME) for u in dps
        ):
            err.append(
                f"DistributionPoints must include this LoTL XML ({LOTL_XML_FILENAME})"
            )

    if root.find("tsl:SchemeInformation/tsl:DistributionPoints/tsl:DistributionPoint", namespaces=NS) is not None:
        err.append(
            "DistributionPoints must be a list of URI children, not DistributionPoint wrappers"
        )

    ptrs = root.findall(
        "tsl:SchemeInformation/tsl:PointersToOtherTSL/tsl:OtherTSLPointer",
        namespaces=NS,
    )
    if not ptrs:
        err.append("PointersToOtherTSL must contain at least one OtherTSLPointer")
        return err

    known_types = set(TL_TYPE_TO_REFERENCE_URI.values())
    for i, ptr in enumerate(ptrs):
        loc = ptr.findtext("tsl:TSLLocation", namespaces=NS)
        if not loc:
            err.append(f"OtherTSLPointer[{i}].TSLLocation is required and non-empty")
        certs = ptr.findall(
            "tsl:ServiceDigitalIdentities/tsl:ServiceDigitalIdentity/tsl:DigitalId/tsl:X509Certificate",
            namespaces=NS,
        )
        if not certs or not any((c.text or "").strip() for c in certs):
            err.append(
                f"OtherTSLPointer[{i}] must include an X509Certificate digital identity "
                "(clause 5.3.13)"
            )
        tsl_types = [
            t.text
            for t in ptr.findall("tsl:AdditionalInformation/tsl:OtherInformation/tsl:TSLType", namespaces=NS)
            if t.text
        ]
        if not tsl_types:
            err.append(f"OtherTSLPointer[{i}] must carry TSLType in AdditionalInformation")
        else:
            for qt in tsl_types:
                if qt not in known_types:
                    err.append(
                        f"OtherTSLPointer[{i}] TSLType is not a known TL/LoTE type URI: {qt!r}"
                    )
        mimes = ptr.findall(
            "tsl:AdditionalInformation/tsl:OtherInformation/tslx:MimeType",
            namespaces=NS,
        )
        if not mimes or not any((m.text or "").strip() for m in mimes):
            err.append(f"OtherTSLPointer[{i}] must carry MimeType in AdditionalInformation")
    return err


def validate_lotl_xml(xml_content: bytes) -> list[str]:
    """Run XSD validation and LoTL semantic checks on unsigned XML bytes."""
    try:
        root = _safe_parse(xml_content)
    except etree.XMLSyntaxError as e:
        return [f"XML is not well-formed: {e}"]
    errors = validate_against_xsd(xml_content)
    errors.extend(validate_lotl_xml_semantics(root))
    return errors
