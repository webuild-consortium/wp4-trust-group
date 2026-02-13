# PID Provider Access Certificate Example

## Overview

This example demonstrates a Wallet-Relying Party Access Certificate (WRPAC) for a **PID Provider** (Person Identification Data Provider) - an entity authorized to issue person identification data to EUDIW users.

## Normative References

| Reference | Document |
|-----------|----------|
| ETSI TS 119 411-8 | Policy and security requirements for Trust Service Providers issuing certificates; Part 8: Access Certificate Policy for EUDI Wallet Relying Parties |
| ETSI TS 119 475 | Relying party attributes supporting EUDI Wallet user's authorization decisions |
| ETSI EN 319 412-1 | Certificate Profiles; Part 1: Overview and common data structures |
| ETSI EN 319 412-3 | Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons |
| ETSI EN 319 411-1 | Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements |
| CIR (EU) 2025/848 | Commission Implementing Regulation on the registration of wallet-relying parties |
| IETF RFC 5280 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |
| ITU-T X.520 | Information technology - Open Systems Interconnection - The Directory: Selected attribute types |

---

## X.509 Certificate Structure

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 01:23:45:67:89:AB:CD:EF
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: 
            C = DE
            O = German Trust Services GmbH
            CN = German EUDI Wallet CA
        Validity:
            Not Before: Jan 15 00:00:00 2025 GMT
            Not After : Jan 15 00:00:00 2027 GMT
        Subject:
            C = DE
            O = Bundesdruckerei GmbH
            organizationIdentifier = NTRDEU-HRB12345
            CN = German PID Issuer Service
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
            Public-Key: (384 bit)
            ASN1 OID: secp384r1
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Extended Key Usage:
                id-kp-clientAuth
            X509v3 Subject Alternative Name:
                URI: https://pid.bdr.de
                email: pid-support@bdr.de
                otherName: id-at-telephoneNumber: +49 30 2598 0
            X509v3 Certificate Policies:
                Policy: 0.4.0.194118.1.2
                    CPS: https://pki.bdr.de/cps
            Authority Information Access:
                OCSP - URI: http://ocsp.bdr.de
                CA Issuers - URI: http://ca.bdr.de/ca.crt
            X509v3 CRL Distribution Points:
                Full Name:
                    URI: http://crl.bdr.de/wallet-ca.crl
    Signature Algorithm: ecdsa-with-SHA384
    Signature Value: [signature bytes]
```

---

## Certificate Fields with ETSI References

### Subject Distinguished Name

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `countryName (C)` | `DE` | ETSI EN 319 412-3 clause 4.2.1 | ISO 3166-1 alpha-2 country code |
| `organizationName (O)` | `Bundesdruckerei GmbH` | ETSI EN 319 412-3 clause 4.2.1; ETSI TS 119 475 Table 1 `legalName` | Legal name as stated in official record |
| `organizationIdentifier` | `NTRDEU-HRB12345` | ETSI EN 319 412-1 clause 5.1.4; ETSI TS 119 411-8 GEN-6.6.1-05; ETSI TS 119 475 clause 5.1.3 | Semantic identifier: NTR (National Trade Register) + Country + ID |
| `commonName (CN)` | `German PID Issuer Service` | ETSI EN 319 412-3 clause 4.2.1; ETSI TS 119 411-8 GEN-6.1.1-04; ETSI TS 119 475 Table 1 `tradeName` | User-friendly trade/service name |

### Subject Alternative Name (SAN)

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `uniformResourceIdentifier` | `https://pid.bdr.de` | ETSI TS 119 411-8 GEN-6.6.1-07; IETF RFC 5280 clause 4.2.1.6; CIR 2025/848 Annex I.7(a); ETSI TS 119 475 Table 1 `supportURI` | Support/contact website URL |
| `rfc822Name` | `pid-support@bdr.de` | ETSI TS 119 411-8 GEN-6.6.1-07; IETF RFC 5280 clause 4.2.1.6; CIR 2025/848 Annex I.7(c); ETSI TS 119 475 Table 1 `email` | Contact email address |
| `otherName (telephoneNumber)` | `+49 30 2598 0` | ETSI TS 119 411-8 GEN-6.6.1-07; ITU-T X.520 clause 6.7.1; CIR 2025/848 Annex I.7(b); ETSI TS 119 475 Table 1 `phone` | Contact phone (OID: 2.5.4.20) |

### Certificate Policies

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `policyIdentifier` | `0.4.0.194118.1.2` | ETSI TS 119 411-8 clause 5.3 (NCP-l-eudiwrp) | Normalized Certificate Policy for legal persons |
| `cpsURI` | `https://pki.bdr.de/cps` | ETSI TS 119 411-8 GEN-6.6.1-06; ETSI EN 319 411-1 clause 6.6.1 | URL to Certificate Practice Statement |

### Key Usage and Extended Key Usage

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `keyUsage` | `digitalSignature` | ETSI EN 319 411-1 clause 6.6.1 | Critical extension for signing |
| `extendedKeyUsage` | `id-kp-clientAuth` | ETSI EN 319 411-1 clause 6.6.1 | Client authentication purpose |

