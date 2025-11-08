# utils.py
import re
import logging
import traceback
from typing import Optional, Iterable, Tuple, List
from rdflib import Graph, RDF, RDFS, OWL, URIRef, Literal, BNode
from rdflib.namespace import DC, DCTERMS, SKOS

log = logging.getLogger("ofn2mkdocs")

# -------------------- namespaces --------------------
DESC_PROPS = (DC.description, SKOS.definition, RDFS.comment, DCTERMS.description)
SKIP_IN_OTHER = set(DESC_PROPS) | {RDFS.label, DCTERMS.description, SKOS.note, SKOS.example}

def _norm_base(u: str) -> str:
    return u.rstrip('/#')

def get_prefix_named_pairs(ontology_doc, ns: str):
    """Return [{'prefix': <str>, 'uri': <str>}, ...] from funowl PrefixDeclarations,
    handling different return shapes of as_prefixes() across funowl versions."""
    pd = getattr(ontology_doc, "prefixDeclarations", None)
    if not pd:
#        log.debug("No prefix declarations found, using default namespace: %s", ns)
        return [{"prefix": "", "uri": ns}]

    ap = pd.as_prefixes()
    out = []

    if hasattr(ap, "items"):
        out = [{"prefix": str(k), "uri": str(v)} for k, v in ap.items()]
    else:
        for item in ap:
            if isinstance(item, tuple) and len(item) == 2:
                k, v = item
                out.append({"prefix": str(k), "uri": str(v)})
#                log.debug("      %s %s", k, v)
                continue

            p = (
                getattr(item, "prefixName", None)
                or getattr(item, "prefix", None)
                or getattr(item, "name", None)
            )
            iri = (
                getattr(item, "fullIRI", None)
                or getattr(item, "iri", None)
                or getattr(item, "iriRef", None)
            )
            if p is not None and iri is not None:
                out.append({"prefix": str(p), "uri": str(iri)})

    if not any(d["uri"] == ns for d in out):
        out.append({"prefix": "", "uri": ns})

#    log.debug("Prefixes extracted: %s", out)
    return out

def get_qname(g: Graph, uri, ns: str, prefix_map: dict):
    if uri is None or not str(uri).strip():
        log.error("Invalid URI provided to get_qname: %s", uri)
        return "INVALID_URI"
    s = str(uri)
    norm = _norm_base(s)
#    log.debug("Processing URI: %s, normalized: %s, namespace: %s", s, norm, ns)
    if norm == _norm_base(ns) or s.startswith(ns):
        local = s[len(_norm_base(ns)):]
        if local.startswith(('/', '#', '_')):
            local = local[1:]
        qname = local.rstrip()
#        log.debug("Matched default namespace, returning QName: %s", qname)
        return qname
    if not prefix_map:
        log.warning("Empty prefix map for URI: %s, namespace: %s", s, ns)
        return s
    for base in sorted(prefix_map.keys(), key=len, reverse=True):
        base_norm = _norm_base(base)
#        log.debug("Checking prefix base: %s, normalized: %s", base, base_norm)
        if s == base or s.startswith(base) or norm == base_norm or norm.startswith(base_norm):
            local = s[len(base):]
            if local.startswith(('/', '#', '_')):
                local = local[1:]
            local = local.rstrip()
            if not local:
#                log.debug("No local part after prefix %s, using base URI", base)
                local = s
            if prefix_map[base] == ":":
                qname = local
            else:
                qname = prefix_map[base] + ":" + local
            return qname
    if not s.startswith('N'):
        log.warning("No prefix found for URI: %s, namespace: %s, prefix_map:", s, ns)
        for prefix in prefix_map:
            log.info("  %s, %s", str(prefix), prefix == ns)
    return s

def get_label(g: Graph, c: URIRef) -> str:
    if c is None:
        log.error("Invalid class URI provided to get_label: None")
        return "INVALID_CLASS"
    for _, _, lbl in g.triples((c, RDFS.label, None)):
        if isinstance(lbl, Literal):
            return str(lbl)
    return str(c).split('#')[-1]

def get_first_literal(g: Graph, subj: URIRef, preds: Iterable[URIRef]) -> Optional[str]:
    if subj is None:
        log.error("Invalid subject URI provided to get_first_literal: None")
        return None
    for p in preds:
        for _, _, lit in g.triples((subj, p, None)):
            if isinstance(lit, Literal):
                return str(lit)
    return None

def get_ontology_metadata(g: Graph, ns: str, predicate: URIRef) -> Optional[str]:
    """Extract metadata (e.g., dc:title, dcterms:description) from any subject in the graph."""
    for subj in g.subjects(predicate=predicate):
        for _, _, lit in g.triples((subj, predicate, None)):
            if isinstance(lit, Literal):
                return str(lit)
    ontology_iri = URIRef(ns.rstrip('#/'))
    for _, _, lit in g.triples((ontology_iri, predicate, None)):
        if isinstance(lit, Literal):
            return str(lit)
    return None

