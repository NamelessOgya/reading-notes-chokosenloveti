# F2LLM Technical Report: Matching SOTA Embedding Performance with 6 Million Open-Source Data

**arXiv:** 2510.02294  
**著者:** Ziyin Zhang$^{1,2}$, Zihan Liao$^{1}$, Hang Yu$^{1}$, Peng Di$^{1}$, Rui Wang$^{2}$（$^{1}$Ant Group, $^{2}$Shanghai Jiao Tong University）  
**発表:** 2025年10月  
**リポジトリ:** [GitHub (CodeFuse-Embeddings)](https://github.com/codefuse-ai/CodeFuse-Embeddings) / [HuggingFace Collection](https://huggingface.co/collections/codefuse-ai/codefuse-embeddings-68d4b32da791bbba993f8d14)  

---

## 一言まとめ
数十億件の事前学習や高コストなLLM合成データ、複雑な多段階学習パイプラインを一切使わず、**公開されている非合成データセットのみから厳選した600万件（6M）のタプル**を用いてQwen3基盤モデルを単一段階（Single Stage）で直接ファインチューニングした埋め込みモデルファミリー（0.6B, 1.7B, 4B）。4Bモデルはクラスタリングで **68.54** という全モデル中歴代最高スコアを樹立し、1.7Bモデルは1B〜2Bクラスで世界1位を達成。チェックポイント・学習データ・学習コードが完全オープンソース化されている。

### 💡 わずか600万件（6M）で高精度・SOTAを達成できた理由（主要な工夫点）
- **マージンベース適応型ハード負例マイニング（勾配情報密度の最大化）**:
  - **偽陰性（False Negative）の徹底排除**: 検索上位5件（Top-5）を無条件除外し、「実は正解」な文書が負例に混ざって埋め込み空間が破壊されるのを防止。
  - **二重マージンフィルタ**: 類似度スコア0.8未満 かつ 正例スコアの95%未満（$\text{score} < 0.95 \times \text{score}_{\text{pos}}$）の「正例より確実に遠いが、難易度の高い境界線」にある負例のみを厳選。
  - **妥協なき破棄基準**: 24件の高品質負例が揃わないクエリはデータごと破棄。薄いデータによる事前学習を不要にするほど、1サンプルあたりの学習情報（勾配の質）を極限まで濃縮。
- **マルチタスク分離損失制御（高いサンプル効率の達成）**:
  - 分類やクラスタリングで同一カテゴリの文同士を誤って反発させないため、ハード負例損失（$\ell_{\text{hard}}$）は全タスク共通で計算しつつ、バッチ内負例損失（$\ell_{\text{in-batch}}$）は**検索タスクのバッチでのみ計算**するようカスタムデータローダーで制御。
  - 先行研究（NV-Embed等）のようにバッチ内損失を完全OFFにすることなく、検索の大規模バッチ（512件）対照シグナルを100%活用し、極めて高いサンプル効率を実現。
- **多様でバランスの取れたタスク設計（4.9M検索 ＋ 0.8Mクラスタリング ＋ 0.2M分類）**:
  - 検索・QA・要約・NLI・STS・重複検出を統一タプル形式に統合。
  - 同一クラスタを正例、他クラスタ24件をハード負例とするクラスタリングデータ（0.8M）の学習が功を奏し、クラスタリングで歴代世界1位（68.54）を記録。
- **基盤LLM（Qwen3）の言語能力を壊さないシンプルな設計（Simplicity is Best）**:
  - 双方向アテンション化や複雑なプーリング層の追加を行わず、LLM本来の「Causal Attention ＋ Last Token Pooling」を維持。事前学習で獲得した推論・言語理解能力を損なわずに単一段階（Single Stage）で直接埋め込み空間へ転移。

---

## 背景

近年、LLMをベースにしたテキスト埋め込みモデルは、情報検索、クラスタリング、分類、RAGなどの広範なタスクにおいて急速に発展し、MTEBリーダーボードの上位を独占している。これらのモデルは、MistralやQwen3などの基盤LLMが事前学習で獲得した高度な言語理解能力を、クエリと文書のペアに対する対照学習によって埋め込み表現空間へ転移させている。

しかし、既存の最高峰（SOTA）埋め込みモデルには以下の深刻な課題と制約が存在していた：

1. **極めて高コストな学習パイプライン**: 数億〜数十億スケールの弱教師あり事前学習（大規模コントラスト事前学習）や、多段階にわたる複雑な学習ステップを必要とする。
2. **高価なLLM合成データへの依存**: E5-Mistral、Gecko、NV-Embed、Gemini Embedding、Qwen3-Embeddingなど、多くのSOTAモデルが高性能なLLMで大量生成した合成データに依存しており、計算コスト・APIコストが莫大である。
3. **再現性（Reproducibility）の欠如**: 多くの研究ではモデルの重み（チェックポイント）のみが公開され、学習データや学習コードが非公開であるため、研究コミュニティでの追試や低予算でのモデル改良が困難であった。
4. **アーキテクチャ改変のトレードオフ**: 因果マスクの撤廃（双方向化）や特殊なプーリング層の追加は、計算コストを増大させるか、必ずしも安定した性能向上につながらない（BGE-ICL等での指摘）。

著者らはこれらの課題を打破するため、**「基盤モデルのアーキテクチャや入力を一切改変せず、オープンソースの非合成データのみから構築した600万件の高品質データセットを用いて、単一段階の直接ファインチューニングを行う」** というアプローチ（F2LLM: Foundation to Feature Large Language Models）を提案した。

---

## 手法

F2LLMは、基盤モデル（Backbone）として Qwen3（0.6B, 1.7B, 4B）を採用し、大規模な弱教師あり事前学習を挟まず、厳選されたデータセットによる単一段階の対照ファインチューニングを直接実施する。

### 1. 統一データフォーマットとタスク指示文（Instruction）の付加

検索（4.9M）、分類（0.2M）、クラスタリング（0.8M）の3つの異なるタスク群を、統一された $( \text{Query}, \text{Positive Passage}, \text{Hard Negative} \times n )$ のタプル形式に統合。クエリには以下のフォーマットでタスク固有の指示文を付加する：

$$ q_{\text{inst}} = \texttt{Instruct: \{task\_instruction\} }\backslash\texttt{n Query:} \{q\} $$

### 2. マージンベース適応型ハード負例マイニング（Margin-Based Adaptive Hard Negative Mining）

- **検索・QA・要約データ**:
  - 各クエリに対し、Qwen3-Embedding-0.6B を用いてTop 100件の関連パッセージを検索。
  - 偽陰性（False Negative＝実質的な正解）の混入を防ぐため、上位5件（Top 5）を除外。
  - 類似度スコアが 0.8 未満 かつ 正例の類似度スコアより 95% 未満（$\text{score} < 0.95 \times \text{score}_{\text{pos}}$）の候補のみをフィルタリング。
  - 残った候補から上位24件をハード負例として選定（24件未満の場合はクエリごと破棄）。
  - 要約データセット（XSum, CNN/DM）は、本文をパッセージ、要約文をクエリとしてこの枠組みに統合。
- **自然言語推論（NLI）**:
  - 含意（Entailment）の仮説を正例とし、中立（Neutral）や矛盾（Contradiction）の仮説をハード負例として追加。不足分は上記マイニングで補完。
- **意味的類似度（STS）**:
  - 類似度スコア4以上のペアをクエリ・正例ペアとし、クエリと正例を反転させたペアも追加。
- **重複検出（QQP等）**:
  - 重複質問を正例ペアとし、同様にハード負例をマイニング。
- **2値分類データ**:
  - 入力文をクエリ、正解クラス名（例: "toxic"）を正例パッセージ、別クラス名（例: "not toxic"）を1つのハード負例として構成。
- **多クラス分類・クラスタリングデータ**:
  - 同一クラス／クラスタ内の別サンプルを正例パッセージとし、他クラス／クラスタから24件をハード負例として選定。

### 3. 損失関数とマルチタスクデータローダー

各クエリ $q_i$ 、正例文書 $d_i^+$ 、 $n$ 個のハード負例文書 $d_{i,1}^-, \dots, d_{i,n}^-$ に対し、温度パラメータ $\tau = 0.05$ とコサイン類似度 $s(\cdot)$ を用いて以下の損失を定義する。

- **ハード負例損失（Hard Negative Loss）**:

$$ \ell_\text{hard} = - \log\frac{e^{s(q_i,d_i^+)/\tau}}{e^{s(q_i,d_i^+)/\tau}+\sum\limits_{j=1}^{n}e^{s(q_i,d_{i,j}^-)/\tau}} $$

- **In-batch 負例損失（In-batch Loss）**:

$$ \ell_\text{in-batch} = - \log\frac{e^{s(q_i,d_i^+)/\tau}}{\sum\limits_{j=1}^{B}e^{s(q_i,d^+_j)/\tau}} $$

- **総合損失（Total Loss）**:

$$ \ell = \ell_\text{hard} + \ell_\text{in-batch} $$

- **マルチタスクデータローダーの工夫**:
  - 各 micro batch（単一GPU内）のサンプルは同一データソースからサンプリング。
  - 各GPUはデータセットのサイズに比例した確率で独立にサンプリングし、全データセットが均等に1エポックを終了するように制御。
  - 検索・クラスタリングでは24件の負例プールから7件をランダムサンプリング（分類は1件）。
  - **ハード負例損失は全タスクで各GPUごとに独立計算**されるが、**In-batch損失は検索タスクのみに適用され、全GPU（mini batch全体）のパッセージを集約して計算**される。これにより、非検索データを混合した際にも高いサンプル効率を維持する。

---

## 結果

### Figure 1: 性能比較および性能・データ量・モデルサイズのトレードオフ

![Figure 1 (Left): MTEB performance comparison](./images/performance.png)
![Figure 1 (Right): Balance between embedding performance, training data, and model size](./images/balance.png)

- **左図（Figure 1 Left: MTEB performance comparison）**: パラメータサイズ別のMTEBスコア比較。F2LLMシリーズ（0.6B, 1.7B, 4B）は、同等パラメータ帯の既存SOTAモデルと拮抗または凌駕する性能を示す。
- **右図（Figure 1 Right: Balance）**: 性能（上方向＝高スコア）、学習データ数（右方向＝少ないデータ数）、モデルサイズ（手前／下方向＝小さいパラメータ）の3軸におけるバランス。F2LLM（4Bおよび1.7B）は、わずか6Mの非合成データと軽量なモデルサイズでありながら、数億データや8Bクラスの巨大モデルに匹敵する極めて優れたパレート最適性を達成している。

---

### Table 1: F2LLM 学習ハイパーパラメータ (Hyperparameters for training F2LLM models)

| Model | Learning Rate | Global Batch Size | Num. GPUs | Micro Batch Size |
|---|:---:|:---:|:---:|:---:|
| 0.6B | 1e-5 | 512 | 16 | 32 |
| 1.7B | 9e-6 | 512 | 16 | 32 |
| 4B | 8e-6 | 512 | 32 | 16 |

- 全モデル共通設定: AdamW オプティマイザ、コサイン学習率減衰（Cosine LR decay）、2エポック学習、500 warmup steps、最大入力長 1024 トークン、ZeRO stage 2、Flash Attention 2、Gradient Checkpointing 有効。

---

### Table 2: MTEB 英語リーダーボード評価結果 (Top models on the MTEB leaderboard)

※「Average」列は全41タスクのマイクロ平均値。

| Model | Classification | Clustering | PairClassification | Reranking | Retrieval | STS | Summarization | **Average** | **Rank** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **【Closed-source】** | | | | | | | | | |
| Seed1.5-Embedding | 89.88 | 60.83 | 87.39 | 50.67 | 67.45 | 87.23 | 36.44 | 74.76 | 3 |
| Seed1.6-Embedding | 92.42 | 59.22 | 85.07 | 50.28 | 64.90 | 86.87 | 37.10 | 74.07 | 6 |
| Gemini Embedding | 90.05 | 59.39 | 87.70 | 48.60 | 64.35 | 85.29 | 38.28 | 73.30 | 8 |
| **【7-8B】** | | | | | | | | | |
| QZhou-Embedding 7B | 88.97 | 61.65 | 92.43 | 51.77 | 67.12 | 91.65 | 33.05 | 75.97 | 1 |
| Qwen3-Embedding 8B | 90.43 | 58.57 | 87.52 | 51.56 | 69.44 | 88.58 | 34.83 | 75.22 | 2 |
| LGAI-Embedding 7B | 89.97 | 59.25 | 88.67 | 49.13 | 66.18 | 86.69 | 38.93 | 74.12 | 5 |
| GTE-Qwen2 7B | 88.52 | 58.97 | 85.90 | 50.47 | 58.09 | 82.69 | 35.74 | 70.72 | 11 |
| GeoEmbedding 7B | 89.67 | 56.50 | 82.51 | 48.32 | 60.91 | 80.60 | 30.43 | 70.21 | 13 |
| **【4B】** | | | | | | | | | |
| Qwen3-Embedding 4B | 89.84 | 57.51 | 87.01 | 50.76 | 68.46 | 88.72 | 34.39 | 74.60 | 4 |
| **F2LLM 4B** | **91.68** | **68.54** | **83.75** | **50.05** | **59.63** | **84.20** | **33.19** | **73.67** | **7** |
| **【1-2B】** | | | | | | | | | |
| **F2LLM 1.7B** | **90.86** | **64.13** | **83.27** | **49.84** | **57.83** | **83.90** | **29.88** | **72.01** | **9** |
| Jasper 2B | 90.27 | 60.52 | 88.14 | 50.00 | 56.05 | 84.37 | 37.19 | 71.41 | 10 |
| **【<1B】** | | | | | | | | | |
| Qwen3-Embedding 0.6B | 85.76 | 54.05 | 84.37 | 48.18 | 61.83 | 86.57 | 33.43 | 70.70 | 12 |
| **F2LLM 0.6B** | **90.56** | **60.36** | **81.49** | **47.88** | **55.70** | **82.48** | **24.54** | **70.03** | **14** |

#### 結果の考察
- **総合性能**: 数億件のデータで事前学習されたモデルや数B〜数十Bの巨大モデルと比べ、わずか6M件の公開データで学習したF2LLM-4Bが総合7位（73.67 pt）、4Bサイズ帯で2位を記録。
- **クラスタリング性能（Clustering）**: F2LLM-4Bは **68.54** を記録し、全モデル（QZhou 7BやQwen3 8B、Seed1.6等）を大きく引き離して**歴代世界最高スコア**を樹立。F2LLM-1.7Bも **64.13** と全7Bモデルを凌駕。
- **モデルサイズ帯別の優位性**:
  - **1B〜2Bサイズ帯**: F2LLM-1.7B（72.01 pt）が Jasper 2B（71.41 pt）を抑えて**世界1位**を獲得。
  - **1B未満サイズ帯**: F2LLM-0.6B（70.03 pt）が第2位。分類（90.56 vs 85.76）やクラスタリング（60.36 vs 54.05）においてQwen3-Embedding 0.6Bを圧倒。

---

### Table 3: 学習用分類・クラスタリングデータセット一覧 (Classification and clustering datasets used for training F2LLM)

※クエリ長・コーパス長はQwen3トークナイザーによるトークン数（クエリ長は指示文を含む）。

| Dataset | Type | # Query | Corpus Size | Query Length | Corpus Length | Source | URL |
|---|:---:|:---:|:---:|:---:|:---:|---|---|
| Amazon Counterfactual | Classification | 8,663 | 2 | 47 | 4 | \citet{2021Amazon-Counterfactual} | https://huggingface.co/datasets/mteb/amazon_counterfactual |
| Amazon Polarity | Classification | 100,000 | 2 | 115 | 2 | \citet{2013Amazon-Reviews} | https://huggingface.co/datasets/mteb/amazon_polarity |
| IMDb | Classification | 24,904 | 2 | 314 | 2 | \citet{2011IMDB} | https://huggingface.co/datasets/mteb/imdb |
| Toxic Conversations | Classification | 49,900 | 2 | 84 | 3 | \citet{2019Toxic-Conversations} | https://huggingface.co/datasets/mteb/toxic_conversations_50k |
| CoLA | Classification | 9,571 | 2 | 28 | 2 | \citet{2019CoLA} | https://gluebenchmark.com/tasks |
| Amazon Reviews | Clustering | 100,000 | 99,966 | 63 | 48 | \citet{2013Amazon-Reviews} | https://huggingface.co/datasets/mteb/amazon_reviews_multi |
| Banking77 | Clustering | 9,993 | 9,993 | 31 | 15 | \citet{2020Banking77} | https://huggingface.co/datasets/mteb/banking77 |
| Emotion | Clustering | 17,944 | 17,944 | 54 | 21 | \citet{2018Emotion} | https://huggingface.co/datasets/mteb/emotion |
| MTOP Intent | Clustering | 17,896 | 17,862 | 28 | 9 | \citet{2021MTOP} | https://huggingface.co/datasets/mteb/mtop_intent |
| MTOP Domain | Clustering | 17,538 | 17,531 | 29 | 10 | \citet{2021MTOP} | https://huggingface.co/datasets/mteb/mtop_domain |
| Massive Scenario | Clustering | 13,547 | 13,488 | 26 | 8 | \citet{2023MASSIVE} | https://huggingface.co/datasets/mteb/amazon_massive_scenario |
| Massive Intent | Clustering | 13,547 | 13,488 | 26 | 8 | \citet{2023MASSIVE} | https://huggingface.co/datasets/mteb/amazon_massive_intent |
| Tweet Sentiment Extraction | Clustering | 26,732 | 26,732 | 40 | 19 | \citet{2020tweet-sentiment-extraction} | https://huggingface.co/datasets/mteb/tweet_sentiment_extraction |
| Arxiv-Clustering-P2P | Clustering | 83,476 | 299,733 | 245 | 222 | \citet{2022mteb-arxiv} | https://huggingface.co/datasets/mteb/raw_arxiv |
| Arxiv-Clustering-S2S | Clustering | 83,486 | 299,630 | 38 | 17 | \citet{2022mteb-arxiv} | https://huggingface.co/datasets/mteb/raw_arxiv |
| Biorxiv-Clustering-P2P | Clustering | 57,296 | 57,215 | 360 | 338 | \citet{2022mteb-biorxiv} | https://huggingface.co/datasets/mteb/raw_biorxiv |
| Biorxiv-Clustering-S2S | Clustering | 57,296 | 57,204 | 42 | 22 | \citet{2022mteb-biorxiv} | https://huggingface.co/datasets/mteb/raw_biorxiv |
| Medrxiv-Clustering-P2P | Clustering | 18,659 | 18,653 | 453 | 431 | \citet{2022mteb-medrxiv} | https://huggingface.co/datasets/mteb/raw_medrxiv |
| Medrxiv-Clustering-S2S | Clustering | 18,659 | 18,652 | 45 | 25 | \citet{2022mteb-medrxiv} | https://huggingface.co/datasets/mteb/raw_medrxiv |
| Reddit-Clustering-P2P | Clustering | 80,000 | 489,218 | 194 | 175 | \citet{2021Reddit-Clustering-P2P} | https://huggingface.co/datasets/sentence-transformers/reddit-title-body |
| Reddit-Clustering-S2S | Clustering | 58,141 | 104,725 | 34 | 15 | \citet{2021Reddit-StackExchange-Clustering-S2S} | https://github.com/UKPLab/TWEAC-qa-agent-selection/tree/master/data/reddit/train |
| StackExchange-Clustering-P2P | Clustering | 80,000 | 430,913 | 304 | 281 | \citet{2021StackExchange-Clustering-P2P} | https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_title_body_jsonl |
| StackExchange-Clustering-S2S | Clustering | 56,731 | 674,714 | 32 | 13 | \citet{2021Reddit-StackExchange-Clustering-S2S} | https://github.com/UKPLab/TWEAC-qa-agent-selection/tree/master/data/stackexchange/train |
| TwentyNewsgroups | Clustering | 11,060 | 10,994 | 230 | 216 | \citet{1995TwentyNewsGroups} | https://huggingface.co/datasets/SetFit/20_newsgroups |
| **Total** | **Classification** | **193,038** | **10** | - | - | - | - |
| **Total** | **Clustering** | **822,001** | **2,678,655** | - | - | - | - |

---

### Table 4: 学習用検索データセット一覧 (Retrieval datasets used for training F2LLM)

| Dataset | Type | # Query | Corpus Size | Query Length | Corpus Length | Source | URL |
|---|:---:|:---:|:---:|:---:|:---:|---|---|
| Arguana | Retrieval | 22,848 | 8,561 | 25 | 210 | \citet{2018Arguana} | https://huggingface.co/datasets/BeIR/arguana-generated-queries |
| SNLI | Retrieval | 54,585 | 320,753 | 32 | 10 | \citet{2015SNLI} | https://huggingface.co/datasets/stanfordnlp/snli |
| MNLI | Retrieval | 112,075 | 358,808 | 42 | 14 | \citet{2018MNLI} | https://huggingface.co/datasets/nyu-mll/multi_nli |
| ANLI | Retrieval | 18,801 | 104,706 | 95 | 14 | \citet{2020ANLI} | https://huggingface.co/datasets/facebook/anli |
| PAQ | Retrieval | 938,771 | 2,492,657 | 30 | 145 | \citet{2021PAQ} | https://huggingface.co/datasets/sentence-transformers/paq |
| SQuAD | Retrieval | 89,509 | 20,951 | 30 | 162 | \citet{2016SQuAD} | https://huggingface.co/datasets/rajpurkar/squad |
| StackExchange | Retrieval | 754,705 | 2,401,305 | 231 | 245 | \citet{2021StackExchangeDataset} | https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_titlebody_best_voted_answer_jsonl |
| MSMARCO | Retrieval | 365,503 | 4,472,684 | 26 | 82 | \citet{2016MSMARCO} | https://huggingface.co/datasets/mteb/msmarco |
| Natural Questions | Retrieval | 97,209 | 75,178 | 30 | 145 | \citet{2019NaturalQuestions} | https://huggingface.co/datasets/sentence-transformers/natural-questions |
| HotpotQA | Retrieval | 120,528 | 1,217,525 | 45 | 103 | \citet{2018HotpotQA} | https://huggingface.co/datasets/mteb/hotpotqa |
| FEVER | Retrieval | 106,605 | 441,174 | 31 | 324 | \citet{2018FEVER} | https://huggingface.co/datasets/mteb/fever |
| ELI5 | Retrieval | 161,345 | 215,884 | 42 | 229 | \citet{2019ELI5} | https://huggingface.co/datasets/Pavithree/eli5 |
| FiQA2018 | Retrieval | 7,452 | 32,615 | 33 | 234 | \citet{2018FIQA} | https://huggingface.co/datasets/mteb/fiqa |
| BioASQ | Retrieval | 125,248 | 149,900 | 27 | 295 | \citet{2015BioASQ} | https://huggingface.co/datasets/BeIR/bioasq-generated-queries |
| NFCorpus | Retrieval | 1,283 | 3,270 | 23 | 333 | \citet{2016NFCorpus} | https://huggingface.co/datasets/mteb/nfcorpus |
| MIRACL | Retrieval | 3,379 | 31,129 | 27 | 158 | \citet{2023MIRACL} | https://huggingface.co/datasets/miracl/miracl |
| Mr.TyDi | Retrieval | 3,547 | 79,695 | 27 | 148 | \citet{2021mrtidy} | https://huggingface.co/datasets/mteb/mrtidy |
| SciFact | Retrieval | 859 | 4,506 | 40 | 353 | \citet{2020SciFact} | https://huggingface.co/datasets/mteb/scifact |
| TriviaQA | Retrieval | 60,025 | 1,014,344 | 36 | 149 | \citet{2017TriviaQA} | https://huggingface.co/datasets/sentence-transformers/trivia-qa-triplet |
| COLIEE | Retrieval | 454 | 532 | 61 | 123 | \citet{2022COLIEE} | https://www.modelscope.cn/datasets/sentence-transformers/coliee |
| PubMedQA | Retrieval | 60,227 | 61,233 | 39 | 314 | \citet{2019PubMedQA} | https://huggingface.co/datasets/qiaojin/PubMedQA |
| S2ORC-Title-Abstract | Retrieval | 250,000 | 2,476,989 | 34 | 136 | \citet{2020S2ORC} | https://huggingface.co/datasets/sentence-transformers/s2orc |
| S2ORC-Title-Citation | Retrieval | 132,879 | 1,619,105 | 36 | 21 | \citet{2020S2ORC} | https://huggingface.co/datasets/sentence-transformers/s2orc |
| S2ORC-Abstract-Citation | Retrieval | 231,587 | 1,615,793 | 259 | 256 | \citet{2020S2ORC} | https://huggingface.co/datasets/sentence-transformers/s2orc |
| Amazon QA | Retrieval | 59,340 | 894,812 | 43 | 69 | \citet{2019AmazonQA} | https://github.com/amazonqa/amazonqa |
| SPECTER | Retrieval | 24,717 | 199,028 | 38 | 14 | \citet{2020SPECTER} | https://huggingface.co/datasets/sentence-transformers/specter |
| XSum | Retrieval | 184,383 | 214,562 | 44 | 459 | \citet{2018XSum} | https://huggingface.co/datasets/EdinburghNLP/xsum |
| CNN\_DM | Retrieval | 100,000 | 290,602 | 82 | 766 | \citet{2015CNN-DM} | https://huggingface.co/datasets/abisee/cnn_dailymail |
| Sentence Compression | Retrieval | 175,477 | 175,477 | 26 | 33 | \citet{2013Sentence-Compression} | https://huggingface.co/datasets/sentence-transformers/sentence-compression |
| StackExchange-DupQuestions-S2S | Retrieval | 183,559 | 158,628 | 31 | 14 | \citet{2021Embedding-Training-Data} | https://huggingface.co/datasets/sentence-transformers/stackexchange-duplicates |
| StackExchange-DupQuestions-P2P | Retrieval | 203,060 | 124,283 | 189 | 180 | \citet{2021Embedding-Training-Data} | https://huggingface.co/datasets/sentence-transformers/stackexchange-duplicates |
| QQP | Retrieval | 243,598 | 445,064 | 31 | 13 | \citet{2019QQP} | https://gluebenchmark.com/tasks |
| StackOverflow-DupQuestions | Retrieval | 19,847 | 315,577 | 27 | 11 | \citet{2018StackOverflowDupQuestions} | https://huggingface.co/datasets/mteb/stackoverflowdupquestions-reranking |
| STS12 | Retrieval | 1,858 | 2,612 | 40 | 27 | \citet{2012STS12} | https://huggingface.co/datasets/mteb/sts12-sts |
| STS22 | Retrieval | 389 | 1,380 | 505 | 494 | \citet{2022STS22} | https://huggingface.co/datasets/mteb/sts22-crosslingual-sts |
| STSBenchmark | Retrieval | 3,297 | 9,247 | 25 | 14 | \citet{2021STSBenchmark} | https://huggingface.co/datasets/mteb/stsbenchmark-sts |
| **Total** | **Retrieval** | **4,918,949** | **22,050,569** | - | - | - | - |

---

### Table 5: MTEB 評価タスク用指示文 (Instructions for evaluation tasks in MTEB)

| Task | Instruction |
|---|---|
| AmazonCounterfactual-Classification | Classify a given Amazon customer review text as either counterfactual or not counterfactual. |
| ArXivHierarchical-ClusteringP2P | Identify the main and secondary category of arXiv papers based on the titles and abstracts. |
| ArXivHierarchical-ClusteringS2S | Identify the main and secondary category of arXiv papers based on the titles. |
| ArguAna | Given a claim, find documents that refute the claim. |
| AskUbuntuDupQuestions | Retrieve duplicate questions from AskUbuntu forum. |
| BIOSSES | Retrieve semantically similar text. |
| Banking77Classification | Given an online banking query, find the corresponding intents. |
| BiorxivClusteringP2P.v2 | Identify the main category of bioRxiv papers based on the titles and abstracts. |
| CQADupstack-GamingRetrieval | Given a question, retrieve questions that are semantically equivalent. |
| CQADupstack-UnixRetrieval | Given a question, retrieve questions that are semantically equivalent. |
| ClimateFEVER-HardNegatives | Given a claim about climate change, retrieve documents that support or refute the claim. |
| FEVERHardNegatives | Given a claim, retrieve documents that support or refute the claim. |
| FiQA2018 | Given a financial question, retrieve passages that answer the question. |
| HotpotQAHardNegatives | Given a multi-hop question, retrieve passages that answer the question. |
| ImdbClassification | Classify the sentiment expressed in the given movie review text from the IMDB dataset. |
| MTOPDomainClassification | Classify the intent domain of the given utterance in task-oriented conversation. |
| MassiveIntentClassification | Given a user utterance as query, find the user intents. |
| MassiveScenario-Classification | Given a user utterance as query, find the user scenarios. |
| MedrxivClusteringP2P.v2 | Identify the main category of medRxiv papers based on the titles and abstracts. |
| MedrxivClusteringS2S.v2 | Identify the main category of medRxiv papers based on the titles. |
| MindSmallReranking | Retrieve relevant news articles based on user browsing history. |
| SCIDOCS | Given a scientific paper title, retrieve paper abstracts that are cited by the given paper. |
| SICK-R | Retrieve semantically similar text. |
| STS12, STS13, STS14, STS15, STS17, STS22.v2, STSBenchmark | Retrieve semantically similar text. |
| SprintDuplicateQuestions | Retrieve duplicate questions from Sprint forum. |
| StackExchange-Clustering.v2 | Identify the topic or theme of StackExchange posts based on the titles. |
| StackExchange-ClusteringP2P.v2 | Identify the topic or theme of StackExchange posts based on the given paragraphs. |
| SummEval-Summarization.v2 | Given a news summary, retrieve other semantically similar summaries. |
| TRECCOVID | Given a query on COVID-19, retrieve documents that answer the query. |
| Touche2020Retrieval.v3 | Given a question, retrieve passages that answer the question. |
| ToxicConversations-Classification | Classify the given comments as either toxic or not toxic. |
| TweetSentimentExtraction-Classification | Classify the sentiment of a given tweet as either positive, negative, or neutral |
| TwentyNewsgroups-Clustering.v2 | Identify the topic or theme of the given news articles. |
| TwitterSemEval2015 | Retrieve tweets that are semantically similar to the given tweet. |
| TwitterURLCorpus | Retrieve tweets that are semantically similar to the given tweet. |

---

### Table 6: 学習データ用指示文 (Instructions for training data of F2LLM)

| Dataset | Type | Instruction |
|---|---|---|
| Arguana, SQuAD, BioASQ, NFCorpus, MIRACL, Mr.TyDi | Retrieval | Given a question, retrieve passages that answer the question. |
| PAQ, StackExchange, MSMARCO, Natural Questions | Retrieval | Given a web search query, retrieve relevant passages that answer the query. |
| SNLI, MNLI, ANLI | Retrieval | Given a premise, retrieve hypotheses that are entailed by the premise. |
| HotpotQA | Retrieval | Given a multi-hop question, retrieve passages that answer the question. |
| FEVER | Retrieval | Given a claim, retrieve documents that support or refute the claim. |
| ELI5 | Retrieval | Given a question from Reddit ELI5 forum, retrieve passages that answer it. |
| FiQA2018 | Retrieval | Given a financial question, retrieve passages that answer the question. |
| SciFact | Retrieval | Given a scientific claim, retrieve passages that support or refute the claim. |
| TriviaQA | Retrieval | Given a trivia question, retrieve passages that can answer it. |
| COLIEE | Retrieval | Given a legal statement, retrieve articles that support it. |
| PubMedQA | Retrieval | Given a question, retrieve paper abstracts from PubMed that can answer it. |
| S2ORC-Title-Abstract | Retrieval | Given a paper's title, retrieve the corresponding abstract. |
| S2ORC-Title-Citation | Retrieval | Given a paper's title, retrieve papers that cite it. |
| S2ORC-Abstract-Citation | Retrieval | Given a paper's abstract, retrieve abstract of papers that cite it. |
| Amazon QA | Retrieval | Given a question about a product, retrieve Amazon reviews that can help answer it. |
| SPECTER | Retrieval | Given a scientific paper title, retrieve paper titles that are cited by the given paper. |
| XSum, CNN\_DM | Retrieval | Given a news summary, retrieve the original news article. |
| Sentence Compression | Retrieval | Given a compressed sentence, retrieve the original sentence before compression. |
| QQP, StackExchange-DupQuestions-S2S, StackExchange-DupQuestions-P2P | Retrieval | Given a question, retrieve questions that are semantically equivalent. |
| StackOverflow-DupQuestions | Retrieval | Retrieve duplicate questions from StackOverflow forum. |
| STS12, STS22, STSBenchmark | Retrieval | Retrieve semantically similar text. |
| Amazon Counterfactual | Classification | Classify a given Amazon customer review text as either counterfactual or not counterfactual. |
| Amazon Polarity | Classification | Classify the given Amazon review into positive or negative sentiment. |
| IMDb | Classification | Classify the sentiment expressed in the given movie review text from the IMDB dataset. |
| Toxic Conversations | Classification | Classify the given comments as either toxic or not toxic. |
| CoLA | Classification | Classify the given sentence as linguistically acceptable or not acceptable. |
| Amazon Reviews | Clustering | Classify the given Amazon review into its appropriate rating category. |
| Banking77 | Clustering | Given an online banking query, find the corresponding intents. |
| Emotion | Clustering | Classify the emotion expressed in the given Twitter message into one of the six emotions: anger, fear, joy, love, sadness, and surprise. |
| MTOP Intent | Clustering | Classify the intent of the given utterance in task-oriented conversation. |
| MTOP Domain | Clustering | Classify the intent domain of the given utterance in task-oriented conversation. |
| Massive Scenario | Clustering | Given a user utterance as query, find the user scenarios. |
| Massive Intent | Clustering | Given a user utterance as query, find the user intents. |
| Tweet Sentiment Extraction | Clustering | Classify the sentiment of a given tweet as either positive, negative, or neutral. |
| Arxiv-Clustering-P2P | Clustering | Identify the main and secondary category of arXiv papers based on the titles and abstracts. |
| Arxiv-Clustering-S2S | Clustering | Identify the main and secondary category of arXiv papers based on the titles. |
| Biorxiv-Clustering-P2P | Clustering | Identify the main category of bioRxiv papers based on the titles and abstracts. |
| Biorxiv-Clustering-S2S | Clustering | Identify the main category of bioRxiv papers based on the titles. |
| Medrxiv-Clustering-P2P | Clustering | Identify the main category of medRxiv papers based on the titles and abstracts. |
| Medrxiv-Clustering-S2S | Clustering | Identify the main category of medRxiv papers based on the titles. |
| Reddit-Clustering-P2P | Clustering | Identify the topic or theme of Reddit posts based on the titles and posts. |
| Reddit-Clustering-S2S | Clustering | Identify the topic or theme of Reddit posts based on the titles. |
| StackExchange-Clustering-P2P | Clustering | Identify the topic or theme of StackExchange posts based on the given paragraphs. |
| StackExchange-Clustering-S2S | Clustering | Identify the topic or theme of StackExchange posts based on the titles. |
| TwentyNewsgroups | Clustering | Identify the topic or theme of the given news articles. |
