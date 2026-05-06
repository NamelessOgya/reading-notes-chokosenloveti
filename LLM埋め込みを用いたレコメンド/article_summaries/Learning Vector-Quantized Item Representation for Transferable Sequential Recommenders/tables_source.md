# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[!t] %
	\caption{Statistics of the preprocessed datasets. ``Avg.~$n$'' denotes the average length of item sequences. ``Avg.~$c$'' denotes the average number of words in item text.
	}
	\label{tab:dataset}
	\resizebox{\columnwidth}{!}{
	\begin{tabular}{l *{5}{r}}
		\toprule
		\textbf{Datasets} & \textbf{\#Users} & \textbf{\#Items} & \textbf{\#Inters.} & \textbf{Avg. $n$} & \textbf{Avg. $c$}\\
		\midrule
		\textbf{Pre-trained} & 1,361,408 & 446,975 & 14,029,229 & 13.51 & 139.34 \\
		\midrule
		\textbf{Scientific}  &  8,442 &  4,385 &  59,427 & 7.04 & 182.87 \\
		\textbf{Pantry}      & 13,101 &  4,898 & 126,962 & 9.69 & 83.17 \\
		\textbf{Instruments} & 24,962 &  9,964 & 208,926 & 8.37 & 165.18 \\
		\textbf{Arts}        & 45,486 & 21,019 & 395,150 & 8.69 & 155.57 \\
		\textbf{Office}      & 87,436 & 25,986 & 684,837 & 7.84 & 193.22 \\
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
\caption{Performance comparison of different models. The best and the second-best 
performance is
denoted in bold and underlined fonts, respectively. ``R@K'' is short for ``Recall@K'' and ``N@K'' is short for ``NDCG@K'', respectively. The features used for item representations of each compared model have been listed, whether ID, text (T), or both (ID+T).}
\label{tab:exp-main}
\resizebox{2.1\columnwidth}{!}{
\begin{tabular}{@{}cccccccccccc@{}}
\toprule
\textbf{Scenario} & \textbf{Dataset} & \textbf{Metric} & \textbf{SASRec} \textsubscript{ID} & \textbf{BERT4Rec} \textsubscript{ID} & \textbf{FDSA} \textsubscript{ID+T} & \textbf{S$^3$-Rec} \textsubscript{ID+T} & \textbf{RecGURU} \textsubscript{ID} & \textbf{SASRec} \textsubscript{T} & \textbf{ZESRec} \textsubscript{T} & \textbf{UniSRec} \textsubscript{T} & \textbf{VQ-Rec} \textsubscript{T} \\\midrule \midrule
\multirow{20}{*}{\shortstack{Cross-\\Domain}} &
\multirow{4}{*}{Scientific} &
     R@10 & 0.1080 & 0.0488 & 0.0899 & 0.0525 & 0.1023 & 0.0994 & 0.0851 & \second{0.1188} & \first{0.1211} \\
 & & N@10   & 0.0553 & 0.0243 & 0.0580 & 0.0275 & 0.0572 & 0.0561 & 0.0475 & \second{0.0641} & \first{0.0643} \\
 & & R@50 & 0.2042 & 0.1185 & 0.1732 & 0.1418 & 0.2022 & 0.2162 & 0.1746 & \first{0.2394} & \second{0.2369} \\
 & & N@50   & 0.0760 & 0.0393 & 0.0759 & 0.0468 & 0.0786 & 0.0815 & 0.0670 & \first{0.0903} & \second{0.0897} \\
\cmidrule(l){2-12}
 & \multirow{4}{*}{Pantry} &
     R@10 & 0.0501 & 0.0308 & 0.0395 & 0.0444 & 0.0469 & 0.0585 & 0.0454 & \second{0.0636} & \first{0.0660} \\
 & & N@10   & 0.0218 & 0.0152 & 0.0209 & 0.0214 & 0.0209 & 0.0285 & 0.0230 & \first{0.0306} & \second{0.0293} \\
 & & R@50 & 0.1322 & 0.1030 & 0.1151 & 0.1315 & 0.1269 & 0.1647 & 0.1141 & \second{0.1658} & \first{0.1753} \\
 & & N@50   & 0.0394 & 0.0305 & 0.0370 & 0.0400 & 0.0379 & 0.0523 & 0.0378 & \first{0.0527} & \first{0.0527} \\
 \cmidrule(l){2-12}
 & \multirow{4}{*}{Instruments} &
     R@10 & 0.1118 & 0.0813 & 0.1070 & 0.1056 & 0.1113 & 0.1127 & 0.0783 & \second{0.1189} & \first{0.1222} \\
 & & N@10   & 0.0612 & 0.0620 & \first{0.0796} & 0.0713 & 0.0681 & 0.0661 & 0.0497 & 0.0680 & \second{0.0758} \\
 & & R@50 & 0.2106 & 0.1454 & 0.1890 & 0.1927 & 0.2068 & 0.2104 & 0.1387 & \second{0.2255} & \first{0.2343} \\
 & & N@50   & 0.0826 & 0.0756 & \second{0.0972} & 0.0901 & 0.0887 & 0.0873 & 0.0627 & 0.0912 & \first{0.1002} \\
 \cmidrule(l){2-12}
 & \multirow{4}{*}{Arts} &
     R@10 & \second{0.1108} & 0.0722 & 0.1002 & 0.1003 & 0.1084 & 0.0977 & 0.0664 & 0.1066 & \first{0.1189} \\
 & & N@10   & 0.0587 & 0.0479 & \first{0.0714} & 0.0601 & 0.0651 & 0.0562 & 0.0375 & 0.0586 & \second{0.0703} \\
 & & R@50 & 0.2030 & 0.1367 & 0.1779 & 0.1888 & 0.1979 & 0.1916 & 0.1323 & \second{0.2049} & \first{0.2249} \\
 & & N@50   & 0.0788 & 0.0619 & \second{0.0883} & 0.0793 & 0.0845 & 0.0766 & 0.0518 & 0.0799 & \first{0.0935} \\
 \cmidrule(l){2-12}
 & \multirow{4}{*}{Office} &
     R@10 & 0.1056 & 0.0825 & 0.1118 & 0.1030 & \second{0.1145} & 0.0929 & 0.0641 & 0.1013 & \first{0.1236} \\
 & & N@10   & 0.0710 & 0.0634 & \first{0.0868} & 0.0653 & 0.0768 & 0.0582 & 0.0391 & 0.0619 & \second{0.0814} \\
 & & R@50 & 0.1627 & 0.1227 & 0.1665 & 0.1613 & \second{0.1757} & 0.1580 & 0.1113 & 0.1702 & \first{0.1957} \\
 & & N@50   & 0.0835 & 0.0721 & \first{0.0987} & 0.0780 & 0.0901 & 0.0723 & 0.0493 & 0.0769 & \second{0.0972} \\
 \midrule
\multirow{4}{*}{\shortstack{Cross-\\Platform}} &
\multirow{4}{*}{\shortstack{Online\\ Retail}} &
     R@10 & 0.1460 & 0.1349 & \second{0.1490} & 0.1418 & 0.1467 & 0.1380 & 0.1103 & 0.1449 & \first{0.1557} \\
 & & N@10   & 0.0675 & 0.0653 & \second{0.0719} & 0.0654 & 0.0658 & 0.0672 & 0.0535 & 0.0677 & \first{0.0730} \\
 & & R@50 & \second{0.3872} & 0.3540 & 0.3802 & 0.3702 & 0.3885 & 0.3516 & 0.2750 & 0.3604 & \first{0.3994} \\
 & & N@50   & 0.1201 & 0.1131 & \second{0.1223} & 0.1154 & 0.1188 & 0.1137 & 0.0896 & 0.1149 & \first{0.1263} \\
 \bottomrule
\end{tabular}
}
\end{table*}
```

## Table 3
```latex
\begin{table*}[t]
\centering
\caption{Ablation analysis on three downstream datasets.
The best and the second-best performance is denoted in bold and underlined fonts, respectively.}
\label{tab:exp-ablation}
\resizebox{2.1\columnwidth}{!}{
\begin{tabular}{@{}lcccccccccccc@{}}
\toprule
\multirow{2}{*}{\textbf{Variants}} & \multicolumn{4}{c}{\textbf{Scientific}} & \multicolumn{4}{c}{\textbf{Office}} & \multicolumn{4}{c}{\textbf{Online Retail}} \\
\cmidrule(lr){2-5} \cmidrule(lr){6-9} \cmidrule(lr){10-13}
 & R@10 & N@10 & R@50 & N@50 & R@10 & N@10 & R@50 & N@50 & R@10 & N@10 & R@50 & N@50 \\
\midrule
(0) VQ-Rec                        & \first{0.1211} & \first{0.0643} & \first{0.2369} & \first{0.0897} & \second{0.1236} & 0.0814 & \first{0.1957} & \second{0.0972} & \second{0.1557} & \second{0.0730} & \first{0.3994} & \second{0.1263} \\
\cmidrule(lr){1-1}
(1) \ \ $w/o$ Pre-training        & 0.1104 & 0.0593 & 0.2238 & 0.0839 & 0.1108 & 0.0666 & 0.1804 & 0.0818 & 0.1535 & 0.0717 & 0.3953 & 0.1244 \\
(2) \ \ $w/o$ Semi-synthetic NS   & \second{0.1194} & \second{0.0631} & \second{0.2358} & \second{0.0886} & 0.1227 & 0.0809 & 0.1951 & 0.0968 & 0.1529 & 0.0702 & \second{0.3938} & 0.1230 \\
\cmidrule(lr){1-1}
(3) \ \ $w/o$ Fine-tuning         & 0.0640 & 0.0361 & 0.0909 & 0.0421 & 0.0261 & 0.0150 & 0.0373 & 0.0174 & 0.0197 & 0.0095 & 0.0419 & 0.0142 \\
(4) \ \ Reuse PQ Index Set        & 0.1168 & 0.0618 & 0.2267 & 0.0859 & 0.1182 & 0.0773 & 0.1869 & 0.0922 & 0.1521 & 0.0707 & 0.3917 & 0.1232 \\
(5) \ \ $w/o$ Code-Emb Alignment  & 0.1183 & 0.0612 & 0.2355 & 0.0867 & \first{0.1242} & \second{0.0824} & \second{0.1956} & \first{0.0980} & 0.1515 & 0.0695 & 0.3924 & 0.1224 \\
(6) \ \ Random Code               & 0.0905 & 0.0494 & 0.1769 & 0.0683 & 0.1134 & \first{0.0837} & 0.1698 & 0.0960 & \first{0.1589} & \first{0.0769} & 0.3933 & \first{0.1282} \\
\bottomrule
\end{tabular}
}
\end{table*}
```

