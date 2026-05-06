# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
\setlength{\tabcolsep}{2pt}
\centering
\caption{\small Performance comparison on sequential recommendation. The last row depicts \% improvement with TIGER relative to the best baseline. Bold (underline) are used to denote the best (second-best) metric.}
\begin{adjustbox}{width=\linewidth}
\begin{tabular}{lcccccccccccc}
\toprule
\multirow{2.5}{*}{Methods} & \multicolumn{4}{c}{\textbf{Sports and Outdoors}} & \multicolumn{4}{c}{\textbf{Beauty}} &  \multicolumn{4}{c}{\textbf{Toys and Games}} \\
\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13}
  & \shortstack{Recall\\@5}  & \shortstack{NDCG\\@5} & \shortstack{Recall\\@10}  & \shortstack{NDCG\\@10} & \shortstack{Recall\\@5}  & \shortstack{NDCG\\@5} & \shortstack{Recall\\@10}  & \shortstack{NDCG\\@10} & \shortstack{Recall\\@5}  & \shortstack{NDCG\\@5} & \shortstack{Recall\\@10}  & \shortstack{NDCG\\@10}  \\
\cmidrule{1-13}
P5~\cite{geng2022recommendation}&0.0061&0.0041&0.0095&0.0052&0.0163&0.0107&0.0254&0.0136&0.0070  & 0.0050  & 0.0121 & 0.0066 \\
Caser~\cite{tang2018personalized}   & 0.0116  & 0.0072  & 0.0194 & 0.0097 & 0.0205 & 0.0131 & 0.0347 & 0.0176 & 0.0166 & 0.0107 & 0.0270 & 0.0141 \\
HGN~\cite{ma2019hierarchical} &  0.0189  & 0.0120  & 0.0313  &  0.0159 & 0.0325  & 0.0206  & 0.0512  & 0.0266  & 0.0321  & 0.0221  & 0.0497  & 0.0277  \\
GRU4Rec~\cite{hidasi2015session}   & 0.0129  & 0.0086  & 0.0204  & 0.0110  & 0.0164  & 0.0099  & 0.0283  & 0.0137  & 0.0097  & 0.0059  & 0.0176  & 0.0084 \\
BERT4Rec~\cite{sun2019bert4rec}   & 0.0115   & 0.0075  & 0.0191  &  0.0099 &  0.0203 & 0.0124  & 0.0347  & 0.0170  & 0.0116   & 0.0071  & 0.0203  & 0.0099 \\
FDSA~\cite{zhang2019feature}  &  0.0182  & 0.0122  & 0.0288  & 0.0156  & 0.0267  & 0.0163  & 0.0407  & 0.0208  & 0.0228  & 0.0140  & 0.0381  & 0.0189 \\
SASRec~\cite{kang2018self} &  0.0233  &  0.0154 & 0.0350  &  0.0192 & 0.0387  & \underline{0.0249}  & 0.0605  & 0.0318  &  \underline{0.0463}  &  \underline{0.0306}  &  0.0675  & 0.0374 \\
S$^3$-Rec~\cite{zhou2020s3} & \underline{0.0251}  & \underline{0.0161}  & \underline{0.0385} & \underline{0.0204} & \underline{0.0387} & 0.0244  & \underline{0.0647}  & \underline{0.0327}  & 0.0443  & 0.0294  &  \underline{0.0700} & \underline{0.0376} \\
\midrule
 \textbf{TIGER [Ours]}
& \textbf{0.0264} & \textbf{0.0181} & \textbf{0.0400} & \textbf{0.0225} 
& \textbf{0.0454} & \textbf{0.0321} & \textbf{0.0648} & \textbf{0.0384}
& \textbf{0.0521} & \textbf{0.0371} & \textbf{0.0712} & \textbf{0.0432} \\
 & \green{+5.22\%}  & \green{+12.55\%}  & \green{+3.90\%}  & \green{+10.29\%}  & \green{+17.31\%}  & \green{+29.04\%}  & \green{+0.15\%}  & \green{+17.43\%}  & \green{+12.53\%}  & \green{+21.24\%}  & \green{+1.71\%}  & \green{+14.97\%}  \\
