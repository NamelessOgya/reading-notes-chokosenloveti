# summary

## 背景
従来の逐次レコメンド（Sequential Recommendation）システムは、モデルがユーザーの行動履歴を時系列順に学習することで次のアイテムを予測しますが、その多くはアイテム固有のIDと一般的なテキスト特徴量に依存していました（例: GRU4Rec、SASRecなど）。しかし、これらのIDベースの手法には以下の課題がありました：
1. **コールドスタート問題:** 学習データに存在しない新規アイテム（コールドスタートアイテム）に対しては、紐づくIDの埋め込み表現が学習されていないため適切に推薦できない。
2. **ドメイン間の知識転移の困難さ:** アイテムIDはドメイン（データセット）間で共有されないため、あるドメインで学習したシーケンスパターンの知識を新しいドメインに転移させることができず、一から再学習する必要がある。

一方で、テキストなどの付加情報を活用する手法（UniSRec等）も提案されてきましたが、これらは事前学習済み言語モデル（PLM）を独立した特徴量抽出器として用い、推薦モデルと別々に学習されるため、文脈レベルの粗い特徴量しか抽出できず、レコメンド特有の詳細な属性レベルのユーザー選好を捉えきれないという課題がありました。本論文では、これらの課題を解決するため、アイテムをテキストとして自然言語表現で学習し、IDを一切必要としない（ID-freeな）推薦システムフレームワーク「**Recformer**」を提案しています。

## 手法
著者は、ユーザーのアイテム行動履歴の学習を「自然言語表現での学習問題」として定着させました。具体的には以下の手法（Recformer）を採用しています。

1. **アイテムの自然言語化:** 
   アイテムの属性（カテゴリ、ブランド、タイトルなど）のKeyとValueをペアとして平坦化し、1つの「アイテムの文章（Item Sentence）」を構築します。
   例: `{k1, v1, k2, v2...}`
   ユーザーの行動履歴は、時間的に最新のアイテムが重視されるよう逆順に並び替えられ、先頭に `[CLS]` トークンが付与された長文テキストとして扱われます。

2. **Longformerを採用したエンコーディング:**
   長文となる文章を効率よく処理するため、ローカルなウィンドウアテンションを持つ双方向Transformerである「Longformer」構造を利用しています。入力される各単語 $w$ の埋め込み $\mathbf{E}_w$ は、以下の4つの埋め込みの和をLayer Normalizationに通したものとして定義されます。
   - **Token embedding ($\mathbf{A}_w$):** 単語トークン表現。
   - **Token position embedding ($\mathbf{B}_w$):** 系列内におけるトークンの位置。
   - **Token type embedding ($\mathbf{C}_w$):** トークンが「属性Key」「属性Value」「[CLS]」のどれに該当するか。
   - **Item position embedding ($\mathbf{D}_w$):** 系列内のどのアイテムに属しているかを示す位置情報。

   $$
   \mathbf{E}_w = \mathrm{LayerNorm}(\mathbf{A}_w + \mathbf{B}_w + \mathbf{C}_w + \mathbf{D}_w)
   $$

   アイテム予測のスコア $r_{i, s}$ は、ユーザー系列の表現 $\mathbf{h}_s$（`[CLS]`トークンから取得）と、候補アイテムの表現 $\mathbf{h}_i$ のコサイン類似度で算出されます。
   $$
   r_{i, s} = \frac{\mathbf{h}_i^{\top} \mathbf{h}_s}{\Vert \mathbf{h}_i \Vert \cdot \Vert \mathbf{h}_s \Vert}
   $$

3. **事前学習 (Pre-training) と 2段階ファインチューニング (Two-Stage Finetuning):**
   - 言語理解と推薦の両方を考慮するため、事前学習では「Masked Language Modeling (MLM)」と「Item-item Contrastive (IIC) 学習」をマルチタスクで最適化します。
   $$
   \mathcal{L}_{\mathrm{PT}} = \mathcal{L}_{\mathrm{IIC}} + \lambda \cdot \mathcal{L}_{\mathrm{MLM}}
   $$
   - ファインチューニング時は、Batchが小さくIn-batch NegativeがFalse Negativeを生む問題を回避するため、全アイテムの特徴量行列 $\mathbf{I}$ を利用した2段階の処理を提案しています。Stage 1ではEpochごとに $\mathbf{I}$ を再計算・更新させ、Stage 2では $\mathbf{I}$ を固定してネットワークのパラメータのみを学習させることで正確な対照学習を実現します。

