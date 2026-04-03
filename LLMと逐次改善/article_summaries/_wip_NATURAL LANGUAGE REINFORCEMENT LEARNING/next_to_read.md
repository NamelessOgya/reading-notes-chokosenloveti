# 次に読むべき関連論文 (Next to Read)

本研究「NATURAL LANGUAGE REINFORCEMENT LEARNING (NLRL)」は、強化学習の報酬や価値更新を自然言語空間のフィードバックに置き換えることで、LLMエージェント内のReasoning能力やCoTを維持したまま、受動的な学習から能動的で解釈可能な学習への転換を目指したものです。
以下に、この論文の後続研究および関連する発展的アプローチ（Concurrent Work等）を列挙します。

## 1. Expanding the Capabilities of Reinforcement Learning via Text Feedback
- **年**: 2026年 (arXiv:2602.02482)
- **概要**:
  通常のRLが単一のスカラー情報に依存する問題に対し、人間の対話において自然に発生する「テキストによるフィードバック（Text Feedback）」を直接利用して学習させるための枠組み（RLTF）を提案しています。自己蒸留（Self Distillation）やフィードバックモデリングといった手法を組み合わせることで、スカラーを介することなく言語情報を内面化させる、NLRLの方向性と非常に親和性が高い研究です。

## 2. Feedback Descent: Open-Ended Text Optimization via Pairwise Comparison
- **年**: 2025年 (arXiv:2511.07919)
- **概要**:
  テキストアーティファクト（プロンプト等）の最適化において、スカラー報酬に圧縮するのではなく「構造化されたテキストフィードバック」の差異を指向性のある勾配（Directional information）として捉える「Feedback Descent」の概念を提唱しています。LLMの推論における空間的最適化を言語フィードバックの枠組みで論じており、NLRLのような言語価値関数と軌を一つにする重要なアプローチを含んでいます。

## 3. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **年**: 2025年 (arXiv:2506.24119)
- **概要**:
  NLRLにおいてもTic-Tac-Toeやマルコフ決定過程におけるエージェント学習が議論されていますが、この研究はさらに一歩進め、人間の監督なしにLLMが継続的にゼロサムゲームの「自己対局（Self-Play）」を繰り返すことで推論モデルが自動的にカリキュラムを生成・強化していくマルチエージェントRLの仕組みを提案しています。スカラー報酬を超えたドメインでの推論能力の転移について詳細に調査しています。

## 4. Reinforcement Learning via Self-Distillation
- **年**: 2026年 (arXiv:2601.20802)
- **概要**:
  コーディングや数学などのタスクにおいて、外部の実行エラーやフィードバック文そのものをRLの学習シグナルへと変換する手法「Self-Distillation Policy Optimization (SDPO)」を提案しています。NLRLのLVF（Language Value Function）と同様に、「外部リワードモデルや教師なしで、モデル自身がコンテキスト内での言語的な振り返りをポリシーに蒸留（還元）する」という点で実用的なアプローチを示しています。
