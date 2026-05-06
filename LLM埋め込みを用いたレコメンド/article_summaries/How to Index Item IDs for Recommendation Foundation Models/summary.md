# How to Index Item IDs for Recommendation Foundation Models

## 背景
基盤モデル（大規模言語モデル：LLM）を用いた生成的レコメンド（Generative Recommendation）は、レコメンドタスクを自然言語生成タスクに変換することで、多段階のフィルタリングを省き直接アイテムを生成することが可能である（例：P5、M6Rec）。しかし、アイテムのタイトルや説明などの自由記述テキストを直接生成させようとすると、実在しないアイテムを生成してしまう「ハルシネーション（Hallucination）」の問題が生じる。
これを防ぐためには、各アイテムに一意のLLM互換のID（トークンシーケンス）を割り当てるインデックス付与（Indexing）が不可欠である。しかし、従来の単純なインデックス手法（ランダムな数値を割り当てるRandom Indexing、タイトルを用いるTitle Indexing、各アイテムに完全に独立した新しいトークンを割り当てるIndependent Indexing）では、無関係なアイテム間でトークンが衝突して意図せぬバイアスを生んだり、学習すべき新規トークンが膨大になるなどの課題があった。本研究では、LLMベースのレコメンド（特にP5）における効果的なアイテムインデックスの手法を体系的に調査・提案する。

## 手法
最適なインデックス手法は「長すぎないこと（テキスト生成の難易度を下げる）」と「事前情報（アイテム間の類似性など）をインデックス構造に組み込むこと（類似アイテムは多くのトークンを共有し、非類似アイテムは共有しないこと）」の2つの基準を満たす必要がある。本論文では以下の4つの高度なインデックス手法を提案している。

1. **Sequential Indexing (SID)**
   ユーザーのインタラクション履歴において連続して現れるアイテムに対し、連続した数値ID（1001から開始）を割り当てる手法。SentencePieceトークナイザを用いると、「1001」と「1002」は「100」「1」と「100」「2」に分割されるため、共起するアイテム間で「100」というトークンが共有され、協調フィルタリング的な情報を自然にエンコードできる。
2. **Collaborative Indexing (CID)**
   Spectral Matrix Factorization (SMF) に基づくスペクトラルクラスタリングを用いてアイテムの共起グラフから階層的なクラスタを構築し、IDを生成する手法。共起頻度に基づく隣接行列（Adjacency matrix）およびラプラシアン行列（Laplacian matrix）を分解し、再帰的にアイテムをクラスタリングする（各階層で $N$ 個のクラスタに分割し、最終クラスタの最大要素数を $k$ とする）。インデックスは、根から葉（アイテム）に至る各クラスタノードの独立トークンの連結として表現される。
3. **Semantic Indexing (SemID)**
   アイテムのメタデータ（カテゴリ情報）を利用し、階層的なカテゴリツリーに基づいてIDを構築する手法。カテゴリの各階層を独立したトークンに割り当て、それを粗いカテゴリから細かいカテゴリへと連結する。
4. **Hybrid Indexing (HID)**
   上記の手法を組み合わせた手法。例えば、CIDまたはSemIDの末尾にIID（Independent Indexing：独立した識別トークン）を付与する **CID+IID** や **SemID+IID** などがある。これにより、階層的な情報（協調的または意味的）を保持しつつ、各アイテムの一意性を強力に保証する。

## 結果

本研究では、Amazon Sports、Amazon Beauty、Yelpの3つのデータセットを用いて評価を行った。

Table 1: Basic statistics of datasets
| | $\#$User | $\#$Item | $\#$Interactions | Sparsity($\%$) |
|---|---|---|---|---|
| Sports | 35,598 | 18,357 | 296,337 | 0.0453 |
| Beauty | 22,363 | 12,101 | 198,502 | 0.0734 |
| Yelp | 30,431 | 20,033 | 316,354 | 0.0519 |

Table 2: Performances of the trivial indexing methods for P5 as well as the baselines.
| Method | Sports HR@5 | Sports NCDG@5 | Sports HR@10 | Sports NCDG@10 | Beauty HR@5 | Beauty NCDG@5 | Beauty HR@10 | Beauty NCDG@10 | Yelp HR@5 | Yelp NCDG@5 | Yelp HR@10 | Yelp NCDG@10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SASRec | 0.0233 | 0.0154 | 0.0350 | 0.0192 | 0.0387 | 0.0249 | 0.0605 | 0.0318 | 0.0170 | 0.0110 | 0.0284 | 0.0147 |
| S$^3$-Rec | 0.0251 | 0.0161 | 0.0385 | 0.0204 | 0.0387 | 0.0244 | 0.0647 | 0.0327 | 0.0201 | 0.0123 | 0.0341 | 0.0168 |
| RID | 0.0208 | 0.0122 | 0.0288 | 0.0153 | 0.0213 | 0.0178 | 0.0479 | 0.0277 | 0.0225 | 0.0159 | 0.0329 | 0.0193 |
| TID | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0182 | 0.0132 | 0.0432 | 0.0254 | 0.0058 | 0.0040 | 0.0086 | 0.0049 |
| IID | 0.0268 | 0.0151 | 0.0386 | 0.0195 | 0.0394 | 0.0268 | 0.0615 | 0.0341 | 0.0232 | 0.0146 | 0.0393 | 0.0197 |

