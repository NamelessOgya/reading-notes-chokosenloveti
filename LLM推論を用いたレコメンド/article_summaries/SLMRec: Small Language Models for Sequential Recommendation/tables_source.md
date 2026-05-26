# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
% \centering
% \caption{Statistics of the Amazon datasets. $\left|\mathcal{U}\right|$, $\left|\mathcal{V}\right|$, and $\left|\mathcal{E}\right|$ denote the number of users, items, and ratings, respectively.}
% \vspace{-5pt}
% % \setlength{\abovecaptionskip}{0pt}
% % \setlength{\belowcaptionskip}{5pt}
% \label{dataset-stats}
% % \setlength\tabcolsep {0.3pt}
% % \renewcommand{\arraystretch}{0.85}
% \resizebox{0.5\textwidth}{!}{
% \begin{tabular}{c|ccc|c}
% \midrule
% \textbf{Dataset} & $\left|\mathcal{U}\right|$ & $\left|\mathcal{V}\right|$ & $\left|\mathcal{E}\right|$ & Density \\ \midrule
% Cloth       & 1,219,678                 & 376,858                  & 11,285,464                & 0.002\%  \\  
% Movie       & 297,529                 & 60,175                  & 3,410,019               & 0.019\%  \\ \midrule
% Music       &  112,395               & 73,713                   & 1,443,755               & 0.017\%  \\ 
% Sport       & 332,447               & 12,314                   & 146,639               & 0.008\% \\ \midrule
% % Tmall       &963,923	& 2,353,207 & 	44,528,127	& 0.002\%        \\ \midrule
% \end{tabular}}
% % \begin{tablenotes}    
% %         % \small            
% %         \item $\left|\mathcal{U}\right|$, $\left|\mathcal{V}\right|$, $\left|\mathcal{E}\right|$ denote the number of users, items, and ratings, respectively. 
% %       \end{tablenotes}
% \vspace{-10pt}
%       \end{table}
```

## Table 2
```latex
\begin{table*}[tb!]
% \begin{threeparttable}
% \scriptsize
\centering
% \setlength{\abovecaptionskip}{0pt}
% \setlength{\belowcaptionskip}{5pt}
\caption{Experimental results (\%) on the Cloth and Movie dataset. The missing MRR value of Open-P5 is unavailable due to the time complexity constrictions. The number on the left of the arrow is the layers $N$ of the student model. The left number on the right of the arrow is the layers $M$ of the teacher model. For Open-P5, we adopt LLaMa as their backbone. 
We highlight the methods with the \textcolor{first}{\textbf{best}} and \textcolor{second}{\textbf{second-best}} average performances. \update{We also give the average ranking of each evaluation metric. } Moreover, \textcolor{third}{E4SRec$_4$}, which has the same number of layers as our $\Ours$, is also marked.
}
\vspace{-10pt}
\label{clothmovie}
% \setlength\tabcolsep{6pt}{
\begin{threeparttable}
        \setlength{\tabcolsep}{3mm}{ 
        \resizebox{\textwidth}{!}{
\begin{tabular}{l|cccc|cccc|c}
\midrule
% \multirow{3}{*}{\bf Methods} & \multicolumn{6}{c}{\bf Cloth Dataset} & \multicolumn{6}{c}{\bf Movie Dataset} & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Average\\Improv.}} 
%    \\
% \cmidrule(r){2-7}\cmidrule{8-13}
%  & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG}  &\multirow{2}{*}{MRR}   & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG} & \multirow{2}{*}{MRR} \\
% \cmidrule(r){2-4}\cmidrule(r){5-6}\cmidrule(r){8-10}\cmidrule{11-12}  & @1   & @5  & @10 & @5 & @10 &   & @1  & @5  & @10 & @5  & @10 &        \\
\multirow{2}{*}{\textbf{Model}}  & \multicolumn{4}{c|}{\texttt{Cloth}} & \multicolumn{4}{c}{\texttt{Movie}} & \multirow{2}{*}{\update{\textbf{Rank}}} \\
% & \multirow{2}{*}{\textbf{Improv.(\%)}} \\
         & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} & \\
\midrule
Caser    
& 9.66   & 15.18 
  & 12.66
    & 13.03
  & 4.27   & 14.96
    & 9.57
   &10.36 & 13.50 \\
   % & -38.19    \\
   
GRU4Rec  & 13.79   &  15.46    
  & 14.64   
   & 15.15   
& 10.56 & 19.47   
 & 15.11 
  & 15.46 & 9.25 \\   
  % & -20.26  \\
 
BERT4Rec    & 13.60   &  14.66     
 & 14.14   
  & 14.59   
& 9.68 & 14.91   
 & 12.40  
  & 12.74  & 11.63  \\
  % & -29.84   \\

SASRec    
& 13.08   & 16.94      
  & 15.01   
    & 15.76   
  & 5.57   & 16.80 
    & 11.17   
   & 12.08 & 11.63 \\
   % & -25.19    \\

