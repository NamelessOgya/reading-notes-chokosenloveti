答えを出力するファイルです。ここからしたを編集して  
  
---

# 問10の解説

## 問題

$X_1,\dots,X_n$ i.i.d. $\sim \mathrm{Ex}(\mu,\sigma)$、密度は

$$
f(x\mid\mu,\sigma)=\sigma^{-1}\exp\{-\sigma^{-1}(x-\mu)\},\quad x>\mu,\ \sigma>0
$$

$U=X_{(1)}$(最小値)、$T=\sum_{i=1}^n(X_i-X_{(1)})$ とおく。

1. $(U,T)$ が $(\mu,\sigma)$ の十分統計量であることを示せ。
2. $n(U-\mu)/\sigma$ と $2T/\sigma$ が独立に、それぞれ $\mathrm{Ex}(0,1)$、$\chi^2_{2(n-1)}$ に従うことを示せ。
3. $\mu,\sigma$ の不偏推定量を与えよ。

## 見取り図

```
(1) 同時密度を U, T で書く → 因子分解定理
(2) Y_i=(X_i-μ)/σ で標準化 → 順序統計量の「間隔」が独立な指数分布になる(レーニィの表現)
(3) (2) から E[U], E[T] が分かる → 不偏になるよう補正
```

**ポイント**:台 $\{x>\mu\}$ が $\mu$ に依存する非正則なモデル。そのため、クラメール・ラオの下限や通常の漸近理論は使えない(実際、$U$ は $\sqrt n$ より速い $n$ のオーダーで収束する)。

---

## (1) 十分統計量

**Step 1:同時密度を書く**

指示関数を明示して書く。

$$
\prod_{i=1}^nf(x_i\mid\mu,\sigma)=\sigma^{-n}\exp\Big\{-\frac{1}{\sigma}\sum_{i=1}^n(x_i-\mu)\Big\}\,\mathbf 1\{x_{(1)}>\mu\}
$$

台の条件「すべての $x_i>\mu$」は、「最小値 $x_{(1)}>\mu$」と同値。

**Step 2:指数部分を $U,T$ で書き換える**

$\sum_i(x_i-\mu)$ に $x_{(1)}$ を足して引く。

$$
\sum_{i=1}^n(x_i-\mu)=\sum_{i=1}^n(x_i-x_{(1)})+n(x_{(1)}-\mu)=T+n(U-\mu)
$$

**Step 3:因子分解**

$$
\prod_{i=1}^nf(x_i\mid\mu,\sigma)=\underbrace{\sigma^{-n}\exp\Big\{-\frac{T+n(U-\mu)}{\sigma}\Big\}\mathbf 1\{U>\mu\}}_{g\big((U,T),\,(\mu,\sigma)\big)}\cdot\underbrace{1}_{h(x)}
$$

$\theta=(\mu,\sigma)$ に依存する部分が、すべて $(U,T)$ を通してしか現れない。因子分解定理(→[十分統計量・因子分解・指数型分布族](../十分統計量・因子分解・指数型分布族.md))より、$(U,T)$ は十分統計量。$\blacksquare$

> 台が $\mu$ に依存するので、指数型分布族ではない。それでも十分統計量は因子分解定理で求まる。

---

## (2) 分布と独立性

### Step 1:標準化する

$Y_i=(X_i-\mu)/\sigma$ とおく。$Y_i$ は i.i.d. で、密度 $e^{-y}\,(y>0)$、つまり標準の指数分布 $\mathrm{Ex}(0,1)$ に従う。

順序統計量 $Y_{(1)}<\cdots<Y_{(n)}$ を使うと、

$$
\frac{n(U-\mu)}{\sigma}=nY_{(1)},\qquad
\frac{T}{\sigma}=\sum_{i=1}^n\big(Y_i-Y_{(1)}\big)=\sum_{i=1}^n\big(Y_{(i)}-Y_{(1)}\big)
$$

### Step 2:順序統計量の同時密度

$Y_{(1)},\dots,Y_{(n)}$ の同時密度は、$0<y_1<\cdots<y_n$ で

$$
n!\,e^{-\sum_{i=1}^ny_i}
$$

**間隔(スペーシング)** $d_i=y_i-y_{i-1}$($y_0=0$、$i=1,\dots,n$)に変数変換する。$y_i=d_1+\cdots+d_i$ なので、ヤコビアンは1(下三角行列で対角成分がすべて1)。指数部分は

$$
\sum_{i=1}^ny_i=\sum_{i=1}^n(n-i+1)\,d_i
$$

($d_1$ は $n$ 回、$d_2$ は $n-1$ 回、…、$d_n$ は1回数えられる。) したがって、同時密度は

$$
n!\prod_{i=1}^ne^{-(n-i+1)d_i}=\prod_{i=1}^n\Big\{(n-i+1)\,e^{-(n-i+1)d_i}\Big\},\quad d_i>0
$$

($n!=\prod_{i=1}^n(n-i+1)$ を使った。)

これは **積の形**。間隔 $d_1,\dots,d_n$ は **互いに独立** で、$d_i\sim\mathrm{Exp}(\text{率 }n-i+1)$。

### Step 3:標準化して $\mathrm{Ex}(0,1)$ にそろえる

$D_i=(n-i+1)\,d_i$ とおくと、$D_i$ は i.i.d. $\mathrm{Ex}(0,1)$(率が1の指数分布)。

(例:$d_1=Y_{(1)}$ は率 $n$ の指数分布なので、$D_1=nY_{(1)}\sim\mathrm{Ex}(0,1)$。これは $\min$ の分布から直接も確かめられる:$P(Y_{(1)}>y)=e^{-ny}$。)

### Step 4:$nY_{(1)}$ と $T/\sigma$ を $D_i$ で表す

- $nY_{(1)}=n\,d_1=D_1$
- $T/\sigma=\sum_{i=1}^n(Y_{(i)}-Y_{(1)})$

