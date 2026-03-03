# [DRAFT] Test Compliance CD

Compliance tests against configured platforms. Separate PR from TL automation.

## Scope

- Execute tests against configured test platforms on PR
- `test_platforms.ini`, `!ENV:` for tokens
- Post report as PR comment

## Config

```ini
[credimi.io]
enabled = true
endpoint = https://api.credimi.io/test
token = !ENV:CREDIMI_API_KEY
```

Pilot: @andrea-dintino. Wallet providers only; other registries handle conformance separately.
