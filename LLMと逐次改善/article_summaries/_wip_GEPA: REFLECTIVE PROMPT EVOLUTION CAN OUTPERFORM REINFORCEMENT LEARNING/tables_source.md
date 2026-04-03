# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[h!]
% \centering
% \small
% \begin{tabular}{|p{2.0cm}|p{4.2cm}|p{3.2cm}|p{3.1cm}|}
% \hline
% \textbf{Benchmark} & \textbf{Description} & \textbf{Compound AI System} & \textbf{Feedback Function} \\
% \hline
% HoVer \cite{hover_bench} & Open-domain multihop fact extraction and claim verification using Wikipedia corpus; requires reasoning across multiple articles. & HoverMultiHop (up to 3 hops via 2 query writer modules and 2 doc summary modules; \cite{langprobe}) & Identifies retrieved correct documents and documents yet to be retrieved; returns as feedback text. \\
% \hline
% HotpotQA \cite{hotpotqa_bench} & Large-scale multi-hop Wikipedia QA (113K pairs). Answering requires reasoning over multiple supporting documents. & Modified HoverMultiHop (answer question at last hop) & Provides relevant documents remaining to be retrieved as feedback at each stage. \\
% \hline
% IFBench \cite{ifbench_bench} & Tests following precise human instructions, especially output constraints; 58 new and OOD output constraints. & 2-stage: (1) answers user query, (2) rewrites answer to satisfy constraints. & Provides descriptions of constraints satisfied and not satisfied. \\
% \hline
% PUPA \cite{papillon_bench} & Privacy-conscious delegation: high response quality while minimizing PII leakage to untrusted models. & PAPILLON: trusted user query rewriter, response rewriter, interleaved with untrusted model (\cite{papillon_bench}) & Feedback text breaks down aggregate response quality score and PII leakage score. \\
% \hline
% FSABench \cite{fsabench_bench} & Multitask: multilabel tag classification (10), sentiment (3), urgency (3); on facility team communications. & 3 modules: tag classifier, sentiment classifier, urgency classifier (one per task) & Feedback: correct labels and errors per module. \\
% \hline
% \end{tabular}
% \caption{Benchmarks, compound AI system architectures, and feedback function types evaluated in this work.}
% \label{tab:compound_benchmarks}
% \end{table}
```

## Table 2
```latex
\begin{table}[ht]
    \centering
    \caption{\added{Total number of calls made by GEPA to reflection LM during optimization.}}
    \label{tab:reflection_calls}
    \begin{tabular}{lcc}
        \toprule
        \textbf{Benchmark Name} & \textbf{Num Reflection Calls} & \textbf{Num Reflection Calls} \\
                                & \textbf{GPT-4.1-Mini}         & \textbf{Qwen3-8B} \\
        \midrule
        AIME-2025      & 24 & 90 \\
        LiveBench-Math & 34 & 38 \\
        HotpotQA       & 69 & 64 \\
        IFBench        & 21 & 17 \\
        Hover          & 92 & 50 \\
        PUPA           & 46 & 38 \\
        \bottomrule
    \end{tabular}
