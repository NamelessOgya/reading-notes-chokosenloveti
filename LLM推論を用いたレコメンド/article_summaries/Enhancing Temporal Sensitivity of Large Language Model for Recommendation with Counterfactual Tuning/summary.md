# Enhancing Temporal Sensitivity of Large Language Model for Recommendation with Counterfactual Tuning

## 背景
逐次推薦（Sequential Recommendation）は、ユーザーの過去の行動履歴から時系列に沿って次の興味を予測するタスクである。近年、この分野において大規模言語モデル（LLM）の豊富な事前学習知識と推論能力を活用する手法が多数提案されている。しかし、既存のLLMベースのモデルはユーザーの行動系列に含まれる「時間的情報（Temporal Information）」を十分に活用できておらず、ユーザーの動的な興味の変化を捉えきれないという課題があった。

この原因として、LLMの基盤であるTransformerの自己注意機構（Self-Attention）自体が順序の概念を持たず、自然言語向けに設計された「位置埋め込み（Position Embedding）」に過度に依存していることが挙げられる。自然言語における位置埋め込みはトークン単位で適用されるため、推薦における「アイテム単位」の時間的まとまりを表現するのには不適である。また、推薦タスクのプロンプトには膨大な指示や文脈が含まれるため、元々希薄な時間的シグナルが他の情報に埋もれてしまう（希釈される）という問題も指摘されている。

## 手法
本論文では、LLMベースの推薦モデルの時間的感度（Temporal Sensitivity）を強化するために、因果推論（Causal Inference）の概念に基づいた **CETRec**（Counterfactual Enhanced Temporal Framework for LLM-Based Recommendation） を提案している。

手法の核となるのは、以下の3つのアプローチである。

### 1. 時間的埋め込み（Temporal Embedding）
アイテム単位の時間的な順序関係を明示的にエンコードするため、各アイテムを構成するすべてのトークンに対して、同一の「時間的埋め込み（ $p_{k}$ ）」を追加する。これにより、アイテムという意味的な境界を保持しつつ、履歴における相対的・絶対的な位置情報をLLMに与える。
トークン $t$ の入力埋め込み $I_{t}$ は以下の数式で定義される：

$$ I_{t} = x_{t} + p_{t} + p_{k} $$

（ $x_{t}$ はトークン埋め込み、 $p_{t}$ は元のトークンレベルの位置埋め込み、 $p_{k}$ はアイテム $k$ に付与される時間的埋め込みを示す。）

### 2. 因果分析に基づく反事実的推論（Counterfactual Inference）
時間的順序が推薦結果に与える因果効果を正確に測定するため、時系列情報 $T$ を独立した因果要因として因果グラフを構築する（Figure: causal-anal 参照）。その上で、推薦されるアイテム群（事実）はそのままに、時間的順序情報のみをすべて「最初のアイテムの埋め込み（ $p_{0}$ ）」に置き換えた「時間情報が消去された反事実世界（Counterfactual World）」を構築する。

- **目的（直感的背景）**: アイテムの「コンテンツ（中身）の効果」と「時間的順序の効果」を分離し、時間的順序が推薦結果に与える純粋な因果効果（ $T \rightarrow H \rightarrow Y$ ）を抽出して学習させる。
- **事実世界（Factual）**: 履歴の各アイテムに最新のものから順に異なる時間的埋め込み（例: 最も古いアイテムに $p_2$ 、次に $p_1$ 、最新に $p_0$ ）を付与し、LLMに時系列の順序を認識させる。
- **反事実世界（Counterfactual）**: 同じ履歴を用いつつ、すべてのアイテムの時間的埋め込みを最も古いアイテムと同じ $p_0$ に一括置換することで、時間的順序情報（絶対・相対時間）を完全に消去（Erase）した仮想的な世界を作る。
- **因果効果の算出**: Twin Networkの概念に基づき、事実世界での予測確率と反事実世界での予測確率の差分（Divergence）として、時間情報が与える純粋な因果効果を定量化する。


### 3. 反事実チューニング（Counterfactual Tuning Task）
モデルが時間的情報に敏感に反応するように、事実世界（時間的順序あり）と反事実世界（時間的順序なし）の出力確率の差分（発散）を最大化する反事実チューニング損失 $L_{CT}$ を導入する。  
各トークンの出力時の確率分布の差を最大化する。  

$$ L_{CT} = \sum_{(x,y) \in \mathcal{D}} \sum_{k=1}^{|y|} \ell \left( f_{\Theta+\Phi}(x_{t}, y_{<k}) - f_{\Theta+\Phi}(x_{0}, y_{<k}); y_{k} \right) $$

