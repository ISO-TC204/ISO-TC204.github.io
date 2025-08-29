# Introduction to ITS Cybersecurity Guidance

Welcome to the ISO Guide to Cybersecurity for Intelligent Transportation Systems (ITS).

ITS operates as a System of Systems (SoS), connecting independently managed devices and services (e.g.,  roadside units (RSUs), On Board Units (OBUs), traffic signal controllers, backend systems) that may be owned and maintained by different organizations. Each is responsible for its own software updates, certificate handling, and operational policies. To ensure secure, coordinated behavior across the ITS, operators must implement shared standards, interoperable trust mechanisms, and consistent communication policies. This site supports public agencies, standards bodies, integrators, manufacturers, and others responsible for the secure design and operation of ITS environments. You may view the [site glossary here](Glossary.md).

## Start Here: Introduction to ITS Cybersecurity – A Beginner's Guide

Begin with this [introductory guide](beginners-guide.md) to understand the basics of ITS Cybersecurity.

## Key Topics in ITS Cybersecurity

This site outlines how to secure ITS systems across all layers of design and operation. Key topics include:

### 1. [ITS Cyber Security Patterns](its-security-patterns.md)

ITS cybersecurity must be implemented consistently across independently managed vehicles, infrastructure, backend systems, and cloud services. These security patterns offer reusable, standards-aligned guidance for deploying protections based on system role, security function, and operational context.

Each pattern addresses a specific cybersecurity capability, for example certificate lifecycle management, application-layer authorization, transport encryption, or misbehavior reporting, and describes how it can be applied across varied ITS deployments. By referencing these patterns, implementers can identify the protections most relevant to their systems, ensure alignment with applicable trust models, and select implementation approaches that provide strong, scalable, and auditable mitigation of cybersecurity risk.

### 2. [Security Regulations, Frameworks, Standards and Guidance Documents](its-security-standards.md)

ITS cybersecurity is supported by a layered set of obligations and references, ranging from international regulations to organizational frameworks and technical standards. This section explains how global regulations such as the EU Cyber Resilience Act and UNECE vehicle requirements, governance frameworks like NIST CSF and ISO/IEC 27001, and sector-specific standards including IEEE 1609.2 and ETSI specifications work together to define secure practices.

### [3. Performing an ITS Threat Analysis](its-threat-analysis.md)

The selection of cybersecurity controls to protect the ITS confidentiality, integrity and availability should be risk-informed, meaning that organizations that operate (e.g,. Infrastructure Owner Operators (IOOs)) an ITS should conduct a comprehensive threat analysis in order to understand the ITS's  risk profile. This threat analysis should be methodical, guided by a standard approach to performing threat and risk assessments.  Threat analysis often involves development of a profile of the ITS system assets, communication data flows, trust boundaries, and communication interfaces. Once this information is well understood and documented, threats and vulnerabilities can be identified for each asset or data flow. From there, an estimate of the likelihood and impact of different risks to the system can be calculated and appropriate mitigations can be identified. This allows [cybersecurity executives](policy-makers.md) within an ITS organization to prioritize the most appropriate cybersecurity controls given the risk profile and operational context of the system.

Several frameworks exist to guide the threat analysis process, depending on regional context. For example:

