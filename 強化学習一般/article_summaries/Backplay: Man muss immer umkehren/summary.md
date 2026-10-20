# Backplay: "Man muss immer umkehren"

- **著者**: Cinjon Resnick, Wes Eldridge, David Ha, Alberto Maria Dai, Devon Hjelm
- **所属**: DeepMind, Google Brain, Mila (Université de Montréal)
- **発表**: arXiv:1807.06919 (2018)

---

## 背景

### 疎報酬（Sparse Rewards）環境における強化学習の根本的困難
モデルフリー深層強化学習（Deep RL）は、碁、将棋、チェスなどの完全情報ゲームやビデオゲームにおいて著しい成功を収めてきた。しかし、エージェントが偶然報酬を受け取るまで試行錯誤を繰り返すモデルフリー強化学習は、**報酬が疎（Sparse Rewards）である環境**において膨大な探索ステップ数と計算時間を要する。
特にゴール達成時のみ正の報酬が得られる環境では、初期状態 $s_{0}$ からゴール $s_{*}$ に至るまでの行動系列が長くなるほど、ランダム探索によって報酬シグナルが得られる確率は状態空間の次元や手数に対して指数関数的に減衰する。結果として、方策勾配法やQ学習の学習シグナル（クレジット割り当て）が機能せず、学習が停滞する。

### 既存の対処法とその限界
この疎報酬問題を解決するために、従来は主に以下の3つのアプローチが取られてきたが、それぞれ本質的な弱点を抱えていた：

1. **人手による報酬シェーピング（Reward Shaping）**:
   ゴールへの距離関数などを補助報酬として設計する手法。効果的である一方、職人芸的なチューニングを要し、少しでも設計を誤ると元のタスクの最適方策とは異なる意図しないバグ行動（報酬ハッキング；例：ゴールせずに報酬が得られるループを行き来する）を学習してしまう危険がある。
2. **模倣学習（Behavioral Cloning / GAIL 等）**:
   人間のエキスパートによる実演軌道（Demonstrations）の $(s, a)$ ペアを模倣する手法。しかし、実演が不完全・下手（Sub-optimal）であった場合、その誤りや遠回りまで完全に模倣してしまい、**「実演以上の性能を発揮できない」** という致命的な限界がある。また、GAIL 等の敵対的模倣学習はハイパーパラメータ調整が極めて不安定で、多くの環境相互作用を要する。
3. **逆方向カリキュラム生成（Reverse Curriculum Generation; RCG / Florensa et al., 2017）**:
   ゴール状態からランダムウォーク（ブラウン運動）で徐々に開始地点を広げていくカリキュラム学習。しかし、環境の物理的・遷移的な「可逆性（Reversibility）」の仮定が必要であり、かつ広い状態空間ではゴールから無関係な行き止まりや無駄な領域へとランダムに迷い込んでしまい、サンプル効率が著しく低下する。

### 本研究の動機とアプローチ
本論文は、数学者カール・ヤコビの有名な格言 **"Man muss immer umkehren"（常に逆から考えよ / Invert, always invert）** に着想を得て、これらの限界を同時に打破する手法 **Backplay** を提案した。
Backplay は、**「たった1本の、ある程度成功している実演軌道（Good enough trajectory）」** が与えられたとき、その実演の**終端（ゴール直前）から開始し、学習が進むにつれて開始地点を初期状態方向へと巻き戻していく（Backwards）**。
エージェントは実演の「行動（Action）」を模倣するのではなく、単に実演軌道上の状態を「初期開始地点」として利用し、そこから先は自身の強化学習（PPO等）で純粋に報酬を最大化する。これにより、**不完全な実演であっても、それを大幅に上回る最適な方策を自発的に学習できる**。

---

## 手法

### 1. MDPの定式化と関連手法との比較
単一エージェントのマルコフ決定過程（MDP）を組 $\mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{T}, r, \gamma)$ で定義する。
- 状態空間 $\mathcal{S}$
- 行動空間 $\mathcal{A}$
- 状態遷移関数 $\mathcal{T}: \mathcal{S} \times \mathcal{A} \to \mathcal{P}(\mathcal{S})$
- 報酬関数 $r: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$
- 割引率 $\gamma \in [0, 1]$

