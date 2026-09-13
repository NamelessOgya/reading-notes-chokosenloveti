# The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers

**arXiv:** 2607.25346  
**著者:** Zhe Xu, Prachi Agrawal, Kavosh Asadi, Tianyi Chen, Carl Hu, Justin Johnson, Wuwei Lan, Mingfu Liang, Xi Liu, TIK ON LUI, Oladipo Ositelu, Sandeep Pandey, Ankit Peshin, Feng Qi, Anil Ramakrishna, Kaushik Rangadurai, Frank Shyu, Luke Simon, Yang Yang, Chiyu Zhang（Meta）  
**発表:** 2026年7月  

---

## 一言まとめ
**LLMを生成器ではなく識別的な意味表現バックボーン（Discriminative Semantic Representation Backbone）として活用し、高効率な2タワー（Two-Tower）検索アーキテクチャを再活性化**したMeta社の研究。  
共有エンコーダ、EOSプーリング、Yes/No＋ユーザー文脈付き次トークン予測（NTP）を備えたCross-Encoder教師からの知識蒸留（CE2TT）、ユーザータワーのCoconut風潜在推論（Latent Reasoning）を導入。  
0.6Bのモデルサイズで8Bの最新生成型推薦モデル（OneRec-Think）を凌駕。  
Meta社内本番システムにおいてDLRMのわずか0.5%のデータで同等精度、日次陳腐化（Staleness）への圧倒的耐性を実証した。

---

## 背景

大規模言語モデル（LLM）は、高度な意味理解力、指示追従性、オープンワールド知識により、推薦システム（Recommender Systems）の領域でも急速に活用が進んでいる。特に近年は、アイテムタイトルや離散的なセマンティックID、ランキング候補リストを言語モデルに直接予測・生成させる「**生成型推薦（Generative Retrieval / Text-to-Text Recommendation）**」（P5, TIGER, OneRec, OneRec-Think, TALLRec 等）が大きな注目を集めてきた。

しかし、生成型推薦モデルを大規模な本番環境の第一段階検索（First-Stage Candidate Retrieval）に導入する際には、以下の**3つの致命的な実用上のボトルネック**が存在する：

1. **極めて高い配信コストと推論レイテンシ**:
   - トークンごとの自己回帰的デコーディング（Autoregressive Decoding）を必要とするため、出力系列長に比例してレイテンシが増大し、大規模な並列ベクトル検索（ANN）のようなスケーラビリティが得られない。
2. **接地（Grounding）の失敗とハルシネーション**:
   - 生成されたテキストトークンやID系列が、実在する有効なカタログアイテムに正確に対応しない（存在しないアイテムIDを生成してしまう）問題が頻発する。
3. **トークンとアイテムの分離による誤差連鎖**:
   - 生成型検索ではモデル外部で「トークン $\to$ アイテム」の変換を行うため、生成時のわずかなズレや予測誤差が下流のアイテム同定へと連鎖的に波及し、性能低下を招く。

これに対し、産業界で長年採用されてきた**古典的な2タワー（Two-Tower / Dual-Encoder）アーキテクチャ**は、ユーザーとアイテムを独立に密ベクトルへとエンコードするため、**全アイテムの埋め込みをオフラインで事前計算・インデックス化し、オンラインでは近似最近傍探索（ANN）によりミリ秒単位で高速検索できる**という決定的な運用優位性を持つ。

著者らは、**「LLMの深い表現力を生成型としてではなく、識別的な意味表現モデルとして活用し、2タワー構造の効率性とスケーラビリティを維持したままSOTA性能を達成できるか？」** という問いを立て、LLMネイティブな2タワー検索フレームワークを構築・検証した。

---

## 手法

提案手法は、高表現力な **Cross-Encoder（CE）教師モデル** の強化と、高効率な **Two-Tower（TT）生徒モデル** への知識蒸留・推論強化の2つの軸から構成される。

![Figure 1: Proposed LLM-native recommendation framework overview](./images/overview.png)

### 1. Cross-Encoder (CE) 教師モデル

Cross-Encoderはユーザーとアイテムのテキストを結合して完全なSelf-Attentionで密に相互作用させるため表現力が高いが、ペアごとの推論コストが高く検索には直接使えない。

