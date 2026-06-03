# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
  \begin{center}
    \caption{Statistics of the four datasets used in this study}
    \label{tab:datasetStats}
    \begin{tabular}{l|ccrrrcc} 
      \toprule
    Dataset & Time span selected &  Data filtering & \#User & \#Item & \#Interaction \\
      \midrule
      MovieLens-25M & 21/11/2009 to 20/11/2019 & No filtering & $62,202$ & $56,774$ & $9,808,925$ \\
      Yelp & 13/12/2009 to 12/12/2019 & 10-core & $116,655$ & $61,027$ & $3,127,215$ \\
      Amazon-music & 02/10/2008 to 01/10/2018 & 5-core & $11,651$ & $9,243$ & $114,833$  \\
      Amazon-electronic & 05/10/2008 to 04/10/2018 & 10-core & $109,990$ & $39,552$ & $1,752,238$ \\
      \bottomrule
    \end{tabular}
  \end{center}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
    \begin{center}
        \caption{Commonly used data split strategies in offline evaluation of recommender systems. We indicate whether local timeline (\eg time specific to a user)  or global timeline is observed, and whether a split strategy leads to data leakage.}
        \label{tab:dataPartitioning}
        \begin{tabular}{l|m{5.5cm}|ccc}
            \toprule
             Data split strategy & Definition of training and test instances  & Local & Global & Data\\
              & & timeline & timeline & leakage \\
             \midrule
             Random-split-by-ratio & Randomly sample a percentage of user-item interactions as test instances; the remaining are training instances. & No  & No & Yes \\
             \hline
             Random-split-by-user & Randomly sample a percentage of users, and take all their interactions as test instances; the remaining instances from other users are training instances. & No & No & Yes\\
            \midrule 
             Leave-one-out-split & Take each user's last interaction as a test instance; all remaining interactions are training instances. & Yes & No & Yes \\
             \hline
            Split-by-timepoint & All interactions after a time point are test instances; interactions before this time point are training instances. & No  & Yes & No\\
            \bottomrule
        \end{tabular}
        
    \end{center}

\end{table*}
```

## Table 3
```latex
\begin{table*}
  \begin{center}
    \caption{Number of test and training instances for test years $Y5$ and $Y7$. From the test year till $Y10$, more future data are made available to training.}
    \label{tab:trainTestYears}
    {\small 
    \begin{tabular}{c|c|c|rrrrrr}
      \toprule
      & Test &\#Test &\multicolumn{6}{c}{ \#Training instances accumulated till adding $Yx$'s data}\\    
      Dataset &   year & instances  & $Y5$ & $Y6$ & $Y7$ & $Y8$ & $Y9$ & $Y10$  \\
      \midrule
      MovieLens& $Y5$ & $3,171$ & $2,489,066$ & $3,876,800$ & $5,602,278$ & $7,243,348$ & $8,474,179$ & $9,805,754$  \\
      -25M&$Y7$ & $9,232$& - & - & $5,596,217$ & $7,237,287$ & $8,468,118$ & $9,799,693$\\
      \midrule
      \multirow{2}{*}{Yelp} & $Y5$ & $3,093$ & $878,494$ & $1,280,070$ & $1,723,554$ & $2,203,266$ & $2,702,445$ & $3,124,122$  \\
      &$Y7$ & $7,241$& - & - & $1,719,406$ & $2,199,118$ & $2,698,297$ & $3,119,974$\\
     \midrule
     Amazon& $Y5$ & $829$ & $18,283$ & $38,873$ & $71,227$ & $95,571$ & $108,496$ & $114,004$ \\
      -music&$Y7$ & $2,686$& - & - & $69,370$ & $93,714$ & $106,639$ & $112,147$\\
     \midrule
     Amazon& $Y5$ & $652$ & $234,398$ & $479,507$ & $898,947$ & $1,317,418$ & $1,607,543$ & $1,751,586$  \\
     -electronic &$Y7$ & $8,747$& - & - & $890,852$ & $1,309,323$ & $1,599,448$ & $1,743,491$\\
      \bottomrule
    \end{tabular}
    }
  \end{center}
