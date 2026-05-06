# TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation

## 背景
大規模言語モデル (LLM) は、自然言語処理などの多くの分野で高い性能を示しており、推薦システムへの応用も期待されている。しかし、In-context Learning (ICL) などの既存アプローチ（ChatGPT等を活用）をそのまま推薦に適用しても、回答を拒否されたり、予測が常に肯定(Yes)に偏ったりするなど、ランダム推論と同等の性能しか出ない問題があった。筆者らは、この原因を「LLMの学習タスクと推薦タスクの間に大きなギャップがあること」および「事前学習時の推薦コーパスが不十分であること」だと考えた。このギャップを埋め、LLMの持つ豊富な知識と汎化能力を推薦タスクに活用するため、推薦データを用いてLLMのチューニングを行い「大規模推薦言語モデル (Large Recommendation Language Model: LRLM)」を構築することを提案した。

## 手法
提案されたチューニングフレームワーク「TALLRec」は、LLMを推薦タスクに適応させるための軽量かつ効率的な手法である。パラメータ効率の良いLoRAアーキテクチャを用いることで、単一のRTX 3090 (24GB) GPUと100件未満の少ない学習データ（Few-shot）でもLLM（本論文ではLLaMA-7B）をチューニングできるようにしている。TALLRecは以下の2つの学習ステージで構成される。

1. **Alpaca Tuning**: LLMの汎化能力を高めるため、Alpacaのself-instructデータを用いて通常のインストラクションチューニングを行う。
2. **Rec-tuning**: 推薦データをインストラクションチューニングの形式にフォーマットし、推薦用のチューニングを行う。
具体的には、以下のように推薦データを「自然言語のQ&Aタスク」として構築する。
   * **Task Instruction (指示)**: これまでの履歴を見て、新しいアイテムを気に入るか Yes/No で答えるようタスクのルールを固定の自然言語で指示。
   * **Task Input (入力)**: ユーザーが過去に高評価したアイテム名（Liked）と低評価だったアイテム名（Disliked）、そして予測対象のターゲットアイテム名を文字列としてそのまま埋め込む。
   * **Task Output (出力)**: 実際にユーザーが気に入るかどうかの正解ラベル（Yes または No）。

**【Rec-tuningのプロンプト構成例（映画推薦の場合）】**
> **Task Instruction:**
> Given the user's historical interactions, please determine whether the user will enjoy the target new movie by answering "Yes" or "No".
> 
> **Task Input:**
> User's liked items: GodFather.
> User's disliked items: Star Wars.
> Target new movie: Iron Man
> 
> **Task Output:**
> No.

TALLRecのチューニング目的関数は以下の通りである。
$$ \max_{\Theta} \sum_{(x,y)\in\mathcal{Z}} \sum_{t=1}^{|y|} \text{log} \left( P_{\Phi + \Theta}(y_{t} | x, y_{<t}) \right) $$
ここで、$\Phi$ は凍結された元のモデルパラメータ、$\Theta$ は学習によって更新されるLoRAのパラメータ、$x$ はInstruction Input、$y$ はInstruction Outputである。

## 結果

### 各種モデルとの性能比較 (RQ1)

|  | Few-shot | GRU4Rec | Caser | SASRec | DROS | GRU-BERT | DROS-BERT | TALLRec |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **movie** | 16 | 49.07 | 49.68 | 50.43 | 50.76 | 50.85 | 50.21 | **67.24** |
| | 64 | 49.87 | 51.06 | 50.48 | 51.54 | 51.65 | 51.71 | **67.48** |
| | 256 | 52.89 | 54.20 | 52.25 | 54.07 | 53.44 | 53.94 | **71.98** |
| **book** | 16 | 48.95 | 49.84 | 49.48 | 49.28 | 50.07 | 50.07 | **56.36** |
| | 64 | 49.64 | 49.72 | 50.06 | 49.13 | 49.64 | 48.98 | **60.39** |
| | 256 | 49.86 | 49.57 | 50.20 | 49.13 | 49.79 | 50.20 | **64.38** |

**Table 1: 従来手法およびTALLRecの少数ショット学習環境におけるAUC（×100）性能比較**

表1が示す通り、TALLRecはわずかなチューニングサンプル数（few-shot）であっても、従来の逐次推薦モデル（GRU4Rec, SASRecなど）を大きく上回る性能を達成した。従来のモデルは限られたサンプル数ではランダムレベル（AUC≒50）から学習を進めることができておらず、BERTでテキスト情報を追加しても改善が見られなかった。

![Figure 3](./images/Fig3.png)
**Figure 3: (a) LLMベースのゼロショット手法とTALLRecの比較。(b) TALLRecの各構成要素のアブレーションとサンプル数ごとの推移。**

図3(a)が示すように、ChatGPTなどを用いた In-context Learning（ゼロショット）は推薦タスクではAUC=0.5付近とランダムと同等の性能に留まったが、TALLRecは大幅な性能向上を示した。これはLLMのもつ言語タスクと推薦タスクの間に大きなギャップがあることを示し、推薦データによる「Rec-tuning」の必要性を裏付けている。

### アブレーションと汎化能力 (RQ2, RQ3)

![Figure 1](./images/Frame_work.png)
**Figure 2: TALLRecのフレームワーク構成。Alpaca TuningとRec-tuningの2ステージからなる。**



図3(b)のアブレーションスタディでは、Alpaca Tuningのみ(AT)に比べてRec-tuningを含むモデル(RT, TALLRec)が圧倒的に高い性能を示しており、Rec-tuningが推薦能力の獲得に不可欠であることがわかる。また、サンプル数が少ない場合（$\leq 128$）は、Alpaca TuningとRec-tuningを組み合わせた「TALLRec」が「RT」単体よりも優れた性能を示し、Alpaca Tuningが未知のタスクへの汎化能力を高める役割を果たしていることが確認された。

![Figure 4](./images/cross_domain.png)
**Figure 4: クロスドメインにおける汎化能力の評価（Movie/Bookデータ間）**

図4はクロスドメイン推薦の実験結果である。MovieデータのみでチューニングしたモデルがBookデータでも高い性能を示すなど、TALLRecが特定のドメインのデータに過学習するのではなく、推薦タスク自体を汎化して学習できていることが明らかになった。また、両方のデータ（Both）を用いて学習させた場合、より多くのドメインデータが汎化性能の向上に寄与することが確認されている。
