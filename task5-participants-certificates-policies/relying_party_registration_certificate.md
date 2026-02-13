# Relying Party Registration Certificate Example

## Overview

This example demonstrates Wallet-Relying Party Registration Certificates (WRPRC) for **Service Providers** - general relying parties that request attributes from EUDIW users.

## Normative References

| Reference | Document |
|-----------|----------|
| ETSI TS 119 475 | Relying party attributes supporting EUDI Wallet user's authorization decisions |
| ETSI TS 119 182-1 | JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures |
| ETSI EN 319 411-1 | Policy and security requirements for Trust Service Providers; Part 1: General requirements |
| CIR (EU) 2025/848 | Commission Implementing Regulation on the registration of wallet-relying parties |
| IETF RFC 7519 | JSON Web Token (JWT) |
| IETF RFC 5646 | Tags for Identifying Languages |

---

## Example 1: E-Commerce Age Verification

### JWT Header

Per ETSI TS 119 475 clause 5.2.2 (Table 5):

```json
{
  "typ": "rc-wrp+jwt",
  "alg": "ES384",
  "b64": true,
  "cty": "b64",
  "x5c": ["<base64-encoded-certificate-chain>"]
}
```

| Field | ETSI Reference | Description |
|-------|----------------|-------------|
| `typ` | ETSI TS 119 475 Table 5 | `rc-wrp+jwt` for JWT format |
| `alg` | ETSI TS 119 182-1 clause 5.1.2 | Signing algorithm |
| `x5c` | ETSI TS 119 182-1 clause 5.1.8 | Certificate chain |

### JWT Payload

```json
{
  "name": "Online Shop AG",
  "sub": {
    "legal_name": "Online Shop AG",
    "id": "LEIDE-529900T8BM49AURSDO55"
  },
  "country": "DE",
  "registry_uri": "https://wrp-register.de/api/v1/relying-parties/DE-WRP-00789",
  "service": [
    { "lang": "de-DE", "value": "Online-Einkaufsplattform mit Altersverifikation" },
    { "lang": "en-US", "value": "Online shopping platform with age verification" }
  ],
  "entitlements": ["https://uri.etsi.org/19475/Entitlement/Service_Provider"],
  "purpose": [
    { "lang": "de-DE", "value": "Altersverifikation für altersbeschränkte Produkte gemäß JuSchG" },
    { "lang": "en-US", "value": "Age verification for age-restricted products" }
  ],
  "credentials": [
    {
      "format": "dc+sd-jwt",
      "meta": { "vct_values": ["https://credentials.example.eu/pid"] },
      "claims": [{ "path": ["age_over_18"] }]
    }
  ],
  "privacy_policy": "https://shop.example.de/privacy",
  "info_uri": "https://shop.example.de",
  "support_uri": "https://shop.example.de/support",
  "dpa": {
    "uri": "https://www.bfdi.bund.de",
    "email": "poststelle@bfdi.bund.de",
    "phone": "+49 228 997799 0"
  },
  "public_body": false,
  "policy_id": ["0.4.0.19475.3.1"],
  "certificate_policy": "https://wrp-register.de/policies/service-provider",
  "iat": 1704067200,
  "exp": 1735689600,
  "status": { "status_list": { "idx": 156, "uri": "https://status.wrp-register.de/statuslist/1" } }
}
```

---

## Payload Fields with ETSI References

### Identity Fields
          Per ETSI TS 119 475 Table 7 and GEN-5.2.4-02:
| Field | ETSI Reference | CIR 2025/848 | Description |
|-------|----------------|--------------|-------------|
| `name` | Table 7; B.2.1 `tradeName` | Annex I.2 | Trade/service name |
| `sub.legal_name` | Table 7; B.2.3 `legalName` | Annex I.1 | Official legal name |
| `sub.id` | Table 7, GEN-5.2.4-02; B.2.5 | Annex I.3 | Identifier per clause 5.1.3 |
| `country` | Table 7; B.2.2 `country` | Annex I.6 | ISO 3166-1 alpha-2 |
| `registry_uri` | Table 7; B.2.1 `registryURI` | Article 3(5) | National registry API |

### Service and Purpose (Service Provider Specific)

Per ETSI TS 119 475 Table 9 and GEN-5.2.4-06:

| Field | ETSI Reference | CIR 2025/848 | Description |
|-------|----------------|--------------|-------------|
| `service` | Table 7; B.2.1 `srvDescription` | Annex I.8 | Service descriptions |
| `purpose` | Table 9; B.2.7 `purpose` | Article 8.2(b) | Purpose of data processing |
| `credentials` | Table 9; B.2.7 `credential` | Annex I.9 | Requested credential types |
| `credentials[].format` | Table 9; B.2.9 `format` | Annex I.9 | Credential format |
| `credentials[].meta` | Table 9; B.2.9 `meta` | Annex I.9 | Credential type metadata |
| `credentials[].claims` | Table 9; B.2.9 `claim` | Annex I.9 | Requested attributes |

