# Reinforcement Learning for Slate-based Recommender Systems: A Tractable Decomposition and Practical Methodology (SlateQ)

論文の背景, 手法, 結果の3項目でまとめます。

---

## 背景

YouTube、Netflix、Spotify などの大規模コンテンツ推薦システムでは、ユーザーに対して複数アイテムのリスト（スレート / Slate）を提示します。従来の商用推薦システムの多くは、個々の推薦候補に対する**直近の即時クリック率（pCTR）や短期的エンゲージメント（近視眼的 / Myopic な目的関数）**を最大化するように最適化されています。

しかし、近視眼的な推薦には以下の深刻な問題があります：
1. **短期的なクリックスルーへの過剰適合**: ユーザーの関心を長期的に維持・開拓する探索（Exploration）や多様なコンテンツの提供が阻害され、長期的な満足度やエンゲージメント（Long-Term Value: LTV）が低下する。
2. **強化学習（RL）適用の組み合わせ爆発**:
   - スレート全体の行動空間はアイテムプール $|\mathcal{I}|$、スレート長 $k$ に対して $\binom{|\mathcal{I}|}{k} k!$（数千万〜数十億通り）に達します。
   - 従来型の Q-learning や SARSA をそのまま適用すると、すべてのスレートの Q値を探索・汎化・最適化（最大化）することは計算量的に完全に不可能です。
3. **本番推薦インフラへの統合の困難さ**:
   - 何億人ものユーザーに対してミリ秒単位のリアルタイム推論を行う大規模システムでは、複雑な RL 方策をゼロから導入することは運用上極めて困難でした。

本論文（Google Research / YouTube）は、ユーザーの選択モデル（Plackett–Luce や Multinomial Logit）の自然な性質を利用して、**スレート全体の長期価値（Q値）を「構成アイテム単体の長期価値」の線形和として分解**する新しい強化学習手法 **SlateQ** を提案しました。これにより、既存の近視眼的ディープニューラルネット推薦インフラをほぼそのまま活用しながら、長期エンゲージメントを最大化するスレート強化学習を YouTube 本番環境で実現しました。

---

## 手法

### 1. マルコフ決定過程（MDP）と2つの自然な仮定

