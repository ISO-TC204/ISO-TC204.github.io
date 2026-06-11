---
published: 2024
pages: 73
title: "ISO 14823-1 - Extract"
standard: "ISO 14823-1"
name: "Intelligent transport systems – Graphic Data Dictionary – Part 1: Specification"
name_1: "Intelligent transport systems"
name_2: "Graphic Data Dictionary"
name_3: "Part 1: Specification"
annotation: "This Extract does not replace the technical standard itself; it is only informative material about the standard."
note: "Note: This Extract presents selected chapters of the described document and retains the original chapter numbering."
---

## Introduction

The standard ISO 14823-1:2024 defines the **Graphic Data Dictionary (GDD)** – a unified, language-independent system for encoding traffic signs and pictograms for the needs of Intelligent Transport Systems (ITS). Its purpose is to enable **efficient transmission, interpretation, and display of traffic information** across different countries, systems, and technologies. This dictionary is used for information exchange between centres (DATEX II) and between infrastructure and vehicles (cooperative systems, C-ITS) for describing traffic signs displayed, for example, on variable message signs.

This revision of the standard is a fundamental rework of the original ISO 14823:2017. The original standard, due to its use of a simple identifier based on ISO 3166-1 and a five-digit structure (service category – nature – sequence number), had two essential limitations: there was **no globally unique identification of pictograms, and adding new pictograms was inflexible** because the numeric space was rigidly structured and difficult to extend.

This revision therefore introduces a more robust mechanism based on the **relative object identifier (OID)**, which enables global identification, hierarchy, and extensibility without breaking compatibility. The revision contains following essential technical and conceptual changes:

- an updated **version 2** of the GDD based on OID and relative object identifiers, enabling global identification, hierarchical generalisation and adding new codes without collisions,

- support for more complex messages thanks to the possibility of including up to **four pictograms** in a single object,

- addition of new codes and removal of redundant ones, adjustment of attributes for better compatibility with other ITS standards,

- marking codes as **“current”** or **“deprecated”** for controlled evolution,

- preservation of full backward compatibility with ISO 14823:2017.

This Extract describes Part 1 of the GDD standard (hereinafter “the described document”) with the specification of the format and the tables of pictograms of individual signs.

*Note: This Extract presents selected chapters of the described document and retains the original chapter numbering.*

## Use

The described document defines the encoding of various traffic signs and serves as the technical foundation for systems that need to uniquely identify and process traffic pictograms in digital form. It provides a unified and extensible framework that enables consistent handling of traffic pictograms regardless of national differences or the communication technology used.

The standard is intended especially for **developers and architects of ITS systems** who implement support for digital traffic signs in C-ITS, V2X communication or navigation services, **vehicle manufacturers and their suppliers** who integrate pictograms into onboard systems, ADAS and in-vehicle signage, **infrastructure operators and traffic centres** that publish traffic information through VMS, C-ITS or DATEX II**, providers of traffic and navigation services** who need interoperable encoding across countries and systems and, **manufacturers of end-user devices** and applications that display traffic information to users.

## Related Documents (Selection)

The described document lists six normative references to the following standards ISO 3166-1 (Country codes), ISO 8601-1 (Date and time representation), ISO 8824-1 (ASN.1 notation), ISO/IEC 8825-5 (Mapping XML schemas to ASN.1), ISO/IEC 8859-1 (Two-letter country codes) and, ISO/IEC 19505-1 (UML modelling).

The text also mentions the previous edition ISO 14823:2017, with which this version is backward compatible.

## Scope

The document defines the structure of the **GDD** and the rules for encoding pictograms as a unified mechanism for encoding, transmitting, and interpreting graphical elements (traffic signs) within ITS. It does not address the method of their graphical rendering nor the formats of transmission protocols. The standard is intended for use in ITS applications that need to uniquely identify and share the meaning of traffic signs in digital form.

## 3 Terms and definitions

This clause defines the basic concepts used within the Graphic Data Dictionary (GDD). It contains a total of 12 terms describing the structure of codes, their meaning and related concepts. The key ones include:

**graphic data dictionary** – a systematically organised catalogue of pictogram codes used in ITS,

**pictogram** – a graphic symbol or icon displayed on a static traffic sign or on an IT system display (e.g. VMS), providing travellers with information about traffic conditions, restrictions, or public facilities

**pictogram code** – a combination of a service category code and a pictogram category code, optionally supplemented by a country code (in version 1)

