# Harnessing Large Language Models for Text-Rich Sequential Recommendation

## 背景
LLM（Large Language Models）は自然言語処理（NLP）分野で強力な推論およびゼロショット・フューショット学習能力を示しており、レコメンドシステム（RS）での応用が盛んに研究されている。とくに「LLM as RS」として、ユーザープロファイル、行動履歴データ、タスク指示をプロンプトとしてLLMに入力して推薦結果を得る手法が一般化しつつある。
しかしながら、eコマースの商品タイトルやSNSのニュース見出しのように「アイテムが豊富なテキスト情報を持つ（Text-Rich）」シーケンシャル・レコメンドのシナリオにおいて、従来の枠組みをそのまま適用すると以下の課題が生じる：
1. **入力長制限（Context Length Limitation）:** ほとんどのLLMは一定のトークン長制限を設けており、長大なユーザーの履歴全体を含めることができない（切り捨てると性能が低下する）。
2. **計算リソースの過剰なオーバーヘッド:** Transformerの計算量はシーケンス長の2乗（$O(n^2)$）となるため、長いテキスト入力はスループットを低下させ、リアルタイム性が求められる推薦システムにおいて致命的となる。
3. **ユーザー嗜好変化の捕捉難易度の上昇:** 文脈が長すぎる（Lost in the middle等の問題）と、LLMはユーザーの最近の嗜好の移り変わりを効果的に捉えることが困難になる。

これらの課題を解決するため、本論文では「Harnessing Large Language Models for Text-Rich Sequential Recommendation (LLM-TRSR)」という新しい枠組みを提案した。

![図1: A schematic diagram of our method.](./images/intro.png)

## 手法
LLM-TRSRは、以下の主要ステップで構成される。
1. ユーザーの行動履歴シーケンスを長いテキストに変換し、それを複数の小さな「ブロック（Blocks）」に分割する。LLMの最大トークン長制限（実験では2048トークン）に収めるため、**アイテム数（実験では1ブロックあたり5アイテム）**を基準にして固定数で分割を行う。
2. **要約器（LLM-based Summarizer）** を用いて各ブロックからユーザーの嗜好の要約（Preference Summary）を抽出する（ゼロショット推論でパラメータは固定）。抽出方法として、「CNN（畳み込み）」と「RNN（再帰）」にインスパイアされた2つのパラダイムを提案。
3. **推薦器（LLM-based Recommender）** に対して、「ユーザー嗜好の要約」「最近の行動履歴」「候補アイテムの情報」を含めたプロンプトを入力し、候補アイテムを推薦（"Yes" または "No"）させる。
4. この推薦器をSFT（Supervised Fine-Tuning）とLoRA（Low-Rank Adaptation）を用いてパラメータ効率よく学習・微調整する。

### 1. ユーザー嗜好の要約抽出
要約の抽出パラダイムとして以下の2つを提案している。要約モデルとしては、強力な要約性能を持つLlama-30b-instructを採用している。

**階層的要約（Hierarchical Summarization）**
CNNに似た構造を持つアプローチ。履歴から作成した複数ブロックをまず個別に要約させ（短期的な嗜好や細部を獲得）、次に得られた複数の要約をLLMに再入力して総合的な要約を生成させる（抽象的で広範な長期嗜好を獲得）。

![図2: 階層的要約パラダイムの概略図](./images/hierarchical.png)
![図3: 個別ブロックの要約例](./images/block_summary.png)
![図4: 複数の要約を統合する階層的要約例](./images/hierarchical_summary.png)

**再帰的要約（Recurrent Summarization）**
RNNに似た構造を持つアプローチ。まず最初のブロックを要約し、次に「1つ前の要約テキスト」と「次のブロックの行動データ」をLLMに入力して要約を再帰的に更新させていくことで、最終的なユーザー嗜好の要約を得る。長期的興味を維持しつつ、短期的傾向の更新が行える。

![図5: 再帰的要約パラダイムの概略図](./images/recurrent.png)
![図6: 最初のブロックの要約例（MINDデータセット）](./images/first_block_MIND.png)
![図7: 再帰的要約による要約の更新例](./images/recurrent_summary.png)


### 2. LLMベースの推薦タスク
ユーザーの嗜好要約ベクトル（テキスト）が得られたら、過度な計算オーバーヘッドなしに推薦器を稼働させることができる。
推薦器へのプロンプトは以下の5つのパートで構成される：

