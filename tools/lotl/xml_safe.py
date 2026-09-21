"""Hardened lxml helpers.

Bandit B320/B410 flag any lxml parse/import. This module is the single place we
parse XML, always with DTD loading, entity expansion and network access disabled
(XXE). Other modules import ``etree`` only to *build* trees (Element, tostring,
XMLSchema).
"""

from lxml import etree  # nosec B410

_PARSER_KWARGS = {
    "resolve_entities": False,
    "load_dtd": False,
    "no_network": True,
    "huge_tree": False,
}


def xml_parser() -> etree.XMLParser:
    """Return a fresh XXE-safe parser. lxml parsers are not thread-safe."""
    return etree.XMLParser(**_PARSER_KWARGS)


def safe_fromstring(xml_content: bytes) -> etree._Element:
    """Parse bytes with the XXE-safe parser."""
    return etree.fromstring(xml_content, parser=xml_parser())  # nosec B320


def safe_parse(source: str) -> etree._ElementTree:
    """Parse a local file with the XXE-safe parser."""
    return etree.parse(source, parser=xml_parser())  # nosec B320
