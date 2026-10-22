# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
    \centering
    \small
    \caption{Performance of $\DAI$ against existing DouDizhu programs by playing 10,000 randomly sampled decks. Algorithm \texttt{A} outperforms \texttt{B} if WP is larger than 0.5 or ADP is larger than 0 (highlighted in boldface). The algorithms are ranked according to the number of the other algorithms that they beat. The full results of each position are provided in Appendix~\ref{sec:D1}.}.
    \vspace{-7pt}
    \label{tab:mainperformance}
    \setlength{\tabcolsep}{2.0pt}
    \begin{tabular}{c||l|cc|cc|cc|cc|cc|cc|cc|cc}
    \toprule
     
\multirow{2}{*}{Rank} & \multirow{2}{*}{\diagbox [width=5em,trim=l] {\texttt{A}}{\texttt{B}}} & \multicolumn{2}{c|}{$\DAI$} & \multicolumn{2}{c|}{DeltaDou} & \multicolumn{2}{c|}{SL} & \multicolumn{2}{c|}{RHCP-v2} & \multicolumn{2}{c|}{RHCP} & \multicolumn{2}{c|}{RLCard} & \multicolumn{2}{c|}{CQN} &\multicolumn{2}{c}{Random}\\
\cline{3-18}
& & WP & ADP & WP & ADP & WP & ADP & WP & ADP & WP & ADP & WP & ADP & WP & ADP & WP & ADP\\
    \hline
    \midrule
     1 & $\DAI$ & - & - & \textbf{0.586} & \textbf{0.258} & \textbf{0.659} & \textbf{0.700} & \textbf{0.757} & \textbf{1.662} & \textbf{0.764} & \textbf{1.671} & \textbf{0.889} & \textbf{2.288} & \textbf{0.810} & \textbf{1.685} & \textbf{0.989} & \textbf{3.036}\\
     2 & DeltaDou & 0.414 & -0.258 & - & - & \textbf{0.617} & \textbf{0.653} & \textbf{0.745} & \textbf{1.500} & \textbf{0.747} & \textbf{1.514} & \textbf{0.876} & \textbf{2.459} & \textbf{0.784} & \textbf{1.534} & \textbf{0.992} & \textbf{3.099}\\
     3 & SL & 0.341 & -0.700 & 0.396 & -0.653 & - & - & \textbf{0.611} & \textbf{0.853} & \textbf{0.632} & \textbf{0.886} & \textbf{0.813} & \textbf{1.821} & \textbf{0.694} & \textbf{1.037} & \textbf{0.976} & \textbf{2.721}\\
     4 & RHCP-v2 & 0.243 & -1.662 & 0.257 & -1.500 & 0.389 & -0.853 & - & - & \textbf{0.515} & \textbf{0.052} & \textbf{0.692} & \textbf{1.121} & \textbf{0.621} & \textbf{0.714} & \textbf{0.967} & \textbf{2.631}\\
     5 & RHCP & 0.236 & -1.671 & 0.253 & -1.514 & 0.369 & -0.886 & 0.485 & -0.052 & - & - & \textbf{0.682} & \textbf{1.259} & \textbf{0.603} & \textbf{0.248} & \textbf{0.941} & \textbf{2.720}\\
     6 & RLCard & 0.111 & -2.288 & 0.124 & -2.459 & 0.187 & -1.821 & 0.309 & -1.121 & 0.318 & -1.259 & - & - & \textbf{0.522} & \textbf{0.168} & \textbf{0.943} & \textbf{2.471}\\
     7 & CQN & 0.190 & -1.685 & 0.216 & -1.534 & 0.306 & -1.037 & 0.379 & -0.714 & 0.397 & -0.248 & 0.478 & -0.168 & - & - & \textbf{0.889} & \textbf{1.912}\\
     8 & Random & 0.011 & -3.036 & 0.008 & -3.099 & 0.024 & -2.721 & 0.033 & -2.631 & 0.059 & -2.720 & 0.057 & -2.471 & 0.111 & -1.912 & - & -\\
   
     \bottomrule
    \end{tabular}
    \vspace{-7pt}
\end{table*}
```

## Table 2
```latex
\begin{table}[t]
    \centering
    \small
    \caption{Comparison of $\DAI$, DeltaDou and SL with the bidding phase by playing 100,000 randomly sampled decks.}
    \label{tab:douzerobidding}
    \begin{tabular}{l|c|c|c}
    \toprule
     
    & $\DAI$ & DeltaDou & SL \\
    \midrule
    WP & \textbf{0.580} & 0.461 & 0.381 \\
    ADP & \textbf{0.323} & -0.004 & -0.320\\
     \bottomrule
    \end{tabular}
    \vspace{-15pt}
