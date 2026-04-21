# Use Case: UC-04 Wallet Relying Party Access Certificate / Registration Certificate Authority Onboarding

## Scope

This document describes the onboarding process for providers of Wallet-Relying Party Registration Certificates (hereafter **WRPRC Authorities**) and providers of Wallet-Relying Party Access Certificates (hereafter **WRPAC Authorities**). The onboarding process results in the WRPAC/WRPRC Authority being listed on a Trusted List maintained by the applicable Trusted List Provider, enabling Wallet Units and other ecosystem participants to validate certificates issued by that authority.

This use case aligns with the [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md), which defines the overall architecture and notification process. See [Trust Infrastructure Schema - Responsibilities Matrix](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix) for details.

WRPAC/WRPRC Authorities are **notified** by Member States to the European Commission for inclusion in EU-level Trusted Lists. They are **not** registered with a Registrar. This distinction is described in the [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).

This document follows the WEBUILD ecosystem structure; see [MVP and MVP+ Definitions](onboarding-base.md#mvp-and-mvp-definitions) in the base document.

Wherever feasible, this specification aligns with processes defined in [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng), [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848), and the [Architecture and Reference Framework](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/), interpreting them for the testing purposes specific to WEBUILD.

For the common framework (terminology, MVP/MVP+, RACI definitions), see [Base Onboarding Framework](onboarding-base.md). This document defines only **WRPAC/WRPRC Authority–specific** content and does not duplicate the base.

---

## Modal Verbs Terminology

The key words and phrases used in this document to indicate requirement levels are defined as follows, in accordance with ETSI Drafting Rules:

| Term | Meaning |
|------|---------|
| **SHALL** | Indicates a mandatory requirement. Non-compliance constitutes non-conformance with this specification. |
| **SHALL NOT** | Indicates a mandatory prohibition. |
| **SHOULD** | Indicates a recommendation. Deviation is permitted where justified, but the implications must be understood and carefully weighed. |
| **SHOULD NOT** | Indicates something not recommended. |
| **MAY** | Indicates a permissible course of action that is optional. |
| **NEED NOT** | Indicates that the action is not required. |

> **Note**: The terms "must" and "must not" are not used as normative terms in this document. Where they appear in direct citations from external sources, they retain the meaning assigned by the source document.

---

## Terminology and Acronyms

- **WRPAC** — Wallet-Relying Party Access Certificate
- **WRPRC** — Wallet-Relying Party Registration Certificate
- **WRPAC Authority** — A provider of Wallet-Relying Party Access Certificates, designated by a Member State per [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Article 7
- **WRPRC Authority** — A provider of Wallet-Relying Party Registration Certificates, authorised by a Member State per [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Article 8

See [Terminology and Acronyms](onboarding-base.md#terminology-and-acronyms) in the base document for further definitions.

---

## Actors

- **Primary Actor [MVP]**:
    - Beneficiaries and Associated Partners acting as a WRPAC Authority
    - Beneficiaries and Associated Partners acting as a WRPRC Authority
- **Secondary Actors [MVP]**:
    - Ecosystem Authority: WEBUILD WP4 Trust Infrastructure group
    - Trusted List Provider: WEBUILD WP4 Trust Infrastructure group

    > **Note**: The Trust Infrastructure group is not a legal entity. However, the Ecosystem Authority MAY be required to provide certain information (e.g. legal name, company address) and to digitally sign data. For testing purposes, at least one representative of the Trust Infrastructure group SHALL be designated and authorised to perform digital signing on behalf of the legal entity they represent.

- **Primary Actor [MVP+]**:
    - WRPAC Authority
    - WRPRC Authority
- **Secondary Actors [MVP+]**:
    - Member State / Supervisory Body (the competent authority responsible for authorising and supervising WRPAC/WRPRC Authorities)
    - European Commission (Trusted List Provider for EU-level WRPAC/WRPRC Authority Trusted Lists)

---

## Goal

- **Technical Goal [MVP]**: To establish an onboarding process for WRPAC/WRPRC Authorities on a Trusted List, enabling trusted interaction between EUDI Wallet Units and Relying Parties.

- **Business Goal [MVP+]**: To establish trust anchors for cryptographic trust validation that identify authorised WRPAC Authorities and WRPRC Authorities, enabling Wallet Units to validate access and registration certificates presented by Relying Parties.

- **Success Criteria**:
    - [MVP] Pilot implementations successfully demonstrate WRPAC/WRPRC Authority onboarding. All WRPAC/WRPRC Authorities within WEBUILD SHALL be included on a publicly accessible Trusted List maintained by the WP4 Trust Infrastructure group.
    - [MVP+] Trust anchors for WRPAC/WRPRC Authorities SHALL be published in EU-level Trusted Lists compiled and published by the European Commission. See [Trust Infrastructure Schema - Responsibilities Matrix](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).

---

## Preconditions

### Preconditions [MVP]

- The WEBUILD WP4 Trust Infrastructure group SHALL be designated to act as Ecosystem Authority and Trusted List Provider for all WEBUILD participants.
- A LoTL with at least one Trusted List for WRPAC/WRPRC Authorities SHALL be available for onboarding; see [MVP trust infrastructure: LoTL and Trusted Lists](onboarding-base.md#mvp-trust-infrastructure-lotl-and-trusted-lists) in the base document.
- The WP4 Trust Infrastructure group SHALL have assigned responsibilities for the onboarding process.
- The WRPAC/WRPRC Authority SHALL be able to provide the data specified in [Data to be provided](#data-to-be-provided).

See [RACI Matrix](onboarding-base.md#raci-matrix) in the base document for RACI acronym definition and role definitions.

| RACI MATRIX — WP4 Trust Infrastructure Group                            | Lead / Co-Lead | WP4 – Testing | IDUnion SCE | [Participant] |
|-------------------------------------------------------------------------|---------------|----------------|-------------|---------------|
| Announce onboarding request to WRPAC/WRPRC Authorities                  | A, C          |                | R           | I             |
| Set up and manage a form to gather data from WRPAC/WRPRC Authorities    | A, C          |                | R           | I             |
| Review WRPAC/WRPRC Authority data                                       | A, C          |                | R           | I             |
| Decide upon listing and de-listing (Ecosystem Authority)                | A, C          |                | R           | I             |
| Inform about decision                                                   | A, C          |                | R           | I             |
| Enable updates on Trusted Lists (Trusted List Provider)                 | A, C          |                | R           | I             |
| Host the Trusted List for WRPAC/WRPRC Authorities                       | A, C          |                | R           | I             |
| Engage with WRPAC/WRPRC Authorities during onboarding / troubleshooting | A, C          |                | R           | I             |

**Onboarding phase — responsibilities by actor**: The following table assigns Responsible (R), Accountable (A), Consulted (C), and Informed (I) for each administrative onboarding step. [MVP]: Ecosystem Authority and Trusted List Provider are the WP4 Trust Infrastructure group; [MVP+]: Member State / Supervisory Body and European Commission apply.

| Step                                           | WRPAC/WRPRC Authority                                             | Ecosystem Authority / Member State       | Trusted List Provider                       |
|------------------------------------------------|-------------------------------------------------------------------|------------------------------------------|---------------------------------------------|
| [MVP] 1.1 Request onboarding                   | R (submit request and data)                                       | A (provide form, receive)                | I                                           |
| [MVP] 1.2 Onboarding request review            | C (clarify if requested)                                          | R, A (review, decide)                    | I                                           |
| [MVP] 1.3 Trusted List updated                 | I (notified)                                                      | R, A (approve, trigger update)           | R (update TL, issue certificates)           |
| [MVP+] 2.1 Request onboarding                  | R (submit compliance evidence to Member State / Supervisory Body) | A (receive)                              | I                                           |
| [MVP+] 2.2 Review onboarding request           | C (clarify if requested)                                          | R, A (review per CIR 2025/848 Annex IV/V) | I                                          |
| [MVP+] 2.3 Approve onboarding to Trusted List  | I                                                                 | R, A (approve, notify EC)                | I                                           |
| [MVP+] 2.4 Confirm successful onboarding       | I (receive confirmation)                                          | R, A (confirm)                           | I                                           |
| [MVP+] 2.5 Trusted List updated                | I (notified)                                                      | A                                        | R (update TL)                               |

### Preconditions [MVP+]

- Each Member State SHALL have designated at least one Supervisory Body or competent authority responsible for authorising WRPAC/WRPRC Authorities ([Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng), [eIDAS Article 22(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1)).
- Each Member State SHALL have designated at least one Trusted List Provider ([eIDAS Article 22(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1)).
- The onboarding WRPAC/WRPRC Authority SHALL demonstrate compliance with the certificate policy and certification practice statement requirements set out in [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Annex IV (for WRPAC) and/or Annex V (for WRPRC), and with [ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf) and [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf) NCP requirements.

---

## Data Model

[MVP]

As a baseline, a single LoTL with one Trusted List (TL) SHALL be used for all WRPAC/WRPRC Authorities in WEBUILD to reduce complexity. For the common LoTL/TL and trust-anchor model, see [MVP trust infrastructure: LoTL and Trusted Lists](onboarding-base.md#mvp-trust-infrastructure-lotl-and-trusted-lists) in the base document.

### Trusted List and Certificate Profile

- Trusted Lists for WRPAC/WRPRC Authorities SHALL comply with [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf). See [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) for detailed implementation guidance, including the WRPAC/WRPRC Authority Trusted List data model, service entries, and profile-specific requirements.
- WRPAC/WRPRC Authority certificates SHALL follow [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) (v01.00.00) section 5. See [Task 3 — X.509 PKI with ETSI Alignments](../../task3-x509-pki-etsi/README.md) for certificate profile specifications.

### Data to be Provided

The WRPAC/WRPRC Authority SHALL provide the following data when requesting onboarding. Under [MVP], data SHALL be submitted via the form provided by the [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group). Under [MVP+], data SHALL be provided as required by the Member State / Supervisory Body and the regulations listed below.

*Normative references*: [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Articles 7, 8, Annex IV, Annex V; [ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf); [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf). *Technical references*: [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf); [ETSI Trusted Lists Implementation Profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md).

*About the WRPAC/WRPRC Authority (legal entity):*

- Legal name of the WRPAC/WRPRC Authority
- Trade name (including EUID where applicable)
- Legal address
- Country (Member State) in which the WRPAC/WRPRC Authority is established
- URI to published terms and conditions
- Statement whether the WRPAC/WRPRC Authority is a Qualified Trust Service Provider (QTSP)
- Statement whether the WRPAC/WRPRC Authority is a single-person company

*Cryptographic material* — one of the following SHALL be provided:

- An X.509 Certificate Signing Request (CSR) for issuance of the Authority certificate. The certificate profile and issuance process are specified in [Task 3 — X.509 PKI with ETSI Alignments](../../task3-x509-pki-etsi/README.md) and [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) section 5. The Trusted List entry SHALL include the issued certificate per [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).
- An X.509 certificate conforming to the profile specified in [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) section 5. In this case, the WRPAC/WRPRC Authority SHALL sign a challenge provided by the [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group) using the private key bound to the public key in the submitted certificate, in order to demonstrate possession of the corresponding private key.

---

## Main Flow

**1. Onboarding via Trust Infrastructure Responsible Group [MVP]**

- 1.1 WRPAC/WRPRC Authority requests onboarding
- 1.2 Onboarding request review
- 1.3 Trusted List of WRPAC/WRPRC Authorities is updated (MVP: by WP4 Trust Infrastructure group; LoTL with one TL for WEBUILD)

**2. Onboarding via Member State / Supervisory Body [MVP+]**

- 2.1 WRPAC/WRPRC Authority requests onboarding
- 2.2 Member State / Supervisory Body reviews onboarding request
- 2.3 Member State / Supervisory Body approves onboarding and notifies European Commission
- 2.4 Member State / Supervisory Body confirms successful onboarding
- 2.5 European Commission updates the EU-level Trusted List of WRPAC/WRPRC Authorities (after Member State notification; see [Trust Infrastructure Schema - Overview](../../task2-trust-framework/trust-infrastructure-schema.md#overview))

**3. Technical Onboarding**

- Certificate issuance for the WRPAC/WRPRC Authority is part of Administrative Onboarding (see 1.3 and 2.5). See [Task 3](../../task3-x509-pki-etsi/README.md), [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf), [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).

**4. Post-Onboarding**

- 3.1 Trusted List / WRPAC/WRPRC Authority monitoring
- 3.2 Trusted List update
- 3.3 De-listing / suspension
- 3.4 WRPAC/WRPRC Authority certificate revocation

---

## Industrial-Scale Considerations

The following considerations apply to WRPAC/WRPRC Authority onboarding (notification and Trusted List listing) at scale. Framework context: [Task 2 — Trust Framework](../../task2-trust-framework/README.md).

### 1. Entity Identification and Trusted List Integration

WRPAC/WRPRC Authorities SHALL be **notified** by Member States to the European Commission and SHALL NOT register with a Registrar. They SHALL be listed on the **Trusted List of WRPAC/WRPRC Authorities**, which is compiled and published by the **European Commission** (MVP+); see [Trust Infrastructure Schema — Responsibilities Matrix](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix). Under MVP, the Trusted List is maintained by the WP4 Trust Infrastructure group. Identification and listing SHALL use the data required by [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Annex IV/V and the notification requirements per [RPACANot_02](../../task2-trust-framework/trust-infrastructure-schema.md#311-member-state-notification-to-european-commission). Trusted Lists SHALL be published and linked via the List of Trusted Lists (LoTL) per [ETSI TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf).

### 2. Certificate Policy and Operational Scope

The WRPAC/WRPRC Authority's Trusted List entry describes the scope of services the authority is authorised to provide — specifically, issuing WRPAC and/or WRPRC certificates to registered Relying Parties. The WRPAC/WRPRC Authority SHALL maintain a published Certificate Policy (CP) and Certification Practice Statement (CPS) meeting the requirements of [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Annex IV/V and at least the Normalised Certificate Policy (NCP) requirements per [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf). The CP and CPS SHALL be syntactically and semantically harmonised across the Union. Sectorial and interoperability requirements are set by the applicable regulations and technical specifications.

---

## 1. Administrative Onboarding

Each WRPAC/WRPRC Authority that intends to issue Wallet-Relying Party Access Certificates and/or Wallet-Relying Party Registration Certificates to registered Relying Parties SHALL apply to be listed on the Trusted List of WRPAC/WRPRC Authorities. Under [MVP], the application SHALL be submitted to the WP4 Trust Infrastructure group. Under [MVP+], the authority SHALL be notified by the Member State to the European Commission per the process described in sections 2.1–2.5.

*Preconditions:*

- **Prerequisites [MVP]**:
    - The WRPAC/WRPRC Authority SHALL be a beneficiary or an Associated Member of the WEBUILD Consortium.
- **Prerequisites [MVP+]**:
    - The Member State SHALL have designated at least one Supervisory Body responsible for authorising WRPAC/WRPRC Authorities.
    - Member States SHALL notify WRPAC/WRPRC Authorities to the European Commission per [Trust Infrastructure Schema — Member State Notification to European Commission](../../task2-trust-framework/trust-infrastructure-schema.md#311-member-state-notification-to-european-commission); the European Commission SHALL compile and publish the EU-level Trusted List of WRPAC/WRPRC Authorities per [Trust Infrastructure Schema — Responsibilities Matrix](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix).
- **Triggers**:
    - A WRPAC/WRPRC Authority that intends to issue WRPAC and/or WRPRC certificates submits an application to be listed.

*Postconditions:*

- **Success**:
    - [MVP] The WP4 Trust Infrastructure group accepts the WRPAC/WRPRC Authority's application.
    - [MVP+] The Member State / Supervisory Body accepts the application and notifies the European Commission.
    - The WRPAC/WRPRC Authority receives a positive response to the application.
- **Failure**:
    - [MVP] The WP4 Trust Infrastructure group rejects the WRPAC/WRPRC Authority's application.
    - [MVP+] The Member State / Supervisory Body rejects the application.
- **Outputs**:
    - The WRPAC/WRPRC Authority is included in the Trusted List for WRPAC/WRPRC Authorities.
    - A WRPAC/WRPRC Authority certificate is issued to the WRPAC/WRPRC Authority.
    - The WRPAC/WRPRC Authority MAY proceed to issue WRPAC and/or WRPRC certificates to registered Relying Parties.

[MVP]

### 1.1 WRPAC/WRPRC Authority Requests Onboarding

1. The WRPAC/WRPRC Authority SHALL submit an onboarding request via the Open Social platform of the WEBUILD Consortium.
2. The [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group) SHALL provide a data collection form and request the following information from the WRPAC/WRPRC Authority:
    1. Legal name of the WRPAC/WRPRC Authority
    2. Trade name (including EUID where applicable)
    3. Legal address
    4. Country (Member State) in which the WRPAC/WRPRC Authority is established
    5. URI to published terms and conditions
    6. Statement whether the WRPAC/WRPRC Authority is a QTSP
    7. Statement whether the WRPAC/WRPRC Authority is a single-person company
    8. One of:
        1. An X.509 Certificate Signing Request (CSR); or
        2. An X.509 certificate conforming to the profile in [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) section 5, together with a signature over a challenge generated by the [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group), using the private key corresponding to the certificate's public key.

### 1.2 Onboarding Request Review

The [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group) SHALL review the onboarding request, verifying that:

- The WRPAC/WRPRC Authority is a beneficiary or associated partner of the WEBUILD Consortium; and
- Either a Certificate Signing Request is provided in the expected format, **or** an X.509 certificate is provided with the expected profile **and** the signed challenge carries a valid signature over the certificate's public key.

> **Note**: The Trust Infrastructure Responsible Group MAY verify whether the submitted data is accurate or complete but is not obligated to do so.

If the review is successful, the Trust Infrastructure Responsible Group SHALL approve the WRPAC/WRPRC Authority for inclusion in the Trusted List.

If the review is unsuccessful, the Trust Infrastructure Responsible Group SHALL inform the WRPAC/WRPRC Authority of the outcome and MAY request additional or corrected data.

### 1.3 Trusted List of WRPAC/WRPRC Authorities Is Updated

Under [MVP], the **WP4 Trust Infrastructure group** (acting as Trusted List Provider) SHALL maintain and update the LoTL and the single Trusted List of WRPAC/WRPRC Authorities for WEBUILD. There is no EU-level or Member State–level WRPAC/WRPRC Authority Trusted List in MVP.

Upon successful review:

- The WRPAC/WRPRC Authority SHALL receive a notification of the successful outcome.
- If a CSR was submitted, the Ecosystem Authority SHALL issue an X.509 certificate to the WRPAC/WRPRC Authority and return it.
- The Trusted List Provider (WP4) SHALL update the Trusted List of WRPAC/WRPRC Authorities with the authority's entry, including the issued or submitted certificate.
- The WRPAC/WRPRC Authority SHALL be notified of the updated Trusted List.

[MVP+]

### 2.1 WRPAC/WRPRC Authority Requests Onboarding

The WRPAC/WRPRC Authority SHALL submit an onboarding request to the Member State / Supervisory Body, providing evidence of compliance with [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Annex IV (WRPAC) and/or Annex V (WRPRC). The submission SHALL include a published Certificate Policy (CP) and Certification Practice Statement (CPS) meeting at least NCP requirements per [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf) and [ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf).

### 2.2 Member State / Supervisory Body Reviews Onboarding Request

The Member State / Supervisory Body SHALL review compliance with [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Annex IV/V requirements, including verification that:

- The CP/CPS is syntactically and semantically harmonised across the Union; and
- The CP/CPS meets at least NCP requirements per [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf); and
- The WRPAC Authority's certificate issuance practices comply with [ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf).

### 2.3 Member State / Supervisory Body Approves Onboarding and Notifies European Commission

Upon approval, the Member State SHALL notify the European Commission per [GenNot_01 / RPACANot_02](../../task2-trust-framework/trust-infrastructure-schema.md#311-member-state-notification-to-european-commission), providing:

- Identification data of the WRPAC/WRPRC Authority; and
- Trust anchors (public keys or certificates) of the WRPAC/WRPRC Authority.

### 2.4 Member State / Supervisory Body Confirms Successful Onboarding

The Member State / Supervisory Body SHALL confirm the successful outcome to the WRPAC/WRPRC Authority and SHALL inform the authority that the European Commission will update the EU-level Trusted List of WRPAC/WRPRC Authorities.

### 2.5 Trusted List of WRPAC/WRPRC Authorities Is Updated

Under [MVP+], the **European Commission** SHALL compile, maintain, and publish the EU-level Trusted List of WRPAC/WRPRC Authorities. Upon receipt of the Member State notification, the Commission SHALL update the Trusted List accordingly. The Trusted List of WRPAC/WRPRC Authorities SHALL NOT be maintained at Member State level. See [Trust Infrastructure Schema — Overview](../../task2-trust-framework/trust-infrastructure-schema.md#overview).

---

## 2. Technical Onboarding

WRPAC/WRPRC Authorities do not have a separate technical onboarding phase. X.509 certificates for the WRPAC/WRPRC Authority SHALL be issued as part of Administrative Onboarding (see sections 1.3 and 2.5). Certificate profile and issuance are described in [Task 3 — X.509 PKI with ETSI Alignments](../../task3-x509-pki-etsi/README.md) and [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) section 5. Trusted List entries and service digital identities SHALL follow [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).

---

## 3. Post-Onboarding

Once a WRPAC/WRPRC Authority is listed on the Trusted List, the Member State / Supervisory Body and the European Commission (as Trusted List Provider) SHALL monitor compliance and keep the Trusted List accurate. Any change in the WRPAC/WRPRC Authority's status or operational data — whether initiated by the Member State, another competent authority, or the WRPAC/WRPRC Authority itself — SHALL trigger an update to the Trusted List entry or de-listing, and MAY require revocation or update of the authority's certificates in line with applicable regulations.

*Preconditions:*

- **Prerequisites [MVP]**:
    - The WP4 Trust Infrastructure group SHALL act as Ecosystem Authority and Trusted List Provider and SHALL have defined procedures for listing, updates, and de-listing.
- **Prerequisites [MVP+]**:
    - The Member State / Supervisory Body and the European Commission (as Trusted List Provider) SHALL have defined procedures for monitoring, Trusted List updates, de-listing, and certificate revocation per [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848), [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng), and eIDAS/ETSI Trusted List provisions.

- **Triggers**:
    - A change in the WRPAC/WRPRC Authority's operational data (e.g. legal name, trust anchors, CP/CPS URL);
    - A Member State, Supervisory Body, or other competent authority decision to suspend or withdraw authorisation;
    - The WRPAC/WRPRC Authority no longer intends to issue WRPAC/WRPRC certificates, or requests de-listing;
    - Non-compliance with [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Annex IV/V requirements or applicable ETSI standards.

*Postconditions:*

- **Success**:
    - Trusted List entries SHALL be updated or the WRPAC/WRPRC Authority SHALL be de-listed without undue delay.
    - WRPAC/WRPRC Authority certificates in the Trusted List entry SHALL be revoked or updated when required.
    - The WRPAC/WRPRC Authority and other interested parties SHALL be informed of listing status changes.
- **Outputs**:
    - Updated or removed Trusted List entries; published certificate revocation information where applicable.

### 3.1 Trusted List / WRPAC/WRPRC Authority Monitoring

The Member State / Supervisory Body and the European Commission (as Trusted List Provider) SHALL monitor listed WRPAC/WRPRC Authorities for continued compliance with [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) Annex IV/V requirements and [ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf). Monitoring SHOULD include changes in legal status, CP/CPS compliance, and notifications from competent authorities. Trusted Lists SHALL be maintained and published per [ETSI TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) and [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf). See [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md) and [ARF – Trusted Lists](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/).

### 3.2 Trusted List Update

The WRPAC/WRPRC Authority SHALL notify the Member State / Supervisory Body (or, under [MVP], the [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group)) of any change to its operational data (e.g. legal name, trust anchors, CP/CPS URL) without undue delay. The Trusted List Provider SHALL update the Trusted List entry so that published information remains accurate. Under [MVP+], Member States SHALL notify the European Commission of changes as required; Trusted List content and format SHALL follow [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) and applicable ETSI Trusted List specifications.

### 3.3 De-listing / Suspension

The Ecosystem Authority (under [MVP]) or the Member State / Supervisory Body (under [MVP+]) MAY decide to de-list a WRPAC/WRPRC Authority, or to set the Trusted List entry status to suspended or invalid, where required by regulation or where the authority no longer meets the conditions for listing (e.g. loss of authorisation, non-compliance with CP/CPS requirements, or request by the WRPAC/WRPRC Authority itself). De-listing or status change SHALL be performed by the Trusted List Provider without undue delay. The WRPAC/WRPRC Authority SHALL be informed of the decision and, where applicable, of available means of redress or appeal.

*Requirements:*
- [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848), Articles 7, 8
- [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng)
- eIDAS Article 22 (Trusted Lists)

### 3.4 WRPAC/WRPRC Authority Certificate Revocation

When a WRPAC/WRPRC Authority is de-listed or its Trusted List entry status is set to invalid or suspended, the X.509 certificate(s) recorded in the Trusted List entry for that authority SHALL be revoked or updated without undue delay. Revocation status SHALL be published in line with the Trusted List and the applicable certificate policy (e.g. CRL, OCSP). Under [MVP], the Ecosystem Authority (as issuer of WRPAC/WRPRC Authority certificates) SHALL revoke certificates when the Trusted List entry is removed or invalidated. Under [MVP+], the body responsible for issuing the authority's certificates SHALL follow the same principle in line with national and Union requirements. See [Task 3 — X.509 PKI with ETSI Alignments](../../task3-x509-pki-etsi/README.md) and the ETSI EN 319 412 series for certificate lifecycle.

---

## Normative References

See [Normative References](onboarding-base.md#normative-references) for all references applicable across onboarding use cases. The following references are specific to WRPAC/WRPRC Authority onboarding:

- [CIR (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848) — Commission Implementing Regulation on the registration of wallet-relying parties (Articles 7, 8, Annex IV, Annex V)
- [ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf) — Access Certificate Policy for EUDI Wallet Relying Parties
- [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.04.01_60/en_31941101v010401p.pdf) v1.4.1 (2023-10) — General policy requirements for Trust Service Providers issuing certificates (NCP requirements)
- [ETSI TS 119 475 v1.2.1](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.02.01_60/ts_119475v010201p.pdf) — Relying party attributes supporting EUDI Wallet user's authorisation decisions (WRPRC content and format)
- [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf) — Lists of trusted entities; data model (Trusted List structure for WRPAC/WRPRC Authorities)
- [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) v01.00.00 — Certificate profile for PID, Wallet, EAA, QEAA, and PSBEAA providers (WRPAC/WRPRC Authority certificate profile, section 5)
- [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng) — Amending eIDAS; establishing the European Digital Identity Framework (eIDAS Article 22 — Trusted Lists)