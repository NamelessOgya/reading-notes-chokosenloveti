# Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization

## 背景
大規模言語モデル（LLM）を用いたシステムの最適化において、プロンプトエンジニアリングやハイパーパラメータ調整を自動化する手法が注目されている。既存の自動化手法として、LLMによる自然言語フィードバックを勾配（Textual Gradient）に見立てて更新を行う手法（代表例：TextGrad）が存在する。
しかし、TextGradなどの手法は直近の出力フィードバックのみに依存する**一階微分（First-order gradient）**に相当する更新を行うため、微小な修正の繰り返しや一時的な変動に影響されやすく、最適化が停滞したり局所解に陥る（Local optimaに直面する）課題を抱えていた。
本論文では、目先のフィードバックだけでなく「応答が反復を通じてどのように進化（変化）したか（Response Evolution）」の履歴を追跡・考慮することで、実質的に**二階微分（Hessian matrix）的な挙動をシミュレートする最適化フレームワーク「REVOLVE」**を提案した。

## 手法
提案手法「REVOLVE」は、TextGradの最適化プロセス（Forward Pass $\rightarrow$ 評価者LLMによるLanguage Lossの計算 $\rightarrow$ Backward Passでの更新）を拡張した手法である。
TextGradにおけるプロンプト $p_t$ の更新は以下のように自然言語のフィードバックに基づいて定義されている。

$$ \nabla{\mathcal{L}}\big(r(p_{t})\big) = \dfrac{\tilde{\partial} \mathcal{L}\big(r(p_{t})\big)}{\tilde{\partial} p_t} $$

REVOLVEでは、過去の応答履歴に伴う進歩の度合いを測る**類似度関数（Similarity function）** $\mathcal{S}\big(r(p_t), r(p_{t-1})\big)$ を導入し、直前の応答から今回の応答への変化率を評価する。この $\mathcal{S}$ をTextGradの更新式のアドオンとして組み込むことで、以下の新しいテキスト勾配（REVOLVE）を算出する。

$$ \textnormal{REVOLVE}\Big(\mathcal{L}\big(r(p_{t})\big)\Big) = \dfrac{\tilde{\partial} \mathcal{L}\big(r(p_{t})\big) +  \mathcal{S}\big(r(p_t), r(p_{t-1})\big)}{\tilde{\partial} p_t} $$

ここで、$\mathcal{S}$ は連続する応答や損失の間の差分ノルム $\dfrac{\Vert\mathcal{L}\big(r(p_{t})\big) - \mathcal{L}\big(r(p_{t-1})\big)\Vert}{\Vert p_t - p_{t-1}\Vert}$ のように定式化され、微小な変化を仮定すると以下のように二階微分近似として機能する。

$$ \textnormal{REVOLVE}\Big(\mathcal{L}\big(r(p_{t})\big)\Big) = \dfrac{\tilde{\partial} \mathcal{L}\big(r(p_{t})\big)}{\tilde{\partial} p_t} + \dfrac{\tilde{\partial}^2 \mathcal{L}\big(r(p_{t})\big)}{\tilde{\partial} {p_t}^2} $$

このように、REVOLVEは明示的な数値のHessian行列を計算するのではなく、**履歴からの変化量をLLMに解析させることで二次最適化のダイナミクスをテキスト最適化の枠組みの中でシミュレートする**。これにより、停滞や振動を抑えた安定かつ着実な進展を実現する。

## 結果
REVOLVEの有効性を検証するため、「Reasoningのためのプロンプト最適化」「Solution（解答）最適化」「コード最適化」の3つのタスクにおいて評価を実施した。

![Method overview and concepts](./images/method_comparison.png)

### 1. プロンプト最適化（Prompt Optimization）
推論タスク（Object CountingおよびGSM8K）においてプロンプトを最適化した結果（Table 1）。REVOLVEは多数のLLMでTextGradを大きく上回り、より効果的な推論を引き出す最適化に成功している。

