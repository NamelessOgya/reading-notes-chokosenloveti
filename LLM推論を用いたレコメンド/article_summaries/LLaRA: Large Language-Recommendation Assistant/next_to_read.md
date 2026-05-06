# 次に読むべき論文 (Next to Read)

LLaRA（Large Language-Recommendation Assistant, SIGIR '24）は、従来の系列推薦モデルが学習したIDベースの行動表現と、LLMの持つテキスト世界知識を同一のプロンプト内に入力空間で統合（ハイブリッドプロンプト）する手法を確立し、カリキュラム学習によって効果的に学習させるアプローチを示しました。本論文の発表以降、この「推薦モデルの埋め込みをいかにLLMに取り込むか」という観点において、数多くの後続研究が生まれています。

Web検索の結果、該当論文は100件以上の被引用数（Semantic Scholar等）を獲得していますが、検索APIの制約によって具体的な被引用論文タイトルを網羅できなかったため、**「LLaRAと同じ発表時期に、ID埋め込みとLLMの統合について別角度からアプローチした最新の関連論文（Concurrent Work）」** および **「LLaRAの比較対象として頻出する基礎論文」** を代替として以下に列挙します。

1. **CoRA: Collaborative Information Perception by Large Language Model’s Weights for Recommendation**
   - **アプローチの角度:** LLaRAは「Input-space（入力プロンプト内）」にID埋め込みなどのCollaborative Tokenを結合する手法をとりましたが、CoRAは「Parameter-space（LLMの重み空間）」にCollaborative Tokenを埋め込む手法（LoRAの重みとして結合させるなど）を提案しています。入力長（コンテキストウィンドウ）を圧迫しないという点でLLaRAとは異なるアプローチをとっており、両者を比較する上で必読です。

2. **CoLLM: Integrating Collaborative Embeddings into Large Language Models for Recommendation**
   - **アプローチの角度:** LLaRAと同様に、LLMとCollaborative Filteringの埋め込みを統合する手法を提案しています。どのようなマッピング手法（プロジェクター層）を用いればLLMが既存の協調情報をもっとも理解しやすくなるかのアーキテクチャ設計に焦点を当てており、同時期の関連研究としてあわせて読むことで、モダリティアライメントの理解が深まります。

3. **PEPLER: Personalized Prompt Learning for Explainable Recommendation**
   - **アプローチの角度:** 推薦の精度だけでなく「なぜそのアイテムを推薦するのか（Explainability）」にLLMを活用する手法です。LLaRAはアイテムの次の行動予測（Next-item prediction）に焦点を当てていますが、PEPLERはユーザーのID埋め込みを利用して生成するテキストのパーソナライズ化に焦点を当てています。推薦システムにおけるLLM活用の別側面として重要です。

4. **TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation**
   - **アプローチの角度:** LLaRAが論文内のベースラインとして比較しているモデルの一つです。LLMを推薦タスクにアラインメント（Tuning）させるための初期の効率的なフレームワークを提案しており、LLaRAのような高度なハイブリッド手法が生まれる前の基礎的ベースラインとして設計を把握しておく必要があります。
