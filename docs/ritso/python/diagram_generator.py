import os
import logging
import traceback
from rdflib import Graph, RDF, RDFS, OWL, XSD, URIRef, BNode
from graphviz import Digraph
from collections import defaultdict
from utils import get_qname, get_id, fmt_title, get_all_class_superclasses, is_refined_property, collect_list, get_class_expression_str, get_ontology_for_uri, insert_spaces, get_leaf_classes, get_property_info, collect_oneOf

# Configure logging
log = logging.getLogger("ofn2mkdocs")

def get_target_info(g: Graph, expr, cls_name: str, ns: str, prefix_map: dict) -> tuple:
    """Get target information for a property's range, handling complex expressions."""
    if not expr:
        return None, False, None, None, False, None
    if isinstance(expr, URIRef):
        target_qname = get_qname(g, expr, ns, prefix_map)
        if target_qname == 'ITSThing':
            return None, False, None, None, False, None
        target_id = get_id(target_qname.replace(":", "_"))
        reflexive = target_qname == cls_name
        is_complex = False
        return target_id, is_complex, None, target_qname, reflexive, expr
    else:  # BNode, complex expression
        target_id = str(expr).replace(":", "_").replace("/", "_").replace("#", "_").replace("_:", "bnode_")
        target_qname = get_class_expression_str(g, expr, ns, prefix_map)
        reflexive = False
        is_complex = True
        return target_id, is_complex, None, target_qname, reflexive, expr

