# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}
\caption{\textbf{Forgetting image classification tasks via negation}. Results are shown for CLIP models, reporting average accuracy (\%) on the eight target tasks we wish to forget (Cars, DTD, EuroSAT, GTSRB, MNIST, RESISC45, SUN397 and SVHN), and the control task (ImageNet). Negating task vectors reduce the accuracy of a pre-trained ViT-L/14 by 45.8 percentage points on the target tasks, with little loss on the control task. Additional details and results are shown in Appendix \ref{sec:clip-neg-extended}.}
% \vspace{-8pt}
\setlength\tabcolsep{5.5pt}
\renewcommand{\arraystretch}{0.9}
\footnotesize
\begin{center}
\begin{tabular}{l@{\hskip .3in}cc|cc|cc}
\toprule
\multirow{2}{*}{Method} & \multicolumn{2}{c|}{ViT-B/32} & \multicolumn{2}{c|}{ViT-B/16} & \multicolumn{2}{c}{ViT-L/14} \\
 & Target ($\downarrow$) & Control ($\uparrow$) & Target ($\downarrow$) & Control ($\uparrow$) & Target ($\downarrow$) & Control ($\uparrow$)  \\\midrule
Pre-trained & 48.3 & 63.4  & 55.2 & 68.3  & 64.8 & 75.5\\\midrule
Fine-tuned  & 90.2 & 48.2  & 92.5 & 58.3 & 94.0 & 72.6 \\
Gradient ascent  & 2.73 & 0.25 & 1.93 & 0.68 & 3.93 & 16.3\\
Random vector  & 45.7 & 61.5 & 53.1 & 66.0 & 60.9 & 72.9\\\midrule
Negative task vector & 24.0 & 60.9 & 21.3 & 65.4 & 19.0 & 72.9\\

\bottomrule
\end{tabular}
\end{center}
\label{tab:forget_image}
\end{table*}
```

## Table 2
```latex
\begin{table*}
\caption{\textbf{Making language models less toxic with negative task vectors.} Results are shown for the GPT-2 Large model. Negative task vectors decrease the amount of toxic generations by 6$\times$, while resulting in a model with comparable perplexity on a control task (WikiText-103). Additional details and results are shown in Appendix \ref{sec:appendix-neg-lang}.}
\setlength\tabcolsep{4.5pt}
\renewcommand{\arraystretch}{0.9}
\footnotesize

\begin{center}

\begin{tabular}{lrrr}

\toprule
 
 Method & \% toxic generations ($\downarrow$)& Avg. toxicity score ($\downarrow$) & WikiText-103 perplexity ($\downarrow$)
 \\\midrule
Pre-trained & 4.8 & 0.06 & 16.4 \\\midrule
Fine-tuned & 57 & 0.56 & 16.6 \\
Gradient ascent & 0.0 & 0.45 & $>$10$^{10}$ \\
Fine-tuned on non-toxic & 1.8 & 0.03 & 17.2 \\
Random vector  & 4.8 & 0.06 & 16.4 \\\midrule
Negative task vector & 0.8 & 0.01 & 16.9 \\\bottomrule
\end{tabular}
\end{center}
\label{tab:toxicity}

\end{table*}
```

## Table 3
```latex
\begin{table*}
\caption{\textbf{Improving domain generalization with task analogies.} Using an auxiliary task for which labeled data is available and unlabeled data from both the auxiliary and the target datasets, task analogies improve the accuracy for multiple T5 models and two sentiment analysis target tasks \citep{zhang2015character,mcauley2013hidden}, without using any labeled data from the target tasks.}
\setlength\tabcolsep{6.5pt}
\renewcommand{\arraystretch}{0.9}
\small
\begin{center}
\begin{tabular}{lcccccccc} 
\toprule
 & & \multicolumn{3}{c}{target = Yelp} & & \multicolumn{3}{c}{target = Amazon} \\\cmidrule{3-5}\cmidrule{7-9}
