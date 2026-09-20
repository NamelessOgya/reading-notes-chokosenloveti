# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[h]
\small
\centering
\caption{Detailed architectures used in the max regression experiments.}
\vspace{5pt}
\begin{tabular}{@{}cccc@{}}\toprule
\multicolumn{2}{c}{Encoder} & \multicolumn{2}{c}{Decoder}\\
\cmidrule(lr){1-2} \cmidrule(lr){3-4}
FF & SAB & Pooling & PMA \\
\midrule
$\fc(64,\relu)$ & $\sab(64, 4)$ & $\mathrm{mean, sum, max}$ & $\pma_1(64,4)$\\
$\fc(64,\relu)$ & $\sab(64, 4)$ & $\fc(64,\relu)$ & $\fc(1,-)$\\
$\fc(64,\relu)$ & & $\fc(1,-)$ & \\
$\fc(64,-)$ & & & \\
\bottomrule
\end{tabular}
\label{tab:max_architecture}
\end{table}
```

## Table 2
```latex
\begin{table}[h]
\centering
\caption{Detailed results for the unique character counting experiment.}
\vspace{5pt}
\begin{tabular}{@{}cc@{}} \toprule
Architecture & Accuracy\\ \midrule
rFF + Pooling & 0.4366 $\pm$ 0.0071 \\
rFF + PMA & 0.4617 $\pm$ 0.0073\\
rFFp-mean + Pooling & 0.4617 $\pm$ 0.0076 \\
rFFp-max + Pooling & 0.4359 $\pm$ 0.0077 \\
rFF + Dotprod & 0.4471 $\pm$ 0.0076 \\
\hline
SAB + Pooling & 0.5659 $\pm$ 0.0067 \\
SAB + Dotprod & 0.5888 $\pm$ 0.0072 \\
SAB + PMA (1) & \bf 0.6037 $\pm$ 0.0072\\
SAB + PMA (2) & 0.5806 $\pm$ 0.0075\\
SAB + PMA (4) & 0.5945 $\pm$ 0.0072\\
SAB + PMA (8)  & 0.6001 $\pm$ 0.0078\\
\bottomrule
\end{tabular}
\label{table:appunique}
\end{table}
```

## Table 3
```latex
\begin{table}[h]
\small
\centering
\caption{Detailed architectures used in the unique character counting experiments.}
\vspace{5pt}
\begin{tabular}{@{}cccc@{}}\toprule
\multicolumn{2}{c}{Encoder} & \multicolumn{2}{c}{Decoder}\\
\cmidrule(lr){1-2} \cmidrule(lr){3-4}
rFF & SAB & Pooling & PMA \\
\midrule
$\conv(64, 3, 2, \bn, \relu)$ & $\conv(64, 3, 2, \bn, \relu)$ & $\mathrm{mean}$ & $\pma_1(8, 8)$ \\
$\conv(64, 3, 2, \bn, \relu)$ & $\conv(64, 3, 2, \bn, \relu)$ & $\fc(64, \relu)$ & $\fc(1, \mathrm{softplus})$ \\
$\conv(64, 3, 2, \bn, \relu)$ & $\conv(64, 3, 2,\bn,\relu)$ & $\fc(1,\mathrm{softplus})$ & \\
$\conv(64, 3, 2, \bn, \relu)$ & $\conv(64,3,2,\bn,\relu)$ & & \\
$\fc(64,\relu)$ & $\sab(64,4)$ & & \\
$\fc(64,\relu)$ & $\sab(64,4)$ & & \\
$\fc(64,\relu)$& & & \\
$\fc(64,-)$ & & & \\
\bottomrule
\end{tabular}
\label{tab:unique_architecture}
\end{table}
```

## Table 4
```latex
\begin{table}[h]
\small
\centering
\caption{Detailed architectures used in 2D synthetic experiments.}
\vspace{5pt}
\begin{tabular}{@{}ccccc@{}}\toprule
\multicolumn{3}{c}{Encoder} & \multicolumn{2}{c}{Decoder}\\
\cmidrule(lr){1-3} \cmidrule(lr){4-5}
rFF & SAB & ISAB & Pooling & PMA \\
\midrule
$\fc(128,\relu)$ & $\sab(128,4)$ & $\isab_m(128,4)$ & $\mathrm{mean}$ & $\pma_4(128,4)$\\
$\fc(128,\relu)$ & $\sab(128,4)$ & $\isab_m(128,4)$ & $\fc(128,\relu)$ & $\sab(128,4)$\\
$\fc(128,\relu)$ & & & $\fc(128,\relu)$ & $\fc(4\cdot(1+2\cdot 2),-)$ \\
$\fc(128,\relu)$& & & $\fc(128,\relu)$ & \\
& & & $\fc(4\cdot(1+2\cdot 2),-)$ & \\
\bottomrule
\end{tabular}
\label{tab:2d_synthetic_architecture}
\end{table}
```

## Table 5
```latex
\begin{table}[h]
\centering
\caption{Average log-likelihood/data (LL0/data) and average log-likelihood/data after single EM iteration (LL1/data) the clustering experiment. The number inside parenthesis  indicates the number of inducing points used in the SABs of encoder. For all PMAs, four seed vectors were used.}
\vspace{5pt}
\begin{tabular}{@{}ccc@{}} \toprule
Architecture & LL0/data & LL1/data \\ \midrule
Oracle & -1.4726 & \\
\hline
rFF + Pooling& -2.0006 $\pm$ 0.0123 &-1.6186 $\pm$ 0.0042 \\
rFFp-mean + Pooling & -1.7606 $\pm$ 0.0213 &-1.5191 $\pm$ 0.0026 \\
rFFp-max + Pooling & -1.7692 $\pm$ 0.0130 &-1.5103 $\pm$ 0.0035 \\
rFF+Dotprod & -1.8549 $\pm$ 0.0128 &-1.5621 $\pm$ 0.0046 \\
\hline
SAB + Pooling & -1.6772 $\pm$ 0.0066 &-1.5070 $\pm$ 0.0115 \\
ISAB (16) + Pooling & -1.6955 $\pm$ 0.0730 &-1.4742 $\pm$ 0.0158 \\
ISAB (32) + Pooling & -1.6353 $\pm$ 0.0182 &-1.4681 $\pm$ 0.0038 \\
ISAB (64) + Pooling & -1.6349 $\pm$ 0.0429 &-1.4664 $\pm$ 0.0080 \\
rFF + PMA  & -1.6680 $\pm$ 0.0040 &-1.5409 $\pm$ 0.0037 \\
SAB + PMA  & -1.5145 $\pm$ 0.0046 &-1.4619 $\pm$ 0.0048 \\
ISAB (16) + PMA & -1.5009 $\pm$ 0.0068 &-1.4530 $\pm$ 0.0037 \\
ISAB (32) + PMA & \bf -1.4963 $\pm$ 0.0064 & \bf-1.4524 $\pm$ 0.0044 \\
ISAB (64) + PMA & -1.5042 $\pm$ 0.0158 &-1.4535 $\pm$ 0.0053 \\
\bottomrule
\end{tabular}
\label{tab:2d_synthetic_more_results}
\end{table}
```

## Table 6
```latex
\begin{table}
\centering
\caption{Average log-likelihood/data (LL0/data) and average log-likelihood/data after single EM iteration (LL1/data) the clustering experiment on large-scale data. The number inside parenthesis  indicates the number of inducing points used in the SABs of encoder. For all PMAs, six seed vectors were used.}
\vspace{5pt}
\begin{tabular}{@{}ccc@{}} \toprule
Architecture & LL0/data & LL1/data \\ \midrule
Oracle & -1.8202 & \\
\hline
rFF + Pooling & -2.5195 $\pm$ 0.0105 &-2.0709 $\pm$ 0.0062 \\
rFFp-mean + Pooling & -2.3126 $\pm$ 0.0154 &-1.9749 $\pm$ 0.0062 \\
\hline
rFF + PMA (6) & -2.0515 $\pm$ 0.0067 &-1.9424 $\pm$ 0.0047 \\
SAB (32) + PMA (6) & \bf-1.8928 $\pm$ 0.0076 & \bf-1.8549 $\pm$ 0.0024 \\
\bottomrule
\end{tabular}
\label{tab:2d_synthetic_large_scale}
\end{table}
```

## Table 7
```latex
\begin{table}
\small
\centering
\caption{Detailed architectures used in CIFAR-100 meta clustering experiments.}
\vspace{5pt}
\begin{tabular}{@{}ccccc@{}}\toprule
\multicolumn{3}{c}{Encoder} & \multicolumn{2}{c}{Decoder}\\
\cmidrule(lr){1-3} \cmidrule(lr){4-5}
rFF & SAB & ISAB & rFF & PMA \\
\midrule
$\fc(256,\relu)$ & $\sab(256, 4)$ & $\isab_m(256, 4)$ & $\mathrm{mean}$ & $\pma_4(128,4)$\\
$\fc(256,\relu)$ &  $\sab(256, 4)$ & $\isab_m(256, 4)$ & $\fc(256,\relu)$ & $\sab(256, 4)$\\
$\fc(256,\relu)$ &  $\sab(256, 4)$ & $\isab_m(256, 4)$ & $\fc(256,\relu)$ & $\sab(256, 4)$ \\
$\fc(256,\relu)$ & & & $\fc(256,\relu)$) & $\fc(4\cdot(1+2\cdot 512),-)$ \\
$\fc(256,\relu)$ & & &$\fc(256,\relu)$ & \\
$\fc(256,-)$ & & & $\fc(256,\relu)$ & \\
 & & & $\fc(4\cdot(1+2\cdot 512),-)$& \\
