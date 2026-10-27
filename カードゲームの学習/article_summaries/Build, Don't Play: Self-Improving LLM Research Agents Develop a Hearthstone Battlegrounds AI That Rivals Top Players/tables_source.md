# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1 (tab:autonomy)
```latex
\begin{table}[t]
  \centering
  \caption{\textbf{Autonomous research in numbers.}}
  \label{tab:autonomy}
  \small
  \begin{tabular}{@{}lr@{\hspace{1em}}lr@{}}
    \toprule
    Duration (from scratch to ladder) & 20 days & Experiments registered & about 10,000 \\
    Engine code (Rust) & 63k lines & Delivered agent versions & 23 \\
    Rule verification records & 375 & Fixes from live games & 184 \\
    Human messages & 418 (0.6\% of all messages) & & \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 2 (tab:envs)
```latex
\begin{table}[t]
  \centering
  \caption{\textbf{Battlegrounds environments and agents.} Only \envname reproduces the full live
  game, and only \agentname plays real games.}
  \label{tab:envs}
  \small
  \resizebox{\linewidth}{!}{%
  \begin{tabular}{@{}lcccccc@{}}
    \toprule
    & \makecell{Full content,\\current patch} & Heroes & \makecell{Recruit +\\combat} &
      \makecell{Trainable\\batch API} & \makecell{Aligned with\\live games} & \makecell{Plays live\\games} \\
    \midrule
    MCTS assistant \citep{zolboot2022hearthstone} & \xmark & partial & \cmark & \xmark & \xmark & \xmark \\
    BGSimulator \citep{bgsimulator} & \xmark & \xmark & \cmark & \cmark & \xmark & \xmark \\
    Firestone / Bob's Buddy \citep{firestone,bobsbuddy} & \cmark & \cmark & \xmark & \xmark & \cmark & \xmark \\
    DeepBattler \citep{deepbattler} & n/a & n/a & n/a & \xmark & n/a & \xmark \\
    \midrule
    \envname + \agentname (ours) & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
    \bottomrule
  \end{tabular}}
\end{table}
```

## Table 3 (tab:agent)
```latex
\begin{table}[t]
  \centering
  \caption{\textbf{\agentname against baselines, and the opponent ablation.} One simulator build,
  three unseen seeds, 24,576 games per row, seven reality-calibrated opponent seats; main exam
  (left) and the harder exam (right). The ablation pair shares its starting point and training
  budget.}
  \label{tab:agent}
  \footnotesize
  \setlength{\tabcolsep}{4pt}
  \begin{tabular}{@{}lcccccc@{}}
    \toprule
    & \multicolumn{3}{c}{Main exam} & \multicolumn{3}{c}{Harder exam} \\
    \cmidrule(lr){2-4}\cmidrule(l){5-7}
    Agent & Place $\downarrow$ & First \% & Top-4 \% & Place $\downarrow$ & First \% & Top-4 \% \\
    \midrule
    Random legal actions & 7.97 & 0.0 & 0.0 & 7.97 & 0.0 & 0.0 \\
    Scripted bot & 7.54 & 0.0 & 0.5 & 7.61 & 0.0 & 0.2 \\
    \agentname, first version (TA-1) & 3.40 & 1.9 & 83.4 & 4.07 & 1.1 & 65.4 \\
    \agentname, mid version (TA-11) & 2.83 & 18.5 & 85.5 & 3.75 & 8.9 & 67.8 \\
    \agentname, final (TA-23) & \textbf{2.33} & \textbf{41.5} & \textbf{89.0} & \textbf{3.28} & \textbf{23.8} & \textbf{73.2} \\
    \midrule
    \multicolumn{7}{@{}l}{\emph{Opponents} (from the same checkpoint, 150 iterations each)} \\
    \quad uncalibrated opponent libraries & 2.74 & 20.9 & 86.8 & 3.64 & 10.3 & 69.6 \\
    \quad reality-calibrated libraries & \textbf{2.65} & \textbf{27.2} & 86.6 & \textbf{3.59} & \textbf{13.5} & 69.2 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 4 (tab:bench-results)
