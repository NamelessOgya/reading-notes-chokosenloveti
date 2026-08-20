# Ruri: Japanese General Text Embeddings

**arXiv:** 2409.07737  
**著者:** Hayato Tsukagoshi, Ryohei Sasano（名古屋大学大学院情報学研究科）  
**発表:** 2024年9月

---

## 背景

テキスト埋め込みモデルは RAG（検索拡張生成）や類似文書検索の基盤として広く利用されているが、英語・多言語モデルの開発が主流であり、日本語専用の汎用埋め込みモデルの開発は遅れていた。その主な原因として以下が挙げられる：

1. **日本語学習データセットの不足** — 英語・多言語モデルに比べ、日本語の検索・QAデータセットは極めて少ない
2. **ライセンス問題** — 商用利用可能な日本語データセットが限られている
3. **専門知識の欠如** — 日本語に特化した埋め込みモデル開発の知見が蓄積されていなかった

本報告書では、日本語に特化した汎用テキスト埋め込みモデルシリーズ **Ruri** の開発プロセスを詳述する。LLMを用いた合成データセット生成、リランカーの構築、知識蒸留を組み合わせることで、既存の多言語・日本語モデルを大幅に上回る性能を達成した。

---

## 手法

### 全体パイプライン

1. **対照事前学習（Contrastive Pre-training）** → Ruri-PT（事前学習済みモデル）を構築
2. **リランカー構築** → 知識蒸留・データフィルタリングに使用
3. **教師あり Fine-tuning** → 最終的な Ruri 埋め込みモデルを構築

---

### Stage 1: 対照事前学習

#### 使用データセット

LLMが生成した合成データ（AutoWikiQA, AutoWikiNLI）を含む多様な日本語データで対照事前学習を実施。

**Table 1: 対照事前学習データセット一覧**

| ソース | Anchor | Positive | Negative | データサイズ |
|---|---|---|---|---|
| Wikipedia (1) | title + section title | 1-paragraph | random 1-paragraph | 19,361,464 |
| Wikipedia (3) | title + section title | 3-paragraphs | random 3-paragraphs | 10,010,462 |
| Wikipedia (long) | title / abst. | abst. / article body | random abst. / article body | 7,889,486 |
| Wiktionary | title | article body | random article body | 697,405 |
| WikiBooks | title + section title | 1-paragraph | random 1-paragraph | 314,207 |
| MQA | title | article body | BM25 mined article body | 25,165,824 |
| CC News (long) | title | article body | BM25 mined article body | 6,248,336 |
| CC News (short) | random sentence | sentence in the same article | sentence in other articles | 2,795,632 |
| AutoWikiQA (MX) | question | passage | BM25 mined passage | 11,563,562 |
| AutoWikiQA (Nemo) | question | passage | BM25 mined passage | 495,062 |
| JRC | title + section title | section body | BM25 mined section body | 131,072 |
| Wiki Atomic Edits | sentence | edited sentence | random sentence | 3,679,939 |
| AutoWikiNLI | premise | hypothesis (entailment) | hypothesis (contradiction) | 203,147 |
| JSNLI | premise | hypothesis (entailment) | hypothesis (contradiction) | 180,146 |
| **Total** | | | | **88,735,744** |

**Table 2: 事前学習モデル一覧**

| モデル | パラメータ数 | GPU | ベースLM |
|---|---|---|---|
| Ruri-PT-small | 68M | A6000×4 | line-corporation/line-distilbert-base-japanese |
| Ruri-PT-base | 111M | A100×4 | tohoku-nlp/bert-base-japanese-v3 |
| Ruri-PT-large | 337M | A100×4 | tohoku-nlp/bert-large-japanese-v2 |

#### 合成データセット

- **AutoWikiQA**: Swallow-MX（Mixtral-8x7Bの日本語継続事前学習版）と Nemotron-4 340B を使用して Wikipedia のランダム段落からクエリと回答を生成。250M以上のクエリ・パッセージペアを含む
- **AutoWikiNLI**: Nemotron-4 340B を用いてWikipedia文から前提・含意・矛盾文の三つ組を生成。矛盾文を先に生成してから含意文を生成する逆順生成で品質を向上。Nemotron Reward Modelで下位20%を除去

#### 学習の工夫

##### ① 改良対照損失（GTE 方式）

通常の対照学習はクエリと正例パッセージの類似度のみを最大化するが、Ruri では **GTE（Li et al. 2023）の改良対照損失**を採用。

**通常の InfoNCE 損失（クエリ → パッセージ方向のみ）：**

