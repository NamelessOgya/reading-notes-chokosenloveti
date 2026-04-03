# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
    \centering
    % \resizebox{\columnwidth}{!}{%

    \small
    % \begin{tabularx}{\textwidth}{llXXll}
    \begin{tabular}{lccccc}
        \toprule
        \multicolumn{6}{c}{Related work on reasoning and decision-making} \\
        \toprule
        \textbf{ Approach} &
        \textbf{Self} &
        \textbf{ Hidden } &
        \textbf{Decision } &
        \textbf{Binary } & 
        \textbf{Memory} \\
        & \textbf{refine} & \textbf{constraints} & \textbf{making} & \textbf{reward} & \\
        \midrule
         Self-refine \citep{madaan2023self} & \greencheck & \redcross & \redcross & \redcross & \redcross \\
         Beam search \citep{xie2023decomposition} & \greencheck & \greencheck & \greencheck & \greencheck & \redcross \\
         \textbf{Reflexion (ours)} & \greencheck & \greencheck & \greencheck & \greencheck & \greencheck \\
    % \end{tabularx}
    \end{tabular}
    % }
    \centering
    \small
    \begin{tabular}{lccccc}
        \toprule
        \multicolumn{6}{c}{Related work on programming} \\
        \midrule
        \textbf{Approach} &
        \textbf{Test} &
        \textbf{Debugging} &
        \textbf{Self-generated} & 
        \textbf{Multiple} & 
        \textbf{Self-reflection} \\
        \textbf{Test execution} &
        \textbf{execution} &
        \textbf{} & 
        \textbf{tests} & 
        \textbf{languages} \\
        \midrule
        AlphaCode \citep{li2022competition} & \greencheck & \redcross & \redcross & \greencheck & \redcross \\
        \hline
        CodeT \citep{chen2022codet} & \greencheck & \redcross & \greencheck & \redcross & \redcross \\
        \hline
        Self-debugging \citep{chen2023teaching} & \greencheck & \greencheck & \redcross & \redcross & \redcross \\
        \hline
        CodeRL \citep{le2022coderl} & \greencheck & \greencheck & \redcross & \redcross & \redcross \\
        \hline
        \textbf{Reflexion (ours)} & \greencheck & \greencheck & \greencheck & \greencheck & \greencheck \\
        \bottomrule
    \end{tabular}
    \vspace{-10pt}
\end{table}
```

## Table 2
```latex
\begin{table}[htbp] 
  \centering
  \begin{tabular}{llll}
    \cmidrule(r){1-4}
    \textbf{Benchmark + Language} &
    \textbf{Prev SOTA Pass@1} &
    \textbf{SOTA Pass@1} &
    \textbf{Reflexion Pass@1} \\
    \midrule
    HumanEval (PY) & 65.8 (CodeT \citep{chen2022codet} + GPT-3.5) & 80.1 (GPT-4) &
        \textbf{91.0} \\
    HumanEval (RS) & -- & 60.0 (GPT-4) & \textbf{68.0} \\
    MBPP (PY) & 67.7 (CodeT \citep{chen2022codet} + Codex \citep{chen2021evaluating})
        & \textbf{80.1} (GPT-4) & 77.1 \\
    MBPP (RS) & -- & 70.9 (GPT-4) & \textbf{75.4} \\
    Leetcode Hard (PY) & -- & 7.5 (GPT-4) & \textbf{15.0} \\
    \bottomrule
  \end{tabular}
  \caption{Pass@1 accuracy for various model-strategy-language combinations. The
  base strategy is a single code generation sample. All instruction-based models
  follow zero-shot code generation.}
  \label{tbl:programming:success}
\end{table}
```

## Table 3
```latex
\begin{table}[htbp] 
  \centering
  \begin{tabular}{lllllll}
    \toprule
    \textbf{Benchmark + Language} &
    \textbf{Base} &
    \textbf{Reflexion} &
    \textbf{TP} &
    \textbf{FN} &
    \textbf{FP} &
    \textbf{TN} \\
    \midrule
    HumanEval (PY) & 0.80 & \textbf{0.91} & 0.99 & 0.40 & 0.01 & 0.60 \\
    MBPP (PY) & \textbf{0.80} & 0.77 & 0.84 & 0.59 & 0.16 & 0.41 \\
    HumanEval (RS) & 0.60 & \textbf{0.68} & 0.87 & 0.37 & 0.13 & 0.63 \\
    MBPP (RS) & 0.71 & \textbf{0.75} & 0.84 & 0.51 & 0.16 & 0.49 \\
    \bottomrule
  \end{tabular}
  \caption{Overall accuracy and test generation performance for HumanEval and
      MBPP. For Rust, HumanEval is the hardest 50 problems from HumanEval Python
      translated to Rust with MultiPL-E \citep{cassano2022multiple}. TP: unit
      tests pass, solution pass; FN: unit tests fail, solution pass; FP: unit
      tests pass, solution fail; TN: unit tests fail, solution fail.}
    \label{tbl:programming:failures}
\end{table}
```

## Table 4
```latex
\begin{table}[htbp]
  \centering
  \begin{tabular}{llll}
    \cmidrule(r){1-4}
    \textbf{Approach} & 
    \textbf{Test Generation} &
    \textbf{Self-reflection} &
    \textbf{Pass@1 (Acc)} \\
    \midrule
     Base model & False & False & 0.60 \\
     Test generation omission & False & True & 0.52 \\
     Self-reflection omission & True & False & 0.60 \\
     \textbf{Reflexion} & True & True & \textbf{0.68} \\
    \bottomrule
  \end{tabular}
  \caption{Pass@1 accuracy for various compromised approaches on the
  Reflexion approach using GPT-4 as the base model on HumanEval Rust
  - 50 hardest problems}
  \label{tbl:programming:ablation} \end{table}
```

## Table 5
```latex
\begin{table}[htbp]
  \centering
  \begin{tabular}{lll}
    \cmidrule(r){1-3}
    \textbf{Approach} & 
    \textbf{Pass@1 accuracy (avg over 8 trials)} &
    \textbf{Pass@1 accuracy (std)} \\
    \midrule
     Baseline & 0.26 & 0.00481 \\
     Reflexion & 0.26 & 0.00305 \\
    \bottomrule
  \end{tabular}
  \caption{Pass@1 accuracy on HumanEval Python using starchat-beta~\citep{li2023starcoder}.}
  \label{tbl:programming:starchat}
\end{table}
```

## Table 6
```latex
\begin{table}[htbp]
  \centering
  \begin{tabular}{lll}
    \cmidrule(r){1-3}
    \textbf{Model} & 
    \textbf{Baseline accuracy} &
    \textbf{Reflexion accuracy} \\
    \midrule
     CoT (GT) + text-davinci-003 & 0.60 & \textbf{0.77} \\
     CoT (GT) + gpt-3.5-turbo & 0.57 & \textbf{0.71} \\
     CoT (GT) + gpt-4 & 0.68 & \textbf{0.80} \\
     ReAct + text-davinci-003 & 0.30 & \textbf{0.55} \\
     ReAct + gpt-3.5-turbo & 0.26 & \textbf{0.38} \\
     ReAct + gpt-4 & 0.39 & \textbf{0.51} \\
    \bottomrule
  \end{tabular}
  \caption{Pass@1 accuracy on 100 HotPotQA using various models.}
  \label{tbl:reasoning:othermodels}
\end{table}
```

