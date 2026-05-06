# Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders

## 背景
近年、自然言語テキストの汎用性を活かして、複数ドメイン間で転移可能なレコメンドモデル（Transferable Recommender）を構築する研究が注目を集めています。その基本的なアイデアは、事前学習済み言語モデル（PLM）を用いてアイテムのテキスト情報をアイテム表現（エンベディング）にエンコードすることです（例：UniSRecなど）。
しかし、このアプローチには、アイテムテキストとアイテム表現が「強固に結びつきすぎている（too tight）」という問題がありました。その結果、テキスト特徴量への依存が過剰になり、ノイズの影響を受けやすくなるだけでなく、ドメイン間のセマンティックなギャップの悪影響が増幅されてしまうという課題がありました。本論文ではこの問題に対処するため、テキストから直接連続値のアイテム表現を得るのではなく、**ベクトル量子化（Vector-Quantized）**を用いた離散コードを間に挟む新しい転移可能なアイテム表現スキーム「**VQ-Rec**」を提案しています。

## 手法
本論文では、「**text $\Longrightarrow$ code $\Longrightarrow$ representation**」という2段階の新しいアイテム表現スキームを導入しました。

1. **テキストのエンコーディング**: 
   アイテムのテキスト $t_i$ を、BERT（固定パラメータ）を用いてテキストエンコーディング $\bm{x}_i$ に変換します。
   $$ \bm{x}_i = \text{BERT}([\text{\texttt{[CLS]}};w_1;\ldots;w_c]) $$
2. **Product Quantization (PQ) による離散コードの生成**:
   $\bm{x}_i$ を $D$ 個のサブベクトルに分割し、Optimized Product Quantization (OPQ) を用いて事前に学習した各部分空間のセントロイド（コードブック）の中で最も近いインデックスを選択します。これにより、アイテムは離散コードのベクトル $\bm{c}_i = (c_{i,1},\ldots, c_{i,D})$ として表現されます。
   $$ c_{i,k} = \arg \min_{j} \|\bm{x}_{i,k}-\bm{a}_{k,j}\|^2 $$
3. **コードからアイテム表現へのマッピング (Code Embedding Lookup)**:
   各次元 $k$ について、独立したコード埋め込み行列 $\bm{E}^{(k)}$ をルックアップし、得られたベクトルを平均プーリングして最終的なアイテム表現 $\bm{v}_i$ を得ます。
   $$ \bm{v}_i = \text{Pool}([\bm{e}_{1,c_{i,1}};\ldots;\bm{e}_{D,c_{i,D}}]) $$
4. **コントラスト事前学習 (Contrastive Pre-training)**:
   ランダムな負例サンプリングでは表現空間がスパースになる（アイテムを見分けるのが簡単すぎて学習が早期に停滞し、細かな意味の違いを捉えきれない）問題に対処するため、以下の2種類の高度な負例サンプリングを組み合わせた拡張コントラスト学習を行います。
   - **セミシンセティックなハードネガティブ（Semi-synthetic negatives）**: 元のアイテムを表す離散コード配列のうち、ごく一部のコードだけをランダムに置換して架空のアイテムを生成します。大部分のコードが共通しているため「元のアイテムと意味的に非常に近いが異なる」ハードネガティブとなり、モデルにミクロな意味の違い（アイテム間の微細な識別）を強制的に学習させます。
   - **ミックスドメインネガティブ（Mixed-domain negatives）**: 事前学習のバッチ内に含まれる「他ドメインのアイテム」を意図的に負例として利用します。他ドメインのアイテムを押し退けることで、表現空間全体の中で「ドメイン間の境界線」というマクロな構造を整理し、未知のドメインに対する転移能力（Transferability）を向上させます。
5. **ドメイン適応のためのファインチューニング (Code-Embedding Alignment)**:
   ターゲットとなる新しいドメインに適応する際、Transformer（シーケンスエンコーダ）のパラメータは固定し、PQのインデックスセットを再利用しつつ、新しいドメインの特性に合わせて「コードと埋め込みのマッピング」を再構築します。これを実現するために、Gumbel-Sinkhornアルゴリズムを用いた微分可能な置換行列（Permutation matrix） $\bm{\Pi}_k$ を導入し、マッピングのアライメントを学習します。
   $$ \hat{\bm{E}}^{(k)} = \bm{\Pi}_k \cdot \bm{E}^{(k)} $$

