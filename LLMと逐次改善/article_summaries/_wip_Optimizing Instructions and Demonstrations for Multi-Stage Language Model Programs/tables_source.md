# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[tp]
\begin{center}
\small
\begin{tabular}{lccc}
\toprule
\textbf{Benchmark} & \textbf{Train} & \textbf{Dev} & \textbf{Test} \\ \midrule
HotPotQA & 500 & 500 & 2000 \\
HotPotQA Conditional & 500 & 200 & 200 \\
Iris & 75 & N/A & 75 \\
Heart Disease & 120 & N/A & 183 \\
ScoNe & 500 & 500 & 1200 \\
HoVer & 500 & 500 & 1520 \\
\bottomrule
\end{tabular}
\caption{Train, Dev, Test splits for each of our datasets. Training data was used for training our Optimizers. Dev data was used as a development set to internally iterate on methods. Test was used for final evaluation and reporting. The datset for HotPotQA Conditional is smaller because the labels were created by hand. We do not create a devset for Iris or Heart Disease due to the fact that these were (1) small datasets and (2) we did not use them for method iteration.}
\label{tab:test_train_split}
\end{center}
\end{table}
```

## Table 2
```latex
\begin{table}[tp]
\begin{center}
\small
\begin{tabular}{llc}
\toprule \textbf{Optimizer} &
\textbf{Benchmark} & \textbf{N} \\ \midrule
\multirow{6}{*}{0-Shot MIPRO} & HotPotQA & 60  \\
 & HotPotQA Conditional & 35 \\
 & Iris & 50 \\
 & Heart Disease & 30  \\
 & ScoNe & 70 \\
 & HoVer & 15 \\
 \midrule
\multirow{6}{*}{Bayesian Bootstrap} & HotPotQA & 60  \\
 & HotPotQA Conditional & N/A \\
 & Iris & N/A \\
 & Heart Disease & N/A  \\
 & ScoNe & 70 \\
 & HoVer & 15 \\
 \midrule
\multirow{6}{*}{MIPRO} & HotPotQA & 30  \\
 & HotPotQA Conditional & 30 \\
 & Iris & 30 \\
 & Heart Disease & 15  \\
 & ScoNe & 70 \\
 & HoVer & 10 \\
