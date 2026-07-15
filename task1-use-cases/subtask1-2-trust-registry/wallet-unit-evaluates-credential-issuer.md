# Use Case UC-TE-02: Wallet Unit Evaluates Credential Issuer (Before PID or Attestation Request)

## Scope

Before requesting a **PID** or an **attestation (EAA)**, the Wallet Unit evaluates the Credential Issuer (PID Provider or Attestation Provider) so that the User only interacts with registered, authorised providers. Trust evaluation uses Access CA LoTEs, optional Registration Certificate Provider LoTEs, the Registrar's registry (or registration certificate), **certificate revocation** checks, and **entity status** in LoTEs (Valid/Invalid per GenNot_05).

## Actors

- **Primary**: Wallet Unit (on behalf of the Holder)
- **Secondary**: Holder (User using the Wallet Unit), Credential Issuer (PID Provider or Attestation Provider), Trusted List / LoTL, Registrar registry (or Provider of Registration Certificates)

## Goal

- **Business**: Ensure the Holder requests credentials only from providers that are registered and entitled to issue the requested credential type.
- **Technical**: Validate the Credential Issuer's access certificate (and optional registration certificate), confirm they are not revoked, confirm Provider entity status in TL is valid, and verify registration/entitlements before starting the issuance flow.

## Preconditions

- Wallet Unit has (or can obtain) the relevant LoTEs: Access CA LoTE; optionally Registration Certificate Provider LoTE ([trust-evaluation-base](trust-evaluation-base.md)).
- Credential Issuer exposes access certificate (and optionally registration certificate) in Issuer metadata (e.g. OpenID4VCI); ARF ISSU_22, ISSU_22a, ISSU_32, RPRC_22.
- Registrar registry is available per Reg_06 (common API) if registration certificate is not used.

## Main Flow (Short)

1. Wallet Unit obtains Credential Issuer metadata (e.g. credential endpoint), including access certificate (and optionally registration certificate).
2. **Access certificate**: Wallet Unit verifies the access certificate is authentic, valid at validation time, and issued by a CA present in the applicable **Access Certificate Authority LoTE** with **valid entity status** (not Invalid); verifies the access certificate is **not revoked** and includes a valid SCT where required (CT_05, ETSI TS 119 411-8) (ISSU_24 for PID, ISSU_34 for Attestation Provider).
3. **Registration certificate** (if present): Wallet Unit verifies authenticity and validity using **Registration Certificate Provider LoTE** (entry with valid status); verifies the registration certificate is **not revoked** per ETSI TS 119 475 / RPRC_02 technical specification.
4. **Registration / entitlements**: Wallet Unit verifies the provider is registered and entitled to issue the requested credential type:
   - If registration certificate is present in metadata: check that the requested attestation type is in the certificate (ISSU_24a for PID Provider, ISSU_34a for Attestation Provider).
   - Otherwise: call **Registrar online service** (URL from metadata) and verify registration and attestation type (ISSU_24a, ISSU_34a). Optionally confirm provider is not suspended/cancelled (Reg_09).
5. If any check fails: display a warning and do **not** request issuance (ISSU_24a, ISSU_34a). If all checks pass, proceed with issuance.

## Success Criteria

- Access certificate validation succeeds only when the issuing CA is in the relevant Access CA Trusted List with valid status, and the certificate is not revoked.
- Registration certificate (if used) is not revoked and issued by a Provider with valid status in the Registration Certificate Provider TL.
- Registration/entitlement verification confirms the provider is registered and authorised for the requested credential type.
- Failed verification leads to no credential request and a clear User warning.

## ARF Requirements (Key)

| Identifier | Requirement |
|------------|-------------|
| ISSU_24   | Wallet Unit SHALL authenticate and validate PID Provider access certificate using Access CA LoTE. |
| ISSU_24a  | Wallet Unit SHALL verify PID Provider is registered (registration cert or Registrar URL) before requesting PID. |
| ISSU_33   | Wallet Unit SHALL accept trust anchors in applicable Access CA LoTE(s) for Attestation Providers. |
| ISSU_33a  | Wallet Unit SHALL accept trust anchors in LoTE(s) for Providers of registration certificates. |
| ISSU_34   | Wallet Unit SHALL authenticate and validate Attestation Provider access certificate using Access CA LoTE. |
| ISSU_34a  | Wallet Unit SHALL verify Attestation Provider is registered and has sub-entitlements for the requested attestation type. |
| CT_05     | Wallet Unit SHALL verify access certificate includes at least one valid SCT during issuance or presentation. |
| GenNot_05 | Suspended/cancelled entities have status Invalid in TL; Wallet Unit SHALL consider only valid-status entries. |

## References

- **Terminology**: [Consolidated Terms and Entity Definitions](../terms-and-entities.md)
- [Trust evaluation base](trust-evaluation-base.md), [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation), [Trusted list / trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md)
