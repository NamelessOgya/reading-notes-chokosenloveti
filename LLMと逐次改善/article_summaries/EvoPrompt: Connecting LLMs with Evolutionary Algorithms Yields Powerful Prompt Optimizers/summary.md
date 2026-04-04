# summary_format  
論文の背景, 手法, 結果の3項目でまとめなさい。

## 背景  
LLM（大規模言語モデル）を利用する際、タスクのパフォーマンスはプロンプトの設計に大きく依存します。そのためプロンプトエンジニアリングは非常に重要ですが、タスクやモデルごとに最適なプロンプトを見つけるには属人的な試行錯誤が必要です。それを自動化するための既存の自動プロンプト最適化手法は、言語モデルの出力確率（トークン確率）などに依存しているものが多く、API経由でのみ利用できるブラックボックスなモデル（GPT-4など）には適用しにくい課題があります。
また、多様なプロンプトを探索する手法（Exploration）か、現在のものを局所的に改善する手法（Exploitation）のどちらかに偏っており、両者のバランスを取ることが難しいという課題もありました。そこで本研究では、強力な探索と知識活用のバランスを保つ「進化的アルゴリズム (Evolutionary Algorithms: EAs)」と、強力な言語理解力を持つ「LLM」を結合させる自動プロンプト最適化フレームワーク「EvoPrompt」を提案しています。

## 手法  
EvoPromptは、進化的アルゴリズム（EAs）のプロセスをベースに、新しいプロンプトの生成・変異を行う「進化オペレーター」としてLLMを活用します。具体的には以下の3ステップから成ります。

1. **Initial population (初期集団)**: 人間が作成した初期プロンプトと、LLMが自動生成したプロンプトを組み合わせて構成し、局所解に陥るのを防ぎます。
2. **Evolution (進化)**: LLMを指示に従って動作させ、プロンプト変異（Mutation）と交叉（Crossover）による新しいプロンプト候補を生成させます。
3. **Update (更新)**: 発展セット（dev set）での適応度（スコア）に基づいて新しいプロンプトを評価し、集団を更新します。

本論文では、EvoPromptを2つの代表的な進化的アルゴリズムとしてインスタンス化しています。

**1. Genetic Algorithm (GA: 遺伝的アルゴリズム) ベースの実装**:
- ルーレット選択を用い、適応度（スコア）に基づいて親となるプロンプトを選びます。集団数 $N$ における $i$ 番目のプロンプトのスコアを $s_{i}$ とすると、選択確率は以下のようになります。

$$ p_{i} = \frac{ s_{i} }{ \sum_{j=1}^{N} s_{j} } $$

- 交叉と突然変異: LLMを用いて親となる複数のプロンプト同士の特徴を交叉させ、その後ランダムな変更（突然変異）を加えます。これにはLLMに対し、以下のような**メタプロンプト（進化用指示）**を与えて操作を実行させます。
  > **【GAの進化用プロンプトの構造例】**
  > より良いプロンプトを生成するために、以下のステップに段階的に従ってください。
  > 1. 以下のプロンプトを**交叉**し、新しいプロンプトを生成してください： [プロンプト1], [プロンプト2]
  > 2. ステップ1で生成したプロンプトを**突然変異**させ、最終的なプロンプトを <prompt> と </prompt> で囲んで出力してください。
- 更新: 古い集団と新しい集団を同居させ、上位 $N$ 個を次世代として保持します。

**2. Differential Evolution (DE: 差分進化アルゴリズム) ベースの実装**:
- DEの典型的な突然変異は、基本ベクトル $\mathbf{x}$、ランダムな $\mathbf{a}$、および差分ベクトル $\mathbf{b}-\mathbf{c}$ とスケール $F$ を用いて以下のように記述されます。

$$ \mathbf{y} = \mathbf{a} + F(\mathbf{b} - \mathbf{c}) $$

- EvoPromptにおける適用: 上記の差分方程式をLLMのテキスト処理として模倣するため、以下のような**メタプロンプト**を用いて段階的な指示を与えます。
  > **【DEの進化用プロンプトの構造例】**
  > より良いプロンプトを生成するために、以下のステップに段階的に従ってください。
  > 1. プロンプト1とプロンプト2の間の**異なる部分（差分）**を特定してください： [プロンプト1], [プロンプト2] （数式の $\mathbf{b}-\mathbf{c}$ に相当）
  > 2. その異なる部分をランダムに**突然変異**させてください。（数式の $F$ によるスケールに相当）
  > 3. その変異させた差分をプロンプト3と**結合**して、新しいプロンプトを生成してください： [プロンプト3] （数式の $\mathbf{a}$ への加算に相当）
  > 4. ステップ3で生成したプロンプトとベースプロンプトを**交叉**させ、最終的なプロンプトを <prompt> と </prompt> で囲んで出力してください： [ベースプロンプト] （数式の $\mathbf{x}$ との交叉に相当）
