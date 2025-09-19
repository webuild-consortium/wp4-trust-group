# ETSI Specifications Policy Application Evaluation

## Executive Summary

This document evaluates ETSI (European Telecommunications Standards Institute) specifications and their application to policy frameworks within trust infrastructures. The evaluation focuses on how ETSI standards support both additive and subtractive policy approaches for credential issuers and relying parties in digital wallet ecosystems.

## Table of Contents

1. [ETSI Policy Framework Overview](#etsi-policy-framework-overview)
2. [Certificate Profile Standards](#certificate-profile-standards)
3. [Trust Service Provider Standards](#trust-service-provider-standards)
4. [Policy Application Mechanisms](#policy-application-mechanisms)
5. [Additive vs Subtractive Policy Support](#additive-vs-subtractive-policy-support)
6. [Implementation Guidelines](#implementation-guidelines)
7. [Compliance Requirements](#compliance-requirements)

## ETSI Policy Framework Overview

### Core Policy Principles

ETSI standards establish several fundamental principles for policy application in trust frameworks:

1. **Interoperability**: Policies must ensure cross-border and cross-domain compatibility
2. **Security**: Policies must maintain appropriate security levels for different use cases
3. **Compliance**: Policies must align with EU regulations (EIDAS, GDPR, etc.)
4. **Transparency**: Policy definitions must be clear and auditable
5. **Flexibility**: Policies must support various deployment scenarios

### Policy Hierarchy

ETSI specifications define a hierarchical policy structure:

```
Regulatory Level (EIDAS, GDPR)
    ↓
ETSI Standards Level (EN 319 xxx series)
    ↓
Implementation Level (Certificate Policies, CPS)
    ↓
Operational Level (Trust Service Provider policies)
```

## Certificate Profile Standards

### ETSI EN 319 412 Series: Certificate Profiles

#### EN 319 412-1: Overview and Common Data Structures
- **Policy Application**: Defines common data structures for policy implementation
- **Additive Support**: Enables explicit definition of required certificate attributes
- **Subtractive Support**: Provides framework for excluding specific attributes
- **Key Features**:
  - Policy Object Identifiers (OIDs)
  - Certificate extensions structure
  - Common attribute definitions

#### EN 319 412-2: Certificate Profile for Natural Persons
- **Policy Application**: Specifies attributes and extensions for individual certificates
- **Additive Support**: Defines mandatory attributes that must be present
- **Subtractive Support**: Allows exclusion of sensitive attributes
- **Key Attributes**:
  - Personal identification data
  - Authentication attributes
  - Role and affiliation information
  - Biometric data (when applicable)

#### EN 319 412-4: Certificate Profile for Web Site Certificates
- **Policy Application**: Defines policies for website authentication
- **Additive Support**: Specifies required domain validation
- **Subtractive Support**: Excludes certain domain types
- **Key Features**:
  - Domain name validation
  - Organization validation
  - Extended validation (EV) requirements

#### EN 319 412-5: QCStatements
- **Policy Application**: Defines qualified certificate statements
- **Additive Support**: Explicitly states compliance with specific policies
- **Subtractive Support**: Excludes non-qualified use cases
- **Key Statements**:
  - Qualified certificate status
  - Policy compliance indicators
  - Usage restrictions

#### EN 319 412-6: Certificate Profile for EUDI Wallet Providers
- **Policy Application**: Specific to EU Digital Identity Wallet ecosystem
- **Additive Support**: Defines required attributes for wallet providers
- **Subtractive Support**: Excludes non-compliant attributes
- **Key Features**:
  - Wallet instance attestation
  - Security compliance verification
  - Cross-border recognition

## Trust Service Provider Standards

### ETSI EN 319 401: General Policy Requirements for TSPs

#### Policy Framework Requirements
- **Governance**: TSPs must establish clear policy governance structures
- **Documentation**: Comprehensive policy documentation requirements
- **Review Process**: Regular policy review and update procedures
- **Compliance Monitoring**: Ongoing compliance verification mechanisms

#### Additive Policy Support
```json
{
  "policy_type": "additive",
  "tsp_requirements": {
    "mandatory_services": [
      "certificate_issuance",
      "certificate_revocation",
      "timestamping"
    ],
    "required_attributes": [
      "organization_name",
      "registration_number",
      "contact_information"
    ],
    "security_requirements": [
      "hsm_protection",
      "audit_logging",
      "incident_response"
    ]
  }
}
```

#### Subtractive Policy Support
```json
{
  "policy_type": "subtractive",
  "tsp_restrictions": {
    "prohibited_services": [
      "anonymous_certificate_issuance",
      "self_signed_certificates"
    ],
    "excluded_attributes": [
      "biometric_templates",
      "financial_account_numbers"
    ],
    "security_restrictions": [
      "no_shared_private_keys",
      "no_weak_cryptography"
    ]
  }
}
```

### ETSI EN 319 411 Series: Policy and Security Requirements

#### EN 319 411-1: General Requirements
- **Policy Scope**: General requirements for all TSPs
- **Security Baseline**: Minimum security requirements
- **Operational Procedures**: Standard operational practices
- **Audit Requirements**: Regular audit and assessment procedures

#### EN 319 411-2: Requirements for Qualified Certificate Issuers
- **Policy Scope**: Additional requirements for qualified certificate issuers
- **EIDAS Compliance**: Full compliance with EIDAS regulation
- **Qualified Status**: Requirements for maintaining qualified status
- **Cross-border Recognition**: International interoperability requirements

#### EN 319 411-8: Access Certificate Policy for EUDI Wallet Relying Parties
- **Policy Scope**: Specific to EUDI Wallet ecosystem relying parties
- **Attribute Access**: Policies governing attribute access requests
- **Consent Management**: User consent requirements and procedures
- **Data Protection**: GDPR compliance requirements

### ETSI TS 119 475: Relying Party Attributes

#### Policy Application Framework
- **Attribute Classification**: Systematic classification of user attributes
- **Access Control**: Policies governing attribute access
- **Purpose Limitation**: Restrictions on attribute usage
- **Consent Requirements**: User consent management

#### Additive Policy Implementation
```json
{
  "policy_approach": "additive",
  "authorized_attributes": [
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
  ]
}
```

#### Subtractive Policy Implementation
```json
{
  "policy_approach": "subtractive",
  "restricted_attributes": [
    {
      "attribute_type": "biometric_data",
      "restriction_reason": "Privacy protection",
      "exceptions": ["explicit_consent", "law_enforcement"]
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
  ]
}
```

## Policy Application Mechanisms

### Certificate Policy (CP) and Certification Practice Statement (CPS)

#### Policy Definition Structure
```
Certificate Policy
├── Policy Identification
├── Policy Scope
├── Policy Requirements
├── Policy Enforcement
└── Policy Maintenance
```

#### Additive Policy Elements
- **Mandatory Requirements**: Explicitly defined requirements
- **Inclusion Criteria**: What must be included
- **Validation Rules**: Required validation procedures
- **Compliance Indicators**: Clear compliance markers

#### Subtractive Policy Elements
- **Exclusion Criteria**: What must be excluded
- **Prohibition Rules**: Explicit prohibitions
- **Exception Handling**: Limited exceptions
- **Risk Mitigation**: Risk-based restrictions

### Trust Mark Integration

#### ETSI Trust Mark Framework
- **Trust Mark Structure**: Standardized trust mark format
- **Policy Assertions**: Policy compliance assertions
- **Verification Mechanisms**: Trust mark validation
- **Revocation Procedures**: Trust mark revocation

#### OpenID Federation Integration
```json
{
  "trust_mark_id": "etsi_compliance_mark_v1.0",
  "issuer": "https://trust-registry.etsi.org",
  "subject": "https://tsp.example.com",
  "trust_mark_type": "etsi_compliance",
  "policy_assertions": [
    {
      "policy_type": "EN_319_411_1",
      "compliance_level": "full",
      "validated_at": "2024-01-01T00:00:00Z"
    },
    {
      "policy_type": "EN_319_412_2",
      "compliance_level": "full",
      "validated_at": "2024-01-01T00:00:00Z"
    }
  ],
  "cryptographic_proof": {
    "type": "JsonWebSignature2020",
    "created": "2024-01-01T00:00:00Z",
    "verificationMethod": "https://trust-registry.etsi.org#key-1",
    "proofValue": "..."
  }
}
```

## Additive vs Subtractive Policy Support

### ETSI Support for Additive Policies

#### Certificate Level
- **Mandatory Extensions**: Required certificate extensions
- **Attribute Requirements**: Mandatory attribute presence
- **Validation Rules**: Required validation procedures
- **Compliance Markers**: Clear compliance indicators

#### Service Level
- **Required Services**: Mandatory service offerings
- **Security Requirements**: Minimum security standards
- **Operational Procedures**: Required operational practices
- **Audit Requirements**: Mandatory audit procedures

#### Implementation Example
```json
{
  "etsi_policy_type": "additive",
  "certificate_requirements": {
    "mandatory_extensions": [
      "keyUsage",
      "extendedKeyUsage",
      "basicConstraints",
      "subjectAlternativeName"
    ],
    "required_attributes": [
      "commonName",
      "organizationName",
      "countryName"
    ],
    "validation_requirements": [
      "identity_verification",
      "domain_validation",
      "organization_validation"
    ]
  },
  "service_requirements": {
    "mandatory_services": [
      "certificate_issuance",
      "certificate_revocation",
      "timestamping"
    ],
    "security_requirements": [
      "hsm_protection",
      "audit_logging",
      "incident_response"
    ]
  }
}
```

### ETSI Support for Subtractive Policies

#### Certificate Level
- **Prohibited Extensions**: Excluded certificate extensions
- **Attribute Restrictions**: Prohibited attributes
- **Usage Limitations**: Restricted usage scenarios
- **Compliance Exclusions**: Non-compliant indicators

#### Service Level
- **Prohibited Services**: Excluded service offerings
- **Security Restrictions**: Prohibited security practices
- **Operational Limitations**: Restricted operational practices
- **Audit Exclusions**: Excluded audit procedures

#### Implementation Example
```json
{
  "etsi_policy_type": "subtractive",
  "certificate_restrictions": {
    "prohibited_extensions": [
      "biometricData",
      "financialData",
      "healthData"
    ],
    "restricted_attributes": [
      "socialSecurityNumber",
      "bankAccountNumber",
      "medicalRecordNumber"
    ],
    "usage_limitations": [
      "no_anonymous_usage",
      "no_shared_private_keys",
      "no_weak_cryptography"
    ]
  },
  "service_restrictions": {
    "prohibited_services": [
      "anonymous_certificate_issuance",
      "self_signed_certificates",
      "unvalidated_certificates"
    ],
    "security_restrictions": [
      "no_shared_private_keys",
      "no_weak_cryptography",
      "no_unencrypted_storage"
    ]
  }
}
```

## Implementation Guidelines

### Policy Definition Process

#### Step 1: Policy Scope Definition
1. **Identify Stakeholders**: Define all relevant stakeholders
2. **Define Scope**: Determine policy scope and boundaries
3. **Assess Requirements**: Identify regulatory and technical requirements
4. **Choose Approach**: Select additive or subtractive approach

#### Step 2: Policy Content Development
1. **Define Rules**: Create specific policy rules
2. **Specify Procedures**: Define implementation procedures
3. **Set Requirements**: Establish compliance requirements
4. **Create Documentation**: Develop comprehensive documentation

#### Step 3: Policy Validation
1. **Technical Validation**: Verify technical feasibility
2. **Legal Validation**: Ensure legal compliance
3. **Stakeholder Review**: Conduct stakeholder review
4. **Pilot Testing**: Implement pilot testing

#### Step 4: Policy Implementation
1. **System Configuration**: Configure systems according to policy
2. **Training**: Train staff on policy requirements
3. **Monitoring**: Implement monitoring and compliance checking
4. **Continuous Improvement**: Regular policy review and updates

### Technical Implementation

#### Certificate Policy Implementation
```python
class ETSIPolicyEngine:
    def __init__(self, policy_type="additive"):
        self.policy_type = policy_type
        self.etsi_standards = self.load_etsi_standards()
        
    def evaluate_certificate_request(self, request):
        if self.policy_type == "additive":
            return self.evaluate_additive_policy(request)
        else:
            return self.evaluate_subtractive_policy(request)
    
    def evaluate_additive_policy(self, request):
        # Check mandatory requirements
        required_attributes = self.etsi_standards.get_required_attributes()
        for attr in required_attributes:
            if not request.has_attribute(attr):
                return {"decision": "deny", "reason": f"Missing required attribute: {attr}"}
        
        # Check validation requirements
        validation_rules = self.etsi_standards.get_validation_rules()
        for rule in validation_rules:
            if not self.validate_rule(rule, request):
                return {"decision": "deny", "reason": f"Validation failed: {rule}"}
        
        return {"decision": "allow", "reason": "All requirements satisfied"}
    
    def evaluate_subtractive_policy(self, request):
        # Check prohibited elements
        prohibited_attributes = self.etsi_standards.get_prohibited_attributes()
        for attr in prohibited_attributes:
            if request.has_attribute(attr):
                return {"decision": "deny", "reason": f"Prohibited attribute present: {attr}"}
        
        # Check restrictions
        restrictions = self.etsi_standards.get_restrictions()
        for restriction in restrictions:
            if self.violates_restriction(restriction, request):
                return {"decision": "deny", "reason": f"Restriction violated: {restriction}"}
        
        return {"decision": "allow", "reason": "No restrictions violated"}
```

#### Trust Mark Implementation
```python
class ETSITrustMark:
    def __init__(self, policy_assertions):
        self.policy_assertions = policy_assertions
        self.etsi_compliance = self.validate_etsi_compliance()
    
    def validate_etsi_compliance(self):
        compliance_status = {}
        for assertion in self.policy_assertions:
            standard = assertion["policy_type"]
            compliance_level = assertion["compliance_level"]
            compliance_status[standard] = self.check_standard_compliance(standard, compliance_level)
        return compliance_status
    
    def check_standard_compliance(self, standard, required_level):
        # Implementation of ETSI standard compliance checking
        pass
```

## Compliance Requirements

### ETSI Standard Compliance

#### EN 319 412 Series Compliance
- **Certificate Structure**: Adherence to defined certificate structures
- **Attribute Requirements**: Compliance with attribute specifications
- **Extension Requirements**: Proper use of certificate extensions
- **Validation Procedures**: Implementation of required validation

#### EN 319 411 Series Compliance
- **TSP Requirements**: Compliance with TSP requirements
- **Security Standards**: Adherence to security standards
- **Operational Procedures**: Implementation of operational procedures
- **Audit Requirements**: Compliance with audit requirements

#### EN 319 401 Compliance
- **General Requirements**: Adherence to general TSP requirements
- **Policy Framework**: Implementation of policy framework
- **Governance Structure**: Establishment of governance structure
- **Documentation Requirements**: Compliance with documentation requirements

### Regulatory Compliance

#### EIDAS Compliance
- **Qualified Certificates**: Compliance with qualified certificate requirements
- **Trust Service Providers**: Adherence to TSP requirements
- **Cross-border Recognition**: Implementation of cross-border mechanisms
- **Audit and Supervision**: Compliance with audit requirements

#### GDPR Compliance
- **Data Protection**: Implementation of data protection measures
- **Privacy by Design**: Integration of privacy principles
- **Consent Management**: Implementation of consent mechanisms
- **Data Subject Rights**: Support for data subject rights

### Implementation Checklist

#### Policy Definition
- [ ] Policy scope clearly defined
- [ ] Stakeholders identified and consulted
- [ ] Regulatory requirements assessed
- [ ] Technical requirements specified
- [ ] Additive/subtractive approach selected

#### Technical Implementation
- [ ] ETSI standards integrated
- [ ] Policy engine implemented
- [ ] Validation procedures established
- [ ] Monitoring systems deployed
- [ ] Audit trails implemented

#### Compliance Verification
- [ ] ETSI standard compliance verified
- [ ] Regulatory compliance confirmed
- [ ] Security requirements met
- [ ] Operational procedures established
- [ ] Documentation completed

## Conclusion

ETSI specifications provide comprehensive frameworks for implementing both additive and subtractive policy approaches in trust infrastructures. The standards offer:

1. **Clear Policy Structures**: Well-defined policy frameworks and requirements
2. **Technical Specifications**: Detailed technical implementation guidelines
3. **Compliance Frameworks**: Comprehensive compliance verification mechanisms
4. **Interoperability Support**: Cross-border and cross-domain compatibility
5. **Security Standards**: Robust security requirements and procedures

The evaluation demonstrates that ETSI standards fully support both policy approaches, enabling organizations to choose the most appropriate model for their specific use cases while maintaining compliance with European regulations and international standards.

## References

### ETSI Standards
- [ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601c.pdf) - Overview and Common Data Structures
- [ETSI EN 319 412-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401c.pdf) - Certificate Profile for Natural Persons
- [ETSI EN 319 412-4](https://www.etsi.org/deliver/etsi_en/319400_319499/31941204/01.04.01_60/en_31941204v010401c.pdf) - Certificate Profile for Web Site Certificates
- [ETSI EN 319 412-5](https://www.etsi.org/deliver/etsi_en/319400_319499/31941205/02.05.01_60/en_31941205v020501c.pdf) - QCStatements
- [ETSI EN 319 412-6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941206/01.00.00_20/en_31941206v010000c.pdf) - Certificate Profile for EUDI Wallet Providers
- [ETSI EN 319 401](https://www.etsi.org/deliver/etsi_en/319400_319499/319401/01.01.01_60/en_319401v010101c.pdf) - General Policy Requirements for TSPs
- [ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.01.01_60/en_31941101v010101c.pdf) - General Requirements for TSPs
- [ETSI EN 319 411-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941102/01.01.01_60/en_31941102v010101c.pdf) - Requirements for Qualified Certificate Issuers
- [ETSI EN 319 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.00.00_60/ts_11941108v010000c.pdf) - Access Certificate Policy for EUDI Wallet Relying Parties
- [ETSI TS 119 475](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.00.00_60/ts_119475v010000c.pdf) - Relying Party Attributes
- [ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119400_119499/119602/01.00.00_60/ts_119602v010000c.pdf) - Trusted Lists Data Model
- [ETSI TS 119 612](https://www.etsi.org/deliver/etsi_ts/119400_119499/119612/02.03.01_60/ts_119612v020301c.pdf) - Trusted Lists

### Related Documents
- [EIDAS Regulation](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [GDPR Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [RFC 3125](https://datatracker.ietf.org/doc/html/rfc3125) - Electronic Signature Policies


