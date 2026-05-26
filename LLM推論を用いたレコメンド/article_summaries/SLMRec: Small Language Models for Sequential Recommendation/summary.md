# SLMRec: Small Language Models for Sequential Recommendation

## 背景
LLM（大規模言語モデル）の逐次推薦（Sequential Recommendation, SR）への応用は、従来のシーケンシャル推薦モデル（LSTMやTransformerベース）と比べて大幅に性能を向上させている。しかし、LLMベースの手法はモデルサイズが非常に大きく（例えば0.1Bから7B以上へと約70倍）、デプロイや推論にかかるコストが莫大であり、数十億のログを日々処理する実世界の推薦システムにおいて非効率で実用的ではないという課題がある。
本研究では、大規模な推薦タスクにおいて、「そもそもLLMの全ての層（深さ）が必要なのか」を調査するモチベーション実験（Motivational Experiments）を行った。その結果、LLMの中間層の多くは推薦タスクにおいて冗長であり、深い層を削ぎ落として浅いモデルにしても十分な性能を維持できることが明らかとなった（NLP領域で見られる現象と同様）。この知見に基づき、大規模なLLMから小規模な言語モデル（Small Language Models, SLM）へと知識蒸留を行うことで、高精度かつ高効率な推薦モデルを構築することを目指した。

## 手法
提案手法 **SLMRec**（Distilling Large Language Models into Small for Sequential Recommendation）は、層ごとの特徴量に対する知識蒸留（Knowledge Distillation）を活用したシンプルで効果的なアプローチである。
E-LLMRec（Embedding-based LLM Recommendation）をベースモデルとし、深いLLM（教師モデル）から浅いLLM（生徒モデル）へと特徴表現の知識を転移させる。

1. **特徴量の類似度（Feature Similarity）**
   教師モデルと生徒モデルの指定ブロックごとの特徴ベクトル間のコサイン類似度を最大化する損失 $\mathcal{D}_{cos}$ を導入。
   ※ここでの「指定ブロック」とは、層の深さが異なる教師モデル（例：24層）と生徒モデル（例：4層）間で知識を対応させるため、それぞれのモデルの全層を同じ数（$B$個）のまとまり（ブロック）に分割したものを指す（数式中の$k$は$k$番目のブロックを示す）。これにより、異なるサイズのモデル間でも段階的に特徴表現を引き継がせることができる。
   $$ \mathcal{D}_{\text{cos}}(\Theta_t, \Theta_s) = \frac{1}{B} \sum_{k=1}^{B} \frac{\mathbf{h}_t^{(k m)} \cdot \mathbf{h}_s^{(k n)}}{\| \mathbf{h}_t^{(k m)} \|_2 \cdot \| \mathbf{h}_s^{(k n)} \|_2} $$

2. **特徴量のL2正規化（Feature Norm Regularization）**
   教師モデルと生徒モデル間の特徴量のL2距離を最小化する損失 $\mathcal{D}_{norm}$ を導入。
   ※ここでの「特徴量」とは、各ブロックを通過した直後の中間出力（隠れ状態ベクトル）を指す。「1. 特徴量の類似度」がベクトルの「方向」を合わせるのに対し、こちらはベクトルの「大きさ（ノルム）」も含めて中間出力を教師モデルにそっくりそのまま近づける役割を持つ。
   $$ \mathcal{D}_{norm}(\Theta_t, \Theta_s) = \frac{1}{B} \sum_{k=1}^{B} \Vert \mathbf{h}_t^{(k m)} - \mathbf{h}_s^{(k n)} \Vert_2^2 $$

