"""Tests for producer."""

import json
from pathlib import Path

import pytest
from unittest.mock import patch

from tools.lotl.producer import get_next_sequence_number, produce
from tools.lotl.settings import LOTL_JSON_FILENAME, LOTL_XML_FILENAME


def test_produce_validate_only(tl_entries_dir: Path, tmp_path: Path) -> None:
    """validate_only exits 0 without signing."""
    code = produce(
        tl_entries_dir=tl_entries_dir,
        output_dir=tmp_path,
        validate_only=True,
    )
    assert code == 0


def test_produce_requires_signing(tl_entries_dir: Path, tmp_path: Path) -> None:
    """Produce without key/cert returns 1."""
    code = produce(
        tl_entries_dir=tl_entries_dir,
        output_dir=tmp_path,
        signing_key=None,
        signing_cert=None,
        validate_only=False,
    )
    assert code == 1


def test_produce_success(
    tl_entries_dir: Path,
    tmp_path: Path,
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """Produce creates signed JSON and XML."""
    key_path, cert_path = signing_key_and_cert
    code = produce(
        tl_entries_dir=tl_entries_dir,
        output_dir=tmp_path,
        signing_key=key_path.read_text(),
        signing_cert=cert_path.read_text(),
    )
    assert code == 0
    json_path = tmp_path / LOTL_JSON_FILENAME
    xml_path = tmp_path / LOTL_XML_FILENAME
    assert json_path.exists()
    assert xml_path.exists()
    data = json.loads(json_path.read_text())
    assert "signature" in data
    assert "LoTE" in data


def test_get_next_sequence_number_from_json_legacy_pilot_shape(tmp_path: Path) -> None:
    """Read sequence from pre-migration (pilot) JSON shape."""
    (tmp_path / LOTL_JSON_FILENAME).write_text(
        json.dumps({"schemeInformation": {"loteSequenceNumber": 7}})
    )
    assert get_next_sequence_number(tmp_path) == 8


def test_get_next_sequence_number_empty(tmp_path: Path) -> None:
    """No existing LoTL returns 1."""
    assert get_next_sequence_number(tmp_path) == 1


def test_get_next_sequence_number_from_json(tmp_path: Path) -> None:
    """Read sequence from existing JSON."""
    (tmp_path / LOTL_JSON_FILENAME).write_text(
        json.dumps(
            {"LoTE": {"ListAndSchemeInformation": {"LoTESequenceNumber": 5}}}
        )
    )
    assert get_next_sequence_number(tmp_path) == 6


def test_get_next_sequence_number_from_xml(tmp_path: Path) -> None:
    """Read sequence from existing XML."""
    xml_content = """<?xml version="1.0"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#">
  <SchemeInformation>
    <TSLSequenceNumber>3</TSLSequenceNumber>
  </SchemeInformation>
</TrustServiceStatusList>"""
    (tmp_path / LOTL_XML_FILENAME).write_text(xml_content)
    assert get_next_sequence_number(tmp_path) == 4


def test_produce_validation_failure(tmp_path: Path) -> None:
    """Produce with invalid tl_entries exits 1."""
    (tmp_path / "pid-provider").mkdir()
    (tmp_path / "pid-provider" / "bad.json").write_text('{"tl_url": "x"}')  # missing trust_anchor
    code = produce(tl_entries_dir=tmp_path, output_dir=tmp_path, validate_only=False)
    assert code == 1


def test_produce_empty_entries_returns_one(
    tmp_path: Path,
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """Produce fails clearly when no TL entries are available."""
    key_path, cert_path = signing_key_and_cert
    code = produce(
        tl_entries_dir=tmp_path,
        output_dir=tmp_path,
        signing_key=key_path.read_text(),
        signing_cert=cert_path.read_text(),
        validate_only=False,
    )
    assert code == 1


def test_produce_generation_exception_returns_one(
    tl_entries_dir: Path,
    tmp_path: Path,
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """Generation exceptions are handled as non-zero exit."""
    from tools.lotl import producer

    key_path, cert_path = signing_key_and_cert
    with patch.object(producer, "generate_lotl_json", side_effect=RuntimeError("boom")):
        code = produce(
            tl_entries_dir=tl_entries_dir,
            output_dir=tmp_path,
            signing_key=key_path.read_text(),
            signing_cert=cert_path.read_text(),
        )
    assert code == 1


def test_produce_validation_exception_returns_one(
    tl_entries_dir: Path,
    tmp_path: Path,
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    """Validation exceptions are handled as non-zero exit."""
    from tools.lotl import producer

    key_path, cert_path = signing_key_and_cert
    with patch.object(producer, "validate_lote_json", side_effect=RuntimeError("boom")):
        code = produce(
            tl_entries_dir=tl_entries_dir,
            output_dir=tmp_path,
            signing_key=key_path.read_text(),
            signing_cert=cert_path.read_text(),
        )
    assert code == 1
