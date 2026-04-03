# NATURAL LANGUAGE REINFORCEMENT LEARNING

## 背景
現在、AIエージェントは環境との継続的な相互作用を通じて学習する方向へ進化しているが、従来の強化学習 (RL) には課題があった。従来のRLでは、状態や行動の価値をスカラー値（数値）で表現・圧縮しているため、「なぜその行動の評価が高いのか / 低いのか」という理由（Why）をエージェント自身が深く理解できない。その結果、良い行動を偶然発見するまで試行錯誤を繰り返すだけの受動的なサンプリング（受動的な学習）にならざるを得ず、Reasoning（推論）能力があらかじめ備わっていない小規模モデル等では性能向上が難しい（Chain-of-Thought (CoT) の退化などが起こる）という問題があった。本研究は、この問題を解決し、エージェントが自ら理由を考えながら能動的かつ熟考的に学習（active and deliberative learning）できるフレームワークとして、**Natural Language Reinforcement Learning (NLRL)** を提案している。

## 手法
NLRLは、従来のRLが持つコアコンポーネントを自然言語の表現空間へと再定義したものである。

1. **Language Value Function (LVF)**
スカラー値の代わりに、LLMを用いて軌道分布（将来の展開）を自然言語による評価（narrative）として生成させる。
$$
Q^{L}_\pi(s_t,a_t)=D_{L}\left(\mathrm{\left(s,a,r\right)}_{t+1: \infty}\sim P_\pi \mid s_t, a_t\right), V^{L}_\pi(s_{t}) = D_{L}\left(\mathrm{a_{t}, \left(s,a\right)}_{t+1: \infty}\sim P_\pi \mid s_t\right)
$$

2. **Language Bellman Equation と Language MC/TD 評価**
従来のMC（モンテカルロ）推定やTD（時間差分）推定のアナロジーとして、言語による推定を定義する。
言語MC評価:
$$
V^{L}_\pi(s_{t})\approx G_{1}\left(\left\{\mathrm{a_{t}^n, \left(s,a\right)}_{t+1: \infty}^{n}\right\}_{n=1}^{K_{MC}}\right)
$$
言語TD評価:
$$
V_\pi^{L}(s_t)\approx G_1\Big(\big\{G_2\big(d(s_t,a_t^n,r(s_t,a_t^n),s_{t+1}^n),V_\pi^L(s_{t+1}^n)\big)\big\}_{n=1}^{K_{TD}} \Big)
$$
ここで、 $G_{1}$ と $G_{2}$ は情報の集約を行う言語アグリゲーター（LLM）であり、 $d$ は遷移履歴の記述である。

3. **Language Policy Improvement**
LLM自身を方策改善オペレータ（ $I$ ）として用いる。現在の行動候補とそれに対応する言語評価 $Q^{L}_\pi$ を提示し、LLMに内省的なCoTを行わせて最も優れた行動を選択・改善させる。その後、改善されたテキスト出力を教師データとして、言語方策モデル $\pi_{L}$ を教師あり微調整（SFT）して更新する。

## 結果
論文ではMaze、Breakthrough、Tic-Tac-Toe、FrozenLakeという複数の環境において、NLRLの各コンポーネントが機能することを実証している。特にLLMエージェントが能動的にフィードバックを解釈し、従来のRLよりも効率的で安定した学習を行う結果を示した。

### 抽出画像と結果
*注：以下に続く結果セクションでは論文中に記載されているすべての図表を網羅的に記載し、考察をまとめている。*

![Comparison between NLRL and traditional RL](./images/nlrl_ragen.png)
従来のRL（左）がスカラーのフィードバックによってサンプリング依存で学習するのに対し、NLRL（右）はテキストによる詳細なフィードバックを受け取り、戦略的な分析を方針に反映できる点を示している。

![Comparing after-train reasoning on FrozenLake](./images/ragen_vs_nlrl.png)
PPOなどを用いた従来型の手法（RAGEN）では学習後に思考プロセス（CoT）が短縮・退化してしまうのに対し、NLRLでは学習後も詳細な盤面評価や将来予測を含むCoTが維持されている。

![NLRL pipeline Implementation](./images/nlrl_main.png)
NLRLをTic-Tac-Toe環境へ適用する際の完全なActor-Criticのパイプライン（1〜7のステップ）。

