# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\centering
\begin{tabular}{lcccccccc}
\toprule
\textbf{Method} & \multicolumn{4}{c}{\textbf{Qwen3-8B}} & \multicolumn{4}{c}{\textbf{GPT-4.1 Mini}} \\
\cmidrule(lr){2-5} \cmidrule(lr){6-9}
& \textbf{HpQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} & \textbf{HpQA} & \textbf{IFBench} & \textbf{Hover} & \textbf{PUPA} \\
\midrule
DSPy Default~\citep{khattab2024dspy} & 42.33 & 36.90 & 35.33 & 80.82 & 38.00 & 47.79 & 46.33 & 78.57 \\
MIPROv2~\citep{opsahl2024optimizing} & 55.33 & 36.22 & 47.33 & 81.55 & 58.00 & 49.15 & 48.33 & 83.37 \\
GRPO~\citep{shao2024deepseekmath} & 43.33 & 35.88 & 38.67 & 86.66 & --- & --- & --- & --- \\
GEPA~\citep{agrawal2025gepa} & \bf 62.33 & 38.61 & 52.33 & \bf 91.85 & \bf 69.00 & 52.72 & 51.67 & \bf 94.47 \\
\midrule
Feedback Descent (ours) & 60.00 & \bf 38.78 & \bf 60.00 & 90.90 & 68.33 & \bf 54.59 & \bf 57.67 & 85.66 \\
\bottomrule
\end{tabular}
\caption{
\label{tab:prompt_optimization}
Prompt optimization results across multiple benchmarks. Feedback Descent consistently outperforms or is competitive with state-of-the-art methods.}
\end{table}
```

## Table 2
```latex
\begin{table}[t]
\centering
\begin{tabular}{ll S[table-format=2.3] S[table-format=1.3] S[table-format=1.3] S[table-format=2.3] S[table-format=1.3] S[table-format=1.3] | S[table-format=1.3]}
\toprule
& \textbf{Method} & {ADRB1} & {PGR} & {PPARA} & {PPARG} & {CDK2} & {F2} & {Avg} \\
\midrule
\multirow{6}{*}{\rotatebox[origin=c]{90}{\shortstack{DOCKSTRING \\ (N=260155)}}}
& Top $50\%$ & 5.305 & 3.478 & 4.549 & 4.210 & 4.385 & 4.168 & 4.349 \\
& Top $90\%$ & 8.785 & 7.878 & 7.987 & 7.658 & 7.733 & 7.477 & 7.920 \\
& Top $99\%$ & 9.620 & 8.703 & 8.718 & 8.449 & 8.453 & 8.139 & 8.680 \\
& Top $99.9\%$ & 10.209 & 9.260 & 9.230 & 9.012 & 8.979 & 8.722 & 9.235 \\
& Top $99.99\%$ & {\blueul{10.742}} & {\blueul{9.723}} & 9.821 & 9.518 & 9.509 & 9.252 & 9.761 \\
& Best Molecule & {\blueul{11.330}} & {\blueul{9.742}} & 9.907 & 9.529 & 9.534 & {\blueul{9.311}} & 9.892 \\
\midrule
& Graph MCTS$^\dagger$~\citep{jensen2019graph} & 8.883 & 7.819 & 7.363 & 7.134 & 7.777 & 6.310 & 7.548 \\
& SMILES GA~\citep{brown2019guacamol} & 9.334 & 8.335 & 9.052 & 8.560 & 8.268 & 7.984 & 8.589 \\
& REINVENT~\citep{olivecrona2017molecular} & 9.867 & 8.604 & 8.735 & 9.054 & 8.695 & 8.441 & 8.899 \\
& Graph GA$^\dagger$~\citep{jensen2019graph} & 10.249 & 8.793 & 9.211 & 8.769 & 8.652 & 8.900 & 9.096 \\
& GP-BO$^\dagger$~\citep{tripp2021a} & 10.552 & 9.307 & 9.680 & 9.485 & 9.067 & 8.686 & 9.463 \\
\midrule
& TextGrad~\citep{yuksekgonul2024textgrad} & 8.531 & 8.057 & 7.953 & 7.256 & 8.174 & 7.357 & 7.888 \\
& Feedback Descent (ours) & \bfseries 10.623 & \bfseries 9.615 & \bfseries 9.919 & \bfseries 10.187 & \bfseries 9.803 & \bfseries 9.300 & \bfseries 9.908 \\
& \hspace{2mm} w/ No Feedback & 6.190 & 8.619 & 8.230 & 8.633 & 8.300 & 8.793 & 8.127 \\
& \hspace{2mm} w/ Random Feedback & 6.604 & 8.385 & 8.276 & 6.780 & 8.793 & 7.993 & 7.805 \\
& \hspace{2mm} w/ Binary Only & 5.863 & 8.779 & 8.507 & 7.998 & 9.439 & 8.420 & 8.168 \\
\bottomrule
\end{tabular}
\vspace{-2mm}
\captionof{table}{
\label{tab:dockstring}
Results for molecule optimization on six protein targets. Full results with standard deviations are in~\cref{tab:dockstring_full}.
For each target, the top generative result is in \textbf{bold}, and any population in the DOCKSTRING database that exceeds the best generative result is {\blueul{underlined}}.
\textbf{Feedback Descent rivals or surpasses specialized molecular optimizers across all six targets.}
}
\vspace{-2mm}
\end{table}
```

