# Trust Infrastructure Schema: Onboarding and Trusted Lists

This document outlines the schema and graphical representation of the EUDI Wallet trust infrastructure. It focuses on three closely related processes: **Registration/Onboarding**, **Notification**, and **Trusted List Publication**, which are separated to align with the Architecture and Reference Framework (ARF).

## Overview

The trust infrastructure relies on three distinct but complementary processes:

1.  **Registration/Onboarding**: Entities (PID Providers, Attestation Providers, Relying Parties) register with Member State Registrars to define operational authorization and entitlements (ARF Section 3.17).
2.  **Notification**: Member States notify the European Commission of **Wallet Providers**, **Access Certificate Authorities (Access CAs)**, and **Providers of Registration Certificates** for inclusion in the relevant Trusted Lists.
3.  **Trusted List Publication**: Publication of cryptographic trust anchors for validation purposes, based on registration data and Member State notifications.

### Responsibilities Matrix

The following table summarizes the registration requirement and the authority responsible for compiling the Trusted List (TL) for each entity type:

| Entity Type | Registration Process | Trusted List Compilation |
| :--- | :--- | :--- |
| **PID Provider** | **Register with MS Registrar** | **European Commission** |
| **Attestation Provider** | **Register with MS Registrar** | **Member State TLP** (per MS) |
| **Relying Party (RP)** | **Register with MS Registrar** | N/A (Uses Access Certificates/Registry) |
| **Wallet Provider** | *Notification only* (by MS to EC) | **European Commission** |
| **Access CA** | *Notification only* (by MS to EC) | **European Commission** |
| **Reg. Cert. Provider** | *Notification only* (by MS to EC) | **European Commission** |

> **Key Distinction**: **Wallet Providers**, **Access CAs**, and **Providers of Registration Certificates** do **not** register with Registrars. They are notified directly by Member States to the European Commission.

## 1. Trust Infrastructure Architecture

### 1.1 Trust Infrastructure Authorities

*   **Registrar**: Established by Member States to manage the registration and operational authorization of **PID Providers**, **Attestation Providers**, and **Relying Parties**.
*   **European Commission**:
    *   Compiles, signs/seals, and publishes Trusted Lists for Wallet Providers, PID Providers, Access CAs, and Registration Cert Providers (per **WPNot_04**, **WPNot_05**, **PPNot_05**, **PPNot_06**, **RPACANot_04**).
    *   Maintains and publishes the **List of Trusted Lists (LoTL)** containing pointers to all published Trusted Lists.
*   **Member State TLP**: Compiles, signs, and publishes National Trusted Lists specifically for **Attestation Providers** (PuB-EAA) and submits the TL URL to the Commission.
*   **Access Certificate Authority (CA)**: Issues access certificates to registered entities. Notified by MS to the Commission; does not interact with Registrars.
*   **Provider of Registration Certificates**: Optionally issues certificates detailing entitlements. Notified by MS to the Commission.

### 1.2 Registered Entities

The following entities must undergo the registration process with a Registrar (ARF Topic 27):

*   **PID Providers**: Issue Person Identification Data. Approved via MS-defined policy.
*   **Attestation Providers**: Issue attestations (QEAA, PuB-EAA, EAA).
*   **Relying Parties (RP)**: Request attributes from Wallet Units.

## 2. Registration/Onboarding Process

The registration process is managed by Member State Registrars and involves (for PID Providers, Attestation Providers, and Relying Parties):

1. Entity registration with identification data and entitlements.
2. Access certificate issuance by Access Certificate Authority.
3. Optional registration certificate issuance by Provider of Registration Certificates.
4. Registry publication for transparency and online verification (per **Reg_03**, **Reg_04**). The registry is always published for all registered entities (PID Providers, Attestation Providers, Relying Parties) and serves as an alternative source when registration certificates are not available. Member States SHALL support the common API specified in [Technical Specification 5](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) for automated retrieval of registry entries (per **Reg_06**, Topic 27). The API uses a secure channel and does not require authentication. Wallet Units use the Registrar's online service URL to verify:
   - PID Provider registration (per **ISSU_24a**).
   - Attestation Provider registration and attestation types (per **ISSU_34a**).
   - Relying Party registration and requested attributes (per **RPRC_18**).

### 2.1 Registration Data and Requirements

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

