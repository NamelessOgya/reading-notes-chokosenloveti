# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\caption{Statistics of the processed datasets.}
% \vspace{-5pt}
\label{tab:dataStatics}
\renewcommand\arraystretch{0.9}
\resizebox{0.49\textwidth}{!}{
\begin{tabular}{cccccc}
\hline
Dataset&\#Train&\#Valid&\#Test&\#User&\#Item
\\ \hline
ML-1M&33,891&10,401&7,331&839&3,256 \\
Amazon-Book&727,468&25,747&25,747&22,967&34,154\\\hline
% \#interactions&539,436& 737,163\\ \hline

\end{tabular}
}
% \vspace{-5pt}
\end{table}
```

## Table 2
```latex
\begin{table*}[th]
\caption{Overall performance comparison on the ML-1M and Amazon-Book datasets. ``Collab.'' denotes collaborative recommendation methods. ``Rel. Imp.'' denotes the relative improvement of BinLLM compared to baselines, averaged over the two metrics.}
% \vspace{-5pt}
\centering
\begin{tabular}{cc|ccc|ccc}
\hline
\multicolumn{2}{c|}{Dataset}                                       & \multicolumn{3}{c|}{ML-1M}  & \multicolumn{3}{c}{Amazon-Book} \\ \hline
\multicolumn{2}{c|}{Methods}                                       & AUC    & UAUC   & Rel. Imp. & AUC      & UAUC    & Rel. Imp.  \\ \hline
\multicolumn{1}{c|}{\multirow{4}{*}{Collab.}} & MF                 & 0.6482 & 0.6361 & 12.9\%    & 0.7134   & 0.5565  & 14.7\%     \\
\multicolumn{1}{c|}{}                         & LightGCN           & 0.5959 & 0.6499 & 15.8\%    & 0.7103   & 0.5639  & 14.2\%     \\
\multicolumn{1}{c|}{}                         & SASRec             & 0.7078 & 0.6884 & 3.0\%     & 0.6887   & 0.5714  & 15.3\%      \\
\multicolumn{1}{c|}{}                         & DIN                & 0.7166 & 0.6459 & 5.6\%     & 0.8163   & 0.6145  & 2.0\%      \\ \hline
\multicolumn{1}{c|}{LM+Collab.}               & CTRL (DIN)         & 0.7159 & 0.6492 & 5.4\%     & 0.8202   & 0.5996  & 3.0\%      \\ \hline
\multicolumn{1}{c|}{\multirow{3}{*}{LLMRec}}  & ICL                & 0.5320 & 0.5268 & 35.8\%    & 0.4820   & 0.4856  & 50.7\%     \\
\multicolumn{1}{c|}{}                         & Prompt4NR & 0.7071 & 0.6739 & 4.1\%     & 0.7224   & 0.5881  & 10.9\%     \\
\multicolumn{1}{c|}{}                         & TALLRec            & 0.7097 & 0.6818 & 3.3\%     & 0.7375   & 0.5983  & 8.2\%      \\ \hline
% \multicolumn{1}{c|}{LM+Collab.}               & CTRL (DIN)         & 0.7159 & 0.6492 & 2.9\%     & 0.8202   & 0.5996  & 4.2\%      \\ \hline
\multicolumn{1}{c|}{}                         & PersonPrompt             & 0.7214 & 0.6563 &  4.5\%          & 0.7273   & 0.5956  &    9.9\%        \\
\multicolumn{1}{c|}{LLMRec+Collab.}              & CoLLM-MF           & 0.7295 & 0.6875 & 1.5\%         & 0.8109   & 0.6225  & 1.7\%          \\
\multicolumn{1}{c|}{}                         & CoLLM-DIN          & 0.7243 & 0.6897 & 1.7\%         & 0.8245   & \textbf{0.6474}  & -1.0\%          \\ \hline
\multicolumn{1}{c|}{Ours}                     & BinLLM             &    \textbf{0.7425}    & \textbf{0.6956}       &    -       &    \textbf{0.8264}      & 0.6319        &  -          \\ \hline
\end{tabular}
\label{tab-main}
\end{table*}
```

## Table 3
```latex
\begin{table}[]
\caption{Results of the ablation studies on ML-1M and Amazon-Book, where ``TO", ``IO", ``IT" denote ``Text-Only", ``ID-Only", ``Intuitive-Tuning", respectively.  }
% \vspace{-5pt}
\resizebox{0.49\textwidth}{!}{
\begin{tabular}{c|cc|cc}
\hline
   Datasets             & \multicolumn{2}{c|}{ML-1M} & \multicolumn{2}{c}{Amazon-book} \\ \hline
Methods         & AUC          & UAUC        & AUC            & UAUC           \\ \hline
BinMF           & 0.7189       & 0.6654      & 0.8087         & 0.5895         \\
BinLLM-TO & 0.7097       & 0.6818      & 0.7375         & 0.5983         \\
BinLLM-IO   &      0.7307        & 0.6797            &  0.8173              &   0.5919             \\
BinLLM-IT       &      0.7286        &    0.6842         &     0.8246           &      0.6165          \\ \hline
BinLLM          & 0.7425       & 0.6956       & 0.8264         & 0.6319         \\ \hline
\end{tabular}
}
\label{tab-ablation}
% \vspace{-8pt}
\end{table}
```

## Table 4
```latex
\begin{table}
% \small
\centering
  \caption{
        Example of the used prompt template, using the same format as CoLLM.
    }
    % \vspace{-10pt}
 \label{tab:prompt-example}
    \begin{tabular}{p{7.5cm}}  
    \hline
        \#Question: A user has given high ratings to the following books: <ItemTitleList>. Additionally, we have information about the user's preferences encoded in the feature <UserID>. Using all available information, make a prediction about whether the user would enjoy the book titled <TargetItemTitle> with the feature <TargetItemID>? Answer with "Yes" or "No". \textbackslash n\#Answer:\\
    \hline
    \end{tabular}
\end{table}
```

