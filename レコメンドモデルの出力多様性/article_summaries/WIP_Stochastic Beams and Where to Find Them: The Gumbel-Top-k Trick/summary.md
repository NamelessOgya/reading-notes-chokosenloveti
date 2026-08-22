# Stochastic Beams and Where to Find Them: The Gumbel-Top-$k$ Trick for Sampling Sequences Without Replacement

論文の背景, 手法, 結果の3項目でまとめます。

---

## 背景

自然言語処理（機械翻訳・テキスト生成）やレコメンドシステム（シーケンシャル推薦・スレート生成）などの系列モデル（Sequence Models）において、モデルの出力確率分布から**代表的な複数の系列（またはアイテムのセット）を重複なく高品質かつ多様に抽出すること**は極めて重要な課題です。

従来の系列生成・探索アプローチには、それぞれ以下のような一長一短が存在していました：

1. **通常の確率的サンプリング（復元抽出 / Sampling with replacement）**:
   - 温度付き Softmax から独立に $k$ 個の系列をサンプリングする手法。
   - 分布のエントロピーが低い（一部の高確率な系列に確率が集中している）場合、同じ高確率系列が何度も重複してサンプリングされてしまい、**出力の多様性（Diversity）が著しく損なわれる**。重複を破棄するリジェクションサンプリングは計算効率が極めて悪い。
2. **決定論的ビームサーチ（Deterministic Beam Search）**:
   - 各ステップで最も確率の高い $k$ 個の部分系列を幅優先探索で追跡する手法。
   - 高品質な系列を探索できるものの、探索が決定論的であるため**得られる系列間のバリエーション（多様性）が極めて乏しく、確率論的な解釈（Importance Sampling等による統計的推定量への利用）が不可能**である。
3. **Diverse Beam Search などのヒューリスティック手法**:
   - 探索時に類似グループへのペナルティを課すことで多様化を図るが、アドホックなペナルティ項に依存しており、理論的な確率分布の保証を欠く。

カテゴリカル分布から単一の要素を確率的に抽出する手法として **Gumbel-Max Trick** が広く知られていますが、これを「**重複なし（非復元抽出 / Sampling without replacement）で $k$ 個の要素を抽出する**」形に拡張したものが **Gumbel-Top-$k$ Trick**（Plackett–Luce 分布からのサンプリングと同等）です。

しかし、系列モデルのように状態空間が指数関数的に爆発する巨大な確率木に対して、すべての系列をあらかじめ列挙して Gumbel ノイズを付与することは計算量的に不可能です。

本論文は、Gumbel-Top-$k$ Trick を系列モデルの確率木上でトップダウン（Top-Down）かつ暗黙的（Implicit）に適用する新しいアルゴリズム **Stochastic Beam Search (SBS)** を提案し、爆発的な状態空間であってもサンプル数 $k$ と系列長に対して線形時間 $\mathcal{O}(k \cdot L)$ で「**Plackett–Luce分布に基づく完全な非復元抽出（重複なし多様サンプリング）**」を実現しました。

---

## 手法

### 1. Gumbel-Max Trick と Gumbel-Top-$k$ Trick の数理

カテゴリカル分布 $\text{Categorical}(p_{1}, \dots, p_{n})$（ここで $p_{i} = \frac{\exp(\phi_{i})}{\sum_{j=1}^{n} \exp(\phi_{j})}$、$\phi_{i}$ は非正則化対数確率）からサンプリングを行う際、各要素に独立な標準Gumbelノイズ $G_{i} \sim \text{Gumbel}(0)$ を加えた**摂動対数確率（Perturbed Log-probability）** $G_{\phi_{i}} = \phi_{i} + G_{i} \sim \text{Gumbel}(\phi_{i})$ を定義します。

- **Gumbel-Max Trick**: 最大値をとるインデックス $I^{*} = \arg\max_{i} G_{\phi_{i}}$ は、元のカテゴリカル分布 $p_{i}$ からの正確なサンプリングとなります。
- **Gumbel-Top-$k$ Trick**: 最大値の代わりに上位 $k$ 個のインデックス $I^{*}_{1}, \dots, I^{*}_{k} = \arg\text{top-}k \, \{ G_{\phi_{i}} \}$ を降順に取得すると、これは**非復元抽出（Plackett–Luce モデル）による正確な順序付きサンプル**となります：

