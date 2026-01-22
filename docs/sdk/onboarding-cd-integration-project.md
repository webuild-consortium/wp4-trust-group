# [FEATURE] Implement Automated Compliance Registry with CD Pipeline

The WP4 Trust Infrastructure requires an automated system to evaluate and register the compliance of entities (Wallet Providers, Relying Parties, and PID/Attestation Providers), and to compile and publish List of Trusted Lists (LoTL) and Trusted Lists (TLs) in both XML and JSON formats. Currently, we need an automated mechanism to validate entity information, test against configured platforms, compile trusted lists, and publish them following the ETSI standards and the ARF, as defined in [Task 3](../task3-x509-pki-etsi/).

## Solution Overview

Implement a comprehensive Continuous Deployment (CD) system that:
1. Validates entity registration files against templates and schemas
2. Executes compliance tests against configured test platforms provided by weBuild participants
3. Automatically generates and signs trusted lists according to ETSI TS 119 612 and TS 119 602
4. Publishes entities to appropriate trusted lists upon successful validation
5. Automatically publishes trusted lists to GitHub Pages for public access

## Functional Requirements

### 1. Entity Registration Validation Tool

**Location**: `tools/entity_registration_validator/`

**Structure**:
```
tools/entity_registration_validator/
├── __init__.py
├── cli.py              # CLI entry point using Typer
├── validator.py        # Core validation logic
├── models.py           # Pydantic models for entity schemas
├── schema_validators/  # Schema validators organized by entity type
│   ├── __init__.py
│   ├── base.py         # Base schema validator with common validation logic
│   ├── field_validators.py # Base field-level validators (Pydantic validators)
│   ├── rp_validator.py     # Relying Party schema validator
│   ├── pub_eaa_validator.py # Public EAA Provider schema validator
│   ├── pid_validator.py    # PID Provider schema validator
│   ├── qeaa_validator.py   # Qualified EAA Provider schema validator
│   └── eaa_validator.py    # EAA Provider schema validator
├── README.md           # Tool documentation
└── tests/              # Test suite
    ├── __init__.py
    ├── unit/           # Unit tests
    │   ├── __init__.py
    │   ├── test_validator.py
    │   ├── test_schema_validators/
    │   │   ├── __init__.py
    │   │   ├── test_base.py
    │   │   ├── test_field_validators.py
    │   │   ├── test_rp_validator.py
    │   │   ├── test_pub_eaa_validator.py
    │   │   ├── test_pid_validator.py
    │   │   ├── test_qeaa_validator.py
    │   │   └── test_eaa_validator.py
    │   └── test_models.py
    └── integration/    # Integration tests
        ├── __init__.py
        ├── test_rp_registration.py      # Relying Party registration tests
        ├── test_pub_eaa_registration.py # Public EAA Provider registration tests
        ├── test_pid_registration.py     # PID Provider registration tests
        ├── test_qeaa_registration.py    # Qualified EAA Provider registration tests
        ├── test_eaa_registration.py     # EAA Provider registration tests
        └── fixtures/                    # Test data fixtures
            ├── rp_valid.json
            ├── pub_eaa_valid.json
            ├── pid_valid.json
            ├── qeaa_valid.json
            ├── eaa_valid.json
            └── invalid_examples/
```

**Requirements**:
- Standalone Python package with CLI using **Typer** (recommended) or `argparse` (standard library fallback)
  - **Typer** (external library, requires `pip install typer`) is recommended for modern Python CLI development: type hints support, automatic help generation, better UX
  - **argparse** (standard library, no dependencies) can be used as fallback if minimal dependencies are required or if external libraries are not desired
- **Pydantic** (required, `pip install pydantic`) for schema validation and field validation:
  - Use Pydantic models to define entity schemas with type hints
  - Leverage Pydantic's built-in validation for field-level validation
  - Support JSON Schema generation from Pydantic models
  - Use Pydantic validators for extensible field-level validation (inheritable for future extensions)
- **Schema organization**:
  - Base schema validator (`schema_validators/base.py`) with common validation logic shared across all entity types
  - Entity-specific schema validators: `rp_validator.py`, `pub_eaa_validator.py`, `pid_validator.py`, `qeaa_validator.py`, `eaa_validator.py`
  - Base field validators (`schema_validators/field_validators.py`) with common field-level validation logic
  - Each entity-specific validator inherits from base validator and extends with entity-specific requirements
