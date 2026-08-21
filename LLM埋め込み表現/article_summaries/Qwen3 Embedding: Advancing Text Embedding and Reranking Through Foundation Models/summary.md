# Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models

**arXiv:** 2506.05176  
**著者:** Yanzhao Zhang*, Mingxin Li*, Dingkun Long*, Xin Zhang*, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou（Tongyi Lab, Alibaba Group）  
**発表:** 2025年6月  
**ライセンス:** Apache 2.0

---

## 背景

RAG（検索拡張生成）やエージェントシステムなど、LLM活用アプリケーションの台頭により、テキスト埋め込みとリランキングモデルに対するスケーラビリティ・文脈理解・タスク特化性の要件が急速に高まっている。

従来の埋め込みモデルは BERT などエンコーダ専用モデルをベースとしていたが、LLM の豊富な世界知識・テキスト理解・推論能力を活用することで、さらなる性能向上が期待できる。本論文では、Qwen3 基盤モデル上に構築した **Qwen3 Embedding シリーズ**（0.6B / 4B / 8B）を提案し、多言語検索・コード検索・複雑なインストラクション追従など多様なタスクで SOTA を達成した。

前身の GTE-Qwen シリーズからの主な革新点は以下の3つ：
1. **大規模合成データによる弱教師あり事前学習**
2. **教師あり Fine-tuning への高品質合成データの組み込み**
3. **Spherical Linear Interpolation（slerp）によるモデルマージ**

---

## 手法

### モデルアーキテクチャ

![Figure 1: Qwen3-Embedding（左）とQwen3-Reranker（右）のアーキテクチャ](./images/q3e-model-arc.png)

Qwen3 基盤モデルの Dense 版を使用。0.6B / 4B / 8B の3サイズを提供。

#### 埋め込みモデル
因果的アテンション（Causal Attention）LLMを使用。入力シーケンスの末尾に `[EOS]` トークンを付加し、最終層のその隠れ状態を埋め込みとして使用する。

インストラクションに従った埋め込みを実現するため、クエリにのみインストラクションを前置：

```
{Instruction} {Query}<|endoftext|>
```

ドキュメント側にはインストラクションを付加しない（非対称設計）。

#### リランキングモデル
LLM を用いたポイントワイズ・リランキング。クエリとドキュメントを1つの文脈に結合し、バイナリ分類問題として関連性を評価：

```
<|im_start|>system
Judge whether the Document meets the requirements based on the Query and the Instruct provided. Note that the answer can only be "yes" or "no".<|im_end|>
<|im_start|>user
<Instruct>: {Instruction}
<Query>: {Query}
<Document>: {Document}<|im_end|>
<|im_start|>assistant
<think>\n\n</think>\n\n
```

関連性スコアを以下の式で算出：

$$\text{score}(q,d) = \frac{e^{P(\text{yes}|I,q,d)}}{e^{P(\text{yes}|I,q,d)}+e^{P(\text{no}|I,q,d)}}$$

---

### 学習パイプライン

![Figure 2: Qwen3 Embedding/Reranking モデルの学習パイプライン](./images/q3e-train-pipeline.png)

#### 損失関数

**埋め込みモデル（改良 InfoNCE）**:

従来の対照学習（標準的な InfoNCE）では、クエリ $q_i$ に対して「正例 $d_i^+$」と「同一バッチ内の他ドキュメント $d_j$（およびハード負例）」のみを一方向（$q \to d$）で計算するのが一般的だった。これには以下の2つの根本的課題があった：
1. **負例プールの限定性**: クエリ同士（$q_i \leftrightarrow q_j$）やドキュメント同士（$d_i^+ \leftrightarrow d_j$）の反発関係が十分に学習されず、埋め込み空間全体の均一性や弁別性が高まりにくい。
2. **偽陰性（False Negatives）のペナルティ問題**: バッチサイズを拡大したり多様な負例を含めると、**「本来は正例になり得るテキスト」や「同一文書の重複」が負例プールに混入**し、モデルが本来正当な関連性を持つテキスト同士の類似度を無理やり下げるよう学習してしまい、表現空間が劣化する。