$$\mathcal{L} = -\log \frac{\exp(\text{sim}(q, p^+) / \tau)}{\sum_{p \in \text{batch}} \exp(\text{sim}(q, p) / \tau)}$$

**改良版（GTE方式）：4方向の類似度を考慮：**

| ペア | 目的 |
|---|---|
| クエリ → パッセージ | 正例の類似度を高める（通常の対照損失） |
| クエリ → クエリ | 同バッチ内の他クエリとの類似度を下げる |
| パッセージ → クエリ | 上と逆方向 |
| パッセージ → パッセージ | 同バッチ内の他パッセージとの類似度を下げる |

バッチ内の全ての非正例ペアについて類似度を下げることを目標とし、より厳密な表現学習を実現する。

---

##### ② タスク均質バッチ（Task-homogeneous Batching）

> *"only triplets from the same dataset were included in a single batch to prevent shortcut learning"*

同一バッチには**必ず同一データセットのサンプルのみ**を含める。

**防止する問題 1：ショートカット学習**  
異なるデータセットを混在させると、モデルが「どのデータセット由来か」という特徴でスコアリングしてしまい、本来の意味的類似性を学習しなくなる。

**防止する問題 2：偽陰性（False Negatives）**  
同バッチに同一文書の重複が含まれると、実際には正例なのにネガティブとして扱われてしまう。各バッチ内で**重複文を事前に除去**することで対処。

**副次的メリット：**  
同一データセットのサンプルは系列長が近いため、**パディングが減り学習時間が短縮**される。

---

##### ③ ハード負例マイニング（BM25 使用）

事前学習フェーズでも BM25 によるハード負例マイニングを実施（Wang et al. 2022 の知見に基づく）。

- 全文書コーパスから転置インデックスを構築
- **データセットごとに独立したインデックスを作成**してインデックス構築・検索コストを削減
- 論文注記：E5 の CCPairs（1.3B ペア規模）では困難だが、Ruri の規模（88M ペア）では実用的に適用可能

---

##### ④ その他の実装上の工夫

| 工夫 | 詳細 |
|---|---|
| **プレフィックス** | クエリ→「クエリ: 」、パッセージ→「文章: 」（英語の "query:" / "passage:" を日本語訳） |
| **バッチサイズ** | 8,192（GTE の知見：8,192 超では改善がほぼない） |
| **位置埋め込みの固定** | E5 と同様にポジショナル埋め込みを固定（SimCSE とは異なる） |
| **プーラー層なし** | SimLM・E5 と同様にプーラー層を使用しない |
| **データ拡張** | 正例文書の文順シャッフルを行い、データ量を増加 |
| **文分割** | 日本語形態素解析器 Konoha を使用 |
| **エポック数** | 1 エポック |



---

### Stage 2: リランカー構築

クロスエンコーダ型リランカーを2段階で学習。知識蒸留とデータフィルタリングに使用する。

**Table 3: リランカー 第1段階データセット**

| ソース | データサイズ |
|---|---|
| JSQuAD | 212,352 |
| AutoWikiQA (Nemo) | 190,743 |
| JaQuAD | 108,068 |
| Quiz No Mori | 36,120 |
| Quiz Works | 29,112 |
| JQaRA | 16,260 |
| MIRACL | 13,968 |
| Mr. TyDi | 7,394 |
| MKQA | 6,636 |
| **Total** | **620,653** |

**Table 4: リランカー 第2段階データセット**

| ソース | データサイズ |
|---|---|
| Quiz No Mori | 18,060 |
| Quiz Works | 14,556 |
| JQaRA | 8,130 |
| MIRACL | 6,984 |
| MR. TyDi | 3,697 |
| **Total** | **51,427** |

- ハード負例: BM25 と mE5-large の Reciprocal Rank Fusion（RRF）で 30〜100位を選択
- 損失: クロスエントロピー損失（正例スコアを63個の負例より高くする）
- 第1段階: シーケンス長256、第2段階: 512

---

### Stage 3: 教師あり Fine-tuning

**Table 5: 教師あり Fine-tuning データセット**

| ソース | 知識蒸留あり | データサイズ |
|---|---|---|
| Quiz No Mori | ✓ | 31,232 |
| Quiz Works | ✓ | 26,624 |
| JQaRA | ✓ | 13,824 |
| MIRACL | ✓ | 12,800 |
| Mr. TyDi | ✓ | 7,168 |
| NU-SNLI | | 109,568 |
| NU-MNLI | | 77,824 |
| JaNLI | | 13,824 |
| **Total** | | **292,864** |

- **知識蒸留**: Ruri-Reranker-Large からスコアを取得。クロスエンコーダとデュアルエンコーダのスコアを min-max 正規化して蒸留
- 関連性スコア < 0.8 のノイズサンプルを除去
- 検索・QAデータに知識蒸留損失、NLIデータに対照学習損失を分離適用

