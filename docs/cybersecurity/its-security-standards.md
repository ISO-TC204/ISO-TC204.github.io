# ITS Security Regulations, Frameworks, Standards and Guidance Documents

Cybersecurity for Intelligent Transport Systems (ITS) is governed by a combination of interoperability frameworks, global standards, and national or local policies. These layers correspond to the model shown in the diagram above and provide the foundation on which ITS-specific technical standards are implemented.

![Standards and Policies](./images/standards and policies.jpg)



## Global Interoperability Frameworks

Global interoperability frameworks establish binding or cross-border rules that ensure consistent cybersecurity obligations for ITS devices and services. They support international trust by aligning requirements for product lifecycle security, update management, and supply chain assurance.

### European Union Cyber Resilience Act (CRA)

The Cyber Resilience Act is a binding regulation that takes effect in the European Union from December 2024. It applies to all digital products, including ITS devices such as On-Board Units (OBUs), Roadside Units (RSUs), and Traffic Management Systems. The CRA requires that products be designed, developed, and maintained with cybersecurity as a core property throughout their lifecycle. Key obligations include security-by-design, secure default configurations, release without known exploitable vulnerabilities, continuous vulnerability remediation, and patching for the full operational lifetime of the product. Products must undergo conformity assessment and display a CE marking before being placed on the EU market. The CRA also mandates vulnerability disclosure processes, incident handling procedures, and supply chain security requirements. This regulation establishes a harmonized baseline of cybersecurity expectations for all ITS products within the EU.

### UNECE Regulations R155 and R156

The United Nations Economic Commission for Europe (UNECE) has issued two vehicle cybersecurity regulations that apply to manufacturers placing vehicles on regulated markets.

- UNECE R155 establishes requirements for a Cybersecurity Management System (CSMS) covering the entire lifecycle of the vehicle, including design, production, and post-production phases. Manufacturers must identify threats, implement mitigations, and demonstrate compliance during type approval.
- UNECE R156 focuses on Software Update Management Systems (SUMS). It requires secure processes for distributing and applying software and firmware updates, including measures for integrity protection, authentication, and auditability.

## Global Standards

Global standards provide a structured methodology for managing cybersecurity risk across organizations and supply chains. They define terminology, risk processes, and assurance methods that are not ITS-specific but serve as a foundation into which ITS standards can be integrated.

### NIST Cybersecurity Framework (CSF)

The NIST Cybersecurity Framework is widely adopted in North America as a risk-based approach to organizing cybersecurity activities. It is structured around six functions: Govern, Identify, Protect, Detect, Respond, and Recover. The CSF guides organizations in setting cybersecurity expectations, performing risk assessments, and aligning operational practices such as patching, monitoring, and incident response. For ITS deployments, state departments of transportation, municipalities, and traffic management centers often use the CSF to structure their security programs and demonstrate alignment with national policy guidance. While the CSF provides a strong governance structure, it does not define technical requirements for ITS protocols or devices, which must be derived from sector-specific standards.

![NIST Functions](images\nist_functions.jpg)

### ISO/IEC 27001

ISO/IEC 27001 is an international standard for establishing an Information Security Management System (ISMS). It requires organizations to identify risks, implement controls, and continuously improve security posture through audits and reviews. Certification to ISO/IEC 27001 demonstrates that an organization has implemented structured governance over information security, including access control, supplier management, and auditing. For Infrastructure Owner-Operators (IOOs), compliance with ISO/IEC 27001 provides assurance to regulators and partners that the organization is managing security in line with global best practices. Like the NIST CSF, it does not address ITS-specific requirements such as certificate validation or message signing, but it provides a foundation into which ITS security standards can be integrated.

## National and Local Policies

National and local governments are responsible for translating global frameworks and standards into enforceable requirements within their jurisdictions. These policies define how international obligations are applied in practice, shaping procurement rules, oversight mechanisms, and operational compliance for agencies, manufacturers, and operators.

In the United States, federal and state agencies frequently use the NIST Cybersecurity Framework and NIST SP 800-53 control catalog as the foundation for transportation cybersecurity programs. For ITS specifically, the Federal Highway Administration (FHWA) has developed ITS Security Control Sets, which tailor these controls to traffic signal controllers, roadside equipment, and transportation management systems. These control sets provide Infrastructure Owner-Operators (IOOs) with prescriptive guidance on how to configure devices, enforce access control, and ensure compliance with national cybersecurity objectives.

