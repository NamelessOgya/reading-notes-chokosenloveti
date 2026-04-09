# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[t]
\centering
\scriptsize
\setlength{\tabcolsep}{1.8pt}
\renewcommand{\arraystretch}{1.1} % Very tight to fit 15 columns
\caption{Comparison on Systems \& Data benchmarks. We report \textbf{Mean $\pm$ Std} and \textbf{Best}. Higher is better for all metrics except \textbf{Cloudcast} ($\downarrow$). \textbf{Bold} indicates best automated strategy. \underline{Underline} indicates results surpassing \textbf{Human SOTA}. Detailed explanations of these benchmarks are given in \cref{tab:adrs_systems}.}
\label{tab:systems-bench}

\makebox[\textwidth][c]{\begin{tabular}{l cc cc cc cc cc cc cc}
\toprule
& \multicolumn{2}{c}{\textbf{Telemetry}} & \multicolumn{2}{c}{\textbf{Cloudcast} $\downarrow$} & \multicolumn{2}{c}{\textbf{EPLB}} & \multicolumn{2}{c}{\textbf{Prism}} & \multicolumn{2}{c}{\textbf{LLM-SQL}} & \multicolumn{2}{c}{\textbf{TXN}} & \multicolumn{2}{c}{\textbf{NS3}} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7} \cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}
\textbf{Strategy} & Avg & Best & Avg & Best & Avg & Best & Avg & Best & Avg & Best & Avg & Best & Avg & Best \\
\midrule
\textbf{Human / SOTA} & --  & 0.822 & -- & 626.2 & -- & 0.1265 & -- & 21.89 & -- & 0.692 & -- & 2,725 & -- & 69.0 \\
\midrule
\multicolumn{15}{l}{\textit{Backbone: GPT-5}} \\
OE & .930 $\pm$ .04 & .952 & 926.9 $\pm$ 171 & 729.8 & .127 $\pm$ .00 & .1272 & 26.23 $\pm$ .00 & 26.23 & .710 $\pm$ .01 & .716 & 4,239 $\pm$ 90 & 4,329 & 92.2 $\pm$ 4.8 & 97.3 \\
GEPA & .916 $\pm$ .05 & .948 & 689.9 $\pm$ 74 & 645.7 & .134 $\pm$ .01 & .1445 & 26.19 $\pm$ .07 & 26.23 & .713 $\pm$ .00 & .713 & 3,753 $\pm$ 204 & 3,984 & 68.9 $\pm$ .00 & 101.8 \\
Shinka & .923 $\pm$ .04 & .952 & 954.8 $\pm$ 125 & 812.7 & .118 $\pm$ .01 & .1272 & 26.26 $\pm$ .00 & 26.26 & .712 $\pm$ .00 & .713 & 4,090 $\pm$ 338 & 4,329 & 89.5 $\pm$ 18.7 & 106.1 \\
\adaevolve{} & \textbf{\underline{.952}} $\pm$ .00 & \textbf{\underline{.952}} & \textbf{662.3} $\pm$ 0.1 & \textbf{640.5} & \textbf{\underline{.134}} $\pm$ .01 & \textbf{\underline{.1453}} & \textbf{\underline{26.30}} $\pm$ .07 & \textbf{\underline{26.37}} & \textbf{\underline{.746}} $\pm$ .03 & \textbf{\underline{.775}} & \textbf{\underline{4,317}} $\pm$ 29 & \textbf{\underline{4,348}} & \textbf{\underline{125.2}} $\pm$ 6.1 & \textbf{\underline{131.8}} \\
\midrule
\multicolumn{15}{l}{\textit{Backbone: Gemini-3-Pro}} \\
OE & \textbf{\underline{.954}} $\pm$ .01 & \textbf{\underline{.960}} & 707.8 $\pm$ 40 & 667.1 & .127 $\pm$ .00 & .1272 & 26.24 $\pm$ .01 & 26.24 & .729 $\pm$ .01 & .736 & 4,109 $\pm$ 254 & 4,274 & 115.2 $\pm$ 13.2 & 125.6 \\
GEPA & .850 $\pm$ .00 & .855 & 720.4 $\pm$ 46 & 667.1 & .127 $\pm$ .00 & .1272 & 26.16 $\pm$ .03 & 26.19 & .713 $\pm$ .00 & .713 & 3,616 $\pm$ 481 & 4,167 & 74.5 $\pm$ 9.5 & 104.0 \\
Shinka & .918 $\pm$ .03 & .933 & 949.8 $\pm$ 73 & 892.3 & .120 $\pm$ .01 & .1272 & 26.25 $\pm$ .01 & 26.26 & .721 $\pm$ .00 & .721 & 3,932 $\pm$ 343 & 4,255 & 84.7 $\pm$ 7.7 & 92.2 \\
\adaevolve{} & \underline{.953} $\pm$ .01 & \textbf{\underline{.960}} & \textbf{642.1} $\pm$ 5.9 & \textbf{637.1} & \textbf{\underline{.145}} $\pm$ .00 & \textbf{\underline{.1453}} & \textbf{\underline{26.26}} $\pm$ .00 & \textbf{\underline{26.26}} & \textbf{\underline{.743}} $\pm$ .01 & \textbf{\underline{.752}} & \textbf{\underline{4,221}} $\pm$ 89 & \textbf{\underline{4,310}} & \textbf{\underline{126.0}} $\pm$ 5.1 & \textbf{\underline{131.8}} \\
\bottomrule
\end{tabular}
}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
\centering
% \tiny is too small. We use \scriptsize with tight columns.
\scriptsize 
\setlength{\tabcolsep}{2.5pt} % Tight spacing
\renewcommand{\arraystretch}{1.1} % Breathable rows
\caption{Mathematical optimization benchmarks. We report \textbf{Mean $\pm$ Std} and \textbf{Best} (Max) objective values. Higher is better for all metrics. \textbf{Bold} denotes the best performing method per backbone. Underline denotes results surpassing \textbf{Human SOTA}. ($N$ values: Square=26, Rect=21, Tri=11, Convex=13, Max=3). The detailed explanations are given in \cref{tab:adaevolve_problem_defs}. For circle packing (rect) problem with Gemini, \adaevolve{} gets 2.36583237, beating the AlphaEvolve reference of 2.36583213. For circle packing (square) problem with Gemini, \adaevolve{} gets 2.63598308, beating the AlphaEvolve reference of 2.63586276.}
\label{tab:math-opt-final}

