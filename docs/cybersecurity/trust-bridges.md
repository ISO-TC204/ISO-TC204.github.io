# Interoperability Strategies for ITS Security 

ITS interoperability refers to the ability of systems that use different certificate authorities or policy frameworks to securely validate and exchange messages. As connected vehicles and infrastructure begin to operate across jurisdictions and trust domains, enabling interoperability becomes essential for safe and reliable communication. This page introduces foundational strategies for achieving interoperability between independent PKIs supporting ITS. 

## The Need for ITS Interoperability

As ITS are increasingly deployed across cities, regions, and national borders, secure communication between vehicles and infrastructure must be maintained even when those systems operate under different governance models and trust frameworks. Interoperability ensures that connected devices, for example vehicles crossing jurisdictional lines or roadside units supporting multiple jurisdictions, can recognize and validate each other’s messages reliably.

Interoperability becomes especially important in contexts where operational coordination spans multiple entities. This includes for example metropolitan planning organizations managing smart intersections, regional agencies operating roadside units, or national governments deploying connected vehicle credentials. Each may have its own policies, security credentials, and trust authorities, but their systems must work together seamlessly. Without an interoperability framework, safety-critical messages, such as vehicle warnings or signal phase and timing information may go unrecognized or untrusted. 

Effective strategies for achieving interoperability include establishing mutual trust relationships, using common message standards, aligning policy enforcement, and supporting devices that can operate within multiple trust domains. The goal is to ensure that messages originating from one domain can be validated and trusted by another without sacrificing security or requiring proprietary solutions. The following sections outline technical and policy-based approaches that support interoperability in the real world, including the role of standards like IEEE 1609.2.2 and the harmonization of certificate policies across trust domains.

## Multi-Jurisdictional Trust with IEEE 1609.2.2

IEEE 1609.2.2 introduces a framework for establishing trust across security domains that operate under different policies, using the Certificate Trust List (CTL). The CTL enumerates Root Certificate Authorities (Root CAs) that the local system recognizes as trusted. Trust is extended by placing the hashed identifier of a Root CA (HashedId32) onto the CTL. This signals to end entities in the local domain that certificates chaining back to the listed Root CA are recognized and valid for use, as long as the trust conditions associated with that Root CA are met. 

IEEE 1609.2.2 adds the ability to assign trust permissions to each Root CA listed on the CTL. These permissions define exactly what a receiving end entity should trust when it encounters a certificate from an external domain. Permissions can be specified in several ways:

By listing which Provider Service Identifiers (PSIDs) are trusted or untrusted.

By stating whether fields like opOrgId or encryptionKey in the certificate should be used.


These permissions provide fine-grained control. For example, an SCMS Manager can trust a foreign Root CA for the purpose of receiving basic safety messages but indicate that it does not trust the opOrgId field due to differences in organizational vetting procedures. This model allows a system operator to define exactly what it accepts from each external trust domain. The receiving entity uses these trust permissions to evaluate messages and ensure that certificates are only accepted for the purposes explicitly permitted by the local CTL. 

IEEE 1609.2.2 enables interoperability between policy domains without requiring them to adopt identical policies. It provides a mechanism for trust to be extended in a controlled and explicit way, supporting cross-border or cross-organizational communication while respecting local assurance requirements.

