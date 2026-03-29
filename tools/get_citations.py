import argparse
import sys
import json
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError

def get_citations(arxiv_id):
    url = f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}/citations?fields=title,authors,year,abstract"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get('data', [])
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}", file=sys.stderr)
        return None
    except URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        return None
    except json.JSONDecodeError:
        print("Failed to parse JSON response.", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description="Fetch citations for a given arXiv ID using Semantic Scholar API.")
    parser.add_argument("arxiv_id", help="The arXiv ID of the paper (e.g., 2405.00338)")
    parser.add_argument("--format", choices=['json', 'markdown'], default='markdown', help="Output format")
    args = parser.parse_args()

    citations = get_citations(args.arxiv_id)
    if citations is None:
        sys.exit(1)

    if not citations:
        print("No citations found.")
        sys.exit(0)

    if args.format == 'json':
        print(json.dumps(citations, indent=2, ensure_ascii=False))
    else:
        print(f"# Citations for arXiv:{args.arxiv_id}\n")
        from operator import itemgetter
        def extract_year(item):
            cp = item.get('citingPaper', {})
            return cp.get('year') or 0
        
        # Sort by year descending
        sorted_citations = sorted(citations, key=extract_year, reverse=True)
        
        for idx, item in enumerate(sorted_citations, 1):
            paper = item.get('citingPaper', {})
            title = paper.get('title', 'Unknown Title')
            year = paper.get('year', 'Unknown Year')
            authors_list = paper.get('authors', [])
            authors = ", ".join([author.get('name', '') for author in authors_list])
            abstract = paper.get('abstract') or "No abstract available."
            
            print(f"## {idx}. {title} ({year})")
            print(f"**Authors:** {authors}\n")
            print(f"**Abstract:** {abstract}\n")
            print("---")

if __name__ == "__main__":
    main()
