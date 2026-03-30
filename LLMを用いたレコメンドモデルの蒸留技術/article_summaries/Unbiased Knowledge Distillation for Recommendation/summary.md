# Unbiased Knowledge Distillation for Recommendation

## 背景

### 知識蒸留（KD）の利点とその落とし穴
大規模な推薦モデルは推論時の遅延を引き起こすため、知識蒸留（KD）により知識を軽量な学生モデルへと転移させるアプローチが一般的です。しかし、既存のKD手法を推薦システムに適用すると、「**人気アイテムへの推薦スコアが過剰に強化され、マイナーな（非人気の）アイテムの推薦精度が致命的に低下する**」という深刻な「人気度バイアス」の増幅問題があることが判明しました。

### 因果推論グラフが明かすバイアスの発生源（Figure 2）
著者らは、このバイアス問題の根本原因を特定するために、因果推論グラフを用いて知識蒸留のプロセスを分析しました。

![Figure 2: The causal graph to describe the knowledge distillation. U: user, I: item, M affinity score, Z item popularity, Y: soft label, S: student. The bias origins from the causal effect of Z on Y. Our UnKD is intended to cut off Z-> Y. Admittedly, there may exist other causal paths from U, I to S, but here we only focus on the causal effect through distillation (ie via Y).](./images/causal_bias.png)

**【結果と考察】**: 推薦蒸留のパイプラインを因果推論グラフで表現したものです。従来の知識蒸留（KD）における最大の問題は、アイテムの人気度（$Z$）が、本来のユーザーの好み（$M$）による純粋な親和性とは無関係に、直接的に教師モデルのスコア（$Y$）へ干渉してしまうパス（$Z \to Y$）が存在している点だと筆者らは定義しています。

グラフにおける各変数は以下の関係を示しています：
* **$I$ (Item)**: 推薦候補となる特定のアイテム
* **$Z$ (Popularity)**: そのアイテムの世間的な人気度
* **$Y$ (Soft Label)**: 教師モデルが出力する推薦スコア（ソフトラベル）

理想的な推薦スコアは、$U$（ユーザー）と$I$（アイテム）の間の純粋な親和性（$M$）によって決まるべきです。しかし現実には、**アイテム自身の人気度（$Z$）が直接的に教師モデルの予測スコア（$Y$）を無意識に引き上げてしまう**という因果的な影響を与えています。これが図中の「**$I \to Z \to Y$ のパス**」です。

知識蒸留では、学生モデルは教師が出力したこのスコア（$Y$）を絶対的な正解としてそのまま丸暗記してしまいます。つまり、教師モデルが「人気アイテムだから」と割り当てた不当に高い評価（バイアス）を、学生モデルがそっくりそのまま学習モデルの中に取り込んでしまうことが、バイアス悪化の元凶であると同定されました。

### 本研究のアプローチとモチベーション
実際のテストデータ分布と比較して、現状の教師モデルの予測はすでに過剰に人気アイテムに偏っています（Figure 1）。

![Figure 1: Ratios of popular/unpopular items in the top-10 recommendation lists from a MF model. We also present the ideal ratios from the test data for comparison.](./images/Figure_result_ratio.png)

**【結果と考察】**: 通常の教師モデル（MF等）を使って生成した推薦リストでは、実際のデータ分布（Test data）と比べて、人気アイテムが極端に多く推薦され、非人気アイテムがほとんど推薦されないという激しい偏りがあることを示しています。この過酷な初期状態が、後段の知識蒸留においてバイアスをさらに悪化させる根本的な原因であると筆者らは推察しています。

しかし、複雑な構造や学習設定を持つ教師モデル自体のプロセスにDebias（バイアス緩和）処理を組み込むことは、精度低下のリスクや最適化の難しさを伴います。

そこで著者らは、**教師モデルの内部構造には一切干渉せず、学生への蒸留段階でのみ人気度バイアスのパス（$Z \to Y$）を遮断・相殺できる、完全に新しい（Teacher-agnostic な）知識蒸留手法**が必要であると考え、本研究の動機としました。

## 手法
著者らは因果推論に基づき、バイアス要因となる「人気度（Popularity）」の影響を相殺する手法「**UnKD (Unbiased Knowledge Distillation)**」を提案しました（Figure 3）。

![Figure 3: We cut off Z-> Y during distillation.](./images/causal_debias.png)