\bottomrule
\end{tabular}
\caption{Number of candidates per module (N) used for optimization. Note that this hyperparameter only applies to our 0-Shot MIPRO, MIPRO, and Bayesian Bootstraping optimizers, because for other optimizers the \# of candidates explored equals the number of trials.}
\label{tab:opt_hyperparams}
\end{center}
\end{table}
```

## Table 3
```latex
\begin{table*}[h]
\centering
\setlength{\tabcolsep}{1.5pt}
\resizebox{\textwidth}{!}{
\begin{tabular}{>{\centering\arraybackslash}m{4cm} | *{3}{>{\centering\arraybackslash}m{1.0cm}} | *{3}{>{\centering\arraybackslash}m{1.0cm}} | *{3}{>{\centering\arraybackslash}m{1.0cm}} | *{3}{>{\centering\arraybackslash}m{1.0cm}} | *{2}{>{\centering\arraybackslash}m{1.0cm}} | *{2}{>{\centering\arraybackslash}m{1.0cm}} | *{2}{>{\centering\arraybackslash}m{1.0cm}}}
\toprule
Optimizer & \multicolumn{3}{c|}{ScoNe} & \multicolumn{3}{c|}{HotPotQA} & \multicolumn{3}{c|}{HoVer} & \multicolumn{3}{c|}{HotPotQA Cond.} & \multicolumn{2}{c|}{Iris} & \multicolumn{2}{c|}{Iris-Typo} & \multicolumn{2}{c}{Heart Disease} \\
& Train & Dev & Test & Train & Dev & Test & Train & Dev & Test & Train & Dev & Test & Train & Test & Train & Test & Train & Test \\
\midrule
\multicolumn{19}{l}{\textit{Instructions only (0-shot)}} \\
\midrule
N/A & 57.0 & 56.2 & 69.1 & 35.4 & 31.8 & 36.1 & 30.2 & 30.8 & 25.3 & 13.8 & 10.5 & 6 & 46.4 & 40.9 & 34.7 & 32 & 23.3 & 26.8 \\
Module-Level OPRO $-$G & 70.0 & 67.4 & 76.1 & 36.0 & 31.7 & 36.0 & 30.0 & 30.0 & 25.7 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
Module-Level OPRO & 69.1 & 67.6 & 73.5 & 41.9 & 36.2 & 39.0 & 37.1 & 38.6 & 32.5 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
0-Shot MIPRO & 66.3 & 65.2 & 71.5 & 40.2 & 34.2 & 36.8 & 37.7 & 38.4 & 33.1 & 22.6 & 20.3 & 14.6 & 40.8 & 36.4 & 56.8 & 56.7 & 26.8 & 25.8 \\
0-Shot MIPRO++ & 69.0 & 66.9 & 75.7 & 41.5 & 36.2 & 39.3 & 37.1 & 37.3 & 32.6 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
\midrule
\multicolumn{19}{l}{\textit{Demonstrations only (Few-shot)}} \\
\midrule
Bootstrap RS & 74.9 & 69.6 & 75.4 & 48.6 & 44.0 & \textbf{45.8} & 42.0 & 42.0 & 37.2 & 16.4 & 15.0 & 10.4 & 95.2 & \textbf{94.1} & 58.9 & 58.7 & 78.4 & \textbf{79.2} \\
Bayesian Bootstrap & 75.4 & 67.4  & 77.4  & 49.2 & 44.8 & \textbf{46.2} & 44.6 & 44.7 & 37.6 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
\midrule
\multicolumn{19}{l}{\textit{Both (Few-shot)}} \\
\midrule
MIPRO & 74.6 & 69.8 & \textbf{79.4} & 49.0 & 43.9 & \textbf{46.4} & 44.7 & 46.7 & \textbf{39.0} & 28.4 & 28.1 & \textbf{23.3} & 98.4 & 88.6 & 69.1 & \textbf{68.7} & 75.2 & 74.2 \\
\bottomrule
\end{tabular}}
\caption{Results averaged across 5 runs, divided into optimizing instructions only (i.e., ``0-shot'' prompts), demonstrations only, and both. The best performing values in each column are highlighted in bold. These bold values represent the highest average scores compared to the second-highest, with significance supported by Wilcoxon signed-rank tests (p < .05) between the corresponding run averages. If significance is not confirmed, multiple results are bolded to denote their comparable performance.}
\vspace{-3mm}
\label{table:performance_comparison}
\end{table*}
```

## Table 4
```latex
\begin{table*}[tp]
\begin{center}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lllccl}
\toprule
\textbf{Benchmark} & \textbf{Task Type} & \textbf{Program} & \textbf{Modules} & \textbf{LM Calls} & \textbf{Metric} \\ \midrule
HotPotQA & Multi-Hop QA & Multi-Hop Retrieval & 2 & 3 & Exact Match \\
HotPotQA Conditional & Multi-Hop QA & Multi-Hop Retrieval & 2 & 3 & Custom \\
Iris & Classification & Chain of Thought & 1 & 1 & Accuracy \\
Iris-Typo & Classification & Chain of Thought & 1 & 1 & Accuracy \\
Heart Disease & Classification & Answer Ensemble & 2 & 4 & Accuracy \\
ScoNe & Natural Language Inference & Chain of Thought & 1 & 1 & Exact Match \\
HoVer & Multi-Hop Claim Verify & Multi-Hop Retrieval & 4 & 4 & Recall@21 \\
\bottomrule
\end{tabular}
}
\caption{DSPy Optimizer Benchmark and associated programs. We benchmark our optimizers on seven diverse programs. Additional details are in Appendices~\ref{sec:task_desc} and~\ref{sec:lm-program-appendix}.}
\label{tab:optimizer-benchmark}
\end{center}
\end{table*}
```

## Table 5
```latex
\begin{table*}[ht]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{Xcc}
\hline
\textbf{Instructions} & \textbf{Trial} & \textbf{Score} \\ \hline
\cline{1-3}
\textit{Baseline} \\
\cline{1-3}P1: context, question -> answer & \multirow{1}{*}{0} & \multirow{1}{*}{57.0} \\
\cline{1-3}

