# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
    \caption{Dataset characteristics. Density is defined as the number of interactions per user (\#Interactions/\#Users).}
    \input{Table/dataset}
    \label{tab:datasets}
\end{table}
```

## Table 2
```latex
\begin{table*}
    \caption{Overall performance with Hit Rate@1 ($\uparrow$) on three datasets. The best result in each column is in boldface, while the second-best result is underlined. * means that some of the predictions are not valid (e.g., misspelling).}
    \input{Table/overall}
    \label{tab:overall_performance}
\end{table*}
```

## Table 3
```latex
\begin{table}
    \caption{Ablation study of IntervalLLM on the Video Games dataset. $\triangle$ indicates applying timestamp as the text prompt. $IntervalEMB$ indicates adding the interval embedding. $IIA$ indicates adding the interval-infused embeddings.}
    \input{Table/ablation}
    \label{tab:ablation}
\end{table}
```

## Table 4
```latex
\begin{table*}
    \caption{Performance on Warm/Cold scenarios evaluated by Hit Rate@1 ($\uparrow$) on the Video Games dataset. \emph{Warm} represents the warm scenario, \emph{Cold} represents the cold-start scenario, and \emph{Diff.} = ((\emph{Cold} - \emph{Warm})/\emph{Warm}).} %denotes the relative performance difference between the warm and cold-start scenarios.}
    \input{Table/33_cold_start}
    \label{tab:33cold_start}
\end{table*}
```

