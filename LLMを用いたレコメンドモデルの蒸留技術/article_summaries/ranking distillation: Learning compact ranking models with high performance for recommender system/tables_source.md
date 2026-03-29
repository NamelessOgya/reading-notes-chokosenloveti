# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t!]
\center
\caption{Statistics of the data sets}\label{tb:dataset}
\vspace{-0.0cm}
\setlength{\tabcolsep}{13pt}
\begin{tabular}{lccccc}
\toprule
\multirow{2}{4em}{\textbf{Datasets}} &
 \multirow{2}{3em}{\textbf{\#users}} & \multirow{2}{3em}{\textbf{\#items}} &
 \textbf{avg. actions} &
 \textbf{$(u, \mathcal{S}^{(u,t)})$} & \multirow{2}{3em}{\textbf{Sparsity}}\\
 & & & \textbf{per user} & \textbf{pairs} &\\
\midrule
Gowalla & 13.1k & 14.0k & 40.74 & 367.6k & 99.71\%\\
\midrule
Foursquare & 10.1k & 23.4k & 30.16 & 198.9k & 99.87\%\\
\bottomrule
\end{tabular}
\end{table*}
```

