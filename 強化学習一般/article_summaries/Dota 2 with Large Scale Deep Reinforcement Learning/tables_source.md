# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}
\centering
\begin{tabular}{cccp{9cm}}
\label{allsurgeries} 
Date & Iteration & \# params & Change\\
\hline
% (jie) Data pulled from big experiment log spreadsheet. I decided to leave out experiments which did not change parameter sizes or have an interesting explanation - they are commented out here for reference.
6/30/2018 & 1 & 43,436,520 & Experiment started \\ % dota-5a
%7/4/2018 & 5,651 & 43,436,520 &  \\ % dota-5b
%7/27/2018 & 50,061 & 43,519,866 &  \\ % dota-5c
%8/2/2018 & 61,211 & 43,519,866 &  \\ % dota-5d OR dota-5d-v2 ??
%8/9/2018 & 72,401 & 43,519,866 &  \\ % dota-5d-v3
%8/14/2018 & 78,001 & 43,519,866 &  \\ % dota-5d-v4
8/17/2018 & 81,821 & 43,559,322 & \dota version 7.19 adds new items, abilities, etc.\\ % dota-5d-719-fp16-a
8/18/2018 & 84,432 & 43,805,274 & Change environment to single courier;\newline remove ``cheating'' observations \\ % courier-2
%8/19/2018 & 86,811 & 43,805,274 &  \\ % courier-3
%8/20/2018 & 89,151 & 43,805,274 &  \\ % five
8/26/2018 & 91,471 & 156,737,674 & Double LSTM size \\ % five-2
9/27/2018 & 123,821 & 156,809,485 & Support for more heroes \\ % babel-2, added all of babel.
10/3/2018 & 130,921 & 156,809,501 & Obs: Roshan spawn timing \\ % babel-3
%10/5/2018 & 132,051 & 156,809,501 &  \\ % babel-4
10/12/2018 & 140,402 & 156,811,805 & Item: Bottle\\ % babel-8
10/19/2018 & 144,121 & 156,286,925 & Obs: Stock counts;\newline Obs: Remove some obsolete obs \\ % babel-12 removed multiple horizons & scripted consumable observations
10/24/2018 & 150,111 & 156,286,867 & Obs: Neutral creep \& rune spawn timers \\ % babel-13
%11/6/2018 & 156,862 & 156,286,867 &  \\ % babel-17
11/7/2018 & 161,482 & 156,221,309 & Obs: Item swap cooldown;\newline Obs: Remove some obsolete obs\\ % babel-18 also removed obsolete observations
%11/9/2018 & 167,840 & 156,221,309 &  \\ % afk-1b
11/28/2018 & 185,749 & 156,221,669 & Item: Divine rapier;\newline Obs: Improve observation of stale enemy heroes \\ % afk-2
%11/30/2018 & 187,591 & 156,221,669 &  \\ % afk-3
12/10/2018 & 193,701 & 157,378,165 & Obs: Modifiers on nonhero units. \\ % afk-4d
12/14/2018 & 196,800 & 157,650,795 & Action: Consumables on allies;\newline Obs: Line of sight information;\newline Obs: next item this hero will purchase;\newline Action: buyback \\ % afk-5b
12/20/2018 & 203,241 & 157,679,655 & \dota version 7.20 adds new items, new item slot, changes map, etc;\newline Obs: number of empty inventory slots \\ % afk-6b
%1/4/2019 & 208,501 & 157,679,655 &  \\ % afk-7
%1/7/2019 & 210,701 & 157,679,655 &  \\ % afk-8
1/23/2019 & 211,191 & 158,495,991 & Obs: Improve observations of area of effects;\newline Obs: improve observation of modifiers' duration;\newline Obs: Improve observations about item Power Treads. \\ % jan-2
%1/24/2019 & 211,953 & 158,495,991 &  \\ % jan-3
%1/29/2019 & 212,596 & 158,495,991 &  \\ % jan-29
4/5/2019 & 220,076 & 158,502,815 & \dota version 7.21 adds new items, abilities, etc. \\ % apr-5
%4/8/2019 & 223,713 & 158,502,815 &  \\ % apr-8
%4/10/2019 & 224,921 & 158,502,815 &  \\ % apr-10
% 4/15/2019 & \todo{??} & \todo{??} & Add auxiliary prediction of networth. \\ % apr-15
\end{tabular}
\caption{All successful surgeries and major environment changes performed during the training of \openaifive. This table does not include surgeries which were ultimately reverted due to training failures, nor minor environment changes (such as improvements to partial reward weights or scripted logic). ``Obs'' indicates than a new observation was added as an input to the model or an existing one was changed. ``Action'' indicates that a new game action was made available, along with appropriate observations about the state of that action. ``Item'' indicates that a new item was introduced, including observation of the item and the action to use the item. The \dota version updates (7.19, 7.20 and 7.21) include many new items, actions, and observations.}
\label{table:list-surgeries}
\end{table}
```

## Table 2
```latex
\begin{table}
\begin{tabular}{lll}
Action Target Type & Example & Parameters \\\hline
No Target & Power Treads & Delay
\\
Point Target & Move & Delay, Offset (Caster)
\\
Unit Target & Attack & Delay, Unit Selection (Regular)
\\
Unit Offset Target & Sniper's Shrapnel & Delay, Unit Selection (Regular), Offset (Regular)
\\
Teleport Target & Town Portal Scroll & Delay, Unit Selection (Teleport), Offset (Regular)
\\
Ward Target & Place Observer Ward & Delay, Offset (Ward)
\\
\end{tabular}
\caption{\textbf{Action Target Types}}
\label{table:action-target-types}
\end{table}
```

## Table 3
```latex
\begin{table}
\begin{threeparttable}
\begin{tabular}{l|cccc}
Param & \cleanexpname & \openaifive & Baseline\\
\hline
Frameskip\tnote{e} & 4 & 4 & 4 \\
LSTM Unroll length\tnote{e} & 16 & 16 & 16 \\
Samples Per Segment\tnote{e} & 16 & 16 & 16 \\
Number of optimizer GPUs & 512 & 480$\leftrightarrow$1,536& 64 \\
Batch Size/optimizer GPU (samples) & 120 & 120$\leftrightarrow$128 & 120 \\
Total Batch Size (samples)\tnote{a} & 61,440 & 61,440$\leftrightarrow$196,608 & 7,680 \\
Total Batch Size (timesteps)\tnote{a} & 983,040 & 983,040$\leftrightarrow$3,145,728 & 122,880\\
Number of rollout GPUs & 512 & 500$\leftrightarrow$1,440 & 64 \\
Number of rollout CPUs & 51,200 & 80,000$\leftrightarrow$172,800 & 6,400 \\
Steps per Iteration & 32 & 32 & 32 \\
LSTM Size & 4096 & 2048 $\rightarrow$ 4096 & 4096 \\
Sample Reuse & 1.0 $\leftrightarrow$ 1.1 & 0.8$\leftrightarrow$2.7 & 1.0$\leftrightarrow$1.1 \\
Team Spirit & 0.3 $\rightarrow$ 0.8 & 0.3 $\rightarrow$ 1.0 & 0.3 \\ 
GAE Horizon & 180 secs $\rightarrow$ 360 secs & 60 secs $\rightarrow$ 840 secs & 180 secs\\
GAE $\lambda$ & 0.95 & 0.95 & 0.95 \\
PPO clipping & 0.2 & 0.2 & 0.2 \\
Value loss weight\tnote{c} & 1.0 & $0.25\leftrightarrow 1.0$ & 1.0 \\
Entropy coefficient & 0.01 $\rightarrow$ 0.001 & 0.01 $\rightarrow$ 0.001 & 0.01 \\
Learning rate & 5e-5 $\rightarrow$ 5e-6 & 5e-5 $\leftrightarrow$ 1e-6 & 5e-5\\
Adam $\beta_1$ & 0.9 & 0.9 & 0.9 \\
Adam $\beta_2$ & 0.999 & 0.999 & 0.999 \\
Past opponents\tnote{b} & 20\% & 20\% & 20\% \\
Past Opponents Learning Rate\tnote{d} & 0.01 & 0.01 & 0.01\\
\end{tabular}
\begin{tablenotes}
    \item[a] Batch size can be measured in samples (each an unrolled LSTM of 16 frames) or in individual timesteps.
    \item[b] Fraction of games played against past opponents (as opposed to self-play).
    \item[c] We normalize rewards using a running estimate of the standard deviation, and the value loss weight is applied post-normalization.
    \item[d] See \autoref{sec:selfplay}.
    \item[e] See \autoref{fig:timescales} for definitions of the various timescale subdivisions of a rollout episode.
