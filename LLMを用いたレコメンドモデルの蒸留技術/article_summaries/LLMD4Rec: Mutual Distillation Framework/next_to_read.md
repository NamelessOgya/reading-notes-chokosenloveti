# 次に読むべき論文 (Next to Read)

## LLMD4Recの被引用論文について
LLMD4Recは発表されたばかり（直近のarXiv preprint）の論文であるため、現時点で**対象論文を直接引用している後続研究（Cited by）は見つかっていません**。

## 関連最新論文 (Concurrent Work / 近接分野)
LLMD4Recと同様に、「推薦システムにおける大規模言語モデル（LLM）の推論・蒸留コスト削減」や「レコメンドへのLLM知識の効果的な統合」をテーマとする、2025年発表の最新関連論文を以下に列挙します。次に読む資料として参考になります。

### 1. SLMRec: Small Language Model Recommender
- **概要**: LLMによるレコメンドにおける推論レイテンシを根本的に解決するため、LLMから推薦タスクにおいて冗長な層をプルーニング（剪定）し、知識蒸留によって軽量な言語モデル（Small Language Model: SLM）へと圧縮して直接推薦システムを動作させる手法。CRMの精度に依存せず、言語モデルそのものの軽量化を行うという、LLMD4Recとは異なるアプローチの蒸留基盤。

### 2. Active Large Language Model-based Knowledge Distillation (ALKDRec など)
- **概要**: 知識蒸留を行う際、データセット全体に対してLLMで推論（指導信号の生成）を行うコストが膨大になる問題を解決する手法。「LLMを教え手として用いる価値が高いサンプル（情報量が多い、難易度が高いなど）」を能動学習（Active Learning）によってサブセットとして選別し、蒸留の計算コストを大幅に削減しながら高精度を維持する。

### 3. Rationale Distillation for Sequential Recommendation
- **概要**: LLMD4Recのように予測確率分布（Score Softmax）のKLダイバージェンスを最小化するだけでなく、「なぜその商品が選ばれたのか」という**推薦の根拠（Rationale）のテキスト的特性**ごと段階的に蒸留し、従来型モデル（CRM）へ説明可能性とより深いユーザープロファイリング能力を同時付与する研究アプローチ。予測層の分布以外のアラインメント手法を学ぶうえで有用。
