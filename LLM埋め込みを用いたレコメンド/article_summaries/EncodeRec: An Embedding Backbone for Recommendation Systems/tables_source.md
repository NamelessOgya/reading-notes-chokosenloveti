# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\centering
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.1}
\begin{tabular}{lcc}
\toprule
\textbf{Model} & \textbf{Recall@10} & \textbf{NDCG@10} \\
\midrule
BERT-Base & 0.09 & 0.07 \\
BLaIR-Large & 0.12 & 0.09 \\
all-MiniLM-L6-v2 & 0.57 & 0.44 \\
EmbeddingGemma & 0.83 & 0.72 \\
\bottomrule
\end{tabular}
\caption{Retrieval results for item descriptions retrieved from titles on 50K items in the Amazon \textit{Beauty} dataset.}
\label{tab:beauty_retrieval}
\end{table}
```

## Table 2
```latex
\begin{table}[t]
% \centering
% \setlength{\tabcolsep}{4pt}
% \renewcommand{\arraystretch}{1.1}
% \begin{tabular}{lcc}
% \toprule
% \textbf{Model} & \textbf{Recall@10} & \textbf{NDCG@10} \\
% \midrule
% BERT-Base & 0.09 & 0.07 \\
% BLaIR-Large & 0.12 & 0.09 \\
% all-MiniLM-L6-v2 & 0.57 & 0.44 \\
% EmbeddingGemma & 0.83 & 0.72 \\
% \bottomrule
% \end{tabular}
% \caption{Retrieval performance for item descriptions retrieved from titles on 50K items in the Amazon \textit{Beauty and Healthcare} dataset.}
% \label{tab:beauty_retrieval}
% \end{table}
```

## Table 3
```latex
\begin{table}[t]
\centering
\renewcommand{\arraystretch}{1.6}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lcccccc}
\toprule
\multirow{2}{*}{\textbf{UniSRec Model}} &
\multicolumn{2}{c}{\textbf{Video Games}} &
\multicolumn{2}{c}{\textbf{Beauty}} &
\multicolumn{2}{c}{\textbf{Baby Products}} \\
\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
 & Recall@10 & NDCG@10 & Recall@10 & NDCG@10 & Recall@10 & NDCG@10 \\
\midrule
BERT  & 0.0214 & 0.0116 & 0.0157 & 0.0098 & 0.0122 & 0.0063 \\
Blair-Base  & \underline{0.0241} & 0.0128 & 0.0245 & 0.0123 & 0.0146 & 0.0131 \\
Blair-Large & 0.0247 & \underline{0.0134} & 0.0239 & 0.0119 & \underline{0.0148} & \underline{0.0075} \\
MiniLM-L6-v2         & 0.0231 & 0.0123 & 0.0218 & 0.0130 & 0.0130 & 0.0066 \\
EncodeRec-22M & 0.0232 & 0.0126 & \underline{0.0333} & \underline{0.0182} & 0.0141 & 0.0072 \\
EmbeddingGemma        & 0.0244 & 0.0129 & 0.0308 & 0.0165 & 0.0147 & 0.0075 \\
EncodeRec-300M & \textbf{0.0263*} & \textbf{0.0142*} & \textbf{0.0387*} & \textbf{0.0206*} & \textbf{0.0162*} & \textbf{0.0084*} \\
\bottomrule
\end{tabular}
}
\caption{UniSRec results across datasets. Best scores in \textbf{bold}, second best \underline{underlined}. The asterisk (*) indicates statistically significant improvements at $p < 0.05$ over the baselines.}

\label{tab:unsirec}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
\centering
\renewcommand{\arraystretch}{1.6}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lcccccc}
\toprule
\multirow{2}{*}{\textbf{TIGER Model}} &
\multicolumn{2}{c}{\textbf{Sports}} &
\multicolumn{2}{c}{\textbf{Beauty}} &
\multicolumn{2}{c}{\textbf{Toys}} \\
\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
 & Recall@10 & NDCG@10 & Recall@10 & NDCG@10 & Recall@10 & NDCG@10 \\
