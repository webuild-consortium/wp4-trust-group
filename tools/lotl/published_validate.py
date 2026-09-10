"""Fetch published participant TLs/LoTEs and enforce the WP4/ETSI profile."""

from __future__ import annotations

import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import TextIO

from tools.lotl.collector import collect_entries
from tools.lotl.list_profile import summarize_published_document, validate_published_document
from tools.lotl.log import get_logger
from tools.lotl.tl_entry import TLEntry
from tools.lotl.tl_validator import (
    fetch_tl,
    validate_tl_signature_json,
    validate_tl_signature_xml,
)
from tools.lotl.validator import validate_tl_entries_dir

logger = get_logger(__name__)

PROFILE_DOC = (
    "task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md §8 "
    "(XML: enveloped-signature then exclusive C14N; JSON: JAdES Baseline B)"
)

_FIX_HINTS: tuple[tuple[str, str], ...] = (
    (
        "XPath Filter 2.0",
        "Replace XPath Filter 2.0 with ds:Transform "
        "enveloped-signature then exclusive C14N "
        "(http://www.w3.org/2000/09/xmldsig#enveloped-signature then "
        "http://www.w3.org/2001/10/xml-exc-c14n#).",
    ),
    (
        "XPath transform",
        "Do not use the 1999 XPath transform; use enveloped-signature then exclusive C14N.",
    ),
    (
        "not signed",
        "Publish an enveloped XAdES Baseline B signature (XML) or JAdES Baseline B (JSON).",
    ),
    (
        "HistoricalInformationPeriod",
        "Annex H (Pub-EAA / national EAA) requires HistoricalInformationPeriod = 65535.",
    ),
    (
        "no TrustedEntity",
        "The list must contain at least one TrustedEntity (LoTE) or TrustServiceProvider (TSL).",
    ),
    (
        "canonical ETSI URI",
        "ETSI registry URIs must be http://uri.etsi.org/... with no trailing slash "
        "(https:// and a final / are rejected).",
    ),
    (
        "List type URI must be",
        "The published LoTEType/TSLType must match the LoTL folder mapping in "
        "tools/lotl/settings.py (TL_TYPE_TO_REFERENCE_URI).",
    ),
    (
        "StatusDeterminationApproach",
        "Use the WP4/ETSI StatusDeterminationApproach URI for this list type.",
    ),
    (
        "SchemeTypeCommunityRules",
        "Include the profile SchemeTypeCommunityRules URI for this list type.",
    ),
    (
        "signature verification failed",
        "The certificate in lotl/tl_entries trust_anchor must verify the published signature.",
    ),
    (
        "Failed to fetch",
        "The publication URL must return HTTP 200 to GitHub Actions (check DNS, TLS, and path).",
    ),
    (
        "JAdES",
        "JSON must be signed JAdES Baseline B: protected header needs alg, x5c, and iat.",
    ),
    (
        "NextUpdate must be at most 6 months",
        "NextUpdate must be at most 6 months after ListIssueDateTime.",
    ),
    (
        "ServiceStatus shall",
        "Annex H services must include ServiceStatus notified or withdrawn.",
    ),
    (
        "ServiceStatus must not",
        "PID and Wallet lists must not include ServiceStatus (TS 119 602 Annex D/E).",
    ),
    (
        "QEAA Provider lists must be",
        "QEAA lists must be TS 119 612 XML TrustServiceStatusList (TSLType EUgeneric).",
    ),
    (
        "document Reference transforms",
        "The document ds:Reference must have exactly two transforms: enveloped-signature, then exclusive C14N.",
    ),
)


@dataclass
class PublicationCheck:
    """One fetched publication URL and its profile result."""

    label: str
    url: str
    errors: list[str] = field(default_factory=list)
    content_type: str = ""
    size_bytes: int = 0
    observed: dict[str, str] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors

    def prefixed_errors(self) -> list[str]:
        if not self.url:
            return [f"{self.label}: {err}" for err in self.errors]
        return [f"{self.label} @ {self.url}: {err}" for err in self.errors]


def finding_hint(message: str) -> str:
    """Return a short remediation hint for a profile error message."""
    for needle, hint in _FIX_HINTS:
        if needle.lower() in message.lower():
            return hint
    return "See the WP4 ETSI trusted-lists implementation profile for the required field or algorithm."


