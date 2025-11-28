# Attestation/EAA Provider Registration Certificate Example

## Overview

This example demonstrates Wallet-Relying Party Registration Certificates (WRPRC) for **Electronic Attestation of Attributes (EAA) Providers**. The WRPRC provides detailed information about the provider's entitlements, the attestations they issue, and their intended use.

## Normative References

| Reference | Document |
|-----------|----------|
| ETSI TS 119 475 | Relying party attributes supporting EUDI Wallet user's authorization decisions |
| ETSI TS 119 182-1 | JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures |
| ETSI EN 319 411-1 | Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements |
| CIR (EU) 2025/848 | Commission Implementing Regulation on the registration of wallet-relying parties |
| IETF RFC 7519 | JSON Web Token (JWT) |
| IETF RFC 8392 | CBOR Web Token (CWT) |
| IETF RFC 5646 | Tags for Identifying Languages |
| ISO 3166-1 | Codes for the representation of names of countries |

---

## JWT Format Example - Qualified EAA Provider

### Header

Per ETSI TS 119 475 clause 5.2.2 (Table 5) and ETSI TS 119 182-1:

```json
{
  "typ": "rc-wrp+jwt",
  "alg": "ES384",
  "b64": true,
  "cty": ["b64"],
  "x5c": ["<base64-encoded-certificate-chain>"]
}
```

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `typ` | `rc-wrp+jwt` | ETSI TS 119 475 Table 5 | Registration Certificate for WRP in JWT format |
| `alg` | `ES384` | ETSI TS 119 182-1 clause 5.1.2; ETSI TS 119 475 GEN-5.2.1-04 | Signing algorithm |
| `b64` | `true` | ETSI TS 119 182-1 clause 5.1.2; ETSI TS 119 475 Table 5 | Base64 encoding indicator |
| `cty` | `["b64"]` | ETSI TS 119 182-1 clause 5.1.3; ETSI TS 119 475 Table 5 | Content type |
| `x5c` | Certificate chain | ETSI TS 119 182-1 clause 5.1.8; ETSI TS 119 475 Table 5 | Certificate chain for verification |

### Payload

Per ETSI TS 119 475 clause 5.2.4 (Tables 7, 8):

```json
{
  "name": "Spanish Driving License Attestation Service",
  "sub": {
    "legal_name": "Ministerio del Interior - Dirección General de Tráfico",
    "id": "VATES-S2800001J"
  },
  "country": "ES",
  "registry_uri": "https://registro.mineco.gob.es/wrp/api/v1/relying-parties/ES-WRP-00123",
  "service": [
    {
      "lang": "es-ES",
      "value": "Servicio de emisión de permisos de conducir digitales y attestaciones relacionadas con la conducción"
    },
    {
      "lang": "en-US",
      "value": "Digital driving license and driving-related attestation issuance service"
    }
  ],
  "entitlements": [
    "https://uri.etsi.org/19475/Entitlement/QEAA_Provider",
    "https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider"
  ],
  "provided_attestations": [
    {
      "format": "dc+sd-jwt",
      "meta": {
        "vct_values": [
          "https://credentials.dgt.es/mobile-driving-license"
        ]
      },
      "claims": [
        { "path": ["family_name"] },
        { "path": ["given_name"] },
        { "path": ["birth_date"] },
        { "path": ["portrait"] },
        { "path": ["driving_privileges"] },
        { "path": ["issue_date"] },
        { "path": ["expiry_date"] },
        { "path": ["issuing_authority"] },
        { "path": ["document_number"] },
        { "path": ["issuing_country"] }
      ]
    },
    {
      "format": "mso_mdoc",
      "meta": {
        "doctype_value": "org.iso.18013.5.1.mDL"
      },
      "claims": [
        { "path": ["org.iso.18013.5.1", "family_name"] },
        { "path": ["org.iso.18013.5.1", "given_name"] },
        { "path": ["org.iso.18013.5.1", "birth_date"] },
        { "path": ["org.iso.18013.5.1", "portrait"] },
        { "path": ["org.iso.18013.5.1", "driving_privileges"] }
      ]
    }
  ],
  "privacy_policy": "https://dgt.es/privacy-policy",
  "info_uri": "https://dgt.es",
  "dpa": {
    "uri": "https://www.aepd.es",
    "email": "ciudadano@aepd.es",
    "phone": "+34 91 266 35 17"
  },
  "public_body": true,
  "policy_id": [
    "0.4.0.19475.3.1"
  ],
  "certificate_policy": "https://pki.dgt.es/wrprc-policy",
  "iat": 1704067200,
  "exp": 1735689600,
  "status": {
    "status_list": {
      "idx": 42,
      "uri": "https://status.dgt.es/wrprc/statuslist/1"
    }
  }
}
```

---

## Payload Fields with ETSI References