HGN    
& 15.96   & 18.70
  & 17.30
    & 18.27
  & 7.54   &19.20
    & 13.42
   &14.73 &6.50 \\
   % & -18.86    \\

LightSANs    
& 14.12   & 20.32
  & 17.30
    & 16.86
  &6.08   &17.54
    & 11.81
   &12.82 & 8.00 \\
   % &000    \\
\midrule 

\update{S$^3$-Rec}    
& 14.10   & 18.67      
  & 16.10   
    & 16.95   
  & 7.75  & 20.39 
    & 15.69   
   & 14.34 &7.50 \\

   \update{DuoRec}    
& 13.06   & 18.29      
  & 15.79   
    & 15.42   
  & 10.07   & 20.37 
    & 17.96   
   & 16.61 &7.88 \\

   \update{MAERec}    
& 13.29   & 18.35      
  & 15.68   
    & 16.13   
  & 8.89   & 20.24 
    & 16.03   
   & 15.28 & 8.38 \\
   
\midrule
 
% Open-P5$_\mathrm{T5}$~\citep{xu2023openp5}   &    &      &  &   &    &   &
%   &    &  &  &   &    &   \\ 
  
Open-P5  & 14.13   & 17.68  
 &  17.02 
   & -  
& 12.66 &  21.98  
 & 17.13 
 & -  & 5.67 \\
 % &  -9.96  \\ 
  
E4SRec  & \textcolor{second}{\textbf{16.71}}	& \textcolor{second}{\textbf{19.45}}
	& \textcolor{second}{\textbf{18.09}}
	& \textcolor{second}{\textbf{18.77}}
  & \textcolor{second}{\textbf{14.74}}   & \textcolor{second}{\textbf{23.79}}  
    & \textcolor{second}{\textbf{19.45}} 
     & \textcolor{second}{\textbf{19.74}} & \textcolor{second}{\textbf{1.75}} \\
     % & 0.00    \\

E4SRec$_{8}$  & 15.30	& 18.54	
	& 16.91	
	& 17.60  
  & 13.32    & 22.49  
    & 17.99   
     & 18.46  &4.00 \\
     % & -5.90   \\

E4SRec$_{4}$  & \textcolor{third}{\textbf{14.58}}	& \textcolor{third}{\textbf{18.05}}	
	& \textcolor{third}{\textbf{16.32}}	
	& \textcolor{third}{\textbf{17.01}}  
  & \textcolor{third}{\textbf{11.80}}    & \textcolor{third}{\textbf{21.54}}  
    & \textcolor{third}{\textbf{16.73}}   
     & \textcolor{third}{\textbf{17.20}} & \textcolor{third}{\textbf{5.75}} \\
     % & -10.24   \\
  
\midrule

$\OursDS{4}{8}$  & \textcolor{first}{\textbf{16.69}}   & \textcolor{first}{\textbf{19.47}}    
 & \textcolor{first}{\textbf{18.07}}   
    & \textcolor{first}{\textbf{18.74}} 
  & \textcolor{first}{\textbf{15.29}}    & \textcolor{first} {\textbf{24.25}}
   & \textcolor{first} {\textbf{19.90}}  
      & \textcolor{first}{\textbf{20.36}} &\textcolor{first}{\textbf{1.50}} \\
      % & +1.49    \\
  
  
\midrule
\end{tabular}}}
	\end{threeparttable}
% \end{threeparttable}
\vspace{-10pt}
\end{table*}
```

## Table 3
```latex
\begin{table*}[tb!]
% \scriptsize
\caption{Experimental results (\%) on the Music and Sport dataset.}
\vspace{-10pt}
\label{musicsport}
% \setlength\tabcolsep{6pt}{
% \begin{tabular}{lccccccccccccccc}
% \toprule
% \multirow{3}{*}{\bf Methods} & \multicolumn{6}{c}{\bf Music Dataset} & \multicolumn{6}{c}{\bf Sport Dataset} & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Average\\Improv.}} 
\begin{threeparttable}
        \setlength{\tabcolsep}{3mm}{ 
        \resizebox{\textwidth}{!}{
\begin{tabular}{l|cccc|cccc|c}
\midrule
% \multirow{2}{*}{\textbf{Model}}  & \multicolumn{4}{|c|}{\texttt{Music}} & \multicolumn{4}{|c|}{\texttt{Sport}} & \multirow{2}{*}{\textbf{Improv.}} \\
%          & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} &  \\
\multirow{2}{*}{\textbf{Model}}  & \multicolumn{4}{|c|}{\texttt{Music}} & \multicolumn{4}{|c}{\texttt{Sport}} & \multirow{2}{*}{\update{\textbf{Rank}}}\\
% & \multirow{2}{*}{\textbf{Improv.(\%)}} \\
         & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} & \\
