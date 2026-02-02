# Base Onboarding Framework for EUDI Wallet Ecosystem Participants

This document provides the common base framework for onboarding processes applicable to Relying Parties, PID Providers, Attestation Providers (QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers), and Wallet Providers in the EUDI Wallet ecosystem. This base document should be referenced by entity-specific onboarding documents to avoid duplication.

## Terminology and Acronyms

This section consolidates terminology and acronyms used across onboarding use cases, aligned with the [EUDI Wallet Architecture and Reference Framework (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/).

### Acronyms

| Acronym | Meaning | Source |
|---------|---------|--------|
| **ARF** | Architecture and Reference Framework (EUDI Wallet) | ARF |
| **CA** | Certificate Authority | ARF |
| **EC** | European Commission | ARF |
| **EAA Provider** | non-qualified Electronic Attestation of Attributes Provider | ARF |
| **EUDI** | European Digital Identity | ARF |
| **EUDIW** | European Digital Identity Wallet | Regulation (EU) 2024/1183 |
| **LoTL** | List of Trusted Lists | ARF, ETSI TS 119 612 |
| **MS** | Member State | ARF |
| **MS TLP** | Member State Trusted List Provider | ARF |
| **PID** | Person Identification Data | ARF |
| **PID Provider** | Provider issuing PIDs | ARF |
| **PuB-EAA Provider** | Public Sector Body Electronic Attestation of Attributes Provider | ARF |
| **QEAA Provider** | Qualified Electronic Attestation of Attributes Provider (a QTSP) | ARF |
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
- **Wallet Provider**: Natural or legal person who provides wallet solutions

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

**Note**: Additional entities may be added to this group as designated by the WP4 Trust Infrastructure group. Consortium participants can propose theirselves applying a Pull Request to add themselves to the list and be actively involved in the registration operations and review processes.

#### RACI Matrix

**RACI** (Responsible, Accountable, Consulted, Informed) is a responsibility assignment matrix used to clarify roles and responsibilities in project management and organizational processes.

**RACI Role Definitions:**

- **Responsible (R)**: The person or group who do the work and execute the task or deliverable. In WEBUILD MVP, this role is performed by the [Trust Infrastructure Responsible Group](#trust-infrastructure-responsible-group), which includes IDunion SCE and other designated entities within the WP4 Trust Infrastructure group.
- **Accountable (A)**: The person or group who owns the result, makes the final decision, and is ultimately answerable for success or failure.
- **Consulted (C)**: Person or group who are asked for input or expertise and are involved through two‑way communication before or during the task.
- **Informed (I)**: People who are kept up to date on progress or outcomes via one‑way communication but are not involved in doing or deciding.

## Common Success Criteria

The following success criteria apply to all participant onboarding processes in the EUDI Wallet ecosystem:

- *Interoperability across Member States*
    - All certificates and attestations are syntactically and semantically harmonised in line with applicable ETSI standards (e.g., ETSI EN 319 411-1 version 1.4.1 (2023-10)) and related IETF RFCs ([RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519), [RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392), [RFC 9162](https://datatracker.ietf.org/doc/html/rfc9162)) (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - Certificates and registration data can be validated cross-border in an automated manner using Trusted Lists as defined in [ETSI TS 119 612 v2.4.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) and [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf). See [ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) for implementation guidance.
- *Secure trust establishment*
    - Each entity's identity and attributes are verifiable via National Registers (for Relying Parties, PID/EAA Providers) or Trusted Lists (for Wallet Providers) and anchored in the EU trust framework (ref. [Regulation (EU) 2024/1183, Article 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)).
    - Continuous monitoring and automatic certificate/attestation revocation mechanisms are implemented and effective within 24 hours of a change request (ref. [Regulation (EU) 2025/848, Article 9(5)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- *Transparency and traceability*
    - All certificate issuances, renewals, and revocations are logged (optionally under RFC 9162 – Certificate Transparency v2.0) and made publicly accessible for validation (ref. [Regulation (EU) 2025/848, Annex IV 3(j), Annex V 3(i)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - Revocation and validity information is provided freely (free of charge), automatically, and reliably (ref. [Regulation (EU) 2025/848, Annex IV 5, Annex V 6](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- *Compliance and accountability*
    - Certificate Policies (CP) and Certification Practice Statements (CPS) follow ETSI EN 319 411-1 version 1.4.1 (2023-10) NCP requirements where applicable (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)). See [ETSI Policy Enumeration](../task5-participants-certificates-policies/etsi-policy-enumeration.md) and [ETSI Policy Evaluation](../task5-participants-certificates-policies/etsi-policy-evaluation.md) for policy specifications and evaluation methods.
    - Each Member State designates appropriate authorities (Registrars for Relying Parties/PID/EAA Providers, Supervisory Bodies for Wallet Providers) and maintains National Registers or Trusted Lists, and communicates changes to the Commission and other Member States (ref. [Regulation (EU) 2025/848, Article 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- *Operational effectiveness*
    - Onboarding is completed through defined processes (administrative + technical for Relying Parties/PID/EAA Providers; certification + listing for Wallet Providers) with measurable outcomes and turnaround times.
    - End-to-end validation succeeds automatically through Trusted List integration (see [Task 3 - ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)).

## Common Preconditions

The following preconditions apply to participant onboarding processes, with entity-specific variations:

### Preconditions for Relying Parties and PID/EAA Providers
- Member State must have established at least one National Register (ref. [Regulation (EU) 2025/848, Article 3 "National registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- Member State must have designated at least one Registrar (ref. [Regulation (EU) 2025/848, Article 3 "National registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- Member State must have authorised at least one Certificate Authority to issue Access Certificates (ref. [Regulation (EU) 2025/848, Article 7 "Wallet-relying party access certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)). See also [ARF "3.18 Access Certificate Authorities"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#318-access-certificate-authorities:~:text=each%20Member%20State.-,3.18%20Access%20Certificate%20Authorities,-Access%20Certificate%20Authorities).
- Member State must have authorised at least one Certificate Authority to issue Registration Certificates (ref. [Regulation (EU) 2025/848, Article 8 "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)). See also [ARF "3.19 Providers of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#319-providers-of-registration-certificates:~:text=3.19-,Providers%20of%20registration%20certificates,-If%20a%20Registrar) and [ARF "6.4.2 Relying Party registration"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#642-relying-party-registration:~:text=6.4.2%20Relying%20Party-,registration,-Figure%2011%20depicts).
- Member State must have published one or more national Registration Policies, including or reusing existing sectoral or national registration policies (ref. [Regulation (EU) 2025/848, Article 4 "Registration policies"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- The European Commission must be notified about the Registrar, the Access Certificate Authority, and the Provider of Registration Certificate (ref. [Regulation (EU) 2024/2980, Article 4 "Notifications by Member States"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202402980&qid=1733300667869)).

### Preconditions for Wallet Providers
- Member State must have designated at least one Supervisory Body responsible for qualifying EUDI wallet providers (ref. [Regulation (EU) 2024/1183, Article 22(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1)).
- Member State must have designated at least one Trusted List Provider (ref. [Regulation (EU) 2024/1183, Article 22(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1)).
- Supervisory Body has delegated the Trusted List Provider to create a national Trusted List for Wallet Providers.
- The European Commission has been notified about the creation of the national Trusted List.
- The European Commission includes national Trusted List in the List of Trusted Lists (LoTL).
- The Wallet Provider was able to successfully certify its wallet solution according to [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj).

## Common Main Flow Structure

All participant onboarding processes follow a structured approach, with entity-specific variations:

> **Registration vs. Notification** (MVP+): The trust infrastructure distinguishes between entities that **register** with Registrars (PID Providers, Attestation Providers, Relying Parties) and entities that are **notified** by Member States to the European Commission without registration (Wallet Providers, Access CAs, Registration Cert Providers). See [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix). For MVP (WEBUILD), all entities register with WEBUILD WP4 Trust Infrastructure group.

### Main Flow for Relying Parties and PID/EAA Providers
**1. Administrative Onboarding**
- 1.1 Registration Application
- 1.2 Registration Review
- 1.3 Registration Confirmation
- 1.4 Publication in the National Register

**2. Technical Onboarding**
- 2.1 Access Certificate Request
- 2.2 Access Certificate Request Review
- 2.3 Access Certificate Issuance
- 2.4 Registration Certificate Request
- 2.5 Registration Certificate Request Review
- 2.6 Registration Certificate Issuance
- *Note: Additional steps (e.g., 2.7 Notification, 2.8 Trusted List Publication) may apply to specific entity types. See [Trust Infrastructure Schema - Registration/Onboarding Process](../task2-trust-framework/trust-infrastructure-schema.md#2-registrationonboarding-process) and [Trust Infrastructure Schema - Trusted List Publication Process](../task2-trust-framework/trust-infrastructure-schema.md#3-trusted-list-publication-process) for entity-specific requirements.*

**3. Post Onboarding**
- 3.1 Registration Monitoring
- 3.2 Registration Update
- 3.3 Registration Suspension / Cancellation
- 3.4 Certificate Revocation

### Main Flow for Wallet Providers
**1. Onboarding Request and Review**
- 1.1 Entity requests onboarding
- 1.2 Authority reviews onboarding request
- 1.3 Authority approves onboarding

**2. Trusted List Publication**
- 2.1 Trusted List is updated
- 2.2 Entity receives notification

**3. Post Onboarding**
- 3.1 Monitoring and verification
- 3.2 Update procedures
- 3.3 Suspension / Removal procedures

## Industrial-Scale Considerations

To support the large-scale onboarding of participants across the EUDI Wallet ecosystem, the registration process must address two critical dimensions:

### 1. Entity Identification and Registry Integration

**Objective**: Efficiently identify and onboard entities, leveraging existing authoritative registries where possible.

**Approaches**:
- **Direct Registration**: Entities register directly with the designated authority (Registrar for Relying Parties/PID/EAA Providers, Supervisory Body for Wallet Providers), providing all required information manually or through automated submission.
- **Registry Import**: Import entity information from existing authoritative registries (e.g., business registries, VAT registries, professional qualification registries, GLEIF for LEI records) to reduce duplication and streamline onboarding.

**Level of Assurance for Existing Registries**:
- Member States must establish criteria for qualifying existing registries as authoritative sources for entity identification.
- Qualification criteria should consider:
  - **Registry Authority**: Legal basis and governance of the source registry.
  - **Data Quality**: Accuracy, completeness, and currency of registry data.
  - **Access Mechanisms**: Availability of machine-readable APIs or data exports.
  - **Identity Verification**: Level of identity proofing and verification performed by the source registry.
  - **Update Frequency**: How frequently registry data is updated and synchronized.
- Qualified registries should be documented in Registration Policies (for Relying Parties/PID/EAA Providers) or Trusted List policies (for Wallet Providers) and made available through the National Register API or Trusted List infrastructure (ref. [Regulation (EU) 2025/848, Article 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).

**Early Binding via Electronic Employee Certificates** (applicable to PID/EAA Providers and Wallet Providers):
- Support for employee or representative electronic certificates (e.g., QSeal/QSign corporate certificates) enables strong early binding between the legal entity and the individual acting on its behalf during onboarding.
- This approach provides cryptographic proof of organisational affiliation and can be complemented with:
  - Electronically signed role-acceptance statements.
  - Domain-validated evidence ensuring explicit confirmation of the individual's mandate.
- This aligns with ETSI EN 319 412-3 and established corporate identity-binding practices (ref. [ETSI EN 319 412-3](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.04.01_60/en_31941203v010401c.pdf)).

**Integration with Authoritative Sources**:
- Optional checks against authoritative registries such as GLEIF (LEI records) enable:
  - Enriched, verified organisational metadata.
  - Improved trust scoring.
  - Automated consistency checks between submitted certificates, policy data, and official entity information.
- Integration with authoritative sources strengthens identity assurance, automates validation steps, and improves interoperability with eIDAS2 and wider trust frameworks.

**Registry Integration Requirements**:
- Automated data import mechanisms from qualified registries.
- Data mapping and transformation to align with applicable requirements (Annex I for Relying Parties/PID/EAA Providers, Trusted List data model for Wallet Providers).
- Validation and verification of imported data against source registries.
- Reconciliation processes for entities already registered in multiple authoritative sources.

### 2. Attribute Authorization Management

**Objective**: Enable efficient and consistent management of credential and attribute authorization requests across Member States and sectors.

**High-Level Approach for Cross-Member State and Cross-Sector Authorization**:

**Credential Catalogues and Taxonomies**:
- **Common Credential Catalogue**: A harmonized catalogue of credential types and attributes available in the EUDI Wallet ecosystem, enabling entities to reference standardized credential and attribute definitions.
- **Attribute Taxonomies**: Hierarchical classification systems for attributes (e.g., identity attributes, professional attributes, qualification attributes) to support consistent authorization policies across sectors.
- **Sectorial Templates**: Pre-configured sets of credentials and attributes aligned with specific sectors (e.g., healthcare, finance, education, public administration) to simplify registration for entities operating in those sectors.

**Authorization Policy Framework**:
- Authorization policies follow the framework defined in [Task 2 - Authentication and Authorization Policy Framework](../task2-trust-framework/authentication-authorization-policy-framework.md), supporting both:
  - **Additive Authorization**: Explicit allow-list model (default deny, explicit allow) for high-security environments.
  - **Subtractive Authorization**: Explicit deny-list model (default allow, explicit deny) for flexible, open ecosystems.
- Policies are expressed through trust marks, registration certificates, or Trusted List entries, enabling automated authorization decisions.

**Cross-Border and Cross-Sector Harmonization**:
- **Harmonized Attribute Definitions**: Common semantic definitions for attributes across Member States to enable cross-border authorization decisions.
- **Mutual Recognition**: Mechanisms for recognizing authorization policies and trust marks across Member States and sectors.
- **Policy Mapping**: Translation mechanisms between sector-specific and national authorization policies to enable interoperability.

**Tools and Mechanisms**:
- **Credential Catalogue APIs**: Machine-readable access to credential and attribute definitions, taxonomies, and sectorial templates.
- **Authorization Policy Templates**: Reusable policy templates for common use cases and sectors.
- **Validation Services**: Automated validation of attribute requests against authorization policies and sectorial requirements.

**Implementation Considerations**:
- These industrial-scale mechanisms are defined at the framework level (see [Task 2 - Trust Framework](../task2-trust-framework/README.md)) and implemented through:
  - Registration Policies (for Relying Parties/PID/EAA Providers) (ref. [Regulation (EU) 2025/848, Article 4](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
  - Registration Certificates containing authorization information (for Relying Parties/PID/EAA Providers) (ref. [Regulation (EU) 2025/848, Article 8](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
  - Trust marks expressing authorization semantics (see [Task 2 - Authentication and Authorization Policy Framework](../task2-trust-framework/authentication-authorization-policy-framework.md)).
  - Trusted List entries (for Wallet Providers) containing trust anchor information.
- Detailed specifications for credential catalogues, taxonomies, and sectorial templates are defined in Task 5 (Participants' Certificates and Policies).

## Common Administrative Onboarding Steps (Relying Parties and PID/EAA Providers)

### 1.1 Registration Application

The entity submits the registration application to the Registrar, providing at least the information set out in Annex I. Alternatively, the Registrar may import entity information from qualified authoritative registries (see [Industrial-Scale Considerations - Entity Identification and Registry Integration](#1-entity-identification-and-registry-integration)).

The Registrar receives the registration application (or initiates registry import) for inclusion in the National Register.

*Requirements:*
- [Regulation (EU) 2025/848, Article 3 "National registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)
    - 1. Member States shall make the **information** set out in **Annex I** on registered wallet-relying parties publicly available online, **both in human-readable form and in a form suitable for automated processing.**
    - 5. The information referred to in paragraph 2 shall be available through a single common application programming interface ('**API**') and through a national website. It shall be **electronically signed or sealed** by or on behalf of the registrar, in accordance with the common requirements for a single API set out in Section 1 of **Annex II**.
- [Regulation (EU) 2025/848, Article 4. "Registration policies"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 5. Where appropriate, the requirements set out in the national registration policy shall **not impede an automated registration process.**
- [Regulation (EU) 2025/848, Article 5 "Information to be provided to the national registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_5:~:text=automated%20registration%20process.-,Article%C2%A05,-Information%20to%20be)
    - 1. Wallet-relying parties shall at least provide the **information set out in Annex I to national registers.**
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 1. Registrars shall establish **easy to use electronic, and where possible, automated registration processes** for wallet-relying parties.
- [Regulation (EU) 2025/848, Annex I "Information regarding wallet-relying parties"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)
See also [EC TS06 v1.0 - Common Set of Relying Party Information to be Registered](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md) and [EC TS05 V1.0 - Common Formats and API for Relying Party Registration Information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md)
    - Summary of the information to be provided:
        - official name of the wallet-relying party
        - one or more official identifiers of the wallet-relying party (EORI, LEI, VAT number...)
        - physical address and Member State if not present in official identifier
        - URL belonging to the wallet-relying party where applicable
        - detailed contact information (phone number, website or email)
        - description of the type of services provided
        - a list of the attributes that the wallet-relying party intends to request for each intended use (see [Industrial-Scale Considerations - Attribute Authorization Management](#2-attribute-authorization-management) for credential catalogues, taxonomies, and sectorial templates)
        - a description of intended use of the data
        - indication whether the wallet-relying party is a public sector body
        - applicable entitlement(s) of the wallet-relying party chosen between:
            - Service_Provider
            - QEAA_Provider
            - Non_Q_EAA_Provider
            - PUB_EAA_Provider
            - PID_Provider
            - QCert_for_ESeal_Provider
            - QCert_for_ESig_Provider
            - rQSigCDs_Provider
            - rQSealCDs_Provider
            - ESig_ESeal_Creation_Provider
        - indication if the wallet-relying party intends to act as an intermediary or to rely upon an intermediary.
        - *Entity-specific information (e.g., attestation types for PID/EAA Providers)*
- [Regulation (EU) 2025/848, Annex II "1. Requirements for Electronic signature or seals applied to the information made available on registered Wallet-Relying Parties referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=1.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20FOR%20ELECTRONIC%20SIGNATURES%20OR%20SEALS%20APPLIED%20TO%20THE%20INFORMATION%20MADE%20AVAILABLE%20ON%20REGISTERED%20WALLET%2DRELYING%20PARTIES%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
    - JavaScript Object Notation ('JSON').
    - IETF RFC 7515 for JSON Web Signatures.
- [Regulation (EU) 2025/848, Annex II "2. Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=2.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20ON%20THE%20SINGLE%20COMMON%20API%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
    - (1) The single common API shall:
        - (a) be a **REST API**, supporting **JSON** as a format and signed in accordance with the relevant requirements specified in Section 1;
        - (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying parties, the name of the wallet-relying parties or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14 and 15;
        - (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, current and historic wallet-relying party access certificates and wallet-relying party registration certificates but exclude the contact information in Annex I point 4;
        - (d) be published as an OpenAPI version 3, together with the appropriate documentation and technical specifications ensuring interoperability across the Union;
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    - (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.

### 1.2 Registration Review

The Registrar verifies the registration application.

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 3. Where possible, registrars shall verify in an automated manner:
        - (a) the accuracy, validity, authenticity and integrity of the information required under Article 5.
        - (b) where applicable, the power of attorney of representatives of the wallet-relying parties drawn up and submitted in accordance with the laws and procedures of the Member State where the National Register is established.
        - (c ) the type of entitlement or entitlements of the wallet-relying parties as set out in Annex I.
        - (d) the absence of an existing registration in another National Register.
    - 4. Registrars shall verify the information set out in paragraph 3 against the supporting documentation provided by the wallet-relying parties or against appropriate authentic sources or other official electronic records in the Member State where the National Register is established and to which the registrars have access in accordance with the applicable national laws and procedures.
    - 5. The verification of entitlements of wallet-relying parties referred to in paragraph 3, point (c) shall be carried out in accordance with Annex III.

### 1.3 Registration Confirmation

The Registrar validates or rejects the registration application (the application status becomes "accepted or rejected").

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 6. Where the registrar **cannot verify the information** in accordance with paragraphs 3 to 5, the registrar shall reject the registration.

The entity receives positive or negative feedback on registration application.

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States).
    - 2. Registrars shall process applications for registration **without undue delay and provide a response** to the application for registration to the applicant within the timeframe defined in the applicable registration policy, using appropriate means and in accordance with the laws and procedures of the Member State where the National Register is established.

### 1.4 Publication in the National Register

The Registrar registers the entity in its registry and publishes it.

*Requirements:*
- [ARF "A.2.3.27 Topic 27 - Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=A.2.3.27%20Topic%2027%20%2D%20Registration%20of%20PID%20Providers%2C%20Providers%20of%20QEAAs%2C%20PuB%2DEAAs%2C%20and%20non%2Dqualified%20EAAs%2C%20and%20Relying%20Parties)
    - PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and **Relying Parties register with a Registrar in their Member State**. The main goal of the registration process is for the Registrar to register relevant information about the registering entity, and make this information available online to interested parties.

## Common Technical Onboarding Steps (Relying Parties and PID/EAA Providers)

### 2.1 Access Certificate Request

The Registrar informs the Access Certificate Authority about the registered entity.

The Access Certificate Authority receives the input and starts the review process for the issuing of the Access Certificate.

*Requirements:*
- [Regulation (EU) 2025/848, Article 7. "Wallet-relying party access certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 3. Member States shall implement in a syntactically and semantically harmonised manner the certificate policies and certificate practice statements for the wallet-relying party access certificates, in accordance with the requirements set out in Annex IV.
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 1. The wallet-relying party access certificate policy applicable to the provision of wallet-relying party access certificates shall describe the security requirements that apply to, and the rules that indicate the applicability of, a wallet-relying party access certificate so that wallet-relying parties can be issued with and use those certificates in their interactions with wallet solutions.
    - 2. The wallet-relying party access certificate practice statement applicable to the provision of wallet-relying party access certificates shall describe the practices that a provider of wallet-relying party access certificates employs in issuing, managing, revoking, and re-keying wallet-relying party access certificates.
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates shall be syntactically and semantically harmonised across the Union and shall, as applicable, comply with at least the normalised certificate policy ('NCP') requirements as specified in standard ETSI EN 319 411-1 version 1.4.1 (2023-10) (ref. [Regulation (EU) 2025/848, Annex IV 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).

### 2.2 Access Certificate Request Review

The Access Certificate Authority verifies the identity and any other attributes of the entity.

The Access Certificate Authority checks the valid registration status and information coherency within a National Register in which that entity is established.

*Requirements:*
- [Regulation (EU) 2025/848, Article 7. "Wallet-relying party access certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_5:~:text=Article%C2%A07-,Wallet%2Drelying%20party%20access%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - Member States shall ensure that providers of wallet-relying party access certificates issue wallet-relying party access certificates **exclusively to registered wallet-relying parties** (ref. [Regulation (EU) 2025/848, Article 7](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates [...] shall include:
        - (a) **a clear description of the public key infrastructure hierarchy** and certification paths from the end-entity wallet-relying party access certificates up to the top of the hierarchy used for issuing them, **indicating the expected trust anchor(s)** in such hierarchy and paths which should rely on the trust framework established in accordance with Article 5a(18) of Regulation (EU) No 910/2014.
        - (b) a comprehensive description of the procedures for the issuance of wallet-relying party access certificates, including for the **verification of the identity and any other attributes of the wallet-relying party** to which a wallet-relying party certificate is to be issued.
        - (c ) the obligation for the providers of wallet-relying party access certificates, when issuing a wallet-relying party access certificate, to verify that:
            - the wallet-relying party is included, **with a valid registration status, in a National Register** of wallet-relying parties of the Member State in which that wallet-relying party is established.
            - any information in the wallet-relying party access certificate is accurate and consistent with the registration information available from that register.

### 2.3 Access Certificate Issuance

The Access Certificate Authority issues the Access Certificate and logs the Access Certificate issued.

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates […] shall include:
        - (j) a description, where relevant, on how a provider of wallet-relying party access certificates **logs all wallet-relying party access certificates they have issued**, in compliance with internet engineering task force ('**IETF**') request for comments ('**RFC**') **9162 Certificate Transparency version 2.0**.
        - (k) the obligation for the wallet-relying party access certificates to include:
            - the location where the certificate supporting the advanced electronic signature or advanced electronic seal on that certificate is available, for the entire certification path to be built up to the expected trust anchor in the public key infrastructure hierarchy used by the provider.
            - a machine processable reference to the applicable certificate policy and certificate practice statement.
            - the information referred to in Annex I, points 1, 2, 3, 5, 6 and 7, (a), (b) and (c).
- [ARF "3.18 Access Certificate Authorities"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#318-access-certificate-authorities:~:text=each%20Member%20State.-,3.18%20Access%20Certificate%20Authorities,-Access%20Certificate%20Authorities)
    - Access Certificate Authorities **issue access certificate to all** PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers and **Relying Parties** in the EUDI Wallet ecosystem.

The Registrar keeps records of the issuance of Access Certificates for 10 years and publishes its history within a common REST API (JSON format).

*Requirements:*
- [Regulation (EU) 2025/848, Article 10 "Record keeping"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - Registrars shall keep records of the information provided by wallet-relying parties and registered in accordance with Annex I for the registration of a wallet-relying party and the issuance of the wallet-relying party access certificates and the wallet-relying party registration certificates, and of any subsequent changes to this information, **for 10 years**.
- [Regulation (EU) 2025/848, Annex II "Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - (1) The single common API shall:
        - (a) **be a REST API**, supporting JSON as a format and signed in accordance with the relevant requirements specified in Section 1;
        - (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying party, the name of the wallet-relying party or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14 and 15;
        - (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, current and historic wallet-relying party access certificates and wallet-relying party registration certificates but exclude the contact information in Annex I point 4;
        - (d) be published as an OpenAPI version 3, together with the appropriate documentation and technical specifications ensuring interoperability across the Union;
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    - (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.

### 2.4 Registration Certificate Request

The Registrar informs the Provider of Registration Certificate about the registered entity.

The Provider of Registration Certificate receives the input and starts the review process for the issuing of the Registration Certificate.

*Requirements:*
- [Regulation (EU) 2025/848, Article 8. "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 2. Where a Member State authorised the issuance of a wallet-relying party registration certificate, that Member State shall:
        - (f) implement dedicated certificate policies and certificate practice statements for the wallet-relying party registration certificates in accordance with the requirements set out in Annex V.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 1. The wallet-relying party registration certificate policy applicable to the provision of wallet-relying party registration certificates shall describe the security requirements that apply to, and the rules that indicate the applicability of, a wallet-relying party registration certificate for their issuance to and use by wallet-relying parties in their interactions with wallet solutions. The wallet-relying party registration certificate policy shall be published in **human-readable**.
    - 2. The wallet-relying party registration certificate practice statement applicable to the provisioning of wallet-relying party registration certificates shall describe the practices that a provider of wallet-relying party registration certificates employs in issuing, managing, revoking, and re-keying wallet-relying party registration certificates, and, where applicable, how they relate to wallet-relying party access certificates issued to wallet-relying parties. The wallet-relying party registration certificate practice statement shall be published in **human-readable**.
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates shall be **syntactically and semantically harmonised** across the Union and shall comply with at least the applicable NCP requirements as specified in standard **ETSI EN 319 411-1 version 1.4.1 (2023-10)** (ref. [Regulation (EU) 2025/848, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).

### 2.5 Registration Certificate Request Review

The Provider of Registration Certificate verifies the identity and any other attributes of the entity.

The Provider of Registration Certificate checks the valid registration status and information coherency within a National Register in which that entity is established.

*Requirements:*
- [Regulation (EU) 2025/848, Article 8. "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 2. Where a Member State authorised the issuance of a wallet-relying party registration certificate, that Member State shall:
        - (a) require providers of wallet-relying party registration certificates to issue wallet-relying party registration certificates **exclusively to registered wallet-relying parties**.
        - (b) **ensure that each intended use is expressed** in the wallet-relying party registration certificates.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - The certificate policy and certificate practice statement applicable to the provision of wallet-relying party registration certificates [...] shall include:
        - (a) a **clear description of the public key infrastructure hierarchy** and certification paths from the end-entity wallet-relying party access certificates up to the top of the hierarchy used for issuing them, **indicating the expected trust anchor(s)** in such hierarchy and paths which should rely on the trust framework established in accordance with Article 5a(18) of Regulation (EU) No 910/2014.
        - (b) a comprehensive description of the procedures for the issuance of wallet-relying party registration certificates, including for the **verification of the identity and any other attributes of the wallet-relying party** to which a wallet-relying party certificate is to be issued.
        - (c) the obligation for the provider of wallet-relying party registration certificates, when issuing a wallet-relying party registration certificate, to verify that:
            - the wallet-relying party is included, **with a valid registration status, in a National Register** for wallet-relying parties of the Member State in which that wallet-relying party is established.
            - the **information** in the wallet-relying party registration certificate is accurate and consistent with the registration information available from that register.
            - the wallet-relying party **access certificate is valid**.
            - the description of the procedures for revocation of wallet-relying party registration certificates is comprehensive.

### 2.6 Registration Certificate Issuance

The Provider of Registration Certificate issues the Registration Certificate and logs the Registration Certificate issued.

*Requirements:*
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates [...] shall include:
        - (i) The provider of wallet-relying party registration certificates **logs all wallet-relying party registration certificates they have issued**.
        - (j) the obligation for the wallet-relying party registration certificates:
            - to include the location where the validation data of the advanced electronic signature or advanced electronic seal for the certificate used to sign or seal the registration certificate is available, for the entire trust chain to be built up to the **expected trust anchor**.
            - to include a machine-readable **reference to the applicable certificate policy and certificate practice statement**.
            - to include the **information** referred to in Annex I, points 1, 2, 3, 5, 6 and 8, 9, 10, 11, 12, 13, 14 and 15.
            - to include the **URL to the privacy policy** referred to in Article 8(2)g.
            - to include a **general access policy** as referred to in Article 8(3).
    - 4. The data exchange format for the relying party registration certificate shall be signed **JSON Web Tokens (IETF RFC 7519)** and **CBOR Web Tokens (IETF RFC 8392).**

The Registrar keeps records of the issuance of Registration Certificates for 10 years and publishes its history within a common REST API (JSON format).

*Requirements:*
- [Regulation (EU) 2025/848, Article 10. "Record keeping"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_10:~:text=Article%C2%A010-,Record%20keeping,-Registrars%20shall%20keep)
    - Registrars shall **keep records of the information provided** by wallet-relying parties and registered in accordance with Annex I for the registration of a wallet-relying party and the issuance of the wallet-relying party access certificates and the wallet-relying party registration certificates, and of any subsequent changes to this information, **for 10 years**.
- [Regulation (EU) 2025/848, Annex II. "2. Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=2.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20ON%20THE%20SINGLE%20COMMON%20API%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
    - (1) The single common API shall:
        - (a) be a **REST API**, supporting **JSON** as a format and signed in accordance with the relevant requirements specified in Section 1.
        - (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying party, the name of the wallet-relying party or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14 and 15.
        - (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, **current and historic wallet-relying party access certificates and wallet-relying party registration certificates** but exclude the contact information in Annex I point 4.
        - (d) be published as an **OpenAPI version 3**, together with the appropriate documentation and technical specifications ensuring interoperability across the Union.
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    - (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.

## Common Post-Onboarding Steps

### 3.1 Registration Monitoring

The Registrar (for Relying Parties/PID/EAA Providers) or Supervisory Body (for Wallet Providers) monitors continuously.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 2. Registrars may suspend or cancel a registration of a wallet-relying party where the registrars have reasons to believe one of the following:
        - (a) the registration contains **information**, which is **inaccurate**, out of date or misleading.
        - (b) the wallet-relying party is **not compliant** with the registration policy.
        - (c) the wallet-relying party is **requesting more attributes** than they have registered in accordance with Article 5 and Article 6.
        - (d) the wallet-relying party is otherwise **acting in breach of Union or national law** in a manner related to their role as wallet-relying party.

The Provider of Registration Certificate (for Relying Parties/PID/EAA Providers) monitors continuously and automatically.

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates [...] shall include:
        - (e) the obligation for the providers of wallet-relying party access certificates to implement measures and processes on:
            - **continuously monitoring** any changes in the National Register for wallet-relying party in which wallet-relying party to whom they have issued wallet-relying party access certificates are registered.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (d) the obligation for the provider of wallet-relying party registration certificates implements measures and processes on:
          - **continuously monitoring** in an automated manner any changes in the National Register for wallet-relying party in which wallet-relying party to whom they have issued wallet-relying party registration certificates are registered.

### 3.2 Registration Update

When needed, the entity updates information.

The Registrar (for Relying Parties/PID/EAA Providers) or Supervisory Body (for Wallet Providers) receives the updated information.

*Requirements:*
- [Regulation (EU) 2025/848, Article 5. "Information to be provided to the national registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_5:~:text=Information%20to%20be%20provided%20to%20the%20national%20registers)
    - 2. Wallet-relying party shall ensure that the **information provided is accurate** at the time of registration.
    - 3. Wallet-relying party **shall update any information previously registered** in the National Register of wallet-relying parties **without undue delay.**
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (d) the obligation for the provider of wallet-relying party registration certificates implements **measures and processes** on:
            - **reissue the wallet-relying party registration certificate**.

### 3.3 Registration Suspension / Cancellation

If:
- The National Registrar (for Relying Parties/PID/EAA Providers) or Supervisory Body (for Wallet Providers) conducts a proportionality assessment whose results lead to the entity registration suspension or cancellation.
- The entity requests the entity registration cancellation.
- The Supervisory Body requests the entity registration suspension/ cancellation.

Then:
The Registrar (for Relying Parties/PID/EAA Providers) or Supervisory Body (for Wallet Providers) suspends/ revokes the entity registration.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 1. Registrars shall suspend or cancel a registration of a wallet-relying party where such a suspension or cancellation is **requested by a supervisory body** pursuant to Article 46a(4), point (f) of Regulation (EU) No 910/2014.
    - 3. Registrars shall suspend or cancel a registration of a wallet-relying party where the **request for cancellation or suspension is made by the same wallet-relying party.**
    - 4. When considering the suspension or cancellation in accordance with paragraph 2, the registrar shall conduct a **proportionality assessment**, taking into account the impact on the fundamental rights, security and confidentiality of the users in the ecosystem, as well as the severity of the disruption envisaged to be caused by the suspension or cancellation and the associated costs, both for the wallet-relying party and the user. Based on the result of this assessment, **the registrar may suspend or cancel the registration with or without prior notice to the affected wallet-relying party**.
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_6:~:text=Article%C2%A06-,Registration%20processes,-1.%C2%A0%C2%A0%C2%A0Registrars%20shall)
    - 7. When a wallet-relying party **no longer intends to rely upon wallet units** for the provision of public or private services under a specific registration, it shall **notify the relevant registrar without undue delay and request the cancellation of that registration**.

The Registrar (for Relying Parties/PID/EAA Providers) or Supervisory Body (for Wallet Providers) sends notice about the entity registration suspension / revocation.

The entity receives notice of its registration suspension / revocation.

The Access Certificate Authority (for Relying Parties/PID/EAA Providers) receives notice of the entity registration suspension/ revocation.

The Provider of Registration Certificate (for Relying Parties/PID/EAA Providers) receives notice of the entity registration suspension / revocation.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 5. Where the registration of a wallet-relying party is suspended or cancelled, the **registrar shall inform** **the provider of the relevant wallet-relying party access certificates**, the **provider of the relevant wallet-relying party registration certificates**, and the **affected wallet-relying party** of this action **without undue delay and not later than 24 hours after the suspension or cancellation.** This notification shall include **information** on the reasons for the suspension or cancellation and on the available means of **redress or appeal**.

### 3.4 Certificate Revocation

If:
- The Registrar (for Relying Parties/PID/EAA Providers) or Supervisory Body (for Wallet Providers) suspends / cancels the entity registration.
- The entity requests the entity certificate revocation.
- The Supervisory Body requests the entity certificate revocation.
- Data Protection Authority requests the entity certificate revocation.

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates [...] shall include:
        - (g) the obligation for the providers of wallet-relying party access certificates to **allow** relevant stakeholders, including **wallet-relying parties** as regards their own certificates, **competent supervisory bodies** and **data protection authorities**, **to request the revocation** of wallet-relying party access certificates.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (f) the obligation for the provider of wallet-relying party registration certificates to **allow** relevant stakeholders, including **wallet-relying parties** as regards their own certificates, competent **supervisory bodies** and **data protection authorities**, **to request the revocation** of wallet-relying party registration certificates.

Then:
- The Access Certificate Authority (for Relying Parties/PID/EAA Providers) revokes the Access Certificate (without undue delay).
- The Provider of Registration Certificate (for Relying Parties/PID/EAA Providers) revokes the Registration Certificate (without undue delay).
- The Trusted List Provider (for Wallet Providers) updates the Trusted List to reflect revocation.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 6. **The provider of wallet-relying party access certificates** and the **provider of wallet-relying party registration certificates**, shall, where applicable, **revoke without undue delay the wallet-relying party access certificates, and the wallet-relying party registration certificates,** respectively, of the wallet-relying party for which registration has been suspended or cancelled.
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates [...] shall include:
        - (d) a comprehensive description of the **procedures for revocation of wallet-relying party access certificates**.
        - (e) the obligation for the providers of wallet-relying party access certificates to implement **measures and processes** on:
            - **revoking**, when changes require, **any wallet-relying party certificate** that the provider issued to the corresponding wallet-relying party, in particular when the content of the certificate is **no longer accurate and consistent** with the information registered, or **when the registration of the wallet-relying party is suspended or cancelled**.
    - 4. The revocation set out in point 3(g) **shall become effective immediately** upon its publication.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (c) the obligation for the provider of wallet-relying party registration certificates, when issuing a wallet-relying party registration certificate, to verify that:
            - the **description of the procedures for revocation** of wallet-relying party registration certificates is comprehensive.
        - (d) the obligation for the provider of wallet-relying party registration certificates implements **measures and processes** on:
            - **revoking any wallet-relying party registration certificate** that they issued to the corresponding wallet-relying party, when such changes so require, in particular when the content of the certificate is **no longer accurate and consistent** with the information registered, or **when the registration of the wallet-relying party is modified, suspended or cancelled**.
    - 5. The revocation referred to in point 3(g/f) **shall become effective immediately** upon its publication.

- The Access Certificate Authority (for Relying Parties/PID/EAA Providers) publishes the Access Certificate revocation status (within 24 hours).
- The Provider of Registration Certificate (for Relying Parties/PID/EAA Providers) publishes the Registration Certificate revocation status (within 24 hours).
- The Trusted List Provider (for Wallet Providers) publishes the Trusted List update (within 24 hours).

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
            - (h) the obligation for the providers of wallet-relying party access certificates to register all such revocations in its certificate database and **to publish the revocation status of the certificate in a timely manner**, and in any event **within 24 hours after** receipt of the revocation request.
            - (i) the obligation for the providers of wallet-relying party access certificates to provide **information on the validity or revocation status** of wallet-relying party certificates issued by that provider.
    - 6. The information set out in point 3(h) shall be made available at least on a per certificate basis at any time and at least beyond the validity period of the certificate in an **automated manner** that is reliable, **free of charge** and effectively in accordance with the certificate policy.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
            - (g) the obligation for the provider of wallet-relying party registration certificates to register all such revocations in its certificate database and **to publish the revocation status of the certificate in a timely manner**, and in any event **within 24 hours after** the receipt of the request for revocation.
            - (h) the obligation for the providers of wallet-relying party registration certificates to provide **information on the validity or revocation status** of wallet-relying party registration certificates issued by that provider.
    - 6. The information referred to in point 3(h/g) shall be made available at least on a per certificate basis at any time and at least beyond the validity period of the certificate in an **automated manner** that is reliable, **free of charge** and effectively in accordance with the certificate policy.

---

## Common Normative References

This section provides the common normative references applicable to all participant onboarding processes, including entity-specific references. Entity-specific onboarding documents should reference this section.

### Architecture and Reference Framework (ARF)
- **ARF Version**: 2.7.3
- **ARF Main Document**: [EUDI Wallet Architecture and Reference Framework 2.7.3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/)
- **ARF Annex II - High-Level Requirements**: [Annex II - High-Level Requirements](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/)

### Project-Specific References
- **Task 2 - Trust Infrastructure Schema**: See [Trust Infrastructure Schema](../task2-trust-framework/trust-infrastructure-schema.md) for the overall architecture, registration vs. notification processes, trusted list compilation responsibilities, and the relationship between registration and trusted list publication
- **Task 2 - Trust Framework**: See [Trust Framework documentation](../task2-trust-framework/README.md) for trust evaluation, trust management, and policy framework definitions
- **Task 2 - Entities Involved**: See [Entities Involved in Trust Evaluation](../task2-trust-framework/entities-involved.md) for definitions of Trusted List Provider, Access Certificate Authority, Provider of Registration Certificates, and other trust infrastructure entities
- **Task 3 - X.509 PKI with ETSI Alignments**: See [X.509 PKI documentation](../task3-x509-pki-etsi/README.md) for certificate management, ETSI compliance, and trusted lists implementation. See [ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) for detailed trusted list implementation guidance
- **Task 4 - Trust Infrastructure APIs**: See [Onboarding API](../task4-trust-infrastructure-api/onboarding-api/README.md) for participant registration and certificate management API specifications
- **Task 5 - Participants' Certificates and Policies**: See [Participants' Certificates and Policies](../task5-participants-certificates-policies/README.md) for certificate and policy data models, trust evaluation methods, and ETSI policy application mechanisms. See [ETSI Policy Enumeration](../task5-participants-certificates-policies/etsi-policy-enumeration.md) and [ETSI Policy Evaluation](../task5-participants-certificates-policies/etsi-policy-evaluation.md) for policy specifications and evaluation methods

### Implementing Acts (IAs)
- **Regulation (EU) 2025/848**: [Commission Implementing Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)
- **Regulation (EU) 2024/2980**: [Commission Implementing Regulation (EU) 2024/2980, Article 4 "Notifications by Member States"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202402980&qid=1733300667869)
- **Regulation (EU) 2024/2981**: [Commission Implementing Regulation (EU) 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj) - Wallet certification requirements
- **Regulation (EU) 2024/1183**: [Regulation (EU) 2024/1183, Article 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- **Regulation (EU) 2025/849**: [Commission Implementing Regulation (EU) 2025/849](https://data.europa.eu/eli/reg_impl/2025/849/oj) - Wallet solution reference identifiers

### European Commission Technical Specifications
- **EC TS02 v0.9** (2025-04): [Specification of systems enabling the notification and subsequent publication of Provider information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md)
- **EC TS03**: [Wallet Unit Attestation](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md)
- **EC TS05 V1.0** (2025-06): [Common Formats and API for Relying Party Registration Information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md)
- **EC TS06 v1.0** (2025-06): [Common Set of Relying Party Information to be Registered](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md)
- **EUDI Wallet Essential Standards and Technical Specifications (STS)**: [Essential Standards and Technical Specifications (STS)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/technical-specifications/#:~:text=Essential%20Standards%20and%20Technical%20Specifications%20(STS))

### ETSI Standards
- **ETSI TS 119 612** (v2.4.1): [Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) - See [ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) for implementation guidance
- **ETSI TS 119 602** (v1.1.1): [Electronic Signatures and Trust Infrastructures (ESI); Trusted lists; Data model. Trusted lists in other formats, such as JSON, CBOR or ASN.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf) - See [ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) for implementation guidance
- **ETSI TS 119 411-8** (v01.01.01): [Access Certificate Policy for EUDI Wallet Relying Parties](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf)
- **ETSI TS 119 475** (v01.01.01): [Relying party attributes supporting EUDI Wallet User's authorisation decisions (Relying Party Attributes)](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.01.01_60/ts_119475v010101p.pdf)
- **ETSI TS 119 472-2** (v1.1.1): [Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 2: Profiles for EAA/PID Presentations to Relying Party](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.01.01_60/ts_11947202v010101p.pdf)
- **ETSI EN 319 411-1**: Version 1.4.1 (2023-10) - Normalised Certificate Policy (NCP) requirements
- **ETSI EN 319 412-2**: [Certificate Profiles; Part 2: Certificate Profile for Legal Persons](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.03.01_60/en_31941202v020301p.pdf)
- **ETSI EN 319 412-3**: [Certificate Profiles; Part 3: Certificate Profile for Natural Persons](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.04.01_60/en_31941203v010401c.pdf) - Corporate identity-binding practices
- **ETSI EN 319 412-6** (v01.00.00): [Certificate profile requirements for PID, Wallet, EAA, QEAA and PSBEAA providers](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf)

### IETF Standards
- **IETF RFC 5280**: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
- **IETF RFC 5914**: Trust Anchor Format
- **IETF RFC 3647**: Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework
- **IETF RFC 5755**: An Internet Attribute Certificate Profile for Authorization
- **IETF RFC 7515**: JSON Web Signature (JWS)
- **IETF RFC 7519**: JSON Web Token (JWT)
- **IETF RFC 8392**: CBOR Web Token (CWT)
- **IETF RFC 9162**: Certificate Transparency Version 2.0
- **IETF Draft OAuth Status List**: [OAuth 2.0 Token Status List](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-status-list-12) - For Wallet Unit Attestation status lists
