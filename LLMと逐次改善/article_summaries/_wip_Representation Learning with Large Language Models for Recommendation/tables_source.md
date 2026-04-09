# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
  \centering
  \caption{Recommendation performance Imprvement of all backbone methods on different datasets in terms of Recall  and NDCG. The superscript * indicates the Imprvement is statistically significant where the p-value is less than $0.05$.}
  \vspace{-0.1in}
  \resizebox{\textwidth}{!}{
    \begin{tabular}{c|c|cccccc|cccccc|cccccc}
      \toprule
            \multicolumn{2}{c|}{Data} & \multicolumn{6}{c|}{Amazon-book} & \multicolumn{6}{c|}{Yelp} & \multicolumn{6}{c}{Steam} \\
        \midrule
            Backbone & Variants & R@5 & R@10 & R@20 & N@5 & N@10 & N@20 & R@5 & R@10 & R@20 & N@5 & N@10 & N@20 & R@5 & R@10 & R@20 & N@5 & N@10 & N@20\\
        \midrule
            \multicolumn{2}{c|}{Semantic Embeddings Only}
            & 0.0081 & 0.0125 & 0.0199 & 0.0072 & 0.0088 & 0.0112 & 0.0013 & 0.0022 & 0.0047 & 0.0014 & 0.0018 & 0.0026 & 0.0033 & 0.0062 & 0.0120 & 0.0031 & 0.0043 & 0.0064\\
        \midrule
            \multirow{4}{*}{GCCF}
            & Base & 0.0537 & 0.0872 & 0.1343 & 0.0537 & 0.0653 & 0.0807 & 0.0390 & 0.0652 & 0.1084 & 0.0451 & 0.0534 & 0.0680 & 0.0500 & 0.0826 & 0.1313 & 0.0556 & 0.0665 & 0.0830\\
            & \model-Con & \textbf{0.0561}* & \textbf{0.0899}* & \textbf{0.1395}* & \textbf{0.0562}* & \textbf{0.0679}* & \textbf{0.0842}* & \textbf{0.0409}* & \textbf{0.0685}* & \textbf{0.1144}* & \textbf{0.0474}* & \textbf{0.0562}* & \textbf{0.0719}* & \textbf{0.0538}* & \textbf{0.0883}* & \textbf{0.1398}* & \textbf{0.0597}* & \textbf{0.0713}* & \textbf{0.0888}*\\ 
            & \model-Gen & 0.0551* & 0.0891* & 0.1372* & 0.0559* & 0.0675* & 0.0832* & 0.0393 & 0.0654 & 0.1074 & 0.0454 & 0.0535 & 0.0678 & 0.0532* & 0.0874* & 0.1385* & 0.0588* & 0.0702* & 0.0875*\\
            & \textbf{Best Imprv.} & $\uparrow$4.28\% & $\uparrow$3.10\% & $\uparrow$3.87\% & $\uparrow$4.66\% & $\uparrow$3.98\% & $\uparrow$4.34\% & $\uparrow$4.87\% & $\uparrow$5.06\% & $\uparrow$5.54\% & $\uparrow$5.10\% & $\uparrow$5.24\% & $\uparrow$5.74\% & $\uparrow$7.60\% & $\uparrow$6.90\% & $\uparrow$6.47\% & $\uparrow$7.37\% & $\uparrow$7.22\% & $\uparrow$6.99\%\\
        \midrule
            \multirow{4}{*}{LightGCN}
            & Base & 0.0570 & 0.0915 & 0.1411 & 0.0574 & 0.0694 & 0.0856 & 0.0421 & 0.0706 & 0.1157 & 0.0491 & 0.0580 & 0.0733 & 0.0518 & 0.0852 & 0.1348 & 0.0575 & 0.0687 & 0.0855\\
            & \model-Con & \textbf{0.0608}* & \textbf{0.0969}* & \textbf{0.1483}* & \textbf{0.0606}* & \textbf{0.0734}* & \textbf{0.0903}* & \textbf{0.0445}* & \textbf{0.0754}* & \textbf{0.1230}* & \textbf{0.0518}* & \textbf{0.0614}* & \textbf{0.0776}* & 0.0548* & 0.0895* & 0.1421* & \textbf{0.0608}* & 0.0724* & 0.0902*\\ 
            & \model-Gen & 0.0596* & 0.0948* & 0.1446* & 0.0605* & 0.0724* & 0.0887* & 0.0435* & 0.0734* & 0.1209* & 0.0505 & 0.0600* & 0.0761* & \textbf{0.0550}* & \textbf{0.0907}* & \textbf{0.1433}* & 0.0607* & \textbf{0.0729}* & \textbf{0.0907}*\\
            & \textbf{Best Imprv.} & $\uparrow$6.67\% & $\uparrow$5.90\% & $\uparrow$5.10\% & $\uparrow$5.57\% & $\uparrow$5.76\% & $\uparrow$5.49\% & $\uparrow$5.70\% & $\uparrow$6.80\% & $\uparrow$6.31\% & $\uparrow$5.50\% & $\uparrow$5.86\% & $\uparrow$5.87\% & $\uparrow$6.18\% & $\uparrow$6.46\% & $\uparrow$6.31\% & $\uparrow$5.74\% & $\uparrow$6.11\% & $\uparrow$6.08\%\\
        \midrule
        \multirow{4}{*}{SGL}
            & Base & 0.0637 & 0.0994 & 0.1473 & 0.0632 & 0.0756 & 0.0913 & 0.0432 & 0.0722 & 0.1197 & 0.0501 & 0.0592 & 0.0753 & 0.0565 & 0.0919 & 0.1444 & 0.0618 & 0.0738 & 0.0917\\
            & \model-Con & \textbf{0.0655}* & \textbf{0.1017}* & 0.1528* & \textbf{0.0652}* & \textbf{0.0778}* & 0.0945* & 0.0452* & 0.0763* & 0.1248* & 0.0530* & 0.0626* & 0.0790* & \textbf{0.0589}* & \textbf{0.0956}* & \textbf{0.1489}* & \textbf{0.0645}* & \textbf{0.0768}* & \textbf{0.0950}*\\ 
            & \model-Gen & 0.0644 & 0.1015 & \textbf{0.1537}* & 0.0648* & 0.0777* & \textbf{0.0947}* & \textbf{0.0467}* & \textbf{0.0771}* & \textbf{0.1263}* & \textbf{0.0537}* & \textbf{0.0631}* & \textbf{0.0798}* & 0.0574* & 0.0940* & 0.1476* & 0.0629* & 0.0752* & 0.0934*\\
            & \textbf{Best Imprv.} & $\uparrow$2.83\% & $\uparrow$2.31\% & $\uparrow$4.34\% & $\uparrow$3.16\% & $\uparrow$2.91\% & $\uparrow$3.72\% & $\uparrow$8.10\% & $\uparrow$6.79\% & $\uparrow$5.51\% & $\uparrow$7.19\% & $\uparrow$6.59\% & $\uparrow$5.98\% & $\uparrow$5.20\% & $\uparrow$4.03\% & $\uparrow$3.12\% & $\uparrow$4.37\% & $\uparrow$4.07\% & $\uparrow$3.60\%\\
        \midrule
        \multirow{4}{*}{SimGCL}
            & Base & 0.0618 & 0.0992 & 0.1512 & 0.0619 & 0.0749 & 0.0919 & 0.0467 & 0.0772 & 0.1254 & 0.0546 & 0.0638 & 0.0801 & 0.0564 & 0.0918 & 0.1436 & 0.0618 & 0.0738 & 0.0915\\
            & \model-Con & \textbf{0.0633}* & \textbf{0.1011}* & \textbf{0.1552}* & \textbf{0.0633}* & \textbf{0.0765}* & \textbf{0.0942}* & \textbf{0.0470} & \textbf{0.0784}* & \textbf{0.1292}* & \textbf{0.0546} & \textbf{0.0642} & \textbf{0.0814}* & \textbf{0.0582}* & \textbf{0.0945}* & \textbf{0.1482}* & \textbf{0.0638}* & \textbf{0.0760}* & \textbf{0.0942}*\\ 
            & \model-Gen & 0.0617 & 0.0991 & 0.1524* & 0.0622 & 0.0752 & 0.0925* & 0.0464 & 0.0767 & 0.1267 & 0.0541 & 0.0634 & 0.0803 & 0.0572 & 0.0929 & 0.1456* & 0.0627* & 0.0747* & 0.0926*\\
            & \textbf{Best Imprv.} & $\uparrow$2.43\% & $\uparrow$1.92\% & $\uparrow$2.65\% & $\uparrow$2.26\% & $\uparrow$2.14\% & $\uparrow$2.50\% & $\uparrow$0.64\% & $\uparrow$1.55\% & $\uparrow$3.03\% & $-$ & $\uparrow$0.63\% & $\uparrow$1.62\% & $\uparrow$3.19\% & $\uparrow$2.94\% & $\uparrow$1.53\% & $\uparrow$3.24\% & $\uparrow$2.98\% & $\uparrow$2.95\%\\
        \midrule
            \multirow{4}{*}{DCCF}
            & Base & 0.0662 & 0.1019 & 0.1517 & 0.0658 & 0.0780 & 0.0943 & 0.0468 & 0.0778 & 0.1249 & 0.0543 & 0.0640 & 0.0800 & 0.0561 & 0.0915 & 0.1437 & 0.0618 & 0.0736 & 0.0914\\
            & \model-Con & 0.0665 & 0.1040* & \textbf{0.1563}* & 0.0668 & 0.0798* & 0.0968* & \textbf{0.0486}* & \textbf{0.0813}* & \textbf{0.1321}* & \textbf{0.0561}* & \textbf{0.0663}* & \textbf{0.0836}* & \textbf{0.0572}* & \textbf{0.0929}* & \textbf{0.1459}* & \textbf{0.0627}* & \textbf{0.0747}* & \textbf{0.0927}*\\ 
            & \model-Gen & \textbf{0.0666} & \textbf{0.1046}* & 0.1559* & \textbf{0.0670}* & \textbf{0.0801}* & \textbf{0.0969}* & 0.0475 & 0.0785 & 0.1281* & 0.0549 & 0.0646 & 0.0815 & 0.0570* & 0.0918 & 0.1430 & 0.0625 & 0.0741 & 0.0915\\
            & \textbf{Best Imprv.} & $\uparrow$0.60\% & $\uparrow$2.65\% & $\uparrow$3.03\% & $\uparrow$1.82\% & $\uparrow$2.69\% & $\uparrow$2.76\% & $\uparrow$3.85\% & $\uparrow$4.50\% & $\uparrow$5.76\% & $\uparrow$3.31\% & $\uparrow$3.59\% & $\uparrow$4.50\% & $\uparrow$2.14\% & $\uparrow$1.53\% & $\uparrow$1.53\% & $\uparrow$1.46\% & $\uparrow$1.49\% & $\uparrow$1.42\%\\
        \midrule
            \multirow{4}{*}{AutoCF}
            & Base & 0.0689 & 0.1055 & 0.1536 & \textbf{0.0705} & 0.0828 & 0.0984 & 0.0469 & 0.0789 & 0.1280 & 0.0547 & 0.0647 & 0.0813 & 0.0519 & 0.0853 & 0.1358 & 0.0572 & 0.0684 & 0.0855\\
            & \model-Con & \textbf{0.0695} & \textbf{0.1083}* & \textbf{0.1586}* & 0.0704 & \textbf{0.0837} & \textbf{0.1001}* & 0.0488* & 0.0814* & 0.1319* & 0.0562* & 0.0663* & 0.0835* & \textbf{0.0540}* & 0.0876* & 0.1372* & 0.0593* & 0.0704* & 0.0872*\\ 
            & \model-Gen & 0.0693 & 0.1069* & 0.1581* & 0.0701 & 0.0830 & 0.0996 & \textbf{0.0493}* & \textbf{0.0828}* & \textbf{0.1330}* & \textbf{0.0572}* & \textbf{0.0677}* & \textbf{0.0848}* & 0.0539* & \textbf{0.0888}* & \textbf{0.1410}* & \textbf{0.0593}* & \textbf{0.0710}* & \textbf{0.0886}*\\
            & \textbf{Best Imprv.} & $\uparrow$0.87\% & $\uparrow$2.65\% & $\uparrow$3.26\% & $\downarrow$0.14\% & $\uparrow$1.87\% & $\uparrow$1.73\% & $\uparrow$5.12\% & $\uparrow$4.94\% & $\uparrow$3.91\% & $\uparrow$4.57\% & $\uparrow$4.64\% & $\uparrow$4.31\% & $\uparrow$4.05\% & $\uparrow$4.10\% & $\uparrow$3.83\% & $\uparrow$3.67\% & $\uparrow$3.80\% & $\uparrow$3.63\%\\
      \bottomrule
      \end{tabular}
    }
  \label{tab:overall comparison}%
