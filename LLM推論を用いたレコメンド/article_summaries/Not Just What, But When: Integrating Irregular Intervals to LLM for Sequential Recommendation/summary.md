# Not Just What, But When: Integrating Irregular Intervals to LLM for Sequential Recommendation

## 背景
逐次推薦（Sequential Recommendation）において、既存の手法（GRU4RecやSASRecなど）は主としてアイテムの系列のみに着目し、アイテムとアイテムの間に生じる「時間的間隔（インターバル）」が静的であると仮定して無視する傾向にあった。しかし、動的なインターバルはユーザーの行動パターンや嗜好の推移（Preference drift）を捉えるための重要な要素である。
論文では、図1に示すように、同じアイテムの購入履歴であっても、購入間隔が異なればアイテムの影響や意図が異なることを指摘している。また、既存研究はユーザーやアイテムの視点からコールドスタート問題を扱ってきたが、「インターバル（時間間隔）の視点」から見たコールドスタート（行動履歴の間隔が長いユーザー）という新しい課題が重要であることを提唱している。

![Examples of purchase histories for two users.](./images/hypo_1_2.png)
*Figure 1: Examples of purchase histories for two users.*

## 手法
提案手法である **IntervalLLM** は、図2に示すように、時間間隔の情報をLLMベースのレコメンドモデルに直接統合するフレームワークである。
主に以下の要素から構成される。

1. **アイテムとインターバルの埋め込み表現**:
   LLMへの入力として、アイテム系列 $X=(x_1, \dots, x_n)$ とそれに対応する時間間隔 $Z=(0, z_1, \dots, z_{n-1})$ を別々の埋め込み層から取得する。
   $$ x_{k} = ItemEMB(i_k) $$
   $$ z_{k-1} = IntervalEMB(t_{k-1}) $$

2. **インターバル注入アテンション (Interval-Infused Attention; IIA)**:
   時間間隔の情報を単に加算するのではなく、アイテムとインターバルの重要性を別々に捉えるためのアテンション機構（IIA）を導入した。
   クエリとして、時間情報を入力する。  
   $$ Q_{z} = ZW^{Q_z}, K_{x} = XW^{K_x}, V_{x} = XW^{V_x} $$
   $$ IIA(X, Z) = \mathrm{softmax}\left(\frac{Q_zK_x^T}{\sqrt{d_q}}+M\right)V_x $$
   これにより、時間的な関係性を保持したアイテム表現 $\hat{x}_k$ を学習する。

3. **Optionalized Prompt (選択形式プロンプト)**:
   生成タスクとしての曖昧さ（アイテム名の完全一致の難しさや綴り間違い）を排除するため、候補アイテムにA, B, C...といった選択肢ラベルを付与し、LLMにアルファベット1文字を出力させる「選択式」のタスクとして指示チューニング（Instruction Fine-tuning）を行っている。モデル全体はLoRAを用いてファインチューニングされる。
   ※ 本モデルの適用はランダムアイテムからのサンプリング(rerankerとしての運用)に限られる。  

![The proposed IntervalLLM](./images/model.png)
*Figure 2: The proposed IntervalLLM. All LLM parameters except for those in LoRA are frozen.*

## 結果
論文では3つのベンチマークデータセットを用いて実験を行っている（Table 1）。

**Table 1: Dataset characteristics.**

| Dataset | #User | #Item | #Interaction | Density |
| :--- | ---: | ---: | ---: | ---: |
| Video Games | 94,762 | 25,612 | 814,586 | 8.59 |
| CDs and Vinyl | 123,876 | 89,370 | 1,552,764 | 12.53 |
| Books | 776,370 | 495,063 | 9,488,297 | 12.22 |

全体的な性能（Table 2）において、提案手法の IntervalLLM は既存の伝統的手法や LLM ベースの手法を一貫して上回り、平均して 4.4% の性能向上を達成している。

**Table 2: Overall performance with Hit Rate@1 ($\uparrow$) on three datasets.**

