# Certificate Management Authorities

Certificate Management Authorities (CMAs) are responsible for operating and governing the trust services that enable secure communications in Intelligent Transport Systems (ITS). These authorities ensure that certificates are issued only to eligible entities, that trust anchors are properly maintained, and that trust within their jurisdictions is supported through consistent application of Certificate Policies (CPs) and Certificate Practice Statements (CPSs).

## Governance and Policy Alignment

Every PKI operates under a [Certificate Policy (CP)](certificate-policy) that defines the acceptable uses, validation rules, and lifecycle requirements for certificates. A corresponding CPS documents how the Provider implements these rules in practice. The CP and CPS must align with applicable global standards (e.g., IEEE 1609.2, ETSI TS 102 941) and regional trust frameworks (e.g., [SCMS](scms-security-policies) or [CCMS](ccms-security-policies)) to ensure interoperability.

PKI Providers are responsible for:

- Establishing and enforcing eligibility criteria for certificate enrollment.
- Maintaining auditable procedures for Root CA approval, suspension, and removal.
- Coordinating with other PKI Providers and policy authorities to support cross-jurisdiction trust where require

## Operational Responsibilities

In addition to governance, Providers perform day-to-day trust management tasks that ensure the smooth functioning of the ITS PKI ecosystem:

- Trust List Management: Updating and publishing trust lists that identify valid Root CAs. These lists must be encoded, signed, and distributed reliably to relying parties.
- Certificate Validation: Ensuring that certificate requests are properly validated, including enrollment and operational certificate types.
- Revocation Management: Publishing Certificate Revocation Lists (CRLs) or applying equivalent revocation mechanisms, and ensuring timely propagation of revocation information.
- Audit and Compliance: Supporting external audits of compliance with CP and CPS requirements, and maintaining evidence of operational integrity.

## Roles in Certificate Trust Management

The table below outlines key roles that may exist within a PKI Provider 

| Example Role | Role Description                                             |
| ------------ | ------------------------------------------------------------ |
| Root CA      | Serves as the top-level trust anchor, issuing certificates to subordinate CAs and enforcing strict policies to ensure the security and integrity of the entire certificate chain. |
| TLM          | Responsible for maintaining and updating the list of trusted root certificates, ensuring that only valid and compliant Root Certification Authorities are recognized by relying parties. |
| CPA          | Responsible for establishing and maintaining the overarching policies and standards that govern certificate issuance, usage, and management throughout the system, and decisions on applications and revocations of Root CA's in the CCMS (ECTL). |
| CPOC         | Acts a the technical interface to a TLM, validates certificate submissions and ensures compliance with operational policies. |
| ECTL         | Provides the encoded and signed electronic trust list used by relying parties to verify which Root Certificate Authorities are trusted at a given time. |

## Assurance and Interoperability

PKI Provider activities must be transparent, auditable, and technically robust. Independent assessments should be conducted regularly to verify compliance with the CP. Where multiple PKIs must interoperate, Providers play a critical role in coordinating cross-certification, harmonizing policies, and ensuring that relying parties can validate certificates from foreign jurisdictions.