\end{table*}
```

## Table 2
```latex
\begin{table}[t]
    \centering
    \caption{Comparison with LLMs-enhanced Approaches.}
    \footnotesize
    \vspace{-0.1in}
    \begin{tabular}{c|c|cc|cc}
        \toprule
            \multicolumn{2}{c|}{Data} & \multicolumn{2}{c|}{Amazon-book} & \multicolumn{2}{c}{Yelp} \\
        \midrule
            \shortstack{Backb.} & Variants & R@20 & N@20 & R@20 & N@20 \\
            \midrule
                \multirow{4}{*}{\shortstack{Light-\\GCN}}
                & Base & 0.1411 & 0.0856 & 0.1157 & 0.0733\\
                & KAR & $0.1416^{+0.3\%}$ & $0.0863^{{+0.8\%}}$ & $0.1194^{{+3.2\%}}$ & $0.0756^{{+3.1\%}}$\\
                & \model-Con & $0.1483^{{+\underline{\textbf{5.1\%}}}}$ & $0.0903^{{+\underline{\textbf{5.5\%}}}}$ & $0.1230^{{+\underline{\textbf{6.3\%}}}}$ & $0.0776^{{+\underline{\textbf{5.9\%}}}}$\\ 
                & \model-Gen & $0.1446^{{+2.5\%}}$ & $0.0887^{{+3.6\%}}$ & $0.1209^{{+4.5\%}}$ & $0.0761^{{+3.8\%}}$\\
            \midrule
                \multirow{4}{*}{\shortstack{SGL}}
                & Base & 0.1473 & 0.0913 & 0.1197 & 0.0753\\
                & KAR & $0.1436^{{-2.5\%}}$ & $0.0875^{{-4.2\%}}$ & $0.1208^{{+0.9\%}}$ & $0.0761^{{+1.1\%}}$\\
                & \model-Con & $0.1528^{{+3.7\%}}$ & $0.0945^{{+3.5\%}}$ & $0.1248^{{+4.3\%}}$ & $0.0790^{{+4.9\%}}$\\ 
                & \model-Gen & $0.1537^{{+\underline{\textbf{4.3\%}}}}$ & $0.0947^{{+\underline{\textbf{3.7\%}}}}$ & $0.1263^{{+\underline{\textbf{5.5\%}}}}$ & $0.0798^{{+\underline{\textbf{6.0\%}}}}$\\
        \bottomrule
    \end{tabular}
    \vspace{-0.15in}             
    \label{tab:comparison kar}