- Process JSON or YAML files describing entities
- Support entity types: `rp`, `pub-eaa-provider`, `pid-provider`, `qeaa-provider`, `eaa-provider`
- **X.509 Certificate Signing Request (CSR) requirement** (validated by `schema_validators/base.py`):
  - Templates MUST include X.509 CSR for the access certificate only
  - The access certificate MUST comply with specifications defined in [Task 3](../task3-x509-pki-etsi/)
  - Base validator validates CSR format, structure, and compliance with Task 3 requirements
  - **Allowed key types per eIDAS 2.0 (ETSI TS 119 312, ENISA EUCC v.2)**:
    - **RSA**: Minimum 3000 bits (RSA 2048 is legacy, sunset date 31 Dec 2025)
    - **ECDSA**: Supported (curves per ETSI TS 119 312 tables 4, 6, 7)
    - **EdDSA**: Supported (per ETSI TS 119 312)
- **Entity identifier uniqueness requirement**:
  - Entity identifiers MUST be unique across all registered entities
  - If a PR uses an entity identifier that is already validated/published, this indicates an **update** to the existing entity in the published Trusted List
  - Duplicate entity identifier values are NOT allowed - the validator MUST check against existing published entities
  - The workflow MUST detect existing entity identifiers and handle updates accordingly
- Validate against JSON Schema templates (using Pydantic models)
- Templates must differ based on entity type (see [Task 2](../task2-trust-framework/))
- Use Pydantic validators from base or entity-specific validators (inheritable for future extensions)
- All configuration in `settings.py` (no hardcoded constants)
- **Testing**: pytest required, minimum 95% code coverage
  - Unit tests for individual components
  - Integration tests for all entity types (rp, pub-eaa-provider, pid-provider, qeaa-provider, eaa-provider) validating end-to-end registration flow

**CLI Interface**:
```bash
python -m tools.entity_registration_validator.cli --file <path> --entity-type <type> [--schema <schema_path>]
# Or if installed as package:
entity-registration-validator --file <path> --entity-type <type> [--schema <schema_path>]
```

**Output**:
- Validation report (JSON or structured text)
- Exit code: 0 for success, non-zero for validation failures

### 2. Directory Structure

**New Directories**:
- `trusted_lists/` - Root directory for published trusted lists
- `onboarding/` - Directory for entity registration files organized by entity type:
  - `onboarding/rp/` - Relying Party registrations
  - `onboarding/pub-eaa-provider/` - Public EAA Provider registrations
  - `onboarding/pid-provider/` - PID Provider registrations
  - `onboarding/qeaa-provider/` - Qualified EAA Provider registrations
  - `onboarding/eaa-provider/` - EAA Provider registrations

**File Naming Convention**:
- Entity files: `<entity_acronym>_<unique_identifier>.json` or `.yaml`
- Example: `rp_example-corp-12345.json`

### 3. GitHub Workflow for PR Validation

**Location**: `.github/workflows/entity-onboarding-validation.yml`

**Trigger Conditions**:
- Activates on PRs that modify files in `onboarding/` directories
- Detects file additions/modifications in `onboarding/*/` paths

**Workflow Steps**:

1. **File Detection and Entity Identifier Check**:
   - Identify changed files in `onboarding/` directories
   - Extract entity type from directory path
   - Extract entity identifier from filename
   - **Check entity identifier uniqueness**:
     - Query existing published Trusted Lists to check if entity identifier already exists
     - If identifier exists: treat PR as an **update** to existing entity in the Trusted List
     - If identifier is new: treat PR as a **new registration**
     - Reject PR if duplicate identifier found for different entity (same identifier cannot exist for multiple entities)

2. **Template Validation**:
   - Load appropriate JSON Schema template for entity type
   - Validate entity file against schema using JSON Schema validator
   - Report validation errors in PR comments

3. **Field-Level Validation**:
   - For each field in the validated template:
     - Call extensible validation method (inheritable base class)
     - Support custom validators per entity type
     - Collect all validation results

4. **Test Platform Integration**:
   - Read test platform configuration from `.ini` file (e.g., `test_platforms.ini`)
   - **MUST support multiple test platforms** - the `.ini` file can contain multiple platform configurations
   - For each test platform with `enabled = true`:
     - Extract platform endpoint and test parameters from `.ini` file
     - **Registration tokens/API keys MUST be retrieved from environment variables** using the `!ENV:` prefix in the `.ini` file
     - The workflow MUST read `token = !ENV:VARIABLE_NAME` from the `.ini` file and retrieve the value from the corresponding environment variable (populated from GitHub Secrets)
     - Execute compliance tests against the platform
     - Collect test results
   - **All active platforms** (those with `enabled = true`) **MUST be executed** in parallel or sequentially
   - Support multiple non-competing test platforms

