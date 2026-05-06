# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[ht!]
    \centering 
    \footnotesize
    \begin{tabularx}{\textwidth}{X ccccccccc}
 
 \toprule
Static Embedding &  SimLex999 &    MEN &  WS353 &     RW &  Google &    MSR &  SemEval2012(2) &  BLESS &     AP \\
\midrule
GloVe &      0.194 &  0.216 &  0.339 &  0.127 &   0.189 &  0.312 &          0.097 &  0.390 &  0.308 \\
FastText        &      0.239 &  \bf 0.239 &  \bf 0.432 &  0.176 &   0.203 &  0.289 &          0.104 &  0.375 &  0.291 \\
ELMo, Layer 1         &      0.276 &  0.167 &  0.317 &  0.148 &   0.170 &  0.326 &          0.114 &  \bf 0.410 &  0.308 \\
ELMo, Layer 2       &      0.215 &  0.151 &  0.272 &  0.133 &   0.130 &  0.268 &          0.132 &  0.395 &  0.318 \\
BERT, Layer 1         &      0.315 &  0.200 &  0.394 & \bf  0.208 &   \bf 0.236 & \bf 0.389 & \bf 0.166 &  0.365 &  \bf 0.321 \\
BERT, Layer 2         &      \bf 0.320 &  0.166 &  0.383 &  0.188 &   0.230 &  0.385 &          0.149 &  0.365 & \bf 0.321 \\
BERT, Layer 11       &      0.221 &  0.076 &  0.319 &  0.135 &   0.175 &  0.290 &          0.149 &  0.370 &  0.289 \\
BERT, Layer 12        &      0.233 &  0.082 &  0.325 &  0.144 &   0.184 &  0.307 &          0.144 &  0.360 &  0.294 \\
GPT-2, Layer 1         &      0.174 &  0.012 &  0.176 &  0.183 &   0.052 &  0.081 &          0.033 &  0.220 &  0.184 \\
GPT-2, Layer 2         &      0.135 &  0.036 &  0.171 &  0.180 &   0.045 &  0.062 &          0.021 &  0.245 &  0.184 \\
GPT-2, Layer 11        &      0.126 &  0.034 &  0.165 &  0.182 &   0.031 &  0.038 &          0.045 &  0.270 &  0.189 \\
GPT-2, Layer 12        &      0.140 & -0.009 &  0.113 &  0.163 &   0.020 &  0.021 &          0.014 &  0.225 &  0.172 \\
\bottomrule

    \end{tabularx}
    \caption{The performance of various static embeddings on word embedding benchmark tasks. The best result for each task is in bold. For the contextualizing models (ELMo, BERT, GPT-2), we use the first principal component of a word's contextualized representations in a given layer as its static embedding. The static embeddings created using ELMo and BERT's contextualized representations often outperform GloVe and FastText vectors.   }
    \label{tab:benchmark}
\end{table*}
```

