# LoTL Producer and Validator

List of Trusted Lists (LoTL) producer and validator for the WP4 Trust Infrastructure. Generates and signs LoTL in XML (XAdES Baseline B) and JSON (JAdES Compact Baseline B) formats per ETSI TS 119 612 and TS 119 602.

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