\end{table}
```

## Table 3
```latex
\begin{table}[h!]
    \centering
    \caption{Summary of the action space of DouDizhu. We follow the summary provided in RLCard~\cite{zha2019rlcard}.}
    \label{tab:sumactionspace}
    \begin{tabular}{l|l}
    \toprule
    \textbf{Action Type} & \textbf{Number of Actions} \\
    \midrule
     Solo    &  $15$\\
     Pair    &  $13$\\
     Trio    &  $13$\\
     Trio with Solo & $182$\\
     Trio with Pair & $156$\\
     Chain of Solo & $36$\\
     Chain of Pair & $52$\\
     Chain of Trio & $45$\\
     Plane with Solo & $21,822$\\
     Plane with Pair & $2,939$\\
     Quad with Solo & $1,326$\\
     Quad with Pair & $858$\\
     Bomb & $13$\\
     Rocket & $1$\\
     Pass & $1$\\
     
     \midrule
     Total & $27,472$\\
     \bottomrule
    \end{tabular}
\end{table}
```

## Table 4
```latex
\begin{table}[h!]
    \centering
    \caption{Features of the Landlord.}
    \label{tab:landlordfeature}
    \begin{tabular}{c|l|l}
    \toprule
     & \textbf{Feature} & \textbf{Size} \\
    \midrule
    \midrule
     Action & Card matrix of the action    &  $54$\\
     
     \midrule
     \multirow{2}{*}{State} & Card matrix of hand cards & $54$\\
      & Card matrix of the union of the other two players' hand cards & $54$\\
      & Card matrix of the most recent move & $54$\\
      & Card matrix of the the played cards of the first Peasant & $54$\\
      & Card matrix of the the played cards of the second Peasant & $54$\\
      & One-hot vector representing the number cards left of the first Peasant & $17$\\
      & One-hot vector representing the number cards left of the second Peasant & $17$\\
      & One-hot vector representing the number bombs in the current state & $15$\\
      & Concatenated matrix of the most recent 15 moves & $5 \times 162$\\
     \bottomrule
    \end{tabular}
    
\end{table}
```

## Table 5
```latex
\begin{table}[h!]
    \centering
    \caption{Features of the Peasants.}
    \label{tab:peasantfeature}
    \begin{tabular}{c|l|l}
    \toprule
     & \textbf{Feature} & \textbf{Size} \\
    \midrule
    \midrule
     Action & Card matrix of the action    &  $54$\\
     
     \midrule
     \multirow{2}{*}{State} & Card matrix of hand cards & $54$\\
      & Card matrix of the union of the other two players' hand cards & $54$\\
      & Card matrix of the most recent move & $54$\\
      & Card matrix of the most recent move performed by the Landlord & $54$\\
      & Card matrix of the most recent move performed by the other Peasant & $54$\\
      & Card matrix of the the played cards of the Landlord & $54$\\
      & Card matrix of the the played cards of the other Peasant & $54$\\
      & One-hot vector representing the number cards left of the Landlord & $20$\\
      & One-hot vector representing the number cards left of the other Peasant & $17$\\
      & One-hot vector representing the number bombs in the current state & $15$\\
      & Concatenated matrix of the most recent 15 moves & $5 \times 162$\\
     \bottomrule
    \end{tabular}
    
\end{table}
```

## Table 6
```latex
\begin{table}[h!]
    \centering
    \caption{Features of the bidding network.}
    \label{tab:sumbiddingfeature}
    \begin{tabular}{l|l}
    \toprule
    \textbf{Feature} & \textbf{Size} \\
    \midrule
    Card matrix of hand cards    &  $54$\\
    A vector representing solos of ranks 3 to A  &  $12$\\
    A vector representing pairs of ranks 3 to 2  &  $13$\\
    A vector representing trios of ranks 3 to 2  &  $13$\\
    A vector representing bombs of ranks 3 to 2 and the rocket  &  $14$\\
    The number of cards of rank 2 and the jokers  &  $10$\\
    A vector encoding historical bidding moves  &  $12$\\
     \midrule
     Total & $128$\\
     \bottomrule
    \end{tabular}
\end{table}
```

## Table 7
```latex
\begin{table}[h!]
    \centering
    \small
    \caption{WP of $\DAI$ and the baselines. L: WP of \texttt{A} as Landlord; P: WP of \texttt{A} as Peasants. If the average WP of L and P is higher than 0.5, we conclude that \texttt{A} outperforms \texttt{B} and highlight both L and P in boldface. The algorithms are ranked according to the number of the other algorithms that they beat.}.
    \label{tab:douzerofullwp}
    \setlength{\tabcolsep}{2.3pt}
    \begin{tabular}{c||l|cc|cc|cc|cc|cc|cc|cc|cc}
    \toprule
     
