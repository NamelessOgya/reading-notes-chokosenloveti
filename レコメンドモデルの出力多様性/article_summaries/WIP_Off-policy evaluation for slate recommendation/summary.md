# Off-policy evaluation for slate recommendation

論文の背景, 手法, 結果の3項目でまとめます。

---

## 背景

Eコマース、ニュース推薦、Web検索などのオンライン推薦システムでは、単一のアイテムではなく**複数のアイテムが順序付きで並んだリスト（スレート / Slate）**をユーザーに提示します。システム運用中に収集されたログデータ（過去の方策 $\mu$ によって収集されたデータ）を用いて、新しい推薦アルゴリズムやランキング方策（ターゲット方策 $\pi$）の性能（クリック率、売上、ユーザー満足度など）をオフラインで評価・検証するタスクを **オフポリシー評価（Off-Policy Evaluation: OPE）** と呼びます。

スレート推薦におけるオフポリシー評価には、以下の極めて深刻な**組み合わせ爆発（Combinatorial Explosion）**の課題が存在していました：

1. **標準的な Inverse Propensity Scoring (IPS) の破綻**:
   - スレート全体の選択肢の総数は、候補アイテム数 $m$、スレート長 $\ell$ に対して $m^{\Omega(\ell)}$（順列数 $m! / (m-\ell)!$）通り存在します。
   - スレート全体を1つの離散行動として扱う標準的な IPS では、スレート全体の選択確率 $\mu(\boldsymbol{s} \mid x)$ で観測報酬を重み付けするため、重要度比（Importance Weight）が天文学的なオーダーで巨大化し、**推定量の分散が爆発して実質的に推定不能**（非現実的な膨大なログデータ量を要求）となります。
2. **直接法（Direct Method: DM）の高バイアス**:
   - 機械学習モデルでスレート全体の期待報酬 $\hat{r}(x, \boldsymbol{s})$ を直接予測するアプローチは分散こそ小さいものの、ユーザー行動やコンテキストの複雑な相互作用を完璧にモデル化できず、**深刻な推定バイアス（モデルの誤設定による誤差）**を抱えます。
3. **高コストなオンライン A/B テストへの依存**:
   - オフラインでの信頼性の高い評価法が存在しなかったため、新方策の検証には数週間に及ぶリスクの高いオンライン A/B テストを繰り返す必要があり、開発サイクルを著しく遅延させていました。

本論文は、コンビナトリアル・バンディットの理論に着想を得て、スレート全体の報酬に対する**加法分解性（Additive Decomposition）**という自然で弱い仮定を導入することで、IPSの不偏性を維持しながらデータ要求量を指数関数的に削減（ $m^{\Omega(\ell)}$ から $\mathcal{O}(\ell m / \epsilon^{2})$ へ）する新しい推定量 **Pseudoinverse (PI) Estimator（疑似逆行列推定量）** を提案しました。

---

## 手法

### 1. コンビナトリアル文脈バンディット（Combinatorial Contextual Bandits）の定式化

- **コンテキスト**: $x \sim D(x)$（ユーザープロファイルや検索クエリなど）。
- **スレート（行動）**: $\boldsymbol{s} = (s_{1}, \dots, s_{\ell})$。ここで各スロット $j \in \{1, \dots, \ell\}$ に配置されるアイテム $s_{j}$ は候補集合 $A_{j}(x)$（サイズ $m_{j} \le m$）から重複なしで選ばれます。
- **スレートのワンホット指示ベクトル**: $\mathbf{1}_{\boldsymbol{s}} \in \{0, 1\}^{\ell m}$。スロット $j$ にアイテム $a$ が配置されているとき対応する要素が 1、それ以外が 0 となる疎ベクトル。
- **観測報酬**: スレート全体に対して観測される単一の集約報酬 $r \in [-1, 1]$（例：ページ全体の滞在時間、総クリック数、NDCG 等）。各アイテム個別の報酬は直接観測されません。
- **方策の価値（期待報酬）**:

$$ V(\pi) = \mathbb{E}_{x \sim D} \mathbb{E}_{\boldsymbol{s} \sim \pi(\cdot \mid x)} \mathbb{E}_{r \sim D(\cdot \mid x, \boldsymbol{s})}[r] $$

### 2. 報酬の加法分解仮定（Additive Decomposition Assumption）

スレート全体の期待報酬 $V(x, \boldsymbol{s}) = \mathbb{E}[r \mid x, \boldsymbol{s}]$ が、各スロット・アイテムの潜在的な寄与ベクトル $\boldsymbol{\phi}_{x} \in \mathbb{R}^{\ell m}$ の線形結合として分解されると仮定します：

$$ V(x, \boldsymbol{s}) = \mathbf{1}_{\boldsymbol{s}}^{T} \boldsymbol{\phi}_{x} = \sum_{j=1}^{\ell} \phi_{x}(j, s_{j}) $$

※重要な点として、潜在寄与ベクトル $\boldsymbol{\phi}_{x}$ はコンテキスト $x$ ごとに任意に変化してよく、特徴量からの線形予測可能性などを一切仮定しません（完全なモデルフリー・ノンパラメトリック）。

### 3. Pseudoinverse (PI) Estimator の導出

ログ方策 $\mu$ の下で観測されるスレート指示ベクトルの非中心共分散行列を $\boldsymbol{\Gamma}_{\mu, x} = \mathbb{E}_{\mu}[\mathbf{1}_{\boldsymbol{s}} \mathbf{1}_{\boldsymbol{s}}^{T} \mid x] \in \mathbb{R}^{\ell m \times \ell m}$ と定義します。

