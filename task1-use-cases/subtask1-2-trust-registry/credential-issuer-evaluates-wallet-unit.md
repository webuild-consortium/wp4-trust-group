# Use Case UC-TE-03: Credential Issuer Evaluates Wallet Unit (Before Issuance)

## Scope

Before issuing a **PID** or an **attestation (EAA)**, the **PID Provider** or **Attestation Provider** evaluates the Wallet Unit by verifying the **Wallet Unit Attestation (WUA)**. The provider ensures the request comes from a Wallet Unit belonging to a Wallet Provider that is listed in the **Wallet Provider Trusted List** with **valid entity status** (not Invalid), and that the WUA is authentic and **not revoked**.

## Actors

- **Primary**: Credential Issuer (PID Provider or Attestation Provider)
- **Secondary**: Wallet Unit (presents WUA), Wallet Provider Trusted List (and LoTL for discovery)

## Goal

- **Business**: Issue credentials only to Wallet Units that are bound to a notified, trusted Wallet Provider.
- **Technical**: Authenticate and validate the WUA using trust anchors from the Wallet Provider Trusted List; verify the Wallet Provider is in that TL with valid status (not Invalid) and the WUA is not revoked.

## Preconditions

- Credential Issuer has (or can obtain) the Wallet Provider Trusted List(s) it needs (ISSU_19, ISSU_28).
- Wallet Unit presents a valid Wallet Unit Attestation in the issuance flow (ARF Topic 9).

## Main Flow (Short)

1. Wallet Unit initiates issuance and presents its **Wallet Unit Attestation (WUA)** to the Credential Issuer.
2. **Trust anchors**: Credential Issuer accepts trust anchors from the **Wallet Provider Trusted List** (ISSU_19 for PID Provider, ISSU_28 for Attestation Provider).
3. **Wallet Provider in TL**: Credential Issuer verifies that the Wallet Provider referenced in the WUA is **present in the Wallet Provider Trusted List** and has **valid entity status** (not Invalid; GenNot_05) (ISSU_21, ISSU_30).
4. **WUA validation**: Credential Issuer authenticates and validates the WUA using the trust anchor(s) registered for that Wallet Provider in the TL; verifies the WUA is **not revoked** (ISSU_21, ISSU_30; Topic 38).
5. If any check fails: reject the issuance request, (the Wallet Unit informs the User of the reason). If all checks pass, proceed with issuance.

## Success Criteria

- Only Wallet Providers that appear in the Wallet Provider Trusted List with valid status (not Invalid) are accepted.
- WUA signature validation and WUA revocation check succeed before issuance.

## ARF Requirements (Key)

| Identifier | Requirement |
|------------|-------------|
| ISSU_19   | PID Provider SHALL accept trust anchors in the Wallet Provider Trusted List it needs. |
| ISSU_21   | PID Provider SHALL verify Wallet Provider is in Wallet Provider TL; authenticate/validate WUA; verify WUA not revoked. |
| ISSU_28   | Attestation Provider SHALL accept trust anchors in the Wallet Provider Trusted List. |
| ISSU_30   | Attestation Provider SHALL verify Wallet Provider in TL; authenticate/validate WUA; verify WUA not revoked. |
| GenNot_05 | Suspended/cancelled Wallet Providers have status Invalid in TL; Credential Issuer SHALL use only valid-status entries. |

## References

- [Trust evaluation base](trust-evaluation-base.md), [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation), [Trusted list / trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md)
