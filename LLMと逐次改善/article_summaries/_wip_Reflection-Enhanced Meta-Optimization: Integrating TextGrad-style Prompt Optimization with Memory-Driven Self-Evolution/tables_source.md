# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[ht]
\centering
\caption{Comparison on GSM8K}
\label{tab:main_results}
\begin{tabular}{l|c|c|c|c}
\hline
\textbf{Method} & \textbf{Epochs} & \textbf{Train Size} & \textbf{Val Acc (\%)} & \textbf{Test Acc (\%)} \\
\hline
TextGrad (100 samples) & 3 & 1000 & 96.0 & 69.0 \\
RAG+Optimizer (100 samples) & 3 & 1000 & 89.0 & 94.0 \\
\hline
TextGrad (full data) & 3 & 6973 & 91.0 & 62.0 \\
TextGrad (full data) & 5 & 6973 & 90.0 & 63.0 \\
Reflection RAG (full) & 3 & 6973 & 90.3 & 89.0 \\
Reflection RAG (full) & 5 & 6973 & 90.0 & 89.8 \\
Adaptive Optimizer (full) & 3 & 6973 & 90.1 & 90.0 \\
Adaptive Optimizer (full) & 5 & 6973 & 90.3 & 93.2 \\
RAG+Optimizer (full) & 3 & 6973 & 90.1 & 90.1 \\
RAG+Optimizer (full) & 5 & 6973 & 90.3 & 90.5 \\
\hline
\end{tabular}
\end{table}
```

