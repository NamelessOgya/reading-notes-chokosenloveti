# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
\caption{\textcolor{black}{Performance comparison of methods without whitening and with whitening. R@20 and N@20 are reported.}}
  \centering
   \small
  \begin{tabular}{l@{\hspace{0.5\tabcolsep}}l@{\hspace{0.5\tabcolsep}}|c@{\hspace{0.5\tabcolsep}}c@{\hspace{0.5\tabcolsep}}|c@{\hspace{0.5\tabcolsep}}c}
    \toprule
    Dataset&Metric& SASRec$^{ID}$ &SASRec$^T$ &WhitenRec & \%Improv\\
    \midrule
    \multirow{2}{*}{Arts}
    &R@20&0.1410&\underline{0.1476}&\textbf{0.1625}& 10.1\%\\
    &N@20&\underline{0.0776}&0.0721&\textbf{0.0796}& 2.6\%\\
    \midrule
    \multirow{2}{*}{Toys}
    &R@20&\underline{0.1121}&0.0983&\textbf{0.1201}& 7.1\% \\
    &N@20&\underline{0.0467}&0.0429&\textbf{0.0521}& 11.6\%\\
    \midrule
    \multirow{2}{*}{Tools}
    &R@20&0.0712&\underline{0.0739}&\textbf{0.0861}& 16.5\%\\
    &N@20&\underline{0.0418}&0.0386&\textbf{0.0453}& 8.4\%\\

    \bottomrule
  \end{tabular}
  \vspace{-1em}
  \label{tab:compare}
\end{table}
```

## Table 2
```latex
\begin{table}
\caption{Dataset Statistics. “Avg. n” and “Avg. i” denote the average length of user sequences and the average actions of items.}
  \centering
   \small
  \begin{tabular}{l|cccccc}
    \toprule
    Datasets & \#Users & \#Items & \#Inter. & Avg. n & Avg. i\\ 
    \midrule
    Arts   & 45,486 & 21,019 & 349,664 & 7.69 & 16.63 \\
    Toys &  85,694 & 40,483 & 618,738 & 7.22 & 15.28 \\
    Tools &  90,599 & 36,244 & 623,248 & 6.88 &17.20 \\
    \textcolor{black}{Food} & \textcolor{black}{28,988} & \textcolor{black}{12,910} & \textcolor{black}{274,509} & \textcolor{black}{9.47} & \textcolor{black}{21.26} \\
    \bottomrule
  \end{tabular}
  \label{tab:stats}
  \vspace{-1.2em}
