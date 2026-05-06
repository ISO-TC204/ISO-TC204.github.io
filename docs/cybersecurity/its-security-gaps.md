# Identify and Remediate Common ITS Security Gaps

Determine where ITS systems fail to correctly validate data, enforce authorization, and apply trust decisions during operation. When these functions are implemented incorrectly or behave inconsistently, systems may accept invalid inputs or apply unintended actions. Use this section to identify common security gaps, understand why they occur, and apply the required controls to ensure correct, consistent, and reliable system behaviour.

## 1. Message Trust and Validation

Standards such as IEEE 1609.2 and ETSI TS 103 097 define how V2X messages are encoded, signed, and validated. Systems rely on these structures to verify message integrity, authenticate message sender, and determine whether a message should be processed. Validation must be performed consistently across implementations. Differences in certificate handling, encoding, algorithm support, or trust anchor configuration, or policy enforcement can cause messages to be incorrectly accepted or rejected.  

| 1a. Messages Incorrectly Accepted or Rejected Due to Expired Certificates | In some ITS workflows, messages are not processed immediately after they are generated. Data may be stored, forwarded, or validated later by backend systems, logging platforms, or external services. In these cases, systems must determine whether a message was valid at the time it was created, not just at the time it is received. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If this distinction is not handled correctly, a signed message may be accepted even though the certificate used to generate the signature was not valid at the time of signing, or a valid message may be rejected because the certificate has since expired. This typically occurs when validation is performed only against the current system time rather than the message creation time. |
| Recommended Mitigation                                       | Systems should validate certificates using the appropriate time context, such as a trusted signature timestamp or equivalent mechanism that reflects when the message was generated. Validation logic should distinguish between the time of signing and the time of verification to ensure consistent and correct processing. |

| 1b.  Unauthorized Messages Accepted Due to Missing or Stale Revocation Data | Certificates may be revoked before their expiration due to compromise, misbehaviour, or administrative action. Revocation information is distributed through mechanisms such as Certificate Revocation Lists (CRLs) or equivalent trust framework updates, which must be regularly obtained and enforced by receiving systems. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If revocation information is not available, not current, or not checked during validation, a message may be accepted even though the signing certificate has been revoked. This can occur when systems fail to update revocation data, do not enforce revocation checks, or operate in disconnected environments without compensating controls. |
| Recommended Mitigation                                       | Systems should ensure that revocation information is available and up to date, and that it is checked during message validation. This includes retrieving revocation data from the applicable trust framework, validating its integrity, and enforcing it consistently when processing messages. |

| 1c. Valid Messages Rejected Due to Encoding Differences Between Systems | Signed messages are generated over a specific byte representation of data. Standards such as IEEE 1609.2 define how data structures are encoded before signing, but implementation differences or incomplete specifications can lead to variations in how the same logical message is represented. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If two systems encode the same logical message differently, signature verification will fail even though the underlying content is identical. This can occur when encoding rules are not clearly defined or not implemented consistently, resulting in messages being incorrectly rejected. |
| Recommended Mitigation                                       | Deployments should define canonical encoding rules for all signed data structures. Systems should generate and verify messages using the same encoding rules to ensure that identical data produces identical byte representations for signing and validation. |

| 1d. Message Rejection Due to Unsupported Cryptographic Algorithm Profiles | ITS message validation depends on both the sending and receiving systems supporting the same cryptographic algorithms. Deployment profiles define which signature algorithms, curves, and hash functions are used for message generation and validation. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If a message is signed using an algorithm that is not supported by the receiving system, the message cannot be validated and may be rejected. This can occur when systems implement different deployment profiles or are not configured to use the same set of approved algorithms. |
| Recommended Mitigation                                       | Deployment specifications should define the cryptographic algorithms to be used for message generation and verification. Systems should generate and verify signed messages using only the algorithms defined by the applicable deployment profile. |

| 1e. Message Rejection Due to Unresolvable Signer Identity | Signed messages reference the identity of the sender through a certificate or identifier that allows the receiver to obtain the corresponding public key. This may require access to locally stored certificates, cached data, or external trust infrastructure. |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| Condition                                                 | If the receiving system cannot obtain or reconstruct the public key associated with the signer, the message cannot be validated and may be rejected. This can occur when required certificates are missing, identifiers cannot be resolved, or supporting certificate distribution mechanisms are not available. |
| Recommended Mitigation                                    | Systems should ensure that signer credentials can be resolved during message validation. This may include maintaining local certificate stores, supporting certificate distribution mechanisms, and ensuring that identifiers used in signed messages can be mapped to verifiable public keys. |