- **Yes/No 出力ヘッドによる関連度スコアリング（推論・判定時の本タスク）**:
  - ユーザーテキスト $x_u$ とアイテムテキスト $x_i$ を結合したプロンプト $x_{u,i}^{\mathrm{yn}} = \operatorname{Prompt}(x_u, x_i)$ を入力：
    ```text
    [ユーザー文脈 x_u] (履歴・嗜好) + [アイテム情報 x_i] (詳細) + "Answer with yes or no:"
    ```
  - **推論時（蒸留用スコア計算時）の挙動**:
    - プロンプトをLLMに1回フォワード（Prefill）し、末尾位置における「yes」と「no」の次トークン予測ロジット値（$\ell_{\mathrm{yes}}, \ell_{\mathrm{no}}$）の差分をスカラーの関連度スコアとして取得：

$$ s_{\mathrm{CE}}(u,i) = \ell_{\mathrm{yes}}(u,i) - \ell_{\mathrm{no}}(u,i) $$

- **ユーザー文脈付き次トークン予測（NTP）補助損失（学習時のみの補助タスク）**:
  - **役割**: 学習時にLLMの言語モデリング能力を活用し、推薦ドメイン特有の意味理解と内部表現力を鍛えるための**補助タスク（Auxiliary Loss）**。
  - **重要**: **推論時には全く使用しない**（テキスト生成は行わない）。学習時（Teacher Forcing）にのみ、ユーザー側の文脈 $x_u$ に条件付けられた状態でプロンプト内のアイテムテキスト $x_i = [t_{i,1}, \dots, t_{i,L_i}]$ の各トークンに対する自己回帰予測損失を計算：

$$ \mathcal{L}_{\mathrm{ntp}} = -\sum_{(u,i)\in\mathcal{S}} \sum_{\ell=1}^{L_i-1} \log p_{\theta} \left( t_{i,\ell+1} \mid x_{u}, t_{i,1}, \ldots, t_{i,\ell} \right) $$

- **CE教師の学習総合損失**:
  - 末尾の Yes/No ロジット差 $s_{\mathrm{CE}}$ による対照学習損失（主タスク）と、アイテムテキストのNTP言語モデル損失（補助タスク）を重み付け加算：

$$ \mathcal{L}_{\mathrm{CE}} = \mathcal{L}_{\mathrm{con}}(s_{\mathrm{CE}}) + \lambda_{\mathrm{ntp}}\mathcal{L}_{\mathrm{ntp}} $$

  （$\lambda_{\mathrm{ntp}} = 0.5$、$\mathcal{L}_{\mathrm{con}}$ はIn-batch負例を用いた対照学習損失）

---

### 2. Cross-Encoder から Two-Tower への知識蒸留 (CE2TT Distillation)

Cross-Encoder（教師）はユーザーとアイテムの全トークン間で密なSelf-Attentionを行うため極めて高いマッチング精度を誇るが、ペアごとの計算が必要なため数百万件規模の候補検索（Retrieval）には計算コスト上使用できない。一方、Two-Tower（生徒）はアイテムベクトルをオフラインで事前計算でき超高速なMIPS検索が可能だが、ユーザーとアイテム間のきめ細やかな相互作用を捉えにくい。

そこで本手法では、**Cross-Encoderのきめ細やかなランキング選好（相対的スコア分布）をTwo-Tower生徒モデルへ転移する「候補セットスコア分布蒸留（Candidate-Set Score-Distribution Distillation）」** を採用している。

#### (1) 候補セット上でのソフトスコア分布の定式化

各ユーザー $u$ に対し、正例アイテムおよび負例アイテムからなる候補セット $\mathcal{C}_{u}$ を構成する。この候補セット上で、CE教師モデルが出力するスコア $s_{\mathrm{CE}}(u,i)$ および TT生徒モデルが出力するスコア $s_{\mathrm{TT}}(u,i) = \mathbf{z}_{u}^\top \mathbf{z}_{i}$ にSoftmax関数（温度パラメータ $T$ ）を適用し、確率分布へと変換する。

- **CE教師の候補セットスコア分布**:

$$ q_{\mathrm{CE}}(i \mid u, \mathcal{C}_{u}) = \frac{\exp(s_{\mathrm{CE}}(u,i) / T)}{\sum_{j \in \mathcal{C}_{u}} \exp(s_{\mathrm{CE}}(u,j) / T)} $$

- **TT生徒の候補セットスコア分布**:

