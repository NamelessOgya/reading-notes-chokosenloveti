# 次に読むべき論文 (Next to Read)

「Feedback Descent: Open-Ended Text Optimization via Pairwise Comparison」から着想を得て、テキストベースのフィードバックや反復的な最適化手法をさらに拡張、あるいは別角度で応用している後続の研究（Cited by）を以下に挙げる。

### 1. Expanding the Capabilities of Reinforcement Learning via Text Feedback
- **著者**: Yuda Song, Lili Chen, Fahim Tajwar et al. (2026)
- **URL**: [Semantic Scholar](https://www.semanticscholar.org/paper/89e0ab207c62915b5d6d0ae058811bf97fabf171)
- **選定理由**: Feedback Descentは「テキストによる理由付けをそのままフィードバックとし、重み更新を伴わない推論時のみで最適化する」手法であったが、本論文は「テキストフィードバック」を強化学習（RL）の枠組みそのものにどう組み込み、モデル能力を拡張できるかに焦点を当てている。推論時最適化の優れた点を強化学習による学習ループへ統合・拡張するアプローチとして直接的な後続研究として極めて重要である。

### 2. Automatic Prompt Optimization for Dataset-Level Feature Discovery
- **著者**: Adrian Cosma, Oleg Szehr, David Kletz et al. (2026)
- **URL**: [Semantic Scholar](https://www.semanticscholar.org/paper/ed1bb6d1c7a0bbff1061a1785ae2bca3963dabc4)
- **選定理由**: Feedback Descentでも検証された「ペアワイズ比較を通じたプロンプト最適化」の手法をさらに発展させ、推論精度を高めるだけでなく、データセット全体からマクロな「特徴」そのものを発見（Feature Discovery）するための最適化へと展開している研究。最適化の対象をタスク解決からデータセットレベルのナレッジディスカバリーへと拡張している点で別角度の応用として有用である。

### 3. InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning
- **著者**: Matthew Y. R. Yang, Hao Bai, Ian Wu et al. (2026)
- **URL**: [Semantic Scholar](https://www.semanticscholar.org/paper/762f8a010040304be1ae88bff0847c31165b3980)
- **選定理由**: Feedback Descentにおける「生成」と「評価（理由付け）」の改善ループに近い概念に対して、さらに「LLM自身に自己介入（Interventions）と信用割り当て（Credit Assignment: どの思考ステップが良かった/悪かったのかの正確な特定）を行わせる」ことで推論能力を一段と向上させる手法を提案している。フィードバックを具体的な内部推論パスの割り当てへと洗練させていく研究として読む価値が高い。
