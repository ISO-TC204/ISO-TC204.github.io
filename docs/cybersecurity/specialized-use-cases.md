# Specialized Use Cases

Certain ITS applications involve heightened cybersecurity risks due to their safety-critical nature, sensitivity of data, or exposure to external networks. This section highlights examples of such use cases and outlines associated risks and considerations for implementers.

## Cooperative Driving Automation (CDA)

Cooperative Driving Automation allows vehicles to coordinate actions such as lane merging, platooning, and emergency response through direct communication. These interactions are highly time-sensitive and safety-critical. Key risks:

- Spoofed messages triggering incorrect maneuvers
- Unauthorized devices attempting to participate
- Injection of false trajectory or intent data



## Probe Data Collection

Probe data applications collect information such as vehicle speed, heading, or environmental conditions to support traffic analysis and planning. Key risks:

- Unauthorized access to collected data
- Leakage of personally identifiable or vehicle-identifiable information
- Injection of fabricated probe reports

## Road Use Charging (RUC)

Road Use Charging systems rely on trusted reporting of mileage, location, or toll zone entry to calculate fees. RUC systems track mileage or toll zone entry to calculate user fees. Accuracy and fairness depend on trusted location reporting. Key risks:

- Manipulation of reported travel data to reduce fees
- Credential sharing or spoofing to mask vehicle identity
- Unauthorized software modification to disable location tracking



## Mobile Edge Computing (MEC) 

MEC allows data processing closer to the field, such as at RSUs or in-vehicle systems, reducing latency for time-sensitive applications. Key risks:

- Unauthorized access to locally processed data
- Deployment of unvetted software at edge nodes
- Disruption of V2X applications through edge-layer compromise

## Cooperative Awareness Message (CAM) 

Cooperative Awareness Messages are used by vehicles and roadside units to broadcast information such as position, speed, and heading at frequent intervals. This basic safety message helps surrounding road users build situational awareness and react appropriately. Key risks:

- Manipulation of CAM content to hide or fake a vehicle’s presence
- Unauthorized transmission of CAMs by rogue devices
- Privacy concerns if CAMs are linked to a permanent vehicle identity
