# Subtask 1.2: Trust Registry and Trust Evaluation Use Cases

This subtask contains use cases for **trust registry operations** and **trust evaluation**: how ecosystem participants use Trusted Lists, registries, and certificates to establish and verify trust during credential issuance and presentation.

## Scope

- **Trust evaluation**: How Wallet Units, Relying Parties, PID Providers, Attestation Providers, and Holders (Users using the Wallet Unit) evaluate the trustworthiness of other participants using Trusted Lists (TL), List of Trusted Lists (LoTL), and Registrar registries.

For terminology and entity definitions, see [Consolidated Terms and Entity Definitions](../terms-and-entities.md).
- **Trust sources**: Access CA Trusted Lists, PID Provider TL, Attestation Provider TL (QEAA/PuB-EAA/EAA), Wallet Provider TL, Registration Certificate Provider TL, and National Registers (per [Trust Infrastructure Schema - Trust Evaluation](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation)).

These use cases are aligned with the [EUDI Wallet Architecture and Reference Framework (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/) and the [Trusted List / Registration / Trust Evaluation requirements matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md).

## Use Case Documents

| Use case | Document | Summary |
|----------|----------|---------|
| **UC-TE-01** | [Trust evaluation base](trust-evaluation-base.md) | Common terminology, trust sources, and ARF requirement mapping |
| **UC-TE-02** | [Wallet Unit evaluates Credential Issuer](wallet-unit-evaluates-credential-issuer.md) | Wallet Unit verifies PID/Attestation Provider before requesting PID or attestation |
| **UC-TE-03** | [Credential Issuer evaluates Wallet Unit](credential-issuer-evaluates-wallet-unit.md) | PID/Attestation Provider verifies Wallet Unit (WUA) before issuing |
| **UC-TE-04** | [Wallet Unit evaluates Relying Party](wallet-unit-evaluates-relying-party.md) | Wallet Unit verifies RP before presentation |
| **UC-TE-05** | [Relying Party evaluates presented credentials](relying-party-evaluates-credentials.md) | RP validates PID and attestation signatures using Trusted Lists |
| **UC-TE-06** | [Trusted List discovery and consumption](trusted-list-discovery-consumption.md) | Obtaining and using LoTL and Trusted Lists for validation |

## Relationship to Other Tasks

- **Task 2** – [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md) (Section 8: Trust Evaluation), [Entities Involved](../../task2-trust-framework/entities-involved.md), [Requirements matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md)
- **Task 3** – [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) for TL format and validation
- **Task 4** – Trust infrastructure APIs for registry and TL access
- **Task 5** – Certificate and policy evaluation (e.g. ETSI policy evaluation)
