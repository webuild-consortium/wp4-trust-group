"""Tests for fetch and validate (tl_validator)."""

from unittest.mock import MagicMock, patch

from tools.lotl.tl_entry import TLEntry
from tools.lotl.tl_validator import fetch_tl, validate_tl_entry


def test_fetch_tl_unreachable() -> None:
    """Fetch unreachable URL returns None."""
    content, raw, ctype = fetch_tl("https://nonexistent.invalid.example.xyz/404", timeout=1)
    assert content is None
    assert raw is None


@patch("tools.lotl.tl_validator.urlopen")
def test_fetch_tl_success(mock_urlopen: MagicMock) -> None:
    """Fetch returns content."""
    from io import BytesIO
    from urllib.response import addinfourl

    mock_resp = addinfourl(BytesIO(b'{"x":1}'), {"Content-Type": "application/json"}, "https://example.com", 200)
    mock_resp.read = lambda: b'{"x":1}'
    mock_resp.headers = {"Content-Type": "application/json"}
    mock_resp.__enter__ = lambda self: self
    mock_resp.__exit__ = lambda *a: None
    mock_urlopen.return_value = mock_resp

    content, raw, ctype = fetch_tl("https://example.com/tl.json")
    assert content is not None
    assert "x" in content


def test_validate_tl_entry_no_fetch(sample_tl_entry: TLEntry) -> None:
    """validate_tl_entry with fetch_and_validate=False passes."""
    valid, errors = validate_tl_entry(sample_tl_entry, fetch_and_validate=False)
    assert valid
    assert not errors