In the European Union, IOOs and manufacturers may adopt ISO/IEC 27001 to structure their organizational security programs while also demonstrating compliance with the EU Cyber Resilience Act (CRA). National conformity assessments serve as the mechanism for verifying that products meet CRA obligations before entering the market.



### Certificate Policy (CP) and Certificate Practices Statements (CPS)

While organizational frameworks such as ISO/IEC 27001, the NIST Cybersecurity Framework, or the EU Cyber Resilience Act provide general requirements for governance and risk management, CP and CPS documents translate those high-level obligations into PKI-specific trust rules. They ensure that certificate authorities, enrollment authorities, and authorization services operate within an auditable and enforceable policy structure.

A [Certificate Policy (CP)](certificate-policy.md) defines the conditions under which certificates are issued, managed, and revoked within an ITS Public Key Infrastructure (PKI). Certificate Practice Statements (CPS) provide the operator-specific implementation details that must align with the CP. Together, these documents establish the governance, approval criteria, and enforcement mechanisms that ensure certificates are only issued to eligible devices and entities, are used for authorized purposes, and can be revoked when necessary.

PKI operators must also define how trust anchors, such as Root Certificate Authorities (Root CAs), are authorized, audited, and removed. The structure of trust management can vary by region. In North America, for example, [SCMS deployments](scms-security-policies.md) use a quorum of Electors to manage the Certificate Trust List (CTL). In Europe, [CCMS implementations](ccms-security-policies.md) designate a central Certificate Policy Authority (CPA) to govern the European Certificate Trust List (ECTL). Both models rely on CP and CPS documents to define trust lifecycle rules and to provide assurance through audit and compliance.

### Technical Standards

Organizational frameworks and policy documents define the governance structure for cybersecurity in ITS. Technical standards implement these requirements at the protocol, device, and system level, ensuring that the policies described in frameworks, regulations, and certificate policies are realized in practice. These standards provide the specific technical controls needed for secure communications, device hardening, certificate management, and misbehavior detection.

The following categories group ITS security standards according to their primary function:

- Edge Device Security Standards – define requirements for hardware security, secure boot, tamper detection, and cryptographic modules in OBUs, RSUs, and other ITS equipment.
- Network and Transport Security Standards – specify protocols for protecting confidentiality, integrity, and authentication of ITS data in transit.
- Application Security Standards – govern how ITS messages are formatted, signed, and validated to ensure interoperability and trust across jurisdictions.
- Security Management Standards – establish rules for security management and monitoring, certificate issuance, validation, revocation, misbehavior reporting, and overall PKI operations.

#### Edge Device Security Standards

Use these standards to select, evaluate, or require hardware that supports key storage, secure boot, tamper detection, and cryptographic processing. This supports trusted execution and resilience at the component level.

| Standard                                                     | Document Type | Description                                                  | Stakeholder Role(s)                                          |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| IEEE 802.3                                                   | Standard      | Ethernet standard supporting wired communications among traffic  infrastructure, including support for secure physical connections. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| IEEE 802.1X                                                  | Standard      | Network access control protocol often used in Ethernet-based ITS backhaul  networks to authenticate RSUs and field devices. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| SAE J3101                                                    | Standard      | Defines hardware security requirements for ground vehicles, including  secure boot, key storage, and hardware protections against tampering. | Vehicle Manufacturers and OEMs                               |
| ISO/IEC 19790:2025                                           | Standard      | Requirements for cryptographic modules used to protect sensitive data,  applicable to both software and hardware modules. | Credential Management Authorities                            |
| NIST FIPS 140-3                                              | Standard      | Federal standard for certifying cryptographic modules, used to evaluate  tamper-resistant secure elements. | Credential Management Authorities                            |
| Trusted Platform Module (TPM) / ISO/IEC  11889               | Standard      | Guidance for secure boot and hardware-based trust anchors in automotive  ECUs. | Vehicle Manufacturers and OEMs                               |
| Protection Profile V2X Hardware Security  Module             | Guidance      | Requirements for HSMs in V2X systems with secure key lifecycle and  resistance to physical attacks. | Credential Management Authorities                            |
| Vehicle C-ITS station profile                                | Guidance      | Technical and operational requirements for C-ITS vehicle stations in  Europe. | Vehicle Manufacturers and OEMs                               |
| UNECE R155                                                   | Standard      | Regulation that mandates cybersecurity management systems for vehicle  manufacturers, including hardware risk mitigation. | Vehicle Manufacturers and OEMs                               |
| ISO 24089                                                    | Standard      | Post-production update requirements.                         | Vehicle Manufacturers and OEMs                               |
| UNECE R156                                                   | Regulation    | Mandates secure update systems for vehicles.                 | Vehicle Manufacturers and OEMs                               |
| SAE J3101                                                    | Standard      | Hardware trust anchors and secure boot.                      | Vehicle Manufacturers and OEMs                               |
| Trusted Platform Module (TPM)                                | Standard      | Hardware-based trust and boot integrity.                     | Vehicle Manufacturers and OEMs                               |
| ISO/IEC 19790:2025                                           | Standard      | Cryptographic module security requirements.                  | Application  and Service Providers, Cybersecurity Oversight and Policy Bodies |
| ISO/TR 23786                                                 | Standard      | Security and risk methods for remote access to vehicle systems. | Infrastructure Owner Operators,  Application and Service Providers |
| Vehicle C-ITS station profile                                | Guidance      | Outlines technical and operational requirements for European vehicle ITS  stations. | Application and Service Providers                            |
| Protection Profile V2X Hardware Security  Module             | Guidance      | Requirements for HSMs with secure key lifecycle and physical attack  resistance. | Credential Management Authorities,  Application and Service Providers |
| SAE J2945/1 On-Board System Requirement  for V2V Safety Communications | Standard      | Security requirements for V2V including key provisioning and secure  storage. | Application and Service Providers                            |

