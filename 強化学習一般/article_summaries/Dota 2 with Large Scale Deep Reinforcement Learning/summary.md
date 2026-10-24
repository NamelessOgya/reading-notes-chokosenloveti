# Dota 2 with Large Scale Deep Reinforcement Learning (OpenAI Five)

- 著者: Christopher Berner, Greg Brockman, Brooke Chan, Vicki Cheung, Przemysław Dębiak, Christy Dennison, David Farhi, Quirin Fischer, Shariq Hashme, Chris Hesse, Rafal Józefowicz, Scott Gray, Catherine Olsson, Jakub Pachocki, Michael Petrov, Henrique Pondé de Oliveira Pinto, Jonathan Raiman, Tim Salimans, Jeremy Schlatter, Jonas Schneider, Szymon Sidor, Ilya Sutskever, Jie Tang, Filip Wolski, Susan Zhang（OpenAI）
- 発表: arXiv: 1912.06680 (2019)
- 原文: [ref_article.md](./ref_article.md)

## 背景

- リアルタイム5対5マルチプレイヤー・オンライン・バトルアリーナ（MOBA）ゲーム『Dota 2』は、リアルタイム戦略性、超長期ホライズン、部分観測（戦場の霧）、巨大な連続・離散ハイブリッド行動空間、および高度なチーム協調が要求される難関ベンチマークである。
- 特徴と課題：
  - **超長期の計画ホライズン**: 1試合約45分、フレームスキップ（4フレーム＝1ステップ）後でも約2万〜4万5000タイムステップに及ぶ。
  - **序盤の内政・レーン戦の決定性**: 序盤数分間の「レーン戦（Laning Phase）」におけるラストヒット・ディナイ・経験値（XP）とゴールドの蓄積が、中盤以降のアイテム・レベル差を生み、最終的な本拠地（Ancient）破壊の勝敗に直結する。序盤のミスやカード・スキルの無駄打ちは致命的なビハインドを生む。
  - **巨大な観測・行動空間**: 毎ステップ約170のユニット情報、約2万種類の離散・連続行動パラメータ。
- OpenAI は、人間の事前知識やMCTSによる木探索を用いず、**純粋な大規模深層強化学習（PPO）** とセルフプレイによって世界チャンピオンチーム「OG」を 2-0 で撃破する超人的AI **OpenAI Five** を実現した。

## 手法

### 1. 超大規模分散強化学習システム（Distributed PPO）

- アルゴリズムにはクリッピング付き **PPO (Proximal Policy Optimization)** を採用。
- コンピュート規模：最大 1,536 基の GPU（オプティマイザ）と 172,800 基の CPU コア（環境ロールアウト）。1日あたり約180年〜900年分のゲームプレイデータを収集。
- **一般化アドバンテージ推定（GAE）**: ホライズン $\tau = 180 \sim 360$ 秒（1ゲーム全体ではなく数分間の時間窓）でブートストラップし、割引率 $\gamma \approx 0.998$ を用いて分散を低減。

### 2. チームスピリット（Team Spirit）と局所・大域報酬の移行

5人のヒーローエージェントは独立したポリシーを持ちつつ、チーム全体の報酬と個人の報酬を **チームスピリット係数 $\tau \in [0, 1]$** で線形補間する：

$$r_t^i = (1 - \tau) r_{\mathrm{solo}, t}^i + \tau r_{\mathrm{team}, t}$$

- **学習初期（$\tau = 0.3$）**: 個人のラストヒット、ゴールド獲得、キル、生存（Solo reward）に大きな重みを置き、エージェントが「ゲームの基本操作・序盤の稼ぎ方」を素早く獲得させる。
- **学習後期（$\tau \to 1.0$ または $0.8$）**: チーム全体の勝利・タワー破壊・本拠地撃破（Team reward）へ重みをシフトさせ、自己犠牲やサポート、集団戦の連携行動を創発させる。

### 3. 報酬シェイピング（Dense Reward Shaping）

最終的な勝敗（Win: +5）のみでは序盤の探索が成立しないため、緻密なドメイン知識に基づく密な報酬を付与：
- 敵・味方・建造物のHP変動、ゴールド・XP獲得、ラストヒット、ディナイ、レーン配分（Lane Assignment ペナルティ）など。
- 学習の進行とともに勝敗の累積値が支配的になるようスケールを設計（Table 1 参照）。

### 4. 外科手術（Model Surgery）と継続的カリキュラム

10ヶ月に及ぶ長期間のトレーニング中、環境のパッチ変更（ルール変更）、ヒーロープール拡大、ネットワーク構造拡張（LSTMサイズ 2048 $\to$ 4096）が発生する。
これらに対して学習を一からやり直すのではなく、**既存のネットワークパラメータの機能を保ったまま入力層・出力層・中間層を動的に拡張する「外科手術（Surgery）」** 技術を開発し、知識を完全に維持したまま学習を継続した。

### 5. 過去モデルとのセルフプレイ（Self-Play with Past Opponents）

