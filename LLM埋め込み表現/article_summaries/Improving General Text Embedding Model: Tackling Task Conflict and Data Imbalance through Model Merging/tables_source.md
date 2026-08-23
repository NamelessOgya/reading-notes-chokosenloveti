# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
  \centering
  \small
  \caption{The number of instances in training datasets.}
  \begin{tabular}{c|c|cccc}
    \toprule
          & \textbf{STS}   & \multicolumn{4}{c}{\textbf{Retrieval}} \\
    \midrule
    \multirow{2}[2]{*}{\textbf{en}} & ALLNLI & FEVER & HotpotQA & MS MARCO & NQ \\
          & 271,612 & 123,140 & 97,825 & 491,007 & 57,110 \\
    \midrule
    \multirow{2}[2]{*}{\textbf{zh}} & SimCLUE & DuReader & Ecom  & Medical & Video \\
          & 802,291 & 86,395 & 99,763 & 97,509 & 99,719 \\
    \bottomrule
  \end{tabular}%
  \label{tab:data_amount_sts_retrieval}%
\end{table}
```

## Table 2
```latex
\begin{table}
  \centering
  \caption{Average performance (\%) on all STS and Retrieval tasks. ``JT'' represents results from joint training, ``SP'' represents results from Self Positioning, and other model merging methods report the best results after hyperparameter tuning.}
  \small
    \begin{tabular}{c|c|c|ccccc|c}
    \toprule
          & \makecell{\textbf{JT}} & \makecell{\textbf{Merging}\\ \textbf{Pipeline}} & \makecell{\textbf{Fi-}\\\textbf{sher}} & \makecell{\textbf{Reg}\\ \textbf{Mean}} & \textbf{TIES}  & \makecell{\textbf{Ave-}\\\textbf{rage}} & \makecell{\textbf{SL-}\\\textbf{ERP}} & \makecell{\textbf{SP}} \\
    \midrule
    \multirow{2}[2]{*}{\textbf{en}} & \multirow{2}[2]{*}{60.1} & Separate   & \textbf{60.5} & 60.4  & 60.2  & \textbf{60.5} & \textbf{60.5} & \textbf{60.5} \\
          &       & Iterative  & \textbf{60.3}    & 60.2 & 59.9  & 60.2 & 60.2 & 60.1 \\
    \midrule
    \multirow{2}[2]{*}{\textbf{zh}} & \multirow{2}[2]{*}{51.2} & Separate   & 51.7  & 52.1  & 51    & 51.8  & \textbf{52.9} & \textbf{52.9} \\
          &       & Iterative  & 52.6  & 52.6  & 51.9  & 52.5  & 52.6 & \textbf{52.9} \\
    \bottomrule
    \end{tabular}%
  \label{tab:performance_sts_retrieval}%
