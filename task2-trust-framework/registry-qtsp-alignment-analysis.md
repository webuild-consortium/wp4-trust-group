# Registry-QTSP Working Group Alignment Analysis

## Overview

This document analyzes the open points and gaps between the Trust Registry working group and the QTSP working group, based on content developed todate in github issues and pull request of the [wp4-trust-group](https://github.com/webuild-consortium/wp4-trust-group).

## What's Missing / Gaps Identified

| Branch | Content | Gap |
|--------|---------|-----|
| [**certs**](https://github.com/webuild-consortium/wp4-trust-group/tree/certs) | ETSI TS 119 411-8, 119 475 specs | Missing: QTSP-specific certificate profiles for dual-role entities |
| [**hrls**](https://github.com/webuild-consortium/wp4-trust-group/tree/hrls) | HLRs matrix | Missing: HLRs for QTSP acting as RP |
| [**infra-schema**](https://github.com/webuild-consortium/wp4-trust-group/tree/infra-schema) | Trust infrastructure schema | Missing: QTSP service endpoints in schema |
| [**etsi-ts-implprof**](https://github.com/webuild-consortium/wp4-trust-group/tree/etsi-ts-implprof) | ETSI 119 612 implementation | Missing: Service type for QTSP-as-RP |
| [**pol-disc**](https://github.com/webuild-consortium/wp4-trust-group/tree/pol-disc) | Policy discovery | Missing: QTSP-specific entitlement discovery |

---

## Open Points for Registry-QTSP WG Coordination

### 1. Service Type URI for QTSP-as-RP

**Issue**: No standardized `ServiceTypeIdentifier` exists for a QTSP that also acts as RP (dual role).

**Current State**: ETSI TS 119 612 defines separate service types:
- `http://uri.etsi.org/TrstSvc/Svctype/CA/QC` for QTSPs issuing qualified certificates
- `http://uri.etsi.org/TrstSvc/Svctype/RelyingParty` for RPs

**Question**: Should a combined service type be defined, or should dual-role entities be listed twice in TSLs?

### 2. WRPRC for QTSPs

**Issue**: Should QTSPs presenting as RPs have WRPRCs?

**Current State**: ETSI TS 119 475 focuses on general RPs. QTSPs already have qualified status in TSL.

**Questions**:
- Does QTSP qualified status in TSL suffice for RP trust?
- Should QTSPs obtain separate WRPRCs for RP activities?
- How should entitlements differ between QTSP services and RP services?

### 3. Entitlement Aggregation

**Issue**: When a QTSP has both:
- QTSP entitlements (from qualified status in TSL)
- RP entitlements (from WRPRC)

**Questions**:
- How should wallets aggregate/display these?
- Which takes precedence in case of conflict?
- Should the wallet show separate trust indicators for each role?

### 4. Cross-Registry Discovery

**Issue**: No defined protocol for wallet to discover which sectoral registers apply to a given RP.

**Current State**: 
- National WRP registers defined in CIR 2025/848
- Sectoral registers (PSD2, healthcare, etc.) exist independently
- No standardized discovery mechanism

**Needed**:
- Registry of registries (meta-registry)
- Sectoral register discovery via TSL extensions
- API specification for cross-registry queries

### 5. Caching Strategy

**Issue**: No specification for cache invalidation across 27+ TSLs + sectoral registers.

**Considerations**:
- TSL `NextUpdate` field provides update hints
- Sectoral registers may have different update frequencies
- Mobile wallet storage/bandwidth constraints
- Offline operation requirements

**Needed**:
- Recommended caching TTLs per resource type
- Delta update mechanisms
- Priority/criticality indicators for cache refresh

### 6. PSD2 Integration

**Issue**: Missing bridge between ETSI trust infrastructure and EBA PSD2 registers.

**Current State**:
- EBA maintains PSD2 register with ~4,000+ entities
- No linkage to ETSI TSL infrastructure
- Different identifier schemes

**Needed**:
- Mapping between PSD2 authorization numbers and ETSI identifiers
- Integration of PSD2 register into LOTL/TSL hierarchy
- WRPRC entitlement definitions for PSD2 services (AISP, PISP, ASPSP)

---

## Proposed Actions

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Define service type URI for dual-role QTSP-RP entities | ETSI ESI | High |
| 2 | Clarify WRPRC requirements for QTSPs acting as RPs | Registry WG | High |
| 3 | Specify entitlement aggregation rules | Policy WG | Medium |
| 4 | Design cross-registry discovery protocol | Infrastructure WG | Medium |
| 5 | Define caching recommendations | Implementation WG | Medium |
| 6 | Create PSD2-ETSI integration profile | Joint PSD2/ETSI | High |

---

## References

- ETSI TS 119 612 v2.4.1 - Trusted Lists
- ETSI TS 119 411-8 - Access Certificate Policy for EUDI Wallet Relying Parties
- ETSI TS 119 475 - Relying party attributes supporting EUDI Wallet user's authorization decisions
- CIR (EU) 2025/848 - Registration of wallet-relying parties
- EBA PSD2 Register

---

**Document Version**: 1.0  
**Last Updated**: 2025-11-27

