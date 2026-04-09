# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[H]
\centering
\footnotesize
\setlength{\tabcolsep}{2pt}
% \renewcommand{\arraystretch}{1.15}

\caption{\textbf{\sys across optimization tasks.}
We compare \sys against strong human-designed methods and prior AI discovery systems, including AlphaEvolve, GEPA, ShinkaEvolve, and OpenEvolve, across mathematical optimization, systems performance optimization (e.g., GPU-to-model placement), and algorithm engineering tasks (e.g., Frontier-CS). For Frontier-CS, we report median scores over 172 competitive programming problems.
Arrows indicate whether higher ($\uparrow$) or lower ($\downarrow$) scores are better.
All \emph{open} AI frameworks are evaluated under a fixed budget of 100 iterations, and the best result among them is reported as “AI Best.”
AlphaEvolve results are taken directly from its original publication.}
\label{tab:first-table}
\vspace{-0.2em}

% \shu{might want to update this table, what should we do for this one}
\begin{tabular}{p{3cm}ccc}
\toprule
\textbf{Task} 
& \textbf{Human Best} 
& \textbf{AlphaEvolve} 
& \textbf{\sys} \\
\midrule

\multicolumn{4}{l}{\textsc{\textbf{Mathematics}}} \\

Circle-Packing ($\uparrow$)
& 2.634
& 2.635
& \textbf{2.636} \\


MinMaxMinDist ($\downarrow$)
& 4.16584
& 4.16579
& \textbf{4.16578} \\

% Third-Autocorr ($\downarrow$)
% & 1.4600
% & 1.4556
% & 1.4558 \\

\addlinespace[0.2em]
\midrule
\textbf{Task}
& \textbf{Human Best}
& \textbf{AI Best}
& \textbf{EvoX} \\
\midrule

\multicolumn{4}{l}{\textsc{\textbf{Systems Optimization}}} \\

Cloud Transfer ($\downarrow$)
& 626.24
& 645.72
& \textbf{623.69} \\

GPU Placement ($\uparrow$)
& 21.89
& 26.26
& \textbf{30.52} \\

Txn Scheduling ($\uparrow$)
& 2724.8
& 4329
& \textbf{4347.8} \\

\addlinespace[0.4em]
\multicolumn{4}{l}{\textsc{\textbf{Algorithms}}} \\



% ALE-Bench-Lite ($\uparrow$)
% & --
% & 1914.6
% & \textbf{1958.2} \\

Frontier-CS ($\uparrow$)
& --
& 56.2
& \textbf{75.5} \\

% \addlinespace[0.4em]
% \multicolumn{4}{l}{\textsc{\textbf{Kernels}}} \\

% Matmul ($\downarrow$)
% & --
% & --
% & \textbf{--} \\
\bottomrule
\end{tabular}
\end{table}
```

## Table 2
```latex
\begin{table*}[t]
% \centering
% \footnotesize
% \setlength{\tabcolsep}{5pt}
% \renewcommand{\arraystretch}{1.15}

% \caption{\textbf{\sys across optimization tasks (horizontal layout).}
% Columns correspond to tasks and subtasks; rows correspond to baselines.
% Arrows indicate whether higher ($\uparrow$) or lower ($\downarrow$) values are better.
% All open AI methods are evaluated under a fixed budget of 100 iterations.
% }
% \label{tab:first-table-horizontal}
% \vspace{0.4em}

% \begin{tabular}{lcccccccc}
% \toprule
% \textbf{Method}
% & \multicolumn{2}{c}{\textbf{Mathematics}}
% & \multicolumn{3}{c}{\textbf{Systems Optimization}}
% & \multicolumn{2}{c}{\textbf{Algorithms}} \\
% \cmidrule(lr){2-3}
% \cmidrule(lr){4-6}
% \cmidrule(lr){7-8}

% & Circle Pack $\uparrow$
% & MinMaxMinDist $\downarrow$
% & Cloud Transfer $\downarrow$
% & GPU Placement $\uparrow$
% & Txn Sched. $\uparrow$
% & ALE-Bench $\uparrow$
% & Signal Proc. $\uparrow$ \\
% \midrule

% \textbf{Human Best}
% & 2.634
% & 4.16584
% & 626.24
% & 21.89
% & 2724.8
% & --
% & -- \\

% \textbf{AI Best}
% & 2.635
% & 4.16579
% & 645.72
% & 26.26
% & 4329
% & 1932.1
% & 0.6866 \\

% \textbf{\sys}
% & \textbf{2.636}
% & \textbf{4.16578}
% & \textbf{623.69}
% & \textbf{30.52}
% & \textbf{4347.8}
% & \textbf{1958.0}
% & \textbf{0.7429} \\