\end{table}
```

## Table 3
```latex
\begin{table}
  \centering
  \caption{Results on MTEB~\cite{muennighoff_mteb_2023} for Separate Merging(Section ~\ref{sec:applications_separate_merging}) and Iterative Merging(Sectuion ~\ref{sec:applications_iterative_merging}). Retri., Pair., Class., Sum. refer to retrieval, pair classification, classification, and summarization, respectively.  All models utilize the T5-large encoder~\cite{raffel_exploring_2020} as their backbone. Results of GTR and Instructor are sourced from ~\cite{su_one_2023}. % Results from Separate Merging (Section~\ref{sec:applications_separate_merging}) are categorized under ``2 clusters'', ``3 clusters'', and ``4 clusters''. 
  For methods requiring sample data (Fisher, RegMean, and our Self Positioning), the first result in each group uses training data, while the second uses alternative data sources. }
  \resizebox{1.0\linewidth}{!}{
    \begin{tabular}{l|cc|cc|cc|cc|cc|cc|cc|cc}
    \toprule
          & \multicolumn{2}{c|}{\textbf{Avg. (56)}} & \multicolumn{2}{c|}{\textbf{Class. (12)}} & \multicolumn{2}{c|}{\textbf{Cluster. (11)}} & \multicolumn{2}{c|}{\textbf{Pair. (3)}} & \multicolumn{2}{c|}{\textbf{ReRank. (4)}} & \multicolumn{2}{c|}{\textbf{Retri. (15)}} & \multicolumn{2}{c|}{\textbf{STS (10)}} & \multicolumn{2}{c}{\textbf{Sum. (1)}} \\
    \midrule
    \textbf{GTR~\cite{ni_large_2022}} & \multicolumn{2}{c|}{58.3} & \multicolumn{2}{c|}{67.1} & \multicolumn{2}{c|}{41.6} & \multicolumn{2}{c|}{85.3} & \multicolumn{2}{c|}{55.4} & \multicolumn{2}{c|}{47.4} & \multicolumn{2}{c|}{78.2} & \multicolumn{2}{c}{29.5} \\
    \textbf{Instructor~\cite{su_one_2023}} & \multicolumn{2}{c|}{61.6} & \multicolumn{2}{c|}{73.9} & \multicolumn{2}{c|}{45.3} & \multicolumn{2}{c|}{85.9} & \multicolumn{2}{c|}{57.5} & \multicolumn{2}{c|}{47.6} & \multicolumn{2}{c|}{83.2} & \multicolumn{2}{c}{31.8} \\
        \midrule
    \multicolumn{17}{c}{\textit{Separate Merging}} \\
    \midrule
    \textbf{TIES} & \multicolumn{2}{c|}{62.2 } & \multicolumn{2}{c|}{72.5 } & \multicolumn{2}{c|}{45.4 } & \multicolumn{2}{c|}{86.3 } & \multicolumn{2}{c|}{57.7 } & \multicolumn{2}{c|}{51.1 } & \multicolumn{2}{c|}{82.8 } & \multicolumn{2}{c}{31.2 } \\
    \textbf{Fisher} & 62.1  & 61.7  & 72.3  & 72.2  & 45.2  & 44.6  & 86.4  & 86.7  & 57.5  & 56.9  & 51.0  & 50.2  & 82.7  & 82.4  & 30.9  & 31.6  \\
    \textbf{RegMean} & 61.5  & 61.4  & 71.9  & 72.0  & 44.7  & 44.5  & 86.6  & 86.7  & 56.9  & 56.8  & 49.7  & 49.6  & 82.4  & 82.4  & 31.6  & 31.5  \\
    \textbf{Self Positioning} & 62.3  & 62.2  & 72.6  & 72.6  & 45.6  & 45.4  & 86.0  & 86.3  & 58.0  & 57.7  & 51.0  & 51.1  & 82.9  & 82.7  & 31.4  & 31.3  \\
    \midrule
    \multicolumn{17}{c}{\textit{Iterative Merging (with extra classification training data) }} \\
    \midrule
    \textbf{TIES} & \multicolumn{2}{c|}{62.8 } & \multicolumn{2}{c|}{78.3 } & \multicolumn{2}{c|}{44.8 } & \multicolumn{2}{c|}{85.1 } & \multicolumn{2}{c|}{57.7 } & \multicolumn{2}{c|}{49.6 } & \multicolumn{2}{c|}{82.2 } & \multicolumn{2}{c}{31.0 } \\
    \textbf{Fisher} & \multicolumn{2}{c|}{62.5 } & \multicolumn{2}{c|}{79.2 } & \multicolumn{2}{c|}{44.5 } & \multicolumn{2}{c|}{84.5 } & \multicolumn{2}{c|}{57.6 } & \multicolumn{2}{c|}{48.7 } & \multicolumn{2}{c|}{81.7 } & \multicolumn{2}{c}{29.9 } \\
    \textbf{RegMean} & \multicolumn{2}{c|}{62.7 } & \multicolumn{2}{c|}{78.8 } & \multicolumn{2}{c|}{44.8 } & \multicolumn{2}{c|}{84.7 } & \multicolumn{2}{c|}{57.4 } & \multicolumn{2}{c|}{49.2 } & \multicolumn{2}{c|}{82.1 } & \multicolumn{2}{c}{30.4 } \\
    \textbf{Self Positioning} & \multicolumn{2}{c|}{63.0 } & \multicolumn{2}{c|}{79.1 } & \multicolumn{2}{c|}{44.6 } & \multicolumn{2}{c|}{85.3 } & \multicolumn{2}{c|}{57.6 } & \multicolumn{2}{c|}{49.9 } & \multicolumn{2}{c|}{82.2 } & \multicolumn{2}{c}{30.5 } \\
    \bottomrule
    \end{tabular}}
  \label{tab:results_mteb}%
