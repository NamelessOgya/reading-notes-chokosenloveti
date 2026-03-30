import argparse
import os
import re

def parse_bbl(bbl_path, out_file):
    if not bbl_path or not os.path.exists(bbl_path):
        print(f"Warning: bbl_path {bbl_path} does not exist or empty.")
        return
    
    with open(bbl_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Splitting based on \bibitem. 
    # Usually bibitems start with \bibitem[{author(year) etc}]{key} or just \bibitem{key}
    # Use tighter regex to avoid greedy matches over newlines where not intended, but allow space or % between ] and {
    items = re.split(r'\\bibitem(?:\[[^\]]*\])?(?:%?\s*)*\{[^\}]*\}', content)
    ref_list = []
    
    # items[0] is typically the preamble \begin{thebibliography}
    for item in items[1:]:
        text = str(item)
        # Remove common LaTeX formatting markers
        text = re.sub(r'\\newblock', '', text)
        text = re.sub(r'\\emph\{(.*?)\}', r'*\1*', text)
        text = text.replace('\n', ' ').replace('\\', '')
        # Delete end block
        text = re.sub(r'end\{thebibliography\}.*', '', text)
        
        # Squeeze whitespace
        text = " ".join(text.split())
        if text:
            ref_list.append(text)
            
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write("# 参考文献一覧\n\n")
        f.write("※ 本自動抽出は正規表現による簡易版です。一部LaTex特殊文字が残る場合があります。\n\n")
        for i, ref in enumerate(ref_list, 1):
            f.write(f"{i}. {ref}\n")
    print(f"Saved {len(ref_list)} references to {out_file}")

def extract_tables(tex_path, out_file):
    if not os.path.exists(tex_path):
        print(f"Warning: {tex_path} does not exist.")
        return
    
    tex_dir = os.path.dirname(tex_path)
    all_tex_files = [os.path.join(tex_dir, f) for f in os.listdir(tex_dir) if f.endswith('.tex')]
    
    content = ""
    for file in all_tex_files:
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                content += f.read() + "\n"
        except Exception as e:
            print(f"Warning: Failed to read {file}: {e}")
        
    tables = re.findall(r'\\begin\{table\*?\}.*?\\end\{table\*?\}', content, flags=re.DOTALL)
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write("# 抽出されたLaTeXテーブル\n\n")
        f.write("以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。\n\n")
        for i, table in enumerate(tables, 1):
            f.write(f"## Table {i}\n")
            f.write("```latex\n")
            f.write(table.strip())
            f.write("\n```\n\n")
            
    print(f"Extracted {len(tables)} tables to {out_file}")

def main():
    parser = argparse.ArgumentParser(description="Parse ArXiv LaTeX and BBL files")
    parser.add_argument("--tex", type=str, required=True, help="Path to main .tex file")
    parser.add_argument("--bbl", type=str, default="", help="Path to .bbl file")
    parser.add_argument("--outdir", type=str, required=True, help="Output directory")
    
    args = parser.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    
    ref_out = os.path.join(args.outdir, "ref_article.md")
    parse_bbl(args.bbl, ref_out)
    
    tables_out = os.path.join(args.outdir, "tables_source.md")
    extract_tables(args.tex, tables_out)

if __name__ == "__main__":
    main()
