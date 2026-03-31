# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[H]
\caption{Top instructions with the highest GSM8K zero-shot test accuracies from prompt optimization with different optimizer LLMs. All results use the pre-trained \texttt{PaLM 2-L} as the scorer. 
}
\centering
\scalebox{0.81}{
\begin{tabular}{P{3.5cm}P{10.5cm}P{1cm}}
\toprule
Source & Instruction & Acc \\
\midrule
\multicolumn{3}{l}{\textit{Baselines}} \\
\hdashline\noalign{\vskip 0.5ex}
\citep{kojima2022large} & Let's think step by step. & 71.8 \\
\citep{zhou2022large} & Let’s work this out in a step by step way to be sure we have the right answer. & 58.8 \\
& (empty string) & 34.0 \\
\midrule
\multicolumn{3}{l}{\textit{Ours}} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{PaLM 2-L-IT} & Take a deep breath and work on this problem step-by-step. & \textbf{80.2} \\
\texttt{PaLM 2-L} & Break this down. & 79.9 \\
\texttt{gpt-3.5-turbo} & A little bit of arithmetic and a logical approach will help us quickly arrive at the solution to this problem. & 78.5 \\
\texttt{gpt-4} & Let's combine our numerical command and clear thinking to quickly and accurately decipher the answer. & 74.5\\
\bottomrule
\end{tabular}}
\label{table:gsm8k_top_instructions_in_intro}
\end{table}
```

## Table 2
```latex
\begin{table}
\centering
\caption{Linear regression by optimizer LLMs: the mean $\pm$ standard deviation of the number of steps and the number of unique $(w, b)$ pairs explored before reaching the global optima.
Both $w$ and $b$ start from 5 random starting points in $[10, 20]$.
We use temperature 1.0 for all models.
We run each setting 5 times.
The starting points are the same across optimizer LLMs but are different across 5 runs, and are grouped by: within the starting region, outside and close to the starting region, and outside and farther from the starting region.
Bold numbers indicate the best among three LLMs in each setting.
}
\scalebox{0.8}{
\begin{tabular}{cccccccc}
\toprule
\multirow{2}{*}{$w_\text{true}$} & \multirow{2}{*}{$b_\text{true}$} & \multicolumn{3}{c}{number of steps} & \multicolumn{3}{c}{number of unique $(w, b)$ pairs explored} \\ \cmidrule(lr){3-5} \cmidrule(lr){6-8}
& & \texttt{text-bison} & \texttt{gpt-3.5-turbo} & \texttt{gpt-4} & \texttt{text-bison} & \texttt{gpt-3.5-turbo} & \texttt{gpt-4} \\
\midrule
15 & 14 & 5.8 \scriptsize{$\pm$ 2.6} & 7.6 \scriptsize{$\pm$ 4.5} & \textbf{4.0} \scriptsize{$\pm$ 1.5} & 40.0 \scriptsize{$\pm$ 12.4}
 & 36.0 \scriptsize{$\pm$ 15.2} & \textbf{17.2} \scriptsize{$\pm$ 5.1} \\
17 & 17 & \textbf{4.0} \scriptsize{$\pm$ 1.8} & 12.6 \scriptsize{$\pm$ 6.0} & 6.0 \scriptsize{$\pm$ 3.7} & 33.4 \scriptsize{$\pm$ 11.7} & 53.8 \scriptsize{$\pm$ 16.9} & \textbf{26.0} \scriptsize{$\pm$ 10.6} \\
16 & 10 & \textbf{3.8} \scriptsize{$\pm$ 2.2} & 10.4 \scriptsize{$\pm$ 5.4} & 6.2 \scriptsize{$\pm$ 3.1} & 30.2 \scriptsize{$\pm$ 13.4} & 42.8 \scriptsize{$\pm$ 16.3} & \textbf{24.2} \scriptsize{$\pm$ 8.2} \\
\hdashline\noalign{\vskip 0.5ex}
3 & 5 & \textbf{9.8} \scriptsize{$\pm$ 2.8} & 10.8 \scriptsize{$\pm$ 2.7} & 12.2 \scriptsize{$\pm$ 2.0} & 55.8 \scriptsize{$\pm$ 16.1} & 39.6 \scriptsize{$\pm$ 10.1} & \textbf{33.0} \scriptsize{$\pm$ 4.0} \\
25 & 23 & 19.6 \scriptsize{$\pm$ 11.4} & 26.4 \scriptsize{$\pm$ 18.3} & \textbf{12.2} \scriptsize{$\pm$ 3.7} & 104.0 \scriptsize{$\pm$ 52.3} & 78.6 \scriptsize{$\pm$ 26.2} & \textbf{44.2} \scriptsize{$\pm$ 8.3} \\
\hdashline\noalign{\vskip 0.5ex}
2 & 30 & \textbf{31.4} \scriptsize{$\pm$ 6.3} & 42.8 \scriptsize{$\pm$ 9.7} & 38.0 \scriptsize{$\pm$ 15.9} & 126.4 \scriptsize{$\pm$ 17.7} & 125.6 \scriptsize{$\pm$ 21.7} & \textbf{99.0} \scriptsize{$\pm$ 24.6} \\
36 & -1 & \textbf{35.8} \scriptsize{$\pm$ 6.4} & 45.4 \scriptsize{$\pm$ 16.9} & 50.4 \scriptsize{$\pm$ 18.8} & 174.0 \scriptsize{$\pm$ 28.2} & 142.2 \scriptsize{$\pm$ 31.2} & \textbf{116.4} \scriptsize{$\pm$ 32.7} \\
\bottomrule
\end{tabular}
}
\label{table:linear_regression_results_in_main_paper}
\end{table}
```

## Table 3
```latex
\begin{table}
\centering
\caption{Results of the Traveling Salesman Problem (TSP) with different number of nodes $n$, where each $n$ contains 5 problems. ``\# steps'' calculates the mean $\pm$ standard error of optimization steps for successful runs that find the optimal solution. ``\# successes'' counts the number of problems that \name{} results in the optimal solution. When no optimal solution is found for any evaluated problem, the corresponding number of steps is N/A.
}
\scalebox{0.7}{
\begin{tabular}{ccccccccc}
\toprule
\multirow{2}{*}{$n$} & \multicolumn{5}{c}{optimality gap (\%)} & \multicolumn{3}{c}{\# steps (\# successes)} \\ \cmidrule(lr){2-6} \cmidrule(lr){7-9}
& NN & FI & \texttt{text-bison} & \texttt{gpt-3.5-turbo} & \texttt{gpt-4} & \texttt{text-bison} & \texttt{gpt-3.5-turbo} & \texttt{gpt-4} \\
\midrule
10 & 13.0 \scriptsize{$\pm$ 1.3} & 3.2 \scriptsize{$\pm$ 1.4} & \textbf{0.0} \scriptsize{$\pm$ 0.0} & \textbf{0.0} \scriptsize{$\pm$ 0.0} & \textbf{0.0} \scriptsize{$\pm$ 0.0} & 40.4 \scriptsize{$\pm$ 5.6} \textbf{\footnotesize{ (5)}} & 46.8 \scriptsize{$\pm$ 9.3} \textbf{\footnotesize{ (5)}} & \textbf{9.6} \scriptsize{$\pm$ 3.0} \textbf{\footnotesize{ (5)}}\\
15 & 9.4 \scriptsize{$\pm$ 3.7} & 1.2 \scriptsize{$\pm$ 0.6} & 4.4 \scriptsize{$\pm$ 1.3} & 1.2 \scriptsize{$\pm$ 1.1} & \textbf{0.2} \scriptsize{$\pm$ 0.2} & N/A (0) & 202.0 \scriptsize{$\pm$ 41.1} \textbf{\footnotesize{ (4)}} & \textbf{58.5} \scriptsize{$\pm$ 29.0} \textbf{\footnotesize{ (4)}} \\
20 & 16.0\scriptsize{$\pm$ 3.9} & \textbf{0.2}\scriptsize{$\pm$ 0.1} & 30.4 \scriptsize{$\pm$ 10.6}  & 4.4 \scriptsize{$\pm$ 2.5} & 1.4 \scriptsize{$\pm$ 0.6} & N/A (0) & 438.0 \scriptsize{$\pm$ 0.0} \footnotesize{ (1)} &  \textbf{195.5} \scriptsize{$\pm$ 127.6} \textbf{\footnotesize{ (2)}} \\
50 & 19.7 \scriptsize{$\pm$ 3.1} & \textbf{9.8} \scriptsize{$\pm$ 1.5} & 219.8 \scriptsize{$\pm$ 13.7}  & 133.0 \scriptsize{$\pm$ 6.8} & 11.0 \scriptsize{$\pm$ 2.6} & N/A (0) & N/A (0) &  N/A (0)\\
\bottomrule
\end{tabular}
}
\label{table:tsp_main_results}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
\footnotesize
\caption{Test accuracies on GSM8K. We show the instruction with the highest test accuracy for each scorer-optimizer pair. 
}
\begin{center}
\scalebox{0.86}{
\begin{tabular}{cP{2cm}P{1.5cm}P{8cm}c}
\toprule
Scorer & Optimizer / Source & Instruction position & Top instruction & Acc \\
\midrule
\multicolumn{3}{l}{\textit{Baselines}} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{PaLM 2-L} & \citep{kojima2022large} & A\_begin & Let's think step by step. & 71.8 \\ [1ex]
\texttt{PaLM 2-L} & \citep{zhou2022large} & A\_begin & Let’s work this out in a step by step way to be sure we have the right answer. & 58.8 \\ [3ex]
\texttt{PaLM 2-L} & & A\_begin & Let's solve the problem. & 60.8 \\ [1ex]
\texttt{PaLM 2-L} & & A\_begin & (empty string) & 34.0 \\ [1ex]
\texttt{text-bison} & \citep{kojima2022large} & Q\_begin & Let's think step by step. & 64.4 \\ [1ex]
\texttt{text-bison} & \citep{zhou2022large} & Q\_begin & Let’s work this out in a step by step way to be sure we have the right answer. & 65.6 \\ [3ex]
\texttt{text-bison} & & Q\_begin & Let's solve the problem. & 59.1 \\ [1ex]
\texttt{text-bison} & & Q\_begin & (empty string) & 56.8 \\
\midrule
\multicolumn{3}{l}{\textit{Ours}} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{PaLM 2-L} & \texttt{PaLM 2-L-IT} & A\_begin & Take a deep breath and work on this problem step-by-step. & \textbf{80.2} \\ [1ex]
\texttt{PaLM 2-L} & \texttt{PaLM 2-L} & A\_begin & Break this down. & 79.9 \\ [1ex]
\texttt{PaLM 2-L} & \texttt{gpt-3.5-turbo} & A\_begin & A little bit of arithmetic and a logical approach will help us quickly arrive at the solution to this problem. & 78.5 \\ [3ex]
\texttt{PaLM 2-L} & \texttt{gpt-4} & A\_begin & Let's combine our numerical command and clear thinking to quickly and accurately decipher the answer. & 74.5 \\ [3ex]
\texttt{text-bison} & \texttt{PaLM 2-L-IT} & Q\_begin & Let's work together to solve math word problems! First, we will read and discuss the problem together to make sure we understand it. Then, we will work together to find the solution. I will give you hints and help you work through the problem if you get stuck. & 64.4 \\ [3ex]
\texttt{text-bison} & \texttt{text-bison} & Q\_end & Let's work through this problem step-by-step: & \textbf{68.5} \\ [1ex]
\texttt{text-bison} & \texttt{gpt-3.5-turbo} & Q\_end & Analyze the given information, break down the problem into manageable steps, apply suitable mathematical operations, and provide a clear, accurate, and concise solution, ensuring precise rounding if necessary. Consider all variables and carefully consider the problem's context for an efficient solution. & 66.5 \\ [5ex]
\texttt{text-bison} & \texttt{gpt-4} & Q\_begin & Start by dissecting the problem to highlight important numbers and their relations. Decide on the necessary mathematical operations like addition, subtraction, multiplication, or division, required for resolution. Implement these operations, keeping in mind any units or conditions. Round off by ensuring your solution fits the context of the problem to ensure accuracy. & 62.7 \\
\bottomrule
\end{tabular}}
\end{center}
\label{table:top_instructions_on_gsm8k}
\end{table}
```

## Table 5
```latex
\begin{table}
\centering
\caption{Top instructions with the highest accuracies found in prompt optimization on BBH movie\_recommendation, ruin\_names, and temporal\_sequences.}
\scalebox{0.85}{
\begin{tabular}{P{2.0cm}P{2.5cm}P{1.2cm}P{7.5cm}c}
\toprule
Scorer & Optimizer & Instruction position & Instruction & Acc \\
\midrule
\multicolumn{3}{l}{\textit{movie\_recommendation}} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{PaLM 2-L} & \texttt{PaLM 2-L-IT} & A\_begin & Based on your input, I have analyzed the given movies in terms of genre, plot, tone, audience rating, year of release, director, cast, and reviews. I have also taken into account the given options. The movie that is most similar to the given movies in terms of all these factors is: & 90.8 \\ [13ex]
\texttt{PaLM 2-L} & \texttt{PaLM 2-L} & A\_begin & The best film: & 88.4 \\ [1ex]
\texttt{PaLM 2-L} & \texttt{gpt-3.5-turbo} & A\_begin & Let's uncover the perfect movie recommendation from the options provided, ensuring an exceptional cinematic experience together as we select the most captivating and satisfying choice that will keep us thoroughly engaged and immersed until the very end. & 88.0 \\ [12ex]
\texttt{text-bison} & \texttt{PaLM 2-L-IT} & Q\_begin & What is the highest-rated movie similar to the given movies, with a similar IMDb rating and released in the same year? & 91.6 \\ [7ex]
\texttt{text-bison} & \texttt{gpt-3.5-turbo} & Q\_begin & Based on the movie list provided, carefully consider your preferences and make a well-informed decision. & 70.8 \\
\midrule
\multicolumn{3}{l}{\textit{ruin\_names}} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{PaLM 2-L} & \texttt{PaLM 2-L-IT} & A\_begin & Which is the funniest pun on the artist or movie name? & 88.0 \\ [1ex]
\texttt{PaLM 2-L} & \texttt{PaLM 2-L} & A\_begin & Answer for ruin: & 83.6 \\ [1ex]
\texttt{PaLM 2-L} & \texttt{gpt-3.5-turbo} & A\_begin & Prepare to have a side-splittingly funny time as we uncover the most clever and hilarious alternatives for these artist or movie names, challenging your wit to guess the correct one with a burst of creativity, humor, and imaginative twists! & 86.8 \\ [12ex]
\texttt{text-bison} & \texttt{PaLM 2-L-IT} & Q\_begin & A humorous edit of an artist or movie name can be created by replacing one or more letters to form a new word or phrase that sounds similar but has a different meaning. The new word or phrase should be relevant to the original word, but it should also be a surprise, which makes the edit funny. For example, the artist or movie name "Rocky" can be changed to "Ricky," and "Schindler's List" can be changed to "Schindler's Lift." Be creative and have fun! & 83.6 \\ [22ex]
\texttt{text-bison} & \texttt{gpt-3.5-turbo} & Q\_begin & Choose the option that offers the most clever and humorous alteration of the given artist or movie name. Let your creativity shine and select the answer that will undoubtedly bring a smile to your face! Make sure to think outside the box! & 75.2 \\
\midrule
\multicolumn{5}{l}{\textit{temporal\_sequences} (no \texttt{PaLM 2-L} as scorer results because its training accuracy on empty string is 100.0)} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{text-bison} & \texttt{PaLM 2-L-IT} & Q\_begin & To determine the time period when a person went to a place, first identify all the time periods when the person's whereabouts are unknown. Then, rule out any time periods during which the person was seen doing something else or the place was closed. The remaining time periods are the possible times when the person could have gone to the place. & 80.4 \\ [18ex]
\texttt{text-bison} & \texttt{gpt-3.5-turbo} & Q\_begin & Identify the optimal time slot for the individual to engage in the mentioned location/activity considering the given sightings and waking up time, taking into account the opening and closing times of the location and the duration of each event. & 53.6 \\
\bottomrule
\end{tabular}
}
\label{table:top_instructions_on_bbh_tasks_main_paper}
\end{table}
```

## Table 6
```latex
\begin{table}
\footnotesize
\caption{Transferability across datasets: accuracies of top instructions found for GSM8K on MultiArith and AQuA.
}
\begin{center}
\scalebox{0.9}{
\begin{tabular}{cP{2.2cm}P{1.5cm}P{5cm}cc}
\toprule
\multirow{2}{*}{Scorer} & \multirow{2}{*}{Source} & \multirow{2}{*}{\parbox{1.5cm} {\centering Instruction position}} & \multirow{2}{*}{Instruction} & \multicolumn{2}{c}{Accuracy} \\ \cmidrule{5-6}
& & & & MultiArith & AQuA \\
\midrule
\multicolumn{3}{l}{\textit{Baselines}} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{PaLM 2-L} & \citep{kojima2022large} & A\_begin & Let's think step by step. & 85.7 & 44.9 \\ [1ex]
\texttt{PaLM 2-L} & \citep{zhou2022large} & A\_begin & Let’s work this out in a step by step way to be sure we have the right answer. & 72.8 & 48.4 \\ [3ex]
\texttt{PaLM 2-L} & & A\_begin & Let's solve the problem. & 87.5 & 44.1 \\ [1ex]
\texttt{PaLM 2-L} & & A\_begin & (empty string) & 69.3 & 37.8 \\ [1ex]
\texttt{text-bison} & \citep{kojima2022large} & Q\_begin & Let's think step by step. & 92.5 & 31.9 \\ [1ex]
\texttt{text-bison} & \citep{zhou2022large} & Q\_begin & Let’s work this out in a step by step way to be sure we have the right answer. & 93.7 & 32.3 \\ [3ex]
\texttt{text-bison} & & Q\_begin & Let's solve the problem. & 85.5 & 29.9 \\ [1ex]
\texttt{text-bison} & & Q\_begin & (empty string) & 82.2 & 33.5 \\
\midrule
\multicolumn{3}{l}{\textit{Ours}} \\
\hdashline\noalign{\vskip 0.5ex}
\texttt{PaLM 2-L} & \texttt{PaLM 2-L-IT} on GSM8K & A\_begin & Take a deep breath and work on this problem step-by-step. & \textbf{95.3} & \textbf{54.3} \\ [4ex]
\texttt{text-bison} & \texttt{PaLM 2-L-IT} on GSM8K & Q\_begin & Let's work together to solve math word problems! First, we will read and discuss the problem together to make sure we understand it. Then, we will work together to find the solution. I will give you hints and help you work through the problem if you get stuck. & \textbf{96.8} & \textbf{37.8} \\
\bottomrule
\end{tabular}
}
\end{center}
\label{table:ins_performance_on_multiarith}
\end{table}
```

## Table 7
```latex
\begin{table}[H]
\scriptsize
\caption{Accuracies on BBH tasks: our found instructions with the \texttt{PaLM 2-L-IT} optimizer vs baseline.
The optimization starts from the empty string.
Because of the 20-80 train-test split, we show accuracies with the format ``training / test / overall (training + test)''.
The \texttt{PaLM 2-L} scores are from A\_begin instructions; the \texttt{text-bison} scores are from Q\_begin instructions.
Bold numbers indicate the best for the corresponding task.
}
\begin{center}
\scalebox{0.85}{
\begin{tabular}{cP{1.2cm}P{2.2cm}P{2.2cm}P{2.2cm}P{2.2cm}}
\toprule
\multirow{2}{*}{Task} & \multirow{2}{*}{Scorer} & Our Acc & ``Let's think step by step.'' Acc & ``Let’s work this out in a step by step way to be sure we have the right answer.'' Acc & empty string ``'' Acc \\ \cmidrule(lr){3-3} \cmidrule(lr){4-4} \cmidrule(lr){5-5} \cmidrule(lr){6-6}
& & training / test / overall & training / test / overall & training / test / overall & training / test / overall \\
\midrule
boolean\_expressions & \texttt{PaLM 2-L} & \textbf{90.0 / 83.5 / 84.8} & 90.0 / 83.0 / 84.4 & 82.0 / 74.0 / 75.6 & 74.0 / 71.0 / 71.6 \\
causal\_judgement & \texttt{PaLM 2-L} & \textbf{84.8 / 58.0 / 63.1} & 73.0 / 55.3 / 58.8 & 59.5 / 57.3 / 57.8 & 29.7 / 49.3 / 45.5 \\
date\_understanding & \texttt{PaLM 2-L} & \textbf{86.0 / 84.5 / 84.8} & 76.0 / 80.0 / 79.2 & 74.0 / 77.0 / 76.4 & 70.0 / 74.0 / 73.2 \\
disambiguation\_qa & \texttt{PaLM 2-L} & \textbf{80.0 / 69.0 / 71.2} & 40.0 / 52.5 / 50.0 & 48.0 / 47.0 / 47.2 & 54.0 / 57.5 / 56.8 \\
dyck\_languages & \texttt{PaLM 2-L} & \textbf{100.0 / 100.0 / 100.0} & 96.0 / 94.5 / 94.8 & 100.0 / 93.5 / 94.8 & 94.0 / 95.0 / 94.8 \\
formal\_fallacies & \texttt{PaLM 2-L} & \textbf{84.0 / 64.0 / 68.4} & 78.0 / 59.5 / 63.2 & 68.0 / 63.0 / 64.0 & 66.0 / 59.0 / 60.4 \\
geometric\_shapes & \texttt{PaLM 2-L} & \textbf{76.0 / 57.0 / 60.8} & 42.0 / 33.0 / 34.8 & 42.0 / 32.0 / 34.0 & 34.0 / 33.0 / 33.2 \\
hyperbaton & \texttt{PaLM 2-L} & \textbf{100.0 / 96.0 / 96.8} & 78.0 / 75.0 / 75.6 & 74.0 / 72.5 / 72.8 & 88.0 / 89.0 / 88.8 \\
logical\_deduction\_seven\_objects & \texttt{PaLM 2-L} & \textbf{74.0 / 57.0 / 60.4} & 46.0 / 37.0 / 38.8 & 34.0 / 30.5 / 31.2 & 46.0 / 45.5 / 45.6 \\
movie\_recommendation & \texttt{PaLM 2-L} & \textbf{92.0 / 90.5 / 90.8} & 62.0 / 52.5 / 54.4 & 52.0 / 48.0 / 48.8 & 80.0 / 83.0 / 82.4 \\
multistep\_arithmetic\_two & \texttt{PaLM 2-L} & \textbf{72.0 / 55.5 / 58.8} & 42.0 / 46.0 / 45.2 & 60.0 / 50.5 / 52.4 & 4.0 / 3.5 / 3.6 \\
navigate & \texttt{PaLM 2-L} & \textbf{92.0 / 75.0 / 78.4} & 68.0 / 62.0 / 63.2 & 70.0 / 64.0 / 65.2 & 38.0 / 37.5 / 37.6 \\
object\_counting & \texttt{PaLM 2-L} & \textbf{84.0 / 86.5 / 86.0} & 36.0 / 46.5 / 44.4 & 60.0 / 62.0 / 61.6 & 28.0 / 27.0 / 27.2 \\
penguins\_in\_a\_table & \texttt{PaLM 2-L} & \textbf{86.2 / 71.8 / 74.7} & 79.3 / 64.1 / 67.1 & 62.1 / 58.1 / 58.9 & 72.4 / 69.2 / 69.9 \\
reasoning\_about\_colored\_objects & \texttt{PaLM 2-L} & \textbf{98.0 / 85.5 / 88.0} & 82.0 / 79.5 / 80.0 & 82.0 / 75.0 / 76.4 & 42.0 / 35.0 / 36.4 \\
ruin\_names & \texttt{PaLM 2-L} & \textbf{88.0 / 88.0 / 88.0} & 70.0 / 55.0 / 58.0 & 80.0 / 75.5 / 76.4 & 88.0 / 76.5 / 78.8 \\
salient\_translation\_error\_detection & \texttt{PaLM 2-L} & \textbf{62.0 / 67.0 / 66.0} & 42.0 / 50.0 / 48.4 & 58.0 / 46.0 / 48.4 & 56.0 / 56.5 / 56.4 \\
snarks & \texttt{PaLM 2-L} & \textbf{85.7 / 83.2 / 83.7} & 60.0 / 62.2 / 61.8 & 54.3 / 53.1 / 53.4 & 51.4 / 60.1 / 58.4 \\
sports\_understanding & \texttt{PaLM 2-L} & \textbf{98.0 / 88.0 / 90.0} & 50.0 / 46.5 / 47.2 & 60.0 / 52.5 / 54.0 & 52.0 / 41.5 / 43.6 \\
temporal\_sequences & \texttt{PaLM 2-L} & \textbf{100.0 / 100.0 / 100.0} & 100.0 / 96.0 / 96.8 & 90.0 / 87.0 / 87.6 & 100.0 / 99.5 / 99.6 \\
tracking\_shuffled\_objects\_seven\_objects & \texttt{PaLM 2-L} & 32.0 / 16.5 / 19.6 & \textbf{58.0 / 61.5 / 60.8} & 54.0 / 55.5 / 55.2 & 14.0 / 23.5 / 21.6 \\
web\_of\_lies & \texttt{PaLM 2-L} & \textbf{62.0 / 52.0 / 54.0} & 46.0 / 41.5 / 42.4 & 24.0 / 31.0 / 29.6 & \textbf{54.0 / 54.0 / 54.0} \\
word\_sorting & \texttt{PaLM 2-L} & \textbf{54.0 / 54.5 / 54.4} & 2.0 / 4.5 / 4.0 & 12.0 / 9.5 / 10.0 & 20.0 / 22.5 / 22.0 \\
\hdashline\noalign{\vskip 0.5ex}
boolean\_expressions & \texttt{text-bison} & \textbf{98.0 / 87.0 / 89.2} & 72.0 / 61.5 / 63.6 & 88.0 / 78.0 / 80.0 &  80.0 / 68.5 / 70.8 \\
causal\_judgement & \texttt{text-bison} & \textbf{78.4 / 58.0 / 62.0} & 70.3 / 50.7 / 54.5 & 73.0 / 55.3 / 58.8 & \textbf{78.4 / 58.0 / 62.0} \\
date\_understanding & \texttt{text-bison} & \textbf{60.0 / 50.0 / 52.0} & 44.0 / 45.5 / 45.2 & 48.0 / 45.0 / 45.6 &  44.0 / 45.0 / 44.8 \\
disambiguation\_qa & \texttt{text-bison} & \textbf{68.0 / 73.0 / 72.0} & 4.0 / 6.0 / 5.6 & 4.0 / 15.5 / 13.2 & 52.0 / 68.5 / 65.2 \\
dyck\_languages & \texttt{text-bison} & \textbf{100.0 / 100.0 / 100.0} & 100.0 / 95.5 / 96.4 & 100.0 / 94.5 / 95.6 & 100.0 / 98.5 / 98.8 \\
formal\_fallacies & \texttt{text-bison} & 70.0 / 53.0 / 56.4 & 64.0 / 54.5 / 56.4 & \textbf{84.0 / 82.5 / 82.8} & 70.0 / 54.5 / 57.6 \\
geometric\_shapes & \texttt{text-bison} & \textbf{40.0 / 19.5 / 23.6} & 22.0 / 13.0 / 14.8 & 18.0 / 12.0 / 13.2 & 20.0 / 14.5 / 15.6 \\
hyperbaton & \texttt{text-bison} & \textbf{80.0 / 79.5 / 79.6} & 64.0 / 67.5 / 66.8 & 64.0 / 69.0 / 68.0 & 64.0 / 64.0 / 64.0 \\
logical\_deduction\_seven\_objects & \texttt{text-bison} & 66.0 / 53.5 / 56.0 & \textbf{56.0 / 58.0 / 57.6} & 56.0 / 56.0 / 56.0 & 58.0 / 56.5 / 56.8 \\
movie\_recommendation & \texttt{text-bison} & \textbf{98.0 / 90.0 / 91.6} & 68.0 / 63.0 / 64.0 & 66.0 / 62.0 / 62.8 & 68.0 / 64.0 / 64.8 \\
multistep\_arithmetic\_two & \texttt{text-bison} & \textbf{32.0 / 16.5 / 19.6} & 12.0 / 18.0 / 16.8 & 18.0 / 17.5 / 17.6 & 16.0 / 18.5 / 18.0 \\
navigate & \texttt{text-bison} & \textbf{72.0 / 61.0 / 63.2} & 56.0 / 55.0 / 55.2 & 60.0 / 56.5 / 57.2 & 56.0 / 57.0 / 56.8 \\
object\_counting & \texttt{text-bison} & \textbf{72.0 / 62.0 / 64.0} & 58.0 / 57.0 / 57.2 & 62.0 / 55.5 / 56.8 & 50.0 / 57.0 / 55.6 \\
penguins\_in\_a\_table & \texttt{text-bison} & \textbf{72.4 / 56.4 / 59.6} & 58.6 / 53.0 / 54.1 & 55.2 / 55.6 / 55.5 & 58.6 / 53.0 / 54.1 \\
reasoning\_about\_colored\_objects & \texttt{text-bison} & \textbf{82.0 / 77.0 / 78.0} & 76.0 / 72.5 / 73.2 & 78.0 / 73.0 / 74.0 & 74.0 / 69.5 / 70.4 \\
ruin\_names & \texttt{text-bison} & \textbf{88.0 / 82.5 / 83.6} & 66.0 / 65.5 / 65.6 & 66.0 / 62.5 / 63.2 & 64.0 / 66.0 / 65.6 \\
salient\_translation \_error\_detection & \texttt{text-bison} & \textbf{46.0 / 50.5 / 49.6} & 42.0 / 47.5 / 46.4 & 42.0 / 49.5 / 48.0 & 44.0 / 50.0 / 48.8 \\
snarks & \texttt{text-bison} & \textbf{80.0 / 81.8 / 81.5} & 68.6 / 77.6 / 75.8 & 71.4 / 76.2 / 75.3 & 77.1 / 84.6 / 73.1 \\
sports\_understanding & \texttt{text-bison} & \textbf{94.0 / 82.5 / 84.8} & 86.0 / 79.0 / 80.4 & 90.0 / 81.0 / 82.8 & 38.0 / 44.5 / 43.2 \\
temporal\_sequences & \texttt{text-bison} & \textbf{78.0 / 81.0 / 80.4} & 36.0 / 43.5 / 42.0 & 32.0 / 45.0 / 42.4 & 36.0 / 43.0 / 41.6 \\
tracking\_shuffled\_objects\_seven\_objects & \texttt{text-bison} & \textbf{32.0 / 15.5 / 18.8} & 10.0 / 17.0 / 15.6 & 10.0 / 18.0 / 16.4 & 12.0 / 15.5 / 14.8 \\
web\_of\_lies & \texttt{text-bison} & \textbf{62.0 / 50.0 / 52.4} & 48.0 / 45.5 / 46.0 & 48.0 / 44.0 / 44.8 & 52.0 / 51.5 / 51.2 \\
word\_sorting & \texttt{text-bison} & \textbf{24.0 / 17.5 / 18.8} & 10.0 / 12.0 / 11.6 & 4.0 / 8.0 / 7.2 & 4.0 / 7.5 / 6.8 \\
\bottomrule
\end{tabular}
}
\end{center}
\label{table:palm2_scores_on_bbh_tasks}
\end{table}
```

## Table 8
```latex
\begin{table}[H]
\scriptsize
\caption{BBH task-wise instructions found by prompt optimization with the \texttt{PaLM 2-L} scorer and the \texttt{PaLM 2-L-IT} optimizer.
The optimization starts from the empty string.
}
\centering
\scalebox{0.99}{
\begin{tabular}{P{2.3cm}P{11.6cm}}
\toprule
Task & Our Instruction \\
\midrule
boolean\_expressions & A Boolean expression is a well-formed expression consisting of variables, values, and logical operators. The expression must evaluate to a single True or False value. The order of precedence of the logical operators is as follows: NOT, AND, OR, XOR, IMP. Parentheses can be used to group subexpressions and to control the order of evaluation.\\ [2ex]
causal\_judgement & When considering questions about causation, a typical person would consider the following factors: whether the action or event was a necessary condition for the outcome to occur, a sufficient condition, a proximate cause, or a foreseeable cause. \\ [2ex]
date\_understanding & To find the date X time ago from today, first find today's date. Then subtract X time from today's date. If the current date is the last day of a month, then the date a month ago is the last day of the previous month. If the current date is not the last day of a month, then the date a month ago is the same day of the previous month. For example, if today is March 31, 2023, then the date a month ago is February 28, 2023. If today is April 1, 2023, then the date a month ago is March 1, 2023.\\ [2ex]
disambiguation\_qa & Identifying Antecedents of Pronouns: A Comprehensive Guide \\ [2ex]
dyck\_languages & First, look for the opening parentheses. Then, count the number of opening parentheses. Finally, close the parentheses in the reverse order that they were opened.\\ [2ex]
formal\_fallacies & A deductive argument is one where the conclusion follows necessarily from the premises. If the premises are true, then the conclusion must also be true. An invalid argument is one where it is possible for the premises to be true and the conclusion to be false.\\ [2ex]
geometric\_shapes & A closed polygonal chain is a series of connected line segments. The line segments can be straight or curved. The first and last line segments are connected. The line segments do not intersect each other except at their endpoints. A closed polygon can be described by an SVG path element, which starts at a given point, goes to one or more additional points, and then ends at the starting point. The path element can consist of straight line segments, curved segments, or a mixture of both.\\ [2ex]
hyperbaton & The correct adjective order in English is opinion, size, shape, age, color, origin, material, and purpose. If you have more than one adjective of the same type, they are usually placed in order of importance. For example, you would say "a large, old, Pakistani ship" rather than "an old, large, Pakistani ship." There are a few exceptions to these rules, but they are generally followed in most cases.\\ [2ex]
logical\_deduction \_seven\_objects & The following questions will test your ability to use deductive reasoning. You will be given a set of statements about a group of objects. You will then be asked to answer questions about the objects based on the statements. The statements in the questions are logically consistent, so you can use them to deduce the order of the objects. For each question, you must choose the option that is logically consistent with the information in the questions.\\ [2ex]
movie\_recommendation & Based on your input, I have analyzed the given movies in terms of genre, plot, tone, audience rating, year of release, director, cast, and reviews. I have also taken into account the given options. The movie that is most similar to the given movies in terms of all these factors is:\\ [2ex]
multistep\_arithmetic \_two & The order of operations in mathematics is PEMDAS, which stands for Parentheses, Exponents, Multiplication, Division, Addition, and Subtraction. When there are multiple operations of the same precedence, they must be performed from left to right. Note that multiplication and division have the same precedence, as do addition and subtraction.\\ [2ex]
navigate & You will return to the starting point if and only if (1) the total number of steps you take forward is equal to the total number of steps you take back, and (2) the total number of turns you make is a multiple of 180 degrees.\\ [2ex]
object\_counting & Here is a list of the objects you mentioned and their corresponding counts:\\ [2ex]
penguins\_in\_a\_table & Here is my new text:\\ [2ex]
reasoning\_about \_colored\_objects & Starting from the leftmost object in the row, I observe the following objects arranged in this order:\\ [4ex]
ruin\_names & Which is the funniest pun on the artist or movie name?\\ [2ex]
salient\_translation \_error\_detection & Instructions: Read the German sentence and its English translation carefully, then identify the type of error in the translation and select the correct option. There are six possible types of errors: Named Entities, Numerical Values, Modifiers or Adjectives, Negation or Antonyms, Facts, and Dropped Content.\\ [2ex]
snarks & Identify the sarcastic statement by considering the following factors: incongruity, exaggeration, understatement, context, speaker's intent, and audience's reaction. I will also consider the speaker's tone of voice, facial expressions, and body language.\\ [2ex]
sports\_understanding & I will determine if a sentence about an athlete is plausible by first checking if it is grammatically correct. If it is, I will then check if it is consistent with the athlete's sport, position, and real-world statistics. I will also check if it is consistent with the rules of the athlete's sport. If the sentence is consistent with all of these things, I will answer "yes", otherwise I will answer "no".\\ [2ex]
temporal\_sequences & The answer is the time that is not mentioned in the given statements. \\ [2ex]
tracking\_shuffled\_objects \_seven\_objects & Claire has the blue ball, Gertrude has the black ball, and Dave has the green ball. They are all happy with their new balls. \\ [2ex]
web\_of\_lies & The answer to a question is yes if there are an odd number of liars before the current speaker, and no if there are an even number of liars before the current speaker. If the current speaker is a truth-teller, they will say the opposite of what the previous person said, while a liar will say the same thing as the previous person said. \\ [2ex]
word\_sorting & Alphabetical order of given words: \\
\bottomrule
\end{tabular}
}
\label{table:found_instructions_on_bbh_tasks_palm_2_l}
\end{table}
```

## Table 9
```latex
\begin{table}[H]
\scriptsize
\caption{BBH task-wise instructions found by prompt optimization with the \texttt{text-bison} scorer and the \texttt{PaLM 2-L-IT} optimizer.
The optimization starts from the empty string.
}
\begin{center}
\begin{tabular}{P{2.3cm}P{11.6cm}}
\toprule
Task& Our Instruction \\
\midrule
boolean\_expressions & Not (not False) and not not False is False \\ [2ex]
causal\_judgement & A typical person would likely answer the questions about causation as follows: \\ [2ex]
date\_understanding & Today is February 28, 2023. It is a Tuesday. Yesterday was Monday, February 27, 2023. Tomorrow will be Wednesday, March 1, 2023. A week ago, it was February 21, 2023, and a month ago, it was January 28, 2023. A year from now, it will be February 28, 2024. The day of the week is important to note because it will help us to correctly answer the questions below. Not all years are leap years that contain February 29. \\ [2ex]
disambiguation\_qa & A pronoun is a word that stands in for a noun. The noun that a pronoun refers to is called its antecedent. To identify the antecedent of a pronoun, look for the noun that the pronoun could be referring to. If there is only one possible noun, then that is the antecedent. If there are two or more possible nouns, then the antecedent is ambiguous. Use the context of the sentence to help you determine the correct antecedent. \\ [2ex]
dyck\_languages & \{ \} \\ [2ex]
formal\_fallacies & How to Evaluate Deductive Validity of an Argument \\ [2ex]
geometric\_shapes & What shape is this SVG code drawing, and how many sides does it have? \\ [2ex]
hyperbaton & In English, adjectives are typically placed before nouns in a specific order. The order is: opinion, size, shape, age, color, origin, material, purpose, noun. For example, the sentence "the big, old, red barn" would be considered grammatically correct, while the sentence "the old, big, red barn" would not. Adjectives that come before nouns are called attributive adjectives, while adjectives that come after nouns are called predicative adjectives. \\ [2ex]
logical\_deduction \_seven\_objects & In this logical reasoning task, you will be given a series of paragraphs, each of which describes a set of objects arranged in a fixed order. The statements in each paragraph are logically consistent. You must read each paragraph carefully and use the information given to determine the logical relationships between the objects. You will then be asked a question about the order of the objects. Read each question carefully and choose the option that answers the question correctly. \\ [2ex]
movie\_recommendation & What is the highest-rated movie similar to the given movies, with a similar IMDb rating and released in the same year? \\ [2ex]
multistep\_arithmetic\_two & Let's solve these equations using PEMDAS order of operations. Remember that PEMDAS stands for parentheses, exponents, multiplication and division, and addition and subtraction. \\ [2ex]
navigate & Starting at the origin, facing north, follow the instructions. If your displacement from the origin is zero and your direction is unchanged, then your answer is Yes. Otherwise, your answer is No. \\ [2ex]
object\_counting & Let me help you count the items you have. Just list them one by one, separated by commas. I will then count each item and tell you how many items there are in total. \\ [2ex]
penguins\_in\_a\_table & This table shows information about penguins. The columns show the penguin’s name, age, height (in cm), and weight (in kg). The penguins are listed in order of their age, from youngest to oldest. \\ [2ex]
reasoning\_about \_colored\_objects & First, read the input carefully. Then, identify all the objects mentioned, their colors, and their positions. Next, visualize the objects and their positions in your mind. Finally, answer the questions accurately based on the information given. Make sure to pay attention to the order of the objects. \\ [2ex]
ruin\_names & A humorous edit of an artist or movie name can be created by replacing one or more letters to form a new word or phrase that sounds similar but has a different meaning. The new word or phrase should be relevant to the original word, but it should also be a surprise, which makes the edit funny. For example, the artist or movie name "Rocky" can be changed to "Ricky," and "Schindler's List" can be changed to "Schindler's Lift." Be creative and have fun! \\ [2ex]
salient\_translation \_error\_detection & The following translations from German to English contain a particular error. The error may be one of the following types: Named Entities, Numerical Values, Modifiers or Adjectives, Negation or Antonyms, Facts, or Dropped Content. Please identify the error. \\ [2ex]
snarks & The statement \\ [2ex]
sports\_understanding & To determine the plausibility of a sports sentence, I will first identify the sport, athletes, teams, and events mentioned in the sentence. Then, I will use my knowledge of the rules of the sport, the context of the sentence, common sense, and my knowledge of the world to determine whether the sentence is plausible. I will also consider the time period and location, as well as any other relevant information. Finally, I will return a score of 1 for plausible sentences and 0 for implausible ones. \\ [2ex]
temporal\_sequences & To determine the time period when a person went to a place, first identify all the time periods when the person's whereabouts are unknown. Then, rule out any time periods during which the person was seen doing something else or the place was closed. The remaining time periods are the possible times when the person could have gone to the place. \\ [2ex]
tracking\_shuffled\_objects \_seven\_objects & At the start of the game, Claire has a blue ball. Throughout the game, pairs of people swap balls. Claire ends up with the yellow ball. \\ [2ex]
web\_of\_lies & People in a group either tell the truth or lie. The truthfulness of a person's statement is determined by the statement of the previous person. If the previous person told the truth, then the current person who says the opposite is lying. If the previous person lied, then the current person who says the opposite is telling the truth. This rule applies to all subsequent statements. \\ [2ex]
word\_sorting & Sort the following words alphabetically, ignoring case and punctuation. Print the sorted list. \\
\bottomrule
\end{tabular}
\end{center}
\label{table:found_instructions_on_bbh_tasks_text_bison}
\end{table}
```

## Table 10
```latex
\begin{table}[H]
\scriptsize
\caption{Accuracies on BBH tasks with the \texttt{gpt-3.5-turbo} optimizer that starts from the empty string.
The \texttt{PaLM 2-L} scores are from A\_begin (left) instructions; the \texttt{text-bison} scores include Q\_begin (left) and Q\_end (right) instructions.
}
\begin{center}
\begin{tabular}{cP{1.2cm}P{2.2cm}P{2.2cm}}
\toprule
\multirow{2}{*}{Task} & \multirow{2}{*}{Scorer} & Our Acc (\texttt{begin}) & Our Acc (\texttt{end})\\ \cmidrule(lr){3-3} \cmidrule(lr){4-4}
& & training / test / overall & training / test / overall \\
\midrule
boolean\_expressions & \texttt{PaLM 2-L} & 92.0 / 86.5 / 87.6 & N/A \\
causal\_judgement & \texttt{PaLM 2-L} & 81.1 / 58.7 / 63.1 & N/A \\
date\_understanding & \texttt{PaLM 2-L} & 86.0 / 82.0 / 82.8 & N/A \\
disambiguation\_qa & \texttt{PaLM 2-L} & 80.0 / 74.0 / 75.2 & N/A \\
dyck\_languages & \texttt{PaLM 2-L} & 100.0 / 100.0 / 100.0 & N/A \\
formal\_fallacies & \texttt{PaLM 2-L} & 88.0 / 63.5 / 68.4 & N/A \\
geometric\_shapes & \texttt{PaLM 2-L} & 60.0 / 41.0 / 44.8 & N/A \\
hyperbaton & \texttt{PaLM 2-L} & 88.0 / 93.0 / 92.0 & N/A \\
logical\_deduction\_seven\_objects & \texttt{PaLM 2-L} & 76.0 / 56.5 / 60.4 & N/A \\
movie\_recommendation & \texttt{PaLM 2-L} & 84.0 / 86.0 / 85.6 & N/A \\
multistep\_arithmetic\_two & \texttt{PaLM 2-L} & 52.0 / 49.0 / 49.6 & N/A \\
navigate & \texttt{PaLM 2-L} & 76.0 / 67.0 / 68.8 & N/A \\
object\_counting & \texttt{PaLM 2-L} & 78.0 / 79.0 / 78.8 & N/A \\
penguins\_in\_a\_table & \texttt{PaLM 2-L} & 82.8 / 72.6 / 74.7 & N/A \\
reasoning\_about \_colored\_objects & \texttt{PaLM 2-L} & 86.0 / 67.5 / 71.2 & N/A \\
ruin\_names & \texttt{PaLM 2-L} & 90.0 / 83.0 / 84.4 & N/A \\
salient\_translation\_error\_detection & \texttt{PaLM 2-L} & 62.0 / 65.0 / 64.4 & N/A \\
snarks & \texttt{PaLM 2-L} & 85.7 / 70.6 / 73.6 & N/A \\
sports\_understanding & \texttt{PaLM 2-L} & 68.0 / 57.5 / 59.6 & N/A \\
temporal\_sequences & \texttt{PaLM 2-L} & 100.0 / 99.5 / 99.6 & N/A \\
tracking\_shuffled\_objects\_seven\_objects & \texttt{PaLM 2-L} & 44.0 / 34.5 / 36.4 & N/A \\
web\_of\_lies & \texttt{PaLM 2-L} & 92.0 / 91.0 / 91.2 & N/A \\
word\_sorting & \texttt{PaLM 2-L} & 62.0 / 52.0 / 54.0 & N/A \\
\hdashline\noalign{\vskip 0.5ex}
boolean\_expressions & \texttt{text-bison} & 84.0 / 78.5 / 79.6 & 80.0 / 78.0 / 78.4\\
causal\_judgement & \texttt{text-bison} & 78.4 / 57.3 / 61.5 & 83.8 / 53.3 / 59.4\\
date\_understanding & \texttt{text-bison} & 52.0 / 45.0 / 46.4 & 64.0 / 52.4 / 54.8\\
disambiguation\_qa & \texttt{text-bison} & 68.0 / 75.5 / 74.0 & 64.0 / 71.5 / 70.0\\
dyck\_languages & \texttt{text-bison} & 100.0 / 99.5 / 99.6 & 100.0 / 100.0 / 100.0\\
formal\_fallacies & \texttt{text-bison} & 70.0 / 54.5 / 57.6 & 74.0 / 53.5 / 57.6\\
geometric\_shapes & \texttt{text-bison} & 28.0 / 15.0 / 17.6 & 48.0 / 28.0 / 32.0\\
hyperbaton & \texttt{text-bison} & 86.0 / 85.0 / 85.2 & 80.0 / 76.5 / 77.2 \\
logical\_deduction\_seven\_objects & \texttt{text-bison} & 66.0 / 57.5 / 59.2 & 62.0 / 55.0 / 56.4\\
movie\_recommendation & \texttt{text-bison} & 76.0 / 69.5 / 70.8 & 82.0 / 70.5 / 72.8\\
multistep\_arithmetic\_two & \texttt{text-bison} & 28.0 / 20.5 / 22.0 & 28.0 / 22.5 / 23.6\\
navigate & \texttt{text-bison} & 72.0 / 61.0 / 63.2 & 68.0 / 59.5 / 61.2\\
object\_counting & \texttt{text-bison} & 68.0 / 71.0 / 70.4 & 72.0 / 69.0 / 69.6 \\
penguins\_in\_a\_table & \texttt{text-bison} & 65.5 / 59.8 / 61.0 & 79.3 / 53.0 / 58.2 \\
reasoning\_about\_colored\_objects & \texttt{text-bison} & 84.0 / 76.5 / 78.0 & 86.0 / 74.0 / 76.4\\
ruin\_names & \texttt{text-bison} & 80.0 / 74.0 / 75.2 & 74.0 / 75.0 / 74.8\\
salient\_translation\_error\_detection & \texttt{text-bison} & 44.0 / 50.5 / 49.2 & 48.0 / 51.0 / 50.4\\
snarks & \texttt{text-bison} & 82.9 / 79.7 / 80.3 & 88.6 / 84.6 / 85.4 \\
sports\_understanding & \texttt{text-bison} & 84.0 / 76.5 / 78.0 & 90.0 / 80.0 / 82.0 \\
temporal\_sequences & \texttt{text-bison} & 50.0 / 54.5 / 53.6 & 64.0 / 61.5 / 62.0\\
tracking\_shuffled\_objects\_seven\_objects & \texttt{text-bison} & 22.0 / 18.5 / 19.2 & 30.0 / 21.5 / 23.2 \\
web\_of\_lies & \texttt{text-bison} & 64.0 / 57.5 / 58.8 & 68.0 / 55.0 / 57.6\\
word\_sorting & \texttt{text-bison} & 26.0 / 19.0 / 20.4 & 32.0 / 25.5 / 26.8 \\
\bottomrule
\end{tabular}
\end{center}
\label{table:gpt_scores_on_bbh_tasks_starting_from_empty}
\end{table}
```

## Table 11
```latex
\begin{table}[H]
\scriptsize
\caption{BBH task-wise instructions found by prompt optimization with the \texttt{PaLM 2-L} scorer and the \texttt{gpt-3.5-turbo} optimizer.
The optimizations start from the empty string.
}
\centering
\begin{tabular}{P{2.3cm}P{11.6cm}}
\toprule
Task & Our Instruction \\
\midrule
boolean\_expressions & An accurate evaluation of logical expressions involves correctly applying Boolean operators, considering the order of operations, and analyzing the truth values of the operands in accordance with Boolean logic principles. \\ [2ex]
causal\_judgement & Understanding causality is critical for accurately assessing cause and effect relationships in various scenarios, leading to well-informed judgments, precise conclusions, and definitive answers to questions about the outcomes involved. \\ [2ex]
date\_understanding & What is the specific date mentioned or required in each given problem or question, taking into account all relevant information, available options, and the provided context? Please provide the accurate answer in the format MM/DD/YYYY. \\ [2ex]
disambiguation\_qa & Accurately analyze and clarify the pronoun-antecedent relationship in the given sentences, identifying the appropriate referent to eliminate any potential confusion or ambiguity and ensure a precise understanding of the intended meaning. \\ [2ex]
dyck\_languages & Solve the sequence by properly closing the parentheses. \\ [2ex]
formal\_fallacies & In determining the deductive validity of arguments based on explicit premises, a meticulous analysis of the logical relationships and implications is essential for definitively establishing their soundness, confirming their validity or invalidity, and ensuring a reliable and robust assessment of the arguments at hand. \\ [2ex]
geometric\_shapes & The SVG path element with the "d" attribute plays a crucial role in web development, allowing for the precise definition and rendering of various shapes on a webpage. \\ [2ex]
hyperbaton & Understanding the correct order of adjectives is crucial for constructing grammatically accurate and coherent sentences that effectively convey the intended meaning in diverse contexts while ensuring clarity, cohesion, and consistency throughout consistently and effortlessly. \\ [2ex]
logical\_deduction \_seven\_objects & By conducting a meticulous analysis of the given information and ensuring logical consistency within each paragraph, we can accurately determine the precise order or ranking of the mentioned objects, allowing us to confidently and consistently identify the correct answer in every presented scenario with utmost precision and confidence. \\ [2ex]
movie\_recommendation & Which movie option from the given choices closely matches the mentioned films in terms of themes, storylines, and characteristics, guaranteeing the highest possible similarity score among them all? \\ [2ex]
multistep\_arithmetic\_two & Evaluate the given mathematical expressions step by step to determine the correct solutions accurately. \\ [2ex]
navigate & Is it possible to determine, with absolute certainty, whether strictly adhering to the given instructions will unfailingly bring you back to the original starting point without any exceptions, errors, or deviations? \\ [2ex]
object\_counting & Determine the total number of objects or entities mentioned in the given list, covering various categories and types, to accurately calculate the overall count. \\ [2ex]
penguins\_in\_a\_table & From the given table, what information can we gather about the mentioned animals and their respective attributes, including names, ages, heights, and weights? \\ [2ex]
reasoning\_about \_colored\_objects & By thoroughly examining the given information, accurately determine the answers for each question by considering the specific characteristics, colors, and positions of the mentioned objects. \\ [2ex]
ruin\_names & Select the most amusing and clever alteration from the options provided for the given artist, movie, or title name, and accurately choose the correct answer to test your wit and creativity. \\ [2ex]
salient\_translation \_error\_detection & Thoroughly examine the given translations from German to English and accurately identify any errors by carefully analyzing the text and selecting the appropriate option with meticulous attention to detail, precision, utmost accuracy, and comprehensive understanding of the language for precise evaluation and categorization. \\ [2ex]
snarks & Which option delivers the most devastatingly sarcastic response, brilliantly exposing the sheer absurdity and leaving absolutely no doubt whatsoever in all the given situations? \\ [2ex]
sports\_understanding & Maintaining the accuracy, reliability, and integrity of sports event representation is essential for upholding the highest standards of credibility, trustworthiness, and overall quality in conveying information, without any compromise, misrepresentation, or distortion, thereby ensuring the factual accuracy of sports journalism. \\ [2ex]
temporal\_sequences & Based on the provided timeline and observed activities, we can accurately determine the possible time range when each individual could have visited their intended destinations and answer questions about their visitation time. \\ [2ex]
tracking\_shuffled\_objects \_seven\_objects & An important point to note is that each person in the group starts with one specific book at the beginning of the semester. \\ [2ex]
web\_of\_lies & Analyzing the consistency and accuracy of statements provided by each person is crucial for determining the truthfulness of individuals in every scenario. \\ [2ex]
word\_sorting & Please sort the given words in alphabetical order: The list of words to be sorted contains - \\ [2ex]

\bottomrule
\end{tabular}
\label{table:found_instructions_on_bbh_tasks_s_palm_2_l_o_gpt_3.5_turbo_from_empty}
\end{table}
```

## Table 12
```latex
\begin{table}[H]
\scriptsize
\caption{BBH task-wise Q\_begin instructions found by prompt optimization with the \texttt{text-bison} scorer and the \texttt{gpt-3.5-turbo} optimizer.
The optimizations start from the empty string.
}
\begin{center}
\begin{tabular}{P{2.3cm}P{11.6cm}}
\toprule
Task & Our Instruction \\
\midrule
boolean\_expressions & Group sub-expressions with parentheses to accurately evaluate logical operations: not, and, and finally or. Determine the resulting value as either True or False. \\ [2ex]
causal\_judgement & Consider the intentions and actions of the individuals involved. \\ [2ex]
date\_understanding & Determine the one-day difference in the given date and express it in the format MM/DD/YYYY. \\ [2ex]
disambiguation\_qa & Determine the precise antecedent of the pronoun in the given sentence and select the correct option or state if it is ambiguous. \\ [2ex]
dyck\_languages & Ensure that all opening brackets have a corresponding closing bracket, and that the closing brackets are in the correct order. \\ [2ex]
formal\_fallacies & Thoroughly analyze the explicitly provided premises and determine the deductive validity of the argument based on all necessary conditions, implications, exclusions, and dependencies given. \\ [2ex]
geometric\_shapes & Analyze the given SVG path element carefully and confidently select the correct option from the provided choices to accurately determine the corresponding shape. Pay close attention to the specific path details and confidently make the most suitable choice. \\ [2ex]
hyperbaton & Select the sentence that strictly adheres to the standard order of adjectives: opinion, size, age, shape, color, origin, material, and purpose. Ensure there are no deviations or alterations in the adjective order. Choose the option without any changes. \\ [2ex]
logical\_deduction \_seven\_objects & Analyze the given information to accurately determine the precise order and ranking of the mentioned objects/people, considering their relationships, positions, and any provided comparisons, for a definitive and logical progression with maximum accuracy and efficiency. \\ [2ex]
movie\_recommendation & Based on the movie list provided, carefully consider your preferences and make a well-informed decision. \\ [2ex]
multistep\_arithmetic\_two & First, simplify any expressions within parentheses following the correct order of operations to accurately evaluate the final answer with efficiency and precision. \\ [2ex]
navigate & Always face forward. Take 10 steps forward. Turn left. Take 5 steps forward. Take 3 steps backward. Finally, take 7 steps forward. Turn around and take 1 step forward. Repeat the previous sequence three times. Follow the given path precisely without any deviations. At the end, turn right and take 11 steps forward. If you follow these instructions, will you return to the starting point?
Options:
- Yes
- No \\ [2ex]
object\_counting & Determine the total count of mentioned vegetables accurately and state the final count as the answer. \\ [2ex]
penguins\_in\_a\_table & Analyze the given table to accurately determine the required information based on the provided criteria and attributes of the penguins and giraffes. Utilize efficient problem-solving strategies to arrive at the correct answer. \\ [2ex]
reasoning\_about \_colored\_objects & State the color of the object mentioned in the given arrangement with utmost accuracy. \\ [2ex]
ruin\_names & Choose the option that offers the most clever and humorous alteration of the given artist or movie name. Let your creativity shine and select the answer that will undoubtedly bring a smile to your face! Make sure to think outside the box! \\ [2ex]
salient\_translation \_error\_detection & Analyze the translation and accurately identify the specific error type based on the source text, providing the most appropriate corresponding option. \\ [2ex]
snarks & Choose the option that wickedly embodies sarcasm. \\ [2ex]
sports\_understanding & Determine the plausibility of the given statement by evaluating factual accuracy, logical consistency, and contextual relevance, then provide a succinct and well-justified response. \\ [2ex]
temporal\_sequences & Identify the optimal time slot for the individual to engage in the mentioned location/activity considering the given sightings and waking up time, taking into account the opening and closing times of the location and the duration of each event. \\ [2ex]
tracking\_shuffled\_objects \_seven\_objects & Pay attention to the given information and track the swaps/exchanges carefully to accurately determine the final possession/position/outcome for the specified individual. \\ [2ex]
web\_of\_lies & To determine the truthfulness of the last person mentioned, analyze the consistency of each statement and count the number of individuals accusing the previous person of lying. If the count of accusers is even, that person tells the truth; if it is odd, that person lies. \\ [2ex]
word\_sorting & Alphabetically sort the given list of words, ensuring all words are included and in ascending order. \\ [2ex]

\bottomrule
\end{tabular}
\end{center}
\label{table:found_instructions_on_bbh_tasks_s_text_bison_o_gpt_3.5_turbo_from_empty}
\end{table}
```

## Table 13
```latex
\begin{table}[H]
\scriptsize
\caption{BBH task-wise Q\_end instructions found by prompt optimization with the \texttt{text-bison} scorer and the \texttt{gpt-3.5-turbo} optimizer.
The optimizations start from the empty string.
}
\begin{center}
\begin{tabular}{P{2.3cm}P{11.6cm}}
\toprule
Task & Our Instruction \\
\midrule
boolean\_expressions & Accurately use order of operations and parentheses to evaluate logical expressions and determine truth values efficiently. \\ [2ex]
causal\_judgement & Consider all relevant factors, prioritize overall well-being and ethical considerations, make well-informed decisions while foreseeing potential consequences efficiently, and consistently strive for optimal outcomes with empathy and adaptability in a thoughtful and comprehensive manner. \\ [2ex]
date\_understanding & Subtract the specified number of days from the given date and format the outcome as MM/DD/YYYY to accurately determine the desired result in an efficient manner. \\ [2ex]
disambiguation\_qa & Clearly identify and select the unambiguous antecedent for the pronoun or designate it as "Ambiguous" if it is unclear. \\ [2ex]
dyck\_languages & Add the missing closing parentheses. \\ [2ex]
formal\_fallacies & Determine the deductive validity of the argument presented based on the explicitly stated premises and reach a definitive conclusion. \\ [2ex]
geometric\_shapes & Analyzing the given SVG path element, accurately determine its shape by closely examining its curves and coordinates, then select the correct option. \\ [2ex]
hyperbaton & Choose the option with the correct adjective order in each sentence, prioritizing specific attributes like size, color, and origin. Place the most specific adjective before the more general ones for precise and standardized ordering across all examples. Ensure accurate alignment of the adjectives based on their respective attributes for consistent and standardized ordering. \\ [2ex]
logical\_deduction \_seven\_objects & Determine the precise order of the given objects/participants based on the provided information and establish the final ranking accurately, considering all relevant factors, while maintaining logical consistency with maximum efficiency. \\ [2ex]
movie\_recommendation & Choose the most similar option from the choices provided that closely aligns with the given movies' themes, genres, and impact for the most accurate recommendation possible. Make your selection wisely. \\ [2ex]
multistep\_arithmetic\_two & Carefully follow the order of operations to precisely simplify the expressions within parentheses and efficiently find the accurate final answer. \\ [2ex]
navigate & Always face forward. Take 10 steps forward. Turn right and walk for 5 steps. Then, make a left turn and continue for 9 steps. Proceed by walking 6 steps backward. Finally, turn around and take 200 steps. Accurately track your movements, diligently adhere to the given path, and ensure to return to the starting point without any deviations or obstacles. \\ [2ex]
object\_counting & Determine the total count of items mentioned, including all listed items, using an efficient and concise method. State the final count as your answer. \\ [2ex]
penguins\_in\_a\_table & Identify the animal with the maximum measurement (weight, age, or height) in the table and state its name and species. \\ [2ex]
reasoning\_about \_colored\_objects & Determine the color of each item in the given scenario and select the correct color option from the provided choices for accurate responses, ensuring utmost precision and completeness. \\ [2ex]
ruin\_names & Choose the option that creatively and hilariously transforms the given artist or movie name. \\ [2ex]
salient\_translation \_error\_detection & Carefully analyze the translations and select the most suitable option from the given choices to rectify the specific error category, ensuring complete precision, accuracy, and faithful representation of the intended meaning, while considering all relevant information in the source text. \\ [2ex]
snarks & Choose the option that cleverly employs sarcasm to defy all expectations and leave everyone utterly dumbfounded, questioning the very essence of their own perception. \\ [2ex]
sports\_understanding & Evaluate the plausibility of each given statement and provide a well-supported justification based on logical reasoning, contextual understanding, and relevant evidence to arrive at a definitive and conclusive answer. \\ [2ex]
temporal\_sequences & Identify the possible time slot for the desired activity based on the given information and sightings, then select the correct option. \\ [2ex]
tracking\_shuffled\_objects \_seven\_objects & Thoroughly analyze the given scenarios, systematically consider all available information, and confidently determine the final outcome with exceptional precision and optimal efficiency, while maintaining a strategic and logical approach throughout the process. \\ [2ex]
web\_of\_lies & Examine each person's statements meticulously to accurately determine the truth and confidently identify who is telling the truth, enabling you to effectively solve the given problem. \\ [2ex]
word\_sorting & Sort the given words alphabetically using spaces as separators while maintaining their original order and including all words. \\ [2ex]

\bottomrule
\end{tabular}
\end{center}
\label{table:found_instructions_on_bbh_tasks_s_text_bison_o_gpt_3.5_turbo_from_empty_q_end}
\end{table}
```

## Table 14
```latex
\begin{table}[H]
\scriptsize
\caption{Accuracies on BBH tasks with the \texttt{PaLM 2-L} scorer and the \texttt{gpt-3.5-turbo} optimizer that starts from ``Let's solve the problem''.
The scores are from A\_begin instructions.
}
\begin{center}
\begin{tabular}{cP{1.2cm}P{2.2cm}P{2.2cm}}
\toprule
\multirow{2}{*}{Task} & \multirow{2}{*}{Scorer} & Our Acc & ``Let's solve the problem.'' Acc \\ \cmidrule{3-4}
& & training / test / overall & training / test / overall \\
\midrule
boolean\_expressions & \texttt{PaLM 2-L} & 98.0 / 89.5 / 91.2 & 78.0 / 69.0 / 70.8 \\
causal\_judgement & \texttt{PaLM 2-L} & 83.8 / 58.7 / 63.6 & 62.0 / 61.3 / 61.5 \\
date\_understanding & \texttt{PaLM 2-L} & 90.0 / 82.0 / 83.6 & 74.0 / 71.0 / 71.6 \\
disambiguation\_qa & \texttt{PaLM 2-L} & 78.0 / 68.0 / 70.0 & 52.0 / 54.5 / 54.0 \\
dyck\_languages & \texttt{PaLM 2-L} & 100.0 / 100.0 / 100.0 & 94.0 / 97.0 / 96.4 \\
formal\_fallacies & \texttt{PaLM 2-L} & 84.0 / 62.0 / 66.4 & 68.0 / 54.0 / 56.8 \\
geometric\_shapes & \texttt{PaLM 2-L} & 62.0 / 42.5 / 46.4 & 30.0 / 22.0 / 23.6 \\
hyperbaton & \texttt{PaLM 2-L} & 94.0 / 91.5 / 92.0 & 72.0 / 77.0 / 76.0 \\
logical\_deduction\_seven\_objects & \texttt{PaLM 2-L} & 66.0 / 53.0 / 55.6 & 38.0 / 36.5 / 36.8 \\
movie\_recommendation & \texttt{PaLM 2-L} & 88.0 / 88.0 / 88.0 & 66.0 / 76.0 / 74.0 \\
multistep\_arithmetic\_two & \texttt{PaLM 2-L} & 66.0 / 55.0 / 57.2  & 30.0 / 22.0 / 23.6 \\
navigate & \texttt{PaLM 2-L} & 76.0 / 67.0 / 68.8  & 54.0 / 63.5 / 61.6 \\
object\_counting & \texttt{PaLM 2-L} & 96.0 / 92.5 / 93.2 & 58.0 / 58.0 / 58.0 \\
penguins\_in\_a\_table & \texttt{PaLM 2-L} & 86.2 / 70.9 / 74.0 & 69.0 / 72.6 / 71.9 \\
reasoning\_about \_colored\_objects & \texttt{PaLM 2-L} & 88.0 / 69.0 / 72.8 & 78.0 / 69.5 / 71.2 \\
ruin\_names & \texttt{PaLM 2-L} & 92.0 / 85.5 / 86.8 & 76.0 / 79.5 / 80.8 \\
salient\_translation\_error\_detection & \texttt{PaLM 2-L} & 66.0 / 67.5 / 67.2 & 30.0 / 35.5 / 34.4 \\
snarks & \texttt{PaLM 2-L} & 88.6 / 76.9 / 79.2 & 80.0 / 70.6 / 72.5 \\
sports\_understanding & \texttt{PaLM 2-L} & 72.0 / 63.5 / 65.2 & 60.0 / 50.5 / 52.4 \\
temporal\_sequences & \texttt{PaLM 2-L} & 100.0 / 99.5 / 99.6 & 96.0 / 92.5 / 93.2 \\
tracking\_shuffled\_objects\_seven\_objects & \texttt{PaLM 2-L} & 56.0 / 63.5 / 62.0 & 42.0 / 51.5 / 49.6 \\
web\_of\_lies & \texttt{PaLM 2-L} & 56.0 / 58.5 / 58.0 & 0.0 / 4.0 / 3.2 \\
word\_sorting & \texttt{PaLM 2-L} & 52.0 / 44.5 / 46.0 & 18.0 / 20.5 / 20.0 \\
\bottomrule
\end{tabular}
\end{center}
\label{table:gpt_scores_on_bbh_tasks_starting_from_solve_the_problem}
\end{table}
```

## Table 15
```latex
\begin{table}[H]
\scriptsize
\caption{BBH task-wise Q\_begin instructions found by prompt optimization with the \texttt{PaLM 2-L} scorer and the \texttt{gpt-3.5-turbo} optimizer.
The optimizations start from ``Let's solve the problem''.
}
\centering
\begin{tabular}{P{2.3cm}P{11.6cm}}
\toprule
Task & Our Instruction \\
\midrule
boolean\_expressions & Let's accurately assess the given conditions and determine their corresponding Boolean values. \\ [2ex]
causal\_judgement & Let's conduct a meticulous evaluation of the given scenarios, accurately determine the causal relationships, and provide definitive answers through comprehensive analysis, ensuring a precise understanding of causation and a thorough determination of events in each situation. \\ [2ex]
date\_understanding & Let's accurately determine the correct date based on the given information and select the corresponding option in the standard MM/DD/YYYY format with utmost precision and reliability, ensuring the most definitive and reliable solution possible for accurate representation in all scenarios without any room for ambiguity, error, or confusion, and providing the highest level of accuracy and reliability. \\ [2ex]
disambiguation\_qa & Let's thoroughly analyze the given sentences to accurately determine the unambiguous antecedents of the pronouns used, ensuring clear understanding, effective communication, and leaving no room for any confusion or ambiguity. \\ [2ex]
dyck\_languages & Let's find the correct closing parentheses and brackets for the given sequences. \\ [2ex]
formal\_fallacies & Let's thoroughly analyze the explicitly stated premises and draw definitive conclusions to accurately determine the deductive validity of the arguments provided in each question, employing precise and logical reasoning in our assessments for unwavering confidence in our determinations. \\ [2ex]
geometric\_shapes & Let's accurately determine the shape represented by the given SVG path element by carefully analyzing its path data and considering all available options for a precise identification. \\ [2ex]
hyperbaton & Let's quickly identify the correct adjective order. \\ [2ex]
logical\_deduction \_seven\_objects & Let's methodically analyze the given information, employ logical reasoning, thoroughly evaluate all relevant details, and accurately determine the solutions for each problem by considering all provided options comprehensively and strategically, ensuring an efficient and effective approach towards arriving at the correct answers. \\ [2ex]
movie\_recommendation & Let's uncover the perfect movie recommendation from the options provided, ensuring an exceptional cinematic experience together as we select the most captivating and satisfying choice that will keep us thoroughly engaged and immersed until the very end. \\ [2ex]
multistep\_arithmetic\_two & Let's tackle the following calculations. \\ [2ex]
navigate & Let's accurately and efficiently determine the correct solution for each given scenario, ensuring the highest level of precision, reliability, and consistency throughout. \\ [2ex]
object\_counting & Let's determine the total count of various items/objects/ingredients/animals mentioned in order to accurately and efficiently find the answer. \\ [2ex]
penguins\_in\_a\_table & Let's analyze the given information and determine the correct answer. \\ [2ex]
reasoning\_about \_colored\_objects & Let's systematically analyze the given information and carefully evaluate each answer choice to confidently determine the accurate and optimal solutions, considering all available options and specific details provided in each question for precise and concise responses, ensuring complete accuracy and clarity in our answers. \\ [2ex]
ruin\_names & Prepare to have a side-splittingly funny time as we uncover the most clever and hilarious alternatives for these artist or movie names, challenging your wit to guess the correct one with a burst of creativity, humor, and imaginative twists! \\ [2ex]
salient\_translation \_error\_detection & Let's meticulously analyze the provided translations, accurately identifying any errors or discrepancies, and conduct a comprehensive evaluation to ensure the highest level of translation quality and fidelity. By considering contextual nuances, cultural references, linguistic conventions, potential factual errors, and any dropped content, our ultimate aim is to achieve precise and thorough assessments for optimal translation accuracy and adherence to the source text. \\ [2ex]
snarks & Let's expertly determine the sarcastic statement among the given options and confidently provide the definitive answer without any room for doubt or confusion, ensuring absolute precision, clarity, and unwavering expertise in our response, while carefully analyzing the context, tone, and intention behind each statement to achieve unrivaled accuracy and unwavering confidence. \\ [2ex]
sports\_understanding & Let's find the accurate information. \\ [2ex]
temporal\_sequences & The flawless approach \\ [2ex]
tracking\_shuffled\_objects \_seven\_objects & By meticulously analyzing the given scenarios and accurately determining the final outcomes through a series of trades, swaps, and exchanges among the individuals involved, let's ascertain the conclusive results. \\ [2ex]
web\_of\_lies & Let's scrutinize each statement provided to accurately determine the truth-teller and uncover the veracity behind their words with unwavering analysis. \\ [2ex]
word\_sorting & Employing efficient and precise measures, sort the given list of words in alphabetical order to provide an optimal solution for any sorting problem, ensuring maximum performance and effectiveness. \\ [2ex]

\bottomrule
\end{tabular}
\label{table:found_instructions_on_bbh_tasks_s_palm_2_l_o_gpt_3.5_turbo_from_solve}
\end{table}
```

