"""Tests for JSON generator."""

from datetime import datetime, timezone
from pathlib import Path

from tools.lotl.json_generator import _add_months_safe_utc, generate_lotl_json
from tools.lotl.settings import LOTL_LOTE_TYPE_URI
from tools.lotl.tl_entry import TLEntry


def test_generate_empty() -> None:
    """Generate LoTL with no entries."""
    out = generate_lotl_json([], sequence_number=1)
    assert "LoTE" in out
    lasi = out["LoTE"]["ListAndSchemeInformation"]
    assert lasi["LoTESequenceNumber"] == 1
    assert lasi["LoTEType"] == LOTL_LOTE_TYPE_URI
    assert lasi["PointersToOtherLoTE"] == []
    assert isinstance(lasi["DistributionPoints"], list)
    assert all(isinstance(u, str) for u in lasi["DistributionPoints"])


def test_generate_with_entries(sample_tl_entry: TLEntry) -> None:
    """Generate LoTL with entries (JSON + XML pointers when URLs differ)."""
    out = generate_lotl_json([sample_tl_entry], sequence_number=2)
    lasi = out["LoTE"]["ListAndSchemeInformation"]
    assert lasi["LoTESequenceNumber"] == 2
    ptrs = lasi["PointersToOtherLoTE"]
    assert len(ptrs) == 2
    assert ptrs[0]["LoTELocation"] == sample_tl_entry.get_tl_url_json()
    assert (
        ptrs[0]["LoTEQualifiers"][0]["LoTEType"]
        == "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList"
    )
    assert ptrs[0]["LoTEQualifiers"][0]["MimeType"] == "application/json"
    assert ptrs[1]["LoTELocation"] == sample_tl_entry.get_tl_url_xml()
    assert ptrs[1]["LoTEQualifiers"][0]["MimeType"] == "application/xml"


def test_x509_in_pointer(
    sample_tl_entry: TLEntry,
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """Valid PEM trust anchor becomes PKIOb in ServiceDigitalIdentities."""
    _key_path, cert_path = signing_key_and_cert
    entry = TLEntry(
        tl_type=sample_tl_entry.tl_type,
        participant_id=sample_tl_entry.participant_id,
        tl_url=sample_tl_entry.tl_url,
        trust_anchor=cert_path.read_text(),
        metadata=sample_tl_entry.metadata,
    )
    out = generate_lotl_json([entry], sequence_number=1)
    ptr0 = out["LoTE"]["ListAndSchemeInformation"]["PointersToOtherLoTE"][0]
    sdi = ptr0["ServiceDigitalIdentities"]
    assert len(sdi) == 1
    assert sdi[0]["X509Certificates"][0]["val"]


def test_add_months_safe_handles_rollover_and_day_clamp() -> None:
    """Month addition handles year rollover and month-end day clamping."""
    dt = datetime(2026, 8, 31, 12, 0, 0, tzinfo=timezone.utc)
    out = _add_months_safe_utc(dt, 6)
    assert out.year == 2027
    assert out.month == 2
    assert out.day == 28
