# Base Onboarding Framework for EUDI Wallet Ecosystem Participants

**Note**: This document provides the common base framework for onboarding processes applicable to Relying Parties, PID Providers, Attestation Providers (QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers), and Wallet Providers in the EUDI Wallet ecosystem. This base document should be referenced by entity-specific onboarding documents to avoid duplication and ensure consistency.

**Note**: Throughout this document, "EUDI Wallets" refers to European Digital Identity Wallets as defined in [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj).

**Note on API Schema Alignment**: The data models and workflows described in this document align with the [Onboarding API data schemas](../../task4-trust-infrastructure-api/onboarding-api/README.md#data-models). Participant types, status values, certificate types, and workflow steps are harmonized across both specifications.

## Common Success Criteria

The following success criteria apply to all participant onboarding processes in the EUDI Wallet ecosystem:

- *Interoperability across Member States*
    - All certificates and attestations are syntactically and semantically harmonised in line with applicable ETSI standards (e.g., ETSI EN 319 411-1 version 1.4.1 (2023-10)) and related IETF RFCs ([RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519), [RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392), [RFC 9162](https://datatracker.ietf.org/doc/html/rfc9162)) (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - Certificates and registration data can be validated cross-border in an automated manner using Trusted Lists as defined in [ETSI TS 119 612 v2.4.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) and [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).
- *Secure trust establishment*
    - Each entity's identity and attributes are verifiable via National Registers (for Relying Parties, PID/EAA Providers) or Trusted Lists (for Wallet Providers) and anchored in the EU trust framework (ref. [Regulation (EU) 2024/1183, Article 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)).
    - Continuous monitoring and automatic certificate/attestation revocation mechanisms are implemented and effective within 24 hours of a change request (ref. [Regulation (EU) 2025/848, Article 9(5)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- *Transparency and traceability*
    - All certificate issuances, renewals, and revocations are logged (optionally under RFC 9162 – Certificate Transparency v2.0) and made publicly accessible for validation (ref. [Regulation (EU) 2025/848, Annex IV 3(j), Annex V 3(i)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - Revocation and validity information is provided freely (free of charge), automatically, and reliably (ref. [Regulation (EU) 2025/848, Annex IV 5, Annex V 6](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- *Compliance and accountability*
    - Certificate Policies (CP) and Certification Practice Statements (CPS) follow ETSI EN 319 411-1 version 1.4.1 (2023-10) NCP requirements where applicable (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - Each Member State designates appropriate authorities (Registrars for Relying Parties/PID/EAA Providers, Supervisory Bodies for Wallet Providers) and maintains National Registers or Trusted Lists, and communicates changes to the Commission and other Member States (ref. [Regulation (EU) 2025/848, Article 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- *Operational effectiveness*
    - Onboarding is completed through defined processes (administrative + technical for Relying Parties/PID/EAA Providers; certification + listing for Wallet Providers) with measurable outcomes and turnaround times.
    - End-to-end validation succeeds automatically through Trusted List integration (see [Task 3 - ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)).
