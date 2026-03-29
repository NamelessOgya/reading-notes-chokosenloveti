# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
  \caption{Recommendation performance and inference time-cost of BIGRec compared with DROS on Amazon Games and Toys datasets. Note that BIGRec is a typical LLM-based recommender with LlaMA-7B and DROS is a state-of-the-art sequential recommendation method. }
  \label{tab:inference time}
  \begin{tabular}{ccccc}
    \toprule
    Dataset&Model&HR@20&NDCG@20&Inference time\\
    \hline
    &DROS&0.0473&0.0267&1.8s\\
    &BIGRec&0.0532&0.0341&2.3$\times10^4s$\\
    \multirow{-3}{*}{Games}&\emph{Gain}&+12.47\%&+27.72\%&$-1.3\times10^6 \% $\\ \hline
    &DROS&0.0231&0.0144&1.6s\\
    &BIGRec&0.0420&0.0207&1.1$\times10^4$s\\
    \multirow{-3}{*}{Toys}&\emph{Gain}&+81.82\%&+43.75\%&$-6.8\times10^5 \% $\\
  \bottomrule
\end{tabular}
\vspace{-0.3cm}
\end{table}
```

## Table 2
```latex
\begin{table}[tbp]
 \vspace{-0em}
  \caption{The ratio of cases where BIGRec outperforms DROS to cases where BIGRec underperforms DROS on NDCG@20. }
  \vspace{-0.3cm}
  \label{tab:great}
  \begin{tabular}{ccc}
    \toprule
    Dataset& Condition	&  Relative Ratio\\
    \hline
                            &BIGRec > DROS & 53.90\%\\               
    \multirow{-2}{*}{Games} &BIGRec < DROS & 46.10\%\\  \hline
                                &BIGRec > DROS & 40.90\%\\
    \multirow{-2}{*}{MovieLens} &BIGRec < DROS & 59.10\%\\  \hline
                           &BIGRec > DROS & 66.67\%\\
    \multirow{-2}{*}{Toys} &BIGRec < DROS & 33.33\%\\
    \bottomrule
\end{tabular}
\vspace{-0cm}
\end{table}
```

## Table 3
```latex
\begin{table}[t]
  \caption{Ratio of overlapped items in Top-20 recommendations between BIGRec and DROS. Additionally, we present the percentage of these items that are actual hits. For comparative analysis, we detail the values specific to items unique to either BIGRec's or DROS's recommendations. 
  }
  \vspace{-0.3cm}
  \label{tab:consis}
  \begin{tabular}{cccc}
    \toprule
    Dataset&Rec. Space &Items Ratio	& Hit Items\\
    \hline
    &BIGRec only&96.01\%&0.21\%\\
    &DROS only&96.01\%&0.18\%\\
    \multirow{-3}{*}{Games}&Overlapped&3.99\%&1.61\% \\ \hline
    &BIGRec only&95.94\%&0.19\%\\
    &DROS only&95.94\%&0.35\%\\
    \multirow{-3}{*}{MovieLens}&Overlapped&4.06\%&2.16\% \\ \hline    
    &BIGRec only&98.95\% &0.17\%\\
    &DROS only&98.95\% &0.08\% \\
    \multirow{-3}{*}{Toys}&Overlapped&1.05\% &3.74\% \\
  \bottomrule
