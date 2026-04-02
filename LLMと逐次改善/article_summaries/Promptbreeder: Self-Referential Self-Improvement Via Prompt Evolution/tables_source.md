# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t!]
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{rrr|rrrr|rrrr}
\toprule
 & \cen{Method} & \cen{LLM} & \row{\cen{MultiArith*}}{\cen{GSM8K}}{\cen{AddSub*}}{\cen{AQuA-RAT}}{\cen{SingleEq*}}{\cen{SVAMP*}}{\cen{CSQA}}{\cen{SQA}}
\midrule
\parbox[t]{2mm}{\multirow{9}{*}{\rotatebox[origin=c]{90}{Zero-shot}}} & CoT & text-davinci-003 & \row{(83.8)}{(56.4)}{(85.3)}{(38.9)}{(88.1)}{(69.9)}{(65.2)}{(63.8)}
 & PoT & text-davinci-003 & \row{(92.2)}{(57.0)}{(85.1)}{(43.9)}{(91.7)}{(70.8)}{--}{--}
 & PS & text-davinci-003 & \row{(87.2)}{(58.2)}{(88.1)}{(42.5)}{(89.2)}{(72.0)}{--}{--}
 & PS+ & text-davinci-003 & \row{(91.8)}{(59.3)}{(\h{92.2})}{(46.0)}{(94.7)}{(75.7)}{(71.9)}{(65.4)}
& PS & PaLM 2-L & \row{97.7}{59.0}{72.4}{40.2}{90.6}{83.8}{77.9}{50.0}
& PS+ & PaLM 2-L & \row{92.5}{60.5}{74.4}{39.4}{94.7}{86.3}{73.3}{50.1}
& APE & PaLM 2-L &  \row{95.8}{77.9}{72.2}{45.7}{82.2}{73.0}{67.3}{38.4}
& OPRO & PaLM 2-L &  \row{--}{80.2}{--}{--}{--}{--}{--}{--}
 & PB (ours)  & PaLM 2-L & \row{\h{99.7}}{\h{83.9}}{87.8}{\h{62.2}}{\h{96.4}}{\h{90.2}}{\h{85.4}}{\h{71.8}} 
\midrule
\parbox[t]{2mm}{\multirow{3}{*}{\rotatebox[origin=c]{90}{Few-}}} & Manual-CoT & text-davinci-003 & \row{(93.6)}{(58.4)}{(\h{91.6})}{(48.4)}{(93.5)}{(80.3)}{(78.3)}{(71.2)}
 & Auto-CoT & text-davinci-003 & \row{(95.5)}{(57.1)}{(90.8)}{(41.7)}{(92.1)}{(78.1)}{--}{--}        
 & PB (ours) & PaLM 2-L & \row{\h{100.0}}{\h{83.5}}{87.1}{\h{64.6}}{\h{98.9}}{\h{93.7}}{\h{85.9}}{\h{80.2}} 
\bottomrule
\end{tabular}
}
\caption{Promptbreeder (\textbf{PB}) comparison to Chain-of-Thought~\citep[\textbf{Manual-CoT},][]{DBLP:conf/nips/Wei0SBIXCLZ22}, Zero-shot \textbf{CoT}~\citep{DBLP:conf/nips/KojimaGRMI22}, Program-of-Thoughts~\citep[\textbf{PoT,}][]{chen2022program}, \textbf{Auto-CoT}~\citep{DBLP:conf/iclr/0001Z0S23}, \textbf{OPRO}~\citep{DBLP:journals/corr/abs-2309-03409}, Automatic Prompt Engineer Zero-shot prompt~\citep[\textbf{APE},][]{zhou2022large}, Plan-and-Solve with (\textbf{PS+}) and without the improved prompt~\citep[\textbf{PS},][]{DBLP:conf/acl/WangXLHLLL23} and using PaLM 2-L~\citep{anil2023palm} as the underlying LLM (\textbf{APE}, \textbf{PS}$_\textbf{PaLM 2-L}$/\textbf{PS}+$_\textbf{PaLM 2-L}$). Best results in both the zero-shot and few-shot categories are highlighted in bold. Results in brackets are directly taken from the Plan-and-Solve paper which uses text-davinci-003~ \citep{DBLP:conf/nips/BrownMRSKDNSSAA20}. For datasets with astericks (MultiArith*, SingleEq*, AddSub*, and SVAMP*), we randomly took half of the examples for training and report accuracy on the remaining test set. See \Cref{sec:experiments} and \Cref{appendix:datasets} for details on the prompts and datasets.}
\label{tab:pe_comparison}
\end{table}
```

## Table 2
```latex
\begin{table}[h!]
    \centering
