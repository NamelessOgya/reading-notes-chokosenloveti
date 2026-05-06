# Recommender Systems with Generative Retrieval (TIGER)

## 背景
現代の推薦システムは、アイテムとクエリを共通の空間に埋め込んだ上で近似最近傍探索（ANN）等を用いて候補を抽出する「retrieve-and-rank」アプローチが主流である（例：SASRecなど）。しかし、これらのパラダイムはランダムでアトミックな「Item ID」に依存しており、新しく追加されたアイテム（コールドスタート）には対応しにくく、またアイテム数が数十億規模になると大規模な埋め込みの学習やインデックスサイズの肥大化等、システム制約の壁に直面する。この課題に対し、本論文はTransformerのネットワーク自体（メモリ）を検索インデックスとして活用する、新たな**生成的検索 (Generative Retrieval)** の枠組みである「TIGER (Transformer Index for GEnerative Recommenders)」を提案する。

## 手法
提案手法「TIGER」は大きく2つの段階で構成される。

1. **Semantic ID (意味的ID) の生成**
   アイテムのコンテンツ特徴（タイトル、カテゴリ、ブランドなど）を事前学習済み言語モデル（Sentence-T5等）に入力し、密な意味的埋め込みベクトル (Semantic Embedding) を獲得する。獲得したベクトルを **RQ-VAE (Residual-Quantized Variational AutoEncoder)** を用いて量子化し、整数のタプルからなるコードワード「Semantic ID」に変換する。
   RQ-VAEは各階層で直前の残差を量子化していく仕組み（再帰的ベクトル量子化）であり、粗い粒度（大分類）から詳細な粒度（小分類）へと階層的な意味構造を保持できる。損失関数は以下のように定義され、エンコーダ・デコーダおよびコードブックを同時に学習する。

   $$ \mathcal{L}(\boldsymbol{x}) := \mathcal{L}_{\text{recon}} + \mathcal{L}_{\text{rqvae}} $$

   ここで、
   $$ \mathcal{L}_{\text{recon}} := \|\boldsymbol{x}- \widehat{\boldsymbol{x}}\|^2 $$

   $$ \mathcal{L}_{\text{rqvae}} := \sum_{d=0}^{m-1}{\|\text{sg}[\boldsymbol{r}_i]- \boldsymbol{e}_{c_i}\|^2} + \beta\|\boldsymbol{r}_i- \text{sg}[\boldsymbol{e}_{c_i}]\|^2 $$

   また、異なるアイテムが全く同じSemantic IDを共有してしまう「衝突 (Collision)」を回避するため、学習後に一意なトークンを末尾に追加して各IDを一意にする。

2. **Semantic ID を用いた Generative Retrieval の学習**
   ユーザーのインタラクション履歴（アイテム系列）を Semantic ID の系列（トークン列）に変換し、Seq2Seq型のTransformerモデル（例えばT5X）を用いて、次にアクセスされるアイテムの Semantic ID を自己回帰的 (autoregressive) に予測するように学習させる。

   **【推論（マッチング）の仕組みと計算コストのトレードオフ】**
   推論時には、モデルが自己回帰的に生成したSemantic IDを、事前に構築した「実際のItem IDとのマッピング辞書」と照合して推薦アイテムを特定する。また、架空の無効なIDが生成されるのを防ぐため、通常はトライ木（Trie Tree）を用いて実在するIDの経路のみを探索する制約付きデコード（Constrained Decoding）が行われる。
   ただし、この「複数トークンの自己回帰的な生成」と「ビームサーチ・トライ木による経路探索」のプロセスは、非常に高速に最適化された従来の近似最近傍探索（ANN）ベースのマッチング手法と比較すると、推論時間（レイテンシ）や計算コストが大きくなるというトレードオフを抱えている。

## 結果
TIGERの有効性は Amazon Reviews の3つのデータセット (Beauty, Sports and Outdoors, Toys and Games) における系列推薦タスクで評価され、既存のSOTAモデルを一貫して上回る性能を達成した。