### Core Identity Fields

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `name` | `Spanish Driving License...` | ETSI TS 119 475 Table 7; B.2.1 `tradeName` | Annex I.2 | Trade/service name |
| `sub.legal_name` | `Ministerio del Interior...` | ETSI TS 119 475 Table 7; B.2.3 `legalName` | Annex I.1 | Official legal name |
| `sub.id` | `VATES-S2800001J` | ETSI TS 119 475 Table 7, GEN-5.2.4-02; B.2.5 `identifier` | Annex I.3 | Organizational identifier per clause 5.1.3 |
| `country` | `ES` | ETSI TS 119 475 Table 7; B.2.2 `country` | Annex I.6 | ISO 3166-1 alpha-2 code |
| `registry_uri` | URL | ETSI TS 119 475 Table 7; B.2.1 `registryURI` | Article 3(5) | National registry API endpoint |

### Service Description

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `service` | Array | ETSI TS 119 475 Table 7; B.2.1 `srvDescription` | Annex I.8 | Multilingual service descriptions |
| `service[].lang` | `es-ES`, `en-US` | ETSI TS 119 475 Table 7; B.2.6 `lang`; IETF RFC 5646 | - | BCP 47 language tag |
| `service[].value` | Description text | ETSI TS 119 475 Table 7; B.2.6 `content` | - | Service description in language |

### Entitlements

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `entitlements` | Array of URIs | ETSI TS 119 475 Table 7, GEN-5.2.4-03; B.2.1 `entitlement` | Annex I.12 | WRP entitlements per Annex A.2 |

### Provided Attestations (EAA Provider Specific)

Per ETSI TS 119 475 Table 8 and GEN-5.2.4-05:

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `provided_attestations` | Array | ETSI TS 119 475 Table 8; B.2.1 `providesAttestations` | Annex I.13 | Attestations issued by provider |
| `provided_attestations[].format` | `dc+sd-jwt`, `mso_mdoc` | ETSI TS 119 475 Table 8; B.2.9 `format` | Annex I.13 | Credential format |
| `provided_attestations[].meta` | Object | ETSI TS 119 475 Table 8; B.2.9 `meta` | Annex I.13 | Credential type metadata |
| `provided_attestations[].claims` | Array | ETSI TS 119 475 Table 8; B.2.9 `claim` | Annex I.13 | Attributes in attestation |

### Privacy and Policy

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `privacy_policy` | URL | ETSI TS 119 475 Table 7; B.2.7 `privacyPolicy` | Article 8.2(g) | Privacy policy URL |
| `info_uri` | URL | ETSI TS 119 475 Table 7; B.2.2 `infoURI` | Annex I.5 | General information URL |
| `public_body` | `true`/`false` | ETSI TS 119 475 Table 10; B.2.1 `isPSB` | Annex I.11 | Public sector body indicator |

### Data Protection Authority

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `dpa` | Object | ETSI TS 119 475 Table 7; B.2.1 `supervisoryAuthority` | Annex IV.3(g), Annex V.3(f) | DPA information |
| `dpa.uri` | URL | ETSI TS 119 475 Table 7; B.2.2 `infoURI` | - | DPA website |
| `dpa.email` | Email | ETSI TS 119 475 Table 7; B.2.2 `email` | - | DPA contact email |
| `dpa.phone` | Phone | ETSI TS 119 475 Table 7; B.2.2 `phone` | - | DPA contact phone |

### Technical Fields

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `policy_id` | `["0.4.0.19475.3.1"]` | ETSI TS 119 475 Table 7, clause 6.1.3 | WRPRC policy OID |
| `certificate_policy` | URL | ETSI TS 119 475 Table 7 | CPS/CP URL |
| `iat` | Unix timestamp | ETSI TS 119 475 Table 7 | Issuance time |
| `exp` | Unix timestamp | ETSI TS 119 475 Table 10, GEN-5.2.4-08 | Expiration (max 12 months after iat) |
| `status` | Object | ETSI TS 119 475 Table 7, GEN-6.2.6.1-04 | Status list reference |
| `status.status_list.idx` | Number | ETSI TS 119 475 GEN-6.2.6.1-04, GEN-6.2.6.1-05 | Position in status bitstring |
| `status.status_list.uri` | URL | ETSI TS 119 475 GEN-6.2.6.1-04 | Status list credential URI |

---

## JWT Format Example - Non-Qualified EAA Provider (University)

### Payload

