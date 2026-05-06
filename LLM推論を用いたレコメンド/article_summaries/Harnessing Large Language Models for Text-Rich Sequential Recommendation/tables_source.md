# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[tb]
  \small
  \caption{Statistics of the datasets.}
  \label{tab:statistics}   
  \centering
  \begin{tabular}{l|r|r}
  \hline
  description & Amazon-M2 & MIND \\\hline
  \# of different attributes&10&4\\
  \# of positive samples in the training set&10,000&10,000\\
  \# of positive samples in the validation set&1,000&1,000\\
  \# of positive samples in the test set&1,000&1,000\\
  Avg. \# of historical user behavior sequence&13.16&16.23\\
  Avg. \# of tokens corresponding to an item&141.45&40.83\\
  \hline
  \end{tabular}
  \vspace{-4mm}
\end{table}
```

## Table 2
```latex
\begin{table*}[tb]  
    \centering  
    \caption{The performance of different models.}  
     \vspace{-2mm}
    \label{tab:main_result}  
      \begin{center}  
    %   \resizebox{\columnwidth}{!}{
          \begin{tabular}{l|ccc|ccc|ccc|ccc}  
              \hline  
            ~&\multicolumn{6}{c|}{Amazon-M2}&\multicolumn{6}{c}{MIND}\\\hline
            ~&\multicolumn{3}{c|}{Recall}&\multicolumn{3}{c|}{MRR}&\multicolumn{3}{c|}{Recall}&\multicolumn{3}{c}{MRR}\\\hline
            
            ~&@3&@5&@10&@3&@5&@10&@3&@5&@10&@3&@5&@10  \\
            \midrule
            NCF&  0.8300&	0.8830&	 0.9440&  0.7328&	0.7448&	0.7529&	0.7010&	0.8030&	0.9240&	0.5523&	0.5759&	0.5926\\
            DIN& 0.7380&	0.8330&	0.9240&	0.5838&	0.6053&	0.6174&	0.7900&	0.8620&	0.9330&	0.6352&	0.6519&	0.6616 \\
            DIEN& 	0.7330&	0.8170&	0.9070&	0.5922&	0.6114&	0.6229&	0.7300&	0.8200&	0.9140&	0.6045&	0.6251&	0.6379 \\ 
            GRU4Rec& 	0.4420&	0.5590&	0.7350&	0.3355&	0.3621&	0.3855&	0.6650&	0.7970&	0.9260&	0.5305&	0.5610&	0.5787 \\
            NARM& 	0.8410&	0.8860&	0.9330&	0.7475&	0.7577&	0.7638&	0.5820&	0.7330&	0.8930&	0.4142&	0.4489&	0.4703\\
            SASRec& 0.6550&	0.7570&	0.9040&	0.4938&	0.5173&	0.5374&	0.8420&	0.8960&	0.9410&	0.7447&	0.7574&	0.7636 \\
            CORE& 	0.5230&	0.4632&	0.6450&	0.4527&	0.4632&	0.4728&	0.5170&	0.5580&	0.6370&	0.4392&	0.4488&	0.4586 \\
            TALLRec&0.8790&0.9050&0.9460&0.8585&0.8644&0.8697&0.8580&0.9020&0.9590&0.7708&0.7807&0.7885\\
            \midrule
            LLM-TRSR-Hierarchical&\textbf{0.8910}&0.9120&0.9490&0.8597&0.8643&0.8693&\textbf{0.9160}&\textbf{0.9430}&0.9750&\textbf{0.8505}&\textbf{0.8568}&\textbf{0.8611}\\
            LLM-TRSR-Recurrent&\textbf{0.8910}&\textbf{0.9130}&\textbf{0.9570}&\textbf{0.8632}&\textbf{0.8681}&\textbf{0.8737}&0.9060&0.9390&\textbf{0.9840}&0.8400&0.8475&0.8534\\
            \hline
          \end{tabular}  
      \end{center}  
    \vspace{-3mm}
    \end{table*}
```

