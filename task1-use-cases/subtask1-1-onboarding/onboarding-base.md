# Base Onboarding Framework for EUDI Wallet Ecosystem Participants

This document provides only the **common** framework: terminology, MVP/MVP+, and Member State requirements under MVP+. All use-case-specific content (preconditions, success criteria, main flows, administrative/technical/post-onboarding steps, data models, requirements) is **only** in the use case documents below and is **referenced** here.

## Onboarding Use Case Documents

| Use case | Document |
|----------|----------|
| **UC-01** Relying Party | [Relying Party Onboarding](relying_party_onboarding.md) |
| **UC-02** PID / Attestation Provider | [PID / Attestation Provider Onboarding](pid_eaa_provider_onboarding.md) |
| **UC-03** Wallet Provider | [Wallet Provider Onboarding](wallet-provider-onboarding.md) |

## Terminology and Acronyms

All terms, acronyms, entity definitions, WEBUILD-specific entities (Trust Infrastructure Responsible Group, RACI), and MVP/MVP+ definitions are maintained in a single document to avoid duplication:

**→ [Consolidated Terms and Entity Definitions](../terms-and-entities.md)**

That document includes: acronyms; wallet-related and trust infrastructure terminology; trust evaluation terms (Trust evaluation, Trust anchor, Entity status, Certificate/credential revocation); entity types; detailed core trust infrastructure entities (TLP, European Commission, Member States, Registrars, Access CA, Provider of Registration Certificates, CAB, NAB, Supervisory Body, PID Provider, QEAA/PuB-EAA/EAA Providers, Wallet Provider, Relying Party, Intermediary, Attestation Scheme Provider, Authentic Source); WEBUILD Trust Infrastructure Responsible Group; MVP and MVP+ definitions; and policy terms (Authentication, Authorization, Additive/Subtractive policy). RACI definitions and matrices are kept in this document and in the use case documents below.

## MVP and MVP+ Definitions (Onboarding Context)

