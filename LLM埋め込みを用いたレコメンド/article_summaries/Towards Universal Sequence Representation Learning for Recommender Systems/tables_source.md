# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[!t] %
	\caption{Statistics of the datasets after preprocessing. ``Avg. $n$'' denotes the average length of item sequences. ``Avg. $c$'' denotes the average number of tokens in item text.
	}
	\label{tab:dataset}
	\resizebox{\columnwidth}{!}{
	\begin{tabular}{l *{5}{r}}
		\toprule
		\textbf{Datasets} & \textbf{\#Users} & \textbf{\#Items} & \textbf{\#Inters.} & \textbf{Avg. $n$} & \textbf{Avg. $c$}\\
		\midrule
		\textbf{Pre-trained} & 1,361,408 & 446,975 & 14,029,229 & 13.51 & 139.34 \\
		- Food   & 115,349 &  39,670 & 1,027,413 &  8.91 & 153.40 \\
		- CDs    &  94,010 &  64,439 & 1,118,563 & 12.64 & 80.43 \\
		- Kindle & 138,436 &  98,111 & 2,204,596 & 15.93 & 141.70 \\
		- Movies & 281,700 &  59.203 & 3,226,731 & 11.45 & 97.54 \\
		- Home   & 731,913 & 185,552 & 6,451,926 &  8.82 & 168.89 \\
		\midrule
		\textbf{Scientific}  &  8,442 &  4,385 &  59,427 & 7.04 & 182.87 \\
		\textbf{Pantry}      & 13,101 &  4,898 & 126,962 & 9.69 & 83.17 \\
		\textbf{Instruments} & 24,962 &  9,964 & 208,926 & 8.37 & 165.18 \\
		\textbf{Arts}        & 45,486 & 21,019 & 395,150 & 8.69 & 155.57 \\
		\textbf{Office}      & 87,436 & 25,986 & 684,837 & 7.84 & 193.22 \\ \midrule
		\textbf{Online Retail} & 16,520 & 3,469 & 519,906 & 26.90 & 27.80 \\
		\bottomrule
	\end{tabular}
	}
\end{table}
```

## Table 2
```latex
\begin{table*}[!ht]
\centering
\caption{Performance comparison of different recommendation models. The best and the second-best performances are denoted in bold and underlined fonts, respectively. ``Improv.'' indicates the relative improvement ratios of the proposed approach over the best performance baselines. ``*'' denotes that the improvements are significant at the level of 0.01 with paired $t$-test.}
\label{tab:exp-main}
\resizebox{2.1\columnwidth}{!}{
\begin{tabular}{@{}ccccccccccccr@{}}
\toprule
Scenario & Dataset & Metric & SASRec  & BERT4Rec & FDSA & S$^3$-Rec & CCDR & RecGURU & ZESRec & \ourt & \ourid & Improv. \\ \midrule \midrule
\multirow{20}{*}{\shortstack{Cross-\\Domain}} &
\multirow{4}{*}{Scientific} &
     Recall@10 & 0.1080 & 0.0488 & 0.0899 & 0.0525 & 0.0695 & 0.1023 & 0.0851 & \underline{0.1188}* & \textbf{0.1235}* & +14.35\% \\
 & & NDCG@10   & 0.0553 & 0.0243 & 0.0580 & 0.0275 & 0.0340 & 0.0572 & 0.0475 & \textbf{0.0641}* & \underline{0.0634}* & +10.52\% \\
 & & Recall@50 & 0.2042 & 0.1185 & 0.1732 & 0.1418 & 0.1647 & 0.2022 & 0.1746 & \underline{0.2394}* & \textbf{0.2473}* & +21.11\% \\
 & & NDCG@50   & 0.0760 & 0.0393 & 0.0759 & 0.0468 & 0.0546 & 0.0786 & 0.0670 & \underline{0.0903}* & \textbf{0.0904}* & +15.01\% \\
\cmidrule(l){2-13}
 & \multirow{4}{*}{Pantry} &
     Recall@10 & 0.0501 & 0.0308 & 0.0395 & 0.0444 & 0.0408 & 0.0469 & 0.0454 & \underline{0.0636}* & \textbf{0.0693}* & +38.32\% \\
 & & NDCG@10   & 0.0218 & 0.0152 & 0.0209 & 0.0214 & 0.0203 & 0.0209 & 0.0230 & \underline{0.0306}* & \textbf{0.0311}* & +35.22\% \\
 & & Recall@50 & 0.1322 & 0.1030 & 0.1151 & 0.1315 & 0.1262 & 0.1269 & 0.1141 & \underline{0.1658}* & \textbf{0.1827}* & +38.20\% \\
 & & NDCG@50   & 0.0394 & 0.0305 & 0.0370 & 0.0400 & 0.0385 & 0.0379 & 0.0378 & \underline{0.0527}* & \textbf{0.0556}* & +39.00\% \\
 \cmidrule(l){2-13}
 & \multirow{4}{*}{Instruments} &
     Recall@10 & 0.1118 & 0.0813 & 0.1070 & 0.1056 & 0.0848 & 0.1113 & 0.0783 & \underline{0.1189}* & \textbf{0.1267}* & +13.33\% \\
 & & NDCG@10   & 0.0612 & 0.0620 & \textbf{0.0796} & 0.0713 & 0.0451 & 0.0681 & 0.0497 & 0.0680 & \underline{0.0748}* & $-$ \\
 & & Recall@50 & 0.2106 & 0.1454 & 0.1890 & 0.1927 & 0.1753 & 0.2068 & 0.1387 & \underline{0.2255}* & \textbf{0.2387}* & +13.34\% \\
 & & NDCG@50   & 0.0826 & 0.0756 & \underline{0.0972} & 0.0901 & 0.0647 & 0.0887 & 0.0627 & 0.0912 & \textbf{0.0991}* & +1.95\% \\
 \cmidrule(l){2-13}
 & \multirow{4}{*}{Arts} &
     Recall@10 & \underline{0.1108} & 0.0722 & 0.1002 & 0.1003 & 0.0671 & 0.1084 & 0.0664 & 0.1066 & \textbf{0.1239}* & +11.82\% \\
 & & NDCG@10   & 0.0587 & 0.0479 & \textbf{0.0714} & 0.0601 & 0.0348 & 0.0651 & 0.0375 & 0.0586 & \underline{0.0712} & $-$ \\
 & & Recall@50 & 0.2030 & 0.1367 & 0.1779 & 0.1888 & 0.1478 & 0.1979 & 0.1323 & \underline{0.2049}* & \textbf{0.2347}* & +15.62\% \\
 & & NDCG@50   & 0.0788 & 0.0619 & \underline{0.0883} & 0.0793 & 0.0523 & 0.0845 & 0.0518 & 0.0799 & \textbf{0.0955}* & +8.15\% \\
 \cmidrule(l){2-13}
 & \multirow{4}{*}{Office} &
     Recall@10 & 0.1056 & 0.0825 & 0.1118 & 0.1030 & 0.0549 & \underline{0.1145} & 0.0641 & 0.1013 & \textbf{0.1280}* & +11.79\% \\
 & & NDCG@10   & 0.0710 & 0.0634 & \textbf{0.0868} & 0.0653 & 0.0290 & 0.0768 & 0.0391 & 0.0619 & \underline{0.0831} & $-$ \\
 & & Recall@50 & 0.1627 & 0.1227 & 0.1665 & 0.1613 & 0.1095 & \underline{0.1757} & 0.1113 & 0.1702 & \textbf{0.2016}* & +14.74\% \\
 & & NDCG@50   & 0.0835 & 0.0721 & \underline{0.0987} & 0.0780 & 0.0409 & 0.0901 & 0.0493 & 0.0769 & \textbf{0.0991} & +0.41\% \\
 \midrule
\multirow{4}{*}{\shortstack{Cross-\\Platform}} &
\multirow{4}{*}{\shortstack{Online\\ Retail}} &
     Recall@10 & 0.1460 & 0.1349 & \underline{0.1490} & 0.1418 & 0.1347 & 0.1467 & 0.1103 & 0.1449 & \textbf{0.1537}* & +3.15\% \\
 & & NDCG@10   & 0.0675 & 0.0653 & \underline{0.0719} & 0.0654 & 0.0620 & 0.0658 & 0.0535 & 0.0677 & \textbf{0.0724} & +0.70\% \\
 & & Recall@50 & 0.3872 & 0.3540 & 0.3802 & 0.3702 & 0.3587 & \textbf{0.3885} & 0.2750 & 0.3604 & \textbf{0.3885} & 0.00\% \\
 & & NDCG@50   & 0.1201 & 0.1131 & \underline{0.1223} & 0.1154 & 0.1108 & 0.1188 & 0.0896 & 0.1149 & \textbf{0.1239}* & +1.31\% \\
 \bottomrule
\end{tabular}
}
\end{table*}
```

## Table 3
```latex
\begin{table}[t]
\small
\caption{Comparison of the transfer learning scenarios and application settings of several approaches. $1\rightarrow 1$ denotes $1$ source domain to $1$ target domain, and $M \rightarrow N$ denotes $M$ source domains to $N$ target domains. ``Non-OL'' denotes that the approach doesn't require overlapped users or items.}
\label{tab:cmp}
\resizebox{\columnwidth}{!}{
\begin{tabular}{@{}lccccc@{}}
\toprule
\multirow{2}{*}{Methods} & \multicolumn{3}{c}{Transfer Learning Scenarios} & \multicolumn{2}{c}{Application Settings} \\ \cmidrule(l){2-4} \cmidrule(l){5-6}
          & $1 \rightarrow 1$ & $M \rightarrow N$ & Non-OL & Transductive            & Inductive            \\ \midrule
S$^3$-Rec~\cite{zhou2020s3rec}    & \textcolor{purple}{\XSolidBrush} & \textcolor{purple}{\XSolidBrush} & \textcolor{purple}{\XSolidBrush} & \textcolor{teal}{\CheckmarkBold} & \textcolor{purple}{\XSolidBrush} \\ 
PeterRec~\cite{yuan2020peterrec}  & \textcolor{teal}{\CheckmarkBold} & \textcolor{purple}{\XSolidBrush} & \textcolor{purple}{\XSolidBrush} & \textcolor{teal}{\CheckmarkBold} & \textcolor{purple}{\XSolidBrush} \\ 
RecGURU~\cite{li2022recguru}   & \textcolor{teal}{\CheckmarkBold} & \textcolor{purple}{\XSolidBrush} & \textcolor{teal}{\CheckmarkBold} & \textcolor{teal}{\CheckmarkBold} & \textcolor{purple}{\XSolidBrush} \\ 
ZESRec~\cite{ding2021zero} & \textcolor{teal}{\CheckmarkBold} & \textcolor{purple}{\XSolidBrush} & \textcolor{teal}{\CheckmarkBold} & \textcolor{purple}{\XSolidBrush} & \textcolor{teal}{\CheckmarkBold} \\ 
UniSRec (ours) & \textcolor{teal}{\CheckmarkBold} & \textcolor{teal}{\CheckmarkBold} & \textcolor{teal}{\CheckmarkBold} & \textcolor{teal}{\CheckmarkBold} & \textcolor{teal}{\CheckmarkBold} \\ \bottomrule
\end{tabular}
}
\end{table}
```