\end{table}
```

## Table 3
```latex
\begin{table*}
    \caption{Performance comparison of different methods on the warm-start setting. The best results are in \textbf{boldface}, and the best results for baselines are \underline{underlined}. * denotes WhitenRec or WhitenRec+ surpasses the best baseline using a paired t-test ($p < 0.01$). The features utilized for item representations in each model are categorized as ID, text (T), or a combination of both (T+ID).}
    \centering
    \small
    \resizebox{\textwidth}{!}{
    \begin{tabular}{l@{\hspace{0.5\tabcolsep}}c|@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} c|@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}}| c@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} c @{\hspace{0.5\tabcolsep}} |c@{\hspace{0.5\tabcolsep}} c@{\hspace{0.5\tabcolsep}} }
    \toprule
    \multirow{2}{*}{Dataset} & \multirow{2}{*}{Metric}
    &GRCN&BM3&SASRec&CL4SRec&SASRec&SASRec&S$^3$-Rec&FDSA&UniSRec&UniSRec&\textcolor{black}{VQRec}&WhitenRec&WhitenRec+\\ 
    &&(T+ID)&(T+ID)&(ID)&(ID)&(T)&(T+ID)&(T+ID)&(T+ID)&(T)&(T+ID)&\textcolor{black}{(T)}&(T)&(T)\\
    
    \midrule
    \multirow{4}{*}{Arts}
    &R@20 &0.0851&0.1233&0.1410&0.1388&0.1476&0.1435&0.1411&0.1284&0.1500&\underline{0.1611}&\textcolor{black}{0.1390}&0.1625&\textbf{0.1688}*\\
    & R@50 &0.1296&0.1782&0.1967&0.1967&0.2129&0.2009&0.2007&0.1788&0.2165&\underline{0.2322}&\textcolor{black}{0.1947}&0.2348&\textbf{0.2403}*\\
    & N@20 &0.0411&0.0642&0.0776&0.0653&0.0721&0.0766&0.0762&\underline{0.0785}&0.0738&0.0774&\textcolor{black}{0.0734}&0.0796&\textbf{0.0810}*\\
    & N@50 &0.0499&0.0750&0.0887&0.0768&0.0850&0.0879&0.088&0.0888&0.0869&\underline{0.0915}&\textcolor{black}{0.0843}&0.0939*&\textbf{0.0952}*\\

    \midrule
    \multirow{4}{*}{Toys}
    & R@20 &0.0651&0.0965&0.1121&0.1094&0.0983&\underline{0.1163}&0.1068&0.0895&0.1042&\textbf{0.1257}&\textcolor{black}{0.1075}&0.1201&\textbf{0.1257}\\
    & R@50 &0.0981&0.1383&0.1581&0.1609&0.1542&0.1664&0.1533&0.1242&0.1607&\underline{0.1801}&\textcolor{black}{0.1491}&0.1798&\textbf{0.1874}*\\
    & N@20 &0.0304&0.0478&0.0467&0.0426&0.0429&0.0511&0.0488&0.0475&0.0451&\underline{0.0513}&\textcolor{black}{0.0468}&0.0521&\textbf{0.0537}*\\
    & N@50 &0.0369&0.0560&0.0558&0.0528&0.0539&0.0610&0.0581&0.0543&0.0563&\underline{0.0621}&\textcolor{black}{0.0550}&0.0639*&\textbf{0.0659}*\\
    
    \midrule
    \multirow{4}{*}{Tools}
    & R@20 &0.0452&0.0530&0.0712&0.0781&0.0739&0.0728&0.0707&0.0633&0.0772&\underline{0.0828}&\textcolor{black}{0.0734}&0.0861*&\textbf{0.0888}*\\
    & R@50 &0.0682&0.0714&0.0941&0.1027&0.1055&0.0954&0.0943&0.0812&0.1091&\underline{0.1116}&\textcolor{black}{0.0963}&0.1196*&\textbf{0.1236}*\\
    & N@20 &0.0234&0.0299&0.0418&0.0385&0.0386&\underline{0.0445}&0.0424&0.0432&0.0407&0.0420&\textcolor{black}{0.0423}&0.0453&\textbf{0.0462}*\\
    & N@50&0.0280&0.0335&0.0463&0.0433&0.0448&\underline{0.0490}&0.0470&0.0468&0.0470&0.0477&\textcolor{black}{0.0468}&0.0519*&\textbf{0.0531}*\\

    \midrule
    \multirow{4}{*}{\textcolor{black}{Food}}