エージェントの確率的方策を $\pi: \mathcal{S} \to \mathcal{P}(\mathcal{A})$ とし、期待割引累積リターン $R_{t} = \mathbb{E} \left[ \sum_{k=0}^{\infty} \gamma^{k} r_{t+k+1} \right]$ の最大化を目指す。

#### Table 1: 関連手法と Backplay の比較
原著論文で示された、模倣学習（BC, GAIL）、逆カリキュラム生成（RCG）、および Backplay の要求条件・基本思想・主な弱点の比較は以下の通りである。

| Method | Requirements | Main Idea | Main Weakness |
|---|---|---|---|
| BC | (State, Action) pairs from expert trajectory. | Learn policy that imitates the expert demonstration. | Sub-optimal expert can yield a very poor learned policy. |
| GAIL | (State, Action) pairs from expert trajectory. | Learn a policy that matches the distribution of expert trajectory pairs. | Difficult to tune; Requires more world interactions; Can perform worse than BC. |
| RCG | Reversable transition function of environment; Resettable environment. | Take random walks from goal state to build curriculum of initial starting states. | Complexity may increase if random walks reach parts of state space irrelevant to a good policy. |
| **Backplay** | State sequence from a `good enough' trajectory; Resettable environment. | Sample starting state from given trajectory by walking backward along trajectory. | If states in `good enough' trajectory are not optimal, then can slow learning the \textit{optimal} policy. |

### 2. Backplay アルゴリズムのメカニズム
Backplay では、ゴール $s_{*}$ に到達する実演軌道の状態系列（行動系列は不要）を以下のように表す：

$$
\tau^{d} = \lbrace s^{d}_{0}, s^{d}_{1}, \dots, s^{d}_{T} \rbrace
$$

環境は任意の状態へリセット可能であると仮定する。各訓練エピソードにおいて、エージェントの初期状態 $s_{\text{start}}$ を真の初期状態 $s_{0}$ からではなく、実演軌道上の終端に近いサブシーケンスから一様サンプリングする：

$$
s_{\text{start}} \sim \text{Unif}\left( \lbrace s^{d}_{T-k}, s^{d}_{T-k+1}, \dots, s^{d}_{T-j} \rbrace \right)
$$

ここで $[j, k]$ はサンプリングウィンドウ（窓）である。
- **学習初期**: 例えばウィンドウを $[0, 4)$ に設定し、ゴール直前の状態 $\lbrace s^{d}_{T-4}, \dots, s^{d}_{T} \rbrace$ から開始する。この位置からはランダム行動でも数ステップでゴールに届き、正の報酬が得られるため、価値関数 $V(s)$ と方策 $\pi(a|s)$ が即座に立ち上がる。
- **学習の進行**: カリキュラムのスケジュールに従い、エポックの進行とともに $j$ と $k$ の値を増やしてウィンドウを過去方向（初期状態方向）へ前進（巻き戻し）させる。
- **学習完了時**: 最終的に $j = k = T$ となり、エージェントは実演の助けを一切借りず、真の初期状態 $s^{d}_{0}$ からのみ開始してタスクを完走できるようになる。

![backplay-graphic-lg](./images/backplay-graphic-lg.png)
*図: Backplay の概念図。実演軌道（実線）の終端から開始し、ウィンドウを後退させながらエージェント自身の探索（点線）によって価値を伝播させる。*

### 3. 理論的解析：サンプル複雑度の指数的改善
論文では、連結無向グラフ $G = (V, E)$ 上のランダムウォーク型ナビゲーションタスクにおいて、Backplay がサンプル効率をどれだけ改善するかを理論的に解析している。
開始ノード $v_{0}$ から目標ノード $v_{*}$ への到達時間を解析するため、グラフ上の距離 $z_{t} = \text{dist}_{G}(s_{t}, v_{*})$ への射影マルコフ連鎖 $\overline{K}$ を考える。目標に向かって近づく遷移確率を $\alpha_{l} = \alpha$（一定）とする。

