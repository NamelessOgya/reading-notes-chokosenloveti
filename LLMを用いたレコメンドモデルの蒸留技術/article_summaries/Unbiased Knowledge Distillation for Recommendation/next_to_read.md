# 次に読むべき論文 (Next to Read)

## 対象論文の「Cited by」に関する調査結果
UnKD（Unbiased Knowledge Distillation for Recommendation, WSDM 2023）は推薦システムにおける「人気度バイアス」という重要な課題に対して因果推論アプローチで知識蒸留を改善した非常に先進的な研究です。
検索による調査を行った結果、いくつかの後続研究による引用やサーベイ論文（MDPI等）での言及が確認できましたが、「UnKDの手法を直接的に拡張・発展させた特定のSOTA後続研究」を明確に単一指定することは（ハルシネーションを避ける観点から）困難でした。

そのため、代替案として本論文と同分野・同発表時期の最新関連論文（Concurrent Work / Recent Progress）から、「レコメンドモデル蒸留におけるバイアスの解消」や「高度な知識転移」という観点で次に読むべき論文を列挙します。

## おすすめの関連論文（Concurrent/Recent Works）

### 1. 蒸留における情報損失やバイアスの別角度からのアプローチ
- **PCKD: Preference-Consistent Knowledge Distillation (2023)**
  - **概要**: 知識蒸留において、教師モデルの特徴次元を学生モデルにアライメントする際に、ユーザーの本来の「好み」が一貫せずに欠如・干渉してしまうという課題（Preference Inconsistency）を指摘した論文です。UnKDが人気度という外部要因の排除を目指したのに対して、こちらは特徴量転送プロセスそのものを正規化することで一貫性のあるクリーンな蒸留を目指しています。

- **FreqD: Frequency-Aware Feature Distillation (2024)**
  - **概要**: 従来のKDがすべての特徴量成分を一律に扱うことにより発生する情報の欠落に着目し、「周波数（Frequency）」の観点から重要な特徴成分を重み付けして蒸留するより洗練された手法です。

### 2. LLM（大規模言語モデル）を用いたレコメンド蒸留基盤の最新動向
推薦分野のKDは、昨今急速に「推論速度の遅いLLMから軽量な従来モデルへの蒸留」というパラダイム（LLM2Rec Distillation）にシフトしています。UnKDの「教師モデルが抱く偏りをいかにクリーンに取り除くか」という問題意識は、巨大なLLMを教師にする際により一層重要となります。

- **DLLM2Rec: Distilling Knowledge from LLMs into Sequential Recommenders (2024)**
  - **概要**: 大規模言語モデル（LLMs）からシーケンシャルレコメンダーに対し、ランキングの重要度を考慮した「Importance-aware ranking distillation」および協調埋め込み知識を蒸留するフレームワークです。

- **Active Large Language Model-based Knowledge Distillation for Session-based Recommendation (ALKDRec) (2024)**
  - **概要**: 大量のデータに対して一律に高コストなLLMでラベルを生成するのではなく、能動学習（Active Learning）を用いて「有益な少数のインスタンス」だけをインテリジェントに選択して学生モデルに蒸留する手法です。「最も効果的でノイズの少ないデータを教師から抽出する」というコンセプトにおいてUnKDの思想と相性が良い研究です。
