# WP4 Trust Group: Consolidated Terms and Entity Definitions

This document is the single source of truth for **terms**, **acronyms**, and **entity definitions** used across WP4 Trust Group deliverables. Other documents in the repository reference this document to avoid duplicating definitions.

**Scope**: EUDI Wallet ecosystem trust infrastructure, onboarding, and trust evaluation, aligned with the [EUDI Wallet Architecture and Reference Framework (ARF)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/).

---

## 1. Acronyms

| Acronym | Meaning | Source |
|---------|---------|--------|
| **ARF** | Architecture and Reference Framework (EUDI Wallet) | ARF |
| **CAB** | Conformity Assessment Body | ARF |
| **CA** | Certificate Authority | ARF |
| **EC** | European Commission | ARF |
| **EAA Provider** | non-qualified Electronic Attestation of Attributes Provider | ARF |
| **EUDI** | European Digital Identity | ARF |
| **EUDIW** | European Digital Identity Wallet | Regulation (EU) 2024/1183 |
| **LoTL** | List of Trusted Lists | ARF, ETSI TS 119 612 |
| **MS** | Member State | ARF |
| **MS TLP** | Member State Trusted List Provider | ARF |
| **NAB** | National Accreditation Body | ARF |
| **PID** | Person Identification Data | ARF |
| **PuB-EAA Provider** | Public Sector Body Electronic Attestation of Attributes Provider | ARF |
| **QEAA Provider** | Qualified Electronic Attestation of Attributes Provider (a QTSP under eIDAS) | ARF |
| **QTSP** | Qualified Trust Service Provider (under eIDAS) | eIDAS Regulation |
| **RP** | Relying Party | ARF |
| **TL** | Trusted List | ARF |
| **TLP** | Trusted List Provider | ARF |
| **WP** | Wallet Provider | ARF |
| **WUA** | Wallet Unit Attestation | ARF |

---

## 2. Key Terminology

### 2.1 Wallet-Related Terms (per Regulation (EU) 2024/1183)

- **wallet solution**: A combination of software, hardware, services, settings, and configurations, including wallet instances, one or more wallet secure cryptographic applications and one or more wallet secure cryptographic devices.
- **wallet instance**: The application installed and configured on a wallet user's device or environment, which is part of a wallet unit, and that the wallet user uses to interact with the wallet unit.
- **wallet unit**: A unique configuration of a wallet solution that includes wallet instances, wallet secure cryptographic applications and wallet secure cryptographic devices provided by a wallet provider to an individual wallet user.
- **wallet provider**: A natural or legal person who provides wallet solutions.

### 2.2 Trust Infrastructure Terms

- **Registrar**: Established by Member States to manage the registration and operational authorization of PID Providers, Attestation Providers, and Relying Parties (ARF Section 3.17).
- **Access Certificate Authority**: Issues access certificates to registered entities (PID Providers, Attestation Providers, Relying Parties) for authentication during service interactions (ARF Section 3.18).
- **Provider of Registration Certificates**: Optionally issues certificates detailing entitlements for registered entities (ARF Section 3.19).
- **Trusted List Provider (TLP)**: A body responsible for maintaining, managing, and publishing a Trusted List (ARF Section 3.5).
- **Member State Trusted List Provider (MS TLP)**: Compiles, signs, and publishes national Trusted Lists for non-qualified EAA Providers and Member State QTSP Trusted Lists for QEAA Providers.
- **Trusted List (TL)**: A list containing trust anchors for validation purposes, published by Trusted List Providers.
- **List of Trusted Lists (LoTL)**: Maintained by the European Commission, contains pointers to all published Trusted Lists (ETSI TS 119 612 D.5).
- **Registry**: Publicly accessible register maintained by Registrars containing registration information about entities.
- **Access Certificate**: Certificate issued by Access Certificate Authority to registered entities for authentication.
- **Registration Certificate**: Optional certificate issued by Provider of Registration Certificates detailing entity entitlements.

### 2.3 Entity Types (Short Definitions)

