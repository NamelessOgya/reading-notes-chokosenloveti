# Multilingual E5 Text Embeddings: A Technical Report

**arXiv:** 2402.05672  
**著者:** Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei（Microsoft Corporation）  
**発表:** 2024年2月

---

## 背景

テキスト埋め込みモデルは情報検索システムや検索拡張言語モデル（RAG）の基盤コンポーネントであるが、既存のほとんどの埋め込みモデルは英語テキストのみで学習されており、多言語対応が限定的であった。本報告書では、英語向け E5 モデルの多言語拡張版として **multilingual E5（mE5）** を提案する。

特に以下の点が動機となっている：
- 多言語情報検索・意味検索ニーズの高まり
- 英語専用モデルとの性能差を縮小する必要性
- インストラクション付き埋め込みが英語単一言語モデルと同等性能を発揮できるかの検証

---

## 手法

### 2段階学習パイプライン

英語 E5 モデルと同じ 2 段階手法を採用する。

#### Stage 1: 弱教師あり対照事前学習

多様な多言語テキストペアを用いた対照学習（Contrastive Pre-training）を実施する。

損失関数は標準的な **InfoNCE 損失**（in-batch negatives のみ）：

$$\mathcal{L} = -\log \frac{\exp(\text{sim}(q, d^+) / \tau)}{\sum_{d \in \mathcal{D}} \exp(\text{sim}(q, d) / \tau)}$$

- バッチサイズ：32,000
- 総ステップ数：30,000（約10億テキストペア）

**Table 1: 対照事前学習のデータ混合**

| データソース | サンプル数 |
|---|---|
| Wikipedia | 150M |
| mC4 | 160M |
| Multilingual CC News | 160M |
| NLLB | 160M |
| Reddit | 160M |
| S2ORC | 50M |
| Stackexchange | 50M |
| xP3 | 80M |
| Misc. SBERT Data | 10M |
| **合計** | **~1B** |

テキストペアの構築方法：
- Wikipedia: (セクションタイトル, セクション本文)
- mC4: (タイトル, ページコンテンツ)
- NLLB: 翻訳ペア
- Reddit: (コメント, 返信)
- S2ORC: (タイトル, アブストラクト) および引用ペア
- Stackexchange: (質問, 回答)

#### Stage 2: 教師あり Fine-tuning

高品質なラベル付きデータセットの組み合わせで学習。in-batch negatives に加え、クロスエンコーダからの **ハード負例マイニング** と **知識蒸留** を導入。  
※ 詳細な手法（損失関数・ハイパーパラメータ等）は英語版 E5 原論文 summary を参照 → [Text Embeddings by Weakly-Supervised Contrastive Pre-training](../Text%20Embeddings%20by%20Weakly-Supervised%20Contrastive%20Pre-training/summary.md)

**Table 2: 教師あり Fine-tuning のデータ混合**

| データセット | サンプル数 |
|---|---|
| MS-MARCO Passage | 500k |
| MS-MARCO Document | 70k |
| NQ, TriviaQA, SQuAD | 220k |
| NLI | 275k |
| ELI5 | 100k |
| NLLB | 100k |
| DuReader Retrieval | 86k |
| Fever | 70k |
| HotpotQA | 70k |
| Quora Duplicate Questions | 15k |
| Mr. TyDi | 50k |
| MIRACL | 40k |
| **合計** | **~1.6M** |

#### インストラクション対応モデル（mE5-large-instruct）

GPT-3.5/4 が生成した合成データ 50万件を追加。計 **150k 種類のインストラクション**を含み **93言語** をカバー。インストラクションはタスクの自然言語説明として埋め込み時に付与される。

### モデル初期化

| モデル | ベースモデル |
|---|---|
| mE5-small | multilingual MiniLM |
| mE5-base | xlm-roberta-base |
| mE5-large | xlm-roberta-large |
| mE5-large-instruct | xlm-roberta-large（新データ混合でfine-tune） |

---

## 結果

### Table 3: English MTEB ベンチマーク（56データセット）

> ベンチマーク詳細 → [MTEB: Massive Text Embedding Benchmark](../MTEB:%20Massive%20Text%20Embedding%20Benchmark/summary.md)

| モデル | MTEB スコア |
|---|---|
| LaBSE | 45.2 |
| Cohere multilingual-v3 | 64.0 |
| BGE large-en-v1.5 | 64.2 |
| mE5-small | 57.9 |
| mE5-base | 59.5 |
| mE5-large | 61.5 |
| **mE5-large-instruct** | **64.4** |

**考察:** mE5-large-instruct は多言語モデルとして初めて Cohere multilingual-v3（64.0）を超え、英語専用の BGE-large-en-v1.5（64.2）も上回る 64.4 を達成。多言語学習が英語性能を大きく損なわないことを示した。

---

### Table 4: 多言語検索 — MIRACLベンチマーク（16言語平均）

> ベンチマーク詳細 → [Making a MIRACL](../Making%20a%20MIRACL:%20Multilingual%20Information%20Retrieval%20Across%20a%20Continuum%20of%20Languages/summary.md)

