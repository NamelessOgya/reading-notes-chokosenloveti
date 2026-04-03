# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[h]
% \vspace{-0.1in}
% \small
%     \centering
%     \begin{tabu} to 1\textwidth { X[l] }
%     \toprule
%           \textbf{Question}: 
%           \textit{Janet’s ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for \$2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?} (Ground truth answer is \textcolor{blue}{18}.)\\
%           \midrule
%           \midrule
%           \textbf{Greedy Decode}:
%           She eats 3 for breakfast every morning and bakes muffins for her friends every day with 4. This means she eats 3 + 4 = 7 eggs every day. She sells the remainder at the farmers' market daily for \$2 per fresh duck egg. So she sells \textcolor{red}{7 * \$2 = \$14} per day. The answer is \textcolor{red}{14}. \\
%           \midrule
%           \textbf{Sample decode with diverse reasoning paths}:\\
%           \vspace{0.01ex}
%           \textbf{- Output 1}: She eats three eggs for breakfast. She bakes muffins for her friends with four eggs. 
%           She sells the remainder at the farmers' market daily for \$2 per fresh duck egg. This means she sells the remainder at the farmers' market daily for \textcolor{red}{\$2 * (16 - 4 - 3) = \$2 * 13 = \$26} per day.  The answer is \textcolor{red}{\$26}. (\textcolor{red}{calculation mistake})\\
%           \vspace{0.01ex}
%           \textbf{- Output 2}: She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for \$2 per fresh duck egg. She eats \textcolor{blue}{3 + 4 = 7} eggs. She \\sells the remainder. So, the number of eggs she sells is \textcolor{blue}{16 - 7 = 9}. She sells each egg for \$2. So, in total she\\ makes \textcolor{blue}{\$2 * 9 = \$18}. The answer is \textcolor{blue}{\$18}.\\
%           \vspace{0.01ex}
%           \textbf{- Output 3}: She eats 3 eggs every morning and bakes muffins for her friends every day with 4 eggs. This means she uses 3 + 4 = 7 eggs every day. She sells the remainder at the farmers' market daily for \$2 each. So in total she sells \textcolor{red}{7 * \$2 = \$14} per day. The answer is \textcolor{red}{\$14}. (\textcolor{red}{incorrect reasoning process})\\
%           \vspace{0.01ex}
%           \textbf{- Output 4}: Janet's ducks lay 16 eggs per day. She eats 3 for breakfast and bakes muffins with 4. That means she has \textcolor{blue}{16 - 3 - 4 = 9} eggs left. She sells them for \$2 each, so she makes \textcolor{blue}{\$2 * 9 = \$18} per day. The answer is \textcolor{blue}{18}.\\
%           \vspace{0.01ex}
%           \textbf{- Output 5}: She eats 3 for breakfast every morning, so she has \textcolor{blue}{16 - 3 = 13} eggs left. Then she bakes muffins with 4 eggs every day, so she has \textcolor{blue}{13 - 4 = 9} eggs left. She sells the remainder at the farmers' market daily for \$2 per fresh duck egg. So she has \textcolor{blue}{9 eggs * \$2 = \$18}. The answer is \textcolor{blue}{\$18}.
%         \\
%     \bottomrule
%     \end{tabu}
%     \vspace{0.02in}
%     \caption{An example showing how self-consistency over diverse reasoning paths can improve reasoning in language models. The outputs are generated from a 137B language model, and the example is taken from the GSM8K dataset \citep{cobbe2021training}. The blue/red color indicates correct/incorrect reasoning paths and their corresponding answers from the model.}
%     \label{tab:example}
%     \vspace{-0.15in}
% \end{table}
```

## Table 2
```latex
\begin{table}[t]
\small
\setlength\tabcolsep{4pt}
    \centering
    \vspace{-0.1in}
    \begin{tabular}{c cccccc}
    \toprule
         & GSM8K  & MultiArith & AQuA & SVAMP & CSQA & ARC-c \\
         \midrule
       Greedy decode & 56.5 & 94.7 & 35.8 & 79.0 & 79.0 & 85.2\\
       \midrule
       Weighted avg (unnormalized) & 56.3 \scriptsize{$\pm$ 0.0} & 90.5 \scriptsize{$\pm$ 0.0} & 35.8 \scriptsize{$\pm$ 0.0} & 73.0 \scriptsize{$\pm$ 0.0} & 74.8 \scriptsize{$\pm$ 0.0} & 82.3 \scriptsize{$\pm$ 0.0} \\
       Weighted avg (normalized) & 22.1 \scriptsize{$\pm$ 0.0} & 59.7 \scriptsize{$\pm$ 0.0} & 15.7 \scriptsize{$\pm$ 0.0} & 40.5 \scriptsize{$\pm$ 0.0} & 52.1 \scriptsize{$\pm$ 0.0} & 51.7 \scriptsize{$\pm$ 0.0}\\
       \midrule
       Weighted sum (unnormalized) & 59.9 \scriptsize{$\pm$ 0.0} & 92.2 \scriptsize{$\pm$ 0.0} & 38.2 \scriptsize{$\pm$ 0.0} & 76.2 \scriptsize{$\pm$ 0.0} & 76.2 \scriptsize{$\pm$ 0.0} & 83.5 \scriptsize{$\pm$ 0.0} \\
       Weighted sum (normalized) & 74.1 \scriptsize{$\pm$ 0.0} & 99.3 \scriptsize{$\pm$ 0.0} & 48.0 \scriptsize{$\pm$ 0.0} & 86.8 \scriptsize{$\pm$ 0.0} & 80.7 \scriptsize{$\pm$ 0.0} & 88.7 \scriptsize{$\pm$ 0.0}\\
       \midrule
       Unweighted sum (majority vote) & 74.4 \scriptsize{$\pm$ 0.1} & 99.3 \scriptsize{$\pm$ 0.0} & 48.3 \scriptsize{$\pm$ 0.5} & 86.6 \scriptsize{$\pm$ 0.1} & 80.7 \scriptsize{$\pm$ 0.1} & 88.7 \scriptsize{$\pm$ 0.1} \\
       \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Accuracy comparison of different answer aggregation strategies on PaLM-540B.}
    \label{tab:aggregation}
