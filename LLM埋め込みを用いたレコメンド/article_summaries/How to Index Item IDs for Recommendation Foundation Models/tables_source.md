# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\vspace{-10pt}
    \centering
    \begin{tabular}{lcccc}
    \toprule
     & $\#$User & $\#$Item & $\#$Interactions & Sparsity($\%$) \\
     \hline
    Sports & 35,598 & 18,357 & 296,337 & 0.0453\\
    \hline
    Beauty & 22,363 & 12,101 & 198,502 & 0.0734 \\
    \hline 
    Yelp & 30,431 & 20,033 & 316,354 & 0.0519\\
    \bottomrule
\end{tabular}
\caption{Basic statistics of datasets}
\label{tab:datasets}
\vspace{-20pt}
\end{table}
```

## Table 2
```latex
\begin{table*}[t]
    \centering
    \setlength{\tabcolsep}{1.5pt}
    \begin{tabular}{lcccccccccccc}
    \toprule
        \multirow{2}{*}{Method} & \multicolumn{4}{c}{\textbf{Amazon Sports}} & \multicolumn{4}{c}{\textbf{Amazon Beauty}} & \multicolumn{4}{c}{\textbf{Yelp}}\\
        \cmidrule(lr){2-5} \cmidrule(lr){6-9} \cmidrule(lr){10-13}
         & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 \\
        \midrule
        SASRec & 0.0233 & \uwave{0.0154} & 0.0350 & 0.0192 & 0.0387 & \uwave{0.0249} & 0.0605 & 0.0318 & 0.0170 & 0.0110 & 0.0284 & 0.0147 \\
        S$^3$\text{-Rec} & \uwave{0.0251} & \textbf{0.0161} & \uwave{0.0385} & \textbf{0.0204} & \uwave{0.0387} & 0.0244 & \textbf{0.0647} & \uwave{0.0327} & 0.0201 & 0.0123 & \uwave{0.0341} & 0.0168 \\
        \midrule
        RID & 0.0208 & 0.0122 & 0.0288 & 0.0153 & 0.0213 & 0.0178 & 0.0479 & 0.0277 & \uwave{0.0225} & \textbf{0.0159} & 0.0329 & \uwave{0.0193}\\
        TID & 0.0000 & 0.0000 & 0.0000 & 0.0000 & 0.0182 & 0.0132 & 0.0432 & 0.0254 & 0.0058 & 0.0040 & 0.0086 & 0.0049\\
        IID & \textbf{0.0268} & 0.0151 & \textbf{0.0386} & \uwave{0.0195} & \textbf{0.0394} & \textbf{0.0268} & \uwave{0.0615} & \textbf{0.0341} & \textbf{0.0232} & \uwave{0.0146} & \textbf{0.0393} & \textbf{0.0197}\\
        \bottomrule
    \end{tabular}
    \caption{Performances of the trivial indexing methods for P5 as well as the baselines. The numbers in bold represent the best results, while the numbers with a wave represent the second-best results. The results for RID and TID are significantly worse on Sports and Beauty, with a $p$-value < 0.05 under the paired Student's t-test protocol.}
    \label{tab:basic}
    \vspace{-15pt}
\end{table*}
```

## Table 3
```latex
\begin{table*}[t]
    \centering
    \begin{tabular}{lcccccccccccc}
    \toprule
    \multicolumn{11}{c}{\textbf{Training Sequence}} & \textbf{Validation} & \textbf{Testing}\\
    \hline
    User 1 & 1001 & 1002 & 1003 & 1004 & 1005 & 1006 & 1007 & 1008 & 1009 & ~ & 1018 & 1019\\ \cline{4-4}  \cline{6-7}
    User 2 & 1010 & 1011 & \multicolumn{1}{|c}{1001} & \multicolumn{1}{|c}{1012} & \multicolumn{1}{|c}{1008} & 1009 & \multicolumn{1}{|c}{1013} & 1014 & ~ & ~ & 1022 & 1023\\\cline{4-7} \cline{10-10}
    User 3 & 1015 & 1016 & 1017 & \multicolumn{1}{|c}{1007} & \multicolumn{1}{|c}{1018} & 1019 & 1020 & 1021 & \multicolumn{1}{|c}{1009} & \multicolumn{1}{|c}{~} & 1015 & 1016\\ \cline{4-6} \cline{10-10}
    User 4 & 1022 & 1023 & \multicolumn{1}{|c}{1005} & 1002 & 1006 & \multicolumn{1}{|c}{1024} & ~ & ~ & ~ & ~ & 1002 & 1008\\ \cline{4-6} \cline{8-10}
    User 5 & 1025 & 1026 & 1027 & 1028 & 1029 & 1030 & \multicolumn{1}{|c}{1024} & {1020} & {1021} & \multicolumn{1}{|c}{1031} & 1033 & 1034\\ \cline{8-10}
    \bottomrule
    \end{tabular}
    \caption{An illustration of Sequential Indexing method. Numbers in boxes represent previously indexed items.}
    \label{tab:sequential_graph}
    \vspace{-20pt}
\end{table*}
```

## Table 4
```latex
\begin{table*}[t]
    \centering
    % \small
    \setlength{\tabcolsep}{2pt}
    % \resizebox{\linewidth}{!}{
    \begin{tabular}{lcccccccccccc}
    \toprule
        \multirow{2}{*}{Method} & \multicolumn{4}{c}{\textbf{Amazon Sports}} & \multicolumn{4}{c}{\textbf{Amazon Beauty}} & \multicolumn{4}{c}{\textbf{Yelp}}\\
        \cmidrule(lr){2-5} \cmidrule(lr){6-9} \cmidrule(lr){10-13}
         & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 \\
        \midrule
        Caser & 0.0116 & 0.0072 & 0.0194 & 0.0097 & 0.0205 & 0.0131 & 0.0347 & 0.0176 & 0.015 & 0.0099 & 0.0263 & 0.0134 \\
        HGN & 0.0189 & 0.0120 & 0.0313 & 0.0159 & 0.0325 & 0.0206 & 0.0512 & 0.0266 & 0.0186 & 0.0115 & 0.0326 & 0.159 \\
        GRU4Rec & 0.0129 & 0.0086 & 0.0204 & 0.0110 & 0.0164 & 0.0099 & 0.0283 & 0.0137 & 0.0176 & 0.0110 & 0.0285 & 0.0145 \\
        BERT4Rec & 0.0115 & 0.0075 & 0.0191 & 0.0099 & 0.0203 & 0.0124 & 0.0347 & 0.0170 & 0.0051 & 0.0033 & 0.0090 & 0.0090 \\
        FDSA & 0.0182 & 0.0122 & 0.0288 & 0.0156 & 0.0267 & 0.0163 & 0.0407 & 0.0208 & 0.0158 & 0.0098 & 0.0276 & 0.0136 \\
        SASRec & 0.0233 & 0.0154 & 0.0350 & 0.0192 & 0.0387 & 0.0249 & 0.0605 & 0.0318 & 0.0170 & 0.0110 & 0.0284 & 0.0147 \\
        S$^3$\text{-Rec} & 0.0251 & 0.0161 & 0.0385 & 0.0204 & 0.0387 & 0.0244 & 0.0647 & 0.0327 & 0.0201 & 0.0123 & 0.0341 & 0.0168 \\
        \midrule
        RID & 0.0208 & 0.0122 & 0.0288 & 0.0153 & 0.0213 & 0.0178 & 0.0479 & 0.0277  & \underline{0.0225} & \underline{0.0159} & 0.0329 & \underline{0.0193}\\
        TID & 0.000 & 0.000 & 0.000 & 0.000 & 0.0182 & 0.0132 & 0.0432 & 0.0254 & 0.0058 & 0.0040 & 0.0086 & 0.0049\\
        IID & \underline{0.0268} & 0.0151 & \underline{0.0386} & 0.0195 & \underline{0.0394} & \underline{0.0268} & 0.0615 & \underline{0.0341} & \underline{0.0232} & \underline{0.0146} & \underline{0.0393} & \underline{0.0197}\\
        \midrule
        SID & \underline{0.0264} & \underline{0.0186} & 0.0358 & \underline{0.0216} & \underline{0.0430} & \underline{0.0288} & 0.0602 & \underline{0.0368} & \textbf{0.0346} & \textbf{0.0242} & \textbf{0.0486} & \textbf{0.0287}\\
        CID & \uwave{0.0313} & \uwave{0.0224} & \uwave{0.0431} & \uwave{0.0262} & \underline{0.0489} & \underline{0.0318} & \underline{0.0680} & \underline{0.0357} & \underline{0.0261} & \underline{0.0171} & \underline{0.0428} & \underline{0.0225}\\
        SemID & \underline{0.0274} & \underline{0.0193} & \underline{0.0406} & \underline{0.0235} & \underline{0.0433} & \underline{0.0299} & \underline{0.0652} & \underline{0.0370} & \underline{0.0202} & \underline{0.0131} & 0.0324 & \underline{0.0170}\\
        \midrule
        SID+IID & 0.0235 & 0.0161 & 0.0339 & 0.0195 & \underline{0.0420} & \underline{0.0297} & 0.0603 & \underline{0.0355} & \uwave{0.0329} & \uwave{0.0236} & \underline{0.0465} & \uwave{0.0280}\\
        CID+IID & \textbf{0.0321} & \textbf{0.0227} & \textbf{0.0456} & \textbf{0.0270} & \textbf{0.0512} & \textbf{0.0356} & \textbf{0.0732} & \textbf{0.0427} & \underline{0.0287} & \underline{0.0195} & \uwave{0.0468} & \underline{0.0254}\\
        SemID+IID & \underline{0.0291} & \underline{0.0196} & \underline{0.0436} & \underline{0.0242} & \uwave{0.0501} & \uwave{0.0344} & \uwave{0.0724} & \uwave{0.0411} & \underline{0.0229} & \underline{0.0150} & \underline{0.0382} & \underline{0.0199}\\
        SemID+CID & 0.0043 & 0.0031 & 0.0070 & 0.0039 & 0.0355 & 0.0248 & 0.0545 & 0.0310 & 0.0021 & 0.0016 & 0.0056 & 0.0029\\
        \bottomrule
    \end{tabular}
    % }
    \caption{Performance of all baseline results and all indexing methods under P5. Numbers in bold represent the best results, numbers with a wavy underline represent the second-best results, and numbers with a straight underline indicate that they are better than the best baseline result. Results better than baselines here have been tested to be significant under the paired Student's t-test protocol with $p$-value $<0.05$.}
    \label{tab:main}
    \vspace{-20pt}
\end{table*}
```

## Table 5
```latex
\begin{table*}[t]
    \centering
    % \small
    \setlength{\tabcolsep}{2pt}
    % \resizebox{\linewidth}{!}{
    \begin{tabular}{lcccccccccccc}
    \toprule
        \multirow{2}{*}{Method} & \multicolumn{4}{c}{\textbf{Amazon Sports}} & \multicolumn{4}{c}{\textbf{Amazon Beauty}} & \multicolumn{4}{c}{\textbf{Yelp}}\\
        \cmidrule(lr){2-5} \cmidrule(lr){6-9} \cmidrule(lr){10-13}
         & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 \\
        \midrule
        SASRec & 0.0233 & 0.0154 & 0.0350 & 0.0192 & 0.0387 & 0.0249 & 0.0605 & 0.0318 & 0.0170 & 0.0110 & 0.0284 & 0.0147 \\
        S$^3$\text{-Rec} & 0.0251 & 0.0161 & \uwave{0.0385} & 0.0204 & 0.0387 & 0.0244 & \textbf{0.0647} & 0.0327 & 0.0201 & 0.0123 & 0.0341 & 0.0168 \\
        \midrule
        SID-TSO & \uwave{0.0264} & \uwave{0.0186} & 0.0358 & \uwave{0.0216} & \textbf{0.0430} & \textbf{0.0288} & \uwave{0.0602} & \textbf{0.0368} & \textbf{0.0346} & \textbf{0.0242} & \textbf{0.0486} & \textbf{0.0287}\\
        SID-RO & 0.0214 & 0.0150 & 0.0291 & 0.0175 & 0.0392 & 0.0257 & 0.0512 & 0.0335 & 0.0324 & 0.0219 & 0.0461 & 0.0263\\
        SID-S2LO & \textbf{0.0304} & \textbf{0.0230} & \textbf{0.0395} & \textbf{0.0259} & 0.0395 & 0.0259 & 0.0520 & 0.0337 & \uwave{0.0335} & \uwave{0.0237} & 0.0442 & \uwave{0.0277}\\
        SID-L2SO & 0.0244 & 0.0176 & 0.0356 & 0.0209 & \uwave{0.0409} & \uwave{0.0286} & 0.0586 & \uwave{0.0343} & 0.0316 & 0.0215 & \uwave{0.0472} & 0.0265 \\
        \bottomrule
    \end{tabular}
    % }
    \caption{Different settings of Sequential Indexing for P5 compared with two baselines on three datasets. The numbers in bold represent the best results, while the numbers with a wave represent the second-best results. TSO results in Amazon Beauty and Yelp are tested to be significant with respect to other settings.}
    \label{tab:sequential}
    \vspace{-15pt}
\end{table*}
```

## Table 6
```latex
\begin{table}[t] % Adding the table environment
\setlength{\tabcolsep}{4pt}
      \begin{tabular}{l|c|c|c|c|c|c}
          \toprule
          \textbf{Dataset} & \multicolumn{2}{c|}{\textbf{Sports}} & \multicolumn{2}{c|}{\textbf{Beauty}} & \multicolumn{2}{c}{\textbf{Yelp}}\\
          \midrule
          SASRec & \multicolumn{2}{c|}{0.0350}& \multicolumn{2}{c|}{0.0605} & \multicolumn{2}{c}{0.0284}  \\
          S$^3$\text{-Rec} & \multicolumn{2}{c|}{0.0385} & \multicolumn{2}{c|}{0.0647} & \multicolumn{2}{c}{0.0341} \\
          \midrule
           & $N$ = 10 & $N$ = 20 & $N$ = 10 & $N$ = 20 & $N$ = 10 & $N$ = 20 \\
           \hline
          $k$=200  & 0.0302 & 0.0423 & 0.0566 & 0.0635 & \uwave{0.0416} & \textbf{0.0428}\\
          $k$=500  & 0.0400 & \uwave{0.0431} & \textbf{0.0680} & \uwave{0.0668}  & 0.0388 & 0.0403\\
          $k$=1000  & \textbf{0.0435} & 0.0416 & 0.0658 & 0.0638 & 0.0385 & 0.0388 \\
          \bottomrule
      \end{tabular}
      % \vspace{8pt}
      \caption{CID hit@10 results under different parameters and datasets. Bold numbers are best results and under-wave numbers are second-best results. The highest scored settings in all datasets are tested to be significant with respect to other settings under the paired Student's t-test with $p$-value < 0.05.} % Caption now starts with "Table"
      \label{tab:CF}
      \vspace{-20pt}
\end{table}
```

## Table 7
```latex
\begin{table}[t] % Adding the table environment
\setlength{\tabcolsep}{4pt}
      \begin{tabular}{l|c|c|c|c|c|c}
        \toprule
        \textbf{Dataset} & \multicolumn{2}{c|}{\textbf{Sports}} & \multicolumn{2}{c|}{\textbf{Beauty}} & \multicolumn{2}{c}{\textbf{Yelp}}\\
        \midrule
         & $N$ = 10 & $N$ = 20 & $N$ = 10 & $N$ = 20 & $N$ = 10 & $N$ = 20 \\
         \hline
        $k$=200  & 4.25 & 3.35 & 4.31 & 3.23 & \uwave{3.88} & \textbf{3.25} \\
        $k$=500  & 3.66 & \uwave{3.66} & \textbf{3.80} & \uwave{2.94} & 3.57 & 2.91 \\
        $k$=1000  & \textbf{3.31} & 2.78 & 3.54 & 3.54 & 3.21 & 2.76 \\
        \bottomrule
      \end{tabular}
      % \vspace{5pt}
      \caption{Average ID lengths under different parameters. Bold numbers in this table correspond to the best results in Table \ref{tab:CF} (i.e., bold numbers in Table \ref{tab:CF}).} % Caption now starts with "Table"
      \label{tab:CF_length}
      \vspace{-20pt}
\end{table}
```

## Table 8
```latex
\begin{table*}[t]
    \centering
    \begin{tabular}{l|l}
    \toprule
        Beauty > Skin Care > \textbf{Eyes} > Combinations & Beauty > Skin Care > Eyes > \textbf{Creams} \\
        Beauty > Makeup > Makeup Remover > \textbf{Eyes} & Beauty > Makeup > Body > Moisturizers > \textbf{Creams} \\
        \bottomrule
    \end{tabular}
    \caption{Examples of non-tree structure categories in Amazon Beauty dataset.}
    \vspace{-15pt}
    \label{tab:nontree}
\end{table*}
```

## Table 9
```latex
\begin{table*}[t]
    \centering
    % \small
    \setlength{\tabcolsep}{1.5pt}
    \resizebox{\linewidth}{!}{
    \begin{tabular}{lcccccccccccc}
    \toprule
        \multirow{2}{*}{Method} & \multicolumn{4}{c}{\textbf{Amazon Sports}} & \multicolumn{4}{c}{\textbf{Amazon Beauty}} & \multicolumn{4}{c}{\textbf{Yelp}}\\
        \cmidrule(lr){2-5} \cmidrule(lr){6-9} \cmidrule(lr){10-13}
         & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 & HR@5 & NCDG@5 & HR@10 & NCDG@10 \\
        \midrule
        SASRec & 0.0233 & 0.0154 & 0.0350 & 0.0192 & 0.0387 & 0.0249 & 0.0605 & 0.0318 & 0.0170 & 0.0110 & 0.0284 & 0.0147 \\
        S$^3$\text{-Rec} & 0.0251 & 0.0161 & 0.0385 & 0.0204 & 0.0387 & 0.0244 & 0.0647 & 0.0327 & \uwave{0.0201} & \uwave{0.0123} & \textbf{0.0341} & \uwave{0.0168} \\
        \midrule
        SemID-non-tree & \textbf{0.0281} & \uwave{0.0192} & \textbf{0.0410} & \uwave{0.0233} & \uwave{0.0423} & \uwave{0.0288} & \uwave{0.0632} & \uwave{0.0354} & 0.0028 & 0.0019 & 0.0050 & 0.0025 \\
        SemID-tree & \uwave{0.0274} & \textbf{0.0193} & \uwave{0.0406} & \textbf{0.0235} & \textbf{0.0433} & \textbf{0.0299} & \textbf{0.0652} & \textbf{0.0370} & \textbf{0.0202} & \textbf{0.0131} & \uwave{0.0324} & \textbf{0.0170} \\
        \bottomrule
    \end{tabular}
    }
    \caption{SemID results under different settings. Bold numbers are best results and under-wave numbers are second-best. Tree setting results in Amazon Beauty and Yelp are tested to be significant with respect to non-tree setting.}
    \label{tab:semantics}
    \vspace{-15pt}
\end{table*}
```

