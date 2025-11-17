# Entities Involved in Trust Evaluation

This document extracts the list of entities involved in trust evaluation, trust registry, and trust infrastructure in the EUDI Wallet ecosystem.

## Core Trust Infrastructure Entities

### 1. Trusted List Provider (TLP)
- **Role**: Maintains, manages, and publishes Trusted Lists
- **Responsibilities**:
  - Maintains Trusted Lists for Wallet Providers, PID Providers, QEAA Providers, PuB-EAA Providers, QESRC Providers, Access Certificate Authorities, and Providers of registration certificates
  - Signs/seals Trusted Lists
  - Publishes Trusted Lists in machine-readable and human-readable formats
- **Trust Evaluation Role**: Provides the authoritative source of trust anchors for entities in the ecosystem

### 2. European Commission
- **Role**: Establishes technical specifications and compiles Trusted Lists
- **Responsibilities**:
  - Establishes technical specifications for information to be notified about various entities
  - Receives notifications from Member States
  - Verifies completeness and technical compliance of notified data
  - Compiles, signs/seals, and publishes Trusted Lists
  - Maintains the List of Trusted Lists (common trust infrastructure)
  - Establishes standard operating procedures for suspension/cancellation
  - Publishes Trusted List locations and trust anchors in the OJEU (Official Journal of the European Union)
- **Trust Evaluation Role**: Central authority that validates, consolidates, and publishes trust information

### 3. Member States
- **Role**: Notify entities to the Commission and establish registries
- **Responsibilities**:
  - Notify PID Providers, PuB-EAA Providers, Wallet Providers, Access Certificate Authorities, and Providers of registration certificates to the European Commission
  - Establish and maintain registries for PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties
  - Approve entities according to well-defined policies before registration
  - Identify entities at appropriate confidence levels
  - Define vetting processes and rules of acceptance
  - Publish registry entries online in machine-readable and human-readable formats
  - Support common APIs for automated retrieval of registry entries
  - Log all changes to registered information
- **Trust Evaluation Role**: First line of trust evaluation - approve and register entities based on defined policies

### 4. Registrars
- **Role**: Manage the registration of Providers and Relying Parties
- **Responsibilities**:
  - Register PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties
  - Maintain registration data including:
    - For Relying Parties: attributes they intend to request, intended use, intermediary relationships
    - For Providers: attestation types they intend to issue
  - Publish registry entries online
  - Enable updates to registered information
  - Suspend or cancel registered entities
  - Verify evidence provided during registration (e.g., intermediary relationships)
- **Trust Evaluation Role**: Conduct registration processes and maintain registration data that supports trust evaluation

## Certificate Authority Entities

### 5. Access Certificate Authority (Access CA)
- **Role**: Issue access certificates for authentication
- **Responsibilities**:
  - Issue access certificates to all PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties registered in Member State registries
  - Comply with common Certificate Policy for Access Certificate Authority
  - Log all issued access certificates for Certificate Transparency (CT)
  - Provide revocation methods
  - Revoke certificates when entities are suspended/cancelled
  - Act as monitors in the CT ecosystem
- **Trust Evaluation Role**: Provide cryptographic proof of entity authenticity and validity through access certificates

### 6. Provider of Registration Certificates
- **Role**: Issue certificates detailing registration status and scope
- **Responsibilities**:
  - Issue registration certificates to registered entities (if Registrar policy requires it)
  - Create separate registration certificates for each intended use (for Relying Parties)
  - Sign/seal registration certificates
  - Comply with common Certificate Policy for registration certificates
  - Revoke registration certificates when suspended/cancelled
- **Trust Evaluation Role**: Provide cryptographic proof of registration status and scope, enabling verification of entity entitlements

## Conformity Assessment and Accreditation Entities

### 7. Conformity Assessment Body (CAB)
- **Role**: Certify Wallet Solutions and audit Trust Service Providers
- **Responsibilities**:
  - Certify Wallet Solutions against normative documents
  - Audit Qualified Trust Service Providers (QTSPs) regularly
  - Carry out assessments on which Member States rely before:
    - Issuing a Wallet Solution
    - Providing 'qualified' status to a Trust Service Provider
- **Trust Evaluation Role**: Assess and certify compliance of Wallet Solutions and audit Trust Service Providers to ensure they meet requirements

### 8. National Accreditation Body (NAB)
- **Role**: Accredit CABs according to EU regulations
- **Responsibilities**:
  - Accredit CABs as competent, independent, and supervised professional certification bodies
  - Monitor CABs to which they have issued accreditation certificates
  - Perform accreditation with authority derived from Member States under Regulation (EC) No 765/2008
- **Trust Evaluation Role**: Ensure CABs are competent and independent, providing trust in the certification process

### 9. Supervisory Body
- **Role**: Review the proper functioning of ecosystem actors
- **Responsibilities**:
  - Review proper functioning of Wallet Providers and other actors in the EUDI Wallet ecosystem
  - Created and appointed by Member States
  - Notified to the Commission by Member States
- **Trust Evaluation Role**: Ongoing oversight and review of ecosystem actors to ensure continued compliance

## Registered Service Provider Entities

### 10. PID Provider
- **Role**: Issue Person Identification Data (PID) to Users
- **Trust Evaluation Involvement**:
  - Must be registered by a Registrar
  - Must be approved by Member State according to well-defined policy
  - Must be identified at appropriate confidence level
  - Receives access certificate from Access Certificate Authority
  - May receive registration certificate from Provider of registration certificates
  - Trust anchors notified to Commission and published in PID Provider Trusted List