\vspace{-0.1in}
\end{table}
```

## Table 3
```latex
\begin{table}[h]
\small
\setlength\tabcolsep{3pt}
    \centering
    \vspace{-0.05in}
    \begin{tabular}{cl  llllll}
    \toprule
        & Method & AddSub & MultiArith & ASDiv & AQuA & SVAMP & GSM8K
        \\
         \midrule
        & Previous SoTA & \textbf{94.9}$^a$ & 60.5$^a$ & 75.3$^b$ & 37.9$^c$ & 57.4$^d$ &  35$^e$ / 55$^g$ \\
        \midrule
        \multirow{2}{*}{UL2-20B} & CoT-prompting & 18.2 & 10.7 & 16.9 & 23.6 & 12.6 & 4.1 \\
       & Self-consistency  & 24.8 {\scriptsize(+6.6)} & 15.0 {\scriptsize(+4.3)} & 21.5 {\scriptsize(+4.6)} & 26.9 {\scriptsize(+3.3)} & 19.4 {\scriptsize(+6.8)} & 7.3 {\scriptsize(+3.2)}\\
        \midrule
        \multirow{2}{*}{\makecell{LaMDA-137B}} &
        CoT-prompting & 52.9 & 51.8 & 49.0 &  17.7 & 38.9 & 17.1\\
        & Self-consistency & 63.5 {\scriptsize(+10.6)} & 75.7 {\scriptsize(+23.9)} & 58.2 {\scriptsize(+9.2)} & 26.8 {\scriptsize(+9.1)} & 53.3 {\scriptsize(+14.4)} & 27.7 {\scriptsize(+10.6)}\\
        \midrule
        \multirow{2}{*}{\makecell{PaLM-540B}} &
        CoT-prompting & 91.9 & 94.7 & 74.0 & 35.8 & 79.0 & 56.5\\
        & Self-consistency & 93.7 {\scriptsize(+1.8)} & 99.3 {\scriptsize(+4.6)} & 81.9 {\scriptsize(+7.9)} & 48.3 {\scriptsize(+12.5)} & 86.6 {\scriptsize(+7.6)} & 74.4 {\scriptsize(+17.9)}\\
        \midrule
        \multirow{2}{*}{\makecell{GPT-3\\\scriptsize{Code-davinci-001}}} & CoT-prompting & 57.2 & 59.5 & 52.7  & 18.9 & 39.8 & 14.6\\
    & Self-consistency & 67.8 {\scriptsize(+10.6)} & 82.7 {\scriptsize(+23.2)} & 61.9 {\scriptsize(+9.2)} & 25.6 {\scriptsize(+6.7)} & 54.5 {\scriptsize(+14.7)}  & 23.4 {\scriptsize(+8.8)}\\
    \midrule
    \multirow{2}{*}{\makecell{GPT-3\\\scriptsize{Code-davinci-002}}} & CoT-prompting & 89.4 & 96.2 & 80.1 & 39.8 & 75.8 & 60.1\\
    & Self-consistency & 91.6 {\scriptsize(+2.2)} & \textbf{100.0} {\scriptsize(+3.8)} & \textbf{87.8} {\scriptsize(+7.6)} & \textbf{52.0} {\scriptsize(+12.2)} & \textbf{86.8} {\scriptsize(+11.0)} & \textbf{78.0} {\scriptsize(+17.9)}\\
    \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Arithmetic reasoning accuracy by self-consistency compared to chain-of-thought prompting \citep{wei2022chain}.
    The previous SoTA baselines are obtained from: 
    $a$: Relevance and LCA operation classifier \citep{roy-roth-2015-solving},
    $b$: \cite{lan2021mwptoolkit},
    $c$: \cite{amini-etal-2019-mathqa},
    $d$: \cite{pi2022reasoning},
    $e$: GPT-3 175B finetuned with 7.5k examples \citep{cobbe2021training},
    $g$: GPT-3 175B finetuned plus an additional 175B verifier \citep{cobbe2021training}. The best performance for each task is shown in bold.}
    \label{tab:sota}
\vspace{-0.1in}
\end{table}
```

## Table 4
```latex
\begin{table}[h]
\small
\setlength\tabcolsep{3pt}
    \centering
    \vspace{-0.05in}
    \begin{tabular}{cl llllll}
    \toprule
        & Method & CSQA & StrategyQA & ARC-e & ARC-c & Letter (4) & Coinflip (4)
        \\
        \midrule
        & Previous SoTA & \textbf{91.2}$^a$ & 73.9$^b$ & 86.4$^c$ & 75.0$^c$ & N/A & N/A \\
        \midrule
        \multirow{2}{*}{UL2-20B} & CoT-prompting & 51.4 & 53.3 & 61.6 & 42.9 & 0.0 & 50.4\\
       & Self-consistency & 55.7 {\scriptsize(+4.3)} & 54.9 {\scriptsize(+1.6)} & 69.8 {\scriptsize(+8.2)} & 49.5 {\scriptsize(+6.8)} & 0.0 {\scriptsize(+0.0)} & 50.5 {\scriptsize(+0.1)}\\
        \midrule
        \multirow{2}{*}{\makecell{LaMDA-137B}} &
        CoT-prompting & 57.9 & 65.4 & 75.3 & 55.1 & 8.2 & 72.4\\
        & Self-consistency & 63.1 {\scriptsize(+5.2)} & 67.8 {\scriptsize(+2.4)} & 79.3 {\scriptsize(+4.0)} & 59.8 {\scriptsize(+4.7)} & 8.2 {\scriptsize(+0.0)} & 73.5 {\scriptsize(+1.1)}\\
        \midrule
        \multirow{2}{*}{\makecell{PaLM-540B}} &
        CoT-prompting & 79.0 & 75.3 & 95.3 & 85.2 & 65.8 & 88.2\\
        & Self-consistency & 80.7 {\scriptsize(+1.7)} & \textbf{81.6} {\scriptsize(+6.3)} & \textbf{96.4} {\scriptsize(+1.1)} & \textbf{88.7} {\scriptsize(+3.5)} & 70.8 {\scriptsize(+5.0)} & 91.2 {\scriptsize(+3.0)}\\
        \midrule
    \multirow{2}{*}{\makecell{GPT-3\\\scriptsize{Code-davinci-001}}} & CoT-prompting & 46.6 & 56.7 & 63.1 & 43.1 & 7.8 & 71.4\\
    & Self-consistency & 54.9 {\scriptsize(+8.3)} & 61.7 {\scriptsize(+5.0)} & 72.1 {\scriptsize(+9.0)} & 53.7 {\scriptsize(+10.6)} & 10.0 {\scriptsize(+2.2)} & 75.9 {\scriptsize(+4.5)}\\
    \midrule
    \multirow{2}{*}{\makecell{GPT-3\\\scriptsize{Code-davinci-002}}} & CoT-prompting & 79.0 & 73.4 & 94.0 & 83.6 & 70.4 & 99.0\\
    & Self-consistency & 81.5 {\scriptsize(+2.5)} & 79.8 {\scriptsize(+6.4)} & 96.0 {\scriptsize(+2.0)} & 87.5 {\scriptsize(+3.9)} & \textbf{73.4} {\scriptsize(+3.0)} & \textbf{99.5} {\scriptsize(+0.5)}\\
        \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Commonsense and symbolic reasoning accuracy by self-consistency compared to chain-of-thought prompting \citep{wei2022chain}.
    The previous SoTA baselines are obtained from: 
    $a$: DeBERTaV3-large + KEAR \citep{https://doi.org/10.48550/arxiv.2112.03254},
    $b$: \cite{palm},
    $c$: UnifiedQA-FT \citep{khashabi-etal-2020-unifiedqa}. The best performance for each task is shown in bold.}
    \label{tab:commonsense}
