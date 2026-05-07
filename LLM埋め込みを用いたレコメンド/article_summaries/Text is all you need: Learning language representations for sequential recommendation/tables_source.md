# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\small
\centering
\caption{Statistics of the datasets after preprocessing. Avg. n denotes the average length of item sequences.}
\label{tab:stat}
\begin{tabular}{lrrrrr}
\toprule
\multicolumn{1}{c}{\textbf{Datasets}} & \multicolumn{1}{c}{\textbf{\#Users}} & \multicolumn{1}{c}{\textbf{\#Items}} & \multicolumn{1}{c}{\textbf{\#Inters.}} & \multicolumn{1}{c}{\textbf{Avg. n}} & \multicolumn{1}{c}{\textbf{Density}} \\ \midrule
\textbf{Pre-training}                 & 3,613,906                            & 1,022,274                            & 33,588,165                             & 9.29                                & 9.1e-6                               \\
-Training                             & 3,501,527                            & 954,672                              & 32,291,280                             & 9.22                                & 9.0e-6                               \\
-Validation                           & 112,379                              & 67,602                               & 1,296,885                              & 11.54                               & 1.7e-4                               \\ \midrule
\textbf{Scientific}                   & 11,041                               & 5,327                                & 76,896                                 & 6.96                                & 1.3e-3                               \\
\textbf{Instruments}                  & 27,530                               & 10,611                               & 231,312                                & 8.40                                & 7.9e-4                               \\
\textbf{Arts}                         & 56,210                               & 22,855                               & 492,492                                & 8.76                                & 3.8e-4                               \\
\textbf{Office}                       & 101,501                              & 27,932                               & 798,914                                & 7.87                                & 2.8e-4                               \\
\textbf{Games}                        & 11,036                               & 15,402                               & 100,255                                & 9.08                                & 5.9e-4                               \\
\textbf{Pet}                          & 47,569                               & 37,970                               & 420,662                                & 8.84                                & 2.3e-4                               \\ \bottomrule
\end{tabular}
\end{table}
```

## Table 2
```latex
\begin{table*}[t]
\centering
\small
\caption{Performance comparison of different recommendation models. The best and the second-best 
%performances 
performance
is bold and underlined respectively. Improv.~denotes the relative improvement of \our over the best baselines.}
\vspace{-3mm}
\label{tab:perf}
\scalebox{0.9}{
\setlength{\tabcolsep}{1mm}{
\begin{tabular}{llcccccccccc}
\toprule
\multicolumn{1}{c}{\textbf{}} &    \multicolumn{1}{c}{\textbf{}}   & \multicolumn{4}{c}{\textbf{ID-Only Methods}}                                                                    & \multicolumn{2}{c}{\textbf{ID-Text Methods}} & \multicolumn{3}{c}{\textbf{Text-Only Methods}}          & \multirow{2}{*}{\textbf{Improv.}} \\ \cmidrule(lr){3-6} \cmidrule(lr){7-8} \cmidrule(lr){9-11}
\multicolumn{1}{c}{\textbf{Dataset}} & \multicolumn{1}{c}{\textbf{Metric}} & \textbf{GRU4Rec} & \textbf{SASRec} & \textbf{BERT4Rec} & \textbf{RecGURU} & \textbf{FDSA}        & \textbf{S$^3$-Rec}       & \textbf{ZESRec} & \textbf{UniSRec} & \textbf{\our} &                                      \\ \midrule
\multirow{3}{*}{Scientific}          & NDCG@10                             & 0.0826           & 0.0797          & 0.0790            & 0.0575           & 0.0716               & 0.0451                & 0.0843          & {\ul 0.0862}     & \textbf{0.1027}    & 19.14\%                              \\
                                     & Recall@10                           & 0.1055           & {\ul 0.1305}    & 0.1061            & 0.0781           & 0.0967               & 0.0804                & 0.1260          & 0.1255           & \textbf{0.1448}    & 10.96\%                              \\
                                     & MRR                                 & 0.0702           & 0.0696          & 0.0759            & 0.0566           & 0.0692               & 0.0392                & 0.0745          & {\ul 0.0786}     & \textbf{0.0951}    & 20.99\%                              \\ \midrule
\multirow{3}{*}{Instruments}         & NDCG@10                             & 0.0633           & 0.0634          & 0.0707            & 0.0468           & 0.0731               & {\ul 0.0797}          & 0.0694          & 0.0785           & \textbf{0.0830}    & 4.14\%                               \\
                                     & Recall@10                           & 0.0969           & 0.0995          & 0.0972            & 0.0617           & 0.1006               & {\ul 0.1110}          & 0.1078          & \textbf{0.1119}  & 0.1052             & -                                    \\
                                     & MRR                                 & 0.0707           & 0.0577          & 0.0677            & 0.0460           & 0.0748               & {\ul 0.0755}          & 0.0633          & 0.0740           & \textbf{0.0807}    & 6.89\%                               \\ \midrule
\multirow{3}{*}{Arts}                & NDCG@10                             & {\ul 0.1075}     & 0.0848          & 0.0942            & 0.0525           & 0.0994               & 0.1026                & 0.0970          & 0.0894           & \textbf{0.1252}    & 16.47\%                              \\
                                     & Recall@10                           & 0.1317           & 0.1342          & 0.1236            & 0.0742           & 0.1209               & {\ul 0.1399}          & 0.1349          & 0.1333           & \textbf{0.1614}    & 15.37\%                              \\
                                     & MRR                                 & 0.1041           & 0.0742          & 0.0899            & 0.0488           & 0.0941               & {\ul 0.1057}          & 0.0870          & 0.0798           & \textbf{0.1189}    & 12.49\%                              \\ \midrule
\multirow{3}{*}{Office}              & NDCG@10                             & 0.0761           & 0.0832          & {\ul 0.0972}      & 0.0500           & 0.0922               & 0.0911                & 0.0865          & 0.0919           & \textbf{0.1141}    & 17.39\%                              \\
                                     & Recall@10                           & 0.1053           & 0.1196          & 0.1205            & 0.0647           & {\ul 0.1285}         & 0.1186                & 0.1199          & 0.1262           & \textbf{0.1403}    & 9.18\%                               \\
                                     & MRR                                 & 0.0731           & 0.0751          & 0.0932            & 0.0483           & {\ul 0.0972}         & 0.0957                & 0.0797          & 0.0848           & \textbf{0.1089}    & 12.04\%                              \\ \midrule
\multirow{3}{*}{Games}               & NDCG@10                             & 0.0586           & 0.0547          & {\ul 0.0628}      & 0.0386           & 0.0600               & 0.0532                & 0.0530          & 0.0580           & \textbf{0.0684}    & 8.92\%                               \\
                                     & Recall@10                           & 0.0988           & 0.0953          & {\ul 0.1029}      & 0.0479           & 0.0931               & 0.0879                & 0.0844          & 0.0923           & \textbf{0.1039}    & 0.97\%                               \\
                                     & MRR                                 & 0.0539           & 0.0505          & {\ul 0.0585}      & 0.0396           & 0.0546               & 0.0500                & 0.0505          & 0.0552           & \textbf{0.0650}    & 11.11\%                              \\ \midrule
\multirow{3}{*}{Pet}                 & NDCG@10                             & 0.0648           & 0.0569          & 0.0602            & 0.0366           & 0.0673               & 0.0742                & {\ul 0.0754}    & 0.0702           & \textbf{0.0972}    & 28.91\%                              \\
                                     & Recall@10                           & 0.0781           & 0.0881          & 0.0765            & 0.0415           & 0.0949               & {\ul 0.1039}          & 0.1018          & 0.0933           & \textbf{0.1162}    & 11.84\%                              \\
                                     & MRR                                 & 0.0632           & 0.0507          & 0.0585            & 0.0371           & 0.0650               & {\ul 0.0710}          & 0.0706          & 0.0650           & \textbf{0.0940}    & 32.39\%                              \\ \bottomrule
                                     
\end{tabular}
}}
\end{table*}
```

## Table 3
```latex
\begin{table}[t]
\centering
\small
\caption{Performance of models compared between in-set items and cold-start items on four datasets. N@10 and R@10 stand for NDCG@10 and Recall@10 respectively.}
\vspace{-3mm}
\label{tab:cold}
\scalebox{1}{
\setlength{\tabcolsep}{1mm}{
\begin{tabular}{llcccccc}
\toprule
\multicolumn{1}{c}{\textbf{}}        & \multicolumn{1}{c}{\textbf{}}       & \multicolumn{2}{c}{\textbf{SASRec}} & \multicolumn{2}{c}{\textbf{UniSRec}} & \multicolumn{2}{c}{\textbf{\our}} \\ \cmidrule(l){3-8} 
\multicolumn{1}{c}{\textbf{Dataset}} & \multicolumn{1}{c}{\textbf{Metric}} & \textbf{In-Set}   & \textbf{Cold}   & \textbf{In-Set}    & \textbf{Cold}   & \textbf{In-Set}     & \textbf{Cold}    \\ \midrule
\multirow{2}{*}{Scientific}          & N@10                                & 0.0775            & 0.0213          & 0.0864             & 0.0441          & 0.1042              & 0.0520           \\
                                     & R@10                                & 0.1206            & 0.0384          & 0.1245             & 0.0721          & 0.1417              & 0.0897           \\ \midrule
\multirow{2}{*}{Instruments}         & N@10                                & 0.0669            & 0.0142          & 0.0715             & 0.0208          & 0.0916              & 0.0315           \\
                                     & R@10                                & 0.1063            & 0.0309          & 0.1094             & 0.0319          & 0.1130              & 0.0468           \\ \midrule
\multirow{2}{*}{Arts}                & N@10                                & 0.1039            & 0.0071          & 0.1174             & 0.0395          & 0.1568              & 0.0406           \\
                                     & R@10                                & 0.1645            & 0.0129          & 0.1736             & 0.0666          & 0.1866              & 0.0689           \\ \midrule
\multirow{2}{*}{Pet}                 & N@10                                & 0.0597            & 0.0013          & 0.0771             & 0.0101          & 0.0994              & 0.0225           \\
                                     & R@10                                & 0.0934            & 0.0019          & 0.1115             & 0.0175          & 0.1192              & 0.0400           \\ \bottomrule
\end{tabular}}}
\vspace{-4mm}
\end{table}
```

## Table 4
```latex
\begin{table*}[t]
\small
\centering
\caption{Ablation study on two downstream datasets. The best and the second-best scores are bold and underlined respectively.}
\vspace{-2mm}
\label{tab:ablation}
\scalebox{1}{
\setlength{\tabcolsep}{1mm}{
\begin{tabular}{lcccccc}
\toprule
\multicolumn{1}{c}{\multirow{2}{*}{\textbf{Variants}}} & \multicolumn{3}{c}{\textbf{Scientific}}                 & \multicolumn{3}{c}{\textbf{Instruments}}                \\ \cmidrule(l){2-4} \cmidrule(l){5-7} 
\multicolumn{1}{c}{}                                   & \textbf{NDCG@10} & \textbf{Recall@10} & \textbf{MRR}    & \textbf{NDCG@10} & \textbf{Recall@10} & \textbf{MRR}    \\ \midrule
(0) \our                                          & \textbf{0.1027}  & \textbf{0.1448}    & \textbf{0.0951} & \textbf{0.0830}  & \textbf{0.1052}    & \textbf{0.0807} \\ \cmidrule(r){1-1}
(1) w/o two-stage finetuning                           & 0.1023           & {\ul 0.1442}       & {\ul 0.0948}    & 0.0728           & 0.1005             & 0.0685          \\
(1) + (2) freezing word emb. \& item emb.              & {\ul 0.1026}     & 0.1399             & 0.0942          & 0.0728           & {\ul 0.1015}       & 0.0682          \\
(1) + (3) trainable word emb. \& item emb.             & 0.0970           & 0.1367             & 0.0873          & {\ul 0.0802}     & {\ul 0.1015}       & 0.0759          \\
(1) + (4) trainable item emb. \& freezing word emb.    & 0.0965           & 0.1383             & 0.0856          & 0.0801           & 0.1014             & {\ul 0.0760}    \\ \cmidrule(r){1-1}
(5) w/o pre-training                                    & 0.0722           & 0.1114             & 0.0650          & 0.0598           & 0.0732             & 0.0584          \\
(6) w/o item position emb. \& token type emb.                        & 0.1018           & 0.1427             & 0.0945          & 0.0518           & 0.0670             & 0.0501          \\ \bottomrule
\end{tabular}
}}
\vspace{-3mm}
\end{table*}
```