3. **多重教師あり学習（Multiple Supervision）**
   生徒モデルの各層ブロックにおいて、タスク固有の推薦知識を獲得させるため、それぞれの中間表現からの予測に対して交差エントロピー誤差 $\mathcal{L}_{ce}$ を課す $\mathcal{L}_{ms}$ を導入。
   ※最終層だけでなく、途中の各ブロックの中間出力に対しても直接「推薦予測」を行わせ、正解ラベルとの誤差を計算する。これにより、生徒モデルが単に教師の中間表現を真似るだけでなく、各段階で自力で推薦タスクを解くための意味のある特徴量を獲得するよう強制する役割がある（また、途中の層に直接誤差を流すことで勾配消失を防ぎ、学習を安定させる効果も持つ）。
   $$ \mathcal{L}_{ms}(\Theta_s,W_a) = \frac{1}{B-1} \sum_{k=1}^{B-1} \mathcal{L}_{ce}(y,\hat{p}_{t}^{(km)}) $$

4. **統合損失（Total Loss）**
   最終的な学習目的関数は以下の通りである。
   $$ \min_{\Theta_s,W_a} [\mathcal{L}_{ce}(\Theta_s) + \lambda_1 (1-\mathcal{D}_{cos}(\Theta_t, \Theta_s)) + \lambda_2 \mathcal{D}_{norm}(\Theta_t, \Theta_s) + \lambda_3  \mathcal{L}_{ms}(\Theta_s,W_a) ] $$

また、本手法は量子化やプルーニングなどの他の後処理技術とも直交しており、組み合わせることでさらなる効率化が可能である。

## 結果

### Figure 1
![Comparison between traditional sequential recommendation and LLM-based recommendation methods](./images/fig1.png)
**考察:** 従来のTSRモデルとLLMベースモデルの違いを示している。E-LLMRecはLLMを特徴抽出器として利用し、予測はTSRフレームワークに準拠する形式をとる。

### Figure 2
![Mot1 Plot: LLaMa Direct Infer Cloth HR@10](./images/llama_direct_infer_cloth_hr10.png)
![Mot1 Plot: LLaMa Direct Infer Cloth NDCG@10](./images/llama_direct_infer_cloth_ndcg10.png)
![Mot1 Plot: LLaMa Direct Infer Cloth MRR](./images/llama_direct_infer_cloth_mrr.png)
![Mot1 Plot: LLaMa Decoder Train Cloth HR@10](./images/llama_decoder_train_cloth_hr10.png)
![Mot1 Plot: LLaMa Decoder Train Cloth NDCG@10](./images/llama_decoder_train_cloth_ndcg10.png)
![Mot1 Plot: LLaMa Decoder Train Cloth MRR](./images/llama_decoder_train_cloth_mrr.png)
**考察:** モチベーション実験の結果。中間層をそのまま推論に用いる（Direct Infer）と精度は落ちるが、後ろの層を削って学習し直す（Decoder Train）と、8層程度の浅いモデルでも24層と同等以上の性能を達成できることを示しており、中間層に冗長性があることが確認できる。

### Figure 3
![Overview of SLMRec](./images/framework.png)
**考察:** 提案モデルSLMRecのアーキテクチャ概要。教師モデルと生徒モデルの層を複数のブロックに分け、それぞれの表現間で層単位の知識蒸留（Layer-wise knowledge distillation）と多重教師あり学習（Multiple supervision）を行っている。


### Table 1: Statistics of the Amazon datasets
| Dataset | $\left|\mathcal{U}\right|$ | $\left|\mathcal{V}\right|$ | $\left|\mathcal{E}\right|$ | Density |
|:---|:---|:---|:---|:---|
| Cloth | 1,219,678 | 376,858 | 11,285,464 | 0.002% |
| Movie | 297,529 | 60,175 | 3,410,019 | 0.019% |
| Music | 112,395 | 73,713 | 1,443,755 | 0.017% |
| Sport | 332,447 | 12,314 | 146,639 | 0.008% |
**考察:** 実験に使用されたAmazonデータセット（Cloth, Movie, Music, Sport）の統計情報。非常にスパースな（密度が低い）大規模産業データセットにおいて有効性を検証している。