- 更新: 生成した候補と元のプロンプトを比較し、より高いスコアを持つ方を次世代へ残します。

## 結果  

EvoPromptは、AlpacaモデルおよびGPT-3.5を使用して、自然言語理解、生成タスク、および難易度の高い BIG-Bench Hard（BBH）など、合計31のデータセットで評価されました。
その結果、自動的に生成されたプロンプトが、人間が設計したプロンプトや、APEやAPOなどの既存の「自動プロンプト最適化手法」を大幅に上回る性能を示しました。具体的にはBBHタスクで最大25％の向上を達成しており、生成されたプロンプト自体が人間にも可読性が高い自然言語で形成されています。総じて、複雑な言語タスクにおいては \mathrm{DE} 型のアルゴリズムが特に有効であることも示されています（Table 12、Figure 3等参照）。

論文内で挙げられている各Figおよび全テーブルの転記は以下の通りです。

![GAのプロセス](./images/ga_cot.png)
（GAプロセスに基づく進化： 親プロンプトを交叉させた上から突然変異させる）

![DEのプロセス](./images/de_cot_v2.png)
（DEプロセスに基づく進化： 2つのプロンプト間の差分を突然変異させ、ベストなものと統合後、交叉する）

![BBHのスコア](./images/bbh.png)
（BBHの複数タスクにおける標準プロンプトからのスコア改善度合。EvoPrompt(DE)が顕著な向上を示す）

![Alpacaの各種ベースライン比較](./images/sst5_subj_asset_3seed.png)

![長さ等のパラメータ分析](./images/len_avg.png)

![バリエーション分析](./images/len_var.png)

![ポピュレーションサイズとの相関](./images/popsize.png)

![APEとの比較分析](./images/ape.png)

![BBHとAPEの比較](./images/bbh_ape.png)

### 論文から抽出された完全なテーブル一覧

以下は論文に記載されているすべての表の正確なデータです。

#### Table 1

| =========================== \textsc{Template for Simplification} =========================== \\ |
|---|
| <PROMPT> |
| <INPUT> |
| The simplification of the sentence is <COMPLETE>\\ |
| **Zero-shot example**: |
| Simplify the text. |
| Subsequently, in February 1941, 600 Jews were sent to Buchenwald and Mauthausen concentration camps. |
| The simplification of the sentence is <COMPLETE>\\ |
| =========================== \textsc{Template for Summarization} =========================== \\ |
| <PROMPT> |
| <INPUT> |
| TL;DR: <COMPLETE>\\ |
| **Zero-shot example**: |
| How would you rephrase that in a few words? |
| Theresa: have you been at Tom's new place? Luis: yes, it's nice Marion: He invited us for a dinner Adam: where is it? Marion: a bit outside the city Adam: where exactly? Marion: Fiesole Luis: very nice! |
| TL;DR: <COMPLETE>\\ |

#### Table 2

| ==========================\textsc{Template for Big-Bench Hard} ==========================\\ |
|---|
| <DESC> |
| Q: <INPUT> |
| A:  <PROMPT> |
| <COMPLETE>\\ |
| **Zero-shot example**: |
| Questions that involve enumerating objects and asking the model to count them. |
| Q: I have a flute, a piano, a trombone, four stoves, a violin, an accordion, a clarinet, a drum, two lamps, and a trumpet. How many musical instruments do I have? |
| A: Let's think step by step. |
| <COMPLETE> |

#### Table 3

