# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\centering
\caption{Performance of top leaderboard models on MTEB(Eng, v2).
% \mjb{Update with new ranking when gecko models are on leaderboard}
}
\label{tab:leaderboard_eng}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lccc|ccccccc}
\toprule

& & \multirow{2}{*}{\parbox{1cm}{\centering{\textbf{Mean}\\\textbf{(Task)}}}} & \multirow{2}{*}{\parbox{1cm}{\centering \textbf{Mean}\\\textbf{(Type)}}} & & &
\multirow{2}{*}{\parbox{1.2cm}{\centering Pair.\\Class.}} & & & &
\\

Model Name & \textbf{Rank} & & & {Class.} & {Clus.} & & {Rerank.} & {Retrieval} & {STS} & {Summ.}\\
\midrule
        {Gemini Embedding} & \textbf 1 & \textcolor{blue}{\textbf{73.3}} & \textcolor{blue}{\textbf{67.7}} & 90.1 & 59.4 & 87.7 & 48.6 & \textcolor{blue}{\textbf{64.4}} & \textcolor{blue}{\textbf{85.3}} & \textcolor{blue}{\textbf{38.3}} \\
        \midrule
        Linq-Embed-Mistral & 2 & 69.8 & 65.3 & 83.0 & 54.1 & 88.4 & 49.4 & 60.1 & 84.7 & 37.3 \\
        jasper\_en\_vision\_language\_v1 & 3 & 71.4 & 66.7 & \textbf{90.3} & \textbf{60.5} & 88.1 & 50.0 & 56.1 & 84.4 & 37.2 \\
        SFR-Embedding-Mistral & 4 & 69.3 & 64.9 & 80.5 & 54.9 & 88.6 & 50.2 & 59.3 & 84.8 & 36.3 \\
        NV-Embed-v2 & 5 & 69.8 & 65.0 & 87.2 & 47.7 & \textbf{88.7} & 49.6 & 62.8 & 83.8 & 35.2 \\
        text-embedding-005 (Gecko) & 6 & 69.6 & 64.8 & 86.0 & 51.9 & 87.6 & 48.8 & 58.8 & 85.2 & 35.1 \\
        text-embedding-004 (Gecko) & 7 & 69.5 & 64.8 & 86.0 & 51.5 & 87.7 & 48.5 & 59.1 & 84.8 & 36.1\\
        gte-Qwen2-7B-instruct & 8 & 70.7 & 65.8 & 88.5 & 59.0 & 85.9 & \textbf{50.5} & 58.1 & 82.7 & 35.7 \\
        e5-mistral-7b-instruct & 9 & 68.0 & 64.0 & 79.9 & 51.4 & 88.4 & 49.8 & 57.6 & 84.3 & 36.6 \\
        stella\_en\_400M\_v5 & 10 & 69.4 & 64.8 & 88.3 & 57.7 & 87.2 & 49.6 & 52.7 & 83.9 & 34.5 \\
        stella\_en\_1.5B\_v5 & 11 & 69.4 & 65.3 & 89.4 & 57.1 & 88.0 & 50.2 & 52.4 & 83.3 & 36.9 \\
        gte-Qwen2-1.5B-instruct & 12 & 67.2 & 63.3 & 85.8 & 53.5 & 87.5 & 49.3 & 50.3 & 82.5 & 33.9 \\
\bottomrule
\end{tabular}
}\vspace{-0.5em}
\end{table}
```

## Table 2
```latex
\begin{table}[t]
\centering
\caption{Performance of top leaderboard models on MTEB(Code).
} 
\label{tab:leaderboard_code}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lccc|cccccccc}
\toprule

& & \multirow{2}{*}{\parbox{1cm}{\centering{\textbf{Mean}\\\textbf{All}}}} & \multirow{2}{*}{\parbox{1cm}{\centering{\textbf{Mean}\\\textbf{\mbox{-COIR}}}}} & & & & & & & & 
\\

Model Name & \textbf{Rank} & & & {AppsR.} & {COIR} & {CESR} & {CSNCCR} & {CSNR} & {CTOC} & {CTODL} & {CQA} \\
\midrule
        {Gemini Embedding} & \textbf 1 & \textcolor{blue}{\textbf{75.5}} & \textcolor{blue}{\textbf{74.7}} & \textcolor{blue}{\textbf{93.8}}	& 81.1 & \textcolor{blue}{\textbf{81.6}} & 84.7 & 91.3 & 89.5 & 31.5 & 50.2 \\
