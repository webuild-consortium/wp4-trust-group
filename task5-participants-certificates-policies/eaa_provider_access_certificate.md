# Attestation/EAA Provider Access Certificate Example

## Overview

This example demonstrates Wallet-Relying Party Access Certificates (WRPAC) for **Electronic Attestation of Attributes (EAA) Providers** - entities authorized to issue electronic attestations of attributes to EUDIW users.

## Normative References

| Reference | Document |
|-----------|----------|
| ETSI TS 119 411-8 | Policy and security requirements for Trust Service Providers issuing certificates; Part 8: Access Certificate Policy for EUDI Wallet Relying Parties |
| ETSI TS 119 475 | Relying party attributes supporting EUDI Wallet user's authorization decisions |
| ETSI EN 319 412-1 | Certificate Profiles; Part 1: Overview and common data structures |
| ETSI EN 319 412-3 | Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons |
| ETSI EN 319 411-1 | Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements |
| ETSI EN 319 411-2 | Policy and security requirements for Trust Service Providers issuing certificates; Part 2: Requirements for trust service providers issuing EU qualified certificates |
| CIR (EU) 2025/848 | Commission Implementing Regulation on the registration of wallet-relying parties |
| IETF RFC 5280 | Internet X.509 Public Key Infrastructure Certificate and CRL Profile |
| ITU-T X.520 | Information technology - Open Systems Interconnection - The Directory: Selected attribute types |

---

## Example 1: Qualified EAA Provider (QEAA)

### X.509 Certificate Structure

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 11:22:33:44:55:66:77:88
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: 
            C = ES
            O = Spanish Qualified Trust Services S.A.
            CN = Spanish EUDI Wallet Qualified CA
        Validity:
            Not Before: Mar 01 00:00:00 2025 GMT
            Not After : Mar 01 00:00:00 2027 GMT
        Subject:
            C = ES
            O = Ministerio del Interior
            organizationIdentifier = VATES-S2800001J
            CN = Spanish Driving License Attestation Service
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
                URI: https://dgt.es/attestations
                email: attestations@dgt.es
                otherName: id-at-telephoneNumber: +34 91 301 5000
            X509v3 Certificate Policies:
                Policy: 0.4.0.194118.1.4
                    CPS: https://pki.dgt.es/cps
            X509v3 QCStatements:
                id-etsi-qcs-QcCompliance
                id-etsi-qcs-QcType: id-etsi-qct-eseal
            Authority Information Access:
                OCSP - URI: http://ocsp.dgt.es
                CA Issuers - URI: http://ca.dgt.es/ca.crt
            X509v3 CRL Distribution Points:
                Full Name:
                    URI: http://crl.dgt.es/wallet-ca.crl
    Signature Algorithm: ecdsa-with-SHA384
    Signature Value: [signature bytes]
```

### Certificate Fields with ETSI References

#### Subject Distinguished Name

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `countryName (C)` | `ES` | ETSI EN 319 412-3 clause 4.2.1 | ISO 3166-1 alpha-2 country code |
| `organizationName (O)` | `Ministerio del Interior` | ETSI EN 319 412-3 clause 4.2.1; ETSI TS 119 475 Table 1 `legalName` | Legal name from official record |
| `organizationIdentifier` | `VATES-S2800001J` | ETSI EN 319 412-1 clause 5.1.4; ETSI TS 119 411-8 GEN-6.6.1-05; ETSI TS 119 475 Table 2 | VAT + Country + VAT Number |
| `commonName (CN)` | `Spanish Driving License Attestation Service` | ETSI EN 319 412-3 clause 4.2.1; ETSI TS 119 411-8 GEN-6.1.1-04; ETSI TS 119 475 Table 1 `tradeName` | User-friendly service name |

#### Subject Alternative Name (SAN)

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `uniformResourceIdentifier` | `https://dgt.es/attestations` | ETSI TS 119 411-8 GEN-6.6.1-07; IETF RFC 5280 clause 4.2.1.6; CIR 2025/848 Annex I.7(a) | Support URL |
| `rfc822Name` | `attestations@dgt.es` | ETSI TS 119 411-8 GEN-6.6.1-07; IETF RFC 5280 clause 4.2.1.6; CIR 2025/848 Annex I.7(c) | Contact email |
| `otherName (telephoneNumber)` | `+34 91 301 5000` | ETSI TS 119 411-8 GEN-6.6.1-07; ITU-T X.520 clause 6.7.1 (OID 2.5.4.20); CIR 2025/848 Annex I.7(b) | Contact phone |

#### Certificate Policies and QCStatements

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `policyIdentifier` | `0.4.0.194118.1.4` | ETSI TS 119 411-8 clause 5.3 (QCP-l-eudiwrp) | Qualified Certificate Policy for legal persons |
| `cpsURI` | `https://pki.dgt.es/cps` | ETSI TS 119 411-8 GEN-6.6.1-06 | CPS URL |
| `QcCompliance` | Present | ETSI EN 319 411-2 clause 6.6.1; ETSI EN 319 412-5 | Indicates EU qualified certificate |
| `QcType` | `id-etsi-qct-eseal` | ETSI EN 319 411-2 clause 6.6.1; ETSI EN 319 412-5 | Qualified electronic seal |

