# A Critical Study on Data Leakage in Recommender System Evaluation

## 背景
推薦システム（Recommender System）のオフライン評価においては、現実世界の運用に即した評価が求められる。しかし、多くの研究では「グローバルな時間軸（Global Timeline）」が無視されている。アイテムのリリース日やユーザーが活動を開始したタイミングといった時間的な文脈が考慮されず、データ全体が静的なセットとして扱われることが多い。
特に、データ分割において Random-split や、ユーザーごとの最後のインタラクションをテストデータにする Leave-one-out-split が一般的に用いられているが、これらはグローバルな時間軸を守っていないため、テストインスタンスが発生した時点より「未来」のデータが学習用データ（Training data）に混入してしまう。これにより、協調フィルタリング（Collaborative Filtering）を介してモデルが未来の情報を事前に学習してしまう「データリーク（Data Leakage）」が発生する。
本研究は、このデータリークが推薦システムの評価に及ぼす影響を詳細に検証し、その深刻さを明らかにした上で、より現実的で公平な評価を行うための「Timeline Scheme（タイムラインスキーム）」を提唱している。

## 手法
データリークの影響を検証するため、MovieLens-25M, Yelp, Amazon-music, Amazon-electronic の4つのデータセットを用い、BPR, NeuMF, SASRec, LightGCN の4つのベースラインモデルを評価した。
検証では Leave-one-out-split を採用しつつ、時間軸を1年ごとに区切り、例えば「5年目（Y5）」のテストデータを評価する際に、本来であればアクセスできないはずの「6年目（Y6）から10年目（Y10）」の「未来のデータ（Future data）」を学習データに段階的に追加することで、データリークの度合いを意図的に変化させる実験を行った。

![Train/test data split for test year Y5 as an example.](./images/TrainTest.png)
![User-item interaction along global timeline.](./images/UserItemTime.png)
![User-item interaction matrix](./images/UserItemMatrix.png)

また、これらデータリークの問題を解決するために提案されたのが **Timeline Scheme（タイムラインスキーム）** である。この手法は以下のように設計されている。
1. 全てのユーザーとアイテムのインタラクションをグローバルな時間順にソートする。
2. 推薦モデルは時間軸に沿って逐次的に学習（インクリメンタル学習、もしくは過去の履歴のみを用いたバッチ再学習）を行う。
3. テストデータ（推薦を要求される時点）に遭遇した際には、その時点までに学習したデータと、その時点でシステム上に存在するアイテムのみを用いて予測を行う。
これにより、未来のデータへのアクセスを遮断し、時間的な文脈を捉えた現実的なオフライン評価が可能となる。

![An illustration of the timeline scheme.](./images/timeline_scheme.png)

## 結果

### 1. データセットと評価戦略の統計
実験に用いたデータセットの統計量（Table 1）と、オフライン評価において用いられるデータ分割手法とデータリークの有無（Table 2）、および各テスト年における学習・テストデータの追加状況（Table 3）は以下の通りである。

**Table 1: Statistics of the four datasets used in this study**
| Dataset | Time span selected | Data filtering | #User | #Item | #Interaction |
|---|---|---|---|---|---|
| MovieLens-25M | 21/11/2009 to 20/11/2019 | No filtering | 62,202 | 56,774 | 9,808,925 |
| Yelp | 13/12/2009 to 12/12/2019 | 10-core | 116,655 | 61,027 | 3,127,215 |
| Amazon-music | 02/10/2008 to 01/10/2018 | 5-core | 11,651 | 9,243 | 114,833 |
| Amazon-electronic | 05/10/2008 to 04/10/2018 | 10-core | 109,990 | 39,552 | 1,752,238 |

