"""n次元の変数変換（n次元の変数変換とヤコビアン.md）用の図を作成するスクリプト。

1. 3次元：1次変換で単位立方体が |det A| 倍の体積の平行六面体になる図／r^{n-1} の図
2. 3変数ガンマ → ディリクレ分布（S ~ Ga(9)、U1 ~ Be(2,7)、S と U は独立）のシミュレーション
3. 数値確認：球座標のヤコビアン r^2 sin(phi)、n次元極座標（R^2 ~ chi2(n)）、累積和（J=1）

実行方法（リポジトリのルートから）:
    uv run --with matplotlib --with numpy --with scipy python 一般教養/数理統計学/script/plot_jacobian_nd.py

出力先: 一般教養/数理統計学/images/
"""

from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
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


def box_faces(vecs):
    """原点から vecs（3本のベクトル）が作る平行六面体の6面を返す。"""
    a, b, c = vecs
    o = np.zeros(3)
    return [
        [o, a, a + b, b], [c, a + c, a + b + c, b + c],
        [o, a, a + c, c], [b, a + b, a + b + c, b + c],
        [o, b, b + c, c], [a, a + b, a + b + c, a + c],
    ]


def fig_volume():
    fig = plt.figure(figsize=(12.5, 5.2))
    A = np.array([[2.0, 0.5, 0.0], [0.5, 1.5, 0.3], [0.0, 0.4, 1.2]])
    d = np.linalg.det(A)

    ax = fig.add_subplot(1, 2, 1, projection="3d")
    cube = list(np.eye(3))
    ax.add_collection3d(Poly3DCollection(box_faces(cube), facecolor=BLUE, edgecolor=BLUE, alpha=0.35))
    para = [A[:, j] for j in range(3)]
    ax.add_collection3d(Poly3DCollection(box_faces(para), facecolor=RED, edgecolor=RED, alpha=0.2))
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_zlim(0, 2)
    ax.set_box_aspect((3, 3, 2))
    ax.view_init(elev=22, azim=-60)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$x_3$")
    ax.set_title(f"1次変換 $\\vec{{y}}=A\\vec{{x}}$：単位立方体（青、体積1）\n"
                 f"→ 平行六面体（赤、体積 $|\\det A|={abs(d):.2f}$）")

    ax = fig.add_subplot(1, 2, 2)
    r = np.linspace(0, 3, 300)
    cols = [BLUE, GREEN, PURPLE, RED]
    for n, col in zip(range(1, 5), cols):
        ax.plot(r, r ** (n - 1), color=col, lw=2.2, label=rf"$n={n}$：$r^{{{n - 1}}}$")
    ax.set_ylim(0, 9.5)
    ax.set_xlabel("$r$")
    ax.set_ylabel(r"$r^{n-1}$（$n$ 次元極座標のヤコビアン）")
    ax.set_title("次元が上がるほど、外側ほど体積が急に増える")
    ax.legend(loc="upper left", fontsize=10)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "jacobian_nd_volume.png", bbox_inches="tight")
    plt.close(fig)
    print(f"det A = {d:.4f}  平行六面体の体積(三重積) = "
          f"{abs(np.dot(A[:, 0], np.cross(A[:, 1], A[:, 2]))):.4f}")


