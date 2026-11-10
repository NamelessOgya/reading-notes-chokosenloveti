# n次元（3次元以上）の変数変換とヤコビアン

## 結論（3行まとめ）

1. **3変数以上でも公式の形は2次元と同じで、$f_Y(y) = f_X\bigl(h(y)\bigr)\,\lvert J \rvert$ です。** 違いは、$J$ が $n \times n$ のヤコビ行列の行列式になることだけです。
2. **$\lvert J \rvert$ は「$n$ 次元の体積の拡大率」です。** 1次元は長さ、2次元は面積、3次元は体積。確率（体積×密度）を保つために、密度に $\lvert J \rvert$ を掛けます。
3. **手順は2次元と同じ（逆変換 → ヤコビアン → 代入 → 範囲 → 周辺化）で、行列式の計算を楽にするコツが重要です。** 代表例は、1次変換（多変量正規分布）、球座標・$n$次元極座標（$\chi^2(n)$）、ガンマ分布 → ディリクレ分布、累積和（ヤコビアン $1$）です。

---

## 1. 公式

### 1-1. 設定

$(X_1, \dots, X_n)$ の同時密度を $f_X$ とし、1対1で微分可能な変換 $y = g(x)$ があって、逆変換が $x_i = h_i(y_1, \dots, y_n)$ とします。**変数の個数は、変換の前後で同じ $n$ 個**にします。

### 1-2. ヤコビアンと公式

$$
J = \frac{\partial(x_1, \dots, x_n)}{\partial(y_1, \dots, y_n)} = \det\begin{pmatrix}
\dfrac{\partial x_1}{\partial y_1} & \cdots & \dfrac{\partial x_1}{\partial y_n} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial x_n}{\partial y_1} & \cdots & \dfrac{\partial x_n}{\partial y_n}
\end{pmatrix}
$$

$$
\boxed{\ f_Y(y_1, \dots, y_n) = f_X\bigl(h_1(y), \dots, h_n(y)\bigr)\,\lvert J \rvert\ }
$$

> [!IMPORTANT]
> 2次元と同じく、**使うのは逆変換のヤコビアン**（$x$ を $y$ で偏微分）です。元の変換のヤコビアン $J_g$ を使うなら $\lvert J \rvert = 1/\lvert J_g \rvert$ と、逆数にします。

### 1-3. 次元ごとの対応

| | 1次元 | 2次元 | $n$ 次元 |
| --- | --- | --- | --- |
| 補正の因子 | $\left\lvert\dfrac{dx}{dy}\right\rvert$ | $\lvert J \rvert$（2×2） | $\lvert J \rvert$（$n \times n$） |
| 意味 | 長さの倍率 | 面積の倍率 | 体積の倍率 |
| 積分の置換 | $dx = \lvert\frac{dx}{dy}\rvert dy$ | $dx_1dx_2 = \lvert J \rvert dy_1dy_2$ | $dx_1\cdots dx_n = \lvert J \rvert dy_1\cdots dy_n$ |

---

## 2. なぜ体積の倍率になるのか

![1次変換で単位立方体が行列式倍の体積の平行六面体になる。n次元極座標のヤコビアン r の n-1 乗のグラフ](./images/jacobian_nd_volume.png)

**左（1次変換）**：変換 $\vec{y} = A\vec{x}$ は、単位立方体を、3本のベクトル $A\vec{e}_1, A\vec{e}_2, A\vec{e}_3$（$A$ の各列）が作る平行六面体に移します。その体積は $\lvert\det A\rvert$ です（この例では $3.06$。三重積 $\lvert \vec{a}\cdot(\vec{b}\times\vec{c})\rvert$ でも同じ値）。

**一般の変換**でも、十分小さな範囲では1次変換とみなせて、その行列がヤコビ行列です。だから体積の倍率はヤコビ行列の行列式 $\lvert J \rvert$ になります。確率の保存 $\int_D f_X\,dx = \int_{g(D)} f_X(h(y))\lvert J \rvert\,dy$ から、2次元と同じ理由で公式が出ます。

**右（$r^{n-1}$）**は 4-2 で使う極座標のヤコビアンです。次元が上がるほど、中心から離れた場所の「体積」が急に増えます。

---

## 3. 行列式の計算のコツ

$n$ が大きいと、ヤコビ行列の行列式の計算が本体になります。次のコツで楽になります。

| コツ | 内容 |
| --- | --- |
| **3×3 の行列式** | サラスの方法か、余因子展開（0 の多い行や列で展開する）。 |
| **三角行列にする** | 三角行列の行列式は**対角成分の積**。$x_k$ が $y_1, \dots, y_k$ だけで書ける変換にすると、そうなる。 |
| **逆数を使う** | $\lvert J \rvert = 1/\lvert J_g \rvert$。逆変換より元の変換のほうが偏微分しやすいときに使う。 |
| **行の足し引き** | 行列式は、ある行に別の行の定数倍を足しても変わらない。式を整理するのに便利。 |
| **ブロック分解** | 変数が独立に分かれる変換なら、$J$ は各ブロックの行列式の積。 |