| モデル | nDCG@10 | R@100 |
|---|---|---|
| BM25 | 39.3 | 78.7 |
| mDPR | 41.5 | 78.8 |
| mE5-small | 60.8 | 92.4 |
| mE5-base | 62.3 | 93.1 |
| **mE5-large** | **66.5** | 94.3 |
| mE5-large-instruct | 65.7 | **94.6** |

**考察:** mE5 モデルは MIRACL 訓練データでファインチューニングされた mDPR に対し、nDCG@10 で +25 pt 以上の大差をつける。mE5-large がランキング精度（nDCG@10）で最高、mE5-large-instruct が再現率（R@100）で最高という傾向が見られた。

---

### Table 5: Bitext マイニング

| モデル | BUCC 2018 (4言語) | Tatoeba (112言語) |
|---|---|---|
| mContriever-msmarco | 93.7 | 37.7 |
| LaBSE | 98.8 | 81.1 |
| mE5-small | 93.2 | 64.2 |
| mE5-base | 98.1 | 68.1 |
| mE5-large | 98.6 | 75.7 |
| **mE5-large-instruct** | **99.0** | **83.8** |

**考察:** Bitext マイニング専用設計の LaBSE（98.8 / 81.1）を mE5-large-instruct（99.0 / 83.8）が超えた。合成データによる言語カバレッジ拡張が低リソース言語を含む Tatoeba（112言語）で特に効果的であった。

---

### Table 6: MIRACL 詳細結果（言語別 nDCG@10 / R@100）

| 言語 | mE5-small (nDCG@10) | mE5-base (nDCG@10) | mE5-large (nDCG@10) | mE5-large-instruct (nDCG@10) | mE5-small (R@100) | mE5-base (R@100) | mE5-large (R@100) | mE5-large-instruct (R@100) |
|---|---|---|---|---|---|---|---|---|
| ar | 71.4 | 71.6 | 76.0 | 76.8 | 96.2 | 95.9 | 97.3 | 97.5 |
| bn | 68.2 | 70.2 | 75.9 | 73.9 | 97.4 | 96.6 | 98.2 | 98.2 |
| en | 48.0 | 51.2 | 52.9 | 51.5 | 85.3 | 86.4 | 87.6 | 88.2 |
| es | 51.2 | 51.5 | 52.9 | 53.7 | 87.6 | 88.6 | 89.1 | 89.3 |
| fa | 53.3 | 57.4 | 59.0 | 59.4 | 90.4 | 91.2 | 92.9 | 92.9 |
| fi | 73.3 | 74.4 | 77.8 | 77.3 | 96.3 | 96.9 | 98.1 | 97.9 |
| fr | 47.6 | 49.7 | 54.5 | 53.7 | 89.5 | 90.0 | 90.6 | 91.7 |
| hi | 55.2 | 58.4 | 62.0 | 60.3 | 91.0 | 92.6 | 93.9 | 94.1 |
| id | 50.7 | 51.1 | 52.9 | 52.1 | 86.2 | 87.4 | 87.9 | 88.4 |
| ja | 63.6 | 64.7 | 70.6 | 69.0 | 95.2 | 96.0 | 97.1 | 96.9 |
| ko | 61.2 | 62.2 | 66.5 | 65.3 | 92.0 | 91.6 | 93.4 | 93.0 |
| ru | 59.1 | 61.5 | 67.4 | 67.9 | 92.2 | 92.7 | 95.5 | 95.4 |
| sw | 68.4 | 71.1 | 74.9 | 72.5 | 94.7 | 95.6 | 96.7 | 97.2 |
| te | 81.3 | 75.2 | 84.6 | 83.4 | 97.6 | 98.0 | 99.2 | 99.0 |
| th | 75.0 | 75.2 | 80.2 | 78.6 | 98.2 | 98.0 | 98.9 | 98.7 |
| zh | 45.9 | 51.5 | 56.0 | 56.2 | 87.9 | 92.1 | 93.3 | 94.9 |
| **Avg** | **60.8** | **62.3** | **66.5** | **65.7** | **92.4** | **93.1** | **94.3** | **94.6** |

**考察:** 言語別では te（テルグ語）・th（タイ語）・fi（フィンランド語）など非ラテン文字言語で高スコアを記録。日本語（ja）は nDCG@10 で mE5-large が 70.6 と良好な性能を示した。英語（en）の nDCG@10 が相対的に低い（52.9）のは、英語特化モデルと比べ汎化の代償とも解釈できる。

---

### Table 7: MTEB 全56データセット詳細結果

