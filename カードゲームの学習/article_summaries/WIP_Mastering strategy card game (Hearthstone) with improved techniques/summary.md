# Mastering strategy card game (Hearthstone) with improved techniques

## 背景
Hearthstone（ハースストーン）をはじめとする戦略カードゲーム（Strategy Card Game）は、不完全情報（部分観測可能）ならびにゼロサムゲームの性質を持ち、Artificial Intelligence (AI) の性能を評価する上で理想的なテストベンチである。これまでの研究において、Legend of Code and Magic (LoCM) などの比較的シンプルなゲームにおいては、End-to-End (E2E) の方策関数と Optimistic Smooth Fictitious Play (OSFP) を組み合わせた手法が有望な成果を上げていた。
しかし、Hearthstoneはヒーロー選択（Picking Hero, PH）、デッキ構築（Card Deck Building, CB）、そしてバトル（Battle, BT）という複数のステージを持つ非常に複雑な商業ゲームであり、状態空間や行動空間の規模も大きい。本研究では、過去の手法をこのより複雑なHearthstoneに適用し、環境の特性に合わせた複数の改善手法（Improved Techniques）を提案することで、トップクラスの人類プレイヤーを打ち破るマスターレベルのエージェントをゼロから学習させることを目的としている。

## 手法
本研究では深層強化学習（DRL）とメタアルゴリズムとして Optimistic Smooth Fictitious Play (OSFP) を用いてゼロからエージェントを学習させた。ベースとなったEnd-to-Endモデルは、以下のように段階ごとの方策関数を組み合わせる。

$$ \pi_\theta(\cdot|o) = \delta \pi_{\theta_{CB}}(\cdot|o) + (1 - \delta) \pi_{\theta_{BT}}(\cdot|o) $$

ここで $\delta$ はデッキ構築（CB）フェーズであれば1、バトル（BT）フェーズであれば0を返す指示関数とする。

Hearthstoneの複雑さに対応するため、以下の技術的な改善が行われた。

1. **PHフェーズのE2Eからの除外（Exclusion of PH）:**
ヒーロー選択をE2E方策関数に含めると、学習が1つのヒーローに偏ってしまい（局所解）、他のヒーローに対する対戦性能が低下することが判明した（[Figure 5](./images/ph.png) 参照）。これを回避するため、ヒーローは一様分布からランダムにサンプリングする形式を採用した（ベースライン: b0）。

2. **割引率 $\gamma$ の改善:**
方策の収束を早める $\gamma = 0.99$ では各エピソードの勝敗リターンを正確に反映できないため、報酬を正確に評価する $\gamma = 1.0$ を適用した（ベースライン: b1/b1.5）。

3. **Random-CBによる初期化:**
バトル方策の学習において多様な状況を探索させるため、デッキ構築の初めの $n$ 枚をランダムに選択させる Random-CB を導入し、より人間らしいデッキ（Flamewaker Mage構成など）の学習を促進させた（ベースライン: b1.5）。

4. **バランス調整によるOff-Policyの軽減（バッファ構造の改善）:**
非同期のActor-Learner構造において、データ生産が消費を上回りすぎる（遅延した）状態を防ぐため、リングバッファではなくキューバッファを導入し、Actor数を半減させてデータ効率と学習の安定性を高めた（ベースライン: b2）。

5. **V-Traceの改善（クリッピングと分散調整）:**
V-Traceでの学習収束を早めるため、重要度サンプリングの重み $\rho$ のクリッピング上限 $\Bar{\rho}$ などを調整し、極端に小さい $\rho$ がトレースを消失させないための下限クリッピングも導入した。価値関数の推定は以下の式で行われる。

$$ v_t = V_t + \sum_{i=0}^k \gamma^i [\prod_{j=0}^{i-1}\text{clip}(\rho_{t+j}, \ubar{c}, \Bar{c})] \text{clip}(\rho_{t+i}, \ubar{\rho}, \Bar{\rho}) \delta_{t+i} $$

さらに、方策勾配についてはPPOによるクリッピングを採用して安定化させた（ベースライン: b3）。

6. **ヒーローごとのモデル分離（Model Isolation by Hero）:**
プレイスタイルが明確に異なる3種のヒーローにそれぞれのモデルを独立させて割り当て、計算リソースを3倍に増やすことでモデルの表現力を最大化した（ベースライン: b4）。

7. **非対称なチート学習（Cheat）:**
不完全情報ゲームであるため、「相手のデッキの一部を覗き見できる」というチート情報を入力空間に含めて学習を行った。評価時に非対称にならないよう、学習データ生成時にのみ適用することで、敵対的戦略（メタ読み）の獲得を促進させた（ベースライン: c5）。

## 結果

本研究で行われたベースラインの勝率評価、および人間（トッププレイヤー）との検証結果は以下の表と図の通りである。

### マシン対マシン評価（勝率行列）

Table 1 は各改善を段階的に加えたモデル同士の勝率（交差対戦結果）を示している。