- **PID Provider**: Provider issuing Person Identification Data to Wallet Units.
- **Attestation Provider**: Provider issuing electronic attestations of attributes (includes QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers).
- **QEAA Provider**: Qualified Electronic Attestation of Attributes Provider (a Qualified Trust Service Provider under eIDAS).
- **PuB-EAA Provider**: Public Sector Body Electronic Attestation of Attributes Provider.
- **EAA Provider**: non-qualified Electronic Attestation of Attributes Provider.
- **Relying Party (RP)**: Service that requests attributes from Wallet Units to provide services to users.
- **Wallet Provider (WP)**: Natural or legal person who provides wallet solutions.
- **Intermediary**: Special class of Relying Party that acts on behalf of other Relying Parties.

---

## 3. Core Trust Infrastructure Entities (Detailed)

The following entities are involved in trust evaluation, trust registry, and trust infrastructure in the EUDI Wallet ecosystem (per EUDIW ARF).

### 3.1 Trusted List Provider (TLP)

- **Role**: Maintains, manages, and publishes Trusted Lists.
- **Responsibilities**: Maintains Trusted Lists for Wallet Providers, PID Providers, QEAA Providers, PuB-EAA Providers, QESRC Providers, Access Certificate Authorities, and Providers of registration certificates; signs/seals Trusted Lists; publishes Trusted Lists in machine-readable and human-readable formats.
- **Trust Evaluation Role**: Provides the authoritative source of trust anchors for entities in the ecosystem.

### 3.2 European Commission

- **Role**: Establishes technical specifications and compiles Trusted Lists.
- **Responsibilities**: Establishes technical specifications for information to be notified about various entities; receives notifications from Member States; verifies completeness and technical compliance of notified data; compiles, signs/seals, and publishes Trusted Lists; maintains the List of Trusted Lists; establishes standard operating procedures for suspension/cancellation; publishes Trusted List locations and trust anchors in the OJEU.
- **Trust Evaluation Role**: Central authority that validates, consolidates, and publishes trust information.

### 3.3 Member States

- **Role**: Notify entities to the Commission and establish registries.
- **Responsibilities**: Notify PID Providers, PuB-EAA Providers, Wallet Providers, Access Certificate Authorities, and Providers of registration certificates to the European Commission; establish and maintain registries for PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties; approve entities according to well-defined policies before registration; identify entities at appropriate confidence levels; define vetting processes and rules of acceptance; publish registry entries online in machine-readable and human-readable formats; support common APIs for automated retrieval of registry entries; log all changes to registered information.
- **Trust Evaluation Role**: First line of trust evaluation — approve and register entities based on defined policies.

### 3.4 Registrars

- **Role**: Manage the registration of Providers and Relying Parties.
- **Responsibilities**: Register PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties; maintain registration data (for Relying Parties: attributes they intend to request, intended use, intermediary relationships; for Providers: attestation types they intend to issue); publish registry entries online; enable updates; suspend or cancel registered entities; verify evidence provided during registration.
- **Trust Evaluation Role**: Conduct registration processes and maintain registration data that supports trust evaluation.

### 3.5 Access Certificate Authority (Access CA)

- **Role**: Issue access certificates for authentication.
- **Responsibilities**: Issue access certificates to all PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties registered in Member State registries; comply with common Certificate Policy for Access Certificate Authority; log all issued access certificates for Certificate Transparency (CT); provide revocation methods; revoke certificates when entities are suspended/cancelled; act as monitors in the CT ecosystem.
- **Trust Evaluation Role**: Provide cryptographic proof of entity authenticity and validity through access certificates.

### 3.6 Provider of Registration Certificates

- **Role**: Issue certificates detailing registration status and scope.
- **Responsibilities**: Issue registration certificates to registered entities (if Registrar policy requires it); create separate registration certificates for each intended use (for Relying Parties); sign/seal registration certificates; comply with common Certificate Policy for registration certificates; revoke registration certificates when suspended/cancelled.
- **Trust Evaluation Role**: Provide cryptographic proof of registration status and scope, enabling verification of entity entitlements.

### 3.7 Conformity Assessment Body (CAB)

