"""共分散と相関係数（共分散と相関係数.md）用の図を作成するスクリプト。

1. 相関係数の大きさと散布図の形（ρ ≈ 0.9, 0.4, 0, -0.9）
2. 相関係数だけでは分からない例（Y=X^2、円周上の点、外れ値1個の影響）
3. 数値例の確認（コイン2枚）

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy python 一般教養/数理統計学/script/plot_covariance_correlation.py

出力先: 一般教養/数理統計学/images/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

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


def sample_rho(x, y):
    return np.corrcoef(x, y)[0, 1]


def fig_scatter_rho():
    rng = np.random.default_rng(1)
    n = 400
    rhos = [0.9, 0.4, 0.0, -0.9]
    colors = [BLUE, GREEN, PURPLE, RED]
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.8))
    for ax, r, c in zip(axes, rhos, colors):
        cov = [[1, r], [r, 1]]
        x, y = rng.multivariate_normal([0, 0], cov, n).T
        ax.scatter(x, y, s=10, color=c, alpha=0.6)
        ax.set_title(rf"$\rho={r}$（標本 $r={sample_rho(x, y):.2f}$）", fontsize=11)
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(-3.5, 3.5)
        ax.set_aspect("equal")
        ax.set_xlabel("$X$")
    axes[0].set_ylabel("$Y$")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "correlation_scatter.png", bbox_inches="tight")
    plt.close(fig)


def fig_pitfalls():
    rng = np.random.default_rng(2)
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))

    # (1) Y = X^2
    ax = axes[0]
    x = rng.uniform(-2, 2, 300)
    y = x**2
    ax.scatter(x, y, s=10, color=BLUE, alpha=0.7)
    ax.set_title(rf"$Y=X^2$：相関 $r={sample_rho(x, y):.2f}$" "\n（完全な関係があるのに相関はほぼ $0$）", fontsize=10.5)
    ax.set_xlabel("$X$")
    ax.set_ylabel("$Y$")

    # (2) 円周
    ax = axes[1]
    th = rng.uniform(0, 2 * np.pi, 300)
    x, y = np.cos(th), np.sin(th)
    ax.scatter(x, y, s=10, color=GREEN, alpha=0.7)
    ax.set_title(rf"円周上の点：相関 $r={sample_rho(x, y):.2f}$" "\n（関係があっても相関はほぼ $0$）", fontsize=10.5)
    ax.set_xlabel("$X$")
    ax.set_aspect("equal")

    # (3) 外れ値
    ax = axes[2]
    x = rng.normal(0, 1, 50)
    y = rng.normal(0, 1, 50)
    r0 = sample_rho(x, y)
    x2 = np.append(x, 8.0)
    y2 = np.append(y, 8.0)
    r1 = sample_rho(x2, y2)
    ax.scatter(x, y, s=14, color=PURPLE, alpha=0.7)
    ax.scatter([8.0], [8.0], s=70, color=RED, zorder=5)
    ax.set_title(f"外れ値1個で相関 r が {r0:.2f} → {r1:.2f}\n（外れ値に弱い）", fontsize=10.5)
    ax.set_xlabel("$X$")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "correlation_pitfalls.png", bbox_inches="tight")
    plt.close(fig)
    return r0, r1


if __name__ == "__main__":
    # 数値例：コイン2枚。X=表の数、Y=1枚目の表(0/1)
    outcomes = [(0, 0), (1, 0), (1, 1), (2, 1)]  # (X, Y) 各 1/4
    xs = np.array([o[0] for o in outcomes], float)
    ys = np.array([o[1] for o in outcomes], float)
    cov = (xs * ys).mean() - xs.mean() * ys.mean()
    rho = cov / (xs.std() * ys.std())
    print(f"コイン2枚: E[XY]={np.mean(xs*ys)}, E[X]={xs.mean()}, E[Y]={ys.mean()}, "
          f"Cov={cov}, V[X]={xs.var()}, V[Y]={ys.var()}, rho={rho:.4f} (1/sqrt2={1/np.sqrt(2):.4f})")
    fig_scatter_rho()
    print("outlier r:", fig_pitfalls())
    print("saved to", OUT_DIR)
