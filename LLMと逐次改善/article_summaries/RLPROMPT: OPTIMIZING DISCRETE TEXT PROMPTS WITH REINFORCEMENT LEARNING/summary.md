# RLPROMPT: Optimizing Discrete Text Prompts with Reinforcement Learning

## 背景
大規模言語モデル（LLMs）を用いたプロンプト学習において、離散的（Discrete）なテキストプロンプトの最適化は極めて重要であるものの、文字列という離散的な制約上、勾配を用いた最適化が困難であるという課題があった。これに対し、埋め込み（Embedding）を直接最適化する連続的（Soft）なプロンプトチューニングが主流となりつつあるが、「人間にとって解釈不能」「他モデルへの転移が困難」「LLMの内部勾配へのアクセスが必要（GPT-3のようなブラックボックスAPIでは使用不可）」といった問題があった。一方で、ヒューリスティックな検索（パラフレーズや手動調整）に基づく離散プロンプトの探索は、探索空間を体系的に網羅できず、安定性に欠ける。本論文ではこれらの課題を解決するため、LLMの勾配を必要とせず、強化学習（RL）を用いて最適化された離散プロンプトを生成するパラメータ効率の良いポリシーネットワーク「RLPrompt」を提案している。

***

**【補足】言及されている代表的な先行研究アプローチまとめ**

<details>
<summary>1. 連続的（Soft）なプロンプトチューニング</summary>

| 論文名 (代表的な提案枠組み) | 発表年 | 手法概要 |
| :--- | :--- | :--- |
| **Prefix-Tuning:** Optimizing continuous prompts for generation | 2021 | 生成タスク向けに、入力や隠れ層の先頭に学習可能な連続ベクトル（Prefix）を付与する。 |
| **P-Tuning:** GPT understands, too | 2021 | 学習可能な埋め込み層を用いて、連続的なプロンプトトークンを最適化する。 |
| **SPOT:** Better frozen model adaptation through soft prompt transfer | 2021 | 別のタスクで事前学習したSoft Promptを転移学習させることで学習効率を上げる。 |
| **PPT:** Pre-trained prompt tuning for few-shot learning | 2021 | 大規模なラベルなしデータでSoft Promptを事前学習し、Few-shot性能を向上させる。 |
| **Input-Tuning:** Adapting unfamiliar inputs to frozen pretrained... | 2022 | 入力表現自体を連続的なプロンプトとしてチューニングし凍結モデルに適応させる。 |

</details>

<details>
<summary>2. ヒューリスティックな離散プロンプトの探索（手動・パラフレーズ・検索）</summary>

| 論文名 (代表的な提案枠組み) | 発表年 | 手法概要 |
| :--- | :--- | :--- |
| **LAMA:** Language models as knowledge bases? | 2019 | 知識抽出タスク等のために手作業でデザインした穴埋め（Cloze）テンプレートを使用する。 |
| **GPT-3:** Language models are few-shot learners | 2020 | Task DescriptionやFew-shotの例示を手作業でヒューリスティックに構築する。 |
| **AutoPrompt:** ...knowledge from language models with automatically... | 2020 | 勾配情報を用いて離散的なトリガートークンを探索・反復編集する。 |
| **PET:** Exploiting cloze-questions for few-shot text classification... | 2021 | 文脈に合ったクロース問題形式の手動テンプレートを用いてFew-Shotテキスト分類を行う。 |
| **LM-BFF:** Making pre-trained language models better few-shot learners | 2021 | T5を用いてプロンプトテンプレートを自動生成・パラフレーズし、最良のものを検索する。 |
| **KATE:** What makes good in-context examples for gpt-3? | 2021 | k-NNアルゴリズムを用いて文脈に適したFew-Shotの例示を検索アルゴリズムで自動取得する。 |
| **GrIPS:** Gradient-free, edit-based instruction search... | 2022 | 勾配を使わず、文単位の編集（パラフレーズや単語の入れ替え等）を繰り返して探索する。 |

</details>

***

