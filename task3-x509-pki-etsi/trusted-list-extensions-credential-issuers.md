# Trusted List Extensions for Credential Issuers and Credential Type

This document describes how Trusted Lists and registration certificates configure which Credential Issuers (PID Providers, QEAA Providers, PuB-EAA Providers, EAA Providers) are authorised to issue specific **attestation types** (ARF RPRC_15, Topic 27). For **what** credential types exist, see [credential-catalogue.md](../task2-trust-framework/credential-catalogue.md).

## Trust Model

- Trust anchor placement and TL responsibilities: [trust-infrastructure-schema.md](../task2-trust-framework/trust-infrastructure-schema.md) (Section 3), ARF Topic 27, Topic 31.
- Entity definitions: [terms-and-entities.md](../task1-use-cases/terms-and-entities.md). Different trust levels apply for non-qualified EAA Providers vs QEAA/PuB-EAA Providers.

## Using Trusted Lists to Configure Allowed Credential Issuers for Specific Attestation Types

### Purpose

Trusted Lists and registration certificates configure which Credential Issuers are allowed to issue specific **attestation types** (ARF RPRC_15, Topic 27).

### Trusted List Owner

Per [trust-infrastructure-schema.md](../task2-trust-framework/trust-infrastructure-schema.md), Trusted Lists are published by Trusted List Providers (European Commission or Member State TLPs). For sector-specific or scheme-specific Trusted Lists, the entity accountable for the list is sometimes referred to as **Trusted List Owner**, **Ecosystem Authority**, or **Scheme Owner** (see [terms-and-entities.md](../task1-use-cases/terms-and-entities.md)).

### Registration Certificate as Source of Truth (when available)

- As specified in the ARF (Topic 27 and the registration certificate requirements, e.g. RPRC_15), a **registration certificate** issued to a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider **SHALL contain the type(s) of attestation that this entity intends to issue to Wallet Units**.
- However, registration certificates are **optional** - they are issued "if the Registrar has a policy of issuing such certificates" (ARF Section 6.3.2.2).
- When a registration certificate is available, per ARF RPRC_22 it SHALL be included **by value** in Credential Issuer metadata during issuance (ETSI TS 119 472-3, §4.2.3), providing a self-contained verification; Trusted List entries may optionally reference it via `registrationCertificateRef` (ETSI TS 119 602, clause 6.6.9).

### Trusted List Entry for Each Provider

- For each Provider role (PID, QEAA, PuB-EAA, EAA), the Trusted List includes the **trust anchor** (public key / certificate) and **metadata** that links the Provider to its registration information.
- This metadata can either:
  - Contain a **machine-readable list of allowed attestation type identifiers / namespaces** directly (making the TL entry self-contained), or
  - Contain a **pointer (URL, reference, identifier)** to the Provider's registration certificate or Registrar API, where the list of allowed attestation types is maintained.

### Conflict Resolution between Trusted List, Registry, and Registration Certificate

When a Trusted List entry is **self-contained** (embedded `allowedAttestationType`, no pointer), Relying Parties follow the TL metadata during validation. The TL may not reflect the current registration state if the Registry or registration certificate contains different attestation types. The following risks are not currently addressed by explicit requirements:

| Risk | Description |
|------|-------------|
| **Disagreement** | No rule when TL metadata and Registry/registration certificate disagree on allowed attestation types. |
| **Precedence** | No hierarchy (Registry vs TL) defined. |
| **Cross-checking** | No requirement to compare TL with Registry during validation. |
| **Staleness** | No rule for TL update frequency when Registry or registration changes. |

**Mitigation approaches** (for further discussion):
- Define precedence rules (e.g., TL as canonical for RP validation vs. Registry as source of truth for registration state).
- Require or recommend cross-checking TL against Registrar API when both are available, with explicit behaviour on mismatch.
- Specify TL update obligations or maximum staleness when self-contained entries are used.
- Prefer pointers (`registrationCertificateRef` or Registrar URI) over embedded lists when registration state changes frequently, so RPs always obtain current data.

**Specification-based approaches** (from ARF and ETSI):

The following provisions from existing specifications inform conflict resolution; they do not explicitly address `allowedAttestationType` disagreement but provide analogous guidance:

| Source | Provision | Relevance |
|--------|-----------|-----------|
| **ETSI TS 119 615** | Trusted lists are "legally constitutive information" regarding qualified status (NOTE 2, clause 4.4.4); certificate–TL mismatch (e.g. `ERROR_TSP_NAME_INCONSISTENCY_BETWEEN_CERT_AND_TL`) leads to PROCESS_FAILED or INDETERMINATE | TL is the canonical reference for validation; external data (cert) must align with TL |
| **ETSI TS 119 602, clause 6.3.15** | `NextUpdate`: The scheme operator SHALL issue an update before `NextUpdate` whenever changes occur to trusted entity or service information (e.g. status). LoTE with past `NextUpdate` SHALL be discarded as expired | TL staleness is controlled; changes to registration/status should trigger TL update; expired TL entries are invalid |
| **ARF GenNot_05** | Suspension/cancellation of a Provider SHALL result in TL status changed to Invalid | Registry status (suspension/cancellation) drives TL updates; Registry is source for lifecycle state |
| **ARF Reg_07, Reg_08, Reg_09** | Registrars enable updates; entities SHALL update registry without undue delay; all changes SHALL be logged | Registry is the authoritative source for registration state; TL is published output of notification (Topic 31) |
| **ARF ISSU_24a, ISSU_34a** | Wallet verification order: (a) registration cert in Credential Issuer metadata, (b) Registrar URI, (c) entitlement in metadata. No TL reference in this flow | At issuance, Registry/registration cert is used; at presentation, RP uses TL (OIA_12–15) |

