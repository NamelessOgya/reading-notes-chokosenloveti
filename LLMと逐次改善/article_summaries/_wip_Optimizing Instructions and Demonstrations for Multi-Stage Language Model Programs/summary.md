# Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs

## 背景
近年、複数のLLM呼び出しをモジュールとして連鎖させる「Language Model (LM) Program」を使って高度なNLPタスクを解く手法が発展している（例: Chain-of-ThoughtやReact等のパイプラインを扱うDSPyなど）。しかし、これらのパイプラインを構築するには、すべてのモジュールで協調して機能するようなプロンプトを手動で調整（プロンプトエンジニアリング）する必要があり、試行錯誤に多大な労力がかかるという問題がある。既存のプロンプト最適化手法（APE、OPRO、EvoPromptなど）は単一プロンプトの最適化には有効だが、モジュールごとの正解ラベルや勾配が手に入らない多段パイプラインに直接適用することは困難であった。
そこで本研究では、この最適化問題を「各モジュールに対する自由記述の指示（Instructions）の最適化」と「Few-Shotデモンストレーション（Demonstrations）の選択」という2つの課題に因数分解し、モジュールごとの正解ラベルなしに行える新しいLLMプログラム最適化アルゴリズム（特にMIPRO）を提案・評価している。

## 手法
本研究では、プログラム全体のスコア $\mu$ を最大化するため、主に以下の戦略を組み合わせたアルゴリズム空間を設計した。

1. **提案（Proposal）戦略**:
   - **Bootstrap Demonstrations**: データセットからランダムに入力をサンプリングし、既存のプログラム $\Phi$ で実行する。最終出力のスコアが高い実行トレースを正解とみなし、その途中のモジュールの入出力をFew-Shotデモンストレーションの候補として利用する。
   - **Grounding Instructions**: LMプロポーザーに対して、データセットの要約やプログラムのコード構造などをコンテキストとして与え、タスクに接地（Grounded）したInstructionを生成させる。
   - **Learning to Propose**: 学習結果を履歴としてLMに保持させる（メタプロンプティング等）か、プロンプト生成関数自体のハイパーパラメータをチューニングする。

2. **クレジット割り当て（Credit Assignment）戦略**:
   多段モジュールの中のどの変数がスコア改善に寄与したかを推定する。
   - **Module-Level Trajectories (O-PRO拡張)**: プログラム全体のスコアが個々のモジュールの品質を代表すると仮定し、モジュールごとに独立した履歴を使ってOPROを実行する（Module-Level OPRO）。
   - **Surrogate Modeling (MIPRO)**: 提案とクレジット割り当てを分離し、Bayesian optimization（ベイズ最適化）を用いて、InstructionとDemonstrationの最適な組み合わせを事後的に探索する（MIPRO: Multi-prompt Instruction Proposal Optimizer）。ミニバッチごとの評価を行うことで効率的な探索と不確実性への頑健性を確保している。

各アルゴリズムやプロンプト例には数式として $\argmax$ などが適用されるが、問題設定の基礎となる評価には以下のような関数と条件が暗黙的に用いられる。

