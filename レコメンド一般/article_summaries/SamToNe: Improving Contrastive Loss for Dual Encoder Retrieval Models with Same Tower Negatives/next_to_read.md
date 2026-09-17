# 次に読むべき論文 (Next to Read)

SamToNe（Moiseev et al., 2023 / arXiv:2306.02516, ACL 2023『SamToNe: Improving Contrastive Loss for Dual Encoder Retrieval Models with Same Tower Negatives』）に関連する対照学習・Dual Encoder・推薦システム向け重要論文を以下に列挙します。

---

## 1. 密接に関連する先行研究・ベースライン（Related & Baseline Works）

### [1] PAIR: Leveraging Passage Centric Similarity with Pairwise Ranking for Dense Retrieval
- **著者:** Ruiyang Ren, Yingqi Qu, Jing Liu, Wayne Xin Zhao, Qiaoqiao She, Hua Wu, Haifeng Wang, Ji-Rong Wen
- **発表:** ACL 2021
- **arXiv:** [2108.06029](https://arxiv.org/abs/2108.06029)
- **関連性と概要:**
  - SamToNe の直接の先行研究。Passage 同士の類似度ペナルティを対照損失に加えるハイブリッド損失 $\mathcal{L}_{\text{PAIR}} = (1-\alpha)\mathcal{L}_c + \alpha \mathcal{L}_P$ を提案。
  - ハイパーパラメータ $\alpha$ の調整と2段階学習を必要とした PAIR に対し、SamToNe は分母への直接統合によりハイパーパラメータフリー＆単一段階学習を実現した。

### [2] Exploring Dual Encoder Architectures for Question Answering
- **著者:** Zhe Dong, Jianmo Ni, Daniel M. Bikel, Enrique Alfonseca, Yuan Wang, Chen Qu, Imed Zitouni（Google Research）
- **発表:** EMNLP 2022
- **ACL Anthology:** [2022.emnlp-main.640](https://aclanthology.org/2022.emnlp-main.640/)
- **関連性と概要:**
  - 非対称 Dual Encoder（ADE）において最終射影層を共有化する **ADE-SPL (Shared Projection Layer)** を提唱した研究（SamToNe と共通の著者グループ）。
  - SamToNe 論文は、この ADE-SPL を用いてもなお Query 空間と Document 空間が位相的に分離してしまう課題を出発点として開発された。

### [3] Large Dual Encoders Are Generalizable Retrievers (GTR)
- **著者:** Jianmo Ni, Chen Qu, Luheng He, Daiyi Peng, Ni Lao, et al.（Google Research）
- **発表:** EMNLP 2022
- **arXiv:** [2112.07899](https://arxiv.org/abs/2112.07899)
- **関連性と概要:**
  - T5 をバックボーンとし、数十億パラメータ規模へスケールさせた Dual Encoder の最高峰。SamToNe の実験アーキテクチャ（T5 エンコーダ ＋ Mean Pooling ＋ 射影層）の基盤となったモデル。

---

## 2. 対照学習の幾何構造・推薦システムへの応用研究（Theory & Applications）

### [4] Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere
- **著者:** Tongzhou Wang, Phillip Isola（MIT）
- **発表:** ICML 2020
- **arXiv:** [2005.10242](https://arxiv.org/abs/2005.10242)
- **関連性と概要:**
  - 対照学習が満たすべき2つの幾何学的性質「**Alignment（正例ペアの近接性）**」と「**Uniformity（空間上での均一分散性）**」を理論的に証明した金字塔的論文。
  - SamToNe が Query 同士の同一タワー負例によって表現空間の縮退を防ぎ、Query と Document の完全なアライメントを実現するメカニズムを幾何学的に理解する上で不可欠な基礎理論。

### [5] Correcting the LogQ Correction: Revisiting Sampled Softmax for Large-Scale Retrieval
- **著者:** Google Research / レコメンド・検索チーム
- **arXiv:** [2408.06992](https://arxiv.org/abs/2408.06992)
- **関連性と概要:**
  - 2-Tower 型の大規模レコメンド・検索において、Sampled Softmax Loss のサンプリングバイアス補正（LogQ 補正）の数理的欠陥を暴き、幾何学的により正確な補正手法を提唱した研究。
  - 本リポジトリ内にまとめあり: [Correcting the LogQ Correction 要約](file:///Users/masashiueno/業界まとめ文書/レコメンド一般/article_summaries/Correcting%20the%20LogQ%20Correction:%20Revisiting%20Sampled%20Softmax%20for%20Large-Scale%20Retrieval/summary.md)

### [6] RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering
- **著者:** Yingqi Qu, Yuchen Ding, Jing Liu, et al.（Baidu）
- **発表:** NAACL 2021
- **arXiv:** [2010.08191](https://arxiv.org/abs/2010.08191)
- **関連性と概要:**
  - クロスバッチ負例（Cross-batch negatives）とクロスエンコーダ蒸留を導入し、Dual Encoder の負例サンプリング効率を極限まで高めた代表的研究。
  - 本リポジトリ内にまとめあり: [RocketQA 要約](file:///Users/masashiueno/業界まとめ文書/レコメンド一般/article_summaries/RocketQA:%20An%20Optimized%20Training%20Approach%20to%20Dense%20Passage%20Retrieval%20for%20Open-Domain%20Question%20Answering/summary.md)

### [7] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models
- **著者:** Yanzhao Zhang, Mingxin Li, Dingkun Long, et al.（Alibaba）
- **発表:** 2025年6月
- **arXiv:** [2506.05176](https://arxiv.org/abs/2506.05176)
- **関連性と概要:**
  - SamToNe の「同一タワー（クエリ同士・文書同士）の反発」をハード負例と単一分母に包括統合し、動的マスク $m_{ij}$ による偽陰性除外を導入した改良型 InfoNCE を提案。
  - 本リポジトリ内にまとめあり: [Qwen3 Embedding 要約](file:///Users/masashiueno/業界まとめ文書/LLM埋め込み表現/article_summaries/Qwen3%20Embedding:%20Advancing%20Text%20Embedding%20and%20Reranking%20Through%20Foundation%20Models/summary.md)

