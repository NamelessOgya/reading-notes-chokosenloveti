# 次に読むべき論文 (Next to Read)

**被引用状況に関する注記:**
本論文「Are Large Language Models Really Effective for Training-Free Cold-Start Recommendation? (arXiv:2512.13001)」は発表直後（2025年12月発表）であるため、現在直接的に本論文を引用している後続研究（Cited by）は見つかりませんでした。（Semantic Scholar APIでの検索結果は0件でした。ハルシネーションを防ぐため偽の引用文献は作成していません）。

そのため、代替として本論文の著者らによる「LLMとレコメンド」に関する一連の関連研究（Concurrent Work / Follow-ups）を以下にリストアップします。

## 1. Revisiting Prompt Engineering: A Comprehensive Evaluation for LLM-based Personalized Recommendation
- **arXiv ID:** 2507.13525
- **概要:** 本論文の著者であるGenki Kusano氏らによる先行/同時期の関連研究です。LLMを用いたパーソナライズド・レコメンドにおいて、「どのようなプロンプト設計が推論コストと精度のバランスを取るのに最適か」を、23種類のプロンプトを用いた大規模な評価で検証しています。LLMリランカーの限界や最適なプロンプトデザインに関する知見が詰まっており、本論文でのLLMの弱点を深掘りするのに適しています。

## 2. Are Longer Prompts Always Better? Prompt Selection in Large Language Models for Recommendation Systems
- **arXiv ID:** 2412.14454
- **概要:** 同じくGenki Kusano氏らによる研究。LLMベースのレコメンドシステムにおいて、プロンプトの長さや複雑さと推論性能との関係性を詳細に分析しています。LLMリランカーが入力のコンテキスト長（候補アイテム数や履歴数）にどう影響されるか（本論文のFigure 2やFigure 3などで議論されていた内容）の因果関係をより深く理解するために役立ちます。

## まとめと次の方針
現状、本論文の結論として「LLMリランカーを直接推論させるよりも、LLMが生成した合成データを使って事前学習・ファインチューニングされたTEM（Qwen3-Embedding等）を使うほうが、Cold-Startレコメンデーションにおいては安定して高精度かつ高速である」ことが示されました。

したがって、今後の調査トピックとしては以下のようなアプローチを取っている最新論文を探すことが推奨されます：
1. **TEMのレコメンド能力を向上させるための、より良質なLLM合成データ（Synthetic Data）の生成手法**
2. **アイテムのメタデータやユーザー属性といった「構造化データ」を、TEMのエンコード空間にうまく組み込むためのアーキテクチャ**
3. **Training-Freeだけでなく、少数の履歴でTEMを高速にファインチューニング・適応させる手法**
