
## $X$ が負の値もとるときの $E[X]=\displaystyle\int_0^\infty P(X>x)\,dx-\int_{-\infty}^0F(x)\,dx$ の証明

### 0. 主張

$E|X|<\infty$ のとき、$F(x)=P(X\le x)$ として

$$
E[X]=\int_0^\infty P(X>x)\,dx-\int_{-\infty}^0F(x)\,dx
$$

第1項は「正の部分」、第2項は「負の部分」の寄与。

### 1. 準備：$X\ge0$ のときの公式（既知）

$$
E[Y]=\int_0^\infty P(Y>y)\,dy\qquad(Y\ge0)
$$

（確認テスト10-1。証明は下の「3. 補足」を参照。）

### 2. 証明：正の部分と負の部分に分ける

**Step 1：分解**

$$
X^+=\max(X,0),\qquad X^-=\max(-X,0)
$$

とおくと、$X=X^+-X^-$、$X^+\ge0$、$X^-\ge0$。期待値の線形性から

$$
E[X]=E[X^+]-E[X^-]
$$

**Step 2：正の部分**

$X^+\ge0$ なので上の公式を使う。$x>0$ で $\{X^+>x\}=\{X>x\}$ だから

$$
E[X^+]=\int_0^\infty P(X^+>x)\,dx=\int_0^\infty P(X>x)\,dx
$$

**Step 3：負の部分**

$X^-\ge0$ なので同様に

$$
E[X^-]=\int_0^\infty P(X^->y)\,dy
$$

$y>0$ で $\{X^->y\}=\{-X>y\}=\{X<-y\}$ だから

$$
E[X^-]=\int_0^\infty P(X<-y)\,dy
$$

$x=-y$ と置換する（$y:0\to\infty$ で $x:0\to-\infty$、$dy=-dx$）：

$$
E[X^-]=\int_{-\infty}^0P(X<x)\,dx
$$

**Step 4：$P(X<x)$ と $F(x)=P(X\le x)$ の違いは無視できる**

$P(X<x)$ と $P(X\le x)$ が異なるのは、$X$ が確率をもつ点 $x$（$P(X=x)>0$ となる点）のときだけで、そのような点は高々可算個。可算個の点は積分に影響しない（測度 $0$）ので

$$
\int_{-\infty}^0P(X<x)\,dx=\int_{-\infty}^0F(x)\,dx
$$

**Step 5：結論**

$$
E[X]=E[X^+]-E[X^-]=\int_0^\infty P(X>x)\,dx-\int_{-\infty}^0F(x)\,dx\qquad\blacksquare
$$

### 3. 補足：$X\ge0$ のときの公式の証明（積分順序の交換）

$Y\ge0$ について、$Y=\displaystyle\int_0^\infty\mathbf 1_{\{x<Y\}}\,dx$（$x$ が $0$ から $Y$ までは $1$、それ以降は $0$ なので、積分は $Y$）。両辺の期待値を取り、積分と期待値の順序を交換する（フビニ/トネリの定理、被積分関数が非負なので常に許される）：

$$
E[Y]=E\left[\int_0^\infty\mathbf 1_{\{x<Y\}}\,dx\right]=\int_0^\infty E\big[\mathbf 1_{\{x<Y\}}\big]\,dx=\int_0^\infty P(Y>x)\,dx
$$

### 4. 別証明：全体を1つの積分で書く

$$
X=\int_0^\infty\mathbf 1_{\{x<X\}}\,dx-\int_{-\infty}^0\mathbf 1_{\{X<x\}}\,dx
$$

が成り立つ。

- $X>0$ のとき：第1項は $\int_0^X1\,dx=X$、第2項は $0$（$x<0<X$ なので $X<x$ は偽）。合計 $X$。
- $X<0$ のとき：第1項は $0$、第2項は $\int_X^01\,dx=-X$（$X<x<0$ の範囲）。引き算で $0-(-X)=X$。

期待値を取ると、積分と期待値を交換して（$E|X|<\infty$ のもとでフビニの定理）

$$
E[X]=\int_0^\infty P(X>x)\,dx-\int_{-\infty}^0P(X<x)\,dx
$$

### 5. 直感

- **正の側**：生存関数 $P(X>x)$ のグラフと $x$ 軸で囲まれる面積（$x>0$）。
- **負の側**：分布関数 $F(x)$ のグラフと $x$ 軸で囲まれる面積（$x<0$）。これを引く。

「$0$ より右の裾の面積」から「$0$ より左の裾の面積」を引いたものが平均。

---

## スタインの公式の証明（詳細版）

### 0. 主張

**標準正規 $Z\sim N(0,1)$**：$g$ が（絶対連続な）関数で $E|g'(Z)|<\infty$ のとき、

