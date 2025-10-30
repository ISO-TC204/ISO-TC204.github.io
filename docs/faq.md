<!-- faqs.md -->

# FAQ's

**1. I’ve got a query / concern / feedback about a document. How do I get in touch with the author?**
>**Answer:** You can simply contact the
[ISO TC204 Secretariat](https://www.iso.org/en/contents/data/committee/05/47/54706.html#secretariat) with the document number and they will connect you with the respective WG convenor. To minimize your wait time, please advise the Secretariat with  your sufficient detail of your issue to assist the WG Convenor provide you an informed  initial response.

**2. What’s meant by ITS Architecture?**
>**Answer:** An ITS architecture represents the fundamental concepts and properties of an intelligent transport system within a defined environment with its embodied components, relationships, and principles of design and evolution. Technically, each system has an own architecture, whether documented or not. Documentation describing an architecture is often called an "architecture", although the more precise term for the documentation is "architecture description". Standardization promotes the concept of adopting similar architecture designs across multiple systems. A generalized description that describes the architecture used by multiple systems is also often referred to as an "architecture" although the more precise term is a "reference architecture".

**4. What’s an ITS Station?**
>**Answer:** An ITS station is a component within an intelligent transport system that performs ITS-related application processing and meets key security requirements to be considered part of the ITS trust domain.

**5. Is there a consolidated list of terms and their definitions?**
>**Answer:** ISO/TC 204 has developed [ISO/TS 14812 Intelligent transport systems — Vocabulary](https://www.iso.org/standard/79779.html). This collates definitions from a wide range of sources across ISO and other external entities. These definitions can be found online for free on the [Online Browsing Platform](https://www.iso.org/obp/ui#iso:std:iso:ts:14812:ed-2:v1:en).

**6. What’s an Object Identifier (OID)?  Is there a consolidated list?**
>**Answer:** An object identifier is a decentralized, globally unique identifier that can be assigned to identify any type of object (e.g., an information item in a message, a document, an encoding scheme). The assignment of identifiers to a meaning is decentralized; this is achieved by the assignment of three root nodes managed by ISO, ITU-T, and a third managed jointly by ISO and ITU-T, each of which is assigned a number and a name. Nodes under the three root nodes are assigned by those organizations and the management of each such node can be assigned to a different entity. Each level of the object identifier tree, except for the root and second level, can have an infinite number of nodes and there can be an infinite number of levels. As a result, any entity can request a new node and then assign their own identifiers to their own objects underneath that node. Within TC 204, we are in the process of establishing our own registry for identifier nodes.

**7. What’s an Application Identifier (ITS-AID)?  Is there a consolidated list?**
>**Answer:** An ITS Application Identifier (ITS-AID) is an identifier given to an ITS application so that its messages can be recognized in electronic communications. The identifiers are managed within the [Registry for ITS Identifiers (RITSI)](https://iso-tc204.github.io/iso5345/its-aid.html).

**8. What’s the difference between an AID and OID?**
>**Answer:** An ITS-AID is used specifically to identify an ITS application in electronic communications. An OID can be used identify any object (including an ITS application, if desired) for any purpose (for which an OID can be recognized).

**9.What’s ASN.1 and why should I care?**
>**Answer:** Abstract Syntax Notation One (ASN.1) is a standard for defining data structures in a precise manner without having to detail the detailed encoding. ASN.1 includes its own set of encoding rules for different styles (e.g., basic, octet-aligned, packed, XML, JSON). The advantage of ASN.1 is that it provides a precise and unambiguous definition of a data structure that can be easily validated and compiled into code resulting in more interoperable implementations.
