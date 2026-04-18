# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\vspace{-5pt}
\caption{Statistics of datasets after preprocessing.}
\label{stat_dataset}
\vspace{-8pt}
\centering
% \scriptsize
\begin{tabularx}{0.42\textwidth}{lcccc}
\toprule 
Dataset & \# users & \# items & \# Interactions & sparsity \\
\midrule
Movies & 20,515 & 44,014 & 637,157 & 00.07\%   \\
Toys & 19,412 & 11,924 &  138,444 & 00.06\%   \\
Sports & 35,598 & 18,357 & 256,598 & 00.04\%   \\
\midrule
\end{tabularx}
\vspace{-8pt}
\end{table}
```

## Table 2
```latex
\begin{table*}[ht!]
\centering
\arraybackslash
\footnotesize
\caption{Performance comparison across different backbones and methods on three datasets with cold-start user settings. Boldface indicates the highest score, while underlining denotes the second-best result among the models. }
\vspace{-5pt}
\begin{tabularx}{0.98\textwidth}{l|c|cccc|cccc|cccc}
\toprule
\multicolumn{2}{c|}{Dataset} & \multicolumn{4}{c|}{Movies} & \multicolumn{4}{c|}{Toys} & \multicolumn{4}{c}{Sports} \\
\midrule
 Backbone & Method & N@10 & M@10 & N@20 & M@20 & N@10 & M@10 & N@20 & M@20 & N@10 & M@10 & N@20 & M@20 \\
