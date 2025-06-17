# Regional Considerations in ITS Cybersecurity 

ITS cybersecurity is shaped by regional differences in legal frameworks, governance models, privacy expectations, and system architecture. These variations influence how trust is established, how anonymity is maintained, and how secure communications are established. The following subsections highlight key governance, trust, and compliance differences that influence regional ITS cybersecurity operations.

## Governance 

There are differences in regional trust models that influence cybersecurity policies and procedures. For example, certificate provisioning to ITS devices is handled differently in Europe vs. North America. These differences impact who can manage certificate policies, who can issue credentials, and how PKI system compliance is enforced.

Europe employs a centralized governance model under the [European Commission](https://commission.europa.eu/index_en). The Certificate Policy Authority (CPA) governs root-level decisions, including Root CA approvals and revocations, scheduling of the [European Certificate Trust List (ECTL)](https://cpoc.jrc.ec.europa.eu/ECTL.html) signing sessions, maintaining policy documents, and management enrollment requests. Roles such as the Trust List Manager (TLM) and [C-ITS point of Contact (CPOC)](https://cpoc.jrc.ec.europa.eu/index.html) operate in accordance with CPA decisions.

North America employs a multi-entity consensus model.  [SCMS Manager](https://www.scmsmanager.org/) for example relies on a group of Electors to establish trust by signing a Certificate Trust List (CTL). Electors follow criteria established through working groups and committees, such as the [Ecosystem Audit Committee (EAC)](https://www.scmsmanager.org/wp-content/uploads/2024/10/SCMS-Manager-EAC-Requirements-v1_0.pdf). In North America, each SCMS Provider is responsible for its own certificate issuance processes, subject to periodic compliance review. 

### Privacy and Anonymity

ITS systems are designed to prevent long-term tracking and identity exposure by using pseudonym certificates, which are short-term certificates that anonymize the link between individual messages and their originating OBUs. The use of short-lived pseudonym certificates is governed by policy. In Europe, privacy is tightly regulated by the [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/). As a result, European C-ITS deployments emphasize strict data minimization and correlation to identity. The use of pseudonym certificates is regulated in the C-ITS Certificate Policy for the CCMS.

In North America, privacy protections are implemented through pseudonymity as well. Certificate are rotated frequently and linkages to vehicle identifies are restricted. 

## Compliance and Audit

In Europe, accredited Root CAs must pass technical and organizational audits  prior to inclusion in the ECTL, as required by the C-ITS Security Policy for CCMS.

In North America, each SCMS Provider selects an independent PKI auditor to validate conformance with SCMS Manager’s Provider Requirements. Providers must maintain certifications (e.g., [ISO 27001](https://www.iso.org/standard/27001) or [TISAX](https://www.enx.com/en-US/tisax/)), and all Certificate Policy (CP) and Certificate Practices Statement (CPS) documents must reflect the approved policy set. 

# Learn More

https://cpoc.jrc.ec.europa.eu/data/documents/E01941_EU%20CCMS_CPA_ToR_Proc_Release-1.1_20241015.pdf

[SCMS-Manager-EAC-Requirements-v1_0.pdf](https://www.scmsmanager.org/wp-content/uploads/2024/10/SCMS-Manager-EAC-Requirements-v1_0.pdf)

[SCMS Manager -  Elector Policy v1.0.docx](https://www.scmsmanager.org/wp-content/uploads/2020/01/Elector-Policy-v1.0.pdf)

[SCMS-Manager-Provider-Requirements-v1_1.pdf](https://www.scmsmanager.org/wp-content/uploads/2024/10/SCMS-Manager-Provider-Requirements-v1_1.pdf)

[Elector-Technical-Specifications-v1.1.pdf](https://www.scmsmanager.org/wp-content/uploads/2020/01/Elector-Technical-Specifications-v1.1.pdf)

[Welcome to TISAX · ENX Portal](https://www.enx.com/en-US/tisax/)

https://www.iso.org/standard/27001





