# Use Case UC-TE-04: Wallet Unit Evaluates Relying Party (Before Presentation)

## Scope

Before the User approves **presentation** of attributes to a Relying Party, the Wallet Unit evaluates the Relying Party: it verifies the RP's access certificate using the **Access Certificate Authority Trusted List**, checks that **certificates are not revoked**, and verifies the **WRPRC included in the presentation request** (authenticity, binding to the access certificate / Service, and requested attributes), so the User can make an informed decision.

## Actors

- **Primary**: Wallet Unit (on behalf of the Holder)
- **Secondary**: Holder (User using the Wallet Unit), Relying Party Instance, Access CA Trusted List, Provider of Registration Certificates (WRPRC Provider Trusted List)

## Goal

- **Business**: Ensure the Holder presents attributes only to Relying Parties that are registered and that the requested attributes match what is registered for that Service and intended use.
- **Technical**: Validate RP access certificate and the WRPRC in the request, verify they are not revoked, and report failed verifications when asking for approval.

## Preconditions

- Wallet Unit has (or can obtain) the relevant **Access Certificate Authority Trusted List(s)** for Relying Parties (RPA_04) and the **Registration Certificate Provider Trusted List** (RPRC_17).
- Relying Party Instance sends a presentation request including the access certificate and a single WRPRC by value (RPRC_19).

## Main Flow (Short)

1. Relying Party Instance sends a presentation request to the Wallet Unit (access certificate and WRPRC for the current Service and intended use).
2. **Access certificate**: Wallet Unit verifies the RP Instance access certificate using trust anchors from the **Relying Party Access Certificate Authority Trusted List(s)** (RPA_04); verifies the access certificate is **not revoked** (Reg_14).
3. **WRPRC in the request** (RPRC_17): Wallet Unit verifies format, authenticity, and validity of the registration certificate. If the certificate is absent, malformed, inauthentic, or expired, the Wallet Unit **warns the User** when asking for approval (RPA_07). The Wallet Provider’s risk policy determines whether approval is still allowed.
4. **Binding** (RPRC_17a): Wallet Unit verifies that the WRPRC contains the same unique Relying Party identifier and Service identifier as the access certificate, or that the WRPRC shows the intermediated RP uses this intermediary.
5. **Attributes** (RPRC_21): Wallet Unit verifies that **all attributes requested** are included in the WRPRC in the same request; if not, warn the User. Optionally confirm RP is not suspended/cancelled (Reg_09).
6. Wallet Unit asks for User approval (RPA_07 / RPA_06). For an intermediary, it SHALL NOT display the intermediary’s trade names (RPI_07).

## Success Criteria

- RP access certificate and WRPRC are validated via the applicable Trusted List(s) and verified not revoked.
- Binding and attribute checks are performed and failures are clearly reported at approval.

## ARF Requirements (Key)

| Identifier | Requirement |
|------------|-------------|
| RPA_04    | Wallet Unit SHALL accept trust anchors in the Trusted List(s) of Relying Party Access CAs (all Member States). |
| RPA_06    | Display Relying Party and Service trade names from the access certificate, except for intermediaries (RPI_07). |
| RPRC_17   | Verify authenticity/validity of the WRPRC in the request; on failure, warn User at approval. |
| RPRC_17a  | WRPRC unique identifier and Service identifier SHALL match the access certificate, or the WRPRC SHALL show use of this intermediary. |
| RPRC_19   | Relying Party Instance SHALL include a single WRPRC by value in each presentation request. |
| RPRC_21   | Wallet Unit SHALL verify requested attributes are in the WRPRC in the same request; on failure, notify User. |
| RPRC_16 / RPRC_18 | Empty in ARF v3.0.0 (no user-opt-in Registrar lookup). |
| Reg_14    | Access CA provides revocation method(s); Wallet Unit SHALL verify access certificate not revoked. |
| RPRC_02   | Technical spec describes revocation of registration certificates; Wallet Unit SHALL verify WRPRC not revoked when used. |

## References

- **Terminology**: [Consolidated Terms and Entity Definitions](../terms-and-entities.md)
- [Trust evaluation base](trust-evaluation-base.md), [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation), [Trusted list / trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md)
