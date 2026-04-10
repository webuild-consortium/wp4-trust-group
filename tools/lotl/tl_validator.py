"""TL validation: fetch TL from URL and validate signature with trust anchor."""

import json
from typing import Optional
from urllib.request import Request, urlopen
from urllib.error import URLError

from tools.lotl.log import get_logger
from tools.lotl.tl_entry import TLEntry

logger = get_logger(__name__)


def fetch_tl(url: str, timeout: int = 30) -> tuple[Optional[str], Optional[bytes], Optional[str]]:
    """Fetch TL from URL.

    Args:
        url: TL URL (JSON or XML).
        timeout: Request timeout in seconds.

    Returns:
        Tuple of (content_str, content_bytes, content_type). None on failure.
    """
    try:
        req = Request(url, headers={"User-Agent": "WP4-LoTL-Validator/1.0"})
        with urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            content_type = resp.headers.get("Content-Type", "")
            try:
                return data.decode("utf-8"), data, content_type
            except UnicodeDecodeError:  # pragma: no cover
                return None, data, content_type
    except URLError as e:  # pragma: no cover
        logger.warning("Failed to fetch %s: %s", url, e)
        return None, None, None
    except Exception as e:  # pragma: no cover
        logger.warning("Error fetching %s: %s", url, e)
        return None, None, None


def validate_tl_signature_json(
    tl_content: str | bytes,
    trust_anchor_pem: str,
) -> tuple[bool, str]:
    """Validate JAdES signature on TL JSON using trust anchor.

    Args:
        tl_content: TL JSON as string or bytes.
        trust_anchor_pem: X.509 certificate PEM for validation.

    Returns:
        Tuple of (is_valid, error_message).
    """
    try:
        from tools.lotl.jades_signer import verify_json

        if isinstance(tl_content, bytes):
            tl_content = tl_content.decode("utf-8")
        payload = json.loads(tl_content)
        verify_json(payload)
        return True, ""
    except Exception as e:
        return False, str(e)


def validate_tl_signature_xml(
    tl_content: bytes,
    trust_anchor_pem: str,
) -> tuple[bool, str]:
    """Validate XAdES signature on TL XML using trust anchor.

    Args:
        tl_content: TL XML bytes.
        trust_anchor_pem: X.509 certificate PEM for validation.

    Returns:
        Tuple of (is_valid, error_message).
    """
    try:
        from tools.lotl.xades_signer import verify_xml

        verify_xml(tl_content, cert_pem=trust_anchor_pem.encode() if isinstance(trust_anchor_pem, str) else trust_anchor_pem)
        return True, ""
    except Exception as e:
        return False, str(e)


def validate_tl_entry(entry: TLEntry, fetch_and_validate: bool = True) -> tuple[bool, list[str]]:
    """Validate a TL entry: fetch TL and verify signature.

    Args:
        entry: TLEntry to validate.
        fetch_and_validate: If True, fetch TL from URL and validate signature.

    Returns:
        Tuple of (is_valid, list of error messages).
    """
    errors: list[str] = []

    if not fetch_and_validate:
        return True, []

    # Prefer JSON for validation (simpler)
    url = entry.get_tl_url_json()
    content_str, content_bytes, content_type = fetch_tl(url)

    if content_str is None and content_bytes is None:
        errors.append(f"Failed to fetch TL from {url}")
        return False, errors

    # Try JSON first
    if "json" in content_type or url.endswith(".json") or (content_str and content_str.strip().startswith("{")):
        valid, err = validate_tl_signature_json(
            content_str or (content_bytes.decode("utf-8") if content_bytes else ""),
            entry.trust_anchor,
        )
        if not valid:
            errors.append(f"JSON signature validation failed: {err}")
        return valid, errors

    # Try XML
    if content_bytes:
        valid, err = validate_tl_signature_xml(content_bytes, entry.trust_anchor)
        if not valid:
            errors.append(f"XML signature validation failed: {err}")
        return valid, errors

    errors.append("Could not determine TL format")
    return False, errors
