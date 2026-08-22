# Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness

論文の背景, 手法, 結果の3項目でまとめます。

---

## 背景

検索エンジンやレコメンドシステムにおいて、ランキングモデルを最適化する **Learning-to-Rank (LTR)** は中核的な技術です。従来の LTR 手法はアイテムごとに予測スコアを割り当て、そのスコア順にソートしてランキングを決定論的に生成していました。しかし、ソート操作は微分不可能（Non-differentiable）であるため、NDCG や ERR などの離散的ランキング評価指標に対して勾配を直接計算することが困難でした。

この課題に対し、近年 **Plackett–Luce (PL) ランキングモデル**（確率的ランキングモデル）が大きな注目を集めています。PLモデルは、ソフトマックス選択を非復元抽出（Sampling without replacement）として逐次適用することで、ランキング全体の結合確率分布をモデル化します。
PLモデルには以下の優れた利点があります：
1. **探索（Exploration）と多様性**: 不確実性を確率分布として明示的に扱うため、オンラインLTRにおいて高い探索性能を発揮し、出力の多様性を担保できる。
2. **公平性（Fairness）の最適化**: 決定論的モデルと異なり、複数のアイテムに対してトップ表示される確率を均等・比例配分できるため、露出の公平性（Exposure-based Fairness）を直接扱える。

しかし、PLモデルを最適化する際の最大の障壁は**計算量（計算コストの爆発）**でした。
- PLモデルの期待報酬に対する真の勾配を計算するには、考えられるすべての順列（アイテム数 $D$ に対して $D!$ 通り）について総和をとる必要があり、理論的に計算不可能です。
- 実用上は REINFORCE アルゴリズム等に基づき、サンプリングされた $N$ 個のランキングからポリシー勾配（Policy Gradient）を推定しますが、高分散であるため収束に大量のサンプル（ $N \ge 1000$ ）を必要とし、計算時間が極めて膨大になるという深刻な欠点がありました。

本論文は、PLモデルとランキング評価指標の数理的構造を活用することで、勾配推定の計算量を劇的に削減し、高いサンプル効率と高速な最適化を実現する新しい最適化手法 **PL-Rank** を提案しています。

---

## 手法

本論文では、既存の Policy Gradient の課題を解消するために、3段階に分けて新しい勾配推定量（Placement Policy Gradient、PL-Rank-1、PL-Rank-2）を導出しています。

### 1. 問題設定と基本定式化

クエリ $q$ に対するアイテム $d \in \mathcal{D}$ の関連度を $\rho_{d} = P(R=1 \mid q, d)$ とし、ランク $k$ の重みを $\theta_{k}$ とします（例：DCG@K では $\theta_{k} = \frac{1}{\log_{2}(k+1)}$）。
長さ $K$ のランキング $y = [y_{1}, y_{2}, \dots, y_{K}]$ に対する期待関連度報酬 $\mathcal{R}(q)$ は以下で定義されます：

$$ \mathcal{R}(q) = \sum_{y \in \pi} \pi(y \mid q) \sum_{k=1}^{K} \theta_{k} \rho_{y_{k}} = \mathbb{E}_{y}\left[ \sum_{k=1}^{K} \theta_{k} \rho_{y_{k}} \right] $$

モデル $m(d) \in \mathbb{R}$ が各アイテムの対数スコアを出力するとき、PLモデルによるアイテム選択確率 $\pi(d \mid y_{1:k-1})$ およびランキング全体の生成確率 $\pi(y)$ は以下のように Softmax の積となります：

$$ \pi(d \mid y_{1:k-1}) = \frac{\exp(m(d)) \mathbb{I}[d \notin y_{1:k-1}]}{\sum_{d' \in \mathcal{D} \setminus y_{1:k-1}} \exp(m(d'))}, \quad \pi(y) = \prod_{k=1}^{K} \pi(y_{k} \mid y_{1:k-1}) $$

### 2. Gumbel-Softmax による高速サンプリング
PLモデルからのランキング生成は、各アイテムの対数スコア $m(d)$ に標準Gumbelノイズ $\gamma_{d} \sim \text{Gumbel}(0, 0)$ を加え、$\hat{m}_{d} = m(d) + \gamma_{d}$ の値でソートすることによって、$\mathcal{O}(|\mathcal{D}| \log |\mathcal{D}|)$ の計算量で高速にサンプリングできます。