## 結果
論文中の各種評価図・表は以下の通りです。

### 1. 入力構成図・全体フレームワーク構成
![Figure 1: Input data comparison between item ID sequences for traditional sequential recommendation and key-value attribute pair sequences used in Recformer.](./images/key_value_seq.png)
![Figure 2: Model input construction. Flatten key-value attribute pairs into an item "sentence".](./images/inputs_flatten.png)
![Figure 3: The overall framework of Recformer.](./images/overall_framework.png)

上記の図は、Recformerが旧来のIDの羅列の代わりにKey-Value構造を用いてItem Sentenceを構築し、それらを順列化してLongformerに入力する枠組みを図示しています。

### 2. データセットと主要性能比較
Table 1は使用したAmazonレビューに基づく各データセットの統計量を示し、Table 2はそれらデータセット上でのID-Only、ID-Text、Text-Onlyベースラインとの性能比較を示しています。

| \textbf{Datasets} | \textbf{\#Users} | \textbf{\#Items} | \textbf{\#Inters.} | \textbf{Avg. n} | \textbf{Density} |
| :-- | --: | --: | --: | --: | --: |
| \textbf{Pre-training} | 3,613,906 | 1,022,274 | 33,588,165 | 9.29 | 9.1e-6 |
| -Training | 3,501,527 | 954,672 | 32,291,280 | 9.22 | 9.0e-6 |
| -Validation | 112,379 | 67,602 | 1,296,885 | 11.54 | 1.7e-4 |
| \textbf{Scientific} | 11,041 | 5,327 | 76,896 | 6.96 | 1.3e-3 |
| \textbf{Instruments} | 27,530 | 10,611 | 231,312 | 8.40 | 7.9e-4 |
| \textbf{Arts} | 56,210 | 22,855 | 492,492 | 8.76 | 3.8e-4 |
| \textbf{Office} | 101,501 | 27,932 | 798,914 | 7.87 | 2.8e-4 |
| \textbf{Games} | 11,036 | 15,402 | 100,255 | 9.08 | 5.9e-4 |
| \textbf{Pet} | 47,569 | 37,970 | 420,662 | 8.84 | 2.3e-4 |

| \textbf{Dataset} | \textbf{Metric} | \textbf{GRU4Rec} | \textbf{SASRec} | \textbf{BERT4Rec} | \textbf{RecGURU} | \textbf{FDSA} | \textbf{S$^3$-Rec} | \textbf{ZESRec} | \textbf{UniSRec} | \textbf{Recformer} | \textbf{Improv.} |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Scientific | NDCG@10 | 0.0826 | 0.0797 | 0.0790 | 0.0575 | 0.0716 | 0.0451 | 0.0843 | 0.0862 | \textbf{0.1027} | 19.14% |
| | Recall@10 | 0.1055 | 0.1305 | 0.1061 | 0.0781 | 0.0967 | 0.0804 | 0.1260 | 0.1255 | \textbf{0.1448} | 10.96% |
| | MRR | 0.0702 | 0.0696 | 0.0759 | 0.0566 | 0.0692 | 0.0392 | 0.0745 | 0.0786 | \textbf{0.0951} | 20.99% |
| Instruments | NDCG@10 | 0.0633 | 0.0634 | 0.0707 | 0.0468 | 0.0731 | 0.0797 | 0.0694 | 0.0785 | \textbf{0.0830} | 4.14% |
| | Recall@10 | 0.0969 | 0.0995 | 0.0972 | 0.0617 | 0.1006 | 0.1110 | 0.1078 | \textbf{0.1119} | 0.1052 | - |
| | MRR | 0.0707 | 0.0577 | 0.0677 | 0.0460 | 0.0748 | 0.0755 | 0.0633 | 0.0740 | \textbf{0.0807} | 6.89% |
| Arts | NDCG@10 | 0.1075 | 0.0848 | 0.0942 | 0.0525 | 0.0994 | 0.1026 | 0.0970 | 0.0894 | \textbf{0.1252} | 16.47% |
| | Recall@10 | 0.1317 | 0.1342 | 0.1236 | 0.0742 | 0.1209 | 0.1399 | 0.1349 | 0.1333 | \textbf{0.1614} | 15.37% |
| | MRR | 0.1041 | 0.0742 | 0.0899 | 0.0488 | 0.0941 | 0.1057 | 0.0870 | 0.0798 | \textbf{0.1189} | 12.49% |
| Office | NDCG@10 | 0.0761 | 0.0832 | 0.0972 | 0.0500 | 0.0922 | 0.0911 | 0.0865 | 0.0919 | \textbf{0.1141} | 17.39% |
| | Recall@10 | 0.1053 | 0.1196 | 0.1205 | 0.0647 | 0.1285 | 0.1186 | 0.1199 | 0.1262 | \textbf{0.1403} | 9.18% |
| | MRR | 0.0731 | 0.0751 | 0.0932 | 0.0483 | 0.0972 | 0.0957 | 0.0797 | 0.0848 | \textbf{0.1089} | 12.04% |
| Games | NDCG@10 | 0.0586 | 0.0547 | 0.0628 | 0.0386 | 0.0600 | 0.0532 | 0.0530 | 0.0580 | \textbf{0.0684} | 8.92% |
| | Recall@10 | 0.0988 | 0.0953 | 0.1029 | 0.0479 | 0.0931 | 0.0879 | 0.0844 | 0.0923 | \textbf{0.1039} | 0.97% |
| | MRR | 0.0539 | 0.0505 | 0.0585 | 0.0396 | 0.0546 | 0.0500 | 0.0505 | 0.0552 | \textbf{0.0650} | 11.11% |
| Pet | NDCG@10 | 0.0648 | 0.0569 | 0.0602 | 0.0366 | 0.0673 | 0.0742 | 0.0754 | 0.0702 | \textbf{0.0972} | 28.91% |
| | Recall@10 | 0.0781 | 0.0881 | 0.0765 | 0.0415 | 0.0949 | 0.1039 | 0.1018 | 0.0933 | \textbf{0.1162} | 11.84% |
| | MRR | 0.0632 | 0.0507 | 0.0585 | 0.0371 | 0.0650 | 0.0710 | 0.0706 | 0.0650 | \textbf{0.0940} | 32.39% |

**考察:**
全体を通して、Recformerはテキストのみを利用する（Text-Onlyベースの）手法でありながら、InstrumentsのRecall@10を除くすべてのデータセットにおいて最良の精度を記録しています（図表上ではNDCG@10で最大28.91%改善）。これは、提案された2段階ファインチューニングを通じてダウンストリームのタスクに効果的に適応し、事前学習から転移された言語理解能力が継続的に利益をもたらすことを示しています。

### 3. コールドスタート問題とゼロショット推薦
Table 3は学習時に出現したアイテム（In-Set）とコールドスタートアイテムでの性能比較を示し、Figure 4およびFigure 5はゼロショット・Few-shotセッティングでの性能を示しています。

| \textbf{Dataset} | \textbf{Metric} | \textbf{SASRec (In-Set)} | \textbf{SASRec (Cold)} | \textbf{UniSRec (In-Set)} | \textbf{UniSRec (Cold)} | \textbf{Recformer (In-Set)} | \textbf{Recformer (Cold)} |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Scientific | N@10 | 0.0775 | 0.0213 | 0.0864 | 0.0441 | 0.1042 | 0.0520 |
| | R@10 | 0.1206 | 0.0384 | 0.1245 | 0.0721 | 0.1417 | 0.0897 |
| Instruments | N@10 | 0.0669 | 0.0142 | 0.0715 | 0.0208 | 0.0916 | 0.0315 |
| | R@10 | 0.1063 | 0.0309 | 0.1094 | 0.0319 | 0.1130 | 0.0468 |
| Arts | N@10 | 0.1039 | 0.0071 | 0.1174 | 0.0395 | 0.1568 | 0.0406 |
| | R@10 | 0.1645 | 0.0129 | 0.1736 | 0.0666 | 0.1866 | 0.0689 |
| Pet | N@10 | 0.0597 | 0.0013 | 0.0771 | 0.0101 | 0.0994 | 0.0225 |
| | R@10 | 0.0934 | 0.0019 | 0.1115 | 0.0175 | 0.1192 | 0.0400 |

![Figure 4: Performance (NDCG@10) of three Text-Only methods under the zero-shot setting.](./images/zero_shot.png)
![Figure 5: Performance (NDCG@10) of SASRec, UniSRec, Recformer over different sizes of training data.](./images/few_shot.png)

**考察:**
Table 3を見ると、IDベースの手法（SASRec）は学習に利用できなかったコールドスタートアイテムに対して大幅に精度を落とす一方で、UniSRecやRecformerのようなテキストベースの手法はそれよりも高い値を維持しています。さらにRecformerはUniSRecと比較しても、テキストの言語表現を推薦と結びつけて柔軟に捉えるため、より高い汎化性能を発揮していると筆者は述べています。これはゼロショット（Figure 4）やFew-Shot（Figure 5）といった「データが少ない状況」において、Recformerが既存のID-Only手法を完全に凌駕していることからも裏付けられています。

### 4. アブレーションスタディと学習ステップの検証
Table 4では提案フレームワークにおける各種要素のアブレーションスタディを行い、Figure 6では事前学習のステップ数による影響を確認しています。

| \textbf{Variants} | \textbf{Scientific (NDCG@10)} | \textbf{Scientific (Recall@10)} | \textbf{Scientific (MRR)} | \textbf{Instruments (NDCG@10)} | \textbf{Instruments (Recall@10)} | \textbf{Instruments (MRR)} |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| (0) Recformer | \textbf{0.1027} | \textbf{0.1448} | \textbf{0.0951} | \textbf{0.0830} | \textbf{0.1052} | \textbf{0.0807} |
| (1) w/o two-stage finetuning | 0.1023 | 0.1442 | 0.0948 | 0.0728 | 0.1005 | 0.0685 |
| (1) + (2) freezing word emb. & item emb. | 0.1026 | 0.1399 | 0.0942 | 0.0728 | 0.1015 | 0.0682 |
| (1) + (3) trainable word emb. & item emb. | 0.0970 | 0.1367 | 0.0873 | 0.0802 | 0.1015 | 0.0759 |
| (1) + (4) trainable item emb. & freezing word emb. | 0.0965 | 0.1383 | 0.0856 | 0.0801 | 0.1014 | 0.0760 |
| (5) w/o pre-training | 0.0722 | 0.1114 | 0.0650 | 0.0598 | 0.0732 | 0.0584 |
| (6) w/o item position emb. & token type emb. | 0.1018 | 0.1427 | 0.0945 | 0.0518 | 0.0670 | 0.0501 |

![Figure 6: Recformer zero-shot recommendation performance over different pre-training steps.](./images/training_steps.png)

**考察:**
アブレーションスタディ（Table 4）より、提案された「2段階ファインチューニング（two-stage finetuning）」を外す（Variants 1）と精度が明確に下落することが分かります。事前学習を行わないケース（Variants 5）で最も性能が低下しており、事前学習による言語基盤と2段階ファインチューニングの併用が有効に機能していることが裏付けられています。
また、Figure 6に示すように、言語理解からアイテムテキスト理解へのドメイン適応は極めて迅速であり、事前学習はおおよそ 4,000 Step 周辺でピークに達し、それ以上学習を続けると過学習によりダウンストリームタスクへの知識転移性が低下することも観察されています。
