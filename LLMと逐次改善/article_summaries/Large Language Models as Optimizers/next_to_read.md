# NEXT TO READ

LARGE LANGUAGE MODELS AS OPTIMIZERS (arXiv:2309.03409) を引用している（Cited by）論文の中で、本手法を発展させているものや、異なる角度からアプローチしている後続研究を以下に列挙します。

1. **metaTextGrad: Learning to learn with language models as optimizers** (2024)
   - **Authors:** Guowei Xu, Mert Yuksekgonul, Carlos Guestrin, Matei Zaharia et al.
   - **URL:** [https://www.semanticscholar.org/paper/cd5d6e7678416ab78a19966b20ffea4746a7e98a](https://www.semanticscholar.org/paper/cd5d6e7678416ab78a19966b20ffea4746a7e98a)
   - **理由:** OPROと同じく「LLMをオプティマイザとして用いる手法」をさらに一歩進め、プロンプトのテキスト勾配（Textual Gradient）を用いた "TextGrad" 等のアプローチを拡張し、メタ学習（Learning to learn）の概念を組み合わせて最適化プロセス自体を学習・適応させるフレームワークを提案しているため。OPROの次世代の最適化パラダイムとして必読。

2. **ARPO: Adaptive Reward-driven Prompt Optimization** (2024)
   - **Authors:** Arnav Singhvi, Shreya Agarwal
   - **URL:** [https://www.semanticscholar.org/paper/8ec204cda7abfe5d46368eb552db4fbe57070e08](https://www.semanticscholar.org/paper/8ec204cda7abfe5d46368eb552db4fbe57070e08)
   - **理由:** OPROが過去の軌跡（スコアとプロンプトのペア）をインペリカルに利用していたのに対し、こちらは報酬（Reward）モデルを用いた適応的（Adaptive）なプロンプトの最適化を提案している。RL（強化学習）や報酬関数に基づく別アプローチでのプロンプト改善と比較する上で非常に重要。

3. **Weak-to-Strong In-Context Optimization of Language Model Reasoning** (2024)
   - **Authors:** Keshav Ramji, Alok N. Shah, Vedant Gaur et al.
   - **URL:** [https://www.semanticscholar.org/paper/eb9a0c61ef05c1e8058130ffe0623feeed395ace](https://www.semanticscholar.org/paper/eb9a0c61ef05c1e8058130ffe0623feeed395ace)
   - **理由:** "Weak-to-Strong Generalization"（弱いモデルの生成や評価を用いて強いモデルの推論を強化する）の文脈と、OPROが提唱したIn-Context最適化を融合させた研究。推論能力の最適化（Reasoning Optimization）における最新の応用事例として大いに関連する。
