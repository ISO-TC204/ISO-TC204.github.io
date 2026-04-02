# ITS Interoperability

ITS interoperability requires that products and systems from different vendors, regions, and domains can exchange, interpret and trust data in a consistent manner.  This depends on alignment across multiple layers, including message formats, security mechanisms, credential policies, and communication protocols. These layers must operate consistently even when systems are deployed across different regions, organizations, and governance models.

## Message and Data Interoperability

Systems must encode, transmit, and interpret messages consistently. This includes agreement on message structure, field definitions, data types, and semantic meaning so that information exchanged between systems is understood in the same way.

Standards define these message sets and their usage. For example:

- SAE J2735 defines common V2X message structures such as Basic Safety Messages (BSM), Signal Phase and Timing (SPaT), and MAP messages.
- SAE J2945/x documents define application-level requirements and expected behaviour associated with those messages.
- CTI 4501 profiles define how message sets are applied in specific deployments, such as connected intersections.

If systems interpret message fields differently, apply inconsistent encoding rules, or assign different meanings to the same data, messages may be processed incorrectly or discarded. Interoperability at this layer depends on consistent implementation of message definitions and their associated application rules.

### Secure Data Structures

Systems must implement security services using compatible data structures, encoding rules, and certificate handling so that messages can be authenticated, validated, and, where applicable, decrypted across implementations.

Standards define how security is applied to messages. For example:

- IEEE 1609.2 defines core security services, including `SignedData` and `EncryptedData` structures, signature formats, and certificate usage.
- ETSI TS 103 097 defines a regional profile of these structures, including security headers, certificate formats, and message profiles

These standards define how messages are secured and interpreted across systems, including how messages are wrapped (such as signed or encrypted), how data is encoded (for example using ASN.1 with canonical encoding rules), and how certificates are included, referenced, and validated.

Interoperability depends on consistent implementation of these elements. Differences in encoding rules, signature structures or algorithms, or certificate handling including variations in format or trust models, can prevent systems from validating or processing messages correctly.

## Credential and Trust Interoperability

Systems must be able to establish trust in credentials issued by different authorities, organizations, or jurisdictions. This includes validating certificates, understanding their scope of use, and determining whether they should be accepted within a given deployment.

Standards define how this trust is established and managed. For example, IEEE 1609.2.1 defines interfaces for certificate handling and distribution, while IEEE 1609.2.2 defines mechanisms for establishing trust between independent credential management systems. In practice, this is implemented through frameworks such as SCMS and CCMS, which define certificate policies, trust models, and governance processes.

Interoperability at this layer depends on alignment of trust anchors, certificate policies, and validation rules. Systems must not only be able to process certificates, but also determine whether those certificates represent entities that are trusted within the local context.

## Authorization and Application Interoperability

Systems must interpret application identifiers and associated permissions consistently so that messages are processed according to their intended use. Even when a message is valid and the sender’s certificate is trusted, the receiving system must still determine whether the sender is permitted to perform the action associated with that message.

Standards define how permissions are expressed and enforced. For example, SAE J2945/5 defines Service Specific Permissions (SSPs) and their use within applications, while SAE J3268 defines Provider Service Identifiers (PSIDs) and their assignment to specific ITS services.

Interoperability at this layer depends on consistent interpretation of these identifiers and permissions. Systems must evaluate whether a message is authorized within its declared application context, based on locally enforced policies.

## Communication and Transport Interoperability

Systems must be able to establish and maintain communication using compatible networking, radio, and transport protocols. This includes how messages are routed, how channels are managed, and how secure sessions are established.

Standards define these communication layers. For example, IEEE 1609.3 specifies networking services for V2X communications. SAE J3161 defines profiles for LTE-V2X communications, and ISO 21177 specifies the use of TLS to secure communications between ITS stations and backend systems.

Interoperability at this layer depends on alignment of communication protocols, channel usage, and transport security configurations. Systems must support compatible mechanisms for message exchange and session establishment. If communication protocols, radio configurations, or transport security mechanisms are not aligned, systems will be unable to exchange data, regardless of whether higher-layer message, security, or trust mechanisms are correctly implemented.

## Cross-Domain and Regional Interoperability

Systems must operate across organizational, regional, and policy boundaries where different credential management systems and governance models are in place. This includes validating and trusting messages originating from external domains that may follow different certificate policies, issuance processes, and trust frameworks.

Regional implementations differ in governance, privacy requirements, and compliance models. For example, Europe uses a more centralized trust model coordinated through the European Certificate Trust List (ECTL) and CPOC, while North America uses a multi-entity model where trust is established through Certificate Trust Lists (CTLs) managed by SCMS participants. These differences affect how credentials are issued, how trust is established, and how policies are enforced across domains.

Standards and frameworks define how this interoperability can be achieved. IEEE 1609.2.2 provides mechanisms for establishing trust between independent security domains using structures such as Certificate Trust Lists (CTLs) and associated trust permissions. Regional implementations include frameworks such as SCMS in North America and CCMS in Europe, along with supporting mechanisms such as CPOC for coordinating trust relationships across European deployments .

Interoperability at this layer depends on how trust is extended between domains. Differences in governance models, certificate policies, privacy requirements, and audit processes influence how credentials are issued and validated. Systems must account for these differences when determining whether to trust external certificates and how to apply them. Systems may operate with different certificate authorities, policy frameworks, and credential formats, but must still be able to validate and trust messages across these boundaries in a controlled and predictable manner.

IEEE 1609.2.2 introduces a framework for establishing trust across security domains that operate under different policies, using the Certificate Trust List (CTL). The CTL enumerates Root Certificate Authorities (Root CAs) that the local system recognizes as trusted. Trust is extended by placing the hashed identifier of a Root CA (HashedId32) onto the CTL. This signals to end entities in the local domain that certificates chaining back to the listed Root CA are recognized and valid for use, as long as the trust conditions associated with that Root CA are met.

### Multi Jurisdictional Trust (IEEE 1609.2.2)

IEEE 1609.2.2 adds the ability to assign trust permissions to each Root CA listed on the CTL. These permissions define exactly what a receiving end entity should trust when it encounters a certificate from an external domain. Permissions can be specified in several ways:

- By listing which ITS-AID/PSID are trusted or untrusted.

- By stating whether fields like opOrgId or encryptionKey in the certificate should be used.

These permissions provide fine-grained control. For example, an SCMS Manager can trust a foreign Root CA for the purpose of receiving basic safety messages but indicate that it does not trust the opOrgId field due to differences in organizational vetting procedures. This model allows a system operator to define exactly what it accepts from each external trust domain. The receiving entity uses these trust permissions to evaluate messages and ensure that certificates are only accepted for the purposes explicitly permitted by the local CTL.

IEEE 1609.2.2 enables interoperability between policy domains without requiring them to adopt identical certificate enrolment and other policies. It provides a mechanism for trust to be extended in a controlled and explicit way, supporting cross-border or cross-organizational communication while respecting local assurance requirements.
