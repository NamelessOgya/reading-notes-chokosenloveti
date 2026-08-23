# Towards General Text Embeddings with Multi-stage Contrastive Learning (GTE)

**arXiv:** 2308.03281  
**著者:** Zehan Li, Xin Zhang, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Meishan Zhang（Alibaba DAMO Academy）  
**発表:** 2023年8月  

---

## 一言まとめ
公開データのみを使ってclosedなモデルを超えようとする試み.  
クエリも負例として活用する改良対照損失が効果的で、その後様々なembeddingモデルの基礎となった。    


## 背景

テキスト埋め込みモデルの研究は従来、意味的類似度（STS）や密検索（Dense Retrieval）など、特定タスクに特化したモデルが主流であった。
- **SimCSE**：対称な文ペアで学習するため、非対称な検索タスク（Retrieval）に弱い
- **DPR 系**：密検索に特化して学習するため、STS タスク等に弱い

近年台頭した E5 などの汎用埋め込みモデルは、大規模な弱教師あり対照学習により高い汎化性能を示しているが、**独自の非公開データ（CCPairs 等）に依存しており、完全な再現性に乏しい**という課題があった。

本論文 **GTE**（General Text Embeddings）では、**完全に公開されているオープンソースデータのみ**を使用し、シンプルな多段階対照学習（Multi-stage Contrastive Learning）と学習戦略の工夫により、商用 API（OpenAI text-embedding-ada-002 等）や先行モデルを凌駕する汎用テキスト埋め込みモデルを構築した。

---

## 手法

### 1. 全体パイプライン（2段階対照学習）

```
Stage 1: 教師なし対照事前学習（Unsupervised Pre-training / ~8億テキストペア）
          ↓
Stage 2: 教師あり対照 Fine-tuning（Supervised Fine-tuning / ~300万トリプレット）
```

- **バックボーン**: BERT（small: 30M, base: 110M, large: 330M）
- **プーリング**: Mean Pooling（全トークンの平均埋め込みを採用、[CLS] は不使用、プーラー層なし）
- **類似度計算**: コサイン類似度 $\cos(e_q, e_d)$

---

### 2. 学習データセット構成

#### Stage 1: 教師なし事前学習データ（~8億ペア / 33データセット）
フィルタリングを行わず、オープンソースから収集した多様なドメイン・タスクのテキストペアを使用。

| タスク分類 (Task Type) | テキストペア形式 (Format) | クエリ例 (Query) | ドキュメント例 (Doc) |
|---|---|---|---|
| **Web Page** | (title, body) | Providence Real Estate \| Providence Homes for Sale | Founded by Roger Williams in 1636, Providence is recognized as one of the country's oldest cities... |
| **Academic Paper** | (title, abstract) | Polymer Quantum Mechanics and its Continuum Limit | A rather non-standard quantum representation of the canonical commutation relations of quantum mechanics... |
| **Hyperlink** | (citation, reference) | After the championship in 1996, the PGA of America raised its stake to 50% and announced that ... | Pebble Beach Golf Links The largest margin of victory ever in a major championship, surpassing the 13-shot ... |
| **Social Media** | (post, comment) | Pretty sure any team with Lebron James will be a playoff contender. Considering UNC would be in the East... | I was being sarcastic and making fun of the East, but honestly I was really in deep thought about this ... |
| **Knowledge Base** | (entity, description) | Animation | Animation is the process of creating the illusion of motion and shape change by means of the rapid display of ... |
| **Community QA** | (question, answer) | How the human species evolved? | A tough question as it overlaps science and theology. Since you asked "how the human species evolved?" I'll assume ... |
| **News** | (summary, content) | Nepalese Opposition Welcomes Return of Parliament | Nepal's opposition alliance formally calls off weeks of pro-democracy protests after King Gyenandra reinstates ... |
| **Code** | (text, code) | SetMaxRecords sets the MaxRecords field's value. | `func (s *DescribeSnapshotCopyGrantsInput) SetMaxRecords (v int64) *DescribeSnapshotCopyGrantsInput { s.MaxRecords` |

