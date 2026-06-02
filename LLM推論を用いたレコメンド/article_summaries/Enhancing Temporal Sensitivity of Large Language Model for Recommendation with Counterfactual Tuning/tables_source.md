# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
  \centering
  \renewcommand\arraystretch{1.2}
  \caption{Statistical details of training datasets.}
  \label{exp:dataset}
  \begin{tabular}{lccc}
    \toprule
    Dataset     &MovieLens&Steam&LastFM   \\
    \midrule
    \#Sequences    &192,483  &151,056&46,897 \\
    \#Items        &  3,952  &  3,581&4,606 \\
    \#Interactions &999,611  &239,796& 73,510\\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 2
```latex
\begin{table*}[h]
  \centering
  \renewcommand\arraystretch{1.2}
  \setlength{\tabcolsep}{3pt} % 缩小列间距
  \small
  \caption{Performance of baselines and CETRec on MovieLens, Steam, and LastFM datasets.}
  \label{tab:performance}
  \begin{tabular}{lcccc|cccc|cccc}
    \toprule
     &\multicolumn{4}{c|}{MovieLens} 
     &\multicolumn{4}{c|}{Steam} 
     &\multicolumn{4}{c}{LastFM} \\
    \cmidrule(lr){2-5} \cmidrule(lr){6-9} \cmidrule(lr){10-13}
     &HR@5&NDCG@5&HR@10&NDCG@10 
     &HR@5&NDCG@5&HR@10&NDCG@10
     &HR@5&NDCG@5&HR@10&NDCG@10 \\
    \midrule
Caser          &0.0667&0.0399&0.1217&0.0573&0.0307&0.0200&0.0488&0.0258&0.0222&0.0145&0.0324&0.0177 \\
GRU4Rec        &0.0475&0.0283&0.0900&0.0417&0.0301&0.0198&0.0479&0.0255&0.0130&0.0079&0.0204&0.0103 \\
SASRec         &0.0542&0.0322&0.0917&0.0441&0.0269&0.0171&0.0450&0.0229&0.0194&0.0097&0.0352&0.0146 \\
P5             &0.0538&0.0334&0.0911&0.0452&0.0688&0.0468&0.1049&0.0583&0.0173&0.0138&0.0273&0.0171 \\
BIGRec
&0.0985&0.0614&0.1093&0.0650&0.0778&0.0530&0.0979&0.0596&0.0264&0.0192&0.0356&0.0221 \\
E4SRec
&0.1050&0.0660&0.1170&0.0700&0.0810&0.0555&0.0982&0.0615&0.0500&0.0325&0.0600&0.0355 \\
LLaRA
&0.1120&0.0710&0.1250&0.0750&0.0850&0.0580&0.0985&0.0635&0.0745&0.0450&0.0880&0.0490 \\
CFT
&0.1043&0.0623&0.1241&0.0691&0.0879&0.0606&0.1013&0.0650&0.0711& 0.0424&0.0838&0.0467 \\


\midrule
CETRec (SinPE) &0.1101&0.0693&0.1209&0.0728&0.0670&0.0436&0.0779&0.0471&0.0780&0.0520&0.0910&0.0550 \\
CETRec (RoPE)  &\textbf{0.1283}&\textbf{0.0779}&\textbf{0.1365}&\textbf{0.0806}&\textbf{0.0921}&\textbf{0.0641}&\textbf{0.1072}&\textbf{0.0690}&\textbf{0.0866}&\textbf{0.0591}&\textbf{0.1030}&\textbf{0.0646} \\
    \bottomrule
  \end{tabular}
\end{table*}
```

## Table 3
```latex
\begin{table*}[h]
  \centering
  \renewcommand\arraystretch{1.2}
    \setlength{\tabcolsep}{3pt}
  \small
  \caption{Ablation results with different positional embedding methods and training variants.}
  \label{tab:abla}
  \begin{tabular}{l lcccc|cccc|cccc}
    \toprule
     &\multicolumn{5}{c|}{MovieLens} 
     &\multicolumn{4}{c|}{Steam} 
     &\multicolumn{4}{c}{LastFM} \\
    \cmidrule(lr){3-6} \cmidrule(lr){7-10} \cmidrule(lr){11-14}
     &
     &HR@5 &NDCG@5&HR@10&NDCG@10
     &HR@5 &NDCG@5&HR@10&NDCG@10
     &HR@5 &NDCG@5&HR@10&NDCG@10 \\
    \midrule
    \multirow{2}{*}{SinPE}
     &CETRec
     &0.1101&0.0693&0.1209&0.0728&0.0670&0.0436&0.0779&0.0471&0.0780&0.0520&0.0910&0.0550 \\
     &\textit{w.o.} CT
     &0.1035&0.0634&0.1167&0.0676&0.0620&0.0407&0.0720&0.0440&0.0721&0.0482&0.0865&0.0514 \\
    \midrule
    \multirow{2}{*}{RoPE}
     &CETRec
     &\textbf{0.1283}&\textbf{0.0779}&\textbf{0.1365}&\textbf{0.0806}
     &\textbf{0.0921}&\textbf{0.0641}&\textbf{0.1072}&\textbf{0.0690}
     &\textbf{0.0866}&\textbf{0.0591}&\textbf{0.1030}&\textbf{0.0646} \\
     &\textit{w.o.} CT
     &0.1192&0.0745&0.1300&0.0781&0.0856&0.0613&0.1021&0.0669&0.0805&0.0565&0.0980&0.0626 \\
    \midrule                
     &\textit{w.o.} Both
     &0.0985&0.0614&0.1093&0.0650&0.0778&0.0530&0.0979&0.0596&0.0264&0.0192&0.0356 &0.0221 \\
    \bottomrule
  \end{tabular}
\end{table*}
```

## Table 4
```latex
\begin{table}
  \centering
  \caption{A tuning template for the Game dataset. <His\_Seq> and <Target\_Item> denote the user's historical interaction sequence and the ground-truth next item, respectively.}
  \label{tab:prompt}

  \begin{tabular}{@{}p{0.3\linewidth}p{0.6\linewidth}@{}}
    \toprule
    \multicolumn{2}{c}{\textbf{Instruction Input}} \\
    \midrule
    \textbf{Task Instruction:} 
      & Given a list of video games the user has played before, please recommend a new video game that the user likes to the user. \\
    \addlinespace
    \cdashline{1-2}[2pt/2pt]
    \noalign{\vskip 4pt}\textbf{Task Input:} 
      & The user has played the following video games before: \texttt{<His\_Seq>} \\
    \midrule
    \multicolumn{2}{c}{\textbf{Instruction Output}} \\
    \midrule
    \textbf{Output:}
      & \texttt{<Target\_Item>} \\
    \bottomrule
  \end{tabular}
\end{table}
```

