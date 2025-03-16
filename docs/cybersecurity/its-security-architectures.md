# ITS Security Architectures

## Overview
A structured security architecture is required for protecting ITS from cyber threats while ensuring interoperability and trust. A layered security approach distributes protections across devices, communications, infrastructure, and policies with the goal of reducing overall risk. In North America, the Architecture Reference for Cooperative and Intelligent Transportation (ARC-IT) provides a framework for integrating security into ITS deployments. ARC-IT incorporates security considerations into ITS architectures by identifying security needs, defining security classes, and aligning with relevant cybersecurity standards.

---


## Layered ITS Security Architectures

A layered ITS security architecture applies protection mechanisms across all aspects of an ITS system, ensuring security is built into devices, communications, infrastructure, and governance. By addressing security at multiple levels, this approach mitigates risks, strengthens trust between entities, and supports secure, interoperable ITS deployments across regions. 

### 1. Layered ITS Security

- **Physical Layer:** The Physical Layer secures ITS hardware against tampering, theft, and unauthorized access by implementing protective measures at the device level. This includes tamper-resistant enclosures for RSUs, securing Traffic Management Centers (TMCs) through controlled access, surveillance, and hardened infrastructure, and hardware security mechanisms that safeguard OBU and/or RSU cryptographic operations. Protection profiles, such as the Vehicle-to-Vehicle (V2V) Communication Security Protection Profile provide security requirements for V2X communication hardware and cryptographic key storage. These are examples of resources that manufacturers and system designers should reference when developing hardware-specific security for ITS components.

- **Network and Transport Layer:** This layer secures data transmission over wired and wireless communication channels, ensuring message integrity, confidentiality, and authentication. IEEE 1609.3 defines network and transport services for Wireless Access in Vehicular Environments (WAVE), supporting reliable data exchange between ITS devices. IEEE 1609.2 and ETSI TS 103 097 provide cryptographic protections for V2X communications, including secure message signing and encryption. Transport Layer Security (TLS 1.3) is commonly used for securing backend communications against interception and tampering. Additional protections, such as device authentication and denial-of-service (DoS) mitigation, help prevent unauthorized access and disruptions to ITS networks.

- **Data Layer:** This layer protects the confidentiality, integrity, and availability of ITS data during storage and processing. Security measures include message-level authentication to ensure the authenticity of data exchanged between ITS components, secure data storage to protect sensitive information from unauthorized access, and privacy-preserving mechanisms such as pseudonym certificates to prevent vehicle tracking. 

- **Application Layer:** The Application Layer protects software and services that interact with ITS components by ensuring secure access, data integrity, and access control. ISO 21177 defines security services for ITS stations, including authentication and secure session management between trusted devices. Secure Application Programming Interfaces (APIs) enable safe system integration and data sharing while enforcing access controls to prevent unauthorized manipulation of ITS applications. Additional security measures, such as code signing and runtime integrity checks, help protect ITS software from tampering or unauthorized modifications.

- **Trust and Identify Layer:** The Trust and Identity Layer establishes and maintains trust within and across ITS systems by enabling secure identity management, authentication, and authorization. Certificate management frameworks, such as the SCMS (Security Credential Management System) in North America and the CCMS (Cooperative Credential Management System) in Europe, provide the foundation for secure V2X communications by issuing and managing digital certificates. Trust bridges facilitate interoperability between different jurisdictions or policy domains, ensuring that ITS devices can securely communicate even when operating under separate certificate authorities. Permissions and entitlements management further enforces security by defining which ITS entities—such as vehicles, RSUs, and backend services—are authorized to perform specific actions, such as requesting signal priority or accessing critical infrastructure systems.

- **Monitoring and Analytics Layer:** The Monitoring and Analytics Layer provides real-time monitoring and analysis to detect and respond to ITS security threats. Misbehavior detection systems can identify compromised or malicious ITS devices by analyzing anomalies in message patterns. For example, misbehavior detection for Basic Safety Messages (BSMs) can identify vehicles broadcasting inconsistent location, speed, or trajectory data, helping to detect GPS spoofing or falsified V2X transmissions. As ITS expands to support additional message types, there is a growing need to develop misbehavior detection profiles for messages beyond BSMs, such as Signal Phase and Timing (SPaT) messages, Roadside Alert messages, and Cooperative Perception messages. 

---

### 2. [Regional Considerations](regional-considerations.md)
Regional considerations in ITS cybersecurity reflect the differing privacy, security, and operational requirements across jurisdictions. These variations impact the design and implementation of ITS systems, especially in areas like trust frameworks, certificate management, and entitlements. Understanding these regional differences is important for achieving compliance with regional regulations and policies.

Key considerations include:

| **Consideration**            | **Description**                                                                                                                                          |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Privacy Requirements**      | - Europe: GDPR requires anonymization and data minimization in ITS systems.                                                                             |
|                               | - North America: Focuses on pseudonymity in V2X communications to protect user identities while enabling traceability for misbehavior detection.         |
| **Security Requirements**     | - SCMS (North America) and CCMS (Europe) may have differing enrollment and cryptographic requirements.                                                      |
|                               | - PSID and SSP entitlements vary based on jurisdictional policies and application needs.                                                                |
| **Interoperability Challenges**| - Regional standards (e.g., ETSI TS 102 940 in Europe, IEEE 1609.2 in North America) require alignment for cross-border V2X communications.             |
|                               | - Trust bridges can be used to connect systems operating under differing security policies or certificate formats.                                                     |
| **Incident Reporting and Audit Practices** | - Incident reporting requirements vary, with some regions requiring real-time reporting to specific authorities.                                                    |
|                               | - Audits may include reviews of certificate management, device configurations, or compliance with standards.                                             |
| **Certification Processes**   | - Certification requirements for ITS devices and applications differ, affecting cryptographic compliance and adherence to trust frameworks.             |
|                               | - Regional differences impact deployment timelines and operational procedures.                                                                          |

---

# Learn More

[Protection Profile V2X Hardware Security Module](https://www.car-2-car.org/fileadmin/documents/Basic_System_Profile/Release_1.3.0/C2CCC_PP_2056_HSM.pdf)

[ETSI TS 103 097](https://www.etsi.org/deliver/etsi_ts/103000_103099/103097/02.01.01_60/ts_103097v020101p.pdf)

[IEEE Std. 1609.2](https://standards.ieee.org/ieee/1609.2/10258/)

[IEEE Std. 1609.3](https://standards.ieee.org/ieee/1609.3/10360/)

