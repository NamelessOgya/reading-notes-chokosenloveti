# EvoX: Meta-Evolution for Automated Discovery

## 背景
近年、大規模言語モデル（LLM）を中心とした進化的アルゴリズム（Evolutionary Algorithm）は、プログラミング、アルゴリズム設計、システムパフォーマンス最適化などの幅広いタスクで科学的発見の推進力となっている（AlphaEvolve、OpenEvolveなど）。これらの既存システムでは、LLMが評価済みの候補解の集合（Population）から有望なものを抽出し、それを文脈としてプロンプトを構築し、新しい解（次世代の解）を生成する。
しかし、これまでのLLM進化的アルゴリズムの弱点として、「探索戦略そのもの（親解をどのように選択し、どのように変異させるか）」が、人間によってあらかじめハードコーディングされた固定のヒューリスティクス（たとえばMAP-Elitesや多様性を重視した固定パラメータ）に依存している点が挙げられる。このため、探索対象のタスクが異なる場合や、同一タスク内でも探索のフェーズ（序盤の探索、終盤の局所的改善）が変わることによって最適な戦略が変化する「非定常性」に対応できず、最適化が特定の局所解に早期に収束（停滞）してしまうという問題が存在していた。
本論文では、LLMによる進化的アルゴリズムをメタ学習（Meta-learning）の枠組みとして定式化し、「解を生成するための探索戦略自体も進化可能なオブジェクトとして扱う」フレームワークである「EvoX」を提案している。

## 手法
EvoXは、タスクそのものの最適解を探索する「Solution evolution loop」と、それを導くための探索戦略を最適化する「Meta-evolution loop」の2つの階層からなる適応的進化フレームワークである。

1. **Solution evolution under the current strategy（解の進化）**
   固定期間（Window）内において、現在の探索戦略 $S_t$ に従い、データベース $\mathcal{D}_t$ から親となる候補解 $x_{\mathrm{par}}$ と探索のヒントとなるインスピレーションセット $\mathcal{I}$ が抽出される。これに対し、LLM（$\mathcal{G}_{\mathrm{sol}}$）が指定された変異オペレーター $\pi$ に従って新しい解を生成する。
   $$
   x' \sim \mathcal{G}_{\mathrm{sol}}(\cdot \mid x_{\mathrm{par}}, \pi, \mathcal{I})
   $$

2. **Progress monitoring and strategy updates（進行状況の監視）**
   探索直近の $W$ ステップにおける評価スコアの変動（$\Delta$）を観測し、閾値 $\tau$ を下回った場合（進捗の停滞）に、新たな探索戦略へのアップデートをトリガーする。一定ウィンドウの評価結果 $J$ は以下のように計算される。
   $$
   J(S_t \mid \mathcal{D}_t) = \frac{ (s_{\mathrm{end}} - s_{\mathrm{start}}) \log(1 + s_{\mathrm{start}}) }{ \sqrt{W} }
   $$
   $\log(1+s_{\mathrm{start}})$ の項により、よりスコア水準が高い地点からの改善を高く評価するよう設計されている。

3. **Meta-evolving the search strategy（探索戦略のメタ進化）**
   アップデートがトリガーされると、EvoXはこれまでの探索戦略の履歴 $\mathcal{H}$（戦略とその時の指標 $\phi$、獲得した評価結果 $J$ の集まり）をもとに、戦略選択データベースの中で高い性能を発揮した戦略をLLM（$\mathcal{G}_{\mathrm{str}}$）に変異（Mutation）させ、現在のPopulationの状態（スコア分布、採用された親解の偏りなど）に適した新たな戦略 $S'$ を生成してデプロイする。
   $$
   S' \sim \mathcal{G}_{\mathrm{str}}(\cdot \mid S_{\mathrm{par}}, \phi(\mathcal{D}_t))
   $$
   これにより、システムはタスクの初期段階（広範な探索）と終盤（トップ解の局所的改善）で動的に探索バイアスを最適化することが可能となる。

## 結果

### 抽出図版および分析
論文中の図版（Fig 1, 2, 3等）とその考察を以下に示す。チェリーピッキングを行わずすべての図表を組み込んでいる。

