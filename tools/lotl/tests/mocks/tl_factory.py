"""Factory for creating mock TL content in tests."""

import json
from typing import Any

from tools.lotl.settings import LOTL_LOTE_TYPE_URI


def make_mock_lotl_json(
    sequence: int = 1,
    qualifier_lote_type: str = "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
) -> dict[str, Any]:
    """Create a minimal mock LoTE JSON structure (unsigned), schema-shaped."""
    return {
        "LoTE": {
            "ListAndSchemeInformation": {
                "LoTEVersionIdentifier": 1,
                "LoTESequenceNumber": sequence,
                "LoTEType": LOTL_LOTE_TYPE_URI,
                "SchemeOperatorName": [{"lang": "en", "value": "Test TLP"}],
                "SchemeTerritory": "EU",
                "ListIssueDateTime": "2025-01-01T00:00:00Z",
                "NextUpdate": "2025-07-01T00:00:00Z",
                "PointersToOtherLoTE": [
                    {
                        "LoTELocation": "https://example.com/tl.json",
                        "ServiceDigitalIdentities": [
                            {"X509Certificates": [{"val": "MIIB"}]}
                        ],
                        "LoTEQualifiers": [
                            {
                                "LoTEType": qualifier_lote_type,
                                "SchemeOperatorName": [
                                    {"lang": "en", "value": "Test TLP"},
                                ],
                                "SchemeTerritory": "EU",
                                "MimeType": "application/json",
                            }
                        ],
                    }
                ],
            }
        }
    }


def make_mock_tl_xml(sequence: int = 1) -> str:
    """Create a minimal mock TL XML structure (unsigned)."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#" Id="tsl-1">
  <SchemeInformation>
    <TSLVersionIdentifier>6</TSLVersionIdentifier>
    <TSLSequenceNumber>{sequence}</TSLSequenceNumber>
    <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
    <SchemeOperatorName><Name xml:lang="en">Test TLP</Name></SchemeOperatorName>
    <SchemeTerritory>EU</SchemeTerritory>
    <ListIssueDateTime>2025-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2025-07-01T00:00:00Z</NextUpdate>
  </SchemeInformation>
  <TrustServiceProviderList/>
</TrustServiceStatusList>"""
