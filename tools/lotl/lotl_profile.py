"""LoTL profile checks shared by the XML (TS 119 612) and JSON (TS 119 602) validators."""

from __future__ import annotations

import re

from tools.lotl.settings import (
    MIME_TSL_XML,
    POINTER_MIME_TYPES,
    TL_TYPE_TO_REFERENCE_URI,
    TSL_TYPE_EU_GENERIC,
)

_PLACEHOLDERS = frozenset({"", "n/a", "na", "not specified", "tbd", "unknown"})
_KNOWN_LIST_TYPES = frozenset(TL_TYPE_TO_REFERENCE_URI.values())


def electronic_address_errors(uris: list[str], field: str) -> list[str]:
    """Clause 5.3.5.2: a mailto: e-mail address, a web site, then an optional tel: number."""
    if len(uris) < 2:
        return [
            f"{field} must list a mailto: e-mail address and a web-site URI, in that "
            f"order (TS 119 612 clause 5.3.5.2), got {uris!r}"
        ]
    err: list[str] = []
    if not uris[0].startswith("mailto:"):
        err.append(f"{field}[0] must be a mailto: e-mail address (clause 5.3.5.2), got {uris[0]!r}")
    if not uris[1].startswith(("https://", "http://")):
        err.append(f"{field}[1] must be a web-site URI (clause 5.3.5.2), got {uris[1]!r}")
    if len(uris) > 3:
        err.append(
            f"{field} allows only an e-mail address, a web site and a telephone number "
            "(clause 5.3.5.2)"
        )
    elif len(uris) == 3 and not uris[2].startswith("tel:"):
        err.append(f"{field}[2] must be a tel: URI (clause 5.3.5.2), got {uris[2]!r}")
    return err


def postal_address_errors(fields: dict[str, str | None], field: str) -> list[str]:
    """Clause 5.3.5.1: a postal address that works, with a two-letter country code."""
    err: list[str] = []
    for name, value in fields.items():
        text = (value or "").strip()
        if text.lower() in _PLACEHOLDERS:
            err.append(
                f"{field}.{name} must be a real postal address value "
                f"(TS 119 612 clause 5.3.5.1), got {value!r}"
            )
        elif name in ("Country", "CountryName") and not re.fullmatch(r"[A-Z]{2}", text):
            err.append(f"{field}.{name} must be a two-letter country code (clause 5.1.5), got {value!r}")
    return err


def scheme_name_errors(names: list[str], territory: str | None) -> list[str]:
    """Clause 5.3.6: every language version reads "CC:name", CC being the scheme territory."""
    if not names:
        return ["SchemeName must contain at least one Name"]
    prefix = f"{territory}:"
    return [
        f"SchemeName {name!r} must read '{prefix}<name>' (TS 119 612 clause 5.3.6)"
        for name in names
        if not name.startswith(prefix) or not name[len(prefix):].strip()
    ]


def pointer_mime_type_errors(where: str, list_type: str | None, mime_types: list[str]) -> list[str]:
    """Clause 5.3.13 c): the MimeType qualifier must match the pointed-to list."""
    err: list[str] = []
    known = list_type in _KNOWN_LIST_TYPES
    for mime in mime_types:
        if mime not in POINTER_MIME_TYPES:
            err.append(f"{where} MimeType must be one of {sorted(POINTER_MIME_TYPES)}, got {mime!r}")
        elif known and list_type == TSL_TYPE_EU_GENERIC and mime != MIME_TSL_XML:
            err.append(
                f"{where} points to a TS 119 612 trusted list, so MimeType must be "
                f"{MIME_TSL_XML!r} (clause 6.2), got {mime!r}"
            )
        elif known and list_type != TSL_TYPE_EU_GENERIC and mime == MIME_TSL_XML:
            err.append(
                f"{where} points to a TS 119 602 LoTE, so MimeType must not be "
                f"{MIME_TSL_XML!r}"
            )
    return err
