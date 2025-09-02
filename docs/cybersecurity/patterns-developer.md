# Secure Manufacturing and Development (D) Patterns

## Pattern D1: Vulnerability Management Program

Establishes a structured, repeatable process for identifying, classifying, and remediating vulnerabilities in ITS applications and systems. This pattern ensures developers and maintainers implement a documented vulnerability management program that includes scanning, triage, patching, secure communications with researchers, and user notification.

### Implementation Context

This pattern applies to any organization that develops or maintains ITS applications, onboard systems (OBUs), infrastructure software (e.g., RSUs), or backend services. Vulnerability management is critical to reduce exploitable attack surfaces, meet regulatory expectations, and demonstrate due diligence.

| **Applies To**   | Application Developers, OEMs, System Integrators, Backend Service Providers |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Vulnerability scanning, verification, patching, and disclosure |
| **Dependencies** | SBOMs, secure update mechanism, vulnerability tracking and classification tools, contact management |

### Key Components

| Component                    | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| Vulnerability Scanning Tools | Perform regular scans on OS, libraries, web services, and firmware. |
| Triage and Classification    | Verify vulnerabilities and assign risk categories (e.g., critical, high). |
| Contact Point for Reporting  | Designated researcher and customer contact (e.g., security@domain.com). |
| Patch Management Process     | Defines procedures for applying and testing security patches. |
| End-User Notification        | Formal method for informing users when patches are available. |
| Remediation Timelines        | Defines maximum time allowed based on severity class.        |
| Security Patch Verification  | Ensures vulnerability is fully remediated and patch integrity is validated. |

### Implementation Details

- Scanning & Detection: Integrate automated vulnerability scanning tools into the development lifecycle. Scan third-party libraries, firmware components, and platform dependencies as part of build or pre-release processes. Schedule full system scans (static/dynamic) prior to major releases.
- Verification & Classification: Review each vulnerability for its potential to be exploited in the deployed environment. Categorize findings using industry standard metrics (e.g., CVSS). Distinguish false positives, document conditions for exploit, and flag high-risk vectors for immediate action.
- Contact Point for Disclosure: Provide a security contact (e.g., `security@yourdomain.com`) and response policy. Monitor submissions from researchers or users and acknowledge reports within a defined SLA. Track inbound reports through a structured intake workflow.
- Remediation Planning: Assign verified vulnerabilities to development teams for remediation. Define a severity-based patch timeline (e.g., critical: 7 days; high: 30 days). Use version control tagging and commit-level traceability for all fixes.
- Patch Testing & Release: Build and test security patches using defined QA workflows. Include regression testing, backward compatibility checks, and validation of the fix. Use digitally signed binaries and validated update packages for delivery.
- User Notification & Disclosure: When a vulnerability fix is deployed, publish release notes with a CVE or internal identifier, affected versions, and remediation instructions. Coordinate responsible disclosure with affected partners or integrators.
- Audit & Traceability: Maintain a log of all vulnerability reports, resolution actions, test outcomes, patch deployments, and communications. Ensure traceability between discovery, fix, and disclosure. Use this log for internal audits or third-party assessments.

### Example Use Cases

| Scenario                    | Behaviour Enforced                                            |
| --------------------------- | ------------------------------------------------------------ |
| Researcher Disclosure       | A third-party security researcher identifies a buffer overflow in an RSU API and emails the listed security contact. A ticket is opened, the vulnerability is verified, and a patch is scheduled. |
| CVE Scan in Web Application | A scanner detects outdated TLS libraries in a traffic app backend. Triage confirms risk, updates the library, and informs customers. |

### Related Standards

| Standard / Guide      | Purpose                              |
| --------------------- | ------------------------------------ |
| NIST SP 800-40r4      | Patch management for federal systems |
| NIST SP 800-53 Rev. 5 | Security control families            |
| ISO/IEC 29147         | Vulnerability disclosure             |
| ISO/IEC 30111         | Vulnerability handling processes     |

## Pattern D2: Secure Product Development Lifecycle

Establishes a structured, security-aware development lifecycle that incorporates cybersecurity risk management into each stage of ITS product design, implementation, and delivery. This pattern helps ensure that both software and hardware products meet minimum cybersecurity expectations, resist common attack vectors, and can be maintained securely over time. A formal Secure Development Lifecycle (SDL) incorporates security engineering, threat modelling, secure coding, vulnerability testing, and traceable quality controls into the product development process.

