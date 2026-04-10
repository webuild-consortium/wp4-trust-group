"""Factory for creating mock TL content in tests."""

import json
from typing import Any


def make_mock_tl_json(
    sequence: int = 1,
    lote_type: str = "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
) -> dict[str, Any]:
    """Create a minimal mock TL JSON structure (unsigned)."""
    return {
        "loteTag": "http://uri.etsi.org/19602/LoTETag",
        "schemeInformation": {
            "loteVersionIdentifier": 1,
            "loteSequenceNumber": sequence,
            "loteType": lote_type,
            "schemeOperatorName": [{"lang": "en", "value": "Test TLP"}],
            "schemeTerritory": "EU",
            "listIssueDateTime": "2025-01-01T00:00:00Z",
            "nextUpdate": "2025-07-01T00:00:00Z",
        },
        "trustedEntitiesList": {"trustedEntity": []},
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
