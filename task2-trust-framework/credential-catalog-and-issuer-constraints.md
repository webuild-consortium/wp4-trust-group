# Comprehensive Evidence and References: Credential Catalogues, EAA, and QEAA

This document compiles all evidence, references, and text about credential catalogues, catalogue of attestations, EAA (Electronic Attestation of Attributes), and QEAA (Qualified Electronic Attestation of Attributes) found in the EUDI Wallet Architecture and Reference Framework. It also covers mechanisms used to prevent unallowed credential type issuance by bogus credential issuers, including the use of Trusted Lists and registration certificates to configure which Credential Issuers are authorized to issue specific attestation types.

## Table of Contents

1. [Glossary and Definitions](#glossary-and-definitions)
2. [Credential Catalogues Overview](#credential-catalogues-overview)
3. [Catalogue of Attributes](#catalogue-of-attributes)
4. [Catalogue of Attestation Schemes](#catalogue-of-attestation-schemes)
5. [EAA (Electronic Attestation of Attributes)](#eaa-electronic-attestation-of-attributes)
6. [QEAA (Qualified Electronic Attestation of Attributes)](#qeaa-qualified-electronic-attestation-of-attributes)
7. [PuB-EAA (Public Sector EAA)](#pub-eaa-public-sector-eaa)
8. [Legal and Regulatory References](#legal-and-regulatory-references)
9. [High-Level Requirements](#high-level-requirements)
10. [Technical Specifications](#technical-specifications)
11. [Important Notes and Distinctions](#important-notes-and-distinctions)
    - [Using Trusted Lists to Configure Allowed Credential Issuers](#using-trusted-lists-to-configure-allowed-credential-issuers-for-specific-attestation-types)
12. [Related Topics and Cross-References](#related-topics-and-cross-references)

## Glossary and Definitions

This section provides key definitions and terminology used throughout this document.

### Core Concepts

- **EAA (Electronic Attestation of Attributes)**: An electronic attestation of attributes that can be issued in three forms: QEAA, PuB-EAA, or non-qualified EAA.

- **QEAA (Qualified Electronic Attestation of Attributes)**: An electronic attestation of attributes issued by a qualified trust service provider (QTSP) that meets the requirements laid down in Annex V of Regulation (EU) 2024/1183.

- **PuB-EAA (Public Sector EAA)**: An electronic attestation of attributes issued by a public sector body that is responsible for an authentic source or by a public sector body designated by the Member State to issue such attestations on behalf of public sector bodies responsible for authentic sources, in accordance with Article 45f and Annex VII of Regulation (EU) 2024/1183.

- **Non-Qualified EAA**: An EAA which is not a QEAA or a PuB-EAA. Non-qualified EAAs can be provided by any (non-qualified) Trust Service Provider.

- **QTSP (Qualified Trust Service Provider)**: A trust service provider that is qualified in accordance with Regulation (EU) No 910/2014 (eIDAS Regulation).

### Catalogues

- **Catalogue of Attributes**: A catalogue exclusively intended for use by QTSPs issuing QEAAs, enabling them to find the access point of the Authentication Source responsible for a given attribute.

- **Catalogue of Attestation Schemes** (also called "catalogue of schemes for the attestation of attributes"): A catalogue intended for use by Relying Parties, Attestation Providers, and other actors to discover which types of attestations exist within the ecosystem and understand their identifiers, syntax, and semantics.

### Attestation Components

- **Attestation Scheme**: A machine-readable attestation definition that specifies the structure, attributes, and technical format of an attestation type.

- **Attestation Rulebook**: A human-readable specification of an attestation scheme that describes the significance, data quality assurance requirements, and minimum requirements for attestation issuance. While the scheme defines the formal structure, the rulebook focuses on substantial requirements.

### Trust Infrastructure

- **Trusted List**: A list maintained by a Trusted List Owner (also known as Ecosystem Authority or Scheme Owner) that contains trust anchors and metadata for trusted entities (e.g., PID Providers, QEAA Providers, PuB-EAA Providers, EAA Providers).

- **Trusted List Owner** (also **Ecosystem Authority** or **Scheme Owner**): The entity accountable for allowing listed EAA Providers (Trusted Entities) to issue credentials mentioned in the metadata of the Trusted List. A Trusted List Owner can list multiple attribute schemes and can list itself as an EAA Provider.

- **Registration Certificate**: A certificate issued to a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider that contains the type(s) of attestation that the entity intends to issue to Wallet Units. Registration certificates are optional and are issued if the Registrar has a policy of issuing such certificates.

- **Registrar**: An entity in a Member State responsible for registering PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers.

### Scope Note

**Note on Alternative Technologies**: This document and the associated project focus on X.509–based QEAA models as defined in the applicable ETSI and eIDAS2 framework. Alternative approaches such as AnonCreds-based mechanisms for revocation and status management with strong privacy guarantees are considered **out of scope** for the first releases of this project.

## Credential Catalogues Overview

### Definition

The EUDI Wallet ecosystem defines **two distinct catalogues** to support discovery and interoperability:

1. **Catalogue of attributes** - For QTSPs to find verification points
2. **Catalogue of attestation schemes** (also called "catalogue of schemes for the attestation of attributes") - For discovering attestation types

### Key Documents

#### Main Architecture Document
- **File**: `architecture-and-reference-framework-main.md`
- **Section**: 5.5 - "Catalogue of attributes and catalogue of attestation schemes"
- **Lines**: 2519-2608

#### Discussion Paper
- **File**: `discussion-topics/o-catalogues-for-attestations.md`
- **Title**: Topic O - Catalogues for Attestations
- **Version**: 1.0, updated 29 Sep 2025
- **GitHub Discussion**: [Link](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/discussions/557)

#### Technical Specification
- **File**: `technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md`
- **Note**: Detailed specification is in the standards and technical specifications repository

#### Requirements Documents
- **Topic 25**: Unified definition and controlled vocabularies for attributes (`annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md`)
- **Topic 26**: References to catalogue of Attestation Rulebooks

### Objectives

The catalogues support achieving a high level of interoperability:

#### Technical Interoperability
Through common standards, protocols, and technical specifications enabling:
- Issuance of attestations
- Presentation of attestations
- Processing of attestations

#### Semantic Interoperability
Through clear definitions of attestation contents:
- Which attributes exist for each attestation type
- Attribute identifiers
- Attribute syntax
- Attribute semantics

### Legal Basis

#### Primary Legislation
- **Article 45e(2) of Regulation (EU) 2024/1183** (European Digital Identity Regulation)
  - Empowers the Commission to establish specifications and procedures for:
    1. The catalogue of attributes
    2. The catalogue of attestation schemes
    3. Verification procedures for qualified electronic attestations of attributes

#### Implementing Regulation
- **Commission Implementing Regulation (EU) 2025/1569 of 29 July 2025**
  - **Article 7**: Defines the catalogue of attributes
  - **Article 8**: Defines the catalogue of schemes for the attestation of attributes

## Catalogue of Attributes

### Purpose

The catalogue of attributes is **exclusively intended for use by QTSPs** issuing QEAAs. It enables them to find the access point of the Authentication Source responsible for a given attribute, at which the QTSP can verify the value of that attribute for a given User.

*This is stated in the ARF main document at Section 5.5.2 (lines 2557-2560) of `architecture-and-reference-framework-main.md`.*

### Scope

- Limited to attributes that rely on **authentic sources within the public sector**
- Primary objective: **discovery of verification points**
- Only **specific types of entities** can add or modify entries

### Key Characteristics

- Must be **publicly available** and **machine-readable**
- Contents available in both **human and machine-readable formats**
- Commission-run catalogue
- High availability required (avoiding single point of failure)

### Registration Requirements

According to **Article 7 of Commission Implementing Regulation 2025/1569**, a request to include or modify an attribute must contain at least:

1. **Identification of the entity** making the request
2. **Reference to Union or national law** (where applicable) under which the entity is considered a primary source of information or recognised authentic source
3. **Attribute status**: whether the request refers to an existing attribute or is a new attribute
4. **Namespace** for the identifier of the attributes (unique within the catalogue of attributes)
5. **Attribute identifier** (unique within the namespace) and **version**
6. **Semantic description** of the attribute
7. **Data type** of the attribute
8. **Verification point** for the attribute at national level or a link to a description on how to initiate verification requests

### Who Can Request Registration

**Article 7 paragraph 3 of Commission Implementing Regulation (EU) 2025/1569** specifies:

- **Member States** SHALL request inclusion of attributes listed in Annex VI to Regulation (EU) No 910/2014 wherever those attributes rely on authentic sources for verification by qualified trust service providers
- **Member States** MAY request inclusion of attributes not listed in Annex VI wherever those attributes rely on authentic sources within the public sector
- **Private entities** that are considered primary sources of information or recognised as authentic in accordance with Union or national law MAY request inclusion of attributes not listed in Annex VI wherever the requesting entity is responsible for those attributes

### High-Level Requirements

From **Topic 25**:

| **Index** | **Requirement Specification** |
|-----------|-------------------------------|
| CAT_04 | A request to include or to modify an attribute in the catalogue of attributes SHALL indicate how a QTSP can use the verification point for that attribute. *Note: This could be, for instance, in the form of (a reference to) an endpoint description text.* |

### Maintenance and Availability

- Commission SHALL make publicly available the existence and maintenance of the catalogue
- Processes SHALL include:
  - Proposing registration to public and private parties
  - Registering attributes
  - Conditions for updating and/or removing attributes
  - Archiving and logging changes
  - Versioning

### Important Notes

- The catalogue of attributes will be used by QTSPs, and each Member State remains free to implement its own verification mechanisms, including the use of OOTS (Once-Only Technical System)

## Catalogue of Attestation Schemes

### Purpose

The catalogue of attestation schemes is intended for use by **Relying Parties, Attestation Providers, and other actors** in the EUDI Wallet ecosystem. It enables them to:

- Discover which types of attestations already exist within the ecosystem
- Understand the identifiers, syntax, and semantics of all attributes within each type of attestation

### Scope

- **Broader scope** than the catalogue of attributes
- Allows **any scheme owner** to register their attestation scheme
- For QEAAs, PuB-EAAs, and EAAs
- May also include attestation schemes for non-qualified EAAs

### Key Principles

1. **Machine-readable format**: Attestation schemes are machine-readable, and each scheme published in the catalogue refers to the corresponding human-readable Attestation Rulebook

2. **Registration is not mandatory**:
   - Attestation schemes for QEAAs and PuB-EAAs **may** be registered (not mandatory)
   - Registration and publication of non-qualified EAAs is not mandatory

3. **Commission responsibility**: The Commission will take measures to establish and maintain the catalogue

4. **Public accessibility**: The catalogue will be publicly accessible

5. **No automatic obligations**: Registration does not create any obligation for acceptance of the relevant type of attestation by any actor. Neither does it automatically imply cross-border recognition

6. **Integration**: Where possible, existing tools created by Member States, the Commission and cross-border organisations will be used to connect to the catalogue

### Registration Requirements

According to **Article 8 of Commission Implementing Regulation 2025/1569**, a request to include or modify a scheme must contain at least:

1. **Name of the scheme**
2. **Name and contact information** of the scheme owner
3. **Status and version** of the scheme
4. **Reference to specific laws, standards or guidelines** where issuance, validation, or use of an electronic attestation of attributes within the scope of the scheme is subject to them
5. **Format or formats** of electronic attestation of attributes within the scope of the scheme
6. **Attribute information**: One or more namespaces, attribute identifiers, semantic descriptions and data types of each attribute that is part of an electronic attestation of attributes within the scope of the scheme, either by:
   - Reference to an attribute in the catalogue of attributes in Article 7, or
   - An attribute defined in an analogue way within the scope of the scheme
7. **Trust model and governance mechanisms** applied under the scheme, including revocation mechanisms
8. **Requirements concerning providers** or the sources of information on which those providers rely when issuing electronic attestations of attributes
9. **Statement** whether electronic attestations of attributes within the scope of the scheme are to be issued as:
   - Qualified electronic attestations of attributes (QEAAs)
   - Electronic attestations of attributes issued by or on behalf of a public sector body responsible for an authentic source (PuB-EAAs)
   - Both

### Who Can Request Registration

**Article 8 paragraph 3 of Commission Implementing Regulation (EU) 2025/1569** specifies:

- **Owners of a scheme** for the attestation of attributes may request adding schemes to the catalogue

### High-Level Requirements

From **Topic 12** (Attestation Rulebooks):

| **Index** | **Requirement Specification** |
|-----------|-------------------------------|
| ARB_07 | When determining the attributes to be included in a new attestation type, the Scheme Provider for the applicable Attestation Rulebook SHOULD consider referring to attributes that are already included in the catalogue of attributes specified in Topic 25 or specified in an attestation scheme included in the catalogue of attestation schemes specified in Commission Implementing Regulation 2025/1569, rather than unnecessarily re-defining all attributes. |
| ARB_33 | If a Scheme Provider for an Attestation Rulebook registers an attestation scheme in the catalogue of attestation schemes meant in Commission Implementing Regulation 2025/1569, Article 8, the registration SHALL include a reference to the corresponding Attestation Rulebook. *Note: By definition, an attestation scheme is machine-readable, whereas an Attestation Rulebook is human-readable.* |

### Maintenance and Availability

- Commission SHALL make the catalogue publicly available and machine-readable
- May be hosted by the Commission or parts may be referenced to other catalogues
- **Delegation to sector-specific authorities**: The Commission may delegate the maintenance of the catalogue to sector-specific authorities, both at the EU level and the national level. This would include the possibility to delegate sector-specific authorities to maintain it on behalf of the Commission.
- Must include an e-discovery mechanism
- High availability required (avoiding single point of failure)

### Publication Process

An Attestation Scheme Provider may publish a new attestation in the **catalogue of attestation schemes** to enable discovery by Relying Parties and other actors. When doing so, the provider **also supplies the machine-readable attestation scheme** in accordance with Technical Specification 11.

### Important Distinctions

#### Scheme vs. Rulebook
- **Scheme for the attestation of attributes** = Machine-readable attestation definition that describes the formal structure (data content descriptive structure)
- **Attestation Rulebook** = Human-readable specification of the scheme that focuses on significance and data quality assurance that should be assured as a minimum requirement by the attestation issuer (substantial requirements)

**Note**: While the scheme defines the formal structure, the rulebook focuses on substantial requirements. For this reason, the sector or industry affiliation should be an access certificate attribute and referred to in the registration certificate.

#### Sectorial Authority Management

Specific sectorial authorities could manage attestation schemes, both at the EU level and the national level. A good example could be the banking sector: a financial and banking data model has been defined at EU level (included in the openbanking API interfaces) and could be extended at national level by the National competence authorities (e.g., national central banks). Data schemes, their inheritance, dependencies, taxonomy, rulebooks, access and registration policies could be delegated to sectorial authorities. Other examples could be the educational sector, commercial sector, and so on.

The rulebook could include a certification process for data quality assurance within the credential issuance process, supervised and ensured by sectorial authorities.

Registering a scheme and its rulebook is assurance of cross-sector interoperability, and it allows issuance restriction policies, enabling WRPRC policy management, so ensuring data quality to the ecosystem.

#### Two Catalogues Serve Different Purposes

| Aspect | Catalogue of Attributes | Catalogue of Attestation Schemes |
|--------|------------------------|----------------------------------|
| **Primary Users** | QTSPs issuing QEAAs | Relying Parties, Attestation Providers, other actors |
| **Purpose** | Find verification points for attributes | Discover attestation types and understand attributes |
| **Scope** | Limited to attributes from authentic public-sector sources | Broader - any scheme owner can register |
| **Who Can Register** | Specific entities (Member States, certain private entities) | Any scheme owner |
| **Mandatory Registration** | N/A | Not mandatory for QEAAs/PuB-EAAs |

## EAA (Electronic Attestation of Attributes)

### Definition

An **Electronic Attestation of Attributes (EAA)** is an electronic attestation of attributes that can be issued in three forms:

1. **QEAA** (Qualified Electronic Attestation of Attributes)
2. **PuB-EAA** (Public Sector EAA)
3. **Non-Qualified EAA** (EAA which is not a QEAA or a PuB-EAA)

### Non-Qualified EAA

#### Definition

A non-qualified EAA is an EAA which is not a QEAA or a PuB-EAA.

#### Providers

Non-qualified EAAs can be provided by any (non-qualified) Trust Service Provider. While they will be supervised under the [European Digital Identity Regulation](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183), it can be assumed that other legal or contractual frameworks will mostly govern the rules for provision, use and recognition of EAAs. Those other frameworks may cover policy areas such as educational credentials, digital payments, although they may also rely on Qualified Electronic Attestation of Attributes Providers.

#### Characteristics

- For non-qualified EAAs to be used, EAA Providers offer Users a way to request and obtain these EAAs
- This implies that these non-qualified EAA Providers comply with the Wallet Unit interface specifications
- The terms and conditions of issuing EAAs and related services are subject to sectoral rules
- Non-qualified EAA Providers are trust service providers in the sense of the [European Digital Identity Regulation](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183)
- Trusted Lists and Trusted List Providers may also exist for non-qualified EAA Providers

**Note on Regulation**: Non-qualified EAAs and their providers are regulated under Regulation (EU) 2024/1183. References include Article 19a, Article 45h of Regulation (EU) 2024/1183, Commission Implementing Regulation (EU) 2025/2160, and Commission Implementing Regulation (EU) 2024/2977. While non-qualified EAAs operate under a different level of trust compared to QEAAs and PuB-EAAs, they are still subject to regulatory oversight.

#### Revocation and Status Management

For revocation and status management of non-qualified EAAs, the revocation mechanism to be used should be specified in the applicable Attestation Rulebook, in accordance with the ARF requirements for Attestation Status List or Attestation Revocation List mechanisms (see VCR_11).

#### Validation Requirements

**OIA_15**: For both proximity and remote presentation flows, a Relying Party SHALL validate the signature of a non-qualified EAA using a trust anchor provided according to the mechanism(s) specified in the applicable Rulebook, see [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks).

**ISSU_10**: After a Wallet Unit receives a non-qualified EAA from an EAA Provider, it SHALL validate the signature of the EAA using a trust anchor provided according to the mechanism(s) specified in the applicable Rulebook, see [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks).

#### Attestation Rulebook Requirements

**ARB_12**: The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include an attribute in the Rulebook indicating that the attestation is an EAA. This attribute SHALL reference the technical specification meant in ARB_25.

**ARB_15**: The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include in the Rulebook one or more attributes or metadata representing the set of data meant in [Annex V](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-54-1) point b) of the European Digital Identity Regulation.

#### Registration

- EAA Providers must be registered by Registrars in Member States
- Registration certificates may be issued to EAA Providers
- EAA Providers must have access certificates issued by Access Certificate Authorities

## QEAA (Qualified Electronic Attestation of Attributes)

### Definition

A **QEAA** is an electronic attestation of attributes which is issued by a qualified trust service provider (QTSP) and meets the requirements laid down in Annex V of the Regulation.

### Providers

#### QEAA Provider Role

**Qualified EAAs are provided by Qualified Trust Service Providers (QTSPs).** The general trust framework for QTSPs (see Chapter III, Section 3 of the [European Digital Identity Regulation]) applies also to QEAA Providers, but specific rules for the Trust Service of issuing QEAAs may be defined as well.

#### Key Responsibilities

- QEAA Providers maintain an interface to Wallet Units to provide QEAAs upon request
- Potentially, they also maintain an interface towards Authentic Sources to verify the value of User attributes, as specified in [Topic 42](./annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md#a2324-topic-42---requirements-for-qtsps-to-access-authentic-sources)

#### User Authentication

It is likely that for most QEAAs, a QEAA Provider will need to verify the identity of a User when issuing a QEAA. It is up to each QEAA Provider to implement the necessary User authentication processes, in compliance with all applicable national and Union legislation. Note that, when User identity verification is necessary, it is likely that the User requesting a QEAA already possesses a PID. This would enable the QEAA Provider to carry out User identification and authentication at LoA high, by requesting and verifying User attributes from the PID in the Wallet Unit.

#### Terms and Conditions

The terms and conditions of these services are for each QEAA Provider to determine, beyond what is specified in the [European Digital Identity Regulation].

### Validation Requirements

**OIA_13**: For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a QEAA in accordance with Art.32 of the [European Digital Identity Regulation](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183). For the verification, the Relying Party SHALL use a trust anchor provided in a QEAA Provider Trusted List made available in accordance with [Art. 22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1) of the European Digital Identity Regulation.

**ISSU_08**: After a Wallet Unit receives a QEAA from a QEAA Provider, it SHALL validate the qualified signature of the QEAA in accordance with Art.32 of the [European Digital Identity Regulation](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183). For the verification, the Wallet Unit SHALL use a trust anchor provided in a QEAA Provider Trusted List made available in accordance with [Art. 22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1) of the European Digital Identity Regulation.

### Attestation Rulebook Requirements

**ARB_11**: The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook an attribute as meant in [Annex V](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-54-1) point a) and [Annex VII](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-56-1) point a) of the European Digital Identity Regulation. This attribute SHALL reference the technical specification meant in ARB_25.

**ARB_13**: The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA SHALL include in the Rulebook one or more attributes or metadata representing the set of data meant in [Annex V](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-54-1) point b) of the European Digital Identity Regulation.

**ARB_16**: The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook one or more attributes representing the set of data meant in [Annex V](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-54-1) point c) or [Annex VII](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e46-55-1) point c) of the European Digital Identity Regulation.

### Registration and Trusted Lists

- QEAA Providers must be registered by Registrars in Member States
- QEAA Providers are notified to the Commission and published in QEAA Provider Trusted Lists
- Trust anchors are notified to Commission and published in QEAA Provider Trusted List
- Registration certificates may be issued to QEAA Providers
- QEAA Providers must have access certificates issued by Access Certificate Authorities

#### Revocation and Status Management

For revocation and status management of QEAAs, the revocation mechanism to be used should be specified in the applicable Attestation Rulebook, in accordance with the ARF requirements for Attestation Status List or Attestation Revocation List mechanisms (see VCR_11).

### Catalogue Registration

- The Schema Provider for an Attestation Rulebook that is a QEAA or PuB-EAA SHOULD request the registration of all attributes in that QEAA or PuB-EAA in the catalogue of attributes
- The Schema Provider for an Attestation Rulebook that is a QEAA or PuB-EAA SHOULD register its Rulebook in the catalogue of Attestation Rulebooks
- Attestation schemes for QEAAs may be registered and published in the catalogue of attestation schemes, but this is not mandatory

## PuB-EAA (Public Sector EAA)

### Definition

A **PuB-EAA** is an electronic attestation of attributes issued by a public sector body that is responsible for an authentic source or by a public sector body that is designated by the Member State to issue such attestations of attributes on behalf of the public sector bodies responsible for authentic sources in accordance with Article 45f and with Annex VII of the Regulation.

### Providers

#### PuB-EAA Provider Role

As specified in the [European Digital Identity Regulation], an attestation may be issued by or on behalf of a public sector body responsible for an Authentic Source. This ARF calls such an attestation a PuB-EAA. A public sector body primarily is a state, regional or local authority, or a body governed by public law.

#### Key Characteristics

- A PuB-EAA Provider, meaning a public sector body issuing PuB-EAAs, is **not a QTSP**
- However, a PuB-EAA Provider has a **qualified certificate, issued by a QTSP**, that allows it to sign PuB-EAAs
- A Relying Party verifies a PuB-EAA by first verifying the signature over the PuB-EAA, and subsequently verifying the signature of the qualified PuB-EAA Provider certificate
- The [European Digital Identity Regulation] stipulates that PuB-EAAs, like QEAAs, have the same legal effect as attestations in paper form
- It is up to the Member States to define terms and conditions for the provisioning of PuB-EAAs, but PuB-EAA Providers will comply with the same technical specifications and standards as Providers of PIDs and other attestations

### Validation Requirements

**OIA_14**: For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a PuB-EAA in accordance with [Art.32](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2594-73-1) of the [European Digital Identity Regulation](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183). For that verification, the Relying Party SHALL use the public key provided in the qualified certificate of the QTSP supporting the qualified signature. The Relying Party SHALL also validate the qualified certificate of the QTSP using a trust anchor provided in a Trusted List made available in accordance with [Art. 22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1) of the European Digital Identity Regulation. The Relying Party SHALL also verify the certified attributes of the qualified certificate, as specified in [Article 45f](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3902-1-1).

**ISSU_09**: After a Wallet Unit receives a PuB-EAA from a PUB-EAA Provider, it SHALL validate the qualified signature of the PuB-EAA in accordance with Art. 32 of the [European Digital Identity Regulation](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183). For that verification, the Wallet Unit SHALL use the public key provided in the qualified certificate of the QTSP supporting the qualified signature. The Wallet Unit SHALL also validate the qualified certificate of the QTSP using a trust anchor provided in a Trusted List made available in accordance with [Art. 22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1) of the European Digital Identity Regulation. Finally, the Wallet Unit SHALL also verify the certified attributes of the qualified certificate, as specified in [Article 45f](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3902-1-1).

### Attestation Rulebook Requirements

**ARB_11**: The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook an attribute as meant in [Annex V](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-54-1) point a) and [Annex VII](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-56-1) point a) of the European Digital Identity Regulation. This attribute SHALL reference the technical specification meant in ARB_25.

**ARB_14**: The Scheme Provider for an attestation Rulebook describing a type of attestation that is a PuB-EAA SHALL include in the Rulebook one or more attributes or metadata representing the set of data meant in [Annex VII](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-56-1) point b) of the European Digital Identity Regulation.

**ARB_16**: The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook one or more attributes representing the set of data meant in [Annex V](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e40-54-1) point c) or [Annex VII](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e46-55-1) point c) of the European Digital Identity Regulation.

### Registration and Trusted Lists

- PuB-EAA Providers must be registered by Registrars in Member States
- PuB-EAA Providers are notified to the Commission and published in PuB-EAA Provider Trusted Lists
- Trust anchors are notified to Commission and published in PuB-EAA Provider Trusted List
- Registration certificates may be issued to PuB-EAA Providers
- PuB-EAA Providers must have access certificates issued by Access Certificate Authorities

#### Revocation and Status Management

For revocation and status management of PuB-EAAs, the revocation mechanism to be used should be specified in the applicable Attestation Rulebook, in accordance with the ARF requirements for Attestation Status List or Attestation Revocation List mechanisms (see VCR_11).

### Catalogue Registration

- The Schema Provider for an Attestation Rulebook that is a QEAA or PuB-EAA SHOULD request the registration of all attributes in that QEAA or PuB-EAA in the catalogue of attributes
- The Schema Provider for an Attestation Rulebook that is a QEAA or PuB-EAA SHOULD register its Rulebook in the catalogue of Attestation Rulebooks
- Attestation schemes for PuB-EAAs may be registered and published in the catalogue of attestation schemes, but this is not mandatory

## Legal and Regulatory References

### Primary Legislation

#### Regulation (EU) 2024/1183 - European Digital Identity Regulation

**Article 45e(2)**
> [...] the Commission shall, taking into account relevant international standards, by means of implementing acts, establish a list of reference standards and, where necessary, establish specifications and procedures for the catalogue of attributes, as well as schemes for the attestation of attributes and verification procedures for qualified electronic attestations of attributes for the purposes of paragraph 1 of this Article.

**Article 45f**
- Defines requirements for PuB-EAAs
- Specifies certified attributes of qualified certificates

**Annex V**
- Requirements for QEAAs
- Point a): Attribute referencing technical specification
- Point b): Set of data to be included
- Point c): Additional attributes

