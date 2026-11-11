"""2次元の変数変換（2次元の変数変換とヤコビアン.md）用の図を作成するスクリプト。

1. ヤコビアン＝面積の拡大率（1次変換の平行四辺形、極座標の小さな領域）
2. ガンマ分布 Ga(2,1), Ga(3,1) の和 U=X1+X2 と比 V=X1/(X1+X2) のシミュレーション確認
   （U ~ Ga(5,1)、V ~ Be(2,3)、U と V は独立）
3. 極座標変換のシミュレーション確認（標準正規分布2個 → R^2 ~ Exp(1/2)、Θ ~ U(0,2π)）

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_jacobian.py

出力先: 一般教養/数理統計学/images/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Polygon
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


def fig_area_scaling():
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.2))

    # 左：1次変換
    ax = axes[0]
    A = np.array([[2.0, 1.0], [0.5, 1.5]])
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], float)
    img = sq @ A.T
    ax.add_patch(Polygon(sq, closed=True, fc=BLUE, ec=BLUE, alpha=0.35, lw=2))
    ax.add_patch(Polygon(img, closed=True, fc=RED, ec=RED, alpha=0.3, lw=2))
    ax.annotate("", xy=img[1], xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8))
    ax.annotate("", xy=img[3], xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8))
    ax.text(0.5, 0.45, "面積 1", ha="center", color=BLUE, fontsize=11)
    ax.text(1.5, 1.05, "面積 $|\\det A|=2.5$", ha="center", color=RED, fontsize=11)
    ax.text(2.1, 0.25, r"$A\vec{e}_1=(2,\,0.5)$", color=RED, fontsize=10)
    ax.text(-0.15, 1.75, r"$A\vec{e}_2=(1,\,1.5)$", color=RED, fontsize=10, ha="right")
    ax.set_xlim(-1.4, 3.6)
    ax.set_ylim(-0.4, 2.6)
    ax.set_aspect("equal")
    ax.axhline(0, color="lightgray", lw=0.8)
    ax.axvline(0, color="lightgray", lw=0.8)
    ax.set_title(r"1次変換 $\vec{y}=A\vec{x}$：単位正方形 → 平行四辺形" "\n" r"$A=[[2,\ 1],\ [0.5,\ 1.5]]$、面積は $|\det A|$ 倍")

    # 右：極座標
    ax = axes[1]
    r1, r2, t1, t2 = 1.5, 2.3, 0.5, 1.1
    th = np.linspace(0, np.pi / 2, 200)
    for r in np.arange(0.5, 3.1, 0.5):
        ax.plot(r * np.cos(th), r * np.sin(th), color="lightgray", lw=0.7)
    for t in np.linspace(0, np.pi / 2, 10):
        ax.plot([0, 3 * np.cos(t)], [0, 3 * np.sin(t)], color="lightgray", lw=0.7)
    tt = np.linspace(t1, t2, 60)
    rr = np.linspace(r1, r2, 30)
    outer = np.c_[r2 * np.cos(tt), r2 * np.sin(tt)]
    inner = np.c_[r1 * np.cos(tt[::-1]), r1 * np.sin(tt[::-1])]
    patch = np.vstack([outer, inner])
    ax.add_patch(Polygon(patch, closed=True, fc=PURPLE, ec=PURPLE, alpha=0.4, lw=2))
    rm = (r1 + r2) / 2
    ax.annotate(r"$\Delta r$", xy=(r2 * np.cos(t2) + 0.0, r2 * np.sin(t2)), xytext=(1.0, 2.5),
                fontsize=12, color=PURPLE, arrowprops=dict(arrowstyle="->", color=PURPLE))
    ax.text(2.0, 3.0, r"面積 $\approx r\,\Delta r\,\Delta\theta$" "\n" r"（$r$ が大きいほど" "\n" r" 横幅 $r\Delta\theta$ が広い）",
            color=PURPLE, fontsize=10.5, va="top")
    ax.plot([0, 3], [0, 0], color="black", lw=0.8)
    ax.plot([0, 0], [0, 3], color="black", lw=0.8)
    ax.set_xlim(-0.2, 3.7)
    ax.set_ylim(-0.2, 3.1)
    ax.set_aspect("equal")
    ax.set_title(r"極座標 $(x,y)=(r\cos\theta,\ r\sin\theta)$：$dx\,dy=r\,dr\,d\theta$")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "jacobian_area.png", bbox_inches="tight")
    plt.close(fig)

    exact = 0.5 * (r2**2 - r1**2) * (t2 - t1)
    approx = rm * (r2 - r1) * (t2 - t1)
    print(f"極座標の小領域の面積: 厳密 {exact:.4f}  r̄ΔrΔθ {approx:.4f}")


def fig_gamma_beta():
    rng = np.random.default_rng(0)
    n = 300_000
    x1 = rng.gamma(2.0, 1.0, n)
    x2 = rng.gamma(3.0, 1.0, n)
    u = x1 + x2
    v = x1 / (x1 + x2)

    fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.4))

    ax = axes[0]
    ax.hist(u, bins=80, density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    g = np.linspace(0.01, 18, 400)
    ax.plot(g, stats.gamma.pdf(g, 5), color=BLUE, lw=2.2, label=r"$Ga(5,1)$")
    ax.set_title(r"$U=X_1+X_2$ の分布")
    ax.set_xlabel("$u$")
    ax.legend(fontsize=9.5)

    ax = axes[1]
    ax.hist(v, bins=80, density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    b = np.linspace(0.001, 0.999, 400)
    ax.plot(b, stats.beta.pdf(b, 2, 3), color=RED, lw=2.2, label=r"$Be(2,3)$")
    ax.set_title(r"$V=X_1/(X_1+X_2)$ の分布")
    ax.set_xlabel("$v$")
    ax.legend(fontsize=9.5)

    ax = axes[2]
    idx = rng.choice(n, 3000, replace=False)
    ax.scatter(u[idx], v[idx], s=5, color=PURPLE, alpha=0.5)
    c = np.corrcoef(u, v)[0, 1]
    ax.set_title(rf"$(U,V)$ の散布図：相関 $r={c:.3f}$（独立）")
    ax.set_xlabel("$u$")
    ax.set_ylabel("$v$")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "jacobian_gamma_beta.png", bbox_inches="tight")
    plt.close(fig)

    print(f"U: 平均 {u.mean():.3f}（5） 分散 {u.var():.3f}（5）")
    print(f"V: 平均 {v.mean():.4f}（0.4） 分散 {v.var():.5f}（0.04）")
    print(f"corr(U,V)={c:.4f}  KS(U,Ga(5,1)) p={stats.kstest(u[:20000], 'gamma', args=(5,)).pvalue:.3f}"
          f"  KS(V,Be(2,3)) p={stats.kstest(v[:20000], 'beta', args=(2, 3)).pvalue:.3f}")


def check_polar():
    rng = np.random.default_rng(1)
    n = 500_000
    z1 = rng.standard_normal(n)
    z2 = rng.standard_normal(n)
    r2 = z1**2 + z2**2
    th = np.arctan2(z2, z1) % (2 * np.pi)
    print(f"R^2: 平均 {r2.mean():.3f}（2） 分散 {r2.var():.3f}（4）  "
          f"KS(R^2, Exp(1/2)) p={stats.kstest(r2[:20000], 'expon', args=(0, 2)).pvalue:.3f}")
    print(f"Θ: 平均 {th.mean():.3f}（π={np.pi:.3f}）  KS(Θ, U(0,2π)) p="
          f"{stats.kstest(th[:20000], 'uniform', args=(0, 2*np.pi)).pvalue:.3f}  corr(R^2, Θ)={np.corrcoef(r2, th)[0,1]:.4f}")


if __name__ == "__main__":
    fig_area_scaling()
    fig_gamma_beta()
    check_polar()
    print("saved to", OUT_DIR)
