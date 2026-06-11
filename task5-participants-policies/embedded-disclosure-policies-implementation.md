# Embedded Disclosure Policies: Implementation Guide

This document provides a guide on implementing **Embedded Disclosure Policies (EDP)**. It defines what an EDP is referring to the corresponding legal framework (Section 1), which policy types (Section 2) and data model are supported (Section 3), and the retrieval mechanism and evaluation flow (Section 4).

## 1. Overview and Legal Framework

### 1.1 Definition
Embedded Disclosure Policies (EDPs) are mechanisms that allow Attestation Providers to specify restrictions on which Relying Parties can access specific Attestations, providing a crucial layer of data protection for users.

These policies are defined by the Attestation Provider and embedded in the Attestation Providers metadata (OpenID4VCI Issuer metadata).
During issuance, the Wallet Unit retrieves and stores the EDP locally, associating it with the Attestation.
During presentation, EDP are evaluated by the Wallet Unit together with the presentation request before allowing Attestation presentation.

**Note**: EDPs could be used by Attestation Providers (QEEA, Pub-EAA and non-qualified EAA Providers), they are not applicable to PID Providers (see EDP_01).

### 1.2 Normative References and EDP Requirements 

- **ARF Topic 43**: Defines the high-level requirements for EDPs. The following ARF 2.9.0 requirements (EDP_01 through EDP_11) are specified:

  - **EDP_01**: A Wallet Unit SHALL enable an Attestation Provider to optionally express an embedded disclosure policy for a QEAA, PuB-EAA, or non-qualified EAA. *Note: The European Digital Identity Regulation does not contain a requirement for PIDs to be able to contain an embedded disclosure policy.*

  - **EDP_02**: A Wallet Unit SHALL support embedded disclosure policies implementing the 'Authorised relying parties only policy' described in Annex III of Implementing Regulation (EU) 2024/2979. If present, such an embedded disclosure policy SHALL contain a list of EU-wide unique identifiers of Relying Parties, as specified in Reg_32. The Wallet Unit SHALL retrieve the Relying Party identifier from the access certificate presented by the Relying Party, and compare it to the list of authorised identifiers in the policy, unless the Relying Party is an intermediary. If the Relying Party is an intermediary, the Wallet Unit SHALL retrieve the unique identifier of the intermediated Relying Party from the presentation request or from the registration certificate of the intermediated Relying Party and compare this identifier to the list of authorised identifiers in the policy. *Note: See RPI_07 for how the Wallet Unit can see if the Relying Party is an intermediary.*

  - **EDP_03**: A Wallet Unit SHALL support embedded disclosure policies implementing the 'Specific root of trust' policy described in Annex III of Implementing Regulation (EU) 2024/2979. If present, such an embedded disclosure policy SHALL contain a list of root or intermediate certificates used for signing Relying Party access certificates. The Wallet Unit SHALL compare the certificate chain that was used to sign the access certificate provided by the Relying Party to the list of authorised root or intermediate certificates in the policy, unless the Relying Party is an intermediary. If the Relying Party is an intermediary, the Wallet Unit SHALL retrieve the root certificate of the Provider of registration certificates of the intermediated Relying Party from the presentation request or from the Registrar's online service (as applicable) and compare this certificate to the list of authorised certificates in the policy. 

  - **EDP_04**: (Empty requirement)

  - **EDP_05**: An embedded disclosure policy SHOULD contain a link to a website of the Attestation Provider explaining the disclosure policy in layman's terms. If this is the case, the Wallet Unit SHALL display the link to the User and allow them to navigate to that website.

  - **EDP_06**: The Wallet Unit SHALL evaluate an embedded disclosure policy in conjunction with the information received from the requesting Relying Party, in order to determine if the Relying Party has permission from the Attestation Provider to access the requested attestation.

  - **EDP_07**: The Wallet Unit SHALL enable the User, based on the outcome of the evaluation of the applicable embedded disclosure policy(s), to deny or allow the presentation of the requested attestation to the Relying Party.

  - **EDP_08**: The Commission SHALL take measures to ensure a technical specification is created establishing common mechanisms for the specification of embedded disclosure policies by Attestation Providers, and for the evaluation of such policies by Wallet Units.

  - **EDP_09**: An Attestation Provider SHALL include an embedded disclosure policy (if any) by value in the Issuer metadata related to the attestation, in compliance with the OpenID4VCI issuance protocol or an extension thereof specified in the technical specification mentioned in EDP_08.

  - **EDP_10**: During attestation issuance, a Wallet Unit SHALL retrieve and store locally the corresponding embedded disclosure policy, if any. *Note: The intent of this requirement is that the Wallet Unit is able to evaluate an EDP during a presentation transaction, without needing to request it again from the Attestation Provider. This is necessary in particular during proximity presentations, which must be able to be done without an internet connection.*

  - **EDP_11**: An Attestation Provider SHALL revoke an attestation if a corresponding embedded disclosure policy is added, changed, or deleted.

