# ITS Security Architectures

This section describes a multi-layered ITS cybersecurity architecture aligned to the ITS-S reference model as described by ISO 21217. Each layer supports specific security capabilities that address risks across applications, communication, and device infrastructure. The architecture below illustrates how these layers combine to support secure and trusted ITS operations.

![Architectural Layers](./images/architecture_layers.jpg)

## Application Layer

The Application Layer is responsible for enabling defined transportation functions, such as signal priority, lane coordination or incident warning. Applications are standardized, certificate-bound services identified by globally or regionally assigned IDs (AAID or PSID) implemented according to strict message structures and access policies. Applications exchange information with other ITS components using standardized message types from standards like SAE J2735 and ETSI EN 302 637-x, and are identified and authorized via Provider Service Identifiers (PSIDs)  /ITS-AIDs and Service-Specific Permissions (SSPs). For example, a transit vehicle’s Onboard Unit (OBU) may have a certificate that includes the PSID for the Signal Request Message (SRM) application and an SSP indicating it is authorized to request transit signal priority at intersections. Permissions should be enforced by both transmitting and receiving ITS-S components. Applications should only initiate communication for services they are explicitly authorized for, and roadside infrastructure (e.g., RSUs) must validate both PSID and SSP on incoming messages.

In addition to certificate-based permissions, many ITS applications operate under local or regional policies configured by ITS Station Operators (SO) that define where, when, and by whom an application may be used. These rules complement certificate-bound permissions and are defined through deployment policy frameworks implemented by jurisdictions, infrastructure owners, or certificate authorities. Polices may be enforced at multiple points in a system and may be implemented through mechanisms such as geofencing, SSP-encoding, infrastructure logic, and credential life-cycle controls. These mechanisms ensure that applications are not only cryptographically authorized, but also contextually constrained to operate within their intended scope.

### Threats to the Application Layer

The table below outlines example threats relevant to this layer.

| Threat Example                              | Security Objectives                                          |
| ------------------------------------------- | ------------------------------------------------------------ |
| Unauthorized access to service functions    | Ensure only authenticated and authorized applications are executed |
| Malicious or unauthorized application code  | Enforce code integrity and secure update processes           |
| Cross-application data leakage              | Isolate applications and enforce secure inter-process communication |
| Exposure of user or operational data        | Apply privacy rules and enforce user consent                 |
| Unauthorized message injection              | A non-authorized OBU transmits Signal Request Messages (SRMs) to manipulate traffic signals. |
| Role escalation                             | A vehicle with general-use permissions reuses or fabricates SSP fields to impersonate an emergency responder. |
| Tampered application logic                  | Malware or modified code causes an ITS device to transmit false warnings or suppress valid messages. |
| Improper deployment (jurisdictions)         | A certified application is installed outside its permitted geographic zone or agency scope. |
| Unauthorized third-party software execution | A device runs unapproved or unsigned applications due to weak software controls or side-loading. |

### Cybersecurity Objectives

The following objectives describe the intended cybersecurity outcomes for this layer and support the mitigation of the threats identified above.

- Restrict application use to authorized roles, based on device certificates and SSP constraints

- Prevent unauthorized message injection or misuse of safety-critical applications
- Ensure software integrity through code signing and runtime validation
- Protect applications from unauthorized modification or execution of unapproved third-party code
- Enforce deployment-specific constraints such as geofencing, jurisdictional scope, and time-based usage

## Facilities Layer

The Facilities layer provides support services for message handling, data management, and inter-application coordination. Security measures here focus on privacy and controlled exposure of message content and services.

### Threats to the Facilities Layer

The table below outlines example threats relevant to this layer.

| Threat Example | Security Objectives                                          |
| -------------- | ------------------------------------------------------------ |
| Message replay | Replay attacks shift time context to mislead behavior        |
| API misuse     | Untrusted entities exploit facility-layer APIs to access or influence protected data |
| Tracking       | Overcollection or linking of contextual data enables re-identification of pseudonymous users |

#### Cybersecurity Objectives

