# Towards Universal Sequence Representation Learning for Recommender Systems

## 背景
これまで逐次推薦（Sequential Recommendation）のモデルは、アイテムのIDをベースとして構築されることが主流でした。しかし、IDベースのモデルは新しい推薦シナリオ（新規ドメインやプラットフォーム）においてアイテムIDが共有されていない場合、モデルの知識を転移することができず、一から再学習するコストがかかるという課題（seesaw phenomenonやコールドスタート問題）がありました。
近年の自然言語処理（NLP）および事前学習済み言語モデル（PLM）の発展により、テキストを汎用的なセマンティックブリッジとして活用するアプローチが期待されていますが、生のテキスト表現を直接推薦モデルに導入するだけでは、特徴空間の異方性（Anisotropy）やドメイン間の意味的ギャップにより十分な効果が得られないことが分かった。

本論文では、明示的なアイテムIDに依存せず、商品のタイトルや説明などのテキスト情報（Item Text）を活用して汎用的で転移可能な系列表現を学習する手法「**UniSRec（Universal Sequence Representation Learning）**」を提案しています。

## 手法
UniSRecは、複数のドメインから得られる相互作用系列（Interaction Sequences）を入力とし、汎用的なアイテム表現と系列表現を学習します。

![Model Overview](./images/model.png)
**Figure 1: The overall framework of UniSRec.** (論文内 Figure 1)

### 1. 汎用的なテキスト・アイテム表現 (Universal Textual Item Representation)
アイテムのテキスト $t_i$ をBERTを用いてエンコードします。
$$ \bm{x}_i = \operatorname{BERT}([\texttt{[CLS]}; w_1, \ldots, w_c]) $$

BERTによって抽出される意味空間は非平滑で異方性（Anisotropy）を持つため、学習可能なパラメータを用いた**[Parametric Whitening (パラメトリック白色化)](../../../../一般教養/データ前処理/白色化/whitening.md)** を適用し、より等方的な（Isotropic）表現へと変換します。
$$ \widetilde{\bm{x}}_i = (\bm{x}_i-\bm{b}) \cdot \bm{W}_1 $$

ドメインの偏りを適応的になじませるため、Mixture-of-Experts (MoE) 強調型アダプタを導入し、複数の白色化変換器（エキスパート）から重み付けで最終的なアイテム表現を算出します。
$$ \bm{v}_i = \sum_{k=1}^{G} g_k \cdot \widetilde{\bm{x}}_i^{(k)} $$
ここで、ゲートとなる各重みは[ランダム適応ノイズ](../../../../一般教養/深層学習系/MoE/moe.md) $\bm{\delta}$ を用いながら算出され、ドメインの違いにより異なる比率でアイテムの意味が解釈されます。
$$ \bm{g} = \operatorname{Softmax}\left(\bm{x}_i \cdot \bm{W}_2 + \bm{\delta} \right) $$

### 2. 汎用的な系列表現 (Universal Sequence Representation)
Transformer（Self-Attentive）エンコーダを用いて取得した系列表現 $\bm{s}$ に対して、複数ドメインのデータが混在する際に特定のドメインばかり学習してしまう現象（Seesaw phenomenon）を防ぐために、2つの対照学習（Contrastive Learning）のタスクを導入しています。

**Sequence-Item Contrastive Task (系列-アイテム対照タスク)**  
シーケンスコンテキストと次に来るアイテムの相関を捉えるために行います。同一バッチ内の「別ドメインのアイテム（across-domain items）」も負例として扱うことで、ドメイン間共通の意味パターンを捉えやすくします。
$$ \ell_{S-I} = -\sum_{j=1}^{B} \log \frac{\exp{\left(\bm{s}_j\cdot\bm{v}_j/\tau\right)}}{\sum_{j'=1}^{B} \exp{\left(\bm{s}_j\cdot\bm{v}_{j'}/\tau\right)}} $$

