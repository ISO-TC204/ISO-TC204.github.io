import os
import logging
import traceback
from rdflib import Graph, RDF, OWL, URIRef, RDFS, Literal
from funowl.converters.functional_converter import to_python
from utils import get_qname, get_ontology_metadata, _norm_base, get_prefix_named_pairs
from rdflib.namespace import DC, DCTERMS

log = logging.getLogger("ofn2mkdocs")

def parse_concept_registry(script_dir):
    registry_path = os.path.join(script_dir, "concept_registry.md")
    if not os.path.exists(registry_path):
        with open(registry_path, 'w', encoding='utf-8') as f:
            f.write("| base_uri | name | type | description |\n|----------|------|------|-------------|\n")
        log.info(f"Created new concept_registry.md in {script_dir}")
        return {}
    content = open(registry_path, 'r', encoding='utf-8').read()
    lines = content.splitlines()
    registry = {}
    in_table = False
    headers = None
    for line in lines:
        if line.strip().startswith('|'):
            if not in_table:
                headers = [h.strip().lower() for h in line.split('|') if h.strip()]
                log.debug(f"Parsed headers: {headers}")
                in_table = True
            elif headers and not line.strip().startswith('|---'):
                values = [v.strip() for v in line.split('|') if v.strip()]
                log.debug(f"Parsed values: {values}")
                if len(values) < 3:  # Require at least base_uri, name, type
                    log.warning(f"Skipping row with insufficient values (expected at least 3, got {len(values)}): {line}")
                    continue
                try:
                    base_uri = values[headers.index('base_uri')]
                    name = values[headers.index('name')]
                    concept_type = values[headers.index('type')]
                    description = values[headers.index('description')] if 'description' in headers and len(values) > headers.index('description') else ''
                    uri = f"{base_uri}{name}"
                    registry[uri] = {'type': concept_type, 'description': description}
                except ValueError as e:
                    log.warning(f"Skipping row due to missing header: {line} ({str(e)})")
    log.info(f"Loaded {len(registry)} entries from concept_registry.md")
    return registry

def update_concept_registry(script_dir, registry):
    registry_path = os.path.join(script_dir, "concept_registry.md")
    with open(registry_path, 'w', encoding='utf-8') as f:
        f.write("| base_uri | name | type | description |\n|----------|------|------|-------------|\n")
        # Sort by base_uri and then name
        sorted_items = sorted(registry.items(), key=lambda x: (x[0].rsplit('/', 1)[0] if '/' in x[0] else x[0], x[0].rsplit('/', 1)[1] if '/' in x[0] else ''))
        for uri, info in sorted_items:
            base_uri, name = uri.rsplit('/', 1) if '/' in uri else (uri, '')
            if '#' in name:
                base_uri, name = f"{base_uri}/{name.split('#')[0]}#", name.split('#')[1]
            if not base_uri.endswith(('#', '/')):
                base_uri += '/'
            if not base_uri.startswith('N'):
                f.write(f"| {base_uri} | {name} | {info['type']} | {info['description']} |\n")
    log.info(f"Updated concept_registry.md with {len(registry)} entries")