- **Implementing Regulation (EU) 2024/2979, Annex III**: Describes the specific policy types:
  - **No policy** indicating that no policy applies to the electronic attestations of attributes.
  - **Authorised relying parties only policy**, indicating that wallet users may only disclose electronic attestations of attributes to authenticated relying parties which are explicitly listed in the disclosure policies.
  - **Specific root of trust** indicating that wallet users should only disclose the specific electronic attestation of attributes to authenticated wallet-relying parties with wallet-relying party access certificates derived from a specific root (or list of specific roots) or intermediate certificate(s).

- **ETSI TS 119 472-3 V1.1.1**: Technical specification defining the embedded disclosure policy extension for OpenID4VCI metadata (Section 4.2.5 "Provision of Embedded Disclosure Policy"). This is the technical specification mentioned in ARF requirement EDP_08, which establishes the following requirements for the data model of Embedded Disclosure Policy (ISS-MDATA-EBD-4.2.5.2-01 through ISS-MDATA-EBD-4.2.5.2-13):
  - **ISS-MDATA-EBD-4.2.5.2-01**: The Embedded Disclosure Policy SHALL be identified by a unique URI.
  - **ISS-MDATA-EBD-4.2.5.2-02**: The Embedded Disclosure Policy may be accessible via this URI.
  - **ISS-MDATA-EBD-4.2.5.2-03**: The Embedded Disclosure Policy associated with EAA SHALL be identified by including its unique URI. The EAA provider SHALL either include the Embedded Disclosure Policy identifier with the data set for the Embedded Disclosure Policy or just provide the identifier if the policy data set has already been pre-loaded into the Wallet Unit.
  - **ISS-MDATA-EBD-4.2.5.2-04**: The Embedded Disclosure Policy may include a description of the applicability of an embedded disclosure to a particular community and/or class of application with common security requirements.
  - **ISS-MDATA-EBD-4.2.5.2-05**: The Embedded Disclosure Policy may include an identifier of the authority responsible for the policy.
  - **ISS-MDATA-EBD-4.2.5.2-06**: The Embedded Disclosure Policy may indicate that no policy restrictions apply for the associated EAA.
  - **ISS-MDATA-EBD-4.2.5.2-07**: The Embedded Disclosure Policy may contain a list of authorised relying parties for the associated EAA:
    - a) as identified by their subject distinguished name as held in the wallet-relying party access certificate in the form of LDAP string as specified in IETF RFC 4514; and/or 
    - b) as indicated by the URI encoded entitlements required of relying parties as specified in ETSI TS 119 475, and held in the wallet relying party registration certificate. 
  - **ISS-MDATA-EBD-4.2.5.2-08**: The Embedded Disclosure Policy may define a specific list of roots of trust, to indicate that EUDI Wallet users should only disclose specific EAAs to Relying Parties in possession of access certificates derived from one of these roots or intermediate certificates.
  - **ISS-MDATA-EBD-4.2.5.2-09**: Each element of the list of roots of trust, as specified in ISS-MDATA-EBD-4.2.5.2-08 above, SHALL include the issuer's distinguished name in the form of LDAP string as specified in IETF RFC 4514 and the issuer's certificate serial number.
  - **ISS-MDATA-EBD-4.2.5.2-10**: Other information may be included in an Embedded Disclosure Policy Extension which may be ignored by the wallet.
  - **ISS-MDATA-EBD-4.2.5.2-11**: Wallet Units should still be able to cope with extensions being present even if they are ignored.
  - **ISS-MDATA-EBD-4.2.5.2-12**: An Embedded Disclosure Policy Extension may be defined which contains alternative policy rules (no policy as in ISS-MDATA-EBD-4.2.5.2-05, authorised relying party only as in ISS-MDATAEBD-4.2.5.2-06 or specific roots of trust as in ISS-MDATA-EBD-4.2.5.2-07) to be applied to specified attributes within the EAA which are allowed to be disclosed using selective disclosure.
  - **ISS-MDATA-EBD-4.2.5.2-13**: The Embedded Disclosure Policy should contain a link to a website of the Attestation Provider explaining the disclosure policy in layman's terms for display by the Wallet Unit to the User and to allow the User to navigate to the website. 