\bottomrule
\end{tabular}
\label{tab:cifar100_architecture}
\end{table}
```

## Table 8
```latex
\begin{table}
\centering
\caption{Average clustering accuracies measured by Adjusted Rand Index (ARI) for CIFAR100 clustering experiments. The number inside parenthesis  indicates the number of inducing points used in the SABs of encoder. For all PMAs, four seed vectors were used.
}
\vspace{5pt}
\begin{tabular}{@{}ccc@{}} \toprule
Architecture & ARI0 & ARI1 \\ \midrule
Oracle & 0.9151 & \\
rFF + Pooling & 0.5593 $\pm$ 0.0149 &0.5693 $\pm$ 0.0171 \\
rFFp-mean + Pooling & 0.5673 $\pm$ 0.0053 &0.5798 $\pm$ 0.0058 \\
rFFp-max + Pooling & 0.5369 $\pm$ 0.0154 &0.5536 $\pm$ 0.0186 \\
rFF+Dotprod & 0.5666 $\pm$ 0.0221 &0.5763 $\pm$ 0.0212 \\
\hline
SAB + Pooling & 0.5831 $\pm$ 0.0341 &0.5943 $\pm$ 0.0337 \\
ISAB (16) + Pooling  & 0.5672 $\pm$ 0.0124 &0.5805 $\pm$ 0.0122 \\
ISAB (32) + Pooling & 0.5587 $\pm$ 0.0104 &0.5700 $\pm$ 0.0134 \\
ISAB (64) +  Pooling & 0.5586 $\pm$ 0.0205 &0.5708 $\pm$ 0.0183 \\
rFF + PMA  & 0.7612 $\pm$ 0.0237 &0.7670 $\pm$ 0.0231 \\
SAB + PMA & 0.9015 $\pm$ 0.0097 &0.9024 $\pm$ 0.0097 \\
ISAB (16) + PMA & \bf 0.9210 $\pm$ 0.0055 &\bf 0.9223 $\pm$ 0.0056 \\
ISAB (32) + PMA & 0.9103 $\pm$ 0.0061 &0.9119 $\pm$ 0.0052 \\
ISAB (64) + PMA & 0.9141 $\pm$ 0.0040 &0.9153 $\pm$ 0.0041 \\
\bottomrule
\end{tabular}
\label{tab:cifar100_more_results}
\end{table}
```

## Table 9
```latex
\begin{table}[h]
\small
\centering
\caption{Detailed architectures used in CelebA meta set anomaly experiments.
$\conv(d, k, s, r, f)$ is a convolutional layer with $d$ output channels, $k$ kernel size, $s$ stride size, $r$ regularization method, and activation function $f$. If $d$ is a list, each element in the list is distributed.
$\fc(d, f, r)$ denotes a fully-connected layer with $d$ units, activation function $f$ and $r$ regularization method.
If ${d}$ is a list, each element in the list is distributed.
$\sab(d, h)$ denotes the SAB with $d$ units and $h$ heads.
%$\mathrm{ISAB}(d, h, n_{\mathrm{ind}})$ denotes the ISAB with $d$ units, $h$ heads and $n_{\mathrm{ind}}$ inducing points.
$\pma(d, h, n_{\mathrm{seed}})$ denotes the PMA with $d$ units, $h$ heads and $n_{\mathrm{seed}}$ vectors.
All MABs used in SAB and PMA uses FC layers with ReLU activations for rFF layers.}
\vspace{5pt}
\begin{tabular}{@{}cccc@{}}\toprule
\multicolumn{2}{c}{Encoder} & \multicolumn{2}{c}{Decoder}\\
\cmidrule(lr){1-2} \cmidrule(lr){3-4}
rFF & SAB & Pooling & PMA \\
\midrule
\multicolumn{2}{c}{$\conv([32, 64, 128], 3, 2, \mathrm{Dropout}, \relu)$} & $\mathrm{mean}$ & $\pma_4(128, 4)$ \\
\multicolumn{2}{c}{$\fc([1024, 512, 256], -, \mathrm{Dropout})$} & $\fc(128, \relu, -)$ & $\sab(128, 4)$ \\
\multicolumn{2}{c}{$\fc(256, -, -)$} & $\fc(128, \relu, -)$ & $\fc(256 \cdot 8, -, -)$ \\
$\fc([128, 128, 128], \relu, -)$ & $\sab(128,4)$ & $\fc(128, \relu, -)$ & \\
$\fc([128, 128, 128], \relu, -)$ & $\sab(128,4)$  & $\fc(256 \cdot 8, -, -)$ & \\
$\fc(128, \relu, -)$ & $\sab(128,4)$ & & \\
$\fc(128, -, -)$ & $\sab(128, 4)$ & & \\
\bottomrule
\end{tabular}
\label{tab:meta_anomaly_architecture}
\end{table}
```

## Table 10
```latex
\begin{table}[h]
\small
\centering
\caption{Detailed architectures used in the point cloud classification experiments.}
\vspace{5pt}
\begin{tabular}{@{}cccc@{}}\toprule
\multicolumn{2}{c}{Encoder} & \multicolumn{2}{c}{Decoder}\\
\cmidrule(lr){1-2} \cmidrule(lr){3-4}
rFF & ISAB & Pooling & PMA \\
\midrule
$\fc(256, \relu)$ & $\isab(256, 4)$ & $\max$& $\mathrm{Dropout}(0.5)$ \\
$\fc(256, \relu)$  & $\isab(256, 4)$ & $\mathrm{Dropout}(0.5)$ & $\pma_1(256, 4)$ \\
$\fc(256, \relu)$  & & $\fc(256, \relu)$ & $\mathrm{Dropout}(0.5)$ \\
$\fc(256, -)$ & &$\mathrm{Dropout}(0.5)$ & $\fc(40, -)$ \\
&&$\fc(40, -)$ &\\
\bottomrule
\end{tabular}
\label{tab:pointcloud_architecture}
\end{table}
```

## Table 11
```latex
\begin{table}[h]
\centering
\caption{Additional point cloud experiments using 100 points.}
\begin{tabular}{@{}ccccc@{}}
\toprule
Architecture & Accuracy\\
\midrule
rFF + Pooling & 0.7951 $\pm$ 0.0166 \\
rFF + PMA (1) & 0.8076 $\pm$ 0.0160 \\
ISAB (16) + Pooling & 0.8273 $\pm$ 0.0159 \\
Set Transformer (16) & \bf 0.8454 $\pm$ 0.0144 \\
\midrule
rFF + Pooling + tricks \citep{Zaheer2017} & 0.82 $\pm$ 0.02 \\
\bottomrule
\end{tabular}
\label{table:app_pointcloud100}
\vspace{10pt}
\centering
\caption{Additional point cloud experiments using 5000 points.}
\begin{tabular}{@{}ccccc@{}}
\toprule
Architecture & Accuracy\\
\midrule
rFF + Pooling & 0.8933 $\pm$ 0.0156 \\
rFF + PMA (1) & 0.8628 $\pm$ 0.0136 \\
ISAB (16) + Pooling & \bf 0.9040 $\pm$ 0.0173 \\
Set Transformer (16) & 0.8779 $\pm$ 0.0122 \\
\midrule
rFF + Pooling + tricks \citep{Zaheer2017} & \bf 0.90 $\pm$ 0.003 \\
\bottomrule
\end{tabular}
\label{table:app_pointcloud5k}
\end{table}
```

## Table 12
```latex
\begin{table}[t]
\centering
\small
\caption{Time complexity of various set operations. $n$ is the number of items, $d$ is the dimensionality of each item, and $m$ is the number of inducing points.}
\label{tab:complexities}
\begin{center}
\vspace{-1mm}