\end{tablenotes}
\end{threeparttable}
\caption{\textbf{Hyperparameters: } The \openaifive and \cleanexpname columns indicate what was done for those individual experiments. For those which were modified during training, $x\rightarrow y$ indicates a smooth monotonic transition (usually a linear change over one to three days), and $x\leftrightarrow y$ indicates a less controlled variation due to either ongoing experimentation or distributed systems fluctuations. The ``Baseline'' indicates the default values for all the experiments in \autoref{appendix:substudies} (each individual experiment used these hyperparameters other than any it explicitly studied, for example in \autoref{sec:methods:batchsize} the batch size was changed from the baseline in each training run, but all the other hyperparameters were from this table).}
\label{table:hyperparams}
\end{table}
```

## Table 4
```latex
\begin{table}
%%% This table's formatting is really hacky. If anyone wants to fix it that would be great.
\begin{scriptsize}
\begin{threeparttable}
\begin{subtable}[t]{0.3\textwidth}
\begin{tabular}[t]{|p{4cm}|c|}
  \hline
  \textbf{Global data}   & \textbf{22}\\\hline
  time since game started & 1 \\\hline
  is it day or night? &  \\
  time to next day/night change & 2 \\\hline
  time to next spawn: creep, neutral, bounty, runes & 4 \\\hline
  time since seen enemy courier &  \\
  is that $>$ 40 seconds?\tnote{a} & 2 \\\hline
  min\&max time to Rosh spawn & 2 \\\hline
  Roshan's current max hp & 1 \\\hline
  is Roshan definitely alive? & 1 \\\hline
  is Roshan definitely dead? & 1 \\\hline
  Next Roshan drops cheese? & 1 \\\hline
  Next Roshan drops refresher? & 1 \\\hline
  Roshan health randomization\tnote{b} & 1 \\\hline
  Glyph cooldown (both teams) & 2 \\\hline
  Stock counts\tnote{c} & 4 \\\hline
