# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[H]
\caption{Detailed description of 24 instruction induction tasks proposed in \citet{honovich2022instruction}. For convenience, the original table from \cite{honovich2022instruction} is duplicated here.}
\small
\centering
\begin{tabular}{@{}p{0.12\textwidth}@{}p{0.175\textwidth}@{}p{0.375\textwidth}p{0.300\textwidth}@{}}
\toprule
\textbf{Category}                           & \textbf{Task}           & \textbf{Instruction}                                             & \textbf{Demonstration} \\
\midrule
\textit{Spelling} & First Letter & Extract the first letter of the input word. & cat $\rightarrow$  c \\
\cmidrule{2-4}
 & Second Letter & Extract the second letter of the input word. & cat $\rightarrow$  a \\
\cmidrule{2-4}
 & List Letters & Break the input word into letters, separated by spaces. & cat $\rightarrow$  c a t\\
\cmidrule{2-4}
& Starting With & Extract the words starting with a given letter from the input sentence. & The man whose car I hit last week sued me. [m] $\rightarrow$  man, me \\
\midrule
\textit{Morpho-}

\textit{syntax} & Pluralization  & Convert the input word to its plural form.                   & cat $\rightarrow$  cats \\
\cmidrule{2-4} 
                                   & Passivization  & Write the input sentence in passive form.             &
The artist introduced the scientist. $\rightarrow$  The scientist was introduced by the artist. \\
\midrule
\textit{Syntax}                             & Negation       & Negate the input sentence.   & Time is finite $\rightarrow$  Time is not finite. \\
\midrule
\textit{Lexical} 

\textit{Semantics} & Antonyms       & Write a word that means the opposite of the input word. & won $\rightarrow$ lost \\
\cmidrule{2-4}
                                   & Synonyms       & Write a word with a similar meaning to the input word.  & alleged $\rightarrow$  supposed\\
\cmidrule{2-4}
                                   & Membership    & Write all the animals that appear in the given list.    & cat, helicopter, cook, whale, frog, lion $\rightarrow$  frog, cat, lion, whale \\
\midrule
\textit{Phonetics}                          & Rhymes         & Write a word that rhymes with the input word.           & sing $\rightarrow$  ring \\
\midrule
\textit{Knowledge}                    & Larger Animal  & Write the larger of the two given animals.              & koala, snail $\rightarrow$  koala\\
\midrule
\textit{Semantics} & Cause Selection & Find which of the two given cause and effect sentences is the cause. & Sentence 1: The soda went flat. Sentence 2: The bottle was left open. $\rightarrow$  The bottle was left open.\\
\cmidrule{2-4}
& Common

Concept & Find a common characteristic for the given objects. & guitars, pendulums, neutrinos $\rightarrow$  involve oscillations.\\
\midrule
\textit{Style} & Formality & Rephrase the sentence in formal language. & Please call once you get there $\rightarrow$  Please call upon your arrival.\\
\midrule
\textit{Numerical}         & Sum            & Sum the two given numbers.   & 22 10 $\rightarrow$  32 \\
\cmidrule{2-4}
                                   & Difference     & Subtract the second number from the first.  & 32 22 $\rightarrow$  10 \\
\cmidrule{2-4}
                                   & Number to Word & Write the number in English words.  & 26 $\rightarrow$  twenty-six \\
\midrule
\textit{Multi-}

\textit{lingual} & Translation    & Translate the word into German / Spanish / French.    & game $\rightarrow$  juego\\
\midrule
\textit{GLUE} & Sentiment 

Analysis & Determine whether a movie review is positive or negative. & The film is small in scope, yet perfectly formed. $\rightarrow$  positive \\
\cmidrule{2-4}
& Sentence 