$Y_{(i)}-Y_{(1)}=d_2+\cdots+d_i$ なので、

$$
\sum_{i=1}^n(Y_{(i)}-Y_{(1)})=\sum_{i=2}^n\sum_{k=2}^id_k=\sum_{k=2}^n(n-k+1)\,d_k=\sum_{k=2}^nD_k
$$

($d_k$ が現れる $i$ は $k,\dots,n$ の $n-k+1$ 個。)

### Step 5:結論

$$
\frac{n(U-\mu)}{\sigma}=D_1,\qquad \frac{T}{\sigma}=D_2+\cdots+D_n
$$

- $D_1,\dots,D_n$ は独立なので、**$D_1$ と $D_2+\cdots+D_n$ は独立**。
- $D_1\sim\mathrm{Ex}(0,1)$。つまり $n(U-\mu)/\sigma\sim\mathrm{Ex}(0,1)$。
- $D_2+\cdots+D_n$ は、i.i.d. 標準指数分布の $n-1$ 個の和なので $\mathrm{Ga}(n-1,1)$(形状 $n-1$、率1)。

ガンマ分布と $\chi^2$ 分布の関係より、$2\cdot\mathrm{Ga}(k,1)=\chi^2_{2k}$ なので、

$$
\frac{2T}{\sigma}=2(D_2+\cdots+D_n)\sim\chi^2_{2(n-1)}\qquad\blacksquare
$$

> **使った道具**:順序統計量の同時密度 $n!\prod f(y_i)$、間隔への変数変換(ヤコビアン1)、指数分布の無記憶性に対応する性質(間隔が独立な指数分布)。これは「レーニィの表現」と呼ばれる。

---

## (3) 不偏推定量

### Step 1:$E[U]$ と $E[T]$

(2) の結果から、

- $U=\mu+\sigma D_1/n$ なので、$E[U]=\mu+\dfrac{\sigma}{n}$(標準指数分布の平均は1)。
- $T=\sigma(D_2+\cdots+D_n)$ なので、$E[T]=(n-1)\,\sigma$。

### Step 2:不偏になるよう補正する

**$\sigma$ について**:

$$
\hat\sigma_U=\frac{T}{n-1}\quad\Rightarrow\quad E[\hat\sigma_U]=\sigma
$$

**$\mu$ について**:$E[U]=\mu+\sigma/n$ の偏り $\sigma/n$ を、$\hat\sigma_U$ で補正する。

$$
\hat\mu_U=U-\frac{\hat\sigma_U}{n}=U-\frac{T}{n(n-1)}
$$

$$
E[\hat\mu_U]=\Big(\mu+\frac{\sigma}{n}\Big)-\frac{\sigma}{n}=\mu\qquad\blacksquare
$$

### 参考:分散

$D_i$ の分散は1なので、

$$
\mathrm{Var}(U)=\frac{\sigma^2}{n^2},\qquad \mathrm{Var}(\hat\sigma_U)=\frac{\sigma^2}{n-1}
$$

$\hat\mu_U$ の分散は、$U$ と $T$ が独立なので $\mathrm{Var}(\hat\mu_U)=\dfrac{\sigma^2}{n^2}+\dfrac{\sigma^2}{n^2(n-1)}=\dfrac{\sigma^2}{n(n-1)}$。

- $\mu$ の推定量の分散は $1/n^2$ のオーダー(通常の $1/n$ より速い)。台が $\mu$ に依存する非正則モデルの特徴。
- $(U,T)$ は完備十分統計量で、$\hat\mu_U,\hat\sigma_U$ はその関数である不偏推定量なので、レーマン・シェフェの定理により **UMVUE**(→[点推定](../点推定.md) の3.10節)。

---

## まとめ

| 小問 | 方針 | 鍵になる式 |
|---|---|---|
| (1) | 因子分解定理 | $\sum(x_i-\mu)=T+n(U-\mu)$ |
| (2) | 標準化 → 順序統計量の間隔に変数変換 | 間隔は独立な指数分布、$nY_{(1)}=D_1$、$T/\sigma=\sum_{k\ge2}D_k$ |
| (3) | $E[U],E[T]$ を補正 | $\hat\sigma=T/(n-1)$、$\hat\mu=U-T/\{n(n-1)\}$ |

**試験での書き方**:(2) の導出を省略せず書くのが難所。「順序統計量の同時密度 → 間隔に変換 → 独立な指数分布」の3手順を書けば足りる。

---

# 問11の解説

## 問題

$X\sim\mathrm{Bin}(n,p)$。$\theta=p(1-p)$ について、

1. 不偏推定量 $\hat\theta_U$ と最尤推定量 $\hat\theta_{ML}$ を求めよ。
2. $\sqrt n(\hat\theta_{ML}-\theta)$ と $\sqrt n(\hat\theta_U-\theta)$ の漸近分布が一致することを示せ。

## 見取り図

```
(1) MLE:不変性で p̂=X/n を代入 / 不偏:E[X(X-1)]=n(n-1)p² を利用
(2) CLT → デルタ法で MLE の漸近分布 / θ̂_U = n/(n-1)·θ̂_ML → スルツキーの定理で同じ極限
```

## (1) 推定量

**最尤推定量**:$p$ の最尤推定量は $\hat p=X/n$。最尤推定量の **不変性**(→[点推定](../点推定.md) の2.2節)より、

$$
\hat\theta_{ML}=\hat p(1-\hat p)=\frac Xn\Big(1-\frac Xn\Big)=\frac{X(n-X)}{n^2}
$$

**不偏推定量**:$\theta=p-p^2$。$E[X]=np$ なので $X/n$ は $p$ の不偏推定量。$p^2$ については、階乗モーメント $E[X(X-1)]=n(n-1)p^2$ より、

$$
E\Big[\frac{X(X-1)}{n(n-1)}\Big]=p^2
$$

よって、

