# 次に読むべき関連・後続論文（Next to Read）

本論文『**Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation**』（Bengio et al., NeurIPS 2021: 初出 GFlowNet）は、離散構造の生成をフローネットワークの保存則として定式化し、報酬関数に比例した確率で多様な候補集合（Diverse Candidate Set）を直接サンプリングする革新的理論を打ち立てました。  
本手法の学習アルゴリズムを改良した研究、理論的基礎を拡張した研究、および生物・材料・推論へと応用した重要論文を以下に列挙します。

---

## 1. 軌跡バランス（Trajectory Balance）による学習の革新
- **論文名:** [Trajectory Balance: Improved Credit Assignment in GFlowNets](https://arxiv.org/abs/2201.13259)
- **著者 / 発表:** Nikolay Malkin, Moksh Jain, Emmanuel Bengio, Chen Sun, Yoshua Bengio (NeurIPS 2022)
- **関係性と発展ポイント:**
  - 初出 GFlowNet の「Flow Matching（局所フロー保存則）」損失は、中間ノードごとの流入・流出を予測するため勾配の分散が大きく、長い軌跡において学習が不安定になる課題がありました。
  - 本研究は、軌跡全体の前向き確率 $P_F(\tau)$ と後ろ向き確率 $P_B(\tau)$ の比を分配関数 $Z$ および報酬 $R(x)$ と一致させる「Trajectory Balance (TB) 損失」を提案。学習速度とスケーラビリティを劇的に向上させ、現在の GFlowNet の標準目的関数となりました。

---

## 2. GFlowNet の包括的理論基盤（モノグラフ）
- **論文名:** [GFlowNet Foundations](https://arxiv.org/abs/2111.09266)
- **著者 / 発表:** Yoshua Bengio, Tristan Deleu, Edward J. Hu, Salem Lahlou, Mo Tiwari, Emmanuel Bengio (JMLR 2023)
- **関係性と発展ポイント:**
  - GFlowNet の数学的基盤（マルコフ連鎖、測度論、変分推論、強化学習との等価性、エントロピー正則化との関係など）を体系的に証明・詳述した集大成的な理論論文です。

---

## 3. 因果グラフ構造学習（Bayesian Structure Learning）への拡張
- **論文名:** [Bayesian Structure Learning with Generative Flow Networks](https://arxiv.org/abs/2202.13903)
- **著者 / 発表:** Tristan Deleu, António Góis, Chris Emezue, Mansi Rankawat, Simon Lacoste-Julien, Stefan Bauer, Yoshua Bengio (UAI 2022 Best Paper Runner-up)
- **関係性と発展ポイント:**
  - 因果推論における有向非巡回グラフ（DAG）の事後分布 $P(G|D)$ からのサンプリング問題に GFlowNet を適用。
  - 非巡回性を保証しながらエッジを1本ずつ追加していく生成プロセスを定義し、マルコフ等価クラスを超えた多様な因果グラフのサンプリングを実現しました。

---

## 4. 生物学的配列設計（DNA / RNA / ペプチド）への展開
- **論文名:** [Biological Sequence Design with GFlowNets](https://arxiv.org/abs/2203.04115)
- **著者 / 発表:** Moksh Jain et al. (ICML 2022)
- **関係性と発展ポイント:**
  - 低分子化合物から、抗体・アプタマー・AMP（抗菌ペプチド）などの長鎖配列設計へと応用を拡大。
  - 実験室でのハイスループット評価（バッチスクリーニング）に耐えうる高活性かつ多様な配列集合の自動生成を実証しました。
