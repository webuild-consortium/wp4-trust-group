# Trust Infrastructure API

This directory contains the implementation of the Trust Infrastructure API for the WP4 Trust Infrastructure.

## API Overview

The Trust Infrastructure API provides comprehensive services for trust management, evaluation, validation, and monitoring within the digital wallet ecosystem.

## Core Services

### Trust Management Services
- **Trust Establishment**: Establish trust relationships between entities
- **Trust Maintenance**: Maintain and update trust relationships
- **Trust Revocation**: Revoke trust relationships when necessary
- **Trust Status**: Query and monitor trust status

### Trust Evaluation Services
- **Trust Scoring**: Calculate trust scores for entities
- **Trust Assessment**: Assess trust levels and factors
- **Trust Validation**: Validate trust relationships
- **Trust History**: Track trust history and changes

### Trust Policy Services
- **Policy Management**: Manage trust policies
- **Policy Enforcement**: Enforce trust policies
- **Policy Compliance**: Check policy compliance
- **Policy Updates**: Update and modify policies

### Trust Monitoring Services
- **Status Monitoring**: Monitor trust status
- **Alert Management**: Manage trust alerts
- **Reporting**: Generate trust reports
- **Analytics**: Trust analytics and insights

## API Endpoints

### Trust Management
```
GET    /api/v1/trust/status                    # Get trust status
POST   /api/v1/trust/establish                 # Establish trust
PUT    /api/v1/trust/update                    # Update trust
DELETE /api/v1/trust/revoke                    # Revoke trust
```

### Trust Evaluation
```
POST   /api/v1/trust/evaluate                  # Evaluate trust
GET    /api/v1/trust/score/{entityId}          # Get trust score
POST   /api/v1/trust/validate                  # Validate trust
GET    /api/v1/trust/history/{entityId}        # Get trust history
```

### Trust Policies
```
GET    /api/v1/trust/policies                  # Get policies
POST   /api/v1/trust/policies                  # Create policy
PUT    /api/v1/trust/policies/{policyId}       # Update policy
DELETE /api/v1/trust/policies/{policyId}       # Delete policy
```

### Trust Monitoring
```
GET    /api/v1/trust/monitoring/status         # Get monitoring status
GET    /api/v1/trust/monitoring/alerts         # Get alerts
POST   /api/v1/trust/monitoring/configure      # Configure monitoring
GET    /api/v1/trust/monitoring/reports        # Get reports
```

## Data Models

