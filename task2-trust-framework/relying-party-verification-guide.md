# Relying Party Verification Guide: Accept or Reject a Presentation

**Audience:** developers building the verifier component of a Relying Party (RP) in WEBUILD.
**Reading time:** about 5 minutes.
**Scope:** what your verifier checks **after** a Wallet Unit has presented a PID or attestation, using the WEBUILD trust infrastructure. Normative detail lives in [UC-TE-05](../task1-use-cases/subtask1-2-trust-registry/relying-party-evaluates-credentials.md) and [UC-TE-06](../task1-use-cases/subtask1-2-trust-registry/trusted-list-discovery-consumption.md); requirement IDs in brackets refer to [ARF 3.0.0 Annex 2](https://eudi.dev/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/). The wallet-side counterpart is [EUDI Wallet Trust and Entitlement Discovery](eudi-wallet-trust-and-entitlement-discovery.md).

This guide is written for **testing in WEBUILD**. Differences for a production deployment are collected in [Before you go to production](#before-you-go-to-production).

## Before you start

- **Your RP is registered.** You hold an access certificate (WRPAC) and a registration certificate (WRPRC), and every attribute you request is listed in your WRPRC. Without this, the wallet refuses to present. See [UC-01 Relying Party onboarding](../task1-use-cases/subtask1-1-onboarding/relying_party_onboarding.md).
- **You can parse both list formats** (OIA_15b): ETSI TS 119 602 LoTE (JSON/XML; PID, PuB-EAA lists) and ETSI TS 119 612 Trusted Lists (XML; national QEAA and EAA lists).
- **You support both revocation mechanisms** (VCR_12): Attestation Status List ([Token Status List](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/)) and Attestation Revocation List.

> **Note – Intermediary.** If you verify on behalf of another RP, you run every check in this guide before forwarding (RPI_08, RPI_09), forward only to that intermediated RP, and delete the credentials immediately afterwards (RPI_10). See [UC-RPI-01](../task1-use-cases/subtask1-2-trust-registry/relying-party-intermediary-use-case.md).

> **Note – European Business Wallet.** Validate EBWOID as a **QEAA or PuB-EAA**, never against the PID Provider list. The `EURegistrarsAndRegistersList` (`ebwoid-provider` folder in the LoTL) lists registrars, not EBWOID issuers. EBWOID may get a dedicated LoTE in the future; check the LoTL for a new list type before relying on this rule. Details are being worked out in [PR #143](https://github.com/webuild-consortium/wp4-trust-group/pull/143).

## Where trust anchors come from

Start from the **WEBUILD LoTL**: <https://webuild-consortium.github.io/wp4-trust-group/> ([`list_of_trusted_lists.json`](https://webuild-consortium.github.io/wp4-trust-group/list_of_trusted_lists.json), [`.xml`](https://webuild-consortium.github.io/wp4-trust-group/list_of_trusted_lists.xml)). It points to every Trusted List you need. Pick the list by credential type:

| Credential type | Trust source in the LoTL | Requirement |
|---|---|---|
| PID | LoTE type `.../19602/LoTEType/EUPIDProvidersList` | OIA_12 |
| QEAA | National TS 119 612 TL, service type `.../Svctype/EAA/Q`; qualified signature per eIDAS Art. 32 | OIA_13 |
| PuB-EAA | LoTE type `.../19602/LoTEType/EUPubEAAProvidersList` | OIA_14 |
| Non-qualified EAA | National TS 119 612 TL, service type `.../Svctype/EAA`, or the mechanism defined in the attestation's Rulebook | OIA_15 |
| EBWOID | As QEAA or PuB-EAA, depending on the issuer (see note above) | UC-TE-07 |

**About the LoTL signing certificate.** The WEBUILD LoTL is signed (JAdES for JSON, XAdES for XML), but its signing certificate is currently delivered only inside the LoTL's own signature header. A forged LoTL could carry a forged certificate and still "verify". Until WP4 publishes the certificate through a separate channel, use **trust on first use**: on the first fetch, take the certificate from the signature header, store its SHA-256 fingerprint, and from then on accept only LoTLs signed with that certificate. If the fingerprint changes, reject the LoTL and confirm the change with WP4 before you pin the new value.

## You should accept if …

… **all** of the following hold. The order is the order you implement them.

1. **The lists are authentic and current.** The LoTL signature verifies with your pinned certificate. Each Trusted List you use verifies with the signing certificate the LoTL gives for it. No list you rely on is past its `NextUpdate` (TLPub_03, TLPub_05, OIA_15a). *(Production: see below.)*
2. **The issuer chains to the right anchor.** The issuer's certificate chains to a trust anchor in the list that matches the credential type in the table above (OIA_12 – OIA_15).
3. **The issuer is not Invalid.** The matching list entry does not have status Invalid. Suspended or cancelled providers are marked Invalid (GenNot_05).
4. **The issuer signature verifies.** The SD-JWT VC issuer signature, or the mdoc `IssuerAuth` (MSO), verifies with that issuer's key.
5. **The credential is not revoked.**
   - If the credential has a status reference: you fetched the status list or revocation list from the URL in the credential, its signature verifies against a trust anchor of the same provider, and the credential's status is valid (VCR_13). Cache status lists instead of fetching them for every presentation (VCR_15).
   - If it has no status reference: its validity period is 24 hours or less (VCR_01).
   - You don't need to check the Wallet Unit separately: the PID's status already covers revocation of the Wallet Unit ([ARF §6.6.3](https://eudi.dev/3.0.0/main/06-trust-model/)).

### Also required (outside the trust infrastructure)

These checks are not part of the trust infrastructure, but a valid issuer signature alone does not make a presentation safe:

- **Holder binding:** the key-binding JWT (SD-JWT VC) or the mdoc `DeviceSignature`/`DeviceMac` verifies with the key bound in the credential (OIA_17). See [SD-JWT](https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/), [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/), [ISO/IEC 18013-5](https://www.iso.org/standard/69084.html).
- **Nonce and audience:** the response carries the nonce and audience (client ID) of your own request, so it cannot be replayed. See [OpenID4VP 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html).
- **Validity period:** the current time is within the credential's `nbf`/`exp` (SD-JWT VC) or `validityInfo` (mdoc).
- **Disclosures:** every disclosed attribute matches a digest signed by the issuer.

## You should reject if …

… **any** of the following holds. Every failure is fail-closed: if you cannot complete a check, reject.

**Trust lists**
- The LoTL signature does not verify, or the signing certificate's fingerprint differs from the one you pinned.
- A Trusted List's signature does not verify with the certificate the LoTL gives for it.
- A list is past its `NextUpdate` and the refresh failed. Do not keep using a stale list.

**Issuer**
- The issuer's certificate chains only to an anchor in a **different** list. An anchor in *some* list is not enough. A PID validated against a QEAA list, or an issuer found only in a WRPAC list, is a reject.
- EBWOID was validated against the PID Provider list or the `EURegistrarsAndRegistersList`.
- The issuer's list entry has status Invalid, even if the credential itself has not expired (GenNot_05).
- The issuer signature does not verify.

**Revocation**
- The status is revoked or suspended.
- The status list cannot be fetched, or its signature does not verify.
- The credential is valid for more than 24 hours but carries no status reference (VCR_01, VCR_11a).

**Binding and protocol**
- A PID has no device binding, or its device-binding signature does not verify.
- An attestation's device-binding signature does not verify.
- The nonce or audience does not match your request, the credential is outside its validity period, or a disclosure does not match its digest.

**Exceptions.** The ARF only recommends checking revocation (VCR_13) and device binding (OIA_17). Skipping one of these checks, or accepting without reliable status information, is allowed only with a documented risk analysis for your use case (VCR_14). For the PID, device binding is always present, so a missing or failing device binding is always a reject.

## Tools and testing your verifier

- **[EUDI Trust Inspector](https://trust-inspector.credimi.io/)** shows the structure of the WEBUILD LoTL and its Trusted Lists.
- **[TL/LoTE Catalogue](https://lote.credimi.io/)** offers valid lists and **deliberately broken ones** (wrong signature, expired, wrong format). Point your verifier at the broken lists and confirm that it rejects every one of them.
- **[Token Status List Console](https://tsl.credimi.io/)** creates test credentials and lets you change their status. Revoke one and confirm that your verifier rejects it.
- **[Python signature libraries](../tools/python_signature_libraries.md)** lists libraries for verifying JAdES and XAdES signatures on Trusted Lists.
- More tools for verifier testing: [Task 7 – Testing and Validation](../task7-testing-validation/README.md).

## Before you go to production

The WEBUILD LoTL is a test infrastructure. In production:

- **Take the LoTL location and its signing anchor from the Official Journal of the EU** (TLPub_06, TLPub_07). Do not hard-code the WEBUILD URL, and do not rely on trust on first use.
- **Remove all test lists and test anchors** from your trust store, including the Credimi test lists.
- **Validate QEAAs as qualified signatures** per eIDAS Art. 32, and obtain non-qualified EAA anchors through the mechanism in the applicable Rulebook (ARF Topic 12). They may not be in any Trusted List.
- **Document every exception** to the fail-closed rules (stale lists, unreachable status, skipped device binding) in a risk analysis (VCR_14).
- **Run regular trust anchor management:** refresh lists before `NextUpdate`, and add or remove anchors as the lists change (OIA_15a).

## Further reading

- [Trust Evaluation Base](../task1-use-cases/subtask1-2-trust-registry/trust-evaluation-base.md): trust sources and ARF mapping
- [ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md): list types, service type URIs, formats
- [LoTL automation and TL integration](../task4-trust-infrastructure-api/lotl-automation-and-tl-integration.md): how the WEBUILD LoTL is built and signed
- [Consolidated Terms and Entity Definitions](../task1-use-cases/terms-and-entities.md)
