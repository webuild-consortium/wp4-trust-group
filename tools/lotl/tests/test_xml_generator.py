"""Tests for XML generator."""

from tools.lotl.tl_entry import TLEntry
from tools.lotl.xml_generator import generate_lotl_xml


def test_generate_empty() -> None:
    """Generate LoTL XML with no entries."""
    xml = generate_lotl_xml([], sequence_number=1)
    assert b"TrustServiceStatusList" in xml
    assert b"TSLSequenceNumber" in xml
    assert b"1" in xml


def test_generate_with_entries(sample_tl_entry: TLEntry) -> None:
    """Generate LoTL XML with entries."""
    xml = generate_lotl_xml([sample_tl_entry], sequence_number=2)
    assert sample_tl_entry.tl_url.encode() in xml
    assert b"DistributionPoint" in xml
