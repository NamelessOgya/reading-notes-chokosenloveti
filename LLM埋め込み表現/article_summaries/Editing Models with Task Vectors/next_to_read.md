# 次に読むべき論文 (Next to Read)

Task Vectors（Ilharco et al., ICLR 2023 / arXiv:2212.04089）の理論を発展させた代表的な後続研究およびモデルマージの重要文献を以下に列挙します。

---

## 1. タスクベクトルの干渉・衝突を解決した直系の後続研究

### [1] Resolving Interference When Merging Models (TIES-Merging)
- **著者:** Prateek Yadav, Derek Tam, Leshem Choshen, Colin Raffel, Mohit Bansal
- **arXiv:** [2306.01708](https://arxiv.org/abs/2306.01708) (NeurIPS 2023)
- **関連性:**
  - 本研究のタスクベクトル加算における「パラメータ符号衝突」と「干渉」を、Trimming & Sign Election により劇的に解消した代表的手法。

### [2] Language Models are Super Mario: Absorbing Abilities from Homologous Models from a Parameter Perspective (DARE)
- **著者:** Le Yu, Bowen Yu, Haiyang Yu, Fei Huang, Yongbin Li
- **arXiv:** [2311.03099](https://arxiv.org/abs/2311.03099) (ICLR 2024)
- **関連性:**
  - タスクベクトルの微小なパラメータの最大99%をランダムドロップしても性能が維持されることを示し、モデルマージの疎性を極限まで高めた研究。

---

## 2. 埋め込みモデルへの応用研究

### [3] Improving General Text Embedding Model: Tackling Task Conflict and Data Imbalance through Model Merging
- **著者:** Mingxin Li, Zhijie Nie, Yanzhao Zhang, Dingkun Long, Richong Zhang, Pengjun Xie
- **arXiv:** [2410.15035](https://arxiv.org/abs/2410.15035) (NeurIPS 2024)
- **関連性:**
  - 本研究のタスクベクトル理論をテキスト埋め込みモデルに適用し、タスク競合（Task Conflict）とデータ不均衡を SLERP / Self Positioning で解決。

### [4] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models
- **著者:** Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, et al.
- **arXiv:** [2506.05176](https://arxiv.org/abs/2506.05176) (2025年6月)
- **関連性:**
  - タスクベクトルのモデルマージをステージ3の重要パイプラインとして採用した最新の大規模埋め込みモデル。