### Table 2: Experimental results (%) on the Cloth and Movie dataset
| Model | Cloth HR@1 | Cloth HR@5 | Cloth NDCG@5 | Cloth MRR | Movie HR@1 | Movie HR@5 | Movie NDCG@5 | Movie MRR | Rank |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Caser | 9.66 | 15.18 | 12.66 | 13.03 | 4.27 | 14.96 | 9.57 | 10.36 | 13.50 |
| GRU4Rec | 13.79 | 15.46 | 14.64 | 15.15 | 10.56 | 19.47 | 15.11 | 15.46 | 9.25 |
| BERT4Rec | 13.60 | 14.66 | 14.14 | 14.59 | 9.68 | 14.91 | 12.40 | 12.74 | 11.63 |
| SASRec | 13.08 | 16.94 | 15.01 | 15.76 | 5.57 | 16.80 | 11.17 | 12.08 | 11.63 |
| HGN | 15.96 | 18.70 | 17.30 | 18.27 | 7.54 | 19.20 | 13.42 | 14.73 | 6.50 |
| LightSANs | 14.12 | 20.32 | 17.30 | 16.86 | 6.08 | 17.54 | 11.81 | 12.82 | 8.00 |
| S$^3$-Rec | 14.10 | 18.67 | 16.10 | 16.95 | 7.75 | 20.39 | 15.69 | 14.34 | 7.50 |
| DuoRec | 13.06 | 18.29 | 15.79 | 15.42 | 10.07 | 20.37 | 17.96 | 16.61 | 7.88 |
| MAERec | 13.29 | 18.35 | 15.68 | 16.13 | 8.89 | 20.24 | 16.03 | 15.28 | 8.38 |
| Open-P5 | 14.13 | 17.68 | 17.02 | - | 12.66 | 21.98 | 17.13 | - | 5.67 |
| E4SRec | 16.71 | 19.45 | 18.09 | 18.77 | 14.74 | 23.79 | 19.45 | 19.74 | 1.75 |
| E4SRec$_8$ | 15.30 | 18.54 | 16.91 | 17.60 | 13.32 | 22.49 | 17.99 | 18.46 | 4.00 |
| E4SRec$_4$ | 14.58 | 18.05 | 16.32 | 17.01 | 11.80 | 21.54 | 16.73 | 17.20 | 5.75 |
| SLMRec$_{4 \leftarrow 8}$ | **16.69** | **19.47** | **18.07** | **18.74** | **15.29** | **24.25** | **19.90** | **20.36** | **1.50** |
**考察:** ClothとMovieデータセットにおける性能評価。SLMRecはE4SRec(教師)とほぼ同等の性能（一部では凌駕）を達成しており、E4SRec$_4$（同じ4層のベースモデル）に対しては全ての指標で大きく上回っている。これにより、知識蒸留が浅いモデルの表現力を大きく底上げしていることがわかる。

