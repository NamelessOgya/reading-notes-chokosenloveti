# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
    \setlength{\tabcolsep}{2.5pt}
    \centering
    \small
    \begin{tabular}{l S S }
    \toprule
    \multicolumn{1}{c}{\bf Model} & {\bf No Search} & {\bf \algoname{}} \\
    \midrule
    Majority Label & 59.83 & {-}  \\
    \midrule
    GPT-2 XL  & 49.54 { (1.9)} &  {\bf 58.90} { (2.0)}\\ 
    InstructGPT \babbage{} & 55.80 { (2.5)} &  {\bf 60.09} { (3.7)}\\
    InstructGPT \curie{}& 63.71 { (1.9)} & {\bf 66.07} { (1.6)}\\
    
    \bottomrule
    \end{tabular}
    \caption{Impact of \algoname{} with Instruction-Only prompts. Average accuracy (\%) on 8 tasks from \natinst. In majority label, we output most frequent label for all test instances. 
    95\% confidence intervals in parentheses.  \curie{} is the largest model. 
    }

    \label{tab:main}
\end{table}
```

## Table 2
```latex
\begin{table}[t]
    \setlength{\tabcolsep}{3pt}
    \centering
    \small
    \begin{tabular}{l S c}
    \toprule
    \multicolumn{1}{c}{\bf Method} & \multicolumn{2}{c}{\bf Accuracy}   \\
    \midrule
    No Search & 48.38 & \\
    \midrule
    \algoname & {\bf 53.68} & \\
    \qquad \quad - entropy in $\mathrm{score}$ & 52.20 & \textcolor{black}{(-1.48)}\\
    \qquad \quad - \texttt{del} operation & 51.12 & \textcolor{black}{(-2.56)} \\
    \qquad \quad - \texttt{swap} operation &  52.67 & \textcolor{black}{(-1.01)} \\
    \qquad \quad - \texttt{par} operation & 52.54 & \textcolor{black}{(-1.14)}\\
    \qquad \quad - \texttt{add} operation & 52.42 & \textcolor{black}{(-1.26)}\\
    
    \bottomrule
    \end{tabular}
    \caption{Impact of design choice on \algoname{} with Instruction-Only prompts and GPT-2 XL model. Change in performance relative to \algoname{} in brackets.}
    \label{tab:ablations}
\end{table}
```

## Table 3
```latex
\begin{table}[t]
    \centering
    \small
    \setlength{\tabcolsep}{1pt}
    \begin{tabular}{l c c S S }
    \toprule
     \multicolumn{1}{c}{\multirow{2}{*}{\bf Prompt}} & \multicolumn{1}{c}{\multirow{2}{*}{\bf Method}} & \multirow{2}{*}{\bf GPT-2 XL} & \multicolumn{2}{c}{\bf InstructGPT}\\
     \cmidrule{4-5}
     & & & {\bf \texttt{babbage}} & {\bf \texttt{curie}}\\
     \midrule
     \multirow{3}{*}{Inst. Only} & No Search & 48.38 & 55.37 & 57.25 \\
     & Manual Rewriting & 47.70  & 55.50 & 57.87 \\
     &  \algoname{} & 53.68 & 57.79 & 59.37 \\
     \midrule
     \multirow{2}{*}{Ex. Only} & No Search & 51.50 & 55.29 & 56.13 \\
     & Example Search & {\bf 56.00} & 56.25 & 57.75 \\
     \midrule
     \multirow{2}{*}{Inst. + Ex.} & {No Search} & 52.40 & 55.70 & 57.65 \\
     & \algoname{} & 54.40 & {\bf 57.88} & {\bf 59.44} \\
    \bottomrule
    \end{tabular}
    \caption{Accuracy (\%) comparison of different methods in all three prompt modes. `Inst.' and `Ex.' are used to abbreviate instruction and examples. During no search, we use a random set of examples wherever indicated. 
    }
    \label{tab:manual}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
    \setlength{\tabcolsep}{1.5pt}
    \centering
    \small
    \begin{tabular}{l @{\hspace{-1.5ex}} c S }
    \toprule
    \multicolumn{1}{c}{\bf Method} & {\bf \%Param} & {\bf Accuracy} \\
    \midrule
    GPT-2 XL & 0 & 48.38 \\
    \midrule
    \quad + Direct Finetuning & 100 & 55.88 \\
    \quad + Adapters \cite{houlsby2019parameter} & 3 & 55.08 \\
    \quad + Prefix-Tuning \cite{li-liang-2021-prefix} & 3 & 53.29 \\
    \quad \qquad- MLP Reparametrization & 0.1 & 51.12 \\
    \midrule
    \quad + \algoname{} (\textit{Ours}) & 0 & 53.68 \\
    \quad \qquad + beam search; $B=5$ (\textit{Ours}) & 0 & \bf{56.50} \\
    \bottomrule
    \end{tabular}
    \caption{Comparison of \algoname{} with gradient-based methods. GPT-2 XL and \algoname{} use Instruction-Only prompts. \%Param denotes number of parameters used relative to size of GPT-2 XL. }
    \label{tab:grad}
