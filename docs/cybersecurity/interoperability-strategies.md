# Interoperability Strategies for ITS Security 

## Regional Considerations: Understand regional differences in regulation and approach 

While ITS cybersecurity standards aim for global interoperability, implementation often varies across regions due to different legal frameworks, privacy expectations, governance models, and deployment architectures. These differences directly affect how trust is established, how permissions are granted, and how secure communications are managed. Understanding regional approaches, such as the SCMS model in North America and the C-ITS Trust Model in Europe is important for organizations deploying cross-border systems or designing interoperable ITS devices and services.  These differences must be taken into account when designing systems intended for multi-regional interoperability.

### Governance 

There are differences in regional trust models that influence cybersecurity policies and procedures. For example, certificate provisioning to ITS devices is handled differently in Europe vs. North America. These differences impact who can manage certificate policies, who can issue credentials, and how PKI system compliance is enforced.

Europe employs a centralized governance model under the [European Commission](https://commission.europa.eu/index_en). The Certificate Policy Authority (CPA) governs root-level decisions, including Root CA approvals and revocations, scheduling of the [European Certificate Trust List (ECTL)](https://cpoc.jrc.ec.europa.eu/ECTL.html) signing sessions, maintaining policy documents, and management enrollment requests. Roles such as the Trust List Manager (TLM) and [C-ITS point of Contact (CPOC)](https://cpoc.jrc.ec.europa.eu/index.html) operate in accordance with CPA decisions.

North America employs a multi-entity consensus model.  [SCMS Manager](https://www.scmsmanager.org/) for example relies on a group of Electors to establish trust by signing a Certificate Trust List (CTL). Electors follow criteria established through working groups and committees, such as the [Ecosystem Audit Committee (EAC)](https://www.scmsmanager.org/wp-content/uploads/2024/10/SCMS-Manager-EAC-Requirements-v1_0.pdf). In North America, each SCMS Provider is responsible for its own certificate issuance processes, subject to periodic compliance review. 

### Privacy and Anonymity

ITS systems are designed to prevent long-term tracking and identity exposure by using pseudonym certificates, which are short-term certificates that anonymize the link between individual messages and their originating OBUs. The use of short-lived pseudonym certificates is governed by policy. In Europe, privacy is tightly regulated by the [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/). As a result, European C-ITS deployments emphasize strict data minimization and correlation to identity. The use of pseudonym certificates is regulated in the C-ITS Certificate Policy for the CCMS.

In North America, privacy protections are implemented through pseudonymity as well. Certificate are rotated frequently and linkages to vehicle identifies are restricted. 

### Compliance and Audit

In Europe, accredited Root CAs must pass technical and organizational audits  prior to inclusion in the ECTL, as required by the C-ITS Security Policy for CCMS.

In North America, each SCMS Provider selects an independent PKI auditor to validate conformance with SCMS Manager’s Provider Requirements. Providers must maintain certifications (e.g., [ISO 27001](https://www.iso.org/standard/27001) or [TISAX](https://www.enx.com/en-US/tisax/)), and all Certificate Policy (CP) and Certificate Practices Statement (CPS) documents must reflect the approved policy set. 



## The Need for ITS Interoperability

ITS interoperability refers to the ability of systems that use different certificate authorities or policy frameworks to securely validate and exchange messages. As connected vehicles and infrastructure begin to operate across jurisdictions and trust domains, enabling interoperability becomes essential for safe and reliable communication. 

As ITS are increasingly deployed across cities, regions, and national borders, secure communication between vehicles and infrastructure must be maintained even when those systems operate under different governance models and trust frameworks. Interoperability ensures that connected devices, for example vehicles crossing jurisdictional lines or roadside units supporting multiple jurisdictions, can recognize and validate each other’s messages reliably.

Interoperability becomes especially important in contexts where operational coordination spans multiple entities. This includes for example metropolitan planning organizations managing smart intersections, regional agencies operating roadside units, or national governments deploying connected vehicle credentials. Each may have its own policies, security credentials, and trust authorities, but their systems must work together seamlessly. Without an interoperability framework, safety-critical messages, such as vehicle warnings or signal phase and timing information may go unrecognized or untrusted. 

Effective strategies for achieving interoperability include establishing mutual trust relationships, using common message standards, aligning policy enforcement, and supporting devices that can operate within multiple trust domains. The goal is to ensure that messages originating from one domain can be validated and trusted by another without sacrificing security or requiring proprietary solutions. The following sections outline technical and policy-based approaches that support interoperability in the real world, including the role of standards like IEEE 1609.2.2 and the harmonization of certificate policies across trust domains.

## Multi-Jurisdictional Trust with IEEE 1609.2.2

IEEE 1609.2.2 introduces a framework for establishing trust across security domains that operate under different policies, using the Certificate Trust List (CTL). The CTL enumerates Root Certificate Authorities (Root CAs) that the local system recognizes as trusted. Trust is extended by placing the hashed identifier of a Root CA (HashedId32) onto the CTL. This signals to end entities in the local domain that certificates chaining back to the listed Root CA are recognized and valid for use, as long as the trust conditions associated with that Root CA are met. 

IEEE 1609.2.2 adds the ability to assign trust permissions to each Root CA listed on the CTL. These permissions define exactly what a receiving end entity should trust when it encounters a certificate from an external domain. Permissions can be specified in several ways:

- By listing which ITS-AID/PSID are trusted or untrusted.

- By stating whether fields like opOrgId or encryptionKey in the certificate should be used.



These permissions provide fine-grained control. For example, an SCMS Manager can trust a foreign Root CA for the purpose of receiving basic safety messages but indicate that it does not trust the opOrgId field due to differences in organizational vetting procedures. This model allows a system operator to define exactly what it accepts from each external trust domain. The receiving entity uses these trust permissions to evaluate messages and ensure that certificates are only accepted for the purposes explicitly permitted by the local CTL. 

IEEE 1609.2.2 enables interoperability between policy domains without requiring them to adopt identical certificate enrollment and other policies. It provides a mechanism for trust to be extended in a controlled and explicit way, supporting cross-border or cross-organizational communication while respecting local assurance requirements.