**relative object identifier** – an identifier that determines an object by its position within the OID tree relative to a defined root

**attribute** – additional coded information that clarifies the meaning of the pictogram (e.g. direction, distance, time)

**specialization** – a relationship between a general class and its more specific variant that adds additional semantic elements

## 4 Abbreviations

The clause lists 10 abbreviations used in the document. For the purposes of this Extract, the following are the most important:

**ASN.1** Abstract Syntax Notation One, the formal language used to define the structure and encoding of the GDD

**GDD** Graphic Data Dictionary, the dictionary defined by this standard

**OID** Object Identifier, the identifier used in version 2 for unique identification of pictograms

**VMS** Variable Message Sign, variable traffic signage capable of displaying pictograms defined in the GDD

Other terms and abbreviations from the ITS domain can be found in the *ITS Terminology* dictionary ([www.itsterminology.org](http://www.itsterminology.org)), the *StandardLand* website ([www.standardland.cz](http://www.standardland.cz)) or the *OBP platform* ([www.iso.org/obp](http://www.iso.org/obp)).

## 5 Conformance

This clause, in four lines, defines two basic conditions for conformance. The implementation must use the GDD structure defined in the standard, and it must select pictogram codes exclusively from the tables provided in the document.

## 6 Requirements

This clause, one page long, lists ten basic functional requirements for the use of the GDD in ITS, with references to parts of the standard. Among the requirements are, for example: graphic data must contain a version and an identifier (OID or country code), the selection of the pictogram code must correspond to the appropriate table according to the type of sign (warning, regulatory, informational, public facilities, supplementary panels, etc.).

## 7 Structure of the pictogram code

This clause, four pages in length, defines **two parallel mechanisms for pictograms identification**, their hierarchy, and the rules for extension, including the marking of obsolete codes.

Clause **7.1 General** explains the existence of two versions of the GDD. **Version 1** (country code + pictogram code) and **Version 2** (relative OID). Both versions are supported in parallel for backward compatibility.

Clause **7.2 Current and deprecated signs** define the lifecycle of pictogram codes. All codes must be marked as **current** or **deprecated**.

Clause **7.3 Relative object identifier (relative OID)** describes the OID hierarchy registered under `{joint-iso-itut(2) its(28) gdd(5)}` and the way pictograms can be generalized according to the required level of detail. It provides examples showing how an application may generalize a relative OID to distinct levels depending on the needed detail (warning sign: specific animal → general animal → general warning).

Clause **7.4 Country code** states that the country code used is the two-letter code according to **ISO 3166-1** (version 1).

Clause **7.5 Pictogram code and OID** contains **Table 1**, which defines the structure and numbering of pictograms for version 1 in the form **“service category → subcategory → nature → sequence number”** (e.g. `trafficSign (1) + regulatory (2) + mandatory (7) + xx `⇒` {1 2 7 xx}`).

## 8 Numbering of pictogram codes

The clause, spanning 40 pages, defines the numerical ranges and mnemonics for all pictogram categories and provides the complete list of codes used in the GDD. It consists primarily of extensive code tables.

Clause **8.1 General** states that each pictogram is assigned a code and a mnemonic name. The codes are divided according to the type of sign.

Clause **8.2 Mnemonics of the codes** describes the rules for forming names in lowerCamelCase, without spaces and without articles. One illustrative example is provided.

**Table 1 (excerpt from Table 2 of the standard) Assigning a service category code and pictogram category code to a specific phrase (mnemonic):**

<table>
  <tr>
    <th>Pictogram code</th>
    <th></th>
    <th>Pictogram name</th>
    <th>Mnemonic</th>
  </tr>
  <tr>
    <td>Service category code</td>
    <td>Pictogram category code</td>
    <td rowspan="2">Intersection where priority is prescribed by the general priority rule (crossroads)</td>
    <td rowspan="2">intersectionWherePriorityIsPrescribed GeneralByPriorityRuleCrossroads</td>
  </tr>
  <tr>
    <td>11</td>
    <td>111</td>
  </tr>
</table>

The following clauses (8.3–8.9) contain the definitions of codes presented through an extensive table in which each pictogram code is assigned a name and a mnemonic. The codes in the tables are grouped into sets, and the sizes of these sets range from tens to hundreds of pictogram codes, with gaps between the sets reserved for future use.

Clause **8.3 Warning traffic signs** (pictogram codes 11111–11999, approximately 9 pages of tables) includes pictograms used to provide **advance warning** to drivers about dangerous or deteriorated road conditions. These include warnings about obstacles, hazardous sections, animals, weather phenomena, or other situations requiring increased attention.

Clause **8.4 Regulatory traffic signs** (pictogram codes 12111–12999, approximately 10 pages of tables) contains pictograms expressing **obligations, prohibitions, and restrictions**. The standard divides them into three groups:

- signs regulating priority (12111–12399),

- prohibitions and restrictions (12411–12699),

- mandatory signs (12711–12999).

Clause **8.5 Guidance traffic signs** (pictogram codes 13111–13999, approximately 11 pages of tables) includes pictograms providing navigational, directional, and general informational content. The standard divides them into six subgroups:

- advance directional information (13111–13399),

- instructions (13411–13499),

- notifications (13511–13599),

- lane guidance (13611–13699),

- warnings (13711–13799),

- identification of places and roads (13811–13999).

Clause **8.6 Public facilities** (pictogram codes 21111–21999, approximately 3 pages of tables) contains pictograms indicating public services and facilities such as parking areas, fuel stations, restaurants, hospitals, toilets, etc.

Clause **8.7 Ambient conditions** (pictogram codes 31111–31999, approximately 2 pages of tables) includes pictograms indicating weather and other environmental conditions that may affect traffic (e.g. rain, fog, wind, snow).

Clause **8.8 Road conditions** (pictogram codes 32111–32999, approximately 1 page of tables) contains pictograms informing about road surface conditions and events along the route (e.g. accidents, congestion, closures, slippery road).

## Annex A – ASN.1 description of GDD (version 2)

This annex contains a one-paragraph reference to the complete formal definition of GDD version 2 in ASN.1, maintained at: [https://standards.iso.org/iso/14823/-1/ed-1/en/](https://standards.iso.org/iso/14823/-1/ed-1/en/)

## Annex B – Attributes of GDD (version 2)

This annex, approximately 10 pages long, contains the definition of attributes applicable to pictograms in version 2, including their types, ranges, and meanings. It also includes tables of values (e.g. directions, distances, time information). It serves as a reference catalogue for interpreting supplementary information.

## Annex C – UML diagram of GDD (version 2)

This annex, approximately 3 pages long, contains four UML diagrams of the GDD version 2 structures. The diagrams illustrate relationships between pictograms, attributes, specializations and OIDs.

## Annex D – Specializations (version 2)

This annex, approximately 2 pages long, describes the mechanism of specializations — the method for creating derived pictograms or regional variants without disrupting the basic GDD structure. It provides rules for extending the OID tree.

## Annex E – ASN.1 description of GDD (version 1)

This annex contains a one-paragraph reference to the original ASN.1 definition of GDD from ISO 14823:2017. It serves for backward compatibility and support of older implementations using country-code-based identifiers.

## Annex F – Attributes of GDD (version 1)

This annex, approximately 6 pages long, lists the attributes used in version 1. The structure is simpler than in version 2 and corresponds to the original 2017 model. It includes tables of values for directions, distances, and other supplementary information.

## Annex G – UML diagram of GDD (version 1)

This annex, one page long, contains a single UML model of the original GDD version 1. It serves as visual documentation of the older model.

## Annex H – List of directions at diverging point

This annex, approximately 5 pages long, contains one extensive table of numerical values for directional information used with pictograms, especially in the context of diverging lanes or branching roads. These values are used as attributes.

## Annex I – Example GDD dataset for the U.N. and selected countries

This annex, half a page long, refers to a URL with illustrative examples of pictogram codes for the U.N. and some countries. It serves as a demonstration of how national variants can be incorporated into the GDD.

## Annex J – Mapping OID to pictogram code (version 1)

This annex, approximately 2 pages long, provides an informative overview of the relationships between version 1 pictogram codes and their corresponding nodes in the OID tree. It explains how the original numeric codes (version 1) can be mapped to the OID structure used in version 2, enabling comparison or conversion between the two versions. The annex serves as a tool for interoperability and understanding the relationship between the historical coding and the new OID-based model.

## Bibliography

The bibliography, half a page long, contains non-normative references to documents related to GDD, ASN.1 and the ITS domain. These sources provide supplementary information for implementation or deeper understanding of the context of the standard but are not mandatory for conformance.