---

## Organizational Identifier Formats

Per ETSI EN 319 412-1 clause 5.1.4 and ETSI TS 119 475 clause 5.1.3, the following identifier types are supported:

| Type URI (ETSI TS 119 475 B.2.5) | Semantic Prefix | Description | Reference |
|----------------------------------|-----------------|-------------|-----------|
| `http://data.europa.eu/eudi/id/EUID` | `NTR` | European Unique Identifier | CIR 2020/2244, CIR 2021/1042 |
| `http://data.europa.eu/eudi/id/LEI` | `LEI` | Legal Entity Identifier | CIR 2022/1860, ISO 17442-1 |
| `http://data.europa.eu/eudi/id/VATIN` | `VAT` | VAT Identification Number | Council Directive 2006/112/EC |
| `http://data.europa.eu/eudi/id/EORI-No` | `EOR` | Economic Operator Registration ID | CIR 1352/2013 |
| `http://data.europa.eu/eudi/id/TIN` | `VAT` | Taxpayer Identification Number | - |
| `http://data.europa.eu/eudi/id/Excise` | `EXC` | Excise Number | Council Regulation 389/2012 |

---

## Certificate Policy OIDs

Per ETSI TS 119 411-8 clause 5.3:

| Policy | OID | Description |
|--------|-----|-------------|
| NCP-n-eudiwrp | `0.4.0.194118.1.1` | Normalized, Natural Person |
| **NCP-l-eudiwrp** | **`0.4.0.194118.1.2`** | **Normalized, Legal Person** (used in this example) |
| QCP-n-eudiwrp | `0.4.0.194118.1.3` | Qualified, Natural Person |
| QCP-l-eudiwrp | `0.4.0.194118.1.4` | Qualified, Legal Person |

---

## Entitlement

Per ETSI TS 119 475 clause 4.2 and Annex A.2.5:

| Attribute | Value |
|-----------|-------|
| Entitlement | `PID_Provider` |
| Description | Provider of person identification data |
| OID | `0.4.0.19475.1.5` (id-etsi-wrpa-entitlement 5) |
| URI | `https://uri.etsi.org/19475/Entitlement/PID_Provider` |
| CIR Reference | CIR 2025/848 Annex I.12 |

---

## OpenSSL Commands

### Generate Key Pair
```bash
# In this example a P-384 ECDSA key will be used
openssl ecparam -name secp384r1 -genkey -noout -out pid_provider.key
```

### Generate CSR
```bash
openssl req -new -key pid_provider.key -out pid_provider.csr \
  -subj "/C=DE/O=Bundesdruckerei GmbH/organizationIdentifier=NTRDEU-HRB12345/CN=German PID Issuer Service"
```

### Extensions Configuration (pid_provider_ext.cnf)
```ini
# Per ETSI TS 119 411-8 and ETSI EN 319 411-1
[v3_wrpac]
keyUsage = critical, digitalSignature
extendedKeyUsage = clientAuth
subjectAltName = @alt_names
certificatePolicies = @policy_section
authorityInfoAccess = OCSP;URI:http://ocsp.bdr.de,caIssuers;URI:http://ca.bdr.de/ca.crt
crlDistributionPoints = URI:http://crl.bdr.de/wallet-ca.crl

# Per ETSI TS 119 411-8 GEN-6.6.1-07 and CIR 2025/848 Annex I.7
[alt_names]
URI.1 = https://pid.bdr.de
email.1 = pid-support@bdr.de

# Per ETSI TS 119 411-8 clause 5.3 and GEN-6.6.1-06
[policy_section]
policyIdentifier = 0.4.0.194118.1.2
CPS.1 = https://pki.bdr.de/cps
```

---

## Mapping to National Register

Per ETSI TS 119 475 clause 5.1.2 and ETSI TS 119 411-8 GEN-6.6.1-10, certificate attributes derive from the national WRP register:

| Register Attribute (ETSI TS 119 475 Annex B) | Certificate Field | CIR 2025/848 Annex |
|----------------------------------------------|-------------------|-------------------|
| `legalName` (B.2.3 LegalPerson) | `organizationName` | Annex I.1 |
| `tradeName` (B.2.1 WalletRelyingParty) | `commonName` | Annex I.2 |
| `identifier` (B.2.5 Identifier) | `organizationIdentifier` | Annex I.3 |
| `country` (B.2.2 LegalEntity) | `countryName` | Annex I.6 |
| `supportURI` (B.2.1 WalletRelyingParty) | SAN URI | Annex I.7(a) |
| `email` (B.2.2 LegalEntity) | SAN rfc822Name | Annex I.7(c) |
| `phone` (B.2.2 LegalEntity) | SAN telephoneNumber | Annex I.7(b) |

---

## Use Case

The PID Provider uses this certificate to:

1. **Authenticate** to EUDIW when issuing Person Identification Data (per CIR 2025/848 Article 7);
2. **Sign** PID issuance requests to prove authenticity;
3. **Establish trust** with the wallet ecosystem via the national trusted list.