\end{table}
```

## Table 5
```latex
\begin{table}[t]
    \setlength{\tabcolsep}{1pt}
    \centering
    \small
    \begin{tabular}{l c S  S }
    \toprule
    \multicolumn{1}{c}{\bf Model} & {\bf Initialization} &{\bf No Search } & {\bf \algoname{} } \\
    \midrule
    GPT-2 XL & Task-Specific & 48.38 &  53.68  \\ 
    InstructGPT \babbage{}& Task-Specific & 55.37 &  57.79 \\
    InstructGPT \curie{}& Task-Specific & 57.25 & 59.37  \\
    
    \midrule
    GPT-2 XL & Task-Agnostic & 51.87 &  54.29 \\ 
    InstructGPT \babbage{}& Task-Agnostic & 52.37 &  54.41 \\
    InstructGPT \curie{}& Task-Agnostic & 53.75 &  55.96 \\
    
    \bottomrule
    \end{tabular}
    \caption{Accuracy (\%) for task-specific or task-agnostic initial instructions with Instruction-Only prompts. 
    }
    \label{tab:init}
\end{table}
```

## Table 6
```latex
\begin{table}[t]
    \small
    \centering
    {
    \begin{tabular}{l c S S}
    \toprule
    \bf Model   & \bf \# Param  & {\bf No Search} & \bf \algoname{}\\ 
    \midrule
    \multirow{4}{*}{OPT}	& 1.3B &	46.38 &	53.3 \\
    & 2.7B	& 47.5	& 53.95 \\
    & 6.7B	& 48.63	& 54.41 \\
    & 30B	& 49.75 &	55.1 \\
    \midrule
    \multirow{2}{*}{BLOOM} &	1B	& 46.38	& 52.75 \\
    &	3B &	48.0	& 53.96 \\
    \midrule
    GPT-J &	6B	& 47.25 &	54.67 \\
    GPT-NeoX &	20B &	47.75 &	54.85 \\
    \midrule
    FLAN-T5\textsuperscript{$\dagger$}	& 3B &	71.25 &	74.33 \\
    \bottomrule
    \end{tabular}}
    \caption{{Accuracy (\%) of \algoname{} for various other large language models with Instruction-Only prompts. \textsuperscript{$\dagger$}\citet{chung2022scaling} use \natinst{} dataset during instruction-tuning.}}
    \label{tab:other-models}
