"""確率変数と分布の収束（確率変数と分布の収束.md）用の図と数値確認を作成するスクリプト。

1. マルコフ・チェビシェフの不等式：真の裾確率と上界の比較
2. 大数の弱法則（チェビシェフによる上界）と、「確率収束するが平均二乗収束しない」例
3. 中心極限定理：標準化した標本平均（指数分布）とコルモゴロフ距離の減衰
4. スラツキーの定理：t統計量の裾確率が n とともに正規分布に近づく様子
5. デルタ法：g(x)=1/x の線形化と、1/X̄ の分布の正規近似
6. 分散安定化変換：ポアソン（√）と二項（arcsin√）、相関係数（フィッシャーの z）

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_convergence.py

出力先: 一般教養/数理統計学/images/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from scipy import stats

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


# ---------------------------------------------------------------- 1. 不等式
def fig_inequalities():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    ax = axes[0]
    a = np.linspace(0.5, 6, 300)
    ax.plot(a, np.exp(-a), color=BLUE, lw=2.4, label=r"真の値 $P(X\geq a)=e^{-a}$")
    ax.plot(a, np.minimum(1, 1 / a), color=RED, lw=2.4, ls="--", label=r"マルコフの上界 $E[X]/a=1/a$")
    ax.set_yscale("log")
    ax.set_ylim(1e-3, 1.5)
    ax.set_xlabel("$a$")
    ax.set_title(r"マルコフの不等式（$X\sim Exp(1)$、$E[X]=1$）")
    ax.legend(loc="lower left", fontsize=9.5)

    ax = axes[1]
    k = np.linspace(1, 5, 300)
    ax.plot(k, 2 * stats.norm.sf(k), color=BLUE, lw=2.4, label=r"$N(0,1)$：$P(|X-\mu|\geq k\sigma)$")
    ax.plot(k, stats.expon.sf(1 + k) + np.where(k < 1, 1 - stats.expon.cdf(1 - k), 0.0), color=GREEN, lw=2.4,
            label=r"$Exp(1)$（$\mu=\sigma=1$）")
    ax.plot(k, np.minimum(1, 1 / k**2), color=RED, lw=2.4, ls="--", label=r"チェビシェフの上界 $1/k^2$")
    ax.set_yscale("log")
    ax.set_ylim(1e-6, 1.5)
    ax.set_xlabel(r"$k$（標準偏差の何倍か）")
    ax.set_title("チェビシェフの不等式")
    ax.legend(loc="lower left", fontsize=9.5)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "convergence_inequalities.png", bbox_inches="tight")
    plt.close(fig)

    print("マルコフ Exp(1): P(X>=3)=%.4f  上界 1/3=%.4f" % (np.exp(-3), 1 / 3))
    print("チェビシェフ k=2: N(0,1) %.4f  Exp(1) %.4f  上界 %.2f" % (2 * stats.norm.sf(2), stats.expon.sf(3), 0.25))
    # 上界がちょうど達成される分布：P(X=±k)=1/(2k^2), P(X=0)=1-1/k^2（k=2）
    k0 = 2.0
    p = 1 / (2 * k0**2)
    x = np.array([-k0, 0, k0])
    pr = np.array([p, 1 - 2 * p, p])
    print("等号が成り立つ分布（k=2）: 分散 %.3f  P(|X|>=2)=%.3f  1/k^2=%.3f" % ((pr * x**2).sum(), pr[[0, 2]].sum(), 1 / k0**2))


# ---------------------------------------------------------------- 2. 大数の弱法則・収束の関係
def fig_lln():
    eps = 0.2
    n = np.arange(1, 401)
    # Exp(1) の標本平均 ~ Ga(n, n)：厳密に計算
    prob = 1 - (stats.gamma.cdf(n * (1 + eps), n) - stats.gamma.cdf(n * (1 - eps), n))
    cheb = np.minimum(1, 1 / (n * eps**2))

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    ax = axes[0]
    ax.plot(n, prob, color=BLUE, lw=2.4, label=r"真の値 $P(|\bar{X}_n-\mu|>\varepsilon)$")
    ax.plot(n, cheb, color=RED, lw=2.4, ls="--", label=r"チェビシェフの上界 $\sigma^2/(n\varepsilon^2)$")
    ax.set_yscale("log")
    ax.set_ylim(1e-6, 1.5)
    ax.set_xlabel("$n$")
    ax.set_title(r"大数の弱法則（$X_i\sim Exp(1)$、$\varepsilon=0.2$）")
    ax.legend(loc="lower left", fontsize=9.5)

    ax = axes[1]
    m = np.arange(1, 201)
    ax.plot(m, 1 / m, color=BLUE, lw=2.4, label=r"$P(|X_n|>\varepsilon)=1/n\ \to\ 0$（確率収束する）")
    ax.plot(m, m, color=RED, lw=2.4, label=r"$E[X_n^2]=n\ \to\ \infty$（平均二乗収束しない）")
    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_xlabel("$n$")
    ax.set_title(r"反例：$X_n=n$（確率 $1/n$）、$0$（確率 $1-1/n$）")
    ax.legend(loc="upper center", fontsize=9.5, bbox_to_anchor=(0.5, 0.97))
    ax.set_ylim(5e-3, 400)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "convergence_lln.png", bbox_inches="tight")
    plt.close(fig)

    for nn in (10, 50, 100, 400):
        print(f"WLLN n={nn}: 真の P={prob[nn - 1]:.2e}  チェビシェフ上界={cheb[nn - 1]:.3f}")
    # D⇏P：X_n=-X
    print("D⇏P: X~N(0,1), X_n=-X, P(|X_n-X|>0.5)=%.4f（n によらず一定）" % (2 * stats.norm.sf(0.25)))


# ---------------------------------------------------------------- 3. 中心極限定理
def fig_clt():
    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))
    g = np.linspace(-4, 4, 400)

    for ax, n, col in zip(axes[:2], (2, 30), (PURPLE, GREEN)):
        x = rng.exponential(1.0, (200_000, n))
        z = np.sqrt(n) * (x.mean(axis=1) - 1.0)  # σ=1
        ax.hist(z, bins=120, range=(-4, 4), density=True, color=col, alpha=0.5, label=r"$\sqrt{n}(\bar{X}_n-\mu)/\sigma$")
        ax.plot(g, stats.norm.pdf(g), color=BLUE, lw=2.2, label=r"$N(0,1)$")
        ax.set_title(rf"$n={n}$（元の分布は $Exp(1)$：右に歪んでいる）")
        ax.set_xlabel("値")
        ax.legend(fontsize=9)

    ax = axes[2]
    ns = np.unique(np.logspace(0, 3, 40).astype(int))
    zz = np.linspace(-6, 6, 4001)
    d = []
    for n in ns:
        cdf = stats.gamma.cdf(n + zz * np.sqrt(n), n)  # √n(X̄-1) の厳密な累積分布関数
        d.append(np.abs(cdf - stats.norm.cdf(zz)).max())
    ax.loglog(ns, d, "o-", color=BLUE, ms=3, lw=1.6, label=r"累積分布関数の最大差（コルモゴロフ距離）")
    ax.loglog(ns, 0.4 / np.sqrt(ns), color=RED, ls="--", lw=1.8, label=r"$0.4/\sqrt{n}$（$n^{-1/2}$ の目安）")
    ax.set_xlabel("$n$")
    ax.set_title("正規分布への近づき方：$n^{-1/2}$ のオーダー")
    ax.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "convergence_clt.png", bbox_inches="tight")
    plt.close(fig)

    for n in (1, 2, 5, 30, 100, 1000):
        cdf = stats.gamma.cdf(n + zz * np.sqrt(n), n)
        print(f"CLT n={n}: コルモゴロフ距離 {np.abs(cdf - stats.norm.cdf(zz)).max():.4f}")


# ---------------------------------------------------------------- 4. スラツキー（t統計量）
def slutsky():
    rng = np.random.default_rng(1)
    print("スラツキー：√n(X̄-μ)/S の P(|T|>1.96)（X_i~Exp(1)、正規なら 0.05）")
    for n, reps in ((10, 200_000), (30, 200_000), (100, 100_000), (1000, 20_000)):
        x = rng.exponential(1.0, (reps, n))
        t = np.sqrt(n) * (x.mean(axis=1) - 1.0) / x.std(axis=1, ddof=1)
        z = np.sqrt(n) * (x.mean(axis=1) - 1.0)
        print(f"  n={n:<5} S の平均 {x.std(axis=1, ddof=1).mean():.4f}（σ=1）  P(|T|>1.96)={(np.abs(t) > 1.96).mean():.4f}"
              f"   P(|Z|>1.96)={(np.abs(z) > 1.96).mean():.4f}")


# ---------------------------------------------------------------- 5. デルタ法
def fig_delta():
    rng = np.random.default_rng(2)
    mu, sd = 2.0, 2.0  # Exp(平均2): μ=2, σ=2
    n = 100
    xbar = rng.exponential(mu, (300_000, n)).mean(axis=1)
    y = 1 / xbar
    gprime = -1 / mu**2
    asd = abs(gprime) * sd / np.sqrt(n)

    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8))

    ax = axes[0]
    x = np.linspace(1.4, 3.0, 300)
    ax.plot(x, 1 / x, color=BLUE, lw=2.4, label=r"$g(x)=1/x$")
    ax.plot(x, 1 / mu + gprime * (x - mu), color=RED, lw=2, ls="--", label=r"接線 $g(\mu)+g'(\mu)(x-\mu)$")
    ax.axvline(mu, color=GRAY, lw=1, ls=":")
    xs = np.linspace(mu - 3 * sd / np.sqrt(n), mu + 3 * sd / np.sqrt(n), 200)
    ax.fill_between(xs, 0.30, 0.30 + 0.5 * stats.norm.pdf(xs, mu, sd / np.sqrt(n)) / stats.norm.pdf(mu, mu, sd / np.sqrt(n)) * 0.08,
                    color=GREEN, alpha=0.5, label=r"$\bar{X}$ の分布（$n=100$）")
    ax.set_xlim(1.4, 3.0)
    ax.set_ylim(0.28, 0.72)
    ax.set_xlabel("$x$")
    ax.set_title(r"狭い範囲では接線とほぼ一致：$g(\bar{X})\approx g(\mu)+g'(\mu)(\bar{X}-\mu)$")
    ax.legend(fontsize=9.5, loc="upper right")

    ax = axes[1]
    ax.hist(y, bins=120, density=True, color=GREEN, alpha=0.5, label=r"$1/\bar{X}$ のシミュレーション")
    gg = np.linspace(0.3, 0.8, 400)
    ax.plot(gg, stats.norm.pdf(gg, 1 / mu, asd), color=BLUE, lw=2.2,
            label=rf"デルタ法：$N(1/\mu,\ g'(\mu)^2\sigma^2/n)=N(0.5,\ {asd**2:.5f})$")
    ax.set_xlabel("値")
    ax.set_title(r"$1/\bar{X}$ の分布（$X_i\sim Exp$（平均2）、$n=100$）")
    ax.legend(fontsize=9, loc="upper right")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "convergence_delta.png", bbox_inches="tight")
    plt.close(fig)

    print(f"デルタ法 1/X̄: 平均 {y.mean():.4f}（0.5） 分散 {y.var():.6f}（g'^2σ²/n={asd**2:.6f}）"
          f"  KS p={stats.kstest(y[:20000], stats.norm(0.5, asd).cdf).pvalue:.3f}")
    # 2次のデルタ法：g(x)=x^2, μ=0 のとき n(X̄)^2/σ² → χ²(1)
    z = rng.standard_normal((200_000, 50)).mean(axis=1)
    w = 50 * z**2
    print(f"2次デルタ法 g=x²,μ=0: n X̄² の平均 {w.mean():.3f}（χ²(1) の平均 1）  P(w>3.84)={(w > 3.84).mean():.4f}（0.05）")


# ---------------------------------------------------------------- 6. 分散安定化変換
def fig_vst():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    ax = axes[0]
    lam = np.linspace(0.5, 30, 120)
    k = np.arange(0, 400)
    var_x, var_sqrt = [], []
    for l in lam:
        pm = stats.poisson.pmf(k, l)
        var_x.append(l)
        m = (pm * np.sqrt(k)).sum()
        var_sqrt.append((pm * k).sum() - m**2)
    ax.plot(lam, var_x, color=RED, lw=2.4, label=r"$V[X]=\lambda$（$\lambda$ とともに増える）")
    ax.plot(lam, np.array(var_sqrt) * 4, color=BLUE, lw=2.4, label=r"$V[2\sqrt{X}]$（ほぼ一定 $\approx 1$）")
    ax.axhline(1, color=GRAY, lw=1, ls=":")
    ax.set_xlabel(r"$\lambda$（ポアソン分布の平均）")
    ax.set_title(r"ポアソン分布：$\sqrt{\cdot}$ で分散がそろう")
    ax.legend(fontsize=9.5, loc="upper left")

    ax = axes[1]
    n = 30
    p = np.linspace(0.05, 0.95, 120)
    kk = np.arange(0, n + 1)
    v_p, v_a = [], []
    for pi in p:
        pm = stats.binom.pmf(kk, n, pi)
        ph = kk / n
        v_p.append((pm * ph**2).sum() - (pm * ph).sum() ** 2)
        a = np.arcsin(np.sqrt(ph))
        v_a.append((pm * a**2).sum() - (pm * a).sum() ** 2)
    ax.plot(p, np.array(v_p) * n * 4, color=RED, lw=2.4, label=r"$4n\,V[\hat{p}]=4p(1-p)$（$p$ で変わる）")
    ax.plot(p, np.array(v_a) * n * 4, color=BLUE, lw=2.4, label=r"$4n\,V[\arcsin\sqrt{\hat{p}}]$（ほぼ一定 $\approx 1$）")
    ax.axhline(1, color=GRAY, lw=1, ls=":")
    ax.set_ylim(0, 1.4)
    ax.set_xlabel(r"$p$（二項分布 $B(30,p)$）")
    ax.set_title(r"二項分布：$\arcsin\sqrt{\cdot}$ で分散がそろう")
    ax.legend(fontsize=9.5, loc="lower center")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "convergence_vst.png", bbox_inches="tight")
    plt.close(fig)

    for l in (1, 4, 10, 30):
        pm = stats.poisson.pmf(k, l)
        m = (pm * np.sqrt(k)).sum()
        print(f"Poisson λ={l}: V[X]={l}  V[√X]={(pm * k).sum() - m**2:.4f}（1/4=0.25）  V[2√X]={4 * ((pm * k).sum() - m**2):.4f}")
    for pi in (0.1, 0.3, 0.5):
        pm = stats.binom.pmf(kk, n, pi)
        ph = kk / n
        a = np.arcsin(np.sqrt(ph))
        va = (pm * a**2).sum() - (pm * a).sum() ** 2
        print(f"Binomial n=30 p={pi}: n·V[p̂]={n * ((pm * ph**2).sum() - (pm * ph).sum() ** 2):.4f}（p(1-p)={pi * (1 - pi):.4f}）"
              f"  4n·V[arcsin√p̂]={4 * n * va:.4f}（1）")


def fisher_z():
    rng = np.random.default_rng(3)
    n = 30
    print(f"フィッシャーの z（n={n}）：V[r] と V[arctanh r]（理論 1/(n-3)={1 / (n - 3):.4f}）")
    for rho in (0.0, 0.5, 0.9):
        cov = [[1, rho], [rho, 1]]
        v = rng.multivariate_normal([0, 0], cov, (100_000, n))
        x, y = v[:, :, 0], v[:, :, 1]
        r = ((x - x.mean(1, keepdims=True)) * (y - y.mean(1, keepdims=True))).sum(1) / np.sqrt(
            ((x - x.mean(1, keepdims=True)) ** 2).sum(1) * ((y - y.mean(1, keepdims=True)) ** 2).sum(1))
        print(f"  ρ={rho}: V[r]={r.var():.4f}（(1-ρ²)²/n={(1 - rho**2) ** 2 / n:.4f}）  V[z]={np.arctanh(r).var():.4f}")


if __name__ == "__main__":
    fig_inequalities()
    fig_lln()
    fig_clt()
    slutsky()
    fig_delta()
    fig_vst()
    fisher_z()
    print("saved to", OUT_DIR)