%  & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG}  &\multirow{2}{*}{MRR}   & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG} & \multirow{2}{*}{MRR} \\
% \cmidrule(r){2-4}\cmidrule(r){5-6}\cmidrule(r){8-10}\cmidrule{11-12}  & @1   & @5  & @10 & @5 & @10 &   & @1  & @5  & @10 & @5  & @10 &       \\
\midrule
Caser    
& 0.71   & 3.28
  & 1.96
    & 2.29
  & 1.05   & 3.75
    & 2.39
   &2.84 & 13.50 \\
   % & 000    \\
   
GRU4Rec  & 1.89   & 3.22     
 & 2.57   
  & 3.08   
  & 5.26   & 7.75 
   & 6.52  
     & 7.08 & 10.13\\
     % & -41.93   \\
 
BERT4Rec    &2.10    &3.16      
  & 2.64  
    & 3.11  
& 4.81 & 6.70    
  & 5.79 
  & 6.26 &10.63  \\
  % & -46.82  \\

SASRec    & 1.82   & 5.72      
 & 3.79   
   & 4.51   
 & 4.70   & 8.43     
  & 6.59  
   & 7.24 & 8.75  \\
   % &-30.60    \\

HGN    
& 2.01   & 5.49
  & 3.82
    &4.17
  & 3.42   &6.24
    &  4.83
   &5.30 & 10.50 \\
   % & 000    \\

LightSANs   
& 1.05   & 4.06
  & 2.54
    &3.00
  & 5.18   &8.94
    & 7.07
   &7.72 & 8.25 \\
   % & 000    \\
   
\midrule

  \update{S$^3$-Rec}    
& 2.48   & 7.37      
  & 4.94   
    & 4.68  
  & 4.14   & 8.49 
    & 6.89  
   & 7.35 & 6.88 \\
   % & -25.19    \\

   \update{DuoRec}    
& 1.84   & 4.50     
  & 3.19  
    & 3.04  
  & 4.13   & 8.81 
    & 7.03   
   & 6.64 & 9.13 \\
   % & -25.19    \\

   \update{MAERec}    
& 2.19   & 6.35      
  & 4.67   
    & 3.96   
  & 4.01   & 8.35 
    & 6.65   
   & 6.98 & 8.63 \\
   % & -25.19    \\
   
\midrule

Open-P5   &  4.35  &   8.12  
 & 6.74  
  &  - 
&5.49 &   8.50 
  & 6.92 
  &  -  &5.33 \\
  % &  -12.62 \\ 
  
E4SRec  & \textcolor{second}{\textbf{5.62}}	& \textcolor{second}{\textbf{9.29}}
	& \textcolor{second}{\textbf{7.50}}	
	& \textcolor{second}{\textbf{7.98}}
   & \textcolor{second}{\textbf{6.40}}   & \textcolor{second}{\textbf{9.67}}
    & \textcolor{second}{\textbf{8.05}}  
     & \textcolor{second}{\textbf{8.70}}  &\textcolor{second}{\textbf{1.75}} \\
     % & 0.00  \\

E4SRec$_{8}$  & 5.46	& 8.86	
	& 7.21	
	& 7.74  
  & 5.48   &  8.63    
   & 7.06  
     & 7.76   &3.63 \\
     % & -7.48    \\

E4SRec$_{4}$  & \textcolor{third}{\textbf{5.33}}	& \textcolor{third}{\textbf{8.75}}
	& \textcolor{third}{\textbf{7.08}}
	& \textcolor{third}{\textbf{7.59}}
  & \textcolor{third}{\textbf{5.41}}   & \textcolor{third}{\textbf{8.65}}     
   & \textcolor{third}{\textbf{7.04}}   
     & \textcolor{third}{\textbf{7.72}} &\textcolor{third}{\textbf{4.50}}  \\
     % & -8.54     \\
  
\midrule
  
$\OursDS{4}{8}$  & \textcolor{first}{\textbf{5.72}}  & \textcolor{first}{\textbf{9.15}}    
  & \textcolor{first}{\textbf{7.48}}
  & \textcolor{first}{\textbf{8.03}} 
& \textcolor{first} {\textbf{6.62}} & \textcolor{first}{\textbf{9.83}}  
 & \textcolor{first}{\textbf{8.25}}
  & \textcolor{first}{\textbf{8.89}} &\textcolor{first}{\textbf{1.25}}  \\
  % & +0.81  \\
  
\midrule
\end{tabular}}}
	\end{threeparttable}
 \vspace{-10pt}
