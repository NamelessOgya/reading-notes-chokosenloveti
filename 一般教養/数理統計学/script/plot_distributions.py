"""代表的な確率分布（代表的な確率分布.md）用の図を作成するスクリプト。

作成する図:
    1. distribution_relations.png : 分布どうしの関係図
    2. distribution_shapes.png    : 各分布の確率関数・確率密度関数の形
    3. distribution_limits.png    : 極限（近似）関係の数値例

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy python 一般教養/数理統計学/script/plot_distributions.py

出力先: 一般教養/数理統計学/images/
"""

from math import comb, exp, gamma, lgamma, log, pi, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# ---------------------------------------------------------------------------
# 共通設定
# ---------------------------------------------------------------------------
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

COLOR_DISCRETE = "#f4a259"    # 離散分布
COLOR_CONTINUOUS = "#5b8e7d"  # 連続分布
COLOR_AUX = "#cccccc"         # 補助的な分布（一覧に含めないもの）
COLOR_LINE = "#1f4e79"


def save(fig, name: str) -> None:
    path = OUT_DIR / name
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"saved: {path}")


# ---------------------------------------------------------------------------
# 確率関数・確率密度関数
# ---------------------------------------------------------------------------
def binom_pmf(k, n, p):
    return comb(n, k) * p**k * (1 - p) ** (n - k)


def poisson_pmf(k, lam):
    return exp(-lam + k * log(lam) - lgamma(k + 1))


def geom_pmf(k, p):  # 初めて成功するまでの失敗回数 k = 0, 1, 2, ...
    return p * (1 - p) ** k


def nbinom_pmf(k, r, p):  # r 回成功するまでの失敗回数
    return comb(r + k - 1, k) * p**r * (1 - p) ** k


def hypergeom_pmf(k, N, K, n):
    if k < max(0, n - (N - K)) or k > min(n, K):
        return 0.0
    return comb(K, k) * comb(N - K, n - k) / comb(N, n)


def normal_pdf(x, mu, sigma):
    return np.exp(-((x - mu) ** 2) / (2 * sigma**2)) / sqrt(2 * pi * sigma**2)


def gamma_pdf(x, alpha, lam):  # 形状 alpha, 率 lam
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = np.exp(alpha * log(lam) + (alpha - 1) * np.log(x[m]) - lam * x[m] - lgamma(alpha))
    return out


def chi2_pdf(x, k):
    return gamma_pdf(x, k / 2, 0.5)


def expon_pdf(x, lam):
    return gamma_pdf(x, 1.0, lam)


def weibull_pdf(x, k, eta):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0
    z = x[m] / eta
    out[m] = (k / eta) * z ** (k - 1) * np.exp(-(z**k))
    return out


def beta_pdf(x, a, b):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = (x > 0) & (x < 1)
    logB = lgamma(a) + lgamma(b) - lgamma(a + b)
    out[m] = np.exp((a - 1) * np.log(x[m]) + (b - 1) * np.log(1 - x[m]) - logB)
    return out


# ---------------------------------------------------------------------------
# 図1: 分布の関係図
# ---------------------------------------------------------------------------
NODES = {
    # key: (表示名, x, y, 種類)
    "bern": ("ベルヌーイ分布\n（1回の試行）", 0.0, 7.6, "aux"),
    "geom": ("幾何分布", 5.5, 7.6, "d"),
    "hyper": ("超幾何分布", -5.5, 5.0, "d"),
    "binom": ("二項分布", 0.0, 5.0, "d"),
    "nbinom": ("負の二項分布", 5.5, 5.0, "d"),
    "pois": ("ポアソン分布", 2.75, 2.0, "d"),
    "expon": ("指数分布", 9.5, 2.0, "c"),
    "weib": ("ワイブル分布", 14.8, 2.0, "c"),
    "norm": ("正規分布", -4.0, -1.2, "c"),
    "gamma": ("ガンマ分布", 5.5, -1.2, "c"),
    "chi2": ("カイ二乗分布", 0.75, -4.4, "c"),
    "beta": ("ベータ分布", 10.5, -4.4, "c"),
    "unif": ("一様分布\n$U(0,1)$", 15.0, -1.2, "aux"),
}