**Sequence-Sequence Contrastive Task (系列-系列対照タスク)**  
元の系列からアイテムのランダム削除（Item drop）や単語の削除（Word drop）を行って生成した増強系列と元の系列との紐付けを学習させ、ノイズに強い系列表現を獲得します。
$$ \ell_{S-S} = -\sum_{j=1}^{B} \log \frac{\exp{\left(\bm{s}_j\cdot \widetilde{\bm{s}}_{j}/\tau\right)}}{\sum_{j'=1}^{B} \exp{\left(\bm{s}_j\cdot\bm{s}_{j'}/\tau\right)}} $$

事前学習全体の損失関数は、これらのマルチタスクとして以下のようになります。
$$ \mathcal{L}_{\text{PT}} = \ell_{S-I} + \lambda \cdot \ell_{S-S} $$


## 結果

### データセットの統計
前処理後のデータセット統計をTable 1に示します。事前学習にはAmazonの5カテゴリを使用し、Fine-tuningにはクロスドメインやクロスプラットフォームとして他のAmazonのカテゴリやOnline Retailのデータが使用されました。

**Table 1: Statistics of the datasets after preprocessing. ``Avg. $n$'' denotes the average length of item sequences. ``Avg. $c$'' denotes the average number of tokens in item text.**

| Datasets | #Users | #Items | #Inters. | Avg. $n$ | Avg. $c$ |
| :--- | ---: | ---: | ---: | ---: | ---: |
| **Pre-trained** | 1,361,408 | 446,975 | 14,029,229 | 13.51 | 139.34 |
| - Food | 115,349 | 39,670 | 1,027,413 | 8.91 | 153.40 |
| - CDs | 94,010 | 64,439 | 1,118,563 | 12.64 | 80.43 |
| - Kindle | 138,436 | 98,111 | 2,204,596 | 15.93 | 141.70 |
| - Movies | 281,700 | 59,203 | 3,226,731 | 11.45 | 97.54 |
| - Home | 731,913 | 185,552 | 6,451,926 | 8.82 | 168.89 |
| **Scientific** | 8,442 | 4,385 | 59,427 | 7.04 | 182.87 |
| **Pantry** | 13,101 | 4,898 | 126,962 | 9.69 | 83.17 |
| **Instruments** | 24,962 | 9,964 | 208,926 | 8.37 | 165.18 |
| **Arts** | 45,486 | 21,019 | 395,150 | 8.69 | 155.57 |
| **Office** | 87,436 | 25,986 | 684,837 | 7.84 | 193.22 |
| **Online Retail** | 16,520 | 3,469 | 519,906 | 26.90 | 27.80 |

### 全体性能 (Overall Performance)
提案手法（$\text{UniSRec}_{\text{Ind}}$ と $\text{UniSRec}_{\text{Tra}}$）を各種ベースラインと比較した結果をTable 2に示します。

**Table 2: Performance comparison of different recommendation models.**