The following objectives describe the intended cybersecurity outcomes for this layer and support the mitigation of the threats identified above.

- Preserve user anonymity and reduce data traceability
- Validate message origin, freshness, and plausibility
- Provide access-controlled APIs for data exchange

### Network and Transport

The Network and Transport Layer secures the communication channels that carry ITS and V2X data across both wireless and wired infrastructures. This includes direct V2X communications between vehicles and RSUs, as well as data exchanged between field devices and backend systems. The primary cybersecurity function of this layer is to ensure that data in transit is protected against tampering, interception, and unauthorized injection, while also enforcing device authentication and maintaining service availability under a variety of environmental and adversarial conditions.

Standards such as IEEE 1609.3 define network and transport protocols for Wireless Access in Vehicular Environments (WAVE), while IEEE 1609.2, IEEE 1609.2.1, and ETSI TS 103 097 provide cryptographic protections, including digital signatures and encryption for V2X messages. Backend communications are typically secured using TLS 1.3 with mutual authentication to protect sensitive data flows between RSUs, TMCs, and service providers.

All V2X messages must be digitally signed to ensure authenticity and integrity. Secure message headers defined by IEEE 1609.2.1 and ETSI TS 103 097 include fields for certificate linkage, timestamps, and replay protection. Devices that cannot validate message signatures must discard the message and may report verification failures to backend systems for further analysis.

While most V2X safety messages are signed but not encrypted, some sensitive data exchanges, such as traveler personalized information or backend configuration files do require encryption. In these cases, protocols such as TLS 1.3 are used to secure communications and ensure confidentiality. 

Pseudonymity protections are also enforced at this layer to prevent persistent tracking of vehicles and infrastructure. Rather than transmitting static identities, devices are issued short-term, unlinkable pseudonym certificates that are rotated regularly. This prevents passive observers from correlating message patterns or locations to reconstruct vehicle trajectories, profile driver behavior, or infer organizational operations. Without effective pseudonym rotation, even properly signed messages could expose operational privacy risks.

### Threats to Network and Transport Layer

The table below outlines example threats relevant to this layer.

| Threat Example                        | Security Objectives                                          |
| ------------------------------------- | ------------------------------------------------------------ |
| Message interception or modification  | Authenticate and encrypt transmitted data                    |
| Replay of valid but outdated messages | Enforce message expiration and sequence validation           |
| Geographic misuse of services         | Apply geographic scope controls to message origin and forwarding |
| Flooding or DoS attacks               | Implement rate limiting, prioritization, and load protections |
| Message injection                     | Attackers send spoofed or malformed messages.                |
| Eavesdropping                         | Passive attackers intercept V2X or backend messages to obtain sensitive information or gain situational awareness. |
| Man-in-the-middle (MITM)              | An attacker inserts themselves between devices to relay or modify communications while impersonating trusted parties. |
| Denial-of-Service (DoS)               | Flooding of wireless or wired interfaces disrupts availability of critical ITS messages. |
| Certificate spoofing                  | Attackers present forged credentials or reuse compromised certificates to authenticate malicious devices. |
| Vehicle tracking                      | Passive observers collect and correlate V2X messages (e.g., BSMs) to track vehicles over time or infer personal behaviors. |

### Cybersecurity Objectives

The following objectives describe the intended cybersecurity outcomes for this layer and support the mitigation of the threats identified above.

- Assure message integrity and authenticity using cryptographic signatures
- Protect confidentiality of sensitive data in transit (e.g., Basic Safety Message (BSMs), certificate requests)
- Authenticate devices and services to prevent spoofing or impersonation
- Prevent unauthorized message injection or modification
- Maintain availability of communication channels

## Access Layer

The Access Layer encompasses the physical and logical interfaces that support communication between ITS devices and external networks. This includes radio interfaces such as V2X as well as wired interfaces such as Ethernet. This layer serves as the point of ingress and egress for V2X messages and operational data, and plays an important role in enforcing message timing, interface-level authentication, and protection against unauthorized access.