# (始点, 終点, ラベル, 種類, 曲がり具合, ラベル位置[0-1])
#   種類: "exact" = 和・変換・特別な場合（厳密な関係）
#         "limit" = 極限（近似）
#         "other" = ポアソン過程・ベイズなどの関係
EDGES = [
    ("bern", "binom", "$n$ 個の和", "exact", 0.0, 0.5),
    ("bern", "geom", "初めて成功する\nまでの失敗回数", "exact", 0.0, 0.5),
    ("geom", "nbinom", "$r$ 個の和\n（$r=1$ で幾何）", "exact", 0.0, 0.5),
    ("hyper", "binom", "$N\\to\\infty$\n（非復元→復元）", "limit", 0.0, 0.5),
    ("binom", "pois", "$n\\to\\infty,\\ np=\\lambda$", "limit", 0.0, 0.45),
    ("nbinom", "pois", "$r\\to\\infty$", "limit", 0.0, 0.45),
    ("binom", "norm", "$n$ 大\n（ド・モアブル＝\nラプラス）", "limit", 0.0, 0.5),
    ("pois", "norm", "$\\lambda$ 大", "limit", 0.0, 0.5),
    ("geom", "expon", "連続化（$p\\to 0$）", "limit", -0.2, 0.5),
    ("pois", "expon", "ポアソン過程の\n待ち時間", "other", 0.0, 0.5),
    ("expon", "gamma", "$\\alpha$ 個の和\n（$\\alpha=1$ で指数）", "exact", 0.0, 0.42),
    ("norm", "chi2", "標準正規の2乗の\n$k$ 個の和", "exact", 0.0, 0.5),
    ("gamma", "chi2", "$\\alpha=k/2,\\ \\lambda=1/2$", "exact", 0.0, 0.5),
    ("gamma", "norm", "$\\alpha$ 大", "limit", 0.0, 0.5),
    ("expon", "weib", "$X^{1/k}$ に変換\n（$k=1$ で指数）", "exact", 0.0, 0.5),
    ("gamma", "beta", "$X/(X+Y)$", "exact", 0.0, 0.5),
    ("unif", "beta", "$\\alpha=\\beta=1$ で一様\n（順序統計量）", "exact", 0.0, 0.5),
    ("binom", "beta", "共役事前分布\n（ベイズ）", "other", -0.28, 0.83),
]

EDGE_STYLE = {
    "exact": dict(color="#333333", ls="-", lw=1.8),
    "limit": dict(color="#bc4b51", ls="--", lw=1.8),
    "other": dict(color="#6a4c93", ls=":", lw=2.2),
}

BOX_W, BOX_H = 2.4, 0.95


def _clip_to_box(cx, cy, tx, ty, margin=0.12):
    """箱の中心 (cx, cy) から (tx, ty) へ向かう線が箱の枠と交わる点を返す。"""
    dx, dy = tx - cx, ty - cy
    hw, hh = BOX_W / 2 + margin, BOX_H / 2 + margin
    t = min(hw / abs(dx) if dx else np.inf, hh / abs(dy) if dy else np.inf)
    return cx + dx * t, cy + dy * t


def fig_relations():
    fig, ax = plt.subplots(figsize=(16, 11.5))
    ax.set_xlim(-7.2, 16.8)
    ax.set_ylim(-5.4, 8.6)
    ax.set_aspect("equal")
    ax.axis("off")

    # 辺
    for s, t, label, kind, rad, pos in EDGES:
        _, x1, y1, _ = NODES[s]
        _, x2, y2, _ = NODES[t]
        st = EDGE_STYLE[kind]
        # arc3 の制御点（matplotlib と同じ定義）
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        cx, cy = mx + rad * dy, my - rad * dx
        # 端点を箱の枠で切る（曲線なら制御点の方向で切る）
        p1 = _clip_to_box(x1, y1, cx, cy) if rad else _clip_to_box(x1, y1, x2, y2)
        p2 = _clip_to_box(x2, y2, cx, cy) if rad else _clip_to_box(x2, y2, x1, y1)
        arrow = FancyArrowPatch(
            p1, p2, arrowstyle="-|>", mutation_scale=20,
            connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0,
            color=st["color"], ls=st["ls"], lw=st["lw"], zorder=1,
        )
        ax.add_patch(arrow)
        # ラベル位置：2次ベジェ曲線上の点
        qx, qy = (p1[0] + p2[0]) / 2 + rad * (p2[1] - p1[1]), (p1[1] + p2[1]) / 2 - rad * (p2[0] - p1[0])
        u = pos
        lx = (1 - u) ** 2 * p1[0] + 2 * (1 - u) * u * qx + u**2 * p2[0]
        ly = (1 - u) ** 2 * p1[1] + 2 * (1 - u) * u * qy + u**2 * p2[1]
        ax.text(lx, ly, label, ha="center", va="center", fontsize=10.5,
                color=st["color"], zorder=6,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.92))

    # 節点
    for key, (name, x, y, kind) in NODES.items():
        fc = {"d": COLOR_DISCRETE, "c": COLOR_CONTINUOUS, "aux": COLOR_AUX}[kind]
        box = FancyBboxPatch((x - BOX_W / 2, y - BOX_H / 2), BOX_W, BOX_H,
                             boxstyle="round,pad=0.05,rounding_size=0.25",
                             fc=fc, ec="black", lw=1.2, zorder=4)
        ax.add_patch(box)
        ax.text(x, y, name, ha="center", va="center", fontsize=13,
                fontweight="bold" if kind != "aux" else "normal", zorder=5,
                color="white" if kind == "c" else "black")

    # 凡例（図の下に置く）
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    handles = [
        Patch(fc=COLOR_DISCRETE, ec="black", label="離散分布"),
        Patch(fc=COLOR_CONTINUOUS, ec="black", label="連続分布"),
        Patch(fc=COLOR_AUX, ec="black", label="補助（一覧外）"),
        Line2D([], [], **EDGE_STYLE["exact"], label="和・変換・特別な場合（厳密）"),
        Line2D([], [], **EDGE_STYLE["limit"], label="極限（近似）"),
        Line2D([], [], **EDGE_STYLE["other"], label="ポアソン過程・ベイズなど"),
    ]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 0.0),
              ncol=3, fontsize=12, framealpha=0.95)
    ax.set_title("代表的な確率分布の関係図", fontsize=18)
    save(fig, "distribution_relations.png")


