# Distributional GFlowNets with Quantile Flows
（原題: Distributional GFlowNets with Quantile Flows）

**arXiv:** [2302.05793](https://arxiv.org/abs/2302.05793)  
**ジャーナル:** TMLR 2024 (Transactions on Machine Learning Research)  
**著者:** Dinghuai Zhang$^{1 *}$, Ling Pan$^{2 *}$, Ricky T. Q. Chen$^3$, Aaron Courville$^1$, Yoshua Bengio$^{1,4}$ ($^*$Equal contribution)  
（$^1$Mila - Université de Montréal, $^2$Hong Kong University of Science and Technology, $^3$Meta AI - FAIR, $^4$CIFAR AI Chair）  
**発表:** 2023年2月（TMLR 2024採択）  
**対象タスク:** 確率的報酬（Noisy / Stochastic Rewards）環境下での生成モデリング、リスク感応的生成（Risk-Sensitive Generation / リスク回避）、離散構造生成（分子設計・生物配列生成・Hypergrid）、生成的フローネットワーク（GFlowNet）

---

## 背景

Generative Flow Networks（GFlowNet）は、目的の報酬関数 $R(x)$ に比例した確率 $P(x) \propto R(x)$ で、高報酬かつ多様な候補群を非反復的（1パス）に直接サンプリングできる強力なフレームワークとして急速に発展してきた。

しかし、従来のすべての GFlowNet（Flow Matching や Trajectory Balance など）には、**「報酬関数 $R(x)$ は完全に確定したスカラー値（決定論的）でなければならない」という重大な制約** が存在していた。現実世界のタスクにおいて、この仮定は以下の致命的な限界をもたらす：

1. **確率的報酬（Stochastic / Noisy Rewards）における数学的破綻**:
   - 実世界の創薬実験や物理計測、ユーザ評価などでは、観測ノイズや環境の揺らぎにより、同一のオブジェクト $x$ に対しても報酬が確率変数 $R(x)$ としてブレる。
   - 著者らは、**従来の GFlowNet を確率的報酬に適用すると、生成確率が真の期待値 $\mathbb{E}[R(x)]$ ではなく、幾何平均 $\exp(\mathbb{E}[\log R(x)])$ に比例してしまう** ことを数学的に証明した（Proposition 1）。対数変換の非線形性により、期待値サンプリングが歪んでしまうのである。
2. **リスク不確実性（Risk Uncertainty）への無力さ**:
   - 医療（創薬）やロボティクス、金融などのクリティカルな領域では、「平均的な期待値は高いが、稀に破滅的な低報酬（致死的な副作用や大事故）をもたらす危険な候補」を避ける **リスク感受性（Risk-Sensitivity / リスク回避性）** が不可欠である。
   - しかし、スカラー値のフローしか持たない従来の GFlowNet は、「結果のばらつき（分散やテールリスク）」を一切認識できず、危険な領域と安全な領域を区別できない。

![Illustration of a distributional GFlowNet with stochastic edge flows](./images/dist_gfn.png)
*(Figure 1: 分布型 GFlowNet の概念図。各エッジフローを単一のスカラーではなく、確率分布（灰色の曲線）としてモデル化することで、確率的報酬やリスク不確実性に対応する)*

これに対し著者らは、分布型強化学習（Distributional RL）に着想を得て、**フロー関数そのものを確率分布としてモデル化し、分位点関数（Quantile Function）を用いてパラメータ化する「Distributional GFlowNets（Quantile Matching）」** を提案した。

---

## 手法

### 0. 手法の全体像（Input / Output / 最適化の目的）

Distributional GFlowNet を機械学習モデルとして簡潔に整理すると、以下の設計となっている：

- **Input（入力）**:
  - **現在の状態 $s$ と次の状態 $s'$（エッジ $s \to s'$）**、および **分位点確率 $\beta \in [0, 1]$**
- **Output（出力）**:
  - **エッジフローの $\beta$-分位点予測値 $Z_\beta^{\log}(s \to s'; \theta)$**
  - 単一の平均値ではなく、Implicit Quantile Network（IQN）によって「任意のパーセンタイル $\beta$ における流量」を柔軟に出力する。
- **何を最小化して学習するか？（損失関数）**:
  - **「分位点マッチング（Quantile Matching: QM）損失」**
  - フロー保存則（入る水＝出る水）を、すべての分位点 $\beta, \tilde{\beta} \in [0, 1]$ にわたって **ピンボール損失（Quantile Regression Loss）** により整合させる。
  - ゴールの排水口では、観測された確率的報酬 $R(x)$ の分布へと直接一致させる。
- **推論時（生成時）の流れ**:
  - 各エッジの分位点関数を数値積分して期待値（またはリスク尺度）を計算し、前向き確率 $P_F(s' \mid s)$ を導出してサンプリングする。

---

### 1. 分位点フロー（Quantile Flows）の定式化

各エッジを通過する流量をスカラーではなく確率変数 $Z(s \to s')$ と見なす。  
この確率変数を表現するため、累積分布関数（CDF）の一般化逆関数である **分位点関数（Quantile Function） $Q_Z(\beta): [0, 1] \to \mathbb{R}$** を用いる。

確率変数 $Z$ の期待値は、分位点関数の均一積分として表される：
$$ \mathbb{E}[Z] = \int_0^1 Q_Z(\beta) d\beta $$

---

### 2. 分位点加法性（Quantile Additivity）による高速計算

従来の分布型RL（Categorical DQN等）を GFlowNet に適用しようとすると、複数の流入・流出フローの和を計算するために膨大な回数の **「確率分布の畳み込み（Convolution）」** が必要になり、計算量が爆発する（Remark 1）。

著者らは、確率論における **分位点加法性（Proposition 2: Quantile Additivity）** を活用することでこの問題を美しく解決した：

> **Proposition 2 (Quantile Additivity):**
> 共通の乱数 $\beta \in [0, 1]$ を共有する確率変数の組 $\{Z^m\}_{m=1}^M$ について、その和 $Z^0 = \sum_{m=1}^M Z^m$ の分位点関数 $Q^0(\beta)$ は、**各変数の分位点関数の単純な足し算** として表される：
> $$ Q^0(\beta) = \sum_{m=1}^M Q^m(\beta) $$

これにより、畳み込み計算を一切行うことなく、単なるテンソルの加算のみで複数フローの合流を瞬時に計算できる。

---

### 3. 分位点マッチング（Quantile Matching: QM）アルゴリズム

エッジの $\beta$-分位点を、数値的安定性のために対数スケール $Z_\beta^{\log}(s \to s'; \theta)$ でモデル化する。

中間状態 $s'$ において、流入フローの $\beta$-分位点と流出フローの $\tilde{\beta}$-分位点の間の TD 的な誤差 $\delta$ を定義する：

$$ \delta^{\beta, \tilde{\beta}}(s'; \theta) = \log \sum_{(s' \to s'') \in \mathcal{A}} \exp Z_{\tilde{\beta}}^{\log}(s' \to s''; \theta) - \log \sum_{(s \to s') \in \mathcal{A}} \exp Z_\beta^{\log}(s \to s'; \theta) $$

分位点回帰（Quantile Regression）の理論に基づき、**ピンボール損失 $\rho_\beta(\delta) = |\beta - \mathbb{I}\{\delta < 0\}| |\delta|$** を用いた **Quantile Matching (QM) 損失** を最小化する：

$$ \mathcal{L}_{\mathrm{QM}}(s'; \theta) = \frac{1}{\tilde{N}} \sum_{i=1}^N \sum_{j=1}^{\tilde{N}} \rho_{\beta_i}\left( \delta^{\beta_i, \tilde{\beta}_j}(s'; \theta) \right) $$

ここで $\beta_i, \tilde{\beta}_j \sim \mathcal{U}[0, 1]$ は一様分布から独立にサンプリングされる。

#### 推論時の前向き方策
学習完了後、エッジフローの期待値を数値積分で推定し、前向き確率 $P_F$ を求める：

$$ P_F(s' \mid s) \propto \mathbb{E}[Z(s \to s')] \approx \frac{1}{N} \sum_{i=1}^N \exp\left( Z_{\beta_i}^{\log}(s \to s'; \theta) \right) $$

---

### 4. 歪みリスク尺度（Distortion Risk Measures）によるリスク感応的方策

分位点関数を手に入れた最大の恩恵は、**「リスクに対する姿勢（リスク回避・リスク追求）」を自由自在にコントロールできる** 点にある。

単なる期待値の代わりに、単調な歪み関数 $g: [0, 1] \to [0, 1]$ を適用した **歪み期待値（Distorted Expectation）** を用いる：

$$ \mathbb{E}^g[Z] = \int_0^1 Q_Z(g(\beta)) d\beta $$

代表的な歪み関数：
- **CVaR（Conditional Value-at-Risk / 条件付きバリュー・アット・リスク）**:
  $$ g(\beta; \eta) = \eta \beta \quad (\eta \in (0, 1]) $$
  下位 $100 \times \eta\%$ の最悪ケースの平均値のみを評価する。**極めて強力なリスク回避的行動** を誘導する。
- **Wang の変換**:
  $$ g(\beta; \eta) = \Phi\left( \Phi^{-1}(\beta) + \eta \right) $$
  $\eta < 0$ でリスク回避的、$\eta > 0$ でリスク追求的となる。
- **CPW（累積確率加重関数）**: 人間の心理的なリスク選好を模倣。

歪み関数 $g$ を用いることで、リスク感応的前向き方策は以下のように計算される：

$$ P_F^g(s' \mid s) \propto \frac{1}{N} \sum_{i=1}^N \exp\left( Z_{g(\beta_i)}^{\log}(s \to s'; \theta) \right) $$

これにより、**「平均スコアが高くても、地雷（低報酬）を踏むリスクがある選択肢」を AI が自発的に回避** するようになる。

---

### 5. 決定論的環境でも従来の GFlowNet より強くなる3大理由

驚くべきことに、本手法（QM）はノイズのない決定論的ベンチマークにおいても、従来の Flow Matching（FM）や Trajectory Balance（TB）を大幅に上回る性能を発揮した。著者らはその理由として以下の3点を挙げている：

1. **補助タスクとしてのリッチな学習シグナル**:
   - 平均値だけでなく全分位点（分布の形全体）を予測させることで、表現学習に強力な正則化がかかり、未知の軌跡への汎化性能が劇的に向上する。
2. **フローの過大評価の抑制**:
   - GFlowNet は過去の軌跡に過剰適合してフローを過大評価しやすいバイアスを持つが、分布全体を保持することで過大評価バイアスが自然に緩和される。
3. **状態エイリアシング（疑似不確実性）の解消**:
   - 決定論的環境であっても、ニューラルネットの表現力の限界により、異なる2つの状態が同一の特徴量に潰れてしまう（部分観測・エイリアシング）現象が起きる。分布型モデリングはこの疑似的な不確実性を無理なく吸収できる。

---

## 結果

著者らは、記号体系（Table 1）を定義した上で、リスク感応的タスク（Risky Hypergrid）、および決定論的な 3大標準ベンチマーク（Hypergrid、Bit Sequences、Molecule Optimization）で網羅的な実験を行った。

#### Table 1: Mathematical Notations
| Symbol | Description |
| :--- | :--- |
| $\mathcal{S}$ | state space |
| $\mathcal{X}$ | object (terminal state) space, subset of $\mathcal{S}$ |
| $\mathcal{A}$ | action / transition space (edges $s \to s'$) |
| $\mathcal{G}$ | directed acyclic graph $(\mathcal{S}, \mathcal{A})$ |
| $\mathcal{T}$ | set of complete trajectories |
| $s$ | state in $\mathcal{S}$ |
| $s_0$ | initial state, element of $\mathcal{S}$ |
| $x$ | terminal state in $\mathcal{X}$ |
| $\tau$ | trajectory in $\mathcal{T}$ |
| $F: \mathcal{T} \to \mathbb{R}$ | Markovian flow |
| $F: \mathcal{S} \to \mathbb{R}$ | state flow |
| $F: \mathcal{A} \to \mathbb{R}$ | edge flow |
| $P_F$ | forward policy (distribution over children) |
| $P_B$ | backward policy (distribution over parents) |
| $Z$ | scalar, equal to $\sum_{\tau \in \mathcal{T}} F(\tau)$ for a Markovian flow |

---

### 1. 確率的リスク付き Hypergrid 実験（Risky Hypergrid）

4隅に高報酬モードがあるが、そのうち一部のモード（緑色領域）には **「微小な確率で極めて低い報酬（地雷）に転落する確率的リスク」** が仕込まれた環境。

![A risky hypergrid environment](./images/risky_grid.png)
*(Figure 2: Risky Hypergrid 環境の構成。黄色は安全な通常モード、緑色は確率的リスクを伴うモード)*

![Risk-Averse Grid Results](./images/grid_sensitive_D2.png)
![Risk-Averse Grid Results](./images/grid_sensitive_D4.png)
![Risk-Averse Grid Results](./images/grid_sensitive_D2_modes.png)
![Risk-Averse Grid Results](./images/grid_sensitive_D4_modes.png)
*(Figure 3: Risky Hypergrid の実験結果。上段: 危険領域への違反率（Violation Rate）。下段: 発見された非リスク通常モードの数)*

- **考察**:
  - **リスク回避の成功（上段）**: CVaR(0.1) や Wang(-0.75) を適用した QM は、通常の FM やリスク中立な QM と比較して、**危険領域への進入率（Violation Rate）を劇的に抑制** した。特に下位 10% のワーストケースに注目する CVaR(0.1) は最も保守的で安全な方策を獲得した。
  - **通常モードの維持（下段）**: リスクを回避しながらも、安全な通常モードはベースラインと全く同等にすべて発見しており、探索能力を損なうことなくリスク回避を実現できることが実証された。

---

### 2. 決定論的 Hypergrid ベンチマーク

$8^3$（Small）から $20^4$（Large: 状態数 160,000）までの多次元グリッド上で、全 $2^D$ 個のモードを発見するタスク。

![Hypergrid Error](./images/grid_D3H8_error.png)
![Hypergrid Error](./images/grid_D3H16_error.png)
![Hypergrid Error](./images/grid_D4H16_error.png)
![Hypergrid Error](./images/grid_D4H20_error.png)
*(Figure 4 上段: 真の報酬分布との $\ell_1$ 誤差の推移。左から $D=3, H=8$、$D=3, H=16$、$D=4, H=16$、$D=4, H=20$)*

![Hypergrid Modes](./images/grid_D3H8_num_mode.png)
![Hypergrid Modes](./images/grid_D3H16_num_mode.png)
![Hypergrid Modes](./images/grid_D4H16_num_mode.png)
![Hypergrid Modes](./images/grid_D4H20_num_mode.png)
*(Figure 4 下段: 学習の進行に伴う発見モード数の推移)*

- **考察**:
  - 従来の TB は小規模（$8^3$）では良好だが、空間が大きくなると急速に悪化した。
  - **Quantile Matching (QM) は、すべてのスケールにおいて最低の $\ell_1$ 誤差と、最も圧倒的に速い全モード発見速度を達成** した。分布型モデリングによるリッチな学習シグナルが、決定論的環境でも探索を劇的に加速することを証明した。

---

### 3. 自己回帰ビット列生成（Bit Sequence Generation）

長さ 120 のビット列（探索空間 $2^{120}$）を自己回帰的に生成するタスク。

![Bit Sequence Results](./images/bit_sequence_dark.png)
*(Figure 5: ビット列生成タスクにおける探索ステップ数に対する発見モード数の推移)*

- **考察**:
  - A2C や SAC、MCMC、そして従来の GFlowNet（FM, TB）と比較して、**QM は最も高いサンプル効率で圧倒的に多数のモードを発見** した。

---

### 4. 実用的分子最適化（Molecule Optimization）

結合木（Junction Tree）表現に基づく分子グラフ生成タスク。薬用特性（Drug-likeness や結合親和性など）を模した報酬関数（7.5以上を高報酬モードと定義）において、多様かつ高品質な分子を探索。

![Molecule Optimization Results](./images/mol_env.png)
![Molecule Optimization Results](./images/molNumberofModes.png)
![Molecule Optimization Results](./images/molTanimotoSimilarity.png)
![Molecule Optimization Results](./images/molTop-100Reward.png)
*(Figure 6: 分子最適化実験。(a) 分子生成ポリシーの概念、(b) 報酬 7.5以上の発見モード数（高いほど良い）、(c) Tanimoto 類似度（低いほど構造が多様で良い）、(d) Top-100 分子の平均報酬（高いほど良い）)*

- **考察**:
  - **モード発見数 (b)**: QM は従来の FM や TB、MARS（MCMC）、PPO（RL）を大きく突き放し、最多の有望分子モードを発見した。
  - **多様性 (c)**: 分子間の構造類似度を示す Tanimoto 類似度が最も低く、**最も構造的に多様な分子群を生成できている** ことが確認された。
  - **品質 (d)**: Top-100 分子の平均報酬においても最高スコアを維持しており、品質を一切犠牲にすることなく圧倒的な多様性を獲得した。
