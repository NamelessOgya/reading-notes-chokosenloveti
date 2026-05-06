# 次に読むべき論文 (Next to Read)

本論文（Recommender Systems with Generative Retrieval; TIGER）の手法を発展させている、あるいは別のアプローチをとっている後続の関連論文を以下に列挙します。

## 1. Generative Retrieval with Semantic Tree-Structured Item Identifiers via Contrastive Learning (2023)
- **概要**: TIGERと同じく「生成型検索（Generative Retrieval）」をレコメンドシステムに適用した研究ですが、アイテムを単純なコードタプルではなく「木構造（Tree-Structured）のセマンティック識別子」としてインデックス化する手法を提案しています。さらに、対照学習（Contrastive Learning）を導入することで、アイテム同士の意味的な近さをより正確に識別子へ反映させ、検索精度を向上させています。
- **選定理由**: TIGERで提案された「RQ-VAEによる階層的なID生成」の課題を、より高度なツリー構造と対照学習によって発展・最適化させた直接的な後続研究であり、ID生成手法の高度化を学ぶのに最適です。

## 2. Language Models Encode Collaborative Signals in Recommendation (2024)
- **概要**: 大規模言語モデル（LLMs）が、推薦システムにおける「協調信号（Collaborative Signals）」をどのように捉え、エンコードしているかを分析した論文です。セマンティックな情報のみならず、ユーザー間の協調フィルタリング的な要素がLLM内部でどのように表現されているかを解明しようとしています。
- **選定理由**: TIGERはアイテムの「テキストベースのセマンティック特徴」からIDを生成し知識を共有しますが、推薦のもう一つの軸である「協調関係（ユーザー行動の類似性）」が言語モデルにどのように取り込まれるかという別視点からのアプローチを提供してくれるため。

## 3. Multimodal Music Tokenization with Residual Quantization for Generative Retrieval
- **概要**: 音楽領域においてマルチモーダルな特徴をRQ-VAEベースで残差量子化（Residual Quantization）し、生成型検索に用いる手法です。
- **選定理由**: TIGERの中核技術である「RQ-VAEによる量子化とGenerative Retrieval」の枠組みを、テキストだけでなく音楽というマルチモーダル領域に拡張しており、他ドメインでの応用例として非常に参考になります。