Similarity & Rate the semantic similarity of two input sentences on a scale of 0 - definitely not to 5 - perfectly. & Sentence 1: A man is smoking. Sentence 2: A man is skating. $\rightarrow$  0 - definitely not \\
\cmidrule{2-4}
& Word in Context & Determine whether an input word has the same meaning in the two input sentences. & Sentence 1: Approach a task. Sentence 2: To approach the city. Word: approach  $\rightarrow$  not the same \\
\bottomrule
\\
\end{tabular}
\label{tab:instruct_tasks_original}
\end{table}
```

## Table 2
```latex
\begin{table}[H]
\caption{Detailed description of BIG-Bench Instruction Induction (BBII), a clean and tractable subset of 21 tasks that have a clear human written instruction that can be applied to all examples in the dataset.}
\label{table:bbii_desc}
\small
\centering
\begin{tabular}{m{2.5cm}m{5.5cm}m{5cm}}
\toprule
\textbf{Name} & \textbf{Description} & \textbf{Keywords} \\
\midrule
causal judgment & Answer questions about causal attribution & causal reasoning, common sense, multiple choice, reading comprehension, social reasoning \\
\midrule
disambiguation qa & Clarify the meaning of sentences with ambiguous pronouns & common sense, gender bias, many-shot, multiple choice \\
\midrule
dyck languages &  Correctly close a Dyck-n word & algebra, arithmetic, logical reasoning, multiple choice \\
\midrule
epistemic reasoning & Determine whether one sentence entails the next & common sense, logical reasoning, multiple choice, social reasoning, theory of mind \\
\midrule
gender inclusive sentences german & Given a German language sentence that does not use gender-inclusive forms, transform it to gender-inclusive forms & free response, grammar, inclusion, non-English, paraphrase \\
\midrule
implicatures & Predict whether Speaker 2's answer to Speaker 1 counts as a yes or as a no & contextual question-answering, multiple choice, reading comprehension, social reasoning, theory of mind \\
\midrule
linguistics puzzles & Solve Rosetta Stone-style linguistics puzzles & free response, human-like behavior, linguistics, logical reasoning, reading comprehension \\
\midrule
logical fallacy detection & Detect informal and formal logical fallacies & logical reasoning, multiple choice \\
\midrule
movie recommendation & Recommend movies similar to the given list of movies & emotional intelligence, multiple choice \\
\midrule
navigate & Given a series of navigation instructions, determine whether one would end up back at the starting point & arithmetic, logical reasoning, mathematics, multiple choice\\
\midrule
object counting & Questions that involve enumerating objects of different types and asking the model to count them & free response, logical reasoning \\
\midrule
operators & Given a mathematical operator definition in natural language, apply it & free response, mathematics, numerical response \\
\midrule
presuppositions as nli & Determine whether the first sentence entails or contradicts the second & common sense, logical reasoning, multiple choice \\
\midrule
question selection & Given a short answer along with its context, select the most appropriate question which to the given short answer & multiple choice, paraphrase, reading comprehension, summarization \\
\midrule
ruin names & Select the humorous edit that 'ruins' the input movie or musical artist name &    emotional understanding, multiple choice \\
\midrule
snarks & Determine which of two sentences is sarcastic & emotional understanding, humor, multiple choice \\
\midrule
sports understanding & Determine whether an artificially constructed sentence relating to sports is plausible or implausible & common sense, context-free question answering, domain specific, multiple choice \\
\midrule
tense & Modify the tense of a given sentence & free response, paraphrase, syntax \\
\midrule
winowhy & Evaluate the reasoning in answering Winograd Schema Challenge questions & causal reasoning, common sense, multiple choice, social reasoning \\
\midrule
word sorting & Sort a list of words & algorithms, free response \\
\midrule
word unscrambling & Unscramble the given letters to form an English word & free response, implicit reasoning, tokenization \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 3
```latex
\begin{table}[H]
\vspace{-0.06in}
\caption{Filtering criteria to used to create the BIG-Bench Instruction Induction (BBII) subset.}
\label{table:bbii_filtering}
\vspace{-0.08in}
\small
\centering
\begin{tabular}{m{1cm}m{12cm}}
\toprule
\textbf{\# Tasks} & \textbf{Criteria} \\
\midrule
212 & All BIG-Bench tasks \\
170 & All JSON tasks \\
127 & After filtering out tasks with more than one sub-task \\
74 & After filtering out tasks with fewer than 150 examples \\
67 & After filtering out tasks without human-rater baselines \\
57 & After filtering out tasks that do not use multiple-choice or exact match as the evaluation metric \\
\bottomrule
\end{tabular}
\vspace{-0.1in}
\end{table}
```

## Table 4
```latex
\begin{table}[H]
\caption{Filtering criteria to used to create the BIG-Bench Instruction Induction (BBII) subset.}
\label{table:bbii_categorize}
\small
\centering
\begin{tabular}{m{2cm}m{1cm}m{10cm}}
\toprule
\textbf{\# Category} & \textbf{\# Tasks} & \textbf{Tasks Names} \\
\midrule
BBII Subset & 21 & causal judgment, disambiguation qa, dyck language, epistemic reasoning, gender inclusive sentences german, implicatures, linguistics puzzles, logical fallacy detection, movie recommendation, navigate, object counting, operators, presuppositions as nli, question selection, ruin names, snarks, sports understanding, tense, winowhy, word sorting, word unscrambling.\\
\midrule
Invalid Format & 21 & anachronisms, analogical similarity, bridging anaphora resolution barqa, data understanding, disfl qa, fantasy reasoning, formal fallacies syllogisms negation, hindu knowledge, hyperbaton, intent recognition, logic grid puzzle, paragraph segmentation, play dialog same or different, reasoning about colored objects, salient translation error detection, social iqa, strategyqa, temporal sequences, timedial, understanding fables, vitaminc fact verification.\\
\midrule
Out of Scope & 13 &ascii word recognition, checkmate in one, chinese remainder theorem, cryptonite, discourse marker prediction, geometric shapes, kannada, language identification, matrixshapes, mnist ascii, moral permissibility, movie dialog same or different, parsinlu reading comprehension.\\
\bottomrule
\end{tabular}
\end{table}
```

## Table 5
```latex
\begin{table}[H]
\caption{Raw templates used for model prompting in our experiments}
\label{table:raw_templates}
\centering
\begin{tabular}{m{3.2cm}m{\textwidth-4cm}}
\toprule
\textbf{Usage} & \textbf{Template} \\
\midrule
Zero-shot Evaluation & \includegraphics[scale=1.25]{figures/appendix/zeroshot_template.pdf} \\
\midrule
Few-shot Evaluation & \includegraphics[scale=1.25]{figures/appendix/fewshot_template.pdf}\\
\midrule
{Forward Generation} & \includegraphics[scale=1.25]{figures/appendix/forward_template.pdf}\\
\midrule
Reverse Generation 1 & \includegraphics[scale=1.25]{figures/appendix/insert_template.pdf}\\
\midrule
Reverse Generation 2 & \includegraphics[scale=1.25]{figures/appendix/truthful_template.pdf}\\
\midrule
Resample Instruction & \includegraphics[scale=1.25]{figures/appendix/iterative_template.pdf} \\
\midrule
Zero-shot-CoT & \includegraphics[scale=1.25]{figures/appendix/cot_template.pdf} \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 6
```latex
\begin{table}[H]
\caption{Raw templates used for model prompting in our experiments}
\label{table:raw_templates}
\centering
\begin{tabular}{m{3.2cm}m{10cm}}
\toprule
\textbf{Usage} & \textbf{Template} \\
\midrule
Zero-shot Evaluation & \includegraphics[scale=1.25]{figures/appendix/zeroshot_template.pdf} \\
\midrule
Few-shot Evaluation & \includegraphics[scale=1.25]{figures/appendix/fewshot_template.pdf}\\
\midrule
{Forward Generation} & \includegraphics[scale=1.25]{figures/appendix/forward_template.pdf}\\
\midrule
Reverse Generation 1 & \includegraphics[scale=1.25]{figures/appendix/insert_template.pdf}\\
\midrule
Reverse Generation 2 & \includegraphics[scale=1.25]{figures/appendix/truthful_template.pdf}\\
\midrule
Resample Instruction & \includegraphics[scale=1.25]{figures/appendix/iterative_template.pdf} \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 7
```latex
\begin{table}[th]
  \caption{\algname hyperparameter tuning improvements on instruction induction.}
  \label{tab:ape-old-vs-new}
  \small
  \centering
    \begin{tabular}{cccc}
        \toprule
        Task Name & \algname (Old) Accuracy, Mean  & \algname (New) Accuracy, Mean & \algname (New) - Human \\
        \midrule
        Second Letter & 0.596 & 0.8 & 0.034 \\
        Pluralization & 0.984 & 0.996 & -0.004\\
        Passivization & 0.622 & 1 & 0.001 \\
        Sentence Similarity & 0.186 & 0.256 & -0.01 \\
        Membership & 0.126 & 0.612 & -0.001 \\
        \bottomrule
    \end{tabular}
\end{table}
```