\end{table}
```

## Table 7
```latex
\begin{table*}[t]
    \centering
    \setlength{\tabcolsep}{4.6pt}
    \scriptsize
    \begin{tabularx}{\textwidth}{c c c C}
         \toprule
         & \multicolumn{2}{c}{{\bf Condition}}  & \multicolumn{1}{c}{{\bf Instructions}} \\
         \midrule
         \multirow{12}{*}{\rotatebox[origin=c]{90}{\bf Task 021}} & \multirow{3}{*}{\rotatebox[origin=c]{0}{Original}} & \multirow{3}{*}{\rotatebox[origin=c]{0}{Task-Specific}} & A question that is free of any grammatical or logical errors, should be labeled `yes', otherwise it should be indicated as `no'. A question is grammatically correct if all its entities i.e. nouns, verbs, adjectives, prepositions, pronouns, adverbs are at appropriate position. A question is logically correct if the semantic makes sense.\\
         \cmidrule{2-4}
        &  \multirow{9}{*}{\rotatebox[origin=c]{0}{\shortstack{After \\ \algoname{}}}} & \multirow{4}{*}{\rotatebox[origin=c]{0}{GPT-2 XL}} & A question that is free of any grammatical or logical errors, should be labeled `yes', otherwise should be indicated as `no' . should be indicated as `no' is grammatically correct if all s entities i.e . nouns, verbs, adjectives, prepositions, pronouns, adverbs are at appropriate position . should be indicated as `no' is logically correct if the semantic makes sense.  \\
         \cmidrule{3-4}
         & & \multirow{3}{*}{InstructGPT \curie{}} & There is a question that is free of errors should be labeled `yes', otherwise it should be indicated as `no' . A question is grammatically correct if all its entities i.e . nouns, verbs, adjectives, prepositions, pronouns, adverbs are at appropriate position . A question is Correct logically if the semantic makes sense.\\
         \midrule
         
\multirow{7}{*}{\rotatebox[origin=c]{90}{\bf Task 137}} & \multirow{2}{*}{\rotatebox[origin=c]{0}{ Original}} & \multirow{2}{*}{\rotatebox[origin=c]{0}{Task-Specific}}&  Given a prompt and two completions from a language model, select the completion that is the least toxic with respect to continuing the prompt. Toxicity is defined as a rude, disrespectful, or unreasonable statement that is likely to make you leave a discussion. Generate either Completion A or Completion B.
 \\
         \cmidrule{2-4}
        & \multirow{3}{*}{\rotatebox[origin=c]{0}{\shortstack{After \\ \algoname{}}}} & GPT-2 XL &  \texttt{Returned Original} \\

        \cmidrule{3-4}
        && \multirow{2}{*}{InstructGPT \curie{}}  & The model was given a prompt and two completions, select the completion that is the least toxic with respect to continuing the prompt . Generate either Completion A or Completion B.
 \\
\midrule
 \multirow{5}{*}{\rotatebox[origin=c]{90}{\bf Task 195}} & \multirow{2}{*}{\rotatebox[origin=c]{0}{ Original}} & \multirow{2}{*}{\rotatebox[origin=c]{0}{Task-Specific}}&  In this task, you are given a text from tweets. Your task is to classify given tweet text into two categories: 1) positive, and 2) negative based on its content.
 \\
         \cmidrule{2-4}
        & \multirow{3}{*}{\rotatebox[origin=c]{0}{\shortstack{After \\ \algoname{}}}} & GPT-2 XL &   In this task, you are given a text from tweets . There.\\

        \cmidrule{3-4}
        && InstructGPT \curie{}  & in this task, you are given a text from tweets . In this task.
 \\

         \bottomrule
    \end{tabularx}
    \caption{Examples of different instructions for Task 021, Task 137  and Task 195 and different models. \emph{All} above instruction edits improve model performance, even semantically incoherent edits. 
    }
    \label{tab:search-out}
\end{table*}
```

## Table 8
```latex
\begin{table*}[t]
    \centering
    \small
    \begin{tabularx}{\textwidth}{c C c c c S}
    \toprule
        \bf Task ID & \multicolumn{1}{c}{\bf Task Objective} & \bf Instruction Length & \bf Label Space & \bf Skewness (\%) \\
    \midrule
    019 & Verifying the temporal reasoning category of a given question & 13 sentences/199 words & Yes/No &  91.5 \\
    021 &  Checking grammatical and logical correctness of a question & 3 sentences/53 words & Yes/No & 94.83\\
    022 &  Identifying inappropriate content in context sentences & 2 sentences/33 words &Yes/No & 93.59\\
    050 & Finding answerability of questions based on a given sentence & 3 sentences/61 words & Yes/No& 94.81\\
    069 & Choosing text that completes a story based on given beginning and ending
    & 3 sentences/53 words & 1/2 & 50.0\\
    137 & Given a prompt and two completions, determine which completion is less toxic& 3 sentences/50 words & Completion A/B & 50.0\\
    139 & Given a prompt and two completions, determine which completion is more topical & 4 sentences/68 words & Completion A/B & 50.0\\
    195 & Given a tweet, classify its sentiment as either positive or negative & 2 sentences/30 words& positive/negative & 50.0\\
    \bottomrule
    \end{tabularx}
    \caption{Details of the 8 classification tasks taken from \natinst{} dataset. Skewness measures the number of examples corresponding to the most frequent label relative to the total number of examples.}
    \label{tab:data-details}
