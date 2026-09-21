# 次に読むべき関連・発展論文（Next to Read）

本論文「Distributional GFlowNets with Quantile Flows」（TMLR 2024）を理解した上で、GFlowNet の拡散モデルへの展開、画像生成プロンプト最適化、および不確実性モデリングの基礎を深めるために推奨される後続・関連文献リストです。

---

## 1. 拡散モデル（Diffusion Models）の多様性アライメントへの適用（被引用論文）

### 📄 Efficient Diversity-Preserving Diffusion Alignment via Gradient-Informed GFlowNets
- **著者:** Zhen Liu, Tim Z. Xiao, Weiyang Liu, Yoshua Bengio, Dinghuai Zhang
- **発表:** 2024年12月（arXiv: [2412.07775](https://arxiv.org/abs/2412.07775)）
- **本論文との関連と推薦理由:**
  - 本論文の筆頭著者 Dinghuai Zhang および Yoshua Bengio らによる直接の発展研究。
  - Stable Diffusion などの大規模テキスト画像生成モデルにおいて、報酬モデル（人間の選好や美観スコア）に合わせてファインチューニングする際、従来の強化学習（RLHF/RLAIF）では生成画像の多様性が失われる（モード崩壊する）問題があった。
  - 本研究では、GFlowNet の考え方を勾配シグナルと融合した **$\nabla$-GFlowNet** を提案し、事前分布の多様性を美しく保持したまま高速に拡散モデルをアライメントすることに成功している。

---

## 2. LLM プロンプト生成・適応への展開（被引用論文）

### 📄 Learning to Sample Effective and Diverse Prompts for Text-to-Image Generation
- **著者:** Taeyoung Yun, Dinghuai Zhang, Jinkyoo Park, Ling Pan
- **発表:** 2025年2月（arXiv: [2502.11477](https://arxiv.org/abs/2502.11477)）
- **本論文との関連と推薦理由:**
  - 本論文の著者陣（Dinghuai Zhang, Ling Pan）による最新の応用展開。
  - 画像生成モデルが好む効果的かつ多様なプロンプト（指示文）を自動生成・適応させるタスクにおいて、強化学習の画一的なサンプリングを脱却し、GFlowNet の確率的サンプリング特性（多様性保持）を活用してプロンプト空間を網羅的に探索する枠組み（PAG）を提案している。

---

## 3. 環境遷移の不確実性を扱う姉妹研究（同時期の重要研究）

### 📄 Stochastic Generative Flow Networks
- **著者:** Ling Pan, Dinghuai Zhang, Moksh Jain, Longbo Huang, Yoshua Bengio
- **発表:** 2023年2月（UAI 2023採択, arXiv: [2302.09465](https://arxiv.org/abs/2302.09465)）
- **本論文との関連と推薦理由:**
  - 本論文が **「報酬の確率的ノイズ（Stochastic Rewards）」** を分位点フローで扱ったのに対し、**「状態遷移の確率的ダイナミクス（Stochastic Transition Dynamics）」** を事後状態（Afterstate）で扱った完全な姉妹研究。
  - 両者を合わせることで、実世界のあらゆる不確実性（遷移のブレと報酬のブレ）に対する GFlowNet の数理的基盤が完成する。
