# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\centering
\small
\caption{Statistics of Datasets. }
\vspace{-12pt}
\label{tab:data_statis}
\begin{small}
\begin{tabular}{lrrr}
\toprule
Dataset& MovieLens & Steam & LastFM \\
\midrule
\# Sequence & 943 & 11,938 & 1,220 \\ 
\# Item & 1,682 & 3,581 & 4,606 \\ 
\# Interaction & 100,000 & 274,726 & 73,510 \\ 
\bottomrule
\end{tabular}
\end{small}
\vspace{-12pt}
\end{table}
```

## Table 2
```latex
\begin{table*}[t]
\centering
\caption{The Results of LLaRA compared with traditional sequential recommender models and LLMs-based methods. Bold and underlined indicate the best and the second-best performance, respectively. *($p$-value $<< 0.05$).}
\vspace{-5pt}
\label{tab:RQ1_res}
\small
\begin{tabular}{lccccccc}
\toprule
\multicolumn{2}{c}{\multirow{2}{*}{}}                                          & \multicolumn{2}{c}{MovieLens$^*$}                                                  & \multicolumn{2}{c}{Steam$^*$} & \multicolumn{2}{c}{LastFM}\\ 
%\cline{3-8}
% \midrule
\multicolumn{2}{c}{}                                                           & \multicolumn{1}{c}{ValidRatio} & HitRatio@1    & \multicolumn{1}{c}{ValidRatio} & HitRatio@1    & \multicolumn{1}{c}{ValidRatio} & HitRatio@1\\ 
\midrule
\multicolumn{1}{l}{\multirow{3}{*}{Traditional}} & GRU4Rec                     & \multicolumn{1}{c}{1.0000}     & 0.3750  & \multicolumn{1}{c}{1.0000}     & 0.4168  & \multicolumn{1}{c}{1.0000}     & 0.2616 \\ 
\multicolumn{1}{l}{}                             & Caser                       & \multicolumn{1}{c}{1.0000}     & 0.3861  & \multicolumn{1}{c}{1.0000}     & 0.4368 & \multicolumn{1}{c}{1.0000} & 0.2233  \\ 
\multicolumn{1}{l}{}                             & SASRec          & \multicolumn{1}{c}{1.0000}     & 0.3444  & \multicolumn{1}{c}{1.0000}     & 0.4010 & \multicolumn{1}{c}{1.0000} & 0.2233 \\ 
\midrule
\multicolumn{1}{l}{\multirow{4}{*}{LLM-based}}         & Llama2                     & \multicolumn{1}{c}{0.4421}  &    0.0421        & \multicolumn{1}{c}{0.1653}     & 0.0135 & \multicolumn{1}{c}{0.3443} & 0.0246\\ 
\multicolumn{1}{l}{}                             & GPT-4                       & \multicolumn{1}{c}{0.9895}     & 0.2000        & \multicolumn{1}{c}{0.9798}     & 0.3626 & \multicolumn{1}{c}{1.0000} & 0.3770 \\  
\multicolumn{1}{l}{}                             & MoRec                         & \multicolumn{1}{c}{1.0000}           & 0.2822& \multicolumn{1}{c}{1.0000}           & 0.3911 & \multicolumn{1}{c}{1.0000} & 0.1652\\ 
\multicolumn{1}{l}{}                             & TALLRec                     & \multicolumn{1}{c}{0.9263}     & 0.3895 & \multicolumn{1}{c}{0.9840}     &0.4637 & \multicolumn{1}{c}{0.9836} & 0.4180\\ 
\midrule
\multicolumn{1}{l}{\multirow{3}{*}{Ours}}        & LLaRA (GRU4Rec)             & \multicolumn{1}{c}{0.9684}     & \underline{0.4421}& \multicolumn{1}{c}{0.9975}     &\underline{0.4924} & \multicolumn{1}{c}{0.9836} & \underline{0.4344}\\ 
\multicolumn{1}{l}{}                             & LLaRA (Caser)               & \multicolumn{1}{c}{0.9684}     & \textbf{0.4737} & \multicolumn{1}{c}{0.9966} & 0.4874 & \multicolumn{1}{c}{0.9918} & \underline{0.4344}\\ 
\multicolumn{1}{l}{}                             & LLaRA (SASRec)              & \multicolumn{1}{c}{0.9684}     & \underline{0.4421} & \multicolumn{1}{c}{0.9975}     &\textbf{0.4949} & \multicolumn{1}{c}{1.0000} & \textbf{0.4508}\\ 
\bottomrule
\end{tabular}
\vspace{-5pt}
\end{table*}
```

## Table 3
```latex
\begin{table}[t]
\centering
\caption{The HitRatio@1 of LLaRA compared with other learning strategies. CL denotes curriculum learning and bold indicates the best performance.}
\vspace{-8pt}
\label{tab:RQ3_res}
\small
\begin{tabular}{lccc}
\toprule
       & \multicolumn{1}{c}{MovieLens} & \multicolumn{1}{c}{Steam} & \multicolumn{1}{c}{LastFM}   \\
\midrule
Direct  & 0.4211 & 0.4899 & \textbf{0.4508}\\
Two-stage  & 0.4316 & 0.4840 & 0.4344\\
LLaRA (CL) & \textbf{0.4421} & \textbf{0.4949} & \textbf{0.4508}\\
\bottomrule
\end{tabular}
\vspace{-12pt}
\end{table}
```

