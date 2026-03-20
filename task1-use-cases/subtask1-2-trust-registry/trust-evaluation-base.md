# Base: Trust Evaluation in the EUDI Wallet Ecosystem

This document provides the **common framework** for trust evaluation use cases: trust sources and mapping to ARF high-level requirements. Terminology is in [Consolidated Terms and Entity Definitions](../terms-and-entities.md). Use-case-specific flows and actors are in the individual use case documents.

## Terminology and Acronyms

See [Consolidated Terms and Entity Definitions](../terms-and-entities.md) for all terms, acronyms, and entity definitions, including trust evaluation terms (Trust evaluation, Trust anchor, Entity status, Certificate revocation, Credential/attestation revocation, Trust Mark, Holder) in [Section 2.3 and 2.4](../terms-and-entities.md#23-trust-evaluation-terms).

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
| **Trust Mark (EUDI Wallet)** | Verifiable, simple, recognisable indication of wallet authenticity and validity; displayed by Wallet Instance for Holder assessment | Holder | Regulation (EU) 2024/1183 Art. 3(50), 5a(5), 5a(8), 5d |

Full requirement set: [Trusted list registration trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md).

## Trust Evaluation Points (Summary)

**0. Holder evaluates own Wallet Instance (via Trust Marks)**  
The Holder (User using the Wallet Unit) can assess the trustworthiness of their own Wallet Instance. Regulation (EU) 2024/1183 Articles 3(50), 5a(5), 5a(8), and 5d introduce Trust Marks as a "verifiable, simple and recognisable indication" capable of ensuring that the authenticity and validity of European Digital Identity Wallets can be verified. Wallet solutions display the EU Digital Identity Wallet Trust Mark for user interaction, enabling Holders to verify they are using a certified, authentic wallet instance before and during use.

**Before Wallet Unit activation (Holder)**  
Holder evaluates: general information on the certification of Wallet Solutions and discovers links to the certification status information (DASH_09); presence and validity of the EU Digital Identity Wallet Trust Mark indicating a certified wallet.

**After Wallet Unit activation (Holder)**  
Holder evaluates: and is informed about the validity status of their Wallet Unit (WURevocation_14 and WURevocation_16); ongoing display of the Trust Mark as an indication of continued authenticity and validity.

1. **Before credential issuance (Wallet Unit → PID/Attestation Provider)**  
   Wallet Unit evaluates: Access Certificate (via Access CA TL), **certificate not revoked** (Reg_14), **Provider entity status in TL not Invalid** (GenNot_05), Provider registration and entitlements (Registry / registration certificate); **registration certificate not revoked** where used (RPRC_02).  
   Provider evaluates: Wallet Unit Attestation (via Wallet Provider TL), **WUA not revoked** (Topic 38), **Wallet Provider entity status in TL not Invalid** (GenNot_05).

2. **Before presentation (Relying Party → Wallet Unit)**  
   Wallet Unit evaluates: Relying Party Access Certificate (via Access CA TL), **access certificate not revoked** (Reg_14), **registration certificate not revoked** where used (RPRC_02), RP registration and requested attributes (Registry / registration certificate); **RP not suspended/cancelled** (registry/Reg_09).

3. **After presentation (Relying Party)**  
   Relying Party evaluates: PID signature (PID Provider TL), attestation signatures (QEAA/PuB-EAA/EAA TLs); **issuer entity status in TL not Invalid** (GenNot_05); **credential/attestation revocation** where required by technical specifications (e.g. PID/EAA revocation mechanisms).

## Normative References

- **ARF**: [EUDI Wallet Architecture and Reference Framework 2.7.3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/), Annex II High-Level Requirements
- **Regulation**: [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1183) (European Digital Identity Regulation), Articles 3(50), 5a(5), 5a(8), 5d (Trust Marks for EUDI Wallets)
- **Project**: [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md), [Entities Involved](../../task2-trust-framework/entities-involved.md), [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)