\multirow{2}{*}{Rank} & \multirow{2}{*}{\diagbox [width=5em,trim=l] {\texttt{A}}{\texttt{B}}} & \multicolumn{2}{c|}{$\DAI$} & \multicolumn{2}{c|}{DeltaDou} & \multicolumn{2}{c|}{SL} & \multicolumn{2}{c|}{RHCP-v2} & \multicolumn{2}{c|}{RHCP} & \multicolumn{2}{c|}{RLCard} & \multicolumn{2}{c|}{CQN} &\multicolumn{2}{c}{Random}\\
\cline{3-18}
& & L & P & L & P & L & P & L & P & L & P & L & P & L & P & L & P\\
    \hline
    \midrule
     1 & $\DAI$ & .4159 & .5841 & \textbf{.4870} & \textbf{.6843} & \textbf{.5692} & \textbf{.7494} & \textbf{.6844} & \textbf{.8303} & \textbf{.7253} & \textbf{.8033} & \textbf{.8695} & \textbf{.9089} & \textbf{.7686} & \textbf{.8513} & \textbf{.9858} & \textbf{.9920}\\
     2 & DeltaDou & .3166 & .5130 & .4120 & .5880 & \textbf{.5130} & \textbf{.7211} & \textbf{.6701} & \textbf{.8165} & \textbf{.7048} & \textbf{.7899} & \textbf{.8563} & \textbf{.8955} & \textbf{.7326} & \textbf{.8351} & \textbf{.9871} & \textbf{.9960}\\
     3 & SL & .2506 & .4308 & .2789 & .5130 & .4072 & .5928 & \textbf{.5370} & \textbf{.6857} & \textbf{.5831} & \textbf{.6810} & \textbf{.7605} & \textbf{.8650} & \textbf{.6450} & \textbf{.7428} & \textbf{.9599} & \textbf{.9927}\\
     4 & RHCP-v2 & .1697 & .3156 & .1835 & .3299 & .3143 & .4630 & .4595 & .5405 & \textbf{.5134} & \textbf{.5165} & \textbf{.6813} & \textbf{.7018} & \textbf{.6313} & \textbf{.6116} & \textbf{.9519} & \textbf{.9821}\\
     5 & RHCP & .1967 & .2747 & .2101 & .2952 & .3190 & .4179 & .4835 & .4866 & .4971 & .5029 & \textbf{.6718} & \textbf{.6913} & \textbf{.6416} & \textbf{.5640} & \textbf{.9092} & \textbf{.9725}\\
     6 & RLCard & .0911 & .1305 & .1045 & .1437 & .1350 & .2395 & .2982 & .3187 & .3087 & .3282 & .4465 & .5535 & \textbf{.5839} & \textbf{.4603} & \textbf{.9314} & \textbf{.9539}\\
     7 & CQN & .1487 & .2314 & .1649 & .2674 & .2572 & .3550 & .3884 & .3687 & .4360 & .3584 & .5397 & .4161 & .5238 & .4762 & \textbf{.8566} & \textbf{.9213}\\
     8 & Random & .0080 & .0142 & .0040 & .0129 & .0073 & .0401 & .0179 & .0481 & .0025 & .0908 & .0461 & .0686 & .0787 & .1434 & .3461 & .6539\\
   
     \bottomrule
    \end{tabular}

\end{table}
```

## Table 8
```latex
\begin{table}[h!]
    \centering
    \small
    \caption{ADP of $\DAI$ and the baselines. L: ADP of \texttt{A} as Landlord; P: ADP of \texttt{A} as Peasants. If the average ADP of L and P is higher than 0, we conclude that \texttt{A} outperforms \texttt{B} and highlight both L and P in boldface. The algorithms are ranked according to the number of the other algorithms that they beat.}.
    \label{tab:douzerofulladp}
    \setlength{\tabcolsep}{1.2pt}
    \begin{tabular}{c||l|cc|cc|cc|cc|cc|cc|cc|cc}
    \toprule
     
\multirow{2}{*}{Rank} & \multirow{2}{*}{\diagbox [width=5em,trim=l] {\texttt{A}}{\texttt{B}}} & \multicolumn{2}{c|}{$\DAI$} & \multicolumn{2}{c|}{DeltaDou} & \multicolumn{2}{c|}{SL} & \multicolumn{2}{c|}{RHCP-v2} & \multicolumn{2}{c|}{RHCP} & \multicolumn{2}{c|}{RLCard} & \multicolumn{2}{c|}{CQN} &\multicolumn{2}{c}{Random}\\
\cline{3-18}
& & L & P & L & P & L & P & L & P & L & P & L & P & L & P & L & P\\
    \hline
    \midrule
     1 & $\DAI$ & -0.435 & 0.435 & \textbf{-0.342} & \textbf{0.858} & \textbf{0.287} & \textbf{1.112} & \textbf{1.436} & \textbf{1.888} & \textbf{1.492} & \textbf{1.850} & \textbf{2.222} & \textbf{2.354} & \textbf{1.368} & \textbf{2.001} & \textbf{3.254} & \textbf{2.818}\\
     2 & DeltaDou & 0.342 & -0.858 & -0.476 & 0.476 & \textbf{0.268} & \textbf{1.038} & \textbf{1.297} & \textbf{1.703} & \textbf{1.312} & \textbf{1.715} & \textbf{2.270} & \textbf{2.648} & \textbf{1.218} & \textbf{1.849} & \textbf{3.268} & \textbf{2.930}\\
     3 & SL & -1.112 & -0.287 & -1.038 & -0.268 & -0.364 & 0.364 & \textbf{0.564} & \textbf{1.142} & \textbf{0.658} & \textbf{1.114} & \textbf{1.652} & \textbf{1.990} & \textbf{0.878} & \textbf{1.196} & \textbf{3.026} & \textbf{2.415}\\
     4 & RHCP-v2 & -1.888 & -1.436 & -1.703 & -1.297 & -1.142 & -0.564 & -0.209 & 0.209 & \textbf{0.074} & \textbf{0.029} & \textbf{1.011} & \textbf{1.230} & \textbf{0.750} & \textbf{0.677} & \textbf{2.638} & \textbf{2.624}\\
     5 & RHCP & -1.850 & -1.492 & -1.715 & -1.312 & -1.114 & -0.658 & -0.029 & -0.074 & -0.007 & 0.007 & \textbf{1.190} & \textbf{1.328} & \textbf{0.927} & \textbf{-0.432} & \textbf{2.722} & \textbf{2.717}\\
     6 & RLCard & -2.354 & -2.222 & -2.648 & -2.270 & -1.990 & -1.652 & -1.230 & -1.011 & -1.328 & -1.190 & -0.266 & 0.266 & \textbf{0.474} & \textbf{-0.138} & \textbf{2.630} & \textbf{2.312}\\
     7 & CQN & -2.001 & -1.368 & -1.849 & -1.218 & -1.196 & -0.878 & -0.677 & -0.750 & 0.432 & -0.927 & 0.138 & -0.474 & 0.056 & -0.056 & \textbf{1.832} & \textbf{1.992}\\
     8 & Random & -2.818 & -3.254 & -2.930 & -3.268 & -2.415 & -3.026 & -2.624 & -2.638 & -2.717 & -2.722 & -2.312 & -2.629 & -1.991 & -1.832 & -0.883 & 0.883\\
   
     \bottomrule
    \end{tabular}

    \vspace{-10pt}