#### Stage 2: 教師あり Fine-tuning データ（~300万トリプレット）
高品質なアノテーション付きデータセットを統合し、外部リトリーバー（BM25, Contriever 等）でマイニングしたハード負例を含む $(q, d^+, d^-)$ トリプレットを使用。

| タスク分類 | トリプレット形式 | クエリ (Query) | 正例 (Doc / Positive) | ハード負例 (Hard Negative) |
|---|---|---|---|---|
| **Web Search** | (query, passage, negative) | finger cellulitis symptoms | The following are the most common symptoms of cellulitis. However... | Cellulitis usually begins as a small area of pain and ... |
| **Open QA** | (question, passage, negative) | big little lies season 2 how many episodes | Big Little Lies (TV series). series garnered several accolades... | Little People, Big World. final minutes of the season two... |
| **NLI** | (sentence, entailment, contradiction) | (Read for Slate 's take on Jackson's findings.) | Slate had an opinion on Jackson's findings. | Slate did not hold any opinion on Jackson's findings. |
| **Fact Verification** | (argument, evidence, others) | Roman Atwood is a content creator. | Roman Bernard Atwood (born May 28, 1983) is an American YouTube personality... | 6th Streamy Awards Casey Neistat and Jesse Wellens, PrankvsPrank ... |
| **Paraphrase** | (sentence, paraphrase, others) | Lexapro taken with crestor any reaction? | Can dayquil be taken with Lexapro? | Can stopping lexapro cause a longer period? |

---

### 3. 学習の工夫

#### ① 改良対照損失（Improved Contrastive Loss）
従来の InfoNCE 損失（一方向）を **双方向・4方向** に拡張。バッチ内ペア $\{(q_i, d_i)\}_{i=1}^N$ に対し、**クエリとドキュメントの両方を負例プールとして活用**：

$$ \mathcal{L} = \mathcal{L}_{q \to d} + \mathcal{L}_{d \to q} $$

$$ \mathcal{L}_{q \to d} = -\frac{1}{N}\sum_{i=1}^N \log \frac{e^{\cos(q_i, d_i)/\tau}}{\sum_{j=1}^N e^{\cos(q_i, d_j)/\tau} + \sum_{j \neq i} e^{\cos(q_i, q_j)/\tau}} $$

$$ \mathcal{L}_{d \to q} = -\frac{1}{N}\sum_{i=1}^N \log \frac{e^{\cos(d_i, q_i)/\tau}}{\sum_{j=1}^N e^{\cos(d_i, q_j)/\tau} + \sum_{j \neq i} e^{\cos(d_i, d_j)/\tau}} $$

温度 $\tau = 0.01$ 固定。これにより**固定バッチサイズ下で追加のフォワードパス（GPUメモリ負荷）なしに実質的な負例数を2倍に拡大**。

##### 【後続モデルへの波及と業界標準化】
GTE が提案した「双方向対称化（$\mathcal{L}_{q \to d} + \mathcal{L}_{d \to q}$）」と「バッチ内の他クエリも負例にする設計」は、**その後のテキスト埋め込みモデル開発における事実上のデファクトスタンダード（業界標準）** として定着した。

| 採用モデル / ツール | 発表時期 | 採用・継承状況 |
|---|:---:|---|
| **Ruri**（東北大 / 理研） | 2024年9月 | GTE 論文を直接引用し、**GTE 方式の改良対照損失を事前学習のコア損失関数としてそのまま採用**（日本語 JMTEB SOTA 獲得）。 |
| **BGE-M3**（BAAI） | 2024年2月 | 密検索（Dense）対照学習において、双方向 In-batch negatives ＋ 教師ありハード負例を統合した損失を採用。 |
| **multilingual-e5 (mE5)** | 2024年2月 | 多言語事前学習・Fine-tuning で双方向対称（Symmetric）対照損失を標準採用。 |
| **Qwen3-Embedding**（Alibaba） | 2025年6月 | GTE 著者陣が開発した最新フラッグシップ。GTE の改良損失をベースに**「5つの負例項 ＋ 偽陰性防止の適応的マスク $m_{ij}$」** へとさらに進化させて採用（MTEB SOTA 獲得）。 |
| **Sentence-Transformers** | - | `MultipleNegativesRankingLoss` など、双方向・相互負例設計が標準の推奨損失関数として OSS 実装。 |