| **Task ID** | **Task** | **Description** | **Prompt** | **Score** |
|---|---|---|---|---|
| 01 | hyperbaton | Order adjectives correctly in English sentences. | Verify the answer by splitting it into components and inspecting each part closely and logically, so we can progress thoughtfully and methodically as we break the task into pieces and explore each part systematically and rationally to reach our goal. | 81.20 |
| 02 | temporal\_sequences | Answer questions about which times certain events could have occurred. | Start by breaking this conundrum into manageable chunks, carefully analyzing each component of this problem and thoroughly inspecting each aspect collaboratively, tackling it together progressively to ensure the correct answer and the desired outcome. | 78.80 |
| 03 | object\_counting | Questions that involve enumerating objects and asking the model to count them. | Examine this logically and assess this methodically, so that we can obtain a precise result by thinking critically and dissecting this math task systematically. | 87.60 |
| 04 | disambiguation\_qa | Clarify the meaning of sentences with ambiguous pronouns. | First, let us ponder and start off by taking our time, going step by step, and using our logic to approach this before we dive into the answer. | 71.20 |
| 05 | logical\_deduction\_three\_objects | A logical deduction task which requires deducing the order of a sequence of objects. | Let's approach it cautiously, examining it thoroughly and methodically, and then approach it incrementally towards a resolution. | 94.40 |
| 05 | logical\_deduction\_five\_objects | A logical deduction task which requires deducing the order of a sequence of objects. | Split the problem into steps and thoughtfully progress through them to find the answer after the proof. | 65.20 |
| 05 | logical\_deduction\_seven\_objects | A logical deduction task which requires deducing the order of a sequence of objects. | Let's take a step-by-step approach to systematically dissect this math task. | 54.40 |

#### Table 4

| **Task ID** | **Task** | **Description** | **Prompt** | **Score** |
|---|---|---|---|---|
| 06 | causal\_judgement | Answer questions about causal attribution. | At first, let's handle things cautiously and resolve this by examining every detail and dealing with one problem at a time. | 65.78 |
| 07 | date\_understanding | Infer the date from context. | Be realistic and practical like a detective, and use evidence to solve the problem in a logical, step-by-step approach. | 85.60 |
| 08 | ruin\_names | Select the humorous edit that 'ruins' the input movie or musical artist name. | Break down a math task into smaller sections and solve each one. | 69.60 |
| 09 | word\_sorting | Sort a list of words. | Analyze each part of the problem logically to solve it like a detective. | 56.40 |
| 10 | geometric\_shapes | Name geometric shapes from their SVG paths. | We'll methodically work through this problem together. | 64.00 |
| 11 | movie\_recommendation | Recommend movies similar to the given list of movies. | Before exploring the answer, | 86.00 |
| 12 | salient\_translation\_error\_detection | Detect the type of error in an English translation of a German source sentence. | Break down the problem into individual steps in order to solve it. | 62.80 |
| 13 | formal\_fallacies | Distinguish deductively valid arguments from formal fallacies. | Let's be realistic and evaluate the situation systematically, tackling it gradually. | 56.00 |
| 14 | penguins\_in\_a\_table | Answer questions about a table of penguins and their attributes. | Let's start by taking a rational and organized approach, breaking it down into smaller parts and thinking it through logically, while being realistic and handling it carefully and methodically to ensure the right solution. | 84.25 |
| 15 | dyck\_languages | Correctly close a Dyck-n word. | Let's be realistic and solve this challenge carefully and slowly, taking it slow to complete it correctly, so we can be realistic and cautiously reach the goal. | 44.40 |
| 16 | multistep\_arithmetic\_two | Solve multi-step arithmetic problems. | Before we dive into the answer, | 51.60 |
| 17 | navigate | Given a series of navigation instructions, determine whether one would end up back at the starting point. | Let's logically work together to systematically solve this math problem one step at a time in unison. | 94.20 |
| 18 | reasoning\_about\_colored\_objects | Answer extremely simple questions about the colors of objects on a surface. | Using a detective's mindset, break down each element of this mathematical reasoning challenge one step at a time and reason like a detective to uncover the solution. | 88.00 |
| 19 | boolean\_expressions | Evaluate the result of a random Boolean expression. | Let's gradually unravel this mathematical challenge by methodically addressing it by examining each element and investigating each factor. | 90.80 |
| 20 | tracking\_shuffled\_objects\_three\_objects | A task requiring determining the final positions of a set of objects given their initial positions and a description of a sequence of swaps. | Progress slowly and carefully through this mathematical reasoning challenge one step at a time. | 69.20 |
| 20 | tracking\_shuffled\_objects\_five\_objects | A task requiring determining the final positions of a set of objects given their initial positions and a description of a sequence of swaps. | Using a logical, step-by-step approach, work through this task to find the correct answer. | 81.20 |
| 20 | tracking\_shuffled\_objects\_seven\_objects | A task requiring determining the final positions of a set of objects given their initial positions and a description of a sequence of swaps. | Examine this issue logically and in detail, step-by-step, analyzing each part of the problem one at a time. | 84.80 |
| 21 | sports\_understanding | Determine whether an artificially constructed sentence relating to sports is plausible or not. | Break down the problem into steps and start solving it. | 96.80 |
| 22 | snarks | Determine which of two sentences is sarcastic. | Break down and analyze each part of the problem in a step by step way to ensure the right answer is obtained. | 77.53 |