| Dataset | Models | Accuracy \% (Improv. over TextGrad) CoT | Accuracy \% (Improv. over TextGrad) TextGrad | Accuracy \% (Improv. over TextGrad) M-TextGrad | Accuracy \% (Improv. over TextGrad) REVOLVE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Object Counting | GPT-3.5 | 77.8 (15.3%↓) | 91.9 (-) | 92.1 (0.2%↑) | **95.5 ± 0.9% (3.9%↑)** |
| | GPT-4 | 92.1 (2.2%↓) | 94.2 (-) | 90.0 (4.5%↓) | **96.3 ± 0.6% (2.2%↑)** |
| | Gemini 1.5 Pro | 94.0 (0.0%) | 94.0 (-) | 94.0 (0.0%) | 94.0 ± 0.0% (0.0%) |
| | Llama 3.1 8B Instruct | 65.0 (15.6%↓) | 77.0 (-) | 80.0 (3.9%↑) | **83.0 ± 1.4% (7.8%↑)** |
| GSM8k | GPT-3.5 | 72.9 (9.9%↓) | 80.9 (-) | 82.1 (1.5%↑) | **85.9 ± 0.6% (6.2%↑)** |
| | GPT-4 | 92.6 (0.4%↓) | 93.0 (-) | 93.9 (1.0%↑) | **94.5 ± 0.4% (1.6%↑)** |
| | Gemini 1.5 Pro | 92.9 (0.4%↓) | 93.3 (-) | **93.9 (0.6%↑)** | 93.0 ± 0.3% (0.3%↓) |
| | Llama 3.1 8B Instruct | 84.6 (0.0%) | 84.6 (-) | 84.6 (0.0%) | 84.6 ± 0.0% (0.0%) |

※ 筆者の考察：GSM8KタスクにおけるLlama 3.1環境では全手法の性能が頭打ちと推測されるが、比較的安価なモデル（GPT-3.5）を高性能モデル（GPT-4o）の評価フィードバックで最適化することで、日々の推論コストを抑えながら大きな初期性能向上が得られる（費用対効果の高さ）ことが実証された。

### 2. ソリューション最適化（Solution Optimization）
GPQAやMMLUといった高難度タスクでのTest-timeソリューション最適化結果。
以下の Figure 1a, 1b, 1c はそれぞれのタスクにおけるAccuracy（≒Loss曲線の代用）の推移推移を示している。

![GPQA Loss Curve](./images/GPQA.png)

![MMLU-ML Loss Curve](./images/MMLU-ML.png)

![MMLU-CP Loss Curve](./images/MMLU-CP.png)

各LLMを用いた詳細なイテレーションごとの結果は Table 4 の通りであり、REVOLVEがすべてにおいて最高性能を達成している。