Table 2から、単純な手法であるRIDやTIDは従来のベースライン（SASRecやS$^3$-Rec）を下回る結果となった。IIDはわずかに改善が見られるものの、すべてのアイテムに独立したトークンを用意するため学習コストが高い。

Table 3: An illustration of Sequential Indexing method.
| User | Train 1 | Train 2 | Train 3 | Train 4 | Train 5 | Train 6 | Train 7 | Train 8 | Train 9 | Train 10 | Validation | Testing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| User 1 | 1001 | 1002 | 1003 | 1004 | 1005 | 1006 | 1007 | 1008 | 1009 | ~ | 1018 | 1019 |
| User 2 | 1010 | 1011 | 1001 | 1012 | 1008 | 1009 | 1013 | 1014 | ~ | ~ | 1022 | 1023 |
| User 3 | 1015 | 1016 | 1017 | 1007 | 1018 | 1019 | 1020 | 1021 | 1009 | ~ | 1015 | 1016 |
| User 4 | 1022 | 1023 | 1005 | 1002 | 1006 | 1024 | ~ | ~ | ~ | ~ | 1002 | 1008 |
| User 5 | 1025 | 1026 | 1027 | 1028 | 1029 | 1030 | 1024 | 1020 | 1021 | 1031 | 1033 | 1034 |

![Illustration of spectral clustering on the item co-appearance graph based on spectral matrix factorization](./images/clustering.png)
*(a) Recursive spectral clustering on item co-appearance graph*

![Adjacency matrix](./images/adjacency.png)
*(b) Adjacency matrix*

![Laplacian matrix](./images/laplacian.png)
*(c) Laplacian matrix*
*Figure 1: Illustration of spectral clustering on the item co-appearance graph based on spectral matrix factorization*

![Collaborative indexing based on the spectral clustering tree](./images/SIGIR-AP_CID_example.png)
*Figure 2: Collaborative indexing based on the spectral clustering tree ($N=4$, $k=20$).*

![An example of semantic indexing](./images/SIGIR-AP_SID_example.png)
*Figure 3: An example of semantic indexing*

