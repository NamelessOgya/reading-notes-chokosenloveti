# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
\centering
\caption{Comprehensive comparisons with existing efficient recommendation methods.}
\label{table:Method}
\vspace{-4mm}
\resizebox{0.8\textwidth}{!}{\begin{tabular}{l|cccccccc}
\toprule
\multirow{2}{*}{Method} & \multirow{2}{*}{Category}  & \multicolumn{3}{c}{Saving} & \multirow{2}{*}{End-to-end} & \multirow{2}{*}{\makecell[c]{Budget \\ controllable}} & \multirow{2}{*}{\makecell[c]{Non-uniform \\ embedding size}} & \multirow{2}{*}{\makecell[c]{Performance \\ reserved}} \\
\cline{3-5}
& & Training cost & Inference cost & Memory & & \\
\toprule
TKD  \cite{kang2021topology}      & KD        & \ding{55} & \ding{51} & \ding{55} & \ding{55} & \ding{51} & \ding{55} & \ding{55} \\
RKD \cite{tang2018ranking} 		  & KD        & \ding{55} & \ding{51} & \ding{55} & \ding{55} & \ding{51} & \ding{55} & \ding{55} \\
AutoEmb \cite{zhaok2021autoemb}   & AutoML    & \ding{55} & \ding{51} & \ding{55} & \ding{51} & \ding{55} & \ding{51} & \ding{51} \\
ESAPN \cite{liu2020automated}     & AutoML    & \ding{55} & \ding{51} & \ding{55} & \ding{51} & \ding{55} & \ding{51} & \ding{51} \\
PEP \cite{liu2021learnable}       & MP        & \ding{51} & \ding{51} & \ding{51} & \ding{51} & \ding{55} & \ding{51} & \ding{55} \\ 
LTH-MRS \cite{wang2022exploring}  & MP        & \ding{55} & \ding{51} & \ding{55} & \ding{55} & \ding{55} & \ding{51} & \ding{51} \\ 
\midrule
Ours     & MP & \ding{51} & \ding{51}  & \ding{51} & \ding{51} & \ding{51} & \ding{51} & \ding{51} \\
\bottomrule
\end{tabular}}
\vspace{-2mm}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
\centering
\caption{Performance over diverse models. 
$l$ and $d$ denote the layer number and the embedding size, respectively.
Following work \cite{chen2021unified}, we use MACs (Tr.) and  MACs (In.) to measure the training and inference computational costs, respectively.}
\label{table:backbone}
% \begin{threeparttable}
\vspace{-4mm}
\resizebox{\textwidth}{40mm}{\begin{tabular}{ccccccccccccc}
\toprule
\multirow{2}{*}{Model} & \multicolumn{4}{c}{MovieLens-1M} & \multicolumn{4}{c}{CiteUlike} & \multicolumn{4}{c}{Foursquare} \\ 
% \cmidrule(r){2-13}
\cmidrule(r){2-5}  \cmidrule(r){6-9} \cmidrule(r){10-13}
& MACs (Tr.) & MACs (In.) & Recall/HR & NDCG & MACs (Tr.) & MACs (In.) & Recall/HR & NDCG & MACs (Tr.) & MACs (In.) & Recall/HR & NDCG \\
\toprule
NeuMF                      & 3.13e+13 & 9.68e+08 & 0.7867 & 0.4478  & 3.85e+12 & 8.87e+08 & 0.4000 & 0.2053 & 3.72e+13 & 2.50e+09 & 0.4940 & 0.2723 \\
\rowcolor{gray!20} + DSL   & 2.09e+13 & 6.47e+08 & 0.7525 & 0.4531  & 2.58e+12 & 5.93e+08 & 0.4000 & 0.2809 & 2.49e+13 & 1.67e+09 & 0.5663 & 0.3449 \\
\midrule
ConvNCF                    & 1.50e+15 & 4.65e+10 & 0.7745 & 0.5261  & 1.83e+14 & 4.26e+10 & 0.3429 & 0.2816 & 1.76e+15 & 1.20e+11 & 0.5301 & 0.2583 \\
\rowcolor{gray!20} + DSL   & 0.38e+15 & 1.19e+10 & 0.7990 & 0.4875  & 0.46e+14 & 1.09e+10 & 0.3714 & 0.2076 & 0.45e+15 & 0.31e+11 & 0.4940 & 0.3115      \\
\midrule
MultVAE                    & 2.40e+12 & 1.08e+10 & 0.3099 & 0.3052  & 1.36e+13 & 6.40e+10 & 0.2260 & 0.1278 & 4.61e+13 & 2.24e+11 & 0.1550 & 0.1639 \\
\rowcolor{gray!20} + DSL   & 1.20e+12 & 0.54e+10 & 0.3080 & 0.3005  & 0.68e+13 & 3.20e+10 & 0.2044 & 0.1093 & 3.69e+13 & 1.79e+11 & 0.1427 & 0.1485 \\
\midrule
CDAE                       & 2.67e+11 & 1.26e+10 & 0.3254 & 0.3236  & 3.60e+12 & 6.77e+10 & 0.1687 & 0.1080 & 1.15e+13 & 2.27e+11 & 0.2504 & 0.2452 \\
\rowcolor{gray!20} + DSL   & 1.33e+11 & 0.63e+10 & 0.3657 & 0.3656  & 1.80e+12 & 3.39e+10 & 0.1423 & 0.0962 & 0.92e+13 & 1.82e+11 & 0.2350 & 0.2303 \\
\midrule
\multirow{2}{*}{} & \multicolumn{4}{c}{Amazon-Book} & \multicolumn{4}{c}{Yelp2018} & \multicolumn{4}{c}{Gowalla} \\ 
\cmidrule(r){2-5}  \cmidrule(r){6-9} \cmidrule(r){10-13}
& MACs (Tr.) & MACs (In.) & Recall & NDCG  & MACs (Tr.) & MACs (In.) & Recall & NDCG & MACs (Tr.) & MACs (In.) & Recall & NDCG \\
\midrule
LightGCN ($l$=3)           & 1.59e+20 & 6.88e+13 & 0.0414 & 0.0321 & 4.00e+19 & 3.32e+13 & 0.0642 & 0.0528 & 1.75e+19 & 2.21e+13 & 0.1816 & 0.1550  \\ 
\rowcolor{gray!20} + DSL   & 0.95e+20 & 4.14e+13 & 0.0416 & 0.0325 & 2.67e+19 & 2.22e+13 & 0.0641 & 0.0527 & 1.16e+19 & 1.48e+13 & 0.1813 & 0.1547  \\ 
\midrule
LightGCN ($l$=4)           & 2.12e+20 & 9.17e+13 & 0.0406 & 0.0313 & 5.34e+19 & 4.42e+13 & 0.0649 & 0.0530 & 2.33e+19 & 2.95e+13 & 0.1830 & 0.1550  \\ 
\rowcolor{gray!20} + DSL   & 1.17e+20 & 5.06e+13 & 0.0405 & 0.0314 & 3.34e+19 & 2.77e+13 & 0.0651 & 0.0536 & 1.45e+19 & 1.84e+13 & 0.1821 & 0.1544  \\ 
\midrule
UltraGCN ($d$=64)          & 5.02e+13 & 6.24e+11 & 0.0678 & 0.0553 & 2.37e+13 & 15.5e+10 & 0.0673 & 0.0554 & 9.05e+13 & 1.61e+11 & 0.1858 & 0.1576  \\ 
\rowcolor{gray!20} + DSL   & 2.69e+13 & 1.56e+11 & 0.0685 & 0.0563 & 1.68e+13 & 9.89e+10 & 0.0645 & 0.0530 & 6.23e+13 & 1.03e+11 & 0.1742 & 0.1448  \\ 
\midrule
UltraGCN ($d$=128)         & 9.85e+13 & 1.25e+12 & 0.0712 & 0.0582 & 4.62e+13 & 3.09e+11 & 0.0676 & 0.0556 & 1.76e+14 & 3.22e+11 & 0.1844 & 0.1539  \\ 
\rowcolor{gray!20} + DSL   & 5.18e+13 & 0.31e+12 & 0.0727 & 0.0582 & 3.23e+13 & 1.98e+11 & 0.0651 & 0.0532 & 1.20e+14 & 2.06e+11 & 0.1792 & 0.1478  \\
\bottomrule
\end{tabular}}