現在の自己と 80%、過去に保存されたチェックポイントの混合と 20% の割合で対戦させ、戦略のループやじゃんけん循環を防いだ。

## 結果

### Table 1: 報酬シェイピングの詳細（Name, Reward, Heroes, Description）

| Name | Reward | Heroes | Description |
|---|:---:|:---:|---|
| Win | 5 | Team | 試合勝利時 |
| Hero Death | -1 | Solo | 自身ヒーローの死亡 |
| Courier Death | -2 | Team | クーリエ（運搬ユニット）の死亡 |
| XP Gained | 0.002 | Solo | 獲得経験値あたり |
| Gold Gained | 0.006 | Solo | 獲得ゴールドあたり（消費しても失われない） |
| Gold Spent | 0.0006 | Solo | クーリエを使わずにアイテム購入に消費したゴールド |
| Health Changed | 2 | Solo | ヒーローの最大HPに対する比率（4次補間関数を使用） |
| Mana Changed | 0.75 | Solo | ヒーローの最大マナに対する比率 |
| Killed Hero | -0.6 | Solo | 敵ヒーロー撃破時（ゴールド・XP報酬が高いため過剰ボーナスを抑制） |
| Last Hit | -0.16 | Solo | ラストヒット時（ゴールド報酬と合わせて約 0.4 に調整） |
| Deny | 0.15 | Solo | 味方クリープのディナイ（敵への経験値遮断） |
| Gained Aegis | 5 | Team | ロシャンのイージス（復活アイテム）獲得 |
| Ancient HP Change | 5 | Team | 敵本拠地（Ancient）の最大HPに対するダメージ比率 |
| Megas Unlocked | 4 | Team | 全兵舎破壊によるメガクリープ解放 |
| T1 Tower | 2.25 | Team | 第1タワー破壊（2/3は削り時、1/3は破壊時） |
| T2 Tower | 3 | Team | 第2タワー破壊 |
| T3 Tower | 4.5 | Team | 第3タワー破壊 |
| T4 Tower | 2.25 | Team | 本拠地前タワー破壊 |
| Shrine | 2.25 | Team | シュライン破壊 |
| Barracks | 6 | Team | 兵舎破壊 |
| Lane Assign | -0.15 | Solo | 序盤に指定外のレーンに滞在している時間（秒あたり） |

### Table 2: 人間トップチームとの対戦成績

| Opponent | Result | Duration | Version | Restrictions |
|---|:---:|:---:|:---:|---|
| **2018年6月6日 (社内戦)** | | | | |
| 社内精鋭チーム | win | 15:15 (降伏) | 7.13 | ミラーマッチ、複数クーリエ、不可視なし |
| 社内精鋭チーム | win | 20:51 | 7.13 | ミラーマッチ、複数クーリエ、不可視なし |
| 観客選抜チーム | win | 31:33 | 7.13 | ミラーマッチ、複数クーリエ、不可視なし |
| 観客選抜チーム | win | 23:33 (降伏) | 7.13 | ミラーマッチ、複数クーリエ、不可視なし |
| **2018年8月5日 (公開ベンチマーク)** | | | | |
| キャスターチーム（元プロ） | win | 21:38 (降伏) | 7.16 | ドラフトあり、複数クーリエ |
| キャスターチーム（元プロ） | win | 24:56 (降伏) | 7.16 | ドラフトあり、複数クーリエ |
| キャスターチーム（元プロ） | lose | 35:47 | 7.16 | 観客ドラフト、複数クーリエ |
| **2018年8月9日 (非公開評価戦)** | | | | |
| Team Secret（世界トッププロ） | win | 17:00 (降伏) | 7.16 | ドラフトあり、複数クーリエ |
| Team Secret | lose | 48:46 | 7.16 | ドラフトあり、複数クーリエ |
| Team Secret | lose | 38:55 | 7.16 | ドラフトあり、複数クーリエ |
| **2019年4月13日 (OpenAI Five Finals)** | | | | |
| **OG（TI8 世界王者）** | **win** | **38:20** | **7.21c** | **公式大会ルール（全制限解除）** |
| **OG（TI8 世界王者）** | **win** | **30:04** | **7.21c** | **公式大会ルール（全制限解除）** |

### Table 3: 主要ハイパーパラメータ比較