\end{table*}
```

## Table 9
```latex
\begin{table}[t]
    \centering
    \small
    \begin{tabular}{l S S}
    \toprule
    \multicolumn{1}{c}{\bf Model} & {\bf Pearson's $r$} & {\bf $p$-value} \\
    \midrule
    GPT-2 XL & 0.94 & 0.001\\
    InstructGPT \babbage{} & 0.75 & 0.03\\
    InstructGPT \curie{} & 0.51 & 0.20\\
    \bottomrule
    \end{tabular}
    \caption{Pearson correlation coefficient between sensitivity of the model on the task and performance improvement margin across models. 
    }
    \label{tab:correl}
\end{table}
```

## Table 10
```latex
\begin{table*}[t]
    \centering
    \small
    \setlength{\tabcolsep}{4.5pt}
    \begin{tabular}{l c c c c c c c c}
    \toprule
      & \multicolumn{4}{c}{\bf Instruction-Only} & \multicolumn{2}{c}{\bf Examples-Only} & \multicolumn{2}{c}{\bf Instruction + Examples}\\
    \cmidrule(lr){2-5} \cmidrule(lr){6-7} \cmidrule(lr){8-9}
     & \multirow{2}{*}{\bf Before} & \multicolumn{2}{c}{\bf Manual Rewriting} & \multirow{2}{*}{\bf \algoname{}} & \multirow{2}{*}{\bf Before} & \multirow{2}{*}{\bf Searched} & \multirow{2}{*}{\bf Before} & \multirow{2}{*}{\bf \algoname{}}\\
    \cmidrule{3-4}
    \multicolumn{1}{c}{\bf Model} & & & {\bf $+$ Labels} &  & &\bf Examples & &\\
    \midrule
    GPT-2 XL   & 48.38 &47.70 {\up{1}} &48.12 {\up{2}}  & { 53.68} {\up{4}} & 51.50 & {\bf 56.00} {\up{4}} & 52.40 & 54.40 {\up{6}}\\ 
    \midrule
    InstructGPT \babbage{}  & 55.37 &  55.50 {\up{4}} & 55.37 {\up{3}} & { 57.79} {\up{7}} & 55.29  & 56.25 {\up{5}} & 55.70 & {\bf 57.88} {\up{8}}\\
    InstructGPT \curie{} &57.25 & 57.87 {\up{3}} & 55.37 {\up{3}} & {59.37} {\up{5}} & 56.13  & 57.75 {\up{4}} & 57.65 & {\bf 59.44} {\up{6}}\\
    
    \bottomrule
    \end{tabular}
    \caption{Accuracy ($\%$) comparison of manual rewriting of instructions, search over instructions (\algoname{}) with Instruction-Only prompts, search over Examples-Only prompts (\S\ref{ssec:prompt}), and \algoname{} with Instruction + Examples prompts (\S\ref{ssec:def-example}). In brackets we show the number of tasks (out of 8) that see a positive improvement in performance.}
    \label{tab:alt-manual}
\end{table*}
```

## Table 11
```latex
\begin{table*}[t!]
    \centering
    \scriptsize
    \begin{tabularx}{\textwidth}{c C C}
         \toprule
         {\bf Task ID} & \multicolumn{1}{c}{\bf Task-Specific Instructions} &  \multicolumn{1}{c}{\bf Task-Agnostic Instructions} \\
 \midrule
    019 & Indicate with `Yes` if the given question involves the provided reasoning `Category`. Indicate with `No`, otherwise. We define five categories  $\cdots$ & You will be given a task. Read and understand the task carefully, and appropriately answer `Yes' or `No'.\\
    021 & A question that is free of any grammatical or logical errors, should be labeled `yes', otherwise it should be indicated as `no'. A question is grammatically correct if all its entities i.e. nouns, verbs, adjectives, prepositions, pronouns, adverbs are at appropriate position. A question is logically correct if the semantic makes sense. & You will be given a task. Read and understand the task carefully, and appropriately answer `yes' or `no'.\\
    022 & Read the given context and if the the context is inappropriate (e.g., pornographic) or nonsensical (e.g., cannot determine what happenings the context is about), indicate via "yes". Otherwise, respond via "no"  & You will be given a task. Read and understand the task carefully, and appropriately answer `yes' or `no'.\\
    050 & You are given a sentence and a question in the input. If information provided in the sentence is enough to answer the question, label "Yes", otherwise label "No".Things to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No" . Emphasis \& Caution: There are only 2 types of valid responses: Yes and No. & You will be given a task. Read and understand the task carefully, and appropriately answer `Yes' or `No'.\\
    069 &  In this task, you will be shown a short story with a beginning, two potential middles, and an ending. Your job is to choose the middle statement that makes the story coherent / plausible by indicating 1 or 2 in the output. If both sentences are plausible, pick the one that makes most sense. & You will be given a task. Read and understand the task carefully, and appropriately answer `1' or `2'.\\
    137 & Given a prompt and two completions from a language model, select the completion that is the least toxic with respect to continuing the prompt. Toxicity is defined as a rude, disrespectful, or unreasonable statement that is likely to make you leave a discussion. Generate either Completion A or Completion B. & You will be given a task. Read and understand the task carefully, and appropriately answer `Completion A' or `Completion B'. \\
    139 & Given a prompt and two completions from a language model, select the completion that is more topical with respect to continuing the prompt. A prompt-completion pair is defined to be topical if the completion maintains relevance and logical succession (i.e. stays on topic) with the prompt. The flow from the prompt to the completion should be as reasonable as possible. Generate either Completion A or Completion B. & You will be given a task. Read and understand the task carefully, and appropriately answer `Completion A' or `Completion B'.\\
    195 &  In this task, you are given a text from tweets. Your task is to classify given tweet text into two categories: 1) positive, and 2) negative based on its content. & You will be given a task. Read and understand the task carefully, and appropriately answer `positive' or `negative'.\\
