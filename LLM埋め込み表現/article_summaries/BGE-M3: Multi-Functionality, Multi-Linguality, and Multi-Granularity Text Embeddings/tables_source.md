# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[!t]
    \centering
    \footnotesize
    \setlength{\tabcolsep}{2pt}
    \begin{tabular}{l|c|cccccccccccccccccc}
    % \ChangeRT{1pt} 
    \hline
    Model & Avg & ar & bn & en & es & fa & fi & fr & hi & id & ja & ko & ru & sw & te & th & zh & de & yo \\
    \hline
    \multicolumn{20}{l}{Baselines~(\textit{Prior Work})} \\
    \hline
    % BM25 (D.T.) & 38.5 & 48.1 & 50.8 & 35.1 & 31.9 & 33.3 & 55.1 & 18.3 & 45.8 & 44.9 & 36.9 & 41.9 & 33.4 & 38.3 & 49.4 & 48.4 & 18.0 & 22.6 & 40.6 \\
    BM25 & 31.9 & 39.5 & 48.2 & 26.7 & 7.7 & 28.7 & 45.8 & 11.5 & 35.0 & 29.7 & 31.2 & 37.1 & 25.6 & 35.1 & 38.3 & 49.1 & 17.5 & 12.0 & 56.1 \\
    mDPR & 41.8 & 49.9 & 44.3 & 39.4 & 47.8 & 48.0 & 47.2 & 43.5 & 38.3 & 27.2 & 43.9 & 41.9 & 40.7 & 29.9 & 35.6 & 35.8 & 51.2 & 49.0 & 39.6  \\
    mContriever & 43.1 & 52.5 & 50.1 & 36.4 & 41.8 & 21.5 & 60.2 & 31.4 & 28.6 & 39.2 & 42.4 & 48.3 & 39.1 & 56.0 & 52.8 & 51.7 & 41.0 & 40.8 & 41.5 \\
    mE5$_{\mathrm{{\text{large}}}}$ & 66.6 & 76.0 & 75.9 & 52.9 & 52.9 & 59.0 & 77.8 & 54.5 & 62.0 & 52.9 & 70.6 & 66.5 & 67.4 & 74.9 & 84.6 & 80.2 & 56.0 & 56.4 & 78.3 \\
    E5$_{\mathrm{\text{mistral-7b}}}$ & 63.4 & 73.3 & 70.3 & 57.3 & 52.2 & 52.1 & 74.7 & 55.2 & 52.1 & 52.7 & 66.8 & 61.8 & 67.7 & 68.4 & 73.9 & 74.0 & 54.0 & 54.1 & 79.7 \\
    OpenAI-3 & 54.9 & - & - & - & - & - & - & - & - & - & - & - & - & - & - & - & - & - & - \\
    \hline
    \multicolumn{20}{l}{M3-Embedding~(\textit{Our Work})} \\
    \hline
    Dense & 69.2 & 78.4 & 80.0 & 56.9 & 56.1 & 60.9 & 78.6 & 58.3 & 59.5 & 56.1 & 72.8 & 69.9 & 70.1 & 78.7 & 86.2 & 82.6 & 62.7 & 56.7 & 81.8 \\
    Sparse & 53.9 & 67.1 & 68.9 & 43.8 & 38.6 & 45.1 & 65.4 & 35.3 & 48.2 & 48.9 & 56.1 & 61.5 & 44.5 & 57.9 & 79.1 & 70.9 & 36.1 & 32.5 & 70.0 \\
    Multi-vec & 70.5 & 79.6 & 81.0 & 59.3 & 57.8 & 62.0 & 80.1 & 59.4 & 61.5 & 58.3 & 74.5 & 71.2 & 71.2 & 79.1 & 87.9 & 83.0 & 63.7 & 58.0 & 82.4 \\
    Dense+Sparse & 70.4 & 79.6 & 80.7 & 58.8 & 58.1 & 62.3 & 79.7 & 58.0 & 62.9 & 58.3 & 73.9 & 71.2 & 69.8 & 78.5 & 87.2 & 83.1 & 63.5 & 57.7 & 83.3 \\
    All & \textbf{71.5} & \textbf{80.2} & \textbf{81.5} & \textbf{59.6} & \textbf{59.7} & \textbf{63.4} & \textbf{80.4} & \textbf{61.2} & \textbf{63.3} & \textbf{59.0} & \textbf{75.2} & \textbf{72.1} & \textbf{71.7} & \textbf{79.6} & \textbf{88.1} & \textbf{83.7} & \textbf{64.9} & \textbf{59.8} & \textbf{83.5} \\
    % \hline
    % \multicolumn{20}{l}{BGE-M3-w.o.ensemble~(\textit{Ablation Study})} \\
    % \hline
    % Dense & \textit{72.2} & & 79.5 & & & & & & 59.2 & & & 69.8 & & 78.2 & 86.0 & 82.4 & 62.1 & & 60.3 \\
    % Sparse & \textit{59.6} & & 65.9 & & & & & & 45.3 & & & 59.4 & & 56.6 & 77.8 & 68.3 & 33.0 & & 70.4 \\
    % Hybrid & \textit{73.4} & & 80.6 & & & & & & 63.2 & & & 71.9 & & 78.7 & 87.4 & 83.3 & 61.7 & & 60.5 \\
    % ColBERT & \textit{72.6} & & 80.1 & & & & & & 60.4 & & & 71.8 & & 79.3 & 87.9 & 82.0 & 61.5 & & 58.8 \\
    % All & \textit{74.2} & & 81.3 & & & & & & 63.8 & & & 73.1 & & 79.7 & 87.9 & 83.9 & 63.6 & & 60.5 \\
    \hline
    
    % \ChangeRT{1pt}
    \end{tabular}
    \vspace{-5pt}
    \caption{\textbf{Multi-lingual retrieval performance on the MIRACL dev set} (measured by nDCG@10).}
    \vspace{-10pt}
    \label{tab:miracl_ndcg_results}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
    \centering
    \footnotesize
    % \scriptsize
    \setlength{\tabcolsep}{3pt}
    \begin{tabular}{lcccccc|ccccc}
    % \ChangeRT{1pt} 
    \hline
    & \multicolumn{6}{c|}{Baselines~(\textit{Prior Work})} & \multicolumn{5}{c}{M3-Embedding~(\textit{Our Work})} \\
    \hline
    & BM25 & mDPR & mContriever & mE5$_{\mathrm{{\text{large}}}}$ & E5$_{\mathrm{\text{mistral-7b}}}$ & OpenAI-3 & Dense & Sparse & Multi-vec & Dense+Sparse & All \\
    \hline
    ar      & 18.9 & 48.2 & 58.2 & 68.7 & 59.6 & 65.6 & 71.1 & 23.5 & 71.4 & 71.1 & \textbf{71.5} \\
    da      & 49.3 & 67.4 & 73.9 & 77.4 & \textbf{77.8} & 73.6 & 77.2 & 55.4 & 77.5 & 77.4 & 77.6 \\
    de      & 35.4 & 65.8 & 71.7 & 76.9 & \textbf{77.0} & 73.6 & 76.2 & 43.3 & 76.3 & 76.4 & 76.3 \\
    % en      & 73.1 & 75.0 & 76.4 & 79.3 & 80.2 & 75.2 & 78.5 & 75.5 & 78.6 & 78.4 & 78.5 \\
    es      & 43.4 & 66.8 & 72.6 & 76.4 & \textbf{77.4} & 73.9 & 76.4 & 50.6 & 76.6 & 76.7 & 76.9 \\
    fi      & 46.3 & 56.2 & 70.2 & 74.0 & 72.0 & 72.7 & 75.1 & 51.1 & 75.3 & 75.3 & \textbf{75.5} \\
    fr      & 45.3 & 68.2 & 72.8 & 75.5 & \textbf{78.0} & 74.1 & 76.2 & 53.9 & 76.4 & 76.6 & 76.6 \\
    he      & 26.9 & 49.7 & 63.8 & 69.6 & 47.2 & 58.1 & 72.4 & 31.1 & 72.9 & 72.5 & \textbf{73.0} \\
    hu      & 38.2 & 60.4 & 69.7 & 74.7 & \textbf{75.0} & 71.2 & 74.7 & 44.6 & 74.6 & 74.9 & \textbf{75.0} \\
    it      & 45.2 & 66.0 & 72.3 & 76.8 & \textbf{77.1} & 73.6 & 76.0 & 52.5 & 76.4 & 76.3 & 76.5 \\
    ja      & 24.5 & 60.3 & 64.8 & 71.5 & 65.1 & 71.9 & 75.0 & 31.3 & 75.1 & 75.0 & \textbf{75.2} \\
    km      & 27.8 & 29.5 & 26.8 & 28.1 & 34.3 & 33.9 & 68.6 & 30.1 & 69.1 & 68.8 & \textbf{69.2} \\
    ko      & 27.9 & 50.9 & 59.7 & 68.1 & 59.4 & 63.9 & 71.6 & 31.4 & 71.7 & 71.6 & \textbf{71.8} \\
    ms      & 55.9 & 65.5 & 74.1 & 76.3 & 77.2 & 73.3 & 77.2 & 62.4 & \textbf{77.4} & \textbf{77.4} & \textbf{77.4} \\
    nl      & 56.2 & 68.2 & 73.7 & 77.8 & \textbf{79.1} & 74.2 & 77.4 & 62.4 & 77.6 & 77.7 & 77.6 \\
    no      & 52.1 & 66.7 & 73.5 & 77.3 & 76.6 & 73.3 & 77.1 & 57.9 & 77.2 & \textbf{77.4} & 77.3 \\
    pl      & 40.8 & 63.3 & 71.6 & 76.7 & \textbf{77.1} & 72.7 & 76.3 & 46.1 & 76.5 & 76.3 & 76.6 \\
    pt      & 44.9 & 65.5 & 72.0 & 73.5 & \textbf{77.5} & 73.7 & 76.3 & 50.9 & 76.4 & 76.5 & 76.4 \\
    ru      & 33.2 & 62.7 & 69.8 & \textbf{76.8} & 75.5 & 72.0 & 76.2 & 36.9 & 76.4 & 76.2 & 76.5 \\
    sv      & 54.6 & 66.9 & 73.2 & 77.6 & \textbf{78.3} & 74.0 & 76.9 & 59.6 & 77.2 & 77.4 & 77.4 \\
    th      & 37.8 & 53.8 & 66.9 & 76.0 & 67.4 & 65.2 & 76.4 & 42.0 & 76.5 & 76.5 & \textbf{76.6} \\
    tr      & 45.8 & 59.1 & 71.1 & 74.3 & 73.0 & 71.8 & 75.6 & 51.8 & 75.9 & \textbf{76.0} & \textbf{76.0} \\
    vi      & 46.6 & 63.4 & 70.9 & 75.4 & 70.9 & 71.1 & 76.6 & 51.8 & 76.7 & 76.8 & \textbf{76.9} \\
    zh\_cn  & 31.0 & 63.7 & 68.1 & 56.6 & 69.3 & 70.7 & 74.6 & 35.4 & 74.9 & 74.7 & \textbf{75.0} \\
    zh\_hk  & 35.0 & 62.8 & 68.0 & 58.1 & 65.1 & 69.6 & 73.8 & 39.8 & 74.1 & 74.0 & \textbf{74.3} \\
    zh\_tw  & 33.5 & 64.0 & 67.9 & 58.1 & 65.8 & 69.7 & 73.5 & 37.7 & 73.5 & \textbf{73.6} & \textbf{73.6} \\
    \hline
    Avg     & 39.9 & 60.6 & 67.9 & 70.9 & 70.1 & 69.5 & 75.1 & 45.3 & 75.3 & 75.3 & \textbf{75.5} \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    \vspace{-5pt}
    \caption{\textbf{Cross-lingual retrieval performance on MKQA} (measured by Recall@100).}
    \vspace{-5pt}
    \label{tab:mkqa_recall@100_results}
