# Performing an ITS Threat Analysis

Cybersecurity threat analysis is a critical step in ensuring the security of Intelligent Transport Systems (ITS), especially given the increasing connectivity of vehicles and infrastructure. This page is a guide for ITS stakeholders on best practices for performing a comprehensive threat, vulnerability, and risk analysis (TVRA) on their ITS.

## What is a Threat Analysis?

A cybersecurity threat analysis is a systematic process of identifying, analyzing, and evaluating the potential threats to a system. It is a foundational and beginning step in the process of defining ITS cybersecurity requirements and selecting the most appropriate ITS cybersecurity controls. This analysis informs the security requirements and the subsequent choice of countermeasures needed to protect the ITS assets.

A threat analysis should be an ongoing process, not a one-time event. It should be performed at all critical stages of the ITS lifecycle, including:

  - **Design and Development Phase:** The goal of a threat analysis in this phase is to build security requirements into the system from the beginning of the ITS program.

  - **Deployment Phase:** The analysis goal in this phase is to account for key attributes of the specific operational environment.

  - **Major Upgrade Phases:** The analysis goal in this phase is to address new functionalities or technologies that have the potential to introduce new vulnerabilities.

  - **After a Security Incident:** The analysis goal in this phase is to learn from the incident and prevent future occurrences.

## High-Level Process for Conducting an ITS Threat Analysis

