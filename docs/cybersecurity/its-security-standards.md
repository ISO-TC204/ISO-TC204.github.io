# Security Standards and Guidance Documents

Use this page to identify standards that support implementation of cybersecurity controls.

## Secure Hardware and Physical Protection

Use these standards to select, evaluate, or require hardware that supports key storage, secure boot, tamper detection, and cryptographic processing. This supports trusted execution and resilience at the component level.

| Standard                                         | Document Type | Description                                                  | Architectural Layer(s) | Stakeholder Role(s)                 |
| ------------------------------------------------ | ------------- | ------------------------------------------------------------ | ---------------------- | ----------------------------------- |
| IEEE 802.3                                       | Standard      | Ethernet standard supporting wired communications among traffic  infrastructure, including support for secure physical connections. | Physical Layer         | Infrastructure Owners and Operators |
| IEEE 802.1X                                      | Standard      | Network access control protocol often used in Ethernet-based ITS backhaul  networks to authenticate RSUs and field devices. | Physical Layer         | Infrastructure Owners and Operators |
| SAE J3101                                        | Standard      | Defines hardware security requirements for ground vehicles, including  secure boot, key storage, and hardware protections against tampering. | Physical Layer         | Vehicle Manufacturers and OEMs      |
| ISO/IEC 19790:2025                               | Standard      | Requirements for cryptographic modules used to protect sensitive data,  applicable to both software and hardware modules. | Physical Layer         | Credential Management Authorities   |
| NIST FIPS 140-3                                  | Standard      | Federal standard for certifying cryptographic modules, used to evaluate  tamper-resistant secure elements. | Physical Layer         | Credential Management Authorities   |
| Trusted Platform Module (TPM) / ISO/IEC  11889   | Standard      | Guidance for secure boot and hardware-based trust anchors in automotive  ECUs. | Physical Layer         | Vehicle Manufacturers and OEMs      |
| Protection Profile V2X Hardware Security  Module | Guidance      | Requirements for HSMs in V2X systems with secure key lifecycle and  resistance to physical attacks. | Physical Layer         | Credential Management Authorities   |
| Vehicle C-ITS station profile                    | Guidance      | Technical and operational requirements for C-ITS vehicle stations in  Europe. | Physical Layer         | Vehicle Manufacturers and OEMs      |
| UNECE R155                                       | Standard      | Regulation that mandates cybersecurity management systems for vehicle  manufacturers, including hardware risk mitigation. | Physical Layer         | Vehicle Manufacturers and OEMs      |

### Network and Transport Security

Apply these standards to enforce confidentiality, integrity, and authentication of data in transit. They define secure sessions for V2X, center-to-field, and backend communications using IP and non-IP protocols.

| Standard           | Document Type | Description                                                  | Architectural Layer | Primary Role(s)                     |
| ------------------ | ------------- | ------------------------------------------------------------ | ------------------- | ----------------------------------- |
| IEEE 1609.3        | Standard      | Defines networking services for WAVE including IPv6 and WSM. | Network Layer       | Infrastructure Owners and Operators |
| ISO 15118          | Standard      | Secure protocols for EV charging with mutual authentication. | Network Layer       | Application and Service Providers   |
| TLS 1.3 (RFC 8446) | Standard      | Modern cryptographic protocol for secure backend communications. | Network Layer       | Infrastructure Owners and Operators |
| DTLS               | Standard      | Datagram version of TLS for UDP-based secure transport.      | Network Layer       | Application and Service Providers   |
| ISO 21217          | Standard      | ITS Station architecture defining network stack.             | Network Layer       | Application and Service Providers   |
| ETSI TS 102 940    | Standard      | Specifies high-level C-ITS security architecture.            | Network Layer       | Credential Management Authorities   |
| ISO 21186-3        | Standard      | Secure data exchange guidelines in C-ITS.                    | Network Layer       | Application and Service Providers   |

### Secure Access

Use these standards to control access across radio, wired, and management interfaces. They help ensure only authorized devices and users can connect to ITS infrastructure and services.

