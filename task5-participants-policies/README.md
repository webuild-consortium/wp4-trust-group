# Task 5: Participants' Certificates and Policies

This task defines the data models and trust evaluation methods for participants' certificates and policies in the WP4 Trust Infrastructure.

**Note on Schema Harmonization**: The data models defined in this task are harmonized with the [Onboarding API](../task4-trust-infrastructure-api/onboarding-api/README.md) and the [onboarding use case documents](../task1-use-cases/subtask1-1-onboarding/onboarding-base.md) to ensure consistency across the trust infrastructure. Participant types, status values, certificate types, and certificate status values are aligned across all specifications.

## Folder contents

- **`README.md`** – Overview of Task 5 and its subcomponents
- **`relying_party_access_certificate.md`** – WRPAC (access certificate) profile for Relying Parties
- **`relying_party_registration_certificate.md`** – WRPRC (registration certificate) profile for Relying Parties. JWT `sub` SHALL equal the paired WRPAC `organizationIdentifier` (legal person) or `serialNumber` (natural person); see [identifier binding](../task3-x509-pki-etsi/etsi-identifier-handling.md#binding-wrpac-identifier-to-wrprc-sub).
- **`pid_provider_access_certificate.md`** – Access certificate profile for PID Providers
- **`eaa_provider_access_certificate.md`** – Access certificate profile for Attestation Providers
- **`eaa_provider_registration_certificate.md`** – Registration certificate profile for Attestation Providers
- **`entity-service-taxonomy.md`** – Two-layer taxonomy: EU entitlements (Layer 1) and domestic activity codes (Layer 2)
- **`policy-approaches-definition.md`** – Description of additive vs. subtractive policy approaches in the WP4 trust framework
- **`etsi-policy-enumeration.md`** – Enumeration of ETSI policy identifiers and mechanisms relevant for the trust framework
- **`etsi-policy-evaluation.md`** – Analysis of ETSI specifications and how they are applied in additive/subtractive policy evaluation
- **`trust-mark-semantics-implementation.md`** – Guidance on implementing trust mark semantics for Credential Issuers and Relying Parties
- **`embedded-disclosure-policies-implementation.md`** – Implementation guidance for disclosure policies embedded in presentation requests
- **[`../task5-participants-certificates-policies/ts5-registry-api-and-data-formats.md`](../task5-participants-certificates-policies/ts5-registry-api-and-data-formats.md)** – TS5 registrar API, JWS response shapes, and Annex A.1 data model notes (wallet-relying party registry)

## Data models

Certificate and policy data models used across onboarding and APIs live in this folder (WRPAC/WRPRC and provider certificate profiles above) and in the [TS5 registry API notes](../task5-participants-certificates-policies/ts5-registry-api-and-data-formats.md). Participant types, status values, certificate types, and certificate status values are aligned with the [Onboarding API](../task4-trust-infrastructure-api/onboarding-api/README.md) and the [onboarding use cases](../task1-use-cases/subtask1-1-onboarding/onboarding-base.md).

## Scope of Task 5

- **Data models** – Define structured representations for certificates, policies, participants and trust relationships that are used across APIs and services.
- **Trust evaluation methods** – Specify scoring algorithms, risk‑based evaluation, and validation/monitoring procedures that operate on those models.
- **Policy handling** – Map high‑level policy concepts from Task 2 and PKI profiles from Task 3 to concrete ETSI‑aligned policy artefacts.
- **Integration** – Provide the certificate and policy information consumed by the Trust Infrastructure API (Task 4), conformance checks (Task 6) and testing (Task 7).