\end{table}
```

## Table 9
```latex
\begin{table}[h!]
    \centering
    \small
    \caption{WP of $\DAI$ against baselines when using ADP as the reward. L: WP of \texttt{A} as Landlord; P: WP of \texttt{A} as Peasants. If the average WP of L and P is higher than 0.5, we conclude that \texttt{A} outperforms \texttt{B} and highlight both L and P in boldface.}.
    \label{tab:douzeroadp}
    \setlength{\tabcolsep}{2.3pt}
    \begin{tabular}{l|cc|cc|cc|cc|cc|cc|cc|cc}
    \toprule
     
\multirow{2}{*}{\diagbox [width=5em,trim=l] {\texttt{A}}{\texttt{B}}} & \multicolumn{2}{c|}{$\DAI$ (ADP)} & \multicolumn{2}{c|}{DeltaDou} & \multicolumn{2}{c|}{SL} & \multicolumn{2}{c|}{RHCP-v2} & \multicolumn{2}{c|}{RHCP} & \multicolumn{2}{c|}{RLCard} & \multicolumn{2}{c|}{CQN} &\multicolumn{2}{c}{Random}\\
\cline{2-17}
& L & P & L & P & L & P & L & P & L & P & L & P & L & P & L & P\\
    \hline
    \midrule
     $\DAI$ (ADP) & .4281 & .5719 & \textbf{.4177} & \textbf{.6319} & \textbf{.5039} & \textbf{.6815} & \textbf{.6615} & \textbf{.7543} & \textbf{.6950} & \textbf{.7628} & \textbf{.8416} & \textbf{.8668} & \textbf{.7198} & \textbf{.8280} & \textbf{.9801} & \textbf{.9895}\\
   
     \bottomrule
    \end{tabular}

\end{table}
```

## Table 10
```latex
\begin{table}[h!]
    \centering
    \small
    \caption{ADP of $\DAI$ against baselines when using WP as the reward. L: ADP of \texttt{A} as Landlord; P: ADP of \texttt{A} as Peasants. If the average ADP of L and P is higher than 0, we conclude that \texttt{A} outperforms \texttt{B} and highlight both L and P in boldface.}.
    \label{tab:douzerowp}
    \setlength{\tabcolsep}{2.3pt}
    \begin{tabular}{l|cc|cc|cc|cc|cc|cc|cc|cc}
    \toprule
     
\multirow{2}{*}{\diagbox [width=5em,trim=l] {\texttt{A}}{\texttt{B}}} & \multicolumn{2}{c|}{$\DAI$ (WP)} & \multicolumn{2}{c|}{DeltaDou} & \multicolumn{2}{c|}{SL} & \multicolumn{2}{c|}{RHCP-v2} & \multicolumn{2}{c|}{RHCP} & \multicolumn{2}{c|}{RLCard} & \multicolumn{2}{c|}{CQN} &\multicolumn{2}{c}{Random}\\
\cline{2-17}
& L & P & L & P & L & P & L & P & L & P & L & P & L & P & L & P\\
    \hline
    \midrule
     $\DAI$ (WP) & -0.411 & 0.411 & \textbf{-0.360} & \textbf{0.664} & \textbf{0.224} & \textbf{1.001} & \textbf{1.252} & \textbf{1.880} & \textbf{1.378} & \textbf{1.794} & \textbf{2.094} & \textbf{2.298} & \textbf{1.418} & \textbf{1.872} & \textbf{2.947} & \textbf{2.518}\\
   
     \bottomrule
    \end{tabular}

