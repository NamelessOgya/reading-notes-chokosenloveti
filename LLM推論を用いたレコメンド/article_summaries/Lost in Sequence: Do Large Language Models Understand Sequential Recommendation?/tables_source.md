# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[h]
\small
% \caption[Caption for LOF]{An example of prompt for next item title generation for LLM4Rec models (i.e., TALLRec, LLaRA, CoLLM, and A-LLMRec). Note that LLaRA uses a hybrid prompting method that uses only text or with item embeddings. }
\caption[Caption for LOF]{An example  prompt for various LLM4Rec models (Next Item Title Generation approach).
% (i.e., TALLRec, LLaRA, CoLLM, and A-LLMRec). 
}
\vspace{-2ex}
\resizebox{0.95\linewidth}{!}{
\begin{tabular}{c|l|l|l}
\toprule
 \multicolumn{1}{c|}{}  & \multicolumn{1}{c|}{(a) \textbf{TALLRec}} & \multicolumn{1}{c|}{(b) \textbf{LLaRA}} & \multicolumn{1}{c}{(c) \textbf{CoLLM/A-LLMRec}} \\ \midrule\midrule
\multirow{3}{*}{\textbf{Inputs}} & This user has made a series of purchases& This user has made a series of purchases in the & This is user representation from recommendation models: \\ 
  & in the following order: (History Item List: & following order: (History Item List: [No.\# Time:& \textcolor{red}{[User Representation]}, and this user has made a series of purchases in\\  
 \multirow{2}{*}{$(\mathcal{P}^{u})$} &[No.\#  Time: YYYY/MM/DD Title: \textcolor{magenta}{Item Title}]).  & YYYY/MM/DD Title: \textcolor{magenta}{Item Title}, \textcolor{blue}{Item Embedding}]). & the following order: (History Item List: [No.\# Time: YYYY/\\
  &Choose one "Title" to recommend for this user&Choose one "Title" to recommend for this user to & MM/DD Title: \textcolor{magenta}{Item Title}, \textcolor{blue}{Item Embedding}]). Choose one "Title" to\\
 & to buy next from the following item "Title" set:& buy next from the following item "Title" set:  & recommend for this user to buy next from the following\\
  &  [Candidate \textcolor{magenta}{Item Titles}]. & [Candidate \textcolor{magenta}{Item Titles}, \textcolor{blue}{Item Embeddings}].&  item "Title" set: [Candidate \textcolor{magenta}{Item Titles}, \textcolor{blue}{Item Embeddings}].\\ \midrule
  
\textbf{Outputs}  &\multirow{2}{*}{Item Title} &\multirow{2}{*}{Item Title} &\multirow{2}{*}{Item Title} \\
$(\text{Text}(i_{n_u+1}^{(u)}))$  & & & \\ \bottomrule

\end{tabular}}
\label{tab title generation prompt}
\vspace{-1.5ex}
\end{table*}
```

## Table 2
```latex
\begin{table*}[h]
% \small
% \caption[Caption for LOF]{An example of prompt for next item retrieval task for LLM4Rec models (i.e., TALLRec, LLaRA, CoLLM, and A-LLMRec).}
% \resizebox{1.0\linewidth}{!}{
% \begin{tabular}{c|l|l|l}
% \toprule
%  \multicolumn{1}{c|}{}  & \multicolumn{1}{c|}{\textbf{TALLRec/LLaRA}} & \multicolumn{1}{c|}{\textbf{LLaRA}} & \multicolumn{1}{c}{\textbf{CoLLM/A-LLMRec}} \\ \midrule\midrule
% \multirow{5}{*}{\textbf{User}} & This user has made a series of purchases& This user has made a series of purchases in the & This is user representation from recommendation models: \\ 
%   & in the following order: (History Item List: & following order: (History Item List: [No.\# Time:& \textcolor{red}{[UserRep]}, and this user has made a series of purchases in\\  
%   &[No.\#  Time: YYYY/MM/DD Title: \textcolor{magenta}{Item Title}]).  & YYYY/MM/DD Title: \textcolor{magenta}{Item Title}, \textcolor{blue}{Embedding}]). & the following order: (History Item List: [No.\# Time: YYYY/\\
%   &Based on this sequence of purchases, generate & Based on this sequence of purchases, generate & MM/DD Title: \textcolor{magenta}{Item Title}, \textcolor{blue}{Embedding}]). Based on this\\
%  &user representation token: \textcolor{brown}{[UserOut]}. & user representation token: \textcolor{brown}{[UserOut]}. &  sequence of purchases and user representation, generate\\
%   &  & &  user representation token: \textcolor{brown}{[UserOut]}.\\ \midrule

%     \multirow{2}{*}{\textbf{Item}} & The item title is as follows: "Title": \textcolor{magenta}{Item Title}, then & \multicolumn{2}{l}{The item title and item embedding are as follows: "Title": \textcolor{magenta}{Item Title}, \textcolor{blue}{Embedding},} \\
%     &generate item representation token: \textcolor{violet}{[ItemOut]}. & \multicolumn{2}{l}{then generate item representation token: \textcolor{violet}{[ItemOut]}} \\ \bottomrule
% \end{tabular}}
% \label{tab next item retrieval prompt}
% \end{table*}
```

## Table 3
```latex
\begin{table*}[h]
\small
\caption{An example prompt for various LLM4Rec models (Next Item Retrieval approach).
% (i.e., TALLRec, LLaRA, CoLLM, and A-LLMRec).
}
\vspace{-2ex}
\resizebox{0.95\linewidth}{!}{
\begin{tabular}{c|l|l|l}
\toprule
 \multicolumn{1}{c|}{}  & \multicolumn{1}{c|}{(a) \textbf{TALLRec}} & \multicolumn{1}{c|}{(b) \textbf{LLaRA/\proposed~(Ours)}} & \multicolumn{1}{c}{(c) \textbf{CoLLM/A-LLMRec}} \\ \midrule\midrule
\multirow{3}{*}{\textbf{User}} & This user has made a series of purchases& This user has made a series of purchases in the & This is user representation from recommendation models: \\ 
  & in the following order: (History Item List: & following order: (History Item List: [No.\# Time:& \textcolor{red}{[User Representation]}, and this user has made a series of purchases in\\  
  \multirow{2}{*}{$(\mathcal{P}^u_{\mathcal{U}})$}&[No.\#  Time: YYYY/MM/DD Title: \textcolor{magenta}{Item Title}]).  & YYYY/MM/DD Title: \textcolor{magenta}{Item Title}, \textcolor{blue}{Item Embedding}]). & the following order: (History Item List: [No.\# Time: YYYY/\\
  &Based on this sequence of purchases, generate & Based on this sequence of purchases, generate & MM/DD Title: \textcolor{magenta}{Item Title}, \textcolor{blue}{Item Embedding}]). Based on this\\
 &user representation token: \textcolor{brown}{[UserOut]}. & user representation token: \textcolor{brown}{[UserOut]}. &  sequence of purchases and user representation, generate\\
  &  & &  user representation token: \textcolor{brown}{[UserOut]}.\\ \midrule

    \textbf{Item} & The item title is as follows: "Title": \textcolor{magenta}{Item Title}, then & \multicolumn{2}{l}{The item title and item embedding are as follows: "Title": \textcolor{magenta}{Item Title}, \textcolor{blue}{Item Embedding}, then generate item representation} \\
    $(\mathcal{P}^i_{\mathcal{I}})$&generate item representation token: \textcolor{violet}{[ItemOut]}. & \multicolumn{2}{l}{token: \textcolor{violet}{[ItemOut]}} \\ \bottomrule
\end{tabular}}
\label{tab next item retrieval prompt}
\vspace{-1.5ex}
\end{table*}
```

## Table 4
```latex
\begin{table*}[t]

% \caption{Performance of various models when trained with original sequences and shuffled sequences (Next Item Retrieval approach). Change ratio indicates the performance change of `Shuffle' compared with `Original'.
% % The ratio of performance change is reported in bracket.
% }
% \vspace{-2ex}
% \resizebox{0.82\linewidth}{!}{
% \begin{tabular}{c|c||cccc||cccc||cccc}
% \toprule
% \multirow{2}{*}{} & \multirow{2}{*}{} & \multicolumn{4}{c||}{Scientific} & \multicolumn{4}{c||}{Electronics}& \multicolumn{4}{c}{CDs}\\ \cmidrule{3-14}
%   & & \multicolumn{1}{c|}{NDCG@10} &  \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20  & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20 & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20  \\ \midrule\midrule

% \multirow{3}{*}{SASRec} & Original    & \multicolumn{1}{c|}{0.2918}  & \multicolumn{1}{c|}{0.3245}  & \multicolumn{1}{c|}{0.4691} & 0.5987& \multicolumn{1}{c|}{0.2267}  & \multicolumn{1}{c|}{0.2606}  & \multicolumn{1}{c|}{0.3749} & 0.5096 & \multicolumn{1}{c|}{0.3451}  & \multicolumn{1}{c|}{0.3795}  & \multicolumn{1}{c|}{0.5278} & 0.6635 \\ 
% & \multirow{1}{*}{Shuffle}    & \multicolumn{1}{c|}{0.2688}  & \multicolumn{1}{c|}{0.3014}  & \multicolumn{1}{c|}{0.4399} & 0.5652 & \multicolumn{1}{c|}{0.2104}  & \multicolumn{1}{c|}{0.2397}  & \multicolumn{1}{c|}{0.3547} & 0.4798 & \multicolumn{1}{c|}{0.3312} & \multicolumn{1}{c|}{0.3632} & \multicolumn{1}{c|}{0.5036} & 0.6340 \\ \cmidrule{2-14}
% & \multirow{1}{*}{Change ratio} & \multicolumn{1}{c|}{(-7.88\%)}  & \multicolumn{1}{c|}{(-7.12\%)}  & \multicolumn{1}{c|}{(-6.22\%)} & (-5.60\%) & \multicolumn{1}{c|}{(-7.19\%)}  & \multicolumn{1}{c|}{(-8.02\%)}  & \multicolumn{1}{c|}{(-5.39\%)} & (-5.85\%) & \multicolumn{1}{c|}{(-4.03\%)} & \multicolumn{1}{c|}{(-4.30\%)} & \multicolumn{1}{c|}{(-4.59\%)} & (-4.45\%)\\ 
% \midrule\midrule

% \multirow{3}{*}{TALLRec} & Original  & \multicolumn{1}{c|}{0.2585}  & \multicolumn{1}{c|}{0.3048}  & \multicolumn{1}{c|}{0.4574} & 0.6276 & \multicolumn{1}{c|}{0.2249}  & \multicolumn{1}{c|}{0.2670}  & \multicolumn{1}{c|}{0.3802} & 0.5476& \multicolumn{1}{c|}{0.3100}  & \multicolumn{1}{c|}{0.3493}  & \multicolumn{1}{c|}{0.5052} & 0.6633 \\ 
% &\multirow{1}{*}{Shuffle}    & \multicolumn{1}{c|}{0.2579}  & \multicolumn{1}{c|}{0.3011}  & \multicolumn{1}{c|}{0.4559} & 0.6267 & \multicolumn{1}{c|}{0.2223}  & \multicolumn{1}{c|}{0.2642}  & \multicolumn{1}{c|}{0.3752} & 0.5421& \multicolumn{1}{c|}{0.3003}  & \multicolumn{1}{c|}{0.3407}  & \multicolumn{1}{c|}{0.5001} & 0.6599 \\ \cmidrule{2-14}
% & \multirow{1}{*}{Change ratio} & \multicolumn{1}{c|}{(-0.23\%)}  & \multicolumn{1}{c|}{(-1.21\%)}  & \multicolumn{1}{c|}{(-0.33\%)} & (-0.14\%) & \multicolumn{1}{c|}{(-1.16\%)}  & \multicolumn{1}{c|}{(-1.05\%)}  & \multicolumn{1}{c|}{(-1.32\%)} & (-1.00\%) & \multicolumn{1}{c|}{(-3.13\%)} & \multicolumn{1}{c|}{(-2.46\%)} & \multicolumn{1}{c|}{(-1.01\%)} & (-0.51\%)\\

% \midrule\midrule
% \multirow{3}{*}{LLaRA} & Original       & \multicolumn{1}{c|}{0.2844}  & \multicolumn{1}{c|}{0.3265}  & \multicolumn{1}{c|}{0.4993} & 0.6658 & \multicolumn{1}{c|}{0.2048}  & \multicolumn{1}{c|}{0.2454}  & \multicolumn{1}{c|}{0.3428} & 0.5048& \multicolumn{1}{c|}{0.2464}  & \multicolumn{1}{c|}{0.2951}  & \multicolumn{1}{c|}{0.4665} & 0.6590 \\ 
% & \multirow{1}{*}{Shuffle}      & \multicolumn{1}{c|}{0.2921}  & \multicolumn{1}{c|}{0.3345}  & \multicolumn{1}{c|}{0.5077} & 0.6757 & \multicolumn{1}{c|}{0.2079}  & \multicolumn{1}{c|}{0.2474}  & \multicolumn{1}{c|}{0.3432} & 0.5009& \multicolumn{1}{c|}{0.2695}        & \multicolumn{1}{c|}{0.3106}        & \multicolumn{1}{c|}{0.4608}       & 0.6423  \\ \cmidrule{2-14}
% & \multirow{1}{*}{Change ratio} & \multicolumn{1}{c|}{(+2.71\%)}  & \multicolumn{1}{c|}{(+2.45\%)}  & \multicolumn{1}{c|}{(+1.68\%)} & (+1.49\%) & \multicolumn{1}{c|}{(+1.51\%)}  & \multicolumn{1}{c|}{(+0.81\%)}  & \multicolumn{1}{c|}{(+0.12\%)} & (-0.77\%) & \multicolumn{1}{c|}{(+9.38\%)} & \multicolumn{1}{c|}{(+5.25\%)} & \multicolumn{1}{c|}{(-1.22\%)} & (-2.53\%)\\

% \midrule\midrule
% \multirow{3}{*}{CoLLM} & Original   & \multicolumn{1}{c|}{0.3111}  & \multicolumn{1}{c|}{0.3489}  & \multicolumn{1}{c|}{0.5182} & 0.6676 & \multicolumn{1}{c|}{0.2565}  & \multicolumn{1}{c|}{0.2946}  & \multicolumn{1}{c|}{0.4256} & 0.5773& \multicolumn{1}{c|}{0.3145}  & \multicolumn{1}{c|}{0.3556}  & \multicolumn{1}{c|}{0.5316} & 0.6944 \\ 
% & \multirow{1}{*}{Shuffle}     & \multicolumn{1}{c|}{0.3181}  & \multicolumn{1}{c|}{0.3545}  & \multicolumn{1}{c|}{0.5301} & 0.6741 & \multicolumn{1}{c|}{0.2636}  & \multicolumn{1}{c|}{0.2999}  & \multicolumn{1}{c|}{0.4218} & 0.5663& \multicolumn{1}{c|}{0.3143}  & \multicolumn{1}{c|}{0.3558}  & \multicolumn{1}{c|}{0.5306} & 0.6947 \\ \cmidrule{2-14}
% & \multirow{1}{*}{Change ratio} & \multicolumn{1}{c|}{(+2.25\%)}  & \multicolumn{1}{c|}{(+1.61\%)}  & \multicolumn{1}{c|}{(+2.30\%)} & (+0.97\%) & \multicolumn{1}{c|}{(+2.77\%)}  & \multicolumn{1}{c|}{(+1.80\%)}  & \multicolumn{1}{c|}{(-0.89\%)} & (-1.91\%) & \multicolumn{1}{c|}{(-0.29\%)} & \multicolumn{1}{c|}{(+0.03\%)} & \multicolumn{1}{c|}{(+0.30\%)} & (+0.75\%)\\

% \midrule\midrule
% \multirow{3}{*}{A-LLMRec} & Original & \multicolumn{1}{c|}{0.2875}  & \multicolumn{1}{c|}{0.3246}  & \multicolumn{1}{c|}{0.4957} & 0.6427 & \multicolumn{1}{c|}{0.2791}  & \multicolumn{1}{c|}{0.3173}  & \multicolumn{1}{c|}{0.4622} & 0.6137& \multicolumn{1}{c|}{0.3119}  & \multicolumn{1}{c|}{0.3526}  & \multicolumn{1}{c|}{0.5300} & 0.6914 \\ 
% &\multirow{1}{*}{Shuffle}         & \multicolumn{1}{c|}{0.2973}  & \multicolumn{1}{c|}{0.3348}  & \multicolumn{1}{c|}{0.5080} & 0.6558& \multicolumn{1}{c|}{0.2741}  & \multicolumn{1}{c|}{0.3113}  & \multicolumn{1}{c|}{0.4560} & 0.6037 & \multicolumn{1}{c|}{0.3078}  & \multicolumn{1}{c|}{0.3471}  & \multicolumn{1}{c|}{0.5272} & 0.6887 \\ \cmidrule{2-14}
% & \multirow{1}{*}{Change ratio} & \multicolumn{1}{c|}{(+3.41\%)}  & \multicolumn{1}{c|}{(+3.14\%)}  & \multicolumn{1}{c|}{(+2.48\%)} & (+2.04\%) & \multicolumn{1}{c|}{(-1.79\%)}  & \multicolumn{1}{c|}{(-1.89\%)}  & \multicolumn{1}{c|}{(-1.31\%)} & (-1.63\%) & \multicolumn{1}{c|}{(-1.31\%)} & \multicolumn{1}{c|}{(-1.56\%)} & \multicolumn{1}{c|}{(-0.53\%)} & (-0.39\%)\\

% \midrule\midrule
% \multirow{3}{*}{\proposed} & Original  & \multicolumn{1}{c|}{0.3388}  & \multicolumn{1}{c|}{0.3758}  & \multicolumn{1}{c|}{0.5532} & 0.6992 & \multicolumn{1}{c|}{0.3044}  & \multicolumn{1}{c|}{0.3424}  & \multicolumn{1}{c|}{0.4885} & 0.6385& \multicolumn{1}{c|}{0.3809}  & \multicolumn{1}{c|}{0.4158}  & \multicolumn{1}{c|}{0.6085} & 0.7461 \\ 
% & \multirow{1}{*}{Shuffle}    & \multicolumn{1}{c|}{0.3224}  & \multicolumn{1}{c|}{0.3591}  & \multicolumn{1}{c|}{0.5287} & 0.6739& \multicolumn{1}{c|}{0.2838}  & \multicolumn{1}{c|}{0.3210}  & \multicolumn{1}{c|}{0.4552} & 0.6030 & \multicolumn{1}{c|}{0.3614}  & \multicolumn{1}{c|}{0.3981}  & \multicolumn{1}{c|}{0.5807} & 0.7111 \\ \cmidrule{2-14}
% & \multirow{1}{*}{Change ratio}  & \multicolumn{1}{c|}{(-4.84\%)}  & \multicolumn{1}{c|}{(-4.44\%)}  & \multicolumn{1}{c|}{(-4.29\%)} & (-3.62\%) & \multicolumn{1}{c|}{(-6.77\%)}  & \multicolumn{1}{c|}{(-6.25\%)}  & \multicolumn{1}{c|}{(-6.82\%)} & (-5.56\%) & \multicolumn{1}{c|}{(-5.12\%)} & \multicolumn{1}{c|}{(-4.26\%)} & \multicolumn{1}{c|}{(-4.57\%)} & (-4.69\%) \\

% \bottomrule
% \end{tabular}}
% \label{tab: shuffle train}
% \vspace{-2ex}
% \end{table*}
```

## Table 5
```latex
\begin{table*}[]

% \caption{Performance of various models when trained with original sequences and shuffled sequences (Next Item Retrieval approach). Change ratio indicates the performance change of `Shuffle' compared with `Original'.
% % The ratio of performance change is reported in bracket.
% }
% \vspace{-2ex}
% \resizebox{0.95\linewidth}{!}{

% \begin{tabular}{c|c||ccc||ccc||ccc||ccc||ccc||ccc}
% \toprule
% \multirow{2}{*}{Dataset}            & \multirow{2}{*}{Metric} & \multicolumn{3}{c|}{SASRec}                                                 & \multicolumn{3}{c||}{TALLRec}                                                & \multicolumn{3}{c||}{LLaRA}                                                  & \multicolumn{3}{c||}{CoLLM}                                                  & \multicolumn{3}{c||}{A-LLMRec}                                               & \multicolumn{3}{c}{\proposed}                                               \\ \cmidrule{3-20} 
%      &                   & \multicolumn{1}{c|}{Original} & \multicolumn{1}{c|}{Shuffle} & Change ratio & \multicolumn{1}{c|}{Original} & \multicolumn{1}{c|}{Shuffle} & Change ratio & \multicolumn{1}{c|}{Original} & \multicolumn{1}{c|}{Shuffle} & Change ratio & \multicolumn{1}{c|}{Original} & \multicolumn{1}{c|}{Shuffle} & Change ratio & \multicolumn{1}{c|}{Original} & \multicolumn{1}{c|}{Shuffle} & Change ratio & \multicolumn{1}{c|}{Original} & \multicolumn{1}{c|}{Shuffle} & Change ratio \\ \midrule\midrule
% \multirow{2}{*}{Scientific}  & NDCG@10           & \multicolumn{1}{c|}{0.2918}         & \multicolumn{1}{c|}{0.2688}        &   (-7.88\%)     & \multicolumn{1}{c|}{0.2585}         & \multicolumn{1}{c|}{0.2579}        &         (-0.23\%) & \multicolumn{1}{c|}{0.2844}         &  \multicolumn{1}{c|}{0.2921}        &   (+2.71\%)      & \multicolumn{1}{c|}{0.3111}         & \multicolumn{1}{c|}{0.3181}        &     (+2.25\%)   & \multicolumn{1}{c|}{0.2875}         & \multicolumn{1}{c|}{0.2973}        &  (+3.41\%)  & \multicolumn{1}{c|}{0.3388}         & \multicolumn{1}{c|}{0.3224}        &     (-4.84\%)    \\ \cmidrule{2-20} 
%      & NDCG@20           & \multicolumn{1}{c|}{0.3245}         & \multicolumn{1}{c|}{0.3014}        &   (-7.12\%)     & \multicolumn{1}{c|}{0.3048}         & \multicolumn{1}{c|}{0.3011}        &    (-1.21\%)     & \multicolumn{1}{c|}{0.3265}         & \multicolumn{1}{c|}{0.3345}        &      (+2.45\%)  & \multicolumn{1}{c|}{0.3489}         & \multicolumn{1}{c|}{0.3545}        &    (+1.61\%)    & \multicolumn{1}{c|}{0.3246}         & \multicolumn{1}{c|}{0.3348}        &    (+3.14\%)    & \multicolumn{1}{c|}{0.3758}         & \multicolumn{1}{c|}{0.3591}        &       (-4.44\%)  \\ \midrule\midrule
% \multirow{2}{*}{Electronics} & NDCG@10           & \multicolumn{1}{c|}{0.2267}         & \multicolumn{1}{c|}{0.2104}        &     (-7.19\%)   & \multicolumn{1}{c|}{0.2249}         & \multicolumn{1}{c|}{0.2223}        &   (-1.16\%) & \multicolumn{1}{c|}{0.2048}         & \multicolumn{1}{c|}{0.2079}        &   (+1.51\%)     & \multicolumn{1}{c|}{0.2565}         & \multicolumn{1}{c|}{0.2636}        &    (+2.77\%)    & \multicolumn{1}{c|}{0.2791}         & \multicolumn{1}{c|}{0.2741}        &    (-1.79\%)   & \multicolumn{1}{c|}{0.3044}         & \multicolumn{1}{c|}{0.2838}        &    (-6.77\%)     \\ \cmidrule{2-20} 
%      & NDCG@20           & \multicolumn{1}{c|}{0.2606}         & \multicolumn{1}{c|}{0.2397}        &    (-8.02\%)     & \multicolumn{1}{c|}{0.2670}         & \multicolumn{1}{c|}{0.2642}        &   (-1.05\%)    & \multicolumn{1}{c|}{0.2454}         & \multicolumn{1}{c|}{0.2474}        &     (+0.81\%)   & \multicolumn{1}{c|}{0.2946}         & \multicolumn{1}{c|}{0.2999}        &    (+1.80\%)     & \multicolumn{1}{c|}{0.3173}         & \multicolumn{1}{c|}{0.3113}        &   (-1.89\%)     & \multicolumn{1}{c|}{0.3424}         & \multicolumn{1}{c|}{0.3210}        &       (-6.25\%)  \\ \midrule\midrule
% \multirow{2}{*}{CDs}         & NDCG@10           & \multicolumn{1}{c|}{0.3451}         & \multicolumn{1}{c|}{0.3312}        &     (-4.03\%)   & \multicolumn{1}{c|}{0.3100}         & \multicolumn{1}{c|}{0.3003}        &   (-3.13\%) & \multicolumn{1}{c|}{0.2464}         & \multicolumn{1}{c|}{0.2695}        &   (+9.38\%)      & \multicolumn{1}{c|}{0.3145}         & \multicolumn{1}{c|}{0.3143}        &      (-0.29\%)  & \multicolumn{1}{c|}{0.3119}         & \multicolumn{1}{c|}{0.3078}        &   (-1.31\%)  & \multicolumn{1}{c|}{0.3809}         & \multicolumn{1}{c|}{0.3614}        &    (-5.16\%)   \\ \cmidrule{2-20} 
%      & NDCG@20           & \multicolumn{1}{c|}{0.3795}         & \multicolumn{1}{c|}{0.3632}        &   (-4.03\%)       & \multicolumn{1}{c|}{0.3493}         & \multicolumn{1}{c|}{0.3407}        &    (-2.46\%)    & \multicolumn{1}{c|}{0.2951}         & \multicolumn{1}{c|}{0.3106}        &    (+5.25\%)   & \multicolumn{1}{c|}{0.3556}         & \multicolumn{1}{c|}{0.3558}        &    (+0.03\%)      & \multicolumn{1}{c|}{0.3526}         & \multicolumn{1}{c|}{0.3471}        &    (-1.56\%)      & \multicolumn{1}{c|}{0.4158}         & \multicolumn{1}{c|}{0.3981}        &      (-4.26\%)   \\ \bottomrule
% \end{tabular}}
% \label{tab: shuffle train}
% % \vspace{-2ex}
% \end{table*}
```

## Table 6
```latex
\begin{table}[t]
\caption{Performance (NDCG@10) of various models when trained with original sequences and shuffled sequences (Next Item Retrieval approach). Change ratio indicates the performance change of `Shuffle' compared with `Original'.
% The ratio of performance change is reported in bracket.
}
\vspace{-1ex}
\resizebox{0.85\linewidth}{!}{
\begin{tabular}{c|c||c|c|c}
\toprule
         &  & Scientific & Electronics & CDs    \\ \midrule \midrule
\multirow{3}{*}{SASRec} &Original    & 0.2918  & 0.2267  & 0.3451 \\ 
&\multirow{1}{*}{Shuffle} & 0.2688 & 0.2104 &0.3312\\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} &  (-7.88\%) & (-7.19\%) &  (-4.03\%) \\
\midrule \midrule

\multirow{3}{*}{TALLRec} & Original   & 0.2585  & 0.2249 & 0.3100 \\
&\multirow{1}{*}{Shuffle} & 0.2579 & 0.2223  & 0.3003 \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} &  (-0.23\%) & (-1.16\%) &  (-3.13\%) \\
\midrule \midrule

\multirow{3}{*}{LLaRA} & Original     & 0.2844     & 0.2048  & 0.2464 \\ 
&\multirow{1}{*}{Shuffle} & 0.2921 & 0.2079  & 0.2695  \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} & (+2.71\%) & (+1.51\%) & (+9.38\%) \\
\midrule \midrule

\multirow{3}{*}{CoLLM} &Original & 0.3111 & 0.2565   & 0.3152 \\ 
&\multirow{1}{*}{Shuffle} & 0.3181 & 0.2636  & 0.3143  \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} & (+2.25\%) & (+2.77\%) & (-0.29\%) \\
\midrule \midrule

\multirow{3}{*}{A-LLMRec} & Original  & 0.2875  & 0.2791  & 0.3119 \\
&\multirow{1}{*}{Shuffle} & 0.2973  & 0.2741  & 0.3078  \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} & (+3.41\%) & (-1.79\%) & (-1.31\%) \\
\midrule \midrule

\multirow{3}{*}{\proposed} & Original  & 0.3388  & 0.3044  & 0.3809 \\
&\multirow{1}{*}{Shuffle} & 0.3224  & 0.2838  & 0.3614  \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} & (-4.84\%) & (-6.77\%) & (-5.11\%) \\
\bottomrule

\end{tabular}}
\label{tab: shuffle train}
\vspace{-1ex}
\end{table}
```

## Table 7
```latex
\begin{table}[t]
% \caption{Performance comparison and performance change rate (in bracket) of Next Item Title Generation approach between models trained on the original sequence and trained on the shuffled sequence (HR@1).}
\caption{Performance (HR@1) of various models when trained with original sequences and shuffled sequences (Next Item Title Generation approach).
% The ratio of performance change is reported in bracket.
}
\vspace{-1ex}
\resizebox{0.85\linewidth}{!}{
\begin{tabular}{c|c||c|c|c}
\toprule
         &  & Scientific & Electronics & CDs    \\ \midrule \midrule
\multirow{3}{*}{SASRec} &Original    & 0.3171  & 0.2390  & 0.3662 \\ 
&\multirow{1}{*}{Shuffle} & 0.2821 & 0.2158 &0.3386\\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} &  (-11.04\%) & (-9.71\%) &  (-7.54\%) \\
\midrule \midrule