\end{table}
```

## Table 5
```latex
\begin{table}[h]
\vspace{-0.05in}
\setlength\tabcolsep{4pt}
\scriptsize
\centering
    \begin{tabu} to 1\textwidth { p{0.9cm} | p{7.8cm} | p{4.7cm}}
        \toprule
        &GSM8K & StrategyQA\\
        \midrule
         \textbf{Question} & \textit{Henry made two stops during his 60-mile bike trip. He first stopped after 20 miles. His second stop was 15 miles before the end of the trip. How many miles did he travel between his first and second stops?} & \textit{Yes or no: Is Albany, Georgia the most populous US Albany?}\\
         \midrule
         \textbf{Greedy Decode} & He traveled 60 miles in total. He stopped after 20 miles, so he traveled \textcolor{red}{60 - 20 = 40 miles} between the first and second stops. The answer is \textcolor{red}{40}. & \textcolor{red}{Albany, Georgia is the most populous US Albany}. Thus, the answer is \textcolor{red}{yes}.\\
         \midrule
         \textbf{Sampled Path 1} & Henry travelled a total of 60 miles. His first stop was 20 miles in, and his second stop was 15 miles before the end. So \textcolor{blue}{between his first and second stops he travelled 60 - 20 -15 = 25 miles}. The answer is \textcolor{blue}{25}. & \textcolor{blue}{The most populous US Albany is Albany, New York}. Thus, Albany, Georgia is not the most populous US Albany. So the answer is \textcolor{blue}{no}.\\
         \midrule
         \textbf{Sampled Path 2} & He made two stops during a 60-mile trip. The first was 20 miles into the trip. The second was 15 miles before the end of the trip. This means \textcolor{blue}{the second stop was 60 - 15 = 45 miles into the trip}. Since he made the stops in order, \textcolor{blue}{the second stop must have been 45 - 20 = 25 miles after the first stop}. The answer is \textcolor{blue}{25}. & \textcolor{blue}{Albany, Georgia has a population of about 88,000. Albany, New York has a population of about 95,000}. Thus, Albany, Georgia is not the most populous US Albany. So the answer is \textcolor{blue}{no}.\\
         \bottomrule
    \end{tabu}
    \vspace{-0.15in}
    \caption{Examples where self-consistency helps repair the errors over greedy decode, on PaLM-540B. Two sampled reasoning paths that are consistent with the ground truth are shown.}
    \label{tab:example_path}
    % \vspace{-0.1in}
\end{table}
```

## Table 6
```latex
\begin{table}[h]
\vspace{-0.1in}
\small
\setlength\tabcolsep{4pt}
    \centering
    \begin{tabular}{c ccccc}
    \toprule
    & ANLI R1 / R2 / R3 & e-SNLI & RTE & BoolQ & HotpotQA (EM/F1) \\
    \midrule
    Standard-prompting (no-rationale) & 69.1 / 55.8 / 55.8 &  85.8 & 84.8 & 71.3 & 27.1 / 36.8  \\
    CoT-prompting \citep{wei2022chain} & 68.8 / 58.9 / 60.6 & 81.0 & 79.1  & 74.2 & 28.9 / 39.8  \\
    \midrule
    Self-consistency & \textbf{78.5} / \textbf{64.5} / \textbf{63.4} & \textbf{88.4} & \textbf{86.3} & \textbf{78.4} & \textbf{33.8 / 44.6}\\
    \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Compare Standard/CoT prompting with self-consistency on common NLP tasks. }
    \label{tab:common_nlp}
\vspace{-0.1in}
\end{table}
```

## Table 7
```latex
\begin{table}[h]
\setlength\tabcolsep{3pt}
\small
    \centering
    \vspace{-0.1in}
    \begin{tabular}{ll ccccc}
    \toprule
        & Beam size / Self-consistency paths & 1 & 5 & 10 & 20 & 40\\
\midrule
\multirow{3}{*}{AQuA} & Beam search decoding (top beam) & 23.6 & 19.3 & 16.1 & 15.0 &10.2  \\
& Self-consistency using beam search & 23.6 & 19.8 \scriptsize{$\pm$ 0.3} & 21.2 \scriptsize{$\pm$ 0.7} & 24.6 \scriptsize{$\pm$ 0.4} & 24.2 \scriptsize{$\pm$ 0.5}\\
& Self-consistency using sampling & 19.7 \scriptsize{$\pm$ 2.5} & \textbf{24.9 \scriptsize{$\pm$ 2.6}} & \textbf{25.3 \scriptsize{$\pm$ 1.8}} & \textbf{26.7 \scriptsize{$\pm$ 1.0}} & \textbf{26.9 \scriptsize{$\pm$ 0.5}} \\
\midrule
\multirow{3}{*}{MultiArith} & Beam search decoding (top beam) & 10.7 & 12.0 &11.3 & 11.0 &10.5\\
& Self-consistency using beam search & 10.7 & 11.8 \scriptsize{$\pm$ 0.0} & 11.4 \scriptsize{$\pm$ 0.1} &12.3 \scriptsize{$\pm$ 0.1} & 10.8 \scriptsize{$\pm$ 0.1}\\
& Self-consistency using sampling & 9.5 \scriptsize{$\pm$ 1.2} & 11.3 \scriptsize{$\pm$ 1.2} & \textbf{12.3 \scriptsize{$\pm$ 0.8}} & \textbf{13.7 \scriptsize{$\pm$ 0.9}} & \textbf{14.7 \scriptsize{$\pm$ 0.3}}\\
\bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Compare self-consistency with beam search decoding on the UL2-20B model.}
    \label{tab:beam_search}
    \vspace{-0.1in}