def iter_annotations(g: Graph, subj: URIRef, ns: str, prefix_map: dict) -> Iterable[Tuple[str, str]]:
    """Yield (predicate_qname, literal) for annotations on subj, excluding DESC_PROPS and SKIP_IN_OTHER."""
    for p, o in sorted(g.predicate_objects(subj), key=lambda po: get_qname(g, po[0], ns, prefix_map).lower()):
        if isinstance(o, Literal) and p not in SKIP_IN_OTHER:
            yield get_qname(g, p, ns, prefix_map), str(o)

def collect_list(g: Graph, node) -> list:
    """Collect RDF list members into a Python list."""
    members = []
    while node != RDF.nil:
        first = g.value(node, RDF.first)
        if first:
            members.append(first)
        node = g.value(node, RDF.rest)
    return members

def get_class_expression_str(g: Graph, expr, ns: str, prefix_map: dict) -> str:
    """Convert complex class expression to string representation."""
    if isinstance(expr, URIRef):
        return get_qname(g, expr, ns, prefix_map)
    if isinstance(expr, BNode):
        union_col = g.value(expr, OWL.unionOf)
        if union_col and union_col != RDF.nil:
            members = collect_list(g, union_col)
            return " or ".join(sorted(get_class_expression_str(g, m, ns, prefix_map) for m in members))
        inter_col = g.value(expr, OWL.intersectionOf)
        if inter_col and inter_col != RDF.nil:
            members = collect_list(g, inter_col)
            return " and ".join(sorted(get_class_expression_str(g, m, ns, prefix_map) for m in members))
        complement = g.value(expr, OWL.complementOf)
        if complement:
            return "not " + get_class_expression_str(g, complement, ns, prefix_map)
        oneOf_members = collect_oneOf(g, expr)
        if oneOf_members:
            return "Enum: " + ", ".join(sorted(get_qname(g, m, ns, prefix_map) for m in oneOf_members))
        return "ComplexExpr"  # Fallback
    return str(expr)

def get_leaf_classes(g: Graph, expr, ns: str, prefix_map: dict) -> list:
    """Recursively get leaf classes from class expressions."""
    leaves = []
    if isinstance(expr, URIRef):
        leaves.append(expr)
    elif isinstance(expr, BNode):
        union_col = g.value(expr, OWL.unionOf)
        inter_col = g.value(expr, OWL.intersectionOf)
        complement = g.value(expr, OWL.complementOf)
        oneOf_members = collect_oneOf(g, expr)
        if union_col and union_col != RDF.nil:
            members = collect_list(g, union_col)
            for m in members:
                leaves.extend(get_leaf_classes(g, m, ns, prefix_map))
        elif inter_col and inter_col != RDF.nil:
            members = collect_list(g, inter_col)
            for m in members:
                leaves.extend(get_leaf_classes(g, m, ns, prefix_map))
        elif complement:
            leaves.extend(get_leaf_classes(g, complement, ns, prefix_map))
        elif oneOf_members:
            leaves.extend(oneOf_members)  # Treat individuals as leaves
        else:
            leaves.append(expr)  # Fallback for other BNodes
    return leaves

def collect_oneOf(g: Graph, node) -> list:
    """Collect members of owl:oneOf if present."""
    if (node, RDF.type, OWL.Class) in g:
        oneOf_col = g.value(node, OWL.oneOf)
        if oneOf_col and oneOf_col != RDF.nil:
            return collect_list(g, oneOf_col)
    return []

def class_restrictions(g: Graph, cls: URIRef, ns: str, prefix_map: dict) -> list:
    """Collect restrictions for a class, including inherited refinements."""
    rows = []
    for restr in g.objects(cls, RDFS.subClassOf):
        if (restr, RDF.type, OWL.Restriction) in g:
            prop = g.value(restr, OWL.onProperty)
            if prop:
                prop_name, is_inverse, base_prop = get_property_info(g, prop, ns, prefix_map)
                is_refined = is_refined_property(g, cls, prop, restr)
                min_card = g.value(restr, OWL.minQualifiedCardinality) or g.value(restr, OWL.minCardinality)
                max_card = g.value(restr, OWL.maxQualifiedCardinality) or g.value(restr, OWL.maxCardinality)
                card = g.value(restr, OWL.qualifiedCardinality) or g.value(restr, OWL.cardinality)
                all_values_from = g.value(restr, OWL.allValuesFrom)
                some_values_from = g.value(restr, OWL.someValuesFrom)
                has_value = g.value(restr, OWL.hasValue)
                label_parts = []
                range_expr = None
                if all_values_from:
                    range_expr = all_values_from
                    label_parts.append("all")
                if some_values_from:
                    range_expr = some_values_from
                    label_parts.append("some")
                if has_value:
                    range_expr = has_value
                    label_parts.append("has")
                if card:
                    label_parts.append(f"exactly {card}")
                if min_card:
                    label_parts.append(f"min {min_card}")
                if max_card:
                    label_parts.append(f"max {max_card}")

                # Handle unqualified cardinality by treating as qualified with owl:Thing
                if label_parts and not range_expr:
                    range_expr = OWL.Thing

                if range_expr and label_parts:
                    range_name = get_class_expression_str(g, range_expr, ns, prefix_map)
                    rows.append((prop_name, f"{' '.join(label_parts)} {range_name}"))
            else:
                rows.append(("", "Unsupported restriction"))

    return rows