\end{table*}
```

## Table 4
```latex
\begin{table*}[t]
  \begin{center}
    \caption{Among top-20 recommendations, the total number of future items recommended for test instances in $Y5$ and $Y7$, respectively, by the four models.}
    \label{tab:FutItems}
    {\small
    \begin{tabular}{l|c|cc|cc|cc|cc} 
      \toprule
    \multirow{2}{*}{Model}  & Dataset &\multicolumn{2}{c|}{MovieLens-25M} &\multicolumn{2}{c|}{Yelp} & 
     
    \multicolumn{2}{c|}{Amazon-music} &\multicolumn{2}{c}{Amazon-electronic} \\
     & Test year  & $Y5$ &  $Y7$ &  $Y5$ & $Y7$ & $Y5$  & $Y7$ & $Y5$ &  $Y7$ \\ 

     \midrule
    \multirow{5}{*}{BPR} 
        &$Y5$ & 0 & $-$ & $0$ & $-$ & 0 & $-$ & $0$ & $-$  \\
        &$Y6$	&$0$	&$-$	&$421$	&$-$	&$615$	&$-$	&$79$	&$-$\\
        &$Y7$	&$22$	&$0$	&$829$	&$0$	&$970$	&$0$	&$363$	&$0$\\
        &$Y8$	&$7$	&$11$	&$2,365$	&$504$	&$1,101$	&$651$	&$263$	&$200$\\
        &$Y9$	&$6$	&$88$	&$5,048$	&$287$	&$1,304$	&$1,103$	&$499$	&$1,224$\\
        &$Y10$	&$4$	&$81$	&$1,851$	&$1,598$	&$1,197$	&$1,155$	&$200$	&$583$\\

     \midrule
     \multirow{5}{*}{NeuMF} 
     &$Y5$ & 0 & $-$ & $0$ & $-$ & 0 & $-$ & $0$ & $-$  \\
     &$Y6$	&$3$	&$-$	&$602$	&$-$	&$910$	&$-$	&$28$	&$-$\\
    &$Y7$	&$7$	&$0$	&$1,631$	&$0$	&$1,501$	&$0$	&$1,303$	&$0$\\
    &$Y8$	&$27$	&$31$	&$3,260$	&$130$	&$1,733$	&$878$	&$549$	&$0$\\
    &$Y9$	&$22$	&$6$	&$3,542$	&$1,177$	&$1,491$	&$1,276$	&$729$	&$216$\\
    &$Y10$	&$15$	&$1$	&$5,205$	&$1,791$	&$1,577$	&$1,573$	&$2,655$	&$326$\\

     \midrule
     \multirow{5}{*}{LightGCN} 
     &$Y5$ & 0 & $-$ & $0$ & $-$ & 0 & $-$ & $0$ & $-$  \\
     &$Y6$	&$11$	&$-$	&$369$	&$-$	&$626$	&$-$	&$37$	&$-$\\
    &$Y7$	&$32$	&$0$	&$739$	&$0$	&$1,050$	&$0$	&$148$	&$0$\\
    &$Y8$	&$116$	&$189$	&$1,070$	&$569$	&$998$	&$632$	&$367$	&$220$\\
    &$Y9$	&$22$	&$26$	&$1,257$	&$979$	&$1,036$	&$893$	&$262$	&$430$\\
    &$Y10$	&$15$	&$58$	&$1,103$	&$1,360$	&$1,152$	&$1,029$	&$260$	&$470$\\

     \midrule
     \multirow{5}{*}{SASRec} 
     &$Y5$ & 0 & $-$ & $0$ & $-$ & 0 & $-$ & $0$ & $-$  \\
     &$Y6$	&$315$	&$-$	&$967$	&$-$	&$906$	&$-$	&$216$	&$-$\\
    &$Y7$	&$442$	&$0$	&$3,074$	&$0$	&$1,548$	&$0$	&$625$	&$0$\\
    &$Y8$	&$144$	&$489$	&$2,228$	&$2,666$	&$1,814$	&$1,341$	&$487$	&$1388$\\
    &$Y9$	&$342$	&$403$	&$3,162$	&$2,893$	&$1,982$	&$1,376$	&$20$	&$3,209$\\
    &$Y10$	&$993$	&$386$	&$1,741$	&$3,014$	&$1,980$	&$1,662$	&$12$	&$2,479$\\

     
     
     \bottomrule
    \end{tabular}
    }
  \end{center}
