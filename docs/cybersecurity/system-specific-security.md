# System-Specific Security

Different ITS systems require unique security solutions. This include mechanisms and approaches for secure messaging, platform security (e.g, OBU/RSU), key and certificate management, privilege management (e.g., entitlements), and various other measures that protect backend TMCs and roadside infrastructure.  This section provides building blocks that can be used to choose specific security features and capabilities needed to protect the confidentiality, integrity and availability of ITS systems. 

## Cybersecurity Building Blocks

### Public Key Infrastructure (PKI) Certificates
PKI is a fundamental component of an ITS security architecture, enabling trusted communication between vehicles, roadside infrastructure, and backend systems. A PKI ensures that messages exchanged within an ITS environment are authentic and protected from tampering.

PKI's issue digital certificates, which are used to authenticate the identity of subscribers. Within an ITS system, subscribers may include vehicle OBUs, RSUs, and any other equipment or service that must implement authenticated, integrity protected or confidential communication. Certificates are issued by a trusted infrastrucutre, ending at a Root Certificate Authority (Root CA), and potentially including multiple subordinate CAs. 

PKI also enables encryption, ensuring that sensitive information remains private, and digital signatures, which verify that messages have not been altered. In the ITS domain, PKI systems such as the Security Credential Management System (SCMS) and the Cooperative Credential Management System (CCMS) are also capable of enforcing privilege management, by including specific permissions that a subscriber is authorized to assert, directly within the certificate. Permissions are included in certificate fields such as the Provider Service Identity / Service Specific Permissions (PSIDSSP) fields of an IEEE 1609.2 certificate. These capabilities help maintain trust across ITS networks, supporting applications such as traffic signal priority, collision warnings, and secure data exchanges between transportation systems.

IEEE Std. 1609.2 certificates also provide anonymity protection through the use of short-lived pseudonym certificates that prevent long-term tracking of any particular vehicle.

#### Regional Variations

- **European Union (EU)**  
  The European Telecommunications Standards Institute (ETSI) standards, such as ETSI TS 103 097, complement IEEE Std. 1609.2 by specifying additional certificate formats for V2X communication. In the EU, the PKI is known as the Cooperative Credential Management System (CCMS). 

- **North America**  
  The Security Credential Management System (SCMS) issues and manages IEEE 1609.2 certificates for OBUs, RSUs, and other ITS Stations.

### Misbehavior Detection Systems
Misbehavior detection systems help identify and respond to security threats in ITS networks by monitoring for unusual or suspicious activity. A misbehavior detection system may be integrated directly into a PKI service, such as the SCMS. Misbehavior detection profiles are defined for specific message types (for example, Basic Safety Messages), in order to identify unexpected behavior from a device. When a receiving device detects unusual behavior, the device can flag that behavior by transmiting a misbehavior report to the PKI for review. The PKI can then determine the most appropriate course of action, to include revoking the offending device's certificates, suspending its certifictes, or other approaches. 

### Secure Messaging Protocols and Capabilities
Information exchanged between vehicles, roadside units, Traffic Management Centers (TMCs) and other entities must be authenticated and integrity protected. PKI systems such as the SCMS and CCMS provide the underlying certificates that are used to acheive these security objectives. Security protocols must also be used, along with these certificates. In ITS systems, Transport Layer Security (TLS) is a widely used protocol that provides encryption and secure communication over networks, safeguarding data from eavesdropping and tampering. In the context of ITS, ISO 21177 specifies security services for ITS stations, including secure session establishment and authentication between trusted devices, utilizing protocols like TLS to ensure the authenticity and integrity of information exchanged. 

### Cross Domain Trust
Cross-domain trust is essential for seamless interoperability within ITS systems in order to ensure secure and reliable communication across different jurisdictions and administrative domains. In the U.S., the IEEE 1609.2.2 standard addresses multi-jurisdictional interoperability by defining mechanisms that enable trust between devices using digital certificates issued under different policy domains. A key component of this approach uses the Certificate Trust List (CTL) with entries for trust permissions associated with each trusted Root CA or SCMS. This allows SCMS Managers to granularly establish and manage trust relationships across multiple trusted domains. 

In Europe, the Cooperative Intelligent Transport Systems (C-ITS) employs the European C-ITS Security Credential Management System (EU CCMS) to manage cross-domain trust. This is acheived using the C-ITS Point of Contact (CPOC) protocol, which facilitates the collection of Root CA certificates and their placement onto the European Certificate Trust List (ECTL). The Trust List Manager (TLM) is responsible for issuing the ECTL, ensuring that all participating entities adhere to a unified trust model. 

## Learn More
[SCMS](https://cpoc.jrc.ec.europa.eu/data/documents/EU_CCMS_CPOC_Protocol_Release_1_2.pdf)
[CPOC](https://cpoc.jrc.ec.europa.eu/data/documents/EU_CCMS_CPOC_Protocol_Release_1_2.pdf)
[ISO 21177](https://www.iso.org/standard/87225.html)
[TLS](https://datatracker.ietf.org/doc/html/rfc8446)



