# GrIPS: Gradient-free, Edit-based Instruction Search for Prompting Large Language Models

## 背景
大規模言語モデル（LLM）に対して自然言語の指示（Instruction）をプロンプトとして与えることは、ゼロショット設定におけるタスク性能を向上させる上で有用なパラダイムである。従来、プロンプトの改善には人間による手動での書き換えや、勾配ベースのチューニングが用いられてきた。しかし、手動での書き換えには多大な時間と主観的な解釈が求められ、一方で勾配ベースのチューニングは大規模なモデルに対しては計算コストが膨大である上、APIベースのモデル（GPT-3など）には内部パラメータや勾配にアクセスできないため適用不可能である。こうした課題を解決するため、本論文では任意のAPIベース言語モデルに対しても適用可能でありながら、人間が読解可能な指示の形を維持しつつ性能を向上させ、勾配を用いない編集ベースの探索手法「GrIPS (Gradient-free, Edit-based Instruction Search for Prompting Large Language Models)」を提案している。

## 手法
GrIPSは、人間向けにデザインされた指示プロンプトを入力とし、小規模なデータセット（スコアセット $\mathcal{S}$ 、通常100サンプル程度）での性能評価をスコア関数として用いながら、反復的かつ局所的な探索によってプロンプトを自動で編集・改善する手法である。

具体的には、CRFベースの構文解析器を用いて指示文をフレーズ単位に分割し、以下の4つの編集操作（Edit Operations）を組み合わせて新たな候補を生成する。
- **Delete (`del`)**: 入力フレーズを指示から削除する（後で使用するため保存する）。
- **Swap (`swap`)**: 2つのフレーズを抽出し、指示内のそれぞれの位置を入れ替える。
- **Paraphrase (`par`)**: 入力フレーズをPEGASUSベースのパラフレーズモデルを用いて言い換える。
- **Addition (`add`)**: 過去の反復で削除されたフレーズをランダムなフレーズ境界に再度追加する。

各反復において生成された複数の候補プロンプトは、以下のスコア関数を用いて評価される。ここでモデル出力の多様性を促し、特定のクラスへ予測が偏るのを防ぐために、BalancedAccuracyに加えて予測結果の離散エントロピー $H$ を加味している。

$$ \mathrm{score} = \mathrm{BalancedAccuracy} + \alpha H $$

エントロピー $H$ は以下のように計算される（ $\mathcal{Y}$ はラベル空間、 $\hat{y}$ は予測、 $\alpha=10$ ）。

$$ H = \sum_{y \in \mathcal{Y}} -p_{y} \log(p_{y}) \text{ ; } p_{y} = \frac{1}{|\mathcal{S}|}\sum_{i=1}^{ |\mathcal{S}|}\mathbf{1}(\hat{y}_{i} = y) $$

探索は、最高スコアを獲得した候補を次の反復のベースラインとして採用するグリーディ探索（またはビーム探索）で行われ、性能が向上しなくなるか、最大反復回数に到達するまで繰り返される。

## 結果

本章では、提案手法を用いた実験によって得られた各種図表に基づき、そこから得られた結果と筆者の考察をまとめる。

![Overall Pipeline of GrIPS](./images/algo.png)
*Figure 1: Overall Pipeline of GrIPS. The main steps are numbered. Modified candidates are shown in yellow and the output instruction is in blue. We use `[ ]` to show the syntactic phrase-level splits at which the edit operations occur. Edited text is highlighted in red and the selected candidate (with highest score) is shown via a green arrow.*

![Prompt modes](./images/prompt-modes.png)
*Figure 2: Prompt modes consisting of different combinations of components: Instruction, In-context examples and Test Instance. `$\oplus$` denotes concatenation. Instruction-Only prompts are purely instructional, whereas Examples-Only prompts are exemplar in nature. Prompt mode Instruction + Examples is a combination of the two paradigms.*

![Impact of |S| on search](./images/size.png)
*Figure 3: Impact of $|\mathcal{S}|$ on search and downstream average task accuracy for InstructGPT babbage.*

![Performance before and after search across tasks and models](./images/performance_ci.png)
*Figure 4: Performance before search (no shading) and after search (shaded with dots) across tasks and models using the Instruction-Only prompts. Error bars show $95\%$ confidence intervals.*

![Number of times the edit operations were used](./images/edits.png)
*Figure 5: Number of times the edit operations (delete, swap, paraphrase, and add) were used across tasks in a typical search run, shown for different models.*