# ---------------------------------------------------------------------------
# 図2: 分布の形
# ---------------------------------------------------------------------------
def _stem(ax, ks, ps, label):
    ax.vlines(ks, 0, ps, color=COLOR_DISCRETE, lw=3, alpha=0.9)
    ax.plot(ks, ps, "o", color=COLOR_DISCRETE, ms=4, label=label)


def fig_shapes():
    fig, axes = plt.subplots(4, 3, figsize=(14, 13))
    axes = axes.ravel()

    # --- 離散 ---
    ax = axes[0]
    ks = np.arange(0, 21)
    for n, p, c in [(20, 0.2, "#f4a259"), (20, 0.5, "#bc4b51")]:
        ax.plot(ks, [binom_pmf(k, n, p) for k in ks], "o-", color=c, ms=3, label=f"$n={n},p={p}$")
    ax.set_title("二項分布 $B(n,p)$")

    ax = axes[1]
    ks = np.arange(0, 21)
    for lam, c in [(1, "#f4a259"), (4, "#bc4b51"), (10, "#6a4c93")]:
        ax.plot(ks, [poisson_pmf(k, lam) for k in ks], "o-", color=c, ms=3, label=fr"$\lambda={lam}$")
    ax.set_title(r"ポアソン分布 $Po(\lambda)$")

    ax = axes[2]
    ks = np.arange(0, 16)
    for p, c in [(0.5, "#f4a259"), (0.2, "#bc4b51")]:
        ax.plot(ks, [geom_pmf(k, p) for k in ks], "o-", color=c, ms=3, label=f"$p={p}$")
    ax.set_title("幾何分布 $Ge(p)$（失敗回数）")

    ax = axes[3]
    ks = np.arange(0, 31)
    for r, p, c in [(1, 0.3, "#f4a259"), (3, 0.3, "#bc4b51"), (8, 0.5, "#6a4c93")]:
        ax.plot(ks, [nbinom_pmf(k, r, p) for k in ks], "o-", color=c, ms=3, label=f"$r={r},p={p}$")
    ax.set_title("負の二項分布 $NB(r,p)$（失敗回数）")

    ax = axes[4]
    ks = np.arange(0, 11)
    for N, K, n, c in [(20, 8, 10, "#f4a259"), (100, 40, 10, "#bc4b51")]:
        ax.plot(ks, [hypergeom_pmf(k, N, K, n) for k in ks], "o-", color=c, ms=3,
                label=f"$N={N},K={K},n={n}$")
    ax.set_title("超幾何分布 $HG(N,K,n)$")

    # --- 連続 ---
    ax = axes[5]
    x = np.linspace(-5, 5, 400)
    for mu, s, c in [(0, 1, "#5b8e7d"), (0, 2, "#1f4e79"), (2, 0.7, "#bc4b51")]:
        ax.plot(x, normal_pdf(x, mu, s), color=c, lw=2, label=fr"$\mu={mu},\sigma={s}$")
    ax.set_title(r"正規分布 $N(\mu,\sigma^2)$")

    ax = axes[6]
    x = np.linspace(1e-3, 10, 400)
    for a, lam, c in [(1, 1, "#5b8e7d"), (2, 1, "#1f4e79"), (5, 1, "#bc4b51"), (5, 2, "#6a4c93")]:
        ax.plot(x, gamma_pdf(x, a, lam), color=c, lw=2, label=fr"$\alpha={a},\lambda={lam}$")
    ax.set_title(r"ガンマ分布 $Ga(\alpha,\lambda)$")

    ax = axes[7]
    x = np.linspace(0.01, 15, 400)
    for k, c in [(1, "#5b8e7d"), (2, "#1f4e79"), (4, "#bc4b51"), (8, "#6a4c93")]:
        ax.plot(x, chi2_pdf(x, k), color=c, lw=2, label=f"$k={k}$")
    ax.set_ylim(0, 0.6)
    ax.set_title(r"カイ二乗分布 $\chi^2(k)$")

    ax = axes[8]
    x = np.linspace(1e-3, 5, 400)
    for lam, c in [(0.5, "#5b8e7d"), (1, "#1f4e79"), (2, "#bc4b51")]:
        ax.plot(x, expon_pdf(x, lam), color=c, lw=2, label=fr"$\lambda={lam}$")
    ax.set_title(r"指数分布 $Exp(\lambda)$")

    ax = axes[9]
    x = np.linspace(0.005, 3, 400)
    for k, c in [(0.5, "#5b8e7d"), (1, "#1f4e79"), (2, "#bc4b51"), (5, "#6a4c93")]:
        ax.plot(x, weibull_pdf(x, k, 1.0), color=c, lw=2, label=fr"$k={k},\eta=1$")
    ax.set_ylim(0, 2.0)
    ax.set_title(r"ワイブル分布 $W(k,\eta)$")

    ax = axes[10]
    x = np.linspace(0.001, 0.999, 400)
    for a, b, c in [(1, 1, "#5b8e7d"), (2, 5, "#1f4e79"), (5, 2, "#bc4b51"), (0.5, 0.5, "#6a4c93")]:
        ax.plot(x, beta_pdf(x, a, b), color=c, lw=2, label=fr"$\alpha={a},\beta={b}$")
    ax.set_ylim(0, 3.0)
    ax.set_title(r"ベータ分布 $Be(\alpha,\beta)$")

    axes[11].axis("off")
    axes[11].text(0.05, 0.6, "オレンジ系：離散分布（確率関数）\n緑・青系：連続分布（確率密度関数）",
                  fontsize=12, va="center")

    for ax in axes[:11]:
        ax.legend(fontsize=8.5)
        ax.grid(alpha=0.3)
    fig.suptitle("代表的な確率分布の形", fontsize=16)
    fig.tight_layout()
    save(fig, "distribution_shapes.png")


