# reading-notes-chokosenloveti  
`chokosenloveti`のための論文まとめです。  

## 推奨環境・拡張機能（VSCode等）
本リポジトリでは、引用関係の歴史的な系譜やネットワーク図などを表現するために **Mermaid.js**（ ````mermaid ```` 記法）を標準採用しています。
VSCodeをはじめとするローカルエディタのプレビュー画面でこれらのグラフを視覚的にレンダリングするためには、以下の拡張機能が必要です。

- **[Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)**
  （※ インストールするだけで、標準のMarkdownプレビュータブにグラフがシームレスに描画されます。なお、GitHubのWeb画面上では拡張機能なしで標準サポート・自動描画されます。）

## ディレクトリ構成ルール

各論文のまとめる際は、以下のように `article_summaries` 以下に論文名のディレクトリを作成し、アセットを管理してください。

- `{調査トピック}/article_summaries/{論文名}/` : 各論文のルートディレクトリ
  - `images/`: 論文まとめに際して必要な画像などを置く場所
  - `pdf/`: 論文のPDFそのものを置く場所
  - `{論文名}.md`: 論文のまとめ本体（背景・手法・結果などを記述）
  - `ref_article.md`: 論文が引用している論文名を列挙するファイル
  - `next_to_read.md`: 次に読むべき論文名を列挙するファイル

## 人間が実行する際の実行方法  
以下のテンプレートファイルの内容を、CopilotやCoding-Agent (antigravityなど) にプロンプトとして与え、自律的なまとめ作業を依頼します。

- **論文単体をまとめる**: `prompt_templete/summary_article.md` を使用
- **領域（トピック）全体をまとめる**: `prompt_templete/summary_topic.md` を使用

## 開発環境 (Docker)

作業の過程でPythonなどの実行環境が必要になる場合は、ローカル環境を汚さないためにDockerコンテナ内で作業を行ってください。
以下のコマンドで、カレントディレクトリがマウントされた軽量なPythonコンテナを起動できます。

```bash
docker compose run --rm python bash
```

## ツールの使い方

論文調査を効率化するための各種スクリプトが `tools/` 以下に用意されています。

### 1. 論文リソースの自動ダウンロード＆抽出 (`extract_arxiv.sh`)

特定の arXiv 論文のPDFやLaTeXソースをダウンロードし、PDF内の画像をPNGに変換、さらに LaTeX からテーブルと参考文献リストを抽出して Markdown に変換します。このスクリプトは抽出時に自動で Docker コンテナを利用します。

```bash
./tools/extract_arxiv.sh <arxiv_id> "<論文名（生成先のディレクトリ名）>"
```

**実行例:**
```bash
./tools/extract_arxiv.sh 2502.15685 "Active Large Language Model-based Knowledge Distillation"
```
※ 完了すると、`{調査トピック}/article_summaries/{論文名}/` 以下に `images/` ファイルや `tables_source.md` などの必要なファイル一式が配置されます。

### 2. 被引用論文（Citations）の取得 (`get_citations.py`)

Semantic Scholar API を利用して、指定した論文を引用している後続研究（被引用論文）の一覧を取得します。

実行には Python 環境が必要なため、Docker コンテナを経由して実行することを推奨します。

```bash
# 標準出力に Markdown 形式で出力されます。適宜ファイルにリダイレクトしてください。
docker compose run --rm python python tools/get_citations.py <arxiv_id> > citations.md
```

**実行例:**
```bash
docker compose run --rm python python tools/get_citations.py 2405.00338 > citations.md
```
