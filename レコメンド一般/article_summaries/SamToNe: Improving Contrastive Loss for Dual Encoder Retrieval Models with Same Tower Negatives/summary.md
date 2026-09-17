# SamToNe: Improving Contrastive Loss for Dual Encoder Retrieval Models with Same Tower Negatives

**arXiv:** [2306.02516](https://arxiv.org/abs/2306.02516)  
**カンファレンス:** ACL 2023 (Short Papers) 採択  
**著者:** Fedor Moiseev$^{*,1}$, Gustavo Hernández Ábrego$^{1}$, Peter Dornbach$^{1}$, Imed Zitouni$^{1}$, Enrique Alfonseca$^{1}$, Zhe Dong$^{*,1}$（$^{1}$Google Inc., $^*$Equal contribution / Corresponding author）  
**発表:** 2023年6月  
**対象タスク:** 情報検索（Dense Retrieval）、質問応答（Question Answering）、デュアルエンコーダ（Dual Encoder / 2-Tower モデル）の対照学習  

---

## 一言まとめ
Dual Encoder（二重エンコーダ）の対照学習において、他サンプルの文書（Cross-tower Negatives）だけでなく、**同一タワー内の他サンプル（Query同士、またはDocument同士）を負例として分母に直接追加する新損失関数「SamToNe（Same Tower Negatives）」** を提案。追加ハイパーパラメータが一切不要（Hyper-parameter Free）かつ単一段階で学習でき、Query空間とDocument空間の位相的分離（Topological Separation）を解消して完全な空間一致（Alignment）を実現。MS MARCO、MultiReQA、BEIRゼロショット評価において、対称（SDE）および非対称（ADE-SPL）Dual Encoder双方の検索精度を一貫して大幅に向上させた。

### 💡 少ない変更で大きな性能向上を達成できた理由（主要な工夫点）
- **Same Tower Negatives（同一タワー負例）の分母直接統合**:
  - 通常の対照損失が「Query 対 他のDocument」のみを反発させるのに対し、分母に「同一バッチ内の他のQuery（または他のDocument）」を直接加算。
- **自己バランシング正則化（Self-Balancing Regularization / パラメータフリー）**:
  - 先行研究 PAIR のようなハイブリッド係数 $\alpha$ や2段階学習を一切排し、分母で同等に競合させることで、クエリ同士の過度な密集（異方性・崩壊）が生じた際に自動で強力な反発ペナルティが働く自己調整機構を実現。
- **位相的断片化の是正（空間の一致保証）**:
  - 射影層を共有してもなお生じていた「Query空間とDocument空間が隣り合う2つの島に分離する問題」を解消し、正例ペアが同一近傍に高密度に配置される幾何構造を確立。

---

## 背景と課題

### 1. Dual Encoder（二重エンコーダ）の主流化と標準的対照学習
テキスト検索や推薦の第1段階（Candidate Generation / Retrieval）では、クエリ塔（Query Tower）と文書塔（Document/Passage Tower）からなる **Dual Encoder アーキテクチャ** が広く用いられている。
- クエリ $q$ と文書 $p$ をそれぞれ独立に低次元密ベクトルへ写像し、内積やコサイン類似度 $s(q, p)$ を MIPS / ANN（近似近傍探索）で計算することで、超高速な検索を実現する。
- Dual Encoder の標準的な学習方法は、ミニバッチ内の他サンプルの正例文書を負例として再利用する **In-batch Sampled Softmax 対照損失** である：
  $$ \mathcal{L}_c = -\log \frac{\exp(s(q_i, p_i)/\tau)}{\sum_{j \in \mathcal{B}} \exp(s(q_i, p_j)/\tau)} $$

### 2. 位相的断片化（Topological Separation）の発見と既存の限界
Dual Encoder には、重みを共有する対称型（Symmetric Dual Encoder: **SDE** / Siamese）と、独立したパラメータを持つ非対称型（Asymmetric Dual Encoder: **ADE**）がある。先行研究（Dong et al., 2022）では、ADE の最終射影層を共有化する **ADE-SPL (Shared Projection Layer)** によって表現空間の一致が促され、検索精度が向上すると報告されていた。

しかし、著者らが様々なタスク（MS MARCO や SearchQA 等）で t-SNE を用いて埋め込み空間を詳細に可視化したところ、以下の深刻な問題が明らかになった：

- **射影層を共有しても空間が一致しない**:
  - 上図（上段: ADE-SPL Standard）が示すように、Query 空間（青）と Document 空間（赤）は、接続してはいるものの **位相的に明確に分離した「2つの独立した島」** になってしまっていた。
  - 通常の In-batch 損失は「Query と Document」の間の交差引き寄せ・反発（Cross-tower）しか扱わないため、Query 同士・Document 同士の幾何学的整合性を制約できず、正例ペア同士が空間内で完全に重なり合うことを保証できなかった。
- **先行手法 PAIR（Ren et al., 2021）の欠点**:
  - 同一タワー内の反発を考慮した先行研究として PAIR が存在したが、PAIR は別個の損失を線形結合するハイブリッド損失 $\mathcal{L}_{\text{PAIR}} = (1-\alpha)\mathcal{L}_c + \alpha \mathcal{L}_P$ を採用していた。
  - このため、ハイパーパラメータ $\alpha$ のチューニングが必須であり、学習も「第1段階: PAIR損失 $\to$ 第2段階: 通常対照損失」という煩雑な2段階学習を強いられていた。

---

## 提案手法：SamToNe（Same Tower Negatives）

### 1. SamToNe 損失関数の定式化

クエリ側の埋め込み空間の識別性を高め、空間の縮退を防ぐため、**同一バッチ内の他のクエリ $\{q_j\}_{j \neq i}$ を負例（Same Tower Negatives）として対照損失の分母に直接統合** する：

$$ \mathcal{L}_S = -\log \frac{\exp(s(q_i, p_i)/\tau)}{\sum_{j \in \mathcal{B}} \exp(s(q_i, p_j)/\tau) + \sum_{j \in \mathcal{B}, j \neq i} \exp(s(q_i, q_j)/\tau)} $$

- $s(q, p)$: コサイン類似度（あるいは正規化内積）
- $\tau$: ソフトマックス温度パラメータ
- 分母第1項: 従来の Cross-tower 負例（他サンプルの文書 $p_j$）
- 分母第2項: **新設された Same Tower 負例（他サンプルのクエリ $q_j$）**

### 2. 双方向への拡張（Both Towers: Query ＆ Document）
通常、対照学習では Query $\to$ Document と Document $\to$ Query の双方から損失を計算する（Bi-directional Loss）。SamToNe も同様に両方のタワーに自然に拡張可能である：
- Document 側から見た損失 $\mathcal{L}_{S, p \to q}$ では、同一バッチ内の他サンプルの文書 $\{p_j\}_{j \neq i}$ が分母に Same Tower Negatives として加わる。
- 総合損失: $\mathcal{L}_{\text{total}} = \mathcal{L}_{S, q \to p} + \mathcal{L}_{S, p \to q}$

### 3. 自己バランシング正則化（Self-Balancing Regularizer）のメカニズム

先行手法である **PAIR（Ren et al., 2021）** との最大の違い。

#### (1) 先行手法 PAIR の構造的限界：なぜ自己バランシングしないのか？
先行研究の PAIR でも「同一タワー（文書同士）の反発」が提案されていましたが、PAIR は通常損失 $\mathcal{L}_Q$（Cross-tower）と文書間ペナルティ損失 $\mathcal{L}_P$（Same-tower）を**それぞれ別個の Softmax 損失として計算し、外部の重み係数 $\alpha$ で線形結合する「ハイブリッド損失」** を採用していました：
$$ \mathcal{L}_{\text{PAIR}} = (1 - \alpha)\mathcal{L}_Q + \alpha \mathcal{L}_P $$
$$ \mathcal{L}_P = -\log \frac{e^{s(p_i^+, q_i)/\tau}}{\sum_{j \neq i} e^{s(p_i^+, p_j^-)/\tau}} $$
この設計には以下の本質的な弱点がありました：
1. **正規化（分母）が分離しているため、空間の歪みに適応できない**:
   - $\mathcal{L}_Q$ と $\mathcal{L}_P$ の分母が完全に分かれているため、クエリ同士や文書同士がどれほど密集・縮退（Collapse）していようと、受ける反発勾配の強さは固定のハイパーパラメータ $\alpha$ によって人為的に決まってしまいます。
   - 空間の乱れ度合いに応じて「今どちらをどれだけ強く補正すべきか」という**自律的な調整が原理的に働きません**。
2. **煩雑な2段階学習の強制**:
   - $\alpha$ のバランス調整が難しいため、PAIR では「第1段階で PAIR 損失を用いて事前学習 $\to$ 第2段階の本番ファインチューニングでは同タワー正則化を完全に捨てて通常の $\mathcal{L}_Q$ だけで学習し直す」という複雑な多段階パイプラインが必要でした。
3. **両タワーへの拡張困難**:
   - クエリ塔（$q-q$）と文書塔（$p-p$）の双方に同一タワー反発を適用しようとすると、$\alpha_1, \alpha_2$ といった複数のハイパーパラメータが際限なく増えてしまい、実務上のチューニングが極めて困難になります。

#### (2) SamToNe のエレガントな解決策：なぜ自律的にバランシングするのか？
SamToNe は別々の損失に分けるのではなく、**「単一の Softmax の分母」に Cross-tower 負例と Same-tower 負例を同列に合算** します：
$$ \mathcal{L}_S = -\log \frac{e^{s(q_i, p_i)/\tau}}{\underbrace{\sum_{j \in \mathcal{B}} e^{s(q_i, p_j)/\tau}}_{\text{Cross-tower (Query-Doc)}} + \underbrace{\sum_{j \in \mathcal{B}, j \neq i} e^{s(q_i, q_j)/\tau}}_{\text{Same-tower (Query-Query)}}} $$

この数式設計により、以下の **自律的な自己バランシング機構** が成立します：
1. **空間の乱れに対する動的な自動補正**:
   - もしクエリ埋め込み同士が空間の一部に密集（Anisotropy / 表現の縮退）すると、$\max_{j \neq i} s(q_i, q_j) \gg \max_{j} s(q_i, p_j)$ となり、分母の第2項（Same-tower 項）が**指数関数の性質によって自動的に支配的**になります。
   - その結果、人為的な係数を一切触らなくても、モデルは「今まさに密集しているクエリ同士を空間全体に均一に分散（Uniformity）させる強烈な勾配」を自律的に発生させます。
2. **類似度比率 $\frac{s(q_i, q_j)}{s(q_i, p_j)}$ の 1.0 への自然な収束**:
   - 同一の分母内で Query-Query と Query-Doc が競合するため、両者の類似度比率 $\frac{s(q_i, q_j)}{s(q_i, p_j)}$ は**自然と 1.0 付近を中心とする正規分布状へと自己収束**します（後述の実験分析・Figure 6 で実証）。
   - これにより、人為的なチューニングなしに、クエリ空間と文書空間の幾何学的境界が完全に消失し、両空間がぴったり重なり合います（Coinciding Parameter Space）。
3. **完全なパラメータフリー ＆ 単一段階（Single-stage）エンドツーエンド**:
   - $\alpha$ の探索も2段階学習のスケジュールも不要であり、最初から最後まで通常の対照学習と同じコード・同じパイプラインで一発学習が完了します。

| 比較項目 | 通常の対照学習 | 先行手法 PAIR (Ren et al., 2021) | **SamToNe (本研究)** |
| :--- | :---: | :---: | :---: |
| **同タワー負例の導入** | なし | あり（ハイブリッド損失として別個計算） | **あり（単一 Softmax の分母に直接合算）** |
| **追加ハイパーパラメータ** | なし | あり（結合重み $\alpha$ のチューニング必須） | **完全フリー（追加パラメータ一切なし）** |
| **学習ステップ** | 単一段階 | 2段階学習が必要（Stage 1: PAIR $\to$ Stage 2: 通常） | **完全な単一段階（1-Stage 直接学習）** |
| **両タワーへの拡張** | - | 困難（さらにパラメータが増加する） | **極めて容易（$q \to p$ と $p \to q$ の分母に足すだけ）** |
| **空間の自己バランシング** | 働かない | **働かない**（$\alpha$ 固定のため空間の歪みに適応不可） | **強力に働く（比率が自然に 1.0 へ自己収束）** |

---

## 実験結果

バックボーンには事前学習済み `t5.1.1` エンコーダ（Small, Base, Large, XL, XXL）を採用し、トークン出力を平均プーリング（Mean Pooling）した上で射影層を通して埋め込みベクトルを生成。

### 1. QA検索ベンチマーク（MS MARCO ＆ MultiReQA）

MS MARCO および MultiReQA（NQ, SQuAD, TriviaQA, SearchQA）の5つの主要データセットにおける検証結果（モデルサイズ: Base）：

| モデル構成 | 損失関数 | MS MARCO P@1 | MS MARCO MRR | NQ P@1 / MRR | SQuAD P@1 / MRR | TriviaQA P@1 / MRR | SearchQA P@1 / MRR | **5タスク平均 P@1** | **5タスク平均 MRR** |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ADE** | Standard | 14.1 | 26.8 | 53.5 / 65.2 | 64.3 / 74.0 | 37.9 / 50.4 | 41.5 / 57.2 | 42.3 | 54.7 |
| | **SamToNe** | **16.0** | **28.5** | 52.8 / 63.9 | 63.6 / 73.0 | 38.4 / 49.8 | **49.2 / 62.3** | **44.0** | **55.5** |
| **ADE-SPL** | Standard | 15.7 | 28.8 | 55.3 / 67.0 | 74.5 / **82.1** | 41.7 / 54.4 | 42.3 / 59.1 | 45.9 | 58.3 |
| | **SamToNe** | **17.6** | **30.4** | **55.7 / 67.2** | 73.8 / 81.7 | 44.0 / 55.9 | **48.5 / 63.4** | **47.9** (+2.0) | **59.7** (+1.4) |
| | PAIR | 16.9 | 29.6 | 55.7 / 67.0 | 74.4 / 82.0 | **45.0 / 56.8** | 44.1 / 60.4 | 47.2 | 59.2 |
| **SDE** | Standard | 16.1 | 29.1 | 54.4 / 66.6 | 74.1 / 81.9 | 41.4 / 54.2 | 37.6 / 55.8 | 44.7 | 57.5 |
| | **SamToNe** | **17.2** | **30.2** | 54.2 / 66.4 | **74.6 / 82.0** | 42.1 / 54.5 | **44.0 / 60.4** | **46.4** (+1.7) | **58.7** (+1.2) |
| | PAIR | 16.1 | 29.1 | 53.8 / 66.2 | 74.1 / 81.7 | 41.3 / 54.5 | 38.7 / 56.6 | 44.7 | 57.5 |

- **全モデル構造で一貫した大幅向上**:
  - ADE-SPL において、MS MARCO の P@1 が $15.7\% \to 17.6\%$（+1.9 pt）、MRR が $28.8\% \to 30.4\%$（+1.6 pt）。
  - SearchQA では P@1 が $42.3\% \to 48.5\%$（**+6.2 pt**）、MRR が $59.1\% \to 63.4\%$（**+4.3 pt**）と爆発的な精度改善を達成。
  - 先行手法 PAIR（平均 P@1 47.2%）を明確に上回り、最高精度を記録した。

---

### 2. モデルサイズのスケーリング耐性（Small 〜 XXL）

![MRR Scaling](./images/scaling-msmarco-mrr.png)

- モデル規模を Small から Base, Large, XL, **XXL（数十億パラメータ級）** までスケールさせても、SamToNe の優位性は全く揺らぐことなく一貫して通常の対照損失を上回り続けた。

---

### 3. BEIR ベンチマーク（ゼロショット汎化性能）

MS MARCO で学習した SDE モデルを用い、ドメイン外の多種多様な検索データセット（BEIR）に対する Zero-shot 転移性能を評価：

![BEIR Relative Improvement](./images/relative_improvement_ndcg10.png)

- Climate-Fever（+2.9%）、CQADupStack（+1.7%）、DBpedia（+0.4%）、FEVER（+2.5%）、SciDocs（+2.1%）、Touché-2020（+1.9%）など、**大半のゼロショットタスクにおいて NDCG@10 が一貫して向上**。
- SamToNe は特定ドメインへの過学習ではなく、「汎用的な埋め込み空間の健全化（正則化）」を促すため、未知ドメインへの汎化性能も底上げされることが実証された。

---

## 詳細な分析と考察

### 1. t-SNE による埋め込み空間の可視化

![Embedding Space Analysis](./images/analysis_embedding_space.png)

- **Standard（通常損失）**: Query 点群（青）と Document 点群（赤）が左右に割れ、境界線で接するだけの「異空間」になっている。
- **SamToNe 適用後**: 青と赤の点群が完全に混合・一致し、同一の幾何学的多様体（Coinciding Parameter Space）上に展開されている。

### 2. Top-1 検索結果のコサイン類似度分布

![Embedding Distance Analysis](./images/msmarco_neighbor_1.png)

- テストセットにおいて、各クエリに対する Top-1 検索結果文書とのコサイン類似度の分布をプロット。
- 通常損失では類似度が 0.6〜0.8 付近に広く散らばっていたのに対し、**SamToNe を適用すると分布全体が劇的に 1.0（完全一致）側へシフト**。正例文書がクエリの直近傍へ強力に引き寄せられている。

### 3. 自己バランシング比率 $\frac{\text{sim}(q_i, q_j)}{\text{sim}(q_i, p_j)}$ の検証

![Distribution of Ratio](./images/Distribution_of_query-query_to_query-document_similarity_ratio.png)

- ランダムに選んだペアにおける「Query-Query 類似度」と「Query-Document 類似度」の比率分布を測定。
- 通常損失や PAIR では比率が大きく歪み、Query 同士の類似度が Document との類似度に比べて不当に高くなったり低くなったりする。
- **SamToNe を適用した場合のみ、比率が綺麗に 1.0 を中心とする正規分布状に収束**。これこそが、同一分母による数学的自己調整（Self-balancing）の直接的な証明である。

---

## 結論と推薦・検索システムへの実務的示唆

1. **損失関数を数行書き換えるだけで得られる恒久的な精度向上**:
   - アーキテクチャの変更や複雑な前処理を一切必要とせず、バッチ内の Query-Query 内積行列を計算して分母に足すだけで、検索精度（P@1, MRR, NDCG）が即座に底上げされる。
2. **2-Tower 型レコメンド（User塔 / Item塔）への絶大な応用価値**:
   - 検索（Query/Doc）だけでなく、レコメンドにおける User-Item Dual Encoder においても「User 空間と Item 空間が分離する問題」は頻発する。
   - ユーザー同士の In-batch 負例（Same Tower Negatives）を導入することで、ユーザーとアイテムの潜在空間を強制的に一致させ、推薦精度の向上やコールドスタート耐性の強化が期待できる。
3. **ハイパーパラメータチューニングからの解放**:
   - 重み係数 $\alpha$ の探索や2段階学習のスケジュール設計が不要なため、実務の学習パイプラインに最も安全かつ低コストに組み込める設計となっている。

---

## 考察：Qwen3 Embedding の改良 InfoNCE との比較・技術的系譜

後続の最新 SOTA モデルである [Qwen3 Embedding（2025）](file:///Users/masashiueno/業界まとめ文書/LLM埋め込み表現/article_summaries/Qwen3%20Embedding:%20Advancing%20Text%20Embedding%20and%20Reranking%20Through%20Foundation%20Models/summary.md) では、本研究の SamToNe と極めて類似した「同一タワー（クエリ同士・ドキュメント同士）の反発」を導入した改良型 InfoNCE 損失が採用されている。両者を比較することで、対照学習の損失設計がどのように発展してきたのかを明確に位置づけることができる。

### 1. 損失関数の比較

- **SamToNe（2023 / Google）**:
  $$ \mathcal{L}_S = -\log \frac{e^{s(q_i, p_i)/\tau}}{\sum_{j \in \mathcal{B}} e^{s(q_i, p_j) / \tau} + \sum_{j \in \mathcal{B}, j \neq i} e^{s(q_i, q_j) / \tau}} $$
- **Qwen3 Embedding（2025 / Alibaba）**:
  $$ \mathcal{L}_\textrm{embedding} = - \frac{1}{N} \sum_i^N \log\frac{e^{s(q_i, d_i^+)/\tau}}{Z_i} $$
  $$ Z_i = \underbrace{e^{s(q_i, d_i^+) / \tau}}_{\text{(1) 正例}} + \underbrace{\sum_k^K m_{ik}e^{s(q_i, d_{i,k}^-)/\tau}}_{\text{(2) ハード負例}} + \underbrace{\sum_{j\neq i} m_{ij}e^{s(q_i, q_j) / \tau}}_{\mathbf{(3) バッチ内他クエリ}} + \underbrace{\sum_{j\neq i} m_{ij}e^{s(d_i^+, d_j) / \tau}}_{\mathbf{(4) バッチ内他文書}} + \underbrace{\sum_{j\neq i} m_{ij}e^{s(q_i, d_j) / \tau}}_{\text{(5) バッチ内他文書}} $$

### 2. 共通する設計思想
- **Cross-tower（Query-Doc）のみの反発では不十分**: クエリ同士（$q_i \leftrightarrow q_j$）やドキュメント同士（$d_i \leftrightarrow d_j$）の反発を対照学習の分母に含めることで、埋め込み空間の異方性（Anisotropy / 空間の一部への縮退）を防ぎ、空間の均一性（Uniformity）とタワー間のアライメント（Alignment）を同時に最大化する。

### 3. 歴史的位置づけと技術的進化

| 比較項目 | SamToNe (2023 / 本研究) | Qwen3 Embedding (2025) |
| :--- | :--- | :--- |
| **歴史的位置づけ** | **「Same-Tower Negatives」の概念的先駆者** | **同タワー負例を包括統合した「完成形」** |
| **主眼・目的** | **空間の位相的一致（Alignment）**<br>Query塔とDoc塔が別々の島に分離する幾何学的断片化の解消 | **空間の表現力最大化 ＆ 偽陰性制御**<br>全方位の境界線を学習しつつ大規模バッチの毒性を抑制 |
| **ハード負例との統合** | In-batch 負例の枠組みが主 | 事前マイニングしたハード負例（$d^-$）と同一分母で共存 |
| **偽陰性（False Negative）対策** | なし（バッチ内重複・類義語の誤反発リスクが残る） | **動的マスク因子 $m_{ij} \in \{0, 1\}$ を導入**<br>類似度高すぎ/重複するペアを自動除外 |
| **対象モデル** | T5 等のエンコーダ型 Dual Encoder | Qwen3 等の大規模デコーダ LLM（0.6B 〜 8B） |

### 4. Qwen3 が克服した「SamToNe の課題」
- **大規模バッチにおける偽陰性（False Negative）の毒性**:
  - バッチサイズが数千〜数万に拡大すると、偶然同じバッチ内に「意味的にほぼ同義なクエリ同士（例:『東京のホテル』と『東京の宿泊先』）」が含まれる確率が急上昇する。
  - SamToNe ではこれらを無条件に負例として強烈に反発させてしまうため、表現空間が歪むリスクがあった。
  - Qwen3 は、類似度や重複度に基づく動的マスク $m_{ij}$ を挟むことで、**「SamToNe の幾何学的恩恵（空間均一化）を保ちながら、偽陰性による学習阻害を完全にシャットアウトする」** という極めて実用的な進化を遂げている。

