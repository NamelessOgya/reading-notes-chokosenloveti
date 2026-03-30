これから以下の調査を依頼します。

# 論文名
Bidirectional Knowledge Distillation for Enhancing Sequential Recommendation with Large Language Models

# 調査トピック
グラフを用いたレコメンド

# 対応事項  
1. 対象論文のWeb検索を行い **arXiv ID** を特定した上で、汎用ツール `./tools/extract_arxiv.sh <arXiv_ID> "{論文名}"` を実行しなさい。これにより、論文ソースのダウンロード、PDF図版の高品質画像変換、そして参照リスト(`ref_article.md`)とテーブル構造(`tables_source.md`)の抽出までを自動で完了させなさい。
2. ダウンロードされたソースファイル (`.tex`) や、ツールで出力された `tables_source.md` 等の解析結果を用いて、`./summary_format.md` に従って `{調査トピック}/article_summaries/{論文名}/` 配下に要約(`summary.md`)を作成しなさい。  
3. 対象論文を引用している（Cited by）論文を検索し、対象論文の手法を発展させているもの、または違う角度からアプローチしているものを探し、次に読む論文として `{調査トピック}/article_summaries/{論文名}/next_to_read.md` に列挙しなさい。
   ※注意: 発表直後などの理由で「対象論文を引用している後続論文」が存在しない場合は、対象論文のReference（引用元）を被引用論文だと偽る捏造（ハルシネーション）を絶対に避けてください。その場合は「被引用がない」旨を記載し、代替案として「同じ発表時期の同分野の最新関連論文（Concurrent Work）」を検索して列挙しなさい。
4. 今回の作業にあたり、再利用可能なcodeがあれば`./tools`に加えなさい。必要においじて`requirements.txt`への加筆も行いなさい。

# 注意事項
- 一時ファイルの保存などが必要になる場合は`./tmp`配下に保存しなさい。
- `Reflection.md`にはこれまでに起きた失敗と対策方法が記載されています。同じミスがないように必ず守りなさい。
- スクリプトの実行などでPython環境が必要な場合は、ローカル環境を汚さないように必ずDockerコンテナ（`docker compose run --rm python bash`）内で作業しなさい。