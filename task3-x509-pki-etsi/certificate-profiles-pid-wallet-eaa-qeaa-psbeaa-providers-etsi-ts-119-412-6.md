# Certificate Profiles for PID, Wallet, EAA, QEAA, and PuB-EAA Providers (ETSI TS 119 412-6)

This document describes the content of ETSI TS 119 412-6 (certificate profile requirements for PID, Wallet Instance Attestation (WIA), Key Attestation (KA), EAA, QEAA, and PuB-EAA Providers) and its relationship to WP4 Trust Group use cases. 

**Note**: In this document, **PuB-EAA** means Public Sector Body Electronic Attestation of Attributes; ETSI TS 119 412-6 uses **PSBEAA** for the same provider type.

These certificates are used by various entities to sign the attestations they issue. For other entities to trust these signatures, a copy of the certificate MUST be available as a trust anchor in a trusted location. Depending on the entity type, this location will be either a List of Trusted Entities (LoTE) or a Trusted List (TL) (see [ARF § 3.5](https://eudi.dev/3.0.0/architecture-and-reference-framework-main/#35-trusted-list-or-lote-provider)).

When validating the signature or seal of a PID, (Q)EAA, PuB-EAA, WIA, or KA, a Wallet Instance or Relying Party MUST verify the LoTE or TL corresponding to the issuing entity type and inspect the `serviceDigitalIdentity` component related to the entity to retrieve the trust anchor certificate. This certificate MUST then be used as the trusted source for the public key required to validate the cryptographic signature or seal.

## Scope of TS 119 412-6

ETSI TS 119 412-6 specifies requirements on **end-entity certificates used by providers** to sign their outputs. The basic certificate fields are described in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) and further specialized by the ETSI EN 319 412 series. The following table specifies the certificate type, its usage, where it can be retrieved as a trust anchor, and the normative reference detailing its profile.

### Common WE BUILD Profile Rules

The following additional WE BUILD profile requirements apply to the PID, Wallet, EAA, QEAA, and PuB-EAA Provider sign/seal certificates. They are additional to, and do not replace, the requirements of ETSI TS 119 412-6 and the applicable ETSI EN 319 412 base profile.

- The subject public key of each end-entity certificate MUST be an ECDSA key on P-256 (`secp256r1`, also named `prime256v1`).
- The issuing CA MUST use ECDSA with SHA-256 (`ecdsa-with-SHA256`) to sign each certificate.
- RSA keys and RSA signature algorithms MUST NOT be used for these sign/seal certificates.
- When the corresponding provider private key signs a JOSE object (e.g., for a Wallet Instance Attestation), the JOSE algorithm identifier is `ES256`, meaning SHA-256 with ECDSA over P-256. `ES256` is a JOSE algorithm identifier and is not an X.509 signature algorithm name.

| Certificate type | Used for | Trust anchor location | Standard |
|------------------|----------|------------------------|----------|
| PID Provider Sign/Seal Certificate | signing PID | PID Providers LoTE | ETSI TS 119 412-6, clause 4 |
| Wallet Provider Sign/Seal Certificate | one Wallet Solution's WIA, KA, and related Token Status List | Trusted List of Wallet Providers (Wallet Providers LoTE) | ETSI TS 119 412-6, clause 5 |
| EAA Provider Sign/Seal Certificate | signing EAA | Member State decision | ETSI TS 119 412-6, clause 6 |
| QEAA Provider Sign/Seal Certificate | signing QEAA | TL | ETSI TS 119 412-6, clause 7 |
| PuB-EAA Provider Sign/Seal Certificate | signing PuB-EAA | PuB-EAA Providers LoTE | ETSI TS 119 412-6, clause 8 |
| **Access certificates** ([WRPAC](../task5-participants-policies/relying_party_access_certificate.md)) | Authenticating entities to the EUDI Wallet ecosystem | WRPAC Provider LoTE | [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| **Registration certificates** ([WRPRC](../task5-participants-policies/relying_party_registration_certificate.md)) | Validating the authorization profile for entities in the EUDI Wallet ecosystem | WRPRC Provider LoTE | [ETSI TS 119 475](../references/etsi/ETSI_TS_119_475.md) |

**Note:** Sign/seal certificates are different from access and registration certificates: while the former are used to sign or seal attestations, the latter convey the identity of an entity (access certificates) and its authorization profile (registration certificates) within the ecosystem. ETSI TS 119 412-6 applies to sign/seal certificates only.

## Profiles by Entity Type

### PID Provider Sign/Seal Certificate

The specific requirements for PID Provider Sign/Seal Certificates are specified in Clause 4 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | REQUIRED. The `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C*, or *Type F*.<br>For additional details, see Clause 4.4.1 [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md), Clause 4.3.2 [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md), and Clause 4.3.1 [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md). |
| `certificatePolicies` | REQUIRED. It MUST include a `PolicyInformation` structure with `policyIdentifier` set to the OID of a certificate policy including at least the requirements for *NCP+*, defined in [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf), to comply with [EUDI Wallet ARF](https://eudi.dev/3.0.0/architecture-and-reference-framework-main/) requirement `AS-AP-10-098`. |
| `subjectAltName` | REQUIRED. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601c.pdf). |
| `authorityInfoAccess` | REQUIRED. It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960). |
| `qcStatements` | REQUIRED. It MUST contain a `QCStatement` structure with `statementId` set to `0.4.0.1862.1.6` (`id-etsi-qcs-QcType`).<br>The corresponding `statementInfo` MUST contain a `QcType` structure including exactly one object identifier, namely `0.4.0.194126.1.1` (`id-etsi-qct-pid`), as defined in Clause 4.5 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md). |

### Wallet Provider Sign/Seal Certificate

The specific requirements for Wallet Provider Sign/Seal Certificates are specified in Clause 5 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | OPTIONAL. If present, the `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C*, or *Type F*.<br>For additional details, see Clause 4.4.1 [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md), Clause 4.3.2 [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md), and Clause 4.3.1 [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md). |
| `certificatePolicies` | REQUIRED. It MUST include a `PolicyInformation` structure with `policyIdentifier` set to the OID of a certificate policy including at least (as per [EUDI Wallet ARF](https://eudi.dev/3.0.0/architecture-and-reference-framework-main/) requirement `EW-DM-38-001`):<br>• The requirements for *NCP*, defined in [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf), for KAs describing a keystore.<br>• The requirements for *NCP+*, defined in [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf), for KAs describing a WSCA/WSCD. |
| `subjectAltName` | REQUIRED. A URI in this extension, when present, is contact information for the Wallet Provider. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601c.pdf). |
| `authorityInfoAccess` | REQUIRED. It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960). |
| `qcStatements` | REQUIRED. It MUST contain a `QCStatement` structure with `statementId` set to `0.4.0.1862.1.6` (`id-etsi-qcs-QcType`).<br>The corresponding `statementInfo` MUST contain a `QcType` structure including exactly one object identifier, namely `0.4.0.194126.1.2` (`id-etsi-qct-wal`), as defined in Clause 5.2 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md). |

Each Wallet Solution MUST have its own sign/seal key pair and certificate for its WIA and KA. The Wallet Provider MUST generate or register a distinct ECDSA P-256 key pair for each Wallet Solution and obtain a distinct sign/seal certificate for each of them. The key pair and certificate MUST NOT be reused for another Wallet Solution. On the Wallet Providers LoTE, that certificate is the `ServiceDigitalIdentity` of the `http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance` service for the solution named by `ServiceName` ([ETSI TS 119 602](../references/etsi/ts_119602v010101p.md) Annex E, Table E.3). The Wallet Solution identifier on that list is `ServiceName` together with `ServiceUniqueIdentifier`. [Technical Specification 3](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md) conveys the solution name in the WIA `wallet_name` claim.

The private key corresponding to a Wallet Solution's sign/seal certificate MUST sign that solution's WIA and KA. These signatures MUST use `ES256`. A Token Status List for the WIA (`client_status`) or the KA (`key_storage_status`) MAY be signed with that same private key, or with a distinct key and certificate. When a distinct revocation certificate is used, it is the trust anchor for WIA and KA Attestation Status Lists in [ARF Topic 31](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/) requirement `WPNot_02`, and the `ServiceDigitalIdentity` of the `http://uri.etsi.org/19602/SvcType/WalletSolution/Revocation` service.

### (Q)EAA Provider Sign/Seal Certificate

The specific requirements for EAA Provider and QEAA Provider Sign/Seal Certificates are specified in Clauses 6 and 7 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md), respectively.

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | OPTIONAL. If present, the `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, or *Type F*.<br>For additional details, see Clause 4.3.2 [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) and Clause 4.3.1 [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md). |
| `certificatePolicies` | REQUIRED (only for QEAA), as described in Clause 6.6.1 of [ETSI EN 319 411-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941102/02.06.01_60/en_31941102v020601p.pdf). |
| `subjectAltName` | REQUIRED. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601c.pdf). |
| `authorityInfoAccess` | REQUIRED (only for QEAA). It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960). |
| `qcStatements` | REQUIRED (only for QEAA). It MUST contain a `QCStatement` structure among those defined in Clause 4.2 of [ETSI EN 319 412-5](https://www.etsi.org/deliver/etsi_en/319400_319499/31941205/02.05.01_60/en_31941205v020501c.pdf). |

For both EAA and QEAA Providers, if they manage the lifecycle of the digital credentials they issue and use a signed revocation list such as a Token Status List, they MUST use the private key corresponding to the same sign/seal certificate to sign or seal the revocation list.

### PuB-EAA Provider Sign/Seal Certificate

> **Warning:** The requirements for PuB-EAA Provider Sign/Seal Certificates in Clause 8 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) do not require this profile to be qualified, while Article 45f(1)(b) of [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng) requires PuB-EAA attestations to be signed with a qualified certificate. To satisfy both requirements, although this combination is not stated in either the [EUDI Wallet ARF](https://eudi.dev/3.0.0/architecture-and-reference-framework-main/) or ETSI TS 119 412-6, this profile merges the EAA, QEAA, and PuB-EAA Provider Sign/Seal Certificate profiles specified in Clauses 6, 7, and 8 of ETSI TS 119 412-6.

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

| Extension | Description |
| :--- | :--- |
| `authorityKeyIdentifier` | REQUIRED. The value SHOULD be derived from the public key using the methods defined in [RFC 5280 Section 4.2.1.1](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). |
| `subjectKeyIdentifier` | OPTIONAL. If present, the `keyIdentifier` field SHOULD be derived from the subject public key using the methods defined in [RFC 5280 Section 4.2.1.2](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2). |
| `keyUsage` | REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, or *Type F*.<br>For additional details, see Clause 4.3.2 [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) and Clause 4.3.1 [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md). |
| `certificatePolicies` | REQUIRED. It MUST include a `PolicyInformation` structure with `policyIdentifier` set to the OID of a certificate policy including at least the requirements for *NCP+*, defined in [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf), to comply with [EUDI Wallet ARF](https://eudi.dev/3.0.0/architecture-and-reference-framework-main/) requirement `AS-AP-10-103`. |
| `subjectAltName` | REQUIRED. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601c.pdf). |
| `authorityInfoAccess` | REQUIRED. It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960). |
| `qcStatements` | REQUIRED. It MUST contain the following `QCStatement` structures:<br>• one with `statementId` set to the OID corresponding to `id-etsi-qcs-QcPSB`. The corresponding `statementInfo` MUST contain a `QcPSB` structure including the fields defined in Clause 8.3 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).<br>• one as defined in Clause 4.2 of [ETSI EN 319 412-5](https://www.etsi.org/deliver/etsi_en/319400_319499/31941205/02.05.01_60/en_31941205v020501c.pdf). |

> **Warning:** Annex A of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) does not define the specific OID of the `id-etsi-qcs-QcPSB` statement identifier.

## Certificate Signing Request Profiles

This section defines the common certificate signing request (CSR) requirements for PID, Wallet, EAA, QEAA, and PuB-EAA Provider sign/seal certificates. The certificate profile selected by the provider determines the profile-specific subject, extensions, certificate policy, and `QcType`.

### Common CSR Profile

A provider requesting one of these sign/seal certificates MUST submit a PKCS#10 CSR encoded in PEM or DER.

The CSR MUST:

1. Contain a valid PKCS#10 CSR signature that proves possession of the requested private key.
2. Use an ECDSA P-256 subject public key and an `ecdsa-with-SHA256` CSR signature.
3. Contain a subject that conforms to the applicable [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) or [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) base profile and matches the provider onboarding data. For a legal-person provider, the subject MUST comply with ETSI EN 319 412-3 clause 4.2.1 and include `countryName`, `organizationName`, `organizationIdentifier`, and `commonName`. Where a natural-person provider profile applies, the subject MUST comply with ETSI EN 319 412-2 clause 4.2.4.
4. Contain a PKCS#9 `extensionRequest` attribute requesting the profile-compliant `keyUsage` choice (ETSI EN 319 412-3 clause 4.3.1 for legal entities or ETSI EN 319 412-2 clause 4.3.2 for natural persons) and the `subjectAltName` values required by the requested certificate profile and provider onboarding data.

For a Wallet Provider CSR, the key pair and certificate MUST NOT be registered or reused for another Wallet Solution. A URI in `subjectAltName`, when present, is contact information for the Wallet Provider.

The CA controls the issuer name, serial number, validity period, `authorityKeyIdentifier`, `subjectKeyIdentifier`, `authorityInfoAccess`, `cRLDistributionPoints`, certificate policy, and `qcStatements` of the issued certificate. The CA MUST apply the complete profile for the requested certificate type, including its profile-specific `QcType`.

### CSR Validation

Before issuing any PID, Wallet, EAA, QEAA, or PuB-EAA Provider sign/seal certificate, the CA MUST perform the following checks:

1. Parse the submitted object as a PKCS#10 CSR in PEM or DER encoding.
2. Verify the CSR signature using the requested subject public key.
3. Verify that the requested public key is ECDSA on P-256 and that the CSR signature uses `ecdsa-with-SHA256`. The CA MUST reject RSA keys and non-P-256 curves.
4. Identify the requested certificate profile and verify that the subject conforms to its applicable ETSI EN 319 412 base profile and matches the submitted provider data.
5. Verify that the `extensionRequest` contains the profile-compliant `keyUsage` choice and the `subjectAltName` values required by the requested certificate profile. Unsupported `keyUsage` requests MUST be rejected.
6. For a Wallet Provider CSR, reject a key pair or certificate registered or reused for another Wallet Solution.
7. For other provider profiles, verify each profile-specific identifier and requested SAN value against the provider's onboarding data.

If any check fails, the CA MUST reject the CSR before certificate issuance. If all checks succeed, the CA MUST issue a fresh certificate that contains all mandatory extensions in the requested certificate profile, including its profile-specific `QcType` where applicable.

## OpenSSL Commands

The following non-normative code examples illustrate the Wallet Provider process for generating a Wallet Solution sign/seal key and CSR, verifying the CSR, and issuing its certificate. They demonstrate common P-256 mechanics; replace the provider subject and contact URI with values from the onboarding request, and replace the CA values with those of the issuing CA. The common CSR profile above applies to all five sign/seal certificate types, while these commands specifically illustrate the Wallet Provider process.

### Generate Key Pair

```bash
openssl genpkey -algorithm EC \
  -pkeyopt ec_paramgen_curve:P-256 \
  -out wallet_solution.key
