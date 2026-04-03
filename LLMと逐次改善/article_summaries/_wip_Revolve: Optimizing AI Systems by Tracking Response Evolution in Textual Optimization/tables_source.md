# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
\centering
\caption{Prompt optimization results for reasoning tasks for various LLMs, with GPT-4o as the optimization engine. The values in parentheses represent the relative improvement in accuracy of the method compared to TextGrad.}
\vspace{-5pt}
% \lyc{We will need to unify notations like bolds and underlines in tables.}
\label{tab:prompt_optimization}
\resizebox{.75\linewidth}{!}{
\begin{tabular}{c|c|cccc}
    \toprule
    \multirow{2}{*}{Dataset} & \multirow{2}{*}{Models} & \multicolumn{4}{c}{\textbf{Accuracy \% (Improv. over TextGrad)}} \\
    \cmidrule(lr){3-6}
    ~ & ~ & CoT & TextGrad & M-TextGrad & REVOLVE \\
    \midrule
    \multirow{4}{*}{Object Counting} 
    & GPT-3.5 & 77.8 (15.3\%$\downarrow$) & 91.9 (-) & 92.1 (0.2\%$\uparrow$) & \textbf{95.5 ± 0.9\% (3.9\%$\uparrow$)} \\
    & GPT-4 & 92.1 (2.2\%$\downarrow$) & 94.2 (-) & 90.0 (4.5\%$\downarrow$) & \textbf{96.3 ± 0.6\% (2.2\%$\uparrow$)} \\
    & Gemini 1.5 Pro & 94.0 (0.0\%) & 94.0 (-) & 94.0 (0.0\%) & 94.0 ± 0.0\% (0.0\%) \\
    & Llama 3.1 8B Instruct & 65.0 (15.6\%$\downarrow$) & 77.0 (-) & 80.0 (3.9\%$\uparrow$) & \textbf{83.0 ± 1.4\% (7.8\%$\uparrow$)} \\
    \midrule
    \multirow{4}{*}{GSM8k} 
    & GPT-3.5 & 72.9 (9.9\%$\downarrow$) & 80.9 (-) & 82.1 (1.5\%$\uparrow$) & \textbf{85.9 ± 0.6\% (6.2\%$\uparrow$)} \\
    & GPT-4 & 92.6 (0.4\%$\downarrow$) & 93.0 (-) & 93.9 (1.0\%$\uparrow$) & \textbf{94.5 ± 0.4\% (1.6\%$\uparrow$)} \\
    & Gemini 1.5 Pro & 92.9 (0.4\%$\downarrow$) & 93.3 (-) & \textbf{93.9 (0.6\%$\uparrow$)} & 93.0 ± 0.3\% (0.3\%$\downarrow$) \\
    & Llama 3.1 8B Instruct & 84.6 (0.0\%) & 84.6 (-) & 84.6 (0.0\%) & 84.6 ± 0.0\% (0.0\%) \\
    \bottomrule
\end{tabular}
}
\vspace{-5pt}
\end{table*}
```

## Table 2
```latex
\begin{table*}[h]
% \small 
% \centering
% \renewcommand{\arraystretch}{1.2}
% \caption{Prompt optimization for reasoning tasks. With REVOLVE, we optimize a system prompt for gpt-3.5-turbo-0125 using gpt-4o as the gradient engine that provides the feedback during backpropagation}
% \begin{tabular}{ccc}
% \hline
% \textbf{Dataset} & \textbf{Method} & \textbf{Accuracy (\%)}\\ \hline
% \multirow{4}{*}{Object Counting~\citep{suzgun2022challenging,srivastava2022beyond}} & CoT (0-shot) & 65.0\\   
% & DSPy (BFSR, 8 demonstrations) & 68.0\\
%  & TextGrad (instruction-only, 0 demonstrations) & 77.0\\
%  & REVOLVE (instruction-only, 0 demonstrations) & 83.0\\ \hline
% % \multirow{4}{*}{Word Sorting~\citep{suzgun2022challenging,srivastava2022beyond}} & CoT (0-shot) & 76.7\\   
% % & DSPy (BFSR, 8 demonstrations) & 79.8\\
% %  & TextGrad (instruction-only, 0 demonstrations) & 79.8\\
% %  & REVOLVE (instruction-only, 0 demonstrations) & TBD\\ \hline
%  \multirow{4}{*}{GSM8k~\citep{cobbe2021training}} & CoT (0-shot) & 72.9\\   
% & DSPy (BFSR, 8 demonstrations) & 81.1\\
%  & TextGrad (instruction-only, 0 demonstrations) & 81.1\\
%  & REVOLVE (instruction-only, 0 demonstrations) & TBD\\ \hline
% \end{tabular}
% \label{tab:ori_head_number}
% \end{table*}
```

## Table 3
```latex
\begin{table*}[t]
% \centering
% \small 
% \caption{Solution optimization results for Llama 3.1 8B Instruct, with itself as the optimization engine. The values in parentheses represent the relative improvement of the method compared to TextGrad.}
% \vspace{-5pt}
% \label{tab:solution_optimization}
% \resizebox{.9\linewidth}{!}{
% \begin{tabular}{c|c|cccc}
%     \toprule
%     \multirow{2}{*}{Dataset} & \multirow{2}{*}{Stage} & \multicolumn{4}{c}{\textbf{Accuracy \% (Improv. over TextGrad)}} \\
%     \cmidrule(lr){3-6}
%     ~ & ~ & CoT & TextGrad & M-TextGrad & REVOLVE \\
%     \midrule
%     \multirow{5}{*}{Google-proof QA} 
%     & Before Training & 21.7 (0.0\%) & 21.7 (-) & 21.7 (0.0\%) & 21.7 (0.0\%) \\
%     & 1st Iteration & - & 25.8 (-) & 26.5 (2.7\%$\uparrow$) & \textbf{26.8 (3.88\%$\uparrow$)} \\
%     & 2nd Iteration & - & 26.8 (-) & 29.3 (9.3\%$\uparrow$) & \textbf{29.8 (11.19\%$\uparrow$)} \\
%     & 3rd Iteration & - & 24.8 (-) & 25.7 (3.6\%$\uparrow$) & \textbf{27.8 (12.10\%$\uparrow$)} \\
%     & Final Results & 21.7 (8.4\%$\downarrow$) & 23.7 (-) & 25.1 (5.9\%$\uparrow$) & \textbf{28.3 (19.41\%$\uparrow$)} \\
%     \midrule
%     \multirow{5}{*}{MMLU-Machine Learning} 
%     & Before Training & 51.8 (0.0\%) & 51.8 (-) & 51.8 (0.0\%) & 51.8 (0.0\%) \\
%     & 1st Iteration & - & 43.8 (-) & 46.9 (7.1\%$\uparrow$) & \textbf{48.2 (10.05\%$\uparrow$)} \\
%     & 2nd Iteration & - & 43.8 (-) & 45.2 (3.2\%$\uparrow$) & \textbf{47.3 (7.99\%$\uparrow$)} \\
%     & 3rd Iteration & - & 43.8 (-)  & 44.4 (1.4\%$\uparrow$) & \textbf{46.4 (5.94\%$\uparrow$)} \\
%     & Final Results & 51.8 (9.5\%$\uparrow$) & 47.3 (-) & 47.4 (0.2\%$\uparrow$) & \textbf{57.1 (20.72\%$\uparrow$)} \\
%     \midrule
%     \multirow{5}{*}{MMLU-College Physics} 
%     & Before Training & 54.7 (0.0\%) & 54.7 (-) & 54.7 (0.0\%) & 54.7 (0.0\%) \\
%     & 1st Iteration &  - & 51.1 (-) & 55.9 (9.4\%$\uparrow$) & \textbf{58.3 (14.1\%$\uparrow$)} \\
%     & 2nd Iteration & - & 51.1 (-) & 61.0 (19.4\%$\uparrow$) & \textbf{62.0 (21.3\%$\uparrow$)} \\
%     & 3rd Iteration & - & 55.7 (-) & 60.3 (8.3\%$\uparrow$) & \textbf{65.7 (18.0\%$\uparrow$)} \\
%     & Final Results & 54.7 (9.3\%$\downarrow$) & 60.3 (-) & 61.6 (2.2\%$\uparrow$) & \textbf{66.4 (10.1\%$\uparrow$)} \\
%     \bottomrule
% \end{tabular}
% }
% % \vspace{-20pt}
% \end{table*}
```

## Table 4
```latex
\begin{table*}[htbp]
\centering
\small 
\caption{Solution optimization results for various LLM, with themselves as the optimization engine. The values in parentheses represent the relative improvement of the method compared to TextGrad.}
% \vspace{-5pt}
\label{tab:solution_optimization}
\resizebox{\linewidth}{!}{
\begin{tabular}{c|c|c|cccc}
    \toprule
    \multirow{2}{*}{Dataset} & \multirow{2}{*}{Models} & \multirow{2}{*}{Stage} & \multicolumn{4}{c}{\textbf{Accuracy \% (Improv. over TextGrad)}} \\
    \cmidrule(lr){4-7}
    ~ & ~ & ~ & CoT & TextGrad & M-TextGrad & REVOLVE \\
    \midrule
    \multirow{15}{*}{Google-proof QA} & \multirow{5}{*}{GPT-4o}
    & Before Training & 50.4 (0.0\%) & 50.4 (-) & 50.4 (0.0\%) & 50.4 (0.0\%) \\
    & & 1st Iteration & - & 50.4 (-) & \textbf{51.1 (1.3\%$\uparrow$)} & 50.9 ± 0.4\% (0.99\%$\uparrow$) \\
    & & 2nd Iteration & - & 50.5 (-) & 50.7 (0.4\%$\uparrow$) & \textbf{51.3 ± 0.5\% (1.58\%$\uparrow$)} \\
    & & 3rd Iteration & - & 50.5 (-) & 51.9 (2.7\%$\uparrow$) & \textbf{52.9 ± 0.6\% (4.75\%$\uparrow$)} \\
    & & Final Results & 50.4 (2.1\%$\downarrow$) & 51.5 (-) & 52.4 (1.7\%$\uparrow$) & \textbf{53.0 ± 0.7\% (2.91\%$\uparrow$)} \\ \cmidrule(lr){2-7}
    % \midrule
    & \multirow{5}{*}{GPT-4-0125-preview}
    & Before Training & 38.8 (0.0\%) & 38.8 (-) & 38.8 (0.0\%) & 38.8 (0.0\%) \\
    & & 1st Iteration & - & 38.5 (-) & 39.3 (2.0\%$\uparrow$) & \textbf{39.5 ± 0.3\% (2.60\%$\uparrow$)} \\
    & & 2nd Iteration & - & 38.3 (-) & 40.1 (4.7\%$\uparrow$) & \textbf{40.3 ± 0.5\% (5.22\%$\uparrow$)} \\
   &  & 3rd Iteration & - & 38.2 (-) & 40.4 (5.7\%$\uparrow$) & \textbf{41.0 ± 0.4\% (7.33\%$\uparrow$)} \\
    & & Final Results & 38.8 (1.8\%$\uparrow$) & 38.1 (-) & 41.5 (8.9\%$\uparrow$) & \textbf{42.2 ± 0.6\% (10.76\%$\uparrow$)} \\ \cmidrule(lr){2-7}
    % \midrule
    & \multirow{5}{*}{Llama 3.1 8B Instruct}
    & Before Training & 21.7 (0.0\%) & 21.7 (-) & 21.7 (0.0\%) & 21.7 (0.0\%) \\
    & & 1st Iteration & - & 25.8 (-) & 26.5 (2.7\%$\uparrow$) & \textbf{26.8 ± 0.2\% (3.88\%$\uparrow$)} \\
    & & 2nd Iteration & - & 26.8 (-) & 29.3 (9.3\%$\uparrow$) & \textbf{29.8 ± 0.5\% (11.19\%$\uparrow$)} \\
   &  & 3rd Iteration & - & 24.8 (-) & 25.7 (3.6\%$\uparrow$) & \textbf{27.8 ± 0.5\% (12.10\%$\uparrow$)} \\
   &  & Final Results & 21.7 (8.4\%$\downarrow$) & 23.7 (-) & 25.1 (5.9\%$\uparrow$) & \textbf{28.3 ± 0.4\% (19.41\%$\uparrow$)} \\
    \midrule
    \multirow{15}{*}{MMLU-Machine Learning} & \multirow{5}{*}{GPT-4o}
    & Before Training & 85.5 (0.0\%) & 85.5 (-) & 85.5 (0.0\%) & 85.5 (0.0\%) \\
    & & 1st Iteration & - & 85.5 (-) & 85.5 (0.0\%) & \textbf{85.8 ± 0.5\% (0.35\%$\uparrow$)} \\
    & & 2nd Iteration & - & 85.6 (-) & 85.4 (0.2\%$\downarrow$) & \textbf{86.1 ± 1.0\% (0.58\%$\uparrow$)} \\
    & & 3rd Iteration & - & 85.6 (-)  & 85.3 (0.3\%$\downarrow$) & \textbf{86.4 ± 1.1\% (0.93\%$\uparrow$)} \\
    & & Final Results & 85.5 (0.3\%$\downarrow$) & 85.8 (-) & 85.0 (0.9\%$\downarrow$) & \textbf{86.7 ± 0.8\% (1.05\%$\uparrow$)} \\ \cmidrule(lr){2-7}
    % \midrule
    & \multirow{5}{*}{GPT-4-0125-preview}
    & Before Training & 76.3 (0.0\%) & 76.3 (-) & 76.3 (0.0\%) & 76.3 (0.0\%) \\
    & & 1st Iteration & - & 76.4 (-) & \textbf{77.2 (1.0\%$\uparrow$)} & 77.1 ± 0.4\% (0.92\%$\uparrow$) \\
    & & 2nd Iteration & - & 76.6 (-) & 77.8 (1.5\%$\uparrow$) & \textbf{77.9 ± 0.6\% (1.70\%$\uparrow$)} \\
    & & 3rd Iteration & - & 77.0 (-)  & 78.1 (1.4\%$\uparrow$) & \textbf{79.2 ± 0.7\% (2.86\%$\uparrow$)} \\
    & & Final Results & 76.3 (3.3\%$\downarrow$) & 78.9 (-) & 79.2 (0.3\%$\uparrow$) & \textbf{81.0 ± 0.8\% (2.66\%$\uparrow$)} \\ \cmidrule(lr){2-7}
    % \midrule
    & \multirow{5}{*}{Llama 3.1 8B Instruct}
    & Before Training & 51.8 (0.0\%) & 51.8 (-) & 51.8 (0.0\%) & 51.8 (0.0\%) \\
    & & 1st Iteration & - & 43.8 (-) & 46.9 (7.1\%$\uparrow$) & \textbf{48.2 ± 0.3\% (10.05\%$\uparrow$)} \\
    & & 2nd Iteration & - & 43.8 (-) & 45.2 (3.2\%$\uparrow$) & \textbf{47.3 ± 0.5\% (7.99\%$\uparrow$)} \\
    & & 3rd Iteration & - & 43.8 (-)  & 44.4 (1.4\%$\uparrow$) & \textbf{46.4 ± 0.6\% (5.94\%$\uparrow$)} \\
    & & Final Results & 51.8 (9.5\%$\uparrow$) & 47.3 (-) & 47.4 (0.2\%$\uparrow$) & \textbf{57.1 ± 0.6\% (20.72\%$\uparrow$)} \\
    \midrule
    \multirow{15}{*}{MMLU-College Physics} & \multirow{5}{*}{GPT-4o}
    & Before Training & 91.0 (0.0\%) & 91.0 (-) & 91.0 (0.0\%) & 91.0 (0.0\%) \\
    & & 1st Iteration &  - & 91.6 (-) & 91.6 (0.0\%) & \textbf{91.8 ± 0.5\% (0.22\%$\uparrow$)} \\
    & & 2nd Iteration & - & 92.1 (-) & 92.3 (0.2\%$\uparrow$) & \textbf{92.5 ± 0.7\% (0.43\%$\uparrow$)} \\
    & & 3rd Iteration & - & 92.8 (-) & 91.2 (1.7\%$\downarrow$) & \textbf{93.2 ± 0.8\% (0.43\%$\uparrow$)} \\
    & & Final Results & 91.0 (2.7\%$\downarrow$) & 93.5 (-) & 91.3 (2.3\%$\downarrow$) & \textbf{94.1 ± 0.9\% (0.64\%$\uparrow$)} \\ \cmidrule(lr){2-7}
    % \midrule
    & \multirow{5}{*}{GPT-4-0125-preview}
    & Before Training & 81.6 (0.0\%) & 81.6 (-) & 81.6 (0.0\%) & 81.6 (0.0\%) \\
    & & 1st Iteration &  - & 82.4 (-) & 81.9 (0.6\%$\downarrow$) & \textbf{82.5 ± 0.3\% (0.12\%$\uparrow$)} \\
    & & 2nd Iteration & - & 83.1 (-) & 82.4 (0.8\%$\downarrow$) & \textbf{83.4 ± 0.4\% (0.36\%$\uparrow$)} \\
    & & 3rd Iteration & - & 84.1 (-) & 82.1 (2.4\%$\downarrow$) & \textbf{84.5 ± 0.6\% (0.48\%$\uparrow$)} \\
    & & Final Results & 81.6 (4.7\%$\downarrow$) & 85.6 (-) & 82.3 (3.8\%$\downarrow$) & \textbf{85.9 ± 0.7\% (0.35\%$\uparrow$)} \\ \cmidrule(lr){2-7}
    % \midrule
    & \multirow{5}{*}{Llama 3.1 8B Instruct}
    & Before Training & 54.7 (0.0\%) & 54.7 (-) & 54.7 (0.0\%) & 54.7 (0.0\%) \\
    & & 1st Iteration &  - & 51.1 (-) & 55.9 (9.4\%$\uparrow$) & \textbf{58.3 ± 0.2\% (14.09\%$\uparrow$)} \\
    & & 2nd Iteration & - & 51.1 (-) & 61.0 (19.4\%$\uparrow$) & \textbf{62.0 ± 0.4\% (21.33\%$\uparrow$)} \\
    & & 3rd Iteration & - & 55.7 (-) & 60.3 (8.3\%$\uparrow$) & \textbf{65.7 ± 0.5\% (17.95\%$\uparrow$)} \\
    & & Final Results & 54.7 (9.3\%$\downarrow$) & 60.3 (-) & 61.6 (2.2\%$\uparrow$) & \textbf{66.4 ± 0.5\% (10.12\%$\uparrow$)} \\
    \bottomrule
\end{tabular}
}
% \vspace{-50pt}
\end{table*}
```

## Table 5
```latex
\begin{table*}[h]
% \small 
% \centering
% \renewcommand{\arraystretch}{1.2}
% \caption{Solution optimization for zero-shot question answering with Llama 3.1 8B Instruct}
% \begin{tabular}{ccc}
% \hline
% \textbf{Dataset} & \textbf{Method} & \textbf{Accuracy (\%)}\\ \hline
% \multirow{4}{*}{Google-proof QA ~\citep{suzgun2022challenging,srivastava2022beyond}} & CoT & TBD\\   
% & Best Reported & TBD\\
%  & TextGrad  & 23.7\\
%  & REVOLVE  & 28.3\\ \hline
% \multirow{3}{*}{MMLU-Machine Learning~\citep{suzgun2022challenging,srivastava2022beyond}} & CoT  & 85.7\\   
%  & TextGrad  & 88.4\\
%  & REVOLVE  & TBD\\ \hline
%  \multirow{3}{*}{MMLU-College Physics~\citep{cobbe2021training}} & CoT & 91.2\\   
%  & TextGrad  & 95.1\\
%  & REVOLVE  & TBD\\ \hline
% \end{tabular}
% \label{tab:solution}
% \end{table*}
```

## Table 6
```latex
\begin{table*}[h]
% \centering
% \vspace{-5pt}
% % \renewcommand{\arraystretch}{1.2}
% \Huge 
% \caption{Code optimization results (averaged over 5 seeds) for Llama 3.1 8B Instruct, with itself as the optimization engine. The values in parentheses represent the relative improvement in completion rate of the method compared to TextGrad.}
% \vspace{-5pt}
% \resizebox{0.85\linewidth}{!}{
% \begin{tabular}{ccc}
% \toprule
% \textbf{Dataset} & \textbf{Method} & \textbf{Completion Rate (Improv. over TextGrad)}\\ \hline
% \multirow{5}{*}{LeetCode Hard} & Zero-shot & 0.12 (50\%$\downarrow$)\\   
% & Reflexion (1 demonstration, 5 iterations) & 0.20 ± 0.002 (16.67\%$\uparrow$)\\
%  & TextGrad (0 demonstrations, 5 iterations) & 0.24 ± 0.005 (-)\\
%  & M-TextGrad (0 demonstrations, 5 iterations) & 0.25 ± 0.003 (4.17\%$\uparrow$)\\
%  & REVOLVE (0 demonstrations, 5 iterations) & \textbf{0.31 ± 0.006} \textbf{(29.17\%$\uparrow$)}\\
% \bottomrule
% \end{tabular}}
% \vspace{-10pt}
% \label{tab:code_optimization}
% \end{table*}
```

## Table 7
```latex
\begin{table*}[h]
\centering
% \vspace{-5pt}
% \renewcommand{\arraystretch}{1.2}
\Huge 
\caption{Code optimization results (averaged over 5 seeds) on LeetCode Hard dataset for various LLMs, with themselves as the optimization engine. The values in parentheses represent the relative improvement in completion rate of the method compared to TextGrad.}
% \vspace{-5pt}
\resizebox{\linewidth}{!}{
\begin{tabular}{c|c|c}
\toprule
\textbf{Models}  &\textbf{Method} & \textbf{Completion Rate (Improv. over TextGrad)}\\ \hline
\multirow{5}{*}{GPT-4o} & Zero-shot & 0.38 (25.49\%$\downarrow$)\\   
& Reflexion (1 demonstration, 5 iterations) & 0.42 ± 0.003 (17.65\%$\downarrow$)\\
 & TextGrad (0 demonstrations, 5 iterations) & 0.51 ± 0.005 (-)\\
 & M-TextGrad (0 demonstrations, 5 iterations) & 0.49 ± 0.005 (3.92\%$\downarrow$)\\
 & REVOLVE (0 demonstrations, 5 iterations) & \textbf{0.52 ± 0.002} \textbf{(1.96\%$\uparrow$)}\\
 \midrule
 \multirow{5}{*}{GPT-4-0125-preview} & Zero-shot & 0.33 (35.29\%$\downarrow$)\\   
& Reflexion (1 demonstration, 5 iterations) & 0.41 ± 0.002 (19.61\%$\downarrow$)\\
 & TextGrad (0 demonstrations, 5 iterations) & 0.51 ± 0.003 (-)\\
 & M-TextGrad (0 demonstrations, 5 iterations) & 0.45 ± 0.006 (11.76\%$\downarrow$)\\
 & REVOLVE (0 demonstrations, 5 iterations) & \textbf{0.56 ± 0.003} \textbf{(9.80\%$\uparrow$)}\\
 \midrule
 \multirow{5}{*}{Llama 3.1 8B Instruct} & Zero-shot & 0.12 (50\%$\downarrow$)\\   
& Reflexion (1 demonstration, 5 iterations) & 0.20 ± 0.002 (16.67\%$\downarrow$)\\
 & TextGrad (0 demonstrations, 5 iterations) & 0.24 ± 0.005 (-)\\
 & M-TextGrad (0 demonstrations, 5 iterations) & 0.25 ± 0.003 (4.17\%$\uparrow$)\\
 & REVOLVE (0 demonstrations, 5 iterations) & \textbf{0.31 ± 0.006} \textbf{(29.17\%$\uparrow$)}\\
 \midrule
\bottomrule
\end{tabular}}
% \vspace{-10pt}
\label{tab:code_optimization}
\end{table*}
```

## Table 8
```latex
\begin{table*}[t]
% \centering
% \small 
% \caption{Comparison of computational resources (GPU memory and runtime) for REVOLVE and baseline methods across tasks.}
% \vspace{-5pt}
% \label{tab:efficiency}
% \resizebox{\linewidth}{!}{
% \begin{tabular}{c|c|ccc|ccc|ccc}
%     \toprule
%     \multirow{2}{*}{Dataset} & \multirow{2}{*}{Stage} & \multicolumn{3}{c}{\textbf{Time per Iteration (s)}} & \multicolumn{3}{c}{\textbf{Total Time to Converge (s)}} & \multicolumn{3}{c}{\textbf{GPU Usage (GB)}} \\
%     \cmidrule(lr){3-11}
%     ~ & ~ & TextGrad & M-TextGrad & REVOLVE & TextGrad & M-TextGrad & REVOLVE & TextGrad & M-TextGrad & REVOLVE\\
%     \midrule
%     \multirow{2}{*}{\textbf{Prompt Optimization}} 
%     & Objective Counting & 92.144 & 110.721 & 137.815 & 276.450 & 110.732 & 137.821 & 3.23 & 3.24 & 3.23 \\ \cmidrule(lr){2-11}
%     & GSM8K & 135.184 & 152.423 & 176.538 & 1351.85 & 1219.393 & 1235.774 & 3.23 & 3.23 & 3.23 \\
%     \midrule
%     \multirow{3}{*}{\textbf{Solution Optimization}} 
%     & Google-proof QA & 153.522 & 178.879 & 197.235 & 614.216 & 1091.162 & 453.641 & 3.24 & 3.23 & 3.24 \\ \cmidrule(lr){2-11}
%     & MMLU-Machine Learning & 172.429 & 207.819 & 223.807 & 896.631 & 685.803 & 626.659 & 3.24 & 3.24 & 3.24 \\ \cmidrule(lr){2-11}
%     & MMLU-College Physics & 188.116 & 225.631 & 245.167 & 1636.612 & 1308.662 & 1054.229 & 3.24 & 3.24 & 3.24 \\ 
%     \midrule
%     \textbf{Code Optimization} & LeetCode Hard & 1078.783 & 1241.917 & 1352.174 & 18986.655 & 18472.411 & 15820.489 & 6.46 & 6.46 & 6.46\\
%     \bottomrule
% \end{tabular}
% }
% % \vspace{-20pt}
% \end{table*}
```

## Table 9
```latex
\begin{table*}[t]
\centering
\small 
\caption{Comparison of computational resources (GPU memory and runtime) for REVOLVE and baseline methods across tasks.}
\vspace{-5pt}
\label{tab:efficiency}
\resizebox{\linewidth}{!}{
\begin{tabular}{c|c|c|c|c|c}
    \toprule
    \textbf{Task} & \textbf{Dataset} & \textbf{Method} & \textbf{Time per Iteration (s)} & \textbf{Total Time to Converge (s)} & \textbf{GPU Usage (GB)} \\
    \midrule
    \multirow{6}{*}{Prompt Optimization}
    & \multirow{3}{*}{Objective Counting} & TextGrad & 92.144 & 276.450 & 3.23  \\ 
    & & M-TextGrad & 110.721 & 110.732 & 3.24 \\
    & & REVOLVE & 137.815 & 137.821 & 3.23 \\ \cmidrule(lr){2-6}
    & \multirow{3}{*}{GSM8K} & TextGrad & 135.184 & 1351.85 & 3.23 \\
    & & M-TextGrad & 152.423 & 1219.393 & 3.23 \\
    & & REVOLVE & 176.538 & 1235.774 & 3.23 \\
    \midrule
    \multirow{9}{*}{Solution Optimization}
    & \multirow{3}{*}{Google-proof QA} & TextGrad & 153.522 & 614.216 & 3.24  \\ 
    & & M-TextGrad & 178.879 & 1091.162 & 3.23 \\
    & & REVOLVE & 197.235 & 453.461 & 3.24 \\ \cmidrule(lr){2-6}
    & \multirow{3}{*}{MMLU-Machine Learning} & TextGrad & 172.429 & 896.631 & 3.24 \\
    & & M-TextGrad & 207.819 & 685.803 & 3.24 \\
    & & REVOLVE & 223.807 & 626.659 & 3.24 \\ \cmidrule(lr){2-6}
    & \multirow{3}{*}{MMLU-College Physics} & TextGrad & 188.116 & 1636.612 & 3.24 \\
    & & M-TextGrad & 225.631 & 1308.662 & 3.24 \\
    & & REVOLVE & 245.167 & 1054.229 & 3.24 \\
    \midrule
    \multirow{3}{*}{Code Optimization}
    & \multirow{3}{*}{Objective Counting} & TextGrad & 1078.783 & 18986.655 & 6.46  \\ 
    & & M-TextGrad & 1241.917 & 18472.411 & 6.46 \\
    & & REVOLVE & 1352.174 & 15820.489 & 6.46 \\ 
    % \midrule
    % \multirow{3}{*}{\textbf{Solution Optimization}} 
    % & Google-proof QA & 153.522 & 178.879 & 197.235 & 614.216 & 1091.162 & 453.641 & 3.24 & 3.23 & 3.24 \\ \cmidrule(lr){2-11}
    % & MMLU-Machine Learning & 172.429 & 207.819 & 223.807 & 896.631 & 685.803 & 626.659 & 3.24 & 3.24 & 3.24 \\ \cmidrule(lr){2-11}
    % & MMLU-College Physics & 188.116 & 225.631 & 245.167 & 1636.612 & 1308.662 & 1054.229 & 3.24 & 3.24 & 3.24 \\ 
    % \midrule
    % \textbf{Code Optimization} & LeetCode Hard & 1078.783 & 1241.917 & 1352.174 & 18986.655 & 18472.411 & 15820.489 & 6.46 & 6.46 & 6.46\\
    \bottomrule
\end{tabular}
}
% \vspace{-20pt}
\end{table*}
```

