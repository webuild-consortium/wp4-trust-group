# Relying Party Access Certificate Example

## Overview

This example demonstrates Wallet-Relying Party Access Certificates (WRPAC) for **Service Providers** - general relying parties that request attributes from EUDIW users for service provision.

## Normative References

| Reference | Document |
|-----------|----------|
| ETSI TS 119 411-8 | Policy and security requirements for Trust Service Providers issuing certificates; Part 8: Access Certificate Policy for EUDI Wallet Relying Parties |
| ETSI TS 119 475 | Relying party attributes supporting EUDI Wallet user's authorization decisions |
| ETSI EN 319 412-1 | Certificate Profiles; Part 1: Overview and common data structures |
| ETSI EN 319 412-2 | Certificate Profiles; Part 2: Certificate profile for certificates issued to natural persons |
| ETSI EN 319 412-3 | Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons |
| ETSI EN 319 411-1 | Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements |
| ETSI EN 319 411-2 | Policy and security requirements for Trust Service Providers issuing certificates; Part 2: Requirements for trust service providers issuing EU qualified certificates |
| CIR (EU) 2025/848 | Commission Implementing Regulation on the registration of wallet-relying parties |
| IETF RFC 5280 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |
| ITU-T X.520 | Information technology - Open Systems Interconnection - The Directory: Selected attribute types |

---

## Example 1: E-Commerce Service Provider (Legal Person)

### X.509 Certificate Structure

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: DE:AD:BE:EF:CA:FE:BA:BE
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
            O = Online Shop AG
            organizationIdentifier = LEIXG-529900T8BM49AURSDO55
            CN = Online Shop Identity Verification
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
            Public-Key: (384 bit)
            ASN1 OID: secp384r1
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Extended Key Usage:
                id-kp-clientAuth
            X509v3 Authority Key Identifier: 
                keyid:DE:AD:BE:EF:01:23:45:67:89:AB:CD:EF:01:23:45:67:89:AB:CD:EF
            X509v3 Subject Alternative Name:
                URI: https://shop.example.de/support
                email: identity@shop.example.de
                otherName: id-at-telephoneNumber: +49 89 1234567
            X509v3 Certificate Policies:
                Policy: 0.4.0.194118.1.2
                    CPS: https://pki.shop.example.de/cps
            Authority Information Access:
                OCSP - URI: http://ocsp.german-tsp.de
                CA Issuers - URI: http://ca.german-tsp.de/wallet-ca.crt
            X509v3 CRL Distribution Points:
                Full Name:
                    URI: http://crl.german-tsp.de/wallet-ca.crl
    Signature Algorithm: ecdsa-with-SHA384
    Signature Value: [signature bytes]
```

### Certificate Fields with ETSI References

#### Subject Distinguished Name (Legal Person)

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `countryName (C)` | `DE` | ETSI EN 319 412-3 clause 4.2.1 | Annex I.6 | ISO 3166-1 alpha-2 country code |
| `organizationName (O)` | `Online Shop AG` | ETSI EN 319 412-3 clause 4.2.1; ETSI TS 119 475 Table 1 `legalName` | Annex I.1 | Legal name from official record |
| `organizationIdentifier` | `LEIXG-529900T8BM49AURSDO55` | ETSI EN 319 412-1 clause 5.1.4; ETSI TS 119 411-8 GEN-6.6.1-05; ETSI TS 119 475 Table 2 | Annex I.3 | LEI + Country + LEI Number |
| `commonName (CN)` | `Online Shop Identity Verification` | ETSI EN 319 412-3 clause 4.2.1; ETSI TS 119 411-8 GEN-6.1.1-04; ETSI TS 119 475 Table 1 `tradeName` | Annex I.2 | User-friendly service name |

#### Subject Alternative Name (SAN)

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `uniformResourceIdentifier` | `https://shop.example.de/support` | ETSI TS 119 411-8 GEN-6.6.1-07; IETF RFC 5280 clause 4.2.1.6; ETSI TS 119 475 Table 1 `supportURI` | Annex I.7(a) | Support URL |
| `rfc822Name` | `identity@shop.example.de` | ETSI TS 119 411-8 GEN-6.6.1-07; IETF RFC 5280 clause 4.2.1.6; ETSI TS 119 475 Table 1 `email` | Annex I.7(c) | Contact email |
| `otherName (telephoneNumber)` | `+49 89 1234567` | ETSI TS 119 411-8 GEN-6.6.1-07; ITU-T X.520 clause 6.7.1 (OID 2.5.4.20); ETSI TS 119 475 Table 1 `phone` | Annex I.7(b) | Contact phone |

