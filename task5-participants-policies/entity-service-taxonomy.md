# Entity and Service Taxonomy

This document defines how **entity categories** and **service classification** work in WP4 onboarding. It complements — but does not replace — the EU-normative identifiers in [EUDI Wallet Trust and Entitlement Discovery](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md) and the entitlement profiles in [RP](relying_party_registration_certificate.md) and [EAA provider](eaa_provider_registration_certificate.md) registration certificate examples.

## Two-layer model

| Layer | Purpose | Examples | Primary consumers |
| ----- | ------- | -------- | ----------------- |
| **Layer 1 — EU normative** | Trust, interoperability, attribute allow-lists | ETSI `LoTEType` / `SvcType` URIs; TS 119 475 entitlements (`Service_Provider`, `QEAA_Provider`, …); sub-entitlements (e.g. PSP) | Wallets, WRPRC validation, Trusted Lists |
| **Layer 2 — Domestic (MS)** | Registrar policy, sector routing, onboarding vetting | ATECO (Italian NACE Rev.2), other national NACE variants; optional UN CPC codes | Registrars, sector registers, policy templates |

Wallets **must** evaluate Layer 1 (entitlements and registered attributes per ARF RPRC_21). Layer 2 supports Registrar decisions and may be shown to users for context; it does **not** override WRPRC entitlements.

## Layer 1 — already documented elsewhere

Do not duplicate Layer 1 here. Use:

- [Entity Type Classification Identifiers](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md#12-entity-type-classification-identifiers) — LoTEType and SvcType for TL-listed actors
- [Common Entitlements](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md#351-common-entitlements-oid-and-uri) — TS 119 475 entitlement URIs
- [EAA provider taxonomy](../task2-trust-framework/eaa-provider-identity-verification-chaining-LoTL.md#2-eaa-provider-taxonomy) — QEAA / Non-Q / PuB-EAA classes
- [Multi-register architecture](../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md#242-multiple-register-architecture) — national and sectoral registers

**Rule:** Custom `TrstSvc/Svctype/...` labels are not used as normative identifiers. Relying Parties are not classified via new Trusted List service types.

## Layer 2 — domestic classification

### Economic activity (ATECO / NACE)

- **ATECO** — Italian implementation of **NACE Rev.2** (Classificazione delle attività economiche).
- **Use:** Categorise the legal entity's primary economic activity during onboarding; select sector policy templates; route to sector registers where applicable.
- **Examples:**
  - `62.01.00` — Software development (general RP; see [auth framework Use Case 5](../task2-trust-framework/authentication-authorization-policy-framework.md#use-case-5-relying-party-with-ateco-classification))
  - `86.10.00` — Hospital activities (healthcare RP; subtractive policy example in [Use Case 6](../task2-trust-framework/authentication-authorization-policy-framework.md#use-case-6-healthcare-relying-party-ateco-861000))

### Service product (CPC, optional)

- **CPC** — UN Central Product Classification; classifies goods and services (including digital services).
- **Use:** Optional refinement of the **service** offered (alongside `srvDescription` and `intendedUse`), mainly for Registrar analytics and sector templates — not for wallet trust decisions.

### Public vs. private sector

- **Layer 1:** `isPSB` / `public_body` flag and entitlements (e.g. `PUB_EAA_Provider`).
- **Layer 2:** NACE division **O** (public administration) or MS-specific public-sector registers where applicable.

## Mapping Layer 1 ↔ Layer 2

| Layer 1 entitlement | Typical Layer 2 inputs | Notes |
| ------------------- | ---------------------- | ----- |
| `Service_Provider` | Any private-sector ATECO/NACE code | Default RP; one entitlement, many activity codes |
| `Service_Provider` + PSP sub-entitlements | Financial services ATECO (e.g. 64.x, 66.x) | Sector register may require both |
| `QEAA_Provider` / `Non_Q_EAA_Provider` / `PUB_EAA_Provider` | Activity code in issuing sector | Provider class fixed by entitlement |
| `PID_Provider` | Usually public-sector or designated MS authority | Vetted at registration |

## Registry data (pilot)

Optional fields in the [RP onboarding registry data model](../task1-use-cases/subtask1-1-onboarding/relying_party_onboarding.md#registry-data-model):

```json
{
  "economicActivity": [{
    "scheme": "NACE",
    "version": "Rev.2",
    "code": "62.01",
    "nationalScheme": "ATECO",
    "nationalCode": "62.01.00"
  }],
  "serviceClassification": [{
    "scheme": "CPC",
    "version": "2.1",
    "code": "8314"
  }]
}
```

Member States may require these fields in national registration policy. They are stored in the TS5 registry ([TS5 data model notes](../task5-participants-certificates-policies/ts5-registry-api-and-data-formats.md)); inclusion in WRPRC is a national certificate-policy choice.

## Governance

| Phase | Maintainer | Publication |
| ----- | ---------- | ----------- |
| **MVP (pilot)** | WP4 Trust Infrastructure group | Pilot registry / Onboarding API |
| **MVP+** | Member State Registrars | TS5 REST API (JWS-signed JSON) per CIR 2025/848 |
| **EU Layer 1** | European Commission | LoTE profiles, credential catalogues, LoTL |

## Related policy work

Domestic classification selects **policy templates** applied at registration (allowed attributes in WRPRC `credentials`, or optional subtractive rules). See [policy approaches](policy-approaches-definition.md) and [issue #2 resolution](issue-2-resolution.md).
