# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\centering
\caption{Offline evaluation on past marketplace search logs with full-dimension embeddings. The fine-tuned model improves all metrics over the strongest baseline.}
\label{tab:full-d}
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{0.95}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{lrrrrr}
\toprule
\textbf{Model} & \textbf{\# dim} & \textbf{nDCG@k} & \textbf{nDCG@k (long)} & \textbf{Prec@k} & \textbf{Recall@k} \\
\midrule
Base            & 768 & 0.198 & 0.234 & 0.015 & 0.613 \\
\textbf{Fine-tuned} & \textbf{768} & \textbf{0.213} & \textbf{0.245} & \textbf{0.016} & \textbf{0.666} \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}
```

## Table 2
```latex
\begin{table}[t]
\centering
\caption{Offline evaluation on the same logs with 32-dimensional embeddings. At \(k=100\), Matryoshka truncation plus domain fine-tuning yields \(\approx 2\times\) nDCG@k versus production PCA and the best overall results.}
\label{tab:trunc-32d}
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{0.95}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{lrrrrr}
\toprule
\textbf{Model} & \textbf{\# dim} & \textbf{nDCG@k} & \textbf{nDCG@k (long)} & \textbf{Prec@k} & \textbf{Recall@k} \\
\midrule
Base            & 32 (PCA)   & 0.099 & 0.142 & 0.007 & 0.272 \\
\textbf{Fine-tuned} & \textbf{32 (MRL)} & \textbf{0.195} & \textbf{0.235} & \textbf{0.015} & \textbf{0.607} \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}
```

## Table 3
```latex
\begin{table}[t]
\centering
\caption{JGLUE Japanese STS (validation). Pearson $r$ and Spearman $\rho$ for base vs.\ fine-tuned models at 768d/256d/32d.}
\label{tab:jsts}
\footnotesize
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{0.95}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{lrr}
\toprule
\textbf{Model (dims)} & \textbf{Pearson $r$} & \textbf{Spearman $\rho$} \\
\midrule
\textbf{Base (768d)}  & \textbf{0.8648} & \textbf{0.8188} \\
\emph{FT (768d)}      & \emph{0.8393}   & \emph{0.7858}   \\
FT (256d)             & 0.8360          & 0.7840          \\
FT (32d)              & 0.7934          & 0.7586          \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
\centering
\caption{Online A/B test results comparing Control (base embedding model) and Treatment (fine-tuned embedding model). Treatment shows statistically significant improvements in revenue per user and search engagement efficiency.}
\label{tab:abtest}
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{0.95}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{l r}
\toprule
\textbf{Metric} & \textbf{Lift (Treatment / Control)} \\
\midrule
Average Transaction per User (ATPU) & Non stat-sig \\
Average Revenue per User (ARPU) & +0.92\% ($p<0.05$) \\
Average Order Price (AoV) & +0.91\% ($p<0.05$) \\
Item Tap Rank & $-0.65\%$ ($p<0.05$) \\
Average Impression via Search & $-0.64\%$ ($p<0.05$) \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}
```

## Table 5
```latex
\begin{table}[t]
\centering
\caption{Hybrid retrieval online experiment. Reported lifts are for the best-match (BM) search module, the SERP component that directly uses the hybrid retrieval logic. Low-hit SERP metrics are reported for the treatment group only.}
\label{tab:hybrid_abtest}
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{0.95}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{l r}
\toprule
\textbf{Metric (BM)} & \textbf{Lift (Treatment / Control)} \\
\midrule
Daily BCR & +0.88\% \\
Daily ATPU & +0.96\% \\
Daily impression count & +2.25\% \\
Daily UIV & +1.48\% \\
\midrule
\multicolumn{2}{l}{\textit{Low-hit SERP metrics}} \\
Zero-hit recovery rate & 60.2\% \\
Low-hit recovery rate & 66.1\% \\
UIV on low-hit SERPs & +12.0\% \\
BCR on low-hit SERPs & +6.95\% \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}
```

