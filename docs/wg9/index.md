# Integrated transport information, management and control (ISO TC 204 WG 9)

## Domain of interest
<!-- DO NOT CHANGE THIS FILE REFERENCE! It aligns with this WG's respective domain of interest definition contained in TC204's Strategic Business Plan as approved by ISO. -->

{% include "ag4/wg9doi.html" %}

<!-- ## News and highlights (optional)
    Refer docs\wg1\index.md for an example of how to include & format any desired WG news & highlights content. Add content AFTER inserting a new line below this comment. 
-->

<!-- === DESCRIPTIONS OF WG STANDARDS / DOCUMENTS ===
    The content below is distilled from the respective WG section in "JSAE ITS Standardization Activities of ISO/TC204 - 2024" and iso.org/obp and is intended as an initial example only for future editing by the respective WG.
-->

## Field device Simple Network Management Protocol (SNMP) data interface
<!-- Standard subject area
    Edit the ## <header title> above to contextualise the respective group of standards described below.
-->

### Overview <!-- Optional -->

The ISO 26048 series defines data that can be used to manage field devices, including device configuration, control and monitoring. Field devices can be quite complex, necessitating the standardization of many data concepts for exchange. As such, the ISO 26048 series is divided into several individual parts.

The scope of the ISO 26048 series does not define the logic used by the management station, the underlying protocols used to exchange the defined data elements, or internal design of the field device. However, the ISO 26048 series does define functional requirements on the interface and assumes an interface based on an SNMPv3 environment as specified by ISO 15784-2.

<!-- Start web info for standard / document -->
??? note "[ISO/TS 26048-1:2025](https://www.iso.org/obp/ui#iso:std:iso:ts:26048:-1:ed-1:v1:en) _Intelligent transport systems — Field device Simple Network Management Protocol (SNMP) data interface — Part 1: Global objects_"

    **Status:** Approved

    **Abstract:** This document (ISO/TS 26048-1) introduces the ISO 26048 series, provides content that is normatively referenced in subsequent parts, and defines data that is applicable to the management of a wide range of field devices.

    ### Description

    **NOTE** Many of the concepts defined in this document were derived from NTCIP 1103 and NTCIP 1201, however, the design has been updated to better address security concerns. It is expected that future versions of NTCIP will migrate to the design defined in this document.

    ### Relationships to other standards
    <!-- Relationships to other standards
      e.g., list Normative references and comm stack references
      PLEASE retain the link to "TC204 Foundational Standards" as the first relationship in the list below 
    -->

    - [TC204 Foundation Standards](../foundational.md)

    #### Normative References

    The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

    - ISO 15784-2 Intelligent transport systems — Data exchange involving roadside modules communication — Part 2: Centre to field device communications using Simple Network Management Protocol (SNMP)
    - ISO/IEC 8825-1 Information technology — ASN.1 encoding rules — Part 1: Specification of Basic Encoding Rules (BER), Canonical Encoding Rules (CER) and Distinguished Encoding Rules (DER)
    - ISO/IEC 8825-7 Information technology — ASN.1 encoding rules — Part 7: Specification of Octet Encoding Rules (OER)
    - ISO/IEC/IEEE 24765 Systems and software engineering — Vocabulary
    - ISO/TS 14812 Intelligent transport systems — Vocabulary
    - RFC 3415 View-based Access Control Model (VACM) for the Simple Network Management Protocol (SNMP)
    - RFC 5424 The Syslog Protocol
    - RFC 5676 Definitions of Managed Objects for Mapping SYSLOG Messages to Simple Network Management Protocol (SNMP) Notifications
    - RFC 8446 The Transport Layer Security (TLS) Protocol Version 1.3
    - [File Transfer Protocol S.S.H.](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-02), October 2001.
<!-- End Standard -->

<!-- Start web info for standard / document -->
??? note "[ISO/AWI TS 26048-3](https://www.iso.org/standard/87055.html?browse=tc) _Intelligent transport systems — Field device SNMP data interface — Part 3: Variable and dynamic message signs_"

    **Status:** Edition 1 **(under development)**{style="color: red;"}

    **Abstract:** This document identifies basic user needs for the management of light-emitting diode (LED) matrix Variable and dynamic message signs(VDMSs) and traces these needs to interoperable designs. This includes the ability to identify the device, its capabilities, and its status.

    ### Description

    Variable and dynamic message signs(VDMSs) are installed in areas where traffic managers identify a frequent need to convey information to the travelling public, such as upstream from interchanges to alert the public to downstream congestion in time for them to alter their routes. This allows traffic managers to improve the efficiency, safety, and quality of traveller journeys. In order to manage the operation of a VDMS and the messages displayed, information exchange between the management systems and the VDMS is needed.

    ### Relationships to other standards

    - [TC204 Foundation Standards](../foundational.md)

<!-- End Standard -->

<!-- End subject area -->

## External References

The European Union- ITS Communications & Information Protocols ([EU-ICIP](https://www.mobilityits.eu)) is a significant resource of ITS standards, and its [Traffic Control & Management page](https://www.mobilityits.eu/traffic-control-management) is of particular relevance to this WG's work.

[How to get involved](../contact.md)
