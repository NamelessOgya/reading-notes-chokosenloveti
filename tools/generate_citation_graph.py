import json
import csv
import argparse
import os
import textwrap
import subprocess

def create_citation_graph(data_file, output_path, timeline_csv):
    # Load JSON
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Load Timeline to get Years
    years = {}
    if os.path.exists(timeline_csv):
        with open(timeline_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row["論文名"].strip()
                match_id = None
                for n in data.get('nodes', []):
                    if title in n['id'] or n['id'] in title:
                        match_id = n['id']
                        break
                if match_id:
                    try:
                        years[match_id] = int(row["発表年"])
                    except ValueError:
                        years[match_id] = 2024
    
    nodes = data.get('nodes', [])
    edges = data.get('edges', [])

    dot_lines = [
        'digraph CitationTree {',
        '    rankdir=BT;',       # Bottom to Top
        '    splines=true;',     # Curved edges
        '    nodesep=0.7;',      # Horizontal spacing
        '    ranksep=1.2;',      # Vertical spacing
    ]

    # 1. Paper Nodes
    dot_lines.append('    // Paper Nodes')
    dot_lines.append('    node [shape=box, style="filled,rounded", fillcolor="#E3F2FD", fontcolor=black, fontname="Helvetica", fontsize=10, margin=0.2];')
    dot_lines.append('    edge [color="#757575", penwidth=1.5, arrowhead=normal, arrowsize=0.8, style=solid];')

    for node in nodes:
        node_id = node['id']
        year = years.get(node_id, 2024)
        
        # Colors based on era for visual aid, even if not forced geometrically
        color = "#E3F2FD"
        if year <= 2020: color = "#FFF9C4"
        elif year <= 2022: color = "#E8F5E9"
        elif year == 2023: color = "#F3E5F5"
        elif year >= 2024: color = "#E3F2FD"

        safe_id = f'"{node_id}"'
        label_text = textwrap.fill(node_id, width=22).replace('\n', '\\n')
        full_label = f"[{year}]\\n{label_text}"
        dot_lines.append(f'    {safe_id} [label="{full_label}", fillcolor="{color}"];')

    # 2. Citation Edges
    dot_lines.append('    // Citation Edges')
    for edge in edges:
        source = f'"{edge["source"]}"'
        target = f'"{edge["target"]}"'
        dot_lines.append(f'    {source} -> {target};')

    dot_lines.append('}')
    
    # Write dot file
    dot_path = "/workspace/tmp/citation_tree.dot"
    os.makedirs(os.path.dirname(dot_path), exist_ok=True)
    with open(dot_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(dot_lines))
        
    print(f"Graphviz DOT file written to {dot_path}")

    # Render
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        subprocess.run(["dot", "-Tpng", dot_path, "-o", output_path], check=True)
        print(f"Graph safely rendered to {output_path} via Graphviz topological sorting")
    except Exception as e:
        print(f"Failed to run 'dot' command: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate citation network graph using Graphviz purely based on topology")
    parser.add_argument("--data", required=True, help="Path to JSON file containing nodes and edges")
    parser.add_argument("--output", required=True, help="Path to output PNG image")
    parser.add_argument("--timeline", required=True, help="Path to timeline CSV file for chronological ordering")
    args = parser.parse_args()
    create_citation_graph(args.data, args.output, args.timeline)
