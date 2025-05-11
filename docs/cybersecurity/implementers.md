# **Implementer Guidance**  

ITS implementers include engineers, system integrators, and security professionals responsible for deploying, configuring, and maintaining secure ITS infrastructure. Implementers must ensure that security mechanisms are correctly applied while maintaining system performance and operational reliability.  

This section provides guidance on security implementation strategies for both European (EU) and North American ITS environments.  
---

## **1. Secure Deployment and Configuration**  

Proper security configuration is important to protect ITS systems from cyber threats. There are resources available to support implementers in this area. This includes tools such as the Federal Highway Administration's [Mobile ITS Security Application](https://github.com/usdot-fhwa-OPS/ITS-Secure-Prototype-Backend) and the [ITS Cybersecurity Framework Profile](https://rosap.ntl.bts.gov/view/dot/72769).  

In addition, in order to be enrolled within PKI systems such as the SCMS, subscribers (e.g., OBUs and RSUs) must demonstrate that they have met the enrollment requirements levied by the PKI provider. These can be found in policy documentation provided by the PKI provider. Testing services can also be procured, such as those provided by OmniAir or other vendors.  

### **Key Implementation Steps Include**  
- Configure **PKI-based authentication** for vehicles, RSUs, and backend systems, making use of either CCMS or SCMS provided IEEE Std. 1609.2 certificates.   

- Implement **secure messaging protocols** such as TLS and IEEE 1609.2 for V2X communication.  

- Establish processes for **certificate lifecycle management**, including revocation and renewal processes.

- Alignment with Standards: Comply with standards such as Common Criteria (e.g., EAL4+ for HSMs) and ETSI TS 102 941 / IEEE Std. 1609.2 for secure V2X communications.
---

## **2** Deploy hardened ITS equipment. 
Implementing hardened ITS equipment ensures resilience against cyber threats. Protection Profiles (PPs) like the V2X HSM PP and SAFERtec modules define security requirements for components such as Onboard Units (OBUs) and Roadside Units (RSUs). These profiles emphasize robust cryptographic operations, secure storage for cryptographic keys, and protection against physical and logical attacks.

### Key implementation steps include:

Tamper Resistance: Deploy hardware with tamper-proof designs and secure elements (e.g., HSMs) to safeguard critical operations.
Secure Boot and Updates: Ensure all devices support secure boot mechanisms and cryptographically verified over-the-air updates.
Access Control and Monitoring: Implement strict access control (e.g., role-based access) and continuous monitoring for anomalies.


## **3. Manage Secure Software and Firmware Updates**  

ITS devices must run trusted and up-to-date software to prevent exploitation.  

### **Key Implementation Steps Include**  
- Use **secure boot** and **code signing** to verify software authenticity.  
- Implement **secure over-the-air (OTA) updates** with integrity verification.  
- Apply **access control** to restrict unauthorized software modifications.  


---

## **Learn More**  
- [IEEE 1609.2](https://standards.ieee.org/standard/1609_2-2016.html)  

- [ETSI TS 102 941](https://www.etsi.org/deliver/etsi_ts/102900_102999/102941/)  

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)  

- [Mobile ITS Security Application](https://github.com/usdot-fhwa-OPS/ITS-Secure-Prototype-Backend)

- [ITS Cybersecurity Framework Profile](https://rosap.ntl.bts.gov/view/dot/72769).  