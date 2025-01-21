# What is ITS Cyber Security?

There are security capabilities that have been designed specifically for the ITS ecosystem. These include:

## Security Credential Management System (SCMS)
The SCMS is an instance of a Public Key Infrastructure (PKI) that issues and manages IEEE Std. 1609.2 certificates for OBUs, RSUs, and ITS equipment. The SCMS is able to issue a special type of certificate—known as a pseudonym certificate—that provides anonymity to the certificate’s holder. SCMS issues policies and procedures that govern the practices associated with certificate issuance, lifecycle, and revocation. SCMS is set up to operate at scale and includes mechanisms such as the Certificate Trust List (CTL) that provide for cross-jurisdictional interoperability. IEEE Std. 1609.2 certificates issued by a SCMS are used to secure communications for V2X applications.

## IEEE 1609.2
IEEE Std. 1609.2 is defined as a family of standards for certificates used to authenticate, integrity protect, and optionally encrypt V2X messaging. The certificate format is designed with ITS-specific fields such as PSID/SSP, OpOrgId, and Geolocation. The IEEE 1609.2 standard is optimized for low-latency messaging in real-time, safety-critical operations.

## PSID/SSP
Provider Service Identifiers (PSIDs) allow for the identification of specific ITS applications and services. Service-Specific Permissions (SSPs) define granular permissions and roles for each PSID. These IEEE Std. 1609.2 certificate fields allow for the use of fine-grained access controls in V2X applications. For example, PSIDs may be used to differentiate vehicles that are authorized to assert signal priority vs. vehicles that are not.

## Misbehavior Detection
A custom misbehavior reporting system has been developed for SCMS operations. This allows for the identification of potentially malicious or faulty behavior in V2X messaging. Specific misbehavior detection profiles have been created for messages such as the Basic Safety Message (BSM), where parameters that may be set maliciously can be identified and reported. Additional profiles will be developed over time for other ITS messages. When received, an SCMS makes a determination as to whether or not the misbehaviors should result in revocation of certificates issued to the misbehaving entities.

---

# Why is X.509 and Traditional Internet Security Insufficient for ITS/V2X Systems?

Transportation systems integrate real-time cyber-physical systems with safety-critical impacts. These systems require cybersecurity solutions that are tailored to their unique needs, including support for user privacy and anonymity, multi-jurisdictional trust, and mobility, all at massive scale. The following characteristics of the transportation ecosystem provide reasoning for needing tailored ITS cybersecurity mechanisms.

## 1. Real-Time, Safety-Critical Operations
Transportation systems often involve real-time interactions that directly affect safety. For example, vehicle-to-Road Side Unit (RSU) communication requires minimal latency so that vehicles can immediately process messages. Any delays introduced through traditional internet security protocols, which are often optimized for less time-sensitive applications, could lead to safety hazards. ITS-specific mechanisms, such as IEEE 1609.2, are designed to prioritize low-latency communication while maintaining security, making them better suited for safety-critical real-time operations.

## 2. Mobility Requirements
Unlike stationary internet systems, transportation systems operate in highly dynamic environments where devices (e.g., vehicles, pedestrians, RSUs) continuously join and leave the network. IEEE Std. 1609.2 certificates are optimized for use in these dynamic environments. Traditional X.509 systems are less equipped to handle frequent certificate updates and revocations required for mobile, decentralized networks.

## 3. Anonymity Requirements
ITS uses pseudonym certificates for vehicles, providing secure communication while preserving user privacy.

## 4. Multi-Entity Trust Management
ITS environments involve a wide range of stakeholders, including vehicles from multiple manufacturers, infrastructure owned by various jurisdictions, and multiple communication providers. Establishing trust across these entities requires specialized structures, such as the Certificate Trust List (CTL), and ITS-specific protocols like PSID/SSP profiles. These mechanisms define application-specific permissions and facilitate trust relationships in dynamic, multi-entity environments. Generic systems like X.509 lack these domain-specific capabilities, making them less suited for managing the complex trust requirements of ITS.