**Table 6: Fine-tuning 済みモデル一覧**

| モデル | #Params | 埋め込み次元 | 層数 | プーリング | コンテキスト長 | 語彙数 | JMTEB Avg. |
|---|---|---|---|---|---|---|---|
| Ruri-small | 68M | 768 | 6 | Mean | 512 | 32,768 | 71.53 |
| Ruri-base | 111M | 768 | 12 | Mean | 512 | 32,768 | 71.91 |
| Ruri-large | 337M | 1024 | 24 | Mean | 512 | 32,768 | 73.31 |

#### ハイパーパラメータ詳細

**Table 7: 埋め込みモデルのハイパーパラメータ**

| パラメータ | PT-Small | PT-Base | PT-Large | Ruri-Small | Ruri-Base | Ruri-Large |
|---|---|---|---|---|---|---|
| learning rate | 1×10⁻⁴ | 5×10⁻⁵ | 3×10⁻⁵ | 1×10⁻⁵ | 5×10⁻⁶ | 3×10⁻⁶ |
| max length | 256 | 256 | 192 | 512 | 512 | 512 |
| warmup ratio | 10% | 10% | 10% | 10% | 10% | 10% |
| batch size | 8192 | 8192 | 8192 | 512 | 512 | 512 |
| epochs | 1 | 1 | 1 | 1 | 1 | 1 |
| τ | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |
| weight decay | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |
| hard negatives | 1 | 1 | 1 | 15 | 15 | 15 |
| task-homogeneous | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| shuffle positive | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| knowledge distillation | | | | ✓ | ✓ | ✓ |

---

## 結果

### Table 8: リランカー性能比較

| モデル | #Param (w/o Emb) | JQaRA (nDCG@10) | JaCWIR (MAP@10) | MIRACL (Recall@30) |
|---|---|---|---|---|
| hotchpotch/japanese-reranker-cross-encoder-xsmall-v1 | 107M (11M) | 61.4 | 93.8 | 90.6 |
| hotchpotch/japanese-reranker-cross-encoder-small-v1 | 118M (21M) | 62.5 | 93.9 | 92.2 |
| hotchpotch/japanese-reranker-cross-encoder-base-v1 | 111M (86M) | 67.1 | 93.4 | 93.3 |
| hotchpotch/japanese-reranker-cross-encoder-large-v1 | 337M (303M) | 71.0 | 93.6 | 91.5 |
| hotchpotch/japanese-bge-reranker-v2-m3-v1 | 568M (303M) | 69.2 | 93.7 | 94.7 |
| BAAI/bge-reranker-v2-m3 | 568M (303M) | 67.3 | 93.4 | 94.9 |
| **Ruri-Reranker-small** | 68M (43M) | 64.5 | 92.6 | 92.3 |
| **Ruri-Reranker-base** | 111M (86M) | 74.3 | 93.5 | 95.6 |
| **Ruri-Reranker-large** | 337M (303M) | **77.1** | **94.1** | **96.1** |

**考察:** Ruri-Reranker-large は既存全てのリランカーを上回り、特に JQaRA（RAG 向け QA 検索タスク）で圧倒的な性能（77.1 vs 71.0）を示した。これは多様な QA データセットによる訓練が奏効したと考えられる。

---

### Table 9: リランカー アブレーション（2段階学習）

| モデル | Stage | JQaRA | JaCWIR | MIRACL |
|---|---|---|---|---|
| Ruri-PT-small | 1 only | 63.9 | 92.5 | 91.2 |
| Ruri-PT-small | 2 only | 60.3 | 89.9 | 89.3 |
| **Ruri-PT-small** | **1→2** | **64.5** | **92.6** | **92.3** |
| Ruri-PT-base | 1 only | 72.9 | 92.4 | 94.2 |
| Ruri-PT-base | 2 only | 68.0 | 92.9 | 93.7 |
| **Ruri-PT-base** | **1→2** | **74.3** | **93.5** | **95.6** |
| Ruri-PT-large | 1 only | 75.8 | 93.4 | 95.4 |
| Ruri-PT-large | 2 only | 70.5 | 90.8 | 93.2 |
| **Ruri-PT-large** | **1→2** | **77.1** | **94.1** | **96.1** |

**考察:** 2段階学習（1→2）が全サイズで最高性能を達成。特に第2段階のみでは第1段階のみより低くなることが多く、粗いデータで広く学んでから精緻なデータで調整する順序が重要であることがわかる。

---

