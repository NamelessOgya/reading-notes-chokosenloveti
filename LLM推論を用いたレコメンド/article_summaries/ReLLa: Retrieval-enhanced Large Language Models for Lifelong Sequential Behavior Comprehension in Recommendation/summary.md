# ReLLa: Retrieval-enhanced Large Language Models for Lifelong Sequential Behavior Comprehension in Recommendation

## 背景
近年、大規模言語モデル (LLM) を推薦システムに適用する試み (例: pointwise スコアリングやリスト順位付けなど) が盛んに行われており、zero-shot や few-shot 設定において高い性能を示すことが報告されている。しかし著者らは、LLM を推薦システムに用いる際の重大な課題として **「生涯シーケンシャル行動不理解問題 (Lifelong Sequential Behavior Incomprehension Problem)」** を発見した。
これは、ユーザーの長期的な行動履歴シーケンスをテキストの文脈 (コンテキスト) として LLM に入力した際、**コンテキストの長さが LLM のトークン制限に達していなくても、推薦に必要な有用な情報を抽出・理解できず、シーケンスが長くなるにつれて逆に推薦精度が低下してしまう現象**である。

Figure 1 に示すように、従来の推薦モデル (SIM) は考慮する行動シーケンスの長さ $K$ が長くなるにつれて AUC 性能が安定して向上する。しかし、オープンソースの LLM である Vicuna-13B (コンテキストウィンドウ: 2048トークン) は、シーケンス長 $K = 15$ で性能がピークに達し、それ以上に長くすると性能が急激に低下する。これは、ユーザープロファイルや履歴から特定アイテムに対する好みを推論するタスクが LLM にとって非常に高度な推論を必要とするためである。

**Figure 1: The illustration of lifelong sequential behavior incomprehension problem for LLMs.**
![Figure 1](./images/knee_point.png)

この課題を解決するため、著者らは **ReLLa** (Retrieval-enhanced Large Language Models) という新しいフレームワークを提案し、zero-shot および few-shot 設定での推薦性能を大幅に改善した。

---

## 手法
提案フレームワーク ReLLa は、主に **「意味的ユーザー行動検索 (SUBR: Semantic User Behavior Retrieval)」** と **「検索強化インストラクションチューニング (ReiT: Retrieval-enhanced Instruction Tuning)」** の2つのコア技術から構成される。

### 1. ポイントワイズスコアリングの定式化
LLM に対し、各データサンプル $x_{i}$ をテンプレートを用いてテキスト $x_{i}^{\text{text}}$ に変換する。また、バイナリラベル $y_{i} \in \{0, 1\}$ は answer token として $y_{i}^{\text{text}} \in \{\text{"Yes"}, \text{"No"}\}$ に変換する。
LLM は $x_{i}^{\text{text}}$ を入力として受け取り、次の予測トークンを予測する。そのプロセスは以下のように表される。

$$ s_{i} = \operatorname{LLM}(x_{i}^{\text{text}}) \in \mathbb{R}^{V} $$

$$ p_{i} = \operatorname{Softmax}(s_{i}) \in \mathbb{R}^{V} $$

$$ \hat{y}_{i}^{\text{text}} \sim p_{i} $$

ここで、 $V$ は語彙数であり、 $s_{i}$ は各トークンの予測ロジットである。
CTR予測などのポイントワイズスコアリングを行うため、 "Yes" の語彙インデックスを $a$ 、 "No" の語彙インデックスを $b$ とし、以下の式によってクリック確率 $\hat{y}_{i}$ を算出する。

$$ \hat{y}_{i} = \frac{\exp(s_{i, a})}{\exp(s_{i, a}) + \exp(s_{i, b})} \in (0, 1) $$

この推定スコア $\hat{y}_{i}$ はテスト時の評価（AUC や Log Loss など）のみで使用され、学習時は causal language modeling の目的関数を用いてチューニングを行う。

### 2. 意味的ユーザー行動検索 (SUBR)
zero-shot 推薦設定ではモデルのパラメータを更新できないため、データ側からアプローチして LLM が理解しやすいように入力コンテキストを「均質化」する。
従来のシーケンシャル推薦では「直近の $K$ 個の行動履歴」を用いるが、SUBR では「ターゲットアイテムに対して意味的に最も関連性の高い $K$ 個の行動」を検索して入力とする。

