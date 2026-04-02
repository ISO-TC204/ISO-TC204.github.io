# Cybersecurity Governance Authorities

Authorities define how trust is established and managed within a deployment. This includes governance of certificate policies, trust anchors, and credential management frameworks. Governance models vary by region. For example, European deployments use a centralized model where a Certificate Policy Authority governs root-level trust decisions and the European Certificate Trust List (ECTL), while North American deployments use a multi-entity model where trust is established through Certificate Trust Lists (CTLs) managed by [SCMS](https://www.scmsmanager.org/) participants. These structures determine who can issue credentials, how trust is extended, and how policy decisions are enforced across the ecosystem.

## Privacy and Identity Protection Policy

Authorities define requirements for protecting identity and preventing long-term tracking of ITS participants. This includes policies governing the use of pseudonym certificates, certificate rotation, and restrictions on identity linkage. Regional approaches differ. European deployments apply strict data protection requirements, including limits on data correlation and retention, while North American deployments implement privacy through pseudonym certificate rotation and restricted access to identity linkage functions.

## Compliance, Audit and Certification

Authorities must verify that policies and regulations are implemented effectively. This includes auditing certificate management authorities for compliance with CP and CPS requirements, reviewing OEM Cybersecurity Management Systems (CSMS) for conformance with [ISO/SAE 21434](ISO/SAE 21434) or [UNECE WP.29 R155](https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security) requirements, and conducting inspections of Infrastructure Owner-Operators (IOOs) to confirm that device security controls are applied consistently. Audits provide assurance that obligations are properly enforced in practice. Authorities define and enforce compliance requirements for all participating entities, including certificate management providers, manufacturers, and operators.

This includes:

- auditing certificate authorities against Certificate Policy (CP) and Certificate Practice Statement (CPS) requirements
- validating OEM cybersecurity management systems
- ensuring infrastructure operators apply required security controls

Compliance models vary by region. For example, European Root CAs must meet defined technical and organizational requirements prior to inclusion in the ECTL, while North American SCMS providers are audited against ecosystem-defined requirements and must maintain recognized certifications such as [ISO/IEC 27001](ISO/IEC 27001) or the [Trusted Information Security Assessment Exchange (TISAX)](https://enx.com/en-US/TISAX/).

## Incident Response and Coordination

Policy authorities are also responsible for establishing and coordinating incident response processes. This includes developing national or regional Computer Security Incident Response Teams (CSIRTs) with the capability to handle ITS-specific incidents, defining reporting obligations for manufacturers and operators, and ensuring that incident information is shared across stakeholders. Authorities coordinate response to cybersecurity incidents across organizational boundaries, including defining reporting obligations, supporting misbehaviour detection processes, and enabling cross-domain response when incidents affect multiple jurisdictions.
