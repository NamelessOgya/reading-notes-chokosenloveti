# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
    \vspace{-5pt}
    \caption{The dataset statistics.}
    \vspace{-5pt}
    \centering
    \resizebox{0.45\textwidth}{!}{
    \renewcommand\arraystretch{1.1}
    \begin{tabular}{c|cccccc}
    \toprule
     Dataset   & \#Users & \#Items & \#Samples & \#Fields & \#Features \\ 
     \midrule
     BookCrossing  & 278,858 & 271,375 & 17,714 & 10 & 912,279 \\
     MovieLens-1M & 6,040 & 3,706 & 970,009 & 10 & 16,944 \\
     MovieLens-25M & 162,541 & 59,047 & 25,000,095 & 6 & 280,576 \\ \bottomrule
    \end{tabular}
    }
    \vspace{-5pt}
    \label{tab:datasets}
\end{table}
```

## Table 2
```latex
\begin{table*}
\vspace{-7pt}
\caption{The performance of different models in \emph{zero-shot}, \emph{full-shot} and \emph{few-shot} settings. 
In \emph{full-shot} setting, the baselines are trained on the entire training set. 
In \emph{few-shot} setting, the number of training shots $N$ is selected from $\{256 (<1\%), 1024(<10\%)\}$ on BookCrossing dataset, and $\{8192 (<1\%), 65536 (<10\%)\}$ on MovieLens-1M and MovieLens-25M datasets. 
% The user behavior sequence length $K$ is set to 60 on BookCrossing and 30 on both MovieLens-1M and MovieLens-25M. 
The best result is given in bold, and the second-best value is underlined. 
\emph{Rel.Impr} denotes the relative AUC improvement rate of ReLLa against each baseline. 
The symbol $\ast$ indicates statistically significant improvement of ReLLa over the best baseline with $p$-value < 0.001.
}
\vspace{-5pt}
% \Jianghao{best bold; second best underlined}
\label{tab:zero & few shot performance}
\resizebox{0.965\textwidth}{!}{
\renewcommand\arraystretch{1.1}
\begin{tabular}{c|c|cccc|cccc|cccc}
\toprule
\hline

\multicolumn{2}{c|}{\multirow{2}{*}{Model}} & \multicolumn{4}{c|}{BookCrossing} & \multicolumn{4}{c|}{MovieLens-1M} & \multicolumn{4}{c}{MovieLens-25M} \\ 
\multicolumn{2}{c|}{} & AUC  & Log Loss & ACC & Rel.Impr & AUC  & Log Loss & ACC & Rel.Impr & AUC  & Log Loss & ACC & Rel.Impr\\ 
   \hline 
   
\multicolumn{1}{c|}{\multirow{3}{*}{Zero-shot}} & Vicuna-7B & 0.7011 & \underline{0.9357} & 0.5378 & 3.45\% & 0.6739 & 0.9510 & 0.5644 & 4.07\% & \underline{0.7468} & 0.6348 & 0.6392 & -1.93\% \\
\multicolumn{1}{c|}{\multirow{3}{*}{}} & Vicuna-13B & \underline{0.7176} & 0.9507 & \underline{0.5649} & 1.07\% & 0.6993 & 0.6291 & 0.6493 & 0.29\% & \textbf{0.7503} & \underline{0.6308} & \underline{0.6427} & -2.39\% \\
\multicolumn{1}{c|}{\multirow{3}{*}{}} & ReLLa (Ours) & \textbf{0.7253$^*$} & \textbf{0.9277$^*$} & \textbf{0.5750$^*$} & - & \textbf{0.7013$^*$} & \textbf{0.6250$^*$} & \textbf{0.6507$^*$} & - & 0.7324 & \textbf{0.5858$^*$} & \textbf{0.7027$^*$} & - \\
   \hline  


\multicolumn{1}{c|}{\multirow{12}{*}{Full-shot}} & DeepFM & 0.7496 & 0.5953 & 0.6760 & 1.05\% & 0.7915 & 0.5484 & 0.7225 & 1.49\% & 0.8189 & 0.4867 & 0.7709 & 3.52\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & AutoInt & 0.7481 & 0.6840 & 0.6365 & 1.26\% & 0.7929 & 0.5453 & 0.7226 & 1.31\% & 0.8169 & 0.4957 & 0.7689 & 3.77\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & DCNv2 & 0.7472 & 0.6816 & 0.6472 & 1.38\% & 0.7931 & 0.5464 & 0.7216 & 1.29\% & 0.8190 & 0.4989 & 0.7702 & 3.50\%\\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & GRU4Rec & 0.7479 & 0.5930 & 0.6777 & 1.28\% & 0.7926 & 0.5453 & 0.7225 & 1.35\% & 0.8186 & 0.4941 & 0.7700 & 3.55\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & Caser & 0.7478 & 0.5990 & 0.6760 & 1.30\% & 0.7918 & 0.5464 & 0.7206 & 1.45\% & 0.8199 & 0.4865 & 0.7707 & 3.39\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & SASRec & 0.7482 & 0.5934 & \textbf{0.6811} & 1.24\% & 0.7934 & 0.5460 & 0.7233 & 1.25\% & 0.8187 & 0.4956 & 0.7691 & 3.54\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & DIN & 0.7477 & 0.6811 & 0.6557 & 1.31\% & 0.7962 & 0.5425 & 0.7252 & 0.89\% & 0.8190 & 0.4906 & 0.7716 & 3.50\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & SIM & \underline{0.7541} & \textbf{0.5893} & 0.6777 & 0.45\% & \underline{0.7992} & \underline{0.5387} & \underline{0.7268} & 0.51\% & \underline{0.8344} & \underline{0.4724} & \underline{0.7822} & 1.59\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & CTR-BERT & 0.7448 & 0.5938 & 0.6704 & 1.71\% & 0.7931 & 0.5457 & 0.7233 & 1.29\% & 0.8079 & 0.5044 & 0.7511 & 4.93\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & PTab & 0.7429 & 0.6154 & 0.6574 & 1.97\% & 0.7955 & 0.5428 & 0.7240 & 0.98\% & 0.8107 & 0.5022 & 0.7551 & 4.56\% \\ 
\multicolumn{1}{c|}{\multirow{4}{*}{}} & P5 & 0.7438 & 0.6128 & 0.6563 & 1.84\% & 0.7937 & 0.5478 & 0.7190 & 1.21\% & 0.8092 & 0.5030 & 0.7527 & 4.76\% \\ 
\hline
\multicolumn{1}{c|}{\multirow{2}{*}{Few-shot}} & ReLLa (<1\%) & 0.7482 & 0.6265 & 0.6800 & - & 0.7927 & 0.5475 & 0.7196 & - & 0.8352 & 0.4693 & 0.7779 & - \\ 
\multicolumn{1}{c|}{\multirow{2}{*}{}} & ReLLa (<10\%) & \textbf{0.7575$^*$} & \underline{0.5919} & \underline{0.6806} & - & \textbf{0.8033$^*$} & \textbf{0.5362$^*$} & \textbf{0.7280$^*$} & - & \textbf{0.8477$^*$} & \textbf{0.4524$^*$} & \textbf{0.7925$^*$} & - \\ 
  
   \hline  
   \bottomrule          
\end{tabular}
\vspace{-5pt}
}
\end{table*}
```

## Table 3
```latex
\begin{table*}
% \caption{The performance of different models in \emph{zero-shot}, \emph{full-shot} and \emph{few-shot} settings. In \emph{full-shot} setting, the baselines are trained on the whole training sets. In \emph{few-shot} setting, the number of training shots $N$ is selected from \{256 (<1\%), 1024(<10\%)\} on BookCrossing and \{8192 (<1\%), 65536 (<10\%)\} on MovieLens-1M and MovieLens-25M. The user behavior sequence length $K$ is set to 60 on BookCrossing and 30 on both MovieLens-1M and MovieLens-25M. The best result is given in bold, and the second-best value is underlined. \emph{Rel.Impr} denotes the relative AUC improvement rate of ReLLa against each baseline. The symbol "$\ast$" indicates statistically significant improvement of ReLLa over the best baseline with $p$-value < 0.001.
% }
% \Jianghao{best bold; second best underlined}
% \label{tab:zero & few shot performance}
% \resizebox{1.02\textwidth}{!}{
% \renewcommand\arraystretch{1.1}
% \begin{tabular}{c|c|cccc|cccc|cccc}
% \toprule
% \hline

% \multicolumn{2}{c|}{\multirow{2}{*}{Model}} & \multicolumn{4}{c|}{BookCrossing} & \multicolumn{4}{c|}{MovieLens-1M} & \multicolumn{4}{c}{MovieLens-25M} \\ 
% \multicolumn{2}{c|}{} & AUC  & Log Loss & ACC & Rel.Impr & AUC  & Log Loss & ACC & Rel.Impr & AUC  & Log Loss & ACC & Rel.Impr\\ 
%    \hline 
   
% \multicolumn{1}{c|}{\multirow{3}{*}{Zero-shot}} & Vicuna-7B & 0.7011 & \underline{0.9357} & 0.5378 & 3.45\% & 0.6739 & 0.9510 & 0.5644 & 4.07\% & \underline{0.7468} & 0.6348 & 0.6392 & -1.93\% \\
% \multicolumn{1}{c|}{\multirow{3}{*}{}} & Vicuna-13B & \underline{0.7176} & 0.9507 & \underline{0.5649} & 1.07\% & 0.6993 & 0.6291 & 0.6493 & 0.29\% & \textbf{0.7503} & \underline{0.6308} & \underline{0.6427} & -2.39\% \\
% \multicolumn{1}{c|}{\multirow{3}{*}{}} & ReLLa (Ours) & \textbf{0.7253$^*$} & \textbf{0.9277$^*$} & \textbf{0.5750$^*$} & - & \textbf{0.7013$^*$} & \textbf{0.6250$^*$} & \textbf{0.6507$^*$} & - & 0.7324 & \textbf{0.5858$^*$} & \textbf{0.7027$^*$} & - \\
%    \hline  


% \multicolumn{1}{c|}{\multirow{12}{*}{Full-shot}} & DeepFM & 0.7496 & 0.5953 & 0.6760 & 0.85\% & 0.7915 & 0.5484 & 0.7225 & 1.49\% & 0.8189 & 0.4867 & 0.7709 & 3.52\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & AutoInt & 0.7481 & 0.6840 & 0.6365 & 1.06\% & 0.7929 & 0.5453 & 0.7226 & 1.31\% & 0.8169 & 0.4957 & 0.7689 & 3.77\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & DCNv2 & 0.7472 & 0.6816 & 0.6472 & 1.18\% & 0.7931 & 0.5464 & 0.7216 & 1.29\% & 0.8190 & 0.4989 & 0.7702 & 3.50\%\\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & GRU4Rec & 0.7479 & 0.5930 & 0.6777 & 1.08\% & 0.7926 & 0.5453 & 0.7225 & 1.35\% & 0.8186 & 0.4941 & 0.7700 & 3.55\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & Caser & 0.7478 & 0.5990 & 0.6760 & 1.10\% & 0.7918 & 0.5464 & 0.7206 & 1.45\% & 0.8199 & 0.4865 & 0.7707 & 3.39\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & SASRec & 0.7482 & 0.5934 & \underline{0.6811} & 1.04\% & 0.7934 & 0.5460 & 0.7233 & 1.25\% & 0.8187 & 0.4956 & 0.7691 & 3.54\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & DIN & 0.7477 & 0.6811 & 0.6557 & 1.11\% & 0.7962 & 0.5425 & 0.7252 & 0.89\% & 0.8190 & 0.4906 & 0.7716 & 3.50\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & SIM & \underline{0.7541} & \underline{0.5893} & 0.6777 & 0.25\% & 0.7992 & \underline{0.5387} & \underline{0.7268} & 0.51\% & 0.8344 & 0.4724 & 0.7822 & 1.59\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & CTR-BERT & 0.7448 & \textbf{0.5878} & 0.6704 & 1.50\% & 0.7931 & 0.5457 & 0.7233 & 1.29\% & 0.0000 & 0.0000 & 0.0000 & -100.00\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & PTab & 0.7429 & 0.6154 & 0.6574 & 1.76\% & 0.7955 & 0.5428 & 0.7240 & 0.98\% & 0.0000 & 0.0000 & 0.0000 & -100.00\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & P5 & 0.7438 & 0.6128 & 0.6563 & 1.64\% & 0.7937 & 0.5478 & 0.7190 & 1.21\% & 0.8092 & 0.5030 & 0.7527 & 4.76\% \\ 
% \hline
% \multicolumn{1}{c|}{\multirow{4}{*}{Few-shot}} & TALLRec (<1\%) & 0.7167 & 0.9293 & 0.4898 & 5.48\% & 0.7718 & 0.5795 & 0.7039 & 4.08\% & 0.8174 & 0.4892 & 0.7685 & 3.71\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & TALLRec (<10\%) & 0.7471 & 0.6144 & \textbf{0.6851} & 1.19\% & \underline{0.8006} & 0.5470 & 0.7217 & 0.34\% & 0.8435 & 0.4539 & 0.7882 & 0.50\% \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & ReLLa (<1\%) & 0.7482 & 0.6265 & 0.6800 & - & 0.7927 & 0.5475 & 0.7196 & - & 0.8352 & 0.4693 & 0.7779 & - \\ 
% \multicolumn{1}{c|}{\multirow{4}{*}{}} & ReLLa (<10\%) & \textbf{0.7560$^*$} & 0.6198 & 0.6789 & - & \textbf{0.8033$^*$} & \textbf{0.5362$^*$} & \textbf{0.7280$^*$} & - & \textbf{0.8477$^*$} & \textbf{0.4524$^*$} & \textbf{0.7925$^*$} & - \\ 
  
%    \hline  
%    \bottomrule          
% \end{tabular}
% }
% \end{table*}
```

## Table 4
```latex
\begin{table*}
\vspace{-7pt}
\caption{ The performance of different variants of ReLLa. We remove different components of ReLLa to evaluate the contribution of each part to the model. 
The best result is given in bold, and the second-best value is underlined. 
}
\vspace{-10pt}
% \Jianghao{best in bold. second best underlined. * to indicate significant}
\label{tab:ablation}
\resizebox{0.88\textwidth}{!}{
\renewcommand\arraystretch{1.1}
\begin{tabular}{c|ccc|ccc|ccc}
\toprule
\hline

% \multicolumn{2}{c|}{\multirow{2}{*}{Model}} & \multicolumn{4}{c}{MovieLens-1M} \\ 
% \multicolumn{2}{c|}{} & AUC  & Log Loss & ACC & Rel.Impr\\ 
\multicolumn{1}{c|}{\multirow{2}{*}{Model Variant}} & \multicolumn{3}{c|}{BookCrossing} & \multicolumn{3}{c|}{MovieLens-1M} & \multicolumn{3}{c}{MovieLens-25M} \\ 
\multicolumn{1}{c|}{} & AUC  & Log Loss & ACC & AUC  & Log Loss & ACC & AUC  & Log Loss & ACC \\ 
   \hline 
ReLLa (Ours) & \textbf{0.7482} & \underline{0.6265} & \textbf{0.6800} & \textbf{0.7927} & \textbf{0.5475} & \textbf{0.7196} & \textbf{0.8352} & \textbf{0.4693} & \textbf{0.7779} \\ 
ReLLa (w/o Mixture) & 0.7399 & \textbf{0.6002} & 0.6715 & 0.7849 & \underline{0.5693} & 0.6985 & 0.8192 & 0.4904 & \underline{0.7715} \\ 
ReLLa (w/o Retrieval) & 0.7167 & 0.9293 & 0.4898 & 0.7718 & 0.5795 & \underline{0.7039} & 0.8174 & \underline{0.4892} & 0.7685 \\ 
ReLLa ($\frac{1}{2}N$-shot) & \underline{0.7415} & 0.6268 & 0.6462 & \underline{0.7862} & 0.5781 & 0.6964 & \underline{0.8231} & 0.5157 & 0.7672 \\ 
ReLLa (w/o IT) & 0.7253 & 0.9277 & 0.5750 & 0.7013 & 0.6250 & 0.6507 & 0.7324 & 0.5858 & 0.7027 \\ 
ReLLa (w/o IT \& Retrieval) & 0.7176 & 0.9507 & 0.5649 & 0.6993 & 0.6291 & 0.6493 & 0.7503 & 0.6308 & 0.6427 \\ 
  
   \hline  
   \bottomrule          
\end{tabular}
\vspace{-10pt}
}
\end{table*}
```

## Table 5
```latex
\begin{table}[h]
    \caption{Zero-shot AUC performance w.r.t. different sequence length $K$ for different LLMs on MovieLens-1M dataset. The peaking performance for each LLM is given in bold.
    }
    \vspace{-10pt}
    \label{tab:universality}
    \resizebox{0.48\textwidth}{!}{
    \renewcommand\arraystretch{1.1}
    \begin{tabular}{c|ccccccc}
    \toprule
    \hline
    \multicolumn{1}{c|}{\multirow{2}{*}{LLM}} & \multicolumn{6}{c}{MovieLens-1M} \\ 
    \multicolumn{1}{c|}{} & K=5 & K=10 & K=15 & K=20 & K=25 & K=30 \\ 
   \hline 
   Falcon-7B & \textbf{0.5906} & 0.5741 & 0.5583 & 0.5420 & 0.5468 & 0.5452 \\ 
   Mistral-7B & 0.6566 & 0.6568 & \textbf{0.6670} & 0.6623 & 0.6612 & 0.6610 \\
   Vicuna-7B & 0.6630 & 0.6586 & \textbf{0.6739} & 0.6527 & 0.6463 & 0.6412 \\
   Vicuna-13B & 0.6807 & 0.6932 & \textbf{0.6993} & 0.6918 & 0.6937 & 0.6908 \\
   LLaMA2-70B & 0.6259 & 0.6348 & \textbf{0.6421} & 0.6402 & 0.6339 & 0.6321 \\
   \hline  
   \bottomrule          
\end{tabular}
}
\end{table}
```

## Table 6
```latex
\begin{table}[t]
    \caption{The model compatibility of ReLLa w.r.t. different backbone LLMs on MovieLens-1M dataset with $K$=30. We also give the performance of SIM, which is the best baseline among traditional recommendation models.
    }
    \vspace{-10pt}
    \label{tab:generalization}
    \resizebox{0.48\textwidth}{!}{
    \renewcommand\arraystretch{1.1}
    \begin{tabular}{c|c|ccc}
    \toprule
    \hline
    \multicolumn{2}{c|}{\multirow{2}{*}{Model}} & \multicolumn{3}{c}{MovieLens-1M} \\ 
    \multicolumn{2}{c|}{} & AUC & Log Loss & ACC \\ 
   \hline 
   \multicolumn{1}{c|}{\multirow{3}{*}{SIM}} & few-shot (<1\%) & 0.7352 & 0.6132 & 0.6743 \\ 
   \multicolumn{1}{c|}{} & few-shot (<10\%) & 0.7414 & 0.6129 & 0.6756 \\ 
   \multicolumn{1}{c|}{} & full-shot & \textbf{0.7992} & \textbf{0.5387} & \textbf{0.7268} \\ 
   \hline 
   \multicolumn{1}{c|}{\multirow{4}{*}{Falcon-7B}} & zero-shot & 0.5906 & 0.7674 & 0.5436 \\ 
   \multicolumn{1}{c|}{} & with SUBR & 0.5964 & 0.7709 & 0.5437 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<1\%) & 0.7811 & 0.5589 & 0.7111 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<10\%) & \textbf{0.7870} & \textbf{0.5658} & \textbf{0.7072} \\ 
   \hline 
   \multicolumn{1}{c|}{\multirow{4}{*}{Mistral-7B}} & zero-shot & 0.6670 & 0.7556 & 0.4793 \\ 
   \multicolumn{1}{c|}{} & with SUBR & 0.6881 & 0.7321 & 0.5119 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<1\%) & 0.7905 & 0.5488 & 0.7210 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<10\%) & \textbf{0.8005} & \textbf{0.5388} & \textbf{0.7275} \\ 
   \hline 
   \multicolumn{1}{c|}{\multirow{4}{*}{Vicuna-7B}} & zero-shot & 0.6739 & 0.9510 & 0.5644 \\ 
   \multicolumn{1}{c|}{} & with SUBR & 0.6704 & 0.7745 & 0.5655 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<1\%) & 0.7918 & 0.5493 & 0.7196 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<10\%) & \textbf{0.8016} & \textbf{0.5365} & \textbf{0.7274} \\ 
   \hline 
   \multicolumn{1}{c|}{\multirow{4}{*}{Vicuna-13B}} & zero-shot & 0.6993 & 0.6291 & 0.6493 \\ 
   \multicolumn{1}{c|}{} & with SUBR & 0.7013 & 0.6250 & 0.6507 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<1\%) & 0.7927 & 0.5475 & 0.7196 \\ 
   \multicolumn{1}{c|}{} & with ReiT (<10\%) & \textbf{0.8033} & \textbf{0.5362} & \textbf{0.7280} \\ 
   \hline  
   \bottomrule          
