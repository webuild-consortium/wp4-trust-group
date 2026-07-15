# Use Case UC-RPI-01: Relying Party Intermediary

## Scope

An **Intermediary** is a Relying Party that requests attribute presentation from a Wallet Unit **on behalf of** another registered Relying Party (the **intermediated RP**). Typical examples: identity/interop gateways, sector platforms, or SaaS verifiers that serve multiple service providers.

This use case covers registration, intermediated remote presentation (OpenID4VP), and wallet-side trust evaluation. Protocol details and JSON examples: [RPI OpenID4VP technical report](../../task2-trust-framework/rp-intermediary-openid4vp-technical-report.md).

## Actors

| Actor | Role |
| ----- | ---- |
| **Intermediary** | Registers as RP with `isIntermediary`; holds **WRPAC**; sends presentation requests |
| **Intermediated RP** | Registered at a Registrar; may hold **WRPRC** per intended use; instructs intermediary what to request |
| **Registrar** | Registers both parties; records `usesIntermediary` relationship (RPI_04) |
| **Access CA / WRPRC Provider** | Issues WRPAC to intermediary; WRPRC to intermediated RP |
| **Wallet Unit** | Authenticates intermediary; displays both identities; evaluates intermediated RP entitlements |
| **Holder (User)** | Approves or denies presentation |

## Goal

- **Business**: Allow service providers to use a trusted third-party verifier without each holding a direct wallet connection, while keeping the User informed of **both** the technical caller and the service consuming the data.
- **Technical**: Intermediary authenticates with its WRPAC; intermediated RP identity and authorisation travel in `verifier_info`; wallet validates both per ARF Topic 52.

## Scenarios

| ID | Scenario | Intermediated? |
| -- | -------- | -------------- |
| **S1** | Interop gateway requests PID for a cinema booking service | Yes |
| **S2** | Intermediary requests attributes for its **own** service | No (direct RP) |

### S1 — Intermediated presentation (primary)

**Example:** *VerifyNow* (intermediary) requests age verification on behalf of *Example Cinema Ltd.* (intermediated RP).

**Preconditions**

- Intermediary registered with `isIntermediary: true` and valid **WRPAC**.
- Intermediated RP registered; intended use and optional **WRPRC** issued; `usesIntermediary` points to the intermediary (RPI_04).
- Intermediated RP provided the intermediary with: trade name, identifier, Registrar URL, intended-use id, attribute list, optional WRPRC reference (RPI_05).

**Main flow**

```mermaid
sequenceDiagram
    participant IRP as Intermediated RP
    participant INT as Intermediary
    participant W as Wallet Unit
    participant U as User

    IRP->>INT: Request attributes (RPI_05 metadata)
    INT->>W: OpenID4VP Request Object<br/>(INT WRPAC + IRP verifier_info)
    W->>W: Detect intermediation (RPI_07)<br/>Validate INT WRPAC + IRP WRPRC/registry
    W->>U: Show INT and IRP names; request consent
    U->>W: Approve or deny
    W->>INT: Authorization Response (response_uri)
    INT->>IRP: Forward attributes (RPI_08/09); delete after use (RPI_10)
```

1. Intermediated RP instructs the intermediary (RPI_05).
2. Intermediary builds and signs the OpenID4VP Request Object with its **WRPAC**; includes intermediated RP `registrar_dataset` and optional `registration_cert` in `verifier_info` (RPI_06, RPRC_19a).
3. Wallet detects intermediation when WRPAC `organizationIdentifier` ≠ `registrar_dataset.identifier` (RPI_07).
4. Wallet validates intermediary WRPAC (Access CA TL) and intermediated RP WRPRC/registry entitlements ([UC-TE-04](wallet-unit-evaluates-relying-party.md)).
5. Wallet displays **both** trade names; User approves (RPA_07).
6. If User opted to verify registration, Wallet checks intermediary–RP relationship via WRPRC `intermediary` field (RPRC_04) or Registrar API (RPI_07a).
7. Wallet sends response to intermediary `response_uri`; intermediary forwards to intermediated RP.

**Postconditions (success)**