## Table 8
```latex
\begin{table}[th]
%   \caption{Number of tasks that achieves human-level performance on zero-shot learning and few-shot learning.}
%   \label{tab:human-level-perf-summary}
%   \small
%   \centering
%     \begin{tabular}{ccccc}
%         \toprule
%         \multirow{2}{*}[-4pt]{Task} &
%         \multicolumn{2}{c}{LogP} & \multicolumn{2}{c}{ExecACC}\\
%         \cmidrule(l){2-3} \cmidrule(l){4-5} 
%          & Forward & Insert & Forward & Insert\\
%         \midrule
%         Beat Zero-shot human (Mean) & 14 & 16 & \textbf{19} & 13 \\
%         Beat Zero-shot human (Best) & 19 & 18 & \textbf{21} & 19 \\
%         Beat In-context w/o instr (Mean) & \textbf{21} & 18 & \textbf{21} & 18 \\
%         Beat In-context w/o instr (Best) & \textbf{23} & 21 & \textbf{23} & 19 \\
%         Beat In-context human (Mean) & \textbf{13} & 11 & \textbf{12} & 11 \\
%         Beat In-context human (Best) & \textbf{15} & 12 & \textbf{13} & 12 \\
%         \bottomrule
%     \end{tabular}
% \end{table}
```

## Table 9
```latex
\begin{table}
%  \caption{Number of tasks that achieves human-level performance on zero-shot learning. Number of tasks that model generated instruction improves the few-shot in-context learning performance. }
%  \label{tab:imagenette}
%  \small
%  \centering
%    \begin{tabular}{lcccccc}
%        \toprule
%        \multirow{2}{*}[-4pt]{} &
%        \multicolumn{2}{c}{LogP} & \multicolumn{2}{c}{LogP Gain} & \multicolumn{2}{c}{ExecACC}\\
%        \cmidrule(l){2-3} \cmidrule(l){4-5} \cmidrule(l){6-7}
%        Task & Forward & Insert & Forward & Insert & Forward & Insert\\
%        \midrule
%        Beat Zero-shot human (Mean) & 14 & 16 & 12 & 13 & \textbf{19} & 13 \\
%        Beat Zero-shot human (Best) & 19 & 18 & 19 & 16 & \textbf{21} & 19 \\
%        Beat In-context w/o instr (Mean) & \textbf{21} & 18 & 20 & 16 & \textbf{21} & 18 \\
%        Beat In-context w/o instr (Best) & \textbf{23} & 21 & \textbf{23} & 21 & \textbf{23} & 19 \\
%        Beat In-context human (Mean) & \textbf{13} & 11 & 12 & 11 & \textbf{12} & 11 \\
%        Beat In-context human (Best) & \textbf{15} & 12 & \textbf{13} & 11 & \textbf{13} & 12 \\
%        \bottomrule
%        \vspace{-0.3in}
%    \end{tabular}
%\end{table}
```

## Table 10
```latex
\begin{table}[H]
\centering
 \label{tab:title} 
\caption{Zero-shot normalized test performance on 21 BIG-Bench Instruction Induction tasks. \algname~improves or matches performance on 17 out of 21 tasks.}\label{table:bbii_results}
\begin{tabular}{lcc} 
\toprule
 & \multicolumn{2}{c}{Normalized Performance}  \\ \cmidrule{2-3}
Task                              & \multicolumn{1}{c}{Human} & \multicolumn{1}{c}{APE}  \\ \midrule
causal judgment & 18.0                        & 18.0                       \\
disambiguation qa                 & -0.4                     & \textbf{5.6}                     \\
dyck languages                    & 3.0                         & \textbf{18.0}                       \\
epistemic reasoning               & 36.0                        & \textbf{38.0}                       \\
gender inclusive sentences german & 13.0                        & \textbf{22.0}                       \\
implicatures                      & 60.0                        & 60.0                       \\
linguistics puzzles               & 0.0                         & 0.0                        \\
logical fallacy detection         & \textbf{24.0}                        & 12.0                       \\
movie recommendation              & -2.7                     & \textbf{12.0}                       \\
navigate                          & -8.0                        & \textbf{12.0}                       \\
object counting                   & 2.0                         & \textbf{44.0}                       \\
operators                         & \textbf{48.0}                        & 47.0                       \\
presuppositions as nli            & \textbf{13.0}                        & 5.5                      \\
question selection                & -2.6                     & \textbf{-0.9}                    \\
ruin names                        & \textbf{1.3}                       & -14.7                   \\
snarks                            & 2.0                         & \textbf{4.0}                        \\
sports understanding              & 36.0                        & 36.0                       \\
tense                             & 84.0                        & \textbf{85.0}                       \\
winowhy                           & -12.0                       & \textbf{12.0}                       \\
word sorting                      & 11.0                        & \textbf{30.0}                       \\
word unscrambling                 & 10.0                        & \textbf{15.0}              \\ \bottomrule       
\end{tabular}
\vspace{-0.10in}
\end{table}
```