```latex
\begin{table}[t]
  \centering
  \caption{\textbf{\benchname results} (368 tasks; accuracy in \%). Play: the 30 scenarios
  \agentname answers, mean over scenarios.
  Real-time: the play score counting only answers given within 1~s. Rules: the ten rule-execution
  scenarios (answered by \envname by construction, so not scored for \agentname). Time: median
  seconds per task (LLMs: estimated from Artificial Analysis medians, \cref{app:bench}; others
  measured).}
  \label{tab:bench-results}
  \footnotesize
  \setlength{\tabcolsep}{2.6pt}
  \begin{tabular}{@{}lrrrrrrrrrr@{}}
    \toprule
    System & Play & Real-time & Combat & Position & Order & Targets & Select & Strategy & Rules & Time (s) \\
    \midrule
    \agentname{} & 91 & 90 & 100 & 98 & 100 & 98 & 64 & 75 & -- & 0.03 \\
    \midrule
    Claude Opus 5.5 & 52 & 0 & 67 & 32 & 60 & 52 & 41 & 38 & 92 & 6.2 \\
    Claude Sonnet 5.5 & 53 & 0 & 58 & 45 & 68 & 52 & 39 & 29 & 85 & 1.4 \\
    GPT-6 Astra & 63 & 0 & 75 & 55 & 72 & 55 & 50 & 54 & 95 & 2.4 \\
    GPT-6.1 Sol & 46 & 0 & 50 & 42 & 48 & 28 & 55 & 43 & 56 & 2.0 \\
    Gemini 3.8 Flash & 44 & 0 & 52 & 32 & 32 & 48 & 41 & 43 & 90 & 9.9 \\
    Grok 4.7 & 22 & 0 & 29 & 0 & 5 & 20 & 38 & 37 & 79 & 4.8 \\
    GLM-5.3 & 40 & 0 & 54 & 20 & 40 & 38 & 41 & 34 & 65 & 26 \\
    Kimi-K2.6 & 28 & 0 & 31 & 8 & 22 & 38 & 36 & 27 & 56 & 16 \\
    Intern-S2-Preview & 32 & 0 & 31 & 12 & 32 & 40 & 44 & 34 & 54 & 2.8 \\
    DeepSeek-V4.1-Flash & 26 & 26 & 29 & 18 & 15 & 32 & 25 & 19 & 29 & 0.91 \\
    Jev & 37 & 37 & 56 & 25 & 20 & 45 & 40 & 17 & 35 & 0.26 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 5 (tab:roles)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{Roles in \frameworkname.}}
  \label{tab:roles}
  \small
  \begin{tabular}{@{}lL{0.62\linewidth}@{}}
    \toprule
    Role & Responsibilities \\
    \midrule
    Research lead & reads the memory, chooses the next problem, dispatches work, records findings \\
    Environment & implements rules and content, verifies rules, fixes discrepancies found in live games \\
    Training & designs recipes and curricula, registers training runs and their successors \\
    Opponent modelling & builds and recalibrates the human-like opponent libraries \\
    Evaluation \& audit & evaluates within one build, re-checks candidates on unseen seeds, reviews \\
    Deployment & maintains the client controller and the models' input formats, collects live games \\
    Sub-agents & short tasks: probes, features behind a test gate, data analysis, reviews \\
    Human researcher & sets goals, rules on ambiguous mechanics, follows progress; in live games presses the shortcut key the AI names \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 6 (tab:releases)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{\agentname releases.} TA-1 to TA-23 in release order, by day of the project, with
  the change each release introduced; the paper uses these names throughout.}
  \label{tab:releases}
  \footnotesize
  \begin{tabular}{@{}llL{0.25\linewidth}llL{0.25\linewidth}@{}}
    \toprule
    Release & Day & Change & Release & Day & Change \\
    \midrule
    TA-1 & 4 & first model & TA-13 & 13 & main line \\
    TA-2 & 5 & main line & TA-14 & 14 & opponents recalibrated to live games \\
    TA-3 & 6 & opponents fitted to human statistics; first-place goal & TA-15 & 14 & play-order fix \\
    TA-4 & 6 & main line & TA-16 & 14 & new opponent libraries \\
    TA-5 & 7 & main line & TA-17 & 15 & graded opponent libraries \\
    TA-6 & 7 & main line & TA-18 & 16 & environment update \\
    TA-7 & 8 & main line & TA-19 & 17 & recalibrated opponents \\
    TA-8 & 8 & main line & TA-20 & 17 & main line \\
    TA-9 & 9 & environment update & TA-21 & 17 & environment update \\
    TA-10 & 9 & opponents from recorded games & TA-22 & 18 & main line \\
    TA-11 & 10 & merged specialist models & TA-23 & 18 & final \\
    TA-12 & 13 & main line &  & &  \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 7 (tab:hparams)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{Training configuration of the final stage (TA-23).}}
  \label{tab:hparams}
  \small
  \resizebox{\linewidth}{!}{%
  \begin{tabular}{@{}ll@{\hspace{2em}}ll@{}}
    \toprule
    Games per member $\times$ steps & 512 $\times$ 256 & Iterations per stage & 300 \\
    Decisions per iteration & about $1.05\times10^6$ & Minibatch / epochs & 8,192 / 1 \\
    Learning rate & $6\times10^{-6} \to 5\times10^{-6}$ & Clip / target KL & 0.2 / 0.05 \\
    $\gamma$ / $\lambda$ & 1.0 / 0.995 & Gradient norm clip & 1.0 \\
    Entropy / value / auxiliary coefficients & 0.002 / 0.5 / 0.1 & KL anchor to the stage's start & 0.1 for 100 iterations \\
    \bottomrule
  \end{tabular}}
\end{table}
```

