# Task 3: X.509 PKI with ETSI Alignments

This task specifies the X.509 PKI infrastructure for the WP4 Trust Infrastructure and aligns it with relevant ETSI and IETF standards.

## Folder contents

- **`README.md`** – Overview of the PKI role and its interaction with other tasks
- **`etsi_trusted_lists_implementation_profile.md`** – Implementation profile for ETSI TS 119 612 and TS 119 602 trusted lists, including signing, distribution, examples and testing guidance

## Scope of Task 3

- **PKI architecture** – Define CA hierarchy (root, intermediate, end‑entity, trust anchors) and certificate types for TSPs, Wallet Providers, Relying Parties, users and supporting services (OCSP, timestamping, etc.).
- **Certificate lifecycle** – Describe processes for request, issuance, validation, renewal and revocation, including CRL and OCSP usage.
- **Certificate Profiles and policies** – Map ETSI EN 319 412‑6, TS 119 411‑8 and TS 119 475 requirements to concrete certificate profiles and attributes used by the trust infrastructure.
- **Integration** – Provide PKI requirements consumed by the Trust Framework (Task 2), APIs (Task 4) and participant certificate/policy models (Task 5).
