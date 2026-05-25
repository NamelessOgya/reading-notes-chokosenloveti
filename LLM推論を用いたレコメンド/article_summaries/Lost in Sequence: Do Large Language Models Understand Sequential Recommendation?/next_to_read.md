# 次に読むべき関連論文 (Next to Read)

本ドキュメントでは、「Lost in Sequence: Do Large Language Models Understand Sequential Recommendation?」からの発展アプローチや、関連するLLM推薦手法の課題に取り組んでいる後続研究・関連研究を記載する。対象論文（arXiv:2502.13909）のSemantic Scholar被引用データに基づき、特に「LLM埋め込みを用いたレコメンド」や「系列情報の高度化」に関連する重要論文を抽出した。

---

## 1. Not Just What, But When: Integrating Irregular Intervals to LLM for Sequential Recommendation (2025)
- **概要**: 従来の系列推奨（LLMを用いた手法を含む）が「アイテムの順序」のみに注目し、アイテム間の「時間的間隔（Interval）」を静的とみなして無視しがちであるという課題を指摘した論文。
- **関連性**: 本対象論文（LLM-SRec）はLLMが「系列的な推移（順序）」を本当に捉えられているかを議論したが、本研究はそこからさらに一歩踏み込み、時間間隔（動的なInterval）をLLMに統合するための新たなフレームワーク「IntervalLLM」を提案している。推薦における時間的依存関係の理解を深める上で、LLM-SRecの議論を拡張する重要な後続研究である。

## 2. AlignGenRec: Aligning collaborative and textual knowledge for llm-based generative recommendation (2025)
- **概要**: LLMを用いた生成的推薦において、協調知識（Collaborative knowledge）とテキスト知識（Textual knowledge）をいかに統合・アライメント（整合化）させるかを探求した研究。
- **関連性**: 対象論文のLLM-SRecは「協調フィルタリングモデルからの系列知識をLLMのテキスト表現空間に直接蒸留する」ことで性能を上げている。この論文も同様に、各モダリティ（テキストと協調情報）間のギャップを埋めるための知識アライメントに取り組んでおり、蒸留や融合アーキテクチャの別のアプローチ（あるいは発展形）として比較・調査する価値がある。

## 3. Understanding Generative Recommendation with Semantic IDs from a Model-scaling View (2025)
- **概要**: Generative Recommendation（GR）において、アイテムをSemantic IDで表現して自己回帰的に予測する手法の限界を、スケーリング法則（Model-scaling）の観点から分析した論文。
- **関連性**: Semantic IDベースの手法がスケーリングの壁に直面する一方で、「LLM-as-RS（LLMをそのまま強力な推論器として用いるアプローチ）」の限界とスケーリング特性が高いことを実証している。対象論文が指摘したLLM4Recの「構造的限界（順序に鈍感であること）」に対して、モデリング側のアーキテクチャ設計やモデルサイズを通じた新たな見解を提供する可能性がある。
