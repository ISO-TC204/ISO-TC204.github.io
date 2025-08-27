# Management Patterns (M) 

## Pattern M1: Certificate Lifecycle Management 

ITS Station Operators and Infrastructure Owners (IOOs) depend on Public Key Infrastructure (PKI) providers to manage the lifecycle of digital certificates that authorize device and application behavior. Lifecycle management includes certificate issuance, validation, renewal, revocation, and trust list administration. The goal is to ensure that only eligible devices with verified cryptographic keys and compliant behavior are allowed to operate within a C-ITS or V2X environment.

The PKI ecosystem includes multiple interrelated functions: certificate issuance, revocation, entitlement authorization, misbehavior management, and trust list governance. As shown in the below diagram, these elements interact to support secure, policy-aligned credential management across jurisdictions.

![PKI Functions](C:/Users/bruss/OneDrive - TrustThink, LLC/Projects - TrustThink, LLC/ITS JPO/ISO/ISO Cybersecurity Website/Development/ISO-TC204.github.io/docs/cybersecurity/images/PKI_Functions.jpg)

##### Implementation Context

While IOOs do not operate the PKI themselves, they must actively manage interactions with PKI providers and ensure their devices maintain trustworthiness throughout the credential lifecycle.

| **Applies To**   | IOOs, RSUs, OBUs, TMC Systems, PKI Providers, Trust List Managers |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Certificate enrollment, revocation monitoring, trust list enforcement, misbehavior integration |
| **Dependencies** | Secure key generation, audit traceability, CRL/CTL configuration, CP/CPS review, misbehavior reporting workflows |

IOOs must:

- Validate that PKI providers conform to Certificate Policy (CP) and Certificate Practice Statement (CPS) requirements.
- Authorize only eligible devices for enrollment (e.g., verified firmware, hardware security modules).
- Configure devices to validate Certificate Trust Lists (CTLs) and download Certificate Revocation Lists (CRLs).
- Participate in PKI audits and policy governance when required.
- Coordinate certificate lifecycle events with backend systems (e.g., trust anchor updates, revocation responses).



##### Key Components

| **Component**                        | **Role**                                                     |
| ------------------------------------ | ------------------------------------------------------------ |
| Certificate Policy (CP)              | Defines PKI operational rules, eligibility criteria, and trust procedures |
| Certificate Practice Statement (CPS) | Describes how the CP is operationalized by the PKI           |
| Enrollment Certificates              | Authenticate devices during credential requests              |
| Authorization Certificates           | Authorize application functions (e.g., based on PSID/SSP)    |
| Certificate Trust List (CTL)         | Set of Root/Intermediate CAs trusted for certificate validation |
| Certificate Revocation List (CRL)    | List of revoked certificates published by the PKI            |
| Misbehavior Report Interface         | Enables revocation decisions for compromised or non-compliant entities |
| Trust List Management Procedures     | Define how CTLs are updated, published, and synchronized across devices |

##### Example Use Cases

| Scenario              | Behavior Enforced                                            |
| --------------------- | ------------------------------------------------------------ |
| ITS Device Enrollment | A compliant device generates a key pair and requests a certificate. The PKI checks CP compliance and issues credentials. |
| Misbehavior Response  | A backend detects invalid messages from an OBU. A misbehavior report is filed and the PKI revokes its certificates. |
| CRL Enforcement       | A field device downloads the latest CRL and rejects signed messages from a revoked certificate. |
| Audit Participation   | An IOO provides documentation showing that all enrolled RSUs met CP requirements and were properly onboarded. |
| Trust List Update     | ITS Devices receive updated CTLs from the PKI Provider.      |

##### Related Standards

| Standard                   | Purpose                                                      |
| -------------------------- | ------------------------------------------------------------ |
| IEEE 1609.2 / 1609.2.1     | Defines certificate structure, cryptographic operations, and revocation processes |
| IEEE 1609.2.2              | Provides mechanisms for trust list management and multi-jurisdictional interoperability |
| ETSI TS 102 941            | Describes enrollment, authorization, and revocation in CCMS  |
| EU C-ITS CP (v3.0)         | Governs eligibility, audit, and lifecycle for EU-based PKI operations |
| SCMS Provider Requirements | Describes expected PKI behavior, interfaces, and controls in U.S.-based SCMS deployments |



