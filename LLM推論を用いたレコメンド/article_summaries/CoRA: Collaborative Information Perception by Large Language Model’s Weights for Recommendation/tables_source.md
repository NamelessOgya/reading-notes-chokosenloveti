# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[ht]
    \centering
    \begin{adjustbox}{max width=\textwidth}
    \begin{tabular}{cc|cccccc}
        \toprule
        \multicolumn{2}{c|}{\textbf{Dataset}} & \multicolumn{3}{c}{Amazon-Book} & \multicolumn{3}{c}{ML-1M} \\
        \cmidrule(lr){1-2} \cmidrule(lr){3-5} \cmidrule(lr){6-8}
        \multicolumn{2}{c|}{\textbf{Method}} & AUC & UAUC & Improve & AUC & UAUC & Improve \\
        \midrule
        \multirow{3}{*}{\textbf{Collab.}} 
        & MF & 0.7105 & 0.5543 & 14.04\% & 0.6486 & 0.6396 & 10.56\% \\
        & LightGCN & 0.7026 & 0.5619 & 13.93\% & 0.5858 & 0.6512 & 15.68\% \\
        & SASRec & 0.6675 & 0.5614 & 17.04\% & 0.7005 & 0.6734 & 3.65\% \\
        \midrule
        \multirow{3}{*}{\textbf{LLMRec}} 
        & ICL & 0.5180 & 0.5043 & 51.61\% & 0.5119 & 0.5178 & 38.37\% \\
        & Prompt4NR & 0.6527 & 0.5011 & 25.10\% & 0.7027 & 0.6713 & 3.28\% \\
        & TALLRec & 0.6583 & 0.4971 & 25.11\% & 0.7044 & 0.6741 & 3.31\% \\
        \midrule
        \multirow{5}{*}{\textbf{\makecell{LLMRec\\ w/ Collab.}}} 
        & PersonPrompt & 0.7113 & 0.5596 & 13.44\% & 0.7014 & 0.6503 & 5.40\% \\
        & CoLLM-MF & 0.8021 & 0.5782 & 5.14\% & 0.7028 & 0.6714 & 3.64\% \\
        & CoLLM-LGCN & 0.7835 & 0.5663 & 7.48\% & 0.7164 & 0.6842 & 4.68\% \\
        & CoLLM-SAS & 0.7538 & 0.5874 & 7.55\% & 0.7059 & 0.6531 & 4.84\% \\
        & BinLLM & 0.8157 & 0.5724 & 4.83\% & 0.7132 & 0.6815 & 2.11\% \\
        \midrule
        \multirow{3}{*}{\textbf{Ours}} 
        & CoRA-MF & \textbf{0.8179} & \textbf{0.6262} & - & \textbf{0.7361} & \textbf{0.6884} & - \\
        & CoRA-LGCN & 0.7886 & 0.5689 & - & 0.7128 & 0.6966 & -  \\
        & CoRA-SAS & 0.7677 & 0.5961 & - & 0.7019 & 0.6517 & - \\
        \bottomrule
    \end{tabular}
    \end{adjustbox}
    \caption{Performance comparison of various models on Amazon-Book and ML-1M. "Collab." denotes collaborative recommendation methods. "Improve" denotes the relative improvement of CoRA compared to baselines, averaged over the two metrics. All improvements are statistically significant, as determined by a paired t-test with $p \leq 0.05$.}
    \label{tab:overall}
\end{table*}
```