### Implementation Context

Secure development practices ensure cybersecurity is addressed from the beginning and maintained through release and post-market support.

| **Applies To**   | ITS application developers, firmware developers, OEM software teams, third-party integrators |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Secure development of OBUs, RSUs, backend services, and V2X applications |
| **Dependencies** | Developer training, secure coding standards, testing frameworks, version control policies |

### Key Components

| **Component**                | **Description**                                              |
| ---------------------------- | ------------------------------------------------------------ |
| Secure Development Lifecycle | A formalized development process that includes security checkpoints at each phase |
| Threat Modelling              | Identify potential attack vectors, misuse cases, and trust boundaries early in design |
| Static/Dynamic/Fuzz Testing  | Use automated tools to uncover vulnerabilities in source code and runtime behaviour |
| Secure Coding Standards      | Apply consistent rules (e.g., MISRA, SEI CERT) to prevent implementation-level flaws |
| Quality Control System       | Track defect rates, code quality metrics, and security regression results through CI/CD |
| Developer Training           | Ensure engineers understand secure development principles and product-specific risks |

### Implementation Details

- Requirements & Design: Begin by performing a security-focused review of product architecture. Identify trust boundaries, data sensitivity, and critical services. Develop threat models to anticipate misuse or compromise scenarios. Apply architectural controls early (e.g., privilege separation, secure boot).
- Coding & Build Phase: Enforce secure coding standards and require code reviews with security checklists. Integrate static analysis tools and dynamic analysis tools into the CI/CD pipeline. Use fuzz testing for inputs like V2X messages, web APIs, or firmware update channels.
- Test & Validation: Perform security regression testing, including authentication/authorization tests, input validation, and transport security checks. Integrate third-party security testing tools and validate security functions (e.g., certificate validation logic, logging, and error handling).
- Quality Control: Maintain centralized tracking of test coverage, open vulnerabilities, patch backlog, and known defects. All releases must pass quality gates including functional correctness, performance, and cybersecurity posture.
- Release & Deployment: Digitally sign release artifacts and maintain integrity verification workflows. Validate that installation or update procedures include checks for compatibility, authentication, and rollback safety.
- Maintenance & Support: Track reported vulnerabilities through a vulnerability management program. Reassess threats periodically and update the SDL based on evolving threat landscape or standards updates.

### Example Use Cases

| **Scenario**             | **Behaviour Enforced**                                        |
| ------------------------ | ------------------------------------------------------------ |
| RSU Firmware Development | A vendor implements a secure firmware update flow and tracks defects through a secure CI/CD pipeline. |
| V2X Application Rollout  | A fleet management app is built using SDL. Threat modelling identifies risk of spoofed messages; mitigation is added, and regression tests validate correctness. |

### Related Standards and References

| **Reference**   | **Purpose**                                                  |
| --------------- | ------------------------------------------------------------ |
| NIST SP 800-218 | Secure Software Development Framework (SSDF)                 |
| ISO/IEC 27034   | Application Security Lifecycle Guidance                      |
| SAE J3061       | Cybersecurity Process Framework for Vehicle Systems          |
| ISO 21434       | Road vehicles – Cybersecurity engineering                    |
| CWE/SANS Top 25 | Reference for common software weakness types                 |
| NIST SP 800-53  | Security testing and evaluation controls for system development |

## Pattern D3: Software Bill of Materials

A Software Bill of Materials (SBOM) provides a structured inventory of the software components and dependencies used in a device, service, or application. This pattern ensures that vendors and developers can identify vulnerable components, track software provenance, and respond effectively to security advisories or regulatory inquiries. SBOMs support transparency and accountability across the ITS supply chain and enable Infrastructure Owners and Operators (IOOs) to assess supply chain risk during procurement and deployment.

### Implementation Context

This pattern applies to ITS vendors, OEMs, software developers, and system integrators that produce or manage software components embedded in field devices, backend services, or V2X applications.

| **Applies To**   | OEMs, software developers, system integrators, device vendors |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Component tracking, vulnerability management, procurement support |
| **Dependencies** | Secure development practices, tooling for SBOM generation, CVE/CPE mapping |

### Key Components

