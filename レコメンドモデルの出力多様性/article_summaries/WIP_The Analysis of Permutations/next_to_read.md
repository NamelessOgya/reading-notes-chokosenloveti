# 次に読むべき論文 (Next to Read)

本論文『**The Analysis of Permutations**』(Robin L. Plackett, 1975) を基礎として発展した重要論文の一覧です。

---

## 1. 確率的順列と最尤推定アルゴリズムの発展

### 📄 Maximum Likelihood Estimation of the Plackett-Luce Model for Incomplete Ranks
- **著者**: David R. Hunter
- **発表**: The Annals of Statistics 2004
- **概要**: 
  Plackett–Luce モデルの最尤推定に対して、Minorization-Maximization (MM) アルゴリズムを適用し、不完全な順位データや大規模データセットに対しても極めて高速・安定に収束する汎用推定フレームワークを提案。
- **読む理由**: Plackett–Luce モデルの近代的・効率的なパラメータ推定アルゴリズムを理解するため。

---

## 2. 機械学習・Learning to Rank への展開

### 📄 Learning to Rank: From Pairwise Approach to Listwise Approach (ListNet)
- **著者**: Zhe Cao, Tao Qin, Tie-Yan Liu, Ming-Feng Tsai, Hang Li
- **発表**: ICML 2007
- **概要**:
  情報検索におけるランキング学習（LTR）において、Plackett–Luce 確率分布に基づく順列クロスエントロピー損失（Listwise Loss）を導入し、現代 LTR の基礎を築いた論文。
- **読む理由**: Plackett–Luce モデルがニューラルネットワークや機械学習の損失関数としてどう定式化されたかを把握するため。

### 📄 Listwise Approach to Learning to Rank: Theory and Algorithm (ListMLE)
- **著者**: Fen Xia, Tie-Yan Liu, Jue Wang, Wensheng Zhang, Hang Li
- **発表**: ICML 2008
- **概要**:
  正解ランキングに対する Plackett–Luce モデルの負の対数尤度（Negative Log-Likelihood）を直接最小化する ListMLE アルゴリズムを提案。
- **読む理由**: 正解ランキングの尤度最大化としての LTR 理論を理解するため。

---

## 3. 高速サンプリングと多様性・強化学習への展開（本トピックまとめ論文）

- **[Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness (PL-Rank)](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Computationally%20Efficient%20Optimization%20of%20Plackett-Luce%20Ranking%20Models%20for%20Relevance%20and%20Fairness/summary.md)** (Harrie Oosterhuis, SIGIR 2021)
- **[Stochastic Beams and Where to Find Them: The Gumbel-Top-$k$ Trick](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Stochastic%20Beams%20and%20Where%20to%20Find%20Them:%20The%20Gumbel-Top-k%20Trick/summary.md)** (Wouter Kool et al., ICML 2019)
