# ITS Cybersecurity Controls

ITS cybersecurity architectures are composed of modular security mechanisms that collectively protect communications, devices, and operational processes. This section identifies key building blocks used with an ITS cybersecurity architecture, including cryptographic tools, secure communications protocols and misbehavior detection mechanisms. 

Strong organizational policies and security procedures are essential to support the technical controls described here. Well-defined processes for key management, certificate policy enforcement, misbehavior handling, and regular compliance audits ensure that the system operates securely over its lifetime.

## Cryptographic Keys

Every ITS station holds at least one pair of keys: a public key and a private key. The public key is shared freely and is included in the device’s certificates. It allows other devices to verify that messages really come from a trusted source. The private key is kept secret inside the device and is used to sign messages or decrypt incoming data when needed.

Keys are generated following secure processes, often during manufacturing or by certified authorities. Once generated, they are stored in secure elements or hardware security modules within the device to prevent theft or tampering. The private key never leaves its secure storage.

When a vehicle sends a V2X message, it signs the message with its private key. Receiving devices use the attached certificate, which includes the public key, to check the signature and confirm that the message has not been altered. This exchange ensures message authenticity and integrity while protecting the sender’s identity when pseudonym certificates are used.

## Identity and Credential Management

### Public Key Infrastructure (PKI)

PKI systems like the SCMS in North America and the CCMS in Europe oversee how certificates are issued, distributed, and verified. Trust Anchor Management ensures that devices rely only on approved root authorities listed on trusted Certificate Trust Lists (CTLs) or Electronic Certificate Trust Lists (ECTLs). These lists define which Root Certificate Authorities are accepted in a given region or deployment.

## Certificate Types and Purposes

Digital certificates bind a public key to a set of attributes and permissions, enabling authentication, access control, and trust establishment.  Certificates are defined by international standards such as IEEE 1609.2 (predominantly used in North America) and ETSI TS 103 097 (used in Europe). 

In Europe, ETSI defines a suite of certificates such as Authorization Tickets (ATs) and Enrolment Credentials (ECs) used within the CCMS. In North America, the SCMS uses similar certificate types but with implementation-specific differences.

| Certificate Type              | Purpose                           | Description                                                  | Region        |
| ----------------------------- | --------------------------------- | ------------------------------------------------------------ | ------------- |
| **Root CA Certificate**       | Root of trust                     | Trust anchor for verifying other certificates; manually installed in devices | Global        |
| **Intermediate CA**           | Delegation of signing authority   | Issues certificates to Enrollment and Authorization Authorities | Global        |
| **Enrolment Credential (EC)** | Device identity proof             | Long-term credential proving a device's legitimacy; used to request operational certificates | Global        |
| **Authorization Ticket (AT)** | Application-level message signing | Short-lived pseudonym certificate used to sign V2X messages (e.g., CAM, DENM, BSM) | Europe (ETSI) |
| **Pseudonym Certificate**     | Equivalent to AT in SCMS          | Privacy-preserving certificate for real-time message signing for any data exchanges between parties with no pre-existing relationship (e,g.., RSU and OBU communications). | North America |
| **Trust List Manager Cert**   | Management of trusted authorities | Used to sign and distribute Certificate Trust Lists (CTLs or ECTLs) | Global        |

### Certificate Policy Enforcement

A strong certificate policy (CP) ensures that each certificate is used only as intended. PKI Operators define certificate policies and practices statements to guide how certificates are requested, used, and renewed. Devices must meet security requirements such as secure key storage and verified firmware. Routine audits check that certificates follow policy rules, and that devices handle keys properly.

### Certificate Revocation 

Sometimes a device’s certificate must be removed from use. This may happen if a device misbehaves, is compromised, or should no longer participate in the system. In many systems, revocation lists (CRLs) are published so that other devices know which certificates to reject. In Europe’s CCMS, short validity periods mean that operational certificates naturally expire, reducing the need for revocation.

### Device Authentication

ITS Devices like vehicles, roadside units, and traffic management servers use certificates to prove their identity when they communicate. This mutual authentication makes sure that only trusted devices exchange messages. Secure elements inside each device protect private keys and ensure that only valid, signed messages are accepted or sent.

### Anonymity and Pseudonymity

To balance trust and privacy, vehicles do not use their permanent identity for routine messages. Instead, a pool of short-term pseudonym certificates is used. These certificates rotate often, and each signed message appears to come from a different identifier. This prevents observers from easily linking messages to a single vehicle. When vehicles send data back to backend servers, they continue using pseudonym certificates to limit tracking.

## Authorization and Entitlement 