- User saw both intermediary and intermediated RP before consent.
- Attributes disclosed only match intermediated RP registered entitlements (RPRC_21).
- Intermediary deletes received credentials immediately after forwarding (RPI_10).

### S2 — Intermediary as direct Relying Party

An entity registered as intermediary may also act **in its own capacity** (RPI_01 note c): WRPAC and `verifier_info` refer to the **same** party. Flow matches [UC-TE-04](wallet-unit-evaluates-relying-party.md) without dual-identity handling.

## Onboarding (summary)

Detailed steps: [Relying Party Onboarding](../subtask1-1-onboarding/relying_party_onboarding.md).

| Step | Intermediary | Intermediated RP |
| ---- | ------------ | ---------------- |
| Register | As RP with `isIntermediary: true` (RPI_01, Reg_26) | At Registrar in establishment MS (RPI_03) |
| Relationship | — | Provide evidence of intermediary use; Registrar sets `usesIntermediary` (RPI_04) |
| Certificates | **WRPAC** (mandatory); own WRPRC only for direct use (S2) | **WRPRC** per intended use; includes `intermediary` association (RPRC_04) |
| Registry API | May register intended uses on behalf of WRP ([TS5 notes](../../task5-participants-certificates-policies/ts5-registry-api-and-data-formats.md)) | — |

**Note:** Intermediated RPs do **not** need a WRPAC (ARF §6.6.5).

## Wallet evaluation checklist

| Check | Source | Applies to |
| ----- | ------ | ---------- |
| WRPAC chain + revocation | Access CA TL | Intermediary |
| WRPRC signature + entitlements | WRPRC Provider TL / registry | Intermediated RP |
| Requested attributes ⊆ registered | RPRC_21 | Intermediated RP |
| Dual identity displayed | RPI_07 | Both |
| Relationship registered | RPI_07a, RPRC_04 | Intermediary ↔ IRP |
| EDP (if present) | EDP_02/03 | Evaluate against **intermediated** RP id/root, not intermediary WRPAC |

## Success criteria

- Intermediary authenticated via valid WRPAC.
- Intermediated RP identity and entitlements verified (WRPRC or registry).
- User informed of both parties before consent.
- Intermediated transaction does not expose intermediary WRPRC in `verifier_info`.

## ARF requirements (key)

| ID | Summary |
| -- | ------- |
| RPI_01 | Intermediary registers as RP; obtains WRPAC |
| RPI_03 | Intermediary registers each intermediated RP |
| RPI_04 | Registrar verifies and records intermediary relationship |
| RPI_05 | Intermediated RP supplies request metadata to intermediary |
| RPI_06 | Intermediary sends request with own WRPAC + IRP data/WRPRC |
| RPI_07 | Wallet detects and displays both identities |
| RPI_07a | Wallet verifies registered relationship when User requests |
| RPI_08–10 | Forwarding, verification, immediate deletion by intermediary |
| RPRC_04 | Intermediated WRPRC contains intermediary association |
| RPRC_19a | Registration data in presentation request extension |

Full matrix: [Trusted List / Registration / Trust Evaluation Matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md) §7.

## Out of scope (this use case)

- Proximity presentation (ISO 18013-5 / TS 119 472-2 clause 5.3) — see technical report §12
- Architecture-group implementation scenario variants ([architecture PR #31](https://github.com/webuild-consortium/architecture/pull/31))

## References

- [Consolidated Terms — Intermediary](../terms-and-entities.md#316-intermediary)
- [RPI OpenID4VP technical report](../../task2-trust-framework/rp-intermediary-openid4vp-technical-report.md)
- [EUDI Wallet Trust and Entitlement Discovery](../../task2-trust-framework/eudi-wallet-trust-and-entitlement-discovery.md)
- [WRPRC Example 3 — With Intermediary](../../task5-participants-policies/relying_party_registration_certificate.md)
- [Embedded Disclosure Policies](../../task5-participants-policies/embedded-disclosure-policies-implementation.md)
- [ARF Topic 52 — Relying Party intermediaries](https://eudi.dev/2.9.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2330-topic-52-relying-party-intermediaries)
