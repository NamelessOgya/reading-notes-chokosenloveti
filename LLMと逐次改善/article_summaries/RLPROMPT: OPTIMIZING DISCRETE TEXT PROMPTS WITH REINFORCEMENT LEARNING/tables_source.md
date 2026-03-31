# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
\centering
\resizebox{\textwidth}{!}{
% \renewcommand{\arraystretch}{1.1}
\begin{tabular}{@{}lllllll@{}}
\toprule
\textbf{Dataset}   & \textbf{Type}                & $|C|$               & \textbf{|Train|}=\textbf{|Dev|}        & \textbf{|Test|}               & \textbf{Manual template}                                                            & \textbf{Label words}                                    \\
\toprule
SST-2     & Sentiment (Movie reviews)   & 2                    & $16 \times |C|$                   & 1.8k                 & \texttt{\textless{}S\textgreater{}} It was \texttt{[MASK]} .                       & terrible, great                                \\
\vspace{-0.2cm} \\
Yelp P.   & Sentiment (Yelp reviews)   & 2                    & $16 \times |C|$                   & 38k                  & \texttt{\textless{}S\textgreater{}} It was \texttt{[MASK]} .                       & terrible, great                                \\
\vspace{-0.2cm} \\
MR        & Sentiment (Movie reviews)   & 2                    & $16 \times |C|$                   & 2k                & \texttt{\textless{}S\textgreater{}} It was \texttt{[MASK]} .                       & terrible, great                                \\
\vspace{-0.2cm} \\
CR        & Sentiment (Product reviews)   & 2                    & $16 \times |C|$                   & 2k                   & \texttt{\textless{}S\textgreater{}} It was \texttt{[MASK]} .                       & terrible, great                                \\
\vspace{-0.2cm} \\
SST-5     & Sentiment (Movie reviews)   & 5                    & $16 \times |C|$                   & 2.2k                 & \texttt{\textless{}S\textgreater{}} It was \texttt{[MASK]} .                       & terrible, bad, okay, good, great                                \\
\vspace{-0.2cm} \\
Yelp      & Sentiment (Yelp reviews)   & 5                    & $16 \times |C|$                   & 50k                  & \texttt{\textless{}S\textgreater{}} It was \texttt{[MASK]} .                       & terrible, bad, okay, good, great                                \\
\vspace{-0.2cm} \\
Subj & Subjectivity (Movie reviews) & 2 & $16 \times |C|$                   & 2k & \texttt{\textless{}S\textgreater{}} This is \texttt{[MASK]} . & subjective, objective \\
\vspace{-0.2cm} \\
AG's News & Topic (News articles)       & 4                    & $16 \times |C|$                   & 7.6k                 & \texttt{[MASK]} News: \texttt{\textless{}S\textgreater{}}                          & World, Sports, Business, Tech                  \\
\vspace{-0.2cm} \\
%Subj & Subjectivity (Movie reviews) & 2 & $16 \times |C|$                   & 2k & \texttt{\textless{}S\textgreater{}} This is \texttt{[MASK]} . & subjective, objective \\
%\vspace{-0.2cm} \\
TREC & Topic (Question types) & 6 & $16 \times |C|$                   & 0.5k & \texttt{[MASK]}: \texttt{\textless{}S\textgreater{}} & 
\begin{tabular}[c]{@{}l@{}}Description, Entity, Expression, Human, \\ Location, Number \end{tabular} \\
% Description, Entity, Expression, Human, \\
% & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} &    & Location, Number     \\
\vspace{-0.2cm} \\
DBPedia   & Topic (Wikipedia ontologies)       & 14                   & $16 \times |C|$                   & 70k                  & \texttt{[{}Category: [MASK]]} \texttt{\textless{}S\textgreater{}}                & 
\begin{tabular}[c]{@{}l@{}}Company, Education, Artist, Sports, Office, \\ Transportation, Building, Natural, Village, \\ Animal, Plant, Album, Film, Written\end{tabular} \\
% Company, Education, Artist, Sports, Office,    \\
%          & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} &                                                                      & Transportation, Building, Natural, Village,    \\
%          & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} &                                                                      & Animal, Plant, Album, Film, Written            \\
\vspace{-0.2cm} \\
Yahoo     & Topic (Question types)       & 10                   & $16 \times |C|$                   & 60k                  & Topic \texttt{[MASK]}: \texttt{\textless{}S\textgreater{}}  &
\begin{tabular}[c]{@{}l@{}}culture, science, health, education, computer, \\ sports, business, music, family, politics\end{tabular} \\

%Subj & Subjectivity (Movie reviews) & 2 & $16 \times |C|$                   & 2k & \texttt{\textless{}S\textgreater{}} This is \texttt{[MASK]} . & subjective, objective \\
% culture, science, health, education, computer, \\
%           & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{} &                                                                      & sports, business, music, family, politics      \\


%RTE       & NLI (pair)           & 2                    & $16 \times |C|$                   & 0.3k                 & \texttt{\textless{}S1\textgreater{}? \texttt{[MASK]}, \textless{}S2\textgreater{}} & Yes, No                                        \\
%SNLI      & NLI (pair)           & 3                    & $16 \times |C|$                   & 9.8k                 & \texttt{\textless{}S1\textgreater{}? \texttt{[MASK]}, \textless{}S2\textgreater{}} & Yes, Maybe, No                                 \\
%MRPC      & paraphrase (pair)    & 2                    & $16 \times |C|$                   & 0.4k                 & \texttt{\textless{}S1\textgreater\ \texttt{[MASK]}, \textless{}S2\textgreater{}}    & Yes, No       \\
\bottomrule
\end{tabular}}
% \vspace{-7pt}
\caption{Main datasets evaluated in this work. $|C|$: $\#$ of classes for classification tasks. \texttt{\textless{}S\textgreater{}}: input sentence. All our label words have a prepended special character Ġ to represent a space before a word. Note that we follow the true few-shot learning setting \cite{perez2021trueFS} by taking the same number of validation and training, which is consistent with previous prompting works. 
}
\label{tab:nlu-dataset}
% \vspace{6pt}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
% \vspace{-5pt}
% \centering
% \begin{center}