$$
E[Zg(Z)]=E[g'(Z)]
$$

**一般の正規 $X\sim N(\mu,\sigma^2)$**：

$$
E[(X-\mu)\,g(X)]=\sigma^2E[g'(X)]
$$

### 1. 証明の核：標準正規密度の微分

標準正規密度を $\varphi(z)=\dfrac1{\sqrt{2\pi}}e^{-z^2/2}$ とする。微分すると

$$
\varphi'(z)=\frac1{\sqrt{2\pi}}e^{-z^2/2}\cdot(-z)=-z\,\varphi(z)
$$

$$
\boxed{z\,\varphi(z)=-\varphi'(z)}
$$

**この性質（微分すると $-z$ 倍になる）が正規分布の本質**で、「$Z$ を掛ける」操作を「微分」に置き換えられる。

### 2. 標準正規の場合（部分積分）

**Step 1：期待値を積分で書く**

$$
E[Zg(Z)]=\int_{-\infty}^\infty z\,g(z)\,\varphi(z)\,dz
$$

**Step 2：$z\varphi(z)=-\varphi'(z)$ を代入**

$$
=-\int_{-\infty}^\infty g(z)\,\varphi'(z)\,dz
$$

**Step 3：部分積分**（$u=g,\ dv=\varphi'dz$ とおくと $du=g'dz$、$v=\varphi$）

$$
\int_{-\infty}^\infty g\,\varphi'\,dz=\Big[g(z)\varphi(z)\Big]_{-\infty}^{\infty}-\int_{-\infty}^\infty g'(z)\,\varphi(z)\,dz
$$

よって

$$
E[Zg(Z)]=-\Big[g\varphi\Big]_{-\infty}^\infty+\int_{-\infty}^\infty g'(z)\varphi(z)\,dz
$$

**Step 4：境界項が $0$ であることを示す**（次節）と、

$$
E[Zg(Z)]=\int_{-\infty}^\infty g'(z)\varphi(z)\,dz=E[g'(Z)]\qquad\blacksquare
$$

### 3. 境界項 $\displaystyle\lim_{z\to\pm\infty}g(z)\varphi(z)=0$ の証明

$E|g'(Z)|<\infty$ から $\lim_{z\to\infty}g(z)\varphi(z)=0$ を示す（$-\infty$ 側も同様）。

**Step 1**：$g(z)=g(0)+\displaystyle\int_0^zg'(t)\,dt$ なので、

$$
|g(z)|\varphi(z)\le|g(0)|\varphi(z)+\varphi(z)\int_0^z|g'(t)|\,dt
$$

第1項は $z\to\infty$ で $0$。

**Step 2**：第2項を、$T>0$ を固定して $[0,T]$ と $[T,z]$ に分ける。

$$
\varphi(z)\int_0^z|g'(t)|\,dt=\varphi(z)\int_0^T|g'(t)|\,dt+\varphi(z)\int_T^z|g'(t)|\,dt
$$

- 前半：$\int_0^T|g'|$ は $z$ によらない定数なので、$\varphi(z)\to0$ から $z\to\infty$ で $0$。
- 後半：$t\le z$ のとき $\varphi(z)\le\varphi(t)$（$\varphi$ は $t>0$ で減少）なので、

$$
\varphi(z)\int_T^z|g'(t)|\,dt\le\int_T^\infty|g'(t)|\varphi(t)\,dt
$$

**Step 3**：$E|g'(Z)|=\displaystyle\int|g'|\varphi<\infty$ なので、右辺は $T\to\infty$ で $0$ に近づく（収束する積分の裾）。したがって、任意の $\varepsilon>0$ に対して $T$ を十分大きく取れば後半を $\varepsilon$ 以下にでき、そのうえで $z$ を大きくすれば前半も $\varepsilon$ 以下にできる。

結局 $\lim_{z\to\infty}g(z)\varphi(z)=0$。$\blacksquare$

### 4. 境界項を出さない別証明（積分順序の交換）

部分積分を使わず、フビニの定理で示す。$g(z)=g(0)+\int_0^zg'(t)dt$ を使う。

**Step 1**：$E[Z]=0$ なので $g(0)$ の項は消える。

$$
E[Zg(Z)]=g(0)\underbrace{E[Z]}_{=0}+E\left[Z\int_0^Zg'(t)\,dt\right]
$$

**Step 2：$Z>0$ の部分**

$$
\int_0^\infty z\varphi(z)\left(\int_0^zg'(t)\,dt\right)dz=\int_0^\infty g'(t)\left(\int_t^\infty z\varphi(z)\,dz\right)dt
$$

（$0\le t\le z<\infty$ の領域で積分順序を交換。）内側は $z\varphi(z)=-\varphi'(z)$ より

$$
\int_t^\infty z\varphi(z)\,dz=\Big[-\varphi(z)\Big]_t^\infty=\varphi(t)
$$

したがって $Z>0$ の部分は $\displaystyle\int_0^\infty g'(t)\varphi(t)\,dt$。

**Step 3：$Z<0$ の部分**も同様に $\displaystyle\int_{-\infty}^0g'(t)\varphi(t)\,dt$。

**Step 4**：足して、

$$
E[Zg(Z)]=\int_{-\infty}^\infty g'(t)\varphi(t)\,dt=E[g'(Z)]
$$

フビニの定理が使える条件は $E|g'(Z)|<\infty$（$\int\int|\cdot|<\infty$）。この方法なら、境界項の議論が不要。

### 5. 一般の正規分布への拡張

$X=\mu+\sigma Z$、$h(z)=g(\mu+\sigma z)$ とおく。連鎖律で $h'(z)=\sigma g'(\mu+\sigma z)$。

標準正規の公式を $h$ に使う：

$$
E[Zh(Z)]=E[h'(Z)]=\sigma E[g'(X)]
$$

左辺は $X-\mu=\sigma Z$ より

$$
E[(X-\mu)g(X)]=E[\sigma Z\,h(Z)]=\sigma E[Zh(Z)]=\sigma\cdot\sigma E[g'(X)]=\sigma^2E[g'(X)]\qquad\blacksquare
$$

### 6. 直感

- $z\varphi(z)=-\varphi'(z)$：密度に $z$ を掛けることは、密度を微分して符号を変えることと同じ。
- 部分積分で微分を $g$ のほうに移す（符号がもう一度反転して正になる）。
- 結果として「$Z$ を掛けて期待値を取る」が「$g$ を微分して期待値を取る」に変わる。

### 7. 使い方の確認

- $g(z)=z$：$E[Z^2]=E[1]=1$。
- $g(z)=z^3$：$E[Z^4]=E[3Z^2]=3$。
- $g(z)=z^{k-1}$：$E[Z^k]=(k-1)E[Z^{k-2}]$（モーメントの漸化式）。

---