### Privacy and Policy

| Field | ETSI Reference | CIR 2025/848 | Description |
|-------|----------------|--------------|-------------|
| `privacy_policy` | Table 7; B.2.7 `privacyPolicy` | Article 8.2(g) | Privacy policy URL |
| `info_uri` | Table 7; B.2.2 `infoURI` | Annex I.5 | Information URL |
| `support_uri` | Table 10; B.2.1 `supportURI` | Annex I.7(a) | Support URL |
| `public_body` | Table 10; B.2.1 `isPSB` | Annex I.11 | Public sector body |
| `dpa` | Table 7; B.2.1 `supervisoryAuthority` | Annex IV.3(g) | DPA info |

### Technical Fields

| Field | ETSI Reference | Description |
|-------|----------------|-------------|
| `policy_id` | Table 7, clause 6.1.3 | WRPRC policy OID: `0.4.0.19475.3.1` |
| `iat` | Table 7 | Issuance timestamp |
| `exp` | Table 10, GEN-5.2.4-08 | Expiration (max 12 months) |
| `status` | Table 7, GEN-6.2.6.1-04 | Status list reference |

---

## Example 2: Banking KYC (Multiple Credentials)

```json
{
  "name": "Dutch Bank Customer Onboarding",
  "sub": { "legal_name": "Dutch Bank N.V.", "id": "LEINL-724500VKKSH9QOLTFR81" },
  "country": "NL",
  "registry_uri": "https://wrp-register.nl/api/v1/relying-parties/NL-WRP-00234",
  "service": [
    { "lang": "en-US", "value": "Online banking account opening service" },
    { "lang": "nl-NL", "value": "Online bankrekening openen" }
  ],
  "entitlements": [
    "https://uri.etsi.org/19475/Entitlement/Service_Provider",
    "https://uri.etsi.org/19475/SubEntitlement/psp/psp-as"
  ],
  "purpose": [
    { "lang": "en-US", "value": "Identity verification and KYC check for bank account opening" }
  ],
  "credentials": [
    {
      "format": "dc+sd-jwt",
      "meta": { "vct_values": ["https://credentials.example.eu/pid"] },
      "claims": [
        { "path": ["family_name"] }, { "path": ["given_name"] },
        { "path": ["birth_date"] }, { "path": ["nationality"] },
        { "path": ["resident_address"] }, { "path": ["personal_identifier"] }
      ]
    },
    {
      "format": "dc+sd-jwt",
      "meta": { "vct_values": ["https://credentials.example.eu/address-attestation"] },
      "claims": [
        { "path": ["resident_address"] }, { "path": ["resident_country"] }
      ]
    }
  ],
  "privacy_policy": "https://dutchbank.nl/privacy",
  "dpa": { "uri": "https://autoriteitpersoonsgegevens.nl", "email": "info@autoriteitpersoonsgegevens.nl" },
  "public_body": false,
  "policy_id": ["0.4.0.19475.3.1"],
  "iat": 1704067200,
  "status": { "status_list": { "idx": 89, "uri": "https://status.wrp-register.nl/statuslist/1" } }
}
```

---

## Example 3: With Intermediary

Per ETSI TS 119 475 Table 10 and GEN-5.2.4-09:

```json
{
  "name": "Small Business Verification",
  "sub": { "legal_name": "Small Business GmbH", "id": "VATDE-DE123456789" },
  "country": "DE",
  "entitlements": ["https://uri.etsi.org/19475/Entitlement/Service_Provider"],
  "credentials": [
    {
      "format": "dc+sd-jwt",
      "meta": { "vct_values": ["https://credentials.example.eu/pid"] },
      "claims": [{ "path": ["age_over_18"] }]
    }
  ],
  "act": {
    "sub": {
      "id": "LEIDE-529900INTERMEDIARY01",
      "name": "Verification Services AG"
    }
  },
  "policy_id": ["0.4.0.19475.3.1"],
  "iat": 1704067200,
  "status": { "status_list": { "idx": 567, "uri": "https://status.wrp-register.de/statuslist/2" } }
}
```

| Field | ETSI Reference | CIR 2025/848 | Description |
|-------|----------------|--------------|-------------|
| `act` | Table 10; B.2.1 `usesIntermediary` | Annex I.14 | Intermediary indication |
| `act.sub.id` | Table 10 | Annex I.14 | Intermediary identifier from WRPAC |
| `act.sub.name` | Table 10 | Annex I.14 | Intermediary name from WRPAC |

---

## Example 4: Natural Person (Notary)