推薦システムを MDP $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$ として定式化します。
- **状態 $s \in \mathcal{S}$**: ユーザーの過去履歴・関心・属性などの潜在状態。
- **行動 $A \in \mathcal{A}$**: $k$ 個のアイテムからなる推薦スレート $A = (a_{1}, \dots, a_{k})$。
- **スレート Q値**: $Q^{\pi}(s, A) = R(s, A) + \gamma \sum_{s'} P(s' \mid s, A) V^{\pi}(s')$

SlateQ では、多くの推薦システムで自然に成立する以下の2つの仮定を置きます：
1. **単一選択仮定 (Single Choice: SC)**: ユーザーは提示されたスレート $A$ の中から高々1つのアイテム $i \in A$ を選択・消費する（何も選択しないヌル選択 $\bot$ を含む）。
2. **選択依存の報酬・状態遷移仮定 (Reward/Transition Dependence on Selection: RTDS)**: 実現する即時報酬 $R(s, i)$ およびユーザーの次状態への遷移確率 $P(s' \mid s, i)$ は、**ユーザーが実際に選択・消費したアイテム $i$ のみに依存**し、スレート内に存在したが選択されなかった他のアイテムには依存しない。

### 2. SlateQ の価値関数分解定理（Slate Decomposition）

アイテム $i$ がクリック（消費）された条件付きでの長期価値を表す**アイテム単位の補助 Q関数** $\bar{Q}^{\pi}(s, i)$ を定義します：

$$ \bar{Q}^{\pi}(s, i) = R(s, i) + \gamma \sum_{s' \in \mathcal{S}} P(s' \mid s, i) V^{\pi}(s') $$

このとき、スレート全体の Q値 $Q^{\pi}(s, A)$ は、ユーザー選択モデル $P(i \mid s, A)$（Plackett–Luce / Multinomial Logit）を用いた**アイテム単位 Q値の期待値として完全に分解**されます：

$$ Q^{\pi}(s, A) = \sum_{i \in A} P(i \mid s, A) \bar{Q}^{\pi}(s, i) $$

### 3. TD学習（SARSA / Q-learning）の更新則

この分解により、スレート単位ではなく**アイテム単体の Q関数 $\bar{Q}(s, i)$ のみを学習**すればよくなります。
状態 $s$ でスレート $A$ を提示し、アイテム $i$ がクリックされて即時報酬 $r$ を得て次状態 $s'$ に遷移し、次スレート $A'$ が選ばれたとき、SARSA 更新は以下のように実行されます：

$$ \bar{Q}^{\pi}(s, i) \leftarrow (1 - \alpha) \bar{Q}^{\pi}(s, i) + \alpha \left( r + \gamma \sum_{j \in A'} P(j \mid s', A') \bar{Q}^{\pi}(s', j) \right) $$

### 4. リアルタイム・スレート最適化（Slate Optimization）

方策の実行時（Serving 時）には、スレート Q値を最大化するスレート $A^{*} = \arg\max_{A} \sum_{i \in A} P(i \mid s, A) \bar{Q}(s, i)$ を見つける必要があります。
- **選択モデルが Multinomial Proportional (MNP) / MNL の場合**:
  $P(i \mid s, A) = \frac{v(s, i)}{\sum_{j \in A \cup \{\bot\}} v(s, j)}$ のとき、この問題は分数計画問題（Fractional Programming）となり、Charnes–Cooper 変換によって厳密な線形計画問題（LP）として多項式時間で解くことができます。
- **Top-$k$ 近似（実務的ヒューリスティック）**:
  各アイテムのスコア $v(s, i) \bar{Q}(s, i)$ の上位 $k$ 件を選択して配置する手法。実環境では極めて高速（数ミリ秒）に動作し、厳密解と遜色ない性能を発揮します。

### 5. 実本番インフラへの統合アーキテクチャ（マルチタスク DNN）

既存の近視眼的ディープニューラルネット（DNN）の構造を再利用し、即時クリック確率 $v(s, i) = \text{pCTR}(s, i)$ を予測するヘッドと並列に、長期価値 $\bar{Q}(s, i)$ を予測する LTV ヘッドを追加したマルチタスクネットワークを構築します。

![System Overview](./images/system_overview.png)
![Network Architecture](./images/network.png)

---

## 結果

### 1. シミュレーション環境（RecSim）での検証

ユーザーの潜在的な興味の飽和・疲弊（User Saturation / Dynamics）を含む推薦シミュレータ **RecSim** において、近視眼的モデル（Myopic）と SlateQ（SARSA-TS, Q-learning）の累積長期エンゲージメントを比較しました。

| 低品質アイテム混入環境 | 高品質アイテム混入環境 | LTV vs. Myopic 比較 |
| :---: | :---: | :---: |
| ![Low Quality Learning](./images/low_quality_learning_curve.png) | ![High Quality Learning](./images/high_quality_learning_curve.png) | ![LTV vs Myopic](./images/LTVvsMyopic1.png) |

- **考察**:
  - 近視眼的モデル（Myopic）は、短期的にはクリック率が高いもののユーザーの興味を急速に疲弊させる「クリックベイト」アイテムを過剰推薦し、長期的な累積リワードが頭打ちになります。
  - 一方、**SlateQ** は将来の状態遷移を考慮し、ユーザーの興味を持続・拡大させる多様で質の高いコンテンツをバランスよく推薦するため、大幅に高い累積長期エンゲージメント（LTV）を達成しました。

---

### 2. YouTube 実トラフィックでの本番 A/B テスト結果

世界最大規模の動画推薦プラットフォーム **YouTube ホーム画面** において、数十億人のユーザーを対象に3週間のライブ実験を実施しました（コントロール群は高度にチューニングされた本番近視眼的DNNモデル、トリートメント群は SlateQ SARSA-TS モデル）。

| 総エンゲージメント時間（TWT）の向上率 | スレート内順位ごとのエンゲージメント変化 |
| :---: | :---: |
| ![TWT Stats](./images/twt_stats.png) | ![Engagement by Position](./images/engagement_by_position.png) |

- **考察**:
  - **有意な総視聴時間（Total Watch Time: TWT）の増加**: SlateQ は既存の本番 baseline に対して、全実験期間にわたり統計的に有意（95%信頼区間内）な総エンゲージメント時間の向上を達成しました。
  - **順位別エンゲージメントの最適化**: スレート内の上位順位（Position 1〜3）において、長期価値の高い魅力的なコンテンツがより効率的に消費されていることが確認されました。

---

### 3. 筆者の考察と総括
1. **スレート推薦 RL の実用化マイルストーン**: 組み合わせ爆発により理論的研究に留まっていたスレート強化学習を、選択モデルに基づく価値分解（SlateQ）とマルチタスクDNNアーキテクチャによって、世界最大規模の推薦基盤で動作する実用技術へと昇華させました。
2. **多様性と長期的最適化の統合**: 短期クリックの最大化から「ユーザー状態の健全な遷移（長期エンゲージメント）」へのパラダイムシフトを可能にし、推薦の出力多様性や探索的推薦を長期価値の観点から正当化・最適化する基盤を確立しました。
