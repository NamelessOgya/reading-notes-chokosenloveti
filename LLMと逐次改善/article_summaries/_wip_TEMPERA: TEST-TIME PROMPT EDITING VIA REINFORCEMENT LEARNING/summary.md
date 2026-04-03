# TEMPERA: TEST-TIME PROMPT EDITING VIA REINFORCEMENT LEARNING

## 背景
大規模言語モデル（LLM）の発展に伴い、In-Context Learning（Few-Shotプロンプティング）が有望な手法として注目されている。しかし、言語モデルの性能は与えられるプロンプトの設計（命令の表現、少数ショットの例の選び方や順序など）に極めて敏感であり、タスクごとに最適なプロンプトを見つけるのは困難である。

従来のアプローチのうち、Soft Prompt Tuning（連続的なプロンプトの最適化）は勾配法を用いて最適化できるものの、生成されたベクトル空間のプロンプトは人間が解釈できない（Interpretableでない）という問題がある。また、Discrete Prompt Optimization（RLPromptなど）による探索は、タスク全体で固定のプロンプト（クエリに依存しないプロンプト）を出力するものが多く、テストケース（入力クエリ）ごとに柔軟にプロンプトを変更することができなかった。
筆者らは、テスト時に与えられたクエリの性質に合わせてプロンプトを個別に編集する「Test-Time Editing（テスト時編集）」の重要性を指摘し、人間の事前知識を取り入れつつ、柔軟かつ解釈可能な離散プロンプトの最適化を自動化する強化学習フレームワーク「TEMPERA」を提案した。

## 手法
本論文では、プロンプトの編集プロセスをマルコフ決定過程（MDP）として定式化し、強化学習（RL）エージェントにテスト時プロンプト編集を行わせる。

テスト時において、初期プロンプト $p_{0}$ とクエリ $x$ が与えられたとき、RLエージェントはアクション空間から編集手法を選択し、各ステップごとにプロンプトを更新する。
状態表現（State）としては、LLMの最後の隠れ状態 $\mathcal{L}(p_{t}, x)$ を利用する。

アクション空間は以下の3つの要素に対する編集操作として定義される。
1. **Instruction（命令文）**: NLTK等を用いてフレーズレベルにトークン化し、フレーズのスワップ（Swap）、追加（Add）、削除（Delete）を行う。
2. **In-Context Exemplar（少数ショットの例）**: 予め用意した例のプールから例を選び、順番を入れ替えたり（Permute）、別の例と差し替えたり（Swap）する。
3. **Verbalizer（ラベルと単語の対応付け）**: 予測対象のラベルをどのようなキーワード（"great"や"terrible"など）で表現するかを変更（Change）する。

報酬（Reward）は、言語モデルが正解ラベル $c$ を予測する対数確率と、それ以外の不正解ラベル $c^{\prime}$ を予測する対数確率の差分ベースのスコア $s$ を用いる。目標は最終的なプロンプトのスコアを中心に高めることであるが、ステップごとに評価するため、連続するステップ間でのスコアの差分を即時報酬 $r_{t}$ として定義する。

$$
s(c, x, p_{t}) = \lambda_{1} \log P_{\mathcal{L}}(\hat{y}_{c} | x, p_{t}) - \lambda_{2} \max_{c^{\prime} \ne c} \log P_{\mathcal{L}}(\hat{y}_{c^{\prime}} | x, p_{t})
$$

$$
r_{t} = s(c, x, p_{t}) - s(c, x, p_{t-1})
$$

Policyの学習にはPPOアルゴリズムを用い、どのような編集を行うか（候補をどのように参照するか）についてAttentionベースのネットワーク構造を採用している。また、学習の安定化のためにObservation（状態）およびRewardの正規化が行われている。

## 結果

TEMPERAは、少数のデータセットを用いたSST-2, Yelp, MR, CR, AG Newsなどのデータセットにおいて、微調整（Finetuning）や既存のプロンプト探索法（RLPrompt, GrIPS, Soft Prompt Tuningなど）を上回る性能を達成した。

### 図解と基本性能
![Figure 1: Data Efficiency (Average)](./images/data_efficiency_avg.png)
![Figure 2: Test-Time Editing via RL](./images/rlprompt.png)
![Figure 3: Data Efficiency for TEMPERA (Individual)](./images/data_efficiency_ind.png)
![Figure 4: Data Efficiency for TEMPERA (Full)](./images/data_efficiency_full.png)
![Figure 5: Comparison of Different Prompting Methods](./images/comparison.png)

Figure 1 や Figure 3, Figure 4 に示される通り、TEMPERAの大きな特徴はそのデータ効率の高さにある。従来のFinetuningが同等の精度を達成するために必要なデータ数と比較して、TEMPERAは平均して5.33倍のデータ効率（少ない少数ショット数で高精度）を達成した。また、Figure 5 の比較表が示すように、勾配計算が不要（Gradient-free）でありながら、クエリ依存（Query-dependent）の解釈可能なプロンプトを生成できる唯一のポジションを確立している。

### 実験結果の詳細 (Table)

