# Reflection-Enhanced Meta-Optimization: Integrating TextGrad-style Prompt Optimization with Memory-Driven Self-Evolution

## 背景
TextGradのようなテキストベースの擬似勾配を用いたプロンプト最適化手法は、効果的でありながらLLMのパラメータ更新を必要としないという利点がある。しかし、多くの場合ステートレス（状態を持たない）であり、セッション間やタスク間で最適化の経験を蓄積・再利用する仕組みが存在しない。また、局所的な最適化に偏るため、トレーニングデータや初期プロンプトの特異な性質に対して過学習（Overfitting）を引き起こしやすく、未知のデータに対する汎化性能が極端に低下するという課題がある。本研究では、自己進化型のエージェントやRAG、Reflectionの考え方から着想を得て、局所的なプロンプトのチューニングと、長期的・大局的な最適化戦略を組み合わせた「Reflection-Enhanced Meta-Optimization (REMO)」を提案している。

## 手法
REMOは、以下の4つのステージを通じて、RAG、メモリ、およびTextGradスタイルの最適化を統合した自己進化型のフレームワークである。

1. **検索拡張推論（Retrieval-Augmented Reasoning）**
入力 $x$ に対して、メモリ $M_{t}$ から関連するコンテキスト $E$ を検索により取得する。現在のシステムプロンプト $P_{t}$ と組み合わせて、推論トレース $r$ と予測値 $\hat{y}$ を生成する。

$$
\hat{y} = f(x; P_{t}, E), \quad E \sim \mathrm{Retrieve}(M_{t}, x)
$$

2. **メモリの即時修正（Immediate Correction）**
予測値 $\hat{y}$ が正解ラベル $y$ と異なる場合、「間違い・ミスのノートブック」として機能する構造化されたレコードを即座にメモリに挿入・更新する。これにより更新された知識が以降の検索ですぐに利用可能となる。

$$
r = \{ x, y, \hat{y}, \mathrm{trace}, \mathrm{timestamp}, \mathrm{meta} \}
$$

3. **バッチレベルのオプティマイザプロンプト更新（Batch-level Optimizer Prompt Update）**
各ミニバッチ・エポックの終了時に、過去のフィードバックを要約した $R_{t}$ を用いて、システム全体を大局的に俯瞰して最適化方向を決定するオプティマイザプロンプト $Q_{t}$ を更新する（メタ最適化）。全体目標は以下の数式で定義される。

$$
\max_{Q_{1:T}} \; \mathbb{E}_{(x,y)\sim D_{\mathrm{val}}} \big[ \mathbf{1}[f(x; P_{T}, M_{T}) = y] \big]
$$

上記は、以下のメモリとオプティマイザのダイナミクスに制約されて更新される。

$$
M_{t} \leftarrow \mathrm{UpdateMemory}(M_{t-1}, r_{t})
$$

$$
Q_{t} \leftarrow \mathrm{OptimizerUpdate}(Q_{t-1}, R_{t})
$$

4. **TextGradを経由したシステムプロンプト最適化（System Prompt Optimization via TextGrad）**
得られた偽勾配（pseudo-gradient） $g$ とオプティマイザプロンプト $Q_{t}$ の誘導に基づき、推論などに用いるシステムプロンプト $P$ を更新する。

$$
P_{t+1} \leftarrow \mathrm{UpdatePrompt}(P_{t}, g; Q_{t})
$$

## 結果
Qwen3-32Bを用いた数学的推論タスク（GSM8K）を用いた定量的評価の結果を Table 1 にまとめる。なお論文内にFigureは存在しない。

### Table 1: Comparison on GSM8K
| Method | Epochs | Train Size | Val Acc (%) | Test Acc (%) |
| :--- | :---: | :---: | :---: | :---: |
| TextGrad (100 samples) | 3 | 1000 | 96.0 | 69.0 |
| RAG+Optimizer (100 samples) | 3 | 1000 | 89.0 | 94.0 |
| TextGrad (full data) | 3 | 6973 | 91.0 | 62.0 |
| TextGrad (full data) | 5 | 6973 | 90.0 | 63.0 |
| Reflection RAG (full) | 3 | 6973 | 90.3 | 89.0 |
| Reflection RAG (full) | 5 | 6973 | 90.0 | 89.8 |
| Adaptive Optimizer (full) | 3 | 6973 | 90.1 | 90.0 |
| Adaptive Optimizer (full) | 5 | 6973 | 90.3 | 93.2 |
| RAG+Optimizer (full) | 3 | 6973 | 90.1 | 90.1 |
| RAG+Optimizer (full) | 5 | 6973 | 90.3 | 90.5 |

### 考察
Table 1の結果から、従来手法である TextGrad（ベースライン）はTrain SizeやEpoch数を増やしても、ValidationとTestでのAccuracyのギャップが最大で約29%も生じており、特定のサンプルに強く過学習（Overfitting）していることが確認できる。
一方で、著者らが提案する **Adaptive Optimizer** や **RAG+Optimizer** （REMOフル構成）の枠組みを適用した結果、Test Accはおおむね90%台に落ち着き、Validation Accとのギャップを最小限に安定化させることに成功している。
特に、Adaptive Optimizerを単独で用いた場合は5Epoch目でピークの93.2%に達している。RAGモジュールとOptimizerを統合した場合（RAG+Optimizer）は、Test Accが90.5%とピーク性能としてはやや下がるものの、局所的な即時補正（RAGによる過去のミスの検索）と大局的なメタ認知戦略（Optimizer）を組み合わせることで、極端な過学習を防ぎつつ未知のテストセットに対し一貫性と堅牢性のある最適化プロセスを実現できていると考察されている。