| Dataset | Models | Stage | Accuracy \% (Improv. over TextGrad) CoT | Accuracy \% (Improv. over TextGrad) TextGrad | Accuracy \% (Improv. over TextGrad) M-TextGrad | Accuracy \% (Improv. over TextGrad) REVOLVE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Google-proof QA | GPT-4o | Before Training | 50.4 (0.0%) | 50.4 (-) | 50.4 (0.0%) | 50.4 (0.0%) |
| | | 1st Iteration | - | 50.4 (-) | **51.1 (1.3%↑)** | 50.9 ± 0.4% (0.99%↑) |
| | | 2nd Iteration | - | 50.5 (-) | 50.7 (0.4%↑) | **51.3 ± 0.5% (1.58%↑)** |
| | | 3rd Iteration | - | 50.5 (-) | 51.9 (2.7%↑) | **52.9 ± 0.6% (4.75%↑)** |
| | | Final Results | 50.4 (2.1%↓) | 51.5 (-) | 52.4 (1.7%↑) | **53.0 ± 0.7% (2.91%↑)** |
| | GPT-4-0125-preview | Before Training | 38.8 (0.0%) | 38.8 (-) | 38.8 (0.0%) | 38.8 (0.0%) |
| | | 1st Iteration | - | 38.5 (-) | 39.3 (2.0%↑) | **39.5 ± 0.3% (2.60%↑)** |
| | | 2nd Iteration | - | 38.3 (-) | 40.1 (4.7%↑) | **40.3 ± 0.5% (5.22%↑)** |
| | | 3rd Iteration | - | 38.2 (-) | 40.4 (5.7%↑) | **41.0 ± 0.4% (7.33%↑)** |
| | | Final Results | 38.8 (1.8%↑) | 38.1 (-) | 41.5 (8.9%↑) | **42.2 ± 0.6% (10.76%↑)** |
| | Llama 3.1 8B Instruct| Before Training | 21.7 (0.0%) | 21.7 (-) | 21.7 (0.0%) | 21.7 (0.0%) |
| | | 1st Iteration | - | 25.8 (-) | 26.5 (2.7%↑) | **26.8 ± 0.2% (3.88%↑)** |
| | | 2nd Iteration | - | 26.8 (-) | 29.3 (9.3%↑) | **29.8 ± 0.5% (11.19%↑)** |
| | | 3rd Iteration | - | 24.8 (-) | 25.7 (3.6%↑) | **27.8 ± 0.5% (12.10%↑)** |
| | | Final Results | 21.7 (8.4%↓) | 23.7 (-) | 25.1 (5.9%↑) | **28.3 ± 0.4% (19.41%↑)** |
| MMLU-Machine Learning | GPT-4o | Before Training | 85.5 (0.0%) | 85.5 (-) | 85.5 (0.0%) | 85.5 (0.0%) |
| | | 1st Iteration | - | 85.5 (-) | 85.5 (0.0%) | **85.8 ± 0.5% (0.35%↑)** |
| | | 2nd Iteration | - | 85.6 (-) | 85.4 (0.2%↓) | **86.1 ± 1.0% (0.58%↑)** |
| | | 3rd Iteration | - | 85.6 (-) | 85.3 (0.3%↓) | **86.4 ± 1.1% (0.93%↑)** |
| | | Final Results | 85.5 (0.3%↓) | 85.8 (-) | 85.0 (0.9%↓) | **86.7 ± 0.8% (1.05%↑)** |
| | GPT-4-0125-preview | Before Training | 76.3 (0.0%) | 76.3 (-) | 76.3 (0.0%) | 76.3 (0.0%) |
| | | 1st Iteration | - | 76.4 (-) | **77.2 (1.0%↑)** | 77.1 ± 0.4% (0.92%↑) |
| | | 2nd Iteration | - | 76.6 (-) | 77.8 (1.5%↑) | **77.9 ± 0.6% (1.70%↑)** |
| | | 3rd Iteration | - | 77.0 (-) | 78.1 (1.4%↑) | **79.2 ± 0.7% (2.86%↑)** |
| | | Final Results | 76.3 (3.3%↓) | 78.9 (-) | 79.2 (0.3%↑) | **81.0 ± 0.8% (2.66%↑)** |
| | Llama 3.1 8B Instruct| Before Training | 51.8 (0.0%) | 51.8 (-) | 51.8 (0.0%) | 51.8 (0.0%) |
| | | 1st Iteration | - | 43.8 (-) | 46.9 (7.1%↑) | **48.2 ± 0.3% (10.05%↑)** |
| | | 2nd Iteration | - | 43.8 (-) | 45.2 (3.2%↑) | **47.3 ± 0.5% (7.99%↑)** |
| | | 3rd Iteration | - | 43.8 (-) | 44.4 (1.4%↑) | **46.4 ± 0.6% (5.94%↑)** |
| | | Final Results | 51.8 (9.5%↑) | 47.3 (-) | 47.4 (0.2%↑) | **57.1 ± 0.6% (20.72%↑)** |
| MMLU-College Physics | GPT-4o | Before Training | 91.0 (0.0%) | 91.0 (-) | 91.0 (0.0%) | 91.0 (0.0%) |
| | | 1st Iteration | - | 91.6 (-) | 91.6 (0.0%) | **91.8 ± 0.5% (0.22%↑)** |
| | | 2nd Iteration | - | 92.1 (-) | 92.3 (0.2%↑) | **92.5 ± 0.7% (0.43%↑)** |
| | | 3rd Iteration | - | 92.8 (-) | 91.2 (1.7%↓) | **93.2 ± 0.8% (0.43%↑)** |
| | | Final Results | 91.0 (2.7%↓) | 93.5 (-) | 91.3 (2.3%↓) | **94.1 ± 0.9% (0.64%↑)** |
| | GPT-4-0125-preview | Before Training | 81.6 (0.0%) | 81.6 (-) | 81.6 (0.0%) | 81.6 (0.0%) |
| | | 1st Iteration | - | 82.4 (-) | 81.9 (0.6%↓) | **82.5 ± 0.3% (0.12%↑)** |
| | | 2nd Iteration | - | 83.1 (-) | 82.4 (0.8%↓) | **83.4 ± 0.4% (0.36%↑)** |
| | | 3rd Iteration | - | 84.1 (-) | 82.1 (2.4%↓) | **84.5 ± 0.6% (0.48%↑)** |
| | | Final Results | 81.6 (4.7%↓) | 85.6 (-) | 82.3 (3.8%↓) | **85.9 ± 0.7% (0.35%↑)** |
| | Llama 3.1 8B Instruct| Before Training | 54.7 (0.0%) | 54.7 (-) | 54.7 (0.0%) | 54.7 (0.0%) |
| | | 1st Iteration | - | 51.1 (-) | 55.9 (9.4%↑) | **58.3 ± 0.2% (14.09%↑)** |
| | | 2nd Iteration | - | 51.1 (-) | 61.0 (19.4%↑) | **62.0 ± 0.4% (21.33%↑)** |
| | | 3rd Iteration | - | 55.7 (-) | 60.3 (8.3%↑) | **65.7 ± 0.5% (17.95%↑)** |
| | | Final Results | 54.7 (9.3%↓) | 60.3 (-) | 61.6 (2.2%↑) | **66.4 ± 0.5% (10.12%↑)** |