## Pattern M2: Certificate-Based Device Enrollment

This pattern establishes a secure, standards-aligned process for onboarding ITS devices into a 1609.2-based PKI environment. It applies to both North American SCMS and European CCMS/C-ITS deployments, using defined enrollment and operational certificate flows to enforce trust, authorization, and revocation readiness.

Devices receive long-term enrollment credentials (ECs) and short-lived operational certificates (e.g., Authorization Tickets or pseudonym certificates). These are used to assert device identity, enable privacy-preserving communication, and support access control enforcement. All issued credentials must be traceable to trusted Root Certificate Authorities, as defined in the Certificate Trust List (CTL).

##### **Implementation Context**

| **Applies To**   | OBUs, RSUs, Roadside Gateways, Trust List Managers (TLMs), Enrollment Authorities |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Secure onboarding, certificate provisioning, trust root installation |
| **Dependencies** | Device key protection, PKI auditability, CP/CPS alignment, CTL/CRL enforcement |

##### **Key Components**

| **Component**                                     | **Role**                                                     |
| ------------------------------------------------- | ------------------------------------------------------------ |
| Enrollment Credential (EC)                        | Verifies device legitimacy; used to authenticate certificate requests |
| Authorization Ticket (AT) / Pseudonym Certificate | Short-term certificate for privacy-preserving application-layer messaging |
| Certificate Trust List (CTL)                      | Identifies all Root CAs trusted for issuance and validation  |
| Manufacturer Certification                        | Evidence that device has passed interoperability and security testing |
| Secure Key Storage                                | Prevents export or misuse of key material; enables secure operations |
| Re-enrollment Capability                          | Supports secure device re-provisioning after key loss or lifecycle reset |

##### **Implementation Details**

- Prequalification and Testing: Devices must meet cryptographic, networking, and security control requirements established by the PKI’s CP/CPS or onboarding authority. (See *OMNIAIR Test Case List*, v1.0.)
- Key Pair Generation: Keys must be generated on-device using secure hardware modules (e.g., TPMs, SEs, HSMs), and marked as non-exportable.
- Initial Enrollment: The device uses its EC to authenticate with the PKI and requests pseudonym or operational certificates containing appropriate PSIDs or ITS-AIDs with SSP constraints.
- Authorization Ticket Handling: Devices may request batches or rolling sets of short-term certificates for message signing. Certificates include validity constraints and permissions to support least privilege and privacy.
- Trust Anchor Provisioning: A CTL must be installed on the device, containing trusted root and intermediate CAs. Devices must reject any certificate chains not rooted in this CTL.
- Lifecycle Support: Devices must support certificate renewal, re-enrollment (e.g., after reset or key loss), and revocation status validation using CRLs or online checks.
- Privacy and Rotation: Devices rotate short-term certificates according to jittered schedules to limit traceability. Implementations must respect system-level policies on pseudonym rotation.

##### **Example Use Cases**

| **Scenario**           | **Behavior Enforced**                                        |
| ---------------------- | ------------------------------------------------------------ |
| Transit OBU Onboarding | A public bus OBU is provisioned with ATs authorizing SRM transmission in approved zones |
| RSU Replacement        | After physical replacement, the new RSU generates its key pair and is securely enrolled |
| Device Decommissioning | A traffic cabinet ITS device is wiped, EC is invalidated, and certs are added to the CRL |

##### **Related Standards and Policies**

| **Reference**                         | **Purpose**                                                  |
| ------------------------------------- | ------------------------------------------------------------ |
| IEEE 1609.2                           | Defines certificate structure, revocation and signature requirements |
| IEEE 1609.2.1                         | Defines enrollment and authorization credentials, and secure provisioning workflows |
| SCMS Manager EE Security Requirements | Defines U.S. requirements for secure key handling, privacy protection, and revocation |
| EU C-ITS Certificate Policy           | Operational and policy requirements for enrollment and issuance |
| ETSI TS 102 941                       | C-ITS trust and certificate handling in EU deployments       |
| ETSI TS 103 097                       | Profiles for EU Authorization Tickets and pseudonym certificates |