潜在寄与ベクトル $\boldsymbol{\phi}_{x}$ の最小二乗解は、Moore-Penrose 疑似逆行列 $\boldsymbol{\Gamma}_{\mu, x}^{\dagger}$ を用いて以下のように表されます：

$$ \bar{\boldsymbol{\phi}}_{x} = \boldsymbol{\Gamma}_{\mu, x}^{\dagger} \mathbb{E}_{\mu}[r \mathbf{1}_{\boldsymbol{s}} \mid x] $$

ターゲット方策 $\pi$ の下での期待スレート指示ベクトルを $\mathbf{q}_{\pi, x} = \mathbb{E}_{\pi}[\mathbf{1}_{\boldsymbol{s}} \mid x]$ とすると、ターゲット方策の期待値 $V(\pi) = \mathbb{E}_{x}[\mathbf{q}_{\pi, x}^{T} \bar{\boldsymbol{\phi}}_{x}]$ に対する標本推定量 **PI推定量** が得られます：

$$ \hat{V}_{\text{PI}}(\pi) = \frac{1}{n} \sum_{i=1}^{n} r_{i} \cdot \mathbf{q}_{\pi, x_{i}}^{T} \boldsymbol{\Gamma}_{\mu, x_{i}}^{\dagger} \mathbf{1}_{\boldsymbol{s}_{i}} $$

さらに、有限サンプルでの分散を低減するための自己正規化版（Weighted PI: wPI）も定義されます：

$$ \hat{V}_{\text{wPI}}(\pi) = \frac{\sum_{i=1}^{n} r_{i} \cdot \mathbf{q}_{\pi, x_{i}}^{T} \boldsymbol{\Gamma}_{\mu, x_{i}}^{\dagger} \mathbf{1}_{\boldsymbol{s}_{i}}}{\sum_{i=1}^{n} \mathbf{q}_{\pi, x_{i}}^{T} \boldsymbol{\Gamma}_{\mu, x_{i}}^{\dagger} \mathbf{1}_{\boldsymbol{s}_{i}}} $$

### 4. なぜ分散が劇的に減少するのか？
- **Plackett–Luce や独立サンプリングにおける共分散構造**:
  例えばログ方策 $\mu$ が各スロットで独立にアイテムを選択する場合、PI 推定量は各スロットごとの確率比の和に簡約されます：

$$ \hat{V}_{\text{PI}}(\pi) = \frac{1}{n} \sum_{i=1}^{n} r_{i} \left( \sum_{j=1}^{\ell} \frac{\pi(s_{ij} \mid x_{i})}{\mu(s_{ij} \mid x_{i})} - \ell + 1 \right) $$

- スレート全体の結合確率の積で割る IPS では重みが $m^{\Omega(\ell)}$ に爆発しますが、PI 推定量では各スロットごとの周辺確率比の和となるため、各サンプルの重みの大きさが $\mathcal{O}(\ell m)$ に抑えられます。

---

## 結果

商用検索エンジン（Bing）の大規模実ログデータ、および標準的な検索ベンチマーク（MSLR-WEB10K）に基づく半合成データセットを用いて、推定精度（RMSE）およびオフライン方策最適化性能を検証しました。

### 1. Bing 商用検索エンジン実ログデータでの評価

Bing の実際の検索ログデータにおいて、2種類のページ全体ユーザー満足度指標（Metric 1, Metric 2）を対象に、50回の独立試行における平均二乗二乗根誤差（RMSE）を対数スケールで比較しました。

![Bing Experiments](./images/bing_plots_grouped.png)

- **考察**:
  - **IPS (Inverse Propensity Scoring)**: スレート空間の爆発により重みの分散が極めて大きく、サンプル数を増やしても RMSE がほとんど減少しません。
  - **Direct Method (DM)**: サンプル数が少ないうちは低い誤差を示しますが、モデルの表現力不足によるバイアスが存在するため、データ量を増やしても一定の誤差フロア（漸近バイアス）に突き当たります。
  - **PI (Pseudoinverse Estimator)**: 適度なデータサイズから最も急速に RMSE が減少し、**不偏性を保ちながら最小の推定誤差を達成**しました。

---

### 2. 半合成データセット（MSLR-WEB10K）における広範な比較

MSLR-WEB10K データセットを用い、候補アイテム数 $m \in \{10, 100\}$、スレート長 $\ell \in \{5, 10\}$、評価指標（NDCG, ERR）、ログ方策とターゲット方策の乖離度（ノイズパラメータ $n \in \{0.0, 0.5, 1.0, 2.0\}$）を系統的に変化させて検証しました。

![All Eval](./images/all_eval.png)

- **考察**:
  - スレート長 $\ell$ や候補数 $m$ が増大するほど、標準 IPS は急速に破綻（高分散）しますが、PI および重み付き PI (wPI) は極めて安定した推定を維持しました。
  - ログ方策 $\mu$ とターゲット方策 $\pi$ の重複度（Overlap）が低い過酷な環境下でも、wPI はベースライン手法（Slate-level Bandit手法やDirect Method）を一貫して上回る精度を示しました。

---

### 3. 筆者の考察と総括
1. **スレート推薦 OPE のブレークスルー**: ページ全体集約の単一報酬しか得られないブラックボックス環境であっても、加法分解構造を利用した線形代数的アプローチ（Moore-Penrose 疑似逆行列）により、指数関数的なサンプル複雑性の壁を打ち破れることを証明しました。
2. **多様性・探索方策の安全な評価**: Plackett–Luce モデルなどの確率的スレート生成方策によって多様性を高めた推薦モデルを、高コストな A/B テストを実施することなく、過去のログから正確かつ低リスクにオフライン評価・最適化できる基盤を確立しました。
