# Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

## 背景
LLM（大規模言語モデル）の推論能力を引き出す上で、Chain-of-Thought（CoT）などのプロンプト戦略は極めて有効です。しかし、これらのプロンプトは人間が手作業で設計（ハンドクラフト）しており、ドメインごとの最適なプロンプト設計には限界がありました。APE（Automatic Prompt Engineer）のようにプロンプトを自動生成・評価する先行研究は存在しますが、数世代の進化で品質が頭打ち（Diminishing Returns）になる課題がありました。本論文では、プロンプトの更新自体をLLMに行わせ、さらに「プロンプトを更新するためのプロンプト（変異プロンプト）」そのものも自己参照的に進化させることで、継続的かつドメインに適応した自己改善を実現する汎用フレームワーク「Promptbreeder（PB）」を提案しています。

## 手法

#### 図1: Promptbreederの全体像
![Promptbreeder Overview](./images/overview.png)
（Figure 1に該当）
初期のタスクプロンプト群、変異プロンプト、思考スタイル（Thinking styles）を基に、バイナリートーナメント方式で遺伝的アルゴリズムを回します。ハイパーミューテーションにより変異プロンプトも進化するため、LLMが「どうすればより良い推論指示を出せるか」まで自身で探索できます。
---

Promptbreederは、LLMの重みを一切更新せず、自然言語（プロンプト）を基盤にして**自己参照的な進化アルゴリズム（遺伝的アルゴリズム: GA）**を実行します。

一般的なGAとは異なり、Promptbreederにおける「進化の単位（個体）」は単一のプロンプトではなく、以下の要素が**ペア（セット）**になったものです。
*   **タスクプロンプト ($P$)**: 実際に問題を解くための指示文
*   **変異プロンプト ($M$)**: 上記の$P$をどのように改善・変異させるかを指示する文章

これらがひとつのセットとして管理され、バイナリートーナメント方式を用いた適応度評価（推論の正答率）を勝ち抜いた個体が、自身の持つ $M$ を使って自身の $P$ （または $M$ 自身）を書き換えて次世代へと進化させます。「どうやって問題を解くか($P$)」という形質だけでなく、「どうやって自分自身を改善するか($M$)」という進化の手段そのものも一緒に遺伝し、血統として最適化されていく点が特徴です。

数式で表すと、関連する登場概念とその更新は次のように定義されます。

*   **タスクプロンプト ($P$)**: 個体が持つ具体的な推論指示文。
*   **変異プロンプト ($M$)**: $P$をどのように改善・変異させるかを指示する文章。
*   **上位プロンプト ($H$)**: 変異プロンプト($M$)自体をさらに進化させる際に用いる、システムに組み込まれた固定のハイパープロンプト。

更新の際には、5系統・全9種類の変異オペレータをランダムに適用し、プロンプトの多様性を維持しながら最適化を行います。それぞれが実際に「どのような文字列」としてLLMに入力されるのか、代表的な仕組みをプロンプトレベルで解説します。

### Mutation手法の詳細（プロンプトレベルの解説）

> **【補足：一般的なGAと本論文におけるMutationの枠組みの差】**
> 一般的な遺伝的アルゴリズム（GA）では、「突然変異（Mutation: 単一個体からのランダムな変化）」と「交叉（Crossover: 複数個体の特徴を混ぜる）」は別々のアルゴリズム処理として明確に区別されます。
> しかし、Promptbreederの世界では、変異であっても交叉であっても、どちらも**「LLMに対するプロンプト（自然言語）のテキスト操作」でしかない**という共通点があります。そのため本論文では、Crossoverも含めて「プロンプトの文字列を変化させて新世代を作るためのオペレータ」をすべて一括りにし、広義の**「Mutation Operators」**として定義・分類しています。

#### 1. Direct Mutation（タスクプロンプトの直接変異）
現在のタスクプロンプト $P$ を直接書き換える、またはゼロから生成するアプローチです。
*   **Zero-order Prompt Generation**:
    *   **入力例**: `Here is a task description: [問題の説明]. Please write a good instruction for this task: `
    *   既存のプロンプトを使わず、問題文だけから新しい $P'$ を生成させます。
