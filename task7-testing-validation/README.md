# Task 7: Testing and validation

Task 7 coordinates the testing and validation of the WP4 trust-infrastructure components and their integration with Wallets, Issuers and Verifiers.

## Scope

- **Component and integration testing** — plan and coordinate tests for individual components developed in Tasks 2–6 and for their end-to-end integration.
- **Test strategy and tooling** — define common approaches, environments and reusable tools for functional, interoperability and conformance testing.
- **Participant self-assessment** — give implementers practical tools to inspect their implementations, reproduce failures and collect technical evidence before formal assessment.
- **Support for deliverables** — provide the evidence and reporting needed for WP4 quality, validation and verification activities.

## Self-assessment toolbox

The ForkBomb/Credimi team provides a central assessment platform, [Credimi](https://credimi.io/), together with six focused utilities available from the **Extras** menu. The tools cover Wallets, credential Issuers and Attestation Providers, Verifiers/Relying Parties, and trust and status infrastructure.

| Tool | Intended users | Self-assessment function |
| --- | --- | --- |
| [Credimi](https://credimi.io/) | Wallet, Issuer and Verifier teams | Runs manual and automated conformance and interoperability tests and retains execution evidence. |
| [Wallet Metadata Capture](https://capture-wallet.credimi.io/) | Wallet teams | Exercises a Wallet against a controlled Issuer and Verifier and exposes the protocol values produced by the Wallet. |
| [Issuer/Verifier Metadata Extractor](https://capture-issuer-verifier.credimi.io/) | Issuer, Verifier and Wallet teams | Resolves issuance metadata and extracts presentation-request metadata and DCQL. |
| [EUDI Trust Inspector](https://trust-inspector.credimi.io/) | Trust-list publishers, consumers and auditors | Audits LoTL and Trusted List structures and produces evidence-oriented findings. |
| [TL/LoTE Catalogue and Onboarding](https://lote.credimi.io/) | Trust-list publishers and consumers | Publishes valid and deliberately broken test lists for onboarding and negative testing. |
| [Token Status List Console](https://tsl.credimi.io/) | Issuer, Wallet and Verifier teams | Creates test credentials, changes their status and verifies signed status-list results. |
| [EUDI Trust & Conformance Atlas](https://atlas.credimi.io/) | All ecosystem roles | Maps legal, architectural and technical sources to actor-specific test coverage. |



------------



### Credimi

[Credimi](https://credimi.io/) is the central platform for repeatable conformance and interoperability assessment. Participants register an implementation under test, select the relevant test suites and integrations, and run tests manually or through automated pipelines.

For Wallet automation, reusable [Maestro](https://maestro.mobile.dev/) actions can be adapted to the target Wallet user interface. Pipelines run through a Credimi Runner on a physical device, emulator or simulator and can be triggered from the web interface, scheduled, or integrated with CI.

Current assessment coverage includes:

- the EUDI Wallet Functional Conformance Assessment Framework (FCAF);
- applicable OpenID Foundation conformance tests for OpenID4VC issuance and presentation profiles;
- WE BUILD WP4 tests, including relevant continuity with earlier EWC test material;
- PagoPA Wallet conformance tests for Italian Wallet Issuer and Verifier profiles; and
- project- or partner-specific suites integrated into the same execution and evidence workflow.

A run can produce pass/fail results, step-level outputs, an execution timeline, logs, device-console output, screenshots, video and machine-readable artifacts. Results remain specific to the tested component version, configuration, profile, suite version and execution environment.

- Platform: <https://credimi.io/>
- Documentation: <https://docs.credimi.io/>
- Conformance testing: <https://docs.credimi.io/manual/conformance/>
- Credimi Runner: <https://docs.credimi.io/manual/credimi-runner/>

## Credimi Extras

The Extras are narrow diagnostic and reference tools. They can be used independently while debugging and together with Credimi pipelines when repeatable assessment evidence is required.

### Wallet Metadata Capture

[Wallet Metadata Capture](https://capture-wallet.credimi.io/) provides a controlled fake Issuer and Verifier for observing Wallet behaviour during OpenID4VCI and OpenID4VP flows.

It captures values such as `client_id`, `redirect_uri`, holder-binding proof keys and optional DPoP keys during issuance. During presentation it exposes the request and Wallet response, decrypts the response where applicable, decodes presentations, and checks items such as nonce handling, holder binding and DCQL matching.

- Tool: <https://capture-wallet.credimi.io/>
- API documentation: <https://capture-wallet.credimi.io/docs>
- Source: <https://github.com/ForkbombEu/credimi-capture-wallet>

### Issuer/Verifier Metadata Extractor

[Issuer/Verifier Metadata Extractor](https://capture-issuer-verifier.credimi.io/) resolves the protocol context referenced by credential offers and presentation requests. It helps participants inspect an integration without manually following each protocol URL.

For issuance, it resolves Credential Issuer and Authorization Server metadata. For presentation, it extracts the request metadata and DCQL query from a presentation request or Credimi verification-use-case URL.

- Tool: <https://capture-issuer-verifier.credimi.io/>
- API documentation: <https://capture-issuer-verifier.credimi.io/docs>
- Source: <https://github.com/ForkbombEu/eudi-conformance-evidence>

### EUDI Trust Inspector

[EUDI Trust Inspector](https://trust-inspector.credimi.io/) is an evidence-oriented tool for inspecting EUDI Lists of Trusted Lists and the Trusted Lists they reference. It accepts a list URL or a local XML/JSON document and reports implemented technical checks related to list structure, schemas, signatures, pointers, certificates and service metadata, including checks relevant to ETSI TS 119 602 and ETSI TS 119 612 processing.

The Inspector produces human-readable and machine-readable findings. It does not decide whether a signer is trusted and must not be used as a production trust-decision engine.

- Tool: <https://trust-inspector.credimi.io/>
- API documentation: <https://trust-inspector.credimi.io/docs>
- Source: <https://github.com/ForkbombEu/eudi-trust-inspector>

### TL/LoTE Catalogue and Onboarding

[TL/LoTE Catalogue and Onboarding](https://lote.credimi.io/) supports participants implementing publication, discovery, ingestion, signature handling and actor resolution for EUDI Lists of Trusted Entities and Trusted Lists.

It provides test catalogue entries and signed JSON/JAdES and XML lists, including version and sequence information, signature status and deliberately broken variants for negative testing. Test lists and their signers are not production trust anchors.

- Catalogue: <https://lote.credimi.io/>
- Onboarding: <https://lote.credimi.io/onboarding>
- API documentation: <https://lote.credimi.io/docs>
- Source: <https://github.com/ForkbombEu/eudi-trusted-list-publisher>

For participant onboarding into a WE BUILD Trusted List, see [Onboarding to the Trusted Lists](../task1-use-cases/subtask1-1-onboarding/trusted-lists-onboarding.md).

### Token Status List Console

[Token Status List Console](https://tsl.credimi.io/) is a mock environment for implementing and testing credential-status and revocation handling. Participants can create batches of test credentials, revoke selected entries, retrieve signed status-list tokens and verify credential status end to end.

The service exposes active/revoked states, credential identifiers and indexes, verification results, and signed Status List Tokens. It also supports paired ISO/IEC 18013-5 identifier lists in JWT or CWT form. It is a test utility, not a production status or certification service.

- Tool: <https://tsl.credimi.io/>
- API documentation: <https://tsl.credimi.io/docs>
- Status-list endpoint: <https://tsl.credimi.io/token_status_list/take>

### EUDI Trust & Conformance Atlas

[EUDI Trust & Conformance Atlas](https://atlas.credimi.io/) is a community-maintained map of the sources relevant to EUDI Wallet conformance. Participants can navigate legal acts, implementing regulations, the Architecture and Reference Framework, standards and technical specifications, filter them by ecosystem role, and inspect the tests mapped to those sources.

The Atlas is a navigation and traceability aid. It is not an official interpretation of the underlying legal or normative material; the official sources prevail.

- Tool: <https://atlas.credimi.io/>
- Reference browser: <https://atlas.credimi.io/reference/>
- Test coverage: <https://atlas.credimi.io/tests/>
- Source: <https://github.com/ForkbombEu/eudi-conformance-atlas>

## Recommended self-assessment paths

| Participant or component | Suggested sequence | Evidence produced |
| --- | --- | --- |
| Wallet | Wallet Metadata Capture → Credimi manual interoperability run → conformance pipeline → trust/status negative tests → Atlas traceability check | Observable Wallet behaviour and repeatable run evidence |
| Issuer / Attestation Provider | Issuer Metadata Extractor → Credimi interoperability/conformance run → trust-list onboarding where applicable → status-list tests → Atlas traceability check | Metadata, issuance, trust-registration and revocation evidence |
| Verifier / Relying Party | Verifier/DCQL Extractor → Credimi interoperability/conformance run → Trust Inspector/test lists → status verification → Atlas traceability check | Request, query, trust and credential-status evidence |
| Trust infrastructure | Publish/onboard valid and broken lists → Trust Inspector → integrate checks into Credimi → Atlas traceability check | List-generation, negative-testing and audit evidence |
| Reviewer / assessor | Inspect Credimi run history and artifacts → independently reproduce selected tests → verify source/test mappings in Atlas | Traceable technical evidence supporting formal assessment |

## Using the evidence

- Record the implementation build, configuration, test profile, suite version, execution date and environment with every result.
- Treat black-box success as evidence of observable behaviour; it does not prove unobservable internal controls, secure-development practices or key-management properties.
- Keep test Issuers, Verifiers, credentials, lists and status services isolated from production trust decisions.
- Distinguish conformance, interoperability, trust and certification claims when reporting results.
- Use Credimi run artifacts and the Extras' machine-readable outputs to reproduce failures and compare results after implementation changes.

