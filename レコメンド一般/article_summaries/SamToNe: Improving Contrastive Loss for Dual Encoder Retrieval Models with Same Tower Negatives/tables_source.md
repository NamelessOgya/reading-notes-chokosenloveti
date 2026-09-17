# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[!th]
\centering
\adjustbox{max width=\textwidth}{
\begin{tabular}{c|c|cc|cc|cc|cc|cc|cc}
\toprule
    \multirow{2}{*}{\textbf{Model}} & 
    \multirow{2}{*}{\textbf{Loss}} & 
    \multicolumn{2}{c|}{\textbf{MSMARCO}} & 
    \multicolumn{2}{c|}{\textbf{NQ}} &
    \multicolumn{2}{c|}{\textbf{SQuAD}} & 
    \multicolumn{2}{c|}{\textbf{TriviaQA}} & 
    \multicolumn{2}{c|}{\textbf{SearchQA}} & 
    \multicolumn{2}{c}{\textbf{Average}} \\
    & & 
    \textbf{P@1} & \textbf{MRR} & 
    \textbf{P@1} & \textbf{MRR} &
    \textbf{P@1} & \textbf{MRR} & 
    \textbf{P@1} & \textbf{MRR} & 
    \textbf{P@1} & \textbf{MRR} & 
    \textbf{P@1} & \textbf{MRR} \\
\hline \hline
    \multirow{2}{*}{\textbf{ADE}} 
    & Standard\rule{0pt}{2.6ex} & 
    $14.1$ & $26.8$ &
    $53.5$ & $65.2$ & 
    $64.3$ & $74.0$ & 
    $37.9$ & $50.4$ & 
    $41.5$ & $57.2$ & 
    $42.3$ & $54.7$ \\
    & SamToNe & 
    $16.0$ & $28.5$ &
    $52.8$ & $63.9$ & 
    $63.6$ & $73.0$ & 
    $38.4$ & $49.8$ & 
    $\mathbf{49.2}$ & $62.3$ & 
    $44.0$ & $55.5$ \\
    \midrule
    \multirow{3}{*}[-3pt]{\textbf{ADE-SPL}} 
    & Standard &
    $15.7$ & $28.8$ &
    $55.3$ & $67.0$ & 
    $74.5$ & $\mathbf{82.1}$ & 
    $41.7$ & $54.4$ & 
    $42.3$ & $59.1$ &
    $45.9$ & $58.3$ \\
    & SamToNe &
    $\mathbf{17.6}$ & $\mathbf{30.4}$ &
    $\mathbf{55.7}$ & $\mathbf{67.2}$ &
    $73.8$ & $81.7$ &
    $44.0$ & $55.9$ & 
    $48.5$ & $\mathbf{63.4}$ & 
    $\mathbf{47.9}$  & $\mathbf{59.7}$ \\
    \cmidrule{2-14}
    & PAIR & 
    $16.9$ & $29.6$ &
    $55.7$ & $67.0$ & 
    $74.4$ & $82.0$ & 
    $\mathbf{45.0}$ & $\mathbf{56.8}$ & 
    $44.1$ & $60.4$ & 
    $47.2$ & $59.2$ \\
    \midrule
    \multirow{3}{*}[-3pt]{\textbf{SDE}} 
    & Standard &
    $16.1$ & $29.1$ &
    $54.4$ & $66.6$ &
    $74.1$ & $81.9$ &
    $41.4$ & $54.2$ &
    $37.6$ & $55.8$ &
    $44.7$ & $57.5$ \\
    & SamToNe &
    $17.2$ & $30.2$ &
    $54.2$ & $66.4$ &
    $\mathbf{74.6}$ & $\mathbf{82.0}$ &
    $42.1$ & $54.5$ &
    $44.0$ & $60.4$ & 
    $46.4$ & $58.7$ \\
    \cmidrule{2-14}
    & PAIR & 
    $16.1$ & $29.1$ &
    $53.8$ & $66.2$ & 
    $74.13$ & $81.7$ & 
    $41.3$ & $54.5$ & 
    $38.7$ & $56.6$ & 
    $44.7$ & $57.5$ \\
\bottomrule
\end{tabular}
}
\caption{\label{table:qa-retrieval-results} 
\footnotesize
Precision at $1$ (P@1)($\%$) and Mean Reciprocal Rank (MRR)($\%$) on QA retrieval tasks. The best-performing models for each task and metric are highlighted in \textbf{bold}.
}
\vspace{-1em}
\end{table*}
```

## Table 2
```latex
\begin{table}[!t]
\centering
\adjustbox{max width=0.9\textwidth}{
\scriptsize
\begin{tabular}{c|c|c||c|c}
\toprule
\diagbox{Task}{Model} & 
\textbf{SDE} & \textbf{SamToNe} & 
\textbf{BM25} & \textbf{GTR-XXL} \\
\midrule
ArguAna & 
    $\underline{40.2}$ & $39.8$ &
    $31.5$ & $\mathbf{54}$ \\
BioASQ &
    $\underline{40.2}$ & $39.7$ &
    $\mathbf{46.5}$ & $32.4$ \\
Climate-Fever & 
    $31.1$ & $\mathbf{\underline{32}}$ & 
    $21.3$ & $26.7$ \\
CQADupStack & 
    $40.7$ & $\mathbf{\underline{41.4}}$ & 
    $29.9$ & $39.9$ \\
DBpedia-entity & 
    $45.7$ & $\mathbf{\underline{45.9}}$ & 
    $31.3$ & $40.8$ \\
Fever & 
    $68.3$ & $\underline{70}$ & 
    $\mathbf{75.3}$ & $74$ \\
FiQA-2018 & 
    $41.8$ & $\underline{42.6}$ & 
    $23.6$ & $\mathbf{46.7}$ \\
HotpotQA & 
    $\mathbf{\underline{66.9}}$ & 
    $66.4$ & $60.3$ & $59.9$ \\
NFCorpus & 
    $\mathbf{\underline{37.2}}$ & $36.5$ & 
    $32.5$ & $34.2$ \\
NQ & 
    $42.9$ & $\underline{47}$ & 
    $29.9$ & $\mathbf{56.8}$ \\
Quora & 
    $\underline{88.8}$ & $88.7$ & 
    $78.9$ & $\mathbf{89.2}$ \\
Robust04 & 
    $53.5$ & $\mathbf{\underline{55.5}}$ & 
    $40.8$ & $50.6$ \\
SCIDOCS & 
    $22.3$ & $\mathbf{\underline{22.4}}$ & 
    $15.8$ & $15.9$ \\
SciFact & 
    $\mathbf{\underline{68}}$ & $67.7$ & 
    $66.5$ & $66.2$ \\
Signal-1M & 
    $\underline{31.8}$ & $31.1$ & 
    $\mathbf{33}$ & $27.3$ \\
Trec-Covid &
    $53.1$ & $\underline{61.2}$ & 
    $\mathbf{65.6}$ & $50.1$ \\
Trec-News & 
    $\mathbf{\underline{49.2}}$ & $48.4$ &
    $39.8$ & $34.6$ \\
Touché-2022 & 
    $22$ & $\mathbf{\underline{32.4}}$ &
    $36.7$ & $25.6$ \\
\midrule
Average & 
    $46.9$ & $\mathbf{48.3}$ & 
    $42.3$ & $45.8$ \\
\bottomrule
\end{tabular}
}
\caption{\label{table:beir-results} 
\footnotesize
NDCG@10 for zero-shot evaluation on the BEIR benchmark after fine-tuning on MSMarco. The best-performing models for each task are highlighted in \textbf{bold}, while the best scores between \textbf{SDE} and \textbf{SDE~w/~SamToNe} are \underline{underscored}.
}
\vspace{-1em}
\end{table}
```

## Table 3
```latex
\begin{table}[!t]
\centering
\adjustbox{max width=0.9\textwidth}{
\scriptsize
\begin{tabular}{c|cc|cc}
\toprule
    \multirow{2}{*}{SamToNe} 
    & \multicolumn{2}{c|}{MSMARCO}
    & \multicolumn{2}{c}{TriviaQA}  \\
    & P@1 & MRR & P@1 & MRR \\
\midrule
    W/O SamToNe & $15.7$ & $28.8$ & $41.7$ & $54.4$ \\
    uni-directional & $17.6$ & $30.4$ & $\mathbf{44.0}$ & $\mathbf{55.9}$ \\
    bidirectional & $\mathbf{18.2}$ & $\mathbf{31.0}$ & $41.7$ & $53.3$ \\
\midrule
    $\%$ of unique documents 
    & \multicolumn{2}{c|}{$98\%$} 
    & \multicolumn{2}{c}{$17\%$} \\
\bottomrule
\end{tabular}
}
\caption{
    \label{table:doc-level-samtone} 
    \footnotesize
    Precision at $1$ (P@1)($\%$) and Mean Reciprocal Rank (MRR)($\%$) when comparing ADE-SPL (\texttt{t5.1.1-large} size) trained without SamToNe and with SamToNe applied to the query tower (\textit{uni-directional}) or to both towers (\textit{bidirectional}). The best-performing models for each task and metric are highlighted in \textbf{bold}.
}
\vspace{-1em}
\end{table}
```

## Table 4
```latex
\begin{table*}[!t]
\centering
\adjustbox{max width=\textwidth}{
\begin{tabular}{c|c|c|cc|cc|cc|cc|cc|cc}
\toprule
\multirow{2}{*}{\textbf{Model size}} & \multirow{2}{*}{\textbf{Architecture}} & \multirow{2}{*}{\textbf{SamToNe}} & \multicolumn{2}{c}{\textbf{MSMARCO}}        & \multicolumn{2}{c}{\textbf{NQ}}           & \multicolumn{2}{c}{\textbf{SQuAD}}        & \multicolumn{2}{c}{\textbf{TriviaQA}}      & \multicolumn{2}{c}{\textbf{SearchQA}}       & \multicolumn{2}{c}{\textbf{Average}} \\
                                     &                                        &                                   & \textbf{P@1}          & \textbf{MRR}        & \textbf{P@1}        & \textbf{MRR}        & \textbf{P@1}         & \textbf{MRR}       & \textbf{P@1}         & \textbf{MRR}        & \textbf{P@1}         & \textbf{MRR}         & \textbf{P@1}      & \textbf{MRR}     \\
\midrule
\multirow{6}{*}{\textbf{base}}       & \multirow{2}{*}{\textbf{ADE}}          & \textbf{No}                       & $13.8$                & $25.8$              & $48.7$              & $60.1$              & $60.9$               & $70.7$             & $35$                 & $46.3$              & $41.7$               & $57.1$               & $40$              & $52$             \\
                                     &                                        & \textbf{Yes}                      & $15.1$                & $27.1$              & $46.1$              & $57.$               & $59$                 & $68.9$             & $32.5$               & $43.1$              & $45.3$               & $58.5$               & $39.6$            & $50.9$           \\
                                     & \multirow{2}{*}{\textbf{ADE-SPL}}      & \textbf{No}                       & $15.4$                & $28.$               & $50.5$              & $62.1$              & $69.8$               & $78.1$             & $38.8$               & $50.7$              & $41.6$               & $58.$                & $43.2$            & $55.4$           \\
                                     &                                        & \textbf{Yes}                      & $\mathbf{16}$         & $\mathbf{28.7}$     & $\mathbf{50.9}$     & $\mathbf{62.3}$     & $69.9$               & $78.1$             & $\mathbf{40.4}$      & $\mathbf{51.7}$     & $\mathbf{45.8}$      & $\mathbf{60.9}$      & $\mathbf{44.6}$   & $\mathbf{56.3}$  \\
                                     & \multirow{2}{*}{\textbf{SDE}}          & \textbf{No}                       & $15.7$                & $28.1$              & $49.3$              & $61.4$              & $70.2$               & $\mathbf{78.5}$    & $37.7$               & $50.4$              & $36.9$               & $54.8$               & $42$              & $54.6$           \\
                                     &                                        & \textbf{Yes}                      & $15.9$                & $28.4$              & $49.7$              & $61.6$              & $\mathbf{70.4}$      & $0.784$            & $39.4$               & $51.5$              & $41.1$               & $57.8$               & $43.3$            & $55.5$           \\
\midrule
\multirow{6}{*}{\textbf{large}}      & \multirow{2}{*}{\textbf{ADE}}          & \textbf{No}                       & $14.1$                & $26.8$              & $53.5$              & $65.2$              & $64.3$               & $74$               & $37.9$               & $50.4$              & $41.5$               & $57.2$               & $42.3$            & $54.7$           \\
                                     &                                        & \textbf{Yes}                      & $16$                  & $28.5$              & $52.8$              & $63.9$              & $63.6$               & $73$               & $38.4$               & $49.8$              & $49.2$               & $62.3$               & $44$              & $55.5$           \\
                                     & \multirow{2}{*}{\textbf{ADE-SPL}}      & \textbf{No}                       & $15.7$                & $28.8$              & $55.3$              & $67$                & $74.5$               & $\mathbf{82.1}$    & $41.7$               & $54.4$              & $42.3$               & $59.1$               & $45.9$            & $58.3$           \\
                                     &                                        & \textbf{Yes}                      & $\mathbf{17.6}$       & $\mathbf{30.4}$     & $\mathbf{55.7}$     & $\mathbf{67.2}$     & $0.738$              & $0.817$            & $\mathbf{44}$        & $\mathbf{55.9}$     & $\mathbf{48.5}$      & $\mathbf{63.4}$      & $\mathbf{47.9}$   & $\mathbf{59.7}$  \\
                                     & \multirow{2}{*}{\textbf{SDE}}          & \textbf{No}                       & $16.1$                & $29.1$              & $54.4$              & $66.6$              & $74.1$               & $81.9$             & $41.4$               & $54.2$              & $37.6$               & $55.8$               & $44.7$            & $57.5$           \\
                                     &                                        & \textbf{Yes}                      & $17.2$                & $30.2$              & $54.2$              & $66.4$              & $\mathbf{74.6}$      & $82$               & $42.1$               & $54.5$              & $44$                 & $60.4$               & $46.4$            & $58.7$           \\
\midrule
\multirow{6}{*}{\textbf{XXL}}        & \multirow{2}{*}{\textbf{ADE}}          & \textbf{No}                       & $14.9$                & $27.9$              & $57.2$              & $69.2$              & $68.7$               & $77.8$             & $46.1$               & $58.7$              & $47.4$               & $62.7$               & $46.9$            & $59.3$           \\
                                     &                                        & \textbf{Yes}                      & $17$                  & $30$                & $57.5$              & $69$                & $67.7$               & $76.9$             & $47$                 & $58.8$              & $52.7$               & $65.9$               & $48.4$            & $60.1$           \\
                                     & \multirow{2}{*}{\textbf{ADE-SPL}}      & \textbf{No}                       & $16.2$                & $29.6$              & $58.7$              & $70.6$              & $\mathbf{78.3}$      & $\mathbf{85.3}$    & $\mathbf{50.9}$      & $\mathbf{63}$       & $45.7$               & $62.3$               & $50$              & $62.2$           \\
                                     &                                        & \textbf{Yes}                      & $\mathbf{17.7}$       & $\mathbf{31.2}$     & $\mathbf{59.8}$     & $\mathbf{71.4}$     & $77.9$               & $84.8$             & $50.1$               & $61.6$              & $\mathbf{51.9}$      & $\mathbf{66.5}$      & $\mathbf{51.5}$   & $\mathbf{63.1}$  \\
                                     & \multirow{2}{*}{\textbf{SDE}}          & \textbf{No}                       & $15.8$                & $29.4$              & $58.2$              & $70.6$              & $79.2$               & $86$               & $46.9$               & $60.3$              & $40.6$               & $59$                 & $48.1$            & $61.1$           \\
                                     &                                        & \textbf{Yes}                      & $17.1$                & $30.6$              & $58.7$              & $70.8$              & $78.2$               & $85.1$             & $48.3$               & $60.6$              & $46.5$               & $62.8$               & $49.8$            & $62$             \\
\midrule
\multicolumn{3}{c}{Dataset Size (train / test queries / test documents)}                                          & \multicolumn{2}{c}{400776 / 6980 / 8841823} & \multicolumn{2}{c}{106521 / 4131 / 22118} & \multicolumn{2}{c}{87133 / 10485 / 10642} & \multicolumn{2}{c}{335659 / 7776 / 238339} & \multicolumn{2}{c}{629160 / 16476 / 454836} &                   &                 
              
\\
\bottomrule
\end{tabular}
}
\caption{\label{appendix-table:qa-retrieval-results} 
\footnotesize
Precision at $1$(P@1)($\%$) and Mean Reciprocal Rank (MRR)($\%$) on QA retrieval tasks. 
}
\vspace{-1em}
\end{table*}
```
