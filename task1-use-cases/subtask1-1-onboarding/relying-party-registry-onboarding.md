# Onboarding a Wallet Relying Party to the Registry

## Overview

WEBUILD beneficiaries and Associated Partners that intend to rely on EUDI Wallets for the provision of digital public or private services onboard as **Wallet Relying Parties (WRPs)** to the pilot Trust Registry. Onboarding registers the organization as a trusted participant and lets it obtain the certificate it needs to authenticate towards Wallet Units.

Onboarding of Wallet Relying Parties is done with the **We Build EUDI Trust Registry Sandbox by Raidiam**. It covers:

- **Trust Establishment** — anchoring participants in a common trust framework so they can be recognized and trusted across the ecosystem.
- **Wallet Relying Party Registration** — registration of consortium members via the registration form.
- **WRPAC Certificate Generation** — the trust registry provides a PKI intermediate CA that is on the WRPAC CA trusted list, and issues the Wallet Relying Party Access Certificates (WRPAC) that prove the organization's identity.
- **Discovery API (`GET /wrp`)** — the trust registry provides a public lookup of registered participants.

Work on the trust infrastructure is ongoing; the current setup enables basic trust establishment so that consortium members can begin piloting.

## Onboarding

- The onboarding instructions are specified in the **[Raidiam WEBUILD EUDI ecosystem documentation](https://www.raidiam.com/developers/docs/raidiam-webuild-eudi-ecosystem-docs)**.
- Onboarding is carried out on the **We Build EUDI Trust Registry Sandbox by Raidiam**, available at **[https://web.sandbox.eudi.raidiam.io/](https://web.sandbox.eudi.raidiam.io/)**.

## How onboarding works

Onboarding is a four-step flow. The key steps are summarised below; follow the linked article for the full instructions.

### 1. Register as a participant

First, provide the details of your organization and role, and request onboarding as a Wallet Relying Party to the registry.

→ Full instructions: [Register as a Participant](https://www.raidiam.com/developers/docs/raidiam-webuild-eudi-ecosystem-docs/register-as-participant/)

### 2. Access your account in the registry

Once your application is provisioned, log in to the **[We Build EUDI Trust Registry Sandbox by Raidiam](https://web.sandbox.eudi.raidiam.io/)** to access your account and manage your organization, application, and certificates in a self-service fashion.

### 3. Request a WRPAC (Wallet Relying Party Access Certificate)

Request the issuance of a WRPAC certificate for your application by completing the CSR process.

→ Full instructions: [Request a WRPAC](https://www.raidiam.com/developers/docs/raidiam-webuild-eudi-ecosystem-docs/request-wrpac/)

### 4. Access the Discovery API (`GET /wrp`)

Registered relying parties are published through the public `GET /wrp` Discovery API, whose response is signed. Use it to look up all relying parties or a specific organization by identifier.

→ Full instructions: [Access the `GET /wrp` API](https://www.raidiam.com/developers/docs/raidiam-webuild-eudi-ecosystem-docs/access-wrp-api/)

## Related documentation

- [Relying Party Onboarding (UC-01)](relying_party_onboarding.md) — the normative onboarding use case (administrative + technical onboarding, Regulation (EU) 2025/848 requirements, data model, RACI).
- [Base Onboarding Framework](onboarding-base.md) — MVP/MVP+ definitions, Member State requirements, terminology.
- [Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md) — registration, notification, and Trusted List publication processes.
- [Trusted List discovery and consumption](../subtask1-2-trust-registry/trusted-list-discovery-consumption.md) — how to obtain and use the LoTL and Trusted Lists for validation.
- [Onboarding API](../../task4-trust-infrastructure-api/onboarding-api/README.md) — the common REST API for registry information.