5. **Test Report Generation**:
   - Generate comprehensive test report
   - Include validation results, schema validation status, and test platform results
   - Post report as PR comment automatically

6. **Certificate Provisioning** (when registration succeeds):
   - If all validations pass AND all test platforms return success:
     - Generate access certificate and registration certificate for the registered entity (for rp and pid/attestation providers only, excluding wallet providers)
     - Access certificate MUST comply with specifications defined in [Task 3](../task3-x509-pki-etsi/)
     - **MUST publish certificates in clear text within the PR thread** (certificates contain public keys only):
       - Post access certificate and registration certificate as PR comment, since certificates are public information
     - **Private keys for signature operations**:
       - MUST be provided via environment variables
       - MUST be stored in GitHub Secrets
       - Used for signing trusted lists and certificates
     - Mark workflow as successful
     - Add label `ready-for-review` to PR
   - If any validation or test fails:
     - Mark workflow as failed
     - Add label `validation-failed` to PR
     - Block merge until resolved

**Configuration File Format** (`test_platforms.ini`):
```ini
[credimi.io]
enabled = true
endpoint = https://api.credimi.io/test
timeout = 30
token = !ENV:CREDIMI_API_KEY

[platform2]
enabled = true
endpoint = https://platform2.example.com/test
timeout = 30
token = !ENV:PLATFORM2_API_KEY

[platform3]
enabled = false
endpoint = https://platform3.example.com/test
timeout = 30
token = !ENV:PLATFORM3_API_KEY
```

**Security Requirements**:
- **Registration tokens/API keys MUST use `!ENV:` prefix in the `.ini` file** to indicate they must be retrieved from environment variables
- The `token = !ENV:VARIABLE_NAME` format signals that the value MUST be taken from the environment variable `VARIABLE_NAME`
- All authentication tokens/API keys **MUST be stored as GitHub Secrets** and provided to the workflow as environment variables
- GitHub Secret naming convention: `<PLATFORM_ID>_API_KEY` (e.g., `CREDIMI_API_KEY`, `PLATFORM2_API_KEY`)
- The workflow MUST retrieve secrets from GitHub Secrets and provide them as environment variables
- The `.ini` file MUST support multiple platforms, and all platforms with `enabled = true` MUST be executed
- **Private keys for signature operations**:
  - MUST be stored in GitHub Secrets
  - MUST be provided via environment variables to the workflow
  - Used for signing trusted lists, certificates, and other cryptographic operations
  - GitHub Secret naming convention: `TL_SIGNING_PRIVATE_KEY`, `CERT_SIGNING_PRIVATE_KEY`, etc.

**Pilot Integration**:
- Andrea D'Intino and team will integrate with `credimi.io` as the first test platform
- Configuration should support additional non-competing platforms
- Platform integration should be pluggable/extensible

### 4. Trusted List Generation Tools

#### 4.1 Trusted List Producer and Signer

**Location**: `tools/trusted_lists/`

**Structure**:
```
tools/trusted_lists/
├── __init__.py
├── cli.py              # CLI entry point for trusted list producer
├── trusted_list_producer.py # Core trusted list generation logic
├── list_of_trusted_lists_producer.py # List of Trusted Lists generation logic
├── xml_generator.py    # XML format generation (ETSI TS 119 612)
├── json_generator.py   # JSON format generation (ETSI TS 119 602)
├── xades_signer.py     # XAdES signature implementation
├── jades_signer.py     # JAdES signature implementation
├── README.md           # Tool documentation
└── tests/              # Test suite
    ├── __init__.py
    ├── unit/           # Unit tests
    │   ├── __init__.py
    │   ├── test_xml_generator.py
    │   ├── test_json_generator.py
    │   ├── test_xades_signer.py
    │   ├── test_jades_signer.py
    │   └── test_producer.py
    └── integration/    # Integration tests
        ├── __init__.py
        ├── test_rp_trusted_list.py
        ├── test_pub_eaa_trusted_list.py
        ├── test_pid_trusted_list.py
        ├── test_qeaa_trusted_list.py
        ├── test_eaa_trusted_list.py
        └── test_list_of_trusted_lists.py
```