Security at the Access Layer is concerned with ensuring that messages originate from trusted hardware components, that unauthorized interfaces are not used to inject or modify data, and that time synchronization is accurate and protected from spoofing or degradation. Compromise at this layer may undermine higher-layer security controls by allowing adversaries to manipulate traffic before cryptographic protections are applied. 

### Threats to the Access Layer

The table below outlines example threats relevant to this layer.

| Threat Example                     | Security Objectives                                          |
| ---------------------------------- | ------------------------------------------------------------ |
| Interface spoofing or hijacking    | Bind device identity to specific hardware interfaces         |
| Degraded timing or synchronization | Validate time source integrity and enforce bounds            |
| Link-layer injection or jamming    | Protect wireless protocols and use hardened media access control |

#### Cybersecurity Objectives

The following objectives describe the intended cybersecurity outcomes for this layer and support the mitigation of the threats identified above.

- Authenticate hardware interfaces and prevent spoofing
- Protect link-layer integrity and timing synchronization
- Prevent unauthorized wireless or physical interface use



## Management Layer

The Management Layer provides the foundation for trust, governance, and policy enforcement across all layers of an ITS security architecture. It encompasses the systems, policies, and controls that establish and maintain trust relationships between devices, infrastructure, and backend services. This layer is responsible for managing cryptographic credentials, coordinating enrollment and authorization processes, and enabling consistent decision-making across administrative domains.

This layer also supports real-time detection and response mechanisms that identify and remediate malicious or anomalous behavior. These include mechanisms for evaluating message content, tracking behavioral consistency, and executing revocation or suspension workflows. 

Key cybersecurity objectives for this layer include establishing a root of trust, controlling enrollment into certificate management systems, enforcing lifecycle rules for certificate issuance and revocation, validating compliance with technical standards, supporting scalable governance structures such as Electors or CPAs, and enabling real-time misbehavior detection and response. These objectives are addressed through a combination of policy-based enforcement, cryptographic controls, behavioral analytics, and coordinated trust administration.

In distributed systems like SCMS, trust is managed by Electors. They sign a multi-party Certificate Trust List (CTL) to prevent unilateral changes. In CCMS, trust is coordinated by a central policy authority and published through the European C-ITS Trust List (ECTL). Before devices can operate, they must be enrolled. Enrollment policies verify security capabilities like key protection, firmware integrity, and standards compliance. Once approved, devices receive an enrollment certificate. This allows them to request operational credentials, such as pseudonym or authorization certificates. Certificate lifecycle controls define how credentials are issued, rotated, and revoked. These processes are governed by system-specific certificate policies and practice statements. Pseudonym certificates are rotated frequently to support privacy. Longer-term credentials like ECs or Root CAs follow stricter auditing and renewal schedules.

The Management Layer also monitors behavior. Devices and infrastructure evaluate message content for consistency and plausibility. If suspicious activity is detected, a Misbehavior Report (MBR) is generated. It includes supporting evidence like signed data, timestamps, and location history. Reports follow standardized formats to support interoperability. They are reviewed by a Misbehavior Authority for validation. Confirmed misbehavior can trigger certificate revocation or temporary suspension. This ensures only trustworthy devices remain active in the ecosystem.

### Threats to the Management Layer

The table below outlines example threats relevant to this layer.

| Threat Example                      | Security Objectives                                          |
| ----------------------------------- | ------------------------------------------------------------ |
| Invalid or unverified certificates  | Verify authenticity and policy conformance of credentials    |
| Inadequate revocation response      | Support timely revocation and trust list updates             |
| Poor misbehavior detection coverage | Enable multi-source reporting and evidence-based evaluation  |
| Unauthorized enrollment             | A device is enrolled into a certificate management system without meeting security or compliance requirements. |
| Key compromise                      | The private key associated with a trusted certificate is extracted or duplicated, allowing impersonation of a legitimate device. |
| Improper trust anchor update        | A CTL update is manipulated and distributed without proper signatures. |
| Stale or missing revocation data    | Devices fail to download updated CRLs or CTLs and continue to trust revoked or expired entities. |
| Enrollment policy evasion           | An attacker submits a non-compliant device for enrollment.   |
| Role escalation using certificate   | A certificate is issued with overly broad SSPs, granting the device capabilities beyond its operational role. |
| Falsified BSMs                      | A vehicle transmits location data inconsistent with plausible movement, affecting other vehicles' path planning. |
| Unauthorized signal requests        | A device sends SRMs without entitlement or in implausible patterns. |
| Replay attacks                      | A recorded V2X message is retransmitted to mislead infrastructure or vehicles. |