| Scenario | Dataset | Metric | SASRec | BERT4Rec | FDSA | S$^3$-Rec | CCDR | RecGURU | ZESRec | UniSRec_T | UniSRec_ID | Improv. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cross-Domain | Scientific | Recall@10 | 0.1080 | 0.0488 | 0.0899 | 0.0525 | 0.0695 | 0.1023 | 0.0851 | 0.1188* | **0.1235*** | +14.35% |
| | | NDCG@10 | 0.0553 | 0.0243 | 0.0580 | 0.0275 | 0.0340 | 0.0572 | 0.0475 | **0.0641*** | 0.0634* | +10.52% |
| | | Recall@50 | 0.2042 | 0.1185 | 0.1732 | 0.1418 | 0.1647 | 0.2022 | 0.1746 | 0.2394* | **0.2473*** | +21.11% |
| | | NDCG@50 | 0.0760 | 0.0393 | 0.0759 | 0.0468 | 0.0546 | 0.0786 | 0.0670 | 0.0903* | **0.0904*** | +15.01% |
| | Pantry | Recall@10 | 0.0501 | 0.0308 | 0.0395 | 0.0444 | 0.0408 | 0.0469 | 0.0454 | 0.0636* | **0.0693*** | +38.32% |
| | | NDCG@10 | 0.0218 | 0.0152 | 0.0209 | 0.0214 | 0.0203 | 0.0209 | 0.0230 | 0.0306* | **0.0311*** | +35.22% |
| | | Recall@50 | 0.1322 | 0.1030 | 0.1151 | 0.1315 | 0.1262 | 0.1269 | 0.1141 | 0.1658* | **0.1827*** | +38.20% |
| | | NDCG@50 | 0.0394 | 0.0305 | 0.0370 | 0.0400 | 0.0385 | 0.0379 | 0.0378 | 0.0527* | **0.0556*** | +39.00% |
| | Instruments | Recall@10 | 0.1118 | 0.0813 | 0.1070 | 0.1056 | 0.0848 | 0.1113 | 0.0783 | 0.1189* | **0.1267*** | +13.33% |
| | | NDCG@10 | 0.0612 | 0.0620 | **0.0796** | 0.0713 | 0.0451 | 0.0681 | 0.0497 | 0.0680 | 0.0748* | - |
| | | Recall@50 | 0.2106 | 0.1454 | 0.1890 | 0.1927 | 0.1753 | 0.2068 | 0.1387 | 0.2255* | **0.2387*** | +13.34% |
| | | NDCG@50 | 0.0826 | 0.0756 | 0.0972 | 0.0901 | 0.0647 | 0.0887 | 0.0627 | 0.0912 | **0.0991*** | +1.95% |
| | Arts | Recall@10 | 0.1108 | 0.0722 | 0.1002 | 0.1003 | 0.0671 | 0.1084 | 0.0664 | 0.1066 | **0.1239*** | +11.82% |
| | | NDCG@10 | 0.0587 | 0.0479 | **0.0714** | 0.0601 | 0.0348 | 0.0651 | 0.0375 | 0.0586 | 0.0712 | - |
| | | Recall@50 | 0.2030 | 0.1367 | 0.1779 | 0.1888 | 0.1478 | 0.1979 | 0.1323 | 0.2049* | **0.2347*** | +15.62% |
| | | NDCG@50 | 0.0788 | 0.0619 | 0.0883 | 0.0793 | 0.0523 | 0.0845 | 0.0518 | 0.0799 | **0.0955*** | +8.15% |
| | Office | Recall@10 | 0.1056 | 0.0825 | 0.1118 | 0.1030 | 0.0549 | 0.1145 | 0.0641 | 0.1013 | **0.1280*** | +11.79% |
| | | NDCG@10 | 0.0710 | 0.0634 | **0.0868** | 0.0653 | 0.0290 | 0.0768 | 0.0391 | 0.0619 | 0.0831 | - |
| | | Recall@50 | 0.1627 | 0.1227 | 0.1665 | 0.1613 | 0.1095 | 0.1757 | 0.1113 | 0.1702 | **0.2016*** | +14.74% |
| | | NDCG@50 | 0.0835 | 0.0721 | 0.0987 | 0.0780 | 0.0409 | 0.0901 | 0.0493 | 0.0769 | **0.0991** | +0.41% |
| Cross-Platform | Online Retail | Recall@10 | 0.1460 | 0.1349 | 0.1490 | 0.1418 | 0.1347 | 0.1467 | 0.1103 | 0.1449 | **0.1537*** | +3.15% |
| | | NDCG@10 | 0.0675 | 0.0653 | 0.0719 | 0.0654 | 0.0620 | 0.0658 | 0.0535 | 0.0677 | **0.0724** | +0.70% |
| | | Recall@50 | 0.3872 | 0.3540 | 0.3802 | 0.3702 | 0.3587 | **0.3885** | 0.2750 | 0.3604 | **0.3885** | 0.00% |
| | | NDCG@50 | 0.1201 | 0.1131 | 0.1223 | 0.1154 | 0.1108 | 0.1188 | 0.0896 | 0.1149 | **0.1239*** | +1.31% |

結果から、IDフリーの帰納的設定 (Inductive setting: $\text{UniSRec}_{\text{Ind}}$) においても、提案手法は他のベースラインに匹敵あるいは上回る性能を発揮しており、IDと組み合わせたトランスダクティブな設定 (Transductive setting: $\text{UniSRec}_{\text{ID}}$) では一貫して最高の精度を記録しました。

**Table 3: Comparison of the transfer learning scenarios and application settings of several approaches.**