$$ p_{\theta}^{\mathrm{TT}}(i \mid u, \mathcal{C}_{u}) = \frac{\exp(s_{\mathrm{TT}}(u,i) / T)}{\sum_{j \in \mathcal{C}_{u}} \exp(s_{\mathrm{TT}}(u,j) / T)} $$

ここで $T$ は蒸留温度（Distillation Temperature、実験では $T = 0.5 \sim 1.0$ を使用）であり、スコアの相対的な差を滑らかにして教師の暗黙的な選好のグラデーション（どれがどれくらい良いか）を生徒へ伝えやすくする役割を果たす。

#### (2) 蒸留損失関数（KLダイバージェンス）

教師のスコア分布 $q_{\mathrm{CE}}$ と生徒のスコア分布 $p_{\theta}^{\mathrm{TT}}$ との間のカルバック・ライブラー情報量（KL Divergence）を最小化する。

$$ \mathcal{L}_{\mathrm{KD}} = T^{2} \sum_{u} \operatorname{KL} \left( q_{\mathrm{CE}}(\cdot \mid u, \mathcal{C}_{u}) \,\|\, p_{\theta}^{\mathrm{TT}}(\cdot \mid u, \mathcal{C}_{u}) \right) $$

（※ $T^2$ は Hinton の知識蒸留における標準的なスケーリング係数）

#### (3) Two-Tower 生徒モデルの総合学習目標

生徒モデルは、正例アイテムとの対照学習損失（Contrastive Loss: $\mathcal{L}_{\mathrm{con}}$）と、上記のCE教師からの蒸留損失 $\mathcal{L}_{\mathrm{KD}}$ を同時に最適化する。

$$ \mathcal{L}_{\mathrm{TT}} = \mathcal{L}_{\mathrm{con}}(s_{\mathrm{TT}}) + \lambda_{\mathrm{KD}} \mathcal{L}_{\mathrm{KD}} $$


---

### 3. Two-Tower (TT) 生徒モデルのアーキテクチャ

- **共有エンコーダ（Shared User-Item Encoder）**:
  - ユーザー側とアイテム側で独立したエンコーダを持たず、同一のLLM（Qwen3-0.6B）パラメータ $\theta$ を共有：

$$ \mathbf{z}_{u} = f_{\theta}(x_{u}), \qquad \mathbf{z}_{i} = f_{\theta}(x_{i}) $$

  これによりユーザーとアイテムが同一の意味空間に射影され、パラメータ効率とアライメントが向上。
- **EOS トークンプール（EOS Pooling）**:
  - 因果アテンション（Causal Attention）の特性上、系列の末尾に追加された `<EOS>` トークンの隠れ状態が系列全体の情報を集約するため、平均プーリング（Mean Pooling）よりも優れた表現力を発揮。
- **ドメイン間転移学習（Cross-Dataset Transfer Learning）**:
  - 複数ドメインの推薦データセット全体で事前にMid-training（事前対照学習）を行い、共通の推薦行動・テキストパターンを獲得した後に目的データセットでファインチューニング。
- **ユーザータワーのCoconut風 潜在推論（Latent Reasoning in User Tower）**:
  - アイテム側は標準のEOSプーリング $\mathbf{z}_{i} = f_{\theta}(x_{i})$ のままとし、**オフライン事前計算性を完全に維持**。
  - 履歴が多く複雑なユーザー側のみ、LLMの最終隠れ状態 $\mathbf{c}_{u} = \mathbf{H}_{u}^{(0)}[-1]$ を連続的な思考トークン（Latent Token）として入力末尾に追加し、もう1ステップの潜在推論パスを実行して最終ベクトル $\mathbf{z}_{u} = \mathbf{H}_{u}^{(1)}[-1]$ を取得。

---

### 4. 本番配信システムアーキテクチャ (System Architecture)

![Figure 2: Serving architecture for LLM-Native Two Tower](./images/polar_arch.png)

- **アイテムパイプライン（ニアライン）**:
  - アイテム作成・更新時に特徴量をプロンプト化し、非同期でLLMエンコードしてベクトルインデックスに登録。
- **ユーザーパイプライン（ニアライン）**:
  - ユーザーの最新行動履歴を集約し、User LLMで定期的に埋め込みを再計算して分散KVストアにキャッシュ。
- **オンライン検索層**:
  - リクエスト時にKVストアからユーザー埋め込みをミリ秒で取得し、アイテムインデックスに対して圧縮空間ANN検索（MIPS）を実行して候補を即座に絞り込み。