#### ② タスク均質バッチ（Task-homogeneous Batching）
同一バッチ内は**必ず同一データソースのサンプルのみ**で構成。データセット固有の特徴（書式・長さ等のショートカット）でモデルが弁別する現象を防止。

#### ③ 温度付き多項分布サンプリング（Temperature-scaled Sampling）
データセットサイズ $n_i$ に対し、指数 $\alpha = 0.5$ の確率分布 $p_i \propto n_i^\alpha$ でサンプリング。大規模データへの偏りと小規模データの過学習を両立して抑制。

---

## 結果

### Table 2: MTEB ベンチマーク（英語・56データセット）評価結果

| モデル | パラメータ | 分類 (Class. 12) | クラスタ (Clust. 11) | ペア分類 (Pair. 3) | リランク (Rerank 4) | 検索 (Retr. 15) | STS (10) | 要約 (Summ. 1) | **総合平均 (Avg. 56)** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **【教師なしモデル】** | | | | | | | | | |
| Glove | 120M | 57.3 | 27.7 | 70.9 | 43.3 | 21.6 | 61.9 | 28.9 | 42.0 |
| BERT | 110M | 61.7 | 30.1 | 56.3 | 43.4 | 10.6 | 54.4 | 29.8 | 38.3 |
| SimCSE | 110M | 62.5 | 29.0 | 70.3 | 46.5 | 20.3 | 74.3 | 31.2 | 45.5 |
| E5$_\text{small}$ | 30M | 67.0 | 41.7 | 78.2 | 53.1 | 40.8 | 68.8 | 25.2 | 54.2 |
| E5$_\text{base}$ | 110M | 67.9 | 43.4 | 79.2 | 53.5 | 42.9 | 69.5 | 24.3 | 55.5 |
| E5$_\text{large}$ | 330M | 69.0 | 44.3 | 80.3 | 54.4 | 44.2 | 69.9 | 24.8 | 56.4 |
| **GTE$_\text{small}$** | 30M | 71.0 | 44.9 | 82.4 | 57.5 | 43.4 | 77.2 | 30.4 | **58.5** |
| **GTE$_\text{base}$** | 110M | 71.5 | 46.0 | 83.3 | 58.4 | 44.2 | 76.5 | 29.5 | **59.0** |
| **GTE$_\text{large}$** | 330M | 71.8 | 46.4 | 83.3 | 58.8 | 44.6 | 76.3 | 30.1 | **59.3** |
| **【教師ありモデル】** | | | | | | | | | |
| SimCSE | 110M | 67.3 | 33.4 | 73.7 | 47.5 | 21.8 | 79.1 | 23.3 | 48.7 |
| Contriever | 110M | 66.7 | 41.1 | 82.5 | 53.1 | 41.9 | 76.5 | 30.4 | 56.0 |
| GTR$_\text{large}$ | 330M | 67.1 | 41.6 | 85.3 | 55.4 | 47.4 | 78.2 | 29.5 | 58.3 |
| Sentence-T5$_\text{large}$ | 330M | 72.3 | 41.7 | 85.0 | 54.0 | 36.7 | 81.8 | 29.6 | 57.1 |
| E5$_\text{small}$ | 30M | 71.7 | 39.5 | 85.1 | 54.5 | 46.0 | 80.9 | 31.4 | 58.9 |
| E5$_\text{base}$ | 110M | 72.6 | 42.1 | 85.1 | 55.7 | 48.7 | 81.0 | 31.0 | 60.4 |
| E5$_\text{large}$ | 330M | 73.1 | 43.3 | 85.9 | 56.5 | 50.0 | 82.1 | 31.0 | 61.4 |
| InstructOR$_\text{base}$ | 110M | 72.6 | 42.1 | 85.1 | 55.7 | 48.8 | 81.0 | 31.0 | 60.4 |
| InstructOR$_\text{large}$ | 330M | 73.9 | 45.3 | 85.9 | 57.5 | 47.6 | 83.2 | 31.8 | 61.6 |
| OpenAI ada-001 | n.a. | 70.4 | 37.5 | 76.9 | 49.0 | 18.4 | 78.6 | 26.9 | 49.5 |
| OpenAI ada-002 | ~300M | 70.9 | 45.9 | 84.9 | 56.3 | 49.3 | 81.0 | 30.8 | 61.0 |
| **GTE$_\text{small}$** | 30M | 72.3 | 44.9 | 83.5 | 57.7 | 49.5 | 82.1 | 30.4 | **61.4** |
| **GTE$_\text{base}$** | 110M | 73.0 | 46.1 | 84.3 | 58.6 | 51.2 | 82.3 | 30.7 | **62.4** |
| **GTE$_\text{large}$** | 330M | 73.3 | 46.8 | 85.0 | 59.1 | 52.2 | 83.4 | 31.7 | **63.1** |
| **【超大規模モデル】** | | | | | | | | | |
| InstructOR$_\text{xl}$ | 1.5B | 73.1 | 44.7 | 86.6 | 57.3 | 49.3 | 83.1 | 32.3 | 61.8 |
| GTR$_\text{xxl}$ | 4.5B | 67.4 | 42.4 | 86.1 | 56.7 | 48.5 | 78.4 | 30.6 | 59.0 |
| Sentence-T5$_\text{xxl}$ | 4.5B | 73.4 | 43.7 | 85.1 | 56.4 | 42.2 | 82.6 | 30.1 | 59.5 |