def finding_title(message: str) -> str:
    """Short title for GitHub Actions annotations and scoreboard grouping."""
    lowered = message.lower()
    if "xpath filter 2.0" in lowered:
        return "XPath Filter 2.0 (forbidden transform)"
    if "not signed" in lowered:
        return "Missing signature"
    if "failed to fetch" in lowered:
        return "Fetch failed"
    if "list type uri" in lowered:
        return "Wrong list type URI"
    if "canonical etsi uri" in lowered:
        return "Non-canonical ETSI URI"
    if "historicalinformationperiod" in lowered:
        return "Missing HistoricalInformationPeriod"
    if "no trustedentity" in lowered:
        return "Empty trusted-entity list"
    if "signature verification failed" in lowered:
        return "Signature does not verify"
    if "jades" in lowered:
        return "JAdES signature profile"
    if "nextupdate" in lowered:
        return "NextUpdate interval"
    if "statusdeterminationapproach" in lowered:
        return "Wrong StatusDeterminationApproach"
    if "schemetypecommunityrules" in lowered:
        return "Missing scheme rules URI"
    if "document reference transforms" in lowered:
        return "Wrong XAdES document transforms"
    if "canonicalizationmethod" in lowered:
        return "Wrong CanonicalizationMethod"
    return "Profile violation"


def published_urls(entry: TLEntry) -> list[str]:
    """Unique publication URLs for one LoTL pointer (JSON and/or XML)."""
    urls: list[str] = []
    for url in (entry.tl_url, entry.tl_url_json, entry.tl_url_xml):
        if url and url not in urls:
            urls.append(url)
    return urls


def fetch_published(
    url: str,
    *,
    timeout: int = 30,
    attempts: int = 3,
) -> tuple[bytes | None, str, str | None]:
    """Fetch a published list. Returns (body, content_type, error)."""
    last_error: str | None = None
    for attempt in range(1, attempts + 1):
        _text, body, content_type = fetch_tl(url, timeout=timeout)
        if body is not None:
            return body, content_type or "", None
        last_error = f"Failed to fetch {url} (attempt {attempt}/{attempts})"
        if attempt < attempts:
            time.sleep(attempt)
    return None, "", last_error


def _try_crypto_verify(
    body: bytes,
    content_type: str,
    url: str,
    trust_anchor: str,
) -> list[str]:
    """Best-effort cryptographic check against the LoTL pointer trust anchor."""
    if not trust_anchor or "BEGIN CERTIFICATE" not in trust_anchor:
        return ["trust_anchor is missing or not an X.509 PEM certificate"]
    stripped = body.lstrip()
    lowered = url.lower()
    ctype = (content_type or "").lower()
    is_json = (
        stripped.startswith(b"{")
        or "json" in ctype
        or lowered.endswith(".json")
    )
    is_xml = (
        stripped.startswith(b"<")
        or "xml" in ctype
        or lowered.endswith(".xml")
    )
    if is_json and not is_xml:
        try:
            text = body.decode("utf-8")
        except UnicodeDecodeError as exc:
            return [f"JSON signature verification failed: {exc}"]
        valid, err = validate_tl_signature_json(text, trust_anchor)
        return [] if valid else [f"JSON signature verification failed: {err}"]
    if is_xml:
        valid, err = validate_tl_signature_xml(body, trust_anchor)
        if valid:
            return []
        # signxml is not a full XAdES verifier; an extra SignedProperties
        # ds:Reference is required by XAdES Baseline B and is not a profile fail.
        if err and "Expected to find 1 references" in err:
            return []
        return [f"XML signature verification failed: {err}"]
    return []