#### Network and Transport Security Standards

Apply these standards to enforce confidentiality, integrity, and authentication of data in transit. They define secure sessions for V2X, center-to-field, and backend communications using IP and non-IP protocols.

| Standard                        | Document Type | Description                                                  | Primary Role(s)                                              |
| ------------------------------- | ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| IEEE 1609.3                     | Standard      | Defines networking services for WAVE including IPv6 and WSM. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| ISO 15118                       | Standard      | Secure protocols for EV charging with mutual authentication. | Application and Service Providers                            |
| TLS 1.3 (RFC 8446)              | Standard      | Modern cryptographic protocol for secure backend communications. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| DTLS                            | Standard      | Datagram version of TLS for UDP-based secure transport.      | Application and Service Providers                            |
| ISO 21217                       | Standard      | ITS Station architecture defining network stack.             | Application and Service Providers                            |
| ETSI TS 102 940                 | Standard      | Specifies high-level C-ITS security architecture.            | Credential Management Authorities                            |
| ISO 21186-3                     | Standard      | Secure data exchange guidelines in C-ITS.                    | Application and Service Providers                            |
| IEEE 802.11p / IEEE 802.11-2016 | Standard      | Specifies DSRC/WAVE radio communications at 5.9 GHz for vehicular  networking. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| 3GPP LTE-V2X / NR-V2X           | Standard      | Specifies cellular V2X radio interfaces for sidelink communication. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| IEEE 802.1X                     | Standard      | Network access control protocol used in Ethernet-based ITS backhaul  networks. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| IEEE 802.3                      | Standard      | Ethernet standard supporting wired communications among traffic  infrastructure. | [Infrastructure Owners and Operators](stakeholder-ioo.md), End  Users and Deployers |
| IEEE Std. 1609.3                | Standard      | Defines IPv6, WAVE short message protocol and service advertisement. | [Infrastructure Owners and Operators](stakeholder-ioo.md)  Application and Service Providers |

#### Application Security Standards

These standards define how ITS messages are structured, signed, and validated. They enable cross-vendor and cross-jurisdiction interoperability and ensure message trustworthiness during exchange.

