"""Validate TL entry files against schema and required fields."""

import json
from pathlib import Path
from typing import Optional

from tools.lotl.settings import VALID_TL_TYPES, get_schema_path


def validate_tl_entry_file(file_path: str | Path) -> list[str]:
    """Validate a single TL entry JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        List of error messages. Empty if valid.
    """
    errors: list[str] = []
    path = Path(file_path)

    if not path.exists():
        return [f"File not found: {path}"]

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]

    # Required fields
    if "tl_url" not in data:
        errors.append("Missing required field: tl_url")
    elif not isinstance(data["tl_url"], str) or not data["tl_url"].strip():
        errors.append("tl_url must be a non-empty string")

    if "trust_anchor" not in data:
        errors.append("Missing required field: trust_anchor")
    elif not isinstance(data["trust_anchor"], str):
        errors.append("trust_anchor must be a string")

    # Validate trust_anchor PEM format
    if "trust_anchor" in data and isinstance(data["trust_anchor"], str):
        ta = data["trust_anchor"]
        if "-----BEGIN CERTIFICATE-----" not in ta or "-----END CERTIFICATE-----" not in ta:
            errors.append("trust_anchor must be a valid X.509 PEM certificate")

    # Optional URL fields
    for field in ("tl_url_xml", "tl_url_json"):
        if field in data and data[field] is not None:
            if not isinstance(data[field], str):
                errors.append(f"{field} must be a string")

    # metadata must be object if present
    if "metadata" in data and data["metadata"] is not None:
        if not isinstance(data["metadata"], dict):
            errors.append("metadata must be an object")

    return errors


def validate_tl_entries_dir(tl_entries_dir: str | Path) -> tuple[bool, list[str]]:
    """Validate all TL entry files in the directory.

    Args:
        tl_entries_dir: Path to lotl/tl_entries/

    Returns:
        Tuple of (all_valid, list of error messages).
    """
    errors: list[str] = []
    path = Path(tl_entries_dir)

    if not path.exists():
        return False, [f"Directory not found: {path}"]

    for tl_type_dir in path.iterdir():
        if not tl_type_dir.is_dir():
            continue
        if tl_type_dir.name not in VALID_TL_TYPES:
            errors.append(f"Invalid TL type directory: {tl_type_dir.name}")
            continue

        for json_file in tl_type_dir.glob("*.json"):
            file_errors = validate_tl_entry_file(json_file)
            for err in file_errors:
                errors.append(f"{json_file}: {err}")

    return len(errors) == 0, errors


def validate_against_schema(
    data: dict,
    schema_path: Optional[Path] = None,
) -> list[str]:
    """Validate data against JSON schema. Returns list of errors."""
    try:
        import jsonschema  # noqa: PLC0415
    except ImportError:
        return []  # Skip schema validation if jsonschema not installed

    schema_path = schema_path or get_schema_path()
    if not schema_path.exists():
        return []

    try:
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)
        jsonschema.validate(data, schema)
        return []
    except jsonschema.ValidationError as e:
        return [str(e.message) if hasattr(e, "message") else str(e)]
    except json.JSONDecodeError:
        return []
