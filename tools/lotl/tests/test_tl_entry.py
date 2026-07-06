"""Tests for tl_entry module."""

import pytest

from tools.lotl.tl_entry import TLEntry


def test_from_dict() -> None:
    """TLEntry.from_dict parses correctly."""
    data = {
        "tl_url": "https://example.com/tl.json",
        "tl_url_xml": "https://example.com/tl.xml",
        "trust_anchor": "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----",
        "metadata": {"country": "IT"},
    }
    entry = TLEntry.from_dict(data, "pid-provider", "acme")
    assert entry.tl_type == "pid-provider"
    assert entry.participant_id == "acme"
    assert entry.tl_url == "https://example.com/tl.json"
    assert entry.tl_url_xml == "https://example.com/tl.xml"
    assert entry.tl_url_json is None
    assert entry.metadata == {"country": "IT"}


def test_get_tl_url_json_default() -> None:
    """get_tl_url_json returns tl_url when tl_url_json absent."""
    entry = TLEntry(tl_type="x", participant_id="y", tl_url="https://a.com/tl.json")
    assert entry.get_tl_url_json() == "https://a.com/tl.json"


def test_get_tl_url_json_explicit() -> None:
    """get_tl_url_json returns tl_url_json when present."""
    entry = TLEntry(
        tl_type="x",
        participant_id="y",
        tl_url="https://a.com/tl",
        tl_url_json="https://a.com/tl.json",
    )
    assert entry.get_tl_url_json() == "https://a.com/tl.json"


def test_get_tl_url_xml_default() -> None:
    """get_tl_url_xml returns tl_url when tl_url_xml absent."""
    entry = TLEntry(tl_type="x", participant_id="y", tl_url="https://a.com/tl.xml")
    assert entry.get_tl_url_xml() == "https://a.com/tl.xml"