```

### Generate CSR

```bash
openssl req -new -sha256 \
  -key wallet_solution.key \
  -out wallet_solution.csr \
  -subj "/C=DE/O=Example of Wallet Provider/CN=Wallet Provider Example/organizationIdentifier=LEIDE-5493001KJTIIGC8Y1R12" \
  -addext "keyUsage=critical,nonRepudiation" \
  -addext "subjectAltName=URI:https://wp.example.test/support"
```

### Inspect and Verify CSR

```bash
openssl req -in wallet_solution.csr -text -noout -verify
```

### Illustrative Certificate Issuance

The issuing key in this example is also ECDSA P-256 and the certificate is signed with SHA-256:

```bash
openssl genpkey -algorithm EC \
  -pkeyopt ec_paramgen_curve:P-256 \
  -out issuing_ca.key

openssl req -new -x509 -sha256 \
  -key issuing_ca.key \
  -out issuing_ca.crt \
  -days 3650 \
  -subj "/C=DE/O=Example Trust Services CA/CN=Example CA/organizationIdentifier=VATDE-123456789"

openssl x509 -req -sha256 \
  -in wallet_solution.csr \
  -CA issuing_ca.crt \
  -CAkey issuing_ca.key \
  -CAcreateserial \
  -out wallet_solution.crt \
  -days 365 \
  -extfile wallet_provider_ext.cnf \
  -extensions v3_wallet_provider