| Standard                                                     | Document Type | Description                                                  | Architectural Layer         | Primary Role(s)                                              |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------ |
| IEEE 802.11p / IEEE 802.11-2016                              | Standard      | Specifies DSRC/WAVE radio communications at 5.9 GHz for vehicular  networking. | Access Layer                | Infrastructure Owners and Operators                          |
| 3GPP LTE-V2X / NR-V2X                                        | Standard      | Specifies cellular V2X radio interfaces for sidelink communication. | Access Layer                | Infrastructure Owners and Operators                          |
| IEEE 802.1X                                                  | Standard      | Network access control protocol used in Ethernet-based ITS backhaul  networks. | Access Layer                | Infrastructure Owners and Operators                          |
| NTCIP / SNMPv3 (RFC 3410)                                    | Standard      | Management protocols with authentication and encryption for ITS field  device communications. | Access Layer                | Infrastructure Owners and Operators                          |
| Standard                                                     | Document Type | Description                                                  | Architectural Layer         | Stakeholder  Roles                                           |
| IEEE 802.3                                                   | Standard      | Ethernet standard supporting wired communications among traffic  infrastructure. | Physical Layer              | Infrastructure Owner Operators, End  Users and Deployers     |
| IEEE Std. 1609.3                                             | Standard      | Defines IPv6, WAVE short message protocol and service advertisement. | Network and Transport Layer | Infrastructure Owner Operators,  Application and Service Providers |
| Vehicle C-ITS station profile                                | Guidance      | Outlines technical and operational requirements for European vehicle ITS  stations. | Physical Layer              | Application and Service Providers                            |
| Protection Profile V2X Hardware Security  Module             | Guidance      | Requirements for HSMs with secure key lifecycle and physical attack  resistance. | Physical Layer              | Credential Management Authorities,  Application and Service Providers |
| SAE J2945/1 On-Board System Requirement  for V2V Safety Communications | Standard      | Security requirements for V2V including key provisioning and secure  storage. | Physical Layer              | Application and Service Providers                            |

### Authenticated Messaging and Data Exchange

These standards define how ITS messages are structured, signed, and validated. They enable cross-vendor and cross-jurisdiction interoperability and ensure message trustworthiness during exchange.

| Standard                             | Document Type | Description                                                  | Architectural Layer | Primary Role(s)                                              |
| ------------------------------------ | ------------- | ------------------------------------------------------------ | ------------------- | ------------------------------------------------------------ |
| SAE J2735                            | Standard      | Defines message formats like BSM, SPaT, MAP.                 | Facilities Layer    | Application and Service Providers                            |
| SAE J2945/x series                   | Standard      | Profiles for message behaviour and signing for V2X.           | Application Layer   | Application and Service Providers                            |
| ETSI EN 302 637-2 / -3               | Standard      | Defines CAM and DENM message formats.                        | Facilities Layer    | Application and Service Providers                            |
| ISO 16460                            | Standard      | Harmonized framework for V2X messages.                       | Facilities Layer    | Standards Development Organizations                          |
| ETSI TS 102 894-2                    | Standard      | Common ITS data dictionary.                                  | Facilities Layer    | Application and Service Providers                            |
| ETSI TS 103 097                      | Standard      | European message authentication and trust validation.        | Facilities Layer    | Credential Management Authorities                            |
| ISO 19091                            | Standard      | Harmonized SPaT/MAP message format  (internationalized SAE). | Facilities Layer    | Application  and Service Providers, End Users and Deployers  |
| ISO/TR 21186-1                       | Standard      | Use cases and profiles for secure data exchange.             | Application Layer   | Application and Service Providers                            |
| ISO/TS 21184 / ISO/TS 21185          | Standard      | Data and communication profiles for trusted ITS exchange.    | Facilities Layer    | Application and Service Providers,  Credential Management Authorities |
| SAE J2945/4 Road Safety Applications | Standard      | Security requirements for RSZW, LCW messages and digital signature  enforcement. | Application Layer   | Application and Service Providers                            |
| SAE J3161/1                          | Standard      | Security for LTE-V2X in light-duty and public safety vehicles. | Application Layer   | Application and Service Providers,  Infrastructure Owner Operators |
| SAE J3161/1B                         | Standard      | Extends J3161/1 to non-light-duty vehicles and motorcycles.  | Application Layer   | Application and Service Providers                            |
| SAE J3161/1C                         | Standard      | Covers school bus-specific V2V security and safety requirements. | Application Layer   | Application and Service Providers                            |
| ISO 19091                            | Standard      | Harmonized SPaT/MAP message format (internationalized SAE)   | Facilities Layer    | Application and Service Providers,  End Users and Deployers  |
|                                      |               |                                                              |                     |                                                              |

### Credential Management and Trust Establishment

Implement these standards to issue, validate, and revoke certificates and to manage permissions. They define how trust anchors and policies are enforced across ITS ecosystems and SCMS/CCMS deployments.

