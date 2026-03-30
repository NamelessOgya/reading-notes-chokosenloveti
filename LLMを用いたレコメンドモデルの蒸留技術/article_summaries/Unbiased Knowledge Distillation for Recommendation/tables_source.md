# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]\small %
		\centering
		\caption{Performance (Recall@10) comparison of various knowledge distillation methods in terms of popular/unpopular items on three real-world datasets. We also report the relative improvements over the baseline (`Student') that is directly learned from the data. The experimental settings and the group partition are detailed in Section 4.}
		\setlength{\tabcolsep}{0.75mm}{
			\begin{tabular}{|c|c|c|c|c|c|c|}
				\hline
				\multicolumn{7}{|c|}{Movielens}\\
				\hline
				&Student&Teacher&RD\cite{10.1145/3219819.3220021}&CD\cite{8970837}&DERRD\cite{10.1145/3340531.3412005}&HTD\cite{10.1145/3447548.3467319} \\
				\hline
				Popular &0.2156&0.2565 &0.2237 &0.2258 &0.2315&0.2228  \\
				Group& ---& +18.97\%& +3.75\% &+4.73\%&+7.37\%&+3.33\%\\
				\hline
				Unpopular&0.0250&0.0517& 0.0242&0.0179 &0.0113&0.0187  \\
				Group& --- & +106.80\%&-3.20\% &-28.40\%  &-54.80\%  &-25.20\%  \\
				\hline
				\multicolumn{7}{|c|}{Apps}\\
				\hline
				&Student&Teacher&RD\cite{10.1145/3219819.3220021}&CD\cite{8970837}&DERRD\cite{10.1145/3340531.3412005}&HTD\cite{10.1145/3447548.3467319} \\
				\hline
				Popular &0.1031&0.1448 &0.1144&0.1212 &0.1058 &0.1195  \\
				Group&  ---& +40.44\%& +10.96\% &+17.55\%&+2.61\%&+15.90\%\\
				\hline
				Unpopular  &0.0109  &0.0164&0.0098&0.0090&0.0098 &0.0061    \\
				Group& --- & +50.45\%&-10.09\% &-17.43\%  &-10.09\%  &-44.03\%  \\
				\hline
				\multicolumn{7}{|c|}{CiteULike}\\
				\hline
				&Student&Teacher&RD\cite{10.1145/3219819.3220021}&CD\cite{8970837}&DERRD\cite{10.1145/3340531.3412005}&HTD\cite{10.1145/3447548.3467319} \\
				\hline
				Popular &0.0831&0.1294&0.0910&0.0887&0.0899 &0.0885 \\
				Group&---  & +55.71\%& +9.50\% &+6.73\%&+8.18\%&+6.49\%\\
				\hline
				Unpopular &0.0095& 0.0537&0.0085&0.0088 &0.0075  &0.0068   \\
				Group& --- & +465.26\%&-10.52\% &-7.36\%  &-21.05\%  &-28.42\%  \\
				\hline
		\end{tabular}}
		\label{tab:table_3}
	\end{table}
```

## Table 2
```latex
\begin{table}[t] %
	\centering
	\caption{Statistics of the  datasets.}
	\begin{tabular}{|c|c|c|c|c|}
		\hline
		dataset&Users&Items&Interactions&Sparsity \\
		\hline
		CiteULike   & 5219  & 25181& 125580 &99.91\% \\
		Apps       & 3898  & 11797& 128105 &99.73\% \\
		MovieLens    & 6040  & 3706&1000209&95.54\% \\
		\hline
	\end{tabular}
	
	\label{tab:table_1}
\end{table}
```

## Table 3
```latex
\begin{table}[t]\small%
	\centering
	\caption{Overall performance comparison between our method and  baselines. All metrics are based on the top-10 results. where the best performance is bold and the second best underlined.}
	\begin{tabular}{|c|c|c|c|c|c|}
		\hline
		&Backbone Model&\multicolumn{2}{c|}{BPRMF}&\multicolumn{2}{c|}{LightGCN}\\
		\hline 
		Dataset&Method&Recall&NDCG&Recall&NDCG\\
		\hline
		
		\multirow{8}{*}{MovieLens}&Teacher&0.1810&0.2951&0.1850&0.3012\\
		\cline{2-6}
		&Student&0.1435&0.2511&0.1456&0.2581\\
		&RD&\underline{0.1473}&\underline{0.2559}&0.1471&0.2583\\
		&CD&0.1445&0.2534&0.1477&0.2602\\
		&DERRD&0.1436&0.2532&\underline{0.1487}&\underline{0.2606}\\
		&HTD&0.1441&0.2539&0.1472&0.2592\\
		\cline{2-6}
		%&UnKD-F&0.1933&0.2377&0.2072&0.2586\\
		&UnKD&\textbf{0.1547}&\textbf{0.2615}&\textbf{0.1569}&\textbf{0.2672}\\
		&impv-e\%&5.02\%&2.18\%&5.51\%&2.53\%\\
		\hline
		\multirow{8}{*}{Apps}&Teacher&0.0991&0.0760&0.1007&0.0782\\
		\cline{2-6}
		&Student&0.0719&0.0539&0.0811&0.0643\\
		&RD&0.0768&0.0596&0.0831&0.0647\\
		&CD&\underline{0.0790}&\underline{0.0608}&\underline{0.0848}&\underline{0.0658}\\
		&DERRD&0.0729&0.0562&0.0832&0.0648\\
		&HTD&0.0732&0.0561&0.0833&0.0652\\
		\cline{2-6}
		%&UnKD-F&0.0272&0.0587&0.0295&0.0651\\
		&UnKD&\textbf{0.0853}&\textbf{0.0644}&\textbf{0.0867}&\textbf{0.0678}\\
		&impv-e\%&7.97\%&5.92\%&2.24\%&3.04\%\\
		\hline
		\multirow{8}{*}{CiteULike}&Teacher&0.1518&0.1016&0.1657&0.1139\\
		\cline{2-6}
		&Student&0.0760&0.0477&0.0783&0.0510\\
		&RD&\underline{0.0808}&0.0514&0.0833&0.0538\\
		&CD&0.0801&\underline{0.0518}&0.0936&0.0616\\
		&DERRD&0.0793&0.0511&0.0809&0.0527\\
		&HTD&0.0788&0.0485&\underline{0.0958}&\underline{0.0628}\\
		\cline{2-6}
		%&UnKD-F&0.0172&0.0501&\underline{0.0212}&0.0617\\
		&UnKD&\textbf{0.0863}&\textbf{0.0550}&\textbf{0.1006}&\textbf{0.0654}\\
		&impv-e\%&6.80\%&6.17\%&5.01\%&4.14\%\\
		\hline
	\end{tabular}
	\label{tab:table_2}
\end{table}
```

## Table 4
```latex
\begin{table*}[ht]%
	\centering
	\caption{Performance comparison (recall@10) between our UnKD and the baselines that leverages debiasing technique in model training. The best performance is shown in bold, and the second best performance is underlined.}
	\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		&Dataset&\multicolumn{3}{c|}{MovieLens}&\multicolumn{3}{c|}{Apps}&\multicolumn{3}{c|}{CiteULike}\\
		\hline 
		\multirow{2}{*}{Backbone Model}&\multirow{2}{*}{Method}&\multirow{2}{*}{Overall}&Popular&Unpopular&\multirow{2}{*}{Overall}&Popular&Unpopular&\multirow{2}{*}{Overall}&Popular&Unpopular\\
		&&&Group&Group&&Group&Group&&Group&Group\\
		\hline
		& Student  &0.1435&0.2156&0.0250& 0.0719& 0.1031&0.0109 &0.0760&0.0831&\underline{0.0095}\\
		& CD  & 0.1445&\textbf{0.2258}&0.0179  & 0.0790&0.1212&0.0090 &0.0801&0.0887&0.0088 \\
		& PD-CD  &\underline{0.1454}&0.2205&0.0210&0.0795&0.1176&\underline{0.0113} &\underline{0.0805}&\underline{0.0890}&0.0092 \\
		%		& Reg-CD  &0.1446& \underline{0.2245}&0.0177& 0.0785&0.1173&0.0101&0.0762&0.0844&0.0063  \\
		BPRMF&HTD&0.1441&\underline{0.2228}&0.0187 &0.0732&0.1195&0.0061&0.0788&0.0885&0.0068\\
		& PD-HTD  &0.1443&0.2150&\underline{ 0.0263} & \underline{0.0808}&\underline{0.1240}&0.0076 & 0.0798&\textbf{0.0897}&0.0073\\
		%		& Reg-HTD  & 0.1441& 0.2204&0.0206 & 0.0759&0.1175&0.0079&0.0765&0.0858&0.0050  \\
		\cline{2-11}
		& UnKD  &\textbf{0.1547}&0.2205 &\textbf{0.0311}&\textbf{0.0853}&\textbf{0.1274}&\textbf{0.0147}&\textbf{0.0863}&0.0854 &\textbf{0.0208}\\
		\hline
		& Student &0.1456&0.2280&\underline{0.0228}  &0.0811&0.1242&0.0093 &0.0783&0.0885&0.0080 \\
		& CD  &0.1477&0.2316&0.0169&0.0848&\underline{0.1310}&0.0091 &0.0936&0.1067&0.0081 \\
		& PD-CD  &\underline{0.1496}&\underline{0.2369}&0.0172&\underline{0.0851}&0.1308&\underline{0.0095}&0.0942&0.1020&0.0110 \\
		%		& Reg-CD    &\underline{0.1502}&\textbf{0.2426}&0.0122&0.0856&0.1299&0.0096 &0.0851&0.0928& 0.0061\\
		LightGCN&HTD&0.1472&0.2328&0.0079&0.0833&0.1291&0.0091&0.0958&\underline{0.1093}&0.0085 \\
		& PD-HTD  &0.1485&0.2364&0.0159 &0.0835&0.1288& 0.0093&\underline{0.0979}&\textbf{0.1102}&\underline{0.0128}\\		
		%		& Reg-HTD  &0.1475&0.2345&0.0172 &\underline{0.0860}&\underline{0.1314}&0.0085  &0.0932&\underline{0.1082}&0.0075\\
		\cline{2-11}
		& UnKD  &\textbf{0.1569}&\textbf{0.2384}&\textbf{0.0292}&\textbf{0.0867}&\textbf{0.1325}&\textbf{0.0118}&\textbf{0.1006}&0.1076&\textbf{0.0162}\\
		
		\hline			
	\end{tabular}
	
	\label{tab:table_4}
\end{table*}
```