---

## 結果

### Table 1: 公開ベンチマーク（Amazon 3データセット）におけるSOTA比較

※ベースライン結果は OneRec-Think (ORT, 8B) から引用。ORTは **Qwen3-8B** を使用しているのに対し、提案手法（Ours）はすべて **Qwen3-0.6B** を使用。太字は全体1位、下線は2位、括弧内はORTに対する相対変化率。

| Model | Beauty R@5 | Beauty R@10 | Beauty N@5 | Beauty N@10 | Sports R@5 | Sports R@10 | Sports N@5 | Sports N@10 | Toys R@5 | Toys R@10 | Toys N@5 | Toys N@10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| BERT4Rec | 0.0232 | 0.0396 | 0.0146 | 0.0199 | 0.0102 | 0.0175 | 0.0065 | 0.0088 | 0.0215 | 0.0332 | 0.0131 | 0.0168 |
| HGN | 0.0319 | 0.0536 | 0.0196 | 0.0266 | 0.0183 | 0.0313 | 0.0109 | 0.0150 | 0.0326 | 0.0517 | 0.0192 | 0.0254 |
| GRU4Rec | 0.0395 | 0.0584 | 0.0265 | 0.0326 | 0.0190 | 0.0312 | 0.0122 | 0.0161 | 0.0330 | 0.0490 | 0.0228 | 0.0279 |
| SASRec | 0.0402 | 0.0607 | 0.0254 | 0.0320 | 0.0199 | 0.0301 | 0.0106 | 0.0141 | 0.0448 | 0.0626 | 0.0300 | 0.0358 |
| TIGER | 0.0405 | 0.0623 | 0.0267 | 0.0337 | 0.0215 | 0.0347 | 0.0137 | 0.0179 | 0.0337 | 0.0547 | 0.0209 | 0.0276 |
| HSTU | 0.0424 | 0.0652 | 0.0280 | 0.0353 | 0.0268 | 0.0343 | 0.0173 | 0.0226 | 0.0366 | 0.0566 | 0.0245 | 0.0309 |
| ReaRec | 0.0450 | 0.0704 | 0.0262 | 0.0344 | 0.0214 | 0.0332 | 0.0116 | 0.0154 | 0.0523 | 0.0764 | 0.0298 | 0.0376 |
| OneRec-Think (ORT, 8B) | <u>0.0563</u> | 0.0791 | **0.0398** | <u>0.0471</u> | 0.0288 | 0.0412 | <u>0.0199</u> | 0.0239 | 0.0579 | 0.0797 | <u>0.0412</u> | 0.0482 |
| **Ours (TT, 0.6B)** | 0.0473 (-16.0%) | <u>0.0825</u> (+4.3%) | 0.0267 (-32.9%) | 0.0380 (-19.3%) | <u>0.0320</u> (+11.1%) | <u>0.0542</u> (+31.6%) | 0.0193 (-3.0%) | <u>0.0264</u> (+10.5%) | <u>0.0644</u> (+11.2%) | <u>0.1078</u> (+35.3%) | 0.0366 (-11.2%) | <u>0.0506</u> (+5.0%) |
| **Ours (CE, 0.6B)** | **0.0575** (+2.1%) | **0.0957** (+21.0%) | <u>0.0351</u> (-11.8%) | **0.0473** (+0.4%) | **0.0438** (+52.1%) | **0.0677** (+64.3%) | **0.0289** (+45.2%) | **0.0365** (+52.7%) | **0.0829** (+43.2%) | **0.1223** (+53.5%) | **0.0555** (+34.7%) | **0.0682** (+41.5%) |

#### 考察
- **Cross-Encoder（Ours CE, 0.6B）**: 12の評価指標中10個で全体首位を独占。8BのOneRec-Thinkに対してSportsのR@10で **+64.3%**、ToysのR@10で **+53.5%** という圧倒的な精度向上を達成。
- **Two-Tower（Ours TT, 0.6B）**: 8BのOneRec-Thinkに対し、R@10においてBeautyで **+4.3%**、Sportsで **+31.6%**、Toysで **+35.3%** 上回り、効率的なベクトル検索モデルでありながら巨大生成型推薦モデルに勝利。

---

### Table 2: Cross-Encoder 教師モデルのバリアント比較 (Performance comparison of CE teacher variants)

