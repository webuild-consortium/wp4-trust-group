"""Tests for WP4/ETSI published TL/LoTE profile checks."""

from __future__ import annotations

import base64
import json
from pathlib import Path

from tools.lotl.jades_signer import sign_json
from tools.lotl.list_profile import (
    ENVELOPED_SIGNATURE_URI,
    EXCLUSIVE_C14N_URI,
    XPATH_FILTER2_URI,
    detect_list_format,
    summarize_published_document,
    validate_json_list,
    validate_published_document,
    validate_xml_list,
)

ENV = ENVELOPED_SIGNATURE_URI
C14N = EXCLUSIVE_C14N_URI
XPATH2 = XPATH_FILTER2_URI

PID_TYPE = "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList"
PID_DETN = "http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU"
PID_RULES = "http://uri.etsi.org/19602/PIDProviders/schemerules/EU"
PID_SVC = "http://uri.etsi.org/19602/SvcType/PID/Issuance"

PUB_TYPE = "http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList"
PUB_DETN = "http://uri.etsi.org/19602/PubEAAProvidersList/StatusDetn/EU"
PUB_RULES = "http://uri.etsi.org/19602/PubEAAProvidersList/schemerules/EU"
PUB_SVC = "http://uri.etsi.org/19602/SvcType/PubEAA/Issuance"
PUB_STATUS = "http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/notified"


def _xml(
    *,
    transforms: list[str] | None = None,
    lote_type: str = PID_TYPE,
    detn: str = PID_DETN,
    rules: str = PID_RULES,
    svc: str = PID_SVC,
    status: str | None = None,
    hip: str | None = None,
    issue: str = "2026-01-01T00:00:00Z",
    nxt: str = "2026-07-01T00:00:00Z",
    entity: bool = True,
    signed: bool = True,
    root: str = "TrustedEntitiesList",
    tsl_type: str | None = None,
    extra_transform_xml: str = "",
    ref_uri: str = "",
    c14n: str = C14N,
) -> bytes:
    tfs = transforms if transforms is not None else [ENV, C14N]
    tf_xml = extra_transform_xml + "".join(
        f'<ds:Transform Algorithm="{alg}"/>' for alg in tfs
    )
    hip_xml = (
        f"<HistoricalInformationPeriod>{hip}</HistoricalInformationPeriod>"
        if hip is not None
        else ""
    )
    status_xml = f"<ServiceStatus>{status}</ServiceStatus>" if status else ""
    tsl_xml = f"<TSLType>{tsl_type}</TSLType>" if tsl_type else ""
    entity_xml = ""
    if entity:
        entity_xml = f"""
        <TrustedEntitiesList>
          <TrustedEntity>
            <TrustedEntityServices>
              <TrustedEntityService>
                <ServiceInformation>
                  <ServiceTypeIdentifier>{svc}</ServiceTypeIdentifier>
                  {status_xml}
                </ServiceInformation>
              </TrustedEntityService>
            </TrustedEntityServices>
          </TrustedEntity>
        </TrustedEntitiesList>"""
    sig_xml = ""
    if signed:
        sig_xml = f"""
  <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:SignedInfo>
      <ds:CanonicalizationMethod Algorithm="{c14n}"/>
      <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256"/>
      <ds:Reference URI="{ref_uri}">
        <ds:Transforms>{tf_xml}</ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue>abc</ds:DigestValue>
      </ds:Reference>
      <ds:Reference Type="http://uri.etsi.org/01903#SignedProperties" URI="#sp">
        <ds:Transforms>
          <ds:Transform Algorithm="{C14N}"/>
        </ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue>def</ds:DigestValue>
      </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>abc</ds:SignatureValue>
  </ds:Signature>"""
    lote_xml = f"<LoTEType>{lote_type}</LoTEType>" if lote_type else ""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<{root} xmlns="http://uri.etsi.org/019602/v1#" Id="root-1">
  <ListAndSchemeInformation>
    {lote_xml}{tsl_xml}
    <StatusDeterminationApproach>{detn}</StatusDeterminationApproach>
    <SchemeTypeCommunityRules>
      <URI>{rules}</URI>
    </SchemeTypeCommunityRules>
    {hip_xml}
    <ListIssueDateTime>{issue}</ListIssueDateTime>
    <NextUpdate><dateTime>{nxt}</dateTime></NextUpdate>
  </ListAndSchemeInformation>
  {entity_xml}
  {sig_xml}
