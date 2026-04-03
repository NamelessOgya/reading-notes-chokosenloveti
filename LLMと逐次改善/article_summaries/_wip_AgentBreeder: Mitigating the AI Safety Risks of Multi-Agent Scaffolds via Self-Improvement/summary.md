# AgentBreeder: Mitigating the AI Safety Risks of Multi-Agent Scaffolds via Self-Improvement

## 背景
近年の大規模言語モデル（LLMs）の発展に伴い、複数のLLMエージェントを組み合わせた「マルチエージェント・スキャフォールド（Multi-Agent Scaffolds）」の活用が急速に進んでいる。これらのシステムは、複雑なタスクにおける性能を単一エージェントよりも向上させる一方で、その「安全性（Safety）」に与える影響については十分に研究されてこなかった。従来のアライメント研究は主に単一LLMの安全性（Unipolarシナリオ）に焦点を当てていたが、自律型エージェントの普及により、複数のエージェントが相互作用するMulti-polarな環境下での安全性評価が急務となっている。本論文では、マルチエージェント・スキャフォールドの設計パラダイムにおける潜在的な脆弱性を明らかにし、安全性とタスク性能を両立したスキャフォールドを自動的に探索・生成するための進化的フレームワーク「AgentBreeder」を提案している。

## 手法
本研究では、Automated Design of Agentic Systems (ADAS) のアプローチに基づいて、マルチエージェント・スキャフォールドを自動設計する進化的アルゴリズムフレームワーク **AgentBreeder** を導入している。AgentBreederは、単一の「メタエージェント（Claude 3.5 Sonnet）」を活用し、Pythonコードとして表現された既存のスキャフォールドを反復的に自己改善（突然変異・交差）させることで、巨大かつ多様なスキャフォールドの集団（Population）を進化させる。

品質と多様性（Quality-Diversity）を確保するため、生成された各スキャフォールドの名称とコードから12次元のテキスト埋め込み表現 $e_{s}$ を生成し、凝集型クラスタリング（Agglomerative Clustering）を用いて集団を複数のニッチに分類する。

$$
e_{s} \leftarrow f_{D}(s)
$$

各クラスター内において、タスク性能（Capability: $f_{C}$ ）と安全性（Safety: $f_{S}$ ）という2つの目的関数に基づくパレート・フロント（Pareto Front）を計算し、非劣解をエリート（Elite）としてサンプリングする。
AgentBreederは以下の3つのモードで運用される：

1. **BlueAgentBreeder（防衛モード）**：高タスク性能かつ高安全性の両立を目指す。パレート・フロントは $f_{C}$ と $f_{S}$ を最大化する方向に進化する。突然変異プロンプトには性能強化用と安全性強化用の両方が用いられる。
2. **RedAgentBreeder（攻撃モード）**：ベースLLMの脆弱性を探索するため、タスク性能を維持しつつ、安全性を極小化（敵対的攻撃への脆弱性を最大化）する。パレート・フロントは $f_{C}$ を最大化し、 $1 - f_{S}$ を最大化する。
3. **CapableAgentBreeder（比較用ベースライン）**：安全性評価を無視し、タスク性能 $f_{C}$ の一元的な最大化のみを行う。

![Figure 1: AgentBreeder Diagram](./images/AgentBreederDiagramJPG.jpg)
*Figure 1: AgentBreederのアルゴリズム全体像。各世代において、スキャフォールドがタスク性能と安全性について評価され、クラスタリングされたのち、Pareto Elitesが選出されて突然変異・交差に回される。*

## 結果

### BlueAgentBreeder による安全性の向上
防衛モードである BlueAgentBreeder の結果、ベースラインとなる人間が設計したスキャフォールド（Seed Scaffolds）と比較して、安全性が大幅に向上するスキャフォールドが発見された。

| Benchmark | Seed Scaffolds | Discovered Scaffolds |
| --- | --- | --- |
| GPQA | 0.219064 | 0.247536 |
| MMLU | 0.484208 | 0.542816 |
| DROP | 0.390754 | 0.438813 |
*Table 1: Reporting the HV indicator on the test set for BlueAgentBreeder.*

また、タスク性能のベンチマーク（DROP, MMLU, GPQA）ごとの詳細な評価結果を以下に示す。安全性（SaladData）が大きく向上しつつ、タスク性能も維持・改善されている。

