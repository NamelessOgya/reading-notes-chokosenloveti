# Plackett–Luceモデルとレコメンドの出力多様性

## 1. 概要
レコメンドシステムにおいて、ユーザーごとに最もスコアの高いTop-$K$個のアイテムを決定論的に提示する手法（アルゴリズム）は、**人気度偏向（Popularity Bias）**や**フィルタバブル**、**出力の単調化（同質化）**を引き起こしやすいという課題があります。

これに対して、アイテムの選好スコア（効用）に応じた確率的なランキング生成モデルである **Plackett–Luce（プラケット・ルース）モデル** を用いることで、スコアの高いアイテムを優先しつつも確率的な揺らぎ（Exploration / Sampling）によって**出力の多様性（Diversity）**を自然に確保することが可能になります。

---

## 2. Plackett–Luceモデルとは？

### (1) 直感的理解
Plackett–Luceモデルは、複数のアイテム候補集合から順序付きのリスト（スレート / Slate）を**「非復元抽出（Sampling without replacement）」**で1つずつ選んでいく連鎖的な確率モデルです。

1. アイテム全集合 $S$ の中から、各アイテムのスコア $s_i$ に比例した確率で 1 位のアイテム $y_1$ を選択します。
2. 選択された $y_1$ を集合から除外し、残りの集合 $S \setminus \{y_1\}$ から同様の確率で 2 位のアイテム $y_2$ を選択します。
3. これを所望のリスト長 $K$ まで繰り返します。

### (2) 数式による定式化
全アイテム数 $N$ 個のうち、アイテム $i$ の潜在的選好スコア（Logit）を $s_i \in \mathbb{R}$（または選好パラメータ $v_i = \exp(s_i) > 0$）とします。

1 位としてアイテム $y_1$ が選ばれる確率は Softmax 関数そのものです：

$$ P(y_1 = i) = \frac{\exp(s_i)}{\sum_{j \in S} \exp(s_j)} $$

$k$ 番目の位置にアイテム $y_k$ が選ばれる条件付き確率は、既に選ばれた上位アイテム $y_{<k} = \{y_1, \dots, y_{k-1}\}$ を除いた残りの集合に対する Softmax となります：

$$ P(y_k \mid y_1, \dots, y_{k-1}) = \frac{\exp(s_{y_k})}{\sum_{j \in S \setminus y_{<k}} \exp(s_j)} $$

したがって、長さ $K$ の推薦リスト $y = (y_1, y_2, \dots, y_K)$ 全体が生成される結合確率は次式で与えられます：

$$ P(y_1, y_2, \dots, y_K) = \prod_{k=1}^{K} \frac{\exp(s_{y_k})}{\sum_{j=k}^{K} \exp(s_{y_j})} $$

---

## 3. レコメンドの多様性における役割と限界

### メリット
- **確率的アプローチによる多様性の獲得**: 決定論的Top-$K$（スコア上位を常に固定表示）から、Plackett–Luceに基づくサンプリングに変更することで、ロングテールアイテムや新しいコンテンツが露出する機会が増えます。
- **温度パラメータ（Temperature）によるハイパーパラメータ制御**: スコアを $\frac{s_i}{\tau}$ と変換することで、$\tau \to 0$ では決定論的Top-$K$に近づき、$\tau \to \infty$ ではランダムサンプリングに近づくため、関連性（Relevance）と多様性（Diversity）のトレードオフを容易に制御できます。

### 限界（IIA仮定の存在）
- Plackett–Luceモデルは **IIA（Independence of Irrelevant Alternatives: 無関係な選択肢の独立性）** の公理に基づいています。
- つまり、「$k$ 番目に選ばれる確率」は**残りのアイテム各自の絶対的なスコアのみに依存**し、**すでに選ばれたアイテムとのコンテンツ的類似度（ジャンルの重複など）を考慮しない**という性質があります。
- そのため、真の意味でのコンテンツ多様性（重複排除）を実現するには、後述する動的Plackett–LuceやDeterminantal Point Processes (DPP) 等の発展手法との融合が必要となります。

---

## 4. 原著論文（Original Papers）

Plackett–Luceモデルは、2つの古典的な基礎研究に基づいています。

1. **Luce (1959)**:
   - **著者**: R. Duncan Luce
   - **文献**: *Individual Choice Behavior: A Theoretical Analysis*, John Wiley & Sons, 1959.
   - **概要**: 意志決定理論における「**Luce's Choice Axiom（ルースの選択公理）**」を提唱。ある集合から1つの選択肢を選ぶ確率が、アイテム固有の価値尺度（worth）の比で表されることを示しました（Softmax / Multinomial Logitモデルの理論基礎）。