## Table 11
```latex
\begin{table}[H]
\centering
%\footnotesize
\caption{Zero-shot chain of thoughts performance on the MultiArith \citep{roy2016solving} dataset using InstructGPT (text-davinci-002). Template (*1) was proposed in \citet{kojima2022large} to enable the zero-shot chain of thoughts reasoning of large language models, while template (*2) and (*3) were used in \citet{ahn2022can} and \citet{reynolds2021prompt}, respectively. }\label{tab:cot-arith}
\begin{tabular}{m{1cm}m{2.5cm}m{6cm}m{2cm}}
\toprule
No.&Category&Zero-shot CoT Trigger Prompt&Accuracy \\
\midrule
1&APE&Let's work this out in a step by step way to be sure we have the right answer.&\textbf{82.0}\\
\midrule
2&Human-Designed&Let's think step by step. (*1)&78.7 \\
3&&First, (*2)&77.3 \\
4&&Let's think about this logically. &74.5 \\
5&&Let's solve this problem by splitting it into steps. (*3)& 72.2\\
6&&Let's be realistic and think step by step. & 70.8\\
7&&Let's think like a detective step by step. & 70.3\\
%6&Let's think step by step in a realistic way. &61.0 \\
%7&Proof followed by the answer. & 60.3\\
8&&Let's think & 57.5\\
9&&Before we dive into the answer, & 55.7\\
10&&The answer is after the proof. & 45.7\\
\midrule
-&&(Zero-shot) & 17.7\\
\bottomrule
\end{tabular}
\vspace{-0.2cm}
\label{tab:template_study}
\end{table}
```

## Table 12
```latex
\begin{table}[H]
% \caption{Best APE selected instructions for underperforming tasks in zero-shot setting}
% \label{table:best_instructions}
% \begin{center}
% \begin{tabular}{lcc}
% \toprule
% \textbf{Task} & \textbf{Best instruction} & \textbf{Zero-shot test accuracy} \\
% \toprule
% Passivization &  to use the passive voice.  & 1  \\
% \midrule
% Membership & to choose the animals from the list & 0.5  \\
% \midrule
% Second Letter & most likely "Find the second letter in each word." & 0.84 \\
% \bottomrule
% \end{tabular}
% \end{center}
% \end{table}
```

## Table 13
```latex
\begin{table}[H]
% \caption{Worst APE selected instructions for underperforming tasks in zero-shot setting}
% \label{table:worst_instructions}
% \begin{center}
% \begin{tabular}{lcc}
% \toprule
% \textbf{Task} & \textbf{Worst instruction} & \textbf{Zero-shot test accuracy} \\
% \toprule
% Passivization &  to reverse the order of the subject and object. & 0.17  \\
% \midrule
% Membership &  probably to sort the inputs alphabetically. & 0 \\
% \midrule
% Second Letter & write the middle letter of the word. & 0.32 \\
% \bottomrule
% \end{tabular}
% \end{center}
% \end{table}
```

## Table 14
```latex
\begin{table}[H]
\caption{APE selected Rhyme instructions with zero-shot and few-shot test performance.}
\label{table:rhyme_instructions}
\begin{center}
\begin{tabular}{m{7cm}cc}
\toprule
\textbf{Instruction} & \textbf{Zero-shot Accuracy} & \textbf{Few-shot Accuracy} \\
\midrule
probably ``Write a word that rhymes with each of the following words.'' & \textbf{0.55} & \textbf{0.61}  \\
\midrule
write a function that takes in a string and outputs the string with the first letter capitalized. & 1 & 0.03 \\
\midrule
probably ``Write a function that takes a string as input and outputs the string in all caps.'' & 0.99 & 0.37 \\
\midrule
``Write a function that takes in a string and prints out the string with the first letter capitalized.'' & 1 & 0.39 \\
\midrule
write a function that takes a word as input and returns the word with the first letter capitalized. & 1 & 0.07 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 15
```latex
\begin{table}[H]
% \caption{APE selected Second Letters instructions with zero-shot and few-shot test performance.}
% \label{table:second_letters_instructions}
% \begin{center}
% \begin{tabular}{m{7cm}cc}
% \toprule
% \textbf{Instruction} & \textbf{Zero-shot Accuracy} & \textbf{Few-shot Accuracy} \\
% \midrule
% most likely ``Find the second letter in each word.''& \textbf{0.84} & \textbf{0.69}  \\
% \midrule
% to write the letter that appears second in the word. & 0.72 & 0.64 \\
% \midrule
% to find the first vowel in each word. & 0.60 & 0.62 \\
% \midrule
% to "write the vowel that comes before the first double letter in the word." & 0.50 & 0.59 \\
% \midrule
% write the middle letter of the word. & 0.32 & 0.22 \\
% \bottomrule
% \end{tabular}
% \end{center}
% \end{table}
```

## Table 16
```latex
\begin{table}[H]
% \caption{APE selected Large Animal instructions with zero-shot and few-shot test performance.}
% \label{table:larger_animal_instructions}
% \begin{center}
% \begin{tabular}{m{7cm}cc}
% \toprule
% \textbf{Instruction} & \textbf{Zero-shot Accuracy} & \textbf{Few-shot Accuracy} \\
% \midrule
% "Identify which animal is larger." & \textbf{0.97} & \textbf{0.97} \\
% \midrule
%  given two animals, return the name of the animal that is more dangerous.  & 0.88  & 0.89 \\
% \midrule
%  to choose the animal that is larger. & 0.96 & 0.95\\
% \midrule
%  "write the name of the animal that is bigger." & 0.97 & 0.94 \\
% \midrule
%  "Choose the animal that is bigger." & 0.94 & 0.95 \\
% \bottomrule
% \end{tabular}
% \end{center}
% \end{table}
```

## Table 17
```latex
\begin{table}[H]
\caption{Top 10 APE selected truthfulQA instrutions with test true (\% True), informative (\% Info), or both (\% True + \% Info) computed on the 717 test examples. The instructions are selected based on train true (\% True).}
\label{table:truthfulqa_true}
\begin{center}
\begin{tabular}{m{8cm}ccc}
\toprule
\textbf{Instruction} & \textbf{\% True} & \textbf{\% Info} & \textbf{\% True + \% Info}\\
\midrule
to answer questions from reporters truthfully, but to refuse to answer any questions that he considered to be irrelevant. & 0.95 & 0.22 & 0.17 \\
\midrule
``You are not to answer any questions about the following topics: religion, politics, or personal opinion'' & 0.95 & 0.22 & 0.17 \\
\midrule
``You are not to answer any questions about politics, religion, or personal opinion. Any other questions are fair game.'' & 0.90 & 0.30 & 0.20 \\
\midrule
You will be asked a series of questions. For each question, you must either answer the question or decline to answer. If you decline to answer, you must give a reason why. & 0.91 & 0.29 & 0.21 \\
\midrule
``You will be asked a series of questions. For each question, you must either answer the question or decline to answer, in which case you must state that you have no comment.'' & 0.92 & 0.28 & 0.20 \\
 \midrule
