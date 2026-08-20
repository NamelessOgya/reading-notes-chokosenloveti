# 次に読む論文リスト — Ruri: Japanese General Text Embeddings

本論文（arXiv: 2409.07737）は 2024年9月に発表された。被引用論文はまだ少数だが、日本語 RAG・埋め込み分野で広く参照されている。

---

## 被引用論文（Cited by）

### 1. Redundancy, Isotropy, and Intrinsic Dimensionality of Prompt-based Text Embeddings (Findings of ACL 2025)
- **著者**: Hayato Tsukagoshi, Ryohei Sasano（Ruri 同著者）
- **関連性**: Ruri の埋め込み表現の幾何学的特性を分析。プロンプト付き埋め込みの冗長性・等方性・内在次元を調査
- **手法の発展**: Ruri で実現したプロンプトベース埋め込みがどのような表現空間を形成するかを理論的に考察
- **推薦理由**: 同著者による直接の後続研究。Ruri の埋め込みの「なぜ良いのか」を解明する分析論文

### 2. Towards Better Search with Domain-Aware Text Embeddings for C2C Marketplaces (2025)
- **関連性**: C2C マーケットプレイス（フリマアプリ等）のドメイン特化検索に Ruri のロールプレフィックス手法を応用
- **手法の発展**: 「クエリ: 」「文章: 」のようなロールプレフィックスを商品検索特化のドメインプレフィックスに拡張
- **推薦理由**: Ruri の非対称接頭辞（prefix）手法を実用アプリケーションに発展させた応用研究

### 3. Omni-JDocVQA: A Comprehensive Japanese Benchmark for Visual Document Understanding (OpenReview, 2025)
- **関連性**: 日本語ビジュアルドキュメント理解ベンチマークの構築に ruri-v3-310m モデルを採用
- **手法の発展**: Ruri をビジュアル QA 評価のための埋め込み基盤として使用し、日本語 VQA の包括的ベンチマークを構築
- **推薦理由**: Ruri が日本語 NLP の幅広い応用（テキスト検索を超えた VQA）で使われている事例

---

## 関連分野の並行研究・後続研究（2025年）

### 4. Ruri v3（Ruri の後継モデル）
- **リリース**: 2025年（cl-nagoya/ruri-v3-30m 〜 310m）
- **ベースモデル**: ModernBERT-Ja（最大 8192 トークンのコンテキスト長対応）
- **関連性**: 本論文（Ruri v1）の直接の後続モデルシリーズ。JMTEB で引き続き高スコアを記録
- **推薦理由**: Ruri の次バージョン。コンテキスト長拡大・軽量化の手法を確認するために必読

### 5. PLaMo-Embedding-1B（Preferred Networks, 2025）
- **関連性**: Ruri に並ぶ日本語特化埋め込みモデル。JMTEB で Ruri に匹敵する性能を達成
- **推薦理由**: 日本語埋め込みの競合研究。Ruri と異なる手法で同等性能を実現しているアプローチを比較するために有用

### 6. JaColBERTv2.5: Optimised Late Interaction Retrieval (arXiv: 2407.xxxxxx, 2024)
- **関連性**: Ruri の論文内でリランカー学習の知識蒸留手法として参照されている後続の日本語特化検索モデル
- **手法の発展**: ColBERT の遅延インタラクション（Late Interaction）を日本語に特化最適化
- **推薦理由**: Ruri が知識蒸留の参照先としたモデル。検索精度のさらなる向上を目指す際の比較対象

### 7. MMTEB: Massive Multilingual Text Embedding Benchmark (arXiv: 2502.13595, 2025)
- **関連性**: JMTEB の英語版に相当する日本語包括評価を担う MMTEB の中に日本語タスクが統合
- **推薦理由**: JMTEB の位置づけ・今後の日本語評価の方向性を把握するための必読論文
