# Network and Transport Related Functions

## Pattern N1: Secure Backend Communications

Secures communication between ITS field devices (e.g., RSUs, OBUs) and backend services (e.g., TMCs, certificate servers, monitoring platforms) using strong encryption and mutual authentication. Depending on the underlying protocol, Transport Layer Security (TLS) or Datagram Transport Layer Security (DTLS) is applied to protect data in transit. TLS 1.3 should be used for TCP-based interfaces (e.g., configuration commands, certificate provisioning), while DTLS is suited for UDP-based traffic such as low-latency telemetry or event reporting. All sessions must use certificates issued by a recognized PKI, and mutual authentication should be enforced to ensure trust on both ends of the connection. 

This pattern ensures confidentiality, integrity, and authenticity of data flows across the ITS environment, and mitigates risk associated with spoofing, tampering, and unauthorized control of devices.

##### **Key Components**

| **Component**                       | **Role**                                                     |
| ----------------------------------- | ------------------------------------------------------------ |
| TLS 1.3 Stack                       | Provides encryption and mutual authentication over TCP-based sessions |
| DTLS 1.3 Stack                      | Supports secure, low-latency communication over UDP          |
| PKI-issued Device Certificates      | Used to authenticate both ends of a session                  |
| Cipher Suite Configuration          | Enforces strong algorithms and disables outdated or insecure ciphers |
| Certificate Revocation Lists (CRLs) | Ensures devices reject expired or revoked certificates       |

##### **Example Use Cases**

| **Scenario**                           | **Behavior Enforced**                                        |
| -------------------------------------- | ------------------------------------------------------------ |
| RSU sends telemetry over DTLS          | RSU establishes secure DTLS session with backend, encrypts payload, and authenticates server |
| Backend server configures field device | Server initiates TLS 1.3 session with RSU, both authenticate using device certificates |
| OBU uploads misbehavior report         | OBU uses DTLS to send a signed and encrypted report to backend with validated identity |

##### **Related Standards and NIST Controls**

| **Standard / Control** | **Purpose**                                                  |
| ---------------------- | ------------------------------------------------------------ |
| IEEE 1609.3 / 1609.2.1 | Defines V2X networking and messaging protocols and certificate usage for ITS |
| ISO 21177              | Secure session establishment between ITS stations            |
| NIST SP 800-52 Rev. 2  | Guidelines for TLS configuration and algorithm selection     |
| NIST SP 800-53 Rev. 5  | Cryptographic protection, mutual auth, integrity, and session security |

## Pattern N2: Secure Session Establishment Using ISO 21177

ITS stations frequently require persistent, authenticated communication sessions across trusted links. These sessions must be established in a standards-compliant manner to ensure confidentiality, authenticity, and resilience. **ISO 21177** provides the formal specification for initiating, negotiating, and managing secure sessions between ITS stations. It defines how to authenticate peers using X.509 certificates, manage session lifetimes, and recover from abnormal session conditions.

During session establishment, each station must present a certificate issued by a trusted CA, validated against local policy and Certificate Trust Lists (CTLs). Sessions should be terminated or rejected if certificate validation fails (e.g., expired, revoked, untrusted root). The standard also defines session renegotiation procedures, enabling secure re-authentication when session conditions change.

ITS operators must ensure all deployed devices that support station-to-station communications implement ISO 21177, and procurement specifications should include support for the standard. 

##### Implementation Context

| **Applies To**   | OBUs, RSUs, Roadside and Central Systems using session-based communication |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Establishing and managing secure, persistent sessions over TCP/IP. |
| **Dependencies** | Valid X.509 certificates, CTL availability, PKI integration, ISO 21177 compliance |

##### Key Components

| **Component**              | **Role**                                                     |
| -------------------------- | ------------------------------------------------------------ |
| ISO 21177 Session Protocol | Negotiates session keys and verifies peer identity using digital certificates |
| X.509 Certificates         | Provide cryptographic identity for session authentication    |
| Certificate Trust List     | Local list of trusted Root and Intermediate CAs for validating peers |
| Session Renegotiation      | Re-establishes trust and session keys periodically or upon failure |

##### Example Use Cases

| **Scenario**                      | **Behavior Enforced**                                        |
| --------------------------------- | ------------------------------------------------------------ |
| RSU-OBU Secure Session            | An RSU validates an OBU’s certificate and initiates a secure ISO 21177 session |
| Session Expiry Handling           | An RSU terminates and renegotiates a session when a certificate expires or is revoked |
| Backend-Controlled Session Policy | A backend management system sets session duration and requires periodic renegotiation |

##### Related Standards

| **Standard** | **Purpose**                                                  |
| ------------ | ------------------------------------------------------------ |
| ISO 21177    | Defines secure session negotiation and management for ITS stations |
| IEEE 1609.2  | Provides certificate structure and signing requirements      |
| ISO 21217    | Reference architecture for ITS station communication functions |











- 