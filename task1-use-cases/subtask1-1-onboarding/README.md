# Subtask 1.1: Onboarding Use Cases

This subtask defines the onboarding use cases for participants in the WP4 Trust Infrastructure.

## Folder contents

- **`README.md`** – Summary of onboarding use case areas in this subtask
- **`trusted-lists-onboarding.md`** – MVP operational guide: how to request onboarding to participant Trusted Lists / LoTEs via the IDunion console (with a registration-path table for RPs vs TL-listed entities)
- **`onboarding-base.md`** – Common onboarding framework (MVP/MVP+, RACI, Member State requirements)
- **`relying_party_onboarding.md`** – UC-01 Relying Party registration (National Register; not TL-listed)
- **`pid_eaa_provider_onboarding.md`** – UC-02 PID / Attestation Provider onboarding
- **`wallet-provider-onboarding.md`** – UC-03 Wallet Provider onboarding
- **`wrpac-wrprc-authority-onboarding.md`** – UC-04 WRPAC/WRPRC Authority onboarding

## Where to register: TL/LoTE vs National Register

| If you are… | Registration guide |
|-------------|-------------------|
| A **Wallet Provider**, **PID/EAA Provider**, **Access CA**, or **Registration Certificate Provider** joining a WE BUILD pilot TL/LoTE | **[Onboarding to the Trusted Lists](trusted-lists-onboarding.md)** |
| A **Relying Party** | **[Relying Party Onboarding](relying_party_onboarding.md)** |
| Looking for normative MVP+ registration, notification, and TL publication rules | **[Trust Infrastructure Schema](../../task2-trust-framework/trust-infrastructure-schema.md#responsibilities-matrix)** |

## Covered onboarding scenarios

### Relying Parties (RPs)
- **RP Registration**: Relying party registration process
- **Policy Acceptance**: RP policy acceptance and agreement
- **Certificate Validation**: RP certificate validation
- **Access Control Setup**: Access control configuration

### PID Providers and Attestation Providers (EAA, QEAA and Pub-EAA Providers)
- **Provider Registration**: PID / Attestation Provider registration process with National Registrar
- **Attestation Type Declaration**: Registration of attestation type(s) to be issued to Wallet Units
- **Access Certificate Issuance**: Access certificate issuance for authentication with Wallet Units
- **Registration Certificate Issuance**: Optional registration certificate issuance containing provider information
- **Trust Anchor Publication**: Trust anchor inclusion in Trusted Lists (for PID Providers, QEAA Providers, and PuB-EAA Providers)
- **Notification to Commission**: Notification to EU Commission and other Member States (for PID Providers and PuB-EAA Providers)

### Wallet Solutions
- **Wallet Providers** – Wallet solutions and providers registration
- **Notification to Commission**: Notification to EU Commission and other Member States