\end{table*}
```

## Table 4
```latex
\begin{table*}[tb!]
% \scriptsize
% % \centering
% % \vspace{-5pt}
% % \setlength{\abovecaptionskip}{0pt}
% % \setlength{\belowcaptionskip}{5pt}
% \caption{Experimental results (\%) on the Cloth and Movie dataset. The missing MRR value of Open-P5 is unavailable due to the time complexity constrictions. The number on the left of the arrow is the layers $N$ of the student model. The left number on the right of the arrow is the layers $M$ of the teacher model. For Open-P5, we adopt LLaMa as their backbone. }
% \label{clothmovie}
% \setlength\tabcolsep{6pt}{
% \begin{tabular}{lccccccccccccccc}
% \toprule
% \multirow{3}{*}{\bf Methods} & \multicolumn{6}{c}{\bf Cloth Dataset} & \multicolumn{6}{c}{\bf Movie Dataset} & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Average\\Improv.}} 
% % & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Train\\Params}}   
% % & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Infer\\Params}}
%    \\
% \cmidrule(r){2-7}\cmidrule{8-13}
%  & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG}  &\multirow{2}{*}{MRR}   & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG} & \multirow{2}{*}{MRR} \\
% \cmidrule(r){2-4}\cmidrule(r){5-6}\cmidrule(r){8-10}\cmidrule{11-12}  & @1   & @5  & @10 & @5 & @10 &   & @1  & @5  & @10 & @5  & @10 &        \\
% \midrule
% GRU4Rec  & 13.79   &  15.46    & 16.83  & 14.64   & 15.08   & 15.15   & 10.56
%   & 19.47   & 25.21  & 15.11 & 16.96  & 15.46    & -20.26  \\
 
% BERT4Rec    & 13.60   &  14.66     & 15.55 & 14.14   &  14.43  & 14.59   & 9.68
%   & 14.91   & 17.98 & 12.40  & 13.38  & 12.74    & -29.84   \\

% SASRec    & 13.08   & 16.94      & 20.26  & 15.01   & 16.08    & 15.76   
%   & 5.57   & 16.80 & 26.85  & 11.17   &  14.42  & 12.08  & -25.19    \\
 
% \midrule
 
% % Open-P5$_\mathrm{T5}$~\citep{xu2023openp5}   &    &      &  &   &    &   &
% %   &    &  &  &   &    &   \\ 
  
% Open-P5  & 14.13   & 17.68  & 19.74 &  17.02 & 16.40   & -  & 12.66
%   &  21.98  & 27.24 & 17.13 &  19.81 & -  &  -9.96  \\ 
  
% E4SRec*  & 16.71	& 19.45	& 21.86	& 18.09	& 18.86	& 18.77   
%   & 14.74    & 23.79  & 29.09  & 19.45   & 21.16   & 19.74  & 0.00    \\

% E4SRec$_{8}$*  & 15.30	& 18.54	& 21.29	& 16.91	& 17.79	& 17.60  
%   & 13.32    & 22.49  & 28.57  & 17.99   & 19.94   & 18.46  & -5.90   \\

% E4SRec$_{4}$*  & 14.58	& 18.05	& 20.92	& 16.32	& 17.25	& 17.01  
%   & 11.80    & 21.54  & 28.02  & 16.73   & 18.82   & 17.20  & -10.24   \\
  
% \midrule
% % \textbf{Offline:}   &    &      &  &   &    &   &
% %   &    &  &  &   &    &  &    &  \\ 
  
% % $\OursDS{32}{32}$ & \textbf{17.63}    & \textbf{19.66}     & 21.39  & \textbf{18.66}   & \textbf{19.21}    & \textbf{19.25}   & 2.00
% %   &    &  &  &   &    &  &    &\\

% $\OursDS{8}{32}$ & 16.56    & 19.05     & 21.33  & 17.79   & 18.53    & 18.48   
%   & 15.18   & 23.93  & 29.30  & 19.69  & 21.41   & 20.06  & -0.17 \\

% % $\OursDS{8}{8}$ & 16.07    & 18.84     & 21.24  & 17.46   & 18.23    & 18.15   & -3.44
% %   &    &  &  &   &    &  &    & \\

% $\OursDS{4}{32}$   & 14.86    & 18.03  & 20.70  & 16.45   & 17.30   & 17.12  & 13.70   
%   & 22.73   & 28.44  & 18.37  & 20.21  &  18.74  & -6.56 \\
  
% $\OursDS{4}{8}$ & 16.10    & 18.85     & 21.33  & 17.48   & 18.28    & 18.17   
%   & 14.83   & 23.08 & 28.02  & 19.08  & 20.67   & 19.45  &-2.55  \\

% \textbf{+$\mathcal{D}_{norm}$:}   &    &      &  &   &    &   &    &      &  &   &    &      &    \\ 

% $\OursDS{4}{8}$   & 16.28    & 19.12     & 21.75 & 17.69   &  18.53  & 18.40  & 14.86   & 23.89     &  30.22 & 19.36  &21.39    &19.84      &-0.37     \\

% \textbf{+$\mathcal{L}_{ms}$:}   &    &      &  &   &    &   &
%   &    &  &  &   &    &    \\ 
  
% $\OursDS{4}{8}$  & 16.85   & 19.05      &  20.93 & 17.96   & 18.57    & 18.59 
%   & 15.05    & 23.48 &  28.60 & 19.40  & 21.05    & 19.76 &-0.85    \\

% \textbf{+$\mathcal{D}_{norm}$+$\mathcal{L}_{ms}$:}   &    &      &  &   &    &   &
%   &    &  &  &   &    &    \\ 