**Proposed approach** (to be confirmed with stakeholders):
- **Precedence**: Treat TL as canonical for RP credential validation (OIA_12–15), consistent with ETSI TS 119 615. Treat Registry/registration cert as authoritative for issuance-time verification (ISSU_24a, ISSU_34a).
- **Staleness**: Apply ETSI TS 119 602 `NextUpdate` semantics: TL entries with embedded `allowedAttestationType` should be updated when Registry or registration status changes; TL providers should respect `NextUpdate` obligations.
- **Cross-checking**: Not mandated today. When both TL and Registrar URI are available, implementations may optionally cross-check and log mismatches for operational monitoring.

### Self-contained Trusted List Entries

- **Credential validation (presentation)**: When verifying issuer entitlement to an attestation type, embedded `allowedAttestationType` in the TL entry suffices; no registration certificate needed.
- **Registration verification (issuance)**: Before requesting a PID or attestation, the Wallet Unit SHALL verify the provider is registered (ISSU_24a for PID, ISSU_34a for attestation): (a) registration certificate in Credential Issuer metadata, or (b) Registrar URI in Credential Issuer metadata.

### Wallet and Relying Party Behaviour

When a Wallet Unit or Relying Party receives a credential, it:

1. Reads the **attestation type identifier / namespace** from the credential.
2. Identifies the **issuer** from the credential's signing certificate and locates the corresponding **Trusted List entry** (by matching the signing certificate against trust anchors in the TL; the certificate does *not* contain a pointer to the TL — see [Trusted List discovery and consumption](../task1-use-cases/subtask1-2-trust-registry/trusted-list-discovery-consumption.md) and ETSI TS 119 615 clause 4.3).
3. From the Trusted List entry (or the referenced registration certificate / Registrar API), obtains the list of **attestation types the issuer is authorised to issue**.
4. **Accepts** the credential as being of that attestation type **only if**:
   - The issuer is present in the applicable Trusted List, and
   - The attestation type in the credential is listed in the issuer's authorised types.

Catalogue defines **what** credential types exist; Trusted Lists and registration certificates define **who** may issue them (RPRC_15, Topic 27). See [credential-catalogue.md](../task2-trust-framework/credential-catalogue.md).

## Non-normative Examples

Illustrative only; no ETSI encoding prescribed.

### Example 1 – QEAA Provider (PID, tax-residency)

- `serviceTypeIdentifier` = `QEAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.pid.1`
  - `allowedAttestationType`: `eu.europa.ec.eudi.tax-residency.1`
  - `registrationCertificateRef`: `<URL or hash of the registration certificate>`

### Example 2 – PuB-EAA Provider (public-benefit)

- `serviceTypeIdentifier` = `PuBEAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.public-benefit.1`
  - `registrationCertificateRef`: `<URL or hash of the registration certificate>`

### Example 3 – EAA Provider (sectoral attestations)

- `serviceTypeIdentifier` = `EAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.university-degree.1`
  - `allowedAttestationType`: `eu.europa.ec.eudi.professional-licence.1`
  - `registrationCertificateRef`: `<URL or hash of the registration certificate>`

`registrationCertificateRef` is optional. With embedded `allowedAttestationType`, the entry is self-contained and sufficient for validation.

### Example 4 – Self-contained entry (no registrationCertificateRef)

- `serviceTypeIdentifier` = `QEAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.pid.1`
  - `allowedAttestationType`: `eu.europa.ec.eudi.tax-residency.1`

## Registration vs. Notification

- **Registration**: Entities are registered by Registrars in Member States
- **Notification**: Registered entities are notified to the Commission and published in Trusted Lists

## Proposals for Further Discussion

### Registration Certificate Hash in Trusted Lists

**Proposal**: Consider adding a `registrationCertificateHash` field to the `ServiceInformationExtensions` component in Trusted List entries (as defined in ETSI TS 119 602, clause 6.6.9) to provide the certificate hash when a registration certificate URL is provided via `registrationCertificateRef`.

**Rationale**: Including a hash of the registration certificate alongside the URL reference would enable:
- Integrity verification of the certificate when retrieved
- Offline validation capabilities
- Reduced dependency on network availability for certificate verification

**Status**: This is a proposal to be further discussed with the European Commission and relevant standardization bodies. The field is not currently defined in ETSI TS 119 602, but the standard's extensible `ServiceInformationExtensions` mechanism (clause 6.6.9) allows for profile-specific extensions to be defined.

## References

- [credential-catalogue.md](../task2-trust-framework/credential-catalogue.md) | [trust-infrastructure-schema.md](../task2-trust-framework/trust-infrastructure-schema.md) | [terms-and-entities.md](../task1-use-cases/terms-and-entities.md)
- ARF: [Topic 27](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties) | [Topic 31](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2320-topic-31---notification-and-publication-of-pid-provider-wallet-provider-attestation-provider-access-certificate-authority-and-provider-of-registration-certificates)
- ETSI TS 119 602 v1.1.1 (6.3.15) | ETSI TS 119 615 v1.3.1 (4.4)
- [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183) | [eIDAS 910/2014 Art.22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0910)