### Trust Entity
```json
{
  "entityId": "string",
  "entityType": "TSP|WALLET_PROVIDER|RELYING_PARTY|CA",
  "entityStatus": "ACTIVE|INACTIVE|SUSPENDED|REVOKED",
  "trustLevel": 1-4,
  "trustScore": 0.0-1.0,
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

### Trust Relationship
```json
{
  "relationshipId": "string",
  "sourceEntityId": "string",
  "targetEntityId": "string",
  "relationshipType": "TRUST|CERTIFICATION|AUTHORIZATION",
  "relationshipStatus": "ACTIVE|INACTIVE|SUSPENDED|REVOKED",
  "trustLevel": 1-4,
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

### Trust Policy
```json
{
  "policyId": "string",
  "policyType": "IDENTITY|SECURITY|OPERATIONAL|LEGAL",
  "policyContent": {
    "rules": [],
    "constraints": [],
    "requirements": []
  },
  "policyStatus": "ACTIVE|INACTIVE|DRAFT",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

### Trust Assessment
```json
{
  "assessmentId": "string",
  "entityId": "string",
  "assessmentType": "INITIAL|PERIODIC|AD_HOC|EMERGENCY",
  "assessmentResult": {
    "trustLevel": 1-4,
    "trustScore": 0.0-1.0,
    "factors": [],
    "recommendations": []
  },
  "assessedAt": "2024-01-01T00:00:00Z",
  "assessorId": "string"
}
```

## Authentication and Authorization

### Authentication Methods
- **OAuth 2.0**: OAuth 2.0 authentication
- **OpenID Connect**: OpenID Connect authentication
- **JWT Tokens**: JSON Web Token authentication
- **API Keys**: API key authentication

### Authorization Levels
- **Admin**: Full access to all operations
- **Trust Manager**: Trust management operations
- **Trust Evaluator**: Trust evaluation operations
- **Trust Monitor**: Trust monitoring operations
- **Read Only**: Read-only access

### Security Requirements
- **HTTPS Only**: All communications over HTTPS
- **TLS 1.3**: Minimum TLS 1.3 encryption
- **Request Signing**: Request signature validation
- **Rate Limiting**: API rate limiting
- **Input Validation**: Comprehensive input validation

## Error Handling

### Error Response Format
```json
{
  "error": {
    "code": "TRUST_001",
    "message": "Trust relationship not found",
    "details": {
      "entityId": "entity-123",
      "relationshipId": "rel-456"
    },
    "timestamp": "2024-01-01T00:00:00Z",
    "requestId": "req-789"
  }
}
```

### Error Codes
- `TRUST_001`: Trust relationship not found
- `TRUST_002`: Invalid trust level
- `TRUST_003`: Trust evaluation failed
- `TRUST_004`: Policy validation failed
- `TRUST_005`: Trust revocation failed
- `AUTH_001`: Authentication required
- `AUTH_002`: Authorization denied
- `VALID_001`: Validation error
- `SYS_001`: System error

## Rate Limiting

### Rate Limits
- **Standard Users**: 1000 requests per hour
- **Trust Managers**: 5000 requests per hour
- **Trust Evaluators**: 2000 requests per hour
- **Trust Monitors**: 10000 requests per hour
- **Admin Users**: 50000 requests per hour

### Rate Limit Headers
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

## Monitoring and Logging

### API Monitoring
- **Response Times**: API response time monitoring
- **Error Rates**: API error rate monitoring
- **Throughput**: API throughput monitoring
- **Availability**: API availability monitoring

### Logging
- **Request Logging**: All API requests logged
- **Response Logging**: All API responses logged
- **Error Logging**: All errors logged with details
- **Audit Logging**: All trust operations audited

### Metrics
- **Trust Operations**: Trust operation metrics
- **API Performance**: API performance metrics
- **Error Metrics**: Error rate and type metrics
- **Usage Metrics**: API usage metrics

## Testing

### Unit Testing
- **Service Testing**: Individual service testing
- **Model Testing**: Data model testing
- **Validation Testing**: Input validation testing
- **Error Testing**: Error handling testing

### Integration Testing
- **API Testing**: End-to-end API testing
- **Database Testing**: Database integration testing
- **External Service Testing**: External service integration testing
- **Performance Testing**: API performance testing

### Security Testing
- **Authentication Testing**: Authentication mechanism testing
- **Authorization Testing**: Authorization mechanism testing
- **Input Validation Testing**: Input validation security testing
- **Penetration Testing**: Security penetration testing

## Documentation

### API Documentation
- **OpenAPI Specification**: Complete OpenAPI 3.0 specification
- **Interactive Documentation**: Swagger UI documentation
- **Code Examples**: Code examples for all endpoints
- **SDK Documentation**: Software development kit documentation

### Developer Resources
- **Getting Started Guide**: Quick start guide
- **Authentication Guide**: Authentication setup guide
- **Error Handling Guide**: Error handling guide
- **Best Practices Guide**: API usage best practices

## Deployment

### Environment Requirements
- **Java 17+**: Java 17 or higher
- **Spring Boot 3.x**: Spring Boot 3.x framework
- **PostgreSQL 13+**: PostgreSQL 13 or higher
- **Redis 6+**: Redis 6 or higher for caching

### Deployment Options
- **Docker**: Docker container deployment
- **Kubernetes**: Kubernetes orchestration
- **Cloud Platforms**: AWS, Azure, GCP deployment
- **On-Premises**: On-premises deployment

### Configuration
- **Environment Variables**: Environment-based configuration
- **Configuration Files**: YAML configuration files
- **Secrets Management**: Secure secrets management
- **Monitoring Configuration**: Monitoring and logging configuration