ここで、数式内の各記号は以下を表す：
- $L_{CT}$ : 反事実チューニング損失（Counterfactual Tuning Loss）
- $\mathcal{D}$ : 学習データセット
- $(x, y)$ : インストラクション入力 $x$ と、正解の生成ターゲット（アイテムのタイトル） $y$ のペア
- $k$ : ターゲット $y$ 内の $k$ 番目のトークン位置
- $|y|$ : ターゲット $y$ の総トークン数
- $\ell$ : 損失関数（予測確率と正解トークン $y_k$ の乖離を評価する関数）
- $f_{\Theta+\Phi}(\cdot)$ : パラメータ $\Theta$ （LLMの基盤モデル）と $\Phi$ （LoRAパラメータ）を持つモデルが出力する、入力に対する次のトークンの予測確率分布
- $x_t$ : 時間的順序情報（時間的埋め込み $p_k$ ）が含まれる事実世界の入力シーケンス
- $x_0$ : 時間的順序情報が消去（ $p_0$ に一括置換）された反事実世界の入力シーケンス
- $y_{<k}$ : すでに生成された $k$ 番目未満のトークン列（自己回帰予測の文脈情報）
- $y_k$ : 生成すべき $k$ 番目の正解ターゲットトークン


これに加えて、通常の推薦能力を維持するための時間認識損失 $L_{TA}$ を同時に最適化する。

$$ L_{TA} = \sum_{(x,y)\in D} \sum_{k=1}^{|y|} \ell \left( f_{\Theta+\Phi}(x, y_{<k});\ y_{k} \right) $$

最終的な目的関数 $L$ は両者の重み付き和として定義される。

$$ L = L_{TA} + \lambda L_{CT} $$

## 結果

本論文ではMovieLens、Steam、LastFMの3つの実データセットを用いてCETRecの評価を行った。

### 図表による評価

![Figure 1: Illustration of absolute vs. relative order effects](./images/temporder.png)
**考察:** ユーザーのインタラクション履歴には、絶対的な時間（いつ起きたか）と相対的な時間（どのような順番で起きたか）の両方の順序情報が含まれており、これらを正確にモデリングすることが推薦精度に直結することを示している。

![Figure: The framework of CETRec](./images/CETRecframework.png)
**考察:** CETRecの全体アーキテクチャ。ユーザーの対話系列をInstruction Tuningのフォーマットに変換し、時間的に順序付けられたシーケンスと、順序情報が消去された（反事実の）シーケンスを並行して入力し、両者の差分から $L_{CT}$ を算出する様子が描かれている。

![Figure: Causal graph and twin network](./images/causal-anal.png)
**考察:** 逐次推薦の因果グラフ (a) と、反事実推論のためのTwin Network (b)。時間的順序 $T$ が履歴 $H$ を通じて推薦結果 $Y$ に与える影響を切り分けて評価・学習する理論的基盤となっている。

![Figure: Performance change rate on reversed sequences](./images/rev-change-rate.png)
**考察:** テストデータのシーケンス順序を反転させた場合の性能変化率（MovieLens）。CETRecはベースラインと比較して順序の反転に対する感度が非常に高く、時間的順序情報を強く捉えられている（順序に依存した予測ができている）ことがわかる。

![Figure: Case study on Steam Dataset](./images/case.png)
**考察:** Steamデータセットを用いたケーススタディ。ユーザーの最近の興味の変化（例: 新しいジャンルのゲームを連続してプレイしている等）に対して、CETRecが正確に時間情報を捉え、適切な推薦を行えていることを定性的に示している。

### テーブルデータによる評価

#### Table 1: Statistical details of training datasets.
| Dataset | MovieLens | Steam | LastFM |
| :--- | :--- | :--- | :--- |
| #Sequences | 192,483 | 151,056 | 46,897 |
| #Items | 3,952 | 3,581 | 4,606 |
| #Interactions | 999,611 | 239,796 | 73,510 |