\end{tabular}
}
\end{table}
```

## Table 7
```latex
\begin{table}[t]
    \caption{Complexity analysis on MovieLens-1M dataset.
    }
    \vspace{-10pt}
    \label{tab:complexity}
    \resizebox{0.48\textwidth}{!}{
    \renewcommand\arraystretch{1.1}
    \begin{tabular}{cccc}
    \toprule
    \hline
    Model & \# Total Parameter & \# Trainable Parameter & Inference Time \\ 
    \hline
    SIM & 1.44M & 1.44M & 3.21ms \\
    ReLLa & 13B & 650M & 500ms \\
   \hline  
   \bottomrule          
\end{tabular}
    \vspace{-10pt}
}
\end{table}
```

## Table 8
```latex
\begin{table}[t]
    \caption{Ablation study w.r.t different PCA dimensionalities for ReLLa on MovieLens-1M dataset under both zero-shot and few-shot (<1\%) settings.
    }
    \vspace{-5pt}
    \label{tab:ablation pca}
    \resizebox{0.45\textwidth}{!}{
    \renewcommand\arraystretch{1.1}
    \begin{tabular}{c|c|ccc}
    \toprule
    \hline
    \multicolumn{1}{c|}{\multirow{2}{*}{Setting}} & \multicolumn{1}{c|}{\multirow{2}{*}{PCA Dim.}} & \multicolumn{3}{c}{MovieLens-1M} \\ 
    \multicolumn{1}{c|}{} & \multicolumn{1}{c|}{} & AUC & Log Loss & ACC \\
    \hline
    \multicolumn{1}{c|}{\multirow{4}{*}{zero-shot}} & 512 & 0.7013 & \textbf{0.6250} & \textbf{0.6507} \\
    \multicolumn{1}{c|}{} & 256 & \textbf{0.7064} & 0.6377 & 0.6357 \\
    \multicolumn{1}{c|}{} & 128 & 0.7063 & 0.6379 & 0.6351 \\
    \multicolumn{1}{c|}{} & 64 & 0.7057 & 0.6375 & 0.6349 \\
    \hline
    \multicolumn{1}{c|}{\multirow{4}{*}{few-shot}} & 512 & \textbf{0.7927} & \textbf{0.5475} & \textbf{0.7196} \\
    \multicolumn{1}{c|}{} & 256 & 0.7917 & 0.5476 & 0.7098 \\
    \multicolumn{1}{c|}{} & 128 & 0.7897 & 0.5606 & 0.7099 \\
    \multicolumn{1}{c|}{} & 64 & 0.7901 & 0.5629 & 0.7099 \\
    \hline  
    \bottomrule          
\end{tabular}
}
\end{table}
```

## Table 9
```latex
\begin{table}[t]
    \caption{Ablation study w.r.t different distance metrics for ReLLa on MovieLens-1M dataset under both zero-shot and few-shot (<1\%) settings.
    }
    \vspace{-5pt}
    \label{tab:ablation distance}
    \resizebox{0.435\textwidth}{!}{
    \renewcommand\arraystretch{1.1}
    \begin{tabular}{c|c|ccc}
    \toprule
    \hline
    \multicolumn{1}{c|}{\multirow{2}{*}{Setting}} & \multicolumn{1}{c|}{\multirow{2}{*}{Distance}} & \multicolumn{3}{c}{MovieLens-1M} \\ 
    \multicolumn{1}{c|}{} & \multicolumn{1}{c|}{} & AUC & Log Loss & ACC \\
    \hline
    \multicolumn{1}{c|}{\multirow{3}{*}{zero-shot}} & Cosine & \textbf{0.7013} & \textbf{0.6250} & \textbf{0.6507} \\
    \multicolumn{1}{c|}{} & L2 & 0.6975 & 0.6356 & 0.6386 \\
    \multicolumn{1}{c|}{} & L1 & 0.6811 & 0.6388 & 0.6339 \\
    \hline
    \multicolumn{1}{c|}{\multirow{3}{*}{Few-shot}} & Cosine & \textbf{0.7927} & \textbf{0.5475} & \textbf{0.7196} \\
    \multicolumn{1}{c|}{} & L2 & 0.7872 & 0.5762 & 0.6944 \\
    \multicolumn{1}{c|}{} & L1 & 0.7833 & 0.5598 & 0.7119 \\
    \hline  
    \bottomrule          
\end{tabular}
}
\end{table}
```

## Table 10
```latex
\begin{table}[t]
    \caption{The averaged heterogeneity scores of two sequence types w.r.t. different length $K$.
    }
    \label{tab:heter score}
    \resizebox{0.48\textwidth}{!}{
    \renewcommand\arraystretch{1.1}
    \begin{tabular}{c|ccccccc}
    \toprule
    \hline
    \multicolumn{1}{c|}{\multirow{2}{*}{Seq. Type}} & \multicolumn{6}{c}{MovieLens-1M} \\ 
    \multicolumn{1}{c|}{} & K=5 & K=10 & K=15 & K=20 & K=25 & K=30 \\ 
   \hline 
   Top Recent (Origin) & 2.91 & 4.19 & 5.09 & 5.80 & 6.39 & 6.90 \\ 
   Top Relevant (Retrieval) & 2.44 & 3.37 & 4.01 & 4.51 & 4.94 & 5.32 \\
   \hline  
   \bottomrule          
\end{tabular}
}
\end{table}
```

