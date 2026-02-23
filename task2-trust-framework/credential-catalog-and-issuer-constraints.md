# Credential Catalogues and Issuer Constraints: Overview

This document provides an overview of two closely related topics in the EUDI Wallet trust framework:

1. **Credential catalogues** – How attestation types and attributes are defined and discovered
2. **Trusted List extensions for credential issuers** – How Trusted Lists and registration certificates constrain which Credential Issuers are authorised to issue specific attestation types

Catalogues define **what** credential types exist; Trusted Lists and registration certificates define **who** is allowed to issue them (ARF Topic 27, RPRC_15).

## Document Structure

This content has been split into two focused documents:

### 1. Credential Catalogue

**[credential-catalogue.md](credential-catalogue.md)** – Catalogue of attributes and catalogue of attestation schemes

Covers:
- The two Commission-run catalogues (attributes, attestation schemes)
- Registration requirements and legal basis (CIR 2025/1569, Articles 7 and 8)
- EAA types (QEAA, PuB-EAA, non-qualified EAA) in the context of catalogue registration
- Scheme vs. Rulebook distinction
- Technical Specification 11 and ARF references

### 2. Trusted List Extensions for Credential Issuers

**[trusted-list-extensions-credential-issuers.md](trusted-list-extensions-credential-issuers.md)** – Trusted List extensions for Credential Issuers and credential type

Covers:
- Using Trusted Lists and registration certificates to configure allowed attestation types per issuer (ARF RPRC_15, Topic 27)
- `serviceInformationExtensions`, `allowedAttestationType`, self-contained vs. certificate-referenced Trusted List entries
- Wallet and Relying Party validation behaviour
- Non-normative examples of Trusted List entries
- Proposal: `registrationCertificateHash` field

## Key Relationships

| Topic | Defines | Primary Reference |
|-------|---------|-------------------|
| **Catalogue of attributes** | Verification points for QTSPs issuing QEAAs | [credential-catalogue.md](credential-catalogue.md#catalogue-of-attributes) |
| **Catalogue of attestation schemes** | Attestation types and their structure | [credential-catalogue.md](credential-catalogue.md#catalogue-of-attestation-schemes) |
| **Trusted Lists** | Which issuers are authorised for which attestation types | [trusted-list-extensions-credential-issuers.md](trusted-list-extensions-credential-issuers.md) |
| **Registration certificates** | Attestation types an issuer intends to issue (when available) | [trusted-list-extensions-credential-issuers.md](trusted-list-extensions-credential-issuers.md#registration-certificate-as-source-of-truth-when-available) |

## Quick Reference

### Entity and Terminology
- [terms-and-entities.md](../task1-use-cases/terms-and-entities.md)

### Trust Infrastructure
- [trust-infrastructure-schema.md](trust-infrastructure-schema.md) – Registration, notification, Trusted List publication

### ARF v2.8.0
- [Section 5.5 - Catalogue of attributes and catalogue of attestation schemes](https://eudi.dev/2.8.0/architecture-and-reference-framework-main/#55-catalogue-of-attributes-and-catalogue-of-attestation-schemes)
- [Annex 2.02 - High-Level Requirements by Topic](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/)