### 11. QEAA Provider (Qualified Electronic Attestation of Attributes Provider)
- **Role**: Issue Qualified Electronic Attestations of Attributes
- **Trust Evaluation Involvement**:
  - Must be registered by a Registrar
  - Must be approved by Member State according to well-defined policy
  - Must be identified at appropriate confidence level
  - Receives access certificate from Access Certificate Authority
  - May receive registration certificate from Provider of registration certificates
  - Trust anchors notified to Commission and published in QEAA Provider Trusted List
  - Audited regularly by CABs

### 12. PuB-EAA Provider (Public Sector EAA Provider)
- **Role**: Issue EAAs on behalf of a public sector body responsible for an Authentic Source
- **Trust Evaluation Involvement**:
  - Must be registered by a Registrar
  - Must be approved by Member State according to well-defined policy
  - Must be identified at appropriate confidence level
  - Must provide conformity assessment report from CAB confirming requirements are met
  - Receives access certificate from Access Certificate Authority
  - May receive registration certificate from Provider of registration certificates
  - Trust anchors notified to Commission and published in PuB-EAA Provider Trusted List

### 13. EAA Provider (Non-Qualified Electronic Attestation of Attributes Provider)
- **Role**: Issue Non-Qualified Electronic Attestations of Attributes
- **Trust Evaluation Involvement**:
  - Must be registered by a Registrar
  - Must be approved by Member State according to well-defined policy
  - Must be identified at appropriate confidence level
  - Receives access certificate from Access Certificate Authority
  - May receive registration certificate from Provider of registration certificates
  - May use alternative trust models and verification mechanisms

### 14. Wallet Provider
- **Role**: Make certified Wallet Solutions available to Users
- **Trust Evaluation Involvement**:
  - Wallet Solutions must be certified by CABs
  - Trust anchors notified to Commission and published in Wallet Provider Trusted List
  - Can be suspended or cancelled by Commission
  - Supervised by Supervisory Bodies

### 15. Relying Party (RP)
- **Role**: Request and receive attributes from a Wallet Unit
- **Trust Evaluation Involvement**:
  - Must be registered by a Registrar
  - Must be identified at appropriate confidence level
  - Receives access certificate(s) from Access Certificate Authority (one per Relying Party Instance)
  - May receive registration certificate(s) from Provider of registration certificates (one per intended use)
  - Registration data includes attributes they intend to request and intended use
  - Can be cancelled by Registrar

### 16. Intermediary
- **Role**: Special class of Relying Party that acts on behalf of other Relying Parties
- **Trust Evaluation Involvement**:
  - Must register as a Relying Party, indicating intent to act as intermediary
  - Must register each intermediated Relying Party at appropriate Registrar
  - Must provide legally valid evidence of relationship with intermediated Relying Party
  - Receives access certificates and registration certificates
  - Relationship with intermediated Relying Party must be registered and verifiable

## Supporting Entities

### 17. Attestation Scheme Provider
- **Role**: Define and publish Attestation Rulebooks and schemes
- **Trust Evaluation Involvement**:
  - Defines trust models for attestations
  - Publishes attestation schemes in catalogue
  - European Commission publishes PID Rulebook
  - Commission operates catalogue of schemes and Rulebooks

### 18. Authentic Source
- **Role**: Act as definitive repository for specific attributes
- **Trust Evaluation Involvement**:
  - PuB-EAA Providers issue EAAs based on Authentic Sources
  - Authentic Sources are referenced in PuB-EAA Provider notifications
  - Catalogue of attributes references Authentic Sources

## Trust Evaluation Relationships

The trust evaluation process involves the following key relationships:

1. **Member States -> Registrars**: Member States establish and oversee Registrars
2. **Registrars -> Registered Entities**: Registrars register and approve entities
3. **Member States -> Access Certificate Authorities**: Member States notify Access CAs to Commission
4. **Access Certificate Authorities -> Registered Entities**: Access CAs issue access certificates
5. **Registrars -> Providers of Registration Certificates**: Registrars may have associated Providers of registration certificates
6. **Providers of Registration Certificates -> Registered Entities**: Issue registration certificates
7. **Member States -> European Commission**: Member States notify entities to Commission
8. **European Commission -> Trusted List Provider**: Commission compiles and publishes Trusted Lists
9. **Trusted List Provider -> Ecosystem**: Publishes Trusted Lists for use by all entities
10. **NABs -> CABs**: NABs accredit CABs
11. **CABs -> Wallet Providers/Trust Service Providers**: CABs certify/audit providers
12. **Supervisory Bodies -> Ecosystem Actors**: Supervisory Bodies review proper functioning

## Trust Evaluation Criteria

Entities are evaluated for trust based on:

- **Registration**: Proper registration with appropriate Registrar
- **Approval**: Approval by Member State according to well-defined policy
- **Identification**: Identification at confidence level proportionate to risk
- **Certification**: Certification by CAB (for Wallet Solutions)
- **Audit**: Regular audits by CABs (for Trust Service Providers)
- **Conformity Assessment**: Conformity assessment reports (for PuB-EAA Providers)
- **Trust Anchors**: Valid trust anchors in Trusted Lists
- **Certificates**: Valid access certificates and registration certificates
- **Compliance**: Ongoing compliance with requirements and policies

