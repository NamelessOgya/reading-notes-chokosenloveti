# 次に読むべき論文 (Next to Read)

本論文『**Conditional Logit Analysis of Qualitative Choice Behavior**』(Daniel McFadden, 1974) を基礎として発展した重要文献の一覧です。

---

## 1. 著者による発展研究（IIAの克服・一般化極値分布）

### 📄 Modeling the Choice of Residential Location (Nested Logit)
- **著者**: Daniel McFadden
- **発表**: Spatial Interaction Theory and Planning Models 1978
- **概要**: 
  条件付きロジットモデルの IIA（無関係な選択肢の独立性）仮定を緩和するため、誤差項に相関構造を持たせた一般化極値分布（Generalized Extreme Value: GEV）およびネスティッド・ロジット（Nested Logit）モデルを提案。
- **読む理由**: 類似した代替アイテム間の共食い（多様性の欠如）を数理的に解決する手法を学ぶため。

---

## 2. 機械学習・深層学習における Gumbel トリックの発展

### 📄 Categorical Reparameterization with Gumbel-Softmax
- **著者**: Eric Jang, Shixiang Gu, Ben Poole
- **発表**: ICLR 2017
- **概要**:
  マクファデンのガンベル乱数最大化定理（Gumbel-Max Trick）を温度パラメータ付き Softmax で連続緩和し、離散変数のサンプリングを微分可能にしてエンドツーエンド学習を可能にした記念碑的論文。
- **読む理由**: マクファデンの理論が現代ディープラーニングの生成モデル（VAEや強化学習）にいかに不可欠かを理解するため。

---

## 3. 推薦システム・出力多様性への展開（本トピックまとめ論文）

- **[Stochastic Beams and Where to Find Them: The Gumbel-Top-$k$ Trick](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Stochastic%20Beams%20and%20Where%20to%20Find%20Them:%20The%20Gumbel-Top-k%20Trick/summary.md)** (Wouter Kool et al., ICML 2019)
  - マクファデンの Gumbel-Max を Top-$k$ 個の非復元抽出へと拡張し、Plackett–Luce 多様スレート生成を高速化した論文。
- **[Reinforcement Learning for Slate-based Recommender Systems (SlateQ)](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Reinforcement%20Learning%20for%20Slate-based%20Recommender%20Systems:%20A%20Tractable%20Decomposition%20and%20Practical%20Methodology/summary.md)** (Eugene Ie et al., IJCAI 2019)
  - マクファデンの条件付きロジット選択モデルを強化学習の長期価値（Q値）分解に組み込んだ YouTube 本番推薦論文。