\end{table}
```

## Table 8
```latex
\begin{table}[h]
\small
    \centering
    \vspace{-0.1in}
    \begin{tabular}{l ccccc}
        \toprule
        & GSM8K & MultiArith & SVAMP & ARC-e &  ARC-c\\
        \midrule
        CoT \citep{wei2022chain} & 17.1 &  51.8 & 38.9 & 75.3 & 55.1 \\
        Ensemble (3 sets of prompts) & 18.6 \scriptsize{$\pm$ 0.5} & 57.1 \scriptsize{$\pm$ 0.7} & 42.1 \scriptsize{$\pm$ 0.6} & 76.6 \scriptsize{$\pm$ 0.1} & 57.0 \scriptsize{$\pm$ 0.2} \\
        Ensemble (40 prompt permutations) & 19.2 \scriptsize{$\pm$ 0.1} & 60.9 \scriptsize{$\pm$ 0.2} & 42.7 \scriptsize{$\pm$ 0.1} & 76.9 \scriptsize{$\pm$ 0.1} & 57.0 \scriptsize{$\pm$ 0.1} \\
        Self-Consistency (40 sampled paths) & \textbf{27.7 \scriptsize{$\pm$ 0.2}} & \textbf{75.7 \scriptsize{$\pm$ 0.3}} & \textbf{53.3 \scriptsize{$\pm$ 0.2}} & \textbf{79.3 \scriptsize{$\pm$ 0.3}} & \textbf{59.8 \scriptsize{$\pm$ 0.2}}\\
    \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Self-consistency outperforms prompt-order and multi-prompt ensembles on LaMDA-137B.}
    \label{tab:ensemble}
\vspace{-0.15in}
\end{table}
```

## Table 9
```latex
\begin{table}[h]
% \centering
%     \begin{tabular}{c|c|c|c|c}
%         \toprule
%         Greedy Decode &  \multicolumn{4}{c}{17.1} \\
%         \midrule
%         \# Sampled Seqs &  5 & 10 & 20 & 40 \\
%         \midrule
%         T = 0.7, $k$ = 40 & 18.5 & 22.1 & 25.6 & 27.0\\
%         T = 0.5, $k$ = 40 & 21.1 & 24.3 & 27.0 & 27.7\\
%         T = 0.3, $k$ = 40 & 21.2 & 22.7 & 23.4 & 23.5\\
%         \midrule
%         T = 0.5, $k$ = 20 & 20.2 & 23.9 & 26.2 & 26.9\\
%         T = 0.5, no top-$k$ & 21.2 & 24.3 & 25.2 & 27.3 \\
%     \bottomrule
%     \end{tabular}
%     \vspace{0.05in}
%     \caption{Effect of the sampling temperature $T$ and the number of sequences we sample on GSM8K accuracy, fixing $k=40$ with top-$k$ sampling; and the effect of $k$ in top-$k$ sampling with a fixed sampling temperature of $T=0.5$. }
%     \label{tab:temperature}
% \end{table}
```

## Table 10
```latex
\begin{table}[h]
\vspace{-0.05in}
\begin{minipage}{0.62\linewidth}
\setlength\tabcolsep{4pt}
    \centering
    \small
    \begin{tabular}{ll c}
    \toprule
     \multirow{5}{*}{LaMDA-137B} &  Prompt with correct chain-of-thought & 17.1 \\
     \cmidrule{2-3}
        & Prompt with imperfect chain-of-thought & 14.9\\
        & \hspace{1mm}  + Self-consistency (40 paths) & \textbf{23.4} \\
    \cmidrule{2-3}
        & Prompt with equations & 5.0 \\
        & \hspace{1mm}  + Self-consistency (40 paths) & \textbf{6.5}\\
    \midrule
      \multirow{2}{*}{PaLM-540B} &  Zero-shot CoT \citep{zero_shot_cot} & 43.0 \\
        & \hspace{1mm}  + Self-consistency (40 paths) & \textbf{69.2}\\
    \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Self-consistency works under imperfect prompts, equation prompts and zero-shot chain-of-thought for GSM8K.}
    \label{tab:robustness}
\end{minipage}\hfill
\begin{minipage}{0.33\linewidth}
		\centering
% 		\vspace{-0.05in}
		\includegraphics[width=1.0\linewidth]{figures/error_rate.pdf}
		\vspace{-0.32in}
		\captionof{figure}{The consistency is correlated with model's accuracy.}
		\label{fig:error_rate}
	\end{minipage}
\vspace{-0.1in}
\end{table}
```

## Table 11
```latex
\begin{table}[h]
\small
    \centering
    \begin{tabular}{c|c|c|c}
    \toprule
    & Prompt set 1 (used in the main text) & Prompt set 2 & Prompt set 3\\
    \midrule
        CoT \citep{wei2022chain} &  56.5 & 54.6 & 54.0 \\
        Self-consistency & 74.4 (+17.9) & 72.1 (+17.5) & 70.4 (+16.4)\\
        \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{GSM8K accuracy over PaLM-540B. The results show robustness of self-consistency with respect to different prompts in the input.}
    \label{tab:robustness_prompt}
\end{table}
```

## Table 12
```latex
\begin{table}[h]
\setlength\tabcolsep{3pt}
    \centering
\small
    \begin{tabular}{ll c}
    \toprule
    & Method & GSM8K accuracy\\
     \midrule
Single model & PaLM-540B, greedy / self-consistency & 56.5 / 74.4\\
\midrule
\multirow{3}{*}{Ensemble of models}  &  LaMDA-137B + PaLM-540B & 36.9 $\pm$ 0.5 \\
& PaLM-540B + GPT-3 (code-davinci-001, 175B) &  36.6 $\pm$ 0.4\\
& LaMDA-137B + GPT-3 (code-davinci-001, 175B) &16.0 $\pm$ 0.8\\
& LaMDA-137B + PaLM-540B + GPT-3 (code-davinci-001, 175B) & 33.3 $\pm$ 0.7\\
\bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Comparison of GSM8K accuracy over multiple-model ensembles.}
    \label{tab:ensemble_model}
\end{table}
```

## Table 13
```latex
\begin{table}[]
\small
    \centering
    \begin{tabular}{l c}
    \toprule
         &  GSM8K accuracy \\
         \midrule
        Different sets of prompts (x40) & 58.9\\
        Prompt-permutation (x40) & 59.6\\
        Self-consistency (x40) & 74.4 \\
        Self-consistency + different sets of prompts (x40) & 75.4\\
        Self-consistency + prompt-permutation (x40) & 73.8\\
        \bottomrule
    \end{tabular}
    \vspace{-0.1in}
    \caption{Combining self-consistency with other ensembling strategies.}
    \label{tab:combine}
