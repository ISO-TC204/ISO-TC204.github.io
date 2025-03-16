# Security Standards and Their Roles

ITS rely on various security standards for safe and secure operations. These standards address various aspects of ITS operations, such as communication, device security, data protection, misbehavior detection, and incident response. 

---

## Categories of ITS Security Standards

### 1. Physical Layer
Standards focus on protecting ITS devices such as Onboard Units (OBUs) and Roadside Units (RSUs) from unauthorized access or tampering. 


#### Key Standards: 
- **SAE J2945/1**: On-Board System Requirement for V2V Safety Communications: The base document for V2V safety and security. Security requirements include security management, bootstrap, certificate loading, certificate storage, certificate revocation list handling, and secure hardware. 

- **ISO/SAE 21434**: Establishes requirements for cybersecurity engineering of road vehicle systems. 

- **SAE J3101**: Provides hardware-based security for ground vehicles. 

- **ISO/IEC 15408 (Common Criteria)**: Offers a framework that can be extended to support evaluation of ITS device security. 

- **V-ITS-S Base Protection Profile (SAFERTEC)**: Provides a framework for evaluating the security and trustworthiness of CV and V2I communications. 


### 2. Network/Transport Layer 

Standards ensuring the secure exchange of data between ITS entities, such as vehicles, infrastructure, and backend systems. These standards can be applied to secure V2V and V2I communications and protect real-time safety critical messaging in ITS environments. 

#### Key Standards: 
- **ISO 21177**: Specifies services for secure session establishment and authentication between trusted ITS devices. 

- **IEEE 1609.2**: Certificate management protocols are specified in this document to support provisioning and management of digital certificates, as specified in IEEE Std 1609.2(TM), to end entities, that is, an actor that uses digital certificates to authorize application activities.

- **ETSI TS 103 097**: Defines security headers and certificate formats for C-ITS communications in Europe. 

- **ISO 15118**: Addresses vehicle-to-grid (V2G) communication interface security for electric vehicles. 

- **IEEE 1609.3**: Services to WAVE devices and systems are provided. Layer 3 and layer 4 of the open system interconnect (OSI) model and the Internet Protocol (IP), User Datagram Protocol (UDP), and Transmission Control Protocol (TCP) elements of the Internet model are represented. Management and data services within WAVE devices are provided

- ** SAE 3315 LTE-V2X Requirements and Deployment Profiles for Aftermarket V2X Devices (AVD)**: This SAE Standard describes classes of AVDs intended to support particular services, provides their respective requirements including RF performance requirements, specifies their respective profiles, and describes the test procedures. This document is targeted to enable early deployments by supporting different classes of AVDs that could interact with on-board units (OBUs) and roadside units (RSUs). 

- **SAE J3161/1 Onboard System Requirements for LTE-V2X V2V Safety Communications**: This SAE Standard specifies system requirements for an on-board vehicle-to-vehicle (V2V) safety communications system for light vehicles and public safety vehicles, including standards profiles, functional requirements, and performance requirements. The system is capable of transmitting and receiving the SAE J2735-defined basic safety message (BSM) over a PC5 Sidelink V2X (mode 4) communications link as defined in ETSI Release 142,3. The system uses Institute of Electrical and Electronics Engineers (IEEE) 1609 standards for network and transport layer communications, as well as security.

- **SAE J3161/1B Onboard System Requirements for LTE-V2X V2V Safety Communications by Non-Light-Duty Vehicles and Motorcycles**

- **SAE J3161/1C Onboard System Requirements for LTE-V2X V2V Safety Communications by School Buses**


---
### 3. Data Layer: 
Standards that address the protection of ITS data in storage and in transit. 

#### Key Standards: 

- **ISO/IEC 27001**: Provides guidelines for managing information security.
- **ISO 21186-3**: Recommends practices for securing data exchange in Cooperative ITS environments.

### Misbehavior Detection and Incident Response
Standards that support the detection, reporting and response to misbehavior within an ITS. 

#### Key Standards:
- **IEEE 1609.2**: Incorporates mechanisms for misbehavior reporting and response.
- **ISO 22320**: Provides incident management guidelines for ITS systems.
- **SAE J3061**: Serves as a cybersecurity guidebook for managing risks in cyber-physical vehicle systems.
- **SAE J3287**:  This document provides a specification of a general misbehavior report format suitable for reporting misbehavior observed by a system running SAE V2X applications, and specific report contents for specific instances of misbehavior. It also provides an overview of the architecture of a system-wide misbehavior management service for the V2X system and positions the misbehavior reporting services within that architecture.


### 4. Application Layer 
Some standards are designed for specific ITS use cases, such as electric vehicle communications and remote diagnostics. 

#### Key Standards:
- **ISO 15118**: Focuses on V2G communication security.
- **SAE J2931/7**: Defines security for Plug-In Electric Vehicle (PEV) communication with charging infrastructure.
- **ISO/TR 23786**: Provides criteria for assessing risks associated with remote access to vehicles.
- ** SAE J2945/4 Road Safety Applications**: Curve Speed warning (CSW), Reduced Speed Zone Warning (RSZW), Lane Closure Warning (LCW), Dynamic Traveler Information (DTI), Incident Information (INC).  This document includes a security requirements section (normative) but those requirements are limited to secure communication (using IEEE Std. 1609.2 certificates).  There are not requirements for the cyber security design or configuration of EEs that assert Road Safety related PSIDs. 

---