Method & &  T5-small & T5-base & T5-large & & T5-small & T5-base & T5-large 
\\\midrule
Fine-tuned on auxiliary & & 88.6 & 92.3 & 95.0 & & 87.9 & 90.8 & 94.8 \\
Task analogies & & 89.9 & 93.0 & 95.1 & & 89.0 & 92.7 & 95.2 \\
Fine-tuned on target & & 91.1 & 93.4 & 95.5 & & 90.2 & 93.2 & 95.5 \\
\bottomrule
\end{tabular}
\end{center}
\label{tab:sentiment-analog}
\vspace{6pt}
\end{table*}
```

## Table 4
```latex
\begin{table*}
\caption{\textbf{Improving performance on target tasks with external task vectors.} For four text classification tasks from the GLUE benchmark, adding task vectors downloaded from the Hugging Face Hub  can improve accuracy of fine-tuned T5 models. Appendix \ref{sec:appendix-add-lang} shows additional details.}
\setlength\tabcolsep{4.5pt}
\renewcommand{\arraystretch}{0.9}
\small
\begin{center}
\begin{tabular}{lccccc}
\toprule
Method & MRPC & RTE & CoLA & SST-2 & Average \\\midrule
Zero-shot &	74.8	& 52.7	& 8.29	& 92.7	& 57.1 \\
Fine-tuned &	88.5 &	77.3 &	52.3 &	94.5 &	78.1 \\
Fine-tuned + task vectors	& 89.3 \tiny{(+0.8)}	& 77.5 \tiny{(+0.2)}& 	53.0	\tiny{(+0.7)} & 94.7 \tiny{(+0.2)}	& 78.6 \tiny{(+0.5)} \\
\bottomrule
\end{tabular}
\end{center}
\label{tab:glue}
\end{table*}
```

## Table 5
```latex
\begin{table*}
\caption{Forgetting via negation on image classification tasks. Results are shown for a CLIP ViT-L/14 model \citep{radford2021learning}, reporting accuracy on both the target (T) and control (C) tasks.}
\setlength\tabcolsep{2.3pt}
\renewcommand{\arraystretch}{1.05}
\footnotesize
\begin{center}
\begin{tabular}{lcc?cc?cc?cc?cc?cc?cc?cc}
\toprule
\multirow{2}{*}{Method} & \multicolumn{2}{c?}{{Cars}} & \multicolumn{2}{c?}{DTD} & \multicolumn{2}{c?}{EuroSAT} & \multicolumn{2}{c?}{GTSRB} & \multicolumn{2}{c?}{MNIST} & \multicolumn{2}{c?}{{RESISC45}} & \multicolumn{2}{c?}{{SUN397}} & \multicolumn{2}{c}{{SVHN}} \\
 & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ \\\midrule
Pre-trained & 77.8 & 75.5 & 55.4 & 75.5 & 60.2 & 75.5 & 50.6 & 75.5 & 76.4 & 75.5 & 71.0 & 75.5 & 68.3 & 75.5 & 58.6 & 75.5 \\
Fine-tuned & 92.8 & 73.1 & 83.7 & 72.3 & 99.2 & 70.5 & 99.3 & 73.1 & 99.8 & 72.9 & 96.9 & 73.8 & 82.4 & 72.7 & 98.0 & 72.6 \\
Neg. gradients & 0.00 & 4.82 & 2.13 & 0.10 & 9.26 & 1.07 & 1.19 & 0.07 & 9.80 & 67.0 & 2.14 & 0.07 & 0.25 & 0.00 & 6.70 & 57.2 \\%\midrule
% Task vectors & & & & & & & & & & & & & & & & & & \\
Random vector & 72.0 & 73.3 & 52.1 & 72.2 & 59.7 & 73.5 & 43.4 & 72.5 & 74.8 & 72.8 & 70.8 & 73.0 & 66.9 & 72.7 & 47.1 & 72.9\\\midrule
Neg. task vector & 32.0 & 72.4 & 26.7 & 72.2 & 7.33 & 73.3 & 6.45 & 72.2 & 2.69 & 74.9 & 19.7 & 72.9 & 50.8 & 72.6 & 6.71 & 72.7 \\

\bottomrule
\end{tabular}
\end{center}
\label{tab:forget_image_l14}
\end{table*}
```

## Table 6
```latex
\begin{table*}
\caption{Forgetting via negation on image classification tasks. Results are shown for a CLIP ViT-B/16 model \citep{radford2021learning}, reporting accuracy on both the target (T) and control (C) tasks.}
\setlength\tabcolsep{2.3pt}
\renewcommand{\arraystretch}{1.05}
\footnotesize
\begin{center}
\begin{tabular}{lcc?cc?cc?cc?cc?cc?cc?cc}
\toprule
\multirow{2}{*}{Method} & \multicolumn{2}{c?}{{Cars}} & \multicolumn{2}{c?}{DTD} & \multicolumn{2}{c?}{EuroSAT} & \multicolumn{2}{c?}{GTSRB} & \multicolumn{2}{c?}{MNIST} & \multicolumn{2}{c?}{{RESISC45}} & \multicolumn{2}{c?}{{SUN397}} & \multicolumn{2}{c}{{SVHN}} \\
 & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$\\\midrule
