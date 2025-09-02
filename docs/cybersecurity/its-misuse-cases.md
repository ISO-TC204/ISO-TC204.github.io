# ITS Cybersecurity Misuse Cases

Misuse cases show how attackers can chain multiple threats to disrupt ITS operations. They help stakeholders understand realistic attack scenarios, identify impacted assets, and apply the right protections to strengthen their systems.

## Misuse Case 1: Phishing Attack Leads to Loss of Monitoring Visibility

An attacker sends a phishing email to an employee working in a Traffic Management Center (TMC). The employee provides credentials that allow the attacker to gain access to the TMC’s IT environment. Once inside, the attacker performs lateral movement to reach the operational technology (OT) network that manages roadside monitoring devices such as Closed-Circuit Television (CCTV) cameras. The attacker issues commands that disable or disrupt these devices, resulting in a loss of video feeds. With monitoring visibility reduced, the TMC cannot effectively oversee traffic conditions or detect incidents in real time.

### Impacted Assets

| Asset Category      | Example Assets Impacted                                   |
| ------------------- | --------------------------------------------------------- |
| Field Devices       | CCTV cameras, roadside monitoring devices                 |
| Operational Systems | TMC video management platforms, OT network infrastructure |
| IT Systems          | Employee workstations, email systems, Active Directory    |
| Communications      | Center-to-field control and data links                    |

## Threats Involved

This misuse case maps to existing threats in the ITS Threat Catalogue:

| Threat ID | Threat                                                       |
| --------- | ------------------------------------------------------------ |
| T_0001    | Unauthorized ITS device or application access                |
| T_0009    | Message interception or modification (attacker manipulates control messages to disable devices) |
| T_0013    | An attacker inserts themselves between devices (man-in-the-middle) to relay or modify communications while impersonating trusted parties. |
| T_0031    | An ITS device is tampered with.                              |
| T_0035    | Social Engineering of ITS personnel leading to credential compromise |
| T_0036    | Attacker moves laterally from IT to OT network               |

### Applicable Cybersecurity Patterns

| Security Pattern                                             | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [D5: Secure Remote Management](patterns-management.md#pattern-m6-secure-remote-management) | Require encrypted communications, mutual authentication, and privilege-based access controls for remote sessions between IT and OT systems. |
| [E2: Secure Device Configuration](patterns-edge.md#pattern-e2-secure-device-configuration) | Harden roadside devices with secure configuration, password management, and audit logging to resist unauthorized shutdown. |

## Misuse Case 2: Compromise of Remote Software Update Process

An attacker compromises the update process used to deliver software or firmware to ITS field devices. This could involve exploiting weak authentication on the update server, intercepting update files in transit, or inserting a malicious update through a compromised supplier. Once the malicious update is applied, the attacker gains persistent control over the device, allowing service disruption, data manipulation, or use of the device as a launch point for further attacks.

## Impacted Assets

| Asset Category      | Example Assets Impacted                                  |
| ------------------- | -------------------------------------------------------- |
| Field Devices       | RSUs, OBUs, CCTV cameras, signal controllers             |
| Operational Systems | Update servers, device management platforms              |
| Communications      | Distribution channels between update servers and devices |

### Threats Involved

| Threat ID | Threat                                                       |
| --------- | ------------------------------------------------------------ |
| T_0006    | Device runs unapproved or unsigned applications              |
| T_0013    | An attacker inserts themselves between devices (man-in-the-middle) to relay or modify communications while impersonating trusted parties. |

## Recommended Mitigations

| Security Pattern                                             | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [E6: Secure Software Integrity and Boot](patterns-edge.md#pattern-e6-software-integrity-verification-and-secure-boot) | Require cryptographic signing and verification of all updates before installation. |
| [D5: Secure Remote Management](patterns-management.md#pattern-m6-secure-remote-management) | Ensure update channels use encrypted, authenticated sessions. |
| [D4: Supply Chain Security](patterns-developer.md#pattern-d4-supply-chain-security) | Verify supplier update processes and components are protected. |

## Pattern E6: Software Integrity Verification and Secure Boot