| 1f. Message Rejection Due to Invalid or Incomplete Certificate Chain | After obtaining the signer’s certificate, the receiving system must validate it against a chain of trust leading to a trusted root certificate. This process depends on correctly configured trust anchors and availability of intermediate certificates. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If the certificate chain cannot be validated to a trusted root, the authenticity of the message cannot be established and the message may be rejected. This can occur due to missing intermediate certificates, incorrect trust anchor configuration, or mismatches between trusted roots and the certificates in use. |
| Recommended Approach                                         | Systems should validate certificate chains against a correctly configured set of trust anchors and ensure that all required intermediate certificates are available. Trust stores should be maintained and updated in accordance with the applicable trust framework. |



## 2. Authorization and Permission Enforcement

Authentication confirms who sent a message, but it does not determine what that sender is allowed to do. Systems must evaluate permissions associated with identities, certificates, or applications before accepting or acting on a message. If authorization is not enforced consistently, systems may accept messages or requests from entities that are authenticated but not permitted to perform the requested action.

| 2a. **Unauthorized Messages Accepted from Authenticated but Unauthorized Senders** | ITS systems often rely on certificates or credentials to authenticate message senders. These credentials may be valid and trusted, but they can represent entities with different roles, privileges, or application permissions. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If authorization is not evaluated after authentication, a system may accept a message or request from an entity that is authenticated but does not have the required permissions. |
| Recommended Mitigation                                       | Systems should evaluate the permissions associated with the authenticated identity or signing credential before accepting or processing messages. Authorization decisions should be based on defined roles, application identifiers, or policy rules enforced by the receiving system. |



## 3. Secure Communication and Session Establishment

ITS systems rely on secure communication protocols such as TLS (e.g., ISO 21177) to protect data exchanged between infrastructure, backend systems, and devices. Establishing a secure session requires both systems to support compatible protocols, credential formats, and cryptographic configurations.

| 3a. Connection Failures Due to Incompatible TLS Configurations | Secure communication between systems is typically established using TLS profiles defined by standards such as ISO 21177. These profiles specify supported protocol versions, cipher suites, and cryptographic algorithms that must be negotiated during session establishment. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If two systems do not support compatible TLS configurations, a secure session cannot be established. This can occur when systems implement different protocol versions, cipher suites, or cryptographic settings, resulting in failed negotiation during the TLS handshake. |
| Recommended Mitigation                                       | Systems should implement the TLS profiles defined by the applicable deployment or regional specification. Configuration should ensure alignment of supported protocol versions, cipher suites, and cryptographic algorithms. Systems should also log and monitor failed session establishment attempts to support troubleshooting and operational visibility. |

| 3b. Connection Failures Due to Incompatible Credential Formats | Mutual authentication during secure session establishment requires both systems to present and validate credentials. Depending on the deployment, credentials may be represented in different formats, such as X.509 certificates or IEEE 1609.2 certificates. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If systems expect different credential formats during authentication, the secure session cannot be established. For example, one system may expect X.509 certificates while the peer presents IEEE 1609.2 credentials, leading to authentication failure. |
| Recommended Mitigation                                       | Deployment specifications should define the credential formats to be supported for mutual authentication. Systems should be configured to support the required credential formats and ensure that authentication mechanisms are compatible across communicating systems. |



## 4. Trust Configuration and System State

Correct message validation and secure communication depend on locally configured trust anchors and accurate system time. These elements are often assumed to be correct, but misconfiguration or drift can cause otherwise valid messages or connections to fail.

| 4a. Valid Messages Rejected Due to Missing or Incorrect Trust Anchors | Certificate validation depends on a locally configured set of trusted root certificates, often referred to as trust anchors. These anchors define which certificate chains are considered valid within a deployment. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If required trust anchors are missing, incorrect, or outdated, a system may be unable to validate otherwise valid certificates. This can result in legitimate messages being rejected or peer systems failing authentication. |
| Recommended Mitigation                                       | Systems should maintain a correctly configured and up-to-date trust store aligned with the applicable trust framework. Trust anchors should be securely provisioned, updated as needed, and validated to ensure they reflect the current set of trusted authorities. |

| 4b. Certificate Validation and Revocation Checks Fail Due to Inaccurate System Time | Certificate validation, signature verification, and revocation checks rely on accurate system time. Time is used to evaluate certificate validity periods, signature timestamps, and other time-dependent security attributes. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Condition                                                    | If system time is incorrect, valid certificates or signatures may appear invalid, or expired or revoked credentials may be incorrectly accepted. This can lead to inconsistent validation results and failed communication between systems. |
| Recommended Approach                                         | Systems should maintain accurate and reliable time synchronization using appropriate time sources. Time should be monitored and managed to ensure it remains within acceptable bounds for validation of certificates and signatures. |

