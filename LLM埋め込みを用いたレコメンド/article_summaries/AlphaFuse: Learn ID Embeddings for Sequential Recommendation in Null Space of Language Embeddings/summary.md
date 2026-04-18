# AlphaFuse: Learn ID Embeddings for Sequential Recommendation in Null Space of Language Embeddings

## 背景
逐次推薦システムにおいて、アイテムのテキストメタデータ（タイトルや説明）を大規模言語モデル（LLM）によって言語埋め込み（semantic space）として抽出し、それと、ユーザーとアイテムの相互作用から学習されるID埋め込み（behavior space）を統合するアプローチが注目を集めている。
しかし、次のような既存のアプローチには、主に3つの限界があった：
  
**既存手法の代表例**

| 論文名 (略称) | 年 | 手法概要 | アプローチ分類 |
| :--- | :--- | :--- | :--- |
| Representation Learning with Large Language Models for Recommendation (RLMRec) | 2024 | LLMの言語埋め込みをターゲットとし、補助的な再構成損失によってID埋め込みの学習をガイドする。 | 意味的再構成<br>(Semantic Reconstruction) |
| Text is all you need: Learning language representations for sequential recommendation (LLMInit) | 2023 | LLMから得た言語埋め込みをそのままID埋め込みの初期値として使い、タスクに合わせて更新していく。 | 意味的初期化<br>(Semantic Initialization) |
| Towards Universal Sequence Representation Learning for Recommender Systems (UniSRec) | 2022 | MLPなどの追加モジュールを学習させ、高次元の言語埋め込みを推薦用空間へ適応的に投影する。 | 適応的プロジェクション<br>(Adaptive Projection) |

これらの手法が抱える主な課題は以下の通りである：
1. **意味空間の退化（Degeneration of semantic space）**： LLMが生成する高次元（例：1536次元）の意味空間を、ID埋め込みの低次元（例：64次元）にマッピングすることで、豊かな世界知識情報が損なわれる。
2. **言語埋め込みの未活用**： 最終的なアイテム埋め込みとして凍結された言語埋め込みを直接使用しないため、推論時に知識が十二分に活かされない。
3. **追加の学習可能パラメータの発生**： アダプタや再構成モジュールなど、推薦モデル本体よりも多くのパラメータを抱え、推論効率の低下やパラメータの冗長性を招く。

これらを解決し、意味情報を損なわずに（semantic-anchored）追加モジュールなしで（tuning-efficient）協調信号を統合するため、著者らは特異値分解（SVD）を用いて言語埋め込みの「零空間（Null Space）」にID埋め込みを注入する **AlphaFuse** を提案した。

## 手法
提案される **AlphaFuse** は以下の4ステップで言語埋め込みの零空間にID埋め込みを構築する：

1. **意味空間の分解（Decomposition of Semantic Space）**  
   アイテム群の言語埋め込み $ \mathbf{E} \in \mathbb{R}^{N \times d_l} $ に対してSVDを行い、意味空間を分解する。高い特異値をもつ「意味の豊富な部分空間（semantic-rich subspaces, 行空間）」と、特異値がほぼゼロの「意味の希薄な部分空間（semantic-sparse space, 零空間）」に分割する。
   
   ![Visualization of space decomposition](./images/space3.png)
   *Figure 1: Visualization of space decomposition.*

2. **零空間のクリッピング（Clipping of Null Space）**  
   意味空間における零空間の次元数は非常に大きいため（全体の約80%）、従来の推薦モデルに適した次元数（例：64や128） $ d_n $ に切り詰める。

