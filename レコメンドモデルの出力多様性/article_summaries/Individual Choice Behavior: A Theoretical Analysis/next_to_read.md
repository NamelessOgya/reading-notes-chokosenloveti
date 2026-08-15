# 次に読むべき論文 (Next to Read)

本著作『**Individual Choice Behavior: A Theoretical Analysis**』(R. Duncan Luce, 1959) を基礎として発展した歴史的・現代的な重要文献の一覧です。

---

## 1. ランキングモデルとしての完成と計量経済学への展開

### 📄 The Analysis of Permutations
- **著者**: Robin L. Plackett
- **発表**: Journal of the Royal Statistical Society (Series C) 1975
- **概要**: 
  Luce の選択公理に基づき、順列（フルランキング）全体の結合確率モデル（Plackett–Luce 分布）を数学的に定式化し、最尤推定法を確立した原典論文。
- **読む理由**: Luce の1要素選択モデルが、いかにして現代のランキングモデルへと拡張されたかを理解するため。

### 📄 Conditional Logit Analysis of Qualitative Choice Behavior
- **著者**: Daniel McFadden (ダニエル・マクファデン)
- **発表**: Frontiers in Econometrics 1974 (ノーベル経済学賞受賞研究)
- **概要**:
  Luce の選択モデルを極値分布（Gumbel 分布）ノイズに基づくランダム効用モデル（Random Utility Model: RUM）として厳密に証明・定式化し、現代計量経済学・多項ロジットの標準理論を構築。
- **読む理由**: Gumbel 分布ノイズと Luce 選択モデル（Softmax）の数学的等価性を学ぶため。

---

## 2. IIA（無関係な選択肢の独立性）の克服と多様性モデル

### 📄 Nested Logit Models of Transport Demand
- **著者**: Daniel McFadden
- **発表**: 1978
- **概要**:
  Luce モデルの最大の弱点である IIA 仮定（類似アイテム間の共食い）を克服するため、階層的な選択肢クラスタリングを導入したネスティッド・ロジットモデル。
- **読む理由**: 推薦におけるカテゴリー多様性や階層的推薦の数理的背景を理解するため。

---

## 3. 機械学習・推薦システムへの展開（本トピックまとめ論文）

- **[Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness (PL-Rank)](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Computationally%20Efficient%20Optimization%20of%20Plackett-Luce%20Ranking%20Models%20for%20Relevance%20and%20Fairness/summary.md)** (Harrie Oosterhuis, SIGIR 2021)
- **[Stochastic Beams and Where to Find Them: The Gumbel-Top-$k$ Trick](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Stochastic%20Beams%20and%20Where%20to%20Find%20Them:%20The%20Gumbel-Top-k%20Trick/summary.md)** (Wouter Kool et al., ICML 2019)
- **[Reinforcement Learning for Slate-based Recommender Systems (SlateQ)](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Reinforcement%20Learning%20for%20Slate-based%20Recommender%20Systems:%20A%20Tractable%20Decomposition%20and%20Practical%20Methodology/summary.md)** (Eugene Ie et al., IJCAI 2019)
