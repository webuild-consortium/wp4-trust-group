## Use Case: UC-01 Relying Party Onboarding

## Basic Information
- **Use Case ID**: UC-01
- **Title**: Relying Party Onboarding
- **Category**: Onboarding
- **Priority**: [High | Medium | Low]
- **Complexity**: [Simple | Medium | Complex]
- **Version**: 1.1
- **Last Updated**: 22/10/2025

## Actors
- **Primary Actor**: Relying Party
- **Secondary Actors**: Registrar, Access Certificate Authority, Provider of Registration Certificate

## Goal
- **Business Goal**: To register Relying Parties that intend to rely on European Digital Identity Wallets (EUDI Wallets) for the provision of digital public or private services (ref. [Regulation (EU) 2025/848, Recital 1](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848))
- **Technical Goal**: To establish a harmonised, secure, and interoperable framework for the registration, certification, and lifecycle management of Relying Parties, enabling trusted interaction between EUDI Wallet Solutions and other parties involved.
- **Success Criteria**:
    - *Interoperability across Member States*
        - All Relying Party Access and Registration Certificates are syntactically and semantically harmonised in line with ETSI EN 319 411-1 version 1.4.1 (2023-10) and related IETF RFCs ([RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519), [RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392), [RFC 9162](https://datatracker.ietf.org/doc/html/rfc9162)) (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
        - Certificates and registration data can be validated cross-border in an automated manner using Trusted Lists as defined in [ETSI TS 119 612 v2.4.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) and [ETSI TS 119 602 v1.1.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf).
    - *Secure trust establishment*
        - Each Relying Party’s identity and attributes are verifiable via National Registers and anchored in the EU trust framework (ref. [Regulation (EU) 2024/1183, Article 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)).
        - Continuous monitoring and automatic Access and Registration Certificate revocation mechanisms are implemented and effective within 24 hours of a change request (ref. [Regulation (EU) 2025/848, Article 9(5)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - *Transparency and traceability*
        - All Certificate issuances, renewals, and revocations are logged (optionally under RFC 9162 – Certificate Transparency v2.0) and made publicly accessible for validation (ref. [Regulation (EU) 2025/848, Annex IV 3(j), Annex V 3(i)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
        - Revocation and validity information is provided freely (free of charge), automatically, and reliably (ref. [Regulation (EU) 2025/848, Annex IV 5, Annex V 6](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - *Compliance and accountability*
        - Certificate Policies (CP) and Certification Practice Statements (CPS) follow ETSI EN 319 411-1 version 1.4.1 (2023-10) NCP requirements (ref. [Regulation (EU) 2025/848, Annex IV 3, Annex V 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
        - Each Member State designates at least one Registrar and maintains at least one National Register and communicates changes to the Commission and other Member States (ref. [Regulation (EU) 2025/848, Article 3](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
    - *Operational effectiveness*
        - Onboarding of new Relying Parties is completed through a dual-phase process (administrative + technical) with measurable outcomes and turnaround times.
        - End-to-end validation of Access and Registration Certificates succeeds automatically through Trusted List integration (see [Task 3 - ETSI Trusted Lists Implementation Profile](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)), except for Relying Parties that are not themselves listed on a Union Trusted List.

## Preconditions
- Member State must have established at least one National Register of Relying Parties (ref. [Regulation (EU) 2025/848, Article 3 "National registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- Member State must have designated at least one Registrar (ref. [Regulation (EU) 2025/848, Article 3 "National registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- Member State must have authorised at least one Certificate Authority to issue Relying Party Access Certificates (ref. [Regulation (EU) 2025/848, Article 7 "Wallet-relying party access certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- Member State must have authorised at least one Certificate Authority to issue Relying Party Registration Certificates (ref. [Regulation (EU) 2025/848, Article 8 "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)). See also [ARF "3.19 Providers of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#319-providers-of-registration-certificates:~:text=3.19-,Providers%20of%20registration%20certificates,-If%20a%20Registrar) and [ARF "6.4.2 Relying Party registration"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#642-relying-party-registration:~:text=6.4.2%20Relying%20Party-,registration,-Figure%2011%20depicts).
- Member State must have published one or more national Registration Policies, including or reusing existing sectoral or national registration policies (ref. [Regulation (EU) 2025/848, Article 4 "Registration policies"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)).
- The European Commission must be notified about the Registrar, the Access Certificate Authority, and the Provider of Registration Certificate. (ref. [Regulation (EU) 2024/2980, Article 4 "Notifications by Member States"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202402980&qid=1733300667869)).

## Main Flow
**1. Administrative Onboarding**
- 1.1 Registration Application
- 1.2 Registration Review
- 1.3 Registration Confirmation
- 1.4 Publication in the National Register

**2. Technical Onboarding**
- 2.1 Access Certificate Request
- 2.2 Access Certificate Request Review
- 2.3 Access Certificate Issuance
- 2.4 Registration Certificate Request
- 2.5 Registration Certificate Request Review
- 2.6 Registration Certificate Issuance

**3. Post Onboarding**
- 3.1 Registration Monitoring
- 3.2 Registration Update
- 3.3 Registration Suspension / Cancellation
- 3.4 Access / Registration Certificate Revocation

## 1. Administrative Onboarding
Each Relying Party that intends to rely on European Digital Identity Wallets (EUDI Wallets) for the provision of digital public or private services will register itself with a Registrar in its Member State. If the registration process is successful, the Registrar includes the Relying Party in its public registry.

*Preconditions:*
- **Prerequisites**:
    - Its Member State has established at least one National Register of Relying Parties;
    - Its Member State has designated at least one Registrar;
    - Its Member State has published one or more national Registration Policies;
    - The European Commission has been notified about the Registrar and the National Register.
- **Triggers**:
    - The Relying Party, that intends to rely on European Digital Identity Wallets (EUDI Wallets) for the provision of digital public or private services, decides to submit a registration application.
    
*Postconditions:*
- **Success**:
    - The Registrar accepts the Relying Party registration application;
    - The Relying Party gets a positive response to the registration application.
- **Failure**:
    - The Registrar rejects the Relying Party registration application.
- **Outputs**:
    - The Relying Party gets included in the Registrar public registry;
    - The Relying Party can proceed with the Technical Onboarding phase to obtain one or more Access Certificate(s) and one or more Registration Certificate(s).

### 1.1 Registration Application
The Relying Party submits the registration application to the Registrar, providing at least the information set out in Annex I.

The Registrar receives the registration application for inclusion in the National Register.

*Requirements:*
- [Regulation (EU) 2025/848, Article 3 "National registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)
    -   1. Member States shall make the **information** set out in **Annex I** on registered wallet-relying parties publicly available online, **both in human-readable form and in a form suitable for automated processing.**
    -    5. The information referred to in paragraph 2 shall be available through a single common application programming interface (‘**API**’) and through a national website. It shall be **electronically signed or sealed** by or on behalf of the registrar, in accordance with the common requirements for a single API set out in Section 1 of **Annex II**.
- [Regulation (EU) 2025/848, Article 4. "Registration policies"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 5. Where appropriate, the requirements set out in the national registration policy shall **not impede an automated registration process.**
- [Regulation (EU) 2025/848, Article 5 "Information to be provided to the national registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_5:~:text=automated%20registration%20process.-,Article%C2%A05,-Information%20to%20be)
    - 1. Wallet-relying parties shall at least provide the **information set out in Annex I to national registers.**
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 1. Registrars shall establish **easy to use electronic, and where possible, automated registration processes** for wallet-relying parties.
- [Regulation (EU) 2025/848, Annex I "Information regarding wallet-relying parties"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)
See also [EC TS06 v1.0 - Common Set of Relying Party Information to be Registered](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md) and [EC TS05 V1.0 - Common Formats and API for Relying Party Registration Information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md)
    - Summary of the information to be provided:
        - official name of the wallet-relying party
        - one or more official identifiers of the wallet-relying party (EORI, LEI, VAT number...)
        - physical address and Member State if not present in official identifier
        - URL belonging to the wallet-relying party where applicable
        - detailed contact information (phone number, website or email)
        - description of the type of services provided
        - a list of the attributes that the wallet-relying party intends to request for each intended use
        - a description of intended use of the data
        - indication whether the wallet-relying party is a public sector body
        - applicable entitlement(s) of the wallet-relying party chosen between:
            - **Service_Provider**
            - QEAA_Provider
            - Non_Q_EAA_Provider
            - PUB_EAA_Provider
            - PID_Provider
            - QCert_for_ESeal_Provider
            - QCert_for_ESig_Provider
            - rQSigCDs_Provider
            - rQSealCDs_Provider
            - ESig_ESeal_Creation_Provider
        - indication if the wallet-relying party intends to act **as an intermediary or to rely upon an intermediary**.
- [Regulation (EU) 2025/848, Annex II "1.   Requirements for Electronic signature or seals applied to the information made available on registered Wallet-Relying Parties referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=1.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20FOR%20ELECTRONIC%20SIGNATURES%20OR%20SEALS%20APPLIED%20TO%20THE%20INFORMATION%20MADE%20AVAILABLE%20ON%20REGISTERED%20WALLET%2DRELYING%20PARTIES%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
    - JavaScript Object Notation (‘JSON’).
    - IETF RFC 7515 for JSON Web Signatures.
- [Regulation (EU) 2025/848, Annex II "2.   Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=2.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20ON%20THE%20SINGLE%20COMMON%20API%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
    - (1) The single common API shall:
        - (a) be a **REST API**, supporting **JSON** as a format and signed in accordance with the relevant requirements specified in Section 1;
        -    (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying parties, the name of the wallet-relying parties or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14, and 15;
        -    (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, current and historic wallet-relying party access certificates and wallet-relying party registration certificates but exclude the contact information in Annex I point 4;
        - (d) be published as an OpenAPI version 3, together with the appropriate documentation and technical specifications ensuring interoperability across the Union;
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    - (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.
- [ARF "A.2.3.27 Topic 27 - Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=A.2.3.27%20Topic%2027%20%2D%20Registration%20of%20PID%20Providers%2C%20Providers%20of%20QEAAs%2C%20PuB%2DEAAs%2C%20and%20non%2Dqualified%20EAAs%2C%20and%20Relying%20Parties)
    - PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and **Relying Parties register with a Registrar in their Member State**. The main goal of the registration process is for the Registrar to register relevant information about the registering entity, and make this information available online to interested parties.

### 1.2 Registration Review
The Registrar verifies the registration application.

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 3. Where possible, registrars shall verify in an automated manner:
        - (a) the accuracy, validity, authenticity and integrity of the information required under Article 5;
        - (b) where applicable, the power of attorney of representatives of the wallet-relying parties drawn up and submitted in accordance with the laws and procedures of the Member State where the national register is established;
        - (c ) the type of entitlement or entitlements of the wallet-relying parties as set out in Annex I;
        - (d) the absence of an existing registration in another national register.
    - 4. Registrars shall verify the information set out in paragraph 3 against the supporting documentation provided by the wallet-relying parties or against appropriate authentic sources or other official electronic records in the Member State where the national register is established and to which the registrars have access in accordance with the applicable national laws and procedures.
    - 5. The verification of entitlements of wallet-relying parties referred to in paragraph 3, point (c) shall be carried out in accordance with Annex III.

### 1.3 Registration Confirmation
The Registrar validates or rejects the registration application (the application status becomes "accepted or rejected").

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 6. Where the registrar **cannot verify the information** in accordance with paragraphs 3 to 5, the registrar shall reject the registration.

The Relying Party receives positive or negative feedback on registration application.

*Requirements:*
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_4:~:text=Article%C2%A04-,Registration%20policies,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 2. Registrars shall process applications for registration **without undue delay and provide a response** to the application for registration to the applicant within the timeframe defined in the applicable registration policy, using appropriate means and in accordance with the laws and procedures of the Member State where the national register is established.

###  1.4 Publication in the National Register
The Registrar registers the Relying Party in its registry and publishes it.

*Requirements:*
- [ARF "6.4.2 Relying Party registration"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#642-relying-party-registration)
See also [ARF, Annex II - High-Level Requirements "A. General requirements for Member State registration processes"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=A.%20General%20requirements%20for%20Member%20State%20registration%20processes) and ["E. Requirements of the registration of Relying party"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=E.%20Requirements%20for%20the%20registration%20of%20Relying%20Parties)
    - [...] each Relying Party will register itself with a Registrar in its Member State. If the registration process is successful, **the Registrar includes the Relying Party in its public registry**.

## 2. Technical Onboarding
Following successful registration, each Relying Party enters a technical onboarding process, harmonized between Member States, to acquire two mandatory certificates:
- the Access Certificate(s), which is required for technical connection and authentication with Wallet Units;
- the Registration Certificate(s), which confirms eligibility to provide services relying on the EUDI Wallets.

*Preconditions:*
- **Prerequisites**:
    - Its Member State has authorised at least one Certificate Authority to issue Relying Party Access Certificates;
    - Its Member State has authorised at least one Certificate Authority to issue Relying Party Registration Certificates;
    - The European Commission has been notified about the Access Certificate Authority and the Provider of Registration Certificate;
    - The Relying Party has successfully completed the Administrative Onboarding phase and is listed in a National Register, notified by the Member State to the EU Commission;
    - The Registrar has included the Relying Party in its public registry.
- **Triggers**:
    - The positive completion of the Relying Party registration process.

*Postconditions:*
- **Success**:
    - The Relying Party receives valid Access and Registration Certificates, both registered and verifiable through the national registry and the EU trust framework;
- **Failure**:
    - The request for Access / Registration Certificate issuance is rejected (e.g. due to inconsistent registry data, failed identity verification, or policy non-compliance).
- **Outputs**:
    - The Relying Party is fully onboarded and authorised to interact with EUDI Wallets.

### 2.1 Access Certificate Request
The Registrar informs the Access Certificate Authority about the registered Relying Party.

The Access Certificate Authority receives the input and starts the review process for the issuing of the Access Certificate.

*Requirements:*
- [Regulation (EU) 2025/848, Article 7. "Wallet-relying party access certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 3. Member States shall implement in a syntactically and semantically harmonised manner the certificate policies and certificate practice statements for the wallet-relying party access certificates, in accordance with the requirements set out in Annex IV.
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 1. The wallet-relying party access certificate policy applicable to the provision of wallet-relying party access certificates shall describe the security requirements that apply to, and the rules that indicate the applicability of, a wallet-relying party access certificate so that wallet-relying parties can be issued with and use those certificates in their interactions with wallet solutions.
    - 2. The wallet-relying party access certificate practice statement applicable to the provision of wallet-relying party access certificates shall describe the practices that a provider of wallet-relying party access certificates employs in issuing, managing, revoking, and re-keying wallet-relying party access certificates.
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates shall be syntactically and semantically harmonised across the Union and shall, as applicable, comply with at least the normalised certificate policy (‘NCP’) requirements as specified in standard ETSI EN 319411-1 version 1.4.1 (2023-10).

### 2.2 Access Certificate Request Review
The Access Certificate Authority verifies the identity and any other attributes of the Relying Party.

The Access Certificate Authority checks the valid registration status and information coherency within a national register in which that Relying Party is established.

*Requirements:*
- [Regulation (EU) 2025/848, Article 7. "Wallet-relying party access certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_5:~:text=Article%C2%A07-,Wallet%2Drelying%20party%20access%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - Member States shall ensure that providers of wallet-relying party access certificates issue wallet-relying party access certificates **exclusively to registered wallet-relying parties**.
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates [...] shall include:
        - (a) **a clear description of the public key infrastructure hierarchy** and certification paths from the end-entity wallet-relying party access certificates up to the top of the hierarchy used for issuing them, **indicating the expected trust anchor(s)** in such hierarchy and paths which should rely on the trust framework established in accordance with Article 5a(18) of Regulation (EU) No 910/2014;
        - (b) a comprehensive description of the procedures for the issuance of wallet-relying party access certificates, including for the **verification of the identity and any other attributes of the wallet-relying party** to which a wallet-relying party certificate is to be issued;
        - (c ) the obligation for the providers of wallet-relying party access certificates, when issuing a wallet-relying party access certificate, to verify that:
            - the wallet-relying party is included, **with a valid registration status, in a national register** of wallet-relying parties of the Member State in which that wallet-relying party is established;
            - any information in the wallet-relying party access certificate is accurate and consistent with the registration information available from that register.

### 2.3 Access Certificate Issuance

The Access Certificate Authority issues the Access Certificate and logs the Access Certificate issued.

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates […] shall include:
        - (j) a description, where relevant, on how a provider of wallet-relying party access certificates **logs all wallet-relying party access certificates they have issued**, in compliance with internet engineering task force (‘**IETF**’) request for comments (‘**RFC**’) **9162 Certificate Transparency version 2.0**;
        - (k) the obligation for the wallet-relying party access certificates to include:
            - the location where the certificate supporting the advanced electronic signature or advanced electronic seal on that certificate is available, for the entire certification path to be built up to the expected trust anchor in the public key infrastructure hierarchy used by the provider;
            - a machine processable reference to the applicable certificate policy and certificate practice statement;
            - the information referred to in Annex I, points 1, 2, 3, 5, 6 and 7, (a), (b) and (c).
- [ARF "3.18 Access Certificate Authorities"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#318-access-certificate-authorities:~:text=each%20Member%20State.-,3.18%20Access%20Certificate%20Authorities,-Access%20Certificate%20Authorities)
    - Access Certificate Authorities **issue access certificate to all** PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers and **Relying Parties** in the EUDI Wallet ecosystem.
- [ARF "6.4.2 Relying Party registration"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#642-relying-party-registration:~:text=6.4.2%20Relying%20Party-,registration,-Figure%2011%20depicts)
    - As a result of successful registration:
        - **an Access Certificate Authority (see Section 3.18) associated with the Registrar issues an access certificate to each Relying Party Instance of the Relying Party**. A Relying Party Instance needs such a certificate to authenticate itself towards Wallet Units when requesting the presentation of attributes, as described in Section 6.6.3.2. Issuing access certificates to a registered Relying Party is mandatory.
- [ARF, Annex II, Topic 27 "Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)
See also [ARF, Annex II - High-Level Requirements "B. General requirements for the issuance of access certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#:~:text=B.%20General%20requirements%20for%20the%20issuance%20of%20access%20certificates) and ["F. Requirements for the contents of access certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2331-topic-31---notification-and-publication-of-pid-provider-wallet-provider-attestation-provider-access-certificate-authority-and-provider-of-registration-certificates:~:text=F.%20Requirements%20for%20the%20contents%20of%20access%20certificates)
    - A registering Relying Party will **receive an Access Certificate for each of the Relying Party Instances it uses** to interact with Wallet Units to request the presentation of attestations.
- [Topic X "Relying Party Registration" / "2.2 Draft CIR on Relying Party registration"](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/discussion-topics/x-relying-party-registration.md)
    - The registrant receives **one or more Relying Party Access Certificates**.
    - Requirements for Relying party access certificates:
        - **X.509 certificate** with certificate policy and certificate practice statement
        - shall comply with **IETF RFC 3647**
        - plus additional requirements set out in the Annex IV

The Registrar keeps records of the issuance of Relying Party Access Certificate for 10 years and publishes its history within a common REST API (JSON format).

*Requirements:*
- [Regulation (EU) 2025/848, Article 10 "Record keeping"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - Registrars shall keep records of the information provided by wallet-relying parties and registered in accordance with Annex I for the registration of a wallet-relying party and the issuance of the wallet-relying party access certificates and the wallet-relying party registration certificates, and of any subsequent changes to this information, **for 10 years**.
- [Regulation (EU) 2025/848, Annex II "Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - (1) The single common API shall:
        - (a) **be a REST API**, supporting JSON as a format and signed in accordance with the relevant requirements specified in Section 1;
        - (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying party, the name of the wallet-relying party or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14 and 15;
        - (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, current and historic wallet-relying party access certificates and wallet-relying party registration certificates but exclude the contact information in Annex I point 4;
        - (d) be published as an OpenAPI version 3, together with the appropriate documentation and technical specifications ensuring interoperability across the Union;
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it.
    - (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.

### 2.4 Registration Certificate Request
The Registrar informs the Provider of Registration Certificate about the registered Relying Party.

The Provider of Registration Certificate receives the input and starts the review process for the issuing of the Registration Certificate.

*Requirements:*
- [Regulation (EU) 2025/848, Article 8. "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    - 2. Where a Member State authorised the issuance of a wallet-relying party registration certificate, that Member State shall:
        - (f) implement dedicated certificate policies and certificate practice statements for the wallet-relying party registration certificates in accordance with the requirements set out in Annex V;
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 1. The wallet-relying party registration certificate policy applicable to the provision of wallet-relying party registration certificates shall describe the security requirements that apply to, and the rules that indicate the applicability of, a wallet-relying party registration certificate for their issuance to and use by wallet-relying parties in their interactions with wallet solutions. The wallet-relying party registration certificate policy shall be published in **human-readable**.
    - 2. The wallet-relying party registration certificate practice statement applicable to the provisioning of wallet-relying party registration certificates shall describe the practices that a provider of wallet-relying party registration certificates employs in issuing, managing, revoking, and re-keying wallet-relying party registration certificates, and, where applicable, how they relate to wallet-relying party access certificates issued to wallet-relying parties. The wallet-relying party registration certificate practice statement shall be published in **human-readable**.
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates shall be **syntactically and semantically harmonised** across the Union and shall comply with at least the applicable NCP requirements as specified in standard **ETSI EN 319411-1 version 1.4.1 (2023-10).**

### 2.5 Registration Certificate Request Review
The Provider of Registration Certificate verifies the identity and any other attributes of the Relying Party.

The Provider of Registration Certificate checks the valid registration status and information coherency within a national register in which that Relying Party is established.

*Requirements:*
- [Regulation (EU) 2025/848, Article 8. "Wallet-relying party registration certificates"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_8:~:text=Article%C2%A08-,Wallet%2Drelying%20party%20registration%20certificates,-1.%C2%A0%C2%A0%C2%A0Member%20States)
    -  2. Where a Member State authorised the issuance of a wallet-relying party registration certificate, that Member State shall:
        - (a) require providers of wallet-relying party registration certificates to issue wallet-relying party registration certificates **exclusively to registered wallet-relying parties**;
        - (b) **ensure that each intended use is expressed** in the wallet-relying party registration certificates
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - The certificate policy and certificate practice statement applicable to the provision of wallet-relying party registration certificates [...] shall include:
        - (a) a **clear description of the public key infrastructure hierarchy** and certification paths from the end-entity wallet-relying party access certificates up to the top of the hierarchy used for issuing them, **indicating the expected trust anchor(s)** in such hierarchy and paths which should rely on the trust framework established in accordance with Article 5a(18) of Regulation (EU) No 910/2014;
        - (b) a comprehensive description of the procedures for the issuance of wallet-relying party registration certificates, including for the **verification of the identity and any other attributes of the wallet-relying party** to which a wallet-relying party certificate is to be issued;
        - (c) the obligation for the provider of wallet-relying party registration certificates, when issuing a wallet-relying party registration certificate, to verify that:
            - the wallet-relying party is included, **with a valid registration status, in a national register** for Relying parties of the Member State in which that wallet-relying party is established;
            - the **information** in the wallet-relying party registration certificate is accurate and consistent with the registration information available from that register;
            - the wallet-relying party **access certificate is valid**;
            - the description of the procedures for revocation of wallet-relying party registration certificates is comprehensive.

### 2.6 Registration Certificate Issuance
The Provider of Registration Certificate issues the Registration Certificate and logs the Registration Certificate issued.

*Requirements:*
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates [...] shall include:
        - (i) The provider of wallet-relying party registration certificates **logs all wallet-relying party registration certificates they have issued**;
        - (j) The obligation for the wallet-relying party registration certificates:
            -    to include the location where the validation data of the advanced electronic signature or advanced electronic seal for the certificate used to sign or seal the registration certificate is available, for the entire trust chain to be built up to the **expected trust anchor**;
            - to include a machine-readable **reference to the applicable certificate policy and certificate practice statement**;
            - to include the **information** referred to in Annex I, points 1, 2, 3, 5, 6 and 8, 9, 10, 11, 12, 13, 14 and 15;
            - to include the **URL to the privacy policy** referred to in Article 8(2)g;
            - 	to include a **general access policy** as referred to in Article 8(3);
    - 4. The data exchange format for the relying party registration certificate shall be signed **JSON Web Tokens (IETF RFC 7519)** and **CBOR Web Tokens (IETF RFC 8392).**
- [ARF "3.19 Providers of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#319-providers-of-registration-certificates:~:text=3.19-,Providers%20of%20registration%20certificates,-If%20a%20Registrar)
    - If a Registrar has a policy of issuing registration certificates, it has one or more associated Provider(s) of registration certificates. Such a Provider **issues one or more registration certificates to each registered Relying Party**, PID Provider, QEAA Provider, PuB-EAA Provider, and non-qualified EAA Provider. Each registration certificate **contains (a subset of) the data registered for that entity**, as described in Section 3.17.
- [ARF "6.4.2 Relying Party registration"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#642-relying-party-registration:~:text=6.4.2%20Relying%20Party-,registration,-Figure%2011%20depicts)
    - As a result of successful registration:
        - **a Provider of registration certificates (see Section 3.19) associated with the Registrar will issue one or more registration certificates to the Relying Party**, if the Registrar has a policy of issuing such registration certificates. The purpose of the registration certificate is described in Section 6.6.3.3. It is up to each Registrar to decide if it issues registration certificates.
- [ARF, Annex II, Topic 27 "Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)
    - Finally, the registering entity will **receive one or more Registration Certificates containing the registered information**, if the Registrar has a policy of issuing such registration certificates.
- [ARF, Annex II, Topic 44 "Registration certificates for PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=A.2.3.44%20Topic%2044%20%2D%20Registration%20certificates%20for%20PID%20Providers%2C%20Providers%20of%20QEAAs%2C%20PuB%2DEAAs%2C%20and%20non%2Dqualified%20EAAs%2C%20and%20Relying%20Parties)
See also ["A. Generic requirements on the specification and contents of registration certificates"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=A.%20Generic%20requirements%20on%20the%20specification%20and%20contents%20of%20registration%20certificates) and  ["B. Requirements on the issuance of registration certificates to Relying Parties"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties:~:text=B%20Requirements%20on%20the%20issuance%20of%20registration%20certificates%20to%20Relying%20Parties).
    - As a Relying party is obliged to register for each purpose ("intended use") separately, multiple registration certificates may be issued to a single Relying party, where **each certificate is related to one specific intended use**. As specified in Technical Specification 5, the Registrar assigns an identifier to each registered intended use of a Relying party. A registration certificate also contains information about the intermediary used by this Relying Party, if applicable.
- [Topic X "Relying Party Registration" / "2.2 Draft CIR on Relying Party registration"](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/discussion-topics/x-relying-party-registration.md)
    - The registrant receives **one or more Relying Party Registration Certificates**.
    - Requirements for Relying party registration certificates:
        - certificate policy and certificate practice statement shall comply with **IETF RFC 3647** and **IETF RFC 5755**
        - includes the information referred to in **Annex I, points 1, 2 and 8**
        - expresses attributes in way compliant with **IETF RFC 5755**
        - plus additional requirements set out in the **Annex V**

The Registrar keeps records of the issuance of Relying Party Registration Certificate for 10 years and publishes its history within a common REST API (JSON format).
- [Regulation (EU) 2025/848, Article 10. "Record keeping"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_10:~:text=Article%C2%A010-,Record%20keeping,-Registrars%20shall%20keep)
    - Registrars shall **keep records of the information provided** by wallet-relying parties and registered in accordance with Annex I for the registration of a wallet-relying party and the issuance of the wallet-relying party access certificates and the wallet-relying party registration certificates, and of any subsequent changes to this information, **for 10 years**.
- [Regulation (EU) 2025/848, Annex II. "2. Requirements on the single common API referred to in Article 3"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_II:~:text=2.%C2%A0%C2%A0%C2%A0REQUIREMENTS%20ON%20THE%20SINGLE%20COMMON%20API%20REFERRED%20TO%20IN%20ARTICLE%C2%A03)
    - (1) The single common API shall:
        - (a) be a **REST API**, supporting **JSON** as a format and signed in accordance with the relevant requirements specified in Section 1;
        - (b) allow any requestor, without prior authentication, to search and request complete lists to the register, for information about registered wallet-relying parties, allowing for partial matches based on defined parameters including, where applicable, the official or business registration number of the wallet-relying party, the name of the wallet-relying party or the information referred to in Article 8, paragraph 2, point (g) and Annex I points 12, 13, 14, and 15;
        - (c) ensure that replies to requests referred to in point (b) that match at least one wallet-relying party shall include one or more statements on information about registered wallet-relying parties and information according to Annex I, **current and historic wallet-relying party access certificates and wallet-relying party registration certificates** but exclude the contact information in Annex I point 4;
        - (d) be published as an **OpenAPI version 3**, together with the appropriate documentation and technical specifications ensuring interoperability across the Union;
        - (e) provide security functions, including security by default and by design, to ensure the availability and integrity of the API and the availability of information through it;
    -  (2) The statements referred to in point (c) shall be expressed under the form of **electronically signed or sealed JSON files**, with a format and structure in accordance with the requirements on electronic signatures or seals set out Section 1.

## 3. Post-Onboarding
Once the Access and Registration Certificates are active, the Relying Party may start offering its registered services to EUDI Wallet Users. It must keep its registration information up to date and comply with certification and revocation policies. Any suspension, cancellation, or change in the Relying Party’s status or intended use - whether initiated by the Registrar, another competent authority, or the Relying Party itself - triggers the update or revocation of its certificates and registry data in line with EU harmonised procedures.

*Preconditions:*
- **Prerequisites**:
    - The Registration Policy, Access / Registration Certificate Policy and Practice Statement are defined and published at national level and harmonised across the Union so that continuous monitoring mechanisms and revocation procedures are in place.
- **Triggers**:
    - Change in the Relying Party’s registration data (e.g. legal status or intended use);
    - Automated detection of inconsistency or invalid data during monitoring by the Registrar or other competent authorities;
    - Notification from competent authorities (e.g. Supervisory Body, Data Protection Authority, Access Certificate Authority, Provider of Registration Certificate) regarding the need for registration or certificates suspension / cancellation / revocation.

*Postconditions:*
- **Success**:
    - The Relying Party updates the existing registration (possibly through automated means) and maintains valid certificates aligned with registry information;
    - The Registrar informs the Access Certificate Authority, the Provider of Registration Certificate and the affected Relying Party about the Relying Party suspension or cancellation without undue delay (≤ 24 hours after the event);
    - The issued Access / Registration Certificate are revoked according to the certificate policy and the certificate practice statement (e.g. when the content of the certificate is no longer accurate and consistent with the information registered, or when the registration of the Relying Party is modified, suspended or cancelled);
    - Updates on Access / Registration Certificates revocation are processed automatically and published within prescribed timeframes (e.g. ≤ 24 hours after request).
- **Failure**:
    - The competent authorities do not properly follow the defined measures and processes on certificates revocation.
- **Outputs**:
    - Updated and published certificate status and revocation information;
    - Audit logs and monitoring records for compliance verification;
    - Notifications to the Relying Party and other interested parties of any registration or certificates status change.

### 3.1 Registration Monitoring

The Registrar monitors continuously.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 2.Registrars may suspend or cancel a registration of a wallet-relying party where the registrars have reasons to believe one of the following:
        - (a) the registration contains **information**, which is **inaccurate**, out of date or misleading;
        - (b) the wallet-relying party is **not compliant** with the registration policy;
        - (c) the wallet-relying party is **requesting more attributes **than they have registered in accordance with Article 5 and Article 6;
        - (d) the wallet-relying party is otherwise **acting in breach of Union or national law** in a manner related to their role as wallet-relying party.

The Provider of Registration Certificate monitors continuously and automatically.

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates [...] shall include:
        - (e) the obligation for the providers of wallet-relying party access certificates to implement measures and processes on:
            - **continuously monitoring** any changes in the national register for wallet-relying party in which wallet-relying party to whom they have issued wallet-relying party access certificates are registered;
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (d) the obligation for the provider of wallet-relying party registration certificates implements measures and processes on:
          - **continuously monitoring** in an automated manner any changes in the national register for wallet-relying party in which wallet-relying party to whom they have issued wallet-relying party registration certificates are registered;
 
### 3.2 Registration Update
When needed, the Relying Party updates information.

The Registrar receives the updated information.

*Requirements:*
- [Regulation (EU) 2025/848, Article 5. "Information to be provided to the national registers"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_5:~:text=Information%20to%20be%20provided%20to%20the%20national%20registers)
     - 2. Wallet-relying party shall ensure that the **information provided is accurate** at the time of registration.
     - 3. Wallet-relying party **shall update any information previously registered** in the national register of wallet-relying parties **without undue delay.**
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
         - (d) the obligation for the provider of Wallet-Relying Party Registration Certificates to implement measures and processes concerning:
            - **reissuing the Wallet-Relying Party Registration Certificate**.

### 3.3 Registration Suspension / Cancellation
If:
- The National Registrar conducts a proportionality assessment whose results lead to the Relying Party registration suspension or cancellation.
- The Relying Party requests the Relying Party registration cancellation.
- The Supervisory Body requests the Relying Party registration suspension/ cancellation.

Then:
The Registrar suspends/ revokes the Relying Party registration.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 1. Registrars shall suspend or cancel a registration of a wallet-relying party where such a suspension or cancellation is **requested by a supervisory body** pursuant to Article 46a(4), point (f) of Regulation (EU) No 910/2014.
    - 3. Registrars shall suspend or cancel a registration of a wallet-relying party where the **request for cancellation or suspension is made by the same wallet-relying party.**
    - 4. When considering the suspension or cancellation in accordance with paragraph 2, the registrar shall conduct a **proportionality assessment**, taking into account the impact on the fundamental rights, security and confidentiality of the users in the ecosystem, as well as the severity of the disruption envisaged to be caused by the suspension or cancellation and the associated costs, both for the wallet-relying party and the user. Based on the result of this assessment, **the registrar may suspend or cancel the registration with or without prior notice to the affected wallet-relying party**.
- [Regulation (EU) 2025/848, Article 6. "Registration processes"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_6:~:text=Article%C2%A06-,Registration%20processes,-1.%C2%A0%C2%A0%C2%A0Registrars%20shall)
    - 7. When a wallet-relying party **no longer intends to rely upon wallet units** for the provision of public or private services under a specific registration, it shall **notify the relevant registrar without undue delay and request the cancellation of that registration**.
- [ARF "6.4.3 Relying Party suspension or cancellation"](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/#643-relying-party-suspension-or-cancellation:~:text=Topic%2027.-,6.4.3%20Relying%20Party%20suspension%20or%20cancellation,-Under%20specific%20conditions)
    - Under specific conditions, a **Registrar may decide to suspend or cancel registration of a registered Relying Party**. The conditions for this will be specified by each Registrar.
    - Suspension or cancellation involves revocation of all valid Relying Party Instance access certificates by the relevant Access CA, such that **the Relying Party is no longer able to interact with Wallet Units**.

The Registrar sends notice about the Relying Party registration suspension / revocation.

The Relying Party receives notice of its registration suspension / revocation.

The Access Certificate Authority receives notice of the Relying Party registration suspension/ revocation.

The Provider of Registration Certificate receives notice of the Relying Party registration suspension / revocation.

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 5.   Where the registration of a wallet-relying party is suspended or cancelled, the **registrar shall inform** **the provider of the relevant wallet-relying party access certificates**, the **provider of the relevant wallet-relying party registration certificates**, and the **affected wallet-relying party** of this action **without undue delay and not later than 24 hours after the suspension or cancellation.** This notification shall include **information** on the reasons for the suspension or cancellation and on the available means of **redress or appeal**.

### 3.4 Access / Registration Certificate Revocation
If:
- The Registrar suspends / cancels the Relying Party registration.
- The Relying Party requests the Relying Party Access / Registration Certificate revocation.
- The Supervisory Body requests the Relying Party Access / Registration certificate revocation.
- Data Protection Authority requests the Relying Party Access / Registration certificate revocation.

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates [...] shall include:
        - (g) the obligation for the providers of wallet-relying party access certificates to **allow** relevant stakeholders, including **wallet-relying parties** as regards their own certificates, **competent supervisory bodies** and **data protection authorities**, **to request the revocation** of wallet-relying party access certificates;
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (f) the obligation for the provider of wallet-relying party registration certificates to **allow** relevant stakeholders, including **wallet-relying parties** as regards their own certificates, competent **supervisory bodies** and **data protection authorities**, **to request the revocation** of wallet-relying party registration certificates;

Then:
- The Access Certificate Authority revokes the Access Certificate (without undue delay).
- The Provider of Registration Certificate revokes the Registration Certificate (without undue delay).

*Requirements:*
- [Regulation (EU) 2025/848, Article 9. "Suspension and cancellation of registration"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#art_9:~:text=Suspension%20and%20cancellation%20of%20registration)
    - 6. **The provider of wallet-relying party access certificates** and the **provider of wallet-relying party registration certificates**, shall, where applicable, **revoke without undue delay the wallet-relying party access certificates, and the wallet-relying party registration certificates,** respectively, of the wallet-relying party for which registration has been suspended or cancelled.
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The certificate policy and certificate practice statement applicable to the provision of wallet-relying party access certificates [...] shall include:
        - (d) a comprehensive description of the **procedures for revocation of wallet-relying party access certificates**;
        - (e) the obligation for the providers of wallet-relying party access certificates to implement **measures and processes** on:
            - **revoking**, when changes require, **any wallet-relying party certificate** that the provider issued to the corresponding wallet-relying party, in particular when the content of the certificate is **no longer accurate and consistent** with the information registered, or **when the registration of the wallet-relying party is suspended or cancelled**.
     - 4. The revocation set out in point 3(g) **shall become effective immediately** upon its publication.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
        - (c) the obligation for the provider of wallet-relying party registration certificates, when issuing a wallet-relying party registration certificate, to verify that:
            - the **description of the procedures for revocation** of wallet-relying party registration certificates is comprehensive.
        - (d) the obligation for the provider of wallet-relying party registration certificates implements **measures and processes** on:
            -    **revoking any wallet-relying party registration certificate** that they issued to the corresponding wallet-relying party, when such changes so require, in particular when the content of the certificate is **no longer accurate and consistent** with the information registered, or **when the registration of the wallet-relying party is modified, suspended or cancelled**.
    - 5. The revocation referred to in point 3(g/f) **shall become effective immediately** upon its publication.

- The Access Certificate Authority publishes the Access Certificate revocation status (within 24 hours).
- The Provider of Registration Certificate publishes the Registration Certificate revocation status (within 24 hours).

*Requirements:*
- [Regulation (EU) 2025/848, Annex IV "Requirements for wallet-relying party access certificates referred to in Article 7"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20access%20certificates%20referred%20to%20in%20Article%C2%A07)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
            - (h) the obligation for the providers of wallet-relying party access certificates to register all such revocations in its certificate database and **to publish the revocation status of the certificate in a timely manner**, and in any event **within 24 hours after** receipt of the revocation request;
            - (i) the obligation for the providers of wallet-relying party access certificates to provide **information on the validity or revocation status** of wallet-relying party certificates issued by that provider;
    - 6. The information set out in point 3(h) shall be made available at least on a per certificate basis at any time and at least beyond the validity period of the certificate in an **automated manner** that is reliable, **free of charge** and effectively in accordance with the certificate policy.
- [Regulation (EU) 2025/848, Annex V "Requirements for wallet-relying party registration certificates referred to in Article 8"](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500848#anx_IV:~:text=Requirements%20for%20wallet%2Drelying%20party%20registration%20certificates%20referred%20to%20in%20Article%C2%A08)
    - 3. The wallet-relying party registration certificate policy and certificate practice statement applicable to the provisioning of wallet-relying party registration certificates […] shall include:
            - (g) the obligation for the provider of wallet-relying party registration certificates to register all such revocations in its certificate database and **to publish the revocation status of the certificate in a timely manner**, and in any event **within 24 hours after** the receipt of the request for revocation;
            - (h) the obligation for the providers of wallet-relying party registration certificates to provide **information on the validity or revocation status** of wallet-relying party registration certificates issued by that provider;
    - 6. The information referred to in point 3(h/g) shall be made available at least on a per certificate basis at any time and at least beyond the validity period of the certificate in an **automated manner** that is reliable, **free of charge** and effectively in accordance with the certificate policy.

---

## Normative References

This document is based on the following normative references:

### Architecture and Reference Framework (ARF)
- **ARF Version**: 2.7.3
- **ARF Main Document**: [EUDI Wallet Architecture and Reference Framework 2.7.3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/architecture-and-reference-framework-main/)
- **ARF Annex II - High-Level Requirements**: [Annex II - High-Level Requirements](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/annexes/annex-2/annex-2-high-level-requirements/)

### Project-Specific References
- **Task 2 - Trust Framework**: See [Trust Framework documentation](../task2-trust-framework/README.md) for trust evaluation, trust management, and policy framework definitions
- **Task 3 - X.509 PKI with ETSI Alignments**: See [X.509 PKI documentation](../task3-x509-pki-etsi/README.md) for certificate management, ETSI compliance, and trusted lists implementation
- **Task 2 - Entities Involved**: See [Entities Involved in Trust Evaluation](../task2-trust-framework/entities-involved.md) for definitions of Trusted List Provider, Access Certificate Authority, Provider of Registration Certificates, and other trust infrastructure entities

### Implementing Acts (IAs)
- **Regulation (EU) 2025/848**: [Commission Implementing Regulation (EU) 2025/848](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202500848)
- **Regulation (EU) 2024/2980**: [Commission Implementing Regulation (EU) 2024/2980, Article 4 "Notifications by Member States"](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202402980&qid=1733300667869)
- **Regulation (EU) 2024/1183**: [Regulation (EU) 2024/1183, Article 5a(18)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)

### European Commission Technical Specifications
- **EC TS05 V1.0** (2025-06): [Common Formats and API for Relying Party Registration Information](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md)
- **EC TS06 v1.0** (2025-06): [Common Set of Relying Party Information to be Registered](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md)
- **EUDI Wallet Essential Standards and Technical Specifications (STS)**: [Essential Standards and Technical Specifications (STS)](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/2.7.3/technical-specifications/#:~:text=Essential%20Standards%20and%20Technical%20Specifications%20(STS))

### ETSI Standards
- **ETSI TS 119 612** (v2.4.1): [Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf)
- **ETSI TS 119 602** (v1.1.1): [Electronic Signatures and Trust Infrastructures (ESI); Trusted lists; Data model. Trusted lists in other formats, such as JSON, CBOR or ASN.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf)
- **ETSI TS 119 411-8** (v01.01.01): [Access Certificate Policy for EUDI Wallet Relying Parties](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf)
- **ETSI TS 119 475** (v01.01.01): [Relying party attributes supporting EUDI Wallet User's authorisation decisions (Relying Party Attributes)](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.01.01_60/ts_119475v010101p.pdf)
- **ETSI TS 119 472-2** (v1.1.1): [Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 2: Profiles for EAA/PID Presentations to Relying Party](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.01.01_60/ts_11947202v010101p.pdf)
- **ETSI EN 319 411-1**: Version 1.4.1 (2023-10) - Normalised Certificate Policy (NCP) requirements
- **ETSI EN 319 412-6** (v01.00.00): [Certificate profile requirements for PID, Wallet, EAA, QEAA and PSBEAA providers](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf)

### IETF Standards
- **IETF RFC 5280**: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
- **IETF RFC 5914**: Trust Anchor Format
- **IETF RFC 3647**: Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework
- **IETF RFC 5755**: An Internet Attribute Certificate Profile for Authorization
- **IETF RFC 7515**: JSON Web Signature (JWS)
- **IETF RFC 7519**: JSON Web Token (JWT)
- **IETF RFC 8392**: CBOR Web Token (CWT)
- **IETF RFC 9162**: Certificate Transparency Version 2.0
