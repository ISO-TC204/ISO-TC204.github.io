# Introduction to ITS Cybersecurity 

Welcome to the International Standards Organization (ISO) Guide Intelligent Transportation Systems (ITS) Cybersecurity.  This site provides practical guidance on how to secure ITS deployments, including threats, standards, system-design approaches, and operational practices. 

An ITS is composed of vehicles, roadside devices, communication networks, backend systems and applications that exchange data in near real-time. These components often communicate across trust boundaries. Vehicles may join and leave networks dynamically, and cannot rely on pre-established trust relationships with roadside infrastructure or peer vehicles. The figure below illustrates some of the complexities associated with an ITS System-of-Systems. 

![ITS Environment](C:/Users/BrianRussell/Documents/backup/cybersecurity/images/its_generic.jpg)

Systems such as Roadside Units (RSUs), sensors, and vehicle On-Board Units (OBUs) are often managed by different organizations. Each organization is responsible for securing its own systems and operations. For example, an Original Equipment Manufacturer (OEM) manages software and firmware updates for its brand of vehicles, a fleet operator monitors the performance and security posture of its fleet, and an infrastructure owner/operator manages roadside devices such as traffic signal controllers. 

These ITS systems exchange data through defined applications that generate and process messages for specific purposes, such as safety, mobility, or traffic operations. Each message is associated with an application profile that defines its structure, meaning and how it should be handled by a receiving system. For example, a vehicle may broadcast a safety message describing its position, speed and other attributes, while infrastructure systems may exchange signal status or control information. These Vehicle-to-Everything (V2X) messages are transmitted and/or received by applications on vehicles, road side equipment, and backend systems, and must be validated, authorized, and interpreted consistently across all ITS participants. 

Because these systems must operate together across organizational boundaries, ITS cybersecurity depends on well-defined standards. These standards define how messages are secured, how devices are identified and authorized, how trust is established between systems, and how data is protected in transit and at rest.

The following sections provide practical guidance on key aspects of ITS cybersecurity, including how messages are secured, how devices are identified and authorized, how trust is established between systems, and how data is protected in transit and at rest.

## Start Here: Introduction to ITS Cybersecurity – A Beginner's Guide

If you are new to the concept of ITS cybersecurity, start with the [Beginners Guide](beginners-guide.md). A glossary of terms is also available here: [site glossary](cybersecurity-glossary.md).

## ITS Cybersecurity

### 1. [ITS Cryptography Fundamentals](primer-cryptography.md)

ITS applications use cryptography to protect message integrity, authenticate senders, and control which devices and applications are allowed to participate in the system. These mechanisms are applied to both broadcast communications such as V2X messaging, and point-to-point communications between infrastructure and back-end systems.  This section explains how cryptographic functions such as digital signatures, secure communication protocols, and credential management are used in practice, including how messages are secured, how systems establish trust, and how credentials are issued, used and managed over time. 

### 2. [Security Regulations, Frameworks, Standards and Guidance Documents](its-security-standards.md)

ITS cybersecurity is informed by a combination of regulations, frameworks and technical standards.  These documents establish how systems are secured and how organizations should manage cybersecurity risk. Frameworks such as ISO/IEC 27001 and the NIST Cybersecurity Framework (CSF) define governance practices, while regulations such as the EU Cybersecurity Resilience Act and UNECE R155/R156 define mandatory requirements. Technical standards developed by organizations such as IEEE, SAE and ETSI define how security is implemented in ITS systems, devices and applications. 

### 3. [Performing an ITS Threat Analysis](its-threat-analysis.md)

ITS device manufacturers, OEMs, and infrastructure owner-operators need to understand the types of threats that can affect their systems and how those threats translate into operational risk. Threat analysis identifies assets, data flows, and trust boundaries, and evaluates how they could be targeted. This section explains how to perform a threat, vulnerability, and risk assessment (TVRA), including how to assess likelihood and impact and prioritize risks to guide security decisions.

### 4. [ITS Security Design Patterns](its-security-patterns.md)

ITS systems require consistent approaches to implementing security across devices, applications, networks, and operational processes. Security design patterns provide reusable solutions for common challenges such as securing communications, managing credentials, enforcing access control, and detecting misbehaviour. This section organizes these patterns by functional area, including application, device, network, and management layers. Each pattern describes how a specific security capability can be implemented in practice. 

### 5. [Interoperability Strategies](its-interoperability-strategies.md)

ITS systems must be able to exchange and process messages across different devices, vendors, and jurisdictions. This requires common message standards so that vehicles, roadside infrastructure, and backend systems can interpret data consistently. In addition to message compatibility, systems must be able to trust each other. This is achieved through certificate-based trust models, where devices validate that messages are authentic and authorized based on credentials issued by trusted authorities. This section explains how interoperability is achieved across trust domains, including the role of Public Key Infrastructure (PKI), policy alignment between regions, and mechanisms such as IEEE 1609.2.2 that enable controlled trust between different certificate authorities.

### 6. [ITS Security Configuration and Hardening Guide](device-hardening-guide.md)

ITS devices and applications must be securely configured before deployment and maintained throughout their lifecycle. Many ITS systems operate in exposed environments, where devices may be physically accessible and remotely reachable, increasing the risk of compromise if not properly secured. This section provides concrete configuration guidance across areas such as authentication, access control, logging, encryption, software updates, and key management. These recommendations can be applied to field devices, backend systems, and applications to reduce attack surface, enforce consistent security policies, and support secure operation at scale.

### 7. [ITS Cybersecurity Roles and Responsibilities](its-stakeholder-guidance.md)

ITS cybersecurity is shared across multiple stakeholder groups, each responsible for different parts of the system. Secure operation depends on clear roles, coordinated processes, and consistent implementation of security controls across vehicles, infrastructure, backend systems, and trust services. This section outlines the responsibilities of key stakeholders, including standards developers, certificate authorities, infrastructure operators, OEMs, application developers, and policy authorities, and how their roles contribute to a secure and interoperable ITS ecosystem.

### 8. [Common ITS Security Gaps & Remediations](its-security-gaps.md)

ITS systems must correctly validate data, enforce authorization, and apply trust decisions during operation. When these functions are not implemented or behave inconsistently, systems may accept invalid inputs, misinterpret data, or apply incorrect decisions. This section identifies common security gaps and the controls required to address them. Each example links a specific system condition to a corresponding requirement, helping implementers understand what must be enforced for correct and reliable system behavior.
