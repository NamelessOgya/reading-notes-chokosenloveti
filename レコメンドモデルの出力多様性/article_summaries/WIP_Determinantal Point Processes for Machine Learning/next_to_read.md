# 次に読むべき論文 (Next to Read)

本モノグラフ『**Determinantal Point Processes for Machine Learning**』(Alex Kulesza, Ben Taskar, 2012) を基礎として推薦システム・深層学習へと発展した重要文献の一覧です。

---

## 1. 推薦システムにおける超高速 DPP 実装（本番適用）

### 📄 Fast Greedy MAP Inference for Determinantal Point Processes to Improve Recommendation Diversity
- **著者**: Laming Chen, Guoxin Zhang, Eric Zhou (Hulu)
- **発表**: NeurIPS 2018
- **概要**: 
  DPP の最大の課題であった計算コストに対し、コレスキー分解の逐次更新（Sherman-Morrison 公式）を用いることで、大規模候補集合からの Greedy MAP 推論をミリ秒単位（劇的な高速化）に短縮し、Hulu の本番動画推薦システムに DPP を導入した超有名論文。
- **読む理由**: DPP を実際の商用推薦エンジンの推論パイプライン（ミリ秒レイテンシ）に組み込む実装テクニックを学ぶため。

---

## 2. 確率的ランキング・スレート強化学習との統合

### 📄 Practical Diversified Recommendations on Large Scale with Determinantal Point Processes
- **著者**: Mark Wilhelm et al. (Google / YouTube)
- **発表**: WWW 2018
- **概要**:
  YouTube などの大規模検索・推薦基盤において、ユーザーの過去の視聴履歴から動的にカーネル行列を構成し、多様な動画スレートを生成する実用システム設計。
- **読む理由**: 大規模ユーザーログから DPP カーネルをエンドツーエンドで学習・提供するアーキテクチャを理解するため。

---

## 3. 本トピックの関連論文まとめ

- **[Review of Individual Choice Behavior: A Theoretical Analysis](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Review%20of%20Individual%20Choice%20Behavior:%20A%20Theoretical%20Analysis/summary.md)** (Gérard Debreu, 1960)
- **[Modeling the Choice of Residential Location (Nested Logit)](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Modeling%20the%20Choice%20of%20Residential%20Location/summary.md)** (Daniel McFadden, 1978)
- **[Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness (PL-Rank)](file:///Users/masashiueno/%E6%A5%AD%E7%95%8C%E3%81%BE%E3%81%A8%E3%82%81%E6%96%87%E6%9B%B8/%E3%83%AC%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%89%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%87%BA%E5%8A%9B%E5%A4%9A%E6%A7%98%E6%80%A7/article_summaries/Computationally%20Efficient%20Optimization%20of%20Plackett-Luce%20Ranking%20Models%20for%20Relevance%20and%20Fairness/summary.md)** (Harrie Oosterhuis, SIGIR 2021)
