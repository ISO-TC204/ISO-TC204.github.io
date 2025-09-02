# Performing an ITS Threat Analysis

ITS operators should conduct threat analysis by evaluating how adversaries could compromise specific functions across the system. Begin by identifying each system component and  for each, assess the types of data it handles, the services it provides, and the interfaces it exposes. Use that information to define the threat surface and determine which attack scenarios are most relevant. Map each identified threat to an [ITS Cybersecurity Pattern](its-security-patterns.md). As the system evolves, repeat the threat analysis to validate that protections remain effective and aligned to real-world risks.

## High-Level Process for Conducting an ITS Threat Analysis

While specific methodologies may vary, most ITS threat analysis efforts follow a common structure. The following high-level steps apply broadly across both European and North American contexts:

1. **Define Scope and Boundaries**
    Identify which ITS devices are within scope for the threat analysis. This should include field devices, communications links, backend systems, cloud applications applications, etc). Document external interfaces.
2. **Identify Assets, Data Flows and Security Objectives** Determine what needs protection within the system. This would include for example cryptographic keys, GNSS data, video feeds, V2X messages, etc. For each asset, define the associated data flows to other assets and for each data flow define security objectives such as ensuring integrity, availability, confidentiality, or non-repudiation.
3. **Identify Threats**  Once assets and data flows are known, consider how they could be targeted. Threats may include unauthorized access, spoofing, message manipulation, denial-of-service, physical tampering, among others. Leverage tools such as the MITRE ATT&CK Framework for a better understanding of attack types, and understand that attacks are often strung together in order to achieve greater effect.  
4. **Evaluate Risk**:  Assess the likelihood and potential impact of each threat materializing, taking into account the environment in which the system operates. This assessment may be qualitative or quantitative. It helps prioritize which risks require mitigation and which may be accepted based on  operational context.
5. **Select and Align Controls**:  For threats requiring mitigation, identify suitable security controls which may be technical, procedural, or administrative. These may include for example message authentication, physical protections, redundancy, or personnel training. Control selection should reflect both the risk profile and the system’s functional requirements. Review the [ITS Cybersecurity Patterns](its-security-patterns.md) page for more information on possible control selection.
6. **Document and Reassess**:  Maintain records of the analysis, including identified threats, rationale for control selection, and residual risks. Threat analysis should be revisited periodically or when significant changes are made to system architecture, configuration, or usage patterns.

### European Threat Analysis Guidance

In European Cooperative ITS deployments, threat analysis practices are well-established through a combination of technical reports and policy mandates:

- ETSI TR 102 893 outlines a Threat, Vulnerability, and Risk Analysis (TVRA) methodology tailored to ITS environments. It provides a structured approach for identifying assets, categorizing threats, and evaluating risk based on likelihood and impact.
- The CCMS Security Policy requires station operators and manufacturers to conduct and maintain operational risk analyses. These are typically carried out using ISO/IEC 27005, which offers a repeatable process for risk management and ties directly to broader information security standards.

### North American Threat Analysis Guidance

In North America, threat analysis activities are often embedded within more general cybersecurity and risk management frameworks:

- The NIST Cybersecurity Framework (CSF) is widely adopted across critical infrastructure sectors, including transportation. It provides a functional model for cybersecurity organized around the lifecycle of identify, protect, detect, respond, and recover.
- The ITS Cybersecurity Profile adapts the NIST CSF for transportation environments, offering detailed guidance tailored to ITS deployments. It outlines cybersecurity activities for stakeholders managing devices like Dynamic Message Signs, Closed-Circuit Television cameras, and Roadside Units.
- Additional resources from the U.S. Department of Transportation, including procedural guidance and control set templates, support risk-informed decision-making for public agencies and infrastructure operators.

## ITS Threat Catalogue

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
