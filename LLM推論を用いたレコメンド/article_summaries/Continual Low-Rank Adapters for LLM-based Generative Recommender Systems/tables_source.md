# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}
% \caption{\TODO \hs{table method and values are going to be updated. as well as the interpretation}}
% \resizebox{0.98\textwidth}{!}{
% %\begin{tabular}{cccc|ccc}
% \begin{tabular}{c R{2.6cm} R{2.6cm} R{2cm}| R{2.6cm} R{2.6cm} R{2cm}}
% \toprule
%  & \multicolumn{3}{c|}{{Hit@10}} & \multicolumn{3}{c}{NDCG@10} \\
% \multirow{-2}{*}{} & \textbf{User-disjoint} & \textbf{Natural split} & \textbf{Diff. (C1-C2)} & \textbf{User-disjoint} & \textbf{Natural split} & \textbf{Diff. (C1-C2)} \\ \midrule
% \multicolumn{1}{c|}{$\cloraall$} & -10.16  & -15.02 & 4.86 & -13.89 & -15.33 & 1.44 \\
% \multicolumn{1}{c|}{$\cloraallinherit$} & -6.91 & -8.3 & 1.39 & -6.25 & -9.33 & 3.08 \\
% \multicolumn{1}{c|}{$\cloralatestinherit$} & 3.66 & 0.79 & 2.87 & 2.08 & 1.33 & 0.75 \\
% \multicolumn{1}{c|}{$\sdloraall$} & -11.38 & -18.58 & 7.19 & -14.58 & -18.67 & 4.08 \\
% \multicolumn{1}{c|}{$\sdloraallinherit$} &  & -10.67 &  &  & -11.33 &  \\
% \multicolumn{1}{c|}{$\sdloralatestinherit$} & 6.1 & 0.4 & 5.7 & 4.86 & 0 & 4.86 \\ \bottomrule
% \end{tabular}
% }\label{tab:cumulative_analysis}
% \end{table*}
```

## Table 2
```latex
\begin{table}[t]
% \centering
% \caption{\TODO   \hs{need too think about the good way to represent each method (now it's too complex e.g., latest+inherit)}}
% \small
% \resizebox{1.00\textwidth}{!}{
% \begin{tabular}{l|ccc| S[table-format=+2.2] S[table-format=+2.2] S[table-format=+2.2]}
% \toprule
% \multicolumn{1}{l|}{} &
% \multicolumn{3}{c|}{\textbf{Design choices}} &
% \multicolumn{3}{c}{\textbf{Task settings}} \\
% \multicolumn{1}{l|}{\textbf{Method}} & \textbf{Learnable mag.} & \textbf{Only latest} & \textbf{Param inherit} & \textbf{(1) User-disjoint}      & \textbf{(2) Natural split} & \textbf{Diff. (1)-(2)} \\ \midrule
% $\cloraall$            &            &            &            & $-8.33\%$ & $-20.67\%$ & $12.33$ \\
% $\cloralatest$         &            & \checkmark &            & $-11.81\%$ & $-17.33\%$ & $5.53$ \\
% $\cloraallinherit$     &            &            & \checkmark & $0.69\%$ & $2.67\%$ & $-1.97$ \\
% $\cloralatestinherit$  &            & \checkmark & \checkmark & $2.08\%$ & $1.33\%$ & $0.75$ \\
% \midrule
% $\sdloraall$           & \checkmark &            &            & $-11.11\%$ & $-14.00\%$ & $2.89$ \\
% $\sdloralatest$        & \checkmark & \checkmark &            & $-15.28\%$ & $-18.00\%$ & $2.72$ \\
% $\sdloraallinherit$    & \checkmark &            & \checkmark & $-7.64\%$ & $-4.00\%$ & $-3.64$ \\
% $\sdloralatestinherit$ & \checkmark & \checkmark & \checkmark & $4.86\%$ & $0.00\%$ & $4.86$ \\
% \bottomrule
% \end{tabular}}
% \label{tab:cumul_analysis}
% \end{table}
```

## Table 3
```latex
\begin{table}[t]
% \centering
% \caption{\TODO \hs{need to think about a cleaner way to represent each method (now it's too complex, e.g., latest+inherit)}}
% \small
% \resizebox{1.00\textwidth}{!}{
% \begin{tabular}{l|ccc| r r r}
% \toprule
% \multicolumn{1}{l|}{} &
% \multicolumn{3}{c|}{\textbf{Design choices}} &
% \multicolumn{3}{c}{\textbf{Task settings}} \\
% \multicolumn{1}{l|}{\textbf{Method}} & \textbf{Learnable mag.} & \textbf{Only latest} & \textbf{Param inherit} & \textbf{(1) User-disjoint} & \textbf{(2) Natural split} & \textbf{Diff. (1)-(2)} \\ \midrule
% $\cloraall$            &            &            &            & $-8.33\%$  & $-20.67\%$ & $12.33$ \\
% $\cloralatest$         &            & \checkmark &            & $-11.81\%$ & $-17.33\%$ & $5.53$  \\
% $\cloraallinherit$     &            &            & \checkmark & $0.69\%$   & $2.67\%$   & $-1.97$ \\
% $\cloralatestinherit$  &            & \checkmark & \checkmark & $2.08\%$   & $1.33\%$   & $0.75$  \\
% \midrule
% $\sdloraall$           & \checkmark &            &            & $-11.11\%$ & $-14.00\%$ & $2.89$  \\
% $\sdloralatest$        & \checkmark & \checkmark &            & $-15.28\%$ & $-18.00\%$ & $2.72$  \\
% $\sdloraallinherit$    & \checkmark &            & \checkmark & $-7.64\%$  & $-4.00\%$  & $-3.64$ \\
% $\sdloralatestinherit$ & \checkmark & \checkmark & \checkmark & $4.86\%$   & $0.00\%$   & $4.86$  \\
% \bottomrule
% \end{tabular}}
% \label{tab:cumul_analysis}
% \end{table}
```

## Table 4
```latex
\begin{table}[t]
% \centering
% \caption{(Left) Design choices; (Right) performance gain vs. single evolving LoRA in different task settings on Instrument dataset. \TODO[conclusion, coonsider removing all+inherit?]
% % \tw{can we have some short conclusion in the caption? or some bold/underline in the table}\hs{kinda worried if the all+inherit would blur our claims because the diff (1)-(2) is smaller than latest+inherit} 
% % %\hs{need to think about a cleaner way to represent each method (now it's too complex, e.g., latest+inherit)} 
% % \tw{yeah i think the issue here is that whether reader can directly grasp the information here, we don't need to show everything, just the thing aligning with what you wanna convey?}
% }
% \small
% \resizebox{1.00\textwidth}{!}{
% \begin{tabular}{l|ccc| r r r}
% \toprule
% \multicolumn{1}{l|}{} &
% \multicolumn{3}{c|}{\textbf{Design choices}} &
% \multicolumn{3}{c}{\textbf{Task settings}} \\
% \multicolumn{1}{l|}{\textbf{Method}} & \textbf{Learnable mag.} & \textbf{Only latest} & \textbf{Param inherit} & \textbf{(1) User-disjoint} & \textbf{(2) Natural split} & \textbf{Diff. (1)-(2)} \\ \midrule
% \cloraall          & \xmark & \xmark & \xmark & $-8.33\%$  & $-20.67\%$ & \pos{$12.33$} \\
% \cloralatest      & \xmark & \cmark & \xmark & $-11.81\%$ & $-17.33\%$ & \pos{$5.53$}  \\
% \cloraallinherit    & \xmark & \xmark & \cmark & \underline{$0.69\%$}   & $\textbf{2.67}\%$   & \negc{$-1.97$} \\
% \cloralatestinherit  & \xmark & \cmark & \cmark & {$\textbf{2.08}\%$}\   & $\underline{1.33}\%$   & \pos{$0.75$}  \\
% \midrule
% \sdloraall           & \cmark & \xmark & \xmark & $-11.11\%$ & $-14.00\%$ & \pos{$2.89$}  \\
% \sdloralatest        & \cmark & \cmark & \xmark & $-15.28\%$ & $-18.00\%$ & \pos{$2.72$}  \\
% \sdloraallinherit    & \cmark & \xmark & \cmark & $\underline{-7.64}\%$  & $\underline{-4.00}\%$  & \negc{$-3.64$} \\
% \sdloralatestinherit & \cmark & \cmark & \cmark & $\textbf{4.86}\%$   & $\textbf{0.00}\%$   & \pos{$4.86$}  \\
% \bottomrule
% \end{tabular}}
% \label{tab:cumul_analysis}
% \vspace{-3mm}
% \end{table}
```

## Table 5
```latex
\begin{table}[t]
% \centering
% \caption{(Left) Design choices; (Right) performance gain vs. single evolving LoRA (w.r.t. NDCG@5) in different task settings on Instrument dataset.}
% \small
% \resizebox{1.00\textwidth}{!}{
% \begin{tabular}{l|ccc| r r r}
% \toprule
% \multicolumn{1}{l|}{} &
% \multicolumn{3}{c|}{\textbf{Design choices}} &
% \multicolumn{3}{c}{\textbf{Task settings}} \\
% \multicolumn{1}{l|}{\textbf{Method}} & \textbf{Learnable mag.} & \textbf{Only latest} & \textbf{Param inherit} & \textbf{(1) User-disjoint} & \textbf{(2) Natural split} & \textbf{Diff. (1)-(2)} \\ \midrule
% \cloraall            & \xmark & \xmark & \xmark & $-8.13\%$  & $-26.77\%$ & \pos{$18.64$} \\
% \cloralatest         & \xmark & \cmark & \xmark & $-12.20\%$ & $-22.05\%$ & \pos{$9.85$}  \\
% \cloraallinherit     & \xmark & \xmark & \cmark & $-3.25\%$  & $1.57\%$   & \negc{$-4.82$} \\
% \cloralatestinherit  & \xmark & \cmark & \cmark & $0.00\%$   & $2.36\%$   & \negc{$-2.36$} \\
% \midrule
% \sdloraall           & \cmark & \xmark & \xmark & $-12.20\%$ & $-15.75\%$ & \pos{$3.55$}  \\
% \sdloralatest        & \cmark & \cmark & \xmark & $-17.07\%$ & $-19.69\%$ & \pos{$2.62$}  \\
% \sdloraallinherit    & \cmark & \xmark & \cmark & $-9.76\%$  & $-2.36\%$  & \negc{$-7.40$} \\
% \sdloralatestinherit & \cmark & \cmark & \cmark & $3.25\%$   & $0.79\%$   & \pos{$2.46$}  \\
% \bottomrule
% \end{tabular}}
% \label{tab:cumul_analysis}
% \vspace{-3mm}
% \end{table}
```

## Table 6
```latex
\begin{table}[t]
\centering
\caption{(Left) Design choices; (Right) performance gain vs. single evolving LoRA (w.r.t. NDCG@5) in different task settings on Instrument dataset.}
% \vspace{-1mm}
\vspace{-1em}
\small
\resizebox{1.00\textwidth}{!}{
\begin{tabular}{l|ccc| r r r}
\toprule
\multicolumn{1}{l|}{} &
\multicolumn{3}{c|}{\textbf{Design choices}} &
\multicolumn{3}{c}{\textbf{Task settings}} \\
\multicolumn{1}{l|}{\textbf{Method}} & \textbf{Learnable mag.} & \textbf{Only latest} & \textbf{Param inherit} & \textbf{(1) User-disjoint} & \textbf{(2) Natural split} & \textbf{Diff. (1)-(2)} \\ \midrule
\cloraall            & \xmark & \xmark & \xmark & $-8.13\%$  & $-26.77\%$ & \pos{$18.64\%$} \\
\cloralatest         & \xmark & \cmark & \xmark & $-12.20\%$ & $-22.05\%$ & \pos{$9.85\%$}  \\
\cloraallinherit     & \xmark & \xmark & \cmark & $-3.25\%$  & $1.57\%$   & \negc{$-4.82\%$} \\
\cloralatestinherit  & \xmark & \cmark & \cmark & $0.00\%$   & $2.36\%$   & \negc{$-2.36\%$} \\
% \midrule
% \sdloraall           & \cmark & \xmark & \xmark & $-12.20\%$ & $-15.75\%$ & \pos{$3.55$}  \\
% \sdloralatest        & \cmark & \cmark & \xmark & $-17.07\%$ & $-19.69\%$ & \pos{$2.62$}  \\
% \sdloraallinherit    & \cmark & \xmark & \cmark & $-9.76\%$  & $-2.36\%$  & \negc{$-7.40$} \\
\sdloralatestinherit & \cmark & \cmark & \cmark & $3.25\%$   & $0.79\%$   & \pos{$2.46\%$}  \\
\bottomrule
\end{tabular}}
\label{tab:cumul_analysis}
% \vspace{-3mm}
\vspace{-2em}
\end{table}
```

## Table 7
```latex
\begin{table}[t]
% \centering
% \caption{(Left) Design choices; (Right) performance gain vs. single evolving LoRA in different task settings on Instrument dataset. \TODO[conclusion, coonsider removing all+inherit?]
% }
% \small
% \resizebox{1.00\textwidth}{!}{
% \begin{tabular}{l|ccc| r r r}
% \toprule
% \multicolumn{1}{l|}{} &
% \multicolumn{3}{c|}{\textbf{Design choices}} &
% \multicolumn{3}{c}{\textbf{Task settings}} \\
% \multicolumn{1}{l|}{\textbf{Method}} & \textbf{Learnable mag.} & \textbf{Only latest} & \textbf{Param inherit} & \textbf{(1) User-disjoint} & \textbf{(2) Natural split} & \textbf{Diff. (1)-(2)} \\ \midrule
% \cloraall          & \xmark & \xmark & \xmark & $-8.33\%$  & $-20.67\%$ & \pos{$12.33$} \\
% \cloralatest      & \xmark & \cmark & \xmark & $-11.81\%$ & $-17.33\%$ & \pos{$5.53$}  \\
% % \cloraallinherit    & \xmark & \xmark & \cmark & \underline{$0.69\%$}   & $\textbf{2.67}\%$   & \negc{$-1.97$} \\
% \cloralatestinherit  & \xmark & \cmark & \cmark & {$\textbf{2.08}\%$}\   & $\underline{1.33}\%$   & \pos{$0.75$}  \\
% % \midrule
% % \sdloraall           & \cmark & \xmark & \xmark & $-11.11\%$ & $-14.00\%$ & \pos{$2.89$}  \\
% % \sdloralatest        & \cmark & \cmark & \xmark & $-15.28\%$ & $-18.00\%$ & \pos{$2.72$}   \\
% % \sdloraallinherit    & \cmark & \xmark & \cmark & $\underline{-7.64}\%$  & $\underline{-4.00}\%$  & \negc{$-3.64$} \\
% \sdloralatestinherit & \cmark & \cmark & \cmark & $\textbf{4.86}\%$   & $\textbf{0.00}\%$   & \pos{$4.86$}  \\
% \bottomrule
% \end{tabular}}
% \label{tab:cumul_analysis}
% \vspace{-3mm}
% \end{table}
```

## Table 8
```latex
\begin{table}[t]
%   \centering
%   \caption{Ablations. Positive \textit{diff.} indicates improvement.}
%   \small
%   \begin{tabular}{
%     l % method
%     c c c  % flags
%     S[table-format=+2.2] % disjoint
%     S[table-format=+2.2] % natural
%     S[table-format=+2.2] % diff
%   }
%   \toprule
%   \textbf{Method} &
%   \textbf{learnable mag} &
%   \textbf{only latest} &
%   \textbf{param inherit} &
%   {\textbf{disjoint}} &
%   {\textbf{natural}} &
%   {\textbf{diff.}} \\
%   \midrule
%   $\cloraall$              &        &           &           &  \num{-8.33} & \num{-20.67} & \num{12.33} \\
%   $\cloralatest$           &        & \checkmark &           & \num{-11.81} & \num{-17.33} & \num{ 5.53} \\
%   $\cloraallinherit$       &        &           & \checkmark &  \num{ 0.69} &  \num{ 2.67} & \num{-1.97} \\
%   $\cloralatestinherit$    &        & \checkmark & \checkmark &  \num{ 2.08} &  \num{ 1.33} & \num{ 0.75} \\
%   \midrule
%   $\sdloraall$             & \checkmark &        &           & \num{-11.11} &  \num{-14.00} & \num{ 2.89} \\
%   $\sdloralatest$          & \checkmark & \checkmark &       & \num{-15.28} &  \num{-18.00} & \num{ 2.72} \\
%   $\sdloraallinherit$      & \checkmark &        & \checkmark &  \num{-7.64} &   \num{-4.00} & \num{-3.64} \\
%   $\sdloralatestinherit$   & \checkmark & \checkmark & \checkmark & \num{ 4.86} &   \num{ 0.00} & \num{ 4.86} \\
%   \bottomrule
%   \end{tabular}
% \end{table}
```

## Table 9
```latex
\begin{table}[t]
  \centering
  \small
  \caption{Recommendation performance averaged across time stages for \ours\ and continual competitors. The best and second-best results are marked in \textbf{bold} and \underline{underline}, respectively. 
  }
\vspace{-1em}
  % \vspace{-1mm}
  \resizebox{\linewidth}{!}{
\begin{tabular}{lcccccccccccc}
\toprule
\multicolumn{1}{c}{\textbf{}} &
\multicolumn{4}{c}{\textbf{Instruments}} &
\multicolumn{4}{c}{\textbf{Movies \& TVs}} &
\multicolumn{4}{c}{\textbf{Books}} \\
\multicolumn{1}{l}{\textbf{Methods}}  & 
\textbf{H@5} & \textbf{H@10} & \textbf{N@5} & \textbf{N@10} &
\textbf{H@5} & \textbf{H@10} & \textbf{N@5} & \textbf{N@10} &
\textbf{H@5} & \textbf{H@10} & \textbf{N@5} & \textbf{N@10} \\
\midrule\addlinespace[-0.000ex]
\rowcolor{red!5}
\textsc{Pretrain} & 0.0166 & 0.0216 & 0.0115 & 0.0131 & 0.0166 & 0.0231 & 0.0111 & 0.0132 & 0.0258 & 0.0283 & 0.0196 & 0.0204 \\ 
[-0.4ex]\midrule\addlinespace[-0.000ex]
\rowcolor{orange!7}
\textsc{Single evolving LoRA} & 0.0181 & 0.0253 & 0.0127 & 0.0150 & \underline{0.0175} & \underline{0.0247} & \underline{0.0116} & \underline{0.0138} & \textbf{0.0448} & \underline{0.0557} & \underline{0.0308} & \underline{0.0344} \\ 
[-0.4ex]\midrule\addlinespace[-0.000ex]
\rowcolor{yellow!5}
Cumulative LoRA Family & & & & & & & & & & & & \\
\hdashline
\rowcolor{yellow!10}
\infall            & 0.0156 & 0.0214 & 0.0105 & 0.0124 & 0.0103 & 0.0139 & 0.0067 & 0.0079 & 0.0236 & 0.0332 & 0.0161 & 0.0193 \\
\rowcolor{yellow!10}
\inflatest        & 0.0131 & 0.0167 & 0.0090 & 0.0102 & 0.0073 & 0.0092 & 0.0047 & 0.0054 &   0.0152   &  0.0197      &    0.0108    &   0.0123       \\
\rowcolor{yellow!10}
\infallinherit     & 0.0149 & 0.0219 & 0.0104 & 0.0126 & 0.0109 & 0.0147 & 0.0072 & 0.0085 & 0.0249 & 0.0324 & 0.0171 & 0.0195 \\
\rowcolor{yellow!10}
\inflatestinherit  & 0.0137 & 0.0202 & 0.0095 & 0.0116 & 0.0094 & 0.0132 & 0.0060 & 0.0072 & 0.0225 & 0.0288 & 0.0153 & 0.0174 \\
\hdashline
\rowcolor{green!5}
\cloraall & 0.0134 & 0.0215 & 0.0093 & 0.0119 & 0.0102 & 0.0130 & 0.0067 & 0.0076 & 0.0264 & 0.0402 & 0.0176 & 0.0221 \\
\rowcolor{green!5}
\cloralatest & 0.0143 & 0.0221 & 0.0099 & 0.0124 & 0.0102 & 0.0130 & 0.0067 & 0.0076 & 0.0246 & 0.0354 & 0.0161 & 0.0196 \\
\rowcolor{green!5}
\cloraallinherit & 0.0182 & \underline{0.0260} & 0.0129 & \underline{0.0154} & 0.0160 & 0.0234 & 0.0107 & 0.0131 & 0.0409 & 0.0514 & 0.0287 & 0.0321 \\
\rowcolor{green!5}
\cloralatestinherit & \underline{0.0185} & 0.0255 & \underline{0.0130} & 0.0152 & 0.0172 & 0.0237 & 0.0114 & 0.0135 & 0.0433 & 0.0542 & 0.0306 & 0.0341 \\
\hdashline
\rowcolor{LavenderLight!20}
\sdloraall & 0.0156 & 0.0226 & 0.0107 & 0.0129 & 0.0094 & 0.0133 & 0.0061 & 0.0074 & 0.0238 & 0.0351 & 0.0162 & 0.0198 \\
\rowcolor{LavenderLight!20}
\sdloralatest & 0.0156 & 0.0218 & 0.0102 & 0.0123 & 0.0101 & 0.0142 & 0.0069 & 0.0082 & 0.0241 & 0.0327 & 0.0159 & 0.0186 \\
\rowcolor{LavenderLight!20}
\sdloraallinherit & 0.0176 & 0.0238 & 0.0124 & 0.0144 & 0.0118 & 0.0171 & 0.0077 & 0.0094 & 0.0332 & 0.0412 & 0.0234 & 0.0260 \\
\rowcolor{LavenderLight!20}
\sdloralatestinherit & 0.0184 & 0.0254 & 0.0128 & 0.0150 & 0.0165 & 0.0235 & 0.0109 & 0.0131 & 0.0432 & 0.0530 & \underline{0.0308} & 0.0340 \\
[-0.4ex]\midrule\addlinespace[0.000ex]
\rowcolor{gray!20} \textbf{\ours} & \textbf{0.0193} & \textbf{0.0268} & \textbf{0.0138} & \textbf{0.0162} & \textbf{0.0180} & \textbf{0.0251} & \textbf{0.0118} & \textbf{0.0141} & \textbf{0.0448} & \textbf{0.0569} & \textbf{0.0311} & \textbf{0.0351} \\
[-0.4ex]\midrule\addlinespace[-0.000ex]
\rowcolor{gray!10}\textbf{Performance Gain} (\%) & & & & & & & & & & & &\\
\hdashline
\rowcolor{gray!5}\textsc{vs.} \single & 6.63\% & 5.93\% & 8.66\% & 8.00\% & 2.86\% & 1.62\% & 1.72\% & 2.17\% & 0.00\% & 2.15\% & 0.97\% & 2.03\% \\
\rowcolor{gray!5}
\textsc{vs.} \cloralatestinherit & 4.32\% & 5.10\% & 6.15\% & 6.58\% & 4.65\% & 5.91\% & 3.51\% & 4.44\% & 3.46\% & 4.98\% & 1.63\% & 2.93\% \\
\rowcolor{gray!5}
\textsc{vs.} \sdloralatestinherit & 4.89\% & 5.51\% & 7.81\% & 8.00\% & 9.09\% & 6.81\% & 8.26\% & 7.63\% & 3.70\% & 7.36\% & 0.97\% & 3.24\% \\
\bottomrule
\end{tabular}}
\label{tab:main}
% \vspace{-3mm}
\vspace{-1.5em}
\end{table}
```

## Table 10
```latex
\begin{table}[]
  \centering\caption{Dataset statistics.}
  \resizebox{\linewidth}{!}{
\begin{tabular}{cl|rrrrrrr}
\hline
\multicolumn{1}{l}{} &  & Total Users & New Users & Total Items & New Items & Total Interactions & Avg Seq Len & Sparsity \\ \toprule
\multirow{6}{*}{Instruments} & $\CAL D_1$ & 17,046 & 17,046 & 40,471 & 40,471 & 141,788 & 8.32 & 0.9998 \\
 & $\CAL D_2$ & 1,772 & 1,183 & 8,346 & 2,900 & 13,197 & 7.45 & 0.9991 \\
 & $\CAL D_3$ & 1,821 & 1,265 & 8,325 & 2,909 & 13,334 & 7.32 & 0.9991 \\
 & $\CAL D_4$ & 2,289 & 1,684 & 9,617 & 3,864 & 18,811 & 8.22 & 0.9991 \\
 & $\CAL D_5$ & 2,238 & 1,699 & 9,131 & 3,365 & 17,573 & 7.85 & 0.9991 \\
\rowcolor{gray!20} & $\CAL D_{1:5}$ & 22,877 & NA & 53,509 & NA & 204,703 & NA & NA \\ \midrule
\multirow{6}{*}{Movies \& TVs} & $\CAL D_1$ & 17,928 & 17,928 & 39,228 & 39,228 & 190,411 & 10.62 & 0.9997 \\
 & $\CAL D_2$ & 1,866 & 1,141 & 11,612 & 1,479 & 17,665 & 9.47 & 0.9992 \\
 & $\CAL D_3$ & 2,106 & 1,200 & 12,658 & 1,926 & 19,874 & 9.44 & 0.9993 \\
 & $\CAL D_4$ & 2,284 & 1,357 & 13,788 & 1,882 & 22,929 & 10.04 & 0.9993 \\
 & $\CAL D_5$ & 2,332 & 1,552 & 13,491 & 1,559 & 22,225 & 9.53 & 0.9993 \\
 \rowcolor{gray!20}& $\CAL D_{1:5}$ & 23,178 & NA & 46,074 & NA & 273,104 & NA & NA \\ \midrule
\multirow{6}{*}{Books} & $\CAL D_1$ & 15,406 & 15,406 & 35,984 & 35,984 & 164,858 & 10.7 & 0.9997 \\
 & $\CAL D_2$ & 1,807 & 618 & 7,155 & 2,711 & 13,918 & 7.7 & 0.9989 \\
 & $\CAL D_3$ & 1,672 & 619 & 6,484 & 2,278 & 12,395 & 7.41 & 0.9989 \\
 & $\CAL D_4$ & 1,948 & 650 & 7,154 & 2,657 & 14,824 & 7.61 & 0.9989 \\
 & $\CAL D_5$ & 1,652 & 1,025 & 5,913 & 2,274 & 11,990 & 7.26 & 0.9988 \\
 \rowcolor{gray!20}& $\CAL D_{1:5}$ & 18,318 & NA & 45,904 & NA & 217,985 & NA & NA \\ \bottomrule
\end{tabular}}
\label{tab:datasets}
\end{table}
```

## Table 11
```latex
\begin{table}[t]
% \centering
% \caption{Performance comparison across three datasets.}
% \small
% \begin{tabular}{lccc}
% \toprule
% \textbf{Method} & \textbf{Instruments} & \textbf{Movies \& TVs} & \textbf{Books} \\ \midrule
% Pretrain              & 0.0153 & 0.0028 & 0.0041 \\
% Fine-tuning           & 0.0180 & 0.0114 & 0.0218 \\
% PISA                  & 0.0194 & 0.0106 & 0.0301 \\
% Pretrain              & 0.0157 & 0.0160 & 0.0235 \\
% Single evolving LoRA  & 0.0178 & 0.0169 & 0.0414 \\
% PESO                  & 0.0190 & 0.0173 & 0.0422 \\
% \bottomrule
% \end{tabular}
% \label{tab:baseline_results}
% \end{table}
```

## Table 12
```latex
\begin{table}[]
\caption{Comparison of LLM-based and traditional methods in continual recommendation.}
\centering
\small
\begin{tabular}{cc|ccc}
\toprule
 &  & Instruments & Movies \& TVs & Books \\ \midrule
\multirow{5}{*}{Traditional two-tower} & Pretrain & 0.0153 & 0.0028 & 0.0041 \\
 & Fine-tuning & 0.0180 & 0.0114 & 0.0218 \\
 & Contrastive & 0.0177 & 0.0101 & 0.0272 \\
 & Contrastive + PIW & 0.0193 & 0.0113 & 0.0243 \\
 & PISA & 0.0194 & 0.0106 & 0.0301 \\ \midrule
\multirow{3}{*}{LLM-based } & Pretrain & 0.0157 & 0.0160 & 0.0235 \\
 & Fine-tuning (w/ LoRA) & 0.0178 & 0.0169 & 0.0414 \\
 & PESO & 0.0190 & 0.0173 & 0.0422 \\
 \bottomrule
\end{tabular}\label{tab:traditional}
\end{table}
```

