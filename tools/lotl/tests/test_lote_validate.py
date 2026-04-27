"""Tests for LoTE JSON validation (schema + semantics)."""

import json
from pathlib import Path
from unittest.mock import patch

from tools.lotl.json_generator import generate_lotl_json
from tools.lotl.jades_signer import sign_json
from tools.lotl.lote_validate import (
    _optional_official_schema_path,
    extract_unsigned_lote,
    validate_lote_json,
    validate_unsigned_lote_root,
)
from tools.lotl.tl_entry import TLEntry


def test_validate_empty_lotl_passes() -> None:
    doc = generate_lotl_json([], sequence_number=1)
    errors = validate_lote_json(doc)
    assert errors == []


def test_validate_sample_entries_passes(sample_tl_entry: TLEntry) -> None:
    doc = generate_lotl_json([sample_tl_entry], sequence_number=2)
    errors = validate_lote_json(doc)
    assert errors == []


def test_validate_rejects_wrong_document_lote_type() -> None:
    doc = generate_lotl_json([], sequence_number=1)
    doc["LoTE"]["ListAndSchemeInformation"]["LoTEType"] = (
        "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList"
    )
    errors = validate_lote_json(doc)
    assert any("LoTL" in e for e in errors)


def test_validate_rejects_bad_datetime() -> None:
    doc = generate_lotl_json([], sequence_number=1)
    doc["LoTE"]["ListAndSchemeInformation"]["ListIssueDateTime"] = "not-a-time"
    errors = validate_lote_json(doc)
    assert any("ListIssueDateTime" in e for e in errors)


def test_validate_rejects_bad_pointer_location(sample_tl_entry: TLEntry) -> None:
    doc = generate_lotl_json([sample_tl_entry], sequence_number=1)
    doc["LoTE"]["ListAndSchemeInformation"]["PointersToOtherLoTE"][0][
        "LoTELocation"
    ] = ""
    errors = validate_lote_json(doc)
    assert any("LoTELocation" in e for e in errors)


def test_validate_rejects_unknown_qualifier_lote_type(sample_tl_entry: TLEntry) -> None:
    doc = generate_lotl_json([sample_tl_entry], sequence_number=1)
    doc["LoTE"]["ListAndSchemeInformation"]["PointersToOtherLoTE"][0][
        "LoTEQualifiers"
    ][0]["LoTEType"] = "https://example.com/unknown-type"
    errors = validate_lote_json(doc)
    assert any("not a known" in e for e in errors)


def test_signed_output_still_validates_lote_subtree(
    sample_tl_entry: TLEntry,
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    unsigned = generate_lotl_json([sample_tl_entry], sequence_number=1)
    key, cert = signing_key_and_cert
    signed = sign_json(unsigned, key, cert)
    assert "signature" in signed
    errs = validate_unsigned_lote_root(signed)
    assert errs == []


def test_validate_rejects_extra_key_on_lote() -> None:
    doc = generate_lotl_json([], sequence_number=1)
    doc["LoTE"]["TrustedEntitiesList"] = []
    errors = validate_lote_json(doc)
    assert errors


def test_extract_unsigned_lote() -> None:
    doc = generate_lotl_json([], sequence_number=1)
    lote = extract_unsigned_lote(doc)
    assert lote and "ListAndSchemeInformation" in lote


def test_optional_official_schema_env_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "nope.json"
    with patch.dict("os.environ", {"LOTE_JSON_SCHEMA": str(missing)}):
        assert _optional_official_schema_path() is None


def test_validate_with_official_schema_when_present(
    sample_tl_entry: TLEntry, tmp_path: Path
) -> None:
    from tools.lotl.lote_validate import get_schemas_dir

    subset_path = get_schemas_dir() / "1960201_lote_lotl_subset.schema.json"
    copy_path = tmp_path / "1960201_json_schema.json"
    copy_path.write_text(subset_path.read_text(encoding="utf-8"), encoding="utf-8")
    with patch.dict("os.environ", {"LOTE_JSON_SCHEMA": str(copy_path)}):
        doc = generate_lotl_json([sample_tl_entry], sequence_number=1)
        err = validate_lote_json(doc)
        assert err == []


def test_produce_fails_on_invalid_lote(
    tl_entries_dir: Path,
    tmp_path: Path,
    signing_key_and_cert: tuple[Path, Path],
) -> None:
    from tools.lotl import producer

    key, cert = signing_key_and_cert

    def _bad_lote(  # type: ignore[no-untyped-def]
        _entries, sequence_number: int = 1, **kwargs
    ):
        return json.loads('{"LoTE": {}}')

    with patch.object(producer, "generate_lotl_json", _bad_lote):
        code = producer.produce(
            tl_entries_dir=tl_entries_dir,
            output_dir=tmp_path,
            signing_key=key.read_text(),
            signing_cert=cert.read_text(),
        )
    assert code == 1


def test_validate_unsigned_root_missing_lote() -> None:
    assert validate_unsigned_lote_root({"foo": 1})
