# Security Governance

This section explains the role of PKI certificate policy in the context of ITS security governance. Trust within a PKI is fundamentally established and maintained through policy documents that include Certificate Policy (CP) and Certificate Practices Statements (CPS). These documents define the rules, responsibilities, and requirements for all stakeholders involved in PKI operations. CP and CPS documents detail processes and policies associated with lifecycle management activities such as certificate enrollment, management, and revocation processes, along with mechanisms to ensure cross-jurisdictional interoperability and adherence to privacy regulations. 

Most PKI systems perform similar functions: trust management, entitlement enrollment, certificate lifecycle management, and misbehavior response. Each PKI Root Certificate Authority is required to define and enforce specific policies that affect the security and management of OBUs, RSUs and other equipment within an ITS environment. These policies are far reaching and impact enrollment processes, device technical security controls, certificate management processes, incident handling processes and overall audit and evaluation processes associated with both the PKI system and the devices being provisioned certificates by the PKI system.  The graphic below illustrates the many policy considerations that must be documented for secure certificate management. 

![pkiPolicies](Images\pkiPolicies.jpg)

## Trust Management
Trust anchor management defines how Root Certificate Authorities  are authorized and monitored. This process includes approving new trust anchors, auditing existing ones, and distributing updated trust lists to relying parties.  A  distributed trust model may involve Electors who are trusted entitles that vote to approve or revoke RCAs. RCAs then certify intermediate authorities (e.g., Enrollment or Pseudonym CAs). 

In the European model, a central policy authority defines certificate policies and oversees Root CA conformance. A designated TLM maintains the trust list, which is distributed to participating entities. Root CA inclusion or removal is based on defined policy and audit compliance. Example roles that may play a part in the overall governance for trust anchor management may include: 

| Example Role | Role Description                                             |
| ------------ | ------------------------------------------------------------ |
| Root CA      | Serves as the top-level trust anchor, issuing certificates to subordinate CAs and enforcing strict policies to ensure the security and integrity of the entire certificate chain. |
| TLM          | Responsible for maintaining and updating the list of trusted root certificates, ensuring that only valid and compliant Root Certification Authorities are recognized by relying parties. |
| CPA          | Responsible for establishing and maintaining the overarching policies and standards that govern certificate issuance, usage, and management throughout the system, and decisions on applications and revocations of Root CA's in the CCMS (ECTL). |
| CPOC         | Acts a the technical interface to a TLM, validates certificate submissions and ensures compliance with operational policies. |
| ECTL         | Provides the encoded and signed electronic trust list used by relying parties to verify which Root Certificate Authorities are trusted at a given time. |

### SCMS Trust Management

In the SCMS model, trust anchor management is handled by a distributed group of entities known as Electors. Electors collectively maintain the CTL, which identifies the Root CAs trusted by the system. Changes to the CTL, such as adding or removing a Root CA require approval through an Elector voting process. A quorum of Electors must digitally sign the CTL update before it is accepted by relying components. This mechanism ensures that no single authority can unilaterally alter the trust anchor set.

### CCMS Trust Management

In the CCMS model, trust anchor management is coordinated by a centralized governance structure. The CPA defines certificate policies and evaluates Root CAs for inclusion in the ECTL. Following a positive audit or policy evaluation, the CPA transmits its endorsement to the C-POC, which acts as the technical liaison. The C-POC validates submitted Root CA certificates and forwards them to the TLM, a designated entity responsible for maintaining and distributing the signed ECTL. Updates to the ECTL are based exclusively on CPA directives and are digitally signed to ensure authenticity. Devices use the signed ECTL to determine which Root CAs are trusted for secure communication.

## Entitlement Enrollment

Entitlement enrollment refers to the policy-governed process of assigning specific permissions to end entities. These permissions define what V2X services a device is authorized to access and what actions it may perform. Common mechanisms for expressing entitlements include the use of PSID and SSP.  Governance frameworks define how these entitlements are granted and validated. 

### Examples - SCMS Entitlement Enrollment 

In the SCMS model, entitlement enrollment begins with identifying the type and intended function of the device (e.g., safety messaging for an OBU). The system assigns appropriate PSIDs and SSPs in accordance with defined policy. These values are included in the Certificate Signing Request (CSR), which is validated by the Registration Authority (RA) prior to certificate issuance. Entitlements are not managed directly by certificate authorities. They are governed by operational policies that define authorized roles and service access.

### Example: CCMS Entitlements

In the CCMS model, entitlement information is reviewed and enforced by subordinate CAs operating under centralized public/ private governance model under the responsibility of the EC. The CPA that defines entitlement policy and ensures consistency across jurisdictions. 

## Certificate Lifecycle
The certificate lifecycle defines processes through which certificates are issued, renewed, and revoked.  Enrollment establishes initial device trust , followed by the issuance of role-specific operational certificates. Governance frameworks must define eligibility criteria and certificate lifecycle requirements. 

#### Example - SCMS Certificate Lifecyle

- Enrollment: Devices are provisioned with an Enrollment Certificate , which authorizes them to participate in SCMS-managed services. A CSR is generated and validated by the Registration Authority (RA). The Enrollment Certificate Authority (ECA) issues the certificate, which serves as a bootstrap credential for requesting role-specific certificates. 

- Issuance: Operational certificates (e.g., pseudonym certificates) are issued based on defined policy. Devices submit requests containing their assigned PSID/SSP entitlements. The issuing CA validates these requests and issues the corresponding certificates based on an approved CP. 

- Revocation: Revocation policies support the removal of certificates due to misbehavior, compromise, or expiration. Pseudonym certificate revocation is managed through CRLs. Root CA revocations require Elector approval and result in CTL updates. 

#### Example - CCMS Certificate Lifecycle

- Enrollment: ITS stations obtain an Enrollment Authorization (EA) certificate, which grants permission to request operational certificates. This enrollment process is managed by the Enrollment Authority and typically involves a one-time provisioning with long-lived credentials tied to the station’s identity and roles.

- Issuance: Operational certificates, including Authorization Tickets (equivalent to pseudonym certificates), are requested from the Authorization Authority (AA). These requests are policy-bound and may include service-specific identifiers. The AA issues short-lived certificates used for day-to-day V2X communications.
- Revocation: The CCMS model does not use Certificate Revocation Lists (CRLs) for ITS stations. Instead, certificates are designed with short validity periods and expire naturally. Removal from the trust framework is handled through expiration and non-renewal, rather than active revocation mechanisms.

