# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[h]
    \centering
    \caption{Hyperparameters for training F2LLM models.}
    \begin{tabular}{rrrrrr}
    \toprule
    Model & Learning Rate & Global Batch Size & Num. GPUs & Micro Batch Size \\
    \midrule
        0.6B & 1e-5 & 512 & 16 & 32 \\
        1.7B & 9e-6 & 512 & 16 & 32 \\
        4B & 8e-6 & 512 & 32 & 16 \\
    \bottomrule
    \end{tabular}
    \label{tab:hyperparameter}
\end{table}
```

## Table 2
```latex
\begin{table}[ht]
    \centering
    \caption{Instructions for evaluation tasks in MTEB.}
    \adjustbox{width=\textwidth-0.8cm,center}{
    \rowcolors{2}{gray!10}{white}
    \begin{tabular}{m{4cm}m{12cm}}
    \toprule
    Task & Instruction \\
    \midrule
AmazonCounterfactual-Classification & Classify a given Amazon customer review text as either counterfactual or not counterfactual. \\
ArXivHierarchical-ClusteringP2P & Identify the main and secondary category of arXiv papers based on the titles and abstracts. \\
ArXivHierarchical-ClusteringS2S & Identify the main and secondary category of arXiv papers based on the titles. \\
ArguAna & Given a claim, find documents that refute the claim. \\
AskUbuntuDupQuestions & Retrieve duplicate questions from AskUbuntu forum. \\
BIOSSES & Retrieve semantically similar text. \\
Banking77Classification & Given an online banking query, find the corresponding intents. \\
BiorxivClusteringP2P.v2 & Identify the main category of bioRxiv papers based on the titles and abstracts. \\
CQADupstack-GamingRetrieval & Given a question, retrieve questions that are semantically equivalent. \\
CQADupstack-UnixRetrieval & Given a question, retrieve questions that are semantically equivalent. \\
ClimateFEVER-HardNegatives & Given a claim about climate change, retrieve documents that support or refute the claim. \\
FEVERHardNegatives & Given a claim, retrieve documents that support or refute the claim. \\
FiQA2018 & Given a financial question, retrieve passages that answer the question. \\
HotpotQAHardNegatives & Given a multi-hop question, retrieve passages that answer the question. \\
ImdbClassification & Classify the sentiment expressed in the given movie review text from the IMDB dataset. \\
MTOPDomainClassification & Classify the intent domain of the given utterance in task-oriented conversation. \\
MassiveIntentClassification & Given a user utterance as query, find the user intents. \\
MassiveScenario-Classification & Given a user utterance as query, find the user scenarios. \\
MedrxivClusteringP2P.v2 & Identify the main category of medRxiv papers based on the titles and abstracts. \\
MedrxivClusteringS2S.v2 & Identify the main category of medRxiv papers based on the titles. \\
MindSmallReranking & Retrieve relevant news articles based on user browsing history. \\
SCIDOCS & Given a scientific paper title, retrieve paper abstracts that are cited by the given paper. \\
SICK-R & Retrieve semantically similar text. \\
STS12, STS13, STS14, STS15, STS17, STS22.v2, STSBenchmark & Retrieve semantically similar text. \\
SprintDuplicateQuestions & Retrieve duplicate questions from Sprint forum. \\
StackExchange-Clustering.v2 & Identify the topic or theme of StackExchange posts based on the titles. \\
StackExchange-ClusteringP2P.v2 & Identify the topic or theme of StackExchange posts based on the given paragraphs. \\
SummEval-Summarization.v2 & Given a news summary, retrieve other semantically similar summaries. \\
TRECCOVID & Given a query on COVID-19, retrieve documents that answer the query. \\
Touche2020Retrieval.v3 & Given a question, retrieve passages that answer the question. \\
ToxicConversations-Classification & Classify the given comments as either toxic or not toxic. \\
TweetSentimentExtraction-Classification & Classify the sentiment of a given tweet as either positive, negative, or neutral \\
TwentyNewsgroups-Clustering.v2 & Identify the topic or theme of the given news articles. \\
TwitterSemEval2015 & Retrieve tweets that are semantically similar to the given tweet. \\
TwitterURLCorpus & Retrieve tweets that are semantically similar to the given tweet. \\
    \bottomrule
    \end{tabular}
    }
    \label{tab:mteb-instruction}