\end{table}
```

## Table 14
```latex
\begin{table}[h]
\scriptsize
    \centering
    \begin{tabular}{p{3.2cm} | p{3.1cm} | p{2.6cm} | p{3.3cm} }
        Question & Greedy Decode & Sampled Path 1 & Sampled Path 2  \\
        \midrule
        \textbf{[MultiArith]}  \textit{Sam had 10 socks. If he threw away 3 old ones that didn't fit and bought 36 new ones, how many socks would he have?}
         & Sam had 10 socks. He threw away 3 old ones that didn't fit. He bought 36 new ones. That means he has \textcolor{red}{10 + 36 - 3 = 41} socks. The answer is \textcolor{red}{41}.
         & Sam had 10 socks. He threw away 3 old ones. So now he has \textcolor{blue}{7} left. Then he bought 36 new ones. So now he has \textcolor{blue}{7 + 36 = 43} socks. The answer is \textcolor{blue}{43}.  
         & He had 10 socks. He threw away 3 old ones that didn't fit. He bought 36 new ones. So in total he has \textcolor{blue}{10 - 3 + 36 = 43} socks. The answer is \textcolor{blue}{43}.  \\
         \midrule
        \textbf{[SVAMP]}   \textit{In a school there are 697 girls and the rest are boys. If there are 228 more girls than boys. How many boys are there in that school?}
         & There are 697 girls and the rest are boys. That means there are \textcolor{red}{697 + 228 = 925} girls. The rest are boys. So the number of boys is \textcolor{red}{925 - 697 = 228}. The answer is \textcolor{red}{228}. 
         & The number of boys is the difference between 697 and 228. This is \textcolor{blue}{697 - 228 = 469}. The answer is \textcolor{blue}{469}.  
         & In the beginning there are 697 girls and the rest are boys. So, the number of boys must be \textcolor{blue}{697 - 228 = 469} boys. The answer is \textcolor{blue}{469}.  \\
         \midrule
         \textbf{[AQuA]} \textit{There are 10 oranges in a basket. Find the no. of ways in which 2 oranges are chosen from the basket?} (a) 45 (b) 90 (c) 120 (d) 150 (e) 180
         & There are 10 oranges in a basket. So there are \textcolor{red}{10 ways} in which 2 oranges are chosen from the basket.  
         & There are 10 oranges in a basket. We need to choose 2 oranges from the basket. So the number of ways are \textcolor{blue}{10C2}. So the answer is \textcolor{blue}{(a)}.  
         & There are 10 oranges in the basket. If you choose 2 oranges, you have \textcolor{blue}{10C2 = 45} ways of choosing 2 oranges. So the answer is \textcolor{blue}{(a)}.  \\
         \midrule
        \textbf{[CommonsenseQA]} \textit{The man laid on the soft moss and looked up at the trees, where was the man?} (a) niagra falls (b) forest (c) waterfall (d) ground (e) tree
        & The answer must be something that is soft and mossy. Of the above choices, \textcolor{red}{only ground is soft and mossy}. So the answer is \textcolor{red}{(d)}.  
        & The answer must be somewhere where moss is found. Of the above choices, \textcolor{blue}{only forests are known for having moss}. So the answer is \textcolor{blue}{(b)}.  
        & The answer must be a place where the man is laying down and looking up at trees. Of the above choices, \textcolor{blue}{only forest is a place where people lay down and look at trees}. So the answer is \textcolor{blue}{(b)}.  \\
        \midrule
         \textbf{[ARC]} \textit{Which of these will most likely harm a habitat?}
         (a) planting trees. (b) water pollution. (c) rainfall. (d) sunlight.
        & Planting trees will not harm a habitat. So the answer is \textcolor{red}{(a)}.  
        & The answer is \textcolor{blue}{(b)}, water pollution, because it will \textcolor{blue}{most likely harm the habitat}. \textcolor{blue}{The other answers are not likely to harm the habitat}.
        & The answer is (b), water pollution. \textcolor{blue}{Trees are good for a habitat, rainfall is necessary for a habitat, and sunlight is necessary for a habitat.} So the answer is \textcolor{blue}{(b)}.  \\
        \midrule
         \textbf{[ARC-challenge]}
         \textit{Which process in the carbon cycle takes the longest to complete?} (a) emission of waste. (b) respiration in animals. (c) photosynthesis in plants. (d) formation of fossil fuels.
         & The process of \textcolor{red}{photosynthesis in plants takes the longest} to complete. So the answer is \textcolor{red}{(c)}.  
         & \textcolor{blue}{The formation of fossil fuels takes the longest time} to complete. So the answer is \textcolor{blue}{(d)}.  
         & The process that takes the longest time to complete is the formation of fossil fuels, \textcolor{blue}{which happens over millions of years}. So the answer is \textcolor{blue}{(d)}.  \\
         \bottomrule
    \end{tabular}
    % \vspace{-0.05in}
    \caption{Additional examples where self-consistency helps repair the errors over greedy decode on LaMDA-137B. Two sampled reasoning paths that are consistent with the ground truth are shown.}
    \label{tab:example_additional}
\end{table}
```

## Table 15
```latex
\begin{table}[h]
\setlength\tabcolsep{4pt}
\scriptsize
    \centering
    \begin{tabular}{p{3cm} | p{3.3cm} | p{3cm} | p{3.4cm} }
        Question & Greedy Decode & Sampled Path 1 & Sampled Path 2  \\
         \midrule
         \textbf{[GSM8K]} \textit{Kyle bought last year's best-selling book for \$19.50. This is with a 25\% discount from the original price. What was the original price of the book?} & The book was sold for \$19.50. This is 25\% less than the original price. This means the original price was 100\%. 25\% of 100\% is 25\%. So the original price was 100\% - 25\% = 75\%. \textcolor{red}{The original price was 75\% of \$19.50.} 75\% of \$19.50 is 75\% * \$19.50 = \$14.625. The answer is \textcolor{red}{\$14.625}. & The original price of the book is \$19.50. Since it was discounted by 25\%, \textcolor{blue}{the original price was 19.50 / 0.75 = 26}. The answer is \textcolor{blue}{26}. & Kyle bought a book that is sold for \$19.50. With a 25\% discount, the original price must be higher. If we call the original price x, then \textcolor{blue}{the discounted price is 0.75x}. Since this is \$19.50, we can write \textcolor{blue}{0.75x = 19.50}. Solving this, we find that the original price is \textcolor{blue}{x = 19.50 / 0.75 = \$26}. The answer is \textcolor{blue}{\$26}.\\
         \midrule
        \textbf{[AQuA]} \textit{The capacity of a tank of dimensions (8 m x 6 m x 2.5 m) is} (a) 120 litres (b) 1200 litres (c) 12000 litres (d) 120000 litres (e) None of these
         & The volume of the tank is 8 m * 6 m * 2.5 m = 120 m$^3$. So the capacity of the tank is \textcolor{red}{120 m$^3$}. So the answer is \textcolor{red}{(c)}.
         & The volume of the tank is 8m * 6m* 2.5m = 120m$^3$. This is \textcolor{blue}{equal to 120000 litres}. So the answer is \textcolor{blue}{(d)} 
         & 
         The volume of the tank is 8 m * 6 m * 2.5 m = 120 m3. \textcolor{blue}{One cubic meter contains 1000 litres, so the tank contains 120 m3 * 1000 liters/m3 = 120,000 liters}. So the answer is \textcolor{blue}{(d)}.\\
         \midrule
         \textbf{[StrategyQA]} \textit{Yes or no: Can the Great Depression be treated with Prozac?}
         & The Great Depression was an economic depression. Prozac is a drug used to treat depression. Thus, \textcolor{red}{the Great Depression could be treated with Prozac}. So the answer is \textcolor{red}{yes}.
         & Prozac is an anti-depressant medication. \textcolor{blue}{The Great Depression is not a disease}. Thus, Prozac cannot treat the Great Depression. So the answer is \textcolor{blue}{no}.
         & \textcolor{blue}{The Great Depression is a time period}. Prozac is used to treat depression (the mental illness). Thus, the Great Depression can not be treated with Prozac. So the answer is \textcolor{blue}{no}.\\
         \midrule
         \textbf{[ARC-easy]} \textit{Which source of energy is nonrenewable?} (a) coal. (b) sunlight. (c) water. (d) wood.
         & \textcolor{red}{Coal, sunlight, and water are all renewable sources of energy. Wood is a nonrenewable source of energy}. So the answer is \textcolor{red}{(d)}.
         & A nonrenewable source of energy is one in which the source is not replenished in a short amount of time. Thus, \textcolor{blue}{the only option that is nonrenewable is coal}. So the answer is \textcolor{blue}{(a)}.
         & \textcolor{blue}{Coal is a fossil fuel and is formed from dead organisms from the past}. \textcolor{blue}{Coal cannot be produced in a short period of time}, so it is considered a nonrenewable source of energy. So the answer is \textcolor{blue}{(a)}.\\
         \midrule
         \textbf{[ARC-challenge]}  \textit{Students studied the revolution of Earth around the Sun. During which month will Florida have the most sunlight energy available? 
} (a) March. (b) June. (c) September. (d) December.
        & \textcolor{red}{The Earth is closest to the Sun in December, hence Florida will have the most sunlight energy available in December.} So the answer is \textcolor{red}{(d)}.
        & \textcolor{blue}{Earth is closest to the Sun on June 21, the summer solstice}. So the answer is \textcolor{blue}{(b)}.
        & \textcolor{blue}{Florida is closer to the sun during June}, so it will have the most sunlight energy during that month. So the answer is \textcolor{blue}{(b)}.\\
         \bottomrule
    \end{tabular}
    % \vspace{0.05in}
    \caption{Additional examples where self-consistency helps repair the errors over greedy decode on PaLM-540B. Two sampled reasoning paths that are consistent with the ground truth are shown.}
    \label{tab:example_additional_palm}
\end{table}
```

## Table 16
```latex
\begin{table}[h]
    \caption{
    Few-shot exemplars for AQUA-RAT.
    }
    \centering
    \small
    \begin{tabular}{p{13.5cm}}
        \toprule
        \textbf{Q:} John found that the average of 15 numbers is 40. If 10 is added to each number then the mean of the numbers is? Answer Choices: (a) 50 (b) 45 (c) 65 (d) 78 (e) 64\\
        \vspace{-1mm}
        \textbf{A:} If 10 is added to each number, then the mean of the numbers also increases by 10. So the new mean would be 50. The answer is (a). \\
        \vspace{0mm}
        \textbf{Q:} If a / b = 3/4 and 8a + 5b = 22,then find the value of a. Answer Choices: (a) 1/2 (b) 3/2 (c) 5/2 (d) 4/2 (e) 7/2\\
        \vspace{-1mm}
        \textbf{A:} If a / b = 3/4, then b = 4a / 3. So 8a + 5(4a / 3) = 22. This simplifies to 8a + 20a / 3 = 22, which means 44a / 3 = 22. So a is equal to 3/2. The answer is (b).\\
        \vspace{0mm}
        \textbf{Q:} A person is traveling at 20 km/hr and reached his destiny in 2.5 hr then find the distance? Answer Choices: (a) 53 km (b) 55 km (c) 52 km (d) 60 km (e) 50 km\\
        \vspace{-1mm}
        \textbf{A:} The distance that the person traveled would have been 20 km/hr * 2.5 hrs = 50 km. The answer is (e).\\
        \vspace{0mm}
        \textbf{Q:} How many keystrokes are needed to type the numbers from 1 to 500? Answer Choices: (a) 1156 (b) 1392 (c) 1480 (d) 1562 (e) 1788\\
        \vspace{-1mm}
        \textbf{A:} There are 9 one-digit numbers from 1 to 9. There are 90 two-digit numbers from 10 to 99. There are 401 three-digit numbers from 100 to 500. 9 + 90(2) + 401(3) = 1392. The answer is (b).\\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-aqua}
\end{table}
```

## Table 17
```latex
\begin{table}[h]
    \caption{
    Few-shot exemplars for ARC easy/challenge.
    }
    \centering
    \small
    \begin{tabular}{p{13.5cm}}
        \toprule
        \textbf{Q:} George wants to warm his hands quickly by rubbing them. Which skin surface will produce the most heat? (a) dry palms. (b) wet palms. (c) palms covered with oil. (d) palms covered with lotion.\\
        \vspace{-1mm}
        \textbf{A:} Dry surfaces will more likely cause more friction via rubbing than other smoother surfaces, hence dry palms will produce the most heat. The answer is (a).\\
        \vspace{0mm}
        \textbf{Q:} Which factor will most likely cause a person to develop a fever? (a) a leg muscle relaxing after exercise. (b) a bacterial population in the bloodstream. (c) several viral particles on the skin. (d) carbohydrates being digested in the stomach.\\
        \vspace{-1mm}
        \textbf{A:} Option (b), bacterial population is the most likely cause for a person developing fever. The answer is (b). \\
        \vspace{0mm}
        \textbf{Q:} Which change in the state of water particles causes the particles to become arranged in a fixed position? (a) boiling. (b) melting. (c) freezing. (d) evaporating.\\
        \vspace{-1mm}
        \textbf{A:} When water is freezed, the particles are arranged in a fixed position; the particles are still moving for all other options. The answer is (c).\\
        \vspace{0mm}
        \textbf{Q:} When a switch is used in an electrical circuit, the switch can (a) cause the charge to build. (b) increase and decrease the voltage. (c) cause the current to change direction. (d) stop and start the flow of current.\\
        \vspace{-1mm}
        \textbf{A:} The function of a switch is to start and stop the flow of a current. The answer is (d).\\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-arc}