### 推論性能の向上
Table 1に示されるように、全データセットにおいて TIGER は最良の成績を収めている。特に Beauty データセットにおいては、SASRec等と比較して NDCG@5 が最大29%、Recall@5 が最大17.3%向上した。

### ID生成手法の比較 (RQ-VAEの優位性)
Table 2の比較実験（Ablation Study）では、Semantic IDの生成にRQ-VAEを用いる手法が、Locality Sensitive Hashing (LSH) やランダムなID割り当てよりも大きく精度で上回ることが示された。コンテンツのセマンティクスを階層的に保持した表現が検索精度に大きく寄寄与している。

### Semantic IDの階層性と新たな機能の創発
RQ-VAEで生成されたSemantic IDは階層的な性質を持つ（Figure 2にRQ-VAEの図解、及びカテゴリとコードワードの対応分布 `code1_distrib.png`, `code2_category_distributions.png` により観察される）。この性質から、以下の「新しい推薦機能 (Emergent Capabilities)」が実現可能であることが確認された。

1. **コールドスタート推薦 (Cold-Start Recommendation)**
   未学習の新規アイテムであっても、コンテンツ特徴から意味的近傍としてのSemantic IDを導出できるため、部分一致（Prefix Match）によって適切に検索対象とすることができる（Figure 3: `cold_recall_K.png`, `cold_recall_epsilon_2.png` ）。TIGERは従来のSemantic KNNを上回る精度で推論が可能であった。
2. **推薦の多様性制御 (Recommendation Diversity)**
   デコード時の温度パラメータ (Temperature) を操作することで、推薦アイテムの多様性（エントロピー）を柔軟に制御できる。Table 3が示すように、温度を上げると出力されるカテゴリの分布がより多様なものへ変化する。

### Invalid IDs (無効なID) の生成への耐性
生成ベースの手法では、実在しないアイテムの ID (Invalid IDs) が生成される懸念があるが、ビームサーチ実行時の無効IDの割合は高々 0.1%〜1.6% 程度であり（`beam_search_invalid_beauty20.png`等に示される）、実用上の問題を回避しつつ高いランキング指標を確保できることが示された。

---
## 抽出された表 (Tables)
### Table 1: Performance comparison on sequential recommendation. The last row depicts \% improvement with TIGER relative to the best baseline. Bold (underline) are used to denote the best (second-best) metric.
| Methods | **Sports and Outdoors** | **Beauty** | **Toys and Games** |
| --- | --- | --- | --- |
|  | Recall @5 | NDCG @5 | Recall @10 | NDCG @10 | Recall @5 | NDCG @5 | Recall @10 | NDCG @10 | Recall @5 | NDCG @5 | Recall @10 | NDCG @10 |
| P5~ | 0.0061 | 0.0041 | 0.0095 | 0.0052 | 0.0163 | 0.0107 | 0.0254 | 0.0136 | 0.0070 | 0.0050 | 0.0121 | 0.0066 |
| Caser~ | 0.0116 | 0.0072 | 0.0194 | 0.0097 | 0.0205 | 0.0131 | 0.0347 | 0.0176 | 0.0166 | 0.0107 | 0.0270 | 0.0141 |
| HGN~ | 0.0189 | 0.0120 | 0.0313 | 0.0159 | 0.0325 | 0.0206 | 0.0512 | 0.0266 | 0.0321 | 0.0221 | 0.0497 | 0.0277 |
| GRU4Rec~ | 0.0129 | 0.0086 | 0.0204 | 0.0110 | 0.0164 | 0.0099 | 0.0283 | 0.0137 | 0.0097 | 0.0059 | 0.0176 | 0.0084 |
| BERT4Rec~ | 0.0115 | 0.0075 | 0.0191 | 0.0099 | 0.0203 | 0.0124 | 0.0347 | 0.0170 | 0.0116 | 0.0071 | 0.0203 | 0.0099 |
| FDSA~ | 0.0182 | 0.0122 | 0.0288 | 0.0156 | 0.0267 | 0.0163 | 0.0407 | 0.0208 | 0.0228 | 0.0140 | 0.0381 | 0.0189 |
| SASRec~ | 0.0233 | 0.0154 | 0.0350 | 0.0192 | 0.0387 | <u>0.0249</u> | 0.0605 | 0.0318 | <u>0.0463</u> | <u>0.0306</u> | 0.0675 | 0.0374 |
| S$^3$-Rec~ | <u>0.0251</u> | <u>0.0161</u> | <u>0.0385</u> | <u>0.0204</u> | <u>0.0387</u> | 0.0244 | <u>0.0647</u> | <u>0.0327</u> | 0.0443 | 0.0294 | <u>0.0700</u> | <u>0.0376</u> |
| **TIGER [Ours]** |
|  | **0.0264** | **0.0181** | **0.0400** | **0.0225** |
|  | **0.0454** | **0.0321** | **0.0648** | **0.0384** |
|  | **0.0521** | **0.0371** | **0.0712** | **0.0432** |
|  | +5.22\% | +12.55\% | +3.90\% | +10.29\% | +17.31\% | +29.04\% | +0.15\% | +17.43\% | +12.53\% | +21.24\% | +1.71\% | +14.97\% |