\end{table}
```

## Table 11
```latex
\begin{table}[h!]
    \centering
    \small
    \caption{$\DAI$ against DeltaDou and SL when using ADP as reward with bidding network.}
    \label{tab:douzeroadpbidding}
    \begin{tabular}{l|c|c|c}
    \toprule
     
    & $\DAI$ (ADP) & DeltaDou & SL \\
    \midrule
    WP & \textbf{0.535} & 0.477 & 0.407 \\
    ADP & \textbf{0.323} & -0.004 & -0.320\\
   
     \bottomrule
    \end{tabular}

\end{table}
```

## Table 12
```latex
\begin{table}[h!]
    \centering
    \small
    \caption{$\DAI$ against DeltaDou and SL when using WP as reward with bidding network.}
    \label{tab:douzerowpbidding}
    \begin{tabular}{l|c|c|c}
    \toprule
     
    & $\DAI$ (WP) & DeltaDou & SL \\
    \midrule
    WP & \textbf{0.580} & 0.461 & 0.381 \\
    ADP & \textbf{0.315} & 0.075 & -0.390\\
   
     \bottomrule
    \end{tabular}

\end{table}
```

## Table 13
```latex
\begin{table}[h!]
    \centering
    \small
    \caption{Head-to-head comparison between using ADP and WP as objectives. $\DAI$ (ADP) outperforms $\DAI$ (WP) in terms of ADP but is worse than $\DAI$ (WP) in terms of WP. The agents tend to learn different skills with different objectives.}
    \label{tab:douzeroheadtohead}
    \setlength{\tabcolsep}{2.3pt}
    \begin{tabular}{l|cc|cc}
    \toprule
     
  & \multicolumn{2}{c|}{ADP} & \multicolumn{2}{c}{WP} \\
\cline{2-5}
& L & P & L & P\\
    \hline
    \midrule
     $\DAI$ (ADP) vs $\DAI$ (WP) & \textbf{-0.3101} & \textbf{0.4476} & .3617 & .5151 \\
   
     \bottomrule
    \end{tabular}

\end{table}
```

## Table 14
```latex
\begin{table}[h!]
    \centering
    \caption{Summary of weights assigned to each category in Botzone.}
    \label{tab:sumweightsbotzone}
    \begin{tabular}{l|l}
    \toprule
    \textbf{Action Type} & \textbf{Weight} \\
    \midrule
     Solo    &  $1$\\
     Pair    &  $2$\\
     Trio (or with Solo / Pair)    &  $4$\\
     Chain of Solo & $6$\\
     Chain of Pair & $6$\\
     Chain of Trio & $8$\\
     Plane with Solo / Pair & $8$\\
     Quad with Solo / Pair & $8$\\
     Space shuttle A (2 consecutive Quad) & $10$\\
     Bomb & $10$\\
     Rocket & $16$\\
     Space shuttle B (more than 3 consecutive Quads) & $20$\\
     Pass & $0$\\
     \bottomrule
    \end{tabular}
\end{table}
```

## Table 15
```latex
\begin{table}[H]
    \centering
    \caption{Case 1: Comparison of $\DAI$ in early stage and later stage. $\DAI$ plays the Landlord position on the same deck with the same opponents. $\DAI$ loses in the early stage but wins the game in the later stage. $\DAI$ in the later stage tends to perform a better planning of the hand. Specifically, $\DAI$ in the later stage tends to first play small pairs, such as 88 and TT, so that it can easily empty the hand later.}
    \begin{tabular}{l|l}
    \toprule
     & Logs  \\
    \midrule
     Early stage & \makecell[l]{H:455557777889TTKKAA22; 3446668999QQKA2BR; 333468TTJJJJQQKA2, L:88, D:QQ, U:P, L:KK,\\ D:P, U:P, L:455559, D:P, U:46JJJJ, L:P, D:P, U:3338, L:P, D:3666, U:P, L:P, D:44999, U:P, L:P, D:8, U:K,\\ L:A, D:2, U:P, L:P, D:K, U:P, L:A, D:BR, U:P, L:P, D:A}  \\
     \midrule
     Later stage & \makecell[l]{H:455557777889TTKKAA22; 3446668999QQKA2BR; 333468TTJJJJQQKA2, L:TT, D:QQ, U:P, L:KK,\\ D:P, U:P, L:88, D:99, U:TT, L:AA, D:P, U:P, L:477779, D:P, U:46JJJJ, L:P, D:P, U:3338, L:5555, D:BR,\\ U:P, L:P, D:3666, U:P, L:P, D:8, U:K, L:2, D:P, U:P, L:2} \\
     \bottomrule 
    \end{tabular}

