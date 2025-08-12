# ITS Security Policy

Cybersecurity in Intelligent Transportation Systems (ITS) is governed by policies and regulations at multiple levels. Some requirements address organizational cybersecurity governance, such as ISO 27001 or the NIST Cybersecurity Framework (CSF), while others apply directly to ITS operational environments like traffic management centers, roadside infrastructure, or METR deployments. A third layer of policy governs external trust and service providers, including PKI ecosystems such as the Security Credential Management System (SCMS) in North America and the Cooperative Credential Management System (CCMS) in Europe. 

This page describes how these policy layers work together to define expectations for securing ITS systems and services.

## Organizational-Level Security Policy 

Organizational frameworks provide the governance foundation for cybersecurity, regardless of sector. They address risk management, process discipline, and compliance but do not define ITS-specific technical controls.

### ISO/IEC 27001

A widely adopted Information Security Management System (ISMS) standard that helps organizations:

- Identify and assess risks.
- Implement and maintain security controls.
- Continuously improve through audit and review cycles.

For Infrastructure Owner Operators (IOOs) in Europe, ISO/IEC 27001 certification demonstrates organizational cybersecurity maturity and aligns with many process-level requirements of the EU Cyber Resilience Act (CRA), including governance, access control, auditing, and supplier management.  However, ISO/IEC 27001 does not cover ITS-specific needs such as message signing, certificate validation, or device-specific security. These require sector-specific policies and standards (e.g., CCMS Security Policy, ETSI TS 103 097, SCMS policy sets).

### NIST Cybersecurity Framework (CSF)

Common in North America, the NIST CSF provides a modular, risk-based structure organized around six functional areas: Govern, Identify, Protect, Detect, Respond, and Recover.
 For ITS deployments, the CSF is used to:

- Define security expectations for state DOTs, transportation agencies, and municipalities.
- Guide risk assessments for ITS devices and systems.
- Align operational practices such as logging, patching, and incident response with national guidelines.

Like ISO/IEC 27001, it does not define protocol-specific requirements. Implementers using SCMS-based architectures must also follow SCMS Certificate Practice Statements, misbehavior reporting formats, and related operational requirements.

## ITS System-Specific Security Policy

These policies apply directly to ITS environments, ensuring the technical security of deployed systems and their components.

### European Union Cyber Resilience Act (CRA)

Effective December 10, 2024, the CRA imposes binding cybersecurity obligations for all digital products in the EU, including OBUs, RSUs, and Traffic Management Systems.
 Key mandates:

- Security-by-design from initial development through end-of-life.
- Products released without known exploitable vulnerabilities, with secure defaults before market placement.
- Continuous maintenance, including patches and vulnerability remediation for the entire operational lifetime.
- CE marking before market release, with enhanced third-party assessment for critical products.

The CRA also requires risk management processes, vulnerability disclosure procedures, incident handling workflows, and supply chain cybersecurity.

### U.S. ITS Control Sets

In the U.S., FHWA ITS Security Control Set documents map ITS requirements to technical and operational controls. These control sets ensure secure communications, certificate use, and operational consistency.

## Third-Party, Trust Management and Cyber Security Policies

ITS ecosystems depend on PKI-based trust services. These policies define how trust anchors are established, maintained, and revoked.

### Trust Management

Operators must establish how Root Certificate Authorities (RCAs) are authorized, audited, and removed. Define approval criteria, governance procedures, and enforcement mechanisms to manage trust relationships over time. Trust model design varies by region:

- SCMS (typical in North America): a quorum of Electors manages the CTL.  You can learn more about [SCMS Manager Policies.](SCMS-Manager-Policies)  
- CCMS (typical in Europe): a central Certificate Policy Authority (CPA) defines trust rules and governs the ECTL.  You can learn more about [CCMS Security Policy](CCMS-Security-Policies). 

The table below describes some of the key roles related to Trust Management. 

| Example Role | Role Description                                             |
| ------------ | ------------------------------------------------------------ |
| Root CA      | Serves as the top-level trust anchor, issuing certificates to subordinate CAs and enforcing strict policies to ensure the security and integrity of the entire certificate chain. |
| TLM          | Responsible for maintaining and updating the list of trusted root certificates, ensuring that only valid and compliant Root Certification Authorities are recognized by relying parties. |
| CPA          | Responsible for establishing and maintaining the overarching policies and standards that govern certificate issuance, usage, and management throughout the system, and decisions on applications and revocations of Root CA's in the CCMS (ECTL). |
| CPOC         | Acts a the technical interface to a TLM, validates certificate submissions and ensures compliance with operational policies. |
| ECTL         | Provides the encoded and signed electronic trust list used by relying parties to verify which Root Certificate Authorities are trusted at a given time. |

 Trust Management policies should specify: 

