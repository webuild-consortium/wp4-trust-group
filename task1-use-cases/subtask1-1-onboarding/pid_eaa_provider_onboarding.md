# Use Case: UC-02 PID / Attestation Provider Onboarding

**Note**: This document describes the PID / Attestation Provider onboarding process. For common onboarding framework elements shared with Relying Parties and Wallet Providers, see [Base Onboarding Framework](onboarding-base.md).

**Note on MVP/MVP+ Structure**: This document follows the WEBUILD ecosystem structure, distinguishing between:
- **[MVP]**: WEBUILD testing/pilot phase requirements, where the WP4 Trust Infrastructure group acts as Ecosystem Authority
- **[MVP+]**: Production/regulatory phase requirements, aligned with EU regulations and Member State implementations

## Basic Information
- **Use Case ID**: UC-02
- **Title**: PID / Attestation Provider Onboarding
- **Category**: Onboarding
- **Priority**: [High | Medium | Low]
- **Complexity**: [Simple | Medium | Complex]
- **Version**: 1.0
- **Last Updated**: 22/10/2025

## Actors

- **Primary Actor [MVP]**:
    - Beneficiaries and Associated Partners providing PID or Attestation services within WEBUILD
- **Secondary Actors [MVP]**:
    - Ecosystem Authority: WEBUILD WP4 Trust Infrastructure group
    - Access Certificate Authority: WEBUILD WP4 Trust Infrastructure group
    - Provider of Registration Certificate: WEBUILD WP4 Trust Infrastructure group
    - Trusted List Provider: WEBUILD WP4 Trust Infrastructure group
    - Please note: The Trust Infrastructure group is not a legal entity. However, the ecosystem authority may be required to provide certain information (e.g., legal name, company address) and to digitally sign data. For testing purposes, we therefore recommend designating at least one representative of the Trust Infrastructure group who is authorized to perform digital signing on behalf of the legal entity they represent.

- **Primary Actor [MVP+]**:
    - PID Provider (legal or natural person) that intends to issue person identification data interoperable with EUDI Wallets
    - Attestation Provider (QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider) that intends to issue electronic attestations of attributes interoperable with EUDI Wallets
- **Secondary Actors [MVP+]**:
    - Registrar (designated by Member State)
    - Access Certificate Authority (authorized by Member State)
    - Provider of Registration Certificate (authorized by Member State)
    - Trusted List Provider (designated by Member State)

## Goal

- **Technical Goal [MVP]**: To establish an onboarding process for PID / Attestation Providers within WEBUILD, enabling trusted interaction between EUDI Wallet Units and PID / Attestation Providers in the testing environment.