- **標準的な強化学習（Standard RL）**:
  目標ノード $s_{*}$（吸収状態）に初めて到達するまでの期待到達時間は、推移確率行列のスペクトルギャップ（Spectral Gap）の逆数に支配され、グラフの直径 $M$ に対して指数関数的になる：
  
  $$
  T_{\text{standard}} = \Omega\left( \alpha^{-M/2} \right)
  $$

- **Backplay**:
  ステップ幅 $m$ で終端から遡る場合、各局所区間での吸収到達確率は $\gamma_{0, m} = \alpha^{m}$ で下限付けられる。区間ごとに価値関数を確定させて遡るため、全体のサンプル複雑度は以下のようになる：
  
  $$
  T_{m} = O\left( \frac{M^2}{m} \frac{1 - \alpha^{m+1}}{1 - \alpha} \alpha^{-m} \right) \sim O\left( \frac{M^2}{m} \alpha^{-m} \right)
  $$

**定理 1**: グラフの直径 $M$ が大きい場合、標準的な強化学習のサンプル複雑度が $\Omega(M \alpha^{-M/2})$ と指数関数的に爆発するのに対し、Backplay は $O(\frac{M^2}{m} \alpha^{-m})$ となり、**グラフの直径に関して指数的なサンプル効率の改善を達成する**。

また、軌道全体から無作為に一様サンプリングする手法（Uniform Baseline）のサンプル複雑度は $O(M^3 \alpha^{-1})$ であり、Backplay（$m=1$ のとき $O(M^2 \alpha^{-1})$）に比べてファクター $M$ だけ遅くなることが示されている。

### 4. Backplay の適用条件（定性分析）
論文では、どのような環境で Backplay が有効に働き、どのような環境で不利になるかを3つのグリッドワールドを用いて視覚的に分類・整理している（Figure 1）。

![Figure 1: 三つのグリッドワールド環境](./images/alex_pomme_grid_backplay_good.png)
*(a) Backplay Helps（広大な自由空間）*

![Figure 1: 三つのグリッドワールド環境](./images/pomme_grid_backplay_good.png)
*(b) Backplay Helps（ボトルネックのある迷路）*

![Figure 1: 三つのグリッドワールド環境](./images/alex_pomme_grid_backplay_bad.png)
*(c) Backplay Hinders（デモが極端な袋小路に迷い込んでいる環境）*

- **(a) 広大な空間**: 準最適な実演であっても高価値状態の近傍にエージェントを配置できるため、次元の呪いを軽減し、実演より優れた方策を学習できる。RCG のようなランダムウォークは拡散してしまい非効率となる。
- **(b) ボトルネック迷路**: 右側の誤った部屋に迷い込む無駄な探索を劇的に削減できる。行動クローニング（BC）では軌道から外れた際に破綻するが、Backplay は実演近傍の探索も自発的に行うため頑健である。
- **(c) 極端な準最適デモ**: 実演が極端な回り道をして深い窪地に捕まっている場合、Backplay は初期の訓練リソースをその準最適軌道の探索に費やしてしまうため、初期状態から直接右上の近道を見つけられる標準RLの方が速い場合がある。

---

## 結果

### 1. 100種類の迷路（Maze）実験

#### 実験設定
- $24 \times 24$ のグリッド上に 120 個の壁をランダム配置した迷路を 100 種類作成。
- エージェントの入力は $24 \times 24$ のバイナリマップ4枚（自身、ゴール、通路、壁）。
- ゴール到達で $+1$、各ステップごとに $-0.03$ のペナルティ。最大 200 ステップ。
- A* アルゴリズムで生成した実演を使用：
  - **Optimal**: 最短経路の実演
  - **5-Optimal**: 最短経路より 5 ステップ長い準最適実演
  - **10-Optimal**: 最短経路より 10 ステップ長い準最適実演
