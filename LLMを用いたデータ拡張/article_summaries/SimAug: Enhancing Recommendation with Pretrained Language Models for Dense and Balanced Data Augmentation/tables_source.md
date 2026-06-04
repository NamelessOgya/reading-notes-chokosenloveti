# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]

\caption{Utility performance with LightGCN backbone. The improvement compares \textit{SimAug} to the vanilla.}
\label{tab.utility_results}
\resizebox{\textwidth}{!}{%
\begin{tabular}{l|ccc|ccc|ccc}
\toprule
\multirow{2}{*}{\textbf{Method}} &          \textbf{Recall@20}   & \textbf{NDCG@20}   &\textbf{Avg@20}   & \textbf{Recall@20}   & \textbf{NDCG@20}   &\textbf{Avg@20} & \textbf{Recall@20}   & \textbf{NDCG@20}   &\textbf{Avg@20}  \\ 
\cline{2-10}
         & \multicolumn{3}{c|}{Appliances} & \multicolumn{3}{c|}{Baby Products} & \multicolumn{3}{c}{Grocery and Gourmet Food} \\ 
       
\hline\hline  Vanilla  &  0.0692 & 0.0328 & 0.0369  & 0.0477 & 0.0230 & 0.0365 & 0.0434 & 0.0234 & 0.0348\\ 
Aug-Random     & 0.0482 & 0.0194 & 0.0249 & 0.0459 & 0.0226 & 0.0354 & 0.0357 & 0.0192 & 0.0292\\ 
Aug-Rec     & 0.0635 & 0.0338 & 0.0344 & 0.0459 & 0.0248 & 0.0354 & 0.0424 & 0.0237 & 0.0342\\ 
SimAug      &  0.0983 & 0.0424 & 0.0515 & 0.0546 & 0.0283 & 0.0419 & 0.0514 & 0.0286 & 0.0408\\ 
Improve (\%) & \textbf{+42.07\%}  & \textbf{+29.09\%}  & \textbf{+39.71\%} & \textbf{+14.55\%} &  \textbf{+22.85\%} &  \textbf{+14.78\%} &\textbf{+18.34\%} &\textbf{+22.29\%}& \textbf{+17.09\%} \\ \hline\hline

&          \multicolumn{3}{c|}{Movies and TV} & \multicolumn{3}{c|}{Office Products} & \multicolumn{3}{c}{Patio Lawn and Garden} \\
\hline   Vanilla & 0.0898 & 0.0554 & 0.0701 & 0.0485 & 0.0268 & 0.0363 & 0.0328 & 0.0172 & 0.0250\\ 
Aug-Random     &  0.0943 & 0.0607 & 0.0754 & 0.0387 & 0.0212 & 0.0294 & 0.0258 & 0.0135 & 0.0201\\ 
Aug-Rec & 0.1008 & 0.0556 & 0.0779 & 0.0487 & 0.0268 & 0.0365 & 0.0319 & 0.0169 & 0.0244\\
SimAug  &  0.1149 & 0.0675 & 0.0886 & 0.0535 & 0.0292 & 0.0399& 0.0386 & 0.0208 & 0.0294\\ 
Improve (\%) & \textbf{+27.95\%} & \textbf{+21.86\%} & \textbf{+26.40\%} & \textbf{+10.21\%} & \textbf{+8.84\%}  & \textbf{+9.94\%}  & \textbf{+17.82\%} & \textbf{+20.44\%} & \textbf{+17.54\%}\\ 

\hline \hline 

&          \multicolumn{3}{c|}{Pet Supplies} & \multicolumn{3}{c|}{Sports and Outdoors} & \multicolumn{3}{c}{Toys and Games} \\
\hline   Vanilla & 0.0559 & 0.0291 & 0.0438 & 0.0403& 0.0213 &0.0310 & 0.0438 & 0.0244 & 0.0334\\ 
Aug-Random     &   0.0490 & 0.0256 & 0.0388 & 0.0319 & 0.0169 & 0.0250 & 0.0326 & 0.0185 & 0.0255\\ 
Aug-Rec & 0.0552 & 0.0306 & 0.0435& 0.0367 & 0.0203 & 0.0284 & 0.0362 &0.0200  & 0.0280\\
SimAug  &   0.0589 & 0.0313 & 0.0461 & 0.0428 & 0.0228 & 0.033 & 0.0465 & 0.0253 & 0.0352\\ 
Improve (\%) &  \textbf{+5.37\%} & \textbf{+7.52\%} & \textbf{+5.32\%} & \textbf{+6.00\%} &  \textbf{+7.32\%} & \textbf{+6.19\%} & \textbf{+6.12\%} & \textbf{+3.67\%} & \textbf{+5.43\%}\\ \toprule
\end{tabular} 
}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]

