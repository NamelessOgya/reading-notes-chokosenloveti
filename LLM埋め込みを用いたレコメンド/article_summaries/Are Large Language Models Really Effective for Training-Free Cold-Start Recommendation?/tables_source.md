# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
  \centering
  \caption{Classification of recommendation settings. The taxonomy is defined by whether the model is trained and by the number of interactions of target users $m$.}
  \label{tab:taxonomy}
  \setlength{\tabcolsep}{6pt}
  \begin{tabular}{@{}c|l p{0.65\textwidth} l@{}}
    \toprule
     & \textbf{Size $m$} & \textbf{Description} & \textbf{References} \\
    \midrule
    \multirow[c]{3}{*}{\rotatebox{90}{Need Training}}  
      & Rich & The model is trained with sufficient data from many users, and the target user also has rich interactions. \colorbox{blue!10}{This is a major research focus in recommender systems.} &~\cite{DBLP:conf/sigir/light_gcn_0001DWLZ020,DBLP:conf/www/ncf_HeLZNHC17,DBLP:conf/cikm/bert4rec_SunLWPLOJ19,DBLP:conf/naacl/WangL24_demo} \\ \cmidrule{2-4} 
      & A few & The model is trained, while the target user has only a few interactions (broad cold-start). &~\cite{DBLP:conf/www/tanp_csr_Lin00PCW21,DBLP:conf/www/coldnas_csr_WuWJDDY23} \\ \cmidrule{2-4} 
      & Zero & The model is trained, but the target user has no interactions and only profile information (narrow cold-start). &~\cite{DBLP:conf/cikm/zs_csr_FengPZCL21,DBLP:conf/aaai/zsl_csr_LiJL00H19,DBLP:conf/nips/dropout_VolkovsYP17} \\
    \midrule
     \multirow[c]{3}{*}{\rotatebox{90}{Training-free}} 
      & Rich & No training is performed; recommendations rely only on the target user's own rich interactions. &~\cite{DBLP:conf/recsys/llm_rec_listwise_DaiSZYSXS0X23,DBLP:conf/ecir/llm_rec_sort_HouZLLXMZ24,DBLP:journals/corr/23_is_chatgpt,tois2023_llmrec_Tang2023OneMF} \\ \cmidrule{2-4} 
      & A few & No training is performed; the target user has only a few interactions (broad cold-start). &~\cite{DBLP:conf/cikm/llm_zsr_HeXJSLFMKM23,DBLP:journals/tors/csr_bandit_SilvaSWRP23} \\ \cmidrule{2-4} 
      & Zero & No training is performed; the target user has no interactions and only profile information (narrow cold-start). \colorbox{red!15}{This is the primary focus of our study.} & - \\
    \bottomrule
  \end{tabular}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