\end{tabular}
\begin{tabular}{|p{4cm}|c|}
  \hline
  \textbf{Per-unit (189 units)}   &  \textbf{43}\\\hline
  position (x, y, z) & 3 \\\hline
  facing angle (cos, sin) & 2 \\\hline
  currently attacking?\tnote{e} & \\
  time since last attack\tnote{d} & 2 \\\hline
  max health & \\
  last 16 timesteps' hit points & 17 \\\hline
  attack damage, attack speed & 2 \\\hline
  physical resistance & 1 \\\hline
  invulnerable due to glyph? & \\
  glyph timer & 2 \\\hline
  movement speed & 1 \\\hline
  on my team? neutral? & 2 \\\hline
  animation cycle time & 1 \\\hline
  eta of incoming ranged \& tower creep projectile (if any) & \\
  \# melee creeps atking this unit\tnote{d} & 3 \\\hline
  [Shrine only] shrine cooldown & 1 \\\hline
  vector to me (dx, dy, length)\tnote{e} & 3 \\\hline
  am I attacking this unit?\tnote{e} & \\
  is this unit attacking me?\tnote{d,e} & \\
  eta projectile from unit to me\tnote{e} & 3 \\\hline
  % \hline
  % textbf{Per-unit categorical data}   &  \\\hline
  \categorical unit type & \categorical 1 \\\hline
  \categorical current animation & \categorical 1 \\
  \hline
