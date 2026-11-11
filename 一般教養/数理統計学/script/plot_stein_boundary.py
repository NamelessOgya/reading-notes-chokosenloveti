"""スタインの公式（スタインの公式.md）用の図を作成するスクリプト。

部分積分で出てくる境界項 g(z)φ(z) が |z|→∞ で 0 に近づく様子を描く。

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy python 一般教養/数理統計学/script/plot_stein_boundary.py

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


def phi(z):
    return np.exp(-(z**2) / 2) / np.sqrt(2 * np.pi)


def fig_boundary():
    z = np.linspace(0, 8, 600)
    cases = [
        (r"$g(z)=z$", z, "#5b8e7d"),
        (r"$g(z)=z^3$", z**3, "#1f4e79"),
        (r"$g(z)=z^6$", z**6, "#6a4c93"),
        (r"$g(z)=e^{2z}$", np.exp(2 * z), "#f4a259"),
        (r"$g(z)=e^{z^2/2}$（速すぎる）", np.exp(z**2 / 2), "#bc4b51"),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    ax = axes[0]
    for label, g, c in cases:
        ls = "--" if "速すぎる" in label else "-"
        ax.plot(z, g * phi(z), color=c, lw=2.2, ls=ls, label=label)
    ax.set_ylim(0, 6)
    ax.set_title(r"境界項 $g(z)\varphi(z)$（ふつうの目盛り）")
    ax.set_xlabel("$z$")
    ax.legend(fontsize=9.5)
    ax.grid(alpha=0.3)

    ax = axes[1]
    for label, g, c in cases:
        ls = "--" if "速すぎる" in label else "-"
        ax.semilogy(z, g * phi(z), color=c, lw=2.2, ls=ls, label=label)
    ax.semilogy(z, phi(z), color="gray", lw=1.5, ls=":", label=r"$\varphi(z)$ のみ")
    ax.set_ylim(1e-14, 1e3)
    ax.set_title(r"境界項 $g(z)\varphi(z)$（縦軸を対数目盛り）")
    ax.set_xlabel("$z$")
    ax.legend(fontsize=9.5, loc="lower left")
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(r"$\varphi(z)$ が急速に小さくなるので、ほとんどの $g$ で $g(z)\varphi(z)\to 0$", fontsize=13)
    fig.tight_layout()
    path = OUT_DIR / "stein_boundary_term.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"saved: {path}")


if __name__ == "__main__":
    fig_boundary()