\begin{tabular}{lccc}
\toprule
Set operations & Time complexity & High-order & Permutation \\
&& interactions & invariant \\
\hline
%Fully- Connected (naive) & $O(n^2d^2)$ & Yes & No \\
\rule{0pt}{2.0ex}Recurrent & $O(nd)$ & Yes & No \\
Pooling~\citep{Zaheer2017} & $O(nd)$ & No & Yes \\
Relational Networks~\citep{Santoro2017} & $O(n^2d)$ & Yes & Yes \\
\midrule
Set Transformer (SAB + PMA, ours) & $O(n^2d)$ & Yes & Yes \\
Set Transformer (ISAB + PMA, ours) & $O(nmd)$ & Yes & Yes \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 13
```latex
\begin{table}[t]
\centering
\small
\caption{Mean absolute errors on the max regression task.}
\vspace{5pt}
\begin{tabular}{@{}ccccc@{}}
\toprule
Architecture & MAE \\\midrule
rFF + Pooling ($\mathrm{mean}$) & 2.133 $\pm$ 0.190 \\
rFF + Pooling ($\mathrm{sum}$) & 1.902 $\pm$ 0.137 \\
rFF + Pooling ($\mathrm{max}$) & \bf 0.1355 $\pm$ 0.0074\\
\midrule
SAB + PMA (ours) & 0.2085 $\pm$ 0.0127\\
\bottomrule
\label{table:max}
\end{tabular}
\end{table}
```