Pre-trained & 64.6 & 68.3 & 44.9 & 68.3 & 53.9 & 68.3 & 43.4 & 68.3 & 51.6 & 68.3 & 65.8 & 68.3 & 65.5 & 68.3 & 52.0 & 68.3 \\
Fine-tuned & 87.0 & 61.9 & 82.3 & 57.5 & 99.1 & 56.0 & 99.0 & 54.7 & 99.7 & 55.2 & 96.4 & 62.2 & 79.0 & 61.7 & 97.7 & 56.8 \\
Neg. gradients & 0.36 & 0.11 & 2.13 & 0.09 & 9.26 & 0.14 & 0.71 & 0.10 & 0.04 & 1.20 & 2.60 & 0.10 & 0.25 & 0.00 & 0.08 & 3.69\\
Rand. task vector & 61.0 & 65.6 & 43.9 & 66.3 & 51.7 & 66.2 & 43.1 & 65.0 & 51.6 & 68.3 & 63.6 & 65.6 & 63.7 & 65.2 & 46.2 & 65.5 \\\midrule
Neg. task vector & 30.8 & 65.4 & 26.5 & 65.6 & 12.3 & 65.8 & 9.53 & 65.8 & 9.55 & 65.4 & 26.5 & 65.1 & 48.6 & 65.1 & 6.43 & 65.4 \\
\bottomrule
\end{tabular}
\end{center}
\label{tab:forget_image_b16}
\end{table*}
```

## Table 7
```latex
\begin{table*}
\caption{Forgetting via negation on image classification tasks. Results are shown for a CLIP ViT-B/32 model \citep{radford2021learning}, reporting accuracy on both the target (T) and control (C) tasks.}
\setlength\tabcolsep{2.3pt}
\renewcommand{\arraystretch}{1.05}
\footnotesize
\begin{center}
\begin{tabular}{lcc?cc?cc?cc?cc?cc?cc?cc}
\toprule
\multirow{2}{*}{Method} & \multicolumn{2}{c?}{{Cars}} & \multicolumn{2}{c?}{DTD} & \multicolumn{2}{c?}{EuroSAT} & \multicolumn{2}{c?}{GTSRB} & \multicolumn{2}{c?}{MNIST} & \multicolumn{2}{c?}{{RESISC45}} & \multicolumn{2}{c?}{{SUN397}} & \multicolumn{2}{c}{{SVHN}} \\
 & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$ & T$\downarrow$ & C$\uparrow$  \\\midrule
Pre-trained & 59.6 & 63.4 & 44.1 & 63.4 & 45.9 & 63.4 & 32.5 & 63.4 & 48.7 & 63.4 & 60.7 & 63.4 & 63.2 & 63.4 & 31.5 & 63.4 \\
Fine-tuned & 79.2 & 55.2 & 78.7 & 49.3 & 98.6 & 47.2 & 98.5 & 39.1 & 99.6 & 42.5 & 95.0 & 53.2 & 75.1 & 54.6 & 97.2 & 44.7 \\
Neg. gradients & 0.01 & 0.11 & 2.13 & 0.10 & 9.26 & 0.10 & 1.19 & 0.07 & 0.00 & 1.22 & 2.60 & 0.10 & 0.25 & 0.01 & 6.38 & 0.29 \\
Rand. task vector & 54.1 & 60.9 & 39.9 & 61.5 & 45.8 & 63.4 & 27.9 & 60.7 & 48.3 & 63.4 & 57.1 & 60.9 & 61.3 & 60.5 & 31.2 & 60.7 \\\midrule
Neg. task vector & 36.0 & 61.1 & 27.8 & 60.2 & 13.6 & 61.3 & 8.13 & 61.4 & 16.7 & 60.7 & 31.7 & 61.0 & 50.7 & 60.5 & 7.65 & 61.0 \\
\bottomrule
\end{tabular}
\end{center}
\label{tab:forget_image_b32}
\end{table*}
```

## Table 8
```latex
\begin{table*}
\caption{The effect of semantic overlap with the control task in forgetting experiments on image classification tasks. Results are shown for a CLIP ViT-L/14 model, reporting accuracy both on the target task and control task (Ctrl, ImageNet).}
\setlength\tabcolsep{4.4pt}
\renewcommand{\arraystretch}{1.05}
\footnotesize
\begin{center}
\begin{tabular}{lcc?cc?cc?cc}
\toprule
\multirow{2}{*}{Method} & \multicolumn{4}{c?}{{Without filtering}} & \multicolumn{4}{c}{With filtering} \\
 & Cars ($\downarrow$) & Ctrl ($\uparrow$) & SUN397 ($\downarrow$) & Ctrl ($\uparrow$) & Cars ($\downarrow$) & Ctrl ($\uparrow$) & SUN397 ($\downarrow$) & Ctrl ($\uparrow$) \\\midrule