| Param | CleanExp (追試版) | OpenAI Five (本番) | Baseline |
|---|:---:|:---:|:---:|
| Frameskip | 4 | 4 | 4 |
| LSTM Unroll length | 16 | 16 | 16 |
| オプティマイザ GPU数 | 512 | 480 $\leftrightarrow$ 1,536 | 64 |
| バッチサイズ/GPU (samples) | 120 | 120 $\leftrightarrow$ 128 | 120 |
| 総バッチサイズ (timesteps) | 983,040 | 983,040 $\leftrightarrow$ 3,145,728 | 122,880 |
| ロールアウト GPU数 | 512 | 500 $\leftrightarrow$ 1,440 | 64 |
| ロールアウト CPU数 | 51,200 | 80,000 $\leftrightarrow$ 172,800 | 6,400 |
| LSTM隠れ層サイズ | 4096 | 2048 $\to$ 4096 | 4096 |
| Sample Reuse (サンプル再利用率) | 1.0 $\leftrightarrow$ 1.1 | 0.8 $\leftrightarrow$ 2.7 | 1.0 $\leftrightarrow$ 1.1 |
| Team Spirit $\tau$ | 0.3 $\to$ 0.8 | 0.3 $\to$ 1.0 | 0.3 |
| GAE ホライズン | 180秒 $\to$ 360秒 | 60秒 $\to$ 840秒 | 180秒 |
| GAE $\lambda$ | 0.95 | 0.95 | 0.95 |
| PPO クッピング $\epsilon$ | 0.2 | 0.2 | 0.2 |
| エントロピー係数 | 0.01 $\to$ 0.001 | 0.01 $\to$ 0.001 | 0.01 |
| 学習率 | 5e-5 $\to$ 5e-6 | 5e-5 $\leftrightarrow$ 1e-6 | 5e-5 |
| 過去対戦相手比率 | 20% | 20% | 20% |

### Table 4: アクションターゲット種別（Action Target Types）

| Action Target Type | Example | Parameters |
|---|---|---|
| No Target | Power Treads（靴切り替え） | Delay |
| Point Target | Move（移動） | Delay, Offset (Caster) |
| Unit Target | Attack（攻撃） | Delay, Unit Selection (Regular) |
| Unit Offset Target | Sniper's Shrapnel（地点指定スキル） | Delay, Unit Selection (Regular), Offset (Regular) |
| Teleport Target | Town Portal Scroll（TPスクロール） | Delay, Unit Selection (Teleport), Offset (Regular) |
| Ward Target | Place Observer Ward（ワード設置） | Delay, Offset (Ward) |

### 各図（Figure）の解説

- **システムアーキテクチャ (Training-Architecture.png / smallarchdiagram.png)**:
  - 1ヒーローあたり1つの4096ユニットLSTMを配置。観測（味方・敵・クリープ・マップデータ）はエンコーダを経てLSTMに入力され、Action Head、Target Head、Delay Head、Value Headへ分岐。
- **レーン割り当てとチームスピリット (expl-lane-assignments-*.pdf)**:
  - 序盤（0〜10分）において各ヒーローが指定されたレーンを守るようペナルティを与えた実験。レーン指定がないと序盤に全員が1つのレーンに集まってしまい、マップ全体の経験値・ゴールド獲得効率が激減することを確認。
  - Team Spirit を 0.3 から徐々に引き上げることで、序盤のレーン戦（個人技能）と終盤の集団戦（チーム連携）が両立することを示した。
- **勝率予測と目標予測 (winrates-OG-game-1.png, objectives-OG-game-1.png)**:
  - 対OG戦の試合中における OpenAI Five の勝率予測値。序盤のキル発生やタワー破壊のたびにリアルタイムに勝率を極めて正確に更新。
- **ヒーロードラフト（hero-selection.png）**:
  - ミニマックス木探索を用いたドラフトツール。相手のピックに対する最悪勝率を最大化する堅実なチーム構成を選択。


# 考察：カードゲーム強化学習への具体的応用と設計指針

OpenAI Five で実証された数々の工学的アプローチは、不完全情報・長期ホライズン・膨大な状態空間を持つカードゲーム（TCG/DCG）の強化学習において極めて強力な指針となる。

---

### 1. ホライズンのブートストラップ（GAE）による分散低減
ロングホライゾン問題の解決手段として。カードゲームにも使いたい。  

---

### 2. 段階的報酬シェイピングとアニーリング（序盤の迷走・無駄打ち防止）
シェイピングとアニーリングの具体的数値感を参考に 

---

### 3. 過去チェックポイントとの混合対戦（Self-Play の循環・忘却防止）
byteRLでも活用の手法。やっぱり大事。

---

### 4. 外科手術（Surgery）によるアップデート・新弾・エラッタ対応
* **解決策（既存の挙動を100%保存したままパラメータを動的拡張）：**  
  * **新カードの追加（入力・Embedding層の拡張）:**  
    カードIDの埋め込みテーブルに行を追加。既存カードへの重みはそのままに、新カードに対する重み列をゼロ初期化することで、追加直後の出力分布を全く崩さずに学習を再開する。
  * **新アクションの追加（出力ヘッドの拡張）:**  
    新しい行動選択肢の出力ロジットを負の大きな値（または重み0）で初期化し、初期選択確率を $\approx 0$ に抑えて既存の定石知識を維持したまま、探索ノイズを通じて徐々に新アクションの有効性を学習させる。
  * **オプティマイザ状態の移植:**  
    Adam のモメンタム（$m_t, v_t$）を既存パラメータ部分について完全に引き継ぎ、追加パラメータのみ 0 で初期化することで、学習再開時のパラメータ破壊を防ぐ。