# Minimal Set of Attributes for WRP Registration in WE BUILD

## Introduction

This document defines the minimal set of attributes to be collected when registering a Wallet Relying Party (WRP) in the WE BUILD trust registry. The attribute set covers all data required to:

- record the WRP entry in the registry and expose it through the public API
- issue a Wallet Relying Party Access Certificate (WRPAC)
- issue a Wallet Relying Party Registration Certificate (WRPRC) 

For WRPs that also hold a provider role, the document additionally covers the attributes required to publish the entity's trust anchor on a Trusted List. 

For practical reasons, in the WE BUILD pilot all attributes required for provider registration can be collected in a single onboarding interaction and used to populate both the Registry and a TL, avoiding the need for separate data collection processes. This streamlines the process as more than a single party in the pilot provides TLs, Registry, and CAs.

In addition to describing the attribute set, this document serves as an implementation guidance for conducting the first onboarding of WRPs into the WE BUILD pilot trust registry infrastructure. 

Assuming the staged rollout of registry infrastructure the document contains examples from the simplest registration case (service provider) to more complex cases (provider registered by an intermediary).

---

## Attribute Destinations

Attributes below are labeled with the following destination keys to reflect why we are collecting them.

| Label | Artefact |
|---|---|
| **WRPAC** | Wallet Relying Party Access Certificate  |
| **WRPRC** | Wallet Relying Party Registration Certificate  |
| **API** | Registry REST API  |
| **TL** | A trusted List |

---

## Section 1 — Entity Identity _(always mandatory)_

> A single legal entity may register multiple Wallet Relying Parties. Entity identity data collected in this section is shared across all WRP registrations belonging to the same entity and does not need to be re-submitted for each.

### 1 · Legal name `legalName`
**Destinations:** WRPAC · WRPRC · API · TL
**Mandatory:** Always

Official name as it appears in the national business register.

```
xyzexamplecompany.de GmbH
```

---

### 2 · Trade / service name `tradeName`
**Destinations:** WRPAC · WRPRC · API · TL
**Mandatory:** Always

User-facing name shown in the wallet UI.

```
xyzexamplecompany.de
```

---

### 3 · Official identifier `identifier`
**Destinations:** WRPAC · WRPRC · API · TL
**Mandatory:** Always

At least one identifier SHALL be an EUID (from BRIS) where available. Use an MS-specific scheme if EUID is not available.

Format: `<CountryCode>/<MS-Code>/<NationalID>`

| Scheme | Example |
|---|---|
| EUID (preferred) | `EU/DE/HRB123456` |
| VAT (fallback) | `DE123456789` |
| LEI (fallback) | `549300ABCDEF123456` |

---

### 4 · Physical address `postalAddress`
**Destinations:** TL
**Mandatory:** Always

Provided to the Registrar. **Excluded from the API response** (CIR Annex II). Included in the Trusted List TSP entry.

```
XYZ Street 1, 10117 Dublin, IE
```

---

### 5 · Info URI `infoURI`
**Destinations:** WRPAC · WRPRC · API · TL
**Mandatory:** Always

Web page belonging to the RP.

```
https://www.xyzexamplecompany.de/about
```

---

### 6 · Country `country`
**Destinations:** WRPAC · WRPRC · API · TL
**Mandatory:** Always

One of ISO 3166-1 compliant entries

```
AT · BE · BG · CY · CZ · DE · DK · EE · ES · FI
FR · GR · HR · HU · IE · IT · LT · LU · LV · MT
NL · PL · PT · RO · SE · SI · SK
```

---

## Section 2 — Contact

### 7 · Email `email`
**Destinations:** WRPAC · WRPRC · API · TL
**Mandatory:** Always

```
support@xyzexamplecompany.de
```

---

## Section 3 — Service & Entitlement _(always mandatory)_

### 8 · Service description `srvDescription`
**Destinations:** WRPRC · API
**Mandatory:** Always

Localised human-readable description of the service.

```
xyzexamplecompany.de provides an age and identity verification service enabling online
retailers to confirm user eligibility for age-restricted products in
compliance with EU and national regulations.
```

---

### 9 · Public sector body flag `isPSB`
**Destinations:** WRPRC · API
**Mandatory:** Always

Select one:

```
☐  false  — private entity (default)
☐  true   — public sector body
```

---

### 10 · Entitlement(s) `entitlements`
**Destinations:** WRPRC · API
**Mandatory:** Always

Select one or more ETSI TS 119 475 URIs. `Service_Provider` must always be included, even when provider entitlements are also selected.

