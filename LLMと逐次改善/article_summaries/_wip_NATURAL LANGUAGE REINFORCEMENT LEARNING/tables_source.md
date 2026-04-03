# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[htbp]
%   \centering
%   \renewcommand{\arraystretch}{1.5}
%   \begin{tabular}{|m{1.5cm}|m{12cm}|}
%     \hline
%     \textbf{Methods} & \textbf{Reasoning After Training} \\
%     \hline
%     \textbf{RAGEN} 
%     & 
%     \begin{minipage}[c]{0.25\linewidth}
%       \raisebox{-\height}{\includegraphics[width=\linewidth]{figs/frozenlake/frozenlake_map.pdf}}
%     \end{minipage}
%     \begin{minipage}[c]{0.75\linewidth}
%       \small \texttt{(THINK):} My thoughts are to go to the goal \newline 
%       \small \texttt{(Action):} Up %|| Right
%     \end{minipage} \\
%     \hline
%     \textbf{NLRL} & 
%     \small \texttt{(THINK):} Based on the evaluations of the next board positions, moving up results in the highest final evaluation of +5, indicating that P is one block closer to the goal position G after the move. Although there is a hole one block away from P after moving up, the potential strategy of moving up and then moving right can help P avoid the hole and arrive at the goal position. In contrast, moving left does not immediately change P's position, and moving down  moves P away from the goal position G. Therefore, moving up is the most favourable move. \newline 
%     \small \texttt{(Action):} Up \\
%     \hline
%   \end{tabular}
%   \caption{Comparing detailed reasoning on FrozenLake environment between RAGEN \citep{wang2025ragen} and NLRL (Ours) using \textit{Llama3.1-8B-Instruct} as the backbone model.}
%   \label{tab:ragen_vs_nlrl}
% \end{table}
```

## Table 2
```latex
\begin{table*}[t]
\vspace{-10pt}
\caption{Language GPI results with ablations on look-ahead steps $N$ and variations number $K$.}
\small
\centering
\begin{tabular}{c|c|c}
\toprule
\centering
  \textbf{Avg Reward} & \textbf{Double T Maze} & \textbf{Medium Maze} \\\midrule 
 \textit{Language policy $\pi^L(s)$ (\ding{172})} &$-27.29\pm4.43$ & $-27.05\pm5.27$ \\
 \textit{Language value function $Q^L(s,a)$ + improvement $I$ (\ding{173},\ding{176})} & $-18.33\pm6.11$ & $-33.57\pm14.41$ \\
 \textit{Language GPI (1 variation, 3 look ahead steps) (\ding{173}, \ding{174}, \ding{176})} & $-17.85\pm3.68$ & $-20.85\pm7.59$ \\
 \textit{Language GPI (4 variations, 1 look ahead steps) (\ding{173}, \ding{174}, \ding{176})} & $-17.48\pm4.53$ & $ -12.65\pm4.72$ \\
 \textit{Language GPI (4 variations, 3 look ahead steps) (\ding{173}, \ding{174}, \ding{176})} & $-12.74\pm4.47$ & $-15.09\pm4.44$   \\
 \textit{Language GPI (6 variations, 3 look ahead steps) (\ding{173}, \ding{174}, \ding{176})} & $-12.15\pm2.96$ & $-15.44\pm4.97$ \\
 \textit{Language GPI (8 variations, 3 look ahead steps) (\ding{173}, \ding{174}, \ding{176})} & $\mathbf{-11.19\pm2.86}$ & $\mathbf{-12.23\pm4.49}$  \\ \bottomrule