\textit{Proposed Instruction at Trial 10} \\
\cline{1-3}
P1: Given a scenario where a patient exhibits symptoms of a high fever, cough, and body aches, prompt the Language Model to determine if we can logically conclude for sure that the patient has contracted the flu. & \multirow{1}{*}{10} & \multirow{1}{*}{62.2} \\
\cline{1-3}

\textit{Proposed Instruction at Trial 50} \\
\cline{1-3}
P1: Given a scenario where a patient exhibits symptoms of a rare disease and has a family history of similar symptoms, prompt the language model to determine whether we can logically conclude for sure that the patient has inherited the rare disease based on the information provided. & \multirow{1}{*}{50} & \multirow{1}{*}{57.2} \\
\cline{1-3}

\textit{Proposed Instruction at Trial 330} \\
\cline{1-3}
P1: Given a scenario where a critically ill patient is not responding positively to treatment, and a doctor is considering a risky experimental procedure, prompt the Language Model to determine if it can logically conclude for sure that the doctor is not considering a standard treatment approach. & \multirow{1}{*}{330} & \multirow{1}{*}{60.2} \\
\cline{1-3}

\textit{Best Proposed Instruction} \\
\cline{1-3}
P1: Given a scenario where a detective is investigating a crime scene, observing a suspect wearing gloves and not leaving fingerprints on a weapon, prompt the Language Model to determine if the suspect can be logically inferred to have committed the crime based on the evidence. & \multirow{1}{*}{80} & \multirow{1}{*}{65.4} \\
\cline{1-3}

\hline
\end{tabularx}
\caption{ScoNe Prompt Progression}
\label{table:ScoNe_prompt_progression}
\end{table*}
```

## Table 6
```latex
\begin{table*}[ht]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{Xcc}
\hline
\textbf{Instructions} & \textbf{Trial} & \textbf{Score} \\ \hline
\cline{1-3}
\textit{Baseline} \\
\cline{1-3}P1: Given the fields `context`, `question`, produce the fields `search\_query`. & \multirow{2}{*}{0} & \multirow{2}{*}{35.4} \\
P2: Given the fields `context`, `question`, produce the fields `answer`. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 10} \\
\cline{1-3}
P1: Given the fields `context` and `question`, generate a search query for identifying relevant information related to the question. & \multirow{2}{*}{10} & \multirow{2}{*}{39.0} \\
P2: Given the context passages and a question, generate the correct answer. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 50} \\
\cline{1-3}
P1: Generate a search query based on the context and question provided. & \multirow{2}{*}{50} & \multirow{2}{*}{38.2} \\
P2: Given the context passages and a question, generate an answer. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 330} \\
\cline{1-3}
P1: Given the fields `context`, `question`, generate the search query to find the director of the film whose success, along with An American Tail and The Land Before Time, prompted Steven Spielberg to establish his own animation studio. & \multirow{2}{*}{330} & \multirow{2}{*}{34.6} \\
P2: Given the context and question, determine the answer by identifying the Finnish former boxer who shares a nickname with a Ugandan political leader and military officer. & & \\
\cline{1-3}

\textit{Best Proposed Instruction} \\
\cline{1-3}
P1: Given the fields `context` and `question`, generate a search query for identifying relevant information related to the question. & \multirow{2}{*}{10} & \multirow{2}{*}{39.0} \\
P2: Given the context passages and a question, generate the correct answer. & & \\
\cline{1-3}

