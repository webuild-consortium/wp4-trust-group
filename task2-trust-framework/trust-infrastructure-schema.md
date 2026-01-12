# Trust Infrastructure Schema: Onboarding and Trusted Lists

This document provides a comprehensive schema and graphical representation of the EUDI Wallet trust infrastructure, focusing on two main processes: **Onboarding** (Registration) and **Trusted List Publication**. These processes are separated to align with the Architecture and Reference Framework (ARF).

## Overview

The trust infrastructure consists of two distinct but related processes:

1. **Registration/Onboarding**: Entities register with Registrars, providing identification data and entitlements. According to the ARF (Section 3.17), entities (PID Providers, Attestation Providers, Relying Parties) are registered by a Registrar in the Member State where they reside. The ARF states that "Member States establish and oversee Registrars" and that "the process and terms and conditions for registering will be determined by each Member State." While the ARF consistently refers to "Member State Registrars" and does not explicitly mention sector-specific or European Commission-level Registrars, it does not explicitly rule them out either. **Note**: Wallet Providers register with a Trusted List Provider (TLP), not with a Registrar (per ARF Section 6.2.2).
2. **Trusted List Publication**: Member State Trusted List Providers (TLPs) compile, sign, and publish Trusted Lists per Member State for PID Providers, Attestation Providers, Access CAs, and Registration Cert Providers, then submit Trusted List URLs to the European Commission. For Wallet Providers, Member States notify Wallet Providers to the Commission, and the Commission compiles, signs/seals, and publishes a single EU-wide Wallet Provider Trusted List. The Commission maintains the List of Trusted Lists (LoTL) containing pointers to all published Trusted Lists. While the ARF does not explicitly specify the organizational level of Trusted List Providers, the notification requirements (GenNot_01) indicate that Member States notify entities to the Commission, suggesting TLPs operate at Member State level.

Both processes are required to establish the trust infrastructure in the EUDI Wallet ecosystem.

