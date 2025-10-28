# ITS geographic data (ISO TC 204 WG 3)

## Domain of interest
<!-- Domain of interest
		Do not change the following file reference. It aligns with this WG's respective domain of interest definition contained in TC204's Strategic Business Plan as approved by ISO.
-->

{% include "ag4/wg3doi.html" %}

<!-- News and highlights (optional)
	Refer docs\wg1\index.md for an example of how to include & format any desired WG news & highlights content. Add content AFTER inserting a new line below this comment. 
-->

<!-- 
	The content below is distilled from the respective WG section in "JSAE ITS Standardization Activities of ISO/TC204 - 2024" and is intended as an initial example only for future editing by the respective WG.
-->

## Geographic Data Files
<!-- Standard subject area
	Edit the ## <header title> above to contextualise the respective group of standards listed below.
-->

### Overview
<!-- Overview (optional)
  Provide an overview of the subject area and associated group of standards. 
 -->
GDF5.1 (the ISO 20524 series) is an evolution of GDF5.0 that introduces the concept of Shareable Features, takes cooperative ITS (Cooperative ITS) needs into account and is harmonized with the European public transportation standard EN 12896:2012 (Transmodel). This last harmonization was made in the framework of the European Optimise Citizen Mobility and Freight Management in Urban Environments (OPTICITIES) project.

<!-- Start web info for standard / document -->
??? note "[ISO 20524-1:2020](https://www.iso.org/obp/ui#iso:std:iso:20524:-1:ed-1:v1:en) _Intelligent transport systems — Geographic Data Files (GDF) GDF5.1 — Part 1: Application independent map data shared between multiple sources_"

    **Status:** Approved

    **Abstract:** GDF5.1 consists of two parts:

    - **GDF5.1 Part 1 (this document)** contains GDF5.0 specification except Public Transport Theme specification which has been revised and is now described in Part 2.
    - GDF5.1 Part 2 (ISO 20524-2:2020) is dedicated to Shareable Features, Cooperative ITS and Public Transport.

    ### Description

    This document presents the specification for GDF5.1 Part 1. GDF5.0 entities are unchanged but Public Transport Theme entities have been removed and corresponding sections and figures are deprecated and refer to GDF5.1 Part 2 (ISO 20524-2:2020). In order to ensure the consistency between GDF5.0 and GDF5.1 Part 1 (this document), the numbering of common figures in both versions has been conserved. GDF5.1 Part 1 (this document) is divided into several parts.

    GDF5.1 Part 1 (this document) is divided into several parts.

    - Conceptual Data Model
    - Feature Catalogue
    - Attribute Catalogue
    - Relationship Catalogue
    - Feature representation rules
    - Appendices A-H

    The actual contents of GDF, apart from a minimum set of metadata elements as specified in the delivery formats, is not specified by this document.

    This document allows the introduction of user-defined Features, Attributes and Relationships.

    ### Relationships to other standards

    GDF5.0 entities are unchanged but Public Transport Theme entities have been removed and corresponding sections and figures are deprecated and refer to GDF5.1 Part 2 (ISO 20524-2:2020).

    - [TC204 Foundation Standards](../foundational.md)
<!-- End web info for standard / document -->

<!-- Start web info for standard / document -->
??? note "[ISO 20524-2:2020](https://www.iso.org/obp/ui#iso:std:iso:20524:-2:ed-1:v1:en) _Intelligent transport systems — Geographic Data Files (GDF) GDF5.1 — Part 2: Map data used in automated driving systems, Cooperative ITS, and multi-modal transport_"

    **Status:** Approved

    **Abstract:** GDF5.1 consists of two parts:

    - GDF5.1 Part 1 (ISO 20524-1:2020) contains GDF5.0 specification except Public Transport Theme specification which has been revised and is now described in Part 2.
    - **GDF5.1 Part 2 (this document)** is dedicated to Shareable Features, Cooperative ITS and Public Transport.

    ### Description

    This document presents the specification for GDF5.1 Part 2 and is divided into several parts.

    GDF5.1 Part 1 (this document) is divided into several parts.

    - Conceptual Data Model
    - Feature Catalogue
    - Attribute Catalogue
    - Relationship Catalogue
    - Feature representation rules
    - Appendices A-I

    ### Relationships to other standards

    - [TC204 Foundation Standards](../foundational.md)

<!-- End Standard -->
<!-- End subject area -->

## Navigation Data Delivery and Structures and Protocols

??? note "[ISO 24099:2011](https://www.iso.org/obp/ui#iso:std:iso:24099:ed-1:v1:en) _Navigation data delivery structures and protocols_"

    **Status:** Approved

    **Abstract:** This International Standard was developed in relation to growing market demand for dynamic update services for map-related data in navigation systems.

    ### Description

    Map-related data includes not only feature geometry and attributes but also point of interest (POI) data such as hotels, restaurants, and dynamic content such as traffic, weather, movie schedules, parking availability, etc. Currently, most map data updates are provided on physical media whose map data content begins aging rapidly once it is delivered to the user. In the future, it is anticipated that the transmission of these data will most often, but not exclusively, be via wireless means. The advantage of wireless data delivery is that it simplifies the distribution logistics thereby accelerating the ability of a consumer to receive fresher data. This International Standard facilitates the potential for on-demand updates of on-board map databases. Further, the updates do not necessarily require the replacement of an entire map database. Rather, the updates can be limited to a portion of a dataset or a specific list of attributes or POI changes can also be provided.

    ### Relationships to other standards

    - [TC204 Foundation Standards](../foundational.md)

## External References

The European Union- ITS Communications & Information Protocols ([EU-ICIP](https://www.mobilityits.eu)) is a significant resource of ITS standards, and its [Road Traffic Data, Geographic and Spatial Data page](https://www.mobilityits.eu/road-traffic-spatial-information) is of particular relevance to this WG's work.

[How to get involved](../contact.md)
