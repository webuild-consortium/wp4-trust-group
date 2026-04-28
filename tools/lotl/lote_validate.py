"""Validate unsigned LoTE JSON (LoTL) for TS 119 602-1 / ``1960201`` interop.

- **JSON Schema** via ``jsonschema``:
  - default: vendored official ETSI ``1960201_json_schema.json`` (with local RFC refs),
  - override: ``LOTE_JSON_SCHEMA`` path,
  - fallback: local subset schema if official schema is unavailable.
- **Semantic checks** — required fields, LoTL profile, ISO-8601 datetimes, pointer / qualifier invariants
  (aligned with ``sirosfoundation/g119612`` ``ListOfTrustedEntities.Validate`` where applicable).
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Generator

from tools.lotl.settings import LOTL_LOTE_TYPE_URI, TL_TYPE_TO_REFERENCE_URI

_SUBSET_NAME = "1960201_lote_lotl_subset.schema.json"
_OPTIONAL_OFFICIAL = "1960201_json_schema.json"


def get_schemas_dir() -> Path:
    return Path(__file__).resolve().parent / "schemas"


def _load_json(path: Path) -> Any:
    import json

    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _iter_validation_errors(
    instance: Any,
    schema: Any,
) -> Generator[str, None, None]:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        yield (
            "JSON Schema validation could not be performed because the "
            "'jsonschema' package is not installed"
        )
        return

    v = Draft202012Validator(schema, format_checker=FormatChecker())
    for e in v.iter_errors(instance):
        path = " / ".join(str(p) for p in e.absolute_path) or "$"
        yield f"{path}: {e.message}"


def validate_json_schema(
    document: dict[str, Any],
    *,
    schema: dict[str, Any],
) -> list[str]:
    """Validate ``document`` with the given JSON Schema. Returns a list of messages."""
    return list(_iter_validation_errors(document, schema))


def _subset_schema() -> dict[str, Any]:
    return _load_json(get_schemas_dir() / _SUBSET_NAME)


def _optional_official_schema_path() -> Path | None:
    env = os.environ.get("LOTE_JSON_SCHEMA", "").strip()
    if env:
        p = Path(env)
        return p if p.is_file() else None
    p = get_schemas_dir() / _OPTIONAL_OFFICIAL
    return p if p.is_file() else None


def _validate_datetime_utc(s: str, name: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(s, str) or not s:
        return [f"{name} must be a non-empty string"]
    if not re.match(
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$",
        s,
    ):
        errors.append(
            f"{name} must be a UTC instant in form YYYY-MM-DDThh:mm:ssZ (TS 119 602 clause 6.1.3)"
        )
        return errors
    try:
        t = s[:-1] + "+00:00" if s.endswith("Z") else s
        datetime.fromisoformat(t)
    except ValueError:
        errors.append(f"{name} is not a valid date-time: {s!r}")
    return errors


def _validate_list_and_scheme(s: Any) -> list[str]:
    if not isinstance(s, dict):
        return ["ListAndSchemeInformation must be an object"]
    err: list[str] = []
    for req in (
        "LoTEVersionIdentifier",
        "LoTESequenceNumber",
        "LoTEType",
        "SchemeOperatorName",
        "SchemeOperatorAddress",
        "ListIssueDateTime",
        "NextUpdate",
    ):
        if req not in s:
            err.append(f"ListAndSchemeInformation missing required field: {req}")
    if err:
        return err
    if not isinstance(s.get("LoTEVersionIdentifier"), int):
        err.append("LoTEVersionIdentifier must be an integer")
    if not isinstance(s.get("LoTESequenceNumber"), int):
        err.append("LoTESequenceNumber must be an integer")
    lote_type = s.get("LoTEType", "")
    if lote_type != LOTL_LOTE_TYPE_URI:
        err.append(
            f"ListAndSchemeInformation.LoTEType must be the EU LoTL type "
            f"{LOTL_LOTE_TYPE_URI!r} for this LoTL producer (got {lote_type!r})"
        )
    if not s.get("SchemeOperatorName"):
        err.append("SchemeOperatorName must be a non-empty name set")
    err.extend(
        _validate_datetime_utc(s.get("ListIssueDateTime", ""), "ListIssueDateTime")
    )
    err.extend(_validate_datetime_utc(s.get("NextUpdate", ""), "NextUpdate"))
    addr = s.get("SchemeOperatorAddress")
    if not isinstance(addr, dict):
        err.append("SchemeOperatorAddress must be an object")
    else:
        for k in ("SchemeOperatorPostalAddress", "SchemeOperatorElectronicAddress"):
            if k not in addr or not isinstance(addr[k], list):
                err.append(f"SchemeOperatorAddress must contain a {k} array")
        eaddr = addr.get("SchemeOperatorElectronicAddress", [])
        if eaddr:
            for i, m in enumerate(eaddr):
                if not isinstance(m, dict) or "uriValue" not in m:
                    err.append(
                        f"SchemeOperatorElectronicAddress[{i}] must be NonEmptyMultiLangURI "
                        "with uriValue"
                    )
    dps = s.get("DistributionPoints", [])
    if dps is not None:
        if not isinstance(dps, list):
            err.append("DistributionPoints must be an array of URI strings")
        else:
            for i, u in enumerate(dps):
                if not isinstance(u, str) or not u.strip():
                    err.append(
                        f"DistributionPoints[{i}] must be a non-empty string (URI per clause 6.3.16)"
                    )
    ptrs = s.get("PointersToOtherLoTE", [])
    if not isinstance(ptrs, list):
        return err + ["PointersToOtherLoTE must be an array"]
    for i, p in enumerate(ptrs):
        if not isinstance(p, dict):
            err.append(f"PointersToOtherLoTE[{i}] must be an object")
            continue
        if not p.get("LoTELocation"):
            err.append(f"PointersToOtherLoTE[{i}].LoTELocation is required and non-empty")
        sdis = p.get("ServiceDigitalIdentities", [])
        if not isinstance(sdis, list) or not sdis:
            err.append(
                f"PointersToOtherLoTE[{i}] must include a non-empty ServiceDigitalIdentities array "
                "(clause 6.3.13)"
            )
        quals = p.get("LoTEQualifiers", [])
        if not isinstance(quals, list) or not quals:
            err.append(
                f"PointersToOtherLoTE[{i}] must have a non-empty LoTEQualifiers array (clause 6.3.13)"
            )
        else:
            for j, q in enumerate(quals):
                if not isinstance(q, dict):
                    err.append(f"PointersToOtherLoTE[{i}].LoTEQualifiers[{j}] must be an object")
                    continue
                for qk in ("LoTEType", "SchemeOperatorName", "MimeType"):
                    if not q.get(qk):
                        err.append(
                            f"PointersToOtherLoTE[{i}].LoTEQualifiers[{j}].{qk} is required"
                        )
                # Referenced list type: known to our policy map (includes qeaa TSL EUgeneric)
                qt = q.get("LoTEType")
                if isinstance(qt, str) and qt not in set(TL_TYPE_TO_REFERENCE_URI.values()):
                    err.append(
                        f"PointersToOtherLoTE[{i}].LoTEQualifiers[{j}].LoTEType "
                        f"is not a known TL/LoTE type URI: {qt!r}"
                    )
    return err


def validate_lote_semantics(lote: dict[str, Any]) -> list[str]:
    """g119612-style + LoTL policy checks (no ``TrustedEntitiesList`` for LoTL-only)."""
    if not isinstance(lote, dict):
        return ["LoTE value must be an object"]
    if "ListAndSchemeInformation" not in lote:
        return ['LoTE must contain "ListAndSchemeInformation"']
    err = _validate_list_and_scheme(lote["ListAndSchemeInformation"])
    if "TrustedEntitiesList" in lote:
        err.append(
            "This LoTL producer must not include TrustedEntitiesList in JSON (use pointers only)"
        )
    if set(lote.keys()) != {"ListAndSchemeInformation"}:
        err.append(
            f"LoTE for LoTL must contain only ListAndSchemeInformation, got {set(lote.keys())!r}"
        )
    return err


def extract_unsigned_lote(
    data: dict[str, Any],
) -> dict[str, Any] | None:
    """Return the ``LoTE`` object, tolerating a signed JAdES wrapper (``signature`` key)."""
    if "LoTE" in data and isinstance(data["LoTE"], dict):
        return data["LoTE"]
    return None


def validate_unsigned_lote_root(document: dict[str, Any]) -> list[str]:
    """
    Validate the root **unsigned** document ``{"LoTE": {...}}`` (no ``signature``), or
    extract ``LoTE`` from a full signed file.
    """
    if "signature" in document and "LoTE" in document:
        inner = {"LoTE": document["LoTE"]}
    elif "LoTE" in document and isinstance(document.get("LoTE"), dict):
        inner = document
    else:
        return ['Root must contain a "LoTE" object (signed files may add "signature")']
    if not isinstance(document.get("LoTE", {}), dict):
        return ["LoTE must be an object"]
    return validate_lote_json(inner)


def validate_lote_json(document: dict[str, Any]) -> list[str]:
    """Run JSON Schema validation (official preferred) and semantic checks.

    ``document`` is ``{"LoTE": {...}}`` (unsigned only).
    """
    errors: list[str] = []
    off = _optional_official_schema_path()
    if off is not None:
        try:
            official = _load_json(off)
            if isinstance(official, dict) and "$id" not in official:
                # Ensure relative $ref (e.g. rfcs/rfc7517.json) resolve from file location.
                official = dict(official)
                official["$id"] = off.resolve().as_uri()
            errors.extend(validate_json_schema(document, schema=official))
        except OSError as e:
            errors.append(f"Failed to read official schema: {e}")
    else:
        errors.extend(validate_json_schema(document, schema=_subset_schema()))
    lote = document.get("LoTE", {})
    if isinstance(lote, dict):
        errors.extend(validate_lote_semantics(lote))
    return errors