\centering
\caption{Recall@10 and nDCG@10 in the narrow cold-start setting. Statistical significance is evaluated using the one-sided Wilcoxon signed-rank test against \texttt{BM25}; $*$ and $\bigtriangledown$ indicate results significantly higher or lower at $p=10^{-4}$.}
\label{tab:overall_results_profile}
\setlength{\tabcolsep}{4pt}
\scalebox{0.83}{
\begin{tabular}{l|cccccc|cc}
\toprule
 & \multicolumn{2}{c}{ML-1M} & \multicolumn{2}{c}{Job (no exp)} & \multicolumn{2}{c}{Job (exp)} & \multicolumn{2}{|c}{All} \\
 & Recall & nDCG & Recall & nDCG & Recall & nDCG & Recall & nDCG \\
\midrule
\texttt{BM25} & $0.202$ & $0.235$ & $0.321$ & $0.373$ & $0.423$ & $0.476$ & $0.315$ & $0.362$ \\ \midrule
\texttt{gte-modernbert-base} & \cellcolor{pslow}$0.221$ & \cellcolor{pslow}$0.251$ & \cellcolor{nhigh}$0.219^{\bigtriangledown}$ & \cellcolor{nhigh}$0.230^{\bigtriangledown}$ & \cellcolor{nhigh}$0.222^{\bigtriangledown}$ & \cellcolor{nhigh}$0.244^{\bigtriangledown}$ & \cellcolor{nmiddle}$0.221^{\bigtriangledown}$ & \cellcolor{nhigh}$0.242^{\bigtriangledown}$ \\
\texttt{multilingual-e5-large} & \cellcolor{plow}$0.223$ & \cellcolor{plow}$0.260$ & \cellcolor{pslow}$0.343$ & $0.381$ & \cellcolor{nmiddle}$0.335^{\bigtriangledown}$ & \cellcolor{nmiddle}$0.376^{\bigtriangledown}$ & $0.300$ & \cellcolor{nslow}$0.339$ \\
\texttt{bge-m3} & \cellcolor{pslow}$0.220$ & \cellcolor{pslow}$0.249$ & $0.307$ & $0.373$ & \cellcolor{nlow}$0.353^{\bigtriangledown}$ & \cellcolor{nmiddle}$0.371^{\bigtriangledown}$ & \cellcolor{nslow}$0.293$ & \cellcolor{nslow}$0.331$ \\
\texttt{gte-Qwen2-1.5B-instruct} & \cellcolor{plow}$0.233$ & \cellcolor{plow}$0.267$ & \cellcolor{plow}$0.361$ & \cellcolor{pslow}$0.402$ & $0.427$ & $0.462$ & \cellcolor{pslow}$0.340$ & $0.377$ \\
\texttt{gte-Qwen2-7B-instruct} & \cellcolor{pslow}$0.222$ & \cellcolor{pslow}$0.255$ & \cellcolor{plow}$0.382^{*}$ & \cellcolor{plow}$0.440$ & \cellcolor{pmiddle}$0.511^{*}$ & \cellcolor{plow}$0.540^{*}$ & \cellcolor{plow}$0.372^{*}$ & \cellcolor{plow}$0.412^{*}$ \\
\texttt{Qwen3-Embedding-0.6B} & \cellcolor{plow}$0.223$ & \cellcolor{plow}$0.260$ & \cellcolor{pmiddle}$0.397^{*}$ & \cellcolor{plow}$0.439$ & \cellcolor{pslow}$0.465$ & \cellcolor{pslow}$0.503$ & \cellcolor{plow}$0.362^{*}$ & \cellcolor{plow}$0.401$ \\
\texttt{Qwen3-Embedding-8B} & \cellcolor{pmiddle}$0.247$ & \cellcolor{plow}$\textbf{0.273}$ & \cellcolor{pmiddle}$\textbf{0.408}^{*}$ & \cellcolor{pmiddle}$\textbf{0.459}^{*}$ & \cellcolor{pmiddle}$\textbf{0.521}^{*}$ & \cellcolor{plow}$\textbf{0.557}^{*}$ & \cellcolor{pmiddle}$\textbf{0.392}^{*}$ & \cellcolor{plow}$\textbf{0.430}^{*}$ \\ \midrule
\texttt{gpt-4.1-mini} & \cellcolor{pslow}$0.218$ & \cellcolor{nlow}$0.207$ & \cellcolor{nlow}$0.273$ & \cellcolor{nhigh}$0.245^{\bigtriangledown}$ & \cellcolor{nlow}$0.355$ & \cellcolor{nhigh}$0.327^{\bigtriangledown}$ & \cellcolor{nlow}$0.282$ & \cellcolor{nmiddle}$0.260^{\bigtriangledown}$ \\ 
\texttt{gpt-4.1} & \cellcolor{phigh}$\textbf{0.269}^{*}$ & \cellcolor{pslow}$0.247$ & \cellcolor{nlow}$0.283$ & \cellcolor{nhigh}$0.258^{\bigtriangledown}$ & \cellcolor{nslow}$0.381$ & \cellcolor{nmiddle}$0.343^{\bigtriangledown}$ & $0.311$ & \cellcolor{nmiddle}$0.283^{\bigtriangledown}$ \\
\texttt{Qwen/Qwen3-8B} & \cellcolor{nslow}$0.187$ & \cellcolor{nmiddle}$0.165^{\bigtriangledown}$ & \cellcolor{nshigh}$0.061^{\bigtriangledown}$ & \cellcolor{nshigh}$0.057^{\bigtriangledown}$ & \cellcolor{nshigh}$0.092^{\bigtriangledown}$ & \cellcolor{nshigh}$0.080^{\bigtriangledown}$ & \cellcolor{nshigh}$0.114^{\bigtriangledown}$ & \cellcolor{nshigh}$0.101^{\bigtriangledown}$ \\
\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 3
```latex
\begin{table*}[t]
\centering
\caption{Recall@10 and nDCG@10 for the broad cold-start setting with $m=1$.}
\label{tab:overall_results_1-shot}
\setlength{\tabcolsep}{4pt}
\scalebox{0.61}{
\begin{tabular}{l|cccccccccc|cc}
\toprule
 & \multicolumn{2}{c}{ML-1M} & \multicolumn{2}{c}{Job} & \multicolumn{2}{c}{Music} & \multicolumn{2}{c}{Movie} & \multicolumn{2}{c}{Books} & \multicolumn{2}{|c}{All} \\
 & Recall & nDCG & Recall & nDCG & Recall & nDCG & Recall & nDCG & Recall & nDCG & Recall & nDCG  \\
 \midrule
\texttt{BM25} & $0.388$ & $0.423$ & $0.414$ & $0.475$ & $0.345$ & $0.457$ & $0.367$ & $0.442$ & $0.473$ & $0.590$ & $0.397$ & $0.477$ \\ \midrule
\texttt{gte-modernbert-base} & \cellcolor{pslow}$0.426$ & \cellcolor{pslow}$0.446$ & \cellcolor{nlow}$0.371$ & \cellcolor{nslow}$0.441$ & \cellcolor{phigh}$0.498^{*}$ & \cellcolor{pmiddle}$0.561^{*}$ & \cellcolor{pmiddle}$0.456^{*}$ & \cellcolor{plow}$0.519^{*}$ & \cellcolor{plow}$0.557^{*}$ & \cellcolor{pslow}$0.628$ & \cellcolor{plow}$0.462^{*}$ & \cellcolor{pslow}$0.519^{*}$ \\
\texttt{multilingual-e5-large} & \cellcolor{plow}$0.436$ & $0.439$ & \cellcolor{nlow}$0.337^{\bigtriangledown}$ & \cellcolor{nlow}$0.393^{\bigtriangledown}$ & \cellcolor{phigh}$0.464^{*}$ & \cellcolor{plow}$0.543^{*}$ & \cellcolor{plow}$0.439^{*}$ & \cellcolor{plow}$0.488$ & \cellcolor{plow}$0.546^{*}$ & \cellcolor{pslow}$0.631$ & \cellcolor{plow}$0.444^{*}$ & $0.499$ \\
\texttt{bge-m3} & \cellcolor{plow}$0.439$ & $0.442$ & $0.417$ & $0.476$ & \cellcolor{pmiddle}$0.429^{*}$ & \cellcolor{plow}$0.505$ & \cellcolor{plow}$0.423^{*}$ & \cellcolor{plow}$0.491$ & \cellcolor{plow}$0.541^{*}$ & $0.616$ & \cellcolor{plow}$0.449^{*}$ & \cellcolor{pslow}$0.506^{*}$ \\
\texttt{gte-Qwen2-1.5B-instruct} & \cellcolor{plow}$0.459^{*}$ & \cellcolor{plow}$0.473$ & \cellcolor{plow}$0.471^{*}$ & \cellcolor{pslow}$0.517$ & \cellcolor{pshigh}$0.532^{*}$ & \cellcolor{pmiddle}$0.581^{*}$ & \cellcolor{phigh}$0.482^{*}$ & \cellcolor{pmiddle}$0.554^{*}$ & \cellcolor{pmiddle}$0.575^{*}$ & \cellcolor{plow}$0.655^{*}$ & \cellcolor{pmiddle}$0.504^{*}$ & \cellcolor{plow}$0.556^{*}$ \\
\texttt{gte-Qwen2-7B-instruct} & \cellcolor{plow}$0.465^{*}$ & \cellcolor{plow}$0.467$ & \cellcolor{pmiddle}$\textbf{0.511}^{*}$ & \cellcolor{plow}$\textbf{0.554}^{*}$ & \cellcolor{pshigh}$0.535^{*}$ & \cellcolor{phigh}$\textbf{0.604}^{*}$ & \cellcolor{pshigh}$\textbf{0.560}^{*}$ & \cellcolor{phigh}$\textbf{0.598}^{*}$ & \cellcolor{pmiddle}$\textbf{0.609}^{*}$ & \cellcolor{plow}$\textbf{0.683}^{*}$ & \cellcolor{phigh}$\textbf{0.536}^{*}$ & \cellcolor{pmiddle}$\textbf{0.581}^{*}$ \\
\texttt{Qwen3-Embedding-0.6B} & \cellcolor{plow}$\textbf{0.465}^{*}$ & \cellcolor{plow}$0.473$ & \cellcolor{plow}$0.458$ & \cellcolor{pslow}$0.515$ & \cellcolor{pmiddle}$0.445^{*}$ & \cellcolor{plow}$0.523^{*}$ & \cellcolor{pmiddle}$0.447^{*}$ & \cellcolor{plow}$0.515^{*}$ & \cellcolor{plow}$0.553^{*}$ & \cellcolor{pslow}$0.625$ & \cellcolor{plow}$0.474^{*}$ & \cellcolor{plow}$0.530^{*}$ \\
\texttt{Qwen3-Embedding-8B} & \cellcolor{plow}$0.465^{*}$ & \cellcolor{plow}$\textbf{0.477}$ & \cellcolor{plow}$0.475^{*}$ & \cellcolor{plow}$0.533$ & \cellcolor{pshigh}$\textbf{0.535}^{*}$ & \cellcolor{phigh}$0.604^{*}$ & \cellcolor{phigh}$0.509^{*}$ & \cellcolor{phigh}$0.578^{*}$ & \cellcolor{pmiddle}$0.587^{*}$ & \cellcolor{plow}$0.652$ & \cellcolor{pmiddle}$0.514^{*}$ & \cellcolor{plow}$0.569^{*}$ \\ \midrule
\texttt{gpt-4.1-mini} & \cellcolor{nlow}$0.339$ & \cellcolor{nhigh}$0.289^{\bigtriangledown}$ & \cellcolor{nhigh}$0.272^{\bigtriangledown}$ & \cellcolor{nhigh}$0.264^{\bigtriangledown}$ & \cellcolor{plow}$0.405^{*}$ & \cellcolor{nmiddle}$0.365^{\bigtriangledown}$ & \cellcolor{nlow}$0.323$ & \cellcolor{nmiddle}$0.311^{\bigtriangledown}$ & $0.487$ & \cellcolor{nmiddle}$0.427^{\bigtriangledown}$ & \cellcolor{nslow}$0.365$ & \cellcolor{nhigh}$0.331^{\bigtriangledown}$ \\
\texttt{gpt-4.1} & $0.391$ & \cellcolor{nmiddle}$0.336^{\bigtriangledown}$ & \cellcolor{nlow}$0.363$ & \cellcolor{nhigh}$0.328^{\bigtriangledown}$ & \cellcolor{phigh}$0.453^{*}$ & \cellcolor{nlow}$0.396$ & \cellcolor{pslow}$0.399$ & \cellcolor{nlow}$0.357^{\bigtriangledown}$ & \cellcolor{plow}$0.556^{*}$ & \cellcolor{nmiddle}$0.470^{\bigtriangledown}$ & \cellcolor{pslow}$0.433^{*}$ & \cellcolor{nmiddle}$0.377^{\bigtriangledown}$ \\
\texttt{Qwen/Qwen3-8B} & \cellcolor{nmiddle}$0.295^{\bigtriangledown}$ & \cellcolor{nhigh}$0.251^{\bigtriangledown}$ & \cellcolor{nshigh}$0.085^{\bigtriangledown}$ & \cellcolor{nshigh}$0.085^{\bigtriangledown}$ & \cellcolor{nhigh}$0.203^{\bigtriangledown}$ & \cellcolor{nshigh}$0.197^{\bigtriangledown}$ & \cellcolor{nshigh}$0.175^{\bigtriangledown}$ & \cellcolor{nshigh}$0.170^{\bigtriangledown}$ & \cellcolor{nhigh}$0.266^{\bigtriangledown}$ & \cellcolor{nshigh}$0.254^{\bigtriangledown}$ & \cellcolor{nhigh}$0.205^{\bigtriangledown}$ & \cellcolor{nshigh}$0.191^{\bigtriangledown}$ \\
\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 4
```latex
\begin{table*}[t]
\centering
\caption{Recall@10 and nDCG@10 in the cross-domain setting with $m'=1$. ``Music $\rightarrow$ Movie'' indicates that the source domain (user behaviors) is Music and the target domain (candidate items) is Movie.}
\label{tab:cross-domain-1}
\setlength{\tabcolsep}{4pt}
\scalebox{0.7}{
\begin{tabular}{l|cccccccc|cc}
\toprule
 & \multicolumn{2}{c}{Music $\rightarrow$ Movie} & \multicolumn{2}{c}{Movie $\rightarrow$ Music} & \multicolumn{2}{c}{Books $\rightarrow$ Movie} & \multicolumn{2}{c}{Movie $\rightarrow$ Books} & \multicolumn{2}{|c}{All}  \\
 & Recall & nDCG & Recall & nDCG & Recall & nDCG & Recall & nDCG & Recall & nDCG \\
\midrule
\texttt{BM25} & $0.249$ & $0.308$ & $0.175$ & $0.214$ & $0.238$ & $0.282$ & $0.197$ & $0.232$ & $0.215$ & $0.259$ \\ \midrule
\texttt{gte-modernbert-base} & \cellcolor{phigh}$0.327^{*}$ & \cellcolor{pmiddle}$0.380$ & \cellcolor{pshigh}$0.307^{*}$ & \cellcolor{pshigh}$0.349^{*}$ & \cellcolor{plow}$0.277$ & \cellcolor{plow}$0.313$ & \cellcolor{phigh}$0.293^{*}$ & \cellcolor{phigh}$0.323^{*}$ & \cellcolor{phigh}$0.301^{*}$ & \cellcolor{phigh}$0.341^{*}$ \\
\texttt{multilingual-e5-large} & \cellcolor{phigh}$0.325^{*}$ & \cellcolor{plow}$0.358$ & \cellcolor{pshigh}$0.267^{*}$ & \cellcolor{phigh}$0.311^{*}$ & \cellcolor{pmiddle}$0.305^{*}$ & \cellcolor{plow}$0.331$ & \cellcolor{phigh}$0.258^{*}$ & \cellcolor{pmiddle}$0.287$ & \cellcolor{phigh}$0.289^{*}$ & \cellcolor{pmiddle}$0.322^{*}$ \\
\texttt{bge-m3} & \cellcolor{plow}$0.293$ & \cellcolor{plow}$0.342$ & \cellcolor{phigh}$0.241^{*}$ & \cellcolor{phigh}$0.283^{*}$ & \cellcolor{plow}$0.266$ & \cellcolor{plow}$0.314$ & \cellcolor{phigh}$0.261^{*}$ & \cellcolor{pmiddle}$0.285$ & \cellcolor{pmiddle}$0.265^{*}$ & \cellcolor{plow}$0.306^{*}$ \\
\texttt{gte-Qwen2-1.5B-instruct} & \cellcolor{phigh}$0.345^{*}$ & \cellcolor{pmiddle}$0.388^{*}$ & \cellcolor{pshigh}$0.331^{*}$ & \cellcolor{pshigh}$\textbf{0.369}^{*}$ & \cellcolor{phigh}$0.351^{*}$ & \cellcolor{phigh}$0.393^{*}$ & \cellcolor{phigh}$0.291^{*}$ & \cellcolor{phigh}$0.310^{*}$ & \cellcolor{pshigh}$0.330^{*}$ & \cellcolor{phigh}$0.365^{*}$ \\
\texttt{gte-Qwen2-7B-instruct} & \cellcolor{pshigh}$\textbf{0.416}^{*}$ & \cellcolor{phigh}$\textbf{0.456}^{*}$ & \cellcolor{pshigh}$\textbf{0.332}^{*}$ & \cellcolor{pshigh}$0.367^{*}$ & \cellcolor{pshigh}$\textbf{0.409}^{*}$ & \cellcolor{pshigh}$\textbf{0.435}^{*}$ & \cellcolor{pshigh}$\textbf{0.321}^{*}$ & \cellcolor{pshigh}$\textbf{0.348}^{*}$ & \cellcolor{pshigh}$\textbf{0.369}^{*}$ & \cellcolor{pshigh}$\textbf{0.402}^{*}$ \\
\texttt{Qwen3-Embedding-0.6B} & \cellcolor{phigh}$0.331^{*}$ & \cellcolor{pmiddle}$0.378$ & \cellcolor{phigh}$0.258^{*}$ & \cellcolor{phigh}$0.293^{*}$ & \cellcolor{phigh}$0.316^{*}$ & \cellcolor{pmiddle}$0.365^{*}$ & \cellcolor{pmiddle}$0.240$ & \cellcolor{pslow}$0.252$ & \cellcolor{phigh}$0.286^{*}$ & \cellcolor{pmiddle}$0.322^{*}$ \\
\texttt{Qwen3-Embedding-8B} & \cellcolor{pshigh}$0.403^{*}$ & \cellcolor{phigh}$0.445^{*}$ & \cellcolor{pshigh}$0.317^{*}$ & \cellcolor{pshigh}$0.349^{*}$ & \cellcolor{pshigh}$0.381^{*}$ & \cellcolor{pshigh}$0.426^{*}$ & \cellcolor{phigh}$0.285^{*}$ & \cellcolor{phigh}$0.311^{*}$ & \cellcolor{pshigh}$0.347^{*}$ & \cellcolor{phigh}$0.383^{*}$ \\ \midrule
\texttt{gpt-4.1-mini} & \cellcolor{nlow}$0.218$ & \cellcolor{nmiddle}$0.230^{\bigtriangledown}$ & \cellcolor{nslow}$0.165$ & \cellcolor{nhigh}$0.147^{\bigtriangledown}$ & \cellcolor{nslow}$0.217$ & \cellcolor{nmiddle}$0.210^{\bigtriangledown}$ & \cellcolor{nmiddle}$0.143$ & \cellcolor{nhigh}$0.122^{\bigtriangledown}$ & \cellcolor{nlow}$0.186$ & \cellcolor{nhigh}$0.177^{\bigtriangledown}$ \\
\texttt{gpt-4.1} & \cellcolor{pslow}$0.265$ & \cellcolor{nlow}$0.262$ & \cellcolor{plow}$0.209$ & \cellcolor{nlow}$0.192$ & \cellcolor{pmiddle}$0.302^{*}$ & $0.271$ & $0.199$ & \cellcolor{nmiddle}$0.171^{\bigtriangledown}$ & \cellcolor{plow}$0.244^{*}$ & \cellcolor{nlow}$0.224^{\bigtriangledown}$ \\
\texttt{Qwen3-8B} & \cellcolor{nshigh}$0.111^{\bigtriangledown}$ & \cellcolor{nshigh}$0.104^{\bigtriangledown}$ & \cellcolor{nshigh}$0.086^{\bigtriangledown}$ & \cellcolor{nshigh}$0.078^{\bigtriangledown}$ & \cellcolor{nhigh}$0.121^{\bigtriangledown}$ & \cellcolor{nshigh}$0.111^{\bigtriangledown}$ & \cellcolor{nshigh}$0.082^{\bigtriangledown}$ & \cellcolor{nshigh}$0.070^{\bigtriangledown}$ & \cellcolor{nshigh}$0.100^{\bigtriangledown}$ & \cellcolor{nshigh}$0.091^{\bigtriangledown}$ \\
\bottomrule
\end{tabular}
}
\end{table*}
```