### Table 2: Ablation study for different ID generation techniques for generative retrieval. We show that RQ-VAE Semantic ID (SID) perform significantly better compared to hashing SIDs and Random IDs.
| Methods | **Sports and Outdoors** | **Beauty** | **Toys and Games** |
| --- | --- | --- | --- |
|  | Recall @5 | NDCG @5 | Recall @10 | NDCG @10 | Recall @5 | NDCG @5 | Recall @10 | NDCG @10 | Recall @5 | NDCG @5 | Recall @10 | NDCG @10 |
| Random ID | 0.007 | 0.005 | 0.0116 | 0.0063 | 0.0296 | 0.0205 | 0.0434 | 0.0250 | 0.0362 | 0.0270 | 0.0448 | 0.0298 |
| LSH SID | 0.0215 | 0.0146 | 0.0321 | 0.0180 | 0.0379 | 0.0259 | 0.0533 | 0.0309 | 0.0412 | 0.0299 | 0.0566 | 0.0349 |
| RQ-VAE SID |
|  | **0.0264** | **0.0181** | **0.0400** | **0.0225** |
|  | **0.0454** | **0.0321** | **0.0648** | **0.0384** |
|  | **0.0521** | **0.0371** | **0.0712** | **0.0432** |

### Table 3: Recommendation diversity with temperature-based decoding.
| Target Category | Most-common Categories for top-10 predicted items |
| --- | --- |
|  | T = 1.0 | T = 2.0 |
| Hair Styling Products | Hair Styling Products | Hair Styling Products, Hair Styling Tools, Skin Face |
| Tools Nail | Tools Nail | Tools Nail, Makeup Nails |
| Makeup Nails | Makeup Nails | Makeup Nails, Skin Hands \ | Nails, Tools Nail |
| Skin Eyes | Skin Eyes | Hair Relaxers, Skin Face, Hair Styling Products, Skin Eyes |
| Makeup Face | Tools Makeup Brushes,Makeup Face | Tools Makeup Brushes, Makeup Face,Skin Face, Makeup Sets, Hair Styling Tools |
| Hair Loss Products | Hair Loss Products,Skin Face, Skin Body | Skin Face, Hair Loss Products, Hair Shampoos,Hair \ | Scalp Treatments, Hair Conditioners |

### Table 4: Recall and NDCG metrics for different number layers.
| Number of Layers | {Recall@5} | {NDCG@5} | {Recall@10} | {NDCG@10} |
| --- | --- | --- | --- | --- |
| 3 | 0.04499 | 0.03062 | 0.06699 | 0.03768 |
| 4 | 0.0454 | 0.0321 | 0.0648 | 0.0384 |
| 5 | 0.04633 | 0.03206 | 0.06596 | 0.03834 |

### Table 5: The effect of providing user information to the recommender system
| Recall@5 | NDCG@5 | Recall@10 | NDCG@10 |  |
| --- | --- | --- | --- | --- |
| No user information | 0.04458 | 0.0302 | 0.06479 | 0.0367 |
| With user id (reported in the paper) | 0.0454 | 0.0321 | 0.0648 | 0.0384 |

