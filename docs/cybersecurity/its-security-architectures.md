# ITS Security Architecture

## The Purpose of an ITS Cybersecurity Architecture

ITS environments are highly distributed and composed of independently managed systems that must collaborate in real time across jurisdictional and policy boundaries. This reference ITS cybersecurity architecture is layered into groupings that map to stakeholder roles, and a set of high level cybersecurity requirements. After reviewing a layer's requirements, navigate to [cybersecurity controls](its-cybersecurity-controls) for guidance on specific implementation recommendations and [standards](security-standards) for pointers to the relevant standards that can be used to implement those controls. Each layer in this reference cybersecurity architecture identifies a set of high level requirements that stakeholders should consider implementing within their ITS deployment. 

## ITS as a System of Systems

ITS should be treated as a system of systems (SoS). Many devices and services will likely be developed, operated, and maintained independently, often within different jurisdictions. This decentralization introduces specific cybersecurity challenges. Expect each device or service to follow its own software lifecycle, potentially rely on distinct certificate authorities, and operate under separate governance and compliance models. To achieve secure interoperability, focus not only on securing each individual system, but also on managing trust relationships and aligning policies across the broader environment.

An ITS cybersecurity architecture should be designed to support flexible trust models, account for asynchronous software and certificate lifecycles, and clearly define how security responsibilities are distributed. Keep in mind that network access alone does not imply trust. Instead, enforce explicit permissions, validate credentials, and apply security policies to ensure each device is authorized to perform its intended functions securely.

## Core Security Principles for an ITS

Use the following principles to guide the development of a resilient, scalable, and standards-aligned ITS architecture

**Defense in Depth**: An ITS must be secured at multiple layers. Relying on a single type of control, such as perimeter firewalls or certificate validation alone, is insufficient. Layered protections ensure that failures or compromises in one area do not expose the entire system.

**Minimum Trust by Default**:  ITS participants should not be granted default privileges solely by virtue of connecting to the network. Instead, authorization is explicitly granted through mechanisms like certificate-based permissions, policy-driven entitlements, and controlled onboarding processes.

**Federated Trust Management**: Because ITS involves many independently managed systems, trust must be managed across organizational and jurisdictional boundaries. This is achieved through coordinated certificate policies, cross-certification mechanisms, and service entitlements that define what certificates are accepted and under what conditions.

**Scalability and Flexibility**:  The architecture must scale to accommodate millions of devices and evolving services. It should be modular, standards-aligned, and capable of integrating with new applications, certificate authorities, or regional deployments without requiring a full redesign.

**Anonymity Protection**:  Anonymity and privacy are important in ITS communications, particularly for users and vehicles transmitting location or user data. Architectures should support mechanisms such as pseudonym certificates, regular certificate rotation, and data minimization techniques. 

**Resilience and Recovery**:  The architecture must be resilient to both accidental failures and malicious attacks. It should support detection of misbehavior, revocation of compromised certificates, and defined processes for auditing PKI systems. 

## Roles and Responsibilities in the ITS Cybersecurity Ecosystem

ITS cybersecurity relies on the coordinated actions of diverse stakeholders, each responsible for securing a portion of the broader system. A clear understanding of these roles ensures accountability, facilitates coordination, and supports end-to-end trust and resilience.

**Standards Development Organizations (SDOs)**: Organizations such as ISO, IEEE, and ETSI define the technical frameworks and specifications that guide secure communication, certificate formats, permissions models, and interoperability. Their work enables regional and global consistency while allowing for tailored implementation.

**Certificate Management Authorities**: PKI Providers of systems such as the SCMS and CCMS manage the lifecycle of digital certificates. Their responsibilities include issuing, renewing, and revoking credentials, maintaining CTL'S, and enforcing policy constraints.

**Infrastructure Owners and Operators**: Public agencies, departments of transportation, and infrastructure providers are responsible for securing roadside units, traffic controllers, and other field equipment. This includes enforcing hardware protections, managing software updates, and coordinating with certificate authorities to onboard or revoke devices as needed.

**Vehicle Manufacturers and OEMs**: Automakers and equipment vendors play a key role in integrating security capabilities within OBUs. They ensure secure certificate storage, implement local misbehavior detection logic, and align with applicable standards and trust frameworks.

