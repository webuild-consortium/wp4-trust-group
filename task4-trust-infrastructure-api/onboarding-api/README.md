# Onboarding API

This directory contains the implementation and detailed specification of the Onboarding API for the WP4 Trust Infrastructure.

**Note on Schema Harmonization**: The data models defined in this API are harmonized with the [Task 5 data models](../../task5-participants-certificates-policies/README.md#data-models) and the [onboarding use case documents](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md) to ensure consistency across the trust infrastructure. Participant types, status values, certificate types, and certificate status values are aligned across all specifications.

## Folder contents

- **`README.md`** – Summary of the Onboarding API responsibilities and main resources

## Scope of the Onboarding API

- **Participant registration and management** – Register participants (TSPs, Wallet Providers, RPs, CAs), manage their data and track registration status.
- **Certificate management** – Submit, validate, store, retrieve and revoke participant certificates used by the trust infrastructure.
- **Policy management** – Submit, review and manage participant policies in the identity, security, operational and legal domains.
- **Compliance and audits** – Run compliance checks, manage audits and publish compliance status and reports for participants.