#### Table 5

| **Method** | **Alpaca** | **GPT-3.5** |
|---|---|---|
|  | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-1 | ROUGE-2 | ROUGE-L |
| MI~[sanh2021multitask] | 35.92 | 11.16 | 31.67 | 43.95 | 17.11 | 39.09 |
| APE~[zhou2022large] | 35.44(0.79) | 10.60(0.38) | 31.80(0.50) | 43.43 | 16.72 | 38.25 |
| **EvoPrompt (GA)** | 38.46(1.45) | 13.36(0.75) | 34.20(1.40) | 45.22 | 18.52 | 41.06 |
| **EvoPrompt (DE)** | **39.46**(0.51) | **13.93**(0.33) | **35.49**(0.56) | **46.49** | **19.49** | **41.96** |

#### Table 6

| \textsc{Instructional Prompts} ============================== \\ |
|---|
| Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\\ |
| $\#\#\#$ Instruction: |
| <PROMPT> \\ |
| $\#\#\#$ Input: |
| <INPUT> \\ |
| $\#\#\#$ Response: |
| <COMPLETE> \\ |
| **Zero-shot Example**: |
| Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\\ |
| $\#\#\#$ Instruction: |
| Please perform Sentiment Classification task. Given the sentence, assign a sentiment label from ['negative', 'positive']. Return label only without any other text. \\ |
| $\#\#\#$ Input: |
| beautifully observed , miraculously unsentimental comedy-drama . \\ |
| $\#\#\#$ Response: |
| <COMPLETE> \\ |

#### Table 7

| **Method** | **Model** | **Content** | **ROUGE-1/2/L** |
|---|---|---|---|
| Manual Instruction | Alpaca-7b | How would you rephrase that in a few words? | 35.92/11.16/31.67 |
|  | GPT | How would you rephrase that in a few words? | 43.95/17.11/39.09 |
| **EvoPrompt** | Alpaca-7b | Carefully examine the text or listen to the conversation to identify the key ideas, comprehend the main idea, and summarize the critical facts and ideas in the concise language without any unnecessary details or duplication. | 39.86/14.24/36.09 |
|  | GPT | Reduce the core by reading or listening carefully to identify the main ideas and key points, so readers can comprehend the important concepts and essential information. | 46.49/19.49/41.96 |

#### Table 8

| **Method** | **Model** | **Content** | **SARI** |
|---|---|---|---|
| Manual Instruction | Alpaca-7b | Simplify the text. | 43.03 |
|  | GPT-3.5 | Simplify the text. | 43.80 |
| **EvoPrompt** | Alpaca-7b | Rewrite the input text into simple English to make it easier to comprehend for non-native English speakers. | 46.67 |
|  | GPT-3.5 | Rewrite the given sentence to make it more accessible and understandable for both native and non-native English speakers. | 47.40 |

#### Table 9

| **Dataset** | **Type** | **Label space** | **|Test|** |
|---|---|---|---|
| SST-2 | Sentiment | {positive, negative} | 1,821 |
| CR | Sentiment | {positive, negative} | 2,000 |
| MR | Sentiment | {positive, negative} | 2,000 |
| SST-5 | Sentiment | {terrible, bad, okay, good, great} | 2,210 |
| AG’s News | News topic | {World, Sports, Business, Tech} | 7,600 |
| TREC | Question topic | {Description, Entity, Expression, Human, Location, Number} | 500 |
| Subj | Subjectivity | {subjective, objective} | 2,000 |
| SAMSum | Summarization | - | 819 |
| ASSET | Simplification | - | 359 |

#### Table 10

