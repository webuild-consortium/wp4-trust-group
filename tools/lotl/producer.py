"""LoTL producer: validate, collect, generate, and sign."""

import json
from pathlib import Path
from typing import Optional

from tools.lotl.collector import collect_entries
from tools.lotl.lote_validate import validate_lote_json
from tools.lotl.jades_signer import sign_json
from tools.lotl.json_generator import generate_lotl_json
from tools.lotl.log import get_logger
from tools.lotl.settings import LOTL_JSON_FILENAME, LOTL_XML_FILENAME
from tools.lotl.validator import validate_tl_entries_dir
from tools.lotl.xades_signer import sign_xml
from tools.lotl.xml_generator import generate_lotl_xml

logger = get_logger(__name__)


def get_next_sequence_number(output_dir: str | Path) -> int:
    """Determine next sequence number from existing LoTL or default to 1."""
    path = Path(output_dir)
    json_file = path / LOTL_JSON_FILENAME
    if json_file.exists():
        try:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)
            seq: int | None = None
            lote = data.get("LoTE")
            if isinstance(lote, dict):
                lasi = lote.get("ListAndSchemeInformation", {})
                if isinstance(lasi, dict):
                    raw = lasi.get("LoTESequenceNumber")
                    if raw is not None:
                        seq = int(raw)
            if seq is None:
                legacy = data.get("schemeInformation", {})
                if isinstance(legacy, dict):
                    raw = legacy.get("loteSequenceNumber")
                    if raw is not None:
                        seq = int(raw)
            if seq is not None:
                return seq + 1
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            pass

    xml_file = path / LOTL_XML_FILENAME
    if xml_file.exists():
        try:
            from lxml import etree

            tree = etree.parse(str(xml_file))
            root = tree.getroot()
            ns = {"tsl": "http://uri.etsi.org/19612/v2.4.1#"}
            seq_elem = root.find(".//tsl:TSLSequenceNumber", ns)
            if seq_elem is not None and seq_elem.text:
                return int(seq_elem.text) + 1
        except Exception:  # noqa: S110
            pass

    return 1


def produce(
    tl_entries_dir: str | Path,
    output_dir: str | Path,
    signing_key: Optional[str | bytes] = None,
    signing_cert: Optional[str | bytes] = None,
    validate_only: bool = False,
) -> int:
    """Produce and sign LoTL.

    Args:
        tl_entries_dir: Path to lotl/tl_entries/
        output_dir: Path to lotl/ (output directory)
        signing_key: Private key PEM (or path). Required unless validate_only.
        signing_cert: Certificate PEM (or path). Required unless validate_only.
        validate_only: If True, only validate tl_entries and exit.

    Returns:
        Exit code: 0 on success, non-zero on failure.
    """
    tl_entries_dir = Path(tl_entries_dir)
    output_dir = Path(output_dir)

    # 1. Validate tl_entries
    valid, errors = validate_tl_entries_dir(tl_entries_dir)
    if not valid:
        for err in errors:
            logger.error(err)
        return 1

    if validate_only:
        logger.info("Validation passed (validate-only mode)")
        return 0

    # 2. Collect entries
    entries = collect_entries(tl_entries_dir)
    if not entries:  # pragma: no cover
        logger.warning("No TL entries found")
        # Still produce empty LoTL

    # 3. Determine sequence number
    sequence = get_next_sequence_number(output_dir)

    # 4. Generate unsigned LoTL
    try:
        lotl_json = generate_lotl_json(entries, sequence_number=sequence)
        lotl_xml = generate_lotl_xml(entries, sequence_number=sequence)
    except Exception as e:
        logger.exception("LoTL generation failed: %s", e)
        return 1

    try:
        v_errs = validate_lote_json(lotl_json)
    except Exception as e:
        logger.exception("LoTE JSON validation failed unexpectedly: %s", e)
        return 1
    if v_errs:
        for e in v_errs:
            logger.error("LoTE JSON validation: %s", e)
        return 1

    # 5. Sign
    if not signing_key or not signing_cert:
        logger.error("Signing key and certificate required for produce mode")
        return 1

    try:
        signed_json = sign_json(lotl_json, signing_key, signing_cert)
        signed_xml_bytes = sign_xml(lotl_xml, signing_key, signing_cert)
    except Exception as e:  # pragma: no cover
        logger.exception("Signing failed: %s", e)
        return 1

    # 6. Write output
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / LOTL_JSON_FILENAME
    xml_path = output_dir / LOTL_XML_FILENAME

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(signed_json, f, indent=2)

    with open(xml_path, "wb") as f:
        f.write(signed_xml_bytes)

    logger.info("LoTL produced: %s, %s (sequence %d)", json_path, xml_path, sequence)
    return 0