\end{table}
```

## Table 18
```latex
\begin{table}[h]
    \caption{
    Few-shot exemplars for HotpotQA (closed-book setting).
    }
    \centering
    \small
    \begin{tabular}{p{14cm}}
        \toprule
        \textbf{Q:} Which magazine was started first Arthur's Magazine or First for Women?\\
        \vspace{-1mm}
        \textbf{A:} Arthur's Magazine started in 1844. First for Women started in 1989. So Arthur's Magazine was started first. The answer is Arthur's Magazine.\\
        \vspace{0mm}
        \textbf{Q:} The Oberoi family is part of a hotel company that has a head office in what city?\\
        \vspace{-1mm}
        \textbf{A:} The Oberoi family is part of the hotel company called The Oberoi Group. The Oberoi Group has its head office in Delhi. The answer is Delhi. \\
        \vspace{0mm}
        \textbf{Q:} What nationality was James Henry Miller's wife?\\
        \vspace{-1mm}
        \textbf{A:} James Henry Miller's wife is June Miller. June Miller is an American. The answer is American.\\
        \vspace{0mm}
        \textbf{Q:} The Dutch-Belgian television series that "House of Anubis" was based on first aired in what year?\\
        \vspace{-1mm}
        \textbf{A:} "House of Anubis" is based on the Dutch–Belgian television series Het Huis Anubis. Het Huis Anubis is first aired in September 2006. The answer is 2006.\\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-hotpotqa}