#### Certificate Policies

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `policyIdentifier` | `0.4.0.194118.1.2` | ETSI TS 119 411-8 clause 5.3 (NCP-l-eudiwrp) | Normalized Certificate Policy for legal persons |
| `cpsURI` | `https://pki.shop.example.de/cps` | ETSI TS 119 411-8 GEN-6.6.1-06 | CPS URL |

---

## Example 2: Financial Services Provider (Qualified Certificate)

### X.509 Certificate Structure

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 12:34:56:78:9A:BC:DE:F0
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: 
            C = NL
            O = Dutch Qualified Trust Services B.V.
            CN = Dutch EUDI Wallet Qualified CA
        Validity:
            Not Before: Feb 01 00:00:00 2025 GMT
            Not After : Feb 01 00:00:00 2027 GMT
        Subject:
            C = NL
            O = Dutch Bank N.V.
            organizationIdentifier = LEIXG-724500VKKSH9QOLTFR81
            CN = Dutch Bank Customer Onboarding
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
            Public-Key: (384 bit)
            ASN1 OID: secp384r1
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Extended Key Usage:
                id-kp-clientAuth
            X509v3 Authority Key Identifier: 
                keyid:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77
            X509v3 Subject Alternative Name:
                URI: https://onboarding.dutchbank.nl
                email: kyc@dutchbank.nl
                otherName: id-at-telephoneNumber: +31 20 123 4567
            X509v3 Certificate Policies:
                Policy: 0.4.0.194118.1.4
                    CPS: https://pki.dutchbank.nl/cps
            X509v3 QCStatements:
                id-etsi-qcs-QcCompliance
                id-etsi-qcs-QcType: id-etsi-qct-eseal
            Authority Information Access:
                OCSP - URI: http://ocsp.dutch-qtsp.nl
            X509v3 CRL Distribution Points:
                Full Name:
                    URI: http://crl.dutch-qtsp.nl/wallet-ca.crl
    Signature Algorithm: ecdsa-with-SHA384
    Signature Value: [signature bytes]
```

### Certificate Fields with ETSI References

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `organizationIdentifier` | `LEIXG-724500VKKSH9QOLTFR81` | ETSI EN 319 412-1 clause 5.1.4; ETSI TS 119 475 Table 2 | LEI for financial institution |
| `policyIdentifier` | `0.4.0.194118.1.4` | ETSI TS 119 411-8 clause 5.3 (QCP-l-eudiwrp); ETSI TS 119 411-8 OVR-5.1-03 | Qualified Certificate Policy |
| `QcCompliance` | Present | ETSI EN 319 411-2 clause 6.6.1; ETSI EN 319 412-5 | EU qualified certificate indicator |
| `QcType` | `id-etsi-qct-eseal` | ETSI EN 319 411-2 clause 6.6.1 | Qualified electronic seal |

---

## Example 3: Natural Person Relying Party (Notary)

### X.509 Certificate Structure

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 01:02:03:04:05:06:07:08
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: 
            C = IT
            O = Italian Trust Services S.p.A.
            CN = Italian EUDI Wallet CA
        Validity:
            Not Before: Apr 01 00:00:00 2025 GMT
            Not After : Apr 01 00:00:00 2027 GMT
        Subject:
            C = IT
            G = Marco
            SN = Rossi
            serialNumber = TINIT-RSSMRC80A01H501U
            CN = Marco Rossi Notary Services
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
            Public-Key: (384 bit)
            ASN1 OID: secp384r1
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Extended Key Usage:
                id-kp-clientAuth
            X509v3 Authority Key Identifier:
                keyid:99:88:77:66:55:44:33:22:11:00:FF:EE:DD:CC:BB:AA:00:11:22:33
            X509v3 Subject Alternative Name:
                URI: https://notaio-rossi.it
                email: marco.rossi@notaio.it
            X509v3 Certificate Policies:
                Policy: 0.4.0.194118.1.1
                    CPS: https://pki.italian-tsp.it/cps
            Authority Information Access:
                OCSP - URI: http://ocsp.italian-tsp.it
            X509v3 CRL Distribution Points:
                Full Name:
                    URI: http://crl.italian-tsp.it/wallet-ca.crl
    Signature Algorithm: ecdsa-with-SHA384
    Signature Value: [signature bytes]
```