\bottomrule
\end{tabular}
\end{adjustbox}
\label{tab:sequential}
\vspace{-1em}
\end{table}
```

## Table 2
```latex
\begin{table*}[!t]
\centering
\caption{\small Ablation study for different ID generation techniques for generative retrieval. We show that RQ-VAE Semantic ID (SID) perform significantly better compared to hashing SIDs and Random IDs.}
\begin{adjustbox}{width=\linewidth}
\begin{tabular}{lcccccccccccc}
\toprule
\multirow{2.5}{*}{Methods} & \multicolumn{4}{c}{\textbf{Sports and Outdoors}} & \multicolumn{4}{c}{\textbf{Beauty}} &  \multicolumn{4}{c}{\textbf{Toys and Games}} \\
\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13}
 & \shortstack{Recall\\@5}  & \shortstack{NDCG\\@5} & \shortstack{Recall\\@10}  & \shortstack{NDCG\\@10} & \shortstack{Recall\\@5}  & \shortstack{NDCG\\@5} & \shortstack{Recall\\@10}  & \shortstack{NDCG\\@10} & \shortstack{Recall\\@5}  & \shortstack{NDCG\\@5} & \shortstack{Recall\\@10}  & \shortstack{NDCG\\@10}  \\
\cmidrule{1-13}
Random ID          & 0.007  & 0.005  & 0.0116 & 0.0063 & 0.0296 & 0.0205 & 0.0434 & 0.0250 & 0.0362 & 0.0270 & 0.0448 & 0.0298 \\
LSH SID             & 0.0215 & 0.0146 & 0.0321 & 0.0180 & 0.0379 & 0.0259 & 0.0533 & 0.0309 & 0.0412 & 0.0299 & 0.0566 & 0.0349 \\
RQ-VAE SID
& \textbf{0.0264} & \textbf{0.0181} & \textbf{0.0400} & \textbf{0.0225}
& \textbf{0.0454} & \textbf{0.0321} & \textbf{0.0648} & \textbf{0.0384}
& \textbf{0.0521} & \textbf{0.0371} & \textbf{0.0712} & \textbf{0.0432} \\
\bottomrule
\end{tabular}
\end{adjustbox}
\vspace{-0.5em}
\label{tab:ablation}
\end{table*}
```

## Table 3
```latex
\begin{table*}[!h]
\centering
\caption{\small Recommendation diversity with temperature-based decoding.}%
\label{tab:diversity_qual}
\begin{adjustbox}{width=\linewidth}
\begin{tabular}{l|l|l}
\toprule
Target Category & \multicolumn{2}{c}{Most-common Categories for top-10 predicted items}\\
\cmidrule{2-3}
& \multicolumn{1}{c}{T = 1.0} & \multicolumn{1}{c}{T = 2.0} \\
\cmidrule{1-3}
Hair Styling Products & Hair Styling Products & Hair Styling Products, Hair Styling Tools, Skin Face\\
Tools Nail & Tools Nail & Tools Nail, Makeup Nails\\
Makeup Nails & Makeup Nails & Makeup Nails, Skin Hands \& Nails, Tools Nail\\
\shortstack[l]{Skin Eyes} & \shortstack[l]{Skin Eyes} & \shortstack[l]{Hair Relaxers, Skin Face, Hair Styling Products, Skin Eyes}\\
\shortstack[l]{Makeup Face} & \shortstack[l]{Tools Makeup Brushes,Makeup Face} & \shortstack[l]{Tools Makeup Brushes, Makeup Face,Skin Face, Makeup Sets, Hair Styling Tools}\\
\shortstack[l]{Hair Loss Products} & \shortstack[l]{Hair Loss Products,Skin Face, Skin Body} & \shortstack[l]{Skin Face, Hair Loss Products, Hair Shampoos,Hair \& Scalp Treatments, Hair Conditioners}\\
\bottomrule
\end{tabular}
\end{adjustbox}
\label{tab:recommendation_diversity}
\end{table*}
```

## Table 4
```latex
\begin{table}[]
\centering
\caption{Recall and NDCG metrics for different number layers.}\label{tab:ablation_layers}
\begin{tabular}{lllll}
\toprule
Number of Layers & {Recall@5} & {NDCG@5} & {Recall@10} & {NDCG@10} \\ 
\midrule
3                 & 0.04499           & 0.03062         & 0.06699            & 0.03768          \\
4                 & 0.0454            & 0.0321          & 0.0648             & 0.0384           \\
5                 & 0.04633           & 0.03206         & 0.06596            & 0.03834         \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 5
```latex
\begin{table}[]
\centering
\caption{The effect of providing user information to the recommender system}\label{tab:ablation_user_id}
\begin{tabular}{lllll}
\toprule
Recall@5                             & NDCG@5  & Recall@10 & NDCG@10 &        \\
\midrule
No user information                  & 0.04458 & 0.0302    & 0.06479 & 0.0367 \\
With user id (reported in the paper) & 0.0454  & 0.0321    & 0.0648  & 0.0384\\
\bottomrule
\end{tabular}
\end{table}
```