\midrule
        inf-retriever-v1-1.5b & 2 & 62.9 & 60.6 & 38.9 & 78.6 & 67.2 & 75.5 & 90.9 & 85.0 & 33.8 & 33.1 \\
        text-embedding-005 (Gecko) & 3 & 63.3 & 65.4 & 91.3 & 48.4 & 54.4 & 55.7 & 87.2 & 82.8 & 34.4 & \textbf{52.2} \\
        voyage-code-3 & 4 & - & - & 93.6 & \textbf{89.4} & - & \textbf{90.1} & \textbf{94.0} & \textbf{95.0} & \textbf{38.6} & 34.5 \\
        NV-Embed-v2 & 5 & - & 59.4 & 29.1 & -  & 74.0 & 68.8 & 86.6 & 89.1 & 33.4 & 34.8 \\
        voyage-3 & 6 & - & 67.3 & 73.0 & - & 75.6 & 77.9 & 92.3 & 89.9 & 33.9 & 28.7 \\
        GritLM-7B & 7 & - & 62.4 & 35.1 & -  & 74.6 & 86.7 & 86.7 & 89.2 & 33.0 & 31.2 \\
        KaLM-emb.-mling.-mini-v1 & 8 & - & 57.4 & 46.8 & -  & 60.0 & 59.5 & 88.0 & 79.9 & 34.0 & 33.6 \\
        text-embedding-3-large & 9 & - & 59.0 & 28.4 & - & 71.1 & 73.2 & 90.5 & 84.3 & 34.2 & 31.0 \\
        NV-Embed-v1 & 10 & - & 57.7 & 30.3 & - & 70.8 & 65.1 & 85.8 & 85.1 & 33.1 & 33.4 \\
        SFR-Embedding-Mistral & 11 & - & 56.7 & 26.1 & - & 68.8 & 64.5 & 86.7 & 83.5 & 32.9 & 34.3 \\
        Linq-Embed-Mistral & 12 & - & 57.5 & 30.2 & - & 70.6 & 64.5 & 87.1 & 84.9 & 32.8 & 32.6 \\
\bottomrule
\end{tabular}
}
\end{table}
```

## Table 3
```latex
\begin{table}[t]
\centering
\caption{Performance of top multilingual models on XTREME-UP (MRR@10).}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{ll|c*{20}{c}}
\toprule
 
 & Average & as & bho & brx & gbm & gom & gu & hi & hne & kn & mai & ml & mni & mr & mwr & or & pa & ps & sa & ta & ur\\
