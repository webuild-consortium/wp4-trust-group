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
# Aligns with ARF + ETSI TS 119 612 / TS 119 602:
# - PuB-EAA (EC) → TS 119 602 Annex H / EUPubEAAProvidersList
# - QEAA (MS QTSP) and non-qualified EAA (MS TLP) → national TS 119 612 TSL
#   (TSLType EUgeneric); disambiguated by ServiceTypeIdentifier
#   Svctype/EAA/Q vs Svctype/EAA (not by a second 602 LoTE type — Annex H is
#   Pub-EAA only).
TL_TYPE_TO_REFERENCE_URI = {
    "wrpac-provider": "http://uri.etsi.org/19602/LoTEType/EUWRPACProvidersList",
    "wrprc-provider": "http://uri.etsi.org/19602/LoTEType/EUWRPRCProvidersList",
    "pub-eaa-provider": "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList",
    "pid-provider": "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
    "qeaa-provider": "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric",
    "eaa-provider": "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric",
    "wallet-provider": "http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList",
    "ebwoid-provider": "http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList",
}

# National TS 119 612 XML Trusted Lists (not TS 119 602 LoTE / Annex H).
TS_119_612_TL_TYPES = frozenset({"qeaa-provider", "eaa-provider"})

# ETSI TS 119 612 clause 5.5.1.1 — how EAA vs QEAA vs Pub-EAA are distinguished
# on a national TSL (same TSLType EUgeneric).
SVC_TYPE_EAA = "http://uri.etsi.org/TrstSvc/Svctype/EAA"
SVC_TYPE_EAA_Q = "http://uri.etsi.org/TrstSvc/Svctype/EAA/Q"
SVC_TYPE_EAA_PUB = "http://uri.etsi.org/TrstSvc/Svctype/EAA/Pub-EAA"

MIME_TSL_XML = "application/vnd.etsi.tsl+xml"

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
