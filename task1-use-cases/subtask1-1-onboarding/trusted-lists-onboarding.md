# Onboarding to the Trusted Lists

## Overview

WEBUILD beneficiaries and Associated Partners may decide to onboard to one or several Trusted Lists that match their Use Case role(s) in the pilot. For the MVP, six Trusted Lists are available for onboarding:

- WEBUILD - QEAA Providers
- WEBUILD - Access Certificate Authorities
- WEBUILD - PID Providers
- WEBUILD - Providers of Registration Certificates
- WEBUILD - PuB-EAA Providers
- WEBUILD - Wallet Providers

Organizations should onboard to the Trusted List(s) that correspond to the role(s) they play in their pilot Use Case(s). An organization participating in multiple roles may need to onboard to more than one Trusted List.

## Where to request onboarding

Onboarding to the Trusted Lists can be requested via the IDunion console:

**[https://console.dev.idunion.info/my-trusted-lists](https://console.dev.idunion.info/my-trusted-lists)**

A step-by-step User Guide is available at:

**[https://docs.dev.idunion.info/docs/user-guide/#onboarding-to-a-trusted-list](https://docs.dev.idunion.info/docs/user-guide/#onboarding-to-a-trusted-list)**

## How onboarding works

There are two ways to onboard to a Trusted List:

1. **Onboarding via invitation** — open the invitation received by e-mail, log in with your EU Business Wallet or register for an account, fill in your organization's data, and continue. A Certificate Signing Request (CSR) is created automatically (or you may upload your own).
2. **Onboarding by request (without invitation)** — go to the [My Trusted Lists console](https://console.dev.idunion.info/my-trusted-lists), search for and select the Trusted List you want to join, click **"Onboard"**, and fill in the required organization data.

In both cases, the data you enter is digitally signed as part of the request (this is not a signature in the legal sense). You will receive a confirmation that your onboarding request is under review, and you will be notified by e-mail once the Ecosystem Authority approves or rejects the request.

See the full [User Guide](https://docs.dev.idunion.info/docs/user-guide/) for detailed steps, including key management options (managed cloud keys, self-created CSR, or client-side HSM on request).

## Additional functionalities available on request

The following can be provided upon request, beyond the standard onboarding flow above:

1. **Additional Trusted Lists** of the types listed above, if necessary for piloting a cross-border scenario.
2. **One or several Trusted Lists for non-qualified EAA Providers.**
3. **Self-managing of a Use Case specific Trusted List.**

To request any of these, contact the WP4 Trust Infrastructure group.

## Related documentation

- [Base Onboarding Framework](../onboarding-base.md) — MVP/MVP+ definitions, Member State requirements, RACI matrix.
- [Trust Infrastructure Schema](../../../task2-trust-framework/trust-infrastructure-schema.md) — registration, notification, and Trusted List publication processes.
- [Trusted List discovery and consumption](../../subtask1-2-trust-registry/trusted-list-discovery-consumption.md) — how to obtain and use the LoTL and Trusted Lists for validation.