Each certificate includes varying fields depending on its type and role. For example, Authorization Tickets (in ETSI) and pseudonym certificates (in SCMS) include permissions that define which messages a device may sign, and the region in which the certificate is valid. A certificate can be explicit, meaning it includes the full public key, or implicit, where only a reconstruction value is stored and the recipient computes the public key. Implicit certificates are smaller. 

### Certificate-based permissions

Certificates may carry specific permissions that define what messages or services a device can access. For ITS, permissions often include Provider Service Identifiers (PSIDs) and Service-Specific Permissions (SSPs) which limit the scope of authorized activities. In Europe, ITS Application Identifiers (ITS-AIDs) serve a similar purpose. These fields ensure that even if a device holds a valid certificate, it can only use it for the purposes allowed by policy.

### Access Control Lists (ACLs)

Access Control Lists help enforce these permissions. Each ITS station checks incoming messages against an ACL to confirm that the sending device is authorized for the requested function. This step happens after verifying the certificate signature and before processing the message content. Proper ACL configuration supports fine-grained control over what actions are permitted within the device or network.

### Interface Security 

Secure interface access ensures that only trusted users or systems can configure or interact with an ITS station. Internal vehicle networks use segmentation to isolate safety-critical functions from non-safety systems, reducing the risk that a compromised subsystem could affect critical controls. Applications on the device must be permissioned correctly to avoid unauthorized data sharing. Firewalls and traffic filters further limit unwanted network connections and detect suspicious traffic patterns.

## Secure Communication Protocols

ITS systems use secure communication standards to protect data as it travels between vehicles and infrastructure. Protocols like TLS and DTLS secure management interfaces and backend connections. V2X messages follow secure message formats defined by standards such as IEEE 1609.2 and ETSI TS 103 097. When IP-based networking is needed, IPsec and VPN tunnels provide additional layers of encryption.

### TLS / DTLS 

TLS and DTLS protect backend communications and configuration interfaces by encrypting data in transit and authenticating endpoints. They help prevent eavesdropping and tampering when devices communicate with management systems or certificate authorities.

### V2X Secure Message Formats

V2X secure message formats ensure that safety and mobility messages are signed and, when needed, encrypted. Standards like IEEE 1609.2 and ETSI TS 103 097 define the structure for signing, certificate attachment, and optional payload encryption. These formats help receivers check authenticity and integrity before acting on data.

### IPsec / VPN tunnels

Internet Protocol Security (IPsec) and Virtual Private Networks (VPNs) provide secure channels for ITS data traveling over public or shared networks. They encapsulate and encrypt packets, offering a layer of confidentiality and integrity beyond standard message signing.

### Secure Time Synchronization 

Accurate time is essential for verifying certificate validity and message timestamps. Secure time synchronization ensures that devices rely on trustworthy time sources, reducing the risk of expired or replayed messages.

## Data In Transit and Data At Rest Encryption 

Sensitive information is encrypted as it moves across networks and when it is stored on a device. End-to-end encryption helps protect backend communications. Selective encryption can protect certain V2X message fields. Data stored locally, such as security logs or credentials, should also be encrypted to prevent exposure if a device is lost or stolen.

### End-to-End Data Encryption

End-to-end encryption applies to connections that pass through multiple systems, such as vehicle-to-cloud communications. This ensures that data stays confidential between the source and final destination, regardless of how many hops or networks it crosses.

### Selective Encryption of V2X Messages

Certain V2X messages or fields may contain sensitive information. Selective encryption protects this data when required. Basic Safety Messages are not encrypted when transmitted. 

### Data at Rest Encryption 

Any data stored on a device, such as security logs, credentials, or operational records, should be encrypted. This prevents unauthorized access if a device is stolen, lost, or physically tampered with.

### Cryptographic Key Management

Key management covers the generation, storage, renewal, and destruction of cryptographic keys throughout their lifecycle. Devices must securely replace keys when certificates are renewed and erase old keys to prevent misuse. Strong key management policies maintain trust and prevent unauthorized operations.

### Integrity Protection

Integrity protection ensures that data remains unaltered from its source to its destination. Digital signatures, hashes, and secure storage checks help detect any tampering or corruption. This is critical for safety messages that must be trusted immediately.

## Misbehavior Detection 

Misbehavior detection systems evaluate messages for plausibility, consistency, and alignment with expected behavior. Misbehavior detection operates both locally, within vehicles and roadside units, and centrally, through backend authorities that assess incoming reports and take appropriate action. In North America, the SCMS includes a dedicated Misbehavior Detection and Reporting System designed to identify and manage malicious or faulty behavior in V2X communications. 

### Local Misbehavior Detection

Each ITS device integrates a Local Misbehavior Detection Service. This service evaluates incoming V2X messages against a set of detectors to identify inconsistencies or anomalies. When suspicious behavior is detected, it is categorized and forwarded to a Misbehavior Authority (MA). 

