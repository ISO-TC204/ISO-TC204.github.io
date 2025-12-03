import os
import sys
import logging
import traceback
from collections import defaultdict
from ontology_processor_ttl import process_ontology
from diagram_generator import generate_diagram
from markdown_generator import generate_markdown, update_mkdocs_nav, generate_index
from utils import get_qname, get_label, is_abstract, get_id
from rdflib import Graph, RDF, XSD, URIRef, Literal

# -------------------- logging --------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")
log = logging.getLogger("ttl2mkdocs")

def main():
    # Check if script is called without arguments
    if len(sys.argv) != 1:
        print("Usage: python ttl2mkdocs.py")
        sys.exit(1)

    # Check for mkdocs.yml in current directory
    root_dir = os.getcwd()
    mkdocs_path = os.path.join(root_dir, "mkdocs.yml")
    if not os.path.exists(mkdocs_path):
        print("Error: mkdocs.yml not found in current directory")
        sys.exit(1)

    # Check for docs directory
    docs_dir = os.path.join(root_dir, "docs")
    if not os.path.isdir(docs_dir):
        print("Error: docs directory not found")
        sys.exit(1)

    # Find all .ttl files in docs directory
    ttl_files = [os.path.join(docs_dir, f) for f in os.listdir(docs_dir) if f.lower().endswith('.ttl')]
    if not ttl_files:
        print("No .ttl files found in docs/")
        sys.exit(0)

    # Initialize global collections
    global_patterns = {}
    global_all_classes = set()
    abstract_map = {}
    ontology_info = {}
    errors = []
    processed_count = 0
    ns_to_ontology = {}
    class_to_onts = defaultdict(list)

    # Process each TTL file
    for ttl_path in sorted(ttl_files):
        ontology_name = os.path.splitext(os.path.basename(ttl_path))[0]
        log.info("########## Processing ontology file: %s", ttl_path)
        # Initialize ontology_info for this file
        ontology_info[ttl_path] = {
            "title": "Untitled Ontology",
            "description": "",
            "patterns": set(),
            "non_pattern_classes": set(),
            "ontology_name": ontology_name
        }
        try:
            # Process ontology
            g, ns, prefix_map, classes, local_classes, prop_map = process_ontology(ttl_path, errors, ontology_info[ttl_path])
            if g is None:
                continue
            ns_to_ontology[ns] = ontology_name

            # Update global collections
            for cls in classes:
                cls_qname = get_qname(g, cls, ns, prefix_map)
                abstract_map[cls_qname] = is_abstract(cls, g, ns)
                if cls_qname != 'ITSThing':
                    global_all_classes.add(cls_qname)
                if ':' not in cls_qname:
                    class_to_onts[cls_qname].append(ontology_name)

            for cls in local_classes:
                cls_name = get_label(g, cls)
                global_all_classes.add(cls_name)
                if cls_name == 'ITSThing':
                    continue
                pattern_literal = g.value(cls, XSD.pattern)
                if pattern_literal and isinstance(pattern_literal, Literal):
                    pattern_name = str(pattern_literal)
                    if pattern_name not in global_patterns:
                        global_patterns[pattern_name] = {"classes": []}
                    global_patterns[pattern_name]["classes"].append((cls_name, ontology_name))
                    ontology_info[ttl_path]["patterns"].add(pattern_name)
                else:
                    ontology_info[ttl_path]["non_pattern_classes"].add(cls_name)
                    class_to_onts[cls_name].append(ontology_name)

            # Process classes for diagrams and Markdown
            for cls in sorted(local_classes, key=lambda u: get_label(g, u).lower()):
                cls_name = get_label(g, cls)
                if cls_name == 'ITSThing':
                    continue
                cls_id = get_id(cls_name)
                log.info("Processing class: %s from %s", cls_name, ttl_path)

                try:
                    # Generate diagram
                    generate_diagram(g, cls, cls_name, cls_id, ns, global_all_classes, abstract_map, ttl_path, errors, prefix_map, ontology_name, ns_to_ontology)

                    # Generate Markdown
                    generate_markdown(g, cls, cls_name, global_patterns, global_all_classes, ns, ttl_path, errors, prefix_map, prop_map, ontology_name, ns_to_ontology, class_to_onts)
                    processed_count += 1

                except Exception as e:
                    error_msg = f"Error processing class {cls_name} from {ttl_path}: {str(e)}\n{traceback.format_exc()}"
                    errors.append(error_msg)
                    log.error(error_msg)

        except Exception as e:
            error_msg = f"Error processing ontology {ttl_path}: {str(e)}\n{traceback.format_exc()}"
            errors.append(error_msg)
            log.error(error_msg)
            continue

    # Update mkdocs.yml navigation
    try:
        update_mkdocs_nav(mkdocs_path, global_patterns, global_all_classes, errors, class_to_onts, ontology_info, ttl_files)
    except Exception as e:
        error_msg = f"Error updating mkdocs.yml: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)

    # Generate index.md
    try:
        generate_index(docs_dir, ttl_files, ontology_info, global_patterns, errors, class_to_onts)
    except Exception as e:
        error_msg = f"Error generating index.md: {str(e)}\n{traceback.format_exc()}"
        errors.append(error_msg)
        log.error(error_msg)

    log.info("Total processed classes: %d", processed_count)
    if errors:
        log.error("Errors occurred:")
        for err in errors:
            log.error(err)

if __name__ == "__main__":
    main()