- **Recommendation Instruction（タスク指示）**
  LLMに対して「要約と直近の履歴を考慮して推薦タスクを解く」という役割を与え、出力を "yes" か "no" に強制するシステム指示。
- **Preference Summary（長期的な嗜好の要約）**
  前段の要約器によって生成された「このユーザーはどういう属性を好むか」という抽象化された長期的な嗜好テキスト。
- **Recent User Behavior（直近の短期的な行動）**
  ユーザーが直近で閲覧した数件のアイテムテキスト。要約だけでは捉えきれない、現在の短期的なコンテキストを提供する。
- **Candidate Item Description（候補アイテムの情報）**
  推薦対象となるターゲットアイテムのタイトルや説明文などのテキスト属性。
- **Final Answer（回答出力用スロット）**
  学習時はここに正解ラベル（"yes" か "no"）を入れてNext-token predictionで学習し、推論時は空欄にして "yes" と "no" の生成確率を取得する。

**【構築されるプロンプトの具体例（イメージ）】**
```text
[Recommendation Instruction]
You are an expert recommendation system. Based on the user's preference summary and their recent interaction history, please predict whether the user will click on the candidate item. Please only output "yes" or "no".

[Preference Summary]
User Preference: The user has a strong interest in outdoor sports equipment...

[Recent User Behavior]
Recent History:
1. Title: "Columbia Men's Waterproof Hiking Shoes"
2. Title: "LED Camping Lantern, Rechargeable"

[Candidate Item Description]
Candidate Item:
Title: "Portable Camping Stove, Windproof"
Description: "This compact camping stove is perfect for outdoor cooking..."

[Final Answer]
Answer: 
```

学習時は、上記のプロンプト全長 $L$ に対してLLMの自己回帰モデルに基づくSFTロス（Next-token prediction）を最適化する。

$$ \mathcal{L}_{sft} = -\sum_{i=1}^{L} \log \Pr(v_{i}|v_{<i}), $$

推論時は、プロンプトの最後に続く予測確率として 'yes' と 'no' のスカラー値を生成し、これをsoftmaxにかけることで確率スコア $p$ を得る。

$$ p_{yes} = \Pr('yes'|P),\quad p_{no} = \Pr('no'|P). $$

$$ p = \frac{\exp(p_{yes})}{\exp(p_{yes})+\exp(p_{no})}. $$

![図8: LLM-based Recommendationの全体像とプロンプト例](./images/recommend.png)


## 結果
提案手法の効果を検証するため、商品推薦のAmazon-M2データセットと、ニュース推薦のMINDデータセットで実験を行った。

### データセットの統計情報
Table 1は用いたデータセットの詳細な統計である。MINDよりAmazon-M2のほうが1アイテムあたりのトークン数が多いことがわかる。

| description | Amazon-M2 | MIND |
| :--- | :--- | :--- |
| # of different attributes | 10 | 4 |
| # of positive samples in the training set | 10,000 | 10,000 |
| # of positive samples in the validation set | 1,000 | 1,000 |
| # of positive samples in the test set | 1,000 | 1,000 |
| Avg. # of historical user behavior sequence | 13.16 | 16.23 |
| Avg. # of tokens corresponding to an item | 141.45 | 40.83 |

### 比較評価結果
Table 2は全ベースラインとの性能比較である。評価はRecallとMRRを用いた。