- **Role**: Certify Wallet Solutions and audit Trust Service Providers.
- **Responsibilities**: Certify Wallet Solutions against normative documents; audit Qualified Trust Service Providers (QTSPs) regularly; carry out assessments on which Member States rely before issuing a Wallet Solution or providing 'qualified' status to a Trust Service Provider.
- **Trust Evaluation Role**: Assess and certify compliance of Wallet Solutions and audit Trust Service Providers.

### 3.8 National Accreditation Body (NAB)

- **Role**: Accredit CABs according to EU regulations.
- **Responsibilities**: Accredit CABs as competent, independent, and supervised professional certification bodies; monitor CABs to which they have issued accreditation certificates; perform accreditation with authority derived from Member States under Regulation (EC) No 765/2008.
- **Trust Evaluation Role**: Ensure CABs are competent and independent.

### 3.9 Supervisory Body

- **Role**: Review the proper functioning of ecosystem actors.
- **Responsibilities**: Review proper functioning of Wallet Providers and other actors in the EUDI Wallet ecosystem; created and appointed by Member States; notified to the Commission by Member States.
- **Trust Evaluation Role**: Ongoing oversight and review of ecosystem actors to ensure continued compliance.

### 3.10 PID Provider

- **Role**: Issue Person Identification Data (PID) to Users.
- **Trust Evaluation Involvement**: Must be registered by a Registrar; must be approved by Member State according to well-defined policy; must be identified at appropriate confidence level; receives access certificate from Access Certificate Authority; may receive registration certificate from Provider of registration certificates; trust anchors notified to Commission and published in PID Provider Trusted List.

### 3.11 QEAA Provider (Qualified Electronic Attestation of Attributes Provider)

- **Role**: Issue Qualified Electronic Attestations of Attributes.
- **Trust Evaluation Involvement**: Must be registered by a Registrar; must be approved by Member State according to well-defined policy; must be identified at appropriate confidence level; receives access certificate from Access Certificate Authority; may receive registration certificate from Provider of registration certificates; trust anchors notified to Commission and published in QEAA Provider Trusted List; audited regularly by CABs.

### 3.12 PuB-EAA Provider (Public Sector EAA Provider)

- **Role**: Issue EAAs on behalf of a public sector body responsible for an Authentic Source.
- **Trust Evaluation Involvement**: Must be registered by a Registrar; must be approved by Member State according to well-defined policy; must be identified at appropriate confidence level; must provide conformity assessment report from CAB; receives access certificate from Access Certificate Authority; may receive registration certificate from Provider of registration certificates; trust anchors notified to Commission and published in PuB-EAA Provider Trusted List.

### 3.13 EAA Provider (Non-Qualified Electronic Attestation of Attributes Provider)

- **Role**: Issue Non-Qualified Electronic Attestations of Attributes.
- **Trust Evaluation Involvement**: Must be registered by a Registrar; must be approved by Member State according to well-defined policy; must be identified at appropriate confidence level; receives access certificate from Access Certificate Authority; may receive registration certificate from Provider of registration certificates; may use alternative trust models and verification mechanisms.

### 3.14 Wallet Provider

- **Role**: Make certified Wallet Solutions available to Users.
- **Trust Evaluation Involvement**: Wallet Solutions must be certified by CABs; trust anchors notified to Commission and published in Wallet Provider Trusted List; can be suspended or cancelled by Commission; supervised by Supervisory Bodies.

### 3.15 Relying Party (RP)

- **Role**: Request and receive attributes from a Wallet Unit.
- **Trust Evaluation Involvement**: Must be registered by a Registrar; must be identified at appropriate confidence level; receives access certificate(s) from Access Certificate Authority (one per Relying Party Instance); may receive registration certificate(s) from Provider of registration certificates (one per intended use); registration data includes attributes they intend to request and intended use; can be cancelled by Registrar.

### 3.16 Intermediary

- **Role**: Special class of Relying Party that acts on behalf of other Relying Parties.
- **Trust Evaluation Involvement**: Must register as a Relying Party, indicating intent to act as intermediary; must register each intermediated Relying Party at appropriate Registrar; must provide legally valid evidence of relationship with intermediated Relying Party; receives access certificates and registration certificates; relationship with intermediated Relying Party must be registered and verifiable.