**Annex VI**
- Lists attributes that Member States SHALL request inclusion of in the catalogue of attributes

**Annex VII**
- Requirements for PuB-EAAs
- Point a): Attribute referencing technical specification
- Point b): Set of data to be included
- Point c): Additional attributes

**Article 22**
- Defines Trusted Lists and their publication
- Used for validation of QEAAs and PuB-EAAs

**Article 32**
- Defines validation requirements for qualified signatures

### Implementing Regulation

#### Commission Implementing Regulation (EU) 2025/1569 of 29 July 2025

**Article 7 - Catalogue of Attributes**

**Article 7 paragraph 3**:
> Member States shall request the inclusion of attributes listed in Annex VI to Regulation (EU) No 910/2014 to the catalogue of attributes wherever those attributes rely on authentic sources for the purpose of the verification by qualified trust service providers.

> In addition, Member States may request the inclusion of attributes not listed in Annex VI to the catalogue of attributes wherever those attributes rely on authentic sources within the public sector. Private entities that are considered to be a primary source of information or recognised as authentic in accordance with Union or national law, including administrative practice, may request the inclusion of attributes not listed in Annex VI to the catalogue of attributes wherever the requesting entity is responsible for those attributes.

**Article 8 - Catalogue of Schemes for the Attestation of Attributes**

