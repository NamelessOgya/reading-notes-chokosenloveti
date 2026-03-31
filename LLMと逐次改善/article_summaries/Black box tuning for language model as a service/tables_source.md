# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t!]
\centering
\caption{Statistics, manual templates, and label words used in our experiments. $\mid\mathcal{Y}\mid$: number of classes.}
\label{tab:data}
\resizebox{\linewidth}{!}{
\begin{tabular}{llcrrcll}
\toprule
\textbf{Category} & \textbf{Dataset} & \textbf{$\mid\mathcal{Y}\mid$} & \textbf{$\mid$Train$\mid$} & \textbf{$\mid$Test$\mid$} & \textbf{Type} & \textbf{Template} & \textbf{Label words} \\ \midrule
\multirow{6}{*}{\begin{tabular}[c]{@{}l@{}}single-\\ sentence\end{tabular}}
& SST-2 & 2 & 67k & 0.9k & sentiment & $\langle S\rangle$. It was \texttt{[MASK]}. & great, bad \\
& Yelp P. & 2 & 560k & 38k & sentiment & $\langle S\rangle$. It was \texttt{[MASK]}. & great, bad \\
& AG's News & 4 & 120k & 7.6k & topic & \texttt{[MASK]} News: $\langle S\rangle$ & World, Sports, Business, Tech \\
& DBPedia & 14 & 560k & 70k & topic & [Category: \texttt{[MASK]}] $\langle S\rangle$ & Company, Education, Artist, Athlete, Office,\\ 
& & & & & & & Transportation, Building, Natural, Village,\\
& & & & & & & Animal, Plant, Album, Film, Written\\ \midrule
\multirow{3}{*}{\begin{tabular}[c]{@{}l@{}}sentence-\\ pair\end{tabular}}
& MRPC & 2 & 3.7k & 0.4k & paraphrase & $\langle S_1\rangle$ ? \texttt{[MASK]}, $\langle S_2\rangle$ & Yes, No \\
& RTE & 2 & 2.5k & 0.3k & NLI & $\langle S_1\rangle$ ? \texttt{[MASK]}, $\langle S_2\rangle$ & Yes, No \\
& SNLI & 3 & 549k & 9.8k & NLI & $\langle S_1\rangle$ ? \texttt{[MASK]}, $\langle S_2\rangle$ & Yes, Maybe, No \\ \bottomrule
\end{tabular}
}
\end{table*}
```

## Table 2
```latex
\begin{table}[t]
\centering
\caption{Default configuration of hyper-parameters.}
\label{tab:hyperparam}
\resizebox{.7\linewidth}{!}{
\begin{tabular}{lc}
\toprule
\textbf{Hyper-parameter} & \textbf{Default} \\ \midrule
Prompt length ($L$)              & 50         \\
Subspace dimension ($d$)         & 500        \\
Population size ($\lambda$)      & 20         \\
Random projection ($\mathbf{A}$) & Uniform    \\
Loss function $\mathcal{L}$      & Cross Entropy \\ 
Budget (\# of API calls)         & 8000      \\ \bottomrule
\end{tabular}
}
\vskip -0.2in
\end{table}
```

## Table 3
```latex
\begin{table*}[t!]
\centering
\caption{Overall comparison on various language understanding tasks. We report mean and standard deviation of performance over 3 different splits (\cref{sec:setup}). All of the results are obtained with pre-trained RoBERTa\textsubscript{LARGE} in 16-shot (per class) setting.}
\label{tab:main_results}
\resizebox{\linewidth}{!}{
\begin{tabular}{lcccccccr}
\toprule
\multirow{2}{*}{\textbf{Method}}                                                  & \textbf{SST-2} & \textbf{Yelp P.} & \textbf{AG's News} & \textbf{DBPedia} & \textbf{MRPC} & \textbf{SNLI} & \textbf{RTE} & \multirow{2}{*}{\textbf{Avg.}} \\
                                                                                  & acc            & acc              & acc                & acc              & F1            & acc           & acc          & \\ \midrule
\multicolumn{9}{c}{\textit{Gradient-Based Methods}}                                                                                                                                                                      \\ \midrule
% Prompt Tuning & 68.23 \small{$\pm$3.78} & 61.02 \small{$\pm$6.65} & 84.81 \small{$\pm$0.66} & 87.75 \small{$\pm$1.48} & 77.48 \small{$\pm$4.85} & 64.55 \small{$\pm$2.43} & 77.13 \small{$\pm$0.83} & 74.42\\
Prompt Tuning & 68.23 \small{$\pm$3.78} & 61.02 \small{$\pm$6.65} & 84.81 \small{$\pm$0.66} & 87.75 \small{$\pm$1.48} & 51.61 \small{$\pm$8.67} & 36.13 \small{$\pm$1.51} & 54.69 \small{$\pm$3.79} & 63.46 \\
\ + Pre-trained prompt & / & / & / & / & 77.48 \small{$\pm$4.85} & 64.55 \small{$\pm$2.43} & 77.13 \small{$\pm$0.83} & 74.42\\
P-Tuning v2    & 64.33 \small{$\pm$3.05} &92.63 \small{$\pm$1.39} &83.46 \small{$\pm$1.01} &97.05 \small{$\pm$0.41} &68.14 \small{$\pm$3.89} &36.89 \small{$\pm$0.79} &50.78 \small{$\pm$2.28} & 70.47 \\ 
% \ \ \ 16-shot                     & 68.23 \small{$\pm$3.78} & 61.02 \small{$\pm$6.65} & 84.81 \small{$\pm$0.66} & 87.75 \small{$\pm$1.48} & 77.48 \small{$\pm$4.85} & 64.55 \small{$\pm$2.43} & 77.13 \small{$\pm$0.83} & 74.42\\
% \ \ \ 32-shot                     & 80.33 \small{$\pm$8.17} & 87.15 \small{$\pm$0.23} & 84.85 \small{$\pm$3.07} & 93.01 \small{$\pm$1.96} & 76.98 \small{$\pm$4.87} & 70.18 \small{$\pm$6.58} & 78.21 \small{$\pm$0.75} & 81.53\\
% \ \ \ 64-shot                     & 86.32 \small{$\pm$5.38} & 89.40 \small{$\pm$0.97} & 88.58 \small{$\pm$0.09} & 92.86 \small{$\pm$0.65} & 80.59 \small{$\pm$1.71} & 74.55 \small{$\pm$4.25} & 78.70 \small{$\pm$0.72} & 84.43\\ \midrule 
% \ \ \ 50-shot  & 67.97 \small{$\pm$9.07}                &                 &  87.27 \small{$\pm$0.80}  &                  &  79.58 \small{$\pm$1.06}         &   70.36 \small{$\pm$4.96}     &  78.70 \small{$\pm$0.29}    & \\
% \ \ \ 100-shot &  81.08 \small{$\pm$10.2}   &                  & 87.68 \small{$\pm$0.45}    &                  &  79.48 \small{$\pm$1.66}             &  77.93 \small{$\pm$0.81}             &  80.14 \small{$\pm$0.59}            & \\
% \ \ \ 200-shot & 92.50 \small{$\pm$0.66}               &                  &  89.11 \small{$\pm$0.35}  &                  &  82.33 \small{$\pm$3.09} &  82.13 \small{$\pm$0.80}             &  79.54 \small{$\pm$0.74}            & \\ \midrule 
Model Tuning & 85.39 \small{$\pm$2.84} & 91.82 \small{$\pm$0.79} & 86.36 \small{$\pm$1.85} & 97.98 \small{$\pm$0.14} & 77.35 \small{$\pm$5.70} & 54.64 \small{$\pm$5.29} & 58.60 \small{$\pm$6.21} & 78.88\\
% \ \ \ 16-shot                     & 85.39 \small{$\pm$2.84} & 91.82 \small{$\pm$0.79} & 86.36 \small{$\pm$1.85} & 97.98 \small{$\pm$0.14} & 77.35 \small{$\pm$5.70} & 54.64 \small{$\pm$5.29} & 58.60 \small{$\pm$6.21} & 78.88\\
% \ \ \ 32-shot                     & 84.55 \small{$\pm$4.60} & 95.87 \small{$\pm$0.10} & 88.47 \small{$\pm$0.96} & 98.61 \small{$\pm$0.03} & 80.37 \small{$\pm$3.55} & 55.96 \small{$\pm$1.91} & 61.49 \small{$\pm$3.27} & 80.76\\
% \ \ \ 64-shot                     & 89.98 \small{$\pm$0.73} & 96.39 \small{$\pm$0.32} & 89.02 \small{$\pm$1.58} & 98.60 \small{$\pm$0.11} & 81.55 \small{$\pm$1.10} & 70.59 \small{$\pm$0.12} & 65.22 \small{$\pm$5.51} & 84.48\\ \bottomrule
% \ \ \ 50-shot    & 88.72 \small{$\pm$0.47}               & 96.16 \small{$\pm$0.12}                 & 89.30 \small{$\pm$0.54}                   & 98.59 \small{$\pm$0.07}                 & 82.69 \small{$\pm$0.63}              & 65.49 \small{$\pm$3.69}              & 62.69 \small{$\pm$1.89}             & \\
% \ \ \ 100-shot   & 91.28 \small{$\pm$0.77}               & 96.13 \small{$\pm$0.18}                 & 90.07 \small{$\pm$0.27}                   & 98.80 \small{$\pm$0.08}                 & 83.96 \small{$\pm$1.35}              & 79.12 \small{$\pm$0.99}              & 71.12 \small{$\pm$4.13}             & \\
% \ \ \ 200-shot   & 91.51 \small{$\pm$0.98}               & 96.52 \small{$\pm$0.29}                 & 90.45 \small{$\pm$0.24}                   & 98.88 \small{$\pm$0.06}                 & 84.88 \small{$\pm$1.88}              & 83.61 \small{$\pm$0.05}              & 76.53 \small{$\pm$2.23}             & \\ 
\midrule
\multicolumn{9}{c}{\textit{Gradient-Free Methods}}                                                                                                                                                                      \\ \midrule
Manual Prompt            & 79.82 & 89.65 & 76.96 & 41.33 & 67.40 & 31.11 & 51.62 & 62.56 \\
In-Context Learning      & 79.79 \small{$\pm$3.06} & 85.38 \small{$\pm$3.92} & 62.21 \small{$\pm$13.46} & 34.83 \small{$\pm$7.59} & 45.81 \small{$\pm$6.67} & 47.11 \small{$\pm$0.63} & 60.36 \small{$\pm$1.56} & 59.36\\
Feature-MLP   &64.80 \small{$\pm$1.78} &79.20 \small{$\pm$2.26} &70.77 \small{$\pm$0.67} & 87.78 \small{$\pm$0.61}&68.40 \small{$\pm$0.86} &42.01 \small{$\pm$0.33} &53.43 \small{$\pm$1.57} & 66.63\\
Feature-BiLSTM   &65.95 \small{$\pm$0.99} &74.68 \small{$\pm$0.10} &77.28 \small{$\pm$2.83} &90.37 \small{$\pm$3.10} &71.55 \small{$\pm$7.10} &46.02 \small{$\pm$0.38} &52.17 \small{$\pm$0.25} & 68.29\\
\textbf{Black-Box Tuning} & 89.56 \small{$\pm$0.25} & 91.50 \small{$\pm$0.16} & 81.51 \small{$\pm$0.79} & 87.80 \small{$\pm$1.53} & 61.56 \small{$\pm$4.34} &  46.58 \small{$\pm$1.33}  & 52.59 \small{$\pm$2.21} & 73.01\\
% \textbf{Black-Box Tuning}  & \underline{89.56} \small{$\pm$0.25} & \textbf{91.50} \small{$\pm$0.16} & \underline{82.50} \small{$\pm$1.13} & 79.99 \small{$\pm$2.95} & 61.56 \small{$\pm$4.34} &  46.58 \small{$\pm$1.33}  & 52.59 \small{$\pm$2.21} & 72.04 \\ 
\ + Pre-trained prompt & / & / & / & / & 75.51 \small{$\pm$5.54} & 83.83 \small{$\pm$0.21} & 77.62 \small{$\pm$1.30} & \textbf{83.90} \\ 
% \ \ \ 16-shot                     & 87.04 \small{$\pm$2.71} & 90.95 \small{$\pm$1.38} & 81.73 \small{$\pm$0.63} & 86.68 \small{$\pm$1.99} & 76.59 \small{$\pm$1.61} & 83.83 \small{$\pm$0.21} & 77.62 \small{$\pm$1.30} & \textbf{83.49}\\
% \ \ \ 32-shot                     & 87.65 \small{$\pm$1.38} & 91.78 \small{$\pm$1.03} & 83.09 \small{$\pm$0.25} & 88.03 \small{$\pm$0.82} & 76.62 \small{$\pm$0.84} & 83.16 \small{$\pm$2.11} & 77.86 \small{$\pm$3.35} & \textbf{84.03}\\
% \ \ \ 64-shot                     & 89.60 \small{$\pm$0.52} & 92.53 \small{$\pm$0.76} & 84.91 \small{$\pm$0.74} & 91.47 \small{$\pm$0.80} & 78.77 \small{$\pm$1.25} & 84.14 \small{$\pm$0.26} & 78.94 \small{$\pm$2.46} & \textbf{85.77}\\ \midrule
% \ \ \ 50-shot            & 89.76 \small{$\pm$0.48}               & 92.76 \small{$\pm$0.61}                 & 84.20 \small{$\pm$1.41}                   &                  & 77.08 \small{$\pm$3.99}              & 84.35 \small{$\pm$0.38}              & 78.22 \small{$\pm$1.04}        &      \\
% \ \ \ 100-shot           & 90.60 \small{$\pm$0.75}               & 93.07 \small{$\pm$1.03}                 & 85.50 \small{$\pm$0.80}                   &                  & 78.76 \small{$\pm$2.11}              & 84.67 \small{$\pm$0.23}              & 78.82 \small{$\pm$0.55}        &      \\
% \ \ \ 200-shot           & 90.83 \small{$\pm$0.98}               & 93.72 \small{$\pm$0.66}                 & 86.74 \small{$\pm$0.52}                   & 92.51 \small{$\pm$0.54}                & 79.00 \small{$\pm$3.47}              & 85.85 \small{$\pm$0.06}              & 78.16 \small{$\pm$0.26}             & \\ 

\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 4
```latex
\begin{table*}[th]
\centering
% PT: Prompt Tuning. MT: Model Tuning. FL: feature-MLP. FB: Feature-BiLSTM. BBT: Black-Box Tuning.
\caption{Comparison of deployment efficiency, viability of as-a-service, test accuracy, training time, memory footprint, and the amount of data to be uploaded/downloaded. $^\star$ indicates the training time of the implementation with ONNX Runtime. All the compared methods are performed on the same 16-shot splits of SST-2 and AG's News.}
\label{tab:time_memo}
\resizebox{.95\linewidth}{!}{
\begin{tabular}{lcccccccc}
\toprule
& \textbf{Deployment-} & \textbf{As-A-} & \textbf{Test} & \textbf{Training} & \multicolumn{2}{c}{\textbf{Memory Footprint}} & \textbf{Upload} & \textbf{Download} \\
& \textbf{Efficient} & \textbf{Service} & \textbf{Accuracy}                & \textbf{Time}        & User          & Server        & per query        & per query   \\ \midrule
\multicolumn{9}{c}{SST-2 (max sequence length: 47)}                                                                                         \\ \midrule
Prompt Tuning   & $\surd$ & $\times$ & 72.6 & 15.9 mins & - & 5.3 GB & - & - \\
Model Tuning   & $\times$ & $\times$ & 87.8 & 9.8 mins & - & 7.3 GB & - & - \\
Feature-MLP   & $\surd$ & $\surd$ & 63.8 & 7.0 mins & 20 MB & 2.8 GB & 4 KB & 128 KB \\
Feature-BiLSTM   & $\surd$ & $\surd$ & 66.2 & 9.3 mins & 410 MB & 2.8 GB & 4 KB & 6016 KB \\
Black-Box Tuning  & $\surd$ & $\surd$ & 89.4 & 10.1 (6.1$^\star$) mins & 30 MB & 3.0 GB & 6 KB & 0.25 KB \\ \midrule
\multicolumn{9}{c}{AG's News (max sequence length: 107)}\\ \midrule
Prompt Tuning & $\surd$ & $\times$ & 84.0 & 30.2 mins & - & 7.7 GB & - & - \\
Model Tuning & $\times$ & $\times$ & 88.4 & 13.1 mins & - & 7.3 GB & - & - \\
Feature-MLP & $\surd$ & $\surd$ & 71.0 & 13.5 mins & 20 MB & 3.6 GB & 20 KB & 256 KB \\
Feature-BiLSTM & $\surd$ & $\surd$ & 73.1 & 19.7 mins & 500 MB & 3.6 GB & 20 KB & 27392 KB \\
Black-Box Tuning & $\surd$ & $\surd$ & 82.6 & 21.0 (17.7$^\star$) mins & 30 MB & 4.6 GB & 22 KB & 1 KB \\ \bottomrule
\end{tabular}
}
\end{table*}
```

