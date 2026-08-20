# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t!]
\small
\centering
\begin{tabular}{llll@{\hspace{4ex}}r}
\bhline
\tabH Source & Anchor & Positive & Negative & Dataset size\\
\bhline
\tabH Wikipedia (1) & title + section title & 1-paragraph & random 1-paragraph & 19,361,464\\
Wikipedia (3) & title + section title & 3-paragraphs & random 3-paragraphs & 10,010,462\\
Wikipedia (long)  & title / abst. & abst. / article body & random abst. / article body & 7,889,486\\
Wiktionary & title & article body & random article body & 697,405\\
WikiBooks  & title + section title & 1-paragraph & random 1-paragraph & 314,207\\
\hline
\tabH MQA & title & article body & BM25 mined article body& 25,165,824\\
\hline
\tabH CC News (long)  & title & article body & BM25 mined article body& 6,248,336\\
CC News (short) & random sentence & sentence in the same article & sentence in other articles & 2,795,632\\
\hline
\tabH AutoWikiQA (MX)  & question & passage & BM25 mined passage& 11,563,562\\
AutoWikiQA (Nemo)  & question & passage & BM25 mined passage & 495,062\\
\hline
\tabH JRC & title + section title & section body & BM25 mined section body & 131,072\\
\hline
\tabH Wiki Atomic Edits & sentence & edited sentence & random sentence & 3,679,939\\
AutoWikiNLI   & premise & hypothesis (entailment) & hypothesis (contradiction) & 203,147\\
JSNLI  & premise & hypothesis (entailment) & hypothesis (contradiction) & 180,146\\
\hline
\tabH Total & & &  &  88,735,744\\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Datasets used for contrastive pre-training
}
\label{tab:contrastive-pretraining-datasets}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t!]
\small
\centering
\begin{tabular}{lccccc}
\bhline
\tabH Model & \#Params.  & GPUs & Base LM  \\
\bhline
\tabH \RuriPTSmall ~(\hf{cl-nagoya/ruri-pt-small}) & \ \ 68M & A6000$\times$4 & \hf{line-corporation/line-distilbert-base-japanese} \\
\RuriPTBase ~(\hf{cl-nagoya/ruri-pt-base}) & 111M & A100$\times$4 & \hf{tohoku-nlp/bert-base-japanese-v3} \\
\RuriPTLarge ~(\hf{cl-nagoya/ruri-pt-large}) & 337M & A100$\times$4 & \hf{tohoku-nlp/bert-large-japanese-v2} \\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Overview of the model with contrastive pre-training.
}
\label{tab:model-summary-pt}
\end{table*}
```

## Table 3
```latex
\begin{table}[t]
\small
\centering
\begin{tabular}{lc}
\bhline
\tabH Source & Dataset size\\
\bhline
\tabH JSQuAD & 212,352\\
AutoWikiQA (Nemo) & 190,743\\
JaQuAD & 108,068\\
Quiz No Mori & \ \ 36,120\\
Quiz Works & \ \ 29,112\\
JQaRA & \ \ 16,260\\
MIRACL & \ \ 13,968\\
Mr. TyDi & \ \ \ \ 7,394\\
MKQA & \ \ \ \ 6,636\\
\hline
\tabH Total & 620,653\\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Datasets used for training the reranker in the first stage.
}
\label{tab:reranker-stage1-datasets}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
\small
\centering
\begin{tabular}{lc}
\bhline
\tabH Source & Dataset size\\
\bhline
\tabH Quiz No Mori & 18,060\\
Quiz Works & 14,556\\
JQaRA & \ \ 8,130\\
MIRACL & \ \ 6,984\\
MR. TyDi & \ \ 3,697\\
\hline
\tabH Total & 51,427 \\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Datasets used for training the reranker in the second stage.
}
\label{tab:reranker-stage2-datasets}
\end{table}
```

## Table 5
```latex
\begin{table*}[t]
\small
\centering
\begin{tabular}{lcccc}
\bhline
\tabH Model & \#Param. (w/o Emb.) & JQaRA & JaCWIR & MIRACL\\
\bhline
\tabH \hf{hotchpotch/japanese-reranker-cross-encoder-xsmall-v1} & 107M \ \ \ (11M) & 61.4 & 93.8 & 90.6 \\
\hf{hotchpotch/japanese-reranker-cross-encoder-small-v1} & 118M \ \ \ (21M) & 62.5 & 93.9 & 92.2 \\
\hf{hotchpotch/japanese-reranker-cross-encoder-base-v1} & 111M \ \ \ (86M) & 67.1 & 93.4 & 93.3 \\
\hf{hotchpotch/japanese-reranker-cross-encoder-large-v1} & 337M \ (303M) & 71.0 & 93.6 & 91.5 \\
\hline
\tabH \hf{hotchpotch/japanese-bge-reranker-v2-m3-v1} & 568M \ (303M) & 69.2 & 93.7 & 94.7 \\
\hf{BAAI/bge-reranker-v2-m3} & 568M \ (303M) & 67.3 & 93.4 & 94.9 \\
\hline
\tabH \RuriRerankerSmall ~(\hf{cl-nagoya/ruri-reranker-small}) & \ \ 68M \ \ \ (43M)\  & 64.5 & 92.6 & 92.3 \\
\RuriRerankerBase ~(\hf{cl-nagoya/ruri-reranker-base}) & 111M \ \ \ (86M) & 74.3 & 93.5 & 95.6 \\
\RuriRerankerLarge ~(\hf{cl-nagoya/ruri-reranker-large}) & 337M \ (303M) & \textbf{77.1} & \textbf{94.1} & \textbf{96.1} \\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Performance comparison of rerankers.
JQaRA is evaluated using nDCG@10, JaCWIR with MAP@10, and MIRACL with Recall@30. ``\#Param. (w/o Emb.)'' indicates the number of parameters, both with and without token embeddings.
}
\label{tab:reranker-result}
\end{table*}
```

## Table 6
```latex
\begin{table}[t]
\small
\tabcolsep 4pt
\centering
\begin{tabular}{lcccc}
\bhline
\tabH Model & Stage & JQaRA & JaCWIR & MIRACL\\
\bhline
\tabH \RuriPTSmall & 1 only & 63.9 & 92.5 & 91.2 \\
\RuriPTSmall & 2 only & 60.3 & 89.9 & 89.3 \\
\RuriPTSmall & 1 $\rightarrow$ 2 & \textbf{64.5} & \textbf{92.6} & \textbf{92.3} \\
\hline
\tabH \RuriPTBase & 1 only & 72.9 & 92.4 & 94.2 \\
\RuriPTBase & 2 only & 68.0 & 92.9 & 93.7 \\
\RuriPTBase & 1 $\rightarrow$ 2 & \textbf{74.3} & \textbf{93.5} & \textbf{95.6} \\
\hline
\tabH \RuriPTLarge & 1 only & 75.8 & 93.4 & 95.4 \\
\RuriPTLarge & 2 only & 70.5 & 90.8 & 93.2 \\
\RuriPTLarge & 1 $\rightarrow$ 2 & \textbf{77.1} & \textbf{94.1} & \textbf{96.1} \\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
The results of the ablation study for two-stage training.
The evaluation metrics are the same as those in Table~\ref{tab:reranker-result}.
}
\label{tab:reranker-ablation-stage}
\end{table}
```

## Table 7
```latex
\begin{table}[t]
\small
\centering
\tabcolsep 4pt
\begin{tabular}{lcccc}
\bhline
\tabH Model & Phase & JQaRA & JaCWIR & MIRACL\\
\bhline
\tabH $\text{BERT}_\text{small}$ & stage1 & 63.7 & 89.4 & 90.4 \\
$\text{BERT}_\text{small}$ & stage2 & 64.3 & 91.4 & 91.6 \\
\RuriPTSmall & stage1 & 63.9 & 92.5 & 91.2 \\
\RuriPTSmall & stage2 & \textbf{64.5} & \textbf{92.6} & \textbf{92.3} \\
\hline
\tabH $\text{BERT}_\text{base}$ & stage1 & 71.8 & 89.3 & 93.9 \\
$\text{BERT}_\text{base}$ & stage2 & 73.1 & 91.6 & 95.1 \\
\RuriPTBase & stage1 & 72.9  & 92.4 & 94.2 \\
\RuriPTBase & stage2 & \textbf{74.3} & \textbf{93.5} & \textbf{95.6 }\\
\hline
\tabH $\text{BERT}_\text{large}$ & stage1 & 76.1 & 92.2 & 95.2 \\
$\text{BERT}_\text{large}$ & stage2 & \textbf{77.3} & 93.5 & 96.0 \\
\RuriPTLarge & stage1 & 75.8 & 93.4 & 95.4 \\
\RuriPTLarge & stage2 & 77.1 & \textbf{94.1} & \textbf{96.1} \\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
The results of the ablation study for the benefit of contrastive pre-training.
The evaluation metrics are the same as those in Table~\ref{tab:reranker-result}.
}
\label{tab:reranker-ablation-pt}
\end{table}
```

## Table 8
```latex
\begin{table}[t]
\small
\centering
\begin{tabular}{lcc}
\bhline
\tabH Source & Distill. & Dataset size\\
\bhline
\tabH Quiz No Mori & \checkmark & \ \ 31,232\\
Quiz Works & \checkmark & \ \ 26,624\\
JQaRA & \checkmark & \ \ 13,824\\
MIRACL & \checkmark & \ \ 12,800\\
Mr. TyDi & \checkmark & \ \ \ \ 7,168\\
\hline
\tabH NU-SNLI & & 109,568\\
NU-MNLI & & \ \ 77,824\\
JaNLI & & \ \ 13,824\\
\hline
\tabH Total & & 292,864\\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Datasets used for supervised fine-tuning.
}
\label{tab:fine-tuning-datasets}
\end{table}
```

## Table 9
```latex
\begin{table*}[t!]
\small
\centering
\begin{tabular}{lccccccc}
\bhline
\tabH Model & \#Params. & Dim. & \#Layer & Pooling & Context Len. & Vocab Size & JMTEB Avg. \\
\bhline
\tabH \RuriSmall ~(\hf{cl-nagoya/ruri-small}) & \ \ 68M & \ \ 768 & \ \ 6 & Mean & 512 & 32,768 & 71.53 \\
\RuriBase ~(\hf{cl-nagoya/ruri-base}) & 111M & \ \ 768 & 12 & Mean & 512 & 32,768 & 71.91 \\
\RuriLarge ~(\hf{cl-nagoya/ruri-large}) & 337M & 1024 & 24 &Mean & 512 & 32,768 & 73.31 \\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Overview of the model with supervised fine-tuning.
}
\label{tab:model-summary-ft}
\end{table*}
```

## Table 10
```latex
\begin{table*}[t!]
\small
% \tabcolsep 4pt
\centering
\begin{tabular}{@{\ \ }lcccccccc@{\ \ }}
\bhline
\tabH Model & \#Param. & Retrieval & STS & Class. & Reranking & Clustering & Pair. & Avg. \\
\bhline
\tabH \hf{cl-nagoya/sup-simcse-ja-base} & 111M & 49.64 & 82.05 & 73.47 & 91.83 & 51.79 & 62.57 & 63.36\\
\hf{cl-nagoya/sup-simcse-ja-large} & 337M & 37.62 & 83.18 & 73.73 & 91.48 & 50.56 & 62.51 & 58.88\\
\hf{cl-nagoya/unsup-simcse-ja-base} & 111M & 40.23 & 78.72 & 73.07 & 91.16 & 44.77 & 62.44 & 58.39\\
\hf{cl-nagoya/unsup-simcse-ja-large} & 337M & 40.53 & 80.56 & 74.66 & 90.95 & 48.41 & 62.49 & 59.58\\
\hf{pkshatech/GLuCoSE-base-ja} & 133M & 59.02 & 78.71 & 76.82 & 91.90 & 49.78 & 66.39 & 67.29\\
\hline
\tabH \hf{sentence-transformers/LaBSE} & 472M & 40.12 & 76.56 & 72.66 & 91.63 & 44.88 & 62.33 & 58.01\\
\hf{intfloat/multilingual-e5-small} & 118M & 67.27 & 80.07 & 67.62 & 93.03 & 46.91 & 62.19 & 67.71\\
\hf{intfloat/multilingual-e5-base} & 278M & 68.21 & 79.84 & 69.30 & 92.85 & 48.26 & 62.26 & 68.61 \\
\hf{intfloat/multilingual-e5-large} & 560M & 70.98 & 79.70 & 72.89 & 92.96 & 51.24 & 62.15 & 70.90\\
\hline
\tabH OpenAI/text-embedding-ada-002 & - & 64.38 & 79.02 & 69.75 & 93.04 & 48.30 & 62.40 & 67.21 \\
OpenAI/text-embedding-3-small & - & 66.39 & 79.46 & 73.06 & 92.92 & 51.06 & 62.27 & 69.18 \\
OpenAI/text-embedding-3-large & - & 74.48 & 82.52 & 77.58 & 93.58 & 53.32 & 62.35 & 74.05 \\
\hline
\tabH \RuriSmall ~(\hf{cl-nagoya/ruri-small}) & \ \ 68M & 69.41 & 82.79 & 76.22 & 93.00 & 51.19 & 62.11 & 71.53\\
\RuriBase ~(\hf{cl-nagoya/ruri-base}) & 111M & 69.82 & 82.87 & 75.58 & 92.91 & 54.16 & 62.38 & 71.91\\
\RuriLarge ~(\hf{cl-nagoya/ruri-large}) & 337M & 73.02 & 83.13 & 77.43 & 92.99 & 51.82 & 62.29 & 73.31\\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Evaluation results on JMTEB. 
``\#Param.'' indicates the number of model parameters, 
``Retrieval'' shows the average performance on 6 retrieval datasets, 
``STS'' on 2 Semantic Textual Similarity datasets, 
``Classification'' on 4 classification datasets, 
``Reranking'' on 1 reranking dataset, 
``Clustering'' on 2 clustering datasets, 
``Pair.'' on 1 pair classification dataset, 
and ``Avg.'' is the micro average across all 16 datasets.
}
\label{tab:main-result}
\end{table*}
```

## Table 11
```latex
\begin{table*}[t!]
\small
\tabcolsep 4.5pt
\centering
\begin{tabular}{lccccccc}
\bhline
\tabH \multirow{2}{*}{Model} & \multirow{2}{*}{JaGovFAQs} & \multirow{2}{*}{JAQKET} & \multirow{2}{*}{Mr. TyDi} & \multicolumn{3}{c}{NLP Journal} & \multirow{2}{*}{Avg.} \\
 &  &  &  & Abst.--Intro. & Title--Abst. & Title--Intro. &  \\
