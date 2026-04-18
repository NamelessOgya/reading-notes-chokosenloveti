# 次に読むべき論文 (Next to Read)

運用方針に基づき、本リストは**「Pre-trained LLMの埋め込みをファインチューニング等の追加学習なしで、そのまま（as-is / Zero-shot / Training-free）推薦タスクに用いるアプローチ」**に厳格に限定して選定しています。

## 厳選論文リスト（LLM埋め込みの「そのまま」活用に特化）

1. **Do We Really Need Specialization? Evaluating Generalist Text Embeddings for Zero-Shot Recommendation and Search**
   - **概要**: 推薦用に特化させたモデルを学習しなくても、オープンソースの汎用テキスト埋め込み（GTEs）を使って「ゼロショット（ベクトル類似度のみ）」でどれだけ機能するのかを徹底検証した論文。
   - **選定理由**: LLMをファインチューニングせず、凍結された汎用モデルの埋め込みを「そのまま使う」だけで十分な精度が出るという仮説を実証する代表的な研究です。

2. **Are Large Language Models Really Effective for Training-Free Cold-Start Recommendation?**
   - **概要**: 追加の学習（ファインチューニングや重い射影層の訓練）を一切行わず、LLMの事前学習済み埋め込み空間の性質だけを「そのまま」利用したコールドスタート推薦の有効性と限界を検証した研究。
   - **選定理由**: 「Training-free（学習を伴わない）」という条件に最も厳密に合致し、埋め込みをそのまま使うアプローチのポテンシャルを測るベースラインとなります。

3. **Are ID Embeddings Necessary? Whitening Pre-trained Text Embeddings for Effective Sequential Recommendation (WhitenRec)**
   - **概要**: 埋め込みに対するニューラルな追加学習を避け、純粋な統計的データ前処理である「白色化（ZCA）」のみを施して空間の偏りを補正し、そのまま推薦特徴量として使う手法。
   - **選定理由**: ニューラルネットによる表現学習を行わず、計算的・統計的な変換のみでLLM本来の隠れた有用なセマンティクスを最大限引き出している点で「そのまま使う」哲学を体現しています。

4. **Lost in Sequence: Do Large Language Models Understand Sequential Recommendation?**
   - **概要**: LLMとその表現（埋め込み）を推薦システムにそのまま持ち込んだ場合、モデルは本当に「ユーザーの行動の順序」を理解しているのか、それとも単なる「文字列の意味の近さ」に依存しているだけなのかを分析した論文。
   - **選定理由**: 埋め込みをそのまま使うアプローチが抱える「時系列情報の喪失」という本質的な弱点や限界を的確に検証しており、手法を採用する際のメリデメ評価に欠かせない知見を与えます。

