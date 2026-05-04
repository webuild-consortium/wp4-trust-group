# Certificate Profiles for PID, Wallet, EAA, QEAA, and PSBEAA Providers (ETSI TS 119 412-6)

This document describes the content of **ETSI TS 119 412-6** (Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers) and its relation to WP4 Trust Group use cases.

## Scope of TS 119 412-6

ETSI TS 119 412-6 specifies requirements on **end-entity certificates used by providers** to sign their outputs:

| Certificate type | Used for | Standard |
|------------------|----------|----------|
| **Sign/seal certificates** (TS 119 412-6) | PID attestations, Wallet output, EAA attestations | ETSI TS 119 412-6 |
| **Access certificates** ([WRPAC](../task5-participants-certificates-policies/relying_party_access_certificate.md)) | Authenticating entities to the EUDI Wallet | [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |

These are **different certificates** with different purposes. TS 119 412-6 applies to sign/seal certificates only.

## Profiles by Entity Type

| Entity | TS 119 412-6 Clause | QcType / Statement | Base Profile |
|-------|---------------------|-------------------|--------------|
| **PID Provider** | Clause 4 | `id-etsi-qct-pid` (0.4.0.194126.1.1) | [EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) (natural) or [EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) (legal person) |
| **Wallet Provider** | Clause 5 | `id-etsi-qct-wal` (0.4.0.194126.1.2) | Inherits 4.1–4.4 from [EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) / [EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) |
| **EAA Provider** | Clause 6 | — | [EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) or [EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) |
| **QEAA Provider** | Clause 7 | — | [EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) or [EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md); issuer shall be QTSP |
| **PSBEAA Provider** | Clause 8 | QcPSB qcStatement (legislation, authentic source) | [EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) or [EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) |

Common requirements across profiles: key usage, Subject Key Identifier, Authority Information Access (AIA). EAA/QEAA/PSBEAA add OCSP/CRL constraints for attestation revocation.

## Mapping to Use Cases

### UC-02: PID / Attestation Provider Onboarding

**Relevant clauses:** 4 (PID), 6 (EAA), 7 (QEAA), 8 (PSBEAA).

| Entity | Sign/seal certificate (TS 119 412-6) | Access certificate (TS 119 411-8) |
|--------|--------------------------------------|----------------------------------|
| PID Provider | Clause 4 — QcType `id-etsi-qct-pid` | [WRPAC](../task5-participants-certificates-policies/pid_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| QEAA Provider | Clause 7 — qualified cert, QTSP issuer | [WRPAC](../task5-participants-certificates-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| PUB-EAA Provider | Clause 8 — QcPSB qcStatement | [WRPAC](../task5-participants-certificates-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |
| Non-Q EAA Provider | Clause 6 — EN 319 412-2/3 | [WRPAC](../task5-participants-certificates-policies/eaa_provider_access_certificate.md) per [TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md) |

**PID Provider:** Certificate used to sign PID attribute attestations. Must include QcType `id-etsi-qct-pid`. Subject per [EN 319 412-2](../references/etsi/ETSI_EN_319_412-2_V2.4.1.md) (natural person) or [EN 319 412-3](../references/etsi/ETSI_EN_319_412-3_V1.3.1.md) (legal person).

**Attestation Providers (EAA, QEAA, PSBEAA):** Certificates used to sign attestations. If OCSP/CRL is used for attestation revocation, the OCSP responder cert or CRL must be issued/signed by the provider's sign/seal certificate.

### UC-03: Wallet Provider Onboarding

**Relevant clause:** 5 (Wallet Provider).

| Entity | Sign/seal certificate (TS 119 412-6) |
|--------|--------------------------------------|
| Wallet Provider | Clause 5 — QcType `id-etsi-qct-wal` |

**Wallet Provider:** Certificate used to sign the output of the Wallet provider. Must include QcType `id-etsi-qct-wal`. Inherits general requirements from clauses 4.1–4.4 (key usage, Subject Key Identifier, AIA).

### Relying Party Onboarding

**Not covered by TS 119 412-6.** Relying parties use **access certificates** ([WRPAC](../task5-participants-certificates-policies/relying_party_access_certificate.md)) per [ETSI TS 119 411-8](../references/etsi/ETSI_TS_119_411-8_V1.1.1.md), not the sign/seal profiles in TS 119 412-6. See also [Trust and Entitlement Discovery](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md) for WRPAC validation flow.

## OIDs (Annex A)

| Identifier | OID | Use |
|------------|-----|-----|
| id-etsi-qct-pid | 0.4.0.194126.1.1 | PID provider sign/seal certificate |
| id-etsi-qct-wal | 0.4.0.194126.1.2 | Wallet provider sign/seal certificate |

## Non-normative examples

The following examples illustrate the distinguishing fields of sign/seal certificates for each entity type. **They are non-normative** and intended only to aid understanding. Conformance requires the full requirements of [ETSI TS 119 412-6](../references/etsi/ETSI_TS_119_412-6_V1.1.1.md) and the applicable base profiles.

### PID Provider (legal person)

```
Subject: C=DE, O=Bundesdruckerei GmbH, organizationIdentifier=NTRDE-HRB12345, CN=German PID Issuer Service
Extensions:
  keyUsage = digitalSignature
  subjectKeyIdentifier = <hash>
  authorityInfoAccess = caIssuers;URI:http://ca.example.com/pid-ca.crt
  QCStatements:
    QcType: id-etsi-qct-pid (0.4.0.194126.1.1)
```
*Used to sign PID attribute attestations issued to the wallet.*

### Wallet Provider (legal person)

```
Subject: C=FR, O=Wallet Solutions SAS, organizationIdentifier=NTRFR-12345678, CN=French EUDI Wallet Instance
Extensions:
  keyUsage = digitalSignature
  subjectKeyIdentifier = <hash>
  authorityInfoAccess = caIssuers;URI:https://ca.example.com/wallet-ca.crt
  QCStatements:
    QcType: id-etsi-qct-wal (0.4.0.194126.1.2)
```
*Used to sign the output of the Wallet provider (e.g. wallet attestations).*

### EAA Provider (non-qualified, legal person)

```
Subject: C=ES, O=Attestation Services SL, organizationIdentifier=VATES-S2800001J, CN=Driving License Attestation
Extensions:
  keyUsage = digitalSignature
  subjectKeyIdentifier = <hash>
  authorityInfoAccess = caIssuers;URI:https://ca.example.com/eaa-ca.crt
  (no QcType — EAA profile does not require QcType)
```
*Used to sign electronic attestations of attributes. OCSP responder cert or CRL, if used, shall be issued/signed by this cert.*

### QEAA Provider (qualified, legal person)

```
Subject: C=DE, O=Qualified TSP GmbH, organizationIdentifier=NTRDE-HRB98765, CN=Qualified Attestation Service
Issuer: QTSP (qualified trust service provider per Regulation (EU) No 910/2014)
Extensions:
  keyUsage = digitalSignature
  subjectKeyIdentifier = <hash>
  authorityInfoAccess = caIssuers;URI:https://qtsp.example.com/qeaa-ca.crt, OCSP;URI:https://ocsp.qtsp.example.com
  QCStatements: QcCompliance, QcType (e.g. id-etsi-qct-eseal per qualified cert profile)
```
*Used to sign qualified electronic attestations of attributes. Issuer shall be a QTSP.*

### PSBEAA Provider (legal person)

```
Subject: C=IT, O=Ministero dell'Interno, organizationIdentifier=VATIT-12345678901, CN=Italian National ID Attestation
Extensions:
  keyUsage = digitalSignature
  subjectKeyIdentifier = <hash>
  authorityInfoAccess = caIssuers;URI:https://ca.gov.it/psbeaa-ca.crt, OCSP;URI:https://ocsp.gov.it
  QCStatements:
    QcPSB: {
      countryOfLegislation = "IT"
      authSourceIdentification = "National Civil Registry"
      legislationIdentification = "Italian ID Act Art. 5"
    }
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