## Table 8 (tab:model-size)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{Model size} (an early experiment: from scratch, same recipe, 400 iterations
  each).}
  \label{tab:model-size}
  \footnotesize
  \setlength{\tabcolsep}{4pt}
  \begin{tabular}{@{}lcccccc@{}}
    \toprule
    & \multicolumn{3}{c}{Main exam} & \multicolumn{3}{c}{Harder exam} \\
    \cmidrule(lr){2-4}\cmidrule(l){5-7}
    Network & Place $\downarrow$ & First \% & Top-4 \% & Place $\downarrow$ & First \% & Top-4 \% \\
    \midrule
    3.5M parameters (d=192, 4 layers) & 3.84 & 0.3 & 73.9 & 4.47 & 0.3 & 54.0 \\
    8M parameters (d=256, 6 layers) & 3.77 & 0.5 & 75.6 & 4.40 & 0.3 & 56.2 \\
    18M parameters (d=384, 8 layers) & \textbf{3.67} & 0.5 & \textbf{78.5} & \textbf{4.28} & 0.4 & \textbf{59.6} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 9 (tab:version-league)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{Eight versions in the same lobbies} (three seeds, 24,576 games per version; a fair
  share is a placement of 4.5, 12.5\% first and 50\% top-four).}
  \label{tab:version-league}
  \small
  \begin{tabular}{@{}llccc@{}}
    \toprule
    Version & Day & Avg.\ place & First (\%) & Top-4 (\%) \\
    \midrule
    TA-23 & 18 & 3.95 & 26.2 & 57.9 \\
    TA-21 & 17 & 4.06 & 23.5 & 56.7 \\
    TA-17 & 15 & 4.36 & 19.7 & 51.6 \\
    TA-14 & 14 & 4.40 & 14.9 & 52.4 \\
    TA-11 & 10 & 4.53 & 9.4 & 51.9 \\
    TA-3 & 6 & 4.76 & 4.4 & 46.6 \\
    TA-2 & 5 & 4.85 & 1.2 & 44.7 \\
    TA-1 & 4 & 5.10 & 0.6 & 38.2 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 10 (tab:ladder)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{Live-ladder games by \agentname version} (games linked to a
  single version with high confidence, without games with a client failure; ratings at the first and
  last game of each group). All games, failures included, are in \cref{tab:ladder-all}.}
  \label{tab:ladder}
  \small
  \begin{tabular}{@{}llrcccc@{}}
    \toprule
    Versions & Days & Games & Avg.\ place & First (\%) & Top-4 (\%) & Rating \\
    \midrule
    TA-2 & 5--6 & 26 & 3.46 & 3.8 & 76.9 & 6,000 $\to$ 7,177 \\
    TA-5--6 & 7--8 & 10 & 3.30 & 20.0 & 80.0 & 7,430 $\to$ 8,225 \\
    TA-8--10 & 8--10 & 47 & 3.57 & 12.8 & 66.0 & 8,117 $\to$ 8,348 \\
    TA-11 & 11--13 & 87 & 3.10 & 16.1 & 78.2 & 8,348 $\to$ 10,910 \\
    TA-12--14 & 13--16 & 28 & 3.36 & 7.1 & 78.6 & 11,001 $\to$ 12,329 \\
    TA-16--17 & 15--16 & 30 & 3.67 & 16.7 & 70.0 & 11,995 $\to$ 12,727 \\
    TA-19--23 & 17--18 & 46 & \textbf{2.37} & \textbf{32.6} & \textbf{91.3} & 12,727 $\to$ \textbf{14,007} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 11 (tab:top10)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{The agent against the server's ten highest-rated players}: each player's last 20
  records on the public leaderboard \citep{wallii} at the cut-off (placements estimated
  by the leaderboard from rating changes, the same measure for every player; players anonymised).}
  \label{tab:top10}
  \small
  \begin{tabular}{@{}lcccr@{}}
    \toprule
    Player & Avg.\ place & First (\%) & Top-4 (\%) & Rating change \\
    \midrule
    P1 & 3.03 & 50 & 65 & $-$319 \\
    P2 & 2.20 & 70 & 80 & +289 \\
    P3 & 2.43 & 55 & 85 & $-$88 \\
    P4 & 1.88 & 65 & 90 & +487 \\
    P5 & 2.50 & 55 & 75 & $-$76 \\
    P6 & 2.05 & 70 & 85 & +459 \\
    P7 & 2.20 & 60 & 80 & +67 \\
    P8 & 2.53 & 50 & 80 & +44 \\
    P9 & 2.53 & 45 & 85 & +140 \\
    P10 & 2.05 & 70 & 85 & +422 \\
    Top ten together (200 records) & 2.34 & 59 & 81 & +1,425 \\
    \midrule
    \agentname (rating $\approx$15,000) & \textbf{1.60} & \textbf{80} & \textbf{90} & \textbf{+1,282} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 12 (tab:ladder-all)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{All live-ladder games by version}, client failures included.}
  \label{tab:ladder-all}
  \small
  \begin{tabular}{@{}lrcccr@{}}
    \toprule
    Versions & Games & Avg.\ place & First (\%) & Top-4 (\%) & With failure \\
    \midrule
    TA-2 & 40 & 3.38 & 2.5 & 77.5 & 14 \\
    TA-5--6 & 24 & 3.12 & 20.8 & 79.2 & 14 \\
    TA-8--10 & 68 & 4.22 & 8.8 & 54.4 & 21 \\
    TA-11 & 89 & 3.07 & 16.9 & 78.7 & 2 \\
    TA-12--14 & 38 & 3.08 & 5.3 & 84.2 & 10 \\
    TA-16--17 & 48 & 3.15 & 20.8 & 79.2 & 18 \\
    TA-19--23 & 56 & 2.54 & 30.4 & 87.5 & 10 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 13 (tab:bench-cats)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{\benchname categories.} 40 scenarios, 960 tasks. \agentname answers
  through its own interface (\cref{sec:bench}); the ten rule-execution scenarios have no agent
  counterpart, because \envname executes the rules for it.}
  \label{tab:bench-cats}
  \small
  \begin{tabular}{@{}lL{0.46\linewidth}L{0.13\linewidth}l@{}}
    \toprule
    Category & Scenarios & Label & \agentname \\
    \midrule
    Rules (7) & legal actions; one-on-one fights; battlecry, spell and magnetic results;
      end- and start-of-turn effects; triples & executed & one-on-one \\
    Economy (5) & gold accounting; upgrade price; can I triple now; gold chains; best purchase
      for the next combat & executed / simulated & purchase \\
    Combat (6) & who attacks first; deterministic fights; win / tie / loss; expected damage;
      lethal risk; start-of-combat effects & simulated & all \\
    Positioning (5) & best of five arrangements; taunt and shield; deathrattle and reborn; against
      venomous; against cleave & simulated & all \\
    Ordering (5) & sell timing; play triggers; spells and minions; adjacent battlecries; mixed & simulated & all \\
    Targets (5) & spell, activate, Hero Power and magnetic targets; which minion to sell & simulated & all \\
    Selection (5) & hero; trinket; discover; choices in natural games; which card to play &
      human, simulated, play-out & all \\
    Strategy (2) & turn plans, early game (turns 4--7) and late game (turns 8+): upgrade, buy,
      refresh or save the Gold & play-out & all \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 14 (tab:bench-examples)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{Example tasks}, one per category (questions abridged; each task also shows the
  state and the rule text of every card). Labels come from \envname.}
  \label{tab:bench-examples}
  \footnotesize
  \begin{tabular}{@{}lL{0.55\linewidth}L{0.27\linewidth}@{}}
    \toprule
    Category & Question & Label \\
    \midrule
    Rules & You cast Misplaced Tea Set. List the Attack and Health of every minion afterwards. &
      [[9,6],[13,8]] (executed, three reseeded copies agree) \\
    Economy & Which tavern minions do you buy, in order, with 9 Gold, each played at once, to win
      the next combat against the warband shown? & positions 2,1,4 (win rate 8.9\%, best of 157
      sequences) \\
    Combat & Estimate the probabilities that you win, tie or lose this combat. &
      0.75 / 0.20 / 0.04 (4,096 combats) \\
    Positioning & Which of five arrangements of your warband (against a Cleave opponent) wins most
      often? & E (best by $\geq$5 points over 2,048 combats each) \\
    Ordering & In which order do you play three minions and sell one before the next combat? &
      B, D, C, A (win rate 90\%) \\
    Targets & Onto which of your Mechs do you magnetize Enchanted Sentinel? & position 0 (71\%) \\
    Selection & Which of three Discovered minions do you take and play? & Electric Synthesizer
      (19\%) \\
    Strategy & Turn 4, 6 Gold, upgrade price 5: upgrade, buy Strike Oil, refresh, or keep the
      Gold? & buy (placement 1.48 against 1.88 for the next best; 128 play-outs per plan) \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Table 15 (tab:tools)