具体的には、以下の手順で実行する。
1. **アイテムのセマンティック埋め込み獲得**: 各アイテムの記述テキスト（タイトルやカテゴリなど）を LLM に入力し、最終層の隠れ状態を平均プーリング（average pooling）することでセマンティックベクトル $u_{t} \in \mathbb{R}^{D}$ を獲得する。
2. **PCA による次元削減とノイズ除去**: 主成分分析 (PCA) を適用し、低次元表現 $v_{t} \in \mathbb{R}^{d}$ ( $d = 512$ ) を得る。
3. **意味的類似度計算**: アイテム間のコサイン類似度を用いて関連度を算出し、ユーザー履歴の全アイテムからターゲットアイテムに最も類似する $K$ 個を抽出する。この際、抽出されたアイテムは元の時系列順序を維持したままコンテキストに配置される。

### 3. 検索強化インストラクションチューニング (ReiT)
few-shot 推薦設定においては、限られた少量の学習データで LLM をインストラクションチューニングする。しかし、単なるインストラクションチューニングでは過学習や破滅的忘却のリスクがある。
そこで ReiT では、SUBR をデータ拡張手法として用いて混合データセットを構築する。各学習サンプル $x_{i}^{\text{text}}$ に対して、SUBR を適用した検索拡張サンプル $\tilde{x}_{i}^{\text{text}}$ を作成し、元のサンプルと合わせて $2N$ サンプルの混合データセット $\mathcal{M}$ を構成する。
目的関数には以下の causal language modeling 目的関数を採用し、Parameter-Efficient Fine-Tuning (PEFT) として LoRA を適用して学習を行う。

$$ \max_{\Theta} \sum_{(x, y) \in \mathcal{M}} \sum_{j=1}^{|y|} \log P_{\Theta}(y_{j} | x, y_{<j}) $$

ここで、 $\Theta$ は LLM のパラメータ、 $y_{j}$ はテキスト出力の $j$ 番目のトークン、 $y_{<j}$ はそれ以前のトークンを示す。
このパターン拡張（パターンエンリッチメント）により、LLM のロバスト性と長期行動シーケンスに対する理解力を向上させる正則化効果が得られる。

---

## 結果

### 1. 性能評価 (RQ1)
BookCrossing (BC), MovieLens-1M (ML-1M), MovieLens-25M (ML-25M) の3つの公開データセットを用いて実験を行った。各ベースラインは全データで学習したフルショット (full-shot) 設定であるのに対し、ReLLa は 10% 未満の few-shot 設定で評価した。

#### Table 1: The dataset statistics.
| Dataset | #Users | #Items | #Samples | #Fields | #Features |
| --- | --- | --- | --- | --- | --- |
| BookCrossing | 278,858 | 271,375 | 17,714 | 10 | 912,279 |
| MovieLens-1M | 6,040 | 3,706 | 970,009 | 10 | 16,944 |
| MovieLens-25M | 162,541 | 59,047 | 25,000,095 | 6 | 280,576 |

