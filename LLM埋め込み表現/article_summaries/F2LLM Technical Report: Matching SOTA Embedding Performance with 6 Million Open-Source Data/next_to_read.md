# 次に読むべき論文 (Next to Read)

F2LLM（Zhang et al., 2025 / arXiv:2510.02294）を引用している後続研究（Cited by）および関連する最新の LLM 埋め込み表現・モデル改良研究を以下に列挙します。

---

## 1. F2LLM を直接引用・発展させた後続研究（Cited by）

### [1] F2LLM-v2: Inclusive, Performant, and Efficient Embeddings for a Multilingual World
- **著者:** Ziyin Zhang, Zihan Liao, Han Yu, Peng Di, Rui Wang（Ant Group / Shanghai Jiao Tong University）
- **arXiv:** [2603.19223](https://arxiv.org/abs/2603.19223) (2026年3月)
- **関連性と概要:**
  - **F2LLM の直接の第2世代モデル**。80M から 14B まで 8 段階のサイズバリエーションを展開し、200 以上の言語をサポート。
  - 新たにキュレーションした 6,000 万件（60M）のオープンソースデータで学習。
  - 2段階学習パイプラインに加え、**Matryoshka Representation Learning（MRL）、モデルプルーニング（枝刈り）、知識蒸留（Knowledge Distillation）** を統合し、大幅な軽量・高速化と MTEB 11 ベンチマークでの首位獲得を両立。

### [2] C2LLM Technical Report: A New Frontier in Code Retrieval via Adaptive Cross-Attention Pooling
- **著者:** Jin Qin, Zihan Liao, Ziyin Zhang, Hang Yu, Peng Di, Rui Wang（Ant Group / Shanghai Jiao Tong University）
- **arXiv:** [2512.21332](https://arxiv.org/abs/2512.21332) (2025年12月)
- **関連性と概要:**
  - F2LLM と同一の研究チームによる、**コード検索（Code Retrieval）特化型の LLM 埋め込みモデル**（0.5B, 7B）。
  - Qwen-2.5-Coder をバックボーンとし、EOS トークン依存の情報ボトルネックを打破する **PMA（Pooling by Multihead Attention）** モジュールを導入。MTEB-Code において 7B モデルが世界 1 位を達成。

### [3] BROTHER: Behavioral Recognition Optimized Through Heterogeneous Ensemble Regularization for Ambivalence and Hesitancy
- **著者:** Alexandre Pereira, Bruno Fernandes, Pablo V. A. Barros
- **arXiv:** [2603.14361](https://arxiv.org/abs/2603.14361) (2026年3月)
- **関連性と概要:**
  - F2LLM をテキスト特徴抽出器（Text Modality Encoder）として動画・音声・言語のマルチモーダル情動認識パイプラインに組み込んだ応用研究。

---

## 2. 非合成データ重視・同系列の重要関連研究（Related & Baseline Works）

### [4] LGAI-Embedding: Towards High-Performance Text Embedding Without Synthetic Data
- **著者:** LG AI Research
- **発表:** 2025年
- **関連性と概要:**
  - 高コストな合成データを用いず、綿密にキュレーションされたオープンソースデータのみで MTEB 上位 SOTA を達成し、F2LLM の設計思想に直接の影響を与えた研究。

### [5] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models
- **著者:** Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, et al.
- **arXiv:** [2506.05176](https://arxiv.org/abs/2506.05176) (2025年6月)
- **関連性と概要:**
  - F2LLM のバックボーン LLM であり、ハード負例マイニング用のエンコーダー（0.6B）としても活用されている Qwen3 基盤の強力な埋め込みモデル。