\midrule
Sentence-T5      & 0.0382 & 0.0199 & 0.0601 & 0.0322 & 0.0578 & 0.0295 \\
Blair-Base       & 0.0270 & 0.0149 & 0.0546 & 0.0309 & 0.0583 & 0.0310 \\
Blair-Large      & 0.0312 & 0.0170 & 0.0599 & 0.0316 & 0.0546 & 0.0294 \\
MiniLM-L6-v2              & 0.0370 & 0.0198 & 0.0640 & 0.0350 & 0.0597 & 0.0312 \\
EncodeRec-22M    & \underline{0.0389} & \underline{0.0204} & \underline{0.0689} & \underline{0.0370} & \textbf{0.0663*} & \underline{0.0348} \\
EmbeddingGemma   & 0.0380 & 0.0203 & 0.0656 & 0.0353 & 0.0609 & 0.0331 \\
EncodeRec-300M   & \textbf{0.0395} & \textbf{0.0212} & \textbf{0.0694*} & \textbf{0.0373*} & \underline{0.0627} & \textbf{0.0362} \\
\bottomrule
\end{tabular}
}
\caption{TIGER results across datasets. Best scores in \textbf{bold}, second best \underline{underlined}.The asterisk (*) indicates statistically significant improvements at $p < 0.05$ over the baselines.}
\label{tab:tiger}
\end{table}
```

## Table 5
```latex
\begin{table*}[t]
% \centering
% \setlength{\tabcolsep}{3.2pt}
% \renewcommand{\arraystretch}{1.15}
% \begin{tabular}{llccc *{9}{c}}
% \toprule
% \textbf{Dataset} & \textbf{Metric} &
% \textbf{SASRec} & \textbf{FDSA} & \textbf{S$^3$-Rec} &
% \multicolumn{9}{c}{\textbf{UnisRec}} \\
% \cmidrule(lr){6-14}
% & & & & &
% \textbf{original} & \textbf{blair-B} & \textbf{blair-L} & \textbf{22M} & \textbf{300M} & \textbf{600M} & \textbf{Mini} & \textbf{Base} & \textbf{Large} \\
% \midrule
% \midrule

% \multirow{2}{*}{\textbf{Beauty}}
%   & recall@10 & 0.05109 & 0.04530 & 0.05226 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
%   & ndcg@10   & 0.02179 & 0.02244 & 0.02279 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
% \midrule

% \multirow{2}{*}{\textbf{Sports}}
%   & recall@10 & 0.02696 & 0.02699 & 0.02557 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
%   & ndcg@10   & 0.01160 & 0.01391 & 0.01097 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
% \midrule

% \multirow{2}{*}{\textbf{Toys}}
%   & recall@10 & 0.06314 & 0.04684 & 0.06659 & 0.05782 & 0.05833
%  & 0.05461
%  & 0.05974
%  & -- & 0.06659
%  & 0.06633 & -- & 0.06800
%  \\
%   & ndcg@10   & 0.02756 & 0.02375 & 0.02942 & 0.02949 & 0.03099 & 0.02941 & 0.03122 & -- & 0.03468 & 0.03482 & -- & 0.03644 \\
% \midrule

% \multirow{2}{*}{\textbf{Steam}}
%   & recall@10 & 0.18259 & 0.14773 & 0.18025 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
%   & ndcg@10   & 0.14763 & 0.08236 & 0.14437 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
% \bottomrule
% \end{tabular}
% \end{table*}
```

## Table 6
```latex
\begin{table*}[t]
% \centering
% \setlength{\tabcolsep}{3.2pt}
% \renewcommand{\arraystretch}{1.15}
% \begin{tabular}{llccc *{9}{c}}
% \toprule
% \textbf{Dataset} & \textbf{Metric} &
% \textbf{SASRec} & \textbf{FDSA} & \textbf{S$^3$-Rec} &
% \multicolumn{9}{c}{\textbf{TIGER}} \\
% \cmidrule(lr){6-14}
% & & & & &
% \textbf{original} & \textbf{blair-B} & \textbf{blair-L} & \textbf{22M} & \textbf{300M} & \textbf{600M} & \textbf{Mini} & \textbf{Base} & \textbf{Large} \\
% \midrule
% \midrule

% \multirow{2}{*}{\textbf{Beauty}}
%   & recall@10 & 0.05109 & 0.04530 & 0.05226 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
%   & ndcg@10   & 0.02179 & 0.02244 & 0.02279 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
% \midrule

% \multirow{2}{*}{\textbf{Sports}}
%   & recall@10 & 0.02696 & 0.02699 & 0.02557 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
%   & ndcg@10   & 0.01160 & 0.01391 & 0.01097 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
% \midrule