\end{tabular}
\end{table}
```

## Table 4
```latex
\begin{table}[htbp]
%   \caption{Detailed performance on user-level of BIGRec and DROS.  BIGRec doesn't always outperform DROS on user-level and their recommendation spaces are quite different from each other. }
%   \label{tab:great}
%   \begin{tabular}{ccccc}
%     \toprule
%     Dataset& Condition	& Users & Ratio & Relative Ratio\\
%     \hline
%                             &BIGRec > DROS & 651 & 4.35\% & 49.54\%\\
%                             &BIGRec = DROS & 106 & 0.71\% & 8.09\%\\                
%     \multirow{-3}{*}{Games} &BIGRec < DROS & 558 & 3.72\% & 42.37\%\\  \hline
%                                 &BIGRec > DROS & 483 & 4.83\% & 39.66\%\\
%                                 &BIGRec = DROS & 37  & 0.37\% & 3.04\%\\
%     \multirow{-3}{*}{MovieLens} &BIGRec < DROS & 698 & 6.98\% & 57.31\%\\  \hline
%                            &BIGRec > DROS & 176 & 3.64\% & 63.53\%\\
%                            &BIGRec = DROS & 13  & 0.27\% & 4.71\%\\
%     \multirow{-3}{*}{Toys} &BIGRec < DROS & 88  & 1.82\% & 31.76\%\\
%     \bottomrule
% \end{tabular}
% \end{table}
```

## Table 5
```latex
\begin{table}[htbp]
%   \caption{Illusion problem study on BIGRec. "-20\%", "-30\%" and "-50\%" denote the ratio that user's real interests are placed in the bottom 20\%, 30\% and 50\% of the recommendation list, respectively.}
%   \label{tab:great}
%   \begin{tabular}{cccc}
%     \toprule
%     Dataset& -20\%	& -30\% & -50\%\\
%     \hline
%     Games  &12.02\%	&18.76\%	&33.34\% \\ 
%     MovieLens  &15.95\%	&25.26\%	&38.79\% \\ 
%     Toys  &13.41\%	&19.74\%	&35.03\% \\
%     \bottomrule
% \end{tabular}
% \end{table}
```

## Table 6
```latex
\begin{table}[htbp]
%   \caption{Further study on consistency of two recommendation spaces.  Obviously, the consistency of two recommendation spaces leads to a higher positive item ratio. }
%   \label{tab:consis}
%   \begin{tabular}{ccccc}
%     \toprule
%     Dataset&Rec. Space &Items   &Pos. Items	& Pos. Ratio\\
%     \hline
%     &BIGRec only&287660&605&0.21\%\\
%     &DROS only&287660&517&0.18\%\\
%     \multirow{-3}{*}{Games}&Consistency&11940&193&1.61\% \\ \hline
%     &BIGRec only&191881&366&0.19\%\\
%     &DROS only&191881&677&0.35\%\\
%     \multirow{-3}{*}{MovieLens}&Consistency&8119&175&2.16\% \\ \hline    
%     &BIGRec only&95645 &165 &0.17\%\\
%     &DROS only&95645 &74 &0.08\% \\
%     \multirow{-3}{*}{Toys}&Consistency&1015 &38 &3.74\% \\
%   \bottomrule
% \end{tabular}
% \end{table}
```

## Table 7
```latex
\begin{table}
  \caption{Statistics of the datasets.}
  \vspace{-0.3cm}
  \label{tab:datasets}
  \begin{tabular}{ccccc}
    \toprule
     \textbf{Datasets} & \textbf{Games} & \textbf{MovieLens} & \textbf{Toys}\\
    \hline    
    \#Users & 55,223 & 69,878 & 19,412\\
    \#Items & 17,408 & 10,681 & 11,924\\
    \#Interactions & 497,577 & 1,320,000 & 167,597\\
    Density & 0.05176\% & 0.1769\% & 0.07241\%\\
  \bottomrule
\end{tabular}
\vspace{-0.5cm}
\end{table}
```

## Table 8
```latex
\begin{table*}[htbp]
\vspace{-0.3cm}
  \caption{Performance comparisons of DLLM2Rec with existing KD methods and LLM-enhanced strategies. The best performance is bold while the runner-up is underlined. \emph{Gain.S} denotes the improvement of DLLM2Rec over the student; while \emph{Gain.B} denotes the improvement of DLLM2Rec over the best baseline. }
  \vspace{-0.3cm}
  \label{tab:performance}
  \begin{tabular}{cccccccc}
    \toprule
\multirow{2}{*}{Backbone} &\multirow{2}{*}{Model}       & \multicolumn{2}{c}{ Games} & \multicolumn{2}{c}{ MovieLens} & \multicolumn{2}{c}{ Toys}\\ 
\cline{3-8} 
                                 &                   & HR@20   & NDCG@20      & HR@20  & NDCG@20        & HR@20 & NDCG@20       \\
\hline
                        Teacher  & BIGRec          & 0.0532  & 0.0341       & 0.0541 & 0.0370         & 0.0420 & 0.0207      \\        
\hline
                                 & +None          & 0.0305  & 0.0150       & 0.0608 & 0.0236         & 0.0172  & 0.0081           \\
                                 & +Hint          & 0.0284  & 0.0120       & 0.0646 & 0.0240   & 0.0128 & 0.0058                 \\
                                 & +HTD             & 0.0299  & 0.0128       & 0.0578 & 0.0229   & 0.0155 & 0.0062                 \\
                                 & +RD              & 0.0398  & 0.0177       & 0.0667 & 0.0254   & 0.0157 & 0.0076                 \\
                                 & +CD              & 0.0306  & 0.0149       & \underline{ 0.0699} & 0.0256 & 0.0126 & 0.0052           \\
                                 & +RRD             & 0.0359  & 0.0163       & 0.0657 & 0.0243         & 0.0215 & 0.0097           \\
                                 & +DCD             & \underline{ 0.0427}  & \underline{0.0190}       & 0.0666 & \underline{ 0.0263}         & \underline{ 0.0262} & \underline{ 0.0114}           \\
                                 & +UnKD            & 0.0370  & 0.0170       & 0.0607 & 0.0226         & 0.0235 & 	0.0114           \\
                                 & KAR               & 0.0307  & 0.0149       & 0.0603 & 0.0229         & 0.0184 & 0.0079         \\
                                 & LLM-CF            & 0.0393	& 0.0174       & 0.0677 & 0.0246         & 0.0132 & 0.0058         \\
                                 & +DLLM2Rec          & \textbf{0.0446} & \textbf{0.0205}  & \textbf{0.0815} & \textbf{0.0308} & \textbf{0.0281} & \textbf{0.0118}          \\
                                 \cline{2-8}
                                 & \emph{Gain.S}  & +46.17\% & +36.94\%   & +34.05\% & +30.43\%    & +63.88\% & +42.18\%               \\
\multirow{-13}{*}{ GRU4Rec}      & \emph{Gain.B}  & +4.56\% & +7.64\%   & +16.60\% & +16.80\%    & +7.40\% & +1.27\%               \\ 
\hline
                                 & +None          & 0.0346  & 0.0190       & 0.0626  & 0.0228        & 0.0207 	& 0.0130            \\
                                 & +Hint          & 0.0358  & 0.0151       & 0.0576 & 0.0216   & 0.0242 & 0.0103                 \\
                                 & +HTD             & 0.0343  & 0.0152       & 0.0569 & 0.0214   & 0.0209 & 0.0097                 \\
                                 & +RD              & 0.0513  & 0.0225  & 0.0778  & \underline{ 0.0310}   & \underline{ 0.0397} & 0.0164           \\
                                 & +CD              & 0.0396  & 0.0231 & 0.0712  & 0.0265        & 0.0232 & 0.0151            \\
                                 & +RRD             & 0.0479  & 0.0202       & 0.0633  & 0.0244        & 0.0325 & 0.0158            \\
                                 & +DCD             & 0.0455  & 0.0211       & 0.0723  & 0.0275        & 0.0375 & \underline{ 0.0175}            \\
                                 & +UnKD            & 0.0447  & 0.0219       & 0.0667  & 0.0247        & 0.0335 & 0.0174            \\
                                 & KAR               & 0.0381	  & 0.0198       & 0.0565	 & 0.0221         & 0.0215	 & 0.0131         \\
                                 & LLM-CF            &\underline{  0.0559}     & \underline{ 0.0251}       & \underline{ 0.0837}	 & 0.0295         & 0.0335 & 0.0152         \\
                                 & +DLLM2Rec          & \textbf{0.0600} & \textbf{0.0262} & \textbf{0.0840} & \textbf{0.0323}  & \textbf{0.0409} & \textbf{0.0177}         \\
                                 \cline{2-8}
                                 & \emph{Gain.S}  & +73.55\% & +38.25\%   & +34.19\% & +41.91\%    & +97.68\% & +36.38\%               \\
\multirow{-13}{*}{ SASRec}       & \emph{Gain.B}  & +7.36\% & +4.40\%   & +0.36\% & +4.34\%    & +3.02\% & +1.19\%               \\ 
\hline
                                 & +None          & 0.0473  & 0.0267       & 0.0852  & 0.0363        & 0.0231 	& 0.0144            \\
                                 & +Hint          & 0.0531  & 0.0240       & 0.0791 & 0.0306   & 0.0302 & 0.0135                 \\
                                 & +HTD             & 0.0489  & 0.0238       & 0.0722 & 0.0289   & 0.0275 & 0.0137                 \\         
                                 & +RD              & 0.0585  & \underline{ 0.0310} & 0.0950 & \underline{ 0.0383}    & 0.0424 & \underline{ 0.0220}          \\
                                 & +CD              & 0.0474  & 0.0270       & 0.0802  & 0.0336        & 0.0238 & 0.0156            \\
                                 & +RRD             & 0.0590  & 0.0293       & 0.0788  & 0.0338        & 0.0424 & 0.0212            \\
                                 & +DCD             & 0.0531  & 0.0273       & 0.0821  & 0.0348        & \underline{ 0.0432} & 0.0211            \\
                                 & +UnKD            & 0.0448  & 0.0209       & 0.0728  & 0.0297        & 0.0375 & 0.0195            \\
                                 & KAR               & 0.0586  & 0.0318       & 0.0859 & 0.0352         & 0.0255 & 0.0156         \\
                                 & LLM-CF            & \underline{ 0.0635}  & 0.0293       & \underline{ 0.0963} & 0.0351         & 0.0385 & 0.0178         \\
                                 & +DLLM2Rec          & \textbf{0.0751} & \textbf{0.0331}  & \textbf{0.1063} & \textbf{0.0437}   & \textbf{0.0463} & \textbf{0.0225}        \\
                                 \cline{2-8}
                                 & \emph{Gain.S}  & +58.77\% & +23.90\%   & +24.77\% & +20.41\%    & +100.43\% & +56.35\%               \\
\multirow{-13}{*}{ DROS}         & \emph{Gain.B}  & +18.27\% & +4.03\%   & +10.38\% & +14.24\%    & +7.07\% & +2.16\%               \\ 
\hline
\end{tabular}
\vspace{-0.3cm}
\end{table*}
```

## Table 9
```latex
\begin{table}[t]
\vspace{-0cm}
  \caption{Performance and efficiency comparison of BIGRec and DLLM2Rec on different datasets.}
  \vspace{-0.3cm}
  \label{tab:Efficiency}
  \setlength{\tabcolsep}{1mm}{
  \begin{tabular}{ccccc}
    \toprule
    Dataset&Model&HR@20&NDCG@20&Inference time\\
    \hline
    \multirow{3}{*}{Games}
    &BIGRec&0.0532&0.0341&2.3$\times10^4$s\\
    &DLLM2Rec&0.0751&0.0331&1.8s\\
    &\emph{Gain}&+37.41\%&-2.99\%&+1.3$\times10^6$\%\\
    \hline
    \multirow{3}{*}{MovieLens}
    &BIGRec&0.0541&0.0370&1.8$\times10^4$s\\
    &DLLM2Rec&0.1063&0.0437&1.7s\\
    &\emph{Gain}&+96.49\%&+18.18\%&+1.1$\times10^6$\%\\   
    \hline
    \multirow{3}{*}{Toys}
    &BIGRec&0.0420&0.0207&1.1$\times10^4$s\\
    &DLLM2Rec&0.0463&0.0225&1.6s\\
    &\emph{Gain}&+10.24\%&+8.70\%&+6.8$\times10^5$\%\\ 
  \bottomrule
\end{tabular}}
\end{table}
```

## Table 10
```latex
\begin{table}
  \caption{Overlapping ratio on Top-20 items.}
    \vspace{-0.3cm}
  \label{tab:overlapping}
  
  \begin{tabular}{ccccc}
    \toprule
     \textbf{Datasets} & \textbf{Before-distillation} & \textbf{Post-distillation}\\
    \hline    
    Games & 3.99\% & 10.88\% \\
    MovieLens & 4.06\% & 10.15\% \\
    Toys & 1.05\% & 14.56\%\\
  \bottomrule
  \end{tabular}
\end{table}
```

## Table 11
```latex
\begin{table}[t]
  \centering
  \caption{Ablation Study on ranking distillation.}
  \vspace{-0.3cm}
  \label{tab:Ablation}
  \scalebox{1.0}{
  \begin{tabular}{cccc}
    \toprule
    Dataset&Model&HR@20&NDCG@20 \\
    \hline
    \multirow{5}{*}{Games}
    &w/o $all_r$               &0.0661 	                &0.0301\\    
    &w/o $w^p_{\mathbf si}$            &0.0697 	                &0.0301\\
    &w/o $w^c_{\mathbf si}$            &0.0733 	                &0.0300\\
    &w/o $w^o_{\mathbf si}$            &0.0568 	                &0.0311\\
    &DLLM2Rec                        &\textbf{0.0751} 	    &\textbf{0.0331}\\
    \hline
    \multirow{5}{*}{MovieLens}
    &w/o $all_r$               &0.0917 	                &0.0364\\    
    &w/o $w^p_{\mathbf si}$            &0.1037	                &0.0429\\
    &w/o $w^c_{\mathbf si}$            &0.0986 	                &0.0398\\
    &w/o $w^o_{\mathbf si}$            &0.1047 	                &0.0430\\
    &DLLM2Rec                        &\textbf{0.1063} 	    &\textbf{0.0437}\\
    \hline
    \multirow{5}{*}{Toys}
    &w/o $all_r$               &0.0386 	                &0.0177\\    
    &w/o $w^p_{\mathbf si}$            &0.0406	                &0.0200\\
    &w/o $w^c_{\mathbf si}$            &0.0430 	                &0.0205\\
    &w/o $w^o_{\mathbf si}$            &0.0445 	                &0.0208\\
    &DLLM2Rec                        &\textbf{0.0463} 	    &\textbf{0.0225}\\
    \bottomrule
  \end{tabular}
  }
  \vspace{-0.3cm}
\end{table}
```

## Table 12
```latex
\begin{table}[t]
  \centering
  \caption{Ablation Study on embedding distillation.}
  \vspace{-0.3cm}
  \label{tab:Ablation2}
  \scalebox{1.0}{
  \begin{tabular}{cccc}
    \toprule
    Dataset&Model&HR@20&NDCG@20 \\
    \hline
    \multirow{5}{*}{Games}
    &w/o $all_e$                 &0.0649 	                &0.0323\\    
    &w/o \emph{offset}                      &0.0700 	                &0.0298\\
    &Hint                            &0.0563 	                &0.0244\\
    &HTD                             &0.0568 	                &0.0246\\
    &DLLM2Rec                        &\textbf{0.0751} 	    &\textbf{0.0331}\\
    \hline
    \multirow{5}{*}{MovieLens}
    &w/o $all_e$                 &0.0999 	                &0.0420\\    
    &w/o \emph{offset}                      &0.1061 	                &0.0425\\
    &Hint                            &0.0861 	                &0.0344\\
    &HTD                             &0.0874 	                &0.0341\\    
    &DLLM2Rec                        &\textbf{0.1063} 	    &\textbf{0.0437}\\
    \hline
    \multirow{5}{*}{Toys}
    &w/o $all_e$                 &0.0379 	                &0.0194\\    
    &w/o \emph{offset}                      &0.0405 	                &0.0195\\
    &Hint                            &0.0358 	                &0.0159\\
    &HTD                             &0.0349 	                &0.0157\\    
    &DLLM2Rec                        &\textbf{0.0463} 	    &\textbf{0.0225}\\
    \bottomrule
  \end{tabular}
  }
  \vspace{-0.3cm}
\end{table}
```