Table 4: Performance of all baseline results and all indexing methods under P5. 
| Method | Sports HR@5 | Sports NCDG@5 | Sports HR@10 | Sports NCDG@10 | Beauty HR@5 | Beauty NCDG@5 | Beauty HR@10 | Beauty NCDG@10 | Yelp HR@5 | Yelp NCDG@5 | Yelp HR@10 | Yelp NCDG@10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caser | 0.0116 | 0.0072 | 0.0194 | 0.0097 | 0.0205 | 0.0131 | 0.0347 | 0.0176 | 0.015 | 0.0099 | 0.0263 | 0.0134 |
| HGN | 0.0189 | 0.0120 | 0.0313 | 0.0159 | 0.0325 | 0.0206 | 0.0512 | 0.0266 | 0.0186 | 0.0115 | 0.0326 | 0.159 |
| GRU4Rec | 0.0129 | 0.0086 | 0.0204 | 0.0110 | 0.0164 | 0.0099 | 0.0283 | 0.0137 | 0.0176 | 0.0110 | 0.0285 | 0.0145 |
| BERT4Rec | 0.0115 | 0.0075 | 0.0191 | 0.0099 | 0.0203 | 0.0124 | 0.0347 | 0.0170 | 0.0051 | 0.0033 | 0.0090 | 0.0090 |
| FDSA | 0.0182 | 0.0122 | 0.0288 | 0.0156 | 0.0267 | 0.0163 | 0.0407 | 0.0208 | 0.0158 | 0.0098 | 0.0276 | 0.0136 |
| SASRec | 0.0233 | 0.0154 | 0.0350 | 0.0192 | 0.0387 | 0.0249 | 0.0605 | 0.0318 | 0.0170 | 0.0110 | 0.0284 | 0.0147 |
| S$^3$-Rec | 0.0251 | 0.0161 | 0.0385 | 0.0204 | 0.0387 | 0.0244 | 0.0647 | 0.0327 | 0.0201 | 0.0123 | 0.0341 | 0.0168 |
| RID | 0.0208 | 0.0122 | 0.0288 | 0.0153 | 0.0213 | 0.0178 | 0.0479 | 0.0277 | 0.0225 | 0.0159 | 0.0329 | 0.0193 |
| TID | 0.000 | 0.000 | 0.000 | 0.000 | 0.0182 | 0.0132 | 0.0432 | 0.0254 | 0.0058 | 0.0040 | 0.0086 | 0.0049 |
| IID | 0.0268 | 0.0151 | 0.0386 | 0.0195 | 0.0394 | 0.0268 | 0.0615 | 0.0341 | 0.0232 | 0.0146 | 0.0393 | 0.0197 |
| SID | 0.0264 | 0.0186 | 0.0358 | 0.0216 | 0.0430 | 0.0288 | 0.0602 | 0.0368 | 0.0346 | 0.0242 | 0.0486 | 0.0287 |
| CID | 0.0313 | 0.0224 | 0.0431 | 0.0262 | 0.0489 | 0.0318 | 0.0680 | 0.0357 | 0.0261 | 0.0171 | 0.0428 | 0.0225 |
| SemID | 0.0274 | 0.0193 | 0.0406 | 0.0235 | 0.0433 | 0.0299 | 0.0652 | 0.0370 | 0.0202 | 0.0131 | 0.0324 | 0.0170 |
| SID+IID | 0.0235 | 0.0161 | 0.0339 | 0.0195 | 0.0420 | 0.0297 | 0.0603 | 0.0355 | 0.0329 | 0.0236 | 0.0465 | 0.0280 |
| CID+IID | 0.0321 | 0.0227 | 0.0456 | 0.0270 | 0.0512 | 0.0356 | 0.0732 | 0.0427 | 0.0287 | 0.0195 | 0.0468 | 0.0254 |
| SemID+IID | 0.0291 | 0.0196 | 0.0436 | 0.0242 | 0.0501 | 0.0344 | 0.0724 | 0.0411 | 0.0229 | 0.0150 | 0.0382 | 0.0199 |
| SemID+CID | 0.0043 | 0.0031 | 0.0070 | 0.0039 | 0.0355 | 0.0248 | 0.0545 | 0.0310 | 0.0021 | 0.0016 | 0.0056 | 0.0029 |

Table 4の全体結果から、提案した高度なインデックス手法（SID, CID, SemID）は従来のベースラインを多くのケースで上回っている。特にCIDとSemIDが高い性能を示し、さらにハイブリッド手法であるCID+IIDとSemID+IIDが最も高い精度を記録した。一方でSemID+CIDのように単に2つの長いインデックスを連結する手法は性能が大きく低下した。

Table 5: Different settings of Sequential Indexing for P5 compared with two baselines on three datasets.
| Method | Sports HR@5 | Sports NCDG@5 | Sports HR@10 | Sports NCDG@10 | Beauty HR@5 | Beauty NCDG@5 | Beauty HR@10 | Beauty NCDG@10 | Yelp HR@5 | Yelp NCDG@5 | Yelp HR@10 | Yelp NCDG@10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SASRec | 0.0233 | 0.0154 | 0.0350 | 0.0192 | 0.0387 | 0.0249 | 0.0605 | 0.0318 | 0.0170 | 0.0110 | 0.0284 | 0.0147 |
| S$^3$-Rec | 0.0251 | 0.0161 | 0.0385 | 0.0204 | 0.0387 | 0.0244 | 0.0647 | 0.0327 | 0.0201 | 0.0123 | 0.0341 | 0.0168 |
| SID-TSO | 0.0264 | 0.0186 | 0.0358 | 0.0216 | 0.0430 | 0.0288 | 0.0602 | 0.0368 | 0.0346 | 0.0242 | 0.0486 | 0.0287 |
| SID-RO | 0.0214 | 0.0150 | 0.0291 | 0.0175 | 0.0392 | 0.0257 | 0.0512 | 0.0335 | 0.0324 | 0.0219 | 0.0461 | 0.0263 |
| SID-S2LO | 0.0304 | 0.0230 | 0.0395 | 0.0259 | 0.0395 | 0.0259 | 0.0520 | 0.0337 | 0.0335 | 0.0237 | 0.0442 | 0.0277 |
| SID-L2SO | 0.0244 | 0.0176 | 0.0356 | 0.0209 | 0.0409 | 0.0286 | 0.0586 | 0.0343 | 0.0316 | 0.0215 | 0.0472 | 0.0265 |

Table 5ではSIDのユーザーソート順（時系列・ランダム・系列長の昇降順）を比較している。時系列順（TSO）が高い性能を示しており、時間的に近いインタラクションを隣接するインデックスにまとめることが重要であることがわかる。

