# レコメンドモデルの出力多様性（Diversity in Recommendation Systems）

本ディレクトリでは、レコメンドモデルにおける出力多様性（Diversity）・スレート生成・確率的ランキング（Plackett–Luceモデル、DPP等）に関する技術ドキュメントおよび論文要約を体系的に管理します。

---

## 📚 論文まとめ一覧 (Article Summaries)

本トピックにおいて調査・要約を完了した主要文献の一覧です（**原典・離散選択基礎 5編 + 多様性・スレート最適化 5編**）。各ディレクトリ内に詳細な要約（`summary.md`）、引用文献リスト（`ref_article.md`）、次に読むべき発展論文リスト（`next_to_read.md`）が格納されています。

### 🏛️ 基礎・選択理論・IIAの克服 (Foundations & Discrete Choice)
| # | 文献名 | 著者・発表 | 主要テーマ | まとめリンク |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Individual Choice Behavior: A Theoretical Analysis** | R. Duncan Luce<br>(1959, John Wiley & Sons) | 選択公理 (Choice Axiom)、Luce Rule (Softmaxの原型)、IIA仮定、非復元逐次選択 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Individual%20Choice%20Behavior:%20A%20Theoretical%20Analysis/summary.md) |
| 2 | **Review of Individual Choice Behavior: A Theoretical Analysis** | Gérard Debreu<br>(1960, AER / Nobel Prize 1983) | **赤バス・青バス問題の起源**、IIA仮定の致命的欠陥の指摘、ドビュッシーとベートーヴェンの反例 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Review%20of%20Individual%20Choice%20Behavior:%20A%20Theoretical%20Analysis/summary.md) |
| 3 | **Conditional Logit Analysis of Qualitative Choice Behavior** | Daniel McFadden<br>(1974, Nobel Prize 2000) | ランダム効用モデル (RUM)、ガンベル極値分布、Softmaxの経済学的・数理的証明、Gumbel-Maxの起源 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Conditional%20Logit%20Analysis%20of%20Qualitative%20Choice%20Behavior/summary.md) |
| 4 | **The Analysis of Permutations** | Robin L. Plackett<br>(1975, JRSS Series C) | 順列確率分布 (Plackett–Luce 分布) の数学的定式化、最尤推定法 (MLE) と検定理論 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/The%20Analysis%20of%20Permutations/summary.md) |
| 5 | **Modeling the Choice of Residential Location** | Daniel McFadden<br>(1978, North-Holland) | **Nested Logit モデル**、一般化極値分布 (GEV)、赤バス・青バス問題の解決、木構造相関 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Modeling%20the%20Choice%20of%20Residential%20Location/summary.md) |

---

### 🚀 多様性制御・スレート推薦の近年の発展手法 (Modern Diversity & RL)
| # | 論文名 | 著者・会議 | 主要テーマ | まとめリンク |
| :-: | :--- | :--- | :--- | :--- |
| 6 | **Determinantal Point Processes for Machine Learning** | Alex Kulesza, Ben Taskar<br>(2012, FnT in Machine Learning) | **行列式点過程 (DPP)**、幾何学的多様性モデリング、関連性と多様性の体積分解、負の相関 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Determinantal%20Point%20Processes%20for%20Machine%20Learning/summary.md) |
| 7 | **Off-policy evaluation for slate recommendation** | Adith Swaminathan et al.<br>(NeurIPS 2017) | スレート推薦の反実仮想評価（OPE）、加法分解仮定、疑似逆行列推定量 (PI) | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Off-policy%20evaluation%20for%20slate%20recommendation/summary.md) |
| 8 | **Stochastic Beams and Where to Find Them: The Gumbel-Top-$k$ Trick for Sampling Sequences Without Replacement** | Wouter Kool et al.<br>(ICML 2019) | Gumbel-Top-$k$ Trick、Stochastic Beam Search、重複のない高速多様スレートサンプリング | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Stochastic%20Beams%20and%20Where%20to%20Find%20Them:%20The%20Gumbel-Top-k%20Trick/summary.md) |
| 9 | **Reinforcement Learning for Slate-based Recommender Systems: A Tractable Decomposition and Practical Methodology** (SlateQ) | Eugene Ie et al.<br>(IJCAI 2019 / YouTube) | スレート強化学習の価値分解 (SlateQ)、長期エンゲージメント（LTV）最大化、本番YouTube適用 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Reinforcement%20Learning%20for%20Slate-based%20Recommender%20Systems:%20A%20Tractable%20Decomposition%20and%20Practical%20Methodology/summary.md) |
| 10 | **Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness** | Harrie Oosterhuis<br>(SIGIR 2021 Best Paper) | Plackett–Luceモデルの高速・低分散勾配最適化 (PL-Rank)、公平性・多様性の直接学習 | [📄 summary.md](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Computationally%20Efficient%20Optimization%20of%20Plackett-Luce%20Ranking%20Models%20for%20Relevance%20and%20Fairness/summary.md) |

---

## 📖 総合技術解説

- **[Plackett–Luceモデルとレコメンドの出力多様性](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/plackett_luce_diversity.md)**
  - Plackett–Luce モデルの数理的基礎（非復元抽出メカニズム）
  - 出力多様性におけるメリットと IIA 仮定の限界（赤バス・青バス問題）
  - 原著論文から DPP・強化学習までの全体発展史
