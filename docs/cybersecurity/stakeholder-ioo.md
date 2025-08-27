# Infrastructure Owner Operators (IOOs)

Infrastructure Owners and Operators (IOOs) are responsible for the secure deployment, configuration, and operation of ITS field equipment such as RSUs, Dynamic Message Signs (DMS), CCTV systems, and traffic controllers. Their actions directly affect the trustworthiness of ITS system operation.  Although an IOO has wide responsibilities related to the overall secure deployment and operation of their ITS infrastructure, the below responsibilities are especially important to cybersecurity risk mitigation. 

## Certificate and Trust Management

IOOs are responsible for managing the certificate lifecycle of their ITS infrastructure by coordinating with one or more PKI providers. This includes selecting trusted providers, validating that devices meet eligibility criteria, and ensuring devices are properly configured to enforce trust anchors and revocation information. These actions enable secure message exchange, device authentication, and policy enforcement at the edge.

Key Actions:

- Select and authorize PKI providers (e.g., SCMS, CCMS) permitted to issue certificates to IOO-managed devices. Reference [Pattern M1: Certificate Lifecycle Management](patterns-management#pattern-m1:-certificate-lifecycle-management) 
- Approve eligible device types after verifying they meet security testing and enrollment prerequisites. Reference [Pattern M2: Certificate-Based Device Enrollment](patterns-management#pattern-m2:-certificate-based-device-enrollment)
- Configure field equipment (e.g., RSUs, DMS) to routinely download and enforce Certificate Revocation Lists (CRLs) to remove compromised or misbehaving entities.

## Secure Device Onboarding and Configuration

Before deploying ITS devices, IOOs must ensure each unit is securely configured, and properly authorized to operate within the environment. This process includes validating boot and firmware integrity, applying a secure baseline configuration, and provisioning appropriate credentials and access controls. 

Key Actions:

- Confirm device integrity by verifying secure boot status, firmware validation, and hardware key generation capabilities. Reference [Pattern E6: Software Integrity Verification and Secure Boot](patterns-edge#pattern-e6:-software-integrity-verification-and-secure-boot) and [Pattern E1: Cryptographic Key Generation](patterns-edge#pattern-e1:-cryptographic-key-generation). 
- Install trust anchors and enforce application-level permissions. 
- Apply secure configuration policies: disable unused interfaces, change default credentials, and enforce least-privilege access. Reference [Pattern E2: Secure Device Configuration](patterns-edge#pattern-e2:-secure-device-configuration). 
- Log onboarding activities and configuration details to support traceability, audits, and future compliance checks.

## Cybersecurity Monitoring and Detection

Ongoing monitoring is essential to detect threats, policy violations, or anomalous behavior in real-time. IOOs must establish processes to observe field device activity, collect and analyze logs, and respond quickly to signs of compromise. Detection capabilities should cover both network-level activity and application-specific anomalies.

Key Actions:

- Define monitoring objectives, performance baselines, and detection thresholds for ITS infrastructure and field devices.
- Deploy or integrate with systems that aggregate logs and detect anomalies across multiple devices or regions.
- Monitor messages for structural correctness, valid certificate use, and operational anomalies (e.g., out-of-bounds geolocation).
- Enable field-based detection of tampering events using onboard sensors and escalate findings for review.

## Incident Response

IOOs must maintain an operational incident response capability tailored to the ITS environment. This includes having clear, tested procedures for identifying and responding to cybersecurity events that could impact roadside equipment, backend services, or trust relationships.

Key Actions:

- Develop and maintain a formal incident response plan that includes defined roles, escalation paths, and response actions. Reference [Pattern M4: Incident Management and Response](patterns-management#pattern-m4:-incident-management-and-response)
- Conduct regular tabletop exercises and simulations to validate procedures and ensure staff readiness.
- Coordinate with vendors, PKI providers, and regional authorities to align on communication and remediation workflows.
- Review and update incident response policies based on evolving threats, technology changes, or lessons learned from real or simulated events.



## Supply Chain Oversight 

IOOs play a critical role in ensuring that the devices and systems they procure meet security and trust requirements before integration into the ITS ecosystem. This requires close coordination with manufacturers and vendors to validate that components support secure operation from the outset.

Key Actions:

- Require suppliers to demonstrate compliance with applicable Certificate Policies and Certificate Practice Statements (CP/CPS), including proper certificate formatting and secure key storage (e.g., secure element or HSM use).
- Validate that vendors implement required hardware protections such as tamper-resistance, firmware integrity verification, and secure boot.
- Incorporate security requirements into procurement specifications and verify conformance through documentation, audits, or third-party testing.