% \bottomrule
% \end{tabular}
% \end{table*}
```

## Table 3
```latex
\begin{table}[t]
% \centering
% \footnotesize
% \setlength{\tabcolsep}{4pt}
% \renewcommand{\arraystretch}{1.2}
% \caption{
% \textbf{Search strategy evolution (summary).}
% EvoX adapts search behavior over time by modifying parent/context selection
% and operator bias in response to stagnation. These stage-level regimes
% are used consistently throughout the appendix.
% }
% \label{tab:search-evolution-summary}
% \begin{tabular}{l p{3.4cm} p{3.4cm}}
% \toprule
% \textbf{Stage} &
% \textbf{Signal Processing} &
% \textbf{Circle Packing} \\
% \midrule
% Early &
% Greedy parent/context selection &
% Uniform parent/context selection \\

% Mid &
% Stratified, multi-objective context &
% Exploration with structural modification \\

% Late &
% UCB-guided structural refinement &
% Top-tier parent selection with refinement \\
% \bottomrule
% \end{tabular}
% \end{table}
```

## Table 4
```latex
\begin{table}[H]
\centering
\small
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.25}
\caption{\textbf{Mathematical optimization benchmarks.}
Summary of optimization tasks used to evaluate \sys, including geometric, combinatorial, and signal processing problems.}
\vspace{0.5em}
\label{tab:benchmark_math}

\begin{tabularx}{\linewidth}{p{4.8cm} p{3.0cm} X}
\toprule
\textbf{Problem} & \textbf{Objective} & \textbf{Description} \\
\midrule

Circle Packing (Square)
& $\max\, r$
& Place $n$ equal-radius circles inside the unit square without overlap; maximize the common radius subject to non-overlap and boundary constraints. \\

Circle Packing (Rectangle)
& $\max\, r$
& Pack $n$ equal-radius circles into a rectangle with fixed aspect ratio, maximizing the radius under geometric constraints. \\

Heilbronn Triangle
& $\max\, \min$ area
& Place $n$ points in $[0,1]^2$ to maximize the area of the smallest triangle formed by any three points. \\

Heilbronn Convex
& $\max\, \min$ area
& Generalization of the Heilbronn triangle problem: maximize the minimum area of convex hulls formed by any subset of $k>3$ points. \\

Min--Max--Min Distance (2 variants)
& $\max\, \frac{d_{\min}}{d_{\max}}$
& Place points to maximize uniformity, measured by the ratio between minimum and maximum pairwise distances. \\

Third Autocorrelation Inequality
& $\min\, C_3$
& Construct witness functions that minimize the third autocorrelation constant in additive combinatorics. \\

Signal Processing
& multi-objective
& Design a causal, online filtering program for noisy time series, balancing fidelity, smoothness, lag, and false trend detection. \\

\bottomrule
\end{tabularx}
\end{table}
```

## Table 5
```latex
\begin{table}[H]
\centering
\small
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.25}
\caption{\textbf{System performance optimization benchmarks.}
Benchmarks drawn from ADRS-Bench~\cite{cheng2025barbarians}, capturing realistic optimization problems from production systems.}
\vspace{0.5em}
\label{tab:benchmark_system}

\begin{tabularx}{\linewidth}{p{4.8cm} p{3.0cm} X}
\toprule
\textbf{Problem} & \textbf{Objective} & \textbf{Description} \\
\midrule

EPLB (Expert Placement Load Balancing)
& $\max$ throughput ratio
& Place and replicate experts in MoE models across GPUs based on activation frequency, minimizing load imbalance and computational skew. \\

PRISM (Global Model Scheduling)
& $\max$ throughput
& Schedule multiple deep learning models across distributed GPUs under memory, compute, and latency SLO constraints in a multi-tenant setting. \\

LLM--SQL
& $\max$ accuracy
& Optimize LLM-driven SQL generation via prompting or post-processing; a query is correct only if it exactly matches ground-truth execution results. \\

Cloudcast (Multi-Region Data Transfer)
& $\min$ cost
& Design cost-efficient data transfer strategies across cloud regions with heterogeneous bandwidths, latencies, and egress pricing under deadline constraints. \\

Transaction Scheduling
& $\max$ commits/sec
& Schedule database transactions under contention to maximize throughput while minimizing aborts from conflicts, deadlocks, or timeouts. \\

Telemetry Repair
& $\max$ reconstruction accuracy
& Reconstruct missing or corrupted telemetry signals using partial observations, exploiting temporal and spatial correlations. \\

\bottomrule
\end{tabularx}
\end{table}
```

## Table 6
```latex
\begin{table}[H]
\centering
\small
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.25}
\caption{\textbf{Algorithmic and research problem benchmarks.}
We evaluate on 182 open-ended problems: 10 NP-hard optimization problems from ALE-Bench-Lite~\cite{imajuku2025ale} and 172 problems from FrontierCS~\cite{mang2025frontiercs}.}
\vspace{0.5em}
\label{tab:benchmark_algorithmic_research}

