# Original Equipment Manufacturers (OEMs)

Vehicle manufacturers (OEMs) play a central role in ensuring that connected and automated vehicles entering the ITS ecosystem are developed, validated, and maintained in accordance with cybersecurity engineering practices. A secure vehicle is one that is designed with cybersecurity integrated into every stage of its lifecycle, is supported by a formal Cybersecurity Management System (CSMS), and is verified through structured testing and supplier assurance.

## Cybersecurity Management System

OEMs should establish and maintain a Cybersecurity Management System (CSMS) in alignment with ISO/SAE 21434 and regulatory requirements such as UNECE R155. A CSMS provides the organizational governance needed to manage cybersecurity risk across the full lifecycle of a vehicle, from concept through decommissioning. It should cover:

- Cybersecurity [risk assessment and threat analysis](threat-analysis.md) at the concept and design stages.
- Integration of cybersecurity into requirements, design reviews, and testing activities.
- Continuous monitoring of vulnerabilities and incidents throughout the operational phase.
- Defined roles, responsibilities, and escalation paths for handling cybersecurity events.

A CSMS should also ensure compliance with UNECE R156 requirements for Software Update Management Systems (SUMS), guaranteeing that all vehicles are equipped with a secure, auditable update process.

## Vehicle Architecture and Network Separation

Vehicles should be designed with clear separation between safety-critical networks (e.g., braking, steering, ADAS domain controllers) and non-safety networks (e.g., infotainment, telematics). Firewalls, gateways, and intrusion detection systems must be implemented to ensure that compromise of external interfaces such as Wi-Fi, Bluetooth, or cellular cannot be leveraged to access safety-critical functions.

## Secure Update and Patch Management

OEMs must provide secure processes for software and firmware updates, whether performed manually or over-the-air (OTA). Updates should be cryptographically signed, verified prior to installation, and designed to prevent rollback to older versions.

## Supply Chain Security

Given the reliance on tiered suppliers, OEMs should implement supply chain assurance processes in line with ISO/SAE 21434 and the EU Cyber Resilience Act. Supplier capability assessments, security requirements in contracts, and verification of supplier components (e.g., ECUs, sensors, communication modules) must be part of the OEM’s program.

## Interface and Wireless Security

All wireless and wired interfaces, including Wi-Fi, Bluetooth, cellular, and telematics, must be hardened against misuse. Testing should confirm that strong authentication is enforced, weak protocols (e.g., 2G cellular) are disabled, and secure pairing methods are used for Bluetooth.

## Cryptographic and Key Management Practices

Vehicles should implement strong cryptographic controls for communication, storage, and authentication. Keys must be generated securely, stored in tamper-resistant environments (e.g., HSMs or secure enclaves), and rotated regularly. Certificates used for V2X or backend communications must follow lifecycle rules defined in the applicable Certificate Policy (CP) and CPS.