Pre-trained & 77.8 & 75.5 & 68.3 & 75.5 & 77.8 & 75.5 & 68.3 & 76.1 \\
Fine-tuned & 92.8 & 73.1 & 82.4 & 72.7 & 92.8 & 73.3 & 82.4 & 73.1 \\\midrule
Neg. task vector & 32.0 & 72.4 & 50.8 & 72.6 & 32.0 & 72.5 & 48.1 & 72.4\\

\bottomrule
\end{tabular}
\end{center}
\label{tab:overlap-ablation}
\end{table*}
```

## Table 9
```latex
\begin{table*}
\caption{Making language models less toxic with negative task vectors. Results are shown for the GPT-2 Medium model.}
\setlength\tabcolsep{4.5pt}
\renewcommand{\arraystretch}{0.9}
\footnotesize
\begin{center}
\begin{tabular}{lrrr}
\toprule
 Method & \% toxic generations ($\downarrow$)& Avg. toxicity score ($\downarrow$) & WikiText-103 perplexity ($\downarrow$)
 \\\midrule
Pre-trained & 4.3 & 0.06 & 18.5 \\
Fine-tuned & 54.5 & 0.54 & 20.2 \\
Gradient ascent & 0.0 & 0.00 & $>$10$^{10}$ \\
Random task vector & 4.2 & 0.05 & 18.5 \\\midrule
Negative task vector & 1.8 & 0.02 & 18.9 \\\bottomrule
\end{tabular}
\end{center}
\label{tab:toxicity_gpt2med}
\end{table*}
```

## Table 10
```latex
\begin{table*}
\caption{Making language models less toxic with negative task vectors. Results are shown for the GPT-2 Small model.}
\setlength\tabcolsep{4.5pt}
\renewcommand{\arraystretch}{0.9}
\footnotesize
\begin{center}
\begin{tabular}{lrrr}
\toprule
 Method & \% toxic generations ($\downarrow$)& Avg. toxicity score ($\downarrow$) & WikiText-103 perplexity ($\downarrow$)
 \\\midrule
Pre-trained & 3.7 & 0.04 & 25.2 \\
Fine-tuned & 62.9 & 0.61 & 28.1 \\
Gradient ascent & 0.0 & 0.00 & $>$10$^{10}$ \\
Random task vector & 3.2 & 0.04 & 25.3 \\\midrule
Negative task vector & 2.5 & 0.03 & 25.3 \\\bottomrule
\end{tabular}
\end{center}
\label{tab:toxicity_gpt2small}
\end{table*}
```

## Table 11
```latex
\begin{table*}
\caption{\textbf{Learning via analogy.} By leveraging vectors from related tasks, we can improve accuracy on four new target tasks without any training data, and with little change on control settings. Results are shown for the CLIP models \citep{radford2019language}, additional details are provided in Appendix \ref{sec:appendix-kingsandqueens}.}
\setlength\tabcolsep{4.5pt}
\renewcommand{\arraystretch}{0.9}
\footnotesize
\begin{center}
\begin{tabular}{lcccccccc}
\toprule
 \multirow{2}{*}{Method}  & \multicolumn{2}{c}{Queens} & \multicolumn{2}{c}{Kings} &  \multicolumn{2}{c}{Woman} & \multicolumn{2}{c}{Men}
 \\
 & Target & Control & Target & Control & Target & Control & Target & Control \\
 \midrule
 ViT-B/32 & 0.00 & 63.4 & 0.00 & 63.4 & 0.00 & 63.4 & 0.00 & 63.4\\
 \quad{+ task vectors} & 42.0 & 62.4 & 30.0 & 62.4 & 69.4 & 62.5 & 58.0 & 62.6\\\midrule
 ViT-B/16 & 0.00 & 68.3 & 0.00 & 68.3 & 0.00 & 68.3 & 0.00 & 68.3 \\