#### Figure 1: EvoXのアーキテクチャと進化ダイナミクス
![Figure 1(a) System architecture](./images/architecturev0.png)
![Figure 1(b) Evolved search breakthroughs](./images/good_bad_two_in_one.png)
*図1(a)$はEvoXの解と戦略が相互作用する二重ループ構造を示し、図1(b)は多目的最適化（Signal Processing等）において、固定のMAP-Elites（赤線）が途中で停滞するのに対し、EvoX（青線）が探索戦略のスイッチングによって壁を突破し続けていることを示している。

#### Figure 2: アルゴリズム及び研究タスクにおけるベンチマーク性能
![Figure 2(a) ALE-Bench-Lite Average Performance](./images/evo2_updated_avg_performance.png)
![Figure 2(b) Frontier-CS Performance](./images/frontierCS-evoX.png)
*図2では10種のALE-Bench-Lite（NP困難なヒューリスティックタスク）および172種のFrontier-CS問題を対象とした結果を示している。固定予算内において、ShinkaEvolveやGEPAが早期に頭打ちになる中、EvoXは持続的にスコアを伸ばし、最良の中央値および平均値を獲得している。

#### Figure 3: 初期戦略の比較とコスト対品質のトレードオフ
![Figure 3(a) Effect of different initial search strategies](./images/all_algorithms_combined_higher_swapped.png)
![Figure 3(b) Cost-quality tradeoff](./images/cost_quality_plot.png)
*図3(a)はHeilbronn triangleタスクにおいて初期の固定戦略（Beam Search, Best-of-N等：点線）の限界に対して、それを種にEvoXで戦略進化を行った結果（実線）を示している。いずれの初期化戦略からもEvoXは固定戦略の限界を超えて改善する強力な復元力（ロバスト性）を証明した。また図3(b)は、同一目標スコア（0.031）に到達するまでのAI推論コストについて示しており、OpenEvolveが約15.4ドルかかるのに対し、EvoXは1ドル未満で到達できる圧倒的なコスト効率を示した。


### 完全な表の文字起こしと分析
Table 2, 3, 7 はソース上でコメントアウトまたは統合されているため、実体となるすべてのTableを省略なしに転記し考察を行う。

#### Table 1: EvoX across optimization tasks
| Task | Human Best | AlphaEvolve または AI Best | EvoX |
| :--- | :--- | :--- | :--- |
| **Mathematics** | | | |
| Circle-Packing ($\uparrow$) | 2.634 | 2.635 | **2.636** |
| MinMaxMinDist ($\downarrow$) | 4.16584 | 4.16579 | **4.16578** |
| **Systems Optimization** | | | |
| Cloud Transfer ($\downarrow$) | 626.24 | 645.72 | **623.69** |
| GPU Placement ($\uparrow$) | 21.89 | 26.26 | **30.52** |
| Txn Scheduling ($\uparrow$) | 2724.8 | 4329 | **4347.8** |
| **Algorithms** | | | |
| Frontier-CS ($\uparrow$) | -- | 56.2 | **75.5** |

**考察 (Table 1):** 数学、システム、アルゴリズムの全ての領域で、EvoXは既存のAI最適化ツール（AlphaEvolve等）や人間の専門家によるベストプラクティスを凌駕、もしくは匹敵する成果を挙げている。同一のLLM推論上限（100イテレーション）という制約のもとでSOTAとなるAI Bestをコンスタントに上回る点は強力である。

#### Table 4: Mathematical optimization benchmarks
| Problem | Objective | Description |
| :--- | :--- | :--- |
| Circle Packing (Square) | $\max r$ | Place $n$ equal-radius circles inside the unit square without overlap; maximize the common radius subject to non-overlap and boundary constraints. |
| Circle Packing (Rectangle) | $\max r$ | Pack $n$ equal-radius circles into a rectangle with fixed aspect ratio, maximizing the radius under geometric constraints. |
| Heilbronn Triangle | $\max \min$ area | Place $n$ points in $[0,1]^2$ to maximize the area of the smallest triangle formed by any three points. |
| Heilbronn Convex | $\max \min$ area | Generalization of the Heilbronn triangle problem: maximize the minimum area of convex hulls formed by any subset of $k>3$ points. |
| Min--Max--Min Distance (2 variants) | $\max \frac{d_{\min}}{d_{\max}}$ | Place points to maximize uniformity, measured by the ratio between minimum and maximum pairwise distances. |
| Third Autocorrelation Inequality | $\min C_3$ | Construct witness functions that minimize the third autocorrelation constant in additive combinatorics. |
| Signal Processing | multi-objective | Design a causal, online filtering program for noisy time series, balancing fidelity, smoothness, lag, and false trend detection. |