| URI | Role | 
|---|---|
| `https://uri.etsi.org/19475/Entitlement/Service_Provider` | RP |
| `https://uri.etsi.org/19475/Entitlement/QEAA_Provider` | QEAA Issuer |
| `https://uri.etsi.org/19475/Entitlement/EAA_Provider` | EAA Issuer |
| `https://uri.etsi.org/19475/Entitlement/PID_Provider` | PID Issuer |
| `https://uri.etsi.org/19475/Entitlement/PuB_EAA_Provider` | PuB-EAA Issuer |
---

## Section 4 — Per Intended Use _(cardinality: 1..N per registration)_

> Intended Use has a **one-to-many** relationship with the RP registration. One registration can have any number of intended use records — one per service scenario (e.g. age verification, KYC, diploma issuance). **Required for providers too** — providers declare the data they request from the wallet during the issuance process (e.g. PID claims verified before issuing a QEAA).

---

### 11 · Purpose `IntendedUse.purpose`
**Destinations:** WRPRC · API
**Mandatory:** Always (per intended use)

GDPR-style purpose statement, localised.

```
To verify that the user is 18 years of age or older ...
```

---

### 12 · Data requested `IntendedUse.credentials`
**Destinations:** WRPRC · API
**Mandatory:** Always (per intended use)

One record per credential type requested. Each record contains:

**`format`** — select one:

| Value | Description |
|---|---|
| `vc+sd-jwt` | SD-JWT Verifiable Credential |
| `mso_mdoc` | ISO 18013-5 mdoc |
| `jwt_vc_json` | JWT VC JSON |

**`vct` / `doctype`** — credential type identifier. Common EUDI types:

| Value | Credential |
|---|---|
| `eu.europa.ec.eudi.pid.1` | Person Identification Data |
| `eu.europa.ec.eudi.mdl.1` | Mobile Driving Licence |
| `eu.europa.ec.eudi.iban.1` | IBAN attestation |
| `eu.europa.ec.eudi.diploma.1` | Education credential |
| `eu.europa.ec.eudi.ehic.1` | European Health Insurance Card |
| `eu.europa.ec.eudi.tax.1` | Tax number |

**`claims`** — list of claim paths requested:

```
age_over_18
family_name, given_name, birth_date
iban
```

---

### 13 · Privacy policy URL `IntendedUse.privacyPolicy`
**Destinations:** WRPRC · API
**Mandatory:** Always (per intended use)

Mandatory in the WRPRC per Article 8.2(g), even though not listed in Annex I of CIR 2025/848.

```
https://xyzexamplecompany.de/legal/privacy-policy
```

---

### 14 · Supervisory authority / DPA `supervisoryAuthority`
**Destinations:** WRPRC · API
**Mandatory:** Always (per intended use)

```
Name:    Berliner Beauftragte für Datenschutz und Informationsfreiheit
Country: DE
Email:   mailbox@datenschutz-berlin.de
```

---

## Section 5 — Intermediary _(conditional)_

### 15 · Intermediary details `usesIntermediary`
**Destinations:** WRPRC · API
**Mandatory:** Conditional — only if the RP relies on an intermediary to forward presentation requests

One record per intermediary, each containing:

```
identifier  — EU/DE/HRB987654
tradeName   — TrustBridge GmbH
registryURI — https://registry.trustbridge.eu/wrp
```

---

### 16 · Is-intermediary flag `isIntermediary`
**Destinations:** WRPRC · API
**Mandatory:** Conditional — only if the RP acts as an intermediary for other RPs

Select one:

```
☐  false  — not acting as intermediary (default)
☐  true   — this entity acts as intermediary for other RPs
```

---

## Section 6 — Provider / Issuer _(conditional)_

> Ask attribute 17 only when a provider entitlement is selected in attribute 10 (QEAA, EAA, PID, or PuB-EAA).

### 17 · Attestation types provided `providesAttestations`
**Destinations:** WRPRC · API
**Mandatory:** Conditional — only when a provider entitlement is present

List each credential type this entity is authorised to issue:

```
eu.europa.ec.eudi.qeaa.diploma.1
eu.europa.ec.eudi.pid.1
eu.europa.ec.eudi.iban.1
```

---

## Section 7 — Trusted List _(conditional)_

> Ask attributes T1–T7 only when a provider/issuer entitlement is present (Section 6). These attributes are **outside Annex I scope** and are collected exclusively to publish the provider's trust anchor on the national Trusted List per ETSI TS 119 612.

---

### T1 · CA certificate chain `serviceDigitalIdentity`
**Destinations:** TL
**Mandatory:** Conditional

Upload PEM or DER file containing the full chain: leaf → intermediate → root. Key algorithm and validity are read from the uploaded file.

