# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[H]
\caption{\textbf{PTV dose metrics}. Several dose metrics of the PTV target are displayed for all the clinical and TextGrad optimized plans, including the mean and minimum doses, as well as the $D_{95}$. For all the metrics, we include the average deviations from the clinical goal across 5 plans and the standard deviation in brackets. Values in bold represent the best for each PTV target.}

    \begin{tabular}{@{}llllll@{}}
    \toprule
    \textbf{Target} & \textbf{Method}   & \textbf{Mean dose [Gy]} & \textbf{Min dose [Gy]}  & \textbf{Max dose [Gy]}
    & \textbf{$\textbf{D}_{95}$ [Gy]}   \\ \midrule
    \multirow{3}{*}{PTV} & Clinical Goal & 70.20 & $\approx70.20$ & $\approx70.20$ & 70.20 \\ 
                             & Radiation Oncologist & +1.97 (0.36) & -8.88 (2.31) & +4.66 (0.82 )& -0.10 (0.15) \\
                             & \textgrad & \textbf{+0.51} (0.09) & \textbf{-8.48} (2.38) & \textbf{+3.63} (0.87) &  \textbf{+0.00} (0.00)  \\
                             \bottomrule
    \end{tabular}
    \centering
    \label{tab:ptv}
\end{table}
```

## Table 2
```latex
\begin{table}[H]
\caption{\textbf{Organs at Risk (OARs) dose metrics}. We show mean dose capturing OAR sparing. Lower values demonstrate better OAR sparing which is desirable, as this number indicates organs at risk, which should not get more than dosage than what is listed in the clinical guidelines. For all the metrics, we include the average mean dose across 5 plans and the standard deviation in brackets.}

    \begin{tabular}{@{}llllc@{}}
    \toprule
    \textbf{Organ} & \textbf{Method} & \textbf{Mean dose [Gy] $\downarrow$} & \textbf{$\textbf{D}_5$$\downarrow$} & \textbf{$\textbf{D}_{50}$$\downarrow$}\\ \midrule

    \multirow{2}{*}{Rectum} & Radiation Oncologist & 23.88 (6.45) & 64.26 (10.00) & 20.04 (5.50)  \\
                             & \textgrad & \textbf{17.18} (4.2) & \textbf{58.82} (18.81) & \textbf{9.54} (0.70)\\ \midrule
    \multirow{2}{*}{Bladder} & Radiation Oncologist & 22.39 (5.55) & 67.81 (6.44) & 14.78 (8.42) \\
                            & \textgrad &  \textbf{20.92} (0.79) & \textbf{65.96} (6.96) & \textbf{14.11} (3.17) 
   \\ \bottomrule
    \end{tabular}
    \centering
    \label{tab:oar}
\end{table}
```

## Table 3
```latex
\begin{table}[!h]
\caption{Code optimization for LeetCode Hard using \gpto. Results are averaged over 5 seeds.}
    \begin{tabular}{@{}lll@{}}
    \toprule
    \textbf{Task} & \textbf{Method}   & \textbf{Completion Rate}   \\ \midrule
    \multirow{3}{*}{LeetCode Hard~\citep{reflexion}} & Zero-shot~\cite{reflexion} & $0.26$ \\ & Reflexion (1 demonstration, 5 iterations)~\citep{reflexion} & $0.31 \pm 0.012$ \\
    & \textgrad~ (0 demonstrations, 5 iterations) &  $\mathbf{0.36} \pm 0.018 $ \\
    \bottomrule
    \end{tabular}
    \centering
    \label{tab:code-optimization}
\end{table}
```

## Table 4
```latex
\begin{table}[!h]
\caption{Solution optimization for zero-shot question answering with \gpto.}
    \begin{tabular}{@{}lll@{}}
    \toprule
    \textbf{Dataset} & \textbf{Method}   & \textbf{Accuracy~($\%$)} \\ \midrule
    \multirow{3}{*}{Google-proof QA~\citep{rein2023gpqa}} & CoT~\citep{wei2022chain, kojima2022large} & $51.0$   \\ 
    & Best reported~\citep{openai2024hello} & $53.6$   \\ 
    & \textgrad & $\mathbf{55.0}$ \\ \midrule
    \multirow{2}{*}{MMLU-Machine Learning~\citep{hendrycks2021measuring}} & CoT~\citep{wei2022chain, kojima2022large} & $85.7$   \\ 
    & \textgrad & $\mathbf{88.4}$ \\ \midrule
    \multirow{2}{*}{MMLU-College Physics~\citep{hendrycks2021measuring}} & CoT~\citep{wei2022chain, kojima2022large} & $91.2$   \\ 
    & \textgrad & $\mathbf{95.1}$ \\ 
    \bottomrule
    \end{tabular}
    \centering
    \label{tab:solution-optimization}
\end{table}
```

## Table 5
```latex
\begin{table}[!h]
\caption{\textbf{Prompt optimization for reasoning tasks.} With \textgrad, we optimize a system prompt for \texttt{gpt-3.5-turbo}~using~\gpto~as the gradient engine that provides the feedback during backpropagation.}
    \begin{tabular}{@{}lll@{}}
    \toprule
    \textbf{Dataset} & \textbf{Method}   & \textbf{Accuracy~($\%$)}\\ \midrule
    \multirow{3}{*}{Object Counting~\citep{suzgun-etal-2023-challenging, srivastava2023beyond}} & CoT (0-shot)~\citep{wei2022chain, kojima2022large} & $77.8$ \\ & DSPy (BFSR, 8 demonstrations)~\citep{khattab2024dspy} & $84.9$  \\
    & \textgrad~(instruction-only, 0 demonstrations) & $\mathbf{91.9}$  \\
    \midrule
    \multirow{3}{*}{Word Sorting~\citep{suzgun-etal-2023-challenging, srivastava2023beyond}} & CoT (0-shot)~\citep{wei2022chain, kojima2022large} & $76.7$ \\ & DSPy (BFSR, 8 demonstrations)~\citep{khattab2024dspy} & $\mathbf{79.8}$  \\
    & \textgrad~(instruction-only, 0 demonstrations) & $\mathbf{79.8}$    \\
   \midrule
    \multirow{3}{*}{GSM8k~\citep{cobbe2021gsm8k}} & CoT (0-shot)~\citep{wei2022chain, kojima2022large} & $72.9$ \\ & DSPy (BFSR, 8 demonstrations)~\citep{khattab2024dspy} & $\mathbf{81.1}$   \\
    & \textgrad~(instruction-only, 0 demonstrations) & $\mathbf{81.1}$ \\
    \bottomrule
    \end{tabular}
    \centering
    \label{tab:prompt-optimization}
\end{table}
```

