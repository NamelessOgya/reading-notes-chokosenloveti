import os
import json
import csv
import re

base_dir = "/workspace/LLMを用いたレコメンドモデルの蒸留技術/article_summaries"
output_csv = "/workspace/tmp/timeline_base.csv"
output_json = "/workspace/tmp/citation_network.json"

metadata_list = []
nodes = []
edges = []

if not os.path.exists(base_dir):
    print(f"Directory {base_dir} does not exist. Run from docker with correct volume mount.")
    exit(1)

dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

for dname in dirs:
    dp = os.path.join(base_dir, dname)
    summary_path = os.path.join(dp, "summary.md")
    ref_path = os.path.join(dp, "ref_article.md")
    
    title = dname
    abstract = ""
    
    if os.path.exists(summary_path):
        with open(summary_path, "r", encoding="utf-8") as f:
            content = f.read()
            m_title = re.search(r'^#\s*(.+)', content, re.MULTILINE)
            if m_title:
                title_match = m_title.group(1).strip()
                if len(title_match) > 3:
                     title = title_match
            
            m_bg = re.search(r'##\s*背景\n+((?:(?!\n##|\n#).)*)', content, re.DOTALL)
            if m_bg:
                bg_text = m_bg.group(1).strip()
                # Remove markdown links, formatting to get plain abstract
                bg_text = re.sub(r'\*\*(.*?)\*\*', r'\1', bg_text)
                sentences = re.split(r'(?<=[。\.])\s+', bg_text)
                abstract = " ".join(sentences[:2]).strip()
                abstract = abstract.replace('\n', ' ')

    nodes.append({
        "id": dname,
        "label": title
    })
    
    metadata_list.append({
        "論文名": title,
        "dir_name": dname,
        "提案モデル": "",
        "発表年": "",
        "発表場所": "",
        "概要": abstract,
        "リンク": f"./LLMを用いたレコメンドモデルの蒸留技術/article_summaries/{dname}/summary.md"
    })

# Pass 2: find cross-citations
for dname in dirs:
    dp = os.path.join(base_dir, dname)
    ref_path = os.path.join(dp, "ref_article.md")
    
    if os.path.exists(ref_path):
        with open(ref_path, "r", encoding="utf-8") as f:
            refs = f.read().lower()
            
            for target_dname in dirs:
                if dname == target_dname:
                    continue
                # Try simple string match against the target's lowercase title or directory name
                # Clean up title for searching
                target_title = next((n['label'] for n in nodes if n['id'] == target_dname), target_dname).lower()
                target_title_clean = re.sub(r'[^a-z0-9]', '', target_title)
                
                # Check directly, or strip non alpha-numeric
                if target_title in refs or target_dname.lower() in refs:
                     edges.append({
                         "source": target_dname, # Reference is older, so target_dname -> dname
                         "target": dname
                     })
                else:
                    # Heuristic fallback: check if clean title chars match a cleaned line in refs
                    ref_lines = refs.split('\n')
                    for line in ref_lines:
                        clean_line = re.sub(r'[^a-z0-9]', '', line)
                        if len(target_title_clean) > 10 and target_title_clean in clean_line:
                            edges.append({
                                 "source": target_dname,
                                 "target": dname
                            })
                            break

os.makedirs("/workspace/tmp", exist_ok=True)

# Write JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump({"nodes": nodes, "edges": edges}, f, ensure_ascii=False, indent=2)

# Write CSV
with open(output_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["論文名", "提案モデル", "発表年", "発表場所", "概要", "リンク"])
    writer.writeheader()
    for row in metadata_list:
        del row["dir_name"]
        writer.writerow(row)

print(f"Extraction complete. Found {len(nodes)} nodes and {len(edges)} edges.")