| Category | Method | Video Games | CDs and Vinyl | Books |
| :--- | :--- | :--- | :--- | :--- |
| Traditional | GRU4Rec | 49.0% | 46.5% | 35.7% |
| | SASRec | 50.8% | 50.9% | 38.0% |
| Traditional + Interval | TiSASRec | 52.9% | 54.1% | 58.6% |
| LLM-based | LLaMA | 56.0% | 45.2%* | 60.2% |
| | LLaRA | 50.5% | 49.6%* | 60.0%* |
| LLM-based + Interval | LLaMA + Interval | 56.3% | 48.7% | 61.1% |
| | IntervalLLM (Ours) | **61.7%** | **55.4%** | **61.9%** |

アブレーションスタディ（Table 3）により、時間情報を単にテキスト（タイムスタンプ）として入力したり、埋め込みとして加算（$IntervalEMB$）するだけよりも、提案するインターバル注入アテンション（$IIA$）を組み合わせた構成が最も性能（61.7%）を引き出せることが確認された。

**Table 3: Ablation study of IntervalLLM on the Video Games dataset.**

| LLaMA | Interval | $IntervalEMB$ | $IIA$ | Hit Rate@1 ($\uparrow$) |
| :--- | :--- | :--- | :--- | :--- |
| ✓ | ✗ | ✗ | ✗ | 56.0% |
| ✓ | $\triangle$ | ✗ | ✗ | 54.2% |
| ✓ | ✓ | ✗ | ✗ | 56.3% |
| ✓ | ✓ | ✓ | ✗ | 56.8% |
| ✓ | ✓ | ✓ | ✓ | **61.7%** |

さらに、Table 4では提案する「インターバルの視点」を含むコールドスタートシナリオでの検証結果を示している。
既存の手法では「インターバルコールド（購入間隔が非常に長い状況）」において性能が著しく低下（最大で-28.0%など）するが、IntervalLLM は全体の性能が高水準であると同時に、ウォーム・コールド間の性能劣化（Diff.）を小さく抑制しており、時間間隔の適切なモデリングが推薦の頑健性に寄与していることが裏付けられた。

**Table 4: Performance on Warm/Cold scenarios evaluated by Hit Rate@1 ($\uparrow$) on the Video Games dataset.**

| Method | User Perspective: Warm ($\uparrow$) | User Perspective: Cold ($\uparrow$) | User Perspective: Diff. | Item Perspective: Warm ($\uparrow$) | Item Perspective: Cold ($\uparrow$) | Item Perspective: Diff. | Interval Perspective: Warm ($\uparrow$) | Interval Perspective: Cold ($\uparrow$) | Interval Perspective: Diff. | Overall ($\uparrow$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GRU4Rec | 49.3% | 48.8% | -1.0% | 53.3% | 45.1% | -15.4% | 55.2% | 43.7% | -20.8% | 49.0% |
| SASRec | 52.2% | 50.1% | -4.0% | 54.7% | 47.4% | -13.3% | 57.4% | 45.2% | -21.2% | 50.8% |
| TiSASRec | 55.0% | 52.3% | -4.9% | 54.3% | 51.0% | -6.1% | 54.6% | 49.1% | -10.1% | 52.9% |
| LLaMA | 56.5% | 55.8% | -1.2% | 58.8% | 53.7% | -8.7% | 61.1% | 51.8% | -15.2% | 56.0% |
| LLaRA | 51.6% | 50.0% | -3.1% | 54.0% | 46.9% | -13.1% | 60.3% | 43.3% | -28.0% | 50.5% |
| LLaMA + Interval | 56.1% | 56.2% | +0.2% | 59.1% | 53.8% | -9.0% | 60.6% | 53.3% | -12.0% | 56.3% |
| IntervalLLM (Ours) | **61.6%** | **61.8%** | +0.3% | **64.4%** | **59.5%** | -7.6% | **65.6%** | **59.1%** | -9.9% | **61.7%** |
