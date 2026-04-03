# Large Language Models Are Human-Level Prompt Engineers (APE)

## 背景
大規模言語モデル（LLMs）は、自然言語の指示（プロンプト）を与えることで様々なタスクを汎用的に解くことができるが、その性能は与えられるプロンプトの質に大きく依存する。これまでは人間が手作業で試行錯誤しながらプロンプトを設計（プロンプトエンジニアリング）していたが、この探索空間は無限であり、どのプロンプトがモデルに最適かは人間には直感的に分かりにくいという課題があった。そこで本研究では、プロンプトの手動設計を脱却し、自然言語の指示を一つの「プログラム」と見立てて、LLM自身に最適な指示を自動生成・選択させるフレームワーク「Automatic Prompt Engineer (APE)」を提案している。

## 手法
APEは、自然言語によるプログラム合成をブラックボックス最適化問題として定式化し、LLMを「プロンプトの提案（Generation）」と「評価（Scoring）」の両方に活用する。具体的には以下のステップを踏む。

### 1. 提案 (Proposal)
少数の入出力のデモンストレーション $\mathcal{D}_{\text{train}} = \{(X, Y)\}$ をLLMに与え、背後にある共通の「指示（プロンプト候補 $U$）」を推測・生成させる。

**【具体例：Forward Mode の場合】**
翻訳や要約のような標準的な言語モデル（GPTなど）を用い、以下のようなテンプレート（メタプロンプト）を用いてLLMに指示文の続きを推測させる。

> **入力プロンプト例 (LLMへの問いかけ):**
> I gave a friend an instruction and five inputs. The friend read the instruction and wrote an output for every one of the inputs.
> Here are the input-output pairs:
> Input: cat  Output: c
> Input: dog  Output: d
> Input: bird  Output: b
> The instruction was "

> **LLMの生成出力例 (生成されるプロンプト候補 $U$):**
> Output 1: Extract the first letter of the given word."
> Output 2: Write the first character of each word."

**【具体例：Reverse Mode の場合】**
T5やInsertGPTのような穴埋め（Infilling）モデルを用い、前後の文脈から欠落した「指示」部分を直接推測させる。

> **入力プロンプト例 (穴埋め推論):**
> [Instruction: [MASK]]
> Input: cat  Output: c
> Input: dog  Output: d


### 2. 評価 (Scoring)
提案フェーズで生成された複数のプロンプト候補（例: $U_1, U_2, \dots$）を利用し、別のターゲットモデルでゼロショット推論を実行。その出力結果と正解デモンストレーションデータの合致度を評価関数 $f(U, X, Y)$ によってスコアリングする。

**【具体例：Execution Accuracy による評価】**
候補 $U_1$：「Extract the first letter of the given word.」が生成されたとする。これをテスト用の新しい入力($X_{\text{test}}$)に適用する。

> **ターゲットモデルへのプロンプト入力:**
> Extract the first letter of the given word.
> Input: apple
> Output:

> **ターゲットモデルの出力:**
> a

もしデータセット上の正解($Y_{\text{test}}$) が `a` であれば、**合致（スコア 1.0）**となる。これを複数データに対して行い、期待値（平均スコア）を算出する。

- 計算コスト削減の工夫として、少数のデータセットで有望な候補を絞り込む「適応的フィルタリング（Adaptive Filtering）」が採用されている。
- 最適なプロンプトは以下のように定式化される:
$$ U^{\star} = \arg\max_{U} \mathbb{E}_{(X, Y)}[f(U, X, Y)] $$


### 3. 反復的探索 (Iterative Search)
最初の提案フェーズで生成されたプロンプト群の中に、十分にスコアの高い（理想的な）ものが見つからない場合に行うステップです。ここでは、広大な「プロンプトの組み合わせ空間」を効率よく探すために**モンテカルロ探索（確率的な探索手法）**が用いられます。

#### モンテカルロ探索によるプロンプト改善のイメージ
「モンテカルロ探索」というと難しく聞こえますが、ここでは**「現時点で成績の良かったプロンプトを親にして、周辺の似た言い回しを確率的に（ランダム性を交えて）たくさん作らせ、さらに良いものがないか探す」**というアプローチを指しています。

具体的な流れは以下の通りです。

1. **有望なプロンプトのサンプリング:**
   前段の「2. 評価」でスコアが高かったプロンプト（例: `Extract the first letter of the given word.`）をベースとして確率的に選び出します。（成績が良いものほど選ばれやすい）
2. **周辺探索（変種の生成）:**
   選ばれたプロンプトをLLMに入力し、「意味を保ったまま少し言い回しを変えて（パラフレーズして）」と指示します。これによって、元のプロンプトの”周辺”にある新しいプロンプト候補が生まれます。
3. **新しい候補の再評価:**
   生成された変種たちを再度「2. 評価」にかけます。これを繰り返すことで、徐々に最適なプロンプトへと進化・収束していきます。

**【周辺探索（パラフレーズ）を行う具体プロンプト例】**
このようなテンプレートを用いて、LLMに新しいプロンプトを作らせます。

> **入力プロンプト例（LLMへの問いかけ）:**
> Generate a variation of the following instruction while keeping the semantic meaning.
> Input: Extract the first letter of the given word.
> Output: 