\end{table}
```

## Table 16
```latex
\begin{table}[t]
    \centering
    \caption{Case 2: Comparison of $\DAI$ in early stage and later stage. $\DAI$ plays the Landlord position on the same deck with the same opponents. In the early stage, $\DAI$ keeps playing PASS because it does not want to break the Rocket. As result, $\DAI$ loses the game. In the later stage, $\DAI$ smartly breaks the Rocket to dominate other Solos, and eventually wins the game.}
    \begin{tabular}{l|l}
    \toprule
     & Logs  \\
    \midrule
     Early stage & \makecell[l]{H:3355556778889JJQKABR; 344446679JJQQKA22; 367899TTTTQKKAA22, L:9, D:K, U:P, L:A, D:2,\\ U:P, L:P, D:3, U:9, L:K, D:A, U:P, L:P, D:4, U:Q, L:P, D:P, U:6789T, L:P, D:P, U:3TTT, L:P, D:P, U:KK,\\ L:P, D:P, U:AA, L:P, D:P, U:22}  \\
     \midrule
     Later stage & \makecell[l]{H:3355556778889JJQKABR; 344446679JJQQKA22; 367899TTTTQKKAA22, L:33, D:66, U:KK, L:P,\\ D:P, U:6789T, L:P, D:P, U:3TTT, L:P, D:P, U:9, L:Q, D:K, U:P, L:A, D:2, U:P, L:P, D:3, U:Q, L:K, D:A,\\ U:P, L:B, D:P, U:P, L:6, D:7, U:A, L:R, D:P, U:P, L:555577JJ, D:P, U:P, L:8889} \\
     \bottomrule 
    \end{tabular}

\end{table}
```

## Table 17
```latex
\begin{table}[H]
    \centering
    \caption{Case 3: Comparison of $\DAI$ in early stage and later stage. $\DAI$ plays the Landlord position on the same deck with the same opponents. In the early stage, the first move of $\DAI$ is 9. However there is a 4 in the hand, which causes troubles in later turns. In the later stage, $\DAI$ plays in a different style by starting with 33 and finally wins the game. Although playing 9 seems to be not bad, it may lead to losing the game later.}
    \begin{tabular}{l|l}
    \toprule
     & Logs  \\
    \midrule
     Early stage & \makecell[l]{H:33455556889TTJAA22BR; 334677778TTJQKA22; 446688999JJQQQKKKA, L:9, D:T, U:A, L:2,\\ D:7777, U:P, L:P, D:TJQKA, U:P, L:5555, D:P, U:P, L:6, D:8, U:P, L:J, D:2, U:P, L:R, D:P, U:P, L:88,\\ D:P, U:JJ, L:AA, D:P, U:P, L:33, D:P, U:66, L:TT, D:P, U:KK, L:P, D:P, U:8999, L:P, D:P, U:QQQK, L:P,\\ D:P, U:44}  \\
     \midrule
     Later stage & \makecell[l]{H:33455556889TTJAA22BR; 334677778TTJQKA22; 446688999JJQQQKKKA, L:33, D:22, U:P, L:BR,\\ D:P, U:P, L:6, D:8, U:A, L:2, D:7777, U:P, L:P, D:TJQKA, U:P, L:5555, D:P, U:P, L:9, D:T, U:P, L:J, D:P,\\ U:K, L:2, D:P, U:P, L:88, D:P, U:JJ, L:P, D:P, U:44999, L:P, D:P, U:66QQQ, L:P, D:P, U:KK, L:AA, D:P, U:P,\\ L:TT, D:P, U:P, L:4} \\
     \bottomrule 
    \end{tabular}

\end{table}
```

## Table 18
```latex
\begin{table}[H]
    \centering
    \caption{Case 4: Comparison of $\DAI$ in early stage and later stage. $\DAI$ plays the LandlordUp and LandlordDown positions on the same deck with the same opponent. While $\DAI$ wins both games. $\DAI$ in the later stage looks more reasonable. In turn 16, $\DAI$ in the early stage chooses to break a pair of 2, which is hard to be explained. $\DAI$ in the later stage tends to play more smoothly and wins the games quickly.}
    \begin{tabular}{l|l}
    \toprule
     & Logs  \\
    \midrule
     Early stage & \makecell[l]{H:3455567788TJJQKKKKA2; 33446678899JQQQA2; 3456799TTTJAA22BR, L:345678, D:P, U:P,\\ L:TJQKA, D:P, U:P, L:55KKK, D:P, U:P, L:7, D:P, U:R, L:P, D:P, U:2, L:P, D:P, U:34567, L:P, D:P, U:J,\\ L:2, D:P, U:B, L:P, D:P, U:2, L:P, D:P, U:AA, L:P, D:P, U:99TTT}  \\
     \midrule
     Later stage & \makecell[l]{H:3455567788TJJQKKKKA2; 33446678899JQQQA2; 3456799TTTJAA22BR, L:345678, D:P, U:P,\\ L:TJQKA, D:P, U:P, L:55KKK, D:P, U:BR, L:P, D:P, U:99TTT, L:P, D:P, U:34567, L:P, D:P,\\ U:AA, L:P, D:P, U:22, L:P, D:P, U:J} \\
     \bottomrule 
    \end{tabular}