- 比較ベースライン：
  - **Standard**: 常に初期状態 $s_{0}$ から開始する通常の PPO
  - **Uniform**: 実演軌道全体から一様に開始状態をサンプリングする PPO
  - **Florensa (RCG)**: ゴールからブラウン運動で開始状態を広げる手法
  - **Behavioral Cloning (BC)**: 実演軌道の行動模倣

#### Table 2: 100種類の迷路における2000エポック後の学習結果（完全転記）
原著論文 Table 2 の全データを一切省略せず完全に書き起こした。

| Algorithm | Map Set | % Optimal | % 0-5 Optimal | Avg Suboptimality | Std Suboptimality |
|---|---|---|---|---|---|
| Standard | All | 0 | 0 | N/A | N/A |
| Uniform | Optimal | 27 | 91 | 8.26 | 32.92 |
| Uniform | 5-Optimal | 51 | 98 | 2.04 | 17.39 |
| Uniform | 10-Optimal | 49 | 98 | 2.04 | 16.79 |
| Florensa | Optimal | 20 | 51 | 63.36 | 78.08 |
| Florensa | 5-Optimal | 48 | 77 | 25.44 | 56.89 |
| Florensa | 10-Optimal | 49 | 69 | 39.75 | 70.92 |
| **Backplay** | **Optimal** | **31** | **100** | **0.64** | **4.96** |
| **Backplay** | **5-Optimal** | **37** | **94** | **7.94** | **33.35** |
| **Backplay** | **10-Optimal** | **54** | **99** | **0.37** | **3.49** |

#### Table 3: 迷路における Backplay のハイパーパラメータ（完全転記）

| Starting at training epoch | Uniform window |
|---|---|
| 0 | [0, 4) |
| 350 | [4, 8) |
| 700 | [8, 16) |
| 1050 | [16, 32) |
| 1400 | [32, 64) |
| 1750 | [64, 64) |

#### 迷路実験における学習曲線（Figure 4, 5, 6）

![Figure 4: Optimal 実演での迷路学習曲線](./images/iclr-revised-reg-quadratic-b80-legendleft-exstandard-min1000.png)
*Figure 4: 最短経路の実演（Optimal）を用いた場合の学習曲線。Backplay はエポック 1800 という極めて早い段階で分散が非常に小さく、高い成功率を達成。一方、Florensa (RCG) は成功率 70% を超えられず分散が大きい。Uniform はエポック 3000 まで成功率が上がらない。*

![Figure 5: 5-Optimal 実演での迷路学習曲線](./images/iclr-revised-5opt-quadratic-b80-legendleft-exstandard-min1000.png)
*Figure 5: 最短より 5 ステップ長い準最適実演（5-Optimal）を用いた場合の学習曲線。Backplay は Florensa よりも一貫して高い期待リターンを維持し、Uniform に対して大幅に少ないサンプル数で収束している。*

![Figure 6: 10-Optimal 実演での迷路学習曲線](./images/iclr-revised-10opt-quadratic-b80-legendleft-exstandard-min1000.png)
*Figure 6: 最短より 10 ステップ長い準最適実演（10-Optimal）を用いた場合の学習曲線。実演が大きく遠回りしている下手なデモであっても、Backplay は Florensa より遥かに安定して高リターンを獲得し、デモを凌駕する最適方策を学習している。*

#### 迷路実験の結果と考察
1. **Standard の完全な失敗**: 通常の PPO（Standard）は疎報酬の探索を打開できず、2000エポック経過しても成功率 **0%** であった。
2. **実演を超える能力（Surpassing Sub-optimal Demonstrations）**: Backplay は、最短手より 10 手も遠回りしている下手な実演（10-Optimal）から学習させた場合でも、**54% の迷路で最短手（最適経路）を自発的に発見し、99% で最短＋5手以内の準最適解に到達**した。平均超過ステップ数はわずか **0.37 手** であり、デモの回り道を完全にショートカットしている。
3. **模倣学習（BC）との決定的な違い**: BC で学習させたエージェントは実演を完全に模倣できたものの、実演以上の性能向上（強化学習による微調整）を試みても全く改善しなかった。実演軌道外の状態価値に関する情報を持たないためである。
4. **Florensa (RCG) に対する優位性**: RCG は迷路の行き止まりに拡散してしまうため、成功率は 50〜70% 程度に留まり、分散（Std Suboptimality: 56〜78）が極めて大きかった。Backplay は成功軌道に沿って後退するため、極めて安定した学習が可能となった。