\makebox[\textwidth][c]{\begin{tabular}{l cc cc cc cc cc cc}
\toprule
& \multicolumn{2}{c}{\textbf{Circle Packing (Square)}} 
& \multicolumn{2}{c}{\textbf{Circle Packing (Rect)}} 
& \multicolumn{2}{c}{\textbf{Heilbronn (Triangles)}} 
& \multicolumn{2}{c}{\textbf{Heilbronn (Convex)}} 
& \multicolumn{2}{c}{\textbf{MinMax Distance}} 
& \multicolumn{2}{c}{\textbf{Signal Processing}} \\
\cmidrule(lr){2-3}
\cmidrule(lr){4-5}
\cmidrule(lr){6-7}
\cmidrule(lr){8-9}
\cmidrule(lr){10-11}
\cmidrule(lr){12-13}

\textbf{Strategy} 
& Avg & Best 
& Avg & Best 
& Avg & Best 
& Avg & Best 
& Avg & Best 
& Avg & Best \\
\midrule
\textbf{Human} & -- & 2.634 & -- & 2.364 & -- & 0.0360 & -- & 0.0306 & -- & 0.2399 & -- & --  \\
\textbf{AlphaEvolve} & -- & 2.635 & -- & 2.3658 & -- & 0.0365 & -- & 0.0309 & -- & 0.2398 & -- & --  \\
\midrule
\multicolumn{13}{l}{\textit{Backbone: GPT-5}} \\
OpenEvolve & 2.531 $\pm$ .018 & 2.541 & 2.267 $\pm$ .014 & 2.276 & 0.028 $\pm$ .006 & 0.028 & 0.025 $\pm$ .005 & 0.027 & 0.226 $\pm$ .003 & 0.2243 & 0.569 $\pm$ .047 & 0.622 \\
GEPA & 2.613 $\pm$ .022 & 2.628 & 2.326 $\pm$ .023 & 2.354 & 0.031 $\pm$ .002 & 0.032 & 0.025 $\pm$ .002 & 0.027 & 0.232 $\pm$ .120 & 0.2392 & 0.689 $\pm$ .014 & 0.705 \\
ShinkaEvolve & 2.464 $\pm$ .083 & 2.541 & 2.335 $\pm$ .026 & 2.358 & 0.032 $\pm$ .012 & {0.034} & 0.023 $\pm$ .005 & 0.026 & 0.239 $\pm$ .001 & \textbf{0.2398} & 0.485 $\pm$ .044 & 0.533 \\
\adaevolve{} & \textbf{2.629} $\pm  $ .001 & \textbf{\underline{2.636}} & \textbf{2.349} $\pm$ .010 & \textbf{2.361} & \textbf{0.033} $\pm$ .001 & \textbf{0.036} & \textbf{0.027} $\pm$ .001 & \textbf{0.029} & \textbf{0.239} $\pm$ .009 & \textbf{0.2404} & \textbf{0.698} $\pm$ .017 & \textbf{0.718} \\
\midrule
\multicolumn{13}{l}{\textit{Backbone: Gemini-3-Pro}} \\
OpenEvolve & 2.541 $\pm$ .000 & 2.541 & 2.365 $\pm$ .001 & 2.366 & 0.033 $\pm$ .000 & 0.035 & 0.028 $\pm$ .009 & 0.028 & 0.240 $\pm$ .000 & 0.2398 & 0.553 $\pm$ .015 & 0.565 \\
GEPA & 2.620 $\pm$ .002 & 2.621 & 2.216 $\pm$ .046 & 2.232 & 0.031 $\pm$ .002 & 0.033 & 0.023 $\pm$ .001 & 0.027 & 0.213 $\pm$ .008 & 0.2178 & \textbf{0.617} $\pm$ .075 & \textbf{0.680} \\
ShinkaEvolve & 2.622 $\pm$ .012 & 2.636 & 2.366 $\pm$ .000 & 2.366 & 0.035 $\pm$ .001 & 0.036 & 0.028 $\pm$ .001 & \textbf{0.029} & \textbf{0.240} $\pm$ .000 & {0.2398} & 0.480 $\pm$ .039 & 0.505 \\
\adaevolve{} & \textbf{\underline{2.632}} $\pm$ .003 & \textbf{\underline{2.636}} & \textbf{{2.366}} $\pm$ .000 & \textbf{\underline{2.366}} & \textbf{0.036} $\pm$ .001 & \textbf{0.036} & \textbf{0.029} $\pm$ .000 & \textbf{0.029} & \textbf{0.240} $\pm$ .000 & \textbf{\underline{0.2404}} & 0.593 $\pm$ .009 & 0.603 \\
\bottomrule
\end{tabular}
}
\label{tab:math-opt}
\end{table*}
```

## Table 3
```latex
\begin{table}[h]
\centering
\small
\setlength{\tabcolsep}{4.5pt}
\renewcommand{\arraystretch}{1.12}

