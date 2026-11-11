"""変数変換（n次元の変数変換とヤコビアン.md）用の図を作成するスクリプト。

1. 1次変換 Y = 2X + 1（X ~ N(0,1)）で、密度が横に2倍伸びて高さが半分になる様子
2. Y = X^2（X ~ N(0,1)）のシミュレーションのヒストグラムと、変数変換で求めた密度の比較

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_change_of_variables.py

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


def fig_change_of_variables():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    # 左：1次変換
    ax = axes[0]
    x = np.linspace(-6, 8, 1000)
    ax.plot(x, norm.pdf(x), color="#1f4e79", lw=2.2, label=r"$X \sim N(0,1)$ の密度")
    ax.plot(x, norm.pdf(x, loc=1, scale=2), color="#bc4b51", lw=2.2,
            label=r"$Y = 2X+1$ の密度 $= \frac{1}{2} f_X\!\left(\frac{y-1}{2}\right)$")
    # 対応する区間 [0, 0.5] → [1, 2]
    xs = np.linspace(0, 0.5, 100)
    ax.fill_between(xs, norm.pdf(xs), color="#1f4e79", alpha=0.35)
    ys = np.linspace(1, 2, 100)
    ax.fill_between(ys, norm.pdf(ys, loc=1, scale=2), color="#bc4b51", alpha=0.35)
    ax.annotate(r"$X \in [0, 0.5]$（幅 0.5）", xy=(0.25, 0.25), xytext=(-5.6, 0.3),
                fontsize=10, color="#1f4e79",
                arrowprops=dict(arrowstyle="->", color="#1f4e79"))
    ax.annotate(r"$Y \in [1, 2]$（幅 1＝2倍）", xy=(1.5, 0.12), xytext=(3.2, 0.26),
                fontsize=10, color="#bc4b51",
                arrowprops=dict(arrowstyle="->", color="#bc4b51"))
    ax.set_title("1次変換：横に2倍伸びる → 高さは半分（面積＝確率は同じ）")
    ax.set_xlabel("値")
    ax.set_ylim(0, 0.5)
    ax.legend(fontsize=9.5, loc="upper right")

    # 右：Y = X^2
    ax = axes[1]
    rng = np.random.default_rng(0)
    samples = rng.standard_normal(200_000) ** 2
    bins = np.linspace(0, 6, 61)
    ax.hist(samples, bins=bins, density=True, color="#5b8e7d", alpha=0.45,
            label=r"$X^2$ のシミュレーション（20万個）")
    y = np.linspace(0.02, 6, 600)
    ax.plot(y, np.exp(-y / 2) / np.sqrt(2 * np.pi * y), color="#6a4c93", lw=2.4,
            label=r"変数変換の結果 $\frac{1}{\sqrt{2\pi y}}e^{-y/2}$")
    ax.set_title(r"非線形変換 $Y = X^2$：$0$ の近くに押し込められて密度が高くなる")
    ax.set_xlabel("$y$")
    ax.set_ylim(0, 2.0)
    ax.legend(fontsize=9.5, loc="upper right")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "change_of_variables_density.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_change_of_variables()
    print("saved to", OUT_DIR)