> **Note**: Wallet Providers do not register with Registrars. They are notified by Member States to the European Commission for Trusted List inclusion (see [Section 3.1.1](#311-wallet-provider-notification)). Wallet Providers do not receive access certificates or registration certificates, as they are not registered with Registrars. The Wallet Solution provided by the Wallet Provider must be certified by Conformity Assessment Bodies (CABs) as described in [ARF Chapter 7](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#7-certification-and-risk-management).

### 2.2 Access Certificate Issuance

After registration of entities (PID Providers, Attestation Providers, Relying Parties) the Access CA issues certificates that:
- Authenticate entities during service interactions.
- Reference the registry for entitlement verification.
- Include Signed Certificate Timestamps (SCT) for Certificate Transparency.

### 2.3 Registration Certificate Issuance (Optional)

If the Registrar policy requires it, the provider of Registration Certificates issues registration certificates that:
- Detail the entity's registration status.
- Specify entitlements for the specific entity, including available attestation types from Credential Issuers and attributes requested by Relying Parties.
- Enable Wallet Units to verify entity entitlements.

Registration certificates are issued per:
- **RPRC_09**: For Relying Parties (Registrar MAY decide to issue registration certificates to Relying Parties).
- **RPRC_13**: For Credential Issuers (PID Providers, Attestation Providers) (Registrar MAY decide to issue registration certificates to Providers).

## 3. Trusted List Publication Process

The Trusted List publication process is separate from registration. See [Overview](#overview) for Trusted List compilation responsibilities. The process involves:

1. Member State TLPs compile, sign, and publish Trusted Lists for all entities (Wallet Providers, PID Providers, Attestation Providers, Access CAs, Registration Cert Providers).
2. Member State TLPs submit Trusted List URLs to the European Commission.
3. Commission verifies Trusted Lists and maintains the List of Trusted Lists (LoTL) containing pointers to all published Trusted Lists.
4. Commission signs and publishes the LoTL.

### 3.1 Trusted List Publication by Trusted List Provider

> **Note on Trusted List Provider Organizational Level**: The ARF ([Section 3.5](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#35-trusted-list-provider)) defines a Trusted List Provider (TLP) as "a body responsible for maintaining, managing, and publishing a Trusted List." Both Member State TLPs and the European Commission act as TLPs with distinct scopes (see [Responsibilities Matrix](#overview)). The ARF does not explicitly specify whether Member State TLPs must be Member State entities, sector-specific bodies, or the European Commission itself. However, the notification requirements (GenNot_01) state that "Member States SHALL notify" entities to the Commission, and [Section 3.5](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#35-trusted-list-provider) states that "relevant entities must be notified to the Commission by a Member State." This suggests that Member State TLPs operate at Member State level, though the ARF does not explicitly rule out other organizational models. There is also an inconsistency in the ARF itself ([Section 6.3.2](https://eudi.dev/2.7.3/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification)) where line 2838 states that "A PID Provider or an Attestation Provider is registered by a Trusted List Provider" while line 2851 states that entities "register itself with a Registrar," regarding whether entities are registered by a TLP or by a Registrar.

The Member State Trusted List Provider (MS TLP) is responsible for (for Attestation Providers only):

1. **Compiling Trusted Lists**: The MS TLP compiles Trusted Lists for Attestation Providers (PuB-EAA Providers with conformity assessment reports).

2. **Signing Trusted Lists**: The MS TLP signs/seals the Trusted Lists using its signing key (for Attestation Providers only).

3. **Publishing Trusted Lists**: The MS TLP publishes the signed Trusted Lists in machine-readable and human-readable formats at a publicly accessible URL (for Attestation Providers only). Per [ETSI TS 119 602 V1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf) (Data model for Lists of Trusted Entities), **Attestation Provider Trusted Lists** (ETSI TS 119 602 Annex H, published by MS TLP) may be published in either **JSON format with compact JAdES Baseline B signature** OR **XML format with XAdES Baseline B signature** (per ETSI EN 319 132-1). When XML is used, it must be an enveloped digital signature.

All Trusted Lists must comply with ETSI TS 119 602 data model and the specific profiles defined in the annexes, or with ETSI TS 119 612 v2.1.1 or a suitable profile derived from ETSI TS 102 231 (per **WPNot_05**, **PPNot_07**, **PuBPNot_03**, **RPACANot_05**).

4. **Submitting to European Commission**: The MS TLP submits the published Trusted List URL to the European Commission (for Attestation Providers only).

The process is triggered by successful registration with the Member State Registrar (for Attestation Providers only). The MS TLP:
- Receives notification of successful registration from the Registrar (or accesses Registry data).
- Extracts trust anchors and relevant data from the Registry.
- Compiles Trusted Lists according to ETSI TS 119 612 specifications.
- Signs and publishes Trusted Lists.
- Submits the Trusted List URL to the European Commission.

> **Note**: For Attestation Providers, the TLP extracts trust anchors that were provided during registration and includes them in the Trusted Lists. See [Overview](#overview) for Trusted List compilation responsibilities and [Section 5.3.1](#531-submission-and-update-models-registration-to-trusted-list) for details on submission and update models.

### 3.1.1 Member State Notification to European Commission

Member States SHALL notify all PID Providers, PuB-EAA Providers, Wallet Providers, Access Certificate Authorities, and Providers of Registration Certificates to the European Commission (per **GenNot_01**). The information notified varies by entity type:

- **PID Providers** (per **PPNot_02**): Identification data, PID Provider trust anchors, Access Certificate Authority trust anchors for PID Providers, Service Supply Point (URL).
- **Wallet Providers** (per **WPNot_02**): Identification data, Wallet Provider trust anchors.
- **PuB-EAA Providers** (per **PuBPNot_02**): Identification data (including conformity assessment report), Service Supply Point (URL).
- **Access Certificate Authorities and Providers of Registration Certificates** (per **RPACANot_02**): Identification data, Trust anchors.

> **Note**: Wallet Providers are notified by Member States to the European Commission (per **GenNot_01**, **WPNot_01**, **WPNot_02**), and are not registered with Registrars. The European Commission compiles, signs/seals, and publishes Trusted Lists for Wallet Providers (per **WPNot_04**, **WPNot_05**), PID Providers (per **PPNot_05**), Access CAs (per **PPNot_06**, **RPACANot_04**), and Registration Cert Providers (per **RPACANot_04**).

### 3.2 European Commission Verification and LoTL Maintenance

The European Commission:
- Compiles, signs/seals, and publishes Trusted Lists (see [Overview](#overview) for details).
- Receives Trusted List URL notifications from Member State TLPs (for Attestation Providers only), verifies completeness and technical compliance of published Trusted Lists.
- Maintains the List of Trusted Lists (LoTL) containing pointers to all published Trusted Lists.
- Signs/seals and publishes the LoTL in machine-readable and human-readable formats.

### 3.3 List of Trusted Lists (LoTL)

Per ETSI TS 119 612 clause D.5, the European Commission maintains a List of Trusted Lists (LoTL) that:
- Contains pointers (TrustedListPointers) to all published Trusted Lists:
  - **Trusted Lists** compiled and published by Member State TLPs (one separate list per Member State for each entity type).

- Each pointer includes the Trusted List location (TSLLocation), scheme territory, and scheme operator name.
- Facilitates cross-border trust establishment.
- Centralizes trusted list distribution.
- Supports federation-level service discovery.

The European Commission:
- Compiles the LoTL from:
  - The directly compiled and published Trusted Lists (Wallet Provider TL, PID Provider TL, Access CA TL, Registration Cert Provider TL).
  - Trusted List URL notifications received from Member State TLPs (for Attestation Providers only).
- Signs/seals the LoTL using the Commission's signing key.
- Publishes the LoTL in machine-readable and human-readable formats.
- Publishes LoTL location and trust anchors in the Official Journal of the European Union (OJEU).

## 4. Key Requirements References

Below is a list of the main requirements relating to the entity registration and Trusted List publication processes. 

### 4.1 Registration Requirements

The matrix collects all the ARF HLRs about the registration phase.

| Requirement | Description | Source |
|------------|-------------|--------|
| **Reg_01** | Member States SHALL provide processes for entity registration | Topic 27 |
| **Reg_10** | Access Certificate Authority SHALL issue access certificates to all registered entities (PID Providers, Attestation Providers, Relying Parties). | Topic 27, Topic 31 |
| **Reg_19** | Member States SHALL approve PID Providers according to well-defined policy | Topic 27 |
| **Reg_21** | Member States SHALL approve Attestation Providers according to well-defined policy | Topic 27 |
| **Reg_25** | Member States SHALL identify Relying Parties at appropriate confidence level | Topic 27 |
| **RPRC_09** | Registrar MAY decide to issue registration certificates to Relying Parties | Topic 27, Topic 44 |
| **RPRC_13** | Registrar MAY decide to issue registration certificates to Providers | Topic 27, Topic 44 |

**Note**: **Reg_01** applies to PID Providers, Attestation Providers, and Relying Parties. **Reg_10** requires Access Certificates to be issued to all registered entities (PID Providers, Attestation Providers, Relying Parties). **RPRC_13** applies to Registration Certificates for Credential Issuers (PID Providers, Attestation Providers). See [Overview](#overview) for entity registration responsibilities.

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
%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
graph TB
    %% --- CLASSES ---
    classDef titleBox fill:none,stroke:none,font-weight:bold,font-size:16px,color:black;    

    subgraph MS["Member State"]
        Registrar[Registrar<br/>Reg_01, Reg_02]
        AccessCA[Access Certificate Authority<br/>Reg_10, Reg_11]
        RegCertProv[Provider of Registration Certificates<br/>RPRC_01, RPRC_02]
        TLProvider[Trusted List Provider<br/>MS Component]
        Registry[Registry<br/>Reg_03, Reg_04]
        WP[Wallet Provider<br/>Notified by MS to Commission<br/>Not registered with Registrar]
        Registry ~~~ WP
    end

    subgraph EC["European Commission"]
        ECNotify[Notification System<br/>GenNot_01, GenNot_02]
        ECVerify[Verification System<br/>GenNot_04]
        LoTLCompile[LoTL Compilation<br/>ETSI TS 119612 D.5]
        LoTL[List of Trusted Lists<br/>Signed/Sealed by EC]
    end

    subgraph EntitiesScope[ ]
        %% inserted title to fix visibility
        EntitiesTitle["Registered Entities<br/>(Register with Registrar)"]:::titleBox
        
        PID[PID Provider<br/>Registers with Registrar<br/>Also notified to Commission<br/>PPNot_02]
        AP[Attestation Provider<br/>PuBPNot_02]
        RP[Relying Party<br/>Reg_25]
        
        %% Force vertical layout
        EntitiesTitle ~~~ PID
        EntitiesTitle ~~~ AP
        EntitiesTitle ~~~ RP
    end

    subgraph TL["Published Trusted Lists"]
        WPTL[Wallet Provider TL<br/>Compiled by EC<br/>WPNot_04, WPNot_05]
        PIDTL[PID Provider TL<br/>Compiled by EC<br/>PPNot_05]
        APTL[Attestation Provider TL<br/>Per MS, compiled by MS TLP<br/>PuBPNot_03]
        ACATL[Access CA TL<br/>Compiled by EC<br/>PPNot_06, RPACANot_04]
        RegCertTL[Registration Cert Provider TL<br/>Compiled by EC<br/>RPACANot_04]
    end

    %% Registration Flow
    PID -->|Register with identification & entitlements<br/>Reg_01, Reg_19| Registrar
    AP -->|Register with identification & entitlements<br/>Reg_01, Reg_21| Registrar
    RP -->|Register with identification & entitlements<br/>Reg_01, Reg_25| Registrar
    
    %% Notification Flow (entities notified to Commission)
    WP -.->|MS notifies WP to Commission<br/>GenNot_01, WPNot_01, WPNot_02| ECNotify
    PID -.->|After registration, MS notifies PID Provider to Commission<br/>GenNot_01, PPNot_01, PPNot_02| ECNotify
    AccessCA -.->|MS notifies Access CA to Commission<br/>GenNot_01, RPACANot_01, RPACANot_02| ECNotify
    RegCertProv -.->|MS notifies Registration Cert Provider to Commission<br/>GenNot_01, RPACANot_01, RPACANot_02| ECNotify
    
    Registrar -->|Approve & Register<br/>Reg_19, Reg_21| Registry
    Registrar -->|Request Access Cert<br/>Reg_10| AccessCA
    AccessCA -->|Issue Access Certificate<br/>Reg_10, Reg_12| EntitiesScope
    Registrar -.->|Optional: Request Reg Cert<br/>RPRC_09, RPRC_13| RegCertProv
    RegCertProv -.->|Issue Registration Certificate<br/>RPRC_02| EntitiesScope
    
    %% Submission and Update: Registration triggers Trusted List publication (Attestation Providers only)
    Registrar -->|Registration Complete<br/>Triggers TLP for Attestation Providers| TLProvider
    Registry -.->|TLP accesses Registry data<br/>Extracts Trust Anchors for Attestation Providers| TLProvider
    
    %% Trusted List Publication Flow
    TLProvider -->|Compile, Sign & Publish<br/>Attestation Provider TL only<br/>PuBPNot_03| APTL
    TLProvider -->|Submit TL URL<br/>GenNot_01| ECNotify
    ECNotify -->|Commission compiles & publishes<br/>Wallet Provider TL<br/>WPNot_04, WPNot_05| WPTL
    ECNotify -->|Commission compiles & publishes<br/>PID Provider TL<br/>PPNot_05| PIDTL
    ECNotify -->|Commission compiles & publishes<br/>Access CA TL<br/>PPNot_06, RPACANot_04| ACATL
    ECNotify -->|Commission compiles & publishes<br/>Registration Cert Provider TL<br/>RPACANot_04| RegCertTL
    ECNotify -->|Verify TL completeness<br/>GenNot_04| ECVerify
    ECVerify -->|Compile LoTL<br/>ETSI TS 119612 D.5| LoTLCompile
    LoTLCompile -->|Sign & Publish LoTL<br/>TLPub_06| LoTL
    LoTL -->|Contains pointers to| TL

    style MS fill:#e1f5ff
    style EC fill:#fff4e1
    style EntitiesScope fill:#e8f5e9
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

    Note over Entity,RegCertProv: Registration/Onboarding Process

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

This diagram shows the complete end-to-end process from entity registration through to Trusted List publication for **Attestation Providers only**. For PID Providers, after registration with Registrar, Member States notify them to the Commission for Trusted List inclusion. For Wallet Providers, Access CAs, and Registration Cert Providers, see [Section 2.1.1](#211-wallet-provider-notification) and [Overview](#overview).

```mermaid
sequenceDiagram
    participant Entity as Attestation Provider<br/>(PuB-EAA Provider)
    participant Registrar as Member State Registrar<br/>Reg_01, Reg_19, Reg_21
    participant Registry as Registry<br/>Reg_03, Reg_04
    participant AccessCA as Access Certificate Authority<br/>Reg_10
    participant TLP as Trusted List Provider<br/>(MS Component)
    participant ECNotify as European Commission<br/>Notification System<br/>GenNot_01
    participant ECVerify as European Commission<br/>Verification System<br/>GenNot_04
    participant LoTLCompile as European Commission<br/>LoTL Compilation<br/>ETSI TS 119612 D.5
    participant LoTL as List of Trusted Lists<br/>Signed by EC
    participant TL as Published Trusted Lists<br/>Signed by TLP

    Note over Entity,TL: Complete Flow: Registration → Trusted List Publication<br/>(Attestation Providers only)

    rect rgb(230, 245, 255)
        Note over Entity,Registry: Phase 1: Registration/Onboarding
        Entity->>Registrar: 1. Submit Registration Request<br/>(Identification, Entitlements, Trust Anchors)
        Note right of Entity: For Attestation Providers: Conformity assessment<br/>report (PuBPNot_02)
        
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
        Note right of TLP: Include trust anchors:<br/>Attestation Providers: Conformity assessment (PuBPNot_02)
        
        TLP->>TL: 9. Sign/Seal & Publish Attestation Provider TL<br/>(TLPub_05)
        Note right of TL: Published at MS TLP URL<br/>Machine-readable & human-readable
        
        TLP->>ECNotify: 10. Submit Attestation Provider TL URL to EC<br/>(GenNot_01)
        
        ECNotify->>ECVerify: 11. Verify TL Completeness & Compliance<br/>(GenNot_04)
        ECVerify->>LoTLCompile: 12. Compile List of Trusted Lists<br/>(ETSI TS 119612 D.5)
        LoTLCompile->>LoTL: 13. Sign/Seal & Publish LoTL<br/>(TLPub_06)
        LoTLCompile->>LoTLCompile: 14. Publish in OJEU<br/>(TLPub_06, TLPub_07)
    end
```

### 5.3.1 Submission and Update Models: Registration to Trusted List

The relationship between Registrar and Trusted List Provider (TLP) can be implemented in two ways (illustrated in Diagram 5.3). Note: The ARF ([Section 6.3.2](https://eudi.dev/2.5.0/architecture-and-reference-framework-main/#632-pid-provider-or-attestation-provider-registration-and-notification)) describes the registration and notification processes but does not explicitly specify these two implementation models. The models presented here are implementation approaches based on the ARF requirements:

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

**Model A (Automatic Trigger)** is recommended for logical coherence and operational efficiency. The Registrar, upon successful registration, should automatically trigger the TLP to compile, sign, and publish Trusted Lists (for Attestation Providers only). This results in:

- Automatic processing of registered Attestation Providers that require Trusted List inclusion.
- Synchronized Registry and Trusted Lists for Attestation Providers.
- Single point of registration for entities.
- Process managed by the Registrar, with TLP acting as the Trusted List publisher for Attestation Providers.

The TLP's role in this model is to:
- Receive registration completion notifications from Registrar (for Attestation Providers only).
- Extract trust anchors and relevant data from Registry.
- Compile Attestation Provider Trusted Lists according to ETSI TS 119 612 specifications.
- Sign/seal and publish Trusted Lists at publicly accessible URLs (per Member State).
- Submit Trusted List URLs to European Commission.

See [Overview](#overview) for Commission-compiled Trusted Lists process.

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
	Note over MS,LoTL: MS SHALL notify all PID Providers, PuB-EAA Providers,<br/>Wallet Providers, Access CAs, and Providers of Registration Certificates<br/>to the European Commission (GenNot_01)
	
	rect rgb(230, 245, 255)
		Note over MS,TL: Phase 1: MS TLP Compiles, Signs & Publishes Attestation Provider TL
		MS->>MS: 1. Compile Attestation Provider TL<br/>(PuBPNot_01, PuBPNot_02)
		Note right of MS: Conformity assessment report<br/>(PuBPNot_02)
		MS->>TL: 2. Sign/Seal & Publish Attestation Provider TL<br/>(TLPub_05)
		Note right of TL: Published at MS TLP URL<br/>ETSI TS 119612 format
	end
	
	rect rgb(255, 244, 225)
		Note over MS,ECNotify: Phase 2: MS Notification to EC
		MS->>ECNotify: 3a. Submit Attestation Provider TL URL<br/>(GenNot_01)
		Note right of MS: For PuB-EAA Providers only
		
		MS->>ECNotify: 3b. Notify PID Provider<br/>(GenNot_01, PPNot_02)
		Note right of MS: Identification data, Trust anchors,<br/>Access CA trust anchors, Service Supply Point
		
		MS->>ECNotify: 3c. Notify Wallet Provider<br/>(GenNot_01, WPNot_02)
		Note right of MS: Identification data,<br/>Wallet Provider trust anchors
		
		MS->>ECNotify: 3d. Notify Access CA<br/>(GenNot_01, RPACANot_02)
		Note right of MS: Identification data, Trust anchors
		
		MS->>ECNotify: 3e. Notify Registration Cert Provider<br/>(GenNot_01, RPACANot_02)
		Note right of MS: Identification data, Trust anchors
	end
	
	rect rgb(255, 230, 230)
		Note over ECVerify,LoTL: Phase 3: EC Compiles TLs, Verifies MS TLs, and Maintains LoTL
		ECNotify->>ECVerify: 4. Verify completeness & compliance<br/>(GenNot_04)
		Note right of ECVerify: Technical validation,<br/>Schema compliance, Verify TL signatures
		
		ECCompile->>ECCompile: 5. Compile Wallet Provider TL<br/>(WPNot_04, WPNot_05)
		ECCompile->>ECCompile: 6. Compile PID Provider TL<br/>(PPNot_05)
		ECCompile->>ECCompile: 7. Compile Access CA TL<br/>(PPNot_06, RPACANot_04)
		ECCompile->>ECCompile: 8. Compile Registration Cert Provider TL<br/>(RPACANot_04)
		
		ECVerify->>ECCompile: 9. Compile List of Trusted Lists<br/>(ETSI TS 119612 D.5)
		Note right of ECCompile: Create TrustedListPointers<br/>for EC-compiled TLs and MS TLP-compiled TLs
		
		ECCompile->>LoTL: 10. Sign/Seal & Publish LoTL<br/>(TLPub_06)
		ECCompile->>ECCompile: 11. Publish in OJEU<br/>(TLPub_06, TLPub_07)
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
        PIDTLPointer[PID Provider TL Pointer<br/>TSLLocation: EC URL<br/>SchemeTerritory: EU<br/>SchemeOperatorName: EC]
        APTLPointer[Attestation Provider TL Pointer<br/>TSLLocation: MS TLP URL<br/>SchemeTerritory: MS Code<br/>SchemeOperatorName: MS TLP]
        ACATLPointer[Access CA TL Pointer<br/>TSLLocation: EC URL<br/>SchemeTerritory: EU<br/>SchemeOperatorName: EC]
        RegCertTLPointer[Registration Cert Provider TL Pointer<br/>TSLLocation: EC URL<br/>SchemeTerritory: EU<br/>SchemeOperatorName: EC]
    end

    subgraph ActualTL["Actual Trusted Lists<br/>Referenced by Pointers"]
        WPTL[Wallet Provider TL<br/>WPNot_05, WPNot_07]
        PIDTL[PID Provider TL<br/>PPNot_07]
        APTL[Attestation Provider TL<br/>PuBPNot_03]
        ACATL[Access CA TL<br/>RPACANot_05]
        RegCertTL[Registration Cert Provider TL<br/>RPACANot_05]
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

    subgraph SubmissionUpdate["Attestation Provider TL Publication<br/>MS TLP (Attestation Providers only)"]
        TLPTrigger[MS TLP Triggered by Registration Completion]
        TLPCompile[Compile Attestation Provider TL<br/>Extract Trust Anchors from Registry]
        TLPPublish[Sign & Publish Attestation Provider TL<br/>TLPub_05]
    end

    subgraph Notification["MS Notification to EC<br/>GenNot_01"]
        NotifWP[MS notifies Wallet Provider<br/>WPNot_01, WPNot_02]
        NotifPID[MS notifies PID Provider<br/>PPNot_01, PPNot_02]
        NotifACA[MS notifies Access CA<br/>RPACANot_01, RPACANot_02]
        NotifRegCert[MS notifies Registration Cert Provider<br/>RPACANot_01, RPACANot_02]
        NotifAPTL[MS TLP submits Attestation Provider TL URL<br/>GenNot_01]
    end

    subgraph ECCompilation["EC Verification & LoTL Maintenance"]
        ECVerify[EC verifies all Trusted Lists<br/>GenNot_04]
        ECCompileLoTL[EC compiles LoTL<br/>ETSI TS 119612 D.5]
        ECPublishLoTL[EC signs & publishes LoTL<br/>TLPub_06]
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
        WPTL[Wallet Provider TL<br/>Per MS, compiled by MS TLP]
        PIDTL[PID Provider TL<br/>Per MS, compiled by MS TLP]
        APTL[Attestation Provider TL<br/>Per MS, compiled by MS TLP]
        ACATL[Access CA TL<br/>Per MS, compiled by MS TLP]
        RegCertTL[Registration Cert Provider TL<br/>Per MS, compiled by MS TLP]
    end

    %% Registration Flow (PID/Attestation Providers, RP)
    PID -->|Register| RegStep1
    AP -->|Register| RegStep1
    RP -->|Register| RegStep1
    RegStep1 --> RegStep2
    RegStep2 --> RegStep3
    RegStep3 --> RegStep4

    %% Attestation Provider TL Publication Flow
    RegStep4 -->|Registration Complete<br/>Triggers MS TLP| TLPTrigger
    TLPTrigger -->|Access Registry Data<br/>Extract Trust Anchors| TLPCompile
    TLPCompile -->|Compile Attestation Provider TL| TLPPublish
    TLPPublish -->|Sign & Publish at URL| NotifAPTL
    TLPPublish --> APTL

    %% Notification Flows (all entities notified to EC)
    WP -->|MS notifies| NotifWP
    PID -->|After registration, MS notifies| NotifPID
    ACA -->|MS notifies| NotifACA
    RegCertProv -->|MS notifies| NotifRegCert

    %% EC Compilation Flows
    NotifWP --> ECCompileWP
    NotifPID --> ECCompilePID
    NotifACA --> ECCompileACA
    NotifRegCert --> ECCompileRegCert
    NotifAPTL --> ECVerify

    ECCompileWP --> WPTL
    ECCompilePID --> PIDTL
    ECCompileACA --> ACATL
    ECCompileRegCert --> RegCertTL
    ECVerify --> ECCompileLoTL

    %% LoTL Compilation
    ECCompileWP --> ECCompileLoTL
    ECCompilePID --> ECCompileLoTL
    ECCompileACA --> ECCompileLoTL
    ECCompileRegCert --> ECCompileLoTL
    ECCompileLoTL --> ECPublishLoTL
    ECPublishLoTL --> TrustedLists

    %% Note: Registration data feeds into Trusted Lists
    RegStep4 -.->|Registry data used for<br/>trust evaluation| TrustedLists

    style Registration fill:#e8f5e9
    style SubmissionUpdate fill:#fff9c4
    style Notification fill:#ffe0b2
    style ECCompilation fill:#fff4e1
    style Entities fill:#f3e5f5
    style TrustedLists fill:#e1f5ff
```

## 6. Key Distinctions

### 6.1 Registration vs. Trusted List Publication

| Aspect | Registration | Trusted List Publication |
|--------|-------------|---------------------------|
| **Purpose** | Enable entity participation in ecosystem | Establish trust anchors for validation |
| **Managed By** | Member State Registrar | EC compiles & publishes TLs: Wallet Provider, PID Provider, Access CA, Registration Cert Provider; MS TLP compiles & publishes Attestation Provider TL per MS; EC maintains LoTL |
| **Scope** | PID Providers, Attestation Providers, Relying Parties. (PID Providers are subsequently notified to Commission). | Selected entities: Wallet Providers (TL compiled by EC), PID Providers (TL compiled by EC), Attestation Providers (per MS TL compiled by MS TLP), Access CAs (TL compiled by EC), Registration Cert Providers (TL compiled by EC) |
| **Output** | Registry entries, Access Certificates, Registration Certificates | Trusted Lists: Wallet Provider TL (compiled by EC), PID Provider TL (compiled by EC), Attestation Provider TL (per MS, compiled by MS TLP), Access CA TL (compiled by EC), Registration Cert Provider TL (compiled by EC); List of Trusted Lists (compiled by EC) |
| **Used For** | Entitlement verification, service access | Cryptographic trust validation |
| **Requirements** | Reg_01, Reg_10, RPRC_09, RPRC_13 | GenNot_01, TLPub_01, TLPub_05, TLPub_06 |
| **Submission and Update** | Managed by Registrar | Varies by entity type (see [Overview](#overview) and [Section 5.3](#53-complete-registration-to-trusted-list-publication-flow)). |

## 9. Summary

The trust infrastructure operates through two distinct but complementary processes:

1. **Registration/Onboarding**: Managed at Member State level, entities (PID Providers, Attestation Providers, Relying Parties) register with Registrars and entitlements are defined. PID Providers are also notified by Member States to the Commission for Trusted List inclusion. See [Overview](#overview) for entity registration responsibilities.
2. **Trusted List Publication**: The European Commission compiles Trusted Lists for Wallet Providers, PID Providers, Access CAs, and Registration Cert Providers. Member State TLPs compile Trusted Lists per Member State for Attestation Providers. See [Overview](#overview) for Trusted List compilation responsibilities.

Both processes are required for the trust ecosystem:
- **Registration**: Defines operational authorization and entitlement management.
- **Trusted Lists**: Contain cryptographic trust anchors for signature and certificate validation.

The separation of these processes aligns with the ARF and enables:
- Independent lifecycle management.
- Different trust models (operational vs. cryptographic).
- Scalable cross-border trust establishment.
- Clear separation of concerns between MS and EU levels.
- Trusted Lists compiled by the European Commission (Wallet Provider, PID Provider, Access CA, Registration Cert Provider) for consistent recognition across all Member States.
- Member State-level Trusted Lists (Attestation Provider) for Member State-specific management.

## 7. Implementation Considerations

### 7.1 Member State Autonomous Trusted Lists

Member States may publish additional Trusted Lists within their own perimeter for internal or national purposes, beyond the eIDAS Trusted Lists published by the European Commission. These Member State-specific Trusted Lists are not normative or usable by other Member States, as only the eIDAS Trusted Lists published by the European Commission (for Wallet Providers, PID Providers, Access CAs, and Registration Cert Providers) and the Attestation Provider Trusted Lists published by Member State TLPs (which are included in the Commission's List of Trusted Lists) are recognized for cross-border trust establishment in the EUDI Wallet ecosystem.

## 8. Trust Evaluation

> **Note**: This section describes trust evaluation processes that use the registration data and Trusted Lists established through the onboarding and Trusted List publication processes described in the main document. As the focus of this document is on **Onboarding (Registration)** and **Trusted List Publication** processes, this section is provided for reference but could be moved to a separate document in the future.

This section describes how trust is evaluated in the ecosystem using the registration data and Trusted Lists established through the onboarding and Trusted List publication processes.

### 8.1 Trust Evaluation Requirements

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

### 8.2 Trust Evaluation Flow

> ⚠️ **Warning**: The content of this section is temporary and will be removed or replaced as it is updated using reference material under development in [https://github.com/webuild-consortium/wp4-trust-group/pull/33](https://github.com/webuild-consortium/wp4-trust-group/pull/33).


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

### 8.3 Trust Evaluation Points

Trust evaluation occurs at multiple points using different trust sources:

1. **During Credential Issuance**:
   - Wallet Units verify Provider registration (Registry) - **ISSU_24a, ISSU_34a**
   - Providers verify Wallet Provider in Trusted List - **ISSU_21, ISSU_30**

2. **During Presentation**:
   - Wallet Units verify Relying Party registration (Registry) - **RPRC_16, RPRC_21**
   - Wallet Units verify Access Certificates using Trusted Lists - **ISSU_24, ISSU_34, RPA_04**
   - Relying Parties validate PID signatures using PID Provider TL - **OIA_12**
   - Relying Parties validate attestation signatures using Attestation Provider TL - **OIA_13, OIA_14**