$$
\hat\theta_U=\frac Xn-\frac{X(X-1)}{n(n-1)}=\frac{X\{(n-1)-(X-1)\}}{n(n-1)}=\frac{X(n-X)}{n(n-1)}
$$

**関係**:$\hat\theta_U=\dfrac{n}{n-1}\hat\theta_{ML}$。最尤推定量は $\dfrac{n-1}{n}\theta$ だけ小さく出る(標本分散の $1/n$ 版と同じ構造)。

> 単純に $\hat p-\hat p^2$ の期待値を取ると $E[\hat p^2]=p^2+\dfrac{p(1-p)}n$ となり、$E[\hat\theta_{ML}]=\theta-\dfrac\theta n=\dfrac{n-1}n\theta$。

## (2) 漸近分布

**Step 1:$\hat p$ の漸近分布**

$X$ は $n$ 個のベルヌーイの和なので、中心極限定理より

$$
\sqrt n(\hat p-p)\xrightarrow{d}N\big(0,\,p(1-p)\big)
$$

**Step 2:デルタ法で $\hat\theta_{ML}$**

$g(p)=p(1-p)$、$g'(p)=1-2p$。$p\ne1/2$ で $g'(p)\ne0$ なので、

$$
\sqrt n(\hat\theta_{ML}-\theta)\xrightarrow{d}N\big(0,\,p(1-p)(1-2p)^2\big)
$$

($p(1-p)(1-2p)^2=\theta(1-4\theta)$ とも書ける。$(1-2p)^2=1-4p(1-p)$ より。)

**Step 3:$\hat\theta_U$ との差が消えることを示す**

$\hat\theta_U=\dfrac n{n-1}\hat\theta_{ML}=\hat\theta_{ML}+\dfrac1{n-1}\hat\theta_{ML}$ より

$$
\sqrt n(\hat\theta_U-\theta)=\sqrt n(\hat\theta_{ML}-\theta)+\frac{\sqrt n}{n-1}\hat\theta_{ML}
$$

- 第1項は Step 2 より、$N(0,\theta(1-4\theta))$ に分布収束。
- 第2項:$\hat\theta_{ML}\xrightarrow{P}\theta$、$\sqrt n/(n-1)\to0$ なので、$0$ に確率収束。

スルツキーの定理(分布収束する量に、0に確率収束する量を足しても極限は変わらない)より、

$$
\sqrt n(\hat\theta_U-\theta)\xrightarrow{d}N\big(0,\,\theta(1-4\theta)\big)\qquad\blacksquare
$$

> $p=1/2$ では $g'(p)=0$ で退化する(収束の速さが $n$ のオーダーになる)。問題文は $p\ne1/2$ を暗黙に仮定している。

## まとめ

- 不偏推定量と最尤推定量は、偏りが $O(1/n)$ だけ違うが、漸近分布は同じ。
- 「不偏でなくても、偏りが $n$ とともに消えれば、漸近的には同じ振る舞い」の典型例。

---

# 問12の解説

## 問題

$X_1,\dots,X_n$ i.i.d. $\sim\mathrm{Po}(\lambda)$。

1. $\sum X_i$ の分布を積率母関数で示せ。
2. $\lambda$ の任意の不偏推定量の分散の下限を、クラメール・ラオの不等式で与えよ。
3. 最尤推定量を求め、分散が下限に達していることを確かめよ。

## 見取り図

```
(1) MGF の積 = 各 MGF の n 乗 → Po(nλ)
(2) 1観測のスコアと I_1 を計算 → I_n=nI_1 → 下限
(3) MLE=標本平均 → 不偏で Var=λ/n → 下限に一致(有効推定量)
```

## (1) 和の分布

$Y=\sum X_i$ とおく。独立性より積率母関数は積になる。ポアソンのMGFは $M_X(t)=e^{\lambda(e^t-1)}$。

$$
M_Y(t)=E[e^{tY}]=\prod_{i=1}^nE[e^{tX_i}]=\{M_X(t)\}^n=e^{n\lambda(e^t-1)}
$$

これは $\mathrm{Po}(n\lambda)$ のMGF。MGFは分布を一意に決めるので、$Y\sim\mathrm{Po}(n\lambda)$。$\blacksquare$

## (2) クラメール・ラオの下限

**Step 1:スコアを計算する**

$\log f(x\mid\lambda)=x\log\lambda-\lambda-\log x!$ なので、

$$
\frac{d}{d\lambda}\log f=\frac x\lambda-1,\qquad\frac{d^2}{d\lambda^2}\log f=-\frac{x}{\lambda^2}
$$

**Step 2:フィッシャー情報量**

$$
I_1(\lambda)=E\Big[-\frac{d^2}{d\lambda^2}\log f(X_1\mid\lambda)\Big]=\frac{E[X_1]}{\lambda^2}=\frac1\lambda
$$

(別の計算:$\mathrm{Var}\big(X/\lambda-1\big)=\mathrm{Var}(X)/\lambda^2=1/\lambda$ と一致。)

i.i.d. なので $I_n(\lambda)=nI_1(\lambda)=n/\lambda$。

**Step 3:下限**

$$
\mathrm{Var}(\hat\theta)\ge\frac1{I_n(\lambda)}=\frac\lambda n
$$

## (3) 最尤推定量

$$
\ell(\lambda)=\sum x_i\log\lambda-n\lambda-\sum\log x_i!,\qquad\ell'(\lambda)=\frac{\sum x_i}{\lambda}-n=0
$$

$$
\hat\lambda=\bar X
$$

- 不偏:$E[\bar X]=\lambda$。
- 分散:$\mathrm{Var}(\bar X)=\dfrac{\mathrm{Var}(X_1)}n=\dfrac\lambda n$。

下限 $\lambda/n$ に **一致する**。つまり $\bar X$ は有効推定量(UMVUE)。$\blacksquare$

## ポイント