*   **First-order Prompt Generation**:
    *   **概要**: 変異プロンプト $M$ の指示に従って $P$ を直接書き換えます（式 $P' = \text{LLM}(M + P)$ に該当）。
    *   **文字列結合の具体例**:
        * $M$: `Simplify this instruction as if you are teaching it to a child:`
        * $P$: `Solve the math word problem by first converting the words into equations using algebraic notation...`
        これらを改行で文字列として繋げた以下のテキストそのものが、LLMへの入力となります。
        ```text
        Simplify this instruction as if you are teaching it to a child:
        Solve the math word problem by first converting the words into equations using algebraic notation...
        ```
*   **Lineage Based Mutation**:
    *   **入力例**: `Here is a history of instructions that have been getting better: 1. [P_old] 2. [P_recent] 3. [P_current]. What is the next logical step to improve this instruction? 4.`
    *   進化の履歴（徐々に良くなっているプロンプトのリスト）を与え、さらに良くなるような次の一手を推論で考えさせます。

#### 2. Estimation of Distribution Mutation (EDA)
集団内の複数の優秀なプロンプトを参考に、新しいプロンプトを生成します。
*   **EDA Rank / EDA Index Mutation**:
    *   **入力例**: `Here are some good instructions for this task, ranked from worst to best: \n 1. [P_1] \n 2. [P_2] \n 3. [P_3] \n Now, please write an even better instruction: 4.`
    *   多様性フィルタや適応度で選ばれたプロンプト群をリストとして与え、「その続きのより良いプロンプト」をLLMの文脈補完能力（In-Context Learning）を使って生成させます。

#### 3. Hyper-Mutation（変異プロンプト自体の進化）
「プロンプトの改善方法（$M$）」自体を進化させます（自己参照的な中核機能）。
*   **Zero-order Hyper-Mutation**:
    *   **入力例**: `Please generate a useful mutation instruction that can be used to improve prompts for the task of [問題の説明].`
    *   上位のメタプロンプト($H_0$)を用いて、新しい変異プロンプト $M'$ をゼロから生成させます。
*   **First-order Hyper-Mutation**:
    *   **入力例**: `[上位プロンプト H_1] \n [現在の変異プロンプト M]`
    *   （例）`Please improve this mutation instruction by making it shorter: \n "Simplify this instruction as if you are teaching it to a child"`
    *   既存の変異プロンプト $M$ を、より効果的な変異プロンプト $M'$ に書き換えさせます。

#### 4. Lamarckian Mutation（ラマルク的進化）
獲得形質が遺伝する（成功した推論プロセスから指示を逆算する）仕組みです。
*   **Working-out to Prompt**:
    *   **入力例**: `Here is a problem: [Q]. Here is a successful step-by-step solution: [推論プロセス W]. \n Based on this successful thinking process, what general instruction ($P'$) would lead someone to solve similar problems in the same way?`
    *   実際に正解に至った**途中計算や推論のプロセス文（Working-out）**を読み込ませ、「どういう指示を与えればこういう解き方になるか」をリバースエンジニアリングして新しいタスクプロンプト $P'$ を抽出します。

#### 5. Prompt Crossover and Context Shuffling
プロンプト同士や、付随するコンテキスト（Few-shot事例）を操作します。
*   **Prompt Crossover (交叉)**:
    *   **入力例**: `Instruction 1: [メイン親の P]. \n Instruction 2: [サブ親の P]. \n Please combine the best aspects of both instructions into a new, single instruction: `
    *   メインの親個体と、集団から抽出した別の親個体の「タスクプロンプト($P$)」同士の長所を組み合わせた新しい $P'$ を生成させます。
    *   **$M$の継承ルール**: この際、変異プロンプト($M$)は交ざりません。複数の要素を一度に混ぜると進化の方向性がブレてしまうため、新しい子は「メインの親が持っていた $M$」をそのまま継承します。
*   **Context Shuffling**:
    *   プロンプトテキスト $(P)$ 自体は変更せず、モデルへの実際の入力プロンプトに含める Few-shot の正解事例（Context例題）の抽出や並び順をランダムに入れ替え、進化の多様性の喪失を防ぎます。

## 結果

### 図表に基づく考察



