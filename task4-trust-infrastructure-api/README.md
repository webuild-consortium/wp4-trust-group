# Task 4: Trust Infrastructure APIs

This task defines and implements the APIs used to expose the WP4 Trust Infrastructure, including the core Trust Infrastructure API and the Onboarding API.

## Folder contents

- **`README.md`** – Overview of the APIs and how this task fits in WP4
- **`trust-infrastructure-api/`** – Implementation and detailed specification of the Trust Infrastructure API (see its `README.md`)
- **`onboarding-api/`** – Implementation and detailed specification of the Onboarding API (see its `README.md`)

## Scope of Task 4

- **Trust Infrastructure API** – Endpoints and models for trust management, evaluation, validation, policies and monitoring, built on top of the trust framework and PKI from Tasks 2 and 3.
- **Onboarding API** – Endpoints and models for participant registration, certificate and policy submission, compliance validation and audit support. Aligns with EC TS05 and EC TS06 for registry data models and retrieval APIs, and with EC TS02 for provider notification and publication flows.
- **Cross‑cutting API aspects** – Common design and runtime concerns such as REST style, OpenAPI descriptions, authentication and authorization (OAuth 2.0 / OpenID Connect / JWT), error handling, monitoring and versioning.

## Normative References

The APIs in this task align with the following European Commission technical specifications and related standards. The [EUDI Wallet Architecture and Reference Framework (ARF) v2.9.0](https://eudi.dev/2.9.0/architecture-and-reference-framework-main/) indexes these specifications under [Technical Specifications](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/technical-specifications); the canonical documents are published in the [eudi-doc-standards-and-technical-specifications](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications) repository.

### European Commission Technical Specifications

- **EC TS02** — Specification of systems enabling notification and publication of Provider information (relevant for provider notification and publication in the trust infrastructure; see ARF Topic 31, **GenNot_01**)
  - [Official document](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md)
  - [ARF index](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md)
- **EC TS05** — Common Formats and API for Relying Party Registration Information (registry API formats and retrieval endpoints; see ARF Topic 27, **Reg_03**, **Reg_06**)
  - [Official document](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md)
  - [ARF index](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md)
- **EC TS06** — Common set of Relying Party information to be registered (minimum data set for participant registration; see ARF Topic 27, **Reg_01a**)
  - [Official document](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md)
  - [ARF index](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md)

### ETSI (upcoming)

- **ETSI EN 319 486** — Common formats and API for Relying Party Registry information (under development at ETSI; expected to standardize the formats and API defined in EC TS05). See [ETSI work item DEN/ESI-0019486](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74933).

### Related project references

- [Onboarding use cases](../task1-use-cases/subtask1-1-onboarding/onboarding-base.md) — Participant registration flows that inform the Onboarding API
- [Trust Infrastructure Schema](../task2-trust-framework/trust-infrastructure-schema.md) — Registry publication and API requirements (**Reg_03**, **Reg_06**)
- [Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) — Legal basis for RP registration and registry APIs (Annex II)