- ポアソン分布は指数型分布族で、$\lambda$ は平均パラメータ($E[X]=\lambda$)。クラメール・ラオの等号が成り立つのは、このためである(問18の結論)。
- スコアが $\dfrac{n}{\lambda}(\bar X-\lambda)$ と、$\hat\lambda-\lambda$ の定数倍になっていることからも、等号成立が分かる。

---

# 問13の解説

## 問題

$X_1,\dots,X_n$ i.i.d. $\sim N(0,\theta)$($\theta$ は分散)。$\hat\theta=\sum X_i^2/n$。

1. $I_n(\theta)$ とクラメール・ラオの下限を与えよ。
2. 最尤推定量を求め、平均と分散を求めよ。
3. $n\hat\theta/\theta$ の分布は。
4. $\sqrt n(\hat\theta-\theta)$ の漸近分布は。

## 見取り図

```
(1) 対数尤度を θ で2階微分 → I_1 = 1/(2θ²) → 下限 2θ²/n
(2) MLE = ΣX²/n、分散 = Var(X²)/n = 2θ²/n(下限に一致)
(3) X²/θ ~ χ²_1 の和 → χ²_n
(4) CLT → N(0, 2θ²)
```

## (1) フィッシャー情報量

$$
\log f(x\mid\theta)=-\frac12\log(2\pi\theta)-\frac{x^2}{2\theta}
$$

$$
\frac{d}{d\theta}\log f=-\frac1{2\theta}+\frac{x^2}{2\theta^2},\qquad
\frac{d^2}{d\theta^2}\log f=\frac1{2\theta^2}-\frac{x^2}{\theta^3}
$$

$E[X_1^2]=\theta$ を使うと、

$$
I_1(\theta)=-E\Big[\frac1{2\theta^2}-\frac{X_1^2}{\theta^3}\Big]=-\frac1{2\theta^2}+\frac1{\theta^2}=\frac1{2\theta^2}
$$

$$
I_n(\theta)=\frac n{2\theta^2},\qquad\mathrm{Var}(\hat\theta')\ge\frac{2\theta^2}n\ \ (\text{任意の不偏推定量}\ \hat\theta')
$$

## (2) 最尤推定量

$$
\ell(\theta)=-\frac n2\log(2\pi\theta)-\frac{\sum x_i^2}{2\theta},\qquad
\ell'(\theta)=-\frac n{2\theta}+\frac{\sum x_i^2}{2\theta^2}=0
$$

$$
\hat\theta_{ML}=\frac1n\sum X_i^2
$$

- 平均:$E[\hat\theta_{ML}]=E[X_1^2]=\theta$(不偏)。
- 分散:$\mathrm{Var}(\hat\theta_{ML})=\dfrac{\mathrm{Var}(X_1^2)}n$。$E[X_1^4]=3\theta^2$(正規分布の4次モーメント)より、$\mathrm{Var}(X_1^2)=3\theta^2-\theta^2=2\theta^2$。

$$
\mathrm{Var}(\hat\theta_{ML})=\frac{2\theta^2}n
$$

下限に一致するので、$\hat\theta_{ML}$ は有効推定量。

## (3) 分布

$X_i/\sqrt\theta\sim N(0,1)$ なので $X_i^2/\theta\sim\chi^2_1$。独立な $n$ 個の和は

$$
\frac{n\hat\theta}{\theta}=\sum_{i=1}^n\frac{X_i^2}\theta\sim\chi^2_n
$$

(確認:$\mathrm{Var}(\chi^2_n)=2n$ から、$\mathrm{Var}(\hat\theta)=\dfrac{\theta^2}{n^2}\cdot2n=\dfrac{2\theta^2}n$ で、(2) と一致。)

## (4) 漸近分布

$X_1^2,\dots,X_n^2$ は i.i.d. で、平均 $\theta$、分散 $2\theta^2$。中心極限定理より、

$$
\sqrt n(\hat\theta-\theta)\xrightarrow{d}N(0,\,2\theta^2)\qquad\blacksquare
$$

漸近分散 $2\theta^2=1/I_1(\theta)$ なので、**漸近有効**(最尤推定量の一般論とも整合)。

---

# 問14の解説

## 問題

問13と同じモデルで $\sqrt\theta$(標準偏差)の推定を考える。

1. $E[|X_i|]=\sqrt{2\theta/\pi}$ を示せ。
2. これを用いた $\sqrt\theta$ のモーメント推定量 $\tilde\theta^{1/2}$ を求め、$\sqrt n(\tilde\theta^{1/2}-\sqrt\theta)$ の漸近分布を求めよ。最尤推定量 $\sqrt{\hat\theta}$ の漸近分布も求め、漸近分散を比較せよ。

## 見取り図

```
(1) 積分を直接計算(∫ x e^{-x²/2θ} は原始関数が出る)
(2) モーメント法:|X| の平均を √θ に変換 → CLT で漸近分散 (π/2-1)θ
    MLE:√θ̂ に問13(4) とデルタ法 → 漸近分散 θ/2
    比較:(π/2-1)θ > θ/2 → MLE の方が漸近分散が小さい
```

## (1) $E[|X|]$

$$
E[|X|]=\frac1{\sqrt{2\pi\theta}}\int_{-\infty}^\infty|x|e^{-x^2/(2\theta)}dx=\frac2{\sqrt{2\pi\theta}}\int_0^\infty xe^{-x^2/(2\theta)}dx
$$

$$
\int_0^\infty xe^{-x^2/(2\theta)}dx=\Big[-\theta e^{-x^2/(2\theta)}\Big]_0^\infty=\theta
$$

$$
E[|X|]=\frac{2\theta}{\sqrt{2\pi\theta}}=\sqrt{\frac{2\theta}{\pi}}\qquad\blacksquare
$$

## (2) モーメント推定量と最尤推定量

### モーメント推定量

