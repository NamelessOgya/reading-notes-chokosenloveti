# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\caption{Statistics of the evaluation datasets.}
\vspace{-5pt}
\label{tab:dataStatics}
\centering
\renewcommand\arraystretch{1.1}
\resizebox{0.43\textwidth}{!}{%
\begin{tabular}{cccccc}
\hline
Dataset&\#Train&\#Valid&\#Test&\#User&\#Item
\\ \hline
ML-1M&33,891&10,401&7,331&839&3,256 \\
Amazon-Book&727,468&25,747&25,747&22,967&34,154\\\hline
% \#interactions&539,436& 737,163\\ \hline

\end{tabular}
\vspace{-5pt}
}
\end{table}
```

## Table 2
```latex
\begin{table*}[]
% \centering
% \caption{Overall performance comparison on the ML-1M and Amazon-Book datasets. "Collab." denotes collaborative recommendation methods. "Rel. Imp." denotes the relative improvement of CoLLM compared to baselines. For a collaborative method, the value is computed using CoLLM implemented on it. For LLMRec methods, the value is computed for CoLLM-MF.}
% \label{tab: overall-performance}
% \resizebox{0.8\textwidth}{!}{%
% \begin{tabular}{cc|ccc|ccc}
% \hline
% \multicolumn{2}{c|}{Dataset}                                 & \multicolumn{3}{c|}{ML-1M}                  & \multicolumn{3}{c}{Amazon-Book} \\ \hline
% \multicolumn{2}{c|}{Methods}                                 & UAUC          & AUC           & Rel. Imp. & UAUC    & AUC     & Rel. Imp. \\ \hline
% \multicolumn{1}{c|}{\multirow{4}{*}{Collab.}}       & MF           & 0.6361 & 0.6482 & 10.3\% & 0.5565 & 0.7134 & 12.8\% \\
% \multicolumn{1}{c|}{}                     & LightGCN         & 0.6499        & 0.5959        & 13.2\%      & 0.5639  & 0.7103  & 10.7\%      \\
% \multicolumn{1}{c|}{}                     & SASRec           & 0.6884        & 0.7078        & 1.9\%       & 0.5714  & 0.6887  & -           \\
% \multicolumn{1}{c|}{}                     & DIN              & 0.6459        & 0.7166        & 3.9\%       & 0.6145  & 0.8163  & 3.2\%       \\ \hline
% \multicolumn{1}{c|}{LM+Collab.}           & CTRL (DIN)       & 0.6492        & 0.7159        & 2.4\%       & 0.5996  & 0.8202  & 2.6\%       \\ \hline
% \multicolumn{1}{c|}{\multirow{3}{*}{LLMRec}} & ICL              &  0.5268            &   0.5320            &    33.8\%         & 0.4856       & 0.4820      & 48.2\%           \\
% \multicolumn{1}{c|}{}                     & Prompt4NR (Vicuna)        & 0.6739        & 0.7071        & 2.7\%       & 0.5881  & 0.7224  & 10.4\%      \\
% \multicolumn{1}{c|}{}                     & TALLRec          & 0.6818        & 0.7097        & 1.8\%       & 0.5983  & 0.7375  & 8.2\%       \\
%  \hline
% \multicolumn{1}{c|}{\multirow{4}{*}{\textbf{Ours}}} & CoLLM-MF & 0.6875 & 0.7295 & -      & 0.6225 & 0.8109 & -      \\
% \multicolumn{1}{c|}{}                     & CoLLM-LightGCN   & 0.6967        & 0.7100        & -           & 0.6149  & 0.7978  & -           \\
% \multicolumn{1}{c|}{}                     & CoLLM-SASRec & 0.6990        & 0.7235        & -           & 0.59       & 0.7726       & -           \\
% \multicolumn{1}{c|}{}                     & CoLLM-DIN    & 0.6897 & 0.7243 & -           & 0.6474  & 0.8245  & -           \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 3
```latex
\begin{table*}[ht]
% \centering
% \caption{Overall performance comparison on the ML-1M and Amazon-Book datasets. ``Collab.'' denotes collaborative recommendation methods. ``Rel. Imp.'' denotes the relative improvement of CoLLM compared to baselines, averaged over the two metrics. For a collaborative method, the Rel. Imp. is computed using CoLLM implemented on it. FFor LLMRec methods, it is determined by comparing them to CoLLM-MF.}
% \vspace{-8pt}
% \begin{tabular}{cc|ccc|ccc}
% \hline
% \multicolumn{2}{c|}{Dataset}                                       & \multicolumn{3}{c|}{ML-1M}  & \multicolumn{3}{c}{Amazon-Book} \\ \hline
% \multicolumn{2}{c|}{Methods}                                       & AUC    & UAUC   & Rel. Imp. & AUC      & UAUC    & Rel. Imp.  \\ \hline
% \multicolumn{1}{c|}{\multirow{4}{*}{Collab.}} & MF                 & 0.6482 & 0.6361 & 10.3\%    & 0.7134   & 0.5565  & 12.8\%     \\
% \multicolumn{1}{c|}{}                         & LightGCN           & 0.5959 & 0.6499 & 13.2\%    & 0.7103   & 0.5639  & 10.7\%     \\
% \multicolumn{1}{c|}{}                         & SASRec             & 0.7078 & 0.6884 & 1.9\%     & 0.6887   & 0.5714  & 8.4\%          \\
% \multicolumn{1}{c|}{}                         & DIN                & 0.7166 & 0.6459 & 3.9\%     & 0.8163   & 0.6145  & 3.2\%      \\ \hline
% \multicolumn{1}{c|}{LM+Collab.}               & CTRL (DIN)         & 0.7159 & 0.6492 & 2.4\%     & 0.8202   & 0.5996  & 2.6\%      \\ \hline
% \multicolumn{1}{c|}{\multirow{3}{*}{LLMRec}}  & ICL                & 0.5320 & 0.5268 & 33.8\%    & 0.4820   & 0.4856  & 48.2\%     \\
% \multicolumn{1}{c|}{}                         & Prompt4NR (Vicuna) & 0.7071 & 0.6739 & 2.7\%     & 0.7224   & 0.5881  & 10.4\%     \\
% \multicolumn{1}{c|}{}                         & TALLRec            & 0.7097 & 0.6818 & 1.8\%     & 0.7375   & 0.5983  & 8.2\%      \\ \hline
% \multicolumn{1}{c|}{\multirow{4}{*}{Ours}}    & CoLLM-MF        & 0.7295 & 0.6875 & -         & 0.8109   & 0.6225  & -          \\
% \multicolumn{1}{c|}{}                         & CoLLM-LightGCN  & 0.7100 & 0.6967 & -         & 0.7978   & 0.6149  & -          \\
% \multicolumn{1}{c|}{}                         & CoLLM-SASRec    & 0.7235 & 0.6990 & -         & 0.7746   & 0.5962    & -          \\
% \multicolumn{1}{c|}{}                         & CoLLM-DIN       & 0.7243 & 0.6897 & -         & 0.8245   & 0.6474  & -          \\ \hline
% \end{tabular}
% \label{mainexp}
% \end{table*}
```

## Table 4
```latex
\begin{table*}[ht]
% \centering
% % \caption{Overall performance comparison on the ML-1M and Amazon-Book datasets. ``Collab.'' denotes collaborative recommendation methods. ``Rel. Imp.'' denotes the relative improvement of CoLLM compared to baselines, averaged over the two metrics. For a collaborative method, the Rel. Imp. is computed using CoLLM implemented on it. For LLMRec methods, it is determined by comparing them to CoLLM-MF.}
% \caption{Overall performance comparison. ``Collab.'' denotes collaborative methods. ``Rel. Imp.'' denotes the relative improvement of CoLLM compared to baselines, averaged over the two metrics. For a collaborative method, the Rel. Imp. is computed using CoLLM implemented on it. For LLMRec methods, it is determined by comparing them to CoLLM-MF.}
% \vspace{-5pt}

% \begin{tabular}{cc|ccc|ccc}
% \hline
% \multicolumn{2}{c|}{Dataset}                                       & \multicolumn{3}{c|}{ML-1M}  & \multicolumn{3}{c}{Amazon-Book} \\ \hline
% \multicolumn{2}{c|}{Methods}                                       & AUC    & UAUC   & Rel. Imp. & AUC      & UAUC    & Rel. Imp.  \\ \hline
% \multicolumn{1}{c|}{\multirow{4}{*}{Collab.}} & MF                 & 0.6482 & 0.6361 & 10.3\%    & 0.7134   & 0.5565  & 12.8\%     \\
% \multicolumn{1}{c|}{}                         & LightGCN           & 0.5959 & 0.6499 & 13.2\%    & 0.7103   & 0.5639  & 10.7\%     \\
% \multicolumn{1}{c|}{}                         & SASRec             & 0.7078 & 0.6884 & 1.9\%     & 0.6887   & 0.5714  & 8.4\%          \\
% \multicolumn{1}{c|}{}                         & DIN                & 0.7166 & 0.6459 & 3.1\%     & 0.8163   & 0.6145  & 3.2\%      \\ 
% \hline
% \multicolumn{1}{c|}{LM+Collab.}               & CTRL (DIN)         & 0.7159 & 0.6492 & 2.9\%     & 0.8202   & 0.5996  & 4.2\%      \\ \hline
% \multicolumn{1}{c|}{\multirow{3}{*}{LLMRec}}  & ICL                & 0.5320 & 0.5268 & 33.8\%    & 0.4820   & 0.4856  & 48.2\%     \\
% \multicolumn{1}{c|}{}                         & Prompt4NR (Vicuna) & 0.7071 & 0.6739 & 2.7\%     & 0.7224   & 0.5881  & 10.4\%     \\
% \multicolumn{1}{c|}{}                         & TALLRec            & 0.7097 & 0.6818 & 1.8\%     & 0.7375   & 0.5983  & 8.2\%      \\ \hline
% \multicolumn{1}{c|}{\multirow{4}{*}{Ours}}    & CoLLM-MF        & 0.7295 & 0.6875 & -         & 0.8109   & 0.6225  & -          \\
% \multicolumn{1}{c|}{}                         & CoLLM-LightGCN  & 0.7100 & 0.6967 & -         & 0.7978   & 0.6149  & -          \\
% \multicolumn{1}{c|}{}                         & CoLLM-SASRec    & 0.7235 & 0.6990 & -         & 0.7746   & 0.5962    & -          \\
% \multicolumn{1}{c|}{}                         & CoLLM-DIN       & 0.7243 & 0.6897 & -         & 0.8245   & 0.6474  & -          \\ 
% \hline
% \end{tabular}
% \label{mainexp}
% % \vspace{-5pt}
% \end{table*}
```

## Table 5
```latex
\begin{table*}[]
\centering
% \caption{Overall performance comparison. ``Collab.'' denotes collaborative methods. ``Rel. Imp.'' denotes the relative improvement of CoLLM compared to baselines, averaged over the AUC and UAUC metrics. For a collaborative method "X" (X$\in$\{MF, LightGCN, SASRec, DIN\}), the Rel. Imp. is computed using CoLLM-X. For LLMRec methods, the Rel. Imp. is determined by comparing them to CoLLM-MF.}
\caption{Overall performance comparison. ``Collab.'' denotes collaborative methods. ``Rel. Imp.'' denotes the relative improvement of CoLLM compared to baselines, averaged over the AUC and UAUC metrics. For a collaborative method "X", the Rel. Imp. is computed using CoLLM-X; For LLMRec methods, it is determined by comparing them to CoLLM-MF.}
% \vspace{-5pt}
\resizebox{0.95\textwidth}{!}{
\begin{tabular}{cc|cccc|cccc}
\hline
\multicolumn{2}{c|}{Dataset}                                       & \multicolumn{4}{c|}{ML-1M}           & \multicolumn{4}{c}{Amazon-Book}      \\ \hline
\multicolumn{2}{c|}{Methods}                                       & AUC    & UAUC   & NDCG   & Rel. Imp. & AUC    & UAUC   & NDCG   & Rel. Imp. \\ \hline
\multicolumn{1}{c|}{\multirow{4}{*}{Collab.}} & MF                 & 0.6482 & 0.6361 & 0.8447 & 10.3\%    & 0.7134 & 0.5565 & 0.8194 & 12.8\%    \\
\multicolumn{1}{c|}{}                         & LightGCN           & 0.5959 & 0.6499 & 0.8564 & 13.2\%    & 0.7103 & 0.5639 & 0.8245 & 11.0\%    \\
\multicolumn{1}{c|}{}                         & SASRec             & 0.7078 & 0.6884 & 0.8612 & 1.9\%     & 0.6887 & 0.5714 & 0.8244 & 8.4\%     \\
\multicolumn{1}{c|}{}                         & DIN                & 0.7166 & 0.6459 & 0.8496 & 4.9\%     & 0.8163 & 0.6145 & 0.8419 & 3.2\%     \\ \hline
\multicolumn{1}{c|}{LM+Collab.}               & CTRL (DIN)         & 0.7159 & 0.6492 & 0.8559 & 4.6\%     & 0.8202 & 0.5996 & 0.8363 & 4.2\%     \\ \hline
\multicolumn{1}{c|}{\multirow{3}{*}{LLMRec}}  & ICL                & 0.5320 & 0.5268 & 0.8114 & 33.8\%    & 0.4820 & 0.4856 & 0.7917 & 48.2\%    \\
\multicolumn{1}{c|}{}                         & Prompt4NR (Vicuna) & 0.7071 & 0.6739 & 0.8663 & 2.7\%     & 0.7224 & 0.5881 & 0.8346 & 10.4\%    \\
\multicolumn{1}{c|}{}                         & TALLRec            & 0.7097 & 0.6818 & 0.8711 & 1.8\%     & 0.7375 & 0.5983 & 0.8361 & 8.2\%     \\ \hline
\multicolumn{1}{c|}{\multirow{4}{*}{Ours}}    & CoLLM-MF           & 0.7295 & 0.6875 & 0.8714 & -         & 0.8109 & 0.6225 & 0.8457 & -         \\
\multicolumn{1}{c|}{}                         & CoLLM-LightGCN     & 0.7100 & 0.6967 & 0.8740 & -         & 0.8026 & 0.6149 & 0.8411 & -         \\
\multicolumn{1}{c|}{}                         & CoLLM-SASRec       & 0.7235 & 0.6990 & 0.8765 & -         & 0.7746 & 0.5962 & 0.8361 & -         \\
\multicolumn{1}{c|}{}                         & CoLLM-DIN          & 0.7353 & 0.6923 & 0.8735 & -         & 0.8245 & 0.6474 & 0.8550 & -         \\ \hline
\end{tabular}
}
\label{mainexp}
\end{table*}
```

## Table 6
```latex
\begin{table}[]
% \centering
% \caption{}
% \label{tab:my-table}
% \resizebox{0.7\textwidth}{!}{%
% \begin{tabular}{c|ccc|ccc}
% \hline
% Dataset          & \multicolumn{3}{c|}{ML-1M} & \multicolumn{3}{c}{Amazon-Book} \\ \hline
% Methods          & uauc      & auc       &    & uauc        & auc        &      \\ \hline
% MF               & 0.6361    & 0.6482    &    & 0.5565      & 0.7134     &      \\
% LightGCN         & 0.6499    & 0.5959    &    & 0.5639      & 0.7103     &      \\
% SASRec           & 0.6884    & 0.7078    &    & 0.5714      & 0.6887     &      \\ \hline
% CTRL             & -         &           &    &             &            &      \\
% ICL              & -         &           &    &             &            &      \\
% TALLRec          & 0.6818    & 0.7097    &    & 0.5976      & 0.5976     &      \\ \hline
% CollabRec-MF     & 0.6875    & 0.7295    &    & 0.6225      & 0.8109     &      \\
% CollabRec-LGCN   & 0.6967    & 0.7100    &    & 0.6149      & 0.7978     &      \\
% CollabRec-SASRec & 0.6990    & 0.7235    &    &             &            &      \\ \hline
% \end{tabular}%
% }
% \end{table}
```

## Table 7
```latex
\begin{table*}[th]
% \centering
% \caption{}
% \label{tab:my-table}
% \resizebox{\textwidth}{!}{%
% \begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|}
% \hline
% Dataset & Methods & MF & LightGCN & SASRec & CTRL & ICL & TALLRec & CollabRec-MF & CollabRec-LGCN & CollabRec-SASRec \\ \hline
% \multirow{3}{*}{ML-1M}       & uauc & 0.6361 & 0.6499 & 0.6884 & - & - & 0.6818 & 0.6875 & 0.6967 & 0.6990 \\ \cline{2-11} 
%                              & auc  & 0.6482 & 0.5959 & 0.7078 &   &   & 0.7097 & 0.7295 & 0.7100 & 0.7235 \\ \cline{2-11} 
%                              &      &        &        &        &   &   &        &        &        &        \\ \hline
% \multirow{3}{*}{Amazon-Book} & UAUC & 0.5565 & 0.5639 & 0.5714 &   &   & 0.5976 & 0.6225 & 0.6149 &        \\ \cline{2-11} 
%                              & AUC  & 0.7134 & 0.7103 & 0.6887 &   &   & 0.5976 & 0.8109 & 0.7978 &        \\ \cline{2-11} 
%                              &      &        &        &        &   &   &        &        &        &        \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 8
```latex
\begin{table}[t]
\centering
\caption{
Results of the ablation studies over CoLLM with respect to the CIE module.
% that is designed for collaborative information modeling.
% Ablation studies over CoLLM with respect to the CIE module designed for collaborative information modeling.
}
% \vspace{-5pt}
\label{tab:my-table}
\centering
\resizebox{0.42\textwidth}{!}{%
\begin{tabular}{c|cc|cc}
\hline
Dataset       & \multicolumn{2}{c|}{ML-1M} & \multicolumn{2}{c}{Amazon-Book} \\ \hline
Methods       & AUC          & UAUC        & AUC            & UAUC           \\ \hline
CoLLM-MF & 0.7295       & 0.6875      & 0.8133         & 0.6314         \\ \hline
w/o CIE       & 0.7097       & 0.6818      & 0.7375         & 0.5983         \\ \hline
w/ UI-token   & 0.7214       & 0.6563      & 0.7273         & 0.5956         \\ \hline
\end{tabular}%
}
% \vspace{-8pt}
\label{tab:ab-model}
\end{table}
```

## Table 9
```latex
\begin{table}[t]
\centering
% \caption{Overall performance of CoLLM with different tuning strategies.}
\caption{Overall performance of CoLLM with different tuning strategies.}
% \vspace{-5pt}

\label{tab:ab-tuning-overall}
\resizebox{0.42\textwidth}{!}{%
\begin{tabular}{c|cc|cc}
\hline
Dataset        & \multicolumn{2}{c|}{ML-1M} & \multicolumn{2}{c}{Amazon-Book} \\ \hline
Tuning Methods & AUC          & UAUC        & AUC            & UAUC           \\ \hline
Default        & 0.7295       & 0.6875      & 0.8109         & 0.6225         \\ \hline
T1             & 0.7360       & 0.6946      & 0.8154         & 0.6139         \\ \hline
T2             & 0.7418       & 0.6906      & 0.8288         & 0.6352         \\ \hline
T3             & 0.7131       & 0.6661      & 0.8104         & 0.5753         \\ \hline
\end{tabular}%
}
% \vspace{-3pt}
\end{table}
```

## Table 10
```latex
\begin{table}[t]
\centering
% \caption{\zy{The training and inference time expenses of TALLRec and CoLLM-MF. The inference time represents the overall cost across the testing set. The "$\Delta$" denotes the relative cost improvement of CoLLM-MF in comparison to TALLRec. "Book" is short for "Amazon-book".}}
\caption{Training and Total Inference Time Comparison: TALLRec vs. CoLLM-MF. "$\Delta$" indicates the relative cost improvement of CoLLM-MF over TALLRec. "Book" is short for "Amazon-book".}
% \vspace{-8pt}
\label{tab:time-cost}
\resizebox{0.45\textwidth}{!}{%
\begin{tabular}{c|cc|cc}
\hline
 & \multicolumn{2}{c|}{Train Time} & \multicolumn{2}{c}{Inference Time} \\ \hline
Dataset & ML-1M & Book & ML-1M & Book \\ \hline
TALLRec & 32min &  354min & 72s & 360s \\
CoLLM-MF &  36min &  418min & 82s & 398s \\
$\Delta$ & 13\% & 18\% & 14\% & 11\% \\ \hline
\end{tabular}%
}
% \vspace{-10pt}
\end{table}
```

## Table 11
```latex
\begin{table*}[h]
% \centering
% \caption{the effect of tuning methods}
% \label{tab:ab-tuning}
% \resizebox{\textwidth}{!}{%
% \begin{tabular}{c|cccccc|cccccc}
% \hline
% Dataset        & \multicolumn{6}{c|}{ML-1M}                          & \multicolumn{6}{c}{Amazon-Book}                     \\ \hline
% tuning Methods & AUC    & UAUC   & w-AUC  & w-UAUC & c-AUC  & c-UAUC & AUC    & UAUC   & w-AUC  & w-UAUC & c-AUC  & c-UAUC \\ \hline
% Default        & 0.7295 & 0.6875 & 0.7545 & 0.7041 & 0.6938 & 0.5830 & 0.8109 & 0.6225 & 0.8217 & 0.6229 & 0.7852 & 0.6294 \\ \hline
% T1             & 0.7301/0.7360 & 0.6933/0.6946 & 0.7614/0.7661 & 0.7101/0.7071 & 0.6947/0.6967 & 0.6119/0.6159 & 0.8154 & 0.6139 & 0.8202 & 0.6183 & 0.8026 & 0.6139 \\ \hline
% T2             & 0.7418 & 0.6906 & 0.7713 & 0.6998 & 0.7002 & 0.5889 & 0.8288 & 0.6352 & 0.8298 & 0.6297 & 0.8212 & 0.6625 \\ \hline
% T3             & 0.7131 & 0.6661 & 0.7599 & 0.6977 & 0.6401 & 0.5421 & 0.8104 & 0.5753 & 0.8148 & 0.6020 & 0.7889 & 0.5024 \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 12
```latex
\begin{table*}[ht]
% \centering
% \caption{}
% \label{tab:my-table}
% \resizebox{0.6\textwidth}{!}{%
% \begin{tabular}{|c|ccc|ccc|}
% \hline
% Dataset          & \multicolumn{3}{c|}{ML-1M}                                    & \multicolumn{3}{c|}{Amazon-Book}                              \\ \hline
% Methods          & \multicolumn{1}{c|}{UAUC}   & \multicolumn{1}{c|}{AUC}    &   & \multicolumn{1}{c|}{UAUC}   & \multicolumn{1}{c|}{AUC}    &   \\ \hline
% MF               & \multicolumn{1}{c|}{0.6361} & \multicolumn{1}{c|}{0.6482} & - & \multicolumn{1}{c|}{0.5565} & \multicolumn{1}{c|}{0.7134} & - \\ \hline
% LightGCN       & \multicolumn{1}{c|}{0.6499} & \multicolumn{1}{c|}{0.5959} & - & \multicolumn{1}{c|}{0.5639} & \multicolumn{1}{c|}{0.7103} & - \\ \hline
% SASRec           & \multicolumn{1}{c|}{0.6884} & \multicolumn{1}{c|}{0.7078} & - & \multicolumn{1}{c|}{0.5714} & \multicolumn{1}{c|}{0.6887} & - \\ \hline
% DIN             & \multicolumn{1}{c|}{0.6459}      & \multicolumn{1}{c|}{0.7166}       & - & \multicolumn{1}{c|}{0.6145}       & \multicolumn{1}{c|}{0.8163}       & - \\ \hline
% CTRL (DIN)             & \multicolumn{1}{c|}{0.6492}      & \multicolumn{1}{c|}{0.7159}       & - & \multicolumn{1}{c|}{0.5996}       & \multicolumn{1}{c|}{0.8202}       & - \\ \hline
% ICL              & \multicolumn{1}{c|}{-}      & \multicolumn{1}{c|}{}       &   & \multicolumn{1}{c|}{}       & \multicolumn{1}{c|}{}       & - \\ \hline
% TALLRec          & \multicolumn{1}{c|}{0.6818} & \multicolumn{1}{c|}{0.7097} & - & \multicolumn{1}{c|}{0.5983} & \multicolumn{1}{c|}{0.7375} & - \\ \hline

% Prompt4NR          & \multicolumn{1}{c|}{0.6739} & \multicolumn{1}{c|}{0.7071} & - & \multicolumn{1}{c|}{0.5881} & \multicolumn{1}{c|}{0.7224} & - \\ \hline

% CollabRec-MF   & \multicolumn{1}{c|}{0.6875} & \multicolumn{1}{c|}{0.7295} & - & \multicolumn{1}{c|}{0.6225} & \multicolumn{1}{c|}{0.8109} & - \\ \hline
% CollabRec-LGCN & \multicolumn{1}{c|}{0.6967} & \multicolumn{1}{c|}{0.7100} & - & \multicolumn{1}{c|}{0.6149} & \multicolumn{1}{c|}{0.7978} & - \\ \hline
% CollabRec-SASRec & \multicolumn{1}{c|}{0.6990} & \multicolumn{1}{c|}{0.7235} & - & \multicolumn{1}{c|}{0.6072/0.5962}       & \multicolumn{1}{c|}{0.7725/0.7742}       & - \\ \hline
% CollabRec-DIN & \multicolumn{1}{c|}{0.6834/0.6897} & \multicolumn{1}{c|}{0.7113/0.7243} & - & \multicolumn{1}{c|}{0.6474}       & \multicolumn{1}{c|}{0.8245}       & - \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 13
```latex
\begin{table*}[]
% \centering
% \caption{performance on cold and warm stat users and items. MF 
%  perform worse than TALLRec;}
% \label{tab:ab-model}
% \resizebox{\textwidth}{!}{%
% \begin{tabular}{c|cccc|cccc}
% \hline
% Dataset       & \multicolumn{4}{c|}{ML-1M}                  & \multicolumn{4}{c}{Amazon-Book}             \\ \hline
% Methods       & warm-auc & warm-uauc & cold-auc & cold-uauc & warm-auc & warm-uauc & cold-auc & cold-auc \\ \hline
% MF            & 0.7274   & 0.6627    & 0.5229   & 0.5594    & 0.7827   & 0.5727    & 0.5250    & 0.5081   \\ \hline
% TALLRec       & 0.7242   & 0.6992    & 0.6861   & 0.5996    & 0.7377   & 0.5808    & 0.7213    & 0.6404   \\ \hline
% CoLLM (MF) & 0.7545   & 0.7041    & 0.6938  & 0.5830    & 0.8217   & 0.6229    &      0.7852     &  0.6294        \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 14
```latex
\begin{table*}[]
% % \centering
% % \caption{performance on cold and warm stat users and items. MF 
% %  perform worse than TALLRec: drift perspective (10 month: 5 month: 5 month for training, validation, testing);}
% % \label{tab:my-table}
% % \resizebox{\textwidth}{!}{%
% % \begin{tabular}{c|cccc|cccc}
% % \hline
% % Dataset       & \multicolumn{4}{c|}{ML-1M}                  & \multicolumn{4}{c}{Amazon-Book}             \\ \hline
% % Methods       & warm-auc & warm-uauc & cold-auc & cold-uauc & warm-auc & warm-uauc & cold-auc & cold-auc \\ \hline
% % MF            & 0.7195   & 0.6616    & 0.5229   & 0.5594    & 0.7827   & 0.5727    & 0.5250    & 0.5081   \\ \hline
% % TALLRec       & 0.7253   & 0.6994    & 0.6861   & 0.5996    & 0.7377   & 0.5808    & 0.7213    & 0.6404   \\ \hline
% % CoLLM (MF) & 0.7527   & 0.7053    & 0.6938  & 0.5830    & 0.8217   & 0.6229    &      0.7852     &  0.6294        \\ \hline
% % \end{tabular}%
% % }
% % \end{table*}
```

## Table 15
```latex
\begin{table*}[]
% % \centering
% % \caption{}
% % \label{tab:my-table}
% % \resizebox{0.75\textwidth}{!}{%
% % \begin{tabular}{c|ccc|ccc|ccc}
% % \hline
% % Dataset &
% %   \multicolumn{3}{c|}{ML-1M} &
% %   \multicolumn{3}{c|}{Amazon-Book} &
% %   \multicolumn{3}{l|}{ML-100k} \\ \hline
% % Methods &
% %   \multicolumn{1}{c|}{uauc} &
% %   \multicolumn{1}{c|}{auc} &
% %    &
% %   \multicolumn{1}{c|}{uauc} &
% %   \multicolumn{1}{c|}{auc} &
% %    &
% %   \multicolumn{1}{l|}{} &
% %   \multicolumn{1}{l|}{} &
% %   \multicolumn{1}{l|}{} \\ \hline
% % MF &
% %   \multicolumn{1}{c|}{0.6361} &
% %   \multicolumn{1}{c|}{0.6482} &
% %   - &
% %   \multicolumn{1}{c|}{0.5565} &
% %   \multicolumn{1}{c|}{0.7134} &
% %   - &
% %   \multicolumn{1}{c|}{0.5565} &
% %   \multicolumn{1}{c|}{0.7134} &
% %   - \\ \hline
% % LightGCN &
% %   \multicolumn{1}{c|}{0.6499} &
% %   \multicolumn{1}{c|}{0.5959} &
% %   - &
% %   \multicolumn{1}{c|}{0.5639} &
% %   \multicolumn{1}{c|}{0.7103} &
% %   - &
% %   \multicolumn{1}{c|}{0.5639} &
% %   \multicolumn{1}{c|}{0.7103} &
% %   - \\ \hline
% % SASRec &
% %   \multicolumn{1}{c|}{0.6884} &
% %   \multicolumn{1}{c|}{0.7078} &
% %   - &
% %   \multicolumn{1}{c|}{0.5714} &
% %   \multicolumn{1}{c|}{0.6887} &
% %   - &
% %   \multicolumn{1}{c|}{0.5714} &
% %   \multicolumn{1}{c|}{0.6887} &
% %   - \\ \hline
% % CTRL &
% %   \multicolumn{1}{c|}{-} &
% %   \multicolumn{1}{c|}{} &
% %   - &
% %   \multicolumn{1}{c|}{} &
% %   \multicolumn{1}{c|}{} &
% %   - &
% %   \multicolumn{1}{c|}{} &
% %   \multicolumn{1}{c|}{} &
% %   - \\ \hline
% % ICL &
% %   \multicolumn{1}{c|}{-} &
% %   \multicolumn{1}{c|}{} &
% %    &
% %   \multicolumn{1}{c|}{} &
% %   \multicolumn{1}{c|}{} &
% %   - &
% %   \multicolumn{1}{c|}{} &
% %   \multicolumn{1}{c|}{} &
% %   - \\ \hline
% % TALLRec &
% %   \multicolumn{1}{c|}{0.6818} &
% %   \multicolumn{1}{c|}{0.7097} &
% %   - &
% %   \multicolumn{1}{c|}{0.5976} &
% %   \multicolumn{1}{c|}{0.5976} &
% %   - &
% %   \multicolumn{1}{c|}{0.5976} &
% %   \multicolumn{1}{c|}{0.5976} &
% %   - \\ \hline
% % CollabRec-MF &
% %   \multicolumn{1}{c|}{0.6875} &
% %   \multicolumn{1}{c|}{0.7295} &
% %   - &
% %   \multicolumn{1}{c|}{0.6225} &
% %   \multicolumn{1}{c|}{0.8109} &
% %   - &
% %   \multicolumn{1}{c|}{0.6225} &
% %   \multicolumn{1}{c|}{0.8109} &
% %   - \\ \hline
% % CollabRec-LGCN &
% %   \multicolumn{1}{c|}{0.6967} &
% %   \multicolumn{1}{c|}{0.7100} &
% %   - &
% %   \multicolumn{1}{c|}{0.6149} &
% %   \multicolumn{1}{c|}{0.7978} &
% %   - &
% %   \multicolumn{1}{c|}{0.6149} &
% %   \multicolumn{1}{c|}{0.7978} &
% %   - \\ \hline
% % CollabRec-SASRec &
% %   \multicolumn{1}{c|}{0.6990} &
% %   \multicolumn{1}{c|}{0.7235} &
% %   - &
% %   \multicolumn{1}{c|}{} &
% %   \multicolumn{1}{c|}{} &
% %   - &
% %   \multicolumn{1}{c|}{} &
% %   \multicolumn{1}{c|}{} &
% %   - \\ \hline
% % \end{tabular}%
% % }
% % \end{table*}
```

## Table 16
```latex
\begin{table*}[]
% \centering
% \caption{The effectiveness of the collaborative module}
% \label{tab:my-table}
% \resizebox{0.5\textwidth}{!}{%
% \begin{tabular}{c|cc|cc}
% \hline
% Dataset              & \multicolumn{2}{c|}{ML-1M} & \multicolumn{2}{c}{Amazon-Book} \\ \hline
% Methods              & uauc         & auc         & uauc           & auc            \\ \hline
% Personlized\_ptrompt & 0.65627      & 0.7214      & 0.5956         & 0.7273         \\ \hline
% CollabRec(MF)        & 0.6875       & 0.7295      & 0.6314         & 0.8133         \\ \hline
% \multicolumn{1}{l|}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l|}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 17
```latex
\begin{table*}[]
% \centering
% \caption{The effect of tuning selections}
% \label{tab:my-table}
% \resizebox{\textwidth}{!}{%
% \begin{tabular}{c|cllccc|cllccc}
% \hline
% Dataset                     & \multicolumn{6}{c|}{ML-1M}                                    & \multicolumn{6}{c}{Amazon-Book}                              \\ \hline
% tuning Methods              & auc    & uauc   & warm-auc & warm-uauc & cold-auc & cold-uauc & auc    & uauc   & warm-auc & warm-uauc & cold-auc & cold-auc \\ \hline
% lora then maping &
%   0.7295 &
%   0.6875 &
%   \multicolumn{1}{c}{0.7527} &
%   \multicolumn{1}{l}{0.7053} &
%   \multicolumn{1}{l}{0.6938} &
%   0.5830 &
%   0.8109 &
%   0.6225 &
%   0.8217 &
%   0.6229 &
%   0.7852 &
%   0.6294 \\ \hline
% lora then maping+random rec &        &        &          &           &          &           &        &        &          &           &          &          \\ \hline
% direct tuning lora+mapping  & 0.7131 & 0.6661 & 0.7599   & 0.6977    & 0.6401   & 0.5421    & 0.8104 & 0.5753 & 0.8148   & 0.6020    & 0.7889   & 0.5024   \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 18
```latex
\begin{table*}[]
% \centering
% \caption{The effect of tuning methods}
% \label{tab:my-table}
% \resizebox{\textwidth}{!}{%
% \begin{tabular}{c|cccccc|cccccc}
% \hline
% Dataset                  & \multicolumn{6}{c|}{ML-1M}                                    & \multicolumn{6}{c}{Amazon-Book}                              \\ \hline
% tuning Methods           & auc    & uauc   & warm-auc & warm-uauc & cold-auc & cold-uauc & auc    & uauc   & warm-auc & warm-uauc & cold-auc & cold-auc \\ \hline
% lora then maping         & 0.7295 & 0.6875 & 0.7545   & 0.7041    & 0.6938   & 0.5830    & 0.8109 & 0.6225 & 0.8217   & 0.6229    & 0.7852   & 0.6294   \\ \hline
% lora then maping+random rec & 0.7418 & 0.6906 & 0.7713 & 0.6998 & 0.7002 & 0.5889 & 0.8288 & 0.6352 & 0.8298 & 0.6297 & 0.8212 & 0.6625 \\ \hline
% direct tuning lora+mapping  & 0.7131 & 0.6661 & 0.7599 & 0.6977 & 0.6401 & 0.5421 & 0.8104 & 0.5753 & 0.8148 & 0.6020 & 0.7889 & 0.5024 \\ \hline
% lora then maping+pre rec & 0.7301 & 0.6933 & 0.7614   & 0.7101    & 0.6947   & 0.6119    & 0.8154 & 0.6139 & 0.8202   & 0.6183    & 0.8026   & 0.6139   \\ \hline
% \end{tabular}%
% }
% \end{table*}
```

## Table 19
```latex
\begin{table}
\caption{Performance comparison on Qwen2-1.5B backbone across ML-1M and Amazon-Book datasets.}
\vspace{-5pt}
\centering
\resizebox{0.45\textwidth}{!}{%
\begin{tabular}{l|ll|ll}
\hline
Dataset  & \multicolumn{2}{l|}{ML-1M} & \multicolumn{2}{l}{Amazon-Book} \\ \hline
Metric   & AUC          & UAUC        & AUC            & UAUC           \\ \hline
MF       & 0.6482       & 0.6361      & 0.7134         & 0.5565         \\
TALLRec  & 0.7027       & 0.6638      & 0.7256         & 0.5830         \\
CoLLM-MF & 0.7354       & 0.6950      & 0.8068         & 0.6147         \\ \hline
\end{tabular}
}
\label{tab:qwen2}
\end{table}
```

## Table 20
```latex
\begin{table*}[h]
\caption{Ensemble results on the AUC metric.}
\vspace{-5pt}
% \resizebox{0.49\textwidth}{!}{%
\centering
\resizebox{0.65\textwidth}{!}{%
\begin{tabular}{c|ccc|cc}
\hline
            & \multicolumn{3}{c|}{Single}     & \multicolumn{2}{c}{Ensemble} \\ \hline
Methods     & MF     & TALLRec & CoLLM-MF        & MF+TALLRec & MF+CoLLM-MF        \\ \hline
ML-1M       & 0.6482 & 0.7097  & {\ul 0.7295} & 0.7239     & \textbf{0.7364} \\
Amazon-book & 0.7134 & 0.7375  & {\ul 0.8109} & 0.7782     & \textbf{0.8112} \\ \hline
\end{tabular}
}
% }
% \vspace{-5pt}
\label{tab:ensemble}
\end{table*}
```