**Table 2: Commonly used data split strategies in offline evaluation of recommender systems**
| Data split strategy | Definition of training and test instances | Local timeline | Global timeline | Data leakage |
|---|---|---|---|---|
| Random-split-by-ratio | Randomly sample a percentage of user-item interactions as test instances; the remaining are training instances. | No | No | Yes |
| Random-split-by-user | Randomly sample a percentage of users, and take all their interactions as test instances; the remaining instances from other users are training instances. | No | No | Yes |
| Leave-one-out-split | Take each user's last interaction as a test instance; all remaining interactions are training instances. | Yes | No | Yes |
| Split-by-timepoint | All interactions after a time point are test instances; interactions before this time point are training instances. | No | Yes | No |

**Table 3: Number of test and training instances for test years Y5 and Y7**
| Dataset | Test year | #Test instances | Y5 | Y6 | Y7 | Y8 | Y9 | Y10 |
|---|---|---|---|---|---|---|---|---|
| MovieLens-25M | Y5 | 3,171 | 2,489,066 | 3,876,800 | 5,602,278 | 7,243,348 | 8,474,179 | 9,805,754 |
| MovieLens-25M | Y7 | 9,232 | - | - | 5,596,217 | 7,237,287 | 8,468,118 | 9,799,693 |
| Yelp | Y5 | 3,093 | 878,494 | 1,280,070 | 1,723,554 | 2,203,266 | 2,702,445 | 3,124,122 |
| Yelp | Y7 | 7,241 | - | - | 1,719,406 | 2,199,118 | 2,698,297 | 3,119,974 |
| Amazon-music | Y5 | 829 | 18,283 | 38,873 | 71,227 | 95,571 | 108,496 | 114,004 |
| Amazon-music | Y7 | 2,686 | - | - | 69,370 | 93,714 | 106,639 | 112,147 |
| Amazon-electronic | Y5 | 652 | 234,398 | 479,507 | 898,947 | 1,317,418 | 1,607,543 | 1,751,586 |
| Amazon-electronic | Y7 | 8,747 | - | - | 890,852 | 1,309,323 | 1,599,448 | 1,743,491 |