**Requirements**:
- Standalone Python program with CLI
- Generate trusted lists according to ETSI TS 119 612 (XML) and TS 119 602 (JSON/XML) in both formats
- Support entity-specific trusted lists for all entity types (rp, pub-eaa-provider, pid-provider, qeaa-provider, eaa-provider)
- Sign using XAdES Baseline B (XML) and JAdES Compact Baseline B (JSON) per [Task 3](../task3-x509-pki-etsi/)
- **Signature libraries**: `signxml` (XAdES) or `python-xades`; `jwcrypto` (JAdES) or `python-jose`; `cryptography` for certificates

**CLI Interface**:
```bash
# Generate both XML and JSON formats with signatures
python -m tools.trusted_lists.cli --entity-type <type> --output-dir <path> [--sign]
# Or if installed as package:
trusted-list-producer --entity-type <type> --output-dir <path> [--sign]
```

**Testing**: pytest required, minimum 90% code coverage
- Unit tests for XML/JSON generation, signing, schema validation
- Integration tests for all entity types in both formats

**References**: See [`task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md`](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)

#### 4.2 List of Trusted Lists Producer and Signer

**Location**: `tools/trusted_lists/` (same folder as trusted list producer)

**Requirements**:
- Standalone Python program with CLI
- **MUST produce all trusted lists AND the List of Trusted Lists in a single execution**:
  1. Generate all entity-specific trusted lists (rp, pub-eaa-provider, pid-provider, qeaa-provider, eaa-provider) in both XML and JSON formats
  2. Generate List of Trusted Lists (LoTL) referencing all generated trusted lists
  3. All trusted lists must be signed before being referenced in the LoTL
- Sign using XAdES Baseline B (XML) and JAdES Compact Baseline B (JSON) per [Task 3](../task3-x509-pki-etsi/)
- **Signature libraries**: `signxml` (XAdES) or `python-xades`; `jwcrypto` (JAdES) or `python-jose`; `cryptography` for certificates

**CLI Interface**:
```bash
# Generate all trusted lists AND the List of Trusted Lists in a single execution
python -m tools.trusted_lists.cli --all --output-dir <path> [--sign]
# Or if installed as package:
trusted-lists-producer --all --output-dir <path> [--sign]

# Alternative: Generate only List of Trusted Lists (assumes trusted lists already exist)
python -m tools.trusted_lists.cli --list-of-trusted-lists --output-dir <path> [--sign]
```

**Testing**: pytest required, minimum 90% code coverage
- Unit tests for LoTL generation, aggregation logic, signing, schema validation
- Integration tests for complete workflow generating all trusted lists and LoTL in single execution

**References**: See [`task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md`](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md)

### 5. Automated Trusted List Update Workflow

**Location**: `.github/workflows/trusted-lists-update.yml`

**Trigger Conditions**:
- On merge to `main` branch
- On successful entity onboarding PR merge
- Manual trigger via workflow_dispatch

**Workflow Steps**:

1. **Collect Onboarded Entities**:
   - Scan `onboarding/` directories for all valid entity files
   - Group by entity type

2. **Generate All Trusted Lists and List of Trusted Lists**:
   - Execute trusted lists producer with `--all` flag to generate all entity-specific trusted lists (rp, pub-eaa-provider, pid-provider, qeaa-provider, eaa-provider) and LoTL in both XML and JSON formats
   - Output: `trusted_lists/<entity_type>_trusted_list.{xml,json}` and `trusted_lists/list_of_trusted_lists.{xml,json}` (all signed)

3. **Commit and Push** (if changes):
   - Commit generated trusted lists to repository
   - Push to `main` branch
   - Create git tag for version tracking

4. **Publish to GitHub Pages**:
   - Copy all generated trusted lists (XML and JSON) to GitHub Pages directory
   - [OPTIONAL] Set proper MIME types: `application/vnd.etsi.tsl+xml` (XML) or `application/json`/`application/vnd.etsi.lote+json` (JSON)
     - Note: ETSI TS 119 612 requires `application/vnd.etsi.tsl+xml` for XML trusted lists, but GitHub Pages does not support custom MIME type configuration. This is a platform limitation.
   - Update github pages index page with links to all published trusted lists

### 6. Configuration Management

**Location**: `settings.py` (root folder)

**Requirements**:
- Centralized configuration for all tools in `settings.py` (no hardcoded constants)
- Support environment variable overrides
- Configuration sections:
  - Entity type definitions and schemas
  - Test platform configurations
  - Trusted list generation parameters
  - Signing certificate paths and credentials
  - Certificate signing settings (algorithms, key formats supported)
  - Private key storage (GitHub Secrets configuration)
  - ETSI standard URIs and identifiers
  - File paths and directory structures

