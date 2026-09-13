# 次に読むべき論文 (Next to Read)

本論文「**The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers**」（Xu et al., Meta, 2026年7月 / arXiv:2607.25346）に関連する、最新の推薦システム・LLM埋め込み表現・潜在推論研究を以下に列挙します。

> [!NOTE]
> 本論文は2026年7月末に公開された直後のフロンティア研究であるため、現時点でSemantic ScholarやWeb上に本論文を引用している後続論文（Cited by）はまだ存在しません。そのため、本論文の対立軸となった**生成型推薦の最新SOTA研究**や、本手法のキー技術（潜在推論、Yes/Noロジットスコアリング、2タワー蒸留）を構成する**同時期の重要関連論文（Concurrent / Foundational Works）**を代替として列挙しています。

---

## 1. 生成型推薦（Generative Retrieval）の最新対抗研究

### [1] OneRec-Think: Think Before You Recommend in Generative Recommenders
- **著者:** Kuaishou Technology（快手）
- **発表:** 2026年
- **関連性と概要:**
  - 本論文が Table 1 で直接比較対象とした**生成型推薦モデルの最高峰（8B）**。
  - アイテムを推薦する前にLLMに思考トレース（In-text Reasoning）を生成させ、文脈とユーザー意図を深く推論した上でセマンティックIDを出力させる。
  - 本論文は「OneRec-Thinkのような生成型は推論遅延と接地エラーが深刻であり、0.6Bの識別的2タワーで凌駕できる」と主張しているため、両者のアプローチを比較対照する上で必読。

### [2] Recommender Systems with Generative Retrieval (TIGER)
- **著者:** Shashank Rajput, Nikhil Mehta, Anima Singh, Ed H. Chi, et al. (Google Research)
- **発表:** NeurIPS 2023
- **関連性と概要:**
  - セマンティックID（RQ-VAEで階層クラスタリングした離散コード）を用いて推薦を「テキスト生成」として定式化した生成型検索の先駆的研究。本論文のベンチマーク実験プロトコルの直接のベースライン。

---

## 2. 潜在推論（Latent Reasoning）とLLM埋め込み技術

### [3] Training Large Language Models to Reason in a Continuous Latent Space (Coconut)
- **著者:** Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, et al.
- **発表:** 2024年 / arXiv:2412.06769
- **関連性と概要:**
  - 言語モデルに自然言語トークンを生成させるのではなく、**連続的な隠れ状態ベクトル（Latent Thought Token）のまま推論ステップを進めさせる「Coconut」**を提唱。
  - 本論文はこの着想を2タワーのユーザータワーに応用し、アイテム側のオフライン事前計算性を崩さずにユーザー側の表現力を向上させた。

### [4] MixLM: Hybrid Language Models for Ranking
- **著者:** 2025年
- **関連性と概要:**
  - Cross-Encoderの出力ヘッドとして、分類層ではなく言語モデルの「Yes / No」の次トークン予測ロジット差を用いる手法を提案した研究。本論文のCE教師モデルのスコアリング設計に直接寄与。

### [5] NV-Embed-v2: Improved Techniques for Training LLMs as Generalist Embedding Models
- **著者:** Chankyu Lee, Rajarshi Roy, Bryan Catanzaro, Wei Ping, et al. (NVIDIA)
- **発表:** 2024年9月 / arXiv:2405.17428
- **関連性と概要:**
  - デコーダ専用LLMをテキスト埋め込みモデルへと転換するための体系的技術（プーリング、対照指示文チューニング、2段階学習）。2タワー型埋め込みモデルの最高峰としての知見を多数提供。
