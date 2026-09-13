# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}
    \centering
    \label{tab:main}
    %\small
    \begin{tabular}{@{}rcccccc}
    
    \toprule
    \multirow{2}{*}[-2pt]{Method} & \multicolumn{2}{c}{GSM8k} & \multicolumn{2}{c}{ProntoQA} & \multicolumn{2}{c}{\dataset}\\
    \cmidrule{2-7}
          & Acc. (\%) & \# Tokens & Acc. (\%) & \# Tokens & Acc. (\%) & \# Tokens \\
        \midrule
        % \cmidrule{1-8}
        CoT  & 42.9{\scriptsize$\ \pm$0.2} & 25.0 &  98.8{\scriptsize$\ \pm$0.8} & 92.5 &  77.5{\scriptsize$\ \pm$1.9} & 49.4 \\
        \midrule
        No-CoT  & 16.5{\scriptsize$\ \pm$0.5} & 2.2 & 93.8{\scriptsize$\ \pm$0.7}  & 3.0 & 76.7{\scriptsize$\ \pm$1.0} & 8.2 \\
        iCoT  & 30.0$^*$ &  2.2 &  99.8{\scriptsize$\ \pm$0.3} &  3.0 & 98.2{\scriptsize$\ \pm$0.3} & 8.2 \\
        Pause Token &  16.4{\scriptsize$\ \pm$1.8} & 2.2 & 77.7{\scriptsize$\ \pm$21.0} & 3.0 &  75.9{\scriptsize$\ \pm$0.7} & 8.2 \\
        % \midrule
        %ROSCOE & 0.60 & - & - & 0.57 & 0.79 & - & - \\
        \midrule
        
        \ours (Ours) & 34.1{\scriptsize$\ \pm$1.5} & 8.2  & 99.8{\scriptsize$\ \pm$0.2} & 9.0 &  97.0{\scriptsize$\ \pm$0.3} & 14.2 \\
        
        - \textit{w/o curriculum} & 14.4{\scriptsize$\ \pm$0.8} & 8.2 & 52.4{\scriptsize$\ \pm$0.4} & 9.0 &  76.1{\scriptsize$\ \pm$0.2} & 14.2 \\
        - \textit{w/o thought} & 21.6{\scriptsize$\ \pm$0.5}  & 2.3 &  99.9{\scriptsize$\ \pm$0.1} & 3.0 &  95.5{\scriptsize$\ \pm$1.1} & 8.2 \\
        - \textit {pause as thought} & 24.1{\scriptsize$\ \pm$0.7} & 2.2 & 100.0{\scriptsize$\ \pm$0.1} & 3.0 &  96.6{\scriptsize$\ \pm$0.8} & 8.2 \\
        % \midrule
    \bottomrule 
    \end{tabular}
    %%
     \small
    %\vspace{-5pt}
    \caption{Results on three datasets: GSM8k, ProntoQA and ProsQA. Higher accuracy indicates stronger reasoning ability, while generating fewer tokens indicates better efficiency. $^*$The result is from \citet{deng2024explicit}.}
    \label{tab:main}
\end{table*}
```

## Table 2
```latex
\begin{table}[]

    \centering
    \begin{tabular}{c|c|c|c}
    \toprule
         \# Nodes & \# Edges & Len. of Shortest Path & \# Shortest Paths \\
         \midrule
           23.0 & 36.0 & 3.8 & 1.6 \\
          \bottomrule
    \end{tabular}
    \captionsetup{justification=centering}
    \caption{Statistics of the graph structure in ProsQA.}
    \label{tab:prosqa}
\end{table}
```

## Table 3
```latex
\begin{table}[]

    \centering
    \begin{tabular}{r|c|c|c}
    \toprule
         Dataset & Training & Validation & Test \\
         \midrule
           GSM8k & 385,620 & 500 & 1319 \\
           ProntoQA & 9,000 & 200 & 800 \\
           ProsQA & 17,886 & 300 & 500 \\
          \bottomrule
    \end{tabular}
    \captionsetup{justification=centering}
    \caption{Statistics of the datasets.}
    \label{tab:stats}
\end{table}
```

## Table 4
```latex
\begin{table}[h!]
    \centering
    \label{tab:efficiency}
    \begin{tabular}{lccc}
        \toprule
        Method & GSM8k & ProntoQA & ProsQA \\
        \midrule
        No-CoT & 0.03 & 0.03 & 0.08 \\
        CoT    & 0.26 & 0.85 & 0.47 \\
        \ours   & 0.09 & 0.11 & 0.15 \\
        \bottomrule
        
    \end{tabular}
    
    \captionsetup{justification=centering}
    \caption{Inference time (in seconds) comparison across tasks and methods.}
\end{table}
```

## Table 5
```latex
\begin{table}[h]
\centering
\begin{tabular}{lcc}
\toprule
\textbf{Model} & \textbf{no-CoT} & \textbf{\ours (Ours)} \\ 
\midrule
Llama 3.2-3B & 26.0 & 31.7 \\
Llama 3-8B   & 42.2 & 43.6 \\
\bottomrule
\end{tabular}
\caption{Experimental results of applying \ours to larger Llama models. We report performance comparisons between models without CoT reasoning (no-CoT) and our proposed \ours method.}
\label{tab:coconut-large-models}
\end{table}
```