| | Amazon-M2<br>Recall@3 | Amazon-M2<br>Recall@5 | Amazon-M2<br>Recall@10 | Amazon-M2<br>MRR@3 | Amazon-M2<br>MRR@5 | Amazon-M2<br>MRR@10 | MIND<br>Recall@3 | MIND<br>Recall@5 | MIND<br>Recall@10 | MIND<br>MRR@3 | MIND<br>MRR@5 | MIND<br>MRR@10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| NCF | 0.8300 | 0.8830 | 0.9440 | 0.7328 | 0.7448 | 0.7529 | 0.7010 | 0.8030 | 0.9240 | 0.5523 | 0.5759 | 0.5926 |
| DIN | 0.7380 | 0.8330 | 0.9240 | 0.5838 | 0.6053 | 0.6174 | 0.7900 | 0.8620 | 0.9330 | 0.6352 | 0.6519 | 0.6616 |
| DIEN | 0.7330 | 0.8170 | 0.9070 | 0.5922 | 0.6114 | 0.6229 | 0.7300 | 0.8200 | 0.9140 | 0.6045 | 0.6251 | 0.6379 |
| GRU4Rec | 0.4420 | 0.5590 | 0.7350 | 0.3355 | 0.3621 | 0.3855 | 0.6650 | 0.7970 | 0.9260 | 0.5305 | 0.5610 | 0.5787 |
| NARM | 0.8410 | 0.8860 | 0.9330 | 0.7475 | 0.7577 | 0.7638 | 0.5820 | 0.7330 | 0.8930 | 0.4142 | 0.4489 | 0.4703 |
| SASRec | 0.6550 | 0.7570 | 0.9040 | 0.4938 | 0.5173 | 0.5374 | 0.8420 | 0.8960 | 0.9410 | 0.7447 | 0.7574 | 0.7636 |
| CORE | 0.5230 | 0.4632 | 0.6450 | 0.4527 | 0.4632 | 0.4728 | 0.5170 | 0.5580 | 0.6370 | 0.4392 | 0.4488 | 0.4586 |
| TALLRec | 0.8790 | 0.9050 | 0.9460 | 0.8585 | 0.8644 | 0.8697 | 0.8580 | 0.9020 | 0.9590 | 0.7708 | 0.7807 | 0.7885 |
| LLM-TRSR-Hierarchical | **0.8910** | 0.9120 | 0.9490 | 0.8597 | 0.8643 | 0.8693 | **0.9160** | **0.9430** | 0.9750 | **0.8505** | **0.8568** | **0.8611** |
| LLM-TRSR-Recurrent | **0.8910** | **0.9130** | **0.9570** | **0.8632** | **0.8681** | **0.8737** | 0.9060 | 0.9390 | **0.9840** | 0.8400 | 0.8475 | 0.8534 |

結果として、提案手法である `LLM-TRSR-Hierarchical` および `LLM-TRSR-Recurrent` の両方が全てのベースラインを上回り、LLMを直接用いるTALLRecよりも高い精度を達成した。また、Amazon-M2ではRecurrentパラダイムが、MINDデータセットではHierarchicalパラダイムが優勢となった。これは、ドメインごとに嗜好の捉え方（推移的変化を重視するか、より普遍的な上位概念の興味を重視するか）が異なるためであると推察される。

### 直近履歴の入力数の影響（Ablation）
プロンプトに含める直近履歴のアイテム数（Historical Item Number）を変化させた際の性能推移を確認した。

![図9: Amazon-M2におけるHistorical Item Numberごとの性能推移 (Hierarchical)](./images/amazon_hierarchical_item_num.png)
![図10: Amazon-M2におけるHistorical Item Numberごとの性能推移 (Recurrent)](./images/amazon_recurrent_item_num.png)
![図11: MINDにおけるHistorical Item Numberごとの性能推移 (Hierarchical)](./images/MIND_hierarchical_item_num.png)
![図12: MINDにおけるHistorical Item Numberごとの性能推移 (Recurrent)](./images/MIND_recurrent_item_num.png)

直近のアイテム数は3つの場合に最良のパフォーマンスを示した。直近履歴を0（全く含めず、要約のみから判断）とした設定でも従来手法を凌駕する強力な結果が得られており、要約自体の質の高さが証明されている。

### モデルサイズの影響
**推薦モデル（Recommender）のパラメータサイズ**
推薦器のバックボーンとしてLlama-2-7bを使用したが、Pythiaの1.4b、2.8bモデルと比較した。当然ながらモデルサイズが大きいほど推薦性能は高く、実運用では精度と計算コストのトレードオフが重要であると指摘されている。

![図13: Amazon-M2における推薦モデルサイズの影響 (Hierarchical)](./images/amazon_hierarchical_model_size.png)
![図14: Amazon-M2における推薦モデルサイズの影響 (Recurrent)](./images/amazon_recurrent_model_size.png)

**要約モデル（Summarizer）のパラメータサイズ**
Llama-30b-instructの代わりに、より小規模なLlama-2-13bを用いた場合を比較した。結果は、13Bのモデルではゼロショットでの要約品質が著しく悪化し、文脈の構造が乱れて人間でも理解しにくい出力となった。これにより、ユーザー嗜好の要約プロセスはパラメータ規模の大きなLLMの高度な推論能力に依存していることが判明した。

![図15: MINDにおける要約モデルサイズの影響 (Hierarchical)](./images/MIND_hierarchical_summary_size.png)
![図16: MINDにおける要約モデルサイズの影響 (Recurrent)](./images/MIND_recurrent_summary_size.png)