\multirow{3}{*}{TALLRec} & Original   & 0.2221  & 0.1787 & 0.2589 \\
&\multirow{1}{*}{Shuffle} & 0.2181 & 0.1815  & 0.2728 \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} &  (-1.81\%) & (+1.57\%) &  (+5.37\%) \\
\midrule \midrule

\multirow{3}{*}{LLaRA} & Original     & 0.3022     & 0.2616  & 0.3142 \\ 
&\multirow{1}{*}{Shuffle} & 0.2996 & 0.2650  & 0.3530  \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} & (-0.86\%) & (+1.30\%) & (+12.35\%) \\
\midrule \midrule

\multirow{3}{*}{CoLLM} &Original & 0.3010 & 0.2311   & 0.3447 \\ 
&\multirow{1}{*}{Shuffle} & 0.3165 & 0.2323  & 0.3763  \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} & (+5.15\%) & (+0.52\%) & (+9.17\%) \\
\midrule \midrule

\multirow{3}{*}{A-LLMRec} & Original  & 0.2804  & 0.2672  & 0.3319 \\
&\multirow{1}{*}{Shuffle} & 0.2796  & 0.2684  & 0.3528  \\ \cmidrule{2-5}
&\multirow{1}{*}{Change ratio} & (-0.29\%) & (+0.45\%) & (+6.30\%) \\
\bottomrule

