<!-- work.md -->

# Work for ISO TC 204

The following sortable table lists the WGs and topic areas included within ISO TC 204.

|Group            | Topic                          |
|-----------------|--------------------------------|
|[WG 14](wg14/index.md)   | Active safety systems          |
|[WG 1](wg1/index.md)     | Architecture                   |
|[WG 20](wg20/index.md)   | Artificial intelligence        |
|[WG 20](wg20/index.md)   | Big data                       |
|[JWG 1](jwg1/index.md)   | City data model                |
|[WG 7](wg7/index.md)     | Commercial vehicles            |
|[WG 16](wg16/index.md)   | Communications                 |
|[WG 18](wg18/index.md)   | Cooperative systems            |
|[AHG 2](ahg2/index.md)   | Cybersecurity                  |
|[WG 14](wg14/index.md)   | Driving automation             |
|[WG 5](wg5/index.md)     | Electronic fee collection      |
|[WG 19](wg19/index.md)   | Electronic traffic regulations |
|[WG 8](wg8/index.md)     | Emergency management           |
|[WG 5](wg5/index.md)     | Fee collection                 |
|[WG 7](wg7/index.md)     | Fleet management               |
|[WG 7](wg7/index.md)     | Freight management             |
|[JWG 11](tc211jwg11/index.md) | Geographic information systems |
|[AG 2](ag2/index.md)     | Identifier registry            |
|[WG 9](wg9/index.md)     | Integrated transport information, management and control|
|[WG 3](wg3/index.md)     | ITS geographic data            |
|[AG 5](ag5/index.md)     | Marketing review               |
|[WG 19](wg19/index.md)   | Mobility integration           |
|[WG 17](wg17/index.md)   | Nomadic devices                |
|[WG 1](wg1/index.md)     | Ontology                       |
|[AG 3](ag3/index.md)     | Operational improvement        |
|[WG 19](wg19/index.md)   | Parking                        |
|[AG 4](ag4/index.md)     | Program coordination           |
|[WG 19](wg19/index.md)   | Public area mobile robots      |
|[WG 8](wg8/index.md)     | Public transport               |
|[JWG 1](jwg1/index.md)   | Smart Cities                   |
|[WG 5](wg5/index.md)     | Toll collection                |
|[WG 9](wg9/index.md)     | Traffic management systems     |
|[WG 10](wg10/index.md)   | Traveller information systems  |
|[WG 1](wg1/index.md)     | Vocabulary                     |

## Domains of Interest

Each TC204 WG focuses on a specific domain of interest. The page for each WG identifies the domain of interest for that WG along with a description underway within that WG.

## ITS Foundational Documents

Documents from various working groups define [TC204's foundational documents](foundational.md) upon which the remainder of concepts are built.

## ARC-IT Foundational Service Packages

[ARC-IT](https://www.arc-it.net) presents a multitude of [service packages](https://www.arc-it.net/html/servicepackages/servicepackages-areaspsort.html) (which are similar to FRAME "solution patterns"). Each service package represents a slice of the architecture that addresses a specific ITS service (e.g., traffic signal control) and is often visually represented using a _physical view_ diagram that depicts _physical objects_ connected with _information flows_.  Within ARC-IT, each information flow depicted on a physical view diagram is hyperlinked to a _communication view_, which identifies specific standards that can be used to implement the flow and provides the likely geographic context for each identified solution.

The diagram below shows the ITS Services that ARC-IT classifies as support packages.  By interrogating these support service packages, it is possible to identify what this site considers the **foundational standards**.

![ARC-IT Support (Foundational Service Packages)](https://github.com/user-attachments/assets/a49c5d06-aaab-4c80-a9ac-9a3dc4d93076){.figure}

/// caption
Foundational Service Packages
///

### [Example: SU05: Location and Time](https://www.arc-it.net/html/servicepackages/sp108.html#tab-3)

As an example, the Location and Time service package identifies the external systems and interfaces that provide accurate location and time to intelligent transportation system devices and systems. Relevant Regions: Australia, Canada, European Union, and United States

A physical view of the service package is shown below

![physical108 SU05](https://github.com/user-attachments/assets/7c42c5d4-8096-41a8-af6f-31685f871cdc)

Each information flow on the ARC-IT website is hyperlinked. For example, when a user clicks on the information flow _(1C) time local form_ between _Center_ and _Service Monitor System_,

![(1C) time local form](https://github.com/user-attachments/assets/eb8c64c9-d3a6-4e93-a864-d816a8f84e6c)

ARC-IT will display the following definition:

>The communication solution **NTP - UDP/IP** is used within Australia, Canada, the E.U. and the U.S.. It combines standards associated with NTP with those for I-I: UDP/IP. The NTP standards include standards required to reliably set time information in a subsystem. The I-I: UDP/IP standards include lower-layer standards that support the Network Time Protocol that allows NTP servers to provide time synchronization services to other NTP servers and clients.

And by clicking on the "Communication Solutions" tab, the user can reveal the communication view diagram as follows:

>![NTP - UDP_IP](https://github.com/user-attachments/assets/65ac3b5c-473d-437a-98ae-c977f915daac)