![FrozenLake experiment results](./images/frozenlake_compare.png)
FrozenLake環境での結果。決定論的遷移（a）および確率論的遷移（b）の双方において、RLベース（RAGEN）やランダム、SFTベースラインよりも高く安定した成功率をNLRLが達成している。

![Tic-Tac-Toe Natural Language Actor Critic Results](./images/nlac-combined.png)
Tic-Tac-Toeにおいてランダムベースの相手と対戦した場合の学習曲線。NLRLは従来の手法やPPOと比較して圧倒的な勝率（Win Rate）に到達している。

![Breakthrough experiment results](./images/breakthrough_exp.png)
Breakthroughによる評価（言語TDによる学習）。学習を行ったモデルは、強力なMCTSエージェントによる盤面評価に匹敵する精度（0.85以上）に達しており、既存モデルによる単純なPromptingから大幅な改善が見られた。


### 表データ（すべての行・列を書き起こし）

**Table 1: Comparing detailed reasoning on FrozenLake environment between RAGEN and NLRL using Llama3.1-8B-Instruct.**
| Methods | Reasoning After Training |
| :------- | :------- |
| **RAGEN** | `(THINK):` My thoughts are to go to the goal <br>`(Action):` Up |
| **NLRL** | `(THINK):` Based on the evaluations of the next board positions, moving up results in the highest final evaluation of +5, indicating that P is one block closer to the goal position G after the move. Although there is a hole one block away from P after moving up, the potential strategy of moving up and then moving right can help P avoid the hole and arrive at the goal position. In contrast, moving left does not immediately change P's position, and moving down moves P away from the goal position G. Therefore, moving up is the most favourable move. <br>`(Action):` Up |

**Table 2: Language GPI results with ablations on look-ahead steps N and variations number K.**
| Avg Reward | Double T Maze | Medium Maze |
| :--- | :--- | :--- |
| *Language policy $\pi^L(s)$* | -27.29±4.43 | -27.05±5.27 |
| *Language value function $Q^L(s,a)$ + improvement $I$* | -18.33±6.11 | -33.57±14.41 |
| *Language GPI (1 variation, 3 look ahead steps)* | -17.85±3.68 | -20.85±7.59 |
| *Language GPI (4 variations, 1 look ahead steps)* | -17.48±4.53 | -12.65±4.72 |
| *Language GPI (4 variations, 3 look ahead steps)* | -12.74±4.47 | -15.09±4.44 |
| *Language GPI (6 variations, 3 look ahead steps)* | -12.15±2.96 | -15.44±4.97 |
| *Language GPI (8 variations, 3 look ahead steps)* | **-11.19±2.86** | **-12.23±4.49** |

**Table 3: Rollout Parameters**
| Parameter | Value |
| :--- | :--- |
| Parallel Environments | 192 |
| Lookahead Step | 4 |
| Lookahead Rollout Number | 4 |
| Deduplicate State | True |

**Table 4: LLM sampling parameters for prompting.**
| LLM Sampling Parameter | Value |
| :--- | :--- |
| Temperature | 1.0 |
| Top K | 50 |
| Top P | 0.95 |
| Max Tokens | 512 |

**Table 5: Data Collection Parameters (general)**
| Parameter | Value |
| :--- | :--- |
| Max Sequence Length | 1024 |
| Warmup Ratio | 0.03 |
| Learning Rate | 2e-5 |
| Learning Rate Scheduler | Constant |
| Dtype | bfloat16 |
| Per Device Train Batch Size | 4 |
| Gradient Accumulation Step | 8 |
| Training Epoch | 2 |
| Number of GPUs | 4 |
| Distributed Framework | FSDP |

**Table 6: Data Collection Parameters**
| Parameter | Value |
| :--- | :--- |
| Parallel Environments | 64 |
| Trajectories per Iteration | 512 |
| Monte Carlo Samples ($K_{MC}$) | 5 |
| Policy Samples per State ($N_{sample}$) | 10 |
| Top-k Actions | 10 |

