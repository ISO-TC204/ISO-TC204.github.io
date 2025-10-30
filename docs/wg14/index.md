# Driving automation and active safety systems (ISO TC 204 WG 14)

## Domain of interest

{% include "ag4/wg14doi.html" %}

<!-- ## News and highlights (optional)
    Refer docs\wg1\index.md for an example of how to include & format any desired WG news & highlights content. Add content AFTER inserting a new line below this comment. 
-->

<!-- === DESCRIPTIONS OF WG STANDARDS / DOCUMENTS ===
    The content below is distilled from the respective WG section in "JSAE ITS Standardization Activities of ISO/TC204 - 2024" and iso.org/obp and is intended as an initial example only for future editing by the respective WG.
-->

## Motorway chauffeur systems
<!-- Standard subject area
    Edit the ## <header title> above to contextualise the respective group of standards described below.
-->

### Overview <!-- Optional -->
<!-- On a new line below, provide an overview of the subject area for the associated group of standards. -->
The ISO 23792 series identifies the performance requirements for an ADS based on its capability to respond to certain conditions and situations. The requirements are derived in order to reliably transfer the control between the human driver and ADS, and for safe operation by the ADS.

The ISO 23792 series focuses on the system functionalities, under the assumption that the FRU is available and responsive to system requests to take over driving tasks.

<!-- Start web info for standard / document -->
??? note "[ISO/TS 23792-1:2023](https://www.iso.org/obp/ui#iso:std:iso:ts:23792:-1:ed-1:v1:en) _Intelligent transport systems — Motorway chauffeur systems (MCS) — Part 1: Framework and general requirements_"
    <!-- edit document reference information
      retain: ??? note "[ : ]( ) _ _"
      find publicly available ISO document URL & info here: iso.org/obp/ui
    -->

    **Status:** Approved **(under revision)**{style="color: red;"}
    <!-- Copy relevant status line from the following list: 
      Edition 1 **(under development)**{style="color: red;"}
      Approved
      Approved **(under revision)**{style="color: red;"} 
    -->

    **Abstract:** This document specifies requirements of the basic set of functionalities and test procedures to verify these requirements. The requirements include vehicle operation to perform the entire dynamic driving task (DDT) within the current lane of travel, to issue a request to intervene (RTI) before disengaging, and to extend operation and temporarily continue to perform the DDT after issuing an RTI.
    
    **Description:**
    
    This document describes one specific form of system engagement. Other forms are possible. These other system engagement forms, especially those provided in combination with other driving automation system features, are not within the scope of this document.
    
    Requirements and test procedures for the additional functionalities are provided in other parts of the ISO 23792 series.
    
    Means related to setting a destination and selecting a route to reach the destination are not within the scope of this document.
    
    This document applies to MCS installed in light vehicles.
 
    **Normative References:**
    
    The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.
    
    - ISO 15622:2018, Intelligent transport systems — Adaptive cruise control systems — Performance requirements and test procedures
    - ISO/SAE PAS 22736, Taxonomy and definitions for terms related to driving automation systems for on-road motor vehicles   
 
    **Relationships to other standards:**
    <!-- Relationships to other standards
      e.g., list Normative references and comm stack references
      *** PLEASE *** retain the link to "TC204 Foundational Standards" as the first relationship in the list below 
    -->

    - [TC204 Foundation Standards](../foundational.md)

    <!-- End Standard -->

<!-- Start web info for standard / document -->
??? note "[ISO/DIS 23792-2](https://www.iso.org/obp/ui#iso:std:iso:ts:23792:-1:ed-1:v1:en) _Intelligent transport systems — Motorway chauffeur systems (MCS) — Part 2: Requirements and test procedures for discretionary lane change_"

    **Status:** Edition 1 **(under development)**{style="color: red;"}
    <!-- Copy relevant status line from the following list: 
      Edition 1 **(under development)**{style="color: red;"}
      Approved
      Approved **(under revision)**{style="color: red;"} 
    -->

    **Abstract:** This document specifies the requirements and test procedure to verify the requirements for the discretionary lane change functionality (DLC).
    
    **Description:**
    
    The DLC is an additional functionality that a MCS compliant to the general requirements specified in ISO 23792-1 can be equipped with. When conditions are satisfied, a DLC equipped MCS performs the entire DDT to change the current lane of travel even though it is still possible to continue operation within its current lane of travel. The system monitors the driving environment in the adjacent lanes and operates the SV by adjusting the speed and lateral position to move the SV to the intended lane. MCS may delay the manoeuvre until the conditions for initiating the lane change are satisfied or cancel the lane change when conditions are not satisfied. Activation of the DLC requires an engaged MCS performing in-lane driving. Means related to setting a destination and selecting a route to reach the destination are not in the scope of this document.
    
    This document applies to the system installed in light vehicles
    <!-- End Standard -->

    **Relationships to other standards:**
    <!-- Relationships to other standards
      e.g., list Normative references and comm stack references
      *** PLEASE *** retain the link to "TC204 Foundational Standards" as the first relationship in the list below 
    -->

    - [TC204 Foundation Standards](../foundational.md)

<!-- End subject area -->

## External References

The European Union- ITS Communications & Information Protocols ([EU-ICIP](https://www.mobilityits.eu)) is a significant resource of ITS standards, and its [Vehicle/Roadway Warning/Control page](https://www.mobilityits.eu/vehicle-roadway-warning-control) is of particular relevance to this WG's work.

- ISO/SAE PAS 22736, Taxonomy and definitions for terms related to driving automation systems for on-road motor vehicles
- [International Organization of Motor Vehicle Manufacturers, Vehicle type definitions](https://oica.net/statistics-production/)

[How to get involved](../contact.md)
