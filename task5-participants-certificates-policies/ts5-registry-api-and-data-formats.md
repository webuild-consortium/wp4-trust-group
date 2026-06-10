# TS5: Common Formats and API for Relying Party Registration Information

This note summarises **Technical Specification 5 (TS5)** from the European Commission’s EUDI Wallet standards package: the **machine-readable data model** and **Registrar REST API** for **wallet-relying party** registration. It aligns national registry publication with **ARF** requirements (e.g. registry transparency, **Reg_06**, **Topic 27**) and the **CIR (EU) 2025/848** rules on registers.

## Normative references

| Reference | Description |
|-----------|-------------|
| [TS5 – Common formats and API for RP registration](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) | Prose specification, API behaviour, data model narrative |
| [TS5 – JSON Schema (Annex A.1)](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/api/ts5-json-common-rp-data-model.json) | Normative **`WalletRelyingParty`** JSON structure |
| [TS5 – OpenAPI 3.1](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/api/ts5-openapi31-registrar-api.yml) | Normative HTTP operations and **JWS** response wrapper |
| [TS6 – Common set of RP information to be registered](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md) | Minimum registration dataset (CIR Annex I alignment) |
| [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32025R0848) | Implementing act on wallet-relying party registration |

## Purpose in the trust architecture

- **Member State Registrars** publish PID Providers, Attestation Providers, and **Relying Parties** in a national registry.
- **Wallet units** use the Registrar’s online service (among other sources) to verify registration and **intended uses** (e.g. attributes requested, purposes, policies), especially when **registration certificates** are not used or are insufficient.
- **Relying parties** are **not** published on EU/Member State **Trusted Lists** in the same way as QTSPs; **TS5** is the primary **interoperable machine interface** for RP registration data, alongside sealed human-readable publication.

TS5 requires:

- **REST** API, **JSON** payloads, OpenAPI 3.x description.
- **Read** endpoints: **open** access over a secure channel (no client authentication required); implementers should apply rate limiting, caching, and DDoS mitigations as described in TS5.
- **Write** endpoints (`POST` / `PUT` / `DELETE` on `/wrp`): **authenticated and authorised** clients only; national choice of mechanism, documented in the OpenAPI `securitySchemes`.
- Successful **read** responses: payload integrity via **JWS** (JWT in compact serialization), as specified in the OpenAPI annex.

## API surface (read path)

Typical **public** operations:

| Method | Path | Role |
|--------|------|------|
| `GET` | `/wrp` | Search or list **WalletRelyingParty** instances (query filters; empty query may return full list with pagination). |
| `GET` | `/wrp/{identifier}` | Return one **WalletRelyingParty** by identifier. |
| `GET` | `/wrp/check-intended-use` | Return a **boolean** result (`isRegistered`) whether a given RP / intended-use / credential / claim / policy URL matches registered **IntendedUse** data. |

**Response format:** `Content-Type: application/jwt` — verify signature using registry keys (OpenAPI describes `x-jku-url` for JWKS).

### JWS payload wrappers (OpenAPI)

After signature verification, decode the JWT payload:

- **List / search (`GET /wrp`):** `iss`, `iat`, **`data`** array of `WalletRelyingParty`, optional **`pagination`** (`next_cursor`, `has_next_page`).
- **Single (`GET /wrp/{identifier}`):** `iss`, `iat`, **`data`** as one `WalletRelyingParty` object.
- **Check (`GET /wrp/check-intended-use`):** `iss`, `iat`, **`data`** with `isRegistered` (boolean) and optional `details` (string).

## Data model essentials (Annex A.1)

The root type combines **Provider** + **LegalEntity** (via `allOf`) with WRP-specific fields. Practitioners should validate instances against **`ts5-json-common-rp-data-model.json`** (note: the file may be UTF-16 encoded in the repository).

Notable WRP-specific attributes:

- **`entitlements`**: array of entitlement URIs (ETSI / CIR roles, e.g. `Service_Provider`, attestation-provider entitlements).
- **`intendedUse`**: zero or more **IntendedUse** objects (service providers declare purposes, policies, and requestable attestations; intermediaries may have none).
- **`supportURI`**: **array** of strings (contact / support; data-deletion-related URI strongly recommended per TS5).
- **`srvDescription`**: array of **arrays** of `MultiLangString` (localised service descriptions).
- **`supervisoryAuthority`**: DPA contact (name, country, email / phone / form URI — at least one contact path expected in practice).
- **`registryURI`**: URI of the national registry API for this wallet-relying party (assigned by the Registrar).
- **`isPSB`**, **`isIntermediary`**, optional **`usesIntermediary`**, optional **`providesAttestations`** for issuers.

