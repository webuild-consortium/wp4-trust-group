# LoTL Producer and Validator

List of Trusted Lists (LoTL) producer and validator for the WP4 Trust Infrastructure. Generates and signs LoTL in XML (XAdES Baseline B) and JSON (JAdES Compact Baseline B) formats per ETSI TS 119 612 and TS 119 602.

**JSON (LoTE) note:** the unsigned JSON from `json_generator.py` follows the ETSI TS 119 602-1 `1960201` JSON schema root shape (see [Task 3 implementation profile](../../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)). Before signing, `produce` validates it with `lote_validate.py` (vendored subset schema in `tools/lotl/schemas/1960201_lote_lotl_subset.schema.json` + semantic checks; optional `LOTE_JSON_SCHEMA` path to the full ETSI `1960201_json_schema.json`).

## Creating a Signing Certificate

The LoTL must be signed with an ETSI-compliant X.509 certificate. Use the provided command to generate a self-signed certificate:

```bash
# Create ETSI-compliant self-signed cert (default: lotl/certs/, Scheme Territory=EU)
python -m tools.lotl.create_signing_cert

# Custom scheme territory and operator name (must match LoTL scheme info)
python -m tools.lotl.create_signing_cert \
  --output-dir lotl/certs/ \
  --scheme-territory IT \
  --scheme-operator-name "Example TLP"

# Custom output filenames
python -m tools.lotl.create_signing_cert -o lotl/certs/ --key-file key.pem --cert-file cert.pem
```

This produces `lotl_signing_key.pem` and `lotl_signing_cert.pem` (or your chosen names) with:
- Subject DN: `C={territory}, O={operator_name}` (per ETSI TS 119 612 clause 5.7.1)
- KeyUsage: digitalSignature, nonRepudiation
- ExtendedKeyUsage: id-tsl-kp-tslSigning (0.4.0.2231.3.0)
- ECDSA P-256 (minimum 3 years usable key per ETSI TS 119 312)

## Configuration: LOTL_SIGNING_KEY and LOTL_SIGNING_CERT

Provide the signing key and certificate either via environment variables or CLI arguments:

**Option 1: Environment variables** (PEM content as string)
```bash
export LOTL_SIGNING_KEY=$(cat lotl/certs/lotl_signing_key.pem)
export LOTL_SIGNING_CERT=$(cat lotl/certs/lotl_signing_cert.pem)
python -m tools.lotl --tl-entries-dir lotl/tl_entries/ --output-dir lotl/
```

**Option 2: File paths** (recommended for local use)
```bash
python -m tools.lotl \
  --signing-key lotl/certs/lotl_signing_key.pem \
  --signing-cert lotl/certs/lotl_signing_cert.pem \
  --tl-entries-dir lotl/tl_entries/ \
  --output-dir lotl/
```

## Usage

```bash
# Produce LoTL (validates tl_entries first, then produces and signs)
python -m tools.lotl --tl-entries-dir lotl/tl_entries/ --output-dir lotl/

# With inline key/cert
python -m tools.lotl --signing-key key.pem --signing-cert cert.pem --tl-entries-dir lotl/tl_entries/ --output-dir lotl/

# Validate-only (for CI, no signing required)
python -m tools.lotl --validate-only --tl-entries-dir lotl/tl_entries/

# Verbose logging
python -m tools.lotl --log-level DEBUG ...
```

Key and certificate can be provided via `--signing-key` / `--signing-cert` or via environment variables `LOTL_SIGNING_KEY` and `LOTL_SIGNING_CERT`.

## Running Tests

```bash
env/bin/pytest tools/lotl/tests/ -v
env/bin/pytest tools/lotl/tests/ --cov=tools.lotl --cov-report=term-missing
```

See [lotl-automation-and-tl-integration.md](../../task4-trust-infrastructure-api/lotl-automation-and-tl-integration.md) for full specification.