\midrule
\multirow{10}{*}{\textbf{SASRec}} 
& Base   
& 0.0338 & 0.0238 & 0.0429 & 0.0263
& 0.0255 & 0.0191 & 0.0321 & 0.0210 
& 0.0073 & 0.0049 & 0.0101 & 0.0057 
\\
& MoRec 
& 0.0154 & 0.0105 & 0.0205 & 0.0119 
& 0.0114 & 0.0069 & 0.0146 & 0.0078 
& 0.0098 & 0.0074 & 0.0109 & 0.0077 
\\
& UniSRec 
& 0.0232 & 0.0160 & 0.0303 & 0.0179 
& 0.0271 & 0.0191 & 0.0311 & 0.0202 
& 0.0071 & 0.0051 & 0.0084 & 0.0055
\\
& WhitenRec 
& 0.0168 & 0.0116 & 0.0223 & 0.0131
& 0.0258 & 0.0181 & 0.0304 & 0.0194 
& \underline{0.0115} & \underline{0.0081} & \underline{0.0141} & \underline{0.0088} 
\\
& RLMRec-Con 
& 0.0346 & 0.0244 & 0.0441 & 0.0269
& 0.0266 & 0.0185 & 0.0304 & 0.0195 
& 0.0089 & 0.0058 & 0.0107 & 0.0063
\\
& RLMRec-Gen 
& 0.0355 & 0.0252 & 0.0449 & 0.0278
& \underline{0.0303} & \underline{0.0246} & \underline{0.0347} & \underline{0.0257}
& 0.0080 & 0.0054 & 0.0102 & 0.0060 
\\
& LLMInit 
& \underline{0.0370} & \underline{0.0264} & \underline{0.0470} & \underline{0.0291}
& 0.0275 & 0.0215 & 0.0313 & 0.0225 
& 0.0083 & 0.0055 & 0.0102 & 0.0060 
\\
& LLM-ESR 
& 0.0139 & 0.0094 & 0.0192 & 0.0108
& 0.0122 & 0.0104 & 0.0153 & 0.0112 
& 0.0101 & 0.0075 & 0.0118 & 0.0079 
\\
% \rowcolor{blue!10}
& \cellcolor{blue!10}AlphaFuse
& \cellcolor{blue!10}\textbf{0.0459}
& \cellcolor{blue!10}\textbf{0.0324}
& \cellcolor{blue!10}\textbf{0.0574}
& \cellcolor{blue!10}\textbf{0.0355}
& \cellcolor{blue!10}\textbf{0.0339}
& \cellcolor{blue!10}\textbf{0.0287}
& \cellcolor{blue!10}\textbf{0.0376}
& \cellcolor{blue!10}\textbf{0.0297}
& \cellcolor{blue!10}\textbf{0.0137}
& \cellcolor{blue!10}\textbf{0.0098}
& \cellcolor{blue!10}\textbf{0.0158}
& \cellcolor{blue!10}\textbf{0.0104}
\\
% \rowcolor{green!10} 
& Best Impr. & 
\cellcolor{green!10}\textbf{+24.05\%} & \cellcolor{green!10}\textbf{+22.73\%} & 
\cellcolor{green!10}\textbf{+22.13\%} & 
\cellcolor{green!10}\textbf{+21.99\%} & 
\cellcolor{green!10}\textbf{+11.88\%} & \cellcolor{green!10}\textbf{+16.67\%} & 
\cellcolor{green!10}\textbf{+8.36\%} & 
\cellcolor{green!10}\textbf{+15.56\%} &
\cellcolor{green!10}\textbf{+19.13\%} & \cellcolor{green!10}\textbf{+20.99\%} & 
\cellcolor{green!10}\textbf{+12.06\%} & 
\cellcolor{green!10}\textbf{+18.18\%} \\
\midrule
\multirow{11}{*}{\textbf{DreamRec}} 
& Base 
& 0.0016 & 0.0013 & 0.0018 & 0.0014 
&  \underline{0.0383} &  \underline{0.0333}
&  \underline{0.0392} &  \underline{0.0336}
&  \underline{0.0158} &  \underline{0.0132} 
&  \underline{0.0170} &  \underline{0.0135} 
\\
& iDreamRec 
& \underline{0.0226} & \underline{0.0180}
& \underline{0.0262} & \underline{0.0189}
& 0.0350 & 0.0301 & 0.0373 & 0.0307
& 0.0141 & 0.0119 & 0.0155 & 0.0123
\\
& MoRec 
& 0.0002 & 0.0002 & 0.0003 & 0.0002
& 0.0030 & 0.0026 & 0.0034 & 0.0027 
& 0.0012 & 0.0010 & 0.0017 & 0.0012 
\\
& UniSRec 
& 0.0021 & 0.0014 & 0.0030 &  0.0017
& 0.0014 & 0.0008 & 0.0022 & 0.0010 
& 0.0004 & 0.0002 & 0.0008 & 0.0003
\\
& WhitenRec 
& 0.0007 & 0.0006 & 0.0008 & 0.0006  
& 0.0029 & 0.0021 & 0.0034 & 0.0022 
& 0.0026 & 0.0019 & 0.0030 & 0.0021
\\
& RLMRec
& 0.0016 & 0.0013 & 0.0019 & 0.0014
& 0.0376 & 0.0321 & 0.0388 & 0.0325
& \underline{0.0160} & \underline{0.0135}
& \underline{0.0172} & \underline{0.0138}
\\
& LLMInit 
& 0.0082 & 0.0056 & 0.0113 & 0.0065 
& 0.0198 & 0.0179 & 0.0214 & 0.0184
& 0.0075 & 0.0065 & 0.0086 & 0.0068 
\\
& LLM-ESR 
& 0.0007 & 0.0004 & 0.0010 & 0.0005
& 0.0073 & 0.0061 & 0.0090 & 0.0066
& 0.0045 & 0.0037 & 0.0048 & 0.0037 
\\
& \cellcolor{blue!10}AlphaFuse
& \cellcolor{blue!10}\textbf{0.0246}
& \cellcolor{blue!10}\textbf{0.0201}
& \cellcolor{blue!10}\textbf{0.0279}
& \cellcolor{blue!10}\textbf{0.0209}
& \cellcolor{blue!10}\textbf{0.0408}
& \cellcolor{blue!10}\textbf{0.0348}
& \cellcolor{blue!10}\textbf{0.0425}
& \cellcolor{blue!10}\textbf{0.0353}
& \cellcolor{blue!10}\textbf{0.0165}
& \cellcolor{blue!10}\textbf{0.0139}
& \cellcolor{blue!10}\textbf{0.0174}
& \cellcolor{blue!10}\textbf{0.0142}
\\
& Best Impr. 
& \cellcolor{green!10}\textbf{+8.85\%} & \cellcolor{green!10}\textbf{+11.67\%}
& \cellcolor{green!10}\textbf{+6.49\%} & \cellcolor{green!10}\textbf{+10.58\%}
& \cellcolor{green!10}\textbf{+6.53\%} & \cellcolor{green!10}\textbf{+4.50\%}
& \cellcolor{green!10}\textbf{+8.42\%} & \cellcolor{green!10}\textbf{+5.06\%}
& \cellcolor{green!10}\textbf{+3.13\%} & \cellcolor{green!10}\textbf{+2.96\%}
& \cellcolor{green!10}\textbf{+1.16\%} & \cellcolor{green!10}\textbf{+2.90\%}
\\
\bottomrule
\end{tabularx}
\label{tab:cold-start}
\end{table*}
```

## Table 3
```latex
\begin{table*}[ht!]
\centering
\caption{Performance comparison across different methods on three datasets with long-tail settings. }
\vspace{-5pt}
\begin{tabularx}{0.98\textwidth}{cl|cc|cccc|cccc}
\toprule
\multirow{2}{*}{\textbf{Dataset}} & \multirow{2}{*}{\textbf{Model}} & \multicolumn{2}{c|}{\textbf{Overall}} & \multicolumn{2}{c}{\textbf{Tail Item}} & \multicolumn{2}{c|}{\textbf{Head Item}} & \multicolumn{2}{c}{\textbf{Tail User}} & \multicolumn{2}{c}{\textbf{Head User}} \\
\cmidrule{3-12}
  & & R@10 & N@10 & R@10 & N@10 & R@10 & N@10 & R@10 & N@10 & R@10 & N@10  \\
