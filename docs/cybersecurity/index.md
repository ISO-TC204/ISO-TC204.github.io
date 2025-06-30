# Introduction to ITS Cybersecurity Guidance

Welcome to the ISO Guide to Cybersecurity for Intelligent Transportation Systems (ITS).

ITS operates as a System of Systems (SoS), connecting independently managed devices and services (e.g.,  roadside units (RSUs), On Board Units (OBUs), traffic signal controllers, backend systems) that may be owned and maintained by different organizations. Each is responsible for its own software updates, certificate handling, and operational policies. To ensure secure, coordinated behaviour across the ITS, operators must implement shared standards, interoperable trust mechanisms, and consistent communication policies. This site supports public agencies, standards bodies, integrators, manufacturers, and others responsible for the secure design and operation of ITS environments. You may view the [site glossary here](Glossary.md).

## Start Here: Introduction to ITS Cybersecurity – A Beginner's Guide

Begin with this [introductory guide](beginners-guide.md) to understand the basics of ITS Cybersecurity.

## Key Topics in ITS Cybersecurity

This site outlines how to secure ITS systems across all layers of design and operation. Key topics include:

### 1. [ITS Security Architectures](its-security-architectures.md)

An ITS security architecture defines how to apply protections across vehicles, infrastructure, networks, and backend systems. It ensures trusted communications, enforces policy, and enables response to security events. Use this architecture to assign responsibilities, align systems under a common trust model, and enforce security at each layer. For example, North American deployments often rely on SCMS for certificate management, while European systems use the CCMS. While these models differ in governance, both support similar PKI-based protections. This page outlines the layered security architecture and helps implementers select the right controls and standards based on operational risk and deployment environment.

### 2. [Security Standards and Their Roles](security-standards.md)

