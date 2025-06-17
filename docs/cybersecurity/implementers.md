# **Implementer Guidance** 

ITS implementers include engineers, system integrators, and field technicians responsible for deploying and maintaining secure infrastructure components. This page provides practical guidance for ensuring that key cybersecurity requirements are met during deployment and operation.  

## Configure and Maintain a Secure Environment

Devices such as OBUs and RSUs must be correctly set up before they can securely communicate within a certificate-based trust system. This setup includes installing issued certificates, enabling secure message protocols, and protecting private keys using secure storage.

### Recommended Actions
- Install valid certificates issued by the appropriate PKI authority (e.g., SCMS, CCMS) using approved enrollment processes.

- Enable secure communication protocols, such as IEEE 1609.2 for signed V2X messages, and TLS for infrastructure and back-office connections.
- Apply secure defaults to networked devices: disable unused interfaces, require mutual authentication, and configure firewall rules.
- Support certificate lifecycle processes, including revocation and renewal, in accordance with policy from the PKI provider.

Tools like the [Mobile ITS Security Application](https://github.com/usdot-fhwa-OPS/ITS-Secure-Prototype-Backend) and the [ITS Cybersecurity Framework Profile](https://rosap.ntl.bts.gov/view/dot/72769) provide deployment checklists and configuration templates.

---

## Establish Processes to Procure Secure Equipment

 A secure ITS environment begins with what you acquire. Before deploying any hardware, software, or service, implement a robust secure procurement strategy.  Integrate cybersecurity considerations into the procurement process from the very beginning, not as an afterthought. Clearly specify cybersecurity requirements for ITS components and services in your Requests for Proposals (RFPs) and contracts. Rigorously assess potential vendors based on their cybersecurity capabilities, transparency into their supply chain, security certifications, and incident response maturity. This reduces the risk of deploying ITS components with known vulnerabilities or insecure defaults and minimizes supply chain risks that could compromise infrastructure, or data. 

## Deploy Hardened Devices

ITS hardware must include safeguards against both physical and logical attacks. This includes protection of cryptographic keys and enforcement of secure startup and update processes.

### Recommended Actions

- Integrate the ITS service operations into the organization's ISMS (information security management system) that may be based on ISO27001 or another baseline or standard.
- se tamper-resistant hardware: OBUs and RSUs should include secure elements or hardware security modules (HSMs) for key protection.
- Support secure boot: Devices must verify firmware signatures during startup.
- Enforce signed software updates: Over-the-air (OTA) updates should include cryptographic verification and rollback protection.
- Apply role-based access control (RBAC): Limit administrative interfaces to authenticated and authorized users only.
- Enable system logging and monitoring: Support detection of unauthorized changes or unexpected behavior.

Security requirements can be guided by Protection Profiles such as the (EU) [C2C-CC V2X HSM PP](https://www.car-2-car.org/fileadmin/documents/Basic_System_Profile/Release_1.3.0/C2CCC_PP_2056_HSM.pdf) or national regulatory frameworks such as UNECE R155.


## Secure Software and Firmware Updates  

Unpatched systems are a common attack vector. Implementers should verify that every device supports a secure update mechanism and that procedures are in place for scheduled updates.

### Recommended Actions
- Verify authenticity of all updates before installation (e.g., digital signature checks).
- Apply secure OTA updates using approved channels and tools.
- Restrict update privileges to trusted administrators using authentication and access control.


---

## **Learn More**  
- [IEEE 1609.2](https://standards.ieee.org/standard/1609_2-2016.html)  

- [ETSI TS 102 941](https://www.etsi.org/deliver/etsi_ts/102900_102999/102941/)  

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)  

- [Mobile ITS Security Application](https://github.com/usdot-fhwa-OPS/ITS-Secure-Prototype-Backend)

- [ITS Cybersecurity Framework Profile](https://rosap.ntl.bts.gov/view/dot/72769).  