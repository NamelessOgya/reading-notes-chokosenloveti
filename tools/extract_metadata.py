import os
import json
import re

base_dir = "/workspace/LLMを用いたレコメンドモデルの蒸留技術/article_summaries"
output_file = "/workspace/tmp/metadata_extraction.json"

metadata = []

if os.path.exists(base_dir):
    for dname in os.listdir(base_dir):
        dp = os.path.join(base_dir, dname)
        if os.path.isdir(dp):
            summary_path = os.path.join(dp, "summary.md")
            ref_path = os.path.join(dp, "ref_article.md")
            
            paper_info = {
                "directory": dname,
                "title": "",
                "abstract": "",
                "citations": []
            }
            
            if os.path.exists(summary_path):
                with open(summary_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                    m_title = re.search(r'^#\s*(.+)', content, re.MULTILINE)
                    if m_title:
                        paper_info["title"] = m_title.group(1).strip()
                    else:
                        paper_info["title"] = dname
                        
                    m_bg = re.search(r'##\s*背景\n+((?:(?!\n##|\n#).)*)', content, re.DOTALL)
                    if m_bg:
                        bg_text = m_bg.group(1).strip()
                        sentences = re.split(r'(?<=[。\.])\s+', bg_text)
                        paper_info["abstract"] = " ".join(sentences[:3]).strip()
            
            if os.path.exists(ref_path):
                with open(ref_path, "r", encoding="utf-8") as f:
                    refs = f.read()
                    paper_info["citations_raw"] = refs[:1500] 

            metadata.append(paper_info)

os.makedirs("/workspace/tmp", exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

print(f"Extraction complete. Result saved to {output_file}")
