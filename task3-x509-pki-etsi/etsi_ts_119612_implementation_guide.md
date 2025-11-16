# ETSI TS 119 612 v2.4.1 Implementation Guide

## Document Information
- **Standard**: [ETSI TS 119 612 V2.4.1 (2025-11)](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf)
- **Title**: Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists
- **Reference**: RTS/ESI-0019612v241
- **Keywords**: e-commerce, electronic signature, security, trust services

## Table of Contents
1. [Overview](#1-overview)
2. [Implementation Tasks](#2-implementation-tasks)
3. [Technical Requirements](#3-technical-requirements)
4. [XML Schema Implementation](#4-xml-schema-implementation)
5. [Service Type Mappings](#5-service-type-mappings)
6. [Status Management](#6-status-management)
7. [Digital Signature Implementation](#7-digital-signature-implementation)
8. [Distribution and Transport](#8-distribution-and-transport)
9. [Examples](#9-examples)
10. [Testing and Validation](#10-testing-and-validation)

## 1. Overview

ETSI TS 119 612 v2.4.1 defines the format and content for eIDAS trusted lists in electronic signature and trust infrastructures. This implementation guide provides specific requirements and examples for implementing this standard in the Wallet ecosystem.

### Trust List WeBuild Implementation Key Features
- XML-based trusted list format
- Comprehensive service type definitions
- Status management and history tracking
- Digital signature requirements
- HTTP transport and distribution mechanisms
- Multi-language support
- Cross-border trust mechanisms
- Integration with official Trusted List Manager (non-EU version) provided by European Commission for schema validation and trusted list management

## 2. Implementation Tasks

### Phase 1: Core Infrastructure

#### Task 1.1: XML Schema Integration
- [ ] Integrate official ETSI XSD schema [v2.4.1](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd)
- [ ] Validate TSL (Trusted List) tag structure against official schema
- [ ] Implement scheme information elements according to schema
- [ ] Configure TSP (Trust Service Provider) information validation
- [ ] Implement service information structure per schema
- [ ] Add service history tracking validation

#### Task 1.1.1: Trusted List Manager Integration
- [ ] Integrate official Trusted List Manager provided by European Commission
- [ ] Use Trusted List Manager non-EU version for LSP (Local Service Provider) implementation
- [ ] Leverage Trusted List Manager for schema validation against official ETSI schema
- [ ] Utilize Trusted List Manager for trusted list creation and management
- [  Implement validation workflows using Trusted List Manager

**Trusted List Manager Resources:**
- **Official Tool**: [Trusted List Manager](https://ec.europa.eu/digital-building-blocks/sites/display/TLSO/Trusted+List+Manager) - Provided by European Commission
- **Non-EU Version**: [Trusted List Manager non-EU](https://ec.europa.eu/digital-building-blocks/sites/display/TLSO/Trusted+List+Manager+non-EU) - Used for this implementation
- **Rationale for non-EU Version**: The EU version has constraints that make it unsuitable for LSP (Local Service Provider) implementations. The non-EU version provides the necessary flexibility while maintaining full schema validation compliance.

#### Task 1.2: Service Type Mapping
- [ ] Map Wallet entities to ETSI service types
- [ ] Define (qualified) trust service types for wallet providers
- [ ] Define (qualified) trust service types for relying parties
- [ ] Define (qualified) trust service types for credential issuers
- [ ] Add service type validation rules

#### Task 1.3: Status Management System
- [ ] Implement service status tracking
- [ ] Implement ETSI TS 119 612's status change history mechanism (ServiceHistory, ServiceHistoryInstance, ServicePreviousStatus, PreviousStatusStartingDate)
- [ ] Add status migration procedures
- [ ] Implement status validation rules

#### Task 1.4: ListOfTrustedLists Implementation
- [ ] Integrate SIE XSD schema for ListOfTrustedLists [v2.4.1](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd)
- [ ] Implement ListOfTrustedLists structure
- [ ] Create TrustedListPointer management
- [ ] Add cross-border trusted list support
- [ ] Implement centralized registry functionality

### Phase 2: Digital Signature and Security

#### Task 2.1: Digital Signature Implementation
- [ ] Implement digital signature algorithms
- [ ] Implement signature validation mechanisms
- [ ] Implement signature verification processes

#### Task 2.2: Authentication and Trust
- [ ] Implement trusted list authentication (out of band distribution of public key material for signature validation)
- [ ] Create trust chain validation example using an entity included in the Trusted List, for cross-border trust validation 
- [ ] Document trust anchor management best practice

### Phase 3: Distribution and Transport (Months 3-5)

#### Task 3.1: HTTP Transport Implementation
- [ ] Implement HTTP transport protocol
- [ ] Create MIME type registrations
- [ ] Add distribution point management
- [ ] Implement availability monitoring
- [ ] Create transport security mechanisms

#### Task 3.2: Publication and Notification
- [ ] Implement trusted list publication
- [ ] Create notification mechanisms
- [ ] Add update distribution
- [ ] Implement version control
- [ ] Create change tracking

## 3. Technical Requirements

### 3.1 Trusted List Format Requirements

#### 3.1.1 XML Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#"
                       xmlns:tsl="http://uri.etsi.org/19612/v2.4.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd">
  <!-- TSL content -->
</TrustServiceStatusList>
```

#### 3.1.2 Required Namespaces
- `http://uri.etsi.org/19612/v2.4.1#` - Main trusted list namespace
- `http://www.w3.org/2001/XMLSchema-instance` - XML Schema instance
- `http://www.w3.org/2000/09/xmldsig#` - XML Digital Signature

#### 3.1.3 Character Encoding
- **Required**: UTF-8 encoding
- **Validation**: Must validate against XML 1.0 specification

### 3.2 TSL Tag Requirements

#### 3.2.1 TSL Version Identifier
```xml
<TSLVersionIdentifier>2</TSLVersionIdentifier>
```

#### 3.2.2 TSL Sequence Number
```xml
<TSLSequenceNumber>1</TSLSequenceNumber>
```

#### 3.2.3 TSL Type
```xml
<TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
```

### 3.3 Scheme Information Requirements

#### 3.3.1 Scheme Operator Information
```xml
<SchemeOperatorName>
  <Name xml:lang="en">Wallet Trust Authority</Name>
  <Name xml:lang="it">Autorità di Fiducia Wallet</Name>
</SchemeOperatorName>
```

#### 3.3.2 Scheme Territory
```xml
<SchemeTerritory>IT</SchemeTerritory>
```

#### 3.3.3 Scheme Information URI
```xml
<SchemeInformationURI>https://trust-list.example.org/scheme-info</SchemeInformationURI>
```

### 3.4 Service Type Requirements

#### 3.4.1 Qualified Trust Service Types
- Electronic Signatures: `http://uri.etsi.org/TrstSvc/Svctype/CA/QC`
- Electronic Seals: `http://uri.etsi.org/TrstSvc/Svctype/CA/QC`
- Time Stamping: `http://uri.etsi.org/TrstSvc/Svctype/TSA/QTST`
- Electronic Registered Delivery: `http://uri.etsi.org/TrstSvc/Svctype/EDS/Q`

#### 3.4.2 Non-Qualified Trust Service Types
- Certificate Services: `http://uri.etsi.org/TrstSvc/Svctype/CA/PKC`
- Time Stamping: `http://uri.etsi.org/TrstSvc/Svctype/TSA`
- Electronic Registered Delivery: `http://uri.etsi.org/TrstSvc/Svctype/EDS`

#### 3.4.3 Wallet-Specific Service Types

The following service types are specific to the Wallet ecosystem and align with EWC Trust List structure and EUDI Architecture requirements:

##### 3.4.3.1 Wallet Provider Services
- Individual Wallet Provider: `http://uri.etsi.org/TrstSvc/Svctype/IndividualWalletProvider`
- Legal Person Wallet Provider: `http://uri.etsi.org/TrstSvc/Svctype/LegalPersonWalletProvider`
- Generic Wallet Provider (for backward compatibility): `http://uri.etsi.org/TrstSvc/Svctype/WalletProvider`

##### 3.4.3.2 Credential Issuer Services
- Person Identification Data (PID) Issuer: `http://uri.etsi.org/TrstSvc/Svctype/PID_Issuer`
- Legal Person Identification Data (LPID) Issuer: `http://uri.etsi.org/TrstSvc/Svctype/LPID_Issuer`
- Qualified Electronic Attestation of Attributes (QEAA) Provider: `http://uri.etsi.org/TrstSvc/Svctype/QEAA_Provider`
- Public Sector Electronic Attestation of Attributes (PUB EAA) Provider: `http://uri.etsi.org/TrstSvc/Svctype/PUB_EAA_Provider`
- Non-Qualified Electronic Attestation of Attributes (EAA) Provider: `http://uri.etsi.org/TrstSvc/Svctype/Non_Q_EAA_Provider`
- Generic Credential Issuer (for backward compatibility): `http://uri.etsi.org/TrstSvc/Svctype/CredentialIssuer`

##### 3.4.3.3 Relying Party Services
- Relying Party: `http://uri.etsi.org/TrstSvc/Svctype/RelyingParty`
- Relying Party Intermediary: `http://uri.etsi.org/TrstSvc/Svctype/RelyingPartyIntermediary`

##### 3.4.3.4 Access Certificate Authority Services

Per EUDI Architecture Annex 2, ISSU_33, there may be separate Access Certificate Authority Trusted Lists for different provider types:

- Access Certificate Authority for QEAA Providers: `http://uri.etsi.org/TrstSvc/Svctype/CA/PKC/QEAA`
- Access Certificate Authority for PUB EAA Providers: `http://uri.etsi.org/TrstSvc/Svctype/CA/PKC/PUB_EAA`
- Access Certificate Authority for EAA Providers: `http://uri.etsi.org/TrstSvc/Svctype/CA/PKC/EAA`
- Generic Access Certificate Authority: `http://uri.etsi.org/TrstSvc/Svctype/CA/PKC`

**References**:
- [EWC Trust List](https://ewc-consortium.github.io/ewc-trust-list/#trust-list)
- [EUDI Architecture Annex 2, ISSU_33](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2-high-level-requirements.md)

## 4. XML Schema Implementation

### 4.1 Official ETSI Schema Reference

The official ETSI TS 119 612 v2.4.1 XML Schema is available at:
**https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd**

### 4.2 Schema Integration

#### 4.2.1 Schema Location Declaration
```xml
xsi:schemaLocation="http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd"
```

#### 4.2.2 Local Schema Caching
For production environments, it's recommended to:
- Download and cache the schema locally
- Use a local schema location for validation
- Implement schema version management
- Monitor for schema updates

#### 4.2.3 Schema Validation
```bash
# Validate TSL against official ETSI schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd tsl.xml

# Or with local cached schema
xmllint --schema 19612_xsd.xsd tsl.xml
```

### 4.3 Key Schema Elements

The official schema includes all necessary elements for:
- **TrustServiceStatusList**: Root element with Id attribute
- **SchemeInformation**: Complete scheme metadata structure
- **TrustServiceProviderList**: TSP container with service information
- **ServiceInformation**: Individual service details and status
- **ServiceHistory**: Status change tracking
- **DigitalSignature**: XML signature support

### 4.4 SIE (Service Information Exchange) Schema

#### 4.4.1 SIE Schema Reference
The ETSI TS 119 612 v2.4.1 also includes a Service Information Exchange (SIE) schema for ListOfTrustedLists:
**https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd**

#### 4.4.2 SIE Schema Purpose
The SIE schema is used for:
- **ListOfTrustedLists**: Container for multiple trusted lists
- **Cross-border trusted list management**
- **Federation-level trusted list aggregation**
- **Service information exchange between authorities**

### 4.5 Clause D.5 - ListOfTrustedLists Implementation

#### 4.5.1 Overview
Clause D.5 of ETSI TS 119 612 v2.4.1 defines the ListOfTrustedLists structure, which is essential for:
- **Multi-jurisdiction trusted list management**
- **Cross-border trust establishment**
- **Federation-level service discovery**
- **Centralized trusted list distribution**

#### 4.5.2 ListOfTrustedLists Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ListOfTrustedLists xmlns="http://uri.etsi.org/19612/v2.4.1#"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd"
                   Id="list-of-trusted-lists-1">
  
  <ListInformation>
    <ListName>
      <Name xml:lang="en">WeBuild LSP Trusted Lists Registry</Name>
      <Name xml:lang="it">Registro delle Liste di Fiducia WeBuild LSP</Name>
      <Name xml:lang="sv">WeBuild LSP-förtroendelistor Register</Name>
    </ListName>
    <ListIdentifier>WEBUILD-TL-REGISTRY-001</ListIdentifier>
    <ListVersion>1</ListVersion>
    <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
    <ListOperatorName>
      <Name xml:lang="en">WeBuild LSP</Name>
      <Name xml:lang="it">WeBuild LSP</Name>
      <Name xml:lang="sv">WeBuild LSP</Name>
    </ListOperatorName>
    <ListOperatorAddress>
      <PostalAddresses>
        <PostalAddress>
          <StreetAddress>Via dei Fori Imperiali 1</StreetAddress>
          <Locality>Rome</Locality>
          <PostalCode>00184</PostalCode>
          <CountryName>IT</CountryName>
        </PostalAddress>
      </PostalAddresses>
      <ElectronicAddress>
        <URI>mailto:trust@webuildlsp.example.org</URI>
      </ElectronicAddress>
    </ListOperatorAddress>
    <DistributionPoints>
      <DistributionPoint>
        <URI>https://trust-list.example.org/lists/list-of-trusted-lists.xml</URI>
      </DistributionPoint>
    </DistributionPoints>
  </ListInformation>
  
  <TrustedLists>
    <TrustedListPointer>
      <TSLLocation>https://trust-list.example.org/tsl/tsl.xml</TSLLocation>
      <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
      <SchemeTerritory>IT</SchemeTerritory>
      <SchemeOperatorName>
        <Name xml:lang="en">Wallet Trust Authority</Name>
      </SchemeOperatorName>
      <SchemeName>
        <Name xml:lang="en">Wallet Trusted List</Name>
      </SchemeName>
      <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
      <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
      <SequenceNumber>1</SequenceNumber>
    </TrustedListPointer>
    
    <TrustedListPointer>
      <TSLLocation>https://trust.fr-wallet.gov.fr/tsl/tsl.xml</TSLLocation>
      <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
      <SchemeTerritory>FR</SchemeTerritory>
      <SchemeOperatorName>
        <Name xml:lang="en">FR-Wallet Trust Authority</Name>
      </SchemeOperatorName>
      <SchemeName>
        <Name xml:lang="en">FR-Wallet Trusted List</Name>
      </SchemeName>
      <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
      <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
      <SequenceNumber>2</SequenceNumber>
    </TrustedListPointer>
  </TrustedLists>
  
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <Reference URI="#list-of-trusted-lists-1">
        <Transforms>
          <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <DigestValue>...</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>...</SignatureValue>
    <KeyInfo>
      <X509Data>
        <X509Certificate>...</X509Certificate>
      </X509Data>
    </KeyInfo>
  </Signature>
</ListOfTrustedLists>
```

#### 4.5.3 ListOfTrustedLists Key Elements

##### 4.5.3.1 ListInformation
- **ListName**: Multi-language name of the list
- **ListIdentifier**: Unique identifier for the list
- **ListVersion**: Version number of the list
- **ListIssueDateTime**: When the list was issued
- **NextUpdate**: When the next update is scheduled
- **ListOperatorName**: Name of the list operator
- **ListOperatorAddress**: Contact information for the operator
- **DistributionPoints**: Where the list can be retrieved

##### 4.5.3.2 TrustedLists Container
- **TrustedListPointer**: Individual trusted list references
- **TSLLocation**: URL where the trusted list can be found
- **TSLType**: Type of trusted list (EUgeneric, etc.)
- **SchemeTerritory**: Country code of the scheme
- **SchemeOperatorName**: Name of the scheme operator
- **SchemeName**: Name of the scheme
- **ListIssueDateTime**: When the trusted list was issued
- **NextUpdate**: When the trusted list will be updated
- **SequenceNumber**: Order of the trusted list in the list

#### 4.5.4 Implementation Requirements

##### 4.5.4.1 ListOfTrustedLists Management
- **Centralized Registry**: Maintain a central registry of all trusted lists
- **Cross-Border Support**: Support trusted lists from multiple jurisdictions
- **Version Control**: Track versions and updates of individual trusted lists
- **Distribution Management**: Ensure reliable distribution of the list

##### 4.5.4.2 TrustedListPointer Management
- **URL Validation**: Ensure all TSL locations are accessible
- **Metadata Synchronization**: Keep metadata in sync with actual trusted lists
- **Update Monitoring**: Monitor for updates to individual trusted lists
- **Error Handling**: Handle cases where trusted lists are unavailable

##### 4.5.4.3 Security Requirements
- **Digital Signatures**: Sign the ListOfTrustedLists with appropriate certificates
- **Certificate Validation**: Validate certificates used for signing
- **Integrity Checking**: Ensure list integrity and authenticity
- **Access Control**: Control access to the list and its updates

#### 4.5.5 Wallet Integration

##### 4.5.5.1 Wallet Provider Integration
```xml
<TrustedListPointer>
  <TSLLocation>https://trust-list.example.org/wallet-providers/tsl.xml</TSLLocation>
  <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
  <SchemeTerritory>IT</SchemeTerritory>
  <SchemeOperatorName>
    <Name xml:lang="en">Wallet Authority</Name>
  </SchemeOperatorName>
  <SchemeName>
    <Name xml:lang="en">Wallet Provider Registry</Name>
  </SchemeName>
  <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
  <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
  <SequenceNumber>1</SequenceNumber>
</TrustedListPointer>
```

##### 4.5.5.2 Credential Issuer Integration
```xml
<TrustedListPointer>
  <TSLLocation>https://trust-list.example.org/credential-issuers/tsl.xml</TSLLocation>
  <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
  <SchemeTerritory>IT</SchemeTerritory>
  <SchemeOperatorName>
    <Name xml:lang="en">Wallet Authority</Name>
  </SchemeOperatorName>
  <SchemeName>
    <Name xml:lang="en">Wallet Credential Issuer Registry</Name>
  </SchemeName>
  <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
  <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
  <SequenceNumber>2</SequenceNumber>
</TrustedListPointer>
```

##### 4.5.5.3 Relying Party Integration
```xml
<TrustedListPointer>
  <TSLLocation>https://trust-list.example.org/relying-parties/tsl.xml</TSLLocation>
  <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
  <SchemeTerritory>IT</SchemeTerritory>
  <SchemeOperatorName>
    <Name xml:lang="en">Wallet Authority</Name>
  </SchemeOperatorName>
  <SchemeName>
    <Name xml:lang="en">Wallet Relying Party Registry</Name>
  </SchemeName>
  <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
  <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
  <SequenceNumber>3</SequenceNumber>
</TrustedListPointer>
```

#### 4.5.6 Validation and Testing

##### 4.5.6.1 SIE Schema Validation
```bash
# Validate ListOfTrustedLists against SIE schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd list-of-trusted-lists.xml

# Validate with detailed error reporting
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd --noout list-of-trusted-lists.xml 2>&1 | head -20
```

##### 4.5.6.2 Cross-Validation
- **TSL Validation**: Validate each referenced trusted list
- **URL Accessibility**: Ensure all TSL locations are accessible
- **Metadata Consistency**: Verify metadata matches actual trusted lists
- **Signature Validation**: Validate digital signatures

#### 4.5.7 Distribution and Access

##### 4.5.7.1 Distribution Points
```xml
<DistributionPoints>
  <DistributionPoint>
    <URI>https://trust-list.example.org/lists/list-of-trusted-lists.xml</URI>
  </DistributionPoint>
  <DistributionPoint>
    <URI>https://backup.Wallet.gov.it/lists/list-of-trusted-lists.xml</URI>
  </DistributionPoint>
</DistributionPoints>
```

##### 4.5.7.2 Access Control
- **Public Access**: ListOfTrustedLists should be publicly accessible
- **HTTPS Required**: All distribution points must use HTTPS
- **Caching Support**: Support appropriate caching headers
- **Load Balancing**: Distribute load across multiple distribution points

#### 4.5.8 Monitoring and Maintenance

##### 4.5.8.1 Update Monitoring
- **Scheduled Updates**: Monitor for scheduled updates
- **Change Detection**: Detect changes in individual trusted lists
- **Version Tracking**: Track versions of all trusted lists
- **Error Reporting**: Report errors in trusted list access

##### 4.5.8.2 Maintenance Procedures
- **Regular Updates**: Update ListOfTrustedLists regularly
- **Metadata Synchronization**: Keep metadata synchronized
- **Error Handling**: Handle errors gracefully
- **Audit Logging**: Log all changes and access

## 5. Service Type Mappings

### 5.1 Wallet Entity to ETSI Service Type Mapping

#### 5.1.1 Wallet Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/WalletProvider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Wallet Provider Services</Name>
  <Name xml:lang="it">Servizi di Provider di Portafoglio</Name>
</ServiceName>
```

#### 5.1.2 Credential Issuers

The following credential issuer types are defined based on eIDAS Implementing Act 848, Annex 1, paragraph 12:

##### 5.1.2.1 Person Identification Data (PID) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/PID_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Person Identification Data Provider</Name>
  <Name xml:lang="it">Provider di Dati di Identificazione Personale</Name>
</ServiceName>
```

##### 5.1.2.2 Qualified Electronic Attestation of Attributes (QEAA) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/QEAA_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Qualified Electronic Attestation of Attributes Provider</Name>
  <Name xml:lang="it">Provider di Attestazioni Elettroniche Qualificate di Attributi</Name>
</ServiceName>
```

##### 5.1.2.3 Electronic Attestation of Attributes (EAA) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/Non_Q_EAA_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Electronic Attestation of Attributes Provider</Name>
  <Name xml:lang="it">Provider di Attestazioni Elettroniche di Attributi</Name>
</ServiceName>
```

##### 5.1.2.4 Public Sector Electronic Attestation of Attributes (PUB EAA) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/PUB_EAA_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Public Sector Electronic Attestation of Attributes Provider</Name>
  <Name xml:lang="it">Provider di Attestazioni Elettroniche di Attributi del Settore Pubblico</Name>
</ServiceName>
```

##### 5.1.2.5 Qualified Certificate for Electronic Seal (QCert for ESeal) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/QCert_for_ESeal_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Qualified Certificate for Electronic Seal Provider</Name>
  <Name xml:lang="it">Provider di Certificati Qualificati per Sigilli Elettronici</Name>
</ServiceName>
```

##### 5.1.2.6 Qualified Certificate for Electronic Signature (QCert for ESig) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/QCert_for_ESig_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Qualified Certificate for Electronic Signature Provider</Name>
  <Name xml:lang="it">Provider di Certificati Qualificati per Firme Elettroniche</Name>
</ServiceName>
```

##### 5.1.2.7 Remote Qualified Electronic Signature Creation Device (rQSigCDs) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/rQSigCDs_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Remote Qualified Electronic Signature Creation Device Provider</Name>
  <Name xml:lang="it">Provider di Dispositivi di Creazione di Firma Elettronica Qualificata Remota</Name>
</ServiceName>
```

##### 5.1.2.8 Remote Qualified Electronic Seal Creation Device (rQSealCDs) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/rQSealCDs_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Remote Qualified Electronic Seal Creation Device Provider</Name>
  <Name xml:lang="it">Provider di Dispositivi di Creazione di Sigillo Elettronico Qualificato Remoto</Name>
</ServiceName>
```

##### 5.1.2.9 Electronic Signature and Seal Creation (ESig/ESeal Creation) Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/ESig_ESeal_Creation_Provider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Electronic Signature and Seal Creation Provider</Name>
  <Name xml:lang="it">Provider di Creazione di Firma e Sigillo Elettronico</Name>
</ServiceName>
```

**Reference**: eIDAS Implementing Act 848, Annex 1, paragraph 12

#### 5.1.3 Relying Parties
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/RelyingParty</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Relying Party Services</Name>
  <Name xml:lang="it">Servizi di Parte Rilasciante</Name>
</ServiceName>
```

#### 5.1.4 Access Certificate Authorities
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/CA/PKC</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Access Certificate Authority</Name>
  <Name xml:lang="it">Autorità di Certificazione per Accesso</Name>
</ServiceName>
```

### 5.2 Service Status Values

#### 5.2.1 Current Status Values
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted` - Service granted
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn` - Service withdrawn
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/suspended` - Service suspended
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel` - Recognized at national level
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel` - Deprecated at national level

#### 5.2.2 Status Change Tracking
```xml
<ServiceHistory>
  <ServiceHistoryInstance>
    <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/WalletProvider</ServiceTypeIdentifier>
    <ServiceName>
      <Name xml:lang="en">Wallet Provider Services</Name>
    </ServiceName>
    <ServiceDigitalIdentity>
      <X509SubjectName>CN=WalletProvider-IT, O=Wallet Authority, C=IT</X509SubjectName>
    </ServiceDigitalIdentity>
    <ServicePreviousStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServicePreviousStatus>
    <PreviousStatusStartingDate>2024-01-01T00:00:00Z</PreviousStatusStartingDate>
  </ServiceHistoryInstance>
</ServiceHistory>
```

## 6. Status Management

### 6.1 Status Change Procedures

#### 6.1.1 Service Granting
```xml
<ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServiceCurrentStatus>
<CurrentStatusStartingDate>2024-01-01T00:00:00Z</CurrentStatusStartingDate>
```

#### 6.1.2 Service Withdrawal
```xml
<ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn</ServiceCurrentStatus>
<CurrentStatusStartingDate>2024-06-01T00:00:00Z</CurrentStatusStartingDate>
```

#### 6.1.3 Service Suspension
```xml
<ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/suspended</ServiceCurrentStatus>
<CurrentStatusStartingDate>2024-03-01T00:00:00Z</CurrentStatusStartingDate>
```

### 6.2 Status Migration Procedures

#### 6.2.1 eIDAS Regulation Migration
- Services under supervision -> Withdrawn
- Services with supervision ceased -> Withdrawn
- Accredited services -> Withdrawn

#### 6.2.2 National Level Recognition
- Services under supervision -> Recognized at national level
- Services with supervision ceased -> Deprecated at national level

## 7. Digital Signature Implementation

### 7.1 Signature Algorithm Requirements

#### 7.1.1 Supported Algorithms
- RSA with SHA-256: `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`
- ECDSA with SHA-256: `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256`
- ECDSA with SHA-384: `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384`

#### 7.1.2 Signature Element Structure
```xml
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
  <SignedInfo>
    <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
    <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
    <Reference URI="#tsl">
      <Transforms>
        <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
      </Transforms>
      <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
      <DigestValue>...</DigestValue>
    </Reference>
  </SignedInfo>
  <SignatureValue>...</SignatureValue>
  <KeyInfo>
    <X509Data>
      <X509Certificate>...</X509Certificate>
    </X509Data>
  </KeyInfo>
</Signature>
```

### 7.2 Signature Validation

#### 7.2.1 Validation Process
1. Verify signature algorithm support
2. Validate certificate chain
3. Check signature value
4. Verify digest value
5. Validate canonicalization

#### 7.2.2 Certificate Requirements
- X.509 v3 certificates
- Valid certificate chain
- Appropriate key usage extensions
- Valid validity period

## 8. Distribution and Transport

### 8.1 HTTP Transport Implementation

#### 8.1.1 MIME Type Registration
```
Content-Type: application/vnd.etsi.tsl+xml
```

#### 8.1.2 HTTP Headers
```
HTTP/1.1 200 OK
Content-Type: application/vnd.etsi.tsl+xml
Content-Length: 12345
Last-Modified: Wed, 01 Jan 2024 00:00:00 GMT
ETag: "tsl-version-1"
Cache-Control: max-age=3600
```

#### 8.1.3 Distribution Points
```xml
<DistributionPoints>
  <DistributionPoint>
    <URI>https://trust-list.example.org/tsl/tsl.xml</URI>
  </DistributionPoint>
  <DistributionPoint>
    <URI>https://backup.Wallet.gov.it/tsl/tsl.xml</URI>
  </DistributionPoint>
</DistributionPoints>
```

### 8.2 Availability Requirements

#### 8.2.1 Uptime Requirements
- Minimum 99.9% availability
- 24/7 operation
- Redundant distribution points
- Load balancing support

#### 8.2.2 Update Frequency
- Daily updates for status changes
- Weekly full updates
- Emergency updates within 1 hour
- Notification of updates

## 9. Examples

> **Note**: The examples below are designed to be compliant with the official ETSI TS 119 612 v2.4.1 schema. However, some elements may need adjustment based on specific implementation requirements and the exact schema validation rules.

### 9.1 Complete TSL Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#"
                       xmlns:tsl="http://uri.etsi.org/19612/v2.4.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd"
                       Id="tsl-1">
  
  <SchemeInformation>
    <TSLVersionIdentifier>2</TSLVersionIdentifier>
    <TSLSequenceNumber>1</TSLSequenceNumber>
    <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
    
    <SchemeOperatorName>
      <Name xml:lang="en">Wallet Trust Authority</Name>
      <Name xml:lang="it">Autorità di Fiducia Wallet</Name>
    </SchemeOperatorName>
    
    <SchemeOperatorAddress>
      <PostalAddresses>
        <PostalAddress>
          <StreetAddress>Via Roma 123</StreetAddress>
          <Locality>Roma</Locality>
          <StateOrProvince>Lazio</StateOrProvince>
          <PostalCode>00100</PostalCode>
          <CountryName>IT</CountryName>
        </PostalAddress>
      </PostalAddresses>
      <ElectronicAddress>
        <URI>mailto:trust@Wallet.gov.it</URI>
      </ElectronicAddress>
    </SchemeOperatorAddress>
    
    <SchemeName>
      <Name xml:lang="en">Wallet Trusted List</Name>
      <Name xml:lang="it">Lista di Fiducia Wallet</Name>
    </SchemeName>
    
    <SchemeInformationURI>https://trust-list.example.org/scheme-info</SchemeInformationURI>
    <StatusDeterminationApproach>http://uri.etsi.org/TrstSvc/TrustedList/StatusDeterminationApproach/BySupervision</StatusDeterminationApproach>
    <SchemeTypeCommunityRules>http://uri.etsi.org/TrstSvc/TrustedList/SchemeTypeCommunityRules/EU</SchemeTypeCommunityRules>
    <SchemeTerritory>IT</SchemeTerritory>
    <TSLPolicyLegalNotice>https://trust-list.example.org/policy</TSLPolicyLegalNotice>
    <HistoricalInformationPeriod>P5Y</HistoricalInformationPeriod>
    <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
    
    <DistributionPoints>
      <DistributionPoint>
        <URI>https://trust-list.example.org/tsl/tsl.xml</URI>
      </DistributionPoint>
    </DistributionPoints>
  </SchemeInformation>
  
  <TrustServiceProviderList>
    <TrustServiceProvider>
      <TSPInformation>
        <TSPName>
          <Name xml:lang="en">Wallet Provider IT S.p.A.</Name>
          <Name xml:lang="it">Wallet Provider IT S.p.A.</Name>
        </TSPName>
        <TSPTradeName>
          <Name xml:lang="en">IT-Wallet</Name>
          <Name xml:lang="it">IT-Wallet</Name>
        </TSPTradeName>
        <TSPAddress>
          <PostalAddresses>
            <PostalAddress>
              <StreetAddress>Via Milano 456</StreetAddress>
              <Locality>Milano</Locality>
              <StateOrProvince>Lombardia</StateOrProvince>
              <PostalCode>20100</PostalCode>
              <CountryName>IT</CountryName>
            </PostalAddress>
          </PostalAddresses>
          <ElectronicAddress>
            <URI>mailto:info@wallet.example.it</URI>
          </ElectronicAddress>
        </TSPAddress>
        <TSPInformationURI>https://wallet.example.it/info</TSPInformationURI>
        <TSPServices>
          <ServiceInformation>
            <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/CA/PKC</ServiceTypeIdentifier>
            <ServiceName>
              <Name xml:lang="en">Wallet Provider Services</Name>
              <Name xml:lang="it">Servizi di Provider di Portafoglio</Name>
            </ServiceName>
            <ServiceDigitalIdentity>
              <X509SubjectName>CN=WalletProvider-IT, O=Wallet Provider IT S.p.A., C=IT</X509SubjectName>
              <X509SKI>...</X509SKI>
              <X509Certificate>...</X509Certificate>
            </ServiceDigitalIdentity>
            <ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServiceCurrentStatus>
            <CurrentStatusStartingDate>2024-01-01T00:00:00Z</CurrentStatusStartingDate>
            <SchemeServiceDefinitionURI>https://trust-list.example.org/scheme/wallet-provider</SchemeServiceDefinitionURI>
            <ServiceSupplyPoints>
              <ServiceSupplyPoint>
                <URI>https://wallet.example.it/api</URI>
              </ServiceSupplyPoint>
            </ServiceSupplyPoints>
            <TSPServiceDefinitionURI>https://wallet.example.it/service-definition</TSPServiceDefinitionURI>
          </ServiceInformation>
        </TSPServices>
      </TSPInformation>
    </TrustServiceProvider>
  </TrustServiceProviderList>
  
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <Reference URI="#tsl-1">
        <Transforms>
          <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <DigestValue>...</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>...</SignatureValue>
    <KeyInfo>
      <X509Data>
        <X509Certificate>...</X509Certificate>
      </X509Data>
    </KeyInfo>
  </Signature>
</TrustServiceStatusList>
```

### 9.2 Service Status Change Example

```xml
<ServiceHistory>
  <ServiceHistoryInstance>
    <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/WalletProvider</ServiceTypeIdentifier>
    <ServiceName>
      <Name xml:lang="en">Wallet Provider Services</Name>
    </ServiceName>
    <ServiceDigitalIdentity>
      <X509SubjectName>CN=WalletProvider-IT, O=Wallet Provider IT S.p.A., C=IT</X509SubjectName>
    </ServiceDigitalIdentity>
    <ServicePreviousStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServicePreviousStatus>
    <PreviousStatusStartingDate>2024-01-01T00:00:00Z</PreviousStatusStartingDate>
  </ServiceHistoryInstance>
</ServiceHistory>
```

### 9.3 Service Extension Example

```xml
<ServiceInformationExtensions>
  <Qualifications>
    <QualificationElement>
      <CriteriaList>
        <Criteria>
          <Qualifier>http://uri.etsi.org/TrstSvc/TrustedList/Qualifier/QCForESig</Qualifier>
        </Criteria>
        <Criteria>
          <Qualifier>http://uri.etsi.org/TrstSvc/TrustedList/Qualifier/QCForESeal</Qualifier>
        </Criteria>
      </CriteriaList>
    </QualificationElement>
  </Qualifications>
  <AdditionalServiceInformation>
    <URI>https://trust-list.example.org/additional-info/wallet-provider</URI>
  </AdditionalServiceInformation>
</ServiceInformationExtensions>
```

### 9.4 Schema-Compliant Example

Here's a corrected example that should validate against the official ETSI schema:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd"
                       Id="tsl-1">
  
  <SchemeInformation>
    <TSLVersionIdentifier>2</TSLVersionIdentifier>
    <TSLSequenceNumber>1</TSLSequenceNumber>
    <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
    
    <SchemeOperatorName>
      <Name xml:lang="en">Wallet Trust Authority</Name>
    </SchemeOperatorName>
    
    <SchemeOperatorAddress>
      <PostalAddresses>
        <PostalAddress>
          <StreetAddress>Via Roma 123</StreetAddress>
          <Locality>Roma</Locality>
          <StateOrProvince>Lazio</StateOrProvince>
          <PostalCode>00100</PostalCode>
          <CountryName>IT</CountryName>
        </PostalAddress>
      </PostalAddresses>
      <ElectronicAddress>
        <URI>mailto:trust@Wallet.gov.it</URI>
      </ElectronicAddress>
    </SchemeOperatorAddress>
    
    <SchemeName>
      <Name xml:lang="en">Wallet Trusted List</Name>
    </SchemeName>
    
    <SchemeInformationURI>https://trust-list.example.org/scheme-info</SchemeInformationURI>
    <StatusDeterminationApproach>http://uri.etsi.org/TrstSvc/TrustedList/StatusDeterminationApproach/BySupervision</StatusDeterminationApproach>
    <SchemeTypeCommunityRules>http://uri.etsi.org/TrstSvc/TrustedList/SchemeTypeCommunityRules/EU</SchemeTypeCommunityRules>
    <SchemeTerritory>IT</SchemeTerritory>
    <TSLPolicyLegalNotice>https://trust-list.example.org/policy</TSLPolicyLegalNotice>
    <HistoricalInformationPeriod>P5Y</HistoricalInformationPeriod>
    <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
    
    <DistributionPoints>
      <DistributionPoint>
        <URI>https://trust-list.example.org/tsl/tsl.xml</URI>
      </DistributionPoint>
    </DistributionPoints>
  </SchemeInformation>
  
  <TrustServiceProviderList>
    <TrustServiceProvider>
      <TSPInformation>
        <TSPName>
          <Name xml:lang="en">Wallet Provider IT S.p.A.</Name>
        </TSPName>
        <TSPAddress>
          <PostalAddresses>
            <PostalAddress>
              <StreetAddress>Via Milano 456</StreetAddress>
              <Locality>Milano</Locality>
              <StateOrProvince>Lombardia</StateOrProvince>
              <PostalCode>20100</PostalCode>
              <CountryName>IT</CountryName>
            </PostalAddress>
          </PostalAddresses>
          <ElectronicAddress>
            <URI>mailto:info@wallet.example.it</URI>
          </ElectronicAddress>
        </TSPAddress>
        <TSPInformationURI>https://wallet.example.it/info</TSPInformationURI>
        <TSPServices>
          <ServiceInformation>
            <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/CA/PKC</ServiceTypeIdentifier>
            <ServiceName>
              <Name xml:lang="en">Certificate Authority Services</Name>
            </ServiceName>
            <ServiceDigitalIdentity>
              <X509SubjectName>CN=WalletProvider-IT, O=Wallet Provider IT S.p.A., C=IT</X509SubjectName>
              <X509SKI>...</X509SKI>
              <X509Certificate>...</X509Certificate>
            </ServiceDigitalIdentity>
            <ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServiceCurrentStatus>
            <CurrentStatusStartingDate>2024-01-01T00:00:00Z</CurrentStatusStartingDate>
            <SchemeServiceDefinitionURI>https://trust-list.example.org/scheme/ca-services</SchemeServiceDefinitionURI>
            <ServiceSupplyPoints>
              <ServiceSupplyPoint>
                <URI>https://wallet.example.it/api</URI>
              </ServiceSupplyPoint>
            </ServiceSupplyPoints>
            <TSPServiceDefinitionURI>https://wallet.example.it/service-definition</TSPServiceDefinitionURI>
          </ServiceInformation>
        </TSPServices>
      </TSPInformation>
    </TrustServiceProvider>
  </TrustServiceProviderList>
  
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <Reference URI="#tsl-1">
        <Transforms>
          <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <DigestValue>...</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>...</SignatureValue>
    <KeyInfo>
      <X509Data>
        <X509Certificate>...</X509Certificate>
      </X509Data>
    </KeyInfo>
  </Signature>
</TrustServiceStatusList>
```

#### 9.4.1 Potential Validation Issues
The examples provided may require adjustments for full schema compliance:

1. **Service Type Identifiers**: The custom Wallet service types (e.g., `http://uri.etsi.org/TrstSvc/Svctype/WalletProvider`) may not be defined in the official schema. Consider using standard ETSI service types or extending the schema.

2. **Element Ordering**: The official schema may require specific element ordering that differs from the examples.

3. **Required Elements**: Some elements marked as optional in the examples may be required by the schema.

4. **Namespace Declarations**: Ensure all namespace declarations match the schema requirements.

#### 9.4.2 Validation Commands
```bash
# Validate the complete TSL example
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd tsl-example.xml

# Validate with detailed error reporting
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd --noout tsl-example.xml 2>&1 | head -20
```

#### 9.4.3 Schema Compliance Checklist
- [ ] All required elements are present
- [ ] Element ordering matches schema requirements
- [ ] Namespace declarations are correct
- [ ] Service type identifiers are valid
- [ ] Date formats comply with schema constraints
- [ ] URI formats are valid
- [ ] Language codes are properly formatted

## 10. Testing and Validation

### 10.1 Schema Validation

#### 10.1.1 XSD Validation
```bash
# Validate TSL against official ETSI schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd tsl.xml

# Or with local cached schema
xmllint --schema 19612_xsd.xsd tsl.xml
```

#### 10.1.2 Content Validation
- Service type identifier validation
- Status value validation
- Date format validation
- URI format validation
- Language code validation

### 10.2 Signature Validation

#### 10.2.1 Digital Signature Verification
```bash
# Verify XML signature
xmlsec1 --verify --pubkey-cert-pem cert.pem tsl.xml
```

#### 10.2.2 Certificate Chain Validation
- Root CA validation
- Intermediate CA validation
- End entity certificate validation
- Revocation status checking

### 10.3 Functional Testing

#### 10.3.1 Status Change Testing
- Test status transitions
- Validate status history
- Test notification mechanisms
- Verify update procedures

#### 10.3.2 Distribution Testing
- HTTP transport testing
- MIME type validation
- Availability testing
- Load testing

## Migration Strategy

### 1. Phase 1: Schema Integration (Month 1)
- Integrate official ETSI XSD schema
- Create basic TSL structure
- Add service type mappings
- Implement schema validation

### 2. Phase 2: Service Management (Month 2)
- Implement service registration
- Add status management
- Create service history tracking
- Implement notification system

### 3. Phase 3: Digital Signatures (Month 3)
- Implement signature generation
- Add signature validation
- Create certificate management
- Implement trust chain validation

### 4. Phase 4: Distribution (Month 4)
- Implement HTTP transport
- Add MIME type support
- Create distribution points
- Implement availability monitoring

### 5. Phase 5: Integration (Month 5)
- Integrate with existing systems
- Add cross-border support
- Implement monitoring and logging
- Create management interfaces

### 6. Phase 6: Testing and Deployment (Month 6)
- Comprehensive testing
- Performance optimization
- Security audit
- Production deployment

## Compliance Checklist

### 1. Technical Compliance
- [ ] Official ETSI XSD schema integration
- [ ] Service type mapping
- [ ] Status management
- [ ] Digital signature implementation
- [ ] HTTP transport support
- [ ] MIME type registration

### 2. Functional Compliance
- [ ] Service registration
- [ ] Status tracking
- [ ] History management
- [ ] Notification system
- [ ] Distribution mechanism
- [ ] Availability monitoring

### 3. Security Compliance
- [ ] Digital signature validation
- [ ] Certificate chain validation
- [ ] Trust anchor management
- [ ] Revocation checking
- [ ] Access control
- [ ] Audit logging

### 4. Operational Compliance
- [ ] 24/7 availability
- [ ] Update procedures
- [ ] Backup mechanisms
- [ ] Disaster recovery
- [ ] Monitoring and alerting
- [ ] Documentation

## References

### Standards and Specifications
- [ETSI TS 119 612 v2.4.1 (2024-11)](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.03.01_60/ts_119612v020301p.pdf)
- [ETSI TS 119 612 v2.4.1 XSD Schema](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd)
- [ETSI TS 119 612 v2.4.1 SIE XSD Schema](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd)
- [eIDAS Regulation (EU) No 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [XML Digital Signature Specification](https://www.w3.org/TR/xmldsig-core1/)
- [XML Schema Part 1: Structures](https://www.w3.org/TR/xmlschema-1/)
- [XML Schema Part 2: Datatypes](https://www.w3.org/TR/xmlschema-2/)

### Official Tools and Resources
- [Trusted List Manager](https://ec.europa.eu/digital-building-blocks/sites/display/TLSO/Trusted+List+Manager) - Official tool provided by European Commission for trusted list creation and management
- [Trusted List Manager non-EU](https://ec.europa.eu/digital-building-blocks/sites/display/TLSO/Trusted+List+Manager+non-EU) - Non-EU version used for LSP implementations (recommended for this project)

## Contact Information

For questions about this implementation guide:
- open an issue
- reach the WeBuild WG groups
---

**Document Version**: 0.9  
**Last Updated**: 2025-11-16  