## 手法
著者らは離散プロンプトの最適化を、テキスト生成タスクとして強化学習の問題に定式化している。直接トークンを編集するのではなく、凍結された小規模LM（DistilGPT-2など）の上に小規模なMLP層を追加したポリシーネットワーク $\pi_{\theta}(z_t | \mathbf{z}_{<t})$ を訓練し、プロンプトトークン $z_t$ を自己回帰的に生成する。
最適化の目的関数は以下の通りである。
$$ \max_{\theta} R(\mathbf{y}_\text{LM}(\hat{\mathbf{z}}, \mathbf{x})), \hat{\mathbf{z}} \sim \prod_{t=1}^T \pi_{\theta}(z_t | \mathbf{z}_{<t}) $$
しかし、巨大なブラックボックスLLMからの報酬シグナルは非常に不安定で複雑である。そこで、訓練効率と安定性を向上させるため、以下の2つの報酬エンジニアリング手法（Reward Engineering）を導入している。

1. **Input-Specific $z$-Score Reward (入力固有の$z$スコア報酬)**
入力データの難易度の差異による報酬のブレを無くすため、入力ごとに適応的な正規化を行う。
$$ z\text{-score}(\mathbf{z}, \mathbf{x}) = \frac{R_{\mathbf{x}}(\mathbf{z}) - \text{mean}_{\mathbf{z}' \in Z(\mathbf{x})} R_{\mathbf{x}}(\mathbf{z}')}{\text{std}_{\mathbf{z}' \in Z(\mathbf{x})}R_{\mathbf{x}}(\mathbf{z}')} $$

2. **Piecewise Reward (区分報酬)**
分類タスクなどにおいて、特定のクラスだけを常に予測するような敵対的プロンプトを避けるため、正解ラベルの確率から他クラスの最大確率を引いたギャップに対し、完全に正解した場合には強いプラスの報酬、間違えた場合にはマイナスの報酬を与える区分的（Piecewise）な設計を行っている。
$$ R(\mathbf{x}, c) = \lambda_1^{1 - \text{Correct}} \lambda_2^{\text{Correct}} \text{Gap}_{\mathbf{z}}(c) $$

### ゼロショットとフューショットのタスク別適応
本手法では応用領域ごとに、RLが「何を報酬関数（自動採点器）として使うか」を変えることで、大きく2つの異なるデータ設定を実現しています。
*   **テキスト分類（Few-Shot）**: 感情分類やトピック分類では、正誤判定のスコア計算に「正解ラベル」が必要なため、1クラスあたりわずか16件の正解データのみを与える「Few-Shot」設定でRLを回しています。
*   **テキストスタイル変換（Zero-Shot）**: 表現の書き換え等の生成タスクでは、「別の分類AIが出すスタイルの一致度」「BERTScoreによる意味の保持度」「他のLMによる文章の流暢さ」の3つを組み合わせた「自動評価器」が教師データの代わりにスコアを出力します。これにより、変換前後の「正解ペアデータ」を1件も必要としない「Zero-Shot（完全教師なし）」での強化学習を可能にしています。

## 結果
### 分類およびテキスト生成における優位性
提案手法（RLPrompt）は、Few-Shotのテキスト分類タスクと、教師なしのテキストスタイル変換（TST）タスクにおいて広範な評価が行われた。

![Table 1: Main datasets evaluated in this work](./images/tab-NLU-dataset.png)

#### Table 1: Main datasets evaluated in this work
| Dataset | Type | $\vert C \vert$ | $\vert\text{Train}\vert=\vert\text{Dev}\vert$ | $\vert\text{Test}\vert$ | Manual template | Label words |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SST-2 | Sentiment (Movie reviews) | 2 | $16 \times \vert C \vert$ | 1.8k | `<S>` It was `[MASK]` . | terrible, great |
| Yelp P. | Sentiment (Yelp reviews) | 2 | $16 \times \vert C \vert$ | 38k | `<S>` It was `[MASK]` . | terrible, great |
| MR | Sentiment (Movie reviews) | 2 | $16 \times \vert C \vert$ | 2k | `<S>` It was `[MASK]` . | terrible, great |
| CR | Sentiment (Product reviews) | 2 | $16 \times \vert C \vert$ | 2k | `<S>` It was `[MASK]` . | terrible, great |
| SST-5 | Sentiment (Movie reviews) | 5 | $16 \times \vert C \vert$ | 2.2k | `<S>` It was `[MASK]` . | terrible, bad, okay, good, great |
| Yelp | Sentiment (Yelp reviews) | 5 | $16 \times \vert C \vert$ | 50k | `<S>` It was `[MASK]` . | terrible, bad, okay, good, great |
| Subj | Subjectivity (Movie reviews)| 2 | $16 \times \vert C \vert$ | 2k | `<S>` This is `[MASK]` . | subjective, objective |
| AG's News | Topic (News articles) | 4 | $16 \times \vert C \vert$ | 7.6k | `[MASK]` News: `<S>` | World, Sports, Business, Tech |
| TREC | Topic (Question types) | 6 | $16 \times \vert C \vert$ | 0.5k | `[MASK]`: `<S>` | Description, Entity, Expression, Human, Location, Number |
| DBPedia | Topic (Wikipedia ontologies)| 14 | $16 \times \vert C \vert$ | 70k | `[Category: [MASK]]` `<S>` | Company, Education, Artist, Sports, Office, Transportation, Building, Natural, Village, Animal, Plant, Album, Film, Written |
| Yahoo | Topic (Question types) | 10 | $16 \times \vert C \vert$ | 60k | Topic `[MASK]`: `<S>` | culture, science, health, education, computer, sports, business, music, family, politics |

