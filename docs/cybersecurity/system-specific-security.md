# ITS Cybersecurity Mechanisms and Building Blocks 

ITS cybersecurity architectures are composed of modular security mechanisms that collectively protect communications, devices, and operational processes. This section identifies key building blocks used with an ITS cybersecurity architecture, including cryptographic tools, secure communications protocols and misbehavior detection mechanisms. 

## Digital Certificates

Digital certificates bind a public key to a set of attributes and permissions, enabling authentication, access control, and trust establishment.  Certificates are defined by international standards such as IEEE 1609.2 (predominantly used in North America) and ETSI TS 103 097 (used in Europe). 

### Certificate Types and Purposes

In Europe, ETSI defines a suite of certificates such as Authorization Tickets (ATs) and Enrolment Credentials (ECs) used within the CCMS. In North America, the SCMS uses similar certificate types but with implementation-specific differences.

| Certificate Type              | Purpose                           | Description                                                  | Region        |
| ----------------------------- | --------------------------------- | ------------------------------------------------------------ | ------------- |
| **Root CA Certificate**       | Root of trust                     | Trust anchor for verifying other certificates; manually installed in devices | Global        |
| **Intermediate CA**           | Delegation of signing authority   | Issues certificates to Enrollment and Authorization Authorities | Global        |
| **Enrolment Credential (EC)** | Device identity proof             | Long-term credential proving a device's legitimacy; used to request operational certificates | Europe        |
| **Authorization Ticket (AT)** | Application-level message signing | Short-lived pseudonym certificate used to sign V2X messages (e.g., CAM, DENM, BSM) | Europe (ETSI) |
| **Pseudonym Certificate**     | Equivalent to AT in SCMS          | Privacy-preserving certificate for real-time message signing | North America |
| **Trust List Manager Cert**   | Management of trusted authorities | Used to sign and distribute Certificate Trust Lists (CTLs or ECTLs) |               |

Each certificate includes varying fields depending on its type and role. For example, Authorization Tickets (in ETSI) and pseudonym certificates (in SCMS) include permissions that define which messages a device may sign, and the region in which the certificate is valid. A certificate can be explicit, meaning it includes the full public key, or implicit, where only a reconstruction value is stored and the recipient computes the public key. Implicit certificates are smaller. 

## Misbehavior Detection Systems

Misbehavior detection systems evlauate messages for plausibility, consistency, and alignment with expected behavior. Misbehavior detection operates both locally, within vehicles and roadside units, and centrally, through backend authorities that assess incoming reports and take appropriate action. In North America, the SCMS includes a dedicated Misbehavior Detection and Reporting System designed to identify and manage malicious or faulty behavior in V2X communications. 

#### Local Misbehavior Detection and Reporting

Each ITS Station (ITS-S) integrates a Local Misbehavior Detection Service. This service evaluates incoming V2X messages against a set of detectors to identify inconsistencies or anomalies. When suspicious behavior is detected, it is categorized and forwarded to a Misbehavior Authority (MA). 

#### Backend Processing and Certificate Revocation

Once received, misbehavior reports are processed by the MA. This entity assesses whether the reported behavior warrants certificate revocation, suspension, or other remediation actions. 

