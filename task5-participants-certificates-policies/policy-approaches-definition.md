# Policy Approaches Definition: Additive vs Subtractive

## Executive Summary

This document defines two distinct policy approaches for the WP4 Trust Infrastructure framework: **Additive** and **Subtractive** policy models. These approaches provide different security paradigms suitable for various deployment scenarios, from high-security zero-trust environments to flexible permissive ecosystems.

## Table of Contents

1. [Introduction](#introduction)
2. [Policy Approach Definitions](#policy-approach-definitions)
3. [Application to Trust Framework](#application-to-trust-framework)
4. [OpenID Federation Trust Mark Integration](#openid-federation-trust-mark-integration)
5. [Attribute and Credential Classification](#attribute-and-credential-classification)
6. [Implementation Guidelines](#implementation-guidelines)
7. [Security Considerations](#security-considerations)
8. [Examples and Use Cases](#examples-and-use-cases)

## Introduction

### Background

In digital trust ecosystems, policy management is crucial for controlling access, defining permissions, and ensuring security. The choice between additive and subtractive policy approaches fundamentally affects the security posture and operational flexibility of the system.

### Zero Trust Principle

A zero-trust approach requires an **additive policy model** where nothing is granted by default, and only explicitly authorized actions are permitted. This mirrors firewall security models with "reject" or "drop" rules that only allow explicitly configured permissions.

### Policy Philosophy Comparison

| Aspect | Additive Approach | Subtractive Approach |
|--------|------------------|---------------------|
| **Security Model** | Zero-trust | Permissive |
| **Default State** | Deny all | Allow all |
| **Authorization** | Explicit allow-list | Explicit deny-list |
| **Risk Level** | Lower (conservative) | Higher (permissive) |
| **Configuration** | Grant specific permissions | Block specific restrictions |
| **Maintenance** | More granular control | Easier to manage |
| **Use Cases** | High-security, sensitive data | Open ecosystems, development |

## Policy Approach Definitions

### Additive Policy Approach

#### Definition
The **Additive Policy Approach** implements an explicit allow-list model where permissions are granted only when explicitly authorized. This follows the principle: **"Nothing is permitted unless explicitly allowed."**

#### Characteristics
- **Default Action**: Deny all requests
- **Authorization Model**: Explicit allow-list
- **Security Posture**: Conservative, high-security
- **Configuration**: Grant specific permissions
- **Risk Management**: Proactive restriction

#### Implementation Pattern
```json
{
  "policy_type": "additive",
  "default_action": "deny",
  "authorized_actions": [
    {
      "action": "issue_credential",
      "credential_type": "VerifiableCredential",
      "conditions": {
        "issuer_authorized": true,
        "credential_schema_valid": true
      }
    }
  ]
}
```

#### Use Cases
- High-security environments
- Zero-trust architectures
- Sensitive data handling
- Regulatory compliance requirements
- Financial services
- Healthcare systems

### Subtractive Policy Approach

#### Definition
The **Subtractive Policy Approach** implements an explicit deny-list model where permissions are granted by default except for explicitly restricted items. This follows the principle: **"Everything is permitted unless explicitly denied."**

#### Characteristics
- **Default Action**: Allow all requests
- **Authorization Model**: Explicit deny-list
- **Security Posture**: Permissive, flexible
- **Configuration**: Block specific restrictions
- **Risk Management**: Reactive restriction

#### Implementation Pattern
```json
{
  "policy_type": "subtractive",
  "default_action": "allow",
  "restricted_actions": [
    {
      "action": "issue_credential",
      "credential_type": "BiometricCredential",
      "restriction_reason": "Privacy concerns",
      "conditions": {
        "explicit_consent_required": true
      }
    }
  ]
}
```

#### Use Cases
- Open ecosystems
- Development environments
- Rapid prototyping
- Innovation platforms
- Collaborative environments
- Research and testing

## Application to Trust Framework

### For Credential Issuers

#### Additive Approach for Credential Issuers
```json
{
  "participant_type": "credential_issuer",
  "policy_approach": "additive",
  "authorized_credential_types": [
    "VerifiableCredential",
    "EUDIWalletCredential",
    "OpenIDConnectCredential"
  ],
  "authorized_attribute_groups": [
    "identity_attributes",
    "authentication_attributes",
    "affiliation_attributes"
  ],
  "scope_restrictions": {
    "geographic_scope": ["EU"],
    "temporal_scope": "2024-01-01T00:00:00Z/2025-12-31T23:59:59Z",
    "purpose_scope": ["authentication", "identification"]
  },
  "compliance_requirements": [
    "ETSI_EN_319_412_6",
    "GDPR_compliance",
    "audit_trail_required"
  ]
}
```

#### Subtractive Approach for Credential Issuers
```json
{
  "participant_type": "credential_issuer",
  "policy_approach": "subtractive",
  "restricted_credential_types": [
    "BiometricCredential",
    "FinancialCredential",
    "HealthCredential"
  ],
  "restricted_attribute_groups": [
    "sensitive_personal_data",
    "special_category_data"
  ],
  "compliance_requirements": [
    "explicit_consent_required",
    "data_protection_impact_assessment",
    "regulatory_approval_required"
  ]
}
```

### For Relying Parties

#### Additive Approach for Relying Parties
```json
{
  "participant_type": "relying_party",
  "policy_approach": "additive",
  "authorized_attribute_requests": [
    {
      "attribute_type": "given_name",
      "purpose": "authentication",
      "retention_period": "session_only"
    },
    {
      "attribute_type": "email",
      "purpose": "communication",
      "retention_period": "30_days"
    }
  ],
  "authorized_purposes": [
    "authentication",
    "authorization",
    "service_delivery"
  ],
  "consent_requirements": [
    "explicit_consent",
    "granular_consent",
    "withdrawal_mechanism"
  ]
}
```

#### Subtractive Approach for Relying Parties
```json
{
  "participant_type": "relying_party",
  "policy_approach": "subtractive",
  "restricted_attribute_requests": [
    {
      "attribute_type": "biometric_data",
      "restriction_reason": "Privacy protection",
      "exceptions": ["law_enforcement", "national_security"]
    },
    {
      "attribute_type": "financial_data",
      "restriction_reason": "Data protection",
      "exceptions": ["financial_services", "payment_processing"]
    }
  ],
  "restricted_purposes": [
    "marketing",
    "profiling",
    "automated_decision_making"
  ],
  "compliance_requirements": [
    "GDPR_consent",
    "data_minimization",
    "purpose_limitation"
  ]
}
```

## OpenID Federation Trust Mark Integration

### Trust Mark Schema for Additive Policies

#### Credential Issuer Trust Mark
```json
{
  "trust_mark_id": "additive_credential_issuer_policy_v1.0",
  "issuer": "https://trust-registry.example.com",
  "subject": "https://credential-issuer.example.com",
  "trust_mark_type": "credential_issuer_policy",
  "policy_approach": "additive",
  "issued_at": "2024-01-01T00:00:00Z",
  "expires_at": "2024-12-31T23:59:59Z",
  "authorized_credential_types": [
    "VerifiableCredential",
    "VerifiablePresentation",
    "EUDIWalletCredential"
  ],
  "authorized_attribute_groups": [
    "identity_attributes",
    "authentication_attributes",
    "affiliation_attributes"
  ],
  "scope_restrictions": {
    "geographic_scope": ["EU"],
    "temporal_scope": "2024-01-01T00:00:00Z/2025-12-31T23:59:59Z",
    "purpose_scope": ["authentication", "identification"]
  },
  "compliance_standards": [
    "ETSI_EN_319_412_6",
    "W3C_Verifiable_Credentials",
    "GDPR"
  ],
  "cryptographic_proof": {
    "type": "JsonWebSignature2020",
    "created": "2024-01-01T00:00:00Z",
    "verificationMethod": "https://trust-registry.example.com#key-1",
    "proofValue": "..."
  }
}
```

#### Relying Party Trust Mark
```json
{
  "trust_mark_id": "additive_relying_party_policy_v1.0",
  "issuer": "https://trust-registry.example.com",
  "subject": "https://relying-party.example.com",
  "trust_mark_type": "relying_party_policy",
  "policy_approach": "additive",
  "issued_at": "2024-01-01T00:00:00Z",
  "expires_at": "2024-12-31T23:59:59Z",
  "authorized_attribute_requests": [
    {
      "attribute_type": "given_name",
      "purpose": "authentication",
      "retention_period": "session_only",
      "consent_required": true
    },
    {
      "attribute_type": "email",
      "purpose": "communication",
      "retention_period": "30_days",
      "consent_required": true
    }
  ],
  "authorized_purposes": [
    "authentication",
    "authorization",
    "service_delivery"
  ],
  "consent_requirements": [
    "explicit_consent",
    "granular_consent",
    "withdrawal_mechanism"
  ],
  "cryptographic_proof": {
    "type": "JsonWebSignature2020",
    "created": "2024-01-01T00:00:00Z",
    "verificationMethod": "https://trust-registry.example.com#key-1",
    "proofValue": "..."
  }
}
```

### Trust Mark Schema for Subtractive Policies

#### Credential Issuer Trust Mark
```json
{
  "trust_mark_id": "subtractive_credential_issuer_policy_v1.0",
  "issuer": "https://trust-registry.example.com",
  "subject": "https://credential-issuer.example.com",
  "trust_mark_type": "credential_issuer_policy",
  "policy_approach": "subtractive",
  "issued_at": "2024-01-01T00:00:00Z",
  "expires_at": "2024-12-31T23:59:59Z",
  "restricted_credential_types": [
    "BiometricCredential",
    "FinancialCredential",
    "HealthCredential"
  ],
  "restricted_attribute_groups": [
    "sensitive_personal_data",
    "special_category_data"
  ],
  "compliance_requirements": [
    "explicit_consent_required",
    "data_protection_impact_assessment",
    "regulatory_approval_required"
  ],
  "cryptographic_proof": {
    "type": "JsonWebSignature2020",
    "created": "2024-01-01T00:00:00Z",
    "verificationMethod": "https://trust-registry.example.com#key-1",
    "proofValue": "..."
  }
}
```

#### Relying Party Trust Mark
```json
{
  "trust_mark_id": "subtractive_relying_party_policy_v1.0",
  "issuer": "https://trust-registry.example.com",
  "subject": "https://relying-party.example.com",
  "trust_mark_type": "relying_party_policy",
  "policy_approach": "subtractive",
  "issued_at": "2024-01-01T00:00:00Z",
  "expires_at": "2024-12-31T23:59:59Z",
  "restricted_attribute_requests": [
    {
      "attribute_type": "biometric_data",
      "restriction_reason": "Privacy protection",
      "exceptions": ["law_enforcement", "national_security"]
    },
    {
      "attribute_type": "financial_data",
      "restriction_reason": "Data protection",
      "exceptions": ["financial_services", "payment_processing"]
    }
  ],
  "restricted_purposes": [
    "marketing",
    "profiling",
    "automated_decision_making"
  ],
  "compliance_requirements": [
    "GDPR_consent",
    "data_minimization",
    "purpose_limitation"
  ],
  "cryptographic_proof": {
    "type": "JsonWebSignature2020",
    "created": "2024-01-01T00:00:00Z",
    "verificationMethod": "https://trust-registry.example.com#key-1",
    "proofValue": "..."
  }
}
```

## Attribute and Credential Classification

### By Scope/Purpose

#### Authentication Attributes
- **Purpose**: User authentication and identity verification
- **Sensitivity Level**: Medium
- **Retention Period**: Short-term (session-based)
- **Examples**:
  - `sub` (subject identifier)
  - `auth_time` (authentication time)
  - `acr` (authentication context class reference)
  - `amr` (authentication methods references)
  - `nonce` (nonce value)
  - `max_age` (maximum authentication age)

#### Identification Attributes
- **Purpose**: User identification and personal data
- **Sensitivity Level**: High
- **Retention Period**: Long-term (with consent)
- **Examples**:
  - `given_name` (first name)
  - `family_name` (last name)
  - `middle_name` (middle name)
  - `nickname` (nickname)
  - `preferred_username` (preferred username)
  - `email` (email address)
  - `phone_number` (phone number)
  - `birthdate` (birth date)
  - `gender` (gender)
  - `nationality` (nationality)

#### Affiliation Attributes
- **Purpose**: Organizational or institutional affiliation
- **Sensitivity Level**: Medium
- **Retention Period**: Medium-term (employment-based)
- **Examples**:
  - `organization` (organization name)
  - `department` (department)
  - `role` (job role)
  - `membership` (membership status)
  - `employee_id` (employee identifier)
  - `manager` (manager information)
  - `office_location` (office location)
  - `work_email` (work email)

#### Delivery Service Attributes
- **Purpose**: Service delivery and operational requirements
- **Sensitivity Level**: Low-Medium
- **Retention Period**: Service-dependent
- **Examples**:
  - `address` (postal address)
  - `preferences` (User preferences)
  - `service_level` (service level agreement)
  - `delivery_method` (delivery method)
  - `language` (preferred language)
  - `timezone` (timezone)
  - `accessibility_needs` (accessibility requirements)

### By Credential Type

#### Verifiable Credentials (W3C Standard)
- **Standard**: W3C Verifiable Credentials Data Model
- **Use Cases**: Identity verification, qualifications, certifications
- **Policy Requirements**:
  - Strong cryptographic proof
  - Revocation checking
  - Schema validation
  - Issuer verification
- **Examples**:
  - Educational credentials
  - Professional certifications
  - Identity documents
  - Membership cards

#### EUDI Wallet Credentials
- **Standard**: EU Digital Identity Wallet
- **Use Cases**: European digital identity, cross-border services
- **Policy Requirements**:
  - ETSI compliance
  - Qualified signatures
  - Cross-border recognition
  - Privacy preservation
- **Examples**:
  - National ID cards
  - Driver's licenses
  - Professional qualifications
  - Health insurance cards

#### OpenID Connect Credentials
- **Standard**: OpenID Connect for Identity Assurance
- **Use Cases**: Authentication, authorization, User info
- **Policy Requirements**:
  - OIDC compliance
  - Scope restrictions
  - Token validation
  - Session management
- **Examples**:
  - Authentication tokens
  - Authorization codes
  - User info claims
  - ID tokens

#### Biometric Credentials
- **Standard**: ISO/IEC 19794 (Biometric data)
- **Use Cases**: High-security authentication, identity verification
- **Policy Requirements**:
  - Explicit consent
  - Data minimization
  - Secure storage
  - Biometric template protection
- **Examples**:
  - Fingerprint templates
  - Facial recognition data
  - Iris scans
  - Voice patterns

#### Financial Credentials
- **Standard**: Various (PCI DSS, ISO 20022)
- **Use Cases**: Financial services, payment processing
- **Policy Requirements**:
  - PCI DSS compliance
  - Strong encryption
  - Audit trails
  - Fraud prevention
- **Examples**:
  - Bank account information
  - Credit card data
  - Payment methods
  - Financial history

#### Health Credentials
- **Standard**: HL7 FHIR, ISO 13606
- **Use Cases**: Healthcare services, medical records
- **Policy Requirements**:
  - HIPAA compliance
  - Medical privacy
  - Consent management
  - Data portability
- **Examples**:
  - Medical records
  - Prescription information
  - Vaccination records
  - Health insurance

## Implementation Guidelines

### Data Models

#### Additive Policy Model
```json
{
  "policy_id": "string",
  "policy_type": "additive",
  "participant_type": "credential_issuer|relying_party",
  "version": "1.0",
  "status": "active|inactive|draft",
  "authorized_actions": [
    {
      "action_id": "string",
      "action_type": "issue_credential|request_attribute",
      "resource_type": "credential_type|attribute_type",
      "resource_identifier": "string",
      "conditions": {
        "issuer_authorized": "boolean",
        "credential_schema_valid": "boolean",
        "compliance_verified": "boolean"
      },
      "scope_restrictions": {
        "geographic_scope": ["string"],
        "temporal_scope": "string",
        "purpose_scope": ["string"]
      }
    }
  ],
  "default_action": "deny",
  "compliance_requirements": ["string"],
  "created_at": "datetime",
  "updated_at": "datetime",
  "created_by": "string",
  "updated_by": "string"
}
```

#### Subtractive Policy Model
```json
{
  "policy_id": "string",
  "policy_type": "subtractive",
  "participant_type": "credential_issuer|relying_party",
  "version": "1.0",
  "status": "active|inactive|draft",
  "restricted_actions": [
    {
      "action_id": "string",
      "action_type": "issue_credential|request_attribute",
      "resource_type": "credential_type|attribute_type",
      "resource_identifier": "string",
      "restriction_reason": "string",
      "conditions": {
        "explicit_consent_required": "boolean",
        "regulatory_approval_required": "boolean",
        "data_protection_impact_assessment": "boolean"
      },
      "exceptions": ["string"]
    }
  ],
  "default_action": "allow",
  "compliance_requirements": ["string"],
  "created_at": "datetime",
  "updated_at": "datetime",
  "created_by": "string",
  "updated_by": "string"
}
```
## Security Considerations

### Additive Policy Security
- **Principle of Least Privilege**: Only grant necessary permissions
- **Explicit Authorization**: All permissions must be explicitly granted
- **Regular Review**: Periodic review of authorized actions
- **Audit Trail**: Complete logging of all policy decisions
- **Change Management**: Strict control over policy changes

### Subtractive Policy Security
- **Risk Assessment**: Regular assessment of allowed actions
- **Exception Monitoring**: Monitor for policy exceptions
- **Compliance Checking**: Regular compliance verification
- **Incident Response**: Rapid response to policy violations
- **Continuous Monitoring**: Real-time monitoring of policy compliance

### General Security Measures
- **Cryptographic Signatures**: All policies and trust marks must be cryptographically signed
- **Access Control**: Strict access control for policy management
- **Version Control**: Complete version history of all policies
- **Backup and Recovery**: Regular backup of policy data
- **Disaster Recovery**: Comprehensive disaster recovery procedures

## Examples and Use Cases

### Example 1: High-Security Government Portal (Additive)

**Scenario**: A government portal for accessing sensitive citizen services requires strict access control.

**Policy Configuration**:
```json
{
  "policy_type": "additive",
  "participant_type": "relying_party",
  "authorized_attribute_requests": [
    {
      "attribute_type": "given_name",
      "purpose": "authentication",
      "retention_period": "session_only",
      "consent_required": true
    },
    {
      "attribute_type": "family_name",
      "purpose": "authentication",
      "retention_period": "session_only",
      "consent_required": true
    },
    {
      "attribute_type": "national_id",
      "purpose": "identification",
      "retention_period": "30_days",
      "consent_required": true,
      "additional_verification": "qualified_signature"
    }
  ],
  "authorized_purposes": ["authentication", "identification"],
  "compliance_requirements": ["GDPR", "EIDAS", "ISO_27001"]
}
```

### Example 2: Open Innovation Platform (Subtractive)

**Scenario**: An open innovation platform that allows flexible access but restricts sensitive data.

**Policy Configuration**:
```json
{
  "policy_type": "subtractive",
  "participant_type": "relying_party",
  "restricted_attribute_requests": [
    {
      "attribute_type": "biometric_data",
      "restriction_reason": "Privacy protection",
      "exceptions": ["explicit_consent", "law_enforcement"]
    },
    {
      "attribute_type": "financial_data",
      "restriction_reason": "Data protection",
      "exceptions": ["financial_services", "payment_processing"]
    },
    {
      "attribute_type": "health_data",
      "restriction_reason": "Medical privacy",
      "exceptions": ["healthcare_services", "emergency_services"]
    }
  ],
  "restricted_purposes": ["marketing", "profiling", "automated_decision_making"],
  "compliance_requirements": ["GDPR", "data_minimization", "purpose_limitation"]
}
```

### Example 3: Financial Services Credential Issuer (Additive)

**Scenario**: A bank issuing financial credentials with strict regulatory compliance.

**Policy Configuration**:
```json
{
  "policy_type": "additive",
  "participant_type": "credential_issuer",
  "authorized_credential_types": [
    "BankAccountCredential",
    "CreditScoreCredential",
    "PaymentMethodCredential"
  ],
  "authorized_attribute_groups": [
    "financial_identity_attributes",
    "account_attributes",
    "transaction_attributes"
  ],
  "scope_restrictions": {
    "geographic_scope": ["EU"],
    "temporal_scope": "2024-01-01T00:00:00Z/2025-12-31T23:59:59Z",
    "purpose_scope": ["financial_services", "payment_processing"]
  },
  "compliance_requirements": ["PCI_DSS", "GDPR", "PSD2", "ISO_27001"]
}
```

### Example 4: Healthcare Credential Issuer (Subtractive)

**Scenario**: A healthcare provider issuing medical credentials with privacy-focused restrictions.

**Policy Configuration**:
```json
{
  "policy_type": "subtractive",
  "participant_type": "credential_issuer",
  "restricted_credential_types": [
    "BiometricCredential",
    "GeneticDataCredential",
    "MentalHealthCredential"
  ],
  "restricted_attribute_groups": [
    "sensitive_health_data",
    "genetic_information",
    "mental_health_data"
  ],
  "compliance_requirements": [
    "HIPAA_compliance",
    "explicit_consent_required",
    "data_protection_impact_assessment",
    "medical_privacy_protection"
  ]
}
```

## Conclusion

The definition of additive and subtractive policy approaches provides the WP4 Trust Infrastructure with flexible and secure policy management capabilities. These approaches enable different security postures suitable for various deployment scenarios, from high-security zero-trust environments to flexible permissive ecosystems.

The integration with OpenID Federation trust marks ensures interoperability and standardized policy communication across different trust domains. The comprehensive attribute and credential classification system provides a solid foundation for policy definition and enforcement.

The implementation guidelines and examples demonstrate practical applications of these policy approaches in real-world scenarios, ensuring that the trust framework can meet diverse requirements while maintaining security and compliance standards.

## References

### Standards
- [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html)
- [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)
- [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf)
- [ETSI TS 119 475](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.00.00_60/ts_119475v010000p.pdf)
- [ISO/IEC 19794](https://www.iso.org/standard/38770.html) (Biometric data)
- [HL7 FHIR](https://www.hl7.org/fhir/) (Health data)

### Related Documents
- [Trust Framework Definition](../task2-trust-framework/README.md)
- [Policy Data Models](README.md#data-models)
- [Trust Evaluation Methods](../task2-trust-framework/trust-infrastructure-schema.md)
- [Use Cases](../task1-use-cases/README.md)

### External Resources
- [Zero Trust Architecture](https://www.nist.gov/publications/zero-trust-architecture)
- [GDPR Compliance](https://gdpr.eu/)
- [EIDAS Regulation](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [PCI DSS Standards](https://www.pcisecuritystandards.org/)


