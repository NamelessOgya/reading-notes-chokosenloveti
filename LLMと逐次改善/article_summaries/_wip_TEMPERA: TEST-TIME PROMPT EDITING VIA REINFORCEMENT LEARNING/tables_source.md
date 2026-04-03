# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
\caption{Effect of different editing techniques. For instruction, we tokenize it into phrases and perform swapping, addition or deletion. We also allow swapping in-context exemplars or changing different verbalizers.}
\scriptsize
\setlength\tabcolsep{3.5pt}
\label{tab:act_example}
\centering
\begin{tabular}{ll cc}
% {lcccccccccccc}
\toprule
& & Before Editing & After Editing \\ 
\midrule  
\multirow{3}{*}{Instruction} & Swap & ``Given text, classify whether it is good or bad." & ``Classify whether it is good or bad, given text."\\
& Add  & ``Given text, classify whether it is good or bad." & ``Given text, given text, Classify whether it is good or bad."\\
& Delete  & ``Given text, classify whether it is good or bad." & ``Classify whether it is good or bad."\\
\midrule
\multirow{2}{*}{Example} & Permute & \{Example $1$, Example $2$, ..., Example $k$ \} & \{Example $k$, Example $3$, ..., Example $1$ \} \\
& Swap  & \{Example $1$, Example $2$, ..., Example $k$ \} & \{Example $k+1$, Example $n$, ..., Example $1$ \}\\
\midrule
\multirow{1}{*}{Verbalizer} & Change & \{ ``positive", ``negative"\} & \{``great", ``terrible"\}\\
\bottomrule 
\end{tabular}
\end{table*}
```

## Table 2
```latex
\begin{table*}[h]
\small
% TODO: Remove if we are short of space
\renewcommand{\arraystretch}{1.2}
\caption{Few-shot classification results. We compare against different baselines in this setting. Results show that \ours{} surpasses various baselines including finetuning, prompt tuning and discrete prompt search. The standard deviations are shown in brackets.}
\setlength\tabcolsep{3.5pt}
\label{tab:few_shot}
\centering
\begin{tabular}{ll ccccc}
% {lcccccccccccc}
\toprule
& & SST-2 & Yelp P. & MR & CR & AG News \\ 
\midrule  
\multirow{1}{*}{Finetuning} & Finetuning (few-shot) & 80.6 (3.9) & 88.7 (4.7) & 67.4 (9.7) & 73.3 (7.5) & 84.9 (3.6)\\
\midrule
\multirow{3}{*}{Continuous Prompt} & Soft Prompt Tuning & 73.8 (10.9) & 88.6 (2.1) & 74.1 (14.6) & 75.9 (11.8) & 82.6 (0.9)\\
& Black-Box Tuning & 89.1 (0.9) & 93.2 (0.5) & 86.6 (1.3) & 87.4 (1.0) & 83.5 (0.9)\\
& AutoPrompt & 75.0 (7.6) & 79.8 (8.3) & 62.0 (0.8) & 57.5 (5.8) & 65.7 (1.9)\\
\midrule
\multirow{5}{*}{Discrete Prompt} & Manual Prompt & 82.8 & 83.0 & 80.9 & 79.6 & 76.9\\
& In-Context Demo. &  85.9 (0.7) & 89.6 (0.4) & 80.6 (1.4) & 85.5 (1.5) & 74.9 (0.8)\\
& Instructions & 89.0 & 84.4 & 85.2 & 80.8 & 54.8\\
& GrIPS & 87.1 (1.5) & 88.2 (0.1) & 86.1 (0.3) & 80.0 (2.5) & 65.4 (9.8)\\
& RLPrompt & 90.1 (1.8) & \textbf{93.9 (1.8)} & 86.7 (2.4) & 87.2 (1.7) & 77.2 (2.0)\\
\midrule
\multirow{1}{*}{Discrete Prompt} & \ours{} (ours) & \textbf{91.9} (2.0) & 92.6 (1.7) & \textbf{88.0} (1.1) & \textbf{91.1} (1.6) & \textbf{85.5} (1.5)\\
\bottomrule 
\end{tabular}