![CID Beauty ablations on N and k](./images/CF_ablation.png)
*Figure 4: CID Beauty ablations on $N$ (number of clusters at each level) and $k$ (maximum number of items allowed in the final cluster).*

![CID average length on Beauty](./images/beauty_length.png)
*Figure 5: CID average length on Beauty.*

Table 6: CID hit@10 results under different parameters and datasets. 
| Dataset | Sports $N$=10 | Sports $N$=20 | Beauty $N$=10 | Beauty $N$=20 | Yelp $N$=10 | Yelp $N$=20 |
|---|---|---|---|---|---|---|
| SASRec | 0.0350 | 0.0350 | 0.0605 | 0.0605 | 0.0284 | 0.0284 |
| S$^3$-Rec | 0.0385 | 0.0385 | 0.0647 | 0.0647 | 0.0341 | 0.0341 |
| $k$=200 | 0.0302 | 0.0423 | 0.0566 | 0.0635 | 0.0416 | 0.0428 |
| $k$=500 | 0.0400 | 0.0431 | 0.0680 | 0.0668 | 0.0388 | 0.0403 |
| $k$=1000 | 0.0435 | 0.0416 | 0.0658 | 0.0638 | 0.0385 | 0.0388 |

Table 7: Average ID lengths under different parameters.
| Dataset | Sports $N$=10 | Sports $N$=20 | Beauty $N$=10 | Beauty $N$=20 | Yelp $N$=10 | Yelp $N$=20 |
|---|---|---|---|---|---|---|
| $k$=200 | 4.25 | 3.35 | 4.31 | 3.23 | 3.88 | 3.25 |
| $k$=500 | 3.66 | 3.66 | 3.80 | 2.94 | 3.57 | 2.91 |
| $k$=1000 | 3.31 | 2.78 | 3.54 | 3.54 | 3.21 | 2.76 |

Figure 4, 5 および Table 6, 7から、CIDにおけるパラメータ $N$ と $k$ の影響を考察している。$k$ が小さすぎると新しいトークンの表現力が不足して精度が下がる。また、インデックスの平均長が3〜4トークン程度になる設定で最適なパフォーマンスが得られることが確認された。長すぎると生成難易度が上がり、短すぎると情報を保持しきれない。

Table 8: Examples of non-tree structure categories in Amazon Beauty dataset.
| | |
|---|---|
| Beauty > Skin Care > **Eyes** > Combinations | Beauty > Skin Care > Eyes > **Creams** |
| Beauty > Makeup > Makeup Remover > **Eyes** | Beauty > Makeup > Body > Moisturizers > **Creams** |

Table 9: SemID results under different settings.
| Method | Sports HR@5 | Sports NCDG@5 | Sports HR@10 | Sports NCDG@10 | Beauty HR@5 | Beauty NCDG@5 | Beauty HR@10 | Beauty NCDG@10 | Yelp HR@5 | Yelp NCDG@5 | Yelp HR@10 | Yelp NCDG@10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SASRec | 0.0233 | 0.0154 | 0.0350 | 0.0192 | 0.0387 | 0.0249 | 0.0605 | 0.0318 | 0.0170 | 0.0110 | 0.0284 | 0.0147 |
| S$^3$-Rec | 0.0251 | 0.0161 | 0.0385 | 0.0204 | 0.0387 | 0.0244 | 0.0647 | 0.0327 | 0.0201 | 0.0123 | 0.0341 | 0.0168 |
| SemID-non-tree | 0.0281 | 0.0192 | 0.0410 | 0.0233 | 0.0423 | 0.0288 | 0.0632 | 0.0354 | 0.0028 | 0.0019 | 0.0050 | 0.0025 |
| SemID-tree | 0.0274 | 0.0193 | 0.0406 | 0.0235 | 0.0433 | 0.0299 | 0.0652 | 0.0370 | 0.0202 | 0.0131 | 0.0324 | 0.0170 |

Table 8とTable 9はSemIDにおけるカテゴリツリー構造の重要性を示している。現実のデータでは同一のカテゴリ名（例：「Eyes」）が異なる親カテゴリの下に現れる（非ツリー構造）ことがあるが、これをそのまま同じトークンとして共有させる（non-tree）よりも、ツリー構造を強制して別のトークンとして扱う（tree）方が精度が高いことが実証された。階層的な検索空間の絞り込みが生成プロセスにおいて有益に働くためである。

総じて、LLMベースのレコメンドにおいて適切なインデックス（ID）を設計することは非常に重要であり、協調的な信号（CID）や意味的な情報（SemID）を階層的に組み込みつつ、各アイテムを最終的に区別するための独立トークンを付与するハイブリッド型（CID+IID等）が、生成の正確性と表現力のバランスを取り最も優れた結果をもたらすことが示された。