\resizebox{\linewidth}{!}{
    \begin{tabular}{p{0.05\textwidth}p{0.95\textwidth}}
\toprule
\textbf{Index} & \textbf{Initially Evolved Prompt} \\
\midrule
0 & Draw a picture of the situation being described in the math word problem\\
1 & Solve the math word problem by first converting the words into equations using algebraic notation. Then solve the equations for the unknown variables, and express the answer as an arabic numeral.\\
2 & Solve the math word problem by breaking the problem into smaller, more manageable parts. Give your answer as an arabic numeral.\\
3 & Generate the answer to a word problem and write it as a number.\\
4 & Collaborative Problem Solving: Work with other people to solve the problem, and give your answer as an arabic numeral.\\
5 & Solve the problem by explaining why systemic or structural issues would not be the cause of the issue.\\
6 & Draw a diagram representing the problem.\\
7 & Solve the math word problem, giving your answer as an equation that can be evaluated.\\
8 & Make a list of ideas for solving this problem, and apply them one by one to the problem to see if any progress can be made.\\
9 & Do NOT use words to write your answer.\\  
\bottomrule
    \end{tabular}
}
    \caption{Examples of initial prompts generated from the problem description for GSM8k}
    \label{tab:initialization}
\end{table}
```

## Table 3
```latex
\begin{table}[h!]
\centering
\begin{tabularx}{\textwidth}{lXX}
%\begin{tabular}{|l|p{6cm}|p{6cm}|}
\toprule
\textbf{Model} & \textbf{Prompt} \\ 
\midrule
CoT & ``“Let’s think step by step.''\\ 
PS &  ``Let’s first understand the problem and devise a plan to solve the problem. Then, let’s carry out the plan and solve the problem step by step.''\\ 
PS+ & ``Let’s first understand the problem, extract relevant variables and their corresponding numerals, and make a plan. Then, let’s carry out the plan, calculate intermediate variables (pay attention to correct numerical calculation and commonsense), solve the problem step by step, and show the answer.''\\ 
APE &  ``Let’s work this out in a step by step way to be sure we have the right answer.''\\ 
OPRO & ``Take a deep breath and work on this problem step-by-step.''\\ 
\bottomrule
\end{tabularx}
%\end{tabular}
\caption{Table of prompts evolved for different arithmetic tasks.}
\label{tab:prompt_table2}
\end{table}
```

## Table 4
```latex
\begin{table}[h!]
\centering
\begin{tabularx}{\textwidth}{lXX}
%\begin{tabular}{|l|p{6cm}|p{6cm}|}
\toprule
\textbf{Task} & \textbf{Prompt 1} & \textbf{Prompt 2} \\ 
\midrule
ADDSUB & Solving word problems involves carefully reading the prompt and deciding on the appropriate operations to solve the problem. & You know what's cool? A million dollars. \\ 
AQUA & Do a simple computation. & MATH WORD PROBLEM CHOICE (A) (B) (C) (D) or (E). \\ 
GSM8K & SOLUTION" &  \\ 
MULTIARITH & Solve the math word problem, giving your answer as an arabic numeral. Let's think step by step. & Solve the math word problem, giving your answer as an arabic numeral. Explain the problem to someone else as a way to simplify it. What is the core issue or problem that needs to be addressed? \\ 
SINGLEEQ & solve the math word problem, which might contain unnecessary information, by isolating the essential facts. Then set up the equations, and give your answer as an arabic numeral. & Solve the math problem. \\ 
SVAMP & visualise solve number & (Solve the math word problem. Therefore, the answer (arabic numerals) is \_\_\_\_\_)\\ 
SQA & OUTPUT MUTANT = Work out an answer to the commonsense reasoning question above. If there are multiple people or perspectives involved, try considering them one at a time. & “Work out an answer to the commonsense reasoning question above. If there are multiple people or perspectives involved, try considering them one at a time. Next, answer yes or no."\\
CSQA & Solve the multiple choice math word problem, choosing (A),(B),(C),(D) or (E). &
 Solve the multiple choice math word problem. Can you recall any similar problems you've done and how you solved them?\\
