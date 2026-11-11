"""積率母関数を使った正規性の証明（積率母関数を使った正規性の証明.md）用の図を作成するスクリプト。

二項分布 B(n, p) を標準化した Y = (X - np)/sqrt(np(1-p)) について、
1. 積率母関数 M_Y(t) が n とともに e^{t^2/2} に近づく様子
2. log M_Y(t) - t^2/2 が n とともに 0 に近づく様子（誤差は 1/sqrt(n) のオーダー）
を描く。数値表も標準出力に表示する。

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy python 一般教養/数理統計学/script/plot_mgf_normality.py

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

COLORS = ["#f4a259", "#5b8e7d", "#6a4c93", "#1f4e79"]


def log_mgf(n, p, t):
    """log M_Y(t) = -t*np/s + n*log(p*e^u + 1 - p),  s = sqrt(np(1-p)), u = t/s。"""
    s = np.sqrt(n * p * (1 - p))
    u = t / s
    return -t * n * p / s + n * np.log(p * np.exp(u) + 1 - p)


def print_table():
    print("p=0.5, t=1  (e^{1/2} =", np.exp(0.5), ")")
    for n in [10, 100, 1000, 10000]:
        print(f"  n={n:6d}  M_Y(1) = {np.exp(log_mgf(n, 0.5, 1.0)):.6f}")
    print("p=0.2, t=1")
    for n in [10, 100, 1000, 10000]:
        print(f"  n={n:6d}  M_Y(1) = {np.exp(log_mgf(n, 0.2, 1.0)):.6f}")


def fig_mgf():
    p = 0.3
    ns = [5, 20, 100, 1000]
    t = np.linspace(-3, 3, 600)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    ax = axes[0]
    for n, c in zip(ns, COLORS):
        ax.plot(t, np.exp(log_mgf(n, p, t)), color=c, lw=1.8, label=f"$n={n}$")
    ax.plot(t, np.exp(t**2 / 2), color="black", lw=2.4, ls="--", label=r"$e^{t^2/2}$（$N(0,1)$）")
    ax.set_title(rf"積率母関数 $M_Y(t)$（$p={p}$）")
    ax.set_xlabel("$t$")
    ax.set_ylim(0, 95)
    ax.legend(fontsize=9.5, loc="upper center")

    ax = axes[1]
    nn = np.logspace(1, 5, 100)
    for t0, c in zip([0.5, 1.0, 2.0], ["#5b8e7d", "#6a4c93", "#bc4b51"]):
        diff = log_mgf(nn, p, t0) - t0**2 / 2
        ax.plot(nn, diff, color=c, lw=2, label=f"$t={t0}$")
    ax.axhline(0, color="black", lw=1, ls="--")
    ax.set_xscale("log")
    ax.set_title(r"誤差 $\log M_Y(t) - t^2/2$：$n$ が大きいほど $0$ に近づく")
    ax.set_xlabel("$n$（対数目盛り）")
    ax.legend(fontsize=9.5, loc="upper right")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "mgf_normality.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    print_table()
    fig_mgf()
    print("saved to", OUT_DIR)