| Standard                             | Document Type | Description                                                  | Primary Role(s)                                              |
| ------------------------------------ | ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SAE J2735                            | Standard      | Defines message formats like BSM, SPaT, MAP.                 | Application and Service Providers                            |
| SAE J2945/x series                   | Standard      | Profiles for message behaviour and signing for V2X.          | Application and Service Providers                            |
| ETSI EN 302 637-2 / -3               | Standard      | Defines CAM and DENM message formats.                        | Application and Service Providers                            |
| ISO 16460                            | Standard      | Harmonized framework for V2X messages.                       | Standards Development Organizations                          |
| ETSI TS 102 894-2                    | Standard      | Common ITS data dictionary.                                  | Application and Service Providers                            |
| ETSI TS 103 097                      | Standard      | European message authentication and trust validation.        | Credential Management Authorities                            |
| ISO 19091                            | Standard      | Harmonized SPaT/MAP message format  (internationalized SAE). | Application  and Service Providers, End Users and Deployers  |
| ISO/TR 21186-1                       | Standard      | Use cases and profiles for secure data exchange.             | Application and Service Providers                            |
| ISO/TS 21184 / ISO/TS 21185          | Standard      | Data and communication profiles for trusted ITS exchange.    | Application and Service Providers,  Credential Management Authorities |
| SAE J2945/4 Road Safety Applications | Standard      | Security requirements for RSZW, LCW messages and digital signature  enforcement. | Application and Service Providers                            |
| SAE J3161/1                          | Standard      | Security for LTE-V2X in light-duty and public safety vehicles. | Application and Service Providers,  Infrastructure Owner Operators |
| SAE J3161/1B                         | Standard      | Extends J3161/1 to non-light-duty vehicles and motorcycles.  | Application and Service Providers                            |
| SAE J3161/1C                         | Standard      | Covers school bus-specific V2V security and safety requirements. | Application and Service Providers                            |
| ISO 19091                            | Standard      | Harmonized SPaT/MAP message format (internationalized SAE)   | Application and Service Providers,  End Users and Deployers  |

#### Security Management Standards

Implement these standards to perform secure management of edge devices, and to issue, validate, and revoke certificates and to manage permissions. 

| Standard                                                     | Document Type | Description                                                  | Primary Role(s)                                              |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| IEEE 1609.2                                                  | Standard      | Defines secure message format and certificates.              | Credential Management Authorities                            |
| IEEE 1609.2.1-2022                                           | Standard      | Certificate lifecycle and permissions enforcement.           | Credential Management Authorities                            |
| ETSI TS 102 941                                              | Standard      | Trust and privacy management for C-ITS.                      | Credential Management Authorities                            |
| ETSI EN 319 411-1                                            | Standard      | Trust service provider requirements for certs.               | Cybersecurity Oversight and Policy Bodies                    |
| C-ITS Point of Contact Protocol                              | Guidance      | CA cross-certification protocol in Europe.                   | Credential Management Authorities                            |
| ETSI TS 102 941  (Trust List Management)                     | Standard      | CTL/CRL processes for European PKI trust  frameworks.        | Credential  Management Authorities                           |
| ETSI TS 102 942                                              | Standard      | Access control rules and cert-based enforcement.             | Credential Management Authorities,  Infrastructure Owner Operators |
| ETSI TS 102 943                                              | Standard      | Encryption and confidentiality services.                     | Credential Management Authorities                            |
| ETSI TS 103 248                                              | Standard      | Pseudonym management and privacy protection in C-ITS.        | Credential Management Authorities,  Application and Service Providers |
| ISO 22320                                                    | Standard      | Incident management processes and protocols.                 | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| SAE J3061 / ISO/SAE 21434                                    | Standard      | Cybersecurity lifecycle and incident response.               | Vehicle Manufacturers and OEMs                               |
| NTCIP Secure Profiles (TLS, SSH)                             | Guidance      | Secure management for center-to-field devices.               | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |
| SAE J3287                                                    | Standard      | Standard for V2X misbehaviour reports.                       | Credential Management Authorities                            |
| ETSI TS 102 941-2                                            | Standard      | European misbehaviour reporting procedures.                  | Credential Management Authorities                            |
| ETSI TS 103 759                                              | Standard      | Standardized misbehaviour message format.                    | Credential Management Authorities                            |
| SCMS ASN.1 Misbehaviour Reports                              | Standard      | Misbehaviour report encoding for SCMS.                       | Credential Management Authorities                            |
| SCMS Misbehaviour Application Spec                           | Standard      | SCMS adjudication and report format.                         | Credential Management Authorities                            |
| SCMS Manager: ASN.1  Specification for Misbehaviour Reports  | Standard      | Defines interoperable ASN.1 encoding for  MBRs.              | Credential  Management Authorities, Infrastructure Owner Operators |
| SCMS Manager: Misbehaviour Report and  Application Specification | Standard      | MBR data format and adjudication rules.                      | Credential Management Authorities,  Infrastructure Owner Operators |
| ETSI TR 103 460                                              | Standard      | Survey of misbehaviour detection techniques.                 | Cybersecurity  Oversight and Policy Bodies, Credential Management Authorities |
| NTCIP / SNMPv3 (RFC 3410)                                    | Standard      | Management protocols with authentication and encryption for ITS field  device communications. | [Infrastructure Owners and Operators](stakeholder-ioo.md)    |

