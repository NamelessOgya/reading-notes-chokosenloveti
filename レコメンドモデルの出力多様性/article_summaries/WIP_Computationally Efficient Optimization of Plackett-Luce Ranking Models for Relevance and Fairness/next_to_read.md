# 次に読むべき論文 (Next to Read)

本論文『**Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness**』(Harrie Oosterhuis, SIGIR 2021) を引用している、または本論文の課題・手法を発展させている重要論文の一覧です。

---

## 1. 直接の発展・フォローアップ論文

### 📄 Learning-to-Rank at the Speed of Sampling: Plackett-Luce Gradient Estimation With Minimal Computational Complexity
- **著者**: Harrie Oosterhuis
- **発表**: ACM SIGIR 2022
- **概要**: 
  本論文（SIGIR 2021）の著者自身による直接の後続研究。本論文で提案された PL-Rank-2 の計算量 $\mathcal{O}(N \cdot K \cdot |\mathcal{D}|)$ をさらに削減し、Gumbelサンプリング（ソート）の計算量と同等レベルである $\mathcal{O}(|\mathcal{D}| \log |\mathcal{D}|)$ にまで極小化した **PL-Rank-3** アルゴリズムを提案しています。PLモデルの最適化を現代の決定論的ソートと完全に同等の速度で実行可能にした決定版研究です。
- **読む理由**: PL-Rankの最終的な到達点と、さらなる高速化アルゴリズムの数理展開を理解するため。

---

## 2. 公平性・多様性の拡張研究

### 📄 Optimizing Group-Fair Plackett-Luce Ranking Models for Relevance and Ex-Post Fairness
- **著者**: Sravanthi Gorantla, Amit Deshpande, Anand Louis
- **発表**: arXiv / FAccT 2023
- **概要**:
  PLモデルを用いてランキングを生成する際、アイテムの属性グループ（性別、カテゴリ、マイノリティ等）に対する公平性制約（Group Fairness）と、生成された個々のリストにおける事後公平性（Ex-Post Fairness）を同時に満たすための最適化手法を提案しています。
- **読む理由**: PLモデルを推薦システムのカテゴリ多様性やグループ公平性に具体的に適用する実践的アプローチを学ぶため。

### 📄 Probabilistic Permutation Graph Search: Black-box Optimization for Fairness in Ranking
- **著者**: Ali Vardasbi, Harrie Oosterhuis, Maarten de Rijke
- **発表**: ACM SIGIR 2022
- **概要**:
  微分不可能な複雑な公平性・多様性指標に対して、確率的順列グラフ（Permutation Graph）探索を用いたブラックボックス最適化手法を提案しています。PLモデル等の確率的ランキング方策における探索効率を高める枠組みを提供しています。
- **読む理由**: 単純な露出格差以外の非線形・複雑な多様性目的関数を最適化する手法を把握するため。

---

## 3. オフポリシー評価・傾向スコア推定の発展

### 📄 Sample-Free Almost-Exact Estimation of Plackett-Luce Propensities for Off-Policy Ranking
- **著者**: Philipp Knyazev, Alexander Tuzhilin et al.
- **発表**: ACM CIKM / WebConf 2024
- **概要**:
  推薦システムにおけるオフポリシー評価（Inverse Propensity Scoring: IPS 等）を行う際、Plackett–Luceモデルによる推薦確率（傾向スコア）をサンプリングなしで準厳密かつ高速に推定する数学的アルゴリズムを提案しています。
- **読む理由**: オンライン推薦ログから多様性・公平性モデルをオフライン評価・学習する際の基盤技術を習得するため。
