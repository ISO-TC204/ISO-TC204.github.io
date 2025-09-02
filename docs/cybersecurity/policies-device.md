# Device and Application Security Policy Recommendations

It is important that application developers and manufacturers understand the complexities related to the configuration options for various cybersecurity controls. The tables below provides examples of cybersecurity configuration options and in many cases recommendations for the optimal option. Each of these policy item details has been taken from the FHWA ITS2P program recommendations.

## Password Policies

| Policy Item                                       | Description                                                  | Recommendation |
| ------------------------------------------------- | ------------------------------------------------------------ | -------------- |
| Minimum Password Length                           | Specifies the minimum length a password should have for utilization within ITS equipment for user authentication, admin authentication, etc... | 12 characters  |
| Minimum Password Quality                          | Specifies the minimum number of password quality categories that need to be enforced, which determine password characteristic requirements. The chosen password should also be checked against a blacklist of unacceptable passwords, which contains previous breach corpuses, dictionary words, and specific words that users are likely to choose. | None           |
| Device Lockout Timeout                            | Specifies the maximum amount of time that may pass before a device is locked from the software automatically. | 5 minutes      |
| Maximum Number of Failed Attempts                 | Specifies the maximum number of times password entry may be failed by a user before being barred from attempting to log into their account and being asked to reset their password. | 3              |
| Enable Credential Recovery                        | Provides technicians with the option to reset or recover credentials. | True           |
| Maximum Days Before Password Expiration           | Mandates routine password changes by specifying maximum days a password can remain active until it must be changed. | 60             |
| Minimum Time Between Credential Recovery Attempts | Represents the minimum number of days that must pass before a password can be recovered again if it has been recently reset. | 5 minutes      |

## Application Restriction Policies

| Policy Item                     | Description                                                  | Recommendation |
| ------------------------------- | ------------------------------------------------------------ | -------------- |
| List of Approved Applications   | Specifies applications that are allowed to run within ITS equipment environments | None           |
| List of Unapproved Applications | Specifies applications that are not allowed to run within ITS equipment environments | None           |

## Physical Security Policies

| Policy Item               | Description                                                  | Recommendation |
| ------------------------- | ------------------------------------------------------------ | -------------- |
| Enable Debugging Features | Manages diagnostics, error catching, and print statements that detail operating information for an ITS device | True           |
| Enable USB                | Determines whether ITS equipment can connect to physical USB ports. | False          |
| Enable Location Services  | Allows for real time location of ITS equipment to be transmitted. | False          |

## User Management Policies

| Policy Item                                         | Description                                                  | Recommendation          |
| --------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| Inactive User Lock                                  | Establishes a maximum number of days for a user account to stay inactive before being disabled to prevent future security vulnerabilities. | No greater than 90 days |
| Require Two Factor Authentication                   | Mandates Two-Factor Authentication for all technicians logging in to ITS equipment. | True                    |
| Enable Multiple Multi Factor Authentication Methods | Allows vendor to enable a variety of methods used to authenticate users. | True                    |

## Audit Collection Policies

| Policy Item                         | Description                                                  | Recommendation |
| ----------------------------------- | ------------------------------------------------------------ | -------------- |
| Enable Account Recovery Logging     | Logs attempts to recover account credentials as well as password changes. | True           |
| Enable Database Interaction Logging | Logs user interactions with database.                        | True           |
| Log Storage Frequency               | Determines how often, in days, logs will be uploaded to a secure database. | 14 days        |

## System Time Policies

| Policy Item                   | Description                                                  | Recommendation |
| ----------------------------- | ------------------------------------------------------------ | -------------- |
| Require Network Time          | Requires network time to be set before proceeding with ITS equipment operation | True           |
| Allow Automatic Date and Time | Allow Date & Time to be automatically configured and readjusted according to time-zones and time changes. | True           |
| Utilize Three Time Sources    | −Enables three synchronized time sources to maintain consistency in event log timestamps. | True           |

## System File Restriction Policies

| Policy Item                 | Description                                                  | Recommendation |
| --------------------------- | ------------------------------------------------------------ | -------------- |
| Enable File Versioning      | Enable storage of older versions of ITS device manuals or data for future reference. | True           |
| Enable Integrity Protection | Identifies and reports changes to ITS device system files.   | True           |
| Enable File Encryption      | Enable secure encryption of files on ITS devices.            | True           |

## Secure Boot Load Policies

| Policy Item                                 | Description                                                  | Recommendation |
| ------------------------------------------- | ------------------------------------------------------------ | -------------- |
| Enable Read/Write Only Permissions          | Only allow sudo users to read/write boot parameters to prevent vulnerability exploitation by non-root users. | True           |
| Require Bootloader Password                 | Only allow sudo users to read/write boot parameters to prevent vulnerability exploitation by non-root users. | True           |
| Require Authentication for Single User Mode | Require authentication when booting into single-user mode to prevent unauthorized users from gaining root access through repeated rebooting. | True           |

### Encrypted Storage Policies

| Policy Item                         | Description                                                  | Recommendation |
| ----------------------------------- | ------------------------------------------------------------ | -------------- |
| Auto-mounting                       | Allows any USB drive or disc to be attached to the system and have its contents transferred into the ITS device. | False          |
| Routine Cloud-based Backups         | Periodically backup hard drive contents to cloud-based storage system in case of system failure. | 30 days        |
| Routine Defragmentation             | Periodically defragment hard-drive in order to reorganize files and improve performance. | 30 days        |
| Limit Hard Drive Storage Capacity   | Limit maximum storage capacity of hard drive to a specified percentage of actual capacity to minimize risk of data corruption and performance loss. | 80%            |
| Generate Encryption Recovery Tokens | Generate fallback tokens in the case that encryption key credentials are lost. | True           |

