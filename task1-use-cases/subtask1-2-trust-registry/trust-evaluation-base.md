# Base: Trust Evaluation in the EUDI Wallet Ecosystem

This document provides the **common framework** for trust evaluation use cases: terminology, trust sources, and mapping to ARF high-level requirements. Use-case-specific flows and actors are in the individual use case documents.

## Terminology and Acronyms

See [onboarding-base.md](../subtask1-1-onboarding/onboarding-base.md#terminology-and-acronyms) for ecosystem terms. Terms specific to trust evaluation:

| Term | Meaning |
|------|---------|
| **Trust evaluation** | The process by which a participant verifies another participant's eligibility and authenticity using Trusted Lists, registries, and certificates (ARF Topics 27, 31, 44; [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation)). |
| **Trust anchor** | Public key (or certificate) in a Trusted List used to validate signatures or certificate chains. |
| **LoTL** | List of Trusted Lists; maintained by the European Commission; single trust anchor for TL discovery (ETSI TS 119 612). |
| **Registry** | Member State register of PID Providers, Attestation Providers, and Relying Parties; used for entitlement and registration verification (Reg_03, Reg_06). |
| **Entity status (in TL)** | Trusted List entries may carry a status (e.g. Valid / Invalid). Suspended or cancelled entities have status **Invalid** in the TL (GenNot_05). Evaluators should use only entries with valid status. |
| **Certificate revocation** | Access certificates and registration certificates can be revoked (Reg_14, Reg_15, RPRC_01, RPRC_02). Validators obtain revocation information (e.g. CRL, OCSP) as specified by the applicable Certificate Policy and check that certificates are not revoked at validation time. |
| **Credential / attestation revocation** | PID, attestations (EAA), and Wallet Unit Attestations (WUA) may be revocable. Where technical specifications or Topic 38 (WUA) require it, evaluators verify that the credential or attestation is not revoked. |

## Trust Sources Used in Evaluation

| Source | Content | Used by | ARF refs |
|--------|---------|---------|----------|
| **PID Provider Trusted List** | Trust anchors for PIDs | Relying Party, Wallet Unit | OIA_12, ISSU_07, PPNot_05 |
| **QEAA / PuB-EAA / EAA Trusted Lists** | Trust anchors for attestations | Relying Party, Wallet Unit | OIA_13, OIA_14, OIA_15, ISSU_08–10 |
| **Wallet Provider Trusted List** | Trust anchors for WUAs | PID Provider, Attestation Provider | ISSU_19, ISSU_21, ISSU_28, ISSU_30 |
| **Access CA Trusted List** | Trust anchors for access certificates | Wallet Unit | ISSU_23, ISSU_24, ISSU_33, ISSU_34, RPA_04 |
| **Registration Certificate Provider TL** | Trust anchors for registration certificates | Wallet Unit | ISSU_33a, RPRC_17 |
| **National Register / Registrar API** | Registered attributes, intended use, attestation types; suspension/cancellation (Reg_09) | Wallet Unit, (optional) User | ISSU_24a, ISSU_34a, RPRC_16–21, Reg_06 |
| **Revocation information (certificates)** | CRL, OCSP or other means per Certificate Policy (Reg_14, RPRC_02) | Wallet Unit, Relying Party, Providers | Reg_14, Reg_15, RPRC_01, RPRC_02 |
| **Revocation information (credentials/WUA)** | Per Topic 38 (WUA); per applicable specs for PID/attestation where defined | Credential Issuer, Relying Party | ISSU_21, ISSU_30, Topic 38 |

Full requirement set: [Trusted list registration trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md).

## Trust Evaluation Points (Summary)

1. **Before credential issuance (Wallet Unit → PID/Attestation Provider)**  
   Wallet Unit evaluates: Access Certificate (via Access CA TL), **certificate not revoked** (Reg_14), **Provider entity status in TL not Invalid** (GenNot_05), Provider registration and entitlements (Registry / registration certificate); **registration certificate not revoked** where used (RPRC_02).  
   Provider evaluates: Wallet Unit Attestation (via Wallet Provider TL), **WUA not revoked** (Topic 38), **Wallet Provider entity status in TL not Invalid** (GenNot_05).

2. **Before presentation (Relying Party → Wallet Unit)**  
   Wallet Unit evaluates: Relying Party Access Certificate (via Access CA TL), **access certificate not revoked** (Reg_14), **registration certificate not revoked** where used (RPRC_02), RP registration and requested attributes (Registry / registration certificate); **RP not suspended/cancelled** (registry/Reg_09).

3. **After presentation (Relying Party)**  
   Relying Party evaluates: PID signature (PID Provider TL), attestation signatures (QEAA/PuB-EAA/EAA TLs); **issuer entity status in TL not Invalid** (GenNot_05); **credential/attestation revocation** where required by technical specifications (e.g. PID/EAA revocation mechanisms).

## Normative References

- **ARF**: [EUDI Wallet Architecture and Reference Framework 2.7.3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/), Annex II High-Level Requirements
- **Project**: [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md), [Entities Involved](../../task2-trust-framework/entities-involved.md), [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)