& \textcolor{black}{R@20} &\textcolor{black}{0.0408}&\textcolor{black}{0.0540}&\textcolor{black}{0.0520}&\textcolor{black}{0.0531}&\textcolor{black}{0.0541}&\textcolor{black}{0.0547}&\textcolor{black}{0.0522}&\textcolor{black}{0.0518}&\textcolor{black}{0.0544}&\textcolor{black}{\underline{0.0555}}&\textcolor{black}{0.0471}&\textcolor{black}{0.0569}&\textcolor{black}{\textbf{0.0586}*}\\
& \textcolor{black}{R@50} &\textcolor{black}{0.0796}&\textcolor{black}{0.0947}&\textcolor{black}{0.0955}&\textcolor{black}{0.0949}&\textcolor{black}{0.0991}&\textcolor{black}{0.0984}&\textcolor{black}{0.0960}&\textcolor{black}{0.0960}&\textcolor{black}{\underline{0.1018}}&\textcolor{black}{0.1001}&\textcolor{black}{0.0861}&\textcolor{black}{0.1043}&\textcolor{black}{\textbf{0.1072}*}\\
& \textcolor{black}{N@20} &\textcolor{black}{0.0162}&\textcolor{black}{0.0215}&\textcolor{black}{0.0208}&\textcolor{black}{0.0214}&\textcolor{black}{0.0220}&\textcolor{black}{0.0222}&\textcolor{black}{0.0210}&\textcolor{black}{0.0210}&\textcolor{black}{0.0221}&\textcolor{black}{\underline{0.0223}}&\textcolor{black}{0.0189}&\textcolor{black}{0.0227}&\textcolor{black}{\textbf{0.0234}*}\\
& \textcolor{black}{N@50} &\textcolor{black}{0.0239}&\textcolor{black}{0.0295}&\textcolor{black}{0.0294}&\textcolor{black}{0.0297}&\textcolor{black}{0.0308}&\textcolor{black}{0.0308}&\textcolor{black}{0.0296}&\textcolor{black}{0.0297}&\textcolor{black}{\underline{0.0315}}&\textcolor{black}{0.0311}&\textcolor{black}{0.0266}&\textcolor{black}{0.0321}&\textcolor{black}{\textbf{0.0330}*}\\

    
    \bottomrule
    \end{tabular}}
    \vspace{-1em}
    \label{tab:overall}