---

### 2. Pommerman（4人対戦爆弾ゲーム）実験

#### 実験設定
- NeurIPS 2018 のコンペティション環境である $11 \times 11$ グリッドの Free-For-All（FFA; 4人生き残り戦）。
- 対戦相手の3体は、2018年6月の大会優勝エージェントである FSMTS（有限状態機械木探索エージェント）のコピー。Backplay の実演としても FSMTS のプレイログを使用。
- 観測空間は 19 枚の $11 \times 11$ 特徴マップ（過去2フレームを結合して 38 チャンネルを入力）。
- 報酬設計：
  - **Sparse（疎報酬）**: 勝利で $+1$、それ以外（死亡または引き分け）で $-1$。
  - **Dense（密報酬）**: 上記に加え、アイテム取得時に $+0.1$。最大 800 ステップ。

![Figure 7: Pommerman 開始画面](./images/pommerman-start.png)
*Figure 7: Pommerman のゲーム開始局面。四隅にエージェントが配置され、木箱（黄色）と破壊不能壁（茶色）で仕切られている。*

#### Table 4: Pommerman 4マップ設定におけるハイパーパラメータ（完全転記）

| Starting at training epoch | Uniform window |
|---|---|
| 0 | [0, 32) |
| 50 | [24, 64) |
| 100 | [56, 128) |
| 150 | [120, 256) |
| 200 | [248, 512) |
| 250 | [504, 800) |
| 300 | [800, 800] |

#### Table 5: Pommerman 100マップ設定におけるハイパーパラメータ（完全転記）

| Starting at training epoch | Uniform window |
|---|---|
| 0 | [0, 32) |
| 85 | [24, 64) |
| 170 | [56, 128) |
| 255 | [120, 256) |
| 340 | [248, 512) |
| 425 | [504, 800) |
| 510 | [800, 800] |

#### Table 6: 100マップにおける Backplay の勝率分布（完全転記）
総計 5000 回以上評価（各マップ最低 32 回対戦）。

| Win Rate | Maps |
|---|---|
| 90% 以上 | 24 |
| 80% 以上 | 26 |
| 70% 以上 | 6 |
| 60% 以上 | 5 |
| 50% 以上 | 5 |

※ 半数以上のマップ（50マップ）で勝率 80% 以上を記録し、全マップで勝率 50% 以上（4人対戦において均等なら 25%）を達成。

#### Pommerman における学習結果（Figure 2, Figure 3）

![Figure 2: Sparse 報酬での学習曲線](./images/iclr-revised-sparse-quadratic-b40-m510-legendleft-font14.png)
*Figure 2 (a): 100マップ・勝者デモ（Sparse）。赤線は初期状態のみからの訓練開始エポック。Standard や Uniform が完全に学習失敗する中、Backplay は初期状態からでも極めて高い勝率を達成。*

![Figure 2 (b), (c)](./images/iclr-revised-sparse-quadratic-b40-m300-nolegend.png)
*Figure 2 (b): 4マップ・勝者デモ（Sparse） / (c): 4マップ・準優勝者デモ（Sparse）。*

![Figure 3: Dense 報酬での学習曲線](./images/iclr-revised-dense-quadratic-b30-m510-legendleft-font14.png)
*Figure 3 (a): 100マップ・勝者デモ（Dense）。アイテム報酬を追加しても、Standard や Uniform は低迷するが、Backplay は安定して高勝率を獲得。*

![Figure 3 (b), (c)](./images/iclr-revised-dense-quadratic-b40-m300-nolegend.png)
*Figure 3 (b): 4マップ・勝者デモ（Dense） / (c): 4マップ・準優勝者デモ（Dense）。*