## Table 6
```latex
\begin{table}[ht]
\small
\centering
\caption{The mean and stand error of the metrics for different dataset (computed using 3 runs with different random seeds)}\label{tab:std_err}
\begin{tabular}{lllll}
\toprule
Datasets & Recall@5         & NDCG@5           & Recall@10        & NDCG@10          \\
\midrule
Beauty                & 0.0441 $\pm$ 0.00069 & 0.0309 $\pm$ 0.00062 & 0.0642 $\pm$ 0.00092 & 0.0374 $\pm$ 0.00061 \\
Sports and Outdoors   & 0.0278 $\pm$ 0.00069 & 0.0189 $\pm$ 0.00043 & 0.0419 $\pm$ 0.0010  & 0.0234 $\pm$ 0.00048 \\
Toys and Games        & 0.0518 $\pm$ 0.00064 & 0.0375 $\pm$ 0.00039 & 0.0698 $\pm$ 0.0013  & 0.0433 $\pm$ 0.00047\\
\bottomrule
\end{tabular}
\end{table}
```

## Table 7
```latex
\begin{table}[]
\centering
\caption{Testing scalability by generating the Semantic IDs on the combined dataset vs generating the Semantic IDs on only the Beauty dataset.}
\label{tab:scalability}
\begin{tabular}{lllll}
\toprule
&Recall@5                                                                   & NDCG@5  & Recall@10 & NDCG@10  \\
\midrule
Semantic ID [Combined datasets]                                & 0.04355 & 0.3047    & 0.06314 & 0.03676   \\
Semantic ID [Amazon Beauty]  & 0.0454  & 0.0321    & 0.0648  & 0.0384   \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 8
```latex
\begin{table}[!ht]
\centering
\caption{\small Dataset statistics for the three real-world benchmarks.}
\label{table:dataset_summary}
\begin{adjustbox}{width=0.6\linewidth}
\begin{tabular}{lcccc}
\toprule
Dataset & \# Users &  \# Items & \multicolumn{2}{c}{Sequence Length}\\
\midrule
& & & Mean & Median \\
\arrayrulecolor{gray}\cmidrule(r){4-5}
Beauty & 22,363 & 12,101 & 8.87 & 6 \\
Sports and Outdoors & 35,598 & 18,357 & 8.32 & 6\\
Toys and Games & 19,412 & 11,924 & 8.63 & 6 \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}
```

## Table 9
```latex
\begin{table*}[ht!]
\centering
\caption{Results for P5\cite{geng2022recommendation} with the standard pre-processing.}
\label{tab:p5_table}
\begin{adjustbox}{width=\linewidth}
\begin{tabular}{clcccccccccccc}
\toprule
&\multirow{2.5}{*}{Methods} & \multicolumn{4}{c}{\textbf{Sports and Outdoors}} & \multicolumn{4}{c}{\textbf{Beauty}} &  \multicolumn{4}{c}{\textbf{Toys and Games}} \\
\cmidrule(lr){3-6}\cmidrule(lr){7-10}\cmidrule(lr){11-14}
 & & Recall@5  & NDCG@5 & Recall@10  & NDCG@10 & Recall@5  & NDCG@5 & Recall@10  & NDCG@10 & Recall@5  & NDCG@5 & Recall@10  & NDCG@10  \\
\cmidrule{2-14}
&P5 &0.0061&0.0041&0.0095&0.0052&0.0163&0.0107&0.0254&0.0136&0.0070  & 0.0050  & 0.0121 & 0.0066 \\
& P5-ours & 0.0107 & 0.0076 & 0.01458 & 0.0088 & 0.035 & 0.025 & 0.048 & 0.0298 & 0.018 & 0.013 & 0.0235 & 0.015 \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table*}
```