- **OpenID4VCI**: Credential issuance protocol

### 1.3 Data Protection Mechanisms
The use of EDPs help enforcing compliance with data protection regulations:
- **GDPR Compliance**: Policies help enforce data minimization and purpose limitation
- **Consent Management**: Policies work alongside user consent mechanisms
- **Audit Trail**: Policy evaluations can be logged for compliance

In particular, EDPs bring the following benefits:
1. **Access Control at Source**:
   - Attestation Providers define who can access their Attestations
   - Policies are embedded at issuance time, ensuring consistent enforcement
   - If policy changes, Attestation must be revoked, ensuring users are not bound by outdated policies 

2. **Automatic Enforcement and Transparency**:
   - Wallet Units automatically evaluate policies before presentation
   - Users are informed of policy restrictions (policy explanation URLs provide clear information about restrictions, thus users understand why certain RPs may be restricted)
   - Prevents unauthorized disclosure attempts

3. **Granular Control and User Control**:
   - Different policies for different Attestations
   - Even if policy allows, user can deny, thus maintaining final control

4. **Trust-Based Restrictions**:
   - Root of trust policies ensure only trusted certificate authorities' RPs can access data
   - Authorized RPs policies ensure only pre-approved entities can access data

## 2. Policy Types

Implementing Regulation (EU) 2024/2979, Annex III defines 3 policy types: 

1. **No policy**. No EDP is present, or the EDP explicitly indicates that no restrictions apply.

2. **Authorised relying parties only policy**. This policy restricts disclosure to a specific list of authorized Relying Parties. The EDP contains a list of Relying Parties that are allowed to access the Attestation. According to ARF Topic 43 (EDP_02) and ETSI TS 119 472-3 V1.1.1 (ISS-MDATA-EBD-4.2.5.2-07), the policy SHALL contain a list of EU-wide unique identifiers of Relying Parties (as specified in Reg_32). As
   - **subject distinguished name** (LDAP string) as specified in IETF RFC 4514 (for legal persons: ``commonName``, ``organizationName``, ``organizationIdentifier`` (ORGID), ``countryName``; for natural persons: ``commonName``, ``givenName``, ``surname``, ``serialNumber`` (SN), ``countryName``), and/or 
   - **URI encoded entitlements** as specified in ETSI TS 119 475  

3. **Specific root of trust policy**. This policy restricts disclosure to Relying Parties whose Access Certificates are signed by specific root or intermediate certificate authorities. According to ARF Topic 43 (EDP_03) and ETSI TS 119 472-3 V1.1.1 (ISS-MDATA-EBD-4.2.5.2-08, ISS-MDATA-EBD-4.2.5.2-09), the policy SHALL contain a list of root or intermediate certificates used for signing Relying Party Access Certificates. Each element of the list of roots of trust SHALL include:
    - The issuer's distinguished name in the form of LDAP string as specified in IETF RFC 4514
    - The issuer's certificate serial number

## 3. Policy Data Model
The data model of the EDP is defined in ETSI TS 119 472-3 V1.1.1 (ISS-MDATA-EBD-4.2.5.2-01 through ISS-MDATA-EBD-4.2.5.2-13) covering: 
  - Policy identification by unique URI
  - Authorised relying parties identification (subject DN in LDAP format per RFC 4514, or entitlement URI per ETSI TS 119 475)
  - Roots of trust specification (issuer DN + certificate serial number)
  - Description of the applicability of the policy
  - Extensions for selective disclosure

The following JSON structure is derived from the above requirements: 