## Table 14
```latex
\begin{table}[t]
\centering
\small
\caption{Accuracy on the unique character counting task.}
\vspace{5pt}
\begin{tabular}{@{}cc@{}} \toprule
Architecture & Accuracy \\ \midrule
rFF + Pooling & 0.4382 $\pm$ 0.0072 \\
rFFp-mean + Pooling & 0.4617 $\pm$ 0.0076 \\
rFFp-max + Pooling & 0.4359 $\pm$ 0.0077 \\
rFF + Dotprod & 0.4471 $\pm$ 0.0076 \\
\midrule
rFF + PMA (ours) & 0.4572 $\pm$ 0.0076\\
SAB + Pooling (ours) & 0.5659 $\pm$ 0.0077 \\
SAB + PMA (ours) & \bf 0.6037 $\pm$ 0.0075 \\
\bottomrule
\label{table:unique}
\end{tabular}
\end{table}
```

## Table 15
```latex
\begin{table*}[h]
	\centering
	\small
	\caption{Meta clustering results.
	The number inside parenthesis indicates the number of inducing points used in ISABs of encoders.
	We show average likelihood per data for the synthetic dataset and the adjusted rand index (ARI) for the CIFAR-100 experiment.
	LL1/data, ARI1 are the evaluation metrics after a single EM update step.
	The oracle for the synthetic dataset is the log likelihood of the actual parameters used to generate the set, and the CIFAR oracle was computed by running EM until convergence.
	%The results measured from function outputs (LL0/data, ARI0) and the results after single EM update (LL1/data, ARI1) are presented.
	}
	\vspace{5pt}
	\begin{tabular}{@{}ccccc@{}}\toprule
		& \multicolumn{2}{c}{Synthetic} & \multicolumn{2}{c}{CIFAR-100} \\
		\cmidrule{2-3}
		\cmidrule{4-5}
	Architecture & LL0/data & LL1/data & ARI0 & ARI1  \\
	\midrule
	Oracle & -1.4726 & & 0.9150 &\\
	rFF + Pooling & -2.0006 $\pm$ 0.0123 &-1.6186 $\pm$ 0.0042 & 0.5593 $\pm$ 0.0149 & 0.5693 $\pm$ 0.0171 \\
	rFFp-mean + Pooling & -1.7606 $\pm$ 0.0213 &-1.5191 $\pm$ 0.0026 & 0.5673 $\pm$ 0.0053 &0.5798 $\pm$ 0.0058 \\
	rFFp-max + Pooling & -1.7692 $\pm$ 0.0130 &-1.5103 $\pm$ 0.0035 & 0.5369 $\pm$ 0.0154 &0.5536 $\pm$ 0.0186 \\
	rFF + Dotprod & -1.8549 $\pm$ 0.0128 &-1.5621 $\pm$ 0.0046 & 0.5666 $\pm$ 0.0221 &0.5763 $\pm$ 0.0212 \\
    \midrule
	SAB + Pooling (ours) & -1.6772 $\pm$ 0.0066 &-1.5070 $\pm$ 0.0115 & 0.5831 $\pm$ 0.0341 &0.5943 $\pm$ 0.0337\\
	ISAB (16) + Pooling (ours) & -1.6955 $\pm$ 0.0730 &-1.4742 $\pm$ 0.0158 & 0.5672 $\pm$ 0.0124 &0.5805 $\pm$ 0.0122\\
	rFF + PMA (ours) & -1.6680 $\pm$ 0.0040 &-1.5409 $\pm$ 0.0037 &  0.7612 $\pm$ 0.0237 &0.7670 $\pm$ 0.0231\\
	SAB + PMA (ours) & -1.5145 $\pm$ 0.0046 &-1.4619 $\pm$ 0.0048 &  0.9015 $\pm$ 0.0097 &0.9024 $\pm$ 0.0097\\
	ISAB (16) + PMA (ours) & \bf -1.5009 $\pm$ 0.0068 & \bf -1.4530 $\pm$ 0.0037 & \bf 0.9210 $\pm$ 0.0055 &\bf 0.9223 $\pm$ 0.0056 \\
	\bottomrule
	\end{tabular}
	\label{tab:meta_clustering}
\end{table*}
```