```json
{
  "name": "Notaio Marco Rossi",
  "sub": {
    "given_name": "Marco",
    "family_name": "Rossi",
    "id": "TINIT-RSSMRC80A01H501U"
  },
  "country": "IT",
  "registry_uri": "https://wrp-register.gov.it/api/v1/relying-parties/IT-WRP-00890",
  "entitlements": ["https://uri.etsi.org/19475/Entitlement/Service_Provider"],
  "purpose": [
    { "lang": "it-IT", "value": "Identificazione delle parti per atti notarili" }
  ],
  "credentials": [
    {
      "format": "dc+sd-jwt",
      "meta": { "vct_values": ["https://credentials.example.eu/pid"] },
      "claims": [
        { "path": ["family_name"] }, { "path": ["given_name"] },
        { "path": ["birth_date"] }, { "path": ["personal_identifier"] }
      ]
    }
  ],
  "privacy_policy": "https://notaio-rossi.it/privacy",
  "dpa": { "uri": "https://www.garanteprivacy.it", "email": "protocollo@gpdp.it" },
  "public_body": false,
  "policy_id": ["0.4.0.19475.3.1"],
  "iat": 1704067200,
  "status": { "status_list": { "idx": 345, "uri": "https://status.wrp-register.gov.it/statuslist/1" } }
}
```

| Field | ETSI Reference | Description |
|-------|----------------|-------------|
| `sub.given_name` | Table 7; B.2.4 `givenName` | First name (natural person) |
| `sub.family_name` | Table 7; B.2.4 `familyName` | Family name (natural person) |
| `sub.id` | GEN-5.1.5-01, Table 4 | Natural person identifier |

---

## Entitlements and Sub-Entitlements

Per ETSI TS 119 475 Annex A:

| Entitlement | URI | OID | Reference |
|-------------|-----|-----|-----------|
| Service_Provider | `https://uri.etsi.org/19475/Entitlement/Service_Provider` | `0.4.0.19475.1.1` | A.2.1 |

### Payment Service Provider Sub-Entitlements (A.3.1)

| Sub-Entitlement | URI | Reference |
|-----------------|-----|-----------|
| Account Servicing PSP | `https://uri.etsi.org/19475/SubEntitlement/psp/psp-as` | A.3.1 |
| Payment Initiation SP | `https://uri.etsi.org/19475/SubEntitlement/psp/psp-pi` | A.3.1 |
| Account Information SP | `https://uri.etsi.org/19475/SubEntitlement/psp/psp-ai` | A.3.1 |
| Card-based Payment PSP | `https://uri.etsi.org/19475/SubEntitlement/psp/psp-ic` | A.3.1 |

---

## Mapping to National Register (Annex B)

| Annex B Class | Attribute | WRPRC Field | CIR 2025/848 |
|---------------|-----------|-------------|--------------|
| B.2.1 WalletRelyingParty | `tradeName` | `name` | Annex I.2 |
| B.2.1 WalletRelyingParty | `registryURI` | `registry_uri` | Article 3(5) |
| B.2.1 WalletRelyingParty | `entitlement` | `entitlements` | Annex I.12 |
| B.2.1 WalletRelyingParty | `supportURI` | `support_uri` | Annex I.7(a) |
| B.2.1 WalletRelyingParty | `isPSB` | `public_body` | Annex I.11 |
| B.2.1 WalletRelyingParty | `usesIntermediary` | `act` | Annex I.14 |
| B.2.2 LegalEntity | `country` | `country` | Annex I.6 |
| B.2.2 LegalEntity | `infoURI` | `info_uri` | Annex I.5 |
| B.2.3 LegalPerson | `legalName` | `sub.legal_name` | Annex I.1 |
| B.2.4 NaturalPerson | `givenName` | `sub.given_name` | Annex I.1 |
| B.2.4 NaturalPerson | `familyName` | `sub.family_name` | Annex I.1 |
| B.2.5 Identifier | `identifier` | `sub.id` | Annex I.3 |
| B.2.7 IntendedUse | `purpose` | `purpose` | Article 8.2(b) |
| B.2.7 IntendedUse | `credential` | `credentials` | Annex I.9 |
| B.2.7 IntendedUse | `privacyPolicy` | `privacy_policy` | Article 8.2(g) |
| B.2.9 Credential | `format`, `meta`, `claim` | `credentials[].*` | Annex I.9 |

---

## WRPRC Policy OID

Per ETSI TS 119 475 clause 6.1.3:

```
wrprc OBJECT IDENTIFIER ::=
{ itu-t(0) identified-organization(4) etsi(0) eudiwrpa(19475) policy-identifiers(3) wrprc(1) }

OID: 0.4.0.19475.3.1
```

---

## Use Cases

Relying Party Registration Certificates are used to:

1. **Declare intended use** - Purpose for requesting attributes (CIR 2025/848 Article 8.2(b));
2. **Define requested credentials** - Attestations and claims needed (Annex I.9);
3. **Support data minimization** - Enforce attribute access policies;
4. **Enable transparency** - Allow users to understand data requests;
5. **Facilitate over-asking detection** - Detect requests beyond declared scope;
6. **Support intermediary chains** - Identify intermediated requests (Annex I.14).