\midrule
{{Gemini Embedding}} & \textcolor{blue}{\textbf{64.3}} & \textcolor{blue}{\textbf{69.2}} & \textcolor{blue}{\textbf{66.4}} & \textcolor{blue}{\textbf{25.7}} & \textcolor{blue}{\textbf{64.9}} & \textcolor{blue}{\textbf{65.5}} & \textcolor{blue}{\textbf{70.3}} & \textcolor{blue}{\textbf{69.1}} & \textcolor{blue}{\textbf{68.3}} & \textcolor{blue}{\textbf{69.5}} & \textcolor{blue}{\textbf{68.4}} & \textcolor{blue}{\textbf{70.8}} & \textcolor{blue}{\textbf{44.4}} & \textcolor{blue}{\textbf{68.8}} & \textcolor{blue}{\textbf{66.5}} & \textcolor{blue}{\textbf{65.8}} & \textcolor{blue}{\textbf{69.5}} & \textcolor{blue}{\textbf{61.9}} & \textcolor{blue}{\textbf{68.1}} & \textcolor{blue}{\textbf{68.6}} & \textcolor{blue}{\textbf{64.8}} \\
{{Gecko i18n Embedding}} & 35.0 & 31.9 & 39.7 & 3.8 & 37.4 & 26.0 & 42.9 & 46.3 & 42.0 & 41.6 & 44.1 & 45.5 & 9.4 & 41.5 & 40.7 & 19.4 & 40.9 & 33.0 & 35.9 & 40.5 & 37.0 \\
\midrule
voyage-3-large & 39.2 & 34.3 & 44.8 & 7.9 & 46.6 & 27.1 & 46.7 & 54.3 & 45.3 & 41.5 & 48.3 & 45.3 & 19.2 & 45.5 & 47.9 & 32.3 & 48.4 & 26.8 & 40.0 & 36.0 & 45.6 \\
Linq-Embed-Mistral & 24.6 & 23.8 & 38.1 & 8.6 & 37.0 & 21.7 & 11.6 & 44.2 & 39.7 & 21.7 & 38.5 & 10.2 & 14.7 & 31.4 & 36.2 & 10.7 & 8.3 & 13.8 & 37.7 & 14.3 & 29.3 \\
multiling.-e5-large-instr. & 18.7 & 21.2 & 21.9 & 1.5 & 19.3 & 8.7 & 13.9 & 30.6 & 22.6 & 24.2 & 24.0 & 8.6 & 6.3 & 23.0 & 19.8 & 17.3 & 24.5 & 15.9 & 19.1 & 22.9 & 28.2 \\
gte-Qwen2-7B-instruct & 17.4 & 14.7 & 22.7 & 5.4 & 23.0 & 7.0 & 19.1 & 30.4 & 19.1 & 16.2 & 25.9 & 21.7 & 7.2 & 23.8 & 24.0 & 11.3 & 19.2 & 11.0 & 21.1 & 9.7 & 15.5 \\
text-embedding-3-large & 18.8 & 18.2 & 28.8 & 3.3 & 28.4 & 11.1 & 14.6 & 40.4 & 29.3 & 17.1 & 31.1 & 15.6 & 2.9 & 25.5 & 28.7 & 8.3 & 11.3 & 6.8 & 26.6 & 6.0 & 22.0 \\
\bottomrule
\end{tabular}
}
\label{tab:xtreme_up_results}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
\centering
\caption{Results using different training mixtures for MTEBs (task mean), XTREME-UP (MRR@10), and XOR-Retrieve (Recall@5kt). Using a Gemini foundation, the English Only mixture is able to achieve good performance on MTEB(Multilingual), MTEB(Eng, v2) and XOR-Retrieve. Multilingual fine-tuning helps the most on the long-tail languages in XTREME-UP. Ablations exclude model souping.
}
\label{tab:main_ablation}
\resizebox{1.00\columnwidth}{!}{%
\begin{tabular}{lcccccc}
\toprule
& {MTEB(Multilingual)} & {MTEB(Eng, v2)} & {MTEB(Code)} & {XOR-Retrieve} & {XTREME-UP} \\
\midrule
Gemini Embedding & \textcolor{blue}{\textbf{68.32}} & \textcolor{blue}{\textbf{73.28}} & \textcolor{blue}{\textbf{74.66}} & \textcolor{blue}{\textbf{90.42}} & 64.33 \\
\midrule
\textit{Pre-Finetuning} \\
\midrule
Pre-finetuning Only & \textbf{48.89} & \textbf{50.99} & \textbf{46.18} & 76.64 & 21.22 \\
No Training & 30.55	& 28.17 & 9.86 & - & - \\
\midrule
\textit{Fine-tuning Mixtures} \\
\midrule
English Only (Diverse Task) & \textbf{66.75} & \textbf{72.77} & 58.68 & 85.70 & 49.34 \\
Multilingual Only (Retrieval) & 58.24 & 61.88 & 58.75 & \textbf{89.00} & \textbf{65.06} \\
Code Only (Retrieval) & 60.20 & 62.25 & \textbf{72.08} & 82.16 & 34.74 \\
\bottomrule
\end{tabular}
}
\end{table}
```

## Table 5
```latex
\begin{table}[ht]
\centering
\caption{Full results of Gemini Embedding on XOR-Retrieve (left) and XTREME-UP (right).}
\resizebox{0.25\columnwidth}{!}{%
\begin{tabular}{lc}
\toprule
Language & Performance \\
\midrule
ar & 91.26 \\
bn & 94.08 \\
fi & 89.17 \\
ja & 86.31 \\
ko & 89.82 \\
ru & 88.61 \\
te & 93.70 \\
\bottomrule
\end{tabular}}
\quad\quad\quad
\centering
\resizebox{0.2\columnwidth}{!}{%
\begin{tabular}{lc}
\toprule
Language & Performance \\
\midrule
as & 69.25 \\
bho & 66.38 \\
brx & 25.66 \\
gbm & 64.87 \\
gom & 65.54 \\
gu & 70.26 \\
hi & 69.06 \\
hne & 68.33 \\
kn & 69.54 \\
mai & 68.39 \\
ml & 70.82 \\
mni & 44.44 \\
mr & 68.77 \\
mwr & 66.49 \\
or & 65.77 \\
pa & 69.55 \\
ps & 61.90 \\
sa & 68.09 \\
ta & 68.57 \\
ur & 64.85 \\
\bottomrule
\end{tabular}
}
\end{table}
```

## Table 6
```latex
\begin{table}[t]
\centering
\caption{Results on MTEB classification using synthetic datasets. Self-training on Gemini generated training data dramatically improves model performance, \textbf{+17.6}. Ablation models exclude souping. {\small \mbox{$^*$ Gecko} training mixtures include training sets provided by several classification tasks from Huggingface.}}
\label{tab:synthetic_data}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{ll|cccc}
\toprule
& \textbf{Average} & {AmazonCounterfactual} & {AmazonPolarity} & {AmazonReviews} & {Emotion} \\
\midrule
\textbf{w/o Synthetic} & 57.57 & 65.43 & 67.29 & 48.84 & 48.70 \\
\textbf{w/ Synthetic} & \textbf{75.17} (+17.6) & \textbf{91.30} & \textbf{96.51} & \textbf{57.00} & \textbf{55.90} \\
\midrule
{Gecko Embedding} & 66.78 & 66.52 & \textbf{97.28}$^*$ & 51.24 & 52.09 \\
{Gemini Embedding} & \textcolor{blue}{\textbf{76.09}} & \textcolor{blue}{\textbf{92.70}} & 96.10 & \textcolor{blue}{\textbf{59.30}} & \textcolor{blue}{\textbf{56.27}} \\
\bottomrule
\end{tabular}
}
\end{table}
```

## Table 7
```latex
\begin{table}[t]
\centering
\caption{Comparison of embedding models on Massive Multilingual Embedding Benchmark: MTEB(Multilingual), MTEB(Eng, v2), and MTEB(Code). We also show results on XOR-Retrieve and XTREME-UP.
For MTEBs, we report task and type mean performances.
We report MRR@10 for XTREME-UP and Recall@5kt for XOR-Retrieve.
$^*$: Averaged over seven code tasks available for all models. $^\dagger$: For Gecko Embedding~\citep{lee2024gecko}, we evaluate text-embedding-004 on MTEB(Eng, v2), text-embedding-005 on MTEB(Code), and text-multilingual-embedding-002 on others.
}
\label{tab:main_table}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{llll|llll}
\toprule
 & & {Gemini} & {Gecko} & {gte-Qwen2-} & {multilingual-e5-} & {Cohere-embed-} & {text-embedding-} \\
 & & {Embedding} & {Embedding$^\dagger$} & {7B-instruct} & {large-instruct} & {multilingual-v3.0} & {3-large} \\