**Article 8 paragraph 3**:
> Owners of a scheme for the attestation of attributes may request adding schemes to the catalogue of schemes for the attestation of attributes.

## High-Level Requirements

### Topic 12 - Attestation Rulebooks

#### ARB_07
When determining the attributes to be included in a new attestation type, the Scheme Provider for the applicable Attestation Rulebook SHOULD consider referring to attributes that are already included in the catalogue of attributes specified in Topic 25 or specified in an attestation scheme included in the catalogue of attestation schemes specified in Commission Implementing Regulation 2025/1569, rather than unnecessarily re-defining all attributes.

#### ARB_11
The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook an attribute as meant in Annex V point a) and Annex VII point a) of the European Digital Identity Regulation. This attribute SHALL reference the technical specification meant in ARB_25.

#### ARB_12
The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include an attribute in the Rulebook indicating that the attestation is an EAA. This attribute SHALL reference the technical specification meant in ARB_25.

#### ARB_13
The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA SHALL include in the Rulebook one or more attributes or metadata representing the set of data meant in Annex V point b) of the European Digital Identity Regulation.

#### ARB_14
The Scheme Provider for an attestation Rulebook describing a type of attestation that is a PuB-EAA SHALL include in the Rulebook one or more attributes or metadata representing the set of data meant in Annex VII point b) of the European Digital Identity Regulation.

