# LARGE LANGUAGE MODELS AS OPTIMIZERS

## 背景
最適化（Optimization）は機械学習やオペレーションズ・リサーチをはじめとする多くの分野において不可欠であるが、勾配を持たない（derivative-free）最適化問題においては、探索空間や目的関数の性質に合わせて手作業でヒューリスティックな最適化手法を調整する必要があった。一方、近年発展が著しい大規模言語モデル（LLMs）は、高度な自然言語処理能力を持ち、コンテキスト内情報をゼロショットで理解し適応的な推論を行うことができる。
本研究では、このLLMを「ブラックボックス最適化器（Optimizer）」として直接活用する新しいフレームワーク「Optimization by PROmpting (OPRO)」を提案する。最適化問題を自然言語で記述することで、微細な数式やソルバーを構築することなく、迅速にタスクに適応し、解を探索・最適化することが可能となる。

## 手法
OPROは以下のステップでLLMを用いて反復的に最適化ループを回す：
1. **メタプロンプト (Meta-prompt) の構築**:
   LLMへの入力となるメタプロンプトには、タスクの説明（自然言語による指示と少数のExemplars）と、これまでに生成された解（ソリューション）とその評価スコアからなる「過去の最適化履歴（Optimization trajectory）」を含める。コンテキスト（LLMの入力長）には限界があるため、生成されたすべての解を入れるわけではなく、**「過去の全ステップを通じて生成された解の中から、最もスコアが高かった上位の解（プロンプト最適化の実験ではトップ20個）」**のみを抽出してメタプロンプトに組み込む。そして、この抽出されたトップ20の解をスコアの低い順から高い順（昇順）に並べて提示することで、LLMに「どのようなアプローチの修正がスコア上昇に繋がるのか」という改善の方向性（擬似的なテキスト勾配）をコンテキスト内で学習させる。
2. **解の生成 (Solution Generation)**:
   Optimizer LLM（例：PaLM 2-L, text-bison, GPT-3.5/4など）は、メタプロンプトを受け取り、過去の解から優れた要素を組み合わせて新しい候補解を複数（デフォルトでは各ステップ8個）生成する。サンプリング温度（Temperature）を細かく制御することで、これまでに発見された解の近傍を「活用（Exploitation）」するか、大きく異なる解を「探索（Exploration）」するかのトレードオフのバランスを取る（実験上はTemperature=1.0が最も性能が高かった）。
3. **評価 (Evaluation)**:
   生成された新しい複数の解は、Scorer LLMによって**すべて同一の訓練データセット（GSM8K等の訓練セットの一部）**上で一斉にテスト・評価される。プロンプト最適化タスクの場合、その「用意された同一の複数問題セット全体を通じた平均正答率（Accuracy）」がそのプロンプト候補のスコアとなる。つまり、特定の問題（簡単な問題）だけをたまたま解けた解が高く評価されるわけではなく、全員が同じ条件でバッチテストを受けるため、ベースラインが解ける簡単な問題に加え「より難易度の高い問題」も正解できた真に汎用性の高いプロンプトだけが上位スコアとして生き残る仕組みになっている。評価が終わると、上位解はメタプロンプトの履歴へと追加され、最高スコアが収束するか規定のステップ数に達するまでこの最適化サイクルを繰り返す。

## 結果
OPROを適用した結果、線形回帰や巡回セールスマン問題（TSP）などで小規模な問題を少ないステップで最適解へ導くことに成功した。さらに「LLM向けのプロンプトを最適化する（プロンプト最適化タスク）」に適用した結果、GSM8KやBig-Bench Hard（BBH）の23タスクにおいて、人間が設計したベースライン（例えば "Let's think step by step."など）を大きく上回るプロンプトを自動発見した。具体的にはGSM8Kにおいてベースラインより最大8%も高いゼロショット推論精度を実現し、見出されたプロンプトは同種の推論タスク（MultiArith, AQuA）等でも高い汎化性能を示した。

アブレーション調査から、メタプロンプトに「過去の解とそれぞれのスコア」を含め昇順に整列して提示することが性能向上に最も寄与することが裏付けられた。スコア情報がないとLLMはどのプロンプトが優れているか判別できず、方向性をもった反復改善が行われない。

以下に論文中に示されているすべての図・表と、それに基づく得られた詳細な結果を記載する。

![workflow.png](./images/workflow.png)
*(Fig. 1) OPROの全体フレームワーク概要。Meta-promptを受け取ったLLMが新解を生成し、評価後に再度Meta-promptへ反映させるループを示す。*

![gsm8k_s_pretrained_palm_2_l_o_finetuned_palm_2_l.png](./images/gsm8k_s_pretrained_palm_2_l_o_finetuned_palm_2_l.png)
*(Fig. 2) プロンプト最適化により生成された命令文のスコア推移。ステップが進むにつれてVarianceが縮小し、かつ平均スコアが増加・高い精度で推移していることが確認できる。*

### Table 1: GSM8Kにおけるゼロショット学習精度の高いインストラクション
| Source | Instruction | Acc |
| :--- | :--- | :--- |
| *Baselines* | | |
| Kojima et al. | Let's think step by step. | 71.8 |
| Zhou et al. | Let’s work this out in a step by step way to be sure we have the right answer. | 58.8 |
| | (empty string) | 34.0 |
| *Ours* | | |
| PaLM 2-L-IT | Take a deep breath and work on this problem step-by-step. | **80.2** |
| PaLM 2-L | Break this down. | 79.9 |
| gpt-3.5-turbo | A little bit of arithmetic and a logical approach will help us quickly arrive at the solution to this problem. | 78.5 |
| gpt-4 | Let's combine our numerical command and clear thinking to quickly and accurately decipher the answer. | 74.5 |

### Table 2: Linear regression by optimizer LLMs (探索されたステップ数と探索されたユニークパスの平均)
| w_true | b_true | text-bison (steps) | gpt-3.5-turbo (steps) | gpt-4 (steps) | text-bison (explorations) | gpt-3.5-turbo (explorations) | gpt-4 (explorations) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 15 | 14 | 5.8 ± 2.6 | 7.6 ± 4.5 | **4.0** ± 1.5 | 40.0 ± 12.4 | 36.0 ± 15.2 | **17.2** ± 5.1 |
| 17 | 17 | **4.0** ± 1.8 | 12.6 ± 6.0 | 6.0 ± 3.7 | 33.4 ± 11.7 | 53.8 ± 16.9 | **26.0** ± 10.6 |
| 16 | 10 | **3.8** ± 2.2 | 10.4 ± 5.4 | 6.2 ± 3.1 | 30.2 ± 13.4 | 42.8 ± 16.3 | **24.2** ± 8.2 |
| 3 | 5 | **9.8** ± 2.8 | 10.8 ± 2.7 | 12.2 ± 2.0 | 55.8 ± 16.1 | 39.6 ± 10.1 | **33.0** ± 4.0 |
| 25 | 23 | 19.6 ± 11.4 | 26.4 ± 18.3 | **12.2** ± 3.7 | 104.0 ± 52.3 | 78.6 ± 26.2 | **44.2** ± 8.3 |
| 2 | 30 | **31.4** ± 6.3 | 42.8 ± 9.7 | 38.0 ± 15.9 | 126.4 ± 17.7 | 125.6 ± 21.7 | **99.0** ± 24.6 |
| 36 | -1 | **35.8** ± 6.4 | 45.4 ± 16.9 | 50.4 ± 18.8 | 174.0 ± 28.2 | 142.2 ± 31.2 | **116.4** ± 32.7 |