% {\renewcommand{\arraystretch}{1.0}
% \resizebox{1.0\textwidth}{!}{
% % {\renewcommand{\arraystretch}{1.0}
% % \setlength{\tabcolsep}{1.5pt}
% \small
% \begin{tabular}{@{}lllllllll@{}}
% \toprule
%                       & \textbf{SST-2}     & \textbf{Yelp P.} & \textbf{MR}    & \textbf{CR}  & \textbf{SST-5} & \textbf{Yelp} &  \textbf{AG's News}   & \textbf{Avg.} \\ \midrule
%                     %   & (acc)              & (acc)            & (acc)          & (acc)        & (acc)               &  \\ \midrule
%  Fine-Tuning          & 80.6 \scriptnumber{3.9}         & 88.7 \scriptnumber{4.7}       & 67.4 \scriptnumber{9.7}     & 73.3 \scriptnumber{7.5} & 40.7 \scriptnumber{3.0} & \textbf{51.0} \scriptnumber{2.2}  & \textbf{84.9} \scriptnumber{3.6}          &  69.5  \\ 
%  Manual Prompt       & 82.8               & 83.0             & 80.9           & 79.6    & 34.9 & 42.1      & 76.9               &  68.6  \\
%  Instructions        & 89.0               & 84.4             & 85.2           & 80.8     & 29.8 & 43.0    & 54.8               &  58.5  \\
%  In-Context Demo.    & 85.9 \scriptnumber{0.7}         & 89.6 \scriptnumber{0.4}       & 80.6 \scriptnumber{1.4}     & 85.5 \scriptnumber{1.5} & 39.3 \scriptnumber{0.9} & 49.4 \scriptnumber{0.3}  & 74.9 \scriptnumber{0.8}   &  72.2  \\
%  Prompt Tuning \emph{(Soft Prompt Tuning)}        & 73.8 \scriptnumber{10.9}        & 88.6 \scriptnumber{2.1}       & 74.1 \scriptnumber{14.6}    & 75.9 \scriptnumber{11.8} & 40.2 \scriptnumber{6.5} & 49.1 \scriptnumber{3.1}   & 82.6 \scriptnumber{0.9}      &  69.2  \\
%  BB Tuning \emph{(2 soft tokens)}      & 83.2 \scriptnumber{3.5}         & 86.0 \scriptnumber{1.6}       & 77.1 \scriptnumber{3.9}     & 83.2 \scriptnumber{2.5} & 39.2 \scriptnumber{2.4}  &  41.5 \scriptnumber{1.9}   & 74.0 \scriptnumber{1.9}         &  69.2  \\
%  BB Tuning \emph{(5 soft tokens)}      & 84.6 \scriptnumber{4.0}         & 78.7 \scriptnumber{2.3}       & 79.8 \scriptnumber{1.5}     & 82.9 \scriptnumber{3.6} &  36.6 \scriptnumber{2.1} & 33.7 \scriptnumber{2.3}    & 73.6 \scriptnumber{3.6}         &  67.1  \\
%  BB Tuning \emph{(Mixed, 50 soft tokens)}      & 89.1 \scriptnumber{0.9}         & 93.2 \scriptnumber{0.5}       & 86.6 \scriptnumber{1.3}     & 87.4 \scriptnumber{1.0} &  38.4 \scriptnumber{1.1} & 44.8 \scriptnumber{1.3}   & 83.5 \scriptnumber{0.9}         &  74.7  \\
%  GrIPS \emph{(Discrete Prompt Enumeration)}                 & 87.1 \scriptnumber{1.5}         & 88.2 \scriptnumber{0.1}       & 86.1 \scriptnumber{0.3}     & 80.0 \scriptnumber{2.5} & 32.0 \scriptnumber{1.8} & 47.2 \scriptnumber{0.5}   & 65.4 \scriptnumber{9.8}      &  69.4  \\ 
%  AutoPrompt            & 75.0 \scriptnumber{7.6}         & 79.8 \scriptnumber{8.3}       & 62.0 \scriptnumber{0.8}     & 57.5 \scriptnumber{5.8} & 27.8 \scriptnumber{3.3} & 29.0 \scriptnumber{5.0}   & 65.7 \scriptnumber{1.9}          &  56.7  \\

 
%  \midrule
%  RLPrompt (Ours, 2 discrete tokens)            &       90.3 \scriptnumber{1.3}             &     94.1 \scriptnumber{0.8}              &  86.5 \scriptnumber{1.2}              &     87.4 \scriptnumber{1.7}         & 40.1 \scriptnumber{1.9}    & 45.6 \scriptnumber{3.8} &     76.8 \scriptnumber{1.4}  & 74.4    \\ 
%  RLPrompt (Ours, 5 discrete tokens)            &       \textbf{92.5} \scriptnumber{0.8}             &     \textbf{95.1} \scriptnumber{1.0}              &  \textbf{87.1} \scriptnumber{0.4}              &     \textbf{89.5} \scriptnumber{0.6}         & \textbf{41.4} \scriptnumber{3.2}   & 44.8 \scriptnumber{4.3} &      80.2 \scriptnumber{0.7} &   \textbf{75.8}  \\
% % Each SOTA category. 
% % No detailed explaination
 
% %                       & \textbf{SST-5} & \textbf{DBPedia} & \textbf{Yahoo} & \textbf{RTE} & \textbf{SNLI}  & \textbf{MRPC} \\
% %                       & (acc)              & (acc)            & (acc)          & (acc)        & (acc)          & \scriptnumber{F1}  \\ \midrule
% %  Manual Prompt         & 34.9               & 59.2             & 17.1           & 51.3         & 49.8           & 61.9  \\
% %  Instruction Learning  & 29.8               & 15.9             & 21.4           & 54.2         & 56.2           & 73.2  \\
% %  In-context Learning   & 39.3 \scriptnumber{0.9}         & 76.6 \scriptnumber{0.4}       & 58.7 \scriptnumber{2.1}     & 60.0 \scriptnumber{1.7}   & 58.1 \scriptnumber{0.6}     & 58.7 \scriptnumber{4.3}  \\
% %  AutoPrompt            & 27.8 \scriptnumber{3.3}         & 63.1 \scriptnumber{2.0}       & 35.5 \scriptnumber{2.0}     & 52.4 \scriptnumber{1.8}   & 36.4 \scriptnumber{3.9}     & 54.6 \scriptnumber{4.9}  \\
% %  GrIPS                 & 32.0 \scriptnumber{1.8}         & 22.1 \scriptnumber{2.9}       & 22.5 \scriptnumber{0.4}     & 54.9 \scriptnumber{0.0}   & 55.3 \scriptnumber{0.0}     & 77.0 \scriptnumber{1.1}  \\
% %  Prompt Tuning         & 21.6 \scriptnumber{2.9}         & 93.7 \scriptnumber{1.0}       & 59.8 \scriptnumber{1.9}     & 51.2 \scriptnumber{1.4}   & 33.6 \scriptnumber{0.2}     & 49.7 \scriptnumber{4.8}  \\
% %  Fine Tuning           &                    &                  &                &              &                &       \\ \midrule

% %  DTPG \scriptnumber{our}            &                    &                  &                &              &                &       \\
%  \bottomrule

%  \end{tabular}}}
% \vspace{-9pt}
% \caption{\small Results of few-shot text classification. The last column shows the average accuracy across all datasets.}
% \label{tab:cls-main}
% \vspace{-5pt}
% \end{center}
% \end{table*}
```

## Table 3
```latex
\begin{table*}[t]
\vspace{-5pt}
\centering
\begin{center}
{\renewcommand{\arraystretch}{1.0}
\resizebox{1\textwidth}{!}{
% {\renewcommand{\arraystretch}{1.0}
\setlength{\tabcolsep}{4pt}
\small
\begin{tabular}{@{}lllllllll@{}}
\toprule
% 2022.10.18
                      & \textbf{SST-2}     & \textbf{Yelp P.} & \textbf{MR}    & \textbf{CR}  & \textbf{SST-5} & \textbf{Yelp} &  \textbf{AG's News}   & \textbf{Avg.} \\ \midrule
                    %   & (acc)              & (acc)            & (acc)          & (acc)        & (acc)               &  \\ \midrule
 Fine-Tuning          & 80.6 \scriptnumber{3.9}         & 88.7 \scriptnumber{4.7}       & 67.4 \scriptnumber{9.7}     & 73.3 \scriptnumber{7.5} & 40.7 \scriptnumber{3.0} & \textbf{51.0} \scriptnumber{2.2}  & \textbf{84.9} \scriptnumber{3.6}          &  69.5  \\ 
 Manual Prompt       & 82.8               & 83.0             & 80.9           & 79.6    & 34.9 & 42.1      & 76.9               &  68.6  \\
 Instructions        & 89.0               & 84.4             & 85.2           & 80.8     & 29.8 & 43.0    & 54.8               &  58.5  \\
 In-Context Demonstration    & 85.9 \scriptnumber{0.7}         & 89.6 \scriptnumber{0.4}       & 80.6 \scriptnumber{1.4}     & 85.5 \scriptnumber{1.5} & 39.3 \scriptnumber{0.9} & 49.4 \scriptnumber{0.3}  & 74.9 \scriptnumber{0.8}   &  72.2  \\
 Prompt Tuning \emph{(Soft Prompt Tuning)}        & 73.8 \scriptnumber{10.9}        & 88.6 \scriptnumber{2.1}       & 74.1 \scriptnumber{14.6}    & 75.9 \scriptnumber{11.8} & 40.2 \scriptnumber{6.5} & 49.1 \scriptnumber{3.1}   & 82.6 \scriptnumber{0.9}      &  69.2  \\
 BB Tuning \emph{(2 soft tokens)}      & 83.2 \scriptnumber{3.5}         & 86.0 \scriptnumber{1.6}       & 77.1 \scriptnumber{3.9}     & 83.2 \scriptnumber{2.5} & 39.2 \scriptnumber{2.4}  &  41.5 \scriptnumber{1.9}   & 74.0 \scriptnumber{1.9}         &  69.2  \\
 BB Tuning \emph{(5 soft tokens)}      & 84.6 \scriptnumber{4.0}         & 78.7 \scriptnumber{2.3}       & 79.8 \scriptnumber{1.5}     & 82.9 \scriptnumber{3.6} &  36.6 \scriptnumber{2.1} & 33.7 \scriptnumber{2.3}    & 73.6 \scriptnumber{3.6}         &  67.1  \\
 BB Tuning \emph{(Mixed, 50 soft tokens)}      & 89.1 \scriptnumber{0.9}         & 93.2 \scriptnumber{0.5}       & 86.6 \scriptnumber{1.3}     & 87.4 \scriptnumber{1.0} &  38.4 \scriptnumber{1.1} & 44.8 \scriptnumber{1.3}   & 83.5 \scriptnumber{0.9}         &  74.7  \\
 GrIPS \emph{(Discrete Prompt Enumeration)}                 & 87.1 \scriptnumber{1.5}         & 88.2 \scriptnumber{0.1}       & 86.1 \scriptnumber{0.3}     & 80.0 \scriptnumber{2.5} & 32.0 \scriptnumber{1.8} & 47.2 \scriptnumber{0.5}   & 65.4 \scriptnumber{9.8}      &  69.4  \\ 
 AutoPrompt            & 75.0 \scriptnumber{7.6}         & 79.8 \scriptnumber{8.3}       & 62.0 \scriptnumber{0.8}     & 57.5 \scriptnumber{5.8} & 27.8 \scriptnumber{3.3} & 29.0 \scriptnumber{5.0}   & 65.7 \scriptnumber{1.9}          &  56.7  \\

 
 \midrule
 RLPrompt (Ours, 2 discrete tokens)            &       90.3 \scriptnumber{1.3}             &     94.1 \scriptnumber{0.8}              &  86.5 \scriptnumber{1.2}              &     87.4 \scriptnumber{1.7}         & 40.1 \scriptnumber{1.9}    & 45.6 \scriptnumber{3.8} &     76.8 \scriptnumber{1.4}  & 74.4    \\ 
 RLPrompt (Ours, 5 discrete tokens)            &       \textbf{92.5} \scriptnumber{0.8}             &     \textbf{95.1} \scriptnumber{1.0}              &  \textbf{87.1} \scriptnumber{0.4}              &     \textbf{89.5} \scriptnumber{0.6}         & \textbf{41.4} \scriptnumber{3.2}   & 44.8 \scriptnumber{4.3} &      80.2 \scriptnumber{0.7} &   \textbf{75.8}  \\

% 2022.10.19
% & \textbf{SST-2}     & \textbf{Yelp P.} & \textbf{MR}    & \textbf{CR}  & \textbf{SST-5} & \textbf{Yelp} &  \textbf{AG's News} &  \textbf{Subj} &  \textbf{Trec} &  \textbf{Yahoo} &  \textbf{DBPedia}   & \textbf{Avg.} \\ \midrule
%                     %   & (acc)              & (acc)            & (acc)          & (acc)        & (acc)               &  \\ \midrule
%  Fine-Tuning          & 80.6 \scriptnumber{3.9}         & 88.7 \scriptnumber{4.7}       & 67.4 \scriptnumber{9.7}     & 73.3 \scriptnumber{7.5} & \underline{40.7} \scriptnumber{3.0} & \textbf{51.0} \scriptnumber{2.2}  & \textbf{84.9} \scriptnumber{3.6} &  \textbf{89.0} \scriptnumber{3.5}  & \textbf{83.9} \scriptnumber{5.5}  & \textbf{65.6} \scriptnumber{2.4}  & \textbf{97.7} \scriptnumber{0.8}           &  \textbf{74.8}  \\ 
%  Manual Prompt       & 82.8               & 83.0             & 80.9           & 79.6    & 34.9 & 42.1      & 76.9  & 51.5 & 31.8 & 18.1& 59.2 & 58.3 \\
%  Instructions        & 89.0               & 84.4             & 85.2           & 80.8     & 29.8 & 43.0    & 54.8 & 50.4 & 26.2 & 21.4 & 15.9 & 52.8  \\
%  In-Context Demo.    & 85.9 \scriptnumber{0.7}         & 89.6 \scriptnumber{0.4}       & 80.6 \scriptnumber{1.4}     & 85.5 \scriptnumber{1.5} & 39.3 \scriptnumber{0.9} & \underline{49.4} \scriptnumber{0.3}  & 74.9 \scriptnumber{0.8} & 51.9 \scriptnumber{1.3} & 29.2 \scriptnumber{2.0} & 36.7 \scriptnumber{2.1} & 76.6 \scriptnumber{0.4}   &  63.6  \\
%  Prompt Tuning \emph{(Soft Prompt Tuning)}        & 73.8 \scriptnumber{10.9}        & 88.6 \scriptnumber{2.1}       & 74.1 \scriptnumber{14.6}    & 75.9 \scriptnumber{11.8} & 40.2 \scriptnumber{6.5} & 49.1 \scriptnumber{3.1}   & 82.6 \scriptnumber{0.9}  & 73.0 \scriptnumber{7.3} & 49.6 \scriptnumber{6.1} & \underline{59.7} \scriptnumber{1.3} & 84.2 \scriptnumber{5.3}    &  68.3  \\
%  BB Tuning \emph{(2 soft tokens)}      & 83.2 \scriptnumber{3.5}         & 86.0 \scriptnumber{1.6}       & 77.1 \scriptnumber{3.9}     & 83.2 \scriptnumber{2.5} & 39.2 \scriptnumber{2.4}  &  41.5 \scriptnumber{1.9}   & 74.0 \scriptnumber{1.9}   & 75.7 \scriptnumber{3.4} & 40.4 \scriptnumber{2.5} & 41.7 \scriptnumber{1.4} & 60.9 \scriptnumber{6.0}       &  63.9  \\
%  BB Tuning \emph{(5 soft tokens)}      & 84.6 \scriptnumber{4.0}         & 78.7 \scriptnumber{2.3}       & 79.8 \scriptnumber{1.5}     & 82.9 \scriptnumber{3.6} &  36.6 \scriptnumber{2.1} & 33.7 \scriptnumber{2.3}    & 73.6 \scriptnumber{3.6}   & 75.8 \scriptnumber{4.4} & 39.8 \scriptnumber{4.6} & 38.2 \scriptnumber{1.8} & 62.7 \scriptnumber{4.1}      &  62.4  \\
%  BB Tuning \emph{(Mixed, 50 soft tokens)}      & 89.1 \scriptnumber{0.9}         & 93.2 \scriptnumber{0.5}       & \underline{86.6} \scriptnumber{1.3}     & \underline{87.4} \scriptnumber{1.0} &  38.4 \scriptnumber{1.1} & 44.8 \scriptnumber{1.3}   & 83.5 \scriptnumber{0.9}  & 71.9 \scriptnumber{5.1} & 46.4 \scriptnumber{8.2} & 50.0 \scriptnumber{0.9} & \underline{90.2} \scriptnumber{0.8}       & 71.0  \\
%  GrIPS \emph{(Discrete Prompt Enumeration)}                 & 87.1 \scriptnumber{1.5}         & 88.2 \scriptnumber{0.1}       & 86.1 \scriptnumber{0.3}     & 80.0 \scriptnumber{2.5} & 32.0 \scriptnumber{1.8} & 47.2 \scriptnumber{0.5}   & 65.4 \scriptnumber{9.8} & 74.8 \scriptnumber{1.1} & 9.5 \scriptnumber{0.2} & 22.5 \scriptnumber{0.4} & 22.1 \scriptnumber{2.9}     &  55.9 \\ 
%  AutoPrompt            & 75.0 \scriptnumber{7.6}         & 79.8 \scriptnumber{8.3}       & 62.0 \scriptnumber{0.8}     & 57.5 \scriptnumber{5.8} & 27.8 \scriptnumber{3.3} & 29.0 \scriptnumber{5.0}   & 65.7 \scriptnumber{1.9}      & 78.9 \scriptnumber{4.5} & 38.8 \scriptnumber{4.3} & 35.5 \scriptnumber{2.0} & 63.1 \scriptnumber{2.0}    & 55.7  \\

 
%  \midrule
%  RLPrompt (Ours, 2 discrete tokens)            &       \underline{90.3} \scriptnumber{1.3}             &     \underline{94.1} \scriptnumber{0.8}              &  86.5 \scriptnumber{1.2}              &     87.4 \scriptnumber{1.7}         & 40.1 \scriptnumber{1.9}    & 45.6 \scriptnumber{3.8} &     76.8 \scriptnumber{1.4}  & \underline{81.9} \scriptnumber{1.2} & \underline{60.5} \scriptnumber{3.2} & 48.6 \scriptnumber{0.6} & 76.0 \scriptnumber{0.6} & 71.6    \\ 
%  RLPrompt (Ours, 5 discrete tokens)            &       \textbf{92.5} \scriptnumber{0.8}             &     \textbf{95.1} \scriptnumber{1.0}              &  \textbf{87.1} \scriptnumber{0.4}              &     \textbf{89.5} \scriptnumber{0.6}         & \textbf{41.4} \scriptnumber{3.2}   & 44.8 \scriptnumber{4.3} &      \underline{80.2} \scriptnumber{0.7} & 81.2 \scriptnumber{1.7} & 57.6 \scriptnumber{4.6} & 48.6 \scriptnumber{1.0} & 84.6 \scriptnumber{1.9} & \underline{73.0}  \\


 
% Each SOTA category. 
% No detailed explaination
 
%                       & \textbf{SST-5} & \textbf{DBPedia} & \textbf{Yahoo} & \textbf{RTE} & \textbf{SNLI}  & \textbf{MRPC} \\
%                       & (acc)              & (acc)            & (acc)          & (acc)        & (acc)          & \scriptnumber{F1}  \\ \midrule
%  Manual Prompt         & 34.9               & 59.2             & 17.1           & 51.3         & 49.8           & 61.9  \\
%  Instruction Learning  & 29.8               & 15.9             & 21.4           & 54.2         & 56.2           & 73.2  \\
%  In-context Learning   & 39.3 \scriptnumber{0.9}         & 76.6 \scriptnumber{0.4}       & 58.7 \scriptnumber{2.1}     & 60.0 \scriptnumber{1.7}   & 58.1 \scriptnumber{0.6}     & 58.7 \scriptnumber{4.3}  \\
%  AutoPrompt            & 27.8 \scriptnumber{3.3}         & 63.1 \scriptnumber{2.0}       & 35.5 \scriptnumber{2.0}     & 52.4 \scriptnumber{1.8}   & 36.4 \scriptnumber{3.9}     & 54.6 \scriptnumber{4.9}  \\
%  GrIPS                 & 32.0 \scriptnumber{1.8}         & 22.1 \scriptnumber{2.9}       & 22.5 \scriptnumber{0.4}     & 54.9 \scriptnumber{0.0}   & 55.3 \scriptnumber{0.0}     & 77.0 \scriptnumber{1.1}  \\
%  Prompt Tuning         & 21.6 \scriptnumber{2.9}         & 93.7 \scriptnumber{1.0}       & 59.8 \scriptnumber{1.9}     & 51.2 \scriptnumber{1.4}   & 33.6 \scriptnumber{0.2}     & 49.7 \scriptnumber{4.8}  \\
%  Fine Tuning           &                    &                  &                &              &                &       \\ \midrule

%  DTPG \scriptnumber{our}            &                    &                  &                &              &                &       \\

% 2022-10-20
%                       & \textbf{SST-2}     & \textbf{Yelp P.} & \textbf{MR}    & \textbf{CR}  & \textbf{SST-5} & \textbf{Yelp} &  \textbf{AG's News}   & \textbf{Avg.} \\ \midrule
%                     %   & (acc)              & (acc)            & (acc)          & (acc)        & (acc)               &  \\ \midrule
%  Fine-Tuning          & 80.6 \scriptnumber{3.9}         & 88.7 \scriptnumber{4.7}       & 67.4 \scriptnumber{9.7}     & 73.3 \scriptnumber{7.5} & \underline{40.7} \scriptnumber{3.0} & \textbf{51.0} \scriptnumber{2.2}  & \textbf{84.9} \scriptnumber{3.6}          &  \textbf{74.8}  \\ 
%  Manual Prompt       & 82.8               & 83.0             & 80.9           & 79.6    & 34.9 & 42.1      & 76.9               &  58.3  \\
%  Instructions        & 89.0               & 84.4             & 85.2           & 80.8     & 29.8 & 43.0    & 54.8               &  52.8  \\
%  In-Context Demonstration    & 85.9 \scriptnumber{0.7}         & 89.6 \scriptnumber{0.4}       & 80.6 \scriptnumber{1.4}     & 85.5 \scriptnumber{1.5} & 39.3 \scriptnumber{0.9} & \underline{49.4} \scriptnumber{0.3}  & 74.9 \scriptnumber{0.8}   &  63.6  \\
%  Prompt Tuning \emph{(Soft Prompt Tuning)}        & 73.8 \scriptnumber{10.9}        & 88.6 \scriptnumber{2.1}       & 74.1 \scriptnumber{14.6}    & 75.9 \scriptnumber{11.8} & 40.2 \scriptnumber{6.5} & 49.1 \scriptnumber{3.1}   & 82.6 \scriptnumber{0.9}      &  68.3  \\
%  BB Tuning \emph{(2 soft tokens)}      & 83.2 \scriptnumber{3.5}         & 86.0 \scriptnumber{1.6}       & 77.1 \scriptnumber{3.9}     & 83.2 \scriptnumber{2.5} & 39.2 \scriptnumber{2.4}  &  41.5 \scriptnumber{1.9}   & 74.0 \scriptnumber{1.9}         &  63.9  \\
%  BB Tuning \emph{(5 soft tokens)}      & 84.6 \scriptnumber{4.0}         & 78.7 \scriptnumber{2.3}       & 79.8 \scriptnumber{1.5}     & 82.9 \scriptnumber{3.6} &  36.6 \scriptnumber{2.1} & 33.7 \scriptnumber{2.3}    & 73.6 \scriptnumber{3.6}         &  62.4  \\
%  BB Tuning \emph{(Mixed, 50 soft tokens)}      & 89.1 \scriptnumber{0.9}         & 93.2 \scriptnumber{0.5}       & \underline{86.6} \scriptnumber{1.3}     & \underline{87.4} \scriptnumber{1.0} &  38.4 \scriptnumber{1.1} & 44.8 \scriptnumber{1.3}   & \underline{83.5} \scriptnumber{0.9}         &  71.0  \\
%  GrIPS \emph{(Discrete Prompt Enumeration)}                 & 87.1 \scriptnumber{1.5}         & 88.2 \scriptnumber{0.1}       & 86.1 \scriptnumber{0.3}     & 80.0 \scriptnumber{2.5} & 32.0 \scriptnumber{1.8} & 47.2 \scriptnumber{0.5}   & 65.4 \scriptnumber{9.8}      &  55.9  \\ 
%  AutoPrompt            & 75.0 \scriptnumber{7.6}         & 79.8 \scriptnumber{8.3}       & 62.0 \scriptnumber{0.8}     & 57.5 \scriptnumber{5.8} & 27.8 \scriptnumber{3.3} & 29.0 \scriptnumber{5.0}   & 65.7 \scriptnumber{1.9}          &  55.7  \\

 
%  \midrule
%  RLPrompt (Ours, 2 discrete tokens)            &       \underline{90.3} \scriptnumber{1.3}             &     \underline{94.1} \scriptnumber{0.8}              &  86.5 \scriptnumber{1.2}              &     \underline{87.4} \scriptnumber{1.7}         & 40.1 \scriptnumber{1.9}    & 45.6 \scriptnumber{3.8} &     76.8 \scriptnumber{1.4}  & 71.6    \\ 
%  RLPrompt (Ours, 5 discrete tokens)            &       \textbf{92.5} \scriptnumber{0.8}             &     \textbf{95.1} \scriptnumber{1.0}              &  \textbf{87.1} \scriptnumber{0.4}              &     \textbf{89.5} \scriptnumber{0.6}         & \textbf{41.4} \scriptnumber{3.2}   & 44.8 \scriptnumber{4.3} &      80.2 \scriptnumber{0.7} &   \underline{73.0}  \\

 \bottomrule

 \end{tabular}}}
 
% \vspace{-9pt}
\caption{\small Results of few-shot text classification. The last column shows the average accuracy across all datasets in this table. Additional results can be found in Table~\ref{tab:cls-addition}.
% Here, we only provide 7 datasets and additional datasets are shown in Appendix~\ref{appendix:additional:cls}.
}
% \caption{\small Results of few-shot text classification. The last column shows the average accuracy across all datasets, including those shown in Table~\ref{tab:cls-addition} \hzt{This is weird. We can just show the average of the datasets reported in this particular table.}.  The best result on each dataset is {\bf bolded} and the second best result \underline{underscored}.
% % Here, we only provide 7 datasets and additional datasets are shown in Appendix~\ref{appendix:additional:cls}.
% }
%  The best result on each dataset is {\bf bolded} and the second best result \underline{underscored}.
\label{tab:cls-main}
% \vspace{-5pt}
\end{center}
\end{table*}
```

## Table 4
```latex
\begin{table*}[t]
\vspace{-5pt}
\centering
{\renewcommand{\arraystretch}{0.9}
\setlength{\tabcolsep}{4pt}
\small
%\resizebox{\textwidth}{15mm}{
\begin{tabular}{@{}l c c c c c c c c@{}}
\toprule
{\bf Methods} & \makecell{{\bf Frozen}\\{\bf LMs}} & {\bf Automated} & \makecell{{\bf Gradient-}\\{\bf Free}} & \makecell{{\bf Guided}\\{\bf Optimize}} & \makecell{{\bf Few-}\\{\bf Shot}} & \makecell{{\bf Zero-}\\{\bf Shot}}  & \makecell{{\bf Transferrable}\\ {\bf b/w LMs}} & \makecell{{\bf Interpret-}\\{\bf -ability}}  \\ \midrule
Fine-Tuning & \xmark  & \cmark  & \xmark  & \cmark  & \xmark & \xmark & \xmark & \xmark \\
Manual Prompt  & \cmark  &  \xmark  &   \cmark  &  \xmark & \cmark & \cmark & \cmark & \cmark \\
Instructions & \cmark  &  \xmark  &   \cmark  &  \xmark & \cmark & \cmark & \cmark & \cmark \\
In-Context Demonstration & \cmark  & \cmark  & \cmark & \xmark  & \cmark &  \xmark & \cmark & \cmark \\
Soft Prompt Tuning & \cmark  & \cmark  & \xmark & \cmark &  \cmark & \xmark & \xmark & \xmark \\ 
Discrete Prompt Enumeration & \cmark  & \cmark  & \cmark & \xmark  & \cmark & \cmark &  \cmark & \cmark \\
AutoPrompt~\cite{shin2020autoprompt} & \cmark &  \cmark & \xmark  &  \cmark & \cmark & \xmark & \cmark & \cmark  \\  
%\midrule
% Black Box Tuning & \cmark  & \cmark  & \cmark & \cmark &  \cmark & \xmark & \xmark & \xmark \\ %\midrule
\midrule
RLPrompt ({\bf Ours}) & \cmark  & \cmark  & \cmark & \cmark  & \cmark & \cmark &  \cmark & \cmark \\
\bottomrule
\end{tabular}
}
%}
% \vspace{-9pt}
\caption{ \small
Comparison of different (prompting) paradigms for using pre-trained LMs on downstream tasks, in terms of several desirable properties. 
% \emph{Guided Optimize} means the optimization or search is guided by either gradient or reward signals, and thus tends to be more efficient than those without guidance (e.g., enumeration).
\emph{Gradient-Free} methods do not require gradient information from the prompted LMs, which may be inaccessible or expensive to compute.
\emph{Guided Optimize} means the optimization/search is guided by gradient or reward signals, which tends to be more efficient than otherwise (e.g., enumeration).
% Prompts consisting of discrete tokens (as opposed to embeddings) are often \emph{transferrable}/reusable by different LMs. Our approach with RL can optimize prompts with rewards without any supervised data (\emph{zero-shot}).
Prompts of discrete tokens (as opposed to embeddings) are often \emph{transferrable}/reusable by different LMs. 
Our approach with RL can optimize prompts using rewards without supervised data (\emph{zero-shot}).
\emph{Discrete Prompt Enumeration} selects the best prompt from a large number of candidates 
% (e.g., from paraphrasing or generation) 
% from which the best is selected 
\cite[e.g., from paraphrasing or generation, ][]{jiang2020can, gao2021LMBFF, liu2021KATE, prasad2022grips}. 
\emph{AutoPrompt} \cite{shin2020autoprompt} uses gradients to edit the discrete prompt tokens. 
%Soft prompt often requires large training data \cite{lester2021promptuning, gu2021ppt, liu2021gpt} (except for some of the recent developments).
See \S\ref{sec:relatedwork} and Appendix \S\ref{appendix:related-work} for more discussion.
% \hzt{
% requires-gradient, interpretable, transferrable b/w LMs, applicable to MLMs, applicable to L2R LMs, few-shot, automated}
%\hzt{What properties we have but few-shot prompt does not? ... perhaps zero-shot (our TST is zero-shot)}
% \cp{Can we change the order of this table to match the related work about prompt learning histories. Also, I think AutoPrompt doesn't work well on FS.}
}
\label{tab:summary}
%\vspace{-2pt}
\end{table*}
```

## Table 5
```latex
\begin{table*}[t]
% \centering
% \small
% \resizebox{\textwidth}{15mm}{
% \begin{tabular}{@{}l c c c c c c@{}}
% \toprule
% {\bf Methods} & {\bf Transferable b. datasets} & {\bf Low-data} & {\bf Transferable b. LMs}  & {\bf Gradient-expensive} & {\bf Frozen LMs} \\ \midrule
% Manual Template  & Unstable &  Unstable  & unstable & \xmark & \cmark\\
% Prompt Paraphrasing & Unstable & Unstable  & unstable & \xmark & \cmark\\ %\midrule
% Gradient-guided Search & Unstable & Poor  & unstable & \cmark & \cmark\\
% Soft Prompt Tuning & Unstable & Unstable & impossible & \cmark & \cmark\\ 
% Meta Tuning & Unstable & Good (\textbf{CLSF}) & / & \cmark & \xmark\\ 
% \midrule

% RLPrompt ({\bf Ours}) & Stable & Promising$^*$ & Good (\textbf{CLSF}) & \xmark & \cmark\\
% \bottomrule
% \end{tabular}}
% %\vspace{7pt}
% \caption{
% \hzt{Please do not say "Unstable"/"Stable" or "Good/Bad" -- those are all very subjective and need experimental supports. Other properties, like "Fronzen LMs", is inherent features for which no experiments are needed. Let's only compare those inherent features.} \hzt{Use only \xmark\ or \cmark, do not use words}
% Comparison of our \modelname against previous prompt-based paradigms. \textbf{Manual Template} \cite{petroni2019KB, brown2020language, schick2021exploiting, tam2021improving} attempts to hand-craft prompt templates for downstream tasks. \textbf{Prompt Paraphrasing} is the key idea of current discrete prompt engineering works, by some heuristics, e.g. editing \cite{prasad2022grips}, paraphrasing \cite{jiang2020can, prasad2022grips}, or reframing \cite{mishra2021reframing, reif2021recipe, liu2021KATE}, etc. \textbf{Gradient-guided Search} \cite{shin2020autoprompt} is another prevalent paradigm which aims to locate suitable hard trigger tokens with sufficient labeled data. \textbf{Soft Prompt Tuning} \cite{lester2021promptuning} directly optimizes continuous embeddings instead for downstream tasks, yet generally very hard to be tuned, e.g. very sensitive with initialization/learning rate \cite{li2021prefix, gu2021ppt} in low-resource settings, and white-box optimization with expensive gradients, leading to high training cost. \textbf{Meta Tuning}, a paradigm only well suited for few-shot classification (\textbf{CLSF} represents classification) tasks, but also tends to learn few-shot data-specific spurious correlations \cite{utama2021avoiding}. In contrast, our \modelname can be well suited in handling drawbacks of previous prompt learning works (Promising$^*$ means we can show good performance in both few-shot classification and zero-shot text generation).
% %\hzt{requires-gradient, interpretable, transferrable b/w LMs, applicable to MLMs, applicable to L2R LMs, few-shot, automated}
% %\hzt{What properties we have but few-shot prompt does not? ... perhaps zero-shot (our TST is zero-shot)}
% }
% \label{tab:summary}
% \end{table*}
```

## Table 6
```latex
\begin{table*}[t]
\vspace{-5pt}
\centering
{\renewcommand{\arraystretch}{1.0}
% \setlength{\tabcolsep}{3pt}
\small
\begin{tabular}{llllll}
\toprule
{Model}    & {Content}    & {Style}      & {Fluency}    & {\bf $\bm{J}$({\scriptsize C, S, F})} & {\bf GM({\scriptsize C, S, F})} \\%& {BLEU}       & {BERTScore}  & {PPL}$\downarrow$        \\ 
\midrule
% \midrule
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Oracles}}                                                                                                                                                                        \\ 
% % \midrule
% Copy              & 100            & 1.4            & 92.2           & 11.9           & 23.5            & 30.1           & 62.2           & 20.6           \\
% Reference         & 62.2           & 78.9           & 88.7           & 55.9           & 75.8           & 100            & 100            & 30.8          \\
\rowcolor{Gray}
\multicolumn{6}{l}{\textit{Training Baselines}}                                                                                                                                                             \\ 
% \midrule
Style Transformer & 75.2           & 96.4           & 58.6           & 46.1           & 75.2            \\%& 27.6           & 56.1           & 78.2           \\
DiRR              & \textbf{78.8} & \textbf{97.7} & 75.6          & {59.6}          & {83.5}           \\%& \textbf{30.0} & \textbf{61.7} & 40.6           \\ 
% \midrule
\rowcolor{Gray}
\multicolumn{6}{l}{\textit{Prompting Baselines (GPT-2-xl)}}                                                                                                                                             \\ 
% \midrule
Null Prompt       & 37.4          & 94.8           & 97.6           & 33.6           & 70.2            \\%& 6.6            & 35.8           & 59.5           \\
Random Prompt     & 39.6           & 93.8           & \textbf{97.8} & 34.7           & 71.3           \\%& 7.3            & 37.4           & 60.5           \\
Manual Prompt     & 64.2 \scriptnumber{6.8}          & 91.5 \scriptnumber{3.6}          & 93.2 \scriptnumber{1.4}          & 53.4 \scriptnumber{7.9}          & 81.8 \scriptnumber{3.4}           \\%& 19.2 \scriptnumber{4.1}          & 53.1 \scriptnumber{5.0}          & 35.5 \scriptnumber{9.0}          \\ 
% \midrule
\rowcolor{Gray}
\multicolumn{6}{l}{\textbf{\textit{\modelname (Ours)}}}                                                                                                                                                                    \\ 
% \midrule
distilGPT-2       & 57.3 \scriptnumber{1.7}          & 96.5 \scriptnumber{0.1}          & 85.3 \scriptnumber{1.3}          & 46.0 \scriptnumber{0.9}          & 77.9 \scriptnumber{0.4}           \\%& 15.7 \scriptnumber{0.7}          & 49.1 \scriptnumber{0.6}          & 43.6 \scriptnumber{0.6}          \\
GPT-2-small       & 60.0 \scriptnumber{0.4}          & 96.4 \scriptnumber{0.3}          & 89.0 \scriptnumber{2.8}          & 50.7 \scriptnumber{1.3}          & 80.1 \scriptnumber{0.8}           \\%& 16.5 \scriptnumber{0.4}          & 51.3 \scriptnumber{0.6}          & 37.8 \scriptnumber{4.8}          \\
GPT-2-medium      & 65.7 \scriptnumber{1.4}          & 95.2 \scriptnumber{1.2}          & 89.3 \scriptnumber{0.1}          & 56.1 \scriptnumber{1.0}          & 82.3 \scriptnumber{0.4}           \\%& 20.0 \scriptnumber{1.2}          & 55.1 \scriptnumber{1.1}          & 34.4 \scriptnumber{0.8}          \\
GPT-2-large       & 65.1 \scriptnumber{1.8}          & 94.6 \scriptnumber{2.3}          & 91.6 \scriptnumber{0.8}          & 56.5 \scriptnumber{1.3}          & 82.6 \scriptnumber{0.7}           \\%& 19.8 \scriptnumber{0.5}          & 54.7 \scriptnumber{0.7}          & 34.9 \scriptnumber{1.4}          \\
GPT-2-xl      & 72.1 \scriptnumber{1.5}          & 94.2 \scriptnumber{2.4}          & 89.5 \scriptnumber{0.5}          & \textbf{61.4 \scriptnumber{2.2}} & \textbf{84.7 \scriptnumber{1.0}}  \\%& 24.2 \scriptnumber{1.2}          & 59.0 \scriptnumber{0.8}          & \textbf{34.3 \scriptnumber{0.9}} \\ 
 \bottomrule
\end{tabular}
}
% \vspace{-7pt}
\caption{\small Automatic evaluation of our method vs. baselines on the Yelp \cite{shen2017style} sentiment transfer dataset. 
$J(\cdot)$ is our main metric which measures the average joint sentence-level scores of Content, Style, and Fluency as defined in \S\ref{subsec:tst-experiment}.
We also report the geometric mean (GM) of the three aspects.
% We also report popular metrics such as geometric mean (GM) of the three aspects, BLEU and BERTScore with references, and perplexity (PPL). 
% Content measures the content preservation using the CTC metric \cite{deng-etal-2021-compression}. Style is the accuracy under our sentiment classifier. Fluency is accuracy under \citet{krishna-etal-2020-reformulating}'s grammaticality classifier. $J(\cdot)$ is our main metric which measures the average joint sentence level score defined in \S\ref{subsec:tst-experiment}. We also report the following popular metrics: GM, the geometric average of Content, Style, and Fluency; BLEU and BERTScore between outputs and references; PPL, the perplexity under a GPT-2 language model. 
% Copy and Reference are oracles that duplicate the input sentence and use the human-written reference, respectively. 
% Copy and Reference duplicates the input sentence and uses the human-written reference, respectively. 
% All numbers are averaged across 10 evaluation runs per experiment. Manual Prompt is averaged over 3 sets of manually-written prompts shown in Table \ref{tab:tst-prompt-examples}. Our methods (\modelname) are averaged across 3 experiments. 
Numbers in (parentheses) are standard deviations across 3 sets of prompts. 
% \hzt{Add some cell background coloring to make the table structure clearer, e.g., \url{https://arxiv.org/pdf/2010.05906.pdf} table.1} 
% \hzt{Perhaps move "Oracles" to the top, so "ours" are in the bottom as convention, to make "ours" results clearer.}
% \hzt{Add some vertical spacing to make the table less dense}
% \mingkai{TODO:Change stderr to stdev}
}
\label{tab:tst-yelp-auto}
% \vspace{-5pt}
\end{table*}
```

## Table 7
```latex
\begin{table*}[t]
% \centering
% {\renewcommand{\arraystretch}{1.2}
% \setlength{\tabcolsep}{5pt}
% \small
% \begin{tabular}{lrrrrr | rrr}
% \toprule
% {Model}    & {Content}    & {Style}      & {Fluency}    & {\bf $\bm{J}$({\scriptsize C, S, F})} & {\bf GM({\scriptsize C, S, F})} & {BLEU}       & {BERTScore}  & {PPL}$\downarrow$        \\ 
% \midrule
% % \midrule
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Oracles}}                                                                                                                                                                        \\ 
% % \midrule
% Copy              & 100 \scriptnumber{0.0}           & 1.4 \scriptnumber{0.0}           & 92.2 \scriptnumber{0.0}          & 11.9 \scriptnumber{0.0}          & 23.5 \scriptnumber{0.0}           & 30.1 \scriptnumber{0.0}          & 62.2 \scriptnumber{0.0}          & 20.6 \scriptnumber{0.0}          \\
% Reference         & 62.2 \scriptnumber{0.0}          & 78.9 \scriptnumber{0.0}          & 88.7 \scriptnumber{0.0}          & 55.9 \scriptnumber{0.0}          & 75.8 \scriptnumber{0.0}          & 100 \scriptnumber{0.0}           & 100 \scriptnumber{0.0}           & 30.8 \scriptnumber{0.0}         \\
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Training Baselines}}                                                                                                                                                             \\ 
% % \midrule
% Style Transformer & 75.2 \scriptnumber{0.1}          & 96.4 \scriptnumber{0.1}          & 58.6 \scriptnumber{0.2}          & 46.1 \scriptnumber{0.2}          & 75.2 \scriptnumber{0.1}           & 27.6 \scriptnumber{0.1}          & 56.1 \scriptnumber{0.0}          & 78.2 \scriptnumber{0.3}          \\
% DiRR              & \textbf{78.8 \scriptnumber{0.0}} & \textbf{97.7 \scriptnumber{0.1}} & 75.6 \scriptnumber{0.2}          & 59.6 \scriptnumber{0.2}          & 83.5 \scriptnumber{0.1}           & \textbf{30.0 \scriptnumber{0.0}} & \textbf{61.7 \scriptnumber{0.0}} & 40.6 \scriptnumber{0.1}          \\ 
% % \midrule
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Prompting Baselines (GPT-2 xlarge)}}                                                                                                                                             \\ 
% % \midrule
% Null Prompt       & 37.4 \scriptnumber{0.1}          & 94.8 \scriptnumber{0.1}          & 97.6 \scriptnumber{0.1}          & 33.6 \scriptnumber{0.1}          & 70.2 \scriptnumber{0.1}           & 6.6 \scriptnumber{0.1}           & 35.8 \scriptnumber{0.1}          & 59.5 \scriptnumber{2.0}          \\
% Random Prompt     & 39.6 \scriptnumber{0.1}          & 93.8 \scriptnumber{0.2}          & \textbf{97.8 \scriptnumber{0.1}} & 34.7 \scriptnumber{0.2}          & 71.3 \scriptnumber{0.1}           & 7.3 \scriptnumber{0.1}           & 37.4 \scriptnumber{0.1}          & 60.5 \scriptnumber{1.6}          \\
% Manual Prompt     & 64.2 \scriptnumber{1.0}          & 91.5 \scriptnumber{0.6}          & 93.2 \scriptnumber{0.2}          & 53.4 \scriptnumber{1.2}          & 81.8 \scriptnumber{0.5}           & 19.2 \scriptnumber{0.6}          & 53.1 \scriptnumber{0.8}          & 35.5 \scriptnumber{1.4}          \\ 
% % \midrule
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textbf{\textit{\modelname (Ours)}}}                                                                                                                                                                    \\ 
% % \midrule
% distilGPT-2       & 57.3 \scriptnumber{0.3}          & 96.5 \scriptnumber{0.1}          & 85.3 \scriptnumber{0.3}          & 46.0 \scriptnumber{0.2}          & 77.9 \scriptnumber{0.1}           & 15.7 \scriptnumber{0.1}          & 49.1 \scriptnumber{0.1}          & 43.6 \scriptnumber{0.6}          \\
% GPT-2 small       & 60.0 \scriptnumber{0.1}          & 96.4 \scriptnumber{0.1}          & 89.0 \scriptnumber{0.5}          & 50.7 \scriptnumber{0.3}          & 80.1 \scriptnumber{0.1}           & 16.5 \scriptnumber{0.1}          & 51.3 \scriptnumber{0.1}          & 37.8 \scriptnumber{0.9}          \\
% GPT-2 medium      & 65.7 \scriptnumber{0.2}          & 95.2 \scriptnumber{0.2}          & 89.3 \scriptnumber{0.2}          & 56.1 \scriptnumber{0.6}          & 82.3 \scriptnumber{0.1}           & 20.0 \scriptnumber{0.2}          & 55.1 \scriptnumber{0.2}          & 34.4 \scriptnumber{0.3}          \\
% GPT-2 large       & 65.1 \scriptnumber{0.3}          & 94.6 \scriptnumber{0.4}          & 91.6 \scriptnumber{0.2}          & 56.5 \scriptnumber{0.5}          & 82.6 \scriptnumber{0.1}           & 19.8 \scriptnumber{0.1}          & 54.7 \scriptnumber{0.1}          & 34.9 \scriptnumber{0.3}          \\
% GPT-2 xlarge      & 72.1 \scriptnumber{0.2}          & 94.2 \scriptnumber{0.4}          & 89.5 \scriptnumber{0.1}          & \textbf{61.4 \scriptnumber{0.7}} & \textbf{84.7 \scriptnumber{0.2}}  & 24.2 \scriptnumber{0.2}          & 59.0 \scriptnumber{0.1}          & \textbf{34.3 \scriptnumber{0.3}} \\ 
%  \bottomrule
% \end{tabular}
% }
% \vspace{-5pt}
% \caption{Automatic evaluation of our method vs. baselines on the Yelp \cite{shen2017style} sentiment transfer dataset. Content measures the content preservation using the CTC metric \cite{deng-etal-2021-compression}. Style is the accuracy under our sentiment classifier. Fluency is accuracy under \citet{krishna-etal-2020-reformulating}'s grammaticality classifier. $J(\cdot)$ is our main metric which measures the average joint sentence level score defined in \S\ref{subsec:tst-experiment}. We also report the following popular metrics: GM, the geometric average of Content, Style, and Fluency; BLEU and BERTScore between outputs and references; PPL, the perplexity under a GPT-2 language model. Copy and Reference are oracles that duplicate the input sentence and use the human-written reference, respectively. 
% % All numbers are averaged across 10 evaluation runs per experiment. Manual Prompt is averaged over 3 sets of manually-written prompts shown in Table \ref{tab:tst-prompt-examples}. Our methods (\modelname) are averaged across 3 experiments. 
% Numbers in (parentheses) are standard errors of performance. 
% % \hzt{Add some cell background coloring to make the table structure clearer, e.g., \url{https://arxiv.org/pdf/2010.05906.pdf} table.1} 
% % \hzt{Perhaps move "Oracles" to the top, so "ours" are in the bottom as convention, to make "ours" results clearer.}
% % \hzt{Add some vertical spacing to make the table less dense}
% % \mingkai{TODO:Change stderr to stdev}
% }
% \label{tab:tst-yelp-auto}
% \vspace{8pt}
% \end{table*}
```

## Table 8
```latex
\begin{table*}
% \centering
% \small

% {\renewcommand{\arraystretch}{0.9}
% \setlength{\tabcolsep}{5pt}
% \begin{tabular}{llllll | lll}
% \toprule
% {Model}    & {Content}    & {Style}      & {Fluency}    & {\bf $\bm{J}$({\scriptsize C, S, F})} & {\bf GM({\scriptsize C, S, F})} & {BLEU}       & {BERTScore}  & {PPL}$\downarrow$        \\ 
% \midrule
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Oracles}}                                                                          \\
% Copy         & 100                 & 6.3           & 79.1                & 5.6                 & 36.8                 & 25.8          & 51.6          & 54.2          \\
% Reference    & 51.6                & 93.7          & 79.1                & 38.2                & 72.6                 & 100           & 100           & 54.2          \\
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Training Baselines (Full Data)}}                                                                             \\
% Deep Latent  & 47.1                & \textbf{70.8} & 49.8                & 17.8                & 55.0                 & \textbf{19.2} & 38.3          & 78.2          \\
% STRAP        & 54.6                & 69.3          & 85.0                  & \textbf{30.3}       & \textbf{68.5}        & 16.3          & \textbf{46.3} & \textbf{33.3} \\
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Prompting Baselines (GPT2-xl)}}                                           \\
% Null Prompt        & 41.9 \scriptnumber{2.4}          & 56.1 \scriptnumber{5.0}    & 87.6 \scriptnumber{1.1}          & 17.3 \scriptnumber{1.2}          & 59.0 \scriptnumber{0.8}           & 9.3 \scriptnumber{0.8}     & 32.7 \scriptnumber{1.0}    & 48.1 \scriptnumber{1.4}    \\
% Random Prompt      & 46.8 \scriptnumber{2.6}          & 55.0 \scriptnumber{4.7}    & \textbf{89.4 \scriptnumber{0.8}} & 17.7 \scriptnumber{1.3}          & 61.2 \scriptnumber{0.8}           & 10.9 \scriptnumber{0.7}    & 34.8 \scriptnumber{1.0}    & 50.5 \scriptnumber{1.6}    \\
% Manual Prompt      & \textbf{58.8 \scriptnumber{2.7}} & 52.9 \scriptnumber{4.5}    & 82.2 \scriptnumber{1.7}          & 22.2 \scriptnumber{1.9}          & 63.4 \scriptnumber{1.5}           & 14.0 \scriptnumber{0.7}    & 40.4 \scriptnumber{0.7}    & 62.4 \scriptnumber{1.5}    \\
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textbf{\textit{\modelname (Ours -- 100-Shot)}}}                                                                                       \\
% GPT2-xl & 51.8 \scriptnumber{1.5}          & 65.1 \scriptnumber{2.7}    & 85.2 \scriptnumber{0.3}          & \underline{26.7} \scriptnumber{1.3}          & \underline{66.0} \scriptnumber{0.9}           & 13.1 \scriptnumber{0.4}    & 39.0 \scriptnumber{0.8}    & 63.2 \scriptnumber{1.3}   \\ \bottomrule
% \end{tabular}
% }
% \vspace{-5pt}
% \caption{\small Automatic evaluation of our method vs. baselines on the Shakespeare \cite{xu-etal-2012-shakespeare} authorship transfer dataset. For this dataset, our method only uses 100 examples per style, and numbers in (parentheses) are standard deviations across 3 randomly-drawn training sets. The remaining format is the same as Table \ref{tab:tst-yelp-auto}.}
% \label{tab:tst-shakespeare-auto}
% \vspace{-5pt}
% \end{table*}
```

## Table 9
```latex
\begin{table}[t]
\small
\centering
{\renewcommand{\arraystretch}{0.9}
\setlength{\tabcolsep}{3pt}
\vspace{6pt}
\begin{tabular}{lrrrr} \toprule
Model           & Content       & Style         & Fluency       & {\bf GM({\scriptsize C, S, F})} \\ \midrule
DiRR            & \textbf{4.83} & \textbf{4.69} & 4.64          & \textbf{4.72}                   \\
Manual Prompt   & 4.25          & 4.38          & \textbf{4.86} & 4.49                            \\
\modelname (Ours) & \underline{4.41}          & \underline{4.68}          & \underline{4.80}           & \underline{4.63}                            \\ \bottomrule
\end{tabular}
}
% \vspace{-9pt}
\caption{\small Human evaluation on Yelp on 5-Likert scale
%for the same aspects as Table \ref{tab:tst-yelp-auto}.
where the best result on each aspect is {\bf bolded} and the second best result \underline{underscored}. DiRR relies on model fine-tuning.
}
\label{tab:tst-yelp-human}
%\vspace{-2pt}
\end{table}
```

## Table 10
```latex
\begin{table*}[h]
\vspace{-5pt}
\setlength{\tabcolsep}{4pt}
\centering
{\renewcommand{\arraystretch}{0.9}
\small
\begin{tabular}{lrlllll}
\toprule
{Method} & {Prompt PPL}$\downarrow$                                         & {Content} & {Style} & {Fluency} & {$J$({\scriptsize C, S, F})} & {GM({\scriptsize C, S, F})} \\ \midrule
% \modelname                 & $2.54\mathrm{e}5$ {\scriptsize ($2.38\mathrm{e}5$)} &
% \modelname                 & $\approx10^5$ {\scriptsize ($\approx10^5$)} &
\modelname                 & $254$K {\scriptsize ($238$K)} &
\textbf{72.1 {\scriptsize(1.5)}}       & 94.2 {\scriptsize(2.4)}     & 89.5 {\scriptsize(0.5)}       & \textbf{61.4 {\scriptsize(2.2)}} & \textbf{84.7 {\scriptsize(1.0)}}  \\
+ Fluency                     & \textbf{82.1 {\scriptsize(2.4)}}                                                  & 52.4 {\scriptsize(1.5)}       & \textbf{96.2 {\scriptsize(0.9)}}     & \textbf{94.6 {\scriptsize(1.0)}}       & 46.7 {\scriptsize(0.7)} & 78.1 {\scriptsize(0.4)} \\ \bottomrule
\end{tabular}
}
% \vspace{-9pt}
\caption{ \small
% \hzt{Both methods are "ours"}
Comparison of prompt optimization with fluency constraint vs no constraint on the Yelp dataset. Both experiments use GPT-2-xl as the text generation model. Prompt PPL is the prompt's perplexity under a GPT-2 langauge model. The text style transfer metrics are the same as in Table \ref{tab:tst-yelp-auto}.}
\label{tab:tst-fluency}
% \vspace{-2pt}
\end{table*}
```

## Table 11
```latex
\begin{table*}[h]
% \vspace{-5pt}
% \setlength{\tabcolsep}{4pt}
% \centering
% {\renewcommand{\arraystretch}{0.9}
% \small
% \begin{tabular}{lrllllllll}
% \toprule
% {Method} & {Prompt PPL}$\downarrow$                                         & {Content} & {Style} & {Fluency} & {$J$({\scriptsize C, S, F})} & {GM({\scriptsize C, S, F})} & {BLEU} & {BERTScore} & {PPL}$\downarrow$  \\ \midrule
% % \modelname                 & $2.54\mathrm{e}5$ {\scriptsize ($2.38\mathrm{e}5$)} &
% % \modelname                 & $\approx10^5$ {\scriptsize ($\approx10^5$)} &
% \modelname                 & $254$K {\scriptsize ($238$K)} &
% \textbf{72.1 {\scriptsize(1.5)}}       & 94.2 {\scriptsize(2.4)}     & 89.5 {\scriptsize(0.5)}       & \textbf{61.4 {\scriptsize(2.2)}} & \textbf{84.7 {\scriptsize(1.0)}}  & \textbf{24.2 {\scriptsize(1.2)}}      & \textbf{59.0 {\scriptsize(0.8)}}             & \textbf{34.3 {\scriptsize(0.9)}}   \\
% + Fluency                     & \textbf{65.0 {\scriptsize(7.5)}}                                                  & 50.8 {\scriptsize(2.4)}       & \textbf{95.4 {\scriptsize(0.1)}}     & \textbf{93.9 {\scriptsize(0.4)}}       & 44.4 {\scriptsize(2.1)} & 76.9 {\scriptsize(1.1)}  & 11.9 {\scriptsize(0.8)}      & 45.2 {\scriptsize(1.8)}           & 42.0 {\scriptsize(3.0)}     \\ \bottomrule
% \end{tabular}
% }
% \vspace{-9pt}
% \caption{ \small
% % \hzt{Both methods are "ours"}
% Comparison of prompt optimization with fluency constraint vs no constraint on the Yelp dataset. Both experiments use GPT-2-xl as the text generation model. Prompt PPL is the prompt's perplexity under a GPT-2 langauge model. The text style transfer metrics are the same as in Table \ref{tab:tst-yelp-auto}}
% \label{tab:tst-fluency}
% \vspace{-2pt}
% \end{table*}
```

## Table 12
```latex
\begin{table}[t]
% \vspace{6pt}
    \centering
{\renewcommand{\arraystretch}{0.9}
\small
    \begin{tabular}{@{}lcc@{}}
    \toprule
    Verbalizers & \modelname & Manual \\ \midrule
    terrible, great & \textbf{92.8 \scriptnumber{0.8}} & 82.8 \\ 
    bad, good & \textbf{91.2 \scriptnumber{1.4}} & 79.7 \\
    negative, positive & \textbf{92.2 \scriptnumber{0.6}} & 76.8 \\
    \bottomrule
    \end{tabular}}
    % \vspace{-5pt}
    \caption{\small Comparison of \modelname and manual prompt on SST-2 using different verbalizers. 
    %The manual prompt is ``It was" and our prompts consist of 2 tokens.
    %Here we only show one prompt example per verbalizer with 2 tokens.
    % \hzt{We don't need the third column, which is distractive.}
    }
    \label{tab:verbalizers}
    % \vspace{-2pt}
\end{table}
```

## Table 13
```latex
\begin{table*}[t]
\centering
\small

{\renewcommand{\arraystretch}{1}
\setlength{\tabcolsep}{5pt}
\begin{tabular}{llllll | lll}
\toprule
 & & & & & & \multicolumn{2}{c}{Content Preservation} & Fluency \\
{Model}    & {Content}    & {Style}      & {Fluency}    & {\bf $\bm{J}$({\scriptsize C, S, F})} & {\bf GM({\scriptsize C, S, F})} & {BLEU}       & {BERTScore}  & {PPL}$\downarrow$        \\ 
\midrule
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Oracles}}                                                                          \\
% Copy         & 100                 & 6.3           & 79.1                & 5.6                 & 36.8                 & 25.8          & 51.6          & 54.2          \\
% Reference    & 51.6                & 93.7          & 79.1                & 38.2                & 72.6                 & 100           & 100           & 54.2          \\
\rowcolor{Gray}
\multicolumn{9}{l}{\textit{Training Baselines (Full Data)}}                                                                             \\
Deep Latent  & 47.1                & \textbf{70.8} & 49.8                & 17.8                & 55.0                 & \textbf{19.2} & 38.3          & 78.2          \\
STRAP        & 54.6                & 69.3          & 85.0                  & \textbf{30.3}       & \textbf{68.5}        & 16.3          & \textbf{46.3} & \textbf{33.3} \\
\rowcolor{Gray}
\multicolumn{9}{l}{\textit{Prompting Baselines (GPT-2-xl)}}                                           \\
Null Prompt        & 41.9 \scriptnumber{2.4}          & 56.1 \scriptnumber{5.0}    & 87.6 \scriptnumber{1.1}          & 17.3 \scriptnumber{1.2}          & 59.0 \scriptnumber{0.8}           & 9.3 \scriptnumber{0.8}     & 32.7 \scriptnumber{1.0}    & 48.1 \scriptnumber{1.4}    \\
Random Prompt      & 46.8 \scriptnumber{2.6}          & 55.0 \scriptnumber{4.7}    & \textbf{89.4 \scriptnumber{0.8}} & 17.7 \scriptnumber{1.3}          & 61.2 \scriptnumber{0.8}           & 10.9 \scriptnumber{0.7}    & 34.8 \scriptnumber{1.0}    & 50.5 \scriptnumber{1.6}    \\
Manual Prompt      & \textbf{58.8 \scriptnumber{2.7}} & 52.9 \scriptnumber{4.5}    & 82.2 \scriptnumber{1.7}          & 22.2 \scriptnumber{1.9}          & 63.4 \scriptnumber{1.5}           & 14.0 \scriptnumber{0.7}    & 40.4 \scriptnumber{0.7}    & 62.4 \scriptnumber{1.5}    \\
\rowcolor{Gray}
\multicolumn{9}{l}{\textbf{\textit{\modelname (Ours -- 100-Shot)}}}                                                                                       \\
GPT-2-xl & 51.8 \scriptnumber{1.5}          & 65.1 \scriptnumber{2.7}    & 85.2 \scriptnumber{0.3}          & \underline{26.7} \scriptnumber{1.3}          & \underline{66.0} \scriptnumber{0.9}           & 13.1 \scriptnumber{0.4}    & 39.0 \scriptnumber{0.8}    & 63.2 \scriptnumber{1.3}   \\ \bottomrule
\end{tabular}
}
% \vspace{-5pt}
\caption{ Automatic evaluation of our method vs. baselines on the Shakespeare \cite{xu-etal-2012-shakespeare} authorship transfer dataset. For this dataset, our method only uses 100 examples per style, and numbers in (parentheses) are standard deviations across 3 randomly-drawn training sets. The metrics are the same as Tables \ref{tab:tst-yelp-auto} and \ref{tab:tst-yelp-addl}.}
\label{tab:tst-shakespeare-auto}
% \vspace{-5pt}
\end{table*}
```

## Table 14
```latex
\begin{table}[h]
\centering
\vspace{6pt}
{\renewcommand{\arraystretch}{1.0}
\setlength{\tabcolsep}{5pt}
\small
\begin{tabular}{llll}
\toprule
& \multicolumn{2}{c}{Content Preservation} & Fluency \\
{Model}    &  {BLEU}       & {BERTScore}  & {PPL}$\downarrow$        \\ 
\midrule
% \midrule
% \rowcolor{Gray}
% \multicolumn{9}{l}{\textit{Oracles}}                                                                                                                                                                        \\ 
% % \midrule
% Copy              & 100            & 1.4            & 92.2           & 11.9           & 23.5            & 30.1           & 62.2           & 20.6           \\
% Reference         & 62.2           & 78.9           & 88.7           & 55.9           & 75.8           & 100            & 100            & 30.8          \\
\rowcolor{Gray}
\multicolumn{4}{l}{\textit{Training Baselines}}                                                                                                                                                             \\ 
% \midrule
Style Transformer &  27.6           & 56.1           & 78.2           \\
DiRR              & \textbf{30.0} & \textbf{61.7} & 40.6           \\ 
% \midrule
\rowcolor{Gray}
\multicolumn{4}{l}{\textit{Prompting Baselines (GPT-2-xl)}}                                                                                                                                             \\ 
% \midrule
Null Prompt       &  6.6            & 35.8           & 59.5           \\
Random Prompt     &  7.3            & 37.4           & 60.5           \\
Manual Prompt     &  19.2 \scriptnumber{4.1}          & 53.1 \scriptnumber{5.0}          & 35.5 \scriptnumber{9.0}          \\ 
% \midrule
\rowcolor{Gray}
\multicolumn{4}{l}{\textbf{\textit{\modelname (Ours)}}}                                                                                                                                                                    \\ 
% \midrule
distilGPT-2       & 15.7 \scriptnumber{0.7}          & 49.1 \scriptnumber{0.6}          & 43.6 \scriptnumber{0.6}          \\
GPT-2-small       & 16.5 \scriptnumber{0.4}          & 51.3 \scriptnumber{0.6}          & 37.8 \scriptnumber{4.8}          \\
GPT-2-medium      & 20.0 \scriptnumber{1.2}          & 55.1 \scriptnumber{1.1}          & 34.4 \scriptnumber{0.8}          \\
GPT-2-large       & 19.8 \scriptnumber{0.5}          & 54.7 \scriptnumber{0.7}          & 34.9 \scriptnumber{1.4}          \\
GPT-2-xl      & 24.2 \scriptnumber{1.2}          & 59.0 \scriptnumber{0.8}          & \textbf{34.3 \scriptnumber{0.9}} \\ 
 \bottomrule
\end{tabular}
}
% \vspace{-7pt}
\caption{ 
Additional automatic evaluation results on Yelp \cite{shen2017style} sentiment transfer.
% Automatic evaluation of our method vs. baselines on the Yelp \cite{shen2017style} sentiment transfer dataset. 
% $J(\cdot)$ is our main metric which measures the average joint sentence-level scores of Content, Style, and Fluency as defined in \S\ref{subsec:tst-experiment}.
% We also report popular metrics such as geometric mean (GM) of the three aspects, BLEU and BERTScore with references, and perplexity (PPL). 
% Content measures the content preservation using the CTC metric \cite{deng-etal-2021-compression}. Style is the accuracy under our sentiment classifier. Fluency is accuracy under \citet{krishna-etal-2020-reformulating}'s grammaticality classifier. $J(\cdot)$ is our main metric which measures the average joint sentence level score defined in \S\ref{subsec:tst-experiment}. We also report the following popular metrics: GM, the geometric average of Content, Style, and Fluency; 
BLEU and BERTScore are computed between outputs and references. PPL is the perplexity under a GPT-2 language model. 
% Copy and Reference are oracles that duplicate the input sentence and use the human-written reference, respectively. 
% Copy and Reference duplicates the input sentence and uses the human-written reference, respectively. 
% All numbers are averaged across 10 evaluation runs per experiment. Manual Prompt is averaged over 3 sets of manually-written prompts shown in Table \ref{tab:tst-prompt-examples}. Our methods (\modelname) are averaged across 3 experiments. 
Numbers in (parentheses) are standard deviations across 3 sets of prompts. 
% \hzt{Add some cell background coloring to make the table structure clearer, e.g., \url{https://arxiv.org/pdf/2010.05906.pdf} table.1} 
% \hzt{Perhaps move "Oracles" to the top, so "ours" are in the bottom as convention, to make "ours" results clearer.}
% \hzt{Add some vertical spacing to make the table less dense}
% \mingkai{TODO:Change stderr to stdev}
}
\label{tab:tst-yelp-addl}
\end{table}
```

## Table 15
```latex
\begin{table*}[h]
% \vspace{5pt}
% \setlength{\tabcolsep}{4pt}
% \centering
% {\renewcommand{\arraystretch}{0.9}
% \small
% \begin{tabular}{lllllll}
% \toprule
% {Method} & {Content} & {Style} & {Fluency} & {\bf $\bm{J}$({\scriptsize C, S, F})} & {\bf GM({\scriptsize C, S, F})} \\ \midrule
% \modelname                 &
% \textbf{72.1 {\scriptsize(1.5)}}       & 94.2 {\scriptsize(2.4)}     & 89.5 {\scriptsize(0.5)}       & \textbf{61.4 {\scriptsize(2.2)}} & \textbf{84.7 {\scriptsize(1.0)}}  \\
% + Joint Score Reward                     & 69.3 {\scriptsize(1.5)}       & \textbf{87.4 {\scriptsize(0.9)}}     & \textbf{99.4 {\scriptsize(1.0)}}       & 60.8 {\scriptsize(0.7)} & 84.4 {\scriptsize(0.4)} \\ 
% - Prompting                     & 69.3 {\scriptsize(1.5)}       & \textbf{87.4 {\scriptsize(0.9)}}     & \textbf{99.4 {\scriptsize(1.0)}}       & 60.8 {\scriptsize(0.7)} & 84.4 {\scriptsize(0.4)} \\ 
% \bottomrule
% \end{tabular}
% }
% \vspace{-9pt}
% \caption{
% % \hzt{Both methods are "ours"}
% Comparison of prompt optimization with fluency constraint vs no constraint on the Yelp dataset. Both experiments use GPT-2-xl as the text generation model. Prompt PPL is the prompt's perplexity under a GPT-2 langauge model. The text style transfer metrics are the same as in Table \ref{tab:tst-yelp-auto}}
% \label{tab:tst-fluency}
% \vspace{-2pt}
% \end{table*}
```

## Table 16
```latex
\begin{table}[t]
    \small
    \resizebox{\columnwidth}{!}{
    \begin{tabular}{@{}lcc@{}}
    \toprule
    Verbalizers & \modelname & Manual \\ 
    \midrule
    World, Sports, Business, Tech & \textbf{77.6} \scriptnumber{1.5} & 76.9 \\
    Global, Athletics, Finance, Technology & \textbf{65.3} \scriptnumber{0.5} &  63.5 \\
    \bottomrule
    \end{tabular}}
    \caption{ Comparison of our method vs. Manual Prompt on AG's News using different verbalizers. The manual prompt is ``News:" and our prompts consist of 2 tokens.}
    % \vspace{5pt}
    \label{tab:verbalizers2}
\end{table}
```

## Table 17
```latex
\begin{table}[t]
    \centering
{\renewcommand{\arraystretch}{1.2}
\small
    \begin{tabular}{@{}rp{4cm}@{}}
    \toprule
    Task Category & Strong Words \\ 
    \midrule
    Sentiment Analysis & \textbf{Absolutely}, \textbf{absolutely}, \textbf{Totally}, \textbf{downright}, profoundly, VERY, Very, Really, highly \\ 
    \begin{tabular}[t]{@{}r@{}} News Classification \end{tabular}
    % Topic Classification 
    &
    \textbf{News},
    \textbf{Reviewer}, 
    \textbf{Reports},
    \textbf{reported}, \textbf{Staff}, \textbf{Information}, \textbf{Statement}, Stories, Guide, say, \\
    \bottomrule
    \end{tabular}}
    % \vspace{-7pt}
    \caption{Strong words from \modelname for different task categories. The words are all sensitive to cases and to whether we prepend the special character Ġ.}
    \label{tab:strong words}
    \vspace{8pt}
\end{table}
```

## Table 18
```latex
\begin{table}[t]
    \small
{\renewcommand{\arraystretch}{1}
    \resizebox{\columnwidth}{!}{
    \begin{tabular}{lcc}
    \toprule
    Template & RoBERTa & GPT-2 \\ 
    \midrule
    \rowcolor{Gray} \multicolumn{3}{l}{SST-2} \\
    \texttt{\textless{}S\textgreater{}} downright \texttt{[MASK]} . &  80.6 &  86.7 \\
    \texttt{\textless{}S\textgreater{}} Really downright \texttt{[MASK]} . &  90.4 &   89.1\\
    \texttt{\textless{}S\textgreater{}} Absolutely \texttt{[MASK]} . & 91.7 & 87.8\\
    \texttt{\textless{}S\textgreater{}} AbsolutelyAbsolutely \texttt{[MASK]} . & 89.2 & 72.3\\
    \begin{tabular}[c]{@{}l@{}} \texttt{\textless{}S\textgreater{}} Absolutely VERY absolute \\   VERY absolute \texttt{[MASK]} . \end{tabular}
    % \texttt{\textless{}S\textgreater{}} Absolutely VERY absolute VERY absolute \texttt{[MASK]} . 
    &  92.7 &  73.8 \\
    \midrule
    \rowcolor{Gray} \multicolumn{3}{l}{AG's News} \\
    \texttt{[MASK]} Reviewer \texttt{\textless{}S\textgreater{}} & 74.5 & --- \\
    \texttt{[MASK]} Reviewer Stories \texttt{\textless{}S\textgreater{}} & 81.0 & --- \\
    \texttt{[MASK]} StaffInformationStatement \texttt{\textless{}S\textgreater{}} &
    76.8 & --- \\
    \begin{tabular}[c]{@{}l@{}} \texttt{[MASK]} StaffInformationStatement \\  Reviewer Stories \texttt{\textless{}S\textgreater{}} \end{tabular}
    &
    % \texttt{[MASK]} StaffInformationStatement\\ Reviewer Stories \texttt{\textless{}S\textgreater{}} &
    79.8 & --- \\
    \bottomrule
    \end{tabular}}
    }
    \caption{The performance of manual prompt examples by composing strong words from Table~\ref{tab:strong words} for both sentiment analysis and news topic classification across RoBERTa-large and GPT-2-large.}
    \label{tab:strongprompt}
\end{table}
```

## Table 19
```latex
\begin{table}[h]
% \centering
% \scriptsize
% \begin{tabular}{lrrr}
% \toprule
%  & \textbf{r-BLEU}   & \textbf{r-BERTScore} & \textbf{PPL}        \\ \hline
% \multicolumn{4}{c}{Training Baselines}                                                       \\ \hline
% Style Transformer       & 27.6 (0.1)          & 56.1 (0.0)             & 78.2 (0.3)          \\
% DiRR                    & \textbf{30.0 (0.0)} & \textbf{61.7 (0.0)}    & 40.6 (0.1)          \\ \hline
% \multicolumn{4}{c}{Prompting Baselines (GPT-2 xlarge)}                                       \\ \hline
% Null Prompt             & 6.6 (0.1)           & 35.8 (0.1)             & 59.5 (2.0)          \\
% Random Prompt           & 7.3 (0.1)           & 37.4 (0.1)             & 60.5 (1.6)          \\
% Manual Prompt           & 19.2 (0.6)          & 53.1 (0.8)             & 35.5 (1.4)          \\ \hline
% \multicolumn{4}{c}{DTPO (Ours)}                                                              \\ \hline
% distilGPT-2             & 15.7 (0.1)          & 49.1 (0.1)             & 43.6 (0.6)          \\
% GPT-2 small             & 16.5 (0.1)          & 51.3 (0.1)             & 37.8 (0.9)          \\
% GPT-2 medium            & 20.0 (0.2)          & 55.1 (0.2)             & 34.4 (0.3)          \\
% GPT-2 large             & 19.8 (0.1)          & 54.7 (0.1)             & 34.9 (0.3)          \\
% GPT-2 xlarge            & 24.2 (0.2)          & 59.0 (0.1)             & \textbf{34.3 (0.3)} \\ \hline
% \multicolumn{4}{c}{Oracles}                                                                  \\ \hline
% Copy                    & 30.1 (0.0)          & 62.2 (0.0)             & 20.6 (0.0)          \\
% Reference               & 100 (0.0)           & 100 (0.0)              & 30.8 (0.0)          \\ \bottomrule
% \end{tabular}
% \caption{Additional evaluation results}
% \label{tab:tst-more-evaluation}
% \end{table}
```

## Table 20
```latex
\begin{table*}[h]
\setlength{\tabcolsep}{2.5pt}
\centering
{\renewcommand{\arraystretch}{1.2}
\small
\begin{tabular}{llrrrrrrrr} \toprule
ID                                                  
& {\begin{tabular}[c]{@{}l@{}}Template \\ {[}\textcolor{red}{to negative} | {\textcolor{teal}{to positive}}{]}\end{tabular}}                                                                                                            & \multicolumn{1}{l}{{Content}} & \multicolumn{1}{l}{{Style}} & \multicolumn{1}{l}{{Fluency}} & \multicolumn{1}{l}{{\bf $\bm{J}$({\scriptsize C, S, F})}} & \multicolumn{1}{l}{\textbf{GM({\scriptsize C, S, F})}} & \multicolumn{1}{l}{{BLEU}} & \multicolumn{1}{l}{{BERTScore}} & \multicolumn{1}{l}{{PPL$\downarrow$}} \\ \midrule
\rowcolor{Gray}
\multicolumn{10}{l}{\textit{Null Prompt}}                   \\
1                                                 
& "\{input\}" "                                                                                                                                                                                           & 37.4 \scriptnumber{0.1}                                & 94.8 \scriptnumber{0.1}                             & \textbf{97.6 \scriptnumber{0.1}}                        & 33.6 \scriptnumber{0.1}                                  & 70.2 \scriptnumber{0.1}                                   & 6.6 \scriptnumber{0.1}                              & 35.8 \scriptnumber{0.1}                                 & 59.5 \scriptnumber{2.0}                            \\ 
\vspace{0cm} \\
\rowcolor{Gray}
\multicolumn{10}{l}{\textit{Manual Prompt}}                   \\
 1                                            
& \begin{tabular}[c]{@{}l@{}}Here is some text: "\{input\}". \\ Here is a rewrite of the text, \\ which is more \\ {[}\textcolor{red}{negative} | \textcolor{teal}{positive}{]}: "\end{tabular}                                              & 72.1 \scriptnumber{0.1}                               & 94.8 \scriptnumber{0.3}                             & 91.6 \scriptnumber{0.1}                               & 62.3 \scriptnumber{0.2}                                  & \textbf{85.6 \scriptnumber{0.1}}                            & 23.9 \scriptnumber{0.1}                             & 58.8 \scriptnumber{0.1}                                 & \textbf{29.6 \scriptnumber{0.3}}                 \\ 
\vspace{0cm} \\
 2                                              & \begin{tabular}[c]{@{}l@{}}Change the following sentence \\ from {[}\textcolor{red}{positive} | \textcolor{teal}{negative}{]} \\ sentiment to {[}\textcolor{red}{negative} | \textcolor{teal}{positive}{]} \\ sentiment but keep its \\ semantics. "\{input\}" "\end{tabular} & 60.4 \scriptnumber{0.1}                              & 91.9 \scriptnumber{0.2}                             & 94.0 \scriptnumber{0.1}                                & 50.5 \scriptnumber{0.1}                                  & 80.5 \scriptnumber{0.1}                                   & 17.4 \scriptnumber{0.1}                            & 51.3 \scriptnumber{0.1}                                & 31.0 \scriptnumber{0.4}                           \\ 
 \vspace{0cm} \\
 3                                              & \begin{tabular}[c]{@{}l@{}}"\{input\}". Rewrite the sentence \\ to be {[}\textcolor{red}{sadder} | \textcolor{teal}{happier}{]} but \\ have the same meaning. "\end{tabular}                                                               & 60.2 \scriptnumber{0.2}                                & 87.7 \scriptnumber{0.4}                              & 94.0 \scriptnumber{0.2}                                & 47.4 \scriptnumber{0.3}                                   & 79.2 \scriptnumber{0.1}                                    & 16.2 \scriptnumber{0.1}                             & 49.3 \scriptnumber{0.1}                                  & 45.8 \scriptnumber{0.7}                            \\ 
 \vspace{0cm} \\
 \rowcolor{Gray}
\multicolumn{10}{l}{\textit{Fluent Prompt}}                   \\
 1                                              & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{I don't like having} | \\ \textcolor{teal}{I love my life (}] "\{input\}" "\end{tabular}                             & 54.1 \scriptnumber{0.5}                                & 95.2 \scriptnumber{0.4}                               & 93.9 \scriptnumber{0.7}                                & 47.4 \scriptnumber{0.4}                                   & 78.5 \scriptnumber{0.3}                                    & 13.4 \scriptnumber{0.4}                             & 45.7 \scriptnumber{0.2}                                  & 52.3 \scriptnumber{1.9}                            \\ 
 \vspace{0cm} \\
 2                                              & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{\ This is not an example} |\\ \textcolor{teal}{The best is good\textbackslash{}n}{]} "\{input\}" "\end{tabular}                & 51.5 \scriptnumber{0.1}                                & \textbf{96.8 \scriptnumber{0.4}}                              & 94.2 \scriptnumber{0.6}                                & 46.0 \scriptnumber{0.4}                                   & 77.7 \scriptnumber{0.1}                                    & 11.9 \scriptnumber{0.3}                             & 46.2 \scriptnumber{0.2}                                  & 35.4 \scriptnumber{2.3}                            \\ 
 \vspace{0cm} \\
 3                                              & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{I don't like} |\\ \textcolor{teal}{I love my work (}{]} "\{input\}" "\end{tabular}                & 51.5 \scriptnumber{0.4}                                & 96.6 \scriptnumber{0.7}                              & 95.7 \scriptnumber{0.5}                                & 46.7 \scriptnumber{0.5}                                   & 78.1 \scriptnumber{0.2}                                    & 12.3 \scriptnumber{0.3}                             & 46.2 \scriptnumber{0.3}                                  & 43.5 \scriptnumber{1.3}                            \\ 
 \vspace{0cm} \\
% \begin{tabular}[c]{@{}l@{}}RL 1\\ (Ours)\end{tabular} 
\rowcolor{Gray}
\multicolumn{10}{l}{\textbf{\textit{\modelname (Ours)}}}                   \\
1
& \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Fixed ($-$ contrasts ($-$ contrasts} | \\ \textcolor{teal}{Dutch English excellent Correct} \\ \textcolor{teal}{(\textgreater{}}{]} "\{input\}" "\end{tabular}                                                     & 71.5 \scriptnumber{0.1}                                & {96.6 \scriptnumber{0.2}}                      & 90.1 \scriptnumber{0.2}                                & \textbf{62.8 \scriptnumber{0.9}}                           & 85.4 \scriptnumber{0.1}                                    & 23.5 \scriptnumber{0.1}                             & 58.7 \scriptnumber{0.1}                                  & 34.1 \scriptnumber{0.2}                            \\ 
\vspace{0cm} \\
% \begin{tabular}[c]{@{}l@{}}RL 2\\ (Ours)\end{tabular} 
2
& \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Fixed RemovedChanged} \\ \textcolor{red}{Prevent outcomes} | \\ \textcolor{teal}{Parameters Comparison}\\ \textcolor{teal}{)=( Compare either}{]} \\ "\{input\}" "\end{tabular}                                                 & 71.0 \scriptnumber{0.1}                                & 91.9 \scriptnumber{0.3}                              & 89.3 \scriptnumber{0.2}                                & 58.9 \scriptnumber{1.1}                                   & 83.5 \scriptnumber{0.1}                                    & 23.7 \scriptnumber{0.1}                             & 58.3 \scriptnumber{0.1}                                  & 35.3 \scriptnumber{0.5}                            \\
\vspace{0cm} \\ 
% \begin{tabular}[c]{@{}l@{}}RL 3\\ (Ours)\end{tabular} 
3
& \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Affect differed judgments} \\ \textcolor{red}{($-$ analysis} | \textcolor{teal}{Difference} \\ \textcolor{teal}{experiences ($-$ contrasting} \\ \textcolor{teal}{experience}{]} "\{input\}" "\end{tabular}                                           & \textbf{73.8 \scriptnumber{0.1}}                        & 94.0 \scriptnumber{0.2}                              & 89.2 \scriptnumber{0.2}                                & 62.6 \scriptnumber{1.1}                                   & 85.2 \scriptnumber{0.1}                                    & \textbf{25.6 \scriptnumber{0.1}}                    & \textbf{59.9} \scriptnumber{0.1}                         & 33.5 \scriptnumber{0.5}                            \\ \bottomrule
\end{tabular} 
}
\caption{Text style transfer performance for various baseline and learned prompts. Manual refers to manually-written prompts, with 1 from \cite{reif2021recipe} and 2-3 written for this experiment. Fluent refers to prompts learned using our method with fluency constraint (\S\ref{subsec:analysis}). RL refers to our main prompt optimization method. The metrics are the same as in Table \ref{tab:tst-yelp-auto}. All outputs are generated using GPT-2-xl and metrics are averaged over 5 runs. Numbers in (parentheses) are standard errors of the averaged metrics.
% \cp{Maybe we can use different color for negative and positive?}
}
\label{tab:tst-prompt-examples}
\end{table*}
```

## Table 21
```latex
\begin{table*}[h]
\setlength{\tabcolsep}{2.5pt}
\centering
{\renewcommand{\arraystretch}{1.2}
\small
\begin{tabular}{llrrrrrrrr} \toprule
ID                                                  
& {\begin{tabular}[c]{@{}l@{}}Template \\ {[}\textcolor{red}{to old} | {\textcolor{teal}{to modern}}{]}\end{tabular}}                                                                                                            & \multicolumn{1}{l}{{Content}} & \multicolumn{1}{l}{{Style}} & \multicolumn{1}{l}{{Fluency}} & \multicolumn{1}{l}{{{\bf $\bm{J}$({\scriptsize C, S, F})}}} & \multicolumn{1}{l}{\textbf{GM({\scriptsize C, S, F})}} & \multicolumn{1}{l}{{BLEU}} & \multicolumn{1}{l}{{BERTScore}} & \multicolumn{1}{l}{{PPL$\downarrow$}} \\ \midrule
\rowcolor{Gray}
\multicolumn{10}{l}{\textit{Null Prompt}}                   \\
1                                                 
& "\{input\}" "                                                                                                                                                                                           & 41.9 \scriptnumber{0.6}                                & 56.1 \scriptnumber{1.3}                             & \textbf{87.6 \scriptnumber{0.3}}                        & 17.3 \scriptnumber{0.3}                                  & 59.0 \scriptnumber{0.2}                                   & 9.3 \scriptnumber{0.2}                              & 32.7 \scriptnumber{0.3}                                 & \textbf{48.1 \scriptnumber{0.4}}                            \\ 
\vspace{0cm} \\
\rowcolor{Gray}
\multicolumn{10}{l}{\textit{Manual Prompt}}                   \\
 1                                            
& \begin{tabular}[c]{@{}l@{}}Here is some text: "\{input\}". \\ Here is a rewrite of the text, \\ which is {[}\textcolor{red}{old} |  \textcolor{teal}{modern}{]} \\ English: "\end{tabular}                                              & 61.5 \scriptnumber{0.2}                               & 51.0 \scriptnumber{1.1}                             & 80.1 \scriptnumber{0.1}                               & 22.6 \scriptnumber{0.6}                                  & {63.1 \scriptnumber{0.5}}                            & \textbf{14.6 \scriptnumber{0.1}}                             & \textbf{40.9 \scriptnumber{0.1}}                                 & {62.6 \scriptnumber{0.2}}                 \\ 
\vspace{0cm} \\
 2                                              & \begin{tabular}[c]{@{}l@{}}Change the following sentence \\ from {[}\textcolor{red}{modern} | \textcolor{teal}{old}{]} English \\ to {[}\textcolor{red}{old} | \textcolor{teal}{modern}{]} English but \\ keep its semantics. "\{input\}" "\end{tabular} & 56.0 \scriptnumber{0.9}                              & 54.1 \scriptnumber{2.3}                             & 83.3 \scriptnumber{0.4}                                & 21.4 \scriptnumber{0.8}                                  & 63.1 \scriptnumber{0.7}                                   & 13.4 \scriptnumber{0.3}                            & 39.7 \scriptnumber{0.3}                                & 61.8 \scriptnumber{0.9}                           \\ 
 \vspace{0cm} \\
 3                                              & \begin{tabular}[c]{@{}l@{}}"\{input\}". Rewrite the sentence \\ to be {[}\textcolor{red}{old} | \textcolor{teal}{new}{]} English \\ but have the same meaning. "\end{tabular}                                                               & \textbf{58.9 \scriptnumber{0.7}}                                & 53.5 \scriptnumber{2.4}                              & 83.2 \scriptnumber{0.6}                                & 22.5 \scriptnumber{1.1}                                   & 63.9 \scriptnumber{0.9}                                    & 13.9 \scriptnumber{0.3}                             & 40.7 \scriptnumber{0.2}                                  & 62.8 \scriptnumber{0.7}                            \\ 
 \vspace{0cm} \\
\rowcolor{Gray}
\multicolumn{10}{l}{\textbf{\textit{\modelname (Ours)}}}                   \\
1
& \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Measure$\cdot$Psal Sanskrit thereto}$^*$ | \\ \textcolor{teal}{TacomaExcellent happiness} \\ \textcolor{teal}{verbs positives{}}{]} "\{input\}" "\end{tabular}                                                     & 49.9 \scriptnumber{0.1}                                & \textbf{67.3 \scriptnumber{0.4}}                      & 85.3 \scriptnumber{0.1}                                & {26.4 \scriptnumber{0.1}}                           & 65.9 \scriptnumber{0.1}                                    & 12.6 \scriptnumber{0.1}                             & 38.0 \scriptnumber{0.1}                                  & 64.5 \scriptnumber{0.4}                            \\ 
\vspace{0cm} \\
% \begin{tabular}[c]{@{}l@{}}RL 2\\ (Ours)\end{tabular} 
2
& \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Character Psal Quran verbsð} | \\ \textcolor{teal}{ Verb Effect verb Effect verb}{]} \\ "\{input\}" "\end{tabular}                                                 & 52.2 \scriptnumber{0.0}                                & 61.7 \scriptnumber{0.4}                              & 85.0 \scriptnumber{0.2}                                & 25.4 \scriptnumber{0.1}                                   & 64.9 \scriptnumber{0.1}                                    & 13.3 \scriptnumber{0.1}                             & 39.0 \scriptnumber{0.1}                                  & 63.2 \scriptnumber{0.3}                            \\
\vspace{0cm} \\ 
% \begin{tabular}[c]{@{}l@{}}RL 3\\ (Ours)\end{tabular} 
3
& \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{ search (< Psal Ethiop} \\ \textcolor{red}{differentiate} | \textcolor{teal}{ Meaning Usage} \\ \textcolor{teal}{ phr phr phr}{]} "\{input\}" "\end{tabular}                                           & 53.3 \scriptnumber{0.1}                       & 66.3 \scriptnumber{0.3}                              & 85.3 \scriptnumber{0.1}                                & \textbf{28.3 \scriptnumber{0.1}}                                   & \textbf{67.1 \scriptnumber{0.1}}                                    & {13.3} \scriptnumber{0.0}                    & {39.9} \scriptnumber{0.1}                         & 61.9 \scriptnumber{0.3}                            \\ \bottomrule
\end{tabular} 
}
\caption{Text style transfer performance for various baseline and learned prompts on Shakespeare \cite{xu-etal-2012-shakespeare}. The metrics and format are the same as Table \ref{tab:tst-prompt-examples}. 
$^*$The dot in this prompt should be the ``dagesh'' character in Hebrew, with unicode number U+05BC. Here we use \textbackslash{}cdot for easier rendering.
% \cp{Maybe we can use different color for negative and positive?}
}
\label{tab:tst-prompt-examples-shakespeare}

\end{table*}
```

## Table 22
```latex
\begin{table*}[h]
% \setlength{\tabcolsep}{3pt}
% \centering
% \small
% \begin{tabular}{llrrrrrrrr} \toprule
%                                                       & {\begin{tabular}[c]{@{}l@{}}Template \\ {[}\textcolor{red}{to negative} | {\textcolor{teal}{to positive}}{]}\end{tabular}}                                                                                                            & \multicolumn{1}{l}{{Content}} & \multicolumn{1}{l}{{Style}} & \multicolumn{1}{l}{{Fluency}} & \multicolumn{1}{l}{{$J$({\scriptsize C, S, F})}} & \multicolumn{1}{l}{{GM({\scriptsize C, S, F})}} & \multicolumn{1}{l}{{BLEU}} & \multicolumn{1}{l}{{BERTScore}} & \multicolumn{1}{l}{{PPL}} \\ \midrule
% Null                                                  & "\{input\}" "                                                                                                                                                                                           & 0.1 & 0.1 & 0.1 & 0.1 & 0.1 & 0.1 & 0.1 & 2.0                             \\ \vspace{0cm} \\
% Manual 1                                              & \begin{tabular}[c]{@{}l@{}}Here is some text: "\{input\}". \\ Here is a rewrite of the text, \\ which is more \\ {[}\textcolor{red}{negative} | \textcolor{teal}{positive}{]}: "\end{tabular}                                              & 0.1 & 0.3 & 0.1 & 0.2 & 0.1 & 0.1 & 0.1 & 0.3                 \\ \vspace{0cm} \\
% Manual 2                                              & \begin{tabular}[c]{@{}l@{}}Change the following sentence \\ from {[}\textcolor{red}{positive} | \textcolor{teal}{negative}{]} \\ sentiment to {[}\textcolor{red}{negative} | \textcolor{teal}{positive}{]} \\ sentiment but keep its \\ semantics. "\{input\}" "\end{tabular} & 0.1 & 0.2 & 0.1 & 0.1 & 0.1 & 0.1 & 0.1 & 0.4                            \\ \vspace{0cm} \\
% Manual 3                                              & \begin{tabular}[c]{@{}l@{}}"\{input\}". Rewrite the sentence \\ to be {[}\textcolor{red}{sadder} | \textcolor{teal}{happier}{]} but \\ have the same meaning. "\end{tabular}                                                               & 0.2 & 0.4 & 0.2 & 0.3 & 0.1 & 0.1 & 0.1 & 0.7                             \\ \vspace{0cm} \\
% Fluent 1                                              & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{\textless{}|endoftext|\textgreater{}We are not in} | \\ \textcolor{teal}{\textless{}|endoftext|\textgreater{}We love and} \\ \textcolor{teal}{thank}{]} "\{input\}" "\end{tabular}                             & 0.2 & 0.2 & 0.2 & 0.2 & 0.1 & 0.1 & 0.1 & 0.6                            \\ \vspace{0cm} \\
% Fluent 2                                              & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{\textless{}|endoftext|\textgreater{}This is not going} |\\ \textcolor{teal}{\textbackslash{}n\textbackslash{}n\textbackslash{}nI love it and}{]}\\ "\{input\}" "\end{tabular}                & 0.1 & 0.3 & 0.4 & 0.3 & 0.2 & 0.1 & 0.1 & 1.4                             \\ \vspace{0cm} \\
% \begin{tabular}[c]{@{}l@{}}RL 1\\ (Ours)\end{tabular} & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Fixed (- contrasts (- contrasts} | \\ \textcolor{teal}{Dutch English excellent Correct} \\ \textcolor{teal}{(\textgreater{}}{]} "\{input\}" "\end{tabular}                                                     & 0.1 & 0.2 & 0.2 & 0.9 & 0.1 & 0.1 & 0.1 & 0.2                             \\ \vspace{0cm} \\
% \begin{tabular}[c]{@{}l@{}}RL 2\\ (Ours)\end{tabular} & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Fixed RemovedChanged} \\ \textcolor{red}{Prevent outcomes} | \\ \textcolor{teal}{Parameters Comparison}\\ \textcolor{teal}{)=( Compare either}{]} \\ "\{input\}" "\end{tabular}                                                 & 0.1 & 0.3 & 0.2 & 1.1 & 0.1 & 0.1 & 0.1 & 0.5                             \\ \vspace{0cm} \\ 
% \begin{tabular}[c]{@{}l@{}}RL 3\\ (Ours)\end{tabular} & \begin{tabular}[c]{@{}l@{}}{[}\textcolor{red}{Affect differed judgments} \\ \textcolor{red}{(- analysis} | \textcolor{teal}{Difference} \\ \textcolor{teal}{experiences (- contrasting} \\ \textcolor{teal}{experience}{]} "\{input\}" "\end{tabular}                                           & 0.1 & 0.2 & 0.2 & 1.1 & 0.1 & 0.1 & 0.1 & 0.5                           \\ \bottomrule
% \end{tabular} 
% \caption{Standard errors of the average performance metrics presented in Table \ref{tab:tst-prompt-examples}, with exactly the same layout.
% }
% \label{tab:tst-prompt-examples-stderr}
% \end{table*}
```

## Table 23
```latex
\begin{table*}[t]
% \begin{minipage}[!t][4.5cm][t]{\columnwidth}
%     \small
%     \resizebox{\columnwidth}{!}{
%     \begin{tabular}{@{}lcc@{}}
%     \toprule
%     Verbalizers & \modelname & Manual \\ 
%     \midrule
%     World, Sports, Business, Tech & \textbf{77.6} \scriptnumber{1.5} & 76.9 \\
%     Global, Athletics, Finance, Technology & \textbf{65.3} \scriptnumber{0.5} &  63.5 \\
%     \bottomrule
%     \end{tabular}}
%     \caption{\small Comparison of our method vs. Manual Prompt on AG's News using different verbalizers. The manual prompt is ``News:" and our prompts consist of 2 tokens.}
%     \label{tab:verbalizers2}
% \end{minipage}\hfill
% \begin{minipage}[!t][4.5cm][t]{\columnwidth}
%     \small
%     \resizebox{\columnwidth}{!}{
%     \begin{tabular}{lcc}
%     \toprule
%     Template & RoBERTa & GPT2 \\ 
%     \midrule
%     \rowcolor{Gray} \multicolumn{3}{l}{SST-2} \\
%     \texttt{\textless{}S\textgreater{}} downright \texttt{[MASK]} . &  80.6 &  86.7 \\
%     \texttt{\textless{}S\textgreater{}} Really downright \texttt{[MASK]} . &  90.4 &   89.1\\
%     \texttt{\textless{}S\textgreater{}} Absolutely \texttt{[MASK]} . & 91.7 & 87.8\\
%     \texttt{\textless{}S\textgreater{}} AbsolutelyAbsolutely \texttt{[MASK]} . & 89.2 & 72.3\\
%     \texttt{\textless{}S\textgreater{}} Absolutely VERY absolute VERY absolute \texttt{[MASK]} . &  92.7 &  73.8 \\
%     \midrule
%     \rowcolor{Gray} \multicolumn{3}{l}{AG's News} \\
%     \texttt{[MASK]} Reviewer \texttt{\textless{}S\textgreater{}} & 74.5 & --- \\
%     \texttt{[MASK]} Stories \texttt{\textless{}S\textgreater{}} & 51.6 & --- \\
%     \texttt{[MASK]} Reviewer Stories \texttt{\textless{}S\textgreater{}} & 81.0 & --- \\
%     \texttt{[MASK]} News \texttt{\textless{}S\textgreater{}} & 79.6 & --- \\
%     \texttt{[MASK]} News Stories \texttt{\textless{}S\textgreater{}} & 78.0 & --- \\
%     \bottomrule
%     \end{tabular}}
%     \caption{\small The performance of manual prompt examples by composing some strong words together for both sentiment analysis and news topic classification across RoBERTa-large and GPT2-large.}
%     \label{tab:strongprompt}
% \end{minipage}
% \end{table*}
```

## Table 24
```latex
\begin{table*}[t]
%     \centering
% {\renewcommand{\arraystretch}{0.9}
% \small
%     \begin{tabular}{@{}lcc@{}}
%     \toprule
%     Verbalizers & \modelname & Manual \\ \midrule
%     World, Sports, Business, Tech & \textbf{77.6} \scriptnumber{1.5} & 76.9 \\
%     Global, Athletics, Finance, Technology &  \textbf{65.3} \scriptnumber{0.5} &  63.5 \\
%     \bottomrule
%     \end{tabular}}
%     \caption{\small Comparison of our method vs. Manual Prompt on AG's News using different verbalizers. The manual prompt is ``News:" and our prompts consist of 2 tokens.}
%     \label{tab:verbalizers2}
% \end{table*}
```

## Table 25
```latex
\begin{table*}[t]
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{rp{16cm}}
\toprule
Dataset & SST-2 \\ 
Instruction & In this task, you are given sentences from movie reviews. The task is to classify a sentence as "great" if the sentiment of the sentence is positive or as "terrible" if the sentiment of the sentence is negative. \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}} VERY Absolutely \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}} AgentMediaGradeOfficials Grade
\texttt{[MASK]} .\\
\midrule
Dataset & Yelp P. \\ 
Instruction & In this task, you are given Yelp reviews. The task is to classify a review as "great" if the overall sentiment of the review is positive or as "terrible" if the overall sentiment of the review is negative. \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}}  Rating Absolutely \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}}  ProductGradeTimeoutAbsolutely Absolutely \texttt{[MASK]} .\\
\midrule
Dataset & MR \\
Instruction & In this task, you are given sentences from movie reviews. The task is to classify a sentence as "great" if the sentiment of the sentence is positive or as "terrible" if the sentiment of the sentence is negative \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}}  downright absolutely \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}} ouslyicals downright certainly consistently \texttt{[MASK]} .\\
\midrule
Dataset & CR \\
Instruction & In this task, you are given sentences from customer reviews. The task is to classify a sentence as "great" if the sentiment of the sentence is positive or as "terrible" if the sentiment of the sentence is negative. \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}}  ITNESSALLY \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}}  absoluteliterally absolute downright downright \texttt{[MASK]} .\\
\midrule
Dataset & SST-5 \\ 
Instruction & In this task, you are given sentences from movie reviews. Based on the given review, classify it to one of the five classes: (1) terrible, (2) bad, (3) okay, (4) good, and (5) great. \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}} Movie entirely \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}} iciticititableually immediately \texttt{[MASK]} .\\
\midrule
Dataset & Yelp \\ 
Instruction & In this task, you are given Yelp reviews. Based on the given review, classify it to one of the five classes: (1) terrible, (2) bad, (3) okay, (4) good, and (5) great. \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}} =-=- Totally \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}} imalimalimalivable Totally \texttt{[MASK]} .\\
\midrule
Dataset & AG's News \\
Instruction & In this task, you are given a news article. Your task is to classify the article to one out of the four topics "World", "Sports", "Business", "Tech" if the article"s main topic is relevant to the world, sports, business, and technology, correspondingly. If you are not sure about the topic, choose the closest option. \\
\modelname 2 token template & \texttt{[MASK]} Reviewer Information \texttt{\textless{}S\textgreater{}} .\\
\modelname 5 token template & \texttt{[MASK]} StaffAreaFocusHardware Advisory \texttt{\textless{}S\textgreater{}} .\\
\midrule
Dataset & Subj \\
Instruction &  In this task, you are given sentences from reviews. The task is to classify a sentence as "subjective" if the opinion of the sentence is subjective or as "objective" if the opinion of the sentence is objective. \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}} Friends pleasantly \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}} BufferActionDialogDialog downright \texttt{[MASK]} .\\
\midrule
Dataset & TREC \\
Instruction &  You are given a question. You need to detect which category better describes the question. Answer with "Description", "Entity", "Expression", "Human", "Location", and "Number". \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}} DeveloperTermin \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}} BufferHttpRuntimeRunnerostics \texttt{[MASK]} .\\
\midrule
Dataset & Yahoo \\
Instruction &  You are given a passage. Using the information present in the passage, you need to classify it into one of the 10 topics: 0 - Culture, 1 - Science, 2 - Health, 3 - Education, 4 - Computers, 5 - Sports, 6 - Business, 7 - Music, 8 - Family, 9 - Politics. \\
\modelname 2 token template & \texttt{\textless{}S\textgreater{}} Source Ireland \texttt{[MASK]} .\\
\modelname 5 token template & \texttt{\textless{}S\textgreater{}} AlertSource mentioning Besidesadays \texttt{[MASK]} .\\
\midrule
Dataset & DBPedia \\
Instruction &  You are given a passage. Using the information present in the passage, you need to classify it into one of the 10 topics: 0 - Culture, 1 - Science, 2 - Health, 3 - Education, 4 - Computers, 5 - Sports, 6 - Business, 7 - Music, 8 - Family, 9 - Politics.  \\
\modelname 2 token template &  typeSection \texttt{[MASK]} : \texttt{\textless{}S\textgreater{}} .\\
\modelname 5 token template &  CommonExamplesSenate Similar comparable \texttt{[MASK]} : \texttt{\textless{}S\textgreater{}} .\\
\bottomrule
\end{tabular}}
\caption{Manual instructions (following \textit{natural instructions} \cite{mishra2021NI}) we tested with in our baseline implementation and some template cases we learned by \modelname for specific datasets.}