\end{table}
```

## Table 3
```latex
\begin{table}[ht]
    \centering
    \caption{Instructions for training data of F2LLM.}
    \adjustbox{width=\textwidth-0.8cm,center}{
    \rowcolors{2}{gray!10}{white}
    \begin{tabular}{m{3.5cm}lm{12cm}}
    \toprule
    Dataset & Type & Instruction \\
    \midrule
Arguana, SQuAD, BioASQ, NFCorpus, MIRACL, Mr.TyDi & Retrieval & Given a question, retrieve passages that answer the question.\\
PAQ, StackExchange, MSMARCO, Natural Questions & Retrieval & Given a web search query, retrieve relevant passages that answer the query.\\
SNLI, MNLI, ANLI & Retrieval & Given a premise, retrieve hypotheses that are entailed by the premise.\\
HotpotQA & Retrieval & Given a multi-hop question, retrieve passages that answer the question.\\
FEVER & Retrieval & Given a claim, retrieve documents that support or refute the claim.\\
ELI5 & Retrieval & Given a question from Reddit ELI5 forum, retrieve passages that answer it.\\
FiQA2018 & Retrieval & Given a financial question, retrieve passages that answer the question.\\
SciFact & Retrieval & Given a scientific claim, retrieve passages that support or refute the claim.\\
TriviaQA & Retrieval & Given a trivia question, retrieve passages that can answer it.\\
COLIEE & Retrieval & Given a legal statement, retrieve articles that support it.\\
PubMedQA & Retrieval & Given a question, retrieve paper abstracts from PubMed that can answer it.\\
S2ORC-Title-Abstract & Retrieval & Given a paper's title, retrieve the corresponding abstract.\\
S2ORC-Title-Citation & Retrieval & Given a paper's title, retrieve papers that cite it.\\
S2ORC-Abstract-Citation & Retrieval & Given a paper's abstract, retrieve abstract of papers that cite it.\\
Amazon QA & Retrieval & Given a question about a product, retrieve Amazon reviews that can help answer it.\\
SPECTER & Retrieval & Given a scientific paper title, retrieve paper titles that are cited by the given paper.\\
XSum, CNN\_DM & Retrieval & Given a news summary, retrieve the original news article.\\
Sentence Compression & Retrieval & Given a compressed sentence, retrieve the original sentence before compression.\\
QQP, StackExchange-DupQuestions-S2S, StackExchange-DupQuestions-P2P & Retrieval & Given a question, retrieve questions that are semantically equivalent.\\
StackOverflow-DupQuestions & Retrieval & Retrieve duplicate questions from StackOverflow forum.\\
STS12, STS22, STSBenchmark & Retrieval & Retrieve semantically similar text.\\
Amazon Counterfactual & Classification & Classify a given Amazon customer review text as either counterfactual or not counterfactual.\\
Amazon Polarity & Classification & Classify the given Amazon review into positive or negative sentiment.\\
IMDb & Classification & Classify the sentiment expressed in the given movie review text from the IMDB dataset.\\
Toxic Conversations & Classification & Classify the given comments as either toxic or not toxic.\\
CoLA & Classification & Classify the given sentence as linguistically acceptable or not acceptable.\\
Amazon Reviews & Clustering & Classify the given Amazon review into its appropriate rating category.\\
Banking77 & Clustering & Given an online banking query, find the corresponding intents.\\
Emotion & Clustering & Classify the emotion expressed in the given Twitter message into one of the six emotions: anger, fear, joy, love, sadness, and surprise.\\
MTOP Intent & Clustering & Classify the intent of the given utterance in task-oriented conversation.\\
MTOP Domain & Clustering & Classify the intent domain of the given utterance in task-oriented conversation.\\
Massive Scenario & Clustering & Given a user utterance as query, find the user scenarios.\\
Massive Intent & Clustering & Given a user utterance as query, find the user intents.\\
Tweet Sentiment Extraction & Clustering & Classify the sentiment of a given tweet as either positive, negative, or neutral.\\
Arxiv-Clustering-P2P & Clustering & Identify the main and secondary category of arXiv papers based on the titles and abstracts.\\
Arxiv-Clustering-S2S & Clustering & Identify the main and secondary category of arXiv papers based on the titles.\\
Biorxiv-Clustering-P2P & Clustering & Identify the main category of bioRxiv papers based on the titles and abstracts.\\
Biorxiv-Clustering-S2S & Clustering & Identify the main category of bioRxiv papers based on the titles.\\
Medrxiv-Clustering-P2P & Clustering & Identify the main category of medRxiv papers based on the titles and abstracts.\\
Medrxiv-Clustering-S2S & Clustering & Identify the main category of medRxiv papers based on the titles.\\
Reddit-Clustering-P2P & Clustering & Identify the topic or theme of Reddit posts based on the titles and posts.\\
Reddit-Clustering-S2S & Clustering & Identify the topic or theme of Reddit posts based on the titles.\\
StackExchange-Clustering-P2P & Clustering & Identify the topic or theme of StackExchange posts based on the given paragraphs.\\
StackExchange-Clustering-S2S & Clustering & Identify the topic or theme of StackExchange posts based on the titles.\\
TwentyNewsgroups & Clustering & Identify the topic or theme of the given news articles. \\
    \bottomrule
    \end{tabular}
    }
    \label{tab:training-instruction}