| Parameter | Type | Description | Based on |
|-----------|------|-------------|----------|
| `policy_uri` | string (URI) | REQUIRED. Unique identifier of the EDP. | ISS-MDATA-EBD-4.2.5.2-01 |
| `policy_type` | string | REQUIRED. Policy type. Values: `"no_policy"`, `authorized_rp_only`, `specific_root_of_trust`. | ISS-MDATA-EBD-4.2.5.2-06/07/08 |
| `description` | string | OPTIONAL. Description of the applicability of the policy to a particular community or class of application. | ISS-MDATA-EBD-4.2.5.2-04 |
| `policy_authority` | string | OPTIONAL. Identifier of the authority responsible for the policy. | ISS-MDATA-EBD-4.2.5.2-05 |
| `policy_info_url` | string (URL) | OPTIONAL. Link to a website explaining the policy in layman's terms. | ISS-MDATA-EBD-4.2.5.2-13, EDP_05 |
| `authorized_parties` | array of objects | REQUIRED if `policy_type` is `authorized_rp_only`. List of authorized RPs. | ISS-MDATA-EBD-4.2.5.2-07 |
| `authorized_parties[].subject_dn` | string | OPTIONAL. Subject DN of the RP from the WRPAC, in LDAP string form as defined in RFC 4514. At least one of `subject_dn` or `entitlement_uri` SHALL be present in each element. | ISS-MDATA-EBD-4.2.5.2-07 |
| `authorized_parties[].entitlement_uri` | string (URI) | OPTIONAL. URI-encoded entitlement or sub-entitlement as specified in ETSI TS 119 475 Annex A, held in the WRPRC. At least one of `subject_dn` or `entitlement_uri` SHALL be present in each element. | ISS-MDATA-EBD-4.2.5.2-07 |
| `trusted_roots` | array of objects | REQUIRED if `policy_type` is `specific_root_of_trust`. List of trusted roots. | ISS-MDATA-EBD-4.2.5.2-08 |
| `trusted_roots[].issuer_dn` | string | REQUIRED. Issuer DN in LDAP string form compliant with RFC 4514. | ISS-MDATA-EBD-4.2.5.2-09 |
| `trusted_roots[].serial_number` | string | REQUIRED. Certificate serial number of the issuer. | ISS-MDATA-EBD-4.2.5.2-09 |

> ⚠️ **Warning**: The structure defined here is an implementation profile based on the ETSI data model requirements, and parameter names MAY change when the ETSI schema is published. 

Below are two non-normative examples:

```json
{
"policy_uri": "https://attestation-provider.example.com/policies/authorised-rps-policy", 
"policy_type": "authorised_rp_only",
"description": "Policy restricting access to authorized banking services", 
"policy_authority": "https://authority.example.com", 
"policy_info_url": "https://attestation-provider.example.com/policy-explanation",
"authorized_parties": [ 
    {
    "subject_dn": "CN=Example RP, O=Example Org, ORGID=EU.RP.123456789, C=IT"
    },
    {
    "entitlement_uri": "https://example.com/entitlements/banking-service" 
    }
]
}
```

```json
{
"policy_uri": "https://attestation-provider.example.com/policies/root-of-trust-policy", 
"policy_type": "specific_root_of_trust",
"description": "Policy restricting access to RPs with certificates from trusted CAs",
"policy_authority": "https://authority.example.com", 
"policy_info_url": "https://attestation-provider.example.com/policy-explanation",
"trusted_roots": [
    {
    "issuer_dn": "CN=Trusted CA Root, O=Trusted CA Organization, C=EU",
    "certificate_serial_number": "1234567890123456789012345678901234"
    },
    {
    "issuer_dn": "CN=Intermediate CA, O=Trusted CA Organization, C=EU",
    "serial_number": "9876543210987654321098765432109876"
    }
]
}
```

**Note**: This policy structure is embedded in the Issuer metadata (OpenID4VCI), not within the digital credential itself.



## 4. Implementation Architecture

### 4.1 Policy Retrieval and Storage

**Attestation Provider** includes the EDP **by value** in the OpenID4VCI Issuer metadata (EDP_09) within the `credential_configurations_supported` object, as an extension to the standard OpenID4VCI 1.0 specification (Section 12.2.4).