### 3. Placement Policy Gradient（配置ポリシー勾配）
従来の基本 Policy Gradient では、ランキング全体の対数確率勾配 $\frac{\partial}{\partial m} \log \pi(y)$ にランキング全体の総報酬 $\sum_{k=1}^{K} \theta_{k} \rho_{y_{k}}$ を乗算していたため、1位のアイテムの貢献がそれ以降の無関係なアイテムの確率まで一様に押し上げてしまうという問題がありました。

ランク $k$ のアイテム $y_{k}$ による報酬はランク $k$ までの部分ランキング $y_{1:k}$ のみに依存することを利用し、期待値の線形性を変形することで以下の推定量が得られます：

$$ \frac{\partial}{\partial m} \mathcal{R}(q) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{k=1}^{K} \left[ \frac{\partial}{\partial m} \log \pi(y_{k}^{(i)} \mid y_{1:k-1}^{(i)}) \right] \left( \sum_{x=k}^{K} \theta_{x} \rho_{y_{x}^{(i)}} \right) $$

各ランク $k$ における選択確率の勾配に対し、「そのランク以降に得られる将来報酬（Following Reward）」のみを重み付けることで、分散を低減します。

### 4. PL-Rank-1（計算量効率化）
Placement Policy Gradient を自動微分フレームワーク（PyTorch等）で計算すると依然として計算負荷が高いため、PLモデルの Softmax の解析的微分：