% \begin{tablenotes}
%         \footnotesize
%         \item[*]$l$ and $d$ denote the layer number and the embedding dimension, respectively. 
%         % \item[**] my website is ... 
%       \end{tablenotes}
%       \end{threeparttable}
\end{table*}
```

## Table 3
```latex
\begin{table*}[t]
\centering
\caption{Result comparisons of diverse solutions for efficient recommendation. The average and standard deviation results are reported across five random runs. We adopt the models with different embedding sizes. The bold and underlined numbers highlight the best and the second best performance, respectively.}
\vspace{-4mm}
\label{table:baselines}
\resizebox{\textwidth}{28mm}{\begin{tabular}{ccccccccccc}
\toprule
\multirow{2}{*}{Category} & \multirow{2}{*}{Method} & \multicolumn{4}{c}{Embedding size=64} & \multicolumn{4}{c}{Embedding size=128} & \multirow{2}{*}{\makecell[c]{Average \\ MACs}} \\ 
\cmidrule(r){3-6}  \cmidrule(r){7-10} &
& MACs (Tr.) & Memory & Recall & NDCG & MACs (Tr.) & Memory & Recall & NDCG &  \\
\toprule
& Baseline & 4.00e+19 & 2103M & 0.0642\scriptsize{(.0001)} & 0.0528\scriptsize{(.0002)} & 8.01e+19 & 2399M & {0.0673\scriptsize\scriptsize{(.0003)}} & 0.0550\scriptsize{(.0001)} & 0 \\ 
\midrule
\multirow{2}{*}{KD} & RKD  & 6.00e+19 & 2103M & 0.0558\scriptsize{(.0005)} & 0.0460\scriptsize{(.0004)} & 1.20e+20 & 2399M & 0.0610\scriptsize{(.0003)} & 0.0493\scriptsize{(.0004)} & \cred{+ 49.9\%}  \\
& TKD       & 6.67e+19 & 2103M & 0.0615\scriptsize{(.0007)} & 0.0514\scriptsize{(.0006)} & 1.34e+20 & 2399M & 0.0645\scriptsize{(.0005)} & 0.0533\scriptsize{(.0003)} & \cred{+ 67.1\%}  \\
\midrule
\multirow{2}{*}{AutoML} & AutoEmb & 7.92e+19 & 4210M & 0.0627\scriptsize{(.0002)} & 0.0511\scriptsize{(.0003)}  & 1.58e+20 & 4521M & 0.0654\scriptsize{(.0003)} & 0.0536\scriptsize{(.0003)} & \cred{+ 97.7\%} \\
& ESAPN  & 1.91e+20 & 4364M & \underline{0.0638\scriptsize{(.0002)}} & \underline{0.0525\scriptsize{(.0002)}} & 3.81e+20  & 4675M & \underline{0.0672\scriptsize{(.0003)}} & \underline{0.0545\scriptsize{(.0002)}} & \cred{+ 376.6\%}  \\
\midrule
\multirow{6}{*}{MP} & RP  & \textbf{2.67e+19}  & \textbf{1052M}  & 0.0557\scriptsize{(.0011)} & 0.0458\scriptsize{(.0010)} & \textbf{5.34e+19} & \textbf{1199M} & 0.0608\scriptsize{(.0009)} & 0.0498\scriptsize{(.0009)} & \textbf{\cgreen{- 33.3\%}} \\ 
& OMP      & 6.67e+19 & 2103M & 0.0622\scriptsize{(.0000)} & 0.0509\scriptsize{(.0001)} & 1.33e+20  & 2399M & 0.0661\scriptsize{(.0001)} & 0.0542\scriptsize{(.0000)} & \cred{+ 66.4\%}  \\ 
& WR       & 1.93e+20 & 2103M & 0.0621\scriptsize{(.0003)} & 0.0501\scriptsize{(.0004)} & 3.85e+20  & 2399M & 0.0661\scriptsize{(.0004)} & 0.0537\scriptsize{(.0005)} & \cred{+ 381.6\%}  \\ 
& PEP      & \underline{3.34e+19} & \underline{2082M} & 0.0592\scriptsize{(.0013)} & 0.0484\scriptsize{(.0011)} & \underline{6.68e+19} & \underline{2375M} & 0.0623\scriptsize{(.0009)} & 0.0501\scriptsize{(.0010)} & \cgreen{- 16.5\%}  \\
& LTH-MRS  & 1.93e+20 & 2103M  & 0.0635\scriptsize{(.0000)} & 0.0525\scriptsize{(.0001)} & 3.85e+20  & 2399M & 0.0666\scriptsize{(.0001)} & 0.0545\scriptsize{(.0001)} & \cred{+ 381.6\%}  \\ 
& DSL (Ours)   & \textbf{2.67e+19} & \textbf{1052M} & \textbf{0.0641\scriptsize{(.0002)}} & \textbf{0.0527\scriptsize{(.0001)}} & \textbf{5.34e+19} & \textbf{1199M} & \textbf{0.0675\scriptsize{(.0003)}} & \textbf{0.0553\scriptsize{(.0002)}} & \textbf{\cgreen{- 33.3\%}} \\ 
\bottomrule
\end{tabular}}
\end{table*}
```

## Table 4
```latex
\begin{table}[t]
% \centering
% \caption{Comparisons with different decay functions.}
% \vspace{-2mm}
% \renewcommand\arraystretch{1.2}
% \label{table:decay}
% \resizebox{0.46\textwidth}{12mm}{\begin{tabular}{lcccccc}
% \toprule
% \multirow{2}{*}{Type}   & \multicolumn{2}{c}{Amazon-book} & \multicolumn{2}{c}{Yelp2018} & \multicolumn{2}{c}{Gowalla} \\
% \cmidrule(r){2-3} \cmidrule(r){4-5} \cmidrule(r){6-7}
%     & Recall & NDCG & Recall & NDCG & Recall & NDCG \\
% \toprule
% Cosine   & 0.0406 & 0.0316 & 0.0641 & 0.0527 & 0.1812 & 0.1546  \\ 
% Linear   & 0.0409 & 0.0317 & 0.0638 & 0.0525 & 0.1803 & 0.1538  \\
% No decay & 0.0394 & 0.0307 & 0.0618 & 0.0507 & 0.1773 & 0.1518  \\ 
% \bottomrule
% \vspace{-8mm}
% \end{tabular}}
% \end{table}
```

## Table 5
```latex
\begin{table}[t]
\centering
\caption{Comparisons with different decay functions.}
\vspace{-4mm}
\renewcommand\arraystretch{0.9}
\label{table:decay}
\begin{tabular}{lcccccc}
\toprule
\multirow{2}{*}{Type}   & \multicolumn{2}{c}{Amazon-book} & \multicolumn{2}{c}{Yelp2018} & \multicolumn{2}{c}{Gowalla} \\
\cmidrule(r){2-3} \cmidrule(r){4-5} \cmidrule(r){6-7}
    & Recall & NDCG & Recall & NDCG & Recall & NDCG \\
\toprule
Cosine   & 0.0406 & 0.0316 & 0.0641 & 0.0527 & 0.1812 & 0.1546  \\ 
Linear   & 0.0409 & 0.0317 & 0.0638 & 0.0525 & 0.1803 & 0.1538  \\
No decay & 0.0394 & 0.0307 & 0.0618 & 0.0507 & 0.1773 & 0.1518  \\ 
\bottomrule
\vspace{-4mm}
\end{tabular}
\end{table}
```

