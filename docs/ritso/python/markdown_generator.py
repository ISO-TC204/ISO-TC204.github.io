import os
import logging
import yaml
import re
import traceback
from collections import defaultdict
from rdflib import Graph, XSD, Literal, URIRef, OWL, RDFS, RDF
from rdflib.namespace import DCTERMS, SKOS
from utils import get_qname, get_first_literal, hyperlink_class, insert_spaces, class_restrictions, iter_annotations, DESC_PROPS, get_ontology_for_uri

log = logging.getLogger("owl2mkdocs")

class SafeMkDocsLoader(yaml.SafeLoader):
    """Custom YAML loader to handle MkDocs-specific python/name tags."""
    def ignore_python_name(self, node):
        """Treat python/name tags as strings."""
        return self.construct_scalar(node)

yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji', SafeMkDocsLoader.ignore_python_name)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format', SafeMkDocsLoader.ignore_python_name)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/name:material.extensions.emoji.to_svg', SafeMkDocsLoader.ignore_python_name)

def get_specializations(g: Graph, cls: URIRef, global_all_classes: set, ns: str, prefix_map: dict, ns_to_ontology: dict) -> list:
    """Find all subclasses (direct and indirect) of the given class."""
    specializations = []
    visited = set()
    def collect_subclasses(c):
        if c in visited:
            return
        visited.add(c)
        for s in g.subjects(RDFS.subClassOf, c):
            if isinstance(s, URIRef) and s != c:
                cls_name = get_first_literal(g, s, [RDFS.label]) or str(s).split('/')[-1].split('#')[-1]
                ont = get_ontology_for_uri(str(s), ns_to_ontology)
                if cls_name in global_all_classes and ont:
                    desc = get_first_literal(g, s, [DCTERMS.description]) or ""
                    specializations.append((cls_name, desc, ont))
                collect_subclasses(s)
    collect_subclasses(cls)
    log.debug(f"Specializations for {cls}: {specializations}")
    return sorted(specializations, key=lambda x: x[0].lower())

def get_used_by(g: Graph, cls: URIRef, global_all_classes: set, ns: str, prefix_map: dict, ns_to_ontology: dict) -> list:
    """Find classes and their properties that reference this class via object property restrictions."""
    used_by = []
    for s in g.subjects(RDF.type, OWL.Restriction):
        prop = g.value(s, OWL.onProperty)
        for predicate in [OWL.allValuesFrom, OWL.someValuesFrom, OWL.hasValue]:
            target = g.value(s, predicate)
            if target == cls and prop:
                prop_name = get_qname(g, prop, ns, prefix_map)
                for cls_sub in g.subjects(RDFS.subClassOf, s):
                    if isinstance(cls_sub, URIRef):
                        cls_name = get_first_literal(g, cls_sub, [RDFS.label]) or str(cls_sub).split('/')[-1].split('#')[-1]
                        ont = get_ontology_for_uri(str(cls_sub), ns_to_ontology)
                        if cls_name in global_all_classes and ont:
                            used_by.append((cls_name, prop_name, ont))
                cls_name = get_first_literal(g, s, [RDFS.label]) or str(s).split('/')[-1].split('#')[-1]
                ont = get_ontology_for_uri(str(s), ns_to_ontology)
                if cls_name in global_all_classes and ont:
                    used_by.append((cls_name, prop_name, ont))
    log.debug(f"Used by for {cls}: {used_by}")
    return sorted(used_by, key=lambda x: x[0].lower())