\end{table*}
```

## Table 3
```latex
\begin{table*}[h]
\begin{minipage}{.49\textwidth}
% TODO: Remove if we are short of space
\renewcommand{\arraystretch}{1.2}
\caption{We compare our method against different methods which do not perform test-time editing. Results show that test-time editing is mostly helpful in harder tasks like AG News.}
% , while easier tasks might not benefit from it.}
\setlength\tabcolsep{3.5pt}
\label{tab:test_time_edit}
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{l ccc}
% {lcccccccccccc}
\toprule
& SST-2 & MR & AG News \\ 
\midrule  
Manual Prompt & 82.8 & 80.9 & 76.9 \\
In-Context Demo. & 85.9 & 80.6 & 74.9 \\
Instructions & 89.0 & 85.2 & 54.8 \\
GrIPS & 87.1 & 87.1 & 65.4 \\
\ours{} (No TTE) & \textbf{92.0} & 87.4 & 81.3 \\
\midrule
\ours & 91.9 & \textbf{88.2} & \textbf{84.3} \\
\bottomrule 
\end{tabular}
}
\end{minipage}
\hspace{0.05in}
% \end{table*}
```

## Table 4
```latex
\begin{table*}[h]
% TODO: Remove if we are short of space
\begin{minipage}{.49\textwidth}
\renewcommand{\arraystretch}{1.2}
\vspace{-3em}
\caption{Ablation on different editing techniques. Results show that adding verbalizer-edits helps all the tasks (especially MR and AG News). Adding instruction-edits marginally helps the performance in SST-2 and MR. }
\setlength\tabcolsep{3.5pt}
\label{tab:techniques}
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{l ccc}
% {lcccccccccccc}
\toprule
& SST-2 & MR & AG News \\ 
\midrule  
\ours{} (No Inst \& Verb) & 91.2 & 87.2 & 82.2 \\
\ours{} (No Inst) & 91.9 & 88.2 & 84.3 \\
\ours{} & \textbf{92.4} & \textbf{88.4} & \textbf{85.5} \\
\bottomrule 
\end{tabular}
}
\end{minipage}
\end{table*}
```

## Table 5
```latex
\begin{table*}[h]
\vspace{-3em}
\caption{Qualitative results on the effect of the learned policy. We see that our method both enables the flexibility of various edits and interpretability of the final results. On the contrary, many prior methods produce non-readable prompts. Red text is prior to editing and blue text are the changes.}
\scriptsize
\setlength\tabcolsep{3.5pt}
\label{tab:examples}
\centering
\begin{tabular}{p{1.1cm}p{1.2cm}p{10.8cm}}
% {lcccccccccccc}
\toprule
\multirow{2}{*}{SST-2} & Before Edit & ``In this task, you are given sentences from movie reviews. The task is to classify a sentence as ``\textcolor{red}{positive}" if the sentiment of the sentence is positive or as ``\textcolor{red}{negative}" if the sentiment of the sentence is negative. Review: of saucy. Sentiment: \textcolor{red}{positive}. Review: cold movie. Sentiment: \textcolor{red}{negative}. Review: heroes. Sentiment: $<$mask$>$." \\
& After Edit \textit{(better verbalizer)} & ``In this task, you are given sentences from movie reviews. The task is to classify a sentence as "\textcolor{blue}{great}" if the sentiment of the sentence is positive or as ``\textcolor{blue}{terrible}" if the sentiment of the sentence is negative. Review: of saucy. Sentiment: \textcolor{blue}{great}. Review: cold movie. Sentiment: \textcolor{blue}{terrible}. Review: heroes. Sentiment: $<$mask$>$."\\
\midrule
\multirow{2}{*}{AG News} & Before Edit & ``Classify the news articles into the categories of World, Sports, Business, and Technology. Article: \textcolor{red}{What's in a Name? Well, Matt Is Sexier Than Paul (Reuters) Reuters - As Shakespeare said, a rose by any other name would smell as sweet. Right? Answer: Technology.} Article: Wall St. Bears Claw Back Into the Black (Reuters) Reuters - Short-sellers, Wall Street's dwindling band of ultra-cynics, are seeing green again. Answer: $<$mask$>$."\\
& After Edit \textit{(better exemplar selection)} &  ``Classify the news articles into the categories of World, Sports, Business, and Technology. Article: \textcolor{blue}{Expansion slows in Japan Economic growth in Japan slows down as the country experiences a drop in domestic and corporate spending. Answer: Business.} Article: Wall St. Bears Claw Back Into the Black (Reuters) Reuters - Short-sellers, Wall Street's dwindling band of ultra-cynics, are seeing green again. Answer: $<$mask$>$."\\
\bottomrule 
\end{tabular}
\end{table*}
```

## Table 6
```latex
\begin{table*}[!tb]
% TODO: Remove if we are short of space
% \renewcommand{\arraystretch}{1.2}
% \parbox{.40\linewidth}{
\begin{minipage}{.49\textwidth}
\caption{Ablation on the number of in-context exemplars. Results show that increasing the number of examples results in a consistent increase of performance except for AG News (which is due to the length limit).}
% \setlength\tabcolsep{3.5pt}
\label{tab:in_context_size}
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{l ccc}
% {lcccccccccccc}
\toprule
& SST-2 & MR & AG News \\ 
\midrule  
\ours{} (2 Examples) & 91.6 & 87.9 & 84.0 \\
\ours{} (4 Examples) & 91.9 & 88.2 & \textbf{84.3} \\
\ours{} (8 Examples) & \textbf{92.4} & \textbf{88.4} & 82.2 \\
\bottomrule 
\end{tabular}
}
\end{minipage}
% \end{table*}
```

## Table 7
```latex
\begin{table*}[h]
\begin{minipage}{.49\textwidth}
% \parbox{.40\textwidth}{
% TODO: Remove if we are short of space
% \renewcommand{\arraystretch}{1.2}
\caption{Ablation on the size of the prompt pool to select from. We see that the performance does not change too much when changing the size of the pool,  indicating that the performance is relatively stable. }
% \setlength\tabcolsep{3.5pt}
\label{tab:pool_size}
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{lccc}
% {lcccccccccccc}
\toprule
& SST-2 & MR & AG News \\ 
\midrule  
\ours{} (Pool Size 8) & 91.6 & 87.9 & 84.1 \\
\ours{} (Pool Size 16) & 91.9 & 88.2 & 84.3 \\
\ours{} (Pool Size 32) & \textbf{92.2} & \textbf{88.4} & \textbf{84.7} \\
\bottomrule 
\end{tabular}
}
\end{minipage}
\end{table*}
```

## Table 8
```latex
\begin{table*}[h]
\caption{Hyperparameters used for \ours{} in all the tasks.}
% \vspace{-10pt}
% \footnotesize
\setlength\tabcolsep{4.0pt}
\label{tab:hyper_params_appendix}
\centering
\begin{tabular}{p{6cm}p{4cm}p{5cm}p{2.5cm}p{2.5cm}p{2cm}p{2cm}}
% {lcccccccccccc}
\toprule
& Hyperparameter Value \\ 
\midrule
Steps per training & 8 \\
Time limit & 8 \\
Number Parallel Processes & 256 \\
Learning rate & 0.00005 \\
Entropy Coefficient & 0.005 \\
Value loss Coefficient & 0.5 \\
Mini Batch Size & 32 \\
Gamma & 0.99 \\ 
GAE Lambda & 0.95 \\
Number of in-context Exemplars & 4 \\
Number of example pool & 16 \\
Positive lambda coefficient ($\lambda_1$) & 2.0 \\
Negative lambda coefficient ($\lambda_2$) & 1.8 \\
\bottomrule 
\end{tabular}
\end{table*}
```

## Table 9
```latex
\begin{table*}
\caption{\color{black} Few-shot classification results. We compare against different baselines in this setting. Results show that \ours{} surpasses various baselines including finetuning, prompt tuning and discrete prompt search. The standard deviations are shown in brackets.}
\footnotesize
\begin{tabular}{ll ccccc}
% {lcccccccccccc}
\toprule
& & RTE & QNLI & SNLI & MNLI & MRPC \\ 
\midrule  
\multirow{1}{*}{Finetuning} & Finetuning (few-shot) & 58.6 (3.9) & 60.2 (4.7) & 54.64 (9.7) & 47.8 (7.5) & 77.4 (3.6)\\
\midrule
\multirow{3}{*}{Continuous Prompt} & Soft Prompt Tuning & 54.7 (10.9) & 49.7 (0.2) & 36.13 (14.6) & 33.2 (0.0) & 51.6 (0.9)\\
& Black-Box Tuning & 52.6 (0.9) & 48.8 (0.6) & 46.58 (1.3) & 42.9 (2.0) & 61.6 (0.9)\\
% & AutoPrompt & - & - & - & - & -\\
\midrule
\multirow{2}{*}{Discrete Prompt} & Manual Prompt & 51.6 & 50.8 &  31.11 & 51.7 & 67.4\\
& In-Context Demo. &  60.4 (0.7) & 53.8 (0.4) & 47.11 (1.4) & 53.4 (1.5) & 45.8 (0.8)\\
% & Instructions & - & - & - & - & -\\
% & GrIPS & - & - & - & - & -\\
% & RLPrompt & - & - & - & - & -\\
\midrule
\multirow{1}{*}{Discrete Prompt} & \ours{} (ours) & 60.3 (2.2) & 57.4 (1.5) & 56.4 (3.2) & 45.2 (2.0) & 74.0 (1.0)\\
\bottomrule 
\end{tabular}
\end{table*}
```

## Table 10
```latex
\begin{table*}[h]
\caption{Natural instructions used for \ours{} in all the tasks.}
% \vspace{-10pt}
% \footnotesize
\setlength\tabcolsep{4.0pt}
\label{tab:natural_inst}
\centering
\begin{tabular}{p{2cm}p{11cm}p{5cm}p{2.5cm}p{2.5cm}p{2cm}p{2cm}}
% {lcccccccccccc}
\toprule
Task & Natural Instructions \\ 
\midrule
SST-2 & ``In this task, you are given sentences from movie reviews. The task is to classify a sentence as ``great" if the sentiment of the sentence is positive or as ``terrible" if the sentiment of the sentence is negative." \\
AG News & ``Classify the news articles into the categories of World, Sports, Business, and Technology." \\
CR & ``In this task, you are given sentences from customer reviews. The task is to classify a sentence as ``great" if the sentiment of the sentence is positive or as ``terrible" if the sentiment of the sentence is negative."\\
MR & ``In this task, you are given sentences from movie reviews. The task is to classify a sentence as ``great" if the sentiment of the sentence is positive or as ``terrible" if the sentiment of the sentence is negative." \\
Yelp & ``In this task, you are given sentences from Yelp reviews. The task is to classify a sentence as ``great" if the sentiment of the sentence is positive or as ``terrible" if the sentiment of the sentence is negative." \\
RTE & N/A\\
SNLI & ``In this task, you're given a pair of sentences, sentence 1 and sentence 2. Your job is to choose whether the two sentences clearly agree (entailment)/disagree (contradiction) with each other, or if this cannot be determined (neutral). Your answer must be in the form of the letters Yes, Maybe, and No respectively." \\
QNLI & ``You are given two sentences(Sentence1 and Sentence2). Answer ``yes" if these sentences are a paraphrase of one another, otherwise answer ``no"." \\
MNLI & ``In this task, you're given a pair of sentences, sentence 1 and sentence 2. Your job is to choose whether the two sentences clearly agree (entailment)/disagree (contradiction) with each other, or if this cannot be determined (neutral). Your answer must be in the form of the letters Yes, Maybe, and No respectively."\\
\bottomrule 
\end{tabular}
\end{table*}
```

## Table 11
```latex
\begin{table*}[h]
\caption{Verbalizers used for \ours{} in all the tasks.}
% \vspace{-10pt}
% \footnotesize
\setlength\tabcolsep{4.0pt}
\label{tab:natural_ver}
\centering
\begin{tabular}{p{2cm}p{11cm}p{5cm}p{2.5cm}p{2.5cm}p{2cm}p{2cm}}
% {lcccccccccccc}
\toprule
Task & Natural Instructions \\ 
\midrule
SST-2 & `Someone just said to me ``\{\{sentence\}\}". Do you think they are \{\{``sad"\}\} or \{\{``happy"\}\}? \{\{ answer\_choices[label]\}\}'\\
AG News & ``What label best describes this news article? \{\{text\}\} \{\{answer\_choices[label]\}\}" \\
CR & `Someone just said to me ``\{\{sentence\}\}". Do you think they are \{\{``sad"\}\} or \{\{``happy"\}\}? \{\{ answer\_choices[label]\}\}'\\
MR & `\{\{text\}\} Did the reviewer find this movie \{\{``good or bad"\}\}? \{\{ answer\_choices[label] \}\}' \\
Yelp & `\{\{ text \}\} Overall, the experience is \{\{ answer\_choices[label] \}\}' \\
RTE & `Does the claim ``\{\{sentence2\}\}" follow from the fact that ``\{\{sentence1\}\}"? Please answer either \{\{``yes"\}\} or \{\{``no"\}\}. \{\{answer\_choices[label]\}\}'\\
SNLI & `Suppose \{\{premise\}\} Can we infer that ``\{\{hypothesis\}\}"? Yes, no, or maybe? \{\{ answer\_choices[label] \}\}' \\
QNLI & `\{\{sentence\}\} Does that sentence have all you need to answer the question ``\{\{question\}\}"? \{\{answer\_choices[label]\}\}' \\
MNLI & `Suppose \{\{premise\}\} Can we infer that "\{\{hypothesis\}\}"? Yes, no, or maybe?  \{\{ answer\_choices[label] \}\} '\\
MRPC & `Does the sentence
      \{\{sentence1\}\} paraphrase (that is, mean the same thing as) this sentence? \{\{sentence2\}\} \{\{ answer\_choices[label] \}\}' \\
\bottomrule 
\end{tabular}
\end{table*}
```

## Table 12
```latex
\begin{table*}
\caption{\color{black} Scaling results for \ours{} in 512 training data per class. Results show that \ours{} also scales and achieves better results comparing to finetuning.}
\footnotesize
\centering
\begin{tabular}{ll cccc}
% {lcccccccccccc}
\toprule
& & SST2 & MR & AG News & RTE \\ 
\midrule  
\multirow{1}{*}{Finetuning} & Finetuning (few-shot) & 93.4 & 87.0 & \textbf{89.5} & 67.9 \\
\midrule
\multirow{1}{*}{Discrete Prompt} & \ours{} (ours) & \textbf{93.8} & \textbf{88.6} & 88.6 & \textbf{71.4}\\
\bottomrule 
\end{tabular}
\end{table*}
```

## Table 13
```latex
\begin{table*}[h]
\caption{\color{black} Details for the dataset including the type, size of training, evaluation and test. Note that here all the sizes are few-shot dataset.}
% \vspace{-10pt}
% \footnotesize
\setlength\tabcolsep{4.0pt}
\label{tab:hyper_params}
\centering
\begin{tabular}{p{2cm}p{2cm}p{2cm}p{3cm}p{2.5cm}p{2cm}p{2cm}}
% {lcccccccccccc}
\toprule
Dataset & Type & $|\mathrm{C}|$ & $|\mathrm{Train}|=|\mathrm{Dev}|$ & $|\mathrm{Test}|$\\ 
\midrule
SST2 & Sentiment & 2 & 32 & 1.8k \\
AG News & topic & 4 & 64 & 7.6k\\
CR & Sentiment & 2 & 32 & 2k\\
MR & Sentiment & 2 & 32 & 2k\\
Yelp & Sentiment & 2 & 32 & 38k\\
RTE & NLI & 2 & 32 & 0.3k\\
SNLI & NLI & 3 & 48 & 10k\\
QNLI & NLI & 3 & 48 & 9.8k\\ 
MNLI & NLI & 3 & 48 & 9.8k\\
\bottomrule 
\end{tabular}
\end{table*}
```

