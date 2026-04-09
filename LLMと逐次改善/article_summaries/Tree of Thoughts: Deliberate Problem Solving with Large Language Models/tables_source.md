# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[htbp]
%   \centering
%   \begin{tabularx}{\textwidth}{X X X}
%     \toprule
%     \textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\
%     \midrule
%     Some long text that needs to be wrapped automatically & Short text & Another long text that needs to be wrapped automatically \\
%     \midrule
%     Short text & Some really long text that needs to be wrapped automatically & Short text \\
%     \bottomrule
%   \end{tabularx}
%   \caption{Example of a table with automatic text wrapping using tabularx.}
%   \label{tab:example}
% \end{table}
```

## Table 2
```latex
\begin{table}[ht]
  \centering
  \begin{tabularx}{\textwidth}{l|XXX}
    \toprule
     &  \textbf{Game of 24} & \textbf{Creative Writing} & \textbf{5x5 Crosswords} \\
    \midrule
    \textbf{\small Input} & 4 numbers {\textcolor{blue}{(4 9 10 13)}}  & 4 random sentences & 10 clues {\textcolor{blue}{(h1.\,presented;..)}}\\
    \midrule
    \textbf{\small Output} & An equation to reach 24 {\textcolor{blue}{(13-9)*(10-4)=24}} & A passage of 4 paragraphs ending in the 4 sentences  & 5x5 letters: {\textcolor{blue}{SHOWN; WIRRA; AVAIL; ...}} \\
    \midrule
    \textbf{\small Thoughts} & 3 intermediate equations {\textcolor{blue}{(13-9=4 (left 4,4,10); 10-4=6 (left 4,6); 4*6=24)}} & A short writing plan {\textcolor{blue}{(1.\,Introduce a book that connects...)}} & Words to fill in for clues: {\textcolor{blue}{(h1.\,shown; v5.\,naled; ...)}}  \\
    \midrule
    \textbf{\small \#ToT steps} & 3 & 1 & 5-10 (variable) \\
    \bottomrule
  \end{tabularx}
\caption{Task overview. Input, output, thought examples are in blue. }
\label{tab:overview}
\vspace{-18pt}
\end{table}
```

## Table 3
```latex
\begin{table}[h]
  \centering
  % \resizebox{\columnwidth}{!}{%
  \begin{tabularx}{\columnwidth}{l|XXX}
    \toprule
  \textbf{Method} & \multicolumn{3}{c}{\textbf{Success Rate (\%)}} \\
  & \textbf{\small Letter} & \textbf{\small Word} & \textbf{\small Game} \\
    \midrule
    IO & 38.7 & 14 & 0 \\
    CoT & 40.6 & 15.6 & 1 \\
    % \midrule
    ToT (ours) & \textbf{78} & \textbf{60} & \textbf{20} \\
    \midrule
    +best state & 82.4 & 67.5 & 35 \\
    -prune & 65.4 & 41.5 & 5 \\
    -backtrack & 54.6 & 20 & 5\\
    % -prune & 
    \bottomrule
  \end{tabularx}
  % }
  \vspace{-10pt}
    \captionof{table}{Mini Crosswords results.}
    \label{table:results_crosswords}
% \end{table}
```

## Table 4
```latex
\begin{table}[ht]
%   \centering
%   \begin{tabular}{ll}
%     \toprule
%     \textbf{Methods} &  \textbf{Win/Tie/Lose} \\
%     \midrule
%     plan-write vs. tot + bfs (breath=5) & 16/35/49 \\
%     IO, CoT, ToT scores & 6.19, 6.93, 7.56\\
%     \bottomrule
%   \end{tabular}
%     \caption{Automatic coherency evaluation on 100 creative writing tasks. \sy{write vs. tot?} \sy{improve evaluation prompt, or use human eval?}}
% \end{table}
```

## Table 5
```latex
\begin{table}[h]
%     \centering
%   \begin{tabular}{lll}
%     \toprule
%     \textbf{} &  \textbf{generate/prompt tokens} & \textbf{cost per case} \\ 
%     \midrule 
%     IO (best of 100) & 7.3\% & 6\% \\
%     CoT (best of 100) & 4.0\% & 3\% \\
%     ToT & 74\% & 19\% \\
%     \bottomrule 
%   \end{tabular}
%     \caption{Caption}
%     \label{tab:my_label}
% \end{table}
```

## Table 6
```latex
\begin{table}[h]
    \centering
    \begin{tabular}{llll}
    \toprule
        \textbf{Game of 24} & \textbf{Generate/Prompt tokens} & \textbf{Cost per case} & \textbf{Success} \\
        \midrule
        IO (best of 100) & 1.8k / 1.0k & \$0.13 & 33\% \\
        CoT (best of 100) & 6.7k / 2.2k & \$0.47 & 49\% \\
        ToT  & 5.5k / 1.4k & \$0.74 & 74\% \\
        \bottomrule
    \end{tabular}
    \caption{Cost analysis on Game of 24.}
    \label{tab:cost_game}
\end{table}
```

## Table 7
```latex
\begin{table}[h]
    \centering
    \begin{tabular}{lll}
    \toprule
        \textbf{Creative Writing} & \textbf{Generate/Prompt tokens} & \textbf{Cost per case} \\
        \midrule
        IO & 0.9k / 0.4k & \$0.06 \\
        CoT & 0.9k / 0.4k & \$0.07  \\
        ToT  & 4k / 2.9k & \$0.32  \\
        \bottomrule
    \end{tabular}
    \caption{Cost analysis on Game of 24.}
    \label{tab:cost_writing}
\end{table}
```