```

### Extensions Configuration (wallet_provider_ext.cnf)

The CA's `wallet_provider_ext.cnf` configuration MUST apply the complete certificate profile selected for the CSR. In particular, it MUST supply the profile-compliant `keyUsage`, `certificatePolicies`, `authorityInfoAccess`, conditional `cRLDistributionPoints`, and the profile-specific `qcStatements`. For a Wallet Provider certificate, this includes `id-etsi-qct-wal` (`0.4.0.194126.1.2`). A URI in `subjectAltName`, when present, is contact information.

The following non-normative configuration illustrates these profile-relevant entries for the example certificate.

```ini
[v3_wallet_provider]
authorityKeyIdentifier = keyid,issuer
subjectKeyIdentifier = hash
keyUsage = critical, nonRepudiation
subjectAltName = @wallet_provider_san
certificatePolicies = @policy_section
authorityInfoAccess = caIssuers;URI:https://ca.example.test/caIssuers/issuing-ca.cer,OCSP;URI:https://ocsp.example.test
crlDistributionPoints = URI:https://crl.example.test/issuing-ca.crl
# id-etsi-qcs-QcType containing id-etsi-qct-wal.
1.3.6.1.5.5.7.1.3 = ASN1:SEQUENCE:qc_statements

[wallet_provider_san]
URI.1 = https://wp.example.test/support
email.1 = support@wp.example.test