\caption{\textbf{Example tactics  produced by the tactic generator across domains.}
Each tactic pairs a high-level solution strategy with a representative computational approach.}
\label{tab:paradigm-examples}

\begin{tabular}{p{3.5cm} p{5.4cm} p{3.1cm}}
\toprule
\textbf{Use case} & \textbf{Meta-Guidance Solution Tactics} & \textbf{Approach type} \\
\midrule

\multirow{5}{*}{\textit{Math / equation systems}}
& Solve nonlinear systems using a trust-region root finder & \texttt{scipy.optimize.root} \\
& Exploit structure by directly solving linear systems & \texttt{scipy.linalg.solve} \\
& Isolate scalar roots with bracketed search & \texttt{scipy.optimize.brentq} \\
& Iterate toward equilibrium with damped fixed-point updates & Fixed-point iteration \\
& Generate symbolic expressions before numerical evaluation & \texttt{sympy.lambdify} + solver \\

\midrule

\multirow{5}{*}{\textit{Continuous optimization}}
& Perform constrained minimization under geometric constraints & \texttt{scipy.optimize.minimize} (SLSQP) \\
& Escape poor basins via multi-start global search & Multi-start + local refine \\
& Initialize layouts using Voronoi structure, then refine locally & Voronoi + optimizer \\
& Enforce feasibility through convex-hull constraints & \texttt{scipy.spatial.ConvexHull} \\
& Optimize box-constrained parameters with quasi-Newton updates & L-BFGS-B \\

\midrule

\multirow{5}{*}{\textit{Combinatorial / assignment}}
& Construct solutions greedily using score-ordered candidates & Greedy heuristic \\
& Compute minimum-cost matchings exactly & Linear sum assignment \\
& Improve configurations through swap-based neighborhoods & Local search \\
& Relax discrete constraints into a linear program & \texttt{scipy.optimize.linprog} \\
& Prioritize decisions with a score-driven heap & Priority-queue greedy \\

\midrule