#### Table 2: The performance of different models in zero-shot, full-shot and few-shot settings.
| Model Setting | Model | BookCrossing AUC | BookCrossing Log Loss | BookCrossing ACC | BookCrossing Rel.Impr | MovieLens-1M AUC | MovieLens-1M Log Loss | MovieLens-1M ACC | MovieLens-1M Rel.Impr | MovieLens-25M AUC | MovieLens-25M Log Loss | MovieLens-25M ACC | MovieLens-25M Rel.Impr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Zero-shot | Vicuna-7B | 0.7011 | <u>0.9357</u> | 0.5378 | 3.45% | 0.6739 | 0.9510 | 0.5644 | 4.07% | <u>0.7468</u> | 0.6348 | 0.6392 | -1.93% |
| Zero-shot | Vicuna-13B | <u>0.7176</u> | 0.9507 | <u>0.5649</u> | 1.07% | 0.6993 | 0.6291 | 0.6493 | 0.29% | **0.7503** | <u>0.6308</u> | <u>0.6427</u> | -2.39% |
| Zero-shot | ReLLa (Ours) | **0.7253$^{*}$** | **0.9277$^{*}$** | **0.5750$^{*}$** | - | **0.7013$^{*}$** | **0.6250$^{*}$** | **0.6507$^{*}$** | - | 0.7324 | **0.5858$^{*}$** | **0.7027$^{*}$** | - |
| Full-shot | DeepFM | 0.7496 | 0.5953 | 0.6760 | 1.05% | 0.7915 | 0.5484 | 0.7225 | 1.49% | 0.8189 | 0.4867 | 0.7709 | 3.52% |
| Full-shot | AutoInt | 0.7481 | 0.6840 | 0.6365 | 1.26% | 0.7929 | 0.5453 | 0.7226 | 1.31% | 0.8169 | 0.4957 | 0.7689 | 3.77% |
| Full-shot | DCNv2 | 0.7472 | 0.6816 | 0.6472 | 1.38% | 0.7931 | 0.5464 | 0.7216 | 1.29% | 0.8190 | 0.4989 | 0.7702 | 3.50% |
| Full-shot | GRU4Rec | 0.7479 | 0.5930 | 0.6777 | 1.28% | 0.7926 | 0.5453 | 0.7225 | 1.35% | 0.8186 | 0.4941 | 0.7700 | 3.55% |
| Full-shot | Caser | 0.7478 | 0.5990 | 0.6760 | 1.30% | 0.7918 | 0.5464 | 0.7206 | 1.45% | 0.8199 | 0.4865 | 0.7707 | 3.39% |
| Full-shot | SASRec | 0.7482 | 0.5934 | **0.6811** | 1.24% | 0.7934 | 0.5460 | 0.7233 | 1.25% | 0.8187 | 0.4956 | 0.7691 | 3.54% |
| Full-shot | DIN | 0.7477 | 0.6811 | 0.6557 | 1.31% | 0.7962 | 0.5425 | 0.7252 | 0.89% | 0.8190 | 0.4906 | 0.7716 | 3.50% |
| Full-shot | SIM | <u>0.7541</u> | **0.5893** | 0.6777 | 0.45% | <u>0.7992</u> | <u>0.5387</u> | <u>0.7268</u> | 0.51% | <u>0.8344</u> | <u>0.4724</u> | <u>0.7822</u> | 1.59% |
| Full-shot | CTR-BERT | 0.7448 | 0.5938 | 0.6704 | 1.71% | 0.7931 | 0.5457 | 0.7233 | 1.29% | 0.8079 | 0.5044 | 0.7511 | 4.93% |
| Full-shot | PTab | 0.7429 | 0.6154 | 0.6574 | 1.97% | 0.7955 | 0.5428 | 0.7240 | 0.98% | 0.8107 | 0.5022 | 0.7551 | 4.56% |
| Full-shot | P5 | 0.7438 | 0.6128 | 0.6563 | 1.84% | 0.7937 | 0.5478 | 0.7190 | 1.21% | 0.8092 | 0.5030 | 0.7527 | 4.76% |
| Few-shot | ReLLa (<1%) | 0.7482 | 0.6265 | 0.6800 | - | 0.7927 | 0.5475 | 0.7196 | - | 0.8352 | 0.4693 | 0.7779 | - |
| Few-shot | ReLLa (<10%) | **0.7575$^{*}$** | <u>0.5919</u> | <u>0.6806</u> | - | **0.8033$^{*}$** | **0.5362$^{*}$** | **0.7280$^{*}$** | - | **0.8477$^{*}$** | **0.4524$^{*}$** | **0.7925$^{*}$** | - |

