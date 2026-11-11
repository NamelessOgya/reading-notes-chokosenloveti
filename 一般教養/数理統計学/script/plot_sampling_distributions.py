"""正規母集団からの標本分布（正規母集団の標本分布.md）用の図と数値確認を作成するスクリプト。

1. 標本平均・標本分散のシミュレーション（n=5, μ=10, σ=2）
   X̄ ~ N(μ, σ²/n)、(n-1)U²/σ² ~ χ²(n-1)、X̄ と U² は独立
2. t分布：T=(X̄-μ)/(U/√n) のシミュレーションと t(n-1) の密度、正規分布との比較
3. F分布：2標本の分散比 (U1²/σ1²)/(U2²/σ2²) のシミュレーションと F(n1-1,n2-1) の密度
4. ノートで導出した密度の式が scipy の密度と一致することの確認

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_sampling_distributions.py

出力先: 一般教養/数理統計学/images/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from scipy import special, stats

OUT_DIR = Path(__file__).resolve().parent.parent / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

_JP_FONT_CANDIDATES = [
    "Hiragino Sans",
    "Hiragino Kaku Gothic ProN",
    "Hiragino Maru Gothic Pro",
    "Noto Sans CJK JP",
    "IPAexGothic",
    "IPAGothic",
]
_available = {f.name for f in font_manager.fontManager.ttflist}
for _name in _JP_FONT_CANDIDATES:
    if _name in _available:
        plt.rcParams["font.family"] = _name
        break
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150

BLUE = "#1f4e79"
RED = "#bc4b51"
GREEN = "#5b8e7d"
PURPLE = "#6a4c93"
GRAY = "#888888"

MU, SIGMA, N = 10.0, 2.0, 5
M = 200_000  # シミュレーション回数


def t_pdf(t, k):
    """ノートで導出した t 分布の密度。"""
    c = np.exp(special.gammaln((k + 1) / 2) - special.gammaln(k / 2)) / np.sqrt(k * np.pi)
    return c * (1 + t**2 / k) ** (-(k + 1) / 2)


def f_pdf(x, d1, d2):
    """ノートで導出した F 分布の密度。"""
    logc = special.gammaln((d1 + d2) / 2) - special.gammaln(d1 / 2) - special.gammaln(d2 / 2)
    return np.exp(logc + (d1 / 2) * np.log(d1 / d2)) * x ** (d1 / 2 - 1) * (1 + d1 * x / d2) ** (-(d1 + d2) / 2)


def samples(rng, n, m, mu=MU, sigma=SIGMA):
    x = rng.normal(mu, sigma, (m, n))
    xbar = x.mean(axis=1)
    u2 = x.var(axis=1, ddof=1)
    return xbar, u2


def fig_mean_var():
    rng = np.random.default_rng(0)
    xbar, u2 = samples(rng, N, M)
    chi = (N - 1) * u2 / SIGMA**2

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))

    ax = axes[0]
    ax.hist(xbar, bins=80, density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    g = np.linspace(7, 13, 400)
    ax.plot(g, stats.norm.pdf(g, MU, SIGMA / np.sqrt(N)), color=BLUE, lw=2.2,
            label=rf"$N(\mu,\ \sigma^2/n)=N(10,\ {SIGMA**2 / N:.1f})$")
    ax.plot(g, stats.norm.pdf(g, MU, SIGMA), color=GRAY, lw=1.5, ls="--", label=r"元の分布 $N(10,\ 4)$")
    ax.set_title(r"標本平均 $\bar{X}$（$n=5$）")
    ax.set_xlabel(r"$\bar{x}$")
    ax.legend(fontsize=9)

    ax = axes[1]
    ax.hist(chi, bins=100, range=(0, 20), density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    g = np.linspace(0.01, 20, 400)
    ax.plot(g, stats.chi2.pdf(g, N - 1), color=RED, lw=2.2, label=r"$\chi^2(n-1)=\chi^2(4)$")
    ax.set_title(r"$(n-1)U^2/\sigma^2$ の分布")
    ax.set_xlabel("値")
    ax.legend(fontsize=9)

    ax = axes[2]
    idx = rng.choice(M, 3000, replace=False)
    ax.scatter(xbar[idx], u2[idx], s=5, color=PURPLE, alpha=0.4)
    c = np.corrcoef(xbar, u2)[0, 1]
    ax.set_title(rf"$(\bar{{X}},\ U^2)$ の散布図：相関 $r={c:.3f}$（独立）")
    ax.set_xlabel(r"$\bar{x}$")
    ax.set_ylabel(r"$U^2$")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "sampling_mean_var.png", bbox_inches="tight")
    plt.close(fig)

    print(f"X̄: 平均 {xbar.mean():.4f}（10） 分散 {xbar.var():.4f}（{SIGMA**2 / N:.2f}）")
    print(f"U²: 平均 {u2.mean():.4f}（4）  分散 {u2.var():.4f}（2σ⁴/(n-1)={2 * SIGMA**4 / (N - 1):.2f}）")
    print(f"(n-1)U²/σ²: KS p={stats.kstest(chi[:20000], 'chi2', args=(N - 1,)).pvalue:.3f}  corr(X̄,U²)={c:.4f}")
    # 偏差平方和の分解：Σ(Xi-μ)² = Σ(Xi-X̄)² + n(X̄-μ)²
    rng2 = np.random.default_rng(1)
    x = rng2.normal(MU, SIGMA, (5, N))
    lhs = ((x - MU) ** 2).sum(axis=1)
    rhs = ((x - x.mean(axis=1, keepdims=True)) ** 2).sum(axis=1) + N * (x.mean(axis=1) - MU) ** 2
    print("平方和の分解（左辺 - 右辺の最大絶対値）:", np.abs(lhs - rhs).max())


def fig_t():
    rng = np.random.default_rng(2)
    xbar, u2 = samples(rng, N, M)
    t = (xbar - MU) / (np.sqrt(u2) / np.sqrt(N))
    z = (xbar - MU) / (SIGMA / np.sqrt(N))

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))

    ax = axes[0]
    g = np.linspace(-6, 6, 600)
    for k, col in ((1, RED), (3, PURPLE), (10, GREEN)):
        ax.plot(g, t_pdf(g, k), color=col, lw=2, label=rf"$t({k})$")
    ax.plot(g, stats.norm.pdf(g), color=BLUE, lw=2.2, ls="--", label=r"$N(0,1)$（$k\to\infty$）")
    ax.set_title(r"$t$ 分布：自由度が大きいほど正規分布に近づく")
    ax.set_xlabel("$t$")
    ax.legend(fontsize=9)

    ax = axes[1]
    ax.hist(t, bins=200, range=(-8, 8), density=True, color=GREEN, alpha=0.5, label=r"$T=\frac{\bar{X}-\mu}{U/\sqrt{n}}$ のシミュレーション")
    g = np.linspace(-8, 8, 600)
    ax.plot(g, t_pdf(g, N - 1), color=RED, lw=2.2, label=r"$t(n-1)=t(4)$")
    ax.plot(g, stats.norm.pdf(g), color=BLUE, lw=1.8, ls="--", label=r"$N(0,1)$")
    ax.set_xlim(-8, 8)
    ax.set_title(r"$\sigma$ を $U$ で置き換えると $t(4)$：裾が重い")
    ax.set_xlabel("値")
    ax.legend(fontsize=8.5, loc="upper right")

    ax = axes[2]
    xs = np.linspace(1, 6, 100)
    tail_t = [(np.abs(t) > c).mean() for c in xs]
    tail_z = [(np.abs(z) > c).mean() for c in xs]
    ax.semilogy(xs, tail_z, color=BLUE, lw=2, label=r"$\sigma$ 既知：$Z=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}$")
    ax.semilogy(xs, tail_t, color=RED, lw=2, label=r"$\sigma$ 未知：$T$（$U$ で置き換え）")
    ax.axvline(1.96, color=GRAY, ls=":", lw=1)
    ax.text(2.05, 8e-5, "1.96", fontsize=9, color=GRAY)
    ax.set_xlabel("$c$")
    ax.set_ylabel(r"$P(|\,\cdot\,|>c)$（対数軸）")
    ax.set_title("裾の確率：$T$ のほうが極端な値が出やすい")
    ax.legend(fontsize=9, loc="lower left")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "sampling_t.png", bbox_inches="tight")
    plt.close(fig)

    ks = stats.kstest(t[:20000], "t", args=(N - 1,)).pvalue
    print(f"T: KS(t(4)) p={ks:.3f}  P(|T|>2.776)={(np.abs(t) > 2.776).mean():.4f}（t(4) の 5% 点: 0.05）"
          f"  P(|Z|>1.96)={(np.abs(z) > 1.96).mean():.4f}（0.05）  P(|T|>1.96)={(np.abs(t) > 1.96).mean():.4f}")
    print(f"T: 分散 {t.var():.3f}（k/(k-2)={4 / 2:.3f}）")


def fig_f():
    rng = np.random.default_rng(3)
    n1, n2 = 6, 11
    s1, s2 = 2.0, 3.0
    _, u1 = samples(rng, n1, M, 0.0, s1)
    _, u2 = samples(rng, n2, M, 5.0, s2)
    ratio = (u1 / s1**2) / (u2 / s2**2)
    d1, d2 = n1 - 1, n2 - 1

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))

    ax = axes[0]
    g = np.linspace(0.01, 5, 600)
    for (a, b), col in (((2, 5), RED), ((5, 10), PURPLE), ((10, 30), GREEN), ((30, 100), BLUE)):
        ax.plot(g, f_pdf(g, a, b), color=col, lw=2, label=rf"$F({a},{b})$")
    ax.set_ylim(0, 1.6)
    ax.set_title(r"$F$ 分布の形（自由度の組で変わる）")
    ax.set_xlabel("$x$")
    ax.legend(fontsize=9)

    ax = axes[1]
    ax.hist(ratio, bins=200, range=(0, 6), density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    g = np.linspace(0.01, 6, 600)
    ax.plot(g, f_pdf(g, d1, d2), color=RED, lw=2.2, label=rf"$F({d1},{d2})$")
    ax.set_xlim(0, 6)
    ax.set_title(rf"分散比 $(U_1^2/\sigma_1^2)\,/\,(U_2^2/\sigma_2^2)$（$n_1=6,\ n_2=11$）")
    ax.set_xlabel("値")
    ax.legend(fontsize=9)

    ax = axes[2]
    k = 6
    rng2 = np.random.default_rng(4)
    z = rng2.standard_normal(M)
    v = rng2.chisquare(k, M)
    t = z / np.sqrt(v / k)
    ax.hist(t**2, bins=200, range=(0, 8), density=True, color=GREEN, alpha=0.5, label=r"$T^2$（$T\sim t(6)$）")
    g = np.linspace(0.01, 8, 600)
    ax.plot(g, f_pdf(g, 1, k), color=RED, lw=2.2, label=r"$F(1,6)$")
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 1.5)
    ax.set_title(r"$t$ の2乗は $F(1,k)$")
    ax.set_xlabel("値")
    ax.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "sampling_f.png", bbox_inches="tight")
    plt.close(fig)

    print(f"F(5,10): KS p={stats.kstest(ratio[:20000], 'f', args=(d1, d2)).pvalue:.3f}  平均 {ratio.mean():.3f}"
          f"（d2/(d2-2)={d2 / (d2 - 2):.3f}）")
    print(f"T²~F(1,6): KS p={stats.kstest((t**2)[:20000], 'f', args=(1, k)).pvalue:.3f}")


def check_densities():
    g = np.linspace(-5, 5, 11)
    for k in (1, 2, 5, 30):
        print(f"t密度 k={k}: 最大誤差 {np.abs(t_pdf(g, k) - stats.t.pdf(g, k)).max():.2e}")
    x = np.linspace(0.05, 5, 11)
    for d1, d2 in ((1, 6), (5, 10), (10, 30)):
        print(f"F密度 ({d1},{d2}): 最大誤差 {np.abs(f_pdf(x, d1, d2) - stats.f.pdf(x, d1, d2)).max():.2e}")
    # 1/F ~ F(d2,d1)、F(d1,∞) → χ²(d1)/d1
    print(f"1/F: P(F(5,10)<=0.5)={stats.f.cdf(0.5, 5, 10):.4f}  P(F(10,5)>=2)={stats.f.sf(2, 10, 5):.4f}")
    print(f"F(5,1e6) vs χ²(5)/5 at 1.5: {stats.f.cdf(1.5, 5, 1_000_000):.4f} {stats.chi2.cdf(7.5, 5):.4f}")
    print(f"t(1)=Cauchy: {stats.t.cdf(1.3, 1):.4f} {stats.cauchy.cdf(1.3):.4f}")
    print(f"臨界値: t(4) 両側5% = {stats.t.ppf(0.975, 4):.3f}   F(5,10) 上側5% = {stats.f.ppf(0.95, 5, 10):.3f}")
    print("t 両側5%点:", {k: round(float(stats.t.ppf(0.975, k)), 3) for k in (1, 2, 4, 9, 29, 100)}, " 正規 1.960")
    print("F 上側5%点:", {(a, b): round(float(stats.f.ppf(0.95, a, b)), 2) for a, b in ((1, 10), (5, 10), (10, 10), (5, 5))})


def helmert(n):
    """ヘルメルト行列：第1行 (1/√n,…)、第k行は先頭の k-1 個が 1/√(k(k-1))、k番目が -(k-1)/√(k(k-1))。"""
    q = np.zeros((n, n))
    q[0, :] = 1 / np.sqrt(n)
    for k in range(2, n + 1):
        c = 1 / np.sqrt(k * (k - 1))
        q[k - 1, : k - 1] = c
        q[k - 1, k - 1] = -(k - 1) * c
    return q


def check_helmert():
    for n in (2, 3, 5, 8):
        q = helmert(n)
        print(f"ヘルメルト行列 n={n}: |QQ^T-I| 最大 {np.abs(q @ q.T - np.eye(n)).max():.1e}  det={np.linalg.det(q):+.4f}")
    q3 = helmert(3)
    print("n=3 の行列（×√6 倍）:", np.round(q3 * np.sqrt(6), 4).tolist())
    z = np.array([1.0, 2.0, 6.0])
    y = q3 @ z
    print(f"Z=(1,2,6): Y={np.round(y, 4)}  Y2²+Y3²={y[1] ** 2 + y[2] ** 2:.4f}  Σ(Z-Z̄)²={((z - z.mean()) ** 2).sum():.4f}"
          f"  Y1={y[0]:.4f}  √3·Z̄={np.sqrt(3) * z.mean():.4f}")
    rng = np.random.default_rng(5)
    n = 5
    q = helmert(n)
    zz = rng.standard_normal((300_000, n))
    yy = zz @ q.T
    print(f"n=5: Y の共分散と I の差の最大 {np.abs(np.cov(yy.T) - np.eye(n)).max():.4f}"
          f"  Σ_{{i≥2}}Y_i² と Σ(Z-Z̄)² の差の最大 {np.abs((yy[:, 1:] ** 2).sum(axis=1) - ((zz - zz.mean(axis=1, keepdims=True)) ** 2).sum(axis=1)).max():.1e}")


if __name__ == "__main__":
    fig_mean_var()
    fig_t()
    fig_f()
    check_densities()
    check_helmert()
    print("saved to", OUT_DIR)
