# Use Case UC-TE-06: Trusted List Discovery and Consumption

## Scope

Participants (Wallet Units, Relying Parties, PID Providers, Attestation Providers) need to **obtain** and **use** Trusted Lists for trust evaluation. This use case covers discovering the **List of Trusted Lists (LoTL)** and the relevant **Trusted Lists (TL)**, and consuming them for validation (signature verification, certificate chain validation, **entity status**, and where applicable **revocation** information). Format and validation rules follow ETSI TS 119 612 / TS 119 602 and the WP4 implementation profile.

## Actors

- **Primary**: Any participant that performs trust evaluation (Wallet Unit, RP, PID Provider, Attestation Provider)
- **Secondary**: European Commission (publishes LoTL and EU-level TLs), Member State TLP (publishes national TLs), LoTL and TL distribution endpoints

## Goal

- **Business**: Rely on an up-to-date, authentic set of trust anchors so that trust decisions are consistent with the EUDI trust framework.
- **Technical**: Resolve LoTL location (e.g. OJEU or Commission endpoint), fetch LoTL and relevant TL(s), verify TL/LoTL signatures, and use trust anchors from TLs in validation logic.

## Preconditions

- LoTL location and trust anchor for verifying the LoTL are published (e.g. OJEU per TLPub_06, TLPub_07).
- Trusted Lists are published in machine-processable, signed form over a secure channel (TLPub_03, TLPub_05); no prior authentication required for retrieval (TLPub_04).
- Participant knows which TL type(s) it needs (e.g. Access CA TL, PID Provider TL, Wallet Provider TL) per its role ([trust-evaluation-base](trust-evaluation-base.md)).

## Main Flow (Short)

1. **Discover LoTL**: Participant obtains the LoTL URL and the trust anchor(s) used to sign/seal the LoTL (e.g. from Commission specifications or OJEU; TLPub_06, TLPub_07).
2. **Fetch LoTL**: Participant retrieves the LoTL over a secure channel; verifies signature/seal of the LoTL using the LoTL trust anchor.
3. **Select TL(s)**: From the LoTL, participant determines the URL(s) and signing key(s) of the Trusted List(s) it needs (e.g. PID Provider TL, Wallet Provider TL, Access CA TL) and optionally Member State TL pointers (e.g. QTSP TL for QEAA, national EAA TL).
4. **Fetch TL(s)**: For each needed TL, participant retrieves the TL, verifies its signature using the key indicated in the LoTL (or the TL’s own signing certificate), and parses the TL according to the applicable format (ETSI TS 119 612 or profile, e.g. [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)).
5. **Consume trust anchors and status**: Participant extracts trust anchors (e.g. public keys, certificates) and **entity status** (e.g. Valid/Invalid per GenNot_05) from the TL entries. Only entries with valid status are used for trust decisions. Participant uses trust anchors and status in:
   - **UC-TE-02**: Access CA TL, Reg Cert Provider TL for Wallet Unit evaluating Credential Issuer
   - **UC-TE-03**: Wallet Provider TL for Credential Issuer evaluating Wallet Unit
   - **UC-TE-04**: Access CA TL (and Reg Cert Provider TL) for Wallet Unit evaluating Relying Party
   - **UC-TE-05**: PID Provider TL, QEAA/PuB-EAA/EAA TLs for Relying Party evaluating credentials
6. **Revocation information**: Where evaluation requires certificate or credential revocation checks, participant obtains revocation information (e.g. CRL, OCSP for access/registration certificates per Reg_14, RPRC_02; WUA/PID/attestation revocation per Topic 38 and applicable specs) from the sources defined in the relevant policies.
7. **Refresh**: Participant refreshes LoTL and TLs according to policy (availability and authenticity of full history per TLPub_08).

## Success Criteria

- LoTL and TLs are retrieved and their signatures verified before use.
- Trust anchors and entity status used in evaluation come only from correctly signed TLs referenced by the LoTL (or from Commission/MS TLP as specified); only valid-status entries are used.
- Revocation information is obtained and used where required by Certificate Policy or credential/attestation specifications.
- Format and validation align with ETSI TS 119 612 / TS 119 602 and the project implementation profile.

## ARF / ETSI Requirements (Key)

| Identifier | Requirement |
|------------|-------------|
| TLPub_03  | Publication over secure channel protecting authenticity and integrity. |
| TLPub_04  | No authentication or prior registration required to retrieve published information. |
| TLPub_05  | Information published in signed/sealed form suitable for automated processing and human-readable. |
| TLPub_06  | Commission publishes in OJEU the locations of the Trusted Lists. |
| TLPub_07  | Commission publishes in OJEU the trust anchors for verifying the signature/seal. |
| TLPub_08  | Full history of notified information available and authentic. |
| WPNot_05, PPNot_07, RPACANot_05 | TL format complies with ETSI TS 119 612 v2.1.1 or suitable profile (e.g. ETSI TS 102 231). |
| GenNot_05 | TL entries carry entity status; suspended/cancelled entities have status Invalid. |
| Reg_14, RPRC_02 | Revocation method(s) for access and registration certificates; participants use these for revocation checks. |

## References

- [Trust evaluation base](trust-evaluation-base.md), [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md) (Section 3: Trusted List Publication), [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md), [Trusted list / trust evaluation matrix](../../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md)