% \multirow{2}{*}{\textbf{Toys}}
%   & recall@10 & 0.06314 & 0.04684 & 0.06659 & 0.05782 & 0.05833
%  & 0.05461
%  & 0.05974
%  & -- & 0.06659
%  & 0.06633 & -- & 0.06800
%  \\
%   & ndcg@10   & 0.02756 & 0.02375 & 0.02942 & 0.02949 & 0.03099 & 0.02941 & 0.03122 & -- & 0.03468 & 0.03482 & -- & 0.03644 \\
% \midrule

% \multirow{2}{*}{\textbf{Steam}}
%   & recall@10 & 0.18259 & 0.14773 & 0.18025 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
%   & ndcg@10   & 0.14763 & 0.08236 & 0.14437 & -- & -- & -- & -- & -- & -- & -- & -- & -- \\
% \bottomrule
% \end{tabular}
% \end{table*}
```

## Table 7
```latex
\begin{table*}[t]
% \centering
% \setlength{\tabcolsep}{3pt}
% \renewcommand{\arraystretch}{1.15}
% \begin{tabular}{ll *{4}{cc}}
% \toprule
% & & \multicolumn{2}{c}{\textbf{Beauty}} & \multicolumn{2}{c}{\textbf{Sports}} & \multicolumn{2}{c}{\textbf{Toys}} & \multicolumn{2}{c}{\textbf{Steam}} \\
% \cmidrule(lr){3-4}\cmidrule(lr){5-6}\cmidrule(lr){7-8}\cmidrule(lr){9-10}
% \textbf{Family} & \textbf{Variant} & \textbf{recall@10} & \textbf{ndcg@10} & \textbf{recall@10} & \textbf{ndcg@10} & \textbf{recall@10} & \textbf{ndcg@10} & \textbf{recall@10} & \textbf{ndcg@10} \\
% \midrule
% \midrule
% \multicolumn{2}{l}{\textbf{SASRec}}   & 0.05109 & 0.02179 & 0.02696 & 0.01160 & 0.06314 & 0.02756 & 0.18259 & 0.14763 \\
% \multicolumn{2}{l}{\textbf{FDSA}}     & 0.04530 & 0.02244 & 0.02699 & 0.01391 & 0.04684 & 0.02375 & 0.14773 & 0.08236 \\
% \multicolumn{2}{l}{\textbf{S$^3$-Rec}}& 0.05226 & 0.02279 & 0.02557 & 0.01097 & 0.06659 & 0.02942 & 0.18025 & 0.14437 \\
% \midrule
% \multirow{9}{*}{\textbf{TIGER}}
%  & original & -- & -- & -- & -- & 0.05782 & 0.02949 & -- & -- \\
%  & blair-B  & -- & -- & -- & -- & 0.05833 & 0.03099 & -- & -- \\
%  & blair-L  & -- & -- & -- & -- & 0.05461 & 0.02941 & -- & -- \\
%  & 22M      & -- & -- & -- & -- & 0.05974 & 0.03122 & -- & -- \\
%  & 300M     & -- & -- & -- & -- & --      & --      & -- & -- \\
%  & 600M     & -- & -- & -- & -- & 0.06659 & 0.03468 & -- & -- \\
%  & Mini     & -- & -- & -- & -- & 0.06633 & 0.03482 & -- & -- \\
%  & Base     & -- & -- & -- & -- & --      & --      & -- & -- \\
%  & Large    & -- & -- & -- & -- & 0.06800 & 0.03644 & -- & -- \\
% \midrule
% \multirow{9}{*}{\textbf{SASRecText}}
%  & original & -- & -- & 0.0069 & 0.0037 & 0.005 & 0.0026 & -- & -- \\
%  & blair-B  & -- & -- & -- & -- & -- & -- & -- & -- \\
%  & blair-L  & -- & -- & -- & -- & -- & -- & -- & -- \\
%  & 22M      & -- & -- & -- & -- & -- & -- & -- & -- \\
%  & 300M     & -- & -- & -- & -- & 0.0049 & 0.0025 & -- & -- \\
%  & 600M     & -- & -- & -- & -- & -- & -- & -- & -- \\
%  & Mini     & -- & -- & -- & -- & -- & -- & -- & -- \\
%  & Base     & -- & -- & -- & -- & -- & -- & -- & -- \\
%  & Large    & -- & -- & -- & -- & -- & -- & -- & -- \\
% \bottomrule
% \end{tabular}
% \end{table*}
```