**Example Structure**:
```python
# Entity types and their schemas
ENTITY_SCHEMAS = {
    'rp': 'schemas/rp_schema.json',
    'pub-eaa-provider': 'schemas/pub_eaa_provider_schema.json',
    'pid-provider': 'schemas/pid_provider_schema.json',
    'qeaa-provider': 'schemas/qeaa_provider_schema.json',
    'eaa-provider': 'schemas/eaa_provider_schema.json',
    # ...
}

# Test platform endpoints (read from test_platforms.ini)
# API keys/tokens MUST be retrieved from GitHub Secrets, not from settings.py
# GitHub Secrets naming: <PLATFORM_ID>_API_KEY
TEST_PLATFORMS_CONFIG_FILE = 'test_platforms.ini'  # Path to platform configuration file

# ETSI URIs
ETSI_LOTE_TYPE_URIS = {
    'pid': 'http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList',
    # ...
}
```

## Acceptance Criteria

- [ ] Entity validation tool validates JSON/YAML files against entity-specific schemas using extensible field-level validation
- [ ] Templates include X.509 CSR for access certificate, validated by base registration validator
- [ ] Access certificate complies with Task 3 specifications
- [ ] Entity identifiers are unique; duplicate identifiers are rejected
- [ ] PRs with existing entity identifiers are treated as updates to published Trusted Lists
- [ ] All tools include unit and integration tests using pytest (minimum 95% code coverage)
- [ ] GitHub workflow triggers on PRs modifying `onboarding/` files, validates schema, executes test platforms, posts results
- [ ] When registration succeeds: certificates generated (for rp and providers only, excluding wallet providers) and published in clear text in PR thread
- [ ] Private keys for signature operations stored in GitHub Secrets and provided via environment variables
- [ ] PR can only be merged when all validations and tests pass
- [ ] Trusted list producer generates signed trusted lists per entity type in both XML (XAdES) and JSON (JAdES) formats
- [ ] List of trusted lists producer generates all trusted lists and signed LoTL in both formats
- [ ] Automated workflow updates trusted lists on PR merge and publishes to GitHub Pages
- [ ] All Python code uses `settings.py` for configuration (no hardcoded constants)
- [ ] Directory structure `trusted_lists/` and `onboarding/` created with proper naming conventions
- [ ] Test platform configuration supports multiple platforms via `.ini` file; all active platforms executed; tokens in GitHub Secrets
- [ ] Integration with credimi.io functional (pilot)

## Component Affected

- [x] [Task 2: Trust Framework](../task2-trust-framework/) (entity templates and requirements)
- [x] [Task 3: X.509 PKI with ETSI alignments](../task3-x509-pki-etsi/) (trusted list generation and signing)
- [x] [Task 4: Trust Infrastructure API](../task4-trust-infrastructure-api/) (onboarding process)
- [x] [Task 7: Testing and Validation](../task7-testing-validation/) (test platform integration)

## Additional Context

### Entity Types

- `rp` (Relying Parties), `pub-eaa-provider` (Public EAA Providers), `pid-provider` (PID Providers), `qeaa-provider` (Qualified EAA Providers), `eaa-provider` (EAA Providers)

### References

- **Task 2**: [`task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md`](../task2-trust-framework/trusted-list-registration-trust-evaluation-matrix.md) - Entity registration requirements
- **Task 3**: [`task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md`](../task3-x509-pki-etsi/etsi_trusted_lists_implementation_profile.md) - Trusted list generation and signing
- **ARF Requirements**: See EUDI Wallet Architecture and Reference Framework Annex 2
- **Implementing Acts**: CIR 2025/848 and related regulations

### Participants

- **Pilot Integration**: Andrea D'Intino and team (credimi.io integration)
- **Interested Participants**: 
  - Christian Klugow
  - (Others to be added)

### Workflow Example

1. Participant creates PR with entity file: `onboarding/rp/example-corp-12345.json` (including X.509 CSR for access certificate)
2. Workflow validates schema, executes field-level validations, calls test platforms
3. If all pass: access certificate and registration certificate generated (for rp and providers only, excluding wallet providers), posted in clear text as PR comment
4. On merge: trusted lists generated and published to GitHub Pages

## Priority

**High**

## Effort Estimation

**Extra Large (2+ weeks)**

## Dependencies

- [Task 2](../task2-trust-framework/) documentation (entity templates and requirements)
- [Task 3](../task3-x509-pki-etsi/) documentation (trusted list generation and signing specifications)
- Test platform API specifications (credimi.io and others)
- ETSI TS 119 612 and TS 119 602 schema files
