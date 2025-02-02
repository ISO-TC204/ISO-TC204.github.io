# ITS Security Architectures

ITS cybersecurity architectures define how devices, vehicles, communication networks, and backend systems work together to enable secure and reliable operations. These architectures focus on protecting data exchanges, establishing trust between entities, and ensuring systems can operate seamlessly across regions and jurisdictions. They address challenges such as scaling trust frameworks, integrating legacy systems, and adapting to emerging technologies, while supporting the secure deployment and operation of ITS systems. 

---

## Layered ITS Security Architectures

A layered ITS security architecture distributes protection mechanism across each aspect of an ITS system, from physical devices to data exchanges and governance. By addressing security at multiple layers, the architecture provides enhanced protection against threats, ensures trust between entities, and supports secure and interoperable ITS deployments across regions.

### 1. Layered ITS Security

- **Physical Layer:** This layer secures physical infrastructure, protecting devices from physical tampering, damage, and unauthorized local access. Examples of security protections applied at the physical layer may include tamper resistant enclosures for RSUs or secure locations for installation of Traffic Management Center (TMC) servers. 

- **Network Layer:** This layer secures data transmitted across wired and wireless communication channels, including V2X communications. Examples include protocols such as IEEE 1609.2 and ETSI TS 103 097, device authentication mechanisms, transport layer security (TLS 3.0), and protections against denial-of-service attacks. 

- **Data Layer:** This layer secures the confidentiality, integrity and availability of ITS data during storage and processing. Examples include applying message-level authentication, secure data storage, and compliance with privacy regulations. Data layer controls can be used to enable end-to-end authenticated messaging between ITS components. 

- **Application Layer:** This layer protects software and services that interact with ITS components.  Examples include ITS application-layer access controls (e.g., ISO 21177) and secure Application Programming Interfaces (APIs) for system integration and data sharing. 

- **Trust and Identify Layer:** This layer establishes trust within and external to an ITS system. Examples include certificate management frameworks such as the CCMS and SCMS, trust bridges and related mechanisms for extending trust, and permissions and entitlements management for ITS devices and applications. 

- **Governance and Policy Layer:** This layer defines the rules, policies and responsibilities for managing ITS security consistently across a domain. Examples include role-based access control policies, incident response plans, audit processes, and alignment with cybersecurity standards. 

- **Monitoring and Analytics Layer:** This layer provides monitoring and analysis to detect and respond to threats and vulnerabilities within an ITS system. Examples include misbehavior detection systems that help identify compromised ITS equipment. 

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