---

## 4. 手順

2次元と同じです。

1. **逆変換を求める**：$x_i = h_i(y)$。
2. **ヤコビアン $J$ を計算し、絶対値をとる。**
3. **公式に代入する**：$f_Y(y) = f_X(h(y))\lvert J \rvert$。
4. **範囲（台）を求める。**
5. **（必要なら）周辺分布を求める**：欲しい変数以外を積分して消す。**変数の個数を揃えるために、補助変数を足して $n$ 個にしてから、あとで消す**のが定石です。

---

## 5. 例

### 5-1. 1次変換 $\vec{Y} = A\vec{X} + \vec{b}$（$n$ 変数）

逆変換 $\vec{x} = A^{-1}(\vec{y} - \vec{b})$ のヤコビ行列は $A^{-1}$ なので、

$$
f_Y(\vec{y}) = \frac{1}{\lvert\det A\rvert}\, f_X\bigl(A^{-1}(\vec{y} - \vec{b})\bigr)
$$

です。独立な標準正規分布 $n$ 個に $\vec{Y} = \vec{\mu} + A\vec{Z}$ を施すと、$\Sigma = AA^\top$、$\lvert\det A\rvert = \sqrt{\det\Sigma}$ より、

$$
f_Y(\vec{y}) = \frac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}}\exp\!\left(-\frac12(\vec{y} - \vec{\mu})^\top\Sigma^{-1}(\vec{y} - \vec{\mu})\right)
$$

となります。これが [多変量正規分布](./多変量正規分布.md) の密度です。

### 5-2. 球座標（3次元）

$(x, y, z) = (r\sin\varphi\cos\theta,\ r\sin\varphi\sin\theta,\ r\cos\varphi)$（$r > 0$、$0 < \varphi < \pi$、$0 \le \theta < 2\pi$）のヤコビ行列は

$$
\begin{pmatrix}
\sin\varphi\cos\theta & r\cos\varphi\cos\theta & -r\sin\varphi\sin\theta \\
\sin\varphi\sin\theta & r\cos\varphi\sin\theta & r\sin\varphi\cos\theta \\
\cos\varphi & -r\sin\varphi & 0
\end{pmatrix}
$$

で、行列式は

$$
\lvert J \rvert = r^2\sin\varphi
$$

です（$\sin\varphi \ge 0$ なので絶対値は不要）。つまり $dx\,dy\,dz = r^2\sin\varphi\,dr\,d\varphi\,d\theta$（球の体積要素）。

**応用：3次元のガウス積分**

$$
\iiint e^{-(x^2+y^2+z^2)/2}\,dx\,dy\,dz = \int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^\infty e^{-r^2/2}\,r^2\sin\varphi\,dr\,d\varphi\,d\theta = 2\pi\cdot 2\cdot\sqrt{\frac{\pi}{2}} = (2\pi)^{3/2}
$$

（$\int_0^\infty r^2e^{-r^2/2}dr = \sqrt{\pi/2}$）。3次元標準正規分布の密度の定数 $(2\pi)^{-3/2}$ の由来です。

### 5-3. $n$ 次元極座標：$\chi^2(n)$ の正体

$n$ 次元でも、$r = \sqrt{x_1^2 + \dots + x_n^2}$ と $n-1$ 個の角度で表すと、

$$
dx_1\cdots dx_n = r^{n-1}\,dr\,d\Omega
$$

（$d\Omega$ は単位球面上の面積要素で、$r$ によらない）となります。2次元は $r$、3次元は $r^2$（$\sin\varphi$ は $d\Omega$ の一部）。

$Z_1, \dots, Z_n$ が独立な $N(0, 1)$ のとき、$R = \sqrt{Z_1^2 + \dots + Z_n^2}$ の密度は

$$
f_R(r) \propto e^{-r^2/2}\cdot r^{n-1}
$$

です。$W = R^2$ に直すと $f_W(w) \propto w^{n/2-1}e^{-w/2}$ なので、

$$
W = Z_1^2 + \dots + Z_n^2 \sim Ga\!\left(\frac{n}{2}, \frac12\right) = \chi^2(n)
$$

になります（[代表的な確率分布](./代表的な確率分布.md) 3-3）。さらに次のこともわかります。

- **向き（球面上の位置）は一様**で、$R$ と独立。
- ガウス積分 $(2\pi)^{n/2} = S_{n-1}\int_0^\infty r^{n-1}e^{-r^2/2}dr$ から、単位球面の表面積 $S_{n-1} = \dfrac{2\pi^{n/2}}{\Gamma(n/2)}$、$n$ 次元球の体積 $\dfrac{\pi^{n/2}}{\Gamma(n/2 + 1)}R^n$ が出る（$n=3$ なら $4\pi$、$\frac43\pi R^3$）。

