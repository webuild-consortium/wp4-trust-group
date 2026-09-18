"""Tests for published TL/LoTE fetch-and-profile validation."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from tools.lotl.jades_signer import sign_json
from tools.lotl.list_profile import ENVELOPED_SIGNATURE_URI, EXCLUSIVE_C14N_URI
from tools.lotl.published_validate import (
    PublicationCheck,
    fetch_published,
    finding_hint,
    finding_title,
    format_published_report,
    published_urls,
    run_published_validation,
    validate_entry_publications,
    validate_published_lists,
)
from tools.lotl.tl_entry import TLEntry

ENV = ENVELOPED_SIGNATURE_URI
C14N = EXCLUSIVE_C14N_URI

PID_XML = f"""<?xml version="1.0" encoding="UTF-8"?>
<TrustedEntitiesList xmlns="http://uri.etsi.org/019602/v1#" Id="root-1">
  <ListAndSchemeInformation>
    <LoTEType>http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList</LoTEType>
    <StatusDeterminationApproach>http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU</StatusDeterminationApproach>
    <SchemeTypeCommunityRules>
      <URI>http://uri.etsi.org/19602/PIDProviders/schemerules/EU</URI>
    </SchemeTypeCommunityRules>
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
      <ds:CanonicalizationMethod Algorithm="{C14N}"/>
      <ds:Reference URI="">
        <ds:Transforms>
          <ds:Transform Algorithm="{ENV}"/>
          <ds:Transform Algorithm="{C14N}"/>
        </ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue>abc</ds:DigestValue>
      </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>abc</ds:SignatureValue>
  </ds:Signature>