3. **意味豊富な部分空間の標準化（Standardization of semantic-rich Subspaces）**  
   言語埋め込みが持つ異方性（anisotropy）に対処するため、特異値を用いたスケーリング（白色化に近い操作）を行い、各意味空間の重みを標準化する。

   具体的には、言語埋め込み行列 $\mathbf{E}$ の共分散行列に対する特異値分解 $\mathbf{U}\mathbf{S}\mathbf{U}^T = \text{SVD}(\mathbf{\Sigma})$ を行い、以下のように演算を行う：

   $$ \mathbf{E}_{\text{language}} = (\mathbf{E}-\mathbf{\mu}) \cdot \mathbf{U}_{[:, :d_s+d_n]} \cdot \mathbf{S}^{-\frac{1}{2}}_{[:d_s+d_n, :d_s+d_n]} $$

   特異値の2乗（分散に相当）を持つ行列 $\mathbf{S}$ を $-\frac{1}{2}$ 乗することは、各次元ごとに特異値 $s_i$ の逆数を掛けることに等しい。これにより、少数の主成分に情報が偏る異方性を緩和し、どの意味空間の軸も同じ程度の重みになり、アイテム同士の実質的な類似度（cosine similarity）のばらつきが抑えられ、より識別性の高い埋め込みが得られる。

   ![Overall framework of language-guided ID embedding learning strategies](./images/framework5.png)
   *Figure 2: Overall framework of language-guided ID embedding learning strategies.*

4. **ID埋め込みの学習（Learning of ID embeddings）**  
   クリッピングされた零空間内において ID埋め込み $ \mathbf{E}_{\text{ID}} $ をゼロ（もしくは乱数）で初期化して学習を行う。一方で、標準化された意味豊富な部分空間における言語埋め込み $ \mathbf{E}_{\text{language}} $ は凍結（frozen）する。
   最終的なアイテム埋め込み $ \mathbf{E}_{\text{item}} $ は以下のように構築される：

$$
\mathbf{E}_{\text{item}} = \mathbf{E}_{\text{language}} + (\mathbf{0} \in \mathbb{R}^{N \times d_s}, \mathbf{E}_{\text{ID}})
$$

## 結果

本実験では、 Movies 、 Toys 、 Sports の3つのデータセットを用いて評価を行った。

### データセット統計

| Dataset | \# users | \# items | \# Interactions | sparsity |
| :--- | :--- | :--- | :--- | :--- |
| Movies | 20,515 | 44,014 | 637,157 | 00.07% |
| Toys | 19,412 | 11,924 | 138,444 | 00.06% |
| Sports | 35,598 | 18,357 | 256,598 | 00.04% |

*Table 1: Statistics of datasets after preprocessing.*

### 特異値と類似度の分布検証

![Normalized singular values of language embeddings](./images/singular_values.png)
*Figure 3: Normalized singular values of language embeddings for the Movies dataset.*

![The cumulative distribution of cosine similarity](./images/ECDF.png)
*Figure 4: The cumulative distribution of cosine similarity for item pairs using language embeddings.*

Figure 3は Movies データセットにおける言語埋め込みの特異値の分布を示す。少数の特異値に意味情報が集中しており、残りの部分空間（零空間）には情報がほとんど無い「低ランク構造」と「異方性」が確認できる。ここから、零空間に協調信号を注入する妥当性が示されている。また、Figure 4のように標準化を行うことでアイテム間の過剰な類似度が低下し、モデルがアイテムを区別しやすくなったことがわかる。

### コールドスタート対応性能比較

