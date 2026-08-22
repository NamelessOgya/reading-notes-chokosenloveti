# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[h]
\begin{center}
\scalebox{1.0}{
\begin{tabular}{c|cccccc}
\toprule
(\%) & b0 & b1.5 & b2 & b3 & b4 & c5 \\
\midrule
b0 & 50.0 & 43.0 & 37.2 & 24.3 & 26.4 & 19.8 \\
b1.5 & 57.0 & 50.0 & 40.0 & 30.4 & 29.7 & 21.3 \\
b2 & 62.8 & 60.0 & 50.0 & 34.9 & 38.3 & 29.9 \\
b3 & 75.7 & 69.6 & 65.1 & 50.0 & 43.5 & 39.0 \\
b4 & 73.6 & 70.3 & 61.7 & 56.5 & 50.0 & 44.5 \\
c5 & 80.2 & 78.7 & 70.1 & 61.0 & 55.5 & 50.0 \\
\bottomrule
\end{tabular}
}
\caption{Winrate table of all models. The entity at $(i, j)$ represents the winrate of ($i$-th row model)-vs-($j$-th column model). All models are described from Sec.\ref{sec:exclude_ph} to Sec.\ref{sec:cheat}. }
\label{tab:baselines}
\end{center}
\end{table}
```

## Table 2
```latex
\begin{table}[h]
\begin{center}
\scalebox{1.0}{
\begin{tabular}{c|cccccc}
\toprule
 & tournament 1 & tournament 2 \\
\midrule
b4-23day-vs-human & 3:0 & 3:0 \\
c5-16day-vs-human & 3:1 & 3:2 \\
\bottomrule
\end{tabular}
}
\caption{Machine-vs-human evaluation result. }
\label{tab:machine-vs-human}
\end{center}
\end{table}
```

## Table 3
```latex
\begin{table}[htbp]
    \centering
    \begin{tabular}{c|c}
        \toprule
         Parameter & Value \\
         \midrule
         {\color{blue}Weight of policy gradient from PPO} & 1.0 \\
         Weight of policy gradient from UPGO & 1.0 \\
         Weight of value function loss & 1.0 \\
         Weight of entropy penalty & 0.01 \\
         Learning rate & 7e-5 \\
         Batch size & 1e+4 * 8gpu \\
         {\color{blue}Discount} & {\color{blue}1.0} \\
         LSTM states & 256 \\
         Sample reuse & 2 \\
         {\color{blue}V-Trace $c$ clip} & {\color{blue}[0.001, 1.007]} \\
         {\color{blue}V-Trace $\rho$ clip} & {\color{blue}[0.001, 1.007]} \\
         \bottomrule
    \end{tabular}
    \caption{Reinforcement learning hyperparameters. }
    \label{tab:rl_hyper_parameter}
\end{table}
```

## Table 4
```latex
\begin{table}[htbp]
    \centering
    \begin{tabular}{c|c}
        \toprule
         Parameter & Value \\
         \midrule
         Self-play Probability, $p$ & 0.6 \\
         {\color{blue}Add to historical model threshold, $\xi$} & {\color{blue}0.55} \\
         Add to historical model max LP, $c$ & 6 \\
         Num samples of each LP & 3.2e+8 \\
         \bottomrule
    \end{tabular}
    \caption{OSFP hyperparameters. The notations are corresponding to Alg. \ref{alg:spfp}. }
    \label{tab:osfp_hyper_parameter}
\end{table}
```

## Table 5
```latex
\begin{table}[htbp]
% \begin{center}
% \scaleb{0.8}{
\begin{tabular}{l|l}
\toprule
Observations & Descriptions \\
\midrule
hero                   & my hero, one of (mage, hunter, warrior) \\
card set               & all cards, including each hero's specific cards \\
card selected mask     & 1 if the card has been selected else 0 \\
card can selected mask & 1 if the card can be selected else 0 \\
\midrule
hero           & my hero, one of (mage, hunter, warrior) \\
oppo hero      & opponent's hero, one of (mage, hunter, warrior) \\
my deck        & cards in my deck \\
decision type  & one of (construct, select, minion battlecry,  \\
               & spell card, minion/hero attack, hero power, \\
               & end turn) \\
my board       & minions on my board and their scalar features \\
oppo board     & minions on opponent's board and \\
               & their scalar features \\
my hand        & cards in my hand and their scalar features \\
my graveyard   & cards in my graveyard and their scalar features \\
oppo graveyard & cards in opponent's graveyard and \\
               & their scalar features \\
my player      & my features, such as number of hands and \\
               & minions, mana, weapon \\
oppo player    & opponent's features, such as number of hands \\
               & and minions, mana, weapon \\
BT action mask & 1 if the action can be done else 0 \\
\bottomrule
\end{tabular}
% }
\caption{Observation Space. The top block is for CB and the bottom block is for BT. }
\label{tab:obs}
% \end{center}
\end{table}
```

## Table 6
```latex
\begin{table}[htbp]
\begin{center}
\scalebox{0.85}{
\begin{tabular}{l|l}
\toprule
Action & Description \\
\midrule
selected card & card that is selected into the deck, corresponding to \\
              & \emph{card set} in observation space \\
\midrule
              & card that is selected as one of \emph{(type, target)}, one step for \emph{type} and \\
              & one step for \emph{target}, \\
selected card & \emph{type} $\in$ \emph{\{my hand card, my board card, opponent’s board card,} \\
              & \emph{my hero power card, end turn card\}}, \\
              & \emph{target} $\in$ \emph{\{my hero, opponent's hero, my board card and} \\
              & \emph{opponent's board card\}} \\
\bottomrule
\end{tabular}
}
\caption{Action Space. The top line is for CB and the bottom line is for BT. }
\label{tab:act}
\end{center}
\end{table}
```