| Dataset | Variant | R@5 | R@10 | N@5 | N@10 |
|---|---|:---:|:---:|:---:|:---:|
| Beauty | projection head | 0.0509 | 0.0862 | 0.0307 | 0.0420 |
| Beauty | yes/no head | 0.0535 | 0.0914 | 0.0328 | 0.0450 |
| Beauty | **yes/no + NTP** | **0.0575** | **0.0957** | **0.0351** | **0.0473** |
| Sports | projection head | 0.0391 | 0.0618 | 0.0245 | 0.0317 |
| Sports | yes/no head | 0.0317 | 0.0550 | 0.0195 | 0.0269 |
| Sports | **yes/no + NTP** | **0.0438** | **0.0677** | **0.0289** | **0.0365** |
| Toys | projection head | 0.0757 | 0.1134 | 0.0492 | 0.0614 |
| Toys | yes/no head | 0.0814 | 0.1203 | 0.0517 | 0.0643 |
| Toys | **yes/no + NTP** | **0.0829** | **0.1223** | **0.0555** | **0.0682** |

#### 考察（補助タスク NTP の有無に関するアブレーション分析）
- **`yes/no head` 単体（NTP補助タスクなし）の不安定性**:
  - `projection head`（通常の線形射影ヘッド）と比較すると、`yes/no head` は Beauty や Toys では精度が向上するものの、**Sports では全4指標で大幅に悪化（R@10 が 0.0618 $\to$ 0.0550 に低下）**しており、言語モデルの Yes/No 判定信号単体ではデータセットによって過学習や性能のバラつきが生じることが確認された。
- **`yes/no + NTP`（NTP補助タスクあり）による一貫したSOTA達成**:
  - ユーザー文脈付き NTP 補助損失を加えることで、この不安定性が完全に解消され、**3データセット・全12指標のすべてで一貫して最高スコア（SOTA）を記録**した。
  - 特に Sports においては、`yes/no head` 単体から R@10 が $0.0550 \to 0.0677$（**+23.1% の劇的改善**）を達成。Beauty でも $0.0914 \to 0.0957$（+4.7%）、Toys でも $0.1203 \to 0.1223$（+1.7%）と確実に向上した。
- **補助タスクが効くメカニズム**:
  - 末尾の「Yes/No」という1スカラーの分類対照信号だけでは、LLMの持つ豊かな言語表現空間が狭い分類タスクに歪められてしまう。
  - 途中のアイテムテキストに対して「このユーザーの好みの文脈において、なぜこのアイテムテキスト（名称や属性）が続くのか」という自己回帰予測タスクを学習時（Teacher Forcing）に同時実行させることで、**推薦ドメイン特有の語彙・属性とユーザー嗜好の関連性を正則化・補完的に深く学習できた**と結論づけられている。このため、蒸留用の教師モデルとして `yes/no + NTP` が最終採用された。

---

### Table 3: Two-Tower 生徒モデルの Leave-one-out アブレーション (Leave-one-out ablation of the TT student)

※全バリアントが Shared+EOS を使用。完全版（Full）から各コンポーネント（TL: 転移学習, CE2TT: 蒸留, Latent: 潜在推論）を1つずつ除去して評価。

| Dataset | Variant | R@5 | R@10 | N@5 | N@10 |
|---|---|:---:|:---:|:---:|:---:|
| Beauty | **Full** | **0.0473** | **0.0825** | 0.0267 | **0.0380** |
| Beauty | w/o TL | 0.0431 | 0.0812 | 0.0241 | 0.0363 |
| Beauty | w/o CE2TT | 0.0427 | 0.0715 | 0.0252 | 0.0345 |
| Beauty | w/o Latent | 0.0463 | 0.0794 | **0.0269** | 0.0374 |
| Sports | **Full** | **0.0320** | **0.0542** | **0.0193** | **0.0264** |
| Sports | w/o TL | 0.0300 | 0.0515 | 0.0174 | 0.0243 |
| Sports | w/o CE2TT | 0.0258 | 0.0417 | 0.0160 | 0.0211 |
| Sports | w/o Latent | 0.0308 | 0.0530 | 0.0185 | 0.0257 |
| Toys | **Full** | 0.0644 | **0.1078** | 0.0366 | **0.0506** |
| Toys | w/o TL | 0.0604 | 0.1050 | 0.0346 | 0.0490 |
| Toys | w/o CE2TT | 0.0626 | 0.0992 | **0.0383** | 0.0502 |
| Toys | w/o Latent | **0.0650** | 0.1063 | 0.0370 | 0.0503 |