| **Dataset** | **Method** | **Content** | **Score** |
|---|---|---|---|
| SST-2 | Manual Instruction | Please perform Sentiment Classification task. Given the sentence, assign a sentiment label from ['negative', 'positive']. Return label only without any other text. | 93.68 |
|  | Natural Instruction | In this task, you are given sentences from movie reviews. The task is to classify a sentence as "great" if the sentiment of the sentence is positive or as "terrible" if the sentiment of the sentence is negative. | 92.86 |
|  | PromptSource | Does the following sentence have a positive or negative sentiment? | 93.03 |
|  | **EvoPrompt** | Examine the movie reviews and classify them as either positive or negative. | 95.61 |
| CR | Manual Instruction | Please perform Sentiment Classification task. Given the sentence, assign a sentiment label from ['negative', 'positive']. Return label only without any other text. | 91.40 |
|  | Natural Instruction | In this task, you are given sentences from movie reviews. The task is to classify a sentence as "great" if the sentiment of the sentence is positive or as "terrible" if the sentiment of the sentence is negative. | 90.90 |
|  | **EvoPrompt** | Analyze customer reviews and categorize each sentence as either 'positive' or 'negative'. | 91.75 |
| MR | Manual Instruction | Please perform Sentiment Classification task. Given the sentence, assign a sentiment label from ['negative', 'positive']. Return label only without any other text. | 88.75 |
|  | Natural Instruction | In this task, you are given sentences from movie reviews. The task is to classify a sentence as "great" if the sentiment of the sentence is positive or as "terrible" if the sentiment of the sentence is negative. | 89.60 |
|  | **EvoPrompt** | Identify if a movie review is positive or negative by accurately categorizing each input-output pair into either 'positive' or 'negative'. | 91.35 |
| SST-5 | Manual Instruction | Please perform Sentiment Classification task. Given the sentence, assign a sentiment label from ['terrible', 'bad', 'okay', 'good', 'great']. Return label only without any other text. | 42.90 |
|  | Natural Instruction | In this task, you are given sentences from movie reviews. Based on the given review, classify it to one of the ﬁve classes: (1) terrible, (2) bad, (3) okay, (4) good, and (5) great. | 48.64 |
|  | **EvoPrompt** | Have your friend evaluate the movie they had just seen and provide a summary opinion (e.g. terrible, bad, okay, good, or great) to determine the sentiment of the movie review. | 52.26 |
| AG's News| Manual Instruction | Please perform News Classification task. Given the news item, assign a label from ['World', 'Sports', 'Business', 'Tech']. Return label only without any other text. | 70.63 |
|  | Natural Instruction | In this task, you are given a news article. Your task is to classify the article to one out of the four topics "World", "Sports", "Business", "Tech" if the article"s main topic is relevant to the world, sports, business, and technology, correspondingly. If you are not sure about the topic, choose the closest option. | 48.89 |
|  | PromptSource | What label best describes this news article? | 45.43 |
|  | **EvoPrompt** | Assess the entire concept of the news story and choose from the World, Sports, Business or Tech categories to categorize it into the correct category. | 76.21 |
| TREC | Manual Instruction | Please perform Question Classification task. Given the question, assign a label from ['Description', 'Entity', 'Expression', 'Human', 'Location', 'Number']. Return label only without any other text. | 50.60 |
|  | Natural Instruction | You are given a question. You need to detect which category better describes the question. Answer with "Description", "Entity", "Expression", "Human", "Location", and "Number". | 55.00 |
|  | PromptSource | Which category best describes the following question? Choose from the following list: Description, Entity, Abbreviation, Person, Quantity, Location. | 36.20 |
|  | **EvoPrompt** | Recognize the inputs (explanations, entities, or humans) and provide the suitable outputs (numbers, descriptions, or entities) to answer the questions in a way that is understandable for non-native English speakers. | 68.00 |
| Subj | Manual Instruction | Please perform Subjectivity Classification task. Given the sentence, assign a label from ['subjective', 'objective']. Return label only without any other text. | 49.75 |
|  | Natural Instruction | In this task, you are given sentences from reviews. The task is to classify a sentence as "subjective" if the opinion of the sentence is subjective or as "objective" if the opinion of the sentence is objective. | 52.55 |
|  | **EvoPrompt** | Construct input-output pairs to demonstrate the subjectivity of reviews and opinions, distinguishing between objective and subjective input while producing examples of personal opinions and illustrations of subjective views, so it can illustrate the subjectivity of judgments and perspectives. | 77.60 |

#### Table 11

