# MTEB: Massive Text Embedding Benchmark

**arXiv:** 2210.07316  
**著者:** Niklas Muennighoff, Nouamane Tazi, Loïc Magne, Nils Reimers  
**発表:** EACL 2023（初版 2022年10月）

---

## 背景

テキスト埋め込みモデルの評価は、STS（意味的類似性）など限られたタスクに偏っており、同じモデルが検索・クラスタリング・分類などの他タスクでもうまく機能するかは不明だった。既存のベンチマーク（SentEval, BEIR 等）はそれぞれ単一タスクに特化しており、埋め込みモデルの**汎用性を総合的に評価する枠組みが存在しなかった**。

本論文では、テキスト埋め込みモデルの汎用評価基盤として **MTEB（Massive Text Embedding Benchmark）** を提案する。

---

## MTEBの設計

### 設計方針（Desiderata）

- **多様性（Diversity）**: 8タスク・58データセット・112言語をカバー
- **シンプルさ（Simplicity）**: テキストリストを受け取り埋め込みベクトルを返すAPIを実装するだけで評価可能（10行以下のコード）
- **拡張性（Extensibility）**: コミュニティからの新データセット・タスク追加をプルリクで受け付け
- **再現性（Reproducibility）**: バージョン管理によりすべての実験結果を JSON で公開

### 8つのタスクカテゴリと評価指標

| タスク | 説明 | 主評価指標 |
|---|---|---|
| **Bitext Mining** | 2言語間で対応文を検索 | F1 |
| **Classification** | 埋め込みを固定してロジスティック回帰で分類 | Accuracy |
| **Clustering** | mini-batch k-means でクラスタリング | V-measure |
| **Pair Classification** | テキストペアの類似・重複ラベル予測 | Average Precision（cosine） |
| **Reranking** | クエリに対して関連文書を再ランキング | MAP |
| **Retrieval** | コーパスから関連文書を検索（BEIR データセットを再利用） | nDCG@10 |
| **STS** | 文ペアの意味的類似度スコアリング | Spearman 相関（cosine） |
| **Summarization** | 機械生成要約を人手要約との類似度でスコアリング | Spearman 相関（cosine） |

### テキスト長の多様性

- **S2S（Sentence to Sentence）**: 文と文を比較（例：全 STS タスク）
- **P2P（Paragraph to Paragraph）**: 段落間の比較（例：ArxivClustering の P2P 版は要約+タイトル）
- **S2P（Sentence to Paragraph）**: 短いクエリと長い文書の比較（検索タスクに多い）

---

## 結果

### 主要な発見

**「全タスクで最強のモデルは存在しない」**

33モデルを評価した結果、単一の埋め込み手法がすべてのタスクで支配的になることはなかった。例：
- **SimCSE**: STS では強力だが、クラスタリング・検索タスクでは低性能
- **GTR / Sentence-T5**: パラメータ数が最大（4.8B）だが E5-base（110M）に匹敵されるケースがある
- **LaBSE**: Bitext Mining に特化した設計で多言語タスクでは強いが、英語単一タスクは弱い

### 評価モデルのカテゴリ

| カテゴリ | 例 |
|---|---|
| 自己教師あり（Transformer） | BERT, SimCSE-Unsup |
| 教師あり（Encoder） | SBERT, LaBSE, GTR, Sentence-T5, E5, BGE |
| 教師あり（Decoder） | SGPT（GPT-NeoX, GPT-J, BLOOM ベース） |
| 非 Transformer | GloVe, LASER（LSTM ベース） |

---

## 限界

- **長文書データセットの不足**: 現在の MTEB は主に短文・段落レベル
- **タスク不均衡**: 検索タスクが多く全体スコアに偏りが出やすい
- **多言語性の不足**: 58 データセット中、多言語は 10 のみ（初版時点）
- **追加モダリティ非対応**: 画像・音声などは含まない

---

## 貢献と位置づけ

**貢献:**
- テキスト埋め込みの多タスク総合評価フレームワークの提案
- 33モデルの包括的ベンチマーク（初版時点で最大規模）
- 公開リーダーボード（HuggingFace Hub）によりコミュニティの標準指標に

**位置づけ:**  
mE5・E5・Qwen3 Embedding など多くの埋め込みモデル論文が「英語評価」の主指標として MTEB を使用している。Table 3（mE5 summary）の 56 データセットはこの MTEB の英語サブセット。