## 結果

以下の各図表は、提案手法（VQ-Rec）の有効性を様々な観点から検証した結果です。

### データセットの統計情報
Table 1には、本実験で用いられた事前学習（Pre-trained）および下流タスク（Scientific, Pantry, Instruments, Arts, Office, Online Retail）のデータセット統計が示されています。

#### Table 1
| \textbf{Datasets} | \textbf{\#Users} | \textbf{\#Items} | \textbf{\#Inters.} | \textbf{Avg. $n$} | \textbf{Avg. $c$} |
| :--- | ---: | ---: | ---: | ---: | ---: |
| \textbf{Pre-trained} | 1,361,408 | 446,975 | 14,029,229 | 13.51 | 139.34 |
| \textbf{Scientific} | 8,442 | 4,385 | 59,427 | 7.04 | 182.87 |
| \textbf{Pantry} | 13,101 | 4,898 | 126,962 | 9.69 | 83.17 |
| \textbf{Instruments} | 24,962 | 9,964 | 208,926 | 8.37 | 165.18 |
| \textbf{Arts} | 45,486 | 21,019 | 395,150 | 8.69 | 155.57 |
| \textbf{Office} | 87,436 | 25,986 | 684,837 | 7.84 | 193.22 |
| \textbf{Online Retail} | 16,520 | 3,469 | 519,906 | 26.90 | 27.80 |

### 全体構造とアーキテクチャ
![Figure 1: The overall framework of the proposed vector-quantized code-based transferable sequential recommender VQ-Rec.](./images/model.png)
Figure 1はVQ-Recの全体的なフレームワークを示しています。アイテムテキストからPQを経て離散コードを抽出し、事前学習ではSemi-synthetic negative等を用いたContrastive Learningを実施、ファインチューニング時にはPermutation Networkでドメインごとのアライメントを調整する様子が視覚化されています。

### モデルの性能比較
Table 2では、複数ドメイン（Cross-Domain）および複数プラットフォーム（Cross-Platform）における他の強力なベースライン（SASRec, BERT4Rec, FDSA, S3-Rec, RecGURU, UniSRec等）との比較結果が示されています。

#### Table 2
| \textbf{Scenario} | \textbf{Dataset} | \textbf{Metric} | \textbf{SASRec} \textsubscript{ID} | \textbf{BERT4Rec} \textsubscript{ID} | \textbf{FDSA} \textsubscript{ID+T} | \textbf{S$^3$-Rec} \textsubscript{ID+T} | \textbf{RecGURU} \textsubscript{ID} | \textbf{SASRec} \textsubscript{T} | \textbf{ZESRec} \textsubscript{T} | \textbf{UniSRec} \textsubscript{T} | \textbf{VQ-Rec} \textsubscript{T} |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cross-Domain | Scientific | R@10 | 0.1080 | 0.0488 | 0.0899 | 0.0525 | 0.1023 | 0.0994 | 0.0851 | 0.1188 | **0.1211** |
| Cross-Domain | Scientific | N@10 | 0.0553 | 0.0243 | 0.0580 | 0.0275 | 0.0572 | 0.0561 | 0.0475 | 0.0641 | **0.0643** |
| Cross-Domain | Scientific | R@50 | 0.2042 | 0.1185 | 0.1732 | 0.1418 | 0.2022 | 0.2162 | 0.1746 | **0.2394** | 0.2369 |
| Cross-Domain | Scientific | N@50 | 0.0760 | 0.0393 | 0.0759 | 0.0468 | 0.0786 | 0.0815 | 0.0670 | **0.0903** | 0.0897 |
| Cross-Domain | Pantry | R@10 | 0.0501 | 0.0308 | 0.0395 | 0.0444 | 0.0469 | 0.0585 | 0.0454 | 0.0636 | **0.0660** |
| Cross-Domain | Pantry | N@10 | 0.0218 | 0.0152 | 0.0209 | 0.0214 | 0.0209 | 0.0285 | 0.0230 | **0.0306** | 0.0293 |
| Cross-Domain | Pantry | R@50 | 0.1322 | 0.1030 | 0.1151 | 0.1315 | 0.1269 | 0.1647 | 0.1141 | 0.1658 | **0.1753** |
| Cross-Domain | Pantry | N@50 | 0.0394 | 0.0305 | 0.0370 | 0.0400 | 0.0379 | 0.0523 | 0.0378 | **0.0527** | **0.0527** |
| Cross-Domain | Instruments | R@10 | 0.1118 | 0.0813 | 0.1070 | 0.1056 | 0.1113 | 0.1127 | 0.0783 | 0.1189 | **0.1222** |
| Cross-Domain | Instruments | N@10 | 0.0612 | 0.0620 | **0.0796** | 0.0713 | 0.0681 | 0.0661 | 0.0497 | 0.0680 | 0.0758 |
| Cross-Domain | Instruments | R@50 | 0.2106 | 0.1454 | 0.1890 | 0.1927 | 0.2068 | 0.2104 | 0.1387 | 0.2255 | **0.2343** |
| Cross-Domain | Instruments | N@50 | 0.0826 | 0.0756 | 0.0972 | 0.0901 | 0.0887 | 0.0873 | 0.0627 | 0.0912 | **0.1002** |
| Cross-Domain | Arts | R@10 | 0.1108 | 0.0722 | 0.1002 | 0.1003 | 0.1084 | 0.0977 | 0.0664 | 0.1066 | **0.1189** |
| Cross-Domain | Arts | N@10 | 0.0587 | 0.0479 | **0.0714** | 0.0601 | 0.0651 | 0.0562 | 0.0375 | 0.0586 | 0.0703 |
| Cross-Domain | Arts | R@50 | 0.2030 | 0.1367 | 0.1779 | 0.1888 | 0.1979 | 0.1916 | 0.1323 | 0.2049 | **0.2249** |
| Cross-Domain | Arts | N@50 | 0.0788 | 0.0619 | 0.0883 | 0.0793 | 0.0845 | 0.0766 | 0.0518 | 0.0799 | **0.0935** |
| Cross-Domain | Office | R@10 | 0.1056 | 0.0825 | 0.1118 | 0.1030 | 0.1145 | 0.0929 | 0.0641 | 0.1013 | **0.1236** |
| Cross-Domain | Office | N@10 | 0.0710 | 0.0634 | **0.0868** | 0.0653 | 0.0768 | 0.0582 | 0.0391 | 0.0619 | 0.0814 |
| Cross-Domain | Office | R@50 | 0.1627 | 0.1227 | 0.1665 | 0.1613 | 0.1757 | 0.1580 | 0.1113 | 0.1702 | **0.1957** |
| Cross-Domain | Office | N@50 | 0.0835 | 0.0721 | **0.0987** | 0.0780 | 0.0901 | 0.0723 | 0.0493 | 0.0769 | 0.0972 |
| Cross-Platform | Online Retail | R@10 | 0.1460 | 0.1349 | 0.1490 | 0.1418 | 0.1467 | 0.1380 | 0.1103 | 0.1449 | **0.1557** |
| Cross-Platform | Online Retail | N@10 | 0.0675 | 0.0653 | 0.0719 | 0.0654 | 0.0658 | 0.0672 | 0.0535 | 0.0677 | **0.0730** |
| Cross-Platform | Online Retail | R@50 | 0.3872 | 0.3540 | 0.3802 | 0.3702 | 0.3885 | 0.3516 | 0.2750 | 0.3604 | **0.3994** |
| Cross-Platform | Online Retail | N@50 | 0.1201 | 0.1131 | 0.1223 | 0.1154 | 0.1188 | 0.1137 | 0.0896 | 0.1149 | **0.1263** |

筆者らの考察として、VQ-Recはほとんどのデータセットで既存手法（特にテキスト表現をそのまま使うUniSRec等）を上回る結果を出しています。これは、連続値のテキスト表現をそのまま用いるよりも、一度離散的なコードブックを経由することでドメイン間のギャップをうまく吸収し、表現の一般化能力が向上していることを示しています。

### 転移学習とドメイン適応の効果
![Figure 3: Relative improvement comparison ratios through transferring for Recall@10 \wrt different downstream datasets. Below the line denotes negative transfer.](./images/transfer.png)
Figure 3は転移学習によるRecall@10の相対的な性能向上率を示しています。ベースラインではゼロ以下の「負の転移（Negative Transfer）」が起きやすいドメイン（Pantry等）でも、VQ-Recは安定してプラスの転移を実現しており、提案するCode-Embedding Alignmentの有効性が裏付けられています。

### アブレーションスタディ
#### Table 3
| \textbf{Variants} | \multicolumn{4}{c}{\textbf{Scientific}} | \multicolumn{4}{c}{\textbf{Office}} | \multicolumn{4}{c}{\textbf{Online Retail}} |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | R@10 | N@10 | R@50 | N@50 | R@10 | N@10 | R@50 | N@50 | R@10 | N@10 | R@50 | N@50 |
| (0) VQ-Rec | **0.1211** | **0.0643** | **0.2369** | **0.0897** | 0.1236 | 0.0814 | **0.1957** | 0.0972 | 0.1557 | 0.0730 | **0.3994** | 0.1263 |
| (1) $w/o$ Pre-training | 0.1104 | 0.0593 | 0.2238 | 0.0839 | 0.1108 | 0.0666 | 0.1804 | 0.0818 | 0.1535 | 0.0717 | 0.3953 | 0.1244 |
| (2) $w/o$ Semi-synthetic NS | 0.1194 | 0.0631 | 0.2358 | 0.0886 | 0.1227 | 0.0809 | 0.1951 | 0.0968 | 0.1529 | 0.0702 | 0.3938 | 0.1230 |
| (3) $w/o$ Fine-tuning | 0.0640 | 0.0361 | 0.0909 | 0.0421 | 0.0261 | 0.0150 | 0.0373 | 0.0174 | 0.0197 | 0.0095 | 0.0419 | 0.0142 |
| (4) Reuse PQ Index Set | 0.1168 | 0.0618 | 0.2267 | 0.0859 | 0.1182 | 0.0773 | 0.1869 | 0.0922 | 0.1521 | 0.0707 | 0.3917 | 0.1232 |
| (5) $w/o$ Code-Emb Alignment | 0.1183 | 0.0612 | 0.2355 | 0.0867 | **0.1242** | 0.0824 | 0.1956 | **0.0980** | 0.1515 | 0.0695 | 0.3924 | 0.1224 |
| (6) Random Code | 0.0905 | 0.0494 | 0.1769 | 0.0683 | 0.1134 | **0.0837** | 0.1698 | 0.0960 | **0.1589** | **0.0769** | 0.3933 | **0.1282** |

Table 3のアブレーションスタディでは、事前学習（1）やSemi-synthetic負例（2）、さらにはCode-Embedding Alignment（5）を除去すると性能が低下することが確認でき、各コンポーネントが精度向上に不可欠であることがわかります。

### データスパース性とコールドスタート問題への頑健性
![Figure 2: Performance comparison \wrt increasing training data on Office datasets.](./images/sparse_office.png)
![Figure 2: Performance comparison \wrt increasing training data on Online Retail datasets.](./images/sparse_or.png)
Figure 2は、下流タスクの学習データの割合を変化させた際の性能変化です。データが非常に少ない（スパースな）状況でも、VQ-Recはベースラインより一貫して高い性能を示しており、事前学習された表現がデータ不足を補っていることがわかります。

![Figure 4: Performance comparison \wrt cold-start items on Office datasets.](./images/cold_start_office.png)
![Figure 4: Performance comparison \wrt cold-start items on Online Retail datasets.](./images/cold_start_or.png)
Figure 4は、テストデータにおけるアイテムの出現頻度（コールドスタート）に対する性能比率を示しています。出現頻度が極端に低い（0~5回）コールドスタートアイテムに対して、VQ-RecはIDベースのSASRecと比べて圧倒的な性能改善率（特にOfficeで200%超）を記録しており、テキスト情報をコード化して利用する強みが最も現れていると考察されています。