$$ P(I^{*}_{1} = i^{*}_{1}, \dots, I^{*}_{k} = i^{*}_{k}) = \prod_{j=1}^{k} \frac{\exp(\phi_{i^{*}_{j}})}{\sum_{\ell \in N \setminus \{i^{*}_{1}, \dots, i^{*}_{j-1}\}} \exp(\phi_{\ell})} $$

### 2. 確率木上でのトップダウン Gumbel 摂動伝播

系列モデル $p_{\boldsymbol{\theta}}(\boldsymbol{y}_{1:t}) = \prod_{t'=1}^{t} p_{\boldsymbol{\theta}}(y_{t'} \mid \boldsymbol{y}_{1:t'-1})$ を確率木として表現します。部分系列 $\boldsymbol{y}^{S}$（部分木の葉ノード集合 $S$ に対応）の対数確率を $\phi_{S} = \log \sum_{i \in S} \exp(\phi_{i})$ と定義します。

部分木の葉ノード群が持つ摂動対数確率の最大値 $G_{\phi_{S}} = \max_{i \in S} G_{\phi_{i}}$ は、Gumbel の最大値特性により自身も Gumbel 分布 $G_{\phi_{S}} \sim \text{Gumbel}(\phi_{S})$ に従います。

親ノード $S$ の摂動値 $G_{\phi_{S}}$ が与えられたとき、その子ノード群 $S' \in \text{Children}(S)$ の摂動値 $G_{\phi_{S'}}$ を「最大値が親の $G_{\phi_{S}}$ と一致する」という条件付き分布からサンプリングします：
1. 各子ノードに対して独立に $G_{\phi_{S'}} \sim \text{Gumbel}(\phi_{S'})$ を生成し、$Z = \max_{S' \in \text{Children}(S)} G_{\phi_{S'}}$ を計算。
2. 以下の変換を適用することで、最大値が厳密に $G_{\phi_{S}}$ となる条件付きGumbelノイズ $\tilde{G}_{\phi_{S'}}$ を生成：

$$ \tilde{G}_{\phi_{S'}} = -\log\left( \exp(-G_{\phi_{S}}) - \exp(-Z) + \exp(-G_{\phi_{S'}}) \right) $$

### 3. Stochastic Beam Search アルゴリズム

木全体を網羅的に生成する代わりに、各ステップ $t$ において**摂動対数確率 $\tilde{G}_{\phi_{S}}$ が上位 $k$ 個の部分系列（ビーム）のみを展開（Expand）**します。

- **枝刈り（Pruning）の正当性**: 上位 $k$ 個の葉ノードの祖先ノードは、各深さ $t$ において必ず高々 $k$ 個しか存在せず、それらの $G_{\phi_{S}}$ は上位 $k$ 個に含まれるため、ビーム幅 $k$ で刈り取っても真のTop-$k$葉ノードが脱落することはありません。
- **計算量**: 展開される系列数は各ステップで高々 $k \times |\mathcal{V}|$（語彙数/候補数）であり、全体の計算量はサンプル数 $k$ と系列長 $L$ に対して $\mathcal{O}(k \cdot L)$ の線形時間で実行可能です。

### 4. 非復元抽出による統計的推定量（Importance Sampling）の構築
SBS によって得られた重複のないサンプル集合 $S$ を用いて、任意の系列関数 $f(\boldsymbol{y})$ の期待値 $\mathbb{E}_{\boldsymbol{y} \sim p}[f(\boldsymbol{y})]$ を低分散に推定できます。
$(k+1)$ 番目に大きい摂動値 $\kappa$（実効閾値）を用いて Priority Sampling の重要度重みを適用した正規化推定量は以下で与えられます：

$$ \mathbb{E}_{\boldsymbol{y}}[f(\boldsymbol{y})] \approx \frac{1}{W(S)} \sum_{i \in S} \frac{p_{\boldsymbol{\theta}}(\boldsymbol{y}^{i} \mid \boldsymbol{x})}{q_{\boldsymbol{\theta}, \kappa}(\boldsymbol{y}^{i} \mid \boldsymbol{x})} f(\boldsymbol{y}^{i}) $$

