# ontology_processor_owl.py
import os
import logging
import traceback
import re
from rdflib import Graph, RDF, OWL, URIRef, Literal, XSD, RDFS
from utils import get_qname, get_ontology_metadata, _norm_base, get_leaf_classes, collect_oneOf, collect_list
from rdflib.namespace import DC, DCTERMS

log = logging.getLogger("owl2mkdocs")

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
            if '#' in uri:
                base_uri, name = uri.rsplit('#', 1)
                base_uri += '#'
            elif '/' in uri:
                base_uri, name = uri.rsplit('/', 1)
                base_uri += '/'
            else:
                base_uri = ''
                name = uri
            if not base_uri.startswith('N') and not name.startswith('N'):
                f.write(f"| {base_uri} | {name} | {info['type']} | {info['description']} |\n")
    log.info(f"Updated concept_registry.md with {len(registry)} entries")

def process_ontology(owl_path: str, errors: list, ontology_info) -> tuple:
    """Process an OWL file and update ontology_info, return graph, namespace, prefix map, classes, local_classes, and property map."""
    # Load OWL ontology
    try:
        if not os.path.exists(owl_path):
            error_msg = f"Ontology file not found: {owl_path}"
            errors.append(error_msg)
            log.error(error_msg)
            return None, None, None, None, None, None

        with open(owl_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract xml:base
        base_match = re.search(r'xml:base\s*=\s*"([^"]+)"', content)
        xml_base = base_match.group(1) if base_match else None
        log.debug(f"Extracted xml_base: {xml_base}")

        # Replace invalid xml: prefixes with xmlns:
        content = content.replace(' xml:', ' xmlns:')

        # Remove leading colon in relative URIs for rdf:about and rdf:resource
        content = content.replace('rdf:about=":', 'rdf:about="')
        content = content.replace('rdf:resource=":', 'rdf:resource="')

        g = Graph()
        if owl_path.lower().endswith('.ttl'):
            g.parse(data=content, format='turtle', base=xml_base)
            log.info("Loaded ontology %s with Turtle format, %d triples", owl_path, len(g))
        else:
            try:
                g.parse(data=content, format='xml', base=xml_base)
                log.info("Loaded ontology %s with RDF/XML, %d triples", owl_path, len(g))
            except Exception as xml_e:
                try:
                    from owlready2 import get_ontology, default_world
                    onto = get_ontology("file://" + os.path.abspath(owl_path)).load()
                    if onto is None:
                        raise ValueError("owlready2 returned None")
                    g = default_world.as_rdflib_graph()
                    log.info("Loaded ontology %s with owlready2 fallback, %d triples", owl_path, len(g))
                except Exception as owl_e:
                    error_msg = f"Failed RDF/XML: {str(xml_e)}\n{traceback.format_exc()}\nFailed owlready2: {str(owl_e)}\n{traceback.format_exc()}"
                    errors.append(error_msg)
                    log.error(error_msg)
                    return None, None, None, None, None, None
        if len(g) == 0:
            error_msg = f"RDF graph is empty after loading ontology {owl_path}"
            errors.append(error_msg)
            log.error(error_msg)
            return None, None, None, None, None, None
    except Exception as e:
        error_msg = f"Failed to load or parse ontology from {owl_path}: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)
        return None, None, None, None, None, None

    # Extract and bind namespaces from content
    default_ns_match = re.search(r'xmlns\s*=\s*"([^"]+)"', content)
    if default_ns_match:
        default_ns = default_ns_match.group(1)
        g.bind('', URIRef(default_ns))
        log.debug(f"Bound default namespace: {default_ns}")
    ns_matches = re.findall(r'xmlns:(\w+)\s*=\s*"([^"]+)"', content)
    for prefix, uri in ns_matches:
        g.bind(prefix, URIRef(uri))
    log.debug(f"Bound additional namespaces: {ns_matches}")

    # Dynamically set default namespace from ontology IRI
    ns = None
    for s in g.subjects(RDF.type, OWL.Ontology):
        ns = str(s)
        break
    if not ns:
        log.warning("No ontology IRI found in OWL file %s; using default namespace", owl_path)
        ns = "https://isotc204.org/ontologies/its/default#"

    # Normalize unexpanded or relative URIs in the graph
    to_fix = []
    for s, p, o in g:
        new_s = s
        new_p = p
        new_o = o
        for term, new_term_setter in zip([s, p, o], [lambda x: globals().__setitem__('new_s', x), lambda x: globals().__setitem__('new_p', x), lambda x: globals().__setitem__('new_o', x)]):
            if isinstance(term, URIRef):
                t_str = str(term)
                if '://' not in t_str:
                    if ':' in t_str:
                        # Likely unexpanded QName
                        prefix, local = t_str.split(':', 1)
                        prefix_ns = None
                        for pr, u in g.namespaces():
                            if pr == prefix:
                                prefix_ns = str(u)
                                break
                        if prefix_ns:
                            new_term_setter(URIRef(prefix_ns + local))
                        else:
                            log.warning(f"Unresolved prefix '{prefix}' in URI '{t_str}'")
                            new_term_setter(URIRef(ns + t_str))
                    else:
                        # Relative URI without prefix
                        new_term_setter(URIRef(ns + t_str))
        if new_s != s or new_p != p or new_o != o:
            to_fix.append((s, p, o, new_s, new_p, new_o))
    for old_s, old_p, old_o, new_s, new_p, new_o in to_fix:
        g.remove((old_s, old_p, old_o))
        g.add((new_s, new_p, new_o))
    if to_fix:
        log.info(f"Normalized {len(to_fix)} triples with unexpanded or relative URIs in {owl_path}")

    # Additional fix for misexpanded QNames appended to base
    to_replace = {}
    for s, p, o in g:
        for term in (s, p, o):
            if isinstance(term, URIRef):
                t_str = str(term)
                if t_str.startswith(ns) and ':' in t_str[len(ns):] and '://' not in t_str[len(ns):]:
                    local_part = t_str[len(ns):]
                    if ':' in local_part:
                        prefix, local = local_part.split(':', 1)
                        prefix_ns = None
                        for pr, u in g.namespaces():
                            if pr == prefix:
                                prefix_ns = str(u)
                                break
                        if prefix_ns:
                            new_term = URIRef(prefix_ns + local)
                            to_replace[term] = new_term
    if to_replace:
        for old, new in to_replace.items():
            for subj, pred, obj in list(g):
                new_subj = new if subj == old else subj
                new_pred = new if pred == old else pred
                new_obj = new if obj == old else obj
                if (new_subj, new_pred, new_obj) != (subj, pred, obj):
                    g.remove((subj, pred, obj))
                    g.add((new_subj, new_pred, new_obj))
        log.info(f"Fixed {len(to_replace)} misexpanded URIs in {owl_path}")

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

    # Extract prefixes and create prefix map
    prefix_map = {str(uri): f"{prefix}:" for prefix, uri in g.namespaces()}
    if ns not in prefix_map:
        prefix_map[ns] = ":"
    # Add missing namespaces to prefix_map with generated prefixes
    for namespace in namespaces:
        if namespace not in prefix_map:
            ns_tail = namespace.rstrip('/#').split('/')[-1].split('#')[-1]
            prefix = ns_tail.lower()
            base_prefix = prefix
            count = 1
            while any(p.startswith(prefix + ':') for p in prefix_map.values()):
                prefix = f"{base_prefix}{count}"
                count += 1
            prefix_map[namespace] = f"{prefix}:"
            g.bind(prefix, URIRef(namespace))
            log.debug(f"Added inferred namespace: {namespace} → {prefix}:")

    # Add prefixes from registry
    for uri, info in registry.items():
        base_uri, name = uri.rsplit('/', 1) if '/' in uri else (uri, '')
        if '#' in name:
            base_uri, name = f"{base_uri}/{name.split('#')[0]}#", name.split('#')[1]
        if not base_uri.endswith(('#', '/')):
            base_uri += '/'
        if base_uri not in prefix_map:
            ns_tail = base_uri.rstrip('/#').split('/')[-1].split('#')[-1]
            prefix = ns_tail.lower()
            base_prefix = prefix
            count = 1
            while any(p.startswith(prefix + ':') for p in prefix_map.values()):
                prefix = f"{base_prefix}{count}"
                count += 1
            prefix_map[base_uri] = f"{prefix}:"
            g.bind(prefix, URIRef(base_uri))
            log.debug(f"Added registry namespace: {base_uri} → {prefix}:")

    log.debug("Prefixes for %s:", owl_path)
    for uri, prefix in prefix_map.items():
        log.debug("  %s → %s", prefix, uri)

    # Collect new concepts (local and external) from the current ontology
    new_concepts = {}
    # Classes (local and declared external)
    for cls in g.subjects(RDF.type, OWL.Class):
        uri = str(cls)
        log.debug(f"Examining class: {uri}")
        if uri not in registry and uri not in new_concepts:
            description = g.value(cls, RDFS.comment) or g.value(cls, DC.description) or ''
            new_concepts[uri] = {'type': 'class', 'description': str(description) if isinstance(description, Literal) else description}
            log.debug(f"Added class: {uri} (local={uri.startswith(ns)})")
    # Object properties
    for prop in g.subjects(RDF.type, OWL.ObjectProperty):
        uri = str(prop)
        if uri not in registry and uri not in new_concepts:
            description = g.value(prop, RDFS.comment) or g.value(prop, DC.description) or ''
            new_concepts[uri] = {'type': 'object_property', 'description': str(description) if isinstance(description, Literal) else description}
            log.debug(f"Added object_property: {uri} (local={uri.startswith(ns)})")
    # Datatype properties
    for prop in g.subjects(RDF.type, OWL.DatatypeProperty):
        uri = str(prop)
        if uri not in registry and uri not in new_concepts:
            description = g.value(prop, RDFS.comment) or g.value(prop, DC.description) or ''
            new_concepts[uri] = {'type': 'datatype_property', 'description': str(description) if isinstance(description, Literal) else description}
            log.debug(f"Added datatype_property: {uri} (local={uri.startswith(ns)})")

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
            if prop and isinstance(prop, URIRef) and not str(prop).startswith(ns):
                uri = str(prop)
                avf = g.value(o, OWL.allValuesFrom)
                svf = g.value(o, OWL.someValuesFrom)
                card = g.value(o, OWL.qualifiedCardinality) or g.value(o, OWL.minQualifiedCardinality) or g.value(o, OWL.maxQualifiedCardinality)
                if avf or svf:
                    target = avf or svf
                    prop_type = 'object_property'
                    # Infer classes from target expression
                    leaf_classes = get_leaf_classes(g, target, ns, prefix_map)
                    for leaf in leaf_classes:
                        if isinstance(leaf, URIRef) and not str(leaf).startswith(ns):
                            leaf_uri = str(leaf)
                            if leaf_uri not in registry and leaf_uri not in new_concepts:
                                new_concepts[leaf_uri] = {'type': 'class', 'description': ''}
                                log.debug(f"Inferred external class from restriction target: {leaf_uri}")
                    # Check if target is a oneOf enumeration
                    oneOf_members = collect_oneOf(g, target)
                    if oneOf_members:
                        # Generate enum class name
                        prop_local = get_qname(g, prop, ns, prefix_map).split(':')[-1]
                        enum_name = f"{prop_local[0].upper()}{prop_local[1:]}Enum"
                        enum_uri = ns + enum_name
                        if enum_uri not in registry and enum_uri not in new_concepts:
                            new_concepts[enum_uri] = {'type': 'class', 'description': 'Generated enumeration for property ' + get_qname(g, prop, ns, prefix_map)}
                            log.debug(f"Added generated enum class: {enum_uri}")
                        # Add individuals
                        for member in oneOf_members:
                            if isinstance(member, URIRef):
                                mem_uri = str(member)
                                if mem_uri not in registry and mem_uri not in new_concepts:
                                    new_concepts[mem_uri] = {'type': 'individual', 'description': ''}
                                    log.debug(f"Added enumeration individual: {mem_uri}")
                elif card:
                    on_class = g.value(o, OWL.onClass)
                    on_data_range = g.value(o, OWL.onDataRange)
                    if on_class:
                        prop_type = 'object_property'
                        # Infer classes from onClass
                        leaf_classes = get_leaf_classes(g, on_class, ns, prefix_map)
                        for leaf in leaf_classes:
                            if isinstance(leaf, URIRef) and not str(leaf).startswith(ns):
                                leaf_uri = str(leaf)
                                if leaf_uri not in registry and leaf_uri not in new_concepts:
                                    new_concepts[leaf_uri] = {'type': 'class', 'description': ''}
                                    log.debug(f"Inferred external class from restriction onClass: {leaf_uri}")
                    elif on_data_range:
                        prop_type = 'datatype_property'
                        # Infer datatypes if complex, but usually simple URIRef
                        if isinstance(on_data_range, URIRef) and not str(on_data_range).startswith(ns):
                            dt_uri = str(on_data_range)
                            if dt_uri not in registry and dt_uri not in new_concepts:
                                new_concepts[dt_uri] = {'type': 'datatype', 'description': ''}
                                log.debug(f"Inferred external datatype: {dt_uri}")
                    else:
                        prop_type = 'object_property'  # Default assumption
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
    log.debug("Found %d classes in ontology %s:", len(classes), owl_path)
    for cls in classes:
        log.debug("Class: %s", get_qname(g, cls, ns, prefix_map))

    # Filter classes by namespace
    local_classes = [cls for cls in classes if str(cls).startswith(ns)]
    log.debug("Filtered to %d local classes in namespace %s for %s:", len(local_classes), ns, owl_path)
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