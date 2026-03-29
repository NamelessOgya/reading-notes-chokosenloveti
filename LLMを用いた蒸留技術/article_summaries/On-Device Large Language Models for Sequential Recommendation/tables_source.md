# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\centering
\small
\begin{tabular}{lccccc}
\hline
\textbf{Datasets} & \textbf{\#Users} & \textbf{\#Items} & \textbf{\#Inter} & \textbf{Sparsity} & \textbf{Avg. \textit{Length}} \\
\hline
Instruments & 24,773 & 9,923 & 206,153 & 99.92\% & 8.32 \\
Arts        & 45,142 & 20,957 & 390,832 & 99.96\% & 8.66 \\
Games       & 50,547 & 16,860 & 452,989 & 99.95\% & 8.96 \\
\hline
\end{tabular}
\caption{Important properties of the datasets used in our experiments.}
\label{table 1}
\vspace{-2em}
\end{table}
```

## Table 2
```latex
\begin{table*}[t]
	%\fontsize{9}{10}\selectfont
% 		\small
% 	\caption{Performances of all comparison methods on three datasets.}
	\begin{center}
		\setlength{\tabcolsep}{1mm}{
		{
		{
			\begin{tabular}{*{13}{c}}
				\toprule
				\multirow{2}{*}{Method} &
				\multicolumn{4}{c}{Instruments} & \multicolumn{4}{c}{Games} & \multicolumn{4}{c}{Arts}\cr
				\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13} & HR@5 & NDCG@5 & HR@10 & NDCG@10 & HR@5 & NDCG@5 & HR@10 & NDCG@10   & HR@5 & NDCG@5 & HR@10 & NDCG@10\\ \hline		
							
				Caser  & 0.0543  & 0.0355 &0.0710& 0.0409& 0.0367 &0.0227 &0.0617 &0.0307&0.0379 &0.0262& 0.0541& 0.0313  \\
				
				HGN &0.0813&0.0668& 0.1048&0.0744 &0.0517& 0.0333&0.0856&0.0442&0.0622&0.0462& 0.0875& 0.0544\\
				
				GRU4Rec&0.0821&0.0698&0.1031&0.0765&0.0586& 0.0381&0.0964&0.0502&0.0749&0.0590 &0.0964 & 0.0659\\
				
				Bert4Rec&0.0671&0.0560&0.0822&0.0608& 0.0482&0.0311 &0.0763&0.0401&0.0559&0.0451&0.0713     &0.0500\\
                   
                    FDSA&0.0834&0.0681&0.1046&0.0750&0.0644&0.0404& 0.1041&0.0531&0.0734&0.0595& 0.0933& 0.0660\\
				SASRec&0.0751&0.0627&0.0947&0.0690&0.0581 &0.0365 &0.0940&0.0481&0.0757 & 0.0508 &0.1016     & 0.0592\\
                S3-Rec&0.0863 &0.0626&0.1136& 0.0714&0.0606&0.0364&0.1002&0.0491&0.0767 & 0.0521& 0.1051& 0.0612\\
                TIGER&0.0863&0.0738&0.1064&0.0803&0.0599&0.0392 & 0.0939&0.0501&0.0788& 0.0631& 0.1012 & 0.0703\\
               % TinyLlaMa&      &     &    &      &     & &      &     &   &    &     & \\
               % Gemma-2b&      &     &    &      &     & &      &     &   &    &     & \\
                LC-Rec& \underline{0.0997}& \underline{0.0852}& 0.1217&0.0923 &\underline{0.0876}&0.0635 &0.1252&\underline{0.0757}& 0.1007& 0.0824& 0.1251& 0.0902\\
                OD-LLM&  0.0993& 0.0851 & \textbf{0.1219} &\textbf{0.0923} & 0.0838 &\textbf{0.0644}& \textbf{0.1264} & 0.0748& \textbf{0.1173} &\textbf{0.1000} & \textbf{0.1434} & \textbf{0.1084}\\\hline
                
    %                \textbf{OD-LLM}& \textbf{0.057}  &\textbf{0.045} 
    %                &\textbf{0.073}&\textbf{0.050} & 0.180 & 0.111 & \textbf{0.272} & 0.148\\ \hline
		\end{tabular}}}}		
	\end{center}
	\caption{A comprehensive performance comparison of all methods.}
	\label{Table 2}
	\vspace{-20pt}	
\end{table*}
```

## Table 3
```latex
\begin{table}[ht]
    \centering
    
    \label{tab:quant_all}

    \begin{tabular}{c|c|c|c|c}
        \hline
        Model & HR@5 & NDCG@5 & HR@10 & NDCG@10 \\
        \hline
        GPTQ & 0.1020 & 0.0880  &  0.1232 & 0.0951 \\
        SparseGPT & 0.0980 & 0.0830 & 0.1200 & 0.0905  \\
        OD-LLM &  0.0993& 0.0851 & 0.1219 &0.0923 \\
        \hline
    \end{tabular}

    { \textbf{(a) Instruments}}

   

    \begin{tabular}{c|c|c|c|c}
        \hline
        Model & HR@5 & NDCG@5 & HR@10 & NDCG@10 \\
        \hline
        GPTQ & 0.0992& 0.0808 & 0.1230&  0.0884       \\
        SparseGPT & 0.0800& 0.0620 &0.1180  & 0.0720        \\
        OD-LLM & 0.0838 &0.0644& 0.1264 & 0.0748       \\
        \hline
    \end{tabular}

    { \textbf{(b) Games}}

   

    \begin{tabular}{c|c|c|c|c}
        \hline
        Model & HR@5 & NDCG@5 & HR@10 & NDCG@10 \\
        \hline
        GPTQ & 0.0796 & 0.0554 & 0.1161 & 0.0672 \\
        SparseGPT &0.0707 &0.0511&    0.1201   &0.0677       \\
        OD-LLM & 0.1173 &0.1000 & 0.1434 & 0.1084 \\
        \hline
    \end{tabular}

    { \textbf{(c) Arts}}
\caption{Comparison with Quantization and Pruning on three datasets.}
\vspace{-10pt}
\end{table}
```

## Table 4
```latex
\begin{table}[ht]%[tb]
	
		% \renewcommand\arraystretch{1.0}
		
		\begin{center}
			% \resizebox{.45\textwidth}{!}{
			\begin{tabular}{c|c|c|c}
				\hline
				\ time (s)/batch& GPTQ&SparseGPT&OD-LLM       \\ \hline	
				  GPU & 17 &12 & 5\\
				   CPU&700& 620& 200\\
				\hline
			\end{tabular}
		\end{center}
		\caption{Inference Speed Comparison (Time(s) per batch).}	
		\label{Table.4}
		\vspace{-2em}
	\end{table}
```