**結果の考察：**
- **zero-shot 推薦**: ReLLa は BookCrossing および MovieLens-1M において元の Vicuna-13B を全ての評価指標で大幅に上回った（Table 2）。これは、SUBR が入力データの質を向上させ、LLM が情報抽出する難易度を効果的に下げたことを裏付けている。
- **few-shot 推薦**: ReLLa (<10%) は、**わずか 10% 未満の学習サンプル数でありながら、全データで学習した従来の CTR モデル（DeepFM, DCNv2, DIN, SIMなど）および他の言語モデルベース手法（PTab, P5など）をほぼ全てのデータセットで凌駕した**（Table 2）。例えば MovieLens-25M では、ReLLa は 65,536 サンプルのみで学習されたのに対し、SIM は約1,935万サンプルでフルショット学習されているが、ReLLa が AUC で 0.8477 を達成し、SIM (0.8344) を上回った。これにより、LLM の知識と推論能力を背景とした ReLLa の高いデータ効率性が証明された。

---

### 2. シーケンス長 $K$ の影響 (RQ2)
行動シーケンスの長さ $K$ を変化させ、推薦精度への影響を検証した。結果は Figure 6 に示されている。

- **Figure 6: The AUC performance of different models w.r.t. different length of user behavior sequence $K$.**
  ![Figure 6](./images/rella-K.png)

**結果の考察：**
- 従来の推薦モデルである SIM (full-shot) は、シーケンス長 $K$ が長くなるにつれて精度が順調に向上する。
- 一方、素の Vicuna-13B (zero-shot) は、 $K=30$ (BookCrossing) または $K=15$ (MovieLens) で精度がピークに達し、それ以上に $K$ を増やすと精度が著しく低下する。これは「生涯シーケンシャル行動不理解問題」を明確に示している。
- 提案手法 **ReLLa は、シーケンス長が長くなっても性能が低下することなく、SIM と同様に精度が向上し続ける**。これにより、ReLLa が LLM の長期コンテキスト理解力を効果的に改善したことが検証された。

---

### 3. サンプル数 $N$ の影響 (RQ3)
学習サンプルのショット数 $N$ がデータ効率性に与える影響を検証した。結果は Figure 7 に示されている。

- **Figure 7: The AUC performance of ReLLa and SIM w.r.t. different numbers of shots $N$ on three datasets.**
  ![Figure 7](./images/rella-N.png)

**結果の考察：**
- $N$ を増やすにつれて ReLLa と SIM の両方が向上するが、同一サンプル数においては ReLLa が SIM を終始大きく引き離している。
- BookCrossing において $N=128, 256$ の極端にデータが少ない設定では、SIM は CTR 予測タスクに失敗（AUCが約0.5）するが、ReLLa は 0.74 以上の高い精度を示し、LLM の持つ汎用能力を背景にした驚異的な data efficiency が実証された。

---

### 4. アブレーションスタディ (RQ4)
提案モデルの各モジュール（Mixture: 混合データ、Retrieval: SUBRによる検索、IT: インストラクションチューニング）の寄与を評価するため、アブレーションスタディを行った。

#### Table 3: The performance of different variants of ReLLa.
| Model Variant | BookCrossing AUC | BookCrossing Log Loss | BookCrossing ACC | MovieLens-1M AUC | MovieLens-1M Log Loss | MovieLens-1M ACC | MovieLens-25M AUC | MovieLens-25M Log Loss | MovieLens-25M ACC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ReLLa (Ours) | **0.7482** | <u>0.6265</u> | **0.6800** | **0.7927** | **0.5475** | **0.7196** | **0.8352** | **0.4693** | **0.7779** |
| ReLLa (w/o Mixture) | 0.7399 | **0.6002** | 0.6715 | 0.7849 | <u>0.5693</u> | 0.6985 | 0.8192 | 0.4904 | <u>0.7715</u> |
| ReLLa (w/o Retrieval) | 0.7167 | 0.9293 | 0.4898 | 0.7718 | 0.5795 | <u>0.7039</u> | 0.8174 | <u>0.4892</u> | 0.7685 |
| ReLLa ($\frac{1}{2}N$-shot) | <u>0.7415</u> | 0.6268 | 0.6462 | <u>0.7862</u> | 0.5781 | 0.6964 | <u>0.8231</u> | 0.5157 | 0.7672 |
| ReLLa (w/o IT) | 0.7253 | 0.9277 | 0.5750 | 0.7013 | 0.6250 | 0.6507 | 0.7324 | 0.5858 | 0.7027 |
| ReLLa (w/o IT & Retrieval) | 0.7176 | 0.9507 | 0.5649 | 0.6993 | 0.6291 | 0.6493 | 0.7503 | 0.6308 | 0.6427 |

