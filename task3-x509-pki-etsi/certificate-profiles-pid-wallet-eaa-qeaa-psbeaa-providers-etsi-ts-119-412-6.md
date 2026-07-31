# Certificate Profiles for PID, Wallet, EAA, QEAA, and PSBEAA Providers (ETSI TS 119 412-6)

This document describes the content of ETSI TS 119 412-6 (Certificate profile requirements for PID, Wallet Instance Attestation (WIA), Key Attestation (KA), EAA, QEAA, and PuB-EAA providers) and its relationship to WP4 Trust Group use cases.

These certificates are used by various entities to sign the attestations they issue. For other entities to trust these signatures, a copy of the certificate MUST be available as a trust anchor in a trusted location. Depending on the entity type, this location will be either a LoTE or a TL (see [ARF § 3.5](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#35-trusted-list-or-lote-provider)).

When validating the signature/seal of a PID, (Q)EAA, PuB-EAA, WIA, or KA, a Wallet Instance or Relying Party MUST verify the LoTE or TL corresponding to the issuing entity type and inspect the **serviceDigitalIdentity** component related to the entity to retrive the trust anchor certificate. This certificate MUST then be used as the trusted source for the public key required to validate the cryptographic signature or seal.

## Scope of TS 119 412-6

ETSI TS 119 412-6 specifies requirements on **end-entity certificates used by providers** to sign their outputs. The basic certificate fields are described in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) and further specialized by the [ETSI EN 319 412] series. The following table specifies the certificate type, its usage, where it can be retrived as a trust anchor, and and the normative reference detailing its profile.

| Certificate type | Used for | Trust anchor location | Standard |
|------------------|----------|------------------------|----------|
| PID Provider Sign/seal certificate | signing PID | PID Providers LoTE | ETSI TS 119 412-6, clause 4 |
| Wallet Provider Sign/seal certificate | WIA, KA | Wallet Providers LoTE  | ETSI TS 119 412-6, clause 5 |
| EAA Provider Sign/seal certificate | signing EAA | MS decision | ETSI TS 119 412-6, clause 6 |
| QEAA Provider Sign/seal certificate | signing QEAA | TL | ETSI TS 119 412-6, clause 7 |
| Pub-EAA Provider Sign/seal certificate | signing  PuB-EAA | Pub-EAA Providers LoTE | ETSI TS 119 412-6, clause 8 |
| **Access certificates** ([WRPAC](../task5-participants-certificates-policies/relying_party_access_certificate.md)) | Authenticating entities to the EUDI Wallet ecosystem | WRPAC Provider LoTE | [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| **Registration certificates** ([WRPAC](../task5-participants-certificates-policies/relying_party_registration_certificate.md)) | Validating the authorization profile for entities in the EUDI Wallet ecosystem | WRPRC Provider LoTE | [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |

**Note**: Signature/Seal certificates are different from Access and Registration certificates: while the former are used to sign/seal attestations, the latter are used to convey the identity of an entity (Access certificates) and its authorization profile (Registration certificate) within the ecosystem. ETSI TS 119 412-6 applies to sign/seal certificates only.

## Profiles by Entity Type

### PID Provider Sign/Seal Certificate

The specific requirements for PID Provider Sign/Seal Certificates are specified in Clause 4 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | REQUIRED. The `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C* or *Type F*.<br>For additional details, see Clause 4.4.1 [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md), Clause 4.3.2 [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) and Clause 4.3.1 [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md). |
| `certificatePolicies` | REQUIRED. It MUST include a `PolicyInformation` structure with `policyIdentifier` set to the OID of a certificate policy including at least the requirements for *NCP+*, defined in [ETSI EN 319 411-1], to comply with [EIDAS-ARF] requirement `AS-AP-10-098`. |
| `subjectAltName` | REQUIRED. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1]. |
| `authorityInfoAccess` | REQUIRED. It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [Online Certificate Status Protocol (OCSP)](#infrastructure-trustonline-certificate-status-protocol-ocsp). |
| `qcStatements` | REQUIRED. It MUST contain a `QCStatement` structure with `statementId` set to `0.4.0.1862.1.6` (`id-etsi-qcs-QcType`).<br>The corresponding `statementInfo` MUST contain a `QcType` structure including exactly one object identifier, namely `0.4.0.194126.1.1` (`id-etsi-qct-pid`), as defined in Clause 4.5 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md). |
 
### Wallet Provider Sign/Seal Certificate

The specific requirements for Wallet Provider Sign/Seal Certificates are specified in Clause 5 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | OPTIONAL. If present, the `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C* or *Type F*.<br>For additional details, see Clause 4.4.1 [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md), Clause 4.3.2 [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) and Clause 4.3.1 [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md). |
| `certificatePolicies` | REQUIRED. It MUST include a `PolicyInformation` structure with `policyIdentifier` set to the OID of a certificate policy including at least (as per [EIDAS-ARF] requirement `EW-DM-38-001`):<br>• The requirements for *NCP*, defined in [ETSI EN 319 411-1], for KAs describing a keystore.<br>• The requirements for *NCP+*, defined in [ETSI EN 319 411-1], for KAs describing a WSCA/WSCD. |
| `subjectAltName` | REQUIRED. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1]. |
| `authorityInfoAccess` | REQUIRED. It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [Online Certificate Status Protocol (OCSP)](#infrastructure-trustonline-certificate-status-protocol-ocsp). |
| `qcStatements` | REQUIRED. It MUST contain a `QCStatement` structure with `statementId` set to `0.4.0.1862.1.6` (`id-etsi-qcs-QcType`).<br>The corresponding `statementInfo` MUST contain a `QcType` structure including exactly one object identifier, namely `0.4.0.194126.1.2` (`id-etsi-qct-wal`), as defined in Clause 5.2 of [ETSI TS 119 412-6]. |

### (Q)EAA Provider Sign/Seal Certificate

The specific requirements for EAA Provider and QEAA Provider Sign/Seal Certificates are specified in Clauses 6 and 7 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md), respectively.

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | OPTIONAL. If present, the `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, or *Type F*.<br>For additional details, see Clause 4.3.2 [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) and Clause 4.3.1 [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md). |
| `certificatePolicies` | REQUIRED (only for QEAA). As described in §6.6.1 of [ETSI EN 319 411-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941102/02.06.01_60/en_31941102v020601p.pdf) |
| `subjectAltName` | REQUIRED. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1]. |
| `authorityInfoAccess` | REQUIRED (only for QEAA). It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [Online Certificate Status Protocol (OCSP)](#infrastructure-trustonline-certificate-status-protocol-ocsp). |
| `qcStatements` | REQUIRED (only for QEAA). It MUST contain a `QCStatement` structure among those defined in Clause 4.2 of [ETSI EN 319 412-5]. |

For both QEAA and EAA Providers, if they manage the lifecycle of the Digital Credentials they issue and they use signed revocation lists such as Token Status List, they MUST use the same Sign/Seal Certificate to sign/seal the revocation list.

### PuB-EAA Provider Sign/Seal Certificate

> **Warning:** While the specific requirements for PuB-EAA Provider Sign/Seal Certificates that are specified in Clause 8 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) do not require this profile to be qualified, Art. 45f(1)(b) of [EU_2024_1183] requires PuB-EAA type Attestations to be signed with a qualified certificate. To satisfy both requirements, although not stated either the [EIDAS-ARF] or [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md), this profile merges the QEAA and PuB-EAA Provider Sign/Seal Certificate profiles specified in Clauses 6, 7 and 8 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | OPTIONAL. If present, the `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. |
| `certificatePolicies` | REQUIRED. It MUST include a `PolicyInformation` structure with `policyIdentifier` set to the OID of a certificate policy including at least the requirements for *NCP+*, defined in [ETSI EN 319 411-1], to comply with [EIDAS-ARF] requirement `AS-AP-10-103`. |
| `subjectAltName` | REQUIRED. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1]. |
| `authorityInfoAccess` | REQUIRED. It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [Online Certificate Status Protocol (OCSP)](#infrastructure-trustonline-certificate-status-protocol-ocsp). |
| `qcStatements` | REQUIRED. It MUST contain the following `QCStatement` structures:<br>• one with `statementId` set to the OID corresponding to `id-etsi-qcs-QcPSB`. The corresponding `statementInfo` MUST contain a `QcPSB` structure including the fields defined in Clause 8.3 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).<br>• one as defined in Clause 4.2 of [ETSI EN 319 412-5]. |

> **Warning:** Annex A of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) does not define the specific OID of the `id-etsi-qcs-QcPSB` statement identifier.