| データセット | mE5-small | mE5-base | mE5-large | mE5-large-instruct |
|---|---|---|---|---|
| BIOSSES | 82.3 | 85.1 | 82.5 | 87.0 |
| SICK-R | 77.5 | 78.5 | 80.2 | 81.7 |
| STS12 | 76.6 | 76.7 | 80.0 | 82.6 |
| STS13 | 77.0 | 78.0 | 81.5 | 87.2 |
| STS14 | 75.5 | 76.6 | 77.7 | 85.0 |
| STS15 | 87.1 | 88.2 | 89.3 | 91.0 |
| STS16 | 83.6 | 84.3 | 85.8 | 87.3 |
| STS17 | 86.4 | 87.8 | 88.1 | 90.0 |
| STS22 | 60.9 | 61.8 | 63.1 | 67.6 |
| STSBenchmark | 84.0 | 85.6 | 87.3 | 88.4 |
| SummEval | 30.0 | 30.1 | 29.7 | 30.4 |
| SprintDuplicateQuestions | 92.2 | 93.0 | 93.1 | 91.2 |
| TwitterSemEval2015 | 70.8 | 72.2 | 75.3 | 80.3 |
| TwitterURLCorpus | 84.8 | 85.5 | 85.8 | 87.1 |
| AmazonCounterfactualClassification | 73.8 | 79.0 | 79.1 | 76.2 |
| AmazonPolarityClassification | 88.7 | 90.6 | 93.5 | 96.3 |
| AmazonReviewsClassification | 44.7 | 44.5 | 47.6 | 56.7 |
| Banking77Classification | 79.4 | 82.7 | 84.7 | 85.7 |
| EmotionClassification | 42.5 | 45.2 | 46.5 | 51.5 |
| ImdbClassification | 80.8 | 85.5 | 90.2 | 94.6 |
| MassiveIntentClassification | 70.3 | 72.1 | 73.8 | 77.1 |
| MassiveScenarioClassification | 74.5 | 77.1 | 77.5 | 80.5 |
| MTOPDomainClassification | 91.1 | 93.1 | 93.7 | 93.9 |
| MTOPIntentClassification | 71.1 | 75.3 | 77.9 | 82.5 |
| ToxicConversationsClassification | 69.4 | 69.8 | 71.3 | 71.1 |
| TweetSentimentExtractionClassification | 62.6 | 61.3 | 62.0 | 64.6 |
| AskUbuntuDupQuestions | 57.9 | 58.2 | 60.3 | 63.9 |
| MindSmallReranking | 30.3 | 31.0 | 31.4 | 33.1 |
| SciDocsRR | 78.1 | 80.7 | 82.0 | 85.9 |
| StackOverflowDupQuestions | 49.2 | 49.4 | 49.7 | 51.5 |
| ArxivClusteringP2P | 39.2 | 40.3 | 44.3 | 46.4 |
| ArxivClusteringS2S | 30.8 | 35.4 | 38.4 | 40.5 |
| BiorxivClusteringP2P | 35.8 | 35.0 | 35.3 | 40.9 |
| BiorxivClusteringS2S | 27.1 | 29.5 | 33.5 | 36.3 |
| MedrxivClusteringP2P | 30.9 | 28.9 | 31.5 | 36.9 |
| MedrxivClusteringS2S | 27.3 | 28.4 | 29.7 | 35.5 |
| RedditClustering | 39.1 | 42.4 | 46.5 | 56.6 |
| RedditClusteringP2P | 59.0 | 55.2 | 63.2 | 64.3 |
| StackExchangeClustering | 53.5 | 55.3 | 57.5 | 66.8 |
| StackExchangeClusteringP2P | 32.1 | 30.5 | 32.7 | 42.5 |
| TwentyNewsgroupsClustering | 33.2 | 36.0 | 38.9 | 51.3 |
| ArguAna | 39.1 | 44.2 | 54.4 | 58.4 |
| ClimateFEVER | 22.6 | 23.9 | 25.7 | 29.9 |
| CQADupstackAndroidRetrieval | 36.1 | 38.5 | 39.7 | 42.7 |
| DBPedia | 37.8 | 40.4 | 41.3 | 38.4 |
| FEVER | 75.3 | 79.4 | 82.8 | 78.0 |
| FiQA2018 | 33.3 | 38.2 | 43.8 | 47.7 |
| HotpotQA | 65.1 | 68.6 | 71.2 | 69.3 |
| MSMARCO | 41.0 | 42.3 | 43.7 | 40.4 |
| NFCorpus | 31.0 | 32.5 | 34.0 | 35.5 |
| NQ | 56.3 | 60.0 | 64.1 | 57.8 |
| QuoraRetrieval | 86.9 | 87.7 | 88.2 | 89.2 |
| SCIDOCS | 13.9 | 17.2 | 17.5 | 18.7 |
| SciFact | 67.7 | 69.3 | 70.4 | 71.8 |
| Touche2020 | 21.2 | 21.4 | 23.4 | 27.2 |
| TRECCOVID | 72.6 | 69.8 | 71.3 | 82.0 |
| **Average** | **57.9** | **59.4** | **61.5** | **64.4** |

**考察:** インストラクション付き mE5-large-instruct は STS 系タスク（意味的類似性）・クラスタリング・分類の全カテゴリで顕著な改善を見せた。特に RedditClustering（+10.1 pt）・TRECCOVID（+10.7 pt）・TwentyNewsgroupsClustering（+12.4 pt）での改善が大きく、インストラクションがドメイン固有のタスクで特に有効であることを示している。一方 DBPedia や FEVER では mE5-large が mE5-large-instruct を上回るケースもあり、インストラクションが逆効果になる場合があることも示唆された。
