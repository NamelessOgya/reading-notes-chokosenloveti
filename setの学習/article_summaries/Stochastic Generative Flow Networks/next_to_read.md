# 次に読むべき関連・発展論文（Next to Read）

本論文「Stochastic Generative Flow Networks」（UAI 2023）を理解した上で、さらに GFlowNet の理論的拡張、探索の改善、および LLM や実世界タスクへの応用を深めるために推奨される後続・関連文献リストです。

---

## 1. 確率的報酬環境へのアプローチ（姉妹研究）

### 📄 Distributional GFlowNets with Quantile Flows
- **著者:** Dinghuai Zhang, Ling Pan, Ricky T. Q. Chen, Aaron Courville, Yoshua Bengio
- **発表:** 2023年2月（arXiv: [2302.05793](https://arxiv.org/abs/2302.05793)）
- **本論文との関連と推薦理由:**
  - 本論文（Stochastic GFlowNets）が **「状態遷移ダイナミクスの確率的ノイズ」** を扱ったのに対し、本研究はまさに **「報酬関数そのものが確率的・ノイズを伴う環境（Stochastic Rewards）」** を扱うための姉妹論文。
  - 分布強化学習（Distributional RL）のアイディアを GFlowNet に融合し、スカラーの報酬ではなく報酬分布（分位点フロー: Quantile Flows）をモデル化することで、リスクを考慮した探索やノイズに頑健な多様サンプリングを実現している。

---

## 2. GFlowNet の探索改善とモード崩壊の克服（被引用後続研究）

### 📄 Loss-Guided Auxiliary Agents for Overcoming Mode Collapse in GFlowNets
- **著者:** Idriss Malek, Aya Laajil, Abhijith Sharma, Eric Moulines, Salem Lahlou
- **発表:** 2025年5月（arXiv: [2505.15251](https://arxiv.org/abs/2505.15251)）
- **本論文との関連と推薦理由:**
  - 本論文を直接引用して発展させた最新研究。
  - GFlowNet は理論的には全モードを発見できるが、実務上は初期に見つかったモードに一時的に囚われることがある。本研究では、メインモデルの訓練損失（Loss）を直接探索シグナルとして活用する補助 GFlowNet（Loss-Guided GFlowNet: LGGFN）を提案。未知領域の発見効率を劇的に加速させている。

---

## 3. オフライン学習と代理モデル依存の解消（被引用後続研究）

### 📄 Beyond the Proxy: Trajectory-Distilled Guidance for Offline GFlowNet Training
- **著者:** Ruishuo Chen, Xun Wang, Rui Hu, Zhuo-Ran Li, Longbo Huang
- **発表:** 2025年5月（arXiv: [2505.20110](https://arxiv.org/abs/2505.20110)）
- **本論文との関連と推薦理由:**
  - 本論文の共著者である Longbo Huang らの研究グループによる被引用論文。
  - 実環境で報酬を自由にクエリできないオフライン設定において、信頼性の低い代理モデル（Proxy）に頼ることなく、逆強化学習（IRL）を用いて軌跡から密なエッジ報酬を抽出・蒸留して安定した学習を実現する新しいオフライン GFlowNet（TD-GFN）を提案している。

---

## 4. LLM の推論ステップ・思考プロセスへの適用（最新応用）

### 📄 Accurate and Diverse LLM Mathematical Reasoning via Automated PRM-Guided GFlowNets
- **著者:** A. Younsi, Abdalgader Abubaker, Mohamed El Amine Seddik, Hakim Hacid, Salem Lahlou
- **発表:** 2025年4月（arXiv: [2504.19981](https://arxiv.org/abs/2504.19981)）
- **本論文との関連と推薦理由:**
  - GFlowNet の応用先が分子設計から **「大規模言語モデル（LLM）の多段階数学推論」** へと急速に拡大していることを示す重要論文。
  - プロセス報酬モデル（PRM: Process Reward Model）のガイダンスと GFlowNet のサンプリング特性を組み合わせ、LLM が多様で精度の高い解法ステップ（思考の連鎖 / CoT）を探索・生成できる仕組みを実証している。