### Certificate Fields with ETSI References (Natural Person)

| Field | Value | ETSI Reference | CIR 2025/848 | Description |
|-------|-------|----------------|--------------|-------------|
| `givenName (G)` | `Marco` | ETSI EN 319 412-2 clause 4.2.4; ETSI TS 119 475 Table 3 `givenName` | Annex I.1 | First name |
| `surname (SN)` | `Rossi` | ETSI EN 319 412-2 clause 4.2.4; ETSI TS 119 475 Table 3 `familyName` | Annex I.1 | Family name |
| `serialNumber` | `TINIT-RSSMRC80A01H501U` | ETSI EN 319 412-1 clause 5.1.3; ETSI TS 119 475 clause 5.1.5 | Annex I.3 | TIN + Country + Tax ID |
| `commonName (CN)` | `Marco Rossi Notary Services` | ETSI EN 319 412-2 clause 4.2.4; ETSI TS 119 475 Table 3 `tradeName` | Annex I.2 | User-friendly service name |
| `policyIdentifier` | `0.4.0.194118.1.1` | ETSI TS 119 411-8 clause 5.3 (NCP-n-eudiwrp) | - | Normalized policy for natural persons |

---

## Organizational Identifier Formats

Per ETSI EN 319 412-1 clause 5.1.4 and ETSI TS 119 475 clause 5.1.3:

### Legal Person Identifiers (Table 2)

| Type URI (ETSI TS 119 475 B.2.5) | Semantic Prefix | ETSI EN 319 412-1 Reference | EU Regulation |
|----------------------------------|-----------------|----------------------------|---------------|
| `http://data.europa.eu/eudi/id/EUID` | `NTR` | LEG-5.1.4-07 | CIR 2020/2244, CIR 2021/1042 |
| `http://data.europa.eu/eudi/id/LEI` | `LEI` | clause 5.1.4 | CIR 2022/1860, ISO 17442-1 |
| `http://data.europa.eu/eudi/id/VATIN` | `VAT` | clause 5.1.4 | Directive 2006/112/EC |
| `http://data.europa.eu/eudi/id/EORI-No` | `EOR` | clause 5.1.4 (future) | CIR 1352/2013 |
| `http://data.europa.eu/eudi/id/TIN` | `VAT` | clause 5.1.4 | - |
| `http://data.europa.eu/eudi/id/Excise` | `EXC` | clause 5.1.4 (future) | Regulation 389/2012 |

### Natural Person Identifiers (Table 4)

| Type URI (ETSI TS 119 475 B.2.5) | Semantic Prefix | ETSI EN 319 412-1 Reference | Description |
|----------------------------------|-----------------|----------------------------|-------------|
| `http://data.europa.eu/eudi/id/VATIN` | `TIN` | NAT-5.1.3-03 | VAT ID for natural persons |
| `http://data.europa.eu/eudi/id/TIN` | `TIN` | NAT-5.1.3-03 | Taxpayer ID |
| National schemes | Various | NAT-5.1.3-03 point (7) | National identification schemes |

---

## Certificate Policy OIDs

Per ETSI TS 119 411-8 clause 5.3:

| Policy | OID | Description | Base Requirements |
|--------|-----|-------------|-------------------|
| **NCP-n-eudiwrp** | **`0.4.0.194118.1.1`** | **Normalized, Natural Person** | ETSI EN 319 411-1 |
| **NCP-l-eudiwrp** | **`0.4.0.194118.1.2`** | **Normalized, Legal Person** | ETSI EN 319 411-1 |
| QCP-n-eudiwrp | `0.4.0.194118.1.3` | Qualified, Natural Person | ETSI EN 319 411-2 |
| **QCP-l-eudiwrp** | **`0.4.0.194118.1.4`** | **Qualified, Legal Person** | ETSI EN 319 411-2 |

---

## Entitlement

Per ETSI TS 119 475 clause 4.2 and Annex A.2.1:

| Attribute | Value | ETSI Reference |
|-----------|-------|----------------|
| Entitlement | `Service_Provider` | ETSI TS 119 475 Annex A.2.1 |
| Description | General service provider | CIR 2025/848 Annex I.12 |
| OID | `0.4.0.19475.1.1` | ETSI TS 119 475 Annex A.2.1 |
| URI | `https://uri.etsi.org/19475/Entitlement/Service_Provider` | ETSI TS 119 475 Annex A.2.1 |

