---
name: Policy Approaches Definition - Additive vs Subtractive
about: Define additive and subtractive policy approaches for trust framework design methodologies
title: '[POLICY] Define Additive and Subtractive Policy Approaches for Trust Framework'
labels: ['enhancement', 'policy', 'trust-framework', 'design-methodology']
assignees: ''
---

# Policy Approaches Definition: Additive vs Subtractive

## Overview

This issue addresses the need to define and propose two distinct policy approaches within the trust framework design methodologies for the WP4 Trust Infrastructure. 

These approaches needs discussions and comments from the participants, along with implementative considerations about a flexible policy management for both credential issuers and relying parties.

## Problem Statement

The current trust framework lacks clear definitions and implementation guidelines for different policy approaches. We need to establish:

1. **Additive Policy Approach**: Explicit allow-list model (zero-trust principle)
2. **Subtractive Policy Approach**: Explicit deny-list model (permissive principle)

These approaches must be applicable to both:
- **Credential Issuers**: Policies governing what Credential types and attribute groups they are authorized to issue
- **Relying Parties**: Policies governing what User attributes they are authorized to request

## Background

### Zero Trust Principle
A zero-trust approach requires an additive policy model where nothing is granted by default, and only explicitly authorized actions are permitted. 

> Note: This mirrors firewall security models with "reject" or "drop" rules that only allow explicitly configured permissions.

### Policy Approaches Comparison

| Aspect | Additive Approach | Subtractive Approach |
|--------|------------------|---------------------|
| **Default State** | Deny all | Allow all |
| **Authorization** | Explicit allow-list | Explicit deny-list |
| **Security Model** | Zero-trust | Permissive |
| **Configuration** | Grant specific permissions | Block specific restrictions |
| **Risk Level** | Lower (conservative) | Higher (permissive) |
| **Maintenance** | More granular control | Easier to manage |

## Requirements

### 1. Policy Approach Definitions

#### Additive Policy Approach

- **Definition**: Explicit allow-list model where permissions are granted only when explicitly authorized
- **Principle**: "Nothing is permitted unless explicitly allowed"
- **Implementation**: Default deny with explicit allow rules
- **Use Cases**: High-security environments, zero-trust architectures, sensitive data handling

#### Subtractive Policy Approach

- **Definition**: Explicit deny-list model where permissions are granted by default except for explicitly restricted items
- **Principle**: "Everything is permitted unless explicitly denied"
- **Implementation**: Default allow with explicit deny rules
- **Use Cases**: Open ecosystems, development environments, rapid prototyping

### 2. Application Scope

#### For Credential Issuers
- **Credential Types**: Define which credential types the issuer is authorized to issue
- **Attribute Groups**: Define which attribute groups can be included in credentials
- **Data Model Compliance**: Ensure compliance with predefined data models
- **Scope Restrictions**: Define operational scope and limitations

#### For Relying Parties
- **User Attributes**: Define which user attributes the RP is authorized to request
- **Purpose Limitations**: Define the purposes for which attributes can be used
- **Data Retention**: Define data retention and processing limitations
- **Consent Requirements**: Define user consent requirements