---

### Table 3: BEIR ゼロショット検索ベンチマーク（nDCG@10）

| データセット | BM25 | SimCSE | Contriever | CPT-S | E5$_\text{small}$ | E5$_\text{base}$ | E5$_\text{large}$ | GTE$_\text{small}$ | GTE$_\text{base}$ | GTE$_\text{large}$ |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **MS MARCO** | 22.8 | 9.4 | 20.6 | 19.9 | 25.4 | 26.0 | 26.2 | 31.3 | **31.8** | 31.7 |
| **Trec-Covid** | 65.6 | 26.2 | 27.4 | 52.9 | 52.0 | 61.0 | 61.8 | 61.8 | 64.0 | **64.8** |
| **NFCorpus** | 32.5 | 9.9 | 31.7 | 32.0 | 29.3 | 35.8 | 33.7 | 34.9 | 36.2 | **38.1** |
| **NQ** | 32.9 | 11.7 | 25.4 | - | 37.3 | 39.0 | **41.7** | 32.0 | 35.3 | 34.5 |
| **HotpotQA** | 60.3 | 19.8 | 48.1 | 51.5 | 46.0 | **52.4** | 52.2 | 49.3 | 50.8 | 49.2 |
| **FiQA** | 23.6 | 9.8 | 24.5 | 34.1 | 38.3 | 40.0 | **43.2** | 37.0 | 36.9 | 40.6 |
| **ArguAna** | 31.5 | 38.3 | 37.9 | 38.7 | 42.5 | 42.2 | **44.4** | 41.6 | 41.0 | 41.3 |
| **Touche-2020** | 36.7 | 8.9 | 19.3 | 21.0 | 19.9 | 16.9 | **19.8** | 17.7 | 18.2 | 18.5 |
| **CQADupStack** | 29.9 | 13.2 | 28.4 | - | 35.0 | 35.4 | 38.9 | 38.1 | **39.9** | 39.8 |
| **Quora** | 78.9 | 78.0 | 83.5 | 68.1 | 85.8 | 85.7 | **86.1** | **86.1** | 85.0 | 84.8 |
| **DBPedia** | 31.3 | 15.0 | 29.2 | 27.2 | 34.5 | 35.4 | **37.1** | 33.5 | 33.2 | 33.6 |
| **Scidocs** | 15.8 | 5.5 | 14.9 | - | 19.9 | 21.1 | 21.8 | 21.5 | 22.5 | **22.7** |
| **Fever** | 75.3 | 21.1 | 68.2 | 57.1 | 62.5 | 63.4 | 68.6 | 71.3 | **72.7** | 70.5 |
| **Climate-Fever** | 21.3 | 11.8 | 15.5 | 15.8 | 14.5 | 15.4 | 15.7 | 21.4 | 21.0 | **25.4** |
| **Scifact** | 66.5 | 25.7 | 64.9 | 65.4 | 68.5 | 73.7 | 72.3 | 72.7 | **74.1** | **74.1** |
| **平均 (Average)** | 41.7 | 20.3 | 36.0 | - | 40.8 | 42.9 | 44.2 | 43.4 | 44.2 | **44.6** |