def hyperlink_class(name: str, all_classes: set, ns: str):
    """Create a hyperlink only for classes in the local namespace."""
    if ':' not in name and name in all_classes:
        return f"[{name}]({name}.md)"
    return name

def fmt_title(name: str, all_classes: set, ns: str, abstract_map: dict) -> str:
    """Format class title for Graphviz, with URL attribute for local classes."""
    display_name = f"<I>{insert_spaces(name)}</I>" if abstract_map.get(name, False) else insert_spaces(name)
    return display_name

def is_abstract(cls, g, ns):
    if cls is None:
        log.error("Invalid class URI provided to is_abstract: None")
        return False
    abstract = g.value(cls, URIRef(ns + "abstract"))
    if abstract is None:
        abstract = g.value(cls, URIRef("http://protege.stanford.edu/ontologies/metadata#abstract"))
    return abstract is not None and str(abstract).lower() == "true"

def get_id(qname):
    if not qname:
        log.error("Invalid qname provided to get_id: %s", qname)
        return "INVALID_QNAME"
    if ':' in qname:
        prefix, local = qname.split(':', 1)
        return prefix + '_' + local
    return qname

def get_all_class_superclasses(cls, g):
    if cls is None:
        log.error("Invalid class URI provided to get_all_class_superclasses: None")
        return set()
    direct_supers = set()
    for super_cls in g.objects(cls, RDFS.subClassOf):
        if isinstance(super_cls, URIRef) and super_cls != OWL.Thing and (super_cls, RDF.type, OWL.Class) in g:
            direct_supers.add(super_cls)
    all_supers = set(direct_supers)
    for sup in direct_supers:
        all_supers.update(get_all_class_superclasses(sup, g))
    return all_supers

def get_property_info(g: Graph, prop: URIRef, ns: str, prefix_map: dict) -> tuple:
    """Get property name, handling inverses."""
    if not prop:
        return None, False, None
    inverse_of = g.value(prop, OWL.inverseOf)
    if inverse_of:
        base_prop = inverse_of
        is_inverse = True
        prop_name = f"inverse {get_qname(g, base_prop, ns, prefix_map)}"
    else:
        base_prop = prop
        is_inverse = False
        prop_name = get_qname(g, base_prop, ns, prefix_map)
    return prop_name, is_inverse, base_prop

def is_refined_property(g: Graph, cls: URIRef, prop: URIRef, restriction: URIRef) -> bool:
    """Check if a property restriction in cls refines an inherited restriction."""
    if cls is None or prop is None or restriction is None:
        log.error("Invalid input to is_refined_property: cls=%s, prop=%s, restriction=%s", cls, prop, restriction)
        return False
    all_supers = get_all_class_superclasses(cls, g)
    for super_cls in all_supers:
        for super_restr in g.objects(super_cls, RDFS.subClassOf):
            if (super_restr, RDF.type, OWL.Restriction) in g:
                super_prop = g.value(super_restr, OWL.onProperty)
                if super_prop == prop:
                    current_avf = g.value(restriction, OWL.allValuesFrom)
                    super_avf = g.value(super_restr, OWL.allValuesFrom)
                    current_card = g.value(restriction, OWL.qualifiedCardinality) or g.value(restriction, OWL.minQualifiedCardinality) or g.value(restriction, OWL.maxQualifiedCardinality)
                    super_card = g.value(super_restr, OWL.qualifiedCardinality) or g.value(super_restr, OWL.minQualifiedCardinality) or g.value(super_restr, OWL.maxQualifiedCardinality)
                    current_on_class = g.value(restriction, OWL.onClass)
                    super_on_class = g.value(super_restr, OWL.onClass)
                    if (current_avf != super_avf or
                        current_card != super_card or
                        current_on_class != super_on_class):
                        return True
    return False

def insert_spaces(name: str) -> str:
    if not name:
        log.error("Invalid name provided to insert_spaces: %s", name)
        return "INVALID_NAME"
    name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', name)
    name = re.sub(r'([a-z\d])([A-Z])', r'\1 \2', name)
    return name

def get_ontology_for_uri(uri_str: str, ns_to_ontology: dict) -> str:
    norm_uri = _norm_base(uri_str)
    for ont_ns, ont_name in sorted(ns_to_ontology.items(), key=lambda x: len(x[0]), reverse=True):
        if norm_uri.startswith(_norm_base(ont_ns)):
            return ont_name
    return None