#### ARB_15
The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include in the Rulebook one or more attributes or metadata representing the set of data meant in Annex V point b) of the European Digital Identity Regulation.

#### ARB_16
The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook one or more attributes representing the set of data meant in Annex V point c) or Annex VII point c) of the European Digital Identity Regulation.

#### ARB_33
If a Scheme Provider for an Attestation Rulebook registers an attestation scheme in the catalogue of attestation schemes meant in Commission Implementing Regulation 2025/1569, Article 8, the registration SHALL include a reference to the corresponding Attestation Rulebook. *Note: By definition, an attestation scheme is machine-readable, whereas an Attestation Rulebook is human-readable.*

### Topic 25 - Unified Definition and Controlled Vocabularies for Attributes

#### CAT_04
A request to include or to modify an attribute in the catalogue of attributes SHALL indicate how a QTSP can use the verification point for that attribute. *Note: This could be, for instance, in the form of (a reference to) an endpoint description text.*

### Topic 1 - Accessing Online Services with a Wallet Unit

#### OIA_13
For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a QEAA in accordance with Art.32 of the European Digital Identity Regulation. For the verification, the Relying Party SHALL use a trust anchor provided in a QEAA Provider Trusted List made available in accordance with Art. 22 of the European Digital Identity Regulation.

