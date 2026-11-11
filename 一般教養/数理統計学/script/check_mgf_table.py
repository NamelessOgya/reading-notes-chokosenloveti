"""代表的な確率分布の積率母関数（積率母関数の覚え方.md）の検算スクリプト。

各分布の積率母関数 M(t)=E[e^{tX}] を、定義（和・数値積分）から直接計算して、
ノートに載せた公式と一致するかを確認する。あわせて、対数をとった
K(t)=log M(t) の微分から平均・分散が出ること（K'(0)=平均、K''(0)=分散）も確かめる。

実行方法（リポジトリのルートから）:
    uv run --with numpy --with scipy python 一般教養/数理統計学/script/check_mgf_table.py
"""

import numpy as np
from scipy import integrate, special, stats


def mgf_discrete(dist, t, kmax=2000):
    k = np.arange(0, kmax)
    return float(np.sum(np.exp(t * k + dist.logpmf(k))))


def mgf_continuous(dist, t, lo, hi):
    val, _ = integrate.quad(lambda x: np.exp(t * x) * dist.pdf(x), lo, hi, limit=400)
    return val


def report(name, t, direct, formula):
    ok = "OK " if abs(direct - formula) < 1e-6 * max(1.0, abs(formula)) else "NG!"
    print(f"{ok} {name:<22} t={t:<5} 定義から={direct:.8f}  公式={formula:.8f}")


def check_all():
    n, p = 10, 0.3
    q = 1 - p
    lam = 2.0
    r = 3
    mu, sg = 1.5, 2.0
    al = 2.5
    k = 5
    a, b = 2.0, 3.0

    t = 0.4
    report("二項 B(10,0.3)", t, mgf_discrete(stats.binom(n, p), t, n + 1), (q + p * np.exp(t)) ** n)
    report("ポアソン Po(2)", t, mgf_discrete(stats.poisson(lam), t, 200), np.exp(lam * (np.exp(t) - 1)))
    t = 0.3  # t < -log q = 0.357
    report("幾何 Ge(0.3)", t, mgf_discrete(stats.nbinom(1, p), t, 4000), p / (1 - q * np.exp(t)))
    report("負の二項 NB(3,0.3)", t, mgf_discrete(stats.nbinom(r, p), t, 4000), (p / (1 - q * np.exp(t))) ** r)

    t = 0.4
    report("正規 N(1.5,4)", t, mgf_continuous(stats.norm(mu, sg), t, -60, 60), np.exp(mu * t + sg**2 * t**2 / 2))
    t = 0.7  # t < lam = 2
    report("指数 Exp(2)", t, mgf_continuous(stats.expon(scale=1 / lam), t, 0, 60), lam / (lam - t))
    report("ガンマ Ga(2.5,2)", t, mgf_continuous(stats.gamma(al, scale=1 / lam), t, 0, 80), (1 - t / lam) ** (-al))
    t = 0.2  # t < 1/2
    report("カイ二乗 χ²(5)", t, mgf_continuous(stats.chi2(k), t, 0, 200), (1 - 2 * t) ** (-k / 2))
    t = 1.3
    report("ベータ Be(2,3)", t, mgf_continuous(stats.beta(a, b), t, 0, 1), special.hyp1f1(a, a + b, t))


def check_cumulants():
    """K(t)=log M(t) の微分から平均・分散が出ることを数値微分で確認する。"""
    h = 1e-4
    cases = {
        "二項 B(10,0.3)": (lambda t: 10 * np.log(0.7 + 0.3 * np.exp(t)), 10 * 0.3, 10 * 0.3 * 0.7),
        "ポアソン Po(2)": (lambda t: 2 * (np.exp(t) - 1), 2.0, 2.0),
        "幾何 Ge(0.3)": (lambda t: np.log(0.3 / (1 - 0.7 * np.exp(t))), 0.7 / 0.3, 0.7 / 0.3**2),
        "正規 N(1.5,4)": (lambda t: 1.5 * t + 4 * t**2 / 2, 1.5, 4.0),
        "指数 Exp(2)": (lambda t: np.log(2 / (2 - t)), 0.5, 0.25),
        "ガンマ Ga(2.5,2)": (lambda t: -2.5 * np.log(1 - t / 2), 2.5 / 2, 2.5 / 4),
        "カイ二乗 χ²(5)": (lambda t: -2.5 * np.log(1 - 2 * t), 5.0, 10.0),
    }
    print()
    for name, (K, m, v) in cases.items():
        d1 = (K(h) - K(-h)) / (2 * h)
        d2 = (K(h) - 2 * K(0) + K(-h)) / h**2
        print(f"K'(0)={d1:.4f}（平均 {m:.4f}）  K''(0)={d2:.4f}（分散 {v:.4f}）  {name}")


def check_relations():
    print()
    t = 0.3
    # ポアソンは二項の極限：n log(1+p(e^t-1)) → λ(e^t-1)（p=λ/n）
    lam = 2.0
    for n in (10, 100, 10000):
        print(f"二項→ポアソン n={n:<6} (1+λ(e^t-1)/n)^n = {(1 + lam * (np.exp(t) - 1) / n) ** n:.6f}"
              f"  ポアソン {np.exp(lam * (np.exp(t) - 1)):.6f}")
    # 指数 = Ga(1,λ)、χ²(2) = Exp(1/2)
    print(f"Exp(2)=Ga(1,2): {2 / (2 - t):.6f} = {(1 - t / 2) ** (-1):.6f}")
    print(f"χ²(2)=Exp(1/2): {(1 - 2 * t) ** (-1):.6f} = {0.5 / (0.5 - t):.6f}")
    # 負の二項 r=1 は幾何
    q, p = 0.7, 0.3
    print(f"NB(1,p)=Ge(p): {(p / (1 - q * np.exp(t))) ** 1:.6f} = {p / (1 - q * np.exp(t)):.6f}")
    # M(0)=1
    print("M(0)=1 の確認:", (0.7 + 0.3) ** 10, np.exp(2 * 0), 0.3 / (1 - 0.7), (1 - 0) ** (-2.5))


if __name__ == "__main__":
    check_all()
    check_cumulants()
    check_relations()