#### 各バリアントの定義と説明

本実験（Leave-one-out Ablation）は、完全版モデル（Full）から特定の改善機能を **「1つだけ除去（without）して、その機能が精度向上にどれだけ寄与しているか」** を検証したものである（全バリアントで共有エンコーダ Shared と EOS プーリングは共通適用）。

- **`Full`（完全版）**:
  すべての改善技術（Shared + EOS + **TL** + **CE2TT** + **Latent**）を統合したモデル。すべてのデータセットにおいて最も安定して最高の R@10 および N@10 を達成。
- **`w/o TL`（without Transfer Learning: ドメイン間転移学習を行わない構成）**:
  - **内容**: 目的のデータセット（例: Beauty）でファインチューニングする前に、利用可能な全推薦データセット（Beauty, Sports, Toysなど）をまとめて共通エンコーダで事前に学習（**Mid-training**）させる工程をスキップし、**対象データセットのデータのみで直接ゼロから学習** させたモデル。
  - **効果・考察**: 除去するとすべてのデータセットで R@10 や N@10 が低下。単一カテゴリのデータだけで閉じるより、複数ドメインの行動・テキストパターンを事前に転移学習しておくことがモデルの汎化性能を確実に高めている。
- **`w/o CE2TT`（without Cross-Encoder to Two-Tower Distillation: 知識蒸留を行わない構成）**:
  - **内容**: Cross-Encoder教師モデルからの候補セットスコア分布蒸留（$\mathcal{L}_{\mathrm{KD}}$）を行わず、通常の対照学習損失（$\mathcal{L}_{\mathrm{con}}$）のみでTwo-Towerモデルを学習させたモデル。
  - **効果・考察**: **モデル全体の精度低下が最も顕著** であり、R@10 が Beauty で -13.3%、Sports で -23.1%、Toys で -8.0% 激減。Cross-Encoderが捉えるきめ細やかな相互作用シグナルをTwo-Towerへ蒸留することが、推薦検索性能の決定打（最重要コンポーネント）であることを実証している。
- **`w/o Latent`（without Latent Reasoning: ユーザータワーの潜在推論を行わない構成）**:
  - **内容**: 複雑なユーザー履歴側に対して最終隠れ状態 $\mathbf{c}_u$ を思考トークンとして再入力し、もう1ステップ内部推論（フォワードパス）を実行する潜在推論をスキップ。**ユーザー側もアイテム側と全く同様に、通常の1回のフォワードパス（EOSプーリング）のみでベクトルを出力** させたモデル。
  - **効果・考察**: 除去すると全データセットで R@10 や N@10 がわずかに低下。アイテム側はオフライン事前計算のため1パスのまま高速性を維持しつつ、情報量の多いユーザー側だけ1ステップ深く思考させて表現を洗練させる工夫が、検索精度の底上げに確実に寄与している。

#### 考察まとめ
- **CE2TT蒸留の寄与が圧倒的に最大**: 蒸留の有無が検索品質のベースラインを大きく左右する。
- **TL（転移学習）とLatent（潜在推論）の補完的効果**: 蒸留ほど劇的ではないものの、どちらを除去しても全データセットで R@10 が低下しており、両者を組み合わせた `Full` 構成が最も頑健で高い検索品質（Top-10の網羅性・適合度）を提供する。

---

### Table 4: 社内本番システムにおける配信効率化手法とQPS向上 (Improving serving efficiency for LLM-native TT without hurting NE)

| Technique | QPS Gain |
|---|:---:|
| Numerical Features FSQ Compression | +19.7% |
| Depth pruning | +10.6% |
| Static vocabulary pruning | +2.0% |
| Post-training Quantization (FP8) | +13.6% |

#### 考察
- 連続特徴量のFSQ量子化（64 bin）によりトークン長を大幅に圧縮し **QPS +19.7%**（NEも+0.3%改善）。
- Transformer層のプルーニング（28層中3層削除）で **QPS +10.6%**、FP8量子化で **QPS +13.6%**（精度劣化わずか0.003%）を達成。

---

### Table 5: モデル陳腐化（Staleness）耐性の検証 (Staleness evaluation on internal dataset)