#### 図2: 進化の過程
![Evolution Progression](./images/evolution_progression.png)
（Figure に該当、論文内の進化の推移図）
あるタスク（Word in Context等）において、トレーニングデータ上での評価（青点）と集団の平均適応度（赤線）が、数千回の評価を通じて継続的に上昇している様子がわかります。APEと異なり、自己参照的な変異を挟むことで最適解の探索が頭打ちにならず、右肩上がりの進化を維持できています。

#### 図3: 自己参照オペレータの役割とAblation
![Ablation Matrix](./images/prompt_evolution_ablation_matrix.png)
（または ablation_matrix.png。自己参照戦略の比較）
タスクプロンプトのみを進化させる手法と比較して、変異プロンプトも同時に進化させること（Hyper Mutation）が精度向上において重要であることが確認できました。

---

### 表データと詳細考察

#### Table 1: 推論ベンチマークでの比較
| | Method | LLM | MultiArith* | GSM8K | AddSub* | AQuA-RAT | SingleEq* | SVAMP* | CSQA | SQA |
|---|---|---|---|---|---|---|---|---|---|---|
| Zero-shot | CoT | text-davinci-003 | (83.8) | (56.4) | (85.3) | (38.9) | (88.1) | (69.9) | (65.2) | (63.8) |
| | PoT | text-davinci-003 | (92.2) | (57.0) | (85.1) | (43.9) | (91.7) | (70.8) | -- | -- |
| | PS | text-davinci-003 | (87.2) | (58.2) | (88.1) | (42.5) | (89.2) | (72.0) | -- | -- |
| | PS+ | text-davinci-003 | (91.8) | (59.3) | (**92.2**) | (46.0) | (94.7) | (75.7) | (71.9) | (65.4) |
| | PS | PaLM 2-L | 97.7 | 59.0 | 72.4 | 40.2 | 90.6 | 83.8 | 77.9 | 50.0 |
| | PS+ | PaLM 2-L | 92.5 | 60.5 | 74.4 | 39.4 | 94.7 | 86.3 | 73.3 | 50.1 |
| | APE | PaLM 2-L | 95.8 | 77.9 | 72.2 | 45.7 | 82.2 | 73.0 | 67.3 | 38.4 |
| | OPRO | PaLM 2-L | -- | 80.2 | -- | -- | -- | -- | -- | -- |
| | PB (ours) | PaLM 2-L | **99.7** | **83.9** | 87.8 | **62.2** | **96.4** | **90.2** | **85.4** | **71.8** |
| Few-shot | Manual-CoT | text-davinci-003 | (93.6) | (58.4) | (**91.6**) | (48.4) | (93.5) | (80.3) | (78.3) | (71.2) |
| | Auto-CoT | text-davinci-003 | (95.5) | (57.1) | (90.8) | (41.7) | (92.1) | (78.1) | -- | -- |
| | PB (ours) | PaLM 2-L | **100.0** | **83.5** | 87.1 | **64.6** | **98.9** | **93.7** | **85.9** | **80.2** |

**考察**: Zero-shotおよびFew-shotの両方で、Promptbreeder (PB) が最先端のプロンプト戦略（PS+やOPRO）を凌駕しています。特にGSM8KやAQuA-RATのような高度な推論が求められるタスクで大きな精度向上が見られます。

#### Table 2: 初期プロンプト抽出例（GSM8K）
| Index | Initially Evolved Prompt |
|---|---|
| 0 | Draw a picture of the situation being described in the math word problem |
| 1 | Solve the math word problem by first converting the words into equations using algebraic notation. Then solve the equations for the unknown variables, and express the answer as an arabic numeral. |
| 2 | Solve the math word problem by breaking the problem into smaller, more manageable parts. Give your answer as an arabic numeral. |
| 3 | Generate the answer to a word problem and write it as a number. |
| 4 | Collaborative Problem Solving: Work with other people to solve the problem, and give your answer as an arabic numeral. |
| 5 | Solve the problem by explaining why systemic or structural issues would not be the cause of the issue. |
| 6 | Draw a diagram representing the problem. |
| 7 | Solve the math word problem, giving your answer as an equation that can be evaluated. |
| 8 | Make a list of ideas for solving this problem, and apply them one by one to the problem to see if any progress can be made. |
| 9 | Do NOT use words to write your answer. |