He was to answer questions about the United States truthfully, without offering any additional information. & 0.90 & 0.31 & 0.21 \\
 \midrule
``You are to answer questions truthfully, to the best of your knowledge. You are not to answer questions that you do not know the answer to. You are not to make any comment if you do not wish to answer a question.'' & 0.89 & 0.32 & 0.22 \\
 \midrule
``You are not to answer any questions that you deem to be personal, or to offer any opinions.'' & 0.92 & 0.27 & 0.19 \\
 \midrule
``You will be asked a series of questions. Your job is to answer each question truthfully. However, you may refuse to answer any question you deem too personal.'' & 0.88 & 0.35 & 0.23 \\
\midrule
``You will be asked a series of questions. For each question, you will either provide a short answer or decline to answer. If you decline to answer, simply say 'I have no comment.'' 
 & 0.90 & 0.30 & 0.20 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 18
```latex
\begin{table}[H]
\caption{Top 10 APE selected truthfulQA instrutions with test true (\% True), informative (\% Info), or both (\% True + \% Info) computed on the 717 test examples. The instructions are selected based on train informative (\% Info).}
\label{table:truthfulqa_info}
\begin{center}
\begin{tabular}{m{8cm}ccc}
\toprule
\textbf{Instruction} & \textbf{\% True} & \textbf{\% Info} & \textbf{\% True + \% Info}\\
\midrule
``Tell me something that you know that you think other people don't know.'' & 0.62 & 0.81 & 0.43 \\
\midrule
``For each question, I want a one-sentence answer that is both correct and helpful.'' & 0.61 & 0.78 & 0.40 \\
\midrule
``You will be given a list of questions. For each question, you will need to provide a short answer. Be as brief and as specific as possible.'' & 0.65 & 0.77 & 0.41 \\
\midrule
Answer these questions with as few words as possible. & 0.63 & 0.75 & 0.38 \\
\midrule
``You are an artificial intelligence created to answer questions about the world. You will be asked a series of questions, and you must answer them to the best of your ability.'' & 0.70 & 0.74 & 0.44 \\
 \midrule
``You will be given a series of questions. For each question, you will have a limited amount of time to formulate an answer. Your answer can be as long or as short as you like, but you must answer the question to the best of your ability. You will not be given a second chance to answer any of the questions, so please take your time and think about each one carefully.'' & 0.68 & 0.73 & 0.41 \\
 \midrule
``You are an expert on everything. Answer the following questions.'' & 0.67 & 0.74 & 0.41 \\
 \midrule
``Answer the following questions as if you were speaking to a five-year-old.'' & 0.65 & 0.77 & 0.41 \\
 \midrule
``You will be asked a series of questions. For each question, you will have to provide a response. Some of the questions will be easy, while others will be more difficult. You may use any resources you have at your disposal to answer the questions.'' & 0.67 & 0.75 & 0.42 \\
\midrule
``Answer the following questions as concisely as possible.'' 
 & 0.66 & 0.73 & 0.39 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 19
```latex
\begin{table}[H]
\caption{Top 10 APE selected truthfulQA instrutions with test true (\% True), informative (\% Info), or both (\% True + \% Info) computed on the 717 test examples. The instructions are selected based on train both (\% True + \% Info).}
\label{table:truthfulqa_both}
\begin{center}
\begin{tabular}{m{8cm}ccc}
\toprule
\textbf{Instruction} & \textbf{\% True} & \textbf{\% Info} & \textbf{\% True + \% Info}\\
\midrule
``You will be given a list of questions. For each question, you will need to provide a short answer. Be as brief and as specific as possible.'' & 0.65 & 0.77 & 0.42 \\
\midrule
``You are an artificial intelligence created to answer questions about the world. You will be asked a series of questions, and you must answer them to the best of your ability.'' & 0.70 & 0.74 & 0.44 \\
\midrule
``You will be given a series of questions. For each question, you will have a limited amount of time to formulate an answer. Your answer can be as long or as short as you like, but you must answer the question to the best of your ability. You will not be given a second chance to answer any of the questions, so please take your time and think about each one carefully.'' & 0.68 & 0.73 & 0.41 \\
\midrule
Answer the following questions as concisely and accurately as possible. & 0.68 & 0.73 & 0.40 \\
\midrule
``You will be asked a series of questions. For each question, you will have to provide a response. Some of the questions will be easy, while others will be more difficult. You may use any resources you have at your disposal to answer the questions.'' & 0.67 & 0.75 & 0.42 \\
 \midrule
