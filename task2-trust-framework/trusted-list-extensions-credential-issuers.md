# Trusted List Extensions for Credential Issuers and Credential Type

This document describes how Trusted Lists and registration certificates are used to configure which Credential Issuers (PID Providers, QEAA Providers, PuB-EAA Providers, EAA Providers) are authorised to issue specific **attestation types** (ARF RPRC_15, Topic 27).

For the catalogue of attributes and catalogue of attestation schemes (which define **what** credential types exist), see [credential-catalogue.md](credential-catalogue.md).

## Trust Model

- Trust anchor placement and Trusted List responsibilities per provider type: see [Trust Infrastructure Schema](trust-infrastructure-schema.md) (Overview, Section 3) and ARF Topic 27, Topic 31.
- Entity and terminology definitions: see [terms-and-entities.md](../task1-use-cases/terms-and-entities.md).
- A different level of trust applies when evaluating non-qualified EAA Providers compared to QEAA Providers and PuB-EAA Providers (see [trust-infrastructure-schema.md](trust-infrastructure-schema.md) Overview for Trusted List responsibilities per provider type).

## Using Trusted Lists to Configure Allowed Credential Issuers for Specific Attestation Types

### Purpose

Trusted Lists and registration certificates configure which Credential Issuers are allowed to issue specific **attestation types** (ARF RPRC_15, Topic 27).

### Trusted List Owner

Per [trust-infrastructure-schema.md](trust-infrastructure-schema.md), Trusted Lists are published by Trusted List Providers (European Commission or Member State TLPs). For sector-specific or scheme-specific Trusted Lists, the entity accountable for the list is sometimes referred to as **Trusted List Owner**, **Ecosystem Authority**, or **Scheme Owner** (see [terms-and-entities.md](../task1-use-cases/terms-and-entities.md)).

### Registration Certificate as Source of Truth (when available)

- As specified in the ARF (Topic 27 and the registration certificate requirements, e.g. RPRC_15), a **registration certificate** issued to a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider **SHALL contain the type(s) of attestation that this entity intends to issue to Wallet Units**.
- However, registration certificates are **optional** - they are issued "if the Registrar has a policy of issuing such certificates" (ARF Section 6.3.2.2).
- When a registration certificate is available, it is referenced from the Trusted List entry or from an associated Registrar service.

### Trusted List Entry for Each Provider

- For each Provider role (PID, QEAA, PuB-EAA, EAA), the Trusted List includes the **trust anchor** (public key / certificate) and **metadata** that links the Provider to its registration information.
- This metadata can either:
  - Contain a **machine-readable list of allowed attestation type identifiers / namespaces** directly (making the TL entry self-contained), or
  - Contain a **pointer (URL, reference, identifier)** to the Provider's registration certificate or Registrar API, where the list of allowed attestation types is maintained.

### Self-contained Trusted List Entries

If the `allowedAttestationType` list is embedded directly in the Trusted List entry's `serviceInformationExtensions`, Wallet Units and Relying Parties can perform validation using only the Trusted List, without needing to retrieve a registration certificate.
- When registration certificates are not available, Wallet Units should use the Registrar's online service URL (ARF ISSU_34a).

### Wallet and Relying Party Behaviour

When a Wallet Unit or Relying Party receives a credential, it:

1. Reads the **attestation type identifier / namespace** from the credential.
2. Identifies the **issuer** from the credential's signing certificate and locates the corresponding **Trusted List entry** (by matching the signing certificate against trust anchors in the TL; the certificate does *not* contain a pointer to the TL — see [Trusted List discovery and consumption](../task1-use-cases/subtask1-2-trust-registry/trusted-list-discovery-consumption.md) and ETSI TS 119 615 clause 4.3).
3. From the Trusted List entry (or the referenced registration certificate / Registrar API), obtains the list of **attestation types the issuer is authorised to issue**.
4. **Accepts** the credential as being of that attestation type **only if**:
   - The issuer is present in the applicable Trusted List, and
   - The attestation type in the credential is listed in the issuer's authorised types.

### Relation to Catalogue Entries

- The **catalogue of attributes** and **catalogue of attestation schemes** define **what** credential types and attributes exist and how they are structured (see [credential-catalogue.md](credential-catalogue.md)).
- Trusted Lists and registration certificates define **who** is allowed to issue which of those types (ARF RPRC_15, Topic 27).

## Non-normative Examples of Trusted List Entries

The following examples are **illustrative only** and do not prescribe a specific ETSI TL encoding, but show how information could be structured conceptually.

### Example 1 – QEAA Provider authorised for PID and tax-residency attestations

For each TL service entry:

- `serviceTypeIdentifier` = `QEAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.pid.1`
  - `allowedAttestationType`: `eu.europa.ec.eudi.tax-residency.1`
  - `registrationCertificateRef`: `<URL or hash of the registration certificate>`

### Example 2 – PuB-EAA Provider authorised only for a specific public-sector entitlement

For each TL service entry:

- `serviceTypeIdentifier` = `PuBEAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.public-benefit.1`
  - `registrationCertificateRef`: `<URL or hash of the registration certificate>`

### Example 3 – Non-qualified EAA Provider with sectoral attestation types

For each TL service entry:

- `serviceTypeIdentifier` = `EAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.university-degree.1`
  - `allowedAttestationType`: `eu.europa.ec.eudi.professional-licence.1`
  - `registrationCertificateRef`: `<URL or hash of the registration certificate>`

**Note on registration certificates**: The `registrationCertificateRef` field is **optional**. If the `allowedAttestationType` list is embedded directly in the Trusted List entry, the entry is **self-contained** and sufficient for validation without retrieving a separate registration certificate.

### Example 4 – Self-contained Trusted List entry (without registration certificate reference)

For a TL service entry that is self-contained:

- `serviceTypeIdentifier` = `QEAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.pid.1`
  - `allowedAttestationType`: `eu.europa.ec.eudi.tax-residency.1`
  - *(No `registrationCertificateRef` field - the TL entry is self-contained)*

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

### Related Documents
- [credential-catalogue.md](credential-catalogue.md) - Catalogue of attributes and catalogue of attestation schemes
- [trust-infrastructure-schema.md](trust-infrastructure-schema.md) - Trust anchor placement and Trusted List publication
- [terms-and-entities.md](../task1-use-cases/terms-and-entities.md) - Entity and terminology definitions

### ARF Requirements (ARF v2.8.0)
- [Topic 27 - Registration](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties) - RPRC_15: registration certificate SHALL contain attestation type(s)
- [Topic 31 - Notification and Publication](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2320-topic-31---notification-and-publication-of-pid-provider-wallet-provider-attestation-provider-access-certificate-authority-and-provider-of-registration-certificates)

### Legal Documents
- [European Digital Identity Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183)
- [Regulation (EU) No 910/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0910) (eIDAS Regulation) - Article 22 on Trusted Lists