2. **Plackett (1975)**:
   - **著者**: Robert L. Plackett
   - **論文**: *"The Analysis of Permutations"*, *Applied Statistics*, Vol. 24, No. 2, pp. 193–202, 1975.
   - **概要**: Luceの選択公理を、ペア比較（Bradley–Terryモデル）から3つ以上のアイテムの順列・フルランキング（Permutations）全体へ拡張。非復元抽出による連鎖的確率モデルとして定式化しました。

---

## 5. 近年の発展手法・応用研究

近年、深層学習や強化学習、Learning-to-Rank (LTR) の発展に伴い、Plackett–Luceモデルを推薦の多様性や最適化に応用する多様な手法が提案されています。

### (1) Gumbel-Top-$k$ Trick (Gumbel-Plackett Sampling)
- **関連論文**: Kool, W., van Hoof, H., & Welling, M. *"Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick"*, ICML 2019.
- **内容**: アイテムのスコア $s_i$ に標準 Gumbel ノイズ $g_i \sim \text{Gumbel}(0, 1)$ を加え、$s_i + g_i$ の値が大きい上位 $K$ 個を選ぶ操作が、**Plackett–Luce分布からの非復元抽出サンプリングと数学的に完全に等価**であることを利用した手法。
- **多様性への効果**: 重い逐次選択ループを回すことなく、GPU上で並列かつ超高速に多様なリスト（Slate）を再現性高くサンプリング可能にしました。

### (2) 端点間差別化可能なPlackett–Luceモデルと PL-Rank
- **関連論文**: Harrie Oosterhuis. *"Computationally Efficient Optimization of Plackett-Luce Ranking Models for Relevance and Fairness"*, SIGIR 2021 (PL-Rank); SIGIR 2022 (PL-Rank-3).
- **内容**: Plackett–Luceモデルでランキングを生成する際、全順列の組み合わせ数が階乗オーダーで爆発するため直接の勾配計算が困難でした。Oosterhuis らは計算量を $O(K N)$ まで削減する効率的な勾配推定アルゴリズム **PL-Rank** を開発しました。
- **多様性への効果**: 推薦モデルを訓練する段階で、NDCGやERRなどの関連性指標だけでなく、多様性指標や公平性指標（Fairness）を損失関数に組み込んで直接エンドツーエンドで最適化できるようになりました。

### (3) スレート推薦と強化学習・オフポリシー最適化
- **関連論文**: 
  - Swaminathan et al. *"Off-policy evaluation for slate recommendation"*, NeurIPS 2017.
  - Ie et al. *"SlateQ: A Tractable Reinforcement Learning Approach to Slate Recommendation"*, IJCAI 2019.
- **内容**: 複数のアイテムで構成される推薦リスト（Slate）全体を1つの行動（Action）として強化学習やContextual Banditで最適化する際、行動空間の爆発を抑えるポリシーとして Plackett–Luce モデルが採用されています。
- **多様性への効果**: 加法的な報酬設計や Inverse Propensity Scoring (IPS) と組み合わせることで、過去のログデータからオフポリシーで多様性とユーザーエンゲージメントを両立するポリシーを学習します。

### (4) 動的・文脈依存 Plackett–Luce (Conditional PL / Dynamic PL)
- **内容**: 標準PLモデルのIIA制約（すでに選ばれたアイテムとの類似性を考慮できない点）を克服するため、$k$ ステップ目の選択スコア $s_i^{(k)}$ を、選択済みアイテム $y_{<k}$ の表現ベクトルを用いて動的に変化させる手法（Attention機構やRNN, Submodularペナルティの導入）。
- **多様性への効果**: 1位に「映画A (アクション)」が選ばれた場合、2位の選択時にはアクション映画全体のスコアを減衰させ、自然に別ジャンル（コメディやサスペンスなど）を上位に引き上げる多様化が可能になります。

---

## 6. まとめ
- **Plackett–Luceモデル**は、スコアに応じた非復元抽出によってリスト（Slate）全体を生成する確率的ランキングモデルです。
- **推薦の多様性**という文脈では、従来の固定的な決定論的ソート脱却、Gumbel-Top-$k$による高速かつ多様なスレートサンプリング、PL-Rankやスレート強化学習を通じた多様性・公平性の直接最適化に活用されています。
- IIAの制限を回避するために、実務や発展研究では**温度調整 $\tau$** や **動的コンテキストモデル（Conditional PL）**、**DPP (Determinantal Point Processes) との組み合わせ**が広く利用されています。
