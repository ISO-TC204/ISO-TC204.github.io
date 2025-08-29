# Standards Developers

Standards development Organizations (SDOs) and Standards Developers are responsible for defining interoperable, secure, and reusable protocols that enable an interoperable ITS ecosystem. SDOs that develop ITS cybersecurity-related standards include ISO, IEEE, ETSI, and SAE. These organizations define the technical specifications for secure communication protocols, certificate formats, identity and authorization models, and trust frameworks used in ITS environments.

A Standards Developer should work to ensure that cybersecurity capabilities (e.g., trust management, authenticated messaging, secure transport) are consistently defined and supported across the ITS vendor community.

### Responsibilities

To meet the needs of implementers and policy bodies, you must:

- Specify security protocols with implementation detail sufficient for conformance testing, certification, and cross-vendor interoperability.
- Align standards across international SDOs (e.g., IEEE, ETSI, ISO, SAE) to support cross-jurisdictional trust models and certificate exchange.
- Avoid redefining existing security mechanisms; instead, adopt and profile protocols (e.g., TLS, DTLS, IEEE 1609.2, X.509) from other mature standards bodies.
- Support layering and modularity so that capabilities can evolve independently and integrate with evolving architectures like MEC, ATC, and cloud-hosted services.
- Define and maintain cryptographic agility to support migration to post-quantum algorithms, strong key lifecycles, and forward secrecy where appropriate.
- Enable testability and certification by including test vectors, profile constraints, and unambiguous processing rules.

### Recommended Actions

- Coordinate through cross-SDO working groups to align message structures, certificate formats, and protocol flows (e.g., IEEE/SAE with ETSI/ISO).
- Profile existing protocols using constrained and well-defined parameter sets appropriate for ITS resource limits and latency constraints.
- Ensure all security-relevant objects have validated encoding and validation logic, including edge cases and malformed inputs.
- Document threat models and show how your specifications mitigate or assume responsibility for threats (e.g., replay, spoofing, denial of service).