\end{tabular}
\end{subtable}
\hfill
\begin{subtable}[t]{0.3\textwidth}
\begin{tabular}[t]{|p{4cm}|c|}
  \hline
  \textbf{Per-hero add'l (10 heroes)}   &  \textbf{25}\\\hline
  is currently alive? & 1 \\\hline
  number of deaths & 1 \\\hline
  hero currently in sight? & \\
  time since this hero last seen & 2 \\\hline
  hero currently teleporting? & \\
  if so, target coordinates (x, y) & \\
  time they've been channeling & 4 \\\hline
  respawn time & 1 \\\hline
  current gold (allies only) & 1 \\\hline
  level & 1 \\\hline
  mana: max, current, \& regen & 3 \\\hline
  health regen rate & 1 \\\hline
  magic resistance & 1 \\\hline
  strength, agility, intelligence & 3 \\\hline
  currently invisible? & 1 \\\hline
  % Due to a bug this is always zero.
  % is\_in\_ability\_phase & \\
  % I think this is the same as the next one.
  % has\_active\_ability & \\
  is using ability? & 1\\\hline
  \# allied/enemy creeps/heroes in line btwn me and this hero\tnote{e} & 4 \\\hline
  \hline
  \textbf{Per-allied-hero additional (5 allied heroes)}   & \textbf{211} \\\hline
  Scripted purchasing settings\tnote{b} & 7 \\\hline
  Buyback: has?, cost, cooldown & 3 \\\hline
  Empty inventory \& backpack slots & 2 \\\hline
  Lane Assignments\tnote{b} & 3 \\\hline
  Flattened nearby terrain: 14x14 grid of passable/impassable? & 196 \\\hline
  \categorical scripted build id & \categorical\\
  \categorical next item to purchase\tnote{b} & \categorical 2 \\\hline
  \hline
  \textbf{Nearby map (8x8)\tnote{e}}   & \textbf{6} \\\hline
  terrain: elevation, passable? & 2 \\\hline
  allied \& enemy creep density & 2 \\\hline
  area of effect spells in effect.\tnote{f} & 2 \\\hline
  \categorical area of effect spells in effect.\tnote{f} & \categorical 2 \\\hline
  \hline
  \textbf{Previous Sampled Action\tnote{e}}   & \textbf{310} \\\hline
  Offset? (Regular, Caster, Ward) & 3x2x9 \\\hline
  % Omitting tp head because that can't possibly matter and it's hard to explain.
  Unit Target's Embedding & 128 \\\hline
  Primary Action's Embedding & 128 \\\hline
\end{tabular}
\end{subtable}
\hfill
\begin{subtable}[t]{0.3\textwidth}
\begin{tabular}[t]{|p{4cm}|c|}
  \hline
  \textbf{Per-modifier (10 heroes x 10 modifiers \& 179 non-heroes x 2 modifiers)}   &  \textbf{2}\\\hline
  remaining duration & 1 \\\hline
  stack count & 1 \\\hline
  \categorical modifier name & \categorical 1 \\
  \hline
  \hline
  \textbf{Per-item (10 heroes x 16 items)}   & \textbf{13}\\\hline
  location one-hot (inventory/backpack/stash) & 3 \\\hline
  charges & 1 \\\hline
  is on cooldown? & \\
  cooldown time & 2 \\\hline
  is disabled by recent swap? & \\
  item swap cooldown & 2 \\\hline
  toggled state & 1 \\\hline
  special Power Treads one-hot & \\
  (str/agi/int/none) & 4\\\hline
  \categorical item name & \categorical 1 \\
  \hline
  \hline
  \textbf{Per-ability (10 heroes x 6 abilities)}   &  \textbf{7}\\\hline
  cooldown time & 1 \\\hline
  in use? & 1 \\\hline
  castable & 1 \\\hline
  Level 1/2/3/4 unlocked?\tnote{d} & 4\\\hline
  \categorical ability name & \categorical 1 \\
  \hline
  \hline
  \textbf{Per-pickup (6 pickups)}   &  15\\\hline
  status one-hot (present/not present/unknown) & 3 \\\hline
  location (x, y) & 2 \\\hline
  distance from all 10 heroes & 10 \\\hline
  \categorical pickup name & \categorical 1 \\
  \hline
  \hline
  \textbf{Minimap (10 tiles x 10 tiles)}   &  \textbf{9}\\\hline
  fraction of tile visible & 1 \\\hline
  \# allied \& enemy creeps & 2 \\\hline
  \# allied \& enemy wards & 2 \\\hline
  \# enemy heroes & 1 \\\hline
  cell (x, y, id) & 3 \\\hline
  % "id" is my description of a really confusing thing that appears to be number of neutral camps in the cell (Roshan counts as 2) + 3 if there's a bounty rune.
  % It's actually a 10x10x12 array, but we appear to never use indices 1 and 2, and index 3 is identical to index 4.
\end{tabular}
\end{subtable}
\end{threeparttable}
\begin{threeparttable}
\begin{tablenotes}
    \item[a] These observations are leftover from an early version of Five which played a restricted 1v1 version of the game. They are likely obsolete and not needed, but this was not tested.
    \item[b] These observations are about our per-game randomizations. See \autoref{sec:methods:exploration}.
    \item[c] For items: gem, smoke of deciept, observer ward, infused raindrop.
    \item[d] Observations are not visible per-se, but can be estimated. We use scripted logic to estimate them from visible observations.
    \item[e] These observations (only) are different for the five different heroes on the team.
    \item[f] This observation appears twice, and serves as an example of the difficulties of surgery. Although this is a categorical input, we began by treating it as a float input to save on engineering work (this observation is unlikely to be very important). Later the time came to upgrade it to a properly embedded categorical input, but our surgery tools do not support removing existing observations. Hence we added the new observation, but were forced to leave the deprecated observation as well.
\end{tablenotes}
\end{threeparttable}
\end{scriptsize}
\caption{
\textbf{Full Observation Space: }
All observations \openaifive receives at each time step. Blue rows are categorical data. Entries with a question mark are boolean observations (only take values 0 or 1 but treated as floats otherwise). The bulk of the observations are per-unit observations, observed for each of 189 units: heroes (5), creeps (30), buildings (21), wards (30), and courier (1) for each team, plus 15 neutrals. If the number of visible units in a category is less than the allotted number, the rest are padded with zeroes. If more, we observe only the units closest to allied heroes. Units in fog of war are not observed. When enemy heroes are in fog of war, we reuse the observation from the last time step when the unit was visible.
}
\label{table:full-obs}
\end{table}
```

## Table 5
```latex
\begin{table}
\begin{threeparttable}
\begin{tabular}{c|c|c|p{8cm}}
    Name          & Reward & Heroes & Description \\\hline
    Win           & 5      & Team & \\
    Hero Death    & -1     & Solo & \\
    Courier Death & -2     & Team & \\
    XP Gained     & 0.002  & Solo & \\
    Gold Gained   & 0.006  & Solo & For each unit of gold gained. Reward is not lost when the gold is spent or lost. \\
    Gold Spent    & 0.0006 & Solo & Per unit of gold spent on items without using courier. \\
    Health Changed& 2      & Solo & Measured as a fraction of hero's max health.\tnote{$\ddagger$} \\
    Mana Changed  & 0.75   & Solo & Measured as a fraction of hero's max mana. \\
    Killed Hero   & -0.6   & Solo & For killing an enemy hero. The gold and experience reward is very high, so this reduces the total reward for killing enemies. \\
    Last Hit      & -0.16  & Solo & The gold and experience reward is very high, so this reduces the total reward for last hit to $\sim 0.4$. \\
    Deny          & 0.15   & Solo & \\
    Gained Aegis  & 5      & Team & \\
    Ancient HP Change & 5     & Team & Measured as a fraction of ancient's max health. \\
    Megas Unlocked   & 4      & Team & \\
    T1 Tower\tnote{*}      & 2.25   & Team & \\
    T2 Tower\tnote{*}      & 3   & Team & \\
    T3 Tower\tnote{*}    & 4.5 & Team & \\
    T4 Tower\tnote{*}    & 2.25 & Team & \\
    Shrine\tnote{*}      & 2.25 & Team & \\
    Barracks\tnote{*}    & 6 & Team & \\
    Lane Assign\tnote{$\dagger$}  & -0.15 & Solo & Per second in wrong lane. \\
\end{tabular}
\begin{tablenotes}
    \item[*] For buildings, two-thirds of the reward is earned linearly as the building loses health, and one-third is earned as a lump sum when it dies.
    \item[$\dagger$] See \autoref{sec:lane-assignments}.
    \item[$\ddagger$] Hero's health is quartically interpolated between 0 (dead) and 1 (full health); health at fraction $x$ of full health is worth $\left(x + 1 - (1-x)^4\right)/2$. This function was not tuned; it was set once and then untouched for the duration of the project.
\end{tablenotes}
\end{threeparttable}
\caption{Shaped Reward Weights}
\label{table:rewards}
\end{table}
```

## Table 6
```latex
\begin{table}
\begin{tabular}{c|c|c|c|l}
Opponent & Result & Duration & Version & Restrictions\\
\hline
\multicolumn{5}{l}{June 6, 2018 - Internal Event}\\
\hline
Internal team & win & 15:15 (surr) & 7.13 & Mirror match, multiple couriers, no invis\\
Internal team & win & 20:51 & 7.13 & Mirror match, multiple couriers, no invis\\
Audience team & win & 31:33 & 7.13 & Mirror match, multiple couriers, no invis\\
Audience team & win & 23:33 (surr) & 7.13 & Mirror match, multiple couriers, no invis\\
\hline
\multicolumn{5}{l}{August 5, 2018 - Benchmark}\\
\hline
Caster team & win & 21:38 (surr) & 7.16 & Drafted, multiple couriers\\
Caster team & win & 24:56 (surr) & 7.16 & Drafted, multiple couriers\\
Caster team & lose & 35:47 & 7.16 & Audience draft, multiple couriers\\
\hline
\multicolumn{5}{l}{August 9, 2018 - Private eval}\\
\hline
Team Secret & win & 17:00 (surr) & 7.16 & Drafted, multiple couriers\\
Team Secret & lose & 48:46 & 7.16 & Drafted, multiple couriers\\
Team Secret & lose & 38:55 & 7.16 & Drafted, multiple couriers\\
\hline
\multicolumn{5}{l}{August 22-23, 2018 - The International}\\
\hline
Pain Gaming & lose & 52:29 & 7.19 & Pre-set lineup\\
Chinese Legends & lose & 45:44 & 7.19 & Pre-set lineup\\
\hline
\multicolumn{5}{l}{October 5, 2018 - Private eval}\\
\hline
Team Lithium & win & 48:57 & 7.19 & TI pre-set lineup\\
Team Lithium & win & 48:16 & 7.19 & TI pre-set lineup\\
Team Lithium & win & 31:33 & 7.19 & Drafted\\
\hline
\multicolumn{5}{l}{January 16, 2019 - Private eval}\\
\hline
SG Esports & win & 24:29 (surr) & 7.19 & TI pre-set lineup\\
SG Esports & win & 25:08 (surr) & 7.19 & Drafted\\
SG Esports & win & 27:36 (surr) & 7.20 & Mirror match\\
SG Esports & win & 25:30 (surr) & 7.20 & Mirror match\\
\hline
\multicolumn{5}{l}{February 1, 2019 - Private eval}\\
\hline
Alliance & win & 17:11 & 7.20d & Drafted\\
Alliance & win & 31:33 & 7.20d & Drafted\\
Alliance & win & 28:16 & 7.20d & Reverse drafted\\
\hline
\multicolumn{5}{l}{April 13, 2019 - \openaifinals}\\
\hline
OG & win & 38:18 & 7.21d & Drafted\\
OG & win & 20:51 & 7.21d & Drafted\\
\end{tabular}
\caption{Major matches of \openaifive against high-skill human players.}
\label{table:milestonegames}
\end{table}
```