</TrustedEntitiesList>
""".encode()


def test_published_urls_unique(sample_tl_entry: TLEntry) -> None:
    sample_tl_entry.tl_url = "https://example.com/a.json"
    sample_tl_entry.tl_url_json = "https://example.com/a.json"
    sample_tl_entry.tl_url_xml = "https://example.com/a.xml"
    assert published_urls(sample_tl_entry) == [
        "https://example.com/a.json",
        "https://example.com/a.xml",
    ]


def test_published_urls_empty() -> None:
    entry = TLEntry(tl_type="pid-provider", participant_id="x", tl_url="")
    assert published_urls(entry) == []


@patch("tools.lotl.published_validate.fetch_tl")
def test_fetch_published_retries_then_succeeds(mock_fetch) -> None:
    mock_fetch.side_effect = [
        (None, None, None),
        ("{}", b'{"x":1}', "application/json"),
    ]
    with patch("tools.lotl.published_validate.time.sleep"):
        body, ctype, err = fetch_published("https://example.com/t.json", attempts=3)
    assert err is None
    assert body == b'{"x":1}'
    assert "json" in ctype
    assert mock_fetch.call_count == 2


@patch("tools.lotl.published_validate.fetch_tl")
def test_fetch_published_all_attempts_fail(mock_fetch) -> None:
    mock_fetch.return_value = (None, None, None)
    with patch("tools.lotl.published_validate.time.sleep"):
        body, _ctype, err = fetch_published("https://example.com/t.json", attempts=2)
    assert body is None
    assert err is not None
    assert "attempt 2/2" in err


@patch("tools.lotl.published_validate.fetch_published")
def test_validate_entry_publications_fetch_error(
    mock_fetch, sample_tl_entry: TLEntry
) -> None:
    mock_fetch.return_value = (None, "", "Failed to fetch")
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=False)
    assert errors
    assert any("Failed to fetch" in e for e in errors)


def test_validate_entry_no_urls() -> None:
    entry = TLEntry(tl_type="pid-provider", participant_id="x", tl_url="")
    errors = validate_entry_publications(entry)
    assert any("no publication URL" in e for e in errors)


@patch("tools.lotl.published_validate.fetch_published")
def test_validate_entry_xpath_filter2_is_reported(
    mock_fetch, sample_tl_entry: TLEntry
) -> None:
    xml = PID_XML.replace(
        ENVELOPED_SIGNATURE_URI.encode(),
        b"http://www.w3.org/2002/06/xmldsig-filter2",
    )
    mock_fetch.return_value = (xml, "application/xml", None)
    sample_tl_entry.tl_url_json = None
    sample_tl_entry.tl_url = "https://example.com/tl.xml"
    sample_tl_entry.tl_url_xml = "https://example.com/tl.xml"
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=False)
    assert any("XPath Filter 2.0" in e for e in errors)


@patch("tools.lotl.published_validate.fetch_published")
@patch("tools.lotl.published_validate.validate_tl_signature_xml")
def test_xades_signed_properties_ref_is_not_crypto_failure(
    mock_crypto, mock_fetch, sample_tl_entry: TLEntry
) -> None:
    mock_fetch.return_value = (PID_XML, "application/xml", None)
    mock_crypto.return_value = (False, "Expected to find 1 references, but found 2")
    sample_tl_entry.tl_url = "https://example.com/tl.xml"
    sample_tl_entry.tl_url_json = None
    sample_tl_entry.tl_url_xml = "https://example.com/tl.xml"
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=True)
    assert not any("signature verification failed" in e for e in errors)


@patch("tools.lotl.published_validate.fetch_published")
@patch("tools.lotl.published_validate.validate_tl_signature_xml")
def test_validate_entry_profile_pass_crypto_fail(
    mock_crypto, mock_fetch, sample_tl_entry: TLEntry
) -> None:
    mock_fetch.return_value = (PID_XML, "application/xml", None)
    mock_crypto.return_value = (False, "bad sig")
    sample_tl_entry.tl_url = "https://example.com/tl.xml"
    sample_tl_entry.tl_url_json = None
    sample_tl_entry.tl_url_xml = "https://example.com/tl.xml"
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=True)
    assert any("XML signature verification failed" in e for e in errors)


@patch("tools.lotl.published_validate.fetch_published")
def test_validate_entry_skips_crypto_when_unsigned(
    mock_fetch, sample_tl_entry: TLEntry
) -> None:
    unsigned = PID_XML.split(b"<ds:Signature")[0] + b"</TrustedEntitiesList>"
    mock_fetch.return_value = (unsigned, "application/xml", None)
    sample_tl_entry.tl_url = "https://example.com/tl.xml"
    sample_tl_entry.tl_url_json = None
    sample_tl_entry.tl_url_xml = "https://example.com/tl.xml"
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=True)
    assert any("not signed" in e for e in errors)
    assert not any("verification failed" in e for e in errors)


def test_validate_published_lists_bad_dir() -> None:
    ok, errors = validate_published_lists("/nonexistent/tl-entries")
    assert not ok
    assert errors


def test_validate_published_lists_no_entries(tmp_path: Path) -> None:
    (tmp_path / "pid-provider").mkdir()
    ok, errors = validate_published_lists(tmp_path)
    assert not ok
    assert any("No TL entries" in e for e in errors)


@patch("tools.lotl.published_validate.check_entry_publications")
def test_validate_published_lists_aggregates(
    mock_entry, tl_entries_dir: Path
) -> None:
    mock_entry.return_value = [
        PublicationCheck(
            label="pid-provider/example-tlp",
            url="https://example.com/tl.xml",
            errors=["XPath Filter 2.0"],
        )
    ]
    ok, errors = validate_published_lists(tl_entries_dir)
    assert not ok
    assert any("XPath Filter 2.0" in e for e in errors)


def test_run_published_validation_exit_codes(
    tl_entries_dir: Path,
) -> None:
    from io import StringIO

    buf = StringIO()
    with patch(
        "tools.lotl.published_validate.check_published_lists",
        return_value=([], []),
    ):
        assert run_published_validation(tl_entries_dir, stream=buf) == 0
        assert "RESULT: PASSED" in buf.getvalue()

    buf = StringIO()
    fail = PublicationCheck(
        label="pid-provider/example-tlp",
        url="https://example.com/tl.xml",
        errors=["XPath Filter 2.0 is not permitted"],
        observed={"transforms": "xpath-filter2"},
        content_type="application/xml",
        size_bytes=12,
    )
    with patch(
        "tools.lotl.published_validate.check_published_lists",
        return_value=([], [fail]),
    ):
        assert run_published_validation(tl_entries_dir, stream=buf) == 1
        text = buf.getvalue()
        assert "RESULT: FAILED" in text
        assert "pid-provider/example-tlp" in text
        assert "Fix:" in text


def test_format_published_report_groups_and_hints() -> None:
    fail = PublicationCheck(
        label="wrprc-provider/idunion",
        url="https://example.com/tl.xml",
        errors=[
            "XPath Filter 2.0 is not permitted (http://www.w3.org/2002/06/xmldsig-filter2)"
        ],
        content_type="application/xml; charset=UTF-8",
        size_bytes=9615,
        observed={
            "format": "xml",
            "root": "TrustedEntitiesList",
            "transforms": "http://www.w3.org/2002/06/xmldsig-filter2 -> "
            "http://www.w3.org/2001/10/xml-exc-c14n#",
        },
    )
    passed = PublicationCheck(
        label="wrpac-provider/raidiam",
        url="https://example.com/lote.json",
        errors=[],
        observed={"format": "json", "LoTEType": "EUWRPACProvidersList"},
    )
    text = format_published_report([], [fail, passed], github=False)
    assert "FAIL  wrprc-provider/idunion" in text
    assert "PASS  wrpac-provider/raidiam" in text
    assert "Observed" in text
    assert "transforms" in text
    assert "enveloped-signature then exclusive C14N" in text
    assert "Passed (checked, no findings)" in text
    gh = format_published_report([], [fail], github=True)
    assert "::group::FAIL wrprc-provider/idunion" in gh
    assert "::error title=" in gh
    assert "::endgroup::" in gh


def test_format_report_local_errors() -> None:
    text = format_published_report(["lotl/tl_entries/x: Invalid JSON"], [])
    assert "FAIL  (local tl_entries files)" in text
    assert "Invalid JSON" in text
    assert "RESULT: FAILED" in text


def test_finding_title_and_hint() -> None:
    assert "XPath Filter 2.0" in finding_title("XPath Filter 2.0 is not permitted")
    assert "enveloped-signature" in finding_hint("XPath Filter 2.0 is not permitted")
    assert finding_title("something unexpected") == "Profile violation"
    assert "implementation profile" in finding_hint("something unexpected")


def test_run_published_validation_github_annotations(
    tl_entries_dir: Path, monkeypatch
) -> None:
    from io import StringIO

    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    buf = StringIO()
    fail = PublicationCheck(
        label="pid-provider/x",
        url="https://example.com/tl.xml",
        errors=["XPath Filter 2.0 is not permitted"],
    )
    with patch(
        "tools.lotl.published_validate.check_published_lists",
        return_value=([], [fail]),
    ):
        assert run_published_validation(tl_entries_dir, stream=buf) == 1
    text = buf.getvalue()
    assert "::error title=" in text
    assert "::group::" in text


@patch("tools.lotl.published_validate.fetch_published")
def test_json_crypto_verify_path(
    mock_fetch, sample_tl_entry: TLEntry, signing_key_and_cert: tuple[Path, Path]
) -> None:
    key_path, cert_path = signing_key_and_cert
    payload = {
        "LoTE": {
            "ListAndSchemeInformation": {
                "LoTEType": "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
                "StatusDeterminationApproach": (
                    "http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU"
                ),
                "SchemeTypeCommunityRules": [
                    {
                        "lang": "en",
                        "uriValue": "http://uri.etsi.org/19602/PIDProviders/schemerules/EU",
                    }
                ],
                "ListIssueDateTime": "2026-01-01T00:00:00Z",
                "NextUpdate": "2026-07-01T00:00:00Z",
            },
            "TrustedEntitiesList": [
                {
                    "TrustedEntityServices": [
                        {
                            "ServiceInformation": {
                                "ServiceTypeIdentifier": (
                                    "http://uri.etsi.org/19602/SvcType/PID/Issuance"
                                )
                            }
                        }
                    ]
                }
            ],
        }
    }
    signed = sign_json(payload, key_path, cert_path)
    mock_fetch.return_value = (
        json.dumps(signed).encode(),
        "application/json",
        None,
    )
    sample_tl_entry.trust_anchor = cert_path.read_text()
    sample_tl_entry.tl_url = "https://example.com/tl.json"
    sample_tl_entry.tl_url_xml = None
    sample_tl_entry.tl_url_json = "https://example.com/tl.json"
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=True)
    assert errors == []


@patch("tools.lotl.published_validate.fetch_published")
def test_crypto_missing_trust_anchor(mock_fetch, sample_tl_entry: TLEntry) -> None:
    mock_fetch.return_value = (PID_XML, "application/xml", None)
    sample_tl_entry.trust_anchor = "not-a-cert"
    sample_tl_entry.tl_url = "https://example.com/tl.xml"
    sample_tl_entry.tl_url_json = None
    sample_tl_entry.tl_url_xml = "https://example.com/tl.xml"
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=True)
    assert any("trust_anchor" in e for e in errors)


@patch("tools.lotl.published_validate.fetch_published")
@patch("tools.lotl.published_validate.validate_tl_signature_json")
def test_json_crypto_failure(
    mock_crypto, mock_fetch, sample_tl_entry: TLEntry
) -> None:
    mock_fetch.return_value = (b'{"LoTE":{}}', "application/json", None)
    mock_crypto.return_value = (False, "nope")
    sample_tl_entry.tl_url = "https://example.com/tl.json"
    sample_tl_entry.tl_url_xml = None
    sample_tl_entry.tl_url_json = "https://example.com/tl.json"
    errors = validate_entry_publications(sample_tl_entry, verify_crypto=True)
    assert any("JSON signature verification failed" in e or "not signed" in e for e in errors)
