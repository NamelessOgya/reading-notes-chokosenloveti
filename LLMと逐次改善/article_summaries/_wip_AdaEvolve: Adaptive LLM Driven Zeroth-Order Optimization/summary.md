# AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization

## 背景
大規模言語モデル（LLM）は推論時の計算量（Test-Time Compute）をスケーリングすることで、プログラム生成やアルゴリズム探索といった問題に対して強力な性能を発揮することがわかっています。この枠組みとして、LLMを突然変異オペレータとして組み込んだ進化的アルゴリズム（OpenEvolve, AlphaEvolve等）が主流になりつつあります。
しかし、従来の手法は、静的なスケジュール（固定のサンプリング温度やプロンプトテンプレート、全探索空間に対する均等な計算資源の割り当て）に基づいて進行するため、探索の非定常的な動態を捉えることができません。これにより、有望な探索フロンティアがあるにもかかわらず、既に局所解に陥って停滞している母集団（島）に計算資源が浪費されてしまうという「計算の無駄遣い」と、設定されたハイパーパラメータへの強い依存性（タスク毎のチューニングが必要になる脆さ）が課題となっていました。

## 手法
著者らは、この問題を解決するためにLLMベースの進化計算を「階層的な適応型最適化問題」と再定義するフレームワーク「**AdaEvolve**」を提案しました。
本手法は、連続最適化におけるAdamやAdaGradのような適応的勾配法から着想を得ており、勾配の代わりに「適応スコア（過去の改善の大きさの軌跡）」の移動平均である**累積改善シグナル（Accumulated Improvement Signal）** $G_{t}^{(k)}$ を用いて、3つのレベルで動的に探索を制御します。