\midrule
\multirow{4}{*}{\textbf{Yelp}} 
& SASRec &
 0.5940 & 0.3597 &
 0.1142 & 0.0495 & 0.7353 & 0.4511 &
 0.5893 & 0.3578 & 0.6122 & 0.3672 \\
& -LLM-ESR &
 \textbf{0.6673} & 0.4208 &
 \textbf{0.1893} & \textbf{0.0845} & \textbf{0.8080} & 0.5199 &
 \textbf{0.6685} & 0.4229 & \textbf{0.6627} & 0.4128 \\
&\cellcolor{blue!10}-\textbf{AlphaFuse}
& \cellcolor{blue!10}0.6631
&\cellcolor{blue!10}\textbf{0.4219}
&\cellcolor{blue!10} 0.1815
& \cellcolor{blue!10}0.0775
& \cellcolor{blue!10}0.8048
& \cellcolor{blue!10}\textbf{0.5232}
& \cellcolor{blue!10}0.6617
& \cellcolor{blue!10}\textbf{0.4239}
& \cellcolor{blue!10}0.6585
& \cellcolor{blue!10}\textbf{0.4141}
\\
& Best Impr. & 
 \cellcolor{red!10}-0.63\% & \cellcolor{green!10}\textbf{+0.26\%} & 
 \cellcolor{red!10}-4.12\% & \cellcolor{red!10}-8.28\% & \cellcolor{red!10}-0.40\% & \cellcolor{green!10}\textbf{+0.63\%} & \cellcolor{red!10}-1.02\% & \cellcolor{green!10}\textbf{+0.24\%} & \cellcolor{red!10}-0.63\% & \cellcolor{green!10}\textbf{+0.31\%} \\
\midrule
\multirow{4}{*}{\textbf{Fashion}} 
& SASRec &
 0.4956 & 0.4429 &
 0.0454 & 0.0235 & 0.6748 & 0.6099 &
 0.3967 & 0.3390 & 0.6239 & 0.5777 \\