**結果の考察：**
- **データ混合の重要性**: ReLLa (w/o Mixture) や ReLLa (w/o Retrieval) は、訓練時と評価時で同じデータタイプを用いるためデータ間の不整合はないが、フルバージョンの ReLLa (Ours) よりも AUC で最大 1.95% 劣る。これは、オリジナルと検索拡張データを混合して学習させる戦略の重要性を示している。
- **パターン拡張の検証**: 訓練サンプル数が同じになるように調整した ReLLa ($\frac{1}{2}N$-shot) は、ReLLa (w/o Mixture) よりも優れた AUC 性能を示した。これは、単に訓練サンプルが倍増したことよりも、混合データによる「行動パターンの多様化（正規化効果）」が過学習を防ぎ、モデルの堅牢性に大きく貢献したことを裏付けている。
- **SUBR の効果**: zero-shot 設定での比較（ReLLa (w/o IT) vs ReLLa (w/o IT & Retrieval)）において、SUBR を適用したモデルが大きく勝っており、行動系列を意味的にフィルタリングすることが LLM の理解を助ける上で本質的であることが示された。

---

### 5. ケーススタディ (RQ5)
LLM 最終層におけるターゲットアイテムと歴史アイテム間のアテンションスコアを可視化した（Figure 8）。

- **Figure 8: The case study of ReLLa on MovieLens-25M dataset.**
  ![Figure 8](./images/case-study.png)

**結果の考察：**
- Vicuna-13B (zero-shot) は、ターゲット映画 『Thor: Ragnarok』 に対し、全く関係のない 『Roman Holiday』 などにアテンションを割いてしまい、予測に失敗した。
- ReLLa (zero-shot) では SUBR により 『Iron Man 3』 などのスーパーヒーロー映画にアテンションが集まるようになったが、一部 『Kick-Ass 2』 などの Marvel 以外の無関係な映画にもアテンションが漏れていた。
- ReLLa (few-shot) では、アテンションが Marvel 製作の関連スーパーヒーロー映画に完全に集中し、正確な予測を達成した。これにより SUBR と ReiT の組み合わせが LLM に関連性を正しく捉えさせる上で有効であることが視覚的にも確認された。

---

### 6. 追加検証 (Appendix)

#### A. 異なるLLMでの検証（不理解問題の普遍性とReLLaの汎用性）
異なるサイズやアーキテクチャの LLM（Falcon, Mistral, LLaMA-2-70Bなど）を用いて、不理解問題の普遍性と ReLLa の適合性を評価した。

##### Table 4: Zero-shot AUC performance w.r.t. different sequence length $K$ for different LLMs on MovieLens-1M dataset.
| LLM | MovieLens-1M K=5 | MovieLens-1M K=10 | MovieLens-1M K=15 | MovieLens-1M K=20 | MovieLens-1M K=25 | MovieLens-1M K=30 |
| --- | --- | --- | --- | --- | --- | --- |
| Falcon-7B | **0.5906** | 0.5741 | 0.5583 | 0.5420 | 0.5468 | 0.5452 |
| Mistral-7B | 0.6566 | 0.6568 | **0.6670** | 0.6623 | 0.6612 | 0.6610 |
| Vicuna-7B | 0.6630 | 0.6586 | **0.6739** | 0.6527 | 0.6463 | 0.6412 |
| Vicuna-13B | 0.6807 | 0.6932 | **0.6993** | 0.6918 | 0.6937 | 0.6908 |
| LLaMA2-70B | 0.6259 | 0.6348 | **0.6421** | 0.6402 | 0.6339 | 0.6321 |