#### Table 2: Performance of baselines and CETRec on MovieLens, Steam, and LastFM datasets.
| | MovieLens HR@5 | MovieLens NDCG@5 | MovieLens HR@10 | MovieLens NDCG@10 | Steam HR@5 | Steam NDCG@5 | Steam HR@10 | Steam NDCG@10 | LastFM HR@5 | LastFM NDCG@5 | LastFM HR@10 | LastFM NDCG@10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Caser | 0.0667 | 0.0399 | 0.1217 | 0.0573 | 0.0307 | 0.0200 | 0.0488 | 0.0258 | 0.0222 | 0.0145 | 0.0324 | 0.0177 |
| GRU4Rec | 0.0475 | 0.0283 | 0.0900 | 0.0417 | 0.0301 | 0.0198 | 0.0479 | 0.0255 | 0.0130 | 0.0079 | 0.0204 | 0.0103 |
| SASRec | 0.0542 | 0.0322 | 0.0917 | 0.0441 | 0.0269 | 0.0171 | 0.0450 | 0.0229 | 0.0194 | 0.0097 | 0.0352 | 0.0146 |
| P5 | 0.0538 | 0.0334 | 0.0911 | 0.0452 | 0.0688 | 0.0468 | 0.1049 | 0.0583 | 0.0173 | 0.0138 | 0.0273 | 0.0171 |
| BIGRec | 0.0985 | 0.0614 | 0.1093 | 0.0650 | 0.0778 | 0.0530 | 0.0979 | 0.0596 | 0.0264 | 0.0192 | 0.0356 | 0.0221 |
| E4SRec | 0.1050 | 0.0660 | 0.1170 | 0.0700 | 0.0810 | 0.0555 | 0.0982 | 0.0615 | 0.0500 | 0.0325 | 0.0600 | 0.0355 |
| LLaRA | 0.1120 | 0.0710 | 0.1250 | 0.0750 | 0.0850 | 0.0580 | 0.0985 | 0.0635 | 0.0745 | 0.0450 | 0.0880 | 0.0490 |
| CFT | 0.1043 | 0.0623 | 0.1241 | 0.0691 | 0.0879 | 0.0606 | 0.1013 | 0.0650 | 0.0711 | 0.0424 | 0.0838 | 0.0467 |
| CETRec (SinPE) | 0.1101 | 0.0693 | 0.1209 | 0.0728 | 0.0670 | 0.0436 | 0.0779 | 0.0471 | 0.0780 | 0.0520 | 0.0910 | 0.0550 |
| CETRec (RoPE) | **0.1283** | **0.0779** | **0.1365** | **0.0806** | **0.0921** | **0.0641** | **0.1072** | **0.0690** | **0.0866** | **0.0591** | **0.1030** | **0.0646** |

**考察:** 提案手法である CETRec (RoPE) は、既存のベースライン手法やLLMベース手法（BIGRec, E4SRec, LLaRA等）と比較して、すべてのデータセットおよび評価指標（HR, NDCG）において一貫して最高の精度を達成している。また、位置埋め込みとしてSinPEを用いた場合よりも、RoPEを用いた場合の方がより高い推薦性能を示した。

#### Table 3: Ablation results with different positional embedding methods and training variants.
| Positional Embedding | Method | MovieLens HR@5 | MovieLens NDCG@5 | MovieLens HR@10 | MovieLens NDCG@10 | Steam HR@5 | Steam NDCG@5 | Steam HR@10 | Steam NDCG@10 | LastFM HR@5 | LastFM NDCG@5 | LastFM HR@10 | LastFM NDCG@10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SinPE | CETRec | 0.1101 | 0.0693 | 0.1209 | 0.0728 | 0.0670 | 0.0436 | 0.0779 | 0.0471 | 0.0780 | 0.0520 | 0.0910 | 0.0550 |
| SinPE | *w.o.* CT | 0.1035 | 0.0634 | 0.1167 | 0.0676 | 0.0620 | 0.0407 | 0.0720 | 0.0440 | 0.0721 | 0.0482 | 0.0865 | 0.0514 |
| RoPE | CETRec | **0.1283** | **0.0779** | **0.1365** | **0.0806** | **0.0921** | **0.0641** | **0.1072** | **0.0690** | **0.0866** | **0.0591** | **0.1030** | **0.0646** |
| RoPE | *w.o.* CT | 0.1192 | 0.0745 | 0.1300 | 0.0781 | 0.0856 | 0.0613 | 0.1021 | 0.0669 | 0.0805 | 0.0565 | 0.0980 | 0.0626 |
| None | *w.o.* Both | 0.0985 | 0.0614 | 0.1093 | 0.0650 | 0.0778 | 0.0530 | 0.0979 | 0.0596 | 0.0264 | 0.0192 | 0.0356 | 0.0221 |

**考察:** 反事実チューニング（CT）を除外した *w.o.* CT モデルや、時間的埋め込み自体を除外した *w.o.* Both モデルとのAblation Study。反事実チューニングを取り除くといずれの埋め込み表現においても精度が低下することから、因果推論に基づいた $L_{CT}$ の導入がモデルの時間的感受性の強化および推薦精度の向上に直接寄与していることが確認された。

#### Table 4: A tuning template for the Game dataset. <His_Seq> and <Target_Item> denote the user's historical interaction sequence and the ground-truth next item, respectively.
| Instruction Input | |
| :--- | :--- |
| **Task Instruction:** | Given a list of video games the user has played before, please recommend a new video game that the user likes to the user. |
| **Task Input:** | The user has played the following video games before: `<His_Seq>` |
| **Instruction Output** | |
| **Output:** | `<Target_Item>` |

**考察:** プロンプトチューニングに用いられた入力フォーマット例。 `<His_Seq>` には時間的埋め込みが付与されたアイテム列が含まれており、これをもとに次の予測アイテム `<Target_Item>` を生成させている。
