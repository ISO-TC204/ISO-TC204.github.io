# Domains of Interest
Each TC204 WG focuses on a specific domain of interest, comprising of multiple key concepts

TC204 standards are grouped by the first 2 levels of the titles of Current / Active standards as follows:

| 1st Level Grouping | 2nd Level Grouping |
| -- | --|
| Automatic vehicle and equipment identification (AV & EI) | Electronic registration identification (ERI) for vehicles |
| Electronic Fee Collection (EFC) | AID for Autonomous Systems |
| | AID for DSRC  |
| | Architecture |
| | Eval Conformity to ISO 17575  |
| | Eval Conformity to ISO 12813  |
| | Eval Conformity to ISO 13141 |
| | Other |
| Intelligent Transport Systems (ITS) | APS |
| | Architecture |



# ITS Foundational Documents
Documents from various working groups define [TC204's foundational documents](foundational.md) upon which the remainder of concepts are built.
 
# ARC-IT Foundational Service Packages
🚧 Among many other things, ARC-IT presents a multitude of [service packages](https://www.arc-it.net/html/servicepackages/servicepackages-areaspsort.html) (akin to solution patterns) that describe information flows by in terms of "triples" (an information flow between two functional objects). Each of these triples is defined in terms of the ITS station, and by digging a little deeper **the specific standards that describe aspects of each component** in context of certain geographic locations. 
<br> 

The diagram below groups multiple service packages that **support** other service packages, or perhaps in other words **foundational service packages**.  By interrogating these support service packages, it is therefore possible to essentially identify the **foundational standards**.
![ARC-IT Support (Foundational Service Packages)](https://github.com/user-attachments/assets/a49c5d06-aaab-4c80-a9ac-9a3dc4d93076)


## [Example: SU05: Location and Time](https://www.arc-it.net/html/servicepackages/sp108.html#tab-3)
>This service package identifies the external systems and interfaces that provide accurate location and time to intelligent transportation system devices and systems. Relevant Regions: Australia, Canada, European Union, and United States
>
>A physical view of the service package is shown below
>>![physical108 SU05](https://github.com/user-attachments/assets/7c42c5d4-8096-41a8-af6f-31685f871cdc)
>
>Consider the information flow **_(1C) time local form_** between **_Center_** and **_Service Monitor System_**
>>![(1C) time local form](https://github.com/user-attachments/assets/eb8c64c9-d3a6-4e93-a864-d816a8f84e6c)
>
>ARC-IT shows:
><table><tr><td> <i> The Communciation solution **NTP - UDP/IP** is used within Australia, Canada, the E.U. and the U.S.. It combines standards associated with NTP with those for I-I: UDP/IP. The NTP standards include standards required to reliably set time information in a subsystem. The I-I: UDP/IP standards include lower-layer standards that support the Network Time Protocol that allows NTP servers to provide time synchronization services to other NTP servers and clients. </i> </td></tr></table>
>
>The standards used in the Communication solution are shown below
>>>![NTP - UDP_IP](https://github.com/user-attachments/assets/65ac3b5c-473d-437a-98ae-c977f915daac)

 
