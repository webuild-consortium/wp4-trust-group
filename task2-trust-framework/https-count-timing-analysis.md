This document aims to bring our attention about pratically approaching the eIDAS infrastructure of trust, in particular about the use case where a Wallet Instance has to evaluate the trust with an entity that is both a RP and a QTSP. We must also consider that entity could be, for instance, also a Credential Issuer at the same time, issuing QEAAs (OpenID4VCI) through credential presentations (OpenID4VP).

This issue aims to find and get reactions, comments and different perspectives from the implementers and stakeholder belonging to specific sectors.

## Acronyms

| Acronym | Definition |
|---------|------------|
| EAA | Electronic Attestation of Attributes |
| LOTL | List of Trusted Lists |
| MS | Member State |
| OCSP | Online Certificate Status Protocol |
| CRL | Certificate Revocation List |
| PSD2 | Payment Services Directive 2 |
| QEAA | Qualified Electronic Attestation of Attributes |
| QTSP | Qualified Trust Service Provider |
| RP | Relying Party |
| RPI | Relying Party Intermediary |
| TSL | Trusted Service List |
| WRPAC | Wallet Relying Party Access Certificate |
| WRPRC | Wallet Relying Party Registration Certificate |

## HTTP Requests Analysis for Wallet Instance Trust Evaluation

Based on [wp4-trust-group Policy Discovery Pull Request](https://github.com/webuild-consortium/wp4-trust-group/pull/33), here's the HTTP request count for a wallet evaluating trust for an RP that is also a QTSP.

### Minimum Request Count

This analysis assumes that the wallet instance discovers the related Member State (or sector specific) Trusted List starting from the WRPAC.

| Step | Requests | Description |
|------|----------|-------------|
| 1. LOTL fetch | 1 | List of Trusted Lists hosted by European Commission|
| 2. Member State TSL | 1 | RP's country TSL (access certificate domain lookup) |
| 3. RP WRPAC OCSP/CRL | 1 | Certificate revocation check |
| 4. RP WRPRC validation | 1 | If provided in request is 0 but query National Register is always recommended|
| 5. RPI WRPAC (if any) | +2 | RPI access certificate and revocation status checks (two distinct HTTP requests) |
| **Subtotal** | **4-6** | For single Member State (MS), single register (4 without RPI, 6 with RPI) |

**Latency Estimate**:
| Scenario | Best (250ms/req) | Worst (4s/req) |
|----------|------------------|----------------|
| **Serialized** (4 req, no RPI) | **1s** | **16s** |
| **Serialized** (6 req, with RPI) | **1.5s** | **24s** |
| **Parallelized** (no RPI) | **~0.5s** | **~8s** |
| **Parallelized** (with RPI) | **~0.75s** | **~12s** |

### Worst Case - Full Discovery (27 MS + Sectoral)

This analysis assumes that the wallet instance aims to fetch all the Trusted Lists and Registers for all the Member States and Sectoral Registers, for offline operations and caches.

**Theoretical maximum for full cross-border discovery:**

| Component | Requests | Notes | Best (250ms/req) | Worst (4s/req) |
|-----------|----------|-------|------------------|----------------|
| LOTL | 1 | | 0.25s | 4s |
| MS TSLs | 27 | EU27 Member States | 6.75s | 108s (1.8 min) |
| National WRP Registers | 27 | One per MS, if RP operates cross-border | 6.75s | 108s (1.8 min) |
| Sectoral Registers | ~50-100 | PSD2, Healthcare, etc. PSD2 alone has ~4,000 entities across EU | 12.5-25s | 200-400s (3.3-6.7 min) |
| OCSP/CRL per CA | ~27-50 | Multiple CAs per country, 1+ per TSL | 6.75-12.5s | 108-200s (1.8-3.3 min) |
| WRPRC Provider validation | 1+ | Per WRPRC | - | - |
| **Total (Serialized)** | **~130-200+** | HTTP requests | **32.5-50s** | **~8.7-13.3 min** |

**Latency Estimate (Full Discovery)**:
| Scenario | Best (250ms/req) | Worst (4s/req) |
|----------|------------------|----------------|
| **Serialized** (~130 req, min) | **32.5s** | **~8.7 min** |
| **Serialized** (~200 req, max) | **50s** | **~13.3 min** |
| **Parallelized** (3 sequential phases) | **~0.75s** | **~12s** |

> **Note**: Parallelized assumes 3 sequential phases: (1) LOTL, (2) all TSLs + registers in parallel, (3) all OCSP/CRL in parallel.


### Practical Scenario (RP in 1 MS with PSD2 authorization)

| Request | Count |
|---------|-------|
| LOTL | 1 |
| Home MS TSL | 1 |
| National WRP Register | 1 |
| PSD2/EBA Register | 1 |
| OCSP for WRPAC | 1 |
| WRPRC Provider validation | 1 |
| **Total** | **~6 requests** |

### Triple-Role Entity: QTSP + RP + Credential Issuer

When an entity operates simultaneously as a **QTSP**, **Relying Party**, and **Credential Issuer** (issuing QEAAs via OpenID4VCI through credential presentations via OpenID4VP), the trust evaluation complexity increases significantly.

#### Additional Validation Requirements

| Component | Requests | Description |
|-----------|----------|-------------|
| **RP Validation** | 4-6 | As per standard RP flow (LOTL, TSL, WRPAC, WRPRC) |
| **QTSP Validation** | 2-3 | TSL lookup for QTSP status + certificate chain validation |
| **Credential Issuer Validation** | 2-4 | Issuer metadata, authorization server discovery, signing key validation |
| **Cross-Role Consistency** | 1-2 | Verify entity identifiers match across all three roles |

#### Combined Request Count

| Scenario | Requests | Notes |
|----------|----------|-------|
| **Best Case** (cached, single MS) | 8-12 | Shared TSL/LOTL lookups across roles |
| **Typical Case** | 12-18 | Some cache misses, additional OCSP checks |
| **Worst Case** (no cache, cross-border) | 25-40+ | Full discovery for each role |

#### Latency Estimates for Triple-Role Validation

| Scenario | Best (250ms/req) | Worst (4s/req) |
|----------|------------------|----------------|
| **Serialized** (12 req, typical) | **3s** | **48s** |
| **Serialized** (25 req, worst) | **6.25s** | **100s (~1.7 min)** |
| **Parallelized** (4 phases) | **~1s** | **~16s** |

*Parallelized phases: (1) LOTL, (2) TSLs + Issuer metadata in parallel, (3) OCSP/CRL + authorization discovery, (4) cross-role consistency checks.*