[policy_section]
policyIdentifier = 0.4.0.194112.1.3
CPS.1 = https://rpca.example.test/cps

[qc_statements]
1 = SEQUENCE:qc_type_statement

[qc_type_statement]
statementId = OID:0.4.0.1862.1.6
statementInfo = SEQUENCE:qc_type

[qc_type]
1 = OID:0.4.0.194126.1.2
```

## Mapping to Use Cases

### UC-02: PID / Attestation Provider Onboarding

**Relevant clauses:** 4 (PID), 6 (EAA), 7 (QEAA), 8 (PuB-EAA).

| Entity | Sign/seal certificate (TS 119 412-6) | Access certificate (TS 119 411-8) |
|--------|--------------------------------------|----------------------------------|
| PID Provider | Clause 4 — `QcType` `id-etsi-qct-pid` | [WRPAC](../task5-participants-policies/pid_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| QEAA Provider | Clause 7 — qualified certificate, QTSP issuer | [WRPAC](../task5-participants-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| PuB-EAA Provider | Clause 8 — `QcPSB` statement | [WRPAC](../task5-participants-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| EAA Provider | Clause 6 — ETSI EN 319 412-2/-3 | [WRPAC](../task5-participants-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |

**PID Provider:** The certificate is used to sign PID attribute attestations. It MUST be formatted as described in [PID Provider Sign/Seal Certificate](#pid-provider-signseal-certificate).

**Attestation Providers (EAA, QEAA, PuB-EAA):** These certificates are used to sign attestations. They MUST be formatted as described in [(Q)EAA Provider Sign/Seal Certificate](#qeaa-provider-signseal-certificate) and [PuB-EAA Provider Sign/Seal Certificate](#pub-eaa-provider-signseal-certificate).

For an EAA, and for a QEAA or PuB-EAA through Clauses 7.3 and 8.4, when OCSP or a CRL is used for revocation of the attestation, the private key corresponding to that provider's sign/seal certificate MUST sign the OCSP responder certificate or the CRL, as required by Clause 6.2 of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md).

### UC-03: Wallet Provider Onboarding

**Relevant clause:** 5 (Wallet Provider).

| Entity | Sign/seal certificate (TS 119 412-6) |
|--------|--------------------------------------|
| Wallet Provider | Clause 5 — one Wallet Solution sign/seal certificate per Wallet Solution; `QcType` `id-etsi-qct-wal` |

**Wallet Provider:** Each Wallet Solution receives its own sign/seal key pair and certificate for its WIA and KA. The corresponding private key signs that solution's WIA and KA using `ES256`. A Token Status List for that solution may be signed with the same key or with a separate revocation key and certificate. The certificate MUST be formatted as described in [Wallet Provider Sign/Seal Certificate](#wallet-provider-signseal-certificate).

### Relying Party Onboarding

**Not covered by TS 119 412-6.** Relying parties use **access certificates** ([WRPAC](../task5-participants-policies/relying_party_access_certificate.md)) per [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md), not the sign/seal profiles in TS 119 412-6. See also [Trust and Entitlement Discovery](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md) for WRPAC validation flow.

## OIDs (Annex A)

| Identifier | OID | Use |
|------------|-----|-----|
| `id-etsi-qct-pid` | `0.4.0.194126.1.1` | PID Provider sign/seal certificate |
| `id-etsi-qct-wal` | `0.4.0.194126.1.2` | Wallet Provider sign/seal certificate |

## Non-normative Examples

The following examples illustrate the distinguishing fields of issued sign/seal certificates for each entity type. **They are non-normative** and are not CSR templates. A CSR is specified in [Certificate Signing Request Profiles](#certificate-signing-request-profiles) and [OpenSSL Commands](#openssl-commands). Conformance requires the full requirements of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) and the applicable base profiles.

### PID Provider Sign/Seal Certificate Example

The following is a non-normative example of a PID Provider Sign/Seal Certificate for a legal person.

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: ecdsa-with-SHA256
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
            Public Key Algorithm: id-ecPublicKey
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
            ASN1 OID: prime256v1
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
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value: BASE64(ECDSA_SIGN(issuerPrivateKey, DER(tbsCertificate)))
```