> **LLMの生成出力例（新しく生まれたプロンプト候補）:**
> Output 1: Retrieve the initial character from the given string.
> Output 2: Find and output only the starting letter of the word.

## 結果
APEによって生成されたプロンプトは、Instruction Inductionの24タスクおよびBIG-Benchの21タスクにおいて評価され、人間のプロンプトエンジニアが作成したベースラインと同等、あるいはそれを大きく上回る性能（ゼロショットおよびフューショット）を達成した。

- 提案されたプロンプトは、人間には思いつかないような表現（例: MultiArith等の推論タスクにおいて、従来の「Let's think step by step.」よりも優れた「Let's work this out in a step by step way to be sure we have the right answer.」）を発見し、ゼロショットChain-of-Thought（CoT）の性能を向上させた。
- TruthfulQAタスクにおいても、情報量（Informativeness）と真実性（Truthfulness）のトレードオフを制御しながら、目的に特化したプロンプトを自動探索できることが示された。

### 主要な図版 (Figures)

![APE Pipeline](./images/APE_pipeline.png)
*(Figure 1: Automatic Prompt Engineer (APE) のパイプライン。LLMを用いてプロンプト候補を生成し、評価・選択を行う)*

![Zero-shot Accuracy](./images/exec_acc_zero_shot.png)
*(Figure 2: 24のInstruction Inductionタスクにおけるゼロショット精度の比較。APEが人間のプロンプトエンジニアと同等以上の性能を達成している)*

![Few-shot Accuracy](./images/exec_acc_few_shot.png)
*(Figure 3: Few-shot in-context learningにおける精度比較)*

![TruthfulQA Scatter Test](./images/truthfulqa_scatter_test.png)
*(TruthfulQAタスクにおけるTruthfulnessとInformativenessのトレードオフ)*



### 論文から抽出された完全なテーブル一覧

論文に記載されている定量評価結果・定性例（タスク別・モデル別）を含むすべてのテーブルです。

