# 次に読むべき論文 (Next to Read)

対象論文：「Enhancing Temporal Sensitivity of Large Language Model for Recommendation with Counterfactual Tuning」

## 被引用論文（Cited by）に関する注記
本論文は2025年に発表された最新研究であるため、現時点で本論文を直接引用（Cited by）している後続研究は確認されませんでした（ハルシネーションを防ぐため、論文内のReferenceを被引用と偽ることは行っていません）。
代替案として、本論文と問題意識を共有している**同時期の同分野の関連論文（Concurrent Work）**を以下に列挙します。これらは、LLMを用いた逐次推薦において「時間的順序・シーケンス情報の理解」をどのように向上させるかに焦点を当てています。

## Concurrent Work（同時期の関連論文）

### 1. TisLLM: Temporal-aware Integration for LLM-based Sequential Recommendation (2025)
- **概要:** 本論文（CETRec）がアイテムレベルの時間的埋め込みと反事実チューニングを用いて時間情報の希釈を防いだのに対し、TisLLMはスライディングウィンドウを用いてユーザーの対話シーケンスを分割し、LLMが段階的に時系列パターン（Temporal gap）を学習できるコンテキスト表現を構築します。
- **読むべき理由:** LLM推薦における時間的情報の理解という同一課題に対して、「ウィンドウ分割による局所的・段階的アプローチ」という別角度からの解決策を提案しており、CETRecの手法と比較・対照する上で非常に有用です。

### 2. Lost in Sequence: Do Large Language Models Understand Sequential Recommendation? (LLM-SRec) (2025)
- **概要:** 本論文（CETRec）でも言及されているように、LLMが順序情報を適切に理解できていない（シーケンスをシャッフルしても精度が落ちにくい）という問題を深く掘り下げた研究です。LLM-SRecでは、SASRecのような従来の逐次推薦モデルから得られた時間的・順序的知識をLLMに蒸留（Distillation）することでこの問題を解決しようと試みています。
- **読むべき理由:** LLMの自己注意機構と自然言語向け位置埋め込みの限界について深く分析されており、CETRecの「因果推論」を用いたアプローチと、LLM-SRecの「知識蒸留」を用いたアプローチの違いを学ぶことができます。

### 3. SLMRec: Small Language Models for Sequential Recommendation (2024-2025)
- **概要:** LLMを逐次推薦（SR）に用いる際のパラメーター効率や層の冗長性に着目した研究です。大規模モデルの表現力を維持しつつ、不要な中間層を削減することで、時間的な推論性能を損なわずに推論・学習コストを大幅に削減（13%のパラメータサイズで同等性能）する手法を提案しています。
- **読むべき理由:** CETRecによってモデルの時間的感度を高めた後、それを実社会の推薦システムとしてスケールさせる際（効率化・スモールモデル化）に直面する課題とその解決策を提供してくれます。
