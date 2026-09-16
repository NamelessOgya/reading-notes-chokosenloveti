# RETHINKING THE UNIFORMITY METRIC IN SELFSUPERVISED LEARNING

## 背景
自己教師あり学習（SSL）は、データ拡張に対して不変な表現を獲得することに長けており、下流タスクで高い性能を発揮する。Wang & Isola (2020)は、学習された表現の良さを測る指標として「Alignment（正例ペア間の近さ）」と「Uniformity（表現が単位超球面上に一様に分布しているか）」の2要素を提案した。しかし、従来のUniformity指標（$\mathcal{L_U}$）は、表現がすべて1点に潰れてしまう「Constant Collapse」は防げるものの、表現が一部の低次元の部分空間にのみ偏って潰れてしまう「Dimensional Collapse（次元の崩壊）」という現象に対しては感度が低く、この崩壊を完全には評価・防止できないという課題があった。

## 手法
著者らは、理想的なUniformity指標が満たすべき4つの要件（desiderata）を定義した上で、新たなUniformity指標を提案している。
具体的には、理想的なUniformityを持つ表現（単位超球面上の一様分布）の各次元が、高次元空間においてはゼロ平均の等方性ガウス分布 $\mathcal{N}(\bm{0}, \bm{I}_m/m)$ に漸近的に近似できることを利用している。学習された表現の分布を $\mathcal{N}(\bm{\mu}, \bm{\Sigma})$ と仮定したとき、この2つのガウス分布間の「2次Wasserstein距離（Quadratic Wasserstein Distance）」を新たな指標 $\mathcal{W}_{2}$ として導入した。
$\mathcal{W}_{2}$ は以下の数式で計算される。

$$ \mathcal{W}_{2} = \sqrt{\Vert \bm{\mu} \Vert^2_{2} + 1 + \mathrm{tr}(\bm{\Sigma}) -\frac{2}{\sqrt{m}} \mathrm{tr}(\bm{\Sigma}^{ \frac{1}{2}})} $$

この $\mathcal{W}_{2}$ は値が小さいほど理想の分布に近い（よりUniformである）ことを示す。そのため、$-\mathcal{W}_{2}$ を新しいUniformity損失項として扱い、既存の各種SSLモデル（MoCo v2, BYOL, BarlowTwins, Zero-CL）の目的関数に補助損失として組み込む手法を提案した。

## 結果

### 各種実験結果のテーブル書き起こし

**Table 1: CIFAR-10およびCIFAR-100における主要な結果**  
*(Proj.とPred.はそれぞれプロジェクターとプレディクターの隠れ層の次元数を示す。)*  
※本論文は新しい独立したモデルではなく**新しいUniformity損失項 $\mathcal{W}_{2}$ を提案**しているため、既存の4つの代表的SSLモデル（MoCo v2, BYOL, BarlowTwins, Zero-CL）に対して、**`+ $\mathcal{W}_{2}$`（太字）が付いている行が本論文の提案手法**です。従来のガウスカーネルUniformity損失（`+ $\mathcal{L_U}$`）やベースラインとの比較を行っています。

