# summary

## 背景
大規模言語モデル（LLMs）は、目標駆動型エージェントとして外部環境（ゲーム、コンパイラ、APIなど）と対話するためにますます利用されるようになっています。しかし、従来の強化学習の手法では膨大な訓練サンプルや高コストなモデルの微調整が必要となるため、これらの言語エージェントが試行錯誤から迅速かつ効率的に学習することは依然として困難でした。この問題を解消するため、著者は重み（パラメータ）の更新ではなく「言語的フィードバック（Verbal Reinforcement）」を通じて言語エージェントを強化する新しいフレームワーク「**Reflexion**」を提案しました。この手法では、エージェントが環境からのタスクのフィードバックに基づいて言葉で「内省（Reflection）」し、その内省テキストをエピソード記憶バッファに保持して、その後の試行でより良い意思決定を促します。

## 手法
Reflexionは、生成と行動を担う**Actor（ $M_{a}$ ）**、生成された軌跡を評価する**Evaluator（ $M_{e}$ ）**、そして未来の試行に役立つ内省テキストを生成する**Self-Reflectionモデル（ $M_{sr}$ ）**の3つの独立したモジュールで構成されています。

1. **Actor**: 状態の観測結果や自身の持つメモリ（短期・長期）に基づいてテキストと行動を生成するLLMベースのエージェントです。
2. **Evaluator**: タスク環境などでActorの出力結果を評価し、報酬スコア（推論タスクでの完全一致に基づくバイナリ評価や、事前定義されたヒューリスティック評価など）を計算します。
3. **Self-Reflection**: Evaluatorからのスパースな報酬シグナルと現在の軌跡、およびメモリの内容に基づき、言語による具体的なフィードバック（行動計画への反省と改善案など）を生成します。

Actorのポリシー $\pi_{\theta}(a_{i} | s_{i})$ はモデルパラメータとメモリの両方を用いた $\theta = \{M_{a}, mem\}$ としてモデル化されます。
1回の試行で軌跡 $\tau_{t}$ と報酬 $r_{t}$ を得たのち、Self-Reflectionモデルがそれを言語サマリー $sr_{t}$ に増幅させ、長期記憶バッファ $mem$ に保存します。この一連の言語的な反省ループをタスクが成功するか最大試行回数に到達するまで繰り返します。

## 結果

### Table 1: 推論、意思決定、プログラミングに関する関連研究とReflexionの比較

| Approach | Self refine | Hidden constraints | Decision making | Binary reward | Memory |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Self-refine | ✔ | ✖ | ✖ | ✖ | ✖ |
| Beam search | ✔ | ✔ | ✔ | ✔ | ✖ |
| **Reflexion (ours)** | ✔ | ✔ | ✔ | ✔ | ✔ |

| Approach | Test execution | Debugging execution | Self-generated tests | Multiple languages | Self-reflection |
| :--- | :---: | :---: | :---: | :---: | :---: |
| AlphaCode | ✔ | ✖ | ✖ | ✔ | ✖ |
| CodeT | ✔ | ✖ | ✔ | ✖ | ✖ |
| Self-debugging | ✔ | ✔ | ✖ | ✖ | ✖ |
| CodeRL | ✔ | ✔ | ✖ | ✖ | ✖ |
| **Reflexion (ours)** | ✔ | ✔ | ✔ | ✔ | ✔ |

**考察 (Table 1)**:  
既存の推論・意思決定手法（Self-refineなど）やプログラミング手法（AlphaCode, CodeRLなど）と比較して、Reflexionは広範なタスク（意思決定、コード生成など）に対応しながら、多言語に対応し、かつエピソードを通して継続する「自己内省の記憶（Memory / Self-reflection）」を明示的に使用するという独自の拡張性を持っています。

### Figure 1, 2: フレームワークの概要とアーキテクチャ

*図: Reflexionは意思決定、プログラミング、推論タスクにおいて機能する (Figure 1)*
![Figure 1](./images/reflexion_tasks.png)

*図: Reflexionのブロック図ならびに強化学習のアルゴリズム (Figure 2)*
![Figure 2](./images/reflexion_rl.png)

**考察 (Figure 1, 2)**:  
Reflexionのループを通じ、各試行における過ちがテキストとして言語化され、それが次の試行に繋がることで徐々に軌跡が修正されていく様子がプロンプトを通じて確認できます。これにより勾配の更新を伴わない新たなパラダイムとしての自己最適化タスクが実現します。

---

### Figure 3: 意思決定タスク（AlfWorld）における性能推移と失敗例の分析

*図: AlfWorldでの成功タスク数の累積推移 (Figure 3a)*
![Figure 3a](./images/alfworld_success.png)

*図: AlfWorldの軌跡の失敗理由に基づく分類 (Figure 3b)*
![Figure 3b](./images/alfworld_failure.png)

**考察 (AlfWorld / Figure 3)**:  
AlfWorldを用いた環境探索と順次意思決定課題において、既存のReActベースラインと比較し Reflexion + ReAct アプローチは134タスク中130タスクのクリアに成功し、絶対精度で22%もの改善を示しました。学習曲線（Figure 3a）は試行を重ねるごとに右肩上がりに成長しており、徐々に反省と探索技術が向上していることを示しています。また、Figure 3bから分かるように、既存では「誤ったアイテムの保持認識」といった失敗からのリカバリーができませんでしたが、Reflexionの軌跡においてはそのようなハルシネーション要因がほぼ排除され、長期的な戦略修正が成功しています。

---

### Figure 4: 推論タスク（HotPotQA）における性能比較

