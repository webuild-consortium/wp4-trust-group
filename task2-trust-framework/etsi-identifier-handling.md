# Handling of Business Identifiers in ETSI Profiles

## Executive Summary

This document analyzes how specific business and tax identifiers (VAT registration number, tax reference number, LEI, EORI number, and excise number) are handled or considered in the current ETSI profiles, particularly in the context of trusted lists content and certificates.

## Table of Contents

1. [Overview](#overview)
2. [ETSI TS 119 612 - Trusted Lists (XML)](#etsi-ts-119-612)
3. [ETSI TS 119 602 - Lists of Trusted Entities (JSON/XML)](#etsi-ts-119-602)
4. [ETSI EN 319 412-1 - Certificate Profile Requirements](#etsi-en-319-412-1)
5. [Identifier Format Specifications](#identifier-format-specifications)
6. [Usage in Certificates](#usage-in-certificates)
7. [Usage in Trusted Lists](#usage-in-trusted-lists)
8. [Gaps and Considerations](#gaps-and-considerations)

## Overview

The ETSI profiles provide specific guidance on how to handle official registration identifiers for legal entities and natural persons. These identifiers are used in:

1. **Trusted Lists (TS 119 612)**: In the `TSPTradeName` field
2. **Lists of Trusted Entities (TS 119 602)**: In the `TETradeName` field
3. **X.509 Certificates (EN 319 412-1)**: In the `organizationIdentifier` attribute (for legal entities) or `serialNumber` attribute (for natural persons)

## ETSI TS 119 612 - Trusted Lists (XML)

### Legal Person Identifiers

According to **ETSI TS 119 612 v2.4.1, clause 5.4.2** (TSP Trade Name), when a Trust Service Provider (TSP) is a legal person, the registration identifier must be expressed using the following structure:

```
[TYPE]-[COUNTRY]-[IDENTIFIER]
```

Where:
- **TYPE**: 3-character legal person identity type reference
- **COUNTRY**: 2-character ISO 3166-1 country code
- **IDENTIFIER**: The actual identifier value

### Supported Identifier Types for Legal Persons

#### 1. VAT Registration Number ✅ **EXPLICITLY SUPPORTED**

- **Type Code**: `VAT`
- **Description**: National value added tax identification number
- **Priority**: **HIGHEST PRIORITY** - When both a VAT number and other national identification numbers exist, the VAT number **shall** be used
- **Format**: `VAT-[COUNTRY]-[VAT_NUMBER]`
- **Example**: `VAT-IT-12345678901`

#### 2. National Trade Register (NTR) ✅ **EXPLICITLY SUPPORTED**

- **Type Code**: `NTR`
- **Description**: Identifier from a national register (e.g., national trade register)
- **Usage**: Used when:
  - No VAT number exists, OR
  - No registered identifier exists (TLSO allocates identifier and uses "NTR")
- **Format**: `NTR-[COUNTRY]-[REGISTER_NUMBER]`
- **Example**: `NTR-DE-HRB123456`

#### 3. LEI (Legal Entity Identifier) ✅ **EXPLICITLY SUPPORTED**

- **Type Code**: `LEI`
- **Description**: Legal Entity Identifier according to ISO 17442-1
- **Standard**: Defined in **ETSI EN 319 412-1 V1.6.1**, section 5.1.4
- **Format**: `LEIXG-[20_CHARACTER_LEI]`
- **Country Code**: `XG` (special code for global identifiers)
- **Example**: `LEIXG-5493001KJTIIGC8Y1R12`
- **Usage**: Can be used in `organizationIdentifier` attribute in X.509 certificates
- **Note**: LEI uses `XG` instead of a country code because it's a globally unique identifier

#### 4. EORI Number ❓ **NOT EXPLICITLY MENTIONED**

- **Status**: Not explicitly mentioned in ETSI TS 119 612 or EN 319 412-1
- **Potential Usage**: Could potentially be used as an NTR identifier if registered in a national trade register
- **Recommendation**: Should be clarified with ETSI or scheme operators

#### 5. Excise Number ❓ **NOT EXPLICITLY MENTIONED**

- **Status**: Not explicitly mentioned in ETSI TS 119 612 or EN 319 412-1
- **Potential Usage**: Could potentially be used as an NTR identifier if registered in a national trade register
- **Recommendation**: Should be clarified with ETSI or scheme operators

### Natural Person Identifiers

For natural persons, the following types are supported:

1. **PAS**: Passport number
2. **IDC**: National identity card number
3. **PNO**: National personal number (civic registration number)
4. **TIN**: Tax Identification Number ✅ **EXPLICITLY SUPPORTED**
   - According to European Commission - Tax and Customs Union
   - Format: `TIN-[COUNTRY]-[TAX_ID]`
   - Reference: http://ec.europa.eu/taxation_customs/tin/tinByCountry.html

## ETSI TS 119 602 - Lists of Trusted Entities (JSON/XML)

### TE Trade Name Requirements

According to **ETSI TS 119 602 v1.1.1**, the `TETradeName` component (clause 6.5.2) must include an official registration identifier that unambiguously identifies the trusted entity.

### Profile-Specific Requirements

#### PID Providers List (Annex D)
- **Legal Entity**: Must use `organizationIdentifier` semantics per **EN 319 412-1 requirements LEG-5.1.4-02, LEG-5.1.4-03, LEG-5.1.4-04**
- **Natural Person**: Must use `serialNumber` semantics per **EN 319 412-1 requirements NAT-5.1.3-02, NAT-5.1.3-03, NAT-5.1.3-04**

#### Wallet Providers List (Annex E)
- Same requirements as PID Providers List
- The registration identifier must be included in the `TETradeName` component

#### WRPAC Providers List (Annex F)
- Same requirements as PID Providers List

#### WRPRC Providers List (Annex G)
- Same requirements as PID Providers List

#### Pub-EAA Providers List (Annex H)
- Same requirements as PID Providers List

### Certificate Digital Identity

The `ServiceDigitalIdentity` component (clause 6.6.3) must contain X.509 certificates where:
- The certified identity data **include the name** (from `TEName`)
- The certified identity data **include the registration number** (from `TETradeName`), where applicable

This means the registration identifier must be present in the certificate's subject distinguished name.

## ETSI EN 319 412-1 - Certificate Profile Requirements

### organizationIdentifier Attribute (Legal Entities)

The ETSI TS 119 602 profiles reference **ETSI EN 319 412-1** requirements:

- **LEG-5.1.4-02**: Requirements for organizationIdentifier attribute
- **LEG-5.1.4-03**: Additional requirements for organizationIdentifier
- **LEG-5.1.4-04**: Further specifications for organizationIdentifier

### LEI (Legal Entity Identifier) Support ✅ **EXPLICITLY DEFINED**

According to **ETSI EN 319 412-1 V1.6.1 (2025-06)**, section 5.1.4, the LEI is **explicitly supported** in the `organizationIdentifier` attribute for legal entities.

#### LEI Format Specification

When the `organizationIdentifier` is used to represent an LEI, it **must** follow this structure:

- **Prefix**: `LEI`
- **Country Code**: `XG` (indicating a global identifier, not country-specific)
- **Separator**: Hyphen `-`
- **Identifier**: The 20-character LEI value

**Format**: `LEIXG-[20_CHARACTER_LEI]`

**Example**: `LEIXG-5493001KJTIIGC8Y1R12`

#### Key Points

1. **Type Code**: `LEI` (3-character prefix)
2. **Country Code**: `XG` (special code for global identifiers, not a real ISO 3166-1 country code)
3. **LEI Value**: Exactly 20 alphanumeric characters (as per ISO 17442-1)
4. **Usage**: Can be used in the `organizationIdentifier` attribute in X.509 certificates
5. **Standard Reference**: Aligns with ISO 17442-1 (LEI standard)

**Note**: The LEI format differs from other identifiers because it uses `XG` instead of a country code, reflecting that LEIs are globally unique identifiers not tied to a specific country.

### serialNumber Attribute (Natural Persons)

For natural persons:
- **NAT-5.1.3-02**: Requirements for serialNumber attribute
- **NAT-5.1.3-03**: Additional requirements for serialNumber
- **NAT-5.1.3-04**: Further specifications for serialNumber

## Identifier Format Specifications

### Complete Format Structure

```
[TYPE]-[COUNTRY]-[IDENTIFIER]
```

### Examples

#### VAT Registration Number
```
VAT-IT-12345678901
VAT-FR-FR12345678901
VAT-DE-DE123456789
```

#### National Trade Register
```
NTR-DE-HRB123456
NTR-IT-12345678901
NTR-FR-123456789
```

#### Legal Entity Identifier (LEI)
```
LEIXG-5493001KJTIIGC8Y1R12
LEIXG-213800ZBKL9B1FRTM75
LEIXG-7ZW8QJWVPR4P1JRNK46
```

#### Tax Identification Number (Natural Person)
```
TIN-IT-ABCDEF12G34H567I
TIN-FR-12345678901
```

### Character Restrictions

- **Type**: Exactly 3 uppercase ASCII characters
- **Country**: Exactly 2 uppercase ISO 3166-1 Alpha-2 characters
- **Separator**: Hyphen-minus "-" (0x2D ASCII, U+002D UTF-8)
- **Identifier**: According to country and identity type reference (no explicit format restrictions beyond country-specific rules)

## Usage in Certificates

### X.509 Certificate Subject DN

When certificates are issued for entities listed in trusted lists, the registration identifier should appear in the certificate's subject distinguished name:

#### For Legal Entities
- **Attribute**: `organizationIdentifier`
- **Format**: Must match the format used in trusted lists (`TYPE-COUNTRY-IDENTIFIER`)
- **Example**: 
  ```
  CN=Example Corp
  O=Example Corporation
  organizationIdentifier=VAT-IT-12345678901
  C=IT
  ```

#### For Natural Persons
- **Attribute**: `serialNumber`
- **Format**: Must match the format used in trusted lists
- **Example**:
  ```
  CN=Mario Rossi
  serialNumber=TIN-IT-ABCDEF12G34H567I
  C=IT
  ```

### Validation Requirements

According to ETSI TS 119 602, the certificate's subject DN must:
1. Include the name from `TEName` component
2. Include the registration number from `TETradeName` component (where applicable)
3. Match the format specified in the trusted list entry

## Usage in Trusted Lists

### TS 119 612 (XML Trusted Lists)

**Field**: `TSPTradeName` (clause 5.4.2)

**Structure**:
```xml
<TSPTradeName>
  <Name xml:lang="en">VAT-IT-12345678901</Name>
</TSPTradeName>
```

### TS 119 602 (JSON/XML Lists of Trusted Entities)

**Field**: `TETradeName` (clause 6.5.2)

**JSON Structure**:
```json
{
  "teTradeName": [
    {
      "lang": "en",
      "value": "VAT-IT-12345678901"
    }
  ]
}
```

**XML Structure**:
```xml
<TETradeName>
  <Name xml:lang="en">VAT-IT-12345678901</Name>
</TETradeName>
```

## Gaps and Considerations

### Explicitly Supported Identifiers

✅ **VAT Registration Number**: Fully supported with highest priority
✅ **Tax Reference Number (TIN)**: Supported for natural persons
✅ **National Trade Register (NTR)**: Supported as fallback for legal entities
✅ **LEI (Legal Entity Identifier)**: **EXPLICITLY SUPPORTED** in ETSI EN 319 412-1 V1.6.1
  - Format: `LEIXG-[20_CHARACTER_LEI]`
  - Used in `organizationIdentifier` attribute
  - Also referenced in ETSI TS 119 475 V1.1.1 with URI `http://data.europa.eu/eudi/id/LEI`

### Not Explicitly Mentioned

❓ **EORI Number (Economic Operator Registration and Identification)**:

❓ **EORI Number (Economic Operator Registration and Identification)**:
- Not explicitly mentioned in ETSI TS 119 612
- Could potentially be used under NTR if registered in a national trade register
- **Recommendation**: Clarify with scheme operators or ETSI

❓ **Excise Number**:
- Not explicitly mentioned in ETSI TS 119 612
- Could potentially be used under NTR if registered in a national trade register
- **Recommendation**: Clarify with scheme operators or ETSI

### Identifier Support Comparison Matrix

The following table provides a quick reference for ETSI support status of all discussed identifiers:

| Identifier | ETSI Support | Primary Specification | Format | Notes |
|------------|--------------|----------------------|--------|-------|
| **VAT Registration Number** | ✅ Explicit | TS 119 612, EN 319 412-1 | `VAT-[COUNTRY]-[VAT_NUMBER]` | Highest priority when available |
| **NTR (National Trade Register)** | ✅ Explicit | TS 119 612, EN 319 412-1 | `NTR-[COUNTRY]-[REGISTER_NUMBER]` | Fallback when VAT not available |
| **LEI (Legal Entity Identifier)** | ✅ Explicit | EN 319 412-1 V1.6.1 | `LEIXG-[20_CHARACTER_LEI]` | Uses `XG` for global identifier |
| **TIN (Tax Identification Number)** | ✅ Explicit | TS 119 612 | `TIN-[COUNTRY]-[TAX_ID]` | For natural persons only |
| **EORI Number** | ❌ Not defined | - | - | Could potentially use NTR format |
| **Excise Number** | ❌ Not defined | - | - | Could potentially use NTR format |

**Legend:**
- ✅ **Explicit**: Fully defined and supported in ETSI specifications
- ❌ **Not defined**: Not mentioned in any ETSI specification

### Priority Rules

According to ETSI TS 119 612:

1. **If VAT number exists**: MUST use VAT (highest priority)
2. **If no VAT number but NTR exists**: Use NTR
3. **If no registered identifier exists**: TLSO allocates identifier and uses "NTR"

### Recommendations

1. **For LEI**: ✅ **Already explicitly supported** in ETSI EN 319 412-1 V1.6.1 - Use format `LEIXG-[20_CHARACTER_LEI]`
2. **For EORI**: Consider adding explicit support or clarification that EORI can be used under NTR type
3. **For Excise Numbers**: Consider adding explicit support or clarification that excise numbers can be used under NTR type
4. **Certificate Implementation**: Ensure certificates in the `certs` branch include the registration identifier in the appropriate format
5. **Validation**: Implement validation to ensure registration identifiers match between trusted lists and certificates

## Implementation Checklist

### For Trusted Lists

- [ ] Include registration identifier in `TSPTradeName` (TS 119 612) or `TETradeName` (TS 119 602)
- [ ] Use correct format: `[TYPE]-[COUNTRY]-[IDENTIFIER]`
- [ ] Prioritize VAT number when available
- [ ] Use NTR as fallback when VAT is not available
- [ ] Ensure country code matches ISO 3166-1 Alpha-2

### For Certificates

- [ ] Include registration identifier in certificate subject DN
- [ ] Use `organizationIdentifier` attribute for legal entities
- [ ] Use `serialNumber` attribute for natural persons
- [ ] Match format exactly with trusted list entry
- [ ] Validate format during certificate issuance

### For Validation

- [ ] Verify registration identifier format matches ETSI specifications
- [ ] Cross-reference registration identifier between trusted list and certificate
- [ ] Validate country code is valid ISO 3166-1 Alpha-2
- [ ] Check priority rules (VAT > NTR)

## References

### ETSI Standards

- **ETSI TS 119 612 v2.4.1** (2025-08): Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists
  - Clause 5.4.2: TSP Trade Name
  - [Official Document](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf)

- **ETSI TS 119 602 v1.1.1** (2025-11): Electronic Signatures and Trust Infrastructures (ESI); Trusted lists; Data model
  - Clause 6.5.2: TE Trade Name
  - Annex D: PID Providers List Profile
  - Annex E: Wallet Providers List Profile
  - Annex F: WRPAC Providers List Profile
  - Annex G: WRPRC Providers List Profile
  - Annex H: Pub-EAA Providers List Profile
  - [Official Document](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf)

- **ETSI EN 319 412-1 V1.6.1** (2025-06): Electronic Signatures and Infrastructures (ESI); Certificate Profiles; Part 1: Overview and Common Data Structures
  - Requirements LEG-5.1.4-02, LEG-5.1.4-03, LEG-5.1.4-04 (organizationIdentifier)
  - Requirements NAT-5.1.3-02, NAT-5.1.3-03, NAT-5.1.3-04 (serialNumber)
  - **Section 5.1.4**: Explicitly defines LEI format as `LEIXG-[20_CHARACTER_LEI]`
  - [Official Document](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601c.pdf)

- **ETSI TS 119 475 V1.1.1** (2025-10): Relying party attributes supporting EUDI Wallet User's authorisation decisions
  - References LEI as a recognized identifier for legal entities
  - LEI URI: `http://data.europa.eu/eudi/id/LEI`
  - Aligns with ISO 17442-1 standards
  - [Official Document](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.01.01_60/ts_119475v010101p.pdf)

### External References

- **ISO 3166-1**: Country codes
- **ISO 17442-1**: Legal Entity Identifier (LEI) standard
- **European Commission - Tax and Customs Union - TIN**: http://ec.europa.eu/taxation_customs/tin/tinByCountry.html
- **GLEIF (Global Legal Entity Identifier Foundation)**: https://www.gleif.org/ - LEI registration and management

---

**Document Version**: 1.0  
**Last Updated**: 2025-01-28  
**Author**: Analysis based on ETSI TS 119 612, TS 119 602, and EN 319 412-1 specifications