| Methods | Transfer Learning Scenarios: $1 \rightarrow 1$ | Transfer Learning Scenarios: $M \rightarrow N$ | Transfer Learning Scenarios: Non-OL | Application Settings: Transductive | Application Settings: Inductive |
| :--- | :---: | :---: | :---: | :---: | :---: |
| S$^3$-Rec | × | × | × | ✓ | × |
| PeterRec | ✓ | × | × | ✓ | × |
| RecGURU | ✓ | × | ✓ | ✓ | × |
| ZESRec | ✓ | × | ✓ | × | ✓ |
| UniSRec (ours)| ✓ | ✓ | ✓ | ✓ | ✓ |

既存の大半のベースラインは単一ドメイン間転移 ($1 \rightarrow 1$) や、ユーザやアイテムのオーバーラップ (Non-OL) を必要としますが、UniSRecはオーバーラップのない複数ドメイン ($M \rightarrow N$) 間での転移を実現し、帰納的およびトランスダクティブの両対応していることが強みです（Table 3）。

### 更なる分析
![Pre-training Dataset Comparison](./images/pt_domain.png)
**Figure 2: Performance comparison \wrt different pre-training datasets.** (論文内 Figure 2)
Figure 2は事前学習に利用したデータセットの組み合わせの分析を示しています。「All」として全てのデータセットで事前学習した際が最も性能向上に寄与しており、多様なドメインデータによる事前学習が悪影響（シーソー現象）をもたらすことなく恩恵を与えられることが分かります。

![Ablation Study Scientific](./images/ablation_sci.png)
![Ablation Study Online Retail](./images/ablation_or.png)
**Figure 3: Ablation study of UniSRec variants on "Scientific" and "Online Retail".** (論文内 Figure 3)

Figure 3のAblation Studyにより、Parametric Whitening (PW) やMoEなどが欠如した場合、学習性能が明確に低下することが判明しました。特にMoEなし($w/o$ MoE)の精度低下が著しく、ドメインの偏りを適応的になじませる機構として鍵となっていることが裏付けられました。

![Cold Start Scientific](./images/cold_start_sci.png)
![Cold Start Online Retail](./images/cold_start_or.png)
**Figure 4: Performance comparison \wrt long-tail items.** (論文内 Figure 4)
Figure 4は学習データでの出現回数が少ないロングテールアイテム（コールドスタートアイテム）に対する性能を示しています。出現回数が極めて少ない（[0, 5)など）カテゴリにおいて他のベースラインを大きく引き離して改善されており、ユニバーサルアプローチがコールドスタート問題の解決に有効であることが実証されました。

![Case Study](./images/case.png)
**Figure 5: The purchase history of a user in the source platform and an anonymous session in the target platform.** (論文内 Figure 5)
最後に著者らは、AmazonからOnline Retailへのクロスプラットフォーム転移が成功した要因として、テキストとしての普遍的な「Dog $\rightarrow$ Cat」の関連性などのシーケンシャルパターンが、言語に依存しない意味空間上で捉えられたことをFigure 5で定性的に確認しています。

## chokosenlovetiの考察

### UniSRec時点におけるテキスト単体モデルの限界と、ID情報のアドバンテージ
本論文（UniSRec, 2022年）の大きな功績は、「テキスト表現の異方性を緩和し、IDに依存しないパラダイム（帰納的設定）を築くことで、未知のアイテムに対して高い推薦精度を出せること」を証明した点にあります。

しかし、実験結果の全体性能表（Table 2）などを俯瞰すると、通常の推論環境（自身が既に学習済みのアイテムを推論するトランスダクティブ設定）において、最終的に最も高い精度を叩き出しているのは「テキスト表現」と「ID表現」をハイブリッドさせたモデル（$\text{UniSRec}_{\text{ID}}$）です。

つまり、本論文の時点では**「テキストだけを用いた表現は汎用性や未知への対応力は高いものの、通常の推薦シナリオにおいては、ユーザーの過去の行動履歴（共に買われたという共起パターン）を直接記憶・学習できる『アイテムID』ベースのアドバンテージ（記憶力）には完全には勝てない」**というのが技術の限界でした。