\bottomrule
\end{tabularx}
%\end{tabular}
\caption{Table of two-stage task-prompts evolved for different arithmetic tasks.}
\label{tab:prompt_table}
\end{table}
```

## Table 5
```latex
\begin{table}[h!]
\centering
\begin{tabularx}{\textwidth}{Xr}
\toprule
\textbf{Instruction} & \textbf{Score} \\
\midrule
Please summarise and improve the following instruction & 24.13\% \\
Simplify this instruction by breaking it up into separate sentences. The instruction should be simple and easily understandable & 17.8\% \\
As a really good teacher, explain the instruction, as if you are explaining it to a child & 16.2\%\\ 
Simplify this instruction as if you are teaching it to a child & 10.0 \\
100 hints & 4.3\% \\
A list of 100 hints & 3.4\% \\
\bottomrule
\end{tabularx}
\caption{The most successful mutation prompts evolved in a self-referential way during a Promptbreeder training run on GSM8K. The score is the probability that they resulted in an improved prompt when applied.}
\label{tab:my_label}
\end{table}
```

## Table 6
```latex
\begin{table}[h!]
\centering
\begin{tabularx}{\textwidth}{Xr}
\toprule
\textbf{Mutation Operator} & \textbf{Percentage} \\
\midrule
Zero-order Hyper-Mutation & 42\% \\
Lineage Based Mutation & 26\% \\
First-order Hyper-Mutation & 23\% \\
EDA Rank and Index Mutation & 12.7\% \\
Direct Mutation & 12\% \\
EDA Mutation & 10.7\% \\
Lamarckian Mutation & 6.3\% \\
\bottomrule
\end{tabularx}
\caption{The proportion of times that an offspring with fitness greater than the parent was produced for each of the types of mutation operator applied, listened from best to worst, for GSM8k.}
\label{tab:mutation_percentages}
\end{table}
```

## Table 7
```latex
\begin{table}[H]
\centering
%\begin{adjustbox}{width=\textwidth}
\begin{tabularx}{\textwidth}{l*{8}{X}}
\toprule
Dataset         & Zero-shot APE & Few-shot APE & PE using APE prompts & Few-shot PE   \\
\bottomrule
First Letter    &            100  & 100 &1 &  \h{100} \\
Second Letter   &            87   & 69 &27 &  \h{95} \\
List Letters    &            99   & 100 &0 &  99 \\
Starting With   &            68   & 69 &6 &  \h{71} \\
Pluralization   &            100  & 100 &23 &  \h{100} \\
Passivization   &            100  & 100 &100 &  \h{100} \\
Negation        &            83   & 90 &16 &  \h{90} \\
Antonyms        &            83   & 86 &80 &  \h{87} \\
Synonyms        &            22   & 14 &16 &  \h{43} \\
Membership      &            66   & 79 &96 &  \h{100} \\
Rhymes          &            100  & 61 &90 &  \h{100} \\
Larger Animal   &            97   & 97 &27 &  \h{97} \\
Cause Selection &            84   & 100 &66 &  \h{100} \\
Common Concept  &            27   & 32 &0 &   0 \\
Formality       &            65   & 70 &10 &  7 \\
Sum             &            100  & 100 &72 &  \h{100} \\
Difference      &            100  & 100 &98 &  \h{100} \\
Number to Word  &            100  & 100 &66 &  \h{100} \\
Translation English-German  &  82 & 86 &46 &  \h{87} \\
Translation English-Spanish &  86 & 91 &80 &  \h{91} \\
Translation English-French  &  78 & 90 &68 &  \h{91} \\
Sentiment Analysis  &        94   & 93 &33 &  \h{93} \\
Sentence Similarity &        36   & 43 &53 &  \h{56} \\
Word in Context     &        62   & 63 &6 &  \h{65} \\
\bottomrule
\end{tabularx}
\caption{Prompt Evolution (PE) using PaLM2-L LLM surpasses APE on 21 out of 24 instruction induction tasks. Three APE controls are provided. The first two are from previously published results using  the  text-davinci-002  model.  The  third  modifies  our PromptBreeder  to  use  APE’s  task-prompt initialisation method and then the  mutation-prompt from the APE paper ``Generate a variation of the following instruction while keeping the semantic meaning''. 
}
\label{tab:ape_comparison}
%\end{adjustbox}
\end{table}
```

