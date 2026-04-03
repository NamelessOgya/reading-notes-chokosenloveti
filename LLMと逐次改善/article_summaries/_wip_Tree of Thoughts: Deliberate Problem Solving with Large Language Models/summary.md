# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

## 背景
大語彙言語モデル（LLMs）は一般的な問題解決において目覚ましい成果を挙げているが、従来の推論プロセスはトークンレベルでの左から右への自己回帰的な生成（直感的な「System 1」モード）に依存している。これにより、探索や戦略的な先読みが必要な問題、あるいは初期の決定が後続の選択肢を大きく制限するような問題（数学的パズル、クロスワード等）では正答を導き出せないという課題があった。これに対し、人間の認知プロセスに見られる「System 2」のような、より意識的で意図的な計画プロセス（複数の選択肢を探索し、状態を自己評価しながら先増やバックトラックを行うプロセス）をLLMに組み込むため、本研究では新たな推論フレームワーク「Tree of Thoughts（ToT）」を考案。

## 手法
ToT（Tree of Thoughts）は、従来の手法（Input-OutputプロンプティングやChain-of-Thoughtプロンプティング）を拡張し、問題解決に向けた中間ステップとしての論理的な思考単位（「thought」）の木構造を探索するフレームワークである。
ToTのフレームワークは以下の4つの要素から構成される：
1. **Thought Decompostion（思考の分解）**: 問題に応じて、数語からなる句や1行の数式、または全体計画の段落など、意味のある中間ステップを「thought」として分割する。
2. **Thought Generator（思考の生成）**: 状態 $s = [x, z_{1\cdots i}]$ が与えられたとき、$k$ 個の次の考え（候補）を生成する。手法には独立にサンプリングする方法（Sample）と、文脈を用いて連続的に提案させる方法（Propose）がある。
3. **State Evaluator（状態の評価）**: 探索の進捗をヒューリスティックに評価する。LLM自身に自己評価を行わせることで、それぞれの状態に対して1〜10などのスコアや、sure/likely/impossibleなどのカテゴリ分け（Value）を行うか、異なる状態間で多数決などの比較（Vote）を行う。
4. **Search Algorithm（探索アルゴリズム）**: 木構造を探索するために、幅優先探索（BFS）や深さ優先探索（DFS）を用いる。特にDFSでは現在の状態が目標に達し得ないと評価された場合、上位ノードへのバックトラックを行う。

## 結果
論文では、高度な探索や計画を必要とする「Game of 24（24ゲーム）」「Creative Writing（創造的文章作成）」「5x5 Mini Crosswords（クロスワードパズル）」の3つのタスクに対して検証された（Table 2）。

### タスクの概要
| | \textbf{Game of 24} | \textbf{Creative Writing} | \textbf{5x5 Crosswords} |
| :--- | :--- | :--- | :--- |
| \textbf{Input} | 4 numbers (4 9 10 13) | 4 random sentences | 10 clues (h1. presented;..) |
| \textbf{Output} | An equation to reach 24 (13-9)*(10-4)=24 | A passage of 4 paragraphs ending in the 4 sentences | 5x5 letters: SHOWN; WIRRA; AVAIL; ... |
| \textbf{Thoughts} | 3 intermediate equations (13-9=4 (left 4,4,10); 10-4=6 (left 4,6); 4*6=24) | A short writing plan (1. Introduce a book that connects...) | Words to fill in for clues: (h1. shown; v5. naled; ...) |
| \textbf{\#ToT steps} | 3 | 1 | 5-10 (variable) |
*Table 2: Task overview. Input, output, thought examples are in blue (as per original tex, represented in parenthesis here).*

### 実験結果と図解
![Tree of Thoughts Teaser Schematic](./images/teaser.png)
*(Fig: Schematic illustrating various approaches to problem solving with LLMs including IO, CoT, CoT-SC, and ToT)*

#### 1. Game of 24 の結果
Game of 24 では、4つの数字を使って四則演算で24を作る必要があるが、GPT-4の標準的なIOやCoTプロンプトでは初期の誤ったトークン予測が致命傷となり正解率が低い。
![Game of 24 ToT Diagram](./images/game24_diagram.png)
*(Fig: ToT in a Game of 24 with thought generation and valuation)*

以下の表に示す通り、IOのベスト100サンプルで33%、CoTのベスト100サンプルで49%の成功率だったのに対し、ToTは探索幅 $b=5$ だけで74%の驚異的な成功率を達成した。これは最初のリステップでの見当違いの計算をToTが可能にする事前評価によって排除できるためである。

| \textbf{Game of 24} | \textbf{Generate/Prompt tokens} | \textbf{Cost per case} | \textbf{Success} |
| :--- | :--- | :--- | :--- |
| IO (best of 100) | 1.8k / 1.0k | $0.13 | 33% |
| CoT (best of 100) | 6.7k / 2.2k | $0.47 | 49% |
| ToT | 5.5k / 1.4k | $0.74 | 74% |
*Table 6: Cost analysis on Game of 24.*

![Game of 24 Scale and Error Analysis](./images/game24_scale.png)
![Game of 24 Scale and Error Analysis](./images/game24_error.png)
*(Fig: Game of 24 scale analysis & error analysis. CoTサンプルの約60％が初手で失敗していることがわかる)*

#### 2. Creative Writing の結果
創造的な推論を要する書き込みタスクにおいては、ToTは計画を生成して最良のものを投票によって選ぶアプローチを適用した。
![Creative Writing Diagram](./images/text_diagram.png)
*(Fig: A step of deliberate search in a randomly picked Creative Writing task)*

| \textbf{Creative Writing} | \textbf{Generate/Prompt tokens} | \textbf{Cost per case} |
| :--- | :--- | :--- |
| IO | 0.9k / 0.4k | $0.06 |
| CoT | 0.9k / 0.4k | $0.07 |
| ToT | 4k / 2.9k | $0.32 |
*Table 7: Cost analysis on Creative Writing.*

![GPT-4 Coherency](./images/gpt4_coherency.png)
![Human Coherency](./images/human_coherency.png)
*(Fig: Creative Writing results. 自動評価と人間による評価の双方で、ToTを用いた文章の論理的整合性が一番高いと評価された)*

#### 3. Mini Crosswords の結果
探索空間が広く、ローカルの正解から修正・バックトラックが必要となるミニクロスワードにおいては、さらにToTの手法が重要となる。以下の表が示す通り、ToTを用いた成功率が際立って高い。

| \textbf{Method} | \multicolumn{3}{c}{\textbf{Success Rate (\%)}} |
| :--- | :--- | :--- | :--- |
| | \textbf{Letter} | \textbf{Word} | \textbf{Game} |
| IO | 38.7 | 14 | 0 |
| CoT | 40.6 | 15.6 | 1 |
| ToT (ours) | **78** | **60** | **20** |
| +best state | 82.4 | 67.5 | 35 |
| -prune | 65.4 | 41.5 | 5 |
| -backtrack | 54.6 | 20 | 5 |
*Table 3: Mini Crosswords results.*
![Crosswords Diagram](./images/crosswords_diagram.png)

### 考察
著者らは、局所的および全体的な探索と評価を組み込むことで、これまでの言語モデル推論（CoTなど）で制約となっていた直感的推論の限界を突破できたと見出している。ToTはタスクに応じた状態定義、ヒューリスティクス評価、探索アルゴリズムを変更することができる高い汎用性を備えており、LLMを単なる「生成器」から「多目的な問題解決エンジン」へと昇華させるための重要なフレームワークであると位置付けている。
