# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[!ht]
\setlength{\tabcolsep}{5pt}
\centering
\begin{tabular}{lcccccccc}
\toprule
Model & Params & Ruby & JS & Go & Python & Java & PHP & Avg. \\
\midrule
CodeBERT & 110M $\times$ 6 & 69.3 & 70.6 & 84.0 & 86.8 & 74.8 & 70.6 & 76.0 \\
GraphCodeBERT & 110M $\times$ 6 & 84.1 & 73.2 & 87.9 & 75.7 & 71.1 & 72.5 & 77.4 \\
\texttt{cpt-code} S & 300M & 86.3 & 86.0 & 97.7 & 99.8 & 94.0 & 96.7 & 93.4 \\
\texttt{cpt-code} M & 1.2B & 85.5 & 86.5 & 97.5 & 99.9 & 94.4 & 97.2 & 93.5 \\
\hline
GTE$_\text{base}$ & 110M & 79.6 & 79.4 & 84.2 & 98.8 & 86.8 & 86.8 & 85.9 \\
\bottomrule
\end{tabular}
\caption{
Results on CodeSearchNet~\cite{codesearchnet}.
We compare with CodeBERT~\cite{feng-etal-2020-codebert}, GraphCodeBERT~\cite{guo2021graphcodebert} and \texttt{cpt-code}~\citep{neelakantan2022text}.
This setting requires finding the relevant code block among 1K candidates for a given natural language query.
}
\label{table:code}
\end{table*}
```

## Table 2
```latex
\begin{table*}[!ht]
\centering
% \setlength{\tabcolsep}{7pt}
% \scalebox{0.95}{
\begin{tabular}{lrcccccccc}
\toprule
 & Params & Class. & Clust. & Pair. & Rerank & Retr. & STS & Summ. & Avg \\
\multicolumn{1}{l}{\# of datasets $\rightarrow$} & & 12     & 11     & 3          & 4      & 15    & 10  & 1    & 56  \\ \hline
\multicolumn{9}{l}{\emph{Unsupervised models}}    \\ \hline
\multicolumn{1}{l}{Glove}   & 120M &  57.3   &  27.7 & 70.9  & 43.3  & 21.6 & 61.9 & 28.9  & 42.0 \\
\multicolumn{1}{l}{BERT}    & 110M &   61.7  & 30.1  &  56.3 & 43.4  &  10.6  &  54.4   &  29.8  &  38.3  \\
\multicolumn{1}{l}{SimCSE}   & 110M & 62.5  &  29.0  &  70.3   &  46.5  & 20.3  & 74.3 & 31.2  & 45.5 \\
\multicolumn{1}{l}{E5$_\text{small}$}   & 30M &   67.0  & 41.7  &  78.2   &  53.1  &  40.8  & 68.8  & 25.2  &  54.2  \\
\multicolumn{1}{l}{E5$_\text{base}$}   & 110M &   67.9  & 43.4  &  79.2   &  53.5  &  42.9  & 69.5  & 24.3  &  55.5  \\
\multicolumn{1}{l}{E5$_\text{large}$}  & 330M & 69.0  &  44.3  &  80.3   &  54.4  & 44.2  & 69.9 & 24.8  & 56.4 \\ 
\hline
\multicolumn{1}{l}{GTE$_\text{small}$} & 30M & 71.0 & 44.9 & 82.4 & 57.5 & 43.4 & 77.2 & 30.4 & 58.5 \\
\multicolumn{1}{l}{GTE$_\text{base}$} & 110M & 71.5 & 46.0 & 83.3 & 58.4 & 44.2 & 76.5 & 29.5 & 59.0 \\
\multicolumn{1}{l}{GTE$_\text{large}$} & 330M & 71.8 & 46.4 & 83.3 & 58.8 & 44.6 & 76.3 & 30.1 & 59.3 \\
\hline
\multicolumn{9}{l}{\emph{Supervised models}}  \\
\hline
\multicolumn{1}{l}{SimCSE}  & 110M & 67.3  &  33.4  &  73.7   &  47.5  & 21.8  &  79.1    &  23.3    &  48.7 \\
% \multicolumn{1}{l}{BERT-FT$_\text{base}$}  &  68.7  &  33.9  &  82.6  & 50.5  & 41.5  &  79.2  & 29.0  &  55.2  \\
\multicolumn{1}{l}{Contriever}   & 110M &  66.7  &  41.1  &  82.5  & 53.1  & 41.9   &  76.5   &  30.4    &  56.0   \\
\multicolumn{1}{l}{GTR$_\text{large}$}   & 330M & 67.1    &  41.6   &   85.3   &  55.4  & 47.4  & 78.2 & 29.5  &  58.3   \\
\multicolumn{1}{l}{Sentence-T5$_\text{large}$}   & 330M & 72.3  &  41.7   &  85.0   &  54.0  & 36.7  &  81.8 &  29.6  & 57.1 \\
\multicolumn{1}{l}{E5$_\text{small}$}     & 30M & 71.7 &  39.5  &  85.1  & 54.5  & 46.0  & 80.9  & 31.4 & 58.9 \\
\multicolumn{1}{l}{E5$_\text{base}$}     & 110M &  72.6 &  42.1  &  85.1  & 55.7  & 48.7 & 81.0  & 31.0 & 60.4 \\
\multicolumn{1}{l}{E5$_\text{large}$}     & 330M & 73.1 & 43.3  &  85.9  & 56.5 & 50.0  & 82.1 & 31.0 & 61.4  \\
\multicolumn{1}{l}{InstructOR$_\text{base}$}     & 110M & 72.6 & 42.1 & 85.1 & 55.7 & 48.8 & 81.0 & 31.0 & 60.4 \\
\multicolumn{1}{l}{InstructOR$_\text{large}$}     & 330M & 73.9 & 45.3 & 85.9 & 57.5 & 47.6 & 83.2 & 31.8 & 61.6 \\
\multicolumn{1}{l}{OpenAI$_\text{ada-001}$}   & n.a. & 70.4 & 37.5 & 76.9 & 49.0 & 18.4 & 78.6 & 26.9 & 49.5 \\
\multicolumn{1}{l}{OpenAI$_\text{ada-002}$}   & n.a. & 70.9 & 45.9 & 84.9 & 56.3 & 49.3 & 81.0 & 30.8 & 61.0 \\
\hline
\multicolumn{1}{l}{GTE$_\text{small}$} & 30M & 72.3 & 44.9 & 83.5 & 57.7 & 49.5 & 82.1 & 30.4 & 61.4 \\
\multicolumn{1}{l}{GTE$_\text{base}$}     & 110M & 73.0 & 46.1 & 84.3 & 58.6 & 51.2 & 82.3 & 30.7 & 62.4 \\
\multicolumn{1}{l}{GTE$_\text{large}$}     & 330M & 73.3 & 46.8 & 85.0 & 59.1 & 52.2 & 83.4 & 31.7 & 63.1 \\
\hline
\multicolumn{9}{l}{\emph{Larger models}}        \\ \hline
\multicolumn{1}{l}{InstructOR$_\text{xl}$}   & 1.5B & 73.1 & 44.7 & 86.6 & 57.3 & 49.3 & 83.1 & 32.3 & 61.8 \\
\multicolumn{1}{l}{GTR$_\text{xxl}$}   & 4.5B & 67.4  &  42.4   & 86.1   &  56.7   &  48.5  &  78.4   & 30.6  &  59.0 \\
\multicolumn{1}{l}{Sentence-T5$_\text{xxl}$}   & 4.5B & 73.4   &  43.7  &  85.1    &  56.4  & 42.2  & 82.6  & 30.1  &  59.5 \\
\bottomrule
\end{tabular}
% }
\caption{
Results on the MTEB~\citep{muennighoff-etal-2023-mteb} (56 datasets in English subset).
Compared models include SimCSE~\citep{gao-etal-2021-simcse}, Sentence-T5~\citep{ni-etal-2022-sentence}, GTR~\citep{ni-etal-2022-large}, Contriever~\citep{izacard2022unsupervised}, OpenAI text embedding API~\citep{neelakantan2022text},  E5~\citep{wang2022text} and InstructOR~\citep{INSTRUCTOR}.
Exact parameter amount of OpenAI ada model is not available, but is suspected to be $\sim$300M, comparable to the BERT large size model.
}
\label{tab:mteb}
\end{table*}
```

## Table 3
```latex
\begin{table*}[!ht]
\centering
\setlength{\tabcolsep}{2pt}
% \resizebox{\textwidth}{!}{
\begin{tabular}{lccccccccccc}
\toprule
Dataset & BM25 & SimCSE & Contriever & CPT-S & E5$_\text{small}$ & E5$_{\text{base}}$ & E5$_{\text{large}}$ & GTE$_\text{small}$ & GTE$_\text{base}$ & GTE$_\text{large}$ \\
\midrule
MS MARCO & 22.8 & 9.4 & 20.6 & 19.9 & 25.4 & 26.0 & 26.2 & 31.3 & 31.8 & 31.7 \\
Trec-Covid & 65.6 & 26.2 & 27.4 & 52.9 & 52.0 & 61.0 & 61.8 & 61.8 & 64.0 & 64.8 \\
NFCorpus & 32.5 & 9.9 & 31.7 & 32.0 &  29.3  & 35.8 & 33.7 & 34.9 & 36.2 & 38.1 \\
NQ & 32.9 & 11.7 & 25.4 & - &  37.3  & 39.0 & 41.7 & 32.0 & 35.3 & 34.5 \\
HotpotQA & 60.3 & 19.8 & 48.1 & 51.5 &  46.0  & 52.4 & 52.2 & 49.3 & 50.8 & 49.2 \\
FiQA & 23.6 & 9.8 & 24.5 & 34.1 &  38.3  & 40.0 & 43.2 & 37.0 & 36.9 & 40.6 \\
ArguAna & 31.5 & 38.3 & 37.9 & 38.7 &  42.5  & 42.2 & 44.4 & 41.6 & 41.0 & 41.3 \\
Touche-2020 & 36.7 & 8.9 & 19.3 & 21.0 & 19.9  & 16.9 & 19.8 & 17.7 & 18.2 & 18.5 \\
CQADupStack & 29.9 & 13.2 & 28.4 & - & 35.0  & 35.4 & 38.9 & 38.1 & 39.9 & 39.8 \\
Quora & 78.9 & 78.0 & 83.5 & 68.1 &  85.8  & 85.7 & 86.1 & 86.1 & 85.0 & 84.8 \\
DBPedia & 31.3 & 15.0 & 29.2 & 27.2 & 34.5  & 35.4 & 37.1 & 33.5 & 33.2 & 33.6 \\
Scidocs & 15.8 & 5.5 & 14.9 & - &  19.9  & 21.1 & 21.8 & 21.5 & 22.5 & 22.7 \\
Fever & 75.3 & 21.1 & 68.2 & 57.1 &  62.5  & 63.4 & 68.6 & 71.3 & 72.7 & 70.5 \\
Climate-Fever & 21.3 & 11.8 & 15.5 & 15.8 & 14.5 & 15.4 & 15.7 & 21.4 & 21.0 & 25.4 \\
Scifact & 66.5 & 25.7 & 64.9 & 65.4 & 68.5  & 73.7 & 72.3 & 72.7 & 74.1 & 74.1 \\
\midrule
Average & 41.7 & 20.3 & 36.0 & - & 40.8  & 42.9 & 44.2 & 43.4 & 44.2 & 44.6 \\
\bottomrule
\end{tabular}
% }
\caption{nDCG@$10$ of different unsupervised methods on the BEIR benchmark~\citep{beir}.
SimCSE is based on BERT$_\text{base}$ backbone.
CPT-S~\citep{neelakantan2022text} is of similar size to BERT$_\text{large}$.
Baseline results are borrowed from E5 paper~\citep{wang2022text}.
Note that Contriever uses dot product as the similarity metric while other models uses cosine similarity.
}
\label{tab:beir_unsup_results}
\end{table*}
```

## Table 4
```latex
\begin{table*}[ht]
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{llll}
\hline
Task Type & Text Pair Format & Query & Doc \\
\hline
Web Page & \begin{tabular}[c]{@{}l@{}}(title, body)\end{tabular} & \begin{tabular}[c]{@{}l@{}}Providence Real Estate | Providence Homes for Sale\end{tabular} & \begin{tabular}[c]{@{}l@{}}Founded by Roger Williams in 1636, Providence is \\ recognized as one of the country's oldest cities\ldots\end{tabular} \\
\hline
Academic Paper &  \begin{tabular}[c]{@{}l@{}}(title, abstract)\end{tabular} & \begin{tabular}[c]{@{}l@{}}Polymer Quantum Mechanics and its Continuum Limit\end{tabular} & \begin{tabular}[c]{@{}l@{}}A rather non-standard quantum representation of the 
\\ canonical commutation relations of quantum mechanics\ldots\end{tabular}   \\ \hline
Hyperlink &  \begin{tabular}[c]{@{}l@{}}(citation, reference)\end{tabular} & \begin{tabular}[c]{@{}l@{}}After the championship in 1996, the PGA of America \\ raised its stake to 50\% and announced that \ldots\end{tabular} &  \begin{tabular}[c]{@{}l@{}}Pebble Beach Golf Links The largest margin of victory \\ ever in a major championship, surpassing the 13-shot \ldots\end{tabular} \\ \hline
Social Media & (post, comment) & \begin{tabular}[c]{@{}l@{}}Pretty sure any team with Lebron James will be a playoff \\ contender. Considering UNC would be in the East\ldots \end{tabular} &  \begin{tabular}[c]{@{}l@{}}I was being sarcastic and making fun of the East, but \\ honestly I was really in deep thought about this \ldots \end{tabular} \\
\hline
Knowledge Base & \begin{tabular}[c]{@{}l@{}}(entity, description)\end{tabular}  & \begin{tabular}[c]{@{}l@{}}Animation \end{tabular}   & \begin{tabular}[c]{@{}l@{}}Animation is the process of creating the illusion of motion \\ and shape change by means of the rapid display of \ldots \end{tabular} \\
\hline
Community QA & (question, answer) & \begin{tabular}[c]{@{}l@{}}How the human species evolved? \end{tabular} & \begin{tabular}[c]{@{}l@{}}A tough question as it overlaps science and theology. Since \\ you asked ``how the human species evolved?'' I'll assume \ldots \end{tabular} \\
\hline
News  & \begin{tabular}[c]{@{}l@{}}(summary, content)\end{tabular}  & \begin{tabular}[c]{@{}l@{}}Nepalese Opposition Welcomes Return of Parliament \end{tabular}   &  \begin{tabular}[c]{@{}l@{}}Nepal's opposition alliance formally calls off weeks of \\ pro-democracy protests after King Gyenandra reinstates \ldots \end{tabular} \\ \hline
Code & \begin{tabular}[c]{@{}l@{}}(text, code)\end{tabular} & \begin{tabular}[c]{@{}l@{}}SetMaxRecords sets the MaxRecords field's value. \end{tabular}   & \begin{tabular}[c]{@{}l@{}}func (s *DescribeSnapshotCopyGrantsInput) SetMaxRecords \\(v int64) *DescribeSnapshotCopyGrantsInput \{ s.MaxRecords \end{tabular}  \\ \hline
\end{tabular}
}
\caption{Examples of mined (query, document) pairs in the pre-training data.}
\label{tab:pt_data}
\end{table*}
```

## Table 5
```latex
\begin{table*}[!ht]
\setlength{\tabcolsep}{5pt}
\centering
\begin{tabular}{lcccccccc}
\toprule
Model & Params & Ruby & JS & Go & Python & Java & PHP & Avg. \\
\midrule
CodeBERT & 110M$\times$6 & 67.9 & 62.0 & 88.2 & 67.2 & 67.6 & 62.8 & 69.3 \\
GraphCodeBERT & 110M$\times$6 & 70.3 & 64.4 & 89.7 & 69.2 & 69.1 & 64.9 & 71.3 \\
UniXcoder & 110M$\times$6 & 74.0 & 68.4 & 91.5 & 72.0 & 72.6 & 67.6 & 74.4 \\
CodeRetriever & 110M$\times$6 & 77.1 & 71.9 & 92.4 & 75.8 & 76.5 & 70.8 & 77.4 \\
\midrule
GTE$_\text{base}$ & 110M & 76.1 & 73.6 & 88.1 & 95.9 & 80.1 & 85.3 & 83.2 \\
\bottomrule
\end{tabular}
\caption{
Results on CodeSearchNet.
Comparison on code search across 6 programming languages~\cite{codesearchnet} with CodeBERT~\cite{feng-etal-2020-codebert}, GraphCodeBERT~\cite{guo2021graphcodebert}, UniXcoder~\cite{guo-etal-2022-unixcoder} and CodeRetriever~\cite{li-etal-2022-coderetriever}.
This setting requires finding the corresponding code candidates from all candidates from dev and test set.
}
\label{table:code-full}
\end{table*}
```

## Table 6
```latex
\begin{table*}[ht]
\centering
\resizebox{\textwidth}{!}{
\begin{tabular}{lllll}
\hline
Task Type & Text Triple Format & query & doc & hard neg \\ \hline
Web Search & \begin{tabular}[c]{@{}l@{}}(query, passage, negative)\end{tabular} & \begin{tabular}[c]{@{}l@{}}finger cellulitis symptoms\end{tabular} & \begin{tabular}[c]{@{}l@{}}The following are the most common \\ symptoms of cellulitis. However\ldots\end{tabular} & \begin{tabular}[c]{@{}l@{}}Cellulitis usually begins as \\ a small area of pain and \ldots\end{tabular} \\
\hline
Open QA  & (question, passage, negative) & \begin{tabular}[c]{@{}l@{}}big little lies season 2 \\ how many episodes\end{tabular} & \begin{tabular}[c]{@{}l@{}}Big Little Lies (TV series). \\ series garnered several accolades\ldots\end{tabular} & \begin{tabular}[c]{@{}l@{}}Little People, Big World. \\ final minutes of the season two\ldots\end{tabular} \\
\hline
Natural Language Inference  & (sentence, entailment, contradiction) & \begin{tabular}[c]{@{}l@{}}(Read  for Slate 's take \\ on Jackson's findings.)\end{tabular} & \begin{tabular}[c]{@{}l@{}}Slate had an opinion \\ on Jackson's findings.\end{tabular} & \begin{tabular}[c]{@{}l@{}}Slate did not hold any opinion \\ on Jackson's findings.\end{tabular} \\
\hline
Fact Verification &  \begin{tabular}[c]{@{}l@{}}(argument, evidence, others)\end{tabular}  & \begin{tabular}[c]{@{}l@{}}Roman Atwood is a \\ content creator.\end{tabular}    &  \begin{tabular}[c]{@{}l@{}}Roman Bernard Atwood (born \\ May 28, 1983) is an American \\ YouTube personality\ldots\end{tabular} & \begin{tabular}[c]{@{}l@{}}6th Streamy Awards Casey Neistat \\ and Jesse Wellens, PrankvsPrank \ldots\end{tabular} \\
\hline
Paraphrase &  \begin{tabular}[c]{@{}l@{}}(sentence, paraphrase, others)\end{tabular} & \begin{tabular}[c]{@{}l@{}}Lexapro taken with \\ crestor any reaction? \end{tabular} & \begin{tabular}[c]{@{}l@{}}Can dayquil be taken with Lexapro?\end{tabular} & \begin{tabular}[c]{@{}l@{}}Can stopping lexapro cause \\ a longer period?\end{tabular} \\
\hline
\end{tabular}
}

\caption{Examples of (query, positive, negative) text triples in fine-tuning data.}
\label{tab:ft_data}

\end{table*}
```

## Table 7
```latex
\begin{table}[!ht]
    \centering
    \begin{tabular}{lrcc}
    \toprule
    Model & Params & Prompting & Accuracy \\ \midrule
    E5$_\text{base}$ & 110M & \cmark & 81.3 \\ 
    E5$_\text{large}$ & 330M & \cmark & 85.3 \\
    \texttt{cpt-text} & 6B & & 88.1 \\
    \texttt{cpt-text} & 6B & \cmark & 89.1 \\
    \midrule
    GTE$_\text{base}$ & 110M & & 85.1 \\
    GTE$_\text{base}$ & 110M & \cmark & 87.2 \\
    \bottomrule
    \end{tabular}
    \caption{Zero shot text classification performance on SST-2. All compared models are the fine-tuned ones.}
    \label{tab:zeroshot_sst2}
\end{table}
```