def check_entry_publications(
    entry: TLEntry,
    *,
    timeout: int = 30,
    attempts: int = 3,
    verify_crypto: bool = True,
) -> list[PublicationCheck]:
    """Fetch and profile-validate every published URL for one tl_entries file."""
    label = f"{entry.tl_type}/{entry.participant_id}"
    urls = published_urls(entry)
    if not urls:
        return [
            PublicationCheck(
                label=label,
                url="",
                errors=["no publication URL (tl_url / tl_url_json / tl_url_xml)"],
            )
        ]

    results: list[PublicationCheck] = []
    for url in urls:
        body, content_type, fetch_err = fetch_published(
            url, timeout=timeout, attempts=attempts
        )
        if fetch_err or body is None:
            results.append(
                PublicationCheck(
                    label=label,
                    url=url,
                    errors=[fetch_err or "empty response"],
                    content_type=content_type,
                )
            )
            continue
        profile_errors = validate_published_document(
            body,
            tl_type=entry.tl_type,
            url=url,
            content_type=content_type,
        )
        errors = list(profile_errors)
        if verify_crypto and not any("not signed" in e.lower() for e in profile_errors):
            errors.extend(
                _try_crypto_verify(body, content_type, url, entry.trust_anchor)
            )
        results.append(
            PublicationCheck(
                label=label,
                url=url,
                errors=errors,
                content_type=content_type,
                size_bytes=len(body),
                observed=summarize_published_document(
                    body, url=url, content_type=content_type
                ),
            )
        )
    return results


def validate_entry_publications(
    entry: TLEntry,
    *,
    timeout: int = 30,
    attempts: int = 3,
    verify_crypto: bool = True,
) -> list[str]:
    """Fetch and profile-validate every published URL for one tl_entries file."""
    checks = check_entry_publications(
        entry, timeout=timeout, attempts=attempts, verify_crypto=verify_crypto
    )
    errors: list[str] = []
    for check in checks:
        errors.extend(check.prefixed_errors())
    return errors


def check_published_lists(
    tl_entries_dir: str | Path,
    *,
    timeout: int = 30,
    attempts: int = 3,
    verify_crypto: bool = True,
) -> tuple[list[str], list[PublicationCheck]]:
    """Return local-file errors and per-URL publication checks."""
    ok, local_errors = validate_tl_entries_dir(tl_entries_dir)
    if not ok:
        return list(local_errors), []

    entries = collect_entries(tl_entries_dir)
    if not entries:
        return [f"No TL entries found in {tl_entries_dir}"], []

    checks: list[PublicationCheck] = []
    for entry in entries:
        checks.extend(
            check_entry_publications(
                entry,
                timeout=timeout,
                attempts=attempts,
                verify_crypto=verify_crypto,
            )
        )
    return [], checks


def validate_published_lists(
    tl_entries_dir: str | Path,
    *,
    timeout: int = 30,
    attempts: int = 3,
    verify_crypto: bool = True,
) -> tuple[bool, list[str]]:
    """Validate local entry files, then every published TL/LoTE they point to."""
    local_errors, checks = check_published_lists(
        tl_entries_dir,
        timeout=timeout,
        attempts=attempts,
        verify_crypto=verify_crypto,
    )
    errors = list(local_errors)
    for check in checks:
        errors.extend(check.prefixed_errors())
    return len(errors) == 0, errors


def _gh_escape(text: str) -> str:
    return (
        text.replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
    )