```
Format:   PEM or DER
Content:  Full certificate chain — leaf → intermediate → root

Example subject DN:
  C=DE, O=xyzexamplecompany.de GmbH,
  CN=xyzexamplecompany.de Attestation Root CA
```

---

### T2 · Issuer metadata URL `serviceSupplyPoints`
**Destinations:** TL
**Mandatory:** Conditional

OpenID4VCI well-known endpoint. Wallets fetch this URL to discover credential and token endpoints automatically.

```
https://issuer.xyzexamplecompany.de/.well-known/openid-credential-issuer
```

---

### T3 · Status list endpoint(s) `serviceSupplyPoints`
**Destinations:** TL
**Mandatory:** Conditional

One URI per credential type or status list instance.

```
OAuth Status List:     https://issuer.xyzexamplecompany.de/status/credentials/v1
Bitstring Status List: https://issuer.xyzexamplecompany.de/status/bsl/v1
```

---

### T4 · Accrediting authority `supervisoryBody`
**Destinations:** TL
**Mandatory:** Conditional

The body that granted the issuer entitlement. Different from the DPA in attribute 14.

```
Name:    Bundesnetzagentur
Country: DE
Contact: info@bundesnetzagentur.de
```

---

### T5 · Authorisation reference `accreditationRef`
**Destinations:** TL
**Mandatory:** Conditional

```
Reference number: BNetzA-QEAA-2024-001234
Date of decision: 2024-03-15
```

---

### T6 · EC notification status `ecNotified`
**Destinations:** TL
**Mandatory:** Conditional (mandatory for PID Providers and QEAA issuers)

Has this provider been notified to the European Commission under eIDAS Article 45d / 45e?

```
☐  true     — notified
☐  false    — not yet notified
☐  pending  — notification submitted, awaiting confirmation
```

---

### T7 · Schema URI (per credential type) `serviceInfoExtensions`
**Destinations:** TL
**Mandatory:** Conditional

One URI per credential type listed in attribute 17.

```
Credential type: eu.europa.ec.eudi.qeaa.diploma.1
Schema URI:      https://credentials.xyzexamplecompany.de/schemas/diploma-v1.json

Credential type: eu.europa.ec.eudi.pid.1
Schema URI:      https://schema.eudi.eu/pid/1.0/pid-type-metadata.json
```

---

## Notes

- **Attribute 4 (physical address)** is collected but excluded from the API response. It is goint to be published in the Trusted List TSP entry.
- **Attribute 7 (email)** is the sole contact channel collected. We ignore other options like mobile phone. It is goin to be used as identifier of an administrator when accessing the registry.
- **Attribute 13 (privacy policy URL)** not a must have for technical reasonas, but it is mandatory in the WRPRC.
- **Section 7 (T1–T7)** These attributes are collected exclusively to publish the provider's trust anchor on a TL.

## Examples

### Example A - Relying Party / Service Provider - Minimalistic Registration
<pre>
Legal name: XYZ Example Company GmbH
Trade name: xyzexamplecompany.de
Official identifier: EU/DE/HRB654321
Physical address: Unter den Linden 1, 10117 Berlin, DE
Info URI: https://www.xyzexamplecompany.de/about
Country: DE
Email: support@xyzexamplecompany.de
Service description: xyzexamplecompany.de provides an age and identity verification service ...
Is public sector body: false
Entitlements: https://uri.etsi.org/19475/Entitlement/Service_Provider
</pre>

### Example B — Relying Party / Service Provider - Single Intended Use
<pre>
Legal name: XYZ Example Company GmbH
Trade name: xyzexamplecompany.de
Official identifier: EU/DE/HRB654321
Physical address: Unter den Linden 1, 10117 Berlin, DE
Info URI: https://www.xyzexamplecompany.de/about
Country: DE
Email: support@xyzexamplecompany.de
Service description: xyzexamplecompany.de provides an age and identity verification service ...
Is public sector body: false
Entitlements: https://uri.etsi.org/19475/Entitlement/Service_Provider

--- Intended Use 1 ---
Purpose: To verify that the user is 18 years old ...
Credential format: vc+sd-jwt
Credential type: eu.europa.ec.eudi.pid.1
Claims requested: age_over_18
Privacy policy URL: https://xyzexamplecompany.de/legal/privacy-policy
DPA name: Berliner Beauftragte für Datenschutz und Informationsfreiheit
DPA country: DE
DPA email: mailbox@datenschutz-berlin.de
</pre>

### Example C — Provider / Issuer
TBD 

### Example D — Intermediary
TBD

### Example E — Reling Party / Service Provider Using an Intermediary
TBD

### Example F — Provider / Issuer Using an Intermediary
TBD


