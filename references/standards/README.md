# Standards

This directory contains official standards and specifications relevant to the WP4 Trust Infrastructure project.

## Trust Infrastructure Core Standards

### ETSI TS 119 612 (v2.4.1) - Trusted Lists
- **Status**: Required
- **Priority**: High
- **Description**: Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists
- **Implementation**: Core component for trust establishment

### IETF RFC 5914 - Trust Anchor Format
- **Status**: Required
- **Priority**: High
- **Description**: Trust Anchor Format
- **Implementation**: Implementation profile required
- **Notes**: Defines the format for trust anchors in the trust infrastructure

### IETF RFC 5280 - X.509 PKI
- **Status**: Required
- **Priority**: High
- **Description**: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
- **Implementation**: Implementation profile required
- **Notes**: Core PKI standard for certificate management

## Certificate and Policy Standards

### ETSI EN 319 412-6 - Certificate Profile Requirements
- **Status**: Required
- **Priority**: High
- **Description**: Certificate profile requirements for PID, Wallet, EAA, QEAA and PSBEAA providers
- **Implementation**: Required for provider certification

### ETSI TS 119 411-8 - Access Certificate Policy
- **Status**: Required
- **Priority**: High
- **Description**: Access Certificate Policy for EUDI Wallet Relying Parties
- **Implementation**: Required for Relying Party policies

### ETSI TS 119 475 - Relying Party Attributes
- **Status**: Required
- **Priority**: High
- **Description**: Relying party attributes supporting EUDI Wallet User's authorisation decisions
- **Implementation**: Required for authorization decisions

## Digital Signature Standards

### ETSI EN 319 132-1 - XAdES Digital Signatures
- **Status**: Required
- **Priority**: High
- **Description**: XAdES digital signatures - Building blocks and XAdES baseline signatures
- **Implementation**: XML-based digital signatures

### ETSI TS 119 182-1 - JAdES Digital Signatures
- **Status**: Required
- **Priority**: High
- **Description**: JAdES digital signatures - Building blocks and JAdES baseline signatures
- **Implementation**: JSON-based digital signatures

### ETSI EN 319 122-1 - CAdES Digital Signatures
- **Status**: Required
- **Priority**: High
- **Description**: CAdES digital signatures - Building blocks and CAdES baseline signatures
- **Implementation**: CMS-based digital signatures

### ETSI EN 319 142-1 - PAdES Digital Signatures
- **Status**: Required
- **Priority**: High
- **Description**: PAdES digital signatures - Building blocks and PAdES baseline signatures
- **Implementation**: PDF-based digital signatures

## Trust Service Provider Standards

### ETSI EN 319 401 - General Policy Requirements
- **Status**: Required
- **Priority**: High
- **Description**: General Policy Requirements for Trust Service Providers
- **Implementation**: Core TSP requirements

### ETSI TS 119 431-1 - TSP Service Components (Remote QSCD)
- **Status**: Required
- **Priority**: High
- **Description**: Policy and security requirements for trust service providers - Part 1: TSP service components operating a remote QSCD / SCDev
- **Implementation**: Remote qualified signature creation device requirements

### ETSI TS 119 431-2 - TSP Service Components (AdES)
- **Status**: Required
- **Priority**: High
- **Description**: Policy and security requirements for trust service providers - Part 2: TSP service components supporting AdES digital signature creation
- **Implementation**: AdES signature creation support

### ETSI TS 119 432 - Remote Digital Signature Protocols
- **Status**: Required
- **Priority**: High
- **Description**: Protocols for remote digital signature creation
- **Implementation**: Remote signature creation protocols

### ETSI TS 119 461 - Identity Proofing Requirements
- **Status**: Required
- **Priority**: High
- **Description**: Policy and security requirements for trust service components providing identity proofing of trust service subjects
- **Implementation**: Identity proofing requirements

## Associated Signature Containers

### ETSI EN 319 162-1 - ASiC
- **Status**: Required
- **Priority**: Medium
- **Description**: Associated Signature Containers (ASiC)
- **Implementation**: Container format for digital signatures

## Implementation Notes

Each standard should be implemented according to its specific requirements and any implementation profiles developed for the WP4 Trust Infrastructure project. Implementation profiles will be documented in the respective task directories.

## Compliance

All implementations must comply with the relevant standards and their implementation profiles. Compliance testing procedures are documented in the testing and validation task directory.
