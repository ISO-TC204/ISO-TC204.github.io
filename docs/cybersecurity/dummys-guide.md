# What is ITS Cyber Security?

Intelligent Transportation Systems (ITS) enhance mobility and safety through connected and automated technologies. ITS relies on real-time data exchange between vehicles, infrastructure, and cloud-based services to optimize traffic flow and vehicular safety. Connected vehicles use vehicle-to-everything (V2X) communication to safeguard drivers from potential collisions, while roadside units (RSUs) relay important information such as reduced speed limits and signal phase changes. Mobile edge computing (MEC) further enables rapid decision-making by processing data close to the roadway, reducing latency for safety-critical applications. This high level of connectivity and automation makes ITS unique in its reliance on secure and reliable digital communication.

ITS cybersecurity ensures the integrity, confidentiality, and availability of these critical data exchanges and services. It protects against cyber threats that could disrupt traffic management, compromise vehicle control, or manipulate digital traffic regulations. This includes securing communications between vehicles and infrastructure, ensuring that only trusted devices participate in ITS applications, while safeguarding the data that supports these applications. 

Traditional cybersecurity mechanisms such as those that are used to secure Internet technologies lack some of the required capabilities needed to ensure the cybersecurity of ITS systems. 

---

# Why is X.509 and Traditional Internet Security Insufficient for ITS/V2X Systems?

ITS operates in real-time and the integration of the component cyber-physical systems introduces risk with safety-critical impacts. ITS cybersecurity solutions should be tailored to the unique requirements of the transportation domain, specifically the need to operate within a real-time mobile environment, the need to support user privacy and anonymity, and the need to support cross-jurisdictional interoperability, all while operating as scale. 

The following ITS attributes should be considered when choosing a cybersecurity framework such as IEEE Std. 1609.2 or X.509. 

## 1. Real-Time, Safety-Critical Operations
ITS involve real-time interactions that directly affect safety. For example, vehicle-to-Road Side Unit (RSU) communication requires minimal latency so that vehicles can immediately process messages. Any delays that would be introduced through traditional internet security protocols, which are often optimized for less time-sensitive applications, could lead to safety hazards. ITS-specific mechanisms, such as IEEE Std. 1609.2 certificates, are designed to prioritize low-latency communication while maintaining security, making them better suited for safety-critical real-time operations.

## 2. Mobility Requirements
Unlike stationary internet systems, transportation systems operate in highly dynamic environments where devices (e.g., vehicles, pedestrians, RSUs) continuously join and leave networks. IEEE Std. 1609.2 certificates are optimized for use in these dynamic environments, with support for example for short duration lifetimes. Traditional X.509 systems are less equipped to handle frequent certificate updates and revocations required for mobile, decentralized networks.

## 3. Anonymity Requirements
Cybersecurity systems such as the Security Credential Management System (SCMS) issue pseudonym certificates to vehicle OBUs, enabling trusted communication while preserving subscriber anonymity. X.509 certificates have no mechanism for preserving subscriber anonymity. 

## 4. Multi-Entity Trust Management
ITS environments involve a wide range of stakeholders, including vehicles from multiple Original Equipment Manufacturers (OEMs), infrastructure owned by various jurisdictions, and multiple communication providers. Establishing trust across these entities requires specialized structures, such as the Certificate Trust List (CTL) in North America or the European Certificate Trust List (ECTL). These mechanisms enable the extension of trust to differing policy domains and suport the dynamic operation of vehicles with infrastructures owned and managed by differing entities. Generic systems like X.509 lack these built-in cross-trust mechanisms and require substantial planning and processes for trust extension, making them less suited for managing complex ITS trust requirements. 

