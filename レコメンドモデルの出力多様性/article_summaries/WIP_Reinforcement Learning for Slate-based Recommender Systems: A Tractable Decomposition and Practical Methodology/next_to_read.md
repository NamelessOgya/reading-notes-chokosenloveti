# 次に読むべき論文 (Next to Read)

本論文『**Reinforcement Learning for Slate-based Recommender Systems: A Tractable Decomposition and Practical Methodology (SlateQ)**』(Eugene Ie et al., IJCAI 2019) を引用している、または本論文の手法を発展させている重要論文の一覧です。

---

## 1. 長期ユーザー満足度と制約付きマッチングへの拡張

### 📄 Optimizing Long-term User Satisfaction in Recommender Systems: A Constrained Matching Approach
- **著者**: Martin Mladenov, Chih-wei Hsu, Vihan Jain, Eugene Ie, Christopher Colby, Nicolas Mayoraz, Hubert Pham, Craig Boutilier
- **発表**: NeurIPS 2020 (Google Research)
- **概要**: 
  SlateQ の後続研究。スレート推薦において単一のエンゲージメント指標だけでなく、推薦の多様性・公平性・エコシステムの健全性（クリエイター保護）といった複数制約を満たしながら、長期満足度を最適化する制約付きマッチング（Constrained Matching）手法を提案しています。
- **読む理由**: SlateQの長期価値最大化を、出力多様性やプラットフォーム全体の健全性制約と両立させる高度な最適化手法を理解するため。

---

## 2. 確率的スレートバンディットと探索の高度化

### 📄 Variational Slate Bandits
- **著者**: Guy Lorberbom, Daniel Haziza, Chen Yanover, Chris Maddison, Tamir Hazan
- **発表**: NeurIPS 2021
- **概要**:
  スレート推薦における組み合わせ探索と多様性獲得を、変分ベイズ推論（Variational Inference）と Gumbel サンプリングを用いて効率化する確率的スレートバンディット手法。
- **読む理由**: SlateQにおける探索（Exploration）をよりベイズ的な不確実性モデリングで洗練させるアプローチを学ぶため。

---

## 3. シーケンシャル推薦と関係性モデリングの統合

### 📄 Sequential Recommendation with Latent Relations and Slate Reinforcement Learning
- **著者**: Zhengxuan Wu, Xiangnan He et al.
- **発表**: ACM RecSys 2021
- **概要**:
  アイテム間の補完関係や代替関係（多様性）を潜在グラフとして表現し、SlateQ の強化学習フレームワークに組み込むことで、より長期的なシーケンス最適化を実現した研究。
- **読む理由**: スレート内のアイテム間相互作用（コンテキスト効果）をより精緻にモデル化する手法を把握するため。

---

## 4. 確率的ランキングモデル（Plackett–Luce）の直接最適化

### 📄 Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness (PL-Rank)
- **著者**: Harrie Oosterhuis
- **発表**: ACM SIGIR 2021 (Best Paper Award)
- **概要**:
  SlateQ が依拠するユーザー選択モデル（Plackett–Luce）をベースに、オフラインでの直接勾配計算を劇的に効率化し、多様性と公平性をエンドツーエンドで最適化するアルゴリズム。
- **読む理由**: 強化学習アプローチ（SlateQ）と LTR 方策勾配法（PL-Rank）の共通点と相違点を深く理解するため。
