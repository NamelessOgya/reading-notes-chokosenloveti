# Learning With Generalised Card Representations for “Magic: The Gathering”

## 背景
カードゲーム（特にコレクティブルカードゲーム）において、ユーザーが現在所持しているカードプール（コンテキスト）に最適なカードを選ぶ「ドラフト（デッキ構築）」は、高度なコンテキスト依存の好みのランク付け問題（Contextual Preference Ranking）として定式化される。
従来、このような問題は人間が選択した行動の履歴（あるカードプールに対して、提示された選択肢の中から1枚を選んだ履歴）を基に、Siamese Neural Networkを用いたTriplet Lossによって学習されてきた。しかし、1つの正例に対して非常に多くの負例が存在するため、サンプルの不均衡やオンラインでのTriplet生成（mining）に伴う計算コストの増大、学習の不安定さが課題であった。
一方、画像と自然言語など異種モーダル間の表現学習で大きな成功を収めているCLIPのInfoNCE Lossは、バッチ内のすべての組み合わせを比較することで非常に効率的な対照学習（Contrastive Learning）を可能にする。しかし、InfoNCE Lossは任意のアイテム同士が比較可能であるという前提に立っており、カードのドラフトのように「実際に提示された選択肢（パック）の中にないカード」とは比較が定義できず、またバッチ内に複数の正当なペアが混在しうる領域では、単純に適用すると性能が劣化するという問題があった。
本研究では、このInfoNCE Lossに「マスク処理」を導入することで、限られたコンテキスト下での暗黙的な選好比較問題にCLIPのスケーラビリティを適用できるようにする拡張モデルを提案している。

## 手法
著者は、カードプール $\mathcal{C}$ に対するカードの好み（Contextual Preference）を学習するため、Triplet Lossに代わり、CLIPの「Contextual InfoNCE Loss」を提案した。

まず、好みは通常、効用関数 $u$ を用いて以下のように定式化される。

$$
u(\mathbf{o}_1) > u(\mathbf{o}_2) \Leftrightarrow \mathbf{o}_1 \succ \mathbf{o}_2
$$

従来のSiamese Neural Networkを用いたアプローチでは、カードプール $\mathcal{C}$ をアンカー $\mathbf{a}$、選ばれたカードを正例 $\mathbf{p}$、選ばれなかったカードを負例 $\mathbf{n}$ とし、距離尺度 $d$ に基づくTriplet Lossを用いて最適化を行っていた。

$$
L_{\text{triplet}}(\mathbf{a},\mathbf{p},\mathbf{n}) = \max(d(\mathbf{a},\mathbf{p})-d(\mathbf{a},\mathbf{n}) + m, 0)
$$

また、距離は推移的であることを利用して任意のアイテムセットのランク付けを行っていた。

$$
(\mathbf{c}_j \succ \mathbf{c}_k \mid \mathcal{C}) \land (\mathbf{c}_k \succ \mathbf{c}_l \mid \mathcal{C}) \Rightarrow (\mathbf{c}_j \succ \mathbf{c}_l \mid \mathcal{C})
$$

対して、標準的なInfoNCEでは以下のような一対一関係が仮定されているが、カードゲーム等では同じバッチ内に同一のカードが複数登場するため、この仮定が成立しない。

$$
\forall i \in [0,N] \not \exists j \in [0,N]: \text{sim}(I_i,T_i) > \text{sim}(I_i, T_j), i \neq j
$$

そこで提案手法である「Adapted InfoNCE Loss (Contextual InfoNCE)」では以下の工夫を行った。
1. **比較可能な対象のマスキング**: $N \times M$（$N$：サンプル数、$M$：ユニークな全カード数）の類似度行列を計算したのち、実際にそのターンの選択肢（パック）として提示されたカードのみを計算対象とするためのマスクを適用する。選ばれた正解カードの位置を1、提示されたが選ばれなかったカードを0、提示されなかったカードを-1にし、損失計算においては提供されなかったカードを無視する。
2. **列方向の損失計算のオミット**: 画像と自然言語のような一対一の組とは異なり、同一カードが別のカードプールに関する異なるサンプルの正例となる可能性がある。そのため、列（カード）方向でのCross Entropy計算を除外し、行（プール）方向のみで損失を計算して最適化する。

