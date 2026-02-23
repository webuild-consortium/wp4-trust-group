# Use Case UC-TE-04: Wallet Unit Evaluates Relying Party (Before Presentation)

## Scope

Before the User approves **presentation** of attributes to a Relying Party, the Wallet Unit evaluates the Relying Party: it verifies the RP's access certificate using the **Access Certificate Authority Trusted List**, checks that **certificates are not revoked**, and optionally verifies the RP's **registration** (and requested attributes) via registration certificate or **Registrar registry**, so the User can make an informed decision.

## Actors

- **Primary**: Wallet Unit (on behalf of the Holder)
- **Secondary**: Holder (User using the Wallet Unit), Relying Party Instance, Access CA Trusted List, Registrar registry (or Provider of Registration Certificates)

## Goal

- **Business**: Ensure the User presents attributes only to Relying Parties that are registered and, if the User opts in, that the requested attributes match what is registered.
- **Technical**: Validate RP access certificate (and registration certificate if present), verify they are not revoked, and when the User requests it, RP registration and requested-attributes consistency (and that RP is not suspended/cancelled).

## Preconditions

- Wallet Unit has (or can obtain) the relevant **Access Certificate Authority Trusted List(s)** for Relying Parties (RPA_04).
- Relying Party Instance sends presentation request including access certificate and, if applicable, registration certificate and RP info (RPRC_19, RPRC_19a).
- Wallet Unit offers the User the option to verify RP registration (RPRC_16).

## Main Flow (Short)

1. Relying Party Instance sends a presentation request to the Wallet Unit (access certificate, and optionally registration certificate and RPRC_19a data).
2. **Access certificate**: Wallet Unit verifies the RP Instance access certificate using trust anchors from the **Relying Party Access Certificate Authority Trusted List(s)** (RPA_04); verifies the access certificate is **not revoked** (Reg_14). If a registration certificate is present, verifies it is **not revoked** (RPRC_02).
3. **Optional User verification**: If the User has chosen to verify the information registered about the Relying Party (RPRC_16):
   - If **registration certificate** is present: Wallet Unit verifies authenticity and validity (e.g. using Registration Certificate Provider TL) per RPRC_17; if verification fails, notify the User when asking for approval (RPRC_17).
   - If **no registration certificate**: Wallet Unit uses the **Registrar online service URL** from the request to fetch registered information; if unavailable or invalid, notify the User when asking for approval (RPRC_18).
   - Wallet Unit verifies that **all attributes requested** in the presentation request are **included in the registered list** (RPRC_21); if not, notify the User about unregistered attributes (RPRC_21). Optionally confirm RP is not suspended/cancelled (Reg_09).
4. Wallet Unit asks for User approval (RPA_07); any negative verification outcome is communicated to the User at this step.

## Success Criteria

- RP access certificate (and registration certificate if present) is validated via the applicable Trusted List(s) and verified not revoked.
- When the User opts in, registration and attribute checks are performed and failures are clearly reported.

## ARF Requirements (Key)

| Identifier | Requirement |
|------------|-------------|
| RPA_04    | Wallet Unit SHALL accept trust anchors in the Trusted List(s) of Relying Party Access CAs (all Member States). |
| RPRC_16   | Wallet Unit SHALL offer the User the possibility to verify information registered about the RP. |
| RPRC_17   | If User wants verification and RP sent registration cert: verify authenticity/validity; on failure, notify User at approval. |
| RPRC_18   | If User wants verification and no registration cert: obtain info from Registrar URL; on failure, notify User at approval. |
| RPRC_21   | When verified, Wallet Unit SHALL verify requested attributes are in the list registered by the Registrar; on failure, notify User. |
| Reg_14    | Access CA provides revocation method(s); Wallet Unit SHALL verify access certificate not revoked. |
| RPRC_02   | Technical spec describes revocation of registration certificates; Wallet Unit SHALL verify reg cert not revoked when used. |

## References

- **Terminology**: [Consolidated Terms and Entity Definitions](../terms-and-entities.md)
- [Trust evaluation base](trust-evaluation-base.md), [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation), [Trusted list / trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md)