## Pattern M3: ITS Cybersecurity Audit and Compliance Checks

Ensures that ITS components and systems maintain alignment with approved cybersecurity policies and configuration baselines over time. This pattern uses audit mechanisms and automated compliance verification to detect deviations in device behavior, software, certificate usage, and trust relationships. It supports both proactive governance and reactive incident investigation by generating a record of configuration states and security-relevant events.

##### Implementation Context

Used in operational environments where long-lived ITS deployments require ongoing verification of cybersecurity posture. Applicable to roadside units, backend infrastructure, and mobile devices. 

##### Key Components

| Component              | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| Audit Logging          | Devices and backend systems must record security-relevant events (e.g., configuration changes, certificate usage, access attempts) in tamper-resistant logs. |
| Compliance Policies    | Defined criteria that describe acceptable configurations, certificate parameters, software versions, and trust settings. |
| Verification Tools     | Automated or manual processes that check actual system state against declared policies. |
| Time Synchronization   | Audit logs must use synchronized, trustworthy timestamps to support forensic traceability. |
| Remediation Mechanisms | Actions taken when noncompliance is detected, such as revoking credentials, triggering alerts, or requiring reconfiguration. |

##### Implementation Details

- Devices must generate audit logs locally and securely transmit them to a central or federated audit system.
- Regular compliance scans should verify that all components:
  - Use valid certificates with unexpired validity periods.
  - Match approved software hashes or package versions.
  - Enforce required access controls.
  - Logs must be cryptographically protected against tampering and reviewed by authorized personnel or systems.
- Devices that fail compliance checks should be flagged for remediation or isolation.

##### Example Use Cases

| Scenario                    | Behavior Enforced                                            |
| --------------------------- | ------------------------------------------------------------ |
| Certificate Lifetime Audit  | Backend system checks for expired or soon-to-expire device certificates and notifies operators. |
| Software Version Compliance | Field devices are scanned periodically to confirm they are running authorized firmware images. |
| Access Control Validation   | Logs show repeated login attempts with unauthorized credentials, triggering an alert. |

##### Related Standards

| Standard       | Purpose                                                      |
| -------------- | ------------------------------------------------------------ |
| NIST SP 800-92 | Provides guidelines for audit log generation, protection, and review. |
| NIST SP 800-53 | Defines audit and compliance controls for federal systems (e.g., AU-2, CA-7). |



## Pattern M4: Incident Management and Response

Establishes a structured, repeatable process for detecting, triaging, responding to, and recovering from cybersecurity incidents that affect ITS systems. This pattern enables organizations to maintain operational continuity and protect system trust by formalizing how incidents are logged, escalated, and resolved. Incident management includes both organizational procedures (e.g., roles, escalation paths, post-incident analysis) and technical enablers (e.g., alert interfaces, remote disablement). It applies to infrastructure operators, certificate authorities, backend service providers, and other trusted participants in the ITS ecosystem.

##### Implementation Context

Incident management applies to any ITS deployment where cybersecurity events may affect the integrity, availability, or trustworthiness of system components. It is particularly relevant for agencies managing field equipment, backend systems, or V2X services.

##### Key Components

| Component                              | Description                                                  |
| -------------------------------------- | ------------------------------------------------------------ |
| Incident Response Plan                 | Documents procedures, escalation chains, contact information, and defined response timelines for anticipated ITS-specific incident types. |
| Monitoring and Alerting                | Enables real-time visibility into system behavior via local anomaly detection, misbehavior reports, backend log aggregation, and threshold-based alerting. |
| Credential Revocation and Trust Change | Ensures that response actions include revoking affected certificates or restricting trust relationships, aligned with SCMS/CCMS procedures. |
| Forensic Evidence Collection           | Devices and backend systems must log events, message traces, and anomalies in a tamper-resistant, time-synchronized manner for later investigation. |
| Stakeholder Communication              | Protocols for notifying affected parties, such as OEMs, IOOs, or SCMS managers, and for fulfilling regional disclosure requirements. |
| Recovery and Lessons Learned           | Post-incident reviews should identify root causes, update playbooks, and guide system or policy improvements. |

##### Implementation Details

