# Use Case UC-TE-03: Credential Issuer Evaluates Wallet Unit (Before Issuance)

## Scope

Before issuing a **PID** or an **attestation (EAA)**, the **PID Provider** or **Attestation Provider** evaluates the Wallet Unit by verifying **Wallet Unit Attestations (WUA)** — specifically the **Wallet Instance Attestation (WIA)** and, where applicable, the **Key Attestation (KA)**. The provider ensures the request comes from a Wallet Unit whose Wallet Provider is listed in the **Wallet Provider LoTE** with **valid entity status** (not Invalid), and that the Wallet Instance and WSCD/keystore referenced in the attestations are **not revoked**.

## Actors

- **Primary**: Credential Issuer (PID Provider or Attestation Provider)
- **Secondary**: Holder (User using the Wallet Unit), Wallet Unit (presents WIA and KA), Wallet Provider LoTE (and LoTL for discovery)

## Goal

- **Business**: Issue credentials only to Wallet Units bound to a notified, trusted Wallet Provider.
- **Technical**: Authenticate and validate the WIA (and KA where device-bound) using trust anchors from the Wallet Provider LoTE; verify the Wallet Instance and WSCD/keystore are not revoked (Topic 38).

## Preconditions

- Credential Issuer has (or can obtain) the Wallet Provider LoTE(s) it needs (ISSU_19, ISSU_28).
- Wallet Unit presents a valid WIA in the issuance flow; for PID issuance and device-bound attestations, the Wallet Unit also presents a KA (ARF Topic 9, [TS3 V1.5](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md)).

## Main Flow (Short)

1. Holder initiates issuance; the Wallet Unit presents its **WIA** (and **KA** for PID issuance or device-bound attestations) to the Credential Issuer.
2. **Trust anchors**: Credential Issuer accepts trust anchors from the **Wallet Provider LoTE** (ISSU_19 for PID Provider, ISSU_28 for Attestation Provider).
3. **WIA validation (all issuance)**: Credential Issuer authenticates and validates the WIA using trust anchor(s) from the Wallet Provider LoTE; verifies the **Wallet Instance** referenced in the WIA has not been revoked (ISSU_21, ISSU_30a; Topic 38).
4. **KA validation (PID and device-bound attestations)**: Credential Issuer authenticates and validates the KA using trust anchor(s) from the Wallet Provider LoTE; verifies the **WSCD or keystore** referenced in the KA has not been revoked (ISSU_21, ISSU_30; Topic 38).
5. **Entity status**: Credential Issuer uses only Wallet Provider LoTE entries with valid status (not Invalid; GenNot_05).
6. If any check fails: reject the issuance request (the Wallet Unit informs the User of the reason). If all checks pass, proceed with issuance.

## Success Criteria

- Only Wallet Providers that appear in the Wallet Provider LoTE with valid status (not Invalid) are accepted.
- WIA and KA (where applicable) signature validation succeed; Wallet Instance and WSCD/keystore revocation checks pass before issuance.

## ARF Requirements (Key)

| Identifier | Requirement |
|------------|-------------|
| ISSU_19   | PID Provider SHALL accept trust anchors in the Wallet Provider LoTE(s) it needs for WIA and KA verification. |
| ISSU_21   | PID Provider SHALL verify the Wallet Unit's WIA and KA using a trust anchor in the Wallet Provider LoTE; verify Wallet Instance and WSCD not revoked. |
| ISSU_28   | Attestation Provider SHALL accept trust anchors in the Wallet Provider LoTE for WIA and KA verification. |
| ISSU_30   | Attestation Provider SHALL verify the KA (device-bound attestations) using a trust anchor in the Wallet Provider LoTE; verify WSCD/keystore not revoked. |
| ISSU_30a  | Attestation Provider SHALL verify the WIA (all attestations) using a trust anchor in the Wallet Provider LoTE; verify Wallet Instance not revoked. |
| GenNot_05 | Suspended/cancelled Wallet Providers have status Invalid in LoTE; Credential Issuer SHALL use only valid-status entries. |

## References

- **Terminology**: [Consolidated Terms and Entity Definitions](../terms-and-entities.md)
- [Trust evaluation base](trust-evaluation-base.md), [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation), [Trusted list / trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md)