- plausibility and consistency checks

### Misbehavior Reporting

When a device detects suspicious behavior, it generates a misbehavior report. This report includes evidence such as conflicting message data or implausible values. Reports are sent securely to a centralized misbehavior authority for review and potential follow-up action.

### Misbehavior Processing

Once received, misbehavior reports are processed by the MA. This entity assesses whether the reported behavior warrants certificate revocation, suspension, or other remediation actions. 



## Secure Boot and Firmware Integrity

Devices should use secure boot to confirm that only trusted software runs when starting up. Firmware updates should be signed and verified before installation. Some implementations may also use measured boot or remote attestation to prove to other parties that the device is running genuine software.

### Secure Boot Process

The secure boot process checks each stage of the device’s software against trusted signatures. This prevents unauthorized or tampered code from loading during startup, ensuring that the device runs approved software only.

### Firmware Image Signing

Firmware updates are signed by a trusted authority before release. Devices verify this signature before applying the update, which ensures that only authentic, verified code can be installed.

### Measured Boot and Attestation

Measured boot records the integrity measurements of each boot component and stores these values securely. Remote attestation allows trusted parties, like backend systems, to check these measurements and confirm that the device is running approved software.

## Tamper Protection and Hardware Security

Hardware security modules and secure elements store keys and certificates safely. Devices should be  designed with tamper evidence and resistance features. If tampering is detected, keys can be erased automatically to prevent misuse.

Many PKI requirements lead directly to hardware security needs. For example, to protect private keys and ensure only authorized software runs, devices must include secure elements, hardware security modules, or trusted computing components. These modules provide secure storage for credentials, perform cryptographic operations, and help enforce policies like secure boot and measured boot.

### Hardware Security Modules and Secure Elements

These components provide a secure environment for storing keys and performing sensitive operations like cryptographic signing. They are resistant to many physical attacks and isolate security functions from the general software stack.

### Tamper Evidence and Tamper Resistance

Devices may include physical seals, protective casings, or sensors that detect and record tampering attempts. If tampering is detected, devices can trigger alerts or disable critical functions to protect keys and data.

### Secure Key Storage and Erasure

Keys stored in secure hardware can be deleted automatically if tampering is detected. Routine key rotation and safe deletion prevent old or compromised keys from being reused by attackers.

## Monitoring and Logging

Security logging records important events so operators can detect and investigate problems. Audits and compliance checks should confirm that systems follow security policies over time.

### Security Event Logging

Devices and backend systems record security-relevant events, such as failed login attempts, configuration changes, or unusual message patterns. Logs help operators investigate incidents and ensure accountability.

### Real-Time Intrusion Detection 

Intrusion detection systems watch for signs of malicious behavior or anomalies. Alerts are raised when suspicious patterns are found, enabling quick investigation and response.

### Audit and Compliance Checks

Regular audits verify that devices and systems follow approved security practices. Compliance checks confirm that configurations, certificates, and software versions meet policy requirements.

## Update Patching

Software updates fix vulnerabilities and add new features. Secure update mechanisms authenticate each update package before installation. Over-the-air updates can help keep deployed systems up to date without removing devices from service.

### Authenticated OTA Updates

Over-the-air updates are signed and verified to prevent malicious software installation. This allows operators to deploy security patches and improvements efficiently, keeping the system protected against new threats.

## Physical Security

ITS deployments often include field equipment installed in public places. Physical security measures help protect cabinets, roadside units, and communication links from unauthorized access or damage. Facilities that host backend servers or management systems also follow physical security best practices.

### Secure Deployment

Field installations should follow best practices for mounting, locking, and physically securing equipment. Placement should consider environmental exposure and limit opportunities for unauthorized access.

### Facility Security

Central facilities that host data servers, key management systems, or monitoring tools must follow strict physical access controls. This includes secure entry points, surveillance, and policies that limit who can handle sensitive infrastructure.

## Jurisdictional Controls

ITS systems often cross administrative borders. Cross-jurisdiction trust strategies ensure that vehicles and roadside equipment can exchange trusted messages in different regions. CTLs and ECTLs define which authorities are trusted and for what purposes. Standards like IEEE 1609.2.2 and European policy frameworks guide how this interoperability is maintained.

### Cross Jurisdiction Trusted Interoperability 

When vehicles cross borders or operate under different authorities, trust must be managed carefully. Cross-jurisdiction interoperability uses CTLs, ECTLs, and approaches such as IEEE 1609.2.2 to define which external certificate authorities and permissions are trusted. This ensures that vehicles and infrastructure can exchange valid, secure messages even when managed by different security systems.

## Conclusion

Cybersecurity also depends on trained staff, clear responsibilities, and documented operational procedures that align with the PKI and device security requirements described above.









