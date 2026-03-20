"""Generate LoTL in JSON format (TS 119 602 LoTE structure)."""

from datetime import datetime, timezone
from typing import Any

from tools.lotl.settings import TL_TYPE_TO_LOTE_URI
from tools.lotl.tl_entry import TLEntry

LOTE_TAG = "http://uri.etsi.org/19602/LoTETag"


def generate_lotl_json(
    entries: list[TLEntry],
    sequence_number: int = 1,
    scheme_operator_name: str = "WE BUILD WP4 Trust Group",
    scheme_name: str = "WP4 List of Trusted Lists",
    scheme_information_uri: str = "https://webuild-consortium.github.io/wp4-trust-group/",
) -> dict[str, Any]:
    """Generate LoTL as JSON structure (unsigned).

    The LoTL references participant TLs by URL. Structure follows TS 119 602
    LoTE pattern adapted for List of Trusted Lists.
    """
    now = datetime.now(timezone.utc)
    issue_dt = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    next_update = now.replace(month=min(now.month + 6, 12) or 12).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    # Build list of TL pointers grouped by type
    distribution_points: list[dict[str, Any]] = []
    for entry in entries:
        dist = {
            "tlType": entry.tl_type,
            "participantId": entry.participant_id,
            "tlUrl": entry.tl_url,
            "tlUrlJson": entry.get_tl_url_json(),
            "tlUrlXml": entry.get_tl_url_xml(),
        }
        if entry.metadata:
            dist["metadata"] = entry.metadata
        distribution_points.append(dist)

    scheme_info = {
        "loteVersionIdentifier": 1,
        "loteSequenceNumber": sequence_number,
        "loteType": "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric",
        "schemeOperatorName": [{"lang": "en", "value": scheme_operator_name}],
        "schemeOperatorAddress": {
            "postalAddresses": [],
            "electronicAddress": [{"lang": "en", "uri": scheme_information_uri}],
        },
        "schemeName": [{"lang": "en", "value": scheme_name}],
        "schemeInformationURI": [{"lang": "en", "uri": scheme_information_uri}],
        "statusDeterminationApproach": "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate",
        "schemeTypeCommunityRules": [],
        "schemeTerritory": "EU",
        "listIssueDateTime": issue_dt,
        "nextUpdate": next_update,
        "distributionPoints": distribution_points,
    }

    return {
        "loteTag": LOTE_TAG,
        "schemeInformation": scheme_info,
    }
