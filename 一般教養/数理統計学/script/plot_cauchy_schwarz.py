"""コーシー・シュワルツの不等式（コーシー・シュワルツの不等式.md）用の図を作成するスクリプト。

1. 判別式による証明：q(t) = E[(X - tY)^2] = E[X^2] - 2E[XY]t + E[Y^2]t^2 のグラフ
   （不等式が成り立つ場合・等号の場合・成り立たない場合）
2. 内積としての意味：|a・b| = |a||b|cosθ ≤ |a||b|

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy python 一般教養/数理統計学/script/plot_cauchy_schwarz.py

出力先: 一般教養/数理統計学/images/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Arc

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


def fig_cs():
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8))

    # 左：判別式
    ax = axes[0]
    t = np.linspace(-1.2, 3.2, 600)
    # q(t) = A - 2Bt + C t^2   （A=E[X^2], B=E[XY], C=E[Y^2]）
    cases = [
        (r"$E[XY]^2 < E[X^2]E[Y^2]$（ふつう）", 2.0, 1.0, 1.5, "#1f4e79", "-"),
        (r"$E[XY]^2 = E[X^2]E[Y^2]$（等号：$X = cY$）", 1.0, 1.0, 1.0, "#5b8e7d", "-"),
        (r"$E[XY]^2 > E[X^2]E[Y^2]$（あり得ない）", 1.0, 1.5, 1.0, "#bc4b51", "--"),
    ]
    for label, A, B, C, col, ls in cases:
        ax.plot(t, A - 2 * B * t + C * t**2, color=col, lw=2.2, ls=ls, label=label)
    ax.axhline(0, color="black", lw=1.2)
    ax.set_ylim(-1.4, 4.5)
    ax.set_title(r"$q(t)=E[(X-tY)^2]$ は $0$ 未満にならない")
    ax.set_xlabel("$t$")
    ax.set_ylabel("$q(t)$")
    ax.legend(fontsize=9.2, loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=1)

    # 右：内積
    ax = axes[1]
    a = np.array([4.0, 1.5])
    b = np.array([2.0, 3.0])
    proj = (a @ b) / (b @ b) * b
    ax.annotate("", xy=a, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="#1f4e79", lw=2.4))
    ax.annotate("", xy=b, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="#bc4b51", lw=2.4))
    ax.plot([a[0], proj[0]], [a[1], proj[1]], color="gray", ls="--", lw=1.4)
    ax.plot([0, proj[0]], [0, proj[1]], color="#6a4c93", lw=5, alpha=0.5, solid_capstyle="butt")
    ax.text(a[0] + 0.1, a[1] - 0.1, r"$\vec{a}$", color="#1f4e79", fontsize=15, va="top")
    ax.text(b[0] - 0.15, b[1] + 0.12, r"$\vec{b}$", color="#bc4b51", fontsize=15, ha="right")
    ax.annotate(r"$\vec{a}$ を $\vec{b}$ 方向へ" "\n" r"射影した長さ $=|\vec{a}|\cos\theta$",
                xy=(proj[0] * 0.5, proj[1] * 0.5), xytext=(3.3, 3.2),
                color="#6a4c93", fontsize=10,
                arrowprops=dict(arrowstyle="->", color="#6a4c93"))
    th_a = np.degrees(np.arctan2(a[1], a[0]))
    th_b = np.degrees(np.arctan2(b[1], b[0]))
    ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=th_a, theta2=th_b, color="black", lw=1.4))
    ax.text(1.0, 0.95, r"$\theta$", fontsize=14)
    ax.set_xlim(-0.5, 6.4)
    ax.set_ylim(-0.6, 4.2)
    ax.set_aspect("equal")
    ax.axhline(0, color="lightgray", lw=0.8)
    ax.axvline(0, color="lightgray", lw=0.8)
    ax.set_title(r"内積 $\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta \leq |\vec{a}||\vec{b}|$")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "cauchy_schwarz.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    # 数値例の確認：a=(1,2,3), b=(4,5,6)
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("(a·b)^2 =", (a @ b) ** 2, " |a|^2|b|^2 =", (a @ a) * (b @ b))
    fig_cs()
    print("saved to", OUT_DIR)
