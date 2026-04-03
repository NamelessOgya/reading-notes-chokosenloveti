# TextualVerifier: Verify TextGrad Step-by-Step

## 背景
大規模言語モデル（LLMs）はゼロショット推論や数学的推論などの領域において目覚ましい成果を挙げているが、複雑な多段階推論において論理的な誤りを含むハルシネーション（幻覚）を起こしうる問題が課題となっている。これに対し、テキストベースの自動微分（Automatic Differentiation via Text）を用いてシステム全体の最適化を行う「TextGrad」という画期的なアプローチが提案されている。TextGradは自然言語フィードバックをテキストの勾配として用いることで、コーディングや推論の精度を大幅に向上させるが、それ自体には生成された推論過程の正しさを保証する「自己検証（self-verification）メカニズム」が統合されていない。
プロセスベースの報酬モデル（PRMs）など、多段階の推論結果を個別のステップ単位で検証するプロセス監視アプローチが有効であることは示されているものの、これまではTextGradによる最適化サイクルの中間ステップや最終出力を精密に検証する仕組みが存在せず、誤った推論を連鎖的に強化してしまうリスクがあった。本研究は、このTextGradの検証機能の欠如を解決するための、LLMを活用したテキストベースの検証システム「TextualVerifier」を提案したものである。

## 手法
TextualVerifierは、バックプロパゲーションのように数値的な勾配（Numerical Gradients）に依存せず、LLMを用いた推論ステップごとの監視・検証を「4段階のワークフロー」としてシステムに組み込む。

![Figure 1: TextualVerifier Architecture showing the four-stage verification workflow: (1) Chain-of-Thought Decomposition, (2) Step Breakdown and Extraction, (3) Variant Generation with Multiple Perspectives, and (4) Majority Voting and Consensus Aggregation.](./images/textualverifier_architecture.png)

1. **Step Extractor (Chain-of-Thought Decomposition & Breakdown)**
   複雑な推論を複数の離散的で論理的なステップに分解する。プロンプトによりCoTを出力させ、正規表現やフォールバックルールを用いて各ステップ（例: `<STEP>...</STEP>`）をテキストから抽出する。
2. **Verified Variant Generator (Variant Generation)**
   抽出された各推論ステップに対して、多様な視点・文脈に基づく複数の検証プロンプトを適用し、「バリアント（検証用の解釈パターンのバリエーション）」を並行生成する。
3. **Voting Mechanism (Majority Voting and Consensus Aggregation)**
   並行生成された複数のバリアントについてLLMによる多数決（Majority Voting）を行いコンセンサスを形成することで、最も確からしい推論を採用し、個別のエラーの影響を低減する。
4. **Step Merger**
   検証を通過したステップたちを `<VERIFIED>...</VERIFIED>` タグで囲んでマージし、最終的な出力フォーマットとして整える。

TextualVerifierは既存のTextGrad実装に侵襲的（Invasive）に改変を加えることなく、以下の2点で統合可能である。

![Figure 2: Integration points with TextGrad showing Loss Function Verification and Optimization Phase Verification within the TextGrad optimization workflow.](./images/integration_points_with_textgrad.png)

* **ロス関数レイヤ (Loss Function Verification)**
  TextGradがテキスト上の「Loss」を計算する際に、算出されたロスが解の質を性格に評価できているかを検証する。
  $$ \text{instance} + \text{instruction} \Rightarrow \text{loss\_value} $$
  $$ \text{instance} + \text{loss\_value} + \text{verification\_prompt} \Rightarrow \text{verified\_loss\_value} $$
* **オプティマイザレイヤ (Optimization Phase Verification)**
  TextGradによる最適化後のソリューションが、論理的正確性を保ったままロスによって指摘された問題を修正できているか確認・検証する。
  $$ (\text{initial\_solution} \land \text{loss\_value}) + \text{optimization\_instruction} \Rightarrow \text{optimized\_solution} $$
  $$ (\text{initial\_solution} \land \text{loss\_value}) + \text{optimized\_solution} + \text{verification\_prompt} \Rightarrow \text{verified\_optimized\_solution} $$

## 結果

本研究では、Gemini 1.5 Pro（コンテキスト長2M）を用いて2段階の検証実験が行われた。第一段階は「TextualVerifier単独でのPRM800Kデータセットによる検証」、第二段階は「TextualVerifierをTextGradと統合した際のベンチマーク検証（GPQA-Diamond, MMLU-ML, MMLU-CP）」である。

![Figure 3: Experiment Phase 1 High-Level Flow using PRM800K dataset.](./images/experiment_phase_1_high_view_flow.png)

