# Domains of Interest
Each TC204 WG focuses on a specific domain of interest, comprising of multiple key concepts.

# ITS Foundational Documents
Documents from various working groups define [TC204's foundational documents](foundational.md) upon which the remainder of concepts are built.
 
# ARC-IT Foundational Service Packages
[ARC-IT](https://www.arc-it.net) presents a multitude of [service packages](https://www.arc-it.net/html/servicepackages/servicepackages-areaspsort.html) (which are similar to FRAME "solution patterns"). Each service package represents a slice of the architecture that address a specific ITS service (e.g., traffic signal control) and is often visually represented using a physical view diagram that depicts physical objects connected with information flows.  Within [ARC-IT], each information flow depicted on a physical view diagram is hyperlinked to a communication view, which identifies specific standards that can be used to implement the flow and provides the likely geographic context for each identified solution. 

The diagram below shows the ITS Services that ARC-IT classifies as support packages.  By interrogating these support service packages, it is possible to identify what this site considers the **foundational standards**.

![ARC-IT Support (Foundational Service Packages)](https://github.com/user-attachments/assets/a49c5d06-aaab-4c80-a9ac-9a3dc4d93076){.figure}

*Foundational Service Packages*{.figcaption}


## [Example: SU05: Location and Time](https://www.arc-it.net/html/servicepackages/sp108.html#tab-3)
This service package identifies the external systems and interfaces that provide accurate location and time to intelligent transportation system devices and systems. Relevant Regions: Australia, Canada, European Union, and United States

A physical view of the service package is shown below

![physical108 SU05](https://github.com/user-attachments/assets/7c42c5d4-8096-41a8-af6f-31685f871cdc)

Each information flow on the ARC-IT website is hyperloinked. For example, by clicking on the information flow **_(1C) time local form_** between **_Center_** and **_Service Monitor System_**

![(1C) time local form](https://github.com/user-attachments/assets/eb8c64c9-d3a6-4e93-a864-d816a8f84e6c)

ARC-IT provides the following definition:
>The Communciation solution **NTP - UDP/IP** is used within Australia, Canada, the E.U. and the U.S.. It combines standards associated with NTP with those for I-I: UDP/IP. The NTP standards include standards required to reliably set time information in a subsystem. The I-I: UDP/IP standards include lower-layer standards that support the Network Time Protocol that allows NTP servers to provide time synchronization services to other NTP servers and clients.

And by clicking on the "Communication Solutions" tab, the user can reveal the communication view diagram as follows:

>![NTP - UDP_IP](https://github.com/user-attachments/assets/65ac3b5c-473d-437a-98ae-c977f915daac)

 