**【筆者の見解・考察】**
*   **汎用性と評価の網羅性**: センチメント分析だけでなく、トピック分類、多クラス分類タスクまで多様な7種類のNLUデータセットを選定しています。これにより、手動テンプレートやラベル語がタスクごとに異なっていても、提案手法のRLPromptが高い適応性を持ち、かつ1クラスあたりわずか16サンプルの「真のFew-Shot設定」においても有効に機能すること（サンプル効率の高さ）を検証する狙いがあります。

#### Table 3: Results of few-shot text classification
| | SST-2 | Yelp P. | MR | CR | SST-5 | Yelp | AG's News | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Fine-Tuning | 80.6 (3.9) | 88.7 (4.7) | 67.4 (9.7) | 73.3 (7.5) | 40.7 (3.0) | **51.0** (2.2) | **84.9** (3.6) | 69.5 |
| Manual Prompt | 82.8 | 83.0 | 80.9 | 79.6 | 34.9 | 42.1 | 76.9 | 68.6 |
| Instructions | 89.0 | 84.4 | 85.2 | 80.8 | 29.8 | 43.0 | 54.8 | 58.5 |
| In-Context Demonstration | 85.9 (0.7) | 89.6 (0.4) | 80.6 (1.4) | 85.5 (1.5) | 39.3 (0.9) | 49.4 (0.3) | 74.9 (0.8) | 72.2 |
| Prompt Tuning (Soft Prompt) | 73.8 (10.9) | 88.6 (2.1) | 74.1 (14.6) | 75.9 (11.8) | 40.2 (6.5) | 49.1 (3.1) | 82.6 (0.9) | 69.2 |
| BB Tuning (2 soft tokens) | 83.2 (3.5) | 86.0 (1.6) | 77.1 (3.9) | 83.2 (2.5) | 39.2 (2.4) | 41.5 (1.9) | 74.0 (1.9) | 69.2 |
| BB Tuning (5 soft tokens) | 84.6 (4.0) | 78.7 (2.3) | 79.8 (1.5) | 82.9 (3.6) | 36.6 (2.1) | 33.7 (2.3) | 73.6 (3.6) | 67.1 |
| BB Tuning (Mixed, 50 soft) | 89.1 (0.9) | 93.2 (0.5) | 86.6 (1.3) | 87.4 (1.0) | 38.4 (1.1) | 44.8 (1.3) | 83.5 (0.9) | 74.7 |
| GrIPS (Discrete Enumeration)| 87.1 (1.5) | 88.2 (0.1) | 86.1 (0.3) | 80.0 (2.5) | 32.0 (1.8) | 47.2 (0.5) | 65.4 (9.8) | 69.4 |
| AutoPrompt | 75.0 (7.6) | 79.8 (8.3) | 62.0 (0.8) | 57.5 (5.8) | 27.8 (3.3) | 29.0 (5.0) | 65.7 (1.9) | 56.7 |
| **RLPrompt (Ours, 2 tokens)** | 90.3 (1.3) | 94.1 (0.8) | 86.5 (1.2) | 87.4 (1.7) | 40.1 (1.9) | 45.6 (3.8) | 76.8 (1.4) | 74.4 |
| **RLPrompt (Ours, 5 tokens)** | **92.5** (0.8) | **95.1** (1.0) | **87.1** (0.4) | **89.5** (0.6) | **41.4** (3.2) | 44.8 (4.3) | 80.2 (0.7) | **75.8** |