※ $ds+0$ 時点のデータで学習後、パラメータ更新なしで後続日程（$ds+1, ds+2, ds+3$）を評価。毎日再学習される運用DLRMとの相対NE比較（負値＝劣化、正値＝改善）。

| Model | $ds+1$ (NE) | $ds+2$ | $ds+3$ |
|---|:---:|:---:|:---:|
| DLRM (production, daily retrained) | baseline | baseline | baseline |
| Frozen DLRM (no update) | baseline | -2.68% | -4.30% |
| **Frozen LLM-Native CE (no update)** | **+2.25%** | **+2.21%** | **+2.23%** |

#### 考察
- 従来のDLRMは日々のID分布変化に極めて弱く、学習を停止すると3日で -4.30% 性能が崩壊する。
- 一方、**LLM-Nativeモデルは不変の自然言語語彙・意味表現に接地しているため、未更新のままでも+2.2%以上の高い優位性を完全に維持**。モデル再学習の頻度を大幅に削減できる運用上の絶大なメリットを証明。

---

### Table 6: データスケーリング特性 (Data scaling on internal dataset)

※ $1\times$ データ時点の性能を基準とし、データ量を2倍・3倍に拡大した際の相対NE改善幅。

| Model | $2\times$ Data | $3\times$ Data |
|---|:---:|:---:|
| DLRM (production) | +1.30% | +1.80% |
| **LLM-native CE** | **+1.59%** | **+2.19%** |

#### 考察
- LLM-Nativeモデルは、DLRMよりも急峻なスケーリングカーブ（$3\times$ データで +2.19% vs +1.80%）を示し、データを増やすほど従来型モデルとの性能差が拡大する。

---

### Table 7: モデル容量スケーリングのポテンシャル (Headroom Study: Gains from Model Scaling)

| Variant | NE gain |
|---|:---:|
| LLM-Native CE 0.6B | baseline |
| + Latent reasoning (residual-stream) | +0.41% |
| + Mixtral MoE (8 experts, top-2) | +0.91% |
| **LLM-Native CE 4B** | **+1.90%** |

---

### Table 8: Amazon公開データセット統計 (Statistics of the three processed Amazon review datasets)

| Dataset | # Users | # Items | Mean Len. | Median Len. |
|---|:---:|:---:|:---:|:---:|
| Beauty | 22,363 | 12,101 | 8.87 | 6 |
| Sports and Outdoors | 35,598 | 18,357 | 8.32 | 6 |
| Toys and Games | 19,412 | 11,924 | 8.63 | 6 |

---

### Table 9: Cross-Encoder 教師モデル ハイパーパラメータ (Cross-encoder hyperparameters)

| Hyperparameter | Value |
|---|:---:|
| Negatives per positive | 31 |
| NTP loss weight $\lambda_{\mathrm{ntp}}$ | 0.5 |
| Epochs | 10 |
| GPUs | $4\times$ A100-80GB |
| Per-GPU batch | 32 |
| Effective batch | 128 |
| Learning rate | $2\times10^{-5}$ |
| Weight decay | 0.01 |
| Warmup ratio | 0.1 |
| Max length (query / item) | 512 / 128 |
| Precision | bf16 |
| Seed | 42 |

---

### Table 10: Two-Tower 生徒モデル ハイパーパラメータ (Two-tower retriever hyperparameters)

| Hyperparameter | Value |
|---|:---:|
| Embedding dimension | raw 1024-d |
| Similarity / temperature $\tau$ | dot product / 0.07 |
| **【Pre-training & fine-tuning (transfer)】** | |
| GPUs | $4\times$ A100-80GB |
| Per-GPU batch | 32 |
| Epochs | 10 |
| Learning rate | $2\times10^{-5}$ |
| **【CE $\to$ TT distillation】** | |
| GPUs | $8\times$ A100-80GB |
| Per-GPU batch | 32 |
| In-batch negatives | 31 |
| Teacher candidates $K$ | 50 |
| Epochs | 5 |
| Learning rate | $1\times10^{-5}$ |
| KD loss weight $\lambda_{\mathrm{KD}}$ | 0.2 |
| Distill temperature $T$ | 1.0 (Beauty) / 0.5 (Sports, Toys) |
| **【Shared】** | |
| Optimizer | AdamW (wd 0.01, warmup 0.1) |
| Max length (query / item) | 512 / 128 |
| Precision | bf16 |
| Seed | 42 |

