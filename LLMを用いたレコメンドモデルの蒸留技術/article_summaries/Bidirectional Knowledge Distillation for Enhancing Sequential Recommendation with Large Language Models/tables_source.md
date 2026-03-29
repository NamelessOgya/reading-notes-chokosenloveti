# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\small
  \centering
  \caption{Statistics of datasets}
  \begin{tabular}{lrrrrr}
    \toprule
    Dataset & \# Users & \# Items & \# Interactions & Density \\
    \midrule
    Beauty & 22,363 & 12,101 & 198,502 & 0.07\% \\
    Sports & 25,598 & 18,357 & 296,337 & 0.06\% \\
    Toys & 19,412 & 11,924 & 167,597 & 0.07\% \\
    Yelp & 30,431 & 20,033 & 316,354 & 0.05\% \\
    \bottomrule
  \end{tabular}

    \label{tab:dataset-stats}
\end{table}
```

## Table 2
```latex
\begin{table*}[htbp]
\centering
\caption{Performance comparison of different methods. For fair evaluation, we report the results of CRM-centric methods and LLM-centric methods separately. The best result for each metric is bolded, and the second best is underlined. 'Imp.s' indicates the relative improvement of our framework on the corresponding backbone (SASRec or E4SRec), while 'Imp.b' indicates the improvement over the best baseline within the same category.}
\renewcommand{\arraystretch}{1.2}
\begin{adjustbox}{max width=\textwidth}
%\setlength{\tabcolsep}{2pt}
\begin{tabular}{l l|cccccc|ccc|cc|ccc}
\toprule
\multirow{2}{*}{\textbf{Dataset}} & \multirow{2}{*}{\textbf{Metric}} & \multicolumn{9}{c|}{\textbf{CRM-centric methods}} & \multicolumn{5}{c}{\textbf{LLM-centric methods}} \\

\cmidrule(r){3-11} \cmidrule(r){12-16}
& & GRU4Rec  & SASRec & S$^3$Rec & DLLM2Rec & LLM-CF & LEADER & \myStringC  & Imp.s & Imp.b & E4SRec & LLM-SRec & \myStringL & Imp.s & Imp.b \\
\midrule

\multirow{6}{*}{\textbf{Beauty}} 
& HR@5  &0.0165 & 0.0260 & 0.0262 & 0.0316 & \underline{0.0377} & 0.0299 & \textbf{0.0453} & 74.23\% & 20.16\% & \underline{0.0518} & 0.0510 & \textbf{0.0553} & 6.76\% & 6.76\% \\

& HR@10  & 0.0286 & 0.0504 & 0.0483 & 0.0553 & \underline{0.0632} & 0.0516 & \textbf{0.0758} & 50.40\% & 19.94\% & 0.0749 & \underline{0.0756} & \textbf{0.0814} & 8.68\% & 7.67\% \\

& HR@20  & 0.0526 & 0.0855 & 0.0816 & 0.0884 & \underline{0.1013} & 0.0870 & \textbf{0.1157} & 35.32\% & 14.22\% & 0.1069 & \underline{0.1092} & \textbf{0.1150} & 7.58\% & 5.31\% \\

& NDCG@5 & 0.0102 & 0.0125 & 0.0133 & 0.0167 & \underline{0.0216} & 0.0158 & \textbf{0.0256} & 104.80\% & 18.52\% & \underline{0.0360} & 0.0345 & \textbf{0.0379} & 5.28\% & 5.28\% \\

& NDCG@10 & 0.0141 & 0.0204 & 0.0206 & 0.0243 & \underline{0.0298} & 0.0228 & \textbf{0.0354} & 73.53\% & 18.79\% & \underline{0.0434} & 0.0424 & \textbf{0.0463} & 6.68\% & 6.68\% \\

& NDCG@20 & 0.0201 & 0.0292 & 0.0290 & 0.0326 & \underline{0.0384} & 0.0317 & \textbf{0.0454} & 55.48\% & 18.23\% & \underline{0.0515} & 0.0508 & \textbf{0.0547} & 6.21\% & 6.21\% \\


\midrule 
\multirow{6}{*}{\textbf{Sports}} 

& HR@5  & 0.0110 & 0.0173 & 0.0158 & 0.0181 & \underline{0.0216} & 0.0174 & \textbf{0.0284} & 52.16\% & 33.96\% & 0.0245 &  \underline{0.0286} & \textbf{0.0304} & 24.08\% & 6.29\% \\

& HR@10  &0.0187 & 0.0307 & 0.0261 & 0.0333 & \underline{0.0382} & 0.0313 & \textbf{0.0468} & 62.44\% & 22.51\% & 0.0373 &  \underline{0.0474} & \textbf{0.0474} & 27.08\% & 9.98\% \\

& HR@20  & 0.0312 & 0.0497 & 0.0383 & 0.0521 & \underline{0.0603} & 0.0518 & \textbf{0.0715} & 43.86\% & 17.41\% & 0.0557 & \underline{0.0660} & \textbf{0.0692} & 24.24\% & 4.85\% \\

& NDCG@5 & 0.0068 & 0.0091 & 0.0094 & 0.0097 & \underline{0.0120} & 0.0096 & \textbf{0.0162} & 78.02\% & 33.88\% & 0.0168 & \underline{0.0184} & \textbf{0.0197} & 17.26\% & 7.07\% \\