| **Method** | **SST-5** | **Subj** |
|---|---|---|
| ***Same iteration*** | APE | EvoPrompt (GA) / EvoPrompt (DE) | APE | EvoPrompt (GA) / EvoPrompt (DE) |
| \# iterations | 9 | 9 / 9 | 15 | 15 / 15 |
| \# tokens | 5.39 M | 5.40 M / 5.52 M | 5.66 M | 5.73 M / 5.93 M |
| score | 45.79 | 50.23 / 49.23 | 67.20 | 70.10 / 79.35 |
| ***Until convergence*** | APE | EvoPrompt (GA) / EvoPrompt (DE) | APE | EvoPrompt (GA) / EvoPrompt (DE) |
| \# iterations | 9 | 7 / 11 | 15 | 15 / 17 |
| \# tokens | 5.39 M | 4.20 M / 6.75 M | 5.66 M | 5.73 M / 6.72 M |
| score | 45.79 | 50.23 / 51.13 | 67.20 | 70.10 / 79.35 |

#### Table 12

| **Method** | **SST-2** | **CR** | **MR** | **SST-5** | **AG's News** | **TREC** | **Subj** | **Avg.** |
|---|---|---|---|---|---|---|---|---|
| MI~[zhang2023sentiment] | 93.68 | **91.40** | 88.75 | 42.90 | 70.63 | 50.60 | 49.75 | 71.07 |
| NI~[naturalinstructions] | 92.86 | 90.90 | 89.60 | 48.64 | 48.89 | 55.00 | 52.55 | 68.21 |
| PromptSource~[bach2022promptsource] | 93.03 | - | - | - | 45.43 | 36.20 | - | - |
| APE~[zhou2022large] | 93.45(0.14) | 91.13(0.45) | 89.98(0.29) | 46.32(0.49) | 71.76(2.81) | 58.73(1.37) | 64.18(0.59) | 73.80 |
| APO~[pryzant2023automatic] | 93.87(0.39) | 91.20(0.04) | 89.85(0.35) | - | - | - | 70.55(1.02) | - |
| **EvoPrompt (GA)** | **95.13**(0.21) | 91.27(0.06) | 90.07(0.25) | **49.91**(0.61) | 72.81(0.61) | **64.00**(0.16) | 70.55(2.58) | 76.25 |
| **EvoPrompt (DE)** | 94.75(0.21) | **91.40**(0.04) | **90.22**(0.09) | 49.89(1.73) | **73.82**(0.35) | 63.73(1.54) | **75.55**(2.26) | **77.05** |

## chokosenlovetiの考察（新規性について）

本論文「EvoPrompt」の新規性と、プロンプト最適化の系譜における位置づけは以下の点に集約されます。

1. **数学的進化モデルの「自然言語（プロンプト）」へのマッピング**
   最も革新的な点は、**「差分進化（DE）」などの高度な数理最適化アルゴリズムを、LLMの自然言語処理能力を介してプロンプト空間に適用したこと**です。特にDEにおいて、本来は数値ベクトルの引き算である「差分（$\mathbf{b}-\mathbf{c}$）」を、「2つのプロンプトの指示の粒度や言い回しの違い（意味的差分）」としてLLMに理解・抽出させ、それを別のプロンプトに加算（結合）させるという発想は、言語モデルのコンテキスト理解力を従来の進化的計算のオペレーターとして見事に昇華させています。

2. **「探索（Exploration）」と「知識活用（Exploitation）」の高度な両立**
   これまでのプロンプト自動最適化手法（APEやProTeGi、OPROなど）は、エラー分析から修正を行う「局所的な改善（Exploitation）」や単純なパラフレーズ生成に留まりがちで、局所解（ある程度良いが最高ではないプロンプト）に陥るリスクがありました。対してEvoPromptは、複数のプロンプトの特徴を掛け合わせる「交叉」と、差分に基づく「変異」を導入することで、広大なプロンプト空間をダイナミックに「探索（Exploration）」しつつ、優秀なプロンプトの構造を「知識活用（Exploitation）」するベストなバランスを自律的に維持できます。

3. **ブラックボックス最適化の新たなパラダイム（LLM as an Evolutionary Operator）**
   勾配情報が完全に不要（API経由のブラックボックスモデルで機能する）でありながら、GrIPSのような単純な編集（単語の置換や削除）ベースの探索よりも遥かに意味論的に高度な検索空間の探索を可能にしています。「LLM自体を、進化的アルゴリズムの『交叉・変異エンジン』として直接組み込む」というパラダイムを強力に実証したマイルストーン的アプローチと言えます。
