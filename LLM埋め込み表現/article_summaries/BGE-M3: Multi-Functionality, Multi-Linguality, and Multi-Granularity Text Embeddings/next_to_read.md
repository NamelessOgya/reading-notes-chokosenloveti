# 次に読むべき論文 (Next to Read)

BGE-M3（Chen et al., 2024 / arXiv:2402.03216）に関連する、最新の多言語埋め込み・ハイブリッド検索・長文検索モデルを以下に列挙します。

---

## 1. BGE シリーズおよび競合多言語埋め込みモデル

### [1] Multilingual E5 Text Embeddings: A Technical Report
- **著者:** Xianian Li, Ping Wang, Chenghao Fan, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Fei Huang, Ji-Rong Wen
- **arXiv:** [2402.05672](https://arxiv.org/abs/2402.05672) (2024年2月)
- **関連性:**
  - 同時期に公開され、MIRACL や多言語検索ベンチマークで BGE-M3 と双璧をなす最重要ベースライン。

### [2] jina-embeddings-v3: Multilingual Embeddings with Task LoRA
- **著者:** Saba Sturua, Isabelle Mohr, Michael Günther, Han Xiao et al.
- **arXiv:** [2409.10173](https://arxiv.org/abs/2409.10173) (2024年9月)
- **関連性:**
  - BGE-M3 が「3つの検索様式を同時出力」するアプローチをとったのに対し、Jina v3 は「Task LoRA」でタスクごとに最適な表現を切り替えるアプローチを採用したライバルモデル。

---

## 2. 後続の大規模 LLM 埋め込みモデル

### [3] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models
- **著者:** Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, et al.
- **arXiv:** [2506.05176](https://arxiv.org/abs/2506.05176) (2025年6月)
- **関連性:**
  - BGE-M3 などの多言語ベンチマーク（MIRACL, MLDR, MTEB）をさらに更新した最新のフラッグシップモデル。

### [4] NV-Embed-v2: Improved Techniques for Training LLMs as Generalist Embedding Models
- **著者:** Chankyu Lee, Rajarshi Roy, Mengyao Xu, et al. (NVIDIA)
- **arXiv:** [2409.07439](https://arxiv.org/abs/2409.07439) (2024年9月)
- **関連性:**
  - MTEB で最高峰のスコアを達成した LLM ベースの埋め込みモデル。