## Mapping to Use Cases

### UC-02: PID / Attestation Provider Onboarding

**Relevant clauses:** 4 (PID), 6 (EAA), 7 (QEAA), 8 (PSBEAA).

| Entity | Sign/seal certificate (TS 119 412-6) | Access certificate (TS 119 411-8) |
|--------|--------------------------------------|----------------------------------|
| PID Provider | Clause 4 — QcType `id-etsi-qct-pid` | [WRPAC](../task5-participants-certificates-policies/pid_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| QEAA Provider | Clause 7 — qualified cert, QTSP issuer | [WRPAC](../task5-participants-certificates-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| PuB-EAA Provider | Clause 8 — QcPSB qcStatement | [WRPAC](../task5-participants-certificates-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| EAA Provider | Clause 6 — EN 319 412-2/3 | [WRPAC](../task5-participants-certificates-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |

**PID Provider:** Certificate used to sign PID attribute attestations. It MUST be formatted as described in [PID Provider Sign/Seal Certificate](#pid-provider-signseal-certificate).

**Attestation Providers (EAA, QEAA, PSBEAA):** Certificates used to sign attestations. These MUST be formatted as described in [(Q)EAA Provider Sign/Seal Certificate](#qeaa-provider-signseal-certificate), [PuB-EAA Provider Sign/Seal Certificate](#puB-eaa-provider-signseal-certificate).


When OCSP/CRL is used for attestation revocation, the OCSP responder cert or CRL MUST be issued/signed by the CA issuing the respective Sign/Seal certificate.

### UC-03: Wallet Provider Onboarding

**Relevant clause:** 5 (Wallet Provider).

| Entity | Sign/seal certificate (TS 119 412-6) |
|--------|--------------------------------------|
| Wallet Provider | Clause 5 — QcType `id-etsi-qct-wal` |

**Wallet Provider:** Certificate used to sign the output of the Wallet provider. It MUST be formatted as described in [Wallet Provider Sign/Seal Certificate](#wallet-provider-signseal-certificate).

### Relying Party Onboarding

**Not covered by TS 119 412-6.** Relying parties use **access certificates** ([WRPAC](../task5-participants-certificates-policies/relying_party_access_certificate.md)) per [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md), not the sign/seal profiles in TS 119 412-6. See also [Trust and Entitlement Discovery](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md) for WRPAC validation flow.

## OIDs (Annex A)

| Identifier | OID | Use |
|------------|-----|-----|
| id-etsi-qct-pid | 0.4.0.194126.1.1 | PID provider sign/seal certificate |
| id-etsi-qct-wal | 0.4.0.194126.1.2 | Wallet provider sign/seal certificate |

## Non-normative examples

The following examples illustrate the distinguishing fields of sign/seal certificates for each entity type. **They are non-normative** and intended only to aid understanding. Conformance requires the full requirements of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) and the applicable base profiles.

### PID Provider Sign/Seal Certificate Example

The following is a non-normative example of a PID Provider Sign/Seal Certificate for legal persons.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: 
            C = IT
            O = Example Trust Services CA
            CN = Example CA
            organizationIdentifier = VATIT-123456789
        Validity:
            Not Before: Jan 27 00:00:00 2026 GMT
            Not After : Jan 27 00:00:00 2027 GMT
        Subject: 
            C = IT
            O = Example of PID Provider
            CN = PID Provider Example
            organizationIdentifier = LEIIT-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                keyid:HEX(20B_KEYID_OF_ISSUING_CA_PUBLIC_KEY)
            X509v3 Subject Key Identifier: 
                SHA-1(SUBJECT_PUBLIC_KEY_VALUE)
            X509v3 Key Usage: critical
                Non Repudiation
            X509v3 Certificate Policies: 
                Policy: 0.4.0.194112.1.3
                    CPS: https://rpca.example.test/cps
            X509v3 Subject Alternative Name: 
                URI: https://pid.example.test/support
                email: support@pid.example.test
                otherName: id-at-telephoneNumber: +420-111-222-333
            X509v3 CRL Distribution Points: 
                Full Name:
                    URI: https://crl.example.test/issuing-ca.crl
            Authority Information Access: 
                CA Issuers - URI: https://ca.example.test/caIssuers/issuing-ca.cer
                OCSP - URI: https://ocsp.example.test
            X509v3 QCStatements: 
                id-etsi-qcs-QcType: id-etsi-qct-pid
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value: BASE64(SIGN(issuerPrivateKey, DER(tbsCertificate)))
```

*Used to sign PID attribute attestations issued to the wallet.*

### Wallet Provider Sign/Seal Certificate Example

The following is a non-normative example of a Wallet Provider Sign/Seal Certificate for legal persons.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: 
            C = DE
            O = Example Trust Services CA
            CN = Example CA
            organizationIdentifier = VATDE-123456789
        Validity:
            Not Before: Jan 27 00:00:00 2026 GMT
            Not After : Jan 27 00:00:00 2027 GMT
        Subject: 
            C = DE
            O = Example of Wallet Provider
            CN = Wallet Provider Example
            organizationIdentifier = LEIDE-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                keyid:HEX(20B_KEYID_OF_ISSUING_CA_PUBLIC_KEY)
            X509v3 Subject Key Identifier: 
                SHA-1(SUBJECT_PUBLIC_KEY_VALUE)
            X509v3 Key Usage: critical
                Non Repudiation
            X509v3 Certificate Policies: 
                Policy: 0.4.0.194112.1.3
                    CPS: https://rpca.example.test/cps
            X509v3 Subject Alternative Name: 
                URI: https://wp.example.test/support
                email: support@wp.example.test
                otherName: id-at-telephoneNumber: +420-111-222-333
            X509v3 CRL Distribution Points: 
                Full Name:
                    URI: https://crl.example.test/issuing-ca.crl
            Authority Information Access: 
                CA Issuers - URI: https://ca.example.test/caIssuers/issuing-ca.cer
                OCSP - URI: https://ocsp.example.test
            X509v3 QCStatements: 
                id-etsi-qcs-QcType: id-etsi-qct-wal
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value: BASE64(SIGN(issuerPrivateKey, DER(tbsCertificate)))
```
*Used to sign the output of the Wallet provider (e.g. wallet attestations).*

### EAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a EAA Provider Sign/Seal Certificate for legal persons.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: 
            C = IT
            O = Example Trust Services CA
            CN = Example CA
            organizationIdentifier = VATIT-123456789
        Validity:
            Not Before: Jan 27 00:00:00 2026 GMT
            Not After : Jan 27 00:00:00 2027 GMT
        Subject: 
            C = FR
            O = Example of EAA Provider
            CN = EAA Provider Example
            organizationIdentifier = LEIXYZ-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                keyid:HEX(20B_KEYID_OF_ISSUING_CA_PUBLIC_KEY)
            X509v3 Key Usage: critical
                Non Repudiation
            X509v3 Certificate Policies: 
                Policy: 0.4.0.194112.1.3
                    CPS: https://rpca.example.test/cps
            X509v3 Subject Alternative Name: 
                URI: https://eaa.example.test/support
                email: support@eaa.example.test
                otherName: id-at-telephoneNumber: +420-111-222-333
            X509v3 CRL Distribution Points: 
                Full Name:
                    URI: https://crl.example.test/issuing-ca.crl
            Authority Information Access: 
                CA Issuers - URI: https://ca.example.test/caIssuers/issuing-ca.cer
                OCSP - URI: https://ocsp.example.test
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value: BASE64(SIGN(issuerPrivateKey, DER(tbsCertificate)))
```
*Used to sign electronic attestations of attributes. OCSP responder cert or CRL, if used, shall be issued/signed by this cert.*

### QEAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a QEAA Provider Sign/Seal Certificate for legal persons.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: 
            C = PT
            O = Example Trust Services CA
            CN = Example CA
            organizationIdentifier = VATPT-123456789
        Validity:
            Not Before: Jan 27 00:00:00 2026 GMT
            Not After : Jan 27 00:00:00 2027 GMT
        Subject: 
            C = PT
            O = Example of (Q)EAA Provider
            CN = (Q)EAA Provider Example
            organizationIdentifier = LEIPT-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                keyid:HEX(20B_KEYID_OF_ISSUING_CA_PUBLIC_KEY)
            X509v3 Key Usage: critical
                Non Repudiation
            X509v3 Certificate Policies: 
                Policy: 0.4.0.194112.1.3
                    CPS: https://rpca.example.test/cps
            X509v3 Subject Alternative Name: 
                URI: https://eaa.example.test/support
                email: support@eaa.example.test
                otherName: id-at-telephoneNumber: +420-111-222-333
            X509v3 CRL Distribution Points: 
                Full Name:
                    URI: https://crl.example.test/issuing-ca.crl
            Authority Information Access: 
                CA Issuers - URI: https://ca.example.test/caIssuers/issuing-ca.cer
                OCSP - URI: https://ocsp.example.test
            X509v3 QCStatements: 
                id-etsi-qcs-QcType: id-etsi-qct-esign
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value: BASE64(SIGN(issuerPrivateKey, DER(tbsCertificate)))
```
*Used to sign qualified electronic attestations of attributes. Issuer shall be a QTSP.*

### PSBEAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a PuB-EAA Provider Sign/Seal Certificate for legal persons.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: 
            C = PL
            O = Example Trust Services CA
            CN = Example CA
            organizationIdentifier = VATPL-123456789
        Validity:
            Not Before: Jan 27 00:00:00 2026 GMT
            Not After : Jan 27 00:00:00 2027 GMT
        Subject: 
            C = PL
            O = Example of PuB-EAA Provider
            CN = PuB-EAA Provider Example
            organizationIdentifier = LEIPL-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
        X509v3 extensions:
            X509v3 Authority Key Identifier: 
                keyid:HEX(20B_KEYID_OF_ISSUING_CA_PUBLIC_KEY)
            X509v3 Subject Key Identifier: 
                SHA-1(SUBJECT_PUBLIC_KEY_VALUE)
            X509v3 Key Usage: critical
                Non Repudiation
            X509v3 Certificate Policies: 
                Policy: 0.4.0.194112.1.3
                    CPS: https://rpca.example.test/cps
            X509v3 Subject Alternative Name: 
                URI: https://pub-eaa.example.test/support
                email: support@pub-eaa.example.test
                otherName: id-at-telephoneNumber: +420-111-222-333
            X509v3 CRL Distribution Points: 
                Full Name:
                    URI: https://crl.example.test/issuing-ca.crl
            Authority Information Access: 
                CA Issuers - URI: https://ca.example.test/caIssuers/issuing-ca.cer
                OCSP - URI: https://ocsp.example.test
            X509v3 QCStatements: 
                id-etsi-qcs-QcPSB:
                    countryOfLegislation: IT
                    authSourceIdentification: https://www.anpr.interno.it
                    legislationIdentification: https://www.normattiva.it/eli/id/2005/05/16/005G0106/sg
                id-etsi-qcs-QcType: id-etsi-qct-esign
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value: BASE64(SIGN(issuerPrivateKey, DER(tbsCertificate)))
```

*Used to sign attestations from an authentic source by or on behalf of a public sector body. QcPSB identifies the legislation and authentic source.*

## References

### ETSI certificate profile specifications

- [ETSI TS 119 412-6 V1.1.1](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) — Provider sign/seal certificate profiles (PID, Wallet, EAA, QEAA, PSBEAA)
- [ETSI EN 319 412-2 V2.4.1](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) — Certificate profile for natural persons (base for TS 119 412-6)
- [ETSI EN 319 412-3 V1.3.1](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) — Certificate profile for legal persons (base for TS 119 412-6)
- [ETSI TS 119 412-6 PDF](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf) — official document
- [ETSI EN 319 412-2 PDF](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf) — official document
- [ETSI EN 319 412-3 PDF](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf) — official document

### Use cases

- [UC-02 PID/EAA Provider Onboarding](../task1-use-cases/subtask1-1-onboarding/pid_eaa_provider_onboarding.md)
- [UC-03 Wallet Provider Onboarding](../task1-use-cases/subtask1-1-onboarding/wallet-provider-onboarding.md)
