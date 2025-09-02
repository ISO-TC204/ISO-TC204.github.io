# ITS Cybersecurity Glossary

Authorization Authority (AA)
: In European C-ITS, the component that issues short-term Authorization Tickets to ITS stations for signing messages.

Authorization Ticket (AT)
: A short-lived certificate in the European CCMS used to sign V2X messages while protecting sender privacy.

Certificate Trust List (CTL)
: A list of trusted Root Certificate Authorities and security authorities used to verify which certificates a system accepts.

Cooperative ITS Credential Management System (CCMS)
: The European system for managing certificates, trust lists, and permissions for ITS stations.

European Certificate Trust List (ECTL)
: The signed electronic version of a trust list used in European deployments to distribute trusted root and authority information to devices.

Enrolment Authority (EA)
: In European C-ITS, the authority that issues Enrolment Credentials proving a device’s legitimacy.

Enrolment Credential (EC)
: A long-term certificate proving that a device is approved to request operational certificates.

Hardware Security Module (HSM)
: A dedicated hardware component used to securely generate, store, and use cryptographic keys; provides strong protection against key theft or tampering.

Intelligent Transport System Application Identifier (ITS-AID)
: Used to uniquely identify ITS application objects.

Lateral Movement
: An attacker technique where access gained on one device or network segment is used to move to other connected systems, increasing the impact of a breach.

Man-in-the-Middle Attack
: A threat where an attacker secretly intercepts and possibly alters communication between two parties who believe they are communicating directly with each other.

Misbehaviour Detection
: A set of processes and services that identify and respond to devices that send invalid or malicious messages.

Onboard Unit (OBU)
: An in-vehicle device that communicates with other vehicles and roadside equipment using secure V2X messages.

Provider Service Identifier (PSID)
: An identifier in certificates that defines which ITS applications a device is authorized to use.

Pseudonym Certificate
: A short-lived certificate in the SCMS that allows vehicles to sign messages without exposing a permanent identity.

Root Certificate Authority (Root CA)
: The highest trust anchor in a PKI that signs subordinate certificates.

Roadside Unit (RSU)
: A field device mounted along the roadway that exchanges secure messages with vehicles and backend systems.

Security Credential Management System (SCMS)
: The North American system for managing V2X certificates, permissions, trust lists, and misbehaviour response.

Service Specific Permission (SSP)
: A field in a certificate that provides detailed constraints on what actions a device may perform within an application.

Trusted Platform Module (TPM)
: A secure hardware chip embedded in a device that stores keys and measurements used for secure boot and attestation; similar in purpose to an HSM but typically built-in.