| Dataset | Method | Movies N@10 | Movies M@10 | Movies N@20 | Movies M@20 | Toys N@10 | Toys M@10 | Toys N@20 | Toys M@20 | Sports N@10 | Sports M@10 | Sports N@20 | Sports M@20 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SASRec Backbone** | | | | | | | | | | | | | |
| | Base | 0.0338 | 0.0238 | 0.0429 | 0.0263 | 0.0255 | 0.0191 | 0.0321 | 0.0210 | 0.0073 | 0.0049 | 0.0101 | 0.0057 |
| | MoRec | 0.0154 | 0.0105 | 0.0205 | 0.0119 | 0.0114 | 0.0069 | 0.0146 | 0.0078 | 0.0098 | 0.0074 | 0.0109 | 0.0077 |
| | UniSRec | 0.0232 | 0.0160 | 0.0303 | 0.0179 | 0.0271 | 0.0191 | 0.0311 | 0.0202 | 0.0071 | 0.0051 | 0.0084 | 0.0055 |
| | WhitenRec | 0.0168 | 0.0116 | 0.0223 | 0.0131 | 0.0258 | 0.0181 | 0.0304 | 0.0194 | 0.0115 | 0.0081 | 0.0141 | 0.0088 |
| | RLMRec-Con | 0.0346 | 0.0244 | 0.0441 | 0.0269 | 0.0266 | 0.0185 | 0.0304 | 0.0195 | 0.0089 | 0.0058 | 0.0107 | 0.0063 |
| | RLMRec-Gen | 0.0355 | 0.0252 | 0.0449 | 0.0278 | 0.0303 | 0.0246 | 0.0347 | 0.0257 | 0.0080 | 0.0054 | 0.0102 | 0.0060 |
| | LLMInit | 0.0370 | 0.0264 | 0.0470 | 0.0291 | 0.0275 | 0.0215 | 0.0313 | 0.0225 | 0.0083 | 0.0055 | 0.0102 | 0.0060 |
| | LLM-ESR | 0.0139 | 0.0094 | 0.0192 | 0.0108 | 0.0122 | 0.0104 | 0.0153 | 0.0112 | 0.0101 | 0.0075 | 0.0118 | 0.0079 |
| | **AlphaFuse** | **0.0459** | **0.0324** | **0.0574** | **0.0355** | **0.0339** | **0.0287** | **0.0376** | **0.0297** | **0.0137** | **0.0098** | **0.0158** | **0.0104** |
| | Best Impr. | +24.05% | +22.73% | +22.13% | +21.99% | +11.88% | +16.67% | +8.36% | +15.56% | +19.13% | +20.99% | +12.06% | +18.18% |
| **DreamRec Backbone** | | | | | | | | | | | | | |
| | Base | 0.0016 | 0.0013 | 0.0018 | 0.0014 | 0.0383 | 0.0333 | 0.0392 | 0.0336 | 0.0158 | 0.0132 | 0.0170 | 0.0135 |
| | iDreamRec | 0.0226 | 0.0180 | 0.0262 | 0.0189 | 0.0350 | 0.0301 | 0.0373 | 0.0307 | 0.0141 | 0.0119 | 0.0155 | 0.0123 |
| | MoRec | 0.0002 | 0.0002 | 0.0003 | 0.0002 | 0.0030 | 0.0026 | 0.0034 | 0.0027 | 0.0012 | 0.0010 | 0.0017 | 0.0012 |
| | UniSRec | 0.0021 | 0.0014 | 0.0030 | 0.0017 | 0.0014 | 0.0008 | 0.0022 | 0.0010 | 0.0004 | 0.0002 | 0.0008 | 0.0003 |
| | WhitenRec | 0.0007 | 0.0006 | 0.0008 | 0.0006 | 0.0029 | 0.0021 | 0.0034 | 0.0022 | 0.0026 | 0.0019 | 0.0030 | 0.0021 |
| | RLMRec | 0.0016 | 0.0013 | 0.0019 | 0.0014 | 0.0376 | 0.0321 | 0.0388 | 0.0325 | 0.0160 | 0.0135 | 0.0172 | 0.0138 |
| | LLMInit | 0.0082 | 0.0056 | 0.0113 | 0.0065 | 0.0198 | 0.0179 | 0.0214 | 0.0184 | 0.0075 | 0.0065 | 0.0086 | 0.0068 |
| | LLM-ESR | 0.0007 | 0.0004 | 0.0010 | 0.0005 | 0.0073 | 0.0061 | 0.0090 | 0.0066 | 0.0045 | 0.0037 | 0.0048 | 0.0037 |
| | **AlphaFuse** | **0.0246** | **0.0201** | **0.0279** | **0.0209** | **0.0408** | **0.0348** | **0.0425** | **0.0353** | **0.0165** | **0.0139** | **0.0174** | **0.0142** |
| | Best Impr. | +8.85% | +11.67% | +6.49% | +10.58% | +6.53% | +4.50% | +8.42% | +5.06% | +3.13% | +2.96% | +1.16% | +2.90% |

*Table 2: Performance comparison across different backbones and methods on three datasets with cold-start user settings.*

Table 2 から、識別モデルの SASRec と 生成モデルの DreamRec のどちらをバックボーンに利用した場合でも、 AlphaFuse がコールドスタートユーザに対して最高の性能を発揮したことがわかる。特化したアダプター等へ余分な依存をせず、言語埋め込みそのものを最終アイテム表現と融合させているため、言語埋め込み固有の世界知識を最も活かせたと考えられる。

### ロングテール対応性能比較

