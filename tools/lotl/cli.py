"""CLI for LoTL producer."""

import argparse
import os
import sys
from pathlib import Path

from tools.lotl.log import configure_logging, get_logger
from tools.lotl.producer import produce
from tools.lotl.settings import LOTL_OUTPUT_DIR, TL_ENTRIES_DIR

logger = get_logger(__name__)


def _load_pem_from_env_or_path(env_var: str, path_arg: str | None) -> str | bytes | None:
    """Load PEM from path or env."""
    if path_arg:
        p = Path(path_arg)
        if p.exists():
            return p.read_text()
        return path_arg  # Inline PEM string  # pragma: no cover
    return os.environ.get(env_var)


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
        "--log-level",
        default=os.environ.get("LOTL_LOG_LEVEL", "INFO"),
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Log level",
    )

    args = parser.parse_args(argv)

    configure_logging(level=args.log_level)

    signing_key = _load_pem_from_env_or_path("LOTL_SIGNING_KEY", args.signing_key)
    signing_cert = _load_pem_from_env_or_path("LOTL_SIGNING_CERT", args.signing_cert)

    return produce(
        tl_entries_dir=args.tl_entries_dir,
        output_dir=args.output_dir,
        signing_key=signing_key,
        signing_cert=signing_cert,
        validate_only=args.validate_only,
    )


if __name__ == "__main__":
    sys.exit(main())