> ⚠️ **Warning**: The field name `embedded_disclosure_policy` used in the example below is illustrative and may differ from the official field name defined in the final version of ETSI TS 119 472-3. Please refer to the official ETSI TS 119 472-3 specification for the exact field name and structure.

```json
{ 
  "credential_issuer": "https://credential-issuer.example.com",
  "credential_endpoint": "https://credential-issuer.example.com/credential",
  "credential_configurations_supported": {
    "credential_type_1": {
      "format": "dc+sd-jwt",
      "embedded_disclosure_policy": {
        "policy_type": "authorised_relying_parties_only",
        "authorized_parties": [...],
        "policy_info_url": "https://...",
        ...
      },
      ...
    }
  }
  ...
}
```

During the Attestation issuance (EDP_10), a Wallet Unit retrieves (if available) and stores locally the corresponding EDP associated with the specific Attestation for which it was retrieved. The EDP SHALL be maintained for the lifetime of the Attestation.

If an Attestation Provider adds, changes, or deletes an EDP for an Attestation, the Attestation Provider SHALL revoke that Attestation (EDP_11). The Wallet Unit detects the policy change indirectly through the normal Attestation status checking mechanism (Status List), which will report that the Attestation as revoked. The locally stored EDP is then implicitly invalidated together with the Attestation. The User needs to request a new issuance to obtain the Attestation with the updated policy.


### 4.2 Policy Evaluation Flow

```
┌─────────────────┐
│  Relying Party  │
│  Presentation   │
│  Request        │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│   Wallet Unit           │
│                         │
│ 1. Retrieve Attestation │
│ 2. Check for EDP        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Policy Evaluation      │
│  (EDP_06)               │      
│                         │
│ - Extract RP Info       │
│ - Check Policy Type     │
│ - Evaluate Conditions   │
└────────┬────────────────┘
         │
         ▼
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌────────┐
│ ALLOW  │ │ DENY   │
└───┬────┘ └───┬────┘
    │          │
    ▼          ▼
┌─────────────────────┐
│  User Decision      │
│  (EDP_07)           │
└─────────────────────┘
```

During the Policy Evaluation (EDP_06), the Wallet Unit SHALL:

1. **Retrieve Policy**: Load the EDP associated with the requested Attestation and determine policy type
2. **Extract Relying Party Information**: 
    - if **Authorised relying parties only** policy type: 
        - For direct Relying Parties: Retrieve the unique identifiers of Relying Parties as held in the Wallet-Relying Party Access Certificate  
        - For intermediaries: Retrieve the unique identifiers of the intermediated Relying Party from:
            - The presentation request, OR
            - The Registration Certificate of the intermediated Relying Party
    - if **Specific root of trust policy** policy type: 
        - For direct Relying Parties: Retrieve the issuer DN and serial number from the root or intermediate certificates in the Wallet-Relying Party Access Certificate chain.
        - For intermediaries: Retrieve the root certificate information of the Provider of Wallet-Relying Registration Certificates of the intermediated Relying Party from:
            - The presentation request, OR
            - The Registrar's online service (as applicable)
3. **Evaluate Conditions**:
   - Apply appropriate evaluation logic
        - if **Authorised relying parties only policy** policy type: match the retrieved identifier against the list of authorized identifiers in the policy, i.e. compare the Relying Party subject DN from the Wallet-Relying Party Access Certificate against `subject_dn` entries, and/or compare the RP entitlements or sub-entitlements from Wallet-Relying Party Registration Certificate against `entitlement_uri` entries. A match on either criterion is sufficient.
        - if **Specific root of trust policy** policy type: verify that the certificate chain matches one of the authorized root or intermediate certificates, i.e. compare against the `trusted_roots` list and match `issuer_dn` using LDAP DN comparison and `serial_number` using integer comparison. 
   - Check if RP meets policy conditions
4. **Decision**: Determine if Relying Party has permission from Attestation Provider

After policy evaluation, the Wallet Unit SHALL (EDP_07):

1. **Present Result**: Show the user the outcome of policy evaluation
2. **Display Policy Information**:
   - Policy explanation URL (if available, EDP_05)
   - Policy type and restrictions
   - RP information
3. **User Decision**: Enable user to:
   - **Allow** presentation (even if policy denies, user has final say)  
   - **Deny** presentation (even if policy permits, user has final say)

