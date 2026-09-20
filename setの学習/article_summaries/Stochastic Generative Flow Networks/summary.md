# Stochastic Generative Flow Networks
（原題: Stochastic Generative Flow Networks）

**arXiv:** [2302.09465](https://arxiv.org/abs/2302.09465)  
**カンファレンス:** UAI 2023 (Proceedings of the 39th Conference on Uncertainty in Artificial Intelligence)  
**著者:** Ling Pan$^{1,2 *}$, Dinghuai Zhang$^{1,2 *}$, Moksh Jain$^{1,2}$, Longbo Huang$^3$, Yoshua Bengio$^{1,2,4}$ ($^*$Equal contribution)  
（$^1$Mila - Québec AI Institute, $^2$Université de Montréal, $^3$Tsinghua University, $^4$CIFAR AI Chair）  
**発表:** 2023年2月（UAI 2023採択）  
**対象タスク:** 確率的遷移環境における生成モデリング、創薬・材料設計、生物学的配列生成（DNA/ペプチド生成）、確率的ダイナミクスを持つ有向非巡回グラフ（DAG）上のサンプリング、生成的フローネットワーク（GFlowNet）

---
## 一言メモ  
GFlowNetは「高報酬のものを探索する」ための生成モデルだが、各行動の際に自由に選択を選べない（確率的に選択が変更されてしまうなど）の場合に弱かった。  
これのような場合にも適用できるようなモデル。

## 背景

Generative Flow Networks（GFlowNet）は、目的関数（エネルギー地形や報酬関数 $R(x)$）に比例した確率 $P(x) \propto R(x)$ で、高報酬かつ構造的に多様な候補群を非反復的（1パス）に直接サンプリングできる革新的な確率的生成モデルとして、分子設計や生物学的配列生成などの分野で脚光を浴びてきた。

しかし、従来のすべての GFlowNet 研究（Bengio et al., 2021; Malkin et al., 2022 等）には、**「環境の遷移ダイナミクスが完全に決定論的（Deterministic）である」という決定的な制約** が存在していた：

1. **決定論的遷移の仮定とその破綻**:
   - 従来の定式化では、状態 $s_t$ でアクション $a_t$ を選択すると、次の状態 $s_{t+1} = T(s_t, a_t)$ が 100% 確実に一意に決定されることを前提としていた。
   - しかし、現実世界の多くのタスクには **環境側の確率的ノイズ（Stochastic Transition Dynamics）** が不可避に存在する。例えば、オリゴプールを用いたタンパク質合成では意図しない配列変異が生じたり、化合物の化学反応では確率的な副反応が発生したり、ロボットの移動ではスリップや外乱が生じる。
2. **確率的環境における従来 GFlowNet の数学的崩壊**:
   - 確率的遷移が存在する環境に従来の GFlowNet（Detailed Balance や Trajectory Balance）をそのまま適用すると、環境の遷移確率の偏りに引きずられ、**「報酬 $R(x)$ に比例した確率でサンプリングする」という基本定理が数学的に破綻** してしまう。

![An example illustrating the failure of existing GFlowNet approaches](./images/example.png)
*(Figure 1: 従来の GFlowNet が確率的環境で失敗する具体例。(左) 四角は状態、丸はアクション、実線矢印はポリシー決定、点線矢印は環境の確率的遷移（点線上の数値は遷移確率、青い四角下の数値は報酬）。(右) 理想解では報酬比率 $1:2$ に応じて $P(s_1)=\frac{1}{3}, P(s_2)=\frac{2}{3}$ となるべきだが、従来の GFlowNet は $P(s_1)=\frac{5}{12}, P(s_2)=\frac{7}{12}$ となり、報酬に比例したサンプリングに失敗する)*

これに対し著者らは、強化学習の「事後状態（Afterstate）」の概念に着想を得て、**エージェントの意思決定ステップと環境の確率的遷移ステップを明確に分離（アイソレーション）し、環境ダイナミクスモデルを学習することで、確率的環境下でも厳密に $P(x) \propto R(x)$ を達成する「Stochastic GFlowNets」** を世界で初めて提案した。

---

## 手法

### 0. 手法の全体像（Input / Output / 最適化の目的）

Stochastic GFlowNet を機械学習モデルとして簡潔に整理すると、以下の設計となっている：

- **Input（入力）**:
  - **現在の環境状態 $s_t$**（偶数状態 Even State）
- **Output（出力）**:
  - **前向き方策 $\pi(a_t \mid s_t)$**: 次に取るべきアクション $a_t$ の選択確率分布
  - **状態フロー予測 $F(s_t) > 0$**: 状態 $s_t$ を通過する総水量の予測値
  - **ダイナミクスモデル $\hat{P}(s_{t+1} \mid s_t, a_t)$**: 中間状態 $(s_t, a_t)$ から各次状態 $s_{t+1}$ へ遷移する確率予測
- **何を最小化して学習するか？（2つの損失関数）**:
  1. **モデル損失 $\mathcal{L}_{\mathrm{model}}$**: 環境の真の遷移確率 $P$ を模倣するための最尤推定損失（負の対数尤度）。
  2. **確率的詳細釣り合い損失 $\mathcal{L}_{\mathrm{StochGFN-DB}}$**: エージェントの意思決定と環境の確率遷移の双方を組み込んだ、**「確率的フロー保存則」の二乗誤差**。
- **推論時（生成時）の流れ**:
  1. 初期状態 $s_0$ から開始。
  2. 学習済みポリシー $\pi(a \mid s)$ に従ってアクションを選択 $\to$ 中間状態 $(s, a)$ へ遷移。
  3. 環境（またはシミュレータ）の確率的遷移によって次状態 $s'$ へ着地。
  4. 終端状態に達するまで繰り返し $\to$ **環境にランダムな揺らぎが存在しても、最終的に得られる候補群は正確に報酬 $R(x)$ に比例した確率で生成される！**

---

### 1. 状態遷移の2段階分解（Afterstate / Odd State の導入）

従来の GFlowNet では $s_t \xrightarrow{a_t} s_{t+1}$ を単一のステップと見なしていたが、Stochastic GFlowNet ではこれを **2段階のステップ** に分解する：

![Decomposition of transitions](./images/method.png)
*(Figure 2: 従来の GFlowNet 遷移（上）を 2段階に分解する構造（下）。(a) ポリシーによるアクション選択（決定論的中間状態 Odd State への遷移）、(b) 環境ダイナミクスによる確率的次状態（Even State）への遷移)*

1. **第1段階：エージェントの意思決定ステップ（Even $\to$ Odd）**:
   - 状態 $s_t$（偶数状態: Even State）において、エージェントはポリシー $\pi(a_t \mid s_t)$ に従ってアクション $a_t$ を選択する。
   - これにより、仮想的な中間状態 **$(s_t, a_t)$（奇数状態: Odd State / Afterstate）** へと **決定論的** に遷移する。
   - このステップの詳細釣り合い条件（後ろ向き確率は $1$）は：
     $$ F(s_t) \pi(a_t \mid s_t) = F((s_t, a_t)) $$
2. **第2段階：環境の確率的遷移ステップ（Odd $\to$ Even）**:
   - 中間状態 $(s_t, a_t)$ から、環境ダイナミクス $P(s_{t+1} \mid s_t, a_t)$ に従って、次の偶数状態 $s_{t+1}$ へと **確率的** に分岐・遷移する。
   - このステップの詳細釣り合い条件は：
     $$ F((s_t, a_t)) P(s_{t+1} \mid (s_t, a_t)) = F(s_{t+1}) \pi_B((s_t, a_t) \mid s_{t+1}) $$

この2段階分解により、**「エージェントの自由意志による選択」と「環境に起因する制御不能なランダム性」を数学的に完全に分離（アイソレーション）** することができる。

#### 💡 従来モデルとのアーキテクチャ・出力の決定的な差分

従来の GFlowNet と比較したとき、ネットワーク構成の最大のポイントは **「環境ダイナミクスモデル $\hat{P}$ が別個のネットワークとして新たに追加された2台体制」** にある：

```
【従来の GFlowNet（決定論的環境）】
  現在の状態 s ────( P_F : 自分の行動選択と環境遷移が一体化 )────> 次の状態 s'

【Stochastic GFlowNet（確率的環境）】
  現在の状態 s_t ──( ① エージェント方策 π )──> 中間状態 (s_t, a_t) ──( ② 環境ダイナミクス P̂ )──> 次の状態 s_{t+1}
```

| 構成要素 | 従来の GFlowNet | Stochastic GFlowNet |
| :--- | :--- | :--- |
| **遷移の扱い** | 行動選択と環境遷移が 1対1（同一視） | **エージェントの選択（$\pi$）** と **環境の気まぐれ（$P$）** を2段階に分離 |
| **エージェント側モデル** | 前向き方策 $P_F(s' \mid s)$、フロー $F(s)$ | **行動方策 $\pi(a \mid s)$**、フロー $F(s)$（従来と同等） |
| **★追加されたモデル** | なし（環境遷移は 100% 確定） | **【新規追加】環境ダイナミクスモデル $\hat{P}(s' \mid s, a)$** |

#### なぜダイナミクスモデル $\hat{P}$ を追加する必要があるのか？
「環境がサイコロを振るなら、AIがわざわざそれを予測しなくても、実環境に任せればいいのでは？」と思われるかもしれない。  
しかし、後述のフロー保存則（Stochastic DB 損失）を計算するためには：
$$ \text{流入量} = F(s_t) \cdot \pi(a_t \mid s_t) \cdot \mathbf{\hat{P}(s_{t+1} \mid s_t, a_t)} $$
という式の中に、**「環境がそのマスへ遷移させる確率の具体的な数値（$\hat{P}$）」を直接代入しなければ、損失関数を計算・逆伝播できない**。  
現実の自然界や実験室は遷移確率の数式を教えてくれないため、**過去の遷移ログから環境の気まぐれを学習・予測する専用のAI（ダイナミクスモデル $\hat{P}$）が不可欠** となる。

---

### 2. 確率的詳細釣り合い条件（Stochastic Detailed Balance: StochGFN-DB）

上記 2つのステップの保存則を結合すると、**確率的環境における新しい詳細釣り合い条件（Stochastic DB Constraint）** が導出される：

$$ F(s_t) \pi(a_t \mid s_t) P(s_{t+1} \mid (s_t, a_t)) = F(s_{t+1}) \pi_B((s_t, a_t) \mid s_{t+1}) $$

#### 学習のための損失関数
実務上は、両辺の対数をとり、その二乗誤差を **確率的詳細釣り合い損失（StochGFN-DB Loss）** として最小化する：

$$ \mathcal{L}_{\mathrm{StochGFN-DB}}(s_t, a_t, s_{t+1}) = \left( \log F(s_t) + \log \pi(a_t \mid s_t) + \log \hat{P}(s_{t+1} \mid s_t, a_t) - \log F(s_{t+1}) - \log \pi_B((s_t, a_t) \mid s_{t+1}) \right)^2 $$

ここで、終端状態 $x$ においては $F(x) = R(x)$ に固定する。

---

### 3. 環境ダイナミクスモデル $\hat{P}$ の学習

環境の真の遷移確率 $P(s' \mid s, a)$ は一般に未知であるため、ニューラルネットワークでパラメータ化されたダイナミクスモデル $\hat{P}_\phi$ を同時に学習する。

リプレイバッファ $\mathcal{B}$ に保存された遷移履歴 $(s, a, s')$ を用い、最尤推定（負の対数尤度の最小化）によりモデルを学習する：

$$ \mathcal{L}_{\mathrm{model}}(s, a, s') = - \log \hat{P}_\phi(s' \mid s, a) $$

出力層は、取り得る次状態候補に対する Softmax 分布として表現される。

---

### 4. Trajectory Balance（TB）への適用とその課題

本手法の枠組みは、遷移単位の DB だけでなく、軌跡全体を扱う **Trajectory Balance（TB）** にもテレスコーピング計算によって拡張できる：

$$ Z \prod_{t=0}^{n-1} \pi(a_t \mid s_t) P(s_{t+1} \mid (s_t, a_t)) = R(x) \prod_{t=0}^{n-1} \pi_B((s_t, a_t) \mid s_{t+1}) $$

対応する損失関数：
$$ \mathcal{L}_{\mathrm{StochGFN-TB}} = \left( \log Z + \sum_{t=0}^{n-1} \left[ \log \pi(a_t \mid s_t) + \log \hat{P}(s_{t+1} \mid s_t, a_t) \right] - \log R(x) - \sum_{t=0}^{n-1} \log \pi_B((s_t, a_t) \mid s_{t+1}) \right)^2 $$

- **理論的・実験的な洞察**:
  - TB は決定論的環境であっても軌跡全体の積を扱うため勾配の分散が大きいことが知られているが、**環境の確率的ノイズが加わるとその分散がさらに致命的に増大する**。
  - そのため、後述の実験でも確認されるように、確率的環境においては **局所的な遷移を1歩ずつ制約する Stochastic DB の方が、Stochastic TB よりも圧倒的に安定して優れた性能を発揮** する。

---

### 5. アルゴリズム全体の学習サイクル

![Illustration of Stochastic GFlowNets](./images/algorithm.png)
*(Figure 3: Stochastic GFlowNets のシステム全体構成。エージェントポリシー $\pi$、ダイナミクスモデル $\hat{P}$、リプレイバッファ $\mathcal{B}$ の相互作用)*

1. 現在のポリシー $\pi$ を用いて環境内で $M$ 本の軌跡 $\tau = (s_0 \to \dots \to s_n)$ をサンプリングし、リプレイバッファ $\mathcal{B}$ に格納。
2. 収集した軌跡データを用いて、$\mathcal{L}_{\mathrm{StochGFN-DB}}$ により GFlowNet パラメータ（ポリシー $\pi$, $\pi_B$, フロー $F$）を更新。
3. バッファ $\mathcal{B}$ からバッチを抽出し、$\mathcal{L}_{\mathrm{model}}$ により環境ダイナミクスモデル $\hat{P}$ を更新。

---

## 結果

著者らは、合成ベンチマーク（GridWorld、Bit Sequences）から、実世界の大規模な生物学的配列設計（TF Bind 8、抗菌ペプチド生成 AMP）に至るまで、確率的遷移ノイズを注入した多様なタスクで包括的な比較実験を行った。

---

### 1. GridWorld 実験

$H \times H$ のグリッド上を移動し、4隅の角（Modes）に配置された高報酬を目指すナビゲーションタスク。エージェントが選んだ行動に対して、確率 $1-\alpha$ で指定方向に進み、確率 $\alpha$ でランダムな隣接領域にスリップする確率的ダイナミクスを導入。

![GridWorld Environment](./images/grid_env.png)
*(Figure 4: GridWorld 環境の報酬構造。4隅の濃い青いマスで報酬が最大となる)*

#### ① マップサイズ拡大に伴う性能比較（$\alpha = 0.25$）

![GridWorld L1 Error](./images/small_grid_stick_0.25.png)
![GridWorld L1 Error](./images/medium_grid_stick_0.25.png)
![GridWorld L1 Error](./images/large_grid_stick_0.25.png)
*(Figure 5: マップサイズ拡大（Small, Medium, Large）に伴う経験的 $L_1$ 誤差の推移)*

![GridWorld Modes](./images/small_grid_stick_0.25_modes.png)
![GridWorld Modes](./images/medium_grid_stick_0.25_modes.png)
![GridWorld Modes](./images/large_grid_stick_0.25_modes.png)
*(Figure 6: マップサイズ拡大に伴い学習中に発見されたモード数の推移)*

- **考察**:
  - MCMC は探索が停滞し、PPO は早期に単一モードへ収束して崩壊した。
  - 従来の GFN（DB および TB）は、確率的環境下では収束保証が破綻するため、マップが大きくなると $L_1$ 誤差が悪化し、4つのモードすべてを発見できなくなった。特に TB は勾配分散の爆発により性能低下が顕著であった。
  - **Stochastic GFlowNet（Stoch-GFN）は、全マップサイズにおいて最速で最低の $L_1$ 誤差に収束し、すべてのモードを完璧に捕捉し続けた**。

#### ② ノイズ強度 $\alpha$ の変化に対する頑健性（Small GridWorld）

![GridWorld Varying Alpha](./images/small_grid_0.5.png)
![GridWorld Varying Alpha](./images/small_grid_0.9.png)
*(Figure 7: ノイズレベル増加（$\alpha = 0.5, 0.9$）における各手法の $L_1$ 誤差比較)*

- **考察**:
  - スリップ確率が $\alpha = 0.9$（行動の9割がランダムに乱される極限環境）に達しても、Stochastic GFlowNet は安定して低誤差を維持し、極めて高いノイズ耐性を実証した。

#### ③ Stochastic TB の検証

![Stochastic TB](./images/tb_stick_0.25_small.png)
![Stochastic TB](./images/tb_stick_0.25_large.png)
![Stochastic TB](./images/tb_stick_0.9_small.png)
*(Figure 8: Trajectory Balance（TB）をベースとした Stochastic GFlowNet の評価。(a) Small, $\alpha=0.25$, (b) Large, $\alpha=0.25$, (c) Small, $\alpha=0.9$)*

- **考察**:
  - Stochastic TB は従来の TB を大幅に改善したものの、大規模環境や高ノイズ下では Stochastic DB に及ばなかった。これは確率的環境における軌跡全体の積に伴う分散増大が原因である。

---

### 2. ビット列生成（Bit Sequence Generation）

長さ $n=120$ のビット列を、$k$ ビットずつ（$k=2, 4$）逐次追加して生成するタスク。所定の目標集合 $M$ との編集距離に基づく報酬関数が設定され、ノイズレベル $\alpha = 0.1, 0.3, 0.5$ の下で評価。

![Bit Sequence Results](./images/nbits_4_stick_0.1.png)
![Bit Sequence Results](./images/nbits_4_stick_0.3.png)
![Bit Sequence Results](./images/nbits_4_stick_0.5.png)
![Bit Sequence Results](./images/nbits_2_stick_0.1.png)
![Bit Sequence Results](./images/nbits_2_stick_0.3.png)
![Bit Sequence Results](./images/nbits_2_stick_0.5.png)
*(Figure 9: ビット列生成タスクにおける発見モード数推移。上段: $k=4$（軌跡長30）、下段: $k=2$（軌跡長60）。左から順に $\alpha = 0.1, 0.3, 0.5$)*

- **考察**:
  - ステップ数が長く探索空間が広大になる $k=2$ において、従来の GFN はほとんど学習が進まずモードを発見できなかった。
  - A2C や SAC、MCMC も探索の停滞に苦しむ中、**Stoch-GFN は軌跡が長くなっても高ノイズ下であっても圧倒的に多くのモードを高速かつ網羅的に発見** した。

---

### 3. 転写因子結合DNA配列生成（TF Bind 8）

特定のヒト転写因子に対する結合親和性が高い 8塩基対の DNA 配列を自己回帰的に生成する生物学的配列設計タスク。

![TF Bind 8 Results](./images/tfbind8_modes.png)
![TF Bind 8 Results](./images/tfbind8_reward.png)
![TF Bind 8 Results](./images/tfbind8_reward_median.png)
*(Figure 10: TF Bind 8 生成タスクの結果。(a) 発見モード数、(b) Top-100 平均報酬、(c) Top-100 中央値スコア)*

- **考察**:
  - Stoch-GFN は、従来の GFN や SAC、A2C、MCMC と比較して **圧倒的に多数の高結合親和性モードを発見** した。
  - また、生成された上位 100 配列の平均報酬および中央値スコアにおいても最高値を記録し、生物配列設計の実世界設定における実用性を証明した。

---

### 4. 抗菌ペプチド生成（Antimicrobial Peptide Generation: AMP）

20種類のアミノ酸から構成される最大長 60 のペプチド配列を設計し、抗菌活性（DBAASP データベースに基づく事前学習済み活性予測器）を最大化・多様化する極めて高次元な実課題（状態空間サイズ $21^{60}$）。確率的ノイズ $\alpha = 0.1$ を導入。

#### Table 1: Better results with Stoch-GFN on the AMP generation task. Larger is better.
| Method | Top-100 reward | Number of modes |
| :--- | :---: | :---: |
| MCMC | 0.632 $\pm$ 0.035 | 3.67 $\pm$ 0.58 |
| A2C | 0.682 $\pm$ 0.032 | 2.66 $\pm$ 0.58 |
| SAC | 0.754 $\pm$ 0.047 | 4.33 $\pm$ 1.33 |
| GFN | 0.748 $\pm$ 0.048 | 3.0 $\pm$ 3.0 |
| **Stoch-GFN (Ours)** | **0.834 $\pm$ 0.023** | **19.5 $\pm$ 2.5** |

- **考察**:
  - 通常の GFN は確率的ノイズ環境下で性能が制限され、発見モード数はわずか $3.0$ 個にとどまった。
  - これに対し **Stoch-GFN は Top-100 報酬で 0.834 を達成し、発見モード数は従来の 6倍以上となる 19.5 個へと劇的に向上** した。実用的な分子創薬・タンパク質工学タスクにおいて、確率的揺らぎに頑健で多様な候補生成が可能であることを決定づけた。