**Application and Service Providers**: Organizations that provide V2X-enabled applications or services, such as navigation, traffic signal priority, or fleet management must validate their services against authorization policies, obtain appropriate credentials, and ensure responsible data use and protection.

**Cybersecurity Oversight and Policy Bodies**: Governance authorities, including national cybersecurity agencies and regional coordinating groups, develop cybersecurity policies, perform audits, and establish incident response processes. These bodies help ensure that security implementations align with risk management goals and regulatory expectations.

**End Users and Deployers**: Those deploying and maintaining ITS components, whether technicians, engineers, or integrators, must follow best practices, enforce operational policies, and ensure device integrity during installation and lifecycle transitions.

## Architectural Layer of an ITS Cybersecurity Architecture

[ISO 21217](https://www.iso.org/standard/80257.html) describes an ITS-S reference model that can be used as a framework for developing and deploying secure ITS communication systems. The ISO 21217 reference model has been extended below to identify and allocate specific cybersecurity functions and capabilities to discrete areas within the model. This page discusses the cybersecurity controls that should be considered by both developers and implementers of an ITS. For more detailed discussion of the threats associated with each of these architectural layers, visit the [ITS Threat Analysis](its-threat-analysis) page. For more detailed descriptions of each of the individual building blocks within the security architecture, see the [ITS Cybersecurity Controls](its-cybersecurity-controls) page. 

## Reference Cybersecurity Architecture

The reference architecture illustrated below maps directly to the ISO 21217 ITS-S reference model, in order to maintain consistency with existing well-known ITS concepts. The architecture is broken out into:

- **Management functions**: The core cybersecurity processes and services that govern trust, monitoring, response, and coordination across an ITS deployment. This includes managing certificate lifecycles, enforcing interoperability rules, auditing systems, handling incidents, and supporting misbehavior adjudication.
- **Application functions:** Define how applications enforce secure behaviors, such as message authentication, service-specific authorization, and secure configuration practices, to maintain system integrity and protect sensitive functions.
- **Facilities functions:** Focuses on privacy protection, trust evaluation, and event-level security. Supports pseudonymity, localized misbehavior detection, anomaly logging, and enforcement of interoperability policies across message exchanges.
- **Network and Transport functions:** Provides the mechanisms to secure data in transit using authenticated, optionally encrypted communications. Ensures transport protocols are resistant to network-layer threats and aligned with trust and policy requirements.
- **Access functions:** Manages how devices establish secure sessions, validate software authenticity, and authenticate themselves to peers or networks. Supports session security, secure boot, and credential-based access enforcement.
- **Physical functions:** Covers the protection of hardware, cryptographic material, and interfaces from physical compromise. Includes secure storage, physical access controls, tamper detection, and secure key generation practices.

![Architectural Layers](./images/architecture_layers.jpg)

## Application Layer

ISO 21217 positions the Application Layer at the top of the ITS Station (ITS-S) architecture, responsible for invoking and managing the communication flows that support ITS services. This layer defines the behavior and security policies of each ITS application and determines how they interact with the rest of the system. In a cybersecurity context, the Application Layer must ensure that data flows are authorized, authenticated, and protected according to both global and local policies.

ITS applications are standardized, certificate-bound services identified by globally or regionally assigned identifiers—known as ITS Application Identifiers (ITS-AIDs) or Provider Service Identifiers (PSIDs). These identifiers are embedded in digital certificates and define the types of messages an application may transmit or process. Additional constraints are expressed through SSPs, which enable fine-grained role definitions. For example, a public transit vehicle’s OBU may be authorized to send a Signal Request Message (SRM) to request priority at intersections, but only if its certificate contains the correct PSID and SSP combination.

These permissions are enforced on both ends of the transaction: a sender must possess a valid certificate with the necessary authorizations, and the recipient must verify the certificate’s attributes before acting on the message. This model ensures that simply joining an ITS-aware network does not grant implicit trust or functionality. Instead, application behavior is tightly scoped to what has been explicitly authorized.

In addition to certificate-bound constraints, ITS applications are subject to deployment-specific policies managed by Station Operators or infrastructure owners. These policies define who may run an application, under what conditions, and in which geographic or operational context. Enforcement can occur through mechanisms such as geofencing, jurisdiction-specific logic in infrastructure, SSP-based filters, or lifecycle controls that determine when and where credentials may be used.

Applications typically use standardized message formats such as SAE J2735 or ETSI EN 302 637-x. These formats define not only the structure of the data but also the associated security requirements for signing, encryption, and validation. Adherence to these standards ensures interoperability and reduces risk from malformed or unauthorized messages.

Implementers should ensure that the following cybersecurity objectives are met at the Application Layer:

- **ITS_APP_1: Enforce permission-based access to ITS services.** All application actions must be tied to valid digital certificates issued through a recognized SCMS or CCMS. Certificates must include the correct PSID/ITS-AID and SSP fields for the intended function.
- **ITS_APP_2: Prevent unauthorized message injection.** All outgoing application messages must be signed, and all incoming messages must be validated against trusted certificate authorities. Message rejection should occur if permissions do not match the expected application profile.
- **ITS_APP_3: Apply policy-aware access rules.** Local rules regarding geographic, jurisdictional, and temporal use of applications should be encoded and enforced through certificate attributes or infrastructure logic. Deployment-specific policies define who may operate devices, under what conditions, and within which jurisdiction. These policies are enforced through mechanisms such as geofencing, time-of-day restrictions, certificate constraints, and service-specific permissions. 

## Facilities Layer

In a cybersecurity context, this layer enables ITS devices to detect misbehavior, log anomalous events, maintain privacy through pseudonymity, and operate securely across jurisdictional boundaries. Facilities functions help ensure that data received from other ITS participants is plausible. This includes real-time plausibility checks, such as verifying that vehicle locations are within valid map bounds or that reported speeds are physically possible, and local misbehavior detection based on defined rules.

To preserve privacy, the Facilities Layer manages pseudonym certificate use. Messages are signed using short-lived, unlinkable identifiers, which prevent long-term tracking of a vehicle or device across sessions.

Facilities components also support structured anomaly logging and reporting. Devices record abnormal or policy-violating behavior and forward relevant information to backend systems for further analysis and adjudication. This process enables scalable misbehavior response while minimizing bandwidth and processing overhead at the edge. When deployed across jurisdictions, ITS devices must interoperate securely. The Facilities Layer contributes to this by ensuring that locally detected anomalies, pseudonym management routines, and trust validation behaviors conform to overarching interoperability policies and system expectations.

Implementers should ensure the following security outcomes at the Facilities Layer:

- **ITS_FAC_1: Maintain user anonymity and protect privacy** through regular pseudonym certificate rotation and suppression of unnecessary identifying information.
- **ITS_FAC_2: Perform local misbehavior detection** by evaluating incoming message data for policy violations or implausible claims.
- **ITS_FAC_3: Log and report anomalous behavior** for further review and potential action by backend misbehavior authorities.
- **ITS_FAC_4: Support secure interoperability** by ensuring facilities-layer logic accommodates regional or jurisdictional trust settings.

### Network and Transport

The Network and Transport Layer in the ISO 21217 ITS-S reference model is responsible for securing communication flows between ITS devices. It ensures that data exchanges are protected against tampering, spoofing, and unauthorized access. This layer enables both transport security, which protects individual message flows, and network security, which protects the communication infrastructure as a whole. Secure session establishment and message validation are core responsibilities, helping to preserve message integrity, authenticate sources, and prevent misuse. 

Standards such as IEEE 1609.3 define network and transport protocols used in vehicular communications, while ISO 21177 provides the mechanism for secure session management between ITS Stations. When backend or control system traffic is exchanged over TCP/IP networks, TLS 1.3 with mutual authentication should be used. DTLS is appropriate when UDP transport is required, such as for latency-sensitive data.

All messages must be verified for structural integrity, origin, and freshness. Anti-replay protections such as timestamps should be enforced to ensure that messages cannot be reused to trigger unintended behaviors.

Implementers should ensure the following cybersecurity outcomes at the Network and Transport Layer:

- **ITS_NET_1: Establish authenticated sessions using ISO 21177.** Use ISO 21177 to negotiate, establish, and manage secure sessions between ITS devices, including session key exchange and validity checks.
- **ITS_NET_2: Implement TLS 1.3 or DTLS with mutual authentication.** Use certificate-based authentication to secure all backend or infrastructure-facing sessions.
- **ITS_NET_3: Validate message integrity and authenticity.** All messages should be checked for proper digital signature and expected structure before use.
- **ITS_NET_4: Reject replayed or expired messages.** Timestamp inspection and session freshness checks should be used to prevent replay attacks.
- **ITS_NET_5: Preserve communication reliability during stress.** Use congestion control, prioritization, and network hardening techniques to maintain service availability during high load or attack conditions.

## Access Layer

Cybersecurity functions at this layer focus on enforcing local policy rules, verifying the authenticity of installed software, and confirming the permissions of connected ITS devices, using local policy checks. For example, an ITS Station may be configured to validate OpOrgIds embedded within a message against a list of authorized OpOrgIds within the locally configured policy. 

Implementers should ensure the following cybersecurity outcomes are met at the Access Layer:

- **ITS_ACC_1: Define and enforce local access policies.** Configure each device to restrict interface use, data access, or operational behavior based on predefined local rules. These policies may be informed by certificate-based entitlements.
- **ITS_ACC_2: Authenticate software before execution.** Ensure that only software with verified provenance is installed and permitted to run. Use digital signatures or other mechanisms to detect unauthorized changes or tampering.
- **ITS_ACC_3: Verify device identity.** Implement controls that authenticate devices before allowing them to initiate communication or participate in ITS operations. This ensures that only authorized hardware can access or influence the system.

## Management Layer

The Management Layer defines cybersecurity functions that operate across the ITS architecture to maintain trust, enforce policies, and support operational oversight. It supports secure onboarding, continuous oversight, and system-wide interoperability through centralized and distributed security services. Management functions govern how devices are credentialed, monitored, and maintained within the ITS environment. They ensure that all participants adhere to defined security policies and that the system can adapt to changes, respond to incidents, and preserve trust over time. These functions span multiple domains and jurisdictions, enabling ITS deployments to interoperate securely even under varying operational policies.

Cybersecurity functions that should be implemented at the Management Layer include:

- **ITS_MGT_1: Certificate Lifecycle Management.** Devices must be enrolled using secure procedures and issued credentials appropriate to their role. Credential issuance, renewal, revocation, and rotation must be governed by strict lifecycle policies.
- **ITS_MGT_2: Audit and Logging.** Security events must be logged in a tamper-resistant, time-synchronized format to support compliance validation and forensic investigation.
- **ITS_MGT_3: Interoperability Enforcement.** Devices must verify that remote systems adhere to policy constraints and CTLs, especially in cross-domain or cross-jurisdiction scenarios.
- **ITS_MGT_4: Secure Time Coordination.** All time-sensitive functions, including certificate validation and anomaly detection, rely on synchronized secure time sources.
- **ITS_MGT_5: Incident Management.** Devices and infrastructure must support structured detection, classification, and remediation of cybersecurity incidents.
- **ITS_MGT_6: Misbehavior Processing and Adjudication.** Anomalous behavior must be detected and reported via structured formats. A Misbehavior Authority evaluates such reports and takes appropriate actions such as revocation or suspension.

## Physical Layer

The Physical Layer includes protections that prevent unauthorized access to or manipulation of ITS hardware. These safeguards apply to both field-deployed devices and centralized systems (e.g., data centers, TMCs). Cybersecurity functions at this layer include securing storage, enforcing physical access controls, implementing tamper detection and response mechanisms, and protecting cryptographic key generation. These controls reduce the risk of physical tampering, unauthorized data extraction, hardware modification, or insertion of malicious components.

To align with the architecture, implementers should focus on the following cybersecurity outcomes:

- **ITS_PHY_1: Secure Storage.** Use tamper-resistant hardware modules such as TPMs, secure elements, or HSMs to protect cryptographic keys and sensitive data. Ensure these components support secure erase and integrity verification functions.
- **ITS_PHY_2: Physical Access Controls.** Restrict access to devices and facilities using strong physical controls such as locking enclosures, badge-based entry, and authorized maintenance procedures.
- **ITS_PHY_3: Tamper Detection and Response.** Employ mechanisms that detect physical intrusion or component replacement. Devices should log tampering events and trigger protective actions, such as key erasure or device lockdown.
- **ITS_PHY_4: Cryptographic Key Generation.** Keys must be generated using hardware-based entropy sources that meet recognized standards. Generation should occur in secure environments to prevent key exposure or duplication.