##### Table 5: The model compatibility of ReLLa w.r.t. different backbone LLMs on MovieLens-1M dataset with $K$=30.
| Backbone LLM | Model Setting | MovieLens-1M AUC | MovieLens-1M Log Loss | MovieLens-1M ACC |
| --- | --- | --- | --- | --- |
| SIM | few-shot (<1%) | 0.7352 | 0.6132 | 0.6743 |
| SIM | few-shot (<10%) | 0.7414 | 0.6129 | 0.6756 |
| SIM | full-shot | **0.7992** | **0.5387** | **0.7268** |
| Falcon-7B | zero-shot | 0.5906 | 0.7674 | 0.5436 |
| Falcon-7B | with SUBR | 0.5964 | 0.7709 | 0.5437 |
| Falcon-7B | with ReiT (<1%) | 0.7811 | 0.5589 | 0.7111 |
| Falcon-7B | with ReiT (<10%) | **0.7870** | **0.5658** | **0.7072** |
| Mistral-7B | zero-shot | 0.6670 | 0.7556 | 0.4793 |
| Mistral-7B | with SUBR | 0.6881 | 0.7321 | 0.5119 |
| Mistral-7B | with ReiT (<1%) | 0.7905 | 0.5488 | 0.7210 |
| Mistral-7B | with ReiT (<10%) | **0.8005** | **0.5388** | **0.7275** |
| Vicuna-7B | zero-shot | 0.6739 | 0.9510 | 0.5644 |
| Vicuna-7B | with SUBR | 0.6704 | 0.7745 | 0.5655 |
| Vicuna-7B | with ReiT (<1%) | 0.7918 | 0.5493 | 0.7196 |
| Vicuna-7B | with ReiT (<10%) | **0.8016** | **0.5365** | **0.7274** |
| Vicuna-13B | zero-shot | 0.6993 | 0.6291 | 0.6493 |
| Vicuna-13B | with SUBR | 0.7013 | 0.6250 | 0.6507 |
| Vicuna-13B | with ReiT (<1%) | 0.7927 | 0.5475 | 0.7196 |
| Vicuna-13B | with ReiT (<10%) | **0.8033** | **0.5362** | **0.7280** |

**結果の考察：**
- Table 4 より、検証した5つの LLM すべてにおいて、性能のピークが $K=5$ または $K=15$ という非常に短いシーケンス長で発生し、長くなると性能が低下した。これにより「生涯シーケンシャル行動不理解問題」が特定の LLM アーキテクチャに依存しない **普遍的な問題** であることが示された。
- Table 5 より、検証した全ての LLM で ReLLa の適用により性能が一貫して向上し、Mistral-7B、Vicuna-7B、Vicuna-13B においては、10% 未満の few-shot でフルデータ学習の SIM を上回る性能を達成した。これにより ReLLa の高い汎用性（モデル互換性）が示された。

#### B. 計算複雑度と推論速度の分析
#### Table 6: Complexity analysis on MovieLens-1M dataset.
| Model | # Total Parameter | # Trainable Parameter | Inference Time |
| --- | --- | --- | --- |
| SIM | 1.44M | 1.44M | 3.21ms |
| ReLLa | 13B | 650M | 500ms |

**結果の考察：**
- ReLLa は高い精度とデータ効率を達成する一方、推論時間は SIM (3.21ms) に対して 500ms と非常に遅い（Table 6）。これは LLM の規模に起因する本質的な制約であり、リアルタイム性が要求される推薦システムへの直接適用には課題がある。現状では、遅延への許容度が高い対話型推薦（Conversational Recommendation）などへの適用が適している。

#### C. PCA 次元数および距離指標の検証 (Ablation on SUBR)
SUBR でのハイパーパラメータの影響を検証した。

##### Table 7: Ablation study w.r.t different PCA dimensionalities for ReLLa on MovieLens-1M dataset under both zero-shot and few-shot (<1%) settings.
| Setting | PCA Dim. | MovieLens-1M AUC | MovieLens-1M Log Loss | MovieLens-1M ACC |
| --- | --- | --- | --- | --- |
| zero-shot | 512 | 0.7013 | **0.6250** | **0.6507** |
| zero-shot | 256 | **0.7064** | 0.6377 | 0.6357 |
| zero-shot | 128 | 0.7063 | 0.6379 | 0.6351 |
| zero-shot | 64 | 0.7057 | 0.6375 | 0.6349 |
| few-shot | 512 | **0.7927** | **0.5475** | **0.7196** |
| few-shot | 256 | 0.7917 | 0.5476 | 0.7098 |
| few-shot | 128 | 0.7897 | 0.5606 | 0.7099 |
| few-shot | 64 | 0.7901 | 0.5629 | 0.7099 |