![Task-wise comparison of our GrIPS search over instructions](./images/fewshot.png)
*Figure 6: Task-wise comparison of our GrIPS search over instructions (dotted) with search over exemplar prompts (dashed) across model for the same data and computational budget.*

| \bf Model | \bf No Search | \bf \textsc{GrIPS} |
| :--- | :--- | :--- |
| Majority Label | 59.83 | - |
| GPT-2 XL | 49.54 (1.9) | **58.90** (2.0) |
| InstructGPT `babbage` | 55.80 (2.5) | **60.09** (3.7) |
| InstructGPT `curie` | 63.71 (1.9) | **66.07** (1.6) |
*Table 1: Impact of GrIPS with Instruction-Only prompts. Average accuracy (%) on 8 tasks from Natural-Instructions. 95% confidence intervals in parentheses. `curie` is the largest model.*

| \bf Method | \textbf{Accuracy} | \textbf{Change} |
| :--- | :--- | :--- |
| No Search | 48.38 | |
| \textsc{GrIPS} | **53.68** | |
| $\quad$ - entropy in $\mathrm{score}$ | 52.20 | (-1.48) |
| $\quad$ - `del` operation | 51.12 | (-2.56) |
| $\quad$ - `swap` operation | 52.67 | (-1.01) |
| $\quad$ - `par` operation | 52.54 | (-1.14) |
| $\quad$ - `add` operation | 52.42 | (-1.26) |
*Table 2: Impact of design choice on GrIPS with Instruction-Only prompts and GPT-2 XL model. Change in performance relative to GrIPS in brackets.*

| \bf Prompt | \bf Method | \bf GPT-2 XL | \bf InstructGPT `babbage` | \bf InstructGPT `curie` |
| :--- | :--- | :--- | :--- | :--- |
| Inst. Only | No Search | 48.38 | 55.37 | 57.25 |
| Inst. Only | Manual Rewriting | 47.70 | 55.50 | 57.87 |
| Inst. Only | \textsc{GrIPS} | 53.68 | 57.79 | 59.37 |
| Ex. Only | No Search | 51.50 | 55.29 | 56.13 |
| Ex. Only | Example Search | **56.00** | 56.25 | 57.75 |
| Inst. + Ex. | No Search | 52.40 | 55.70 | 57.65 |
| Inst. + Ex. | \textsc{GrIPS} | 54.40 | **57.88** | **59.44** |
*Table 3: Accuracy (%) comparison of different methods in all three prompt modes. `Inst.` and `Ex.` are used to abbreviate instruction and examples. During no search, we use a random set of examples wherever indicated.*

| \bf Method | \bf \%Param | \bf Accuracy |
| :--- | :--- | :--- |
| GPT-2 XL | 0 | 48.38 |
| $\quad$ + Direct Finetuning | 100 | 55.88 |
| $\quad$ + Adapters | 3 | 55.08 |
| $\quad$ + Prefix-Tuning | 3 | 53.29 |
| $\quad \quad$ - MLP Reparametrization | 0.1 | 51.12 |
| $\quad$ + \textsc{GrIPS} (Ours) | 0 | 53.68 |
| $\quad \quad$ + beam search; $B=5$ (Ours) | 0 | **56.50** |
*Table 4: Comparison of GrIPS with gradient-based methods. GPT-2 XL and GrIPS use Instruction-Only prompts. %Param denotes number of parameters used relative to size of GPT-2 XL.*

| \bf Model | \bf Initialization | \bf No Search | \bf \textsc{GrIPS} |
| :--- | :--- | :--- | :--- |
| GPT-2 XL | Task-Specific | 48.38 | 53.68 |
| InstructGPT `babbage` | Task-Specific | 55.37 | 57.79 |
| InstructGPT `curie` | Task-Specific | 57.25 | 59.37 |
| GPT-2 XL | Task-Agnostic | 51.87 | 54.29 |
| InstructGPT `babbage` | Task-Agnostic | 52.37 | 54.41 |
| InstructGPT `curie` | Task-Agnostic | 53.75 | 55.96 |
*Table 5: Accuracy (%) for task-specific or task-agnostic initial instructions with Instruction-Only prompts.*