$$ \frac{\partial}{\partial m} \pi(d \mid y_{1:k-1}) = \pi(d \mid y_{1:k-1}) \left( \frac{\partial}{\partial m} m(d) - \sum_{d' \in \mathcal{D}} \pi(d' \mid y_{1:k-1}) \frac{\partial}{\partial m} m(d') \right) $$

を代入して整理することで、アイテムごとの勾配として以下の **PL-Rank-1** 推定量を導出しました：

$$ \frac{\partial}{\partial m} \mathcal{R}(q) \approx \frac{1}{N} \sum_{d \in \mathcal{D}} \left[ \frac{\partial}{\partial m} m(d) \right] \sum_{i=1}^{N} \left( \sum_{k=\text{rank}(d, y^{(i)})}^{K} \theta_{k} \rho_{y_{k}^{(i)}} - \sum_{k=1}^{\text{rank}(d, y^{(i)})} \pi(d \mid y_{1:k-1}^{(i)}) \sum_{x=k}^{K} \theta_{x} \rho_{y_{x}^{(i)}} \right) $$

- **第1項（配置後報酬）**: アイテム $d$ が配置されたランク以降に得られた報酬の総和。
- **第2項（配置確率によるリスク）**: アイテム $d$ がその位置までに配置される確率によって、他のアイテムが押し出されて得られなくなる将来報酬（リスク）。

この式により、自動微分グラフを介さずに $\mathcal{O}(N \cdot K \cdot |\mathcal{D}|)$ の極めて軽量な計算量で直接勾配を計算可能になりました。

### 5. PL-Rank-2（サンプル効率の向上）
PL-Rank-1 では、サンプル数 $N$ が小さい場合、ある高関連度アイテム $d$ が一度もTop-$K$にサンプリングされないと負の重みを受けてしまう課題があります。そこで、期待報酬からアイテム $d$ 自体の直接報酬 $\theta_{k} \rho_{d}$ を明示的に分離して以下の **PL-Rank-2** を導出しました：

$$ \frac{\partial}{\partial m} \mathcal{R}(q) \approx \frac{1}{N} \sum_{d \in \mathcal{D}} \left[ \frac{\partial}{\partial m} m(d) \right] \sum_{i=1}^{N} \left( \sum_{k=\text{rank}(d, y^{(i)})+1}^{K} \theta_{k} \rho_{y_{k}^{(i)}} + \sum_{k=1}^{\text{rank}(d, y^{(i)})} \pi(d \mid y_{1:k-1}^{(i)}) \left( \theta_{k} \rho_{d} - \sum_{x=k}^{K} \theta_{x} \rho_{y_{x}^{(i)}} \right) \right) $$

PL-Rank-2 では、Top-$K$に選ばれなかったアイテムに対しても直接報酬とリスクの差分から正の勾配を与えることが可能になり、少ないサンプル数（ $N=10$ 等）でも極めて安定した学習が実現されます。

### 6. 公平性指標（Fairness）への拡張
露出（Exposure）に基づく公平性指標 $\mathcal{F}(q)$ に対しても、連鎖律 $\frac{\partial \mathcal{F}(q)}{\partial m} = \sum_{d} \frac{\partial \mathcal{F}(q)}{\partial \mathcal{E}_{d}} \frac{\partial \mathcal{E}_{d}}{\partial m}$ を適用することで、関連度 $\rho_{d}$ を $\frac{\partial \mathcal{F}(q)}{\partial \mathcal{E}_{d}}$ に置き換えるだけで全く同一の PL-Rank アルゴリズムにより公平性・多様性の最適化が可能です。

---

## 結果

3つの大規模公開ベンチマークデータセット（Yahoo! Webscope, MSLR-WEB30k, Istella）を用いて、各手法の性能・サンプル効率・計算時間を検証しました。

### 1. 完全転記テーブル

#### Table 1: 各サンプル数 $N$ における1エポックあたりの平均学習時間（分）
以下の表は、論文内の Table 1 の全データを省略なく転記したものです（括弧内は標準偏差）。

| データセット | 最適化手法 | $N=1$ | $N=10$ | $N=100$ | $N=1000$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Yahoo** | LambdaLoss | 2.48 (0.05) | 2.53 (0.04) | 3.06 (0.08) | 10.25 (0.53) |
| | Policy Gradient | 3.79 (0.09) | 3.80 (0.06) | 4.28 (0.15) | 8.27 (0.50) |
| | Placement P.G. | 3.83 (0.08) | 3.86 (0.05) | 4.42 (0.10) | 8.26 (0.44) |
| | **PL-Rank-1** | **2.45 (0.06)** | **2.49 (0.06)** | **2.82 (0.09)** | **5.70 (0.14)** |
| | PL-Rank-2 | 2.49 (0.06) | 2.52 (0.06) | 2.87 (0.08) | 6.22 (0.15) |
| **MSLR** | LambdaLoss | 2.73 (0.11) | 3.96 (0.59) | 36.36 (31.46) | 1669.59 (450.69) |
| | Policy Gradient | 3.30 (0.10) | 3.45 (0.10) | 5.25 (0.35) | 24.20 (2.77) |
| | Placement P.G. | 3.32 (0.17) | 3.42 (0.13) | 5.27 (0.41) | 23.97 (2.68) |
| | **PL-Rank-1** | **2.16 (0.14)** | **2.28 (0.13)** | **3.34 (0.13)** | **18.48 (2.10)** |
| | PL-Rank-2 | 2.19 (0.15) | 2.35 (0.17) | 3.45 (0.06) | 21.10 (2.78) |
| **Istella** | LambdaLoss | 3.53 (0.12) | 4.50 (0.10) | 27.81 (19.20) | 142.74 (16.25) |
| | Policy Gradient | 4.10 (0.17) | 4.51 (0.16) | 8.74 (0.26) | 44.29 (2.17) |
| | Placement P.G. | 4.08 (0.17) | 4.51 (0.18) | 8.72 (0.23) | 44.74 (2.55) |
| | **PL-Rank-1** | **3.01 (0.12)** | **3.27 (0.09)** | **6.90 (0.19)** | **39.80 (2.65)** |
| | PL-Rank-2 | 3.04 (0.13) | 3.31 (0.10) | 7.02 (0.14) | 40.64 (3.96) |

---

#### Table 2: 同一計算時間最適化後の DCG@5 比較
以下の表は、動的サンプル数更新（Dynamic $N$）を用いて同一時間最適化した際の DCG@5 の比較結果です（$\triangledown$ は PL-Rank-2 に対する有意な劣後 $p < 0.01$ を示す）。

| 項目 / 手法 | Yahoo | MSLR | Istella |
| :--- | :--- | :--- | :--- |
| **最適化時間（分）** | 100分 | 120分 | 200分 |
| LambdaLoss | 11.11$^{\triangledown}$ (0.05) | 7.80$^{\triangledown}$ (0.09) | 18.75$^{\triangledown}$ (0.10) |
| Policy Gradient | 11.03$^{\triangledown}$ (0.04) | 8.21$^{\triangledown}$ (0.07) | 18.75$^{\triangledown}$ (0.10) |
| Placement Policy Gradient | 11.31$^{\triangledown}$ (0.02) | 8.33$^{\triangledown}$ (0.04) | 19.23$^{\triangledown}$ (0.06) |
| PL-Rank-1 | 11.38$^{\triangledown}$ (0.03) | **8.39**$^{-}$ (0.04) | 19.31$^{\triangledown}$ (0.05) |
| **PL-Rank-2** | **11.42**$^{-}$ **(0.02)** | **8.39**$^{-}$ **(0.03)** | **19.38**$^{-}$ **(0.05)** |

---

### 2. 図版の引用と結果の考察

#### Figure 1: サンプル数 $N$ の違いによる学習曲線 (DCG@5 vs. Epoch)
以下は、異なるサンプル数（ $N=10, 100, 1000$ ）におけるエポックごとの DCG@5 の推移です。

| データセット | $N=10$ | $N=100$ | $N=1000$ |
| :---: | :---: | :---: | :---: |
| **Yahoo!** | ![Yahoo 10](./images/Webscope_C14_Set1_10samples.png) | ![Yahoo 100](./images/Webscope_C14_Set1_100samples.png) | ![Yahoo 1000](./images/Webscope_C14_Set1_1000samples.png) |
| **MSLR** | ![MSLR 10](./images/MSLR-WEB30k_10samples.png) | ![MSLR 100](./images/MSLR-WEB30k_100samples.png) | ![MSLR 1000](./images/MSLR-WEB30k_1000samples.png) |
| **Istella** | ![Istella 10](./images/istella_10samples.png) | ![Istella 100](./images/istella_100samples.png) | ![Istella 1000](./images/istella_1000samples.png) |

![凡例](./images/legend_samples.png)

- **考察**:
  - 基本 Policy Gradient はサンプル数への依存が著しく、$N=10$ では収束が著しく悪化し、$N=1000$ に至るまで最適性能に達しません。
  - 一方、**PL-Rank-2** は $N=10$ という極めて少ないサンプル数でも高いサンプル効率を発揮し、初期段階から優れた DCG@5 を達成しています。
  - $N \ge 100$ では PL-Rank-1, PL-Rank-2, Placement Policy Gradient のエポック単位の性能差は小さくなりますが、次の計算時間において圧倒的な差が生じます。

---

#### Figure 2: 実時間（分）ベースでの学習収束比較 (DCG@5 vs. Minutes Trained)
動的サンプル数戦略（ $N = 10 + 90 \cdot \frac{\text{epoch}}{40}$ ）を用いた実時間比較です。

| Yahoo! Webscope | MSLR-WEB30k | Istella |
| :---: | :---: | :---: |
| ![Yahoo Dynamic](./images/Webscope_C14_Set1_dynamic.png) | ![MSLR Dynamic](./images/MSLR-WEB30k_dynamic.png) | ![Istella Dynamic](./images/istella_dynamic.png) |

![凡例](./images/legend_dynamic.png)

- **考察**:
  - Table 1 に示されるように、PL-Rank は勾配計算の数式展開を簡略化したことで、Policy Gradient よりも1エポックあたりの計算時間が大幅に短縮されています。
  - その結果、同じ実時間（Minutes Trained）で比較した際、PL-Rank-1 および PL-Rank-2 は他の全ての手法を圧倒するスピードで高い DCG@5 に収束します。

---

#### Figure 3: 公平性指標（Disparity Error）の最適化推移
公平性指標（アイテム間の露出不均衡エラー）を目的関数とした場合の推移です。

![Fairness Dynamic](./images/fairness_Webscope_C14_Set1_dynamic.png)
![Fairness Legend](./images/legend_fairness_dynamic.png)

- **考察**:
  - PL-Rank-2 は関連度指標だけでなく、露出に基づく公平性（Fairness）や多様性の最適化においても、Policy Gradient と同等の安定性を維持しながら、極めて高速に不均衡誤差を低減できることが実証されました。

---

### 3. 筆者の考察と総括
1. **アルゴリズム特化型勾配計算の優位性**: 汎用的な自動微分に頼るのではなく、Plackett–Luceモデルとランキング指標の数理構造を利用して勾配式を解析的に展開・整理することで、計算複雑性を $\mathcal{O}(N \cdot K \cdot |\mathcal{D}|)$ に抑えつつ、劇的な高速化が達成できることを示しました。
2. **確率的ランキングモデルの実用化への道**: 計算コストの高さゆえに本番環境への適用が難しかったPLモデルを、決定論的モデルと同等以上の実用的な時間で訓練可能にし、推薦の多様性・公平性制御の普及に決定的な前進をもたらしました。
