# 論文の背景

LLMなどの複数の複雑なコンポーネントを組み合わせた「Compound AI Systems」が台頭し、これらをいかにして自動的かつ原則的に最適化するかが新たな課題となっている。ニューラルネットワークの黎明期において、バックプロパゲーションと自動微分（Automatic Differentiation; AD）が最適化を極めて容易にしたことに着想を得て、テキストを通じた”自動微分”による最適化フレームワーク「TextGrad」を提案した。

# 手法

TextGradは、LLMなどのコンポーネントによる計算プロセスを計算グラフとして表現し、システム全体を言語モデル同士の対話（プロンプティング）によって最適化するフレームワークである。抽象的な数式による勾配表現と、実際のプロンプト上の操作は以下のように対応している。

### 1. 変数と順伝播（Forward Pass）
計算グラフ上のノードは「変数（Variable）」として扱われる。変数は単なるテキストの「値」だけでなく、「言語モデルのシステムプロンプト」や「関数の推論結果」といった文脈を示す**役割記述（Role description）**を保持する。順伝播では、入力プロンプトがLLMに渡され、その出力と依存関係が計算グラフに記録される。

### 2. 勾配の計算（Backward Computation）
下流タスクでの評価（Loss / Evaluation）に基づいて、テキストによる勾配（フィードバック）をバックプロパゲーションのように各コンポーネントに逆伝播（$\text{backward}(f)$）させる。
実際のシステムでは、「勾配計算エンジン（Backward Engine）」となるLLMに対し、評価関数の結果や直前の出力をタグ（`<LM_OUTPUT>`, `<OBJECTIVE_FUNCTION>`など）で囲んで提示し、以下のような制約を課したシステムプロンプトを投げる。

> *「あなたは最適化システムの勾配（フィードバック）エンジンです。目的関数に基づいて変数への建設的な批判を提供してください。決して新しい変数のバージョン（修正案そのもの）は提案せず、"どこをどう変えればよくなるか"という戦略や説明（＝勾配）のみを抽出してください。」*

### 3. 勾配の統合（Gradient Accumulation / バッチ最適化）
数式上は微分や連鎖律で記述される勾配の統合は、プロンプトの操作上では**複数のフィードバックテキストの単純な文字列結合（改行区切り）**として実装される。

$$
\frac{\partial \mathcal{L}}{\partial v} = \bigcup_{w \in \text{SuccessorsOf}(v)} \text{backward\_chain}_f\left(v, w,  \frac{\partial \mathcal{L}}{\partial w}\right)
$$

上記のように、各Successor（例えばミニバッチ最適化における複数の異なる質問や、複雑なグラフ内の複数の後続処理など）から得られた個別の批判テキストを収集し、すべて連結した巨大な `<FEEDBACK>` ブロックを生成する。これにより、複数のデータポイントから得られた**勾配蓄積（Gradient Accumulation）**が単純な言語モデルのコンテキスト結合として自然に実現され、オプティマイザは多角的で安定した批判を一度に受け取ることができる。
なお、深層学習フレームワークの `zero_grad()` と同様に、**この結合されたフィードバック文字列は「現在の1ステップ（1イテレーション）」でのみ使用され、変数の更新が終わると破棄（クリア）される**。古い批判が蓄積してコンテキスト長を圧迫したり、すでに修正済みの指摘でLLMが混乱したりするのを防ぐ仕様になっている。

### 4. オプティマイザによる変数の更新とモメンタム（Textual Gradient Descent; TGD）
結合されたテキストベースの勾配を用い、TGDオプティマイザ（別のLLM）によって新しい $v_{\text{new}}$ にアップデートされる。

$$
v_{\text{new}} = \text{TGD.step}\left(v, \frac{\partial \mathcal{L}}{\partial v}\right)
$$

オプティマイザには、特定のノードに対する `<FEEDBACK>` の束と、現在の変数が渡され、以下のように更新を指示される。

> *「あなたは最適化システムの一部です。入力されたフィードバック（ノイズを含む場合がある）を受け取り、それを使って変数（プロンプトやコード等）を改善してください。改善後の変数テキストのみを `<IMPROVED_VARIABLE>` タグで囲んで出力し、直接その部分を置き換えてください。」*

**モメンタム（慣性項）の実装と履歴の保持**
数理最適化（SGD等）におけるモメンタムは、過去の勾配の線形結合を用いることで振動を抑え更新を加速する手法である。TextGradにおいては、これを**「変数の過去の最適化履歴（遷移ログ）」**としてプロンプト上で再現している。具体的には、プロンプト末尾に `<PAST_ITERATIONS>` というタグを用いて過去の変数（テキスト）の変遷を提示する。
ここで全履歴を無限に保持するのではなく、オプティマイザ初期化時のパラメーター（例：`momentum_window = 3`）等で**「直近どれだけ前の世代（ステップ）まで保持するか」の上限を指定する**。保持上限（スライディングウィンドウ）を超えた古い履歴のテキストは自動的に捨てる仕組みになっているため、LLMに対してコンテキスト長の崩壊を起こすことなく、「過去にどのような修正を経て今の状態に至ったのか」という適度な文脈（モメンタム）だけを認識させ、局所解の停滞を避けるための高度な推論を促している。

