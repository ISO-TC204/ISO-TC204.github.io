# Application (A) Security Patterns 

## Pattern A1: Authenticated Messaging

All outbound messages in an ITS system must be cryptographically signed using certificates that encode authorized behaviors. This ensures message integrity, origin authenticity, and accountability. Depending on the communication context, authentication may occur at the message level (e.g., signed BSMs over broadcast) or via mutually authenticated sessions (e.g., secure TCP-based control exchanges using ISO 21177). This pattern enforces trust relationships, supports interoperability, and provides a basis for misbehavior detection and privacy-preserving identity models. Authenticated messaging requires a valid certificate, trusted anchors, and policy-aware enforcement. In privacy-sensitive applications, pseudonym certificates should be used and rotated regularly.

##### Implementation Context

| **Applies To**   | OBUs, RSUs, backend services, cloud-hosted ITS components    |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Message signing, source authentication, session security     |
| **Dependencies** | Certificate provisioning, CTL configuration, signing logic, session establishment (where applicable) |

##### Key Components

| **Component**                | **Role**                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| Certificate-Based Signing    | Ensures message authenticity and integrity; signer must use a certificate with the appropriate entitlements (e.g., PSID/SSP or ITS-AID) |
| Pseudonym Certificates       | Used to protect identity and location privacy, typically for broadcast messages (e.g., BSMs) |
| CTL (Certificate Trust List) | Defines which Root CAs are trusted to issue certificates; devices must reject any certificate not chaining to a listed Root |
| Session Authentication       | For ISO 21177-based communications, mutual authentication and secure channel setup precede message exchange |
| Application Binding Logic    | Checks that the message type matches the permissions encoded in the certificate used to sign it |

##### Implementation Details

- Key Provisioning: Devices must generate or receive cryptographic keys securely. Certificates must be provisioned via a recognized PKI (e.g., SCMS, CCMS) with correct fields (e.g., PSID, SSP, ITS-AID).
- Message Signing: Applications must sign outbound messages with a certificate that explicitly authorizes the message type or service (e.g., an SRM must be signed with a certificate that includes the relevant PSID and SSP).
- Session Setup (ISO 21177): For connection-based communications, devices should implement mutual authentication and secure session negotiation. Signed session setup messages form the basis for trust.
- Policy Validation:  In addition to verifying the certificate’s signature chain, recipients must validate that the certificate includes the correct PSID or ITS-AID for the incoming message, and if applicable, that any SSP constraints are met. Messages that do not meet these criteria must be dropped or logged.
- Pseudonym Use and Rotation: For privacy-sensitive messages, pseudonym certificates should be rotated frequently to prevent long-term tracking. Rotation policies should align with privacy requirements and backend validation capabilities.
- Trust Anchors: All devices must maintain an up-to-date CTL listing trusted Root CAs. Chains that do not resolve to a listed Root must be rejected.
- Certificate Updates: Devices may support secure download of updated certificates or CTLs, either autonomously or during a maintenance cycle. Updates must be validated before use.

##### Example Use Cases

| **Scenario**                   | **Behavior Enforced**                                        |
| ------------------------------ | ------------------------------------------------------------ |
| BSM Broadcast from OBU         | Signed with pseudonym certificate; recipient checks trust chain and message plausibility |
| ISO 21177 Secure Session Setup | Mutual authentication using long-term certificates before data exchange |

##### Related Standards

| Standard        | Purpose                                                      |
| --------------- | ------------------------------------------------------------ |
| IEEE Std 1609.2 | Defines certificate format and digital signature processing  |
| ISO 21177       | Defines secure session establishment for ITS communications  |
| ETSI TS 102 940 | Security architecture for ITS (including trust models)       |
| ETSI TS 103 097 | Certificate format and signing structure for EU V2X communications |
| SAE J2735       | Defines common message types that must be signed (e.g., SRM, BSM, TIM) |

## Pattern A2: Authenticated Message Validation

Ensures that ITS devices only accept messages that are digitally signed with certificates issued by trusted Certificate Authorities (CAs). Each device validates incoming messages by checking the sender's certificate and confirming that it chains to a known Root CA listed in its Certificate Trust List (CTL). This protects against unauthorized or spoofed messages and enforces compliance with trust policy across deployments.

##### Implementation Context

| **Applies To** | OBUs, RSUs, application platforms, infrastructure systems    |
| -------------- | ------------------------------------------------------------ |
| Used For       | Validating the authenticity of signed messages, enforcing trust boundaries |
| Dependencies   | Certificate Trust List (CTL), certificate parsing and signature verification logic, trusted Root CA management |



##### Implementation Details

