"""Tests for collector."""

import json
from pathlib import Path

import pytest

from tools.lotl.collector import collect_entries, iter_entries_by_type
from tools.lotl.tl_entry import TLEntry


def test_collect_empty(tmp_path: Path) -> None:
    """Empty directory returns empty list."""
    assert collect_entries(tmp_path) == []


def test_collect_nonexistent() -> None:
    """Nonexistent directory returns empty list."""
    assert collect_entries("/nonexistent/path/12345") == []


def test_collect_single_entry(tl_entries_dir: Path) -> None:
    """Collect single entry from pid-provider."""
    entries = collect_entries(tl_entries_dir)
    assert len(entries) == 1
    assert entries[0].tl_type == "pid-provider"
    assert entries[0].participant_id == "example-tlp"
    assert entries[0].tl_url == "https://example.com/pid_providers.json"


def test_collect_invalid_tl_type(tmp_path: Path) -> None:
    """Invalid TL type directory is skipped."""
    (tmp_path / "invalid-type").mkdir()
    (tmp_path / "invalid-type" / "x.json").write_text('{"tl_url": "https://x", "trust_anchor": "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----"}')
    entries = collect_entries(tmp_path)
    assert len(entries) == 0


def test_collect_missing_required(tmp_path: Path) -> None:
    """Missing required fields raises."""
    (tmp_path / "pid-provider").mkdir()
    (tmp_path / "pid-provider" / "x.json").write_text('{"tl_url": "https://x"}')
    with pytest.raises(ValueError, match="Missing required"):
        collect_entries(tmp_path)


def test_iter_entries_by_type(sample_tl_entry: TLEntry) -> None:
    """iter_entries_by_type groups by tl_type."""
    entries = [sample_tl_entry]
    items = list(iter_entries_by_type(entries))
    assert len(items) == 1
    assert items[0][0] == "pid-provider"
    assert len(items[0][1]) == 1