### 1. TextualVerifier 単独の性能比較 (PRM800K)

| **Config** | **Accuracy** | **Proc. Time** | **LLM Calls** | **Score** |
| :--- | :--- | :--- | :--- | :--- |
| 1 variant | +1.4 pp | 66,465 ms | 18.8 | 66.3/100 |
| 2 variants | +1.4 pp | 196,098 ms | 56.4 | 63.1/100 |
| 3 variants | +2.9 pp | 227,156 ms | 75.1 | 62.2/100 |
| 4 variants | +5.7 pp | 253,620 ms | 93.9 | 57.9/100 |
| 5 variants | +0.0 pp | 327,053 ms | 112.7 | 32.9/100 |

上表（Table 1）は、生成するバリアント（検証視点）の数を1から5まで変えたときの結果である。
* すべての設定で計算は100%成功し、Stuart-Maxwell検定の結果、$p < 0.001$で統計的有意に検証後の品質向上がみられた。特に約29%のステップで評価レートの向上が確認された。
* **1 variant設定**は精度の向上（+1.4 pp）を維持しながらも実行時間およびLLMコールの面で高い効率を示し、スコアが最も高かった。
* **4 variants設定**では最も高い精度の向上（+5.7 pp）を得た。しかし、5 variantsとした場合はオーバーヘッドが膨大になるばかりか精度の向上が見られず (+0.0 pp)、冗長な過多な検証はノイズ増大や悪影響に繋がることが示唆されている。

![Figure 4: Experiment Phase 2 High-Level Flow using GPQA-Diamond, MMLU-ML, and MMLU-CP datasets.](./images/experiment_phase_2_high_view_flow.png)

### 2. TextGrad + TextualVerifier 統合結果比較

| **Method** | **Accuracy** | **Improvement** | **LLM Calls** |
| :--- | :--- | :--- | :--- |
| TextGrad-Only | 68.2% | - | 0.0 |
| TextGrad + TV (Loss) | **70.4%** | **+2.2 pp** | 5.9 |
| TextGrad + TV (Optimizer) | 65.0% | -3.2 pp | 9.6 |
| TextGrad + TV (Both) | 67.2% | -1.0 pp | 15.1 |

TextGradに統合した場合の比較（Table 2）では、実装箇所による効果の違いが明白に表れた。
* TextGradの損失関数の検証のみを行った**TextGrad + TV (Loss)**が最も高い精度（70.4%, +2.2 pp向上）を達成し、なおかつLLMコールの増加数（5.9）も抑えられている。最適化サイクルにおけるエラーの源流であるLossを検証することが、最も費用対効果が高いことが判明した。
* 逆に、オプティマイザの出力に対する検証を含めると精度が悪化（TV Optimizerでは -3.2 pp）した。これはMMLU-MLなどの分野において、検証プロセスが特定のドメインの最適化パターンと干渉（干渉や過剰修正）を引き起こす可能性が示唆された。

### 3. TextualVerifierのバージョン間の比較 (Loss)

| **Version** | **GPQA** | **MMLU-ML** | **MMLU-CP** | **Overall** |
| :--- | :--- | :--- | :--- | :--- |
| TextGrad Only | 51.01% | 76.79% | 91.18% | 67.96% |
| V1 (Basic) | +5.05 pp | -2.68 pp | +3.92 pp | +2.67 pp |
| V2 (Contextual) | +5.56 pp | +7.14 pp | +2.94 pp | **+5.34 pp** |
| V3 (Consolidated) | **+8.08 pp** | **+10.71 pp** | +0.98 pp | **+5.34 pp** |
| V4 (Simplified) | +1.01 pp | +5.35 pp | -2.94 pp | +1.21 pp |

Table 3はLossにTVを統合した場合での、アーキテクチャ設計（V1からV4）ごとの性能を比較した補足検証の結果である。
* V2（コンテキスト累積型）とV3（並列パイプライン統合型）の実装が共にベースライン比 +5.34 ppの素晴らしい改善を見せた。
* 複雑な学際的タスクであるGPQAや、機械学習の専門領域であるMMLU-MLにおいては**V3**が極めて高い精度向上効果（最大 +10.71 pp）を叩き出しており、より重層的・並行的な検証統合モデルがTextGrad本来の能力を正しく解放することを示している。
* 結論として、数値的勾配に依存しないテキストベースでも、CoTと多数決メカニズムを効果的にTextGradのLossに組み込むことで、推論の妥当性とシステムパフォーマンスを安全に引き上げられることが証明された。
