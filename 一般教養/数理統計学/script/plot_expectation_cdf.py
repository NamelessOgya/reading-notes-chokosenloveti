"""期待値を分布関数で表す式（期待値を分布関数で表す式.md）用の図を作成するスクリプト。

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy python 一般教養/数理統計学/script/plot_expectation_cdf.py

出力先: 一般教養/数理統計学/images/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# ---------------------------------------------------------------------------
# 共通設定
# ---------------------------------------------------------------------------
OUT_DIR = Path(__file__).resolve().parent.parent / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 日本語フォント（macOS のヒラギノ → Linux の Noto / IPA の順に探す）
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

COLOR_CDF = "#1f4e79"     # 分布関数の線
COLOR_AREA = "#f4a259"    # 期待値に相当する面積（正）
COLOR_NEG = "#5b8e7d"     # 負の部分の面積
COLOR_MEAN = "#bc4b51"    # 期待値の位置


def save(fig, name: str) -> None:
    path = OUT_DIR / name
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"saved: {path}")


# ガンマ分布（形状2, 尺度1）: F(x) = 1 - e^{-x}(1 + x), 平均 2
def gamma2_cdf(x):
    x = np.asarray(x, dtype=float)
    return np.where(x < 0, 0.0, 1.0 - np.exp(-x) * (1.0 + x))


def gamma2_ppf(p):
    """F(x) = p となる x を二分法で求める（F の逆関数）。"""
    p = np.atleast_1d(p).astype(float)
    lo = np.zeros_like(p)
    hi = np.full_like(p, 50.0)
    for _ in range(100):
        mid = (lo + hi) / 2
        mask = gamma2_cdf(mid) < p
        lo = np.where(mask, mid, lo)
        hi = np.where(mask, hi, mid)
    return (lo + hi) / 2


# ---------------------------------------------------------------------------
# 図1: 分布関数と期待値の面積
# ---------------------------------------------------------------------------
def fig_cdf_area():
    x = np.linspace(0, 8, 500)
    F = gamma2_cdf(x)
    mean = 2.0

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.fill_between(x, F, 1, color=COLOR_AREA, alpha=0.5,
                    label=r"面積 $=\int_0^\infty (1-F(x))\,dx = E[X]$")
    ax.plot(x, F, color=COLOR_CDF, lw=2.5, label=r"分布関数 $F(x)=P(X\leq x)$")
    ax.axhline(1, color="gray", ls="--", lw=1)
    ax.axvline(mean, color=COLOR_MEAN, ls=":", lw=2, label=fr"期待値 $E[X]={mean:g}$")
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("$x$")
    ax.set_ylabel("確率")
    ax.set_title("分布関数のグラフと高さ1の線の間の面積が期待値（ガンマ分布, 平均2）")
    ax.legend(loc="lower right")
    save(fig, "cdf_area_expectation.png")


# ---------------------------------------------------------------------------
# 図2: サイコロの階段グラフ（P(X >= k) を足す）
# ---------------------------------------------------------------------------
def fig_dice_staircase():
    fig, ax = plt.subplots(figsize=(7, 4))
    for k in range(1, 7):
        h = (7 - k) / 6  # P(X >= k)
        ax.bar(k - 0.5, h, width=1.0, bottom=1 - h, color=COLOR_AREA,
               alpha=0.55, edgecolor="white", lw=1.5)
        ax.text(k - 0.5, 1 - h / 2, fr"$\frac{{{7 - k}}}{{6}}$",
                ha="center", va="center", fontsize=13, zorder=5,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
    # 分布関数（階段）
    xs = np.arange(0, 8)
    Fs = np.clip(xs / 6, 0, 1)
    ax.step(xs, Fs, where="post", color=COLOR_CDF, lw=2.5,
            label=r"分布関数 $F(x)$（サイコロ）")
    ax.axhline(1, color="gray", ls="--", lw=1)
    ax.axvline(3.5, color=COLOR_MEAN, ls=":", lw=2, label=r"$E[X]=3.5$")
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("$x$")
    ax.set_ylabel("確率")
    ax.set_title(r"各列の高さ $P(X\geq k)$ を足すと $\frac{6+5+4+3+2+1}{6}=3.5$")
    ax.legend(loc="lower right")
    save(fig, "dice_staircase.png")


# ---------------------------------------------------------------------------
# 図3: 縦に切る vs 横に切る
# ---------------------------------------------------------------------------
def fig_vertical_horizontal():
    x = np.linspace(0, 8, 500)
    F = gamma2_cdf(x)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)

    # 左: 縦に切る
    ax = axes[0]
    ax.fill_between(x, F, 1, color=COLOR_AREA, alpha=0.25)
    for x0 in np.arange(0.25, 8, 0.5):
        f0 = gamma2_cdf(x0)
        ax.add_patch(plt.Rectangle((x0 - 0.2, f0), 0.4, 1 - f0,
                                   color=COLOR_AREA, alpha=0.75, lw=0))
    ax.plot(x, F, color=COLOR_CDF, lw=2.5)
    x0 = 1.25
    ax.annotate(r"高さ $1-F(x)$", xy=(x0, (1 + gamma2_cdf(x0)) / 2),
                xytext=(3.2, 0.55), fontsize=12,
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.set_title(r"縦に切る：$\int_0^\infty (1-F(x))\,dx$")
    ax.set_xlabel("$x$")
    ax.set_ylabel("確率")

    # 右: 横に切る
    ax = axes[1]
    ax.fill_between(x, F, 1, color=COLOR_AREA, alpha=0.25)
    for p0 in np.arange(0.05, 1.0, 0.1):
        w = gamma2_ppf(p0)[0]
        ax.add_patch(plt.Rectangle((0, p0 - 0.04), w, 0.08,
                                   color=COLOR_AREA, alpha=0.75, lw=0))
    ax.plot(x, F, color=COLOR_CDF, lw=2.5)
    p0 = 0.65
    ax.annotate(r"幅 $F^{-1}(p)$", xy=(gamma2_ppf(p0)[0] / 2, p0),
                xytext=(3.5, 0.3), fontsize=12,
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.set_title(r"横に切る：$\int_0^1 F^{-1}(p)\,dp = \int x f(x)\,dx$")
    ax.set_xlabel("$x$")

    for ax in axes:
        ax.axhline(1, color="gray", ls="--", lw=1)
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 1.08)
    fig.suptitle("同じ面積を縦に切るか横に切るか", fontsize=13)
    save(fig, "vertical_vs_horizontal.png")


# ---------------------------------------------------------------------------
# 図4: 期待値の大小が面積の大小に対応する
# ---------------------------------------------------------------------------
def fig_compare_means():
    x = np.linspace(0, 10, 500)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    for ax, mean in zip(axes, [1.0, 3.0]):
        F = 1 - np.exp(-x / mean)
        ax.fill_between(x, F, 1, color=COLOR_AREA, alpha=0.5)
        ax.plot(x, F, color=COLOR_CDF, lw=2.5)
        ax.axhline(1, color="gray", ls="--", lw=1)
        ax.axvline(mean, color=COLOR_MEAN, ls=":", lw=2)
        ax.set_title(fr"指数分布 平均 {mean:g}：面積 $= {mean:g}$")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 1.08)
        ax.set_xlabel("$x$")
    axes[0].set_ylabel("確率")
    axes[0].text(4, 0.5, "すぐ1に近づく\n→ 面積が小さい", fontsize=12)
    axes[1].text(4, 0.35, "なかなか1に近づかない\n→ 面積が大きい", fontsize=12)
    save(fig, "compare_means.png")


# ---------------------------------------------------------------------------
# 図5: 負の値もとる場合（正規分布）
# ---------------------------------------------------------------------------
def fig_negative():
    from math import erf, sqrt

    mu, sigma = 1.0, 1.5
    x = np.linspace(-5, 7, 600)
    F = np.array([0.5 * (1 + erf((xi - mu) / (sigma * sqrt(2)))) for xi in x])

    fig, ax = plt.subplots(figsize=(8, 4))
    pos = x >= 0
    neg = x <= 0
    ax.fill_between(x[pos], F[pos], 1, color=COLOR_AREA, alpha=0.55,
                    label=r"$+\int_0^\infty (1-F(x))\,dx$")
    ax.fill_between(x[neg], 0, F[neg], color=COLOR_NEG, alpha=0.55,
                    label=r"$-\int_{-\infty}^0 F(x)\,dx$")
    ax.plot(x, F, color=COLOR_CDF, lw=2.5, label="分布関数 $F(x)$")
    ax.axhline(1, color="gray", ls="--", lw=1)
    ax.axvline(0, color="black", lw=1)
    ax.axvline(mu, color=COLOR_MEAN, ls=":", lw=2, label=fr"$E[X]={mu:g}$")
    ax.set_xlim(-5, 7)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("$x$")
    ax.set_ylabel("確率")
    ax.set_title(r"負の値もとる場合（正規分布 $N(1, 1.5^2)$）：オレンジ − 緑 = 期待値")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "negative_values.png")


# ---------------------------------------------------------------------------
# 図6: マルコフの不等式
# ---------------------------------------------------------------------------
def fig_markov():
    x = np.linspace(0, 8, 500)
    F = gamma2_cdf(x)
    a = 3.0
    tail = 1 - gamma2_cdf(a)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.fill_between(x, F, 1, color=COLOR_AREA, alpha=0.35,
                    label=r"面積 $=E[X]$")
    ax.add_patch(plt.Rectangle((0, 1 - tail), a, tail, color=COLOR_MEAN,
                               alpha=0.6, lw=0,
                               label=r"長方形：幅 $a$ × 高さ $P(X>a)$"))
    ax.plot(x, F, color=COLOR_CDF, lw=2.5, label="分布関数 $F(x)$")
    ax.axhline(1, color="gray", ls="--", lw=1)
    ax.axvline(a, color="black", ls=":", lw=1)
    ax.text(a + 0.05, 0.03, "$a$", fontsize=13)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("$x$")
    ax.set_ylabel("確率")
    ax.set_title(r"長方形は面積に収まる：$a\,P(X>a) \leq E[X]$")
    ax.legend(loc="lower right")
    save(fig, "markov_inequality.png")


if __name__ == "__main__":
    fig_cdf_area()
    fig_dice_staircase()
    fig_vertical_horizontal()
    fig_compare_means()
    fig_negative()
    fig_markov()