\end{table*}
```

## Table 3
```latex
\begin{table*}[!t]
    \centering
    \small
    \setlength{\tabcolsep}{2.5pt}
    \begin{tabular}{lc|c|ccccccccccccc}
    % \ChangeRT{1pt} 
    \hline
    & Max Length & Avg & ar & de & en & es & fr & hi & it & ja & ko & pt & ru & th & zh \\
    \hline
    \multicolumn{16}{l}{Baselines~(\textit{Prior Work})} \\
    \hline
    % BM25 (W.T.) & - & 28.9 & 16.0 & 36.9 & 67.9 & 42.6 & 51.6 & 16.2 & 40.4 & 8.3 & 19.6 & 36.2 & 13.2 & 26.2 & 0.5 \\
    % BM25 (D.T.) & - & 64.1 & 57.0 & 60.3 & 67.9 & 82.1 & 77.4 & 58.1 & 74.5 & 58.2 & 51.6 & 80.7 & 73.6 & 34.3 & 58.0 \\
    BM25 & 8192 & 53.6 & 45.1 & 52.6 & 57.0 & 78.0 & 75.7 & 43.7 & 70.9 & 36.2 & 25.7 & 82.6 & 61.3 & 33.6 & 34.6 \\
    mDPR & 512 & 23.5 & 15.6 & 17.1 & 23.9 & 34.1 & 39.6 & 14.6 & 35.4 & 23.7 & 16.5 & 43.3 & 28.8 & 3.4 & 9.5 \\
    mContriever & 512 & 31.0 & 25.4 & 24.2 & 28.7 & 44.6 & 50.3 & 17.2 & 43.2 & 27.3 & 23.6 & 56.6 & 37.7 & 9.0 & 15.3 \\
    mE5$_{\mathrm{{\text{large}}}}$ & 512 & 34.2 & 33.0 & 26.9 & 33.0 & 51.1 & 49.5 & 21.0 & 43.1 & 29.9 & 27.1 & 58.7 & 42.4 & 15.9 & 13.2 \\
    % E5$_{\mathrm{\text{mistral-7b}}}$ & 36.0 & 27.4 & 28.9 & 35.2 & 53.3 & 59.3 & 20.9 & 48.4 & 31.1 & 27.0 & 64.1 & 43.5 & 14.7 & 14.5 \\
    % jina-embeddings-v2-base-en & - & - & - & 28.0 & - & - & - & - & - & - & - & - & - & - \\
    % bge-v2 & 35.8 & 31.6 & 29.2 & 32.0 & 50.9 & 55.9 & 23.9 & 45.0 & 34.2 & 26.8 & 58.9 & 43.2 & 17.4 & 16.3 \\
    % bge-v2 (MCLS-256) & 35.5 & 31.3 & 29.0 & 32.0 & 49.6 & 55.5 & 23.9 & 44.4 & 33.0 & 26.7 & 58.4 & 43.2 & 17.6 & 16.3 \\
    % bge-v2-w.o.long & 33.9 & 31.0 & 27.5 & 30.9 & 48.6 & 54.1 & 22.8 & 42.2 & 31.0 & 23.9 & 56.9 & 41.3 & 15.9 & 14.7 \\
    % bge-v2-w.o.long (MCLS-256) & 33.8 & 30.7 & 28.1 & 31.0 & 48.1 & 53.3 & 22.6 & 42.4 & 31.0 & 23.8 & 56.8 & 41.2 & 16.5 & 14.4 \\
    % bge-v2-short & 36.5 & 32.4 & 30.2 & 32.7 & 51.8 & 56.3 & 24.3 & 46.4 & 34.4 & 27.1 & 58.4 & 44.6 & 18.8 & 16.5 \\
    % bge-v2-short (MCLS-256) & 36.2 & 32.1 & 29.8 & 32.8 & 50.9 & 56.4 & 24.4 & 45.5 & 33.8 & 27.0 & 58.6 & 43.7 & 19.2 & 16.4 \\
    E5$_{\mathrm{\text{mistral-7b}}}$ & 8192 & 42.6 & 29.6 & 40.6 & 43.3 & 70.2 & 60.5 & 23.2 & 55.3 & 41.6 & 32.7 & 69.5 & 52.4 & 18.2 & 16.8 \\
    text-embedding-ada-002 & 8191 & 32.5 & 16.3 & 34.4 & 38.7 & 59.8 & 53.9 & 8.0 & 46.5 & 28.6 & 20.7 & 60.6 & 34.8 & 9.0 & 11.2 \\
    jina-embeddings-v2-base-en & 8192 & - & - & - & 37.0 & - & - & - & - & - & - & - & - & - & - \\
    \hline
    \multicolumn{16}{l}{M3-Embedding~(\textit{Our Work})} \\
    \hline
    Dense           & 8192 & 52.5 & 47.6 & 46.1 & 48.9 & 74.8 & 73.8 & 40.7 & 62.7 & 50.9 & 42.9 & 74.4 & 59.5 & 33.6 & 26.0 \\
    Sparse          & 8192 & 62.2 & 58.7 & 53.0 & 62.1 & 87.4 & 82.7 & 49.6 & 74.7 & 53.9 & 47.9 & 85.2 & 72.9 & 40.3 & 40.5 \\
    Multi-vec    & 8192 & 57.6 & 56.6 & 50.4 & 55.8 & 79.5 & 77.2 & 46.6 & 66.8 & 52.8 & 48.8 & 77.5 & 64.2 & 39.4 & 32.7 \\
    Dense+Sparse    & 8192 & 64.8 & 63.0 & 56.4 & \textbf{64.2} & \textbf{88.7} & \textbf{84.2} & \textbf{52.3} & \textbf{75.8} & 58.5 & 53.1 & \textbf{86.0} & \textbf{75.6} & 42.9 & \textbf{42.0} \\
    All             & 8192 & \textbf{65.0} & \textbf{64.7} & \textbf{57.9} & 63.8 & 86.8 & 83.9 & 52.2 & 75.5 & \textbf{60.1} & \textbf{55.7} & 85.4 & 73.8 & \textbf{44.7} & 40.0 \\
    % Dense (MCLS)    & 8192 & 50.7 & 45.6 & 48.7 & 47.3 & 73.8 & 70.3 & 39.4 & 60.0 & 48.3 & 38.7 & 73.1 & 56.6 & 31.5 & 26.3 \\
    % Dense+Sparse (0.3)    & 8192 & 59.9 & 56.2 & 54.5 & 58.4 & 83.2 & 80.1 & 47.6 & 69.8 & 56.0 & 49.7 & 79.8 & 67.0 & 41.2 & 34.6 \\
    % All             & 8192 & 60.1 & 57.1 & 54.0 & 58.5 & 82.3 & 80.4 & 48.9 & 69.7 & 56.3 & 51.0 & 80.2 & 66.4 & 42.0 & 34.8 \\
    % bge-v2 & 49.3 & 43.5 & 44.1 & 46.1 & 71.5 & 70.7 & 35.7 & 60.7 & 46.0 & 38.3 & 71.7 & 56.5 & 30.7 & 25.1 \\
    % bge-v2 (MCLS-256) & 49.9 & 45.1 & 46.1 & 45.6 & 73.3 & 71.1 & 37.1 & 59.4 & 48.2 & 36.3 & 72.4 & 55.5 & 33.1 & 25.0 \\
    \hline
    \multicolumn{16}{l}{M3-w.o.long} \\
    \hline
    % Dense-w.o.long (new) & 8192 & 39.3 & 34.2 & 33.4 & 36.7 & 62.1 & 56.7 & 26.6 & 49.8 & 38.8 & 27.5 & 61.1 & 48.6 & 19.5 & 15.8 \\
    % Dense-w.o.long (new) (MCLS) & 8192 & 43.8 & 36.3 & 41.6 & 40.4 & 67.2 & 62.7 & 31.9 & 54.4 & 41.6 & 31.8 & 66.3 & 51.3 & 25.8 & 17.7 \\
    Dense-w.o.long & 8192 & 41.2 & 35.4 & 35.2 & 37.5 & 64.0 & 59.3 & 28.8 & 53.1 & 41.7 & 29.8 & 63.5 & 51.1 & 19.5 & 16.5 \\
    Dense-w.o.long (MCLS) & 8192 & 45.0 & 37.9 & 43.3 & 41.2 & 67.7 & 64.6 & 32.0 & 55.8 & 43.4 & 33.1 & 67.8 & 52.8 & 27.2 & 18.2 \\
    % bge-v2-short & 43.4 & 37.7 & 38.2 & 37.3 & 66.4 & 63.1 & 28.9 & 54.6 & 43.8 & 31.1 & 65.1 & 53.8 & 26.3 & 18.1 \\
    % bge-v2-short (MCLS-256) & 47.3 & 40.1 & 45.9 & 42.2 & 69.3 & 67.5 & 33.1 & 59.0 & 46.0 & 35.9 & 69.7 & 55.6 & 30.0 & 20.9 \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    \vspace{-5pt}
    \caption{\textbf{Evaluation of multilingual long-doc retrieval on the MLDR test set} (measured by nDCG@10).}
    % , w.r.t. maximum passages sequence length of 512 and 8192
    \vspace{-15pt}
    \label{tab:bge_long_results}