---

## Mapping to National Register

Per ETSI TS 119 475 clause 5.1.2 and ETSI TS 119 411-8 GEN-6.6.1-10:

### Legal Person (Table 1)

| Register Attribute (Annex B) | Certificate Field | CIR 2025/848 |
|------------------------------|-------------------|--------------|
| `legalName` (B.2.3 LegalPerson) | `organizationName` | Annex I.1 |
| `tradeName` (B.2.1 WalletRelyingParty) | `commonName` | Annex I.2 |
| `identifier` (B.2.5 Identifier) | `organizationIdentifier` | Annex I.3 |
| `country` (B.2.2 LegalEntity) | `countryName` | Annex I.6 |
| `supportURI` (B.2.1 WalletRelyingParty) | SAN URI | Annex I.7(a) |
| `email` (B.2.2 LegalEntity) | SAN rfc822Name | Annex I.7(c) |
| `phone` (B.2.2 LegalEntity) | SAN telephoneNumber | Annex I.7(b) |

### Natural Person (Table 3)

| Register Attribute (Annex B) | Certificate Field | CIR 2025/848 |
|------------------------------|-------------------|--------------|
| `givenName` (B.2.4 NaturalPerson) | `givenName` | Annex I.1 |
| `familyName` (B.2.4 NaturalPerson) | `surname` | Annex I.1 |
| `tradeName` (B.2.1 WalletRelyingParty) | `commonName` | Annex I.2 |
| `identifier` (B.2.5 Identifier) | `serialNumber` | Annex I.3 |
| `country` (B.2.2 LegalEntity) | `countryName` | Annex I.6 |
| `supportURI` (B.2.1 WalletRelyingParty) | SAN URI | Annex I.7(a) |
| `email` (B.2.2 LegalEntity) | SAN rfc822Name | Annex I.7(c) |
| `phone` (B.2.2 LegalEntity) | SAN telephoneNumber | Annex I.7(b) |

---

## OpenSSL Commands

### Generate Key Pair
```bash
# In this example a P-384 ECDSA key will be used
openssl ecparam -name secp384r1 -genkey -noout -out relying_party.key
```

### Generate CSR (Legal Person)
```bash
# Per ETSI EN 319 412-3 clause 4.2.1
openssl req -new -key relying_party.key -out relying_party.csr \
  -subj "/C=DE/O=Online Shop AG/organizationIdentifier=LEIXG-529900T8BM49AURSDO55/CN=Online Shop Identity Verification"
```

### Generate CSR (Natural Person)
```bash
# Per ETSI EN 319 412-2 clause 4.2.4
openssl req -new -key relying_party.key -out relying_party.csr \
  -subj "/C=IT/GN=Marco/SN=Rossi/serialNumber=TINIT-RSSMRC80A01H501U/CN=Marco Rossi Notary Services"
```

### Extensions Configuration (rp_ext.cnf)
```ini
# Per ETSI TS 119 411-8 and ETSI EN 319 411-1
[v3_wrpac]
# Per ETSI EN 319 411-1 clause 6.6.1
keyUsage = critical, digitalSignature
extendedKeyUsage = clientAuth

# Per ETSI TS 119 411-8 GEN-6.6.1-07 and CIR 2025/848 Annex I.7
subjectAltName = @alt_names

# Per ETSI TS 119 411-8 clause 5.3 and GEN-6.6.1-06
certificatePolicies = @policy_section

authorityInfoAccess = OCSP;URI:http://ocsp.tsp.example
crlDistributionPoints = URI:http://crl.tsp.example/wallet-ca.crl

# Per ETSI TS 119 411-8 GEN-6.6.1-07
[alt_names]
URI.1 = https://service.example.com/support
email.1 = support@service.example.com

[policy_section]
# NCP-l-eudiwrp per ETSI TS 119 411-8 clause 5.3
policyIdentifier = 0.4.0.194118.1.2
CPS.1 = https://pki.service.example.com/cps
```

---

## Use Cases

Relying Party Access Certificates are used to:

1. **Authenticate** to EUDIW when requesting attributes (per CIR 2025/848 Article 7);
2. **Sign** attribute requests to prove authenticity;
3. **Establish trust** with wallet users via national trusted lists (per eIDAS Article 22);
4. **Enable verification** of the relying party's identity by the wallet.