\end{table*}
```

## Table 4
```latex
\begin{table*}
    \caption{Performance comparison of different methods on the cold-start setting. The best results are in \textbf{boldface}, and the second best results are \underline{underlined}. * denotes WhitenRec or WhitenRec+ surpasses the best baseline using a paired t-test ($p < 0.01$).}
    \centering
    \small
    % \resizebox{\textwidth}{!}{
    \begin{tabular}{l|cc|cc|c c| cc}
    \toprule
    \multirow{2}{*}{Model}&\multicolumn{2}{c|}{Arts}&\multicolumn{2}{c|}{Toys}
&\multicolumn{2}{c|}{Tools} &\multicolumn{2}{c}{\textcolor{black}{Food}}\\   
    &R@20&N@20&R@20&N@20&R@20&N@20&\textcolor{black}{R@20}&\textcolor{black}{N@20}\\
    \midrule
    SASRec(T)&0.0300&0.0130&0.0239&0.0100&0.0153&0.0057&\textcolor{black}{0.0031}&\textcolor{black}{0.0013}\\
    UniSRec(T)&0.0617&0.0281&0.0519&0.0222&0.0298&0.0158&\textcolor{black}{0.0037}&\textcolor{black}{0.0011}\\
    \midrule
    WhitenRec$_{G=1}$(T)&0.0554&0.0271&0.0530&0.0238*&0.0431*&0.0234*&\textcolor{black}{0.0037}&\textcolor{black}{0.0012}\\
    WhitenRec$_{G>1}$(T)&\underline{0.0656}*&\underline{0.0297}*&\underline{0.0624}*&\underline{0.0265}*&\underline{0.0501}*&\underline{0.0252}*&\underline{\textcolor{black}{0.0044*}}&\underline{\textcolor{black}{0.0014*}}\\
    WhitenRec+(T)&\textbf{0.0693}*&\textbf{0.0315}*&\textbf{0.0626}*&\textbf{0.0266}*&\textbf{0.0537}*&\textbf{0.0268}*&\textbf{\textcolor{black}{0.0048*}}&\textbf{\textcolor{black}{0.0017*}}\\
    \bottomrule
    \end{tabular}
    \label{tab:cold}
    \vspace{-1em}
\end{table*}
```

## Table 5
```latex
\begin{table*}
    \caption{Performance comparison of projection head for WhitenRec+.}
    \centering
    \small
    \begin{tabular}{l| c c |c c| c c| c c}
     \toprule
    \multirow{2}{*}{Model}&\multicolumn{2}{c|}{Arts}&\multicolumn{2}{c|}{Toys}&\multicolumn{2}{c|}{Tools} &\multicolumn{2}{c}{\textcolor{black}{Food}}\\   
    &R@20&N@20&R@20&N@20&R@20&N@20&\textcolor{black}{R@20}&\textcolor{black}{N@20}\\
    \midrule
     Linear&0.1476&0.0724&0.1029&0.0448&0.0751&0.0396&\textcolor{black}{0.0551}&\textcolor{black}{0.0222}\\
    MLP-1&0.1627&0.0782&0.1168&0.0494&0.0836&0.0427&\textcolor{black}{0.0560}&\textcolor{black}{0.0221}\\
    MLP-2&\underline{0.1688}&\textbf{0.0810}&\underline{0.1257}&\underline{0.0537}&\underline{0.0888}&\underline{0.0462}&\textcolor{black}{\textbf{0.0586}}&\textcolor{black}{\textbf{0.0234}}\\
    MLP-3&{0.1655}&\underline{0.0808}&\textbf{0.1261}&\textbf{0.0547}&\textbf{0.0894}&\textbf{0.0469}&\textcolor{black}{\underline{0.0565}}&\textcolor{black}{\underline{0.0229}}\\
    \textcolor{black}{MoE} & \textcolor{black}{\textbf{0.1690}} & \textcolor{black}{0.0784} & \textcolor{black}{0.0896} & \textcolor{black}{0.0446} & \textcolor{black}{0.0852} & \textcolor{black}{0.0438} & \textcolor{black}{0.0553} & \textcolor{black}{0.0221}\\
    \bottomrule
    \end{tabular}
    \vspace{-1em}
    \label{tab:head}
\end{table*}
```

## Table 6
```latex
\begin{table*}
    \caption{Performance comparison of whitening methods for WhitenRec+.}
    \centering
    \small
    \begin{tabular}{l| c c| c c| c c|cc}
     \toprule
    \multirow{2}{*}{Model}&\multicolumn{2}{c|}{Arts}&\multicolumn{2}{c|}{Toys}&\multicolumn{2}{c|}{Tools} &\multicolumn{2}{c}{\textcolor{black}{Food}}\\   
    &R@20&N@20&R@20&N@20&R@20&N@20&\textcolor{black}{R@20}&\textcolor{black}{N@20}\\
    \midrule
    PW &0.1243&0.0599 &0.0843&0.0363&0.0626&0.0322&\textcolor{black}{0.0547}&\textcolor{black}{0.0217}\\
    \textcolor{black}{BERT-flow}&\textcolor{black}{0.1550}&\textcolor{black}{0.0755}&\textcolor{black}{0.1082}&\textcolor{black}{0.0469}&\textcolor{black}{0.0796}&\textcolor{black}{0.0416}&\textcolor{black}{0.0558}&\textcolor{black}{0.0225}\\
    PCA&0.1283&0.0633&0.0748&0.0333&0.0625&0.0334&\textcolor{black}{0.0565}&\textcolor{black}{0.0227}\\
    BN&0.1628&0.0789&0.1150&0.0494&0.0799&0.0418&\textcolor{black}{\underline{0.0569}}&\textcolor{black}{0.0228}\\
    CD&\underline{0.1664}&\underline{0.0798}&\underline{0.1230}&\underline{0.0528}&\textbf{0.0891}&\textbf{0.0465}&\textcolor{black}{0.0565}&\textcolor{black}{\underline{0.0229}}\\
    ZCA&\textbf{0.1688}&\textbf{0.0810}&\textbf{0.1257}&\textbf{0.0537}&\underline{0.0888}&\underline{0.0462}&\textcolor{black}{\textbf{0.0586}}&\textcolor{black}{\textbf{0.0234}}\\

    \bottomrule
    \end{tabular}
    \vspace{-1em}
    \label{tab:whiten-methods}
\end{table*}
```

## Table 7
```latex
\begin{table}
    \caption{Performance comparison using different ensemble methods.}
    \centering
    \small
    \begin{tabular}{l@{\hspace{0.5\tabcolsep}}
    |c@{\hspace{0.7\tabcolsep}}c@{\hspace{0.7\tabcolsep}}c@{\hspace{0.7\tabcolsep}}|c@{\hspace{0.7\tabcolsep}}c@{\hspace{0.7\tabcolsep}}c}
     \toprule
    \multirow{2}{*}{Dataset}
    & \multicolumn{3}{c|}{R@20} & \multicolumn{3}{c}{N@20} \\   
    & Sum &Concat& Attn & Sum &Concat& Attn\\
    \midrule
    \multirow{1}{*}{Arts}&\textbf{0.1688}&0.1634&\underline{0.1640}&\textbf{0.0810}&0.0800&\underline{0.0803}\\
    \multirow{1}{*}{Toys}&\textbf{0.1257}&0.1187&\underline{0.1227}&\textbf{0.0537}&0.0515&\underline{0.0530}\\
    \multirow{1}{*}{Tools}&\underline{0.0888}&0.0854&\textbf{0.0892}&\underline{0.0462}&0.0445&\textbf{0.0465}\\
    \multirow{1}{*}{Food}&\textbf{0.0586}&\underline{0.0580}&\underline{0.0580}&\textbf{0.0234}&\textbf{0.0234}&\underline{0.0232}\\
    \bottomrule
    \end{tabular}
    \label{tab:ensemble-method}
    \vspace{-1em}
\end{table}
```

## Table 8
```latex
\begin{table}
    \renewcommand{\arraystretch}{0.9}
    \caption{\textcolor{black}{Performance comparison of WhitenRec and WhitenRec+ Using text or text+ID Embeddings.}}
    \centering
    \small
    % \resizebox{\columnwidth}{!}{
    \begin{tabular}{l c|cc|cccc}
     \toprule
    \multirow{2}{*}{Dataset} & \multirow{2}{*}{Metric} 
    & \multicolumn{2}{c|}{WhitenRec} & \multicolumn{2}{c}{WhitenRec+} \\   
    &&(T)&(T+ID)&(T)&(T+ID)\\
    \midrule
    \multirow{2}{*}{Arts} & R@20 &\textbf{0.1625}&0.1442&\textbf{0.1688}&0.1434\\
    & N@20 &\textbf{0.0796}&0.0786&\textbf{0.0810}&0.0787\\
    \midrule
    \multirow{2}{*}{Toys} & R@20&\textbf{0.1201}&0.1166&\textbf{0.1257}&0.1163 \\
    & N@20 &0.0521&\textbf{0.0532}&\textbf{0.0537}&0.0527\\
    \midrule
    \multirow{2}{*}{Tools} & R@20&\textbf{0.0861}&0.0756&\textbf{0.0888}&0.0741 \\
    & N@20 &\textbf{0.0453}&0.0449&\textbf{0.0462}&0.0453\\
    \midrule
    \multirow{2}{*}{Food} & R@20 &\textbf{0.0569}&0.0549&\textbf{0.0586}&0.0537\\
    & N@20 &\textbf{0.0227}&0.0222&\textbf{0.0234}&0.0220\\
    \bottomrule
    \end{tabular}
    \label{tab:with-ids}
    \vspace{-1em}
\end{table}
```

## Table 9
```latex
\begin{table}
  \centering
   \small
   % \color{blue}
       \renewcommand{\arraystretch}{0.9}
   \caption{\textcolor{black}{Efficiency Comparison on Tools Dataset.}}
    \resizebox{\columnwidth}{!}{
  % \vspace{-0.5em}
  \begin{tabular}{c|cc|cc|ccccc}
    \toprule
    \multirow{2}{*}{Model} & \multicolumn{2}{c|}{UniSRec} &\multicolumn{2}{c|}{WhitenRec} & \multicolumn{2}{c}{WhitenRec+}&\\
    & (T) & (T+ID) & (T) & (T+ID) & (T) & (T+ID)\\
    \midrule
    \#Params & 2.9M &13.8M&1.4M&12.2M&1.4M&12.2M\\
    s/Epoch &90 &99 &63 & 75 &64 & 77\\
    \bottomrule
  \end{tabular}}
  \vspace{-1.2em}
  \label{tab:efficiency}
\end{table}
```

