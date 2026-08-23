# 次に読むべき論文 (Next to Read)

GTE（Li et al., 2023 / arXiv:2308.03281）の設計思想を継承・発展させている後続研究および関連研究を以下に列挙します。

---

## 1. GTE の設計思想を直接継承した言語特化モデル

### [1] Ruri: Japanese General Text Embeddings
- **著者:** Daisuke Tsukagoshi, Masato Mita, Jun Suzuki (Tohoku University / RIKEN AIP)
- **arXiv:** [2409.07737](https://arxiv.org/abs/2409.07737) (2024年9月)
- **関連性:**
  - GTE で提案された **改良対照損失（双方向・4方向）** と **タスク均質バッチ（Task-homogeneous Batching）** を明示的に引用・採用し、日本語汎用テキスト埋め込み（JMTEB SOTA）を構築した代表的研究。

---

## 2. GTE 著者陣（Alibaba Tongyi Lab）による直接の後続研究

### [2] Improving General Text Embedding Model: Tackling Task Conflict and Data Imbalance through Model Merging
- **著者:** Mingxin Li, Zhijie Nie, Yanzhao Zhang, Dingkun Long, Richong Zhang, Pengjun Xie
- **arXiv:** [2410.15035](https://arxiv.org/abs/2410.15035) / NeurIPS 2024 (2024年10月)
- **関連性:**
  - GTE のような一括同時対照学習で生じる「タスク競合（Task Conflict）」や「データ不均衡」を、タスクごとの独立学習＋**モデルマージ（SLERP / Self Positioning）** によって解決した発展研究。

### [3] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models
- **著者:** Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, et al.
- **arXiv:** [2506.05176](https://arxiv.org/abs/2506.05176) (2025年6月)
- **関連性:**
  - GTE の改良対照損失をさらに「適応的マスク $m_{ij}$」付きの5項損失へ拡張し、大規模デコーダベース LLM（0.6B / 4B / 8B）へ発展させた最新フラッグシップモデル。

---

## 3. 直接の比較対象となった基盤モデル

### [4] Text Embeddings by Weakly-Supervised Contrastive Pre-training (E5)
- **著者:** Liang Wang, Nan Yang, Xiaolong Huang, Binyuan Hui, Linjun Li, Fei Huang, Furu Wei
- **arXiv:** [2212.03533](https://arxiv.org/abs/2212.03533) (ACL 2024)
- **関連性:**
  - GTE が非公開データ依存の課題を克服する対象として比較した代表モデル。