\bhline
\tabH \hf{pkshatech/GLuCoSE-base-ja} & 63.88 & 39.82 & 30.28 & 78.26 & 82.06 & 59.82 & 59.02\\
\hline
\tabH \hf{intfloat/multilingual-e5-small} & 64.11 & 49.97 & 36.05 & 85.21 & 95.26 & 72.99 & 67.27\\
\hf{intfloat/multilingual-e5-base} & 65.34 & 50.67 & 38.38 & 87.10 & 94.73 & 73.05 & 68.21 \\
\hf{intfloat/multilingual-e5-large} & 70.30 & 58.78 & \textbf{43.63} & 86.00 & 94.70 & 72.48 & 70.98 \\
\hline
\tabH OpenAI/text-embedding-ada-002 & 61.02 & 42.56 & 14.51 & 94.99 & 91.23 & 81.98 & 64.38\\
OpenAI/text-embedding-3-small & 64.02 & 33.94 & 20.03 & 98.47 & 91.70 & 90.17 & 66.39\\
OpenAI/text-embedding-3-large & 72.41 & 48.21 & 34.88 & \textbf{99.33} & \textbf{96.55} & \textbf{95.47} & 74.48\\
\hline
\tabH \RuriSmall ~(\hf{cl-nagoya/ruri-small}) & 73.65 & 48.44 & 33.43 & 87.69 & 97.17 & 76.09 & 69.41\\
\RuriBase ~(\hf{cl-nagoya/ruri-base}) & 74.56 & 50.12 & 35.45 & 86.89 & \textbf{96.57} & 75.31 & 69.82\\
\RuriLarge ~(\hf{cl-nagoya/ruri-large}) & \textbf{76.68} & \textbf{61.74} & 38.03 & 87.12 & \textbf{96.58} & 77.97 & 73.02\\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Evaluation results on the retrieval tasks.
We used nDCG@10 as an evaluation metric for all tasks.
}
\label{tab:retrieval-result}
\end{table*}
```

## Table 12
```latex
\begin{table*}[t!]
\small
\centering
% \tabcolsep 4pt
\begin{tabular}{lccccccc}
\bhline
\tabH Model & Retrieval & STS & Class. & Reranking & Clustering & Pair. & Avg. \\
\bhline
\tabH \RuriPTLarge & \textbf{71.48} & 82.06 & 76.12 & \textbf{92.75} & \textbf{53.41} & 62.27 & \textbf{72.46}\\
% \tabH \RuriPTLarge & \textbf{71.48} & 82.06 & 76.12 & \textbf{92.75} & \textbf{53.41} & 62.27 & \textbf{73.02}\\
\RuriPTLarge ~w/o retrieval & 68.08 & \textbf{82.32} & \textbf{76.42} & 92.66 & 51.98 & 62.29 & 71.11\\
% \RuriPTLarge ~w/o retrieval & 68.08 & \textbf{82.32} & \textbf{76.42} & 92.66 & 51.98 & 62.29 & 72.29\\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Performance of pre-trained models on JMTEB with and without using synthesized retrieval datasets.
}
\label{tab:ablation-synthesized-dataset}
\end{table*}
```

## Table 13
```latex
\begin{table*}[t!]
\small
\centering
% \tabcolsep 4pt
\begin{tabular}{lccccccc}
\bhline
\tabH Model & Retrieval & STS & Class. & Reranking & Clustering & Pair. & Avg. \\
\bhline
\tabH \RuriPTSmall & 67.39 & 81.41 & 75.41 & 92.98 & 51.13 & 62.44 & 70.41\\
\RuriSmall ~w/o pre-training & 56.62 & 82.45 & 77.30 & 92.01 & 47.77 & 62.42 & 66.49\\
\RuriSmall & 69.41 & 82.79 & 76.22 & 93.00 & 51.19 & 62.11 & \textbf{71.53}\\
\hline
\tabH \RuriPTBase & 68.18 & 81.81 & 74.56 & 92.82 & 53.35 & 62.33 & 70.80\\
\RuriBase ~w/o pre-training & 52.99 & 81.95 & 76.19 & 91.60 & 51.85 & 62.20 & 65.25\\
\RuriBase & 69.82 & 82.87 & 75.58 & 92.91 & 54.16 & 62.38 & \textbf{71.91}\\
\hline
\tabH \RuriPTLarge & 71.48 & 82.06 & 76.12 & 92.75 & 53.41 & 62.27 & 72.46\\
\RuriLarge ~w/o pre-training & 57.84 & 83.66 & 76.50 & 91.51 & 49.56 & 62.35 & 67.09\\
\RuriLarge & 73.02 & 83.13 & 77.43 & 92.99 & 51.82 & 62.29 & \textbf{73.31}\\
\bhline
\end{tabular}
\vspace{-1ex}
\caption{
Evaluation results of the model with and without contrastive pre-training.
``w/o pre-training'' represents the performance of the model that underwent only supervised fine-tuning without contrastive pre-training.
}
\label{tab:ablation-pre-training}
\end{table*}
```

## Table 14
```latex
\begin{table*}[t]
\small
\centering
\begin{tabular}{l@{\hspace{6ex}}ccc@{\hspace{8ex}}ccc}
\bhline
\tabH Phase & \multicolumn{3}{c}{Pre-training} & \multicolumn{3}{c}{Fine-tuning} \\
Model & \RuriPTSmall & \RuriPTBase  & \RuriPTLarge & \RuriSmall & \RuriBase & \RuriLarge \\
\bhline
\tabH learning rate & 1$\times10^{-4}$ & 5$\times10^{-5}$ & 3$\times10^{-5}$ & 1$\times10^{-5}$ & 5$\times10^{-6}$ & 3$\times10^{-6}$  \\
max length & 256 & 256 & 192 & 512 & 512 & 512 \\
warmup ratio & 10\% & 10\% & 10\% & 10\% & 10\% & 10\% \\
batch size & 8192 & 8192 & 8192 & 512 & 512& 512 \\
epochs & 1 & 1 & 1 & 1 & 1 & 1 \\
$\tau$ & 0.01 & 0.01 & 0.01 & 0.01 & 0.01 & 0.01 \\
weight decay & 0.01 & 0.01 & 0.01 & 0.01 & 0.01 & 0.01 \\
hard negatives & 1 & 1 & 1 & 15 & 15 & 15 \\
task-homogeneous & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
shuffle positive & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
knowledge distillation &  & &  & \checkmark & \checkmark & \checkmark \\
\bhline
\end{tabular}
\caption{
Hyperparameters for contrastive pre-training and supervised fine-tuning.
}
\label{tab:hyperparameters-emb}
\end{table*}
```

## Table 15
```latex
\begin{table*}[t]
\small
\centering
\begin{tabular}{l@{\hspace{6ex}}ccc@{\hspace{8ex}}ccc}
\bhline
\tabH Phase & \multicolumn{3}{c}{Stage1} & \multicolumn{3}{c}{Stage2} \\
% Model & \RuriRerankerBase & \RuriRerankerLarge & \RuriRerankerBase & \RuriRerankerLarge \\
Model & Small & Base & Large & Small & Base & Large \\
\bhline
\tabH learning rate & 1$\times10^{-4}$ & 5$\times10^{-5}$ & 3$\times10^{-5}$ & 1$\times10^{-5}$ & 5$\times10^{-6}$ & 3$\times10^{-6}$  \\
max length & 256 & 256 & 256 & 512 & 512 & 512 \\
warmup ratio & 10\% & 10\% & 10\% & 10\% & 10\% & 10\% \\
batch size & 512 & 512 & 512 & 64 & 64 & 64\\
epochs & 1 & 1 & 1 & 1 & 1 & 1 \\
weight decay & 0.01 & 0.01 & 0.01 & 0.01 & 0.01 & 0.01 \\
hard negatives & 63 & 63 & 63 & 63 & 63 & 63 \\
task-homogeneous  &  &  &  &  &  &  \\
shuffle positive & \checkmark & \checkmark & \checkmark & & & \\
\bhline
\end{tabular}
\caption{
Hyperparameters for rerankers.
}
\label{tab:hyperparameters-reranker}
\end{table*}
```

