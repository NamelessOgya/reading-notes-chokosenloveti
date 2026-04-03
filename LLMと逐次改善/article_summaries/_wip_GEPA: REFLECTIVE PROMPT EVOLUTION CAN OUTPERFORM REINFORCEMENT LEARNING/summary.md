# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

## 背景
近年、大規模言語モデル（LLM）の推論能力を向上させるために、強化学習（RL）などの手法が盛んに研究されている。特にGRPO（Group Relative Policy Optimization）のような強化学習ベースのテスト時計算アプローチが注目を浴びている。
しかし、RLを用いた方策最適化は、膨大な数のロールアウトからの学習（サンプル効率の悪さ）や、スカラー報酬というスパースな信号に依存していることによる学習の難しさといった課題がある。
本論文では、モデルの重みを更新する代わりに自然言語のプロンプトを「進化的アルゴリズム」を用いて継続的に改善し、LLM自身の「リフレクション（振り返り、内省）」を活用する手法「GEPA（Genetic-Pareto）」を提案し、離散的なプロンプト最適化がRL手法を凌駕できるかどうかの検証を行った。

## 手法
提案されている「GEPA（Genetic-Pareto）」は、Genetic Algorithm（遺伝的アルゴリズム）とPareto-based（パレートベース）の候補選択を組み合わせたテスト時プロンプトオプティマイザである。
具体的には以下のステップで構成される：

1. **初期プロンプトと候補プール生成（Initialization & Pool）**
初期プロンプトをシステムに与え、複数の候補を管理するプールを作成する。

2. **ロールアウトとフィードバック収集（Rollout & Feedback）**
対象のタスク環境上で、バッチごとのロールアウト（推論軌跡）を生成する。この際、可能な場合は各コンポーネントごとの詳細な言語ベースのフィードバック関数 $\mu_f$ を利用してエラー原因を特定する。

3. **リフレクティブなプロンプト変異（Reflective Prompt Mutation）**
収集した軌跡とフィードバックを元に、LLM自身に「どこが間違っていたか」を自然言語でリフレクション（内省）させ、それに対する解決策となるような新しい命令（プロンプト）を生成・提案させる。
変異操作として、過去のプロンプトを修正するだけでなく、パレートフロント上の優れた複数のプロンプトたちの長所を自然言語レベルで統合する「Merge（交叉）」といった遺伝的アルゴリズムのアプローチを用いる。

4. **パレートベースの候補選択（Pareto-based Candidate Selection）**
新たに生成したプロンプトを評価し、良くなった候補を残す。この際、単一の最高スコア候補（Greedy）からのみ変異を繰り返すと局所最適解に陥るため、GEPAではパレートベース（多様性を確保しつつ優秀な親を複数残す）でツリー探索を行い、より高性能なプロンプトへと進化させる。