\midrule
\multirow{2}{3.5cm}{\textbf{MTEB(Multilingual)} \footnotesize{\citep{enevoldsen2025mmteb}}} & Mean (Task) & \textcolor{blue}{\textbf{68.32}} & 62.13 & 62.51 & 63.23 & 61.10 & 58.92 \\
& Mean (Type) & \textcolor{blue}{\textbf{59.64}} & 54.32 & 56.00 & 55.17 & 53.31 & 51.48 \\
\cmidrule{2-8}
& - Bitext Mining & 79.32 & 70.73 & 73.92 & \textbf{80.13} & 70.50 & 62.17 \\
& - Classification & \textcolor{blue}{\textbf{71.84}} & 64.64 & 61.55 & 64.94 & 62.95 & 60.27 \\
& - Clustering & \textcolor{blue}{\textbf{54.99}} & 48.47 & 53.36 & 51.54 & 47.61 & 47.49 \\
& - Inst. Retrieval & \textcolor{blue}{\textbf{5.18}} & 4.08 & 4.94 & -0.40 & -1.89 & -2.68 \\
& - Multilabel Class. & \textcolor{blue}{\textbf{29.16}} & 22.80 & 25.48 & 22.91 & 22.74 & 22.03 \\
& - Pair Class. & 83.64 & 81.14 & \textbf{85.13} & 80.86 & 79.88 & 79.17 \\
& - Reranking & \textcolor{blue}{\textbf{65.72}} & 61.22 & 65.55 & 62.61 & 64.07 & 63.89 \\
& - Retrieval & \textcolor{blue}{\textbf{67.71}} & 59.68 & 60.08 & 57.12 & 59.16 & 59.27 \\
& - STS & \textcolor{blue}{\textbf{79.40}} & 76.11 & 73.98 & 76.81 & 74.80 & 71.68 \\
\midrule
\multirow{2}{3.5cm}{\textbf{MTEB(Eng, v2)} \footnotesize{\citep{enevoldsen2025mmteb}}} & Mean (Task) & \textcolor{blue}{\textbf{73.30}} & 69.53 & 70.72 & 65.53 & 66.01 & 66.43 \\
& Mean (Type) & \textcolor{blue}{\textbf{67.67}} & 64.82 & 65.77 & 61.21 & 61.43 & 62.15 \\
\midrule
\multirow{2}{3.5cm}{\textbf{MTEB(Code)}$^*$ \footnotesize{\citep{enevoldsen2025mmteb}}} & & \multirow{2}{*}{\textcolor{blue}{\textbf{74.66}}} & \multirow{2}{*}{65.40} & \multirow{2}{*}{56.41} & \multirow{2}{*}{57.94} & \multirow{2}{*}{51.94} & \multirow{2}{*}{58.95} \\
& & & \\
\midrule
\multirow{2}{3cm}{\textbf{XOR-Retrieve} \footnotesize{\citep{asai2021xor}}} & & \multirow{2}{*}{\textcolor{blue}{\textbf{90.42}}} & \multirow{2}{*}{65.67} & \multirow{2}{*}{N/A} & \multirow{2}{*}{N/A} & \multirow{2}{*}{N/A} & \multirow{2}{*}{68.76} \\
& & & \\
\midrule
\multirow{2}{3cm}{\textbf{XTREME-UP} \footnotesize{\citep{ruder2023xtreme}}} & & \multirow{2}{*}{\textcolor{blue}{\textbf{64.33}}} & \multirow{2}{*}{34.97} & \multirow{2}{*}{17.39} & \multirow{2}{*}{18.68} & \multirow{2}{*}{N/A} & \multirow{2}{*}{18.80} \\
& & & \\
\midrule
\textbf{Commercial Use} & & \Checkmark & \Checkmark & & & \Checkmark & \Checkmark \\
\bottomrule
\end{tabular}
}
\end{table}
```

## Table 8
```latex
\begin{table}[ht]
\centering
\caption{Full results of Gemini Embedding on MTEB(Multilingual).}
\resizebox{0.3365\columnwidth}{!}{%
\begin{tabular}{lc}
\toprule
Task Name & Performance \\
\midrule
AILAStatutes & 48.77 \\
AfriSentiClassification & 53.56 \\
AlloProfClusteringS2S.v2 & 56.36 \\
AlloprofReranking & 81.77 \\
AmazonCounterfactualClassification & 88.20 \\
ArXivHierarchicalClusteringP2P & 64.92 \\
ArXivHierarchicalClusteringS2S & 63.84 \\
ArguAna & 86.44 \\
ArmenianParaphrasePC & 96.89 \\
BUCC.v2 & 98.99 \\
BelebeleRetrieval & 90.73 \\
BibleNLPBitextMining & 20.72 \\
BigPatentClustering.v2 & 38.06 \\
BiorxivClusteringP2P.v2 & 53.86 \\
BornholmBitextMining & 51.69 \\
BrazilianToxicTweetsClassification & 28.02 \\
BulgarianStoreReviewSentimentClassfication & 78.13 \\
CEDRClassification & 57.42 \\
CLSClusteringP2P.v2 & 42.68 \\
CSFDSKMovieReviewSentimentClassification & 49.38 \\
CTKFactsNLI & 87.59 \\
CataloniaTweetClassification & 54.51 \\
Core17InstructionRetrieval & 7.69 \\
CovidRetrieval & 79.13 \\
CyrillicTurkicLangClassification & 95.30 \\
CzechProductReviewSentimentClassification & 68.16 \\
DBpediaClassification & 94.76 \\
DalajClassification & 50.47 \\
DiaBlaBitextMining & 87.23 \\
EstonianValenceClassification & 53.52 \\
FaroeseSTS & 86.12 \\
FilipinoShopeeReviewsClassification & 48.45 \\
FinParaSTS & 28.60 \\
FinancialPhrasebankClassification & 88.64 \\
FloresBitextMining & 83.71 \\
GermanSTSBenchmark & 88.09 \\
GreekLegalCodeClassification & 43.76 \\
GujaratiNewsClassification & 92.05 \\
HALClusteringS2S.v2 & 32.00 \\
HagridRetrieval & 99.31 \\
IN22GenBitextMining & 93.75 \\
IndicCrosslingualSTS & 62.87 \\
IndicGenBenchFloresBitextMining & 96.77 \\
IndicLangClassification & 87.69 \\
IndonesianIdClickbaitClassification & 67.00 \\
IsiZuluNewsClassification & 40.53 \\
ItaCaseholdClassification & 73.30 \\
JSICK & 84.99 \\
KorHateSpeechMLClassification & 17.69 \\
KorSarcasmClassification & 60.51 \\
KurdishSentimentClassification & 86.39 \\
LEMBPasskeyRetrieval & 38.50 \\
LegalBenchCorporateLobbying & 95.98 \\
MIRACLRetrievalHardNegatives & 70.42 \\
MLQARetrieval & 84.16 \\
MacedonianTweetSentimentClassification & 71.83 \\
MalteseNewsClassification & 37.38 \\
MasakhaNEWSClassification & 83.55 \\
MasakhaNEWSClusteringS2S & 57.45 \\
MassiveIntentClassification & 81.92 \\
MedrxivClusteringP2P.v2 & 47.16 \\
MultiEURLEXMultilabelClassification & 5.28 \\
MultiHateClassification & 72.47 \\
NTREXBitextMining & 93.64 \\
NepaliNewsClassification & 98.14 \\
News21InstructionRetrieval & 10.26 \\
\bottomrule
\end{tabular}}
\centering
\resizebox{0.33\columnwidth}{!}{%
\begin{tabular}{lc}
\toprule
Task Name & Performance \\
\midrule
NollySentiBitextMining & 68.71 \\
NordicLangClassification & 85.97 \\
NorwegianCourtsBitextMining & 93.42 \\
NusaParagraphEmotionClassification & 56.38 \\
NusaTranslationBitextMining & 77.52 \\
NusaX-senti & 80.31 \\
NusaXBitextMining & 82.52 \\
OdiaNewsClassification & 91.84 \\
OpusparcusPC & 96.62 \\
PAC & 71.68 \\
PawsXPairClassification & 59.99 \\
PlscClusteringP2P.v2 & 74.31 \\
PoemSentimentClassification & 59.66 \\
PolEmo2.0-OUT & 77.53 \\
PpcPC & 95.50 \\
PunjabiNewsClassification & 82.61 \\
RTE3 & 89.55 \\
Robust04InstructionRetrieval & -2.41 \\
RomaniBibleClustering & 43.22 \\
RuBQReranking & 73.84 \\
SCIDOCS & 25.15 \\
SIB200ClusteringS2S & 41.74 \\
SICK-R & 82.75 \\
SNLHierarchicalClusteringP2P & 61.41 \\
STS12 & 81.55 \\
STS13 & 89.89 \\
STS14 & 85.41 \\
STS15 & 90.44 \\
STS17 & 88.58 \\
STS22.v2 & 71.69 \\
STSB & 85.50 \\
STSBenchmark & 89.08 \\
STSES & 81.75 \\
ScalaClassification & 51.85 \\
SemRel24STS & 73.14 \\
SentimentAnalysisHindi & 76.06 \\
SinhalaNewsClassification & 82.29 \\
SiswatiNewsClassification & 62.38 \\
SlovakMovieReviewSentimentClassification & 90.35 \\
SpartQA & 10.30 \\
SprintDuplicateQuestions & 96.90 \\
StackExchangeClustering.v2 & 92.07 \\
StackOverflowQA & 96.71 \\
StatcanDialogueDatasetRetrieRetrieval & 51.11 \\
SwahiliNewsClassification & 66.05 \\
SwednClusteringP2P & 45.84 \\
SwissJudgementClassification & 57.86 \\
T2Reranking & 67.95 \\
TERRa & 63.92 \\
TRECCOVID & 86.32 \\
Tatoeba & 81.97 \\
TempReasonL1 & 2.96 \\
ToxicConversationsClassification & 88.75 \\
TswanaNewsClassification & 53.37 \\
TweetTopicSingleClassification & 71.11 \\
TwitterHjerneRetrieval & 98.02 \\
TwitterURLCorpus & 87.05 \\
VoyageMMarcoReranking & 66.73 \\
WebLINXCandidatesReranking & 10.97 \\
WikiCitiesClustering & 91.63 \\
WikiClusteringP2P.v2 & 28.23 \\
WikipediaRerankingMultilingual & 92.24 \\
WikipediaRetrievalMultilingual & 94.20 \\
WinoGrande & 60.52 \\
XNLI & 85.26 \\
indonli & 60.69 \\
\bottomrule
\end{tabular}
}
\end{table}
```

## Table 9
```latex
\begin{table}[ht]
\centering
\caption{Full results of Gemini Embedding on MTEB(Eng, v2) (left) and MTEB(Code) (right).}
\resizebox{0.3365\columnwidth}{!}{%
\begin{tabular}{lc}
\toprule
Task Name & Performance \\
\midrule
AmazonCounterfactualClassification & 92.69 \\
ArXivHierarchicalClusteringP2P & 64.92 \\
ArXivHierarchicalClusteringS2S & 63.84 \\
ArguAna & 86.44 \\
AskUbuntuDupQuestions & 64.24 \\
BIOSSES & 88.97 \\
Banking77Classification & 94.27 \\
BiorxivClusteringP2P.v2 & 53.86 \\
CQADupstackGamingRetrieval & 70.68 \\
CQADupstackUnixRetrieval & 53.69 \\
ClimateFEVERHardNegatives & 31.06 \\
FEVERHardNegatives & 88.98 \\
FiQA2018 & 61.78 \\
HotpotQAHardNegatives & 87.01 \\
ImdbClassification & 94.98 \\
MTOPDomainClassification & 99.27 \\
MassiveIntentClassification & 88.46 \\
MassiveScenarioClassification & 92.08 \\
MedrxivClusteringP2P.v2 & 47.16 \\
MedrxivClusteringS2S.v2 & 45.01 \\
MindSmallReranking & 32.95 \\
SCIDOCS & 24.04 \\
SICK-R & 82.75 \\
STS12 & 81.55 \\
STS13 & 89.89 \\
STS14 & 85.41 \\
STS15 & 90.44 \\
STS17 & 91.61 \\
STS22.v2 & 68.37 \\
STSBenchmark & 89.08 \\
SprintDuplicateQuestions & 96.90 \\
StackExchangeClustering.v2 & 92.07 \\
StackExchangeClusteringP2P.v2 & 50.91 \\
SummEvalSummarization.v2 & 38.28 \\
TRECCOVID & 86.32 \\
Touche2020Retrieval.v3 & 52.39 \\
ToxicConversationsClassification & 88.75 \\
TweetSentimentExtractionClassification & 69.88 \\
TwentyNewsgroupsClustering.v2 & 57.37 \\
TwitterSemEval2015 & 79.17 \\
TwitterURLCorpus & 87.05 \\
\bottomrule
\end{tabular}}
\quad
\centering
\resizebox{0.33\columnwidth}{!}{%
\begin{tabular}{lc}
\toprule
Task Name & Performance \\
\midrule
AppsRetrieval & 93.75 \\
COIRCodeSearchNetRetrieval & 81.06 \\
CodeEditSearchRetrieval & 81.61 \\
CodeFeedbackMT & 56.28 \\
CodeFeedbackST & 85.33 \\
CodeSearchNetCCRetrieval & 84.69 \\
CodeSearchNetRetrieval & 91.33 \\
CodeTransOceanContest & 89.53 \\
CodeTransOceanDL & 31.47 \\
CosQA & 50.24 \\
StackOverflowQA & 95.92 \\
SyntheticText2SQL & 69.96 \\
\bottomrule
\end{tabular}
}
\end{table}
```

## Table 10
```latex
\begin{table}[t]
\centering
\caption{Results on filtering the MIRACL datasets. We show that proper filtering of retrieval datasets using LLMs can greatly improve the performance.}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{ll|c*{17}{c}}
\toprule
 & \textbf{Average} & ar & bn & de & en & es & fa & fi & fr & hi & id & ja & ko & ru & sw & te & th & yo & zh \\