| **Component**             | **Description**                                              |
| ------------------------- | ------------------------------------------------------------ |
| SBOM Format Specification | Use standard formats such as SPDX, CycloneDX, or SWID to ensure consistency and automation. |
| Component Inventory       | A complete list of software components (name, version, vendor, license, hash). |
| Dependency Mapping        | Include relationships between software components (parent-child, static/dynamic linking). |
| Vulnerability References  | Link components to known vulnerabilities via CVE or CPE identifiers where possible. |
| Update and Maintenance    | Define how and when the SBOM is updated (e.g., on each software release or patch cycle). |

### Implementation Details

- Tool Integration: Use automated tools integrated into CI/CD pipelines to generate SBOMs during the build process. Validate that the SBOM reflects the final deployed image or firmware.
- Format Selection: Choose a recognized standard such as SPDX  or CycloneDX , and ensure output is machine-readable (e.g., JSON or XML).
- Component Granularity: List all software packages and libraries, including open-source, proprietary, and third-party components.
- Validation and Review: Perform SBOM validation to check for completeness, accuracy, and alignment with product binaries.
- Distribution: Provide SBOMs to customers or regulators upon request, and include them as part of security documentation or procurement packages.
- Security Alignment: Link SBOMs to vulnerability databases (e.g., NVD) and maintain an internal process to identify and act on component vulnerabilities.

### Example Use Cases

| **Scenario**                     | **Behaviour Enforced**                                        |
| -------------------------------- | ------------------------------------------------------------ |
| Field Device Procurement         | IOO requests an SBOM during procurement to assess supply chain risk and vulnerability exposure. |
| Patch Planning and Risk Analysis | A newly disclosed CVE affects an open-source library. The developer uses the SBOM to identify affected products and issue a patch. |

### Related Standards

| **Standard**               | **Purpose**                                                  |
| -------------------------- | ------------------------------------------------------------ |
| SPDX 2.3.0                 | Linux Foundation standard for describing software component metadata. |
| CycloneDX 1.5              | Lightweight SBOM standard maintained by OWASP, focused on supply chain use. |
| NTIA SBOM Minimum Elements | U.S. government-defined baseline for SBOM content and distribution. |

## Pattern D4: Supply Chain Security

Supply Chain Security ensures that cybersecurity requirements are consistently applied across all suppliers and partners involved in the design, development, production, and operation of ITS devices and services. The pattern provides a framework for verifying supplier capability, setting contractual requirements, and ensuring that vulnerabilities or compromises in one part of the supply chain do not propagate through the system. This aligns with ISO/SAE 21434 provisions on distributed development and supplier management.

### Implementation Context

This pattern applies to OEMs, Tiered suppliers, system integrators, and Infrastructure Owners and Operators (IOOs) who procure, deliver, or maintain ITS components and services.

| **Applies To**   | OEMs, suppliers, integrators, IOOs, device vendors           |
| ---------------- | ------------------------------------------------------------ |
| **Used For**     | Supplier assurance, procurement, lifecycle risk management   |
| **Dependencies** | Cybersecurity governance, secure development lifecycle, incident response processes |

### Key Components

| **Component**                           | **Description**                                              |
| --------------------------------------- | ------------------------------------------------------------ |
| Supplier Capability Assessment          | Evaluate supplier maturity and ability to meet cybersecurity engineering requirements. |
| RFQ/Contract Requirements               | Include explicit cybersecurity obligations and reference to ISO/SAE 21434. |
| Cybersecurity Interface Agreement (CIA) | Define responsibilities, milestones, vulnerability handling, and end-of-support provisions. |
| Vulnerability Disclosure                | Require suppliers to identify, report, and remediate vulnerabilities throughout support period. |
| Secure Production & Delivery            | Apply controls to prevent unauthorized modifications during manufacturing and logistics. |
| Incident Response & Updates             | Ensure suppliers provide secure update mechanisms and participate in coordinated response. |

### Example Use Cases

| **Scenario**              | **Behaviour Enforced**                                        |
| ------------------------- | ------------------------------------------------------------ |
| Procurement of ITS Device | IOO requests evidence of ISO/SAE 21434 conformity and complete a cybersecurity interface agreement (CIA) before purchase. |

### Related Standards

| **Standard**       | **Purpose**                                                  |
| ------------------ | ------------------------------------------------------------ |
| ISO/SAE 21434      | Defines cybersecurity engineering for road vehicles, including supplier management. |
| ISO/IEC 27036      | Provides guidance on information security for supplier relationships. |
| UNECE R155 Annex 5 | Outlines requirements for supplier cybersecurity management in type approval. |
