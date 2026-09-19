# 次に読むべき論文 (Next to Read)

Towards Better Search with Domain-Aware Text Embeddings for C2C Marketplaces（Rusli et al., Mercari, 2025 / arXiv:2512.21021）に関連する、日本語埋め込み基盤モデルおよび Eコマース・MRL 検索研究を以下に列挙します。

---

## 1. ベースモデルおよび日本語最先端埋め込みモデル

### [1] Ruri v3: High-Performance Japanese Text Embeddings
- **開発:** cl-nagoya / クルツ（早大・名大・東北大・SB Intuitions）
- **関連性:**
  - メルカリのベースモデルとなった Ruri シリーズの最新フラッグシップモデル。日本語 JMTEB / JSICK / MIRACL-ja で最高峰の性能を誇る。

### [2] Matryoshka Representation Learning (MRL)
- **著者:** Aditya Kusupati, Gantavya Bhatt, Aniket Rege, et al.
- **NeurIPS 2022**
- **関連性:**
  - 本論文で 768 次元 $\to$ 32 次元圧縮の中核技術として採用されたマルチスケール表現学習の原著論文。

---

## 2. Eコマース・C2C 検索における対照学習とクリックノイズ対策

### [3] Que2Search: Fast and Accurate Query and Title Matching for Search at Scale
- **著者:** Liu et al. (Meta / Facebook Marketplace)
- **KDD 2021**
- **関連性:**
  - Facebook Marketplace における C2C / C2B 検索のためのマルチモーダル・テキスト埋め込みモデル。

### [4] Embedding-based Retrieval in Facebook Search
- **著者:** Huang et al.
- **KDD 2020**
- **関連性:**
  - ハード負例マイニングとソーシャル・マーケットプレイス検索の業界標準アーキテクチャ。