このように、数値空間での勾配更新や高度な最適化アルゴリズム（ミニバッチ蓄積やモメンタム）を、**「多様な批判の結合（勾配の統合）」**と**「過去の履歴を考慮したリライト（モメンタム付きの変数更新）」**というLLMの自然言語処理操作に完全にマッピングした点が、本手法の最大の特徴である。

# 結果

TextGradを多様なタスク（ゼロショット推論、コード生成、分子構造最適化、放射線治療計画など）に適用し、システムプロンプトや特定のインスタンス（コード片など）の最適化において高い性能を示した。

### 図の参照と結果

![Figure 1: TextGradの全体概要](./images/figure_1.png)
**Figure 1**: TextGradは計算グラフ上の各変数に対するテキストフィードバックのバックプロパゲーションを行い、プロンプト最適化やソリューション最適化に用いることができる。

![Figure 2: 分子構造最適化](./images/molecule_design.png)
**Figure 2**: in silicoの分子結合親和性（Vinaスコアなど）をLossとして扱い、LLMが化学的知見を基に新たな低分子化合物を設計・最適化するプロセスにおいて、TextGradが有効に機能することが示されている。

![Figure 3: 放射線治療計画](./images/treatment_planning_trajectories.png)
**Figure 3**: 放射線治療計画において、腫瘍への線量を最大化しつつ危険臓器（OAR）への影響を最小化するようなハイパーパラメータ最適化にTextGradを適用した場合の軌跡。

![Fragment Plot](./images/Fragment_Plot.png)
![Novelty Plot](./images/Novelty_Plot.png)
![Molecule ADMET](./images/molecule_admet.png)
**Appendix Figures**: 分子最適化実験における、フラグメントベースの評価や新規性の推移、ADMET特性に関する結果。

![PTV](./images/ptv.png)
(※補助画像。PTVとOARに関連する図版)

### 表の参照と結果

以下に論文中で提示された全Tableを示す。

## Table 1
| **Target** | **Method** | **Mean dose [Gy]** | **Min dose [Gy]** | **Max dose [Gy]** | **$\textbf{D}_{95}$ [Gy]** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| PTV | Clinical Goal | 70.20 | $\approx70.20$ | $\approx70.20$ | 70.20 |
| PTV | Radiation Oncologist | +1.97 (0.36) | -8.88 (2.31) | +4.66 (0.82) | -0.10 (0.15) |
| PTV | TextGrad | **+0.51** (0.09) | **-8.48** (2.38) | **+3.63** (0.87) | **+0.00** (0.00) |

**Table 1の考察**: PTV（計画標的体積）への放射線量の指標。TextGradによって最適化されたプランは、人間の専門家（Radiation Oncologist）のプランよりもClinical Goalに近い（偏差が小さい）結果を示しており、高精度な治療計画の立案が可能であることを示している。

## Table 2
| **Organ** | **Method** | **Mean dose [Gy] $\downarrow$** | **$\textbf{D}_5$$\downarrow$** | **$\textbf{D}_{50}$$\downarrow$** |
| :--- | :--- | :--- | :--- | :--- |
| Rectum | Radiation Oncologist | 23.88 (6.45) | 64.26 (10.00) | 20.04 (5.50) |
| Rectum | TextGrad | **17.18** (4.2) | **58.82** (18.81) | **9.54** (0.70) |
| Bladder | Radiation Oncologist | 22.39 (5.55) | 67.81 (6.44) | 14.78 (8.42) |
| Bladder | TextGrad | **20.92** (0.79) | **65.96** (6.96) | **14.11** (3.17) |

**Table 2の考察**: OAR（危険臓器：直腸や膀胱）への放射線量を最小化するという観点でも、TextGradの最適化結果は専門家よりも低被ばく線量を達成（低いMean doseやD5, D50値）し、臓器の保護に寄与している。

## Table 3
| **Task** | **Method** | **Completion Rate** |
| :--- | :--- | :--- |
| LeetCode Hard | Zero-shot | $0.26$ |
| LeetCode Hard | Reflexion (1 demonstration, 5 iterations) | $0.31 \pm 0.012$ |
| LeetCode Hard | TextGrad (0 demonstrations, 5 iterations) | $\mathbf{0.36} \pm 0.018$ |

**Table 3の考察**: LeetCode Hard問題のコード作成タスクにおいて、デモンストレーションなしのTextGradがReflexionを上回る成功率（36%）を達成しており、コードの挙動を直接最適化することの強力さが分かる。