\end{tabular}
\vspace{-10pt}
\label{tab:language_td}
\end{table*}
```

## Table 3
```latex
\begin{table}[H]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Parameter} & \textbf{Value} \\
\midrule
Parallel Environments & 192 \\
Lookahead Step & 4 \\
Lookahead Rollout Number & 4 \\
Deduplicate State & True \\
\bottomrule
\end{tabular}
\caption{Rollout Parameters}
\end{table}
```

## Table 4
```latex
\begin{table}[H]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{LLM Sampling Parameter} & \textbf{Value} \\
\midrule
Temperature & 1.0 \\
Top K & 50 \\
Top P & 0.95 \\
Max Tokens & 512 \\
\bottomrule
\end{tabular}
\caption{LLM sampling parameters for prompting.}
\end{table}
```

## Table 5
```latex
\begin{table}[H]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Parameter} & \textbf{Value} \\
\midrule
Max Sequence Length & 1024 \\
Warmup Ratio & 0.03 \\
Learning Rate & 2e-5 \\
Learning Rate Scheduler & Constant \\
Dtype & bfloat16 \\
Per Device Train Batch Size & 4 \\
Gradient Accumulation Step & 8 \\
Training Epoch & 2 \\
Number of GPUs & 4 \\
Distributed Framework & FSDP \\
\bottomrule
\end{tabular}
\caption{Data Collection Parameters}
\end{table}
```

## Table 6
```latex
\begin{table}[H]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Parameter} & \textbf{Value} \\
\midrule
Parallel Environments & 64 \\
Trajectories per Iteration & 512 \\
Monte Carlo Samples ($K_{MC}$) & 5 \\
Policy Samples per State ($N_{sample}$) & 10 \\
Top-k Actions & 10 \\
\bottomrule
\end{tabular}
\caption{Data Collection Parameters}
\label{tab:data_collection_params}
\end{table}
```

## Table 7
```latex
\begin{table}[H]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Hyperparameter} & \textbf{Value} \\
\midrule
Learning Rate & 1e-5 \\
Learning Rate Schedule & Constant \\
Training Epochs per Iteration & 2 \\
FSDP Configuration & Full Sharding \\
Gradient Checkpointing & Enabled \\
Batch Size & 8 \\
Max Sequence Length & 1024 \\
Training Hardware & 4 × H100 GPUs \\
\bottomrule
\end{tabular}
\caption{Model Training Hyperparameters}
\label{tab:training_params}
\end{table}
```

## Table 8
```latex
\begin{table}[H]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Parameter} & \textbf{Value} \\
\midrule
Buffer History Length ($K_{buffer}$) & 3 iterations \\
Merging Strategy & Equal sampling \\
Buffer Content & State-action pairs with MC estimates \\
\bottomrule
\end{tabular}
\caption{Buffer Management Configuration}
\label{tab:buffer_params}
\end{table}
```

## Table 9
```latex
\begin{table}[H]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Parameter} & \textbf{Value} \\
\midrule
MC Trajectories per State-Action & 5 \\
Trajectory Completion & Full game \\
Value Aggregation & Average over returns \\
Sampling Temperature & 0.7 \\
Action Space Size & 9 positions (0-8) \\
\bottomrule
\end{tabular}
\caption{Policy Evaluation Configuration}
\label{tab:policy_eval_params}
\end{table}
```

## Table 10
```latex
\begin{table}[htbp]
\centering
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Parameter} & \textbf{Value} \\
\midrule
Learning Rate (Actor) & 1e-5 \\
Learning Rate (Critic) & 1e-5 \\
PPO Epochs & 1 \\
Batch Size & 16 \\
Gradient Accumulation Steps & 2 \\
Value Loss Coefficient & 0.5 \\
Entropy Coefficient & 0.01 \\
PPO Clip Range & 0.2 \\
Discount Factor ($\gamma$) & 0.99 \\
GAE Parameter ($\lambda$) & 0.95 \\
\bottomrule
\end{tabular}
\caption{PPO Training Hyperparameters}
\label{tab:ppo_hyperparameters}
\end{table}
```

## Table 11
```latex
\begin{table}[htbp]
  \centering
  \renewcommand{\arraystretch}{1.5}
  \begin{tabular}{|m{1.5cm}|m{0.8cm}|m{4cm}|m{6cm}|}
    \hline
    \textbf{Methods} & \textbf{Map} & \textbf{Initial Stage} & \textbf{Late Training} \\
    \hline
    {RAGEN} (\textit{Qwen2.5-0.5B-Instruct}) & 
    \multirow{3}{*}{\raisebox{-3.5cm}{\begin{tabular}{@{}l@{}}
      \texttt{\_G0\_} \\
      \texttt{\_\_\_O} \\
      \texttt{PO\_\_} \\
      \texttt{\_\_\_\_}
    \end{tabular}}} & 
    \small \texttt{(THINK):} Let's start by considering the initial state: \textit{<MAP>}. The goal is to reach the target 'PO\_\_\_' from the hole 'O\_\_O\_\_O\_\_O'. I'll start by moving to the left to avoid the hole. \newline 
    \small \texttt{(Action):} Left || Up & 
    \small \texttt{(THINK):} Forbid the goal and go left then up. \newline 
    \small \texttt{(Action):} Left || Up \\
    \cline{1-1} \cline{3-4}
    {RAGEN} (\textit{Qwen2.5-7B-Instruct}) &  & 
    \small \texttt{(THINK):} Move left to avoid the hole and then go up to reach the goal. \newline 
    \small \texttt{(Action):} Left || Up & 
    \small \texttt{(THINK):} Up may lead to the hole or the target. \newline 
    \small \texttt{(Action):} Up || Up \\
    \cline{1-1} \cline{3-4}
    {RAGEN} (\textit{Llama3.1-8B-Instruct}) &
    & 
    \small \texttt{(THINK):} To avoid the hole and go to the target, I should go up to stay safe and then move to the right to approach the goal from a safe distance. \newline 
    \small \texttt{(Action):} Up || Right & 
    \small \texttt{(THINK):} My thoughts are to go to the goal \newline 
    \small \texttt{(Action):} Up || Right \\
    \cline{1-1} \cline{3-4}
    \textbf{NLRL} (\textit{Llama3.1-8B-Instruct}) & & 
    \small \texttt{(THINK):} The current board position is <\textit{MAP}>. The goal is on the top left, and the player is on the bottom left. The player is not in the hole. The available moves are 1, 2, 3, 4. Since the player is already on the leftmost position, moving left is not an option. The player can move down to get closer to the goal. Therefore, the best next move for P is to play action 2 to move down.  \newline 
    \small \texttt{(Action):} Down & 
    \small \texttt{(THINK):} Based on the evaluations of the next board positions, moving up results in the highest final evaluation of +5, indicating that P is one block closer to the goal position G after the move. Although there is a hole one block away from P after moving up, the potential strategy of moving up and then moving right can help P avoid the hole and arrive at the goal position. In contrast, moving left does not immediately change P's position, and moving down  moves P away from the goal position G. Therefore, moving up is the most favourable move. \newline 
    \small \texttt{(Action):} Up \\
    \hline
  \end{tabular}
  \vspace{0.3cm}
  \caption{Comparing detailed reasoning on FrozenLake environment between RAGEN \citep{wang2025ragen} and NLRL (Ours). No matter what backbone model we used, RAGEN style of training will downgrade the model only to output the simplest reasoning. Our method encourages the model to develop rigorous reasoning as the training progresses.}
  \label{tab:ragen_vs_nlrl_full}
\end{table}
```

