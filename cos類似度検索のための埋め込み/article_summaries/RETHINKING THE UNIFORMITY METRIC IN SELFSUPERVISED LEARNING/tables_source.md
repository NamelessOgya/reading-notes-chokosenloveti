# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table*}[h]
\vspace{-2pt}
\centering
\caption{Main results on CIFAR-10 and CIFAR-100. Proj. and Pred. are the hidden dimensions in  projector and predictor. {\color{red} $\uparrow$} and {\color{blue} $\downarrow$} indicates  gains and losses, respectively.}
\vspace{6pt}
\resizebox{0.98\textwidth}{!}{
\begin{tabular}{lcccccccccccc}\hline
\multirow{2}{*}{Methods} & \multirow{2}{*}{Proj.} & \multirow{2}{*}{Pred.} &\multicolumn{5}{|c}{CIFAR-10} & \multicolumn{5}{|c}{CIFAR-100} \\\cline{4-13}
& & & \multicolumn{1}{|c}{Acc@1$\uparrow$} & Acc@5$\uparrow$ & $\mathcal{W}_{2}\downarrow$ & $\mathcal{L_U}\downarrow$ & $\mathcal{L_A}\downarrow$ & \multicolumn{1}{|c}{Acc@1$\uparrow$} & Acc@5$\uparrow$ & $\mathcal{W}_{2}\downarrow$ & $\mathcal{L_U}\downarrow$ & $\mathcal{L_A}\downarrow$ \\\hline
%\multicolumn{13}{c}{\textit{w/o Wasserstein Distance}} \\
SimCLR & 256 & \XSolidBrush  & 89.85\quad\quad\enspace & 99.78 & 1.04\quad\quad\enspace & -3.75 & 0.47\quad\quad\enspace & 63.43\quad\quad\enspace & 88.97 & 1.05\quad\quad\enspace & -3.75 &  0.50\quad\quad\enspace\\
NNCLR & 256 & 256  & 87.46\quad\quad\enspace & 99.63 & 1.23\quad\quad\enspace & -3.12 & 0.38\quad\quad\enspace  & 54.90\quad\quad\enspace & 83.81 & 1.23\quad\quad\enspace & -3.18 & 0.43\quad\quad\enspace\\
%MoCo V2 & 256 & \XSolidBrush & 90.65 & \textbf{99.81} & 1.06 & -3.75  & 0.51 & 66.12 & 90.11 & 1.06 & -3.75 & 0.50\\
SimSiam & 256 & 256  & 86.71\quad\quad\enspace & 99.67 & 1.19\quad\quad\enspace & -3.33 & 0.39\quad\quad\enspace & 56.10\quad\quad\enspace & 84.34 & 1.21\quad\quad\enspace & -3.29 & 0.42\quad\quad\enspace\\
AlignUniform & 256 &\XSolidBrush & 90.37\quad\quad\enspace & 99.76 & 0.94\quad\quad\enspace & -3.82 & 0.51\quad\quad\enspace & 65.08\quad\quad\enspace  & 90.15 & 0.95\quad\quad\enspace & -3.82 & 0.53\quad\quad\enspace\\\hline
MoCo v2 & 256 & \XSolidBrush & 90.65\quad\quad\enspace & 99.81 & 1.06\quad\quad\enspace & -3.75  & 0.51\quad\quad\enspace & 60.27\quad\quad\enspace & 86.29 & 1.07\quad\quad\enspace & -3.60 & 0.46\quad\quad\enspace \\
MoCo v2 + $\mathcal{L_U}$ & 256 & \XSolidBrush & 90.98 { \color{red} $\uparrow _{0.33}$} & 99.67 & 0.98 { \color{red} $\uparrow _{0.08}$} & -3.82 & 0.53 { \color{blue} $\downarrow _{0.02}$} & 61.21 { \color{red} $\uparrow _{0.94}$} & 87.32 & 0.98 { \color{red} $\uparrow _{0.09}$} & -3.81 & 0.52 { \color{blue} $\downarrow _{0.06}$}\\
MoCo v2 + $\mathcal{W}_{2}$ & 256 & \XSolidBrush  &  91.41 { \color{red} $\uparrow _{0.76}$} & 99.68 & 0.33 { \color{red} $\uparrow _{0.73}$} & -3.84 & 0.63 { \color{blue} $\downarrow _{0.12}$} & 63.68 { \color{red} $\uparrow _{3.41}$} & 88.48 & 0.28 { \color{red} $\uparrow _{0.79}$} & -3.86 & 0.66 { \color{blue} $\downarrow _{0.20}$}\\\hline
BYOL & 256 & 256 & 89.53\quad\quad\enspace & 99.71 & 1.21\quad\quad\enspace& -2.99 & \textbf{0.31}\quad\quad\enspace& 63.66\quad\quad\enspace & 88.81 & 1.20\quad\quad\enspace & -2.87 & \textbf{0.33}\quad\quad\enspace\\
BYOL + $\mathcal{L_U}$ & 256 & \XSolidBrush & 90.09 { \color{red} $\uparrow _{0.56}$} & 99.75 & 1.09 { \color{red} $\uparrow _{0.12}$} & -3.66 & 0.40 { \color{blue} $\downarrow _{0.09}$} & 62.68 { \color{blue} $\downarrow _{0.98}$} & 88.44 & 1.08 { \color{red} $\uparrow _{0.12}$} & -3.70 & 0.51 { \color{blue} $\downarrow _{0.18}$}\\
BYOL + $\mathcal{W}_{2}$ & 256 & 256 & 90.31 { \color{red} $\uparrow _{0.78}$} & 99.77 & 0.38 { \color{red} $\uparrow _{0.83}$} & -3.90 & 0.65 { \color{blue} $\downarrow _{0.34}$} & 65.16 { \color{red} $\uparrow _{1.50}$} & 89.25 & 0.36 { \color{red} $\uparrow _{0.84}$} & -3.91 & 0.69 { \color{blue} $\downarrow _{0.36}$}\\\hline
BarlowTwins & 256 & \XSolidBrush & 91.16\quad\quad\enspace & 99.80 & 0.22\quad\quad\enspace & -3.91  & 0.75\quad\quad\enspace & 68.19\quad\quad\enspace & 90.64 & 0.23\quad\quad\enspace & -3.91 & 0.75\quad\quad\enspace\\
BarlowTwins + $\mathcal{L_U}$ & 256 & \XSolidBrush & 91.38 { \color{red} $\uparrow _{0.22}$} & 99.77 & 0.21 { \color{red} $\uparrow _{0.01}$} & -3.92 & 0.76 { \color{blue} $\downarrow _{0.01}$} & 68.41 { \color{red} $\uparrow _{0.22}$} & 90.99 & 0.22 { \color{red} $\uparrow _{0.01}$} & -3.91 & 0.76 { \color{blue} $\downarrow _{0.01}$}\\
BarlowTwins + $\mathcal{W}_{2}$ & 256 & \XSolidBrush & \textbf{91.43} { \color{red} $\uparrow _{0.27}$} & 99.78 & 0.19 { \color{red} $\uparrow _{0.03}$} & -3.92 & 0.76 { \color{blue} $\downarrow _{0.01}$} & 68.47 { \color{red} $\uparrow _{0.28}$} & 90.64 & 0.19 { \color{red} $\uparrow _{0.04}$} & -3.91 &  0.79 { \color{blue} $\downarrow _{0.04}$} \\\hline
Zero-CL & 256 & \XSolidBrush & 91.35\quad\quad\enspace & 99.74 & 0.15\quad\quad\enspace & \textbf{-3.94} & 0.70\quad\quad\enspace & 68.50\quad\quad\enspace & 90.97 & 0.15\quad\quad\enspace & -3.93 & 0.75\quad\quad\enspace\\
Zero-CL + $\mathcal{L_U}$ & 256 & \XSolidBrush & 91.28 { \color{blue} $\downarrow _{0.07}$} & 99.74 & 0.15\quad\quad\enspace & \textbf{-3.94} & 0.72 { \color{blue} $\downarrow _{0.02}$} & 68.44 { \color{blue} $\downarrow _{0.06}$} & 90.91 & 0.15\quad\quad\enspace & -3.93 & 0.74 { \color{red} $\uparrow _{0.01}$}\\
Zero-CL + $\mathcal{W}_{2}$  & 256 & \XSolidBrush & 91.42 { \color{red} $\uparrow _{0.07}$} & \textbf{99.82} & \textbf{0.14} { \color{red} $\uparrow _{0.01}$} & \textbf{-3.94} & 0.71 { \color{blue} $\downarrow _{0.01}$} & \textbf{68.55} { \color{red} $\uparrow _{0.05}$} &  \textbf{91.02} & \textbf{0.14} { \color{red} $\uparrow _{0.01}$} & \textbf{-3.94} & 0.76 { \color{blue} $\downarrow _{0.01}$}\\\hline
\end{tabular}}
\label{table:main results table}
\end{table*}
```

## Table 2
```latex
\begin{table*}[t]
\centering
\caption{Parameter settings for various models in the experiments.}
\label{table:parameter setting}
\resizebox{0.60\textwidth}{!}{
\begin{tabular}{l c c c c} \hline
Models & MoCo v2 & BYOL & BarlowTwins & Zero-CL \\\hline
$\alpha_{\max}$ & 1.0 & 0.2 & 30.0 & 30.0 \\
$\alpha_{\min}$ & 1.0 & 0.2 & 0 & 30.0 \\\hline
\end{tabular}}
\end{table*}
```

## Table 3
```latex
\begin{table*}[h]
\centering
\caption{Parameter setting for various models in experiments.}
\label{table:parameter setting}
\resizebox{0.60\textwidth}{!}{
\begin{tabular}{l c c c c} \hline
Models & MoCo v2 & BYOL & BarlowTwins & Zero-CL \\\hline
$\alpha_{max}$ & 1.0 & 0.2 & 30.0 & 30.0 \\
$\alpha_{min}$ & 1.0 & 0.2 & 0 & 30.0 \\\hline
\end{tabular}}
\end{table*}
```