#### 行動分布の変遷と自爆回避のメカニズム（Figure 8）

![Figure 8: Pommerman 行動選択ヒストグラム](./images/typical-genesis-histogram.png)
*(a) Standard Sparse: 学習が進むにつれて爆弾（右端）を全く置かなくなる。*

![Figure 8: Pommerman 行動選択ヒストグラム](./images/typical-fx100-histogram.png)
*(b) Backplay Sparse: 爆弾を適切に使いこなし、多彩な行動バランスを維持。*

#### Pommerman 実験の結果と考察
1. **通常RL（Standard）の局所解（自爆恐怖症）**:
   Figure 8 (a) に示すように、Standard RL は初期のランダム行動で爆弾を設置して自爆死を繰り返し、負の報酬（$-1$）を大量に被る。その結果、**「爆弾を置く行動を完全に禁止し、何もしない（Pass）」という極めて消極的な局所最適解**に退行してしまい、永久に勝利できなくなる。
2. **Backplay による終盤戦術の先行習得**:
   Backplay では、敵が残り1体となった終盤局面から開始するため、エージェントはまず「安全に爆風を避けつつ、相手を爆破して勝つ」という局所的な勝利パターンを習得する。その上でゲーム開始地点へと遡るため、**「爆弾を安全に使い、壁を破壊してアイテムを取り、敵を追い詰める」という攻撃的かつ高度な立ち回りを確実に学習**できた。
3. **実演にない新規プレイスタイルの創発**:
   学習したエージェントは、実演者である FSMTS さえ使っていなかった**「爆弾をキックして相手に投げつける（Bomb throwing）」という独自のプレイスタイル**を自発的に編み出した。これは、Backplay が実演の行動に縛られず、純粋な報酬最大化によって最適方策を探索していることの決定的な証拠である。

---

## 考察とカードゲームへの示唆

### 実務的知見（Practical Findings）
- **ウィンドウの進行速度**: ウィンドウの巻き戻しを「急ぎすぎる」と方策が崩壊するが、「ゆっくりすぎる」分には何ら破綻しない。安全側に倒して保守的なスケジュールを設定すべきである。
- **適応的進行の不要性**: 成功率が一定値を超えるまで待つ適応型ルールよりも、固定エポックで定期的にウィンドウを後退させる方が、状態空間の多様な価値を大まかに把握させる上で効率的であった。

### カードゲームにおける「序盤のカード浪費問題」への直接的示唆
本論文の知見は、**「勝敗報酬が遠い環境で、序盤のやり取りがおざなりになり、手札の重要カードを無駄打ちしてしまう」** というカードゲーム強化学習の課題に対し、即座に適用可能な解決策を提供する：

1. **「勝利棋譜の巻き戻しリセット」による序盤制御**:
   - カードゲームシミュレータ上で、人間や既存AIが勝利した対戦ログ（1局の手番系列）を用意する。
   - **初期エポック**: 互いの残り手札が1〜2枚、あるいは最終ターンの「詰め」局面から開始する。エージェントは1〜2手で勝敗報酬 $+1/-1$ を得るため、「どのカードを切れば勝てるか」を即座にマスターする。
   - **中期〜後期エポック**: 開始地点を中盤、そして開幕ターン（フル手札）へと徐々に遡らせる。
   - **効果**: エージェントはすでに「終盤にどのカードが残っていれば勝てるか」の価値関数を完全に把握しているため、**「開幕に適当に切り札を切ると、後で自分が勝てる終盤の盤面に移行できなくなる」という因果関係を損失として正しく評価**できるようになり、序盤の無駄打ちが自然に消滅する。
2. **不完全なプレイングからの脱却**:
   模倣学習と異なり、実演者が序盤に少し非効率なカードの切り方をしていたとしても、Backplay は行動を強制しないため、エージェント自身のRLによって「人間よりもさらに無駄のない完璧な手札温存」を自力で発見できる。
