# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[!h]
\caption{Better results with Stoch-GFN on the AMP generation task. Larger is better.}
\label{tab:amp}
\centering
\begin{tabular}{ccccc}
\toprule
 ~ & Top-$100$ reward & Number of modes \\
\midrule
MCMC  & $0.632\pm 0.035$& $3.67\pm 0.58$\\
A2C & $0.682\pm 0.032$ & $2.66\pm 0.58$\\
SAC & $0.754 \pm 0.047$& $4.33\pm 1.33$\\
GFN & $0.748 \pm 0.048$ & $3.0 \pm 3.0$\\
Stoch-GFN & {\highlight{$0.834 \pm 0.023$}} & {\highlight{$19.5 \pm 2.5$}}\\
\bottomrule
\end{tabular}
\end{table}
```

