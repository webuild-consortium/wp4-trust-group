# Task 7: Testing and Validation
This task focuses on comprehensive testing and validation of the WP4 Trust Infrastructure components and their integration.

## Folder contents

- **`README.md`** – High‑level description of testing and validation responsibilities for WP4

## Scope of Task 7

- **Component and integration testing** – Plan and coordinate tests that validate individual components (Tasks 2–6) and their end‑to‑end integration.
- **Test strategy and tooling** – Define common testing approaches, environments and tools reused across conformance, interoperability and functional tests.
- **Support for deliverables** – Provide evidence and reporting needed for WP4 deliverables related to quality, validation and verification.

## Testing tools
### EUDI Trusted Lists Inspector

EUDI Trusted List Inspector is an open-source tool for testing, validating and debugging EUDI trust infrastructure artifacts.

It can **audit WE BUILD LoTLs and referenced ETSI TS 119 602 LoTE and TS 119 612 Trusted Lists**, inspect XML/JSON/JAdES content, assess certificate chains, signatures, schemas, list pointers and service metadata, and produce machine-readable JSON and human-readable Markdown evidence reports. It also provides dedicated checks supporting the preparation of trust-authority fixtures for wallet testing.

The tool is evidence-oriented and does not claim complete legal or normative ETSI conformance. 

The tool has a Web GUI, OpenAPI documentation, source code is available under Apache2 and is deployed at a stable URL. 

- Deployment: https://trust-inspector.credimi.io/
- Interactive API documentation: https://trust-inspector.credimi.io/docs
- Source repository: https://github.com/ForkbombEu/eudi-trusted-lists-inspector