### 5-4. ガンマ分布 → ディリクレ分布（3変数）

2次元の「和と比」（[2次元の変数変換とヤコビアン](./2次元の変数変換とヤコビアン.md) 5-3）の3変数版です。$X_i \sim Ga(\alpha_i, 1)$（$i = 1, 2, 3$）が独立として、

$$
S = X_1 + X_2 + X_3,\qquad U_1 = \frac{X_1}{S},\quad U_2 = \frac{X_2}{S}\qquad(U_3 = 1 - U_1 - U_2)
$$

とします。変数は $(S, U_1, U_2)$ の3個です。

**① 逆変換**：$x_1 = su_1$、$x_2 = su_2$、$x_3 = s(1 - u_1 - u_2)$。

**② ヤコビアン**：

$$
J = \det\begin{pmatrix}
u_1 & s & 0 \\
u_2 & 0 & s \\
1 - u_1 - u_2 & -s & -s
\end{pmatrix}
= u_1\cdot s^2 - s\bigl(-su_2 - s + su_1 + su_2\bigr) = u_1s^2 + s^2 - u_1s^2 = s^2
$$

（1行目で余因子展開）。$\lvert J \rvert = s^2$。2次元のときは $s$ でした。**$n$ 変数なら $s^{n-1}$** です。

**③ 同時密度**：$\alpha = \alpha_1 + \alpha_2 + \alpha_3$ として、$\prod x_i^{\alpha_i - 1} = s^{\alpha - 3}\prod u_i^{\alpha_i - 1}$ に注意すると、

$$
f(s, u) = \frac{s^{\alpha - 3}\prod u_i^{\alpha_i - 1}\,e^{-s}}{\Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3)}\cdot s^2
= \underbrace{\frac{s^{\alpha - 1}e^{-s}}{\Gamma(\alpha)}}_{Ga(\alpha,\,1)}\cdot\underbrace{\frac{\Gamma(\alpha)}{\prod\Gamma(\alpha_i)}\,u_1^{\alpha_1 - 1}u_2^{\alpha_2 - 1}u_3^{\alpha_3 - 1}}_{\text{ディリクレ分布 }Dir(\alpha_1,\alpha_2,\alpha_3)}
$$

**④ 範囲**：$s > 0$、$u_1, u_2 > 0$、$u_1 + u_2 < 1$。

**結論**：

- $S \sim Ga(\alpha_1 + \alpha_2 + \alpha_3, 1)$（ガンマ分布の再生性）。
- $(U_1, U_2, U_3) \sim Dir(\alpha_1, \alpha_2, \alpha_3)$（**ディリクレ分布**。ベータ分布の多変数版）。
- **$S$ と $U$ は独立**。
- 周辺分布は $U_i \sim Be(\alpha_i,\ \alpha - \alpha_i)$。$\alpha_i = 1$ のとき一様。$n=2$ ならベータ分布。

**数値で確認**：$Ga(2,1)$、$Ga(3,1)$、$Ga(4,1)$ で30万回シミュレーションしました。

![S が Ga(9,1)、U1 が Be(2,7) に従い、S と U1 に相関がなく、(U1,U2,U3) が三角形の上に分布する](./images/jacobian_nd_dirichlet.png)

| 量 | 公式 | シミュレーション |
| --- | --- | --- |
| $S$ の平均・分散 | $9,\ 9$ | $9.004,\ 9.002$ |
| $U$ の平均 | $\left(\frac29, \frac39, \frac49\right) = (0.2222, 0.3333, 0.4444)$ | $(0.2226, 0.3334, 0.4440)$ |
| $U_1$ の分散（$Be(2,7)$） | $0.01728$ | $0.01734$ |
| $S$ と $U_1$ の相関 | $0$（独立） | $-0.0006$ |

### 5-5. 累積和（ヤコビアンが 1）

$X_1, \dots, X_n$ が独立な指数分布 $Exp(\lambda)$ のとき、

$$
Y_1 = X_1,\quad Y_2 = X_1 + X_2,\quad \dots,\quad Y_n = X_1 + \dots + X_n
$$

を考えます。逆変換は $x_k = y_k - y_{k-1}$（$y_0 = 0$）で、ヤコビ行列は

$$
\begin{pmatrix}
1 & 0 & \cdots & 0 \\
-1 & 1 & \ddots & \vdots \\
& \ddots & \ddots & 0 \\
0 & & -1 & 1
\end{pmatrix}
$$

という**下三角行列**なので、行列式は対角成分の積 $1$ です。よって

