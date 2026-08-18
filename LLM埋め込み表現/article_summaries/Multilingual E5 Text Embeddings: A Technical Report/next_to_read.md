# 次に読む論文リスト — Multilingual E5 Text Embeddings

本論文（arXiv: 2402.05672）は 2024年2月に発表され、Semantic Scholar で 500件以上の被引用数を記録している。主要な後続研究を以下に列挙する。

---

## 被引用論文（Cited by）

### 1. mmE5: Improving Multimodal Multilingual Embeddings via High-Fidelity Synthetic Data
- **関連性**: mE5 の直接の後継研究。テキストを超えたマルチモーダル（テキスト・画像・音声）多言語埋め込みに拡張
- **手法の発展**: 高品質合成データを用いてモダリティ間のギャップを埋め、MMEB ベンチマークで SOTA 達成
- **arXiv**: ACL 2025 採録論文
- **推薦理由**: mE5 の「合成データによる多言語拡張」という方針を視覚・音声モダリティに拡大した直接の後続研究

### 2. Training Sparse Mixture of Experts Text Embedding Models
- **関連性**: mE5 をベースラインとしながら、MoE（Mixture of Experts）アーキテクチャで多言語埋め込みをスケール
- **手法の発展**: 専門家の疎結合で推論コストを抑えながら多様な言語・タスクに特化できる埋め込みモデルの実現を目指す
- **推薦理由**: mE5 の「効率と多言語性のトレードオフ」という課題にアプローチした工学的な発展

### 3. Ruri: Japanese General Text Embeddings (arXiv: 2409.07737)
- **関連性**: mE5-large を外部ハード負例マイニング（RRF）のベースモデルとして使用し、mE5 の多言語能力を日本語特化モデルの構築に活用
- **手法の発展**: 日本語専用の合成データ・リランカー・知識蒸留を組み合わせた JMTEB SOTA
- **推薦理由**: mE5 の日本語能力の限界を明示し、専用モデルの必要性と開発手法を詳述

### 4. jina-embeddings-v3: Multilingual Embeddings with Task LoRA
- **関連性**: mE5 とのベンチマーク比較を通じて発展。タスク固有の LoRA アダプターで単一モデルが複数タスクを切り替え
- **手法の発展**: インストラクション方式に代わり LoRA で軽量にタスク特化。Long Context（最大 8192 トークン）対応
- **推薦理由**: mE5 の「インストラクション付き埋め込み」を別角度から実現するアプローチ

### 5. MMTEB: Massive Multilingual Text Embedding Benchmark (arXiv: 2502.13595)
- **関連性**: mE5 を含む多言語埋め込みモデルを250言語・500タスクで包括的に評価する大規模ベンチマーク
- **手法の発展**: MTEB を大幅に拡張し、Instruction Retrieval・Long-Document Retrieval・Code Retrieval を追加
- **推薦理由**: mE5 の弱点（英語以外のタスクでの性能）を定量化し、今後のモデル開発の方向性を示すベンチマーク論文

---

## 関連分野の並行研究（Concurrent Work）

### 6. E5-Mistral: Improving Text Embeddings with Large Language Models (arXiv: 2401.00368)
- **著者**: Liang Wang et al. (同著者陣による並行研究)
- **関連性**: 英語 E5 の LLM 版。Mistral-7B を使った instruction-tuned 埋め込みで MTEB SOTA を達成
- **推薦理由**: mE5 の英語特化版として比較対象。GPT-4 合成データの活用法を詳述

### 7. BGE-M3: Badminton Generative Embedding (arXiv: 2402.03216)
- **関連性**: mE5 と同時期発表。Dense/Sparse/Multi-vector の3種出力に対応した多機能多言語モデル
- **推薦理由**: mE5 が対照とするベースラインとして頻出。ハイブリッド検索への拡張を検討する際の必読論文