ITS cybersecurity depends on standards that define how to implement trust, secure communications, and system protections. Use this page to identify which standards support core cybersecurity functions, such as certificate management, authenticated messaging, or permission enforcement. For example, implementing secure V2X requires applying standards like [ISO 21177](https://www.iso.org/standard/87225.html), [IEEE 1609.2](https://standards.ieee.org/ieee/1609.2/10258/), and/or [ETSI TS 103 097](https://www.etsi.org/deliver/etsi_ts/103000_103099/103097/02.01.01_60/ts_103097v020101p.pdf) to handle certificate validation and message protection. Regional deployments may profile these differently: North America’s SCMS architecture relies on IEEE-based standards, while Europe’s C-ITS model uses ETSI protocols and centralized onboarding through the CPOC.

### [3. Performing an ITS Threat Analysis](ITS-Threat-Analysis.md)

The selection of cybersecurity controls to protect the ITS confidentiality, integrity and availability should be risk-informed, meaning that organizations that operate (e.g,. Infrastructure Owner Operators (IOOs)) an ITS should conduct a comprehensive threat analysis in order to understand the ITS's  risk profile. This threat analysis should be methodical, guided by a standard approach to performing threat and risk assessments.  Threat analysis often involves development of a profile of the ITS system assets, communication data flows, trust boundaries, and communication interfaces. Once this information is well understood and documented, threats and vulnerabilities can be identified for each asset or data flow. From there, an estimate of the likelihood and impact of different risks to the system can be calculated and appropriate mitigations can be identified. This allows [cybersecurity executives](policy-makers.md) within an ITS organization to prioritize the most appropriate cybersecurity controls given the risk profile and operational context of the system.

Several frameworks exist to guide the threat analysis process, depending on regional context. For example:

- In Europe, threat analysis activities are often shaped by [ETSI TR 102 893](https://www.etsi.org/deliver/etsi_tr/102800_102899/102893/01.02.01_60/tr_102893v010201p.pdf), a technical report that provides a structured approach for assessing risks in cooperative ITS environments. European station operators and manufacturers are also expected to conduct and maintain operational risk assessments in alignment with [ISO/IEC 27005](https://www.iso.org/standard/80585.html), as outlined in the CCMS Security Policy.

- In North America, threat analysis is typically informed by the [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) and the [ITS Cybersecurity Profile](https://transportationops.org/publications/usdot-resource-intelligent-transportation-systems-its-cybersecurity-framework-0), which together provide a foundation for identifying risks and applying controls across systems such as Dynamic Message Signs, Closed-Circuit Television cameras, RSUs and other systems.

### 4. [Interoperability Strategies](interoperability-strategies.md)

ITS devices must often interoperate across different policy jurisdictions. These jurisdictions may be based on local, regional, national or international borders. ITS components must be able to be configured to trust peer devices that may have been issued digital certificates that align with these different jurisdictions' policies and regulations. ITS Standards Developers, Policy-Makers, and Implementers have options for enabling seamless trusted interoperability. For example, at a national level policy-makers may choose to harmonize policies across multiple jurisdictions. There are technical options available as well. For example,  IEEE Std. 1609.2.2 provides a mechanism whereby specific trust permissions can be allocated to Root Certificate Authorities (Root CAs) using a PKI's Certificate Trust List (CTL). Other examples of interoperability enablers may include the use of trust bridges, that bridge trust between different domains.

### 5. [ITS Cybersecurity Controls](its-cybersecurity-controls.md)

ITS cybersecurity controls define the protections that must be implemented across system components, stakeholders, and environments. Use this page to identify the specific technical and operational safeguards needed to mitigate identified threats. Controls are organized by function such as certificate lifecycle management, access enforcement, software integrity, secure configuration, logging and auditing, misbehaviour response, and physical protections.

Responsibility for implementing controls is shared. Device manufacturers must embed protections into hardware and firmware. IOOs and operators are responsible for enforcing organizational policies, assigning roles and entitlements, and ensuring secure deployment and operation. Select controls based on your system's threat profile, architecture, and operational context.

### 6. [Stakeholder-Specific Guidance](stakeholder-guidance.md)

This section provides guidance tailored to different stakeholder perspectives, helping policy-makers, standards developers, and implementers understand their role in ITS development and deployment and their responsibilities related to ITS cybersecurity.  Guidance is included for:

- **Standards developers**, who must envision and document technologies and processes that enable ITS operations, while maintaining confidentiality, integrity, availability and resilience. Standards developers should keep in mind the need for cross-jurisdictional interoperability. SDOs may define standards applicable to ITS internationally, which then requires national and regional profiles of those standards to be created that meet appropriate policies and regulations.
- **Policy Makers**, who play a key role in defining the high-level frameworks for secure ITS system operations. Policy-makers must be able to understand and mitigate the risks associated with their ITS, provide guidance on harmonization across trust boundaries, and define minimum requirements to ensure trusted communication across an ITS.
- **Implementers**, who are responsible for identifying appropriate cybersecurity controls based on the given risk profile and operational context of the ITS. Implementers are deploying technology such as RSUs, managing certificate lifecycles, and enforcing security policies at the device and network levels. Implementers are responsible for the full lifecycle of the cybersecurity process, including incident response and forensic analysis.

### 7. [Security Policies](security-policies.md)

ITS cybersecurity policies define how protections are implemented, enforced, and maintained across devices, communications, and backend systems. These policies support secure deployment and operations by setting expectations for trust management, certificate handling, secure software updates, misbehaviour response, and audit enforcement. ITS operators must define clear policy rules for how trust anchors are approved and revoked, how device entitlements are assigned and validated, and how software is signed and verified. Policies must also require standardized incident handling procedures and governance models that ensure oversight across all roles and systems. This page outlines policy suggestions across key ITS security areas.

### 8. [Specialized Use Cases](specialized-use-cases.md)

As described above, the design of an ITS cybersecurity architecture should be based on an understanding of the risks, including residual risks, associated with the system, given the systems' operational context. As ITS technologies and concepts continue to evolve, new threats and risks are potentially introduced. This section describes some leading-edge use cases and system concepts and explores how each may introduce new sets of risks that must be mitigated within a cybersecurity architecture.

Use cases include emerging system ConOps such as Cooperative Driving Automation (CDA) and Mobile Edge Computing (MEC), where secure communication and trust management are critical to safe and efficient operation.