### Table 3: Experimental results (%) on the Music and Sport dataset
| Model | Music HR@1 | Music HR@5 | Music NDCG@5 | Music MRR | Sport HR@1 | Sport HR@5 | Sport NDCG@5 | Sport MRR | Rank |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Caser | 0.71 | 3.28 | 1.96 | 2.29 | 1.05 | 3.75 | 2.39 | 2.84 | 13.50 |
| GRU4Rec | 1.89 | 3.22 | 2.57 | 3.08 | 5.26 | 7.75 | 6.52 | 7.08 | 10.13 |
| BERT4Rec | 2.10 | 3.16 | 2.64 | 3.11 | 4.81 | 6.70 | 5.79 | 6.26 | 10.63 |
| SASRec | 1.82 | 5.72 | 3.79 | 4.51 | 4.70 | 8.43 | 6.59 | 7.24 | 8.75 |
| HGN | 2.01 | 5.49 | 3.82 | 4.17 | 3.42 | 6.24 | 4.83 | 5.30 | 10.50 |
| LightSANs | 1.05 | 4.06 | 2.54 | 3.00 | 5.18 | 8.94 | 7.07 | 7.72 | 8.25 |
| S$^3$-Rec | 2.48 | 7.37 | 4.94 | 4.68 | 4.14 | 8.49 | 6.89 | 7.35 | 6.88 |
| DuoRec | 1.84 | 4.50 | 3.19 | 3.04 | 4.13 | 8.81 | 7.03 | 6.64 | 9.13 |
| MAERec | 2.19 | 6.35 | 4.67 | 3.96 | 4.01 | 8.35 | 6.65 | 6.98 | 8.63 |
| Open-P5 | 4.35 | 8.12 | 6.74 | - | 5.49 | 8.50 | 6.92 | - | 5.33 |
| E4SRec | 5.62 | 9.29 | 7.50 | 7.98 | 6.40 | 9.67 | 8.05 | 8.70 | 1.75 |
| E4SRec$_8$ | 5.46 | 8.86 | 7.21 | 7.74 | 5.48 | 8.63 | 7.06 | 7.76 | 3.63 |
| E4SRec$_4$ | 5.33 | 8.75 | 7.08 | 7.59 | 5.41 | 8.65 | 7.04 | 7.72 | 4.50 |
| SLMRec$_{4 \leftarrow 8}$ | **5.72** | **9.15** | **7.48** | **8.03** | **6.62** | **9.83** | **8.25** | **8.89** | **1.25** |
**考察:** MusicおよびSportデータセットでも同様に、SLMRecは全ての指標で従来のTSRモデルを凌駕し、同層数のE4SRec$_4$に対しても明確な性能向上を示している。平均ランクも最も高い（1.25）。

### Table 6: Experiment results (%) of ablation study on Cloth and Movie
| $\text{SLMRec}$ | Cloth HR@1 | Cloth HR@5 | Cloth NDCG@5 | Cloth MRR | Movie HR@1 | Movie HR@5 | Movie NDCG@5 | Movie MRR |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| +$\mathcal{D}_{cos}$ | 16.10 | 18.85 | 17.48 | 18.17 | 14.83 | 23.08 | 19.08 | 19.45 |
| +$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$ | 16.28 | 19.12 | 17.69 | 18.40 | 14.86 | 23.89 | 19.36 | 19.84 |
| +$\mathcal{D}_{cos}$,$\mathcal{L}_{ms}$ | 16.85 | 19.05 | 17.96 | 18.59 | 15.05 | 23.48 | 19.40 | 19.76 |
| +$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$,$\mathcal{L}_{ms}$ | **16.69** | **19.47** | **18.07** | **18.74** | **15.29** | **24.25** | **19.90** | **20.36** |
**考察:** アブレーションスタディの結果、3つの損失関数（コサイン類似度、L2正規化、多重教師あり学習）がそれぞれ性能向上に寄与しており、これらを全て組み合わせた場合が最も高い性能を発揮していることが確認できる。

### Table 7: Efficiency comparison of Open-P5, E4SRec, and our SLMRec
| Method | Tr time(h) | Inf time(h) | Tr params (B) | Inf params (B) |
|:---|:---|:---|:---|:---|
| Open-P5$_\mathrm{LLaMa}$ | 0.92 | 4942 | 0.023 | 7.237 |
| E4SRec | 3.95 | 0.415 | 0.023 | 6.631 |
| **SLMRec$_{4 \leftarrow 8}$** | 0.60 | 0.052 | 0.003 | 0.944 |
**考察:** 各LLMベースモデルの計算効率の比較。SLMRecはE4SRecに比べて推論パラメータが約13%（0.944B vs 6.631B）に圧縮され、訓練時間は約6.6倍（0.60h vs 3.95h）、推論時間は約8倍（0.052h vs 0.415h）に高速化されており、圧倒的な効率性を実現している。