Qwen3 Embedding ではこれらを解決するため、**5方向の包括的負例プール**と**動的マスク因子 $m_{ij}$ による偽陰性フィルタリング**を導入した：

$$\mathcal{L}_\textrm{embedding} = - \frac{1}{N} \sum_i^N \log\frac{e^{s(q_i, d_i^+)/\tau}}{Z_i}$$

$$Z_i = \underbrace{e^{s(q_i, d_i^+) / \tau}}_{\text{(1) 正例}} + \underbrace{\sum_k^K m_{ik}e^{s(q_i, d_{i,k}^-)/\tau}}_{\text{(2) } K \text{ 個のハード負例}} + \underbrace{\sum_{j\neq i} m_{ij}e^{s(q_i, q_j) / \tau}}_{\text{(3) バッチ内他クエリ}} + \underbrace{\sum_{j\neq i} m_{ij}e^{s(d_i^+, d_j) / \tau}}_{\text{(4) バッチ内ドキュメント同士}} + \underbrace{\sum_{j\neq i} m_{ij}e^{s(q_i, d_j) / \tau}}_{\text{(5) バッチ内他ドキュメント}}$$

**各項の類似度と役割（最適化の狙い）:**

| 項 | 類似度 | 通常のInfoNCE | 役割（何と何を引き離すか / 最適化の狙い） |
|---|---|:---:|---|
| **(1)** | $s(q_i, d_i^+)$ | **あり** | **クエリ $\times$ 正例ドキュメント**: 正例同士の類似度を最大化する（分子・分母共通） |
| **(2)** | $s(q_i, d_{i,k}^-)$ | 設定依存 | **クエリ $\times$ ハード負例**: 難度の高い負例を**「対象クエリ $q_i$」**から遠ざける |
| **(3)** | $s(q_i, q_j)$ | **なし** | **クエリ $\times$ 他クエリ**: 異なる検索クエリ同士を引き離し、クエリ空間での縮退を防ぐ |
| **(4)** | $s(d_i^+, d_j)$ | **なし** | **正例ドキュメント $\times$ 他ドキュメント**: ドキュメント同士を引き離し、ドキュメント空間全体に均一に分散させる |
| **(5)** | $s(q_i, d_j)$ | **あり** | **クエリ $\times$ 他ドキュメント**: バッチ内の関係ない他ドキュメントを**「対象クエリ $q_i$」**から遠ざける |

- **偽陰性を防ぐ適応的マスク因子 $m_{ij}$**:
  $$m_{ij} = \begin{cases} 0 & \text{if } s_{ij} > s(q_i, d_i^+) + 0.1 \text{ or } d_j == d_i^+, \\ 1 & \text{otherwise} \end{cases}$$
  - **完全重複の除外 ($d_j == d_i^+$)**: 同一テキストがバッチ内に重複して存在する場合、負例から除外。
  - **高類似度サンプルの適応的除外 ($s_{ij} > s(q_i, d_i^+) + 0.1$)**: 負例候補の類似度 $s_{ij}$ が正例ペアの類似度 $s(q_i, d_i^+)$ を超える（+0.1 のマージン以上）場合、「誤って負例に混入した潜在的正例（偽陰性）」と判断して損失の分母から自動除外。これにより、大規模バッチ・多様な負例プールでも学習が破壊されない。

**リランキングモデル（SFT 損失）**:

$$L_\textrm{reranking} = -\log p(l|\mathcal{P}(q,d))$$

ラベル $l$ は正例で "yes"、負例で "no"。バイナリ分類の対数尤度を最大化する。

#### 多段階学習