\end{table}
```

## Table 4
```latex
\begin{table}[t]
    \centering
    \caption{Top models on the MTEB leaderboard. ``Average'' column is the micro average of all 41 tasks.}
    \adjustbox{width=\textwidth+0.1cm,center}{
    \begin{tabular}{m{3.9cm}>{\raggedleft\arraybackslash}m{1.2cm}>{\raggedleft\arraybackslash}m{1.3cm}>{\raggedleft\arraybackslash}m{1.3cm}>{\raggedleft\arraybackslash}m{1.3cm}>{\raggedleft\arraybackslash}m{1.3cm}>{\raggedleft\arraybackslash}m{1.3cm}>{\raggedleft\arraybackslash}m{1.3cm}>{\raggedleft\arraybackslash}m{1.3cm}r}
    \toprule
        Model & Classifi-cation & Clustering & PairClassi-fication & Reranking & Retrieval & STS & Summari-zation & \textbf{Average} & \textbf{Rank} \\
    \midrule
        \rowcolor{gray!15}
        \multicolumn{10}{c}{\emph{Closed-source}} \\
        Seed1.5-Embedding & 89.88 & 60.83 & 87.39 & 50.67 & 67.45 & 87.23 & 36.44 & 74.76 & 3 \\
        Seed1.6-Embedding & 92.42 & 59.22 & 85.07 & 50.28 & 64.90 & 86.87 & 37.10 & 74.07 & 6 \\
        Gemini Embedding & 90.05 & 59.39 & 87.70 & 48.60 & 64.35 & 85.29 & 38.28 & 73.30 & 8 \\
    \midrule
        \rowcolor{gray!15}
        \multicolumn{10}{c}{\emph{7-8B}} \\
        QZhou-Embedding 7B & 88.97 & 61.65 & 92.43 & 51.77 & 67.12 & 91.65 & 33.05 & 75.97 & 1 \\
        Qwen3-Embedding 8B & 90.43 & 58.57 & 87.52 & 51.56 & 69.44 & 88.58 & 34.83 & 75.22 & 2 \\
        LGAI-Embedding 7B & 89.97 & 59.25 & 88.67 & 49.13 & 66.18 & 86.69 & 38.93 & 74.12 & 5 \\
        GTE-Qwen2 7B & 88.52 & 58.97 & 85.90 & 50.47 & 58.09 & 82.69 & 35.74 & 70.72 & 11\\
        GeoEmbedding 7B & 89.67 & 56.50 & 82.51 & 48.32 & 60.91 & 80.60 & 30.43 & 70.21 & 13 \\
    \midrule
        \rowcolor{gray!15}
        \multicolumn{10}{c}{\emph{4B}} \\
        Qwen3-Embedding 4B & 89.84 & 57.51 & 87.01 & 50.76 & 68.46 & 88.72 & 34.39 & 74.60 & 4 \\
        F2LLM 4B & 91.68 & 68.54 & 83.75 & 50.05 & 59.63 & 84.20 & 33.19 & 73.67 & 7 \\
    \midrule
        \rowcolor{gray!15}
        \multicolumn{10}{c}{\emph{1-2B}} \\
        F2LLM 1.7B & 90.86 & 64.13 & 83.27 & 49.84 & 57.83 & 83.90 & 29.88 & 72.01 & 9 \\
        Jasper 2B & 90.27 & 60.52 & 88.14 & 50.00 & 56.05 & 84.37 & 37.19 & 71.41 & 10 \\
    \midrule
        \rowcolor{gray!15}
        \multicolumn{10}{c}{\emph{<1B}} \\
        Qwen3-Embedding 0.6B & 85.76 & 54.05 & 84.37 & 48.18 & 61.83 & 86.57 & 33.43 & 70.70 & 12 \\
        F2LLM 0.6B & 90.56 & 60.36 & 81.49 & 47.88 & 55.70 & 82.48 & 24.54 & 70.03 & 14 \\
    \bottomrule
    \end{tabular}
    }
    \label{tab:baseline-results}