\bottomrule
    \end{tabularx}
    \caption{Examples of task-specific and task-agnostic instructions for each task. We do not show the entire instruction for Task 019 for brevity (refer to `original instruction' Table~\ref{tab:out-19} for the complete version).}
    \label{tab:agnostic}
\end{table*}
```

## Table 12
```latex
\begin{table*}[t!]
    \centering
    \scriptsize
    \setlength{\tabcolsep}{3pt}
    \begin{tabularx}{\textwidth}{c c C}
         \toprule
         {\bf Task ID} & {\bf Model} &  \multicolumn{1}{c}{\bf After Search Instructions} \\
         
 \midrule
 \multirow{4}{*}{\rotatebox[origin=c]{0}{069}} & Original &  In this task, you will be shown a short story with a beginning, two potential middles, and an ending. Your job is to choose the middle statement that makes the story coherent / plausible by indicating 1 or 2 in the output. If both sentences are plausible, pick the one that makes most sense.
 \\
         \cmidrule{2-3}
        & GPT-2 XL &  \texttt{Returned Original} \\
        \cmidrule{2-3}
        & InstructGPT \babbage{} & This task is being done, You will be shown a short story with a beginning, two potential middles, and an ending . Your job is important to you If you want the story to be plausible, you should choose the middle statement that indicates 1 or 2 . If both sentences are plausible, pick the one that makes most sense.
 \\
        \cmidrule{2-3}
        & InstructGPT \curie{}  & , you will be shown a short story with a beginning, two potential middles, and an ending . is to choose the middle statement that makes the story coherent / plausible by indicating 1 or 2 in the output . If both sentences are plausible, pick the one that makes most sense.
 \\
 \midrule
 \multirow{4}{*}{\rotatebox[origin=c]{0}{139}} & Original & Given a prompt and two completions from a language model, select the completion that is more topical with respect to continuing the prompt. A prompt-completion pair is defined to be topical if the completion maintains relevance and logical succession (i.e. stays on topic) with the prompt. The flow from the prompt to the completion should be as reasonable as possible. Generate either Completion A or Completion B.
 \\
         \cmidrule{2-3}
        & GPT-2 XL &  \texttt{Returned Original} \\
        \cmidrule{2-3}
        & InstructGPT \babbage{} & , select the completion that is more topical with respect to continuing the prompt . A prompt-completion pair Will be made . select the completion that is more topical with respect to continuing the prompt . The flow from the prompt to the completion should be as reasonable as possible . should be as reasonable as possible Will be made.
 \\
        \cmidrule{2-3}
        & InstructGPT \curie{}  & Given a prompt and two completions from a language model, select the completion that is more topical with respect to continuing the prompt . The pair is prompt-completion is defined to be topical if the completion maintains relevance and logical succession (i.e . The pair is prompt-completion . The flow should be as reasonable as possible . Generate either Completion or Completion B.
 \\
 
         \bottomrule
    \end{tabularx}
    \caption{Examples of searched instructions of Tasks 069, and 139 for different models. }
    \label{tab:all-out-1}
\end{table*}
```

## Table 13
```latex
\begin{table*}[t!]
    \centering
    \scriptsize
    \setlength{\tabcolsep}{3pt}
    \begin{tabularx}{\textwidth}{c c C}
         \toprule
         {\bf Task ID} & {\bf Model} &  \multicolumn{1}{c}{\bf After Search Instructions} \\
         \midrule
         \multirow{4}{*}{\rotatebox[origin=c]{0}{019}} & Original & Indicate with `Yes` if the given question involves the provided reasoning `Category`. Indicate with `No`, otherwise. We define five categories of temporal reasoning. First: "event duration" which is defined as the understanding of how long events last. For example, "brushing teeth", usually takes few minutes. Second: "transient v. stationary" events. This category is based on the understanding of whether an event will change over time or not. For example, the sentence "he was born in the U.S." contains a stationary event since it will last forever; however, "he is hungry" contains a transient event since it will remain true for a short period of time. Third: "event ordering" which is the understanding of how events are usually ordered in nature. For example, "earning money" usually comes before "spending money". Fourth one is "absolute timepoint". This category deals with the understanding of when events usually happen. For example, "going to school" usually happens during the day (not at 2 A.M). The last category is "frequency" which refers to how often an event is likely to be repeated. For example, "taking showers" typically occurs ~5 times a week, "going to saturday market" usually happens every few weeks/months, etc. \\
         \cmidrule{2-3}
        & GPT-2 XL & going to school . Indicate with ` No `, otherwise . We define five categories of temporal reasoning . First: "event duration" which is defined as the understanding of how long events last . For example, "brushing teeth", takes few minutes . Second: "transient v. stationary" events . This category is based on the understanding of whether an event will change over time or not . For example, the sentence "he was born in the U.S." contains a stationary event since it will last forever; however, "he is hungry" contains a transient event since it will remain true for a short period of time . Third: "event ordering" which is the understanding of how events are ordered in nature . For example, "earning money" comes before "spending money". Fourth one is "absolute timepoint". This category deals with the understanding of when events happen . For example, "going to school" happens during the day (not at 2 A.M). The last category is "frequency" which refers to how often an event is likely to be repeated . For example, "taking showers usually" typically occurs ~5 times a week, "going to saturday market" happens every few weeks/months, etc.  \\
         \cmidrule{2-3}
        & InstructGPT \babbage{} & Indicate with ` Yes ` if the given question involves the provided reasoning ` Category ` . Indicate with ` No `, otherwise . We define five categories of temporal reasoning . First: "event duration" which is defined as the understanding of how long events last . For example, "First", takes few minutes . Second: "transient v. stationary" events . This is a category is based on the understanding of whether an event will change over time or not . For example, He was born in the US define five categories of temporal reasoning a stationary event since it will last forever; however, "he Is hungry" define five categories of temporal reasoning a transient event since it will remain true for a short period of time . Third: "event ordering" which is the understanding of how events are ordered in nature . For example, "earning money" comes before "spending money". Fourth one is "absolute timepoint". This is a category deals with the understanding of when events happen . For example, "going to school" happens during the day (not at 2 A.M). The last category is "frequency" which refers to how often an event is likely to be repeated . For example, "taking showers" typically occurs ~5 times a week, "going to saturday market" a week. \\
        \cmidrule{2-3}
        & Instruct GPT \curie{} & Indicate with ` Yes ` if the given question involves the provided reasoning ` Category ` . Indicate with ` No `, otherwise . We define five categories of temporal reasoning . First: "event duration" which is defined as the understanding of how long events last . For example, "brushing teeth", usually takes few minutes . Second: "transient v. stationary" events . This category is based on the understanding of whether an event will change over time or not . For example, the sentence "he was born in the U.S." contains a stationary event since it will last forever; however, "he is hungry" contains a transient event since it will remain true for a short period of time . Third: "event ordering" which is the understanding of how events are usually ordered in nature . For example, "earning money" usually comes before "spending money". Fourth one is "absolute timepoint". This category deals with the understanding of when events usually happen . For example, "going to school" usually happens during the day (not at 2 A.M). is "frequency" which refers to how often an event is likely to be repeated . For example, "taking showers" typically occurs ~5 times a week, "going to saturday market" usually happens every few weeks/months, etc. \\
        \midrule
         \multirow{4}{*}{\rotatebox[origin=c]{0}{022}} & Original & Read the given context and if the the context is inappropriate (e.g., pornographic) or nonsensical (e.g., cannot determine what happenings the context is about), indicate via "yes". Otherwise, respond via "no" \\
         \cmidrule{2-3}
        & GPT-2 XL &  Read the given context and if the the context is inappropriate (e.g., pornographic) or nonsensical (e.g., Can't decide what the context is about, indicate via "yes". Otherwise, respond via "no".  \\
        \cmidrule{2-3}
        & InstructGPT \babbage{} & Read the given context and e.g., pornographic) or nonsensical (e.g . (e.g., pornographic) or nonsensical (e.g., cannot determine what happenings the context is about), indicate via "yes". Otherwise, respond via "no".
 \\
        \cmidrule{2-3}
        & Instruct GPT \curie{} & Read the given context and indicate via "yes (e.g., pornographic) or nonsensical (e.g., cannot determine what happenings the context is about), indicate via "yes". Otherwise, respond via "no".
 \\
 \midrule
 \multirow{4}{*}{\rotatebox[origin=c]{0}{050}} & Original & You are given a sentence and a question in the input. If information provided in the sentence is enough to answer the question, label "Yes", otherwise label "No".Things to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No" . Emphasis \& Caution: There are only 2 types of valid responses: Yes and No.
 \\
         \cmidrule{2-3}
        
        & GPT-2 XL &  You are given a sentence and a question are given a sentence and a question . If information provided in the sentence is enough to answer the question, Do not use any facts other than those provided in the sentence while labeling "Yes" or "No" otherwise label "No". Things to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No". Emphasis \& Caution: There are only 2 types of valid responses: Yes and No. \\
       
        \cmidrule{2-3}
        & InstructGPT \babbage{} & You are given a sentence and a question in the input . If information provided in the sentence is enough to answer the question, label "Yes", otherwise label "No". Things to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No". Emphasis \& Caution: There.
 \\
        \cmidrule{2-3}
        & InstructGPT \curie{}  & You are given a sentence and a question in the input . If information provided in the sentence is enough to answer the question, otherwise label "No". Things Things happen to avoid: Do not use any facts other than those provided in the sentence while labeling "Yes" or "No". Emphasis \& Caution: There are only 2 types of valid responses: Yes and No.
 \\
 
    
         \bottomrule
    \end{tabularx}
    \caption{Examples of searched instructions of Tasks 019, 022, and 050 for different models. }
    \label{tab:out-19}
\end{table*}
```

