# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[!t]
\centering
\caption{SOTA comparison on the three Amazon datasets. Baseline results are from Table~1 of ORT (OneRec-Think) \citep{liu-etal-2026-onerec}. OneRec-Think uses a Qwen3-8B backbone, whereas all of our variants use Qwen3-0.6B. The best scores are shown in bold, the second-best scores are underlined, and parenthesized percentages below our scores denote relative changes over ORT.}
% Ours (CE) uses the yes/no head with NTP loss, and Ours (TT) uses Shared+EOS, TL, CE2TT, and latent reasoning.
% We do not report 8B variants because the smaller batches required by our current training setup would substantially reduce the number of in-batch negatives, confounding a direct backbone-scaling comparison. 
\label{tab:sota_comparison}
\newcommand{\ortdiff}[2]{\begin{tabular}[c]{@{}c@{}}#1\\{\small #2}\end{tabular}}
\newcommand{\posdiff}[1]{\textcolor{green!50!black}{(+#1\%)}}
\newcommand{\negdiff}[1]{\textcolor{red!70!black}{(-#1\%)}}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccccccccc}
\toprule
 & \multicolumn{4}{c}{\textbf{Beauty}} & \multicolumn{4}{c}{\textbf{Sports}} & \multicolumn{4}{c}{\textbf{Toys}} \\
\cmidrule(lr){2-5} \cmidrule(lr){6-9} \cmidrule(lr){10-13}
\textbf{Model} & \textbf{R@5} & \textbf{R@10} & \textbf{N@5} & \textbf{N@10} & \textbf{R@5} & \textbf{R@10} & \textbf{N@5} & \textbf{N@10} & \textbf{R@5} & \textbf{R@10} & \textbf{N@5} & \textbf{N@10} \\
\midrule
BERT4Rec      & 0.0232 & 0.0396 & 0.0146 & 0.0199 & 0.0102 & 0.0175 & 0.0065 & 0.0088 & 0.0215 & 0.0332 & 0.0131 & 0.0168 \\
HGN           & 0.0319 & 0.0536 & 0.0196 & 0.0266 & 0.0183 & 0.0313 & 0.0109 & 0.0150 & 0.0326 & 0.0517 & 0.0192 & 0.0254 \\
GRU4Rec       & 0.0395 & 0.0584 & 0.0265 & 0.0326 & 0.0190 & 0.0312 & 0.0122 & 0.0161 & 0.0330 & 0.0490 & 0.0228 & 0.0279 \\
SASRec        & 0.0402 & 0.0607 & 0.0254 & 0.0320 & 0.0199 & 0.0301 & 0.0106 & 0.0141 & 0.0448 & 0.0626 & 0.0300 & 0.0358 \\
TIGER         & 0.0405 & 0.0623 & 0.0267 & 0.0337 & 0.0215 & 0.0347 & 0.0137 & 0.0179 & 0.0337 & 0.0547 & 0.0209 & 0.0276 \\
HSTU          & 0.0424 & 0.0652 & 0.0280 & 0.0353 & 0.0268 & 0.0343 & 0.0173 & 0.0226 & 0.0366 & 0.0566 & 0.0245 & 0.0309 \\
ReaRec        & 0.0450 & 0.0704 & 0.0262 & 0.0344 & 0.0214 & 0.0332 & 0.0116 & 0.0154 & 0.0523 & 0.0764 & 0.0298 & 0.0376 \\
ORT  & \underline{0.0563} & 0.0791 & \textbf{0.0398} & \underline{0.0471} & 0.0288 & 0.0412 & \underline{0.0199} & 0.0239 & 0.0579 & 0.0797 & \underline{0.0412} & 0.0482 \\
\midrule
Ours (TT)     & \ortdiff{0.0473}{\negdiff{16.0}} & \ortdiff{\underline{0.0825}}{\posdiff{4.3}} & \ortdiff{0.0267}{\negdiff{32.9}} & \ortdiff{0.0380}{\negdiff{19.3}} & \ortdiff{\underline{0.0320}}{\posdiff{11.1}} & \ortdiff{\underline{0.0542}}{\posdiff{31.6}} & \ortdiff{0.0193}{\negdiff{3.0}} & \ortdiff{\underline{0.0264}}{\posdiff{10.5}} & \ortdiff{\underline{0.0644}}{\posdiff{11.2}} & \ortdiff{\underline{0.1078}}{\posdiff{35.3}} & \ortdiff{0.0366}{\negdiff{11.2}} & \ortdiff{\underline{0.0506}}{\posdiff{5.0}} \\
\midrule
Ours (CE)     & \ortdiff{\textbf{0.0575}}{\posdiff{2.1}} & \ortdiff{\textbf{0.0957}}{\posdiff{21.0}} & \ortdiff{\underline{0.0351}}{\negdiff{11.8}} & \ortdiff{\textbf{0.0473}}{\posdiff{0.4}} & \ortdiff{\textbf{0.0438}}{\posdiff{52.1}} & \ortdiff{\textbf{0.0677}}{\posdiff{64.3}} & \ortdiff{\textbf{0.0289}}{\posdiff{45.2}} & \ortdiff{\textbf{0.0365}}{\posdiff{52.7}} & \ortdiff{\textbf{0.0829}}{\posdiff{43.2}} & \ortdiff{\textbf{0.1223}}{\posdiff{53.5}} & \ortdiff{\textbf{0.0555}}{\posdiff{34.7}} & \ortdiff{\textbf{0.0682}}{\posdiff{41.5}} \\
\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 2
```latex
\begin{table}[!t]
\centering
\caption{Performance comparison of CE teacher variants across the three Amazon datasets. The best is shown in bold.}
\label{tab:ce_results}
% \resizebox{\linewidth}{!}{%
\begin{tabular}{llcccc}
\toprule
\textbf{Dataset} & \textbf{Variant} & \textbf{R@5} & \textbf{R@10} & \textbf{N@5} & \textbf{N@10} \\
\midrule
\multirow{3}{*}{Beauty}
% & OneRec-Think                & 0.0563 & 0.0791 & \textbf{0.0398} & 0.0471 \\
& projection head        & 0.0509 & 0.0862 & 0.0307 & 0.0420 \\
& yes/no head            & 0.0535 & 0.0914 & 0.0328 & 0.0450 \\
& yes/no + NTP & \textbf{0.0575} & \textbf{0.0957} & \textbf{0.0351} & \textbf{0.0473} \\
\midrule
\multirow{3}{*}{Sports}
% & OneRec-Think                & 0.0288 & 0.0412 & 0.0199 & 0.0239 \\
& projection head        & 0.0391 & 0.0618 & 0.0245 & 0.0317 \\
& yes/no head            & 0.0317 & 0.0550 & 0.0195 & 0.0269 \\
& yes/no + NTP & \textbf{0.0438} & \textbf{0.0677} & \textbf{0.0289} & \textbf{0.0365} \\
\midrule
\multirow{3}{*}{Toys}
% & OneRec-Think                & 0.0579 & 0.0797 & 0.0412 & 0.0482 \\
& projection head        & 0.0757 & 0.1134 & 0.0492 & 0.0614 \\
& yes/no head            & 0.0814 & 0.1203 & 0.0517 & 0.0643 \\
& yes/no + NTP & \textbf{0.0829} & \textbf{0.1223} & \textbf{0.0555} & \textbf{0.0682} \\
\bottomrule
\end{tabular}
% }
\end{table}
```

## Table 3
```latex
\begin{table}[!t]
\centering
\caption{Leave-one-out ablation of the TT student across the three Amazon datasets. All variants use Shared+EOS; each ablated variant removes one component from the full model. The best score in each dataset--metric pair is shown in bold.}
\label{tab:tt_ablation_results}
\begin{tabular}{llcccc}
\toprule
\textbf{Dataset} & \textbf{Variant} & \textbf{R@5} & \textbf{R@10} & \textbf{N@5} & \textbf{N@10} \\
\midrule
\multirow{4}{*}{Beauty}
& Full & \textbf{0.0473} & \textbf{0.0825} & 0.0267 & \textbf{0.0380} \\
& w/o TL & 0.0431 & 0.0812 & 0.0241 & 0.0363 \\
& w/o CE2TT & 0.0427 & 0.0715 & 0.0252 & 0.0345 \\
& w/o Latent & 0.0463 & 0.0794 & \textbf{0.0269} & 0.0374 \\
\midrule
\multirow{4}{*}{Sports}
& Full & \textbf{0.0320} & \textbf{0.0542} & \textbf{0.0193} & \textbf{0.0264} \\
& w/o TL & 0.0300 & 0.0515 & 0.0174 & 0.0243 \\
& w/o CE2TT & 0.0258 & 0.0417 & 0.0160 & 0.0211 \\
& w/o Latent & 0.0308 & 0.0530 & 0.0185 & 0.0257 \\
\midrule
\multirow{4}{*}{Toys}
& Full & 0.0644 & \textbf{0.1078} & 0.0366 & \textbf{0.0506} \\
& w/o TL & 0.0604 & 0.1050 & 0.0346 & 0.0490 \\
& w/o CE2TT & 0.0626 & 0.0992 & \textbf{0.0383} & 0.0502 \\
& w/o Latent & \textbf{0.0650} & 0.1063 & 0.0370 & 0.0503 \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
\centering
\caption{Improving serving efficiency for LLM-native TT without hurting NE}
\label{tab:internal-efficiency}
\begin{tabular}{ll}
\toprule
Technique & QPS Gain \\
\midrule
Numerical Features FSQ Compression & 19.7\% \\
Depth pruning & 10.6\% \\
Static vocabulary pruning  & 2.0\% \\
Post-training Quantization & 13.6\% \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 5
```latex
\begin{table}[t]
\centering
\caption{Staleness. Both DLRM and LLM-Native model is trained until $ds{+}0$ and evaluated on 
$ds{+}1$/$ds{+}2$/$ds{+}3$ (negative =
degradation).}
\label{tab:internal-staleness}
\begin{tabular}{llll}
\toprule
Model & $ds{+}1$ (NE) & $ds{+}2$ & $ds{+}3$ \\
\midrule
DLRM (production) & baseline & baseline & baseline \\
Frozen DLRM & baseline & $-2.68\%$ & $-4.30\%$ \\
Frozen LLM-Native CE     & $+2.25\%$ & $+2.21\%$ & $+2.23\%$ \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 6
```latex
\begin{table}[t]
\centering
\caption{Data scaling. The model performance (NE) is the same at $1\times$ data while LLM-Native CE shows NE gains at  $2\times$/$3\times$ relative to that model's own
$1\times$ point.}
\label{tab:internal-datascaling}
\begin{tabular}{lll}
\toprule
Model & $2\times$ & $3\times$ \\
\midrule
DLRM (production)   & $+1.30\%$ & $+1.80\%$ \\
LLM-native CE       & $+1.59\%$ & $+2.19\%$ \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 7
```latex
\begin{table}[t]
\centering
\caption{Headroom Study: Gains from Model Scaling}
\label{tab:internal-capacity}
\begin{tabular}{ll}
\toprule
Variant & NE gain \\
\midrule
LLM-Native CE $0.6\text{B}$ & baseline \\
+ Latent reasoning (residual-stream)          & $+0.41\%$ \\
+ Mixtral MoE ($8$ experts, top-$2$)                & $+0.91\%$ \\
LLM-Native CE $4\text{B}$ & $+1.90\%$ \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 8
```latex
\begin{table}[t]
% \centering
% \caption{Incremental NE gains from POLAR modeling techniques (each relative to
% its own ablation baseline). $^{\dagger}$Early results.}
% \label{tab:internal-methods}
% \begin{tabular}{ll}
% \toprule
% Technique & NE gain \\
% \midrule
% Latent reasoning (residual-stream)          & $+0.41\%$ \\
% Agentic memory (MOCHA, Dual Encoder)$^{\dagger}$ & $+0.3$--$0.5\%$ \\
% Data scaling ($3\times$)                     & $+0.5\%$ \\
% CrossEncoder $\rightarrow$ Dual Encoder distillation & $35\%$ KTR \\
% \bottomrule
% \end{tabular}
% \end{table}
```

## Table 9
```latex
\begin{table*}[!h]
\centering
\caption{Statistics of the three processed Amazon review datasets.}
\label{tab:dataset_statistics}
\begin{tabular}{lrrrr}
\toprule
Dataset & \# Users & \# Items & Mean Len. & Median Len. \\
\midrule
Beauty & 22,363 & 12,101 & 8.87 & 6 \\
Sports and Outdoors & 35,598 & 18,357 & 8.32 & 6 \\
Toys and Games & 19,412 & 11,924 & 8.63 & 6 \\
\bottomrule
\end{tabular}
\end{table*}
```

## Table 10
```latex
\begin{table}[t]
\centering
\caption{Cross-encoder (yes/no head + NTP loss) hyperparameters.}
\label{tab:ce-hparams}
\begin{tabular}{ll}
\toprule
Hyperparameter & Value \\
\midrule
Negatives per positive & $31$ \\
NTP loss weight $\lambda_{\mathrm{ntp}}$ & $0.5$ \\
Epochs & $10$ \\
GPUs & $4\times$ A100-80GB \\
Per-GPU batch & $32$ \\
Effective batch & $128$ \\
Learning rate & $2\times10^{-5}$ \\
Weight decay & $0.01$ \\
Warmup ratio & $0.1$ \\
Max length (query / item) & $512$ / $128$ \\
Precision & bf16 \\
Seed & $42$ \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 11
```latex
\begin{table}[t]
\centering
\caption{Two-tower retriever hyperparameters (shared encoder, EOS pooling,
transfer $+$ CE$\to$TT distillation $+$ latent reasoning).}
\label{tab:tt-hparams}
% \resizebox{\linewidth}{!}{%
\begin{tabular}{ll}
\toprule
Hyperparameter & Value \\
\midrule
Embedding & raw $1024$-d \\
Similarity / temperature $\tau$ & dot product / $0.07$ \\
\midrule
\multicolumn{2}{l}{\emph{Pre-training \& fine-tuning (transfer)}} \\
GPUs & $4\times$ A100-80GB \\
Per-GPU batch & $32$ \\
Epochs & $10$ \\
Learning rate & $2\times10^{-5}$ \\
\midrule
\multicolumn{2}{l}{\emph{CE$\to$TT distillation}} \\
GPUs & $8\times$ A100-80GB \\
Per-GPU batch & $32$ \\
In-batch negatives & $31$ \\
Teacher candidates $K$ & $50$ \\
Epochs & $5$ \\
Learning rate & $1\times10^{-5}$ \\
KD loss weight $\lambda_{\mathrm{KD}}$ & $0.2$ \\
Distill temperature $\mathcal{T}$ & $1.0$ (Beauty) / $0.5$ (Sports, Toys) \\
\midrule
\multicolumn{2}{l}{\emph{Shared}} \\
Optimizer & AdamW (wd $0.01$, warmup $0.1$) \\
Max length (query / item) & $512$ / $128$ \\
Precision & bf16 \\
Seed & $42$ \\
\bottomrule
\end{tabular}
% }
\end{table}
```

## Table 12
```latex
\begin{table*}[!t]
\centering
\caption{Complete two-tower ablation across the three Amazon datasets. The best score in each dataset--metric pair is shown in bold.}
\label{tab:tt_ablation_full_results}
\begin{tabular}{lcccccccc}
\toprule
\textbf{Dataset} & \textbf{Shared+EOS} & \textbf{TL} & \textbf{CE2TT} & \textbf{Latent} & \textbf{R@5} & \textbf{R@10} & \textbf{N@5} & \textbf{N@10} \\
\midrule
\multirow{9}{*}{Beauty}
& - & - & - & - & 0.0214 & 0.0389 & 0.0125 & 0.0180 \\
& \checkmark & - & - & - & 0.0415 & 0.0672 & 0.0253 & 0.0337 \\
& \checkmark & - & \checkmark & - & 0.0429 & 0.0800 & 0.0241 & 0.0360 \\
& \checkmark & \checkmark & - & - & 0.0430 & 0.0714 & 0.0260 & 0.0351 \\
& \checkmark & \checkmark & \checkmark & - & 0.0463 & 0.0794 & \textbf{0.0269} & 0.0374 \\
& \checkmark & - & - & \checkmark & 0.0425 & 0.0711 & 0.0251 & 0.0343 \\
& \checkmark & - & \checkmark & \checkmark & 0.0431 & 0.0812 & 0.0241 & 0.0363 \\
& \checkmark & \checkmark & - & \checkmark & 0.0427 & 0.0715 & 0.0252 & 0.0345 \\
& \checkmark & \checkmark & \checkmark & \checkmark & \textbf{0.0473} & \textbf{0.0825} & 0.0267 & \textbf{0.0380} \\
\midrule
\multirow{9}{*}{Sports}
& - & - & - & - & 0.0054 & 0.0109 & 0.0033 & 0.0050 \\
& \checkmark & - & - & - & 0.0205 & 0.0347 & 0.0131 & 0.0177 \\
& \checkmark & - & \checkmark & - & 0.0298 & 0.0510 & 0.0175 & 0.0243 \\
& \checkmark & \checkmark & - & - & 0.0261 & 0.0426 & 0.0166 & 0.0219 \\
& \checkmark & \checkmark & \checkmark & - & 0.0308 & 0.0530 & 0.0185 & 0.0257 \\
& \checkmark & - & - & \checkmark & 0.0223 & 0.0387 & 0.0132 & 0.0184 \\
& \checkmark & - & \checkmark & \checkmark & 0.0300 & 0.0515 & 0.0174 & 0.0243 \\
& \checkmark & \checkmark & - & \checkmark & 0.0258 & 0.0417 & 0.0160 & 0.0211 \\
& \checkmark & \checkmark & \checkmark & \checkmark & \textbf{0.0320} & \textbf{0.0542} & \textbf{0.0193} & \textbf{0.0264} \\
\midrule
\multirow{9}{*}{Toys}
& - & - & - & - & 0.0294 & 0.0489 & 0.0175 & 0.0237 \\
& \checkmark & - & - & - & 0.0600 & 0.0968 & 0.0367 & 0.0487 \\
& \checkmark & - & \checkmark & - & 0.0614 & 0.1049 & 0.0353 & 0.0493 \\
& \checkmark & \checkmark & - & - & 0.0563 & 0.0928 & 0.0332 & 0.0450 \\
& \checkmark & \checkmark & \checkmark & - & \textbf{0.0650} & 0.1063 & 0.0370 & 0.0503 \\
& \checkmark & - & - & \checkmark & 0.0604 & 0.0946 & \textbf{0.0383} & 0.0493 \\
& \checkmark & - & \checkmark & \checkmark & 0.0604 & 0.1050 & 0.0346 & 0.0490 \\
& \checkmark & \checkmark & - & \checkmark & 0.0626 & 0.0992 & \textbf{0.0383} & 0.0502 \\
& \checkmark & \checkmark & \checkmark & \checkmark & 0.0644 & \textbf{0.1078} & 0.0366 & \textbf{0.0506} \\
\bottomrule
\end{tabular}
\end{table*}
```

