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

# TS 119 612 XML namespace (Annex B.0 / D.1). The 19612_xsd.xsd targetNamespace
# is 02231/v2#, not the document-number URI used in some WP4 drafts.
NS_TSL = "http://uri.etsi.org/02231/v2#"
NS_TSL_LEGACY = "http://uri.etsi.org/19612/v2.4.1#"
NS_TSL_ADDITIONAL = "http://uri.etsi.org/02231/v2/additionaltypes#"
TSL_XSD_SCHEMA_LOCATION = (
    "https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd"
)

# TS 119 612 compiled-list (LoTL) identifiers (clause 5.3.3 / D.5)
TSL_TAG_URI = "http://uri.etsi.org/19612/TSLTag"
LOTL_TSL_TYPE_URI = (
    "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUlistofthelists"
)
LOTL_SCHEME_RULES_URI = (
    "http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUlistofthelists"
)
LOTL_STATUS_DETN_URI = (
    "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate"
)
# Clause 5.3.12: 65535 means historical information is never removed.
LOTL_HISTORICAL_INFORMATION_PERIOD = 65535

# Clause 5.3.10. Also the "CC:" prefix of the scheme name (clause 5.3.6).
LOTL_SCHEME_TERRITORY = "EU"

# Scheme operator contact (clause 5.3.5). Override with the LOTL_OPERATOR_* environment variables.
LOTL_OPERATOR_EMAIL = os.environ.get("LOTL_OPERATOR_EMAIL", "wp4-trust@example.org")
LOTL_OPERATOR_WEBSITE = os.environ.get(
    "LOTL_OPERATOR_WEBSITE", "https://webuild-consortium.github.io/wp4-trust-group/"
)
LOTL_OPERATOR_POSTAL_ADDRESS = {
    "StreetAddress": os.environ.get("LOTL_OPERATOR_STREET", "Rome"),
    "Locality": os.environ.get("LOTL_OPERATOR_LOCALITY", "Rome"),
    "PostalCode": os.environ.get("LOTL_OPERATOR_POSTAL_CODE", "00100"),
    "CountryName": os.environ.get("LOTL_OPERATOR_COUNTRY", "IT"),
}

TSL_TYPE_EU_GENERIC = "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric"

# MimeType qualifier of a pointer (clause 5.3.13 c)). Only the TSL type is registered
# (clause 6.2.2). TS 119 602 V1.1.1 requires a MimeType but registers no LoTE media
# type, so the two LoTE values are a WP4 convention (Task 3 implementation profile).
MIME_TSL_XML = "application/vnd.etsi.tsl+xml"
MIME_LOTE_XML = "application/xml"
MIME_LOTE_JSON = "application/json"
POINTER_MIME_TYPES = frozenset([MIME_TSL_XML, MIME_LOTE_XML, MIME_LOTE_JSON])

# Output filenames
LOTL_JSON_FILENAME = "list_of_trusted_lists.json"
LOTL_XML_FILENAME = "list_of_trusted_lists.xml"


def get_schema_path() -> Path:
    """Return path to the TL entry JSON schema."""
    return Path(__file__).parent / "schemas" / "tl_entry.json"