## 5. Finer-Grained Authorization Control
ITS applications often require more granular access control than traditional systems can provide. For example, PSID/SSP profiles are used to define specific roles, permissions, and entitlements for ITS applications. These profiles ensure that only authorized entities can perform specific functions, such as controlling traffic signals, sending merge coordination commands, or accessing sensitive data streams. By using PSID/SSP profiles, ITS systems can tailor permissions at the application level, allowing different stakeholders to securely share infrastructure while maintaining distinct operational boundaries. Generic frameworks like X.509 are not designed to accommodate such fine-grained, role-based permissions.

## 6. A Unique Threat Model
Transportation systems face unique threats, such as spoofed traffic signals or falsified vehicle positions. Misbehavior within a cooperative driving scenario, for example, could involve a vehicle transmitting false data to disrupt platooning. ITS-specific security mechanisms, including misbehavior detection and reporting, are designed to address these threats in ways generic internet security cannot.

## 7. Scalability and Certificate Management
The scale of ITS networks—millions of vehicles, RSUs, and other devices—requires efficient certificate issuance, rotation, and revocation processes. SCMS is designed for this scale, enabling seamless management of certificates across diverse ITS networks. Generic systems like X.509 do not inherently address the scalability and frequency of certificate changes required in ITS.

---


# Choosing between X.509 and IEEE 1609.2 

## Where X.509 Certificates Are Appropriate

### Overview of X.509 Usage in ITS
X.509 certificates are widely used in traditional Internet security and backend systems. In ITS, they serve specific roles where compatibility with existing IT infrastructure are required.

### Benefits of X.509 Certificates
- Standardized format supported by most cryptographic frameworks.
- Suitable for backend communications, such as securing data exchange between traffic management centers.
- Well-documented lifecycle management, including issuance, renewal, and revocation.

### Limitations in ITS Contexts
- Limited support for mobility and frequent certificate updates.
- Lack of built-in mechanisms for user anonymity and privacy.
- Inefficiencies in real-time, low-latency applications like V2X.

### Scenarios for X.509 Usage
- Securing backend communication between centralized systems.
- Protecting data at rest in transportation management databases.


---

## IEEE 1609.2 Certificates

### Why IEEE 1609.2 is Better Suited for V2X Communications
IEEE 1609.2 is specifically designed for V2X environments, addressing the unique challenges of mobility, privacy, and real-time communication. Unlike X.509, it supports:
- Anonymity through pseudonym certificates.
- Efficient certificate rotation for dynamic environments.
- Compatibility with SCMS and other ITS-specific infrastructures.

### Key Features of IEEE 1609.2
1. **Support for Anonymity**: Pseudonym certificates ensure privacy without sacrificing security.
2. **Efficient Certificate Lifetimes**: Short-lived certificates reduce the risk of compromise and streamline revocation.
3. **Bootstrap Processes for Entitlements**: Enables secure onboarding of vehicles and devices into the ITS ecosystem.

### Scenarios Where IEEE 1609.2 is Better Suited than X.509
- **On-road Communication**: Vehicle-to-Infrastructure (V2I) and Vehicle-to-Vehicle (V2V) messaging.
- **Safety-Critical Applications**: Real-time alerts and coordination in cooperative driving scenarios.
- **Dynamic Environments**: High-frequency certificate updates for mobile entities.

---


### Decision Matrix for Choosing Between X.509 and IEEE 1609.2
| Requirement                      | X.509                  | IEEE 1609.2            |
|----------------------------------|------------------------|------------------------|
| Real-time Communication          | ✘                      | ✔                      |
| Privacy and Anonymity            | ✘                      | ✔                      |
| Backend Compatibility            | ✔                      | ✘                      |
| Mobility                         | ✘                      | ✔                      |

---