\end{table}
```

## Table 19
```latex
\begin{table}[H]
    \centering
    \caption{Case 1: Randomly selected (rather than cherry-picked) full self-play games of $\DAI$. $\DAI$ plays the Landlord, LandlordUP and LandlordDown positions. All $\DAI$ agents were trained using WP as objectives. }
    \begin{tabular}{l}
    \toprule
    Logs  \\
      \midrule 
 \makecell[l]{H:335556788899TTJKKA2R; 6677789TTJJQQKA2B; 334444569JQQKAA22, L:33, D:66, U:QQ, L:KK,\\ D:P, U:AA, L:P, D:P, U:9, L:T, D:A, U:P, L:2, D:B, U:P, L:P, D:9, U:J, L:A, D:2, U:P, L:R, D:P, U:P, L:5559,\\ D:777J, U:P, L:P, D:J, U:K, L:P, D:P, U:5, L:6, D:8, U:4444, L:P, D:P, U:33, L:88, D:TT, U:22, L:P, D:P, U:6}  \\ 
 \midrule 
 \makecell[l]{H:34455777889JQQKA222B; 345668899TTTJQKAA; 33456679TJJQKKA2R, L:44, D:P, U:JJ, L:QQ,\\ D:AA, U:P, L:P, D:3, U:T, L:J, D:P, U:Q, L:K, D:P, U:A, L:P, D:P, U:9, L:A, D:P, U:2, L:B, D:P, U:P, L:3,\\ D:4, U:6, L:9, D:Q, U:P, L:2, D:P, U:R, L:P, D:P, U:34567, L:P, D:P, U:KK, L:22, D:P, U:P, L:77788, D:66TTT, U:P, L:P,\\ D:J, U:P, L:P, D:9, U:P, L:P, D:9, U:P, L:P, D:8, U:P, L:P, D:5, U:P, L:P, D:K, U:P, L:P, D:8}  \\ 
 \midrule 
 \makecell[l]{H:34455666789TTJQQKA2R; 335688899TJQA222B; 34457779TJJQKKKAA, L:445566, D:P, U:P, L:6789T,\\ D:89TJQ, U:9TJQK, L:TJQKA, D:P, U:P, L:Q, D:A, U:P, L:2, D:B, U:P, L:R, D:P, U:P, L:3}  \\ 
 \midrule 
 \makecell[l]{H:334447779TTTJQKKK22R; 3345566678TJQKA2B; 556888999JJQQAAA2, L:33444, D:55666, U:888JJ, L:TTT22,\\ D:P, U:55AAA, L:P, D:P, U:QQ, L:P, D:P, U:6999, L:QKKK, D:P, U:P, L:R, D:P, U:P, L:777J, D:P, U:P, L:9}  \\ 
 \midrule 
 \makecell[l]{H:455577899TTJJKKAA22B; 3346789TJJQQAA22R; 334456667889TQQKK, L:4, D:P, U:K, L:A,\\ D:2, U:P, L:P, D:6789TJ, U:P, L:P, D:4, U:Q, L:A, D:2, U:P, L:B, D:R, U:P, L:P, D:33, U:88, L:TT, D:QQ, U:P, L:KK,\\ D:AA, U:P, L:22, D:P, U:P, L:JJ, D:P, U:P, L:77, D:P, U:P, L:99, D:P, U:P, L:5558}  \\ 
 \midrule 
 \makecell[l]{H:3345666889JQQQKAA22B; 4457777899TJQAA2R; 33455689TTTJJKKK2, L:5, D:9, U:J, L:K,\\ D:2, U:P, L:B, D:R, U:P, L:P, D:89TJQ, U:P, L:P, D:44, U:P, L:88, D:AA, U:P, L:22, D:7777, U:P, L:P, D:5}  \\ 
 \midrule 
 \makecell[l]{H:334679999TTQQKKKAA2B; 3455677888JQKA22R; 344556678TTJJJQA2, L:33, D:55, U:TT, L:QQ,\\ D:P, U:P, L:TT, D:P, U:JJ, L:AA, D:22, U:P, L:P, D:4, U:Q, L:2, D:P, U:P, L:469999, D:P, U:P, L:7KKK, D:P, U:P, L:B}  \\ 
 \midrule 
 \makecell[l]{H:3455667899TTTJJQQKAB; 33567788JJQQKA22R; 3444567899TKKAA22, L:6, D:K, U:A, L:B,\\ D:P, U:P, L:34567, D:P, U:56789, L:89TJQ, D:P, U:P, L:5, D:6, U:A, L:P, D:P, U:T, L:A, D:2, U:P, L:P, D:5, U:9, L:J,\\ D:P, U:K, L:P, D:P, U:K, L:P, D:P, U:22, L:P, D:P, U:3444}  \\ 
 \midrule 
 \makecell[l]{H:345578TTJJJQKKKA2222; 3334566667789QQKR; 445788999TTJQAAAB, L:3, D:8, U:Q, L:2,\\ D:P, U:B, L:P, D:P, U:J, L:Q, D:K, U:P, L:A, D:P, U:P, L:4, D:9, U:T, L:P, D:P, U:88, L:TT, D:QQ, U:P, L:P,\\ D:4, U:9, L:2, D:6666, U:P, L:P, D:5, U:9, L:K, D:R, U:P, L:P, D:33377}  \\ 
 \midrule 
 \makecell[l]{H:3334577889TTJQKAAA2B; 345566789TJQQKKA2; 445667899TJJQK22R, L:5, D:6, U:K, L:P,\\ D:A, U:P, L:2, D:P, U:P, L:T, D:K, U:P, L:B, D:P, U:R, L:P, D:P, U:456789TJQ, L:P, D:P, U:4, L:K, D:2, U:P, L:P,\\ D:3, U:9, L:A, D:P, U:2, L:P, D:P, U:J, L:A, D:P, U:2, L:P, D:P, U:6}  \\ 
     \bottomrule 
    \end{tabular}
