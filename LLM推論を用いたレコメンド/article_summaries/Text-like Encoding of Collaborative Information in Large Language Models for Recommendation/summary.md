# 論文の要約：Text-like Encoding of Collaborative Information in Large Language Models for Recommendation

## 背景
大規模言語モデル（LLM）を用いたレコメンドシステム（LLMRec）において、ユーザやアイテムの「協調情報（Collaborative Information）」を統合することは、高精度な推薦を行う上で非常に重要である。従来の手法は、LLMの潜在空間に新たなトークンを追加して協調エンベディングをゼロから学習させるか、外部の協調フィルタリングモデル（MF等）の出力をLLMのトークンエンベディング空間へマッピングするアプローチをとっていた。しかし、これらの手法で得られる情報は元来の「テキスト」とはかけ離れた形式であり、汎用テキストデータの処理に特化したLLMの推論能力を最大限に引き出せていなかった。そこで本研究は、協調情報を「テキストライクな形式」にエンコードし、LLMにとって自然な入力を与えることで親和性を高める新しい手法「BinLLM」を提案している。

## 手法
BinLLMは、外部の協調モデルから取得したエンベディングを「二進数シーケンス（Binary Sequence）」に変換し、それを人間にも読めるテキストのようにプロンプトに埋め込む手法である。この枠組みにより、LLMがシーケンス同士の論理演算（ANDなど）のような推論を直接行いやすくなる。

具体的なステップと数式は以下の通りである。

1. **協調モデルによるエンベディング生成:**
ユーザ $u$ とアイテム $i$ の協調エンベディング（ $\bm{e}_{u}, \bm{e}_{i}$ ）を外部の協調モデル（例：$f_c$）から取得する。
$$ \bm{e}_{u} = f_c(u;\theta) $$
$$ \bm{e}_{i} = f_c(i;\theta) $$

2. **二値化（Binarization）:**
取得した実数値エンベディングを、完全結合層とtanh活性化関数 $\sigma(\cdot)$ に通し、最後に符号関数 $\text{sign}(\cdot)$ を適用して二値シーケンス $\bm{h}_u, \bm{h}_i$ へ変換する。
$$ \bm{h}_u = \text{sign}(\sigma(W\bm{e}_u + b)) $$
$$ \bm{h}_i = \text{sign}(\sigma(W\bm{e}_i + b)) $$
ここで、符号関数は以下のように定義される。
$$ \text{sign}(x) = \begin{cases} 1, \quad \text{if } x>0 \\ 0, \quad \text{else} \end{cases} $$

3. **ドット付き十進法による圧縮（Compression）:**
二進数シーケンスはトークン長が長くなる課題がある。そこでIPv4アドレスと同様の考え方で、8桁ごとの二進数を1つの十進数に変換し、ドットで区切る表現手法（オプション）を提供する。
$$ \underbrace{10101100}_{172.}\underbrace{00010000}_{16.}\underbrace{11111110}_{254.}\underbrace{00000001}_{1}. $$