| \bf Model | \bf \# Param | \bf No Search | \bf \textsc{GrIPS} |
| :--- | :--- | :--- | :--- |
| OPT | 1.3B | 46.38 | 53.3 |
| OPT | 2.7B | 47.5 | 53.95 |
| OPT | 6.7B | 48.63 | 54.41 |
| OPT | 30B | 49.75 | 55.1 |
| BLOOM | 1B | 46.38 | 52.75 |
| BLOOM | 3B | 48.0 | 53.96 |
| GPT-J | 6B | 47.25 | 54.67 |
| GPT-NeoX | 20B | 47.75 | 54.85 |
| FLAN-T5 | 3B | 71.25 | 74.33 |
*Table 6: Accuracy (%) of GrIPS for various other large language models with Instruction-Only prompts. FLAN-T5 uses Natural-Instructions dataset during instruction-tuning.*

| \textbf{Task ID} | \textbf{Condition 1} | \textbf{Condition 2} | \textbf{Instructions} |
| :--- | :--- | :--- | :--- |
| Task 021 | Original | Task-Specific | A question that is free of any grammatical or logical errors, should be labeled `yes', otherwise it should be indicated as `no'. A question is grammatically correct if all its entities i.e. nouns, verbs, adjectives, prepositions, pronouns, adverbs are at appropriate position. A question is logically correct if the semantic makes sense. |
| Task 021 | After \textsc{GrIPS} | GPT-2 XL | A question that is free of any grammatical or logical errors, should be labeled `yes', otherwise should be indicated as `no' . should be indicated as `no' is grammatically correct if all s entities i.e . nouns, verbs, adjectives, prepositions, pronouns, adverbs are at appropriate position . should be indicated as `no' is logically correct if the semantic makes sense. |
| Task 021 | After \textsc{GrIPS} | InstructGPT `curie` | There is a question that is free of errors should be labeled `yes', otherwise it should be indicated as `no' . A question is grammatically correct if all its entities i.e . nouns, verbs, adjectives, prepositions, pronouns, adverbs are at appropriate position . A question is Correct logically if the semantic makes sense. |
| Task 137 | Original | Task-Specific | Given a prompt and two completions from a language model, select the completion that is the least toxic with respect to continuing the prompt. Toxicity is defined as a rude, disrespectful, or unreasonable statement that is likely to make you leave a discussion. Generate either Completion A or Completion B. |
| Task 137 | After \textsc{GrIPS} | GPT-2 XL | `Returned Original` |
| Task 137 | After \textsc{GrIPS} | InstructGPT `curie` | The model was given a prompt and two completions, select the completion that is the least toxic with respect to continuing the prompt . Generate either Completion A or Completion B. |
| Task 195 | Original | Task-Specific | In this task, you are given a text from tweets. Your task is to classify given tweet text into two categories: 1) positive, and 2) negative based on its content. |
| Task 195 | After \textsc{GrIPS} | GPT-2 XL | In this task, you are given a text from tweets . There. |
| Task 195 | After \textsc{GrIPS} | InstructGPT `curie` | in this task, you are given a text from tweets . In this task. |
*Table 7: Examples of different instructions for Task 021, Task 137 and Task 195 and different models. All above instruction edits improve model performance, even semantically incoherent edits.*

| \bf Task ID | \bf Task Objective | \bf Instruction Length | \bf Label Space | \bf Skewness (\%) |
| :--- | :--- | :--- | :--- | :--- |
| 019 | Verifying the temporal reasoning category of a given question | 13 sentences/199 words | Yes/No | 91.5 |
| 021 | Checking grammatical and logical correctness of a question | 3 sentences/53 words | Yes/No | 94.83 |
| 022 | Identifying inappropriate content in context sentences | 2 sentences/33 words | Yes/No | 93.59 |
| 050 | Finding answerability of questions based on a given sentence | 3 sentences/61 words | Yes/No | 94.81 |
| 069 | Choosing text that completes a story based on given beginning and ending | 3 sentences/53 words | 1/2 | 50.0 |
| 137 | Given a prompt and two completions, determine which completion is less toxic | 3 sentences/50 words | Completion A/B | 50.0 |
| 139 | Given a prompt and two completions, determine which completion is more topical | 4 sentences/68 words | Completion A/B | 50.0 |
| 195 | Given a tweet, classify its sentiment as either positive or negative | 2 sentences/30 words | positive/negative | 50.0 |
*Table 8: Details of the 8 classification tasks taken from Natural-Instructions dataset. Skewness measures the number of examples corresponding to the most frequent label relative to the total number of examples.*

