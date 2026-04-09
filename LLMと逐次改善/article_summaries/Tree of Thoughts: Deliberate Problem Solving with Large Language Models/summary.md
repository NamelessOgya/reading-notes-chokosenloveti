# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

## 背景
大語彙言語モデル（LLMs）は一般的な問題解決において目覚ましい成果を挙げているが、従来の推論プロセスはトークンレベルでの左から右への自己回帰的な生成（直感的な「System 1」モード）に依存している。これにより、探索や戦略的な先読みが必要な問題、あるいは初期の決定が後続の選択肢を大きく制限するような問題（数学的パズル、クロスワード等）では正答を導き出せないという課題があった。これに対し、人間の認知プロセスに見られる「System 2」のような、より意識的で意図的な計画プロセス（複数の選択肢を探索し、状態を自己評価しながら先増やバックトラックを行うプロセス）をLLMに組み込むため、本研究では新たな推論フレームワーク「Tree of Thoughts（ToT）」を考案。

## 手法
ToT（Tree of Thoughts）は、従来の手法（Input-OutputプロンプティングやChain-of-Thoughtプロンプティング）を拡張し、問題解決に向けた中間ステップとしての論理的な思考単位（「thought」）の木構造を構築・探索するフレームワークである。
これにより、LLMは「次に何を考えるか」を多角的に検討し、行き詰まった際には前の状態に戻る（バックトラック）など、人間の「System 2」（熟慮的思考）に近い推論プロセスが可能となる。

ToTの具体的な実装は、以下の4つの主要なコンポーネントに分解されて定式化される。

### 1. Thought Decomposition（思考の分解・定義）
最初のステップは、対象となる問題に対し、LLMにとって解決しやすい「意味のある中間ステップ（thought）」をどう定義するかである。
- **柔軟な単位**: タスクの性質に応じて、数語からなる句（クロスワードの単語）、1行の数式（24ゲームの中間計算）、または全体計画の段落（文章作成のプロット）など様々な粒度で定義される。
- **重要性**: 各thoughtは、LLMが「論理的かつ一貫した次のパス」を単独で生成できる程度に小さく、かつ問題全体の解決に向けて十分な進捗が測れる程度にまとまっている必要がある。  
  
思考を分割するのは人間が行う。  

### 2. Thought Generator（思考の生成）
現在の状態 $s = [x, z_{1\cdots i}]$（入力とこれまでの推論の歴史）が与えられたとき、$k$ 個の「次の考え（候補）」を生成する。主に以下の2つの戦略が用いられる。
- **Sample（独立サンプリング）**: 同じプロンプトを用いてLLMから独立に複数の候補をサンプリングする手法。思考空間が広く、多様なアイデアが必要なタスク（例：Creative Writing）に適している。
- **Propose（連続的提案）**: 「考えられる候補をまとめて提案せよ」というプロンプトを使用し、相互に重複しないような候補を一度に生成させる手法。思考のステップが限定的で、互いに排他的な候補を得たい場合（例：Game of 24の次の一手）に適している。

### 3. State Evaluator（状態の評価）
様々な経路（木構造）を探索する上で、各状態が目標達成に向けてどれほど有望かを評価する「ヒューリスティック機能」をLLM自身に担わせる。**どの枝が有望（最適）かはAI（LLM）自身の判断で決めるが、この評価用AI自体（モデルの重み）は本手法の中で最適化（学習）されない。** 事前の学習済みの専用評価モデル等を用いるのではなく、汎用的なゼロショット・フューショットプロンプティングのみによって評価を行う点が特徴である。
- **Value（状態の絶対評価）**: 各状態について独立にプロンプトを与え、LLMにその有望さを評価させる。例えば1〜10のスコア付けや、確実（sure）/可能性あり（likely）/不可能（impossible）といったカテゴリへの分類を行う。探索の打ち切り（枝刈り）の判断に利用される。
- **Vote（状態の相対評価）**: 複数の異なる状態（候補）をLLMに比較させ、最も有望なものに投票させる。文章の評価のように、明確なスコア付けが難しく、相対的な「良さ」を比較で測るのが効果的なタスク（例：Creative Writing）で利用される。

### 4. Search Algorithm（探索アルゴリズム）
生成されたthoughtと、State Evaluatorによる評価を活用し、問題解決に向けた木構造を系統的に探索する。**AIの学習データセット全体に対する探索ではなく、「1つの問題に対して推論を行う都度」、この木の探索を行なって最適な思考パスを選ぶ** 推論時のアルゴリズムである。
- **幅優先探索（BFS, Breadth-First Search）**: 探索の深さが比較的浅く、限られたステップ数で完了する問題（例：Game of 24やCreative Writing）に有用。各ステップで評価の上位 $b$ 個の候補だけを残す（ビームサーチ的なアプローチ）ことで探索空間の爆発を抑える。
- **深さ優先探索（DFS, Depth-First Search）**: 探索空間が広大で、試行錯誤と修正が必要な問題（例：Mini Crosswords）に適している。最も有望な経路を深く掘り下げ、Evaluatorが「不可能（impossible）」と判定した場合は、その経路を破棄（枝刈り）し、親ノードへバックトラックして別のパスを模索する。

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

## chokosenlovetiの考察

### 新規性
本手法の最大の新規性は、LLMの推論プロセスを「トークンレベルの一直線なテキスト生成」から「状態空間上の経路探索問題」へとフレームワーク化した点にある。
従来のCoT（Chain of Thought）等が「やり直しの効かない一本道の思考（System 1）」であったのに対し、ToTは思考を意味のある単位（Thought）で区切り、LLM自身による自己評価をヒューリスティクスとして用いることで、古典的な探索アルゴリズム（BFS/DFSなど）をLLM推論に導入した。これにより、「複数案を同時に天秤にかける」「行き詰まったら前段に戻って考え直す（バックトラック）」といった、人間の熟慮的思考（System 2）に迫る動的な推論を、モデルの追加学習なし（プロンプティングのみ）で実現した。

### 評価機の改善
ToTは、LLMを推論時の探索アルゴリズムの部品として組み込む。しかし、本手法の枠組みにおいて着目すべき点は、「どの枝が最適かはAIが決めるが、その評価機（Evaluator）自体は改善・最適化の対象外となっている」ということである。
探索パスが正しいかどうかは完全にベースとなるLLMの自己評価精度（直感的な見立て等）に依存しており、LLMが評価を誤れば探索はそのまま見当違いの方向へ進んでしまう。