4. **LLMの予測とチューニング:**
上記で変換されたIDシーケンスと、アイテムのタイトルなどのテキスト履歴情報を一つのプロンプトに統合し、LoRAを用いて推論・予測 $\hat{y}$ を行う。
$$ \hat{y} = LLM_{\hat{\Phi}+\Phi^{'}}(p) $$
学習時には、実数値から二値化された結果で損失関数を最小化すると同時に、最初から協調情報をプロンプトに含めてしまうと「ショートカット」として過学習するのを防ぐため、テキストのみで事前学習した後に協調情報を追加する Two-step tuning を導入している。
$$ \mathop{minimize} \limits _{\theta, W,b} \sum_{(u,i,t)\in \mathcal{D}}{ \ell(t,\bm{h}_u^{\top}\bm{h}_i) } $$

## 結果

以下の各データセット（ML-1M, Amazon-Book）に基づき、BinLLMの有効性が検証された。

### Table 1: Statistics of the processed datasets.

| Dataset | #Train | #Valid | #Test | #User | #Item |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ML-1M | 33,891 | 10,401 | 7,331 | 839 | 3,256 |
| Amazon-Book | 727,468 | 25,747 | 25,747 | 22,967 | 34,154 |

### Table 2: Overall performance comparison

| Dataset | | ML-1M | | | Amazon-Book | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Methods | | AUC | UAUC | Rel. Imp. | AUC | UAUC | Rel. Imp. |
| Collab. | MF | 0.6482 | 0.6361 | 12.9% | 0.7134 | 0.5565 | 14.7% |
| | LightGCN | 0.5959 | 0.6499 | 15.8% | 0.7103 | 0.5639 | 14.2% |
| | SASRec | 0.7078 | 0.6884 | 3.0% | 0.6887 | 0.5714 | 15.3% |
| | DIN | 0.7166 | 0.6459 | 5.6% | 0.8163 | 0.6145 | 2.0% |
| LM+Collab. | CTRL (DIN) | 0.7159 | 0.6492 | 5.4% | 0.8202 | 0.5996 | 3.0% |
| LLMRec | ICL | 0.5320 | 0.5268 | 35.8% | 0.4820 | 0.4856 | 50.7% |
| | Prompt4NR | 0.7071 | 0.6739 | 4.1% | 0.7224 | 0.5881 | 10.9% |
| | TALLRec | 0.7097 | 0.6818 | 3.3% | 0.7375 | 0.5983 | 8.2% |
| LLMRec+Collab. | PersonPrompt | 0.7214 | 0.6563 | 4.5% | 0.7273 | 0.5956 | 9.9% |
| | CoLLM-MF | 0.7295 | 0.6875 | 1.5% | 0.8109 | 0.6225 | 1.7% |
| | CoLLM-DIN | 0.7243 | 0.6897 | 1.7% | 0.8245 | **0.6474** | -1.0% |
| Ours | BinLLM | **0.7425** | **0.6956** | - | **0.8264** | 0.6319 | - |

### Table 3: Results of the ablation studies

| Datasets | ML-1M | | Amazon-book | |
| :--- | :--- | :--- | :--- | :--- |
| Methods | AUC | UAUC | AUC | UAUC |
| BinMF | 0.7189 | 0.6654 | 0.8087 | 0.5895 |
| BinLLM-TO | 0.7097 | 0.6818 | 0.7375 | 0.5983 |
| BinLLM-IO | 0.7307 | 0.6797 | 0.8173 | 0.5919 |
| BinLLM-IT | 0.7286 | 0.6842 | 0.8246 | 0.6165 |
| BinLLM | 0.7425 | 0.6956 | 0.8264 | 0.6319 |

### Table 4: Example of the used prompt template

| |
| :--- |
| #Question: A user has given high ratings to the following books: <ItemTitleList>. Additionally, we have information about the user's preferences encoded in the feature <UserID>. Using all available information, make a prediction about whether the user would enjoy the book titled <TargetItemTitle> with the feature <TargetItemID>? Answer with "Yes" or "No". \n#Answer: |


### 各Figureの参照と考察

![BinLLM Architecture](/Users/masashiueno/業界まとめ文書/LLM推論を用いたレコメンド/article_summaries/Text-like Encoding of Collaborative Information in Large Language Models for Recommendation/images/binLLM_v3.png)
**Figure 1**: BinLLMのアーキテクチャ。紫色がテキストフィールド（映画名や本のタイトルなど）、赤色が協調情報を「二進数シーケンス」にテキストとして変換して埋め込まれたIDフィールド（<UserID>等）を表している。

![ML-1M Warm](/Users/masashiueno/業界まとめ文書/LLM推論を用いたレコメンド/article_summaries/Text-like Encoding of Collaborative Information in Large Language Models for Recommendation/images/RQ1_1.png)
![Amazon-book Warm](/Users/masashiueno/業界まとめ文書/LLM推論を用いたレコメンド/article_summaries/Text-like Encoding of Collaborative Information in Large Language Models for Recommendation/images/RQ1_3.png)
![ML-1M Cold](/Users/masashiueno/業界まとめ文書/LLM推論を用いたレコメンド/article_summaries/Text-like Encoding of Collaborative Information in Large Language Models for Recommendation/images/RQ1_2.png)
![Amazon-book Cold](/Users/masashiueno/業界まとめ文書/LLM推論を用いたレコメンド/article_summaries/Text-like Encoding of Collaborative Information in Large Language Models for Recommendation/images/RQ1_4.png)
**Figure 2**: ML-1M、Amazon-BookそれぞれのWarmおよびColdシナリオにおける性能比較。

![ML-1M Compression](/Users/masashiueno/業界まとめ文書/LLM推論を用いたレコメンド/article_summaries/Text-like Encoding of Collaborative Information in Large Language Models for Recommendation/images/ml-compression.png)
![Amazon-book Compression](/Users/masashiueno/業界まとめ文書/LLM推論を用いたレコメンド/article_summaries/Text-like Encoding of Collaborative Information in Large Language Models for Recommendation/images/amazon-compression.png)
**Figure 3**: 協調情報エンベディングを二進数ではなくIPv4アドレスのような「ドット付き十進法（compression）」で圧縮して用いた際と、非圧縮の場合の性能比較。

#### 考察のまとめ

1. **全体性能の向上（Table 2）:**
ただの協調フィルタリングモデルはもちろん、従来のLLMを用いた推薦手法（Prompt4NRやTALLRec等）と比較しても、BinLLMは多くの指標で最高精度を記録した。注目すべきは、ベースとされた協調部分が単純なMFであるにも関わらず、DINといったより高精度な協調モデルを用いた別手法「CoLLM-DIN」をも大半の指標で上回っている点である。これは、協調情報を「テキスト」として自然に組み込ませることがLLMの潜在能力を大きく引き出していることを示唆している。
2. **Warm/Coldシナリオ双方への耐性（Figure 2）:**
既存手法のLLMRec（TALLRec等）はWarmシナリオで性能が落ちる傾向にあったが、BinLLMは充実した協調情報を活用することでWarmシナリオでもMF等の既存手法を上回る結果を出した。さらにColdシナリオでも既存LLMRecと同等以上に優位性があり、シナリオ問わず高い汎化性能を持つことが実証された。
3. **二進数化シーケンスの重要性（Table 3）:**
テキスト情報なし（BinLLM-IO）や協調情報なし（BinLLM-TO）のバリエーションよりも、両者を統合した元手法が圧倒的に性能が高い。さらに、単純な文字列化（UMAPを用いた次元圧縮など）を試した実験結果よりも、二値化アプローチの方が高い予測精度を保っていた。これは、LLMが「ビット単位の並び」をテキストのトークン列として直接解釈し、論理的なANDなどの比較演算に相当する推論を自然に実行できるためと考察されている。
4. **圧縮による効率性の証明（Figure 3）:**
プロンプトのトークン消費が増える課題に対して、上述したドット付き十進数（IPv4的記法）の圧縮を行っても、Figure 3のように予測性能（AUC/UAUC）や全体的な精度の傾向はほぼ同水準を維持できることがわかった。これにより、モデルの推論効率を向上させつつ実用的なデータ幅に収める手段が確保されている。
