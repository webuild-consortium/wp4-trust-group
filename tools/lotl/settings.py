"""Centralized configuration for the LoTL package."""

import os
from pathlib import Path

# LoTL root directory
LOTL_DIR = os.environ.get("LOTL_DIR", "lotl/")

# TL entries directory (folder-per-TL-type)
TL_ENTRIES_DIR = os.environ.get("LOTL_TL_ENTRIES_DIR", "lotl/tl_entries/")

# Output directory for LoTL
LOTL_OUTPUT_DIR = os.environ.get("LOTL_OUTPUT_DIR", "lotl/")

# Signing (certificate paths, private key from env)
SIGNING_CERT_PATH = os.environ.get("LOTL_SIGNING_CERT", "")
# Private key via env: LOTL_SIGNING_KEY

# Log level
LOG_LEVEL = os.environ.get("LOTL_LOG_LEVEL", "INFO")

# Valid TL types (per spec)
VALID_TL_TYPES = frozenset(
    [
        "wrpac-provider",
        "wrprc-provider",
        "pub-eaa-provider",
        "pid-provider",
        "qeaa-provider",
        "eaa-provider",
        "wallet-provider",
        "ebwoid-provider",
    ]
)

# Mapping from tl_type to ETSI identifier for the *referenced* trusted list (LoTE type or TSL type).
# Aligns with task2-trust-framework/trust-infrastructure-schema.md §3:
# - PuB-EAA (EC) and national non-qualified EAA → TS 119 602 Annex H / EUPubEAAProvidersList
# - QEAA (MS QTSP) → national TS 119 612 trusted list (TSLType EUgeneric), not Annex H
TL_TYPE_TO_REFERENCE_URI = {
    "wrpac-provider": "http://uri.etsi.org/19602/LoTEType/EUWRPACProvidersList",
    "wrprc-provider": "http://uri.etsi.org/19602/LoTEType/EUWRPRCProvidersList",
    "pub-eaa-provider": "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList",
    "pid-provider": "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
    "qeaa-provider": "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric",
    "eaa-provider": "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList",
    "wallet-provider": "http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList",
    "ebwoid-provider": "http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList",
}

# Backward-compatible alias (values are not always LoTEType URIs)
TL_TYPE_TO_LOTE_URI = TL_TYPE_TO_REFERENCE_URI

# TS 119 602-1: document type for an EU List of Trusted Lists (LoTL) LoTE
LOTL_LOTE_TYPE_URI = "http://uri.etsi.org/19602/LoTLType/EUListOfTrustedLists"

# Output filenames
LOTL_JSON_FILENAME = "list_of_trusted_lists.json"
LOTL_XML_FILENAME = "list_of_trusted_lists.xml"


def get_schema_path() -> Path:
    """Return path to the TL entry JSON schema."""
    return Path(__file__).parent / "schemas" / "tl_entry.json"