\end{table}
```

## Table 3
```latex
\begin{table*}[htp]
\centering
\caption{Benchmark results for different optimizers evaluated on GPT-4.1 Mini. As a prompt-optimization system, GEPA works off-the-shelf on \textit{closed-source} models as well, outperforming state-of-the-art prompt optimizers including MIPROv2 \added{(in 2 settings: Instruction-only optimization (``MIPROv2-No-Demos'') as well as joint instruction and few-shot optimization (``MIPROv2'')), Trace (with its OptoPrime optimizer), and TextGrad}. \added{Additionally, GEPA-optimized prompts demonstrate strong cross-model generalization: ``GEPA-Qwen-Opt''—optimized entirely for (and using) the weaker Qwen3-8B—achieves a +9\% gain when evaluated on GPT-4.1-Mini without modification, notably outperforming all baselines (MIPROv2, TextGrad, Trace) that optimized directly for (and using) GPT-4.1-Mini.}}
% Additionally, GEPA-optimized prompts generalize across models. ``GEPA-Qwen-Opt'' reports results of evaluating prompts optimized by GEPA for (and using) Qwen3-8B (config GEPA from table~\ref{tab:main-results}) but evaluated without modification on GPT-4.1-Mini.  Although the whole optimization process (including the reflection language model, and the rollout model for training and validation) used the less capable Qwen3 8B model, optimized prompts still show significant improvement (+9\%) over the baseline and even outperform other optimizers, all of which optimize for (and using) GPT-4.1-Mini
\label{tab:main-results-gpt}
\resizebox{0.96\textwidth}{!}{
% \begin{tabular}{lcccccccc}
% \toprule
% \textbf{GPT-4.1 Mini} & \textbf{AIME-2025} & \textbf{LiveBench-Math} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{Aggregate} & \textbf{Improvement} \\
% % \midrule
% % \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
% \midrule
% Baseline         & 49.33 & 58.20 & 38.00 & 47.79 & 46.33 & 78.57 & 53.03 & --- \\
% \added{Trace (OptoPrime)}  & \added{45.33} & \added{60.74} & \added{60.33} & \added{51.19} & \added{46.00} & \added{74.18} & \added{56.30} & \added{+3.27} \\
% \added{MIPROv2-No-Demos} & \added{48.67} & \added{60.97} & \added{38.00} & \added{52.04} & \added{51.33} & \added{91.85} & \added{57.14} & \added{+4.11} \\
% MIPROv2          & 51.33 & 61.84 & 58.00 & 49.15 & 48.33 & 83.37 & 58.67 & +5.64 \\
% \added{TextGrad}  & \added{46.67} & \added{63.84} & \added{62.33} & \added{48.64} & \added{47.67} & \added{85.68} & \added{59.14} & \added{+6.11} \\ 
% GEPA             & \textbf{59.33} & \textbf{64.13} & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 65.22 & +12.19 \\
% GEPA+Merge       & \textbf{59.33}* & \textbf{64.13}* & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{66.36} & +\textbf{13.33} \\
% \midrule
% \multicolumn{9}{l}{\added{Optimized with Qwen3-8B, evaluated on GPT-4.1-Mini}} \\
% \midrule
% \added{GEPA-Qwen-Opt}  & \added{52.67} & \added{59.31} & \added{65.67} & \added{49.83} & \added{54.67} & \added{90.05} & \added{62.03} & \added{+9.00} \\
% \bottomrule
% \end{tabular}
% }
\begin{tabular}{lcccccccc}
\toprule
\textbf{GPT-4.1 Mini} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{AIME-2025} & \textbf{LiveBench-Math} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
\midrule
Baseline & 38.00 & 47.79 & 46.33 & 78.57 & 49.33 & 58.20 & 53.03 & --- \\
\added{Trace (OptoPrime)} & \added{60.33} & \added{51.19} & \added{46.00} & \added{74.18} & \added{45.33} & \added{60.74} & \added{56.30} & \added{+3.27} \\
\added{MIPROv2-No-Demos} & \added{38.00} & \added{52.04} & \added{51.33} & \added{91.85} & \added{48.67} & \added{60.97} & \added{57.14} & \added{+4.11} \\
MIPROv2 & 58.00 & 49.15 & 48.33 & 83.37 & 51.33 & 61.84 & 58.67 & +5.64 \\
\added{TextGrad} & \added{62.33} & \added{48.64} & \added{47.67} & \added{85.68} & \added{46.67} & \added{63.84} & \added{59.14} & \added{+6.11} \\ 
GEPA & \textbf{69.00} & 52.72 & 51.67 & 94.47 & \textbf{59.33} & \textbf{64.13} & 65.22 & +12.19 \\
\textbf{GEPA+Merge} & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{59.33} & \textbf{64.13} & \textbf{66.36} & +\textbf{13.33} \\
\midrule
\multicolumn{9}{l}{\added{Optimized with Qwen3-8B, evaluated on GPT-4.1-Mini}} \\
\midrule
\added{GEPA-Qwen-Opt} & \added{65.67} & \added{49.83} & \added{54.67} & \added{90.05} & \added{52.67} & \added{59.31} & \added{62.03} & \added{+9.00} \\
\bottomrule
\end{tabular}
}
\vspace{-4mm}
\end{table*}
```

## Table 4
```latex
\begin{table*}[htp]
\centering
\caption{Benchmark results for different optimizers with Qwen3 8B. GEPA and GEPA+Merge achieve better performance than GRPO with far fewer rollouts on all benchmarks except AIME. For example, for IFBench, GEPA found optimal prompts after just 678 rollouts achieving 38.61\%, outperforming GRPO's test set score of 35.88\% with 24,000 rollouts.}
\label{tab:main-results}
\resizebox{0.96\textwidth}{!}{
% \begin{tabular}{lcccccccc}
% \toprule
% \textbf{Qwen3 8B} & \added{\textbf{AIME-2025}} & \added{\textbf{LiveBench-Math}} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{Aggregate} & \textbf{Improvement} \\
% % \midrule
% % \multicolumn{7}{l}{\textbf{Qwen3-8B}} \\
% \midrule
% Baseline         & \added{27.33} & \added{48.70} & 42.33 & 36.90 & 35.33 & 80.82 & \added{45.23} & --- \\
% MIPROv2          & \added{20.00} & \added{46.60} & 55.33 & 36.22 & 47.33 & 81.55 & \added{47.84} & \added{+2.61} \\
% GRPO             & \added{\textbf{38.00}}   & \added{51.26}   & 43.33 & 35.88 & 38.67 & 86.66 & \added{48.91} & \added{+3.68} \\
% % GEPAWLinear      & 58.33 & 30.44 & 45.33 & 85.45 & 54.89 & +6.04 \\
% % GEPAWMergeWLinear& 62.00 & 37.76 & 47.67 & 90.29 & 59.43 & +10.59 \\
% GEPA             & \added{32.00} & \added{\textbf{51.95}} & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & \textbf{\added{54.85}} & +\textbf{\added{9.62}} \\
% GEPA+Merge       & \added{32.00} & \added{\textbf{51.95}} & \textbf{64.33} & 28.23 & 51.67 & 86.26 & \added{52.40} & \added{+7.17} \\
% \bottomrule
% \end{tabular}
\begin{tabular}{lcccccccc}
\toprule
\textbf{Qwen3 8B} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \added{\textbf{AIME-2025}} & \added{\textbf{LiveBench-Math}} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{7}{l}{\textbf{Qwen3-8B}} \\
\midrule
Baseline & 42.33 & 36.90 & 35.33 & 80.82 & \added{27.33} & \added{48.70} & \added{45.23} & --- \\
GRPO & 43.33 & 35.88 & 38.67 & 86.66 & \added{\textbf{38.00}} & \added{51.26} & \added{48.91} & \added{+3.68} \\
MIPROv2 & 55.33 & 36.22 & 47.33 & 81.55 & \added{20.00} & \added{46.60} & \added{47.84} & \added{+2.61} \\
% GEPAWLinear      & 58.33 & 30.44 & 45.33 & 85.45 & 54.89 & +6.04 \\
% GEPAWMergeWLinear& 62.00 & 37.76 & 47.67 & 90.29 & 59.43 & +10.59 \\
GEPA & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & \added{32.00} & \added{\textbf{51.95}} & \textbf{\added{54.85}} & +\textbf{\added{9.62}} \\
GEPA+Merge & \textbf{64.33} & 28.23 & 51.67 & 86.26 & \added{32.00} & \added{\textbf{51.95}} & \added{52.40} & \added{+7.17} \\
\midrule
\multicolumn{9}{l}{\added{Total optimization budget (\# rollouts)}} \\
% \textit{GEPA (+Merge)} & \textit{6.9k} & \textit{3.6k} & \textit{7.1k} & \textit{2.4k} & \textit{1.8k} & \textit{1.8k} & \textit{3.9k} & --- \\
\added{GEPA (+Merge)} & \added{6871} & \added{3593} & \added{7051} & \added{2426} & \added{1839} & \added{1839} & \added{3936} & --- \\
\added{GRPO} & \added{24000} & \added{24000} & \added{24000} & \added{24000} & \added{24000} & \added{24000} & \added{24000} & --- \\
% \textit{GEPA (+Merge)} & \textit{6871} & \textit{3593} & \textit{7051} & \textit{2426} & \textit{1839} & \textit{1839} & \textit{3936} & --- \\
% \textit{GRPO} & \textit{24000} & \textit{24000} & \textit{24000} & \textit{24000} & \textit{24000} & \textit{24000} & \textit{24000} & --- \\
% \midrule
\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 5
```latex
\begin{table*}[th]
% \centering
% \caption{Benchmark results for different optimizers evaluated on GPT-4.1 Mini. As a prompt-optimization system, GEPA works off-the-shelf on \textit{closed-source} models as well, outperforming state-of-the-art prompt optimizers including MIPROv2 \added{(in 2 settings: Instruction-only optimization (``MIPROv2-No-Demos'') as well as joint instruction and few-shot optimization (``MIPROv2'')), Trace (with its OptoPrime optimizer), and TextGrad}. \added{Additionally, GEPA-optimized prompts demonstrate strong cross-model generalization: ``GEPA-Qwen-Opt''—optimized entirely for (and using) the weaker Qwen3-8B—achieves a +9\% gain when evaluated on GPT-4.1-Mini without modification, notably outperforming all baselines (MIPROv2, TextGrad, Trace) that optimized directly for (and using) GPT-4.1-Mini.}}
% % Additionally, GEPA-optimized prompts generalize across models. ``GEPA-Qwen-Opt'' reports results of evaluating prompts optimized by GEPA for (and using) Qwen3-8B (config GEPA from table~\ref{tab:main-results}) but evaluated without modification on GPT-4.1-Mini.  Although the whole optimization process (including the reflection language model, and the rollout model for training and validation) used the less capable Qwen3 8B model, optimized prompts still show significant improvement (+9\%) over the baseline and even outperform other optimizers, all of which optimize for (and using) GPT-4.1-Mini
% \label{tab:main-results-gpt}
% \resizebox{0.96\textwidth}{!}{
% % \begin{tabular}{lcccccccc}
% % \toprule
% % \textbf{GPT-4.1 Mini} & \textbf{AIME-2025} & \textbf{LiveBench-Math} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{Aggregate} & \textbf{Improvement} \\
% % % \midrule
% % % \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
% % \midrule
% % Baseline         & 49.33 & 58.20 & 38.00 & 47.79 & 46.33 & 78.57 & 53.03 & --- \\
% % \added{Trace (OptoPrime)}  & \added{45.33} & \added{60.74} & \added{60.33} & \added{51.19} & \added{46.00} & \added{74.18} & \added{56.30} & \added{+3.27} \\
% % \added{MIPROv2-No-Demos} & \added{48.67} & \added{60.97} & \added{38.00} & \added{52.04} & \added{51.33} & \added{91.85} & \added{57.14} & \added{+4.11} \\
% % MIPROv2          & 51.33 & 61.84 & 58.00 & 49.15 & 48.33 & 83.37 & 58.67 & +5.64 \\
% % \added{TextGrad}  & \added{46.67} & \added{63.84} & \added{62.33} & \added{48.64} & \added{47.67} & \added{85.68} & \added{59.14} & \added{+6.11} \\ 
% % GEPA             & \textbf{59.33} & \textbf{64.13} & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 65.22 & +12.19 \\
% % GEPA+Merge       & \textbf{59.33}* & \textbf{64.13}* & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{66.36} & +\textbf{13.33} \\
% % \midrule
% % \multicolumn{9}{l}{\added{Optimized with Qwen3-8B, evaluated on GPT-4.1-Mini}} \\
% % \midrule
% % \added{GEPA-Qwen-Opt}  & \added{52.67} & \added{59.31} & \added{65.67} & \added{49.83} & \added{54.67} & \added{90.05} & \added{62.03} & \added{+9.00} \\
% % \bottomrule
% % \end{tabular}
% % }
% \begin{tabular}{lcccccccc}
% \toprule
% \textbf{GPT-4.1 Mini} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{AIME-2025} & \textbf{LiveBench-Math} & \textbf{Aggregate} & \textbf{Improvement} \\
% % \midrule
% % \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
% \midrule
% Baseline & 38.00 & 47.79 & 46.33 & 78.57 & 49.33 & 58.20 & 53.03 & --- \\
% \added{Trace (OptoPrime)} & \added{60.33} & \added{51.19} & \added{46.00} & \added{74.18} & \added{45.33} & \added{60.74} & \added{56.30} & \added{+3.27} \\
% \added{MIPROv2-No-Demos} & \added{38.00} & \added{52.04} & \added{51.33} & \added{91.85} & \added{48.67} & \added{60.97} & \added{57.14} & \added{+4.11} \\
% MIPROv2 & 58.00 & 49.15 & 48.33 & 83.37 & 51.33 & 61.84 & 58.67 & +5.64 \\
% \added{TextGrad} & \added{62.33} & \added{48.64} & \added{47.67} & \added{85.68} & \added{46.67} & \added{63.84} & \added{59.14} & \added{+6.11} \\ 
% GEPA & \textbf{69.00} & 52.72 & 51.67 & 94.47 & \textbf{59.33} & \textbf{64.13} & 65.22 & +12.19 \\
% GEPA+Merge & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{59.33} & \textbf{64.13} & \textbf{66.36} & +\textbf{13.33} \\
% \midrule
% \multicolumn{9}{l}{\added{Optimized with Qwen3-8B, evaluated on GPT-4.1-Mini}} \\
% \midrule
% \added{GEPA-Qwen-Opt} & \added{65.67} & \added{49.83} & \added{54.67} & \added{90.05} & \added{52.67} & \added{59.31} & \added{62.03} & \added{+9.00} \\
% \bottomrule
% \end{tabular}
% }
% \vspace{-4mm}
% \end{table*}
```

## Table 6
```latex
\begin{table*}[tp]
% \centering
% \caption{Benchmark results for different optimizers over Qwen3 8B and GPT-4.1 Mini models across multiple tasks.}
% \label{tab:main-results}
% \resizebox{0.7\textwidth}{!}{
% \begin{tabular}{lcccccc}
% \toprule
% \textbf{Model} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{7}{l}{\textbf{Qwen3-8B}} \\
% \midrule
% Baseline         & 42.33 & 36.90 & 35.33 & 80.82 & 48.85 & --- \\
% MIPROv2          & 55.33 & 36.22 & 47.33 & 81.55 & 55.11 & +6.26 \\
% GRPO             & 43.33 & 35.88 & 38.67 & 86.66 & 51.14 & +2.29 \\
% % GEPAWLinear      & 58.33 & 30.44 & 45.33 & 85.45 & 54.89 & +6.04 \\
% % GEPAWMergeWLinear& 62.00 & 37.76 & 47.67 & 90.29 & 59.43 & +10.59 \\
% GEPA             & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & \textbf{61.28} & +\textbf{12.44} \\
% GEPA+Merge       & \textbf{64.33} & 28.23 & 51.67 & 86.26 & 57.62 & +8.78 \\
% \midrule
% \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
% \midrule
% Baseline         & 38.00 & 47.79 & 46.33 & 78.57 & 52.67 & --- \\
% MIPROv2          & 58.00 & 49.15 & 48.33 & 83.37 & 59.71 & +7.04 \\
% % GEPAWLinear      & 66.00 & 49.49 & 51.00 & 94.03 & 65.13 & +12.46 \\
% % GEPAWMergeWLinear& 64.00 & 49.15 & 52.67 & 93.34 & 64.79 & +12.12 \\
% GEPA             & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 66.97 & +14.29 \\
% GEPA+Merge       & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{68.69} & +\textbf{16.02} \\
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 7
```latex
\begin{table*}[tp]
% \centering
% \caption{Benchmark results for different optimizers over Qwen3 8B and GPT-4.1 Mini models across multiple tasks.}
% \label{tab:main-results}
% \resizebox{0.7\textwidth}{!}{
% \begin{tabular}{lcccccc}
% \toprule
% \textbf{Model} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{7}{l}{\textbf{Qwen3-8B}} \\
% \midrule
% Baseline         & 42.33 & 36.90 & 35.33 & 80.82 & 48.85 & --- \\
% MIPROv2          & 55.33 & 36.22 & 47.33 & 81.55 & 55.11 & +6.26 \\
% GRPO             & 43.33 & 35.88 & 38.67 & 86.66 & 51.14 & +2.29 \\
% % GEPAWLinear      & 58.33 & 30.44 & 45.33 & 85.45 & 54.89 & +6.04 \\
% % GEPAWMergeWLinear& 62.00 & 37.76 & 47.67 & 90.29 & 59.43 & +10.59 \\
% GEPA             & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & \textbf{61.28} & +\textbf{12.44} \\
% GEPA+Merge       & \textbf{64.33} & 28.23 & 51.67 & 86.26 & 57.62 & +8.78 \\
% \midrule
% \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
% \midrule
% Baseline         & 38.00 & 47.79 & 46.33 & 78.57 & 52.67 & --- \\
% MIPROv2          & 58.00 & 49.15 & 48.33 & 83.37 & 59.71 & +7.04 \\
% % GEPAWLinear      & 66.00 & 49.49 & 51.00 & 94.03 & 65.13 & +12.46 \\
% % GEPAWMergeWLinear& 64.00 & 49.15 & 52.67 & 93.34 & 64.79 & +12.12 \\
% GEPA             & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 66.97 & +14.29 \\
% GEPA+Merge       & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{68.69} & +\textbf{16.02} \\
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 8
```latex
\begin{table*}[ht]
% \centering
% \caption{Benchmark results for qwen3-8b and gpt-41-mini models across multiple tasks (no FSABench).}
% \label{tab:main-results-no-fsa}
% \resizebox{\textwidth}{!}{
% \begin{tabular}{l|cccc|cc}
% \toprule
% \textbf{Model} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{Papillon} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{7}{l}{\textbf{Qwen3-8B}} \\
% \midrule
% Baseline         & 42.33 & 36.90 & 35.33 & 80.82 & 48.85 & --- \\
% MIPROv2          & 55.33 & 36.22 & 47.33 & 81.55 & 55.11 & +6.26 \\
% GRPO             & 43.33 & 35.88 & 38.67 & 86.66 & 51.14 & +2.29 \\
% % GEPAWLinear      & 58.33 & 30.44 & 45.33 & 85.45 & 54.89 & +6.04 \\
% % GEPAWMergeWLinear& 62.00 & 37.76 & 47.67 & 90.29 & 59.43 & +10.59 \\
% GEPA             & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & \textbf{61.28} & +\textbf{12.44} \\
% GEPA+Merge       & \textbf{64.33} & 28.23 & 51.67 & 86.26 & 57.62 & +8.78 \\
% \midrule
% \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
% \midrule
% Baseline         & 38.00 & 47.79 & 46.33 & 78.57 & 52.67 & --- \\
% MIPROv2          & 58.00 & 49.15 & 48.33 & 83.37 & 59.71 & +7.04 \\
% % GEPAWLinear      & 66.00 & 49.49 & 51.00 & 94.03 & 65.13 & +12.46 \\
% % GEPAWMergeWLinear& 64.00 & 49.15 & 52.67 & 93.34 & 64.79 & +12.12 \\
% GEPA             & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 66.97 & +14.29 \\
% GEPA+Merge       & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{68.69} & +\textbf{16.02} \\
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 9
```latex
\begin{table*}[ht]
% \centering
% \caption{Benchmark results for qwen3-8b and gpt-41-mini models across multiple tasks (no FSABench).}
% \label{tab:main-results-no-fsa}
% \resizebox{\textwidth}{!}{
% \begin{tabular}{l|cccc|cc}
% \toprule
% \textbf{Model} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{7}{l}{\textbf{Qwen3 8B}} \\
% \midrule
% Baseline & 42.33 & 36.90 & 35.33 & 80.82 & 48.35 & --- \\
% MIPROv2 & 55.33 & 36.22 & 47.33 & 81.55 & 55.61 & +7.26 \\
% GRPO (24K steps) & 43.33 & 35.88 & 38.67 & 86.66 & 51.64 & +3.29 \\
% % GEPA & 58.33 & 30.44 & 45.33 & 85.45 & 54.39 & +6.04 \\
% % GEPA\{M\} & 62.00 & 37.76 & 47.67 & 90.29 & 59.43 & +11.08 \\
% GEPA & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & \textbf{61.78} & +\textbf{13.43} \\
% GEPA+Merge & \textbf{64.33} & 28.23 & 51.67 & 86.26 & 57.12 & +8.77 \\
% \midrule
% \multicolumn{7}{l}{\textbf{GPT 4.1 mini}} \\
% \midrule
% Baseline & 38.00 & 47.79 & 46.33 & 78.57 & 52.17 & --- \\
% MIPROv2 & 58.00 & 49.15 & 48.33 & 83.37 & 59.21 & +7.04 \\
% % GEPA & 66.00 & 49.49 & 51.00 & 94.03 & 65.63 & +13.46 \\
% % GEPA\{M\} & 64.00 & 49.15 & 52.67 & 93.34 & 64.79 & +12.62 \\
% GEPA & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 66.97 & +14.80 \\
% GEPA+Merge & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{68.69} & +\textbf{16.52} \\
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 10
```latex
\begin{table*}[ht]
% \centering
% \caption{Benchmark results for qwen3-8b and gpt-41-mini models across multiple tasks. (Columns reordered)}
% \label{tab:main-results-reordered}
% \resizebox{\textwidth}{!}{
% \begin{tabular}{l|ccccc|cc}
% \toprule
% \textbf{Model} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{FSABench} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{8}{l}{\textbf{Qwen3 8B}} \\
% \midrule
% Baseline & 42.33 & 36.90 & 35.33 & 80.82 & 71.42 & 53.36 & --- \\
% MIPROv2 & 55.33 & 36.22 & 47.33 & 81.55 & 82.55 & 60.60 & +7.24 \\
% GRPO (24K steps) & 43.33 & 35.88 & 38.67 & 86.66 & \textbf{90.64} & 59.04 & +5.68 \\
% % GEPA & 58.33 & 30.44 & 45.33 & 85.45 & 85.00 & 60.91 & +7.55 \\
% % GEPA\{M\} & 62.00 & 37.76 & 47.67 & 90.29 & 85.59 & 64.66 & +11.30 \\
% GEPA & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & 82.16 & \textbf{65.46} & +\textbf{12.10} \\
% GEPA+Merge & \textbf{64.33} & 28.23 & 51.67 & 86.26 & 82.84 & 62.67 & +9.31 \\
% \midrule
% \multicolumn{8}{l}{\textbf{GPT 4.1 mini}} \\
% \midrule
% Baseline & 38.00 & 47.79 & 46.33 & 78.57 & 80.74 & 58.29 & --- \\
% MIPROv2 & 58.00 & 49.15 & 48.33 & 83.37 & 87.65 & 65.30 & +7.01 \\
% % GEPA & 66.00 & 49.49 & 51.00 & 94.03 & 87.11 & 69.53 & +11.24 \\
% % GEPA\{M\} & 64.00 & 49.15 & 52.67 & 93.34 & \textbf{89.61} & 69.75 & +11.47 \\
% GEPA & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 88.04 & 71.18 & +12.89 \\
% GEPA+Merge & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & 88.53 & \textbf{72.66} & +\textbf{14.37} \\
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 11
```latex
\begin{table*}[ht]
% \centering
% \caption{Benchmark results for qwen3-8b and gpt-41-mini models across multiple tasks. (Columns reordered)}
% \label{tab:main-results-reordered}
% \resizebox{\textwidth}{!}{
% \begin{tabular}{l|ccccc|cc}
% \toprule
% \textbf{Model} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{FSABench} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{8}{l}{\textbf{Qwen3 8B}} \\
% \midrule
% Baseline & 42.33 & 36.90 & 35.33 & 80.82 & 71.42 & 53.36 & --- \\
% MIPROv2 & 55.33 & 36.22 & 47.33 & 81.55 & 82.55 & 60.60 & +7.24 \\
% GRPO (24K steps) & 43.33 & 35.88 & 38.67 & 86.66 & \textbf{90.64} & 59.04 & +5.68 \\
% GEPA & 58.33 & 30.44 & 45.33 & 85.45 & 85.00 & 60.91 & +7.55 \\
% GEPA\{M\} & 62.00 & 37.76 & 47.67 & 90.29 & 85.59 & 64.66 & +11.30 \\
% GEPA\{P\} & 62.33 & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & 82.16 & \textbf{65.46} & +\textbf{12.10} \\
% GEPA\{M\}\{P\} & \textbf{64.33} & 28.23 & 51.67 & 86.26 & 82.84 & 62.67 & +9.31 \\
% \midrule
% \multicolumn{8}{l}{\textbf{GPT 4.1 mini}} \\
% \midrule
% Baseline & 38.00 & 47.79 & 46.33 & 78.57 & 80.74 & 58.29 & --- \\
% MIPROv2 & 58.00 & 49.15 & 48.33 & 83.37 & 87.65 & 65.30 & +7.01 \\
% GEPA & 66.00 & 49.49 & 51.00 & 94.03 & 87.11 & 69.53 & +11.24 \\
% GEPA\{M\} & 64.00 & 49.15 & 52.67 & 93.34 & \textbf{89.61} & 69.75 & +11.47 \\
% GEPA\{P\} & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 88.04 & 71.18 & +12.89 \\
% GEPA\{M\}\{P\} & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & 88.53 & \textbf{72.66} & +\textbf{14.37} \\
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 12
```latex
\begin{table*}[ht]
% \centering
% \caption{Benchmark results for qwen3-8b and gpt-41-mini models across multiple tasks.}
% \label{tab:main-results}
% \resizebox{\textwidth}{!}{
% \begin{tabular}{l|ccccc|cc}
% \toprule
% \textbf{Model} & \textbf{FSABench} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Papillon} & \textbf{Hover} & \textbf{Aggregate} & \textbf{Improvement} \\
%  % & & \textbf{Bench} & & & \textbf{Bench} & & \\
%  % & (\textit{FacilitySupportAnalyzerMM}) & (\textit{HotpotMultiHop}) & (\textit{IFBenchCoT2StageProgram}) & (\textit{PAPILLON}) & (\textit{HoverMultiHop}) & & \\
% \midrule
% \multicolumn{8}{l}{\textbf{Qwen3 8B}} \\
% \midrule
% Baseline & 71.42 & 42.33 & 36.90 & 80.82 & 35.33 & 53.36 & --- \\
% MIPROv2 & 82.55 & 55.33 & 36.22 & 81.55 & 47.33 & 60.60 & +7.24 \\
% GRPO (24K steps) & \textbf{90.64} & 43.33 & 35.88 & 86.66 & 38.67 & 59.04 & +5.68 \\
% % GEPA & 85.00 & 58.33 & 30.44 & 85.45 & 45.33 & 60.91 & +7.55 \\
% % GEPA\{M\} & 85.59 & 62.00 & 37.76 & 90.29 & 47.67 & 64.66 & +11.30 \\
% GEPA & 82.16 & 62.33 & \textbf{38.61} & \textbf{91.85} & \textbf{52.33} & \textbf{65.46} & +\textbf{12.10} \\
% GEPA+Merge & 82.84 & \textbf{64.33} & 28.23 & 86.26 & 51.67 & 62.67 & +9.31 \\
% \midrule
% \multicolumn{8}{l}{\textbf{GPT 4.1 mini}} \\
% \midrule
% Baseline & 80.74 & 38.00 & 47.79 & 78.57 & 46.33 & 58.29 & --- \\
% MIPROv2 & 87.65 & 58.00 & 49.15 & 83.37 & 48.33 & 65.30 & +7.01 \\
% % GEPA & 87.11 & 66.00 & 49.49 & 94.03 & 51.00 & 69.53 & +11.24 \\
% % GEPA\{M\} & \textbf{89.61} & 64.00 & 49.15 & 93.34 & 52.67 & 69.75 & +11.47 \\
% GEPA & 88.04 & \textbf{69.00} & 52.72 & 94.47 & 51.67 & 71.18 & +12.89 \\
% GEPA+Merge & 88.53 & 65.67 & \textbf{55.95} & \textbf{96.46} & \textbf{56.67} & \textbf{72.66} & +\textbf{14.37} \\
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 13
```latex
\begin{table*}[htp]
\centering
% \caption{Comparing candidate selection strategies across different tasks with Qwen3 8B. At each step, \lstinline{SelectBestCandidate} \added{(used by TextGrad)} evolves the candidate prompt only from the top-scoring candidate, \added{while BeamSearch selects uniformly from top-N candidates}, which are more prone to getting stuck in a local optimum. \added{In comparison, GEPA's Pareto-based candidate selection strategy leads to +12.44\% improvement over baseline, significantly outperforming the +6.04\% and +5.11\% improvements of other candidate selection strategies, while keeping the evolution harness fixed.}}
\caption{Comparing candidate selection strategies across different tasks with Qwen3 8B \added{while keeping the evolution harness fixed}. 
At each step, \lstinline{SelectBestCandidate} \added{(used by TextGrad~\cite{textgrad})} evolves only from the top-scoring candidate. \lstinline{BeamSearch} maintains a pool of the top-N candidates (used by APO~\cite{pryzant_apo}), but is still prone to local optima. In comparison, GEPA's Pareto-based selection yields a +12.44\% improvement, significantly outperforming the +6.05\% and +5.11\% gains of greedy and beam-search strategies respectively.}
\label{tab:ablation_1}
\resizebox{0.8\textwidth}{!}{
\begin{tabular}{lcccccc}
\toprule
\textbf{Qwen3 8B} & \textbf{HotpotQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{Aggregate} & \textbf{Improvement} \\
% \midrule
% \multicolumn{7}{l}{\textbf{Qwen3-8B}} \\
\midrule
% Baseline         & 42.33 & 36.90 & 35.33 & 80.82 & 48.85 & --- \\
% MIPROv2          & 55.33 & 36.22 & 47.33 & 81.55 & 55.11 & +6.26 \\
% GRPO             & 43.33 & 35.88 & 38.67 & 86.66 & 51.14 & +2.29 \\
Baseline & 42.33 & 36.90 & 35.33 & 80.82 & 48.84 & --- \\
SelectBestCandidate      & 58.33 & 30.44 & 45.33 & 85.45 & 54.89 & +6.05 \\
\added{BeamSearch}               & \added{57.33} & \added{36.39} & \added{41.00} & \added{81.08} & \added{53.95} & \added{+5.11} \\
% GEPAWMergeWLinear& 62.00 & 37.76 & 47.67 & 90.29 & 59.43 & +10.59 \\
GEPA             & \textbf{62.33} & \textbf{38.61} & \textbf{52.33} & \textbf{91.85} & \textbf{61.28} & \textbf{+12.44} \\
% GEPA+Merge       & \textbf{64.33} & 28.23 & 51.67 & 86.26 & 57.62 & +8.78 \\
% \midrule
% \multicolumn{7}{l}{\textbf{GPT-4.1 mini}} \\
% \midrule
% Baseline         & 38.00 & 47.79 & 46.33 & 78.57 & 52.67 & --- \\
% MIPROv2          & 58.00 & 49.15 & 48.33 & 83.37 & 59.71 & +7.04 \\
% % GEPAWLinear      & 66.00 & 49.49 & 51.00 & 94.03 & 65.13 & +12.46 \\
% % GEPAWMergeWLinear& 64.00 & 49.15 & 52.67 & 93.34 & 64.79 & +12.12 \\
% GEPA             & \textbf{69.00} & 52.72 & 51.67 & 94.47 & 66.97 & +14.29 \\
% GEPA+Merge       & 65.67 & \textbf{55.95} & \textbf{56.67} & \textbf{96.46} & \textbf{68.69} & +\textbf{16.02} \\
\bottomrule
\end{tabular}
}
\end{table*}
```