## 5. Finer-Grained Authorization Control
ITS applications often require more granular access control than X.509 structures can provide. For example, IEEE Std. 1609.2 enables the use of Provider Service Identifiers (PSID)/Service Specific Profiles (SSP) which define a subscribers privileges for specific ITS applications and roles. Assertion of specific PSID/SSP values in an IEEE 1609.2 certificate ensures that only authorized subscribers are able to perform specific actions, such as requesting traffic signal priority or accessing sensitive data. Well-defined PSID/SSP profiles allow an ITS to enforce fine-grained authorization and access control.  

## 6. A Unique Threat Model
ITS faces real-world cyber threats that impact traffic operations and safety. Researchers have shown that they can spoof GPS signals, causing vehicles to misinterpret their location, or hijack roadside units (RSUs) to broadcast false messages, creating congestion or dangerous driving conditions. In past incidents, ransomware attacks on transportation agencies have shut down traffic management centers, preventing operators from monitoring road conditions. Additionally, researchers have demonstrated remote exploits on vehicle-to-everything (V2X) communication, allowing attackers to inject false vehicle attributes into Basic Safety Messages (BSM). These threats require ITS-specific security measures, such as misbehavior detection and certificate-based authentication and privileging, that are not provided via X.509 certificates. 

## 7. Scalability and Certificate Management
The scale of ITS networks includes millions of vehicles, RSUs, and other devices that require efficient certificate issuance, rotation, and revocation processes. SCMS is designed for this scale, enabling seamless management of certificates. X.509-based Public Key Infrastructures (PKI) do not inherently address the scalability and frequency of certificate changes required in ITS.

---

# Choosing between X.509 and IEEE 1609.2 

## X.509 Certificates

X.509 certificates are widely used in traditional Internet security and backend systems. In ITS, they are often used in specific scenarios where compatibility with existing IT infrastructure is required. Scenarios may include security for backend systems or for protection of data at rest in backend databases. 

### Benefits of X.509 Certificates
- Standardized format supported by most cryptographic frameworks.
- Suitable for backend communications, such as securing data exchange between traffic management centers.
- Well-documented lifecycle management, including issuance, renewal, and revocation.

### Limitations in ITS Contexts
- Limited support for mobility and frequent certificate updates.
- Lack of built-in mechanisms for user anonymity and privacy.
- Inefficiencies in real-time, low-latency applications like V2X.

---

## IEEE 1609.2 Certificates

IEEE Std. 1609.2 certificates are specifically designed for V2X environments, addressing the unique challenges of mobility, privacy, and real-time communication. Unlike X.509 certificates, IEEE Std. 1609.2 certificates support:
- Anonymity by issuing pseudonym certificates to vehicle OBUs. 
- Efficient certificate lifetimes for dynamic environments.
- Privilege management through the use of PSID/SSP. 
- Additional built-in access control features through fields such as the Operational Organization Identifier (opOrgId) field. 


### Scenarios Where IEEE 1609.2 is Better Suited than X.509
- On-road communication using Vehicle-to-Infrastructure (V2I) and Vehicle-to-Vehicle (V2V) messaging.
- Safety-Critical Applications that require real-time messaging or support cooperative driving scenarios.
- Dynamic environments through high-frequency certificate updates for mobile vehicle subscribers.

---


### Decision Matrix for Choosing Between X.509 and IEEE 1609.2

This table provides a simplified examination of potential scenarios where either X.509 or IEEE Std. 1609.2 certificates may be more suitable. Readers are encouraged to perform their own in-depth evaluation when designing an ITS cybersecurity architecture. 


| Requirement                      | X.509                  | IEEE 1609.2            |
|----------------------------------|------------------------|------------------------|
| Bandwidth-constrained operations          | ✘                      | ✔                      |
| Low-latency real-time communications |  ✘                   | ✔                     |
| Subscriber anonymity                | ✘                      | ✔                      |
| TMC Operations                                | ✔                      | ✘                      |
| Mobility                            | ✘                      | ✔                      |
| Network V2X-based Applications (e.g., TIMs)   | ✘           | ✔                      | 


---