## Table 16
```latex
\begin{table*}[t]
\centering
\small
\caption{
Test accuracy for the point cloud classification task using $100, 1000, 5000$ points.
}
\vspace{5pt}
\begin{tabular}{@{}ccccc@{}}
\toprule
Architecture & 100 pts & 1000 pts & 5000 pts \\
\midrule
rFF + Pooling \citep{Zaheer2017} & - & 0.83 $\pm$ 0.01 & - \\
rFFp-max + Pooling \citep{Zaheer2017} & 0.82 $\pm$ 0.02  & 0.87 $\pm$ 0.01& \bf 0.90 $\pm$ 0.003 \\
\midrule
rFF + Pooling& 0.7951 $\pm$ 0.0166  & 0.8551 $\pm$ 0.0142 & 0.8933 $\pm$ 0.0156  \\
\midrule
rFF + PMA (ours) & 0.8076 $\pm$ 0.0160 & 0.8534 $\pm$ 0.0152  & 0.8628 $\pm$ 0.0136\\
ISAB (16) + Pooling (ours) & 0.8273 $\pm$ 0.0159 & \bf 0.8915 $\pm$ 0.0144 & \bf 0.9040 $\pm$ 0.0173  \\
ISAB (16) + PMA (ours) & \bf 0.8454 $\pm$ 0.0144 & 0.8662 $\pm$ 0.0149 & 0.8779 $\pm$ 0.0122  \\
\bottomrule
\end{tabular}
\label{table:pointcloud}
\end{table*}
```