### Table 10: リランカー アブレーション（対照事前学習の効果）

| モデル | Phase | JQaRA | JaCWIR | MIRACL |
|---|---|---|---|---|
| BERT-small | stage1 | 63.7 | 89.4 | 90.4 |
| BERT-small | stage2 | 64.3 | 91.4 | 91.6 |
| **Ruri-PT-small** | stage1 | 63.9 | 92.5 | 91.2 |
| **Ruri-PT-small** | stage2 | **64.5** | **92.6** | **92.3** |
| BERT-base | stage1 | 71.8 | 89.3 | 93.9 |
| BERT-base | stage2 | 73.1 | 91.6 | 95.1 |
| **Ruri-PT-base** | stage1 | 72.9 | 92.4 | 94.2 |
| **Ruri-PT-base** | stage2 | **74.3** | **93.5** | **95.6** |
| BERT-large | stage1 | 76.1 | 92.2 | 95.2 |
| BERT-large | stage2 | **77.3** | 93.5 | 96.0 |
| **Ruri-PT-large** | stage1 | 75.8 | 93.4 | 95.4 |
| **Ruri-PT-large** | stage2 | 77.1 | **94.1** | **96.1** |

**考察:** 対照事前学習済みモデル（Ruri-PT）はほぼ全てのサイズ・フェーズで通常 BERT を上回った。対照学習とリランキングは目的関数が異なるが、対照事前学習がテキストの重要情報にフォーカスする能力を培うため、リランキング性能向上に繋がると考えられる。

---

### Table 11: JMTEB 全体評価結果

| モデル | #Param | Retrieval | STS | Class. | Reranking | Clustering | Pair. | Avg. |
|---|---|---|---|---|---|---|---|---|
| cl-nagoya/sup-simcse-ja-base | 111M | 49.64 | 82.05 | 73.47 | 91.83 | 51.79 | 62.57 | 63.36 |
| cl-nagoya/sup-simcse-ja-large | 337M | 37.62 | 83.18 | 73.73 | 91.48 | 50.56 | 62.51 | 58.88 |
| cl-nagoya/unsup-simcse-ja-base | 111M | 40.23 | 78.72 | 73.07 | 91.16 | 44.77 | 62.44 | 58.39 |
| cl-nagoya/unsup-simcse-ja-large | 337M | 40.53 | 80.56 | 74.66 | 90.95 | 48.41 | 62.49 | 59.58 |
| pkshatech/GLuCoSE-base-ja | 133M | 59.02 | 78.71 | 76.82 | 91.90 | 49.78 | 66.39 | 67.29 |
| sentence-transformers/LaBSE | 472M | 40.12 | 76.56 | 72.66 | 91.63 | 44.88 | 62.33 | 58.01 |
| intfloat/multilingual-e5-small | 118M | 67.27 | 80.07 | 67.62 | 93.03 | 46.91 | 62.19 | 67.71 |
| intfloat/multilingual-e5-base | 278M | 68.21 | 79.84 | 69.30 | 92.85 | 48.26 | 62.26 | 68.61 |
| intfloat/multilingual-e5-large | 560M | 70.98 | 79.70 | 72.89 | 92.96 | 51.24 | 62.15 | 70.90 |
| OpenAI/text-embedding-ada-002 | - | 64.38 | 79.02 | 69.75 | 93.04 | 48.30 | 62.40 | 67.21 |
| OpenAI/text-embedding-3-small | - | 66.39 | 79.46 | 73.06 | 92.92 | 51.06 | 62.27 | 69.18 |
| OpenAI/text-embedding-3-large | - | 74.48 | 82.52 | 77.58 | 93.58 | 53.32 | 62.35 | 74.05 |
| **Ruri-small** | 68M | 69.41 | 82.79 | 76.22 | 93.00 | 51.19 | 62.11 | 71.53 |
| **Ruri-base** | 111M | 69.82 | 82.87 | 75.58 | 92.91 | 54.16 | 62.38 | 71.91 |
| **Ruri-large** | 337M | 73.02 | 83.13 | 77.43 | 92.99 | 51.82 | 62.29 | 73.31 |

**考察:** Ruri-base（111M）は mE5-large（560M）を Avg. で上回った（71.91 vs 70.90）。OpenAI のプロプライエタリモデルとも遜色ない性能を示している。特に Retrieval と STS で既存日本語モデルを大きく上回る。

---

### Table 12: 検索タスク詳細評価（nDCG@10）

