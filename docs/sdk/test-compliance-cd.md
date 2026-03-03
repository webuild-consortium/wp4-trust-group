# [DRAFT] Test Compliance CD

Compliance tests against configured platforms. Separate from [TL automation](onboarding-cd-integration-project.md).

## Scope

- PR workflow: schema validation, test platform execution, report as comment
- `test_platforms.ini`, `!ENV:` for tokens
- Cert provisioning on success

## Workflow

Trigger: PRs modifying `onboarding/`

1. File detection, entity id check
2. Template validation
3. Field-level validation
4. **Test platform integration**: execute against enabled platforms
5. Report generation, post to PR
6. Cert provisioning if all pass

## Config

```ini
[credimi.io]
enabled = true
endpoint = https://api.credimi.io/test
token = !ENV:CREDIMI_API_KEY
```

Tokens from GitHub Secrets. Pilot: @andrea-dintino. Wallet providers; other registries handle conformance separately.