---

### Table 11: Two-Tower 生徒モデル 全組み合わせアブレーション結果 (Complete two-tower ablation)

※バニラ基準（1行目）は個別エンコーダ＋Mean Pooling。それ以降はすべて Shared+EOS を使用。

| Dataset | Shared+EOS | TL | CE2TT | Latent | R@5 | R@10 | N@5 | N@10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Beauty | - | - | - | - | 0.0214 | 0.0389 | 0.0125 | 0.0180 |
| Beauty | \checkmark | - | - | - | 0.0415 | 0.0672 | 0.0253 | 0.0337 |
| Beauty | \checkmark | - | \checkmark | - | 0.0429 | 0.0800 | 0.0241 | 0.0360 |
| Beauty | \checkmark | \checkmark | - | - | 0.0430 | 0.0714 | 0.0260 | 0.0351 |
| Beauty | \checkmark | \checkmark | \checkmark | - | 0.0463 | 0.0794 | **0.0269** | 0.0374 |
| Beauty | \checkmark | - | - | \checkmark | 0.0425 | 0.0711 | 0.0251 | 0.0343 |
| Beauty | \checkmark | - | \checkmark | \checkmark | 0.0431 | 0.0812 | 0.0241 | 0.0363 |
| Beauty | \checkmark | \checkmark | - | \checkmark | 0.0427 | 0.0715 | 0.0252 | 0.0345 |
| Beauty | \checkmark | \checkmark | \checkmark | \checkmark | **0.0473** | **0.0825** | 0.0267 | **0.0380** |
| Sports | - | - | - | - | 0.0054 | 0.0109 | 0.0033 | 0.0050 |
| Sports | \checkmark | - | - | - | 0.0205 | 0.0347 | 0.0131 | 0.0177 |
| Sports | \checkmark | - | \checkmark | - | 0.0298 | 0.0510 | 0.0175 | 0.0243 |
| Sports | \checkmark | \checkmark | - | - | 0.0261 | 0.0426 | 0.0166 | 0.0219 |
| Sports | \checkmark | \checkmark | \checkmark | - | 0.0308 | 0.0530 | 0.0185 | 0.0257 |
| Sports | \checkmark | - | - | \checkmark | 0.0223 | 0.0387 | 0.0132 | 0.0184 |
| Sports | \checkmark | - | \checkmark | \checkmark | 0.0300 | 0.0515 | 0.0174 | 0.0243 |
| Sports | \checkmark | \checkmark | - | \checkmark | 0.0258 | 0.0417 | 0.0160 | 0.0211 |
| Sports | \checkmark | \checkmark | \checkmark | \checkmark | **0.0320** | **0.0542** | **0.0193** | **0.0264** |
| Toys | - | - | - | - | 0.0294 | 0.0489 | 0.0175 | 0.0237 |
| Toys | \checkmark | - | - | - | 0.0600 | 0.0968 | 0.0367 | 0.0487 |
| Toys | \checkmark | - | \checkmark | - | 0.0614 | 0.1049 | 0.0353 | 0.0493 |
| Toys | \checkmark | \checkmark | - | - | 0.0563 | 0.0928 | 0.0332 | 0.0450 |
| Toys | \checkmark | \checkmark | \checkmark | - | **0.0650** | 0.1063 | 0.0370 | 0.0503 |
| Toys | \checkmark | - | - | \checkmark | 0.0604 | 0.0946 | **0.0383** | 0.0493 |
| Toys | \checkmark | - | \checkmark | \checkmark | 0.0604 | 0.1050 | 0.0346 | 0.0490 |
| Toys | \checkmark | \checkmark | - | \checkmark | 0.0626 | 0.0992 | **0.0383** | 0.0502 |
| Toys | \checkmark | \checkmark | \checkmark | \checkmark | 0.0644 | **0.1078** | 0.0366 | **0.0506** |

#### アブレーション総括
- **個別エンコーダ＋Mean Pooling（Vanilla）から Shared+EOS への変更だけで、R@10が Beauty で 0.0389 $\to$ 0.0672、Sports で 0.0109 $\to$ 0.0347、Toys で 0.0489 $\to$ 0.0968 と約2〜3倍に激増**。
- ここに CE2TT 蒸留、転移学習、ユーザータワー潜在推論を積み重ねることで、すべてのデータセットにおいて単独モデル最高精度に到達することを実証。