##### Table 8: Ablation study w.r.t different distance metrics for ReLLa on MovieLens-1M dataset under both zero-shot and few-shot (<1%) settings.
| Setting | Distance | MovieLens-1M AUC | MovieLens-1M Log Loss | MovieLens-1M ACC |
| --- | --- | --- | --- | --- |
| zero-shot | Cosine | **0.7013** | **0.6250** | **0.6507** |
| zero-shot | L2 | 0.6975 | 0.6356 | 0.6386 |
| zero-shot | L1 | 0.6811 | 0.6388 | 0.6339 |
| few-shot | Cosine | **0.7927** | **0.5475** | **0.7196** |
| few-shot | L2 | 0.7872 | 0.5762 | 0.6944 |
| few-shot | L1 | 0.7833 | 0.5598 | 0.7119 |

**結果の考察：**
- PCA 次元数は 512 が最も良い性能を示した（Table 7）。次元が低すぎると情報損失により精度が低下する。
- 距離指標では、高次元空間において「次元の呪い」の影響を受けにくいコサイン距離（Cosine）が、L1 および L2 距離に対して最も高い性能を示した（Table 8）。

#### D. 不理解問題の潜在的要因と検索による「均質化」の証明
著者らは、不理解問題の要因を **「ユーザー行動系列の高い異質性（Heterogeneity）を LLM が処理しきれないこと」** と仮説を立てた。系列長 $K$ が伸びるほど、多様なジャンルのアイテムが混在して異質性が高まり、LLM の preference 推論を妨げる。
これを検証するため、系列に含まれるユニークな映画ジャンル数を「異質性スコア（Heterogeneity Score）」として定義し、直近履歴 (Top Recent) と SUBR 適用履歴 (Top Relevant) を比較した。

##### Table 9: The averaged heterogeneity scores of two sequence types w.r.t. different length $K$.
| Seq. Type | MovieLens-1M K=5 | MovieLens-1M K=10 | MovieLens-1M K=15 | MovieLens-1M K=20 | MovieLens-1M K=25 | MovieLens-1M K=30 |
| --- | --- | --- | --- | --- | --- | --- |
| Top Recent (Origin) | 2.91 | 4.19 | 5.09 | 5.80 | 6.39 | 6.90 |
| Top Relevant (Retrieval) | 2.44 | 3.37 | 4.01 | 4.51 | 4.94 | 5.32 |

**結果の考察：**
- Table 9 より、直近履歴はシーケンス長 $K$ が長くなるほど異質性スコアが 6.90 にまで急増する。これが LLM の理解力を超える原因と考えられる。
- 一方、SUBR（意味的検索）を適用した系列では、ターゲットアイテムに類似するアイテムが集まるため、異質性スコアが有意に低下する（ $K=30$ で 5.32 ）。
- これにより、**検索技術の本質は「行動系列の均質化 (Homogenization)」であり、不要な異質ノイズを排除することで、LLM が長期的な依存関係を正確に処理できるようサポートしていること**が実証された。

---

## 補足図版（プロンプト・詳細デザイン）

- **Figure 2: Illustration of textual input-output pair.**
  ![Figure 2](./images/prompt_illustration.png)

- **Figure 3: Illustration of semantic user behavior retrieval (SUBR).**
  ![Figure 3](./images/semantic_retrieval.png)

- **Figure 4: Illustration of descriptive text for an item (movie).**
  ![Figure 4](./images/item_description.png)

- **Figure 5: Illustration of retrieval-enhanced instruction tuning (ReiT).**
  ![Figure 5](./images/retrieval-enhanced_instruction_tuning.png)

- **Figure 9: Examples of hard prompt templates for three datasets without SUBR.**
  ![Figure 9](./images/prompt_simple.png)

- **Figure 10: Examples of hard prompt templates for three datasets with SUBR.**
  ![Figure 10](./images/prompt_ret.png)

- **Figure 11: Examples of hard prompt templates of item descriptions for three datasets.**
  ![Figure 11](./images/item_description-all.png)
