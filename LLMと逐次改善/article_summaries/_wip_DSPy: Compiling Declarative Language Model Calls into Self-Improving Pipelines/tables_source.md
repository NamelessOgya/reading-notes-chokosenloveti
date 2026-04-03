# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[tp]
  \centering

  \caption{Results with in-context learning on HotPotQA multi-hop retrieval question answering. We report answer exact match (Ans) and pair-retrieval accuracy (Psg). Each row represents a separate pipeline: the module in the Program column is compiled against the examples in the Training set. The programs, compilers, and (small) training sets are defined in the main text. For HotPotQA, we use the training set (and not dev) directly for cross-validation. $^*$The marked result is evaluated on 50\% of our test set due to cost.}

  \vspace{2mm}
    
  \scalebox{0.85}{
  \begin{tabular}{l l c c c c c c c c}
    \toprule
    && \multicolumn{4}{c}{GPT-3.5} & \multicolumn{4}{c}{Llama2-13b-chat} \\
    \cmidrule(lr){3-6} \cmidrule(lr){7-10}
    Program & Compiler & \multicolumn{2}{c}{Dev} & \multicolumn{2}{c}{Test} & \multicolumn{2}{c}{Dev} & \multicolumn{2}{c}{Test} \\
    & & Ans & Psg & Ans & Psg & Ans & Psg & Ans & Psg \\
    \midrule
    \multirow{1}{*}{vanilla} 
    & fewshot   & 34.3 & n/a & 31.5 & n/a & 27.5 & n/a & 21.8 & n/a \\
    \midrule
    \multirow{2}{*}{\texttt{CoT\_RAG}}     
    & fewshot   & 36.4 & 36.0 & 29.8 & 34.4 & 34.5 & 36.0 & 28.0 & 34.4 \\
    & bootstrap & 42.3 & 36.0 & -- & -- & 38.3 & 36.0 & 32.9 & 34.4 \\
    \midrule
    \multirow{4}{*}{\texttt{react}} 
    & none           & 20.3 & -- & -- & -- & 20.0 & -- & -- & -- \\
    & +human\_r   & 33.0 & -- & -- & -- & 28.3 & -- & -- & -- \\
    & bootstrap & 31.0 & -- & -- & -- & 24.7 & -- & -- & -- \\
    & bootstrap$\times$2 & 39.0 & -- & -- & -- & 40.0 & -- & -- & -- \\
    \midrule
    \multirow{3}{*}{\texttt{multihop}} 
    & fewshot   & 36.9 & 38.3 & 31.2 & 40.8 & 34.7 & 32.0 & 31.3 & 30.8 \\
    & bootstrap & \textbf{48.7} & \textbf{47.0} & \textbf{39.6} & \textbf{43.8} & \textbf{42.0} & \textbf{48.3} & \textbf{36.4} & \textbf{43.5} \\
    & ensemble  & \textbf{54.7} & -- & \textbf{45.6}$^*$ & -- & \textbf{50.0} & -- & \textbf{41.0} & -- \\
    \bottomrule
  \end{tabular}
  }
  \label{tab:hotpotqa-results}

\vspace{-3mm}
\end{table}
```

## Table 2
```latex
\begin{table}[tp]
\small
  \centering

  \caption{Results with in-context learning on GSM8K math word problems. Each row represents a separate pipeline: the module in the Program column is compiled against the examples in the Training set. The programs, compilers, and (small) training sets are defined in Section~\ref{sec:mw}. %
  Rows with \texttt{ensemble} build on the immediately preceding row. Notably, all programs in this table are expressed by composing two to four DSPy modules and teleprompters. Compiling the correct \textit{modules}, instead of string prompts, improves different LMs from 4--20\% accuracy to 49--88\% accuracy.}

  \vspace{1mm}
  
    \scalebox{0.88}{
    \begin{tabular}{l l l r r r r}
    \toprule
    &&& \multicolumn{2}{c}{GPT-3.5} & \multicolumn{2}{c}{Llama2-13b-chat} \\
    \cmidrule(lr){4-5} \cmidrule(lr){6-7}
    Program & Compilation & Training & Dev & Test & Dev & Test \\
    \midrule
    \multirow{5}{*}{\texttt{vanilla}}
    &  none      & n/a     & 24.0 & 25.2 & 7.0 & 9.4 \\
    & \texttt{fewshot}   & \texttt{trainset}     & 33.1 & -- & 4.3 & -- \\
    & \texttt{bootstrap}   & \texttt{trainset}      & 44.0 & -- & 28.0 & -- \\
    & \texttt{bootstrap}$\times2$   & \texttt{trainset}      & 64.7 & 61.7 & 37.3 & 36.5 \\
    & +\texttt{ensemble}   & \texttt{trainset}      & 62.7 & 61.9 & 39.0 & 34.6 \\
    \midrule
    \multirow{5}{*}{\texttt{CoT}}     
    &  none          & n/a     & 50.0 &  --  & 26.7 & -- \\
    & \texttt{fewshot}   & \texttt{trainset}      & 63.0 & -- & 27.3 & -- \\
    & \texttt{fewshot}   & +\texttt{human\_CoT} & 78.6 & 72.4 & 34.3 & 33.7 \\
    & \texttt{bootstrap} & \texttt{trainset}      & 80.3 & 72.9 & 43.3 & -- \\
    & +\texttt{ensemble}  & \texttt{trainset}      & \textbf{88.3} & 81.6 & 43.7 & -- \\
    \midrule
    \multirow{4}{*}{\texttt{reflection}} 
    & none  & n/a & 65.0 & -- & 36.7 & -- \\
    & \texttt{fewshot} & \texttt{trainset} & 71.7 & -- & 36.3 & -- \\
    & \texttt{bootstrap} & \texttt{trainset}  & 83.0 & 76.0 & 44.3 & 40.2 \\
    & +\texttt{ensemble}& \texttt{trainset}  & 86.7 & -- & \textbf{49.0} & \textbf{46.9} \\
    \bottomrule
  \end{tabular}
     }
    
  \label{tab:math-results}

\end{table}
```

