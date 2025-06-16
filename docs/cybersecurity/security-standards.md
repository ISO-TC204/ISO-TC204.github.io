# Security Standards and Guidance Documents

Intelligent Transportation Systems (ITS) rely on a layered cybersecurity architecture to ensure safe and trusted operation across vehicles, roadside infrastructure, central management systems, and users. Each layer of this architecture is supported by internationally recognized standards that help protect against cyber threats and maintain system integrity, confidentiality, availability, and trust. The standards shown below are organized according to the key layers of the ITS security architecture:

- Physical Layer
- Access Layer
- Network and Transport Layer
- Facilities Layer
- Application Layer
- Management Layer

---

## Physical Layer

| Standard Standards and Guidance Documents                    | Document Type | Description                                                  |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ |
| IEEE 802.3                                                   | Standard      | Ethernet standard supporting wired communications among traffic infrastructure, including support for secure physical connections. |
| IEEE 802.1X                                                  | Standard      | Network access control protocol often used in Ethernet-based ITS backhaul networks to authenticate RSUs and field devices. |
| SAE J3101                                                    | Standard      | Defines hardware security requirements for ground vehicles, including secure boot, key storage, and hardware protections against tampering. |
| SAE J2945/1 On-Board System Requirement for V2V Safety Communications | Standard      | Specifies foundational requirements for V2V safety applications including secure communications, key provisioning, secure storage, and revocation handling. |
| ISO/IEC 19790:2025                                           | Standard      | Provides requirements for cryptographic modules used to protect sensitive data, applicable to both software and hardware modules. |
| NIST FIPS 140-3                                              | Standard      | U.S. Federal standard for certifying cryptographic modules. Commonly used to evaluate tamper-resistant secure elements in OBUs and RSUs. |
| Trusted Platform Module (TPM) / ISO/IEC 11889                | Standard      | Guidance for secure boot and hardware-based trust anchors in automotive ECUs. |
| [Protection Profile V2X Hardware Security Module](https://www.car-2-car.org/fileadmin/documents/Basic_System_Profile/Release_1.3.0/C2CCC_PP_2056_HSM.pdf) | Guidance      | Outlines the functional and assurance requirements for HSMs used in V2X systems, with focus on secure key lifecycle and resistance to physical attacks. |
| [Vehicle C-ITS station profile](https://www.car-2-car.org/fileadmin/documents/Basic_System_Profile/Release_1.6.3/C2CCC_RS_2037_Profile.pdf) | Guidance      | Outlines the technical and operational requirements for cooperative intelligent transport systems (C-ITS) vehicle stations in Europe, |
| UNECE R155                                                   | Standard      | Regulation that mandates cybersecurity management systems for vehicle manufacturers, including hardware risk mitigation. |

## Access Layer

| Standard                        | Document Type | Description                                                  |
| ------------------------------- | ------------- | ------------------------------------------------------------ |
| IEEE 802.11p / IEEE 802.11-2016 | Standard      | Specifies DSRC/WAVE radio communications at 5.9 GHz for vehicular networking. Enables low-latency broadcast but without link encryption, requiring secure message signing at higher layers. |
| 3GPP LTE-V2X / NR-V2X           | Standard      | Specifies cellular V2X radio interfaces for sidelink communication. Security depends on higher-layer protections using certificates. |
| NTCIP / SNMPv3 (RFC 3410)       | Standard      | Management protocols with authentication and encryption for ITS field device communications. |

## Network and Transport Layer

| Standard                                                     |          | Description                                                  |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| [IEEE Std. 1609.3](https://standards.ieee.org/ieee/1609.3/10360/) | Standard | Defines networking services including IPv6, WAVE short message protocol, and service advertisement for WAVE communications. |
| ISO 15118                                                    | Standard | Provides secure protocols for EV charging including Plug & Charge, with a PKI for mutual authentication and encrypted sessions. |
| TLS 1.3 (RFC 8446)                                           | Standard | Modern cryptographic protocol used to secure communications between ITS backend systems, RSUs, and cloud services. |
| ISO 21186-3                                                  | Standard | Gives guidelines for secure data exchange in C-ITS environments including interface protection and message authenticity. |
| ISO 21177                                                    | Standard | Establishes session security services and trust mechanisms for ITS stations including mutual authentication and session key establishment. |
| ETSI TS 102 940                                              | Standard | Specifies the security architecture of an ITS trust domain and which is used by the European CCMS. |
| ETSI TS 103 248                                              | Standard | Defines privacy and identity protection in C-ITS networks and supports pseudonym management in the transport layer. |
| DTLS                                                         | Standard | Datagram version of TLS for UDP-based secure transport.      |
| ISO 21217                                                    | Standard | ITS Station reference architecture defining the networking stack within ITS stations. |
| ISO 21210 / ETSI EN 302 636-6-1                              | Standard | Profile for IPv6 communication in ITS networks, over GeoNetworking or other media. |
| ETSI EN 302 636-4-1 / -4-2                                   | Standard | GeoNetworking protocols for position-based message forwarding in C-ITS. |
| NTCIP Secure Profiles (TLS, SSH)                             | Guidance | NTCIP profiles updated to endorse secure transport and management of center-to-field device communications. |

## Facilities Layer

| Standard                    | Document Type | Description                                                  |
| --------------------------- | ------------- | ------------------------------------------------------------ |
| ISO/TS 21184 / ISO/TS 21185 | Standard      | Specify global transport data management and comms profiles for trusted device communication. |
| ETSI TS 102 894-2           | Standard      | Defines a common ITS data dictionary across messages.        |
| ISO 19091                   | Standard      | Harmonized SPaT/MAP message format (based on SAE, for international use). |
| ISO 16460                   | Standard      | Harmonized framework for V2X messages across regions.        |
| ETSI EN 302 637-2 / -3      | Standard      | Defines CAM and DENM message formats used in European C-ITS. |

## Application Layer

| Standard                                                     | Document Type | Description                                                  |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ |
| SAE J2735                                                    | Standard      | Defines message formats like BSM, SPaT, MAP used in V2X; foundational for all V2X applications. |
| SAE J2945/x series                                           | Standard      | Profiles message behavior and security use (e.g., signing, permissions) for different V2X applications. |
| ISO/TR 21186-1                                               | Standard      | Describes use cases and application profiles for secure data exchange in cooperative systems, supplementing ISO 21186-3. |
| SAE J2945/4 Road Safety Applications                         | Standard      | Specifies security requirements for road safety messages like RSZW and LCW, including digital signature enforcement via IEEE 1609.2. |
| ISO 24089                                                    | Standard      | Provides post-production software update requirements, including update security and verification mechanisms for ITS applications. |
| UNECE R156                                                   | Regulation    | Mandates secure software update management systems for vehicles, including integrity checks and update logging. |
| SAE J3161/1 Onboard System Requirements for LTE-V2X V2V Safety Communications | Standard      | Defines requirements for LTE-V2X systems in light-duty and public safety vehicles including performance and security aspects. |
| SAE J3161/1B Onboard System Requirements for LTE-V2X V2V Safety Communications by Non-Light-Duty Vehicles and Motorcycles | Standard      | Extends J3161/1 requirements to non-light-duty vehicles and motorcycles, ensuring consistent V2V communication and security. |
| SAE J3161/1C Onboard System Requirements for LTE-V2X V2V Safety Communications by School Buses | Standard      | Covers system requirements and adaptations for V2V communications specific to school buses, including security and safety mandates. |
| ISO/TR 23786                                                 | Standard      | Offers security and risk assessment methods for remote access to automotive systems, especially for diagnostics and updates. |
| ISO 22320                                                    | Standard      | Specifies incident management processes and coordination structures applicable to ITS emergency scenarios. |
| SAE J3061 / ISO/SAE 21434                                    | Standard      | Cybersecurity lifecycle engineering guidelines for automotive systems (development, maintenance, incident response). |

## Management Layer

| Standard                                                     | Document Type | Description                                                  |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ |
| IEEE 1609.2                                                  | Standard      | Defines the format and processing of secure messages and digital certificates in V2X systems including signing and verification mechanisms. |
| IEEE 1609.2.1-2022                                           | Standard      | Specifies certificate lifecycle processes, message permissions, and enrollment protocols for end-entity credential management. |
| C-ITS Point of Contact Protocol                              | Guidance      | Facilitates inter-trust domain communications, including rules for certificate authority cross-certification in Europe. |
| [ETSI TS 103 097](https://www.etsi.org/deliver/etsi_ts/103000_103099/103097/02.01.01_60/ts_103097v020101p.pdf) | Standard      | Specifies secure message formats and certificate structures used in European C-ITS deployments, enabling message authentication and trust validation. |
| ETSI TS 102 940                                              | Standard      | Defines high-level C-ITS security architecture and entities. |
| ETSI TS 102 941                                              | Standard      | Defines trust and privacy management for an ITS trust domain including CA management which is the standard being used for the CCMS. |
| ETSI TS 102 942                                              | Standard      | Access control rules and certificate-based permissions enforcement. |
| ETSI TS 102 943                                              | Standard      | Confidentiality services and guidelines for encrypting C-ITS messages. |
| ETSI EN 319 411-1                                            | Standard      | Defines trust service provider requirements for qualified and non-qualified certificate issuance. |
| NIST FIPS 186-5, SP 800-186                                  | Standard      | Specifications for elliptic curve cryptography used in ITS certificates. |
| SAE J3287                                                    | Standard      | Standardizes formats for V2X misbehavior reports and procedures for detecting and documenting anomalous or malicious behaviors. |
| SCMS Manager: ASN.1 Specification for Misbehavior Reports    | Standard      | Defines ASN.1-based encoding for misbehavior reports to ensure interoperability across trust |
| SCMS Manager: Misbehavior Report and Application Specification | Standard      | Describes data structure and adjudication rules for processing internal and peer-generated misbehavior reports within SCMS. |
| ETSI TS 102 941-2                                            | Standard      | Specifies procedures for misbehavior reporting and detection in C-ITS deployments. |
| ETSI TR 103 460                                              | Standard      | Survey of misbehavior detection techniques; guidance on methods. |
| ETSI TS 103 759                                              | Standard      | Standardized service and message format for reporting misbehavior in European C-ITS. |
| ETSI TS 102 941 (Trust List Management)                      | Standard      | Defines CTL/CRL processes and procedures in EU PKI trust framework. |



