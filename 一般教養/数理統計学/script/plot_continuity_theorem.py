"""連続性定理（連続性定理.md）用の図を作成するスクリプト。

1. 特性関数が収束すると分布も収束する例（±1 の和を √n で割ったもの → 標準正規分布）
2. 極限の特性関数が t=0 で連続でないと分布が収束しない例（N(0, n)）

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_continuity_theorem.py

出力先: 一般教養/数理統計学/images/
"""

from math import comb
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

COLORS = ["#f4a259", "#5b8e7d", "#6a4c93", "#1f4e79"]
NS = [1, 4, 16, 64]


def rademacher_cdf(n, z):
    """S_n = (X_1+...+X_n)/√n（X_i = ±1 が確率 1/2）の分布関数を z で評価。"""
    # S_n = (2K - n)/√n, K ~ Bin(n, 1/2)
    ks = np.arange(n + 1)
    vals = (2 * ks - n) / np.sqrt(n)
    probs = np.array([comb(n, int(k)) for k in ks], dtype=float) / 2**n
    cum = np.cumsum(probs)
    idx = np.searchsorted(vals, z, side="right") - 1
    out = np.where(idx >= 0, cum[np.clip(idx, 0, n)], 0.0)
    return out


def fig_clt():
    t = np.linspace(-6, 6, 1200)
    z = np.linspace(-3.5, 3.5, 2000)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    ax = axes[0]
    for n, c in zip(NS, COLORS):
        ax.plot(t, np.cos(t / np.sqrt(n)) ** n, color=c, lw=1.8, label=f"$n={n}$")
    ax.plot(t, np.exp(-(t**2) / 2), color="black", lw=2.4, ls="--",
            label=r"$e^{-t^2/2}$（$N(0,1)$）")
    ax.axhline(0, color="gray", lw=0.6)
    ax.set_title(r"特性関数 $\varphi_n(t)=\cos^n(t/\sqrt{n})$")
    ax.set_xlabel("$t$")
    ax.set_ylim(-1.1, 1.15)
    ax.legend(fontsize=9.5, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=5)

    ax = axes[1]
    for n, c in zip(NS, COLORS):
        ax.plot(z, rademacher_cdf(n, z), color=c, lw=1.6, label=f"$n={n}$")
    ax.plot(z, norm.cdf(z), color="black", lw=2.4, ls="--", label=r"$\Phi(z)$（$N(0,1)$）")
    ax.set_title(r"分布関数 $P(S_n \leq z)$")
    ax.set_xlabel("$z$")
    ax.legend(fontsize=9.5, loc="upper left")

    fig.suptitle(r"$\pm1$ を $n$ 個足して $\sqrt{n}$ で割る：特性関数が近づく ⇒ 分布も近づく",
                 fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "continuity_clt.png", bbox_inches="tight")
    plt.close(fig)


def fig_counterexample():
    t = np.linspace(-3, 3, 1200)
    x = np.linspace(-25, 25, 2000)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    ax = axes[0]
    for n, c in zip(NS, COLORS):
        ax.plot(t, np.exp(-n * t**2 / 2), color=c, lw=1.8, label=f"$n={n}$")
    ax.plot(0, 1, "o", color="black", ms=7, zorder=5)
    ax.plot([-3, -0.03], [0, 0], color="black", lw=2.4, ls="--")
    ax.plot([0.03, 3], [0, 0], color="black", lw=2.4, ls="--", label="極限（$t=0$ だけ 1）")
    ax.set_title(r"特性関数 $\varphi_n(t)=e^{-nt^2/2}$：極限が $t=0$ で不連続")
    ax.set_xlabel("$t$")
    ax.set_ylim(-0.1, 1.15)
    ax.legend(fontsize=9.5, loc="upper right")

    ax = axes[1]
    for n, c in zip(NS, COLORS):
        ax.plot(x, norm.pdf(x, scale=np.sqrt(n)), color=c, lw=1.8, label=f"$N(0,{n})$")
    ax.set_title("密度：どんどん平たくなり、確率が無限遠へ逃げる")
    ax.set_xlabel("$x$")
    ax.legend(fontsize=9.5, loc="upper right")

    fig.suptitle(r"反例 $X_n \sim N(0,n)$：特性関数は各点で収束するが、分布は収束しない", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "continuity_counterexample.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_clt()
    fig_counterexample()
    print("saved to", OUT_DIR)
