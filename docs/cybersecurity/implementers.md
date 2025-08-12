# Implementers

As an ITS implementer, you are challenged to deploy secure, resilient systems that operate in compliance with standardized trust models. That means installing, configuring, and maintaining devices and software that support multiple security services, including cryptographic validation, secure networking, and reliable logging. This page provides recommended actions on that can assist with installing and maintaining a secure ITS deployment.

## Provision Devices with Valid Credentials

Every device must have a digital identity. Start by enrolling RSUs, OBUs, signal controllers, and back-office systems with the chosen PKI (SCMS or CCMS). Devices must store private keys securely and use certificates issued by trusted Certificate Authorities.

- Use the approved enrolment and certificate request workflows from your PKI provider.
- Confirm that each device includes secure hardware for private key protection (e.g., HSM or secure element).
- Validate that all issued certificates include correct identifiers, permissions (e.g., PSID/SSP), and expiration periods.
- Configure devices and services to reject untrusted or expired certificates.

## Configure Secure Communications

Configure communication security across the ITS.

- Enable IEEE 1609.2 signing on V2X components.
- Enforce TLS or DTLS for backend and management interfaces.
- Disable unused ports and services. Only expose the interfaces needed for operation.
- Require mutual authentication where applicable (e.g., RSU ↔ TMC).

## Support Certificate Lifecycle Operations

Devices must be able to replace expiring certificates and process revocation information.

- Automate certificate renewal processes to avoid lapses in coverage.
- Install and establish processes for regular updates of Certificate Trust Lists (CTLs).
- Configure devices to download and process Certificate Revocation Lists (CRLs).
- Confirm device behaviour when encountering revoked or unknown certificates.

## Deploy Only Hardened Devices

Never deploy a device with insecure firmware, open debug ports, or default credentials. Verify that hardware and software meet modern cybersecurity expectations.

- Require secure boot with cryptographic firmware validation.
- Enforce cryptographically signed software and OTA updates.
- Lock down administrative interfaces. Use role-based access control (RBAC) and secure authentication.
- Log all access and configuration changes, and store logs in a tamper-evident way.

## Embed Cybersecurity in Procurement

Don’t wait until installation to care about security. Ensure every ITS component you acquire includes cybersecurity functionality, documentation, and vendor support.

- Include cybersecurity requirements in all RFIs and RFPs.
- Evaluate vendor supply chains for transparency and security certifications.
- Require proof of secure software development and incident response readiness.
- Validate that vendor equipment complies with standards such as IEEE 1609.2 or ETSI TS 103 097

## Maintain a Field-Ready Update Process

Outdated software introduces unacceptable risk. Make sure your operational teams can deploy secure updates regularly.

- Require all updates to be digitally signed and verified before installation.
- Maintain tooling to deploy updates over-the-air
- Track update histories across all devices. Maintain audit logs for review.

## Use Available Tools

Tools like the [Mobile ITS Security Application](https://github.com/usdot-fhwa-OPS/ITS-Secure-Prototype-Backend) and the [ITS Cybersecurity Framework Profile](https://rosap.ntl.bts.gov/view/dot/72769) offer pre-built deployment workflows, configuration checklists, and compliance mappings to guide secure deployments.