### 3.17 Attestation Scheme Provider

- **Role**: Define and publish Attestation Rulebooks and schemes.
- **Trust Evaluation Involvement**: Defines trust models for attestations; publishes attestation schemes in catalogue; European Commission publishes PID Rulebook; Commission operates catalogue of schemes and Rulebooks.

### 3.18 Authentic Source

- **Role**: Act as definitive repository for specific attributes.
- **Trust Evaluation Involvement**: PuB-EAA Providers issue EAAs based on Authentic Sources; Authentic Sources are referenced in PuB-EAA Provider notifications; catalogue of attributes references Authentic Sources.

---

## 4. WEBUILD-Specific Entities

### 4.1 Trust Infrastructure Responsible Group

The **Trust Infrastructure Responsible Group** is a designated group within the WEBUILD WP4 Trust Infrastructure group that performs the Responsible (R) role in RACI matrices for onboarding processes during the WEBUILD MVP phase. This group is responsible for executing tasks and deliverables related to trust infrastructure operations, including but not limited to:

- Managing onboarding requests and data collection
- Reviewing entity data and making recommendations
- Maintaining and updating Trusted Lists
- Hosting Trusted Lists
- Engaging with entities during onboarding and troubleshooting

The following table lists the entities that are part of the Trust Infrastructure Responsible Group:

| Entity | Legal Name | Website | Administrative Contact | Technical Contact |
|--------|------------|---------|------------------------|------------------|
| IDunion SCE | GER-IDunion SCE | [https://www.idunion.eu](https://www.idunion.eu) | [info@idunion.eu](mailto:info@idunion.eu) | [info@idunion.eu](mailto:info@idunion.eu) |
| Forkbomb | Forkbomb BV | [https://forkbomb.eu](https://forkbomb.eu) | [info@forkbomb.eu](mailto:info@forkbomb.eu) | [info@forkbomb.eu](mailto:info@forkbomb.eu) |
| Department for digital transformation | Department for digital transformation | [https://innovazione.gov.it](https://innovazione.gov.it) | [g.messori@innovazione.gov.it](mailto:g.messori@innovazione.gov.it) | [gi.demarco@innovazione.gov.it](mailto:gi.demarco@innovazione.gov.it) |

**Note**: Additional entities may be added to this group as designated by the WP4 Trust Infrastructure group. Consortium participants can propose themselves by applying a Pull Request to add themselves to the list and be actively involved in the registration operations and review processes.

RACI (Responsible, Accountable, Consulted, Informed) definitions and the RACI matrices for onboarding are kept in the onboarding documents: [Base Onboarding Framework](subtask1-1-onboarding/onboarding-base.md#raci-matrix) and in each use case document (Relying Party, PID/EAA Provider, Wallet Provider).

---

## 5. MVP and MVP+ Definitions

Onboarding use cases distinguish between two phases. Entity-specific onboarding documents reference these definitions and do not duplicate them.

### 5.1 MVP

**MVP** (Minimum Viable Product) refers to the WEBUILD testing/pilot phase:

- The WP4 Trust Infrastructure group acts as **Ecosystem Authority** (and, where applicable, as Registrar, Access Certificate Authority, Provider of Registration Certificates, and Trusted List Provider).
- All participating entities (Relying Parties, PID/EAA Providers, Wallet Providers) **register** with the WEBUILD WP4 Trust Infrastructure group for the purposes of the pilot.
- Registers and Trusted Lists are maintained by the WP4 Trust Infrastructure group for WEBUILD testing.

**MVP trust infrastructure**: The WEBUILD pilot uses a **List of Trusted Lists (LoTL)** that references one or more **Trusted Lists (TL)** (e.g. one TL for PID/EAA Providers, one for Wallet Providers, as needed per entity type). The **LoTL is the trust anchor** in the ETSI TS 119 612 model. The WEBUILD LoTL references the relevant TL(s); each TL in turn references the trust anchor used to issue Access and Registration Certificates (and, where applicable, other trust anchors for entity listing).

### 5.2 MVP+

**MVP+** refers to the production/regulatory phase aligned with EU regulations and Member State implementations:

- Registration and notification follow the [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).
- **Registration**: PID Providers, Attestation Providers, and Relying Parties register with **Member State Registrars**.
- **Notification**: Wallet Providers, Access Certificate Authorities, and Providers of Registration Certificates are **notified** by Member States to the European Commission (they do not register with Registrars).
- Trust anchors are published via Trusted Lists and National Registers as defined in the Trust Infrastructure Schema.

---

## 6. Policy and Framework Terms

### 6.1 Authentication (Trust Framework)

**Definition**: The process of verifying the identity of a subject (User, system, or entity) to ensure they are who they claim to be within a trust framework.

**Key Characteristics**: Identity verification; trust evidence validation; trust session establishment; foundation for subsequent authorization decisions.

*Source: [Authentication vs Authorization Policy Framework](../task2-trust-framework/authentication-authorization-policy-framework.md).*

### 6.2 Authorization (Trust Framework)

**Definition**: The process of determining what actions a subject is permitted to perform or what resources they can access after successful authentication within a trust framework.

**Key Characteristics**: Trust permission granting; resource access control; trust policy enforcement; context-aware trust.

*Source: [Authentication vs Authorization Policy Framework](../task2-trust-framework/authentication-authorization-policy-framework.md).*

### 6.3 Additive Policy Approach

**Definition**: Implements an explicit allow-list model where permissions are granted only when explicitly authorized. Principle: **"Nothing is permitted unless explicitly allowed."**

**Characteristics**: Default action: deny all; authorization model: explicit allow-list; security posture: conservative, high-security; configuration: grant specific permissions. Suitable for zero-trust and high-security environments.

*Source: [Policy Approaches Definition](../task5-participants-certificates-policies/policy-approaches-definition.md).*

### 6.4 Subtractive Policy Approach

**Definition**: Implements an explicit deny-list model where permissions are granted by default except where explicitly restricted. Principle: **"Everything is permitted unless explicitly denied."**

**Characteristics**: Default action: allow all; authorization model: explicit deny-list; security posture: permissive; configuration: block specific restrictions. Suitable for open ecosystems and development.

*Source: [Policy Approaches Definition](../task5-participants-certificates-policies/policy-approaches-definition.md).*

---

## 7. Trust Infrastructure Relationships (Summary)

Main relationships among trust infrastructure entities:

1. **Member States → Registrars**: Member States establish and oversee Registrars.
2. **Registrars → Registered Entities**: Registrars register and approve entities.
3. **Member States → Access Certificate Authorities**: Member States notify Access CAs to Commission.
4. **Access Certificate Authorities → Registered Entities**: Access CAs issue access certificates.
5. **Registrars → Providers of Registration Certificates**: Registrars may have associated Providers of registration certificates.
6. **Providers of Registration Certificates → Registered Entities**: Issue registration certificates.
7. **Member States → European Commission**: Member States notify entities to Commission.
8. **European Commission → Trusted List Provider**: Commission compiles and publishes Trusted Lists.
9. **Trusted List Provider → Ecosystem**: Publishes Trusted Lists for use by all entities.
10. **NABs → CABs**: NABs accredit CABs.
11. **CABs → Wallet Providers / Trust Service Providers**: CABs certify/audit providers.
12. **Supervisory Bodies → Ecosystem Actors**: Supervisory Bodies review proper functioning.

---

## 8. Trust Evaluation Criteria (Summary)

Entities are evaluated for trust based on:

- **Registration**: Proper registration with appropriate Registrar.
- **Approval**: Approval by Member State according to well-defined policy.
- **Identification**: Identification at confidence level proportionate to risk.
- **Certification**: Certification by CAB (for Wallet Solutions).
- **Audit**: Regular audits by CABs (for Trust Service Providers).
- **Conformity Assessment**: Conformity assessment reports (for PuB-EAA Providers).
- **Trust Anchors**: Valid trust anchors in Trusted Lists.
- **Certificates**: Valid access certificates and registration certificates.
- **Compliance**: Ongoing compliance with requirements and policies.