% % $\OursDS{32}{32}$  &    &      &  &   &    &   &
% %   &    &  &  &   &    &  &    &  \\

% % $\OursDS{8}{32}$  
% %   &    &      &  &   &    &  &    &      &  &   &    &   &  &    &  \\

% % $\OursDS{4}{32}$   & 15.27   & 18.22 & 20.73  & 16.74   & 17.54   & 17.42  &    
% %   &    &  &  &   &    &  &    & \\
  
% $\OursDS{4}{8}$  & 16.69   & 19.47      &  21.90 & 18.07   & 18.85    & 18.74 
%   & 15.29    & 24.25 &  30.19 & 19.90  & 21.82    & 20.36 & +1.49    \\
  
  
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 5
```latex
\begin{table*}[tb!]
% \scriptsize
% % \centering
% % \vspace{-5pt}
% % \setlength{\abovecaptionskip}{0pt}
% % \setlength{\belowcaptionskip}{5pt}
% \caption{Experimental results (\%) on the Music and Sport dataset.}
% \label{musicsport}
% \setlength\tabcolsep{6pt}{
% \begin{tabular}{lccccccccccccccc}
% \toprule
% \multirow{3}{*}{\bf Methods} & \multicolumn{6}{c}{\bf Music Dataset} & \multicolumn{6}{c}{\bf Sport Dataset} & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Average\\Improv.}} 
% % & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Train\\Params}}   & \multirow{3}{*}{\parbox[c]{0.75cm}{\bfseries Infer\\Params}}
%    \\
% \cmidrule(r){2-7}\cmidrule{8-13}
%  & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG}  &\multirow{2}{*}{MRR}   & \multicolumn{3}{c}{HR} &\multicolumn{2}{c}{NDCG} & \multirow{2}{*}{MRR} \\
% \cmidrule(r){2-4}\cmidrule(r){5-6}\cmidrule(r){8-10}\cmidrule{11-12}  & @1   & @5  & @10 & @5 & @10 &   & @1  & @5  & @10 & @5  & @10 &       \\
% \midrule
% GRU4Rec  & 1.89   & 3.22     & 4.36 & 2.57   & 2.93   & 3.08   
%   & 5.26   & 7.75 & 9.64 & 6.52   & 7.13    & 7.08 & -41.93   \\
 
% BERT4Rec    &2.10    &3.16      &4.04  & 2.64  &2.92    & 3.11  & 4.81
%   & 6.70    & 7.98  & 5.79 & 6.20  & 6.26   & -46.82  \\

% SASRec    & 1.82   & 5.72      & 8.64 & 3.79   & 4.72    & 4.51   
%  & 4.70   & 8.43     & 11.21  & 6.59  & 7.48   & 7.24   &-30.60    \\
 
% \midrule
% % Open-P5$_\mathrm{T5}$~\citep{xu2023openp5}   &    &      &  &   &    &   &
% %   &    &  &  &   &    &   \\ 
  
% Open-P5   &  4.35  &   8.12   &  10.18& 6.74  & 7.83   &  - &5.49
%   &   8.5 & 11.28 & 6.92 & 7.65  &  -  &  -12.62 \\ 
  
% E4SRec*  & 5.62	& 9.29	& 11.64	& 7.50	& 8.26	& 7.98  
%    & 6.40   & 9.67     & 12.35 & 8.05  &  8.91   & 8.70   & 0.00  \\

% E4SRec$_{8}$*  & 5.46	& 8.86	& 11.14	& 7.21	& 7.95	& 7.74  
%   & 5.48   &  8.63    &  11.34 & 7.06  & 7.93    & 7.76   & -7.48    \\

% E4SRec$_{4}$*  & 5.33	& 8.75	& 10.94	& 7.08	& 7.78	& 7.59  
%   & 5.41   & 8.65     & 11.35  & 7.04   & 7.91   & 7.72   & -8.54     \\
  
% \midrule
  
% % $\OursDS{32}{32}$ &    &      &  &   &    &       & 2.00
% % &    &      &  &   &    &    &    & \\

% $\OursDS{8}{32}$ & 5.65    & 8.89     & 11.34  & 7.30   & 8.09    & 7.90   & 5.43
%   & 8.77   & 11.45     & 7.11  & 7.97  & 7.78   & -6.39     \\

% % $\OursDS{8}{8}$ & 16.07    & 18.84     & 21.24  & 17.46   & 18.23    & 18.15   & -3.44
% %   &    &  &  &   &    &  &    & \\

% $\OursDS{4}{32}$   & 5.26   &  8.55 & 10.88 &6.96   & 7.71    & 7.50  & 5.76   
%   &  8.91  & 11.45 & 7.35  & 8.17  & 8.02   & -7.56   \\ 
  
% $\OursDS{4}{8}$ & 5.62    & 8.78     & 11.09  & 7.23   & 7.97    & 7.81   & 6.25
%   & 9.25    &  11.68 & 7.76  & 8.54  & 8.41    & -3.55   \\

% \textbf{+$\mathcal{D}_{norm}$:}   &    &      &  &   &    &   &    &      &  &   &    &      &   \\ 

% $\OursDS{4}{8}$   & 5.95    & 9.26     & 11.68 & 7.65  &  8.42  & 8.23  & 6.61   & 9.82     &12.34  & 8.24  & 9.05   & 8.87     & +1.97  \\

% \textbf{+$\mathcal{L}_{ms}$:}   &    &      &  &   &    &   &    &      &  &   &    &      &   \\ 

% $\OursDS{4}{8}$  & 5.69   & 8.94     & 11.18  & 7.36  & 8.08   & 7.91  & 6.51
%   & 9.39   &  11.80 & 7.96 & 8.74  & 8.62    & -1.75   \\
  
% \textbf{+$\mathcal{D}_{norm}$+$\mathcal{L}_{ms}$:}   &    &      &  &   &    &   &    &      &  &   &    &      &   \\ 

% % $\OursDS{32}{32}$  &    &      &  &   &    &   &
% %   &    &  &  &   &    &  &    &  \\

% % $\OursDS{8}{32}$  & 
% %   &    &  &  &   &   & 
% %   &    &  &  &   &    &  &    &  \\

% % $\OursDS{4}{32}$   &    &  &  &   &    &  &    
% %   &    &  &  &   &    &  &    & \\
  
% $\OursDS{4}{8}$  & 5.72   & 9.15     & 11.45  & 7.48  & 8.21   & 8.03  & 6.62
%   & 9.83   &  12.34 & 8.25 & 9.06  & 8.89    & +0.81  \\

% % \midrule
% % \textbf{Online:}   &    &      &  &   &    &   &
% %   &    &  &  &   &    &  &    &  \\ 

% % $\OursDS{8}{32}$  &    &      &  &   &    &   &
% %   &    &  &  &   &    &  &    & \\

% % $\OursDS{4}{32}$   &    &  &  &   &    &  &    
% %   &    &  &  &   &    &  &    & \\
  
% % $\OursDS{4}{8}$  &  5.26  & 8.50      & 10.88  & 6.90  & 7.67   & 7.52   & 
% %   &    &  &  &   &    &  &    &  \\

% % \textbf{+cls:}   &    &      &  &   &    &   &
% %   &    &  &  &   &    &  &    &  \\ 

% % $\OursDS{8}{32}$  &    &      &  &   &    &   &
% %   &    &  &  &   &    &  &    & \\

% % $\OursDS{4}{32}$   &    &  &  &   &    &  &    
% %   &    &  &  &   &    &  &    & \\
  
% % $\OursDS{4}{8}$  & 5.48   & 8.54     & 10.90  &   &    &   &
% %   &    &  &  &   &    &  &    &  \\
  
  
% \bottomrule
% \end{tabular}
% }
% \end{table*}
```

