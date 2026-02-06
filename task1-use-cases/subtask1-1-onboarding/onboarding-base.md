# Base Onboarding Framework for EUDI Wallet Ecosystem Participants

This document provides only the **common** framework: terminology, MVP/MVP+, and Member State requirements under MVP+. All use-case-specific content (preconditions, success criteria, main flows, administrative/technical/post-onboarding steps, data models, requirements) is **only** in the use case documents below and is **referenced** here.

## Onboarding Use Case Documents

| Use case | Document |
|----------|----------|
| **UC-01** Relying Party | [Relying Party Onboarding](relying_party_onboarding.md) |
| **UC-02** PID / Attestation Provider | [PID / Attestation Provider Onboarding](pid_eaa_provider_onboarding.md) |
| **UC-03** Wallet Provider | [Wallet Provider Onboarding](wallet-provider-onboarding.md) |

## Terminology and Acronyms

This section consolidates terminology and acronyms used across onboarding use cases, aligned with the [EUDI Wallet Architecture and Reference Framework (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/).

### Acronyms

| Acronym | Meaning | Source |
|---------|---------|--------|
| **ARF** | Architecture and Reference Framework (EUDI Wallet) | ARF |
| **CA** | Certificate Authority | ARF |
| **EC** | European Commission | ARF |
| **EUDI** | European Digital Identity | ARF |
| **EUDIW** | European Digital Identity Wallet | Regulation (EU) 2024/1183 |
| **LoTL** | List of Trusted Lists | ARF, ETSI TS 119 612 |
| **MS** | Member State | ARF |
| **MS TLP** | Member State Trusted List Provider | ARF |
| **PID** | Person Identification Data | ARF |
| **QTSP** | Qualified Trust Service Provider (under eIDAS) | eIDAS Regulation |
| **RP** | Relying Party | ARF |
| **TL** | Trusted List | ARF |
| **TLP** | Trusted List Provider | ARF |
| **WP** | Wallet Provider | ARF |

### Key Terminology

#### Wallet-Related Terms (per Regulation (EU) 2024/1183)

- **wallet solution**: A combination of software, hardware, services, settings, and configurations, including wallet instances, one or more wallet secure cryptographic applications and one or more wallet secure cryptographic devices
- **wallet instance**: The application installed and configured on a wallet user's device or environment, which is part of a wallet unit, and that the wallet user uses to interact with the wallet unit
- **wallet unit**: A unique configuration of a wallet solution that includes wallet instances, wallet secure cryptographic applications and wallet secure cryptographic devices provided by a wallet provider to an individual wallet user
- **wallet provider**: A natural or legal person who provides wallet solutions

#### Trust Infrastructure Entities (per ARF)

- **Registrar**: Established by Member States to manage the registration and operational authorization of PID Providers, Attestation Providers, and Relying Parties (ARF Section 3.17)
- **Access Certificate Authority**: Issues access certificates to registered entities (PID Providers, Attestation Providers, Relying Parties) for authentication during service interactions (ARF Section 3.18)
- **Provider of Registration Certificates**: Optionally issues certificates detailing entitlements for registered entities (ARF Section 3.19)
- **Trusted List Provider (TLP)**: A body responsible for maintaining, managing, and publishing a Trusted List (ARF Section 3.5)
- **Member State Trusted List Provider (MS TLP)**: Compiles, signs, and publishes national Trusted Lists for non-qualified EAA Providers and Member State QTSP Trusted Lists for QEAA Providers

#### Entity Types

- **PID Provider**: Provider issuing Person Identification Data to Wallet Units
- **Attestation Provider**: Provider issuing electronic attestations of attributes (includes QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers)
- **QEAA Provider**: Qualified Electronic Attestation of Attributes Provider (a Qualified Trust Service Provider under eIDAS)
- **PuB-EAA Provider**: Public Sector Body Electronic Attestation of Attributes Provider
- **EAA Provider**: non-qualified Electronic Attestation of Attributes Provider
- **Relying Party (RP)**: Service that requests attributes from Wallet Units to provide services to users
- **Wallet Provider (WP)**: Natural or legal person who provides wallet solutions

#### Trust Infrastructure Terms

- **Trusted List (TL)**: A list containing trust anchors for validation purposes, published by Trusted List Providers
- **List of Trusted Lists (LoTL)**: Maintained by the European Commission, contains pointers to all published Trusted Lists (ETSI TS 119 612 D.5)
- **Registry**: Publicly accessible register maintained by Registrars containing registration information about entities
- **Access Certificate**: Certificate issued by Access Certificate Authority to registered entities for authentication
- **Registration Certificate**: Optional certificate issued by Provider of Registration Certificates detailing entity entitlements

For additional entity definitions, see [Task 2 - Entities Involved](../task2-trust-framework/entities-involved.md).

### WEBUILD-Specific Entities

#### Trust Infrastructure Responsible Group

The **Trust Infrastructure Responsible Group** is a designated group within the WEBUILD WP4 Trust Infrastructure group that performs the Responsible (R) role in RACI matrices for onboarding processes during the WEBUILD MVP phase. This group is responsible for executing tasks and deliverables related to trust infrastructure operations, including but not limited to:

- Managing onboarding requests and data collection
- Reviewing entity data and making recommendations
- Maintaining and updating Trusted Lists
- Hosting Trusted Lists
- Engaging with entities during onboarding and troubleshooting

The following table lists the entities that are part of the Trust Infrastructure Responsible Group:

| Entity | Legal Name | Website | Administrative Contact | Technical Contact |
|--------|------------|---------|----------------------|-------------------|
| IDunion SCE | GER-IDunion SCE | [https://www.idunion.eu](https://www.idunion.eu) | [info@idunion.eu](mailto:info@idunion.eu) | [info@idunion.eu](mailto:info@idunion.eu) |
| Forkbomb | Forkbomb BV | [https://forkbomb.eu](https://forkbomb.eu) | [info@forkbomb.eu](mailto:info@forkbomb.eu) | [info@forkbomb.eu](mailto:info@forkbomb.eu) |
| Department for digital transformation | Department for digital transformation | [https://innovazione.gov.it](https://innovazione.gov.it) | [g.messori@innovazione.gov.it](mailto:g.messori@innovazione.gov.it) | [gi.demarco@innovazione.gov.it](mailto:gi.demarco@innovazione.gov.it) |

**Note**: Additional entities may be added to this group as designated by the WP4 Trust Infrastructure group. Consortium participants can propose theirselves applying a Pull Request to add themselves to the list and be actively involved in the registration operations and review processes.

#### RACI Matrix

**RACI** (Responsible, Accountable, Consulted, Informed) is a responsibility assignment matrix used to clarify roles and responsibilities in project management and organizational processes.

**RACI Role Definitions:**

- **Responsible (R)**: The person or group who do the work and execute the task or deliverable.
- **Accountable (A)**: The person or group who owns the result, makes the final decision, and is ultimately answerable for success or failure.
- **Consulted (C)**: Person or group who are asked for input or expertise and are involved through two‑way communication before or during the task.
- **Informed (I)**: People who are kept up to date on progress or outcomes via one‑way communication but are not involved in doing or deciding.

## MVP and MVP+ Definitions

Onboarding use cases distinguish between two phases. Entity-specific onboarding documents (Relying Party, PID/EAA Provider, Wallet Provider) reference these definitions and do not duplicate them.

### MVP

**MVP** (Minimum Viable Product) refers to the WEBUILD testing/pilot phase:

- The WP4 Trust Infrastructure group acts as **Ecosystem Authority** (and, where applicable, as Registrar, Access Certificate Authority, Provider of Registration Certificates, and Trusted List Provider).
- All participating entities (Relying Parties, PID/EAA Providers, Wallet Providers) **register** with the WEBUILD WP4 Trust Infrastructure group for the purposes of the pilot.
- Registers and Trusted Lists are maintained by the WP4 Trust Infrastructure group for WEBUILD testing.

### MVP+

**MVP+** refers to the production/regulatory phase aligned with EU regulations and Member State implementations:

- Registration and notification follow the [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).
- **Registration**: PID Providers, Attestation Providers, and Relying Parties register with **Member State Registrars**.
- **Notification**: Wallet Providers, Access Certificate Authorities, and Providers of Registration Certificates are **notified** by Member States to the European Commission (they do not register with Registrars).
- Trust anchors are published via Trusted Lists and National Registers as defined in the Trust Infrastructure Schema.

### Member State requirements under MVP+

Under MVP+, Member States have the following obligations (ref. [Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) and [Trust Infrastructure Schema](../task2-trust-framework/trust-infrastructure-schema.md)):

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

Preconditions, main flows, administrative/technical/post-onboarding steps, and industrial-scale considerations are defined in [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md). Registration vs. notification (MVP+): [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).

## Industrial-Scale Considerations

See [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md). Framework-level context: [Task 2 - Trust Framework](../task2-trust-framework/README.md).

## Administrative, Technical, and Post-Onboarding Steps

Defined only in the use case documents. Shared steps for Relying Parties and PID/EAA Providers: [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md); [Relying Party Onboarding](relying_party_onboarding.md) references those. Wallet Provider steps: [Wallet Provider Onboarding](wallet-provider-onboarding.md).

## Normative References

The following references apply across onboarding use cases. Entity-specific documents may add further references.

- **ARF**: [EUDI Wallet Architecture and Reference Framework 2.7.3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/), [Annex II - High-Level Requirements](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/)
- **Project**: [Trust Infrastructure Schema](../task2-trust-framework/trust-infrastructure-schema.md), [Trust Framework](../task2-trust-framework/README.md), [Entities Involved](../task2-trust-framework/entities-involved.md), [X.509 PKI / ETSI](../task3-x509-pki-etsi/README.md), [Onboarding API](../task4-trust-infrastructure-api/onboarding-api/README.md), [Participants' Certificates and Policies](../task5-participants-certificates-policies/README.md)
- **Regulations**: [Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848), [Regulation (EU) 2024/2980 Art. 4](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202402980), [Regulation (EU) 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj), [Regulation (EU) 2024/1183 Art. 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj), [Regulation (EU) 2025/849](https://data.europa.eu/eli/reg_impl/2025/849/oj)
- **EC specs**: [EC TS02](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md), [EC TS03](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md), [EC TS05](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md), [EC TS06](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md)
- **ETSI**: TS 119 612, TS 119 602, TS 119 411-8, TS 119 475, TS 119 472-2, EN 319 411-1, EN 319 412-2/3/6 (IETF standards are referenced where applicable in ETSI and ARF)

For entity-specific and full citations, see [Relying Party Onboarding](relying_party_onboarding.md), [PID/EAA Provider Onboarding](pid_eaa_provider_onboarding.md), and [Wallet Provider Onboarding](wallet-provider-onboarding.md).