\label{tab:nlu-instruction}
\end{table*}
```

## Table 26
```latex
\begin{table*}[h]
\centering
\begin{center}
{\renewcommand{\arraystretch}{1.0}
% \resizebox{0.8\textwidth}{!}{
\small
\vspace{10pt}
\begin{tabular}{@{}llllll@{}}
\toprule
& Subj                               & TREC                & Yahoo               & DBPedia  & Avg.           \\
\midrule
Fine-Tuning                 & \textbf{89.0} \scriptnumber{3.5}                & \textbf{83.9} \scriptnumber{5.5} & \textbf{65.6} \scriptnumber{2.4} & \textbf{97.7} \scriptnumber{0.8} & \textbf{84.1} \\
Manual Prompt               & 51.5                               & 31.8                & 18.1                & 59.2  & 40.2              \\
Instructions                & 50.4                               & 26.2                & 21.4                & 15.9  & 28.5              \\
In-Context Demonstration             & 51.9 \scriptnumber{1.3}                         & 29.2 \scriptnumber{2.0}          & 36.7 \scriptnumber{2.1}          & 76.6 \scriptnumber{0.4}  & 48.6        \\
Prompt Tuning \textit{(Soft Prompt Tuning)}               & 73.0 \scriptnumber{7.3}                         & 49.6 \scriptnumber{6.1}          & \underline{59.7} \scriptnumber{1.3}          & 84.2 \scriptnumber{5.3}   & 66.6       \\
BB Tuning \textit{(2 soft tokens)}          & 75.7 \scriptnumber{3.4}                         & 40.4 \scriptnumber{2.5}          & 41.7 \scriptnumber{1.4}          & 60.9 \scriptnumber{6.0}  & 54.7        \\
BB Tuning \textit{(5 soft tokens)}         & 75.8 \scriptnumber{4.4}                         & 39.8 \scriptnumber{4.6}          & 38.2 \scriptnumber{1.8}          & 62.7 \scriptnumber{4.1}  & 54.1        \\
BB Tuning \textit{(Mixed, 50 soft tokens)} & 71.8 \scriptnumber{5.1}                         & 46.4 \scriptnumber{8.2}          & 50.0 \scriptnumber{0.9}          & \underline{90.2} \scriptnumber{0.8}  & 64.6        \\
GrIPS \textit{(Discrete Prompt Enumeration)}                      & 74.8 \scriptnumber{1.1}                         & 9.5 \scriptnumber{0.2}           & 22.5 \scriptnumber{0.4}          & 22.1 \scriptnumber{2.9} & 32.2         \\
AutoPrompt                  & 78.9 \scriptnumber{4.5}                         & 38.8 \scriptnumber{4.3}          & 35.5 \scriptnumber{2.0}          & 63.1 \scriptnumber{2.0}  & 54.1        \\
\midrule
RLPrompt (2 discrete tokens)                & \underline{81.9} \scriptnumber{1.2}              & \underline{60.5} \scriptnumber{3.3}          & 48.6 \scriptnumber{0.6}          & 76.0 \scriptnumber{0.6} & 66.8         \\
RLPrompt (5 discrete tokens)                & 81.2 \scriptnumber{1.7}                         & 57.6 \scriptnumber{4.6}          & 48.6 \scriptnumber{1.0}          & 84.6 \scriptnumber{1.9} & \underline{68.0}         \\
\bottomrule
\end{tabular}}
% }
\caption{Additional results of few-shot text classification. The best result on each dataset is {\bf bolded} and the second best result \underline{underscored}. The remaining format follows Table~\ref{tab:cls-main}.}
\label{tab:cls-addition}
\end{center}
\end{table*}
```