### Table 6: The mean and stand error of the metrics for different dataset (computed using 3 runs with different random seeds)
| Datasets | Recall@5 | NDCG@5 | Recall@10 | NDCG@10 |
| --- | --- | --- | --- | --- |
| Beauty | 0.0441 $\pm$ 0.00069 | 0.0309 $\pm$ 0.00062 | 0.0642 $\pm$ 0.00092 | 0.0374 $\pm$ 0.00061 |
| Sports and Outdoors | 0.0278 $\pm$ 0.00069 | 0.0189 $\pm$ 0.00043 | 0.0419 $\pm$ 0.0010 | 0.0234 $\pm$ 0.00048 |
| Toys and Games | 0.0518 $\pm$ 0.00064 | 0.0375 $\pm$ 0.00039 | 0.0698 $\pm$ 0.0013 | 0.0433 $\pm$ 0.00047 |

### Table 7: Testing scalability by generating the Semantic IDs on the combined dataset vs generating the Semantic IDs on only the Beauty dataset.
|  | Recall@5 | NDCG@5 | Recall@10 | NDCG@10 |
| --- | --- | --- | --- | --- |
| Semantic ID [Combined datasets] | 0.04355 | 0.3047 | 0.06314 | 0.03676 |
| Semantic ID [Amazon Beauty] | 0.0454 | 0.0321 | 0.0648 | 0.0384 |

### Table 8: Dataset statistics for the three real-world benchmarks.
| Dataset | \# Users | \# Items | Sequence Length |
| --- | --- | --- | --- |
|  |  |  | Mean | Median |
| \arrayrulecolor{gray}\cmidrule(r){4-5} |
| Beauty | 22,363 | 12,101 | 8.87 | 6 |
| Sports and Outdoors | 35,598 | 18,357 | 8.32 | 6 |
| Toys and Games | 19,412 | 11,924 | 8.63 | 6 |

### Table 9: Results for P5\cite{geng2022recommendation
|  | Methods | **Sports and Outdoors** | **Beauty** | **Toys and Games** |
| --- | --- | --- | --- | --- |
|  |  | Recall@5 | NDCG@5 | Recall@10 | NDCG@10 | Recall@5 | NDCG@5 | Recall@10 | NDCG@10 | Recall@5 | NDCG@5 | Recall@10 | NDCG@10 |
|  | P5 | 0.0061 | 0.0041 | 0.0095 | 0.0052 | 0.0163 | 0.0107 | 0.0254 | 0.0136 | 0.0070 | 0.0050 | 0.0121 | 0.0066 |
|  | P5-ours | 0.0107 | 0.0076 | 0.01458 | 0.0088 | 0.035 | 0.025 | 0.048 | 0.0298 | 0.018 | 0.013 | 0.0235 | 0.015 |



## 抽出された図版 (Figures)
- **Figure 1 (Overview)**
  ![introduction_overview.png](./images/introduction_overview.png)
  ![semantic_id_generation_overview.png](./images/semantic_id_generation_overview.png)
  ![enc-dec-overview_neurips.png](./images/enc-dec-overview_neurips.png)
- **Figure 2 (RQ-VAE Landscape)**
  ![RQVAE_landscape_neurips.png](./images/RQVAE_landscape_neurips.png)
- **Figure 3 (Cold Start Recommendation)**
  ![cold_recall_K.png](./images/cold_recall_K.png)
  ![cold_recall_epsilon_2.png](./images/cold_recall_epsilon_2.png)
- **Appendix (Invalid IDs / Category Distribution)**
  ![beam_search_invalid_beauty20.png](./images/beam_search_invalid_beauty20.png)
  ![beam_search_invalid_sports20.png](./images/beam_search_invalid_sports20.png)
  ![beam_search_invalid_toys20.png](./images/beam_search_invalid_toys20.png)
  ![code1_distrib.png](./images/code1_distrib.png)
  ![code2_category_distributions.png](./images/code2_category_distributions.png)