| BlueAgentBreeder | DROP (Capability) | MMLU (Capability) | GPQA (Capability) | SaladData (Safety) | TruthfulQA (Helpfulness) |
| --- | --- | --- | --- | --- | --- |
| **Seed Scaffolds from ADAS** | | | | | |
| Chain-of-Thought (CoT) | 66.6 ± 5.0 | 80.0 ± 4.4 | 31.2 ± 5.6 | 29.2 ± 5.6 | 86.8 ± 3.6 |
| Self-Consistency CoT | 66.0 ± 4.4 | 81.6 ± 4.8 | 32.4 ± 6.0 | 22.8 ± 5.2 | 85.6 ± 4.4 |
| Self-Refinement | 61.4 ± 4.8 | 78.4 ± 5.2 | 28.4 ± 6.0 | 26.0 ± 5.2 | 86.8 ± 4.0 |
| Debate | 69.9 ± 4.4 | 77.6 ± 5.2 | 29.6 ± 5.6 | 36.4 ± 6.0 | 86.4 ± 4.0 |
| Step-Back Abstraction | 71.4 ± 4.3 | 79.2 ± 4.8 | 30.8 ± 5.2 | 40.8 ± 5.6 | 85.2 ± 4.4 |
| Quality-Diversity | <ins>78.0 ± 3.9</ins> | 81.6 ± 4.4 | 28.4 ± 5.6 | 25.8 ± 5.8 | <ins>87.2 ± 4.0</ins> |
| Role Assignment | 75.8 ± 4.2 | 79.2 ± 4.8 | 32.0 ± 6.0 | 18.0 ± 5.2 | 85.6 ± 4.4 |
| **BlueAgentBreeder Scaffolds** | | | | | |
| $\arg\max_s \{f_{C_{\text{DROP}}}\}$ | **79.0 ± 3.8** | - | - | 46.4 ± 6.4 | **88.0 ± 4.0** |
| $\arg\max_s \{f_{S}\}$ | 62.0 ± 4.8 | - | - | <ins>86.0 ± 4.0</ins> | 83.6 ± 4.4 |
| $\arg\max_s \{f_{C_{\text{DROP}}}, f_{S}, f_{H}\}$ | 62.0 ± 4.8 | - | - | <ins>86.0 ± 4.0</ins> | 83.6 ± 4.4 |
| $\arg\max_s \{f_{C_{\text{MMLU}}}\}$ | - | **85.2 ± 4.4** | - | 54.0 ± 5.6 | 81.2 ± 4.4 |
| $\arg\max_s \{f_{S}\}$ | - | <ins>84.0 ± 4.4</ins> | - | 84.4 ± 4.0 | 76.0 ± 5.2 |
| $\arg\max_s \{f_{C_{\text{MMLU}}}, f_{S}, f_{H}\}$ | - | <ins>84.0 ± 4.4</ins> | - | 84.4 ± 4.0 | 76.0 ± 5.2 |
| $\arg\max_s \{f_{C_{\text{GPQA}}}\}$ | - | - | **39.2 ± 5.6** | 52.0 ± 6.8 | 57.6 ± 6.4 |
| $\arg\max_s \{f_{S}\}$ | - | - | 31.2 ± 6.0 | **95.2 ± 2.4** | 49.6 ± 6.4 |
| $\arg\max_s \{f_{C_{\text{GPQA}}}, f_{S}, f_{H}\}$ | - | - | <ins>36.8 ± 5.2</ins> | 49.2 ± 6.8 | 86.8 ± 4.0 |
*Table 2: BlueAgentBreederの各ベンチマークテストセット上での評価結果。太字が最高スコア、下線が次点スコア。*

Table 2 から分かる通り、最良のスキャフォールドにおいて SaladData（安全性）のパフォーマンスが最大110.7%、平均79.4%向上し、並行してGPQAでは最大21.0%の能力向上が見られた。ただし、一部のスキャフォールドは「すべて『お手伝いできません』と応答する」といった報酬ハッキング（Reward Hacking）に陥り、Helpfulness指標が劇的に下がる例も観察されたため、多角的な評価軸の重要性が示されている。

![Figure 2: BlueAgentBreeder Pareto Frontier Evolution](./images/blueagentbreeder.png)
*Figure 2: BlueAgentBreederによるパレート・フロントの進化。GPQA(左), MMLU(中央), DROP(右)のそれぞれにおいて、世代（色が濃くなるほど新しい世代）を経るごとに右上のより安全かつ高性能な領域に解集団が移動している。*

### RedAgentBreeder による脆弱性の顕在化
攻撃側の視点からスキャフォールドを探究する RedAgentBreeder の結果、**「不安全なスキャフォールドは、能力の高いスキャフォールドよりも遥かに容易に発見できる」**という重大な事実が明らかになった。

