# 次に読むべき論文 (Next to Read)

※注意: 本論文（IntervalLLM）は発表直後（2025年）であるため、現時点で本手法を直接引用・発展させた後続研究（Cited by）は十分に確認できませんでした。そのため、ハルシネーション（捏造）を避け、**同じ発表時期・同分野の最新関連論文（Concurrent Work）**から、LLMと時間情報の統合（Temporal / Interval）に関する重要なアプローチを提案しているものを列挙します。

## 1. Tempura: Training-Free Temporal Prompting for LLM-based Recommendation
- **選定理由**: IntervalLLMがモデルのファインチューニング（LoRA）やアテンション層の追加を行ったのに対し、Tempuraは**追加の学習を一切行わず（Training-Free）に**LLMへ時間情報（Temporal Dynamics）を認識させるプロンプティング手法を提案しています。時間情報の扱い方をIn-Context Learningやクラスタリングの工夫のみで解決しようとするアプローチであり、IntervalLLMとの対比や組み合わせの観点から非常に有用です。

## 2. TisLLM: Temporal-aware Integration for LLM-based Sequential Recommendation
- **選定理由**: IntervalLLMが個々の行動間の「インターバル」に焦点を当てたのに対し、TisLLMはユーザーの行動データを「時間的なスライディングウィンドウ（時系列スライス）」で分割し、それを集約することでLLMに時間的な文脈表現を獲得させる手法を提案しています。時系列の区切り方や時間文脈の集約方法について、異なるアプローチからの知見を得ることができます。

## 3. SLMRec: Small Language Models for Sequential Recommendation
- **選定理由**: 時間情報や複雑な行動シーケンスをLLMに組み込むと計算コストが膨大になります。SLMRecは、LLMの持つ高度なシーケンス推論能力（時間情報なども含む）を小規模な言語モデル（Small Language Models）に知識蒸留（Knowledge Distillation）する手法です。IntervalLLMのように複雑化したモデルを実世界のリアルタイム推薦にデプロイする際の実用的な解決策として次に読むべき研究です。