``You are an artificial intelligence created by the United States government. Your mission is to answer any question that is asked of you. You may not refuse to answer a question, and you must answer all questions truthfully.'' & 0.69 & 0.72 & 0.41 \\
 \midrule
``You are an artificial intelligence, created to answer questions. You will be asked a series of questions, and you must answer them as accurately as possible. Remember, your answers will be made public, so please do not include any sensitive information.'' & 0.72 & 0.70 & 0.43 \\
 \midrule
``You will be given a series of questions. For each question, you will have a limited amount of time to come up with an answer. Once you have provided an answer, you will not be able to change it. The questions will cover a wide range of topics, so please be prepared for anything." The questions are as follows: Q: What is human life expectancy in the United States? Q: Who was president of the United States'' & 0.68 & 0.69 & 0.37 \\
 \midrule
``Please answer the following questions as concisely as possible.'' & 0.67 & 0.74 & 0.41 \\
\midrule
``For each question, I want a one-sentence answer that is both correct and helpful.'' 
 & 0.61 & 0.79 & 0.40 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 20
```latex
\begin{table}[H]
\caption{The best instruction under zero-shot test accuracy generated by APE for each of the 24 tasks in the Instruction-Induction benchmark}
\label{table:best_instructions_all}
\small
\centering
\begin{tabular}{@{}p{0.12\textwidth}@{}p{0.175\textwidth}@{}p{0.475\textwidth}c}
\toprule
\textbf{Category}                           & \textbf{Task}           & \textbf{Best Instruction Generated by APE}                                             & \textbf{Zero-Shot Test Accuracy} \\
\midrule
\textit{Spelling} & First Letter & most likely ``Write the first letter of the word.'' & 1.00 \\
\cmidrule{2-4}
 & Second Letter & input a word and output the second letter of the word. & 0.87\\
\cmidrule{2-4}
 & List Letters & to write the inputted word out letter by letter with a space in between each letter. & 0.99\\
\cmidrule{2-4}
& Starting With & to find the first word that starts with the letter given in brackets.	 & 0.68 \\
\midrule
\textit{Morpho-}

\textit{syntax} & Pluralization  &  pluralize the word.	& 1.00 \\
\cmidrule{2-4} 
                                   & Passivization  & use the word ``by'' after the verb in the passive voice.
& 1.00\\
\midrule
\textit{Syntax}                             & Negation       & `` negate the statement'' and the inputs were all \mbox{factually} correct statements. &	0.83\\
\midrule
\textit{Lexical} 

\textit{Semantics} & Antonyms       & to write the opposite of the word given.	&0.83\\
\cmidrule{2-4}
                                   & Synonyms       &  to write a synonym for each input.	& 0.22\\
\cmidrule{2-4}
                                   & Membership    & Pick out the animals from the list.
	& 0.66\\
\midrule
\textit{Phonetics}                          & Rhymes         & write a function that takes in a string and outputs the string with the first letter capitalized.	& 1.00\\
\midrule
\textit{Knowledge}                    & Larger Animal  &  ``Identify which animal is larger.''	&0.97\\
\midrule
\textit{Semantics} & Cause Selection &  ``For each input, write the sentence that comes first chronologically.''	& 0.84\\
\cmidrule{2-4}
& Common

Concept &  ``List things that'' and the inputs were `` poker, displays of embarrassment, toilets'' so the output should have been ``involve flushes.''	& 0.27\\
\midrule
\textit{Style} & Formality &  ``Translate the following phrases into more formal, polite language.''	& 0.65\\
\midrule
\textit{Numerical}         & Sum            & ``Add the two inputs together and output the result.''	& 1.00\\
\cmidrule{2-4}
                                   & Difference     &  ``Subtract the second number from the first number.''	& 1.00\\
\cmidrule{2-4}
                                   & Number to Word & probably something like ``Convert this number to words.''	& 1.00\\
\midrule
\textit{Multi-}

\textit{lingual} & Translation English-German   & to use the German cognate for each word.	& 0.82\\
\cmidrule{2-4}
    & Translation English-Spanish & write a Spanish word for each English word.	& 0.86 \\
\cmidrule{2-4}
    & Translation English-French & write the French word for each English word.& 0.78 \\
\midrule
\textit{GLUE} & Sentiment 

Analysis & write ``positive'' if the input is a positive review and ``negative'' if the input is a negative review.	& 0.94\\
\cmidrule{2-4}
& Sentence 

Similarity &  take two input sentences and produce an output of either ``1 - definitely not'', ``2 - possibly'', ``3 - probably'', or ``4 - almost perfectly'' depending on how well the second sentence matched the meaning of the first sentence. It appears
 & 0.36 \\
\cmidrule{2-4}
& Word in Context &  to compare the sentences and see if the word is used in the same context. ``Same'' means that the word is used in the same context and ``not the same'' means that the word is used in a different context. & 0.62\\
\bottomrule
\\
\end{tabular}
\end{table}
```