#### OIA_14
For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a PuB-EAA in accordance with Art.32 of the European Digital Identity Regulation. For that verification, the Relying Party SHALL use the public key provided in the qualified certificate of the QTSP supporting the qualified signature. The Relying Party SHALL also validate the qualified certificate of the QTSP using a trust anchor provided in a Trusted List made available in accordance with Art. 22 of the European Digital Identity Regulation. The Relying Party SHALL also verify the certified attributes of the qualified certificate, as specified in Article 45f.

#### OIA_15
For both proximity and remote presentation flows, a Relying Party SHALL validate the signature of a non-qualified EAA using a trust anchor provided according to the mechanism(s) specified in the applicable Rulebook, see Topic 12.

### Topic 10 - Issuing a PID or Attestation to a Wallet Unit

#### ISSU_08
After a Wallet Unit receives a QEAA from a QEAA Provider, it SHALL validate the qualified signature of the QEAA in accordance with Art.32 of the European Digital Identity Regulation. For the verification, the Wallet Unit SHALL use a trust anchor provided in a QEAA Provider Trusted List made available in accordance with Art. 22 of the European Digital Identity Regulation.

#### ISSU_09
After a Wallet Unit receives a PuB-EAA from a PUB-EAA Provider, it SHALL validate the qualified signature of the PuB-EAA in accordance with Art. 32 of the European Digital Identity Regulation. For that verification, the Wallet Unit SHALL use the public key provided in the qualified certificate of the QTSP supporting the qualified signature. The Wallet Unit SHALL also validate the qualified certificate of the QTSP using a trust anchor provided in a Trusted List made available in accordance with Art. 22 of the European Digital Identity Regulation. Finally, the Wallet Unit SHALL also verify the certified attributes of the qualified certificate, as specified in Article 45f.