- In Europe, threat analysis activities are often shaped by [ETSI TR 102 893](https://www.etsi.org/deliver/etsi_tr/102800_102899/102893/01.02.01_60/tr_102893v010201p.pdf), a technical report that provides a structured approach for assessing risks in cooperative ITS environments. European station operators and manufacturers are also expected to conduct and maintain operational risk assessments in alignment with [ISO/IEC 27005](https://www.iso.org/standard/80585.html), as outlined in the CCMS Security Policy.

- In North America, threat analysis is typically informed by the [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) and the [ITS Cybersecurity Profile](https://transportationops.org/publications/usdot-resource-intelligent-transportation-systems-its-cybersecurity-framework-0), which together provide a foundation for identifying risks and applying controls across systems such as Dynamic Message Signs, Closed-Circuit Television cameras, RSUs and other systems.

### 4. [Interoperability Strategies](its-interoperability-strategies.md)

ITS devices must often interoperate across different policy jurisdictions. These jurisdictions may be based on local, regional, national or international borders. ITS components must be able to be configured to trust peer devices that may have been issued digital certificates that align with these different jurisdictions' policies and regulations. ITS Standards Developers, Policy-Makers, and Implementers have options for enabling seamless trusted interoperability. For example, at a national level policy-makers may choose to harmonize policies across multiple jurisdictions. There are technical options available as well. For example,  IEEE Std. 1609.2.2 provides a mechanism whereby specific trust permissions can be allocated to Root Certificate Authorities (Root CAs) using a PKI's Certificate Trust List (CTL). Other examples of interoperability enablers may include the use of trust bridges, that bridge trust between different domains.

### 5. [Device and Application Security Policy Recommendations](policies-device.md)

ITS devices and applications must be configured in accordance with strong cybersecurity policies to prevent misuse, unauthorized access, or compromise. This section provides recommended configuration options for password management, user authentication, logging, encryption, and other security-relevant functions. The recommendations are based on established ITS guidance and can be applied across field devices, backend systems, and supporting applications to strengthen resilience and support consistent policy enforcement.

### 6. [**ITS Stakeholder Groups and Their Cybersecurity Focus Areas**](its-stakeholder-guidance.md)

This section provides guidance tailored to different stakeholder perspectives, helping policy-makers, standards developers, and implementers understand their role in ITS development and deployment and their responsibilities related to ITS cybersecurity.  Guidance is included for:

- **[Standards developers](stakeholder-standards-developer.md)**, who must envision and document technologies and processes that enable ITS operations, while maintaining confidentiality, integrity, availability and resilience. Standards developers should keep in mind the need for cross-jurisdictional interoperability. SDOs may define standards applicable to ITS internationally, which then requires national and regional profiles of those standards to be created that meet appropriate policies and regulations.
- **[Cybersecurity Oversight and Policy Authorities](stakeholder-policy-maker.md)** who play a key role in defining the high-level frameworks for secure ITS system operations. These bodies help ensure that security implementations align with risk management goals and regulatory expectations.
- **[Infrastructure Owner Operators (IOOs)](stakeholder-ioo.md)**, who are responsible for deploying, configuring, and maintaining ITS equipment such as RSUs, traffic controllers, and backend systems. IOOs must ensure that all devices are securely onboarded, monitored, and managed across their operational lifecycle. This includes overseeing certificate enrollment, applying secure configurations, collecting and analyzing cybersecurity logs, and supporting incident response and certificate revocation processes.
- **[Original Equipment Manufacturers (OEMs)](stakeholder-oem.md)**, who develop connected and automated vehicles. These stakeholders should work to ensure that their vehicles meet cybersecurity requirements defined in standards such as ISO/SAE 21434. 
- **[ITS Manufacturers and Application Developers](stakeholder-appdev.md)**, who design and deliver OBUs, RSUs, and application software. These stakeholders must implement security capabilities such as secure boot, tamper detection, and certificate validation. They are responsible for integrating with PKI services, enforcing policy constraints, and ensuring their products can interoperate within a multi-jurisdictional trust framework.
- **[Certificate Management Authorities](stakeholder-certmgmt.md)**, who design, develop and operate Public Key Infrastructure (PKI) systems, such as CCMS and SCMS. They are responsible for ensuring that these systems comply with published certificate policy and practices, and that they successfully pass audits on a routine basis. 

### 7. [ITS Misuse Cases](its-misuse-cases.md)

ITS misuse cases illustrate how attackers could chain multiple threats together to compromise transportation systems. Each case provides a short scenario, identifies which assets are affected, and highlights the relevant threats and mitigations. Misuse cases are designed to illustrate how incidents may unfold in practice so that stakeholders can better understand how to calculate risk and choose the optimal cybersecurity patterns for risk mitigation. 