\end{table}
```

## Table 19
```latex
\begin{table*}
    \caption{
    Few-shot exemplars for all arithmetic reasoning tasks, from \cite{wei2022chain}.
    }
    \centering
    \small
    \begin{tabular}{p{13.5cm}}
        \toprule
        \textbf{Q:} There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today? \\
        \vspace{-1mm}
        \textbf{A:} We start with 15 trees. Later we have 21 trees. The difference must be the number of trees they planted. So, they must have planted 21 - 15 = 6 trees. The answer is 6. \\
        \vspace{0mm}
        \textbf{Q:} If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot? \\
        \vspace{-1mm}
        \textbf{A:} There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5. \\
        \vspace{0mm}
        \textbf{Q:} Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total? \\
        \vspace{-1mm}
        \textbf{A:} Leah had 32 chocolates and Leah's sister had 42. That means there were originally 32 + 42 = 74 chocolates. 35 have been eaten. So in total they still have 74 - 35 = 39 chocolates. The answer is 39. \\
        \vspace{0mm}
        \textbf{Q:} Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny? \\
        \vspace{-1mm}
        \textbf{A:} Jason had 20 lollipops. Since he only has 12 now, he must have given the rest to Denny. The number of lollipops he has given to Denny must have been 20 - 12 = 8 lollipops. The answer is 8. \\
        \vspace{0mm}
        \textbf{Q:} Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now? \\
        \vspace{-1mm}
        \textbf{A:} He has 5 toys. He got 2 from mom, so after that he has 5 + 2 = 7 toys. Then he got 2 more from dad, so in total he has 7 + 2 = 9 toys. The answer is 9. \\
        \vspace{0mm}
        \textbf{Q:} There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room? \\
        \vspace{-1mm}
        \textbf{A:} There are 4 days from monday to thursday. 5 computers were added each day. That means in total 4 * 5 = 20 computers were added. There were 9 computers in the beginning, so now there are 9 + 20 = 29 computers. The answer is 29. \\
        \vspace{0mm}
        \textbf{Q:} Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday? \\
        \vspace{-1mm}
        \textbf{A:} Michael initially had 58 balls. He lost 23 on Tuesday, so after that he has 58 - 23 = 35 balls. On Wednesday he lost 2 more so now he has 35 - 2 = 33 balls. The answer is 33.\ \\
        \vspace{0mm}
        \textbf{Q:} Olivia has \$23. She bought five bagels for \$3 each. How much money does she have left? \\
        \vspace{-1mm}
        \textbf{A:} She bought 5 bagels for \$3 each. This means she spent 5 * \$3 = \$15 on the bagels. She had \$23 in beginning, so now she has \$23 - \$15 = \$8. The answer is 8. \\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-math}
    \vspace{-0.1in}
\end{table*}
```

## Table 20
```latex
\begin{table}[h]
    \caption{
    Few-shot exemplars for ANLI.
    }
    \centering
    \small
    \begin{tabular}{p{14cm}}
        \toprule
        Premise:\\
        "Conceptually cream skimming has two basic dimensions - product and geography."\\
        Based on this premise, can we conclude the hypothesis "Product and geography are what make cream skimming work." is true?\\
        OPTIONS:\\
        - yes\\
        - no\\
        - it is not possible to tell\\
        \vspace{-1mm}
        \textbf{A:} Based on "cream skimming has two basic dimensions" we can't infer that these two dimensions are what make cream skimming work. The answer is it is not possible to tell.\\
        \vspace{0mm}
        Premise:\\
        "One of our member will carry out your instructions minutely."\\
        Based on this premise, can we conclude the hypothesis "A member of my team will execute your orders with immense precision." is true?\\
        OPTIONS:\\
        - yes\\
        - no\\
        - it is not possible to tell\\
        \vspace{-1mm}
        \textbf{A:} "one of" means the same as "a member of", "carry out" means the same as "execute", and "minutely" means the same as "immense precision". The answer is yes.\\
        \vspace{0mm}
        Premise:\\
        "Fun for adults and children."\\
        Based on this premise, can we conclude the hypothesis "Fun for only children." is true?\\
        OPTIONS:\\
        - yes\\
        - no\\
        - it is not possible to tell\\
        \vspace{-1mm}
        \textbf{A:} "adults and children" contradicts "only children". The answer is no.\\
        \vspace{0mm}
        Premise:\\
        "He turned and smiled at Vrenna."\\
        Based on this premise, can we conclude the hypothesis "He smiled at Vrenna who was walking slowly behind him with her mother." is true?\\
        OPTIONS:\\
        - yes\\
        - no\\
        - it is not possible to tell\\
        \vspace{-1mm}
        \textbf{A:} the premise does not say anything about "Vrenna was walking". The answer is it is not possible to tell.\\
        \vspace{0mm}
        Premise:\\
        "well you see that on television also"\\
        Based on this premise, can we conclude the hypothesis "You can see that on television, as well." is true?\\
        OPTIONS:\\
        - yes\\
        - no\\
        - it is not possible to tell\\
        \vspace{-1mm}
        \textbf{A:} "also" and "as well" mean the same thing. The answer is yes.\\
        \vspace{0mm}
        Premise:\\
        "Vrenna and I both fought him and he nearly took us."\\
        Based on this premise, can we conclude the hypothesis "Neither Vrenna nor myself have ever fought him." is true?\\
        OPTIONS:\\
        - yes\\
        - no\\
        - it is not possible to tell\\
        \vspace{-1mm}
        \textbf{A:} "Vrenna and I both" contradicts "neither Vrenna nor myself". The answer is no.\\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-nli}