実験では、手動プロンプト（Manual Prompt）、In-Context学習、ソフトプロンプトチューニング（Prompt Tuning, BB Tuning）や離散プロンプトのヒューリスティック探索（GrIPS, AutoPrompt）など、既存の多様なパラダイムを凌駕する精度を達成した。特にFine-Tuningと比較した場合、全パラメータを更新するコストが不要でありながら、同等もしくはそれ以上のゼロショット・フューショット性能を安定して引き出せている。

**【筆者の見解・考察】**
*   **圧倒的なFew-Shot性能**: RLPromptは、人間の手動プロンプトやインコンテクスト学習を大幅に上回るだけでなく、すべての全パラメータファインチューニングやSoft Prompt Tuningをも上回るパフォーマンスを発揮しています。
*   **離散探索アルゴリズムの弱点克服**: GrIPSやAutoPromptといった既存の離散探索アルゴリズムに対して、RLPromptによる「強化学習を用いた生成」が明確な優位性を持つ（局所解に陥りにくく、より良いトークン空間を効率的に探索できている）ことが証明されたと結論づけています。

#### Table 4: Comparison of different (prompting) paradigms
| Methods | Frozen LMs | Automated | Gradient-Free | Guided Optimize | Few-Shot | Zero-Shot | Transferrable b/w LMs | Interpretability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fine-Tuning | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manual Prompt | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Instructions | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| In-Context Demonstration | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Soft Prompt Tuning | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Discrete Prompt Enumeration | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| AutoPrompt | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **RLPrompt (Ours)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**【筆者の見解・考察】**
*   **実用性のマトリックス**: 筆者らはこの表を通じて、RLPromptの強力なアドバンテージを強調しています。連続ベクトルを用いる手法（Soft Prompt）と異なり、「モデル内部の勾配情報がいらない（Gradient-Free）」かつ「LLM間でプロンプトが使い回せる（Transferable）」という離散プロンプトの特長を維持したまま、「自動化された効率的な探索（Automated / Guided Optimize）」の両立に成功している唯一の最適化手法であると主張しています。

#### Table 6: Automatic evaluation on Yelp sentiment transfer 
| Model | Content | Style | Fluency | **J(C, S, F)** | **GM(C, S, F)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Training Baselines** | | | | | |
| Style Transformer | 75.2 | 96.4 | 58.6 | 46.1 | 75.2 |
| DiRR | **78.8** | **97.7** | 75.6 | 59.6 | 83.5 |
| **Prompting Baselines (GPT-2-xl)** | | | | | |
| Null Prompt | 37.4 | 94.8 | 97.6 | 33.6 | 70.2 |
| Random Prompt | 39.6 | 93.8 | **97.8** | 34.7 | 71.3 |
| Manual Prompt | 64.2 (6.8) | 91.5 (3.6) | 93.2 (1.4) | 53.4 (7.9) | 81.8 (3.4) |
| **RLPrompt (Ours)** | | | | | |
| distilGPT-2 | 57.3 (1.7) | 96.5 (0.1) | 85.3 (1.3) | 46.0 (0.9) | 77.9 (0.4) |
| GPT-2-small | 60.0 (0.4) | 96.4 (0.3) | 89.0 (2.8) | 50.7 (1.3) | 80.1 (0.8) |
| GPT-2-medium | 65.7 (1.4) | 95.2 (1.2) | 89.3 (0.1) | 56.1 (1.0) | 82.3 (0.4) |
| GPT-2-large | 65.1 (1.8) | 94.6 (2.3) | 91.6 (0.8) | 56.5 (1.3) | 82.6 (0.7) |
| GPT-2-xl | 72.1 (1.5) | 94.2 (2.4) | 89.5 (0.5) | **61.4** (2.2) | **84.7** (1.0) |

モデルアーキテクチャやタスク（分類対生成）を変えてもRLPromptは機能する。テキストスタイル変換のような生成タスクでも、ゼロショットで適切なプロンプトを発見し、最高峰のファインチューニングモデル(DiRR)以上の性能を発揮した。

**【筆者の見解・考察】**
*   **ゼロショット生成タスクへの適応性**: スタイル変換（TST）のような、並行コーパスを持たない教師なし生成タスクにおいても、RLPromptが極めて有効であることが示されています。
*   **モデルスケーリングの効果**: GPT-2のサイズを小規模から特大（XL）へと拡大させるに伴い、RLPromptを用いて発見されたプロンプトの効果も綺麗にスケールしています。これは、RLPromptが「タスクを適切に制御するトリガー」を確実に探し当てており、LMsが大きいほどそのトリガーに強く従うというメカニズムを証明しています。

