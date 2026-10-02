# 次に読むべき論文 (Next to Read)

jina-embeddings-v3（Sturua et al., EMNLP 2024 / arXiv:2409.10173）に関連する、最新の多言語・マルチタスク埋め込みモデルおよび関連研究を以下に列挙します。

---

## 1. 直接の比較対象となった最先端多言語モデル

### [1] BGE-M3: Multi-Functionality, Multi-Linguality, and Multi-Granularity Text Embeddings
- **著者:** Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu (BAAI)
- **arXiv:** [2402.03216](https://arxiv.org/abs/2402.03216) (2024年2月)
- **関連性:**
  - 多言語・長文（8,192長）対応の代表的ライバルモデル。密・疎・マルチベクトルのハイブリッド表現アプローチ。

### [2] Multilingual E5 Text Embeddings: A Technical Report
- **著者:** Xianian Li, Ping Wang, Chenghao Fan, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Fei Huang, Ji-Rong Wen
- **arXiv:** [2402.05672](https://arxiv.org/abs/2402.05672) (2024年2月)
- **関連性:**
  - 指示文チューニング（Instruct）を採用した代表的多言語モデルであり、本論文が Task LoRA との比較対象とした最重要ベースライン。

---

## 2. MoE / アダプタベースの効率的埋め込みモデル

### [3] Training Sparse Mixture of Experts Text Embedding Models (Nomic Embed v2)
- **著者:** Zach Nussbaum, Brandon Duderstadt (Nomic AI)
- **arXiv:** [2502.07972](https://arxiv.org/abs/2502.07972) (2025年2月)
- **関連性:**
  - Jina v3 が「Task LoRA」でタスク特化を達成したのに対し、Nomic v2 は「Sparse MoE（ルーターによる動的エキスパート選択）」で効率化と表現力向上を達成した対照的な最先端手法。

### [4] NV-Embed-v2: Improved Techniques for Training LLMs as Generalist Embedding Models
- **著者:** Chankyu Lee, Rajarshi Roy, Mengyao Xu, et al. (NVIDIA)
- **arXiv:** [2409.07439](https://arxiv.org/abs/2409.07439) (2024年9月)
- **関連性:**
  - デコーダ LLM をベースに Latent Attention と LoRA を駆使して MTEB 世界 1 位を獲得したフラッグシップモデル。
