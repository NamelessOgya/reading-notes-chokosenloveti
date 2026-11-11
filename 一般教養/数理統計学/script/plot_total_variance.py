"""条件付き分散の公式（条件付き分散の公式.md）用の図を作成するスクリプト。

1. 混合分布 Y（X=A なら N(0,1)、X=B なら N(4,1)）：群の中のばらつきと群の平均のばらつき
2. 全分散の公式 V[Y] = E[V[Y|X]] + V[E[Y|X]] の内訳（4つの例）
3. シミュレーションによる公式の確認（標準出力）

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_total_variance.py

出力先: 一般教養/数理統計学/images/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from scipy.stats import norm

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
ORANGE = "#f4a259"


def fig_total_variance():
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))

    # 左：混合分布
    ax = axes[0]
    y = np.linspace(-4, 8, 800)
    pa = 0.5 * norm.pdf(y, 0, 1)
    pb = 0.5 * norm.pdf(y, 4, 1)
    ax.fill_between(y, pa, color=BLUE, alpha=0.25, label=r"$X=A$：$N(0,1)$（重み $\frac{1}{2}$）")
    ax.fill_between(y, pb, color=RED, alpha=0.25, label=r"$X=B$：$N(4,1)$（重み $\frac{1}{2}$）")
    ax.plot(y, pa + pb, color="black", lw=2.2, label=r"$Y$ の分布（混合）")
    for m, c in [(0, BLUE), (4, RED)]:
        ax.axvline(m, color=c, ls="--", lw=1.2)
    ax.axvline(2, color="black", ls=":", lw=1.4)
    ax.annotate("", xy=(0, 0.235), xytext=(4, 0.235),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.8))
    ax.text(2, 0.25, r"群の平均のばらつき $V[E[Y|X]]=4$", ha="center", color=PURPLE, fontsize=10.5)
    ax.annotate("", xy=(-1, 0.1), xytext=(1, 0.1),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.8))
    ax.text(-3.9, 0.15, r"群の中のばらつき" "\n" r"$V[Y|X]=1$", ha="left", color=GREEN, fontsize=10)
    ax.annotate("", xy=(-1.05, 0.115), xytext=(-2.3, 0.143),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0))
    ax.text(2.2, 0.14, r"$E[Y]=2$", fontsize=10)
    ax.set_title(r"$V[Y]=E[V[Y|X]]+V[E[Y|X]]=1+4=5$")
    ax.set_xlabel("$y$")
    ax.set_ylim(0, 0.29)
    ax.legend(fontsize=9.2, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=1)

    # 右：内訳（割合）
    ax = axes[1]
    examples = [
        ("混合分布（左図）", 1.0, 4.0),
        (r"間引き $N\sim Po(10),\ Y|N\sim B(N,0.3)$", 10 * 0.3 * 0.7, 0.09 * 10),
        (r"ポアソン-ガンマ $\Theta\sim Ga(3,1),\ Y|\Theta\sim Po(\Theta)$", 3.0, 3.0),
        (r"2変量正規 $\rho=0.6$（$\sigma_Y=1$）", 1 - 0.36, 0.36),
    ]
    labels, within, between = [], [], []
    for lab, w, b in examples:
        tot = w + b
        labels.append(lab)
        within.append(w / tot)
        between.append(b / tot)
    ypos = np.arange(len(examples))[::-1]
    ax.barh(ypos, within, color=GREEN, label=r"$E[V[Y|X]]$（群の中）")
    ax.barh(ypos, between, left=within, color=PURPLE, label=r"$V[E[Y|X]]$（群の間）")
    for yp, w, b in zip(ypos, within, between):
        ax.text(w / 2, yp, f"{w*100:.0f}%", ha="center", va="center", color="white", fontsize=10.5)
        ax.text(w + b / 2, yp, f"{b*100:.0f}%", ha="center", va="center", color="white", fontsize=10.5)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels, fontsize=9.5)
    ax.set_xlim(0, 1)
    ax.set_xlabel(r"$V[Y]$ に占める割合")
    ax.set_title(r"全分散の公式の内訳：$V[Y]$ を2つに分ける")
    ax.legend(fontsize=9.5, loc="upper center", bbox_to_anchor=(0.45, -0.17), ncol=2)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "total_variance.png", bbox_inches="tight")
    plt.close(fig)


def check_by_simulation():
    rng = np.random.default_rng(0)
    n = 1_000_000

    # (a) 混合
    x = rng.integers(0, 2, n)
    y = rng.normal(4 * x, 1)
    print(f"混合: V[Y]={y.var():.3f}（公式 5）  E[Y]={y.mean():.3f}（公式 2）")

    # (b) ランダム和  N~Po(4), X_i~U(0,6)（mu=3, sigma^2=3）
    lam, mu, s2 = 4.0, 3.0, 3.0
    cnt = rng.poisson(lam, 200_000)
    ysum = np.array([rng.uniform(0, 6, k).sum() for k in cnt])
    print(f"ランダム和: E[Y]={ysum.mean():.3f}（公式 {lam*mu}）  V[Y]={ysum.var():.3f}"
          f"（公式 {lam*s2 + lam*mu**2}）")

    # (c) 間引き
    nn = rng.poisson(10, n)
    yy = rng.binomial(nn, 0.3)
    print(f"間引き: E[Y]={yy.mean():.3f}, V[Y]={yy.var():.3f}（公式はどちらも 3）")

    # (d) ポアソン-ガンマ  Theta~Ga(3, rate=1)
    th = rng.gamma(3.0, 1.0, n)
    yp = rng.poisson(th)
    print(f"ポアソン-ガンマ: E[Y]={yp.mean():.3f}（公式 3）  V[Y]={yp.var():.3f}（公式 6）")

    # (e) 2変量正規
    rho = 0.6
    z1 = rng.standard_normal(n)
    z2 = rho * z1 + np.sqrt(1 - rho**2) * rng.standard_normal(n)
    near = np.abs(z1 - 1.0) < 0.02
    print(f"2変量正規: X≈1 のとき E[Y|X]={z2[near].mean():.3f}（公式 {rho}）  "
          f"V[Y|X]={z2[near].var():.3f}（公式 {1-rho**2}）")


if __name__ == "__main__":
    check_by_simulation()
    fig_total_variance()
    print("saved to", OUT_DIR)