## Table 6
```latex
\begin{table*}[tb!]
\centering
\caption{Experiment results (\%) of ablation study.
}
\vspace{-10pt}
\label{clothmovieablation}
% \setlength\tabcolsep{6pt}{
\begin{threeparttable}
        \setlength{\tabcolsep}{3mm}{ 
        \resizebox{\textwidth}{!}{
\begin{tabular}{l|cccc|cccc}
\midrule
\multirow{2}{*}{\textbf{$\Ours$}}  & \multicolumn{4}{c|}{\texttt{Cloth}} & \multicolumn{4}{c}{\texttt{Movie}} \\
% & \multirow{2}{*}{\textbf{Improv.(\%)}} \\
         & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR}  \\
\midrule
+$\mathcal{D}_{cos}$  & 16.10   & 18.85    
 & 17.48   
    & 18.17 
  & 14.83    & 23.08
   & 19.08  
      & 19.45 \\

+$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$  & 16.28   & 19.12
 & 17.69   
    & 18.40 
  &  14.86   & 23.89
   &   19.36
      & 19.84 \\
      
+$\mathcal{D}_{cos}$,$\mathcal{L}_{ms}$  & \textcolor{first}{\textbf{16.85}}   & 19.05    
 & 17.96  
    & 18.59 
  & 15.05    & 23.48
   & 19.40 
      & 19.76 \\
      
+$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$,$\mathcal{L}_{ms}$  & 16.69   & \textcolor{first}{\textbf{19.47}}    
 & \textcolor{first}{\textbf{18.07}}   
    & \textcolor{first}{\textbf{18.74}} 
  & \textcolor{first}{\textbf{15.29}}    & \textcolor{first} {\textbf{24.25}}
   & \textcolor{first} {\textbf{19.90}}  
      & \textcolor{first}{\textbf{20.36}} \\
      % & +1.49    \\
  
  
\midrule
\end{tabular}}}
	\end{threeparttable}
% \end{threeparttable}
\vspace{-10pt}
\end{table*}
```