# ---------------------------------------------------------------------------
# 図3: 極限（近似）関係
# ---------------------------------------------------------------------------
def fig_limits():
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.3))
    w = 0.38

    # 超幾何 → 二項
    ax = axes[0]
    n, p = 10, 0.4
    ks = np.arange(0, n + 1)
    ax.bar(ks - w / 2, [hypergeom_pmf(k, 25, 10, n) for k in ks], width=w,
           color="#cccccc", label="超幾何 $N=25,K=10$")
    ax.bar(ks + w / 2, [hypergeom_pmf(k, 1000, 400, n) for k in ks], width=w,
           color=COLOR_DISCRETE, label="超幾何 $N=1000,K=400$")
    ax.plot(ks, [binom_pmf(k, n, p) for k in ks], "o-", color=COLOR_LINE, label="二項 $B(10,0.4)$")
    ax.set_title("超幾何 → 二項（$N$ が大きいと復元抽出と同じ）")

    # 二項 → ポアソン
    ax = axes[1]
    lam = 3
    ks = np.arange(0, 13)
    ax.bar(ks - w / 2, [binom_pmf(k, 10, lam / 10) for k in ks], width=w,
           color="#cccccc", label="二項 $n=10,p=0.3$")
    ax.bar(ks + w / 2, [binom_pmf(k, 300, lam / 300) for k in ks], width=w,
           color=COLOR_DISCRETE, label="二項 $n=300,p=0.01$")
    ax.plot(ks, [poisson_pmf(k, lam) for k in ks], "o-", color=COLOR_LINE, label=r"ポアソン $\lambda=3$")
    ax.set_title(r"二項 → ポアソン（$n\to\infty,\ np=\lambda$）")

    # 二項 → 正規
    ax = axes[2]
    n, p = 100, 0.3
    ks = np.arange(10, 51)
    ax.bar(ks, [binom_pmf(k, n, p) for k in ks], width=0.8, color=COLOR_DISCRETE,
           label="二項 $B(100,0.3)$")
    x = np.linspace(10, 50, 400)
    ax.plot(x, normal_pdf(x, n * p, sqrt(n * p * (1 - p))), color=COLOR_CONTINUOUS, lw=2.5,
            label=r"正規 $N(30,\ 21)$")
    ax.set_title("二項 → 正規（$n$ が大きい）")

    for ax in axes:
        ax.legend(fontsize=9)
        ax.grid(alpha=0.3)
        ax.set_xlabel("$k$")
    axes[0].set_ylabel("確率")
    fig.tight_layout()
    save(fig, "distribution_limits.png")


if __name__ == "__main__":
    fig_relations()
    fig_shapes()
    fig_limits()