\begin{tabularx}{\linewidth}{p{4.2cm} p{1.0cm} X}
\toprule
\textbf{Problem / Category} & \textbf{Count} & \textbf{Description} \\
\midrule

\multicolumn{3}{l}{\textit{ALE-Bench-Lite: NP-hard optimization from AtCoder Heuristic Contests}} \\
\addlinespace[2pt]

\texttt{ahc008} (Territory)
& 1
& Control agents on a grid to place fences isolating pets; $\max$ satisfaction. \\

\texttt{ahc011} (Sliding Puzzle)
& 1
& Rearrange tiles so line patterns form a large connected tree; $\max$ connectivity. \\

\texttt{ahc015} (Candy Clustering)
& 1
& Cluster candies of the same flavor using global tilt operations; $\max$ clustering score. \\

\texttt{ahc016} (Graph Classification)
& 1
& Design reference graphs and classify noisy, permuted query graphs; $\min$ classification error. \\

\texttt{ahc024} (Map Compression)
& 1
& Compress a grid map preserving district adjacency; $\min$ map size. \\

\texttt{ahc025} (Weight Balancing)
& 1
& Partition items with unknown weights into balanced groups; $\min$ imbalance. \\

\texttt{ahc026} (Box Stacking)
& 1
& Rearrange numbered boxes across stacks to a target configuration; $\min$ moves. \\

\texttt{ahc027} (Cleaning Route)
& 1
& Design a cyclic robot route to minimize steady-state dirt; $\min$ average dirtiness. \\

\texttt{ahc039} (Fishing Net)
& 1
& Construct a rectilinear polygon enclosing targets under a perimeter budget; $\max$ net score. \\

\texttt{ahc046} (Skating with Blocks)
& 1
& Visit target squares in order using moves, slides, and blocks; $\min$ actions. \\

\midrule

\multicolumn{3}{l}{\textit{FrontierCS: open-ended CS problems}} \\
\addlinespace[2pt]

\texttt{Optimization}
& 38
& Maximize or minimize a quantitative objective over a parameterized search space under resource constraints. IDs: 1, 2, 15, 16, 22, 25, 26, 27, 28, 30, 33, 35, 36, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 52, 53, 54, 57, 58, 59, 61, 64, 68, 69, 79, 81, 86, 93, 229. \\

\texttt{Constructive}
& 62
& Synthesize a valid structured object (e.g., packing, graph, expression) under global constraints. IDs: 0, 3, 4, 5, 6, 7, 8, 9, 13, 17, 23, 24, 60, 62, 63, 70, 72, 73, 75, 77, 80, 82, 83, 85, 87, 89, 142, 174--193, 192, 193, 203, 205, 207, 209--214, 217, 220, 222, 225, 227, 228, 239, 241. \\

\texttt{Interactive}
& 72
& Solve a hidden-instance task via an adaptive query-response protocol, minimizing queries or interaction steps. IDs: 10, 11, 14, 101, 104, 106--113, 117, 119--125, 127, 132--135, 137, 138, 140, 141, 143--145, 147--171, 226, 231, 233, 243, 245, 247--249, 252--258. \\

\bottomrule
\end{tabularx}
\end{table}
```

## Table 7
```latex
\begin{table*}[h]
% \small
% \centering
% \caption{EvoX performance across additional benchmark families. Score = final achieved objective value under a fixed evaluation budget.}

% \begin{tabular}{llcccc}
% \toprule
% Benchmark & Generator Model & OpenEvolve & GEPA & ShinkaEvolve & EvoX \\
% \midrule

% Frontier-CS~\cite{mang2025frontiercs} & GPT-5 & -- & -- & -- & -- \\

% GPU-Mode Kernels~\cite{gpumode_reference_kernels} & Gemini-3.0 & -- & -- & -- & -- \\

% ARC-AGI~\cite{chollet2025arc} & GPT-5 & 41\% & -- & -- & 48\% \\
% ARC-AGI~\cite{chollet2025arc} & Gemini-3-Pro & 45\% & -- & -- & 51\% \\

% Prompt Optimization~\cite{khattab2023dspy} & GPT-4.1-mini & -- & -- & -- & -- \\

% \bottomrule
% \end{tabular}
% \label{tab:additional-benchmarks}
% \end{table*}
```

## Table 8
```latex
\begin{table*}[h]
\small
\centering
\caption{EvoX performance on ARC-AGI benchmarks. Values denote final accuracy.}
\label{tab:additional-benchmarks}

\begin{tabular}{l cc}
\toprule
Backbone & OpenEvolve & EvoX \\
\midrule
GPT-5 & 41\% & 48\% \\
Gemini-3-Pro & 45\% & 51\% \\
\bottomrule
\end{tabular}
\end{table*}
```