累積改善シグナル $G_{t}^{(k)}$ は、各島 $k$ におけるスコアの正規化された改善度合い $\delta_{t}^{(k)} = \max\left(\frac{f' - f_{k}^*}{f_{k}^*}, 0\right)$ から以下のように更新されます：
$$
G_{t}^{(k)} = \rho \cdot G_{t-1}^{(k)} + (1 - \rho) \cdot (\delta_{t}^{(k)})^2
$$
このシグナルに基づき、AdaEvolveは以下の3つの適応レベルを実行します。

1. **Level 1: Local Adaptation (島内の探索強度の制御)**
   島内の探索（Exploration）と活用（Exploitation）のバランスを動的に調整します。累積改善シグナルを用いて探索強度 $I_{t}^{(k)}$ を計算し、停滞時には探索率を上げ（ランダムな親選択と多様なプロンプトの利用）、改善が進んでいる時は活用（良い親の改良）を進めます。
   $$
   I_{t}^{(k)} = I_{\min} + \frac{I_{\max} - I_{\min}}{1 + \sqrt{G_{t}^{(k)} + \epsilon}}
   $$

2. **Level 2: Global Adaptation (島間の計算資源割り当て)**
   島（サブの母集団）ごとの予算割り当てを、UCBを用いたMulti-Armed Bandit問題として解きます。この際、低いベースラインから小さな改善を繰り返す「貧弱な島のバイアス（Poor Island Bias）」を避けるため、各島の報酬を島のローカルな最高スコアではなく、**グローバル最高スコア（全体トップ）** $f_{\text{global}}^*$ を用いて正規化します。
   $$
   r_{t}^{(k)} = \frac{f' - f_{k}^*}{f_{\text{global}}^*}
   $$
   さらに、島間の報酬の減衰統計量（$R_{t}^{(k)}, V_{t}^{(k)}$）を計算することで、過去に幸運な改善を引いただけで現在停滞している島に資源が奪われるのを防いでいます。

3. **Level 3: Meta-Guidance (戦略的アプローチの生成)**
   上記2つのレベルの数値的な適応だけでは進展しない（概念的な局所解に陥った）場合、メタガイドを生成します。各島の累積改善シグナルが閾値を下回った時点で「System 2」的な介入として別のLLMを呼び出し、現在の行き詰まりを分析させ、「貪欲法から動的計画法に切り替える」といった上位レベルの解法パラダイム（Solution Tactics）を提案・注入することで、根本的なアプローチの転換を図ります。

## 結果
AdaEvolveは、組み合わせ最適化、システム最適化、アルゴリズム設計などの185のオープンエンドな最適化問題に対して、**タスク固有のハイパーパラメータ調整を一切行わずに**（モデル名と反復回数の指定のみで）汎用的に適用され、各評価においてベースラインを上回りました。

![AdaEvolve overview](./images/adaevolve_fig1_final.png)
*Figure 1: AdaEvolveの概要。静的なポリシースケジューリングを用いる従来のLLM進化ベース手法に対し、AdaEvolveは階層的適応として「島内の探索強度」「計算リソースの再配置」「メタ介入」を展開し停滞を打破する。*

![scaling_curves_paper_v2_arxiv](./images/scaling_curves_paper_v2_arxiv.png)
*Figure: スケーリングカーブの性能推移。*

### システムおよびデータベンチマークの結果
Table 1は、Telemetry等のシステム最適化ベンチマークにおける結果です。GTP-5およびGemini-3-Proをバックボーンとした比較において、AdaEvolveはHuman SOTAをも超える最高性能（Cloudcastのコスト低減やNS3のスループット向上など）を安定して叩き出していることがわかります。

| Strategy | Telemetry (Avg) | Telemetry (Best) | Cloudcast $\downarrow$ (Avg) | Cloudcast $\downarrow$ (Best) | EPLB (Avg) | EPLB (Best) | Prism (Avg) | Prism (Best) | LLM-SQL (Avg) | LLM-SQL (Best) | TXN (Avg) | TXN (Best) | NS3 (Avg) | NS3 (Best) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Human / SOTA** | -- | 0.822 | -- | 626.2 | -- | 0.1265 | -- | 21.89 | -- | 0.692 | -- | 2,725 | -- | 69.0 |
| *Backbone: GPT-5* | | | | | | | | | | | | | | |
| OE | .930 $\pm$ .04 | .952 | 926.9 $\pm$ 171 | 729.8 | .127 $\pm$ .00 | .1272 | 26.23 $\pm$ .00 | 26.23 | .710 $\pm$ .01 | .716 | 4,239 $\pm$ 90 | 4,329 | 92.2 $\pm$ 4.8 | 97.3 |
| GEPA | .916 $\pm$ .05 | .948 | 689.9 $\pm$ 74 | 645.7 | .134 $\pm$ .01 | .1445 | 26.19 $\pm$ .07 | 26.23 | .713 $\pm$ .00 | .713 | 3,753 $\pm$ 204 | 3,984 | 68.9 $\pm$ .00 | 101.8 |
| Shinka | .923 $\pm$ .04 | .952 | 954.8 $\pm$ 125 | 812.7 | .118 $\pm$ .01 | .1272 | 26.26 $\pm$ .00 | 26.26 | .712 $\pm$ .00 | .713 | 4,090 $\pm$ 338 | 4,329 | 89.5 $\pm$ 18.7 | 106.1 |
| **AdaEvolve** | **.952 $\pm$ .00** | **.952** | **662.3 $\pm$ 0.1** | **640.5** | **.134 $\pm$ .01** | **.1453** | **26.30 $\pm$ .07** | **26.37** | **.746 $\pm$ .03** | **.775** | **4,317 $\pm$ 29** | **4,348** | **125.2 $\pm$ 6.1** | **131.8** |
| *Backbone: Gemini-3-Pro* | | | | | | | | | | | | | | |
| OE | **.954 $\pm$ .01** | **.960** | 707.8 $\pm$ 40 | 667.1 | .127 $\pm$ .00 | .1272 | 26.24 $\pm$ .01 | 26.24 | .729 $\pm$ .01 | .736 | 4,109 $\pm$ 254 | 4,274 | 115.2 $\pm$ 13.2 | 125.6 |
| GEPA | .850 $\pm$ .00 | .855 | 720.4 $\pm$ 46 | 667.1 | .127 $\pm$ .00 | .1272 | 26.16 $\pm$ .03 | 26.19 | .713 $\pm$ .00 | .713 | 3,616 $\pm$ 481 | 4,167 | 74.5 $\pm$ 9.5 | 104.0 |
| Shinka | .918 $\pm$ .03 | .933 | 949.8 $\pm$ 73 | 892.3 | .120 $\pm$ .01 | .1272 | 26.25 $\pm$ .01 | 26.26 | .721 $\pm$ .00 | .721 | 3,932 $\pm$ 343 | 4,255 | 84.7 $\pm$ 7.7 | 92.2 |
| **AdaEvolve** | .953 $\pm$ .01 | **.960** | **642.1 $\pm$ 5.9** | **637.1** | **.145 $\pm$ .00** | **.1453** | **26.26 $\pm$ .00** | **26.26** | **.743 $\pm$ .01** | **.752** | **4,221 $\pm$ 89** | **4,310** | **126.0 $\pm$ 5.1** | **131.8** |

### 数学的最適化ベンチマークにおける結果
Table 2はFunSearchやAlphaEvolveなどで扱われた数学的パズル（Circle Packingの充填問題やHeilbronn問題など）での評価結果です。AdaEvolveはAlphaEvolveのスコアをさらに超え、探索空間の大きい難しい問題でも局所解を脱出して最適な配置を発見できていることが示されています。

| Strategy | Circle Packing (Square) Avg | Circle Packing (Square) Best | Circle Packing (Rect) Avg | Circle Packing (Rect) Best | Heilbronn (Triangles) Avg | Heilbronn (Triangles) Best | Heilbronn (Convex) Avg | Heilbronn (Convex) Best | MinMax Distance Avg | MinMax Distance Best | Signal Processing Avg | Signal Processing Best |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Human** | -- | 2.634 | -- | 2.364 | -- | 0.0360 | -- | 0.0306 | -- | 0.2399 | -- | -- |
| **AlphaEvolve** | -- | 2.635 | -- | 2.3658 | -- | 0.0365 | -- | 0.0309 | -- | 0.2398 | -- | -- |
| *Backbone: GPT-5*|  |  |  |  |  |  |  |  |  |  |  |  |
| OpenEvolve | 2.531 $\pm$ .018 | 2.541 | 2.267 $\pm$ .014 | 2.276 | 0.028 $\pm$ .006 | 0.028 | 0.025 $\pm$ .005 | 0.027 | 0.226 $\pm$ .003 | 0.2243 | 0.569 $\pm$ .047 | 0.622 |
| GEPA | 2.613 $\pm$ .022 | 2.628 | 2.326 $\pm$ .023 | 2.354 | 0.031 $\pm$ .002 | 0.032 | 0.025 $\pm$ .002 | 0.027 | 0.232 $\pm$ .120 | 0.2392 | 0.689 $\pm$ .014 | 0.705 |
| ShinkaEvolve | 2.464 $\pm$ .083 | 2.541 | 2.335 $\pm$ .026 | 2.358 | 0.032 $\pm$ .012 | 0.034 | 0.023 $\pm$ .005 | 0.026 | 0.239 $\pm$ .001 | **0.2398** | 0.485 $\pm$ .044 | 0.533 |
| **AdaEvolve** | **2.629 $\pm$ .001** | **2.636** | **2.349 $\pm$ .010** | **2.361** | **0.033 $\pm$ .001** | **0.036** | **0.027 $\pm$ .001** | **0.029** | **0.239 $\pm$ .009** | **0.2404** | **0.698 $\pm$ .017** | **0.718** |
| *Backbone: Gemini-3-Pro*| | | | | | | | | | | | |
| OpenEvolve | 2.541 $\pm$ .000 | 2.541 | 2.365 $\pm$ .001 | 2.366 | 0.033 $\pm$ .000 | 0.035 | 0.028 $\pm$ .009 | 0.028 | 0.240 $\pm$ .000 | 0.2398 | 0.553 $\pm$ .015 | 0.565 |
| GEPA | 2.620 $\pm$ .002 | 2.621 | 2.216 $\pm$ .046 | 2.232 | 0.031 $\pm$ .002 | 0.033 | 0.023 $\pm$ .001 | 0.027 | 0.213 $\pm$ .008 | 0.2178 | **0.617 $\pm$ .075** | **0.680** |
| ShinkaEvolve | 2.622 $\pm$ .012 | 2.636 | 2.366 $\pm$ .000 | 2.366 | 0.035 $\pm$ .001 | 0.036 | 0.028 $\pm$ .001 | **0.029** | **0.240 $\pm$ .000** | 0.2398 | 0.480 $\pm$ .039 | 0.505 |
| **AdaEvolve** | **2.632 $\pm$ .003** | **2.636** | **2.366 $\pm$ .000** | **2.366** | **0.036 $\pm$ .001** | **0.036** | **0.029 $\pm$ .000** | **0.029** | **0.240 $\pm$ .000** | **0.2404** | 0.593 $\pm$ .009 | 0.603 |

### メタ介入によるタクティクス生成の効果（考察）
Table 3ではメタ・ガイダンス層によって生成され投入される「解決の戦略指針（Tactics）」の具体例が示されています。AdaEvolveは、プログラムが数学系ならトラスト領域探索への変更や、組合せ系なら貪欲法から交換近傍探索（local search）へのアルゴリズムパラダイムの移行など、人間のように上位レベルでのアプローチ転換を行うことで、単純なコード変異を超えた進化を実現しています。

| Use case | Meta-Guidance Solution Tactics | Approach type |
| :--- | :--- | :--- |
| *Math / equation systems* | Solve nonlinear systems using a trust-region root finder | `scipy.optimize.root` |
| | Exploit structure by directly solving linear systems | `scipy.linalg.solve` |
| | Isolate scalar roots with bracketed search | `scipy.optimize.brentq` |
| | Iterate toward equilibrium with damped fixed-point updates | Fixed-point iteration |
| | Generate symbolic expressions before numerical evaluation | `sympy.lambdify` + solver |
| *Continuous optimization* | Perform constrained minimization under geometric constraints | `scipy.optimize.minimize` (SLSQP) |
| | Escape poor basins via multi-start global search | Multi-start + local refine |
| | Initialize layouts using Voronoi structure, then refine locally | Voronoi + optimizer |
| | Enforce feasibility through convex-hull constraints | `scipy.spatial.ConvexHull` |
| | Optimize box-constrained parameters with quasi-Newton updates | L-BFGS-B |
| *Combinatorial / assignment* | Construct solutions greedily using score-ordered candidates | Greedy heuristic |
| | Compute minimum-cost matchings exactly | Linear sum assignment |
| | Improve configurations through swap-based neighborhoods | Local search |
| | Relax discrete constraints into a linear program | `scipy.optimize.linprog` |
| | Prioritize decisions with a score-driven heap | Priority-queue greedy |
| *Signal / filtering* | Suppress impulsive noise with median filtering | `scipy.signal.medfilt` |
| | Preserve trends via polynomial smoothing | Savitzky--Golay filter |
| | Balance noise and fidelity with adaptive Wiener filtering | Wiener filter |
| | Aggregate robust statistics over sliding windows | Percentile filter |
| | Apply learned structure through custom convolution kernels | `scipy.ndimage.convolve` |

### ADRS および AlphaEvolve問題セットの詳細 (Table 4, 5, 6)
Table 4とTable 5 はそれぞれ評価で用いられたシステムの詳細目的と、AlphaEvolve由来の数学的問題の定義仕様に関する説明です。また Table 6 では、さらにARC-AGI-2ベンチマークにてGPT-5とGemini-3-Proでの精度がOpenEvolve対比で6-7%向上していることが示され、AdaEvolveの改善メカニズムがAGIタスクにおいても普遍的な効果を持つことが示されました。

Table 4: **ADRS systems benchmarks**
| Task | Objective | Problem description |
| :--- | :--- | :--- |
| **Telemetry Repair** | Repair buggy network telemetry pipelines | Automatically fix data processing logic to improve correctness and confidence calibration. |
| **Cloudcast** | Optimize multi-cloud data transfer cost | Select routing and placement strategies to minimize monetary transfer cost across providers. |
| **Expert Parallelism Load Balancer (EPLB)** | Balance expert-parallel load across GPUs | Reduce stragglers by redistributing expert assignments while preserving throughput. |
| **Model Placement (Prism)** | Optimize model-to-GPU placement cost | Assign model components to GPUs to minimize global execution cost under capacity constraints. |
| **LLM-SQL** | Reorder tabular data for prefix efficiency | Improve prefix-cache hit rates by reordering rows or columns without altering semantics. |
| **Transaction Scheduling (TXN)** | Minimize makespan in transaction execution | Schedule dependent transactions to reduce overall completion time. |
| **Datacenter TCP Congestion Control (NS3)** | Maximize throughput and minimize queue latency | Tune congestion control behavior under realistic network simulation workloads. |

Table 5: **Mathematical optimization benchmarks used in AdaEvolve**
| Problem | Objective (exact task definition) |
| :--- | :--- |
| **Circle Packing (Square)** $N=26$ | Pack $N$ disjoint circles inside a *unit square* so as to **maximize the sum of their radii**. |
| **Circle Packing (Rectangle)** $N=21$ | Pack $N$ disjoint circles inside a *rectangle of perimeter 4* so as to **maximize the sum of their radii**. |
| **Heilbronn Problem (Triangle)** $N=11$ | Place $N$ points on or inside a *triangle of unit area* so that the **minimum area of any triangle formed by the points is maximized**. |
| **Heilbronn Problem (Convex Region)** $N=13$ | Place $N$ points on or inside a *convex region of unit area* so that the **minimum area of any triangle formed by the points is maximized**. |
| **MinMax Distance** $N=3$ | For given $N$ and dimension $d$, find $N$ points in $\mathbb{R}^d$ that **maximize the ratio between the minimum and maximum pairwise distances**. |
| **Signal Processing** | Optimize a continuous signal processing objective under noisy evaluation, where candidate programs transform an input signal and are scored by an external evaluator. |

Table 6: **AdaEvolve performance on ARC-AGI-2 benchmarks**
| Backbone | OpenEvolve | AdaEvolve |
| :--- | :--- | :--- |
| GPT-5 | 42% | 49% |
| Gemini-3-Pro | 44% | 50% |

総じて、AdaEvolveは過去の改善量から算出される単一の「累積改善シグナル」が全てを動的に統率することで、従来のヒューリスティクス（停滞したら再起動、予算の均等割り振り）を一新し、大規模LLMのスケーリング則にふさわしい自律的なゼロ次最適化環境を提供しています。