---

### Table 1 & 5: CodeSearchNet（コード検索）評価結果

#### Table 1: 1K 候補内検索（MRR）
| モデル | パラメータ | Ruby | JS | Go | Python | Java | PHP | **平均 (Avg.)** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CodeBERT** | 110M $\times$ 6 | 69.3 | 70.6 | 84.0 | 86.8 | 74.8 | 70.6 | 76.0 |
| **GraphCodeBERT** | 110M $\times$ 6 | 84.1 | 73.2 | 87.9 | 75.7 | 71.1 | 72.5 | 77.4 |
| **cpt-code S** | 300M | 86.3 | 86.0 | 97.7 | 99.8 | 94.0 | 96.7 | 93.4 |
| **cpt-code M** | 1.2B | 85.5 | 86.5 | 97.5 | 99.9 | 94.4 | 97.2 | 93.5 |
| **GTE$_\text{base}$** | 110M | 79.6 | 79.4 | 84.2 | 98.8 | 86.8 | 86.8 | **85.9** |

#### Table 5: 全開発・テストセット候補内検索（MRR）
| モデル | パラメータ | Ruby | JS | Go | Python | Java | PHP | **平均 (Avg.)** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CodeBERT** | 110M $\times$ 6 | 67.9 | 62.0 | 88.2 | 67.2 | 67.6 | 62.8 | 69.3 |
| **GraphCodeBERT** | 110M $\times$ 6 | 70.3 | 64.4 | 89.7 | 69.2 | 69.1 | 64.9 | 71.3 |
| **UniXcoder** | 110M $\times$ 6 | 74.0 | 68.4 | 91.5 | 72.0 | 72.6 | 67.6 | 74.4 |
| **CodeRetriever** | 110M $\times$ 6 | 77.1 | 71.9 | 92.4 | 75.8 | 76.5 | 70.8 | 77.4 |
| **GTE$_\text{base}$** | 110M | 76.1 | 73.6 | 88.1 | 95.9 | 80.1 | 85.3 | **83.2** |

---

## 分析（Ablation Study）

### 1. 多段階学習の影響（Influence of Different Training Stages / Section 5.3）

BERT-base（110M）を用い、学習戦略の違いによる MTEB 56タスク平均スコアの差分を検証：

