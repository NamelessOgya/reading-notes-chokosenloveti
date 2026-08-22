# 次に読むべき論文 (Next to Read)

本論文（Li et al., NeurIPS 2024 / arXiv:2410.15035）の手法を発展させている後続研究、直接の理論基盤、およびモデルマージ技術を活用した関連研究を以下に列挙します。

---

## 1. 著者陣による直接の後続・大規模展開研究

### [1] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models
- **著者:** Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, et al. (Tongyi Lab, Alibaba Group)
- **arXiv:** [2506.05176](https://arxiv.org/abs/2506.05176) (2025年6月)
- **関連性:**
  - 本研究（Li et al., 2024）の著者陣が Alibaba Tongyi Lab で開発した最新の大規模埋め込み・リランキングモデル（0.6B / 4B / 8B）。
  - 本研究で提案された **slerp ベースのモデルマージ技術** を Stage 3 の重要なパイプラインとして正式採用し、多言語・マルチタスク評価（MTEB / MMTEB / CMTEB / MTEB-Code）で圧倒的な SOTA を達成。

---

## 2. モデルマージ・タスクベクトルの理論・サーベイ論文

### [2] Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities
- **著者:** Prateek Yadav, Derek Tam, Leshem Choshen, Colin Raffel, Mohit Bansal et al. / Enkelejda Kasneci et al.
- **arXiv:** [2408.07666](https://arxiv.org/abs/2408.07666) / ACM Computing Surveys (2024)
- **関連性:**
  - 大規模言語モデルにおけるモデルマージ技術の包括的サーベイ。
  - テキスト埋め込みモデルにおけるマルチタスク競合（Task Conflict）やデータ不均衡を解消する応用例として本論文のアプローチが体系的に位置づけられている。

### [3] Editing Models with Task Vectors
- **著者:** Gabriel Ilharco, Marco Tulio Ribeiro, Mitchell Wortsman, Suchin Gururangan, Ludwig Schmidt, Hannaneh Hajishirzi, Ali Farhadi
- **arXiv:** [2212.04089](https://arxiv.org/abs/2212.04089) (ICLR 2023)
- **関連性:**
  - 本研究で基礎概念として用いられている「タスクベクトル（$V = \theta - \theta_0$）」の原著論文。
  - 重み空間での足し算・引き算によるモデルの能力獲得・忘却制御の幾何学的基礎を解説している。

---

## 3. 直接の比較・ベースラインとなったマルチタスク埋め込みモデル

### [4] One Embedder, Any Task: Instruction-Finetuned Text Embeddings (InstructOR)
- **著者:** Hongjin Su, Weijia Shi, Jungo Kasai, Yizhong Wang, Yushi Hu, Mari Ostendorf, Wen-tau Yih, Noah A. Smith, Luke Zettlemoyer, Tao Yu
- **arXiv:** [2212.09741](https://arxiv.org/abs/2212.09741) (ACL 2023)
- **関連性:**
  - 本研究の実験で 330 タスクの大規模クラスタリング・マージ対象となったベースラインモデル。
  - 指示文（Instruction）付き埋め込みのパイオニアであり、一括学習（Joint Training）の限界を本論文のマージ手法がどのように打破したかを比較理解する上で重要。
