# WP4 Trust Group

Public resources shared within the WE BUILD WP4 Trust Infrastructure group

The Trust Registry Infrastructure group is dedicated to establishing the framework for trust evaluation and management within digital wallet ecosystems, in compliance but not limited to the model defined by European regulation (910/2014 as amended by Regulation (EU) 2024/1183).  

The group develops an implementation of the trust model based on a trusted third party (Trusted Lists) resulting in a Trust Framework and an demo infrastructure of trust. 

The group aims to create a comprehensive infrastructure of trust that supports seamless interactions among diverse entities. 

## Contributing

We welcome contributions from all collaborators.

- Open issues for bugs, improvements, or questions
- Submit pull requests following the repository structure
- Use discussions (if enabled) for ideas and proposals

By contributing, you agree to follow the project's coding and documentation guidelines.

## Funding

Co-funded by the European Union

The project is co-funded by the European Union. However, the views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the granting authority. Neither the European Union nor the granting authority can be held responsible.

## Licensing

Licensed to the WE BUILD Consortium under the consortium agreements. The WE BUILD Consortium licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use these files except in compliance with the License.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Tasks

- [ ] **Definition of the Use cases​**
- [ ] **Definition of the Trust Framework​**
- [ ] **X.509 PKI with ETSI alignments​**
- [ ] **Trust Infrastructure API and additional features​**
  - [ ] Trust Infrastructure API
  - [ ] Onboarding API
- [ ] **Participants' Certificates and Policies​**
  - [ ] Data model
  - [ ] Trust evaluation methods
- [ ] **Wallet Instance Conformance/Interop Checks​**
- [ ] **Testing and Validation​**

## Directory Structure

```
wp4-trust-group/
│
├── references/                     # Standards, Drafts, Documentation
│   ├── standards/                  # Official standards and specifications
│   ├── drafts/                     # Draft specifications and working documents
│   ├── reference-specifications/   # Reference implementations and profiles
│   └── overview.md                 # Overview of all references
│
├── task1-use-cases/               # Use cases​
│   ├── subtask1-1-onboarding/     # Use cases​ onboarding
│   └── subtask1-2-trust-registry/ # Use cases​ trust registry
│
├── task2-trust-framework/         # Trust Framework
│
├── task3-x509-pki-etsi/           # X.509 PKI with ETSI alignments
│
├── task4-trust-infrastructure-api/ # Trust Infrastructure API and additional features
│   ├── trust-infrastructure-api/   # Trust Infrastructure API
│   └── onboarding-api/             # Onboarding API
│
├── task5-participants-certificates-policies/ # Participants' Certificates and Policies
│   ├── data-model/                 # Data model
│   └── trust-evaluation-methods/   # Trust evaluation methods
│
├── task6-wallet-conformance-interop/ # Wallet Instance Conformance/Interop Checks
│
├── task7-testing-validation/       # Testing and Validation
│
├── docs/                          # Documentation
│   ├── architecture/              # Architecture documentation
│   ├── api/                       # API documentation
│   ├── standards/                 # Standards compliance documentation
│   └── testing/                   # Testing documentation
│
├── examples/                      # Examples and use cases
│   ├── trust-framework/           # Trust framework examples
│   ├── api-usage/                 # API usage examples
│   └── testing/                   # Testing examples
│
├── tools/                         # Development and validation tools
│   ├── validation/                # Validation tools
│   ├── testing/                   # Testing tools
│   └── deployment/                # Deployment tools
│
├── .github/                       # CI/CD workflows and templates
│   ├── workflows/                 # GitHub Actions workflows
│   ├── ISSUE_TEMPLATE/            # Issue templates
│   └── PULL_REQUEST_TEMPLATE/     # Pull request templates
│
├── README.md                      # This file
└── LICENSE                        # License file
```

## Informative References

### Standards

- **ETSI TS 119 612** (v2.3.1) - Trusted Lists
- **IETF RFC 5914** - Trust Anchor Format
- **IETF RFC 5280** - X.509 PKI

### Drafts

- **ETSI EN 319 412-6** - Certificate profile requirements for PID, Wallet, EAA, QEAA and PSBEAA providers
- **ETSI TS 119 411-8** - Access Certificate Policy for EUDI Wallet Relying Parties
- **ETSI TS 119 475** - Relying party attributes supporting EUDI Wallet user's authorisation decisions (Relying Party Attributes)
- **ETSI TS 119 602** - Electronic Signatures and Trust Infrastructures (ESI); Trusted lists; Data model. Trusted lists in other formats, such as JSON, CBOR or ASN.1.
- **OpenID Federation 1.0** - Draft 41 (December 2024)
- **OpenID Federation Wallet Architectures 1.0** - Draft 03 (October 2024)


### Requirements References

- **ARF Requirements About Trust Infrastructure** - https://github.com/webuild-consortium/wp4-trust-group/issues/1


## Getting Started

1. Clone the repository
2. Review the task directories for specific implementation details
3. Check the references directory for relevant standards and specifications
4. Follow the contributing guidelines for any modifications

## Contact

For questions and discussions, please use the GitHub Issues or Discussions section of this repository.
