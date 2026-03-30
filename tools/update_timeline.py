import csv

input_csv = "/workspace/tmp/timeline_base.csv"
output_csv = "/workspace/LLMを用いたレコメンドモデルの蒸留技術/timeline.csv"

# Updated data
updates = {
    "Topology Distillation for Recommender System": {"提案モデル": "Topology Distillation (TD)", "発表年": "2021", "発表場所": "KDD"},
    "On-Device Large Language Models for Sequential Recommendation": {"提案モデル": "On-Device LLM Distillation", "発表年": "2024", "発表場所": "arXiv"},
    "Distillation Matters: Empowering Sequential Recommenders to Match the Performance of Large Language Model": {"提案モデル": "LLM2Seq Distillation", "発表年": "2024", "発表場所": "arXiv"},
    "LLMD4Rec: Mutual Distillation Framework": {"提案モデル": "LLMD4Rec", "発表年": "2024", "発表場所": "WWW"},
    "DE-RRD: A Knowledge Distillation Framework for Recommender System": {"提案モデル": "DE-RRD", "発表年": "2020", "発表場所": "CIKM"},
    "RDRec: Rationale Distillation for LLM-based Recommendation": {"提案モデル": "RDRec", "発表年": "2024", "発表場所": "WSDM"},
    "Collaborative Distillation for Top-N Recommendation": {"提案モデル": "Collaborative Distillation (CD)", "発表年": "2020", "発表場所": "KDD"},
    "Unbiased Knowledge Distillation for Recommendation": {"提案モデル": "Unbiased KD", "発表年": "2023", "発表場所": "WSDM"},
    "Active Large Language Model-based Knowledge Distillation for Session-based Recommendation": {"提案モデル": "Active-LLM KD", "発表年": "2024", "発表場所": "WWW"},
    "SLMRec: Distilling Large Language Models into Small for Sequential Recommendation": {"提案モデル": "SLMRec", "発表年": "2024", "発表場所": "SIGIR"},
    "Bidirectional Knowledge Distillation for Enhancing Sequential Recommendation with Large Language Models (LLMD4Rec)": {"提案モデル": "LLMD4Rec (Bidirectional)", "発表年": "2024", "発表場所": "WWW"},
    "Ranking Distillation: Learning Compact Ranking Models With High Performance for Recommender System": {"提案モデル": "Ranking Distillation (RD)", "発表年": "2018", "発表場所": "KDD"}
}

with open(input_csv, "r", encoding="utf-8") as fin, open(output_csv, "w", encoding="utf-8", newline="") as fout:
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    # Sort out duplicate LLMD4Rec if necessary or just write it.
    rows = []
    for row in reader:
        title = row["論文名"]
        for key, val in updates.items():
            if key in title or title in key:
                row["提案モデル"] = val["提案モデル"]
                row["発表年"] = val["発表年"]
                row["発表場所"] = val["発表場所"]
                break
        rows.append(row)
        
    # Sort rows by Year
    rows.sort(key=lambda x: int(x["発表年"]) if x["発表年"].isdigit() else 2099)
    for row in rows:
        writer.writerow(row)

print("Timeline updated successfully.")