#### Table 5: System performance optimization benchmarks
| Problem | Objective | Description |
| :--- | :--- | :--- |
| EPLB (Expert Placement Load Balancing) | $\max$ throughput ratio | Place and replicate experts in MoE models across GPUs based on activation frequency, minimizing load imbalance and computational skew. |
| PRISM (Global Model Scheduling) | $\max$ throughput | Schedule multiple deep learning models across distributed GPUs under memory, compute, and latency SLO constraints in a multi-tenant setting. |
| LLM-SQL | $\max$ accuracy | Optimize LLM-driven SQL generation via prompting or post-processing; a query is correct only if it exactly matches ground-truth execution results. |
| Cloudcast (Multi-Region Data Transfer) | $\min$ cost | Design cost-efficient data transfer strategies across cloud regions with heterogeneous bandwidths, latencies, and egress pricing under deadline constraints. |
| Transaction Scheduling | $\max$ commits/sec | Schedule database transactions under contention to maximize throughput while minimizing aborts from conflicts, deadlocks, or timeouts. |
| Telemetry Repair | $\max$ reconstruction accuracy | Reconstruct missing or corrupted telemetry signals using partial observations, exploiting temporal and spatial correlations. |

#### Table 6: Algorithmic and research problem benchmarks
| Problem / Category | Count | Description |
| :--- | :--- | :--- |
| **ALE-Bench-Lite: NP-hard optimization from AtCoder Heuristic Contests** | | |
| `ahc008` (Territory) | 1 | Control agents on a grid to place fences isolating pets; $\max$ satisfaction. |
| `ahc011` (Sliding Puzzle) | 1 | Rearrange tiles so line patterns form a large connected tree; $\max$ connectivity. |
| `ahc015` (Candy Clustering) | 1 | Cluster candies of the same flavor using global tilt operations; $\max$ clustering score. |
| `ahc016` (Graph Classification) | 1 | Design reference graphs and classify noisy, permuted query graphs; $\min$ classification error. |
| `ahc024` (Map Compression) | 1 | Compress a grid map preserving district adjacency; $\min$ map size. |
| `ahc025` (Weight Balancing) | 1 | Partition items with unknown weights into balanced groups; $\min$ imbalance. |
| `ahc026` (Box Stacking) | 1 | Rearrange numbered boxes across stacks to a target configuration; $\min$ moves. |
| `ahc027` (Cleaning Route) | 1 | Design a cyclic robot route to minimize steady-state dirt; $\min$ average dirtiness. |
| `ahc039` (Fishing Net) | 1 | Construct a rectilinear polygon enclosing targets under a perimeter budget; $\max$ net score. |
| `ahc046` (Skating with Blocks) | 1 | Visit target squares in order using moves, slides, and blocks; $\min$ actions. |
| **FrontierCS: open-ended CS problems** | | |
| `Optimization` | 38 | Maximize or minimize a quantitative objective over a parameterized search space under resource constraints. (IDs: 1, 2, ... 229) |
| `Constructive` | 62 | Synthesize a valid structured object (e.g., packing, graph, expression) under global constraints. (IDs: 0, 3, ... 241) |
| `Interactive` | 72 | Solve a hidden-instance task via an adaptive query-response protocol, minimizing queries or interaction steps. (IDs: 10, 11, ... 258) |

#### Table 8: EvoX performance on ARC-AGI benchmarks.
| Backbone | OpenEvolve | EvoX |
| :--- | :--- | :--- |
| GPT-5 | 41% | 48% |
| Gemini-3-Pro | 45% | 51% |

**考察 (Table 4, 5, 6, 8に対する全体的分析):**
各表で示される約200に上る多岐にわたるベンチマークにおいて、EvoXの適応的メタ進化が普遍的に機能していることがわかる。数学的な最悪値や最小化・最大化タスクから、GPUスケジューリングのような大規模システムの配置問題、さらにはARC-AGIのような純粋な論理一般化問題（GPT-5バックボーンにおいてOpenEvolveを上回る48%、Gemini-3-Proでは51%を記録）に至るまで、同一のパラダイムで改善ができている。これはEvoXが「固定の探索戦略」に依存する既存の進化的アプローチ（OpenEvolve, GEPA等）よりも、環境に対して動的にヒューリスティクスを書き換える「戦略自体の進化」を利用していることに起因している。局所解に陥ることなく段階を押し上げるブレークスルーを生む設計であることが証明された。