```latex
\begin{table}[h]
  \centering
  \caption{\textbf{LLMs with \envname as a tool} (accuracy in \%, text-only / with tools per
  category; the agent column is \agentname on the same tasks).}
  \label{tab:tools}
  \footnotesize
  \setlength{\tabcolsep}{3pt}
  \begin{tabular}{@{}lrrrrrrrrrrr@{}}
    \toprule
    Model & Tasks & Text & Tools & Position & Order & Targets & Purchase & Select & Agent & Calls & Time (s) \\
    \midrule
    GPT-6 Astra & 144 & 62 & 97 & 55/98 & 72/100 & 55/92 & 75/88 & 69/100 & 99 & 5.2 & 21 \\
    GLM-5.3 & 144 & 38 & 81 & 20/82 & 40/62 & 38/95 & 38/62 & 75/94 & 99 & 5.8 & 11 \\
    Kimi-K2.6 & 144 & 26 & 65 & 8/68 & 22/35 & 38/98 & 25/0 & 50/88 & 99 & 8.9 & 39 \\
    Intern-S2-Preview & 144 & 32 & 41 & 12/40 & 32/30 & 40/45 & 12/12 & 69/75 & 99 & 9.8 & 18 \\
    DeepSeek-V4.1-Flash & 144 & 24 & 64 & 18/50 & 15/42 & 32/92 & 38/25 & 31/100 & 99 & 8.6 & 42 \\
    \bottomrule
  \end{tabular}
\end{table}
```