![GEPAのメインアルゴリズム解説図](./images/FullGepa.png)
*(Figure: GEPA's core algorithm for reflective prompt evolution)*

![GEPAによるプロンプト反復改善の可視化](./images/iterative_refinement_visualization.png)
*(Figure: Iterative refinement visualization)*

## 結果
GEPAの性能を検証するため、Qwen3-8BおよびGPT-4.1-Mini上で複数タスク（HotpotQA、IFBench、HoverBench、PUPA、AIME-2025、LiveBench-Math、FSABenchなど）を用いて評価を行った。

### 1. サンプル効率と強化学習（GRPO）との比較
GEPAは強化学習モデル（GRPO等）と比較して、はるかに少ないロールアウト（サンプル数）で同等以上の性能を達成した。

![ロールアウト数とスコアの比較（HotpotQA）](./images/HotpotQABench_qwen3-8b_True_rollout_vs_score.png)
*(Figure: Rollout vs validation performance for HotpotQA with Qwen3-8B)*

以下の表4は、Qwen3-8BにおけるGEPAと他オプティマイザ（GRPO、MIPROv2）の最終的なパフォーマンスをまとめている。

#### Table 4: Benchmark results for different optimizers with Qwen3 8B
| \textbf{Qwen3 8B} | \textbf{HotpotQA} | \textbf{IFBench} | \textbf{Hover} | \textbf{PUPA} | \textbf{AIME-2025} | \textbf{LiveBench-Math} | \textbf{Aggregate} | \textbf{Improvement} |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Baseline | 42.33 | 36.90 | 35.33 | 80.82 | 27.33 | 48.70 | 45.23 | --- |
| GRPO | 43.33 | 35.88 | 38.67 | 86.66 | **38.00** | 51.26 | 48.91 | +3.68 |
| MIPROv2 | 55.33 | 36.22 | 47.33 | 81.55 | 20.00 | 46.60 | 47.84 | +2.61 |
| GEPA | 62.33 | **38.61** | **52.33** | **91.85** | 32.00 | **51.95** | **54.85** | **+9.62** |
| GEPA+Merge | **64.33** | 28.23 | 51.67 | 86.26 | 32.00 | **51.95** | 52.40 | +7.17 |
| **Total optimization budget (# rollouts)** | | | | | | | | |
| GEPA (+Merge) | 6871 | 3593 | 7051 | 2426 | 1839 | 1839 | 3936 | --- |
| GRPO | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | --- |

> **考察**: AIMEを除くすべてのベンチマークでGEPAがGRPOとMIPROv2を上回った。また注目すべき点として、GRPOが24,000回のロールアウトを消費しているのに対し、GEPAは平均して約3,900回のロールアウトで最適解に到達しており、**桁違いのサンプル効率**を実証した。自然言語ベースのリフレクションがスカラー信号（報酬）よりもはるかに豊かな情報源として機能することが分かる。

### 2. GPT-4.1-Miniおよび他オプティマイザとの比較
GPT-4.1-Miniにおいても、Trace（OptoPrime）やTextGradといったSOTAオプティマイザと比較して最も高いスコアを叩き出した。

#### Table 3: Benchmark results for different optimizers evaluated on GPT-4.1 Mini
| \textbf{GPT-4.1 Mini} | \textbf{HotpotQA} | \textbf{IFBench} | \textbf{Hover} | \textbf{PUPA} | \textbf{AIME-2025} | \textbf{LiveBench-Math} | \textbf{Aggregate} | \textbf{Improvement} |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Baseline | 38.00 | 47.79 | 46.33 | 78.57 | 49.33 | 58.20 | 53.03 | --- |
| Trace (OptoPrime) | 60.33 | 51.19 | 46.00 | 74.18 | 45.33 | 60.74 | 56.30 | +3.27 |
| MIPROv2-No-Demos | 38.00 | 52.04 | 51.33 | 91.85 | 48.67 | 60.97 | 57.14 | +4.11 |
| MIPROv2 | 58.00 | 49.15 | 48.33 | 83.37 | 51.33 | 61.84 | 58.67 | +5.64 |
| TextGrad | 62.33 | 48.64 | 47.67 | 85.68 | 46.67 | 63.84 | 59.14 | +6.11 |
| GEPA | **69.00** | 52.72 | 51.67 | 94.47 | **59.33** | **64.13** | 65.22 | +12.19 |
| **GEPA+Merge** | 65.67 | **55.95** | **56.67** | **96.46** | **59.33** | **64.13** | **66.36** | **+13.33** |
| **Optimized with Qwen3-8B, evaluated on GPT-4.1-Mini** | | | | | | | | |
| GEPA-Qwen-Opt | 65.67 | 49.83 | 54.67 | 90.05 | 52.67 | 59.31 | 62.03 | +9.00 |

> **考察**: オプティマイザとしての性能が+13.33%向上し、各タスクベースの手法（TextGrad等）を大きく上回った。さらに興味深いのは「Cross-model generalization（他モデルへの汎化）」である。パラメータ数の小さい`Qwen3-8B`で最適化させたプロンプトをそのまま`GPT-4.1-Mini`へ適応したゼロショット設定（`GEPA-Qwen-Opt`）においてさえも+9.00%の向上を見せており、GPT-4.1上で直接最適化したMIPROv2等を超える性能を発揮した。これはGEPAがモデル特有の表面的なハックではなく、タスクの本質的な解法を自然言語として提示できている証左と言える。

![GPT-4.1-Miniでのオプティマイザ性能の集計グラフ](./images/optimizer_performance_gpt-41-mini.png)
*(Figure: Optimizer performance on GPT-4.1-Mini)*

### 3. パレートベースの候補選択のアブレーション（Ablation）
単一のベスト候補を追う手法（SelectBestCandidate）との性能差は以下の通りである。

#### Table 13: Comparing candidate selection strategies across different tasks with Qwen3 8B
| \textbf{Qwen3 8B} | \textbf{HotpotQA} | \textbf{IFBench} | \textbf{Hover} | \textbf{PUPA} | \textbf{Aggregate} | \textbf{Improvement} |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Baseline | 42.33 | 36.90 | 35.33 | 80.82 | 48.84 | --- |
| SelectBestCandidate | 58.33 | 30.44 | 45.33 | 85.45 | 54.89 | +6.05 |
| BeamSearch | 57.33 | 36.39 | 41.00 | 81.08 | 53.95 | +5.11 |
| GEPA | **62.33** | **38.61** | **52.33** | **91.85** | **61.28** | **+12.44** |

> **考察**: 単一の最良スコアのみに注目するSelectBestCandidate（TextGradでも用いられる手法）や、トップNの一様な検索を行うBeamSearchは、容易に局所最適に陥ってしまい、+5~6%の向上に留まった。一方、GEPAが採用したパレートベースの進化戦略は多様性を維持しながら安定して探索木を構築できるため、+12.44%もの劇的な改善をもたらし、そのアルゴリズムの有効性が立証された。

### 4. 特殊タスクへの応用（GPU/NPU向けのコード生成と最適化）
GEPAは純粋な自然言語タスクだけでなく、コンパイラや実行環境からのフィードバックを得るプログラミングタスクにも応用可能である。論文ではCUDAカーネルコードの最適化において、ベースライン（PyTorch-eager）を超える高速なカーネル生成タスクなどでも成果を上げていることが示されている。

![CUDAカーネル最適化でのGEPAの性能](./images/kernelbench_fastp_vs_budget.png)
*(Figure: GEPA for CUDA kernel optimization. fast_p vs rollouts)*

![AMD NPUs向けカーネルの生成タスクにおけるGEPAの利用率推移](./images/npueval_vec_util_gpt4o.png)
*(Figure: Vector utilization rates on AMD NPUs using GEPA)*
