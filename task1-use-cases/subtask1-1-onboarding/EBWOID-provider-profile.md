# Profile for a list of providers of European Business Wallet Owner Identification Data

## Introduction

The document specifies a LoTE profile aimed at supporting the issuance of EBWOID in the context of the WEBUILD consortia. It is designed to be a list of trusted issuers for EBWOID.

## Scope

The Trusted List of EBWOID Providers is intended to convey trust in a set of legal entities and their solutions, within [REGULATION (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng). The WEBUILD Consortia is tasked with designing, implementing, and testing the trusted digital business identity ecosystem envisioned by this regulation. This specification outlines the onboarding and the profile of a Trusted List for EBWOID providers within WEBUILD. Wherever feasible, the specification closely aligns to processes defined in the Regulation as well as the [Architecture and Reference Framework](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#622-wallet-provider-registration-and-notification), interpreting them for the testing purposes specific to WEBUILD.

## Terminology

1. **EBWOID**: European Business Wallet Owner Identification Data
2. **LoTE**: List of Trusted Entities

## Actors

**Primary Actor [MVP]:** Beneficiaries and Associated Partners providing an EBWOID for testing purposes to a test owner of a European Business Wallet prototype

**Secondary Actors [MVP]:**

- Ecosystem Authority: WEBUILD WP4 Trust Infrastructure group
- Trusted List Provider: WEBUILD WP4 Trust Infrastructure group

## General requirements

The EBWOID providers list shall be issued as a list of trusted entities compliant to the latest version of ETSI TS 119 602.

ETSI TS 119 602 v.1.1.1 (2025-11) does not include a dedicated EBWOID profile. The data model below describes the EBWOID profile that is in use by the WEBUILD consortium.

### Preconditions for onboarding

- The WEBUILD WP4 Trust Infrastructure group is assigned to act as Ecosystem Authority and Trusted List Provider for all WEBUILD participants.
- A Trusted List for EBWOID Providers is available for onboarding.
- WP4 Trust Infrastructure group has assigned responsibilities for the onboarding process.
- EBWOID Providers are able to provide the requested data.

Each Trusted List in WEBUILD must be managed. This matrix defines the responsibilities for the EBWOID Trusted List in WEBUILD.

| Task | WP4 – Trust Infrastructure Lead/Co-Lead | PID/EBWOID Working Group | IDunion SCE | [Another participant] |
|---|---|---|---|---|
| Set up the Trusted List | I, A | C, I | R | |
| Host the Trusted List | I, A | I | R | |
| Invite EBWOID Provider to onboard | I | R, A | C | |
| Review onboarding requests | I | A, C | R | |
| Decide upon listing and de-listing | I | A, R | I | |
| Support EBWOID providers during and after onboarding | I, A | C | R | |
| Conduct conformity tests | I, A | R | I | |

- **Responsible (R):** The person or group who do the work and execute the task or deliverable.
- **Accountable (A):** The person or group who owns the result, makes the final decision, and is ultimately answerable for success or failure.
- **Consulted (C):** Person or group who are asked for input or expertise and are involved through two-way communication before or during the task.
- **Informed (I):** People who are kept up to date on progress or outcomes via one-way communication but are not involved in doing or deciding.

## Scheme information

The `ListAndSchemeInformation` component of the EBWOID providers list shall comply with the requirements laid down in Table A.1.

**Table A.1: EBWOID providers list scheme information**

| LoTE component (ETSI TS 119 602 v.1.1.1 (2025-11)) | Additional requirement |
|---|---|
| **LoTE version identifier** (clause 6.3.1) | The value of the `LoTEVersionIdentifier` component shall be "1". |
| **LoTE sequence number** (clause 6.3.2) | The first instance of the EBWOID providers list shall be issued with the value of the `LoTESequenceNumber` component number set to "1". |
| **LoTE type** (clause 6.3.3) | The value of the `LoTEType` component shall be `"http://uri.etsi.org/19602/LoTEType/EUEBWOIDProvidersList"`. |
| **Scheme operator name** (clause 6.3.4) | No additional requirements. |
| **Scheme operator address** (clause 6.3.5) | No additional requirements. |
| **Scheme name** (clause 6.3.6) | No additional requirements. |
| **Scheme information URI** (clause 6.3.7) | The `SchemeInformationURI` component shall contain: a) a URI where users can receive information about the EBWOID providers list; and b) a URI where users can retrieve all previous instances of the EBWOID providers list. |
| **Status determination approach** (clause 6.3.8) | The value of `StatusDeterminationApproach` shall be `"http://uri.etsi.org/19602/EBWOIDProvidersList/StatusDetn/EU"`. |
| **Scheme type/community/rules** (clause 6.3.9) | The value of the `SchemeTypeCommunityRules` component shall be `"http://uri.etsi.org/19602/EBWOIDProviders/schemerules/EU"`. |
| **Scheme territory** (clause 6.3.10) | The value of the `SchemeTerritory` component shall be `"EU"`. |
| **LoTE policy/legal notice** (clause 6.3.11) | No additional requirements. |
| **Historical information period** (clause 6.3.12) | The `HistoricalInformationPeriod` component shall not be present, meaning — in compliance with clause 6.3.12 of ETSI TS 119 602 — that historical information is not kept in the list. |
| **Pointers to other LoTEs** (clause 6.3.13) | The `PointersToOtherLoTE` component shall contain a pointer to the present EBWOID providers list itself. |
| **List issue date and time** (clause 6.3.14) | No additional requirements. |
| **Next update** (clause 6.3.15) | No additional requirements. |
| **Distribution points** (clause 6.3.16) | No additional requirements. |
| **Scheme extensions** (clause 6.3.17) | No additional requirements. |