ユーザーやアイテムの平均的な活動期間は短く、全体のタイムライン（10年）のごく一部しか活動していないことが可視化されている。
![Mean active time period in years.](./images/userItemMeanActiveness.png)
![Median active time period in years](./images/userItemMedianActiveness.png)
![Activeness of Ipad models](./images/ipad_pop.png)
![Ipad models' official release dates and their IDs in Amazon-electronic dataset](./images/ipad_pop_legend.png)
![MovieLens-25M Popularity](./images/movielens_pop.png)
![Yelp Popularity](./images/yelp_pop.png)
![MovieLens-25M weekly activity with release log](./images/movielens_weekly_activity_with_release_log.png)
![Yelp weekly activity with release log](./images/yelp_weekly_activity_with_release_log.png)
![Amazon-music weekly activity with release log](./images/amazonm_weekly_activity_with_release_log.png)
![Amazon-electronic weekly activity with release log](./images/amazone_weekly_activity_with_release_log.png)

### 2. 「未来のアイテム」の推薦（Top-N Recommendation Listへの影響）
未来のデータが追加されるにつれ、本来テスト時点ではリリースされておらず存在し得ない「未来のアイテム」が推薦リストに含まれるようになることが確認された。
Table 4 に示されるように、Y5 あるいは Y7 のテストインスタンスに対して、未来のデータを用いたモデルは数百から数千の未来のアイテムを推薦してしまっている。これは現在のオフライン評価の手法が破綻している強力な証拠である。

**Table 4: Among top-20 recommendations, the total number of future items recommended for test instances in Y5 and Y7**
| Model | Dataset | MovieLens-25M Y5 | MovieLens-25M Y7 | Yelp Y5 | Yelp Y7 | Amazon-music Y5 | Amazon-music Y7 | Amazon-electronic Y5 | Amazon-electronic Y7 |
|---|---|---|---|---|---|---|---|---|---|
| BPR Y5 | | 0 | - | 0 | - | 0 | - | 0 | - |
| BPR Y6 | | 0 | - | 421 | - | 615 | - | 79 | - |
| BPR Y7 | | 22 | 0 | 829 | 0 | 970 | 0 | 363 | 0 |
| BPR Y8 | | 7 | 11 | 2,365 | 504 | 1,101 | 651 | 263 | 200 |
| BPR Y9 | | 6 | 88 | 5,048 | 287 | 1,304 | 1,103 | 499 | 1,224 |
| BPR Y10 | | 4 | 81 | 1,851 | 1,598 | 1,197 | 1,155 | 200 | 583 |
| NeuMF Y5 | | 0 | - | 0 | - | 0 | - | 0 | - |
| NeuMF Y6 | | 3 | - | 602 | - | 910 | - | 28 | - |
| NeuMF Y7 | | 7 | 0 | 1,631 | 0 | 1,501 | 0 | 1,303 | 0 |
| NeuMF Y8 | | 27 | 31 | 3,260 | 130 | 1,733 | 878 | 549 | 0 |
| NeuMF Y9 | | 22 | 6 | 3,542 | 1,177 | 1,491 | 1,276 | 729 | 216 |
| NeuMF Y10 | | 15 | 1 | 5,205 | 1,791 | 1,577 | 1,573 | 2,655 | 326 |
| LightGCN Y5 | | 0 | - | 0 | - | 0 | - | 0 | - |
| LightGCN Y6 | | 11 | - | 369 | - | 626 | - | 37 | - |
| LightGCN Y7 | | 32 | 0 | 739 | 0 | 1,050 | 0 | 148 | 0 |
| LightGCN Y8 | | 116 | 189 | 1,070 | 569 | 998 | 632 | 367 | 220 |
| LightGCN Y9 | | 22 | 26 | 1,257 | 979 | 1,036 | 893 | 262 | 430 |
| LightGCN Y10 | | 15 | 58 | 1,103 | 1,360 | 1,152 | 1,029 | 260 | 470 |
| SASRec Y5 | | 0 | - | 0 | - | 0 | - | 0 | - |
| SASRec Y6 | | 315 | - | 967 | - | 906 | - | 216 | - |
| SASRec Y7 | | 442 | 0 | 3,074 | 0 | 1,548 | 0 | 625 | 0 |
| SASRec Y8 | | 144 | 489 | 2,228 | 2,666 | 1,814 | 1,341 | 487 | 1388 |
| SASRec Y9 | | 342 | 403 | 3,162 | 2,893 | 1,982 | 1,376 | 20 | 3,209 |
| SASRec Y10 | | 993 | 386 | 1,741 | 3,014 | 1,980 | 1,662 | 12 | 2,479 |

また、Jaccard類似度を用いた分析（Figure 4）によって、未来のデータが増加するにつれて、データリークなしの場合（Y5まで）の推薦リストから著しく推薦内容が変容していくことが確認された。
![Legend for similarity](./images/legend.png)
![Y5, LightGCN on MovieLens-25M](./images/recList_lightgcn_movielens_5.png)
![Y7, SASRec on Amazon-electronic](./images/recList_sasrec_amazone_7.png)

### 3. 推薦精度への予測不可能な影響
データリークが含まれる場合、単純に未来のデータ量が増えれば推薦精度が向上するという一貫した傾向はなく、性能の向上と悪化が入り混じる「予測不可能」な影響が見られた（Figure 5、Table 5）。

![MovieLens-25M Y5HR20](./images/movielens_Y5HR20.png)
![MovieLens-25M Y5NDCG20](./images/movielens_Y5NDCG20.png)
![Yelp Y5HR20](./images/yelp_Y5HR20.png)
![Yelp Y5NDCG20](./images/yelp_Y5NDCG20.png)
![Amazon-music Y5HR20](./images/amazonm_Y5HR20.png)
![Amazon-music Y5NDCG20](./images/amazonm_Y5NDCG20.png)
![Amazon-electronic Y5HR20](./images/amazone_Y5HR20.png)
![Amazon-electronic Y5NDCG20](./images/amazone_Y5NDCG20.png)

**Table 5: Lowest, highest performance changes (in percentage)**
| Dataset | Metric | BPR | NeuMF | LightGCN | SASRec |
|---|---|---|---|---|---|
| MovieLens-25M | HR@20 | -8.0%, +2.3% | -4.1%, +0.9% | -3.8%, +11.1% | -5.3%, +17.2% |
| MovieLens-25M | NDCG@20 | -6.3%, +5.5% | -1.5%, +2.0% | -9.3%, +6.8% | -5.4%, +16.8% |
| Yelp | HR@20 | -17.8%, +9.2% | -6.1%, +18.3% | -0.3%, +10.8% | -13.6%, +1.9% |
| Yelp | NDCG@20 | -13.9%, +15.4% | -6.6%, +18.3% | -0.5%, +8.0% | -29.0%, -0.6% |
| Amazon-music | HR@20 | +19.3%, +37.2% | +39.6%, +65.6% | 0%, +22.8% | -5.4%, +3.3% |
| Amazon-music | NDCG@20 | +23.6%, +51.8% | +40.2%, +89.5% | +1.9%, +32.7% | -3.4%, +6.3% |
| Amazon-electronic | HR@20 | +6.4%, +22.9% | -38.1%, +14.3% | -9.7%, +22.4% | -7.5%, +62.5% |
| Amazon-electronic | NDCG@20 | +10.3%, +22.0% | -35.5%, +13.8% | -7.7%, +24.1% | -3.3%, +73.0% |

さらに、最も深刻な問題として、未来のデータが追加されるにつれて4つのベースラインモデルの**順位（Ranking order）が一貫せず変動する**ことが Table 6 によって示された。このため、データリークを含む現在のオフライン評価の枠組みでは、どのモデルが真に優れているかを比較・検証することは事実上不可能であることが示された。

**Table 6: Ranking order of BPR, NeuMF, SASRec, and LightGCN in terms of HR@20 for test year Y5**
| Dataset | Train Year | BPR | NeuMF | SASRec | LightGCN |
|---|---|---|---|---|---|
| MovieLens-25M | Y5 | 2 | 3 | 1 | 4 |
| MovieLens-25M | Y6 | 3 | 4 | 1 | 2 |
| MovieLens-25M | Y7 | 2 | 3 | 1 | 4 |
| MovieLens-25M | Y8 | 4 | 2 | 1 | 3 |
| MovieLens-25M | Y9 | 3 | 2 | 1 | 4 |
| MovieLens-25M | Y10 | 4 | 3 | 1 | 2 |
| Yelp | Y5 | 3 | 4 | 2 | 1 |
| Yelp | Y6 | 3 | 4 | 2 | 1 |
| Yelp | Y7 | 2 | 4 | 3 | 1 |
| Yelp | Y8 | 3 | 4 | 2 | 1 |
| Yelp | Y9 | 3 | 4 | 2 | 1 |
| Yelp | Y10 | 2 | 4 | 3 | 1 |
| Amazon-music | Y5 | 2 | 4 | 3 | 1 |
| Amazon-music | Y6 | 1 | 3 | 4 | 2 |
| Amazon-music | Y7 | 1 | 3 | 4 | 2 |
| Amazon-music | Y8 | 2 | 3 | 4 | 1 |
| Amazon-music | Y9 | 2 | 3 | 4 | 1 |
| Amazon-music | Y10 | 1 | 3 | 4 | 2 |
| Amazon-electronic | Y5 | 2 | 3 | 4 | 1 |
| Amazon-electronic | Y6 | 2 | 3 | 4 | 1 |
| Amazon-electronic | Y7 | 2 | 3 | 4 | 1 |
| Amazon-electronic | Y8 | 1 | 3 | 4 | 2 |
| Amazon-electronic | Y9 | 2 | 4 | 3 | 1 |
| Amazon-electronic | Y10 | 3 | 4 | 2 | 1 |

結論として、オフライン評価においてモデルの再現性および現実性を担保するためには、Timeline Scheme のような「グローバルな時間軸」に厳格に従った枠組みの導入が不可欠であり、推薦モデル自体もそのような経時的なデータ追加に対応できる（インクリメンタルな）設計が求められると筆者らは考察している。