\end{table*}
```

## Table 4
```latex
\begin{table}[]
    \centering
    \small
    \setlength{\tabcolsep}{4pt}
    \begin{tabular}{lcc}
    % \ChangeRT{1pt} 
    \hline
    Model & Max Length & nDCG@10 \\
    \hline
    \multicolumn{3}{l}{Baselines~(\textit{Prior Work})} \\
    \hline
    mDPR                                    & 512 & 16.3 \\
    mContriever                             & 512 & 23.3 \\
    mE5$_{\mathrm{{\text{large}}}}$         & 512 & 24.2 \\
    % bge-large-en-v1.5                       & 512 & 27.3 \\
    E5$_{\mathrm{\text{mistral-7b}}}$       & 8192 & 49.9 \\
    text-embedding-ada-002                  & 8191 & 41.1 \\
    text-embedding-3-large                  & 8191 & 51.6 \\
    jina-embeddings-v2-base-en              & 8192 & 39.4 \\
    \hline
    \multicolumn{3}{l}{M3-Embedding~(\textit{Our Work})} \\
    \hline
    Dense                                   & 8192 & 48.7 \\
    Sparse                                  & 8192 & 57.5 \\
    Multi-vec                            & 8192 & 55.4 \\
    Dense+Sparse                            & 8192 & 60.1 \\
    All                                     & 8192 & \textbf{61.7} \\
    \hline
    % \multicolumn{3}{l}{M3-w.o.long~(\textit{Ablation Study})} \\
    % \hline
    %  Dense w.o.long                          & 8192 & 32.9 \\
    % Dense w.o.long (MCLS)               & 8192 & 41.5 \\
    % \hline
    \end{tabular}
    \caption{\textbf{Evaluation on NarrativeQA} (nDCG@10).}
    % \vspace{-10pt}
    \label{tab:narrativeqa_results}