$E\big[|X_i|\sqrt{\pi/2}\big]=\sqrt\theta$ なので、標本平均を等置して

$$
\tilde\theta^{1/2}=\frac1n\sum_{i=1}^n|X_i|\sqrt{\frac\pi2}
$$

**漸近分布**:$|X_i|\sqrt{\pi/2}$ は i.i.d. で、平均 $\sqrt\theta$、分散は

$$
\mathrm{Var}\big(|X_i|\sqrt{\pi/2}\big)=E[X_i^2]\cdot\frac\pi2-(\sqrt\theta)^2=\frac\pi2\theta-\theta=\Big(\frac\pi2-1\Big)\theta
$$

中心極限定理より、

$$
\sqrt n(\tilde\theta^{1/2}-\sqrt\theta)\xrightarrow{d}N\Big(0,\Big(\frac\pi2-1\Big)\theta\Big)
$$

### 最尤推定量

$\sqrt\theta$ の最尤推定量は、不変性より $\sqrt{\hat\theta}$($\hat\theta=\sum X_i^2/n$)。問13(4) の $\sqrt n(\hat\theta-\theta)\to N(0,2\theta^2)$ と、デルタ法($g(\theta)=\sqrt\theta$、$g'(\theta)=\dfrac1{2\sqrt\theta}$)より、

$$
\sqrt n(\sqrt{\hat\theta}-\sqrt\theta)\xrightarrow{d}N\Big(0,\ \frac{2\theta^2}{4\theta}\Big)=N\Big(0,\ \frac\theta2\Big)
$$

### 比較

$$
\Big(\frac\pi2-1\Big)\theta-\frac12\theta=\frac{\pi-3}2\theta>0
$$

- モーメント推定量の漸近分散は $0.571\theta$、最尤推定量は $0.5\theta$。
- **最尤推定量の方が漸近分散が小さい**。漸近相対効率は $0.5/0.571\approx0.876$。
- 最尤推定量は漸近有効(漸近分散がクラメール・ラオの下限に一致:$g'(\theta)^2/I_1=\dfrac{1}{4\theta}\cdot2\theta^2=\dfrac\theta2$)ので、これは一般論とも整合する。

> モーメント法は計算が簡単だが、効率では最尤法に劣る例。

---

# 問15の解説

## 問題

$X_1,\dots,X_n$ を密度 $f(x\mid\theta)$ からのランダムサンプルとし、$h(\theta)$ の不偏推定量 $\hat h(X)$ が存在するとき、

$$
\mathrm{Var}_\theta(\hat h)\ge\frac{\{h'(\theta)\}^2}{nI_1(\theta)}
$$

を示せ。

## 見取り図

```
スコア S_n の性質:E[S_n]=0、Var(S_n)=I_n=nI_1
Cov(ĥ, S_n) = h'(θ)(不偏性 + 微分と積分の交換)
コーシー・シュワルツ → {h'}² ≤ Var(ĥ)·I_n
```

(点推定.md の3.4節の証明で、$h(\theta)=\theta$ とした特別な場合。)

## 証明

**記号**:$f_n(x\mid\theta)=\prod f(x_i\mid\theta)$、スコア $S_n(\theta,X)=\dfrac{d}{d\theta}\log f_n(X\mid\theta)$。正則条件(微分と積分の交換)を仮定する。

**Step 1:$E[S_n]=0$、$\mathrm{Var}(S_n)=I_n$**

$$
E[S_n]=\int\frac{\partial_\theta f_n}{f_n}f_n\,dx=\partial_\theta\int f_n\,dx=\partial_\theta1=0
$$

よって $\mathrm{Var}(S_n)=E[S_n^2]=I_n(\theta)=nI_1(\theta)$。

**Step 2:共分散を計算する**

$E[S_n]=0$ なので、$E[(\hat h-h(\theta))S_n]=E[\hat hS_n]$。$\partial_\theta f_n=S_nf_n$ を使うと、

$$
E[\hat hS_n]=\int\hat h(x)\frac{\partial_\theta f_n(x\mid\theta)}{f_n(x\mid\theta)}f_n(x\mid\theta)\,dx=\frac d{d\theta}\int\hat h(x)f_n(x\mid\theta)\,dx=\frac d{d\theta}E[\hat h]=h'(\theta)
$$

最後の等号は、$\hat h$ が不偏($E[\hat h]=h(\theta)$)であることによる。

**Step 3:コーシー・シュワルツの不等式**

$$
\big\{E[(\hat h-h(\theta))S_n]\big\}^2\le E[(\hat h-h(\theta))^2]\cdot E[S_n^2]=\mathrm{Var}(\hat h)\cdot I_n(\theta)
$$

左辺は Step 2 より $\{h'(\theta)\}^2$。

$$
\{h'(\theta)\}^2\le\mathrm{Var}(\hat h)\,I_n(\theta)\ \Rightarrow\ \mathrm{Var}(\hat h)\ge\frac{\{h'(\theta)\}^2}{nI_1(\theta)}\qquad\blacksquare
$$

## ポイント

- 不偏性が使われるのは、Step 2 の $\dfrac d{d\theta}E[\hat h]=h'(\theta)$ のところだけ。
- $\hat h$ が不偏でないとき($E[\hat h]=h+b$)は、$h'(\theta)$ が $h'(\theta)+b'(\theta)$ になる(問18(3))。

---

# 問16の解説

## 問題

$(X_i,Y_i)$ は互いに独立で、$X_i,Y_i$ も独立に $N(\mu_i,\sigma^2)$($i=1,\dots,n$)。

1. $\mu_1,\dots,\mu_n,\sigma^2$ の最尤推定量を求めよ。
2. $\sigma^2$ の最尤推定量が一致性を持たないことを示し、一致推定量を与えよ。
3. プールした推定量 $\Big\{\sum(X_i-\bar X)^2+\sum(Y_i-\bar Y)^2\Big\}/(2n)$ が一致性を持たないことを示せ。

## 見取り図

```
(1) 対数尤度を μ_i と σ² で微分 → μ̂_i=(X_i+Y_i)/2、σ̂²=ΣX_i-Y_i)²/(4n)
(2) X_i-Y_i ~ N(0,2σ²) → 大数の法則で σ̂² → σ²/2 (一致しない) → 2倍した推定量が一致
(3) 平均 X̄ を共通に引くと、μ_i のばらつき b₀ が混入 → σ²+b₀ に収束
```

**この問題のテーマ**:ネイマン・スコットの問題(偶有パラメータ問題)。$n$ を増やすとパラメータ $\mu_i$ も $n$ 個増えるので、最尤推定量の一致性が成り立たない。

## (1) 最尤推定量

観測は $2n$ 個で、パラメータは $n+1$ 個。

$$
\ell(\mu_1,\dots,\mu_n,\sigma^2)=-n\log(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_{i=1}^n\big\{(x_i-\mu_i)^2+(y_i-\mu_i)^2\big\}
$$

$\mu_i$ で微分して0とおく:

$$
\frac{\partial\ell}{\partial\mu_i}=\frac1{\sigma^2}\{(x_i-\mu_i)+(y_i-\mu_i)\}=0\ \Rightarrow\ \hat\mu_i=\frac{X_i+Y_i}2
$$

$(x_i-\hat\mu_i)^2+(y_i-\hat\mu_i)^2=\dfrac{(x_i-y_i)^2}2$ を使うと、$\sigma^2$ で微分して

$$
\frac{\partial\ell}{\partial\sigma^2}=-\frac n{\sigma^2}+\frac1{2\sigma^4}\sum\frac{(x_i-y_i)^2}2=0\ \Rightarrow\ \hat\sigma^2=\frac1{4n}\sum_{i=1}^n(X_i-Y_i)^2
$$

## (2) 一致性の欠如と一致推定量

$X_i-Y_i$ は i.i.d. $\sim N(0,2\sigma^2)$(独立な正規分布の差)。大数の法則より、

$$
\frac1n\sum(X_i-Y_i)^2\xrightarrow{P}E[(X_1-Y_1)^2]=2\sigma^2
$$

$$
\hat\sigma^2=\frac14\cdot\frac1n\sum(X_i-Y_i)^2\xrightarrow{P}\frac{2\sigma^2}4=\frac{\sigma^2}2\neq\sigma^2
$$

**最尤推定量は $\sigma^2/2$ に収束し、一致性を持たない**。(実際、すべての $n$ で $E[\hat\sigma^2]=\sigma^2/2$ と偏りがある。)

**一致推定量**:$\hat\sigma^2$ を2倍する。

$$
\tilde\sigma^2=\frac1{2n}\sum_{i=1}^n(X_i-Y_i)^2\xrightarrow{P}\sigma^2
$$

(不偏でもある。$E[\tilde\sigma^2]=\sigma^2$。)

**なぜ最尤法が失敗するか**:最尤推定量の一致性の理論は、パラメータの次元が $n$ によらず **固定** されていることを前提にしている。ここでは $\mu_i$ を各ペアで推定するため、自由度が1つ失われる(各ペアの $X_i,Y_i$ から $\mu_i$ と $\sigma^2$ を同時に推定している)。この失われた自由度の分だけ偏りが残り、$n$ を増やしても消えない。

## (3) プール推定量の非一致性

$\bar X=\frac1n\sum X_i$、$\bar\mu=\frac1n\sum\mu_i$ とおく。仮定として、

$$
\frac1n\sum\mu_i\to a_0,\qquad b_n:=\frac1n\sum(\mu_i-\bar\mu)^2\to b_0>0
$$

**Step 1:分解する**

$X_i-\bar X=(X_i-\mu_i)-(\bar X-\bar\mu)+(\mu_i-\bar\mu)$ を2乗して平均を取ると、

$$
\frac1n\sum(X_i-\bar X)^2=\frac1n\sum(X_i-\mu_i)^2-(\bar X-\bar\mu)^2+\frac2n\sum(\mu_i-\bar\mu)(X_i-\mu_i)+b_n
$$

**Step 2:各項の収束**

- 第1項:大数の法則より $\sigma^2$ に確率収束。
- 第2項:$\bar X-\bar\mu\sim N(0,\sigma^2/n)$ なので $0$ に確率収束。
- 第3項:平均0、分散 $\dfrac{4\sigma^2}{n^2}\sum(\mu_i-\bar\mu)^2=\dfrac{4\sigma^2b_n}n\to0$ なので $0$ に確率収束。
- 第4項:$b_n\to b_0$。

$$
\frac1n\sum(X_i-\bar X)^2\xrightarrow{P}\sigma^2+b_0
$$

**Step 3:結論**

$Y$ についても同様。プール推定量は、2つの平均なので

$$
\frac{\sum(X_i-\bar X)^2+\sum(Y_i-\bar Y)^2}{2n}\xrightarrow{P}\sigma^2+b_0
$$

$b_0>0$ なら $\sigma^2$ に収束しない。**$b_0=0$ のとき(すべての $\mu_i$ が(漸近的に)等しいとき)だけ一致性を持つ**。$\blacksquare$

**理由**:$X_i$ と $Y_i$ で共通の $\bar X,\bar Y$ を引くと、$\mu_i$ の違いによるばらつきが誤差として混入する。ペアの差 $X_i-Y_i$ を使えば $\mu_i$ が消えるので、(2) の推定量は一致する。

---

# 問18の解説

## 問題

クラメール・ラオの不等式について、

1. 不等式(6.10)で等号が成立する必要十分条件は、$\hat\theta$ の分布が指数型分布族に入ることを示せ。
2. 不等式(6.17)を示せ。
3. 不等式(6.18)を示せ。

(教科書の式:(6.10) は不偏推定量のクラメール・ラオ、(6.17) は $h(\theta)$ の不偏推定量のクラメール・ラオ(問15)、(6.18) は偏りがある推定量の平均2乗誤差の下限。PDFの解答の記述から対応を推測した。)

## 見取り図

```
(1) 等号 ⟺ コーシー・シュワルツの等号 ⟺ スコアが (θ̂-θ) の定数倍
    → 積分すると log f が θ̂(x)·(θの関数) の形 → 指数型分布族
(2) 問15 と同じ
(3) 偏りがあるときは E[δ] の微分が g'+b' になる → MSE = Var + bias² を足す
```

## (1) 等号成立条件

**Step 1:等号がいつ成り立つか**

問15の証明で使ったコーシー・シュワルツの不等式は、2つの確率変数 $\hat\theta-\theta$ と $S_n$ が **線形関係**($S_n=a\,(\hat\theta-\theta)$ の形)のときだけ等号が成り立つ。

$$
S_n(\theta,x)=\frac d{d\theta}\log f_n(x\mid\theta)=a(\theta)\{\hat\theta(x)-\theta\}
$$

係数 $a$ は $x$ によらないが、$\theta$ には依存してよい($a=a(\theta)$)。

**Step 2:$\theta$ で積分する**

$$
\log f_n(x\mid\theta)=\hat\theta(x)\int a(\theta)\,d\theta-\int\theta a(\theta)\,d\theta+b(x)
$$

($b(x)$ は積分定数で、$x$ のみの関数。) $\eta(\theta)=\int a\,d\theta$、$A(\theta)=\int\theta a\,d\theta$ とおき、$h(x)=e^{b(x)}$ とすると、

$$
f_n(x\mid\theta)=h(x)\exp\big\{\eta(\theta)\hat\theta(x)-A(\theta)\big\}
$$

これは、**十分統計量 $T(x)=\hat\theta(x)$ を持つ指数型分布族**の形。

PDFの解答では $a$ を定数としている($a(\theta)\equiv a$ のとき):

$$
f(x\mid\theta)=h(x)\exp\Big\{a\hat\theta(x)\theta-\frac a2\theta^2\Big\}
$$

**Step 3:逆(指数型分布族なら等号が成立する場合がある)**

1次元の指数型分布族 $f(x\mid\theta)=h(x)c^*(\theta)\exp\{\theta T(x)\}$ では、$E[T(X)]=-\dfrac d{d\theta}\log c^*(\theta)$。これが $a\theta$ となる制約を入れると、$c^*(\theta)=e^{-a\theta^2/2}$ で、$\hat\theta=T/a$ は $\theta$ の不偏推定量になり、上の形と一致する。

**結論**:不偏推定量 $\hat\theta$ の分散がクラメール・ラオの下限に達する必要十分条件は、データの分布が $f(x\mid\theta)=h(x)\exp\{\eta(\theta)\hat\theta(x)-A(\theta)\}$ の形の指数型分布族で、$\hat\theta$ がその十分統計量(平均パラメータの推定量)であること。$\blacksquare$

**例**:問12(ポアソン)、問13($N(0,\theta)$ の分散)は、いずれも等号が成立する指数型分布族。

## (2) 不等式(6.17)

問15の証明そのもの:

$$
\mathrm{Var}(\hat h)\ge\frac{\{h'(\theta)\}^2}{nI_1(\theta)}
$$

## (3) 不等式(6.18):偏りのある推定量

$\delta(X)$ を $g(\theta)$ の推定量とし(不偏とは限らない)、偏りを $\mathrm{Bias}(\delta)=E[\delta]-g(\theta)$ とおく。

**Step 1:平均2乗誤差を分解する**

$$
\mathrm{MSE}(\theta,\delta)=E[(\delta-g(\theta))^2]=\mathrm{Var}(\delta)+\{\mathrm{Bias}(\delta)\}^2
$$

**Step 2:分散にクラメール・ラオを適用する**

$\delta$ は $E[\delta]$ の(その意味での)不偏推定量。(6.17) の $h(\theta)=E_\theta[\delta]$ とみなすと、

$$
\mathrm{Var}(\delta)\ge\frac{\{(d/d\theta)E[\delta]\}^2}{I_n(\theta)}
$$

**Step 3:偏りの微分を使って書き直す**

$\mathrm{Bias}(\delta)=E[\delta]-g(\theta)$ を $\theta$ で微分すると $\dfrac d{d\theta}E[\delta]=g'(\theta)+\dfrac d{d\theta}\mathrm{Bias}(\delta)$。

$$
\mathrm{MSE}(\theta,\delta)\ge\frac{\{g'(\theta)+\mathrm{Bias}'(\delta)\}^2}{I_n(\theta)}+\{\mathrm{Bias}(\delta)\}^2\qquad\blacksquare
$$

**ポイント**:偏りを許すと、$\mathrm{Bias}'<0$($\theta$ が増えると偏りが減る)になるように設計すれば、分散の下限を下げられる。縮小推定がMSEで不偏推定量を上回れる理由。

---

# 質問返答履歴

この会話での、点推定・十分統計量・問10まわりの質問と返答の記録。

## A. 問題の選定

**Q**:「問18までの範囲で、点推定を網羅するために解くべき問題を教えて」(`MathStat_Answers.pdf` のp23-27)

**A**:23〜24ページの問題文を読み取り、**問10〜18** が範囲と判断。点推定の項目への対応は次の通り。

| 問 | 内容 | カバーする項目 |
|---|---|---|
| 10 | 指数分布 $\mathrm{Ex}(\mu,\sigma)$ | 十分統計量、不偏推定量、非正則モデル |
| 11 | $\mathrm{Bin}$、$\theta=p(1-p)$ | 不偏性、最尤法、デルタ法 |
| 12 | ポアソン | クラメール・ラオ、有効推定量 |
| 13 | $N(0,\theta)$ | フィッシャー情報量、漸近有効性 |
| 14 | $\sqrt\theta$ の推定 | モーメント法 vs 最尤法 |
| 15 | $h(\theta)$ のクラメール・ラオ | CR の一般形 |
| 16 | ネイマン・スコット | 一致性の反例 |
| 17(\*) | 2変量正規の相関係数 | 余裕があれば |
| 18 | CR の等号条件 | 指数型分布族 |

この範囲に含まれない項目:ベイズ法(問27)、BLUE(問22)、識別可能性。

## B. 問10に関する質問

**Q1**:「十分統計量を正しく理解してないかもしれないのですが、なんで尤度を取ろうという発想になるんでしょうか」

**A1**:十分統計量の定義は「$T$ を与えたときのデータの条件付き分布が $\theta$ に依存しない」こと。条件付き確率 $\dfrac{f(x;\theta)}{P_\theta(T=t)}$ の計算で、同時密度(尤度と同じ式)が自然に現れる。因子分解定理は、「$\theta$ に依存する部分が $T$ を通してだけ現れる」ことを確認する道具。尤度を新たに発想するのではなく、定義の計算に出てくる式。→ [点推定.md](../点推定.md) の3.10節に定義を追記。

**Q2**:「作成いただいた解答ですが、なんで順序統計量使う感じになってるんですか」

**A2**:$U=X_{(1)}$ と $T=\sum(X_i-X_{(1)})$ の定義に最小値が入っているため。$U$ と $T$ の独立性は直観では自明でないので、$U$ と $T$ を同時に表せる枠組みとして、順序統計量の間隔 $D_i$ を使った。別解として、変数変換($X_1$ が最小の場合に $(U,X_2-U,\dots)$ に変換)や、指数分布の無記憶性を使う方法もある。

**Q3**:「$Y_{(1)},Y_{(2)},\dots$ の同時密度の部分、確率密度関数の分母の $\sigma$ を忘れてませんか」

**A3**:忘れていない。$Y_i=(X_i-\mu)/\sigma$ と標準化したので、ヤコビアンの $\sigma$ が元の密度の $\sigma^{-1}$ と打ち消し合い、$Y_i$ の密度は $e^{-y}$(標準指数分布)になる。$\sigma$ は、$U=\mu+\sigma Y_{(1)}$、$T=\sigma\sum(Y_i-Y_{(1)})$ と $X$ に戻すときに現れる。

**Q4**:「スペーシング変換することでめっちゃ綺麗になりましたね。なんで思いついた？典型的な処理？」

**A4**:指数分布の順序統計量を扱うときの典型的な処理(レーニィの表現)。理由は3つ:(1) $U,T$ がどちらも「最小値からの差」で、間隔で書くのが自然、(2) 指数部分 $\sum y_{(i)}=\sum(n-i+1)d_i$ が間隔の線形和になり、指数関数が積に分解できて独立性が出る、(3) 無記憶性から、間隔が独立な指数分布になると予想できる。

**Q5**:「$D_i$ はどうして iid とわかるのですか」

**A5**:(独立)同時密度が $d_i$ ごとの関数の積に分解し、領域が直積($d_i>0$)になるから。(同分布)各因子は率 $n-i+1$ の指数分布の密度で、$(n-i+1)$ 倍すると率1の指数分布にそろう。$d_i$ 自体は同分布ではなく、$D_i=(n-i+1)d_i$ にして初めて i.i.d. になる。

**Q6**:「($d_1=Y_{(1)}$ は率 $n$ の指数分布なので、$D_1=nY_{(1)}\sim\mathrm{Ex}(0,1)$。…)これがよくわかりませんでした」

**A6**:3つの事実に分けて説明。(1) 最小値の生存関数 $P(Y_{(1)}>y)=\prod P(Y_i>y)=e^{-ny}$ で、率 $n$ の指数分布。(2) $d_1=y_{(1)}-y_{(0)}=y_{(1)}$($y_{(0)}=0$ と定義)。(3) $P(nY_{(1)}>t)=e^{-t}$ なので、$n$ 倍すると標準指数分布。直感は、$n$ 個が並行して待つと、最初に起きるまでの時間が $1/n$ に縮むこと。

## C. 点推定の理論に関する質問(要約)

| 質問 | 要点 |
|---|---|
| 不偏性とは | $E_\theta[\hat\theta]=\theta$ が **すべての** $\theta$ で成り立つこと。平均的に偏りがない |
| 不偏だが一致でない例 | $\hat\theta=X_1$。$n$ を増やしても分散が減らない |
| 一致だが不偏でない例 | $\bar X+1/n$、標本分散の $1/n$ 版。偏りが $n\to\infty$ で消える |
| 一致性と不偏性の違い | 不偏性は各 $n$ での平均、一致性は $n\to\infty$ で偏りもばらつきも消えること |
| なぜ線形に限定(BLUE) | 計算が簡単で、分布を仮定せず(平均と分散だけで)最良が決まる |
| ガウス・マルコフの定理 | $E[\varepsilon]=0$、$\mathrm{Var}(\varepsilon)=\sigma^2I$ だけで、OLS が線形不偏推定量の中で最良。$DX=0$ のもと、$DD^\top$ が半正定値であることで証明 |
| フィッシャー情報量の微分 | $\theta$ で微分する。$x$ を固定した対数尤度(尤度)を $\theta$ の関数として見る |
| 正則条件 | 台が $\theta$ に依存しない、微分可能、微分と積分の交換など。クラメール・ラオと漸近理論の前提 |
| クラメール・ラオの証明 | スコアの期待値0、共分散が1、コーシー・シュワルツの3段階 |
| 漸近正規性は一致性より細かい? | 分布収束は弱いが、$\sqrt n$ で拡大した量への主張。スルツキーの定理で一致性を含む |
| 傾きの分散が $nI$ | $I$ はスコアの分散(定義)、$n$ 個の独立な和なので分散は $n$ 倍 |