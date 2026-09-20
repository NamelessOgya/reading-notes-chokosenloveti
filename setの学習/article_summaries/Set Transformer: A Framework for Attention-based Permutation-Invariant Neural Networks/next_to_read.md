# 次に読むべき関連・後続論文（Next to Read）

本論文『**Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks**』（Lee et al., ICML 2019）は、集合構造データに対してアテンション機構と誘起点（Inducing Points）を導入し、置換不変性・置換同変性を保証しながら計算量を線形化（$\mathcal{O}(nm)$）した先駆的研究です。  
本論文の知見を発展させた研究、および異なる視点から集合・構造学習にアプローチした重要論文を以下に列挙します。

---

## 1. 潜在ボトルネックと反復アテンションへの発展
- **論文名:** [Perceiver: General Perception with Iterative Attention](https://arxiv.org/abs/2103.03206)
- **著者 / 発表:** Andrew Jaegle, Felix Gimeno, Andrew Brock, Oriol Vinyals, Andrew Zisserman, Joao Carreira (DeepMind / ICML 2021)
- **関係性と発展ポイント:**
  - Set Transformer の **ISAB（誘起点との Cross-Attention）** および **PMA（シードベクトルによる集約）** と同系統の「小さな固定次元の潜在配列（Latent Array）が、数万〜数十万の入力要素に Cross-Attention を行うことで二乗計算量を回避する」という設計思想を極限まで洗練。
  - 点群だけでなく、高解像度画像、音声、動画、ポイントクラウドなど、あらゆるモダリティに対してアーキテクチャを変更せずに直接適用できる汎用知覚モデルへと発展させました。

---

## 2. オブジェクト中心表現とスロット競合への応用
- **論文名:** [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055)
- **著者 / 発表:** Francesco Locatello, Dirk Weissenborn, Thomas Unterthiner, Aravindh Mahendran, Georg Heigold, Jakob Uszkoreit, Alexey Dosovitskiy, Thomas Kipf (Google Research, Brain Team / NeurIPS 2020)
- **関係性と発展ポイント:**
  - PMA のシードベクトルと同様に、交換可能な複数の「スロット（Slots）」を用意し、入力特徴マップに対して反復的かつ要素間で競合する Softmax（Key方向ではなく Query/スロット方向への正規化）を行うことで、画像や動画から個別の物体表現（Object Slots）を教師なしで分解・獲得する手法を確立しました。

---

## 3. 「集合を出力する」逆タスクへの拡張
- **論文名:** [Deep Set Prediction Networks](https://arxiv.org/abs/1906.06565) (DSPN)
- **著者 / 発表:** Yan Zhang, Jonathon Hare, Adam Prügel-Bennett (NeurIPS 2019)
- **関係性と発展ポイント:**
  - Set Transformer が「集合を入力して特徴や数値を予測する」のに対し、DSPN は「画像や潜在ベクトルを入力して、要素数が可変で順序のない集合を出力する（Set Prediction）」逆問題に挑んだ研究。
  - 置換不変なエンコーダを用いて生成途中の集合を評価し、勾配降下法（内側の最適化）によって集合の要素を逐次生成・配置するアーキテクチャを提案しています。

---

## 4. 幾何学的点群処理への特化発展
- **論文名:** [Point Transformer](https://arxiv.org/abs/2012.09688)
- **著者 / 発表:** Hengshuang Zhao, Li Jiang, Jiaya Jia, Philip Torr, Vladlen Koltun (ICCV 2021 Oral)
- **関係性と発展ポイント:**
  - Set Transformer は大域的な全対全または誘起点経由のアテンションを扱いましたが、3次元点群（Point Cloud）の幾何学的性質に特化させ、3次元ユークリッド空間上の局所 $k$ 近傍（$k$-NN）に対するベクトルアテンション（スカラー内積ではなくチャネルごとに重みを持つアテンション）を導入。
  - 局所的な幾何特徴と位置オフセットのエンコードにより、3次元セグメンテーションや分類で当時の世界最高峰精度（SOTA）を達成しました。

---

## 5. 深層化に伴う学習安定性と表現力の改善
- **論文名:** [Equivariant Set Transformers / ST++: Stabilizing Deep Set Transformers](https://arxiv.org/abs/2202.04018)
- **著者 / 発表:** S. Kim et al. (ICLR / NeurIPS)
- **関係性と発展ポイント:**
  - Set Transformer をより深い層（Deep architecture）へと拡張した際に生じる、アテンション重みの集中（Rank collapse）や勾配消失の課題を分析。
  - 集合専用の正規化層（Set Norm）や置換同変な残差接続を提案し、大規模データセットにおける表現力と学習の安定性を大幅に改善しました。
