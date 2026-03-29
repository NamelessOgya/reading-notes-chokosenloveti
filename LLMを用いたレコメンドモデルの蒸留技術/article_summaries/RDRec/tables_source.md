# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
\centering
\resizebox{\linewidth}{!}{ % \columnwidth % \paperwidth
  \begin{tabular}{cccccc}
\hline
    {Dataset} &{\#User} &{\#Item} &{\#Review}& {Avg.}& Density (\%)\\
\hline
    {Sports} &48,993& 34,298& 296,337& 8.3 & 0.0453 \\
    {Beauty} & 22,363& 12,101& 198,502& 8.9 & 0.0734 \\
    {Toys} &19,804& 22,086&  167,597& 8.6 & 0.0724 \\
\hline
\end{tabular}
}
  \caption{\label{tab:statistics}Statistics of dataset. ``\#User'', ``\#Item'', ``\#Review'', and ``Avg.'' denote the number of users, items, reviews, and average user reviews, respectively.}
\end{table}
```

## Table 2
```latex
\begin{table*}
\centering
\resizebox{.86\linewidth}{!}{ % \columnwidth % \paperwidth
\begin{tabular}{c|cccc|cccc|cccc}
\hline
\multirow {2}{*}{Models} & \multicolumn{4}{c|}{Sports} & \multicolumn{4}{c|}{Beauty} & \multicolumn{4}{c}{Toys}\\
& H@5 &N@5 & H@10 & N@10 & H@5 &N@5 & H@10 & N@10 & H@5 &N@5 & H@10 & N@10\\
\hline
Caser & 0.0116 & 0.0072 & 0.0194 & 0.0097 & 0.0205 & 0.0131 & 0.0347 & 0.0176 & 0.0166 & 0.0107 & 0.0270 & 0.0141\\
HGN & 0.0189 & 0.0120 & 0.0313 & 0.0159 & 0.0325 & 0.0206 & 0.0512 & 0.0266 & 0.0321 & 0.0221 & 0.0497 & 0.0277\\
GRU4Rec & 0.0129 & 0.0086 & 0.0204 & 0.0110 & 0.0164 & 0.0099 & 0.0283 & 0.0137 & 0.0097 & 0.0059 & 0.0176 & 0.0084\\
BERT4Rec & 0.0115 & 0.0075 & 0.0191 & 0.0099 & 0.0203 & 0.0124 & 0.0347 & 0.0170 & 0.0116 & 0.0071 & 0.0203 & 0.0099\\
FDSA & 0.0182 & 0.0122 & 0.0288 & 0.0156 & 0.0267 & 0.0163 & 0.0407 & 0.0208 & 0.0228 & 0.0140 & 0.0381 & 0.0189\\
SASRec & 0.0233 & 0.0154 & 0.0350 & 0.0192 & 0.0387 & 0.0249 & 0.0605 & 0.0318 & 0.0463 & 0.0306 & 0.0675 & 0.0374\\
S$^3$-Rec & 0.0251 & 0.0161 & 0.0385 & 0.0204 & 0.0387 & 0.0244 & 0.0647 & 0.0327 & 0.0443 & 0.0294 & 0.0700 & 0.0376\\
% LightLM & - & - & - & - & 0.0431 & 0.0353 & 0.0581 & 0.0392 & 0.0475 & 0.0330 & 0.0619 & 0.0376\\
% SP5 & 0.0223 & 0.0139 & 0.0289 & 0.0161 & 0.0457 & 0.0336 & 0.0622 & 0.0389 & 0.0218 & 0.0143 & 0.0360 & 0.0191\\
P5 & 0.0387 & 0.0312 & 0.0460 & 0.0336 & 0.0508 & 0.0379 & 0.0664 & 0.0429 & 0.0648 & 0.0567 & 0.0709 & 0.0587\\
RSL & 0.0392 & 0.0330 & 0.0512 & 0.0375 & 0.0508 & 0.0381 & 0.0667 & 0.0446 & 0.0676 & 0.0583 & 0.0712 & 0.0596\\
POD & \ul{0.0497} & \ul{0.0399} & \ul{0.0579} & \ul{0.0422} & \ul{0.0559} & \ul{0.0420} & \ul{0.0696} & \ul{0.0471} & \ul{0.0692} & \ul{0.0589} & \ul{0.0749} & \ul{0.0601} \\
\textbf{Ours} & \textbf{0.0505} & \textbf{0.0408} & \textbf{0.0596} & \textbf{0.0433} & \textbf{0.0601} & \textbf{0.0461} & \textbf{0.0743} & \textbf{0.0504} & \textbf{0.0723} & \textbf{0.0593} & \textbf{0.0802} & \textbf{0.0605} \\
\hline
Impv (\%). & \textbf{1.6} & \textbf{2.2} & \textbf{2.8} & \textbf{2.5} & \textbf{7.5}* & \textbf{9.8}* & \textbf{6.7}* & \textbf{7.1}* & \textbf{4.4}* & \textbf{0.6} & \textbf{7.1}* & \textbf{0.7} \\
p-value & 6.3e-1 & 5.1e-1 & 2.7e-1 & 3.8e-1 & 8.1e-3 & 2.4e-3 & 2.1e-2 & 2.5e-2 & 1.0e-2 & 5.8e-1 & 1.7e-5 & 5.9e-1\\
\hline
\end{tabular}
}
\caption{\label{tab:sequential_recommendation} Performance comparison on sequential recommendation. \textbf{Bold}: Best, \ul{underline}: Second best. ``*'' indicates that the improvement is statistically significant (p-value < 0.05) in the 10-trial T-test. All of the baselines are reported by the papers \cite{geng2022recommendation, chu2023leveraging, li2023prompt}, except for the POD model.}
 % 
\end{table*}
```

## Table 3
```latex
\begin{table*}
\centering
\resizebox{1\linewidth}{!}{ % \columnwidth % \paperwidth
\begin{tabular}{c|ccccc|ccccc|ccccc}
\hline
\multirow {2}{*}{Models} & \multicolumn{5}{|c|}{Sports} & \multicolumn{5}{c|}{Beauty} & \multicolumn{5}{c}{Toys}\\
& H@1& H@5 &N@5 & H@10 & N@10 & H@1 & H@5 &N@5 & H@10 & N@10 & H@1 & H@5 &N@5 & H@10 & N@10\\
\hline
MF & 0.0314 & 0.1404 & 0.0848 & 0.2563 & 0.1220 & 0.0311 & 0.1426 & 0.0857 & 0.2573 & 0.1224 & 0.0233 & 0.1066 & 0.0641 & 0.2003 & 0.0940\\
MLP & 0.0351 & 0.1520 & 0.0927 & 0.2671 & 0.1296 & 0.0317 & 0.1392 & 0.0848 & 0.2542 & 0.1215 & 0.0252 & 0.1142 & 0.0688 & 0.2077 & 0.0988 \\
P5 & 0.0726 & 0.1955 & 0.1355 & 0.2802 & 0.1627 & 0.0608 & 0.1564 & 0.1096 & 0.2300 & 0.1332 & 0.0451 & 0.1322 & 0.0889 & 0.2023 & 0.1114 \\
RSL & 0.0892 & 0.2092 & 0.1502 & \ul{0.3001} & 0.1703 & 0.0607 & 0.1612 & 0.1110 & 0.2209 & 0.1302 & 0.0389 & 0.1423 & 0.0825 & 0.1926 & 0.1028 \\
POD & \ul{0.0927} & \ul{0.2105} & \ul{0.1539} & {0.2889} & \ul{0.1782} & \ul{0.0846} & \ul{0.1931} & \ul{0.1404} & \ul{0.2677} & \ul{0.1639} & \ul{0.0579} & \ul{0.1461} & \ul{0.1029} & \ul{0.2119} & \ul{0.1244}\\
\textbf{Ours} & \textbf{0.1285} & \textbf{0.2747} & \textbf{0.2033} & \textbf{0.3683} & \textbf{0.2326} & \textbf{0.1203} & \textbf{0.2572} & \textbf{0.1902} & \textbf{0.3380} & \textbf{0.2160} & \textbf{0.0660} & \textbf{0.1655} & \textbf{0.1171} & \textbf{0.2375} & \textbf{0.1398} \\
\hline
Impv. (\%) & \textbf{38.6}*& \textbf{30.5}*& \textbf{32.1}* & \textbf{27.5}* & \textbf{30.5}* & \textbf{42.2}* & \textbf{33.2}* & \textbf{35.8}* & \textbf{26.3}* & \textbf{31.8}* & \textbf{13.9}* & \textbf{13.2}* & \textbf{13.8}* & \textbf{12.1}* & \textbf{12.4}* \\
p-value & 2.3e-14 & 1.1e-14 & 2.8e-15 & 1.1e-16 & 5.0e-15 & 3.8e-15 & 2.0e-15 & 1.7e-15 & 2.7e-15 & 2.1e-15  & 5.6e-7 & 4.4e-8 & 2.4e-8 & 1.2e-8 & 9.8e-9 \\
\hline
\end{tabular}
}
\caption{\label{tab:top_n_recommendation} Comparison on top-N recommendation. The T-test shows the results by RDRec and the second-best, POD.}


%The results of the T-test were obtained by comparing RDRec and the second-best baseline, POD.}



\end{table*}
```

## Table 4
```latex
\begin{table}
\centering
\resizebox{.95\linewidth}{!}{ % \columnwidth % \paperwidth
  \begin{tabular}{cc|cc|cc|cc}
\hline
% \multirow {2}{*}{Ratio}
    \multirow {2}{*}{UsP} &  \multirow {2}{*}{ItA} & \multicolumn{2}{|c|}{Sports} & \multicolumn{2}{c|}{Beauty} & \multicolumn{2}{c}{Toys}\\
 & & H@10 & N@10 & H@10 &N@10 & H@10 & N@10\\
\hline
\multicolumn{8}{c}{Sequential recommendation}\\
\hline
   \ding{56} & \ding{56} & {0.0566} & {0.0408} & {0.0705} & {0.0479} & {0.0768} & {0.0573} \\
   \ding{52} & \ding{56} & \ul{0.0581} & \ul{0.0425} & \ul{0.0729} & \ul{0.0494} & {0.0787} & 0.0589\\
   \ding{56} & \ding{52}&  {0.0573} & {0.0411} & {0.0712} & {0.0492} & \ul{0.0788} & \ul{0.0593}\\
   \ding{52} & \ding{52}& \textbf{0.0596} & \textbf{0.0433} & \textbf{0.0743} & \textbf{0.0504} & \textbf{0.0802} & \textbf{0.0605} \\
\hline
\multicolumn{8}{c}{Top-N recommendation}\\
\hline
    \ding{56} & \ding{56}  & 0.2977 & 0.1850 & 0.2777 & 0.1701 & 0.2200 & 0.1284 \\
    \ding{52} & \ding{56} & 0.3509 & 0.2200 & 0.3080 & 0.1912 & 0.2214 & 0.1307 \\
    \ding{56} & \ding{52}& \ul{0.3513} & \ul{0.2249} & \ul{0.3275} & \ul{0.2048} & \ul{0.2321} & \ul{0.1370} \\
    \ding{52} & \ding{52}& \textbf{0.3683} & \textbf{0.2326} & \textbf{0.3380} & \textbf{0.2160} & \textbf{0.2375} & \textbf{0.1398}\\
\hline
\end{tabular}
    }
  \caption{\label{tab:ablation_study} Ablation study. ``w/o X'' denotes the removed parts. ``UsP'' and ``ItA'' indicate the distillation of user preferences and item attributes, respectively.}
\end{table}
```

## Table 5
```latex
\begin{table}
\centering
\resizebox{\linewidth}{!}{ % \columnwidth % \paperwidth
  \begin{tabular}{c|cc|cc|cc}
\hline
% \multirow {2}{*}{Ratio}
    Ratio & \multicolumn{2}{|c|}{Sports} & \multicolumn{2}{c|}{Beauty} & \multicolumn{2}{c}{Toys}\\
 EG:RG:SR:TR& H@10 & N@10 & H@10 &N@10 & H@10 & N@10\\
\hline
\multicolumn{7}{c}{Sequential recommendation}\\
\hline
    1\ :\ 1\ :\ 1\ :\ 1 & \textbf{0.0596} & \textbf{0.0433} & \textbf{0.0743} & \textbf{0.0504} & 0.0789 & 0.0594\\
    1\ :\ 1\ :\ 2\ :\ 1 & \ul{0.0593} & \ul{0.0431} & \ul{0.0735} & \ul{0.0502} & \ul{0.0790} & \ul{0.0601} \\
    1\ :\ 1\ :\ 1\ :\ 3 & 0.0592 & 0.0426 & 0.0702 & 0.0445 & \textbf{0.0802} & \textbf{0.0605} \\
\hline
\multicolumn{7}{c}{Top-N recommendation}\\
\hline
    1\ :\ 1\ :\ 1\ :\ 1 & \ul{0.3261} & \ul{0.2022} & \ul{0.2855} & \ul{0.1854} & \ul{0.2214} & \ul{0.1307} \\
    1\ :\ 1\ :\ 2\ :\ 1 & 0.2822 & 0.1722 & 0.2693 & 0.1584 & 0.1872 & 0.1037 \\
    1\ :\ 1\ :\ 1\ :\ 3 & \textbf{0.3683} & \textbf{0.2160} & \textbf{0.3380} & \textbf{0.2160} & \textbf{0.2375} & \textbf{0.1398}\\
\hline
\end{tabular}
    }
  \caption{\label{tab:ratio} Performance on the sample ratios of various tasks. ``EG'', ``RG'', ``SR'' and ``TR'' denote explanation and rationale generation, and sequential and top-N recommendations, respectively.}
\end{table}
```

## Table 6
```latex
\begin{table*}
\centering
\resizebox{\linewidth}{!}{ % \columnwidth % \paperwidth
\begin{tabular}{c|cccc|cccc|cccc}
\hline
% \multirow {2}{*}{Ratio}
Ratio & \multicolumn{4}{c|}{Sports} & \multicolumn{4}{c|}{Beauty} & \multicolumn{4}{c}{Toys}\\
EG:RG:SR:TR& H@5 &N@5 & H@10 & N@10 & H@5 &N@5 & H@10 & N@10 & H@5 &N@5 & H@10 & N@10\\
\hline
\multicolumn{13}{c}{Sequential recommendation}\\
\hline
1\ :\ 1\ :\ 1\ :\ 1 & \textbf{0.0503} & \textbf{0.0402} & \textbf{0.0596} & \textbf{0.0433} & \textbf{0.0601} & \textbf{0.0461} & \textbf{0.0743} & \textbf{0.0504} & 0.0716 & 0.0579 & 0.0789 & 0.0594\\
1\ :\ 1\ :\ 2\ :\ 1 & \ul{0.0501} & \ul{0.0398} & \ul{0.0593} & \ul{0.0431} & \ul{0.0595} & \ul{0.0457} & \ul{0.0735} & \ul{0.0502} & 0.0713 & 0.0581 & 0.0790 & 0.0601\\
1\ :\ 1\ :\ 3\ :\ 1 & 0.0496 & 0.0399 & 0.0578 & 0.0420 & 0.0573 & 0.0417 & 0.0662 & 0.0452 & 0.0713 & 0.0583 & 0.0792 & 0.0601\\
1\ :\ 1\ :\ 1\ :\ 2 & 0.0489 & 0.0374 & 0.0571 & 0.0387 & 0.0565 & 0.0419 & 0.0715 & 0.0466 & \ul{0.0717} & \ul{0.0588} & \ul{0.0799} & \ul{0.0602}\\
1\ :\ 1\ :\ 1\ :\ 3  & 0.0483 & 0.0369 & 0.0592 & 0.0426 & {0.0547} & {0.0395} & {0.0702} & {0.0445} & \textbf{0.0723} & \textbf{0.0593} & \textbf{0.0802} & \textbf{0.0605} \\
\hline
\multicolumn{13}{c}{Top-N recommendation}\\
\hline
1\ :\ 1\ :\ 1\ :\ 1 & 0.2381 & 0.1750 & 0.3261 & 0.2022 & 0.2136 & 0.1516 & 0.2885 & 0.1854 & 0.1482 & 0.1062 & 0.2144 & 0.1307\\
1\ :\ 1\ :\ 2\ :\ 1 & 0.2042 & 0.1476 & 0.2822 & 0.1722 & 0.1845 & 0.1350 & 0.2693 & 0.1584 & 0.1253 & 0.0876 & 0.1872 & 0.1037\\
1\ :\ 1\ :\ 3\ :\ 1 & 0.1524 & 0.1080 & 0.2101 & 0.1298  & 0.1424 & 0.1024 & 0.2178 & 0.1359 & 0.1118 & 0.0780 & 0.1803 & 0.0998\\
1\ :\ 1\ :\ 1\ :\ 2 & \ul{0.2439} & \ul{0.1810} & \ul{0.3303} & \ul{0.2067} & \ul{0.2372} & \ul{0.1784} & \ul{0.3237} & \ul{0.2030} & \ul{0.1579} & \ul{0.1091} & \ul{0.2221} & \ul{0.1339}\\
1\ :\ 1\ :\ 1\ :\ 3 & \textbf{0.2747} & \textbf{0.2033} & \textbf{0.3683} & \textbf{0.2326} & \textbf{0.2572} & \textbf{0.1902} & \textbf{0.3380} & \textbf{0.2160} & \textbf{0.1655} & \textbf{0.1171} & \textbf{0.2375} & \textbf{0.1398} \\
\hline

\end{tabular}
}
\caption{\label{tab:detail_of_sample_ratio} Performance comparison on various sample ratios for training RDRec. ``EG'', ``RG'', ``SR'' and ``TR'' denote explanation generation, rationale generation, and sequential and top-N recommendations, respectively.}
\end{table*}
```

## Table 7
```latex
\begin{table}
\centering
\resizebox{\linewidth}{!}{ % \columnwidth % \paperwidth
  \begin{tabular}{c|cccc}
\hline
    \multirow {2}{*}{\textbf{Datasets}} & \multicolumn{4}{c}{\textbf{Stages}} \\
    & \textbf{Distillation} & \textbf{Pre-training} & \textbf{SR} & \textbf{TR}\\
\hline
    Sports & 16h46m28s  & 16h23m23s & 15m03s & 18m23s \\
\hline
    Beauty & 11h50m14s & 12h45m12s & 13m33s & 16m07s \\
\hline
    Toys & 09h13m05s & 08h39m37s & 16m25s & 18m21s \\
\hline
\end{tabular}
}
\caption{\label{tab:running_time} Execution time in various stages. ``SR'' and ``TR'' represent the cumulative inference time for all users in sequential and top-N recommendations, respectively. ``h'', ``m'', and ``s'' refer to ``hours'' and ``minutes'', and ``seconds'' respectively.}
\end{table}
```

