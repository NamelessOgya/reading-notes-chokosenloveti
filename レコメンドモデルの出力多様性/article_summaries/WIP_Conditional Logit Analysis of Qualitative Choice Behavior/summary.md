# Conditional Logit Analysis of Qualitative Choice Behavior

論文の背景, 手法, 結果の3項目でまとめます。

---

## 背景

計量経済学や社会科学、交通工学、マーケティングにおいて、消費者が車・電車・バスなどの**離散的な選択肢（Qualitative / Discrete Alternatives）**の中から1つを選ぶ行動をどのように計量モデル化するかは長年の重要課題でした。

本論文以前の意思決定理論には以下の大きな断絶が存在していました：
1. **新古典派経済学の効用最大化理論**:
   - 消費者は自身の効用を最大化する選択肢を 100% 確実に選ぶ（決定論的効用モデル）と仮定していましたが、現実のデータで観測される「同じ所得・属性の個人でも異なる選択をする」という確率的な揺らぎを説明できませんでした。
2. **サーストン・モデル（Thurstone 1927）の多重積分問題**:
   - ランダム効用モデル（RUM）として正規分布誤差（プロビットモデル）を仮定すると、選択肢数が3つ以上になった瞬間に多重積分の数値計算が不可能になり、パラメータ推定が行き詰まっていました。
3. **ルースの選択公理（Luce 1959）と経済理論の未接続**:
   - ルースは心理学的な公理から Softmax 型の選択確率（Luce Rule）を導きましたが、それが「消費者が効用を最大化している」という経済学の基本原理とどう結びついているのか、その微視的経済学的根拠（Micro-foundations）が未解明でした。

**ダニエル・マクファデン（Daniel McFadden）** は本論文において、新古典派経済学の「効用最大化行動」と統計学の「極値分布（ガンベル分布）」を融合させ、**多項ロジットモデル（Conditional Logit Model / Softmax）のミクロ経済学的・数理統計学的基礎を完全に確立**しました（本研究を含む離散選択理論の功績により、マクファデンは2000年にノーベル経済学賞を受賞）。

---

## 手法

### 1. ランダム効用モデル（Random Utility Model: RUM）の定式化

意思決定者 $n$ が選択肢集合 $C = \{1, 2, \dots, J\}$ から選択肢を選ぶ状況を考えます。
各選択肢 $i \in C$ から個人 $n$ が得る潜在的な効用 $U_{ni}$ を、観測可能な確定効用 $V_{ni}$ と、観測不可能なランダム誤差 $\epsilon_{ni}$ の和としてモデル化します：

$$ U_{ni} = V_{ni} + \epsilon_{ni} = \boldsymbol{\beta}^{T} \boldsymbol{x}_{ni} + \epsilon_{ni} $$

ここで $\boldsymbol{x}_{ni}$ は選択肢の属性（例：価格、所要時間、コンテンツ特徴量）および個人の属性を表す特徴量ベクトル、$\boldsymbol{\beta}$ は推定すべきパラメータベクトルです。

消費者は**自身の効用が最大となる選択肢 $i$ を選択**します：

$$ P_{n}(i \mid C) = P\left( U_{ni} > \max_{j \in C, j \neq i} U_{nj} \right) = P\left( V_{ni} + \epsilon_{ni} > \max_{j \neq i} (V_{nj} + \epsilon_{nj}) \right) $$

---

### 2. ガンベル分布（Type I 極値分布）とマクファデンの定理

マクファデンは、各誤差項 $\epsilon_{ni}$ が互いに独立同分布（i.i.d.）で以下の**ガンベル分布（Type I Extreme Value / Gumbel Distribution）**に従うと仮定しました：

$$ F(\epsilon) = P(\epsilon \le t) = \exp(-\exp(-t)) $$

このとき、最大効用を選択する確率 $P_{n}(i \mid C)$ は、閉形式（解析解）として厳密に **Softmax / 条件付きロジット（Conditional Logit）関数** と一致することを証明しました：

$$ P_{n}(i \mid C) = \frac{\exp(V_{ni})}{\sum_{j \in C} \exp(V_{nj})} = \frac{\exp(\boldsymbol{\beta}^{T} \boldsymbol{x}_{ni})}{\sum_{j \in C} \exp(\boldsymbol{\beta}^{T} \boldsymbol{x}_{nj})} $$

- **数理的架橋の達成**:
  Luce (1959) が「選択公理」から導いた比率尺度 $v(i) = \exp(V_{ni})$ の正当性が、「各選択肢のランダムノイズがガンベル分布に従う下での効用最大化行動」という経済学的メカニズムとして完全に証明されました。

---

### 3. 最尤推定法（Maximum Likelihood Estimation: MLE）と大域的凸性

観測された $N$ 人の選択データ $(y_{n1}, \dots, y_{nJ})$（個人 $n$ が $i$ を選んだとき $y_{ni}=1$、それ以外 $0$）に対する対数尤度関数は以下となります：

$$ \ln L(\boldsymbol{\beta}) = \sum_{n=1}^{N} \sum_{i \in C} y_{ni} \ln P_{n}(i \mid C) = \sum_{n=1}^{N} \sum_{i \in C} y_{ni} \left( \boldsymbol{\beta}^{T} \boldsymbol{x}_{ni} - \ln \sum_{j \in C} \exp(\boldsymbol{\beta}^{T} \boldsymbol{x}_{nj}) \right) $$

マクファデンは、この対数尤度関数がパラメータ $\boldsymbol{\beta}$ に関して**強凹（Strictly Concave）**であることを証明しました。これにより、局所最適解に陥ることなくニュートン法（Newton-Raphson）や勾配降下法によって大域的最適解 $\hat{\boldsymbol{\beta}}$ が確実に求まることが保証されました。

---

## 結果（実証分析と理論的影響）

### 1. サンフランシスコ湾岸高速鉄道（BART）の需要予測実証
マクファデンらは本手法を、当時建設中であったサンフランシスコ湾岸高速鉄道（BART: Bay Area Rapid Transit）の開業前交通需要予測に適用しました。
- 開業前に人々の通勤選択データ（自動車・バス・徒歩）からモデルを学習し、BART 開業後の乗車率を予測したところ、公式予測（従来の集計モデル）よりも遥かに正確に実際の利用率を的中させ、本モデルの実用性と精度の高さを世界に証明しました。

---

## 考察と現代機械学習・推薦システムへの絶大な影響

1. **ディープラーニングと Softmax の理論的支柱**:
   - 現代の分類モデル（Cross-Entropy 損失）や推薦モデル（Item2Vec, SASRec, YouTube DNN）で出力層に Softmax を用いる根拠は、本論文の「ガンベル誤差のもとでの最適選択モデル」にあります。
2. **Gumbel-Max / Gumbel-Softmax トリックの起源**:
   - 近年の深層学習で広く用いられる **Gumbel-Max Trick**（カテゴリカル分布からのサンプリング）や **Gumbel-Softmax / Concrete 分布**（離散変数の微分可能緩和）は、すべてマクファデンが示した「効用 $V_{i}$ に標準ガンベルノイズ $G_{i}$ を足して $\arg\max$ を取ると Softmax 確率でサンプリングされる」という定理そのものを応用したものです。
3. **出力多様性・スレート推薦への接続**:
   - 後続研究（Kool et al. 2019 の Gumbel-Top-$k$ や Eugene Ie et al. 2019 の SlateQ）は、本論文の条件付きロジットモデルを複数アイテムの非復元抽出や長期強化学習へと発展させた直接の後継技術です。