\hline
\end{tabularx}
\caption{HotpotQA Prompt Progression}
\label{table:HotpotQA_prompt_progression}
\end{table*}
```

## Table 7
```latex
\begin{table*}[ht]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{Xcc}
\hline
\textbf{Instructions} & \textbf{Trial} & \textbf{Score} \\ \hline
\cline{1-3}
\textit{Baseline} \\
\cline{1-3}P1: Given the fields `claim`, `summary\_1`, produce the fields `query`. & \multirow{4}{*}{0} & \multirow{4}{*}{30.2} \\
P2: Given the fields `claim`, `summary\_1`, `summary\_2`, produce the fields `query`. & & \\
P3: Given the fields `claim`, `passages`, produce the fields `summary`. & & \\
P4: Given the fields `claim`, `context`, `passages`, produce the fields `summary`. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 10} \\
\cline{1-3}
P1: Given a claim about a historical event or location and a summary of key details related to the claim, generate a series of specific queries to verify the accuracy of the claim, including details such as original names, purposes, seating capacities, reconstructions, and durations of usage. & \multirow{4}{*}{10} & \multirow{4}{*}{33.6} \\
P2: Given the fields `claim`, `summary\_1`, `summary\_2`, produce the fields `query`. & & \\
P3: Given the crucial need to fact-check claims in real-time news reporting, generate a concise `summary` by processing the `claim` against relevant `passages` to verify the accuracy of the claim and extract essential information. & & \\
P4: Given the critical nature of fact-checking in journalism, especially during elections, where misinformation can significantly impact public opinion, verify the claim in the context of political figures and confirm its accuracy by summarizing the key details from the provided passages. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 30} \\
\cline{1-3}
P1: Given the critical nature of verifying claims in important decision-making processes, use the provided `claim` and `summary\_1` to generate a precise and informative `query` that seeks to confirm or refute the accuracy of the claim in question. & \multirow{4}{*}{30} & \multirow{4}{*}{32.4} \\
P2: Prompt the LM to generate a query that verifies the accuracy of a claim regarding the stadium where a specific sports team's home games were played, including details such as the original name and purpose of the stadium, seating capacity during a particular event, reconstruction into a new facility, duration of serving as the team's home ballpark, and the correct location of a mentioned Olympic Games. & & \\
P3: Given the high stakes scenario where a claim states that a radio station played oldies from artists like Leo Dan and broadcasted in Spanish throughout North America between 1979 and 1995, analyze the provided passages to generate a concise `summary` confirming or refuting the claim. & & \\
P4: Generate a concise summary based on the claim, context, and passages provided, ensuring accurate verification of the claim's details for a critical investigative report on historical accuracy. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 130} \\
\cline{1-3}
P1: Given a claim about a historical event or location and a summary of key details related to the claim, generate a series of specific queries to verify the accuracy of the claim, including details such as original names, purposes, seating capacities, reconstructions, and durations of usage. & \multirow{4}{*}{130} & \multirow{4}{*}{34.0} \\
P2: Given a scenario where a controversial statement regarding a significant historical event is presented in the claim, along with contradicting summaries in `summary\_1` and `summary\_2`, task the LM to generate a refined query in `query` that delves deeper into the specifics of the claim, seeking to validate or debunk the claim with concrete evidence and details from relevant sources. & & \\
P3: Given the fields `claim`, `passages`, produce the fields `summary`. & & \\
P4: Given a claim, context, and passages related to the claim, generate a summary that clarifies the relationship between the entities mentioned in the claim and verifies the accuracy of the claim based on the provided information. & & \\
\cline{1-3}

\textit{Best Proposed Instruction} \\
\cline{1-3}
P1: Given the fields `claim`, `summary\_1`, produce the fields `query`. & \multirow{4}{*}{40} & \multirow{4}{*}{35.0} \\
P2: Given the critical need to verify and validate statements on high-stakes topics such as historical events, scientific discoveries, or biographical information, generate a query that effectively assesses the accuracy of claims by synthesizing information from `claim`, `summary\_1`, and `summary\_2` fields to extract relevant details and provide a comprehensive response. & & \\
P3: Given the high stakes scenario where a claim states that a radio station played oldies from artists like Leo Dan and broadcasted in Spanish throughout North America between 1979 and 1995, analyze the provided passages to generate a concise `summary` confirming or refuting the claim. & & \\
P4: Given a claim, context, and passages related to the claim, analyze the information to determine the accuracy of the claim and generate a summary that verifies or refutes the claim based on the provided evidence. & & \\
\cline{1-3}