1. **弱教師あり事前学習（Stage 1）**: Qwen3-32B が生成した約1.5億ペアの合成データで学習
2. **教師あり Fine-tuning（Stage 2）**: コサイン類似度 > 0.7 でフィルタリングした高品質合成データ約1200万ペア ＋ 手動アノテーションデータ約700万ペアで継続学習
3. **モデルマージ（Stage 3）**:
   - **背景・動機**: 汎用テキスト埋め込みモデルでは、検索・STS・分類・多言語・コード検索などの間で「タスク競合（Task Conflict）」や「データ不均衡（Data Imbalance）」が生じやすい。
   - **手法**: **球面線形補間（slerp: Spherical Linear Interpolation）** を採用。Fine-tuning の過程で保存された異なるデータ分布や学習進捗を反映する複数のチェックポイントを角度ベースで滑らかに補間マージする。単純な重み平均（LERP）と異なり、パラメータの幾何構造や大きさを損なわずに融合可能。
   - **先行研究**: 著者らの先行研究 [*Li et al., 2024 "Improving General Text Embedding Model: Tackling Task Conflict and Data Imbalance through Model Merging"* (arXiv:2410.15035)](https://arxiv.org/abs/2410.15035) に基づく。
   - **効果**: 追加学習なしでタスク間のトレードオフを解消し、未知のデータ分布に対する頑健性・汎化性能を向上。

#### 合成データ生成（Synthetic Data Generation）

従来の埋め込みモデル（E5, GTE等）はWebやフォーラムからテキストペアをマイニングしていたが、「特定言語・ドメインへの偏り」「ノイズ制御の難しさ」という課題があった。Qwen3 Embedding では **Qwen3-32B** を用いて、多次元で属性を制御した高品質な合成データセットをゼロから構築した。

##### ① 生成対象の4タスク
1. **Retrieval（テキスト検索）**: 多言語コーパスからのドキュメント $\to$ 検索クエリ生成（中核データ）
2. **Bitext Mining（対訳・多言語マイニング）**: 言語横断の文ペア
3. **STS（意味的類似度）**: 類似度の異なるテキストペア
4. **Classification（テキスト分類）**: テキスト $\to$ ラベル・説明文ペア

##### ② 検索データの「2段階生成パイプライン」
単調なクエリ生成を防ぎ、多様で自然な検索シナリオを再現するため、**ペルソナ注入（Persona Hub）を用いた2段階方式**を採用：

- **Stage A（コンフィグ決定）**:
  - 文書に関連するペルソナ候補5つを Persona Hub から検索して提示。
  - LLM が文書に最適な以下の設定を JSON で決定：
    - `Character`: 想定ユーザー（例: 歴史学者、学生、エンジニアなど）
    - `Question_Type`: 5種類（`keywords` / `acquire_knowledge` / `summary` / `yes_or_no` / `background`）
    - `Difficulty`: 3段階（`high_school` / `university` / `phd`）
- **Stage B（クエリ生成）**:
  - Stage A で確定したコンフィグに加え、`Length`（単語数）や `Language`（多言語・クロスリンガル）を指定し、そのペルソナの視点・口調で検索クエリを生成。

##### ③ データ規模とステージ別活用

| フェーズ | 使用データ | 規模 | 役割・選定基準 |
|---|---|---|---|
| **Stage 1（事前学習）** | 合成データ全体 | **約 1.5 億ペア (150M)** | 多様・多言語なデータでモデルの基礎汎化能力を獲得 |
| **Stage 2（Fine-tuning）** | 高品質合成データ<br>＋ 手動アノテーション | **約 1,200 万ペア (12M)**<br>＋ 約 700 万ペア (7M) | 合成データのうち**コサイン類似度 $> 0.7$** でフィルタリングした極めて高品質なペアのみを選抜 |

※リランキングモデルは Stage 1 の弱教師あり学習を行わず、Stage 2（高品質データによる SFT）+ モデルマージのみで構築。

---

## 結果

### Table 1: MTEB Multilingual (MMTEB) 評価結果（131タスク）

| モデル | Size | Mean (Task) | Mean (Type) | Bitext Mining | Classification | Clustering | Inst. Retrieval | Multilabel Class. | Pair Class. | Rerank | Retrieval | STS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NV-Embed-v2 | 7B | 56.29 | 49.58 | 57.84 | 57.29 | 40.80 | 1.04 | 18.63 | 78.94 | 63.82 | 56.72 | 71.10 |
| GritLM-7B | 7B | 60.92 | 53.74 | 70.53 | 61.83 | 49.75 | 3.45 | 22.77 | 79.94 | 63.78 | 58.31 | 73.33 |
| BGE-M3 | 0.6B | 59.56 | 52.18 | 79.11 | 60.35 | 40.88 | -3.11 | 20.1 | 80.76 | 62.79 | 54.60 | 74.12 |
| multilingual-e5-large-instruct | 0.6B | 63.22 | 55.08 | 80.13 | 64.94 | 50.75 | -0.40 | 22.91 | 80.86 | 62.61 | 57.12 | 76.81 |
| gte-Qwen2-1.5B-instruct | 1.5B | 59.45 | 52.69 | 62.51 | 58.32 | 52.05 | 0.74 | 24.02 | 81.58 | 62.58 | 60.78 | 71.61 |
| gte-Qwen2-7b-Instruct | 7B | 62.51 | 55.93 | 73.92 | 61.55 | 52.77 | 4.94 | 25.48 | 85.13 | 65.55 | 60.08 | 73.98 |
| text-embedding-3-large | - | 58.93 | 51.41 | 62.17 | 60.27 | 46.89 | -2.68 | 22.03 | 79.17 | 63.89 | 59.27 | 71.68 |
| Cohere-embed-multilingual-v3.0 | - | 61.12 | 53.23 | 70.50 | 62.95 | 46.89 | -1.89 | 22.74 | 79.88 | 64.07 | 59.16 | 74.80 |
| Gemini Embedding | - | 68.37 | 59.59 | 79.28 | 71.82 | 54.59 | 5.18 | **29.16** | 83.63 | 65.58 | 67.71 | 79.40 |
| **Qwen3-Embedding-0.6B** | 0.6B | 64.33 | 56.00 | 72.22 | 66.83 | 52.33 | 5.09 | 24.59 | 80.83 | 61.41 | 64.64 | 76.17 |
| **Qwen3-Embedding-4B** | 4B | 69.45 | 60.86 | 79.36 | 72.33 | 57.15 | **11.56** | 26.77 | 85.05 | 65.08 | 69.60 | 80.86 |
| **Qwen3-Embedding-8B** | 8B | **70.58** | **61.69** | **80.89** | **74.00** | **57.65** | 10.06 | 28.66 | **86.40** | **65.63** | **70.88** | **81.08** |

**考察:** Qwen3-Embedding-8B は MMTEB で 70.58 を達成し、プロプライエタリな Gemini Embedding（68.37）を上回る。0.6B という最小モデルでも既存オープンソース最強の multilingual-e5-large-instruct（0.6B）を大きく超え（64.33 vs 63.22）、Instruction Retrieval タスクで特に顕著な改善（5.09 vs -0.40）が見られた。Multilabel Classification では Gemini Embedding（29.16）に届かないが、他ほぼ全カテゴリで SOTA を達成した。

---

### Table 2: MTEB English・Chinese・Code 評価結果

| モデル | Size | Dim | MTEB (Eng, v2) Mean (Task) | MTEB (Eng, v2) Mean (Type) | CMTEB Mean (Task) | CMTEB Mean (Type) | MTEB (Code) |
|---|---|---|---|---|---|---|---|
| NV-Embed-v2 | 7B | 4096 | 69.81 | 65.00 | 63.0 | 62.0 | - |
| GritLM-7B | 7B | 4096 | 67.07 | 63.22 | - | - | 73.6 |
| multilingual-e5-large-instruct | 0.6B | 1024 | 65.53 | 61.21 | - | - | 65.0 |
| gte-Qwen2-1.5b-instruct | 1.5B | 1536 | 67.20 | 63.26 | 67.12 | 67.79 | - |
| gte-Qwen2-7b-instruct | 7B | 3584 | 70.72 | 65.77 | 71.62 | 72.19 | 56.41 |
| text-embedding-3-large | - | 3072 | 66.43 | 62.15 | - | - | 58.95 |
| cohere-embed-multilingual-v3.0 | - | 1024 | 66.01 | 61.43 | - | - | 51.94 |
| Gemini Embedding | - | 3072 | 73.30 | 67.67 | - | - | 74.66 |
| **Qwen3-Embedding-0.6B** | 0.6B | 1024 | 70.70 | 64.88 | 66.33 | 67.44 | 75.41 |
| **Qwen3-Embedding-4B** | 4B | 2560 | 74.60 | 68.09 | 72.26 | 73.50 | 80.06 |
| **Qwen3-Embedding-8B** | 8B | 4096 | **75.22** | **68.70** | **73.83** | **75.00** | **80.68** |

**考察:** MTEB Code（コード検索）で Qwen3-Embedding-8B が 80.68 と圧倒的な SOTA を達成（Gemini Embedding 74.66、GritLM 73.6 に対して大差）。Qwen3 基盤モデルのコード理解能力が直接貢献していると考えられる。英語 MTEB でも Gemini Embedding（73.30）を上回る 75.22 を達成。

---

### Table 3: リランキング評価結果

| モデル | Param | MTEB-R (Eng) | CMTEB-R (Chinese) | MMTEB-R (Multilingual) | MLDR | MTEB-Code | FollowIR |
|---|---|---|---|---|---|---|---|
| Qwen3-Embedding-0.6B（ベースライン） | 0.6B | 61.82 | 71.02 | 64.64 | 50.26 | 75.41 | 5.09 |
| Jina-multilingual-reranker-v2-base | 0.3B | 58.22 | 63.37 | 63.73 | 39.66 | 58.98 | -0.68 |
| gte-multilingual-reranker-base | 0.3B | 59.51 | 74.08 | 59.44 | 66.33 | 54.18 | -1.64 |
| BGE-reranker-v2-m3 | 0.6B | 57.03 | 72.16 | 58.36 | 59.51 | 41.38 | -0.01 |
| **Qwen3-Reranker-0.6B** | 0.6B | 65.80 | 71.31 | 66.36 | 67.28 | 73.42 | 5.41 |
| **Qwen3-Reranker-4B** | 4B | **69.76** | 75.94 | 72.74 | 69.97 | 81.20 | **14.84** |
| **Qwen3-Reranker-8B** | 8B | 69.02 | **77.45** | **72.94** | **70.19** | **81.22** | 8.05 |

**考察:** Qwen3-Reranker 全モデルが既存リランカーを上回り、特に FollowIR（複雑なインストラクション追従検索）で Qwen3-Reranker-4B が 14.84 と突出した性能を示した。既存リランカーはこのタスクでマイナスかほぼ0のスコアしか出せていないことと対照的であり、インストラクション対応能力が大幅に向上している。MLDR でも Qwen3-Reranker-8B（70.19）が従来最強の gte-multilingual-reranker-base（66.33）を大きく上回った。

---

### Table 4: アブレーション研究 — Qwen3-Embedding-0.6B（各コンポーネントの寄与）

| モデル設定 | MMTEB | MTEB (Eng, v2) | CMTEB | MTEB (Code, v1) |
|---|---|---|---|---|
| w/ only synthetic data（Stage 1 のみ） | 58.49 | 60.63 | 59.78 | 66.79 |
| w/o synthetic data（合成データなし） | 61.21 | 65.59 | 63.37 | 74.58 |
| w/o model merge（モデルマージなし） | 62.56 | 68.18 | 64.76 | 74.89 |
| **Qwen3-Embedding-0.6B（フルシステム）** | **64.33** | **70.70** | **66.33** | **75.41** |

**考察:** 
- **合成データの効果**: 合成データ Stage 1 のみの行（58.49）vs 合成データなしの行（61.21）を比較すると、合成データ単体での事前学習だけでは直接 SFT より劣る。しかし合成データあり（フルシステム 64.33）vs なし（61.21）を見ると、+3.12 pt の明確な効果が確認できる。合成データは Stage 1 の弱教師あり学習として Stage 2 の下地を作ることに価値がある
- **モデルマージの効果**: w/o model merge（62.56）vs フルシステム（64.33）で MMTEB +1.77 pt、英語 MTEB で +2.52 pt、中国語 CMTEB で +1.57 pt、コード検索で +0.52 pt と、追加の学習コストなしで全ベンチマークにわたり一貫した改善。タスク競合やチェックポイントごとの偏りを解消する強力な手法であることが実証されている
- 全コンポーネントを組み合わせることで相乗効果が生まれ、いずれの単体除去よりもフルシステムが優れている

