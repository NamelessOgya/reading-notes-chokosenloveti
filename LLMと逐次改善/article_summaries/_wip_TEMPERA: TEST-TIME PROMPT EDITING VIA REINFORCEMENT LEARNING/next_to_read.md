# 次に読むべき論文 (Next to Read)

TEMPERA（Test-Time Prompt Editing via Reinforcement Learning）の「クエリに依存したテスト時プロンプト最適化（Query-Aware / Task-Aware Prompt Optimization）」というアプローチを引用し、さらに発展させている後続の研究・関連論文をリストアップします。強化学習（RL）やテキストフィードバック（Textual Rewards）を用いてプロンプトをタスクごとに洗練させていく手法がトレンドとなっています。

### 1. TRPrompt: Bootstrapping Query-Aware Prompt Optimization from Textual Rewards
- **著者:** Andreea Nica, Ivan Zakazov, N. Baldwin, Saibo Geng, Robert West
- **発行年:** 2025
- **概要:** 
TEMPERAの「テスト時・クエリ依存（Query-aware）」のプロンプト最適化手法を発展させた研究です。スコアベースの数値的な報酬にとどまらず、言語モデルからの「テキストによるフィードバック（Textual feedback）」を組み込み、対象のターゲットモデルパラメータを直接更新することなくプロンプトモデルを学習させます。データセットの事前収集も不要としており、難易度の高い数学推論（MATHデータセットなど）において極めて高いパフォーマンスを発揮することを実証しています。

### 2. Better by Comparison: Retrieval-Augmented Contrastive Reasoning for Automatic Prompt Optimization
- **著者:** Juhyeon Lee, Wonduk Seo, Hyunjin An, Seunghyun Lee, Yi Bu
- **発行年:** 2025
- **概要:** 
プロンプトの自動最適化に「対照推論（Contrastive Reasoning）」を導入した（CRPOフレームワーク）研究です。RAG（Retrieval-Augmented Generation）的なアプローチで過去の高・中・低品質なプロンプト-応答ペアを検索・取得し、なぜ特定のプロンプトが機能し他が失敗するのかをLLM自身に推論（自己反省・比較）させることで、頑健かつ解釈可能な形で自動プロンプト最適化を行います。

### 3. TAPO: Task-Referenced Adaptation for Prompt Optimization
- **著者:** Wenxin Luo, Weirui Wang, Xiaopeng Li, Weibo Zhou, Pengyue Jia, Xiangyu Zhao
- **発行年:** 2025
- **概要:** 
自動プロンプト最適化（APO）において、タスク固有の特性（Task-specific characteristics）が見落とされがちであるという課題に対処する「TAPO（マルチタスク考慮型プロンプト最適化フレームワーク）」を提案する論文です。メトリクス選択、多角的な評価、そして進化型アルゴリズム（Evolution-based optimization）に基づき、多様なタスクに対して適応力が高く、ドメイン固有性の高いプロンプトを自動精製するアプローチを取っています。

### 4. How to Auto-optimize Prompts for Domain Tasks? Adaptive Prompting and Reasoning through Evolutionary Domain Knowledge Adaptation
- **著者:** Yang Zhao, Pu Wang, H. Yang
- **発行年:** 2025
- **概要:** 
「EGO-Prompt」と呼ばれる自動最適化フレームワークを提案する研究です。専門家が定義した因果関係グラフ（SCG）を初期点とし、それを言語モデルの推論に基づいて進化的に最適化・修正していきます。医療・交通など、高度な専門ドメインの知識推論プロセスにおいて、因果情報に基づくプロンプト生成とテキストベースの勾配（Textual gradients）を融合させており、動的最適化の新たなユースケースとして注目されます。

---
**調査メモ:**
TEMPERAは、Discrete空間で強化学習（RL）を用いた探索を行うという点で画期的でしたが、最近の被引用論文の傾向としては、「テキストベースの報酬（Textual Rewards）」「自己反省（Self-Reflection）」「進化アルゴリズムとRAGの融合」を用いて探索効率とクエリ適応性を向上させるアプローチが主流になっていることがわかります。