| Dataset | Model | Overall R@10 | Overall N@10 | Tail Item R@10 | Tail Item N@10 | Head Item R@10 | Head Item N@10 | Tail User R@10 | Tail User N@10 | Head User R@10 | Head User N@10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Yelp** | SASRec | 0.5940 | 0.3597 | 0.1142 | 0.0495 | 0.7353 | 0.4511 | 0.5893 | 0.3578 | 0.6122 | 0.3672 |
| | -LLM-ESR | **0.6673** | 0.4208 | **0.1893** | **0.0845** | **0.8080** | 0.5199 | **0.6685** | 0.4229 | **0.6627** | 0.4128 |
| | -**AlphaFuse** | 0.6631 | **0.4219** | 0.1815 | 0.0775 | 0.8048 | **0.5232** | 0.6617 | **0.4239** | 0.6585 | **0.4141** |
| | Best Impr. | -0.63% | +0.26% | -4.12% | -8.28% | -0.40% | +0.63% | -1.02% | +0.24% | -0.63% | +0.31% |
| **Fashion** | SASRec | 0.4956 | 0.4429 | 0.0454 | 0.0235 | 0.6748 | 0.6099 | 0.3967 | 0.3390 | 0.6239 | 0.5777 |
| | -LLM-ESR | 0.5619 | 0.4743 | 0.1095 | 0.0520 | **0.7420** | 0.6424 | 0.4811 | 0.3769 | 0.6668 | 0.6005 |
| | -**AlphaFuse** | **0.6008** | **0.5103** | **0.2601** | **0.1646** | 0.7364 | **0.6479** | **0.5352** | **0.4276** | **0.6860** | **0.6175** |
| | Best Impr. | +6.92% | +7.59% | +137.53% | +216.54% | -0.75% | +0.86% | +11.25% | +13.45% | +2.88% | +2.83% |
| **Beauty** | SASRec | 0.4388 | 0.3030 | 0.0870 | 0.0649 | 0.5227 | 0.3598 | 0.4270 | 0.2941 | 0.4926 | 0.3438 |
| | -LLM-ESR | 0.5672 | 0.3713 | **0.2257** | **0.1108** | 0.6486 | 0.4334 | 0.5581 | 0.3643 | 0.6087 | 0.4032 |
| | -**AlphaFuse** | **0.5793** | **0.4046** | 0.1625 | 0.1006 | **0.6787** | **0.4771** | **0.5692** | **0.3984** | **0.6258** | **0.4326** |
| | Best Impr. | +2.13% | +8.97% | -28.00% | -9.21% | -4.64% | +10.08% | +1.99% | +9.36% | +2.81% | +7.29% |

*Table 3: Performance comparison across different methods on three datasets with long-tail settings.*

表3が示すように、ロングテールのユーザやアイテムへの対応に特化して作られた LLM-ESR と比較しても AlphaFuse は非常に強い競争力を持ち、とくに Fashion データセットでは LLM-ESR を大幅に凌駕している。

### アブレーションスタディとハイパーパラメータ解析

| Dataset | Model | SASRec N@10 | SASRec M@10 | SASRec N@20 | SASRec M@20 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Movies** | **AlphaFuse** | **0.0459** | **0.0324** | **0.0574** | **0.0355** |
| | -w/o Frozen. | 0.0350 | 0.0249 | 0.0444 | 0.0274 |
| | -w/o Clip. | 0.0148 | 0.0096 | 0.0197 | 0.0109 |
| | -w/o Stand. | 0.0354 | 0.0250 | 0.0450 | 0.0276 |

*Table 4: The ablation study with SASRec as the backbone.*

| Dataset | Model | DreamRec N@10 | DreamRec M@10 | DreamRec N@20 | DreamRec M@20 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Movies** | **AlphaFuse** | **0.0246** | **0.0201** | **0.0279** | **0.0209** |
| | -w/o Decom. | 0.0103 | 0.0084 | 0.0120 | 0.0089 |
| | -w/o Frozen. | 0.0214 | 0.0177 | 0.0242 | 0.0185 |
| | -w/o Stand. | 0.0114 | 0.0089 | 0.0140 | 0.0095 |

*Table 5: The ablation study with DreamRec as the backbone.*