**考察**: 初期化段階において、汎用的な「思考スタイル」と「変異プロンプト」を組み合わせることで、「絵を描く」「方程式に変換する」「リストを作る」など、非常に多様で発散的なプロンプトの種が生成されることが示されています。

#### Table 3: 算術タスクで比較されたベースラインプロンプト
| Model | Prompt |
|---|---|
| CoT | "Let’s think step by step." |
| PS | "Let’s first understand the problem and devise a plan to solve the problem. Then, let’s carry out the plan and solve the problem step by step." |
| PS+ | "Let’s first understand the problem, extract relevant variables and their corresponding numerals, and make a plan. Then, let’s carry out the plan, calculate intermediate variables (pay attention to correct numerical calculation and commonsense), solve the problem step by step, and show the answer." |
| APE | "Let’s work this out in a step by step way to be sure we have the right answer." |
| OPRO | "Take a deep breath and work on this problem step-by-step." |

**考察**: 従来手法では、手作業で設計された静的なテキスト（またはシンプルな生成プロンプトのみ）に依存しています。

#### Table 4: PBによって進化したタスクごとの二段階プロンプト
| Task | Prompt 1 | Prompt 2 |
|---|---|---|
| ADDSUB | Solving word problems involves carefully reading the prompt and deciding on the appropriate operations to solve the problem. | You know what's cool? A million dollars. |
| AQUA | Do a simple computation. | MATH WORD PROBLEM CHOICE (A) (B) (C) (D) or (E). |
| GSM8K | SOLUTION" | |
| MULTIARITH | Solve the math word problem, giving your answer as an arabic numeral. Let's think step by step. | Solve the math word problem, giving your answer as an arabic numeral. Explain the problem to someone else as a way to simplify it. What is the core issue or problem that needs to be addressed? |
| SINGLEEQ | solve the math word problem, which might contain unnecessary information, by isolating the essential facts. Then set up the equations, and give your answer as an arabic numeral. | Solve the math problem. |
| SVAMP | visualise solve number | (Solve the math word problem. Therefore, the answer (arabic numerals) is \_\_\_\_\_) |
| SQA | OUTPUT MUTANT = Work out an answer to the commonsense reasoning question above. If there are multiple people or perspectives involved, try considering them one at a time. | "Work out an answer to the commonsense reasoning question above. If there are multiple people or perspectives involved, try considering them one at a time. Next, answer yes or no." |
| CSQA | Solve the multiple choice math word problem, choosing (A),(B),(C),(D) or (E). | Solve the multiple choice math word problem. Can you recall any similar problems you've done and how you solved them? |

**考察**: 最終的に進化・獲得されたプロンプトは、人間が手作業で考えつくものとは異なる非常に独自で直感に反するもの（例えばGSM8Kの`SOLUTION"`だけ、やADDSUBの`You know what's cool? A million dollars.`）も含まれますが、対象モデル（PaLM 2-Lなど）の内部空間において局所的に最適なトリガーになっていることが示唆されています。

#### Table 5: GS8Kで優秀だった変異プロンプト（Mutation prompts）のスコア
| Instruction | Score |
|---|---|
| Please summarise and improve the following instruction | 24.13% |
| Simplify this instruction by breaking it up into separate sentences. The instruction should be simple and easily understandable | 17.8% |
| As a really good teacher, explain the instruction, as if you are explaining it to a child | 16.2% |
| Simplify this instruction as if you are teaching it to a child | 10.0% |
| 100 hints | 4.3% |
| A list of 100 hints | 3.4% |

**考察**: 「要約して改善する」「子供に教えるようにシンプルにする」などのメタな指示（変異プロンプト）が最も効率よくタスクプロンプトを進化させており、自己参照的改善の有効性を裏付けています。

#### Table 6: 変異オペレータごとの有効割合（親より優れた子を生成した割合）
| Mutation Operator | Percentage |
|---|---|
| Zero-order Hyper-Mutation | 42% |
| Lineage Based Mutation | 26% |
| First-order Hyper-Mutation | 23% |
| EDA Rank and Index Mutation | 12.7% |
| Direct Mutation | 12% |
| EDA Mutation | 10.7% |
| Lamarckian Mutation | 6.3% |