\end{table}
```

## Table 3
```latex
\begin{table}[t]
    \centering
    \caption{Performance comparison  with different initialized parameters from various pre-training methods on the Yelp.}
    \footnotesize
    \vspace{-0.1in}
    \begin{tabular}{c|ccc|ccc}
        \toprule
            Metric & \multicolumn{3}{c|}{Recall} & \multicolumn{3}{c}{NDCG} \\
        \midrule
            Pretrained Params & @5 & @10 & @20 & @5 & @10 & @20 \\
        \midrule
            None & 0.0274 & 0.0462 & 0.0820 & 0.0203 & 0.0270 & 0.0375 \\
            Base & 0.0304 & 0.0557 & 0.0971 & 0.0229 & 0.0319 & 0.0439 \\
            \model-Con & 0.0359 & 0.0613 & 0.1034 & 0.0261 & 0.0352 & 0.0475 \\
            \model-Gen & \textbf{0.0362} & \textbf{0.0612} & \textbf{0.1068} & \textbf{0.0263} & \textbf{0.0353} & \textbf{0.0484} \\
        \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \label{tab:pretrain}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
    \centering
    \caption{\model's efficiency with various recommenders.}
    \vspace{-0.1in}
    \footnotesize
    \vspace{-0.1in}
    \begin{tabular}{c|cccccc}
        \midrule
            Ama-Variants & GCCF & LightGCN & SGL & SimGCL & DCCF & AutoCF \\
        \midrule
            Base & 0.88s & 1.01s & 2.18s & 2.62s & 2.26s & 2.73s\\
            \model-Con & 1.95s & 1.94s & 2.58s & 3.02s & 2.49s & 2.96s\\
            \model-Gen & 1.72s & 1.76s & 2.36s & 2.69s & 2.29s & 2.96s\\
        \midrule
            Yelp-Variants & GCCF & LightGCN & SGL & SimGCL & DCCF & AutoCF \\
        \midrule
            Base & 1.11s & 1.26s & 2.80s & 3.35s & 3.02s & 3.96s\\
            \model-Con & 2.39s & 2.57s & 3.27s & 3.95s & 3.42s & 4.41s\\
            \model-Gen & 2.03s & 2.12s & 3.20s & 3.50s & 3.24s & 4.39s\\
        \midrule
            Steam-Variants & GCCF & LightGCN & SGL & SimGCL & DCCF & AutoCF \\
        \midrule
            Base & 2.05s & 2.27s & 5.42s & 6.47s & 9.31s & 8.44s\\
            \model-Con & 4.32s & 4.67s & 6.77s & 7.88s & 10.18s & 10.06s\\
            \model-Gen & 3.33s & 3.81s & 6.10s & 6.89s & 9.57s & 9.89s\\
        \bottomrule
    \end{tabular}
    \vspace{-0.2in}
    \label{tab:time}
\end{table}
```

## Table 5
```latex
\begin{table}
    \centering
    \small
    %\footnotesize
    %\scriptsize
    \caption{Statistics of the experimental datasets.}
    \vspace{-0.15in}
    \begin{tabular}{ccccc}
        \toprule
        Dataset & \#Users & \#Items & \#Interactions & Density\\
        \midrule
        Amazon-book & 11,000 & 9,332 & 120,464 & 1.2$e^{-3}$\\
        Yelp & 11,091 & 11,010 & 166,620 & 1.4$e^{-3}$\\
        Steam & 23,310 & 5,237 & 316,190 & 2.6$e^{-3}$\\
        \bottomrule
    \end{tabular}
    \label{tab:data statistics}
\end{table}
```