```json
{
  "name": "University of Amsterdam Credential Service",
  "sub": {
    "legal_name": "Universiteit van Amsterdam",
    "id": "NTRNLD-KVK34567890"
  },
  "country": "NL",
  "registry_uri": "https://wrp-register.nl/api/v1/relying-parties/NL-WRP-00456",
  "service": [
    {
      "lang": "nl-NL",
      "value": "Uitgifte van digitale studentenkaarten en academische credentials"
    },
    {
      "lang": "en-US",
      "value": "Issuance of digital student cards and academic credentials"
    }
  ],
  "entitlements": [
    "https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider"
  ],
  "provided_attestations": [
    {
      "format": "dc+sd-jwt",
      "meta": {
        "vct_values": [
          "https://credentials.uva.nl/student-id"
        ]
      },
      "claims": [
        { "path": ["family_name"] },
        { "path": ["given_name"] },
        { "path": ["student_id"] },
        { "path": ["faculty"] },
        { "path": ["program"] },
        { "path": ["enrollment_date"] },
        { "path": ["expected_graduation"] },
        { "path": ["student_status"] }
      ]
    },
    {
      "format": "dc+sd-jwt",
      "meta": {
        "vct_values": [
          "https://credentials.uva.nl/diploma"
        ]
      },
      "claims": [
        { "path": ["family_name"] },
        { "path": ["given_name"] },
        { "path": ["degree_title"] },
        { "path": ["field_of_study"] },
        { "path": ["graduation_date"] },
        { "path": ["honors"] },
        { "path": ["diploma_number"] }
      ]
    }
  ],
  "privacy_policy": "https://uva.nl/privacy",
  "info_uri": "https://credentials.uva.nl",
  "dpa": {
    "uri": "https://autoriteitpersoonsgegevens.nl",
    "email": "info@autoriteitpersoonsgegevens.nl",
    "phone": "+31 70 888 85 00"
  },
  "public_body": false,
  "policy_id": [
    "0.4.0.19475.3.1"
  ],
  "certificate_policy": "https://pki.uva.nl/wrprc-policy",
  "iat": 1704067200,
  "exp": 1735689600,
  "status": {
    "status_list": {
      "idx": 78,
      "uri": "https://status.uva.nl/wrprc/statuslist/1"
    }
  }
}
```

---

## Entitlements for EAA Providers

Per ETSI TS 119 475 Annex A.2 and CIR 2025/848 Annex I.12:

| Entitlement | URI | OID | ETSI Reference | Description |
|-------------|-----|-----|----------------|-------------|
| QEAA_Provider | `https://uri.etsi.org/19475/Entitlement/QEAA_Provider` | `0.4.0.19475.1.2` | Annex A.2.2 | Qualified EAA provider |
| Non_Q_EAA_Provider | `https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider` | `0.4.0.19475.1.3` | Annex A.2.3 | Non-qualified EAA provider |
| PUB_EAA_Provider | `https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider` | `0.4.0.19475.1.4` | Annex A.2.4 | Public sector EAA provider |

---

## Organizational Identifier Formats

Per ETSI TS 119 475 clause 5.1.3 and Table 2:

| Type URI (B.2.5) | Semantic Prefix | ETSI Reference | EU Regulation |
|------------------|-----------------|----------------|---------------|
| `http://data.europa.eu/eudi/id/EUID` | `NTR` | GEN-5.1.3-02, Table 2 | CIR 2020/2244 |
| `http://data.europa.eu/eudi/id/LEI` | `LEI` | GEN-5.1.3-02, Table 2 | CIR 2022/1860 |
| `http://data.europa.eu/eudi/id/VATIN` | `VAT` | GEN-5.1.3-02, Table 2 | Directive 2006/112/EC |

---

## WRPRC Policy OID

Per ETSI TS 119 475 clause 6.1.3:

```
wrprc OBJECT IDENTIFIER ::=
{ itu-t(0) identified-organization(4) etsi(0) eudiwrpa(19475) policy-identifiers(3) wrprc(1) }

OID: 0.4.0.19475.3.1
```

---

## Mapping to National Register (Annex B Classes)

Per ETSI TS 119 475 Annex B:

| Annex B Class | Attribute | WRPRC Field | CIR 2025/848 |
|---------------|-----------|-------------|--------------|
| B.2.1 WalletRelyingParty | `tradeName` | `name` | Annex I.2 |
| B.2.1 WalletRelyingParty | `registryURI` | `registry_uri` | Article 3(5) |
| B.2.1 WalletRelyingParty | `srvDescription` | `service` | Annex I.8 |
| B.2.1 WalletRelyingParty | `entitlement` | `entitlements` | Annex I.12 |
| B.2.1 WalletRelyingParty | `providesAttestations` | `provided_attestations` | Annex I.13 |
| B.2.1 WalletRelyingParty | `isPSB` | `public_body` | Annex I.11 |
| B.2.1 WalletRelyingParty | `supervisoryAuthority` | `dpa` | Annex IV.3(g) |
| B.2.2 LegalEntity | `country` | `country` | Annex I.6 |
| B.2.2 LegalEntity | `infoURI` | `info_uri` | Annex I.5 |
| B.2.3 LegalPerson | `legalName` | `sub.legal_name` | Annex I.1 |
| B.2.5 Identifier | `identifier` | `sub.id` | Annex I.3 |
| B.2.6 MultiLangString | `lang`, `content` | `service[].lang`, `service[].value` | - |
| B.2.7 IntendedUse | `privacyPolicy` | `privacy_policy` | Article 8.2(g) |
| B.2.9 Credential | `format`, `meta`, `claim` | `provided_attestations[].*` | Annex I.13 |

---

## Use Cases

EAA Provider Registration Certificates are used to:

1. **Declare attestation types** - Specify which attestations the provider can issue (per CIR 2025/848 Annex I.13)
2. **Define claim schemas** - List the attributes included in each attestation type
3. **Support transparency** - Allow wallet users to understand what credentials are available
4. **Enable discovery** - Help wallets identify appropriate attestation providers
5. **Facilitate trust decisions** - Provide information for embedded disclosure policies (per CIR 2024/2979 Article 10)