## Table 17
```latex
\begin{table}[t]
\centering
\small
\caption{Meta set anomaly results.
Each architecture is evaluated using average of test AUROC and test AUPR.
%Random guess shows AUROC as 0.5 and AUPR as 0.125.
%Other describing methods are same with the above description.
%200 test datasets are used to measure the performance of each model and all experiments are repeated 5 times.
}
\vspace{5pt}
\begin{tabular}{@{}ccccc@{}}\toprule
Architecture & Test AUROC & Test AUPR  \\
\midrule
Random guess & 0.5 & 0.125 \\
rFF + Pooling & 0.5643 $\pm$ 0.0139 & 0.4126 $\pm$ 0.0108 \\
rFFp-mean + Pooling & 0.5687 $\pm$ 0.0061 & 0.4125 $\pm$ 0.0127 \\
rFFp-max + Pooling & 0.5717 $\pm$ 0.0117 & 0.4135 $\pm$ 0.0162 \\
rFF + Dotprod & 0.5671 $\pm$ 0.0139 & 0.4155 $\pm$ 0.0115 \\
\midrule
SAB + Pooling (ours) & 0.5757 $\pm$ 0.0143 & 0.4189 $\pm$ 0.0167 \\
%ISAB (4) + Pooling & 0.5679 $\pm$ 0.0155 & 0.4202 $\pm$ 0.0166 \\
rFF + PMA (ours) & 0.5756 $\pm$ 0.0130 & 0.4227 $\pm$ 0.0127 \\
SAB + PMA (ours) & \bf 0.5941 $\pm$ 0.0170 & \bf 0.4386 $\pm$ 0.0089 \\
%Set Transformer (4) & 0.5629 $\pm$ 0.0167 & 0.4122 $\pm$ 0.0151 \\
\bottomrule
\end{tabular}
\label{tab:meta_anomaly}
\end{table}
```