※ 筆者の考察：MMLUにおいてTextGrad（一階微分）ではイテレーションごとに性能が初期状態よりも劣化するLocal Optimaへの陥りがしばしば見られたが、これはフィードバックの曲率（変化の文脈）を加味していないためである。またモメンタムを加えたM-TextGradは停滞こそ避けるものの過剰な変動（振動）が生じやすい。REVOLVEは応答履歴からの高階近似を作用させることで、滑らかな最適化軌跡により局所解から安定して脱却し持続的な改善を実現できた。

### 3. コード最適化（Code Optimization）
LeetCode Hard データセットにおけるコードの自己最適化の結果（Table 7）。

| Models | Method | Completion Rate (Improv. over TextGrad) |
| :--- | :--- | :--- |
| GPT-4o | Zero-shot | 0.38 (25.49%↓) |
| | Reflexion (1 demonstration, 5 iterations) | 0.42 ± 0.003 (17.65%↓) |
| | TextGrad (0 demonstrations, 5 iterations) | 0.51 ± 0.005 (-) |
| | M-TextGrad (0 demonstrations, 5 iterations) | 0.49 ± 0.005 (3.92%↓) |
| | REVOLVE (0 demonstrations, 5 iterations) | **0.52 ± 0.002 (1.96%↑)** |
| GPT-4-0125-preview | Zero-shot | 0.33 (35.29%↓) |
| | Reflexion (1 demonstration, 5 iterations) | 0.41 ± 0.002 (19.61%↓) |
| | TextGrad (0 demonstrations, 5 iterations) | 0.51 ± 0.003 (-) |
| | M-TextGrad (0 demonstrations, 5 iterations) | 0.45 ± 0.006 (11.76%↓) |
| | REVOLVE (0 demonstrations, 5 iterations) | **0.56 ± 0.003 (9.80%↑)** |
| Llama 3.1 8B Instruct| Zero-shot | 0.12 (50%↓) |
| | Reflexion (1 demonstration, 5 iterations) | 0.20 ± 0.002 (16.67%↓) |
| | TextGrad (0 demonstrations, 5 iterations) | 0.24 ± 0.005 (-) |
| | M-TextGrad (0 demonstrations, 5 iterations) | 0.25 ± 0.003 (4.17%↑) |
| | REVOLVE (0 demonstrations, 5 iterations) | **0.31 ± 0.006 (29.17%↑)** |

※ 筆者の考察：SoTAであるReflexionやTextGradを上回る結果となった。Llama 3.1 8B InstructにおいてはTextGrad比で 29.17% もの大幅な解答完答率向上となった。複雑なコーディング課題ほど単一ステップのフィードバックでは修正しきれないエッジケースや構造的なバグが多く、進化の軌跡を捉えた二次的な調整（REVOLVE）が強力に効いていると考えられる。

### 計算コストの比較 (Efficiency)
二次微分シミュレートに伴うGPU使用率・処理時間等のコスト効率の比較（Table 9）。

| Task | Dataset | Method | Time per Iteration (s) | Total Time to Converge (s) | GPU Usage (GB) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Prompt Optimization | Objective Counting | TextGrad | 92.144 | 276.450 | 3.23 |
| | | M-TextGrad | 110.721 | 110.732 | 3.24 |
| | | REVOLVE | 137.815 | 137.821 | 3.23 |
| | GSM8K | TextGrad | 135.184 | 1351.85 | 3.23 |
| | | M-TextGrad | 152.423 | 1219.393 | 3.23 |
| | | REVOLVE | 176.538 | 1235.774 | 3.23 |
| Solution Optimization | Google-proof QA | TextGrad | 153.522 | 614.216 | 3.24 |
| | | M-TextGrad | 178.879 | 1091.162 | 3.23 |
| | | REVOLVE | 197.235 | 453.461 | 3.24 |
| | MMLU-Machine Learning | TextGrad | 172.429 | 896.631 | 3.24 |
| | | M-TextGrad | 207.819 | 685.803 | 3.24 |
| | | REVOLVE | 223.807 | 626.659 | 3.24 |
| | MMLU-College Physics | TextGrad | 188.116 | 1636.612 | 3.24 |
| | | M-TextGrad | 225.631 | 1308.662 | 3.24 |
| | | REVOLVE | 245.167 | 1054.229 | 3.24 |
| Code Optimization | Objective Counting | TextGrad | 1078.783 | 18986.655 | 6.46 |
| | | M-TextGrad | 1241.917 | 18472.411 | 6.46 |
| | | REVOLVE | 1352.174 | 15820.489 | 6.46 |

※ 筆者の考察：REVOLVEはプロンプト間の類似度計算などで1イテレーションあたりの経過時間はベースラインより微増するものの、GPU使用量に変更はなく、結果的にTextGradよりも少ないイテレーション数で収束（高い正答・ロス低下）に向かうため、**全体としての必要処理時間（Total Time）はむしろ短縮され、効率性が高い**ことが示明された。
