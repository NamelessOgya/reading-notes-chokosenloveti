# 次に読むべき論文 (Next to Read)

本論文（Tempura: arXiv 2405.02778）を引用しており、LLMの推論を用いたレコメンドや時系列情報（Temporal Awareness）の考慮について発展・別角度からアプローチしている後続論文を以下に列挙します。Semantic Scholar APIによる被引用ネットワーク検索から事実確認を行っています。

1. **Enhancing Time Awareness in Generative Recommendation** (2025)
   - Tempuraの「時間的な文脈の理解」というテーマをさらに推し進め、生成的なレコメンド手法においてどのように時間的認識を強化できるかに焦点を当てた直近の研究。LLMによる生成ベースのレコメンドに興味がある場合に読むべき後続論文。
2. **Using LLMs to Capture Users' Temporal Context for Recommendation** (2025)
   - Tempuraと同様にLLMを活用してユーザの過去の履歴（時間的コンテキスト）を直接キャプチャするアプローチを議論している論文。より進んだコンテキストの捉え方やモデリング手法を探求する上で重要。
3. **Enhancing Temporal Sensitivity of Large Language Model for Recommendation with Counterfactual Tuning** (2025)
   - Tempuraが追加学習不要（Training-Free）なプロンプト工夫で時間的感度を向上させたのに対し、本論文は反事実的チューニング（Counterfactual Tuning）を用いてLLMのモデル自体の時間的感度を向上させるアプローチを取っている。Training-basedな手法との比較・組み合わせの観点で非常に有用。
4. **Beyond Inter-Item Relations: Dynamic Adaption for Enhancing LLM-Based Sequential Recommendation** (2024)
   - アイテム間の静的な関係性にとどまらず、ユーザの興味の動的（Dynamic）な推移をLLMでいかに捉えるかに取り組んでいる後続研究。
5. **Towards Next-Generation LLM-based Recommender Systems: A Survey and Beyond** (2024)
   - Tempuraを含む、次世代のLLMベースのレコメンドシステム全体を俯瞰したサーベイ論文。Tempuraの立ち位置や、LLMをレコメンデーションに組み込むためのプロンプト戦略・アーキテクチャの最新の全体像を把握するのに最適。
