## Use Case: UC-03 Wallet Provider Onboarding

## Basic Information

- **Use Case ID**: UC-03
- **Title**: Wallet Provider Onboarding
- **Category**: Onboarding
- **Priority**: [High]
- **Complexity**: [Medium]
- **Version**: 0.1
- **Last Updated**: 09/01/2026

## Scope

The Trusted List of Wallet Providers is intended to convey trust in a set of legal entities and their solutions
within [REGULATION (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng). The WEBUILD Consortia is tasked
with designing, implementing, and testing the trusted digital business identity ecosystem envisioned by this regulation.
This specification outlines the onboarding process for Wallet Providers within WEBUILD. Whereever feasible, the
specification closely allign to processes defined in the Regulation as well as
the [Architecture and Reference Framework](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#622-wallet-provider-registration-and-notification),
interpreting them for the testing purposes specific to WEBUILD.

## Terminology

(1) ‘wallet solution’ means a combination of software, hardware, services, settings, and configurations, including
wallet instances, one or more wallet secure cryptographic applications and one or more wallet secure cryptographic
devices;
(2) ‘wallet instance’ means the application installed and configured on a wallet user’s device or environment, which is
part of a wallet unit, and that the wallet user uses to interact with the wallet unit;
(3) ‘wallet unit’ means a unique configuration of a wallet solution that includes wallet instances, wallet secure
cryptographic applications and wallet secure cryptographic devices provided by a wallet provider to an individual
wallet user;
(4) ‘wallet provider’ means a natural or legal person who provides wallet solutions

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
    - [MVP] Pilot implementations successfully demonstrate wallet providers' onboarding
    - [MVP] All wallet providers within WEBUILD are included on a publicly accessible trusted list maintained by the WP4 Trust
      Infrastructure group
    - [MVP+] The onboarding process for wallet providers is formally defined and documented in a harmonized manner that aligns
      with EU regulatory and technical frameworks.

## Preconditions

[MVP]

- The WEBUILD WP4 Trust Infrastructure group is assigned to act as Ecosystem Authority and Trusted List Provider for all
  WEBUILD participants
- A Trusted List for Wallet Providers is available for onboarding
- WP4 Trust Infrastructure group has assigned responsibilities for the onboarding process
- Wallet Providers are able to provide the requested data.

| RACI MATRIX - WP4 Trust Infrastructure Group                     | Lead/ Co-Lead | WP 4 - Testing | IDunion SCE | [Participant] |
|------------------------------------------------------------------|---------------|----------------|-------------|---------------|
| Announce onboarding request to Wallet Providers                  |       A,C     |                |      R      |       I       |
| Set up and manage a form to gather data from Wallet Providers    |       A,C     |                |      R      |       I       |
| Review Wallet Provider Data                                      |       A,C     |                |      R      |       I       |
| Decide upon listing and de-listing (Ecosystem Authority)         |       A,C     |                |      R      |       I       |
| Inform about decision                                            |       A,C     |                |      R      |       I       |
| Enable updates on Trusted Lists (Trusted List Provider)          |       A,C     |                |      R      |       I       |
| Host the Trusted List for Wallet Providers                       |       A,C     |                |      R      |       I       |
| Engage with Wallet Providers during onboarding / troubleshooting |       A,C     |                |      R      |       I       |
| Set up wallet conformity assessment                              |       I       |      A,R       |      C      |       I       |

- Responsible (R): The person or group who do the work and execute the task or deliverable.
- Accountable (A): The person or group who owns the result, makes the final decision, and is ultimately answerable for
  success or failure.
- Consulted (C): Person or group who are asked for input or expertise and are involved through two‑way communication
  before or during the task.
- Informed (I): People who are kept up to date on progress or outcomes via one‑way communication but are not involved in
  doing or deciding


[MVP+]

- Each Member State must have designated at least one Supervisory Body responsible for qualifying EUDI wallet providers
  to onboard to a Trusted List.
- Each Member State must have designated at least one Trusted List
  provider ([Regulation EU 2024/1183 - Article 22(3)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1))
- The onboarding Wallet Provider can present
    - proof of successfully passing an EUDI Wallet certification process according
      to [CIR 2024/2981](https://data.europa.eu/eli/reg_impl/2024/2981/oj)


## Data Model

[MVP]

- As a baseline, there will be a single Trusted List for all wallet providers in WEBUILD to reduce complexity.
- Trusted Lists for Wallet Providers comply to ETSI 119 602
- Wallet Provider Certificate Profile: ETSI 119 412-6, section 5
- Wallet Unit Attestion: [https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/ewc-rfc004-individual-wallet-attestation.md](https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/ewc-rfc004-individual-wallet-attestation.md), [OIDC4VCI 1.0, Appendix E](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html#appendix-E)
- unique reference identifier for the wallet solution according
  to [CIR 2025/849 Annex 2(a)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500849)
- [token-status-list](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-status-list-12)


### Trusted List of Entitites Data Model

| LoTE component                                          | Format                                   | Sample value for WEBUILD MVP                                                                                                                    | Notes                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ListAndSchemeInformation                                |                                          |                                                                                                                                                 | Scheme information will be explicitly mentioned  (Article 5d, 2b of Regulation (EU)
No 2024/1183)                                                                                                                                                                                                                                                                  |
| LoTE version identifier (clause 6.3.1)                  | integer                                  | 1                                                                                                                                               | The identifer refers to the ETSI 119 602 version                                                                                                                                                                                                                                                                   |
| LoTE sequence number<br>(clause 6.3.2)                  | integer                                  | 1                                                                                                                                               | The sequence number refers the present Trust List (e.g. for Wallet Providers)                                                                                                                                                                                                                                      |
| LoTE type (clause 6.3.3)                                | URI                                      | http://uri.etsi.org/19602/LoTEType/EUWalletProvidersList                                                                                        | Relying Parties shall not accept any other URI for the TL of Wallet Providers                                                                                                                                                                                                                                      |
| Scheme operator name (clause 6.3.4)                     | multilingual character strings           | EN-WEBUILD WP4 Trust Registry Working Group<br><br>alt: GER-IDunion SCE                                                                         | to be discussed whether this is the Ecosystem Authority or the Trusted List Provider / must be the formal legal name                                                                                                                                                                                               |
| Scheme operator address (clause 6.3.5)                  | - PostalAddresses<br>- ElectronicAddress | Rheinstraße 5<br>63225 Langen<br>DE<br>mailto:info@idunion.eu<br>https://www.idunion.eu                                                         | If the Trust Registry Working Group was selected as Scheme operator, this field remains empty.                                                                                                                                                                                                                     |
| Scheme name (clause 6.3.6)                              | multilingual character strings           | EU:EN_WEBUILD_WALLET_PROVIDER                                                                                                                   |                                                                                                                                                                                                                                                                                                                    |
| Scheme information URI (clause 6.3.7)                   | URI                                      | https://github.com/webuild-consortium/wp4-trust-group/tree/main/task1-use-cases/subtask1-1-onboarding                                           | - 2 URIs shall be present<br>- 1 URI shall lead to an archived version of the Trusted List<br>- 1 URI shall provide information about Wallet Provider Trust List<br>- Sample URI is leading to Subtask 1.1 and shall be replaced by URI leading to a description about Wallet Provider Trusted List infrastructure |
| Status determination <br>approach (clause 6.3.8)        | URI                                      | http://uri.etsi.org/19602/WalletProvidersList/StatusDetn/EU                                                                                     |                                                                                                                                                                                                                                                                                                                    |
| Scheme type/community/rules <br>(clause 6.3.9)          |                                          | http://uri.etsi.org/19602/WalletProvidersList/schemerules/EU                                                                                    |                                                                                                                                                                                                                                                                                                                    |
| Scheme <br>territory (clause 6.3.10)                    | string                                   | EU                                                                                                                                              |                                                                                                                                                                                                                                                                                                                    |
| LoTE policy/legal <br>notice (clause 6.3.11)            | URI or multilingual character strings    | https://github.com/webuild-consortium/wp4-trust-group/tree/main/task1-use-cases/subtask1-1-onboarding                                           | Sample URI is leading to Subtask 1.1 and shall be replaced by URI leading to Wallet Provider onboarding as soon as it is published          -  Article 5d, 2c of Regulation (EU)
No 2024/1183                                                                                                                                                                       |
| Historical information <br>period (clause 6.3.12)       | integer                                  |                                                                                                                                                 | shall not be present                                                                                                                                                                                                                                                                                               |
| Pointers to other <br>LoTEs (clause 6.3.13)             |                                          | [URI where this Trusted List is published]                                                                                                      | The PointersToOtherLoTE component shall contain a pointer to the present <br>wallet providers list itself. <br>                                                                                                                                                                                                    |
| List issue date and <br>time (clause 6.3.14)            | date-time value                          | 2026-03-31T14:30:15Z                                                                                                                            |                                                                                                                                                                                                                                                                                                                    |
| Next update (clause 6.3.15)                             |                                          | 2026-04-30T14:30:15Z                                                                                                                            | - WEBUILD may update the trusted list every months                                                                                                                                                                                                                                                                 |
| Distribution <br>points (clause 6.3.16)                 | URI                                      |                                                                                                                                                 | - this field is optional<br>- if used, it shall have an indication of its criticality<br>- in WEBUILD, this field shall not be present                                                                                                                                                                             |
| Scheme <br>extensions (clause 6.3.17)                   | all formats allowed                      |                                                                                                                                                 | - this field is optional<br>- if used, it shall have an indication of its criticality<br>- in WEBUILD, this field shall not be present                                                                                                                                                                             |
| TE General (clause 6.4.0)                               |                                          |                                                                                                                                                 | - The first published version of the Trusted List for Wallet Providers shall not list any wallet providers<br>                                                                                                                                                                                                     |
| TE name (clause 6.5.1)                                  | multilingual character strings           | DE-Spherity GmbH                                                                                                                                | refers to legal name, not the name of the wallet solution                                                                                                                                                                                                                                                          |
| TE trade name (clause 6.5.2)                            | multilingual character strings           | DE-Spherity DED2601V.HRB31566                                                                                                                   |                                                                                                                                                                                                                                                                                                                    |
| TE address (clause 6.5.3)                               |                                          | Emil-Figge-Straße 80<br>44227 Dortmund <br>DE<br>mailto:info@spherity.com<br>https://www.spherity.com<br>+4923196819760<br>                     |                                                                                                                                                                                                                                                                                                                    |
| TE information URI (clause 6.5.4)                       | sequence of multilingual pointers        | https://www.spherity.com/terms-conditions<br>https://www.spherity.com/eida<br>http://uri.etsi.org/19602/ListOfTrustedEntities/WalletProvider/DE |                                                                                                                                                                                                                                                                                                                    |
| TE information extensions (clause 6.5.5)                |                                          |                                                                                                                                                 | - shall be filled if Associated Bodies are responsible for the provision of the wallet solution                                                                                                                                                                                                                    |
| Service type identifier (clause 6.6.1)                  | URI                                      | http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance<br>http://uri.etsi.org/19602/SvcType/WalletSolution/Revocation                        | - .../Issuance describes the service of the wallet solution, [more information] - for further debate: .../ Revocation shall provide validity status information about the wallet solution --> we assume this URI leads to a Certificate Revocation List hosted by the wallet provider (#issuance-service-entry-of-a-wallet-solution) <br> - .../Revocation describes the service where status list entry of the wallet solution is listed, [more information](#revocation-service-entry-of-a-wallet-solution)             |
| Service name (clause 6.6.2)                             | multilingual character strings           | EU:EUDI Wallet                                                                                                                                  |                                                                                                                                                                                                                                                                                                                    |
| Service digital identity (clause 6.6.3)                 | Base64 string                            | [x509 certificate]                                                                                                                              | - X509 Certificate profile according to ETSI 319 412-6                                                                                                                                                                                                                                                             |
| Service current status (clause 6.6.4)                   | URI                                      |                                                                                                                                                 | - This field shall not be used for a list of wallet providers<br> - the absence of this field means all listed solutions are certified wallet solutions<br> - when certification is expired, the corresponding entry in the wallet provider list shall be removed from the TE service entries                      |
| Current status starting date and<br>time (clause 6.6.5) | Date-time value                          |                                                                                                                                                 | - This field shall not be used for a list of wallet providers<br>                                            |
| Scheme service definition URI<br>(clause 6.6.6)         | URI                                      | https://github.com/webuild-consortium/wp4-trust-group/tree/main/task1-use-cases/subtask1-1-onboarding                                           | Sample URI is leading to Subtask 1.1 and shall be replaced by URI leading to wallet provider onboarding as soon as it is published                                                                                                                                                                                 |
| Service supply points (clause 6.6.7)                    | URI                                      | [URI leading the status list of the wallet solution]                                                                                            | - URI where Relying Parties can obtain the service validity                                                                                                                                                                                                                                                        |
| TE service definition URI<br>(clause 6.6.8)             | URI                                      | https://www.spherity.com/eida                                                                                                                   |                                                                                                                                                                                                                                                                                                                    |
| Service unique identifier extension (clause 6.6.9.1)    | URI                                      | https://www.spherity.com/eida	| The ServiceUniqueIdentifier extension shall be used to provide thereference number of the wallet solution identified through the ServiceName component, as the Commission shall publish this information in the Official Journal of the European Union pursuant to Article 5d of Regulation (EU) No 2024/1183 
 Service history instance (clause 6.7)                   |                                          |                                                                                                                                                 | - this component contains historical information such as the abov mentionted elements ServiceName, ServiceStatus, StatusStartingTime<br> - in ServiceDigitalIdentity only 1 x509 can be used to present the public key                                                                                             |
| Signature (clause 6.8.1)                                | AdES digital signature                   |                                                                                                                                                 | The "Country code" and "Organization" fields in Subject Distinguished Name of the certificate supporting the AdES<br>digital signature shall match respectively the "Scheme Territory" and one of the "Scheme operator name" value                                                                                 |

### Issuance Service Entry of a Wallet Solution

| LoTE component                                          | Format                         | Sample value for WEBUILD MVP                                                                          | notes                                                                                                                              |
|---------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Service type identifier (clause 6.6.1)                  | URI                            | http://uri.etsi.org/19602/SvcType/WalletSolution/Issuance                                             |                                                                                                                                    |
| Service name (clause 6.6.2)                             | multilingual character strings | EU:EUDI Wallet                                                                                        |                                                                                                                                    |
| Service digital identity (clause 6.6.3)                 | Base64 string                  | [x509 certificate]                                                                                    | - X509 Certificate profile according to ETSI 319 412-6                                                                             |
| Service current status (clause 6.6.4)                   | URI                            | -                                                                                                     | - This field shall not be used for a list of wallet providers                                                                      |
| Current status starting date and<br>time (clause 6.6.5) | Date-time value                | -                                                                                                     | - This field shall not be used for a list of wallet providers                                                                      |
| Scheme service definition URI<br>(clause 6.6.6)         | URI                            | https://github.com/webuild-consortium/wp4-trust-group/tree/main/task1-use-cases/subtask1-1-onboarding | Sample URI is leading to Subtask 1.1 and shall be replaced by URI leading to wallet provider onboarding as soon as it is published |
| Service supply points (clause 6.6.7)                    | URI                            | https://www.wallet-solution.com                                                                       | - at least one URI where Relying Parties can access the service                                                                    |
| TE service definition URI<br>(clause 6.6.8)             | URI                            | https://www.spherity.com/eida                                                                         |                                                                                                                                    |
| Service unique identifier extension (clause 6.6.9.1)    | URI                            | wallet_solution_reference_number                                                                      |                                                                                                                                    |

### Revocation Service Entry of a Wallet Solution (Optional)

| LoTE component                                          | Format                         | Sample value for WEBUILD MVP                                                                          | notes                                                                                                                              |
|---------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Service type identifier (clause 6.6.1)                  | URI                            | http://uri.etsi.org/19602/SvcType/WalletSolution/Revocation                                           |                                                                                                                                    |
| Service name (clause 6.6.2)                             | multilingual character strings | EU:Spherity Wallet Solutions Status List                                                              |                                                                                                                                    |
| Service digital identity (clause 6.6.3)                 | Base64 string                  | [x509 certificate]                                                                                    | - X509 Certificate profile according to ETSI 319 412-6                                                                             |
| Service current status (clause 6.6.4)                   | URI                            | -                                                                                                     | - This field shall not be used for a list of wallet providers                                                                      |
| Current status starting date and<br>time (clause 6.6.5) | Date-time value                | -                                                                                                     | - This field shall not be used for a list of wallet providers                                                                      |
| Scheme service definition URI<br>(clause 6.6.6)         | URI                            | https://github.com/webuild-consortium/wp4-trust-group/tree/main/task1-use-cases/subtask1-1-onboarding | Sample URI is leading to Subtask 1.1 and shall be replaced by URI leading to wallet provider onboarding as soon as it is published |
| Service supply points (clause 6.6.7)                    | URI                            | https://www.spherity.com/wallet-solution-status-list/123456                                           | - Entry of Token Status List of Wallet Solutions, published by the Wallet Provider                                                 |
| TE service definition URI<br>(clause 6.6.8)             | URI                            | https://www.spherity.com/eida/status-description                                                      |                                                                                                                                    |
| Service unique identifier extension (clause 6.6.9.1)    | URI                            | wallet_solution_reference_number                                                                      |                                                                                                                                    |

### Wallet Provider Certificate Profile

**Certificate issuer (Wallet Provider Onboarding Authority):**
[ETSI EN 319 412-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.03.01_60/en_31941202v020301p.pdf),
section 4.2.3

| Certificate Field name | Format                  | Sample value for EUDIW MVP                                           | Notes                                           |
|------------------------|-------------------------|----------------------------------------------------------------------|-------------------------------------------------|
| `countryName`          | ISO 3166-2 Country Code | DE                                                                   | -                                               |
| `organizationName`     | string                  | WEBUILD WP4 Trust Registry Working Group<br><br>alt: GER-IDunion SCE | to be discussed / must be the formal legal name |
| `commonName`           | string                  | WEBUILD WP4 Trust Registry Working Group<br><br>alt: GER-IDunion     | Name commonly used to identify the organization |

**Certificate subject (Wallet Provider):**
[ETSI EN 319 412-3](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf),
section 4.2.1

| Certificate Field name | Format                  | Sample value for EUDIW MVP                                     | Notes                                           |
|------------------------|-------------------------|----------------------------------------------------------------|-------------------------------------------------|
| `countryName`          | ISO 3166-2 Country Code | DE                                                             | -                                               |
| `organizationName`     | string                  | Spherity GmbH, tp be discussed / must be the formal legal name |                                                 |
| `commonName`           | string                  | Spherity                                                       | Name commonly used to identify the organization |


## Main Flow

**1. Onboarding via WP4 Trust Infrastructure group [MVP]**

- 1.1 Wallet Provider requests onboarding
- 1.2 WP4 Trust Infrastructure group approves onboarding to Trusted List
- 1.3 Trusted List of Wallet Providers is updated


**2. Onboarding via Supervisory Body [MVP+]**

- 2.1 Wallet Provider requests onboarding
- 2.2 Supervisory Body reviews onboarding request
- 2.3 Supervisory Body approves onboarding to Trusted List
- 2.4 Trusted List of Wallet Providers is updated
- 2.5 Supervisory Body confirms successful administrative onboarding


## Onboarding

Each Wallet Provider that intends to provide a European Digital Identity Wallet for natural persons or a European
Business Wallet for legal persons will register itself and its wallet solution at WP 4 Trust Registry Infrastructure Working Group in WEBUILD.
If the application process is successful, WP4 Trust Registry Infrastructure Working Group will update the Trusted
List of Wallet Providers.

_Preconditions:_

- **Prerequisites [MVP]**
    - The Wallet Provider is a beneficiary or an Associated Member of the WEBUILD Consortium
- **Triggers**:
    - The Wallet Provider, that intends to provide a European Digital Identity Wallets (EUDI Wallets) or a European
      Business Wallet, applies to be listed.
- **Prerequisites [MVP+]**:
    - Member State has designated at least one Supervisory Body;
    - Member State has designated at least one Trusted List Provider;
    - Supervisory Body has delegated the Trusted List Provider to create a national Trusted List for Wallet Providers
    - The Europen Commission has been notified about the creation of the national Trusted List.
    - The European Comission includes national Trusted List in the List of Trusted Lists (LoTL)
    - The Wallet Provider was able to successfully certify its wallet solution according
      to [CIR 2024/2981](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202402981)

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
2. WP4 Trust Infrastructure group provides a form and requests data from the Wallet Provider
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

### 1.2 WP4 Trust Infrastructure group approves onboarding request

Responsible person or group reviews whether

- wallet provider is beneficiary or associated partner of WEBUILD Consortium
- Certificate Signing Request is provided in the expected format

Note: WP4 Trust Infrastructure group will not check whether data is correct or complete.

If successful, responsible Person or group approves Wallet Provider to join the Trusted List for Wallet Providers.
If not successful, responsible person or group informs about the review result and may request additional data.

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