\end{tabular}}
\label{tab: shuffle train - title generation}
\vspace{-1.5ex}
\end{table}
```

## Table 8
```latex
\begin{table}[t]
\caption{Cosine similarity between user representations obtained based on original sequences and
those obtained based on shuffled sequences during inference (The models are trained on the original sequences).}
\vspace{-1ex}
\resizebox{0.8\linewidth}{!}{
\begin{tabular}{c||c|c|c|c}
\toprule
         & Movies & Scientific & Electronics & CDs    \\ \midrule\midrule
SASRec   & 0.6535 & 0.7375     & 0.7083      & 0.7454 \\ \midrule
TALLRec  & 0.9731 & 0.9326     & 0.9678      & 0.9570 \\ \midrule
LLaRA    & 0.9639 & 0.9424     & 0.9800      & 0.9624 \\ \midrule
CoLLM    & 0.9067 & 0.9263     & 0.8921      & 0.9526 \\ \midrule
A-LLMRec & 0.8872 & 0.8911     & 0.8623      & 0.8706 \\ \midrule
\proposed & 0.6128 & 0.7852     & 0.7393      & 0.8589 \\ \bottomrule
\end{tabular}}
\label{tab: user similarity}
\vspace{-2.25ex}
\end{table}
```

## Table 9
```latex
\begin{table*}[t]
\caption{Overall model performance. The best performance is denoted in bold.}
\vspace{-2ex}
\resizebox{0.875\linewidth}{!}{
\begin{tabular}{c|c||cccc||cc||ccccc}
\toprule
\multirow{2}{*}{Dataset} & \multirow{2}{*}{Metric} & \multicolumn{4}{c||}{CF-SRec}                                                           & \multicolumn{2}{c||}{LM-based}                                   & \multicolumn{5}{c}{LLM4Rec}                                                                                                      \\ \cmidrule{3-13} 
&                   & \multicolumn{1}{c|}{GRU4Rec} & \multicolumn{1}{c|}{BERT4Rec} & \multicolumn{1}{c|}{NextItNet} & SASRec & \multicolumn{1}{c|}{CTRL} & RECFORMER & \multicolumn{1}{c|}{TALLRec} & \multicolumn{1}{c|}{LLaRA} & \multicolumn{1}{c|}{CoLLM} & \multicolumn{1}{c|}{A-LLMRec} & \proposed \\ \midrule\midrule
\multirow{4}{*}{Movies} & NDCG@10           & \multicolumn{1}{c|}{0.3152}        & \multicolumn{1}{c|}{0.2959}         & \multicolumn{1}{c|}{0.2538}          & 0.3459 & \multicolumn{1}{c|}{0.2785} &   0.2068  & \multicolumn{1}{c|}{0.1668}        & \multicolumn{1}{c|}{0.1522}      & \multicolumn{1}{c|}{0.3223}      & \multicolumn{1}{c|}{0.3263}         &  \textbf{0.3560} \\ \cline{2-13} 
  & NDCG@20           & \multicolumn{1}{c|}{0.3494}        & \multicolumn{1}{c|}{0.3303}         & \multicolumn{1}{c|}{0.2879}          &  0.3745 & \multicolumn{1}{c|}{0.3099} &    0.2337  & \multicolumn{1}{c|}{0.2126}        & \multicolumn{1}{c|}{0.1944}      & \multicolumn{1}{c|}{0.3577}      & \multicolumn{1}{c|}{0.3629}         & \textbf{0.3924}  \\ \cline{2-13} 
  & HR@10             & \multicolumn{1}{c|}{0.4883}        & \multicolumn{1}{c|}{0.4785}         & \multicolumn{1}{c|}{0.4221}          & 0.5180  & \multicolumn{1}{c|}{0.4264} &    0.3569  & \multicolumn{1}{c|}{0.3234}        & \multicolumn{1}{c|}{0.2914}      & \multicolumn{1}{c|}{0.5089}      & \multicolumn{1}{c|}{0.5127}         & \textbf{0.5569} \\ \cline{2-13} 
  & HR@20             & \multicolumn{1}{c|}{0.6245}        & \multicolumn{1}{c|}{0.6213}         & \multicolumn{1}{c|}{0.5522}          &  0.6310 & \multicolumn{1}{c|}{0.5429} &    0.5264  & \multicolumn{1}{c|}{0.5060}        & \multicolumn{1}{c|}{0.4599}      & \multicolumn{1}{c|}{0.6491}      & \multicolumn{1}{c|}{0.6577}         & \textbf{0.7010} \\ \midrule\midrule
\multirow{4}{*}{Scientific} & NDCG@10           & \multicolumn{1}{c|}{0.2642}        & \multicolumn{1}{c|}{0.2576}         & \multicolumn{1}{c|}{0.2263}& 0.2918 & \multicolumn{1}{c|}{0.2152} &   0.2907    & \multicolumn{1}{c|}{0.2585}        & \multicolumn{1}{c|}{0.2844}      & \multicolumn{1}{c|}{0.3111}      & \multicolumn{1}{c|}{0.2875}         &   \textbf{0.3388}  \\ \cline{2-13} 
  & NDCG@20           & \multicolumn{1}{c|}{0.2974}        & \multicolumn{1}{c|}{0.2913}         & \multicolumn{1}{c|}{0.2657}          &  0.3245  & \multicolumn{1}{c|}{0.2520} &  0.3113  & \multicolumn{1}{c|}{0.3048}        & \multicolumn{1}{c|}{0.3265}      & \multicolumn{1}{c|}{0.3489}      & \multicolumn{1}{c|}{0.3246}         & \textbf{0.3758} \\ \cline{2-13} 
  & HR@10             & \multicolumn{1}{c|}{0.4313}        & \multicolumn{1}{c|}{0.4437}         & \multicolumn{1}{c|}{0.3908}          & 0.4691 & \multicolumn{1}{c|}{0.3520} &    0.4506  & \multicolumn{1}{c|}{0.4574}        & \multicolumn{1}{c|}{0.4993}      & \multicolumn{1}{c|}{0.5182}      & \multicolumn{1}{c|}{0.4957}         & \textbf{0.5532}  \\ \cline{2-13} 
  & HR@20             & \multicolumn{1}{c|}{0.5524}        & \multicolumn{1}{c|}{0.5822}         & \multicolumn{1}{c|}{0.5356}          & 0.5987   & \multicolumn{1}{c|}{0.4882} &    0.5710  & \multicolumn{1}{c|}{0.6276}        & \multicolumn{1}{c|}{0.6658}      & \multicolumn{1}{c|}{0.6676}      & \multicolumn{1}{c|}{0.6427}         & \textbf{0.6992} \\ \midrule\midrule
\multirow{4}{*}{Electronics} & NDCG@10           & \multicolumn{1}{c|}{0.2364}        & \multicolumn{1}{c|}{0.1867}         & \multicolumn{1}{c|}{0.1712}          &   0.2267 & \multicolumn{1}{c|}{0.1680} &  0.2032   & \multicolumn{1}{c|}{0.2249}        & \multicolumn{1}{c|}{0.2048}      & \multicolumn{1}{c|}{0.2565}      & \multicolumn{1}{c|}{0.2791}         & \textbf{0.3044} \\ \cline{2-13} 
  & NDCG@20           & \multicolumn{1}{c|}{0.2743}        & \multicolumn{1}{c|}{0.2172}         & \multicolumn{1}{c|}{0.2069}          &  0.2606 & \multicolumn{1}{c|}{0.2003} &   0.2441  & \multicolumn{1}{c|}{0.2670}        & \multicolumn{1}{c|}{0.2454}      & \multicolumn{1}{c|}{0.2948}      & \multicolumn{1}{c|}{0.3173}         & \textbf{0.3424} \\ \cline{2-13} 
  & HR@10             & \multicolumn{1}{c|}{0.3843}        & \multicolumn{1}{c|}{0.3325}         & \multicolumn{1}{c|}{0.3017}          &  0.3749  & \multicolumn{1}{c|}{0.2861} &    0.3586 & \multicolumn{1}{c|}{0.3802}        & \multicolumn{1}{c|}{0.3441}      & \multicolumn{1}{c|}{0.4236}      & \multicolumn{1}{c|}{0.4622}         & \textbf{0.4885} \\ \cline{2-13} 
  & HR@20             & \multicolumn{1}{c|}{0.5196}        & \multicolumn{1}{c|}{0.4740}         & \multicolumn{1}{c|}{0.4324}          & 0.5096  & \multicolumn{1}{c|}{0.4152} &    0.5213  & \multicolumn{1}{c|}{0.5476}        & \multicolumn{1}{c|}{0.5032}      & \multicolumn{1}{c|}{0.5741}      & \multicolumn{1}{c|}{0.6137}         & \textbf{0.6385} \\ \midrule\midrule
\multirow{4}{*}{CDs} & NDCG@10           & \multicolumn{1}{c|}{0.2155}        & \multicolumn{1}{c|}{0.3019}         & \multicolumn{1}{c|}{0.2207}          &  0.3451  & \multicolumn{1}{c|}{0.2968} &   0.3238   & \multicolumn{1}{c|}{0.3100}        & \multicolumn{1}{c|}{0.2464}      & \multicolumn{1}{c|}{0.3152}      & \multicolumn{1}{c|}{0.3119}         &  \textbf{0.3809}\\ \cline{2-13} 
  & NDCG@20           & \multicolumn{1}{c|}{0.2530}        & \multicolumn{1}{c|}{0.3386}         & \multicolumn{1}{c|}{0.2562}          & 0.3795  & \multicolumn{1}{c|}{0.3316} &    0.3642   & \multicolumn{1}{c|}{0.3493}        & \multicolumn{1}{c|}{0.2951}      & \multicolumn{1}{c|}{0.3557}      & \multicolumn{1}{c|}{0.3526}         & \textbf{0.4158}  \\ \cline{2-13} 
  & HR@10             & \multicolumn{1}{c|}{0.3712}        & \multicolumn{1}{c|}{0.5018}         & \multicolumn{1}{c|}{0.3842}          & 0.5278  & \multicolumn{1}{c|}{0.4574} &     0.5140  & \multicolumn{1}{c|}{0.5052}        & \multicolumn{1}{c|}{0.4665}      & \multicolumn{1}{c|}{0.5290}      & \multicolumn{1}{c|}{0.5300}         & \textbf{0.6085}  \\ \cline{2-13} 
  & HR@20             & \multicolumn{1}{c|}{0.5092}        & \multicolumn{1}{c|}{0.6605}         & \multicolumn{1}{c|}{0.5422}          & 0.6635  & \multicolumn{1}{c|}{0.5957} & 0.6739 & \multicolumn{1}{c|}{0.6633}        & \multicolumn{1}{c|}{0.6590}      & \multicolumn{1}{c|}{0.6895}      & \multicolumn{1}{c|}{0.6914}         & \textbf{0.7461} \\ \bottomrule
\end{tabular}}
\label{tab: overall performance}
\vspace{-1.5ex}
\end{table*}
```

## Table 10
```latex
\begin{table*}[t]
% \caption{Ablation studies on the components of~\proposed.}
% \vspace{-2ex}
% \resizebox{0.9\linewidth}{!}{
% \begin{tabular}{c|c|c||cccc||cccc||cccc||cccc}
% \toprule
% \multirow{2}{*}{Row}&\multirow{2}{*}{Ablation} &\multirow{2}{*}{Inference Set}  &\multicolumn{4}{c||}{Movies}& \multicolumn{4}{c||}{Scientific} & \multicolumn{4}{c||}{Electronics}& \multicolumn{4}{c}{CDs}\\ \cmidrule{4-19} 
% & & & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20  & \multicolumn{1}{c|}{NDCG@10} &  \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20  & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20 & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20  \\ \midrule\midrule
                  
% \multirow{3}{*}{(a)}&\multirow{3}{*}{
% \makecell{w.o. $\mathcal{L}_\text{Distill}$, \\$\mathcal{L}_\text{Uniform}$}} & Original  & \multicolumn{1}{c|}{0.3204}  & \multicolumn{1}{c|}{0.3569}  & \multicolumn{1}{c|}{0.5031} & 0.6476 & \multicolumn{1}{c|}{0.3088}  & \multicolumn{1}{c|}{0.3450}  & \multicolumn{1}{c|}{0.5162} & 0.6606& \multicolumn{1}{c|}{0.2659}  & \multicolumn{1}{c|}{0.3066}  & \multicolumn{1}{c|}{0.4427} & 0.6037 & \multicolumn{1}{c|}{0.2278}  & \multicolumn{1}{c|}{0.2701}  & \multicolumn{1}{c|}{0.4048} & 0.5725 \\ 
% & & \multirow{1}{*}{Shuffle} & \multicolumn{1}{c|}{0.3176}  & \multicolumn{1}{c|}{0.3557}  & \multicolumn{1}{c|}{0.4966} & 0.6482 & \multicolumn{1}{c|}{0.3013}  & \multicolumn{1}{c|}{0.3379}  & \multicolumn{1}{c|}{0.5058} & 0.6512 & \multicolumn{1}{c|}{0.2589}  & \multicolumn{1}{c|}{0.2990}  & \multicolumn{1}{c|}{0.4334} & 0.5924 & \multicolumn{1}{c|}{0.2224} & \multicolumn{1}{c|}{0.2649} & \multicolumn{1}{c|}{0.3962} & 0.5697\\ \cmidrule{3-19}
% & &  \multirow{1}{*}{Change ratio} & \multicolumn{1}{c|}{(-0.87\%)}  & \multicolumn{1}{c|}{(-0.34\%)}  & \multicolumn{1}{c|}{(-1.29\%)} & (+0.09\%) & \multicolumn{1}{c|}{(-2.33\%)}  & \multicolumn{1}{c|}{(-2.06\%)}  & \multicolumn{1}{c|}{(-2.01\%)} & (-1.43\%) & \multicolumn{1}{c|}{(-2.63\%)}  & \multicolumn{1}{c|}{(-2.48\%)}  & \multicolumn{1}{c|}{(-2.10\%)} & (-1.87\%) & \multicolumn{1}{c|}{(-2.37\%)} & \multicolumn{1}{c|}{(-1.92\%)} & \multicolumn{1}{c|}{(-2.12\%)} & (-0.49\%)\\ 
% \midrule\midrule

% \multirow{3}{*}{(b)}&\multirow{3}{*}{w.o. $\mathcal{L}_\text{Uniform}$}  &  Original  & \multicolumn{1}{c|}{0.3339}  & \multicolumn{1}{c|}{0.3700}  & \multicolumn{1}{c|}{0.5229} & 0.6654 & \multicolumn{1}{c|}{0.3283}  & \multicolumn{1}{c|}{3653}  & \multicolumn{1}{c|}{0.5421} & 0.6884 & \multicolumn{1}{c|}{0.2895}  & \multicolumn{1}{c|}{0.3285}  & \multicolumn{1}{c|}{0.4665} & 0.6209& \multicolumn{1}{c|}{0.3622}  & \multicolumn{1}{c|}{0.4013}  & \multicolumn{1}{c|}{0.5823} & 0.7371 \\
% & & \multirow{1}{*}{Shuffle}         & \multicolumn{1}{c|}{0.3089}  & \multicolumn{1}{c|}{0.3456}  & \multicolumn{1}{c|}{0.4915} & 0.6328 & \multicolumn{1}{c|}{0.3164}  & \multicolumn{1}{c|}{0.3536}  & \multicolumn{1}{c|}{0.5260} & 0.6686 & \multicolumn{1}{c|}{0.2732}  & \multicolumn{1}{c|}{0.3110}  & \multicolumn{1}{c|}{0.4472} & 0.5976& \multicolumn{1}{c|}{0.3478}  & \multicolumn{1}{c|}{0.3885}  & \multicolumn{1}{c|}{0.5642} & 0.7278 \\ \cmidrule{3-19}
% & & \multirow{1}{*}{Change ratio}    & \multicolumn{1}{c|}{(-7.49\%)}  & \multicolumn{1}{c|}{(-6.59\%)}  & \multicolumn{1}{c|}{(-6.00\%)} & (-4.90\%) & \multicolumn{1}{c|}{(-3.62\%)}  & \multicolumn{1}{c|}{(-3.20\%)}  & \multicolumn{1}{c|}{(-2.97\%)} & (-2.87\%) & \multicolumn{1}{c|}{(-5.63\%)}  & \multicolumn{1}{c|}{(-5.33\%)}  & \multicolumn{1}{c|}{(-4.14\%)} & (-3.75\%) & \multicolumn{1}{c|}{(-3.98\%)} & \multicolumn{1}{c|}{(-3.19\%)} & \multicolumn{1}{c|}{(-3.11\%)} & (-1.26\%)\\
% \midrule\midrule

% \multirow{3}{*}{(c)}& \multirow{3}{*}{\proposed}  &  Original & \multicolumn{1}{c|}{\textbf{0.3560}}  & \multicolumn{1}{c|}{\textbf{0.3924}}  & \multicolumn{1}{c|}{\textbf{0.5569}} & \textbf{0.7010} & \multicolumn{1}{c|}{\textbf{0.3388}}  & \multicolumn{1}{c|}{\textbf{0.3758}}  & \multicolumn{1}{c|}{\textbf{0.5532}} & \textbf{0.6992} & \multicolumn{1}{c|}{\textbf{0.3044}}  & \multicolumn{1}{c|}{\textbf{0.3424}}  & \multicolumn{1}{c|}{\textbf{0.4885}} & \textbf{0.6385} & \multicolumn{1}{c|}{\textbf{0.3809}}  & \multicolumn{1}{c|}{\textbf{0.4158}}  & \multicolumn{1}{c|}{\textbf{0.6085}} & \textbf{0.7461} \\
% & &  \multirow{1}{*}{Shuffle}   & \multicolumn{1}{c|}{0.3263}  & \multicolumn{1}{c|}{0.3624}  & \multicolumn{1}{c|}{0.5188} & 0.6618 & \multicolumn{1}{c|}{0.3224}  & \multicolumn{1}{c|}{0.3591}  & \multicolumn{1}{c|}{0.5287} & 0.6739 & \multicolumn{1}{c|}{0.2838}  & \multicolumn{1}{c|}{0.3210}  & \multicolumn{1}{c|}{0.4552} & 0.6030& \multicolumn{1}{c|}{0.3614}        & \multicolumn{1}{c|}{0.3981}        & \multicolumn{1}{c|}{0.5807}       & 0.7111  \\ \cmidrule{3-19}
% & &  \multirow{1}{*}{Change ratio}    & \multicolumn{1}{c|}{(-8.34\%)}  & \multicolumn{1}{c|}{(-7.65\%)}  & \multicolumn{1}{c|}{(-6.84\%)} & (-5.59\%) & \multicolumn{1}{c|}{(-4.84\%)}  & \multicolumn{1}{c|}{(-4.44\%)}  & \multicolumn{1}{c|}{(-4.43\%)} & (-3.62\%) & \multicolumn{1}{c|}{(-6.77\%)}  & \multicolumn{1}{c|}{(-6.25\%)}  & \multicolumn{1}{c|}{(-6.82\%)} & (-5.56\%) & \multicolumn{1}{c|}{(-5.11\%)} & \multicolumn{1}{c|}{(-4.26\%)} & \multicolumn{1}{c|}{(-4.57\%)} & (-4.69\%)\\


% \bottomrule
% \end{tabular}}
% \vspace{-2.5ex}
% \label{tab: ablation}
% \end{table*}
```

## Table 11
```latex
\begin{table}[h]
\caption{Performance on cross-domain scenarios (HR@10).}
\vspace{-1.5ex}
\resizebox{0.925\linewidth}{!}{
\begin{tabular}{c||c|c|c|c|c|c}
\toprule
& SASRec                                 & TALLRec                                & LLaRA                                  & CoLLM                                  & A-LLMRec                               & \proposed                               \\ \hline
Electronics $\rightarrow$ & \multirow{2}{*}{0.1002}                & \multirow{2}{*}{0.1214}                & \multirow{2}{*}{0.1225}                & \multirow{2}{*}{0.1232}                & \multirow{2}{*}{0.1262}                & \multirow{2}{*}{\textbf{0.1310}}                \\ 
Scientific                &                                        &                                        &                                        &                                        &                                        &                                        \\ \midrule\midrule
Electronics $\rightarrow$     & \multirow{2}{*}{0.0974}& \multirow{2}{*}{0.1132} & \multirow{2}{*}{0.1174} & \multirow{2}{*}{0.1152}& \multirow{2}{*}{0.1217}& \multirow{2}{*}{\textbf{0.1369}} \\ 
   CDs &             &                &                 &                &               &            \\ \bottomrule
\end{tabular}}
\label{tab: cross-domain}
\vspace{-1.5ex}
\end{table}
```

## Table 12
```latex
\begin{table*}[t]
\caption{Ablation studies on the components of~\proposed.}
\vspace{-2ex}
\resizebox{0.85\linewidth}{!}{
\begin{tabular}{c|c|c||cc||cc||cc||cc}
\toprule
\multirow{2}{*}{Row}&\multirow{2}{*}{Ablation} &\multirow{2}{*}{Train Set}  &\multicolumn{2}{c||}{Movies}& \multicolumn{2}{c||}{Scientific} & \multicolumn{2}{c||}{Electronics}& \multicolumn{2}{c}{CDs}\\ \cmidrule{4-11} 
& & & \multicolumn{1}{c|}{NDCG@10} & NDCG@20 & \multicolumn{1}{c|}{NDCG@10} &  NDCG@20 & \multicolumn{1}{c|}{NDCG@10} & NDCG@20 & \multicolumn{1}{c|}{NDCG@10} & NDCG@20   \\ \midrule\midrule
                  
\multirow{3}{*}{(a)}&\multirow{3}{*}{
\makecell{w.o. $\mathcal{L}_\text{Distill}$, \\$\mathcal{L}_\text{Uniform}$}} & Original  & \multicolumn{1}{c|}{0.3204}  & 0.3569   & \multicolumn{1}{c|}{0.3088}  & 0.3450 & \multicolumn{1}{c|}{0.2659}  & 0.3066 & \multicolumn{1}{c|}{0.2278}  & 0.2701  \\ 
& & \multirow{1}{*}{Shuffle} & \multicolumn{1}{c|}{0.3176}  & 0.3557 & \multicolumn{1}{c|}{0.3013}  & 0.3379 & \multicolumn{1}{c|}{0.2589}  & 0.2990   & \multicolumn{1}{c|}{0.2224} & 0.2649 \\ \cmidrule{3-11}
& &  \multirow{1}{*}{Change ratio} & \multicolumn{1}{c|}{(-0.87\%)}  & (-0.34\%)  & \multicolumn{1}{c|}{(-2.33\%)}  & (-2.06\%) & \multicolumn{1}{c|}{(-2.63\%)}  & (-2.48\%) & \multicolumn{1}{c|}{(-2.37\%)} & (-1.92\%)\\ 
\midrule\midrule

\multirow{3}{*}{(b)}&\multirow{3}{*}{w.o. $\mathcal{L}_\text{Uniform}$}  &  Original  & \multicolumn{1}{c|}{0.3339}  & 0.3700  & \multicolumn{1}{c|}{0.3283}  & 0.3653  & \multicolumn{1}{c|}{0.2895}  & 0.3285  & \multicolumn{1}{c|}{0.3622}  & 0.4013 \\
& & \multirow{1}{*}{Shuffle}         & \multicolumn{1}{c|}{0.3089}  & 0.3456 & \multicolumn{1}{c|}{0.3164}  & 0.3536 & \multicolumn{1}{c|}{0.2732}  & 0.3110 & \multicolumn{1}{c|}{0.3478}  & 0.3885 \\ \cmidrule{3-11}
& & \multirow{1}{*}{Change ratio}    & \multicolumn{1}{c|}{(-7.49\%)}  & (-6.59\%) & \multicolumn{1}{c|}{(-3.62\%)}  & (-3.20\%) & \multicolumn{1}{c|}{(-5.63\%)}  & (-5.33\%)  & \multicolumn{1}{c|}{(-3.98\%)} & (-3.19\%)\\
\midrule\midrule

\multirow{3}{*}{(c)}& \multirow{3}{*}{\proposed}  &  Original & \multicolumn{1}{c|}{\textbf{0.3560}}  & \textbf{0.3924} & \multicolumn{1}{c|}{\textbf{0.3388}}  & \textbf{0.3758} & \multicolumn{1}{c|}{\textbf{0.3044}}  & \textbf{0.3424} & \multicolumn{1}{c|}{\textbf{0.3809}}  & \textbf{0.4158} \\
& &  \multirow{1}{*}{Shuffle}   & \multicolumn{1}{c|}{0.3263}  & 0.3624& \multicolumn{1}{c|}{0.3224}  & 0.3591 & \multicolumn{1}{c|}{0.2838}  & 0.3210 & \multicolumn{1}{c|}{0.3614}        & 0.3981 \\ \cmidrule{3-11}
& &  \multirow{1}{*}{Change ratio}    & \multicolumn{1}{c|}{(-8.34\%)}  & (-7.65\%)& \multicolumn{1}{c|}{(-4.84\%)}  & (-4.44\%) & \multicolumn{1}{c|}{(-6.77\%)}  & (-6.25\%) & \multicolumn{1}{c|}{(-5.11\%)} & (-4.26\%)\\


\bottomrule
\end{tabular}}
\vspace{-1.5ex}
\label{tab: ablation}
\end{table*}
```

## Table 13
```latex
\begin{table}[t]
\caption{Train/Inference time comparison.}
\vspace{-1ex}
\resizebox{0.9\linewidth}{!}{
\begin{tabular}{c|c|c|c|c}
\toprule
 \multirow{2}{*}{}& \multicolumn{2}{c|}{Scientific} &\multicolumn{2}{c}{Electronics} \\ \cmidrule{2-5}
     & \multicolumn{1}{c|}{Train (min/epoch)}       & Inference (min)  & \multicolumn{1}{c|}{Train (min/epoch)} &  Inference (min) \\ \midrule
\midrule
% SASRec                   & \multicolumn{1}{c|}{-}             &   & \multicolumn{1}{c|}{} &    \\ \midrule
TALLRec                  & \multicolumn{1}{c|}{194.43}         &  37.04  & \multicolumn{1}{c|}{236.73} &  29.04 \\ \midrule
LLaRA                    & \multicolumn{1}{c|}{202.20}         &  38.79 & \multicolumn{1}{c|}{241.17} & 30.62 \\ \midrule
CoLLM                    & \multicolumn{1}{c|}{214.12}         &      39.86 & \multicolumn{1}{c|}{251.51} & 32.58\\ \midrule
A-LLMRec                    & \multicolumn{1}{c|}{190.94}         &  35.01 & \multicolumn{1}{c|}{235.02} & 28.14 \\ \midrule\midrule
\proposed                & \multicolumn{1}{c|}{\textbf{185.91}}         &  \textbf{34.17}  & \multicolumn{1}{c|}{\textbf{218.21}} & \textbf{27.57}\\ \bottomrule
\end{tabular}}
\label{tab: train time}
\vspace{-2ex}
\end{table}
```

## Table 14
```latex
\begin{table}[t]
% \caption{Performance comparison of prompts with/without explicit user representations.}
% \vspace{-2ex}
% \resizebox{0.7\linewidth}{!}{
% \begin{tabular}{c|c||c||c}
% \toprule
% Dataset                      & Metric  & \makecell{With User \\Representations} & \proposed \\ \midrule\midrule
% \multirow{4}{*}{Movies}      & NDCG@10 & \textbf{0.3625}    & 0.3560                   \\ \cline{2-4} 
%                              & NDCG@20 & \textbf{0.4003}    & 0.3924                   \\ \cline{2-4} 
%                              & HR@10   & \textbf{0.5626}    & 0.5569                   \\ \cline{2-4} 
%                              & HR@20   & 0.7004    & \textbf{0.7010}                   \\ \midrule\midrule
% \multirow{4}{*}{Scientific}  & NDCG@10 & 0.3342    & \textbf{0.3388}                   \\ \cline{2-4} 
%                              & NDCG@20 & 0.3733    & \textbf{0.3758}                   \\ \cline{2-4} 
%                              & HR@10   & 0.5516    & \textbf{0.5532}                   \\ \cline{2-4} 
%                              & HR@20   & 0.6976    & \textbf{0.6992}                   \\ \midrule\midrule
% \multirow{4}{*}{Electronics} & NDCG@10 & 0.2924    & \textbf{0.3044}                   \\ \cline{2-4} 
%                              & NDCG@20 & 0.3405    & \textbf{0.3424}                   \\ \cline{2-4} 
%                              & HR@10   & 0.4725    & \textbf{0.4885}                   \\ \cline{2-4} 
%                              & HR@20   & 0.6239    & \textbf{0.6385}                   \\ \bottomrule
% \end{tabular}}
% \label{tab prompt study}
% \end{table}
```

## Table 15
```latex
\begin{table*}[]
% \caption{Distillation with contrastive learning method}
% \resizebox{1.0\linewidth}{!}{
% \begin{tabular}{c|c||cccc||cccc||cccc}
% \toprule
% \multirow{2}{*}{}            & \multirow{2}{*}{} & \multicolumn{4}{c||}{Movies}                                                                          & \multicolumn{4}{c||}{Scientific}                                                                      & \multicolumn{4}{c}{Electronics}                                                                     \\ \cmidrule{3-14} 
%  &                   & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}   & HR@20   & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}   & HR@20   & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}   & HR@20   \\ \midrule\midrule
% \multirow{3}{*}{Contrastive} & Original          & \multicolumn{1}{c|}{0.3410}  & \multicolumn{1}{c|}{0.3749}  & \multicolumn{1}{c|}{0.5345}  & 0.6687  & \multicolumn{1}{c|}{0.2767}  & \multicolumn{1}{c|}{0.3152}  & \multicolumn{1}{c|}{0.4817}  & 0.6338  & \multicolumn{1}{c|}{0.2553}  & \multicolumn{1}{c|}{0.2935}  & \multicolumn{1}{c|}{0.4277}  & 0.5792  \\  
%  & Shuffle           & \multicolumn{1}{c|}{0.3151}        & \multicolumn{1}{c|}{0.3480}        & \multicolumn{1}{c|}{0.4975}        &  0.6326 & \multicolumn{1}{c|}{0.2638}        & \multicolumn{1}{c|}{0.3021}        & \multicolumn{1}{c|}{0.4650}        &  0.6177  & \multicolumn{1}{c|}{0.2398}        & \multicolumn{1}{c|}{0.2785}        & \multicolumn{1}{c|}{0.4065}        &  0.5608       \\ \cmidrule{2-14} 
%  & Change ratio      & \multicolumn{1}{c|}{(-7.60\%)}        & \multicolumn{1}{c|}{(-7.18\%)}        & \multicolumn{1}{c|}{(-6.92\%)}        &  (-5.40\%)    & \multicolumn{1}{c|}{(-4.66\%)}        & \multicolumn{1}{c|}{(-4.16\%)}        & \multicolumn{1}{c|}{(-3.47\%)}        &  (-2.54\%) & \multicolumn{1}{c|}{(-6.07\%)}        & \multicolumn{1}{c|}{(-5.11\%)}        & \multicolumn{1}{c|}{(-4.96\%)}        &  (-3.18\%)   \\ \midrule\midrule
% \multirow{3}{*}{\proposed}    & Original          & \multicolumn{1}{c|}{0.3560}  & \multicolumn{1}{c|}{0.3924}  & \multicolumn{1}{c|}{0.5569}  & 0.7010  & \multicolumn{1}{c|}{0.3388}  & \multicolumn{1}{c|}{0.3758}  & \multicolumn{1}{c|}{0.5532}  & 0.6992  & \multicolumn{1}{c|}{0.3044}  & \multicolumn{1}{c|}{0.3424}  & \multicolumn{1}{c|}{0.4885}  & 0.6385  \\ 
%  & Shuffle           & \multicolumn{1}{c|}{0.3272}  & \multicolumn{1}{c|}{0.3631}  & \multicolumn{1}{c|}{0.5169}  & 0.6592  & \multicolumn{1}{c|}{0.3232}  & \multicolumn{1}{c|}{0.3605}  & \multicolumn{1}{c|}{0.5336}  & 0.6813  & \multicolumn{1}{c|}{0.2845}  & \multicolumn{1}{c|}{0.3234}  & \multicolumn{1}{c|}{0.4638}  & 0.6184  \\ \cmidrule{2-14} 
%  & Change ratio      & \multicolumn{1}{c|}{(-8.10\%)} & \multicolumn{1}{c|}{(-7.47\%)} & \multicolumn{1}{c|}{(-7.18\%)} & (-5.96\%) & \multicolumn{1}{c|}{(-4.60\%)} & \multicolumn{1}{c|}{(-4.07\%)} & \multicolumn{1}{c|}{(-3.54\%)} & (-2.56\%) & \multicolumn{1}{c|}{(-6.53\%)} & \multicolumn{1}{c|}{(-5.55\%)} & \multicolumn{1}{c|}{(-5.06\%)} & (-3.15\%) \\ \bottomrule
% \end{tabular}}
% \label{tab contrastive}
% \end{table*}
```

## Table 16
```latex
\begin{table}[]
% \caption{Performance with different backbone LLM sizes (i.e., LLaMA 3.1 (8B) vs. LLaMA 3.2 (3B-Instruct)). 
% \textcolor{blue}{(3B) refers to the model trained with LLaMA 3.2 (3B-Instruct), while (8B) refers to the model trained using LLaMA 3.1 (8B).}}
% % \proposed~(3.2) indicates ~\proposed~ trained using LLaMA 3.2 (3B-Instruct).}
% \resizebox{1.0\linewidth}{!}{
% \begin{tabular}{c|c||c||c||c||c||c||c}
% \toprule
% Dataset &   Metric & TALLRec (8B) & LLaRA (8B)  & CoLLM (8B)  & A-LLMRec (8B) & \proposed~(8B) & \proposed~(3B) \\ \midrule\midrule
% \multirow{4}{*}{Movies}      & NDCG@10 & 0.1673  & 0.1562 & 0.3342 & 0.3347   &\textbf{0.3565}  & 0.3560 \\ \cline{2-8} 
%  & NDCG@20 & 0.2115  & 0.2008 & 0.3685 & 0.3703   & 0.3909  & \textbf{0.3924} \\ \cline{2-8} 
%  & HR@10   & 0.3189  & 0.3048 & 0.5193 & 0.5249   & 0.5500  & \textbf{0.5569} \\ \cline{2-8} 
%  & HR@20   & 0.4906  & 0.4724 & 0.6621 & 0.6708   & 0.6860  &  \textbf{0.7010} \\ \midrule\midrule
% \multirow{4}{*}{Scientific}  & NDCG@10 & 0.2736  & 0.2855 & 0.3120 & 0.2874  & \textbf{0.3560} & 0.3388 \\ \cline{2-8} 
%  & NDCG@20 & 0.3182  & 0.3301 & 0.3496 & 0.3248   & \textbf{0.3911} & 0.3758 \\ \cline{2-8} 
%  & HR@10   & 0.4776  & 0.5053 & 0.5208 & 0.4955   & \textbf{0.5695}  & 0.5532 \\ \cline{2-8} 
%  & HR@20   & 0.6383  & 0.6674 & 0.6645 & 0.6438   & \textbf{0.7081}   & 0.6992 \\ \midrule\midrule
% \multirow{4}{*}{Electronics} & NDCG@10 & 0.2562  & 0.2209 & 0.2773 & 0.2845   & \textbf{0.3136}  & 0.3044\\ \cline{2-8} 
%  & NDCG@20 & 0.2987  & 0.2647 & 0.3152 & 0.3211   & \textbf{0.3528}  & 0.3424 \\ \cline{2-8} 
%  & HR@10   & 0.4266  & 0.3649 & 0.4535 & 0.4710   & \textbf{0.5008}  & 0.4885\\ \cline{2-8} 
%  & HR@20   & 0.5955  & 0.5284 & 0.6035 & 0.6209   & \textbf{0.6559}  & 0.6385\\ \bottomrule
% \end{tabular}}
% \label{tab llm size}
% \end{table}
```

## Table 17
```latex
\begin{table}[]
% \caption{Autoregressive learning}
% \resizebox{1.0\linewidth}{!}{
% \begin{tabular}{c|c||cccc||cccc}
% \toprule
% \multirow{2}{*}{}         & \multirow{2}{*}{} & \multicolumn{4}{c|}{Scientific}                                                                    & \multicolumn{4}{c}{Electronics}                                                                    \\ \cmidrule{3-10} 
%   &                   & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20  & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}  & HR@20   \\ \midrule\midrule
% \multirow{3}{*}{TALLRec}  & Original          & \multicolumn{1}{c|}{0.2724}  & \multicolumn{1}{c|}{0.3139}  & \multicolumn{1}{c|}{0.4780} & 0.6421 & \multicolumn{1}{c|}{0.2540}  & \multicolumn{1}{c|}{0.2972}  & \multicolumn{1}{c|}{0.4225} & 0.5941  \\ 
%   & Shuffle           & \multicolumn{1}{c|}{0.2647}  & \multicolumn{1}{c|}{0.3065}  & \multicolumn{1}{c|}{0.4668} & 0.6310 & \multicolumn{1}{c|}{0.2453}  & \multicolumn{1}{c|}{0.2902}  & \multicolumn{1}{c|}{0.4118} & 0.5839  \\ \cmidrule{2-10} 
%   & Change ratio      & \multicolumn{1}{c|}{(-2.83\%)}  & \multicolumn{1}{c|}{(-2.36\%)}  & \multicolumn{1}{c|}{(-2.34\%)} & (-1.73\%) & \multicolumn{1}{c|}{(-3.43\%)}  & \multicolumn{1}{c|}{(-2.36\%)}  & \multicolumn{1}{c|}{(-2.53\%)} & (-1.72\%)  \\ \midrule\midrule
% \multirow{3}{*}{LLaRA}    & Original          & \multicolumn{1}{c|}{0.2860}  & \multicolumn{1}{c|}{0.3257}  & \multicolumn{1}{c|}{0.5057} & 0.6789 & \multicolumn{1}{c|}{0.2175}  & \multicolumn{1}{c|}{0.2577}  & \multicolumn{1}{c|}{0.3649} & 0.5250  \\ 
%   & Shuffle           & \multicolumn{1}{c|}{0.2804}  & \multicolumn{1}{c|}{0.3213}  & \multicolumn{1}{c|}{0.4967} & 0.6685 & \multicolumn{1}{c|}{0.2137}  & \multicolumn{1}{c|}{0.2534}  & \multicolumn{1}{c|}{0.3583} & 0.5193  \\ \cmidrule{2-10} 
%   & Change ratio      & \multicolumn{1}{c|}{(-1.96\%)}  & \multicolumn{1}{c|}{(-1.35\%)}  & \multicolumn{1}{c|}{(-1.78\%)} & (-1.53\%) & \multicolumn{1}{c|}{(-1.75\%)}  & \multicolumn{1}{c|}{(-1.67\%)}  & \multicolumn{1}{c|}{(-1.81\%)} & (-1.09\%) \\ \midrule\midrule
% \multirow{3}{*}{CoLLM}    & Original          & \multicolumn{1}{c|}{0.3254}  & \multicolumn{1}{c|}{0.3599}  & \multicolumn{1}{c|}{0.5348} & 0.6710 & \multicolumn{1}{c|}{0.2745}  & \multicolumn{1}{c|}{0.3092}  & \multicolumn{1}{c|}{0.4433} & 0.5817  \\ 
%   & Shuffle           & \multicolumn{1}{c|}{0.3182}  & \multicolumn{1}{c|}{0.3531}  & \multicolumn{1}{c|}{0.5244} & 0.6609 & \multicolumn{1}{c|}{0.2657}  & \multicolumn{1}{c|}{0.3007}  & \multicolumn{1}{c|}{0.4324} & 0.5724  \\ \cmidrule{2-10} 
%   & Change ratio      & \multicolumn{1}{c|}{(-2.21\%)}  & \multicolumn{1}{c|}{(-1.89\%)}  & \multicolumn{1}{c|}{(-1.94\%)} & (-1.51\%) & \multicolumn{1}{c|}{(-3.21\%)}  & \multicolumn{1}{c|}{(-2.75\%)}  & \multicolumn{1}{c|}{(-2.46\%)} & (-1.60\%)  \\ \midrule\midrule
% \multirow{3}{*}{A-LLMRec} & Original          & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}       &        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}       &         \\
%   & Shuffle           & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}       &        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}       &         \\ \cmidrule{2-10} 
%   & Change ratio      & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}       &        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}        & \multicolumn{1}{c|}{}       &         \\ \midrule\midrule
% \multirow{3}{*}{\proposed} & Original          & \multicolumn{1}{c|}{0.3478}  & \multicolumn{1}{c|}{0.3844}  & \multicolumn{1}{c|}{0.5629} & 0.6985 & \multicolumn{1}{c|}{0.3129}  & \multicolumn{1}{c|}{0.3505}  & \multicolumn{1}{c|}{0.4940} & 0.6407  \\ \
%   & Shuffle           & \multicolumn{1}{c|}{0.3253}  & \multicolumn{1}{c|}{0.3688}  & \multicolumn{1}{c|}{0.5413} & 0.6807 & \multicolumn{1}{c|}{0.2972}  & \multicolumn{1}{c|}{0.3355}  & \multicolumn{1}{c|}{0.4768} & 0.6251  \\ \cmidrule{2-10} 
%   & Change ratio      & \multicolumn{1}{c|}{(-6.46\%)} & \multicolumn{1}{c|}{(-4.05\%)}  & \multicolumn{1}{c|}{(-3.84\%)} & (-2.55\%) & \multicolumn{1}{c|}{(-5.02\%)}  & \multicolumn{1}{c|}{(-4.28\%)}  & \multicolumn{1}{c|}{(-3.48\%)} & (-2.43\%)  \\ \bottomrule
% \end{tabular}}
% \label{tab: auto-regressive}
% \end{table}
```

## Table 18
```latex
\begin{table}[]
% \caption{Performance with different backbone LLM sizes (i.e., LLaMA 3.1 (8B) vs. LLaMA 3.2 (3B-Instruct)). \proposed~(3.2) indicates ~\proposed~ trained using LLaMA 3.2 (3B-Instruct).}
% \resizebox{1.0\linewidth}{!}{
% \begin{tabular}{c|c||c||c||c||c||c||c}
% \toprule
% Dataset &   Metric & TALLRec & LLaRA  & CoLLM  & A-LLMRec & \proposed & \proposed (3.2) \\ \midrule\midrule
% \multirow{4}{*}{Movies}      & NDCG@10 & 0.1673  & 0.1562 & 0.3342 & 0.3347   &\textbf{0.3565}  & 0.3560 \\ \cline{2-8} 
%  & NDCG@20 & 0.2115  & 0.2008 & 0.3685 & 0.3703   & 0.3909  & \textbf{0.3924} \\ \cline{2-8} 
%  & HR@10   & 0.3189  & 0.3048 & 0.5193 & 0.5249   & 0.5500  & \textbf{0.5569} \\ \cline{2-8} 
%  & HR@20   & 0.4906  & 0.4724 & 0.6621 & 0.6708   & 0.6860  &  \textbf{0.7010} \\ \midrule\midrule
% \multirow{4}{*}{Scientific}  & NDCG@10 & 0.2736  & 0.2855 & 0.3120 & 0.2874  & \textbf{0.3560} & 0.3388 \\ \cline{2-8} 
%  & NDCG@20 & 0.3182  & 0.3301 & 0.3496 & 0.3248   & \textbf{0.3911} & 0.3758 \\ \cline{2-8} 
%  & HR@10   & 0.4776  & 0.5053 & 0.5208 & 0.4955   & \textbf{0.5695}  & 0.5532 \\ \cline{2-8} 
%  & HR@20   & 0.6383  & 0.6674 & 0.6645 & 0.6438   & \textbf{0.7081}   & 0.6992 \\ \midrule\midrule
% \multirow{4}{*}{Electronics} & NDCG@10 & 0.2562  & 0.2209 & 0.2773 & 0.2845   & \textbf{0.3136}  & 0.3044\\ \cline{2-8} 
%  & NDCG@20 & 0.2987  & 0.2647 & 0.3152 & 0.3211   & \textbf{0.3528}  & 0.3424 \\ \cline{2-8} 
%  & HR@10   & 0.4266  & 0.3649 & 0.4535 & 0.4710   & \textbf{0.5008}  & 0.4885\\ \cline{2-8} 
%  & HR@20   & 0.5955  & 0.5284 & 0.6035 & 0.6209   & \textbf{0.6559}  & 0.6385\\ \bottomrule
% \end{tabular}}
% \label{tab llm size}
% \end{table}
```

## Table 19
```latex
\begin{table}[h]
\caption{Statistics of datasets after preprocessing.}
\vspace{-2ex}
\resizebox{0.75\linewidth}{!}{
\begin{tabular}{c|c|c|c|c}
\toprule
Dataset & Movies & Scientific & Electronics & CDs  \\ \midrule\midrule
\# Users      & 11,947    & 23,627    &  27,601 & 18,481 \\ \midrule
\# Items  & 17,490    & 25,764    &  31,533 & 30,951   \\ \midrule
\# Interactions & 144,071    & 266,164    &  292,308 & 284,695      \\ \bottomrule
\end{tabular}}
\label{tab dataset}
\end{table}
```

## Table 20
```latex
\begin{table}[t]
\caption{Performance comparison of prompts with/without explicit user representations.}
\vspace{-2ex}
\resizebox{0.7\linewidth}{!}{
\begin{tabular}{c|c||c||c}
\toprule
Dataset                      & Metric  & \makecell{With User \\Representations} & \proposed \\ \midrule\midrule
\multirow{2}{*}{Movies}      & NDCG@10 & \textbf{0.3625}    & 0.3560                   \\ \cline{2-4} 
                             & HR@10   & \textbf{0.5626}    & 0.5569                   \\ \midrule\midrule
\multirow{2}{*}{Scientific}  & NDCG@10 & 0.3342    & \textbf{0.3388}                   \\ \cline{2-4} 
                             & HR@10   & 0.5516    & \textbf{0.5532}                   \\\midrule\midrule
\multirow{2}{*}{Electronics} & NDCG@10 & 0.2924    & \textbf{0.3044}                   \\ \cline{2-4} 
                             & HR@10   & 0.4725    & \textbf{0.4885}                   \\ \bottomrule
\end{tabular}}
\vspace{-2.5ex}
\label{tab prompt study}
\end{table}
```

## Table 21
```latex
\begin{table}[t]
% \caption{Performance comparison of prompts with/without explicit user representations.}
% \vspace{-2ex}
% \resizebox{0.7\linewidth}{!}{
% \begin{tabular}{c|c||c||c}
% \toprule
% Dataset                      & Metric  & \makecell{With User \\Representations} & \proposed \\ \midrule\midrule
% \multirow{4}{*}{Movies}      & NDCG@10 & \textbf{0.3625}    & 0.3560                   \\ \cline{2-4} 
%                              & NDCG@20 & \textbf{0.4003}    & 0.3924                   \\ \cline{2-4} 
%                              & HR@10   & \textbf{0.5626}    & 0.5569                   \\ \cline{2-4} 
%                              & HR@20   & 0.7004    & \textbf{0.7010}                   \\ \midrule\midrule
% \multirow{4}{*}{Scientific}  & NDCG@10 & 0.3342    & \textbf{0.3388}                   \\ \cline{2-4} 
%                              & NDCG@20 & 0.3733    & \textbf{0.3758}                   \\ \cline{2-4} 
%                              & HR@10   & 0.5516    & \textbf{0.5532}                   \\ \cline{2-4} 
%                              & HR@20   & 0.6976    & \textbf{0.6992}                   \\ \midrule\midrule
% \multirow{4}{*}{Electronics} & NDCG@10 & 0.2924    & \textbf{0.3044}                   \\ \cline{2-4} 
%                              & NDCG@20 & 0.3405    & \textbf{0.3424}                   \\ \cline{2-4} 
%                              & HR@10   & 0.4725    & \textbf{0.4885}                   \\ \cline{2-4} 
%                              & HR@20   & 0.6239    & \textbf{0.6385}                   \\ \bottomrule
% \end{tabular}}
% \label{tab prompt study}
% \end{table}
```

## Table 22
```latex
\begin{table*}[]
% \caption{Distillation with contrastive learning method.}
% \resizebox{1.0\linewidth}{!}{
% \begin{tabular}{c|c||cccc||cccc||cccc}
% \toprule
% \multirow{2}{*}{Distillation Loss}            & \multirow{2}{*}{} & \multicolumn{4}{c||}{Movies}                                                                          & \multicolumn{4}{c||}{Scientific}                                                                      & \multicolumn{4}{c}{Electronics}                                                                     \\ \cmidrule{3-14} 
%  &                   & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}   & HR@20   & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}   & HR@20   & \multicolumn{1}{c|}{NDCG@10} & \multicolumn{1}{c|}{NDCG@20} & \multicolumn{1}{c|}{HR@10}   & HR@20   \\ \midrule\midrule
% \multirow{3}{*}{Contrastive} & Original          & \multicolumn{1}{c|}{0.3410}  & \multicolumn{1}{c|}{0.3749}  & \multicolumn{1}{c|}{0.5345}  & 0.6687  & \multicolumn{1}{c|}{0.2767}  & \multicolumn{1}{c|}{0.3152}  & \multicolumn{1}{c|}{0.4817}  & 0.6338  & \multicolumn{1}{c|}{0.2553}  & \multicolumn{1}{c|}{0.2935}  & \multicolumn{1}{c|}{0.4277}  & 0.5792  \\  
%  & Shuffle           & \multicolumn{1}{c|}{0.3151}        & \multicolumn{1}{c|}{0.3480}        & \multicolumn{1}{c|}{0.4975}        &  0.6326 & \multicolumn{1}{c|}{0.2638}        & \multicolumn{1}{c|}{0.3021}        & \multicolumn{1}{c|}{0.4650}        &  0.6177  & \multicolumn{1}{c|}{0.2398}        & \multicolumn{1}{c|}{0.2785}        & \multicolumn{1}{c|}{0.4065}        &  0.5608       \\ \cmidrule{2-14} 
%  & Change ratio      & \multicolumn{1}{c|}{(-7.60\%)}        & \multicolumn{1}{c|}{(-7.18\%)}        & \multicolumn{1}{c|}{(-6.92\%)}        &  (-5.40\%)    & \multicolumn{1}{c|}{(-4.66\%)}        & \multicolumn{1}{c|}{(-4.16\%)}        & \multicolumn{1}{c|}{(-3.47\%)}        &  (-2.54\%) & \multicolumn{1}{c|}{(-6.07\%)}        & \multicolumn{1}{c|}{(-5.11\%)}        & \multicolumn{1}{c|}{(-4.96\%)}        &  (-3.18\%)   \\ \midrule\midrule
% \multirow{3}{*}{\proposed~(MSE)}    & Original          & \multicolumn{1}{c|}{\textbf{0.3560}}  & \multicolumn{1}{c|}{\textbf{0.3924}}  & \multicolumn{1}{c|}{\textbf{0.5569}}  & \textbf{0.7010}  & \multicolumn{1}{c|}{\textbf{0.3388}}  & \multicolumn{1}{c|}{\textbf{0.3758}}  & \multicolumn{1}{c|}{\textbf{0.5532}}  & \textbf{0.6992}  & \multicolumn{1}{c|}{\textbf{0.3044}}  & \multicolumn{1}{c|}{\textbf{0.3424}}  & \multicolumn{1}{c|}{\textbf{0.4885}}  & \textbf{0.6385}  \\ 
%  & Shuffle           & \multicolumn{1}{c|}{0.3272}  & \multicolumn{1}{c|}{0.3631}  & \multicolumn{1}{c|}{0.5169}  & 0.6592  & \multicolumn{1}{c|}{0.3232}  & \multicolumn{1}{c|}{0.3605}  & \multicolumn{1}{c|}{0.5336}  & 0.6813  & \multicolumn{1}{c|}{0.2845}  & \multicolumn{1}{c|}{0.3234}  & \multicolumn{1}{c|}{0.4638}  & 0.6184  \\ \cmidrule{2-14} 
%  & Change ratio      & \multicolumn{1}{c|}{(-8.10\%)} & \multicolumn{1}{c|}{(-7.47\%)} & \multicolumn{1}{c|}{(-7.18\%)} & (-5.96\%) & \multicolumn{1}{c|}{(-4.60\%)} & \multicolumn{1}{c|}{(-4.07\%)} & \multicolumn{1}{c|}{(-3.54\%)} & (-2.56\%) & \multicolumn{1}{c|}{(-6.53\%)} & \multicolumn{1}{c|}{(-5.55\%)} & \multicolumn{1}{c|}{(-5.06\%)} & (-3.15\%) \\ \bottomrule
% \end{tabular}}
% \label{tab contrastive}
% \end{table*}
```

## Table 23
```latex
\begin{table}[]
\caption{Distillation with contrastive learning (NDCG@10).}
\resizebox{0.8\linewidth}{!}{
\begin{tabular}{c|c||c||c||c}
\toprule
Distillation Loss            & Inference  & Movies                                                                         & Scientific                                                                      & Electronics                                                                     \\ \midrule\midrule
\multirow{3}{*}{Contrastive} & Original          & 0.3410  & 0.2767  & 0.2553 \\  
 & Shuffle           & 0.3151 & 0.2638         & 0.2398     \\ \cmidrule{2-5} 
 & Change ratio      & (-7.60\%)    & (-4.66\%)    & (-6.07\%)  \\ \midrule\midrule
\multirow{3}{*}{\proposed~(MSE)}    & Original          & \textbf{0.3560}  & \textbf{0.3388}  & \textbf{0.3044} \\ 
 & Shuffle           & 0.3272 & 0.3232    & 0.2845  \\ \cmidrule{2-5} 
 & Change ratio      & (-8.10\%)  & (-4.60\%)  & (-6.53\%) \\ \bottomrule
\end{tabular}}
\label{tab contrastive}
\vspace{-1.5ex}
\end{table}
```

## Table 24
```latex
\begin{table}[]
% \caption{Average pairwise Euclidean distance between user representations. }
% \resizebox{0.8\linewidth}{!}{
% \begin{tabular}{c||c|c|c|c}
% \toprule
%      & Movies & Scientific & Electronics & CDs   \\ \midrule\midrule
% w.o. $\mathcal{L}_\text{Uniform}$ & 7.69   & 7.78       & 8.03        & 9.82  \\ \midrule
% \proposed & 9.33   & 11.54      & 13.81       & 11.68 \\ \bottomrule
% \end{tabular}}
% \label{tab: over-smoothing}
% \end{table}
```

