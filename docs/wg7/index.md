# General fleet management and commercial/freight (ISO TC 204 WG 7)

## Domain of interest
<!-- Domain of interest
		Do not change the following file reference. It aligns with this WG's respective domain of interest definition contained in TC204's Strategic Business Plan as approved by ISO.
-->

{% include "ag4/wg7doi.html" %}

<!-- News and highlights (optional)
	Refer docs\wg1\index.md for an example of how to include & format any desired WG news & highlights content. Add content AFTER inserting a new line below this comment. 
-->

<!-- 
	The content below is distilled from the respective WG section in "JSAE ITS Standardization Activities of ISO/TC204 - 2024" and is intended as an initial example only for future editing by the respective WG.
-->

<!-- Start web info for Standard subject area -->
## Data Dictionary and Message Sets
<!-- Standard subject area
  Edit the ## <header title> above to contextualise the respective group of standards described below.
-->

### Overview
<!-- Overview (optional)
  Provide an overview of the subject area and associated group of standards. 
 -->

<!-- Start web info for standard / document -->

??? note "[ISO 17687:2007](https://www.iso.org/obp/ui/#iso:std:iso:17687:ed-1:v1:en) _Transport Information and Control Systems (TICS) — General fleet management and commercial freight operations — Data dictionary and message sets for electronic identification and monitoring of hazardous materials/dangerous goods transportation_"

    **Status:** Approved

    **Abstract:** This International Standard supports the automated identification, monitoring and exchange of emergency response information regarding dangerous goods carried on board road transport vehicles.

    ### Description

    Such information may include the identification, quantity and current condition (such as pressure and temperature) of such goods, as well as any relevant emergency response information. Reporting this information may occur prior to or during transportation of the goods in a manner that allows all interested parties to access and interpret the information correctly. When equipped with appropriate electronics and communications capabilities, vehicles carrying dangerous goods may respond to queries regarding their status or self-initiate a message.

    This International Standard does not specify nor even imply that any particular on-board or off-board systems should be capable of performing such monitoring, data retention or communications. However, where such capability does exist, then this International Standard does apply. This International Standard does not intend to affect any country’s laws and regulations regarding dangerous goods transportation, but offers means to electronically support emergency response practices by providing a standard for electronic identification and monitoring messages.

    The provisions of this International Standard cover four contextual situations:

    1. general requirements;
    2. on-board systems;
    3. roadside recipient to emergency control centres;
    4. emergency control centres to emergency control centres.

    It is intended that the information defined here be carried on board the transport vehicle and may then be transferred to interested roadside systems by whatever communications means are appropriate to that roadside system.

    ### Relationships to other standards

    - [TC204 Foundation Standards](../foundational.md)

    The following referenced documents are indispensable for the application of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

    The reader is advised to pay careful attention to 5.5, “Important implementation recommendation”.

    - ISO/IEC 8824 (all parts), Information technology — Abstract Syntax Notation One (ASN.1)
    - ISO/IEC 8825 (all parts), Information technology — ASN.1 encoding rules
    - ISO 14817, Transport information and control systems — Requirements for an ITS/TICS central Data Registry and ITS/TICS Data Dictionaries
    - IEEE 1512.3, IEEE Standard for free hazardous material incident management message sets for use by emergency management centers
    - NFPA 704, Identification of the Free Hazards of Materials for Emergency Response
    - SAE J2313, On-board land vehicle mayday reporting interface
    - SAE 2540.ITIS, ITIS phrases list

## Electronic information exchange

### Overview

??? note "[ISO/TS 24533:2012](https://www.iso.org/obp/ui/#iso:std:iso:ts:24533:ed-1:v1:en) _Intelligent transport systems — Electronic information exchange to facilitate the movement of freight and its intermodal transfer — Road transport information exchange methodology_"

    **Status:** Approved

    **Abstract:** Seamless exchange of accurate, complete, and timely data at transportation hand-offs has always been important for efficiency and accountability. There is also an understanding of needs for security of transport information, and for transfer of information related to security against terrorism as well as theft and traditional contraband. It is imperative for standards development organizations to address and facilitate dealing with these needs.

    ### Description

    ISO/TR 14813-2:2000, 7.4.1 identifies a commercial vehicle functional domain:

    - "These transactions maintain the TICS information about a shipment from the time of the order by the consignor to the reception of goods by the consignee. The key TICS transactions are to provide registers of service providers and to enable the goods to be tracked throughout intermodal journeys."

    ### Relationships to other standards

    ⚠️ Note: This edition has been been replaced by (ISO/TS 24533-2:2022), which has been technically revised.

    - [TC204 Foundation Standards](../foundational.md)

??? note "[ISO 24533-2:2022](https://www.iso.org/obp/ui/#iso:std:iso:ts:24533:ed-1:v1:en) _Intelligent transport systems — Electronic information exchange to facilitate the movement of freight and its intermodal transfer — Part 2: Common reporting system_"

    **Status:** Approved

    ⚠️ Note: This first edition cancels and replaces the first edition (ISO/TS 24533:2012), which has been technically revised.

    The main changes are as follows:

    - removal of information on the interoperability of freight data exchange standards (intended to be the subject of ISO/AWI 24533-1:—1)
    - inclusion of information on a common reporting system allowing industry and government to communicate on freight data requirements and needs in an interoperable manner.

    **Abstract:** The seamless exchange of accurate, complete and timely data communication at transportation hand-offs has always been important for efficiency and accountability. Hand-offs with a universal method of exchange that allows data interoperability between all parties in the supply chain is critically important for maximizing efficiency and accountability. The efficient exchange of data also provides for security of transport information and for transfer of information related to security against terrorism as well as theft and traditional contraband. It is imperative for standards development organizations to address and facilitate the handling of these needs.

    ### Description

    ISO/TR 14813-2:2000, 7.4.1 identifies a commercial vehicle functional domain:

    - "These transactions maintain the TICS information about a shipment from the time of the order by the consignor to the reception of goods by the consignee. The key TICS transactions are to provide registers of service providers and to enable the goods to be tracked throughout intermodal journeys."

    ### Relationships to other standards

    - [TC204 Foundation Standards](../foundational.md)

## External References

The European Union- ITS Communications & Information Protocols ([EU-ICIP](https://www.mobilityits.eu)) is a significant resource of ITS standards, and its [Freight & Fleet page](https://www.mobilityits.eu/freight-fleet) is of particular relevance to this WG's work.

[How to get involved](../contact.md)