### 図版についての考察

![Figure 1: Comparison between typical existing prompt optimization frameworks and our framework](./images/figure-1.png)

**【筆者の見解・考察】**
*   **勾配バックプロパゲーションの回避**: 従来手法（左側のSoft Tuning等）は巨大なLLMの内部を逆伝播（赤い矢印）が通過するため、計算リソースの枯渇やブラックボックスAPIへの不適合をもたらしますが、RLPrompt（右側）は更新の対象を別建ての「小規模なMLP層」に完全に隔離しているため、メインのLLMは一切の勾配計算なしの完全な推論モードで使用できるという技術革新を分かりやすく提示しています。

![Figure 2: Overview of RLPrompt for discrete prompt optimization](./images/figure-2.png)

**【筆者の見解・考察】**
*   **強化学習によるフィードバックループの完成**: LLMは環境（Environment）として機能し、テキストとその評価（Reward）のみを生成器（Policy）へ返します。タスク固有の「教師データ」の代わりに独自設計の「Reward関数」を使うことで、分類スコアだろうとテキストの流暢性だろうと、自由自在にLLMの出力を最適化できる「汎用的フレームワーク」として完成していることを図説しています。

### 「意味不明な文字列」の発見とモデル間の高い転移性
本研究の最も興味深い洞察の一つは、最適化の結果生成されるプロンプト自体にある。RLPromptが探索空間から選び出したプロンプトの多くは、文法的に破綻しており、人間からすると「意味不明（Gibberish）」なテキストへと収束していた（例：SST-2タスクにおいて `Absolutely VERY absolute VERY absolute [MASK]` など）。

#### Table 18: Performance of strong words combinations
| Template | RoBERTa | GPT-2 |
| :--- | :--- | :--- |
| **SST-2** | | |
| `<S>` downright `[MASK]` . | 80.6 | 86.7 |
| `<S>` Really downright `[MASK]` . | 90.4 | 89.1 |
| `<S>` Absolutely `[MASK]` . | 91.7 | 87.8 |
| `<S>` AbsolutelyAbsolutely `[MASK]` . | 89.2 | 72.3 |
| `<S>` Absolutely VERY absolute VERY absolute `[MASK]` . | 92.7 | 73.8 |
| **AG's News** | | |
| `[MASK]` Reviewer `<S>` | 74.5 | --- |
| `[MASK]` Reviewer Stories `<S>` | 81.0 | --- |
| `[MASK]` StaffInformationStatement `<S>` | 76.8 | --- |
| `[MASK]` StaffInformationStatement Reviewer Stories `<S>` | 79.8 | --- |

**【筆者の見解・考察】**
*   **言語モデルが解釈する「自然言語」の異質性**: `Absolutely VERY absolute VERY absolute` のように、人間にとっては文法的に崩壊している「意味不明（Gibberish）」なテキストが、人間が書いた流暢な英語よりも高い精度を叩き出しています。筆者らは、LLMが理解するタスクのトリガー表現（プロンプトの本質）は、人間が扱う自然言語の文法や意味論に必ずしも縛られない「独自の潜在的なパターン」であると考察しています。
*   **モデル間で共有されるユニバーサルトリガー**: さらに重要かつ驚くべき点として、DistilGPT-2を用いたRLにより探索されたこのGibberishなプロンプトを、アーキテクチャや訓練データが異なる RoBERTa に直接入力しても高いパフォーマンスを維持（転移）できることを発見しました。これは「LMsは事前学習を通じ、人間には解読できない言語横断的・モデル横断的な共通のトリガー空間を獲得している」という極めて興味深い洞察を与えています。

しかし、人間にとっては意味不明でも、モデルに対するタスクパフォーマンスは人間が構築した「自然な英語のプロンプト」よりも遥かに高かった。さらに驚くべきことに、これらの「意味不明なプロンプト」は、GPT-2などで学習された後、RoBERTaなどの全くアーキテクチャの異なる言語モデルに入力した際にも、高次元で性能を維持できる（互換性がある）ことが明らかになった。
これらの結果は、LLMがプロンプトからタスクの意図を汲み取るプロセスが、人間の「自然言語の読み取り方法」とは本質的に異なっており、内部表現において何らかの「言語モデル共通のトリガーとなるパターン」を獲得している可能性を示唆している。