#### Entitlement

| Attribute | Value | ETSI Reference |
|-----------|-------|----------------|
| Entitlement | `QEAA_Provider` | ETSI TS 119 475 clause 4.2, Annex A.2.2 |
| Description | Qualified trust service provider issuing qualified electronic attestations of attributes | CIR 2025/848 Annex I.12 |
| OID | `0.4.0.19475.1.2` | ETSI TS 119 475 Annex A.2.2 |
| URI | `https://uri.etsi.org/19475/Entitlement/QEAA_Provider` | ETSI TS 119 475 Annex A.2.2 |

---

## Example 2: Non-Qualified EAA Provider

### X.509 Certificate Structure

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: AA:BB:CC:DD:EE:FF:00:11
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: 
            C = NL
            O = Dutch Trust Services B.V.
            CN = Dutch EUDI Wallet CA
        Validity:
            Not Before: Feb 15 00:00:00 2025 GMT
            Not After : Feb 15 00:00:00 2027 GMT
        Subject:
            C = NL
            O = University of Amsterdam
            organizationIdentifier = NTRNLD-KVK34567890
            CN = UvA Student Credential Service
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
                URI: https://credentials.uva.nl
                email: credentials@uva.nl
            X509v3 Certificate Policies:
                Policy: 0.4.0.194118.1.2
                    CPS: https://pki.uva.nl/cps
            Authority Information Access:
                OCSP - URI: http://ocsp.uva.nl
            X509v3 CRL Distribution Points:
                Full Name:
                    URI: http://crl.uva.nl/wallet-ca.crl
    Signature Algorithm: ecdsa-with-SHA384
    Signature Value: [signature bytes]
```

### Certificate Fields with ETSI References

| Field | Value | ETSI Reference | Description |
|-------|-------|----------------|-------------|
| `organizationIdentifier` | `NTRNLD-KVK34567890` | ETSI EN 319 412-1 clause 5.1.4; ETSI TS 119 475 Table 2 | NTR (EUID) + Country + Chamber of Commerce ID |
| `policyIdentifier` | `0.4.0.194118.1.2` | ETSI TS 119 411-8 clause 5.3 (NCP-l-eudiwrp) | Normalized Certificate Policy for legal persons |

#### Entitlement

| Attribute | Value | ETSI Reference |
|-----------|-------|----------------|
| Entitlement | `Non_Q_EAA_Provider` | ETSI TS 119 475 clause 4.2, Annex A.2.3 |
| Description | Trust service provider issuing non-qualified electronic attestations of attributes | CIR 2025/848 Annex I.12 |
| OID | `0.4.0.19475.1.3` | ETSI TS 119 475 Annex A.2.3 |
| URI | `https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider` | ETSI TS 119 475 Annex A.2.3 |

---

## Example 3: Public Sector EAA Provider

### X.509 Certificate Structure

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 99:88:77:66:55:44:33:22
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: 
            C = FR
            O = Agence Nationale des Titres Sécurisés
            CN = French EUDI Wallet CA
        Validity:
            Not Before: Apr 01 00:00:00 2025 GMT
            Not After : Apr 01 00:00:00 2027 GMT
        Subject:
            C = FR
            O = Direction Générale des Finances Publiques
            organizationIdentifier = VATFR-12345678901
            CN = French Tax Certificate Service
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
                URI: https://impots.gouv.fr/attestations
                email: attestations@dgfip.finances.gouv.fr
                otherName: id-at-telephoneNumber: +33 1 40 04 04 04
            X509v3 Certificate Policies:
                Policy: 0.4.0.194118.1.2
                    CPS: https://pki.dgfip.finances.gouv.fr/cps
            Authority Information Access:
                OCSP - URI: http://ocsp.dgfip.finances.gouv.fr
            X509v3 CRL Distribution Points:
                Full Name:
                    URI: http://crl.dgfip.finances.gouv.fr/wallet-ca.crl
    Signature Algorithm: ecdsa-with-SHA384
    Signature Value: [signature bytes]
```

#### Entitlement

| Attribute | Value | ETSI Reference |
|-----------|-------|----------------|
| Entitlement | `PUB_EAA_Provider` | ETSI TS 119 475 clause 4.2, Annex A.2.4 |
| Description | Public sector body or its agent issuing electronic attestations of attributes from authentic sources | CIR 2025/848 Annex I.12 |
| OID | `0.4.0.19475.1.4` | ETSI TS 119 475 Annex A.2.4 |
| URI | `https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider` | ETSI TS 119 475 Annex A.2.4 |

---

## Organizational Identifier Formats

Per ETSI EN 319 412-1 clause 5.1.4 and ETSI TS 119 475 clause 5.1.3:

