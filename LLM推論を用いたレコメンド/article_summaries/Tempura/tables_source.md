# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[!htp]
\centering
\caption{Performance comparison on ML-1M and Games datasets. We highlight the best performance in \textbf{bold}. N$@K$ denotes NDCG@$K$.}
\begin{tabular}{@{}ccccccccc@{}}
\toprule
\multirow{2}{*}{Method} & \multicolumn{4}{c}{ML-1M}     & \multicolumn{4}{c}{Games}     \\ \cmidrule(l){2-9} 
                        & N@1   & N@5   & N@10  & N@20  & N@1   & N@5   & N@10  & N@20  \\ \midrule
BM25                    & 4.00  & 13.14 & 20.53 & 33.70  & 16.50  & 30.09 & 37.19 &  46.11 \\
UniSRec                 & 9.00  & 20.08 & 26.72 & 38.24 & 19.50 & 34.86 &  40.82  & 49.15 \\
VQ-Rec                  & 9.50  & 19.52 & 27.11 & 38.72 & 5.50  & 16.76 & 25.27 & 36.42 \\ \midrule
Sequential              & 21.43	& 42.57	& 48.59	& 53.28 & 24.12	& 47.26 & 53.03 & 56.56 \\
RF                      & 26.56	& 45.99	& 51.27	& 55.98 & 25.63 & 50.02 & 53.72 & 57.84 \\
ICL                     & 26.40 & 47.51 & 53.32 & 57.23 & 26.00 &	49.68 &	53.63 & 57.38 \\ \midrule
Cluster                & 27.00  &  45.82 & 52.04 & 56.21 & 26.15 & 47.41 & 52.39 & 57.19  \\
FCL                     & 29.16 & 48.35 & 54.11 & 58.44 & 29.00 &  51.56  & 55.11 & 59.17  \\
Ours (Concat.)                    & \textbf{31.50} & \textbf{49.68} & \textbf{54.96} &  \textbf{59.16} &  19.00  & 45.20  & 50.01  & 53.96   \\ 
Ours (Ensemble)                   &  30.50 &  48.35 & 54.28 & 58.56 &   \textbf{35.50} & \textbf{53.89} & \textbf{58.74} & \textbf{62.35} \\ \bottomrule
\end{tabular}
\end{table*}
```

## Table 2
```latex
\begin{table*}[!htp]
\centering
\caption{Performance comparison on ML-1M and Amazon Review datasets. We highlight the best performance in \textbf{bold}. N$@K$ denotes NDCG@$K$. }
\vspace{-8pt}
\label{tab:main}
\scalebox{1.0}{
\begin{tabular}{@{}ccccccccccccc@{}}
\toprule
\multirow{2}{*}{Method} & \multicolumn{3}{c}{ML-1M}     & \multicolumn{3}{c}{Games}  & \multicolumn{3}{c}{Kindle}    \\ \cmidrule(l){2-10} 
                        & N@1   & N@5   & N@10   & N@1   & N@5   & N@10 & N@1   & N@5   & N@10 \\ \midrule
BM25                    & 4.00  & 13.14 & 20.53   & 16.50  & 30.09 & 37.19 & 6.50  & 18.07 & 24.96  \\
UniSRec                 & 9.00  & 20.08 & 26.72  & 19.50 & 34.86 &  40.82 &  5.00  &  16.21 & 25.03  \\
VQ-Rec                  & 9.50  & 19.52 & 27.11  & 5.50  & 16.76 & 25.27 & 4.30 & 14.22 & 23.58 &  \\ \midrule
Sequential              & 21.43	& 42.57	& 48.59	 & 24.12 & 47.26 & 53.03 & 10.20 & 27.96 & 33.72  \\
RF                      & 26.56	& 45.99	& 51.27	 & 25.63 & 50.02 & 53.72 &  11.11 & 28.77 & 35.71  \\
ICL                     & 26.40 & 47.51 & 53.32  & 26.00 &	49.68 &	53.63 &  13.07 & 30.82 & 36.41 \\ \midrule
Cluster                & 27.00  &  45.82 & 52.04 & 26.15 & 47.41 & 52.39  & 13.20 &   25.77 & 34.07  \\
PCL                     & 29.16 & 48.44 & 54.21 & 29.00 &  51.56  & 55.11 &  11.55 & 29.45 & 36.46 \\
GCL & 30.50 & 48.53 & 53.26 & 32.00 & 51.61 & 56.63 & 10.00 & 31.45 &	36.67 \\ 
PCL + Cluster                   &  30.50 &  48.35 & \textbf{54.88} &  35.50 & 53.89 & 58.74 & 12.00 & 30.15 & \textbf{38.23}  \\ 
\model{}                   &  \textbf{31.50}  &  \textbf{48.64} & 54.49 &  \textbf{39.00} & \textbf{56.51} & \textbf{60.95} & \textbf{14.00} & \textbf{32.17} & 37.59  \\ \bottomrule
\end{tabular}
}
\vspace{-4mm}
\end{table*}
```

## Table 3
```latex
\begin{table}[]
\caption{Performance of \model{} with randomized items, clusters and correctly ordered inputs. }
\label{exp:random}
\centering
\scalebox{0.9}{
\begin{tabular}{@{}cccc@{}}
\toprule
                           & Item-R & Cluster-R & Correct \\ \midrule
ML-1M & 51.78 &  52.47   &   54.49          \\ \midrule
Games & 51.83 & 54.18    &    60.95      \\ \midrule 
Kindle & 34.13  &  33.92    & 37.59      \\ \bottomrule
\end{tabular}
}
\vspace{-5mm}
\end{table}
```

## Table 4
```latex
\begin{table*}[!h]
\centering
\caption{Case study of structure analysis in the historical interaction sequence.}
\vspace{-8pt}
\label{tab:case_dis}
\begin{tabular}{@{}l@{}}
\toprule\toprule
\textcolor{red}{Cluster 1:} [Mad Max - PlayStation 4, Metal Gear Solid V: The Phantom Pain - PlayStation 4]. \\
\textcolor{blue}{Cluster summary:} Action games on PlayStation 4. \\ 
\textcolor{red}{Cluster 2:} [Star Wars: Battlefront - Standard Edition - PlayStation 4, Fallout 4 - PlayStation 4, \\ Just Cause 3 - PlayStation 4, Far Cry Primal - PlayStation 4 Standard Edition]. \\
\textcolor{blue}{Cluster summary:} Open-world action games on PlayStation 4. \\
\textcolor{red}{Cluster 3:} [Tom Clancy\'s The Division - PlayStation 4, Uncharted 4: A Thief\'s End - PlayStation 4, \\Homefront: The Revolution - PlayStation 4, Deus Ex: Mankind Divided - PlayStation 4]. \\
\textcolor{blue}{Cluster summary:} Action games with a focus on story and/or multiplayer on PlayStation 4. \\
\textcolor{red}{Cluster 4:} [Rise of the Tomb Raider: 20 Year Celebration - PlayStation 4, Dishonored 2 - PlayStation 4, \\ Resident Evil 7: Biohazard - PS4 Digital Code, Horizon Zero Dawn - PlayStation 4, Tom Clancy’s \\ Ghost Recon Wildlands - PlayStation 4]. \\
\textcolor{blue}{Cluster summary:} Single-player action shooting games with a focus on exploration and/or stealth on PS4. \\ \midrule
\textbf{Target item:} Prey - Pre-load - PS4 Digital Code \textcolor{orange}{First-person action-adventure shooting game}  \\
\bottomrule \bottomrule
\end{tabular}
\vspace{-3mm}
\end{table*}
```

## Table 5
```latex
\begin{table}[]
\centering
\caption{Performance with GPT-4 (NDCG@10). \model{} can further improve the performance when the backbone LLM is more powerful. }
\vspace{-1mm}
\label{tab:gpt4}
\begin{tabular}{@{}cccc@{}}
\toprule
Method     & ML-1M & Games & Kindle \\ \midrule
Sequential & 55.75 & 66.43 & 57.65  \\ \midrule
ICL   &    54.82    &  67.84   &   54.72                \\ \midrule
  \model{}         & 58.39 & 68.13 & 58.59  \\ \bottomrule
\end{tabular}
\vspace{-5mm}
\end{table}
```