#### Cybersecurity Objectives

The following objectives describe the intended cybersecurity outcomes for this layer and support the mitigation of the threats identified above.

- Establish a root of trust for all participants in the ITS environment.
- Control enrollment into certificate management systems through device validation. 
- Manage certificate issuance and revocation according to strict lifecycle rules.
- Ensure compliance with technical standards and operational policies. 
- Enable governance structures (e.g., Electors) to manage trust at scale.
- Support secure multi-jurisdictional interoperability. 
- Detect falsified or anomalous message content in real-time to identify compromised or malfunctioning devices.
- Validate behavioral consistency across space and time, such as physical plausibility of location, speed, and trajectory data.
- Enable revocation or remediation workflows tied to validated misbehavior events. 

## Physical Layer

The Physical Layer provides protections for field-deployed and centralized ITS assets. It addresses threats arising from direct physical access, such as device manipulation, cryptographic key theft, and sabotage. Components like RSUs, OBUs, signal controllers, and cabinet-based systems often operate in exposed environments and must be physically secured to prevent tampering. Devices should be enclosed in tamper-resistant housings with sealed entry points, monitored access controls, and environmental sensors. Access must be logged and managed under formal procedures. Backend infrastructure such as TMCs requires similar safeguards, including badge-controlled entry, monitored access points, and facility intrusion detection.

Cryptographic material must be protected using secure hardware such as secure elements, TPMs, or HSMs that perform operations in isolated environments. Keys must be non-exportable and protected by tamper-response mechanisms that erase sensitive material upon physical compromise. All firmware must be cryptographically signed, with secure boot enabled and unauthorized interfaces disabled before deployment. Updates must be authenticated, signed, and version-controlled, including over-the-air update workflows.

ITS devices should also be hardened and validated against environmental and signal manipulation. Shielding, anomaly detection, and redundant communications can help ensure operational resilience in harsh or adversarial environments.

The table below outlines example threats relevant to this layer.

| Threat Example                    | Security Objectives                                          |
| --------------------------------- | ------------------------------------------------------------ |
| Hardware tampering or replacement | Detect physical intrusion and validate firmware state        |
| Unauthorized physical port access | Enforce access control at all service interfaces             |
| Extraction of cryptographic keys  | Store keys in tamper-resistant secure elements               |
| Unauthorized cabinet access       | Attackers gain access to RSU or controller enclosures to manipulate configurations, install rogue devices, or extract sensitive data. |
| Cryptographic key extraction      | Attackers extract private keys from unsecured OBUs or RSUs using exposed memory or interfaces. |
| Device cloning or hardware swaps  | Physical removal of trusted units and replacement with malicious devices impersonating the original identity. |
| Unauthorized firmware upload      | Use of USB, serial, or debug ports to install unsigned or malicious firmware. |
| Sensor spoofing or blinding       | Attackers interfere with radar, video, or Global Positioning System (GPS) sensors using external signals. |
| Sabotage                          | RSUs or cabinets are damaged or degraded through vandalism or non-adversarial means. |

#### Cybersecurity Objectives

The following objectives describe the intended cybersecurity outcomes for this layer and support the mitigation of the threats identified above.

- Prevent unauthorized physical access to devices and infrastructure
- Protect cryptographic materials (e.g., private keys, firmware signatures) from extraction or tampering
- Ensure authenticity and integrity of firmware and hardware configurations
- Support traceability and accountability through access logging and auditability
- Provide secure boundaries to ensure devices operate only in authorized physical and network contexts (e.g., school bus OBU must only be installed in a school bus)