| Type URI (ETSI TS 119 475 B.2.5) | Semantic Prefix | ETSI EN 319 412-1 Reference | EU Regulation |
|----------------------------------|-----------------|----------------------------|---------------|
| `http://data.europa.eu/eudi/id/EUID` | `NTR` | LEG-5.1.4-07 | CIR 2020/2244 |
| `http://data.europa.eu/eudi/id/LEI` | `LEI` | clause 5.1.4 | CIR 2022/1860 |
| `http://data.europa.eu/eudi/id/VATIN` | `VAT` | clause 5.1.4 | Directive 2006/112/EC |
| `http://data.europa.eu/eudi/id/EORI-No` | `EOR` | clause 5.1.4 (future) | CIR 1352/2013 |

---

## Certificate Policy OIDs

Per ETSI TS 119 411-8 clause 5.3:

| Policy | OID | Description | Base Requirements |
|--------|-----|-------------|-------------------|
| NCP-n-eudiwrp | `0.4.0.194118.1.1` | Normalized, Natural Person | ETSI EN 319 411-1 |
| NCP-l-eudiwrp | `0.4.0.194118.1.2` | Normalized, Legal Person | ETSI EN 319 411-1 |
| QCP-n-eudiwrp | `0.4.0.194118.1.3` | Qualified, Natural Person | ETSI EN 319 411-2 |
| **QCP-l-eudiwrp** | **`0.4.0.194118.1.4`** | **Qualified, Legal Person** | **ETSI EN 319 411-2** |

---

## All EAA Provider Entitlements

Per ETSI TS 119 475 Annex A.2 and CIR 2025/848 Annex I.12:

| Entitlement | URI | OID | Description |
|-------------|-----|-----|-------------|
| QEAA_Provider | `https://uri.etsi.org/19475/Entitlement/QEAA_Provider` | `0.4.0.19475.1.2` | Qualified EAA provider |
| Non_Q_EAA_Provider | `https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider` | `0.4.0.19475.1.3` | Non-qualified EAA provider |
| PUB_EAA_Provider | `https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider` | `0.4.0.19475.1.4` | Public sector EAA provider |

---

## Mapping to National Register

Per ETSI TS 119 475 clause 5.1.2 (Table 1) and ETSI TS 119 411-8 GEN-6.6.1-10:

| Register Attribute (ETSI TS 119 475 Annex B) | Certificate Field | CIR 2025/848 Reference |
|----------------------------------------------|-------------------|------------------------|
| `legalName` (B.2.3 LegalPerson) | `organizationName` | Annex I.1 |
| `tradeName` (B.2.1 WalletRelyingParty) | `commonName` | Annex I.2 |
| `identifier` (B.2.5 Identifier) | `organizationIdentifier` | Annex I.3 |
| `country` (B.2.2 LegalEntity) | `countryName` | Annex I.6 |
| `supportURI` (B.2.1 WalletRelyingParty) | SAN URI | Annex I.7(a) |
| `email` (B.2.2 LegalEntity) | SAN rfc822Name | Annex I.7(c) |
| `phone` (B.2.2 LegalEntity) | SAN telephoneNumber | Annex I.7(b) |

---

## OpenSSL Commands

### Generate Key Pair
```bash
openssl ecparam -name secp384r1 -genkey -noout -out eaa_provider.key
```

### Generate CSR
```bash
# Per ETSI EN 319 412-3 clause 4.2.1 subject DN format
openssl req -new -key eaa_provider.key -out eaa_provider.csr \
  -subj "/C=ES/O=Ministerio del Interior/organizationIdentifier=VATES-S2800001J/CN=Spanish Driving License Attestation Service"
```

### Extensions Configuration (eaa_provider_ext.cnf)
```ini
# Per ETSI TS 119 411-8 and ETSI EN 319 411-2
[v3_qeaa_wrpac]
# Per ETSI EN 319 411-1 clause 6.6.1
keyUsage = critical, digitalSignature
extendedKeyUsage = clientAuth

# Per ETSI TS 119 411-8 GEN-6.6.1-07 and CIR 2025/848 Annex I.7
subjectAltName = @alt_names

# Per ETSI TS 119 411-8 clause 5.3 and GEN-6.6.1-06
certificatePolicies = @policy_section

[alt_names]
URI.1 = https://dgt.es/attestations
email.1 = attestations@dgt.es

[policy_section]
# QCP-l-eudiwrp per ETSI TS 119 411-8 clause 5.3
policyIdentifier = 0.4.0.194118.1.4
CPS.1 = https://pki.dgt.es/cps
```

---

## Use Cases

EAA Providers use these certificates to:

1. **Authenticate** to EUDIW when issuing attestations (per CIR 2025/848 Article 7)
2. **Sign** attestation issuance requests to prove authenticity
3. **Establish trust** with the wallet ecosystem via national trusted lists (per eIDAS Article 22)
4. **Prove authorization** to issue specific types of attestations (per entitlements in CIR 2025/848 Annex I.12)