![Dimension of Item embeddings](./images/dim_item_embs.png)
*Figure 5(a): Dimension of Item embeddings.*

![Dimension of ID embeddings](./images/dim_ID_embs.png)
*Figure 5(b): Dimension of ID embeddings.*

![Threshold of Semantic Weights](./images/thres_DreamRec.png)
*Figure 5(c): Threshold of Semantic Weights.*

SASRec・DreamRecの両方の構成において、言語埋め込みの「凍結（Frozen）」「零空間のクリッピング（Clip）またDecomposition」「意味豊富な空間の標準化（Standardization）」というすべての処理モジュールが性能向上に不可欠であることが Table 4 と Table 5 によって確認された。
ハイパーパラメータ解析（Figure 5）では、 アイテム埋め込み全体の次元を増やしすぎると零空間でのID学習が困難になりかえって性能が落ちること（Figure 5(a)）、適正範囲（Figure 5(b)）や DreamRec での適切な特異値の閾値設定（Figure 5(c)）が鍵であることが明らかになった。

### 学習と推論効率の検証

| Models | \# Trainable Parameters | Inference GFLOPs |
| :--- | :--- | :--- |
| UniSRec | 1.69M | 4.24 |
| LLM-ESR | 4.10M | 3.34 |
| MoRec | 0.28M | 0.72 |
| WhitenRec | 0.28M | 0.72 |
| RLMRec | 7.10M | 0.22 |
| LLMInit | 5.72M | 0.22 |
| SASRec | 5.72M | 0.22 |
| **AlphaFuse** | **2.90M** | **0.22** |

*Table 6: Comparison of efficiency through the number of trainable parameters and GFLOPs during inference.*

Table 6 は AlphaFuse の効率性の高さを示している。追加の学習モジュールを抱えず、言語パースを事前に凍結しているため、必要な学習パラメータ数（2.90M）や推論演算量（0.22 GFLOPs）の両方において顕著な低コスト化を実現している。単なる予測精度の向上だけでなく、実装上のスケーラビリティも非常に高いと言える。

## chokosenlovetiの考察

### 異方性への対応

LLMが生成する埋め込み表現は、しばしば特定の狭い円錐状の空間に分布が偏ってしまう「異方性（Anisotropy）」の問題を抱えている。これにより、全く異なるアイテム同士であってもコサイン類似度が極端に高くなりやすく、推薦モデルがアイテム間の微妙な差異（協調フィルタリング的な識別性）を学習する上で大きなボトルネックとなる。

AlphaFuseでは、言語埋め込みの共分散行列を特異値分解（SVD）し、意味が集中している部分空間の各次元を特異値に基づいてスケーリング（標準化）するアプローチを採用している。これは実質的に「白色化（Whitening）」に近い操作であり、一部の支配的な特異成分の影響をなだめ、各次元の持つ情報の重みを均等化することに寄与している。結果としてFigure 4に示されるようにアイテム間の過剰な類似度が低下し、意味空間の解像度が向上している。

単なる次元削減ではなく、「意味の事前知識が詰まった空間の異方性を補正しつつ凍結し、残りの不要な零空間に純粋な推薦ID信号を注入する」という空間の棲み分けを行った点は、テキスト情報と協調信号が互いを干渉して破壊し合う（Degeneration）のを防ぐ、非常に理にかなったエレガントな設計であると評価できる。

### 未知アイテムとコールドスタートへの強さ

AlphaFuseの空間分離アーキテクチャは、未知のアイテム（Inductive設定）をサポートしている。推薦モデルが学習時に一度も見たことがないアイテムが投入された場合でも、未学習のID部分を単に「ゼロベクトル」として扱うことで、テキストから算出される言語埋め込みのみを用いてそのまま推論空間に統合できる。

ただし、論文内の実験においては「完全にテキスト情報のみの未知アイテム（Zero-shot）」単体での検証は行われていない。その代わりとして、相互作用が極めて少ない「コールドスタートアイテム（Tail Item）」を用いた検証が実施されており、既存の言語モデルベース手法（UniSRecやLLM-ESR等）より高精度。テキスト空間が協調情報に汚染（退化）されないため、学習が不十分なアイテムであっても事前学習済みLLMの知識を100%発揮できることが、コールドスタート対応力の根拠となっている。