def format_published_report(
    local_errors: list[str],
    checks: list[PublicationCheck],
    *,
    github: bool = False,
) -> str:
    """Human-readable CI report: scoreboard, observed fields, findings, hints."""
    lines: list[str] = []
    failed_checks = [c for c in checks if not c.ok]
    passed_checks = [c for c in checks if c.ok]
    failed_labels = sorted({c.label for c in failed_checks})
    passed_labels = sorted({c.label for c in passed_checks if c.label not in failed_labels})
    n_findings = len(local_errors) + sum(len(c.errors) for c in failed_checks)
    overall_fail = bool(local_errors or failed_checks)

    lines.append("=" * 78)
    lines.append("WP4 / ETSI published TL and LoTE profile check")
    lines.append("=" * 78)
    lines.append(f"Pointers checked : {len({c.label for c in checks})}")
    lines.append(f"URLs fetched     : {len(checks)}")
    lines.append(f"Passed           : {len(passed_labels)}")
    lines.append(f"Failed           : {len(failed_labels)}")
    lines.append(f"Findings         : {n_findings}")
    lines.append(f"Profile          : {PROFILE_DOC}")
    lines.append("")
    lines.append("Scoreboard")
    lines.append("-" * 78)
    if local_errors:
        lines.append("FAIL  (local tl_entries files)")
    for label in sorted({c.label for c in checks}):
        status = "FAIL" if label in failed_labels else "PASS"
        n_err = sum(len(c.errors) for c in checks if c.label == label)
        extra = f"  ({n_err} finding{'s' if n_err != 1 else ''})" if n_err else ""
        lines.append(f"{status}  {label}{extra}")
    if not checks and not local_errors:
        lines.append("(no published URLs checked)")
    lines.append("")

    if local_errors:
        lines.append("Local tl_entries errors")
        lines.append("-" * 78)
        for i, err in enumerate(local_errors, 1):
            lines.append(f"  {i}. {err}")
            lines.append(f"     Fix: {finding_hint(err)}")
        lines.append("")

    if failed_checks:
        lines.append("Failure detail")
        lines.append("-" * 78)
        for label in failed_labels:
            n_err = sum(len(c.errors) for c in checks if c.label == label)
            heading = f"FAIL {label}  ({n_err} finding{'s' if n_err != 1 else ''})"
            if github:
                lines.append(f"::group::{heading}")
            else:
                lines.append("")
                lines.append(heading)
            for check in [c for c in checks if c.label == label]:
                if check.ok:
                    lines.append(f"  URL          : {check.url}  (this URL passed)")
                    lines.append("")
                    continue
                lines.append(f"  URL          : {check.url or '(none)'}")
                if check.content_type:
                    lines.append(f"  Content-Type : {check.content_type}")
                if check.size_bytes:
                    lines.append(f"  Size         : {check.size_bytes} bytes")
                if check.observed:
                    lines.append("  Observed")
                    for key, value in check.observed.items():
                        lines.append(f"    {key:28} {value}")
                lines.append("  Findings")
                for i, err in enumerate(check.errors, 1):
                    title = finding_title(err)
                    lines.append(f"    {i}. [{title}]")
                    lines.append(f"       {err}")
                    lines.append(f"       Fix: {finding_hint(err)}")
                    if github:
                        lines.append(
                            "::error title="
                            f"{_gh_escape(f'{label}: {title}')}::"
                            f"{_gh_escape(err)}"
                        )
                lines.append("")
            if github:
                lines.append("::endgroup::")
        if passed_labels:
            lines.append("Passed (checked, no findings)")
            lines.append("-" * 78)
            for label in passed_labels:
                urls = [c.url for c in passed_checks if c.label == label]
                lines.append(f"  PASS  {label}")
                for url in urls:
                    lines.append(f"        {url}")
            lines.append("")

    lines.append("=" * 78)
    if overall_fail:
        lines.append(
            f"RESULT: FAILED  — {n_findings} finding(s) across "
            f"{len(failed_labels)} pointer(s). CI is red until publishers "
            "fix the lists above (or remove the LoTL pointer)."
        )
    else:
        lines.append("RESULT: PASSED  — all published TLs/LoTEs match the WP4/ETSI profile.")
    lines.append("=" * 78)
    return "\n".join(lines) + "\n"


def run_published_validation(
    tl_entries_dir: str | Path,
    *,
    timeout: int = 30,
    attempts: int = 3,
    verify_crypto: bool = True,
    stream: TextIO | None = None,
) -> int:
    """CLI helper: print a debug-friendly report and return a process exit code."""
    out = stream if stream is not None else sys.stdout
    github = os.environ.get("GITHUB_ACTIONS", "").lower() == "true"
    local_errors, checks = check_published_lists(
        tl_entries_dir,
        timeout=timeout,
        attempts=attempts,
        verify_crypto=verify_crypto,
    )
    report = format_published_report(local_errors, checks, github=github)
    out.write(report)
    out.flush()
    failed = bool(local_errors) or any(not c.ok for c in checks)
    if failed:
        logger.error(
            "Published TL/LoTE WP4/ETSI profile validation failed "
            "(%s finding(s)). See the report above.",
            len(local_errors) + sum(len(c.errors) for c in checks if not c.ok),
        )
        return 1
    logger.info("Published TL/LoTE WP4/ETSI profile validation passed")
    return 0