| Standard                                 | Document Type | Description                                           | Architectural Layer         | Primary Role(s)                                              |
| ---------------------------------------- | ------------- | ----------------------------------------------------- | --------------------------- | ------------------------------------------------------------ |
| IEEE 1609.2                              | Standard      | Defines secure message format and certificates.       | Management Layer            | Credential Management Authorities                            |
| IEEE 1609.2.1-2022                       | Standard      | Certificate lifecycle and permissions enforcement.    | Management Layer            | Credential Management Authorities                            |
| ETSI TS 102 941                          | Standard      | Trust and privacy management for C-ITS.               | Management Layer            | Credential Management Authorities                            |
| ETSI EN 319 411-1                        | Standard      | Trust service provider requirements for certs.        | Management Layer            | Cybersecurity Oversight and Policy Bodies                    |
| C-ITS Point of Contact Protocol          | Guidance      | CA cross-certification protocol in Europe.            | Management Layer            | Credential Management Authorities                            |
| ETSI TS 102 941  (Trust List Management) | Standard      | CTL/CRL processes for European PKI trust  frameworks. | Management Layer            | Credential  Management Authorities                           |
| ETSI TS 102 942                          | Standard      | Access control rules and cert-based enforcement.      | Management Layer            | Credential Management Authorities,  Infrastructure Owner Operators |
| ETSI TS 102 943                          | Standard      | Encryption and confidentiality services.              | Management Layer            | Credential Management Authorities                            |
| ETSI TS 103 248                          | Standard      | Pseudonym management and privacy protection in C-ITS. | Network and Transport Layer | Credential Management Authorities,  Application and Service Providers |
|                                          |               |                                                       |                             |                                                              |

### Misbehaviour Detection and Revocation

Use these standards to structure misbehaviour reports, share them across SCMS entities, and apply adjudication processes. They support coordinated response to compromised or malicious actors in the ecosystem.

| Standard                                                     | Document Type | Description                                     | Architectural Layer | Primary Role(s)                                              |
| ------------------------------------------------------------ | ------------- | ----------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| SAE J3287                                                    | Standard      | Standard for V2X misbehaviour reports.           | Management Layer    | Credential Management Authorities                            |
| ETSI TS 102 941-2                                            | Standard      | European misbehaviour reporting procedures.      | Management Layer    | Credential Management Authorities                            |
| ETSI TS 103 759                                              | Standard      | Standardized misbehaviour message format.        | Management Layer    | Credential Management Authorities                            |
| SCMS ASN.1 Misbehaviour Reports                               | Standard      | Misbehaviour report encoding for SCMS.           | Management Layer    | Credential Management Authorities                            |
| SCMS Misbehaviour Application Spec                            | Standard      | SCMS adjudication and report format.            | Management Layer    | Credential Management Authorities                            |
| SCMS Manager: ASN.1  Specification for Misbehaviour Reports   | Standard      | Defines interoperable ASN.1 encoding for  MBRs. | Management Layer    | Credential  Management Authorities, Infrastructure Owner Operators |
| SCMS Manager: Misbehaviour Report and  Application Specification | Standard      | MBR data format and adjudication rules.         | Management Layer    | Credential Management Authorities,  Infrastructure Owner Operators |
| ETSI TR 103 460                                              | Standard      | Survey of misbehaviour detection techniques.     | Management Layer    | Cybersecurity  Oversight and Policy Bodies, Credential Management Authorities |

### Software Integrity and Update Security

Apply these standards to verify firmware and software authenticity, support secure updates, and monitor software state. They enable secure lifecycle management of fielded systems and components.

| Standard                      | Document Type | Description                                                  | Architectural Layer | Primary Role(s)                                              |
| ----------------------------- | ------------- | ------------------------------------------------------------ | ------------------- | ------------------------------------------------------------ |
| ISO 24089                     | Standard      | Post-production update requirements.                         | Application Layer   | Vehicle Manufacturers and OEMs                               |
| UNECE R156                    | Regulation    | Mandates secure update systems for vehicles.                 | Application Layer   | Vehicle Manufacturers and OEMs                               |
| SAE J3101                     | Standard      | Hardware trust anchors and secure boot.                      | Physical Layer      | Vehicle Manufacturers and OEMs                               |
| Trusted Platform Module (TPM) | Standard      | Hardware-based trust and boot integrity.                     | Physical Layer      | Vehicle Manufacturers and OEMs                               |
| ISO/IEC 19790:2025            | Standard      | Cryptographic module security requirements.                  | Physical Layer      | Application  and Service Providers, Cybersecurity Oversight and Policy Bodies |
| ISO/TR 23786                  | Standard      | Security and risk methods for remote access to vehicle systems. | Application Layer   | Infrastructure Owner Operators,  Application and Service Providers |
|                               |               |                                                              |                     |                                                              |

### Incident Management and Operational Oversight

These standards guide incident coordination, event logging, and audit practices. Use them to establish oversight processes that detect, document, and respond to cybersecurity events across stakeholders.

| Standard                         | Document Type | Description                                    | Architectural Layer | Primary Role(s)                     |
| -------------------------------- | ------------- | ---------------------------------------------- | ------------------- | ----------------------------------- |
| ISO 22320                        | Standard      | Incident management processes and protocols.   | Management Layer    | Infrastructure Owners and Operators |
| SAE J3061 / ISO/SAE 21434        | Standard      | Cybersecurity lifecycle and incident response. | Management Layer    | Vehicle Manufacturers and OEMs      |
| NTCIP Secure Profiles (TLS, SSH) | Guidance      | Secure management for center-to-field devices. | Network Layer       | Infrastructure Owners and Operators |
|                                  |               |                                                |                     |                                     |
