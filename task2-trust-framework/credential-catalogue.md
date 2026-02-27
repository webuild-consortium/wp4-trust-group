# Credential Catalogue: Catalogue of Attributes and Catalogue of Attestation Schemes

This document compiles evidence, references, and specifications for the EUDI Wallet **catalogue of attributes** and **catalogue of attestation schemes**, as defined in the Architecture and Reference Framework (ARF) v2.8.0 and Commission Implementing Regulation (EU) 2025/1569.

For Trusted List extensions used to configure which Credential Issuers are authorised to issue specific attestation types, see [trusted-list-extensions-credential-issuers.md](https://github.com/webuild-consortium/wp4-trust-group/blob/main/task3-x509-pki-etsi/trusted-list-extensions-credential-issuers.md).

## Glossary and Definitions

**Entity and trust terminology**: See [terms-and-entities.md](https://github.com/webuild-consortium/wp4-trust-group/blob/main/task1-use-cases/terms-and-entities.md).

**Catalogue and attestation concepts**: See [ARF v2.8.0 Section 5.5](https://eudi.dev/2.8.0/architecture-and-reference-framework-main/#55-catalogue-of-attributes-and-catalogue-of-attestation-schemes) and [Technical Specification 11](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md).

## Credential Catalogues Overview

### Definition

The EUDI Wallet ecosystem defines **two distinct catalogues** to support discovery and interoperability:

1. **Catalogue of attributes** - For QTSPs to find verification points
2. **Catalogue of attestation schemes** (also called "catalogue of schemes for the attestation of attributes") - For discovering attestation types

### Key Documents

#### Main Architecture Document (ARF v2.8.0)
- [Section 5.5 - Catalogue of attributes and catalogue of attestation schemes](https://eudi.dev/2.8.0/architecture-and-reference-framework-main/#55-catalogue-of-attributes-and-catalogue-of-attestation-schemes)

#### Discussion Paper
- [Topic O - Catalogues for Attestations](https://eudi.dev/2.8.0/discussion-topics/o-catalogues-for-attestations/) (Version 1.0, updated 29 Sep 2025)
- [GitHub Discussion](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/discussions/557)

#### Technical Specification
- [Technical Specification 11 - Interfaces and formats for catalogue of attributes and catalogue of schemes](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md)

#### Requirements Documents (ARF v2.8.0 Annex 2.02)
- [Topic 25 - Unified definition and controlled vocabularies for attributes](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2315-topic-25---unified-definition-and-controlled-vocabularies-for-attributes)
- Topic 26 (References to catalogue of Attestation Rulebooks) has been removed in ARF v2.8.0; see [Discussion Paper Topic O](https://eudi.dev/2.8.0/discussion-topics/o-catalogues-for-attestations/) Section 3.2.

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

*ARF v2.8.0 Section 5.5.2*

### Scope

- Limited to attributes that rely on **authentic sources within the public sector**
- Primary objective: **discovery of verification points**
- Only **specific types of entities** can add or modify entries

### Key Characteristics

Per CIR 2025/1569 Article 7 and ARF Section 5.5.2: publicly available, machine-readable, Commission-run catalogue. Contents available in both human and machine-readable formats.

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

From **Topic 25** (ARF v2.8.0 Annex 2.02; former catalogue HLRs have been removed per Discussion Paper Topic O):

| **Index** | **Requirement Specification** |
|-----------|-------------------------------|
| CAT_04 | A request to include or to modify an attribute in the catalogue of attributes SHALL indicate how a QTSP can use the verification point for that attribute. *Note: This could be, for instance, in the form of (a reference to) an endpoint description text.* |

### Maintenance and Availability

Per ARF Section 5.5.2 and CIR 2025/1569 Article 7, the catalogue of attributes will be established and maintained by the Commission. The Commission will make the existence and maintenance publicly available, including processes for proposing registration, registering attributes, and conditions for updating or removing attributes.

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

From **Topic 12** (Attestation Rulebooks, ARF v2.8.0 Annex 2.02):

| **Index** | **Requirement Specification** |
|-----------|-------------------------------|
| ARB_07 | When determining the attributes to be included in a new attestation type, the Scheme Provider for the applicable Attestation Rulebook SHOULD consider referring to attributes that are already included in the catalogue of attributes specified in Topic 25 or specified in an attestation scheme included in the catalogue of attestation schemes specified in Commission Implementing Regulation 2025/1569, rather than unnecessarily re-defining all attributes. |
| ARB_33 | If a Scheme Provider for an Attestation Rulebook registers an attestation scheme in the catalogue of attestation schemes meant in Commission Implementing Regulation 2025/1569, Article 8, the registration SHALL include a reference to the corresponding Attestation Rulebook. *Note: By definition, an attestation scheme is machine-readable, whereas an Attestation Rulebook is human-readable.* |

### Maintenance and Availability

Per ARF Section 5.5.3 and CIR 2025/1569 Article 8, the Commission will take measures to establish and maintain the catalogue of attestation schemes. The catalogue will be publicly accessible. It may be hosted by the Commission or parts may be referenced to other catalogues. The Commission may delegate maintenance to sector-specific authorities at EU or national level.

### Publication Process

An Attestation Scheme Provider may publish a new attestation in the **catalogue of attestation schemes** to enable discovery by Relying Parties and other actors. When doing so, the provider **also supplies the machine-readable attestation scheme** in accordance with Technical Specification 11.

### Important Distinctions

#### Scheme vs. Rulebook
- **Scheme for the attestation of attributes** = Machine-readable attestation definition that describes the formal structure (data content descriptive structure)
- **Attestation Rulebook** = Human-readable specification of the scheme that focuses on significance and data quality assurance that should be assured as a minimum requirement by the attestation issuer (substantial requirements)

**Note**: While the scheme defines the formal structure, the rulebook focuses on substantial requirements (ARF Section 5.4, Discussion Paper Topic O).

#### Two Catalogues Serve Different Purposes

| Aspect | Catalogue of Attributes | Catalogue of Attestation Schemes |
|--------|------------------------|----------------------------------|
| **Primary Users** | QTSPs issuing QEAAs | Relying Parties, Attestation Providers, other actors |
| **Purpose** | Find verification points for attributes | Discover attestation types and understand attributes |
| **Scope** | Limited to attributes from authentic public-sector sources | Broader - any scheme owner can register |
| **Who Can Register** | Specific entities (Member States, certain private entities) | Any scheme owner |
| **Mandatory Registration** | N/A | Not mandatory for QEAAs/PuB-EAAs |

## EAA Types and Catalogue Registration

### EAA (Electronic Attestation of Attributes)

An **Electronic Attestation of Attributes (EAA)** can be issued in three forms:

1. **QEAA** (Qualified Electronic Attestation of Attributes)
2. **PuB-EAA** (Public Sector EAA)
3. **Non-Qualified EAA** (EAA which is not a QEAA or a PuB-EAA)

See [terms-and-entities.md](https://github.com/webuild-consortium/wp4-trust-group/blob/main/task1-use-cases/terms-and-entities.md) for entity definitions.

### Catalogue Registration by EAA Type

- **QEAA/PuB-EAA**: Attestation schemes for QEAAs and PuB-EAAs **may** be registered and published in the catalogue of attestation schemes, but this is **not mandatory** (ARF Section 5.5.3). Attributes may be registered in the catalogue of attributes by the entities specified in CIR 2025/1569 Article 7 (Member States, certain private entities).
- **Non-qualified EAA**: Registration and publication in the catalogue of attestation schemes is **not mandatory** (ARF Section 5.5.3). Provider registration (with Member State Registrar and inclusion in national EAA Provider Trusted Lists) **is** required for participation.

### Catalogue Registration Principles

- Registration in catalogues is **not mandatory** for QEAAs and PuB-EAAs (ARF v2.8.0 Section 5.5.3).
- Registration does not create any obligation for acceptance of the relevant type of attestation by any actor. Neither does it automatically imply cross-border recognition (ARF v2.8.0 Section 5.5.3).

### Catalogue Terminology

- The term "catalogue of published Attestation Rulebooks" is being rephrased to "catalogue of schemes for the attestation of attributes" (Discussion Paper Topic O Section 3.3)
- ARF v2.8.0 has incorporated the changes discussed in [Discussion Paper Topic O](https://eudi.dev/2.8.0/discussion-topics/o-catalogues-for-attestations/): the former HLRs in Topics 25 and 26 have been removed; Topic 25 now contains only CAT_04 (verification point for attributes), and Topic 26 has been removed.

## Legal and Regulatory References

### Primary Legislation

#### Regulation (EU) 2024/1183 - European Digital Identity Regulation

**Article 45e(2)**
> [...] the Commission shall, taking into account relevant international standards, by means of implementing acts, establish a list of reference standards and, where necessary, establish specifications and procedures for the catalogue of attributes, as well as schemes for the attestation of attributes and verification procedures for qualified electronic attestations of attributes for the purposes of paragraph 1 of this Article.

**Annex VI**
- Lists attributes that Member States SHALL request inclusion of in the catalogue of attributes

### Implementing Regulation

#### Commission Implementing Regulation (EU) 2025/1569 of 29 July 2025

**Article 7 - Catalogue of Attributes**

**Article 7 paragraph 3**:
> Member States shall request the inclusion of attributes listed in Annex VI to Regulation (EU) No 910/2014 to the catalogue of attributes wherever those attributes rely on authentic sources for the purpose of the verification by qualified trust service providers.

> In addition, Member States may request the inclusion of attributes not listed in Annex VI to the catalogue of attributes wherever those attributes rely on authentic sources within the public sector. Private entities that are considered to be a primary source of information or recognised as authentic in accordance with Union or national law, including administrative practice, may request the inclusion of attributes not listed in Annex VI to the catalogue of attributes wherever the requesting entity is responsible for those attributes.

**Article 8 - Catalogue of Schemes for the Attestation of Attributes**

**Article 8 paragraph 3**:
> Owners of a scheme for the attestation of attributes may request adding schemes to the catalogue of schemes for the attestation of attributes.

## Technical Specifications

### TS11 - Interfaces and Formats for Catalogue of Attributes and Catalogue of Schemes

**Note**: The detailed specification can be found in the standards and technical specifications repository:
- [Technical Specification 11](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md)

This specification defines:
- Interfaces for registering attributes in the catalogue of attributes
- Interfaces for querying the catalogue of attributes
- Interfaces for registering attestation schemes in the catalogue of attestation schemes
- Interfaces for querying the catalogue of attestation schemes
- Formats for machine-readable attestation schemes

## Related Topics and Cross-References (ARF v2.8.0)

- [Topic 12 - Attestation Rulebooks](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a239-topic-12---attestation-rulebooks)
- [Topic 25 - Unified definition and controlled vocabularies for attributes](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2315-topic-25---unified-definition-and-controlled-vocabularies-for-attributes)
- Topic 26 - Removed in ARF v2.8.0; see [Discussion Paper Topic O](https://eudi.dev/2.8.0/discussion-topics/o-catalogues-for-attestations/) Section 3.2.
- [Topic 42 - Requirements for QTSPs to Access Authentic Sources](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2324-topic-42---requirements-for-qtsps-to-access-authentic-sources) - Related to the catalogue of attributes (verification points)

## References

### Legal Documents
- [European Digital Identity Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183)
- [Commission Implementing Regulation (EU) 2025/1569](http://data.europa.eu/eli/reg_impl/2025/1569/oj)
- [Regulation (EU) No 910/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0910) (eIDAS Regulation)

### Architecture Documents (ARF v2.8.0)
- [Architecture and Reference Framework Main Document - Section 5.5](https://eudi.dev/2.8.0/architecture-and-reference-framework-main/#55-catalogue-of-attributes-and-catalogue-of-attestation-schemes)
- [Annex 2.02 - High-Level Requirements by Topic](https://eudi.dev/2.8.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/)
- [Discussion Paper on Topic O](https://eudi.dev/2.8.0/discussion-topics/o-catalogues-for-attestations/)
