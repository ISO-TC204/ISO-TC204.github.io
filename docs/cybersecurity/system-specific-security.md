# System-Specific Security

ITS systems require cybersecurity architectures that are built using fundamental cybersecurity building blocks. These include secure messaging, platform security for OBUs and RSUs, key and certificate management, privilege management (e.g., entitlements), and protections for TMCs and roadside infrastructure. This section outlines core components that can be used to design ITS cybersecurity architectures, ensuring the confidentiality, integrity, and availability of ITS systems.

## Cybersecurity Building Blocks

### Certificate Formats

Digital certificates are a fundamental building block of ITS cybersecurity, ensuring that messages are authenticated, integrity-protected, and, in some cases, encrypted. ITS certificates include domain-specific fields that allow for fine-grained security controls, such as defining permissions for different vehicle types and applications. For example, some certificates may grant a vehicle permission to request signal priority at intersections, while others may only allow participation in general V2X communications. These certificates are optimized for low-latency, real-time messaging in safety-critical environments.

One widely adopted certificate format in ITS is defined by IEEE Std. 1609.2, which specifies a standardized structure for signing, encrypting, and authenticating V2X messages. Designed for ITS applications, these certificates include fields such as Provider Service Identifiers (PSIDs) and Service-Specific Permissions (SSPs) to enable fine-grained access control. For example, PSIDs identify specific ITS services, while SSPs define the permissions granted for a particular application, such as distinguishing between emergency vehicles authorized to request signal priority and standard vehicles that are not. Additionally, 1609.2 supports anonymity protection through short-lived pseudonym certificates, preventing long-term tracking of individual vehicles while still ensuring message authenticity. 


### Public Key Infrastructure (PKI) Systems

PKI provides the trust foundation for secure ITS communication, ensuring that messages between vehicles, roadside units, and backend systems originate from authenticated sources and have not been tampered with. PKIs issue digital certificates that bind a cryptographic key to an entity, such as a vehicle or infrastructure device, enabling secure message signing, encryption, and authentication. A PKI typically consists of a Root Certificate Authority (Root CA) and multiple subordinate CAs that issue certificates to different ITS participants.

PKI systems in ITS do more than authenticate devices—they also enforce privilege management by embedding permissions within certificates. This allows ITS applications to define access levels, such as determining which vehicles can request priority at traffic signals. 

#### Regional Considerations
In North America, the Security Credential Management System (SCMS) implements PKI-based trust for V2X communications, while in Europe, the Cooperative Credential Management System (CCMS) provides a similar framework. 

### Secure Messaging Protocols and Capabilities
PKI systems such as SCMS and CCMS provide the foundation for trust in ITS by issuing digital certificates, but secure communication requires more than just certificates—it also relies on security protocols that enforce authentication, integrity protection, and confidentiality. These protocols ensure that messages exchanged between vehicles, roadside units (RSUs), and Traffic Management Centers (TMCs) remain protected against eavesdropping, modification, or forgery.


### Misbehavior Detection Systems
A custom misbehavior reporting system has been developed for SCMS operations. This allows for the identification of potentially malicious or faulty behavior in V2X messaging. Specific misbehavior detection profiles have been created for messages such as the Basic Safety Message (BSM), where parameters that may be set maliciously can be identified and reported. Additional profiles will be developed over time for other ITS messages. When received, an SCMS makes a determination as to whether or not the misbehaviors should result in revocation of certificates issued to the misbehaving entities.

### Trust Management and Interoperability 
ITS systems must establish trust across different jurisdictions and policy domains to ensure interoperable communication. As vehicles and infrastructure interact across regions, trust management frameworks enable interoperability between systems using digital certificates issued by different authorities. These frameworks define how entities verify the authenticity of messages originating from separate certificate domains while maintaining security. 

In North America, IEEE Std. 1609.2.2 defines mechanisms for multi-jurisdictional interoperability, allowing devices to trust certificates issued under different policy domains. This is accomplished through the Certificate Trust List (CTL), which specifies trust permissions for each recognized Root CA or SCMS. SCMS Managers use these permissions to establish granular trust relationships, ensuring secure and interoperable communication between ITS entities.

In Europe, cross-domain trust is facilitated by the C-ITS Point of Contact (CPOC) protocol, which collects Root CA certificates and integrates them into the European Certificate Trust List (ECTL). The Trust List Manager (TLM) oversees the issuance of the ECTL, ensuring that all participating entities follow a unified and secure trust model for cross-border ITS communications.

---

## Learn More
[SCMS](https://cpoc.jrc.ec.europa.eu/data/documents/EU_CCMS_CPOC_Protocol_Release_1_2.pdf)

[CPOC](https://cpoc.jrc.ec.europa.eu/data/documents/EU_CCMS_CPOC_Protocol_Release_1_2.pdf)

[ISO 21177](https://www.iso.org/standard/87225.html)

[TLS](https://datatracker.ietf.org/doc/html/rfc8446)