## Table 4
| **Dataset** | **Method** | **Accuracy ($\%$)** |
| :--- | :--- | :--- |
| Google-proof QA | CoT | $51.0$ |
| Google-proof QA | Best reported | $53.6$ |
| Google-proof QA | TextGrad | $\mathbf{55.0}$ |
| MMLU-Machine Learning | CoT | $85.7$ |
| MMLU-Machine Learning | TextGrad | $\mathbf{88.4}$ |
| MMLU-College Physics | CoT | $91.2$ |
| MMLU-College Physics | TextGrad | $\mathbf{95.1}$ |

**Table 4の考察**: 複数のQAタスクにおけるゼロショットでの解法最適化において、既存手法を上回る最高精度を記録した。GPT-4oを用いたTextGradによって、Google-proof QAのような高度な問題でも性能向上が図れる。

## Table 5
| **Dataset** | **Method** | **Accuracy ($\%$)** |
| :--- | :--- | :--- |
| Object Counting | CoT (0-shot) | $77.8$ |
| Object Counting | DSPy (BFSR, 8 demonstrations) | $84.9$ |
| Object Counting | TextGrad (instruction-only, 0 demonstrations) | $\mathbf{91.9}$ |
| Word Sorting | CoT (0-shot) | $76.7$ |
| Word Sorting | DSPy (BFSR, 8 demonstrations) | $\mathbf{79.8}$ |
| Word Sorting | TextGrad (instruction-only, 0 demonstrations) | $\mathbf{79.8}$ |
| GSM8k | CoT (0-shot) | $72.9$ |
| GSM8k | DSPy (BFSR, 8 demonstrations) | $\mathbf{81.1}$ |
| GSM8k | TextGrad (instruction-only, 0 demonstrations) | $\mathbf{81.1}$ |

**Table 5の考察**: プロンプト自体の最適化タスクにおいても、複数デモンストレーションを利用したDSPyと同等以上の精度を「命令のみ（デモなし）」で達成しており、システムプロンプトの更新が高レベルに行われていることが示唆された。
全体として、TextGradの抽象化が分野を問わず広く有効であり、手計算によるチューニングなしで即座に適用できる汎用性の高さが実証された。

# chokosenlovetiの考察

## 新規性

本論文の最大の新規性は、自然言語によるフィードバックを用いた最適化を、単一のプロンプト改善にとどまらず、**「複雑なCompound AI Systems（複合AIシステム）全体に対する、連鎖律（Chain Rule）を伴う強固な自動微分・バックプロパゲーションのフレームワーク」として数学的かつ実装レベルで定式化した点**にある。

特に、テキスト勾配（Textual Gradients）を用いた最適化の先駆である **ProTeGi** と比較した場合、以下の明確な差分と概念的な進化が存在する。

1. **最適化対象の汎化（プロンプトから計算グラフのあらゆる変数へ）**
   ProTeGiはあくまで「プロンプトエンジニアリングの自動化（Automatic Prompt Optimization）」を目的とした手法であり、最適化対象はシステム入力としてのプロンプト文に限られていた。対してTextGradは、システム内のあらゆるテキスト出力を「計算グラフ上の変数」として扱う。これにより、言語モデルへのプロンプトだけでなく、生成されたコードのロジック、分子構造の文字列表現、果ては放射線治療計画のハイパーパラメータまで、全く異なるドメインの変数最適化を単一の「テキスト勾配」で実行可能にしている。

2. **連鎖律（Backpropagation）による多段コンポーネントの最適化**
   ProTeGiの最適化範囲は、実質的に「プロンプト入力 $\to$ LLM出力」という1ステップの操作に対するローカルなエラー探索（エラーから修正案を出すプロセス）であった。一方のTextGradは、微分の連鎖律（Chain Rule）をテキスト操作（LLMによるフィードバック生成）にマッピングしている。これにより、あるコンポーネントAの出力がコンポーネントBの入力となるといった多段の推論パイプライン（DAG）において、最終ステップのLoss（批判）を、ステップBを通してステップAまで「逆伝播」させ、遠く離れた上流の変数に対して正確にフィードバック（勾配）を届けることを可能にした。

3. **探索アルゴリズムのPyTorch的抽象化とエコシステムの確立**
   ProTeGiがビーム探索やバンディットアルゴリズムを用いて有望なプロンプトをヒューリスティックに探索・選択していたのに対し、TextGradは `Textual Gradient Descent (TGD)` という形で、深層学習における最適化器（Optimizer）の概念を完全に輸入している。勾配の蓄積（複数の質問からのフィードバックを結合するミニバッチ最適化）やモメンタムといった標準的な最適化技術をプロンプト表現上で透過的に実装し、「LLMを用いたシステム構築自体を、PyTorchでのニューラルネットワーク構築と同じ設計パラダイムに引き上げた」点が、後続研究に対し極めて大きなパラダイムシフトを生んでいる。