## Table 7
```latex
\begin{table}[tb!]
\centering
\caption{Efficiency comparison of Open-P5, E4SRec, and our $\Ours$ in terms of epoch-wise training time (hours), inference time (hours), number of training parameters (B) and inference parameters (B). These comparisons were conducted on a machine with an A100 GPU. The training batch size for all models was standardized at 256. During inference, E4SRec and SLMREC utilized
a batch size of 512, whereas Open-P5’s inference was performed with a batch size of 1.
% \update{During inference, Open-P5 processes one sample at a time (batch size = 1), while other models leverage parallel processing with a batch size of 512. It should be noticed that E4SRec and SLMRec utilized a pre-trained embedding layer that did not count in the training parameters. Besides, we also show the average improvements of selected baselines and our method against SASRec.}
}
\vspace{-10pt}
\label{tbl:efficiency}
% Please add the following required packages to your document preamble:
% \usepackage{multirow}
\begin{threeparttable}
        \setlength{\tabcolsep}{3mm}{ 
        \resizebox{0.8\textwidth}{!}{
\begin{tabular}{l|cc|cc}
\midrule
\textbf{Method}
 & \textbf{Tr time(h)} & \textbf{Inf time(h)}  & \textbf{Tr params (B)} & \textbf{Inf params (B)} \\
 % & \update{\textbf{Improv. (\%)}} \\
 \hline
 % \update{SASRec} &0.014  & 0.015   & 0.007 &0.007  & 0.00 \\
 % \update{MAERec} & 0.086 & 0.089  & 0.008 &0.008 & 11.96 \\ \midrule
 Open-P5$_\mathrm{LLaMa}$ & 0.92 & 4942   & 0.023 &7.237  \\
 % &25.75 \\
 E4SRec &3.95 &0.415 & 0.023  & 6.631 \\ 
 % &43.39 \\
 %ANS-GT & 570.1 & 539.2 & 1.0 & 511.9 & 461.0 & 2.1 & - & - & -\\
    % E4SRec$_{4}$* & 0.90  & 0.083 & 0.003   & 0.944   \\
    \textbf{$\Ours$$_{4 \leftarrow 8}$} & 0.60   & 0.052  & 0.003 & 0.944 \\
    % & 45.26 \\
\midrule
% \vspace{-5pt}
\end{tabular}}}
	\end{threeparttable}
 \vspace{-15pt}
\end{table}
```