**Table 7: Model Training Hyperparameters**
| Hyperparameter | Value |
| :--- | :--- |
| Learning Rate | 1e-5 |
| Learning Rate Schedule | Constant |
| Training Epochs per Iteration | 2 |
| FSDP Configuration | Full Sharding |
| Gradient Checkpointing | Enabled |
| Batch Size | 8 |
| Max Sequence Length | 1024 |
| Training Hardware | 4 × H100 GPUs |

**Table 8: Buffer Management Configuration**
| Parameter | Value |
| :--- | :--- |
| Buffer History Length ($K_{buffer}$) | 3 iterations |
| Merging Strategy | Equal sampling |
| Buffer Content | State-action pairs with MC estimates |

**Table 9: Policy Evaluation Configuration**
| Parameter | Value |
| :--- | :--- |
| MC Trajectories per State-Action | 5 |
| Trajectory Completion | Full game |
| Value Aggregation | Average over returns |
| Sampling Temperature | 0.7 |
| Action Space Size | 9 positions (0-8) |

**Table 10: PPO Training Hyperparameters**
| Parameter | Value |
| :--- | :--- |
| Learning Rate (Actor) | 1e-5 |
| Learning Rate (Critic) | 1e-5 |
| PPO Epochs | 1 |
| Batch Size | 16 |
| Gradient Accumulation Steps | 2 |
| Value Loss Coefficient | 0.5 |
| Entropy Coefficient | 0.01 |
| PPO Clip Range | 0.2 |
| Discount Factor ($\gamma$) | 0.99 |
| GAE Parameter ($\lambda$) | 0.95 |

**Table 11: Comparing detailed reasoning on FrozenLake environment between RAGEN and NLRL.**
| Methods | Map | Initial Stage | Late Training |
| :------- | :------- | :------- | :------- |
| RAGEN (Qwen2.5-0.5B-Instruct) | `_G0_`<br>`___O`<br>`PO__`<br>`____` | `(THINK):` Let's start by considering the initial state: <MAP>. The goal is to reach the target 'PO___' from the hole 'O__O__O__O'. I'll start by moving to the left to avoid the hole. <br>`(Action):` Left \|\| Up | `(THINK):` Forbid the goal and go left then up. <br>`(Action):` Left \|\| Up |
| RAGEN (Qwen2.5-7B-Instruct) |  | `(THINK):` Move left to avoid the hole and then go up to reach the goal. <br>`(Action):` Left \|\| Up | `(THINK):` Up may lead to the hole or the target. <br>`(Action):` Up \|\| Up |
| RAGEN (Llama3.1-8B-Instruct) |  | `(THINK):` To avoid the hole and go to the target, I should go up to stay safe and then move to the right to approach the goal from a safe distance. <br>`(Action):` Up \|\| Right | `(THINK):` My thoughts are to go to the goal <br>`(Action):` Up \|\| Right |
| **NLRL** (Llama3.1-8B-Instruct) |  | `(THINK):` The current board position is <MAP>. The goal is on the top left, and the player is on the bottom left. The player is not in the hole. The available moves are 1, 2, 3, 4. Since the player is already on the leftmost position, moving left is not an option. The player can move down to get closer to the goal. Therefore, the best next move for P is to play action 2 to move down.  <br>`(Action):` Down | `(THINK):` Based on the evaluations of the next board positions, moving up results in the highest final evaluation of +5, indicating that P is one block closer to the goal position G after the move. Although there is a hole one block away from P after moving up, the potential strategy of moving up and then moving right can help P avoid the hole and arrive at the goal position. In contrast, moving left does not immediately change P's position, and moving down moves P away from the goal position G. Therefore, moving up is the most favourable move. <br>`(Action):` Up |

### 考察 
NLRLは、RL特有の高分散な勾配推定からのサンプリング依存を脱却し、環境とテキストベースで対話することで戦略的で能動的な思考プロセスを自発的に学習できることを示している。Table 11で明確に比較されている通り、単純なスカラーのPPOでは報酬を追求する過程で不要と見なされたCoT（思考プロセス）が崩壊してしまうが、NLRLのアーキテクチャでは言語モデル間のフィードバックが維持されるため、学習後期になっても高い解釈性と論理的な思考プロセスを維持できる大きなメリットがある。また、各種アブレーションの結果（Table 2）から、Language GPIにおける分散（Lookaheadの数等のパラメータ）を増やすことで安定して改善できることも確認された。