\midrule
\textbf{w/o Filtering} & 59.8 & \textbf{74.8} & 71.5 & 46.5 & 54.6 & 44.5 & 51.3 & 66.8 & 46.0 & \textbf{59.4} & 34.9 & 56.9 & 55.1 & 62.6 & 69.7 & 73.6 & 71.9 & \textbf{85.0} & 51.7 \\
\textbf{w/ Filtering} & \textbf{63.7} (+3.9) & 74.2 & \textbf{74.7} & \textbf{52.9} & \textbf{54.7} & \textbf{47.3} & \textbf{55.5} & \textbf{74.7} & \textbf{49.5} & 59.3 & \textbf{47.1} & \textbf{61.9} & \textbf{63.3} & \textbf{64.8} & \textbf{76.0} & \textbf{75.0} & \textbf{75.0} & 83.3 & \textbf{57.0} \\
\midrule
{{Gecko Embedding}} & 56.2 & 64.3 & 66.7 & 49.1 & 45.3 & 48.5 & 49.2 & 65.2 & 45.1 & 55.0 & 44.7 & 52.6 & 57.5 & 55.1 & 67.4 & 74.5 & 66.5 & 54.0 & 50.7 \\
{{Gemini Embedding}} & \textcolor{blue}{\textbf{70.1}} & \textcolor{blue}{\textbf{78.3}} & \textcolor{blue}{\textbf{79.0}} & \textcolor{blue}{\textbf{59.8}} & \textcolor{blue}{\textbf{58.7}} & \textcolor{blue}{\textbf{57.0}} & \textcolor{blue}{\textbf{60.9}} & \textcolor{blue}{\textbf{78.0}} & \textcolor{blue}{\textbf{55.6}} & \textcolor{blue}{\textbf{65.4}} & \textcolor{blue}{\textbf{54.3}} & \textcolor{blue}{\textbf{75.1}} & \textcolor{blue}{\textbf{68.9}} & \textcolor{blue}{\textbf{73.4}} & \textcolor{blue}{\textbf{81.0}} & \textcolor{blue}{\textbf{80.5}} & \textcolor{blue}{\textbf{80.8}} & \textcolor{blue}{\textbf{88.8}} & \textcolor{blue}{\textbf{65.7}} \\
\bottomrule
\end{tabular}
}
\label{tab:miracl_results}
\end{table}
```

## Table 11
```latex
\begin{table}[t]
\centering
\caption{Performance of top leaderboard models on MTEB(Multilingual).}
\label{tab:leaderboard_multilingual}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lccc|ccccccccc}
\toprule
& & \multirow{2}{*}{\parbox{1cm}{\centering{\textbf{Mean}\\\textbf{(Task)}}}} & \multirow{2}{*}{\parbox{1cm}{\centering \textbf{Mean}\\\textbf{(Type)}}} & \multirow{2}{*}{\parbox{1.2cm}{\centering Bitext\\Mining}} & & & \multirow{2}{*}{\parbox{1.2cm}{\centering Inst.\\Retrieval}} & \multirow{2}{*}{\parbox{1.2cm}{\centering Multi.\\Class.}} & \multirow{2}{*}{\parbox{1.2cm}{\centering Pair.\\Class.}} \\
Model Name & \textbf{Rank} &  &  & & {Class.} & {Clus.} & & & & {Rerank.} & {Retrieval} & {STS} \\
\midrule
{Gemini Embedding} & \textbf{1} & \textcolor{blue}{\textbf{68.3}} & \textcolor{blue}{\textbf{59.6}} & 79.3 & \textcolor{blue}{\textbf{71.8}} & \textcolor{blue}{\textbf{55.0}} & \textcolor{blue}{\textbf{5.2}} & \textcolor{blue}{\textbf{29.2}} & 83.6 & \textcolor{blue}{\textbf{65.6}} & \textcolor{blue}{\textbf{67.7}} & \textcolor{blue}{\textbf{79.4}} \\
\midrule

