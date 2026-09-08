# Certificate Profiles for PID, Wallet, EAA, QEAA, and PSBEAA Providers (ETSI TS 119 412-6)

This document describes the content of ETSI TS 119 412-6 (Certificate profile requirements for PID, Wallet Instance Attestation (WIA), Key Attestation (KA), EAA, QEAA, and PuB-EAA providers) and its relationship to WP4 Trust Group use cases.

These certificates are used by various entities to sign the attestations they issue. For other entities to trust these signatures, a copy of the certificate MUST be available as a trust anchor in a trusted location. Depending on the entity type, this location will be either a LoTE or a TL (see [ARF § 3.5](https://eudi.dev/3.0.0/architecture-and-reference-framework-main/#35-trusted-list-or-lote-provider)).

When validating the signature/seal of a PID, (Q)EAA, PuB-EAA, WIA, or KA, a Wallet Instance or Relying Party MUST verify the LoTE or TL corresponding to the issuing entity type and inspect the **serviceDigitalIdentity** component related to the entity to retrieve the trust anchor certificate. This certificate MUST then be used as the trusted source for the public key required to validate the cryptographic signature or seal.

## Scope of TS 119 412-6

ETSI TS 119 412-6 specifies requirements on **end-entity certificates used by providers** to sign their outputs. The basic certificate fields are described in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) and further specialized by the [ETSI EN 319 412] series. The following table specifies the certificate type, its usage, where it can be retrieved as a trust anchor, and the normative reference detailing its profile.

### Common WE BUILD profile rules

The following additional WE BUILD profile requirements apply to the PID, Wallet, EAA, QEAA, and PuB-EAA Provider sign/seal certificates. They are additional to, and do not replace, the requirements of ETSI TS 119 412-6 and the applicable ETSI EN 319 412 base profile.

- The subject public key of each end-entity certificate MUST be an ECDSA key on P-256 (`secp256r1`, also named `prime256v1`).
- The X.509 signature algorithm used to sign each certificate MUST be ECDSA with SHA-256 (`ecdsa-with-SHA256`).
- RSA keys and RSA signature algorithms MUST NOT be used for these sign/seal certificates.
- When the corresponding provider private key signs a JOSE object (e.g., for a Wallet Instance Attestation), the JOSE algorithm identifier is `ES256`, meaning SHA-256 with ECDSA over P-256. `ES256` is a JOSE algorithm identifier and is not an X.509 signature algorithm name.

| Certificate type | Used for | Trust anchor location | Standard |
|------------------|----------|------------------------|----------|
| PID Provider Sign/seal certificate | signing PID | PID Providers LoTE | ETSI TS 119 412-6, clause 4 |
| Wallet Provider Sign/seal certificate | one Wallet Solution's WIA, KA, and related Token Status List | Wallet Providers LoTE  | ETSI TS 119 412-6, clause 5 |
| EAA Provider Sign/seal certificate | signing EAA | MS decision | ETSI TS 119 412-6, clause 6 |
| QEAA Provider Sign/seal certificate | signing QEAA | TL | ETSI TS 119 412-6, clause 7 |
| Pub-EAA Provider Sign/seal certificate | signing  PuB-EAA | Pub-EAA Providers LoTE | ETSI TS 119 412-6, clause 8 |
| **Access certificates** ([WRPAC](../task5-participants-policies/relying_party_access_certificate.md)) | Authenticating entities to the EUDI Wallet ecosystem | WRPAC Provider LoTE | [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| **Registration certificates** ([WRPRC](../task5-participants-policies/relying_party_registration_certificate.md)) | Validating the authorization profile for entities in the EUDI Wallet ecosystem | WRPRC Provider LoTE | [ETSI TS 119 475](../references/etsi/ETSI_TS_119_475.md) |

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
| `subjectAltName` | REQUIRED. It MUST include at least one URI `GeneralName` whose value is exactly the URI of the Wallet Solution associated with the certificate. The URI MUST match the URI recorded for that Wallet Solution in the Wallet Provider's Trusted List. A missing or mismatching Wallet Solution URI is invalid. |
| `cRLDistributionPoints` | CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in [ETSI EN 319 412-1]. |
| `authorityInfoAccess` | REQUIRED. It MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.2` (`id-ad-caIssuers`) and `accessLocation` specifying at least one access location of a valid CA certificate of the issuing CA.<br><br>If OCSP is supported by the issuing CA, the extension MUST include an `AccessDescription` structure with `accessMethod` set to `1.3.6.1.5.5.7.48.1` (`id-ad-ocsp`) and `accessLocation` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in [Online Certificate Status Protocol (OCSP)](#infrastructure-trustonline-certificate-status-protocol-ocsp). |
| `qcStatements` | REQUIRED. It MUST contain a `QCStatement` structure with `statementId` set to `0.4.0.1862.1.6` (`id-etsi-qcs-QcType`).<br>The corresponding `statementInfo` MUST contain a `QcType` structure including exactly one object identifier, namely `0.4.0.194126.1.2` (`id-etsi-qct-wal`), as defined in Clause 5.2 of [ETSI TS 119 412-6]. |

Each Wallet Solution MUST have its own criptographic material and its related sign/seal certificate. The Wallet Provider MUST generate or register a distinct ECDSA P-256 key pair for each Wallet Solution and obtain a distinct sign/seal certificate for each of them. The key pair and certificate MUST NOT be reused for another Wallet Solution.

The private key corresponding to a Wallet Solution's sign/seal certificate MUST sign that solution's WIA, KA, and every Token Status List used for the WIA (`client_status`) or KA (`key_storage_status`) revocation status. These signatures MUST use `ES256`. A separate WIA, KA, or Token Status List signing key or certificate MUST NOT be used for that Wallet Solution.

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

## Certificate Signing Request Profiles

This section defines the common CSR requirements for requests for PID, Wallet, EAA, QEAA, and PuB-EAA Provider sign/seal certificates. The certificate profile selected by the provider determines the profile-specific subject, extensions, certificate policy, and QcType.

### Common CSR Profile

A provider requesting one of these sign/seal certificates MUST submit a PKCS#10 certificate signing request encoded in PEM or DER.

The CSR MUST:

1. Contain a valid PKCS#10 CSR signature that proves possession of the requested private key.
2. Use an ECDSA P-256 subject public key and an `ecdsa-with-SHA256` CSR signature.
3. Contain a subject that conforms to the applicable [ETSI EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) or [ETSI EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) base profile and matches the provider onboarding data. For a legal-person provider, the subject MUST comply with ETSI EN 319 412-3 clause 4.2.1 and include `countryName`, `organizationName`, `organizationIdentifier`, and `commonName`. Where a natural-person provider profile applies, the subject MUST comply with ETSI EN 319 412-2 clause 4.2.4.
4. Contain a PKCS#9 `extensionRequest` attribute requesting the profile-compliant `keyUsage` choice (ETSI EN 319 412-3 clause 4.3.1 for legal entities or ETSI EN 319 412-2 clause 4.3.2 for natural persons) and the `subjectAltName` values required by the requested certificate profile and provider onboarding data.

For a Wallet Provider CSR, the `subjectAltName` MUST include at least one URI `GeneralName` whose value is exactly the Wallet Solution URI supplied in [UC-03](../task1-use-cases/subtask1-1-onboarding/wallet-provider-onboarding.md) and recorded for that Wallet Solution in the Trusted List. A missing or mismatching Wallet Solution URI is invalid. The Wallet Provider key pair and certificate MUST NOT be registered or reused for another Wallet Solution.

The CA controls the issuer name, serial number, validity period, `authorityKeyIdentifier`, `subjectKeyIdentifier`, `authorityInfoAccess`, `cRLDistributionPoints`, certificate policy, and `qcStatements` of the issued certificate. The CA MUST apply the complete profile for the requested certificate type, including its profile-specific QcType.

### CSR Validation

Before issuing any PID, Wallet, EAA, QEAA, or PuB-EAA Provider sign/seal certificate, the CA MUST perform the following checks:

1. Parse the submitted object as a PKCS#10 CSR in PEM or DER encoding.
2. Verify the CSR signature using the requested subject public key.
3. Verify that the requested public key is ECDSA on P-256 and that the CSR signature uses `ecdsa-with-SHA256`. The CA MUST reject RSA keys and non-P-256 curves.
4. Identify the requested certificate profile and verify that the subject conforms to its applicable ETSI EN 319 412 base profile and matches the submitted provider data.
5. Verify that the `extensionRequest` contains the profile-compliant `keyUsage` choice and the `subjectAltName` values required by the requested certificate profile. Unsupported `keyUsage` requests MUST be rejected.
6. For a Wallet Provider CSR, compare the URI SAN exactly with the Wallet Solution URI supplied in [UC-03](../task1-use-cases/subtask1-1-onboarding/wallet-provider-onboarding.md) and recorded in the Trusted List. Reject a missing or mismatching URI and reject a key pair or certificate registered or reused for another Wallet Solution.
7. For other provider profiles, verify each profile-specific identifier and requested SAN value against the provider' service onboarding data.

If any check fails, the CA MUST reject the CSR before certificate issuance. If all checks succeed, the CA MUST issue a fresh certificate that contains all mandatory extensions in the requested certificate profile, including its profile-specific QcType where applicable.

### Non-normative OpenSSL Code Examples

The following non-normative code examples illustrate the Wallet Provider process for generating a Wallet Solution sign/seal key and CSR, verifying the CSR, and issuing its certificate. They demonstrate common P-256 mechanics; replace the subject, Wallet Solution identifier, and CA values with values from the onboarding request. The common CSR profile above applies to all five sign/seal certificate types, while these commands specifically illustrate the Wallet Provider process.

#### Generate Key Pair

```bash
openssl genpkey -algorithm EC \
  -pkeyopt ec_paramgen_curve:P-256 \
  -out wallet_solution.key
```

#### Generate CSR

```bash
openssl req -new -sha256 \
  -key wallet_solution.key \
  -out wallet_solution.csr \
  -subj "/C=DE/O=Example Wallet Provider/organizationIdentifier=VATDE-123456789/CN=Example Wallet Solution" \
  -addext "keyUsage=critical,nonRepudiation" \
  -addext "subjectAltName=URI:https://example.wallet.solution"
```

#### Inspect and Verify CSR

```bash
openssl req -in wallet_solution.csr -text -noout -verify
```

#### Illustrative Certificate Issuance

The issuing key in this example is also ECDSA P-256 and the certificate is signed with SHA-256:

```bash
openssl genpkey -algorithm EC \
  -pkeyopt ec_paramgen_curve:P-256 \
  -out issuing_ca.key

openssl req -new -x509 -sha256 \
  -key issuing_ca.key \
  -out issuing_ca.crt \
  -days 3650 \
  -subj "/C=DE/O=Example Trust Services CA/CN=Example CA"

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

The CA's `wallet_provider_ext.cnf` configuration MUST apply the complete certificate profile selected for the CSR. In particular, it MUST supply the profile-compliant `keyUsage`, the required `subjectAltName`, `certificatePolicies`, `authorityInfoAccess`, conditional `cRLDistributionPoints`, and the profile-specific `qcStatements`. For a Wallet Provider certificate, this includes the exact Wallet Solution URI and `id-etsi-qct-wal` (`0.4.0.194126.1.2`).

## Mapping to Use Cases

### UC-02: PID / Attestation Provider Onboarding

**Relevant clauses:** 4 (PID), 6 (EAA), 7 (QEAA), 8 (PSBEAA).

| Entity | Sign/seal certificate (TS 119 412-6) | Access certificate (TS 119 411-8) |
|--------|--------------------------------------|----------------------------------|
| PID Provider | Clause 4 — QcType `id-etsi-qct-pid` | [WRPAC](../task5-participants-policies/pid_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| QEAA Provider | Clause 7 — qualified cert, QTSP issuer | [WRPAC](../task5-participants-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| PuB-EAA Provider | Clause 8 — QcPSB qcStatement | [WRPAC](../task5-participants-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| EAA Provider | Clause 6 — EN 319 412-2/3 | [WRPAC](../task5-participants-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |

**PID Provider:** Certificate used to sign PID attribute attestations. It MUST be formatted as described in [PID Provider Sign/Seal Certificate](#pid-provider-signseal-certificate).

**Attestation Providers (EAA, QEAA, PuB-EAA):** Certificates used to sign attestations. These MUST be formatted as described in [(Q)EAA Provider Sign/Seal Certificate](#qeaa-provider-signseal-certificate) and [PuB-EAA Provider Sign/Seal Certificate](#pub-eaa-provider-signseal-certificate).


When OCSP/CRL is used for attestation revocation, the OCSP responder cert or CRL MUST be issued/signed by the CA issuing the respective Sign/Seal certificate.

### UC-03: Wallet Provider Onboarding

**Relevant clause:** 5 (Wallet Provider).

| Entity | Sign/seal certificate (TS 119 412-6) |
|--------|--------------------------------------|
| Wallet Provider | Clause 5 — one Wallet Solution sign/seal certificate per Wallet Solution, with URI SAN binding; QcType `id-etsi-qct-wal` |

**Wallet Provider:** Each Wallet Solution receives its own sign/seal key pair and certificate. The certificate's URI SAN is the Wallet Solution URI. The corresponding private key signs the Wallet Solution's WIA, KA, and related Token Status Lists using `ES256`. The certificate MUST be formatted as described in [Wallet Provider Sign/Seal Certificate](#wallet-provider-signseal-certificate).

### Relying Party Onboarding

**Not covered by TS 119 412-6.** Relying parties use **access certificates** ([WRPAC](../task5-participants-policies/relying_party_access_certificate.md)) per [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md), not the sign/seal profiles in TS 119 412-6. See also [Trust and Entitlement Discovery](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md) for WRPAC validation flow.

## OIDs (Annex A)

| Identifier | OID | Use |
|------------|-----|-----|
| id-etsi-qct-pid | 0.4.0.194126.1.1 | PID provider sign/seal certificate |
| id-etsi-qct-wal | 0.4.0.194126.1.2 | Wallet provider sign/seal certificate |

## Non-normative examples

The following examples illustrate the distinguishing fields of issued sign/seal certificates for each entity type. **They are non-normative** and are not CSR templates. A CSR is specified in [Certificate Signing Request Profiles](#certificate-signing-request-profiles) and [OpenSSL Commands](#openssl-commands). Conformance requires the full requirements of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) and the applicable base profiles.

### PID Provider Sign/Seal Certificate Example

The following is a non-normative example of a PID Provider Sign/Seal Certificate for legal persons.

```
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

```
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
                URI: https://wallet.example.test/solution
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
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value: BASE64(ECDSA_SIGN(issuerPrivateKey, DER(tbsCertificate)))
```
*Used to sign the WIA, KA, and related Token Status List for the example Wallet Solution.*

### EAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a EAA Provider Sign/Seal Certificate for legal persons.

```
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
            organizationIdentifier = LEIXYZ-5493001KJTIIGC8Y1R12
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
*Used to sign electronic attestations of attributes. OCSP responder cert or CRL, if used, shall be issued/signed by this cert.*

### QEAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a QEAA Provider Sign/Seal Certificate for legal persons.

```
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
            O = Example of (Q)EAA Provider
            CN = (Q)EAA Provider Example
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
*Used to sign qualified electronic attestations of attributes. Issuer shall be a QTSP.*

### PSBEAA Provider Sign/Seal Certificate Example

The following is a non-normative example of a PuB-EAA Provider Sign/Seal Certificate for legal persons.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 6F:3A:0B:91:D2:...
        Signature Algorithm: ecdsa-with-SHA256
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

### ETSI certificate profile specifications

- [ETSI TS 119 412-6 V1.1.1](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) — Provider sign/seal certificate profiles (PID, Wallet, EAA, QEAA, PSBEAA)
- [ETSI EN 319 412-2 V2.4.1](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) — Certificate profile for natural persons (base for TS 119 412-6)
- [ETSI EN 319 412-3 V1.3.1](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) — Certificate profile for legal persons (base for TS 119 412-6)
- [ETSI TS 119 412-6 PDF](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf) — official document
- [ETSI EN 319 412-2 PDF](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf) — official document
- [ETSI EN 319 412-3 PDF](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf) — official document

### WE BUILD and related specifications

- [WE BUILD CS-002: Credential Presentation](https://github.com/webuild-consortium/wp4-architecture/blob/main/conformance-specs/cs-02-credential-presentation.md#5-protocol-overview) — P-256/ES256 presentation crypto suite
- [WE BUILD CS-004: Individual Wallet Unit Attestation (WUA) Lifecycle](https://github.com/webuild-consortium/wp4-architecture/blob/main/conformance-specs/cs-04-wua-lifecycle.md#82-status--revocation-interface) — WIA/KA Token Status List requirements
- [EUDI Wallet Technical Specification TS-03](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md#25-revocation) — WIA/KA status and signature algorithm background

### Use cases

- [UC-02 PID/EAA Provider Onboarding](../task1-use-cases/subtask1-1-onboarding/pid_eaa_provider_onboarding.md)
- [UC-03 Wallet Provider Onboarding](../task1-use-cases/subtask1-1-onboarding/wallet-provider-onboarding.md)