\end{table}
```

## Table 21
```latex
\begin{table}[h]
    \caption{
    Few-shot exemplars for e-SNLI (the rationales are crowd-sourced annotations from the original dataset).
    }
    \centering
    \small
    \begin{tabular}{p{14cm}}
        \toprule
        Premise:\\
"A person on a horse jumps over a broken down airplane."\\
Based on this premise, can we conclude the hypothesis "A person is training his horse for a competition." is true?\\
OPTIONS:\\
- yes\\
- no\\
- it is not possible to tell\\
\textbf{A:} The person is not necessarily training his horse. The answer is it is not possible to tell.\\
\vspace{0mm}
Premise:\\
"A person on a horse jumps over a broken down airplane."\\
Based on this premise, can we conclude the hypothesis "A person is at a diner, ordering an omelette." is true?\\
OPTIONS:\\
- yes\\
- no\\
- it is not possible to tell\\
\textbf{A:} One jumping horse cannot be in a diner ordering food. The answer is no.\\
\vspace{0mm}
Premise:\\
"A person on a horse jumps over a broken down airplane."\\
Based on this premise, can we conclude the hypothesis "A person is outdoors, on a horse." is true?\\
OPTIONS:\\
- yes\\
- no\\
- it is not possible to tell\\
\textbf{A:} A broken down airplane is outdoors. The answer is yes.\\
\vspace{0mm}
Premise:\\
"Children smiling and waving at camera."\\
Based on this premise, can we conclude the hypothesis "They are smiling at their parents." is true?\\
OPTIONS:\\
- yes\\
- no\\
- it is not possible to tell\\
\textbf{A:} Just because they are smiling and waving at a camera does not imply their parents or anyone is anyone behind it. The answer is it is not possible to tell.\\
\vspace{0mm}
Premise:\\
"Children smiling and waving at camera."\\
Based on this premise, can we conclude the hypothesis "The kids are frowning." is true?
OPTIONS:\\
- yes\\
- no\\
- it is not possible to tell\\
\textbf{A:} One cannot be smiling and frowning at the same time. The answer is no.\\
\vspace{0mm}
Premise:\\
"Children smiling and waving at camera."\\
Based on this premise, can we conclude the hypothesis "There are children present." is true?\\
OPTIONS:\\
- yes\\
- no\\
- it is not possible to tell\\
\textbf{A:}The children must be present to see them smiling and waving. The answer is yes.\\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-esnli}
\end{table}
```

## Table 22
```latex
\begin{table}[h]
    \caption{
    Few-shot exemplars for RTE.
    }
    \centering
    \small
    \begin{tabular}{p{14cm}}
        \toprule
        Premise:\\
        "No Weapons of Mass Destruction Found in Iraq Yet."\\
        Based on this premise, can we conclude the hypothesis "Weapons of Mass Destruction Found in Iraq." is true?\\
        \vspace{-1mm}
        \textbf{A:} "No Weapons of Mass Destruction Found" contradicts "Weapons of Mass Destruction Found". The answer is no.\\
        \vspace{0mm}
        Premise:\\
        "A place of sorrow, after Pope John Paul II died, became a place of celebration, as Roman Catholic faithful gathered in downtown Chicago to mark the installation of new Pope Benedict XVI."\\
        Based on this premise, can we conclude the hypothesis "Pope Benedict XVI is the new leader of the Roman Catholic Church." is true?'\\
        \vspace{-1mm}
        \textbf{A:} "installation of new Pope Benedict XVI." means "Pope Benedict XVI is the new leader". The answer is yes. \\
        \vspace{0mm}
        Premise:\\
        "A man is due in court later charged with the murder 26 years ago of a teenager whose case was the first to be featured on BBC One's Crimewatch. Colette Aram, 16, was walking to her boyfriend's house in Keyworth, Nottinghamshire, on 30 October 1983 when she disappeared. Her body was later found in a field close to her home. Paul Stewart Hutchinson, 50, has been charged with murder and is due before Nottingham magistrates later."\\
        Based on this premise, can we conclude the hypothesis "Paul Stewart Hutchinson is accused of having stabbed a girl." is true?\\
        \vspace{-1mm}
        \textbf{A:} The premise does not say Paul Stewart Hutchinson "stabbed" this girl. The answer is no.\\
        \vspace{0mm}
        Premise:\\
        "Herceptin was already approved to treat the sickest breast cancer patients, and the company said, Monday, it will discuss with federal regulators the possibility of prescribing the drug for more breast cancer patients."\\
        Based on this premise, can we conclude the hypothesis "Herceptin can be used to treat breast cancer." is true?\\
        \vspace{-1mm}
        \textbf{A:} "Herceptin was approved to treat breast cancer" implies that "Herceptin can be used to treat breast cancer". The answer is yes.\\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-rte}
\end{table}
```

## Table 23
```latex
\begin{table}[h]
    \caption{
    Few-shot exemplars for BoolQ (closed-book setting).
    }
    \centering
    \small
    \begin{tabular}{p{14cm}}
        \toprule
        \textbf{Q:} does system of a down have 2 singers?\\
        \vspace{-1mm}
        \textbf{A:} System of a Down currently consists of Serj Tankian, Daron Malakian, Shavo Odadjian and John Dolmayan. Serj and Daron do vocals, so the band does have two singers. The answer is yes.\\
        \vspace{0mm}
        \textbf{Q:} do iran and afghanistan speak the same language?\\
        \vspace{-1mm}
        \textbf{A:} Iran and Afghanistan both speak the Indo-European language Persian. The answer is yes. \\
        \vspace{0mm}
        \textbf{Q:} is a cello and a bass the same thing?\\
        \vspace{-1mm}
        \textbf{A:} The cello is played sitting down with the instrument between the knees, whereas the double bass is played standing or sitting on a stool. The answer is no.\\
        \vspace{0mm}
        \textbf{Q:} can you use oyster card at epsom station?\\
        \vspace{-1mm}
        \textbf{A:} Epsom railway station serves the town of Epsom in Surrey and is not in the London Oyster card zone. The answer is no.\\
        \bottomrule
    \end{tabular}
    \label{tab:prompt-boolq-cb}
\end{table}
```

