# Performing an ITS Threat Analysis

Threat analysis is a foundational practice for improving ITS cybersecurity. It allows planners, system designers, and operators to proactively identify potential vulnerabilities, understand how those vulnerabilities could be exploited, and prioritize protective measures before systems are deployed or as they evolve over time.

## High-Level Process for Conducting an ITS Threat Analysis

While specific methodologies may vary, most ITS threat analysis efforts follow a common structure. The following high-level steps apply broadly across both European and North American contexts:

1. **Define the Scope and System Boundary** Begin by describing the ITS environment under consideration. This includes identifying physical devices (such as Roadside Units, cameras, or signage), software platforms, communications interfaces, and any backend systems that interact with field devices. The goal is to clearly establish what is in scope for analysis and what is not.
2. **Identify Assets and Security Objectives** Determine what needs protection within the system. This may include cryptographic keys, position and timing data, video feeds, safety-critical messages, or access credentials. For each asset, define the associated security objectives—such as ensuring integrity, availability, confidentiality, or non-repudiation.
3. **Identify Threats**  Once assets are known, consider how they could be targeted. Threats may include unauthorized access, spoofing, message manipulation, denial-of-service, and physical tampering. 
4. **Evaluate Risk**:  Assess the likelihood and potential impact of each threat materializing, taking into account the environment in which the system operates. This assessment may be qualitative or quantitative. It helps prioritize which risks require mitigation and which may be accepted based on mission or operational context.
5. **Select and Align Controls**:  For threats requiring mitigation, identify suitable security controls which may be technical, procedural, or administrative. These may include for example message authentication, physical protections, redundancy, or personnel training. Control selection should reflect both the risk profile and the system’s functional requirements.
6. **Document and Reassess**:  Maintain records of the analysis, including identified threats, rationale for control selection, and residual risks. Threat analysis should be revisited periodically or when significant changes are made to system architecture, configuration, or usage patterns.

## European Threat Analysis Guidance

In European Cooperative ITS deployments, threat analysis practices are well-established through a combination of technical reports and policy mandates:

- ETSI TR 102 893 outlines a Threat, Vulnerability, and Risk Analysis (TVRA) methodology tailored to ITS environments. It provides a structured approach for identifying assets, categorizing threats, and evaluating risk based on likelihood and impact.
- The CCMS Security Policy requires station operators and manufacturers to conduct and maintain operational risk analyses. These are typically carried out using ISO/IEC 27005, which offers a repeatable process for risk management and ties directly to broader information security standards.

## North American Threat Analysis Guidance

In North America, threat analysis activities are often embedded within more general cybersecurity and risk management frameworks:

- The NIST Cybersecurity Framework (CSF) is widely adopted across critical infrastructure sectors, including transportation. It provides a functional model for cybersecurity organized around the lifecycle of identify, protect, detect, respond, and recover.
- The ITS Cybersecurity Profile adapts the NIST CSF for transportation environments, offering detailed guidance tailored to ITS deployments. It outlines cybersecurity activities for stakeholders managing devices like Dynamic Message Signs, Closed-Circuit Television cameras, and Roadside Units.
- Additional resources from the U.S. Department of Transportation, including procedural guidance and control set templates, support risk-informed decision-making for public agencies and infrastructure operators.