\caption{Fairness performance with LightGCN backbone. The improvement compares \textit{SimAug} to the vanilla.}
\label{tab.fairness_results}
\resizebox{\textwidth}{!}{%
\begin{tabular}{l|ccc|ccc|ccc}
\toprule
\multirow{2}{*}{\textbf{Method}} &          \textbf{Pop@20}   & \textbf{Unpop@20}   &\textbf{Fairness}   & \textbf{Pop@20}   & \textbf{Unpop@20}   &\textbf{Fairness} & \textbf{Pop@20}   & \textbf{Unpop@20}   &\textbf{Fairness} \\ 
\cline{2-10}
         & \multicolumn{3}{c|}{Appliances} & \multicolumn{3}{c|}{Baby Products} & \multicolumn{3}{c}{Grocery and Gourmet Food} \\ 
       
\hline\hline  Vanilla  &  0.0510 & 0.0011 & 2.0638 & 0.0314 & 0.0001 & 0.1794  & 0.0269 & 0.0007 & 2.5431\\ 
Aug-Rec     & 0.0479 &0.0001 &0.2211& 0.0301 &0.0000 &0.013 &0.0263& 0.0004 &1.3366 \\ 
SimAug      & 0.0626& 0.0215 &34.3659 & 0.0357 &0.0021 &5.742 &0.0306 &0.0031& 10.2771\\ 
Improve (\%) & \textbf{+22.69\%} & \textbf{+1942.96\%} &\textbf{+1565.18\%} &\textbf{+13.96\%}&\textbf{+3547.44\%} &\textbf{+3100.60\%} &\textbf{+14.03\%} &\textbf{+360.79\%} &\textbf{+304.11\%}\\ \hline\hline

&          \multicolumn{3}{c|}{Movies and TV} & \multicolumn{3}{c|}{Office Products} & \multicolumn{3}{c}{Patio Lawn and Garden} \\
\hline   Vanilla & 0.0496 & 0.0078& 15.7805 &0.0313& 0.0015 &4.6585 &0.0214 &0.0004 &2.0732\\ 
Aug-Rec & 0.0549 &0.0061 &11.1712 &0.0314& 0.0010& 3.0524 &0.0208& 0.0001 &0.6651\\
SimAug  & 0.0600& 0.0190 &31.6080 &0.0332 &0.0049 &14.8501& 0.0248& 0.0015 &6.115\\ 
Improve (\%) & \textbf{+20.96\%} &\textbf{+142.28\%} &\textbf{+100.30\%} &
 \textbf{+6.15\%} &\textbf{+238.39\%}& \textbf{+218.77\%}& \textbf{+16.09\%}& \textbf{+242.41\%} &\textbf{+194.96\%} \\ 

\hline \hline 

&          \multicolumn{3}{c|}{Pet Supplies} & \multicolumn{3}{c|}{Sports and Outdoors} & \multicolumn{3}{c}{Toys and Games} \\
\hline   Vanilla & 0.0359 & 0.0005& 1.4791 &0.0266 &0.0004 &1.6130& 0.0276 &0.0023 &8.2593\\ 
Aug-Rec &0.0353 &0.0004& 1.0966 &0.0242 &0.0001& 0.5937& 0.0229 &0.0005 &2.2025\\
SimAug  &  0.0378 &0.0009 &2.4665 &0.0278 &0.0015 &5.4730 &0.0267 &0.0088 &32.9507\\ 
Improve (\%) &  \textbf{+5.26\%} &\textbf{+75.53\%}& \textbf{+66.76\%} &\textbf{+4.52\%} &\textbf{+254.64\%} &\textbf{+239.30\%}& -3.31\% &\textbf{+285.74\%}& \textbf{+298.95\%} \\ \toprule
\end{tabular} 
}
\end{table*}
```

## Table 3
```latex
\begin{table*}[]
\centering
\small
\caption{Impact of different LLMs on Baby and Office Products.}
\label{tab:plms}
\begin{tabular}{l|c|ccc|ccc}
\toprule
&     \multirow{2}{*}{Model Size}  &    \textbf{Recall@20}   & \textbf{NDCG@20}   &\textbf{Avg@20}   & \textbf{Recall@20}   & \textbf{NDCG@20}   &\textbf{Avg@20} \\ 
\cline{3-8}
    &      & \multicolumn{3}{c|}{Baby Products} & \multicolumn{3}{c}{Office Products} \\ 
       