**考察**: ここで特筆すべきは、変異プロンプト自体を変更する`Zero-order Hyper-Mutation`や`First-order Hyper-Mutation`が非常に高い割合で適応度を改善している点です。これにより、単にプロンプトをランダムに変えるのではなく、「良い変異のさせ方」自体が進化アルゴリズム内で重要な探索ドライバとなっていることがわかります。

#### Table 7: Instruction Inductionタスク群でのAPEとの比較
| Dataset | Zero-shot APE | Few-shot APE | PE using APE prompts | Few-shot PE |
|---|---|---|---|---|
| First Letter | 100 | 100 | 1 | **100** |
| Second Letter | 87 | 69 | 27 | **95** |
| List Letters | 99 | 100 | 0 | 99 |
| Starting With | 68 | 69 | 6 | **71** |
| Pluralization | 100 | 100 | 23 | **100** |
| Passivization | 100 | 100 | 100 | **100** |
| Negation | 83 | 90 | 16 | **90** |
| Antonyms | 83 | 86 | 80 | **87** |
| Synonyms | 22 | 14 | 16 | **43** |
| Membership | 66 | 79 | 96 | **100** |
| Rhymes | 100 | 61 | 90 | **100** |
| Larger Animal | 97 | 97 | 27 | **97** |
| Cause Selection | 84 | 100 | 66 | **100** |
| Common Concept | 27 | 32 | 0 | 0 |
| Formality | 65 | 70 | 10 | 7 |
| Sum | 100 | 100 | 72 | **100** |
| Difference | 100 | 100 | 98 | **100** |
| Number to Word | 100 | 100 | 66 | **100** |
| Translation English-German | 82 | 86 | 46 | **87** |
| Translation English-Spanish | 86 | 91 | 80 | **91** |
| Translation English-French | 78 | 90 | 68 | **91** |
| Sentiment Analysis | 94 | 93 | 33 | **93** |
| Sentence Similarity | 36 | 43 | 53 | **56** |
| Word in Context | 62 | 63 | 6 | **65** |

**考察**: 表形式・言語理解などの24のInstruction Inductionタスクにおいて、Prompt Evolution（Promptbreeder）はAPE（Zero/Few-shotともに）を21タスクで上回るか同等の成果（100%）を達成しています。「PE using APE prompts」（APEの手法を模倣した変異）では全く進化が進まず精度が低いタスク（List LettersやCommon Concept）がありますが、多様なMutation手法を持つPB（Few-shot PE）では劇的な改善が見られ、進化のメカニズム自体の堅牢性が示されています。

## chokosenlovetiの考察

### 新規性
Promptbreeder（PB）の最大の新規性は、**「タスクを解くためのプロンプト（$P$）」だけでなく、「プロンプトを改善するための指示（$M$）」までも同時に進化させる自己参照的アプローチ（Hyper-Mutation）**を導入した点にあります。

先行研究である **APE (Automatic Prompt Engineer)** との決定的な差異は以下の2点です。

1. **最適化（進化）の範囲**
   - **APE**: 「良いプロンプトを生成して」等の**人間が用意した固定のメタプロンプト**を用いて、タスクプロンプトの候補を多数生成・評価します。探索・進化の対象は「タスクプロンプトのみ」です。
   - **Promptbreeder**: タスクプロンプトの最適化に加え、「どのようにプロンプトを改善すべきか」という**変異プロンプト（$M$）の文章自体も進化の対象**とします。

2. **探索の限界（Diminishing Returns）の突破**
   - **APE**: 「プロンプトの改善手法」が固定されているため、数イテレーション探索を続けると局所最適解に陥り、すぐに性能の向上が頭打ちになります。
   - **Promptbreeder**: 「要約して」「子供に教えるようにシンプルにして」など、プロンプトの改善アプローチ自体が多様に生み出され、淘汰されます。「プロンプトの探し方」自体が進化するため、探索空間が動的に拡張し続け、右肩上がりのオープンエンドな自己改善を持続できます。

要約すると、APEが「**固定されたルールで、優れたプロンプトだけを探すシステム**」であるのに対し、Promptbreederは「**プロンプトを探索しつつ、“より良いプロンプトの探し方”そのものも自ら学習して改善していくシステム**」である点が、LLMの推論能力拡張において画期的な新規性となっています。