\quad{+ task vectors} & 66.0 & 67.5 & 94.0 & 67.4 & 87.8 & 67.5 & 62.0 & 67.6 \\\midrule
ViT-L/14 & 0.00 & 75.5 & 0.00 & 75.5 & 0.00 & 75.5 & 0.00 & 75.5 \\
\quad{+ task vectors} & 100 & 74.7 & 100 & 74.5 & 100 & 74.6 & 96.0 & 74.6\\
\bottomrule
\end{tabular}
\end{center}
\label{tab:kingsandqueens}
\end{table*}
```

## Table 12
```latex
\begin{table*}
\caption{\textbf{Learning by analogy on subpopulations.} Results are shown for multiple CLIP models, as detailed in Section \ref{sec:appendix-sketches}.}
\setlength\tabcolsep{4.5pt}
\renewcommand{\arraystretch}{0.9}
\footnotesize
\begin{center}
\begin{tabular}{lccccccc}
\toprule
 \multirow{2}{*}{Model} & Samples & \multirow{2}{*}{Task vectors} & \multicolumn{5}{c}{Accuracy} \\
& per class & & Sketches-A & Sketches-B & ImageNet-A & ImageNet-B & Average\\\midrule
\multirow{8}{*}{ViT-B/32} & 0 & \xmark & 0.712 & 0.677 & 0.861 & 0.923& 0.793 \\
& 0 & \cmark & 0.782 & 0.758 & 0.861 & 0.926& 0.832 \\
& 1 & \xmark & 0.754 & 0.758 & 0.868 & 0.919& 0.825 \\
& 1 & \cmark & 0.782 & 0.766 & 0.866 & 0.922& 0.834 \\
& 2 & \xmark & 0.768 & 0.778 & 0.868 & 0.919& 0.833 \\ 
& 2 & \cmark & 0.786 & 0.800 & 0.867 & 0.922& 0.844 \\
& 4 & \xmark & 0.810 & 0.780 & 0.871 & 0.926& 0.847 \\
& 4 & \cmark & 0.802 & 0.796 & 0.871 & 0.927& 0.849 \\\midrule
\multirow{8}{*}{ViT-B/16} & 0 & \xmark & 0.716 & 0.732 & 0.885 & 0.946& 0.820\\
& 0 & \cmark & 0.794 & 0.794 & 0.889 & 0.953& 0.858\\
& 1 & \xmark & 0.758 & 0.812 & 0.894 & 0.948& 0.853\\
& 1 & \cmark & 0.796 & 0.804 & 0.897 & 0.957& 0.863\\
& 2 & \xmark & 0.792 & 0.817 & 0.897 & 0.951& 0.865\\
& 2 & \cmark & 0.804 & 0.829 & 0.899 & 0.956& 0.872\\
& 4 & \xmark & 0.815 & 0.812 & 0.904 & 0.952& 0.871\\
& 4 & \cmark & 0.831 & 0.825 & 0.904 & 0.953& 0.878\\\midrule
\multirow{8}{*}{ViT-L/14} & 0 & \xmark & 0.823 & 0.831 & 0.913 & 0.962& 0.882\\
& 0 & \cmark & 0.879 & 0.861 & 0.922 & 0.968& 0.908\\
& 1 & \xmark & 0.845 & 0.863 & 0.923 & 0.971& 0.900\\
& 1 & \cmark & 0.879 & 0.863 & 0.930 & 0.973& 0.911\\
& 2 & \xmark & 0.865 & 0.881 & 0.925 & 0.973& 0.911\\
& 2 & \cmark & 0.875 & 0.881 & 0.932 & 0.975& 0.916\\
& 4 & \xmark & 0.875 & 0.883 & 0.934 & 0.973& 0.916\\
& 4 & \cmark & 0.903 & 0.887 & 0.941 & 0.975& 0.927\\

\bottomrule
\end{tabular}
\end{center}
\label{tab:sketches}
\end{table*}
```