</{root}>
""".encode()


def test_pid_xml_profile_passes() -> None:
    errors = validate_xml_list(_xml(), tl_type="pid-provider")
    assert errors == []


def test_xpath_filter2_is_rejected() -> None:
    errors = validate_xml_list(
        _xml(transforms=[XPATH2, C14N]),
        tl_type="pid-provider",
    )
    assert any("XPath Filter 2.0" in e for e in errors)
    assert any("enveloped-signature then exclusive C14N" in e for e in errors)


def test_xpath_1999_is_rejected() -> None:
    xpath1999 = "http://www.w3.org/TR/1999/REC-xpath-19991116"
    errors = validate_xml_list(
        _xml(transforms=[xpath1999, C14N]),
        tl_type="pid-provider",
    )
    assert any("XPath transform" in e for e in errors)


def test_unsigned_xml_is_rejected() -> None:
    errors = validate_xml_list(_xml(signed=False), tl_type="pid-provider")
    assert any("not signed" in e for e in errors)


def test_empty_entity_list_is_rejected() -> None:
    errors = validate_xml_list(_xml(entity=False), tl_type="pid-provider")
    assert any("no TrustedEntity" in e for e in errors)


def test_wrong_list_type_is_rejected() -> None:
    errors = validate_xml_list(
        _xml(lote_type=PUB_TYPE),
        tl_type="pid-provider",
    )
    assert any("List type URI must be" in e for e in errors)


def test_https_etsi_uri_is_rejected() -> None:
    errors = validate_xml_list(
        _xml(lote_type="https://uri.etsi.org/19602/LoTEType/EUPIDProvidersList"),
        tl_type="pid-provider",
    )
    assert any("canonical ETSI URI" in e for e in errors)


def test_next_update_beyond_six_months_is_rejected() -> None:
    errors = validate_xml_list(
        _xml(issue="2026-01-01T00:00:00Z", nxt="2026-08-01T00:00:00Z"),
        tl_type="pid-provider",
    )
    assert any("at most 6 months" in e for e in errors)


def test_pid_must_not_have_service_status_or_hip() -> None:
    errors = validate_xml_list(
        _xml(status=PUB_STATUS, hip="65535"),
        tl_type="pid-provider",
    )
    assert any("ServiceStatus must not be used" in e for e in errors)
    assert any("HistoricalInformationPeriod shall not be present" in e for e in errors)


def test_annex_h_requires_hip_and_status() -> None:
    errors = validate_xml_list(
        _xml(
            lote_type=PUB_TYPE,
            detn=PUB_DETN,
            rules=PUB_RULES,
            svc=PUB_SVC,
            status=None,
            hip=None,
        ),
        tl_type="eaa-provider",
    )
    assert any("HistoricalInformationPeriod" in e for e in errors)
    assert any("ServiceStatus shall be present" in e for e in errors)


def test_annex_h_xml_profile_passes() -> None:
    errors = validate_xml_list(
        _xml(
            lote_type=PUB_TYPE,
            detn=PUB_DETN,
            rules=PUB_RULES,
            svc=PUB_SVC,
            status=PUB_STATUS,
            hip="65535",
        ),
        tl_type="eaa-provider",
    )
    assert errors == []


def test_malformed_xml() -> None:
    errors = validate_xml_list(b"<not-closed>", tl_type="pid-provider")
    assert any("not well-formed" in e for e in errors)


def test_document_reference_external_uri_rejected() -> None:
    errors = validate_xml_list(
        _xml(ref_uri="https://example.com/tl.xml"),
        tl_type="pid-provider",
    )
    assert any("same-document" in e for e in errors)


def test_wrong_c14n_method() -> None:
    errors = validate_xml_list(
        _xml(c14n="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"),
        tl_type="pid-provider",
    )
    assert any("CanonicalizationMethod" in e for e in errors)


def test_inclusive_c14n_transform_forbidden() -> None:
    errors = validate_xml_list(
        _xml(transforms=[ENV, "http://www.w3.org/TR/2001/REC-xml-c14n-20010315"]),
        tl_type="pid-provider",
    )
    assert any("not permitted" in e for e in errors)


def test_fragment_root_id_is_allowed() -> None:
    errors = validate_xml_list(_xml(ref_uri="#root-1"), tl_type="pid-provider")
    assert errors == []


def test_qeaa_must_be_tsl_root() -> None:
    errors = validate_xml_list(
        _xml(
            lote_type="",
            tsl_type="http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric",
            detn="http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate",
            rules="http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon",
            svc="http://uri.etsi.org/TrstSvc/Svctype/EAA/Q",
            root="TrustedEntitiesList",
        ),
        tl_type="qeaa-provider",
    )
    assert any("TrustServiceStatusList" in e for e in errors)


def test_unknown_tl_type() -> None:
    errors = validate_xml_list(_xml(), tl_type="not-a-type")
    assert any("Unknown TL type" in e for e in errors)


def test_disallowed_service_type() -> None:
    errors = validate_xml_list(
        _xml(svc="http://uri.etsi.org/19602/SvcType/WRPAC/Issuance"),
        tl_type="pid-provider",
    )
    assert any("not allowed" in e for e in errors)


def test_missing_scheme_rules() -> None:
    errors = validate_xml_list(_xml(rules="http://example.com/rules"), tl_type="pid-provider")
    assert any("SchemeTypeCommunityRules must include" in e for e in errors)


def test_missing_status_detn() -> None:
    errors = validate_xml_list(_xml(detn=""), tl_type="pid-provider")
    assert any("StatusDeterminationApproach must be" in e for e in errors)


def test_bad_datetimes() -> None:
    errors = validate_xml_list(
        _xml(issue="not-a-date", nxt="also-bad"),
        tl_type="pid-provider",
    )
    assert any("ListIssueDateTime is not a valid" in e for e in errors)
    assert any("NextUpdate is not a valid" in e for e in errors)


def test_detect_format() -> None:
    assert detect_list_format(b"  <xml/>", url="https://x/t") == "xml"
    assert detect_list_format(b'{"a":1}', url="https://x/t") == "json"
    assert detect_list_format(b"\xef\xbb\xbf<root/>") == "xml"
    assert detect_list_format(b"hello", url="https://x/t.json", content_type="text") == "json"
    assert detect_list_format(b"hello", url="https://x/t.xml") == "xml"
    assert detect_list_format(b"hello") == "unknown"


def test_validate_published_document_unknown() -> None:
    errors = validate_published_document(b"nope", tl_type="pid-provider")
    assert any("Could not determine" in e for e in errors)


def test_validate_published_document_routes_xml_and_json() -> None:
    xml_errs = validate_published_document(_xml(), tl_type="pid-provider", url="https://x/tl.xml")
    assert xml_errs == []
    json_errs = validate_published_document(
        b"not-json",
        tl_type="pid-provider",
        url="https://x/tl.json",
        content_type="application/json",
    )
    assert any("not well-formed" in e for e in json_errs)


def _lote_json(
    *,
    lote_type: str = PID_TYPE,
    detn: str = PID_DETN,
    rules: str = PID_RULES,
    svc: str = PID_SVC,
    status: str | None = None,
    hip: int | None = None,
    issue: str = "2026-01-01T00:00:00Z",
    nxt: str = "2026-07-01T00:00:00Z",
    entities: bool = True,
) -> dict:
    svc_info: dict = {"ServiceTypeIdentifier": svc}
    if status:
        svc_info["ServiceStatus"] = status
    lasi: dict = {
        "LoTEType": lote_type,
        "StatusDeterminationApproach": detn,
        "SchemeTypeCommunityRules": [{"lang": "en", "uriValue": rules}],
        "ListIssueDateTime": issue,
        "NextUpdate": nxt,
    }
    if hip is not None:
        lasi["HistoricalInformationPeriod"] = hip
    lote: dict = {"ListAndSchemeInformation": lasi}
    if entities:
        lote["TrustedEntitiesList"] = [
            {
                "TrustedEntityServices": [
                    {"ServiceInformation": svc_info},
                ]
            }
        ]
    else:
        lote["TrustedEntitiesList"] = []
    return {"LoTE": lote}


def test_json_pid_with_jades_passes(signing_key_and_cert: tuple[Path, Path]) -> None:
    key_path, cert_path = signing_key_and_cert
    signed = sign_json(_lote_json(), key_path, cert_path)
    errors = validate_json_list(json.dumps(signed), tl_type="pid-provider")
    assert errors == []


def test_json_unsigned_rejected() -> None:
    errors = validate_json_list(json.dumps(_lote_json()), tl_type="pid-provider")
    assert any("not signed" in e for e in errors)


def test_json_qeaa_rejected() -> None:
    errors = validate_json_list(b"{}", tl_type="qeaa-provider")
    assert any("612 XML" in e for e in errors)


def test_json_malformed() -> None:
    errors = validate_json_list(b"{", tl_type="pid-provider")
    assert any("not well-formed" in e for e in errors)


def test_json_root_not_object() -> None:
    errors = validate_json_list(b"[1]", tl_type="pid-provider")
    assert any("root must be an object" in e for e in errors)


def test_json_protected_must_be_b64_string() -> None:
    doc = _lote_json()
    doc["signature"] = {"protected": {"alg": "ES256"}, "signature": "x"}
    errors = validate_json_list(json.dumps(doc), tl_type="pid-provider")
    assert any("flattened JSON serialization" in e for e in errors)


def test_json_compact_jws_header_ok() -> None:
    header = base64.urlsafe_b64encode(
        json.dumps({"alg": "ES256", "x5c": ["MII"], "iat": 1}).encode()
    ).decode().rstrip("=")
    doc = _lote_json()
    doc["signature"] = f"{header}.e30.sig"
    errors = validate_json_list(json.dumps(doc), tl_type="pid-provider")
    assert not any("protected header" in e or "not signed" in e for e in errors)


def test_json_compact_jws_not_three_parts() -> None:
    doc = _lote_json()
    doc["signature"] = "not-a-jws"
    errors = validate_json_list(json.dumps(doc), tl_type="pid-provider")
    assert any("compact JWS" in e for e in errors)


def test_json_bad_alg_and_missing_x5c_iat() -> None:
    header = base64.urlsafe_b64encode(json.dumps({"alg": "none"}).encode()).decode().rstrip("=")
    doc = _lote_json()
    doc["signature"] = {"protected": header, "signature": "sig"}
    errors = validate_json_list(json.dumps(doc), tl_type="pid-provider")
    assert any("alg must be one of" in e for e in errors)
    assert any("x5c" in e for e in errors)
    assert any("iat" in e for e in errors)


def test_json_annex_h_missing_hip() -> None:
    header = base64.urlsafe_b64encode(
        json.dumps({"alg": "ES256", "x5c": ["MII"], "iat": 1}).encode()
    ).decode().rstrip("=")
    doc = _lote_json(
        lote_type=PUB_TYPE,
        detn=PUB_DETN,
        rules=PUB_RULES,
        svc=PUB_SVC,
        status=PUB_STATUS,
        hip=None,
    )
    doc["signature"] = {"protected": header, "signature": "sig"}
    errors = validate_json_list(json.dumps(doc), tl_type="eaa-provider")
    assert any("HistoricalInformationPeriod" in e for e in errors)


def test_json_annex_h_passes_with_hip() -> None:
    header = base64.urlsafe_b64encode(
        json.dumps({"alg": "ES256", "x5c": ["MII"], "iat": 1}).encode()
    ).decode().rstrip("=")
    doc = _lote_json(
        lote_type=PUB_TYPE,
        detn=PUB_DETN,
        rules=PUB_RULES,
        svc=PUB_SVC,
        status=PUB_STATUS,
        hip=65535,
    )
    doc["signature"] = {"protected": header, "signature": "sig"}
    errors = validate_json_list(json.dumps(doc), tl_type="eaa-provider")
    assert errors == []


def test_json_invalid_signature_type() -> None:
    doc = _lote_json()
    doc["signature"] = 123
    errors = validate_json_list(json.dumps(doc), tl_type="pid-provider")
    assert any("JAdES object or compact JWS" in e for e in errors)


def test_json_bad_protected_b64() -> None:
    doc = _lote_json()
    doc["signature"] = {"protected": "!!!", "signature": "sig"}
    errors = validate_json_list(json.dumps(doc), tl_type="pid-provider")
    assert any("Cannot decode JAdES protected header" in e for e in errors)


def test_json_protected_not_object() -> None:
    header = base64.urlsafe_b64encode(b'"string"').decode().rstrip("=")
    doc = _lote_json()
    doc["signature"] = {"protected": header, "signature": "sig"}
    errors = validate_json_list(json.dumps(doc), tl_type="pid-provider")
    assert any("must be a JSON object" in e for e in errors)


def test_signature_without_document_reference() -> None:
    xml = b"""<?xml version="1.0"?>
    <TrustedEntitiesList xmlns="http://uri.etsi.org/019602/v1#">
      <ListAndSchemeInformation>
        <LoTEType>http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList</LoTEType>
        <StatusDeterminationApproach>http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU</StatusDeterminationApproach>
        <SchemeTypeCommunityRules><URI>http://uri.etsi.org/19602/PIDProviders/schemerules/EU</URI></SchemeTypeCommunityRules>
        <ListIssueDateTime>2026-01-01T00:00:00Z</ListIssueDateTime>
        <NextUpdate><dateTime>2026-07-01T00:00:00Z</dateTime></NextUpdate>
      </ListAndSchemeInformation>
      <TrustedEntitiesList>
        <TrustedEntity>
          <TrustedEntityServices>
            <TrustedEntityService>
              <ServiceInformation>
                <ServiceTypeIdentifier>http://uri.etsi.org/19602/SvcType/PID/Issuance</ServiceTypeIdentifier>
              </ServiceInformation>
            </TrustedEntityService>
          </TrustedEntityServices>
        </TrustedEntity>
      </TrustedEntitiesList>
      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
          <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
          <ds:Reference Type="http://uri.etsi.org/01903#SignedProperties" URI="#sp">
            <ds:Transforms>
              <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <ds:DigestValue>x</ds:DigestValue>
          </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue>x</ds:SignatureValue>
      </ds:Signature>
    </TrustedEntitiesList>
    """
    errors = validate_xml_list(xml, tl_type="pid-provider")
    assert any("no document ds:Reference" in e for e in errors)


def test_annex_h_bad_service_status() -> None:
    errors = validate_xml_list(
        _xml(
            lote_type=PUB_TYPE,
            detn=PUB_DETN,
            rules=PUB_RULES,
            svc=PUB_SVC,
            status="http://example.com/status",
            hip="65535",
        ),
        tl_type="pub-eaa-provider",
    )
    assert any("Annex H ServiceStatus" in e for e in errors)


def test_missing_list_type_uri() -> None:
    errors = validate_xml_list(_xml(lote_type=""), tl_type="pid-provider")
    assert any("Missing list type URI" in e for e in errors)


def test_wrong_status_detn_value() -> None:
    errors = validate_xml_list(
        _xml(detn="http://uri.etsi.org/19602/WalletProvidersList/StatusDetn/EU"),
        tl_type="pid-provider",
    )
    assert any("StatusDeterminationApproach must be" in e and "got" in e for e in errors)


def test_summarize_xml_exposes_transforms() -> None:
    info = summarize_published_document(_xml(transforms=[XPATH2, C14N]))
    assert info["format"] == "xml"
    assert info["root"] == "TrustedEntitiesList"
    assert XPATH2 in info["transforms"]
    assert info["signatures"] == "1"
    assert info["entities"] == "1"


def test_summarize_json_exposes_jades_header() -> None:
    import base64
    import json as json_lib

    header = base64.urlsafe_b64encode(
        json_lib.dumps({"alg": "ES256", "x5c": ["MII"], "iat": 1}).encode()
    ).decode().rstrip("=")
    doc = _lote_json(hip=65535)
    doc["signature"] = {"protected": header, "signature": "sig"}
    info = summarize_published_document(json_lib.dumps(doc).encode(), url="https://x/t.json")
    assert info["format"] == "json"
    assert info["jws_alg"] == "ES256"
    assert info["jws_x5c"] == "yes"
    assert info["signature"] == "jades-flattened"


def test_summarize_unknown_format() -> None:
    info = summarize_published_document(b"hello")
    assert info["format"] == "unknown"


def test_summarize_malformed_bodies() -> None:
    xml_info = summarize_published_document(b"<not-closed>", url="https://x/t.xml")
    assert "parse_error" in xml_info
    json_info = summarize_published_document(b"{", url="https://x/t.json")
    assert "parse_error" in json_info
    unsigned = summarize_published_document(
        b'{"LoTE":{"ListAndSchemeInformation":{}}}', url="https://x/t.json"
    )
    assert unsigned["signature"] == "missing"
