# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[ht]
    \centering
    \small
    \begin{tabular}{|m{1.1cm}|m{3.35cm}|m{3.8cm}|m{4cm}|}
    \hline
    Method & Requirements & Main Idea & Main Weakness \\ [0.5ex] 
    \hline\hline
    BC & (State, Action) pairs from expert trajectory. & Learn policy that imitates the expert demonstration. & Sub-optimal expert can yield a very poor learned policy. \\ 
    \hline
    GAIL & (State, Action) pairs from expert trajectory. & Learn a policy that matches the distribution of expert trajectory pairs. &  Difficult to tune; Requires more world interactions; Can perform worse than BC. \\
    \hline
    RCG & Reversable transition function of environment; Resettable environment. & Take random walks from goal state to build curriculum of initial starting states. & Complexity may increase if random walks reach parts of state space irrelevant to a good policy. \\
    \hline
    Backplay & State sequence from a `good enough' trajectory; Resettable environment. & Sample starting state from given trajectory by walking backward along trajectory. & If states in `good enough' trajectory are not optimal, then can slow learning the \textit{optimal} policy. \\ [1ex] 
    \hline    
    \end{tabular}
    \caption{Comparison of Backplay with related work: Behavioral Cloning (BC), Generative Adversarial Imitation Learning (GAIL), and Reverse Curriculum Generation (RCG).}
    \label{table:algorithm-comparison}
\end{table}
```

## Table 2
```latex
\begin{table}
\centering
{
\small
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Algorithm} & \textbf{Map Set} & \textbf{\% Optimal} & \textbf{\% 0-5 Optimal} & \textbf{Avg Suboptimality}  & \textbf{Std Suboptimality} \\
\hline
Standard & All & 0 & 0 & N/A & N/A \\ \hline
Uniform & Optimal & 27 & 91 & 8.26 & 32.92 \\ \hline
Uniform & 5-Optimal & 51 & 98 & 2.04 & 17.39  \\ \hline
Uniform & 10-Optimal & 49 & 98 & 2.04 & 16.79  \\ \hline
Florensa & Optimal & 20 & 51 & 63.36 & 78.08  \\ \hline
Florensa & 5-Optimal & 48 & 77 & 25.44 & 56.89  \\ \hline
Florensa & 10-Optimal & 49 & 69 & 39.75 & 70.92  \\ \hline
% \cite{florensa2017reverse} mean & Optimal & 7.2 & 16.8 & 32.00 & 31.44  \\ \hline
% \cite{florensa2017reverse} mean & 5-Optimal & 14.4 & 24.2 & 40.79 & 39.43  \\ \hline
% \cite{florensa2017reverse} mean & 10-Optimal & 20.4 & 31.2 & 43.49 & 47.59  \\ \hline
Backplay & Optimal & \textbf{31} & \textbf{100} & $\textbf{0.64}$ & \textbf{4.96}  \\ \hline
Backplay & 5-Optimal & 37 & 94 & 7.94 & 33.35   \\ \hline
Backplay & 10-Optimal & \textbf{54} & 99 & $\textbf{0.37}$ & 3.49  \\ \hline
\end{tabular}
}
\caption{Results after 2000 epochs on 100 mazes. Note that for Backplay and Uniform, the Map Set is also the type of demonstrator, where N-optimal has demonstrations N steps longer than the shortest path. From left to right, the table shows: the percentage of mazes on which the agent optimally reaches the goal, percentage on which it reaches in at most five steps more than optimal, and the average and standard deviation of extra steps over optimal. Both Backplay and Uniform succeed on almost all mazes and, importantly, can outperform the experts' demonstrations. On the other hand, Standard does not learn a useful policy and Florensa fails to learn more than $50-70\%$ of the maps, which is why its sub-optimality mean and std is so high. Results for Backplay were generally consistent across all seeds. For others, we report their best score. See \ref{sec:maze-learning-curves} for further details.}
\label{table:Maze-results}
% \end{wraptable}    
\end{table}
```

## Table 3
```latex
\begin{table}[H]
\centering
{
\small
\begin{tabular}{|cc|}
\hline
Starting at training epoch & Uniform window \\ \hline
0 & [0, 4) \\ \hline
350 & [4, 8) \\ \hline
700 & [8, 16) \\ \hline
1050 & [16, 32) \\ \hline
1400 & [32, 64) \\ \hline
1750 & [64, 64) \\ \hline
\end{tabular}
}
\caption{Backplay hyperparameters for Maze.}
\label{table:backplay-maze}
\end{table}
```

## Table 4
```latex
\begin{table}[H]
\centering
{
\small
\begin{tabular}{|cc|}
\hline
Starting at training epoch & Uniform window \\ \hline
0 & [0, 32) \\ \hline
50 & [24, 64) \\ \hline
100 & [56, 128) \\ \hline
150 & [120, 256) \\ \hline
200 & [248, 512) \\ \hline
250 & [504, 800) \\ \hline
300 & [800, 800] \\ \hline
\end{tabular}
}
\caption{Backplay hyperparameters for Pommerman 4 maps.}
\label{table:backplay-pommerman-four}
\end{table}
```

## Table 5
```latex
\begin{table}[H]
\centering
{
\small
\begin{tabular}{|cc|}
\hline
Starting at training epoch & Uniform window \\ \hline
0 & [0, 32) \\ \hline
85 & [24, 64) \\ \hline
170 & [56, 128) \\ \hline
255 & [120, 256) \\ \hline
340 & [248, 512) \\ \hline
425 & [504, 800) \\ \hline
510 & [800, 800] \\ \hline
\end{tabular}
}
\caption{Backplay hyperparameters for Pommerman 100 maps.}
\label{table:backplay-pommerman-hundred}
\end{table}
```

## Table 6
```latex
\begin{table}[H]
\centering
{
\small
\begin{tabular}{|l|c|}
\hline
Win & Maps \\ \hline
90\% & 24 \\ \hline
80\% & 26 \\ \hline
70\% & 6 \\ \hline
60\% & 5  \\ \hline
50\% & 5 \\ \hline
\end{tabular}
}
% \captionsetup{width=8cm}
\caption{Aggregate per-map win rates of the model trained with Backplay on 100 Pommerman maps. The model was run over 5000 times in total, with at least 32 times on each of the 100 maps. The \textit{Maps} column shows the number of maps on which the Backplay agent had a success rate of at least the percent in the \textit{Win} column. Note that this model has a win rate of $>80\%$ on more than half of the maps and a win rate of $>50\%$ on all maps.}
\label{table:fx100}
\end{table}
```

## Table 7
```latex
\begin{table}[t]
\caption{Sample table title}
\label{sample-table}
\begin{center}
\begin{tabular}{ll}
\multicolumn{1}{c}{\bf PART}  &\multicolumn{1}{c}{\bf DESCRIPTION}
\\ \hline \\
Dendrite         &Input terminal \\
Axon             &Output terminal \\
Soma             &Cell body (contains cell nucleus) \\
\end{tabular}
\end{center}
\end{table}
```