- Evaluation criteria for new Root CAs (e.g., audits, conformance testing).
- Procedures for removing compromised or non-compliant CAs.
- Methods for distributing updated CTLs/ECTLs to field devices.
- Methods for versioning CTLs/ECTLs on field devices. 
- Requirements that ITS devices must reject unsigned or unrecognized trust anchors.

### Certificate Policies (CP) and Certificate Practice Statements (CPS)

Every PKI must be governed by a Certificate Policy (CP) that defines acceptable certificate uses, validation rules, and interoperability expectations. Certificate Practice Statements (CPS) from PKI operators must align with these policies and outline the implementation details of:

- Enrollment processes (e.g., validation, RA functions).
- Operational certificate issuance (e.g., constraints, PSID/SSP inclusion).
- Revocation mechanisms (e.g., CRL use, expiration policies).

Audits and compliance checks ensure CPS adherence and allow agencies to verify that PKI participants meet security and policy obligations. Certificate lifecycle requirements are defined in these documents.  A strong lifecycle policy ensures that certificates are only issued to eligible devices, are used for authorized roles, and can be revoked if necessary.

In an SCMS, devices request an Enrollment Certificate, validated by the Registration Authority (RA) and issued by the Enrollment Certificate Authority (ECA). Operational certificates (e.g., pseudonym certs) are requested using entitlements like PSIDs/SSPs and issued by the Authorization Authority. Revocation is managed through CRLs. 

In a CCMS, devices obtain long-lived Enrollment Authorization (EA) certificates from the Enrollment Authority. Short-lived Authorization Tickets (ATs) are requested from the Authorization Authority and used for day-to-day signing. The short lifetime of the certificates negates the need for revocation processes. 

A PKI's CP and CPS Documents should specify:

- Eligibility criteria for certificate enrollment.
- Validation rules for certificate requests.
- Certificate expiration schedules.
- Revocation workflows and enforcement.

### Entitlement Management

Entitlement policies define what services a device is allowed to access, expressed in terms of PSIDs, SSPs, or ITS-AIDs. In an SCMS, PSID/SSP values are assigned based on device roles and validated during CSR submission. The RA ensures entitlements comply with operational policies. In a CCMS, entitlements are coordinated by the CPA and enforced by subordinate CAs to ensure consistency. 

Entitlement policies should specify: 

- Who is authorized to assign entitlements (e.g., registration authority, policy authority).
- Acceptable combinations of service permissions.
- Requirements for auditing of entitlements privileging processing during issuance. 

### Secure Software and Firmware Policy

Software is a frequent target for attack. Policies must dictate how software and firmware are developed, signed, distributed, and verified before and during use.

Secure Software and Firmware policies should include: 

- Require ITS devices to verify firmware integrity at boot using trusted signatures.
- Mandate code signing for any distributed firmware updates, using cryptographic identities tied to trusted developers.
- Define who can issue updates, how those updates are verified, and how rollback or recovery is handled.
- Require procedures to respond to known vulnerabilities in software components, including patch timelines and risk assessments.

### Incident Response and Misbehavior Reporting Policy

Security incidents must be detected, reported, and mitigated. Policies define the roles and responsibilities during a security incident and provide the structure for auditing and recovery.

Policies Related to Incident Response should include: 

- What constitutes a reportable anomaly (e.g., invalid messages, location spoofing, traffic flooding).
- The need to use standardized message formats (e.g., SCMS MBR ASN.1) and reporting workflows.
- How misbehavior reports are validated and who can take action (e.g., revoke certificates).
- How cybersecurity incidents are escalated and shared across jurisdictions. 

### Audit, Evaluation, and Oversight

A strong governance framework should include roles for continuous evaluation and auditing of all entities. 

Policies Related to Audit, Evaluation and Oversight should include:  

- What audit data must be logged (e.g., certificate usage, trust list updates, firmware installs).
- The need for periodic review of PKI authority adherence to published CP and CPS documentation.
