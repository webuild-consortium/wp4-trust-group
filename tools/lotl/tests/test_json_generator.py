"""Tests for JSON generator."""

from tools.lotl.json_generator import generate_lotl_json
from tools.lotl.tl_entry import TLEntry


def test_generate_empty() -> None:
    """Generate LoTL with no entries."""
    out = generate_lotl_json([], sequence_number=1)
    assert out["loteTag"] == "http://uri.etsi.org/19602/LoTETag"
    assert out["schemeInformation"]["loteSequenceNumber"] == 1
    assert out["schemeInformation"]["distributionPoints"] == []


def test_generate_with_entries(sample_tl_entry: TLEntry) -> None:
    """Generate LoTL with entries."""
    out = generate_lotl_json([sample_tl_entry], sequence_number=2)
    dps = out["schemeInformation"]["distributionPoints"]
    assert len(dps) == 1
    assert dps[0]["tlType"] == "pid-provider"
    assert dps[0]["participantId"] == "example-tlp"
    assert dps[0]["tlUrl"] == sample_tl_entry.tl_url