\end{table}
```

## Table 20
```latex
\begin{table}[H]
    \centering
    \caption{Case 2: Randomly selected (rather than cherry-picked) full games of $\DAI$ played with other agents in Botzone. $\DAI$ plays the position as noted in the left column. All $\DAI$ agents were trained using WP as objectives. }
    \begin{tabular}{l|l}
    \toprule
    Position & Logs  \\
      \midrule 
Landlord & \makecell[l]{H:33455778999TTTQKKAA2; 34567788TJQKKA2BR; 344566689JJJQQA22, L:48999TTT, D:BR,\\ U:P, L:P, D:34567, U:P, L:P, D:TJQKA, U:P, L:P, D:88, U:QQ, L:KK, D:P, U:22, L:P, D:P, U:3666,\\ L:P, D:P, U:5JJJ, L:P, D:P, U:44, L:AA, D:P, U:P, L:2, D:P, U:P, L:77, D:P, U:P, L:33,\\ D:P, U:P, L:55, D:P, U:P, L:Q}  \\ 
 \midrule 
Peasants & \makecell[l]{H:34456779TTJKKKAAAA22; 34455668888JQQQ2R; 335677999TTJJQK2B, L:34567, D:P,\\ U:9TJQK, L:P, D:P, U:T, L:J, D:Q, U:P, L:A, D:2, U:P, L:P, D:445566, U:P, L:P, D:38888Q, U:P,\\ L:P, D:Q, U:P, L:P, D:R, U:P, L:P, D:J}  \\ 
 \midrule 
Landlord & \makecell[l]{H:334455668899TJQQAA2B; 34567777TJJKKKAA2; 34568899TTJQQK22R, L:33445566, D:P,\\ U:P, L:9, D:T, U:P, L:Q, D:A, U:P, L:P, D:777JJ, U:P, L:P, D:34567, U:P, L:89TJQ, D:P, U:9TJQK,\\ L:P, D:P, U:3, L:8, D:A, U:P, L:2, D:P, U:R, L:P, D:P, U:88, L:AA, D:P, U:22, L:P,\\ D:P, U:4, L:B}  \\ 
 \midrule 
Peasants & \makecell[l]{H:34455677889TTJJQKK2R; 33557899JQQQKKA22; 344666789TTJAAA2B, L:345678, D:P,\\ U:6789TJ, L:789TJQ, D:P, U:P, L:4, D:7, U:A, L:2, D:P, U:B, L:R, D:P, U:P, L:5, D:A, U:P,\\ L:P, D:JQQQ, U:P, L:P, D:55, U:P, L:KK, D:22, U:P, L:P, D:K, U:A, L:P, D:P, U:A, L:P,\\ D:P, U:3, L:T, D:P, U:2, L:P, D:P, U:66, L:P, D:P, U:44, L:P, D:P, U:T}  \\ 
 \midrule 
Peasants & \makecell[l]{H:3355667789TJJQA222BR; 334446788TQQKKAA2; 455678999TTJJQKKA, L:33, D:88,\\ U:TT, L:P, D:P, U:45678, L:89TJQ, D:P, U:P, L:556677, D:QQKKAA, U:P, L:P, D:4, U:A, L:2, D:P, U:P,\\ L:J, D:P, U:Q, L:A, D:P, U:P, L:2, D:P, U:P, L:2, D:P, U:P, L:BR}  \\ 
 \midrule 
Landlord & \makecell[l]{H:334566778899TTQQKA2B; 3455689TJJQKKAA22; 344567789TJJQKA2R, L:456789T, D:89TJQKA,\\ U:P, L:P, D:3, U:4, L:K, D:A, U:2, L:P, D:P, U:34567, L:6789T, D:P, U:P, L:33, D:55, U:P,\\ L:QQ, D:22, U:P, L:P, D:4, U:J, L:B, D:P, U:R, L:P, D:P, U:789TJQKA}  \\ 
 \midrule 
Landlord & \makecell[l]{H:33455668TTTJJJQKAA22; 3445677789QQKKA2R; 3456788999TJQKA2B, L:4, D:A,\\ U:P, L:P, D:4, U:9, L:Q, D:K, U:2, L:P, D:P, U:89TJQKA, L:P, D:P, U:B, L:P, D:P, U:3456789}  \\ 
     \bottomrule 
    \end{tabular}

\end{table}
```