\multirow{5}{*}{\textit{Signal / filtering}}
& Suppress impulsive noise with median filtering & \texttt{scipy.signal.medfilt} \\
& Preserve trends via polynomial smoothing & Savitzky--Golay filter \\
& Balance noise and fidelity with adaptive Wiener filtering & Wiener filter \\
& Aggregate robust statistics over sliding windows & Percentile filter \\
& Apply learned structure through custom convolution kernels & \texttt{scipy.ndimage.convolve} \\

\bottomrule
\end{tabular}
\label{tab:param}
\end{table}
```

## Table 4
```latex
\begin{table}[h!]
\centering
\small
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.25}
\caption{\textbf{ADRS systems benchmarks.}
Each task specifies a concrete systems optimization objective.}
\label{tab:adrs_systems}
\makebox[\textwidth][c]{
\begin{tabular}{p{3.6cm} p{4.8cm} p{5.8cm}}
\toprule
\textbf{Task} & \textbf{Objective} & \textbf{Problem description} \\
\midrule

\textbf{Telemetry Repair}
& Repair buggy network telemetry pipelines
& Automatically fix data processing logic to improve correctness and confidence calibration. \\

\textbf{Cloudcast}
& Optimize multi-cloud data transfer cost
& Select routing and placement strategies to minimize monetary transfer cost across providers. \\

\textbf{Expert Parallelism Load Balancer (EPLB)}
& Balance expert-parallel load across GPUs
& Reduce stragglers by redistributing expert assignments while preserving throughput. \\

\textbf{Model Placement (Prism)}
& Optimize model-to-GPU placement cost
& Assign model components to GPUs to minimize global execution cost under capacity constraints. \\

\textbf{LLM-SQL}
& Reorder tabular data for prefix efficiency
& Improve prefix-cache hit rates by reordering rows or columns without altering semantics. \\

\textbf{Transaction Scheduling (TXN)}
& Minimize makespan in transaction execution
& Schedule dependent transactions to reduce overall completion time. \\

\textbf{Datacenter TCP Congestion Control (NS3)}
& Maximize throughput and minimize queue latency
& Tune congestion control behavior under realistic network simulation workloads. \\

\bottomrule
\end{tabular}
}
\end{table}
```

## Table 5
```latex
\begin{table}[h!]
\centering
\small
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.25}
\caption{\textbf{Mathematical optimization benchmarks used in AdaEvolve.}
Each task is defined exactly as in Appendix~B of the AlphaEvolve paper.}
\label{tab:adaevolve_problem_defs}

\begin{tabular}{p{5.2cm} p{8.6cm}}
\toprule
\textbf{Problem} & \textbf{Objective (exact task definition)} \\
\midrule

\textbf{Circle Packing (Square)} \newline $N{=}26$
&
Pack $N$ disjoint circles inside a \emph{unit square} so as to
\textbf{maximize the sum of their radii}. \\

\addlinespace[0.3em]

\textbf{Circle Packing (Rectangle)} \newline $N{=}21$
&
Pack $N$ disjoint circles inside a \emph{rectangle of perimeter $4$} so as to
\textbf{maximize the sum of their radii}. \\

\addlinespace[0.3em]

\textbf{Heilbronn Problem (Triangle)} \newline $N{=}11$
&
Place $N$ points on or inside a \emph{triangle of unit area} so that
the \textbf{minimum area of any triangle formed by the points is maximized}. \\

\addlinespace[0.3em]

\textbf{Heilbronn Problem (Convex Region)} \newline $N{=}13$
&
Place $N$ points on or inside a \emph{convex region of unit area} so that
the \textbf{minimum area of any triangle formed by the points is maximized}. \\

\addlinespace[0.3em]

\textbf{MinMax Distance}  \newline $N{=}3$
&
For given $N$ and dimension $d$, find $N$ points in $\mathbb{R}^d$ that
\textbf{maximize the ratio between the minimum and maximum pairwise distances}. \\

\addlinespace[0.3em]

\textbf{Signal Processing}
&
Optimize a continuous signal processing objective under noisy evaluation,
where candidate programs transform an input signal and are scored by an
external evaluator. \\

\bottomrule
\end{tabular}
\end{table}
```

## Table 6
```latex
\begin{table*}[h]
\centering
\small
\caption{AdaEvolve performance on ARC-AGI-2 benchmarks. Values denote final accuracy under a matched inference budget.}
\label{tab:ada-additional-results}

\begin{tabular}{l cccc}
\toprule
Backbone & OpenEvolve & AdaEvolve \\
\midrule
GPT-5 & 42\% & 49\% \\
Gemini-3-Pro & 44\% & 50\% \\
\bottomrule
\end{tabular}
\end{table*}
```

