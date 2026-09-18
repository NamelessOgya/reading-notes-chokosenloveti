# 次に読むべき論文 (Next to Read)

Ruri / Ruri v3（Tsukagoshi et al., 2024-2025 / arXiv:2409.07737 / cl-nagoya）に関連する、最新の日本語埋め込み・長文エンコーダ・合成データ研究を以下に列挙します。

---

## 1. Ruri を応用した実サービス検索研究

### [1] Towards Better Search with Domain-Aware Text Embeddings for C2C Marketplaces (Mercari)
- **著者:** Andre Rusli, Miao Cao, Shoma Ishimoto, Sho Akiyama, Max Frenzel
- **arXiv:** [2512.21021](https://arxiv.org/abs/2512.21021) (2025年12月)
- **関連性:**
  - Ruri-Small-v2 をベースモデルに採用し、メルカリの購買ログ対照学習と MRL 32 次元圧縮を施して本番導入した実用化論文。

---

## 2. 埋め込みモデルの幾何構造・次元圧縮分析

### [2] Redundancy, Isotropy, and Intrinsic Dimensionality of Prompt-based Text Embeddings
- **著者:** Hayato Tsukagoshi, Ryohei Sasano (名古屋大学 / ACL 2025 Findings)
- **arXiv:** [2506.01435](https://arxiv.org/abs/2506.01435) (2025年6月)
- **関連性:**
  - Ruri の主著者（塚越氏・笹野氏）による、テキスト埋め込み空間の等方性と固有次元に関する理論的・幾何学的分析研究。

---

## 3. 次世代 ModernBERT バックボーン研究

### [3] ModernBERT: Smarter, Better, Faster, Longer
- **著者:** Benjamin Warner, Antoine Chaffin, Benjamin Clavié, et al.
- **arXiv:** [2412.13663](https://arxiv.org/abs/2412.13663) (2024年12月)
- **関連性:**
  - Ruri v3 のベースアーキテクチャとなった、8,192 トークン・RoPE・Unpadding FlashAttention 対応の次世代 BERT エンコーダ。
