# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[H]
    \centering
    \begin{tabular}{c|c|c}
         Benchmark & Seed Scaffolds & Discovered Scaffolds \\
         \hline
         GPQA & 0.219064 & 0.247536 \\
         MMLU & 0.484208 & 0.542816 \\
         DROP & 0.390754 & 0.438813
    \end{tabular}
    \caption{Reporting the HV indicator on the test set for \textsc{BlueAgentBreeder}.}
    \label{tab:bluehv}
\end{table}
```

## Table 2
```latex
\begin{table}[t!]
\centering


% \begin{minipage}{\textwidth}
% \resizebox{\textwidth}{!}{
\begin{tabular}{l@{\hskip 10pt}c@{\hskip 10pt}c@{\hskip 10pt}c@{\hskip 10pt}c@{\hskip 10pt}c}
\toprule
 % Apply light blue color to the first header row
\textsc{BlueAgentBreeder} & \multicolumn{3}{c}{Capability} & Safety & Helpfulness \\
\cmidrule(l{2pt}r{10pt}){2-4} \cmidrule(l{2pt}r{10pt}){5-5} \cmidrule(l{2pt}r{10pt}){6-6}
% Apply light blue color to the second header row
 & \textbf{DROP} & \textbf{MMLU} & \textbf{GPQA} & \textbf{SaladData} & \textbf{TruthfulQA} \\
\midrule
 \multicolumn{6}{l}{\emph{Seed Scaffolds from ADAS \citep{adas}}} \\
\midrule
Chain-of-Thought (CoT) & 66.6 $\pm$ 5.0 & 80.0 $\pm$ 4.4  & 31.2 $\pm$ 5.6  & 29.2 $\pm$ 5.6 & 86.8 $\pm$ 3.6 \\
Self-Consistency CoT & 66.0 $\pm$ 4.4 & 81.6 $\pm$ 4.8 & 32.4 $\pm$ 6.0 & 22.8 $\pm$ 5.2  & 85.6 $\pm$ 4.4 \\
Self-Refinement  & 61.4 $\pm$ 4.8 & 78.4 $\pm$ 5.2 & 28.4 $\pm$ 6.0 & 26.0 $\pm$ 5.2 & 86.8 $\pm$ 4.0 \\
Debate& 69.9 $\pm$ 4.4 & 77.6 $\pm$ 5.2 & 29.6 $\pm$ 5.6 & 36.4 $\pm$ 6.0  & 86.4 $\pm$ 4.0 \\
Step-Back Abstraction &  71.4 $\pm$ 4.3 & 79.2 $\pm$ 4.8 & 30.8 $\pm$ 5.2 & 40.8 $\pm$ 5.6 & 85.2 $\pm$ 4.4 \\
Quality-Diversity  & \underline{78.0 $\pm$ 3.9}  & 81.6 $\pm$ 4.4 & 28.4 $\pm$ 5.6 &  25.8 $\pm$ 5.8 & \underline{87.2 $\pm$ 4.0} \\
Role Assignment  & 75.8 $\pm$ 4.2 & 79.2 $\pm$ 4.8 & 32.0 $\pm$ 6.0 & 18.0 $\pm$ 5.2 & 85.6 $\pm$ 4.4 \\
\midrule
 \multicolumn{6}{l}{\emph{BlueAgentBreeder Scaffolds ($S=\text{SaladData}$, $H=\text{TruthfulQA}$)}} \\
\midrule

${\arg\max_s} \{f_{C_\text{DROP}}\}$& {\textbf{79.0 $\pm$ 3.8}} & - & - & 46.4 $\pm$ 6.4 & \textbf{88.0 $\pm$ 4.0}\\
${\arg\max_s} \{f_{S}\}$ & 62.0 $\pm$ 4.8 & - & - & \underline{86.0 $\pm$ 4.0} & 83.6 $\pm$ 4.4\\
${\arg\max_s} \{f_{C_\text{DROP}},f_{S},f_{H}\}$ & 62.0 $\pm$ 4.8 & - & - & \underline{86.0 $\pm$ 4.0} & 83.6 $\pm$ 4.4\\
% \midrule
${\arg\max_s} \{f_{C_\text{MMLU}}\}$ & - &{\textbf{85.2 $\pm$ 4.4}}  & - & 54.0 $\pm$ 5.6 & 81.2 $\pm$ 4.4\\
${\arg\max_s} \{f_{S}\}$ & - & \underline{84.0 $\pm$ 4.4}& -  & 84.4 $\pm$ 4.0 & 76.0 $\pm$ 5.2\\
${\arg\max_s} \{f_{C_\text{MMLU}},f_{S},f_{H}\}$  & - & \underline{84.0 $\pm$ 4.4} & - & 84.4 $\pm$ 4.0 & 76.0 $\pm$ 5.2\\
% \midrule
${\arg\max_s} \{f_{C_\text{GPQA}}\}$  & - & -&\textbf{39.2 $\pm$ 5.6} & 52.0 $\pm$ 6.8 & 57.6 $\pm$ 6.4\\
${\arg\max_s} \{f_{S}\}$ & - & - & 31.2 $\pm$ 6.0  & \textbf{95.2 $\pm$ 2.4} & 49.6 $\pm$ 6.4\\
${\arg\max_s} \{f_{C_\text{GPQA}},f_{S},f_{H}\}$  & - & - & \underline{36.8 $\pm$ 5.2} & 49.2 $\pm$ 6.8 & 86.8 $\pm$ 4.0\\
\bottomrule

\end{tabular}
% }
% \end{minipage}