& -LLM-ESR &
 0.5619 & 0.4743 &
 0.1095 & 0.0520 & \textbf{0.7420} & 0.6424 &
 0.4811 & 0.3769 & 0.6668 & 0.6005 \\
& \cellcolor{blue!10}-\textbf{AlphaFuse}
& \cellcolor{blue!10}\textbf{0.6008}
& \cellcolor{blue!10}\textbf{0.5103}
& \cellcolor{blue!10}\textbf{0.2601}
& \cellcolor{blue!10}\textbf{0.1646}
&\cellcolor{blue!10} 0.7364
& \cellcolor{blue!10}\textbf{0.6479}
& \cellcolor{blue!10}\textbf{0.5352}
& \cellcolor{blue!10}\textbf{0.4276}
& \cellcolor{blue!10}\textbf{0.6860}
& \cellcolor{blue!10}\textbf{0.6175}
\\
& Best Impr. & 
 \cellcolor{green!10}\textbf{+6.92\%} & \cellcolor{green!10}\textbf{+7.59\%} & \cellcolor{green!10}\textbf{+137.53\%} & \cellcolor{green!10}\textbf{+216.54\%} & 
 \cellcolor{red!10}-0.75\% & \cellcolor{green!10}\textbf{+0.86\%} & \cellcolor{green!10}\textbf{+11.25\%} & \cellcolor{green!10}\textbf{+13.45\%}& \cellcolor{green!10}\textbf{+2.88\%} & \cellcolor{green!10}\textbf{+2.83\%} \\
\midrule
\multirow{4}{*}{\textbf{Beauty}} 
& SASRec &
 0.4388 & 0.3030 &
 0.0870 & 0.0649 & 0.5227 & 0.3598 &
 0.4270 & 0.2941 & 0.4926 & 0.3438 \\
& -LLM-ESR &
 0.5672 & 0.3713 & 
 \textbf{0.2257} & \textbf{0.1108} & 0.6486 & 0.4334 &
 0.5581 & 0.3643 & 0.6087 & 0.4032 \\
& \cellcolor{blue!10}{-\textbf{AlphaFuse}} 
& \cellcolor{blue!10}{\textbf{0.5793}}
& \cellcolor{blue!10}{\textbf{0.4046}}
& \cellcolor{blue!10}{0.1625}
& \cellcolor{blue!10}{0.1006}
& \cellcolor{blue!10}\textbf{0.6787}
& \cellcolor{blue!10}\textbf{0.4771}
& \cellcolor{blue!10}\textbf{0.5692}
& \cellcolor{blue!10}\textbf{0.3984}
& \cellcolor{blue!10}\textbf{0.6258}
& \cellcolor{blue!10}\textbf{0.4326}
\\
& Best Impr. & 
\cellcolor{green!10}\textbf{+2.13\%} & 
\cellcolor{green!10}\textbf{+8.97\%} & 
 \cellcolor{red!10}-28.00\% &  \cellcolor{red!10}-9.21\% & \cellcolor{red!10}\textbf{-4.64\%} & 
\cellcolor{green!10}\textbf{+10.08\%} & 
\cellcolor{green!10}\textbf{+1.99\%} & 
\cellcolor{green!10}\textbf{+9.36\%} & 
\cellcolor{green!10}\textbf{+2.81\%}& 
\cellcolor{green!10}\textbf{+7.29\%}\\
\bottomrule
\end{tabularx}
\label{tab:long-tail}
\end{table*}
```

## Table 4
```latex
\begin{table}[t!]
\centering
\caption{The ablation study with SASRec as the backbone.}
\vspace{-5pt}
\begin{tabularx}{0.47\textwidth}{cl|cccc}
\toprule
\multirow{2}{*}{\textbf{Dataset}} & \multirow{2}{*}{\textbf{Model}} & \multicolumn{4}{c}{\textbf{SASRec Backbone}} \\
\cmidrule{3-6}
  & & N@10 & M@10 & N@20 & M@20\\