$$ \text{Maximize } \mu(\Phi(x), x') \geq \lambda $$

（ただし $\Phi(x)$ はプログラム出力、$x'$ はメタデータ/最終ラベル、$\lambda$ は足切りしきい値）

## 結果
本研究では、DSPy上で7つの多様なLMプログラムベンチマークを用いて実験を行った。各ベースラインアルゴリズム（0-Shot MIPRO, Bootstrap Random Search, Module-Level OPRO, およびMIPRO）の成績を比較している。

![Motivation](./images/first_page_fig.png)
*(Figure 1: LM Programの最適化問題の枠組み)*

![MIPRO Optimizer](./images/mipro_vertical.png)
*(Figure 4: MIPRO Optimizerの処理フロー。Bayesian Surrogate modelを利用した最適化)*

![ScoNe Plots](./images/ScoNe_plots.png)
*(Figure: ScoNeの最適化スコア結果の遷移)*

実験の結果（**Table 3** 参照）、MIPROは特に「InstructionsとDemonstrationsの同時最適化」において非常に強力であり、7つのベンチマークのうち5つで他のベースラインを超える性能を示した（最大で正解率+13%の改善）。
筆者らの考察として、以下の知見が挙げられる。
- 最も大きな性能ブーストは、しばしば「Few-shotデモンストレーションの最適化」から得られる（Bootstrap RS等で大幅な改善が見られた）。
- ただし、データセットに条件付きのルール（HotpotQA Conditionalなど）が含まれる場合、ルールをLMに反映させるために「Instructionの最適化」が不可欠となる。
- InstructionsとDemonstrationsの双方を同時に最適化するアプローチ（MIPRO）が一般に最良である。
- Bayesian Surrogate Modelのようなサロゲートモデルベースのアプローチは、スコアのノイズ（新たなミニバッチの多様性による変動など）に対してより頑健であり、OPROのような履歴依存のモデルより多段プログラムに適している。

### 論文から抽出された完全なテーブル一覧

論文に記載されている定量評価結果・定性例（タスク別・モデル別）を含むすべてのテーブルです。

#### Table 1
| **Benchmark** | **Train** | **Dev** | **Test** |
|---|---|---|---|
| HotPotQA | 500 | 500 | 2000 |
| HotPotQA Conditional | 500 | 200 | 200 |
| Iris | 75 | N/A | 75 |
| Heart Disease | 120 | N/A | 183 |
| ScoNe | 500 | 500 | 1200 |
| HoVer | 500 | 500 | 1520 |

#### Table 2
| **Benchmark** | **N** |
|---|---|
| 0-Shot MIPRO | HotPotQA | 60 |
|  | HotPotQA Conditional | 35 |
|  | Iris | 50 |
|  | Heart Disease | 30 |
|  | ScoNe | 70 |
|  | HoVer | 15 |
| Bayesian Bootstrap | HotPotQA | 60 |
|  | HotPotQA Conditional | N/A |
|  | Iris | N/A |
|  | Heart Disease | N/A |
|  | ScoNe | 70 |
|  | HoVer | 15 |
| MIPRO | HotPotQA | 30 |
|  | HotPotQA Conditional | 30 |
|  | Iris | 30 |
|  | Heart Disease | 15 |
|  | ScoNe | 70 |
|  | HoVer | 10 |

#### Table 3
| Optimizer | ScoNe | HotPotQA | HoVer | HotPotQA Cond. | Iris | Iris-Typo | Heart Disease |
|---|---|---|---|---|---|---|---|
|  | Train | Dev | Test | Train | Dev | Test | Train | Dev | Test | Train | Dev | Test | Train | Test | Train | Test | Train | Test |
| *Instructions only (0-shot)* |
| N/A | 57.0 | 56.2 | 69.1 | 35.4 | 31.8 | 36.1 | 30.2 | 30.8 | 25.3 | 13.8 | 10.5 | 6 | 46.4 | 40.9 | 34.7 | 32 | 23.3 | 26.8 |
| Module-Level OPRO $-$G | 70.0 | 67.4 | 76.1 | 36.0 | 31.7 | 36.0 | 30.0 | 30.0 | 25.7 | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Module-Level OPRO | 69.1 | 67.6 | 73.5 | 41.9 | 36.2 | 39.0 | 37.1 | 38.6 | 32.5 | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 0-Shot MIPRO | 66.3 | 65.2 | 71.5 | 40.2 | 34.2 | 36.8 | 37.7 | 38.4 | 33.1 | 22.6 | 20.3 | 14.6 | 40.8 | 36.4 | 56.8 | 56.7 | 26.8 | 25.8 |
| 0-Shot MIPRO++ | 69.0 | 66.9 | 75.7 | 41.5 | 36.2 | 39.3 | 37.1 | 37.3 | 32.6 | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| *Demonstrations only (Few-shot)* |
| Bootstrap RS | 74.9 | 69.6 | 75.4 | 48.6 | 44.0 | **45.8** | 42.0 | 42.0 | 37.2 | 16.4 | 15.0 | 10.4 | 95.2 | **94.1** | 58.9 | 58.7 | 78.4 | **79.2** |
| Bayesian Bootstrap | 75.4 | 67.4 | 77.4 | 49.2 | 44.8 | **46.2** | 44.6 | 44.7 | 37.6 | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| *Both (Few-shot)* |
| MIPRO | 74.6 | 69.8 | **79.4** | 49.0 | 43.9 | **46.4** | 44.7 | 46.7 | **39.0** | 28.4 | 28.1 | **23.3** | 98.4 | 88.6 | 69.1 | **68.7** | 75.2 | 74.2 |

#### Table 4
| **Benchmark** | **Task Type** | **Program** | **Modules** | **LM Calls** | **Metric** |
|---|---|---|---|---|---|
| HotPotQA | Multi-Hop QA | Multi-Hop Retrieval | 2 | 3 | Exact Match |
| HotPotQA Conditional | Multi-Hop QA | Multi-Hop Retrieval | 2 | 3 | Custom |
| Iris | Classification | Chain of Thought | 1 | 1 | Accuracy |
| Iris-Typo | Classification | Chain of Thought | 1 | 1 | Accuracy |
| Heart Disease | Classification | Answer Ensemble | 2 | 4 | Accuracy |
| ScoNe | Natural Language Inference | Chain of Thought | 1 | 1 | Exact Match |
| HoVer | Multi-Hop Claim Verify | Multi-Hop Retrieval | 4 | 4 | Recall@21 |

#### Table 5
| **Instructions** | **Trial** | **Score** |
|---|---|---|
| *Baseline* |
| \cline1-3P1: context, question -> answer | 0 | 57.0 |
| *Proposed Instruction at Trial 10* |
| P1: Given a scenario where a patient exhibits symptoms of a high fever, cough, and body aches, prompt the Language Model to determine if we can logically conclude for sure that the patient has contracted the flu. | 10 | 62.2 |
| *Proposed Instruction at Trial 50* |
| P1: Given a scenario where a patient exhibits symptoms of a rare disease and has a family history of similar symptoms, prompt the language model to determine whether we can logically conclude for sure that the patient has inherited the rare disease based on the information provided. | 50 | 57.2 |
| *Proposed Instruction at Trial 330* |
| P1: Given a scenario where a critically ill patient is not responding positively to treatment, and a doctor is considering a risky experimental procedure, prompt the Language Model to determine if it can logically conclude for sure that the doctor is not considering a standard treatment approach. | 330 | 60.2 |
| *Best Proposed Instruction* |
| P1: Given a scenario where a detective is investigating a crime scene, observing a suspect wearing gloves and not leaving fingerprints on a weapon, prompt the Language Model to determine if the suspect can be logically inferred to have committed the crime based on the evidence. | 80 | 65.4 |

#### Table 6
| **Instructions** | **Trial** | **Score** |
|---|---|---|
| *Baseline* |
| \cline1-3P1: Given the fields `context`, `question`, produce the fields `search\_query`. | 0 | 35.4 |
| P2: Given the fields `context`, `question`, produce the fields `answer`. |  |  |
| *Proposed Instruction at Trial 10* |
| P1: Given the fields `context` and `question`, generate a search query for identifying relevant information related to the question. | 10 | 39.0 |
| P2: Given the context passages and a question, generate the correct answer. |  |  |
| *Proposed Instruction at Trial 50* |
| P1: Generate a search query based on the context and question provided. | 50 | 38.2 |
| P2: Given the context passages and a question, generate an answer. |  |  |
| *Proposed Instruction at Trial 330* |
| P1: Given the fields `context`, `question`, generate the search query to find the director of the film whose success, along with An American Tail and The Land Before Time, prompted Steven Spielberg to establish his own animation studio. | 330 | 34.6 |
| P2: Given the context and question, determine the answer by identifying the Finnish former boxer who shares a nickname with a Ugandan political leader and military officer. |  |  |
| *Best Proposed Instruction* |
| P1: Given the fields `context` and `question`, generate a search query for identifying relevant information related to the question. | 10 | 39.0 |
| P2: Given the context passages and a question, generate the correct answer. |  |  |

#### Table 7
| **Instructions** | **Trial** | **Score** |
|---|---|---|
| *Baseline* |
| \cline1-3P1: Given the fields `claim`, `summary\_1`, produce the fields `query`. | 0 | 30.2 |
| P2: Given the fields `claim`, `summary\_1`, `summary\_2`, produce the fields `query`. |  |  |
| P3: Given the fields `claim`, `passages`, produce the fields `summary`. |  |  |
| P4: Given the fields `claim`, `context`, `passages`, produce the fields `summary`. |  |  |
| *Proposed Instruction at Trial 10* |
| P1: Given a claim about a historical event or location and a summary of key details related to the claim, generate a series of specific queries to verify the accuracy of the claim, including details such as original names, purposes, seating capacities, reconstructions, and durations of usage. | 10 | 33.6 |
| P2: Given the fields `claim`, `summary\_1`, `summary\_2`, produce the fields `query`. |  |  |
| P3: Given the crucial need to fact-check claims in real-time news reporting, generate a concise `summary` by processing the `claim` against relevant `passages` to verify the accuracy of the claim and extract essential information. |  |  |
| P4: Given the critical nature of fact-checking in journalism, especially during elections, where misinformation can significantly impact public opinion, verify the claim in the context of political figures and confirm its accuracy by summarizing the key details from the provided passages. |  |  |
| *Proposed Instruction at Trial 30* |
| P1: Given the critical nature of verifying claims in important decision-making processes, use the provided `claim` and `summary\_1` to generate a precise and informative `query` that seeks to confirm or refute the accuracy of the claim in question. | 30 | 32.4 |
| P2: Prompt the LM to generate a query that verifies the accuracy of a claim regarding the stadium where a specific sports team's home games were played, including details such as the original name and purpose of the stadium, seating capacity during a particular event, reconstruction into a new facility, duration of serving as the team's home ballpark, and the correct location of a mentioned Olympic Games. |  |  |
| P3: Given the high stakes scenario where a claim states that a radio station played oldies from artists like Leo Dan and broadcasted in Spanish throughout North America between 1979 and 1995, analyze the provided passages to generate a concise `summary` confirming or refuting the claim. |  |  |
| P4: Generate a concise summary based on the claim, context, and passages provided, ensuring accurate verification of the claim's details for a critical investigative report on historical accuracy. |  |  |
| *Proposed Instruction at Trial 130* |
| P1: Given a claim about a historical event or location and a summary of key details related to the claim, generate a series of specific queries to verify the accuracy of the claim, including details such as original names, purposes, seating capacities, reconstructions, and durations of usage. | 130 | 34.0 |
| P2: Given a scenario where a controversial statement regarding a significant historical event is presented in the claim, along with contradicting summaries in `summary\_1` and `summary\_2`, task the LM to generate a refined query in `query` that delves deeper into the specifics of the claim, seeking to validate or debunk the claim with concrete evidence and details from relevant sources. |  |  |
| P3: Given the fields `claim`, `passages`, produce the fields `summary`. |  |  |
| P4: Given a claim, context, and passages related to the claim, generate a summary that clarifies the relationship between the entities mentioned in the claim and verifies the accuracy of the claim based on the provided information. |  |  |
| *Best Proposed Instruction* |
| P1: Given the fields `claim`, `summary\_1`, produce the fields `query`. | 40 | 35.0 |
| P2: Given the critical need to verify and validate statements on high-stakes topics such as historical events, scientific discoveries, or biographical information, generate a query that effectively assesses the accuracy of claims by synthesizing information from `claim`, `summary\_1`, and `summary\_2` fields to extract relevant details and provide a comprehensive response. |  |  |
| P3: Given the high stakes scenario where a claim states that a radio station played oldies from artists like Leo Dan and broadcasted in Spanish throughout North America between 1979 and 1995, analyze the provided passages to generate a concise `summary` confirming or refuting the claim. |  |  |
| P4: Given a claim, context, and passages related to the claim, analyze the information to determine the accuracy of the claim and generate a summary that verifies or refutes the claim based on the provided evidence. |  |  |

#### Table 8
| **Instructions** | **Trial** | **Score** |
|---|---|---|
| *Baseline* |
| \cline1-3P1: Given the fields `context`, `question`, produce the fields `search\_query`. | 0 | 13.8 |
| P2: When the answer is a person, respond entirely in lowercase.  When the answer is a place, ensure your response contains no punctuation.  When the answer is a date, end your response with “Peace!”.  Never end your response with "Peace!" under other circumstances.  When the answer is none of the above categories respond in all caps. |  |  |
| *Proposed Instruction at Trial 10* |
| P1: Given the critical context of a high-profile criminal investigation, including the suspect's alibi and potential witnesses, and the urgent question of the suspect's whereabouts during the time of the crime, generate a search query that combines the suspect's alibi details and witness statements to determine the suspect's location at the time of the crime. | 10 | 18.6 |
| P2: Given the urgency of a live trivia competition where every answer counts, ensure your response follows the specific formatting rules: When the answer is a person, reply entirely in lowercase. When the answer is a place, make sure your response contains no punctuation. If the answer is a date, conclude your response with “Peace!” without fail. Never end your response with "Peace!" under different circumstances. And when the answer falls outside these categories, reply in all caps. |  |  |
| *Proposed Instruction at Trial 40* |
| P1: Given the context and question about a critical historical event, generate a search query that accurately identifies the key individuals involved in the event and their roles. | 40 | 19.4 |
| P2: When revealing the name of the mysterious undercover agent in the top-secret operation, ensure the identity is concealed in all caps. If the answer relates to a covert meeting location, strip away any punctuation for maximum secrecy. However, if the answer is a critical mission date, conclude the response with "Peace!" to signify the successful operation. Remember, precision is paramount in this mission! |  |  |
| *Proposed Instruction at Trial 190* |
| P1: Please generate a search query for the question: "What is the name of the person who R Lee Ermy played his character in the Prefontaine film and who is also an American track and field coach and co-founder of Nike Inc? | 190 | 20.6 |
| P2: When providing the estimated GDP of the country where the first female Nobel laureate in physics was born, respond in lowercase. For all other categories, ensure your response is in all caps. |  |  |
| *Best Proposed Instruction* |
| P1: Generate a search query based on the context and question provided, focusing on identifying a specific historical figure or event with critical details for accurate retrieval. | 130 | 26.6 |
| P2: When providing the estimated GDP of the country where the first female Nobel laureate in physics was born, respond in lowercase. For all other categories, ensure your response is in all caps. |  |  |

#### Table 9
| **Instructions** | **Trial** | **Score** |
|---|---|---|
| *Baseline* |
| \cline1-3P1: Given the petal and sepal dimensions in cm, predict the iris species. | 0 | 34.7 |
| *Proposed Instruction at Trial 10* |
| P1: Using the provided petal length, petal width, sepal length, and sepal width measurements in cm, predict the iris species accurately to save a critically endangered species from extinction. | 10 | 34.67 |
| *Proposed Instruction at Trial 20* |
| P1: Using the dimensions of a flower with a petal length of 1.8 cm, petal width of 0.3 cm, sepal length of 6.2 cm, and sepal width of 3.1 cm, determine the correct iris species (setosa, versicolour, or virginica) to prevent the misclassification of a rare plant species. | 20 | 37.33 |
| *Proposed Instruction at Trial 60* |
| P1: Given the critical situation in which a rare species of iris is on the brink of extinction, predict the iris species based on the dimensions of the petals and sepals in order to save it from extinction. | 60 | 45.33 |
| *Best Proposed Instruction* |
| P1: Given the critical situation in which a rare species of iris is on the brink of extinction, predict the iris species based on the dimensions of the petals and sepals in order to save it from extinction. | 60 | 45.33 |

#### Table 10
| **Instructions** | **Trial** | **Score** |
|---|---|---|
| *Baseline* |
| \cline1-3P1: Given patient information, predict the presence of heart disease. I can critically assess the provided trainee opinions. | 0 | 23.3 |
| P2: Given patient information, predict the presence of heart disease. |  |  |
| P3: Given patient information, predict the presence of heart disease. |  |  |
| P4: Given patient information, predict the presence of heart disease. |  |  |
| *Proposed Instruction at Trial 10* |
| P1: Given a patient's demographic information, symptoms, and test results, predict if the patient has heart disease. Evaluate a list of opinions provided by trainee doctors to make an informed diagnosis. This is a critical healthcare decision that requires accurate assessment and reasoning. | 10 | 12.5 |
| P2: Given the critical condition of a 50-year-old male patient presenting with typical angina, high blood pressure, elevated cholesterol levels, and multiple vessels colored by fluoroscopy, predict the presence of heart disease. |  |  |
| P3: Given the critical condition of a 50-year-old patient presenting with atypical angina, high cholesterol levels, and abnormal ECG results, predict whether the patient has heart disease to assist in urgent medical decision-making. |  |  |
| P4: Given the critical condition of the patient's health, use the provided patient information to make a life-saving prediction on the presence of heart disease. |  |  |
| *Proposed Instruction at Trial 30* |
| P1: Given a critical situation in the emergency room where time is of the essence, use the patient's age, sex, chest pain type, blood pressure, cholesterol levels, and other relevant factors to predict the presence of heart disease accurately. Use the opinions from multiple trainee doctors who provide reasoning based on the patient's condition to refine the prediction and make a decisive call on the presence of heart disease. | 30 | 10.0 |
| P2: Based on the dataset and the task of predicting the presence of heart disease in patients, prompt the LM with the scenario of a critical care situation where a patient is rushed to the emergency room with symptoms of a possible heart attack. Ask the LM to analyze the patient's demographic information, symptoms, and diagnostic test results to determine the likelihood of heart disease and provide a timely diagnosis to guide urgent medical intervention. |  |  |
| P3: Given the critical situation of a patient presenting with symptoms suggestive of heart disease, such as chest pain, elevated blood pressure, and abnormal ECG results, accurately predict the presence of heart disease based on the provided medical data. |  |  |
| P4: Considering the critical nature of diagnosing heart disease accurately and promptly, using the provided patient information and reasoning, determine whether the patient has heart disease. |  |  |
| *Proposed Instruction at Trial 90* |
| P1: Given patient information, predict the presence of heart disease. I can critically assess the provided trainee opinions. | 90 | 22.5 |
| P2: Given patient information, predict the presence of heart disease. |  |  |
| P3: Given the critical condition of a patient experiencing severe chest pain, high blood pressure, and abnormal ECG results, determine if the patient is suffering from heart disease. |  |  |
| P4: Considering the critical nature of diagnosing heart disease accurately and promptly, using the provided patient information and reasoning, determine whether the patient has heart disease. |  |  |
| *Best Proposed Instruction* |
| P1: Given patient information, predict the presence of heart disease. I can critically assess the provided trainee opinions. | 90 | 22.5 |
| P2: Given patient information, predict the presence of heart disease. |  |  |
| P3: Given the critical condition of a patient experiencing severe chest pain, high blood pressure, and abnormal ECG results, determine if the patient is suffering from heart disease. |  |  |
| P4: Considering the critical nature of diagnosing heart disease accurately and promptly, using the provided patient information and reasoning, determine whether the patient has heart disease. |  |  |