## List of trusted entities

Each `TrustedEntityInformation` component present in a `TrustedEntity` component listed in the `TrustedEntitiesList` component of the EBWOID providers list shall comply with the requirements laid down in Table A.2.

**Table A.2: EBWOID provider information (for each listed EBWOID provider)**

| LoTE component | Additional requirement |
|---|---|
| **TE name** (clause 6.5.1) | The value of the `TEName` component shall be the name of the provider of EBWOID. |
| **TE trade name** (clause 6.5.2) | The `TETradeName` component shall include an official registration identifier as registered in official records, where such a registered identifier exists, that unambiguously identifies the EBWOID provider. In case the EBWOID provider is a legal entity, the value of this component shall have the same semantics as the one required for the `organizationIdentifier` attribute in requirements LEG-5.1.4-02, LEG-5.1.4-03 and LEG-5.1.4-04 of ETSI EN 319 412-1. In case the EBWOID provider is a natural person, the value shall have the same semantics as the one required for the `serialNumber` attribute in requirements NAT-5.1.3-02, NAT-5.1.3-03 and NAT-5.1.3-04 of ETSI EN 319 412-1. |
| **TE address** (clause 6.5.3) | The `TEAddress` component shall contain: a) the postal address of the EBWOID provider; and b) the contact email and contact phone number of the provider of person identification data, for matters related to the person identification data it provides. |
| **TE information URI** (clause 6.5.4) | The `TEInformationURI` component shall contain: a) the URL of the webpage that contains the policies, terms and conditions of the provider of EBWOID that apply to the provision and use of the EBWOID it provides; b) where applicable, the URL of the webpage that contains additional information about the EBWOID provider; c) the URI `"http://uri.etsi.org/19602/ListOfTrustedEntities/EBWOIDProvider/CC"` where "CC" is replaced by the ISO 3166-1 Alpha-2 code of the Member State responsible for that EBWOID provider. |
| **TE information extensions** (clause 6.5.5) | Where applicable, the `OtherAssociatedBody` extension shall be used to provide, in an `AssociatedBody` element, the name of the body responsible for ensuring that the person identification data is associated with the wallet unit. |
| **Trusted Entity Services (list of services)** (clause 6.4.2) | See Table A.3. |

Each `ServiceInformation` component present in the `TrustedEntityServices` component of a `TrustedEntity` component listed in the `TrustedEntitiesList` component of the PID providers list shall comply with the requirements laid down in Table A.3.

**Table A.3: Service information (for each service of a listed EBWOID provider)**

| LoTE component | Additional requirement |
|---|---|
| **Service type identifier** (clause 6.6.1) | The following URIs may be used as values of the `ServiceTypeIdentifier` component, to the exclusion of any other: a) `"http://uri.etsi.org/19602/SvcType/EBWOID/Issuance"` to indicate that the service is one under which person identity data are issued; b) `"http://uri.etsi.org/19602/SvcType/EBWOID/Revocation"` to indicate that the service provides validity status information on person identity data. |
| **Service name** (clause 6.6.2) | No additional requirements. |
| **Service digital identity** (clause 6.6.3) | The `ServiceDigitalIdentity` component shall contain one or more X.509 certificates that can be used to verify the signature or seal created by the provider of EBWOID on the EBWOID it provides, and for which the certified identity data include the name, and where applicable, the registration number, of the EBWOID provider, as specified in the `TEName` and `TETradeName` components respectively. |
| **Service current status** (clause 6.6.4) | The `ServiceStatus` component shall not be used. As noted in clause 6.6.0 of ETSI TS 119 602, when the `HistoricalInformationPeriod` component is absent, or present with a zero value, and the `ServiceStatus` component is absent, this signifies that all listed trusted entity services have the same approval status in the list of trusted entities scheme. Under the present profile, the absence of the service status means that all listed providers of EBWOID are bodies notified by EU Member States as currently responsible for issuing and revoking the EBWOID and ensuring that the EBWOID of a user is cryptographically bound to a business wallet unit. When a listed body is not responsible for this issuance and revocation process, it shall be removed from the list. |
| **Current status starting date and time** (clause 6.6.5) | The `StatusStartingTime` component shall not be used. As noted in clause 6.6.0 of ETSI 119 602, when the `StatusStartingTime` component is absent, this signifies that verification of the approval status of a listed entity service can only be done at the current time. LoTEs without the `StatusStartingTime` component are not suitable for verification of approval statuses of entity services in the past. Under the present profile, an HTTP URI leading to historical previous versions of the EBWOID providers list is provided through the `SchemeInformationURI` component. |
| **Scheme service definition URI** (clause 6.6.6) | No additional requirements. |
| **Service supply points** (clause 6.6.7) | No additional requirements. |
| **TE service definition URI** (clause 6.6.8) | No additional requirements. |
| **Service information extensions** (clause 6.6.9) | No additional requirements. |
| **History information** (clause 6.4.4) | No additional requirements. |

## Signature

The EBWOID providers list shall be signed by means of a compact JAdES Baseline B signature as specified in ETSI TS 119 182-1.