\end{table*}
```

## Table 5
```latex
\begin{table*}
  \begin{center}
    \caption{Lowest, highest performance changes (in percentage) when having more future data from the test year till $Y10$, computed based on the result of not accessing future data in training as reference.}
    \label{tab:improvement}
    \begin{tabular}{c|c|c|c|c|c} 
    \toprule
    Dataset&Metric & BPR  &NeuMF & LightGCN  & SASRec\\
    \midrule
    MovieLens&HR@20	&$-8.0\%$, $+2.3\%$	&$-4.1\%$, $+0.9\%$	&$-3.8\%$, $+11.1\%$	&$-5.3\%$, $+17.2\%$ \\
    -25M&NDCG@20	&$-6.3\%$, $+5.5\%$	&$-1.5\%$, $+2.0\%$	&$-9.3\%$, $+6.8\%$	&$-5.4\%$, $+16.8\%$\\  

    \midrule
    \multirow{2}{*}{Yelp}&HR@20	&$-17.8\%$, $+9.2\%$	&$-6.1\%$, $+18.3\%$	&$-0.3\%$, $+10.8\%$	&$-13.6\%$, $+1.9\%$\\
    &NDCG@20	&$-13.9\%$, $+15.4\%$	&$-6.6\%$, $+18.3\%$	&$-0.5\%$, $+8.0\%$	&$-29.0\%$, $-0.6\%$\\
    \midrule
    Amazon&HR@20	&$+19.3\%$, $+37.2\%$	&$+39.6\%$, $+65.6\%$	&$0\%$, $+22.8\%$	&$-5.4\%$, $+3.3\%$\\
    -music&NDCG@20	&$+23.6\%$, $+51.8\%$	&$+40.2\%$, $+89.5\%$	&$+1.9\%$, $+32.7\%$	&$-3.4\%$, $+6.3\%$\\
    \midrule
    Amazon&HR@20	&$+6.4\%$, $+22.9\%$	&$-38.1\%$, $+14.3\%$	&$-9.7\%$, $+22.4\%$	&$-7.5\%$, $+62.5\%$\\
    -electronic&NDCG@20	&$+10.3\%$, $+22.0\%$	&$-35.5\%$, $+13.8\%$	&$-7.7\%$, $+24.1\%$	&$-3.3\%$, $+73.0\%$\\
    \bottomrule
    \end{tabular}
  \end{center}
\end{table*}
```

## Table 6
```latex
\begin{table*}[t]
    \centering
    \caption{Ranking order of BPR, NeuMF, SASRec, and LightGCN in terms of HR@20 for test year $Y5$,  with different amount of ``future data'', on four datasets. Here, $1$ indicates that the model achieves the highest HR@20, and correspondingly the best recommendation performance. $4$ refers to the worst model in terms of HR@20 among four baselines.}
    {\small 
    \begin{tabular}{c|c|cccc}
        \toprule
         Dataset & Train Year & BPR & NeuMF & SASRec & LightGCN \\
         \midrule
         \multirow{6}{*}{MovieLens-25M} &$Y5$	&$2$	&$3$	&$1$	&$4$\\
        &$Y6$	&$3$	&$4$	&$1$	&$2$\\
        &$Y7$	&$2$	&$3$	&$1$	&$4$\\
        &$Y8$	&$4$	&$2$	&$1$	&$3$\\
        &$Y9$	&$3$	&$2$	&$1$	&$4$\\
        &$Y10$	&$4$	&$3$	&$1$	&$2$\\



         \midrule
         \multirow{6}{*}{Yelp}&$Y5$	&$3$	&$4$	&$2$	&$1$\\
        &$Y6$	&$3$	&$4$	&$2$	&$1$\\
        &$Y7$	&$2$	&$4$	&$3$	&$1$\\
        &$Y8$	&$3$	&$4$	&$2$	&$1$\\
        &$Y9$	&$3$	&$4$	&$2$	&$1$\\
        &$Y10$	&$2$	&$4$	&$3$	&$1$\\



         \midrule
         \multirow{6}{*}{Amazon-music}&$Y5$	&$2$	&$4$	&$3$	&$1$\\
        &$Y6$	&$1$	&$3$	&$4$	&$2$\\
        &$Y7$	&$1$	&$3$	&$4$	&$2$\\
        &$Y8$	&$2$	&$3$	&$4$	&$1$\\
        &$Y9$	&$2$	&$3$	&$4$	&$1$\\
        &$Y10$	&$1$	&$3$	&$4$	&$2$\\



         \midrule
         \multirow{6}{*}{Amazon-electronic} &$Y5$	&$2$	&$3$	&$4$	&$1$\\
        &$Y6$	&$2$	&$3$	&$4$	&$1$\\
        &$Y7$	&$2$	&$3$	&$4$	&$1$\\
        &$Y8$	&$1$	&$3$	&$4$	&$2$\\
        &$Y9$	&$2$	&$4$	&$3$	&$1$\\
        &$Y10$	&$3$	&$4$	&$2$	&$1$\\




         \bottomrule
    \end{tabular}
    }
    \label{tab:rankingOrder}
\end{table*}
```

