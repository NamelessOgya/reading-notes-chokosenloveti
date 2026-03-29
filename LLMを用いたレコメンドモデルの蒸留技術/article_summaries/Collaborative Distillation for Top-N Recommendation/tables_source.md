# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t!]
\begin{center}
\caption{Statistics of four benchmark datasets.}\label{tab:statistics}
%\begin{tabular}{p{1.0cm}p{1.2cm}p{1.2cm}p{2.0cm}p{1.2cm}p{4cm}p{4cm}}
\begin{tabular}{llllccc}
\toprule
Dataset & \# of users & \# of items & \# of interactions & Sparsity & min/max/avg. interactions per user & min/max/avg. interactions per item \\
\hline
AMusic & 2,831 & 13,410 & 63,054 & 99.83\% & 10/714/22.27 & 1/155/4.70 \\
ML100K & 943 & 1,682 & 100,000 & 93.70\% & 20/737/106.04 & 1/583/59.45 \\
Yelp & 9,788 & 25,373 & 489,820 & 99.80\% & 20/1024/50.04 & 1/674/19.30 \\
Gowalla & 13,149 & 14,009 & 535,650 & 99.71\% & 15/764/40.73 & 15/1743/38.24 \\
\bottomrule
\end{tabular}
\end{center}
\vskip -0.2in
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
%\begin{center}
%\caption{Hyperparameters of our model.}\label{tab:statistics}
%\begin{tabular}{p{1.5cm}p{10cm}p{5cm}}
%\toprule
%Notation & Definition & Value \\
%\hline
%$\lambda$ & Balance the collaborative filtering loss and knowledge distillation loss in collaborative distillation & [0, 0.2, 0.4, 0.6, 0.8, 1] (default = 1) \\
%T1 & Control the scale of real-valued logit(zui) in logistic function & [0.5, 1, 2, 4] (default = 1) \\
%T2 & Control the scale of real-valued logit(zui) in logistic function & [1, 2, 4, 6, 8] (default = 1) \\
%$\delta$ &Sampling ratio of user's missing interactions for knowledge distillation & [0, 0.2, 0.4, 0.6, 0.8, 1] (default = 0.2) \\
%$\eta$ & The number of negative sampling at Caser model & [1, 3, 5, 7, 9] (default = 3) %\\
%\bottomrule
%\end{tabular}
%\end{center}
%\end{table*}
```

## Table 3
```latex
\begin{table*}[t]
\caption{Performance comparison of each model in four benchmark datasets.}\label{tab:com1}
\begin{center}
\begin{tabular}{p{1cm}p{1.1cm}p{1.1cm}p{1.5cm}p{1.1cm}p{1.5cm}p{1.1cm}p{1.5cm}p{1.1cm}p{1.5cm}}
\toprule
\multicolumn{2}{c}{Models} & \multicolumn{2}{c}{AMusic} & \multicolumn{2}{c}{ML100K} & \multicolumn{2}{c}{Yelp} & \multicolumn{2}{c}{Gowalla}\\
 &  & HR@50 & NDCG@50 & HR@50 & NDCG@50 & HR@50 & NDCG@50 & HR@50 & NDCG@50  \\
\hline
\multirow{7}{*}{CDAE}
& Teacher & 0.1727 & 0.0547 & 0.3917 & 0.1288 &0.1150 & 0.0340 & 0.3057 & 0.1269 \\
& Student & 0.1217 & 0.0370 & 0.3565 & 0.1107 &0.0956 & 0.0278 & 0.2632 & 0.1088 \\
& RD & 0.1275 & 0.0402 & 0.3578 & 0.1112 & 0.0949 & 0.0272 & 0.2638 & 0.1092 \\
& RD-Rank & 0.1238 & 0.0366 & 0.3580 & 0.1110 & 0.0915 & 0.0258 & 0.2602 & 0.1034 \\
& CD-Base & 0.1613 & 0.0498 & 0.3707 & 0.1124 & 0.1042 & 0.0304 & 0.2613 & 0.1093 \\
& CD-TG & \text{0.1653} & \text{0.0513} & \textbf{0.3805} & \text{0.1175} &\text{0.1060} & \text{0.0309} & \text{0.2682} & \text{0.1113} \\
& CD-SG & \textbf{0.1681} & \textbf{0.0519} & \text{0.3741} & \textbf{0.1182} & \textbf{0.1067} & \textbf{0.0313} & \textbf{0.2710} & \textbf{0.1122}\\
\cline{2-10}
& Gain (\%) & 31.8 & 29.1 & 6.3 & 6.3 & 12.4 & 15.1 & 2.7 & 2.7\\
\hline
\multirow{7}{*}{Caser}
& Teacher & 0.1366 & 0.0392 & 0.3145 & 0.0868 & 0.0947 & 0.0266 & 0.3005 & 0.1109 \\
& Student & 0.0919 & 0.0276 & 0.2717 & 0.0730 & 0.0789 & 0.0220 & 0.2033 & 0.0768 \\
& RD & 0.0936 & 0.0276 & 0.2732 & 0.0758 & 0.0814 & 0.0230 & 0.2358 & 0.0877 \\
& RD-Rank & 0.0909 & 0.0271 & 0.2787 & 0.0774 & 0.0813 & 0.0232 & 0.2362 & 0.0880\\
& CD-Base & 0.1211 & \textbf{0.0355} & 0.3147 & 0.0872 & 0.0874 & 0.0244 & 0.2557 & \textbf{0.0943} \\
& CD-TG & 0.1135 & 0.0336 & \textbf{0.3203} & \text{0.0879} & 0.0899 & 0.0249 & \text{0.2525} & \text{0.0904} \\
& CD-SG & \textbf{0.1247} & \text{0.0351} & 0.3196 & \textbf{0.0891} & \textbf{0.0965} & \textbf{0.0269} & \textbf{0.2570} & 0.0925 \\
\cline{2-10}
& Gain (\%) & 33.2 & 28.6 & 17.2 & 17.5 & 18.6 & 17.0 & 9.0 & 7.5\\
\hline
\bottomrule
\end{tabular}
\end{center}
\vskip -0.2in
\end{table*}
```