#### ISSU_10
After a Wallet Unit receives a non-qualified EAA from an EAA Provider, it SHALL validate the signature of the EAA using a trust anchor provided according to the mechanism(s) specified in the applicable Rulebook, see Topic 12.

#### ISSU_34
A Wallet Unit SHALL authenticate and validate the Attestation Provider access certificate before requesting the issuance of an attestation. The Wallet Unit SHALL verify that the access certificate is authentic and is valid at the time of validation, and that the issuer of the access certificate is a CA that is in an Access Certificate Authority Trusted List, as documented in Topic 27.

#### ISSU_34a
Before requesting the issuance of an attestation, the Wallet Unit SHALL verify that the Attestation Provider is a registered QEAA Provider, PuB-EAA Provider, or EAA Provider. The Wallet Unit SHALL also verify the Provider's sub-entitlements, i.e., whether the Provider properly registered for the issuance of the type of attestation that the User wants to obtain. The Wallet Unit SHALL do these checks using information contained in the Attestation Provider registration certificate, if available in the Credential Issuer metadata of the Attestation Provider. If the registration certificate is not available, the Wallet Unit SHALL use the URL of the Registrar's online service, contained in the Credential Issuer metadata, to obtain such information. If the registered information does not confirm that the Attestation Provider is indeed registered as a QEAA Provider, PuB-EAA Provider, or EAA Provider, or if the registered information does not confirm that the Attestation Provider is registered for the issuance of the type of attestation that the User wants to obtain, the Wallet Unit SHALL NOT request the issuance of the attestation.

### Topic 27 - Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties

#### RPRC_15
The contents of a registration certificate issued to a PID Provider, a QEAA Provider, a PuB-EAA Provider, or a non-qualified EAA Provider SHALL contain the type(s) of attestation that this entity intends to issue to Wallet Units.

### Topic 31 - Notification and Publication

#### RPACANot_03
Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers SHALL ensure that their access certificates can be authenticated using the trust anchors of an Access Certificate Authority notified to the Commission.

#### RPACANot_03a
Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers SHALL ensure that their registration certificates, if issued to them, can be authenticated using the trust anchors of a Provider of registration certificates notified to the Commission.

## Technical Specifications

### TS11 - Interfaces and Formats for Catalogue of Attributes and Catalogue of Schemes

**File**: `technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md`

**Note**: The detailed specification can be found in the standards and technical specifications repository:
- [Specification of interfaces and formats for catalogue of attributes and catalogue of attestations](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md)

This specification defines:
- Interfaces for registering attributes in the catalogue of attributes
- Interfaces for querying the catalogue of attributes
- Interfaces for registering attestation schemes in the catalogue of attestation schemes
- Interfaces for querying the catalogue of attestation schemes
- Formats for machine-readable attestation schemes

## Related Topics and Cross-References

