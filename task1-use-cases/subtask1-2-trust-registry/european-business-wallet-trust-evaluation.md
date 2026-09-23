# Use Case UC-TE-07: European Business Wallet Trust Evaluation Overlay

This use case applies the existing trust-evaluation flows when the wallet is a **European Business Wallet (EBW)** and when the core identity attestation is **EBWOID** (owner identification data), not a natural-person PID.

**Framework (normative for WP4 trust interpretation):** [European Business Wallet in the WP4 Trust Framework](../../task2-trust-framework/european-business-wallet-trust-framework.md).  
**Common evaluation machinery:** [UC-TE-01 Trust evaluation base](trust-evaluation-base.md).  
**Terms:** [Consolidated Terms and Entity Definitions](../terms-and-entities.md).

This document does **not** repeat the EBW legal background. It only states **who evaluates whom**, which **trust sources** apply, and how that maps to onboarding (Task 1.1).

## Scope

| In scope | Out of scope (other WPs / later WP4) |
|----------|--------------------------------------|
| EBW Provider listed as Wallet Provider | Separate production EBW-provider trusted list under COM(2025) 838 |
| EBWOID issued as QEAA or PuB-EAA | European Digital Directory as a trust source |
| EBW Unit as holder in issuance and presentation | QERDS addressing and legal equivalence of submissions |
| EBW as Relying Party (WRPAC/WRPRC) | Mandate / power-of-attorney protocol |
| Registrar discovery via `EURegistrarsAndRegistersList` | Confidential-attribute access-authorization credential (open: [#89](../../task6-wallet-conformance-interop/issue-89-resolution.md)) |

## Actors

- **EBW Unit** — wallet unit of an economic operator (holder). Primary evaluator in TE-07.1 and TE-07.3.
- **EBW Provider** — Wallet Provider of that unit. Listed on `EUWalletProvidersList` (same LoTE as EUDI Wallet Providers).
- **EBWOID Provider** — Attestation Provider (QEAA or PuB-EAA) issuing owner identification data. **Not** the LoTL folder `ebwoid-provider`.
- **Relying Party** — including another EBW or a public body acting as verifier. Registered; not TL-listed.
- **Credential Issuer** — any PID/EAA/QEAA/PuB-EAA provider issuing into the EBW (EBWOID or other attestations).
- **LoTL / LoTE / Registry** — trust sources as in UC-TE-01.

## Onboarding mapping (Task 1.1)

No new onboarding use case is required for the pilot. Existing UCs already cover the listing paths:

| Participant | Use case | What to declare for EBW |
|-------------|----------|-------------------------|
| EBW Provider | [UC-03 Wallet Provider](../subtask1-1-onboarding/wallet-provider-onboarding.md) | Solution type = European Business Wallet for legal persons |
| EBWOID Provider | [UC-02 PID / EAA Provider](../subtask1-1-onboarding/pid_eaa_provider_onboarding.md) | Attestation type(s) include EBWOID (schema may still be named LPID) |
| EBW acting as RP | [UC-01 Relying Party](../subtask1-1-onboarding/relying_party_onboarding.md) | Same WRPAC/WRPRC registration; EUID preferred official identifier |
| Registrar / register TLP | Operational [TL onboarding](../subtask1-1-onboarding/trusted-lists-onboarding.md) as `ebwoid-provider` | Folder means **Annex I registrars list**, not EBWOID issuers |

Pilot registration of EBW Providers follows the same MVP/MVP+ split as other Wallet Providers ([onboarding-base](../subtask1-1-onboarding/onboarding-base.md)).

## Mapping of existing evaluation use cases

| Existing UC | When the wallet is an EBW |
|-------------|---------------------------|
| [UC-TE-02](wallet-unit-evaluates-credential-issuer.md) Wallet Unit evaluates issuer | **Applies.** Requested attestation type may be EBWOID. Issuer entitlement (ISSU_34a) must include that type. |
| [UC-TE-03](credential-issuer-evaluates-wallet-unit.md) Issuer evaluates Wallet Unit | **Applies with a gap.** Same Wallet Provider LoTE; organisational WUA ([EWC RFC 006](https://github.com/EWC-consortium/eudi-wallet-rfcs)) is not yet a WP4 profile. Pilot may use RFC 004 WIA/KA. |
| [UC-TE-04](wallet-unit-evaluates-relying-party.md) Wallet Unit evaluates RP | **Applies.** RPRC_21 bounds requested attributes. Insufficient alone for confidential EBW attributes ([#89](../../task6-wallet-conformance-interop/issue-89-resolution.md)). |
| [UC-RPI-01](relying-party-intermediary-use-case.md) Intermediary | **Applies** when an intermediary presents to an EBW or presents on behalf of an EBW-as-RP. |
| [UC-TE-05](relying-party-evaluates-credentials.md) RP evaluates credentials | **Applies.** EBWOID is validated as QEAA/PuB-EAA, **not** as PID (do not use PID Provider LoTE for EBWOID). |
| [UC-TE-06](trusted-list-discovery-consumption.md) LoTL consumption | **Applies.** Additional list type: `EURegistrarsAndRegistersList` (`ebwoid-provider` entries). |

## Extended flows

### TE-07.1 EBW Unit evaluates EBWOID Provider (before owner-ID request)

Same steps as [UC-TE-02](wallet-unit-evaluates-credential-issuer.md) with:

1. Attestation type = EBWOID (or LPID schema id if that is what the catalogue/rulebook publishes).
2. Trust anchors from **QEAA national QTSP TL** or **PuB-EAA LoTE**, never from `lotl/tl_entries/ebwoid-provider/`.
3. If the registration certificate or Registrar API does not list EBWOID/LPID as an entitled type, the unit MUST NOT request issuance (ISSU_34a).

**Gap:** the WP4 [credential catalogue](../../task2-trust-framework/credential-catalogue.md) does not yet publish a canonical EBWOID/LPID scheme id.

### TE-07.2 EBWOID Provider evaluates EBW Unit (before issuance)

Same steps as [UC-TE-03](credential-issuer-evaluates-wallet-unit.md):

1. Validate WUA against **Wallet Provider LoTE** (`EUWalletProvidersList`).
2. Confirm the listed solution is in **valid** status (GenNot_05).
3. Confirm Wallet Instance / WSCD not revoked (Topic 38).

**Gap:** organisational wallet unit attestation is not specified in Task 3/5. Until it is, issuers SHOULD document whether they accept RFC 004 individual WUA, RFC 006 organisational WUA, or both.

### TE-07.3 EBW Unit evaluates Relying Party (before presentation)

Same steps as [UC-TE-04](wallet-unit-evaluates-relying-party.md) (WRPAC via Access CA LoTE; WRPRC in the request; RPRC_21; registry fallback).

| Data class (architecture [#137](https://github.com/webuild-consortium/wp4-architecture/issues/137)) | WP4 evaluation today |
|-----------------------------------------------------------------------------------------------|----------------------|
| Public (EBWOID, EU company certificate, voluntarily shared EAAs) | WRPRC + RPRC_21 |
| Confidential (UBO, IBAN, …) | Same WRPRC path only — **no** legitimate-interest attestation type |

Holder-side per-RP access matrices (architecture Option 1) are Wallet Provider scope, not this use case.

### TE-07.4 Relying Party evaluates EBWOID and bound attestations

Same steps as [UC-TE-05](relying-party-evaluates-credentials.md):

1. Resolve issuer trust anchors from LoTL → QEAA/PuB-EAA/EAA list (UC-TE-06).
2. Validate EBWOID signature, issuer status, and revocation as required by the attestation scheme.
3. If a rulebook requires wallet binding, validate WUA / key binding against the Wallet Provider LoTE.
4. Validate additional EAAs independently (each against its issuer TL and any `allowedAttestationType` constraint).

An EBW deployer that accepts only a **private subset** of issuers is **unspecified** ([#75](../../task6-wallet-conformance-interop/issue-75-resolution.md)). Ecosystem TL validation remains mandatory regardless of any private allow-list.

## Success criteria

- EBW Unit requests EBWOID only from an issuer entitled for that attestation type and valid in the applicable QEAA/PuB-EAA/EAA list.
- EBWOID Provider issues only to an EBW Unit whose Wallet Provider is valid in `EUWalletProvidersList`.
- Presentation to an RP proceeds only after WRPAC/WRPRC (or documented registry fallback) succeed.
- Verifiers never treat `ebwoid-provider` LoTL entries as EBWOID issuer trust anchors.
- Failed checks stop the flow and surface a clear error to the authorised representative.

## ARF / WP4 requirement mapping

ARF requirements used here are the same identifiers as UC-TE-02–05 (ISSU_24/24a/33/33a/34/34a, ISSU_19/21, RPA_04, RPRC_17/19/21, GenNot_05, CT_05). The ARF does **not** define legal-person Wallet Units; WP4 applies those requirements **by analogy** to EBW Units and treats EBWOID as an attestation (OIA_13/14/15, ISSU_08/09/10), not as PID (OIA_12, ISSU_07).

## References

- [European Business Wallet in the WP4 Trust Framework](../../task2-trust-framework/european-business-wallet-trust-framework.md)
- [Trust evaluation base](trust-evaluation-base.md)
- [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation)
- [EUDI Wallet trust and entitlement discovery](../../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md)
- [EWC RFC 005 LPID](https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/ewc-rfc005-issue-legal-person-identification-data.md), [EWC rb001](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb001-legal-person-identification-data.md)
- Issues [#90](https://github.com/webuild-consortium/wp4-trust-group/issues/90), [#89](https://github.com/webuild-consortium/wp4-trust-group/issues/89), [#75](https://github.com/webuild-consortium/wp4-trust-group/issues/75)
