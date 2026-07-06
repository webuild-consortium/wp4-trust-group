# Task 5: Participants' Certificates and Policies

This task defines the data models and trust evaluation methods for participants' certificates and policies in the WP4 Trust Infrastructure.

**Note on Schema Harmonization**: The data models defined in this task are harmonized with the [Onboarding API schemas](../task4-trust-infrastructure-api/onboarding-api/README.md#data-models) and the [onboarding use case documents](../task1-use-cases/subtask1-1-onboarding/onboarding-base.md) to ensure consistency across the trust infrastructure. Participant types, status values, certificate types, and certificate status values are aligned across all specifications.

## Folder contents

- **`README.md`** – Overview of Task 5 and its subcomponents
- **`policy-approaches-definition.md`** – Description of additive vs. subtractive policy approaches in the WP4 trust framework
- **`etsi-policy-enumeration.md`** – Enumeration of ETSI policy identifiers and mechanisms relevant for the trust framework
- **`etsi-policy-evaluation.md`** – Analysis of ETSI specifications and how they are applied in additive/subtractive policy evaluation
- **`trust-mark-semantics-implementation.md`** – Guidance on implementing trust mark semantics for Credential Issuers and Relying Parties
- **`data-model/`** – Subtask 5.1: data model specifications for certificates, policies, participants and relationships
- **`trust-evaluation-methods/`** – Subtask 5.2: algorithms and methods for trust scoring, assessment, validation and monitoring

## Scope of Task 5

- **Data models** – Define structured representations for certificates, policies, participants and trust relationships that are used across APIs and services.
- **Trust evaluation methods** – Specify scoring algorithms, risk‑based evaluation, and validation/monitoring procedures that operate on those models.
- **Policy handling** – Map high‑level policy concepts from Task 2 and PKI profiles from Task 3 to concrete ETSI‑aligned policy artefacts.
- **Integration** – Provide the certificate and policy information consumed by the Trust Infrastructure API (Task 4), conformance checks (Task 6) and testing (Task 7).