| 設定 (Setting) | 学習内容 | MTEB 平均スコア | Full（多段階）との差分 |
|---|---|:---:|:---:|
| **① FT のみ (Solely Fine-tuning)** | 教師ありデータ（~300万件）のみで学習 | **57.8** | -4.6 pt |
| **② PT のみ (Solely Pre-training)** | 教師なしテキストペア（~8億件）のみで対照事前学習 | **59.0** | -3.4 pt |
| **③ Full (PT $\to$ FT)** | **事前学習（PT）後に教師あり Fine-tuning（FT）を実施（提案手法）** | **62.4** | **基準 (+4.6 pt / +3.4 pt)** |

**重要考察:**
1. **教師あり単体（FTのみ: 57.8）の限界**: 高品質なラベル付きデータでも、件数が数百〜数千万件では汎用空間の獲得に不足。
2. **教師なし事前学習（PTのみ: 59.0）の優位性**: 8億ペアの Web データによる事前学習単体（59.0）が、教師あり単体（57.8）を **+1.2 pt 上回る**。広大な表現空間の事前獲得が不可欠。
3. **多段階学習の相乗効果**: 事前学習後に教師あり FT を行うことで、さらに **+3.4 pt（59.0 $\to$ 62.4）大幅に性能が跳ね上がる**。

---

### 2. モデルスケール別の PT / FT スコア推移（Section 5.1）

| モデルスケール | パラメータ数 | Stage 1（PT のみ） | Stage 2（PT $\to$ FT 完了後） | 向上幅 |
|---|:---:|:---:|:---:|:---:|
| **GTE-small** | 30M (MiniLM) | 58.5 | **61.4** | **+2.9 pt** |
| **GTE-base** | 110M (BERT-base) | 59.0 | **62.4** | **+3.4 pt** |
| **GTE-large** | 330M (BERT-large) | 59.3 | **63.1** | **+3.8 pt** |

---

### 3. バッチサイズの影響（Section 5.1）

| バッチサイズ ($B$) | MTEB 平均スコア (PT) |
|:---:|:---:|
| **2,048** | 56.78 |
| **4,096** | 57.27 |
| **8,192** | 58.99 |
| **16,384** | **59.03 (飽和)** |

- バッチサイズは約 10,000 付近で性能が飽和し、それ以上の拡大では追加ゲインが得られない。

---

### 4. 改良対照損失の効果（Section 5.5）

| 損失関数設定 | Stage 1 (PT) | Stage 2 (FT) |
|---|:---:|:---:|
| **Vanilla InfoNCE (一方向)** | 57.3 | 61.8 |
| **改良対照損失 (GTE / 双方向・4方向)** | **57.8 (+0.5 pt)** | **62.4 (+0.6 pt)** |

---

### 5. データサンプリング比率 $\alpha$ の影響（Section 5.4）

| サンプリング指数 $\alpha$ | 検索 (Retrieval) | STS | MTEB 総合平均 |
|:---:|:---:|:---:|:---:|
| **$\alpha = 0$ (一様サンプリング)** | 36.7 | 73.2 | 55.4 |
| **$\alpha = 0.3$** | 44.6 | 75.9 | 58.9 |
| **$\alpha = 0.5$ (提案設定)** | 44.2 | **76.5** | **59.0** |
| **$\alpha = 1.0$ (サイズ比例)** | 42.0 | 75.5 | 58.3 |

---

## 貢献と限界

### 貢献
- **オープンソースデータのみで SOTA 達成**: 非公開データに頼らず、MTEB で OpenAI ada-002 を上回る精度を実証。
- **改良対照損失（双方向・4方向）の提案**: 固定バッチサイズで負例数を倍増させる手法を確立（Ruri や後続モデルに継承）。
- **タスク均質バッチと $\alpha=0.5$ サンプリング**: マルチタスク対照学習の標準ベストプラクティスを提示。
- **コード検索への高い汎化性**: プログラミング言語特化のチューニングなしに高いコード検索能力を獲得。

### 限界
- **コンテキスト長 512 トークン**: 長文処理に非対応。
- **英語特化**: 多言語対応は未実施。
- **双方向アテンション（BERT型）に限定**: 生成タスクとの統合は対象外。