def add_class_expression_node(graph, g: Graph, expr, ns: str, prefix_map: dict, global_all_classes: set, ns_to_ontology: dict, abstract_map: dict, created: set, is_superclass: bool = False, in_associated_cluster: bool = False, enum_members: list = None, enum_name: str = None) -> tuple:
    """Recursively add nodes for class expressions, returning (node_id, label)."""
    if isinstance(expr, URIRef):
        qname = get_qname(g, expr, ns, prefix_map)
        node_id = get_id(qname.replace(":", "_"))
        if node_id in created:
            return node_id, qname
        created.add(node_id)
        local = qname.split(":")[-1]
        target_ont = get_ontology_for_uri(str(expr), ns_to_ontology)
        url = None if ':' in qname else f"../_counters/{target_ont}__{local}.md" if qname in global_all_classes else None
        label = qname
        graph.node(
            node_id,
            label=f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1"><TR><TD BGCOLOR="lightgray" ALIGN="CENTER">{label}</TD></TR></TABLE>>',
            URL=url,
            margin="0"
        )
        log.debug("Added node %s: %s (superclass=%s, in_associated_cluster=%s)", node_id, qname, is_superclass, in_associated_cluster)
        return node_id, qname
    else:  # BNode
        node_id = str(expr).replace(":", "_").replace("/", "_").replace("#", "_").replace("_:", "bnode_")
        if node_id in created:
            return node_id, get_class_expression_str(g, expr, ns, prefix_map)
        created.add(node_id)
        expr_str = get_class_expression_str(g, expr, ns, prefix_map)
        # Handle unionOf
        union_col = g.value(expr, OWL.unionOf)
        if union_col and union_col != RDF.nil:
            members = collect_list(g, union_col)
            stereo = "unionOf"
            graph.node(node_id, f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" BGCOLOR="lightyellow"><TR><TD ALIGN="CENTER">«{stereo}»</TD></TR></TABLE>>', margin="0")
            for member in sorted(members, key=str):
                member_id, _ = add_class_expression_node(graph, g, member, ns, prefix_map, global_all_classes, ns_to_ontology, abstract_map, created, is_superclass=False, in_associated_cluster=in_associated_cluster)
                graph.edge(node_id, member_id, style="dotted", label="member", arrowhead="normal")
            log.debug("Added union node %s: %s", node_id, expr_str)
            return node_id, ""
        # Handle intersectionOf
        inter_col = g.value(expr, OWL.intersectionOf)
        if inter_col and inter_col != RDF.nil:
            members = collect_list(g, inter_col)
            stereo = "intersectionOf"
            graph.node(node_id, f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" BGCOLOR="lightyellow"><TR><TD ALIGN="CENTER">«{stereo}»</TD></TR></TABLE>>', margin="0")
            for member in sorted(members, key=str):
                member_id, _ = add_class_expression_node(graph, g, member, ns, prefix_map, global_all_classes, ns_to_ontology, abstract_map, created, is_superclass=False, in_associated_cluster=in_associated_cluster)
                graph.edge(node_id, member_id, style="dotted", label="member", arrowhead="normal")
            return node_id, ""
        # Handle complementOf
        complement = g.value(expr, OWL.complementOf)
        if complement:
            stereo = "not"
            graph.node(node_id, f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" BGCOLOR="lightyellow"><TR><TD ALIGN="CENTER">«{stereo}»</TD></TR></TABLE>>', margin="0")
            comp_id, _ = add_class_expression_node(graph, g, complement, ns, prefix_map, global_all_classes, ns_to_ontology, abstract_map, created, is_superclass=False, in_associated_cluster=in_associated_cluster)
            graph.edge(node_id, comp_id, style="dotted", label="of", arrowhead="normal")
            log.debug("Added complement node %s: %s", node_id, expr_str)
            return node_id, ""
        # Handle oneOf enumeration
        oneOf_members = collect_oneOf(g, expr)
        if oneOf_members:
            stereo = "Enum"
            member_str = '<BR/>'.join([f"+ {get_qname(g, m, ns, prefix_map)}" for m in sorted(oneOf_members, key=str)])
            graph.node(node_id, f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1"><TR><TD BGCOLOR="lightgray" ALIGN="CENTER">«{stereo}»<BR/>{enum_name or expr_str}</TD></TR><TR><TD ALIGN="LEFT">{member_str}</TD></TR></TABLE>>', margin="0")
            log.debug("Added enum node %s: %s with members %s", node_id, enum_name or expr_str, oneOf_members)
            return node_id, enum_name or ""
        # Default for other expressions
        graph.node(node_id, f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" BGCOLOR="lightyellow"><TR><TD ALIGN="CENTER">{expr_str}</TD></TR></TABLE>>', margin="0")
        log.debug("Added fallback node %s: %s", node_id, expr_str)
        return node_id, expr_str

def generate_diagram(g: Graph, cls: URIRef, cls_name: str, cls_id: str, ns: str, global_all_classes: set, abstract_map: dict, ofn_path: str, errors: list, prefix_map: dict, ontology_name: str, ns_to_ontology: dict):
    """Generate a DOT file for a given class, producing an ODM-like diagram with associated cluster defined before edges."""
    # Ensure output directory exists
    diagrams_dir = os.path.join(os.path.dirname(ofn_path), "diagrams")
    if not os.path.exists(diagrams_dir):
        os.makedirs(diagrams_dir)
        log.info(f"Created diagrams directory: {diagrams_dir}")
    cls_filename = f"{ontology_name}__{cls_name}"

    # Initialize Digraph with ODM-like styling
    dot = Digraph(
        comment=f"Diagram for {cls_name}",
        format="svg",
        graph_attr={"overlap": "false", "splines": "true", "rankdir": "TB"},
        node_attr={"shape": "none", "fontsize": "12", "fontname": "Arial", "margin": "0"},
        edge_attr={"fontsize": "11", "fontname": "Arial"}
    )
    dot.engine = 'dot'  # Use dot for better hierarchical layout

    # Track combined properties to merge restrictions
    combined = defaultdict(dict)

    # Add main class node with datatype properties
    with dot.subgraph() as main_group:
        main_group.attr(rank='max')
        data_props = defaultdict(list)
        for restriction in g.objects(cls, RDFS.subClassOf):
            if (restriction, RDF.type, OWL.Restriction) in g:
                prop = g.value(restriction, OWL.onProperty)
                if not prop:
                    continue
                prop_name, is_inverse, base_prop = get_property_info(g, prop, ns, prefix_map)
                if base_prop and (base_prop, RDF.type, OWL.DatatypeProperty) in g:
                    range_type = g.value(base_prop, RDFS.range) or XSD.string
                    range_name = get_class_expression_str(g, range_type, ns, prefix_map)
                    restrictions = []
                    stereotype = "refined" if is_refined_property(g, cls, base_prop, restriction) else ""
                    if is_inverse:
                        stereotype += ", inverse" if stereotype else "inverse"
                    all_values_from = g.value(restriction, OWL.allValuesFrom)
                    if all_values_from:
                        range_name = get_class_expression_str(g, all_values_from, ns, prefix_map)
                        restrictions.append("only")
                    on_data_range = g.value(restriction, OWL.onDataRange)
                    qualified_card = g.value(restriction, OWL.qualifiedCardinality)
                    min_qualified_card = g.value(restriction, OWL.minQualifiedCardinality)
                    max_qualified_card = g.value(restriction, OWL.maxQualifiedCardinality)
                    if qualified_card:
                        restrictions.append(f"exactly {qualified_card}")
                    if min_qualified_card:
                        restrictions.append(f"min {min_qualified_card}")
                    if max_qualified_card:
                        restrictions.append(f"max {max_qualified_card}")
                    if on_data_range:
                        range_name = get_class_expression_str(g, on_data_range, ns, prefix_map)
                    card = g.value(restriction, OWL.cardinality)
                    min_card = g.value(restriction, OWL.minCardinality)
                    max_card = g.value(restriction, OWL.maxCardinality)
                    if card:
                        restrictions.append(f"exactly {card}")
                    if min_card:
                        restrictions.append(f"min {min_card}")
                    if max_card:
                        restrictions.append(f"max {max_card}")
                    restriction_str = f"«{', '.join(restrictions)}»" if restrictions else ""
                    data_props[prop_name].append((restriction_str, range_name, stereotype))
                    log.debug("Added datatype property %s: %s «%s»", prop_name, range_name, stereotype)

        attributes = []
        for prop_name, restrictions in sorted(data_props.items()):
            all_restrictions = []
            range_names = set()
            stereotypes = set()
            for restriction_str, range_name, stereotype in restrictions:
                if restriction_str:
                    all_restrictions.append(restriction_str)
                range_names.add(range_name)
                if stereotype:
                    stereotypes.add(stereotype)
            range_name = range_names.pop() if range_names else "string"
            restriction_label = ", ".join(sorted(set(r.strip('«»') for r in all_restrictions))) if all_restrictions else ""
            stereotype_label = ", ".join(sorted(set(s for s in stereotypes))) if stereotypes else ""
            attribute = f"{prop_name}: {range_name}"
            if restriction_label or stereotype_label:
                labels = [l for l in [restriction_label, stereotype_label] if l]
                attribute = f"{attribute} «{', '.join(labels)}»"
            attributes.append(attribute)

        attributes_html = "".join(f'<TR><TD ALIGN="LEFT">{prop}</TD></TR>' for prop in attributes)
        main_label = f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1"><TR><TD BGCOLOR="lightgray" ALIGN="CENTER" PORT="e">{cls_name}</TD></TR>{attributes_html}</TABLE>>'
        main_group.node(
            cls_id,
            main_label,
            URL=f"../classes/{ontology_name}__{cls_name}.md" if cls_name in global_all_classes else None,
            margin="0"
        )
        log.debug("Added main class node %s: %s", cls_id, cls_name)

    # Add superclasses (direct superclasses via rdfs:subClassOf)
    super_uris = set()
    for super_cls in g.objects(cls, RDFS.subClassOf):
        if isinstance(super_cls, URIRef) and super_cls != OWL.Thing:
            super_uris.add(super_cls)
    superclasses = {get_qname(g, u, ns, prefix_map) for u in super_uris}
    created = set()
    for sup_uri in sorted(super_uris, key=lambda u: get_qname(g, u, ns, prefix_map).lower()):
        sup_id, _ = add_class_expression_node(dot, g, sup_uri, ns, prefix_map, global_all_classes, ns_to_ontology, abstract_map, created, is_superclass=True)
        log.debug("Added superclass node %s", sup_id)

    # Collect associated classes for object properties
    associated_uris = set()
    for restriction in g.objects(cls, RDFS.subClassOf):
        if (restriction, RDF.type, OWL.Restriction) in g:
            prop = g.value(restriction, OWL.onProperty)
            if prop and (prop, RDF.type, OWL.ObjectProperty) in g:
                for target_expr in [g.value(restriction, p) for p in (OWL.onClass, OWL.allValuesFrom, OWL.someValuesFrom) if g.value(restriction, p)]:
                    leaf_classes = get_leaf_classes(g, target_expr, ns, prefix_map)
                    for leaf in leaf_classes:
                        if isinstance(leaf, URIRef):
                            leaf_qname = get_qname(g, leaf, ns, prefix_map)
                            if leaf_qname != cls_name and leaf_qname not in superclasses:
                                associated_uris.add(leaf)
                                log.debug("Added associated URI: %s", leaf_qname)

    # Create associated cluster and add nodes
    assoc_nodes = []
    created_complex = set()
    with dot.subgraph(name='cluster_associated') as associated_cluster:
        associated_cluster.attr(style='invis', label='')
        associated_cluster.node('Invis', label='<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1"><TR><TD></TD></TR></TABLE>>', style='invis', margin="0")
        for assoc_uri in sorted(associated_uris, key=lambda u: get_qname(g, u, ns, prefix_map).lower()):
            assoc_id, _ = add_class_expression_node(associated_cluster, g, assoc_uri, ns, prefix_map, global_all_classes, ns_to_ontology, abstract_map, created_complex, is_superclass=False, in_associated_cluster=True)
            assoc_nodes.append(assoc_id)
            log.debug("Added associated node %s", assoc_id)

    # Process object properties
    for restriction in g.objects(cls, RDFS.subClassOf):
        if (restriction, RDF.type, OWL.Restriction) in g:
            prop = g.value(restriction, OWL.onProperty)
            if not prop:
                continue
            prop_name, is_inverse, base_prop = get_property_info(g, prop, ns, prefix_map)
            if base_prop and (base_prop, RDF.type, OWL.ObjectProperty) in g:
                is_refined = is_refined_property(g, cls, base_prop, restriction)
                style = "dashed" if is_refined else "solid"
                label_parts = []
                target_expr = None
                reflexive = False

                on_class = g.value(restriction, OWL.onClass)
                qualified_card = g.value(restriction, OWL.qualifiedCardinality)
                min_qualified_card = g.value(restriction, OWL.minQualifiedCardinality)
                max_qualified_card = g.value(restriction, OWL.maxQualifiedCardinality)
                if qualified_card:
                    label_parts.append(f"exactly {qualified_card}")
                if min_qualified_card:
                    label_parts.append(f"min {min_qualified_card}")
                if max_qualified_card:
                    label_parts.append(f"max {max_qualified_card}")
                if label_parts and on_class:
                    target_expr = on_class

                all_values_from = g.value(restriction, OWL.allValuesFrom)
                if all_values_from:
                    label_parts.append("only")
                    target_expr = all_values_from

                some_values_from = g.value(restriction, OWL.someValuesFrom)
                if some_values_from:
                    label_parts.append("some")
                    target_expr = some_values_from

                card = g.value(restriction, OWL.cardinality)
                min_card = g.value(restriction, OWL.minCardinality)
                max_card = g.value(restriction, OWL.maxCardinality)
                if card:
                    label_parts.append(f"exactly {card}")
                if min_card:
                    label_parts.append(f"min {min_card}")
                if max_card:
                    label_parts.append(f"max {max_card}")

                # Handle unqualified cardinality by treating as qualified with owl:Thing
                if label_parts and not target_expr:
                    target_expr = OWL.Thing

                if target_expr and label_parts:
                    # Check for oneOf enumeration
                    oneOf_members = collect_oneOf(g, target_expr)
                    enum_name = None
                    if oneOf_members:
                        prop_local = prop_name.split(':')[-1]
                        enum_name = f"{prop_local[0].upper()}{prop_local[1:]}Enum"
                    target_id, _, _, target_qname, reflexive, _ = get_target_info(g, target_expr, cls_name, ns, prefix_map)
                    key = (prop_name, target_id)
                    if key not in combined:
                        combined[key] = {
                            'label_parts': [],
                            'style': style,
                            'prop_name': prop_name,
                            'target_expr': target_expr,
                            'reflexive': reflexive,
                            'target_qname': target_qname,
                            'is_inverse': is_inverse,
                            'enum_members': oneOf_members,
                            'enum_name': enum_name
                        }
                    combined[key]['label_parts'].extend(label_parts)
                    combined[key]['style'] = "dashed" if is_refined else combined[key]['style']
                    log.debug("Added object property %s -> %s: %s, style=%s, reflexive=%s", prop_name, target_qname, label_parts, style, reflexive)

    # Add edges for superclasses
    for sup_uri in sorted(super_uris, key=lambda u: get_qname(g, u, ns, prefix_map).lower()):
        sup_id, _ = add_class_expression_node(dot, g, sup_uri, ns, prefix_map, global_all_classes, ns_to_ontology, abstract_map, created, is_superclass=True)
        dot.edge(cls_id, sup_id, arrowhead="onormal", style="solid")
        log.debug("Added generalization edge %s -> %s", cls_id, sup_id)

    # Add invisible edges for layout
    if assoc_nodes:
        dot.edge(cls_id, 'Invis', style="invis")
        prev = 'Invis'
        for assoc_id in assoc_nodes:
            dot.edge(prev, assoc_id, style="invis")
            log.debug("Added invisible edge %s -> %s", prev, assoc_id)
            prev = assoc_id

    # Add object property edges
    for key, data in combined.items():
        prop_name = data['prop_name']
        style = data['style']
        label_parts = data['label_parts']
        reflexive = data['reflexive']
        target_expr = data['target_expr']
        is_inverse = data['is_inverse']
        enum_members = data.get('enum_members', [])
        enum_name = data.get('enum_name')
        target_id, target_label = add_class_expression_node(dot, g, target_expr, ns, prefix_map, global_all_classes, ns_to_ontology, abstract_map, created_complex, is_superclass=False, in_associated_cluster=True)
        label_prefix = f"«{', '.join(sorted(set(label_parts)))}» " if label_parts else ""
        if style == "solid":
            label = f" {prop_name} \n {label_prefix} "
        else:
            label = f" onProperty: {prop_name} \n {label_prefix} "
        source_id = cls_id if not is_inverse else target_id
        dest_id = target_id if not is_inverse else cls_id
        arrowhead = "normal" if not is_inverse else "inv"
        if reflexive:
            dot.edge(cls_id, cls_id, label=label, style=style, arrowhead=arrowhead)
        else:
            dot.edge(source_id, dest_id, label=label, style=style, arrowhead=arrowhead)
        log.debug("Added edge %s -> %s: %s", source_id, dest_id, label)

    # Save and render the DOT file
    log.debug("Generated DOT source for %s:\n%s", cls_name, dot.source)
    try:
        dot_file = os.path.join(diagrams_dir, f"{cls_filename}.dot")
        dot.save(dot_file)
        with open(dot_file, 'r') as f:
            log.debug("DOT file content:\n%s", f.read())
        dot.render(dot_file, cleanup=False)
        dot.render(dot_file, format='png', cleanup=False)
    except Exception as e:
        error_msg = f"Error rendering diagram for {cls_name} from {ofn_path}: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)
        raise

def main():
    """Main function to process the ontology and generate diagrams."""
    g = Graph()
    g.parse("Activity.owl", format="xml")
    ns = "https://standards.iso.org/iso-iec/5087/-1/ed-1/en/ontology/Activity#"
    prefix_map = {
        "activity": ns,
        "time": "http://www.w3.org/2006/time#",
        "spatialLoc": "https://standards.iso.org/iso-iec/5087/-1/ed-1/en/ontology/SpatialLoc#",
        "change": "https://standards.iso.org/iso-iec/5087/-1/ed-1/en/ontology/Change#",
        "owl": "http://www.w3.org/2002/07/owl#"
    }
    ontology_name = "Activity"
    ns_to_ontology = {ns: "Activity"}
    global_all_classes = {get_qname(g, s, ns, prefix_map) for s, p, o in g.triples((None, RDF.type, OWL.Class))}
    abstract_map = {}  # Assume no abstract classes for simplicity
    errors = []

    # Generate diagrams for each class
    for cls in g.subjects(RDF.type, OWL.Class):
        cls_name = get_qname(g, cls, ns, prefix_map)
        cls_id = get_id(cls_name.replace(":", "_"))
        generate_diagram(g, cls, cls_name, cls_id, ns, global_all_classes, abstract_map, "Activity.owl", errors, prefix_map, ontology_name, ns_to_ontology)

    if errors:
        log.error("Errors encountered: %s", errors)

if __name__ == "__main__":
    main()