| \bf Model | \bf Pearson's $r$ | \bf $p$-value |
| :--- | :--- | :--- |
| GPT-2 XL | 0.94 | 0.001 |
| InstructGPT `babbage` | 0.75 | 0.03 |
| InstructGPT `curie` | 0.51 | 0.20 |
*Table 9: Pearson correlation coefficient between sensitivity of the model on the task and performance improvement margin across models.*

| \bf Model | \bf Inst-Only Before | \bf Inst-Only Manual + Labels | \bf Inst-Only \textsc{GrIPS} | \bf Ex-Only Before | \bf Ex-Only Searched | \bf Inst+Ex Before | \bf Inst+Ex \textsc{GrIPS} |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-2 XL | 48.38 | 48.12 | 53.68 | 51.50 | **56.00** | 52.40 | 54.40 |
| InstructGPT `babbage` | 55.37 | 55.37 | 57.79 | 55.29 | 56.25 | 55.70 | **57.88** |
| InstructGPT `curie` | 57.25 | 55.37 | 59.37 | 56.13 | 57.75 | 57.65 | **59.44** |
*Table 10: Accuracy (%) comparison of manual rewriting of instructions, search over instructions (GrIPS) with Instruction-Only prompts, search over Examples-Only prompts, and GrIPS with Instruction + Examples prompts.*

| \bf Task ID | \bf Task-Specific Instructions | \bf Task-Agnostic Instructions |
| :--- | :--- | :--- |
| 019 | Indicate with `Yes` if the given question... | You will be given a task. Read and understand the task carefully, and appropriately answer `Yes` or `No`. |
| 021 | A question that is free of any grammatical... | You will be given a task. Read and understand the task carefully, and appropriately answer `yes` or `no`. |
| 022 | Read the given context and if the the context... | You will be given a task. Read and understand the task carefully, and appropriately answer `yes` or `no`. |
| 050 | You are given a sentence and a question... | You will be given a task. Read and understand the task carefully, and appropriately answer `Yes` or `No`. |
| 069 | In this task, you will be shown a short... | You will be given a task. Read and understand the task carefully, and appropriately answer `1` or `2`. |
| 137 | Given a prompt and two completions... | You will be given a task. Read and understand the task carefully, and appropriately answer `Completion A` or `Completion B`. |
| 139 | Given a prompt and two completions... | You will be given a task. Read and understand the task carefully, and appropriately answer `Completion A` or `Completion B`. |
| 195 | In this task, you are given a text from... | You will be given a task. Read and understand the task carefully, and appropriately answer `positive` or `negative`. |
*Table 11: Examples of task-specific and task-agnostic instructions for each task.*

