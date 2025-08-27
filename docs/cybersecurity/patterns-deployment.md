# Deployment and Integration Functions

## Pattern D1: 1609.2.2 Multi Jurisdictional Interoperability 

Ensures that ITS devices only trust messages and services from explicitly authorized sources. This pattern defines how devices determine which certificates to trust, which SCMS Managers or Root CAs are allowed, and what entitlements (e.g., PSIDs or SSPs) are considered valid. Trust decisions are guided by signed, policy-based structures such as Certificate Trust Lists (CTLs), with device behavior scoped to specific operational contexts. By implementing structured interoperability policies, this pattern supports secure collaboration across jurisdictions, vendors, and SCMS domains, while preventing unauthorized use of ITS applications or services.

##### Implementation Context

Used when deploying ITS devices into multi-jurisdictional environments where multiple SCMS Managers, Root CAs, or policy frameworks coexist. 

##### Key Components

| Component                    | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| Certificate Trust List (CTL) | Digitally signed structure that enumerates which Root CAs, SCMS Managers, and permissions are trusted. |
| Trust Permissions            | Defined at a per-RCA or per-SCMS Manager level. Specifies what application permissions (e.g., PSIDs, SSPs, OpOrgIds) are allowed. |
| Policy Enforcement Engine    | Logic within the device or backend service that evaluates received messages against the active CTL and permissions. |
| Context-Specific Rules       | Trust decisions may vary based on jurisdiction, device role, or geolocation. |



##### Implementation Details

- Devices must store and validate the latest CTL signed by the device's Home SCMS Manager. 
- CTLs should include detailed permission sets that scope trust to specific PSIDs, SSPs, or operational attributes.
- Devices must verify that incoming message certificates match both the issuing authority and the authorized permissions within the CTL.
- Trust relationships may be restricted to only a subset of applications or message types to prevent overbroad interoperability.
- Implementations should allow for segmented trust, for example, accepting a Root CA for basic safety messages but not for high-privilege services like SPaT/MAP control.

##### Example Use Cases

| Scenario                            | Behavior Enforced                                            |
| ----------------------------------- | ------------------------------------------------------------ |
| Cross-jurisdiction message exchange | An RSU in Jurisdiction A trusts SRM messages from an OBU in Jurisdiction B, but only if the certificate’s SSP matches a permitted entitlement in the CTL. |

##### Related Standards

| Standard      | Purpose                                                      |
| ------------- | ------------------------------------------------------------ |
| IEEE 1609.2.2 | Defines how SCMS Managers, Root CAs, and permissions are expressed and enforced in CTLs and Trust Permission Structures. |
| IEEE 1609.2   | Base certificate and message format definitions.             |



