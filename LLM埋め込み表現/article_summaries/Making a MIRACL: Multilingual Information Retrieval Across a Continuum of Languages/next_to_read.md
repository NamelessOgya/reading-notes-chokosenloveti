# 次に読むべき論文 (Next to Read)

MIRACL データセット（Zhang et al., TACL 2023 / arXiv:2210.09984）を利用・発展させた後続の代表的多言語埋め込み・検索モデル、および関連研究を以下に列挙します。

---

## 1. MIRACL を主要ベンチマークとして飛躍させた多言語埋め込みモデル

### [1] Multilingual E5 Text Embeddings: A Technical Report
- **著者:** Xianian Li, Ping Wang, Chenghao Fan, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Fei Huang, Ji-Rong Wen (Tongyi Lab, Alibaba Group / Renmin University of China)
- **arXiv:** [2402.05672](https://arxiv.org/abs/2402.05672) (2024年2月)
- **関連性:**
  - MIRACL を多言語検索の標準ベンチマークとして採用し、弱教師あり多言語対照事前学習 + 教師あり Fine-tuning により、MIRACL の平均 nDCG@10 をベースライン（0.415）から **0.65+** へと大幅に更新した代表的モデル。

### [2] BGE-M3: Multi-Functionality, Multi-Linguality, and Multi-Granularity Text Embeddings
- **著者:** Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu (BAAI)
- **arXiv:** [2402.03216](https://arxiv.org/abs/2402.03216) (2024年2月)
- **関連性:**
  - MIRACL の多言語検索タスクにおいて、密検索（Dense）・疎検索（Sparse/Lexical）・マルチベクトル（Multi-vector/ColBERT）を単一モデルで統合し、MIRACL 含む多言語ベンチマークで最高峰の精度を実証。

### [3] Ruri: Japanese General Text Embeddings
- **著者:** Daisuke Tsukagoshi, Masato Mita, Jun Suzuki (Tohoku University / RIKEN AIP)
- **arXiv:** [2409.07737](https://arxiv.org/abs/2409.07737) (2024年9月)
- **関連性:**
  - 日本語におけるリランキング・密検索の主要評価セットとして MIRACL (Japanese) を採用。

---

## 2. MIRACL の前身となった基盤データセット

### [4] Mr. TyDi: A Multi-lingual Benchmark for Dense Retrieval
- **著者:** Xinyu Zhang, Odunayo Ogundepo, Ehsan Kamalloo, Ramy Eskander, Noah A. Smith, Jimmy Lin
- **arXiv:** [2108.08787](https://arxiv.org/abs/2108.08787) (2021年8月)
- **関連性:**
  - MIRACL の直接の前身となった 11 言語の多言語密検索ベンチマーク。
  - TyDi QA からの変換方式と、MIRACL で行われた高品質化・高密度化アノテーションの差分を理解する上で重要。