\end{table}
```

## Table 4
```latex
\begin{table}
  \centering
  \caption{Statistics for the clustering results of 330 tasks.}
    \begin{tabular}{c|ll}
    \toprule
          & \multicolumn{1}{c}{\textbf{Task Count}} & \multicolumn{1}{c}{\textbf{Instance Count}} \\
    \midrule
    \textbf{2 clusters} & 30/300 & 1,255,000/18,000 \\
    \textbf{3 clusters} & 30/121/179 & 1,255,000/72,600/107,400 \\
    \textbf{4 clusters} & 30/92/97/111 & 1,255,000/55,200/58,200/66,600 \\
    \bottomrule
    \end{tabular}%
  \label{tab:statistics_clustering}%
\end{table}
```

## Table 5
```latex
\begin{table*}
  \centering
  \caption{Results on MTEB~\cite{muennighoff_mteb_2023}. Retri., Pair., Class., Sum. refer to retrieval, pair classification, classification, and summarization, respectively.  All models utilize the T5-large encoder~\cite{raffel_exploring_2020} as their backbone. Results of GTR and Instructor are sourced from ~\cite{su_one_2023}. Results from Separate Merging (Section~\ref{sec:applications_separate_merging}) are categorized under ``2 clusters'', ``3 clusters'', and ``4 clusters''. 
  For methods requiring sample data (Fisher, RegMean, and our Self Positioning), the first result in each group uses training data, while the second uses alternative data sources. }
  \resizebox{1.0\linewidth}{!}{
    \begin{tabular}{l|cc|cc|cc|cc|cc|cc|cc|cc}
    \toprule
          & \multicolumn{2}{c|}{\textbf{Avg. (56)}} & \multicolumn{2}{c|}{\textbf{Class. (12)}} & \multicolumn{2}{c|}{\textbf{Cluster. (11)}} & \multicolumn{2}{c|}{\textbf{Pair. (3)}} & \multicolumn{2}{c|}{\textbf{ReRank. (4)}} & \multicolumn{2}{c|}{\textbf{Retri. (15)}} & \multicolumn{2}{c|}{\textbf{STS (10)}} & \multicolumn{2}{c}{\textbf{Sum. (1)}} \\
    \midrule
    \textbf{GTR~\cite{ni_large_2022}} & \multicolumn{2}{c|}{58.3} & \multicolumn{2}{c|}{67.1} & \multicolumn{2}{c|}{41.6} & \multicolumn{2}{c|}{85.3} & \multicolumn{2}{c|}{55.4} & \multicolumn{2}{c|}{47.4} & \multicolumn{2}{c|}{78.2} & \multicolumn{2}{c}{29.5} \\
    \textbf{Instructor~\cite{su_one_2023}} & \multicolumn{2}{c|}{61.6} & \multicolumn{2}{c|}{73.9} & \multicolumn{2}{c|}{45.3} & \multicolumn{2}{c|}{85.9} & \multicolumn{2}{c|}{57.5} & \multicolumn{2}{c|}{47.6} & \multicolumn{2}{c|}{83.2} & \multicolumn{2}{c}{31.8} \\
    \midrule
    \multicolumn{17}{c}{\textit{2 clusters}} \\
    \midrule
    \textbf{TIES} & \multicolumn{2}{c|}{62.3 } & \multicolumn{2}{c|}{72.8 } & \multicolumn{2}{c|}{45.7 } & \multicolumn{2}{c|}{86.2 } & \multicolumn{2}{c|}{57.8 } & \multicolumn{2}{c|}{50.7 } & \multicolumn{2}{c|}{83.1 } & \multicolumn{2}{c}{31.3 } \\
    \textbf{Fisher} & 62.3  & 62.1  & 72.8  & 72.7  & 45.4  & 45.1  & 86.1  & 86.4  & 57.8  & 57.6  & 51.2  & 50.8  & 82.9  & 82.9  & 30.8  & 31.0  \\
    \textbf{RegMean} & 61.9  & 61.9  & 72.4  & 72.5  & 45.2  & 45.2  & 86.5  & 86.6  & 57.3  & 57.3  & 50.1  & 50.0  & 83.0  & 83.0  & 31.1  & 31.0  \\
    \textbf{Self Positioning} & 62.2  & 62.3  & 72.8  & 72.8  & 45.7  & 45.5  & 85.9  & 86.3  & 57.8  & 57.7  & 50.3  & 50.8  & 83.1  & 83.0  & 31.3  & 30.9  \\
    \midrule
    \multicolumn{17}{c}{\textit{3 clusters}} \\
    \midrule
    \textbf{TIES} & \multicolumn{2}{c|}{62.2 } & \multicolumn{2}{c|}{72.5 } & \multicolumn{2}{c|}{45.4 } & \multicolumn{2}{c|}{86.3 } & \multicolumn{2}{c|}{57.7 } & \multicolumn{2}{c|}{51.1 } & \multicolumn{2}{c|}{82.8 } & \multicolumn{2}{c}{31.2 } \\
    \textbf{Fisher} & 62.1  & 61.7  & 72.3  & 72.2  & 45.2  & 44.6  & 86.4  & 86.7  & 57.5  & 56.9  & 51.0  & 50.2  & 82.7  & 82.4  & 30.9  & 31.6  \\
    \textbf{RegMean} & 61.5  & 61.4  & 71.9  & 72.0  & 44.7  & 44.5  & 86.6  & 86.7  & 56.9  & 56.8  & 49.7  & 49.6  & 82.4  & 82.4  & 31.6  & 31.5  \\
    \textbf{Self Positioning} & 62.3  & 62.2  & 72.6  & 72.6  & 45.6  & 45.4  & 86.0  & 86.3  & 58.0  & 57.7  & 51.0  & 51.1  & 82.9  & 82.7  & 31.4  & 31.3  \\
    \midrule
    \multicolumn{17}{c}{\textit{4 clusters}} \\
    \midrule
    \textbf{TIES} & \multicolumn{2}{c|}{62.1 } & \multicolumn{2}{c|}{72.3 } & \multicolumn{2}{c|}{45.2 } & \multicolumn{2}{c|}{86.4 } & \multicolumn{2}{c|}{57.6 } & \multicolumn{2}{c|}{51.2 } & \multicolumn{2}{c|}{82.6 } & \multicolumn{2}{c}{31.3 } \\
    \textbf{Fisher} & 62.1  & 61.7  & 72.3  & 72.2  & 45.2  & 44.6  & 86.4  & 86.7  & 57.5  & 56.9  & 51.0  & 50.2  & 82.7  & 82.4  & 30.9  & 31.6  \\
    \textbf{RegMean} & 61.5  & 61.4  & 71.9  & 72.0  & 44.7  & 44.5  & 86.6  & 86.7  & 56.9  & 56.8  & 49.7  & 49.6  & 82.4  & 82.4  & 31.6  & 31.5  \\
    \textbf{Self Positioning} & 62.3  & 62.2  & 72.6  & 72.6  & 45.6  & 45.4  & 86.0  & 86.3  & 58.0  & 57.7  & 51.0  & 51.1  & 82.9  & 82.7  & 31.4  & 31.3  \\
    \midrule
    \multicolumn{17}{c}{\textit{Iterative Merging (with extra classification training data) }} \\
    \midrule
    \textbf{TIES} & \multicolumn{2}{c|}{62.8 } & \multicolumn{2}{c|}{78.3 } & \multicolumn{2}{c|}{44.8 } & \multicolumn{2}{c|}{85.1 } & \multicolumn{2}{c|}{57.7 } & \multicolumn{2}{c|}{49.6 } & \multicolumn{2}{c|}{82.2 } & \multicolumn{2}{c}{31.0 } \\
    \textbf{Fisher} & \multicolumn{2}{c|}{62.5 } & \multicolumn{2}{c|}{79.2 } & \multicolumn{2}{c|}{44.5 } & \multicolumn{2}{c|}{84.5 } & \multicolumn{2}{c|}{57.6 } & \multicolumn{2}{c|}{48.7 } & \multicolumn{2}{c|}{81.7 } & \multicolumn{2}{c}{29.9 } \\
    \textbf{RegMean} & \multicolumn{2}{c|}{62.7 } & \multicolumn{2}{c|}{78.8 } & \multicolumn{2}{c|}{44.8 } & \multicolumn{2}{c|}{84.7 } & \multicolumn{2}{c|}{57.4 } & \multicolumn{2}{c|}{49.2 } & \multicolumn{2}{c|}{82.1 } & \multicolumn{2}{c}{30.4 } \\
    \textbf{Self Positioning} & \multicolumn{2}{c|}{63.0 } & \multicolumn{2}{c|}{79.1 } & \multicolumn{2}{c|}{44.6 } & \multicolumn{2}{c|}{85.3 } & \multicolumn{2}{c|}{57.6 } & \multicolumn{2}{c|}{49.9 } & \multicolumn{2}{c|}{82.2 } & \multicolumn{2}{c}{30.5 } \\
    \bottomrule
    \end{tabular}}
  \label{tab:appendix_results_mteb}%
\end{table*}
```

