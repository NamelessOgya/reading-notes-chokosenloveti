# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[h!]
\centering
\begin{tabular}{c|ccc}
\hline
       & Beauty & Sports & Toys \\ \hline
$\text{R-square}$  & 0.94  & 0.97   & 0.94 \\
$R_0$  & 0.4529   & 3e-1   & 1.7e-1 \\
$A$    & 16.8  & 24.8 & 6.1 \\
$B$    & 1e-2 & 1e-2 & 1e-2 \\
$a$    & 0.6 & 0.63 & 0.52 \\
$b$    & 2.23 & 1.97 & 2.02 \\ \hline
\end{tabular}
\caption{The fitted empirical parameters of scaling laws of SID-based GR.}
\label{tab:fitted_params_SID}
\end{table}
```

## Table 2
```latex
\begin{table}[h!]
\centering
\small
\begin{tabular}{r|ccccc}
\hline
\textbf{\#Params} & \textbf{\#Layers} & $\mathbf{d_{\text{model}}}$ & \textbf{\#Heads} & $\mathbf{d_{\text{kv}}}$ & $\mathbf{d_{\text{ff}}}$ \\
\hline
336{,}000 & 1 & 64  & 3  & 64 & 512  \\
778{,}000 & 2 & 64  & 3  & 64 & 512  \\
1{,}900{,}000 & 5 & 64  & 3  & 64 & 512  \\
3{,}300{,}000 & 9 & 64  & 3  & 64 & 512  \\
6{,}700{,}000 & 3 & 128 & 6  & 64 & 1024 \\
13{,}000{,}000 & 4 & 128 & 6 & 64 & 1024 \\
21{,}000{,}000 & 7 & 128 & 6  & 64 & 1024 \\
43{,}000{,}000 & 8 & 192 & 9  & 64 & 1536 \\
88{,}000{,}000 & 9 & 320 & 15 & 64 & 2560 \\
192{,}000{,}000 & 20 & 384 & 18 & 64 & 3072 \\
\hline
\end{tabular}
\label{tab:scale RS}
\caption{The details of scaling RS module in SID-based GR. The \#Params are just rounded values. The \#Layers are the same for both encoder and decoder in the module.}
\end{table}
```

## Table 3
```latex
\begin{table}[h]
\centering
\begin{tabular}{rccc}
\hline
\textbf{\#Params} & \textbf{\#Layers} & $\mathbf{d_{\text{model}}}$ & \textbf{\#Heads} \\
\hline
   98,304      & 2  & 64   & 2  \\
  786,432      & 4  & 128  & 4  \\
1,572,864      & 8  & 128  & 4  \\
6,291,456      & 8 & 256  & 8  \\
25,165,824     & 8 & 512  & 8  \\
75,497,472    & 24 & 512 & 8 \\
\hline
\end{tabular}
\label{tab:details of scaling sasrec}
\caption{The details of scaling the SASRec model.}
\end{table}
```

## Table 4
```latex
\begin{table}[h]
\centering
\begin{tabular}{lrrr}
\toprule
\textbf{Dataset} & \textbf{\# users} & \textbf{\# items} & \textbf{\# actions}  \\
\midrule
\textit{Beauty} & 22,363 & 12,101 & 198,502 \\
\textit{Toys and Games} & 19,412 & 11,924 & 167,597 \\
\textit{Sports and Outdoors} & 35,598 & 18,357 & 296,337\\\bottomrule
\end{tabular}
\caption{Statistics of the datasets used in our experiments.}
\label{tab:dataset_stats}
\end{table}
```

## Table 5
```latex
\begin{table}[h]
\centering
\begin{tabular}{c|cccc}
\hline
       & Qwen3-0.6B    & Qwen3-1.7B     & Qwen3-4B    & Qwen3-8B   \\ \hline
Beauty  & 0.0356 & 0.0379 & 0.0393 & 0.0409 \\ 
Sports  & 0.0197 & 0.0217 & 0.0225 & 0.0234 \\ 
Toys  & 0.0367 & 0.0380 & 0.0392 & 0.0398 \\ \hline
\end{tabular}
\caption{The results when we input SIDs as item representations into the LLM.}
\label{tab:SIDs_into_LLM}
\end{table}
```

## Table 6
```latex
\begin{table}[h]
\centering
\begin{tabular}{c|cc}
\hline
       & SID-based GR   & LLM-as-RS      \\ \hline
Beauty  & 0.018 & \textbf{0.030} \\ 
Sports  & 0.006 & \textbf{0.014}   \\ 
Toys  & 0.022 & \textbf{0.028}  \\ \hline
\end{tabular}
\caption{The comparison on the cold-start items. LLM-as-RS consistently outperforms SID-based GR.}
\label{tab:cold_start}
\end{table}
```

## Table 7
```latex
\begin{table}[h!]
\centering
\begin{tabular}{c|ccc}
\hline
       & Beauty & Sports & Toys \\ \hline
$R_0$  & 3e-1   & 3e-1   & 1.7e-1 \\
$A$    & 9.9e2  & 9.87e2 & 2.19e-1 \\
$B$    & 3.4e-1 & 3.35e-1 & 9.93e2 \\
$\gamma$ & 9.08e-2 & 1.82e-2 & 1.74e-1 \\
$\beta$  & 2.10e-2 & 1.69e-2 & 2.29e-2 \\
$a$    & 1.98e1 & 2.02e1 & 2.47e-2 \\
$b$    & 1.39e-2 & 9.47e-3 & 2.02e1 \\ \hline
\end{tabular}
\caption{The fitted empirical parameters in Section~\ref{subsec:llm_rs_scale}.}
\label{tab:fitted_params}
\end{table}
```

## Table 8
```latex
\begin{table}[h!]
\centering
\begin{tabular}{c|cc}
\hline
 & $\beta=0$ & $\beta>0$ \\ \hline
Beauty & 4.2e-4 & \textbf{3.5e-4} \\ 
Sports & 1e-3 & \textbf{3.6e-4} \\ 
Toys & 1.2e-3 & \textbf{9.8e-4} \\ \hline
\end{tabular}
\caption{Held-out fitting errors (the lower the better) of Equation~\ref{eq:llm_scaling_law} when $\beta=0$ and $\beta>0$.}
\label{tab:held_errors}
\end{table}
```

