# 次に読むべき論文 (Next to Read)

本論文『**Off-policy evaluation for slate recommendation**』(Adith Swaminathan et al., NeurIPS 2017) を引用している、または本論文の課題・手法を発展させている重要論文の一覧です。

---

## 1. スレート強化学習への展開（第4弾対象論文）

### 📄 Reinforcement Learning for Slate-based Recommender Systems: A Tractable Decomposition and Practical Methodology (SlateQ)
- **著者**: Eugene Ie, Vihan Jain, Jing Wang, Sanmit Narvekar, Rifat Saleh, Arjun Wu, Craig Boutilier
- **発表**: IJCAI 2019 (Google Research / YouTube)
- **概要**: 
  スレート推薦における組み合わせ爆発の課題に対し、ユーザーの選択モデル（Plackett–Luce や Multinomial Logit）を仮定して、スレート全体の長期価値（Q値）を各アイテムの価値の期待値として分解し、実用的な強化学習（TD学習/Q学習）を実現した研究。
- **読む理由**: スレートオフライン評価から、長期エンゲージメント（LTV）を最大化するスレート強化学習への自然な拡張を学ぶため。

---

## 2. 逐次ユーザー行動モデルとの統合

### 📄 Counterfactual Evaluation of Slate Recommendations with Sequential User Behavior
- **著者**: James McInerney, Brian Brost, Praveen Chandar, Rishabh Mehrotra, Benjamin Carterette
- **発表**: ACM RecSys 2020 (Spotify)
- **概要**:
  スレート推薦において、ユーザーがリストを上から順に閲覧して途中で離脱するカスケード行動（Cascade Model）を明示的に組み込み、PI 推定量よりもさらに分散の小さい反実仮想評価（Counterfactual Evaluation）を提案しています。
- **読む理由**: スレート推薦の実環境におけるユーザー心理・行動バイアスをモデルに取り入れる手法を理解するため。

---

## 3. 反実仮想 LTR との統合

### 📄 Unifying Online and Counterfactual Learning to Rank
- **著者**: Harrie Oosterhuis, Maarten de Rijke
- **発表**: ACM WSDM 2021
- **概要**:
  ログデータからの反実仮想学習（OPE）とオンラインでの適応的バンディット探索をシームレスに統合し、バイアスを補正しながら継続的にランキングモデルを更新するフレームワークを提案しています。
- **読む理由**: オフポリシー評価を実サービスの継続学習ループに組み込むための実践的設計を把握するため。

---

## 4. コンビナトリアルバンディット推定量としての理論的発展

### 📄 Optimal Off-Policy Evaluation from Multiple Logging Policies in Slate Bandits
- **著者**: Nathan Kallus, Masatoshi Uehara et al.
- **発表**: NeurIPS 2021 / ICML
- **概要**:
  複数の異なるログ方策から得られた不均一なログデータに対して、効率的影響関数（Efficient Influence Function）を用いて漸近有効性（最小分散）を達成するスレート推定量。
- **読む理由**: PI 推定量を超える究極的な分散削減の数理理論を把握するため。
