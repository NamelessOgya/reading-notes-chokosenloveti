# EncodeRec: An Embedding Backbone for Recommendation Systems

## 背景
近年のレコメンドシステムでは、事前学習済み言語モデル（PLM）の埋め込み（Embedding）を活用する手法が主流になりつつある。しかし、PLMの埋め込みには主に2つの限界がある。
1. **埋め込み空間の構造化不足**: PLMは言語モデリングとして最適化されており、検索やランキングなどのタスクに不可欠な「明確に分離された弁別性の高い埋め込み空間（距離学習など）」を形成するように明示的に最適化されていない。
2. **表現の汎用性**: PLMの表現は汎用的すぎるため、レコメンドの質を左右する「同じドメイン（カテゴリ）内での細かな属性の違い（価格帯、ターゲット年齢層、難易度など）」などのドメイン特化の微細なセマンティクスを捉えきれない。

既存研究（例：BLaIR）では、ユーザーのレビューを用いてメタデータとの関連を学習することでこの問題に対処しようとしたが、レビューに含まれる主観的なノイズが汎化性能を低下させる可能性があった。また、最新の汎用埋め込みモデル（EmbeddingGemmaなど）に対しても、レコメンドに特化したバックボーンが依然として優位性を持つのかが課題となっていた。

## 手法
本論文では、レコメンド目的に合致したアイテム表現を生成するための埋め込みバックボーン「**EncodeRec**」を提案している。

- **メタデータ主導の対照学習（Contrastive Learning）**:
  ユーザーのレビュー（主観的ノイズ）に依存するのではなく、アイテムのタイトルを高精度な「セマンティックアンカー（クエリ）」とし、それと「アイテムの説明文＋属性情報（ドキュメント）」とを関連付ける客観的な対照学習を採用している。これにより、アイテムの事実に基づいた基本的な同一性を学習する。
- **共有エンコーダの利用**:
  タイトル `$x_{i}^{(q)}$` と説明文/属性 `$x_{i}^{(d)}$` の両方を、 パラメータを共有する単一のエンコーダ `$\mathrm{Emb}(\cdot)$` で処理し、同じ表現空間に配置する。

$$ h_{i}^{(q)} = \mathrm{Emb}(x_{i}^{(q)}), \qquad h_{i}^{(d)} = \mathrm{Emb}(x_{i}^{(d)}) $$

- **InfoNCEロスによる最適化**:
  バッチ内の同一アイテムのタイトルと説明文を正例とし、他のアイテムを負例として学習する（In-batch Negative Sampling）。これにより同じアイテムのメタデータビューを近づけ、無関係なアイテムを引き離す構造化された表現空間を獲得する。学習中、レコメンドモデルの学習時には言語モデルのパラメータは凍結されるため、計算効率も高い。

$$ \mathcal{L} = - \frac{1}{N} \sum_{i=1}^{N} \log \frac{\exp\!\left( \mathrm{sim}(h_{i}^{(q)}, h_{i}^{(d)}) / \tau \right)}{\sum_{j=1}^{N} \exp\!\left( \mathrm{sim}(h_{i}^{(q)}, h_{j}^{(d)}) / \tau \right)} $$

## 結果
![](./images/pic.png)

EncodeRecは、シーケンシャルレコメンド（例：UniSRec）や生成型レコメンド（例：TIGER）のための「ドロップイン（そのまま置き換え可能）」なバックボーンとして評価された。

| Model | Recall@10 | NDCG@10 |
| :--- | :--- | :--- |
| BERT-Base | 0.09 | 0.07 |
| BLaIR-Large | 0.12 | 0.09 |
| all-MiniLM-L6-v2 | 0.57 | 0.44 |
| EmbeddingGemma | 0.83 | 0.72 |

*Table 1: Retrieval results for item descriptions retrieved from titles on 50K items in the Amazon Beauty dataset.*

