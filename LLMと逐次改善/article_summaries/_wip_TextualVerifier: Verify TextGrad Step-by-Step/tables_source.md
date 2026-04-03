# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[htbp]
\caption{TextualVerifier Standalone Performance}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Config} & \textbf{Accuracy} & \textbf{Proc. Time} & \textbf{LLM Calls} & \textbf{Score} \\
\hline
1 variant & +1.4 pp & 66,465 ms & 18.8 & 66.3/100 \\
\hline
2 variants & +1.4 pp & 196,098 ms & 56.4 & 63.1/100 \\
\hline
3 variants & +2.9 pp & 227,156 ms & 75.1 & 62.2/100 \\
\hline
4 variants & +5.7 pp & 253,620 ms & 93.9 & 57.9/100 \\
\hline
5 variants & +0.0 pp & 327,053 ms & 112.7 & 32.9/100 \\
\hline
\end{tabular}
\label{tab1}
\end{center}
\end{table}
```

## Table 2
```latex
\begin{table}[htbp]
\caption{TextGrad with TextualVerifier Integration Performance}
\begin{center}
\begin{tabular}{|l|c|c|c|}
\hline
\textbf{Method} & \textbf{Accuracy} & \textbf{Improvement} & \textbf{LLM Calls} \\
\hline
TextGrad-Only & 68.2\% & - & 0.0 \\
\hline
TextGrad + TV (Loss) & \textbf{70.4\%} & \textbf{+2.2 pp} & 5.9 \\
\hline
TextGrad + TV (Optimizer) & 65.0\% & -3.2 pp & 9.6 \\
\hline
TextGrad + TV (Both) & 67.2\% & -1.0 pp & 15.1 \\
\hline
\end{tabular}
\label{tab2}
\end{center}
\end{table}
```

## Table 3
```latex
\begin{table}[htbp]
\caption{TextualVerifier Version Comparison Results}
\begin{center}
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Version} & \textbf{GPQA} & \textbf{MMLU-ML} & \textbf{MMLU-CP} & \textbf{Overall} \\
\hline
TextGrad Only & 51.01\% & 76.79\% & 91.18\% & 67.96\% \\
\hline
V1 (Basic) & +5.05 pp & -2.68 pp & +3.92 pp & +2.67 pp \\
\hline
V2 (Contextual) & +5.56 pp & +7.14 pp & +2.94 pp & \textbf{+5.34 pp} \\
\hline
V3 (Consolidated) & \textbf{+8.08 pp} & \textbf{+10.71 pp} & +0.98 pp & \textbf{+5.34 pp} \\
\hline
V4 (Simplified) & +1.01 pp & +5.35 pp & -2.94 pp & +1.21 pp \\
\hline
\end{tabular}
\label{tab3}
\end{center}
\end{table}
```