*Used to sign PID attribute attestations issued to the wallet.*

### Wallet Provider Sign/Seal Certificate Example

The following is a non-normative example of one Wallet Solution's Wallet Provider Sign/Seal Certificate for a legal person.

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: ecdsa-with-SHA256
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
            Public Key Algorithm: id-ecPublicKey
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
            ASN1 OID: prime256v1
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
            X509v3 CRL Distribution Points: 
                Full Name:
                    URI: https://crl.example.test/issuing-ca.crl
            Authority Information Access: 
                CA Issuers - URI: https://ca.example.test/caIssuers/issuing-ca.cer
                OCSP - URI: https://ocsp.example.test
            X509v3 QCStatements: 
                id-etsi-qcs-QcType: id-etsi-qct-wal
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value: BASE64(ECDSA_SIGN(issuerPrivateKey, DER(tbsCertificate)))
```

*Used to sign the WIA and KA for the example Wallet Solution. A Token Status List for that solution may be signed with this certificate or with a separate revocation certificate.*

### EAA Provider Sign/Seal Certificate Example

The following is a non-normative example of an EAA Provider Sign/Seal Certificate for a legal person.

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: ecdsa-with-SHA256
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
            organizationIdentifier = LEIFR-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
            ASN1 OID: prime256v1
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
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value: BASE64(ECDSA_SIGN(issuerPrivateKey, DER(tbsCertificate)))
```