\caption{We report the evaluation results of \textsc{BlueAgentBreeder} on the held-out test set of capability benchmark (DROP \citep{drop}, MMLU \citep{mmlu}, GPQA \citep{gpqa}), safety benchmark (SaladData \citep{saladdata}) and ensure a trivial solution has not been found by evaluating each scaffold's helpfulness on TruthfulQA \citep{truthfulqa}. For each benchmark, we compare the \textsc{AgentBreeder}-discovered scaffolds against seed scaffolds, with the highest and second highest result in each column given in bold and underlined respectively. We report the median accuracy (or F1 score for DROP) along with a 95\% confidence interval computed over 250 held-out test samples. The evolution is conducted independently for each capability benchmark.}
\label{tab:blue_tab}
\end{table}
```

## Table 3
```latex
\begin{table}[H]
    \centering
    \begin{tabular}{c|c|c}
         Benchmark & Seed Scaffolds & Discovered Scaffolds \\
         \hline
         DROP & 0.572759 & 0.0.602547
    \end{tabular}
    \caption{Reporting the HV indicator on the test set for \textsc{RedAgentBreeder}.}
    \label{tab:redhv}
\end{table}
```

## Table 4
```latex
\begin{table}[H]

\begin{tabular}{lccc}
\toprule
\multicolumn{1}{c}{\textsc{RedAgentBreeder}} & \multicolumn{1}{c}{Capability} & \multicolumn{1}{c}{Harm} \\
\cmidrule(lr){2-2}\cmidrule(lr){3-3}
& \textbf{DROP} & \textbf{1-SaladData} \\
\midrule
\multicolumn{3}{l}{\emph{Seed Scaffolds from ADAS \citep{adas}}} \\
\midrule
CoT & 68.2 $\pm$ 4.7 & \underline{76.8 $\pm$ 4.8}  \\
CoTSC & 69.6 $\pm$ 4.8 & 70.8 $\pm$ 6.0  \\
Refine & 62.6 $\pm$ 4.7 & 71.6 $\pm$ 5.2 \\
Debate& 63.2 $\pm$ 4.8 & 56.0 $\pm$ 6.0 \\
StepBack &  67.5 $\pm$ 4.5 & 58.0 $\pm$ 6.0 \\
QD & \underline{74.9 $\pm$ 4.2} & 73.6 $\pm$ 5.2 \\
Roles & 73.1 $\pm$ 3.7 & 46.4 $\pm$ 6.0  \\
\midrule
\multicolumn{3}{l}{\emph{RedAgentBreeder Scaffolds}} \\
\midrule
${\arg\max_s} \{f_{C_\text{DROP}}\}$ & \textbf{75.0 $\pm$ 4.1} & 26.0 $\pm$ 5.2  \\
${\arg\max_s} \{f_{1-S}\}$ & 67.7 $\pm$ 4.7 & \textbf{81.6 $\pm$ 4.8}  \\
${\arg\max_s} \{f_{C_\text{DROP}},f_{1-S}\}$  & 67.7 $\pm$ 4.7 & \textbf{81.6 $\pm$ 4.8}  \\
\bottomrule

\end{tabular}
\caption{We report the evaluation results of \textsc{AgentBreeder} run in ``red'' mode on the held-out test set. We seek to maximize performance on DROP \citep{drop} whilst also maximizing performance on 1-SaladData \citep{saladdata}, an inverted version of the SaladData benchmark where unsafe responses are scored highly. For each
benchmark, we compare the \textsc{AgentBreeder}-discovered scaffolds against seed scaffolds, with the highest and second highest result
in each column given in bold and underlined respectively. We report the F1 score and median accuracy for DROP and 1-SaladData respectively, along with a 95\% confidence interval computed over 250 held-out test samples.}
\label{tab:red_table}
\end{table}
```

## Table 5
```latex
\begin{table}[H]
\begin{tabular}{lccccc}

\toprule
\multicolumn{4}{c}{\textsc{CapableAgentBreeder}} \\
\midrule
 \multicolumn{3}{c}{Capability} & \multicolumn{1}{c}{Safety} \\
\cmidrule(lr){1-3}\cmidrule(lr){4-4}
\textbf{DROP} & \textbf{MMLU} & \textbf{GPQA} & \textbf{SaladData} \\

\midrule
\multicolumn{4}{l}{\emph{Seed Scaffolds \citep{adas}}} \\
\midrule
 70.4 $\pm$ 3.1 & 80.2 $\pm$ 3.6 & 35.2 $\pm$ 4.4 & 31.2 $\pm$ 4.2 \\

 64.4 $\pm$ 3.2 & \textbf{82.6 $\pm$ 3.4} & 38.1 $\pm$ 4.3 & 17.8 $\pm$ 3.4 \\
69.3 $\pm$ 3.2 & 81.2 $\pm$ 3.6 & \underline{39.4 $\pm$ 4.4} & 55.6 $\pm$ 4.6 \\

\midrule
\multicolumn{4}{l}{\emph{ADAS Scaffolds }} \\
\midrule

\underline{72.0 $\pm$ 3.0} & - & - & 57.0 $\pm$ 4.2 \\
 - & 80.4 $\pm$ 3.4 & - & \textbf{76.4 $\pm$ 3.6} \\
 - & - & 37.4 $\pm$ 3.6 & 61.0 $\pm$ 4.2 \\
 
\midrule
\multicolumn{4}{l}{\emph{CapableAgentBreeder Scaffolds}} \\
\midrule

 \textbf{72.3 $\pm$ 3.1} & - & - & 39.4 $\pm$ 4.4 \\
 - & \underline{82.4 $\pm$ 3.2} & - & \underline{58.0 $\pm$ 4.2} \\
 - & - & \textbf{41.2 $\pm$ 4.4} & 43.8 $\pm$ 4.4 \\
  
\bottomrule

\end{tabular}
\caption{We report the evaluation results of \textsc{CapableAgentBreeder} on the held-out test sets. For each benchmark, we compare the \textsc{AgentBreeder}-discovered scaffolds with the seed and discovered scaffolds from the seminal work ADAS \citep{adas}, with the highest and second highest result in each column given in bold and underlined respectively. We report the F1 score on DROP \citep{drop} and median accuracy on the other benchmarks, along with a 95\% confidence interval computed over 500 held-out test samples.}
\label{tab:capable}
\end{table}
```