\hline
\end{tabularx}
\caption{HoVeR Prompt Progression}
\label{table:HoVeR_prompt_progression}
\end{table*}
```

## Table 8
```latex
\begin{table*}[ht]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{Xcc}
\hline
\textbf{Instructions} & \textbf{Trial} & \textbf{Score} \\ \hline
\cline{1-3}
\textit{Baseline} \\
\cline{1-3}P1: Given the fields `context`, `question`, produce the fields `search\_query`. & \multirow{2}{*}{0} & \multirow{2}{*}{13.8} \\
P2: When the answer is a person, respond entirely in lowercase.  When the answer is a place, ensure your response contains no punctuation.  When the answer is a date, end your response with “Peace!”.  Never end your response with "Peace!" under other circumstances.  When the answer is none of the above categories respond in all caps. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 10} \\
\cline{1-3}
P1: Given the critical context of a high-profile criminal investigation, including the suspect's alibi and potential witnesses, and the urgent question of the suspect's whereabouts during the time of the crime, generate a search query that combines the suspect's alibi details and witness statements to determine the suspect's location at the time of the crime. & \multirow{2}{*}{10} & \multirow{2}{*}{18.6} \\
P2: Given the urgency of a live trivia competition where every answer counts, ensure your response follows the specific formatting rules: When the answer is a person, reply entirely in lowercase. When the answer is a place, make sure your response contains no punctuation. If the answer is a date, conclude your response with “Peace!” without fail. Never end your response with "Peace!" under different circumstances. And when the answer falls outside these categories, reply in all caps. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 40} \\
\cline{1-3}
P1: Given the context and question about a critical historical event, generate a search query that accurately identifies the key individuals involved in the event and their roles. & \multirow{2}{*}{40} & \multirow{2}{*}{19.4} \\
P2: When revealing the name of the mysterious undercover agent in the top-secret operation, ensure the identity is concealed in all caps. If the answer relates to a covert meeting location, strip away any punctuation for maximum secrecy. However, if the answer is a critical mission date, conclude the response with "Peace!" to signify the successful operation. Remember, precision is paramount in this mission! & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 190} \\
\cline{1-3}
P1: Please generate a search query for the question: "What is the name of the person who R Lee Ermy played his character in the Prefontaine film and who is also an American track and field coach and co-founder of Nike Inc? & \multirow{2}{*}{190} & \multirow{2}{*}{20.6} \\
P2: When providing the estimated GDP of the country where the first female Nobel laureate in physics was born, respond in lowercase. For all other categories, ensure your response is in all caps. & & \\
\cline{1-3}

\textit{Best Proposed Instruction} \\
\cline{1-3}
P1: Generate a search query based on the context and question provided, focusing on identifying a specific historical figure or event with critical details for accurate retrieval. & \multirow{2}{*}{130} & \multirow{2}{*}{26.6} \\
P2: When providing the estimated GDP of the country where the first female Nobel laureate in physics was born, respond in lowercase. For all other categories, ensure your response is in all caps. & & \\
\cline{1-3}

\hline
\end{tabularx}
\caption{HotPotQA Conditional Prompt Progression}
\label{table:HotPotQA Conditional_prompt_progression}
\end{table*}
```

## Table 9
```latex
\begin{table*}[ht]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{Xcc}
\hline
\textbf{Instructions} & \textbf{Trial} & \textbf{Score} \\ \hline
\cline{1-3}
\textit{Baseline} \\
\cline{1-3}P1: Given the petal and sepal dimensions in cm, predict the iris species. & \multirow{1}{*}{0} & \multirow{1}{*}{34.7} \\
\cline{1-3}

\textit{Proposed Instruction at Trial 10} \\
\cline{1-3}
P1: Using the provided petal length, petal width, sepal length, and sepal width measurements in cm, predict the iris species accurately to save a critically endangered species from extinction. & \multirow{1}{*}{10} & \multirow{1}{*}{34.67} \\
\cline{1-3}

\textit{Proposed Instruction at Trial 20} \\
\cline{1-3}
P1: Using the dimensions of a flower with a petal length of 1.8 cm, petal width of 0.3 cm, sepal length of 6.2 cm, and sepal width of 3.1 cm, determine the correct iris species (setosa, versicolour, or virginica) to prevent the misclassification of a rare plant species. & \multirow{1}{*}{20} & \multirow{1}{*}{37.33} \\
\cline{1-3}

\textit{Proposed Instruction at Trial 60} \\
\cline{1-3}
P1: Given the critical situation in which a rare species of iris is on the brink of extinction, predict the iris species based on the dimensions of the petals and sepals in order to save it from extinction. & \multirow{1}{*}{60} & \multirow{1}{*}{45.33} \\
\cline{1-3}

\textit{Best Proposed Instruction} \\
\cline{1-3}
P1: Given the critical situation in which a rare species of iris is on the brink of extinction, predict the iris species based on the dimensions of the petals and sepals in order to save it from extinction. & \multirow{1}{*}{60} & \multirow{1}{*}{45.33} \\
\cline{1-3}

