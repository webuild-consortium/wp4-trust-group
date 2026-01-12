# Onboarding API

This directory contains the implementation of the Onboarding API for the WP4 Trust Infrastructure.

**Note on Schema Harmonization**: The data models defined in this API are harmonized with the [Task 5 data models](../task5-participants-certificates-policies/README.md#data-models) and the [onboarding use case documents](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md) to ensure consistency across the trust infrastructure. Participant types, status values, certificate types, and certificate status values are aligned across all specifications.

## API Overview

The Onboarding API provides comprehensive services for participant registration, certificate management, policy management, and compliance validation within the trust infrastructure.

## Core Services

### Participant Registration Services
- **Participant Registration**: Register new participants
- **Participant Management**: Manage participant information
- **Participant Validation**: Validate participant data
- **Participant Status**: Track participant status

### Certificate Management Services
- **Certificate Submission**: Submit certificates for validation
- **Certificate Validation**: Validate certificate data
- **Certificate Storage**: Store validated certificates
- **Certificate Retrieval**: Retrieve certificate information

### Policy Management Services
- **Policy Submission**: Submit policies for validation
- **Policy Validation**: Validate policy compliance
- **Policy Storage**: Store validated policies
- **Policy Retrieval**: Retrieve policy information

### Compliance Validation Services
- **Compliance Checking**: Check participant compliance
- **Audit Management**: Manage compliance audits
- **Compliance Reporting**: Generate compliance reports
- **Compliance Monitoring**: Monitor compliance status

## API Endpoints

### Participant Registration
```
POST   /api/v1/onboarding/register              # Register participant
GET    /api/v1/onboarding/status/{participantId} # Get registration status
PUT    /api/v1/onboarding/update/{participantId} # Update participant
DELETE /api/v1/onboarding/remove/{participantId} # Remove participant
```

### Certificate Management
```
POST   /api/v1/onboarding/certificates          # Submit certificate
GET    /api/v1/onboarding/certificates/{certId} # Get certificate
PUT    /api/v1/onboarding/certificates/{certId} # Update certificate
DELETE /api/v1/onboarding/certificates/{certId} # Revoke certificate
```

### Policy Management
```
POST   /api/v1/onboarding/policies              # Submit policy
GET    /api/v1/onboarding/policies/{policyId}   # Get policy
PUT    /api/v1/onboarding/policies/{policyId}   # Update policy
DELETE /api/v1/onboarding/policies/{policyId}   # Delete policy
```

### Compliance Validation
```
POST   /api/v1/onboarding/validate              # Validate compliance
GET    /api/v1/onboarding/compliance/{participantId} # Get compliance status
POST   /api/v1/onboarding/audit                 # Request audit
GET    /api/v1/onboarding/audit/{auditId}       # Get audit result
```

## Data Models

### Participant
```json
{
  "participantId": "string",
  "participantType": "RELYING_PARTY|PID_PROVIDER|QEAA_PROVIDER|PUB_EAA_PROVIDER|NON_Q_EAA_PROVIDER|WALLET_PROVIDER|ACCESS_CA|REGISTRATION_CA",
  "participantName": "string",
  "participantStatus": "PENDING|ACTIVE|INACTIVE|SUSPENDED|REVOKED",
  "contactInfo": {
    "email": "string",
    "phone": "string",
    "address": "string"
  },
  "website": "string",
  "officialIdentifiers": ["string"],
  "memberState": "string",
  "entitlements": ["string"],
  "registrationDate": "2024-01-01T00:00:00Z",
  "lastUpdated": "2024-01-01T00:00:00Z"
}
```

### Certificate
```json
{
  "certificateId": "string",
  "participantId": "string",
  "certificateType": "ACCESS_CERTIFICATE|REGISTRATION_CERTIFICATE",
  "certificateData": "string",
  "certificateStatus": "PENDING|VALID|INVALID|REVOKED|EXPIRED",
  "validFrom": "2024-01-01T00:00:00Z",
  "validTo": "2024-12-31T23:59:59Z",
  "revokedAt": "2024-01-01T00:00:00Z",
  "revocationReason": "string",
  "submittedAt": "2024-01-01T00:00:00Z",
  "validatedAt": "2024-01-01T00:00:00Z"
}
```

### Policy
```json
{
  "policyId": "string",
  "participantId": "string",
  "policyType": "IDENTITY|SECURITY|OPERATIONAL|LEGAL",
  "policyContent": "string",
  "policyStatus": "PENDING|APPROVED|REJECTED|EXPIRED",
  "submittedAt": "2024-01-01T00:00:00Z",
  "reviewedAt": "2024-01-01T00:00:00Z",
  "reviewedBy": "string"
}
```

### Compliance Status
```json
{
  "participantId": "string",
  "complianceStatus": "COMPLIANT|NON_COMPLIANT|PENDING|UNDER_REVIEW",
  "complianceScore": 0.0-1.0,
  "lastChecked": "2024-01-01T00:00:00Z",
  "nextCheck": "2024-01-01T00:00:00Z",
  "violations": [],
  "recommendations": []
}
```

### Audit
```json
{
  "auditId": "string",
  "participantId": "string",
  "auditType": "INITIAL|PERIODIC|AD_HOC|COMPLAINT",
  "auditStatus": "PENDING|IN_PROGRESS|COMPLETED|FAILED",
  "auditResult": {
    "complianceStatus": "COMPLIANT|NON_COMPLIANT",
    "findings": [],
    "recommendations": []
  },
  "auditDate": "2024-01-01T00:00:00Z",
  "auditorId": "string"
}
```

## Registration Workflow

The registration workflow follows the detailed onboarding phases defined in the [onboarding use case documents](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md):

### Phase 1: Administrative Onboarding
1. **Application Submission**: Participant submits registration application with required information (see [Common Administrative Onboarding Steps - 1.1 Registration Application](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#11-registration-application))
2. **Review**: Registrar verifies the registration application (see [Common Administrative Onboarding Steps - 1.2 Registration Review](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#12-registration-review))
3. **Confirmation**: Registrar validates or rejects the registration application (see [Common Administrative Onboarding Steps - 1.3 Registration Confirmation](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#13-registration-confirmation))
4. **Publication**: Registrar registers the entity in its registry and publishes it (see [Common Administrative Onboarding Steps - 1.4 Publication in the National Register](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#14-publication-in-the-national-register))

### Phase 2: Technical Onboarding
1. **Access Certificate Request**: Registrar informs Access Certificate Authority about registered entity (see [Common Technical Onboarding Steps - 2.1 Access Certificate Request](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#21-access-certificate-request))
2. **Access Certificate Review**: Access Certificate Authority verifies identity and registration status (see [Common Technical Onboarding Steps - 2.2 Access Certificate Request Review](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#22-access-certificate-request-review))
3. **Access Certificate Issuance**: Access Certificate Authority issues and logs the Access Certificate (see [Common Technical Onboarding Steps - 2.3 Access Certificate Issuance](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#23-access-certificate-issuance))
4. **Registration Certificate Request**: Registrar informs Provider of Registration Certificate about registered entity (see [Common Technical Onboarding Steps - 2.4 Registration Certificate Request](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#24-registration-certificate-request))
5. **Registration Certificate Review**: Provider of Registration Certificate verifies identity and registration status (see [Common Technical Onboarding Steps - 2.5 Registration Certificate Request Review](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#25-registration-certificate-request-review))
6. **Registration Certificate Issuance**: Provider of Registration Certificate issues and logs the Registration Certificate (see [Common Technical Onboarding Steps - 2.6 Registration Certificate Issuance](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#26-registration-certificate-issuance))
7. **Notification and Trusted List Publication**: (For PID/EAA Providers) Member State notifies EU Commission and publishes trust anchor in Trusted List (see entity-specific onboarding documents)

### Phase 3: Post-Onboarding
1. **Registration Monitoring**: Continuous monitoring of registration status and compliance (see [Common Post-Onboarding Steps - 3.1 Registration Monitoring](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#31-registration-monitoring))
2. **Registration Update**: Entity updates information as needed (see [Common Post-Onboarding Steps - 3.2 Registration Update](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#32-registration-update))
3. **Registration Suspension/Cancellation**: Suspension or cancellation procedures when needed (see [Common Post-Onboarding Steps - 3.3 Registration Suspension / Cancellation](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#33-registration-suspension--cancellation))
4. **Certificate Revocation**: Certificate revocation procedures (see [Common Post-Onboarding Steps - 3.4 Certificate Revocation](../../task1-use-cases/subtask1-1-onboarding/onboarding-base.md#34-certificate-revocation))

## Certificate Validation Process

### Step 1: Certificate Submission
1. Participant submits certificate
2. System validates certificate format
3. System checks certificate chain
4. System stores certificate

### Step 2: Certificate Validation
1. System retrieves certificate
2. System validates certificate chain
3. System checks revocation status
4. System returns validation result

### Step 3: Certificate Storage
1. System stores validated certificate
2. System updates participant status
3. System notifies participant
4. System logs validation result

## Policy Validation Process

### Step 1: Policy Submission
1. Participant submits policy document
2. System validates policy format
3. System checks policy compliance
4. System stores policy

### Step 2: Policy Review
1. Administrator reviews policy
2. Administrator validates policy content
3. Administrator checks compliance status
4. Administrator approves or rejects policy

### Step 3: Policy Activation
1. System activates approved policy
2. System updates participant status
3. System notifies participant
4. System logs policy activation

## Compliance Validation Process

### Step 1: Compliance Check
1. System retrieves participant data
2. System validates compliance criteria
3. System generates compliance report
4. System updates compliance status

### Step 2: Compliance Reporting
1. System generates compliance report
2. System notifies participant
3. System stores compliance record
4. System schedules next check

### Step 3: Compliance Monitoring
1. System monitors compliance status
2. System tracks compliance changes
3. System alerts on violations
4. System maintains compliance history

## Error Handling

### Error Response Format
```json
{
  "error": {
    "code": "ONBOARD_001",
    "message": "Participant registration failed",
    "details": {
      "participantId": "participant-123",
      "validationErrors": []
    },
    "timestamp": "2024-01-01T00:00:00Z",
    "requestId": "req-789"
  }
}
```

### Error Codes
- `ONBOARD_001`: Participant registration failed
- `ONBOARD_002`: Certificate validation failed
- `ONBOARD_003`: Policy validation failed
- `ONBOARD_004`: Compliance check failed
- `ONBOARD_005`: Audit request failed
- `VALID_001`: Validation error
- `AUTH_001`: Authentication required
- `AUTH_002`: Authorization denied

## Security Requirements

### Authentication
- **OAuth 2.0**: OAuth 2.0 authentication
- **OpenID Connect**: OpenID Connect authentication
- **JWT Tokens**: JSON Web Token authentication
- **API Keys**: API key authentication

### Authorization
- **Role-Based Access**: Role-based access control
- **Permission-Based Access**: Permission-based access control
- **Resource-Based Access**: Resource-based access control
- **Time-Based Access**: Time-based access control

### Data Protection
- **Encryption at Rest**: Data encryption at rest
- **Encryption in Transit**: Data encryption in transit
- **Data Masking**: Sensitive data masking
- **Data Retention**: Data retention policies

## Monitoring and Logging

### API Monitoring
- **Response Times**: API response time monitoring
- **Error Rates**: API error rate monitoring
- **Throughput**: API throughput monitoring
- **Availability**: API availability monitoring

### Audit Logging
- **Registration Events**: Participant registration events
- **Certificate Events**: Certificate management events
- **Policy Events**: Policy management events
- **Compliance Events**: Compliance validation events

### Security Logging
- **Authentication Events**: Authentication events
- **Authorization Events**: Authorization events
- **Data Access Events**: Data access events
- **Security Events**: Security-related events