*Used to sign electronic attestations of attributes. If OCSP or a CRL is used for attestation revocation, the private key corresponding to the provider sign/seal certificate signs the OCSP responder certificate or CRL, respectively.*

### QEAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a QEAA Provider Sign/Seal Certificate for a legal person.

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: ecdsa-with-SHA256
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
            O = Example of QEAA Provider
            CN = QEAA Provider Example
            organizationIdentifier = LEIPT-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
            ASN1 OID: prime256v1
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
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value: BASE64(ECDSA_SIGN(issuerPrivateKey, DER(tbsCertificate)))
```

*Used to sign qualified electronic attestations of attributes. The issuer in this example is a QTSP.*

### PuB-EAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a PuB-EAA Provider Sign/Seal Certificate for a legal person.

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: ecdsa-with-SHA256
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
            O = Example of PuB-EAA Provider
            CN = PuB-EAA Provider Example
            organizationIdentifier = LEIIT-5493001KJTIIGC8Y1R12
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
            Public-Key: BASE64(SPKI_PUBLIC_KEY_BYTES)
            ASN1 OID: prime256v1
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
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value: BASE64(ECDSA_SIGN(issuerPrivateKey, DER(tbsCertificate)))
```

*Used to sign attestations from an authentic source by or on behalf of a public sector body. QcPSB identifies the legislation and authentic source.*