\hline
\end{tabularx}
\caption{Iris-Typo Prompt Progression}
\label{table:Iris_prompt_progression}
\end{table*}
```

## Table 10
```latex
\begin{table*}[ht]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{Xcc}
\hline
\textbf{Instructions} & \textbf{Trial} & \textbf{Score} \\ \hline
\cline{1-3}
\textit{Baseline} \\
\cline{1-3}P1: Given patient information, predict the presence of heart disease. I can critically assess the provided trainee opinions. & \multirow{4}{*}{0} & \multirow{4}{*}{23.3} \\
P2: Given patient information, predict the presence of heart disease. & & \\
P3: Given patient information, predict the presence of heart disease. & & \\
P4: Given patient information, predict the presence of heart disease. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 10} \\
\cline{1-3}
P1: Given a patient's demographic information, symptoms, and test results, predict if the patient has heart disease. Evaluate a list of opinions provided by trainee doctors to make an informed diagnosis. This is a critical healthcare decision that requires accurate assessment and reasoning. & \multirow{4}{*}{10} & \multirow{4}{*}{12.5} \\
P2: Given the critical condition of a 50-year-old male patient presenting with typical angina, high blood pressure, elevated cholesterol levels, and multiple vessels colored by fluoroscopy, predict the presence of heart disease. & & \\
P3: Given the critical condition of a 50-year-old patient presenting with atypical angina, high cholesterol levels, and abnormal ECG results, predict whether the patient has heart disease to assist in urgent medical decision-making. & & \\
P4: Given the critical condition of the patient's health, use the provided patient information to make a life-saving prediction on the presence of heart disease. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 30} \\
\cline{1-3}
P1: Given a critical situation in the emergency room where time is of the essence, use the patient's age, sex, chest pain type, blood pressure, cholesterol levels, and other relevant factors to predict the presence of heart disease accurately. Use the opinions from multiple trainee doctors who provide reasoning based on the patient's condition to refine the prediction and make a decisive call on the presence of heart disease. & \multirow{4}{*}{30} & \multirow{4}{*}{10.0} \\
P2: Based on the dataset and the task of predicting the presence of heart disease in patients, prompt the LM with the scenario of a critical care situation where a patient is rushed to the emergency room with symptoms of a possible heart attack. Ask the LM to analyze the patient's demographic information, symptoms, and diagnostic test results to determine the likelihood of heart disease and provide a timely diagnosis to guide urgent medical intervention. & & \\
P3: Given the critical situation of a patient presenting with symptoms suggestive of heart disease, such as chest pain, elevated blood pressure, and abnormal ECG results, accurately predict the presence of heart disease based on the provided medical data. & & \\
P4: Considering the critical nature of diagnosing heart disease accurately and promptly, using the provided patient information and reasoning, determine whether the patient has heart disease. & & \\
\cline{1-3}

\textit{Proposed Instruction at Trial 90} \\
\cline{1-3}
P1: Given patient information, predict the presence of heart disease. I can critically assess the provided trainee opinions. & \multirow{4}{*}{90} & \multirow{4}{*}{22.5} \\
P2: Given patient information, predict the presence of heart disease. & & \\
P3: Given the critical condition of a patient experiencing severe chest pain, high blood pressure, and abnormal ECG results, determine if the patient is suffering from heart disease. & & \\
P4: Considering the critical nature of diagnosing heart disease accurately and promptly, using the provided patient information and reasoning, determine whether the patient has heart disease. & & \\
\cline{1-3}

\textit{Best Proposed Instruction} \\
\cline{1-3}
P1: Given patient information, predict the presence of heart disease. I can critically assess the provided trainee opinions. & \multirow{4}{*}{90} & \multirow{4}{*}{22.5} \\
P2: Given patient information, predict the presence of heart disease. & & \\
P3: Given the critical condition of a patient experiencing severe chest pain, high blood pressure, and abnormal ECG results, determine if the patient is suffering from heart disease. & & \\
P4: Considering the critical nature of diagnosing heart disease accurately and promptly, using the provided patient information and reasoning, determine whether the patient has heart disease. & & \\
\cline{1-3}

\hline
\end{tabularx}
\caption{Heart Disease Prompt Progression}
\label{table:Heart_Disease_prompt_progression}
\end{table*}
```