Onboarding use cases distinguish between two phases. Full definitions are in the [Consolidated Terms and Entity Definitions](../terms-and-entities.md#5-mvp-and-mvp-definitions). Summary:

- **MVP**: WEBUILD testing/pilot phase; WP4 Trust Infrastructure group acts as Ecosystem Authority (and as Registrar, Access CA, Provider of Registration Certificates, TLP); entities register with WP4; registers and Trusted Lists maintained by WP4. LoTL is the trust anchor; see consolidated doc for LoTL/TL model.
- **MVP+**: Production/regulatory phase; registration with Member State Registrars (PID/Attestation Providers, Relying Parties); notification to European Commission (Wallet Providers, Access CAs, Providers of Registration Certificates); trust anchors via Trusted Lists and National Registers per [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).

## RACI Matrix

**RACI** (Responsible, Accountable, Consulted, Informed) is a responsibility assignment matrix used to clarify roles and responsibilities in project management and organizational processes.

**RACI role definitions:**

- **Responsible (R)**: The person or group who do the work and execute the task or deliverable.
- **Accountable (A)**: The person or group who owns the result, makes the final decision, and is ultimately answerable for success or failure.
- **Consulted (C)**: Person or group who are asked for input or expertise and are involved through two-way communication before or during the task.
- **Informed (I)**: People who are kept up to date on progress or outcomes via one-way communication but are not involved in doing or deciding.

The use case documents below ([Relying Party](relying_party_onboarding.md), [PID/EAA Provider](pid_eaa_provider_onboarding.md), [Wallet Provider](wallet-provider-onboarding.md)) each contain their own RACI matrices for onboarding tasks.

### Trust Infrastructure Responsible Group

The entities that perform the Responsible (R) role in the RACI matrices are listed in the [Consolidated Terms and Entity Definitions](../terms-and-entities.md#41-trust-infrastructure-responsible-group).

### Member State requirements under MVP+

Under MVP+, Member States have the following obligations (ref. [Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) and [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md)):

| Requirement | Description | Reference |
|-------------|-------------|-----------|
| **Designate Registrar(s)** | Member States designate at least one Registrar to manage registration and operational authorization of PID Providers, Attestation Providers, and Relying Parties. | ARF Section 3.17; Reg_01 (Topic 27) |
| **National Register(s)** | Member States maintain and publish National Register(s) with information on registered wallet-relying parties (at least Annex I data), in human-readable and machine-processable form, via a single common API and national website; data electronically signed or sealed per Annex II. | Regulation (EU) 2025/848, Article 3, Annex I, Annex II |
| **Registration policies** | Member States adopt registration policies; processes shall be easy to use, electronic, and where possible automated. | Regulation (EU) 2025/848, Articles 4, 5, 6 |
| **Notify European Commission** | Member States notify the European Commission (without undue delay) as required: e.g. body responsible for trusted lists and where they are published (eIDAS Article 22(3)); PID Providers, PuB-EAA Providers, Wallet Providers, Access CAs, Providers of Registration Certificates per GenNot_01. | eIDAS Article 22(3); Trust Infrastructure Schema Section 3.1.1 |
| **Trusted List Provider (MS TLP)** | Member States ensure national Trusted Lists are established, maintained, and published (e.g. QTSP Trusted Lists for QEAA Providers; national TL for non-qualified EAA Providers); MS TLP compiles, signs, and publishes these and submits URLs to the Commission for inclusion in the LoTL. | eIDAS Article 22; Trust Infrastructure Schema Section 3 |
| **Certificate policies** | Member States implement harmonised certificate policies and CPS for WRPAC (and, where applicable, WRPRC) per Annex IV / Annex V. | Regulation (EU) 2025/848, Articles 7, 8, Annex IV, Annex V |

Entity-specific onboarding documents (Relying Party, PID/EAA Provider, Wallet Provider) specify which of these apply to each entity type and reference the Trust Infrastructure Schema for registration vs. notification and Trusted List compilation.

## Success Criteria

See [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md).

## Preconditions

See [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md).

## Main Flows and Steps

Preconditions, main flows, administrative/technical/post-onboarding steps, and industrial-scale considerations are defined in [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md). Registration vs. notification (MVP+): [Trust Infrastructure Schema - Responsibilities Matrix](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).

## Industrial-Scale Considerations

See [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md). Framework-level context: [Task 2 - Trust Framework](../../task2-trust-framework/README.md).

## Administrative, Technical, and Post-Onboarding Steps

Defined only in the use case documents. Shared steps for Relying Parties and PID/EAA Providers: [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md); [Relying Party Onboarding](relying_party_onboarding.md) references those. Wallet Provider steps: [Wallet Provider Onboarding](wallet-provider-onboarding.md).

## Normative References

The following references apply across onboarding use cases. Entity-specific documents may add further references.

- **ARF**: [EUDI Wallet Architecture and Reference Framework 2.7.3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/), [Annex II - High-Level Requirements](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/)
- **Project**: [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md), [Trust Framework](../../task2-trust-framework/README.md), [Entities Involved](../../task2-trust-framework/entities-involved.md), [X.509 PKI / ETSI](../../task3-x509-pki-etsi/README.md), [Onboarding API](../../task4-trust-infrastructure-api/onboarding-api/README.md), [Participants' Certificates and Policies](../../task5-participants-certificates-policies/README.md)
- **Regulations**: [Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848), [Regulation (EU) 2024/2980 Art. 4](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202402980), [Regulation (EU) 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj), [Regulation (EU) 2024/1183 Art. 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj), [Regulation (EU) 2025/849](https://data.europa.eu/eli/reg_impl/2025/849/oj)
- **EC specs**: [EC TS02](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md), [EC TS03](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md), [EC TS05](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md), [EC TS06](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md)
- **ETSI**: TS 119 612, TS 119 602, TS 119 411-8, TS 119 475, TS 119 472-2, EN 319 411-1, EN 319 412-2/3/6 (IETF standards are referenced where applicable in ETSI and ARF)

For entity-specific and full citations, see [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md).