ネットワーク構成としては、カードの特徴量（属性値、BERTによるテキスト埋め込み、画像オートエンコーダの潜在表現の結合）を処理する「Card encoder」と、すでに選ばれたカード群を処理するCNNベースの「Pool encoder」を用い、最終的に同じ埋め込み空間上で内積（コサイン類似度）を比較するアーキテクチャが採用された。

## 結果
### Figureの考察

![Figure 1(a): Contrastive learning approach with InfoNCE loss as in CLIP.](./images/clip_overview.png)
![Figure 1(b): Proposed contrastive learning approach with masked InfoNCE loss.](./images/clip_mtg_overview.png)
*Figure 1: InfoNCE Lossの適応に関する概要。*
Figure 1(a)は標準のCLIPで用いられるInfoNCE Lossの類似度行列を示しており、対角成分のみを正例として計算している。対して、提案手法であるFigure 1(b)はマスキングが施されたInfoNCEを示している。ここでは、提示されたパックに存在しない組み合わせ（色無しの領域）をマスクして無視し、明示的な選択および拒否のみに基づいて比較を行っていることが視覚的に分かる。これにより、誤った負例による学習のノイズ（実際には相性が良いがパックになかっただけ）を排除することに成功している。

![Figure 2: Pseudocode for the adapted InfoNCE loss.](./images/pseudocode.png)
*Figure 2: 提案手法（Masked InfoNCE）の擬似コード。*
擬似コードからは、InfoNCEを用いたバッチ処理における行列演算のスケーリングの恩恵を受けながらも、マスクを適用して行方向のみCross Entropyを計算していることが確認できる。これによりTriplet Lossのように計算コストを行列全域に拡大することなく、明示的な比較対象の情報を落とすことなく学習を効率化できていることが読み取れる。

![Figure 3(a): Weight-shared output layer (used in triplet loss).](./images/siamese_overview.png)
![Figure 3(b): Separate output layers (used in InfoNCE loss).](./images/clip_network_overview.png)
*Figure 3: サブネットワーク構成の差異。*
Figure 3では、Triplet Loss利用時のSiameseネットワーク構造と、InfoNCE Loss利用時のネットワーク構造が対比されている。Triplet Lossを用いる場合(a)はSharedメインブロックを通じて比較評価されるが、InfoNCE(b)においてはCard encoderとPool encoderが独立したネットワークとして学習され、最後に出力された埋め込みベクトルの類似度行列を通じて学習される。独立した出力を得られることでより柔軟な表現抽出が可能になっている。

### Tableの考察

| Method | Top-1 Accuracy | Training time per epoch |
| :--- | :--- | :--- |
| Standard InfoNCE | 54.24% | 52:47min |
| Sigmoid InfoNCE | 68.11% | 53:30min |
| Adapted InfoNCE | **68.80%** | 52:45min |
| Triplet loss random mining | 67.23% | **47:31min** |
| Triplet loss hardest mining | 66.56% | 1:07:35h |
| Triplet loss all mining | 65.98% | 11:51:24h |

*Table 1: 異なるアプローチの比較結果。精度指標としてホールドアウトテストセットの正しい選択を予測する Top-1 精度を、計算コスト指標として 1エポックあたりの学習時間を計測。*

Table 1より以下の考察が得られる。
- **標準InfoNCEの限界**: Standard InfoNCEは精度が54.24%と著しく低い。これは類似度行列内にデータに基づいていない不正確な比較が多数発生し、学習が阻害されているためである。
- **Sigmoid InfoNCEの改善**: 正規化をSoftmaxからSigmoidに変更したSigmoid InfoNCE（複数の正当ペアを許容）は68.11%まで改善したが、依然として「文脈から外れた（提示すらされていないアイテムの）比較」が行われているため最適ではない。
- **提案手法の優位性**: 提案のAdapted InfoNCEは精度68.80%で最高性能を獲得し、標準InfoNCEとほぼ同等の学習時間（52分45秒）を維持している。
- **Triplet Lossとの比較**: Triplet Lossにおいて、Random Miningが最速かつ最高精度（67.23%）となった。Hardest Miningは精度が下がり計算時間も増大し、All Miningはバッチサイズを縮小したため計算時間が非現実的（11時間以上）になり精度低下を引き起こした（65.98%）。
- **結論**: Adapted InfoNCEはTripletベースの中で最も優秀であったRandom Miningよりも高精度であり、無駄な計算時間オーバーヘッドを追加することなく最適化されるため、ドラフト時のコンテキストに応じたモデル学習に極めて適していることが証明された。