\end{table}
```

## Table 5
```latex
\begin{table}[]
    \centering
    \small
    \setlength{\tabcolsep}{3pt}
    \begin{tabular}{ll|c}
        \hline
        \multicolumn{2}{l|}{Model} & MIRACL  \\
        \hline
        \multirow{3}{*}{M3-w.skd} & Dense & 69.2 \\
        & Sparse & 53.9 \\
        & Multi-vec & 70.5 \\
        \hline
        \multirow{3}{*}{M3-w.o.skd} & Dense & 68.7 \\
        & Sparse & 36.7 \\
        & Multi-vec & 69.3 \\
        \hline
    \end{tabular}
    \caption{\textbf{Ablation study of self-knowledge distillation on the MIRACL dev set} (nDCG@10).}
    \label{tab:brief_unify_ablation}
    % \vspace{-8pt}
\end{table}
```

## Table 6
```latex
\begin{table}[]
    \centering
    \small
    \setlength{\tabcolsep}{3pt}
    \begin{tabular}{l|cc}
        \hline
        Model (Dense) & MIRACL  \\
        \hline
        Fine-tune & 60.5  \\
        RetroMAE + Fine-tune & 66.1  \\
        RetroMAE + Unsup + Fine-tune & 69.2 \\
        \hline
    \end{tabular}
    \caption{\textbf{Ablation study of multi-stage training on the MIRACL dev set} (nDCG@10).}
    \label{tab:stage}
    \vspace{-8pt}
