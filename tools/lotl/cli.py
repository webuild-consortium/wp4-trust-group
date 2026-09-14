"""CLI for LoTL producer."""

import argparse
import os
import sys
from pathlib import Path

from tools.lotl.cert_expiry import run_expiry_checks
from tools.lotl.log import configure_logging, get_logger
from tools.lotl.pem_util import normalize_pem_for_ci
from tools.lotl.producer import produce
from tools.lotl.settings import LOTL_OUTPUT_DIR, PUBLISHED_LOTL_JSON_URL, TL_ENTRIES_DIR

logger = get_logger(__name__)


def _load_pem_from_env_or_path(env_var: str, path_arg: str | None) -> str | bytes | None:
    """Load PEM from path or env."""
    if path_arg:
        p = Path(path_arg)
        if p.exists():
            return p.read_text()
        return path_arg  # Inline PEM string  # pragma: no cover
    raw = os.environ.get(env_var)
    if raw is None:
        return None
    return normalize_pem_for_ci(raw)


def main(argv: list[str] | None = None) -> int:
    """Entry point for LoTL CLI."""
    parser = argparse.ArgumentParser(
        description="LoTL (List of Trusted Lists) producer and validator",
    )
    parser.add_argument(
        "--tl-entries-dir",
        default=TL_ENTRIES_DIR,
        help="Path to lotl/tl_entries/",
    )
    parser.add_argument(
        "--output-dir",
        default=LOTL_OUTPUT_DIR,
        help="Path to lotl/ output directory",
    )
    parser.add_argument(
        "--signing-key",
        help="Path to signing key PEM or inline PEM. Else LOTL_SIGNING_KEY env.",
    )
    parser.add_argument(
        "--signing-cert",
        help="Path to signing cert PEM or inline PEM. Else LOTL_SIGNING_CERT env.",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate tl_entries, do not produce/sign",
    )
    parser.add_argument(
        "--check-expiry",
        action="store_true",
        help=(
            "Check certificate expiry for tl_entries trust anchors, an optional "
            "published LoTL (--lotl-json), and the signing certificate if provided. "
            "Does not produce or sign."
        ),
    )
    parser.add_argument(
        "--lotl-json",
        help=(
            "Path or URL of a published LoTL JSON to inspect for expired "
            f"signing and pointer certificates (default for scheduled CI: "
            f"{PUBLISHED_LOTL_JSON_URL})"
        ),
    )
    parser.add_argument(
        "--log-level",
        default=os.environ.get("LOTL_LOG_LEVEL", "INFO"),
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Log level",
    )

    args = parser.parse_args(argv)

    configure_logging(level=args.log_level)

    signing_key = _load_pem_from_env_or_path("LOTL_SIGNING_KEY", args.signing_key)
    signing_cert = _load_pem_from_env_or_path("LOTL_SIGNING_CERT", args.signing_cert)

    if args.check_expiry:
        entries_dir = Path(args.tl_entries_dir)
        entries_arg = entries_dir if entries_dir.exists() else None
        if entries_arg is None and not args.lotl_json and not signing_cert:
            logger.error(
                "Nothing to check: provide --tl-entries-dir, --lotl-json, "
                "or a signing certificate"
            )
            return 1
        errors = run_expiry_checks(
            tl_entries_dir=entries_arg,
            lotl_json_source=args.lotl_json,
            signing_cert_pem=signing_cert,
        )
        for err in errors:
            logger.error(err)
        if errors:
            logger.error("Certificate expiry check failed (%d error(s))", len(errors))
            return 1
        logger.info("Certificate expiry check passed")
        return 0

    return produce(
        tl_entries_dir=args.tl_entries_dir,
        output_dir=args.output_dir,
        signing_key=signing_key,
        signing_cert=signing_cert,
        validate_only=args.validate_only,
    )


if __name__ == "__main__":
    sys.exit(main())
