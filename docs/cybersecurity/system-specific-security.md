# ITS Cybersecurity Controls

ITS cybersecurity architectures are composed of modular security mechanisms that collectively protect communications, devices, and operational processes. This section identifies key building blocks used with an ITS cybersecurity architecture, including cryptographic tools, secure communications protocols and misbehavior detection mechanisms. 

## Identity and Credential Management

Public Key Infrastructure (PKI)

- SCMS/CCMS
- Trust Anchor Management
  - 

## Certificate Types and Purposes

Digital certificates bind a public key to a set of attributes and permissions, enabling authentication, access control, and trust establishment.  Certificates are defined by international standards such as IEEE 1609.2 (predominantly used in North America) and ETSI TS 103 097 (used in Europe). 

In Europe, ETSI defines a suite of certificates such as Authorization Tickets (ATs) and Enrolment Credentials (ECs) used within the CCMS. In North America, the SCMS uses similar certificate types but with implementation-specific differences.

| Certificate Type              | Purpose                           | Description                                                  | Region        |
| ----------------------------- | --------------------------------- | ------------------------------------------------------------ | ------------- |
| **Root CA Certificate**       | Root of trust                     | Trust anchor for verifying other certificates; manually installed in devices | Global        |
| **Intermediate CA**           | Delegation of signing authority   | Issues certificates to Enrollment and Authorization Authorities | Global        |
| **Enrolment Credential (EC)** | Device identity proof             | Long-term credential proving a device's legitimacy; used to request operational certificates | Europe        |
| **Authorization Ticket (AT)** | Application-level message signing | Short-lived pseudonym certificate used to sign V2X messages (e.g., CAM, DENM, BSM) | Europe (ETSI) |
| **Pseudonym Certificate**     | Equivalent to AT in SCMS          | Privacy-preserving certificate for real-time message signing | North America |
| **Trust List Manager Cert**   | Management of trusted authorities | Used to sign and distribute Certificate Trust Lists (CTLs or ECTLs) |               |

### Certificate Policy Enforcement

- Audits
- device security requirements (secure key storage, firmware updates,)
- Certifcate Policy (CP)
- Certificate Practices Statements (CPS) 



### Certificate Revocation 

An outcome of a misbehavior investigation may be to place the offending OBU or RSU's certificate on a CRL. The CRL is ... 







### Device Authentication

- OBU/ RSU/ TMC servers/etc



Mutual authentication 

- 
- Secure elements 



### Anonymity and Pseudonymity



enrollment certificate issued first, then only used to obtain pseudonym certificates.  and then ... short-term pseudonym certificates for v2x communication

vehicles issued pool of short-term pseudonym certificates that rotate frequently.  messages re signed with different pseudonyms to dissuade correlation by eavesdroppers. 



Anonymity for Back-End Data Communications

when vehicles submit misbehavior reports or otherwise communicate with back-end servers, they should use pseudonym certificates to limit the ability of a backend system to link messages to a vehicle identity. 

## Authorization and Entitlement 

Each certificate includes varying fields depending on its type and role. For example, Authorization Tickets (in ETSI) and pseudonym certificates (in SCMS) include permissions that define which messages a device may sign, and the region in which the certificate is valid. A certificate can be explicit, meaning it includes the full public key, or implicit, where only a reconstruction value is stored and the recipient computes the public key. Implicit certificates are smaller. 

### Certificate-based permissions

- PSID/SSP
- ITS-AID
- 

### Access Control Lists (ACLs)

ITS-Station configured with ACLs to verify permissions, after authenticating a message. 



Interface Security 

- Secure interface access
- Intra-vehicle network segmentation
- Application Permissioning
- Network firewalls and traffic filtering





## Secure Communication Protocols

### TLS / DTLS 



### V2X Secure Message Formats



### IPsec / VPN tunnels



### Secure Time Synchronization 









## Data In Transit and Data At Rest Encryption 

### End-to-End Data Encryption





### Selective Encryption of V2X Messages





### Data at Rest Encryption 



### Cryptographic Key Management





### Integrity Protection





## Misbehavior Detection 

Misbehavior detection systems evaluate messages for plausibility, consistency, and alignment with expected behavior. Misbehavior detection operates both locally, within vehicles and roadside units, and centrally, through backend authorities that assess incoming reports and take appropriate action. In North America, the SCMS includes a dedicated Misbehavior Detection and Reporting System designed to identify and manage malicious or faulty behavior in V2X communications. 

### Local Misbehavior Detection

Each ITS device integrates a Local Misbehavior Detection Service. This service evaluates incoming V2X messages against a set of detectors to identify inconsistencies or anomalies. When suspicious behavior is detected, it is categorized and forwarded to a Misbehavior Authority (MA). 

- plausibility and consistency checks

### Misbehavior Reporting





### Misbehavior Processing

Once received, misbehavior reports are processed by the MA. This entity assesses whether the reported behavior warrants certificate revocation, suspension, or other remediation actions. 





## Secure Boot and Firmware Integrity



### Secure Boot Process



### Firmware Image Signing





### Measured Boot and Attestation





## Tamper Protection and Hardware Security

### Hardware Security Modules and Secure Elements



### Tamper Evidence and Tamper Resitance



### Secure Key Storage and Erasure





## Monitoring and Logging

### Security Event Logging

### Real-Time Intrusion Detection 

### Audit and Compliance Checks



## Update Patching

### Authenticated OTA Updates





## Physical Security

### Secure Deployment



### Facility Security





## Jurisdictional Controls



### Cross Jurisdiction Trusted Interoperability 













