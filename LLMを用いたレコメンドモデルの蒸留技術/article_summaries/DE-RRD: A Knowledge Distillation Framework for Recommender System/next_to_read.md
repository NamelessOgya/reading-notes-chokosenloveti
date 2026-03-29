# 次に読むべき論文 (DE-RRD: A Knowledge Distillation Framework for Recommender System)

※ ウェブ検索等で被引用論文を特定することが困難であったため、ハルシネーション（捏造）を避けるためにルールに従い、本論文と同じ発表時期の同分野の主要な関連論文（Concurrent / Baseline Work）、または後続の類似する推薦システムの知識蒸留研究を「次に読む論文」として列挙しています。

## 1. 知識蒸留（KD）× 推薦システムの関連研究・ベースライン
DE-RRDは推薦システムにおけるKDアプローチとして「ランキング（RRD）」と「Latent知識（DE）」に着目していますが、その周辺の研究です。
- **Ranking Distillation: Learning Compact Ranking Models With High Performance for Recommender System** (RD)
  - POINT: Point-wiseアプローチによる予測結果の知識蒸留の基礎。DE-RRD論文内で比較対象となる代表的ベースライン。
- **Collaborative Distillation for Top-N Recommendation** (CD)
  - POINT: 未観測アイテムに対する順位やソフトラベルを用いた知識蒸留の手法であり、DE-RRDと並ぶ重要な手法。

## 2. 最近のLLMを用いた推薦システムの蒸留技術（発展・別角度）
本トピック（LLMを用いたレコメンドモデルの蒸留技術）に直結する、DE-RRD以降に登場したLLMを利用した知識蒸留アプローチを扱った論文です。
- **RDRec: Rationale Distillation for LLM-based Recommendation**
  - POINT: 大規模言語モデル（LLM）が生成した推薦の「理由（Rationale）」を小さなモデルに蒸留させるというアプローチ。DE-RRDの「Latent Knowledgeの蒸留」を言語モデル由来の表現に変えた別角度からの発展として読める。
- **LLMD4Rec: Mutual Distillation Framework**
  - POINT: 推薦ドメインにおいて教師とLLM間で双方向の蒸留を行う手法。KDのパラダイムをさらに一段引き上げる内容。