\end{table}
```

## Table 5
```latex
\begin{table}[ht]
    \centering
    \caption{Classification and clustering datasets used for training F2LLM. Average query and corpus lengths are measured by the number of Qwen3 tokens, and the length of queries includes instructions.}
    \adjustbox{width=\textwidth-0.0cm,center}{
    \rowcolors{2}{gray!10}{white}
    \begin{tabular}{m{3cm}crr>{\raggedleft\arraybackslash}m{1cm}>{\raggedleft\arraybackslash}m{1cm}m{3cm}m{7cm}}
    \toprule
Dataset & Type & \# Query & Corpus Size & Query Length & Corpus Length & Source & URL \\
    \midrule
Amazon Counterfactual & Classification & 8,663 & 2 & 47 & 4 & \citet{2021Amazon-Counterfactual} & \url{https://huggingface.co/datasets/mteb/amazon_counterfactual} \\
Amazon Polarity & Classification & 100,000 & 2 & 115 & 2 & \citet{2013Amazon-Reviews} & \url{https://huggingface.co/datasets/mteb/amazon_polarity} \\
IMDb & Classification & 24,904 & 2 & 314 & 2 & \citet{2011IMDB} & \url{https://huggingface.co/datasets/mteb/imdb} \\
Toxic Conversations & Classification & 49,900 & 2 & 84 & 3 & \citet{2019Toxic-Conversations} & \url{https://huggingface.co/datasets/mteb/toxic_conversations_50k} \\
CoLA & Classification & 9,571 & 2 & 28 & 2 & \citet{2019CoLA} & \url{https://gluebenchmark.com/tasks} \\
Amazon Reviews & Clustering & 100,000 & 99,966 & 63 & 48 & \citet{2013Amazon-Reviews} & \url{https://huggingface.co/datasets/mteb/amazon_reviews_multi} \\
Banking77 & Clustering & 9,993 & 9,993 & 31 & 15 & \citet{2020Banking77} & \url{https://huggingface.co/datasets/mteb/banking77} \\
Emotion & Clustering & 17,944 & 17,944 & 54 & 21 & \citet{2018Emotion} & \url{https://huggingface.co/datasets/mteb/emotion} \\
MTOP Intent & Clustering & 17,896 & 17,862 & 28 & 9 & \citet{2021MTOP} & \url{https://huggingface.co/datasets/mteb/mtop_intent} \\
MTOP Domain & Clustering & 17,538 & 17,531 & 29 & 10 & \citet{2021MTOP} & \url{https://huggingface.co/datasets/mteb/mtop_domain} \\
Massive Scenario & Clustering & 13,547 & 13,488 & 26 & 8 & \citet{2023MASSIVE} & \url{https://huggingface.co/datasets/mteb/amazon_massive_scenario} \\
Massive Intent & Clustering & 13,547 & 13,488 & 26 & 8 & \citet{2023MASSIVE} & \url{https://huggingface.co/datasets/mteb/amazon_massive_intent} \\
Tweet Sentiment Extraction & Clustering & 26,732 & 26,732 & 40 & 19 & \citet{2020tweet-sentiment-extraction} & \url{https://huggingface.co/datasets/mteb/tweet_sentiment_extraction} \\
Arxiv-Clustering-P2P & Clustering & 83,476 & 299,733 & 245 & 222 & \citet{2022mteb-arxiv} & \url{https://huggingface.co/datasets/mteb/raw_arxiv} \\
Arxiv-Clustering-S2S & Clustering & 83,486 & 299,630 & 38 & 17 & \citet{2022mteb-arxiv} & \url{https://huggingface.co/datasets/mteb/raw_arxiv} \\
Biorxiv-Clustering-P2P & Clustering & 57,296 & 57,215 & 360 & 338 & \citet{2022mteb-biorxiv} & \url{https://huggingface.co/datasets/mteb/raw_biorxiv} \\
Biorxiv-Clustering-S2S & Clustering & 57,296 & 57,204 & 42 & 22 & \citet{2022mteb-biorxiv} & \url{https://huggingface.co/datasets/mteb/raw_biorxiv} \\
Medrxiv-Clustering-P2P & Clustering & 18,659 & 18,653 & 453 & 431 & \citet{2022mteb-medrxiv} & \url{https://huggingface.co/datasets/mteb/raw_medrxiv} \\
Medrxiv-Clustering-S2S & Clustering & 18,659 & 18,652 & 45 & 25 & \citet{2022mteb-medrxiv} & \url{https://huggingface.co/datasets/mteb/raw_medrxiv} \\
Reddit-Clustering-P2P & Clustering & 80,000 & 489,218 & 194 & 175 & \citet{2021Reddit-Clustering-P2P} & \url{https://huggingface.co/datasets/sentence-transformers/reddit-title-body} \\
Reddit-Clustering-S2S & Clustering & 58,141 & 104,725 & 34 & 15 & \citet{2021Reddit-StackExchange-Clustering-S2S} & \url{https://github.com/UKPLab/TWEAC-qa-agent-selection/tree/master/data/reddit/train} \\
StackExchange-Clustering-P2P & Clustering & 80,000 & 430,913 & 304 & 281 & \citet{2021StackExchange-Clustering-P2P} & \url{https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_title_body_jsonl} \\
StackExchange-Clustering-S2S & Clustering & 56,731 & 674,714 & 32 & 13 & \citet{2021Reddit-StackExchange-Clustering-S2S} & \url{https://github.com/UKPLab/TWEAC-qa-agent-selection/tree/master/data/stackexchange/train} \\
TwentyNewsgroups & Clustering & 11,060 & 10,994 & 230 & 216 & \citet{1995TwentyNewsGroups} & \url{https://huggingface.co/datasets/SetFit/20_newsgroups} \\
    \midrule
    \rowcolor{white} Total & Classification & 193,038 & 10 \\
    \rowcolor{white} Total & Clustering & 822,001 & 2,678,655 \\
    \bottomrule
    \end{tabular}
    }
    \label{tab:training-data-classification-clustering}
\end{table}
```

## Table 6
```latex
\begin{table}[ht]
    \centering
    \caption{Retrieval datasets used for training F2LLM. Average query and corpus lengths are measured by the number of Qwen3 tokens, and the length of queries includes instructions.}
    \adjustbox{width=\textwidth-0.0cm,center}{
    \rowcolors{2}{gray!10}{white}
    \begin{tabular}{m{3cm}crr>{\raggedleft\arraybackslash}m{1cm}>{\raggedleft\arraybackslash}m{1cm}m{3cm}m{7cm}}
    \toprule
Dataset & Type & \# Query & Corpus Size & Query Length & Corpus Length & Source & URL \\
    \midrule
Arguana & Retrieval & 22,848 & 8,561 & 25 & 210 & \citet{2018Arguana} & \url{https://huggingface.co/datasets/BeIR/arguana-generated-queries} \\
SNLI & Retrieval & 54,585 & 320,753 & 32 & 10 & \citet{2015SNLI} & \url{https://huggingface.co/datasets/stanfordnlp/snli} \\
MNLI & Retrieval & 112,075 & 358,808 & 42 & 14 & \citet{2018MNLI} & \url{https://huggingface.co/datasets/nyu-mll/multi_nli} \\
ANLI & Retrieval & 18,801 & 104,706 & 95 & 14 & \citet{2020ANLI} & \url{https://huggingface.co/datasets/facebook/anli} \\
PAQ & Retrieval & 938,771 & 2,492,657 & 30 & 145 & \citet{2021PAQ} & \url{https://huggingface.co/datasets/sentence-transformers/paq} \\
SQuAD & Retrieval & 89,509 & 20,951 & 30 & 162 & \citet{2016SQuAD} & \url{https://huggingface.co/datasets/rajpurkar/squad} \\
StackExchange & Retrieval & 754,705 & 2,401,305 & 231 & 245 & \citet{2021StackExchangeDataset} & \url{https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_titlebody_best_voted_answer_jsonl} \\
MSMARCO & Retrieval & 365,503 & 4,472,684 & 26 & 82 & \citet{2016MSMARCO} & \url{https://huggingface.co/datasets/mteb/msmarco} \\
Natural Questions & Retrieval & 97,209 & 75,178 & 30 & 145 & \citet{2019NaturalQuestions} & \url{https://huggingface.co/datasets/sentence-transformers/natural-questions} \\
HotpotQA & Retrieval & 120,528 & 1,217,525 & 45 & 103 & \citet{2018HotpotQA} & \url{https://huggingface.co/datasets/mteb/hotpotqa} \\
FEVER & Retrieval & 106,605 & 441,174 & 31 & 324 & \citet{2018FEVER} & \url{https://huggingface.co/datasets/mteb/fever} \\
ELI5 & Retrieval & 161,345 & 215,884 & 42 & 229 & \citet{2019ELI5} & \url{https://huggingface.co/datasets/Pavithree/eli5} \\
FiQA2018 & Retrieval & 7,452 & 32,615 & 33 & 234 & \citet{2018FIQA} & \url{https://huggingface.co/datasets/mteb/fiqa} \\
BioASQ & Retrieval & 125,248 & 149,900 & 27 & 295 & \citet{2015BioASQ} & \url{https://huggingface.co/datasets/BeIR/bioasq-generated-queries} \\
NFCorpus & Retrieval & 1,283 & 3,270 & 23 & 333 & \citet{2016NFCorpus} & \url{https://huggingface.co/datasets/mteb/nfcorpus} \\
MIRACL & Retrieval & 3,379 & 31,129 & 27 & 158 & \citet{2023MIRACL} & \url{https://huggingface.co/datasets/miracl/miracl} \\
Mr.TyDi & Retrieval & 3,547 & 79,695 & 27 & 148 & \citet{2021mrtidy} & \url{https://huggingface.co/datasets/mteb/mrtidy} \\
SciFact & Retrieval & 859 & 4,506 & 40 & 353 & \citet{2020SciFact} & \url{https://huggingface.co/datasets/mteb/scifact} \\
TriviaQA & Retrieval & 60,025 & 1,014,344 & 36 & 149 & \citet{2017TriviaQA} & \url{https://huggingface.co/datasets/sentence-transformers/trivia-qa-triplet} \\
COLIEE & Retrieval & 454 & 532 & 61 & 123 & \citet{2022COLIEE} & \url{https://www.modelscope.cn/datasets/sentence-transformers/coliee} \\
PubMedQA & Retrieval & 60,227 & 61,233 & 39 & 314 & \citet{2019PubMedQA} & \url{https://huggingface.co/datasets/qiaojin/PubMedQA} \\
S2ORC-Title-Abstract & Retrieval & 250,000 & 2,476,989 & 34 & 136 & \citet{2020S2ORC} & \url{https://huggingface.co/datasets/sentence-transformers/s2orc} \\
S2ORC-Title-Citation & Retrieval & 132,879 & 1,619,105 & 36 & 21 & \citet{2020S2ORC} & \url{https://huggingface.co/datasets/sentence-transformers/s2orc} \\
S2ORC-Abstract-Citation & Retrieval & 231,587 & 1,615,793 & 259 & 256 & \citet{2020S2ORC} & \url{https://huggingface.co/datasets/sentence-transformers/s2orc} \\
Amazon QA & Retrieval & 59,340 & 894,812 & 43 & 69 & \citet{2019AmazonQA} & \url{https://github.com/amazonqa/amazonqa} \\
SPECTER & Retrieval & 24,717 & 199,028 & 38 & 14 & \citet{2020SPECTER} & \url{https://huggingface.co/datasets/sentence-transformers/specter} \\
XSum & Retrieval & 184,383 & 214,562 & 44 & 459 & \citet{2018XSum} & \url{https://huggingface.co/datasets/EdinburghNLP/xsum} \\
CNN\_DM & Retrieval & 100,000 & 290,602 & 82 & 766 & \citet{2015CNN-DM} & \url{https://huggingface.co/datasets/abisee/cnn_dailymail} \\
Sentence Compression & Retrieval & 175,477 & 175,477 & 26 & 33 & \citet{2013Sentence-Compression} & \url{https://huggingface.co/datasets/sentence-transformers/sentence-compression} \\
StackExchange-DupQuestions-S2S & Retrieval & 183,559 & 158,628 & 31 & 14 & \citet{2021Embedding-Training-Data} & \url{https://huggingface.co/datasets/sentence-transformers/stackexchange-duplicates} \\
StackExchange-DupQuestions-P2P & Retrieval & 203,060 & 124,283 & 189 & 180 & \citet{2021Embedding-Training-Data} & \url{https://huggingface.co/datasets/sentence-transformers/stackexchange-duplicates} \\
QQP & Retrieval & 243,598 & 445,064 & 31 & 13 & \citet{2019QQP} & \url{https://gluebenchmark.com/tasks} \\
StackOverflow-DupQuestions & Retrieval & 19,847 & 315,577 & 27 & 11 & \citet{2018StackOverflowDupQuestions} & \url{https://huggingface.co/datasets/mteb/stackoverflowdupquestions-reranking} \\
STS12 & Retrieval & 1,858 & 2,612 & 40 & 27 & \citet{2012STS12} & \url{https://huggingface.co/datasets/mteb/sts12-sts} \\
STS22 & Retrieval & 389 & 1,380 & 505 & 494 & \citet{2022STS22} & \url{https://huggingface.co/datasets/mteb/sts22-crosslingual-sts} \\
STSBenchmark & Retrieval & 3,297 & 9,247 & 25 & 14 & \citet{2021STSBenchmark} & \url{https://huggingface.co/datasets/mteb/stsbenchmark-sts} \\
    \midrule
    \rowcolor{white} Total & Retrieval & 4,918,949 & 22,050,569 \\
    \bottomrule
    \end{tabular}
    }
    \label{tab:training-data-retrieval}
\end{table}
```

