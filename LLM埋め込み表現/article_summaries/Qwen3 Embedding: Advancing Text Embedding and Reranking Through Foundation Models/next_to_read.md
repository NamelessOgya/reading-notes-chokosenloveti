# 次に読む論文リスト — Qwen3 Embedding

本論文（arXiv: 2506.05176）は 2025年6月に発表され、Semantic Scholar で 1,100件以上の被引用数を記録している（2026年8月時点）。被引用論文が非常に多いため、特に関連性・重要性の高いものを厳選して列挙する。

---

## 被引用論文（Cited by）

### 1. Gemini Embedding: Generalizable Embeddings from Gemini (arXiv: 2503.07891)
- **関連性**: Qwen3 Embedding が凌駕した前 SOTA モデル。Gemini 基盤の商用埋め込みモデルの技術詳細
- **手法**: Gemini モデルの巨大な世界知識を埋め込みに転用。MMTEB で Qwen3 発表前は最高スコア
- **推薦理由**: Qwen3 Embedding の「倒すべき対象」として論文中で比較されており、技術的な差分を理解するために必読

### 2. MMTEB: Massive Multilingual Text Embedding Benchmark (arXiv: 2502.13595)
- **関連性**: Qwen3 Embedding の主評価ベンチマーク（131タスク・250言語以上）
- **手法の発展**: MTEB を大幅に拡張しコミュニティ駆動で維持。Instruction Retrieval・Code Retrieval 等の新タスクを追加
- **推薦理由**: Qwen3 の性能を正確に解釈するための必読ベンチマーク論文

### 3. NV-Embed-v2: Improved Techniques for Training LLMs as Generalist Embedding Models (NVIDIA, 2024)
- **関連性**: Qwen3 Embedding が比較対象とした7B LLM ベース埋め込みモデル
- **手法**: LLM 埋め込みの学習技法（双方向アテンション・Multi-task instruction training）を詳述
- **推薦理由**: Qwen3 の Instruction Retrieval での突出した改善（5.09 vs 1.04）と対比するための技術論文

### 4. GTE-Qwen2: Multi-stage Text Embedding with General Text Embeddings (arXiv: 2407.19669)
- **関連性**: Qwen3 Embedding の前身。Qwen2 ベースの GTE モデルシリーズの技術詳細
- **手法の発展**: Qwen3 Embedding はこの GTE-Qwen2 から合成データ生成・モデルマージを大幅に強化
- **推薦理由**: Qwen3 との技術的な変化点を把握するために必要な直接の前身論文

### 5. FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions (arXiv: 2403.15246)
- **関連性**: Qwen3-Reranker が14.84という突出したスコアを達成したタスクのベンチマーク論文
- **手法**: 検索モデルのインストラクション追従能力を評価する新ベンチマーク
- **推薦理由**: Qwen3 Embedding/Reranker の最大の差別化要因（インストラクション対応）を評価する枠組みを理解するために必読

### 6. Improving Text Embeddings with Large Language Models (E5-Mistral, arXiv: 2401.00368)
- **関連性**: Qwen3 の多段階学習・合成データ戦略の先行研究として引用
- **手法**: GPT-4 による合成データ生成と Mistral-7B の組み合わせで MTEB SOTA
- **推薦理由**: Qwen3 と同じ「LLM 合成データ + LLM バックボーン」アプローチの先駆的論文

---

## 関連分野の並行研究・後続研究（2025年）

### 7. Scaling Laws for Text Embeddings (2025年以降)
- **関連性**: Qwen3 Embedding が 0.6B/4B/8B の3サイズで示したスケーリング特性（0.6B でも既存 7B モデルを凌駕）
- **推薦理由**: LLM ベース埋め込みモデルのスケーリング則を体系化した研究として今後の方向性を示す

### 8. Matryoshka Representation Learning (arXiv: 2205.13147, Kusupati et al.)
- **関連性**: Qwen3 Embedding が採用している可変次元埋め込み（Flexible Dimension Representation）の理論的基盤
- **手法**: 埋め込みをネスト構造で学習し、低次元でも高精度を維持する MRL の提案論文
- **推薦理由**: Qwen3 の「次元圧縮時の精度維持」機能の背景理論として理解が深まる

### 9. Persona Hub: Scaling Synthetic Data Creation with 1 Billion Diverse AI Personas (arXiv: 2406.20094)
- **関連性**: Qwen3 Embedding の合成データ生成で使用された Persona Hub（クエリ多様性向上のためのキャラクター選択）
- **推薦理由**: Qwen3 の合成データ生成パイプラインの「多様性確保」メカニズムの詳細を把握するために必読