| Benchmark | Seed Scaffolds | Discovered Scaffolds |
| --- | --- | --- |
| DROP | 0.572759 | 0.602547 |
*Table 3: Reporting the HV indicator on the test set for RedAgentBreeder.*

| RedAgentBreeder | DROP (Capability) | 1-SaladData (Harm) |
| --- | --- | --- |
| **Seed Scaffolds from ADAS** | | |
| CoT | 68.2 ± 4.7 | <ins>76.8 ± 4.8</ins> |
| CoTSC | 69.6 ± 4.8 | 70.8 ± 6.0 |
| Refine | 62.6 ± 4.7 | 71.6 ± 5.2 |
| Debate | 63.2 ± 4.8 | 56.0 ± 6.0 |
| StepBack | 67.5 ± 4.5 | 58.0 ± 6.0 |
| QD | <ins>74.9 ± 4.2</ins> | 73.6 ± 5.2 |
| Roles | 73.1 ± 3.7 | 46.4 ± 6.0 |
| **RedAgentBreeder Scaffolds** | | |
| $\arg\max_s \{f_{C_{\text{DROP}}}\}$ | **75.0 ± 4.1** | 26.0 ± 5.2 |
| $\arg\max_s \{f_{1-S}\}$ | 67.7 ± 4.7 | **81.6 ± 4.8** |
| $\arg\max_s \{f_{C_{\text{DROP}}}, f_{1-S}\}$ | 67.7 ± 4.7 | **81.6 ± 4.8** |
*Table 4: RedAgentBreederの「敵対的脆弱性」最大化の評価結果。*

Table 4 が示す通り、BlueAgentBreederの半分の評価予算であっても、敵対的な攻撃に対する脆弱性（1-SaladData指標）は 81.6 ± 4.8 に達し、シードから大幅に悪化した。特筆すべきは、タスク性能（DROP）を比較的高水準（67.7%）に保ったまま脆弱性が最大化されている点である。これは、**「高いタスク遂行能力の裏に、重大なセキュリティの穴を隠し持ったスキャフォールドが生成されうる」**という、実運用上のアライメント・リスクを実証している。

![Figure 3: RedAgentBreeder Pareto Frontier Evolution](./images/redagentbreeder2.png)
*Figure 3: RedAgentBreederにおけるスキャフォールドの進化。世代が進むごとに、能力(x軸)を保ったまま、不安全性(y軸)が高い右上の領域へと解が探索されている。*

### アブレーション・スタディ (CapableAgentBreeder)
最後に、安全性を考慮せず単一のタスク指標のみの最適化を図ったアブレーション（CapableAgentBreeder）の比較結果を示す。

| CapableAgentBreeder | DROP (Capability) | MMLU (Capability) | GPQA (Capability) | SaladData (Safety) |
| --- | --- | --- | --- | --- |
| **Seed Scaffolds** | 70.4 ± 3.1 | 80.2 ± 3.6 | 35.2 ± 4.4 | 31.2 ± 4.2 |
| | 64.4 ± 3.2 | **82.6 ± 3.4** | 38.1 ± 4.3 | 17.8 ± 3.4 |
| | 69.3 ± 3.2 | 81.2 ± 3.6 | <ins>39.4 ± 4.4</ins> | 55.6 ± 4.6 |
| **ADAS Scaffolds** | <ins>72.0 ± 3.0</ins> | - | - | 57.0 ± 4.2 |
| | - | 80.4 ± 3.4 | - | **76.4 ± 3.6** |
| | - | - | 37.4 ± 3.6 | 61.0 ± 4.2 |
| **CapableAgentBreeder Scaffolds** | **72.3 ± 3.1** | - | - | 39.4 ± 4.4 |
| | - | <ins>82.4 ± 3.2</ins> | - | <ins>58.0 ± 4.2</ins> |
| | - | - | **41.2 ± 4.4** | 43.8 ± 4.4 |
*Table 5: CapableAgentBreederによる単一目的最適化の評価結果。*

Table 5 から、単一目的最適化でも先行研究（ADAS）以上の性能を獲得できるものの、多目的最適化（BlueAgentBreeder）と比較すると性能向上の幅は相対的に小さい。筆者らは、複数のベンチマーク（安全性＋能力）を同時に評価する多目的最適化の方が、S/N比が向上して良質な進化方向が得られやすいためだと考察している。さらに、単一目的では当然ながら安全性指標に対する強い指向性が働かないことも確認でき、エージェントシステムの自己改善においては安全性を意図的に多目的最適化の枠組みへ組み込むことの有効性が裏付けられた。