**【結果と考察】**: 提案手法「UnKD」のコンセプト図です。事前のデータ操作や複雑な教師モデル自体の再構築という困難なアプローチを避けるため、下流の「蒸留プロセス（$Y \to S$）」の段階においてアイテムの人気度に基づくグループ化処理を挟むことで、因果関係上における $Z \to Y$ のバイアスパスの影響を効果的に切り落とし（Cut off）、純粋な $M$（ユーザーとの真の親和性）だけをクリーンに転移させる理論的枠組みを示しています。

UnKDは因果グラフ（Figure 2）において以下の効果推定に基づいています：
- **TE (Total Effect)**: アイテムがソフトラベルに与える全体効果 $\text{TE}_i = Y_i|u - Y_{i^*}|u$
- **PEZ (Path-specific Effect through Z)**: 「人気度」を通じたバイアス効果 $\text{PEZ}_i = Y_{i^*, Z_i}|u - Y_{i^*}|u$
- **PEM (Path-specific Effect through M)**: ユーザーの純粋な親和性を通じた真の推薦効果 $\text{PEM}_i = \text{TE}_i - \text{PEZ}_i = Y_i|u - Y_{i^*, Z_i}|u$

UnKDは、この「PEM」に近似するクリーンな情報を抽出するため、以下の**グループ単位のサンプリングと学習（Group-wise Learning）**を行います：

![Figure 4: Illustrations of (a) the traditional knowledge distillations and (b) our proposed UnKD. UnKD partitions items into multiple groups according to their popularity, and then extracts the ranking knowledge among each group to learn the student.](./images/Last_Model.png)

**【結果と考察】**: UnKDの具体的なシステムアーキテクチャ図です。全アイテムを単一のプールで扱う従来の知識蒸留（a）とは異なり、UnKD（b）ではアイテムの人気度スコアに基づき独立した $K$ 個のグループに分割・制限した上でサンプリングと損失計算を行います。筆者らは、この単純なグループ化によって「同一グループ内では人気度差がほぼゼロ（$Z_i - Z_j \approx 0$）となり、教師スコアの差分が純粋な好みのみを反映する」という性質を利用し、実装が非常に軽量かつ堅牢（Teacher-agnostic）なバイアス除去手法を完成させています。

### 1. グループ分割 (Group Partition)
全アイテムをあらかじめその人気度順にソートし、それぞれのグループ Popularity の合計が均等になるように $K$ 個のグループ（$\mathcal{G}$）に分割します。
この処理の最大の意義は、**同一グループ内に振り分けられたアイテム同士は人気度がほぼ等しい（$Z_i \approx Z_j$）**とみなせる状態を作ることです。これによって後のステップで比較する際に「人気度バイアスの影響」が相殺され、純粋にユーザーの嗜好（PEM）だけでアイテムを比較できるクリーンな土台を用意します。

### 2. グループ内サンプリング (Group-wise Sampling)
作成した各グループ $g \in \mathcal G$ の中で独立してサンプリングを行います。ここで**「教師モデルの知識」が正例と負例の選定（ペア作り）に直接利用されます**。
具体的には、教師モデルが出力した予測スコア（ソフトラベル）に基づき、同じ人気度グループ内での相対的なランキングを決定します。このランキングから、教師がより高く評価したアイテム（正例 $i^+$）と、低く評価したアイテム（負例 $i^-$）のペア $(i^+, i^-)$ を確率的に抽出します。この段階で、ペアは「**世間的な人気度は全く同じだけど、教師モデルの知識において明確な優劣（好み）の差が存在するペア**」に確定します。

### 3. グループ内学習 (Group-wise Learning) と 蒸留損失 $\mathcal{L}_G$
サンプリングしたペア情報を用いて、学生モデルを最適化します。ここで用いるのが、本手法の中核であり人気度バイアス回避の要となる**グループ内蒸留損失 $\mathcal{L}_G$** です。

$$ \mathcal{L}_{G} = -\sum_u{\frac{1}{|\mathcal{U}|}\sum_{g\in \mathcal G}\sum_{(i^+,i^-)\in \mathcal{S}_{ug}} \log\sigma(\textbf{e}_{u}^T \textbf{e}_{i^{+}}-\textbf{e}_{u}^T \textbf{e}_{i^{-}})} $$
$$ \mathcal{L} = \mathcal{L}_{R} + \lambda \mathcal{L}_{G} $$
（$\mathcal{L}_R$ は正解データからの通常の教師あり損失、$\lambda$ はバランスをとる重み係数、$\sigma$ はシグモイド関数、$\textbf{e}_u$ と $\textbf{e}_i$ は学生モデルの特徴ベクトル）