\end{table}
```

## Table 7
```latex
\begin{table*}[!t]
    \centering
    \footnotesize
    \begin{tabular}{ccccccc}
    % \ChangeRT{1pt} 
    \hline
    Language & Source  & \#train & \#dev & \#test & \#cropus & Avg. Length of Docs \\
    \hline
    ar & Wikipedia & 1,817 & 200 & 200 & 7,607 & 9,428 \\
    de & Wikipedia, mC4 & 1,847 & 200 & 200 & 10,000 & 9,039 \\
    % en & Wikipedia & 104,090 & 200 & 800 & 200,000 & 3,308 \\
    en & Wikipedia & 10,000 & 200 & 800 & 200,000 & 3,308 \\
    es & Wikipedia, mC4 & 2,254 & 200 & 200 & 9,551 & 8,771 \\
    fr & Wikipedia & 1,608 & 200 & 200 & 10,000 & 9,659 \\
    hi & Wikipedia & 1,618 & 200 & 200 & 3,806 & 5,555 \\
    it & Wikipedia & 2,151 & 200 & 200 & 10,000 & 9,195 \\
    ja & Wikipedia & 2,262 & 200 & 200 & 10,000 & 9,297 \\
    ko & Wikipedia & 2,198 & 200 & 200 & 6,176 & 7,832 \\
    pt & Wikipedia & 1,845 & 200 & 200 & 6,569 & 7,922 \\
    ru & Wikipedia & 1,864 & 200 & 200 & 10,000 & 9,723 \\
    th & mC4 & 1,970 & 200 & 200 & 10,000 & 8,089 \\
    % zh & Wikipedia, Wudao & 100,834 & 200 & 800 & 200,000 & 4,249 \\
    zh & Wikipedia, Wudao & 10,000 & 200 & 800 & 200,000 & 4,249 \\
    \hline
    % Total & -- & 226,358 & 2,600 & 3,800 & 493,709 & 4,737 \\
    Total & -- & 41,434 & 2,600 & 3,800 & 493,709 & 4,737 \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    % \vspace{-5pt}
    \caption{Specifications of MultiLongDoc dataset.}
    % \vspace{-10pt}
    \label{tab:bge_long}
\end{table*}
```

## Table 8
```latex
\begin{table}[h]
    \centering
    % \setlength{\tabcolsep}{3pt} 
    \footnotesize
    \begin{tabular}{C{2.4cm}|C{2.2cm}|C{1.2cm}}
    \toprule
    % \hline
        Data Source & Language & Size \\
        \hline
        \multicolumn{3}{c}{Unsupervised Data} \\
        \hline
        MTP & EN, ZH & 291.1M \\
        \hline
        S2ORC, Wikipeida & EN & 48.3M \\
        \hline
        % S2ORC & EN & 41.8M \\
        xP3, mC4, CC-News & Multi-Lingual & 488.4M \\
        \hline
        % xP3 & Multi-Lingual & 62.6M \\
        % mC4 & Multi-Lingual & 16.4M \\
        % CC-News & Multi-Lingual & 409.4M \\
        NLLB, CCMatrix & Cross-Lingual & 391.3M \\
        \hline
        % NLLB & Cross-Lingual & 197.8M \\
        % CCMatrix & Cross-Lingual & 193.5M \\
        CodeSearchNet & Text-Code & 344.1K \\
        \hline
        Total & -- & 1.2B \\ 
        \hline
        \hline
        \multicolumn{3}{c}{Fine-tuning Data} \\
        \hline
        MS MARCO, HotpotQA, NQ, NLI, etc. & EN & 1.1M \\
        \hline
        DuReader, T$^2$-Ranking, NLI-zh, etc. & ZH & 386.6K \\
        \hline
        MIRACL, Mr.TyDi & Multi-Lingual & 88.9K \\
        % \hline
        % FT Total & -- & -- \\ 
        \hline
        \hline
        MultiLongDoc & Multi-Lingual & 41.4K \\
    % \hline
    \bottomrule
    \end{tabular}
    \caption{Specification of training data.}
    \vspace{-10pt}
    \label{tab:data}
