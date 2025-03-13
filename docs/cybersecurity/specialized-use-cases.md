
## ITS Station-to-ITS Station Communication

ITS Stations, including Roadside Units (RSUs) and backend systems, communicate to exchange data such as Signal Phase and Timing (SPaT) data and Traveler Information Messages (TIM). These stations may use IEEE Std. 1609.2 and, if relevant, ETSI TS 103 097** certificates and formats. Secure communication between ITS Stations ensures that only trusted entities can participate in data exchanges.

### Security Services That May Be Employed

- **ISO 21177 – Secure Session Establishment and Authentication**  
  Ensures authentication and secure session management for ITS data exchanges.

## Backend Infrastructure to RSU

Backend infrastructure components may be provisioned with **X.509 certificates**, which enable secure communication using protocols such as **Transport Layer Security (TLS)**.


## Inter-Domain Interoperability

Secure interoperability between ITS domains is necessary to facilitate communication between different networks, security policies, and administrative domains.

## Use Cases

- **Road Use Charging with IEEE 1609.2 and TLS**  
  Road use charging systems may leverage IEEE 1609.2 certificates for authentication, combined with TLS for secure data transmission.  

- **Probe Data Collection**  
  Secure probe data collection requires authentication, privacy-preserving mechanisms, and encryption to protect the integrity and confidentiality of collected vehicle data.