従来の知識蒸留では、教師モデルが出力した絶対的なスコア値（例: 0.85）をそのまま学生モデルにコピーさせます。しかしそれだと、人気アイテムに与えられた過大評価（バイアスの下駄）も丸ごと学生に学習させてしまいます。注目すべきは、**この $\mathcal{L}_G$ の数式自体の変数には「教師モデルの出力値」が直接登場しない**という点です。

代わりに、この数式（BPR損失ベース）は**「引き算（$\textbf{e}_{u}^T \textbf{e}_{i^{+}} - \textbf{e}_{u}^T \textbf{e}_{i^{-}}$）を通して、同じグループ内で $i^-$ よりも $i^+$ の方の予測スコアを高くさせる」** ことしか行いません。

前ステップのサンプリングにおいて、どのアイテムを $i^+$ に設定するかの決定権は完全に教師モデルの知識に依存しています。同じ人気度の条件で教師モデルが $i^+$ をより高く評価したということは、そこには人気度バイアスが存在せず、純粋なユーザーとの親和性（PEM）が反映されていると断言できます。
すなわちこのステップは、スコア数値を近似させるのではなく、**「人気度の影響が相殺された空間内で、『教師モデルがデータセットの中からどのアイテムを正負のペアとして選定したか』というサンプリング結果を通して、間接的に教師の”真のランキング知識”を学生に教え込む」**という非常にエレガントな構造になっています。

## 結果

結論として、UnKDは人気度バイアスの悪影響を遮断し、推論の公平性と全体の正確性を同時に向上させました。

![Figure 5: The relative improvements (wrt recall@10) of KDs over the baseline that directly trained from the dataset. Here we visualize the results in terms of popular and unpopular group, respectively.](./images/Figure_base_group_2.png)

**【結果と考察（RQ1）】**: ベースラインモデルに対する知識蒸留（KD）手法群の相対的な性能向上率を、人気アイテムグループ（Popular）と非人気アイテムグループ（Unpopular）別に比較プロットした結果です。従来のKD手法（赤線など）は人気アイテムへの推薦力を過剰に高める一方で、非人気アイテムの精度をマイナスへと叩き落としています（バイアスの悪化）。対してUnKD（青星）は、人気アイテムの過剰な最適化を防ぎつつ、非人気アイテムの精度向上率を他の手法から圧倒的に引き離しており（最大100%以上の向上の乖離）、モデル全体での「公平な知識転移」が達成できていることが明確に示されています。

![Figure 6: Performance comparison with varying K.](./images/Figure_mf_group.png)

**【結果と考察（RQ3）】**: アイテムを分割するグループ数（$K$）の変化が、最終的なレコメンド性能に与える影響の分析結果です。筆者の考察によれば、$K$ を増やすほど1グループ内のアイテム間の人気度差が小さくなり、蒸留による因果的バイアスが理論的に相殺されやすくなります（非人気アイテム側の精度上昇要因）。しかし、$K$ が過大になると各グループに属するアイテム数が激減してしまい、サンプリングされる正例・負例のペア数が不足し、学習に必要なランキング知識そのものが失われてしまいます。このため「バイアス減少」と「情報量の維持」の間にトレードオフが発生し、実験的に $K=4$ または $5$ 付近が推薦パラメーターにおける最適解となることが実証されました。

**Table 1: Performance (Recall@10) comparison of various knowledge distillation methods in terms of popular/unpopular items on three real-world datasets.**

| Dataset | Metric | Student | Teacher | RD | CD | DERRD | HTD |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Movielens | Popular | 0.2156 | 0.2565 | 0.2237 | 0.2258 | 0.2315 | 0.2228 |
| Movielens | Group | --- | +18.97% | +3.75% | +4.73% | +7.37% | +3.33% |
| Movielens | Unpopular | 0.0250 | 0.0517 | 0.0242 | 0.0179 | 0.0113 | 0.0187 |
| Movielens | Group | --- | +106.80% | -3.20% | -28.40% | -54.80% | -25.20% |
| Apps | Popular | 0.1031 | 0.1448 | 0.1144 | 0.1212 | 0.1058 | 0.1195 |
| Apps | Group | --- | +40.44% | +10.96% | +17.55% | +2.61% | +15.90% |
| Apps | Unpopular | 0.0109 | 0.0164 | 0.0098 | 0.0090 | 0.0098 | 0.0061 |
| Apps | Group | --- | +50.45% | -10.09% | -17.43% | -10.09% | -44.03% |
| CiteULike | Popular | 0.0831 | 0.1294 | 0.0910 | 0.0887 | 0.0899 | 0.0885 |
| CiteULike | Group | --- | +55.71% | +9.50% | +6.73% | +8.18% | +6.49% |
| CiteULike | Unpopular | 0.0095 | 0.0537 | 0.0085 | 0.0088 | 0.0075 | 0.0068 |
| CiteULike | Group | --- | +465.26% | -10.52% | -7.36% | -21.05% | -28.42% |

