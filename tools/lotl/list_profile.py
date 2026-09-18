"""WP4 / ETSI profile checks for published participant TLs and LoTEs.

Enforces the signature and list-type constraints from:

- ETSI TS 119 612 V2.4.1 Annex B.1 (enveloped XAdES transforms)
- ETSI TS 119 602 V1.1.1 Annex D–I (LoTE types, JAdES / XAdES)
- WP4 ``etsi_trusted_lists_implementation_profile.md``
"""

from __future__ import annotations

import base64
import json
from calendar import monthrange
from datetime import datetime, timezone
from typing import Any

from lxml import etree

from tools.lotl.settings import (
    SVC_TYPE_EAA,
    SVC_TYPE_EAA_Q,
    TS_119_612_TL_TYPES,
    TL_TYPE_TO_REFERENCE_URI,
)

ENVELOPED_SIGNATURE_URI = "http://www.w3.org/2000/09/xmldsig#enveloped-signature"
EXCLUSIVE_C14N_URI = "http://www.w3.org/2001/10/xml-exc-c14n#"
XPATH_FILTER2_URI = "http://www.w3.org/2002/06/xmldsig-filter2"
XPATH_1999_URI = "http://www.w3.org/TR/1999/REC-xpath-19991116"

FORBIDDEN_TRANSFORM_URIS = frozenset(
    {
        XPATH_FILTER2_URI,
        XPATH_1999_URI,
        # Inclusive C14N is not the mandated exclusive algorithm.
        "http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        "http://www.w3.org/2006/12/xml-c14n11",
        "http://www.w3.org/2001/10/xml-exc-c14n#WithComments",
    }
)

MANDATED_DOCUMENT_TRANSFORMS = (ENVELOPED_SIGNATURE_URI, EXCLUSIVE_C14N_URI)

SIGNED_PROPERTIES_TYPE_MARKER = "SignedProperties"

ANNEX_H_TL_TYPES = frozenset({"pub-eaa-provider"})
NO_HIP_TL_TYPES = frozenset({"pid-provider", "wallet-provider"})
NO_SERVICE_STATUS_TL_TYPES = frozenset({"pid-provider", "wallet-provider"})
NEXT_UPDATE_MAX_MONTHS_TL_TYPES = frozenset(
    {
        "pid-provider",
        "wallet-provider",
        "wrpac-provider",
        "wrprc-provider",
        "pub-eaa-provider",
        "ebwoid-provider",
    }
)

STATUS_DETN_URI = {
    "pid-provider": "http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU",
    "wallet-provider": "http://uri.etsi.org/19602/WalletProvidersList/StatusDetn/EU",
    "wrpac-provider": "http://uri.etsi.org/19602/WRPACProvidersList/StatusDetn/EU",
    "wrprc-provider": "http://uri.etsi.org/19602/WRPRCProvidersList/StatusDetn/EU",
    "pub-eaa-provider": "http://uri.etsi.org/19602/PubEAAProvidersList/StatusDetn/EU",
    "eaa-provider": "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate",
    "qeaa-provider": "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate",
    "ebwoid-provider": "http://uri.etsi.org/19602/RegistrarsAndRegistersList/StatusDetn/EU",
}

SCHEME_RULES_URI = {
    "pid-provider": "http://uri.etsi.org/19602/PIDProviders/schemerules/EU",
    "wallet-provider": "http://uri.etsi.org/19602/WalletProvidersList/schemerules/EU",
    "wrpac-provider": "http://uri.etsi.org/19602/WRPACProvidersList/schemerules/EU",
    "wrprc-provider": "http://uri.etsi.org/19602/WRPRCProvidersList/schemerules/EU",
    "pub-eaa-provider": "http://uri.etsi.org/19602/PubEAAProvidersList/schemerules/EU",
    "ebwoid-provider": "http://uri.etsi.org/19602/RegistrarsAndRegistersList/schemerules/EU",
}

# TS 119 612 lists are mixed national TSLs; require the distinguishing service
# type when entities are present, but do not forbid other 612 service types.
REQUIRED_612_SERVICE_TYPE = {
    "eaa-provider": SVC_TYPE_EAA,
    "qeaa-provider": SVC_TYPE_EAA_Q,
}

