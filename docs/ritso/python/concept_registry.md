![Draft for review only](../../assets/img/draft_for_review.svg)

# Concept Registry

This page lists all known concepts (classes and properties) included in the RITSO.

| base_uri | name | type | description |
|----------|------|------|-------------|
| agent/ |  | class | Person (3.1.1.6) or organization (3.1.1.7) that is capable of performing actions |
| biologicalEntity/ |  | class | material entity (3.1.1.3) that was or is a living organism |
| entity/ |  | class | concrete or abstract thing that exists, did exist, or can possibly exist, including associations among these things |
| http://www.w3.org/2001/XMLSchema# | string | class |  |
| https://w3id.org/citydata/part1/ | hasDescription | object_property |  |
| https://w3id.org/citydata/part1/ | hasIdentifier | object_property |  |
| https://w3id.org/citydata/part1/ | hasName | object_property |  |
| https://w3id.org/itsdata/core/ | ITSClass | class | A class to organize all classes defined in all recognized ITS Ontologies. |
| https://w3id.org/itsdata/core/ | ITSDatatypeProperty | datatype_property | A datatype property to organize all datatype properties defined in all recognized ITS Ontologies. |
| https://w3id.org/itsdata/core/ | ITSObjectProperty | object_property | An object property to organize all object properties defined in all recognized ITS Ontologies. |
| https://w3id.org/itsdata/core/ | ITSPattern | class |  |
| https://w3id.org/itsdata/core/ | ITSThing | class |  |
| https://w3id.org/itsdata/core/ | version | datatype_property | The version of the object. |
| https://w3id.org/itsdata/regulation/ | LegalBasis | class | A legal basis provides references to the legal documents that authorize an entity to issue the types of regulations covered by a traffic regulation order. |
| https://w3id.org/itsdata/regulation/ | RegulationObjectProperty | object_property | An object property to organize all object properties defined in the Traffic Regulation Ontology. |
| https://w3id.org/itsdata/regulation/ | RuleMaker | class | An entity that has the responsibility for creating and maintaining rules of the road or regulations for a geographic and operational scope as defined by the parent jurisdictional entity. |
| https://w3id.org/itsdata/regulation/ | TrafficRegulation | class | A traffic regulation is a rule having the force of law that is established by a regulator through a traffic regulation order. |
| https://w3id.org/itsdata/regulation/ | TrafficRegulationOrder | class | A legally recognised document or publication issued to enact a specific traffic regulation or regulations by a competent authority. |
| https://w3id.org/itsdata/regulation/ | TroDataProperty | datatype_property | - |
| https://w3id.org/itsdata/regulation/ | TroPattern | class | - |
| https://w3id.org/itsdata/regulation/ | TroThing | class | - |
| https://w3id.org/itsdata/regulation/ | externalReferences | object_property | - |
| https://w3id.org/itsdata/regulation/ | implementedLocation | object_property | - |
| https://w3id.org/itsdata/regulation/ | implementedValidity | object_property | - |
| https://w3id.org/itsdata/regulation/ | index | datatype_property | - |
| https://w3id.org/itsdata/regulation/ | issuingAuthority | object_property | The entity that issued the instance of the traffic regulation order |
| https://w3id.org/itsdata/regulation/ | legalBasis | object_property | formal authority within the law (e.g., statute, ordinance, administrative rule, constitutional provision) that empowers an entity to create, adopt, or enforce a regulation |
| https://w3id.org/itsdata/regulation/ | predefinedItineraryReference | datatype_property | - |
| https://w3id.org/itsdata/regulation/ | predefinedLocationGroupReference | datatype_property | - |
| https://w3id.org/itsdata/regulation/ | reasonCode | object_property | A reason justifying the existence of the instance of the traffic regulation order |
| https://w3id.org/itsdata/regulation/ | status | object_property | The current lifecycle status of the instance of the containing class |
| https://w3id.org/itsdata/regulation/ | trafficRegulation | object_property | - |
| https://w3id.org/itsdata/regulation/ | validityByOrder | object_property | - |
| https://w3id.org/itsdata/regulation/ | validityTimeSpecification | object_property | - |
| https://w3id.org/itsdata/time/ | approvalDate | datatype_property | The date on which the object was approved. |
| immaterialEntity/ |  | class | entity (3.1.1.1) that does not occupy three-dimensional space |
| materialEntity/ |  | class | entity (3.1.1.1) that occupies three-dimensional space |
| nonBiologicalEntity/ |  | class | material entity (3.1.1.3) that is not and has never been a living organism |
| organization/ |  | class | immaterial entity (3.1.1.2) that is a structured group of one or more agents |
| person/ |  | class | biological entity (3.1.1.5) that is a human being |
