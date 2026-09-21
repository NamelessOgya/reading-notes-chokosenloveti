# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[H]
\centering
\begin{tabular}{ll}
    \toprule
    Symbol & Description \\ %[0.5ex] 
    \midrule
    $\mathcal{S}$ & state space \\
    $\X$ & object (terminal state) space, subset of $\mathcal{S}$\\
    $\A$ & action / transition space (edges $\s\to\s'$)\\
    $\mathcal{G}$ & directed acyclic graph $(\mathcal{S},\A)$ \\
    $\mathcal{T}$ & set of complete trajectories \\
    $\s$ & state in $\mathcal{S}$\\
    $\s_0$ & initial state, element of $\mathcal{S}$ \\
    $\x$ & terminal state in $\X$ \\
    $\tau$ & trajectory in $\mathcal{T}$ \\
    $F: \mathcal{T} \to \R$ & Markovian flow\\
    $F: \mathcal{S} \to \R$ & state flow\\
    $F: \A \to \R$ & edge flow\\
    $P_F$ & forward policy (distribution over children) \\
    $P_B$ & backward policy (distribution over parents) \\
    $Z$ & scalar, equal to $\sum_{\tau\in\mathcal{T}}F(\tau)$ for a Markovian flow \\
    \bottomrule
\end{tabular}
% \caption{Caption}
% \label{tab:my_label}
\end{table}
```