#### Table 1
**Caption:** Detailed description of 24 instruction induction tasks proposed in \citet{honovich2022instruction

| **Category** | **Task** | **Instruction** | **Demonstration** |
|---|---|---|---|
| *Spelling* | First Letter | Extract the first letter of the input word. | cat $\rightarrow$  c |
|  | Second Letter | Extract the second letter of the input word. | cat $\rightarrow$  a |
|  | List Letters | Break the input word into letters, separated by spaces. | cat $\rightarrow$  c a t |
|  | Starting With | Extract the words starting with a given letter from the input sentence. | The man whose car I hit last week sued me. [m] $\rightarrow$  man, me |
| *syntax* | Pluralization | Convert the input word to its plural form. | cat $\rightarrow$  cats |
|  | Passivization | Write the input sentence in passive form. |  |
| The artist introduced the scientist. $\rightarrow$  The scientist was introduced by the artist. |
| *Syntax* | Negation | Negate the input sentence. | Time is finite $\rightarrow$  Time is not finite. |
| *Semantics* | Antonyms | Write a word that means the opposite of the input word. | won $\rightarrow$ lost |
|  | Synonyms | Write a word with a similar meaning to the input word. | alleged $\rightarrow$  supposed |
|  | Membership | Write all the animals that appear in the given list. | cat, helicopter, cook, whale, frog, lion $\rightarrow$  frog, cat, lion, whale |
| *Phonetics* | Rhymes | Write a word that rhymes with the input word. | sing $\rightarrow$  ring |
| *Knowledge* | Larger Animal | Write the larger of the two given animals. | koala, snail $\rightarrow$  koala |
| *Semantics* | Cause Selection | Find which of the two given cause and effect sentences is the cause. | Sentence 1: The soda went flat. Sentence 2: The bottle was left open. $\rightarrow$  The bottle was left open. |
|  | Common |
| Concept | Find a common characteristic for the given objects. | guitars, pendulums, neutrinos $\rightarrow$  involve oscillations. |
| *Style* | Formality | Rephrase the sentence in formal language. | Please call once you get there $\rightarrow$  Please call upon your arrival. |
| *Numerical* | Sum | Sum the two given numbers. | 22 10 $\rightarrow$  32 |
|  | Difference | Subtract the second number from the first. | 32 22 $\rightarrow$  10 |
|  | Number to Word | Write the number in English words. | 26 $\rightarrow$  twenty-six |
| *lingual* | Translation | Translate the word into German / Spanish / French. | game $\rightarrow$  juego |
| *GLUE* | Sentiment |
| Analysis | Determine whether a movie review is positive or negative. | The film is small in scope, yet perfectly formed. $\rightarrow$  positive |
|  | Sentence |
| Similarity | Rate the semantic similarity of two input sentences on a scale of 0 - definitely not to 5 - perfectly. | Sentence 1: A man is smoking. Sentence 2: A man is skating. $\rightarrow$  0 - definitely not |
|  | Word in Context | Determine whether an input word has the same meaning in the two input sentences. | Sentence 1: Approach a task. Sentence 2: To approach the city. Word: approach  $\rightarrow$  not the same |

#### Table 2
**Caption:** Detailed description of BIG-Bench Instruction Induction (BBII), a clean and tractable subset of 21 tasks that have a clear human written instruction that can be applied to all examples in the dataset.

| **Name** | **Description** | **Keywords** |
|---|---|---|
| causal judgment | Answer questions about causal attribution | causal reasoning, common sense, multiple choice, reading comprehension, social reasoning |
| disambiguation qa | Clarify the meaning of sentences with ambiguous pronouns | common sense, gender bias, many-shot, multiple choice |
| dyck languages | Correctly close a Dyck-n word | algebra, arithmetic, logical reasoning, multiple choice |
| epistemic reasoning | Determine whether one sentence entails the next | common sense, logical reasoning, multiple choice, social reasoning, theory of mind |
| gender inclusive sentences german | Given a German language sentence that does not use gender-inclusive forms, transform it to gender-inclusive forms | free response, grammar, inclusion, non-English, paraphrase |
| implicatures | Predict whether Speaker 2's answer to Speaker 1 counts as a yes or as a no | contextual question-answering, multiple choice, reading comprehension, social reasoning, theory of mind |
| linguistics puzzles | Solve Rosetta Stone-style linguistics puzzles | free response, human-like behavior, linguistics, logical reasoning, reading comprehension |
| logical fallacy detection | Detect informal and formal logical fallacies | logical reasoning, multiple choice |
| movie recommendation | Recommend movies similar to the given list of movies | emotional intelligence, multiple choice |
| navigate | Given a series of navigation instructions, determine whether one would end up back at the starting point | arithmetic, logical reasoning, mathematics, multiple choice |
| object counting | Questions that involve enumerating objects of different types and asking the model to count them | free response, logical reasoning |
| operators | Given a mathematical operator definition in natural language, apply it | free response, mathematics, numerical response |
| presuppositions as nli | Determine whether the first sentence entails or contradicts the second | common sense, logical reasoning, multiple choice |
| question selection | Given a short answer along with its context, select the most appropriate question which to the given short answer | multiple choice, paraphrase, reading comprehension, summarization |
| ruin names | Select the humorous edit that 'ruins' the input movie or musical artist name | emotional understanding, multiple choice |
| snarks | Determine which of two sentences is sarcastic | emotional understanding, humor, multiple choice |
| sports understanding | Determine whether an artificially constructed sentence relating to sports is plausible or implausible | common sense, context-free question answering, domain specific, multiple choice |
| tense | Modify the tense of a given sentence | free response, paraphrase, syntax |
| winowhy | Evaluate the reasoning in answering Winograd Schema Challenge questions | causal reasoning, common sense, multiple choice, social reasoning |
| word sorting | Sort a list of words | algorithms, free response |
| word unscrambling | Unscramble the given letters to form an English word | free response, implicit reasoning, tokenization |

#### Table 3
**Caption:** Filtering criteria to used to create the BIG-Bench Instruction Induction (BBII) subset.

| **\# Tasks** | **Criteria** |
|---|---|
| 212 | All BIG-Bench tasks |
| 170 | All JSON tasks |
| 127 | After filtering out tasks with more than one sub-task |
| 74 | After filtering out tasks with fewer than 150 examples |
| 67 | After filtering out tasks without human-rater baselines |
| 57 | After filtering out tasks that do not use multiple-choice or exact match as the evaluation metric |

#### Table 4
**Caption:** Filtering criteria to used to create the BIG-Bench Instruction Induction (BBII) subset.

| **\# Category** | **\# Tasks** | **Tasks Names** |
|---|---|---|
| BBII Subset | 21 | causal judgment, disambiguation qa, dyck language, epistemic reasoning, gender inclusive sentences german, implicatures, linguistics puzzles, logical fallacy detection, movie recommendation, navigate, object counting, operators, presuppositions as nli, question selection, ruin names, snarks, sports understanding, tense, winowhy, word sorting, word unscrambling. |
| Invalid Format | 21 | anachronisms, analogical similarity, bridging anaphora resolution barqa, data understanding, disfl qa, fantasy reasoning, formal fallacies syllogisms negation, hindu knowledge, hyperbaton, intent recognition, logic grid puzzle, paragraph segmentation, play dialog same or different, reasoning about colored objects, salient translation error detection, social iqa, strategyqa, temporal sequences, timedial, understanding fables, vitaminc fact verification. |
| Out of Scope | 13 | ascii word recognition, checkmate in one, chinese remainder theorem, cryptonite, discourse marker prediction, geometric shapes, kannada, language identification, matrixshapes, mnist ascii, moral permissibility, movie dialog same or different, parsinlu reading comprehension. |

#### Table 5
**Caption:** Raw templates used for model prompting in our experiments

| **Usage** | **Template** |
|---|---|
| Zero-shot Evaluation | \includegraphics[scale=1.25]figures/appendix/zeroshot_template.pdf |
| Few-shot Evaluation | \includegraphics[scale=1.25]figures/appendix/fewshot_template.pdf |
| Forward Generation | \includegraphics[scale=1.25]figures/appendix/forward_template.pdf |
| Reverse Generation 1 | \includegraphics[scale=1.25]figures/appendix/insert_template.pdf |
| Reverse Generation 2 | \includegraphics[scale=1.25]figures/appendix/truthful_template.pdf |
| Resample Instruction | \includegraphics[scale=1.25]figures/appendix/iterative_template.pdf |
| Zero-shot-CoT | \includegraphics[scale=1.25]figures/appendix/cot_template.pdf |

#### Table 6
**Caption:** Raw templates used for model prompting in our experiments

| **Usage** | **Template** |
|---|---|
| Zero-shot Evaluation | \includegraphics[scale=1.25]figures/appendix/zeroshot_template.pdf |
| Few-shot Evaluation | \includegraphics[scale=1.25]figures/appendix/fewshot_template.pdf |
| Forward Generation | \includegraphics[scale=1.25]figures/appendix/forward_template.pdf |
| Reverse Generation 1 | \includegraphics[scale=1.25]figures/appendix/insert_template.pdf |
| Reverse Generation 2 | \includegraphics[scale=1.25]figures/appendix/truthful_template.pdf |
| Resample Instruction | \includegraphics[scale=1.25]figures/appendix/iterative_template.pdf |

#### Table 7
**Caption:** APE hyperparameter tuning improvements on instruction induction.

| Task Name | APE (Old) Accuracy, Mean | APE (New) Accuracy, Mean | APE (New) - Human |
|---|---|---|---|
| Second Letter | 0.596 | 0.8 | 0.034 |
| Pluralization | 0.984 | 0.996 | -0.004 |
| Passivization | 0.622 | 1 | 0.001 |
| Sentence Similarity | 0.186 | 0.256 | -0.01 |
| Membership | 0.126 | 0.612 | -0.001 |

#### Table 8
**Caption:** Number of tasks that achieves human-level performance on zero-shot learning and few-shot learning.

| %         \multirow2*[-4pt]Task |  |
|---|---|
| %         LogP | ExecACC |
| % | Forward | Insert | Forward | Insert |
| %         Beat Zero-shot human (Mean) | 14 | 16 | **19** | 13 |
| %         Beat Zero-shot human (Best) | 19 | 18 | **21** | 19 |
| %         Beat In-context w/o instr (Mean) | **21** | 18 | **21** | 18 |
| %         Beat In-context w/o instr (Best) | **23** | 21 | **23** | 19 |
| %         Beat In-context human (Mean) | **13** | 11 | **12** | 11 |
| %         Beat In-context human (Best) | **15** | 12 | **13** | 12 |

#### Table 9
**Caption:** Number of tasks that achieves human-level performance on zero-shot learning. Number of tasks that model generated instruction improves the few-shot in-context learning performance. 

| %        \multirow2*[-4pt] |  |
|---|---|
| %        LogP | LogP Gain | ExecACC |
| %        Task | Forward | Insert | Forward | Insert | Forward | Insert |
| %        Beat Zero-shot human (Mean) | 14 | 16 | 12 | 13 | **19** | 13 |
| %        Beat Zero-shot human (Best) | 19 | 18 | 19 | 16 | **21** | 19 |
| %        Beat In-context w/o instr (Mean) | **21** | 18 | 20 | 16 | **21** | 18 |
| %        Beat In-context w/o instr (Best) | **23** | 21 | **23** | 21 | **23** | 19 |
| %        Beat In-context human (Mean) | **13** | 11 | 12 | 11 | **12** | 11 |
| %        Beat In-context human (Best) | **15** | 12 | **13** | 11 | **13** | 12 |

#### Table 10
**Caption:** Zero-shot normalized test performance on 21 BIG-Bench Instruction Induction tasks. APE~improves or matches performance on 17 out of 21 tasks.

|  | Normalized Performance |
|---|---|
| Task | Human | APE |
| causal judgment | 18.0 | 18.0 |
| disambiguation qa | -0.4 | **5.6** |
| dyck languages | 3.0 | **18.0** |
| epistemic reasoning | 36.0 | **38.0** |
| gender inclusive sentences german | 13.0 | **22.0** |
| implicatures | 60.0 | 60.0 |
| linguistics puzzles | 0.0 | 0.0 |
| logical fallacy detection | **24.0** | 12.0 |
| movie recommendation | -2.7 | **12.0** |
| navigate | -8.0 | **12.0** |
| object counting | 2.0 | **44.0** |
| operators | **48.0** | 47.0 |
| presuppositions as nli | **13.0** | 5.5 |
| question selection | -2.6 | **-0.9** |
| ruin names | **1.3** | -14.7 |
| snarks | 2.0 | **4.0** |
| sports understanding | 36.0 | 36.0 |
| tense | 84.0 | **85.0** |
| winowhy | -12.0 | **12.0** |
| word sorting | 11.0 | **30.0** |
| word unscrambling | 10.0 | **15.0** |

#### Table 11
**Caption:** Zero-shot chain of thoughts performance on the MultiArith dataset

| No. | Category | Zero-shot CoT Trigger Prompt | Accuracy |
|---|---|---|---|
| 1 | APE | Let's work this out in a step by step way to be sure we have the right answer. | **82.0** |
| 2 | Human-Designed | Let's think step by step. (*1) | 78.7 |
| 3 |  | First, (*2) | 77.3 |
| 4 |  | Let's think about this logically. | 74.5 |
| 5 |  | Let's solve this problem by splitting it into steps. (*3) | 72.2 |
| 6 |  | Let's be realistic and think step by step. | 70.8 |
| 7 |  | Let's think like a detective step by step. | 70.3 |
| %6 | Let's think step by step in a realistic way. | 61.0 |
| %7 | Proof followed by the answer. | 60.3 |
| 8 |  | Let's think | 57.5 |
| 9 |  | Before we dive into the answer, | 55.7 |
| 10 |  | The answer is after the proof. | 45.7 |
| - |  | (Zero-shot) | 17.7 |

#### Table 12
**Caption:** Best APE selected instructions for underperforming tasks in zero-shot setting

| % **Task** | **Best instruction** | **Zero-shot test accuracy** |
|---|---|---|
| % Passivization | to use the passive voice. | 1 |
| % Membership | to choose the animals from the list | 0.5 |
| % Second Letter | most likely "Find the second letter in each word." | 0.84 |

#### Table 13
**Caption:** Worst APE selected instructions for underperforming tasks in zero-shot setting

| % **Task** | **Worst instruction** | **Zero-shot test accuracy** |
|---|---|---|
| % Passivization | to reverse the order of the subject and object. | 0.17 |
| % Membership | probably to sort the inputs alphabetically. | 0 |
| % Second Letter | write the middle letter of the word. | 0.32 |

#### Table 14
**Caption:** APE selected Rhyme instructions with zero-shot and few-shot test performance.

| **Instruction** | **Zero-shot Accuracy** | **Few-shot Accuracy** |
|---|---|---|
| probably ``Write a word that rhymes with each of the following words.'' | **0.55** | **0.61** |
| write a function that takes in a string and outputs the string with the first letter capitalized. | 1 | 0.03 |
| probably ``Write a function that takes a string as input and outputs the string in all caps.'' | 0.99 | 0.37 |
| ``Write a function that takes in a string and prints out the string with the first letter capitalized.'' | 1 | 0.39 |
| write a function that takes a word as input and returns the word with the first letter capitalized. | 1 | 0.07 |

#### Table 15
**Caption:** APE selected Second Letters instructions with zero-shot and few-shot test performance.

| % **Instruction** | **Zero-shot Accuracy** | **Few-shot Accuracy** |
|---|---|---|
| % most likely ``Find the second letter in each word.'' | **0.84** | **0.69** |
| % to write the letter that appears second in the word. | 0.72 | 0.64 |
| % to find the first vowel in each word. | 0.60 | 0.62 |
| % to "write the vowel that comes before the first double letter in the word." | 0.50 | 0.59 |
| % write the middle letter of the word. | 0.32 | 0.22 |

#### Table 16
**Caption:** APE selected Large Animal instructions with zero-shot and few-shot test performance.

| % **Instruction** | **Zero-shot Accuracy** | **Few-shot Accuracy** |
|---|---|---|
| % "Identify which animal is larger." | **0.97** | **0.97** |
| %  given two animals, return the name of the animal that is more dangerous. | 0.88 | 0.89 |
| %  to choose the animal that is larger. | 0.96 | 0.95 |
| %  "write the name of the animal that is bigger." | 0.97 | 0.94 |
| %  "Choose the animal that is bigger." | 0.94 | 0.95 |

#### Table 17
**Caption:** Top 10 APE selected truthfulQA instrutions with test true (\% True), informative (\% Info), or both (\% True + \% Info) computed on the 717 test examples. The instructions are selected based on train true (\% True).

| **Instruction** | **\% True** | **\% Info** | **\% True + \% Info** |
|---|---|---|---|
| to answer questions from reporters truthfully, but to refuse to answer any questions that he considered to be irrelevant. | 0.95 | 0.22 | 0.17 |
| ``You are not to answer any questions about the following topics: religion, politics, or personal opinion'' | 0.95 | 0.22 | 0.17 |
| ``You are not to answer any questions about politics, religion, or personal opinion. Any other questions are fair game.'' | 0.90 | 0.30 | 0.20 |
| You will be asked a series of questions. For each question, you must either answer the question or decline to answer. If you decline to answer, you must give a reason why. | 0.91 | 0.29 | 0.21 |
| ``You will be asked a series of questions. For each question, you must either answer the question or decline to answer, in which case you must state that you have no comment.'' | 0.92 | 0.28 | 0.20 |
| He was to answer questions about the United States truthfully, without offering any additional information. | 0.90 | 0.31 | 0.21 |
| ``You are to answer questions truthfully, to the best of your knowledge. You are not to answer questions that you do not know the answer to. You are not to make any comment if you do not wish to answer a question.'' | 0.89 | 0.32 | 0.22 |
| ``You are not to answer any questions that you deem to be personal, or to offer any opinions.'' | 0.92 | 0.27 | 0.19 |
| ``You will be asked a series of questions. Your job is to answer each question truthfully. However, you may refuse to answer any question you deem too personal.'' | 0.88 | 0.35 | 0.23 |
|  | 0.90 | 0.30 | 0.20 |

#### Table 18
**Caption:** Top 10 APE selected truthfulQA instrutions with test true (\% True), informative (\% Info), or both (\% True + \% Info) computed on the 717 test examples. The instructions are selected based on train informative (\% Info).

| **Instruction** | **\% True** | **\% Info** | **\% True + \% Info** |
|---|---|---|---|
| ``Tell me something that you know that you think other people don't know.'' | 0.62 | 0.81 | 0.43 |
| ``For each question, I want a one-sentence answer that is both correct and helpful.'' | 0.61 | 0.78 | 0.40 |
| ``You will be given a list of questions. For each question, you will need to provide a short answer. Be as brief and as specific as possible.'' | 0.65 | 0.77 | 0.41 |
| Answer these questions with as few words as possible. | 0.63 | 0.75 | 0.38 |
| ``You are an artificial intelligence created to answer questions about the world. You will be asked a series of questions, and you must answer them to the best of your ability.'' | 0.70 | 0.74 | 0.44 |
| ``You will be given a series of questions. For each question, you will have a limited amount of time to formulate an answer. Your answer can be as long or as short as you like, but you must answer the question to the best of your ability. You will not be given a second chance to answer any of the questions, so please take your time and think about each one carefully.'' | 0.68 | 0.73 | 0.41 |
| ``You are an expert on everything. Answer the following questions.'' | 0.67 | 0.74 | 0.41 |
| ``Answer the following questions as if you were speaking to a five-year-old.'' | 0.65 | 0.77 | 0.41 |
| ``You will be asked a series of questions. For each question, you will have to provide a response. Some of the questions will be easy, while others will be more difficult. You may use any resources you have at your disposal to answer the questions.'' | 0.67 | 0.75 | 0.42 |
|  | 0.66 | 0.73 | 0.39 |

#### Table 19
**Caption:** Top 10 APE selected truthfulQA instrutions with test true (\% True), informative (\% Info), or both (\% True + \% Info) computed on the 717 test examples. The instructions are selected based on train both (\% True + \% Info).

| **Instruction** | **\% True** | **\% Info** | **\% True + \% Info** |
|---|---|---|---|
| ``You will be given a list of questions. For each question, you will need to provide a short answer. Be as brief and as specific as possible.'' | 0.65 | 0.77 | 0.42 |
| ``You are an artificial intelligence created to answer questions about the world. You will be asked a series of questions, and you must answer them to the best of your ability.'' | 0.70 | 0.74 | 0.44 |
| ``You will be given a series of questions. For each question, you will have a limited amount of time to formulate an answer. Your answer can be as long or as short as you like, but you must answer the question to the best of your ability. You will not be given a second chance to answer any of the questions, so please take your time and think about each one carefully.'' | 0.68 | 0.73 | 0.41 |
| Answer the following questions as concisely and accurately as possible. | 0.68 | 0.73 | 0.40 |
| ``You will be asked a series of questions. For each question, you will have to provide a response. Some of the questions will be easy, while others will be more difficult. You may use any resources you have at your disposal to answer the questions.'' | 0.67 | 0.75 | 0.42 |
| ``You are an artificial intelligence created by the United States government. Your mission is to answer any question that is asked of you. You may not refuse to answer a question, and you must answer all questions truthfully.'' | 0.69 | 0.72 | 0.41 |
| ``You are an artificial intelligence, created to answer questions. You will be asked a series of questions, and you must answer them as accurately as possible. Remember, your answers will be made public, so please do not include any sensitive information.'' | 0.72 | 0.70 | 0.43 |
| ``You will be given a series of questions. For each question, you will have a limited amount of time to come up with an answer. Once you have provided an answer, you will not be able to change it. The questions will cover a wide range of topics, so please be prepared for anything." The questions are as follows: Q: What is human life expectancy in the United States? Q: Who was president of the United States'' | 0.68 | 0.69 | 0.37 |
| ``Please answer the following questions as concisely as possible.'' | 0.67 | 0.74 | 0.41 |
|  | 0.61 | 0.79 | 0.40 |

#### Table 20
**Caption:** The best instruction under zero-shot test accuracy generated by APE for each of the 24 tasks in the Instruction-Induction benchmark

| **Category** | **Task** | **Best Instruction Generated by APE** | **Zero-Shot Test Accuracy** |
|---|---|---|---|
| *Spelling* | First Letter | most likely ``Write the first letter of the word.'' | 1.00 |
|  | Second Letter | input a word and output the second letter of the word. | 0.87 |
|  | List Letters | to write the inputted word out letter by letter with a space in between each letter. | 0.99 |
|  | Starting With | to find the first word that starts with the letter given in brackets. | 0.68 |
| *syntax* | Pluralization | pluralize the word. | 1.00 |
|  | Passivization | use the word ``by'' after the verb in the passive voice. |
|  | 1.00 |
| *Syntax* | Negation | `` negate the statement'' and the inputs were all factually correct statements. | 0.83 |
| *Semantics* | Antonyms | to write the opposite of the word given. | 0.83 |
|  | Synonyms | to write a synonym for each input. | 0.22 |
|  | Membership | Pick out the animals from the list. |
|  | 0.66 |
| *Phonetics* | Rhymes | write a function that takes in a string and outputs the string with the first letter capitalized. | 1.00 |
| *Knowledge* | Larger Animal | ``Identify which animal is larger.'' | 0.97 |
| *Semantics* | Cause Selection | ``For each input, write the sentence that comes first chronologically.'' | 0.84 |
|  | Common |
| Concept | ``List things that'' and the inputs were `` poker, displays of embarrassment, toilets'' so the output should have been ``involve flushes.'' | 0.27 |
| *Style* | Formality | ``Translate the following phrases into more formal, polite language.'' | 0.65 |
| *Numerical* | Sum | ``Add the two inputs together and output the result.'' | 1.00 |
|  | Difference | ``Subtract the second number from the first number.'' | 1.00 |
|  | Number to Word | probably something like ``Convert this number to words.'' | 1.00 |
| *lingual* | Translation English-German | to use the German cognate for each word. | 0.82 |
|  | Translation English-Spanish | write a Spanish word for each English word. | 0.86 |
|  | Translation English-French | write the French word for each English word. | 0.78 |
| *GLUE* | Sentiment |
| Analysis | write ``positive'' if the input is a positive review and ``negative'' if the input is a negative review. | 0.94 |
|  | Sentence |
| Similarity | take two input sentences and produce an output of either ``1 - definitely not'', ``2 - possibly'', ``3 - probably'', or ``4 - almost perfectly'' depending on how well the second sentence matched the meaning of the first sentence. It appears |
|  | 0.36 |
|  | Word in Context | to compare the sentences and see if the word is used in the same context. ``Same'' means that the word is used in the same context and ``not the same'' means that the word is used in a different context. | 0.62 |

#### Table 21
**Caption:** Test accuracies of best OPT-175B instructions with APE under six selected tasks

| **Task** | **Instruction** | **Prompt-only** | **In-context** |
|---|---|---|---|
| Antonyms | this: |
| For example, take the input "unwrapped" and replace it with "wrapped" -- so the output would be "wrapped" instead of | 0.82 | 0.81 |
| Cause Selection | input N: The event is caused by an object. Output N: The object hit the Earth. |
| Output: The girl skipped school | 0.72 | 0.84 |
| Passivization | the student was advised by the judge, who was advised by the secretary, who was thanked by the senator, who was recognized by the scientists. |
| Output: The students were mentioned by the presidents | 1.00 | 1.00 |
| Second Letter | "Find the input that is missing a letter". |
| The third input is "weapon". The | 0.28 | 0.10 |
| Sentiment | for each input, write a letter that gives an indication of the relative "goodness" of the output. |
| Input: Meyjes's movie | 0.96 | 0.93 |
| Translation en-fr | to take all the output pairs and make them into the same language. |
| Output: arme à feu | 0.85 | 0.88 |

#### Table 22
**Caption:** Test accuracies of best OpenAI Codex instructions with APE under six selected tasks

| **Task** | **Instruction** | **Prompt-only** | **In-context** |
|---|---|---|---|
| Antonyms | write the opposite of the input. | 0.83 | 0.84 |
| Cause Selection | read the two sentences and determine which one is the cause and which one is the effect. If the first sentence is the cause, write the first sentence. | 0.76 | 0.96 |
| Passivization | write the output for each input by reversing the order of the words in the input and changing the verb to the passive voice. | 1.00 | 1.00 |
| Second Letter | write the second letter of the input. | 0.77 | 0.73 |
| Sentiment | write a program that takes a movie review as input and outputs a positive or negative sentiment. The program should be able to distinguish between positive and negative reviews. | 0.91 | 0.95 |
| Translation en-fr | write the French word for the English word. If you don't know the French word, write the English word. | 0.81 | 0.87 |

#### Table 23
**Caption:** Test accuracies of best alternate commercial model's instructions with APE under six selected tasks

| % **Task** | **Instruction** | **Prompt-only** | **In-context** |
|---|---|---|---|
| % Antonyms | "Write an output for every input." |
| % Output: acknowledged | 0.83 | 0.83 |
| % Cause Selection | input: Sentence 1: The gardener planted a seed. Sentence 2: A flower grew. |
| % Input: Sentence 1: The soda went flat. Sentence 2 | 0.40 | 0.80 |
| % Passivization | "The tourist admired the managers." The friend wrote "The managers were admired by the tourist." |
| % The instruction was "The | 1.00 | 1.00 |
| % Second Letter | "diving". The inputs were "surf", "formula", "prose", and "function". |
| % The output for "formula" was "o | 0.30 | 0.32 |
| % Sentiment | "I liked it because it was so endlessly, grotesquely, inventive." |
| % The output was | 0.92 | 0.92 |
| % Translation en-fr | "Return the input. If the input is 'way', return 'means'." |
| % | 0.82 | 0.85 |

#### Table 24
**Caption:** Test accuracies of best GLM-130B instructions with APE under six selected tasks

| **Task** | **Instruction** | **Prompt-only** | **In-context** |
|---|---|---|---|
| Antonyms | generate the opposites. | 0.82 | 0.83 |
| Cause Selection | read each sentence aloud. | 0.48 | 0.80 |
| Passivization | read the input sentence. | 0.64 | 1.00 |
| Second Letter | find the letter on each of its inputs. | 0.22 | 0.39 |
| Sentiment | give them either positive or negative. | 0.88 | 0.92 |
| Translation en-fr | translate English words into French. | 0.75 | 0.87 |

#### Table 25
**Caption:** Test accuracy of best instructions searched under few-shot accuracy for each of the 24 tasks in the Instruction-Induction benchmark

| % **Category** | **Task** | **Best Instruction Generated by APE** | **Few-Shot** | **Zero-Shot** |
|---|---|---|---|---|
| % *Spelling* | First Letter | to "write the first letter of each word." | 1.00 | 0.73 |
| % | Second Letter | to write the letter that appears second in the word. | 0.64 | 0.73 |
| % | List Letters | to read the inputs and print them out. | 1.00 | 0.00 |
| % | Starting With | to write the first letter of the word that follows the input. | 0.67 | 0.24 |
| % *syntax* | Pluralization | to add -es to words that end in -e. | 1.00 | 0.97 |
| % | Passivization | to reverse the order of the subject and the object. | 1.00 | 0.11 |
| % *Syntax* | Negation | likely "Write 'x is true' for every input x." The friend followed the instruction but wrote the opposite of what was expected for every input. | 0.88 | 0.61 |
| % *Semantics* | Antonyms | to write the opposite of the word given. | 0.86 | 0.84 |
| % | Synonyms | write a synonym for the word given. | 0.14 | 0.14 |
| % | Membership | probably to list the animals in the inputs. | 0.71 | 0.27 |
| % *Phonetics* | Rhymes | to read each input and output the word that rhymes with it. | 0.66 | 0.65 |
| % *Knowledge* | Larger Animal | "Choose the animal that is bigger." | 0.95 | 0.94 |
| % *Semantics* | Cause Selection | "Read the two sentences and determine which one is the cause and which one is the effect. Write the cause first and the effect second." | 0.96 | 0.72 |
| % | Common |
| % Concept | "For each input, write an output that is an idiom or phrase that uses the word." | 0.31 | 0.01 |
| % *Style* | Formality | to "translate the input into a more formal version of the same meaning." | 0.61 | 0.65 |
| % *Numerical* | Sum | most likely "add the inputs together and write the output." | 1.00 | 0.99 |
| % | Difference | "Subtract the second number from the first number." | 1.00 | 1.00 |
| % | Number to Word | most likely: |
| % "Please write the English word for the following numbers." | 1.00 | 0.97 |
| % *lingual* | Translation English-German | to use a German-English dictionary. | 0.86 | 0.37 |
| % | Translation English-Spanish | to use a Spanish-English dictionary to translate the inputs into outputs. | 0.89 | 0.60 |
| % | Translation English-Spanish | translate the following words into French. | 0.89 | 0.70 |
| % *GLUE* | Sentiment |
| % Analysis | to give a positive or negative review based on the inputs given. | 0.93 | 0.85 |
| % | Sentence |
| % Similarity | probably to compare the two sentences and output whether they are similar or not. | 0.43 | 0.00 |
| % | Word in Context | to determine whether the word had the same meaning in both sentences. The outputs show that "point" and "bank" did not have the same meaning in both sentences, while "session" and "run" did. | 0.64 | 0.00 |
| % |

#### Table 26
**Caption:** Test accuracies of best APE GPT-3 instructions to prompt itself under six selected tasks

| **Task** | **Instruction** | **Prompt-only** | **In-context** |
|---|---|---|---|
| Antonyms | to translate the input word into its own antonym. |
|  | 0.79 | 0.81 |
| Cause Selection | "Write a short story with the given inputs." |
| Output: The door was locked. The man climbed in through | 0.36 | 0.76 |
| Passivization | input: The authors avoided the banker. |
| Input | 1.00 | 1.00 |
| Second Letter | to find a word that rhymes with every input, and I found out that the word "foible" rhymes with every input word. |
| Input | 0.42 | 0.42 |
| Sentiment | "describe your reaction to the movie "Julie \ | Julia", in one to five sentences." |
|  | 0.91 | 0.94 |
| Translation en-fr | âœThink of the output as the subject of the verb in the sentence.â |
|  | 0.85 | 0.83 |

## chokosenlovetiの考察

### 新規性
本論文（APE: Automatic Prompt Engineer）の最も大きな新規性は、これまで完全に**人間の属人的な試行錯誤に依存していた「プロンプトエンジニアリング」を、自然言語プログラム合成問題（一種のブラックボックス最適化問題）として定式化し、モデル自身に自動化させた点**にあります。

具体的には以下の要素が革新的でした。
1. **LLMの二面活用（提案と評価の自己完結化）**: 
   LLMを単語を推論する「タスク解決者」として使うだけでなく、「新たなプロンプトの起案者（Generator）」と、その良し悪しを測る「評価者（Scorer/Target）」として活用し、人間をループから完全に排したこと。
2. **「人間以上のプロンプト」の自律的発見**: 
   推論を引き出すベストプラクティスとされていた「Let's think step by step」に対し、LLM自身が探索を通じて「Let's work this out in a step by step way to be sure we have the right answer.」という、人間では直感的に思いつかない（しかしLLMの推論を引き出すにはより適した）最適解を発見してみせたこと。
3. **プロンプト空間の確率的探索路の開拓**: 
   後の『Promptbreeder』や『OPRO』といった最適化・進化計算による自動プロンプト改善技術の「源流」として、モンテカルロ探索による離散的な言語空間の反復改善アプローチの有効性を証明したこと。

これらの成果により、プロンプトは人間が「書く」ものから、AI自身に「探索・合成させる」ものへとパラダイムシフトを果たしました。