Linq-Embed-Mistral & 2 & 61.5 & 54.2 & 70.3 & 62.2 & 51.3 & 0.9 & 24.8 & 80.4 & 64.4 & 58.7 & 74.9 \\
gte-Qwen2-7B-instruct & 3 & 62.5 & 56.0 & 73.9 & 61.6 & 53.4 & 4.9 & 25.5 & \textbf{85.1} & 65.6 & 60.1 & 74.0 \\
multilingual-e5-large-instruct & 4 & 63.2 & 55.2 & \textbf{80.1} & 64.9 & 51.5 & -0.4 & 22.9 & 80.9 & 62.6 & 57.1 & 76.8 \\
SFR-Embedding-Mistral & 5 & 60.9 & 54.0 & 70.0 & 60.0 & 52.6 & 0.2 & 24.6 & 80.3 & 64.2 & 59.4 & 74.8 \\
GritLM-7B & 6 & 60.9 & 53.8 & 70.5 & 61.8 & 50.5 & 3.5 & 22.8 & 79.9 & 63.8 & 58.3 & 73.3 \\
text-multilingual-embedding-002 & 7 & 62.1 & 54.3 & 70.7 & 64.6 & 48.5 & 4.1 & 22.8 & 81.1 & 61.2 & 59.7 & 76.1 \\
GritLM-8x7B & 8 & 60.5 & 53.4 & 68.2 & 61.6 & 50.9 & 2.4 & 24.4 & 79.7 & 62.6 & 57.5 & 73.2 \\
e5-mistral-7b-instruct & 9 & 60.3 & 53.2 & 70.6 & 60.3 & 51.4 & -0.6 & 22.2 & 81.1 & 63.8 & 55.8 & 74.0 \\
Cohere-embed-multilingual-v3.0 & 10 & 61.1 & 53.3 & 70.5 & 63.0 & 47.6 & -1.9 & 22.7 & 79.9 & 64.1 & 59.2 & 74.8 \\
gte-Qwen2-1.5B-instruct & 11 & 59.5 & 52.8 & 62.5 & 58.3 & 52.6 & 0.7 & 24.0 & 81.6 & 62.6 & 60.8 & 71.6 \\
bilingual-embedding-large & 12 & 60.9 & 53.0 & 73.6 & 62.8 & 47.2 & -3.0 & 22.4 & 79.8 & 61.4 & 55.1 & 77.8 \\
\bottomrule
\end{tabular}
}
\end{table}
```

