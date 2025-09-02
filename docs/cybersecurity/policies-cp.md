# PKI Certificate Policy (CP)

Every Public Key Infrastructure (PKI) must be governed by a Certificate Policy (CP). The CP defines the rules under which certificates are issued, managed, and revoked, and establishes the conditions that determine certificate trust. Within ITS PKIs based on IEEE 1609.2, the CP describes the certificate lifecycle, specifying how enrollment, operational use, and revocation are handled. Certificate Practice Statements (CPS) produced by PKI operators provide the implementation details of these requirements and ensure that the CP is applied consistently in practice.  The figure below breaks out many of the common elements found in a CP. 

![Certificate Policy Elements](images\cp-categories.png)

### Enrollment Policies and Procedures

A CP must establish clear rules for how devices and entities are enrolled into the PKI. Enrollment begins with the installation of trusted root and elector certificates, which form the foundation of the trust chain. The policy should require that enrollment connections be secure, typically using physically inspected or otherwise validated communication channels, and that the procedures for provisioning are documented and auditable. Devices must demonstrate that they are in a known good state, free of unauthorized modifications, and running approved versions of firmware or software. Integrity can be confirmed through a trusted hash over installed software and through a self-test that validates the device’s operational readiness. These measures ensure that only eligible and uncompromised devices are introduced into the trust domain.

### Identity Validation Approaches

The CP must define the methods used to validate certificate requests and device eligibility, both at enrollment and throughout the lifecycle of the device. Initial validation may include audits by trusted authorities, declarations from manufacturers, or evaluation by a registration authority. The policy should further describe how validations are refreshed over time to confirm ongoing compliance, with requirements for periodic review or revalidation of entities. 

### Secure Device Enrollment Environment

Policies for enrollment must extend to the environment in which enrollment occurs. The CP should require that enrollment activities be carried out in physically secure facilities, accessible only to authorized technicians and using approved equipment. An activity log must be maintained for all enrollment actions to provide accountability and traceability. Equipment designated for enrollment must be restricted to that purpose and not repurposed for other functions. These provisions protect the enrollment process itself, ensuring that the issuance of initial credentials cannot be compromised through weak physical or procedural controls.

### Device Security Policies

The CP must define baseline security requirements for devices that will hold and use PKI certificates. This begins with key management, requiring secure storage of private keys in tamper-resistant environments and clear rules for key protection. Cryptographic policies should define supported protocols such as TLS, the minimum acceptable algorithm strengths, and requirements for random number generation. Host processor requirements include distinct operational and maintenance states, support for secure boot, and mechanisms for continuous integrity protection. The CP must mandate that all software and firmware updates be cryptographically signed and verified using trusted verification keys before installation. Operating systems should implement access control mechanisms that enforce least privilege, ensuring that only authorized roles can access sensitive functions and that privileged applications are strictly limited. Where hardware security modules (HSMs) are used, the CP should establish minimum assurance levels, with conformance to FIPS 140-2 at Level 2 or Level 3 depending on the risk context. 