ALLOWED_SERVICE_TYPES = {
    "pid-provider": frozenset(
        {
            "http://uri.etsi.org/19602/SvcType/PID/Issuance",
            "http://uri.etsi.org/19602/SvcType/PID/Revocation",
        }
    ),
    "wallet-provider": frozenset(
        {
            "http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance",
            "http://uri.etsi.org/19602/SvcType/WalletSolution/Revocation",
        }
    ),
    "wrpac-provider": frozenset(
        {
            "http://uri.etsi.org/19602/SvcType/WRPAC/Issuance",
            "http://uri.etsi.org/19602/SvcType/WRPAC/Revocation",
        }
    ),
    "wrprc-provider": frozenset(
        {
            "http://uri.etsi.org/19602/SvcType/WRPRC/Issuance",
            "http://uri.etsi.org/19602/SvcType/WRPRC/Revocation",
        }
    ),
    "pub-eaa-provider": frozenset(
        {
            "http://uri.etsi.org/19602/SvcType/PubEAA/Issuance",
            "http://uri.etsi.org/19602/SvcType/PubEAA/Revocation",
        }
    ),
    "ebwoid-provider": frozenset({"http://uri.etsi.org/19602/SvcType/Register"}),
}

ANNEX_H_SERVICE_STATUS = frozenset(
    {
        "http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/notified",
        "http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/withdrawn",
    }
)

ALLOWED_JWS_ALGS = frozenset(
    {
        "ES256",
        "ES384",
        "ES512",
        "EdDSA",
        "RS256",
        "RS384",
        "RS512",
        "PS256",
        "PS384",
        "PS512",
    }
)

ENTITY_LOCAL_NAMES = frozenset({"TrustedEntity", "TrustServiceProvider"})


