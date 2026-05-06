# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[width=.9\linewidth,cols=5,pos=h]
\caption{\fontfamily{ptm}\selectfont Detail of datasets. Av. n means the average length of sequences.}
\label{tab1}
\begin{tabular*}{\tblwidth}{@{} lcccc @{} } 
\toprule
Dataset & Users & Items & Av. n & Density \\ 
\midrule
Office & 77,284 & 27,467 & 4.34491 & 1.5819$\times 10^{-4}$ \\ 
Music & 19,513 & 10,445 & 4.52729 & 4.3344$\times 10^{-4}$ \\ 
ML-1M & 6,040 & 3,703 & 44.66805 & 1.2063$\times 10^{-2}$ \\ 
\bottomrule
\end{tabular*}
\end{table}
```

## Table 2
```latex
\begin{table*}[!t]
\captionsetup{width=0.735\linewidth}
\caption{\fontfamily{ptm}\selectfont Experiment results of our model using $L_{general}$ ,$L_{seq}$ and $L_{pop}$. W/O represent models with and without the use of the UniT framework. Bold indicates the performance of sampling strategies surpasses that of the original model.}
\label{tab3}
\centering
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lcccccccccc@{}}
\toprule
\multirow{2}{*}{Dataset}& & \multicolumn{2}{c}{\textbf{SASRec}} & \multicolumn{2}{c}{\textbf{BERT4Rec}} & \multicolumn{2}{c}{\textbf{UnisRec}} & \multicolumn{2}{c}{\textbf{LinRec}} \\
\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
 &  & HR & NDCG & HR & NDCG & HR & NDCG & HR & NDCG \\
\midrule
\multirow{4}{*}{Office} & W/O & 0.03191 & 0.01289 & 0.03444 & 0.01442 & 0.03192 & 0.01296 & 0.02613 & 0.01044 \\
& $L_{general}$ & \textbf{0.03198} & \textbf{0.01323} & \textbf{0.03540} & \textbf{0.01485} & \textbf{0.03196} & \textbf{0.01306} & \textbf{0.02689} & \textbf{0.01090} \\
& $L_{seq}$ & \textbf{0.03447} & \textbf{0.01418} & \textbf{0.03901} & \textbf{0.01646} & \textbf{0.03592} & \textbf{0.01489} & \textbf{0.02664} & \textbf{0.01061} \\
& $L_{pop}$ & \textbf{0.03229} & \textbf{0.01319} & \textbf{0.03588} & \textbf{0.01510} & \textbf{0.03253} & \textbf{0.01340} & \textbf{0.02625} & 0.01043 \\
\midrule
\multirow{4}{*}{Music} & W/O & 0.05275 & 0.02177 & 0.05345 & 0.02180 & 0.05331 & 0.02215 & 0.04881 & 0.01954 \\
& $L_{general}$ & \textbf{0.05298} & \textbf{0.02201} & 0.05345 & \textbf{0.02205} & \textbf{0.05366} & \textbf{0.02222} & \textbf{0.04907} & \textbf{0.02052} \\
& $L_{seq}$ & \textbf{0.05343} & \textbf{0.0218} & \textbf{0.05427} & \textbf{0.02239} & \textbf{0.05411} & \textbf{0.02229} & \textbf{0.05035} & \textbf{0.02053} \\
& $L_{pop}$ & \textbf{0.05406} & \textbf{0.02203} & \textbf{0.05384} & \textbf{0.02195} & \textbf{0.05332} & \textbf{0.02229} & \textbf{0.04933} & \textbf{0.02054} \\
\midrule
\multirow{4}{*}{Movie} & W/O & 0.16545 & 0.06252 & 0.07103 & 0.02562 & 0.16910 & 0.06429 & 0.11010 & 0.04145 \\
& $L_{general}$ & \textbf{0.17301} & \textbf{0.06498} & \textbf{0.07600} & \textbf{0.02750} & 0.16333 & 0.06180 & \textbf{0.11308} & \textbf{0.04227} \\
& $L_{seq}$ & \textbf{0.17075} & \textbf{0.06486} & \textbf{0.07658} & \textbf{0.02719} & \textbf{0.17517} & \textbf{0.06595} & \textbf{0.11292} & \textbf{0.04375} \\
& $L_{pop}$ & \textbf{0.17086} & \textbf{0.06412} & \textbf{0.07889} & \textbf{0.02867} & \textbf{0.17114} & \textbf{0.06467} & \textbf{0.11267} & \textbf{0.04237} \\
\bottomrule
\end{tabular*}
\end{table*}
```