Table 1より、既存のBERTやBLaIRといったモデルと比較して、事前学習済みの汎用テキスト埋め込みモデル（EmbeddingGemmaなど）が検索において高い性能を示していることがわかる。本研究では、これらの強力な汎用モデルをベースにEncodeRecの学習レシピ（対照学習）を適用して評価した。

| UniSRec Model | Video Games (Recall@10) | Video Games (NDCG@10) | Beauty (Recall@10) | Beauty (NDCG@10) | Baby Products (Recall@10) | Baby Products (NDCG@10) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BERT | 0.0214 | 0.0116 | 0.0157 | 0.0098 | 0.0122 | 0.0063 |
| Blair-Base | <u>0.0241</u> | 0.0128 | 0.0245 | 0.0123 | 0.0146 | 0.0131 |
| Blair-Large | 0.0247 | <u>0.0134</u> | 0.0239 | 0.0119 | <u>0.0148</u> | <u>0.0075</u> |
| MiniLM-L6-v2 | 0.0231 | 0.0123 | 0.0218 | 0.0130 | 0.0130 | 0.0066 |
| EncodeRec-22M | 0.0232 | 0.0126 | <u>0.0333</u> | <u>0.0182</u> | 0.0141 | 0.0072 |
| EmbeddingGemma | 0.0244 | 0.0129 | 0.0308 | 0.0165 | 0.0147 | 0.0075 |
| EncodeRec-300M | **0.0263\*** | **0.0142\*** | **0.0387\*** | **0.0206\*** | **0.0162\*** | **0.0084\*** |

*Table 2: UniSRec results across datasets. Best scores in **bold**, second best <u>underlined</u>. The asterisk (\*) indicates statistically significant improvements at p < 0.05 over the baselines.*

Table 2のUniSRec（シーケンシャルレコメンド）の結果より、EncodeRec（特にEncodeRec-300M）がすべてのデータセットで最高性能を達成し、他のベースラインを5〜26%上回った。また、EncodeRec-22MはBLaIRと比べてパラメータ数が6分の1〜16分の1でありながら、同等以上の競争力を持つ結果を出しており、効率性の高さが証明されている。モデルサイズやドメインデータの増加に伴うスケーラビリティも確認された。

| TIGER Model | Sports (Recall@10) | Sports (NDCG@10) | Beauty (Recall@10) | Beauty (NDCG@10) | Toys (Recall@10) | Toys (NDCG@10) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sentence-T5 | 0.0382 | 0.0199 | 0.0601 | 0.0322 | 0.0578 | 0.0295 |
| Blair-Base | 0.0270 | 0.0149 | 0.0546 | 0.0309 | 0.0583 | 0.0310 |
| Blair-Large | 0.0312 | 0.0170 | 0.0599 | 0.0316 | 0.0546 | 0.0294 |
| MiniLM-L6-v2 | 0.0370 | 0.0198 | 0.0640 | 0.0350 | 0.0597 | 0.0312 |
| EncodeRec-22M | <u>0.0389</u> | <u>0.0204</u> | <u>0.0689</u> | <u>0.0370</u> | **0.0663\*** | <u>0.0348</u> |
| EmbeddingGemma | 0.0380 | 0.0203 | 0.0656 | 0.0353 | 0.0609 | 0.0331 |
| EncodeRec-300M | **0.0395** | **0.0212** | **0.0694\*** | **0.0373\*** | <u>0.0627</u> | **0.0362** |

*Table 3: TIGER results across datasets. Best scores in **bold**, second best <u>underlined</u>. The asterisk (\*) indicates statistically significant improvements at p < 0.05 over the baselines.*

Table 3のTIGER（生成型レコメンドのためのセマンティックIDトークン化）の実験結果からも、EncodeRecのバックボーンが最も強力なベースラインを4〜9%定常的に上回っている。そして特筆すべき考察として、EncodeRecは「セマンティックIDの衝突（複数の異なるアイテムが同一のIDにマッピングされてしまう現象）」を完全に排除することに成功しており、生成型レコメンダの主要な弱点（表現空間の限界による曖昧性や誤差）を抜本的に解決する有用性が示された。
