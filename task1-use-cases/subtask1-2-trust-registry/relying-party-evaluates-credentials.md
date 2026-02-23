# Use Case UC-TE-05: Relying Party Evaluates Presented Credentials (PID and Attestations)

## Scope

After receiving **PID** and/or **attestations (EAA)** from a Wallet Unit (proximity or remote presentation), the **Relying Party** evaluates the authenticity of the credentials by validating their signatures using trust anchors from the appropriate **Trusted Lists** (PID Provider TL, QEAA/PuB-EAA/EAA TLs), **issuer entity status** (not Invalid) in those TLs, and **credential/attestation revocation** where required by technical specifications.

## Actors

- **Primary**: Relying Party (or Relying Party Instance)
- **Secondary**: Holder (User using the Wallet Unit), Wallet Unit (source of presented credentials), PID Provider Trusted List, QEAA/PuB-EAA/EAA Provider Trusted Lists (or rulebook-defined mechanism for non-qualified EAA)

## Goal

- **Business**: Accept only PID and attestations that are signed by providers listed in the relevant Trusted Lists, ensuring compliance with the EUDI trust framework.
- **Technical**: Validate PID and attestation signatures using the correct trust anchors from Trusted Lists; consider issuer (PID Provider / Attestation Provider) entity status in TL (GenNot_05); where specs require it, verify PID and attestations are not revoked.

## Preconditions

- User, after reviewing the identity of the RP (RPA_05), the intended use and any privacy policies, if available, as shown by the Wallet Unit, approved the presentation (RPA_10).
- Relying Party has (or can obtain) the Trusted Lists needed for the credential types it accepts: PID Provider TL; QEAA Provider TL (e.g. Member State QTSP TL); PuB-EAA Provider TL; for non-qualified EAA, mechanism per applicable Rulebook (Topic 12).
- Presented credentials (PID, QEAA, PuB-EAA, or non-qualified EAA) are available for signature verification.

## Main Flow (Short)

1. Relying Party receives presented PID and/or attestations from the Wallet Unit (presentation flow completed).
2. **PID**: Relying Party validates the **signature of the PID** using a trust anchor from the **PID Provider Trusted List** (Topic 31); uses only PID Provider entries with **valid entity status** (not Invalid; GenNot_05). Where technical specifications require it, verifies the **PID is not revoked** (OIA_12).
3. **QEAA**: Relying Party validates the **qualified signature of the QEAA** per Art. 32 using a trust anchor from a **QEAA Provider Trusted List** (Member State QTSP TL); considers **issuer status in TL** (GenNot_05). Where specs require it, verifies the **attestation is not revoked** (OIA_13).
4. **PuB-EAA**: Relying Party validates the **qualified signature of the PuB-EAA** per Art. 32; validates the QTSP certificate via TL; verifies certified attributes per Article 45f; considers **issuer status in TL**. Where specs require it, verifies **attestation not revoked** (OIA_14).
5. **Non-qualified EAA**: Relying Party validates the **signature of the EAA** using trust anchors per the **applicable Rulebook** (Topic 12); considers issuer status where applicable; **revocation** per rulebook/specs (OIA_15).
6. If any signature, certificate, status, or revocation check fails: reject the presentation (the Wallet Unit informs the User of the reason). If all pass, the RP may use the attributes for the service.

## Success Criteria

- PID is accepted only when its signature validates against the PID Provider Trusted List, issuer has valid status in TL, and (where required) PID is not revoked.
- QEAA/PuB-EAA are accepted only when validated per eIDAS/Art. 32 and the relevant Trusted Lists, with valid issuer status and (where required) attestation not revoked.
- Non-qualified EAA is accepted only when validated per the applicable Rulebook, with revocation checked where specified.

## ARF Requirements (Key)

| Identifier | Requirement |
|------------|-------------|
| OIA_12    | RP SHALL validate PID signature using trust anchor from PID Provider TL (Topic 31). |
| OIA_13    | RP SHALL validate QEAA qualified signature per Art. 32 using QEAA Provider TL (Art. 22). |
| OIA_14    | RP SHALL validate PuB-EAA qualified signature per Art. 32; validate QTSP cert via TL; verify certified attributes per Art. 45f. |
| OIA_15    | RP SHALL validate non-qualified EAA signature per mechanism(s) in applicable Rulebook (Topic 12). |
| GenNot_05 | Suspended/cancelled PID/Attestation Providers have status Invalid in TL; RP SHALL use only valid-status entries for trust anchors and issuer checks. |

## References

- **Terminology**: [Consolidated Terms and Entity Definitions](../terms-and-entities.md)
- [Trust evaluation base](trust-evaluation-base.md), [Trust Infrastructure Schema §8](../../task2-trust-framework/trust-infrastructure-schema.md#8-trust-evaluation), [Trusted list / trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md), [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)
