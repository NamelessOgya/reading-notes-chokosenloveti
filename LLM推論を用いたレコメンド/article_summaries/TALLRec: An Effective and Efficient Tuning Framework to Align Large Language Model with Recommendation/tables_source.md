# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
\setlength{\abovecaptionskip}{0cm}
\setlength{\belowcaptionskip}{0cm}
\caption{
Performance comparison between conventional sequential recommendation baselines and TALLRec under different few-shot training settings. The reported result is the AUC multiplied by 100, with boldface indicating the highest score. $\ddagger$: significantly better than all baselines with t-test $p$<0.01.
}
\setlength{\tabcolsep}{4mm}{
\resizebox{\textwidth}{!}{
\begin{tabular}{ccccccccc}
\toprule
% & & \multicolumn{6}{c}{\textbf{Baseline}} & \multicolumn{1}{c}{\textbf{Ours}} \\
% \cmidrule{3-8}\cmidrule{9-9}
 & \colorbox{gray!10}{Few-shot} & GRU4Rec                  & Caser                & SASRec               & DROS  & GRU-BERT & DROS-BERT &        TALLRec \\
 \midrule
 \multirow{3}{*}{movie} & 16   & 49.07                & 49.68                & 50.43                & 50.76    &50.85 & 50.21 & \textbf{67.24}$\ddagger$\\
                        & 64   & 49.87                & 51.06                & 50.48                 & 51.54    &51.65  & 51.71 &  \textbf{67.48}$\ddagger$\\
                        & 256  & 52.89                & 54.20                & 52.25                 & 54.07    &53.44 & 53.94 & \textbf{71.98}$\ddagger$\\ 
\midrule
\multirow{3}{*}{book}   & 16     & 48.95              & 49.84                & 49.48                & 49.28   & 50.07 & 50.07 &  \textbf{56.36}\\
                        & 64     & 49.64              & 49.72                & 50.06                & 49.13  & 49.64 & 48.98 & \textbf{60.39}$\ddagger$ \\
                        & 256    & 49.86              & 49.57                & 50.20                & 49.13  & 49.79 & 50.20 & \textbf{64.38}$\ddagger$\\ \bottomrule
\end{tabular}
}}

\label{tab:over_all_conpare}
\end{table*}
```

## Table 2
```latex
\begin{table}[]
% \begin{tabular}{cccccc}
% \toprule
%         \multirow{2}{*}{Model name} & Point-wise & Pair-wise & \multicolumn{3}{c}{List-wise}                                                                                   \\
% \cdashline{2-2}[1pt/2.5pt]\noalign{}
% \cdashline{3-3}[1pt/2.5pt]\noalign{}
% \cdashline{4-6}[1pt/2.5pt]\noalign{\vspace{0.5ex}}

%             & AUC        & AUC       &  NDCG@1 & NDCG@3 & NDCG@5 \\
% \midrule
% SASRec      & 52.25      & 56.3      & 28.8                                & \underline{51.8}                                & 64.4                                \\
% SASRec-full & 68.7       & \textbf{68.1}      & \textbf{38.5}                              & \textbf{61.2}                                & \textbf{70.3}                                \\
% LLM4Rec     & \textbf{71.2}       & \underline{66.03}     & \underline{30.5  }                              & 51.1                                & \underline{64.9 }   \\

% \bottomrule
% \end{tabular}
% \end{table}
```

## Table 3
```latex
\begin{table}
%   \caption{Frequency of Special Characters}
%   \label{tab:freq}
%   \begin{tabular}{ccl}
%     \toprule
%     Non-English or Math&Frequency&Comments\\
%     \midrule
%     \O & 1 in 1,000& For Swedish names\\
%     $\pi$ & 1 in 5& Common in math\\
%     \$ & 4 in 5 & Used in business\\
%     $\Psi^2_1$ & 1 in 40,000& Unexplained usage\\
%   \bottomrule
% \end{tabular}
% \end{table}
```

## Table 4
```latex
\begin{table*}
%   \caption{Some Typical Commands}
%   \label{tab:commands}
%   \begin{tabular}{ccl}
%     \toprule
%     Command &A Number & Comments\\
%     \midrule
%     \texttt{{\char'134}author} & 100& Author \\
%     \texttt{{\char'134}table}& 300 & For tables\\
%     \texttt{{\char'134}table*}& 400& For wider tables\\
%     \bottomrule
%   \end{tabular}
% \end{table*}
```

## Table 5
```latex
\begin{table}
\vspace{-0.5cm}
\centering
 \tiny  
  \caption{ 
 % Example of tuning data for instruction tuning in a translation task.
 A tuning sample for a translation task.
    }
 \label{table-operators}
 \vspace{-0.4cm}
 \resizebox{0.4\textwidth}{!}{
    \begin{tabular}{ll}
        \toprule
        \multicolumn{2}{c}{\textbf{Instruction Input}} \\
        % \cdashline{1-2}[1pt/2.5pt]\noalign{\vskip 0.5ex}
        \midrule
        {Task Instruction:}  & Translate from English to Chinese.\\ 
        {Task Input:} & Who am I ? \\  
        \midrule
        \multicolumn{2}{c}{\textbf{Instruction Output}}  \\
        % \cdashline{1-2}[1pt/2.5pt]\noalign{\vskip 0.5ex}
        \midrule
        {Task Output:}  &  \begin{CJK}{UTF8}{gbsn}我是谁?\end{CJK} \\ 
        \bottomrule
    \end{tabular}
}
\end{table}
```

## Table 6
```latex
\begin{table}
\centering
 \tiny  
  \caption{A tuning sample for rec-tuning.}
 \label{table-operators}
 \resizebox{0.45\textwidth}{!}{
    \begin{tabular}{@{}ll@{}}
        \toprule
        \multicolumn{2}{c}{\textbf{Instruction Input}} \\
        % \cdashline{1-2}[1pt/2.5pt]\noalign{\vskip 0.5ex}
        \midrule
        {Task Instruction:}  & \makecell[lp{4cm}]{Given the user's historical interactions, please determine  whether the user will enjoy the target new movie by answering "Yes" or "No".}\\ 
        % \cdashline{1-2}[1pt/2.5pt]\noalign{\vskip 0.5ex}
        \midrule
        {Task Input:} & \makecell[lp{4cm}]{User's liked items: GodFather. \\ User's disliked items: Star Wars.\\Target new  movie:  Iron Man}\\
        \midrule
        \multicolumn{2}{c}{\textbf{Instruction Output}}  \\
        % \cdashline{1-2}[1pt/2.5pt]\noalign{\vskip 0.5ex}
        \midrule
        
        {Task Output:}  &  No. \\ 
        \bottomrule
  \label{table:rec-tuning}
    \end{tabular}
    }
\end{table}
```