### Table 3: Results of the Traveling Salesman Problem (TSP) 
| n | NN (optimality gap %) | FI (optimality gap %) | text-bison (optimality gap %) | gpt-3.5-turbo (optimality gap %) | gpt-4 (optimality gap %) | text-bison (# steps) | gpt-3.5-turbo (# steps) | gpt-4 (# steps) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 10 | 13.0 ± 1.3 | 3.2 ± 1.4 | **0.0** ± 0.0 | **0.0** ± 0.0 | **0.0** ± 0.0 | 40.4 ± 5.6 (5) | 46.8 ± 9.3 (5) | **9.6** ± 3.0 (5) |
| 15 | 9.4 ± 3.7 | 1.2 ± 0.6 | 4.4 ± 1.3 | 1.2 ± 1.1 | **0.2** ± 0.2 | N/A (0) | 202.0 ± 41.1 (4) | **58.5** ± 29.0 (4) |
| 20 | 16.0 ± 3.9 | **0.2** ± 0.1 | 30.4 ± 10.6 | 4.4 ± 2.5 | 1.4 ± 0.6 | N/A (0) | 438.0 ± 0.0 (1) | **195.5** ± 127.6 (2) |
| 50 | 19.7 ± 3.1 | **9.8** ± 1.5 | 219.8 ± 13.7 | 133.0 ± 6.8 | 11.0 ± 2.6 | N/A (0) | N/A (0) | N/A (0) |

### Table 4: Test accuracies on GSM8K (with different scorer-optimizer pairs)
| Scorer | Optimizer / Source | Instruction position | Top instruction | Acc |
| :--- | :--- | :--- | :--- | :--- |
| *Baselines* | | | | |
| PaLM 2-L | Kojima et al. | A_begin | Let's think step by step. | 71.8 |
| PaLM 2-L | Zhou et al. | A_begin | Let’s work this out in a step by step way to be sure we have the right answer. | 58.8 |
| PaLM 2-L | | A_begin | Let's solve the problem. | 60.8 |
| PaLM 2-L | | A_begin | (empty string) | 34.0 |
| text-bison | Kojima et al. | Q_begin | Let's think step by step. | 64.4 |
| text-bison | Zhou et al. | Q_begin | Let’s work this out in a step by step way to be sure we have the right answer. | 65.6 |
| text-bison | | Q_begin | Let's solve the problem. | 59.1 |
| text-bison | | Q_begin | (empty string) | 56.8 |
| *Ours* | | | | |
| PaLM 2-L | PaLM 2-L-IT | A_begin | Take a deep breath and work on this problem step-by-step. | **80.2** |
| PaLM 2-L | PaLM 2-L | A_begin | Break this down. | 79.9 |
| PaLM 2-L | gpt-3.5-turbo | A_begin | A little bit of arithmetic and a logical approach will help us quickly arrive at the solution to this problem. | 78.5 |
| PaLM 2-L | gpt-4 | A_begin | Let's combine our numerical command and clear thinking to quickly and accurately decipher the answer. | 74.5 |
| text-bison | PaLM 2-L-IT | Q_begin | Let's work together to solve math word problems! First, we will read and discuss the problem together to make sure we understand it. Then, we will work together to find the solution. I will give you hints and help you work through the problem if you get stuck. | 64.4 |
| text-bison | text-bison | Q_end | Let's work through this problem step-by-step: | **68.5** |
| text-bison | gpt-3.5-turbo | Q_end | Analyze the given information, break down the problem into manageable steps, apply suitable mathematical operations, and provide a clear, accurate, and concise solution, ensuring precise rounding if necessary. Consider all variables and carefully consider the problem's context for an efficient solution. | 66.5 |
| text-bison | gpt-4 | Q_begin | Start by dissecting the problem to highlight important numbers and their relations. Decide on the necessary mathematical operations like addition, subtraction, multiplication, or division, required for resolution. Implement these operations, keeping in mind any units or conditions. Round off by ensuring your solution fits the context of the problem to ensure accuracy. | 62.7 |

### Table 5: Top instructions on BBH Tasks
| Scorer | Optimizer | Instruction position | Instruction | Acc |
| :--- | :--- | :--- | :--- | :--- |
| *movie_recommendation* | | | | |
| PaLM 2-L | PaLM 2-L-IT | A_begin | Based on your input, I have analyzed the given movies in terms of genre, plot, tone, audience rating, year of release, director, cast, and reviews. I have also taken into account the given options. The movie that is most similar to the given movies in terms of all these factors is: | 90.8 |
| PaLM 2-L | PaLM 2-L | A_begin | The best film: | 88.4 |
| PaLM 2-L | gpt-3.5-turbo | A_begin | Let's uncover the perfect movie recommendation from the options provided, ensuring an exceptional cinematic experience together as we select the most captivating and satisfying choice that will keep us thoroughly engaged and immersed until the very end. | 88.0 |
| text-bison | PaLM 2-L-IT | Q_begin | What is the highest-rated movie similar to the given movies, with a similar IMDb rating and released in the same year? | 91.6 |
| text-bison | gpt-3.5-turbo | Q_begin | Based on the movie list provided, carefully consider your preferences and make a well-informed decision. | 70.8 |
| *ruin_names* | | | | |
| PaLM 2-L | PaLM 2-L-IT | A_begin | Which is the funniest pun on the artist or movie name? | 88.0 |
| PaLM 2-L | PaLM 2-L | A_begin | Answer for ruin: | 83.6 |
| PaLM 2-L | gpt-3.5-turbo | A_begin | Prepare to have a side-splittingly funny time as we uncover the most clever and hilarious alternatives for these artist or movie names, challenging your wit to guess the correct one with a burst of creativity, humor, and imaginative twists! | 86.8 |
| text-bison | PaLM 2-L-IT | Q_begin | A humorous edit of an artist or movie name can be created by replacing one or more letters to form a new word or phrase that sounds similar but has a different meaning. The new word or phrase should be relevant to the original word, but it should also be a surprise, which makes the edit funny. For example, the artist or movie name "Rocky" can be changed to "Ricky," and "Schindler's List" can be changed to "Schindler's Lift." Be creative and have fun! | 83.6 |
| text-bison | gpt-3.5-turbo | Q_begin | Choose the option that offers the most clever and humorous alteration of the given artist or movie name. Let your creativity shine and select the answer that will undoubtedly bring a smile to your face! Make sure to think outside the box! | 75.2 |
| *temporal_sequences* | | | | |
| text-bison | PaLM 2-L-IT | Q_begin | To determine the time period when a person went to a place, first identify all the time periods when the person's whereabouts are unknown. Then, rule out any time periods during which the person was seen doing something else or the place was closed. The remaining time periods are the possible times when the person could have gone to the place. | 80.4 |
| text-bison | gpt-3.5-turbo | Q_begin | Identify the optimal time slot for the individual to engage in the mentioned location/activity considering the given sightings and waking up time, taking into account the opening and closing times of the location and the duration of each event. | 53.6 |

### Table 6: Transferability across datasets
| Scorer | Source | Instruction position | Instruction | MultiArith | AQuA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Baselines* | | | | | |
| PaLM 2-L | Kojima et al. | A_begin | Let's think step by step. | 85.7 | 44.9 |
| PaLM 2-L | Zhou et al. | A_begin | Let’s work this out in a step by step way to be sure we have the right answer. | 72.8 | 48.4 |
| PaLM 2-L | | A_begin | Let's solve the problem. | 87.5 | 44.1 |
| PaLM 2-L | | A_begin | (empty string) | 69.3 | 37.8 |
| text-bison | Kojima et al. | Q_begin | Let's think step by step. | 92.5 | 31.9 |
| text-bison | Zhou et al. | Q_begin | Let’s work this out in a step by step way to be sure we have the right answer. | 93.7 | 32.3 |
| text-bison | | Q_begin | Let's solve the problem. | 85.5 | 29.9 |
| text-bison | | Q_begin | (empty string) | 82.2 | 33.5 |
| *Ours* | | | | | |
| PaLM 2-L | PaLM 2-L-IT on GSM8K | A_begin | Take a deep breath and work on this problem step-by-step. | **95.3** | **54.3** |
| text-bison | PaLM 2-L-IT on GSM8K | Q_begin | Let's work together to solve math word problems! First, we will read and discuss the problem together to make sure we understand it. Then, we will work together to find the solution. I will give you hints and help you work through the problem if you get stuck. | **96.8** | **37.8** |

### BBH全体でのタスクごとの精度と最適化推移
Table 7〜15では、BBHに含まれる23種の全タスクにおいて各モデル・開始プロンプト別の詳細な精度や最適化されたプロンプトが記載・評価されている。空白のプロンプトやベースラインに比べて平均的に5〜20%の向上がBBHの23タスク全体で一貫して確認された。

### 完全な抽出テーブル一覧 (Table 7 - 15)

論文から抽出された精緻な定量評価結果（タスク別・モデル別）を含むすべてのテーブルです。

#### Table 7
**Caption:** Accuracies on BBH tasks: our found instructions with the \texttt{PaLM 2-L-IT

| Task | Scorer | Our Acc | ``Let's think step by step.'' Acc | ``Let’s work this out in a step by step way to be sure we have the right answer.'' Acc | empty string ``'' Acc |
|---|---|---|---|---|---|
|  |  | training / test / overall | training / test / overall | training / test / overall | training / test / overall |
| boolean\_expressions | `PaLM 2-L` | **90.0 / 83.5 / 84.8** | 90.0 / 83.0 / 84.4 | 82.0 / 74.0 / 75.6 | 74.0 / 71.0 / 71.6 |
| causal\_judgement | `PaLM 2-L` | **84.8 / 58.0 / 63.1** | 73.0 / 55.3 / 58.8 | 59.5 / 57.3 / 57.8 | 29.7 / 49.3 / 45.5 |
| date\_understanding | `PaLM 2-L` | **86.0 / 84.5 / 84.8** | 76.0 / 80.0 / 79.2 | 74.0 / 77.0 / 76.4 | 70.0 / 74.0 / 73.2 |
| disambiguation\_qa | `PaLM 2-L` | **80.0 / 69.0 / 71.2** | 40.0 / 52.5 / 50.0 | 48.0 / 47.0 / 47.2 | 54.0 / 57.5 / 56.8 |
| dyck\_languages | `PaLM 2-L` | **100.0 / 100.0 / 100.0** | 96.0 / 94.5 / 94.8 | 100.0 / 93.5 / 94.8 | 94.0 / 95.0 / 94.8 |
| formal\_fallacies | `PaLM 2-L` | **84.0 / 64.0 / 68.4** | 78.0 / 59.5 / 63.2 | 68.0 / 63.0 / 64.0 | 66.0 / 59.0 / 60.4 |
| geometric\_shapes | `PaLM 2-L` | **76.0 / 57.0 / 60.8** | 42.0 / 33.0 / 34.8 | 42.0 / 32.0 / 34.0 | 34.0 / 33.0 / 33.2 |
| hyperbaton | `PaLM 2-L` | **100.0 / 96.0 / 96.8** | 78.0 / 75.0 / 75.6 | 74.0 / 72.5 / 72.8 | 88.0 / 89.0 / 88.8 |
| logical\_deduction\_seven\_objects | `PaLM 2-L` | **74.0 / 57.0 / 60.4** | 46.0 / 37.0 / 38.8 | 34.0 / 30.5 / 31.2 | 46.0 / 45.5 / 45.6 |
| movie\_recommendation | `PaLM 2-L` | **92.0 / 90.5 / 90.8** | 62.0 / 52.5 / 54.4 | 52.0 / 48.0 / 48.8 | 80.0 / 83.0 / 82.4 |
| multistep\_arithmetic\_two | `PaLM 2-L` | **72.0 / 55.5 / 58.8** | 42.0 / 46.0 / 45.2 | 60.0 / 50.5 / 52.4 | 4.0 / 3.5 / 3.6 |
| navigate | `PaLM 2-L` | **92.0 / 75.0 / 78.4** | 68.0 / 62.0 / 63.2 | 70.0 / 64.0 / 65.2 | 38.0 / 37.5 / 37.6 |
| object\_counting | `PaLM 2-L` | **84.0 / 86.5 / 86.0** | 36.0 / 46.5 / 44.4 | 60.0 / 62.0 / 61.6 | 28.0 / 27.0 / 27.2 |
| penguins\_in\_a\_table | `PaLM 2-L` | **86.2 / 71.8 / 74.7** | 79.3 / 64.1 / 67.1 | 62.1 / 58.1 / 58.9 | 72.4 / 69.2 / 69.9 |
| reasoning\_about\_colored\_objects | `PaLM 2-L` | **98.0 / 85.5 / 88.0** | 82.0 / 79.5 / 80.0 | 82.0 / 75.0 / 76.4 | 42.0 / 35.0 / 36.4 |
| ruin\_names | `PaLM 2-L` | **88.0 / 88.0 / 88.0** | 70.0 / 55.0 / 58.0 | 80.0 / 75.5 / 76.4 | 88.0 / 76.5 / 78.8 |
| salient\_translation\_error\_detection | `PaLM 2-L` | **62.0 / 67.0 / 66.0** | 42.0 / 50.0 / 48.4 | 58.0 / 46.0 / 48.4 | 56.0 / 56.5 / 56.4 |
| snarks | `PaLM 2-L` | **85.7 / 83.2 / 83.7** | 60.0 / 62.2 / 61.8 | 54.3 / 53.1 / 53.4 | 51.4 / 60.1 / 58.4 |
| sports\_understanding | `PaLM 2-L` | **98.0 / 88.0 / 90.0** | 50.0 / 46.5 / 47.2 | 60.0 / 52.5 / 54.0 | 52.0 / 41.5 / 43.6 |
| temporal\_sequences | `PaLM 2-L` | **100.0 / 100.0 / 100.0** | 100.0 / 96.0 / 96.8 | 90.0 / 87.0 / 87.6 | 100.0 / 99.5 / 99.6 |
| tracking\_shuffled\_objects\_seven\_objects | `PaLM 2-L` | 32.0 / 16.5 / 19.6 | **58.0 / 61.5 / 60.8** | 54.0 / 55.5 / 55.2 | 14.0 / 23.5 / 21.6 |
| web\_of\_lies | `PaLM 2-L` | **62.0 / 52.0 / 54.0** | 46.0 / 41.5 / 42.4 | 24.0 / 31.0 / 29.6 | **54.0 / 54.0 / 54.0** |
| word\_sorting | `PaLM 2-L` | **54.0 / 54.5 / 54.4** | 2.0 / 4.5 / 4.0 | 12.0 / 9.5 / 10.0 | 20.0 / 22.5 / 22.0 |
| boolean\_expressions | `text-bison` | **98.0 / 87.0 / 89.2** | 72.0 / 61.5 / 63.6 | 88.0 / 78.0 / 80.0 | 80.0 / 68.5 / 70.8 |
| causal\_judgement | `text-bison` | **78.4 / 58.0 / 62.0** | 70.3 / 50.7 / 54.5 | 73.0 / 55.3 / 58.8 | **78.4 / 58.0 / 62.0** |
| date\_understanding | `text-bison` | **60.0 / 50.0 / 52.0** | 44.0 / 45.5 / 45.2 | 48.0 / 45.0 / 45.6 | 44.0 / 45.0 / 44.8 |
| disambiguation\_qa | `text-bison` | **68.0 / 73.0 / 72.0** | 4.0 / 6.0 / 5.6 | 4.0 / 15.5 / 13.2 | 52.0 / 68.5 / 65.2 |
| dyck\_languages | `text-bison` | **100.0 / 100.0 / 100.0** | 100.0 / 95.5 / 96.4 | 100.0 / 94.5 / 95.6 | 100.0 / 98.5 / 98.8 |
| formal\_fallacies | `text-bison` | 70.0 / 53.0 / 56.4 | 64.0 / 54.5 / 56.4 | **84.0 / 82.5 / 82.8** | 70.0 / 54.5 / 57.6 |
| geometric\_shapes | `text-bison` | **40.0 / 19.5 / 23.6** | 22.0 / 13.0 / 14.8 | 18.0 / 12.0 / 13.2 | 20.0 / 14.5 / 15.6 |
| hyperbaton | `text-bison` | **80.0 / 79.5 / 79.6** | 64.0 / 67.5 / 66.8 | 64.0 / 69.0 / 68.0 | 64.0 / 64.0 / 64.0 |
| logical\_deduction\_seven\_objects | `text-bison` | 66.0 / 53.5 / 56.0 | **56.0 / 58.0 / 57.6** | 56.0 / 56.0 / 56.0 | 58.0 / 56.5 / 56.8 |
| movie\_recommendation | `text-bison` | **98.0 / 90.0 / 91.6** | 68.0 / 63.0 / 64.0 | 66.0 / 62.0 / 62.8 | 68.0 / 64.0 / 64.8 |
| multistep\_arithmetic\_two | `text-bison` | **32.0 / 16.5 / 19.6** | 12.0 / 18.0 / 16.8 | 18.0 / 17.5 / 17.6 | 16.0 / 18.5 / 18.0 |
| navigate | `text-bison` | **72.0 / 61.0 / 63.2** | 56.0 / 55.0 / 55.2 | 60.0 / 56.5 / 57.2 | 56.0 / 57.0 / 56.8 |
| object\_counting | `text-bison` | **72.0 / 62.0 / 64.0** | 58.0 / 57.0 / 57.2 | 62.0 / 55.5 / 56.8 | 50.0 / 57.0 / 55.6 |
| penguins\_in\_a\_table | `text-bison` | **72.4 / 56.4 / 59.6** | 58.6 / 53.0 / 54.1 | 55.2 / 55.6 / 55.5 | 58.6 / 53.0 / 54.1 |
| reasoning\_about\_colored\_objects | `text-bison` | **82.0 / 77.0 / 78.0** | 76.0 / 72.5 / 73.2 | 78.0 / 73.0 / 74.0 | 74.0 / 69.5 / 70.4 |
| ruin\_names | `text-bison` | **88.0 / 82.5 / 83.6** | 66.0 / 65.5 / 65.6 | 66.0 / 62.5 / 63.2 | 64.0 / 66.0 / 65.6 |
| salient\_translation \_error\_detection | `text-bison` | **46.0 / 50.5 / 49.6** | 42.0 / 47.5 / 46.4 | 42.0 / 49.5 / 48.0 | 44.0 / 50.0 / 48.8 |
| snarks | `text-bison` | **80.0 / 81.8 / 81.5** | 68.6 / 77.6 / 75.8 | 71.4 / 76.2 / 75.3 | 77.1 / 84.6 / 73.1 |
| sports\_understanding | `text-bison` | **94.0 / 82.5 / 84.8** | 86.0 / 79.0 / 80.4 | 90.0 / 81.0 / 82.8 | 38.0 / 44.5 / 43.2 |
| temporal\_sequences | `text-bison` | **78.0 / 81.0 / 80.4** | 36.0 / 43.5 / 42.0 | 32.0 / 45.0 / 42.4 | 36.0 / 43.0 / 41.6 |
| tracking\_shuffled\_objects\_seven\_objects | `text-bison` | **32.0 / 15.5 / 18.8** | 10.0 / 17.0 / 15.6 | 10.0 / 18.0 / 16.4 | 12.0 / 15.5 / 14.8 |
| web\_of\_lies | `text-bison` | **62.0 / 50.0 / 52.4** | 48.0 / 45.5 / 46.0 | 48.0 / 44.0 / 44.8 | 52.0 / 51.5 / 51.2 |
| word\_sorting | `text-bison` | **24.0 / 17.5 / 18.8** | 10.0 / 12.0 / 11.6 | 4.0 / 8.0 / 7.2 | 4.0 / 7.5 / 6.8 |

#### Table 8
**Caption:** BBH task-wise instructions found by prompt optimization with the \texttt{PaLM 2-L

| Task | Our Instruction |
|---|---|
| boolean\_expressions | A Boolean expression is a well-formed expression consisting of variables, values, and logical operators. The expression must evaluate to a single True or False value. The order of precedence of the logical operators is as follows: NOT, AND, OR, XOR, IMP. Parentheses can be used to group subexpressions and to control the order of evaluation. |
| causal\_judgement | When considering questions about causation, a typical person would consider the following factors: whether the action or event was a necessary condition for the outcome to occur, a sufficient condition, a proximate cause, or a foreseeable cause. |
| date\_understanding | To find the date X time ago from today, first find today's date. Then subtract X time from today's date. If the current date is the last day of a month, then the date a month ago is the last day of the previous month. If the current date is not the last day of a month, then the date a month ago is the same day of the previous month. For example, if today is March 31, 2023, then the date a month ago is February 28, 2023. If today is April 1, 2023, then the date a month ago is March 1, 2023. |
| disambiguation\_qa | Identifying Antecedents of Pronouns: A Comprehensive Guide |
| dyck\_languages | First, look for the opening parentheses. Then, count the number of opening parentheses. Finally, close the parentheses in the reverse order that they were opened. |
| formal\_fallacies | A deductive argument is one where the conclusion follows necessarily from the premises. If the premises are true, then the conclusion must also be true. An invalid argument is one where it is possible for the premises to be true and the conclusion to be false. |
| geometric\_shapes | A closed polygonal chain is a series of connected line segments. The line segments can be straight or curved. The first and last line segments are connected. The line segments do not intersect each other except at their endpoints. A closed polygon can be described by an SVG path element, which starts at a given point, goes to one or more additional points, and then ends at the starting point. The path element can consist of straight line segments, curved segments, or a mixture of both. |
| hyperbaton | The correct adjective order in English is opinion, size, shape, age, color, origin, material, and purpose. If you have more than one adjective of the same type, they are usually placed in order of importance. For example, you would say "a large, old, Pakistani ship" rather than "an old, large, Pakistani ship." There are a few exceptions to these rules, but they are generally followed in most cases. |
| logical\_deduction \_seven\_objects | The following questions will test your ability to use deductive reasoning. You will be given a set of statements about a group of objects. You will then be asked to answer questions about the objects based on the statements. The statements in the questions are logically consistent, so you can use them to deduce the order of the objects. For each question, you must choose the option that is logically consistent with the information in the questions. |
| movie\_recommendation | Based on your input, I have analyzed the given movies in terms of genre, plot, tone, audience rating, year of release, director, cast, and reviews. I have also taken into account the given options. The movie that is most similar to the given movies in terms of all these factors is: |
| multistep\_arithmetic \_two | The order of operations in mathematics is PEMDAS, which stands for Parentheses, Exponents, Multiplication, Division, Addition, and Subtraction. When there are multiple operations of the same precedence, they must be performed from left to right. Note that multiplication and division have the same precedence, as do addition and subtraction. |
| navigate | You will return to the starting point if and only if (1) the total number of steps you take forward is equal to the total number of steps you take back, and (2) the total number of turns you make is a multiple of 180 degrees. |
| object\_counting | Here is a list of the objects you mentioned and their corresponding counts: |
| penguins\_in\_a\_table | Here is my new text: |
| reasoning\_about \_colored\_objects | Starting from the leftmost object in the row, I observe the following objects arranged in this order: |
| ruin\_names | Which is the funniest pun on the artist or movie name? |
| salient\_translation \_error\_detection | Instructions: Read the German sentence and its English translation carefully, then identify the type of error in the translation and select the correct option. There are six possible types of errors: Named Entities, Numerical Values, Modifiers or Adjectives, Negation or Antonyms, Facts, and Dropped Content. |
| snarks | Identify the sarcastic statement by considering the following factors: incongruity, exaggeration, understatement, context, speaker's intent, and audience's reaction. I will also consider the speaker's tone of voice, facial expressions, and body language. |
| sports\_understanding | I will determine if a sentence about an athlete is plausible by first checking if it is grammatically correct. If it is, I will then check if it is consistent with the athlete's sport, position, and real-world statistics. I will also check if it is consistent with the rules of the athlete's sport. If the sentence is consistent with all of these things, I will answer "yes", otherwise I will answer "no". |
| temporal\_sequences | The answer is the time that is not mentioned in the given statements. |
| tracking\_shuffled\_objects \_seven\_objects | Claire has the blue ball, Gertrude has the black ball, and Dave has the green ball. They are all happy with their new balls. |
| web\_of\_lies | The answer to a question is yes if there are an odd number of liars before the current speaker, and no if there are an even number of liars before the current speaker. If the current speaker is a truth-teller, they will say the opposite of what the previous person said, while a liar will say the same thing as the previous person said. |
| word\_sorting | Alphabetical order of given words: |

#### Table 9
**Caption:** BBH task-wise instructions found by prompt optimization with the \texttt{text-bison

| Task | Our Instruction |
|---|---|
| boolean\_expressions | Not (not False) and not not False is False |
| causal\_judgement | A typical person would likely answer the questions about causation as follows: |
| date\_understanding | Today is February 28, 2023. It is a Tuesday. Yesterday was Monday, February 27, 2023. Tomorrow will be Wednesday, March 1, 2023. A week ago, it was February 21, 2023, and a month ago, it was January 28, 2023. A year from now, it will be February 28, 2024. The day of the week is important to note because it will help us to correctly answer the questions below. Not all years are leap years that contain February 29. |
| disambiguation\_qa | A pronoun is a word that stands in for a noun. The noun that a pronoun refers to is called its antecedent. To identify the antecedent of a pronoun, look for the noun that the pronoun could be referring to. If there is only one possible noun, then that is the antecedent. If there are two or more possible nouns, then the antecedent is ambiguous. Use the context of the sentence to help you determine the correct antecedent. |
| dyck\_languages | \ \ |
| formal\_fallacies | How to Evaluate Deductive Validity of an Argument |
| geometric\_shapes | What shape is this SVG code drawing, and how many sides does it have? |
| hyperbaton | In English, adjectives are typically placed before nouns in a specific order. The order is: opinion, size, shape, age, color, origin, material, purpose, noun. For example, the sentence "the big, old, red barn" would be considered grammatically correct, while the sentence "the old, big, red barn" would not. Adjectives that come before nouns are called attributive adjectives, while adjectives that come after nouns are called predicative adjectives. |
| logical\_deduction \_seven\_objects | In this logical reasoning task, you will be given a series of paragraphs, each of which describes a set of objects arranged in a fixed order. The statements in each paragraph are logically consistent. You must read each paragraph carefully and use the information given to determine the logical relationships between the objects. You will then be asked a question about the order of the objects. Read each question carefully and choose the option that answers the question correctly. |
| movie\_recommendation | What is the highest-rated movie similar to the given movies, with a similar IMDb rating and released in the same year? |
| multistep\_arithmetic\_two | Let's solve these equations using PEMDAS order of operations. Remember that PEMDAS stands for parentheses, exponents, multiplication and division, and addition and subtraction. |
| navigate | Starting at the origin, facing north, follow the instructions. If your displacement from the origin is zero and your direction is unchanged, then your answer is Yes. Otherwise, your answer is No. |
| object\_counting | Let me help you count the items you have. Just list them one by one, separated by commas. I will then count each item and tell you how many items there are in total. |
| penguins\_in\_a\_table | This table shows information about penguins. The columns show the penguin’s name, age, height (in cm), and weight (in kg). The penguins are listed in order of their age, from youngest to oldest. |
| reasoning\_about \_colored\_objects | First, read the input carefully. Then, identify all the objects mentioned, their colors, and their positions. Next, visualize the objects and their positions in your mind. Finally, answer the questions accurately based on the information given. Make sure to pay attention to the order of the objects. |
| ruin\_names | A humorous edit of an artist or movie name can be created by replacing one or more letters to form a new word or phrase that sounds similar but has a different meaning. The new word or phrase should be relevant to the original word, but it should also be a surprise, which makes the edit funny. For example, the artist or movie name "Rocky" can be changed to "Ricky," and "Schindler's List" can be changed to "Schindler's Lift." Be creative and have fun! |
| salient\_translation \_error\_detection | The following translations from German to English contain a particular error. The error may be one of the following types: Named Entities, Numerical Values, Modifiers or Adjectives, Negation or Antonyms, Facts, or Dropped Content. Please identify the error. |
| snarks | The statement |
| sports\_understanding | To determine the plausibility of a sports sentence, I will first identify the sport, athletes, teams, and events mentioned in the sentence. Then, I will use my knowledge of the rules of the sport, the context of the sentence, common sense, and my knowledge of the world to determine whether the sentence is plausible. I will also consider the time period and location, as well as any other relevant information. Finally, I will return a score of 1 for plausible sentences and 0 for implausible ones. |
| temporal\_sequences | To determine the time period when a person went to a place, first identify all the time periods when the person's whereabouts are unknown. Then, rule out any time periods during which the person was seen doing something else or the place was closed. The remaining time periods are the possible times when the person could have gone to the place. |
| tracking\_shuffled\_objects \_seven\_objects | At the start of the game, Claire has a blue ball. Throughout the game, pairs of people swap balls. Claire ends up with the yellow ball. |
| web\_of\_lies | People in a group either tell the truth or lie. The truthfulness of a person's statement is determined by the statement of the previous person. If the previous person told the truth, then the current person who says the opposite is lying. If the previous person lied, then the current person who says the opposite is telling the truth. This rule applies to all subsequent statements. |
| word\_sorting | Sort the following words alphabetically, ignoring case and punctuation. Print the sorted list. |

#### Table 10
**Caption:** Accuracies on BBH tasks with the \texttt{gpt-3.5-turbo

| Task | Scorer | Our Acc (`begin`) | Our Acc (`end`) |
|---|---|---|---|
|  |  | training / test / overall | training / test / overall |
| boolean\_expressions | `PaLM 2-L` | 92.0 / 86.5 / 87.6 | N/A |
| causal\_judgement | `PaLM 2-L` | 81.1 / 58.7 / 63.1 | N/A |
| date\_understanding | `PaLM 2-L` | 86.0 / 82.0 / 82.8 | N/A |
| disambiguation\_qa | `PaLM 2-L` | 80.0 / 74.0 / 75.2 | N/A |
| dyck\_languages | `PaLM 2-L` | 100.0 / 100.0 / 100.0 | N/A |
| formal\_fallacies | `PaLM 2-L` | 88.0 / 63.5 / 68.4 | N/A |
| geometric\_shapes | `PaLM 2-L` | 60.0 / 41.0 / 44.8 | N/A |
| hyperbaton | `PaLM 2-L` | 88.0 / 93.0 / 92.0 | N/A |
| logical\_deduction\_seven\_objects | `PaLM 2-L` | 76.0 / 56.5 / 60.4 | N/A |
| movie\_recommendation | `PaLM 2-L` | 84.0 / 86.0 / 85.6 | N/A |
| multistep\_arithmetic\_two | `PaLM 2-L` | 52.0 / 49.0 / 49.6 | N/A |
| navigate | `PaLM 2-L` | 76.0 / 67.0 / 68.8 | N/A |
| object\_counting | `PaLM 2-L` | 78.0 / 79.0 / 78.8 | N/A |
| penguins\_in\_a\_table | `PaLM 2-L` | 82.8 / 72.6 / 74.7 | N/A |
| reasoning\_about \_colored\_objects | `PaLM 2-L` | 86.0 / 67.5 / 71.2 | N/A |
| ruin\_names | `PaLM 2-L` | 90.0 / 83.0 / 84.4 | N/A |
| salient\_translation\_error\_detection | `PaLM 2-L` | 62.0 / 65.0 / 64.4 | N/A |
| snarks | `PaLM 2-L` | 85.7 / 70.6 / 73.6 | N/A |
| sports\_understanding | `PaLM 2-L` | 68.0 / 57.5 / 59.6 | N/A |
| temporal\_sequences | `PaLM 2-L` | 100.0 / 99.5 / 99.6 | N/A |
| tracking\_shuffled\_objects\_seven\_objects | `PaLM 2-L` | 44.0 / 34.5 / 36.4 | N/A |
| web\_of\_lies | `PaLM 2-L` | 92.0 / 91.0 / 91.2 | N/A |
| word\_sorting | `PaLM 2-L` | 62.0 / 52.0 / 54.0 | N/A |
| boolean\_expressions | `text-bison` | 84.0 / 78.5 / 79.6 | 80.0 / 78.0 / 78.4 |
| causal\_judgement | `text-bison` | 78.4 / 57.3 / 61.5 | 83.8 / 53.3 / 59.4 |
| date\_understanding | `text-bison` | 52.0 / 45.0 / 46.4 | 64.0 / 52.4 / 54.8 |
| disambiguation\_qa | `text-bison` | 68.0 / 75.5 / 74.0 | 64.0 / 71.5 / 70.0 |
| dyck\_languages | `text-bison` | 100.0 / 99.5 / 99.6 | 100.0 / 100.0 / 100.0 |
| formal\_fallacies | `text-bison` | 70.0 / 54.5 / 57.6 | 74.0 / 53.5 / 57.6 |
| geometric\_shapes | `text-bison` | 28.0 / 15.0 / 17.6 | 48.0 / 28.0 / 32.0 |
| hyperbaton | `text-bison` | 86.0 / 85.0 / 85.2 | 80.0 / 76.5 / 77.2 |
| logical\_deduction\_seven\_objects | `text-bison` | 66.0 / 57.5 / 59.2 | 62.0 / 55.0 / 56.4 |
| movie\_recommendation | `text-bison` | 76.0 / 69.5 / 70.8 | 82.0 / 70.5 / 72.8 |
| multistep\_arithmetic\_two | `text-bison` | 28.0 / 20.5 / 22.0 | 28.0 / 22.5 / 23.6 |
| navigate | `text-bison` | 72.0 / 61.0 / 63.2 | 68.0 / 59.5 / 61.2 |
| object\_counting | `text-bison` | 68.0 / 71.0 / 70.4 | 72.0 / 69.0 / 69.6 |
| penguins\_in\_a\_table | `text-bison` | 65.5 / 59.8 / 61.0 | 79.3 / 53.0 / 58.2 |
| reasoning\_about\_colored\_objects | `text-bison` | 84.0 / 76.5 / 78.0 | 86.0 / 74.0 / 76.4 |
| ruin\_names | `text-bison` | 80.0 / 74.0 / 75.2 | 74.0 / 75.0 / 74.8 |
| salient\_translation\_error\_detection | `text-bison` | 44.0 / 50.5 / 49.2 | 48.0 / 51.0 / 50.4 |
| snarks | `text-bison` | 82.9 / 79.7 / 80.3 | 88.6 / 84.6 / 85.4 |
| sports\_understanding | `text-bison` | 84.0 / 76.5 / 78.0 | 90.0 / 80.0 / 82.0 |
| temporal\_sequences | `text-bison` | 50.0 / 54.5 / 53.6 | 64.0 / 61.5 / 62.0 |
| tracking\_shuffled\_objects\_seven\_objects | `text-bison` | 22.0 / 18.5 / 19.2 | 30.0 / 21.5 / 23.2 |
| web\_of\_lies | `text-bison` | 64.0 / 57.5 / 58.8 | 68.0 / 55.0 / 57.6 |
| word\_sorting | `text-bison` | 26.0 / 19.0 / 20.4 | 32.0 / 25.5 / 26.8 |

#### Table 11
**Caption:** BBH task-wise instructions found by prompt optimization with the \texttt{PaLM 2-L

| Task | Our Instruction |
|---|---|
| boolean\_expressions | An accurate evaluation of logical expressions involves correctly applying Boolean operators, considering the order of operations, and analyzing the truth values of the operands in accordance with Boolean logic principles. |
| causal\_judgement | Understanding causality is critical for accurately assessing cause and effect relationships in various scenarios, leading to well-informed judgments, precise conclusions, and definitive answers to questions about the outcomes involved. |
| date\_understanding | What is the specific date mentioned or required in each given problem or question, taking into account all relevant information, available options, and the provided context? Please provide the accurate answer in the format MM/DD/YYYY. |
| disambiguation\_qa | Accurately analyze and clarify the pronoun-antecedent relationship in the given sentences, identifying the appropriate referent to eliminate any potential confusion or ambiguity and ensure a precise understanding of the intended meaning. |
| dyck\_languages | Solve the sequence by properly closing the parentheses. |
| formal\_fallacies | In determining the deductive validity of arguments based on explicit premises, a meticulous analysis of the logical relationships and implications is essential for definitively establishing their soundness, confirming their validity or invalidity, and ensuring a reliable and robust assessment of the arguments at hand. |
| geometric\_shapes | The SVG path element with the "d" attribute plays a crucial role in web development, allowing for the precise definition and rendering of various shapes on a webpage. |
| hyperbaton | Understanding the correct order of adjectives is crucial for constructing grammatically accurate and coherent sentences that effectively convey the intended meaning in diverse contexts while ensuring clarity, cohesion, and consistency throughout consistently and effortlessly. |
| logical\_deduction \_seven\_objects | By conducting a meticulous analysis of the given information and ensuring logical consistency within each paragraph, we can accurately determine the precise order or ranking of the mentioned objects, allowing us to confidently and consistently identify the correct answer in every presented scenario with utmost precision and confidence. |
| movie\_recommendation | Which movie option from the given choices closely matches the mentioned films in terms of themes, storylines, and characteristics, guaranteeing the highest possible similarity score among them all? |
| multistep\_arithmetic\_two | Evaluate the given mathematical expressions step by step to determine the correct solutions accurately. |
| navigate | Is it possible to determine, with absolute certainty, whether strictly adhering to the given instructions will unfailingly bring you back to the original starting point without any exceptions, errors, or deviations? |
| object\_counting | Determine the total number of objects or entities mentioned in the given list, covering various categories and types, to accurately calculate the overall count. |
| penguins\_in\_a\_table | From the given table, what information can we gather about the mentioned animals and their respective attributes, including names, ages, heights, and weights? |
| reasoning\_about \_colored\_objects | By thoroughly examining the given information, accurately determine the answers for each question by considering the specific characteristics, colors, and positions of the mentioned objects. |
| ruin\_names | Select the most amusing and clever alteration from the options provided for the given artist, movie, or title name, and accurately choose the correct answer to test your wit and creativity. |
| salient\_translation \_error\_detection | Thoroughly examine the given translations from German to English and accurately identify any errors by carefully analyzing the text and selecting the appropriate option with meticulous attention to detail, precision, utmost accuracy, and comprehensive understanding of the language for precise evaluation and categorization. |
| snarks | Which option delivers the most devastatingly sarcastic response, brilliantly exposing the sheer absurdity and leaving absolutely no doubt whatsoever in all the given situations? |
| sports\_understanding | Maintaining the accuracy, reliability, and integrity of sports event representation is essential for upholding the highest standards of credibility, trustworthiness, and overall quality in conveying information, without any compromise, misrepresentation, or distortion, thereby ensuring the factual accuracy of sports journalism. |
| temporal\_sequences | Based on the provided timeline and observed activities, we can accurately determine the possible time range when each individual could have visited their intended destinations and answer questions about their visitation time. |
| tracking\_shuffled\_objects \_seven\_objects | An important point to note is that each person in the group starts with one specific book at the beginning of the semester. |
| web\_of\_lies | Analyzing the consistency and accuracy of statements provided by each person is crucial for determining the truthfulness of individuals in every scenario. |
| word\_sorting | Please sort the given words in alphabetical order: The list of words to be sorted contains - |

#### Table 12
**Caption:** BBH task-wise Q\_begin instructions found by prompt optimization with the \texttt{text-bison

| Task | Our Instruction |
|---|---|
| boolean\_expressions | Group sub-expressions with parentheses to accurately evaluate logical operations: not, and, and finally or. Determine the resulting value as either True or False. |
| causal\_judgement | Consider the intentions and actions of the individuals involved. |
| date\_understanding | Determine the one-day difference in the given date and express it in the format MM/DD/YYYY. |
| disambiguation\_qa | Determine the precise antecedent of the pronoun in the given sentence and select the correct option or state if it is ambiguous. |
| dyck\_languages | Ensure that all opening brackets have a corresponding closing bracket, and that the closing brackets are in the correct order. |
| formal\_fallacies | Thoroughly analyze the explicitly provided premises and determine the deductive validity of the argument based on all necessary conditions, implications, exclusions, and dependencies given. |
| geometric\_shapes | Analyze the given SVG path element carefully and confidently select the correct option from the provided choices to accurately determine the corresponding shape. Pay close attention to the specific path details and confidently make the most suitable choice. |
| hyperbaton | Select the sentence that strictly adheres to the standard order of adjectives: opinion, size, age, shape, color, origin, material, and purpose. Ensure there are no deviations or alterations in the adjective order. Choose the option without any changes. |
| logical\_deduction \_seven\_objects | Analyze the given information to accurately determine the precise order and ranking of the mentioned objects/people, considering their relationships, positions, and any provided comparisons, for a definitive and logical progression with maximum accuracy and efficiency. |
| movie\_recommendation | Based on the movie list provided, carefully consider your preferences and make a well-informed decision. |
| multistep\_arithmetic\_two | First, simplify any expressions within parentheses following the correct order of operations to accurately evaluate the final answer with efficiency and precision. |
| navigate | Always face forward. Take 10 steps forward. Turn left. Take 5 steps forward. Take 3 steps backward. Finally, take 7 steps forward. Turn around and take 1 step forward. Repeat the previous sequence three times. Follow the given path precisely without any deviations. At the end, turn right and take 11 steps forward. If you follow these instructions, will you return to the starting point? |
| - No |
| object\_counting | Determine the total count of mentioned vegetables accurately and state the final count as the answer. |
| penguins\_in\_a\_table | Analyze the given table to accurately determine the required information based on the provided criteria and attributes of the penguins and giraffes. Utilize efficient problem-solving strategies to arrive at the correct answer. |
| reasoning\_about \_colored\_objects | State the color of the object mentioned in the given arrangement with utmost accuracy. |
| ruin\_names | Choose the option that offers the most clever and humorous alteration of the given artist or movie name. Let your creativity shine and select the answer that will undoubtedly bring a smile to your face! Make sure to think outside the box! |
| salient\_translation \_error\_detection | Analyze the translation and accurately identify the specific error type based on the source text, providing the most appropriate corresponding option. |
| snarks | Choose the option that wickedly embodies sarcasm. |
| sports\_understanding | Determine the plausibility of the given statement by evaluating factual accuracy, logical consistency, and contextual relevance, then provide a succinct and well-justified response. |
| temporal\_sequences | Identify the optimal time slot for the individual to engage in the mentioned location/activity considering the given sightings and waking up time, taking into account the opening and closing times of the location and the duration of each event. |
| tracking\_shuffled\_objects \_seven\_objects | Pay attention to the given information and track the swaps/exchanges carefully to accurately determine the final possession/position/outcome for the specified individual. |
| web\_of\_lies | To determine the truthfulness of the last person mentioned, analyze the consistency of each statement and count the number of individuals accusing the previous person of lying. If the count of accusers is even, that person tells the truth; if it is odd, that person lies. |
| word\_sorting | Alphabetically sort the given list of words, ensuring all words are included and in ascending order. |

#### Table 13
**Caption:** BBH task-wise Q\_end instructions found by prompt optimization with the \texttt{text-bison

| Task | Our Instruction |
|---|---|
| boolean\_expressions | Accurately use order of operations and parentheses to evaluate logical expressions and determine truth values efficiently. |
| causal\_judgement | Consider all relevant factors, prioritize overall well-being and ethical considerations, make well-informed decisions while foreseeing potential consequences efficiently, and consistently strive for optimal outcomes with empathy and adaptability in a thoughtful and comprehensive manner. |
| date\_understanding | Subtract the specified number of days from the given date and format the outcome as MM/DD/YYYY to accurately determine the desired result in an efficient manner. |
| disambiguation\_qa | Clearly identify and select the unambiguous antecedent for the pronoun or designate it as "Ambiguous" if it is unclear. |
| dyck\_languages | Add the missing closing parentheses. |
| formal\_fallacies | Determine the deductive validity of the argument presented based on the explicitly stated premises and reach a definitive conclusion. |
| geometric\_shapes | Analyzing the given SVG path element, accurately determine its shape by closely examining its curves and coordinates, then select the correct option. |
| hyperbaton | Choose the option with the correct adjective order in each sentence, prioritizing specific attributes like size, color, and origin. Place the most specific adjective before the more general ones for precise and standardized ordering across all examples. Ensure accurate alignment of the adjectives based on their respective attributes for consistent and standardized ordering. |
| logical\_deduction \_seven\_objects | Determine the precise order of the given objects/participants based on the provided information and establish the final ranking accurately, considering all relevant factors, while maintaining logical consistency with maximum efficiency. |
| movie\_recommendation | Choose the most similar option from the choices provided that closely aligns with the given movies' themes, genres, and impact for the most accurate recommendation possible. Make your selection wisely. |
| multistep\_arithmetic\_two | Carefully follow the order of operations to precisely simplify the expressions within parentheses and efficiently find the accurate final answer. |
| navigate | Always face forward. Take 10 steps forward. Turn right and walk for 5 steps. Then, make a left turn and continue for 9 steps. Proceed by walking 6 steps backward. Finally, turn around and take 200 steps. Accurately track your movements, diligently adhere to the given path, and ensure to return to the starting point without any deviations or obstacles. |
| object\_counting | Determine the total count of items mentioned, including all listed items, using an efficient and concise method. State the final count as your answer. |
| penguins\_in\_a\_table | Identify the animal with the maximum measurement (weight, age, or height) in the table and state its name and species. |
| reasoning\_about \_colored\_objects | Determine the color of each item in the given scenario and select the correct color option from the provided choices for accurate responses, ensuring utmost precision and completeness. |
| ruin\_names | Choose the option that creatively and hilariously transforms the given artist or movie name. |
| salient\_translation \_error\_detection | Carefully analyze the translations and select the most suitable option from the given choices to rectify the specific error category, ensuring complete precision, accuracy, and faithful representation of the intended meaning, while considering all relevant information in the source text. |
| snarks | Choose the option that cleverly employs sarcasm to defy all expectations and leave everyone utterly dumbfounded, questioning the very essence of their own perception. |
| sports\_understanding | Evaluate the plausibility of each given statement and provide a well-supported justification based on logical reasoning, contextual understanding, and relevant evidence to arrive at a definitive and conclusive answer. |
| temporal\_sequences | Identify the possible time slot for the desired activity based on the given information and sightings, then select the correct option. |
| tracking\_shuffled\_objects \_seven\_objects | Thoroughly analyze the given scenarios, systematically consider all available information, and confidently determine the final outcome with exceptional precision and optimal efficiency, while maintaining a strategic and logical approach throughout the process. |
| web\_of\_lies | Examine each person's statements meticulously to accurately determine the truth and confidently identify who is telling the truth, enabling you to effectively solve the given problem. |
| word\_sorting | Sort the given words alphabetically using spaces as separators while maintaining their original order and including all words. |

#### Table 14
**Caption:** Accuracies on BBH tasks with the \texttt{PaLM 2-L

| Task | Scorer | Our Acc | ``Let's solve the problem.'' Acc |
|---|---|---|---|
|  |  | training / test / overall | training / test / overall |
| boolean\_expressions | `PaLM 2-L` | 98.0 / 89.5 / 91.2 | 78.0 / 69.0 / 70.8 |
| causal\_judgement | `PaLM 2-L` | 83.8 / 58.7 / 63.6 | 62.0 / 61.3 / 61.5 |
| date\_understanding | `PaLM 2-L` | 90.0 / 82.0 / 83.6 | 74.0 / 71.0 / 71.6 |
| disambiguation\_qa | `PaLM 2-L` | 78.0 / 68.0 / 70.0 | 52.0 / 54.5 / 54.0 |
| dyck\_languages | `PaLM 2-L` | 100.0 / 100.0 / 100.0 | 94.0 / 97.0 / 96.4 |
| formal\_fallacies | `PaLM 2-L` | 84.0 / 62.0 / 66.4 | 68.0 / 54.0 / 56.8 |
| geometric\_shapes | `PaLM 2-L` | 62.0 / 42.5 / 46.4 | 30.0 / 22.0 / 23.6 |
| hyperbaton | `PaLM 2-L` | 94.0 / 91.5 / 92.0 | 72.0 / 77.0 / 76.0 |
| logical\_deduction\_seven\_objects | `PaLM 2-L` | 66.0 / 53.0 / 55.6 | 38.0 / 36.5 / 36.8 |
| movie\_recommendation | `PaLM 2-L` | 88.0 / 88.0 / 88.0 | 66.0 / 76.0 / 74.0 |
| multistep\_arithmetic\_two | `PaLM 2-L` | 66.0 / 55.0 / 57.2 | 30.0 / 22.0 / 23.6 |
| navigate | `PaLM 2-L` | 76.0 / 67.0 / 68.8 | 54.0 / 63.5 / 61.6 |
| object\_counting | `PaLM 2-L` | 96.0 / 92.5 / 93.2 | 58.0 / 58.0 / 58.0 |
| penguins\_in\_a\_table | `PaLM 2-L` | 86.2 / 70.9 / 74.0 | 69.0 / 72.6 / 71.9 |
| reasoning\_about \_colored\_objects | `PaLM 2-L` | 88.0 / 69.0 / 72.8 | 78.0 / 69.5 / 71.2 |
| ruin\_names | `PaLM 2-L` | 92.0 / 85.5 / 86.8 | 76.0 / 79.5 / 80.8 |
| salient\_translation\_error\_detection | `PaLM 2-L` | 66.0 / 67.5 / 67.2 | 30.0 / 35.5 / 34.4 |
| snarks | `PaLM 2-L` | 88.6 / 76.9 / 79.2 | 80.0 / 70.6 / 72.5 |
| sports\_understanding | `PaLM 2-L` | 72.0 / 63.5 / 65.2 | 60.0 / 50.5 / 52.4 |
| temporal\_sequences | `PaLM 2-L` | 100.0 / 99.5 / 99.6 | 96.0 / 92.5 / 93.2 |
| tracking\_shuffled\_objects\_seven\_objects | `PaLM 2-L` | 56.0 / 63.5 / 62.0 | 42.0 / 51.5 / 49.6 |
| web\_of\_lies | `PaLM 2-L` | 56.0 / 58.5 / 58.0 | 0.0 / 4.0 / 3.2 |
| word\_sorting | `PaLM 2-L` | 52.0 / 44.5 / 46.0 | 18.0 / 20.5 / 20.0 |

#### Table 15
**Caption:** BBH task-wise Q\_begin instructions found by prompt optimization with the \texttt{PaLM 2-L

| Task | Our Instruction |
|---|---|
| boolean\_expressions | Let's accurately assess the given conditions and determine their corresponding Boolean values. |
| causal\_judgement | Let's conduct a meticulous evaluation of the given scenarios, accurately determine the causal relationships, and provide definitive answers through comprehensive analysis, ensuring a precise understanding of causation and a thorough determination of events in each situation. |
| date\_understanding | Let's accurately determine the correct date based on the given information and select the corresponding option in the standard MM/DD/YYYY format with utmost precision and reliability, ensuring the most definitive and reliable solution possible for accurate representation in all scenarios without any room for ambiguity, error, or confusion, and providing the highest level of accuracy and reliability. |
| disambiguation\_qa | Let's thoroughly analyze the given sentences to accurately determine the unambiguous antecedents of the pronouns used, ensuring clear understanding, effective communication, and leaving no room for any confusion or ambiguity. |
| dyck\_languages | Let's find the correct closing parentheses and brackets for the given sequences. |
| formal\_fallacies | Let's thoroughly analyze the explicitly stated premises and draw definitive conclusions to accurately determine the deductive validity of the arguments provided in each question, employing precise and logical reasoning in our assessments for unwavering confidence in our determinations. |
| geometric\_shapes | Let's accurately determine the shape represented by the given SVG path element by carefully analyzing its path data and considering all available options for a precise identification. |
| hyperbaton | Let's quickly identify the correct adjective order. |
| logical\_deduction \_seven\_objects | Let's methodically analyze the given information, employ logical reasoning, thoroughly evaluate all relevant details, and accurately determine the solutions for each problem by considering all provided options comprehensively and strategically, ensuring an efficient and effective approach towards arriving at the correct answers. |
| movie\_recommendation | Let's uncover the perfect movie recommendation from the options provided, ensuring an exceptional cinematic experience together as we select the most captivating and satisfying choice that will keep us thoroughly engaged and immersed until the very end. |
| multistep\_arithmetic\_two | Let's tackle the following calculations. |
| navigate | Let's accurately and efficiently determine the correct solution for each given scenario, ensuring the highest level of precision, reliability, and consistency throughout. |
| object\_counting | Let's determine the total count of various items/objects/ingredients/animals mentioned in order to accurately and efficiently find the answer. |
| penguins\_in\_a\_table | Let's analyze the given information and determine the correct answer. |
| reasoning\_about \_colored\_objects | Let's systematically analyze the given information and carefully evaluate each answer choice to confidently determine the accurate and optimal solutions, considering all available options and specific details provided in each question for precise and concise responses, ensuring complete accuracy and clarity in our answers. |
| ruin\_names | Prepare to have a side-splittingly funny time as we uncover the most clever and hilarious alternatives for these artist or movie names, challenging your wit to guess the correct one with a burst of creativity, humor, and imaginative twists! |
| salient\_translation \_error\_detection | Let's meticulously analyze the provided translations, accurately identifying any errors or discrepancies, and conduct a comprehensive evaluation to ensure the highest level of translation quality and fidelity. By considering contextual nuances, cultural references, linguistic conventions, potential factual errors, and any dropped content, our ultimate aim is to achieve precise and thorough assessments for optimal translation accuracy and adherence to the source text. |
| snarks | Let's expertly determine the sarcastic statement among the given options and confidently provide the definitive answer without any room for doubt or confusion, ensuring absolute precision, clarity, and unwavering expertise in our response, while carefully analyzing the context, tone, and intention behind each statement to achieve unrivaled accuracy and unwavering confidence. |
| sports\_understanding | Let's find the accurate information. |
| temporal\_sequences | The flawless approach |
| tracking\_shuffled\_objects \_seven\_objects | By meticulously analyzing the given scenarios and accurately determining the final outcomes through a series of trades, swaps, and exchanges among the individuals involved, let's ascertain the conclusive results. |
| web\_of\_lies | Let's scrutinize each statement provided to accurately determine the truth-teller and uncover the veracity behind their words with unwavering analysis. |
| word\_sorting | Employing efficient and precise measures, sort the given list of words in alphabetical order to provide an optimal solution for any sorting problem, ensuring maximum performance and effectiveness. |



![ablation_meta_prompt_instruction_ordering_gsm8k.png](./images/ablation_meta_prompt_instruction_ordering_gsm8k.png)
*(Fig. 3) メタプロンプト内の過去指示スコアの順序に関するAblation。スコアを大きい順から小さい順（昇順）に並べた方がLLMがうまくコンテキストを捉え、最終的なタスク精度が高いことが確認された。*

![overfitting_analysis_bbh_snarks.png](./images/overfitting_analysis_bbh_snarks.png)
*(Fig. 4) 過学習（Overfitting）の分析。OPROで訓練データに適合しても、検証（Validation）やテストデータへの汎化性能がほぼパラレルに向上しており、極端な汎化性能の低下は見られない。*

![compare_with_evoprompt_gsm8k.png](./images/compare_with_evoprompt_gsm8k.png)
*(Fig. 5) 先行研究および他のプロンプト変異アルゴリズム(EvoPromptのGA / DE）との比較。OPROはこのように複雑な変異指示を与えずとも長期間の履歴を活用することから、最も安定的かつ優位にスコアを上昇させている。*