def process_ontology(ofn_path: str, errors: list, ontology_info) -> tuple:
    """Process an OFN file, update ontology_info, and return graph, namespace, prefix map, classes, local classes, and property map."""
    # Check file extension
    if not ofn_path.lower().endswith('.ofn'):
        error_msg = f"Invalid file extension for {ofn_path}. Expected .ofn, skipping."
        errors.append(error_msg)
        log.error(error_msg)
        return None, None, None, None, None, None

    # Load OFN ontology using funowl
    try:
        doc = to_python(ofn_path)
        if not doc:
            raise ValueError("Failed to parse OWL functional syntax document")
        
        # Get default namespace from document
        ns = None
        if hasattr(doc, 'ontology') and doc.ontology and doc.ontology.iri:
            ns = str(doc.ontology.iri)
        if not ns:
            log.warning("No ontology IRI found in OFN file %s; using default namespace", ofn_path)
            ns = "https://isotc204.org/ontologies/its/regulation#"
        log.info("Using namespace %s", ns)

        # Get prefix map from funowl document
        prefix_pairs = get_prefix_named_pairs(doc, ns)
        prefix_map = {item['uri']: f"{item['prefix']}:" if item['prefix'] else ':' for item in prefix_pairs}
        log.debug("Prefixes from funowl for %s:", ofn_path)
        for item in prefix_pairs:
            log.debug("  %s → %s", item['prefix'], item['uri'])

        # Convert to rdflib Graph
        g = Graph()
        doc.to_rdf(g)
        log.info("Converted to RDF graph with %d triples", len(g))

        # Bind prefixes to graph for serialization and queries
        for item in prefix_pairs:
            prefix = item['prefix'].rstrip(':') if item['prefix'] else ''
            uri = URIRef(item['uri'])
            g.bind(prefix, uri)

    except Exception as e:
        error_msg = f"Failed to load or parse ontology from {ofn_path}: {str(e)}\n{traceback.format_exc()}\nEnsure the 'funowl' library is installed (`pip install funowl`) and the .ofn file is valid."
        errors.append(error_msg)
        log.error(error_msg)
        return None, None, None, None, None, None

    # Load the concept registry from the Python script directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    registry = parse_concept_registry(script_dir)

    # Add object and datatype properties from registry to the graph
    for uri, info in registry.items():
        if info['type'] == 'object_property':
            g.add((URIRef(uri), RDF.type, OWL.ObjectProperty))
            log.debug(f"Added to graph: {uri} a owl:ObjectProperty")
        elif info['type'] == 'datatype_property':
            g.add((URIRef(uri), RDF.type, OWL.DatatypeProperty))
            log.debug(f"Added to graph: {uri} a owl:DatatypeProperty")

    # Collect additional namespaces from the RDF graph
    namespaces = set()
    for s, p, o in g:
        for term in (s, p, o):
            if isinstance(term, URIRef):
                # Extract namespace by removing the last component (after last '/' or '#')
                uri = str(term)
                ns_end = max(uri.rfind('/'), uri.rfind('#'))
                if ns_end != -1 and uri.startswith('http'):
                    namespace = uri[:ns_end + 1]
                    namespaces.add(namespace)

    # Add missing namespaces to prefix_map with generated prefixes
    for namespace in namespaces:
        if namespace not in prefix_map:
            # Generate a prefix based on the last part of the namespace
            ns_tail = namespace.rstrip('/#').split('/')[-1].split('#')[-1]
            prefix = ns_tail.lower()
            # Ensure uniqueness by appending a number if prefix exists
            base_prefix = prefix
            count = 1
            while any(p.startswith(prefix + ':') for p in prefix_map.values()):
                prefix = f"{base_prefix}{count}"
                count += 1
            prefix_map[namespace] = f"{prefix}:"
            g.bind(prefix, URIRef(namespace))
            log.debug(f"Added inferred namespace: {namespace} → {prefix}:")

    # Update prefix map with registry namespaces
    for uri, info in registry.items():
        base_uri, name = uri.rsplit('/', 1) if '/' in uri else (uri, '')
        if '#' in name:
            base_uri, name = f"{base_uri}/{name.split('#')[0]}#", name.split('#')[1]
        if not base_uri.endswith(('#', '/')):
            base_uri += '/'
        if base_uri not in prefix_map:
            prefix = name.lower()
            # Ensure uniqueness
            base_prefix = prefix
            count = 1
            while any(p.startswith(prefix + ':') for p in prefix_map.values()):
                prefix = f"{base_prefix}{count}"
                count += 1
            prefix_map[base_uri] = f"{prefix}:"
            g.bind(prefix, URIRef(base_uri))
            log.debug(f"Added registry namespace: {base_uri} → {prefix}:")

    log.debug("Final prefixes for %s:", ofn_path)
    for uri, prefix in prefix_map.items():
        log.debug("  %s → %s", prefix, uri)

    # Collect new concepts (local and external) from the current ontology
    new_concepts = {}
    # Local classes
    for cls in g.subjects(RDF.type, OWL.Class):
        uri = str(cls)
        if uri.startswith(ns) and uri not in registry and uri not in new_concepts:
            description = g.value(cls, RDFS.comment) or g.value(cls, DC.description) or ''
            new_concepts[uri] = {'type': 'class', 'description': str(description) if isinstance(description, Literal) else description}
            log.debug(f"Added local class: {uri}")
    # Local object properties
    for prop in g.subjects(RDF.type, OWL.ObjectProperty):
        uri = str(prop)
        if uri.startswith(ns) and uri not in registry and uri not in new_concepts:
            description = g.value(prop, RDFS.comment) or g.value(prop, DC.description) or ''
            new_concepts[uri] = {'type': 'object_property', 'description': str(description) if isinstance(description, Literal) else description}
            log.debug(f"Added local object_property: {uri}")
    # Local datatype properties
    for prop in g.subjects(RDF.type, OWL.DatatypeProperty):
        uri = str(prop)
        if uri.startswith(ns) and uri not in registry and uri not in new_concepts:
            description = g.value(prop, RDFS.comment) or g.value(prop, DC.description) or ''
            new_concepts[uri] = {'type': 'datatype_property', 'description': str(description) if isinstance(description, Literal) else description}
            log.debug(f"Added local datatype_property: {uri}")

    # Inferred external concepts from usage
    for s, p, o in g.triples((None, RDFS.subClassOf, None)):
        if isinstance(o, URIRef) and not str(o).startswith(ns) and str(o) != str(OWL.Thing):
            uri = str(o)
            if uri not in registry and uri not in new_concepts:
                new_concepts[uri] = {'type': 'class', 'description': ''}
                log.debug(f"Inferred external class: {uri}")
    for s, p, o in g.triples((None, RDFS.subClassOf, None)):
        if (o, RDF.type, OWL.Restriction) in g:
            prop = g.value(o, OWL.onProperty)
            if prop and not str(prop).startswith(ns):
                uri = str(prop)
                avf = g.value(o, OWL.allValuesFrom)
                card = g.value(o, OWL.qualifiedCardinality) or g.value(o, OWL.minQualifiedCardinality) or g.value(o, OWL.maxQualifiedCardinality)
                if avf and isinstance(avf, URIRef):
                    prop_type = 'object_property'
                elif card or g.value(o, OWL.onDataRange):
                    prop_type = 'datatype_property'
                else:
                    prop_type = 'object_property'  # Default assumption
                if uri not in registry and uri not in new_concepts:
                    new_concepts[uri] = {'type': prop_type, 'description': ''}
                    log.debug(f"Inferred external {prop_type}: {uri}")

    # Update registry with new concepts only if not present
    for uri, info in new_concepts.items():
        if uri not in registry:
            registry[uri] = info
    update_concept_registry(script_dir, registry)

    # Extract ontology metadata and update ontology_info
    dc_title = get_ontology_metadata(g, ns, DC.title) or "Untitled Ontology"
    dc_description = get_ontology_metadata(g, ns, DC.description) or ""
    ontology_info["title"] = dc_title
    ontology_info["description"] = dc_description
    ontology_info["patterns"] = set()
    ontology_info["non_pattern_classes"] = set()

    # Extract classes (include external from registry)
    classes = set(g.subjects(RDF.type, OWL.Class)) - {OWL.Thing}
    for uri, info in registry.items():
        if info['type'] == 'class' and str(uri).startswith('http'):
            classes.add(URIRef(uri))
    classes = {cls for cls in classes if str(cls).startswith("http")}
    log.info("Found %d classes in ontology %s:", len(classes), ofn_path)
    for cls in classes:
        log.debug("  %s", str(cls))

    # Filter classes by namespace
    local_classes = [cls for cls in classes if str(cls).startswith(ns)]
    log.info("Filtered to %d local classes", len(local_classes))
    for cls in local_classes:
        log.debug("  %s", get_qname(g, cls, ns, prefix_map))

    # Create property map: qname to URI
    prop_map = {}
    for p in g.subjects(RDF.type, OWL.ObjectProperty):
        qn = get_qname(g, p, ns, prefix_map)
        prop_map[qn] = p
    for p in g.subjects(RDF.type, OWL.DatatypeProperty):
        qn = get_qname(g, p, ns, prefix_map)
        prop_map[qn] = p
    # Add external properties from registry
    for uri, info in registry.items():
        if info['type'] in ('object_property', 'datatype_property'):
            qn = get_qname(g, URIRef(uri), ns, prefix_map)
            prop_map[qn] = URIRef(uri)
            log.debug(f"Added external {info['type']}: {qn}")

    return g, ns, prefix_map, classes, local_classes, prop_map