def _local_name(tag: str | None) -> str:
    if not tag:
        return ""
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def _add_months(dt: datetime, months: int) -> datetime:
    month_index = (dt.month - 1) + months
    year = dt.year + (month_index // 12)
    month = (month_index % 12) + 1
    day = min(dt.day, monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def _parse_utc(value: str) -> datetime | None:
    if not value or not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _first_text(root: etree._Element, local: str) -> str:
    for el in root.iter():
        if _local_name(el.tag) == local:
            text = (el.text or "").strip()
            if text:
                return text
            for child in el:
                if _local_name(child.tag) in {"dateTime", "DateTime"}:
                    child_text = (child.text or "").strip()
                    if child_text:
                        return child_text
    return ""


def _all_texts(root: etree._Element, local: str) -> list[str]:
    out: list[str] = []
    for el in root.iter():
        if _local_name(el.tag) == local:
            text = (el.text or "").strip()
            if text:
                out.append(text)
    return out


def _has_element(root: etree._Element, names: frozenset[str]) -> bool:
    for el in root.iter():
        if _local_name(el.tag) in names:
            return True
    return False


def _flag_etsi_registry_uri(value: str, field: str) -> list[str]:
    """ETSI registry URIs are published as http://uri.etsi.org/... with no trailing slash."""
    if not value or "uri.etsi.org" not in value:
        return []
    canonical = value.strip().replace("https://uri.etsi.org", "http://uri.etsi.org").rstrip(
        "/"
    )
    if value.strip() != canonical:
        return [
            f"{field} must use the canonical ETSI URI {canonical!r} "
            f"(http://uri.etsi.org, no trailing slash); got {value!r}"
        ]
    return []


def _check_next_update(issue: str, nxt: str, tl_type: str) -> list[str]:
    errors: list[str] = []
    if not issue:
        errors.append("ListIssueDateTime is required")
    if not nxt:
        errors.append("NextUpdate is required")
    issue_dt = _parse_utc(issue) if issue else None
    next_dt = _parse_utc(nxt) if nxt else None
    if issue and issue_dt is None:
        errors.append(f"ListIssueDateTime is not a valid UTC date-time: {issue!r}")
    if nxt and next_dt is None:
        errors.append(f"NextUpdate is not a valid UTC date-time: {nxt!r}")
    if (
        tl_type in NEXT_UPDATE_MAX_MONTHS_TL_TYPES
        and issue_dt is not None
        and next_dt is not None
        and next_dt > _add_months(issue_dt, 6)
    ):
        errors.append(
            "NextUpdate must be at most 6 months after ListIssueDateTime "
            f"(WP4 TS 119 602 profile); issue={issue} next={nxt}"
        )
    return errors


def _check_common_profile(
    *,
    tl_type: str,
    list_type_uri: str,
    status_detn: str,
    scheme_rules: list[str],
    service_types: list[str],
    service_statuses: list[str],
    historical_period: str,
    issue: str,
    nxt: str,
    has_entities: bool,
    root_local: str,
) -> list[str]:
    errors: list[str] = []
    expected_type = TL_TYPE_TO_REFERENCE_URI.get(tl_type)
    if not expected_type:
        errors.append(f"Unknown TL type {tl_type!r}")
        return errors

    if tl_type in TS_119_612_TL_TYPES and root_local and root_local != "TrustServiceStatusList":
        label = (
            "Non-qualified EAA Provider"
            if tl_type == "eaa-provider"
            else "QEAA Provider"
        )
        errors.append(
            f"{label} lists must be ETSI TS 119 612 XML Trusted Lists "
            f"(root TrustServiceStatusList); got {root_local!r}"
        )

    if not list_type_uri:
        errors.append(
            f"Missing list type URI; expected {expected_type!r} for {tl_type}"
        )
    elif list_type_uri != expected_type:
        errors.append(
            f"List type URI must be {expected_type!r} for {tl_type}; "
            f"got {list_type_uri!r}"
        )
    errors.extend(_flag_etsi_registry_uri(list_type_uri, "List type URI"))

    expected_detn = STATUS_DETN_URI.get(tl_type)
    if expected_detn:
        if not status_detn:
            errors.append(
                f"StatusDeterminationApproach must be {expected_detn!r} for {tl_type}"
            )
        elif status_detn != expected_detn:
            errors.append(
                f"StatusDeterminationApproach must be {expected_detn!r} for {tl_type}; "
                f"got {status_detn!r}"
            )
        errors.extend(
            _flag_etsi_registry_uri(status_detn, "StatusDeterminationApproach")
        )

    expected_rules = SCHEME_RULES_URI.get(tl_type)
    if expected_rules:
        if expected_rules not in scheme_rules:
            errors.append(
                f"SchemeTypeCommunityRules must include {expected_rules!r} for {tl_type}"
            )
        for uri in scheme_rules:
            errors.extend(_flag_etsi_registry_uri(uri, "SchemeTypeCommunityRules"))

    allowed_svc = ALLOWED_SERVICE_TYPES.get(tl_type)
    if allowed_svc:
        for svc in service_types:
            errors.extend(_flag_etsi_registry_uri(svc, "ServiceTypeIdentifier"))
            if svc not in allowed_svc:
                errors.append(
                    f"ServiceTypeIdentifier {svc!r} is not allowed for {tl_type}; "
                    f"allowed={sorted(allowed_svc)}"
                )
    elif tl_type in TS_119_612_TL_TYPES:
        for svc in service_types:
            errors.extend(_flag_etsi_registry_uri(svc, "ServiceTypeIdentifier"))
        required_svc = REQUIRED_612_SERVICE_TYPE.get(tl_type)
        if required_svc and has_entities and required_svc not in service_types:
            errors.append(
                f"{tl_type} TS 119 612 lists must include ServiceTypeIdentifier "
                f"{required_svc!r} when TrustServiceProviders are present "
                "(EAA vs QEAA vs Pub-EAA are distinguished by Svctype, not LoTEType)"
            )

    for st in service_statuses:
        errors.extend(_flag_etsi_registry_uri(st, "ServiceStatus"))

    if tl_type in NO_SERVICE_STATUS_TL_TYPES and service_statuses:
        errors.append(
            f"ServiceStatus must not be used on {tl_type} lists (TS 119 602 Annex D/E)"
        )

    if tl_type in ANNEX_H_TL_TYPES:
        if historical_period != "65535":
            errors.append(
                "HistoricalInformationPeriod shall be present with value 65535 "
                f"on Annex H (Pub-EAA) lists; got {historical_period!r}"
            )
        if has_entities and not service_statuses:
            errors.append(
                "ServiceStatus shall be present on Annex H trusted-entity services"
            )
        for st in service_statuses:
            if st not in ANNEX_H_SERVICE_STATUS:
                errors.append(
                    f"Annex H ServiceStatus must be one of {sorted(ANNEX_H_SERVICE_STATUS)}; "
                    f"got {st!r}"
                )

    if tl_type in NO_HIP_TL_TYPES and historical_period:
        errors.append(
            f"HistoricalInformationPeriod shall not be present on {tl_type} lists; "
            f"got {historical_period!r}"
        )

    if not has_entities:
        errors.append(
            "Published list has no TrustedEntity / TrustServiceProvider entries"
        )

    errors.extend(_check_next_update(issue, nxt, tl_type))
    return errors


def _document_references(sig: etree._Element) -> list[etree._Element]:
    refs: list[etree._Element] = []
    for el in sig.iter():
        if _local_name(el.tag) != "Reference":
            continue
        # Stay inside this Signature (iter() includes descendants only)
        parent_sig = el
        while parent_sig is not None and _local_name(parent_sig.tag) != "Signature":
            parent_sig = parent_sig.getparent()  # type: ignore[assignment]
        if parent_sig is not sig:
            continue
        typ = el.get("Type") or ""
        if SIGNED_PROPERTIES_TYPE_MARKER in typ:
            continue
        refs.append(el)
    return refs


def _transform_algorithms(ref: etree._Element) -> list[str]:
    algs: list[str] = []
    for el in ref.iter():
        if _local_name(el.tag) == "Transform":
            algs.append(el.get("Algorithm") or "")
    return algs


def _validate_xml_signatures(root: etree._Element) -> list[str]:
    errors: list[str] = []
    signatures = [el for el in root.iter() if _local_name(el.tag) == "Signature"]
    if not signatures:
        errors.append(
            "XML list is not signed; WP4/ETSI require an enveloped XAdES Baseline B "
            "signature"
        )
        return errors

    seen_forbidden: set[str] = set()
    for el in root.iter():
        if _local_name(el.tag) != "Transform":
            continue
        alg = el.get("Algorithm") or ""
        if alg in seen_forbidden:
            continue
        if alg == XPATH_FILTER2_URI:
            seen_forbidden.add(alg)
            errors.append(
                "XPath Filter 2.0 is not permitted "
                f"({XPATH_FILTER2_URI}). TS 119 612 Annex B.1 / TS 119 602 Annex H "
                "require ds:Transform Algorithm="
                f"{ENVELOPED_SIGNATURE_URI!r} then {EXCLUSIVE_C14N_URI!r}"
            )
        elif alg == XPATH_1999_URI:
            seen_forbidden.add(alg)
            errors.append(
                f"XPath transform {XPATH_1999_URI} is not permitted; "
                "use enveloped-signature then exclusive C14N"
            )
        elif alg in FORBIDDEN_TRANSFORM_URIS:
            seen_forbidden.add(alg)
            errors.append(
                f"Transform algorithm {alg!r} is not permitted by the WP4/ETSI "
                "enveloped XAdES profile"
            )

    for idx, sig in enumerate(signatures):
        c14n = ""
        for el in sig.iter():
            if _local_name(el.tag) == "CanonicalizationMethod":
                c14n = el.get("Algorithm") or ""
                break
        if c14n != EXCLUSIVE_C14N_URI:
            errors.append(
                f"Signature[{idx}] CanonicalizationMethod must be "
                f"{EXCLUSIVE_C14N_URI!r}; got {c14n!r}"
            )

        doc_refs = _document_references(sig)
        if not doc_refs:
            errors.append(
                f"Signature[{idx}] has no document ds:Reference "
                "(URI='' or same-document reference to the enveloping list)"
            )
            continue
        primary = next(
            (
                ref
                for ref in doc_refs
                if (ref.get("URI") or "") in {"", None}
                or str(ref.get("URI") or "").startswith("#")
            ),
            doc_refs[0],
        )
        algs = _transform_algorithms(primary)
        uri = primary.get("URI")
        if uri not in {"", None} and not (isinstance(uri, str) and uri.startswith("#")):
            errors.append(
                f"Signature[{idx}] document Reference URI must be empty or a "
                f"same-document fragment; got {uri!r}"
            )
        if tuple(algs) != MANDATED_DOCUMENT_TRANSFORMS:
            errors.append(
                f"Signature[{idx}] document Reference transforms must be "
                f"{list(MANDATED_DOCUMENT_TRANSFORMS)}; got {algs} "
                "(enveloped-signature then exclusive C14N; XPath Filter 2.0 "
                "is not an allowed substitute)"
            )
    return errors


def validate_xml_list(xml_bytes: bytes, *, tl_type: str) -> list[str]:
    """Validate a published XML TL/LoTE against the WP4/ETSI profile."""
    try:
        root = etree.fromstring(xml_bytes)
    except etree.XMLSyntaxError as exc:
        return [f"XML is not well-formed: {exc}"]

    errors = _validate_xml_signatures(root)
    root_local = _local_name(root.tag)
    lote_type = _first_text(root, "LoTEType")
    tsl_type = _first_text(root, "TSLType")
    list_type = tsl_type if tl_type in TS_119_612_TL_TYPES else (lote_type or tsl_type)
    errors.extend(
        _check_common_profile(
            tl_type=tl_type,
            list_type_uri=list_type,
            status_detn=_first_text(root, "StatusDeterminationApproach"),
            scheme_rules=_scheme_rule_uris_xml(root),
            service_types=_all_texts(root, "ServiceTypeIdentifier"),
            service_statuses=_all_texts(root, "ServiceStatus"),
            historical_period=_first_text(root, "HistoricalInformationPeriod"),
            issue=_first_text(root, "ListIssueDateTime"),
            nxt=_first_text(root, "NextUpdate"),
            has_entities=_has_element(root, ENTITY_LOCAL_NAMES),
            root_local=root_local,
        )
    )
    return errors


def _scheme_rule_uris_xml(root: etree._Element) -> list[str]:
    uris: list[str] = []
    for el in root.iter():
        if _local_name(el.tag) != "SchemeTypeCommunityRules":
            continue
        for child in el.iter():
            if _local_name(child.tag) in {"URI", "uriValue"}:
                text = (child.text or "").strip()
                if text:
                    uris.append(text)
            uri_attr = child.get("uriValue")
            if uri_attr:
                uris.append(uri_attr)
    return uris


def _walk_json(obj: Any, collector: dict[str, list[str]]) -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in collector and isinstance(value, str) and value:
                collector[key].append(value)
            elif key == "SchemeTypeCommunityRules" and isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and item.get("uriValue"):
                        collector["SchemeTypeCommunityRules"].append(str(item["uriValue"]))
                    elif isinstance(item, str):
                        collector["SchemeTypeCommunityRules"].append(item)
            else:
                _walk_json(value, collector)
    elif isinstance(obj, list):
        for item in obj:
            _walk_json(item, collector)


def _b64url_json(data: str) -> Any:
    padding = (4 - len(data) % 4) % 4
    raw = base64.urlsafe_b64decode(data + "=" * padding)
    return json.loads(raw.decode("utf-8"))


def _validate_json_signature(doc: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    sig = doc.get("signature")
    if not sig:
        errors.append(
            "JSON list is not signed; TS 119 602 requires a compact JAdES Baseline B "
            "signature"
        )
        return errors
    if isinstance(sig, str):
        parts = sig.split(".")
        if len(parts) != 3:
            errors.append("JSON signature string is not a compact JWS (header.payload.sig)")
            return errors
        try:
            header = _b64url_json(parts[0])
        except Exception as exc:
            errors.append(f"Cannot decode compact JAdES protected header: {exc}")
            return errors
    elif isinstance(sig, dict):
        protected = sig.get("protected")
        signature_b64 = sig.get("signature")
        if not isinstance(protected, str) or not signature_b64:
            errors.append(
                "JAdES signature must use RFC 7515 flattened JSON serialization "
                "with base64url 'protected' and 'signature' strings "
                "(WP4 / TS 119 182-1 Baseline B)"
            )
            return errors
        try:
            header = _b64url_json(protected)
        except Exception as exc:
            errors.append(f"Cannot decode JAdES protected header: {exc}")
            return errors
    else:
        errors.append("JSON signature must be a JAdES object or compact JWS string")
        return errors

    if not isinstance(header, dict):
        errors.append("JAdES protected header must be a JSON object")
        return errors
    alg = header.get("alg")
    if alg not in ALLOWED_JWS_ALGS:
        errors.append(
            f"JAdES protected header alg must be one of {sorted(ALLOWED_JWS_ALGS)}; "
            f"got {alg!r}"
        )
    x5c = header.get("x5c")
    if not isinstance(x5c, list) or not x5c:
        errors.append("JAdES protected header must include a non-empty x5c certificate chain")
    iat = header.get("iat")
    if not isinstance(iat, int) or iat <= 0:
        errors.append(
            "JAdES protected header must include iat as a positive Unix timestamp "
            "(TS 119 182-1 §5.1.11, mandatory from 2025-07-15)"
        )
    return errors


def validate_json_list(raw: bytes | str, *, tl_type: str) -> list[str]:
    """Validate a published JSON LoTE against the WP4/ETSI profile."""
    if tl_type in TS_119_612_TL_TYPES:
        label = (
            "Non-qualified EAA Provider"
            if tl_type == "eaa-provider"
            else "QEAA Provider"
        )
        return [
            f"{label} lists must be ETSI TS 119 612 XML Trusted Lists, "
            "not a TS 119 602 JSON LoTE"
        ]
    try:
        text = raw.decode("utf-8") if isinstance(raw, bytes) else raw
        doc = json.loads(text)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"JSON is not well-formed: {exc}"]
    if not isinstance(doc, dict):
        return ["JSON root must be an object"]

    errors = _validate_json_signature(doc)
    lote = doc.get("LoTE") if isinstance(doc.get("LoTE"), dict) else doc
    lasi = lote.get("ListAndSchemeInformation") if isinstance(lote, dict) else {}
    if not isinstance(lasi, dict):
        lasi = {}

    collected: dict[str, list[str]] = {
        "ServiceTypeIdentifier": [],
        "ServiceStatus": [],
        "SchemeTypeCommunityRules": [],
        "HistoricalInformationPeriod": [],
    }
    _walk_json(lote, collected)

    entities = lote.get("TrustedEntitiesList") if isinstance(lote, dict) else None
    has_entities = isinstance(entities, list) and len(entities) > 0

    hip = lasi.get("HistoricalInformationPeriod")
    hip_text = str(hip) if hip is not None else (
        collected["HistoricalInformationPeriod"][0]
        if collected["HistoricalInformationPeriod"]
        else ""
    )

    errors.extend(
        _check_common_profile(
            tl_type=tl_type,
            list_type_uri=str(lasi.get("LoTEType") or ""),
            status_detn=str(lasi.get("StatusDeterminationApproach") or ""),
            scheme_rules=collected["SchemeTypeCommunityRules"],
            service_types=collected["ServiceTypeIdentifier"],
            service_statuses=collected["ServiceStatus"],
            historical_period=str(hip_text) if hip_text else "",
            issue=str(lasi.get("ListIssueDateTime") or ""),
            nxt=str(lasi.get("NextUpdate") or ""),
            has_entities=bool(has_entities),
            root_local="LoTE",
        )
    )
    return errors


def detect_list_format(
    content: bytes,
    url: str = "",
    content_type: str = "",
) -> str:
    """Return ``xml``, ``json``, or ``unknown``."""
    ctype = (content_type or "").lower()
    lowered_url = url.lower()
    stripped = content.lstrip()
    if stripped.startswith(b"\xef\xbb\xbf"):
        stripped = stripped[3:].lstrip()
    if (
        stripped.startswith(b"<")
        or "xml" in ctype
        or lowered_url.endswith(".xml")
    ):
        return "xml"
    if (
        stripped.startswith(b"{")
        or stripped.startswith(b"[")
        or "json" in ctype
        or lowered_url.endswith(".json")
    ):
        return "json"
    return "unknown"


def validate_published_document(
    content: bytes,
    *,
    tl_type: str,
    url: str = "",
    content_type: str = "",
) -> list[str]:
    """Validate one published TL/LoTE body (XML or JSON)."""
    fmt = detect_list_format(content, url=url, content_type=content_type)
    if fmt == "xml":
        return validate_xml_list(content, tl_type=tl_type)
    if fmt == "json":
        return validate_json_list(content, tl_type=tl_type)
    return [
        "Could not determine published list format (expected XML Trusted List / "
        f"LoTE or JSON LoTE); content-type={content_type!r} url={url!r}"
    ]


def summarize_published_document(
    content: bytes,
    *,
    url: str = "",
    content_type: str = "",
) -> dict[str, str]:
    """Extract fields that make CI failure logs easier to debug."""
    fmt = detect_list_format(content, url=url, content_type=content_type)
    info: dict[str, str] = {"format": fmt}
    if fmt == "xml":
        try:
            root = etree.fromstring(content)
        except etree.XMLSyntaxError as exc:
            info["parse_error"] = str(exc)
            return info
        info["root"] = _local_name(root.tag)
        lote_type = _first_text(root, "LoTEType")
        tsl_type = _first_text(root, "TSLType")
        if lote_type:
            info["LoTEType"] = lote_type
        if tsl_type:
            info["TSLType"] = tsl_type
        detn = _first_text(root, "StatusDeterminationApproach")
        if detn:
            info["StatusDeterminationApproach"] = detn
        hip = _first_text(root, "HistoricalInformationPeriod")
        if hip:
            info["HistoricalInformationPeriod"] = hip
        issue = _first_text(root, "ListIssueDateTime")
        nxt = _first_text(root, "NextUpdate")
        if issue:
            info["ListIssueDateTime"] = issue
        if nxt:
            info["NextUpdate"] = nxt
        sigs = [el for el in root.iter() if _local_name(el.tag) == "Signature"]
        info["signatures"] = str(len(sigs))
        n_ent = sum(
            1 for el in root.iter() if _local_name(el.tag) in ENTITY_LOCAL_NAMES
        )
        info["entities"] = str(n_ent)
        transforms: list[str] = []
        c14n = ""
        if sigs:
            for el in sigs[0].iter():
                if _local_name(el.tag) == "CanonicalizationMethod" and not c14n:
                    c14n = el.get("Algorithm") or ""
                if _local_name(el.tag) == "Transform":
                    alg = el.get("Algorithm") or ""
                    if alg and alg not in transforms:
                        transforms.append(alg)
        if c14n:
            info["CanonicalizationMethod"] = c14n
        if transforms:
            info["transforms"] = " -> ".join(transforms)
        return info

    if fmt == "json":
        try:
            doc = json.loads(content.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            info["parse_error"] = str(exc)
            return info
        if not isinstance(doc, dict):
            info["root"] = type(doc).__name__
            return info
        info["top_keys"] = ",".join(sorted(doc.keys()))
        lote = doc.get("LoTE") if isinstance(doc.get("LoTE"), dict) else doc
        lasi = lote.get("ListAndSchemeInformation") if isinstance(lote, dict) else {}
        if isinstance(lasi, dict):
            for key in (
                "LoTEType",
                "StatusDeterminationApproach",
                "HistoricalInformationPeriod",
                "ListIssueDateTime",
                "NextUpdate",
            ):
                if lasi.get(key) is not None and lasi.get(key) != "":
                    info[key] = str(lasi[key])
        entities = lote.get("TrustedEntitiesList") if isinstance(lote, dict) else None
        info["entities"] = str(len(entities) if isinstance(entities, list) else 0)
        sig = doc.get("signature")
        if not sig:
            info["signature"] = "missing"
            return info
        if isinstance(sig, str):
            info["signature"] = "compact-jws"
            parts = sig.split(".")
            if parts:
                try:
                    header = _b64url_json(parts[0])
                    if isinstance(header, dict):
                        info["jws_alg"] = str(header.get("alg") or "")
                        info["jws_x5c"] = "yes" if header.get("x5c") else "no"
                        info["jws_iat"] = "yes" if header.get("iat") else "no"
                except Exception:
                    info["jws_header"] = "undecodable"
            return info
        if isinstance(sig, dict):
            info["signature"] = "jades-flattened"
            protected = sig.get("protected")
            if isinstance(protected, str):
                try:
                    header = _b64url_json(protected)
                    if isinstance(header, dict):
                        info["jws_alg"] = str(header.get("alg") or "")
                        info["jws_x5c"] = "yes" if header.get("x5c") else "no"
                        info["jws_iat"] = "yes" if header.get("iat") else "no"
                except Exception:
                    info["jws_header"] = "undecodable"
            else:
                info["jws_protected"] = type(protected).__name__
        return info

    info["note"] = "unrecognised body (not XML or JSON)"
    return info