Each **IntendedUse** (Annex A.1) includes:

- **`purpose`**: `MultiLangString` array (min one).
- **`privacyPolicy`**: single **`Policy`** object in the **JSON Schema** (`policyURI`, `type`).
- **`intendedUseIdentifier`**, **`createdAt`**, optional **`revokedAt`**.
- **`credentials`**: array (min one per `IntendedUse` when present) of **Credential** objects.

Each **Credential**:

- **`format`**, **`meta`** (schema types as **string** in JSON Schema — often a stringified JSON metadata object per format).
- **`claims`**: array (min one) of **Claim** objects with **`path`** (TS5 describes path semantics aligned with OpenID4VP; the schema types `path` as string).

## Illustrative example (JWT payload only, Annex A.1–oriented)

This example is **illustrative**. It uses field names from **Annex A.1** (`credentials`, `claims`, `privacyPolicy` as a **single** object). Replace URLs, identifiers, and `meta` with catalogue- and MS-specific values.

```json
{
  "iss": "https://registry.example-ms.eu/eudi",
  "iat": 1743168000,
  "data": [
    {
      "identifier": [
        {
          "identifier": "EUID-EXAMPLE-0123456789",
          "type": "http://data.europa.eu/eudi/id/EUID"
        }
      ],
      "country": "NL",
      "legalPerson": {
        "legalName": ["Example Payments B.V."]
      },
      "policy": [],
      "entitlements": [
        "https://uri.etsi.org/19475/Entitlement/Service_Provider"
      ],
      "isPSB": false,
      "isIntermediary": false,
      "registryURI": "https://registry.example-ms.eu/eudi",
      "supportURI": [
        "https://pay.example.nl/support",
        "https://pay.example.nl/privacy/data-deletion"
      ],
      "srvDescription": [
        [
          { "lang": "en", "content": "Payment initiation and account information services." },
          { "lang": "nl", "content": "Betaalinitiatie- en rekeninginformatiediensten." }
        ]
      ],
      "supervisoryAuthority": {
        "name": "Autoriteit Persoonsgegevens",
        "country": "NL",
        "formURI": ["https://www.autoriteitpersoonsgegevens.nl/"]
      },
      "intendedUse": [
        {
          "intendedUseIdentifier": "iu-2026-0007",
          "createdAt": "2026-01-15",
          "purpose": [
            {
              "lang": "en",
              "content": "Strong customer authentication and compliance checks for payment services (contractual necessity)."
            }
          ],
          "privacyPolicy": {
            "type": "Privacy Statement",
            "policyURI": "https://pay.example.nl/privacy/payments"
          },
          "credentials": [
            {
              "format": "dc+sd-jwt",
              "meta": "{\"vct\":\"urn:example:pid-person\"}",
              "claims": [
                { "path": "[\"credentialSubject\",\"family_name\"]" }
              ]
            }
          ]
        }
      ],
      "providesAttestations": []
    }
  ],
  "pagination": {
    "has_next_page": false,
    "next_cursor": null
  }
}
```

## Validation and specification alignment

When declaring **conformance**, teams should:

1. **Validate `WalletRelyingParty` JSON** against **`ts5-json-common-rp-data-model.json`** (Annex A.1).
2. **Validate HTTP** against **`ts5-openapi31-registrar-api.yml`**, including **JWS** handling.

**Known inconsistencies** (as of maintenance of this note; check upstream for updates):

- **Property names:** Annex A.1 uses **`credentials`** and **`claims`**. The published OpenAPI component names sometimes use **`credential`** / **`claim`** — implementations should **not** treat the OpenAPI schema fragment as overriding Annex A.1 for instance data until the Commission publishes a single aligned release.
- **`privacyPolicy`:** TS5 **narrative** describes an **array** of policies; **Annex A.1** references a **single** `Policy` object. Prefer **Annex A.1** for JSON Schema validation; follow MS/registry guidance if the narrative interpretation is adopted nationally.
- **`Claim.path`:** The schema types `path` as a string while the description refers to path structure per OpenID4WP — agree encoding (string vs JSON array) with your registry and test vectors.

## Relation to Task 5 certificates

**TS5** complements **ETSI TS 119 475**-oriented **Relying Party Access / Registration Certificates** documented in this folder (`relying_party_access_certificate.md`, `relying_party_registration_certificate.md`). Registry data feeds user-facing **authorization decisions** and wallet-side checks; certificates and TS5 together satisfy CIR and ARF transparency and verification goals.

---

*This document is informative for the WP4 Trust Group. For authoritative requirements, use the Commission’s TS5/TS6 publications and the CIR linked above.*