def generate_markdown(g: Graph, cls: URIRef, cls_name: str, global_patterns: dict, global_all_classes: set, ns: str, file_path: str, errors: list, prefix_map: dict, prop_map: dict, ontology_name: str, ns_to_ontology: dict, class_to_onts: dict):
    """Generate Markdown file for a class, including all superclasses and disjoint statements in Formalization."""
    classes_dir = os.path.join(os.path.dirname(file_path), "classes")
    filename = os.path.join(classes_dir, f"{ontology_name}__{cls_name}.md")
    
    log.debug(f"Writing {filename} for class {cls_name} ({cls})")
    
    # Check if this is a pattern class
    is_pattern = cls_name in global_patterns

    if is_pattern:
        # Pattern class Markdown
        title = f"# {insert_spaces(cls_name)}\n\n"
        desc = get_first_literal(g, cls, [DCTERMS.description]) or ""
        top_desc = f"{desc}\n\n" if desc else ""
        members_md = "It consists of the following classes:\n\n"
        member_tuples = global_patterns[cls_name]["classes"]
        for mem_cls, mem_ont in sorted(member_tuples, key=lambda x: x[0].lower()):
            if mem_cls == 'ITSThing':
                continue
            display_mem = insert_spaces(mem_cls)
            if len(class_to_onts[mem_cls]) > 1:
                display_mem += f" ({mem_ont})"
            members_md += f"- [{display_mem}]({mem_ont}__{mem_cls}.md)\n"
        content = title + top_desc + members_md
    else:
        # Non-pattern class Markdown
        title = f"# {cls_name}\n\n"
        desc = get_first_literal(g, cls, [DCTERMS.description]) or ""
        top_desc = f"{desc}\n\n" if desc else ""
        note = get_first_literal(g, cls, [SKOS.note]) or ""
        note_md = f"NOTE: {note}\n\n" if note else ""
        example = get_first_literal(g, cls, [SKOS.example]) or ""
        example_md = f"EXAMPLE: {example}\n\n" if example else ""
        diagram_line = f"![{cls_name} Diagram](../diagrams/{ontology_name}__{cls_name}.dot.svg)\n\n<a href=\"../../diagrams/{ontology_name}__{cls_name}.dot.svg\">Open interactive {cls_name} diagram</a>\n\n"
        
        # Specializations section
        specializations = get_specializations(g, cls, global_all_classes, ns, prefix_map, ns_to_ontology)
        specializations_md = ""
        if specializations:
            specializations_md += f"## Specializations of {cls_name}\n\n"
            specializations_md += "| Class | Description |\n"
            specializations_md += "|-------|-------------|\n"
            for spec_cls, spec_desc, spec_ont in specializations:
                display_spec = insert_spaces(spec_cls)
                if len(class_to_onts[spec_cls]) > 1:
                    display_spec += f" ({spec_ont})"
                link = f"{spec_ont}__{spec_cls}.md"
                specializations_md += f"| [{display_spec}]({link}) | {spec_desc} |\n"
            specializations_md += "\n"
        else:
            log.debug(f"No specializations found for {cls_name}")
        
        # Formalization section with superclasses and disjoints
        restr_rows = class_restrictions(g, cls, ns, prefix_map)
        # Collect direct superclasses
        superclasses = []
        for super_cls in g.objects(cls, RDFS.subClassOf):
            if isinstance(super_cls, URIRef) and super_cls != OWL.Thing:
                super_name = get_qname(g, super_cls, ns, prefix_map)
                superclasses.append(("subClassOf", super_name))
        # Collect disjoint classes
        disjoints = []
        for disjoint_cls in g.objects(cls, OWL.disjointWith):
            if isinstance(disjoint_cls, URIRef):
                disjoint_name = get_qname(g, disjoint_cls, ns, prefix_map)
                disjoints.append(("disjointWith", disjoint_name))
        # Combine with restrictions from class_restrictions
        formalization_rows = sorted(restr_rows + superclasses + disjoints, key=lambda x: x[0].lower())
        formalization_md = ""
        if formalization_rows:
            formalization_md += f"## Formalization for {cls_name}\n\n"
            formalization_md += "| Property | Constraint |\n"
            formalization_md += "|----------|------------|\n"
            for prop, constr in formalization_rows:
                log.debug(f"Restriction for {cls_name}: ({prop}, '{constr}')")
                formalization_md += f"| {prop} | {constr} |\n"
            formalization_md += "\n"
        
        # Used by section
        used_by = get_used_by(g, cls, global_all_classes, ns, prefix_map, ns_to_ontology)
        used_by_md = ""
        if used_by:
            used_by_md += f"## Used by classes\n\n"
            used_by_md += "| Class | Property |\n"
            used_by_md += "|-------|----------|\n"
            for used_cls, used_prop, used_ont in used_by:
                display_used = insert_spaces(used_cls)
                if len(class_to_onts[used_cls]) > 1:
                    display_used += f" ({used_ont})"
                link = f"{used_ont}__{used_cls}.md"
                used_by_md += f"| [{display_used}]({link}) | {used_prop} |\n"
            used_by_md += "\n"
        
        # Other annotations
        other_annot_md = ""
        annotations = list(iter_annotations(g, cls, ns, prefix_map))
        if annotations:
            other_annot_md += "## Other annotations\n\n"
            other_annot_md += "| Annotation | Value |\n"
            other_annot_md += "|------------|-------|\n"
            for pred, val in sorted(annotations):
                other_annot_md += f"| {pred} | {val} |\n"
            other_annot_md += "\n"
        
        content = title + top_desc + note_md + example_md + diagram_line + specializations_md + formalization_md + used_by_md + other_annot_md

    # Write Markdown file
    try:
        os.makedirs(classes_dir, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        log.debug("Generated Markdown file: %s", filename)
    except Exception as e:
        error_msg = f"Error writing Markdown for {cls_name} from {file_path}: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)
        raise

def update_mkdocs_nav(mkdocs_path: str, global_patterns: dict, global_all_classes: set, errors: list, class_to_onts: dict, ontology_info: dict, input_files: list):
    """Update mkdocs.yml navigation with file > pattern > class or file > class structure."""
    try:
        with open(mkdocs_path, 'r', encoding="utf-8") as f:
            config = yaml.load(f, Loader=SafeMkDocsLoader)
    except Exception as e:
        error_msg = f"Error reading mkdocs.yml: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)
        raise

    new_nav = [{"Home": "index.md"}]
    
    if len(input_files) == 1:
        # Single file case: PatternName > ClassName or ClassName
        file_path = input_files[0]
        ontology_name = ontology_info[file_path]["ontology_name"]
        # Patterns
        pattern_names = sorted(ontology_info[file_path]["patterns"], key=str.lower)
        for pat_name in pattern_names:
            if pat_name == 'ITSThing':
                continue
            display_pat = insert_spaces(pat_name)
            if len(class_to_onts[pat_name]) > 1:
                display_pat += f" ({ontology_name})"
            sub_nav = []
            member_tuples = global_patterns.get(pat_name, {"classes": []})["classes"]
            # Filter members to this ontology
            member_dict = defaultdict(list)
            for mem_cls, mem_ont in member_tuples:
                if mem_ont == ontology_name:
                    member_dict[mem_cls].append(mem_ont)
            for mem_cls in sorted(member_dict.keys(), key=str.lower):
                if mem_cls == 'ITSThing':
                    continue
                display_mem = insert_spaces(mem_cls)
                if len(class_to_onts[mem_cls]) > 1:
                    display_mem += f" ({ontology_name})"
                sub_nav.append({display_mem: f"classes/{ontology_name}__{mem_cls}.md"})
            if sub_nav:  # Only add pattern if it has classes
                new_nav.append({display_pat: sub_nav})
        # Non-pattern classes
        non_pattern_classes = sorted(
            [cls for cls in ontology_info[file_path]["non_pattern_classes"] if cls not in global_patterns and cls != 'ITSThing'],
            key=str.lower
        )
        for cls_name in non_pattern_classes:
            display_cls = insert_spaces(cls_name)
            if len(class_to_onts[cls_name]) > 1:
                display_cls += f" ({ontology_name})"
            new_nav.append({display_cls: f"classes/{ontology_name}__{cls_name}.md"})
    else:
        # Multiple files case: FileName > PatternName > ClassName or FileName > ClassName
        for file_path in sorted(ontology_info.keys(), key=lambda x: ontology_info[x]["title"].lower()):
            ontology_name = ontology_info[file_path]["ontology_name"]
            display_ont = ontology_info[file_path]["title"] or ontology_name
            ont_nav = []
            # Patterns
            pattern_names = sorted(ontology_info[file_path]["patterns"], key=str.lower)
            for pat_name in pattern_names:
                if pat_name == 'ITSThing':
                    continue
                display_pat = insert_spaces(pat_name)
                if len(class_to_onts[pat_name]) > 1:
                    display_pat += f" ({ontology_name})"
                sub_nav = []
                member_tuples = global_patterns.get(pat_name, {"classes": []})["classes"]
                # Filter members to this ontology
                member_dict = defaultdict(list)
                for mem_cls, mem_ont in member_tuples:
                    if mem_ont == ontology_name:
                        member_dict[mem_cls].append(mem_ont)
                for mem_cls in sorted(member_dict.keys(), key=str.lower):
                    if mem_cls == 'ITSThing':
                        continue
                    display_mem = insert_spaces(mem_cls)
                    if len(class_to_onts[mem_cls]) > 1:
                        display_mem += f" ({ontology_name})"
                    sub_nav.append({display_mem: f"classes/{ontology_name}__{mem_cls}.md"})
                if sub_nav:  # Only add pattern if it has classes
                    ont_nav.append({display_pat: sub_nav})
            # Non-pattern classes
            non_pattern_classes = sorted(
                [cls for cls in ontology_info[file_path]["non_pattern_classes"] if cls not in global_patterns and cls != 'ITSThing'],
                key=str.lower
            )
            for cls_name in non_pattern_classes:
                display_cls = insert_spaces(cls_name)
                if len(class_to_onts[cls_name]) > 1:
                    display_cls += f" ({ontology_name})"
                ont_nav.append({display_cls: f"classes/{ontology_name}__{cls_name}.md"})
            if ont_nav:  # Only add ontology if it has patterns or classes
                new_nav.append({display_ont: ont_nav})

    config["nav"] = new_nav
    try:
        with open(mkdocs_path, 'w', encoding="utf-8") as f:
            yaml.safe_dump(config, f, sort_keys=False, allow_unicode=True)
    except Exception as e:
        error_msg = f"Error writing mkdocs.yml: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)
        raise

def generate_index(docs_dir: str, input_files: list, ontology_info: dict, global_patterns: dict, errors: list, class_to_onts: dict):
    """Generate index.md file."""
    index_path = os.path.join(docs_dir, "index.md")
    index_content = ""

    if len(input_files) == 1:
        # Single file case
        file_path = input_files[0]
        if file_path not in ontology_info:
            error_msg = f"Skipping index.md generation for {file_path} due to earlier processing failure"
            errors.append(error_msg)
            log.error(error_msg)
            return
        filename = os.path.basename(file_path)
        title = ontology_info[file_path]["title"]
        description = ontology_info[file_path]["description"]
        patterns = sorted(ontology_info[file_path]["patterns"], key=str.lower)
        non_pattern_classes = sorted(ontology_info[file_path]["non_pattern_classes"], key=str.lower)

        index_content += f"# {title}\n\n"
        if description:
            index_content += f"{description}\n\n"
        index_content += "This ontology consists of the following patterns:\n\n"
        for pat_name in patterns:
            if pat_name == 'ITSThing':
                continue
            pat_ont = ontology_info[file_path]["ontology_name"]
            display_pat = insert_spaces(pat_name)
            if len(class_to_onts[pat_name]) > 1:
                display_pat += f" ({pat_ont})"
            index_content += f"- [{display_pat}](classes/{pat_ont}__{pat_name}.md)\n"
        if non_pattern_classes:
            index_content += "\nThe ontology also contains the following classes that are not assigned to any pattern:\n\n"
            for cls_name in non_pattern_classes:
                if cls_name == 'ITSThing':
                    continue
                cls_ont = ontology_info[file_path]["ontology_name"]
                display_cls = insert_spaces(cls_name)
                if len(class_to_onts[cls_name]) > 1:
                    display_cls += f" ({cls_ont})"
                index_content += f"- [{display_cls}](classes/{cls_ont}__{cls_name}.md)\n"
        index_content += f"\nThe formal definition of these patterns is available in [{os.path.splitext(filename)[1][1:].upper()} Syntax]({filename}).\n"
    else:
        # Multiple files case
        readme_path = os.path.join(os.path.dirname(docs_dir), "README.md")
        if os.path.exists(readme_path):
            try:
                with open(readme_path, 'r', encoding="utf-8") as f:
                    first_line = f.readline().strip()
                    title = first_line.lstrip('#').strip() if first_line.startswith('#') else first_line
            except Exception as e:
                error_msg = f"Error reading README.md: {str(e)}\n{traceback.format_exc()}"
                errors.append(error_msg)
                log.error(error_msg)
                title = "No README.md file found for title"
        else:
            title = "No README.md file found for title"

        index_content += f"# {title}\n\n"
        for file_path in sorted(input_files, key=lambda x: ontology_info[x]["title"].lower()):
            if file_path not in ontology_info:
                error_msg = f"Skipping index.md generation for {file_path} due to earlier processing failure"
                errors.append(error_msg)
                log.error(error_msg)
                continue
            filename = os.path.basename(file_path)
            title = ontology_info[file_path]["title"] or "Unknown Title"
            description = ontology_info[file_path]["description"] or "Unknown description"
            ont_name = ontology_info[file_path]["ontology_name"]
            if not ontology_info[file_path]["title"]:
                log.warning("The ontology %s is missing a dc:title annotation.", filename)
            if not ontology_info[file_path]["description"]:
                log.warning("The ontology %s is missing a dcterms:description annotation.", filename)
            patterns = sorted(ontology_info[file_path]["patterns"], key=str.lower)
            non_pattern_classes = sorted(ontology_info[file_path]["non_pattern_classes"], key=str.lower)

            index_content += f"## {title}\n\n"
            if description:
                index_content += f"{description}\n\n"
            index_content += "This ontology consists of the following patterns:\n\n"
            for pat_name in patterns:
                if pat_name == 'ITSThing':
                    continue
                display_pat = insert_spaces(pat_name)
                if len(class_to_onts[pat_name]) > 1:
                    display_pat += f" ({ont_name})"
                index_content += f"- [{display_pat}](classes/{ont_name}__{pat_name}.md)\n"
            if non_pattern_classes:
                index_content += "\nThe ontology also contains the following classes that are not assigned to any pattern:\n\n"
                for cls_name in non_pattern_classes:
                    if cls_name == 'ITSThing':
                        continue
                    display_cls = insert_spaces(cls_name)
                    if len(class_to_onts[cls_name]) > 1:
                        display_cls += f" ({ont_name})"
                    index_content += f"- [{display_cls}](classes/{ont_name}__{cls_name}.md)\n"
            index_content += f"\nThe formal definition of these patterns is available in [{os.path.splitext(filename)[1][1:].upper()} Syntax]({filename}).\n\n"

    # Write index.md
    try:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        log.info("Generated index.md at %s", index_path)
    except Exception as e:
        error_msg = f"Error writing index.md: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)
        raise