*図: HotPotQAの課題における各アプローチの比較：Reflexionを用いた方が大幅に向上 (Figure 4a, b, c)*
![Figure 4a](./images/hotpotqa_success.png)
![Figure 4b](./images/hotpotqa_cot_gt.png)
![Figure 4c](./images/hotpotqa_ablation.png)

**考察 (HotPotQA / Figure 4)**:  
HotPotQAの推論的探索タスクにおいて、CoTならびにReActといった手法とReflexionを組み合わせた結果を比較しています。Reflexionを導入することで、ベースラインから絶対精度で20%の大幅な向上が確認されました。さらにアブレーション実験（Figure 4c）において「過去の軌跡をそのままメモリに入れる（Episodic Memory）」だけよりも「自己内省の言語化（Self-reflection）」を含めた方が明らかに性能向上の寄与度が高い（約8%差）ことが示されており、単純なリトライによる改善ではなく、失敗への言語的フィードバックが強化学習のフックとして極めて有効に作用しています。

---

### プログラミング用ベンチマークにおけるテスト結果 (Table 2 ~ 6)

#### Table 2

| Benchmark + Language | Prev SOTA Pass@1 | SOTA Pass@1 | Reflexion Pass@1 |
| :--- | :--- | :--- | :--- |
| HumanEval (PY) | 65.8 (CodeT + GPT-3.5) | 80.1 (GPT-4) | **91.0** |
| HumanEval (RS) | -- | 60.0 (GPT-4) | **68.0** |
| MBPP (PY) | 67.7 (CodeT + Codex) | **80.1** (GPT-4) | 77.1 |
| MBPP (RS) | -- | 70.9 (GPT-4) | **75.4** |
| Leetcode Hard (PY) | -- | 7.5 (GPT-4) | **15.0** |

**考察 (Table 2)**:  
Reflexionはコード生成プログラミングにおいても顕著な結果をもたらしました。当時の最先端（SOTA）であるGPT-4と比較し、HumanEval (Python)にてPass@1精度を80.1%から91.0%に飛躍させています。MBPP Pythonを除く全てのベンチマークでSOTAを達成しており、難易度の高いLeetcode Hardでも精度を2倍に高めています。

#### Table 3: 詳細なテストパス精度

| Benchmark + Language | Base | Reflexion | TP | FN | FP | TN |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| HumanEval (PY) | 0.80 | **0.91** | 0.99 | 0.40 | 0.01 | 0.60 |
| MBPP (PY) | **0.80** | 0.77 | 0.84 | 0.59 | 0.16 | 0.41 |
| HumanEval (RS) | 0.60 | **0.68** | 0.87 | 0.37 | 0.13 | 0.63 |
| MBPP (RS) | 0.71 | **0.75** | 0.84 | 0.51 | 0.16 | 0.49 |

**考察 (Table 3)**:  
MBPP PythonにおいてベースラインがReflexionをわずかに上回った理由を詳細に分析するための混同行列です。Reflexionによる自動コード修正は「生成したユニットテストの質」に依存し、MBPP PythonではFP（テストはパスするが実装は間違っている、つまりテスト自体が不完全なケース）の割合が16.3%と高く、偽陽性により学習ループが早々に成功を誤認してしまう問題が示唆されています。一方、テスト品質の高いHumanEvalではFPが1.4%にとどまり、全体の高いパフォーマンスに貢献しています。

#### Table 4: アブレーション検証（HumanEval Rust / GPT-4）

| Approach | Test Generation | Self-reflection | Pass@1 (Acc) |
| :--- | :--- | :--- | :--- |
| Base model | False | False | 0.60 |
| Test generation omission | False | True | 0.52 |
| Self-reflection omission | True | False | 0.60 |
| **Reflexion** | True | True | **0.68** |

**考察 (Table 4)**:  
自己生成テスト（Test generation）と自己内省（Self-reflection）の個別寄与度を調べるためのアブレーション実験です。自己内省のみ行いテストがない（精度52%）場合や、テストのみで内省がない（精度60%）場合ではベースラインのパフォーマンスを超えることはできず、両者が相互に連携することで初めて高いパス成功率（68%）を導き出せることを実証しています。

#### Table 5: 異なるベースモデル (starchat-beta) を使用した精度

| Approach | Pass@1 accuracy (avg over 8 trials) | Pass@1 accuracy (std) |
| :--- | :--- | :--- |
| Baseline | 0.26 | 0.00481 |
| Reflexion | 0.26 | 0.00305 |

**考察 (Table 5)**:  
Starchat-betaをベースモデルにした実験。強力なLLM（GPT-4等）では内省による向上効果が得られますが、中規模モデルなど自己評価能力や内省の生成能力が十分ではないモデルではこのループ技術が機能しにくい可能性が暗示されています。

#### Table 6: HotPotQA における多様なモデルでの精度比較

| Model | Baseline accuracy | Reflexion accuracy |
| :--- | :--- | :--- |
| CoT (GT) + text-davinci-003 | 0.60 | **0.77** |
| CoT (GT) + gpt-3.5-turbo | 0.57 | **0.71** |
| CoT (GT) + gpt-4 | 0.68 | **0.80** |
| ReAct + text-davinci-003 | 0.30 | **0.55** |
| ReAct + gpt-3.5-turbo | 0.26 | **0.38** |
| ReAct + gpt-4 | 0.39 | **0.51** |

**考察 (Table 6)**:  
HotPotQAにおいて、text-davinci-003, gpt-3.5-turbo, gpt-4 といった異なるLLMをバックエンドに用いた際の精度の変化です。いずれのモデルでもReflexionを加えることでBaselineから明らかな成績向上が見られることから、一定以上の基盤能力を備えるモデルに対して一貫して汎用性の高いアプローチであることが確認されました。