\end{table}
```

## Table 9
```latex
\begin{table}[!t]
    \centering
    \setlength{\tabcolsep}{4pt}
    \begin{tabular}{lcc}
    \toprule
        \multirow{2}{*}{Length Range} & \multicolumn{2}{c}{Batch Size} \\
        \cline{2-3}
            & Unsupervised &  Fine-tuning \\
        \hline
        0-500       & 67,200 & 1,152 \\
        500-1000    & 54,720 & 768 \\
        1000-2000   & 37,248 & 480 \\
        2000-3000   & 27,648 & 432 \\
        3000-4000   & 21,504 & 336 \\
        4000-5000   & 17,280 & 336 \\
        5000-6000   & 15,072 & 288 \\
        6000-7000   & 12,288 & 240 \\
        7000-8192   & 9,984  & 192 \\
    \bottomrule
    \end{tabular}
    \caption{Detailed total batch size used in training for data with different sequence length ranges.}
    \label{tab:batch_size_dict}
\end{table}
```

## Table 10
```latex
\begin{table}[h]
    \centering
    \setlength{\tabcolsep}{5pt}
    \begin{tabular}{cccc}
    % \ChangeRT{1pt} 
    \hline
    \multirow{2}{*}{Use Split-batch} & \multicolumn{3}{c}{Max Length} \\
    \cline{2-4}
    & 1024 & 4096 & 8192 \\
    \hline
    $\times$ & 262 & 25  & 6 \\
    $\surd$ & 855 & 258 & 130 \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    % \vspace{-5pt}
    \caption{Maximum batch size per device under different experimental settings.}
    % , w.r.t. maximum passages sequence length of 512 and 8192
    % \vspace{-10pt}
    \label{tab:efficient_batching}
\end{table}
```

## Table 11
```latex
\begin{table}[!t]
    \centering
    \setlength{\tabcolsep}{1.5pt}
    \begin{tabular}{llccc}
    \toprule
        % \multirow{2}{*}{Length Range} & \multicolumn{2}{c}{Batch Size} \\
        % \cline{2-3}
        %     & Unsupervised &  Fine-tuning \\
        Method & Tokenizer & MIRACL & MKQA & MLDR \\
        \midrule
        BM25 & Analyzer & 38.5 & 40.9 & 64.1 \\
        BM25 & XLM-R &  31.9 & 39.9 & 53.6 \\
        M3(Sparse) & XLM-R & 53.9 & 45.3 & 62.2 \\
        M3(All) & XLM-R & 71.5 & 75.5 & 65.0 \\
        
    \bottomrule
    \end{tabular}
    \caption{Comparison with the BM25 methods using different tokenizers. }
    \label{tab:bm25_tokenizer}
\end{table}
```

## Table 12
```latex
\begin{table*}[!t]
    \centering
    \footnotesize
    \setlength{\tabcolsep}{2.1pt}
    \begin{tabular}{l|c|cccccccccccccccccc}
    % \ChangeRT{1pt} 
    \hline
    Model & Avg & ar & bn & en & es & fa & fi & fr & hi & id & ja & ko & ru & sw & te & th & zh & de & yo \\
    \hline
    \multicolumn{20}{l}{Baselines~(\textit{Prior Work})} \\
    \hline
    % BM25 (D.T.) & 77.2 & 88.9 & 90.9 & 81.9 & 70.2 & 73.1 & 89.1 & 65.3 & 86.8 & 90.4 & 80.5 & 78.3 & 66.1 & 70.1 & 83.1 & 88.7 & 56.0 & 57.2 & 73.3 \\
    BM25 & 67.3 & 78.7 & 90.0 & 63.6 & 25.4 & 68.1 & 81.2 & 50.2 & 73.8 & 71.8 & 73.6 & 70.1 & 56.4 & 69.9 & 73.3 & 87.5 & 55.1 & 42.8 & 80.1 \\
    mDPR & 79.0 & 84.1 & 81.9 & 76.8 & 86.4 & 89.8 & 78.8 & 91.5 & 77.6 & 57.3 & 82.5 & 73.7 & 79.7 & 61.6 & 76.2 & 67.8 & 94.4 & 89.8 & 71.5  \\
    mContriever & 84.9 & 92.5 & 92.1 & 79.7 & 84.1 & 65.4 & 95.3 & 82.4 & 64.6 & 80.2 & 87.8 & 87.5 & 85.0 & 91.1 & 96.1 & 93.6 & 90.3 & 84.1 & 77.0 \\
    mE5$_{\mathrm{{\text{large}}}}$ & 94.1 & 97.3 & 98.2 & 87.6 & 89.1 & 92.9 & 98.1 & 90.6 & 93.9 & 87.9 & 97.1 & 93.4 & 95.5 & 96.7 & 99.2 & 98.9 & 93.3 & 90.7 & 93.1 \\
    E5$_{\mathrm{\text{mistral-7b}}}$ & 92.7 & 96.0 & 96.0 & 90.2 & 87.5 & 88.0 & 96.7 & 92.8 & 89.9 & 88.4 & 95.1 & 89.4 & 95.0 & 95.5 & 95.1 & 96.5 & 90.1 & 88.7 & 97.9 \\
    % OpenAI-embebedding-3 & 54.9 \\
    \hline
    \multicolumn{20}{l}{M3-Embedding~(\textit{Our Work})} \\
    \hline
    Dense   & 95.5 & 97.6 & 98.7 & 90.7 & 91.1 & 94.0 & 97.9 & 93.8 & 94.4 & 90.5 & 97.5 & 95.5 & 95.9 & 97.2 & \textbf{99.4} & 99.1 & 96.9 & 90.9 & 98.7 \\
    Sparse  & 85.6 & 92.0 & 96.7 & 81.5 & 72.1 & 87.0 & 91.5 & 73.3 & 87.1 & 84.8 & 92.4 & 91.7 & 76.9 & 85.1 & 98.1 & 95.2 & 72.9 & 69.1 & 92.9 \\
    Multi-vec  & 96.3 & 97.8 & \textbf{98.9} & 91.7 & 92.4 & 94.9 & 98.2 & \textbf{96.1} & 95.1 & 92.5 & \textbf{98.0} & 95.9 & 96.6 & 97.3 & \textbf{99.4} & \textbf{99.2} & 97.3 & \textbf{92.4} & 99.2 \\
    Dense+Sparse  & 96.2 & \textbf{98.0} & \textbf{98.9} & \textbf{92.4} & 92.5 & \textbf{95.6} & 98.3 & 94.6 & \textbf{95.6} & \textbf{92.6} & 97.5 & 95.6 & 96.6 & \textbf{97.4} & 99.1 & 99.0 & 96.8 & 91.0 & \textbf{100.0} \\
    All  & \textbf{96.4} & \textbf{98.0} & \textbf{98.9} & 92.1 & \textbf{92.9} & \textbf{95.6} & \textbf{98.4} & 95.6 & 95.2 & 92.5 & \textbf{98.0} & \textbf{96.0} & \textbf{96.7} & 97.2 & \textbf{99.4} & \textbf{99.2} & \textbf{97.6} & 92.3 & 99.2 \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    % \vspace{-5pt}
    \caption{Recall@100 on the dev set of the MIRACL dataset for multilingual retrieval in all 18 languages.}
    % \vspace{-10pt}
    \label{tab:miracl_recall_results}