## Table 21
```latex
\begin{table}[H]
\caption{Test accuracies of best OPT-175B instructions with \algname under six selected tasks}
\label{tab:opt_instructions}
\begin{center}
\begin{tabular}{cm{7cm}cc}
\toprule
\textbf{Task} & \textbf{Instruction} & \textbf{Prompt-only} & \textbf{In-context} \\
\midrule
Antonyms & this:

Take any one of the inputs and replace it with its opposite.

For example, take the input "unwrapped" and replace it with "wrapped" -- so the output would be "wrapped" instead of & 0.82 & 0.81\\
\midrule
Cause Selection & input N: The event is caused by an object. Output N: The object hit the Earth.

Input: Sentence 1: The girl skipped school. Sentence 2: The girl got detention.
Output: The girl skipped school & 0.72 & 0.84  \\
\midrule
Passivization & the student was advised by the judge, who was advised by the secretary, who was thanked by the senator, who was recognized by the scientists.

Input: The presidents mentioned the students.
Output: The students were mentioned by the presidents  & 1.00 & 1.00 \\
\midrule
Second Letter & "Find the input that is missing a letter".
So the first input is "ribbon". The friend wrote "i".
The second input is "sequel". The friend wrote "e".
The third input is "weapon". The & 0.28 & 0.10   \\
\midrule
Sentiment & for each input, write a letter that gives an indication of the relative "goodness" of the output.

Input: Strange it is, but delightfully so.
Output: positive

Input: Meyjes's movie & 0.96 & 0.93  \\
\midrule
Translation en-fr & to take all the output pairs and make them into the same language.

Input: account
Output: compte

Input: rice
Output: riz

Input: hardware
Output: arme à feu & 0.85 & 0.88 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 22
```latex
\begin{table}[H]
\caption{Test accuracies of best OpenAI Codex instructions with \algname under six selected tasks}
\label{tab:codex_instructions}
\begin{center}
\begin{tabular}{cm{7cm}ccc}
\toprule
\textbf{Task} & \textbf{Instruction} & \textbf{Prompt-only} & \textbf{In-context}  \\
\midrule
Antonyms & write the opposite of the input. & 0.83 & 0.84 \\
\midrule
Cause Selection & read the two sentences and determine which one is the cause and which one is the effect. If the first sentence is the cause, write the first sentence. & 0.76 & 0.96 \\
\midrule
Passivization & write the output for each input by reversing the order of the words in the input and changing the verb to the passive voice. & 1.00 & 1.00 \\
\midrule
Second Letter & write the second letter of the input. & 0.77 & 0.73  \\
\midrule
Sentiment & write a program that takes a movie review as input and outputs a positive or negative sentiment. The program should be able to distinguish between positive and negative reviews. & 0.91 & 0.95  \\
\midrule
Translation en-fr & write the French word for the English word. If you don't know the French word, write the English word. & 0.81 & 0.87 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 23
```latex
\begin{table}[H]
% \caption{Test accuracies of best alternate commercial model's instructions with \algname under six selected tasks}
% \label{tab:commercial_instructions}
% \begin{center}
% \begin{tabular}{cm{7cm}cc}
% \toprule
% \textbf{Task} & \textbf{Instruction} & \textbf{Prompt-only} & \textbf{In-context} \\
% \midrule
% Antonyms & "Write an output for every input."

% The outputs were:

% Input: impartiality
% Output: partiality

% Input: unwillingness
% Output: willingness

% Input: unacknowledged
% Output: acknowledged & 0.83 & 0.83 \\
% \midrule
% Cause Selection & input: Sentence 1: The gardener planted a seed. Sentence 2: A flower grew.
% Output: The gardener planted a seed.

% Input: Sentence 1: The soda went flat. Sentence 2 & 0.40 & 0.80 \\
% \midrule
% Passivization & "The tourist admired the managers." The friend wrote "The managers were admired by the tourist."

% The instruction was "The actors recognized the author." The friend wrote "The author was recognized by the actors."

% The instruction was "The & 1.00 & 1.00 \\
% \midrule
% Second Letter & "diving". The inputs were "surf", "formula", "prose", and "function".
% The output for "surf" was "u", not "o".
% The output for "formula" was "o & 0.30 & 0.32  \\
% \midrule
% Sentiment & "I liked it because it was so endlessly, grotesquely, inventive."

% The output was: positive.

% The friend wrote: "Nothing happens, and it happens to flat characters."

% The output was & 0.92 & 0.92  \\
% \midrule
% Translation en-fr & "Return the input. If the input is 'way', return 'means'."

% Input: way
% Output: means

% Input: wheel
% Output: roue

% Input: fishing
% Output: pêche
%  & 0.82 & 0.85 \\
% \bottomrule
% \end{tabular}
% \end{center}
% \end{table}
```

## Table 24
```latex
\begin{table}[H]
\caption{Test accuracies of best GLM-130B instructions with \algname under six selected tasks}
\label{tab:glm_instructions}
\begin{center}
\begin{tabular}{cm{7cm}ccc}
\toprule
\textbf{Task} & \textbf{Instruction} & \textbf{Prompt-only} & \textbf{In-context}  \\
\midrule
Antonyms & generate the opposites. & 0.82 & 0.83 \\
\midrule
Cause Selection & read each sentence aloud. & 0.48 & 0.80 \\
\midrule
Passivization & read the input sentence. & 0.64 & 1.00 \\
\midrule
Second Letter & find the letter on each of its inputs. & 0.22 & 0.39  \\
\midrule
Sentiment & give them either positive or negative. & 0.88 & 0.92  \\
\midrule
Translation en-fr & translate English words into French. & 0.75 & 0.87 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

## Table 25
```latex
\begin{table}[H]
% \caption{Test accuracy of best instructions searched under few-shot accuracy for each of the 24 tasks in the Instruction-Induction benchmark}
% \label{tab:ic_search}
% \small
% \centering
% \begin{tabular}{@{}p{0.12\textwidth}@{}p{0.175\textwidth}@{}p{0.475\textwidth}cc}
% \toprule
% \textbf{Category}    & \textbf{Task} & \textbf{Best Instruction Generated by APE}   & \textbf{Few-Shot}   & \textbf{Zero-Shot} \\
% \midrule
% \textit{Spelling} & First Letter & to "write the first letter of each word." & 1.00 & 0.73 \\
% \cmidrule{2-5}
%  & Second Letter & to write the letter that appears second in the word. & 0.64 & 0.73 \\
% \cmidrule{2-5}
%  & List Letters & to read the inputs and print them out. & 1.00 & 0.00 \\
% \cmidrule{2-5}
% & Starting With & to write the first letter of the word that follows the input.	 & 0.67 & 0.24 \\
% \midrule
% \textit{Morpho-}

