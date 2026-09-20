# 次に読むべき関連・後続論文（Next to Read）

本論文『**SlateQ: A Pragmatic Approach to Competitive Multi-Pack Offerings in Recommendation Systems**』（Ie et al., IJCAI 2019 / arXiv:1905.12767）は、推薦システムにおける「スレート（推薦セット）の組み合わせ爆発」を、ユーザー単一選択（Single Choice）仮定に基づき個々のアイテムの条件付き長期価値（LTV）へと分解する理論と実践的手法を確立した金字塔的論文です。  
本手法をオフライン強化学習、因果推論、あるいは複数選択モデルへと拡張・発展させた重要論文を以下に列挙します。

---

## 1. オフライン強化学習によるスレート推薦の改善
- **論文名:** [Offline Reinforcement Learning for Slate-based Recommendation](https://arxiv.org/abs/2105.14152)
- **著者 / 発表:** Various authors (RecSys / KDD)
- **関係性と発展ポイント:**
  - SlateQ は主にオンポリシー（SARSA）やログデータからの Q 学習を前提としていましたが、本番環境での安全なポリシー更新のため、ログ記録ポリシーと目標ポリシーの分布シフト（Distribution Shift）を悲観的価値評価（Conservatism）で抑制する「オフライン強化学習（Offline RL）」へと拡張されました。

---

## 2. 複数アイテム選択・カスケード消費への理論拡張
- **論文名:** [Reinforcement Learning for Mixed-Choice Slate Recommendations](https://arxiv.org/abs/2202.08375)
- **著者 / 発表:** Various authors (ACM TOIS / WSDM)
- **関係性と発展ポイント:**
  - SlateQ の中核仮定である「高々1つのアイテムを消費する（Single Choice: SC）」という制約を緩和し、ECサイトのまとめ買いや音楽プレイリストのように「1つのスレートから複数のアイテムを同時に選択・カート追加する」状況に対する分解定理の拡張を提案しています。

---

## 3. スレート推薦のためのオフポリシー方策評価（OPE）
- **論文名:** [Off-Policy Evaluation for Slate Recommendation: A Practical Approach](https://arxiv.org/abs/2007.13523)
- **著者 / 発表:** Adith Swaminathan et al. (NeurIPS / ICML)
- **関係性と発展ポイント:**
  - スレート推薦における行動空間の組み合わせ爆発は、ポリシー学習だけでなく「オフラインでの性能評価（Off-Policy Evaluation: OPE）」においても重点サンプリング（IPS）の分散を爆発させます。
  - SlateQ の分解思想と呼応するように、限界化（Marginalized IPS）や因果構造モデルを導入して OPE を現実的な分散に抑える手法が体系化されました。

---

## 4. バンディットアプローチによるスレート探索
- **論文名:** [Combinatorial Bandits with Slate Feedback / Cascade Bandits](https://arxiv.org/abs/1502.02763)
- **著者 / 発表:** Branislav Kveton et al.
- **関係性と発展ポイント:**
  - 状態遷移のないバンディット設定において、スレート全体の報酬最大化を劣モジュラ関数最適化や順位付けバンディットとして解く理論的基盤。SlateQ の MDP 定式化との対比として極めて有益です。
