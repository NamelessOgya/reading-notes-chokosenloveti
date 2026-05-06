# 次に読むべき論文 (Next to Read)

本論文（"How to Index Item IDs for Recommendation Foundation Models", 2023）は、LLMを用いた生成的レコメンドにおける「アイテムIDの付与方法（Indexing）」という基礎的かつ重要な課題を体系化した先駆的な研究です。
この手法（SID, CID, SemID等）を発展させたり、より深く体系化している後続研究として以下の論文を推奨します。

## 1. A Survey of Item Identifiers in Generative Recommendation: Construction, Alignment, and Generation
- **概要**: Generative Recommender Systems (Gen-RecSys) における「アイテムID（Item Identifiers）」に関する包括的なサーベイ論文です。
- **読むべき理由**: 本論文が提案したSID, CID, SemIDなどのインデックス手法をさらに「構築 (Construction)」「アラインメント (Alignment)」「生成 (Generation)」の3つのライフサイクルに分類し、VQ（Vector Quantization）やRQ、PQといったコードブックベースの量子化手法などの最新のID構築技術まで網羅しています。本論文の発展的な位置づけを把握するのに最適です。

## 2. DIGER: Differentiable Semantic ID for Generative Recommendation
- **概要**: 意味的ID（Semantic ID）を微分可能な（Differentiable）形で学習し、生成モデルにおけるレコメンド性能を向上させる手法（DIGER）を提案した論文です。
- **読むべき理由**: 本論文のSemID（カテゴリベースの意味的インデックス）はヒューリスティックに構築されたものでしたが、DIGERはそれをエンドツーエンドで学習可能な形に昇華させており、インデックス手法をよりモデルと密結合させて最適化するという別のアプローチ（発展形）を提示しています。
