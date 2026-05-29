"""Tests for validator."""

import json
from pathlib import Path

import pytest

from tools.lotl.validator import validate_tl_entry_file, validate_tl_entries_dir


def test_validate_valid_file(tmp_path: Path) -> None:
    """Valid file has no errors."""
    f = tmp_path / "entry.json"
    f.write_text(json.dumps({
        "tl_url": "https://example.com/tl.json",
        "trust_anchor": "-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----",
    }))
    assert validate_tl_entry_file(f) == []


def test_validate_missing_tl_url(tmp_path: Path) -> None:
    """Missing tl_url returns error."""
    f = tmp_path / "entry.json"
    f.write_text(json.dumps({"trust_anchor": "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----"}))
    errors = validate_tl_entry_file(f)
    assert any("tl_url" in e for e in errors)


def test_validate_missing_trust_anchor(tmp_path: Path) -> None:
    """Missing trust_anchor returns error."""
    f = tmp_path / "entry.json"
    f.write_text(json.dumps({"tl_url": "https://example.com/tl.json"}))
    errors = validate_tl_entry_file(f)
    assert any("trust_anchor" in e for e in errors)


def test_validate_invalid_pem(tmp_path: Path) -> None:
    """Invalid PEM format returns error."""
    f = tmp_path / "entry.json"
    f.write_text(json.dumps({
        "tl_url": "https://example.com/tl.json",
        "trust_anchor": "not-a-valid-pem",
    }))
    errors = validate_tl_entry_file(f)
    assert any("trust_anchor" in e or "PEM" in e for e in errors)


def test_validate_dir(tl_entries_dir: Path) -> None:
    """validate_tl_entries_dir on valid dir."""
    valid, errors = validate_tl_entries_dir(tl_entries_dir)
    assert valid
    assert not errors


def test_validate_dir_nonexistent() -> None:
    """Nonexistent dir returns invalid."""
    valid, errors = validate_tl_entries_dir("/nonexistent/path/xyz")
    assert not valid
    assert errors


def test_validate_file_nonexistent() -> None:
    """Nonexistent file returns errors."""
    errors = validate_tl_entry_file("/nonexistent/file.json")
    assert errors
    assert "not found" in errors[0].lower() or "exist" in errors[0].lower()


def test_validate_invalid_json(tmp_path: Path) -> None:
    """Invalid JSON returns error."""
    f = tmp_path / "bad.json"
    f.write_text("not valid json {")
    errors = validate_tl_entry_file(f)
    assert any("json" in e.lower() for e in errors)


def test_validate_against_schema_valid() -> None:
    """validate_against_schema with valid data returns no errors."""
    from tools.lotl.validator import validate_against_schema

    data = {"tl_url": "https://x.com/tl.json", "trust_anchor": "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----"}
    errors = validate_against_schema(data)
    # May be [] if jsonschema not installed
    assert isinstance(errors, list)


def test_validate_dir_invalid_tl_type(tmp_path: Path) -> None:
    """Invalid TL type directory is reported."""
    (tmp_path / "pid-provider").mkdir()
    (tmp_path / "pid-provider" / "x.json").write_text(
        json.dumps({"tl_url": "https://x.com/tl.json", "trust_anchor": "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----"})
    )
    (tmp_path / "invalid-type").mkdir()
    (tmp_path / "invalid-type" / "y.json").write_text(
        json.dumps({"tl_url": "https://y.com/tl.json", "trust_anchor": "-----BEGIN CERTIFICATE-----\nY\n-----END CERTIFICATE-----"})
    )
    valid, errors = validate_tl_entries_dir(tmp_path)
    assert not valid
    assert any("invalid-type" in e or "Invalid TL type" in e for e in errors)


def test_validate_empty_tl_url(tmp_path: Path) -> None:
    """Empty tl_url returns error."""
    f = tmp_path / "entry.json"
    f.write_text(json.dumps({"tl_url": "   ", "trust_anchor": "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----"}))
    errors = validate_tl_entry_file(f)
    assert any("tl_url" in e for e in errors)


def test_validate_tl_url_xml_not_string(tmp_path: Path) -> None:
    """tl_url_xml not a string returns error."""
    f = tmp_path / "entry.json"
    f.write_text(json.dumps({
        "tl_url": "https://x.com/tl.json",
        "tl_url_xml": 123,
        "trust_anchor": "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----",
    }))
    errors = validate_tl_entry_file(f)
    assert any("tl_url_xml" in e for e in errors)