## Table 8
```latex
\begin{table*}[h!]
\centering
\footnotesize
% \setlength\tabcolsep{0.5pt}
% \setlength{\abovecaptionskip}{0pt}
% \setlength{\belowcaptionskip}{5pt}
% \captionsetup{font=small}
\caption{\centering Hyper-parameter (HP) settings of our method on each dataset.
}
\label{HPs}
\resizebox{\textwidth}{!}{
\begin{tabular}{l|c|c|c|c}
\toprule
\textbf{HP}\phantom{0} & \textbf{Cloth} & \textbf{Movie} &\textbf{ Music} & \textbf{Sport} \\ \midrule
adam\_beta1 & 0.9 & 0.9 & 0.9 & 0.9   \\
adam\_beta2 & 0.999 & 0.999 & 0.999 & 9.999 \\

adam\_epsilon & 1e-8 & 1e-8 & 1e-8 & 1e-8 \\
learning\_rate & 0.003 & 0.001 & 0.002 & 0.002\\
logging\_steps & 1 & 1 & 1 & 1 \\
lr\_scheduler\_type & cosine & cosine & cosine & cosine \\
max\_grad\_norm & 1.0 & 1.0 & 1.0 & 1.0 \\
max\_steps  &1500 & -1 & 800 & 2000 \\
optimizer &\phantom{0} adamw\_torch\phantom{0}  &\phantom{0} adamw\_torch\phantom{0}  & \phantom{0} adamw\_torch\phantom{0}  & \phantom{0} adamw\_torch\phantom{0}  \\
save\_strategy & steps & steps & steps & steps \\
save\_steps & 50 &100 & 100 & 100 \\ 
eval\_steps & 50 & 100 & 100 & 100\\
warmup\_steps & 50  &50 & 100 & 50 \\
$\lambda_1$ & 1.0 & 1.0 &1.0 & 1.0 \\
$\lambda_2$ & 0.1 & 0.1 & 0.1 & 0.1 \\
$\lambda_3$ & 1.0 & 1.0 & 0.01 & 0.1 \\
$b$ & 4 & 4 & 4 & 4 \\
\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 9
```latex
\begin{table*}[tb!]
\footnotesize
% \setlength\tabcolsep{0.5pt}
% \setlength{\abovecaptionskip}{0pt}
% \setlength{\belowcaptionskip}{5pt}
% \captionsetup{font=small}
\caption{\centering Detailed efficiency comparison of Open-P5, E4SRec, and our $\Ours$, in terms of training and inference time, on each dataset.
}
\label{Main Results}
\resizebox{\textwidth}{!}{
\begin{tabular}{l|cc|cc|cc|cc}
\toprule
\multirow{2}{*}{\phantom{0}\textbf{Method} \phantom{0}} & \multicolumn{2}{c|}{\textbf{Cloth}\phantom{0}} & \multicolumn{2}{c|}{\textbf{Movie} \phantom{0}} & \multicolumn{2}{c|}{\textbf{Music}\phantom{0}} & \multicolumn{2}{c}{\textbf{Sport}}\\ \cline{2-9}
   & \phantom{0} Tr time  (h)  & \phantom{0}  Inf time (h) & \phantom{0} Tr time (h)  & \phantom{0}  Inf time (h) & \phantom{0} Tr time (h)  & \phantom{0}  Inf time (h) &\phantom{0}  Tr time (h)  & \phantom{0}  Inf time (h) \\
\midrule 
\midrule
Open-P5$_\mathrm{LLaMa}$ &1.36 	&3554.43 &0.36 &3504					&0.35 	&3692 	&1.60 	&9017 \\ \midrule
E4SRec &5.27 	&0.578	&1.90 	&0.208 	&1.88 	&0.216  &6.75 	&0.660\\ \midrule
\textbf{$\Ours$$_{4 \leftarrow 8}$} & 0.97 	&0.070 	&0.15 	&0.030 					&0.30 	&0.030 	&0.98 	&0.078\\ 

\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 10
```latex
\begin{table}[tb!]
\centering
\caption{\update{Efficiency comparison of SASRec, MAERec and our $\Ours$ in terms of epoch-wise inference time (hours). These comparisons were conducted on a machine with an A100 GPU.  During inference,  models leverage parallel processing with a batch size of 512.}
% \update{During inference, Open-P5 processes one sample at a time (batch size = 1), while other models leverage parallel processing with a batch size of 512. It should be noticed that E4SRec and SLMRec utilized a pre-trained embedding layer that did not count in the training parameters. Besides, we also show the average improvements of selected baselines and our method against SASRec.}
}
\label{appendix:tbl:efficiency}
% Please add the following required packages to your document preamble:
% \usepackage{multirow}
\begin{threeparttable}
        \setlength{\tabcolsep}{3mm}{ 
        \resizebox{0.45\textwidth}{!}{
\begin{tabular}{l|c|c}
\midrule
\textbf{Method}
 & \textbf{Inf time(h)}   
 & \textbf{Improv. (\%)} \\
 \hline
 SASRec   & 0.015    & 0.00 \\
 MAERec  & 0.061   & 11.96 \\ \midrule
 % Open-P5$_\mathrm{LLaMa}$  & 4942   
 % &25.75 \\
 % E4SRec  &0.415  
 %  &43.39 \\
    \textbf{$\Ours$$_{4 \leftarrow 8}$}  & 0.052  & 45.26 \\
\midrule
% \vspace{-5pt}
\end{tabular}}}
	\end{threeparttable}
\end{table}
```

## Table 11
```latex
\begin{table*}[tb!]
\centering
\caption{Experiment results (\%) of ablation study.
}
\vspace{-5pt}
\label{musicsportablation}
% \setlength\tabcolsep{6pt}{
\begin{threeparttable}
        \setlength{\tabcolsep}{3mm}{ 
        \resizebox{\textwidth}{!}{
\begin{tabular}{l|cccc|cccc}
\midrule
\multirow{2}{*}{\textbf{$\Ours$}}  & \multicolumn{4}{c|}{\texttt{Music}} & \multicolumn{4}{c}{\texttt{Sport}} \\
% & \multirow{2}{*}{\textbf{Improv.(\%)}} \\
         & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR} & \textbf{HR@1} & \textbf{HR@5}  & \textbf{NDCG@5} & \textbf{MRR}  \\
\midrule
+$\mathcal{D}_{cos}$  & 5.62   & 8.78   
 & 7.23   
    & 7.81 
  & 6.25    & 9.25
   & 7.76  
      & 8.41 \\

+$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$  & \textcolor{first}{\textbf{5.95}}   & \textcolor{first}{\textbf{9.26}}
 & \textcolor{first}{\textbf{7.65}} 
    & \textcolor{first}{\textbf{8.23}} 
  &  6.61   & 9.82
   &   8.24
      & 8.87 \\
      
+$\mathcal{D}_{cos}$,$\mathcal{L}_{ms}$  & 5.69   & 8.94    
 & 7.36  
    & 7.91
  & 6.51    & 9.39
   & 7.96 
      & 8.62 \\
      
+$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$,$\mathcal{L}_{ms}$  & 5.72   & 9.15   
 & 7.48 
    & 8.03
  & \textcolor{first}{\textbf{6.62}}    & \textcolor{first} {\textbf{9.83}}
   & \textcolor{first} {\textbf{8.25}}  
      & \textcolor{first}{\textbf{8.89}} \\
      % & +1.49    \\
  
  
\midrule
\end{tabular}}}
	\end{threeparttable}
% \end{threeparttable}
\vspace{-5pt}
\end{table*}
```

