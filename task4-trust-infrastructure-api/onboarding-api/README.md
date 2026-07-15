# Onboarding API

This directory contains the implementation and detailed specification of the Onboarding API for the WP4 Trust Infrastructure.

**Note on Schema Harmonization**: The data models defined in this API are harmonized with the [Task 5 data models](../../task5-participants-certificates-policies/README.md#data-models) and the [onboarding use case documents](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md) to ensure consistency across the trust infrastructure. Participant types, status values, certificate types, and certificate status values are aligned across all specifications.

## Folder contents

- **`README.md`** – Summary of the Onboarding API responsibilities and main resources

## Scope of the Onboarding API

The Onboarding API exposes endpoints for:

- **Participant registration** — Submitting registration requests and identification data (aligned with [EC TS06](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md); ARF **Reg_01a**).
- **Certificate management** — Access Certificate and Registration Certificate issuance and lifecycle.
- **Policy management** — Attaching and querying entitlement and policy data.
- **Compliance and audit** — Verification of registered data and audit trail access.

Registry publication and retrieval follow [EC TS05](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) (ARF **Reg_03**, **Reg_06**). Provider notification and publication follow [EC TS02](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md) (ARF Topic 31, **GenNot_01**). [ETSI EN 319 486](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74933) (upcoming) will standardize the registry formats and API based on EC TS05.

## Normative References

The Onboarding API aligns with the following specifications for registration data and registry APIs:

- **EC TS05** — [Common Formats and API for Relying Party Registration Information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) — Registry API formats, signed JSON publication, and retrieval endpoints (ARF **Reg_03**, **Reg_06**)
- **EC TS06** — [Common set of Relying Party information to be registered](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md) — Minimum data set for registration (ARF **Reg_01a**)
- **EC TS02** — [Specification of systems enabling notification and publication of Provider information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md) — Provider notification and publication flows (ARF Topic 31, **GenNot_01**)
- **ETSI EN 319 486** (upcoming) — Will standardize common formats and API for Relying Party Registry information based on EC TS05

These specifications are indexed in the [ARF technical specifications](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main/docs/technical-specifications). See also the [Task 4 overview](../README.md#normative-references) and [onboarding use cases](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md).
