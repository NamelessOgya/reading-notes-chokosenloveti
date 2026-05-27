# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[b]
\setlength{\abovecaptionskip}{3pt}
\caption{Splits available in popular RS frameworks} \label{tab:frameworks}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lcccccccc}
\toprule
\multirow{2}{*}{\textbf{Split Type}} & Cornac    & DaisyRec  & Elliot    & FuxiCTR   & Recomdrs.  & RecBole   & RecPack   & RePlay    \\
 &
  {\small \cite{salah2020}} &
  {\small \cite{sun2023}} &
  {\small \cite{anelli2021}} &
  {\small \cite{Jieming2021}} &
  {\small \cite{Graham2019}} &
  {\small \cite{Zhao2021}} &
  {\small \cite{Michiels2022}} &
  {\small \cite{Vasilev2024}} \\ \midrule
LOO-based                             & \cmark & \cmark & \cmark & \xmark & \cmark & \cmark & \cmark & \cmark \\
GTS-based                            & \xmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
GTS + NIP                         & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \cmark & \xmark \\ \hline
\end{tabular}%
}
\end{table}
```

## Table 2
```latex
\begin{table}[t]
\setlength{\abovecaptionskip}{3pt}
\caption{Statistics of the datasets after preprocessing} \label{tab:dataset_stats}
\resizebox{0.9\columnwidth}{!}{%
    \centering
    \begin{tabular}{lrrrrrr}
    \toprule
        \textbf{Dataset} & \textbf{\#Interact.} & \textbf{\#Users} & \textbf{\#Items} & \textbf{Avg. Len.} & \textbf{Density (\%)} & \textbf{\#Days} \\ \midrule
        Beauty~\cite{mcauley2015imagebased} & 198 502 & 22 363 & 12 101 & 8.9 & 0.07 & 4 424 \\ 
        BeerAdv~\cite{mcauley2012beer} & 1 475 412 & 14 635 & 22 074 & 100.8 & 0.46 & 5 620 \\ 
        Diginetica\hyperref[digi]{\textsuperscript{\ref{digi}}} & 485 903 & 61 279 & 25 593 & 7.9 & 0.03 & 152 \\ 
        ML-1M~\cite{ml1} & 999 611 & 6 040 & 3 416 & 165.5 & 4.84 & 1 038 \\ 
        ML-20M~\cite{ml1}  & 19 984 024 & 138 493 & 18 345 & 144.3 & 0.79 & 7 385 \\ 
        Sports~\cite{mcauley2015imagebased} & 296 337 & 35 598 & 18 357 & 8.3 & 0.05 & 4 521 \\ 
        YooChoose~\cite{yooooo} & 2 792 229 & 335 203 & 20 758 & 8.3 & 0.04 & 181 \\ 
        Zvuk~\cite{shevchenko2024variability} & 8 087 953 & 19 267 & 150 206 & 419.8 & 0.28 & 91 \\ 
        \bottomrule
    \end{tabular}
    }
\end{table}
```

## Table 3
```latex
\begin{table}[t]
\setlength{\abovecaptionskip}{3pt}
\caption{Median delta $\delta$ (in seconds) between each target interaction and the previous one: for different (a) validation types on the validation, and (b) target options on the test set}
\label{tab:test_and_val_delta}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{llrrrrrrrr}
\toprule
\textbf{Set} & \textbf{Setup\tiny{ $\downarrow$}}   & {\small Beauty}    
  & {\small BeerAdv}   
  & {\small Diginetica} 
  & {\small ML-1M}     
  & {\small ML-20M}     
  & {\small Sports}     
  & {\small YooChoose} 
  & {\small Zvuk}     \\ \midrule
Full Data & $-$ & 345,600 & 73,182 & 58 & 0 & 11 & 172,800 & 59 & 14  \\ 
\midrule
\multirow{4}{*}{(a) Valid} & LOO   & 172,800   & 360,900 & 63 & 18 & 17 & 86,400    & 59 & 98  \\
                       & GT Last    & 1,036,800 & 446,371 & 71 & 27 & 41 & 1,209,600 & 67 & 84  \\
                       & UB    &   604,800 & 691,188 & 70 & 15 & 19 &   518,400 & 65 & 78  \\
                       & LTI   &   604,800 & 690,794 & 70 & 15 & 21 &   518,400 & 65 & 68  \\ \midrule
\multirow{5}{*}{(b) Test}  & LOO   &   604,800 & 737,140 & 70 & 17 & 20 &   518,400 & 65 & 73  \\
                       & Last  & 1,382,400 & 508,452 & 70 & 67 & 29 & 1,296,000 & 68 & 91  \\
                       & First & 8,640,000 & 4,921,729 & 186 & 7,153,214 & 21,145,894 & 11,577,600 & 259 & 346,010 \\
                       & Rand. & 3,628,800 &   439,805 & 65 & 35 & 15 &   4,752,000 & 62 & 120 \\
                       & Succ. &   172,800 &    75,916 & 58 & 22 & 14 &      86,400 & 60 & 67  \\ \bottomrule
\end{tabular}%
}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
\setlength{\abovecaptionskip}{4pt}
\setlength{\abovecaptionskip}{3pt}
\caption{Test subset statistics for GTS for different quantiles} \label{tab:test_quant}
\resizebox{1\columnwidth}{!}{%
    \centering
\begin{tabular}{l|lrrrr|lrrrr|rrrrr}
\toprule
\multirow{2}{*}{\textbf{Dataset}} &
  \textbf{Len.} &
  \multicolumn{4}{c|}{\textbf{Holdout Len.}} &
  \multicolumn{5}{c|}{\textbf{\#Users (K)}} &
  \multicolumn{5}{c}{\textbf{\#Days}} \\ \cline{2-16} 
 &
  \textit{Full} &
  $q_{0.8}$ &
  $q_{0.9}$ &
  $q_{0.95}$ &
  $q_{0.975}$ &
  \textit{Full} &
  $q_{0.8}$ &
  $q_{0.9}$ &
  $q_{0.95}$ &
  $q_{0.975}$ &
  \textit{Full} &
  $q_{0.8}$ &
  $q_{0.9}$ &
  $q_{0.95}$ &
  $q_{0.975}$ \\ 
\midrule
Beauty     &  8.88  & 3.88  & 3.25  & 2.76  & 2.45  & 22.4 & 10.2 & 6.11  & 3.52  & 1.91  & 4,424 & 138 & 71 & 35 & 19 \\
BeerAdv    & 101    & 42.5  & 28.8  & 18.7  & 12.0  & 14.6 & 6.94  & 5.12  & 3.94  & 3.07  & 5,620 & 354 & 183 & 94 & 48 \\
Diginetica &  7.93  & 7.68  & 7.66  & 7.38  & 6.55  & 61.3 & 12.7 & 6.35  & 3.29  & 1.86  &   152 &  20 & 9  & 4  & 2  \\
ML-1M      & 166    & 112   & 82.7  & 61.5  & 45.6  &  6.04 & 1.78  & 1.21  & 0.81  & 0.55  & 1,038 & 818 & 790 & 617 & 400 \\
ML-20M     & 144    & 126   & 108   & 92.8  & 86.9  &139 & 31.7 & 18.6 & 10.8 & 5.75  & 7,385 &1,994&1,100& 569 & 201 \\
Sports     &  8.32  & 3.52  & 2.89  & 2.61  & 2.60  & 35.6 & 16.7 & 10.2 & 5.63  & 2.79  & 4,521 & 163 & 88 & 43 & 22 \\
YooChoose  &  8.33  & 8.49  & 8.55  & 8.57  & 8.79  &335 & 65.8 & 32.7 & 16.3 & 7.94  &   181 &  34 & 17 & 10 & 5  \\
Zvuk       & 420    & 150   & 95.9  & 61.6  & 42.8  & 19.3 & 10.8 & 8.43  & 6.57  & 4.73  &    91 &  16 & 8  & 4  & 2  \\ 
\bottomrule
\end{tabular}%
}
\end{table}
```

## Table 5
```latex
\begin{table}[t]
% \setlength{\abovecaptionskip}{3pt}
% \caption{Test subset statistics for GTS for different quantiles} \label{tab:test_quant}
% \resizebox{1\columnwidth}{!}{%
% \centering
% \begin{tabular}{@{}l|lrrrr|lrrrr|lrrrr@{}}
% \toprule
% \multirow{2}{*}{\textbf{Dataset}} &
%   \textbf{Len.} &
%   \multicolumn{4}{c|}{\textbf{Holdout Len.}} &
%   \multicolumn{5}{c|}{\textbf{\#Users}} &
%   \multicolumn{5}{c}{\textbf{\#Days}} \\ \cline{2-16} 
%  &
%   \textit{Full} &
%   $q_{0.8}$ &
%   $q_{0.9}$ &
%   $q_{0.95}$ &
%   $q_{0.975}$ &
%   \textit{Full} &
%   $q_{0.8}$ &
%   $q_{0.9}$ &
%   $q_{0.95}$ &
%   $q_{0.975}$ &
%   \textit{Full} &
%   $q_{0.8}$ &
%   $q_{0.9}$ &
%   $q_{0.95}$ &
%   $q_{0.975}$ \\ 
% \midrule \midrule
% Beauty &  
%   8.88 & 3.88 & 3.25 & 2.76 & 2.45 & 22.4k & 10.2k & 6.1k & 3.5k & 1.9k & 4.4k & 138  & 71  & 35  & 19  \\
% BeerAdv &  
%   100.8 & 42.5 & 28.8 & 18.7 & 12.0 & 14.6k & 6.9k  & 5.1k & 3.9k & 3.1k & 5.6k & 354  & 183 & 94  & 48  \\
% Diginetica &  
%   7.93 & 7.68 & 7.66 & 7.38 & 6.55 & 61.3k & 12.7k & 6.3k & 3.3k & 1.9k & 152  & 20  & 9   & 4   & 2   \\
% ML-1M &  
%   165.5 & 112.1 & 82.7 & 61.5 & 45.6 & 6.0k  & 1.8k  & 1.2k & 813  & 548  & 1.0k & 818 & 790 & 617 & 400 \\
% ML-20M &  
%   144.3 & 125.9 & 107.7 & 92.8 & 86.9 & 138.5k & 31.7k & 18.6k & 10.8k & 5.8k & 7.4k & 2.0k & 1.1k & 569 & 201 \\
% Sports &  
%   8.32 & 3.52 & 2.89 & 2.61 & 2.60 & 35.6k & 16.7k & 10.2k & 5.6k & 2.8k & 4.5k & 163 & 88  & 43  & 22  \\
% YooChoose &  
%   8.33 & 8.49 & 8.55 & 8.57 & 8.79 & 335.2k & 65.8k & 32.7k & 16.3k & 7.9k & 181  & 34  & 17  & 10  & 5   \\
% Zvuk &  
%   419.8 & 149.6 & 95.9 & 61.6 & 42.8 & 19.3k & 10.8k & 8.4k  & 6.6k & 4.7k & 91   & 16  & 8   & 4   & 2   \\
% \bottomrule
% \end{tabular}%
% }
% \end{table}
```

## Table 6
```latex
\begin{table}[]
\setlength{\abovecaptionskip}{4pt}
\caption{Mean (across datasets) correlations between test and validation metrics for GTS with (a) \textnormal{\emph{Last}} and (b) \textnormal{\emph{Successive}} test targets and different validation types. Best values are in bold, second best are underlined.}
\label{tab:validation_corr_successive}
\resizebox{1\columnwidth}{!}{%
    \centering
    \begin{tabular}{ll|ccc|ccc}
    \toprule
    \multicolumn{2}{l|}{\textbf{Correlation}} & \multicolumn{3}{c|}{\textbf{Kendall}} & \multicolumn{3}{c}{\textbf{Spearman}} \\ \hline
    \textbf{Target} & \textbf{Valid. Type\tiny{$\downarrow$}} & {\small HR@10} & {\small MRR@10} & {\small NDCG@10} & {\small HR@10} & {\small MRR@10} & {\small NDCG@10} \\ 
    \midrule
    \multirow{7}{*}{(a) Test Last}   & UB            & 0.72 & 0.72 & 0.74 & 0.87 & 0.88 & 0.89 \\
                                     & LTI           & 0.73 & 0.75 & 0.75 & 0.88 & 0.90 & 0.90 \\
                                     & GT Last       & \textbf{0.78} & \textbf{0.79} & \textbf{0.79} & \textbf{0.93} & \textbf{0.93} & \textbf{0.93} \\
                                     & GT First      & 0.61 & 0.54 & 0.57 & 0.77 & 0.69 & 0.73 \\
                                     & GT Rand.     & 0.75 & 0.75 & 0.76 & 0.90 & 0.91 & \underline{0.92} \\
                                     & GT Sucv. & \underline{0.76} & \underline{0.77} & \underline{0.77} & \underline{0.91} & \underline{0.92} & \underline{0.92} \\
                                     & GT All        & 0.46 & 0.37 & 0.43 & 0.59 & 0.50 & 0.56 \\
    \midrule
    \multirow{7}{*}{(b) Test Sucv.}  & UB            & 0.78 & 0.78 & 0.80 & 0.93 & 0.92 & \underline{0.94} \\
                                     & LTI           & 0.80 & \textbf{0.83} & \underline{0.82} & \underline{0.94} & \textbf{0.95} & \textbf{0.95} \\
                                     & GT Last       & \underline{0.81} & \underline{0.81} & \underline{0.82} & \underline{0.94} & \underline{0.94} & \textbf{0.95} \\
                                     & GT First      & 0.64 & 0.56 & 0.59 & 0.80 & 0.72 & 0.75 \\
                                     & GT Rand.     & 0.80 & \underline{0.81} & 0.81 & \underline{0.94} & \underline{0.94} & \underline{0.94} \\
                                     & GT Sucv. & \textbf{0.83} & \textbf{0.83} & \textbf{0.83} & \textbf{0.95} & \textbf{0.95} & \textbf{0.95} \\
                                     & GT All        & 0.48 & 0.37 & 0.44 & 0.60 & 0.49 & 0.56 \\
    \bottomrule
    \end{tabular}%
}
\end{table}
```

## Table 7
```latex
\begin{table}[t!]
\setlength{\abovecaptionskip}{3pt}
\caption{Holdout statistics for different splits ($q_{0.9}$ for GTS)} \label{tab:valid_test_stats}
\resizebox{1\columnwidth}{!}{%
    \centering
\begin{tabular}{p{1cm}llrrrrrrrr}
\toprule
\multicolumn{1}{c}{\textbf{Set}} & \textbf{Split} & \textbf{Stats.\tiny{ $\downarrow$}} & 
{\small Beauty}    
  & {\small BeerAdv}   
  & {\small Diginetica} 
  & {\small ML-1M}     
  & {\small ML-20M}     
  & {\small Sports}     
  & {\small YooChoose} 
  & {\small Zvuk}     \\ \midrule 
\multirow{4}{*}{\parbox{1cm}{\centering Full\\Data}} & \multirow{4}{*}{$-$} & \#Days          & 4,424  & 5,620  & 152   & 1,038 & 7,385   & 4,521  & 181    & 91    
\\
                           &                      & Lifetime (\%)        & 12.4 & 11.56 & 0.01 & 9.14 & 2.66 & 12.0 & 0.01 & 43.47   \\
                           &                      & \#Users         & 22,363 & 14,635 & 61,279 & 6,040 & 138,493 & 35,598 & 335,203 & 19,267 \\
                           &                      & Seq. Len.       & 8.88  & 101   & 7.93  & 166  & 144    & 8.32  & 8.33   & 420   \\ 
                           
                           \midrule
\multicolumn{1}{c}{\multirow{9}{*}{Valid}}    & \multirow{2}{*}{LOO} & \#Days (\%)     & 84.0  & 66.9  & 100   & 100  & 94.7   & 69.4  & 100    & 100   \\
                           &                      & \#Users (\%)    & 100   & 100   & 100   & 100  & 100    & 100   & 100    & 100   \\ \cmidrule{2-11} 
                           & \multirow{3}{*}{GT}  & \#Days (\%)     & 1.38  & 2.76  & 6.58  & 2.41 & 10.9   & 1.50  & 8.29   & 7.69  \\
                           &                      & \#Users (\%)    & 28.0  & 35.4  & 9.55  & 17.3 & 11.9   & 27.2  & 8.87   & 41.7  \\
                           &                      & Holdout Len. & 2.84  & 25.6  & 7.47  & 86.0 & 109    & 2.73  & 8.45   & 90.7  \\ \cmidrule(l){2-11}
                           & \multirow{2}{*}{UB}  & \#Days (\%)     & 45.6  & 57.3  & 90.1  & 23.8 & 79.3   & 41.2  & 90.6   & 91.2  \\
                           &                      & \#Users (\%)    & 4.58  & 7.00  & 1.67  & 17.0 & 0.74   & 2.88  & 0.31   & 5.31  \\ \cmidrule(l){2-11}
                           & \multirow{2}{*}{LTI} & \#Days (\%)     & 82.4  & 63.7  & 94.1  & 23.8 & 79.6   & 66.1  & 90.6   & 91.2  \\
                           &                      & \#Users (\%)    & 96.0  & 94.0  & 90.0  & 99.5 & 90.2   & 96.1  & 90.3   & 95.6  \\ \midrule
\multicolumn{1}{c}{\multirow{5}{*}{Test}}      & \multirow{2}{*}{LOO} & \#Days (\%)     & 84.0  & 66.9  & 100   & 100  & 94.5   & 68.1  & 100    & 100   \\
                           &                      & \#Users (\%)    & 100   & 100   & 100   & 100  & 100    & 100   & 100    & 100   \\ \cmidrule{2-11} 
                           & \multirow{3}{*}{GTS} & \#Days (\%)     & 1.60  & 3.26  & 5.92  & 76.1 & 14.9   & 1.95  & 9.39   & 8.79  \\
                           &                      & \#Users (\%)    & 27.3  & 35.0  & 10.4  & 20.0 & 13.4   & 28.7  & 9.74   & 43.8  \\
                           &                      & Holdout Len. & 3.25  & 28.8  & 7.66  & 82.7 & 108    & 2.89  & 8.55   & 95.9  \\ \bottomrule
\end{tabular}%
}
\end{table}
```

## Table 8
```latex
\begin{table}[t!]
\setlength{\abovecaptionskip}{4pt}
\caption{Mean (across datasets) correlations between test GTS Successive target and other options for different metrics. Best values are in bold, second best are underlined.}
\label{tab:test_vs_test_corr}
\resizebox{0.9\columnwidth}{!}{%
    \centering
    \begin{tabular}{lcccccc}
    \hline
    \multirow{2}{*}{\textbf{Test Split}} & \multicolumn{3}{c}{\textbf{Kendall}} & \multicolumn{3}{c}{\textbf{Spearman}} \\ 
    \cmidrule(lr){2-4} \cmidrule(lr){5-7}
    & HR@10 & MRR@10 & NDCG@10 & HR@10 & MRR@10 & NDCG@10 \\ 
    \hline
    LOO       & 0.71      & 0.70       & 0.71        & 0.87       & 0.86        & 0.87        \\
    GTS Last   & \underline{0.83} & \underline{0.82}  & \underline{0.83}   & \underline{0.93}  & \underline{0.94}   & \underline{0.94}   \\
    GTS First  & 0.70      & 0.60       & 0.62        & 0.82       & 0.70        & 0.72        \\
    GTS Random & \textbf{0.91} & \textbf{0.90} & \textbf{0.91} & \textbf{0.98} & \textbf{0.98} & \textbf{0.98} \\
    GTS All    & 0.57      & 0.37       & 0.43        & 0.68       & 0.46        & 0.53        \\
    \hline
    \end{tabular}
}
\end{table}
```

## Table 9
```latex
\begin{table}[t]
\setlength{\abovecaptionskip}{4pt}
\caption{Validation and test NDCG@10 of SASRec$^+$ at optimal validation configuration for different splits.
\textnormal{\emph{Test R.}} denotes setup with retraining on combined training and validation data.
\textnormal{\emph{LTI}} and \textnormal{\emph{UB}} in this study use only \textnormal{\emph{Last}} validation target. 
}
\label{tab:retrain}
\resizebox{0.93\columnwidth}{!}{%
\begin{tabular}{ll|cccr|cccr}
\toprule
\multicolumn{2}{l|}{\textbf{Dataset}}       & \multicolumn{4}{c|}{Diginetica}        & \multicolumn{4}{c}{Amazon Beauty}      \\ 
\hline
\textbf{Split} & \textbf{Target\tiny{ $\downarrow$}} & \textbf{Valid} & \textbf{Test} & \textbf{Test R.} & \textbf{$\Delta$ Test} & \textbf{Valid} & \textbf{Test} & \textbf{Test R.} & \textbf{$\Delta$ Test} \\ 
\midrule 
\multirow{2}{*}{GT} 
  & Last & 0.154 & 0.154 & 0.161 & 4.55\%  & 0.046 & 0.024 & 0.037 & 54.2\% \\
  & Sucv. & 0.154 & 0.149 & 0.160 & 7.38\%  & 0.044 & 0.022 & 0.040 & 81.8\% \\ 
\midrule
\multirow{2}{*}{UB}  
  & Last & 0.180 & 0.152 & 0.155 & 1.97\%   & 0.074 & 0.036 & 0.037 & 2.78\% \\
  & Sucv. &   –   & 0.159 & 0.158 & -0.63\% &   –   & 0.040 & 0.040 & 0.00\% \\ 
\midrule
\multirow{2}{*}{LTI} 
  & Last & 0.187 & 0.135 & 0.126 & -6.67\%  & 0.067 & 0.031 & 0.036 & 16.1\% \\
  & Sucv. &   –   & 0.147 & 0.129 & -12.2\%  &   –   & 0.036 & 0.039 & 8.33\% \\ 
\midrule 
LOO                  
  & Last & 0.179 & 0.181 & 0.157 & -13.3\% & 0.073 & 0.059 & 0.065 & 10.2\% \\ 
\bottomrule
\end{tabular}%
}
\end{table}
```