## Data At Rest Security Policies

| Policy Item                           | Description                                                  | Recommendation |
| ------------------------------------- | ------------------------------------------------------------ | -------------- |
| Enable Data at Rest Encryption        | Encrypts sensitive data at rest on servers, applications, and databases. | True           |
| Enable Data Loss Protection Solutions | Enable DLP in the Cloud with tools such as Google Cloud DLP, Barracuda Backup etc...in order to further secure data at rest and minimize data leaks. | True           |
| Routine Data Backup                   | Back up Data at rest routinely in the case of mishandled data transfers or power outages. | True           |
| Data Tokenization                     | Substitute sensitive data with non-sensitive tokens that will not be able to be exploited if data is stolen or leaked. | True           |

## Audit Management Policies

| Policy Item                             | Description                                                  | Recommendation |
| --------------------------------------- | ------------------------------------------------------------ | -------------- |
| Data Retention Capacity                 | Sets the max size (in bytes) of data to be held by audit logs. | None           |
| Enable auditd verification (Linux only) | Verify that auditd (daemon that records system events, provides information regarding unauthorized access instances) is installed. | True           |
| Enable Automatic Log Deletion           | Delete audit logs if they have reached maximum file size capacity. | None           |

## Integrity Protection Policies

| Policy Item              | Description                                                  | Recommendation |
| ------------------------ | ------------------------------------------------------------ | -------------- |
| Enable AIDE (Linux only) | AIDE takes a snapshot of the current filesystem’s state noting register hashes, modification times, and other data defined by administrators. A database is then built based on this snapshot and is stored to use in future integrity checks against the system’s status. AIDE will automatically report any discrepancies between versions found during integrity checks to administrators. | True           |
| Enable Version Control   | Allows for data recovery or rollback in case of breaches or data loss incidents. | True           |

## Privilege Management Policies

| Policy Item                                                  | Description                                                  | Recommendation |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| Require re-authentication for Privilege Escalation (Linux only) | −Users will be required to reauthenticate to access higher-privilege resources or tasks. Prevent automated processes from being able to utilize elevated privileges. | True           |
| sudo Authentication Timeout (Linux only)                     | −Establishes a timeout that reduces the window of opportunity for unauthorized privileged access by unauthorized users. | 15 minutes     |

## Firmware and Software Update Policies

| Policy Item                                | Description                                                  | Recommendation |
| ------------------------------------------ | ------------------------------------------------------------ | -------------- |
| Automated Software Patch Management        | Deploy automated software update tools in order to ensure that third-party software on all systems is running the most recent security updates. | True           |
| Automate Operating System Patch Management | Ensure that operating systems are running the most recent security updates. | True           |

## Firewall Settings Policies

| Policy Item     | Description                                                  | Recommendation |
| --------------- | ------------------------------------------------------------ | -------------- |
| Enable Firewall | Manage a host-based firewall or port-filtering tool on end-user devices, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed. | True           |
|                 |                                                              |                |

## Secure Key Management Policies

| Policy Item                            | Description                                                  | Recommendation  |
| -------------------------------------- | ------------------------------------------------------------ | --------------- |
| Routine Key Rotation                   | An over-used key can encrypt too much data making it vulnerable to cracking, especially using old symmetric algorithms. High volumes of data can be exposed in the event of a key becoming compromised, which can be countered with frequent key rotations, | 30 days         |
| Audit Key Logging                      | Key lifecycle is logged to identify instances of key compromise. | True            |
| Multi Factor Authentication Key Access | Require multi-factor authentication to access keys. Important for keys that have high privilege such as admin. | True            |
| Configure Key Size                     | −Larger keys offer longer protection at the cost of performance. Configuration is based on input passed in as an integer which determines the bit size of the key. | P-256 for ECDSA |

## Remote Configuration Policies

| Policy Item                                      | Description                                                  | Recommendation |
| ------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| Authorize Remote Access Based on Connection Type | Authorize users based on the connection type provided.       | True           |
| Authorize Remote Access Based on Time of Day     | Authorize remote access for users based on the time of day. Ex: Certain users will only have remote access during an organization’s business/working hours. | True           |
| Authorize and Verify Caller ID                   | −Specify the telephone number that the user must be calling from in order to establish a successful connection. Requires hardware to detect the number that the user is calling from. | None           |
| Enable Callback Options                          | Allows users to connect remotely and without use of callback. | True           |
| Assign Static IP Address for Remote Access       | −Assign a unique IP address to each user that connects to an ITS remotely. | None           |
| Assign Duration of Session                       | −Disconnect users after a specified amount of idle time has passed. | 45 minutes     |
| Assign Maximum Session                           | Disconnect users after an allotted time.                     | 60 minutes     |
| Configure Encryption Parameters                  | −Permit or define VPN connections to the remote server.      | Yes            |

## Data In Transit Policies

| Policy Item                     | Description                                                  | Recommendation |
| ------------------------------- | ------------------------------------------------------------ | -------------- |
| Enable End to End Encryption    | −Encrypt data before sending to destinations endpoints and only decrypt data using a public-private key pair. | True           |
| Enable Authentication Endpoints | −Access to data endpoints should be configured to require authentication in order to further secure data transportation. | None           |
| Enable Secure Protocols         | −Provide a secure protocol to perform encrypted communications. SSL, TLS, HTTPs. HTTPs are the most appropriate protocol to implement for this usage case, but other options can be selected based on administrator discretion. |                |
