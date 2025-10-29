# Traveller information (ISO TC 204 WG 10)

## Domain of interest
<!-- DO NOT CHANGE THIS FILE REFERENCE! It aligns with this WG's respective domain of interest definition contained in TC204's Strategic Business Plan as approved by ISO. -->

{% include "ag4/wg10doi.html" %}

<!-- ## News and highlights (optional)
    Refer docs\wg1\index.md for an example of how to include & format any desired WG news & highlights content. Add content AFTER inserting a new line below this comment. 
-->

<!-- === DESCRIPTIONS OF WG STANDARDS / DOCUMENTS ===
    The content below is distilled from the respective WG section in "JSAE ITS Standardization Activities of ISO/TC204 - 2024" and iso.org/obp and is intended as an initial example only for future editing by the respective WG.
-->

## Traffic and Traveller Information via TPEG2
<!-- Standard subject area
    Edit the ## <header title> above to contextualise the respective group of standards described below.
-->

### Overview <!-- Optional -->
<!-- On a new line below, provide an overview of the subject area for the associated group of standards. -->
When the Traveller Information Services Association (TISA), derived from former forums, was inaugurated in December 2007, TPEG development was taken over by TISA and continued in the TPEG applications working group. TISA set about the development of a new TPEG structure that would be UML-based. This has subsequently become known as TPEG Generation 2 (TPEG2).

TPEG2 is embodied in the ISO 21219 series and it comprises many parts covering the introduction, rules, toolkit and application components.

The following classification provides a helpful grouping of the different TPEG2 parts according to their intended purpose. Note that the list below is potentially incomplete, as it is possible that new TPEG2 parts will be introduced in future.

- **Toolkit parts:** TPEG2-INV (ISO 21219-1), TPEG2-UML (ISO 21219-2), TPEG2-UBCR (ISO 21219-3), TPEG2-UXCR (ISO 21219-4), TPEG2-SFW (ISO 21219-5), TPEG2-MMC (ISO 21219-6), TPEG2-LRC (ISO/TS 21219-7).
- **Special applications:** TPEG2-SNI (ISO 21219-91), TPEG2-CAI (ISO 21219-102), TPEG2-LTE (ISO/TS 21219-24).
- **Location referencing:** TPEG2-OLR (ISO/TS 21219-22), TPEG2-GLR (ISO/TS 21219-21), TPEG2-TLR (ISO 17572-2), TPEG2-DLR (ISO 17572-3).
- **Applications:** TPEG2-PKI (ISO 21219-143), TPEG2-TEC (ISO 21219-154), TPEG2-FPI (ISO 21219-165), TPEG2-TFP (ISO 21219-18), TPEG2-WEA (ISO 21219-196), TPEG2-RMR (ISO/TS 21219-23), TPEG2-EMI (ISO/TS 21219-25), TPEG2-VLI (ISO/TS 21219-26).

TPEG2 has been developed to be broadly (but not totally) backward compatible with TPEG1 to assist in transitions from earlier implementations, while not hindering the TPEG2 innovative approach and being able to support many new features, such as dealing with applications with both long-term, unchanging content and highly dynamic content, such as parking information.

<!-- Start web info for standard / document -->
??? note "[ISO 21219-1:2023](https://www.iso.org/obp/ui#iso:std:iso:21219:-1:ed-1:v1:en) _Intelligent transport systems — Traffic and travel information (TTI) via transport protocol experts group, generation 2 (TPEG2) — Part 1: Introduction, numbering and versions (TPEG2-INV)_"
    <!-- edit document reference information
      retain: ??? note "[ : ]( ) _ _"
      find publicly available ISO document URL & info here: iso.org/obp/ui
    -->

    **Status:** Approved
   <!-- Copy relevant status line from the following list: 
      Edition 1 **(under development)**{style="color: red;"}
      Approved
      Approved **(under revision)**{style="color: red;"} 
    -->

    **Abstract:** This document defines an index to the complete set of TPEG Generation 2 toolkit components and applications. New applications are enumerated with an application identification (AID) as they are added to the TPEG applications family.
    
    **Description:**
    
    - NOTE 1 This document will be updated when new applications occur in order to indicate the latest status and the inter-working of the various TPEG specifications. This document will be revised as a new edition every time a new issue of any other specification is issued.
    
    - NOTE 2 Preliminary AIDs are allocated and managed by TISA. Refer external references below.
    
    **Normative References:**
    
    There are no normative references in this document.
    
    **Relationships to other standards:**
  <!-- Relationships to other standards
      e.g., list Normative references and comm stack references
      *** PLEASE *** retain the link to "TC204 Foundational Standards" as the first relationship in the list below 
    -->

    - [TC204 Foundation Standards](../foundational.md)
    
  <!-- End Standard -->