| (%) | b0 | b1.5 | b2 | b3 | b4 | c5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| b0 | 50.0 | 43.0 | 37.2 | 24.3 | 26.4 | 19.8 |
| b1.5 | 57.0 | 50.0 | 40.0 | 30.4 | 29.7 | 21.3 |
| b2 | 62.8 | 60.0 | 50.0 | 34.9 | 38.3 | 29.9 |
| b3 | 75.7 | 69.6 | 65.1 | 50.0 | 43.5 | 39.0 |
| b4 | 73.6 | 70.3 | 61.7 | 56.5 | 50.0 | 44.5 |
| c5 | 80.2 | 78.7 | 70.1 | 61.0 | 55.5 | 50.0 |

**考察:** 最初の強力なベースライン（b0: LoCMのコンペティション優勝モデルと同等）に対して、改良を加えるごとに明確に勝率が上昇している。特に、V-TraceとPPOを組み合わせた改良（b3）と、非対称なチート学習（c5）が大きな跳躍をもたらしており、c5モデルはb0に対して 80.2% の圧倒的勝率を記録した。

### マシン対人間（トッププレイヤー）の評価

中国サーバーで過去にトップ10（100万人規模）に入り込んだストリーマーを対象に、Best-of-5 (Bo5) の「Conquest」ルールでのトーナメントを実施した。

| | tournament 1 | tournament 2 |
| :--- | :--- | :--- |
| b4-23day-vs-human | 3:0 | 3:0 |
| c5-16day-vs-human | 3:1 | 3:2 |

**考察:** 通常モデル（b4-23day）およびチート学習モデル（c5-16day）ともに、人間のトッププレイヤーに対して全トーナメントで勝利を収めた（Table 2）。
特筆すべき点として、AIは専門的な事前知識・人間データを一切提供されずにゼロから学習したにもかかわらず、人間界の強力なメタデッキである「Flamewaker Mage」と酷似するデッキ（[Figure 7a](./images/deck-ai.png) および [Figure 7b](./images/deck-human.png) 参照）を自律的に構築する能力を獲得した。これにより、戦略カードゲームにおいて手法の汎用性と強力な自己対戦による環境探索（OSFP）の有効性が立証された。

### 実験パラメータ設定

ハイパーパラメータは以下のTable 3（DRLの設定）およびTable 4（OSFPの設定）となる。

**Table 3: Reinforcement learning hyperparameters.**
| Parameter | Value |
| :--- | :--- |
| Weight of policy gradient from PPO | 1.0 |
| Weight of policy gradient from UPGO | 1.0 |
| Weight of value function loss | 1.0 |
| Weight of entropy penalty | 0.01 |
| Learning rate | 7e-5 |
| Batch size | 1e+4 * 8gpu |
| Discount | 1.0 |
| LSTM states | 256 |
| Sample reuse | 2 |
| V-Trace $c$ clip | [0.001, 1.007] |
| V-Trace $\rho$ clip | [0.001, 1.007] |

**Table 4: OSFP hyperparameters.**
| Parameter | Value |
| :--- | :--- |
| Self-play Probability, $p$ | 0.6 |
| Add to historical model threshold, $\xi$ | 0.55 |
| Add to historical model max LP, $c$ | 6 |
| Num samples of each LP | 3.2e+8 |

### Observation/Action Space

状態空間（Table 5）および行動空間（Table 6）は人間が認識可能な情報を分解し、オートレグレッシブにアクション（選ぶ→ターゲット指定する）を生成するように設計されている。

**Table 5: Observation Space.**
| Observations | Descriptions |
| :--- | :--- |
| hero | my hero, one of (mage, hunter, warrior) |
| card set | all cards, including each hero's specific cards |
| card selected mask | 1 if the card has been selected else 0 |
| card can selected mask | 1 if the card can be selected else 0 |
| hero | my hero, one of (mage, hunter, warrior) |
| oppo hero | opponent's hero, one of (mage, hunter, warrior) |
| my deck | cards in my deck |
| decision type | one of (construct, select, minion battlecry, spell card, minion/hero attack, hero power, end turn) |
| my board | minions on my board and their scalar features |
| oppo board | minions on opponent's board and their scalar features |
| my hand | cards in my hand and their scalar features |
| my graveyard | cards in my graveyard and their scalar features |
| oppo graveyard | cards in opponent's graveyard and their scalar features |
| my player | my features, such as number of hands and minions, mana, weapon |
| oppo player | opponent's features, such as number of hands and minions, mana, weapon |
| BT action mask | 1 if the action can be done else 0 |

**Table 6: Action Space.**
| Action | Description |
| :--- | :--- |
| selected card | card that is selected into the deck, corresponding to *card set* in observation space |
| selected card | card that is selected as one of *(type, target)*, one step for *type* and one step for *target*, *type* $\in$ *{my hand card, my board card, opponent’s board card, my hero power card, end turn card}*, *target* $\in$ *{my hero, opponent's hero, my board card and opponent's board card}* |

### モデルのネットワーク構造
ネットワーク全体像（[Figure 4](./images/e2estructure-1.png), [Figure 4](./images/e2estructure-2.png) 参照）では、Observation入力に対してEmbedding（Hero・Card等）を行いLSTMステートとともに価値（Value）や方策（Policy）へと分解する構成を採用している。これによりフェーズをまたいだ柔軟な出力が可能となっている。また、実験では専用のWebインターフェース（[Figure 6](./images/ui-cb.png), [Figure 6](./images/ui-bt.png), [Figure 6](./images/ui-bt-anonymous.png)）を用いて実行検証がなされた。
