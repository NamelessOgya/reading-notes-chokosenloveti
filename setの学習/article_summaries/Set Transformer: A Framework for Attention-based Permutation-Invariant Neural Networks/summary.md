# Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks

**arXiv:** [1810.00825](https://arxiv.org/abs/1810.00825)  
**カンファレンス:** ICML 2019 (Proceedings of the 36th International Conference on Machine Learning)  
**著者:** Juho Lee$^1$, Yoonho Lee$^1$, Jungtaek Kim$^2$, Adam R. Kosiorek$^3$, Seungjin Choi$^2$, Yee Whye Teh$^3$  
（$^1$AITRICS, $^2$POSTECH, $^3$University of Oxford）  
**発表:** 2019年6月  
**対象タスク:** 集合構造データ処理（Set-structured Data）、点群分類（Point Cloud Classification）、メタクラスタリング（Amortized Clustering）、集合異常検知（Set Anomaly Detection）、複数インスタンス学習（Multiple Instance Learning）

---

## 背景

機械学習の多くの問題において、入力データは順序を持たない「集合（Set）」として与えられる。例えば、3次元空間内の点群データ（Point Cloud）、天文学における星の観測データ集合、クラスタリングにおけるデータ点集合、複数インスタンス学習（MIL）におけるパケットや画像の集合、さらにはメタ学習におけるタスク内サンプル集合などがこれに該当する。

集合を入力として扱うニューラルネットワークは、入力要素の順序をどのように並び替えても出力が変化しない **「置換不変性（Permutation Invariance）」**、あるいは要素ごとの変換において入力の並び替えと同じ順序で出力が並び替わる **「置換同変性（Permutation Equivariance）」** を厳密に満たさなければならない。

従来の代表的な集合処理アーキテクチャである **Deep Sets**（Zaheer et al., 2017）や **PointNet**（Qi et al., 2017）では、置換不変性を保証するために以下のような「独立変換＋固定プーリング」という設計を採用していた：
1. 各インスタンス $x_i$ を行ごとのフィードフォワードネットワーク（rFF: row-wise Feedforward）によって独立に特徴ベクトルへ射影する。
2. 全要素の特徴ベクトルに対し、平均（$\mathrm{mean}$）、総和（$\mathrm{sum}$）、最大値（$\mathrm{max}$）といった単純かつ固定的なプーリング関数を適用して集約する。

しかし、この従来設計には決定的な2つの欠点が存在していた：
- **要素間相互作用の欠落**:
  - 各インスタンスは集約段階まで互いに完全に独立して処理されるため、インスタンス間のペアワイズな類似度や高次の相互作用（Higher-order interactions）、文脈依存の関係性を捉えることができない。
- **固定プーリングの表現力不足**:
  - $\mathrm{sum}$ や $\mathrm{mean}$ などの固定的な集約操作は全要素を一様に圧縮してしまい、問題やコンテキストに応じた適応的な集約（例えば最大値の検出や複数クラスタ中心の抽出）が困難である。

これに対し著者らは、自然言語処理で革新をもたらした **アテンション機構（Multi-head Attention）** が「入力の順序に依存しない置換同変な操作」であることに着目し、要素間の相互作用を捉えつつ、集合集約までを一貫してアテンションで適応的に行う新しいフレームワーク **「Set Transformer」** を提案した。さらに、Self-Attention の計算量 $\mathcal{O}(n^2)$ が大規模な集合（$n \gg 1$）でボトルネックになる問題を解決するため、**誘起点（Inducing Points）** を用いて計算量を $\mathcal{O}(nm)$（$m \ll n$）へと線形化する革新的な構造を導入した。

---

## 手法

Set Transformer は、エンコーダとデコーダから構成される。エンコーダは置換同変（Permutation Equivariant）な層の積層によって入力集合を特徴集合へ変換し、デコーダは置換不変（Permutation Invariant）なプーリング層によって特徴集合を固定長の出力へ集約する。

![Diagrams of our attention-based set operations](./images/main.png)
*(a) Our model (Set Transformer の全体構成)*

---

### 1. Multihead Attention Block (MAB)

すべての基本ビルディングブロックとなるのが、Transformer のエンコーダブロックから位置エンコーディング（Positional Encoding）とドロップアウトを除去した **MAB (Multihead Attention Block)** である。

行ベクトルとして $n$ 個の要素を持つ行列 $X \in \mathbb{R}^{n \times d_q}$ と、$n_v$ 個の要素を持つ行列 $Y \in \mathbb{R}^{n_v \times d_v}$ を入力とする MAB は以下のように定義される：

$$ \mathrm{MAB}(X, Y) = \mathrm{LayerNorm}(H + \mathrm{rFF}(H)) $$

$$ H = \mathrm{LayerNorm}(X + \mathrm{Multihead}(X, Y, Y; \omega)) $$

ここで：
- $\mathrm{rFF}$ は各行（インスタンス）に独立・同一に適用されるフィードフォワードネットワーク。
- $\mathrm{LayerNorm}$ はレイヤー正規化。
- $\mathrm{Multihead}(Q, K, V; \omega)$ は $h$ 個のアテンションヘッドを持つマルチヘッドアテンションであり、$X$ が Query、$Y$ が Key および Value として機能する。

![MAB](./images/mab.png)
*(b) MAB (Multihead Attention Block)*

---

### 2. Set Attention Block (SAB)

集合内の要素同士の相互作用をモデル化するため、$X$ 自身を Query, Key, Value として MAB に入力する **SAB (Set Attention Block)** を定義する：

$$ \mathrm{SAB}(X) \coloneqq \mathrm{MAB}(X, X) $$

SAB は $n$ 個の要素からなる集合を受け取り、要素間のペアワイズな全対全（All-to-all）アテンションを計算して、同じサイズ $n$ の集合を出力する。SAB を複数層積層することで、3体間やそれ以上の高次相互作用（Higher-order interactions）をエンコードすることが可能となる。

![SAB](./images/fig_sab.png)
*(c) SAB (Set Attention Block)*

SAB の時間計算量は $\mathcal{O}(n^2)$ であり、要素数 $n$ が大きくなると計算コストが急増する。

---

### 3. Induced Set Attention Block (ISAB)

大規模な集合に対して二乗の計算量 $\mathcal{O}(n^2)$ を回避するため、ガウス過程のスパース近似手法などにヒントを得た **ISAB (Induced Set Attention Block)** を提案した。

ISAB では、モデル内部で保持・学習される $m$ 個の $d$ 次元パラメータベクトル $I \in \mathbb{R}^{m \times d}$ を **誘起点（Inducing Points）** として導入する。$m$ 個の誘起点を持つ ISAB は、2段階の MAB 操作として定義される：

$$ H = \mathrm{MAB}(I, X) \in \mathbb{R}^{m \times d} $$

$$ \mathrm{ISAB}_m(X) = \mathrm{MAB}(X, H) \in \mathbb{R}^{n \times d} $$

- **第1段階**: 誘起点 $I$（Query）が入力集合 $X$（Key/Value）を参照し、入力集合のグローバルな情報を凝縮した $m$ 個の特徴 $H$ を生成する（計算量 $\mathcal{O}(nm)$）。
- **第2段階**: 元の入力集合 $X$（Query）が凝縮特徴 $H$（Key/Value）を参照し、サイズ $n$ の出力集合を生成する（計算量 $\mathcal{O}(nm)$）。

これにより、計算量は $\mathcal{O}(n^2)$ から $\mathcal{O}(nm)$ へと削減される。通常 $m \ll n$（例えば $m=16$）に設定するため、実質的に要素数 $n$ に対する線形時間計算量を実現する。

![ISAB](./images/imab.png)
*(d) ISAB (Induced Set Attention Block)*

#### 置換同変性の性質
> **Property 1:** $\mathrm{SAB}(X)$ および $\mathrm{ISAB}_m(X)$ はともに入力 $X$ の置換に対して **置換同変（Permutation Equivariant）** である。すなわち、任意の置換行列 $P$ に対して $\mathrm{SAB}(PX) = P\,\mathrm{SAB}(X)$ が成立する。

---

### 4. Pooling by Multihead Attention (PMA)

エンコーダによって得られた特徴集合 $Z \in \mathbb{R}^{n \times d}$ を集約して固定サイズの表現を得るため、学習可能な $k$ 個のシードベクトル $S \in \mathbb{R}^{k \times d}$ を Query とする **PMA (Pooling by Multihead Attention)** を導入する：

$$ \mathrm{PMA}_k(Z) = \mathrm{MAB}(S, \mathrm{rFF}(Z)) \in \mathbb{R}^{k \times d} $$

- 多くの単一出力タスクでは $k=1$（1つのシードベクトル）が用いられる。
- 一方、メタクラスタリングのように複数の出力が要求されるタスクでは、$k$ 個のシードベクトルを用いて $k$ 個のクラスタパラメータを同時に出力できる。
- $k > 1$ の場合、集約後の $k$ 個の出力ベクトルの相関や競合（Explaining-away 効果）をモデル化するため、PMA の直後に SAB を適用する：

$$ H = \mathrm{SAB}(\mathrm{PMA}_k(Z)) $$

#### 置換不変性の性質
> **Proposition 1:** エンコーダ（SAB/ISAB の積層）が置換同変であり、デコーダの PMA が置換不変な変換であるため、**Set Transformer 全体は入力集合 $X$ の置換に対して厳密に置換不変（Permutation Invariant）** である。

---

### 5. 各モジュールの入出力次元と全体構造のまとめ

アテンション機構 $\mathrm{MAB}(Q, K)$ の最も重要な性質は、**「出力の行数（要素数）は、必ず Query（$Q$）の行数に一致する」** という点である（Key/Value $K$ の行数は集約されて消える）。

各ブロックの入出力テンソルの次元（Shape）の推移は以下のようになる：

#### ① 要素モジュールごとの入出力次元

| モジュール | 入力 | 内部パラメータ | 出力次元 | 役割・要素数の変化 |
| :--- | :--- | :--- | :--- | :--- |
| **MAB$(Q, K)$** | $Q \in \mathbb{R}^{n_q \times d}$<br>$K \in \mathbb{R}^{n_k \times d}$ | — | **$\mathbb{R}^{n_q \times d}$** | **Query の要素数 $n_q$ に揃う**（$K$ の要素数 $n_k$ はアテンションで集約される） |
| **SAB$(X)$** | $X \in \mathbb{R}^{n \times d}$ | — | **$\mathbb{R}^{n \times d}$** | $n \to n$（要素数不変。全要素同士の総当たり比較） |
| **ISAB$_m(X)$** | $X \in \mathbb{R}^{n \times d}$ | 誘起点 $I \in \mathbb{R}^{m \times d}$ | **$\mathbb{R}^{n \times d}$** | $n \to m \to n$（要素数不変。$m$ 個の代表ハブを介して線形化）<br>・$H = \mathrm{MAB}(I, X) \in \mathbb{R}^{m \times d}$ （$n \to m$ へ集約）<br>・$\mathrm{MAB}(X, H) \in \mathbb{R}^{n \times d}$ （$m \to n$ へ復元） |
| **PMA$_k(Z)$** | $Z \in \mathbb{R}^{n \times d}$ | シード $S \in \mathbb{R}^{k \times d}$ | **$\mathbb{R}^{k \times d}$** | **$n \to k$ に集約（プーリング）**。<br>学習可能な $k$ 個の質問（Query）を投げ、$n$ 個の可変長集合を目的の固定サイズ $k$ 個に集約する |

---

#### ② 全体パイプライン（Encoder $\to$ Decoder）の流れ

```
[ 入力集合 X ]
  │  Shape: (n, d_x)   ※ 要素数 n はデータごとに異なっていてもよい（可変長）
  ▼
【Encoder】: SAB または ISAB_m の積層 (Permutation Equivariant)
  │  Shape: (n, d)     ※ 各要素が他の要素の情報を取り込みつつ、要素数 n をそのまま維持
  ▼  特徴集合 Z ∈ ℝ^(n × d)
【Decoder】
  │
  ├─ 1. PMA_k(Z) = MAB(S, rFF(Z))
  │     Query: S ∈ ℝ^(k × d), Key/Value: Z ∈ ℝ^(n × d)
  │     Shape: (k, d)  ★ ここで要素数 n が消失し、固定の k 個に集約（プーリング）される！
  │
  ├─ 2. SAB(PMA_k(Z))
  │     Shape: (k, d)  ※ 出力された k 個の表現同士の相互関係（競合・重複排除）を調整
  │
  └─ 3. rFF(...)
        Shape: (k, d_y) ※ 最終タスクの次元（クラス確率、クラスタ平均・分散など）へ射影
  ▼
[ 最終出力 Y ]
  Shape: (k, d_y)
  ・k=1 の場合: (1, d_y) → 集合全体の集約値（文字数予測、回帰値、分類ラベルなど）
  ・k>1 の場合: (k, d_y) → k 個の個別出力（4つのクラスタ中心パラメータなど）
```


---

## 結果

著者らは、Set Transformer の有効性と各モジュールの寄与を検証するため、5つの多様なタスクで実験を行った。ベースラインとして、rFF + Pooling（Deep Sets）、rFFp-mean/rFFp-max + Pooling（Deep Sets の置換同変拡張）、rFF + Dotprod（アテンションプーリング）などと比較している。

---

### 1. トイ問題: 最大値回帰（Maximum Value Regression）

実数の集合 $\{x_1, \dots, x_n\}$ が与えられたとき、その最大値 $\mathrm{max}(x_1, \dots, x_n)$ を予測する回帰タスク。損失関数には平均絶対誤差（MAE: $|p - \mathrm{max}(x)|$）を用いる。

#### Table 1: Mean absolute errors on the max regression task.
| Architecture | MAE |
| :--- | :---: |
| rFF + Pooling ($\mathrm{mean}$) | 2.133 $\pm$ 0.190 |
| rFF + Pooling ($\mathrm{sum}$) | 1.902 $\pm$ 0.137 |
| rFF + Pooling ($\mathrm{max}$) | **0.1355 $\pm$ 0.0074** |
| SAB + PMA (ours) | 0.2085 $\pm$ 0.0127 |

- **結果と考察**:
  - $\mathrm{mean}$ プーリングや $\mathrm{sum}$ プーリングは、全要素を一様に足し合わせてしまうため MAE が約 1.9〜2.1 と極めて大きな誤差を出している。
  - 一方、$\mathrm{max}$ プーリングはタスクの定義そのものが最大値であるため、エンコーダが恒等関数を学習するだけで完全な予測が可能であり、最も低い MAE（0.1355）を達成した。
  - 注目すべきは、**SAB + PMA（Set Transformer）が事前の最大値構造を与えられていないにもかかわらず、0.2085 という $\mathrm{max}$ プーリングに匹敵する極めて高い精度を自律的に学習できた** 点である。これは、アテンション機構が集合の中から最大要素を自発的に特定し、それに重みを集中させて集約できる柔軟性を持つことを実証している。

---

### 2. ユニーク文字数のカウント（Counting Unique Characters）

Omniglot データセット（1,623種類の文字、各20画像）から 6〜10 枚の画像をサンプリングして集合を作成し、その中に何種類のユニークな文字が含まれているかを予測するタスク。ポアソン回帰モデルを用い、予測されたポアソン分布の最頻値が実際の文字数と一致した頻度（Accuracy）を測定。

![Counting unique characters](./images/omni20.png)
*(Figure 2: Counting unique characters: Omniglot からサンプリングされた20枚の画像セットの例。この中に14種類の異なる文字が含まれている)*

#### Table 2: Accuracy on the unique character counting task.
| Architecture | Accuracy |
| :--- | :---: |
| rFF + Pooling | 0.4382 $\pm$ 0.0072 |
| rFFp-mean + Pooling | 0.4617 $\pm$ 0.0076 |
| rFFp-max + Pooling | 0.4359 $\pm$ 0.0077 |
| rFF + Dotprod | 0.4471 $\pm$ 0.0076 |
| rFF + PMA (ours) | 0.4572 $\pm$ 0.0076 |
| SAB + Pooling (ours) | 0.5659 $\pm$ 0.0077 |
| **SAB + PMA (ours)** | **0.6037 $\pm$ 0.0075** |

![Accuracy of ISAB_n + PMA](./images/isab_n.png)
*(Figure 3: 誘起点の数 $n$ に対する $\mathrm{ISAB}_n + \mathrm{PMA}$ の正解率の変化)*

- **結果と考察**:
  - エンコーダに要素間相互作用を持たないモデル（rFFベース）は、デコーダを工夫しても正解率 43%〜46% 程度にとどまる。ユニーク数を数えるには「画像Aと画像Bが同じ文字かどうか」を比較・照合する必要があるため、インスタンス独立な表現では本質的に限界がある。
  - エンコーダに SAB を導入すると正解率が **56.59%** に急上昇し、デコーダに PMA を組み合わせることで最高精度 **60.37%** に達した。
  - **Figure 3（誘起点数 $n$ の影響）**: $\mathrm{ISAB}_n + \mathrm{PMA}$ において、誘起点がわずか 1 個（$\mathrm{ISAB}_1$）であっても従来の rFF + Pooling を上回る性能を示し、誘起点の数 $n$ を増やすにつれて急速に精度が向上して SAB（全対全アテンション）の性能へと漸近していくことが確認された。

---

### 3. ガウス混合モデルによるメタクラスタリング（Amortized Clustering with MoG）

$k=4$ 個のガウス分布から生成された 2次元データ点集合（Synthetic）、および CIFAR-100 からサンプリングされた画像埋め込み集合（512次元）を入力とし、反復的な EM アルゴリズムを実行することなく、ニューラルネットワークの1パス推論で各クラスタのパラメータ $\{\pi_j, \mu_j, \sigma_j\}_{j=1}^4$ を直接予測するタスク。評価指標は対数尤度（LL）および Adjusted Rand Index（ARI）。

#### Table 3: Meta clustering results.
| Architecture | Synthetic: LL0/data | Synthetic: LL1/data | CIFAR-100: ARI0 | CIFAR-100: ARI1 |
| :--- | :---: | :---: | :---: | :---: |
| Oracle | -1.4726 | — | 0.9150 | — |
| rFF + Pooling | -2.0006 $\pm$ 0.0123 | -1.6186 $\pm$ 0.0042 | 0.5593 $\pm$ 0.0149 | 0.5693 $\pm$ 0.0171 |
| rFFp-mean + Pooling | -1.7606 $\pm$ 0.0213 | -1.5191 $\pm$ 0.0026 | 0.5673 $\pm$ 0.0053 | 0.5798 $\pm$ 0.0058 |
| rFFp-max + Pooling | -1.7692 $\pm$ 0.0130 | -1.5103 $\pm$ 0.0035 | 0.5369 $\pm$ 0.0154 | 0.5536 $\pm$ 0.0186 |
| rFF + Dotprod | -1.8549 $\pm$ 0.0128 | -1.5621 $\pm$ 0.0046 | 0.5666 $\pm$ 0.0221 | 0.5763 $\pm$ 0.0212 |
| SAB + Pooling (ours) | -1.6772 $\pm$ 0.0066 | -1.5070 $\pm$ 0.0115 | 0.5831 $\pm$ 0.0341 | 0.5943 $\pm$ 0.0337 |
| ISAB (16) + Pooling (ours) | -1.6955 $\pm$ 0.0730 | -1.4742 $\pm$ 0.0158 | 0.5672 $\pm$ 0.0124 | 0.5805 $\pm$ 0.0122 |
| rFF + PMA (ours) | -1.6680 $\pm$ 0.0040 | -1.5409 $\pm$ 0.0037 | 0.7612 $\pm$ 0.0237 | 0.7670 $\pm$ 0.0231 |
| SAB + PMA (ours) | -1.5145 $\pm$ 0.0046 | -1.4619 $\pm$ 0.0048 | 0.9015 $\pm$ 0.0097 | 0.9024 $\pm$ 0.0097 |
| **ISAB (16) + PMA (ours)** | **-1.5009 $\pm$ 0.0068** | **-1.4530 $\pm$ 0.0037** | **0.9210 $\pm$ 0.0055** | **0.9223 $\pm$ 0.0056** |

※ LL0/ARI0 はネットワーク直接出力値、LL1/ARI1 は出力値を初期値として EM を1ステップ更新した後の値。

![Clustering results for 10 test datasets](./images/ff.png)
![Clustering results for 10 test datasets](./images/sab_ff.png)
![Clustering results for 10 test datasets](./images/ff_sab.png)
![Clustering results for 10 test datasets](./images/sab.png)
*(Figure 4: 10個のテストデータセットに対するクラスタリング結果、クラスタ中心および共分散楕円。左上: rFF+Pooling, 右上: SAB+Pooling, 左下: rFF+PMA, 右下: Set Transformer (SAB+PMA))*

- **結果と考察**:
  - PMA の導入が劇的な効果をもたらした。CIFAR-100 において、Pooling を用いたモデルは ARI 0.53〜0.59 にとどまるが、rFF + PMA は **0.7612**、SAB + PMA は **0.9015**、さらに **ISAB (16) + PMA は 0.9210** に達し、EM を収束するまで回した Oracle（0.9150）をも上回る精度を達成した。
  - **なぜ ISAB (16) が完全な SAB より優れているのか？**: 著者らは、わずか 16 個の誘起点を通すボトルネック構造が、グローバルなデータ幾何構造の学習を促進するとともに、過学習に対する正則化（Regularization）および知識移転（Knowledge Transfer）として機能したためと考察している。
  - **Figure 4 の可視化**: rFF+Pooling（左上）は全クラスタ中心がデータ全体の平均付近に縮退してしまい分離に失敗しているのに対し、Set Transformer（右下）は 4 つのクラスタ中心と共分散楕円を美しく正確に分離・再現している。

---

### 4. 集合内異常検知（Set Anomaly Detection）

CelebA データセット（顔画像）からサンプリングした 8 枚の画像集合（共通する2つの属性を持つ正常画像 7 枚と、どちらの属性も持たない異常画像 1 枚）から、仲間外れの異常画像を特定するタスク。

![Sampled datasets for anomaly detection](./images/celeba.png)
*(Figure 5: サンプリングされたデータセットの例。各行が1つのセットであり、7枚の正常画像と1枚の異常画像（赤枠）で構成される。右端の列は正常画像が共通して持つ2つの属性を示す)*

#### Table 5: Meta set anomaly results.
| Architecture | Test AUROC | Test AUPR |
| :--- | :---: | :---: |
| Random guess | 0.5 | 0.125 |
| rFF + Pooling | 0.5643 $\pm$ 0.0139 | 0.4126 $\pm$ 0.0108 |
| rFFp-mean + Pooling | 0.5687 $\pm$ 0.0061 | 0.4125 $\pm$ 0.0127 |
| rFFp-max + Pooling | 0.5717 $\pm$ 0.0117 | 0.4135 $\pm$ 0.0162 |
| rFF + Dotprod | 0.5671 $\pm$ 0.0139 | 0.4155 $\pm$ 0.0115 |
| SAB + Pooling (ours) | 0.5757 $\pm$ 0.0143 | 0.4189 $\pm$ 0.0167 |
| rFF + PMA (ours) | 0.5756 $\pm$ 0.0130 | 0.4227 $\pm$ 0.0127 |
| **SAB + PMA (ours)** | **0.5941 $\pm$ 0.0170** | **0.4386 $\pm$ 0.0089** |

- **結果と考察**:
  - どの属性が共通しているかはセットごとに未知であるため、モデルは集合内の全画像を比較して「多数派の共通項」を推論し、「それに該当しない画像」を検出しなければならない。
  - SAB + PMA は、従来の全ベースラインを有意に上回る AUROC（0.5941）および AUPR（0.4386）を記録し、文脈内でのメタ推論能力の高さを示した。

---

### 5. 点群分類（Point Cloud Classification: ModelNet40）

ModelNet40 データセットを用い、3次元物体の点群（点数 $n \in \{100, 1000, 5000\}$）から物体カテゴリ（40クラス）を分類するタスク。点数が多いため $\mathcal{O}(n^2)$ の SAB ではなく $\mathcal{O}(nm)$ の ISAB（誘起点 $m=16$）を評価。

#### Table 4: Test accuracy for the point cloud classification task using 100, 1000, 5000 points.
| Architecture | 100 pts | 1000 pts | 5000 pts |
| :--- | :---: | :---: | :---: |
| rFF + Pooling (Zaheer et al., 2017) | — | 0.83 $\pm$ 0.01 | — |
| rFFp-max + Pooling (Zaheer et al., 2017) | 0.82 $\pm$ 0.02 | 0.87 $\pm$ 0.01 | **0.90 $\pm$ 0.003** |
| rFF + Pooling | 0.7951 $\pm$ 0.0166 | 0.8551 $\pm$ 0.0142 | 0.8933 $\pm$ 0.0156 |
| rFF + PMA (ours) | 0.8076 $\pm$ 0.0160 | 0.8534 $\pm$ 0.0152 | 0.8628 $\pm$ 0.0136 |
| ISAB (16) + Pooling (ours) | 0.8273 $\pm$ 0.0159 | **0.8915 $\pm$ 0.0144** | **0.9040 $\pm$ 0.0173** |
| **ISAB (16) + PMA (ours)** | **0.8454 $\pm$ 0.0144** | 0.8662 $\pm$ 0.0149 | 0.8779 $\pm$ 0.0122 |

- **結果と考察**:
  - 点数が少ない過酷な設定（100点）において、ISAB(16) + PMA が **84.54%** を達成し、ベースライン（79.51%〜82%）を大きく引き離した。情報量が乏しい状況ほど、疎な点同士の幾何学的相互作用をアテンションで補完する能力が真価を発揮する。
  - 点数が増加するにつれて（1000点、5000点）、点群自体の密度が十分高くなり個別の点同士の複雑な相互関係をモデル化する必要性が薄れるため、シンプルなプーリングとの差は縮まるが、ISAB(16) + Pooling は 5000点でも最高精度（90.40%）を維持した。