**【結果と考察（RQ1の核心）】**: 人気/非人気アイテムごとのTop-10 Recallの詳細比較です。結果として、通常のKD手法群（RD, CD等）が非人気アイテムグループ（Unpopular）に対して軒並みマイナス成長（学生単体で学習した場合よりも精度が低下）を記録する中、UnKDのみが全3データセットにおいて大幅なプラス成長（CiteULikeでは他手法が-10〜20%台なのに対し UnKDは +465% という圧倒的成長）を記録しました。筆者はこれを、UnKDが人気度バイアスに汚染された教師スコアから、真にユーザーが望む順位知識だけを救い出すことに成功した決定的な証拠であると論じています。

**Table 2: Statistics of the datasets.**

| dataset | Users | Items | Interactions | Sparsity |
| :--- | :--- | :--- | :--- | :--- |
| CiteULike | 5219 | 25181 | 125580 | 99.91% |
| Apps | 3898 | 11797 | 128105 | 99.73% |
| MovieLens | 6040 | 3706 | 1000209 | 95.54% |

**【結果と考察】**: 実験に使用された3つの実世界データセット（CiteULike, Apps, MovieLens）の統計情報です。スパース性（Sparsity）が95%〜99.9%と非常に高く、このようなアイテム間のインタラクション頻度が極端に偏っている（典型的なロングテール分布を持つ）過酷な実環境データにおいて、提案手法（UnKD）が実際のサービス同様の厳しい条件下でも頑健にバイアスへ対処し、機能するかどうかを検証するために選定されています。

**Table 3: Overall performance comparison between our method and baselines. All metrics are based on the top-10 results. where the best performance is bold and the second best underlined.**

| Dataset | Backbone Model | Method | BPRMF Recall | BPRMF NDCG | LightGCN Recall | LightGCN NDCG |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MovieLens | BPRMF/LightGCN | Teacher | 0.1810 | 0.2951 | 0.1850 | 0.3012 |
| MovieLens | BPRMF/LightGCN | Student | 0.1435 | 0.2511 | 0.1456 | 0.2581 |
| MovieLens | BPRMF/LightGCN | RD | 0.1473 | 0.2559 | 0.1471 | 0.2583 |
| MovieLens | BPRMF/LightGCN | CD | 0.1445 | 0.2534 | 0.1477 | 0.2602 |
| MovieLens | BPRMF/LightGCN | DERRD | 0.1436 | 0.2532 | 0.1487 | 0.2606 |
| MovieLens | BPRMF/LightGCN | HTD | 0.1441 | 0.2539 | 0.1472 | 0.2592 |
| MovieLens | BPRMF/LightGCN | UnKD | 0.1547 | 0.2615 | 0.1569 | 0.2672 |
| MovieLens | BPRMF/LightGCN | impv-e% | +5.02% | +2.18% | +5.51% | +2.53% |
| Apps | BPRMF/LightGCN | Teacher | 0.0991 | 0.0760 | 0.1007 | 0.0782 |
| Apps | BPRMF/LightGCN | Student | 0.0719 | 0.0539 | 0.0811 | 0.0643 |
| Apps | BPRMF/LightGCN | RD | 0.0768 | 0.0596 | 0.0831 | 0.0647 |
| Apps | BPRMF/LightGCN | CD | 0.0790 | 0.0608 | 0.0848 | 0.0658 |
| Apps | BPRMF/LightGCN | DERRD | 0.0729 | 0.0562 | 0.0832 | 0.0648 |
| Apps | BPRMF/LightGCN | HTD | 0.0732 | 0.0561 | 0.0833 | 0.0652 |
| Apps | BPRMF/LightGCN | UnKD | 0.0853 | 0.0644 | 0.0867 | 0.0678 |
| Apps | BPRMF/LightGCN | impv-e% | +7.97% | +5.92% | +2.24% | +3.04% |
| CiteULike | BPRMF/LightGCN | Teacher | 0.1518 | 0.1016 | 0.1657 | 0.1139 |
| CiteULike | BPRMF/LightGCN | Student | 0.0760 | 0.0477 | 0.0783 | 0.0510 |
| CiteULike | BPRMF/LightGCN | RD | 0.0808 | 0.0514 | 0.0833 | 0.0538 |
| CiteULike | BPRMF/LightGCN | CD | 0.0801 | 0.0518 | 0.0936 | 0.0616 |
| CiteULike | BPRMF/LightGCN | DERRD | 0.0793 | 0.0511 | 0.0809 | 0.0527 |
| CiteULike | BPRMF/LightGCN | HTD | 0.0788 | 0.0485 | 0.0958 | 0.0628 |
| CiteULike | BPRMF/LightGCN | UnKD | 0.0863 | 0.0550 | 0.1006 | 0.0654 |
| CiteULike | BPRMF/LightGCN | impv-e% | +6.80% | +6.17% | +5.01% | +4.14% |

