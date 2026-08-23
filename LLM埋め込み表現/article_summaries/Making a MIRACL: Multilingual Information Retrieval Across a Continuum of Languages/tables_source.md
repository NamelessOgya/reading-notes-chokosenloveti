# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[]
\resizebox{0.6\textwidth}{!}{
\begin{tabular}{lccccccc}
\toprule
\multirow{2}{*}{\textbf{Language}} & \multirow{2}{*}{\textbf{ISO}}  & \multicolumn{3}{c}{\textbf{nDCG@10}} & \multicolumn{3}{c}{\textbf{Recall@100}} \\
& & \textbf{BM25} & \textbf{mDPR} & \textbf{Hybrid} & \textbf{BM25} & \textbf{mDPR} & \textbf{Hybrid} \\
\cmidrule(lr){1-2} \cmidrule(lr){3-5} \cmidrule(lr){6-8} 
Arabic & \Ar & 0.481 & 0.499 & 0.673 & 0.889 & 0.841 & 0.941 \\
Bengali & \Bn & 0.508 & 0.443 & 0.654 & 0.909 & 0.819 & 0.932 \\
English & \En & 0.351 & 0.394 & 0.549 & 0.819 & 0.768 & 0.882 \\
Spanish & \Es & 0.319 & 0.478 & 0.641 & 0.702 & 0.864 & 0.948 \\
Persian & \Fa & 0.333 & 0.480 & 0.594 & 0.731 & 0.898 & 0.937 \\
Finnish & \Fi & 0.551 & 0.472 & 0.672 & 0.891 & 0.788 & 0.895 \\
French & \Fr & 0.183 & 0.435 & 0.523 & 0.653 & 0.915 & 0.965 \\
Hindi & \Hi & 0.458 & 0.383 & 0.616 & 0.868 & 0.776 & 0.912 \\
Indonesian & \Id & 0.449 & 0.272 & 0.443 & 0.904 & 0.573 & 0.768 \\
Japanese & \Ja & 0.369 & 0.439 & 0.576 & 0.805 & 0.825 & 0.904 \\
Korean & \Ko & 0.419 & 0.419 & 0.609 & 0.783 & 0.737 & 0.900 \\
Russian & \Ru & 0.334 & 0.407 & 0.532 & 0.661 & 0.797 & 0.874 \\
Swahili & \Sw & 0.383 & 0.299 & 0.446 & 0.701 & 0.616 & 0.725 \\
Telugu & \Te & 0.494 & 0.356 & 0.602 & 0.831 & 0.762 & 0.857 \\
Thai & \Th & 0.484 & 0.358 & 0.599 & 0.887 & 0.678 & 0.823 \\
Chinese & \Zh & 0.180 & 0.512 & 0.526 & 0.560 & 0.944 & 0.959 \\
\cmidrule(lr){1-2} \cmidrule(lr){3-5} \cmidrule(lr){6-8} 
Average & & 0.393 & 0.415 & 0.578 & 0.787 & 0.788 & 0.889 \\
\bottomrule
\end{tabular}
}
\vspace{0.2cm}
\caption{Baseline results on the development set of \miracl:\ BM25 uses the implementation in Anserini with default parameters and language-specific analyzers;
mDPR is fine-tuned on the MS MARCO Passage dataset and applied to each language in a zero-shot manner;
Hybrid combines BM25 and mDPR scores.
}
\label{tab:baselines}
\end{table*}
```

## Table 2
```latex
\begin{table*}[]
    \resizebox{1.0\textwidth}{!}{
    \begin{tabular}{lcrrrrrrrrrrc}
    \toprule
    \multirow{2}{*}{\textbf{Language}} & \multirow{2}{*}{\textbf{ISO}} & \multicolumn{2}{c}{\textbf{Train}} & \multicolumn{2}{c}{\textbf{Dev}} & \multicolumn{2}{c}{\textbf{Test-A}} & \multicolumn{2}{c}{\textbf{Test-B}} & \multicolumn{1}{l}{\multirow{2}{*}{\bf \# Passages}} & \multicolumn{1}{l}{\multirow{2}{*}{\bf \# Articles}} & \multirow{2}{*}{\textbf{\makecell{In \\ \mrtydi?}}} \\
    & & \multicolumn{1}{r}{\textbf{\# Q}} & \multicolumn{1}{r}{\textbf{\# J}} & \multicolumn{1}{r}{\textbf{\# Q}} & \multicolumn{1}{r}{\textbf{\# J}} & \multicolumn{1}{r}{\textbf{\# Q}} & \multicolumn{1}{r}{\textbf{\# J}} & \multicolumn{1}{r}{\textbf{\# Q}} & \multicolumn{1}{r}{\textbf{\# J}} & \multicolumn{1}{r}{} & \multicolumn{1}{r}{} \\
     \cmidrule(lr){1-2} \cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10} \cmidrule(lr){11-12} \cmidrule(lr){13-13}
Arabic & {\Ar} & 3,495 & 25,382 & 2,896 & 29,197 & 936 & 9,325 & 1,405 & 14,036 & 2,061,414 & 656,982 & \tick \\
Bengali & {\Bn} & 1,631 & 16,754 & 411 & 4,206 & 102 & 1,037 & 1,130 & 11,286 & 297,265 & 63,762 & \tick \\
English & {\En} & 2,863 & 29,416 & 799 & 8,350 & 734 & 5,617 & 1,790 & 18,241 & 32,893,221 & 5,758,285 & \tick \\
Spanish & {\Es} & 2,162 & 21,531 & 648 & 6,443 & -- & -- & 1,515 & 15,074 & 10,373,953 & 1,669,181 & \cross \\
Persian & {\Fa} & 2,107 & 21,844 & 632 & 6,571 & -- & -- & 1,476 & 15,313 & 2,207,172 & 857,827 & \cross \\
Finnish & {\Fi} & 2,897 & 20,350 & 1,271 & 12,008 & 1,060 & 10,586 & 711 & 7,100 & 1,883,509 & 447,815 & \tick \\
French & {\Fr} & 1,143 & 11,426 & 343 & 3,429 & -- & -- & 801 & 8,008 & 14,636,953 & 2,325,608 & \cross\\
Hindi & {\Hi} & 1,169 & 11,668 & 350 & 3,494 & -- & -- & 819 & 8,169 & 506,264 & 148,107 & \cross \\
Indonesian & {\Id} & 4,071 & 41,358 & 960 & 9,668 & 731 & 7,430 & 611 & 6,098 & 1,446,315 & 446,330 & \tick \\
Japanese & {\Ja} & 3,477 & 34,387 & 860 & 8,354 & 650 & 6,922 & 1,141 & 11,410 & 6,953,614 & 1,133,444 & \tick \\
Korean & {\Ko} & 868 & 12,767 & 213 & 3,057 & 263 & 3,855 & 1,417 & 14,161 & 1,486,752 & 437,373 & \tick \\
Russian & {\Ru} & 4,683 & 33,921 & 1,252 & 13,100 & 911 & 8,777 & 718 & 7,174 & 9,543,918 & 1,476,045 & \tick \\
Swahili & {\Sw} & 1,901 & 9,359 & 482 & 5,092 & 638 & 6,615 & 465 & 4,620 & 131,924 & 47,793 & \tick \\
Telugu & {\Te} & 3,452 & 18,608 & 828 & 1,606 & 594 & 5,948 & 793 & 7,920 & 518,079 & 66,353 & \tick \\
Thai & {\Th} & 2,972 & 21,293 & 733 & 7,573 & 992 & 10,432 & 650 & 6,493 & 542,166 & 128,179 & \tick \\
Chinese & {\Zh} & 1,312 & 13,113 & 393 & 3,928 & -- & -- & 920 & 9,196 & 4,934,368 & 1,246,389 & \cross \\
     \cmidrule(lr){1-2} \cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10} \cmidrule(lr){11-12} \cmidrule(lr){13-13}
Total & & 40,203 & 343,177 & 13,071 & 126,076 & 7,611 & 76,544 & 16,362 & 164,299 & 90,416,887 & 16,909,473 \\
    \midrule
    \multicolumn{2}{l}{Surprise Language 1} & ? & ? & ?& ?& ?& ?& ?& ?& ? & ? & \cross \\
    \multicolumn{2}{l}{Surprise Language 2} & ? & ? & ?& ?& ?& ?& ?& ?& ? & ? & \cross\\
    \bottomrule
    \end{tabular}
    }
   \vspace{0.2cm}
   \caption{
        Descriptive statistics for each language, split combination in \miracl:\ \#~Q denotes the number of queries; \#~J denotes the number of judgments (both relevant and non-relevant).
        Statistics of each Wikipedia corpus are also provided:\ \#~Passages denotes the number of passages in each language;
        \#~Articles denotes the number of Wikipedia articles from which the passages were drawn.
        The final column indicates if the language is contained in \mrtydi.
        \miracl encompasses 18 languages in total:\ 16 of which are known, with 2 ``surprise'' languages whose identities will be revealed in the future.
    }
    \label{tab:miracl-stats} 
    \end{table*}
```

