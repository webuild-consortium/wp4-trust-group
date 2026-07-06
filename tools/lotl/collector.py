"""Collect TL entries from the tl_entries directory."""

import json
from pathlib import Path
from typing import Iterator

from tools.lotl.settings import VALID_TL_TYPES, get_schema_path
from tools.lotl.tl_entry import TLEntry


def collect_entries(tl_entries_dir: str | Path) -> list[TLEntry]:
    """Scan tl_entries directory and collect all valid TL entries.

    Args:
        tl_entries_dir: Path to lotl/tl_entries/

    Returns:
        List of TLEntry instances.
    """
    entries: list[TLEntry] = []
    path = Path(tl_entries_dir)

    if not path.exists():
        return entries

    for tl_type_dir in path.iterdir():
        if not tl_type_dir.is_dir():
            continue
        if tl_type_dir.name not in VALID_TL_TYPES:
            continue

        for json_file in tl_type_dir.glob("*.json"):
            participant_id = json_file.stem
            try:
                entry = _load_entry(json_file, tl_type_dir.name, participant_id)
                if entry:
                    entries.append(entry)
            except (json.JSONDecodeError, KeyError) as e:
                raise ValueError(f"Invalid entry in {json_file}: {e}") from e

    return entries


def _load_entry(
    json_path: Path,
    tl_type: str,
    participant_id: str,
) -> TLEntry | None:
    """Load a single TL entry from a JSON file."""
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    if "tl_url" not in data or "trust_anchor" not in data:
        raise ValueError(f"Missing required fields in {json_path}")

    return TLEntry.from_dict(data, tl_type, participant_id, json_path)


def iter_entries_by_type(
    entries: list[TLEntry],
) -> Iterator[tuple[str, list[TLEntry]]]:
    """Yield (tl_type, entries) for each TL type."""
    by_type: dict[str, list[TLEntry]] = {}
    for e in entries:
        by_type.setdefault(e.tl_type, []).append(e)

    for tl_type in sorted(by_type):
        yield tl_type, by_type[tl_type]
