# Cardsformer: Grounding language to learn a generalizable policy in hearthstone

## 背景
強化学習（RL）は囲碁、将棋、ポーカーなど多くの伝統的ゲームで人間レベルのパフォーマンスを示してきた。近年ではより複雑な状態空間を持つStarCraft IIやDota 2のようなビデオゲームもテストベッドとして導入されている。しかし、これらの複雑な環境において事前知識なしでゼロから学習することは膨大な訓練時間を要し、さらに環境の動的ルール（ダイナミクス）が変化すると学習済みポリシーが容易に機能しなくなるという問題がある。
人間は、自然言語で記述されたルールなどの「事前知識」から環境の動的変化を推測・学習し、新しい環境にも適応（一般化）することができる。本論文ではこれに着想を得て、複雑な動的ルールと膨大なカードプールを持つ対戦型トレーディングカードゲーム「Hearthstone（ハースストーン）」をテストベッドとし、自然言語で記述されたカードの効果をモデルに理解（Language Grounding）させることで、未学習の新しいカードに対しても一般化可能なポリシーを学習する人工知能「Cardsformer」を提案している。

## 手法
Hearthstoneの環境は、言語条件付き部分観測マルコフ決定過程（LC-POMDP）として定式化される。
Cardsformerは従来のモンテカルロ木探索（MCTS）のようなリアルタイムの木シミュレーションに依存せず、以下の2つのニューラルネットワークモデルで構成される完全なEnd-to-Endシステムである。

1. **Prediction Model（予測モデル）**
   カードの能力などの自然言語による記述（MPNetによる文埋め込み）と現在の状態から、将来の状態遷移（対象となるミニオンやヒーローの属性変化など）を予測するモデル。
   学習は環境から収集されたオフライン軌跡を用いた教師あり学習で行われる。Hearthstoneのすべてを予測することは不可能なため、実際に変化があった値（$N_{a}$）のみに基づいたMSE（平均二乗誤差）のバリエーションで損失関数を次のように定義している。
   
   $$ L_{M}(\theta) = \mathbb{E} \left[ \frac{1}{N_{a}} \sum_{i} \left( M_{\theta}(s_{t}, a_{t})_{i} - c_{t+1, i} \right)^{2} \right] $$

2. **Policy Model（ポリシーモデル）**
   Prediction Modelによって予測された「将来の状態変化」を追加の入力として受け取り、それらに基づいて現在の状態・行動の価値（Q値）を推定するモデル。
   Prediction Modelの重みは固定した状態で、Deep Monte-Carlo (DMC) を用いたQ学習（自己対戦）により強化学習される。報酬は勝った場合に $+1$、負けた場合に $-1$ のみ与えられるスパース報酬を使用する。
   モデルの学習は以下の損失関数を最小化するように行われる。
   
   $$ L_{Q}(\theta) = \mathbb{E} \left[ \left( r_t + \gamma \max_{a'} Q_{\theta'}(s_{t+1}, a', M(s_{t+1}, a')) - Q_{\theta}(s_t, a_t, M(s_t, a_t)) \right)^{2} \right] $$

状態および行動の入力表現では、各ゲームエンティティ（手札、ミニオン等）の属性ベクトル $c_{i}$ に対して、そのカード効果等の自然言語記述の埋め込み $l_{i}$ が連結（Concatenation）され、行動はSourceフラグとTargetフラグによって定義される。

## 結果

### 1. 訓練済み・未訓練カードにおける勝率の比較（ベースラインに対する優位性）
Cardsformerは、訓練用のカード群だけでなく、未知の未訓練カード（Unseen cards）をデッキに複数混ぜたシナリオでの汎化テストにおいても、既存のMCTSベースエージェント（Dynamic Lookahead, Aggressive/Controlling Agent）を大幅に上回る性能や互角の性能を実証した。

| Unseen cards | 0 | 10 | 20 | 30 |
|---|---|---|---|---|
| Dynamic Lookahead | 78.0 ± 2.5 | 70.7 ± 2.2 | 64.0 ± 4.0 | 47.5 ± 2.6 |
| Aggressive Agent | 92.9 ± 1.6 | 98.4 ± 1.4 | 96.8 ± 1.4 | 97.4 ± 1.9 |
| Controlling Agent | 94.1 ± 2.2 | 89.6 ± 2.7 | 87.7 ± 3.0 | 89.7 ± 3.5 |

上記テーブルは、Cardsformerの各ベースラインに対する勝率（％）を示している。完全な未訓練カードのみで構成されたデッキ（Unseen cards 30）においても、SOTAであるDynamic Lookaheadに対して47.5%と善戦し、それ以外のAgentに対しては大勝している。これは、ゲーム内の直接的なカード効果の実装（シミュレーション）を持たなくても、言語モデルによって意味を推測・グラウンディングし、ゼロショットでの汎化能力を獲得していることを示している。

### 2. コンポーネントのアブレーションと学習効率の向上
Prediction Modelや、事前学習済み言語モデル（MPNet）による言語埋め込みの有無が、システム全体のパフォーマンスと学習速度にどのような影響を与えるかを調査している（Figure 3）。
言語埋め込みをCard IDのOne-Hotエンコーディングに置き換えたモデル（One-Hot Policy）と、Prediction Modelを取り除いたモデル（Language Only Cardsformer）、そして完全なCardsformerの学習曲線を比較した結果、Cardsformerが圧倒的に早い段階（約2,000万フレーム）で他モデルの最終性能（1億フレーム）に到達し、さらに高い勝率キャップに到達することが証明された。自然言語からの動的状態変化の予測が、強化学習の探索と学習効率に極めて大きく寄与している。

### 3. シャプレー値（Shapley values）による判断の解釈
Policy ModelがQ値を算出する際に、どの入力フィーチャを重要視しているかをSHAPを用いて分析している（Figure 5）。
モデルは、圧倒的にPrediction Modelが予測する「対戦相手のヒーローのヘルス予測（No.1）」と「自身のヒーローのヘルス予測（No.5）」などの将来の状態予測に大きく依存して現在の行動を評価・決定していることがわかった。これにより、予測モデルの出力が正しく方針決定に寄与（Grounding）していることが裏付けられた。

### 参照図版
![Figure 1: Two sample cards, a snapshot of the game board, and a list of game entities in Hearthstone.](./images/paper.pdf-0002-02.png)
![Figure 2 (a) and (b): Architecture of Cardsformer](./images/paper.pdf-0004-02.png)
![Figure 2 (c): Model details for the Prediction Model and the Policy Model](./images/paper.pdf-0004-03.png)
![Figure 3: The comparison of ablation models throughout the training process](./images/paper.pdf-0006-04.png)
![Figure 4: Ablation study on language embedding methods](./images/paper.pdf-0007-02.png)
![Figure 5: Shapley values of five most decisive input features](./images/paper.pdf-0007-09.png)