\hline 
Vanilla& - & 0.0477& 0.0230 &0.0365 &0.0485 &0.0268 &0.0363 \\
\hline
SBert-L6& 80MB & 0.0546 &0.0283& 0.0419 & 0.0535 & 0.0292& 0.0399\\
SBert-L12 &120MB &0.0538 &0.0277 &0.0413 & 0.0538& 0.0291 &0.0401\\
SBert-Mpnet &420MB &0.0534 &0.0274 &0.0410 & 0.0530 & 0.0289 &0.0396 \\
\hline
gte-small & 0.07GB & 0.0546 & 0.0280 &  0.0419 & 0.0553 &0.0304& 0.0411 \\
gte-base & 0.22GB & 0.0551 & 0.0284 & 0.0422 & 0.0554 & 0.0306 & 0.0413\\
gte-large & 0.67GB & 0.0546 & 0.0281 & 0.0419 & 0.0556 & 0.0306 & 0.0413 \\
\hline

Llama2-13b & 26GB &0.0519 &0.0265 &0.0399 & 0.0469 &0.0250 & 0.0352\\ 
\toprule

\end{tabular}
\end{table*}
```

## Table 4
```latex
\begin{table}[h]
\small
\caption{Dataset Statistics}
    \centering
    \resizebox{0.5\textwidth}{!}{%
    \begin{tabular}{l|c|c|c}
\toprule
        \textbf{Dataset} & \# \textbf{User} & \# \textbf{Item} & \# \textbf{Interaction} \\
        \hline
        Appliances & 18,830 & 6,542 &65,694\\
        Baby Products & 88,126  & 24,737 & 703,964\\
        Grocery and Gourmet Food &257,363 & 95,555 & 2,437,551\\
        Movies and TV & 106,074 & 54,679&1,233,612\\
        Office Products & 137,461 & 55,075&1,106,657\\
        Patio Lawn and Garden & 238,042 & 89,710& 1,921,639\\
        Pet Supplies & 365,763 & 80,194&3,101,564\\
        Sports and Outdoors & 215,038 & 91,719&1,780,007\\
        Toys and Games & 268,929 & 117,230 &2,375,168\\
      \toprule
    \end{tabular}
    }
    \label{tab.data}
\end{table}
```

## Table 5
```latex
\begin{table}[h]
    \centering
    \caption{Average degrees}
    \resizebox{0.5\textwidth}{!}{%
    \begin{tabular}{c|c|c|c}
    \toprule
        Dataset & Pop & Unpop & Pop/Unpop\\
        \hline
        Appliances & 8.22 & 1.62 & 5.07 \\
        Baby Products & 39.63 & 4.76 & 8.32 \\
        Grocery and Gourmet Food & 31.55 & 4.59 & 6.87 \\
        Movies and TV & 24.33 & 4.50 & 5.41 \\
        Office Products & 21.25 & 3.97 & 5.35 \\
        Patio Lawn and Garden & 23.59 & 4.10 & 5.75 \\
        Pet Supplies & 66.22 & 5.93 & 11.17 \\
        Sports and Outdoors & 20.35 & 3.86 & 5.27 \\
        Toys and Games & 20.99 & 4.08 & 5.15 \\
      \toprule
    \end{tabular}
    }
    \label{tab:degree}
\end{table}
```