\end{table*}
```

## Table 13
```latex
\begin{table*}[!t]
    \centering
    \small
    \setlength{\tabcolsep}{3pt}
    \begin{tabular}{lcccccc|ccccc}
    % \ChangeRT{1pt} 
    \hline
    & \multicolumn{6}{c|}{Baselines~(\textit{Prior Work})} & \multicolumn{5}{c}{M3-Embedding~(\textit{Our Work})} \\
    \hline
    & BM25 & mDPR & mContriever & mE5$_{\mathrm{{\text{large}}}}$ & E5$_{\mathrm{\text{mistral-7b}}}$ & OpenAI-3 & Dense & Sparse & Multi-vec & Dense+Sparse & All \\
    \hline
    ar      & 13.4 & 33.8 & 43.8 & 59.7 & 47.6 & 55.1 & 61.9 & 19.5 & 62.6 & 61.9 & \textbf{63.0} \\
    da      & 36.2 & 55.7 & 63.3 & 71.7 & \textbf{72.3} & 67.6 & 71.2 & 45.1 & 71.7 & 71.3 & 72.0 \\
    de      & 23.3 & 53.2 & 60.2 & \textbf{71.2} & 70.8 & 67.6 & 69.8 & 33.2 & 69.6 & 70.2 & 70.4 \\
    % en      & 63.4 & 67.2 & 68.3 & 75.6 & 76.2 & 69.9 & 73.3 & 68.7 & 73.5 & 73.5 & 73.7 \\
    es      & 29.8 & 55.4 & 62.3 & 70.8 & \textbf{71.6} & 68.0 & 69.8 & 40.3 & 70.3 & 70.2 & 70.7 \\
    fi      & 33.2 & 42.8 & 58.7 & 67.7 & 63.6 & 65.5 & 67.8 & 41.2 & 68.3 & 68.4 & \textbf{68.9} \\
    fr      & 30.3 & 56.5 & 62.6 & 69.5 & \textbf{72.7} & 68.2 & 69.6 & 43.2 & 70.1 & 70.1 & 70.8 \\
    he      & 16.1 & 34.0 & 50.5 & 61.4 & 32.4 & 46.3 & 63.4 & 24.5 & 64.4 & 63.5 & \textbf{64.6} \\
    hu      & 26.1 & 46.1 & 57.1 & 68.0 & \textbf{68.3} & 64.0 & 67.1 & 34.5 & 67.3 & 67.7 & 67.9 \\
    it      & 31.5 & 53.8 & 62.0 & 71.2 & \textbf{71.3} & 67.6 & 69.7 & 41.5 & 69.9 & 69.9 & 70.3 \\
    ja      & 14.5 & 46.3 & 50.7 & 63.1 & 57.6 & 64.2 & 67.0 & 23.3 & 67.8 & 67.1 & \textbf{67.9} \\
    km      & 20.7 & 20.6 & 18.7 & 18.3 & 23.3 & 25.7 & 58.5 & 24.4 & 59.2 & 58.9 & \textbf{59.5} \\
    ko      & 18.3 & 36.8 & 44.9 & 58.9 & 49.4 & 53.9 & 61.9 & 24.3 & 63.2 & 62.1 & \textbf{63.3} \\
    ms      & 42.3 & 53.8 & 63.7 & 70.2 & 71.1 & 66.1 & 71.6 & 52.5 & 72.1 & 71.8 & \textbf{72.3} \\
    nl      & 42.5 & 56.9 & 63.9 & \textbf{73.0} & 74.5 & 68.8 & 71.3 & 52.9 & 71.8 & 71.7 & 72.3 \\
    no      & 38.5 & 55.2 & 63.0 & 71.1 & 70.8 & 67.0 & 70.7 & 47.0 & 71.4 & 71.1 & \textbf{71.6} \\
    pl      & 28.7 & 50.4 & 60.9 & 70.5 & \textbf{71.5} & 66.1 & 69.4 & 36.4 & 70.0 & 69.9 & 70.4 \\
    pt      & 31.8 & 52.5 & 61.0 & 66.8 & \textbf{71.6} & 67.7 & 69.3 & 40.2 & 70.0 & 69.8 & 70.6 \\
    ru      & 21.8 & 49.8 & 57.9 & \textbf{70.6} & 68.7 & 65.1 & 69.4 & 29.2 & 70.0 & 69.4 & 70.0 \\
    sv      & 41.1 & 54.9 & 62.7 & 72.0 & \textbf{73.3} & 67.8 & 70.5 & 49.8 & 71.3 & 71.5 & 71.5 \\
    th      & 28.4 & 40.9 & 54.4 & 69.7 & 57.1 & 55.2 & 69.6 & 34.7 & 70.5 & 69.8 & \textbf{70.8} \\
    tr      & 33.5 & 45.5 & 59.9 & 67.3 & 65.5 & 64.9 & 68.2 & 40.9 & 69.0 & 69.1 & \textbf{69.6} \\
    vi      & 33.6 & 51.3 & 59.9 & 68.7 & 62.3 & 63.5 & 69.6 & 42.2 & 70.5 & 70.2 & \textbf{70.9} \\
    zh\_cn  & 19.4 & 50.1 & 55.9 & 44.3 & 61.2 & 62.7 & 66.4 & 26.9 & 66.7 & 66.6 & \textbf{67.3} \\
    zh\_hk  & 23.9 & 50.2 & 55.5 & 46.4 & 55.9 & 61.4 & 65.8 & 31.2 & 66.4 & 65.9 & \textbf{66.7} \\
    zh\_tw  & 22.5 & 50.6 & 55.2 & 45.9 & 56.5 & 61.6 & 64.8 & 29.8 & 65.3 & 64.9 & \textbf{65.6} \\
    \hline
    Avg     & 28.1 & 47.9 & 56.3 & 63.5 & 62.4 & 62.1 & 67.8 & 36.3 & 68.4 & 68.1 & \textbf{68.8} \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    % \vspace{-5pt}
    \caption{Recall@20 on MKQA dataset for cross-lingual retrieval in all 25 languages.}
    % \vspace{-10pt}
    \label{tab:mkqa_recall@20_results}
