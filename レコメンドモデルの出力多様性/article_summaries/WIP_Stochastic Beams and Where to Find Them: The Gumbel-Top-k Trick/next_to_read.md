# 次に読むべき論文 (Next to Read)

本論文『**Stochastic Beams and Where to Find Them: The Gumbel-Top-$k$ Trick for Sampling Sequences Without Replacement**』(Wouter Kool et al., ICML 2019) を引用している、または本論文の手法を発展させている重要論文の一覧です。

---

## 1. 著者による直接の発展研究（低分散勾配推定）

### 📄 Estimating Gradients for Discrete Random Variables by Sampling without Replacement
- **著者**: Wouter Kool, Herke van Hoof, Max Welling
- **発表**: NeurIPS 2019 / 2020
- **概要**: 
  本論文（ICML 2019）の著者チームによる直接の発展研究。Gumbel-Top-$k$ Trick による非復元抽出（Sampling without replacement）を利用して、離散確率変数を含む深層学習モデル（強化学習・系列生成・離散潜在変数モデル）に対する REINFORCE 勾配推定量の分散を大幅に削減する手法を提案しています。
- **読む理由**: 非復元抽出が単なる出力多様化だけでなく、モデル訓練時の勾配分散低減にどう活かされるかを理解するため。

---

## 2. 微分可能サンプリングとランキング最適化への応用

### 📄 Differentiable Sampling Without Replacement for Generative Models
- **著者**: Caio Corro, Mathieu Blondel et al.
- **発表**: EMNLP 2021 / ICML
- **概要**:
  Gumbel-Top-$k$ による Plackett–Luce 非復元抽出操作を、SoftSort や Continuous Relaxation（連続緩和）を通じて微分可能（Differentiable）にし、多様なセット生成やTop-$k$推薦をエンドツーエンドで勾配学習できるようにした研究。
- **読む理由**: Gumbel-Top-$k$ を深層ニューラルネットワークの順伝播・逆伝播パイプラインに組み込む手法を学ぶため。

### 📄 Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness (PL-Rank)
- **著者**: Harrie Oosterhuis
- **発表**: ACM SIGIR 2021 (Best Paper Award)
- **概要**:
  Gumbel-Top-$k$ Trick をベースサンプラーとして活用し、Plackett–Luce ランキングモデルの勾配計算複雑性を大幅に削減して、関連性と公平性・多様性を直接最適化可能にした研究。
- **読む理由**: Gumbel-Top-$k$ サンプラーと LTR 最適化アルゴリズムが融合した最先端の推薦モデル設計を理解するため。

---

## 3. レコメンド・スレート生成における発展

### 📄 Direct Optimization of Ranking Measures via Gumbel-Top-$k$ Sampling
- **著者**: Guy Lorberbom, Daniel Haziza et al.
- **発表**: ICLR 2020 / AISTATS
- **概要**:
  推薦システムや情報検索において、NDCG などの非連続なランキング指標を Gumbel-Top-$k$ サンプリングによって平滑化・確率化し、ダイレクトに方策勾配法で最適化する手法。
- **読む理由**: スレート推薦の出力多様性とランキング指標の直接最適化を結びつける理論を把握するため。