| モデル | JaGovFAQs | JAQKET | Mr. TyDi | NLP Journal Abst.--Intro. | NLP Journal Title--Abst. | NLP Journal Title--Intro. | Avg. |
|---|---|---|---|---|---|---|---|
| pkshatech/GLuCoSE-base-ja | 63.88 | 39.82 | 30.28 | 78.26 | 82.06 | 59.82 | 59.02 |
| intfloat/multilingual-e5-small | 64.11 | 49.97 | 36.05 | 85.21 | 95.26 | 72.99 | 67.27 |
| intfloat/multilingual-e5-base | 65.34 | 50.67 | 38.38 | 87.10 | 94.73 | 73.05 | 68.21 |
| intfloat/multilingual-e5-large | 70.30 | 58.78 | **43.63** | 86.00 | 94.70 | 72.48 | 70.98 |
| OpenAI/text-embedding-ada-002 | 61.02 | 42.56 | 14.51 | 94.99 | 91.23 | 81.98 | 64.38 |
| OpenAI/text-embedding-3-small | 64.02 | 33.94 | 20.03 | 98.47 | 91.70 | 90.17 | 66.39 |
| OpenAI/text-embedding-3-large | 72.41 | 48.21 | 34.88 | **99.33** | **96.55** | **95.47** | 74.48 |
| **Ruri-small** | 73.65 | 48.44 | 33.43 | 87.69 | 97.17 | 76.09 | 69.41 |
| **Ruri-base** | 74.56 | 50.12 | 35.45 | 86.89 | **96.57** | 75.31 | 69.82 |
| **Ruri-large** | **76.68** | **61.74** | 38.03 | 87.12 | **96.58** | 77.97 | 73.02 |

**考察:** Ruri-large は JaGovFAQs（FAQ 検索）・JAQKET（QA 検索）で最高性能を達成。一方、NLP Journal タスク（LaTeX 論文関連）では OpenAI モデルが圧倒的に優れており、プロプライエタリモデルが大規模な LaTeX 論文データで事前学習されている可能性を示唆している。Mr. TyDi では mE5-large（43.63）が依然トップであり、多言語データから日本語を学ぶことの優位性が一部残っている。

---

### Table 13: アブレーション — 合成データセットの効果

| モデル | Retrieval | STS | Class. | Reranking | Clustering | Pair. | Avg. |
|---|---|---|---|---|---|---|---|
| **Ruri-PT-large** | **71.48** | 82.06 | 76.12 | **92.75** | **53.41** | 62.27 | **72.46** |
| Ruri-PT-large w/o retrieval | 68.08 | **82.32** | **76.42** | 92.66 | 51.98 | 62.29 | 71.11 |

**考察:** 合成検索データセット（AutoWikiQA）を除去すると Retrieval が −3.4 pt 低下し、平均でも −1.35 pt の差が生じた。著者が主張する「合成データが1点以上の差をもたらす」という効果が確認された。

---

### Table 14: アブレーション — 対照事前学習の効果

| モデル | Retrieval | STS | Class. | Reranking | Clustering | Pair. | Avg. |
|---|---|---|---|---|---|---|---|
| Ruri-PT-small | 67.39 | 81.41 | 75.41 | 92.98 | 51.13 | 62.44 | 70.41 |
| Ruri-small w/o pre-training | 56.62 | 82.45 | 77.30 | 92.01 | 47.77 | 62.42 | 66.49 |
| **Ruri-small** | 69.41 | 82.79 | 76.22 | 93.00 | 51.19 | 62.11 | **71.53** |
| Ruri-PT-base | 68.18 | 81.81 | 74.56 | 92.82 | 53.35 | 62.33 | 70.80 |
| Ruri-base w/o pre-training | 52.99 | 81.95 | 76.19 | 91.60 | 51.85 | 62.20 | 65.25 |
| **Ruri-base** | 69.82 | 82.87 | 75.58 | 92.91 | 54.16 | 62.38 | **71.91** |
| Ruri-PT-large | 71.48 | 82.06 | 76.12 | 92.75 | 53.41 | 62.27 | 72.46 |
| Ruri-large w/o pre-training | 57.84 | 83.66 | 76.50 | 91.51 | 49.56 | 62.35 | 67.09 |
| **Ruri-large** | 73.02 | 83.13 | 77.43 | 92.99 | 51.82 | 62.29 | **73.31** |

**考察:** 対照事前学習なし（w/o pre-training）では Retrieval が large で −15.18 pt（57.84→73.02）もの大幅な低下が見られ、事前学習の効果が際立っている。STS・分類タスクへの影響は相対的に小さく、検索性能への寄与が特に大きいことがわかる。Ruri-PT（事前学習のみ）単体でも既存多言語モデルと同等以上の性能を示し、事前学習だけで効果的な埋め込み表現が学習されていることが確認された。