- Define an ITS-specific incident taxonomy, covering events such as credential theft, unauthorized message transmission, backend compromise, or device tampering.
- Map each incident type to containment actions (e.g., device isolation, credential revocation), and clearly define the authority and authentication required to execute these actions.
- Ensure that every field device and backend component supports audit logging, credential status reporting, and if feasible, remote disablement.
- Require vendors to document and test their device response behavior during simulated incidents.
- Incorporate incident response training into operator SOPs, and conduct table-top or live exercises annually.

##### Example Use Cases

| Scenario                     | Behavior Enforced                                            |
| ---------------------------- | ------------------------------------------------------------ |
| TMC Ransomware Attack        | A traffic management center is compromised by ransomware. Systems are isolated from the network, incident response teams begin recovery procedures, and affected stakeholders are notified. |
| Unexpected Firmware Detected | A device reports a firmware version that does not match the approved baseline. The system flags it for containment and a field inspection is scheduled. |

##### Related Standards

| Standard         | Purpose                                                      |
| ---------------- | ------------------------------------------------------------ |
| NIST SP 800-61r2 | Provides a framework for computer security incident handling. |



## Pattern M5: Misbehavior Detection and Reporting 

Operators must actively monitor for misbehavior within their ITS networks and support reporting, adjudication, and remediation. Misbehavior refers to message-level or behavioral anomalies—either malicious or accidental—that degrade system trust or operational safety. A full misbehavior lifecycle includes detection (local or backend), secure reporting, verification by an adjudicating authority, and proportional remediation (e.g., revocation, certificate issuance pause, or software update)

##### Implementation Context

| **Applies To**   | IOOs, RSUs, OBUs, PKI Providers, Backend Services, Misbehavior Authorities |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Detecting, reporting, and adjudicating V2X misbehavior across all layers |
| **Dependencies** | Detection rules, misbehavior authority capability, PKI integration, misbehavior policy |

##### Key Components

| **Component**                      | **Role**                                                     |
| ---------------------------------- | ------------------------------------------------------------ |
| Local Detection Logic              | RSUs and OBUs detect anomalies                               |
| Backend Correlation Engine         | Aggregates and analyzes reports to detect patterns and false positives |
| Misbehavior Reporting Interface    | Secure channel for reports; includes cryptographically protected evidence |
| Adjudication and Remediation Logic | Authority validates reports and issues trust changes (e.g., revocation, suspension) |

##### Implementation Details

- Configure devices for local detection. Use plausibility checks and rule-based filters to flag suspicious activity, such as falsified position or signal preemption attempts.
- Enable structured logging. Capture message metadata, certificate info, and system state at time of anomaly for forensic analysis.
- Transmit signed reports. Devices must support secure misbehavior report generation using cryptographically bound evidence.
- Set up a backend adjudication workflow. Define procedures to investigate reports, determine attribution, and assess severity and impact.
- Support remediation actions. Integrate with certificate revocation or suspension mechanisms, such as CRLs, issuance pause, or software rollback.
- Define policy and thresholds. Specify which types of misbehavior trigger which level of response—revocation, temporary suspension, warning, etc.
- Train operators. Staff must understand the full lifecycle: detection → reporting → adjudication → remediation → reinstatement.
- Perform after-action reviews. Continuously improve detection policies and processes based on incident learnings.

##### Example Use Cases

| **Scenario**                   | **Action**                                                   |
| ------------------------------ | ------------------------------------------------------------ |
| Ghost Vehicle Broadcast        | RSU flags multiple identical vehicle IDs with inconsistent positions; report sent to backend |
| Unauthorized Signal Preemption | OBU uses unauthorized PSID to trigger green light; revoked after confirmation |
| Implausible BSM Speed Claim    | Vehicle claims certain speed; backend correlates across multiple RSUs to confirm inaccuracy. |

##### Related Standards

| **Standard**    | **Purpose**                                                  |
| --------------- | ------------------------------------------------------------ |
| IEEE 1609.2     | Defines security services, including signing of misbehavior reports |
| SAE J3287       | Guidance on misbehavior detection and adjudication           |
| IEEE 1609.2.1   | Interfaces for end-entity certificate and misbehavior management |
| ETSI TS 103 759 | Misbehavior Reporting service (EU)                           |