def fig_dirichlet():
    rng = np.random.default_rng(0)
    n = 300_000
    al = (2.0, 3.0, 4.0)
    x = np.column_stack([rng.gamma(a, 1.0, n) for a in al])
    s = x.sum(axis=1)
    u = x / s[:, None]

    fig, axes = plt.subplots(1, 4, figsize=(17, 4.4))

    ax = axes[0]
    ax.hist(s, bins=80, density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    g = np.linspace(0.01, 25, 400)
    ax.plot(g, stats.gamma.pdf(g, 9), color=BLUE, lw=2.2, label=r"$Ga(9,1)$")
    ax.set_title(r"$S=X_1+X_2+X_3$ の分布")
    ax.set_xlabel("$s$")
    ax.legend(fontsize=9.5)

    ax = axes[1]
    ax.hist(u[:, 0], bins=80, density=True, color=GREEN, alpha=0.5, label="シミュレーション")
    b = np.linspace(0.001, 0.999, 400)
    ax.plot(b, stats.beta.pdf(b, 2, 7), color=RED, lw=2.2, label=r"$Be(2,7)$")
    ax.set_title(r"$U_1=X_1/S$ の分布（周辺分布）")
    ax.set_xlabel("$u_1$")
    ax.legend(fontsize=9.5)

    ax = axes[2]
    idx = rng.choice(n, 3000, replace=False)
    ax.scatter(s[idx], u[idx, 0], s=5, color=PURPLE, alpha=0.5)
    c = np.corrcoef(s, u[:, 0])[0, 1]
    ax.set_title(rf"$(S,U_1)$ の散布図：相関 $r={c:.3f}$（独立）")
    ax.set_xlabel("$s$")
    ax.set_ylabel("$u_1$")

    ax = axes[3]
    # 正三角形座標：頂点 (1,0,0),(0,1,0),(0,0,1)
    P = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2]])
    pts = u[idx] @ P
    ax.scatter(pts[:, 0], pts[:, 1], s=5, color=BLUE, alpha=0.35)
    tri = np.vstack([P, P[0]])
    ax.plot(tri[:, 0], tri[:, 1], color="black", lw=1.2)
    off = 0.05
    ax.text(P[0, 0] - off, P[0, 1] - off, "$u_1=1$", ha="right", va="top", fontsize=10)
    ax.text(P[1, 0] + off, P[1, 1] - off, "$u_2=1$", ha="left", va="top", fontsize=10)
    ax.text(P[2, 0], P[2, 1] + off, "$u_3=1$", ha="center", va="bottom", fontsize=10)
    ax.set_xlim(-0.35, 1.35)
    ax.set_ylim(-0.2, 1.05)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(r"$(U_1,U_2,U_3)$：和が1の三角形の上に分布" "\n" r"$Dir(2,3,4)$")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "jacobian_nd_dirichlet.png", bbox_inches="tight")
    plt.close(fig)

    print(f"S: 平均 {s.mean():.3f}（9） 分散 {s.var():.3f}（9）")
    print(f"U 平均 {u.mean(axis=0).round(4)}（{[round(a / 9, 4) for a in al]}）")
    print(f"U1 分散 {u[:, 0].var():.5f}（Be(2,7)={2 * 7 / (81 * 10):.5f}）  corr(S,U1)={c:.4f}")


def numeric_checks():
    # 球座標のヤコビアン（有限差分）
    def sph(p):
        r, ph, th = p
        return np.array([r * np.sin(ph) * np.cos(th), r * np.sin(ph) * np.sin(th), r * np.cos(ph)])

    p0 = np.array([1.7, 0.9, 2.3])
    h = 1e-6
    J = np.column_stack([(sph(p0 + h * e) - sph(p0 - h * e)) / (2 * h) for e in np.eye(3)])
    print(f"球座標 det J = {np.linalg.det(J):.5f}  r^2 sin(phi) = {p0[0] ** 2 * np.sin(p0[1]):.5f}")

    # 3次元ガウス積分 = (2π)^{3/2}：r^2 sin(phi) を使った計算
    val = 4 * np.pi * np.sqrt(np.pi / 2) * 1.0  # ∫_0^∞ r^2 e^{-r^2/2} dr = sqrt(π/2)
    print(f"3次元ガウス積分 = {val:.5f}  (2π)^(3/2) = {(2 * np.pi) ** 1.5:.5f}")

    # n次元極座標：R^2 ~ chi2(n)
    rng = np.random.default_rng(1)
    for dim in (3, 5):
        z = rng.standard_normal((400_000, dim))
        r2 = (z ** 2).sum(axis=1)
        print(f"n={dim}: R^2 平均 {r2.mean():.3f}（{dim}） 分散 {r2.var():.3f}（{2 * dim}）  "
              f"KS(R^2, chi2({dim})) p={stats.kstest(r2[:20000], 'chi2', args=(dim,)).pvalue:.3f}")

    # 累積和：Y_k = X_1+...+X_k（X_i ~ Exp(1)）、J = 1
    n = 4
    x = rng.exponential(1.0, (400_000, n))
    y = x.cumsum(axis=1)
    print(f"累積和: Y_4 平均 {y[:, 3].mean():.3f}（4） 分散 {y[:, 3].var():.3f}（4）  "
          f"KS(Y_4, Ga(4)) p={stats.kstest(y[:20000, 3], 'gamma', args=(4,)).pvalue:.3f}")
    # 順序統計量との対応：Y_1,Y_2,Y_3 は Y_4 で割ると U(0,1) の順序統計量
    w = y[:, :3] / y[:, 3:4]
    print(f"Y_k/Y_4 の平均 {w.mean(axis=0).round(4)}（U(0,1)の順序統計量: 0.25, 0.5, 0.75）")


if __name__ == "__main__":
    fig_volume()
    fig_dirichlet()
    numeric_checks()
    print("saved to", OUT_DIR)
