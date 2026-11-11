"""多変量正規分布（多変量正規分布.md）用の図を作成するスクリプト。

1. 2変量正規分布の等高線（楕円）：分散・相関によって形がどう変わるか
2. 条件付き分布と回帰直線、マハラノビス距離の2乗 ~ χ²(2)、
   「周辺分布が正規でも同時正規とは限らない」反例
3. シミュレーションによる公式の確認（標準出力）

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_multivariate_normal.py

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


def sigma_matrix(s1, s2, rho):
    return np.array([[s1**2, rho * s1 * s2], [rho * s1 * s2, s2**2]])


def maha2(grid_x, grid_y, mu, Sigma):
    inv = np.linalg.inv(Sigma)
    dx = grid_x - mu[0]
    dy = grid_y - mu[1]
    return inv[0, 0] * dx**2 + 2 * inv[0, 1] * dx * dy + inv[1, 1] * dy**2


def fig_ellipses():
    rng = np.random.default_rng(0)
    cases = [
        (1.0, 1.0, 0.0, "$\\sigma_1=\\sigma_2=1,\\ \\rho=0$\n円（無相関で分散が等しい）", BLUE),
        (1.6, 0.7, 0.0, "$\\sigma_1=1.6,\\ \\sigma_2=0.7,\\ \\rho=0$\n軸に平行な楕円（独立）", GREEN),
        (1.0, 1.0, 0.8, "$\\sigma_1=\\sigma_2=1,\\ \\rho=0.8$\n右上がりの楕円", RED),
        (1.0, 1.0, -0.6, "$\\sigma_1=\\sigma_2=1,\\ \\rho=-0.6$\n右下がりの楕円", PURPLE),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(15, 4.2))
    gx, gy = np.meshgrid(np.linspace(-4.5, 4.5, 300), np.linspace(-4.5, 4.5, 300))
    for ax, (s1, s2, rho, title, col) in zip(axes, cases):
        Sigma = sigma_matrix(s1, s2, rho)
        pts = rng.multivariate_normal([0, 0], Sigma, 350)
        ax.scatter(pts[:, 0], pts[:, 1], s=7, color=col, alpha=0.35)
        d2 = maha2(gx, gy, [0, 0], Sigma)
        cs = ax.contour(gx, gy, np.sqrt(d2), levels=[1, 2, 3], colors=[col], linewidths=[2.2, 1.6, 1.0])
        ax.clabel(cs, fmt={1: "1", 2: "2", 3: "3"}, fontsize=9)
        ax.set_aspect("equal")
        ax.set_xlim(-4.5, 4.5)
        ax.set_ylim(-4.5, 4.5)
        ax.set_title(title, fontsize=10)
        ax.set_xlabel("$x_1$")
    axes[0].set_ylabel("$x_2$")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "mvn_ellipses.png", bbox_inches="tight")
    plt.close(fig)


def fig_properties():
    rng = np.random.default_rng(1)
    rho = 0.8
    Sigma = sigma_matrix(1, 1, rho)
    n = 400_000
    pts = rng.multivariate_normal([0, 0], Sigma, n)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))

    # (A) 条件付き分布と回帰直線
    ax = axes[0]
    sub = pts[:700]
    ax.scatter(sub[:, 0], sub[:, 1], s=7, color=BLUE, alpha=0.3)
    xs = np.linspace(-3.5, 3.5, 10)
    ax.plot(xs, rho * xs, color=RED, lw=2.2, label=r"$E[X_2|X_1]=\rho x_1$")
    ax.plot(xs, xs / rho, color=GREEN, lw=2.2, label=r"$E[X_1|X_2]=\rho x_2$ の直線")
    ax.plot(xs, xs, color="gray", lw=1.2, ls="--", label="主軸（$x_2=x_1$）")
    ax.axvline(1.0, color=PURPLE, lw=1.2, ls=":")
    yy = np.linspace(-2, 3.4, 300)
    ax.plot(1.0 + 0.9 * stats.norm.pdf(yy, rho * 1.0, np.sqrt(1 - rho**2)), yy, color=PURPLE, lw=2.2,
            label=r"$X_1=1$ のときの $X_2$ の分布" "\n" r"$N(0.8,\ 0.36)$")
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect("equal")
    ax.set_title(r"条件付き分布：$X_2|X_1=x_1 \sim N(\rho x_1,\ 1-\rho^2)$", fontsize=10.5)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.legend(fontsize=8.5, loc="upper left", bbox_to_anchor=(0.0, -0.2), ncol=1)

    # (B) マハラノビス距離
    ax = axes[1]
    inv = np.linalg.inv(Sigma)
    d2 = np.einsum("ij,jk,ik->i", pts, inv, pts)
    ax.hist(d2, bins=np.linspace(0, 14, 80), density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    g = np.linspace(0.01, 14, 300)
    ax.plot(g, stats.chi2.pdf(g, 2), color=BLUE, lw=2.2, label=r"$\chi^2(2)$")
    q95 = stats.chi2.ppf(0.95, 2)
    ax.axvline(q95, color=RED, ls="--", lw=1.4)
    ax.text(q95 + 0.2, 0.3, f"{q95:.2f}\n（95%点）", color=RED, fontsize=10)
    ax.set_title(r"$(X-\mu)^\top\Sigma^{-1}(X-\mu)\ \sim\ \chi^2(2)$", fontsize=10.5)
    ax.set_xlabel("マハラノビス距離の2乗")
    ax.legend(fontsize=9.5)

    # (C) 反例
    ax = axes[2]
    x = rng.standard_normal(1500)
    s = rng.choice([-1, 1], 1500)
    y = s * x
    ax.scatter(x, y, s=7, color=PURPLE, alpha=0.4)
    ax.set_aspect("equal")
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_title("反例：$X\\sim N(0,1)$、$Y=SX$（$S=\\pm1$）\n"
                 f"周辺は両方 $N(0,1)$、相関 {np.corrcoef(x, y)[0, 1]:.2f}、でも独立でない", fontsize=10)
    ax.set_xlabel("$X$")
    ax.set_ylabel("$Y$")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "mvn_properties.png", bbox_inches="tight")
    plt.close(fig)

    return pts, Sigma, d2, q95


def check_numerics(pts, Sigma, d2, q95):
    print("標本共分散行列:\n", np.cov(pts.T).round(3))
    near = np.abs(pts[:, 0] - 1.0) < 0.02
    print(f"X1≈1 のとき X2: 平均 {pts[near, 1].mean():.3f}（公式 0.8） 分散 {pts[near, 1].var():.3f}（公式 0.36）")
    print(f"マハラノビス距離²: 平均 {d2.mean():.3f}（2） 95%点以内の割合 {np.mean(d2 <= q95):.4f}（0.95）  "
          f"KS p={stats.kstest(d2[:20000], 'chi2', args=(2,)).pvalue:.3f}")
    # 線形結合 W = X1 - X2: 分散 a^T Σ a
    a = np.array([1.0, -1.0])
    w = pts @ a
    print(f"W=X1-X2: 平均 {w.mean():.3f}（0） 分散 {w.var():.3f}（公式 {a @ Sigma @ a:.3f}）")
    # 2変量密度の値の確認
    mvn = stats.multivariate_normal([0, 0], Sigma)
    rho = 0.8
    f = 1 / (2 * np.pi * np.sqrt(1 - rho**2)) * np.exp(-(0.7**2 - 2 * rho * 0.7 * (-0.4) + 0.4**2) / (2 * (1 - rho**2)))
    print(f"密度 f(0.7, -0.4): scipy {mvn.pdf([0.7, -0.4]):.6f}  公式 {f:.6f}")
    # 独立な正規の和・スケール
    x1 = np.random.default_rng(5).normal(1, 2, 300_000)
    x2 = np.random.default_rng(6).normal(-3, 1.5, 300_000)
    s = x1 + x2
    print(f"独立な正規の和: 平均 {s.mean():.3f}（-2） 分散 {s.var():.3f}（{4 + 2.25}）")


if __name__ == "__main__":
    fig_ellipses()
    pts, Sigma, d2, q95 = fig_properties()
    check_numerics(pts, Sigma, d2, q95)
    print("saved to", OUT_DIR)