## References

### ETSI Certificate Profile Specifications

- [ETSI TS 119 412-6 V1.1.1](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) — Provider sign/seal certificate profiles (PID, Wallet, EAA, QEAA, and PuB-EAA (PSBEAA))
- [ETSI EN 319 412-2 V2.4.1](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) — Certificate profile for natural persons (base for TS 119 412-6)
- [ETSI EN 319 412-3 V1.3.1](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) — Certificate profile for legal persons (base for TS 119 412-6)
- [ETSI EN 319 411-1 V1.4.1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf) — General policy requirements for trust service providers issuing certificates
- [ETSI EN 319 411-2 V2.6.1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941102/02.06.01_60/en_31941102v020601p.pdf) — Policy requirements for trust service providers issuing EU qualified certificates
- [ETSI EN 319 412-1 V1.6.1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601c.pdf) — General certificate profile requirements and common data structures
- [ETSI EN 319 412-5 V2.5.1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941205/02.05.01_60/en_31941205v020501c.pdf) — Qualified certificate statements
- [ETSI TS 119 412-6 PDF](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf) — official document
- [ETSI EN 319 412-2 PDF](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf) — official document
- [ETSI EN 319 412-3 PDF](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf) — official document

### Regulatory and Architecture References

- [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng) — amended eIDAS regulatory framework
- [EUDI Wallet ARF v3.0.0](https://eudi.dev/3.0.0/architecture-and-reference-framework-main/) — architecture and reference framework requirements
- [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) — Internet X.509 PKI certificate and CRL profile
- [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960) — Online Certificate Status Protocol (OCSP)

### WE BUILD and Related Specifications

- [WE BUILD CS-002: Credential Presentation](https://github.com/webuild-consortium/wp4-architecture/blob/main/conformance-specs/cs-02-credential-presentation.md#5-protocol-overview) — P-256/ES256 presentation crypto suite
- [WE BUILD CS-004: Individual Wallet Unit Attestation (WUA) Lifecycle](https://github.com/webuild-consortium/wp4-architecture/blob/main/conformance-specs/cs-04-wua-lifecycle.md#82-status--revocation-interface) — WIA/KA Token Status List requirements
- [EUDI Wallet Technical Specification TS-03](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md#25-revocation) — WIA/KA status and signature algorithm background

### Use Cases

- [UC-02 PID/EAA Provider Onboarding](../task1-use-cases/subtask1-1-onboarding/pid_eaa_provider_onboarding.md)
- [UC-03 Wallet Provider Onboarding](../task1-use-cases/subtask1-1-onboarding/wallet-provider-onboarding.md)