& NDCG@10 & 0.0092 & 0.0134 & 0.0121 & 0.0144 & \underline{0.0176} & 0.0135 & \textbf{0.0221} & 64.93\% & 25.57\% & 0.0211 & \underline{0.0235} & \textbf{0.0252} & 19.43\% & 7.23\% \\

& NDCG@20 & 0.0123 & 0.0182 & 0.0164 & 0.0191 & \underline{0.0230} & 0.0187 & \textbf{0.0283} & 55.49\% & 26.91\% & 0.0256 & \underline{0.0271} & \textbf{0.0307} & 19.92\% & 13.28\% \\


\midrule 
\multirow{6}{*}{\textbf{Toys}} 
& HR@5  & 0.0158 & 0.0427 & 0.0378 & 0.0447 & \underline{0.0465} & 0.0457 & \textbf{0.0552} & 29.27\% & 18.71\% & \underline{0.0553} & 0.0552 & \textbf{0.0606} & 9.58\% & 9.58\% \\

& HR@10  & 0.0275 & 0.0664 & 0.0615 & 0.0708 & 0.0757 & \underline{0.077} & \textbf{0.0815} & 22.74\% & 5.84\% & 0.0776 & \underline{0.0814} & \textbf{0.0889} & 14.56\% & 9.21\% \\

& HR@20  & 0.0454 & 0.0989 & 0.0914 & 0.1047 & 0.1084 & \underline{0.1143} & \textbf{0.1189} & 20.22\% & 4.02\% & 0.1072 &  \underline{0.1145} & \textbf{0.1211} & 12.97\% & 5.76\% \\

& NDCG@5 &  0.0095 & 0.0221 & 0.0199 & 0.0231 & 0.0251 & \underline{0.0273} & \textbf{0.0340} & 53.85\% & 24.54\% & \underline{0.0403} & 0.0385 & \textbf{0.0425} & 5.46\% & 5.46\% \\

& NDCG@10 & 0.0132 & 0.0297 & 0.0275 & 0.0316 & 0.0341 & \underline{0.0354} & \textbf{0.0398} & 34.01\% & 12.43\% & 0.0475 & \underline{0.0479} & \textbf{0.0516} & 8.63\% & 7.72\% \\

& NDCG@20 & 0.0177 & 0.0378 & 0.0352 & 0.0401 & 0.0423 & \underline{0.0451} & \textbf{0.0495} & 30.95\% & 9.76\% & 0.0549 & \underline{0.0562} & \textbf{0.0598} & 8.93\% & 6.41\% \\


\midrule 
\multirow{6}{*}{\textbf{Yelp}} 
& HR@5  & 0.0196 & 0.0223 & 0.0237 & 0.0259 & \underline{0.0275} & 0.0252 & \textbf{0.0391} & 75.34\% & 42.18\% & 0.0309 & \underline{0.0316} & \textbf{0.0366} & 18.45\% & 15.82\% \\

& HR@10  & 0.0326 & 0.0390 & 0.0379 & 0.0404 & 0.0417 & \underline{0.0451} & \textbf{0.0626} & 60.51\% & 38.80\% & 0.0478 &  \underline{0.0526} & \textbf{0.0582} & 21.76\% & 10.68\% \\

& HR@20  & 0.0543 & 0.0661 & 0.0604 & 0.0662 & 0.0654 & \underline{0.0730} & \textbf{0.0985} & 49.02\% & 34.93\% & 0.0735 & \underline{0.0851} & \textbf{0.0901} & 22.59\% & 5.88\% \\


& NDCG@5 & 0.0121 & 0.0141 & 0.0154 & 0.0179 & \underline{0.0190} & 0.0159 & \textbf{0.0257} & 82.27\% & 35.26\% & \underline{0.0211} & 0.0199 & \textbf{0.0244} & 15.64\% & 15.64\% \\

& NDCG@10 & 0.0162 & 0.0194 & 0.0201 & 0.0225 & \underline{0.0236} & 0.0223 & \textbf{0.0332} & 71.13\% & 40.68\% & 0.0265 & \underline{0.0274} & \textbf{0.0314} & 18.49\% & 14.60\% \\

& NDCG@20 & 0.0217 & 0.0262 & 0.0258 & 0.0287 & 0.0291 & \underline{0.0294} & \textbf{0.0423} & 61.45\% & 43.88\% & 0.0330 & \underline{0.0352} & \textbf{0.0393} & 19.09\% & 11.65\% \\

\bottomrule
\end{tabular}
\end{adjustbox}
\label{tab:exp1}
\end{table*}
```

## Table 3
```latex
\begin{table}[t]\small
\caption{Comparison of Training Efficiency between E4SRec and One-Loop \myStringL}
\centering
\begin{tabular}{lccc}
\toprule
\textbf{Method} & \textbf{Dataset} &\textbf{Training Time (s)} & \textbf{Hit@10}\\
\midrule
\midrule
\multirow{2}{*}{E4SRec} & Beauty & 1.3×10$^4$ & 0.0749 \\
                       & Toys    & 1.1×10$^4$ & 0.0766 \\
\cmidrule(lr){1-4}
\multirow{2}{*}{\myStringC{}} & Beauty & 9.0×10$^3$ & 0.0776 \\
                              & Toys   & 7.4×10$^3$ & 0.0831 \\
\bottomrule
\end{tabular}
\label{tab:comparison}
\end{table}
```