**Submission and Update Process**: The relationship between Registration and Trusted List Publication operates through the submission and update process between the Member State Registrar and the Trusted List Provider (TLP). Upon successful registration, the Registrar triggers the TLP to compile, sign, and publish Trusted Lists (for PID Providers, Attestation Providers, Access CAs, Registration Cert Providers). The TLP then submits the Trusted List URL to the European Commission. **Note**: Wallet Providers register directly with the TLP in their Member State, the Member State notifies Wallet Providers to the Commission, and the Commission compiles and publishes the EU-wide Wallet Provider Trusted List directly (no URL submission by TLP). See [Section 5.3.1](#531-submission-and-update-models-registration-to-trusted-list) for detailed submission and update models.

## 1. Trust Infrastructure Architecture

### 1.1 Trust Infrastructure Authorities

The trust infrastructure is operated by the following authorities and entities:

- **Registrar**: Manages registration of entities (PID Providers, Attestation Providers, Relying Parties). According to the ARF (Section 3.17), entities are registered by a Registrar in the Member State where they reside. The ARF states that "Member States establish and oversee Registrars" and that "the process and terms and conditions for registering will be determined by each Member State." While the ARF consistently refers to Member State-level Registrars, it does not explicitly specify whether Registrars can be sector-specific or established at European Commission level. Note: Wallet Providers register with a Trusted List Provider, not with a Registrar (per ARF Section 6.2.2).
- **Access Certificate Authority**: Issues access certificates to registered entities (PID Providers, Attestation Providers, Relying Parties). Note: Wallet Providers do not receive access certificates as they register with TLP, not with Registrar.
- **Provider of Registration Certificates**: Optionally issues registration certificates detailing entitlements.
- **Trusted List Provider (TLP)**: Compiles, signs, and publishes Trusted Lists for entities (PID Providers, Attestation Providers, Access CAs, Registration Cert Providers) per Member State, and submits Trusted List URLs to the European Commission. The ARF does not explicitly specify whether the TLP must be a Member State entity, a sector-specific body, or the European Commission itself. However, the notification process (GenNot_01) requires Member States to notify entities to the Commission, suggesting the TLP operates at Member State level. **Note**: Wallet Provider Trusted Lists are compiled and published by the European Commission, not by Member State TLPs.
- **European Commission**: Receives Trusted List URL notifications from Member State TLPs (for PID Providers, Attestation Providers, Access CAs, Registration Cert Providers), verifies Trusted Lists, compiles and publishes the Wallet Provider Trusted List (EU-wide), and compiles, signs, and publishes the List of Trusted Lists (LoTL).

### 1.2 Registered Entities

The following entities register with Registrars and participate in the trust infrastructure:

- **PID Providers**: Issue Person Identification Data. PID Providers must be approved by Member States according to a well-defined policy before registration (per **Reg_19**, [Topic 27](https://eudi.dev/2.7.3/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)). Member States define specific vetting processes and rules of acceptance for inclusion in the PID Provider Registry. This is a policy-based approval process, not a technical certification like Wallet Solutions.
- **Attestation Providers**: QEAA Providers, PuB-EAA Providers, EAA Providers.
- **Relying Parties (RP)**: Request attributes from Wallet Units.

**Note**: Wallet Providers register with a Trusted List Provider (TLP), not with a Registrar (per [ARF Section 6.2.2](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#622-wallet-provider-registration-and-notification)). Wallet Solutions must be certified by Conformity Assessment Bodies (CABs) according to [Commission Implementing Regulation (EU) 2024/2981](https://eur-lex.europa.eu/eli/reg_impl/2024/2981/oj) (per [ARF Chapter 7](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#7-certification-and-risk-management)). Certification is performed against national certification schemes (transitory) and eventually a harmonized scheme under the [Cybersecurity Act (CSA)](https://eur-lex.europa.eu/eli/reg/2019/881/oj) (Regulation (EU) 2019/881), at assurance level High. See [Section 2.1.1](#211-wallet-provider-registration) for details.

## 2. Registration/Onboarding Process

The registration process is managed by Member State Registrars and involves (for PID Providers, Attestation Providers, and Relying Parties):

1. Entity registration with identification data and entitlements.
2. Access certificate issuance by Access Certificate Authority.
3. Optional registration certificate issuance by Provider of Registration Certificates.
4. Registry publication for transparency and online verification (per **Reg_03**, **Reg_04**). The registry is always published for all registered entities (PID Providers, Attestation Providers, Relying Parties) and serves as an alternative source when registration certificates are not available. Member States SHALL support the common API specified in [Technical Specification 5](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) for automated retrieval of registry entries (per **Reg_06**, Topic 27). The API uses a secure channel and does not require authentication. Wallet Units use the Registrar's online service URL to verify:
   - PID Provider registration (per **ISSU_24a**).
   - Attestation Provider registration and attestation types (per **ISSU_34a**).
   - Relying Party registration and requested attributes (per **RPRC_18**).

### 2.1 Registration Flow

Entities register with their Member State Registrar before participating in the ecosystem. The common set of data to be registered is specified in [ARF Section 6.3.2.2](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#6322-data-about-the-pid-provider-or-attestation-provider-is-included-in-the-registry) and [Section 6.4.2](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#642-relying-party-registration), and detailed in [Technical Specification 6](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md) per requirement **Reg_01a** (Topic 27).

The registration data includes:

- **Identification data**: Name, country, business registration number (as applicable).
- **Entitlements**:
  - **For PID Providers**: Attestation type(s) that the Provider intends to issue to Wallet Units (e.g., national PID).
  - **For QEAA Providers**: Attestation type(s) that the Provider intends to issue to Wallet Units (e.g., diplomas, professional qualifications).
  - **For PuB-EAA Providers**: Attestation type(s) that the Provider intends to issue to Wallet Units (e.g., mDLs, vehicle registration cards).
  - **For non-qualified EAA Providers**: Attestation type(s) that the Provider intends to issue to Wallet Units.
  - **For Relying Parties**: Attributes that the Relying Party intends to request from Wallet Units, and for what purpose (intended use). The Registrar also registers if the Relying Party intends to use the services of an intermediary, and if so, which one.
- **Service supply points**: URLs where services are available (e.g., PID issuance endpoint, attestation issuance endpoint, presentation request endpoint).

#### 2.1.1 Wallet Provider Registration

Wallet Providers register with a Trusted List Provider (TLP) in their Member State, not with a Registrar (per [ARF Section 6.2.2](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#622-wallet-provider-registration-and-notification)). The information to be notified about Wallet Providers is specified in **WPNot_01** and **WPNot_02** (Topic 31). The notification includes:

- **Identification data**: Member State/Country of establishment, name as registered in an official record, business registration number (where applicable).
- **Wallet Provider trust anchors**: Public keys and name supporting the authentication of Wallet Unit Attestations (WUA) issued by the Wallet Provider (per **WPNot_02**).

Note: Wallet Providers do not receive access certificates or registration certificates, as they do not register with a Registrar. The Wallet Solution provided by the Wallet Provider must be certified as described in [ARF Chapter 7](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#7-certification-and-risk-management).

> **Note**: Wallet Providers follow a different registration process than other entities. They register with a Trusted List Provider (TLP), not with a Registrar, and do not receive access certificates or registration certificates. The notification process (per **WPNot_01**, **WPNot_02**) involves providing Trust Anchors for WUA authentication, which are published in the Wallet Provider Trusted List.

### 2.2 Access Certificate Issuance

After registration, the Access Certificate Authority issues access certificates to registered entities (PID Providers, Attestation Providers, Relying Parties). Note: Wallet Providers do not receive access certificates as they register with TLP, not with Registrar. These certificates:
- Enable authentication during service interactions.
- Reference the registry for entitlement verification.
- Include Signed Certificate Timestamps (SCT) for Certificate Transparency.

### 2.3 Registration Certificate Issuance (Optional)

If the Registrar policy requires it, the Provider of Registration Certificates issues registration certificates that:
- Detail the entity's registration status.
- Specify entitlements (attestation types for Credential Issuers, attributes for Relying Parties).
- Enable Wallet Units to verify entity entitlements.

Registration certificates are issued per:
- **RPRC_09**: For Relying Parties (Registrar MAY decide to issue registration certificates to Relying Parties).
- **RPRC_13**: For Credential Issuers (PID Providers, Attestation Providers) (Registrar MAY decide to issue registration certificates to Providers).

> **Note**: Wallet Providers do not receive registration certificates unless they are also acting as Relying Parties. In that case, they would receive registration certificates per **RPRC_09** for their Relying Party role, not per **RPRC_13**.

## 3. Trusted List Publication Process

The Trusted List publication process is separate from registration and involves:

1. **For PID Providers, Attestation Providers, Access CAs, Registration Cert Providers**: Member State Trusted List Provider (TLP) compiles, signs, and publishes Trusted Lists per Member State, then submits Trusted List URL to European Commission.
2. **For Wallet Providers**: Member States notify Wallet Providers to the European Commission, and the Commission compiles, signs/seals, and publishes a single EU-wide Wallet Provider Trusted List.
3. Commission verifies and maintains the List of Trusted Lists (LoTL) containing pointers to all published Trusted Lists.
4. Commission signs and publishes the LoTL.

### 3.1 Trusted List Publication by Trusted List Provider

> **Note on Trusted List Provider Organizational Level**: The ARF ([Section 3.5](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#35-trusted-list-provider)) defines a Trusted List Provider (TLP) as "a body responsible for maintaining, managing, and publishing a Trusted List" but does not explicitly specify whether the TLP must be a Member State entity, a sector-specific body, or the European Commission itself. However, the notification requirements (GenNot_01) state that "Member States SHALL notify" entities to the Commission, and [Section 3.5](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#35-trusted-list-provider) states that "relevant entities must be notified to the Commission by a Member State." This suggests that TLPs operate at Member State level, though the ARF does not explicitly rule out other organizational models. There is also an inconsistency in the ARF itself ([Section 6.3.2](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification)) where line 2838 states that "A PID Provider or an Attestation Provider is registered by a Trusted List Provider" while line 2851 states that entities "register itself with a Registrar," regarding whether entities are registered by a TLP or by a Registrar.

The Trusted List Provider (TLP) is responsible for:

1. **Compiling Trusted Lists**: The TLP compiles Trusted Lists per entity type from registered entities:
   - PID Providers (with trust anchors for PID signature verification)
   - Attestation Providers (PuB-EAA Providers with conformity assessment reports)
   - Access Certificate Authorities (with trust anchors for access certificate verification)
   - Providers of Registration Certificates (with trust anchors for registration certificate verification)

**Note**: Wallet Provider Trusted Lists are compiled and published by the European Commission, not by Member State TLPs. Member States notify Wallet Providers to the Commission (per **WPNot_01**, **WPNot_02**), and the Commission compiles, signs/seals, and publishes a single EU-wide Wallet Provider Trusted List (per **WPNot_04**, **WPNot_05**). Per [ETSI TS 119 602 Annex E](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf), the Scheme Territory for the Wallet Provider Trusted List is "EU", indicating it is a single EU-wide list containing all Wallet Providers from all Member States, not separate lists per Member State. This is different from other Trusted Lists (PID Provider, Attestation Provider, Access CA, Registration Cert Provider) where Member State TLPs compile, sign, and publish separate Trusted Lists per Member State, then submit TL URLs to the Commission.

2. **Signing Trusted Lists**: The TLP signs/seals the Trusted Lists using its signing key (for PID Providers, Attestation Providers, Access CAs, and Registration Cert Providers). **Note**: Wallet Provider Trusted Lists are signed/sealed by the European Commission, not by Member State TLPs.

3. **Publishing Trusted Lists**: The TLP publishes the signed Trusted Lists in machine-readable and human-readable formats at a publicly accessible URL (for PID Providers, Attestation Providers, Access CAs, and Registration Cert Providers). **Note**: Wallet Provider Trusted Lists are published by the European Commission, not by Member State TLPs. Per [ETSI TS 119 602 V1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf) (Data model for Lists of Trusted Entities), the format requirements are:
   - **Wallet Provider Trusted Lists** (Annex E, published by EC): Must be published in **JSON format with compact JAdES Baseline B signature** (per ETSI TS 119 182-1).
   - **PID Provider Trusted Lists** (Annex D, published by MS TLP): Must be published in **JSON format with compact JAdES Baseline B signature** (per ETSI TS 119 182-1).
   - **Access CA Trusted Lists** (Annex F - WRPAC Providers, published by MS TLP): Must be published in **JSON format with compact JAdES Baseline B signature** (per ETSI TS 119 182-1).
   - **Registration Cert Provider Trusted Lists** (Annex G - WRPRC Providers, published by MS TLP): Must be published in **JSON format with compact JAdES Baseline B signature** (per ETSI TS 119 182-1).
   - **Pub-EAA Provider Trusted Lists** (Annex H, published by MS TLP): May be published in either **JSON format with compact JAdES Baseline B signature** OR **XML format with XAdES Baseline B signature** (per ETSI EN 319 132-1). When XML is used, it must be an enveloped digital signature.

All Trusted Lists must comply with ETSI TS 119 602 data model and the specific profiles defined in the annexes, or with ETSI TS 119 612 v2.1.1 or a suitable profile derived from ETSI TS 102 231 (per **WPNot_05**, **PPNot_07**, **PuBPNot_03**, **RPACANot_05**).

4. **Submitting to European Commission**: The TLP submits the published Trusted List URL to the European Commission (for PID Providers, Attestation Providers, Access CAs, and Registration Cert Providers). **Note**: For Wallet Providers, Member States notify Wallet Providers to the Commission, and the Commission compiles and publishes the Wallet Provider Trusted List directly (no URL submission by TLP).

The process is triggered by successful registration with the Member State Registrar (for PID Providers, Attestation Providers, Access CAs, and Registration Cert Providers). The TLP:
- Receives notification of successful registration from the Registrar (or accesses Registry data).
- Extracts trust anchors and relevant data from the Registry.
- Compiles Trusted Lists according to ETSI TS 119 612 specifications.
- Signs and publishes Trusted Lists.
- Submits the Trusted List URL to the European Commission.

> **Note**: The TLP extracts trust anchors that were provided during registration (e.g., PID signature Trust Anchors for PID Providers) and includes them in the Trusted Lists. **Note on Wallet Providers**: Wallet Providers register with a TLP in their Member State, and the Member State notifies Wallet Providers to the European Commission (per ARF Section 6.2.2). The European Commission then compiles, signs/seals, and publishes the Wallet Provider Trusted List (per **WPNot_04**), not the Member State TLP. See [Section 5.3.1](#531-submission-and-update-models-registration-to-trusted-list) for details on submission and update models.

### 3.2 European Commission Verification and LoTL Maintenance

The European Commission:
- **For Wallet Providers**: Compiles, signs/seals, and publishes the Wallet Provider Trusted List directly (per **WPNot_04**, **WPNot_05**). Member States notify Wallet Providers to the Commission, and the Commission compiles the Trusted List.
- **For other entities**: Receives Trusted List URL notifications from Member State TLPs, verifies completeness and technical compliance of published Trusted Lists.
- Maintains the List of Trusted Lists (LoTL) containing pointers to all published Trusted Lists.
- Signs/seals the LoTL.
- Publishes the LoTL in machine-readable and human-readable formats.

### 3.3 List of Trusted Lists (LoTL)

Per ETSI TS 119 612 clause D.5, the European Commission maintains a List of Trusted Lists (LoTL) that:
- Contains pointers (TrustedListPointers) to all published Trusted Lists:
  - Trusted Lists published by Member State TLPs (PID Provider TLs, Attestation Provider TLs, Access CA TLs, Registration Cert Provider TLs) - one pointer per Member State per entity type.
  - The single EU-wide Wallet Provider Trusted List published by the European Commission.
- Each pointer includes the Trusted List location (TSLLocation), scheme territory, and scheme operator name.
- Facilitates cross-border trust establishment.
- Centralizes trusted list distribution.
- Supports federation-level service discovery.

The European Commission:
- Compiles the LoTL from:
  - Trusted List URL notifications received from Member State TLPs (for PID Providers, Attestation Providers, Access CAs, Registration Cert Providers).
  - The directly published Wallet Provider Trusted List (compiled and published by the Commission itself).
- Signs/seals the LoTL using the Commission's signing key.
- Publishes the LoTL in machine-readable and human-readable formats.
- Publishes LoTL location and trust anchors in the Official Journal of the European Union (OJEU).

## 4. Key Requirements References

Below is a list of the main requirements relating to the entity registration and Trusted List publication processes. 

### 4.1 Registration Requirements

The matrixes collects all the ARF HLRs about the registration phase.

| Requirement | Description | Source |
|------------|-------------|--------|
| **Reg_01** | Member States SHALL provide processes for entity registration | Topic 27 |
| **Reg_10** | Access Certificate Authority SHALL issue access certificates to all registered entities (PID Providers, Attestation Providers, Relying Parties). Note: Wallet Providers do not receive access certificates. | Topic 27, Topic 31 |
| **Reg_19** | Member States SHALL approve PID Providers according to well-defined policy | Topic 27 |
| **Reg_21** | Member States SHALL approve Attestation Providers according to well-defined policy | Topic 27 |
| **Reg_25** | Member States SHALL identify Relying Parties at appropriate confidence level | Topic 27 |
| **RPRC_09** | Registrar MAY decide to issue registration certificates to Relying Parties | Topic 27, Topic 44 |
| **RPRC_13** | Registrar MAY decide to issue registration certificates to Providers | Topic 27, Topic 44 |

**Note**: **Reg_01** applies to PID Providers, Attestation Providers, and Relying Parties. Wallet Providers register with a Trusted List Provider, not with a Registrar (per ARF Section 6.2.2). **Reg_10** requires Access Certificates to be issued to all registered entities (PID Providers, Attestation Providers, Relying Parties). **RPRC_13** applies to Registration Certificates for Credential Issuers (PID Providers, Attestation Providers). Wallet Providers do not receive access certificates or registration certificates, as they do not register with a Registrar.

### 4.2 Trusted List Requirements

| Requirement | Description | Source |
|------------|-------------|--------|
| **GenNot_01** | Member States SHALL notify entities to European Commission | Topic 31 |
| **GenNot_03** | Commission SHALL enable secure notification, verification, and publication | Topic 31 |
| **GenNot_04** | Commission SHALL verify completeness and technical compliance | Topic 31 |
| **WPNot_01** | Commission SHALL establish technical specifications for Wallet Provider information | Topic 31 |
| **PPNot_01** | Commission SHALL establish technical specifications for PID Provider information | Topic 31 |
| **PuBPNot_01** | Commission SHALL establish technical specifications for PuB-EAA Provider information | Topic 31 |
| **RPACANot_01** | Commission SHALL establish technical specifications for Access CA information | Topic 31 |
| **TLPub_01** | Commission SHALL establish technical specifications for Trusted List publication | Topic 31 |
| **TLPub_06** | Commission SHALL publish Trusted List locations in OJEU | Topic 31 |
| **TLPub_07** | Commission SHALL publish trust anchors in OJEU | Topic 31 |

## 5. Trust Infrastructure Diagrams

The following Mermaid diagrams illustrate the trust infrastructure architecture and processes.

### 5.1 Overall Trust Infrastructure Architecture

```mermaid
graph TB
    subgraph MS["Member State"]
        Registrar[Registrar<br/>Reg_01, Reg_02]
        AccessCA[Access Certificate Authority<br/>Reg_10, Reg_11]
        RegCertProv[Provider of Registration Certificates<br/>RPRC_01, RPRC_02]
        TLProvider[Trusted List Provider<br/>MS Component]
        Registry[Registry<br/>Reg_03, Reg_04]
    end

    subgraph EC["European Commission"]
        ECNotify[Notification System<br/>GenNot_01, GenNot_02]
        ECVerify[Verification System<br/>GenNot_04]
        LoTLCompile[LoTL Compilation<br/>ETSI TS 119612 D.5]
        LoTL[List of Trusted Lists<br/>Signed/Sealed by EC]
    end

    subgraph Entities["Registered Entities<br/>(Register with Registrar)"]
        PID[PID Provider<br/>PPNot_02]
        AP[Attestation Provider<br/>PuBPNot_02]
        RP[Relying Party<br/>Reg_25]
    end
    
    WP[Wallet Provider<br/>Registers with TLP in MS<br/>MS notifies to Commission<br/>Commission compiles TL]

    subgraph TL["Published Trusted Lists"]
        WPTL[Wallet Provider TL<br/>WPNot_05]
        PIDTL[PID Provider TL<br/>PPNot_07]
        APTL[Attestation Provider TL<br/>PuBPNot_03]
        ACATL[Access CA TL<br/>RPACANot_05]
        RegCertTL[Registration Cert Provider TL<br/>RPACANot_05]
    end

    %% Registration Flow
    Entities -->|Register with identification & entitlements<br/>Reg_01: PID/Attestation Providers, RP<br/>Reg_19, Reg_21, Reg_25| Registrar
    WP -.->|Register with TLP in MS<br/>ARF Section 6.2.2| TLProvider
    TLProvider -.->|MS notifies WP to Commission<br/>WPNot_01, WPNot_02| ECNotify   

    Registrar -->|Approve & Register<br/>Reg_19, Reg_21| Registry
    Registrar -->|Request Access Cert<br/>Reg_10| AccessCA
    AccessCA -->|Issue Access Certificate<br/>Reg_10, Reg_12| Entities
    Registrar -.->|Optional: Request Reg Cert<br/>RPRC_09, RPRC_13| RegCertProv
    RegCertProv -.->|Issue Registration Certificate<br/>RPRC_02| Entities

    %% Submission and Update: Registration triggers Trusted List publication
    Registrar -->|Registration Complete<br/>Triggers TLP| TLProvider
    Registry -.->|TLP accesses Registry data<br/>Extracts Trust Anchors| TLProvider
    
    %% Trusted List Publication Flow
    TLProvider -->|Compile, Sign & Publish<br/>Trusted Lists<br/>PID/Attestation Providers, Access CA, Reg Cert Providers| TL
    TLProvider -->|Submit TL URL<br/>GenNot_01| ECNotify
    ECNotify -->|Commission compiles & publishes<br/>Wallet Provider TL<br/>WPNot_04, WPNot_05| WPTL
    ECNotify -->|Verify TL completeness<br/>GenNot_04| ECVerify
    ECVerify -->|Compile LoTL<br/>ETSI TS 119612 D.5| LoTLCompile
    LoTLCompile -->|Sign & Publish LoTL<br/>TLPub_06| LoTL
    LoTL -->|Contains pointers to| TL

    style MS fill:#e1f5ff
    style EC fill:#fff4e1
    style Entities fill:#e8f5e9
    style TL fill:#f3e5f5
```

### 5.2 Registration/Onboarding Process Flow

```mermaid
sequenceDiagram
    participant Entity as Entity<br/>(PID/Attestation Provider, RP)
    participant Registrar as Member State Registrar<br/>Reg_01, Reg_02
    participant Registry as Registry<br/>Reg_03, Reg_04
    participant AccessCA as Access Certificate Authority<br/>Reg_10, Reg_12
    participant RegCertProv as Provider of Registration Certificates<br/>RPRC_01, RPRC_02

    Note over Entity,RegCertProv: Registration/Onboarding Process<br/>(Note: Wallet Providers register with TLP, not Registrar)

    Entity->>Registrar: 1. Submit Registration Request<br/>(Identification data, Entitlements)
    Note right of Entity: For Attestation Providers: Attestation types<br/>For RP: Attributes, Intended use

    alt PID/Attestation Provider
        Registrar->>Registrar: 2b. Approve Provider<br/>(Reg_19, Reg_21)
    else Relying Party
        Registrar->>Registrar: 2c. Approve Relying Party<br/>(Reg_25)
    end

    Registrar->>Registry: 3. Register Entity<br/>(Reg_01, Reg_03)
    Note right of Registry: Publish registry entry<br/>Reg_03, Reg_04

    Registrar->>AccessCA: 4. Request Access Certificate<br/>(Reg_10)
    Note right of AccessCA: Issue certificate with<br/>SCT (CT_04), Registry reference

    AccessCA->>Entity: 5. Issue Access Certificate<br/>(Reg_10, Reg_12)

    alt Registrar Policy Requires Registration Certificate
        alt Relying Party
            Registrar->>RegCertProv: 6a. Request Registration Certificate<br/>(RPRC_09)
            Note right of RegCertProv: For Relying Parties<br/>One per intended use
        else Credential Issuer (PID/Attestation Provider)
            Registrar->>RegCertProv: 6b. Request Registration Certificate<br/>(RPRC_13)
            Note right of RegCertProv: For Credential Issuers<br/>(PID/Attestation Providers)<br/>One certificate per provider
        end

        RegCertProv->>Entity: 7. Issue Registration Certificate<br/>(RPRC_02, RPRC_14)
    end

    Entity->>Registry: 8. Update Information<br/>(Reg_07, Reg_08)
    
    Note over Registrar,Registry: Registration completion may trigger<br/>Trusted List notification (see 5.3)
```

### 5.3 Complete Registration to Trusted List Publication Flow

This diagram shows the complete end-to-end process from entity registration through to Trusted List publication, including the submission and update process between Registrar and Trusted List Provider.

```mermaid
sequenceDiagram
    participant Entity as Entity<br/>(PID/Attestation Provider)
    participant Registrar as Member State Registrar<br/>Reg_01, Reg_19, Reg_21
    participant Registry as Registry<br/>Reg_03, Reg_04
    participant AccessCA as Access Certificate Authority<br/>Reg_10
    participant TLP as Trusted List Provider<br/>(MS Component)
    participant ECNotify as European Commission<br/>Notification System<br/>GenNot_01
    participant ECVerify as European Commission<br/>Verification System<br/>GenNot_04
    participant LoTLCompile as European Commission<br/>LoTL Compilation<br/>ETSI TS 119612 D.5
    participant LoTL as List of Trusted Lists<br/>Signed by EC
    participant TL as Published Trusted Lists<br/>Signed by TLP

    Note over Entity,TL: Complete Flow: Registration → Trusted List Publication

    rect rgb(230, 245, 255)
        Note over Entity,Registry: Phase 1: Registration/Onboarding
        Entity->>Registrar: 1. Submit Registration Request<br/>(Identification, Entitlements, Trust Anchors)
        Note right of Entity: For PID Providers: PID signature Trust Anchors<br/>For Attestation Providers: Conformity assessment
        
        Registrar->>Registrar: 2. Approve Entity<br/>(Reg_01, Reg_19, Reg_21)
        Registrar->>Registry: 3. Register Entity<br/>(Reg_01, Reg_03)
        Registrar->>AccessCA: 4. Request Access Certificate<br/>(Reg_10)
        AccessCA->>Entity: 5. Issue Access Certificate<br/>(Reg_10, Reg_12)
    end

    rect rgb(255, 244, 225)
        Note over Registrar,TLP: Phase 2: Submission and Update - Registration to Trusted List
        Note over Registrar,TLP: Two possible submission and update models:
        alt Model A: Automatic Trigger (Recommended)
            Registrar->>TLP: 6a. Trigger Notification<br/>(Upon successful registration)
            Note right of Registrar: Registration completion<br/>automatically triggers TLP notification
        else Model B: Separate Registration
            Entity->>TLP: 6b. Separate Registration Request<br/>(Additional registration at TLP)
            Note right of Entity: Entity must separately<br/>register with TLP
            TLP->>TLP: 6c. Verify Registration Status<br/>(Check Registry)
        end
        
        TLP->>TLP: 7. Extract Trust Anchors & Registry Data<br/>(Collect data for TL compilation)
        Note right of TLP: Extract trust anchors from<br/>registration data<br/>Verify entity is in Registry
    end

    rect rgb(255, 230, 230)
        Note over TLP,TL: Phase 3: Trusted List Publication and Notification
        TLP->>TLP: 8. Compile Trusted Lists<br/>(Per entity type, ETSI TS 119612)
        Note right of TLP: Include trust anchors:<br/>- PID Providers: PID signature Trust Anchors (PPNot_02)<br/>- Attestation Providers: Conformity assessment (PuBPNot_02)<br/>Note: Wallet Provider TL compiled by EC, not MS TLP
        
        TLP->>TL: 9. Sign/Seal & Publish Trusted Lists<br/>(TLPub_05)
        Note right of TL: Published at MS TLP URL<br/>Machine-readable & human-readable
        
        TLP->>ECNotify: 10. Submit TL URL to EC<br/>(GenNot_01, PPNot_01/PuBPNot_01)<br/>Note: Wallet Provider TL compiled by EC directly
        
        ECNotify->>ECVerify: 11. Verify TL Completeness & Compliance<br/>(GenNot_04)
        ECVerify->>LoTLCompile: 12. Compile List of Trusted Lists<br/>(ETSI TS 119612 D.5)
        LoTLCompile->>LoTL: 13. Sign/Seal & Publish LoTL<br/>(TLPub_06)
        LoTLCompile->>LoTLCompile: 14. Publish in OJEU<br/>(TLPub_06, TLPub_07)
    end
```

### 5.3.1 Submission and Update Models: Registration to Trusted List

The relationship between Registrar and Trusted List Provider (TLP) can be implemented in two ways, as referenced in [ARF section 6.3.2](https://eudi.dev/2.5.0/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification):

#### Model A: Automatic Trigger (Recommended)

In this model, successful registration with the Registrar automatically triggers the Trusted List Provider to prepare and submit the Trusted List URL to the European Commission.

**Process:**
1. Entity registers with Registrar (per **Reg_01**, **Reg_19**, **Reg_21**)
2. Registrar completes registration and publishes to Registry
3. Registrar automatically notifies TLP of successful registration
4. TLP extracts trust anchors and registry data
5. TLP prepares and submits Trusted List URL to European Commission

**Advantages:**
- Single registration point for entities.
- Reduced administrative burden.
- Maintains consistency between Registry and Trusted Lists.
- Automatic synchronization.

**Requirements:**
- Registrar and TLP must have integration mechanisms for submission and update.
- TLP must have access to Registry data.
- Clear definition of when registration is "complete" and triggers notification.

#### Model B: Separate Registration

In this model, entities must separately register with both the Registrar and the Trusted List Provider.

**Process:**
1. Entity registers with Registrar (per **Reg_01**, **Reg_19**, **Reg_21**)
2. Registrar completes registration and publishes to Registry
3. Entity separately registers with TLP (or TLP initiates based on Registry data)
4. TLP verifies entity is registered in Registry
5. TLP prepares and submits Trusted List URL to European Commission

**Advantages:**
- Clear separation of concerns.
- Independent lifecycle management.
- Permits different approval criteria.

**Disadvantages:**
- Requires entities to manage two registration processes.
- Potential for inconsistency between Registry and Trusted Lists.
- Additional administrative overhead.

#### Recommendation

**Model A (Automatic Trigger)** is recommended for logical coherence and operational efficiency. The Registrar, upon successful registration, should automatically trigger the TLP to compile, sign, and publish Trusted Lists. This results in:

- Automatic processing of all registered entities (PID Providers, Attestation Providers) that require Trusted List inclusion. Note: Wallet Providers register directly with TLP.
- Synchronized Registry and Trusted Lists.
- Single point of registration for entities.
- Process managed by the Registrar, with TLP acting as the Trusted List publisher.

The TLP's role in this model is to:
- Receive registration completion notifications from Registrar (for PID Providers, Attestation Providers, Access CAs, Registration Cert Providers).
- Extract trust anchors and relevant data from Registry.
- Compile Trusted Lists per entity type according to ETSI TS 119 612 specifications (for PID Providers, Attestation Providers, Access CAs, Registration Cert Providers).
- Sign/seal and publish Trusted Lists at publicly accessible URLs (per Member State).
- Submit Trusted List URLs to European Commission.

**Note on Wallet Providers**: Wallet Providers follow a different process. They register with TLP in their Member State, the Member State notifies Wallet Providers to the Commission, and the Commission compiles, signs/seals, and publishes the EU-wide Wallet Provider Trusted List directly. The TLP does not compile or publish Wallet Provider Trusted Lists.

### 5.3.2 Trusted List Publication Process Flow (Notification Only)

This diagram focuses solely on the notification process, as referenced in the original document structure.

```mermaid
sequenceDiagram
    participant MS as Member State<br/>Trusted List Provider
    participant ECNotify as European Commission<br/>Notification System<br/>GenNot_01
    participant ECVerify as European Commission<br/>Verification System<br/>GenNot_04
    participant ECCompile as European Commission<br/>Compilation System<br/>TLPub_01
    participant LoTL as List of Trusted Lists<br/>ETSI TS 119612 D.5
    participant TL as Published Trusted Lists<br/>TLPub_05

    Note over TLP,LoTL: Trusted List Publication Process

    rect rgb(230, 245, 255)
        Note over TLP,TL: Phase 1: MS TLP Compiles, Signs & Publishes Trusted Lists<br/>(Note: Wallet Provider TL is compiled by EC, not MS TLP)
        TLP->>TLP: 1. Compile PID Provider TL<br/>(PPNot_01, PPNot_02)
        Note right of TLP: Trust anchors for PID<br/>signature (PPNot_02)
        
        TLP->>TLP: 2. Compile Attestation Provider TL<br/>(PuBPNot_01, PuBPNot_02)
        Note right of TLP: Conformity assessment<br/>report (PuBPNot_02)
        
        TLP->>TLP: 3. Compile Access CA TL<br/>(RPACANot_01, RPACANot_02)
        Note right of TLP: Trust anchors for<br/>access cert verification
        
        TLP->>TLP: 4. Compile Registration Cert Provider TL<br/>(RPACANot_01, RPACANot_02)
        
        TLP->>TL: 5. Sign/Seal & Publish Trusted Lists<br/>(TLPub_05)
        Note right of TL: Published at MS TLP URL<br/>Machine-readable & human-readable<br/>ETSI TS 119612 format
    end

    rect rgb(255, 244, 225)
        Note over TLP,ECNotify: Phase 2: MS TLP Submits TL URLs to EC
        TLP->>ECNotify: 7. Submit TL URLs to EC<br/>(GenNot_01)
        Note right of TLP: Submit URLs of published<br/>Trusted Lists per entity type
    end

    rect rgb(255, 230, 230)
        Note over ECVerify,LoTL: Phase 3: EC Verifies and Maintains LoTL
        ECNotify->>ECVerify: 8. Verify TL Completeness & Compliance<br/>(GenNot_04)
        Note right of ECVerify: Technical validation<br/>Schema compliance<br/>Verify TL signatures
        
        ECVerify->>LoTLCompile: 9. Compile List of Trusted Lists<br/>(ETSI TS 119612 D.5)
        Note right of LoTLCompile: Create TrustedListPointers<br/>with TSLLocation per MS<br/>Plus EU-wide Wallet Provider TL
        
        LoTLCompile->>LoTL: 10. Sign/Seal & Publish LoTL<br/>(TLPub_06)
        Note right of LoTL: Published by EC<br/>Contains pointers to MS TLs<br/>and EU-wide Wallet Provider TL
        
        LoTLCompile->>LoTLCompile: 11. Publish in OJEU<br/>(TLPub_06, TLPub_07)
        Note right of LoTLCompile: LoTL location &<br/>trust anchors
    end
```

### 5.4 List of Trusted Lists Structure (ETSI TS 119612 D.5)

```mermaid
graph TB
    subgraph LoTL["List of Trusted Lists<br/>ETSI TS 119612 D.5"]
        ListInfo[ListInformation<br/>ListName, ListIdentifier<br/>ListVersion, ListIssueDateTime]
        TrustedLists[TrustedLists Container]
        Signature[Digital Signature<br/>Signed/Sealed by EC]
    end

    subgraph TLPointers["TrustedListPointers"]
        WPTLPointer[Wallet Provider TL Pointer<br/>TSLLocation: EC URL<br/>SchemeTerritory: EU<br/>SchemeOperatorName: EC]
        PIDTLPointer[PID Provider TL Pointer<br/>TSLLocation: MS TLP URL<br/>SchemeTerritory: MS Code<br/>SchemeOperatorName: MS TLP]
        APTLPointer[Attestation Provider TL Pointer<br/>TSLLocation: MS TLP URL<br/>SchemeTerritory: MS Code<br/>SchemeOperatorName: MS TLP]
        ACATLPointer[Access CA TL Pointer<br/>TSLLocation: MS TLP URL<br/>SchemeTerritory: MS Code<br/>SchemeOperatorName: MS TLP]
        RegCertTLPointer[Registration Cert Provider TL Pointer<br/>TSLLocation: MS TLP URL<br/>SchemeTerritory: MS Code<br/>SchemeOperatorName: MS TLP]
    end

    subgraph ActualTL["Actual Trusted Lists<br/>Referenced by Pointers"]
        WPTL[Wallet Provider TL<br/>EU-wide, published by EC<br/>WPNot_04, WPNot_05]
        PIDTL[PID Provider TL<br/>Per MS, published by MS TLP<br/>PPNot_07]
        APTL[Attestation Provider TL<br/>Per MS, published by MS TLP<br/>PuBPNot_03]
        ACATL[Access CA TL<br/>Per MS, published by MS TLP<br/>RPACANot_05]
        RegCertTL[Registration Cert Provider TL<br/>Per MS, published by MS TLP<br/>RPACANot_05]
    end

    LoTL --> ListInfo
    LoTL --> TrustedLists
    LoTL --> Signature

    TrustedLists --> TLPointers

    TLPointers --> WPTLPointer
    TLPointers --> PIDTLPointer
    TLPointers --> APTLPointer
    TLPointers --> ACATLPointer
    TLPointers --> RegCertTLPointer

    WPTLPointer -.->|TSLLocation| WPTL
    PIDTLPointer -.->|TSLLocation| PIDTL
    APTLPointer -.->|TSLLocation| APTL
    ACATLPointer -.->|TSLLocation| ACATL
    RegCertTLPointer -.->|TSLLocation| RegCertTL

    style LoTL fill:#fff4e1
    style TLPointers fill:#e1f5ff
    style ActualTL fill:#e8f5e9
```

### 5.5 Entity Registration and Trusted List Relationship

```mermaid
graph TB
    subgraph Registration["Registration Process<br/>Managed by MS Registrar"]
        RegStep1["1. Entity Registration<br/>Reg_01 (PID/Attestation Providers, RP)<br/>Reg_19, Reg_21, Reg_25"]
        RegStep2["2. Access Certificate Issuance<br/>Reg_10, Reg_12<br/>(PID/Attestation Providers, RP only)"]
        RegStep3["3. Optional Registration Certificate<br/>RPRC_09 (RP), RPRC_13 (Credential Issuers)"]
        RegStep4[4. Registry Publication<br/>Reg_03, Reg_04]
    end
    
    subgraph WPRegistration["Wallet Provider Registration Managed by MS TLP & EC"]
        WPRegStep1[1. Wallet Provider registers with TLP in MS<br/>WPNot_01, WPNot_02]
        WPRegStep2[2. MS notifies WP to Commission<br/>WPNot_01, WPNot_02]
        WPRegStep3[3. EC compiles & publishes EU-wide Wallet Provider TL<br/>WPNot_04, WPNot_05]
    end

    subgraph SubmissionUpdate["Submission and Update: Registration → Trusted List<br/>Registrar → Trusted List Provider"]
        TLPTrigger[Trusted List Provider<br/>Triggered by Registration Completion]
        TLPCompile[Compile Trusted Lists<br/>Extract Trust Anchors from Registry]
        TLPPublish[Sign & Publish Trusted Lists<br/>TLPub_05]
    end

    subgraph Notification["Notification & LoTL Process<br/>MS TLP → EC"]
        NotifStep1[1. MS TLP Submits TL URL<br/>GenNot_01]
        NotifStep2[2. EC Verifies TL<br/>GenNot_04]
        NotifStep3[3. EC Compiles LoTL<br/>ETSI TS 119612 D.5]
        NotifStep4[4. EC Signs & Publishes LoTL<br/>TLPub_06]
    end

    subgraph Entities["Entities"]
        WP[Wallet Provider]
        PID[PID Provider]
        AP[Attestation Provider]
        RP[Relying Party]
        ACA[Access CA]
        RegCertProv[Registration Cert Provider]
    end

    subgraph TrustedLists["Published Trusted Lists"]
        WPTL[Wallet Provider TL<br/>WPNot_05]
        PIDTL[PID Provider TL<br/>PPNot_07]
        APTL[Attestation Provider TL<br/>PuBPNot_03]
        ACATL[Access CA TL<br/>RPACANot_05]
        RegCertTL[Registration Cert Provider TL<br/>RPACANot_05]
    end

    %% Registration Flow (PID/Attestation Providers, RP)
    PID -->|Register| RegStep1
    AP -->|Register| RegStep1
    RP -->|Register| RegStep1
    RegStep1 --> RegStep2
    RegStep2 --> RegStep3
    RegStep3 --> RegStep4

    %% Wallet Provider Registration Flow (separate)
    WP -->|Register with TLP in MS<br/>not with Registrar| WPRegStep1
    WPRegStep1 -->|MS notifies to Commission| WPRegStep2
    WPRegStep2 -->|EC compiles & publishes<br/>EU-wide TL| WPRegStep3
    WPRegStep3 -->|EU-wide TL published by EC| WPTL

    %% Submission and Update Flow
    RegStep4 -->|Registration Complete<br/>Triggers TLP| TLPTrigger
    TLPTrigger -->|Access Registry Data<br/>Extract Trust Anchors| TLPCompile
    TLPCompile -->|Compile per entity type| TLPPublish
    TLPPublish -->|Sign & Publish at URL| NotifStep1

    %% Notification Flow
    NotifStep1 --> NotifStep2
    NotifStep2 --> NotifStep3
    NotifStep3 --> NotifStep4

    NotifStep4 --> TrustedLists

    %% Note: Registration data feeds into Trusted Lists
    RegStep4 -.->|Registry data used for<br/>trust evaluation| TrustedLists

    style Registration fill:#e8f5e9
    style WPRegistration fill:#ffe0b2
    style SubmissionUpdate fill:#fff9c4
    style Notification fill:#fff4e1
    style Entities fill:#f3e5f5
    style TrustedLists fill:#e1f5ff
```

## 6. Key Distinctions

### 6.1 Registration vs. Trusted List Publication

| Aspect | Registration | Trusted List Publication |
|--------|-------------|---------------------------|
| **Purpose** | Enable entity participation in ecosystem | Establish trust anchors for validation |
| **Managed By** | Member State Registrar | Member State TLP compiles, signs & publishes TLs per MS (PID/Attestation Providers, Access CAs, Reg Cert Providers); EC compiles & publishes EU-wide Wallet Provider TL; EC maintains LoTL |
| **Scope** | PID Providers, Attestation Providers, Relying Parties (register with Registrar). Wallet Providers register separately with TLP. | Selected entities: Wallet Providers (EU-wide TL published by EC), PID Providers (per MS TL published by MS TLP), Attestation Providers (per MS TL published by MS TLP), Access CAs (per MS TL published by MS TLP) |
| **Output** | Registry entries, Access Certificates, Registration Certificates | Trusted Lists: Wallet Provider TL (EU-wide, signed/sealed by EC), other TLs (per MS, signed/sealed by MS TLP); List of Trusted Lists (signed/sealed by EC) |
| **Used For** | Entitlement verification, service access | Cryptographic trust validation |
| **Requirements** | Reg_01, Reg_10, RPRC_09, RPRC_13 | GenNot_01, TLPub_01, TLPub_05, TLPub_06 |
| **Submission and Update** | Managed by Registrar | For PID/Attestation Providers, Access CAs, Reg Cert Providers: Triggered by Registrar registration completion; TLP compiles, signs & publishes TLs per MS, then submits TL URL to EC. For Wallet Providers: MS notifies WP to EC, EC compiles & publishes EU-wide TL directly. |

## 8. Summary

The trust infrastructure operates through two distinct but complementary processes:

1. **Registration/Onboarding**: Managed at Member State level, entities (PID Providers, Attestation Providers, Relying Parties) register with Registrars and entitlements are defined. Wallet Providers register with Trusted List Providers (TLPs) in their Member State, not with Registrars.
2. **Trusted List Publication**: 
   - **For PID Providers, Attestation Providers, Access CAs, Registration Cert Providers**: Managed at Member State level - MS TLPs compile, sign, and publish Trusted Lists per Member State, then submit TL URLs to the European Commission.
   - **For Wallet Providers**: Managed at EU level - Member States notify Wallet Providers to the Commission, and the Commission compiles, signs/seals, and publishes a single EU-wide Wallet Provider Trusted List.

Both processes are required for the trust ecosystem:
- **Registration**: Defines operational authorization and entitlement management.
- **Trusted Lists**: Contain cryptographic trust anchors for signature and certificate validation.

The separation of these processes aligns with the ARF and enables:
- Independent lifecycle management.
- Different trust models (operational vs. cryptographic).
- Scalable cross-border trust establishment.
- Clear separation of concerns between MS and EU levels.
- EU-wide Wallet Provider Trusted List for consistent Wallet Provider recognition across all Member States.

## 7. Trust Evaluation

> **Note**: This section describes trust evaluation processes that use the registration data and Trusted Lists established through the onboarding and Trusted List publication processes described in the main document. As the focus of this document is on **Onboarding (Registration)** and **Trusted List Publication** processes, this section is provided for reference but could be moved to a separate document in the future.

This section describes how trust is evaluated in the ecosystem using the registration data and Trusted Lists established through the onboarding and Trusted List publication processes.

### 7.1 Trust Evaluation Requirements

| Requirement | Description | Source |
|------------|-------------|--------|
| **ISSU_19** | PID Providers SHALL accept trust anchors in Wallet Provider Trusted Lists | Topic 31 |
| **ISSU_21** | PID Providers SHALL verify Wallet Provider presence in Trusted List | Topic 31 |
| **ISSU_24** | Wallet Units SHALL authenticate and validate access certificates using Access CA Trusted Lists | Topic 27 |
| **ISSU_24a** | Wallet Units SHALL verify PID Provider registration before PID issuance | Topic 27, Topic 44 |
| **ISSU_34a** | Wallet Units SHALL verify Attestation Provider registration before attestation issuance | Topic 27, Topic 44 |
| **RPA_04** | Wallet Units SHALL accept trust anchors in Relying Party Access CA Trusted Lists | Topic 31 |
| **RPRC_16** | Wallet Units SHALL offer Users possibility to verify Relying Party registration | Topic 44 |
| **RPRC_21** | Wallet Units SHALL verify requested attributes are registered | Topic 44 |

### 7.2 Trust Evaluation Flow

```mermaid
graph LR
    subgraph WalletUnit["Wallet Unit"]
        WU[Wallet Unit<br/>ISSU_24, ISSU_34a, RPRC_16]
    end

    subgraph Providers["Credential Providers"]
        PIDProv[PID Provider<br/>ISSU_19, ISSU_21]
        AttProv[Attestation Provider<br/>ISSU_30]
    end

    subgraph RP["Relying Party"]
        RPInst[Relying Party Instance<br/>RPA_04, RPRC_19]
    end

    subgraph TrustSources["Trust Sources"]
        WPTL[Wallet Provider TL<br/>ISSU_19, ISSU_21]
        PIDTL[PID Provider TL<br/>OIA_12]
        APTL[Attestation Provider TL<br/>OIA_13, OIA_14]
        ACATL[Access CA TL<br/>ISSU_24, ISSU_34]
        Registry[Registry<br/>ISSU_24a, ISSU_34a, RPRC_16]
        RegCertTL[Registration Cert Provider TL<br/>ISSU_33a]
    end

    %% PID Issuance Trust Evaluation
    WU -->|1. Request PID| PIDProv
    PIDProv -->|2. Verify WUA in TL<br/>ISSU_21| WPTL
    WU -->|3. Verify Access Cert in TL<br/>ISSU_24| ACATL
    WU -->|4. Verify Registration<br/>ISSU_24a| Registry
    WU -.->|5. Verify Reg Cert in TL<br/>ISSU_33a| RegCertTL

    %% Attestation Issuance Trust Evaluation
    WU -->|1. Request Attestation| AttProv
    AttProv -->|2. Verify WUA in TL<br/>ISSU_30| WPTL
    WU -->|3. Verify Access Cert in TL<br/>ISSU_34| ACATL
    WU -->|4. Verify Registration & Entitlements<br/>ISSU_34a| Registry
    WU -.->|5. Verify Reg Cert in TL<br/>ISSU_33a| RegCertTL

    %% Presentation Trust Evaluation
    RPInst -->|1. Present Request| WU
    WU -->|2. Verify Access Cert in TL<br/>RPA_04| ACATL
    WU -->|3. Verify Registration<br/>RPRC_16| Registry
    WU -->|4. Verify Requested Attributes<br/>RPRC_21| Registry
    WU -.->|5. Verify Reg Cert in TL<br/>RPRC_17| RegCertTL

    %% RP Validation
    RPInst -->|Validate PID Signature<br/>OIA_12| PIDTL
    RPInst -->|Validate QEAA Signature<br/>OIA_13| APTL
    RPInst -->|Validate PuB-EAA Signature<br/>OIA_14| APTL

    style WalletUnit fill:#e8f5e9
    style Providers fill:#fff3e0
    style RP fill:#f3e5f5
    style TrustSources fill:#e1f5ff
```

### 7.3 Trust Evaluation Points

Trust evaluation occurs at multiple points using different trust sources:

1. **During Credential Issuance**:
   - Wallet Units verify Provider registration (Registry) - **ISSU_24a, ISSU_34a**
   - Providers verify Wallet Provider in Trusted List - **ISSU_21, ISSU_30**

2. **During Presentation**:
   - Wallet Units verify Relying Party registration (Registry) - **RPRC_16, RPRC_21**
   - Wallet Units verify Access Certificates using Trusted Lists - **ISSU_24, ISSU_34, RPA_04**

3. **During Signature Validation**:
   - Relying Parties validate PID signatures using PID Provider TL - **OIA_12**
   - Relying Parties validate attestation signatures using Attestation Provider TL - **OIA_13, OIA_14**