$$
f_Y(y) = \prod_{k=1}^n\lambda e^{-\lambda(y_k - y_{k-1})}\cdot 1 = \lambda^n e^{-\lambda y_n}\qquad(0 < y_1 < \dots < y_n)
$$

となります。$y_n$ だけに依存する形です。ここから次のことがわかります。

- $y_1, \dots, y_{n-1}$ を積分して消すと（$0 < y_1 < \dots < y_{n-1} < y_n$ の体積は $y_n^{n-1}/(n-1)!$）、$f_{Y_n}(y_n) = \dfrac{\lambda^n y_n^{n-1}e^{-\lambda y_n}}{(n-1)!}$、つまり $Y_n \sim Ga(n, \lambda)$。**ポアソン過程で、$n$ 番目の事象が起きる時刻**がガンマ分布に従うことの証明です（[代表的な確率分布](./代表的な確率分布.md) 3-2）。
- $Y_n$ を固定したとき、$y_1, \dots, y_{n-1}$ の条件付き密度は $\dfrac{(n-1)!}{y_n^{n-1}}$（定数）で、**$[0, y_n]$ 上の一様乱数 $n-1$ 個を小さい順に並べたもの**（順序統計量）の分布と一致します。「ポアソン過程の事象は、$[0, t]$ に一様に散らばる」という性質です。

**数値で確認**：$\lambda = 1$、$n = 4$ で40万回シミュレーションしました。

| 量 | 公式 | シミュレーション |
| --- | --- | --- |
| $Y_4$ の平均・分散 | $4,\ 4$ | $4.004,\ 4.015$ |
| $Y_k / Y_4$（$k = 1, 2, 3$）の平均 | $0.25,\ 0.5,\ 0.75$ | $0.2496,\ 0.5000,\ 0.7497$ |

---

## 6. 発展と注意

### 6-1. 変数の個数が違うとき

求めたい変数が $m$ 個（$m < n$）なら、**補助変数を $n - m$ 個足して $n$ 変数の1対1変換にしてから、補助変数を積分して消します**。5-4 の $S$ は、$U$ を取り出すために足した補助変数とも見られます。変数の個数が違うままでは、ヤコビアン（正方行列の行列式）が定義できません。

### 6-2. 1対1でないとき

$y$ に対応する $x$ が複数あるときは、**それぞれの枝で $f_X(h_k(y))\lvert J_k \rvert$ を計算して足します**（1次元、2次元と同じ）。

### 6-3. ヤコビアンが 0 になる点

$\lvert J \rvert = 0$ の点（例：球座標の $r = 0$ や $\varphi = 0, \pi$）は体積が潰れる点で、測度 $0$ なので積分には影響しません。ただし**そこでは逆変換が一意でなく、変換が使えない**ので、範囲から外して考えます。

### 6-4. 積率母関数との使い分け

- **変換後の密度そのものが欲しい**（例：5-4 でディリクレ分布）→ ヤコビアン。
- **独立な和の分布を、既知の分布と見比べたい**→ 積率母関数のほうが楽。
- 5-4 のように**和と比が独立**といった構造は、同時密度の形から一目でわかる。

---

## 7. 試験での使い方

- **逆変換のヤコビアンを使う。** 元の変換のヤコビアンなら逆数にする。
- **絶対値を忘れない。** 5-4 の $J$ は $s^2$ で正だが、符号が負になることもある。
- **範囲（台）を必ず書く。** $u_1 + u_2 < 1$ のような条件を落とさない。
- **行列式は三角行列や余因子展開で楽をする。** 0 の多い行・列で展開する。
- **変数の個数を揃える。** 求めたい変数が少ないときは補助変数を足して、あとで積分して消す。
- **最後の確認**：積分が $1$ になるか、既知の分布の形になっているかを確かめる。

---

## まとめ

- **公式**：$f_Y(y) = f_X\bigl(h(y)\bigr)\lvert J \rvert$、$J = \det\dfrac{\partial(x_1, \dots, x_n)}{\partial(y_1, \dots, y_n)}$（逆変換のヤコビアン）。
- **意味**：$\lvert J \rvert$ は $n$ 次元の体積の拡大率。
- **例**：1次変換 $\frac{1}{\lvert\det A\rvert}$（多変量正規分布）、球座標 $r^2\sin\varphi$、$n$ 次元極座標 $r^{n-1}$（$\chi^2(n)$）、ガンマ → ディリクレ（$s^{n-1}$）、累積和（$1$）。
- **手順**：逆変換 → ヤコビアン → 代入 → 範囲 → 周辺化（補助変数で変数の個数を揃える）。

---

## 図の作り方

図とシミュレーションの確認は [script/plot_jacobian_nd.py](./script/plot_jacobian_nd.py) で行っています。リポジトリのルートで次を実行すると `images/` に出力されます（数値の確認結果は標準出力に表示されます）。

```bash
uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_jacobian_nd.py
```