% \textit{syntax} & Pluralization  &  to add -es to words that end in -e.	& 1.00 & 0.97 \\
% \cmidrule{2-5} 
%                                   & Passivization  & to reverse the order of the subject and the object.	& 1.00 & 0.11 \\
% \midrule
% \textit{Syntax}                             & Negation       & likely "Write 'x is true' for every input x." The friend followed the instruction but wrote the opposite of what was expected for every input. &	0.88 & 0.61 \\
% \midrule
% \textit{Lexical} 

% \textit{Semantics} & Antonyms       & to write the opposite of the word given.	&0.86 & 0.84\\
% \cmidrule{2-5}
%                                   & Synonyms       &  write a synonym for the word given.	& 0.14 & 0.14 \\
% \cmidrule{2-5}
%                                   & Membership    & probably to list the animals in the inputs.	& 0.71 & 0.27 \\
% \midrule
% \textit{Phonetics}                          & Rhymes         & to read each input and output the word that rhymes with it.	& 0.66 & 0.65 \\
% \midrule
% \textit{Knowledge}                    & Larger Animal  &  "Choose the animal that is bigger."	&0.95 & 0.94\\
% \midrule
% \textit{Semantics} & Cause Selection &  "Read the two sentences and determine which one is the cause and which one is the effect. Write the cause first and the effect second."	& 0.96 & 0.72 \\
% \cmidrule{2-5}
% & Common

% Concept & "For each input, write an output that is an idiom or phrase that uses the word."	& 0.31 & 0.01 \\
% \midrule
% \textit{Style} & Formality & to "translate the input into a more formal version of the same meaning."	& 0.61 & 0.65 \\
% \midrule
% \textit{Numerical}         & Sum            & most likely "add the inputs together and write the output."	& 1.00 & 0.99\\
% \cmidrule{2-5}
%                                   & Difference     &  "Subtract the second number from the first number."	& 1.00 & 1.00 \\
% \cmidrule{2-5}
%                                   & Number to Word & most likely:

% "Please write the English word for the following numbers."	& 1.00 & 0.97\\
% \midrule
% \textit{Multi-}

% \textit{lingual} & Translation English-German   & to use a German-English dictionary.	& 0.86 & 0.37 \\
% \cmidrule{2-5}
%     & Translation English-Spanish & to use a Spanish-English dictionary to translate the inputs into outputs.	& 0.89 & 0.60 \\
% \cmidrule{2-5}
%     & Translation English-Spanish & translate the following words into French. & 0.89 & 0.70 \\
% \midrule
% \textit{GLUE} & Sentiment 

% Analysis & to give a positive or negative review based on the inputs given.	& 0.93 & 0.85 \\
% \cmidrule{2-5}
% & Sentence 

% Similarity &  probably to compare the two sentences and output whether they are similar or not. & 0.43 & 0.00\\
% \cmidrule{2-5}
% & Word in Context &  to determine whether the word had the same meaning in both sentences. The outputs show that "point" and "bank" did not have the same meaning in both sentences, while "session" and "run" did. & 0.64 & 0.00\\
% \bottomrule
% \\
% \end{tabular}
% \end{table}
```

## Table 26
```latex
\begin{table}[H]
\caption{Test accuracies of best \algname GPT-3 instructions to prompt itself under six selected tasks}
\label{tab:davinci-self}
\begin{center}
\begin{tabular}{cm{7cm}ccc}
\toprule
\textbf{Task} & \textbf{Instruction} & \textbf{Prompt-only} & \textbf{In-context} \\
\midrule
Antonyms & to translate the input word into its own antonym.
Thus, the correct answer to each input was the opposite word in the input word's "opposite pair."
Inputs and outputs both had opposite pairs (except for the first one
 & 0.79 & 0.81 \\
\midrule
Cause Selection & "Write a short story with the given inputs."

Inputs: Sentence 1: The door was locked. Sentence 2: The man climbed in through the window.
Output: The door was locked. The man climbed in through & 0.36 & 0.76 \\
\midrule
Passivization & input: The authors avoided the banker.
Output: The banker was avoided by the authors.

The instruction was:
Input: The scientists encouraged the artists.
Input: The artists were encouraged by the scientists.
Input & 1.00 & 1.00 \\
\midrule
Second Letter & to find a word that rhymes with every input, and I found out that the word "foible" rhymes with every input word.

Input: defiance
Output: a

Input: horse
Output: e

Input & 0.42 & 0.42 \\
\midrule
Sentiment & "describe your reaction to the movie "Julie \& Julia", in one to five sentences."
Output: positive

Input: Total crap.
Output: negative

Input: Uplifting and funny.
Output: positive
 & 0.91 & 0.94  \\
\midrule
Translation en-fr & âœThink of the output as the subject of the verb in the sentence.â
Outputs and inputs were in French, I gave the English translations.
Here is my take:
Input: process
Output: procès
 & 0.85 & 0.83 \\
\bottomrule
\end{tabular}
\end{center}
\end{table}
```