- Signature Validation: Each received message must be digitally signed. The receiving device extracts the certificate from the message and verifies the cryptographic signature.
- Certificate Path Building: Devices build a trust path from the sender’s certificate through one or more intermediary certificates to a Root CA listed in the CTL.  See Diagram below. 

- CTL Management: Devices must be provisioned with an up-to-date Certificate Trust List. Only certificates chaining to a listed Root CA are accepted.
- Chain Validation Logic: Each certificate in the chain must be valid (not expired or revoked), and its issuer must be the subject of the next certificate in the chain.
- Performance Considerations: Trust chain validation and signature checking must be efficient to support real-time message processing in latency-sensitive ITS environments.

![Trust Chain](C:/Users/bruss/OneDrive - TrustThink, LLC/Projects - TrustThink, LLC/ITS JPO/ISO/ISO Cybersecurity Website/Development/ISO-TC204.github.io/docs/cybersecurity/images/trustChain.jpg)

##### Example Use Cases

| Scenario                                      | Behavior Enforced                                            |
| --------------------------------------------- | ------------------------------------------------------------ |
| RSU validates Signal Request Message (SRM)    | RSU verifies that an SRM was signed by a certificate chaining to a trusted Root CA before granting signal priority. |
| Field technician configures device onboarding | Installer confirms the OBU’s certificate chains to an accepted CA before the device is accepted into the deployment. |



##### Related Standards

| Standard          | Purpose                                                      |
| ----------------- | ------------------------------------------------------------ |
| IEEE Std 1609.2   | Defines certificate formats, digital signature algorithms, and trust chain requirements |
| IEEE Std 1609.2.1 | Updates certificate and CTL handling for multi-jurisdictional V2X deployments |
| ETSI TS 103 097   | Defines certificate and message signature format for V2X communications (EU) |
| ETSI TS 102 941   | Describes trust management and Root CA configuration (EU)    |

## Pattern A3: Certificate-bound application authorization

Restricts ITS application behavior to only those actions explicitly authorized through certificate entitlements. Applications are identified using Provider Service Identifiers (PSIDs) or ITS Application Identifiers (ITS-AIDs) with permissions further refined through Service-Specific Permissions (SSPs). These constraints are enforced by both senders and receivers to prevent unauthorized use of ITS messages or services. This pattern enforces least privilege and supports federated trust enforcement.  

##### Implementation Context

| **Applies To**   | OBUs, RSUs, application platforms, infrastructure systems    |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Message-level authorization, application permission enforcement, service access control |
| **Dependencies** | Certificate profiles including PSID/SSP fields, sender and receiver enforcement logic, deployment policies |

##### Key Components

| **Component**                  | **Role**                                                     |
| ------------------------------ | ------------------------------------------------------------ |
| PSID / ITS-AID in Certificates | Identifies authorized ITS application (e.g., SRM, TIM)       |
| Service-Specific Permissions   | Encodes additional constraints based on role, region, vehicle type, etc. |
| Sender Enforcement Logic       | Restricts outbound messages to match permitted certificates and services |
| Receiver Validation Logic      | Ensures incoming messages match expected application entitlements |

##### Implementation Details

- Certificate Configuration: SCMS/CCMS must issue certificates with valid PSID and optional SSP values appropriate to the role of the device.
- Sender Behavior: Devices must select certificates that match the intended application. This may require runtime certificate selection or predefined associations.
- Receiver Behavior: RSUs or backend systems must inspect both PSID and SSP fields before processing messages. Rejected messages should be logged and discarded.
- Local Policy Filters: RSUs or backend systems may apply operational policies to further constrain behavior (e.g., only vehicles from authorized agencies may request signal priority).
- Operational Context: Devices may carry multiple certificates, each with different entitlements. Runtime logic must select the appropriate credential based on the current application and role.

##### Example Use Cases

| Scenario                     | Behavior Enforced                                            |
| ---------------------------- | ------------------------------------------------------------ |
| Public Transit SRMs          | Only transit vehicles with authorized certificates can request signal priority |
| Emergency Hazard Warnings    | Only certified emergency services may broadcast hazard notifications |
| Regional Access Restrictions | Certificates scoped by jurisdiction to restrict message validity to local areas |
|                              |                                                              |

##### Related Standards

| Standard        | Purpose                                                      |
| --------------- | ------------------------------------------------------------ |
| IEEE Std 1609.2 | Certificate formats, application identifiers, and SSP fields |
| SAE J2735       | Application-layer message definitions (e.g., SRM, BSM, TIM)  |
| ETSI TS 102 941 | Authorization framework for ITS applications (EU)            |
| ETSI TS 103 097 | Certificate structure and permissions for V2X (EU)           |

