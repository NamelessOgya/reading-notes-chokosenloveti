# SlateQ: A Pragmatic Approach to Competitive Multi-Pack Offerings in Recommendation Systems
（原題: Reinforcement Learning for Slate-based Recommender Systems: A Tractable Decomposition and Practical Methodology / IJCAI-19: SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets）

**arXiv:** [1905.12767](https://arxiv.org/abs/1905.12767)  
**カンファレンス:** IJCAI 2019 (Proceedings of the 28th International Joint Conference on Artificial Intelligence)  
**著者:** Eugene Ie, Vihan Jain, Jing Wang, Sanmit Narvekar, Ritesh Agarwal, Rui Wu, Heng-Tze Cheng, Morganeb Touati, Randy Zou, Tushar Chandra, Craig Boutilier  
（Google Research / YouTube）  
**発表:** 2019年5月（IJCAI 2019採択）  
**対象タスク:** スレート推薦（Slate-based Recommender Systems / List-wise Recommendation）、強化学習（RL）、長期ユーザーエンゲージメント（LTV）最大化、大規模動画推薦（YouTube）

---

## 背景

現実の大規模推薦システム（YouTube、Netflix、ECサイトなど）において、ユーザーに提示されるのは単一のアイテムではなく、複数（$k$ 個）のアイテムを束ねた **「スレート（Slate: 推薦リストや推薦グリッド）」** である。

従来の多くの推薦システムは、推薦したアイテムがその場でクリックされるか、あるいは即座に視聴されるかという **「近視眼的（Myopic）な即時エンゲージメント（CTR、直後の滞在時間など）」** のみを予測・最適化していた。しかし、近視眼的な最適化は以下のような重大な弊害をもたらす：
- **クリックベイト（釣りコンテンツ）の蔓延**:
  - 短期的にはクリックされるが、ユーザーの長期的な満足度を損ない、プラットフォームからの離脱を招く。
- **長期的価値（LTV: Long-Term Value）の無視**:
  - ユーザーの興味関心の推移や多様性の充足、将来の継続訪問といったセッションを超えた累積エンゲージメントを計画・誘導できない。

長期的価値を最大化するためにはマルコフ決定プロセス（MDP）に基づく **強化学習（Reinforcement Learning: RL）** が自然なアプローチとなる。しかし、スレート推薦に標準的な深層強化学習（DQN等）を適用しようとすると、以下の致命的な **「組み合わせ爆発（Combinatorial Action Space）」** の壁に直面する：
- 全アイテム集合を $\mathcal{I}$、スレートサイズを $k$ としたとき、可能なスレートの総数は $\binom{|\mathcal{I}|}{k} \cdot k!$ 通りに達する。
- YouTube のように候補が数十万〜数億件、スレートサイズが $k=10$〜$20$ の場合、行動空間のサイズは天文学的となり、**「十分な探索（Exploration）」** も **「Q値の汎化（Generalization）」** も不可能になる。さらに、Q値が最大となるスレートを選択する **「最適化（Argmax Optimization）」** はNP困難となり、ミリ秒単位の応答が求められるオンライン推薦では到底実行できない。

これに対し著者らは、現実的なユーザー選択行動の仮定（スレート内の1つのアイテムを消費すること）に基づき、**スレート全体のQ値を、構成要素である個々のアイテムの長期価値（LTV）の期待値へと完全に分解（Decomposition）する理論フレームワーク「SlateQ」** を提案した。これにより組み合わせ爆発を完全に回避し、YouTube の本番環境（数十億ユーザー規模）における強化学習の大規模実稼働を世界で初めて実証した。

---

## 手法

![System Overview of YouTube Recommendation](./images/system_overview.png)
*(YouTube 推薦システムにおける候補生成（Candidate Generator）とランカー（Ranker）のパイプライン概要)*

---

### 1. 2つの核心仮定（Core Assumptions）

スレート $A = (a_1, \dots, a_k)$ に対する Q 関数 $Q(s, A)$ を分解するため、著者らは現実の推薦環境に即した2つの合理的な仮定を置いた：

1. **Single Choice（SC仮定: 単一選択）**:
   - ユーザーは提示されたスレート $A$ の中から、高々 1 つのアイテム $i \in A$ を選択・消費する（何も選択しないヌルアイテム $\bot$ を含む）。
   - すなわち、選択される部分集合 $B \subseteq A$ について、$|B| = 1$ の場合のみ選択確率 $P(B|s, A) > 0$ を持つ。
2. **Reward/Transition Dependence on Selection（RTDS仮定: 選択依存の報酬と状態遷移）**:
   - 得られる即時報酬 $R(s, A)$、および次状態への遷移確率 $P(s'|s, A)$ は、スレート内の非選択アイテムには依存せず、**ユーザーが実際に選択・消費したアイテム $i \in A$ のみに依存する**：
     $$ R(s, A, i) = R(s, A', i) = R(s, i) $$
     $$ P(s'|s, A, i) = P(s'|s, A', i) = P(s'|s, i) $$

---

### 2. SlateQ 分解定理（Slate Decomposition Theorem）

データ生成ポリシー $\pi$ において、状態 $s$ でアイテム $i$ がクリック・消費されたという条件の下での長期価値を表す **アイテム単位の補助関数（Item-wise Auxiliary LTV Function） $\bar{Q}^\pi(s, i)$** を定義する：

$$ \bar{Q}^\pi(s, i) = R(s, i) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, i) V^\pi(s') $$

このとき、SC仮定とRTDS仮定の下で、以下の完全分解定理が成り立つ：

> **Proposition 1 (SlateQ 分解定理):**
> $$ Q^\pi(s, A) = \sum_{i \in A} P(i|s, A) \bar{Q}^\pi(s, i) $$

#### 定理の導出
$$ Q^\pi(s, A) = R(s, A) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, A) V^\pi(s') $$
SC仮定とRTDS仮定より、即時報酬と遷移確率は選択確率で重み付けされたアイテム単体の期待値となる：
$$ R(s, A) = \sum_{i \in A} P(i|s, A) R(s, i), \quad P(s'|s, A) = \sum_{i \in A} P(i|s, A) P(s'|s, i) $$
これを代入すると：
$$ Q^\pi(s, A) = \sum_{i \in A} P(i|s, A) \left[ R(s, i) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, i) V^\pi(s') \right] = \sum_{i \in A} P(i|s, A) \bar{Q}^\pi(s, i) $$

この定理により、**組み合わせ爆発するスレート空間 $(A)$ を学習・探索する必要が完全に消滅し、単一アイテムの条件付き長期価値 $\bar{Q}(s, i)$ とユーザー選択モデル $P(i|s, A)$ のみを学習すればよい** ことが保証される。

---

### 3. TD学習アルゴリズム（SARSA / Q-learning 更新則）

状態 $s$ でスレート $A$ を提示し、ユーザーがアイテム $i$ を消費して即時報酬 $r$ を獲得、次状態 $s'$ へ遷移して次スレート $A'$ が提示されたとき、$\bar{Q}^\pi$ は以下の Temporal-Difference（TD）則で更新される：

$$ \bar{Q}^\pi(s, i) \leftarrow (1 - \alpha) \bar{Q}^\pi(s, i) + \alpha \left( r + \gamma \sum_{j \in A'} P(j|s', A') \bar{Q}^\pi(s', j) \right) $$

Q-learning（オフポリシー最適化）の場合は、次スレート $A'$ を現在のQ値に関する最適スレート $A^* = \arg\max_{A'} Q(s', A')$ に置き換えて更新する。

---

### 4. スレート最適化（Slate Optimization at Serving Time）

推論時（サービング時）には、与えられた候補群の中から Q 値を最大化するスレート $A^* = \arg\max_A \sum_{i \in A} P(i|s, A) \bar{Q}(s, i)$ をミリ秒単位で選定する必要がある。

ユーザー選択モデルとして標準的な **多項ロジットモデル（Multinomial Logit: MNL）** を採用する：
$$ P(i|s, A) = \frac{e^{v(s, i)}}{1 + \sum_{j \in A} e^{v(s, j)}} $$
ここで $v(s, i)$ はアイテム $i$ の即時クリック魅力度（pCTRスコア）。このときスレート最適化は **分数計画（Fractional Programming）** に帰着され、以下の手法で解くことができる：
- **Optimal Serving (OS / 線形計画法 LP)**:
  - 変数変換により $k$ 個のアイテム選択問題を厳密な線形計画問題に変換して解く。
- **Greedy Serving (GS / 貪欲法)**:
  - 限界利得（Marginal Gain）が最大となるアイテムを1つずつ $k$ 個選定する。
- **Top-$k$ Serving (TS)**:
  - 各アイテムのスコア $e^{v(s, i)} \bar{Q}(s, i)$ の上位 $k$ 件を単純抽出する。計算量は極小で、本番の超低レイテンシ環境に適する。

---

### 5. マルチタスク深層ニューラルネットワーク構成

![Multi-task DNN Architecture](./images/network.png)
*(YouTube 本番ランカーのマルチタスク DNN 構成：Main Network と Label Network の2台体制)*

YouTube の本番環境では、既存の近視眼的ランカーと同じ入力特徴量（ユーザーの過去の行動履歴、静的属性、アイテム特徴）を持つ **マルチタスク Deep Neural Network** を採用した：
- **共有中間層**: 4層の Fully-Connected 層（ユニット数: 2048, 1024, 512, 256、ReLU活性化）。
- **出力ヘッド**:
  - 即時魅力度ヘッド $v(s, i)$（pCTR予測）
  - **長期価値ヘッド $\bar{Q}(s, i)$（クリック時期待 LTV 予測）**
  - その他（動画完了率、エンゲージメント予測など）

#### 左右のネットワークの違い（Main Network vs. Label Network）

図に描かれている左右のネットワークは、同一のネットワーク構造を持ちながら、**「現在学習中のモデル」と「正解ラベルを作るために重みを固定したコピーモデル（Target Network）」** という異なる役割を担っている：

| 項目 | 左側：Main (trainable) Network | 右側：Label Network (Target Network) |
| :--- | :--- | :--- |
| **役割** | **いま学習（パラメータ更新）している現在のメインモデル** | **正解ラベルを計算するためだけに重みを一時固定したコピーモデル** |
| **重み更新** | 毎ステップ、勾配降下法（SGD）によって **常に更新され続ける** | 一定間隔（$M$ ステップ）の間、**重み $\theta_{\mathrm{label}}$ をカチッと固定（フリーズ）** |
| **入力データ** | **現在の状態 $s$** と **提示されたアイテム $a$** | **次の状態 $s'$** と **次回候補のアイテム $a'$** |
| **出力** | 現在の予測 Q 値 $q(s, a, w)$ および pCTR | 正解ラベル生成用の未来 Q 値 $q(s', a', w_{\mathrm{label}})$ および pCTR |

#### なぜ右側の「Label Network」が必要なのか？（動く標的問題の防止）

強化学習（TD学習 / Q学習）では、正解となる教師データが最初から存在せず、以下の式のように **「未来の期待 Q 値」を自己参照（ブートストラップ）して正解ラベル（LTV Label）を自作** する：

$$ \text{LTV Label} = r(s, a) + \gamma \sum_{a' \in A'} \mathrm{pCTR}(s', a', A') \cdot q(s', a', w_{\mathrm{label}}) $$

もし現在学習中の左側のネットワーク自身で未来の Q 値を計算してしまうと、**「自分がパラメータを更新すると正解ラベルの位置も勝手に動いて逃げていく」という「動く標的問題（Moving Target Problem）」** が発生し、学習が激しく振動・発散して崩壊してしまう。

そのため、DQN と同様に以下の2台同期サイクルを導入している：
1. **安全なラベル生成**: 右側の **重みが固定された Label Network** を使って、ブレない安定した正解ラベル（LTV Label）を計算する。
2. **メインモデルの学習**: 左側の Main Network がその正解ラベルを目指して重みを更新する。
3. **定期的な同期**: $M$ 回の学習ステップごとに、左側の Main Network の最新パラメータを右側の Label Network へ上書きコピーして同期する。


---

## 結果

著者らは、シミュレーション環境（Dopamine ベース）での網羅的なアルゴリズム比較、および YouTube 本番環境での大規模 A/B テストを実施した。

---

### 1. シミュレーション実験: 近視眼的 vs 長期的価値（LTV）

5,000 人のシミュレーションユーザーを用い、30万ステップ学習させた各アルゴリズムのセッション平均リターン（Avg. Return）および推薦品質（Avg. Quality）を測定した。

#### Table: Comparison of Myopic vs. LTV Policies (300K steps).
| Strategy | Avg. Return (%) | Avg. Quality (%) |
| :--- | :---: | :---: |
| Random | 159.2 | -0.5929 |
| MYOP-TS (近視眼的 Top-$k$) | 166.3 (4.46% 改善) | -0.5428 (8.45% 改善) |
| MYOP-GS (近視眼的 貪欲法) | 166.3 (4.46% 改善) | -0.5475 (7.66% 改善) |
| SARSA-TS (オンポリシー LTV) | 168.4 (5.78% 改善) | -0.4908 (17.22% 改善) |
| SARSA-GS | 172.1 (8.10% 改善) | -0.3876 (34.63% 改善) |
| QL-TT-TS (Q-learning Top-k訓練/Top-k推論) | 168.4 (5.78% 改善) | -0.4931 (16.83% 改善) |
| QL-GT-GS (貪欲法訓練/貪欲法推論) | 172.9 (8.61% 改善) | -0.3772 (36.38% 改善) |
| QL-OT-TS (最適訓練/Top-k推論) | 169.0 (6.16% 改善) | -0.4905 (17.27% 改善) |
| QL-OT-GS (最適訓練/貪欲法推論) | 173.8 (9.17% 改善) | -0.3408 (42.52% 改善) |
| **QL-OT-OS (最適訓練/最適推論)** | **174.6 (9.67% 改善)** | **-0.3056 (48.46% 改善)** |

※ カッコ内のパーセンテージは Random ベースラインからの改善幅。

- **考察**:
  - SlateQ を用いたすべての LTV 手法（SARSA, QL）は、近視眼的モデル（MYOP）を大幅に上回るリターンを達成した。例えば QL-OT-GS は、Random からの改善幅において MYOP の **2倍以上（+105.6%）** の向上を示した。
  - LTV モデルは推薦品質（Avg. Quality）が劇的に高く（最大 +48.46%）、高品質な推薦がユーザーセッション長を延伸させ、結果として累積エンゲージメントを最大化していることが確認された。

---

### 2. SlateQ vs 非分解フルスレート Q学習（Full Slate Q: FSQ）

スレート全体を行動として直接扱う非分解モデル FSQ と、SlateQ（SARSA-TS）の比較。実行可能なトイサイズ（候補数 20、スレートサイズ 3、全 1,140 スレート）で検証。

#### Table: SlateQ vs. Full Slate Q (FSQ).
| Strategy | Avg. Return (%) | Avg. Quality (%) |
| :--- | :---: | :---: |
| Random | 160.6 | -0.6097 |
| FSQ (非分解フルスレートQ学習) | 164.2 (2.24% 改善) | -0.5072 (16.81% 改善) |
| **SARSA-TS (SlateQ)** | **170.7 (6.29% 改善)** | **-0.5340 (12.41% 改善)** |

- **考察**:
  - FSQ は理論上最適方策に収束可能だが、1,140 通りのスレートを行動として個別学習しなければならないため、探索と汎化が極めて困難であり、同じ学習量ではリターン 164.2 にとどまった。さらに FSQ の学習時間は SlateQ の **約6倍** を要した。
  - 一方、SlateQ はアイテム単位の分解により劇的に効率的な学習を実現し、Random からの改善幅で **FSQ の約2.8倍（+180%増）** の圧倒的な優位性を示した。

---

### 3. ユーザー選択モデルの不一致に対する頑健性（Robustness to User Choice）

ユーザーが多項ロジットではなく、上位から順に閲覧して確率的に消費する **カスケードモデル（Cascade Model）** に従って行動する場合のロバスト性評価。モデル側は多項ロジット仮定のまま学習・推論を行う。

#### Table: Robustness to Cascade User Choice Model.
| Strategy | Avg. Return (%) | Avg. Quality (%) |
| :--- | :---: | :---: |
| Random | 159.9 | -0.5976 |
| MYOP-TS | 163.6 (2.31% 改善) | -0.5100 (14.66% 改善) |
| SARSA-TS | 166.8 (4.32% 改善) | -0.4171 (30.20% 改善) |
| QL-TT-TS | 166.5 (4.13% 改善) | -0.4227 (29.27% 改善) |
| QL-OT-TS | 167.5 (4.75% 改善) | -0.3985 (33.32% 改善) |
| **QL-OT-OS** | **167.6 (4.82% 改善)** | **-0.3903 (34.69% 改善)** |

- **考察**:
  - 真のユーザー選択行動がモデルの仮定と完全に一致しない過酷な環境下であっても、SlateQ は近視眼的ベースライン（MYOP）を一貫して上回り続けた。現実の推薦環境で選択モデルが厳密に成立しない場合でも実用的な頑健性を持つことが証明された。

---

### 4. YouTube 本番環境での大規模ライブ実験（Live Experiments）

YouTube の数十億ユーザーに対し、3週間にわたる実トラフィック A/B テストを実施。既存の本番近視眼的モデル（MYOP-TS）を対照群（Control）、SlateQ（SARSA-TS）を処置群（Treatment）として比較した。

#### 対照群（Control: MYOP-TS）と処置群（Treatment: SARSA-TS）の構成比較

比較の公平性（Fair Comparison）を担保するため、両者は **入力特徴量・共有DNN層・候補生成器・探索アルゴリズムに至るまで完全に同一のインフラ・アーキテクチャ** を共有している：

| 構成要素 | 対照群（Control: MYOP-TS） | 処置群（Treatment: SARSA-TS） |
| :--- | :--- | :--- |
| **モデルの正体** | **当時の YouTube 本番環境で実稼働していた最高峰ランカー** | SlateQ 分解に基づく長期価値（LTV）ランカー |
| **入力特徴量** | ユーザー過去履歴・行動統計量・静的属性、アイテム特徴（共通） | 共通（同一の特徴量ベクトルを使用） |
| **共有中間層 (DNN)** | 4層 FC（2048 $\to$ 1024 $\to$ 512 $\to$ 256、ReLU、共通） | 共通（同一構造の共有バックボーン） |
| **候補生成器** | 数億件から上位数百件を抽出（共通） | 共通 |
| **探索・選定手法** | トンプソンサンプリング（TS）による貪欲上位 $k$ 件選定 | トンプソンサンプリング（TS）による貪欲上位 $k$ 件選定 |
| **ランキングの目的関数**<br>（唯一の差異） | **即時エンゲージメント（Myopic）**<br>・今クリックされるか（pCTR）<br>・**直後に何分見られるか（目先の期待視聴時間）** | **長期エンゲージメント（LTV / Q値）**<br>・今クリックされるか（pCTR）<br>・**将来にわたる累積視聴時間（$\bar{Q}(s, i)$）** |

![Aggregate user engagement increase](./images/twt_stats_qydra.png)
*(Figure 1: 対照群に対する累積ユーザーエンゲージメント時間（Viewtime）の増加率推移。全データポイントは 95% 信頼区間内で統計的に有意)*

![Engagement by position](./images/engagement_by_position.png)
*(Figure 2: スレート内の提示順位（Position 1〜10）ごとの累積エンゲージメント分布の変化)*

- **実世界での成果と考察**:
  - **エンゲージメント時間の有意な増加（Figure 1）**:
    - 単純なトイモデルではなく、Google エンジニア陣が極限まで最適化し尽くした「本番最強の近視眼的DNN」と全く同じ土俵（DNN構造や特徴量）で戦わせた結果、**スコアリングを即時視聴時間から長期 Q 値に切り替えただけで、3週間の実験期間全体にわたり総エンゲージメント時間（Viewtime）を一貫して有意に向上** させた。
  - **上位スロットでのエンゲージメント向上（Figure 2）**:
    - スレート内の順位ごとの分析では、処置群のユーザーは特に **スレートの上位順位（Position 1〜3）に提示されたアイテムから、対照群よりも遥かに大きな長期エンゲージメントを獲得** していることが確認された。即時クリックだけでなく将来の継続視聴を呼び込む良質コンテンツが上位に適切に配置された結果である。

