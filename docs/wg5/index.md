# Fee and toll collection (ISO TC 204 WG 5)

## Introduction

Fees and tolls in the road transport sector are used around the world to raise revenue, manage congestion and internalize transport costs, often with the aim of contributing to more sustainable road transport.

Electronic fee collection (EFC) is the general term used to designate ICT solutions that automatically, and without stopping, collect road user fees and tolls. EFC is the general title assigned to ISO publications in the field of road fee and toll collection. EFC systems support efficient charging of road vehicles and a broad variety of pricing policies.

Currently, there are three main technologies used in EFC:

- Dedicated short-range communication (DSRC)
- Autonomous GNSS-based systems
- Image recognition-based systems (incl. ANPR aka ALPR)

## Domain of interest

{% include "ag4/wg5doi.html" %}

## EFC standardization

EFC standards provide solid technical support for agreements between stakeholders (toll chargers and toll service providers) and underpin the interoperability between EFC systems.

![Benefits of EFC standards](/assets/img/wg5benefits.png)

Benefits of EFC standards

ISO/TC 204/WG 5 is responsible for international standardization of the EFC application, whilst other international standardization groups develop technology-related standards (such as GNSS and communication technologies). Most EFC standards are developed as joint work items with [CEN/TC 278/WG 1](https://www.itsstandards.eu/its-application-areas/electronic-fee-collection/), which is responsible for standardization at European level. In addition, [ETSI](https://www.etsi.org/standards#Pre-defined%20Collections) provides certain technical standards on testing that are relevant for EFC.

Standardization in WG1 can be divided into the following areas:

- Technology-independent standards (e.g. architecture, security and information flows)
- Technology-dependent standards (DSRC-, image recognition- and GNSS-based systems)

## Overview of EFC standards

WG 5, jointly with CEN/TC 278/WG 1, has produced a series of standards, technical specifications and technical reports. These documents can be purchased from [ISO](https://www.iso.org/store.html) or national standardization bodies.

Click for a standard preview (which links to the Online Browsing Platform, which in turn provide links to on-line store for purchase of the document) or to download machine-readable files (MRFs, e.g. ASN.1 code).

### Standards and technical specifications (incl. CEN only)

|                 | **Technology-independent**  | **Technology-dependent**  |
|-----------------|-----------------------------|---------------------------|
| **Frameworks**  | [ISO 17573 -1](https://www.iso.org/obp/ui/#iso:std:iso:17573:-1) Architecture | [ISO 21719-1](https://www.iso.org/obp/ui/#iso:std:iso:21719:-1:dis:ed-1:v1:en) OBE personalization  |
|                 | [ISO 17573-2](https://www.iso.org/obp/ui/#iso:std:iso:17573:-2:dis:ed-2:v1:en) Vocabulary | |
|                 | [ISO 17573-3](https://www.iso.org/obp/ui#iso:std:iso:17573:-3) Data dictionary [[ASN.1](https://standards.iso.org/iso/17573/-3)] | |
|                 | [ISO 17574](https://www.iso.org/obp/ui/#iso:std:iso:17574:dis:ed-4:v1:en) Security profiles | |
|                 | [ISO 19299](https://www.iso.org/obp/ui/#iso:std:iso:19299) Security framework | |
| **Toolboxes**   | [ISO 12855](https://www.iso.org/obp/ui/#iso:std:iso:12855) Information exchange between TC and TSP [\[ASN.1\]](https://standards.iso.org/iso/12855/)  | [ISO 14906](https://www.iso.org/obp/ui#iso:std:iso:14906) DSRC application interface [\[ASN.1\]](https://standards.iso.org/iso/14906)  |
|                 | [ISO/TS 37444](https://www.iso.org/obp/ui#iso:std:iso:ts:37444:ed-1:v1:en) Charging performance | [ISO 16785](https://www.iso.org/obp/ui/#iso:std:iso:16785:dis:ed-1:v1:en) Interface between DSRC-OBE and external in-vehicle devices [\[ASN.1\]](http://standards.iso.org/iso/ts/16785/) |
|                 | [ISO/TS 21192](https://www.iso.org/obp/ui/#iso:std:iso:ts:21192) EFC for traffic management [\[ASN.1\]](https://standards.iso.org/iso/ts/21192/) | [ISO 25110](https://www.iso.org/obp/ui/#iso:std:iso:25110) DSRC-ICC application interface |
|                 | [ISO/TS 21193](https://www.iso.org/obp/ui/#iso:std:iso:ts:21193)  EFC using common media [\[ASN.1\]](https://standards.iso.org/iso/ts/21193/)  | ISO 17575 AID for Autonomous EFC [\[part1\]](https://www.iso.org/obp/ui/#iso:std:iso:17575:-1)[\[part2\]](https://www.iso.org/obp/ui/#iso:std:iso:17575:-2)[\[part3\]](https://www.iso.org/obp/ui/#iso:std:iso:17575:-3)[\[ASN.1\]](http://standards.iso.org/iso/17575) |
|                 |   | [CEN/TS 16702](https://standards.cen.eu/dyn/www/f?p=204:105:0:::::) Secure monitoring [\[part1\]](https://standards.cen.eu/dyn/www/f?p=204:110:0::::FSP_PROJECT:65303&cs=15049F640ADFD060428A163E0833B68C1)[\[part2\]](https://standards.cen.eu/dyn/www/f?p=204:110:0::::FSP_PROJECT:66755&cs=16393979C7D6600E5CC18239BBAE6C620)[\[ASN.1\]](https://www.itsstandards.eu/app/uploads/sites/14/2021/12/CEN16702-22020.asn) |
| **Profiles**    | [EN 16986](https://standards.cen.eu/dyn/www/f?p=204:105:0:::::) IAP for information exchange between TC and TSP [\[MRFs\]](https://www.itsstandards.eu/standards/) | EN 15509 IAP for DSRC EFC [\[ASN.1\]](https://www.itsstandards.eu/app/uploads/sites/14/2022/05/EN155092022CenEfcDsrcApplicationv1.asn) |
|                 | | ISO/TS 21719 OBE personalization [\[part1\]](https://www.iso.org/obp/ui/#iso:std:iso:ts:21719:-2) [\[part2\]](https://www.iso.org/obp/ui/#iso:std:iso:ts:21719:-3) |
|                 | | [ISO 12813](https://www.iso.org/obp/ui/#iso:std:iso:12813) Compliance check communication (CCC) [\[ASN.1\]](https://standards.iso.org/iso/12813/) |
|                 | | [ISO 13141](https://www.iso.org/obp/ui#iso:std:iso:13141) Localization augmentation communication (LAC) [\[ASN.1\]](https://standards.iso.org/iso/13141/) |
| **Tests**       | [CEN/TS 17154](https://standards.cen.eu/dyn/www/f?p=204:105:0:::::) Tests against 16986 [[part1]](https://www.itsstandards.eu/standards/) | [ISO 14907-1](https://www.iso.org/obp/ui/#iso:std:iso:14907:-1) Test procedures for user and fixed equipment |
|                 | | [ISO 14907-2](https://www.iso.org/obp/ui/#iso:std:iso:14907:-2) OBU tests against 14906  |
|                 | | [EN 15876](https://standards.cen.eu/dyn/www/f?p=204:105:0:::::) Tests against 15509 |
|                 | | [CEN/TS 18078](https://standards.cencenelec.eu/dyn/www/f?p=CEN:105::RESET::::) RLAN interferences to DSRC |
|                 | | [ISO 13143](https://www.iso.org/obp/ui/#iso:std:iso:13143) Tests against 12813 |
|                 | | [ISO 13140](https://www.iso.org/obp/ui/#iso:std:iso:13140:-1) Tests against 13141 |
|                 | | ISO 16407 Tests against 17575-1 [\[part1\]](https://www.iso.org/obp/ui/#iso:std:iso:16407:-1)[\[part2\]](https://www.iso.org/obp/ui/#iso:std:iso:16407:-2)[\[TTCN\]](https://standards.iso.org/iso/16407/) |
|                 | | [ISO 16410](https://www.iso.org/obp/ui/#iso:std:iso:16410:-1) Tests against 17575-3 [\[part1\]](https://www.iso.org/obp/ui/#iso:std:iso:16410:-1)[\[part2\]](https://www.iso.org/obp/ui/#iso:std:iso:16410:-2)[][](https://www.iso.org/standard/70050.html)[\[TTCN\]](https://standards.iso.org/iso/16410/) |

## Contact us

Want to know more or participate? Please contact us.

![Contact us](/assets/img/wg5pics.png)

## Resources / presentations

- [Introduction to EFC standards](https://wpn.nen.nl/app/uploads/sites/14/2025/05/Introduction-to-EFC-stds-1.pdf)
- [CO2-based tolling – Eurovignette Directive and EFC standards](https://wpn.nen.nl/app/uploads/sites/14/2025/05/CO2-based-tolling-Eurovignette-Directive-and-EFC-standards.pdf)
