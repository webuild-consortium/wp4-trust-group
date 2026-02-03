# Use Case: UC-03 Wallet Provider Onboarding

## Scope

This document describes the Wallet Provider onboarding process. The Trusted List of Wallet Providers is intended to convey trust in a set of legal entities and their solutions within [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng). Wallet Providers are notified by Member States to the European Commission for inclusion in Trusted Lists.

This use case aligns with the [Trust Infrastructure Schema](../task2-trust-framework/trust-infrastructure-schema.md), which defines the overall architecture and notification process. See [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix) for details.

This document follows the WEBUILD ecosystem structure; see [MVP and MVP+ Definitions](onboarding-base.md#mvp-and-mvp-definitions) in the base document.

Wherever feasible, this specification aligns with processes defined in Regulation (EU) 2024/1183 and the [Architecture and Reference Framework](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/), interpreting them for the testing purposes specific to WEBUILD.

For the common framework (terminology, MVP/MVP+, success criteria, preconditions), see [Base Onboarding Framework](onboarding-base.md). This document defines only **Wallet Provider–specific** content; it does not duplicate the base.

## Terminology and Acronyms

See [Terminology and Acronyms](onboarding-base.md#terminology-and-acronyms) in the base document.

## Actors


- **Primary Actor [MVP]**:
    - Beneficiaries and Associated Partners providing a prototype of a EUDI Wallet for natural persons
    - Beneficiaries and Associated Partners providing a prototype of a European Business Wallet
- **Secondary Actors [MVP]**:
    - Ecosystem Authority: WEBUILD WP4 Trust Infrastructure group
    - Trusted List Provider: WEBUILD WP4 Trust Infrastructure group
      Please note: The Trust Infrastructure group is not a legal entity. However, the ecosystem authority may be
      required to provide certain information (e.g., legal name, company address) and to digitally sign data. For
      testing purposes, we therefore recommend designating at least one representative of the Trust Infrastructure group
      who is authorized to perform digital signing on behalf of the legal entity they represent.

- **Primary Actor [MVP+]**:
    - EUDI Wallet Provider for natural persons
    - European Business Wallet Providers for legal persons
- **Secondary Actors [MVP+]**:
    - Supervisory Body entitled by a Member State of the European Union (alternative names: Registrar or Ecosystem
      Authority)
    - Trusted List Provider (alternative name: List of trusted entity scheme operator)



## Goal


- **Technical Goal [MVP]**: To establish an onboarding process for wallet providers on a trusted list, enabling trusted
  interaction between EUDI Wallet Units and other parties involved.

- **Business Goal [MVP+]**: Establish Trust Anchors for cryptographic trust validation to identify certified
  Providers and certified solutions of
    - EUDI Wallets for natural persons [CIR 2025/849](https://data.europa.eu/eli/reg_impl/2025/849/oj)
    - European Business
      Wallets [Proposal for a Regulation (EU) 2025/0358 (COD) ](https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-establishment-european-business-wallets)
- **Success Criteria**:
    - [MVP] Pilot implementations successfully demonstrate wallet providers' onboarding; all wallet providers within WEBUILD are included on a publicly accessible trusted list maintained by the WP4 Trust Infrastructure group.
    - [MVP+] See [Success Criteria](onboarding-base.md#success-criteria). Wallet Provider–specific: onboarding via notification (not registration with Registrar); trust anchors published in Trusted Lists (see [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix)).

## Preconditions

### Preconditions [MVP]

- The WEBUILD WP4 Trust Infrastructure group is assigned to act as Ecosystem Authority and Trusted List Provider for all WEBUILD participants.
- A Trusted List for Wallet Providers is available for onboarding.
- WP4 Trust Infrastructure group has assigned responsibilities for the onboarding process.
- Wallet Providers are able to provide the requested data.

See [RACI Matrix](onboarding-base.md#raci-matrix) in the base document for RACI acronym definition and role definitions.

| RACI MATRIX - WP4 Trust Infrastructure Group                     | Lead/ Co-Lead | WP 4 - Testing |[Responsible](onboarding-base.md#trust-infrastructure-responsible-group)| [Participant] |
|------------------------------------------------------------------|---------------|----------------|--------------|---------------|
| Announce onboarding request to Wallet Providers                  |       A,C     |                |      R       |       I       |
| Set up and manage a form to gather data from Wallet Providers    |       A,C     |                |      R       |       I       |
| Review Wallet Provider Data                                      |       A,C     |                |      R       |       I       |
| Decide upon listing and de-listing (Ecosystem Authority)         |       A,C     |                |      R       |       I       |
| Inform about decision                                            |       A,C     |                |      R       |       I       |
| Enable updates on Trusted Lists (Trusted List Provider)          |       A,C     |                |      R       |       I       |
| Host the Trusted List for Wallet Providers                       |       A,C     |                |      R       |       I       |
| Engage with Wallet Providers during onboarding / troubleshooting |       A,C     |                |      R       |       I       |
| Set up wallet conformity assessment                              |       I       |      A,R       |      C       |       I       |

**Onboarding phase – responsibilities by actor**: The following table assigns responsibility (R), accountability (A), consulted (C), or informed (I) for each administrative onboarding step. [MVP]: Ecosystem Authority and Trusted List Provider are the WP4 Trust Infrastructure group; [MVP+]: Supervisory Body and MS Trusted List Provider apply.

| Step | Wallet Provider | Ecosystem Authority / Supervisory Body | Trusted List Provider |
|------|-----------------|----------------------------------------|------------------------|
| [MVP] 1.1 Request onboarding | R (submit request and data) | A (provide form, receive) | I |
| [MVP] 1.2 Onboarding request review | C (clarify if requested) | R, A (review, decide) | I |
| [MVP] 1.3 Trusted List updated | I (notified) | R, A (approve, trigger update) | R (update TL, issue certificates) |
| [MVP+] 2.1 Request onboarding | R (conformity assessment, submit to Supervisory Body) | A (receive) | I |
| [MVP+] 2.2 Review onboarding request | C (clarify if requested) | R, A (review per CIR 2024/2981) | I |
| [MVP+] 2.3 Approve onboarding to Trusted List | I | R, A (approve, generate unique ref. id.) | I |
| [MVP+] 2.4 Confirm successful onboarding | I (receive report) | R, A (confirm) | I |
| [MVP+] 2.5 Trusted List updated | I (notified) | A | R (update TL) |

### Preconditions [MVP+]

- Each Member State must have designated at least one Supervisory Body responsible for qualifying EUDI wallet providers to onboard to a Trusted List.
- Each Member State must have designated at least one Trusted List provider ([Regulation EU 2024/1183 - Article 22(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1)).
- The onboarding Wallet Provider can present proof of successfully passing an EUDI Wallet certification process according to [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj).

## Data Model

[MVP]

- As a baseline, there will be a single Trusted List for all wallet providers in WEBUILD to reduce complexity.

### Trusted List and certificate profile

- Trusted Lists for Wallet Providers comply with [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf). See [ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) for detailed implementation guidance, including Wallet Provider Trusted List data model, service entries, and profile-specific requirements.
- Wallet Provider Certificate Profile: See [Task 3 - X.509 PKI with ETSI Alignments](../task3-x509-pki-etsi/README.md) for certificate profile specifications. Certificates follow [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) (v01.00.00), section 5.
- Wallet Unit Attestation: [EWC RFC 004 - Individual Wallet Attestation](https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/ewc-rfc004-individual-wallet-attestation.md), [OIDC4VCI 1.0, Appendix E](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html#appendix-E)
- Unique reference identifier for the wallet solution according to [CIR 2025/849 Annex 2(a)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849)
- [Token Status List](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-status-list-12) (OAuth 2.0 Token Status List)

### Data to be provided

The Wallet Provider must provide the following when requesting onboarding. [MVP]: submitted via the form provided by the Trust Infrastructure Responsible Group; [MVP+]: as required by the Supervisory Body and the regulations below. Normative: [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng) (wallet providers, Trusted Lists, Article 22(3)); [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj) (conformity assessment, certification of EUDI Wallets); [CIR 2025/849](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849) (unique reference identifier per Annex 2(a), wallet solution data). Technical: [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf) (Trusted List structure, wallet solution service entries); [ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) (Wallet Provider Trusted List data model).

*About the Wallet Provider (legal entity):*
- Legal name of the wallet provider
- Trade name (including EUID where applicable)
- Legal address
- Country (Member State) in which the Wallet Provider is registered
- URI to terms and conditions
- Statement whether the Wallet Provider is a QTSP
- Statement whether the Wallet Provider is a single-person company

*About each Wallet Solution:*
- Statement whether the solution is an EUDI Wallet for natural persons or a European Business Wallet for legal persons
- Name of the Wallet Solution
- URI to the Wallet Solution
- URI of the Wallet Solution's status list entry (optional)
- Details on associated body, if applicable
- X.509 certificate signing request (required for issuance of the wallet solution certificate; certificate profile and issuance process: [Task 3 - X.509 PKI with ETSI Alignments](../task3-x509-pki-etsi/README.md), [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) section 5; Trusted List entry includes the issued certificate per [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf))
- Unique reference identifier of the wallet solution (optional; [MVP+] per CIR 2025/849 Annex 2(a))

## Main Flow

**1. Onboarding via Trust Infrastructure Responsible Group [MVP]**

- 1.1 Wallet Provider requests onboarding
- 1.2 Onboarding Request Review
- 1.3 Trusted List of Wallet Providers is updated


**2. Onboarding via Supervisory Body [MVP+]**

- 2.1 Wallet Provider requests onboarding
- 2.2 Supervisory Body reviews onboarding request
- 2.3 Supervisory Body approves onboarding to Trusted List
- 2.4 Supervisory Body confirms successful administrative onboarding
- 2.5 Trusted List of Wallet Providers is updated

**2. Technical Onboarding**

- Certificate issuance for wallet solutions is part of Administrative Onboarding (see 1.3, 2.5). See [Task 3](../task3-x509-pki-etsi/README.md), [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf), [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).

**3. Post-Onboarding**

- 3.1 Trusted List / Wallet Provider Monitoring
- 3.2 Trusted List Update
- 3.3 De-listing / Suspension
- 3.4 Wallet Solution Certificate / Status Revocation

## Industrial-Scale Considerations

The following apply to Wallet Provider onboarding (notification and Trusted List listing) at scale. Framework context: [Task 2 - Trust Framework](../task2-trust-framework/README.md).

### 1. Entity Identification and Trusted List Integration

Wallet Providers are **notified** by Member States to the European Commission and do not register with a Registrar. They are listed on the **Trusted List of Wallet Providers**, which is compiled and published by the **European Commission** (MVP+); see [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix). For MVP, the Trusted List is maintained by the WP4 Trust Infrastructure group. Identification and listing use the data required by the Supervisory Body and [CIR 2024/2981](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202402981) / [CIR 2025/849](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849). Trusted Lists are published and linked via the [List of Trusted Lists (LoTL)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (ETSI TS 119 612).

### 2. Attribute and Wallet Solution Scope

Wallet solutions (EUDI Wallet for natural persons, European Business Wallet for legal persons) and their certified scope are described in the Trusted List entry. Conformity assessment and certification define the attributes and functionalities the wallet solution supports; sectorial and interoperability requirements are set by the applicable regulations and technical specifications.

## 1. Administrative Onboarding

Each Wallet Provider that intends to provide a European Digital Identity Wallet for natural persons or a European Business Wallet for legal persons will register itself and its wallet solution at WP 4 Trust Registry Infrastructure Working Group in WEBUILD. If the application process is successful, WP4 Trust Registry Infrastructure Working Group will update the Trusted List of Wallet Providers.

_Preconditions:_

- **Prerequisites [MVP]**
    - The Wallet Provider is a beneficiary or an Associated Member of the WEBUILD Consortium
- **Triggers**:
    - The Wallet Provider, that intends to provide a European Digital Identity Wallets (EUDI Wallets) or a European Business Wallet, applies to be listed.
- **Prerequisites [MVP+]**:
    - Member State has designated at least one Supervisory Body responsible for qualifying Wallet Providers.
    - Member States notify Wallet Providers to the European Commission (per [Trust Infrastructure Schema - Member State Notification to European Commission](../task2-trust-framework/trust-infrastructure-schema.md#311-member-state-notification-to-european-commission)); the European Commission compiles and publishes the EU-level Trusted List of Wallet Providers (per [Trust Infrastructure Schema - Responsibilities Matrix](../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix)).
    - The Wallet Provider has successfully certified its wallet solution according to [CIR 2024/2981](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202402981).

_Postconditions:_

- **Success**:
    - [MVP] WP4 Trust Infrastructure group accepts the Wallet application
    - [MVP+] The Supervisory Body accepts the Wallet Provider application;
    - The Wallet Provider gets a positive response to the application.
- **Failure**:
    - [MVP] WP4 Trust Infrastructure group reject the Wallet application
    - [MVP+] The Supervisory Body rejects the Wallet Provider application.
- **Outputs**:
    - The Wallet Provider gets included in the Trusted Lists for Wallet Providers;
    - Wallet Provider Certificate is issued to the Wallet Provider
    - The Wallet Provider can provide their wallet solutions to users.

[MVP]

### 1.1 Wallet Provider requests onboarding

1. Wallet provider requests onboarding via Open Social of the WeBuild Consortium
2. The [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group) provides a form and requests data from the Wallet Provider
3. Wallet provider provides the following data about itself:
    1. legal name of wallet provider
    2. Trade name incl. EUID
    3. legal address
    4. Country name of Member state in which wallet Provider is registered
    5. URI to terms and conditions
    6. statement whether Wallet Provider is a QTSP
    7. statement whether Wallet Provider is a single-person company
4. Wallet Provider provides the following data about its Wallet Solutions:
    1. statement whether wallet solution is an EUDI Wallet for natural persons or a European Business Wallet for legal
       entities
    2. Name of the Wallet Solution
    3. URI to Wallet Solution
    4. URI of Wallet Solution's status list entry in the Wallet Provider's status list (optional)
    5. details on associated body, if applicable
    6. X509 certificate signing request
    7. unique reference identifier of the wallet solution (optional)

### 1.2 Onboarding Request Review

The [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group) reviews the onboarding request, verifying:

- Wallet provider is beneficiary or associated partner of WEBUILD Consortium
- Certificate Signing Request is provided in the expected format

**Note**: The Trust Infrastructure Responsible Group may check whether data is correct or complete, but is not required to do so.

If successful, the Trust Infrastructure Responsible Group approves the Wallet Provider to join the Trusted List for Wallet Providers.
If not successful, the Trust Infrastructure Responsible Group informs about the review result and may request additional data.

### 1.3 Trusted List of Wallet Providers is updated

- Wallet Provider receives a notification about the successful reviewing process.
- X509 certificates for Wallet Solutions are issued by the Ecosystem Authority
- Trusted List Provider updates Trusted List of Wallet Providers.
- Wallet Provider is notified about updated Trusted List.
- Wallet Provider receives a x509 certificate for each of its wallet solutions

[MVP+]

### 2.1 Wallet Provider requests onboarding

1. Wallet Provider passes for Conformity Assessment at dedicated Conformity Assessment Bodies.
2. The Conformity Assessment results are provided to the Supervisory Body.

### 2.2 Supervisory Body reviews onboarding request

1. Supervisory Body reviews compliance according
   to  [CIR 2024/2981](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202402981)

### 2.3 Supervisory Body approves onboarding to Trusted List

1. Supervisory body generates a unique reference identifier for the wallet solution according
   to [CIR 2025/849 Annex 2(a)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849)

### 2.4 Supervisory Body confirms successful administrative onboarding

1. Wallet provider receives a certification assessment report compliant with Article 5c of Regulation (EU) No 910/2014

### 2.5 Trusted List of Wallet Providers is updated

## 2. Technical Onboarding

Wallet Providers do not have a separate technical onboarding phase. X.509 certificates for wallet solutions are issued as part of Administrative Onboarding (see sections 1.3 and 2.5). Certificate profile and issuance are described in [Task 3 - X.509 PKI with ETSI Alignments](../task3-x509-pki-etsi/README.md) and [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) section 5. Trusted List entries and service digital identities follow [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).

## 3. Post-Onboarding

Once a Wallet Provider and its wallet solution(s) are listed on the Trusted List, the Supervisory Body and Trusted List Provider monitor compliance and keep the Trusted List accurate. Any change in the Wallet Provider’s status, certified scope, or conformity—whether initiated by the Supervisory Body, another competent authority, or the Wallet Provider—triggers an update to the Trusted List entry or de-listing, and may require revocation or update of wallet solution certificates or status information in line with applicable regulations.

*Preconditions:*
- **Prerequisites [MVP]**:
    - The WP4 Trust Infrastructure group acts as Ecosystem Authority and Trusted List Provider and has defined procedures for listing, updates, and de-listing.
- **Prerequisites [MVP+]**:
    - The Supervisory Body and Trusted List Provider have defined procedures for monitoring, Trusted List updates, de-listing, and certificate/status revocation per [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng), [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj), [CIR 2025/849](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849), and eIDAS/ETSI Trusted List provisions.
- **Triggers**:
    - Change in the Wallet Provider’s or wallet solution’s data (e.g. legal name, scope, conformity status);
    - Supervisory Body or competent authority decision to suspend, restrict, or withdraw certification or listing;
    - Wallet Provider no longer intends to provide the wallet solution or requests de-listing;
    - Non-compliance with conformity or regulatory requirements.

*Postconditions:*
- **Success**:
    - Trusted List entries are updated or the Wallet Provider/wallet solution is de-listed without undue delay.
    - Wallet solution certificates or status list entries are revoked or updated when required.
    - The Wallet Provider and other interested parties are informed of listing status changes.
- **Outputs**:
    - Updated or removed Trusted List entries; published certificate/status revocation information where applicable.

### 3.1 Trusted List / Wallet Provider Monitoring

The Supervisory Body and Trusted List Provider monitor listed Wallet Providers and their wallet solutions for continued compliance with [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj) and [CIR 2025/849](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849). Monitoring may include conformity surveillance, changes in legal or certification status, and notifications from competent authorities. Trusted Lists are maintained and published per [ETSI TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) and [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf). See [Trust Infrastructure Schema](../task2-trust-framework/trust-infrastructure-schema.md) and [ARF – Trusted Lists](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/).

### 3.2 Trusted List Update

The Wallet Provider notifies the Supervisory Body (or, under [MVP], the [Trust Infrastructure Responsible Group](onboarding-base.md#trust-infrastructure-responsible-group)) of any change to its data or wallet solution(s) without undue delay. The Trusted List Provider updates the Trusted List entry so that published information remains accurate. Under [MVP+], Member States notify the European Commission of changes as required; Trusted List content and format follow [CIR 2025/849](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849) and ETSI Trusted List specifications.

### 3.3 De-listing / Suspension

The Ecosystem Authority (under [MVP]) or the Supervisory Body (under [MVP+]) may decide to de-list a Wallet Provider or a wallet solution, or to set the Trusted List entry status to suspended or invalid, where required by regulation or where the provider no longer meets the conditions for listing (e.g. withdrawal of certification, non-compliance, or request by the Wallet Provider). De-listing or status change is performed by the Trusted List Provider; the Wallet Provider is informed of the decision and, where applicable, of redress or appeal. References: [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng), [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj), [CIR 2025/849](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849), eIDAS Article 22 (Trusted Lists).

### 3.4 Wallet Solution Certificate / Status Revocation

When a Wallet Provider or wallet solution is de-listed or its status is set to invalid/suspended, any X.509 certificates issued for the wallet solution (and, where used, status list entries) are revoked or updated without undue delay. Revocation status is published in line with the Trusted List and certificate policy (e.g. status list, CRL, or OCSP). Under [MVP], the Ecosystem Authority (as issuer of wallet solution certificates) revokes certificates when the Trusted List entry is removed or invalidated. Under [MVP+], the body responsible for issuing wallet solution certificates follows the same principle in line with national and Union requirements. See [Task 3 - X.509 PKI with ETSI Alignments](../task3-x509-pki-etsi/README.md) and ETSI EN 319 412 series for certificate lifecycle.

---

## Normative References

See [Normative References](onboarding-base.md#normative-references) for all references applicable to Wallet Provider onboarding processes, including Wallet Provider-specific references.
