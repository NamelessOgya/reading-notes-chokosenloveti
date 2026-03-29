# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[tp]
  \centering
  \fontsize{6.5}{6.8}\selectfont
  \caption{Performance of different methods.  * indicates statistically significant improvement of the proposed method to baseline models on t-test ($p < 0.05$). `Improve' indicates the relative improvements of ALKDRec over the strongest baseline. }
  \label{tab:RSComparison}
% \begin{tabular}{c|c|cccccccc|c|cc}
\begin{tabular}{c|c|c|cc|cccccc|c|c}\midrule\midrule
Datasets                        & \multicolumn{1}{l|}{Backbone} & Metric    & Student Rec & Teacher Rec & DE            & FTD              & HTD           & unKD    & DSL           & DLLM2Rec      & ALKDRec      & Improve.        \\\midrule\midrule
\multirow{12}{*}{Hetrec2011-ML} & \multirow{4}{*}{FPMC}          & recall@5  & 0.00730     & 0.01339     & 0.00690       & \underline{ 0.00933}    & 0.00893       & 0.00527 & 0.00527       & 0.00933       & \textbf{0.01258*} & 34.78\%         \\
                                &                                & ndcg@5    & 0.00379     & 0.00781     & 0.00358       & 0.00457          & \underline{ 0.00570} & 0.00361 & 0.00356       & 0.00467       & \textbf{0.00747*} & 31.10\%         \\
                                &                                & recall@10 & 0.01055     & 0.02191     & 0.01258       & \underline{ 0.01866}    & 0.01460       & 0.00893 & 0.00893       & 0.01623       & \textbf{0.02150*} & 15.22\%         \\
                                &                                & ndcg@10   & 0.00415     & 0.01002     & 0.00658       & \underline{ 0.00901}    & 0.00723       & 0.00426 & 0.00436       & 0.00731       & \textbf{0.01019*} & 13.06\%         \\\cline{2-13}
                                & \multirow{4}{*}{STAMP}         & recall@5  & 0.00609     & 0.00852     & 0.00852       & 0.00811          & 0.00609       & 0.00487 & \underline{ 0.00852} & 0.00609       & \textbf{0.01014*} & 19.05\%         \\
                                &                                & ndcg@5    & 0.00364     & 0.00446     & \underline{ 0.00529} & 0.00450          & 0.00337       & 0.00309 & 0.00452       & 0.00364       & \textbf{0.00670*} & 26.76\%         \\
                                &                                & recall@10 & 0.01177     & 0.01907     & \underline{ 0.01501} & 0.01298          & 0.01217       & 0.01014 & 0.01298       & 0.01217       & \textbf{0.01623*} & 8.11\%          \\
                                &                                & ndcg@10   & 0.00563     & 0.00937     & \underline{ 0.00729} & 0.00616          & 0.00517       & 0.00509 & 0.00542       & 0.00575       & \textbf{0.00799*} & 9.58\%          \\\cline{2-13}
                                & \multirow{4}{*}{AttMix}        & recall@5  & 0.00122     & 0.00527     & 0.00527       & \textbf{0.00649} & 0.00325       & 0.00365 & 0.00527       & 0.00527       & \underline{0.00609 }         & -6.25\%         \\
                                &                                & ndcg@5    & 0.00067     & 0.00361     & 0.00306       & \underline{ 0.00332}    & 0.00222       & 0.00235 & 0.00306       & 0.00284       & \textbf{0.00370*} & 11.40\%         \\
                                &                                & recall@10 & 0.00406     & 0.00933     & 0.00933       & 0.01014          & 0.00730       & 0.00568 & 0.00933       & \underline{ 0.01055} & \textbf{0.01095*} & 3.84\%          \\
                                &                                & ndcg@10   & 0.00180     & 0.00419     & 0.00409       & 0.00366          & 0.00351       & 0.00262 & 0.00406       & \underline{ 0.00448} & \textbf{0.00547*} & 22.14\%         \\\midrule\midrule
\multirow{12}{*}{Amazon-Games}  & \multirow{4}{*}{FPMC}          & recall@5  & 0.03309     & 0.05773     & 0.02886       & 0.03260          & \underline{ 0.03459} & 0.00921 & 0.03211       & 0.03409       & \textbf{0.03583*} & 3.60\%          \\
                                &                                & ndcg@5    & 0.01857     & 0.03322     & 0.01471       & 0.01869          & 0.01917       & 0.00504 & 0.01802       & \underline{ 0.01954} & \textbf{0.02188*} & 11.98\%         \\
                                &                                & recall@10 & 0.05101     & 0.08311     & 0.04703       & 0.05126          & \underline{ 0.05200} & 0.01643 & 0.04331       & 0.05126       & \textbf{0.05748*} & 10.53\%         \\
                                &                                & ndcg@10   & 0.02199     & 0.03688     & 0.01938       & \underline{ 0.02251}    & 0.02199       & 0.00696 & 0.01891       & 0.02225       & \textbf{0.02610*} & 15.97\%         \\\cline{2-13}
                                & \multirow{4}{*}{STAMP}         & recall@5  & 0.03583     & 0.05375     & 0.02937       & 0.03359          & 0.03085       & 0.01643 & 0.03086       & \underline{ 0.03608} & \textbf{0.03707} & {2.76\%} \\
                                &                                & ndcg@5    & 0.02025     & 0.03091     & 0.01624       & 0.01938          & 0.01689       & 0.00850 & 0.01777       & \underline{ 0.02051} & \textbf{0.02103} & {2.55\%} \\
                                &                                & recall@10 & 0.04902     & 0.07066     & 0.04231       & 0.05051          & 0.04877       & 0.02290 & 0.04505       & \underline{ 0.05051} & \textbf{0.05325*} & 5.42\%          \\
                                &                                & ndcg@10   & 0.02119     & 0.03104     & 0.01724       & \underline{ 0.02246}    & 0.02215       & 0.00934 & 0.01905       & 0.02188       & \textbf{0.02342*} & 4.26\%          \\\cline{2-13}
                                & \multirow{4}{*}{AttMix}        & recall@5  & 0.01916     & 0.04379     & 0.01095       & 0.00325          & 0.01568       & 0.00406 & 0.00487       & \underline{ 0.01866} & \textbf{0.01916} & {2.67\%} \\
                                &                                & ndcg@5    & 0.01144     & 0.02546     & 0.00600       & 0.00206          & 0.00910       & 0.00234 & 0.00280       & \underline{ 0.01103} & \textbf{0.01118} & {1.33\%} \\
                                &                                & recall@10 & 0.02264     & 0.05200     & 0.01717       & 0.00690          & 0.02140       & 0.00649 & 0.00933       & \underline{ 0.02215} & \textbf{0.02936*} & 32.59\%         \\
                                &                                & ndcg@10   & 0.00983     & 0.02315     & 0.00687       & 0.00323          & 0.00977       & 0.00310 & 0.00355       & \underline{ 0.00987} & \textbf{0.01343*} & 36.07\%        \\\midrule\midrule
\end{tabular}
\end{table*}
```

## Table 2
```latex
\begin{table}
% \caption{Statistics of the experimental datasets} \centering
% % For LaTeX tablesd use
%   \fontsize{9}{10}\selectfont
% \begin{tabular}{p{2.5cm}p{1.1cm}p{1.1cm}p{1.5cm}l}
% \hline\noalign{\smallskip}
%  &\#Sessions &\#Items&\#Interactions  \\
% \noalign{\smallskip}\hline\noalign{\smallskip}
% Hetrec2011-ML & 12,323  & 8,475 & 112,034 \\
% Amazon-Games &  20,091  & 26,138 & 132,677  \\ 
% \noalign{\smallskip} \hline
% \end{tabular} \label{Table_es}
% \end{table}
```

## Table 3
```latex
\begin{table}[tp]
  \centering
  \fontsize{7}{7}\selectfont
  \caption{Performance of the variants for ablation studies measured by recall (R@10) and ndcg (N@10). }
  \label{table_ablation}
\begin{tabular}{|c|cc|cc|cc|}
        \midrule \multicolumn{7}{|c|}{Hetrec2011-ML}    \\\midrule
Backbone & \multicolumn{2}{c|}{FPMC}            & \multicolumn{2}{c|}{STAMP}           & \multicolumn{2}{c|}{AttMix}          \\\midrule
Metric     & R@10        & N@10          & R@10        & N@10          & R@10        & N@10          \\\midrule
TR         & 0.01907          & 0.00897          & 0.01055          & 0.00476          & 0.00852          & 0.00375          \\
Random     & 0.01907          & 0.00856          & 0.01339          & 0.00755          & 0.00974          & 0.00469          \\
Easiest    & 0.01623          & 0.00693          & 0.01542          & 0.00754          & 0.00933          & 0.00426          \\
Hardest    & 0.01298          & 0.00639          & 0.01582          & 0.00756          & 0.00933          & 0.00439          \\
RAD-BC   & 0.01420          & 0.00658          & 0.01177          & 0.00601          & \textbf{0.01136} & 0.00519          \\
ALKDRec  & \textbf{0.02150} & \textbf{0.01019} & \textbf{0.01623} & \textbf{0.00799} & 0.01095          & \textbf{0.00547} \\\midrule\midrule
\multicolumn{7}{|c|}{Amazon-Games}         \\\midrule
Backbone& \multicolumn{2}{c|}{FPMC}            & \multicolumn{2}{c|}{STAMP}           & \multicolumn{2}{c|}{AttMix}          \\\midrule
Metric     & R@10        & N@10          & R@10        & N@10          & R@10        & N@10          \\\midrule
TR         & 0.05175          & 0.02238          & 0.05200          & 0.02223          & 0.02264          & 0.01002          \\
Random     & 0.05101	      & 0.02239          & 0.05225          & 0.02203          & 0.02538          & 0.01132          \\
Easiest    & 0.05076	      & 0.02238         & 0.05026          & 0.02161          & 0.01966          & 0.00905          \\
Hardest    & 0.04877	      & 0.02133          & 0.05001          & 0.02173          & 0.02239          & 0.00997          \\
RAD-BC   & 0.05200	      & 0.02321          & 0.05225          & 0.02228          & 0.02712          & 0.01210          \\
ALKDRec  & \textbf{0.05748} & \textbf{0.02610} & \textbf{0.05325} & \textbf{0.02342} & \textbf{0.02936} & \textbf{0.01343} \\\midrule         
\end{tabular}
\end{table}
```