\end{table*}
```

## Table 14
```latex
\begin{table*}[!t]
    \centering
    \small
    \setlength{\tabcolsep}{2.5pt}
    \begin{tabular}{l|c|cccccccccccccccccc}
    % \ChangeRT{1pt} 
    \hline
    Model & Avg & ar & bn & en & es & fa & fi & fr & hi & id & ja & ko & ru & sw & te & th & zh & de & yo \\
    \hline
    \multicolumn{20}{l}{M3-w.skd} \\
    \hline
    Dense & 69.2 & 78.4 & 80.0 & 56.9 & 56.1 & 60.9 & 78.6 & 58.3 & 59.5 & 56.1 & 72.8 & 69.9 & 70.1 & 78.7 & 86.2 & 82.6 & 62.7 & 56.7 & 81.8 \\
    Sparse & 53.9 & 67.1 & 68.9 & 43.8 & 38.6 & 45.1 & 65.4 & 35.3 & 48.2 & 48.9 & 56.1 & 61.5 & 44.5 & 57.9 & 79.1 & 70.9 & 36.1 & 32.5 & 70.0 \\
    Multi-vec & 70.5 & 79.6 & 81.0 & 59.3 & 57.8 & 62.0 & 80.1 & 59.4 & 61.5 & 58.3 & 74.5 & 71.2 & 71.2 & 79.1 & 87.9 & 83.0 & 63.7 & 58.0 & 82.4 \\
    \hline
    \multicolumn{20}{l}{M3-w.o.skd} \\
    \hline
    Dense & 68.7 & 78.0 & 79.1 & 56.4 & 55.4 & 60.3 & 78.3 & 58.2 & 59.0 & 55.1 & 72.4 & 68.8 & 69.5 & 77.8 & 85.8 & 82.5 & 63.0 & 56.0 & 80.6 \\
    Sparse & 36.7 & 48.2 & 51.9 & 24.3 & 20.3 & 26.0 & 48.6 & 16.8 & 30.1 & 32.0 & 33.0 & 43.1 & 27.2 & 45.2 & 63.6 & 52.2 & 22.6 & 16.5 & 59.2 \\
    Multi-vec & 69.3 & 78.7 & 80.2 & 57.6 & 56.7 & 60.5 & 79.0 & 58.4 & 59.3 & 57.5 & 74.0 & 70.3 & 70.2 & 78.6 & 86.9 & 82.1 & 61.9 & 56.7 & 78.2 \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    % \vspace{-5pt}
    \caption{Ablation study of self-knowledge distillation on the MIRACL dev set (nDCG@10).}
    % \vspace{-10pt}
    \label{tab:unify_ablation}
\end{table*}
```

## Table 15
```latex
\begin{table*}[!t]
    \centering
    \small
    \setlength{\tabcolsep}{2.5pt}
    \begin{tabular}{l|c|cccccccccccccccccc}
    % \ChangeRT{1pt} 
    \hline
    Model & Avg & ar & bn & en & es & fa & fi & fr & hi & id & ja & ko & ru & sw & te & th & zh & de & yo \\
    \hline
    \multicolumn{20}{l}{Fine-tune} \\
    \hline
    Dense & 60.5 & 71.0 & 72.5 & 47.6 & 46.7 & 51.8 & 72.3 & 50.9 & 48.9 & 48.9 & 65.7 & 60.5 & 60.9 & 71.9 & 81.3 & 74.7 & 54.4 & 48.7 & 60.6 \\
    \hline
    \multicolumn{20}{l}{RetroMAE + Fine-tune} \\
    \hline
    Dense & 66.1 & 75.9 & 77.9 & 54.5 & 54.0 & 58.3 & 76.6 & 55.1 & 57.0 & 53.9 & 70.1 & 66.9 & 66.9 & 74.8 & 86.1 & 79.5 & 61.9 & 52.7 & 67.5 \\
    \hline
    \multicolumn{20}{l}{RetroMAE + Unsup + Fine-tune} \\
    \hline
    Dense & 69.2 & 78.4 & 80.0 & 56.9 & 56.1 & 60.9 & 78.6 & 58.3 & 59.5 & 56.1 & 72.8 & 69.9 & 70.1 & 78.7 & 86.2 & 82.6 & 62.7 & 56.7 & 81.8 \\
    \hline
    % \ChangeRT{1pt}
    \end{tabular}
    % \vspace{-5pt}
    \caption{Ablation study of multi-stage training on the MIRACL dev set (nDCG@10).}
    % \vspace{-10pt}
    \label{tab:stage_ablation}
\end{table*}
```