ITS stakeholders should conduct threat analysis by evaluating how adversaries could compromise specific functions across the system. Begin by identifying each system component, and then for each component, assess the types of data that the component handles, the services it provides, and the interfaces it exposes. Use this information to define the threat surface and determine which attack scenarios are most relevant. Map each identified threat to an [ITS Cybersecurity Pattern](file:///docs/cybersecurity/its-security-patterns.md). As the system evolves, repeat the threat analysis at each critical lifecycle stage to validate that protections remain effective and aligned to real-world risks.

While specific methodologies may vary, most ITS threat analysis efforts follow a common structure. The following high-level steps apply broadly across both European and North American contexts:

1.  **Define Scope and Boundaries**: Identify which ITS assets are within scope for the threat analysis. This should include field devices, communications links, backend systems, cloud applications, etc. Document external interfaces.

2.  **Identify Assets, Data Flows and Security Objectives**:  Determine what needs protection within the system. For each asset, define the associated data flows to other assets. This would include for example cryptographic keys, GNSS data, video feeds, V2X messages, etc. Then for each data flow, define security objectives such as ensuring integrity, availability, confidentiality, or non-repudiation.

3.  **Identify Relevant Threats**: Once assets and data flows are known, consider how they could be targeted. Threats may include unauthorized access, spoofing, message manipulation, denial-of-service, physical tampering, etc. Leverage tools such as the [MITRE ATT\&CK Framework](https://attack.mitre.org/) for a better understanding of attack types. It is important to understand and anticipate that attacks are often strung together in order to achieve greater effect.

4.  **Evaluate Risk**: Assess the likelihood and potential impact of each threat materializing in the specific operational environment in which the ITS operates. This assessment may be qualitative or quantitative. Risks should be prioritized based upon which risks require mitigation and which may be accepted based on operational context.

5.  **Select and Align Controls**: For threats requiring mitigation, identify suitable security controls which may be technical, procedural, or administrative. These may include for example message authentication, physical protections, redundancy, or personnel training. Control selection should reflect both the risk profile and the system’s functional requirements. Review the [ITS Cybersecurity Patterns](file:///docs/cybersecurity/its-security-patterns.md) page for more information on possible control selection.

6.  **Document and Reassess**: Maintain records of the analysis, including identified threats, rationale for control selection, and residual risks. Threat analysis should be revisited periodically or when significant changes are made to system architecture, configuration, or usage patterns.

## Core Threat Analysis Reference Methodologies:

There are several recognized methodologies for conducting a cybersecurity threat analysis, each with a slightly different focus. The two primary approaches for ITS are the European and North American models.

### European Approach (ETSI/ISO)

The European Telecommunications Standards Institute (ETSI) provides a detailed, 10-step TVRA (Threat, Vulnerability, Risk Analysis) methodology for conducting a threat analysis of various systems. This method is cyclical and aims to provide a quantitative rationale for security design. The TVRA method, as detailed in [ETSI TS 102 165-1](https://www.etsi.org/deliver/etsi_ts/102100_102199/10216501/05.03.01_60/ts_10216501v050301p.pdf), provides a structured process that systematically identifies threats, analyzes vulnerabilities, and evaluates the resulting risks. This approach helps in understanding the relationship between threats, vulnerabilities, and their potential impact on the system. The 10 steps of the TVRA process can be summarized as follows:

1.  **Identify the Target of Evaluation (TOE):** Define the ITS scope, assets, and environment.

2.  **Identify Objectives:** State the high-level security goals.

3.  **Identify Functional Security Requirements:** Derive specific requirements from the security objectives.

4.  **Inventory Assets:** Detail all assets within the ITS.

5.  **Identify Vulnerabilities and Threat Level:** Classify weaknesses and the threats that could exploit them.

6.  **Calculate Likelihood and Impact:** Quantify the probability and severity of a successful attack.

7.  **Establish Risks:** Determine risk as the product of likelihood and impact.

8.  **Identify Countermeasures:** Propose conceptual security solutions to reduce risks.

9.  **Conduct Cost-Benefit Analysis:** Evaluate the financial and operational trade-offs of the countermeasures.

10. **Specify Detailed Requirements:** Refine the security requirements and selected countermeasures for implementation.

In European Cooperative ITS deployments, threat analysis practices are well-established through a combination of technical reports and policy mandates. [ETSI TR 102 893](https://www.etsi.org/deliver/etsi_tr/102800_102899/102893/01.02.01_60/tr_102893v010201p.pdf) as an example outlines a TVRA methodology tailored to ITS environments. It provides a structured approach for identifying assets, categorizing threats, and evaluating risk based on likelihood and impact.

### North American Approach (NIST)

In North American Cooperative ITS deployments, threat analysis practices are becoming established through policy mandates. The National Institute of Standards and Technology (NIST) provides a risk assessment framework in its [Special Publication 800-30](https://www.nist.gov/privacy-framework/nist-sp-800-30). This process is composed of four high-level steps that closely align with the ETSI TVRA methodology:

1.  **Prepare for the Assessment:** Define the assessment’s purpose, scope, and identify assets and objectives. This aligns with the first four steps of the ETSI TVRA.

2.  **Conduct the Assessment:** Identify threats and vulnerabilities, and then analyze the likelihood and impact of threat events to determine the overall risk. This maps to steps 5, 6, and 7 of the ETSI TVRA.

3.  **Communicate Assessment Results:** The findings are presented to stakeholders, including recommendations for countermeasures. This corresponds to ETSI TVRA steps 8, 9, and 10.

4.  **Maintain the Assessment:** This is a continuous process of monitoring risk factors and updating the assessment. The cyclical nature of the ETSI TVRA process inherently maps to this maintenance phase.

North American threat analysis activities are also often embedded within other more general cybersecurity and risk management frameworks:

The [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) (CSF) provides a high-level, risk-based approach to managing cybersecurity. While NIST SP 800-30 provides the detailed methodology for the "Identify" function of the CSF, the CSF itself is a broader tool for communication and organization-wide risk management. The results of a NIST SP 800-30 risk assessment directly feed into the CSF's risk management strategy.

The [ITS CSF Profiles](https://transportationops.org/publications/usdot-resource-intelligent-transportation-systems-its-cybersecurity-framework-0) (ITS Profile) adapts the NIST CSF for transportation environments, offering detailed guidance tailored to ITS deployments. It outlines cybersecurity activities for stakeholders managing devices like Dynamic Message Signs, Closed-Circuit Television cameras, and Roadside Units.

Additional resources from the U.S. Department of Transportation, including procedural guidance and control set templates, support risk-informed decision-making for public agencies and infrastructure operators.

<!--Insert Relationship to ITS Control Sets Section-->

### Comparing North American and European Approaches

The following comparison table offers a summary comparison of the two continental approaches the TVRAs.

| **Feature**          | **ETSI TVRA**                                                | **NIST SP 800-30**                                           |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Primary Audience** | ETSI standards developers, but applicable to others          | Federal agencies, but widely adopted by the private sector   |
| **Number of Steps**  | 10 steps (detailed, granular)                                | 4 steps (high-level, process-oriented)                       |
| **Focus**            | Quantified analysis of threats, vulnerabilities, and risks to define security requirements | Risk assessment as part of an overall risk management framework |
| **Core Principle**   | Cyclical process, requiring re-evaluation with any system changes | Continuous monitoring and maintenance of risk factors        |
| **Output**           | A quantified measure of risks and detailed security requirements | Risk assessment report for decision-making                   |

*Table 1. North American / European TVRA Standards Comparison Table*

### Prioritizing Core Threats and Threat Sources

Threats to ITS are evolving as technology becomes more interconnected, particularly with the rise of **Vehicle-to-Everything (V2X)** communication. The primary threat sources are often sophisticated adversaries who exploit vulnerabilities to gain access to critical infrastructure. As highlighted in U.S. government guidance, these threats can originate from foreign-owned or controlled technology, making supply chain security a critical concern. There are several primary categories of ITS threats, as described in the following table:

| **ITS Threat Category**                  | **Description**                                              |
| ---------------------------------------- | ------------------------------------------------------------ |
| **Firmware / Software Vulnerabilities**  | Exploitable bugs or backdoors in the software of ITS assets can be used by attackers to gain control or disrupt operations. |
| **Physical Attacks**                     | Unauthorized direct physical access to ITS assets at locations such as field cabinets and server rooms can compromise the entire system. |
| **Denial-of-Service (DoS) Attacks**      | Malicious actors can flood ITS networks with a high volume of messages, disrupting communication and the normal operation of the systems. |
| **Spoofing Attacks**                     | Malicious actors mimic legitimate ITS assets to send false data, such as fake location information or traffic warnings, to mislead drivers and autonomous systems. |
| **Data Integrity and Message Tampering** | ITS asset messages, which may contain critical safety information like speed and position, can be intercepted and altered in transit. This can result in inaccurate or deceptive information being transmitted throughout the ITS environment. |

*Table 2. Key ITS Threat Categories*

These threat categories are described in detail in the ITS Threat Catalog, which can be used as a reference throughout the TVRA process.

## How to Use the ITS Threat Catalog: 

The ITS T**hreat Catalog** is a list of known or potential ITS threats. It is a resource to help identify potential threats that are a risk to a specific ITS environment. To utilize this resource effectively, users should first identify relevant ITS components (e.g., a vehicle's communication module, a roadside unit, or a central management server). For each of these components, you should select the relevant threats from the catalog and then proceed to a [detailed risk assessment](#Evaluating_Risk). Each threat in the catalog is categorized by its source (e.g., malicious insider, external hacker), its likelihood, and its impact rating. By mapping these threats to the system's architecture, you can methodically identify potential attack vectors and associated risk. Finally, use the Recommended Cybersecurity Controls column to identify controls that can be used to mitigate these threats in part or in whole.

## ITS Threat Catalogue

<<<<<<< HEAD:docs/cybersecurity/threat-analysis.md
The following threats may be applicable to an ITS. You may use these threats as references when developing your system-specific threat analysis and risk profile. See the Recommended Cybersecurity Controls column to identify controls that can be used to mitigate these threats in part or in whole.

| Threat ID | Threat Example                                               | [Recommended Cybersecurity Patterns](its-security-patterns.md) |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| T_0001    | Unauthorized ITS device or application access.               | [E2: Secure Device Configuration](patterns-edge.md#pattern-e2-secure-device-configuration) |
| T_0002    | Malware or modified code causes an ITS device to transmit false warnings or suppress valid messages. | [E6: Software Integrity Verification and Secure Boot](patterns-edge.md#pattern-e6-software-integrity-verification-and-secure-boot) |
| T_0003    | Exposure of driver identity information.                     | Pseudonymity                                                 |
| T_0004    | Unauthorized message injection                               | [A1: Authenticated Messaging](patterns-application.md#pattern-a1-authenticated-messaging) |
| T_0005    | A vehicle with general-use permissions reuses or fabricates SSP fields to impersonate an emergency responder. | [A3: Certificate-bound application authorization](patterns-application.md#pattern-a3-certificate-bound-application-authorization) |
| T_0006    | A device runs unapproved or unsigned applications due to weak software controls or side-loading. | [E2: Secure Device Configuration](patterns-edge.md#pattern-e2-secure-device-configuration) |
| T_0007    | Replay attacks re-use messages to impersonate legitimate messaging. | [N2 Secure Session Establishment Using ISO 21177](patterns-network.md#pattern-n2-secure-session-establishment-using-iso-21177) |
| T_0008    | Overcollection or linking of contextual data enables re-identification of pseudonymous users | Pseudonymity                                                 |
| T_0009    | Message interception or modification                         | [A1: Authenticated Messaging](patterns-application.md#pattern-a1-authenticated-messaging) |
| T_0010    | Geographic misuse of services                                | [A3: Certificate-bound application authorization](patterns-application.md#pattern-a3-certificate-bound-application-authorization); [E4: ITS Station Access Control](patterns-edge.md#pattern-e4-its-station-access-control) |
| T_0011    | Attackers send spoofed or malformed messages.                | [N1: Secure Backend Communications](patterns-network.md#pattern-n1-secure-backend-communications) [N2 Secure Session Establishment Using ISO 21177](patterns-network.md#pattern-n2-secure-session-establishment-using-iso-21177) |
| T_0012    | Passive attackers intercept V2X or backend messages to obtain sensitive information or gain situational awareness. | [N1: Secure Backend Communications](patterns-network.md#pattern-n1-secure-backend-communications) [N2 Secure Session Establishment Using ISO 21177](patterns-network.md#pattern-n2-secure-session-establishment-using-iso-21177) |
| T_0013    | An attacker inserts themselves between devices (man-in-the-middle) to relay or modify communications while impersonating trusted parties. | [N1: Secure Backend Communications](patterns-network.md#pattern-n1-secure-backend-communications) [N2 Secure Session Establishment Using ISO 21177](patterns-network.md#pattern-n2-secure-session-establishment-using-iso-21177) |
| T_0014    | Attackers present forged credentials or reuse compromised certificates to authenticate malicious devices. | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management) |
| T_0015    | Timing or synchronization failures due to misconfigured or denied Network Time Protocol | Secure Time                                                  |
| T_0016    | Link-layer injection or jamming                              | [N1: Secure Backend Communications](patterns-network.md#pattern-n1-secure-backend-communications) [N2: Secure Session Establishment Using ISO 21177](patterns-network.md#pattern-n2-secure-session-establishment-using-iso-21177) |
| T_0017    | Invalid or expired certificates used to attempt to gain access | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management) |
| T_0018    | Inadequate revocation response                               | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management) |
| T_0019    | Poor misbehaviour detection coverage                         | [M5: misbehaviour Detection and Reporting](patterns-management.md#pattern-m5-misbehaviour-detection-and-reporting) |
| T_0020    | ITS devices with revoked certificates are still trusted within the ITS. | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management) |
| T_0021    | Misbehaviours go undetected within the ITS                   | [M5: misbehaviour Detection and Reporting](patterns-management.md#pattern-m5-misbehaviour-detection-and-reporting) |
| T_0022    | An ITS device is enrolled into a certificate management system without meeting security or compliance requirements. | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management) |
| T_0023    | The private key associated with a trusted certificate is extracted or duplicated, allowing impersonation of a legitimate device. | [E1: Cryptographic Key Generation](patterns-edge.md#pattern-e1-cryptographic-key-generation) |
| T_0024    | A CTL update is manipulated and distributed without proper signatures. | [D1: 1609.2.2 Multi Jurisdictional Interoperability](patterns-deployment.md#pattern-i1-160922-multi-jurisdictional-interoperability); [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management) |
| T_0025    | Devices fail to download updated CRLs or CTLs and continue to trust revoked or expired entities. | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management); [E2: Secure Device Configuration](patterns-edge.md#pattern-e2-secure-device-configuration) |
| T_0026    | An attacker submits a non-compliant device for enrolment.    | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management); |
| T_0027    | A certificate is issued with overly broad SSPs, granting the device capabilities beyond its operational role. | [M1: IEEE Std 1609.2 Certificate Lifecycle Management](patterns-management.md#pattern-m1-certificate-lifecycle-management); [A3: Certificate-bound application authorization](patterns-application.md#pattern-a3-certificate-bound-application-authorization) |
| T_0028    | A vehicle transmits location data inconsistent with plausible movement, affecting other vehicles' path planning | [M5: misbehaviour Detection and Reporting](patterns-management.md#pattern-m5-misbehaviour-detection-and-reporting) |
| T_0029    | A device sends SRMs without entitlement or in implausible patterns. | [M5: misbehaviour Detection and Reporting](patterns-management.md#pattern-m5-misbehaviour-detection-and-reporting); [A3: Certificate-bound application authorization](patterns-application.md#pattern-a3-certificate-bound-application-authorization) |
| T_0030    | A recorded V2X message is retransmitted to mislead infrastructure or vehicles. | [N1: Secure Backend Communications](patterns-network.md#pattern-n1-secure-backend-communications); [N2 Secure Session Establishment Using ISO 21177](patterns-network.md#pattern-n2-secure-session-establishment-using-iso-21177) |
| T_0031    | An ITS device is tampered with.                              | Physical Access Controls; [E3: Tamper Detection and Response](patterns-edge.md#pattern-e3-tamper-detection-and-response) |
| T_0032    | An attacker gains unauthorized physical port access.         | Physical Access Controls; [E3: Tamper Detection and Response](patterns-edge.md#pattern-e3-tamper-detection-and-response) |
| T_0033    | Attackers gain access to RSU or controller enclosures to manipulate configurations, install rogue devices, or extract sensitive data. | Physical Access Controls; [E3: Tamper Detection and Response](patterns-edge.md#pattern-e3-tamper-detection-and-response) |
| T_0034    | Use of USB, serial, or debug ports to install unsigned or malicious firmware. | [E6: Software Integrity Verification and Secure Boot](patterns-edge.md#pattern-e6-software-integrity-verification-and-secure-boot) |
| T_0035    | Social Engineering of ITS personnel leading to credential compromise |                                                              |
| T_0036    | Attacker moves laterally from IT to OT network               |                                                              |
=======
The following threats may be applicable to any specific ITS environment. You may use these threats as references when developing your system-specific threat analysis and risk profile.

| **Threat ID** | **Threat Example**                                           | [**Recommended Cybersecurity Patterns**](file:///docs/cybersecurity/its-security-patterns.md) |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| T\_0001       | Unauthorized ITS device or application access.               | [E2: Secure Device Configuration](file:///docs/cybersecurity/patterns-edge.md#pattern-e2:-secure-device-configuration) |
| T\_0002       | Malware or modified code causes an ITS device to transmit false warnings or suppress valid messages. | [E6: Software Integrity Verification and Secure Boot](file:///docs/cybersecurity/patterns-edge.md#pattern-e6:-software-integrity-verification-and-secure-boot) |
| T\_0003       | Exposure of driver identity information.                     | Pseudonymity                                                 |
| T\_0004       | Unauthorized message injection                               | [A1: Authenticated Messaging](file:///docs/cybersecurity/patterns-application.md#pattern-a1:-authenticated-messaging) |
| T\_0005       | A vehicle with general-use permissions reuses or fabricates SSP fields to impersonate an emergency responder. | [A3: Certificate-bound application authorization](file:///docs/cybersecurity/patterns-application.md#pattern-a3:-certificate-bound-application-authorization) |
| T\_0006       | A device runs unapproved or unsigned applications due to weak software controls or side-loading. | [E2: Secure Device Configuration](file:///docs/cybersecurity/patterns-edge.md#pattern-e2:-secure-device-configuration) |
| T\_0007       | Replay attacks re-use messages to impersonate legitimate messaging. | [N2 Secure Session Establishment Using ISO 21177](file:///docs/cybersecurity/patterns-network.md#pattern-n2:-secure-session-establishment-using-iso-21177) |
| T\_0008       | Overcollection or linking of contextual data enables re-identification of pseudonymous users | Pseudonymity                                                 |
| T\_0009       | Message interception or modification                         | [A1: Authenticated Messaging](file:///docs/cybersecurity/patterns-application.md#pattern-a1:-authenticated-messaging) |
| T\_0010       | Geographic misuse of services                                | [A3: Certificate-bound application authorization](file:///docs/cybersecurity/patterns-application.md#pattern-a3:-certificate-bound-application-authorization); [E4: ITS Station Access Control](file:///docs/cybersecurity/patterns-edge.md#pattern-e4:-its-station-access-control) |
| T\_0011       | Attackers send spoofed or malformed messages.                | [N1: Secure Backend Communications](file:///docs/cybersecurity/patterns-network.md#pattern-n1:-secure-backend-communications) [N2 Secure Session Establishment Using ISO 21177](file:///docs/cybersecurity/patterns-network.md#pattern-n2:-secure-session-establishment-using-iso-21177) |
| T\_0012       | Passive attackers intercept V2X or backend messages to obtain sensitive information or gain situational awareness. | [N1: Secure Backend Communications](file:///docs/cybersecurity/patterns-network.md#pattern-n1:-secure-backend-communications) [N2 Secure Session Establishment Using ISO 21177](file:///docs/cybersecurity/patterns-network.md#pattern-n2:-secure-session-establishment-using-iso-21177) |
| T\_0013       | An attacker inserts themselves between devices (man-in-the-middle) to relay or modify communications while impersonating trusted parties. | [N1: Secure Backend Communications](file:///docs/cybersecurity/patterns-network.md#pattern-n1:-secure-backend-communications) [N2 Secure Session Establishment Using ISO 21177](file:///docs/cybersecurity/patterns-network.md#pattern-n2:-secure-session-establishment-using-iso-21177) |
| T\_0014       | Attackers present forged credentials or reuse compromised certificates to authenticate malicious devices. | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management) |
| T\_0015       | Timing or synchronization failures due to misconfigured or denied Network Time Protocol | Secure Time                                                  |
| T\_0016       | Link-layer injection or jamming                              | [N1: Secure Backend Communications](file:///docs/cybersecurity/patterns-network.md#pattern-n1:-secure-backend-communications) [N2 Secure Session Establishment Using ISO 21177](file:///docs/cybersecurity/patterns-network.md#pattern-n2:-secure-session-establishment-using-iso-21177) |
| T\_0017       | Invalid or expired certificates used to attempt to gain access | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management) |
| T\_0018       | Inadequate revocation response                               | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management) |
| T\_0019       | Poor misbehaviour detection coverage                         | [M5: Misbehavior Detection and Reporting](file:///docs/cybersecurity/patterns-management.md#pattern-m5:-misbehavior-detection-and-reporting) |
| T\_0020       | ITS devices with revoked certificates are still trusted within the ITS. | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management) |
| T\_0021       | Misbehaviours go undetected within the ITS                   | [M5: Misbehavior Detection and Reporting](file:///docs/cybersecurity/patterns-management.md#pattern-m5:-misbehavior-detection-and-reporting) |
| T\_0022       | An ITS device is enrolled into a certificate management system without meeting security or compliance requirements. | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management) |
| T\_0023       | The private key associated with a trusted certificate is extracted or duplicated, allowing impersonation of a legitimate device. | [E1: Cryptographic Key Generation](file:///docs/cybersecurity/patterns-edge.md#pattern-e1:-cryptographic-key-generation) |
| T\_0024       | A CTL update is manipulated and distributed without proper signatures. | [D1: 1609.2.2 Multi Jurisdictional Interoperability](file:///docs/cybersecurity/patterns-deployment.md#pattern-d1:-160922-multi-jurisdictional-interoperability); [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management) |
| T\_0025       | Devices fail to download updated CRLs or CTLs and continue to trust revoked or expired entities. | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management); [E2: Secure Device Configuration](file:///docs/cybersecurity/patterns-edge.md#pattern-e2:-secure-device-configuration) |
| T\_0026       | An attacker submits a non-compliant device for enrolment.    | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management); |
| T\_0027       | A certificate is issued with overly broad SSPs, granting the device capabilities beyond its operational role. | [M1 IEEE Std 1609.2 Certificate Lifecycle Management](file:///docs/cybersecurity/patterns-management.md#certificate-lifecycle-management); [A3: Certificate-bound application authorization](file:///docs/cybersecurity/patterns-application.md#pattern-a3:-certificate-bound-application-authorization) |
| T\_0028       | A vehicle transmits location data inconsistent with plausible movement, affecting other vehicles' path planning | [M5: Misbehavior Detection and Reporting](file:///docs/cybersecurity/patterns-management#pattern-m5:-misbehavior-detection-and-reporting) |
| T\_0029       | A device sends SRMs without entitlement or in implausible patterns. | [M5: Misbehavior Detection and Reporting](file:///docs/cybersecurity/patterns-management.md#pattern-m5:-misbehavior-detection-and-reporting); [A3: Certificate-bound application authorization](file:///docs/cybersecurity/patterns-application.md#pattern-a3:-certificate-bound-application-authorization) |
| T\_0030       | A recorded V2X message is retransmitted to mislead infrastructure or vehicles. | [N1: Secure Backend Communications](file:///docs/cybersecurity/patterns-network.md#pattern-n1:-secure-backend-communications); [N2 Secure Session Establishment Using ISO 21177](file:///docs/cybersecurity/patterns-network.md#pattern-n2:-secure-session-establishment-using-iso-21177) |
| T\_0031       | An ITS device is tampered with.                              | Physical Access Controls; [E3: Tamper Detection and Response](file:///docs/cybersecurity/patterns-edge.md#pattern-e3:-tamper-detection-and-response) |
| T\_0032       | An attacker gains unauthorized physical port access.         | Physical Access Controls; [E3: Tamper Detection and Response](file:///docs/cybersecurity/patterns-edge.md#pattern-e3:-tamper-detection-and-response) |
| T\_0033       | Attackers gain access to RSU or controller enclosures to manipulate configurations, install rogue devices, or extract sensitive data. | Physical Access Controls; [E3: Tamper Detection and Response](file:///docs/cybersecurity/patterns-edge.md#pattern-e3:-tamper-detection-and-response) |
| T\_0034       | Use of USB, serial, or debug ports to install unsigned or malicious firmware. | [E6: Software Integrity Verification and Secure Boot](file:///docs/cybersecurity/patterns-edge.md#pattern-e6:-software-integrity-verification-and-secure-boot) |
| T\_0035       | Social Engineering of ITS personnel leading to credential compromise |                                                              |
| T\_0036       | Attacker moves laterally from IT to OT network               |                                                              |

*Table 3. ITS Threat Catalog*

## Evaluating Risk

Not every identified threat requires a complex, expensive mitigation. The decision to mitigate a threat or accept the associated risk is a fundamental part of the risk management process, driven by a strategic balance between a threat's potential harm and the cost of preventing it. The decision to mitigate a threat or accept its risk is a core component of any cybersecurity strategy. In the context of ITS, this determination is made after a thorough risk assessment, which evaluates threats based on a simple principle:

Risk = Likelihood × Impact

To prioritize threats, you must first quantify them. This is typically done by evaluating the likelihood of a threat using factors like required exploitation time, required expertise, opportunity, and equipment. Calculating threat likelihood can be accomplished through an analysis using the following table:

| **Likelihood** | **Description**                                              |
| -------------- | ------------------------------------------------------------ |
| Low            | There are strong technical barriers to the implementation of the threat and/or the motivations for a threat actor are very low. |
| Medium         | There are low technical barriers to the implementation of the threat and/or there are reasonable motivations for a threat actor. |
| High           | There are low technical barriers to the implementation of the threat and/or there are high motivations for a threat actor. |

*Table 4. ITS Threat Likelihood Scoring Table*

The impact of a threat is determined by the consequences of a successful attack, such as the loss of confidentiality, integrity, or availability.

| **Impact** | **Description**                                              |
| ---------- | ------------------------------------------------------------ |
| Low        | There is minimal degradation to ITS operations and minimal data integrity degradation/loss in the event of a security incident. |
| Medium     | There is moderate degradation to ITS operations and/or moderate data integrity degradation/loss in the event of a security incident. |
| High       | There is major degradation to ITS operations and/or major data integrity degradation/loss in the event of a security incident. |

*Table 5. ITS Threat Impact Scoring Table*

## Determining Acceptable Risk

The decision to mitigate a threat or accept its risk is a core component of any cybersecurity strategy. A threat may be considered "acceptable" and not require mitigation if its resulting risk score is below a predefined threshold set by the organization. An example risk scoring matrix is a simple table where likelihood (low, medium, high) is plotted against impact (low, medium, high) to determine the risk level.

|                       | **Low Impact** | **Medium Impact** | **High Impact** |
| --------------------- | -------------- | ----------------- | --------------- |
| **High Likelihood**   | Moderate Risk  | High Risk         | Critical Risk   |
| **Medium Likelihood** | Low Risk       | Moderate Risk     | High Risk       |
| **Low Likelihood**    | Very Low Risk  | Low Risk          | Moderate Risk   |

*Table 6. Risk Scoring Matrix*

The risk score helps to prioritize threats, creating a clear picture of which ones pose the greatest danger to the system's security, safety, and functionality. The following table provides examples of how the ITS Threat Catalog can be used to define and prioritize threat risk, in order to determine the overall acceptable risk of relevant ITS threats:

| **Priority** | **Threat ID** | **Threat**               | **Likelihood** | **Impact** | **Risk Score** |
| ------------ | ------------- | ------------------------ | -------------- | ---------- | -------------- |
| 1            | T\_0031       | ITS Device Tamper        | High           | Medium     | High           |
| 2            | T\_0009       | ITS Message Modification | Medium         | High       | High           |
| 3            | T\_0003       | Driver Identity Exposure | Medium         | Medium     | Moderate       |
| 4            | T\_0032       | Physical Port Access     | Low            | High       | Moderate       |

*Table 7. Example TVRA Threat and Risk Analysis List*

## The Decision-Making Process

Once a comprehensive threat and risk analysis have been completed, the decision-making process begins by conducting a cost-benefit analysis. The cost-benefit analysis evaluates the financial and operational trade-offs of each threat between the threat risk and the cost of the applicable threat countermeasures. For each threat in the TVRA threat and risk analysis, decision must be made to either mitigate the threat, or accept the associated threat risk.

Threat mitigation is often appropriate for threats that have a high or critical risk score. Mitigation involves implementing cybersecurity controls and best practices to reduce either the likelihood or the impact of the threat.

Accepting a threat risk means making a conscious and informed decision to not implement cybersecurity controls. This is typically done for threats with a low (or sometimes moderate) risk score, where the cost of mitigation is higher than the potential impact of the event.

It is rare that an organization with have enough resources available to mitigate all identified risks. This is where the importance of risk prioritization plays a role. By following this systematic process, organizations can allocate their limited resources strategically, focusing on protecting what matters most while making informed decisions about threats that pose a minimal or acceptable level of risk.

The key to a consistent approach is to define a clear risk acceptance threshold. This is a business-level decision, not a technical one, that sets the maximum level of risk the organization is willing to tolerate. Any threat with a risk score above this threshold requires mitigation, while those below may be considered for acceptance.

By prioritizing threats by risk score in the TVRA threat and risk analysis list, This threshold can then be mapped against an organization’s currently available resources. Ideally an organization’s available resources will align with the risk mitigation threshold. Threats above the threshold will have resources allocated for mitigation. Threats below the threshold will not have resources made available and the risk from these threats will be accepted. If there is a misalignment between an organization’s risk threshold and available resources, the TVRA process provides a quantitative analysis for any resulting organizational budgetary and policy discussions.

## List of References and Resources

  - [ITS Cybersecurity Pattern](file:///docs/cybersecurity/its-security-patterns.md)

  - [MITRE ATT\&CK Framework](https://attack.mitre.org/)

  - [ETSI TS 102 165-1](https://www.etsi.org/deliver/etsi_ts/102100_102199/10216501/05.03.01_60/ts_10216501v050301p.pdf)

  - [ETSI TR 102 893](https://www.etsi.org/deliver/etsi_tr/102800_102899/102893/01.02.01_60/tr_102893v010201p.pdf)

  - [NIST Special Publication 800-30](https://www.nist.gov/privacy-framework/nist-sp-800-30)

  - [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

  - [ARC-IT ITS CSF Profile](https://transportationops.org/publications/usdot-resource-intelligent-transportation-systems-its-cybersecurity-framework-0)
>>>>>>> 7ac835d (BF Updates to ITS-Threat-Analysis page content):docs/cybersecurity/ITS-Threat-Analysis.md