### Topic 12 - Attestation Rulebooks
- Defines requirements for Attestation Rulebooks for QEAAs, PuB-EAAs, and EAAs
- Specifies requirements for referencing catalogues

### Topic 25 - Unified Definition and Controlled Vocabularies for Attributes
- Defines requirements for the catalogue of attributes
- Specifies requirements for attribute registration

### Topic 26 - References to Catalogue of Attestation Rulebooks
- Being updated to reflect the distinction between catalogue of schemes and catalogue of rulebooks

### Topic 27 - Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties
- Defines registration requirements for QEAA Providers, PuB-EAA Providers, and EAA Providers

### Topic 31 - Notification and Publication
- Defines notification requirements for QEAA Providers, PuB-EAA Providers, and EAA Providers
- Specifies Trusted List requirements

### Topic 42 - Requirements for QTSPs to Access Authentic Sources
- Defines how QEAA Providers access authentic sources to verify attributes
- Related to the catalogue of attributes (verification points)

### Section 3.6 - QEAA Providers
- Detailed description of QEAA Provider role and responsibilities

### Section 3.7 - PuB-EAA Providers
- Detailed description of PuB-EAA Provider role and responsibilities

### Section 3.8 - EAA Providers
- Detailed description of EAA Provider role and responsibilities

### Section 5.2.3 - QEAA Definition
- Definition of QEAA in the context of attestations

### Section 5.2.4 - PuB-EAA Definition
- Definition of PuB-EAA in the context of attestations

### Section 5.2.5 - EAA Definition
- Definition of non-qualified EAA in the context of attestations

### Section 5.5 - Catalogue of Attributes and Catalogue of Attestation Schemes
- Comprehensive description of both catalogues

### Section 6.6.3.6 - Relying Party Verifies Authenticity
- Validation procedures for QEAAs, PuB-EAAs, and EAAs

## Important Notes and Distinctions

### Scheme vs. Rulebook
- **Scheme for the attestation of attributes** = Machine-readable attestation definition
- **Attestation Rulebook** = Human-readable specification of the scheme

### Catalogue Terminology
- The term "catalogue of published Attestation Rulebooks" should be rephrased to "catalogue of schemes for the attestation of attributes"
- The ARF includes high-level requirements (HLR) for these catalogues, which are considered outdated and will be updated (see Discussion Paper Topic O, Section 3)

### Trust Model
- PID Providers, QEAA Providers, and PuB-EAA Providers have trust anchors in Commission-compiled Trusted Lists
- Non-qualified EAA Providers may have trust anchors through mechanisms specified in applicable Rulebook
- QEAA Providers and PuB-EAA Providers operate within a regulated framework and are regularly audited
- Non-qualified EAA Providers are also regulated under Regulation (EU) 2024/1183 (see Article 19a, Article 45h, Commission Implementing Regulation (EU) 2025/2160, and Commission Implementing Regulation (EU) 2024/2977), but operate under a different level of trust compared to QEAAs and PuB-EAAs

### Using Trusted Lists to configure allowed Credential Issuers for specific attestation types

- **Purpose**: Trusted Lists and registration certificates together can be used to configure which Credential Issuers are allowed to issue specific **attestation types**, even though any entity could technically sign arbitrary data.
- **Trusted List Owner**:
  - Each Trusted List has a **Trusted List Owner** (also known as **Ecosystem Authority** or **Scheme Owner**). The Trusted List Owner is accountable for allowing the listed EAA Providers (also known as **Trusted Entities**) to issue credentials that are mentioned in the metadata of the Trusted List.
  - A Trusted List Owner can list multiple attribute schemes. The listed EAA Providers are allowed to issue all attribute schemes that are listed. It is recommended to set up 1 Trusted List per attribute scheme.
  - A Trusted List Owner can list itself as an EAA Provider.
  - The Wallet and Relying Party must trust the Trusted List Owner to accept the credential. Wallet Providers MAY configure the verification component in their Wallet Solutions as follows:
    - European Commission is trusted per default
    - PID-Provider, QEAA and PuB-EAA are trusted as referenced in the European Commission's Trusted List
    - Wallet users will receive an alert if a Trusted List Owner is unknown and MAY be able to configure Trusted List Owner as being trusted

- **Registration certificate as source of truth** (when available):
  - As specified in the ARF (Topic 27 and the registration certificate requirements, e.g. RPRC_15), a **registration certificate** issued to a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider **SHALL contain the type(s) of attestation that this entity intends to issue to Wallet Units**.
  - However, registration certificates are **optional** - they are issued "if the Registrar has a policy of issuing such certificates" (ARF Section 6.3.2.2).
  - When a registration certificate is available, it is referenced from the Trusted List entry or from an associated Registrar service.
  - It is suggested to add a field called `registrationCertificateHash` (for example) in the Trusted List entry, which would provide the certificate hash in cases where the certificate URL is provided.
- **Trusted List entry for each provider**:
  - For each Provider role (PID, QEAA, PuB-EAA, EAA), the Trusted List includes the **trust anchor** (public key / certificate) and **metadata** that links the Provider to its registration information.
  - This metadata can either:
    - Contain a **machine-readable list of allowed attestation type identifiers / namespaces** directly (making the TL entry self-contained), or
    - Contain a **pointer (URL, reference, identifier)** to the Provider's registration certificate or Registrar API, where the list of allowed attestation types is maintained.
- **Self-contained Trusted List entries**:
  - **Yes, Trusted List entries can be sufficient on their own** without requiring a separate registration certificate.
  - If the `allowedAttestationType` list is embedded directly in the Trusted List entry's `serviceInformationExtensions`, Wallet Units and Relying Parties can perform validation using only the Trusted List, without needing to retrieve a registration certificate.
  - This approach is simpler and reduces dependencies, but may be less flexible for frequent updates or detailed provider information.
  - The ARF specifies that when registration certificates are not available, Wallet Units should use the Registrar's online service URL (ISSU_34a), but a self-contained Trusted List entry with embedded `allowedAttestationType` values would also satisfy this requirement.