ここで $q_{\boldsymbol{\theta}, \kappa}(\boldsymbol{y}^{i} \mid \boldsymbol{x}) = 1 - \exp(-\exp(\phi_{i} - \kappa))$ であり、$W(S) = \sum_{i \in S} \frac{p_{\boldsymbol{\theta}}(\boldsymbol{y}^{i} \mid \boldsymbol{x})}{q_{\boldsymbol{\theta}, \kappa}(\boldsymbol{y}^{i} \mid \boldsymbol{x})}$ です。

---

## 結果

WMT14 英語-フランス語機械翻訳タスク（3,003文）および pretrained ConvS2S モデルを用いて、系列の出力多様性、BLEUスコア、および統計推定量の分散低減効果を検証しました。

### 1. 多様性（Diversity）と品質（BLEU）のトレードオフ検証

生成された $k$ 個の文におけるユニークな $n$-gram の割合を多様性指標 $d = \frac{1}{4}\sum_{n=1}^{4} d_{n}$ とし、BLEU スコア（Min / Mean / Max）との関係を比較しました。

| サンプルサイズ $k=5$ | サンプルサイズ $k=10$ | サンプルサイズ $k=20$ |
| :---: | :---: | :---: |
| ![Diversity k=5](./images/k5diversity.png) | ![Diversity k=10](./images/k10diversity.png) | ![Diversity k=20](./images/k20diversity.png) |

- **考察**:
  - **Stochastic Beam Search (SBS)** は、従来のヒューリスティックな Diverse Beam Search (DBS) と比較して、**同一の多様性レベルにおいて常に高い平均/最大BLEUスコアを達成**しています。
  - 通常の確率的サンプリング（Sampling）は同じ良質な文を重複抽出するため平均BLEUは高く見えますが、多様性が低く、最大BLEU（最良の文を見つける能力）は劣ります。
  - SBS は温度パラメータ $T < 0.5$ において決定論的ビームサーチと同等の最高品質（Max BLEU）を維持しながら、出力のバリエーション（多様性）を劇的に向上させることが確認されました。

---

### 2. 文レベル BLEU スコアの統計的推定

文レベル BLEU の期待値を、通常の Monte Carlo (MC) サンプリングと SBS による非復元抽出推定量で比較しました。

![BLEU Estimates](./images/bleu_estimates.png)

- **考察**:
  - サンプルサイズ $k$ を変化させた際の推定値の分散（2.5パーセンタイル〜97.5パーセンタイル）を評価した結果、正規化 SBS 推定量は MC サンプリングと比較して**分散（ばらつき）が劇的に小さく、より少ないサンプル数で真の期待値へ高速に収束**しました。
  - $T < 0.5$ の低エントロピー環境において、重複サンプリングを排除した効果が顕著に現れています。

---

### 3. 条件付きエントロピーの推定

モデルの出力不確実性を表すエントロピー $\mathbb{E}[-\log p(\boldsymbol{y} \mid \boldsymbol{x})]$ の推定比較です。

![Entropy Estimates](./images/entropy_estimates.png)

- **考察**:
  - エントロピーのように稀な系列（低確率系列）が大きな寄与を持つ指標に対しても、SBS推定量は MC サンプリングよりも著しく狭い信頼区間（超低分散）を達成しました。
  - これにより、推薦や強化学習におけるエントロピー正則化項（多様性ペナルティ）を低計算コスト・低分散で最適化できる道が開かれました。

---

### 4. 筆者の考察と総括
1. **理論と探索の架け橋**: Gumbel-Top-$k$ Trick を木探索に導入した Stochastic Beam Search は、純粋な確率サンプリングと決定論的ビームサーチの中間に位置する「**理論的根拠（確率解釈）を持つランダム化ビーム探索**」を確立しました。
2. **推薦システム・スレート生成への応用価値**: 本手法は自然言語生成のみならず、推薦システムにおける「ユーザーへの重複のない多様なスレート（リスト）提示」や「オフラインでの低分散方策評価（Off-policy Policy Evaluation）」の基盤サンプラーとして絶大な実用性を持ちます。
