# ETSI Trusted Lists Implementation Profile
## Unified Guide for TS 119 612 (XML) and TS 119 602 (JSON/XML)

## Document Information
- **Standards**: 
  - [ETSI TS 119 612 V2.4.1 (2025-11)](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) - Trusted Lists (XML)
  - [ETSI TS 119 602 V1.1.1 (2025-11)](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf) - Lists of trusted entities; Data model (JSON/XML)
  - [ETSI TS 119 615 V1.3.1 (2026-01)](https://www.etsi.org/deliver/etsi_ts/119600_119699/119615/01.03.01_60/ts_119615v010301p.pdf) - Procedures for using and interpreting EUMS national trusted lists
- **Keywords**: e-commerce, electronic signature, eudi wallet, security, trust services

## Table of Contents
1. [Overview](#1-overview)
2. [Standards Relationship](#2-standards-relationship)
3. [URI and Endpoint Reference](#3-uri-and-endpoint-reference)
4. [Implementation Tasks](#4-implementation-tasks)
5. [XML Implementation (TS 119 612)](#5-xml-implementation-ts-119-612)
6. [JSON Implementation (TS 119 602)](#6-json-implementation-ts-119-602)
7. [Profile-Specific Requirements](#7-profile-specific-requirements)
8. [Digital Signature Implementation](#8-digital-signature-implementation)
9. [Distribution and Transport](#9-distribution-and-transport)
10. [Examples](#10-examples)
11. [Testing and Validation](#11-testing-and-validation)
12. [Python Libraries for Signatures](../tools/python_signature_libraries.md) (in `tools/`)

## 1. Overview

This implementation profile provides unified guidance for implementing both ETSI TS 119 612 (Trusted Lists - XML) and ETSI TS 119 602 (Lists of Trusted Entities - JSON/XML) in the Wallet ecosystem.

### 1.1 Standards Overview

**ETSI TS 119 612 v2.4.1** defines:
- XML-based Trusted Service Lists (TSL)
- Format for eIDAS trusted lists
- Service type definitions and status management
- XAdES digital signatures

**ETSI TS 119 602 v1.1.1 (2025-11)** (per ARF v2.8.0 STS list) (“Lists of trusted entities; Data model”) defines:
- Abstract data model for Lists of Trusted Entities (LoTE)
- JSON and XML bindings
- Profile-based approach for different entity types
- JAdES (JSON) and XAdES (XML) digital signatures

**ETSI TS 119 615 v1.3.1** defines:
- Procedures for **using and interpreting** EUMS national trusted lists when **validating** EU qualified trust service outputs (e.g. qualified certificates, time stamps, validation reports)
- Interoperable algorithms for authenticating the EC-compiled List of Trusted Lists (LoTL) and EUMS national trusted lists
- Implements the rules of Commission Implementing Decision (EU) 2015/1505; builds on ETSI TS 119 612

**Distinction**: TS 119 612 and TS 119 602 define **structure and format** of trusted lists (production side). TS 119 615 defines **procedures for authentication and interpretation** (consumption/validation side).

### 1.2 When to Use Which Standard

| Use Case | Standard | Format |
|----------|----------|--------|
| Traditional eIDAS Trusted Lists | TS 119 612 | XML only |
| EU Wallet Provider Lists | TS 119 602 | JSON (preferred) or XML |
| EU PID Provider Lists | TS 119 602 | JSON (preferred) or XML |
| EU Pub-EAA Provider Lists | TS 119 602 | JSON or XML |
| Custom Trust Lists | TS 119 602 | JSON or XML |
| Cross-border TSL aggregation | TS 119 612 | XML (ListOfTrustedLists) |

## 2. Standards Relationship

### 2.1 Data Model Mapping

TS 119 602 is a generalization of TS 119 612. The components map as follows:

| TS 119 602 (LoTE) | TS 119 612 (TSL) |
|-------------------|------------------|
| LoTE | TSL |
| Trusted Entity (TE) | Trust Service Provider (TSP) |
| Trusted Entity Service | Trust Service |
| LoTE Version Identifier | TSL Version Identifier |
| LoTE Sequence Number | TSL Sequence Number |
| LoTE Type | TSL Type |
| Scheme Operator | Scheme Operator |
| Service Digital Identity | Service Digital Identity |

### 2.2 XML Binding Options

For TS 119 602 XML binding, you can:
1. **Use TS 119 612 schema directly** (recommended for compatibility)
2. **Use TS 119 602 explicit scheme XML schema** (from ETSI repository)

## 3. URI and Endpoint Reference

### 3.1 Schema and Repository URIs

#### 3.1.1 XML Schema Endpoints (TS 119 612)
```
# Main TSL Schema
https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd

# ListOfTrustedLists (SIE) Schema
https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd
```

#### 3.1.2 JSON Schema Endpoints (TS 119 602)
```
# LoTE JSON Schema Repository
https://forge.etsi.org/rep/esi/x19_60201_lists_of_trusted_entities
```

#### 3.1.3 XML Schema Endpoints (TS 119 602)
```
# LoTE XML Schema (if using explicit scheme)
https://forge.etsi.org/rep/esi/x19_60201_lists_of_trusted_entities
```

### 3.2 LoTE Type URIs (TS 119 602)

These identify the type of list:

```
# PID Providers List
http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList

# Wallet Providers List
http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList

# WRPAC Providers List
http://uri.etsi.org/19602/LoTEType/EUWRPACProvidersList

# WRPRC Providers List
http://uri.etsi.org/19602/LoTEType/EUWRPRCProvidersList

# Pub-EAA Providers List
http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList

# Registrars and Registers List
http://uri.etsi.org/19602/LoTEType/EURegistrarsAndRegistersList
```

### 3.3 TSL Type URIs (TS 119 612)

```
# Generic EU Trusted List
http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric
```

### 3.4 Service Type Identifier URIs

#### 3.4.1 TS 119 602 Service Types

```
# PID Services
http://uri.etsi.org/19602/SvcType/PID/Issuance
http://uri.etsi.org/19602/SvcType/PID/Revocation

# Wallet Services
http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance
http://uri.etsi.org/19602/SvcType/WalletSolution/Revocation

# Pub-EAA Services
http://uri.etsi.org/19602/SvcType/PubEAA/Issuance
http://uri.etsi.org/19602/SvcType/PubEAA/Revocation

# WRPAC Services
http://uri.etsi.org/19602/SvcType/WRPAC/Issuance
http://uri.etsi.org/19602/SvcType/WRPAC/Revocation

# WRPRC Services
http://uri.etsi.org/19602/SvcType/WRPRC/Issuance
http://uri.etsi.org/19602/SvcType/WRPRC/Revocation

# Register Service
http://uri.etsi.org/19602/SvcType/Register
```

#### 3.4.2 TS 119 612 Service Types

```
# Qualified Certificate Services
http://uri.etsi.org/TrstSvc/Svctype/CA/QC

# Public Key Certificate Services
http://uri.etsi.org/TrstSvc/Svctype/CA/PKC

# Qualified Time Stamping
http://uri.etsi.org/TrstSvc/Svctype/TSA/QTST

# Time Stamping
http://uri.etsi.org/TrstSvc/Svctype/TSA

# Wallet Provider (custom)
http://uri.etsi.org/TrstSvc/Svctype/WalletProvider
http://uri.etsi.org/TrstSvc/Svctype/IndividualWalletProvider
http://uri.etsi.org/TrstSvc/Svctype/LegalPersonWalletProvider

# Credential Issuers (custom)
http://uri.etsi.org/TrstSvc/Svctype/PID_Issuer
http://uri.etsi.org/TrstSvc/Svctype/QEAA_Provider
http://uri.etsi.org/TrstSvc/Svctype/PUB_EAA_Provider
http://uri.etsi.org/TrstSvc/Svctype/Non_Q_EAA_Provider
```

### 3.5 Status Determination Approach URIs

**TS 119 612 (EU Member State trusted lists):** the value shall be `http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate` (clause 5.3.8, annex D.5.2).

**TS 119 602 (LoTE profiles):**

```
# PID Providers
http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU

# Wallet Providers
http://uri.etsi.org/19602/WalletProvidersList/StatusDetn/EU

# WRPAC Providers
http://uri.etsi.org/19602/WRPACProvidersList/StatusDetn/EU

# WRPRC Providers
http://uri.etsi.org/19602/WRPRCProvidersList/StatusDetn/EU

# Pub-EAA Providers
http://uri.etsi.org/19602/PubEAAProvidersList/StatusDetn/EU

# Registrars and Registers
http://uri.etsi.org/19602/RegistrarsAndRegistersList/StatusDetn/EU
```

### 3.6 Scheme Type/Community/Rules URIs

```
# PID Providers
http://uri.etsi.org/19602/PIDProviders/schemerules/EU

# Wallet Providers
http://uri.etsi.org/19602/WalletProvidersList/schemerules/EU

# WRPAC Providers
http://uri.etsi.org/19602/WRPACProvidersList/schemerules/EU

# WRPRC Providers
http://uri.etsi.org/19602/WRPRCProvidersList/schemerules/EU

# Pub-EAA Providers
http://uri.etsi.org/19602/PubEAAProvidersList/schemerules/EU

# Registrars and Registers
http://uri.etsi.org/19602/RegistrarsAndRegistersList/schemerules/EU
```

### 3.7 Service Status URIs

#### 3.7.1 TS 119 612 Status Values
```
http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted
http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn
http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/suspended
http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel
http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel
```

#### 3.7.2 TS 119 602 Pub-EAA Status Values
```
http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/notified
http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/withdrawn
```

### 3.8 Distribution Point URIs

These are HTTP/HTTPS endpoints where lists are published:

```
# Example TSL Distribution Point
https://trust-list.example.org/tsl/tsl.xml

# Example LoTE Distribution Point (JSON)
https://trust-list.example.org/lote/pid-providers.json

# Example LoTE Distribution Point (XML)
https://trust-list.example.org/lote/pid-providers.xml

# ListOfTrustedLists Distribution Point
https://trust-list.example.org/lists/list-of-trusted-lists.xml
```

### 3.9 Information URI Patterns

#### 3.9.1 Scheme Information URIs
These point to documentation about the scheme:
```
https://ec.europa.eu/pid-providers-list
https://ec.europa.eu/wallet-providers-list
```

#### 3.9.2 TE Information URIs
These point to information about trusted entities:
```
# PID Provider Information
http://uri.etsi.org/19602/ListOfTrustedEntities/PIDProvider/CC
# Where CC is ISO 3166-1 Alpha 2 country code

# Wallet Provider Information
http://uri.etsi.org/19602/ListOfTrustedEntities/WalletProvider/CC

# WRPAC Provider Information
http://uri.etsi.org/19602/ListOfTrustedEntities/WRPACProvider/CC

# WRPRC Provider Information
http://uri.etsi.org/19602/ListOfTrustedEntities/WRPRCProvider/CC

# Pub-EAA Provider Information
http://uri.etsi.org/19602/ListOfTrustedEntities/PubEAAProvider/CC

# Registrar Information
http://uri.etsi.org/19602/ListOfTrustedEntities/Registrar/CC
```

### 3.10 LoTE Tag URI

```
http://uri.etsi.org/19602/LoTETag
```

## 4. Implementation Tasks

### Phase 1: Core Infrastructure

#### Task 1.1: Choose Implementation Approach
- [ ] Decide: TS 119 612 (XML only) or TS 119 602 (JSON/XML)
- [ ] For TS 119 602: Choose JSON or XML binding
- [ ] For TS 119 602 XML: Use TS 119 612 schema or explicit schema

#### Task 1.2: Schema Integration

**For XML (TS 119 612 or TS 119 602):**
- [ ] Download/cache XSD schema from ETSI repository
- [ ] Integrate schema validation
- [ ] Implement XML serialization/deserialization
- [ ] Handle multilingual strings

**For JSON (TS 119 602):**
- [ ] Download/cache JSON schema from ETSI repository
- [ ] Integrate JSON schema validation
- [ ] Implement JSON serialization/deserialization
- [ ] Handle multilingual strings

#### Task 1.3: Data Model Implementation
- [ ] Implement scheme information structure
- [ ] Implement trusted entities/providers list structure
- [ ] Implement service information structure
- [ ] Implement service history tracking
- [ ] Add multilingual support

#### Task 1.4: Trusted List Manager Integration (TS 119 612)
- [ ] Integrate Trusted List Manager non-EU version
- [ ] Use for schema validation
- [ ] Use for trusted list creation and management

**Resources:**
- [Trusted List Manager non-EU](https://ec.europa.eu/digital-building-blocks/sites/display/TLSO/Trusted+List+Manager+non-EU)

### Phase 2: Profile Implementation

#### Task 2.1: PID Providers Profile (TS 119 602)
- [ ] Implement PID provider list structure
- [ ] Use correct LoTE type URI
- [ ] Use correct service type URIs
- [ ] Implement validation rules

#### Task 2.2: Wallet Providers Profile (TS 119 602)
- [ ] Implement wallet provider list structure
- [ ] Add service unique identifier extension
- [ ] Implement validation rules

#### Task 2.3: Other Profiles
- [ ] WRPAC providers profile
- [ ] WRPRC providers profile
- [ ] Pub-EAA providers profile
- [ ] Registrars and Registers profile

### Phase 3: Digital Signatures

#### Task 3.1: JAdES Signature (JSON - TS 119 602)
- [ ] Implement Compact JAdES Baseline B signature generation
- [ ] Implement JAdES signature validation
- [ ] Handle certificate chain attachment

#### Task 3.2: XAdES Signature (XML - TS 119 612/602)
- [ ] Implement XAdES Baseline B signature generation
- [ ] Implement XAdES signature validation
- [ ] Handle enveloped signature format

### Phase 4: Distribution and Management

#### Task 4.1: Publication
- [ ] Implement distribution points
- [ ] Add HTTP/HTTPS transport support
- [ ] Implement update mechanisms
- [ ] Add version control
- [ ] Set appropriate MIME types

#### Task 4.2: Consumption
- [ ] Implement list fetching
- [ ] Add signature verification
- [ ] Implement entity lookup
- [ ] Add caching mechanisms

## 5. XML Implementation (TS 119 612)

### 5.1 XML Schema Integration

#### 5.1.1 Schema Location
```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd"
                       Id="tsl-1">
  <!-- TSL content -->
</TrustServiceStatusList>
```

#### 5.1.2 Required Namespaces
- `http://uri.etsi.org/19612/v2.4.1#` - Main TSL namespace
- `http://www.w3.org/2001/XMLSchema-instance` - XML Schema instance
- `http://www.w3.org/2000/09/xmldsig#` - XML Digital Signature

### 5.2 Basic XML Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.4.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.4.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd"
                       Id="tsl-1">
  
  <SchemeInformation>
    <!-- TS 119 612 clause 5.3.1: value shall be "6" -->
    <TSLVersionIdentifier>6</TSLVersionIdentifier>
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
          <PostalCode>00100</PostalCode>
          <CountryName>IT</CountryName>
        </PostalAddress>
      </PostalAddresses>
      <ElectronicAddress>
        <URI>mailto:trust@wallet.gov.it</URI>
        <URI>https://wallet.gov.it</URI>
      </ElectronicAddress>
    </SchemeOperatorAddress>
    <SchemeName>
      <Name xml:lang="en">Wallet Trusted List</Name>
    </SchemeName>
    <SchemeInformationURI>https://trust-list.example.org/scheme-info</SchemeInformationURI>
    <StatusDeterminationApproach>http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate</StatusDeterminationApproach>
    <SchemeTypeCommunityRules>http://uri.etsi.org/TrstSvc/TrustedList/SchemeTypeCommunityRules/EU</SchemeTypeCommunityRules>
    <SchemeTerritory>IT</SchemeTerritory>
    <ListIssueDateTime>2025-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2025-07-01T00:00:00Z</NextUpdate>
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
            </ServiceName>
            <ServiceDigitalIdentity>
              <X509SubjectName>CN=WalletProvider-IT, O=Wallet Provider IT S.p.A., C=IT</X509SubjectName>
              <X509SKI>...</X509SKI>
              <X509Certificate>...</X509Certificate>
            </ServiceDigitalIdentity>
            <ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServiceCurrentStatus>
            <CurrentStatusStartingDate>2025-01-01T00:00:00Z</CurrentStatusStartingDate>
            <ServiceSupplyPoints>
              <ServiceSupplyPoint>
                <URI>https://wallet.example.it/api</URI>
              </ServiceSupplyPoint>
            </ServiceSupplyPoints>
          </ServiceInformation>
        </TSPServices>
      </TSPInformation>
    </TrustServiceProvider>
  </TrustServiceProviderList>
  
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <!-- XAdES signature -->
  </Signature>
</TrustServiceStatusList>
```

### 5.3 Schema Validation

```bash
# Validate TSL against official ETSI schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd tsl.xml

# Or with local cached schema
xmllint --schema 19612_xsd.xsd tsl.xml
```

## 6. JSON Implementation (TS 119 602)

### 6.1 JSON Schema Location

The JSON schema is available at:
**https://forge.etsi.org/rep/esi/x19_60201_lists_of_trusted_entities**

### 6.2 Basic JSON Structure

```json
{
  "loteTag": "http://uri.etsi.org/19602/LoTETag",
  "schemeInformation": {
    "loteVersionIdentifier": 1,
    "loteSequenceNumber": 1,
    "loteType": "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList",
    "schemeOperatorName": [
      {
        "lang": "en",
        "value": "European Commission"
      }
    ],
    "schemeOperatorAddress": {
      "postalAddresses": [
        {
          "lang": "en",
          "streetAddress": "Rue de la Loi 200",
          "locality": "Brussels",
          "postalCode": "1049",
          "country": "BE"
        }
      ],
      "electronicAddress": [
        {
          "lang": "en",
          "uri": "mailto:trust@ec.europa.eu"
        },
        {
          "lang": "en",
          "uri": "https://ec.europa.eu"
        }
      ]
    },
    "schemeName": [
      {
        "lang": "en",
        "value": "EU:PID Providers List"
      }
    ],
    "schemeInformationURI": [
      {
        "lang": "en",
        "uri": "https://ec.europa.eu/pid-providers-list"
      }
    ],
    "statusDeterminationApproach": "http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU",
    "schemeTypeCommunityRules": [
      {
        "lang": "en",
        "uri": "http://uri.etsi.org/19602/PIDProviders/schemerules/EU"
      }
    ],
    "schemeTerritory": "EU",
    "listIssueDateTime": "2025-01-01T00:00:00Z",
    "nextUpdate": "2025-07-01T00:00:00Z"
  },
  "trustedEntitiesList": {
    "trustedEntity": [
      {
        "trustedEntityInformation": {
          "teName": [
            {
              "lang": "en",
              "value": "PID Provider Example Ltd."
            }
          ],
          "teTradeName": [
            {
              "lang": "en",
              "value": "PID-12345678"
            }
          ],
          "teAddress": {
            "tePostalAddress": [
              {
                "lang": "en",
                "streetAddress": "Example Street 1",
                "locality": "Example City",
                "postalCode": "12345",
                "country": "IT"
              }
            ],
            "teElectronicAddress": [
              {
                "lang": "en",
                "uri": "mailto:info@pid-provider.example"
              },
              {
                "lang": "en",
                "uri": "https://pid-provider.example"
              }
            ]
          },
          "teInformationURI": [
            {
              "lang": "en",
              "uri": "https://pid-provider.example/policies"
            },
            {
              "lang": "en",
              "uri": "http://uri.etsi.org/19602/ListOfTrustedEntities/PIDProvider/IT"
            }
          ]
        },
        "trustedEntityServices": {
          "trustedEntityService": [
            {
              "serviceInformation": {
                "serviceTypeIdentifier": "http://uri.etsi.org/19602/SvcType/PID/Issuance",
                "serviceName": [
                  {
                    "lang": "en",
                    "value": "PID Issuance Service"
                  }
                ],
                "serviceDigitalIdentity": {
                  "x509Certificate": [
                    "MIIF..."
                  ]
                }
              }
            }
          ]
        }
      }
    ]
  }
}
```

### 6.3 Multilingual Format

**Multilingual String:**
```json
{
  "lang": "en",
  "value": "English text"
}
```

**Multilingual Pointer:**
```json
{
  "lang": "en",
  "uri": "https://example.org/page"
}
```

### 6.4 Date-Time Format

All date-time values must be ISO 8601 format in UTC:
- Format: `YYYY-MM-DDTHH:mm:ssZ`
- Example: `2025-01-01T00:00:00Z`

### 6.5 JSON Schema Validation

```bash
# Using ajv-cli
npm install -g ajv-cli
ajv validate -s lote-schema.json -d lote.json

# Using Python
python -m jsonschema lote.json lote-schema.json
```

## 7. Profile-Specific Requirements

### 7.1 PID Providers List (TS 119 602, Annex D)

#### Required URIs
- **LoTE Type**: `http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList`
- **Status Determination Approach**: `http://uri.etsi.org/19602/PIDProvidersList/StatusDetn/EU`
- **Scheme Type/Community/Rules**: `http://uri.etsi.org/19602/PIDProviders/schemerules/EU`
- **Service Types**: 
  - `http://uri.etsi.org/19602/SvcType/PID/Issuance`
  - `http://uri.etsi.org/19602/SvcType/PID/Revocation`

#### Key Requirements
- ServiceStatus component **shall not** be used
- StatusStartingTime component **shall not** be used
- HistoricalInformationPeriod **shall not** be present
- Next update maximum: 6 months
- Signature: Compact JAdES Baseline B

### 7.2 Wallet Providers List (TS 119 602, Annex E)

#### Required URIs
- **LoTE Type**: `http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList`
- **Status Determination Approach**: `http://uri.etsi.org/19602/WalletProvidersList/StatusDetn/EU`
- **Scheme Type/Community/Rules**: `http://uri.etsi.org/19602/WalletProvidersList/schemerules/EU`
- **Service Types**:
  - `http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance`
  - `http://uri.etsi.org/19602/SvcType/WalletSolution/Revocation`

#### Key Requirements
- ServiceStatus component **shall not** be used
- StatusStartingTime component **shall not** be used
- HistoricalInformationPeriod **shall not** be present
- ServiceUniqueIdentifier extension **shall** be used
- Next update maximum: 6 months
- Signature: Compact JAdES Baseline B

### 7.3 Pub-EAA Providers List and national non-qualified EAA Provider lists (TS 119 602, Annex H)

**Scope**: Annex H defines the LoTE profile for **Pub-EAA Providers** (EC-compiled list) and is also used for **national non-qualified EAA Provider Trusted Lists** compiled and published by Member State TLPs (per ARF v2.8.0 and the trust infrastructure schema).

#### Required URIs
- **LoTE Type**: `http://uri.etsi.org/19602/LoTEType/EUPubEAAProvidersList`
- **Status Determination Approach**: `http://uri.etsi.org/19602/PubEAAProvidersList/StatusDetn/EU`
- **Scheme Type/Community/Rules**: `http://uri.etsi.org/19602/PubEAAProvidersList/schemerules/EU`
- **Service Types**:
  - `http://uri.etsi.org/19602/SvcType/PubEAA/Issuance`
  - `http://uri.etsi.org/19602/SvcType/PubEAA/Revocation`
- **Service Status Values**:
  - `http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/notified`
  - `http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/withdrawn`

#### Key Requirements
- ServiceStatus component **shall** be present
- StatusStartingTime component **shall** be present
- HistoricalInformationPeriod **shall** be present with value `65535`
- Next update maximum: 6 months
- Signature: Compact JAdES Baseline B (JSON) or XAdES Baseline B (XML)
- Service history uses X509SKI (not X509Certificate)

## 8. Digital Signature Implementation

### 8.1 JAdES Signature (JSON - TS 119 602)

#### Requirements
- **Format**: Compact JAdES Baseline B
- **Standard**: ETSI TS 119 182-1

#### Implementation Steps
1. Create JWS header with algorithm
2. Build payload (LoTE JSON without signature)
3. Create JWS signature
4. Attach certificate chain in `x5c` header
5. Validate against JAdES Baseline B profile

#### Signature Structure
```json
{
  "protected": {
    "alg": "ES256",
    "x5u": "https://example.org/cert.pem"
  },
  "signature": "...",
  "header": {
    "x5c": ["MIIF..."]
  }
}
```

### 8.2 XAdES Signature (XML - TS 119 612/602)

#### Requirements
- **Format**: XAdES Baseline B
- **Standard**: ETSI EN 319 132-1
- **Type**: Enveloped signature
- **Canonicalization**: Exclusive XML Canonicalization

#### Signature Structure
```xml
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
  <SignedInfo>
    <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
    <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
    <Reference URI="">
      <Transforms>
        <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        <Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
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

### 8.3 Certificate Requirements

#### Subject DN Requirements
- **Country code**: Must match Scheme Territory
- **Organization**: Must match Scheme Operator Name

#### Key Usage
- Digital signature
- Non-repudiation

## 9. Distribution and Transport

### 9.1 HTTP Transport

#### 9.1.1 MIME Types

**XML (TS 119 612):**
```
Content-Type: application/vnd.etsi.tsl+xml
```

**JSON (TS 119 602):**
```
Content-Type: application/json
# Or specific:
Content-Type: application/vnd.etsi.lote+json
```

#### 9.1.2 HTTP Headers

```
HTTP/1.1 200 OK
Content-Type: application/vnd.etsi.tsl+xml
Content-Length: 12345
Last-Modified: Wed, 01 Jan 2025 00:00:00 GMT
ETag: "tsl-version-1"
Cache-Control: max-age=3600
```

#### 9.1.3 Distribution Points

**XML:**
```xml
<DistributionPoints>
  <DistributionPoint>
    <URI>https://trust-list.example.org/tsl/tsl.xml</URI>
  </DistributionPoint>
</DistributionPoints>
```

**JSON:**
```json
{
  "schemeInformation": {
    "distributionPoints": [
      "https://trust-list.example.org/lote/pid-providers.json"
    ]
  }
}
```

### 9.2 Availability Requirements

- Minimum 99.9% availability
- 24/7 operation
- Redundant distribution points
- Load balancing support

### 9.3 Update Frequency

- Daily updates for status changes
- Weekly full updates
- Emergency updates within 1 hour
- Notification of updates

## 10. Examples

For **procedures for authenticating and using trusted lists** (LoTL and EUMS national trusted lists when validating trust service outputs), see **ETSI TS 119 615** clause 4 (e.g. PRO-4.1 authenticating the EC compiled list of trusted lists, PRO-4.2 authenticating an EUMS trusted list, PRO-4.3 obtaining listed services matching a certificate, and subsequent determination procedures). This profile does not duplicate those normative procedures.

### 10.1 Complete XML TSL Example (TS 119 612)

See section 5.2 for complete XML example.

### 10.2 Complete JSON LoTE Example (TS 119 602)

See section 6.2 for complete JSON example.

### 10.3 Service with History (Pub-EAA)

```json
{
  "serviceInformation": {
    "serviceTypeIdentifier": "http://uri.etsi.org/19602/SvcType/PubEAA/Issuance",
    "serviceName": [
      {
        "lang": "en",
        "value": "Pub-EAA Issuance Service"
      }
    ],
    "serviceDigitalIdentity": {
      "x509Certificate": ["MIIF..."]
    },
    "serviceCurrentStatus": "http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/notified",
    "currentStatusStartingDateAndTime": "2025-01-01T00:00:00Z"
  },
  "serviceHistory": {
    "serviceHistoryInstance": [
      {
        "serviceName": [
          {
            "lang": "en",
            "value": "Pub-EAA Issuance Service"
          }
        ],
        "serviceDigitalIdentity": {
          "x509SKI": ["a1b2c3..."]
        },
        "servicePreviousStatus": "http://uri.etsi.org/19602/PubEAAProvidersList/SvcStatus/withdrawn",
        "previousStatusStartingDateAndTime": "2024-06-01T00:00:00Z"
      }
    ]
  }
}
```

## 11. Testing and Validation

### 11.1 XML Schema Validation

```bash
# Validate TSL against official ETSI schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd tsl.xml
```

### 11.2 JSON Schema Validation

```bash
# Using ajv-cli
ajv validate -s lote-schema.json -d lote.json

# Using Python
python -m jsonschema lote.json lote-schema.json
```

### 11.3 Signature Validation

#### XAdES Validation
```bash
xmlsec1 --verify --pubkey-cert-pem cert.pem tsl.xml
```

#### JAdES Validation
Use appropriate JAdES validation library (see section 12).

### 11.4 Profile-Specific Validation Checklists

#### PID Providers List
- [ ] LoTE type URI is correct
- [ ] Status determination approach URI is correct
- [ ] Scheme type/community/rules URI is correct
- [ ] ServiceStatus is NOT present
- [ ] StatusStartingTime is NOT present
- [ ] HistoricalInformationPeriod is NOT present
- [ ] Next update is within 6 months
- [ ] Signature is Compact JAdES Baseline B

#### Wallet Providers List
- [ ] LoTE type URI is correct
- [ ] ServiceUniqueIdentifier extension is present
- [ ] Other requirements similar to PID Providers

#### Pub-EAA Providers List
- [ ] LoTE type URI is correct
- [ ] ServiceStatus is present
- [ ] StatusStartingTime is present
- [ ] HistoricalInformationPeriod is `65535`
- [ ] Service history uses X509SKI (not X509Certificate)

## Implementation Checklist

### Core Implementation
- [ ] Choose standard (TS 119 612 or TS 119 602)
- [ ] Choose format (XML or JSON)
- [ ] Schema integration
- [ ] Data model implementation
- [ ] Multilingual support
- [ ] Date-time handling

### Profile Implementation
- [ ] PID Providers profile
- [ ] Wallet Providers profile
- [ ] WRPAC Providers profile
- [ ] WRPRC Providers profile
- [ ] Pub-EAA Providers profile
- [ ] Registrars and Registers profile

### Signature Implementation
- [ ] XAdES signature generation (XML)
- [ ] XAdES signature validation (XML)
- [ ] JAdES signature generation (JSON)
- [ ] JAdES signature validation (JSON)

### Distribution and Management
- [ ] Distribution points implementation
- [ ] HTTP/HTTPS transport
- [ ] Update mechanisms
- [ ] Version control
- [ ] List consumption API

## References

### Standards
- [ETSI TS 119 612 v2.4.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf)
- [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf)
- [ETSI TS 119 182-1](https://www.etsi.org/deliver/etsi_ts/119100_119199/11918201/01.02.01_60/ts_11918201v010201p.pdf) - JAdES
- [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf) - XAdES

### Schema Repositories
- [ETSI TS 119 612 XSD Schema](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd)
- [ETSI TS 119 612 SIE XSD Schema](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_sie_xsd.xsd)
- [ETSI TS 119 602 JSON/XML Schema](https://forge.etsi.org/rep/esi/x19_60201_lists_of_trusted_entities)

### Tools
- [Trusted List Manager non-EU](https://ec.europa.eu/digital-building-blocks/sites/display/TLSO/Trusted+List+Manager+non-EU)

### Regulations
- [Regulation (EU) No 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj) - eIDAS
- [Commission Implementing Regulation (EU) 2024/2980](https://eur-lex.europa.eu/eli/reg_impl/2024/2980/oj)
- [Commission Implementing Regulation (EU) 2025/1569](https://eur-lex.europa.eu/eli/reg_impl/2025/1569/oj)
- [Commission Implementing Regulation (EU) 2025/2164](https://eur-lex.europa.eu/eli/reg_impl/2025/2164/oj) – trusted lists / TS 119 612 (marked Done in ARF v2.8.0 STS list)

---

**Document Version**: 1.1  
**Last Updated**: 2025-02-02  
**ARF alignment**: v2.8.0 (ETSI TS 119 602 title "Lists of trusted entities; Data model" V1.1.1 (2025-11); Annex H for Pub-EAA and national non-qualified EAA Provider lists; TS 119 612 / CIR 2025/2164)