- **Wallet and Relying Party behaviour**:
  - When a Wallet Unit or Relying Party receives a credential, it:
    1. Reads the **attestation type identifier / namespace** from the credential.
    2. Identifies the **issuer** from the credential’s signing certificate and locates the corresponding **Trusted List entry**.
    3. From the Trusted List entry (or the referenced registration certificate / Registrar API), obtains the list of **attestation types the issuer is authorised to issue**.
    4. **Accepts** the credential as being of that attestation type **only if**:
       - The issuer is present in the applicable Trusted List, and
       - The attestation type in the credential is listed in the issuer’s authorised types.
  - This means another issuer can technically issue a syntactically similar credential, but compliant Wallets and Relying Parties **will not treat it as that “exclusive” credential type**, because the Trusted List / registration data will not list that type for the other issuer.
- **Relation to catalogue entries**:
  - The **catalogue of attributes** and **catalogue of attestation schemes** define **what** credential types and attributes exist and how they are structured.
  - Trusted Lists and registration certificates define **who** is allowed to issue which of those types.
  - Together, catalogues + Trusted Lists provide a way to establish that certain credential types are **exclusively associated with specific, authorised Credential Issuers**.

#### Non-normative examples of Trusted List entries

The following examples are **illustrative only** and do not prescribe a specific ETSI TL encoding, but show how information could be structured conceptually.

- **Example 1 – QEAA Provider authorised for PID and tax-residency attestations**

  For each TL service entry:

  - `serviceTypeIdentifier` = `QEAAProvider`
  - `serviceInformationExtensions`:
    - `allowedAttestationType`: `eu.europa.ec.eudi.pid.1`
    - `allowedAttestationType`: `eu.europa.ec.eudi.tax-residency.1`
    - `registrationCertificateRef`: `<URL or hash of the registration certificate>`
    - `registrationCertificateHash`: `<hash of the registration certificate>` (optional, suggested when URL is provided)

- **Example 2 – PuB-EAA Provider authorised only for a specific public-sector entitlement**

  For each TL service entry:

  - `serviceTypeIdentifier` = `PuBEAAProvider`
  - `serviceInformationExtensions`:
    - `allowedAttestationType`: `eu.europa.ec.eudi.public-benefit.1`
    - `registrationCertificateRef`: `<URL or hash of the registration certificate>`
    - `registrationCertificateHash`: `<hash of the registration certificate>` (optional, suggested when URL is provided)

- **Example 3 – Non-qualified EAA Provider with sectoral attestation types**

  For each TL service entry:

  - `serviceTypeIdentifier` = `EAAProvider`
  - `serviceInformationExtensions`:
    - `allowedAttestationType`: `eu.europa.ec.eudi.university-degree.1`
    - `allowedAttestationType`: `eu.europa.ec.eudi.professional-licence.1`
    - `registrationCertificateRef`: `<URL or hash of the registration certificate>`
    - `registrationCertificateHash`: `<hash of the registration certificate>` (optional, suggested when URL is provided)

**Note on registration certificates**: The `registrationCertificateRef` field is **optional**. If the `allowedAttestationType` list is embedded directly in the Trusted List entry, the entry is **self-contained** and sufficient for validation without retrieving a separate registration certificate.

In all cases, Wallet Units and Relying Parties would:

1. Read the `serviceTypeIdentifier` and confirm that the issuer plays the expected role (QEAAProvider / PuBEAAProvider / EAAProvider).
2. Check that the `allowedAttestationType` list contains the attestation type found in the credential.
3. If `registrationCertificateRef` is present, optionally follow it to retrieve the full registration certificate, which SHOULD list the same attestation types as part of the provider's authorisation. If `registrationCertificateRef` is absent, the Trusted List entry alone is sufficient for validation.

**Example 4 – Self-contained Trusted List entry (without registration certificate reference)**

For a TL service entry that is self-contained:

- `serviceTypeIdentifier` = `QEAAProvider`
- `serviceInformationExtensions`:
  - `allowedAttestationType`: `eu.europa.ec.eudi.pid.1`
  - `allowedAttestationType`: `eu.europa.ec.eudi.tax-residency.1`
  - *(No `registrationCertificateRef` field - the TL entry is self-contained)*

In this case, Wallet Units and Relying Parties can validate credentials using only the Trusted List entry, without needing to retrieve any additional registration certificate or query a Registrar service.

### Registration vs. Notification
- **Registration**: Entities are registered by Registrars in Member States
- **Notification**: Registered entities are notified to the Commission and published in Trusted Lists

### Catalogue Registration
- Registration in catalogues is **not mandatory** for QEAAs and PuB-EAAs. *This is stated in the ARF main document at Section 5.5.*
- **Registration is mandatory for Non-Qualified EAAs** to guarantee interoperability and quality standardization on the attestation issuance and its content
- Registration does not create any obligation for acceptance of the relevant type of attestation. *This is stated in the ARF main document at Section 5.5.*
- Registration does not automatically imply cross-border recognition

## References

### Legal Documents
- [European Digital Identity Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183)
- [Commission Implementing Regulation (EU) 2025/1569](http://data.europa.eu/eli/reg_impl/2025/1569/oj)
- [Regulation (EU) No 910/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0910) (eIDAS Regulation)

### Technical Documents

**Note**: The following documents are part of the EUDI Wallet Architecture and Reference Framework repository, not this repository. They are referenced here for completeness.

- [Technical Specification 11](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md) - Located in the EUDI Wallet Standards and Technical Specifications repository
- [Discussion Paper on Topic O](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/discussion-topics/o-catalogues-for-attestations.md) - Located in the EUDI Wallet Architecture and Reference Framework repository
- Credential Catalogue Information - Referenced in the EUDI Wallet Architecture and Reference Framework

### Architecture Documents

**Note**: The following documents are part of the EUDI Wallet Architecture and Reference Framework repository, not this repository.

- [Architecture and Reference Framework Main Document](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md) - Located in the EUDI Wallet Architecture and Reference Framework repository
- [Annex 2.02 - High-Level Requirements by Topic](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md) - Located in the EUDI Wallet Architecture and Reference Framework repository

## Document History

- **Created**: Based on comprehensive search of the EUDI Wallet Architecture and Reference Framework
- **Sources**: All files in the `docs/` directory
- **Last Updated**: Based on current state of the repository