- **Business Goal [MVP+]**: To register PID / Attestation Providers that intend to issue person identification data or electronic attestations of attributes interoperable with EUDI Wallets (ref. [Regulation (EU) 2025/848, Recital 1](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- **Technical Goal [MVP+]**: To establish a harmonised, secure, and interoperable framework for the registration, certification, and lifecycle management of PID / Attestation Providers, enabling trusted interaction between EUDI Wallet Solutions and other parties involved.

- **Success Criteria**:
    - [MVP] Pilot implementations successfully demonstrate PID / Attestation Provider onboarding within WEBUILD
    - [MVP] All PID / Attestation Providers within WEBUILD are included in a publicly accessible register and Trusted List maintained by the WP4 Trust Infrastructure group
    - [MVP+] The onboarding process for PID / Attestation Providers is formally defined and documented in a harmonized manner that aligns with EU regulatory and technical frameworks (ref. [Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848))
    - [MVP+] See [Common Success Criteria](onboarding-base.md#common-success-criteria) in the base document for additional criteria
    - Additional entity-specific success criteria:
    - *Interoperability across Member States*
        - All PID / Attestation Providers Access and Registration Certificates are syntactically and semantically harmonised in line with ETSI EN 319 411-1 version 1.4.1 (2023-10) and related IETF RFCs ([RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519), [RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392), [RFC 9162](https://datatracker.ietf.org/doc/html/rfc9162)) (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
        - Certificates and registration data can be validated cross-border in an automated manner using Trusted Lists as defined in [ETSI TS 119 612 v2.4.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) and [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).
    - *Secure trust establishment*
        - Each PID / Attestation Providers’s identity and attributes are verifiable via National Registers and anchored in the EU trust framework (ref. [Regulation (EU) 2024/1183, Article 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)).
        - Continuous monitoring and automatic Access and Registration Certificate revocation mechanisms are implemented and effective within 24 hours of a change request (ref. [Regulation (EU) 2025/848, Article 9(5)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - *Transparency and traceability*
        - All Certificate issuances, renewals, and revocations are logged (optionally under RFC 9162 – Certificate Transparency v2.0) and made publicly accessible for validation (ref. [Regulation (EU) 2025/848, Annex IV 3(j), Annex V 3(i)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
        - Revocation and validity information is provided freely (free of charge), automatically, and reliably (ref. [Regulation (EU) 2025/848, Annex IV 5, Annex V 6](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - *Compliance and accountability*
        - Certificate Policies (CP) and Certification Practice Statements (CPS) follow ETSI EN 319 411-1 version 1.4.1 (2023-10) NCP requirements (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
        - Each Member State designates at least one Registrar and maintains at least one National Register and communicates changes to the Commission and other Member States (ref. [Regulation (EU) 2025/848, Article 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - *Operational effectiveness*
        - Onboarding of new PID / Attestation Providers is completed through a dual-phase process (administrative + technical) with measurable outcomes and turnaround times.
        - End-to-end validation of Access and Registration Certificates succeeds automatically through Trusted List integration (see [Task 3 - ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)).

## Preconditions

See [Common Preconditions](onboarding-base.md#common-preconditions) in the base document for common preconditions applicable to all participants.

### Preconditions [MVP]
- The WEBUILD WP4 Trust Infrastructure group has established a register for PID / Attestation Providers within WEBUILD.
- The WEBUILD WP4 Trust Infrastructure group has established a Trusted List for PID / Attestation Providers within WEBUILD.
- The WEBUILD WP4 Trust Infrastructure group has designated representatives authorized to act as Ecosystem Authority, Access Certificate Authority, Provider of Registration Certificate, and Trusted List Provider.
- The WEBUILD WP4 Trust Infrastructure group has published registration policies for the WEBUILD testing environment.

### Preconditions [MVP+]
- See [Preconditions for Relying Parties and PID/EAA Providers](onboarding-base.md#preconditions-for-relying-parties-and-pideaa-providers) in the base document.
- Member State must have established a Trusted List for PID / Attestation Providers (for PID Providers, QEAA Providers, PuB-EAA Providers).

## Main Flow

See [Common Main Flow Structure](onboarding-base.md#common-main-flow-structure) in the base document for the overall flow structure.

**Note**: The detailed steps below apply to both [MVP] and [MVP+] phases, with specific procedures and requirements differentiated where applicable.

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
- 2.7 Notification to EU Commission and other Member States [MVP+ only]
- 2.8 Publication in Trusted List

**3. Post Onboarding**
- 3.1 Registration Monitoring
- 3.2 Registration Update
- 3.3 Registration Suspension / Cancellation
- 3.4 Access / Registration Certificate Revocation

## Industrial-Scale Considerations

See [Industrial-Scale Considerations](onboarding-base.md#industrial-scale-considerations) in the base document for common approaches to entity identification, registry integration, and attribute authorization management.

To support the large-scale onboarding of PID / Attestation Providers across the EUDI Wallet ecosystem, the registration process must address two critical dimensions:

### 1. Entity Identification and Registry Integration

**Objective**: Efficiently identify and onboard entities, leveraging existing authoritative registries where possible.

**Approaches**:
- **Direct Registration**: Entities register directly with the National Registrar, providing all required information manually or through automated submission.
- **Registry Import**: Import entity information from existing authoritative registries (e.g., business registries, VAT registries, professional qualification registries, GLEIF for LEI records) to reduce duplication and streamline onboarding.

**Level of Assurance for Existing Registries**:
- Member States must establish criteria for qualifying existing registries as authoritative sources for entity identification.
- Qualification criteria should consider:
  - **Registry Authority**: Legal basis and governance of the source registry.
  - **Data Quality**: Accuracy, completeness, and currency of registry data.
  - **Access Mechanisms**: Availability of machine-readable APIs or data exports.
  - **Identity Verification**: Level of identity proofing and verification performed by the source registry.
  - **Update Frequency**: How frequently registry data is updated and synchronized.
- Qualified registries should be documented in Registration Policies and made available through the National Register API (ref. [Regulation (EU) 2025/848, Article 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).

**Early Binding via Electronic Employee Certificates**:
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
- Data mapping and transformation to align with Annex I requirements.
- Validation and verification of imported data against source registries.
- Reconciliation processes for entities already registered in multiple authoritative sources.

### 2. Attribute Authorization Management

**Objective**: Enable efficient and consistent management of credential and attribute authorization requests across Member States and sectors.

**High-Level Approach for Cross-Member State and Cross-Sector Authorization**:

**Credential Catalogues and Taxonomies**:
- **Common Credential Catalogue**: A harmonized catalogue of credential types and attributes available in the EUDI Wallet ecosystem, enabling PID / Attestation Providers to reference standardized credential and attribute definitions.
- **Attribute Taxonomies**: Hierarchical classification systems for attributes (e.g., identity attributes, professional attributes, qualification attributes) to support consistent authorization policies across sectors.
- **Sectorial Templates**: Pre-configured sets of credentials and attributes aligned with specific sectors (e.g., healthcare, finance, education, public administration) to simplify registration for Providers operating in those sectors.

**Authorization Policy Framework**:
- Authorization policies follow the framework defined in [Task 2 - Authentication and Authorization Policy Framework](../task2-trust-framework/authentication-authorization-policy-framework.md), supporting both:
  - **Additive Authorization**: Explicit allow-list model (default deny, explicit allow) for high-security environments.
  - **Subtractive Authorization**: Explicit deny-list model (default allow, explicit deny) for flexible, open ecosystems.
- Policies are expressed through trust marks and registration certificates, enabling automated authorization decisions.

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
  - Registration Policies (ref. [Regulation (EU) 2025/848, Article 4](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
  - Registration Certificates containing authorization information (ref. [Regulation (EU) 2025/848, Article 8](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
  - Trust marks expressing authorization semantics (see [Task 2 - Authentication and Authorization Policy Framework](../task2-trust-framework/authentication-authorization-policy-framework.md)).
- Detailed specifications for credential catalogues, taxonomies, and sectorial templates are defined in Task 5 (Participants' Certificates and Policies).

## 1. Administrative Onboarding

Each PID / Attestation Provider that intends to issue person identification data or electronic attestations of attributes interoperable with EUDI Wallets will register itself with a designated Registrar in its Member State. Registration may occur through direct submission or via import from qualified authoritative registries (see [Industrial-Scale Considerations](onboarding-base.md#industrial-scale-considerations)). If the registration process is successful, the Registrar includes the PID / Attestation Provider in its public registry.

*Preconditions:*
- **Prerequisites [MVP]**:
    - The WEBUILD WP4 Trust Infrastructure group has established a register for PID / Attestation Providers within WEBUILD.
    - The WEBUILD WP4 Trust Infrastructure group has designated representatives authorized to act as Registrar.
    - The WEBUILD WP4 Trust Infrastructure group has published registration policies for the WEBUILD testing environment.
- **Prerequisites [MVP+]**:
    - Its Member State has established at least one National Register of PID / Attestation Providers.
    - Its Member State has designated at least one Registrar of PID / Attestation Providers.
    - Its Member State has published one or more national Registration Policies.
    - The European Commission has been notified about the Registrar and the National Register.
- **Triggers**: 
    - The PID / Attestation Provider, that intends to issue person identification data or electronic attestations of attributes interoperable with EUDI Wallets decides to submit a registration application.
    
*Postconditions:*
- **Success**: 
    - The Registrar accepts the PID / Attestation Provider registration application.
    - The Registrar publishes the Provider’s information in its public registry of registered PID and Attestation Providers.
- **Failure**: 
    - The Registrar rejects the PID / Attestation Provider registration application and informs the PID / Attestation Provider.
- **Outputs**: 
    - The PID / Attestation Provider is considered administratively registered.
    - The PID / Attestation Provider can proceed to Technical Onboarding to obtain one or more Access Certificate(s) and one or more Registration Certificate(s).

### 1.1 Registration Application

**For [MVP]**: The PID / Attestation Provider (Beneficiary or Associated Partner) submits the registration application to the WEBUILD WP4 Trust Infrastructure group, providing required information for WEBUILD testing purposes. The application includes:
- Entity identification and contact information
- Attestation type(s) that the Provider intends to issue (e.g., QEAA, PuB-EAA, non-qualified EAA, PID)
- Service description and intended use of EUDI Wallet data
- For QEAA Providers: Qualification evidence
- For PuB-EAA Providers: Public sector body evidence
- For non-qualified EAA Providers: Service provider information

**For [MVP+]**: The PID / Attestation Provider submits the registration application to the Registrar, providing at least the information set out in Annex I. Alternatively, the Registrar may import entity information from qualified authoritative registries (see [Industrial-Scale Considerations - Entity Identification and Registry Integration](onboarding-base.md#1-entity-identification-and-registry-integration)).

The Registrar receives the registration application (or initiates registry import) for inclusion in the National Register.

*Requirements:*
- [Regulation (EU) 2025/848, Article 3 "National registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)
    -   1. Member States shall make the **information** set out in **Annex I** on registered wallet-relying parties publicly available online, **both in human-readable form and in a form suitable for automated processing.** 
    -    5. The information referred to in paragraph 2 shall be available through a single common application programming interface (‘**API**’) and through a national website. It shall be **electronically signed or sealed** by or on behalf of the registrar, in accordance with the common requirements for a single API set out in Section 1 of **Annex II**.
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
        - a list of the attributes that the wallet-relying party intends to request for each intended use
        - a description of intended use of the data
        - indication whether the wallet-relying party is a public sector body
        - applicable entitlement(s) of the wallet-relying party chosen between:
            - Service_Provider
            - **QEAA_Provider**
            - **Non_Q_EAA_Provider**
            - **PUB_EAA_Provider**
            - **PID_Provider**
            - QCert_for_ESeal_Provider
            - QCert_for_ESig_Provider
            - rQSigCDs_Provider
            - rQSealCDs_Provider
            - ESig_ESeal_Creation_Provider
        - indication if the wallet-relying party intends to act as an intermediary or to rely upon an intermediary.
        - the attestation type(s) that the Provider intends to issue to Wallet Units (see [ARF "3.17 Registrars"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#317-registrars:~:text=an%20accreditation%20certificate.-,3.17%20Registrars,-All%20PID%20Providers)).
- [Regulation (EU) 2025/848, Annex II "1.   Requirements for Electronic signature or seals applied to the information made available on registered Wallet-Relying Parties referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=1.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20FOR%20ELECTRONIC%20SIGNATURES%20OR%20SEALS%20APPLIED%20TO%20THE%20INFORMATION%20MADE%20AVAILABLE%20ON%20REGISTERED%20WALLET%2DRELYING%20PARTIES%20REFERRED%20TO%20IN%20ARTICLE%C2%A03) 
    - JavaScript Object Notation (‘JSON’)
    - IETF 7515 for JSON Web Signatures
- [Regulation (EU) 2025/848, Annex II "2.   Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=2.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20ON%20THE%20SINGLE%20COMMON%20API%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
See also [ARF, Annex II - High-Level Requirements "A. General requirements for Member State registration processes"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=A.%20General%20requirements%20for%20Member%20State%20registration%20processes) and ["C. Requirements for the registration of PID Providers"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=C.%20Requirements%20for%20the%20registration%20of%20PID%20Providers) and ["D. Requirements for the registration of Attestation Providers"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=D.%20Requirements%20for%20the%20registration%20of%20Attestation%20Providers).
    - (1) The single common API shall:
        - (a) be a **REST API**, supporting **JSON** as a format and signed in accordance with the relevant requirements specified in Section 1.
        -    (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying parties, the name of the wallet-relying parties or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14 and 15.
        -    (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, current and historic wallet-relying party access certificates and wallet-relying party registration certificates but exclude the contact information in Annex I point 4.
        - (d) be published as an OpenAPI version 3, together with the appropriate documentation and technical specifications ensuring interoperability across the Union.
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    - (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.
- [ARF "A.2.3.27 Topic 27 - Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=A.2.3.27%20Topic%2027%20%2D%20Registration%20of%20PID%20Providers%2C%20Providers%20of%20QEAAs%2C%20PuB%2DEAAs%2C%20and%20non%2Dqualified%20EAAs%2C%20and%20Relying%20Parties)
    - **PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers**, and Relying Parties **register with a Registrar in their Member State**. The main goal of the registration process is for the Registrar to register relevant information about the registering entity, and make this information available online to interested parties.

### 1.2 Registration Review

**For [MVP]**: The WEBUILD WP4 Trust Infrastructure group reviews the registration application, verifying entity information, attestation type(s), and compliance with WEBUILD testing requirements.

**For [MVP+]**: See [Common Administrative Onboarding Steps - 1.2 Registration Review](onboarding-base.md#12-registration-review) in the base document.

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

**For [MVP]**: The WEBUILD WP4 Trust Infrastructure group validates or rejects the registration application and notifies the PID / Attestation Provider of the decision.

**For [MVP+]**: See [Common Administrative Onboarding Steps - 1.3 Registration Confirmation](onboarding-base.md#13-registration-confirmation) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States) 
    - 6. Where the registrar **cannot verify the information** in accordance with paragraphs 3 to 5, the registrar shall reject the registration.

The PID / Attestation Provider receives positive or negative feedback on registration application.

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States).
    - 2. Registrars shall process applications for registration **without undue delay and provide a response** to the application for registration to the applicant within the timeframe defined in the applicable registration policy, using appropriate means and in accordance with the laws and procedures of the Member State where the National Register is established.
  
### 1.4 Publication in the National Register

**For [MVP]**: The WEBUILD WP4 Trust Infrastructure group registers the PID / Attestation Provider in the WEBUILD register, including the attestation type(s) the Provider intends to issue, and makes the information publicly accessible for testing purposes.

**For [MVP+]**: See [Common Administrative Onboarding Steps - 1.4 Publication in the National Register](onboarding-base.md#14-publication-in-the-national-register) in the base document. Additionally, the Registrar registers the attestation type(s) that the Provider intends to issue to Wallet Units (see [ARF "3.17 Registrars"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#317-registrars:~:text=an%20accreditation%20certificate.-,3.17%20Registrars,-All%20PID%20Providers)).

*Requirements:*

- [ARF "3.17 Registrars"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#317-registrars:~:text=an%20accreditation%20certificate.-,3.17%20Registrars,-All%20PID%20Providers)
    - For a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider, the **Registrar registers the attestation type(s) this entity wants to issue to Wallet Units**, for example, diplomas, driving licenses or vehicle registration cards.
- [ARF "6.3.2.2 Data about the PID Provider or Attestation Provider is included in the registry"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification:~:text=the%20next%20subsections.-,6.3.2.2%20DATA%20ABOUT%20THE%20PID%20PROVIDER%20OR%20ATTESTATION%20PROVIDER%20IS%20INCLUDED%20IN%20THE%20REGISTRY,-When%20a%20PID)
See also [ARF, Annex II - High-Level Requirements "A. General requirements for Member State registration processes"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=A.%20General%20requirements%20for%20Member%20State%20registration%20processes), ["C. Requirements for the registration of PID Providers"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=C.%20Requirements%20for%20the%20registration%20of%20PID%20Providers) and ["D. Requirements for the registration of Attestation Providers"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=D.%20Requirements%20for%20the%20registration%20of%20Attestation%20Providers)
   -  When a PID Provider or Attestation Provider is registered, the **Registrar registers a set of data about the PID Provider or Attestation Provider in its register.** The Registrar makes the contents of the register available to the **general public, both in machine-readable and human-readable format.**
   -  The data to be registered about a PID Provider, QEAA Provider, PuB-EAA Provider, or EAA Provider **includes the attestation type(s) that the Provider intends to issue to Wallet Units.** This enables Wallet Units and Relying Parties to verify that a given PID Provider or Attestation Provider registered its intent to issue a specific attestation type. 
   
## 2. Technical Onboarding

As a result of successful registration, each registered PID / Attestation Provider undergoes a technical onboarding process to obtain one or more Access Certificate(s) (which is mandatory and needed to authenticate itself towards a Wallet Unit when issuing a PID or an attestation to it) and one or more Registration Certificate(s) (which confirms the PID / Attestation Provider eligibility to issue person identification data or electronic attestations of attributes interoperable with European Digital Identity Wallets (EUDI Wallets). After certificate issuance, Member State notifies the European Commission and other Member States about the PID / Attestation Provider and the trust anchor of the PID / Attestation Provider gets included in a Trusted List.

*Preconditions:*
- **Prerequisites [MVP]**:
    - The WEBUILD WP4 Trust Infrastructure group has designated representatives authorized to act as Access Certificate Authority, Provider of Registration Certificate, and Trusted List Provider.
    - The PID / Attestation Provider has successfully completed the Administrative Onboarding phase and is listed in the WEBUILD register.
    - A Trusted List for PID / Attestation Providers has been established within WEBUILD.
- **Prerequisites [MVP+]**:
    - Its Member State has authorised at least one Certificate Authority to issue PID / Attestation Provider Access Certificates.
    - Its Member State has authorised at least one Certificate Authority to issue PID / Attestation Provider Registration Certificates.
    - The European Commission has been notified about the Access Certificate Authority and the Provider of Registration Certificate.
    - The PID / Attestation Provider has successfully completed the Administrative Onboarding phase and is listed in a National Register, notified by the Member State to the EU Commission.
    - A Trusted List for PID / Attestation Providers has been established and published.
- **Triggers**:
    - The positive completion of the PID / Attestation Provider registration process.

*Postconditions:*
- **Success**: 
    - The PID / Attestation Provider receives valid Access Certificate and one or more Registration Certificates (if applicable), registered and verifiable through the National Register and the EU trust framework.
    - The PID / Attestation Provider is notified to EU and Member States.
    - The trust anchor of the PID / Attestation Provider is included in a Trusted List.
- **Failure**:
    - The request for Access / Registration Certificate issuance is rejected (e.g. due to inconsistent registry data, failed identity verification, or policy non-compliance).
- **Outputs**:
    - The PID / Attestation Provider is fully onboarded and authorised to interact with EUDI Wallets.

### 2.1 Access Certificate Request

See [Common Technical Onboarding Steps - 2.1 Access Certificate Request](onboarding-base.md#21-access-certificate-request) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Article 7. "Wallet-relying party access certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 3. Member States shall implement in a syntactically and semantically harmonised manner the certificate policies and certificate practice statements for the wallet-relying party access certificates, in accordance with the requirements set out in Annex IV.
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 1. The wallet-relying party access certificate policy applicable to the provision of wallet-relying party access certificates shall describe the security requirements that apply to, and the rules that indicate the applicability of, a wallet-relying party access certificate so that wallet-relying parties can be issued with and use those certificates in their interactions with wallet solutions.
    - 2. The wallet-relying party access certificate practice statement applicable to the provision of wallet-relying party access certificates shall describe the practices that a provider of wallet-relying party access certificates employs in issuing, managing, revoking, and re-keying wallet-relying party access certificates.
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates shall be syntactically and semantically harmonised across the Union and shall, as applicable, comply with at least the normalised certificate policy (‘NCP’) requirements as specified in standard ETSI EN 319411-1 version 1.4.1 (2023-10). 

### 2.2 Access Certificate Request Review

See [Common Technical Onboarding Steps - 2.2 Access Certificate Request Review](onboarding-base.md#22-access-certificate-request-review) in the base document.

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

See [Common Technical Onboarding Steps - 2.3 Access Certificate Issuance](onboarding-base.md#23-access-certificate-issuance) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates […] shall include:
        - (j) a description, where relevant, on how a provider of wallet-relying party access certificates **logs all wallet-relying party access certificates they have issued**, in compliance with internet engineering task force (‘**IETF**’) request for comments (‘**RFC**’) **9162 Certificate Transparency version 2.0**;
        - (k) the obligation for the wallet-relying party access certificates to include:
            - the location where the certificate supporting the advanced electronic signature or advanced electronic seal on that certificate is available, for the entire certification path to be built up to the expected trust anchor in the public key infrastructure hierarchy used by the provider.
            - a machine processable reference to the applicable certificate policy and certificate practice statement.
            - the information referred to in Annex I, points 1, 2, 3, 5, 6 and 7, (a), (b) and (c).

- [ARF "3.18 Access Certificate Authorities"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#318-access-certificate-authorities:~:text=each%20Member%20State.-,3.18%20Access%20Certificate%20Authorities,-Access%20Certificate%20Authorities)
    - Access Certificate Authorities **issue access certificate to all PID Providers, QEAA Providers, PuB-EAA Providers**, **non-qualified EAA Providers** and Relying Parties in the EUDI Wallet ecosystem.
- [ARF "6.3.2.2 Data about the PID Provider or Attestation Provider is included in the registry"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification:~:text=of%20an%20error.-,6.3.2.3%20PID%20PROVIDER%20OR%20ATTESTATION%20PROVIDER%20RECEIVES%20AN%20ACCESS%20CERTIFICATE%20AND%20A%20REGISTRATION%20CERTIFICATE,-When%20a%20PID) 
    - When a PID Provider or Attestation Provider is registered by a Member State, a Access Certificate Authority (see Section 3.18 **issues one or more access certificates to the PID Provider or to the Attestation Provider.** A PID Provider or an Attestation Provider needs such a certificate to authenticate itself towards a Wallet Unit when issuing a PID or an attestation to it, as described in Section 6.6.2.2.
    - A PID Provider access certificate **does not indicate that its subject is a PID Provider**. Similarly, an Attestation Provider access certificate **does not indicate that its subject is a QEAA Provider, a PuB-EAA Provider, or a non-qualified EAA Provider**. Furthermore, the access certificate of a PID Provider or Attestation Provider **does not contain the Provider's registration to issue attestations of a specific type**, for instance an mDL or diploma. Such information is included in the registration certificates (if issued), and in any case available in the Registrar's online service.
    - To manage both situations, either with use of a registration certificate or without, the access certificate of a PID Provider or Attestation Provider contains a **URL to the Registrar's online service**, which a Wallet Unit can use to obtain information on the Provider's registration. 
- [ARF, Annex II, Topic 27 "Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties). 
See also [ARF, Annex II - High-Level Requirements "B. General requirements for the issuance of access certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=B.%20General%20requirements%20for%20the%20issuance%20of%20access%20certificates) and ["F. Requirements for the contents of access certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2331-topic-31---notification-and-publication-of-pid-provider-wallet-provider-attestation-provider-access-certificate-authority-and-provider-of-registration-certificates:~:text=F.%20Requirements%20for%20the%20contents%20of%20access%20certificates)
    - Similarly, a **QEAA Provider, PuB-EAA Provider, or non-qualified EAA Providers will receive an access certificate for each of the service supply point(s)** it uses to interact with Wallet Units to issue attestations.
- [Topic X "Relying Party Registration" / "2.2 Draft CIR on Relying Party registration"](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/discussion-topics/x-relying-party-registration.md)
    - The registrant receives **one or more Relying Party Access Certificates**. 
    - Requirements for Relying Party access certificates:
        - **X.509 certificate** with certificate policy and certificate practice statement
        - shall comply with **IETF RFC 3647**
        - plus additional requirements set out in the Annex IV

The Registrar keeps records of the issuance of PID / Attestation Provider Access Certificate for 10 years and publishes its history within a common REST API (JSON format).

*Requirements:*
- [Regulation (EU) 2025/848, Article 10 "Record keeping"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - Registrars shall keep records of the information provided by wallet-relying parties and registered in accordance with Annex I for the registration of a wallet-relying party and the issuance of the wallet-relying party access certificates and the wallet-relying party registration certificates, and of any subsequent changes to this information, **for 10 years**.
- [Regulation (EU) 2025/848, Annex II "Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - (1) The single common API shall:
        - (a) **be a REST API**, supporting JSON as a format and signed in accordance with the relevant requirements specified in Section 1.
        - (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying party, the name of the wallet-relying party or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14 and 15.
        - (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, current and historic wallet-relying party access certificates and wallet-relying party registration certificates but exclude the contact information in Annex I point 4.
        - (d) be published as an OpenAPI version 3, together with the appropriate documentation and technical specifications ensuring interoperability across the Union.
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    - (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.

### 2.4 Registration Certificate Request

See [Common Technical Onboarding Steps - 2.4 Registration Certificate Request](onboarding-base.md#24-registration-certificate-request) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Article 8. "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 2. Where a Member State authorised the issuance of a wallet-relying party registration certificate, that Member State shall:
        - (f) implement dedicated certificate policies and certificate practice statements for the wallet-relying party registration certificates in accordance with the requirements set out in Annex V.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 1. The wallet-relying party registration certificate policy applicable to the provision of wallet-relying party registration certificates shall describe the security requirements that apply to, and the rules that indicate the applicability of, a wallet-relying party registration certificate for their issuance to and use by wallet-relying parties in their interactions with wallet solutions. The wallet-relying party registration certificate policy shall be published in **human-readable**.
    - 2. The wallet-relying party registration certificate practice statement applicable to the provisioning of wallet-relying party registration certificates shall describe the practices that a provider of wallet-relying party registration certificates employs in issuing, managing, revoking, and re-keying wallet-relying party registration certificates, and, where applicable, how they relate to wallet-relying party access certificates issued to wallet-relying parties. The wallet relying party registration certificate practice statement shall be published in **human-readable**.
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates shall be **syntactically and semantically harmonised** across the Union and shall comply with at least the applicable NCP requirements as specified in standard **ETSI EN 319 411-1 version 1.4.1 (2023-10)** (ref. [Regulation (EU) 2025/848, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).

### 2.5 Registration Certificate Request Review

See [Common Technical Onboarding Steps - 2.5 Registration Certificate Request Review](onboarding-base.md#25-registration-certificate-request-review) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Article 8. "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    -  2. Where a Member State authorised the issuance of a wallet-relying party registration certificate, that Member State shall:
        - (a) require providers of wallet-relying party registration certificates to issue wallet-relying party registration certificates **exclusively to registered wallet-relying parties**;
        - (b) **ensure that each intended use is expressed** in the wallet-relying party registration certificates.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - The certificate policy and certificate practice statement applicable to the provision of wallet-relying party registration certificates [...] shall include:
        - (a) a **clear description of the public key infrastructure hierarchy** and certification paths from the end-entity wallet-relying party access certificates up to the top of the hierarchy used for issuing them, **indicating the expected trust anchor(s)** in such hierarchy and paths which should rely on the trust framework established in accordance with Article 5a(18) of Regulation (EU) No 910/2014.
        - (b) a comprehensive description of the procedures for the issuance of wallet-relying party registration certificates, including for the **verification of the identity and any other attributes of the wallet-relying party** to which a wallet-relying party certificate is to be issued.
        - (c) the obligation for the provider of wallet-relying party registration certificates, when issuing a wallet-relying party registration certificate, to verify that:
            - the wallet-relying party is included, **with a valid registration status, in a National Register** for Relying parties of the Member State in which that wallet-relying party is established.
            - the **information** in the wallet-relying party registration certificate is accurate and consistent with the registration information available from that register.
            - the wallet-relying party **access certificate is valid**.
            - the description of the procedures for revocation of wallet-relying party registration certificates is comprehensive.

### 2.6 Registration Certificate Issuance

See [Common Technical Onboarding Steps - 2.6 Registration Certificate Issuance](onboarding-base.md#26-registration-certificate-issuance) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates [...] shall include:
        - (i) The provider of wallet-relying party registration certificates **logs all wallet-relying party registration certificates they have issued**.
        - (j) the obligation for the wallet-relying party registration certificates:
            -    to include the location where the validation data of the advanced electronic signature or advanced electronic seal for the certificate used to sign or seal the registration certificate is available, for the entire trust chain to be built up to the **expected trust anchor**;
            - to include a machine-readable **reference to the applicable certificate policy and certificate practice statement**;
            - to include the **information** referred to in Annex I, points 1, 2, 3, 5, 6 and 8, 9, 10, 11, 12, 13, 14 and 15.
            - to include the **URL to the privacy policy** referred to in Article 8(2)g.
            - 	to include a **general access policy** as referred to in Article 8(3);
    - 4. The data exchange format for the relying party registration certificate shall be signed **JSON Web Tokens (IETF RFC 7519)** and **CBOR Web Tokens (IETF RFC 8392).**
- [ARF "6.3 Trust throughout a PID Provider or an Attestation Provider lifecycle"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification:~:text=or%20suspended%20separately.-,6.3%20Trust%20throughout%20a%20PID%20Provider%20or%20an%20Attestation%20Provider%20lifecycle,-6.3.1%20PID%20Provider)
    -    When a PID Provider or Attestation Provider is registered by a Member State, a Access Certificate Authority (see Section 3.18 **issues one or more access certificates to the PID Provider or to the Attestation Provider.** A PID Provider or an Attestation Provider needs such a certificate to authenticate itself towards a Wallet Unit when issuing a PID or an attestation to it, as described in Section 6.6.2.2.
    -    Furthermore, the access certificate of a PID Provider or Attestation Provider does not contain the Provider's **registration to issue attestations of a specific type**, for instance an mDL or diploma. Such information is **included in the registration certificates (if issued)**, and in any case available in the Registrar's online service.
    -    Such information is instead available via the Registrar's online service. Additionally, the same information is **included in a registration certificate issued to the PID Provider or Attestation Provider by a Provider of registration certificates, if the Registrar has a policy of issuing such certificate**s - see Section 3.17. 
- [ARF "3.19 Providers of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#317-registrars:~:text=in%20the%20ecosystem.-,3.19%20Providers%20of%20registration%20certificates,-If%20a%20Registrar)
    - If a Registrar has a policy of issuing registration certificates, it has one or more associated Provider(s) of registration certificates. Such a Provider **issues one or more registration certificates to each** registered Relying Party, **PID Provider, QEAA Provider, PuB-EAA Provider, and non-qualified EAA Provider.** Each registration certificate **contains (a subset of) the data registered for that entity**, as described in Section 3.17.
- [ARF, Annex II, Topic 27 "Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)
    - Finally, the registering entity will **receive one or more Registration Certificates containing the registered information**, if the Registrar has a policy of issuing such registration certificates.
- [ARF, Annex II, Topic 44 "Registration certificates for PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=A.2.3.44%20Topic%2044%20%2D%20Registration%20certificates%20for%20PID%20Providers%2C%20Providers%20of%20QEAAs%2C%20PuB%2DEAAs%2C%20and%20non%2Dqualified%20EAAs%2C%20and%20Relying%20Parties)
See also ["A. Generic requirements on the specification and contents of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=A.%20Generic%20requirements%20on%20the%20specification%20and%20contents%20of%20registration%20certificates) and  ["C. Requirements on the issuance of registration certificates to PID Providers and Attestation Providers"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=C.%20Requirements%20on%20the%20issuance%20of%20registration%20certificates%20to%20PID%20Providers%20and%20Attestation%20Providers).
    - A registration certificate may be issued by a Provider of registration certificates to a **PID Provider, a QEAA Provider, a PuB-EAA Provider, a non-qualified EAA Provider**, or a Relying Party during the registration process described in Topic 27. However, although registration of these entities is mandatory, issuance of a registration certificate is **optional**.
    - Registration certificates contain **generic information regarding its subject**, such as name, unique identifier, role (Relying Party, PID Provider, QEAA Provider, etc.), **service description, etc**.
    - A registration certificate for a PID Provider, a QEAA Provider, a PuB-EAA Provider, a non-qualified EAA Provider contains **information on the attestation type(s) it intends to issue.**
    - The above types of registration certificate can be **combined in a single certificate**, for instance in case an Attestation Providers intends to request data from the User's PID during issuance of an attestation. Such an Attestation Provider would then register both as a Relying Party (which is called a Service Provider in Technical Specification 5) and as a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider.
    - A registration certificate is **signed by the Provider of registration certificates** that issued it. 
- [Topic X "Relying Party Registration" / "2.2 Draft CIR on Relying Party registration"](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/discussion-topics/x-relying-party-registration.md).
    - The registrant receives **one or more Relying Party Registration Certificates**. 
    - Requirements for Relying Party registration certificates:
        - certificate policy and certificate practice statement shall comply with **IETF RFC 3647** and **IETF RFC 5755**
        - includes the information referred to in **Annex I, points 1, 2 and 8**
        - expresses attributes in way compliant with **IETF RFC 5755**
        - plus additional requirements set out in the **Annex V**

The Registrar keeps records of the issuance of PID / Attestation Provider Registration Certificate for 10 years and publishes its history within a common REST API (JSON format).
- [Regulation (EU) 2025/848, Article 10. "Record keeping"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_10:~:text=Article%C2%A010-,Record%20keeping,-Registrars%20shall%20keep)
    - Registrars shall **keep records of the information provided** by wallet-relying parties and registered in accordance with Annex I for the registration of a wallet-relying party and the issuance of the wallet-relying party access certificates and the wallet-relying party registration certificates, and of any subsequent changes to this information, **for 10 years**.
- [Regulation (EU) 2025/848, Annex II. "2. Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=2.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20ON%20THE%20SINGLE%20COMMON%20API%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
    - (1) The single common API shall:
        - (a) be a **REST API**, supporting **JSON** as a format and signed in accordance with the relevant requirements specified in Section 1.
        - (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying party, the name of the wallet-relying party or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14 and 15.
        - (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, **current and historic wallet-relying party access certificates and wallet-relying party registration certificates** but exclude the contact information in Annex I point 4.
        - (d) be published as an **OpenAPI version 3**, together with the appropriate documentation and technical specifications ensuring interoperability across the Union.
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    -  (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1. 

### 2.7 Notification to EU Commission and other Member States [MVP+ only]

**Note**: This step applies only to [MVP+] phase. For [MVP], notification to EU Commission is not required.

Member State notifies the PID / PuB-EAA Provider to EU Commission and other Member States.

*Requirements:*
- [Topic 31 "Notification and publication of PID Provider, Wallet Provider, Attestation Provider, Access Certificate Authority, and Provider of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2331-topic-31---pid-provider-wallet-provider-attestation-provider-and-access-certificate-authority-notification-and-publication:~:text=A.2.3.31%20Topic%2031%20%2D%20Notification%20and%20publication%20of%20PID%20Provider%2C%20Wallet%20Provider%2C%20Attestation%20Provider%2C%20Access%20Certificate%20Authority%2C%20and%20Provider%20of%20registration%20certificates)
See also ["A. Generic requirements for notification"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2331-topic-31---pid-provider-wallet-provider-attestation-provider-and-access-certificate-authority-notification-and-publication:~:text=A.%20Generic%20requirements%20for%20notification), ["B. Requirements for the notification of PID Providers"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2331-topic-31---pid-provider-wallet-provider-attestation-provider-and-access-certificate-authority-notification-and-publication:~:text=B.%20Requirements%20for%20the%20notification%20of%20PID%20Providers), ["D. Requirements for the notification of QEAA Providers"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2331-topic-31---pid-provider-wallet-provider-attestation-provider-and-access-certificate-authority-notification-and-publication:~:text=D.%20Requirements%20for%20the%20notification%20of%20QEAA%20Providers).
    - PID Providers, PuB-EAA Providers, Wallet Providers, Access Certificate Authorities, and Providers of registration certificates **must be notified by a Member State to the Commission**. As part of the notification process, the trust anchors of these parties must be included in a Trusted List.
    - Note: Notification **does not apply to QEAA Providers and (non-qualified) EAA Providers**, as explained in Sections D and F below, respectively.

- [ARF Tecnical Specification "Specification of systems enabling the notification and subsequent publication of Provider information"](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md#:~:text=Specification%20of%20systems%20enabling%20the%20notification%20and%20subsequent%20publication%20of%20Provider%20information)
    - The present document **specifies selected technical and procedural aspects related to the notification and subsequent publication of Provider information** according to (EU) No 910/2014 and the Commission Implementation Regulation (CIR) (EU) 2024/2980 of 28 November 2024 laying down rules for the application of Regulation (EU) No 910/2014 of the European Parliament and of the Council as regards notifications to the Commission concerning the European Digital Identity Wallet (EUDIW) ecosystem.

### 2.8 Publication in Trusted List

**For [MVP]**: The trust anchor of the PID / Attestation Provider is included in the WEBUILD Trusted List maintained by the WP4 Trust Infrastructure group. The Trusted List is made publicly accessible for testing purposes.

**For [MVP+]**: The trust anchor of the PID / Attestation Provider is included in a Trusted List maintained by the Member State's Trusted List Provider. For PID Providers, QEAA Providers, and PuB-EAA Providers, this is mandatory. Non-qualified EAA Providers are not included in a Trusted List by a Member State (ref. [ARF "6.3.2.4 PID Provider or Attestation Provider trust anchors are included in a Trusted List"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#6323-pid-provider-or-attestation-provider-receives-an-access-certificate-and-a-registration-certificate:~:text=registration%20certificate%20contents.-,6.3.2.4%20PID%20PROVIDER%20OR%20ATTESTATION%20PROVIDER%20TRUST%20ANCHORS%20ARE%20INCLUDED%20IN%20A%20TRUSTED%20LIST,-For%20a%20PID)).

*Requirements:*
- [ARF "3.5 Trusted List Provider"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#35-trusted-list-provider:~:text=and%20Wallet%20Providers.-,3.5%20Trusted%20List%20Provider,-A%20Trusted%20List)
    - A Trusted List Provider (TLP) is a body responsible for maintaining, managing, and publishing a Trusted List. Within the EUDI Wallet ecosystem, Trusted Lists exist for the following entities:
        - Wallet Providers, see Section 3.3,
        - **PID Providers**, see Section 3.4,
        - **QEAA Providers**, see Section 3.6,
        - **PuB-EAA Providers**, see Section 3.7,
        - Qualified Electronic Signature Remote Creation (QESRC) Providers, see Section 3.9,
        - Access Certificate Authorities, see Section 3.18,
        - Providers of registration certificates, see Section 3.19.
    - Non-qualified EAA Providers are trust service providers in the sense of the [European Digital Identity Regulation]. Therefore, **Trusted Lists and Trusted List Providers may also exist for non-qualified EAA Providers**. However, this is **out of scope of the ARF**.
- [ARF "6.3.2 PID Provider or Attestation Provider registration and notification](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification:~:text=Section%206.3.3.-,6.3.2%20PID%20Provider%20or%20Attestation%20Provider%20registration%20and%20notification,-6.3.2.1%20INTRODUCTION)
    - If the registration and notification processes are successful, at least the following happens:
        -    Data about the PID Provider or Attestation Provider is included in the registry of the relevant Registrar.
        -    The PID Provider or Attestation Provider receives an access certificate and optionally one or more registration certificates.
        -    **The trust anchors of the PID Provider or Attestation Provider are included in a Trusted List.**
- [ARF "6.3.2.4 PID Provider or Attestation Provider trust anchors are included in a Trusted List"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#6323-pid-provider-or-attestation-provider-receives-an-access-certificate-and-a-registration-certificate:~:text=registration%20certificate%20contents.-,6.3.2.4%20PID%20PROVIDER%20OR%20ATTESTATION%20PROVIDER%20TRUST%20ANCHORS%20ARE%20INCLUDED%20IN%20A%20TRUSTED%20LIST,-For%20a%20PID)
    - For a PID Provider, a QEAA Provider, or a PuB-EAA Provider, successful registration and notification also means **that the Provider is notified to the European Commission and that its trust anchors are included in a Trusted List.** Relying Parties can use these trust anchors to verify the authenticity of PIDs, QEAAs, and PuB-EAAs they obtain from Wallet Units.
    - **Non-qualified EAA Providers are not included in a Trusted List** by a Member State.
- [Topic 31 "Notification and publication of PID Provider, Wallet Provider, Attestation Provider, Access Certificate Authority, and Provider of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2331-topic-31---pid-provider-wallet-provider-attestation-provider-and-access-certificate-authority-notification-and-publication:~:text=A.2.3.31%20Topic%2031%20%2D%20Notification%20and%20publication%20of%20PID%20Provider%2C%20Wallet%20Provider%2C%20Attestation%20Provider%2C%20Access%20Certificate%20Authority%2C%20and%20Provider%20of%20registration%20certificates). 
    -  PID Providers, PuB-EAA Providers, Wallet Providers, Access Certificate Authorities, and Providers of registration certificates **must be notified by a Member State to the Commission. **As part of the notification process, the trust anchors of these parties must be included in a Trusted List**.
  
## 3. Post-Onboarding
Once the Access and Registration Certificates are active, the PID / Attestation Provider  may start offering its registered services to EUDI Wallet Users. It must keep its registration information up to date and comply with certification and revocation policies. Any suspension, cancellation, or change in the PID / Attestation Provider ’s status or intended use - whether initiated by the Registrar, another competent authority, or the PID / Attestation Provider  itself - triggers the update or revocation of its certificates and registry data in line with EU harmonised procedures.

*Preconditions:*
- **Prerequisites**: 
    - The Registration Policy, Access / Registration Certificate Policy and Practice Statement are defined and published at national level and harmonised across the Union so that continuous monitoring mechanisms and revocation procedures are in place.
- **Triggers**: 
    - Change in the PID / Attestation Provider’s registration data (e.g. legal status or intended use);
    - Automated detection of inconsistency or invalid data during monitoring by the Registrar or other competent authorities.
    - Notification from competent authorities (e.g. Supervisory Body, Data Protection Authority, Access Certificate Authority, Provider of Registration Certificate) regarding the need for registration or certificates suspension / cancellation / revocation.

*Postconditions:*
- **Success**: 
    - The PID / Attestation Provider updates the existing registration (possibly through automated means) and maintains valid certificates aligned with registry information.
    - The Registrar informs the Access Certificate Authority, the Provider of Registration Certificate and the affected PID / Attestation Provider about the PID / Attestation Provider suspension or cancellation without undue delay (≤ 24 hours after the event).
    - The issued Access / Registration Certificate are revoked according to the certificate policy and the certificate practice statement (e.g. when the content of the certificate is no longer accurate and consistent with the information registered, or when the registration of the PID / Attestation Provider is modified, suspended or cancelled).
    - Updates on Access / Registration Certificates revocation are processed automatically and published within prescribed timeframes (e.g. ≤ 24 hours after request).
- **Failure**: 
    - The competent authorities do not properly follow the defined measures and processes on certificates revocation.
- **Outputs**:
    - Updated and published certificate status and revocation information.
    - Audit logs and monitoring records for compliance verification.
    - Notifications to the PID / Attestation Provider and other interested parties of any registration or certificates status change.

### 3.1 Registration Monitoring

See [Common Post-Onboarding Steps - 3.1 Registration Monitoring](onboarding-base.md#31-registration-monitoring) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 2.Registrars may suspend or cancel a registration of a wallet-relying party where the registrars have reasons to believe one of the following:
        - (a) the registration contains **information**, which is **inaccurate**, out of date or misleading.
        - (b) the wallet-relying party is **not compliant** with the registration policy.
        - (c) the wallet-relying party is **requesting more attributes **than they have registered in accordance with Article 5 and Article 6.
        - (d) the wallet-relying party is otherwise **acting in breach of Union or national law** in a manner related to their role as wallet-relying party.

The Provider of Registration Certificate monitors continuously and automatically

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

See [Common Post-Onboarding Steps - 3.2 Registration Update](onboarding-base.md#32-registration-update) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Article 5. "Information to be provided to the national registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_5:~:text=Information%20to%20be%20provided%20to%20the%20national%20registers)
     - 2. Wallet-relying party shall ensure that the **information provided is accurate** at the time of registration.
     - 3. Wallet-relying party **shall update any information previously registered** in the National Register of wallet-relying parties **without undue delay.**
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
         - (d) the obligation for the provider of wallet-relying party registration certificates implements **measures and processes** on:
            - **reissue the wallet-relying party registration certificate**;

### 3.3 Registration Suspension / Cancellation

See [Common Post-Onboarding Steps - 3.3 Registration Suspension / Cancellation](onboarding-base.md#33-registration-suspension--cancellation) in the base document.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 1. Registrars shall suspend or cancel a registration of a wallet-relying party where such a suspension or cancellation is **requested by a supervisory body** pursuant to Article 46a(4), point (f) of Regulation (EU) No 910/2014.
    - 3. Registrars shall suspend or cancel a registration of a wallet-relying party where the **request for cancellation or suspension is made by the same wallet-relying party.**
    - 4. When considering the suspension or cancellation in accordance with paragraph 2, the registrar shall conduct a **proportionality assessment**, taking into account the impact on the fundamental rights, security and confidentiality of the users in the ecosystem, as well as the severity of the disruption envisaged to be caused by the suspension or cancellation and the associated costs, both for the wallet-relying party and the user. Based on the result of this assessment, **the registrar may suspend or cancel the registration with or without prior notice to the affected wallet-relying party**.
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_6:~:text=Article%C2%A06-,Registration%20processes,-1.%C2%A0%C2%A0%C2%A0Registrars%20shall)
    - 7. When a wallet-relying party **no longer intends to rely upon wallet units** for the provision of public or private services under a specific registration, it shall **notify the relevant registrar without undue delay and request the cancellation of that registration**.

- [ARF "6.3.3 Suspension or cancellation of the registration of a PID Provider or Attestation Provider"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#631-pid-provider-or-attestation-provider-lifecycle:~:text=Topic%2031.-,6.3.3%20Suspension%20or%20cancellation%20of%20the%20registration%20of%20a%20PID%20Provider%20or%20Attestation%20Provider,-Under%20specific%20conditions)
    - Under specific conditions, a **Registrar may decide to suspend or cancel the registration of a PID Provider or Attestation Provider.** The conditions for this will be specified by each Registrar.
    - Suspension or cancellation implies that the PID Provider or Attestation Provider access certificates are revoked. As a result, **the PID Provider or Attestation Provider will no longer be able to issue PIDs or attestations to Wallet Units**

The Registrar sends notice about the PID / Attestation Provider registration suspension / revocation.
The PID / Attestation Provider receives notice of its registration suspension / revocation.
The Access Certificate Authority receives notice of the PID / Attestation Provider registration suspension/ revocation.
The Provider of Registration Certificate receives notice of the PID / Attestation Provider registration suspension / revocation.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 5.   Where the registration of a wallet-relying party is suspended or cancelled, the **registrar shall inform** **the provider of the relevant wallet-relying party access certificates**, the **provider of the relevant wallet-relying party registration certificates**, and the **affected wallet-relying party** of this action **without undue delay and not later than 24 hours after the suspension or cancellation.** This notification shall include **information** on the reasons for the suspension or cancellation and on the available means of **redress or appeal**.

### 3.4 Access / Registration Certificate Revocation

See [Common Post-Onboarding Steps - 3.4 Certificate Revocation](onboarding-base.md#34-certificate-revocation) in the base document.

**Note for PID/EAA Providers**: For PID Providers, QEAA Providers, or PuB-EAA Providers, suspension or cancellation also implies that its status in the respective Trusted List will be changed to Invalid (ref. [ARF "6.3.3 Suspension or cancellation of the registration of a PID Provider or Attestation Provider"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#631-pid-provider-or-attestation-provider-lifecycle:~:text=Topic%2031.-,6.3.3%20Suspension%20or%20cancellation%20of%20the%20registration%20of%20a%20PID%20Provider%20or%20Attestation%20Provider,-Under%20specific%20conditions)).

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates [...] shall include:
        - (g) the obligation for the providers of wallet-relying party access certificates to **allow** relevant stakeholders, including **wallet-relying parties** as regards their own certificates, **competent supervisory bodies** and **data protection authorities**, **to request the revocation** of wallet-relying party access certificates.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (f) the obligation for the provider of wallet-relying party registration certificates to **allow** relevant stakeholders, including **wallet-relying parties** as regards their own certificates, competent **supervisory bodies** and **data protection authorities**, **to request the revocation** of wallet-relying party registration certificates.
Then:
- The Access Certificate Authority revokes the Access Certificate (without undue delay).
- The Provider of Registration Certificate revokes the Registration Certificate (without undue delay).

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 6. **The provider of wallet-relying party access certificates** and the **provider of wallet-relying party registration certificates**, shall, where applicable, **revoke without undue delay the wallet-relying party access certificates, and the wallet-relying party registration certificates,** respectively, of the wallet-relying party for which registration has been suspended or cancelled.
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates [...] shall include:
        - (d) a comprehensive description of the **procedures for revocation of wallet-relying party access certificates**;
        - (e) the obligation for the providers of wallet-relying party access certificates to implement **measures and processes** on:
            - **revoking**, when changes require, **any wallet-relying party certificate** that the provider issued to the corresponding wallet-relying party, in particular when the content of the certificate is **no longer accurate and consistent** with the information registered, or **when the registration of the wallet-relying party is suspended or cancelled**.
     - 4. The revocation set out in point 3(g) **shall become effective immediately** upon its publication. 
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (c) the obligation for the provider of wallet-relying party registration certificates, when issuing a wallet-relying party registration certificate, to verify that:
            - the **description of the procedures for revocation** of wallet-relying party registration certificates is comprehensive.
        - (d) the obligation for the provider of wallet-relying party registration certificates implements **measures and processes** on:
            -    **revoking any wallet-relying party registration certificate** that they issued to the corresponding wallet-relying party, when such changes so require, in particular when the content of the certificate is **no longer accurate and consistent** with the information registered, or **when the registration of the wallet-relying party is modified, suspended or cancelled**.
    - 5. The revocation referred to in point 3(g/f) **shall become effective immediately** upon its publication.

- [ARF "6.3.3 Suspension or cancellation of the registration of a PID Provider or Attestation Provider"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#631-pid-provider-or-attestation-provider-lifecycle:~:text=Topic%2031.-,6.3.3%20Suspension%20or%20cancellation%20of%20the%20registration%20of%20a%20PID%20Provider%20or%20Attestation%20Provider,-Under%20specific%20conditions)
    - Suspension or cancellation implies that the **PID Provider or Attestation Provider access certificates are revoked.** As a result, the PID Provider or Attestation Provider will no longer be able to issue PIDs or attestations to Wallet Units.
    - For a PID Provider, QEAA Provider, or PuB-EAA Provider, suspension or cancellation also implies that its status in the **respective Trusted List will be changed to Invalid.** As a result, Relying Parties will no longer trust PIDs or attestations issued by that Provider. For non-qualified EAA Providers, the applicable Rulebook (see Topic 12) may define similar mechanisms ensuring that Relying Parties will no longer trust the trust anchors of EAA Providers of which the registration was suspended or cancelled.
    - When a Registrar suspends or cancels registration of a PID Provider or Attestation Provider, the **PID Provider or Attestation Provider revokes all of their PIDs or attestations** as described in Section 6.6.3.7.

- The Access Certificate Authority publishes the Access Certificate revocation status (within 24 hours).
- The Provider of Registration Certificate publishes the Registration Certificate revocation status (within 24 hours).

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

## Normative References

See [Common Normative References](onboarding-base.md#common-normative-references) in the base document for common references applicable to all participant onboarding processes.

### Additional PID/EAA Provider-Specific References

#### European Commission Technical Specifications
- **EC TS02 v0.9** (2025-04): [Specification of systems enabling the notification and subsequent publication of Provider information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md)

#### ETSI Standards
- **ETSI TS 119 472-2** (v1.1.1): [Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 2: Profiles for EAA/PID Presentations to Relying Party](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.01.01_60/ts_11947202v010101p.pdf)
- **ETSI EN 319 412-3**: [Certificate Profiles; Part 3: Certificate Profile for Natural Persons](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.04.01_60/en_31941203v010401c.pdf) - Corporate identity-binding practices
- **ETSI EN 319 412-6** (v01.00.00): [Certificate profile requirements for PID, Wallet, EAA, QEAA and PSBEAA providers](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf)