**【結果と考察】**: BPRMFおよびLightGCNをバックボーン（骨格）モデルとした場合の、モデル全体の総合推薦性能比較です。「バイアス除去に特化すると、モデル全体の総合的な推薦精度そのものは落ちてしまう」というトレードオフが一般的に知られていますが、UnKDは人気度バイアスを是正しつつ、全体スコア（Recall / NDCG）においてもすべての比較手法を打ち破りSOTA（最高性能）を達成しています。筆者はこれを「非人気アイテムの埋もれていた正解（真の好み）を大幅に掘り起こせたことが、結果的にシステム全体の精度底上げにも大きく貢献したためである」と鮮やかに結論づけています。

**Table 4: Performance comparison (recall@10) between our UnKD and the baselines that leverages debiasing technique in model training.**

| Backbone Model | Method | MovieLens Overall | MovieLens Popular | MovieLens Unpopular | Apps Overall | Apps Popular | Apps Unpopular | CiteULike Overall | CiteULike Popular | CiteULike Unpopular |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BPRMF | Student | 0.1435 | 0.2156 | 0.0250 | 0.0719 | 0.1031 | 0.0109 | 0.0760 | 0.0831 | 0.0095 |
| BPRMF | CD | 0.1445 | 0.2258 | 0.0179 | 0.0790 | 0.1212 | 0.0090 | 0.0801 | 0.0887 | 0.0088 |
| BPRMF | PD-CD | 0.1454 | 0.2205 | 0.0210 | 0.0795 | 0.1176 | 0.0113 | 0.0805 | 0.0890 | 0.0092 |
| BPRMF | HTD | 0.1441 | 0.2228 | 0.0187 | 0.0732 | 0.1195 | 0.0061 | 0.0788 | 0.0885 | 0.0068 |
| BPRMF | PD-HTD | 0.1443 | 0.2150 | 0.0263 | 0.0808 | 0.1240 | 0.0076 | 0.0798 | 0.0897 | 0.0073 |
| BPRMF | UnKD | 0.1547 | 0.2205 | 0.0311 | 0.0853 | 0.1274 | 0.0147 | 0.0863 | 0.0854 | 0.0208 |
| LightGCN | Student | 0.1456 | 0.2280 | 0.0228 | 0.0811 | 0.1242 | 0.0093 | 0.0783 | 0.0885 | 0.0080 |
| LightGCN | CD | 0.1477 | 0.2316 | 0.0169 | 0.0848 | 0.1310 | 0.0091 | 0.0936 | 0.1067 | 0.0081 |
| LightGCN | PD-CD | 0.1496 | 0.2369 | 0.0172 | 0.0851 | 0.1308 | 0.0095 | 0.0942 | 0.1020 | 0.0110 |
| LightGCN | HTD | 0.1472 | 0.2328 | 0.0079 | 0.0833 | 0.1291 | 0.0091 | 0.0958 | 0.1093 | 0.0085 |
| LightGCN | PD-HTD | 0.1485 | 0.2364 | 0.0159 | 0.0835 | 0.1288 | 0.0093 | 0.0979 | 0.1102 | 0.0128 |
| LightGCN | UnKD | 0.1569 | 0.2384 | 0.0292 | 0.0867 | 0.1325 | 0.0118 | 0.1006 | 0.1076 | 0.0162 |

**【結果と考察（RQ2）】**: 「教師モデル自体を事前にDebias（バイアス除去）学習させた場合（PD-CD, PD-HTDなど）」と、「普通の教師モデルを使い、蒸留時に初めてDebiasを行う提案手法（UnKD）」との直接比較です。結果として、上流に干渉して懸命にDebiasを試みるよりも、下流の蒸留段階でUnKDを用いた方が、人気アイテムに対する極端な精度低下を防ぎながら、全体性能および非人気アイテムの精度で最終的に上回る結果となりました。
ここから筆者は、「教師モデルの構造や学習最適化パラメーターに依存せずに『クリーンな知識の抽出』のみに専念できる Teacher-agnostic（教師非依存）な UnKD のアプローチこそが、複雑化する現代の推薦モデル設計において最も実用的で優れた解決策である」と総括しています。