| Methods | Proj. | Pred. | CIFAR-10 <br> Acc@1$\uparrow$ | CIFAR-10 <br> Acc@5$\uparrow$ | CIFAR-10 <br> $\mathcal{W}_{2}\downarrow$ | CIFAR-10 <br> $\mathcal{L_U}\downarrow$ | CIFAR-10 <br> $\mathcal{L_A}\downarrow$ | CIFAR-100 <br> Acc@1$\uparrow$ | CIFAR-100 <br> Acc@5$\uparrow$ | CIFAR-100 <br> $\mathcal{W}_{2}\downarrow$ | CIFAR-100 <br> $\mathcal{L_U}\downarrow$ | CIFAR-100 <br> $\mathcal{L_A}\downarrow$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| SimCLR | 256 | \XSolidBrush | 89.85 | 99.78 | 1.04 | -3.75 | 0.47 | 63.43 | 88.97 | 1.05 | -3.75 | 0.50 |
| NNCLR | 256 | 256 | 87.46 | 99.63 | 1.23 | -3.12 | 0.38 | 54.90 | 83.81 | 1.23 | -3.18 | 0.43 |
| SimSiam | 256 | 256 | 86.71 | 99.67 | 1.19 | -3.33 | 0.39 | 56.10 | 84.34 | 1.21 | -3.29 | 0.42 |
| AlignUniform | 256 | \XSolidBrush | 90.37 | 99.76 | 0.94 | -3.82 | 0.51 | 65.08 | 90.15 | 0.95 | -3.82 | 0.53 |
| MoCo v2 (Baseline) | 256 | \XSolidBrush | 90.65 | 99.81 | 1.06 | -3.75 | 0.51 | 60.27 | 86.29 | 1.07 | -3.60 | 0.46 |
| MoCo v2 + $\mathcal{L_U}$ (従来損失) | 256 | \XSolidBrush | 90.98 | 99.67 | 0.98 | -3.82 | 0.53 | 61.21 | 87.32 | 0.98 | -3.81 | 0.52 |
| **MoCo v2 + $\mathcal{W}_{2}$ (提案手法)** | 256 | \XSolidBrush | 91.41 | 99.68 | 0.33 | -3.84 | 0.63 | 63.68 | 88.48 | 0.28 | -3.86 | 0.66 |
| BYOL (Baseline) | 256 | 256 | 89.53 | 99.71 | 1.21 | -2.99 | 0.31 | 63.66 | 88.81 | 1.20 | -2.87 | 0.33 |
| BYOL + $\mathcal{L_U}$ (従来損失) | 256 | \XSolidBrush | 90.09 | 99.75 | 1.09 | -3.66 | 0.40 | 62.68 | 88.44 | 1.08 | -3.70 | 0.51 |
| **BYOL + $\mathcal{W}_{2}$ (提案手法)** | 256 | 256 | 90.31 | 99.77 | 0.38 | -3.90 | 0.65 | 65.16 | 89.25 | 0.36 | -3.91 | 0.69 |
| BarlowTwins (Baseline) | 256 | \XSolidBrush | 91.16 | 99.80 | 0.22 | -3.91 | 0.75 | 68.19 | 90.64 | 0.23 | -3.91 | 0.75 |
| BarlowTwins + $\mathcal{L_U}$ (従来損失) | 256 | \XSolidBrush | 91.38 | 99.77 | 0.21 | -3.92 | 0.76 | 68.41 | 90.99 | 0.22 | -3.91 | 0.76 |
| **BarlowTwins + $\mathcal{W}_{2}$ (提案手法)** | 256 | \XSolidBrush | **91.43** | 99.78 | 0.19 | -3.92 | 0.76 | 68.47 | 90.64 | 0.19 | -3.91 | 0.79 |
| Zero-CL (Baseline) | 256 | \XSolidBrush | 91.35 | 99.74 | 0.15 | **-3.94** | 0.70 | 68.50 | 90.97 | 0.15 | -3.93 | 0.75 |
| Zero-CL + $\mathcal{L_U}$ (従来損失) | 256 | \XSolidBrush | 91.28 | 99.74 | 0.15 | **-3.94** | 0.72 | 68.44 | 90.91 | 0.15 | -3.93 | 0.74 |
| **Zero-CL + $\mathcal{W}_{2}$ (提案手法)** | 256 | \XSolidBrush | 91.42 | **99.82** | **0.14** | **-3.94** | 0.71 | **68.55** | **91.02** | **0.14** | **-3.94** | 0.76 |

**Table 2 & 3: 各モデルにおける設定パラメータ**

| Models | MoCo v2 | BYOL | BarlowTwins | Zero-CL |
| :--- | :---: | :---: | :---: | :---: |
| $\alpha_{\max}$ | 1.0 | 0.2 | 30.0 | 30.0 |
| $\alpha_{\min}$ | 1.0 | 0.2 | 0 | 30.0 |

*(Table 2とTable 3は完全に同一の内容であり、Wasserstein距離項に適用されるアニーリング重みパラメータを示している。)*

### 実験結果と考察

Table 1に示されるように、従来のUniformity Loss（$\mathcal{L_U}$）を追加するケースと比較して、Wasserstein距離に基づくUniformity Loss（$\mathcal{W}_{2}$）を各SSL手法（MoCo v2, BYOL, BarlowTwins, Zero-CL）の補助項として導入した場合の方が、CIFAR-10およびCIFAR-100の両方で一貫して高いDownstream性能（Acc@1）を達成していることがわかる。
手法に $\mathcal{W}_{2}$ を導入することで、Alignment項 ($\mathcal{L_A}$) はわずかに悪化（距離が上昇）する傾向がみられるものの、$\mathcal{W}_{2}$ 指標自体の改善が著しく、結果として特異値の低下を防いで表現の良さを底上げすることに寄与したと考察されている。

![Constant Collapse and Dimensional Collapse](./images/ConstantCollapse_DimensionalCollapse.png)
*(Figure: 従来のConstant Collapse（左）と、部分的に有用な空間が減ってしまうDimensional Collapse（右）の視覚的イメージ)*

![Singular Value Spectra Base](./images/CIFAR_100_SVD.png)
![MoCo v2 Dimensional Collapse](./images/MoCo_CIFAR_100_SVD.png)
![BYOL Dimensional Collapse](./images/BYOL_CIFAR_100_SVD.png)
*(Figure: CIFAR-100表現における共分散行列の特異値（Singular Value Spectra）に基づくDimensional Collapseの分析)*

Figureの特異値の降順分布グラフを用いたDimensional Collapseの分析から、非常に興味深い結果が得られている。ベースラインのモデル（特にMoCo v2やBYOL）では、学習後期のインデックスに該当する多数の次元で特異値がゼロに沈み込んでおり、極度の「Dimensional Collapse」を引き起こしていることが確認できる。
重要な点として、同じモデルに従来のUniformity Loss（$\mathcal{L_U}$）をヒューリスティックに追加しても、この次元の崩壊のカーブは殆ど改善されなかった。
一方で、提案手法である $\mathcal{W}_{2}$ をLossに追加した場合、特異値の分布曲線が高水準を保ったまま右へシフトしており、ゼロに潰れる次元が効果的かつ明確に減少している。これにより、提案指標 $\mathcal{W}_{2}$ はDimensional Collapseに対する感度が極めて高く、これをモデルの正則化として機能させることで、より広範な次元を有効活用できる（cos類似度などで情報損失の少ない）表現の獲得に成功していると筆者らは推論している。