| | | SST-2 | Yelp P. | MR | CR | AG News |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| Finetuning | Finetuning (few-shot) | 80.6 (3.9) | 88.7 (4.7) | 67.4 (9.7) | 73.3 (7.5) | 84.9 (3.6) |
| Continuous Prompt | Soft Prompt Tuning | 73.8 (10.9) | 88.6 (2.1) | 74.1 (14.6) | 75.9 (11.8) | 82.6 (0.9) |
| | Black-Box Tuning | 89.1 (0.9) | 93.2 (0.5) | 86.6 (1.3) | 87.4 (1.0) | 83.5 (0.9) |
| | AutoPrompt | 75.0 (7.6) | 79.8 (8.3) | 62.0 (0.8) | 57.5 (5.8) | 65.7 (1.9) |
| Discrete Prompt | Manual Prompt | 82.8 | 83.0 | 80.9 | 79.6 | 76.9 |
| | In-Context Demo. | 85.9 (0.7) | 89.6 (0.4) | 80.6 (1.4) | 85.5 (1.5) | 74.9 (0.8) |
| | Instructions | 89.0 | 84.4 | 85.2 | 80.8 | 54.8 |
| | GrIPS | 87.1 (1.5) | 88.2 (0.1) | 86.1 (0.3) | 80.0 (2.5) | 65.4 (9.8) |
| | RLPrompt | 90.1 (1.8) | **93.9 (1.8)** | 86.7 (2.4) | 87.2 (1.7) | 77.2 (2.0) |
| Discrete Prompt | TEMPERA (ours) | **91.9** (2.0) | 92.6 (1.7) | **88.0** (1.1) | **91.1** (1.6) | **85.5** (1.5) |
Table 2 においてベースラインとの比較が行われており、TEMPERAは殆どのタスクでSoTAを達成した。SST-2では絶対値で1.8%の向上、CRでは3.9%の向上を達成しており、分散（括弧内の標準偏差）もContinuous Prompt系の手法に比べて小さく安定している。

| | Before Editing | After Editing |
| :--- | :--- | :--- |
| Instruction (Swap) | "Given text, classify whether it is good or bad." | "Classify whether it is good or bad, given text." |
| Instruction (Add) | "Given text, classify whether it is good or bad." | "Given text, given text, Classify whether it is good or bad." |
| Instruction (Delete) | "Given text, classify whether it is good or bad." | "Classify whether it is good or bad." |
| Example (Permute) | {Example 1, Example 2, ..., Example k } | {Example k, Example 3, ..., Example 1 } |
| Example (Swap) | {Example 1, Example 2, ..., Example k } | {Example k+1, Example n, ..., Example 1 } |
| Verbalizer (Change) | { "positive", "negative"} | {"great", "terrible"} |
Table 1 は具体的なアクション空間の例を示しており、人間にとって解釈可能（Readable）なテキスト変形のみに制約されていることがわかる。

| | SST-2 | MR | AG News |
| :--- | :---: | :---: | :---: |
| Manual Prompt | 82.8 | 80.9 | 76.9 |
| In-Context Demo. | 85.9 | 80.6 | 74.9 |
| Instructions | 89.0 | 85.2 | 54.8 |
| GrIPS | 87.1 | 87.1 | 65.4 |
| TEMPERA (No TTE) | **92.0** | 87.4 | 81.3 |
| TEMPERA | 91.9 | **88.2** | **84.3** |
Table 3 のアブレーション実験では、テスト時編集（TTE: Test-Time Editing）の寄与を検証している。AG Newsのような難易度の高いタスクほどクエリ依存（Query-dependent）にプロンプトを変動させる恩恵が大きく（+3.0%）、TTEを含めることの有用性が証明されている。

| | SST-2 | MR | AG News |
| :--- | :---: | :---: | :---: |
| TEMPERA (No Inst & Verb) | 91.2 | 87.2 | 82.2 |
| TEMPERA (No Inst) | 91.9 | 88.2 | 84.3 |
| TEMPERA | **92.4** | **88.4** | **85.5** |
Table 4 のアクション空間の要素のアブレーションによれば、InstructionやVerbalizerの編集を取り除くことで一貫して精度が低下しており、多様な編集手法を組み合わせることの優位性が確認された。

| | SST-2 | MR | AG News |
| :--- | :---: | :---: | :---: |
| TEMPERA (2 Examples) | 91.6 | 87.9 | 84.0 |
| TEMPERA (4 Examples) | 91.9 | 88.2 | **84.3** |
| TEMPERA (8 Examples) | **92.4** | **88.4** | 82.2 |

| | SST-2 | MR | AG News |
| :--- | :---: | :---: | :---: |
| TEMPERA (Pool Size 8) | 91.6 | 87.9 | 84.1 |
| TEMPERA (Pool Size 16) | 91.9 | 88.2 | 84.3 |
| TEMPERA (Pool Size 32) | **92.2** | **88.4** | **84.7** |
Table 6 (上) および Table 7 (下) は、In-Context Exemplar（少数ショットの例）数と候補のプールサイズに関する検証である。例示の数を増やす、あるいは候補となるプールサイズを大きくして探索の余地を増やすことで精度は向上する傾向にあるが、AG Newsにおける8 Examplesのようにトークン数上限（RoBERTaの場合は512）によって切断（Truncate）が発生すると精度低下を引き起こすことが示唆された。

**Table 5 (定性的な編集結果の例)**
| Task | 編集前後 | 内容 |
| :--- | :--- | :--- |
| **SST-2** | Before Edit | In this task, you are given sentences from movie reviews... / Review: heroes. Sentiment: <mask\>. |
| | After Edit | In this task, you are given sentences from movie reviews... *(Verbalizerがpositive/negativeからgreat/terribleへと最適化されている)* |
| **AG News** | Before Edit | Classify the news articles into the categories... |
| | After Edit | Classify the news articles into the categories... *(クエリの内容により近いIn-Context Exemplarへと差し替えられている)* |
Table 5 は定性的な出力であり、RL方針によって最適化された結果が元の意味を維持しつつタスクの難易度を劇的に下げる単語選びや用例選択になっていることを示している。
（※他、付録の実験・Table 8〜13についても論文中に記載あり。紙幅と要約の都合で割愛するが、総じてスケーラビリティとハイパーパラメータに関する情報が補足されている。）