<!-- Start web info for standard / document -->
??? note "[ISO TS 21219-13:2025](https://www.iso.org/obp/ui#iso:std:iso:ts:21219:-13:ed-1:v1:en) _Intelligent transport systems — Traffic and travel information (TTI) via transport protocol experts group, generation 2 (TPEG2) — Part 13: Public transport information service (TPEG2-PTS)_"

    **Status:** Approved **(under review)**{style="color: red;"}
  <!-- Copy relevant status line from the following list: 
      Edition 1 **(under development)**{style="color: red;"}
      Approved
      Approved **(under revision)**{style="color: red;"} 
    -->

    **Abstract:** This document describes the “public transport information service” (PTS) application, which is intended to cover all modes of public (i.e. collective) transport, both for inter-urban and intra-urban travel. The PTS application is designed to allow the efficient and language-independent delivery of public transport information directly from a service provider to end-users.
    
    **Description:**
    
    The PTS application design is based on three main use cases.
    
    - **Provision of alert information:** an alert is a warning that indicates an emergency situation. This case is specifically relevant for broadcast/push mode, for major deviations or disruptions which are relevant for a large number of travellers. A dedicated alert request is also defined and can be used if a backchannel is available.
    
    - **Timetable information, both scheduled and real time:** this information is in some cases relevant for broadcast, e.g. in case of large events for the transport modalities to/from the event site. A dedicated timetable request is also defined and can be used if a backchannel is available.
    
    - **Individual requests for trip information** (backchannel is required).
    
    The PTS application focuses on providing core information regarding public transport in order to ensure the compactness of the TPEG application. Specific information as provided in typical public transport apps (e.g. fare information) is not in the scope of this document.
 
    **Normative References:**
    
    The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.
    
    - ISO 21219-1, Intelligent transport systems — Traffic and travel information (TTI) via transport protocol experts group, generation 2 (TPEG2) — Part 1: Introduction, numbering and versions (TPEG2-INV)
    - ISO 21219-7, Intelligent transport systems — Traffic and travel information (TTI) via transport protocol experts group, generation 2 (TPEG2) — Part 7: Location referencing container (TPEG2-LRC)
    - ISO 21219-9, Intelligent transport systems — Traffic and travel information (TTI) via transport protocol experts group, generation 2 (TPEG2) — Part 9: Service and network information (TPEG2-SNI)
    - ISO 21219-14, Intelligent transport systems — Traffic and travel information (TTI) via transport protocol experts group, generation 2 (TPEG2) — Part 14: Parking information (TPEG2-PKI)
    - ISO 21219-15, Intelligent transport systems — Traffic and travel information (TTI) via transport protocol experts group, generation 2 (TPEG2) — Part 15: Traffic event compact (TPEG2-TEC)   
 
    **Relationships to other standards:**
  <!-- Relationships to other standards
      e.g., list Normative references and comm stack references
      *** PLEASE *** retain the link to "TC204 Foundational Standards" as the first relationship in the list below 
    -->

    - [TC204 Foundation Standards](../foundational.md)
    
  <!-- End Standard -->

<!-- End subject area -->

## External References

- The European Union- ITS Communications & Information Protocols ([EU-ICIP](https://www.mobilityits.eu)) is a significant resource of ITS standards, and its [Traffic and Traveller information page](https://www.mobilityits.eu/traffic-transport-information) is of particular relevance to this WG's work.

- [TISA](http://www.tisa.org/)

[How to get involved](../contact.md)