\midrule

\multirow{4}{*}{\textbf{Movies}}
& \cellcolor{blue!10}\textbf{AlphaFuse}
& \cellcolor{blue!10}0.0459
& \cellcolor{blue!10}0.0324 
& \cellcolor{blue!10}0.0574 
& \cellcolor{blue!10} 0.0355 \\
& \cellcolor{red!10}-w/o Frozen. 
& \cellcolor{red!10} 0.0350
& \cellcolor{red!10} 0.0249
& \cellcolor{red!10} 0.0444
& \cellcolor{red!10} 0.0274 \\
& \cellcolor{red!10}-w/o Clip.
& \cellcolor{red!10} 0.0148  
& \cellcolor{red!10} 0.0096  
& \cellcolor{red!10} 0.0197
& \cellcolor{red!10} 0.0109
\\
& \cellcolor{red!10}-w/o Stand. 
&  \cellcolor{red!10}0.0354
&  \cellcolor{red!10}0.0250
&  \cellcolor{red!10}0.0450
&  \cellcolor{red!10}0.0276\\
\bottomrule
\end{tabularx}
\label{tab:SASRec_abla}
\vspace{-8pt}
\end{table}
```

## Table 5
```latex
\begin{table}[t!]
\centering
\caption{The ablation study with DreamRec as the backbone.}
\vspace{-5pt}
\begin{tabularx}{0.47\textwidth}{cl|cccc}
\toprule
\multirow{2}{*}{\textbf{Dataset}} & \multirow{2}{*}{\textbf{Model}} & \multicolumn{4}{c}{\textbf{DreamRec Backbone}} \\
\cmidrule{3-6}
  & & N@10 & M@10 & N@20 & M@20\\
\midrule 
\multirow{4}{*}{\textbf{Movies}}
& \cellcolor{blue!10}\textbf{AlphaFuse}
& \cellcolor{blue!10}0.0246
& \cellcolor{blue!10}0.0201
& \cellcolor{blue!10}0.0279
& \cellcolor{blue!10}0.0209 \\
& \cellcolor{red!10}-w/o Decom. 
& \cellcolor{red!10}0.0103
& \cellcolor{red!10}0.0084
& \cellcolor{red!10}0.0120
& \cellcolor{red!10}0.0089
\\
& \cellcolor{red!10}-w/o Frozen.
& \cellcolor{red!10}0.0214
& \cellcolor{red!10}0.0177
& \cellcolor{red!10}0.0242
& \cellcolor{red!10}0.0185
\\
& \cellcolor{red!10}-w/o Stand. 
& \cellcolor{red!10}0.0114 
& \cellcolor{red!10}0.0089
& \cellcolor{red!10}0.0140
& \cellcolor{red!10}0.0095
\\
\bottomrule
\end{tabularx}
\vspace{-5pt}
\label{tab:DreamRec_abla}
\end{table}
```

## Table 6
```latex
\begin{table}[t]
\caption{Comparison of efficiency through the number of trainable parameters and GFLOPs during inference.}
\label{tab:efficiency}
\centering
% \scriptsize
\vspace{-5pt}
\begin{tabular}{lcc}
\toprule 
Models &  \# Trainable Parameters & Inference GFLOPs \\
\midrule
UniSRec   & 1.69M &  4.24  \\
LLM-ESR   & 4.10M &  3.34  \\
MoRec     & 0.28M &  0.72  \\
WhitenRec & 0.28M &  0.72  \\
RLMRec    & 7.10M &  0.22  \\
LLMInit   & 5.72M &  0.22  \\
SASRec    & 5.72M &  0.22  \\
\cellcolor{blue!10}AlphaFuse & \cellcolor{blue!10}2.90M &  \cellcolor{blue!10}0.22  \\
\midrule
\end{tabular}
\end{table}
```