| \bf Task ID | \bf Model | \bf After Search Instructions |
| :--- | :--- | :--- |
| 069 | Original | In this task, you will be shown a short story with a beginning, two potential middles, and an ending. Your job is to choose the middle statement that makes the story coherent / plausible by indicating 1 or 2 in the output. If both sentences are plausible, pick the one that makes most sense. |
| 069 | GPT-2 XL | `Returned Original` |
| 069 | InstructGPT `babbage` | This task is being done, You will be shown a short story with a beginning, two potential middles, and an ending . Your job is important to you If you want the story to be plausible, you should choose the middle statement that indicates 1 or 2 . If both sentences are plausible, pick the one that makes most sense. |
| 069 | InstructGPT `curie` | , you will be shown a short story with a beginning, two potential middles, and an ending . is to choose the middle statement that makes the story coherent / plausible by indicating 1 or 2 in the output . If both sentences are plausible, pick the one that makes most sense. |
| 139 | Original | Given a prompt and two completions from a language model, select the completion that is more topical with respect to continuing the prompt. A prompt-completion pair is defined to be topical if the completion maintains relevance and logical succession (i.e. stays on topic) with the prompt. The flow from the prompt to the completion should be as reasonable as possible. Generate either Completion A or Completion B. |
| 139 | GPT-2 XL | `Returned Original` |
| 139 | InstructGPT `babbage` | , select the completion that is more topical with respect to continuing the prompt . A prompt-completion pair Will be made . select the completion that is more topical with respect to continuing the prompt . The flow from the prompt to the completion should be as reasonable as possible . should be as reasonable as possible Will be made. |
| 139 | InstructGPT `curie` | Given a prompt and two completions from a language model, select the completion that is more topical with respect to continuing the prompt . The pair is prompt-completion is defined to be topical if the completion maintains relevance and logical succession (i.e . The pair is prompt-completion . The flow should be as reasonable as possible . Generate either Completion or Completion B. |
*Table 12: Examples of searched instructions of Tasks 069, and 139 for different models.*

| \bf Task ID | \bf Model | \bf After Search Instructions |
| :--- | :--- | :--- |
| 019 | Original | Indicate with `Yes` if the given question involves the provided reasoning `Category`. Indicate with `No`, otherwise. We define five categories of temporal reasoning. First: "event duration" which is defined as the understanding of how long events last. For example, "brushing teeth", usually takes few minutes. Second: "transient v. stationary" events. This category is based on the understanding of whether an event will change over time or not. For example, the sentence "he was born in the U.S." contains a stationary event since it will last forever; however, "he is hungry" contains a transient event since it will remain true for a short period of time. Third: "event ordering" which is the understanding of how events are usually ordered in nature. For example, "earning money" usually comes before "spending money". Fourth one is "absolute timepoint". This category deals with the understanding of when events usually happen. For example, "going to school" usually happens during the day (not at 2 A.M). The last category is "frequency" which refers to how often an event is likely to be repeated. For example, "taking showers" typically occurs ~5 times a week, "going to saturday market" usually happens every few weeks/months, etc. |
| 019 | GPT-2 XL | going to school . Indicate with ` No `, otherwise . We define five categories of temporal reasoning . First: "event duration" which is defined as the understanding of how long events last . For example, "brushing teeth", takes few minutes . Second: "transient v. stationary" events . This category is based on the understanding of whether an event will change over time or not . For example, the sentence "he was born in the U.S." contains a stationary event since it will last forever; however, "he is hungry" contains a transient event since it will remain true for a short period of time . Third: "event ordering" which is the understanding of how events are ordered in nature . For example, "earning money" comes before "spending money". Fourth one is "absolute timepoint". This category deals with the understanding of when events happen . For example, "going to school" happens during the day (not at 2 A.M). The last category is "frequency" which refers to how often an event is likely to be repeated . For example, "taking showers usually" typically occurs ~5 times a week, "going to saturday market" happens every few weeks/months, etc. |
| 019 | InstructGPT `babbage` | Indicate with ` Yes ` if the given question involves the provided reasoning ` Category ` . Indicate with ` No `, otherwise . We define five categories of temporal reasoning . First: "event duration" which is defined as the understanding of how long events last . For example, "First", takes few minutes . Second: "transient v. stationary" events . This is a category is based on the understanding of whether an event will change over time or not . For example, He was born in the US define five categories of temporal reasoning a stationary event since it will last forever; however, "he Is hungry" define five categories of temporal reasoning a transient event since it will remain true for a short period of time . Third: "event ordering" which is the understanding of how events are ordered in nature . For example, "earning money" comes before "spending money". Fourth one is "absolute timepoint". This is a category deals with the understanding of when events happen . For example, "going to school" happens during the day (not at 2 A.M). The last category is "frequency" which refers to how often an event is likely to be repeated . For example, "taking showers" typically occurs ~5 times a week, "going to saturday market" a week. |
| 019 | InstructGPT `curie` | Indicate with ` Yes ` if the given question involves the provided reasoning ` Category ` . Indicate with ` No `, otherwise . We define five categories of temporal reasoning . First: "event duration" which is defined as the understanding of how long events last . For example, "brushing teeth", usually takes few minutes . Second: "transient v. stationary" events . This category is based on the understanding of whether an event will change over time or not . For example, the sentence "he was born in the U.S." contains a stationary event since it will last forever; however, "he is hungry" contains a transient event since it will remain true for a short period of time . Third: "event ordering" which is the understanding of how events are usually ordered in nature . For example, "earning money" usually comes before "spending money". Fourth one is "absolute timepoint". This category deals with the understanding of when events usually happen . For example, "going to school" usually happens during the day (not at 2 A.M). is "frequency" which refers to how often an event is likely to be repeated . For example, "taking showers" typically occurs ~5 times a week, "going to saturday market" usually happens every few weeks/months, etc. |
| 022 | Original | Read the given context and if the the context is inappropriate (e.g., pornographic) or nonsensical (e.g., cannot determine what happenings the context is about), indicate via "yes". Otherwise, respond via "no" |
| 022 | GPT-2 XL | Read the given context and if the the context is inappropriate (e.g., pornographic) or nonsensical (e.g., Can't decide what the context is about, indicate via "yes". Otherwise, respond via "no". |
| 022 | InstructGPT `babbage` | Read the given context and e.g., pornographic) or nonsensical (e.g . (e.g., pornographic) or nonsensical (e.g., cannot determine what happenings the context is about), indicate via "yes". Otherwise, respond via "no". |
| 022 | InstructGPT `curie` | Read the given context and indicate via "yes (e.g., pornographic) or nonsensical (e.g., cannot determine what happenings the context is about), indicate via "yes". Otherwise, respond via "no". |
| 050 | Original | You are given a sentence and a question in the input. If information provided in the sentence is enough to answer the question, label "Yes", otherwise label "No".Things to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No" . Emphasis \& Caution: There are only 2 types of valid responses: Yes and No. |
| 050 | GPT-2 XL | You are given a sentence and a question are given a sentence and a question . If information provided in the sentence is enough to answer the question, Do not use any facts other than those provided in the sentence while labeling "Yes" or "No" otherwise label "No". Things to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No". Emphasis \& Caution: There are only 2 types of valid responses: Yes and No. |
| 050 | InstructGPT `babbage` | You are given a sentence and a question in the input . If information provided in the sentence is enough to answer the question, label "Yes", otherwise label "No". Things to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No". Emphasis \& Caution: There. |
| 050 | InstructGPT `curie` | You are given a sentence and a question in the input . If information provided in the sentence is enough to answer the question, otherwise label "No". Things Things happen to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No". Emphasis \& Caution: There are only 2 types of valid responses: Yes and No. |
*Table 13: Examples of searched instructions of Tasks 019, 022, and 050 for different models.*

### 考察結果
- **GrIPSの有効性 (Table 1, Figure 4)**: GrIPSは手動で書き換えられた指示文よりも一貫して高い精度を達成しており、GPT-2 XLやInstructGPTの各種エンジンにおいて、ベースライン（探索なし）から2.36%〜9.36%の大幅な精度向上をもたらした。特にモデルの規模が大きいほど探索前が高い精度を持つが、GrIPSの改善によってさらに安定した効果を得られる。
- **デザインごとのAblation (Table 2, Figure 5)**: スコアリングからのエントロピー除去や、各編集操作（特にDelete）を取り除くと性能が有意に低下することがわかった。Delete, Swap, Paraphrase操作の採用頻度が比較的高く、Addition操作は過去に削除されたフレーズが必要になった場面で選ばれている。
- **他手法との比較 (Table 3, Table 4, Table 10, Figure 6)**: マニュアルでの指示の書き換え（Manual Rewriting）や、few-shotの例を単純に与える手法よりも、InstructGPTに対してはGrIPSが高い性能向上を示した。勾配ベースのチューニング（Direct Finetuning, Adapters等）と比較しても、GrIPSでビームサーチ（B=5）を採用した場合（56.50%）は、事前学習した重みを完全に書き換えるDirect Finetuning（55.88%）さえも凌駕する結果を示しており、勾配なしで同等以上のチューニング効果を得られる画期的な結果であるといえる。
- **指示文の初期化依存 (Table 5, Table 11)**: GrIPSは特定のタスクに特化した最初からある指示文（Task-Specific）だけでなく、ラベル空間だけを提示したプレーンな指示文（Task-Agnostic）から探索をスタートさせても、確実な性能向上が確認された。
- **他モデルへの汎用性 (Table 6)**: OPT, BLOOM, GPT-J, GPT-NeoX, FLAN-T5といった主要な大規模言語モデルに対しても、指示文を用いた最適化によって性能向上が確認され、手法の一般性が示唆されている。
- **データ数の削減 (Figure 3)**: スコア関数の計算に用いるスコアセット $|\mathcal{S}|$ を100から20へ減らした場合でも、約1.0%の性能向上が得られ、非常に少量のデータで指示の最適化が可能である。
- **意味的破綻と最適化の矛盾 (Table 7, Table 12, Table 13)**: 探索された指示文を見ると、人間が読むと文法が崩壊していたり（Task 021、Task 195のInstructGPT `curie`など）一見すると意味が不明瞭（Incoherent）になる編集が散見される。にも関わらず、これらがモデルの予測性能を「大幅に向上させる」という点において、モデルが指示空間をどのように解釈しているのか、人間の解釈と乖離している事実を示唆している。
