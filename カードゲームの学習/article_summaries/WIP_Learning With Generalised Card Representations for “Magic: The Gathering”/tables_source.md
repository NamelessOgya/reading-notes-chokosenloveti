# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[h]
\caption{Comparison of the different approaches. As a performance measure, we use top-1 accuracy of predicting the correct choice on a held-out test set as well as training time per epoch. We see that the unchanged InfoNCE does not perform well in this task due to numerous inaccurate comparisons in the matrix, but our proposed adaptions lead to the best overall results. \textit{Triplet loss random mining} is fastest due to less computation overhead in the similarity matrix. \textit{all mining} should be regarded with caution as we had to downsize the batch size by a factor of 10, thus strongly influencing the results. Interestingly, \textit{hardest mining} leads to worse accuracy than \textit{random mining}}
\label{tab:results}
\resizebox{\columnwidth}{!}{
\begin{tabular}{ccccc}
\toprule
Method & Top-1 Accuracy & Training time per epoch\\
\toprule
Standard InfoNCE & 54.24\% & 52:47min\\
Sigmoid InfoNCE & 68.11\% & 53:30min\\
Adapted InfoNCE & \textbf{68.80\%} & 52:45min\\
Triplet loss random mining& 67.23\% & \textbf{47:31min}\\
Triplet loss hardest mining& 66.56\% &1:07:35h\\
Triplet loss all mining& 65.98\% & 11:51:24h\\
\bottomrule
\end{tabular}}
\end{table}
```