### Table 8: Hyper-parameter (HP) settings of our method on each dataset
| HP | Cloth | Movie | Music | Sport |
|:---|:---|:---|:---|:---|
| adam_beta1 | 0.9 | 0.9 | 0.9 | 0.9 |
| adam_beta2 | 0.999 | 0.999 | 0.999 | 9.999 |
| adam_epsilon | 1e-8 | 1e-8 | 1e-8 | 1e-8 |
| learning_rate | 0.003 | 0.001 | 0.002 | 0.002 |
| logging_steps | 1 | 1 | 1 | 1 |
| lr_scheduler_type | cosine | cosine | cosine | cosine |
| max_grad_norm | 1.0 | 1.0 | 1.0 | 1.0 |
| max_steps | 1500 | -1 | 800 | 2000 |
| optimizer | adamw_torch | adamw_torch | adamw_torch | adamw_torch |
| save_strategy | steps | steps | steps | steps |
| save_steps | 50 | 100 | 100 | 100 |
| eval_steps | 50 | 100 | 100 | 100 |
| warmup_steps | 50 | 50 | 100 | 50 |
| $\lambda_1$ | 1.0 | 1.0 | 1.0 | 1.0 |
| $\lambda_2$ | 0.1 | 0.1 | 0.1 | 0.1 |
| $\lambda_3$ | 1.0 | 1.0 | 0.01 | 0.1 |
| $b$ | 4 | 4 | 4 | 4 |
**考察:** 実験で設定したハイパーパラメータの一覧。各種最適化や損失の重み（$\lambda_1, \lambda_2, \lambda_3$）がデータセットごとに明記されている。

### Table 9: Detailed efficiency comparison on each dataset
| Method | Cloth Tr time (h) | Cloth Inf time (h) | Movie Tr time (h) | Movie Inf time (h) | Music Tr time (h) | Music Inf time (h) | Sport Tr time (h) | Sport Inf time (h) |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Open-P5$_\mathrm{LLaMa}$ | 1.36 | 3554.43 | 0.36 | 3504 | 0.35 | 3692 | 1.60 | 9017 |
| E4SRec | 5.27 | 0.578 | 1.90 | 0.208 | 1.88 | 0.216 | 6.75 | 0.660 |
| **SLMRec$_{4 \leftarrow 8}$** | 0.97 | 0.070 | 0.15 | 0.030 | 0.30 | 0.030 | 0.98 | 0.078 |
**考察:** データセットごとのより詳細な訓練および推論時間の比較結果。いずれのデータセットにおいてもSLMRecはベースラインと比較して極めて低遅延・高効率で動作することが分かる。

### Table 10: Efficiency comparison of SASRec, MAERec and our SLMRec
| Method | Inf time(h) | Improv. (%) |
|:---|:---|:---|
| SASRec | 0.015 | 0.00 |
| MAERec | 0.061 | 11.96 |
| **SLMRec$_{4 \leftarrow 8}$** | 0.052 | 45.26 |
**考察:** 推論時間についてのTSRとの比較。SLMRecは推論時間が0.052hであり、MAERec（0.061h）よりも高速かつ性能改善幅（45.26%）が圧倒的である。

### Table 11: Experiment results (%) of ablation study on Music and Sport
| $\text{SLMRec}$ | Music HR@1 | Music HR@5 | Music NDCG@5 | Music MRR | Sport HR@1 | Sport HR@5 | Sport NDCG@5 | Sport MRR |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| +$\mathcal{D}_{cos}$ | 5.62 | 8.78 | 7.23 | 7.81 | 6.25 | 9.25 | 7.76 | 8.41 |
| +$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$ | **5.95** | **9.26** | **7.65** | **8.23** | 6.61 | 9.82 | 8.24 | 8.87 |
| +$\mathcal{D}_{cos}$,$\mathcal{L}_{ms}$ | 5.69 | 8.94 | 7.36 | 7.91 | 6.51 | 9.39 | 7.96 | 8.62 |
| +$\mathcal{D}_{cos}$,$\mathcal{D}_{norm}$,$\mathcal{L}_{ms}$ | 5.72 | 9.15 | 7.48 | 8.03 | **6.62** | **9.83** | **8.25** | **8.89** |
**考察:** MusicおよびSportデータセットにおけるアブレーション。Table 6と同様に各損失の複合的な有効性が裏付けられている。
