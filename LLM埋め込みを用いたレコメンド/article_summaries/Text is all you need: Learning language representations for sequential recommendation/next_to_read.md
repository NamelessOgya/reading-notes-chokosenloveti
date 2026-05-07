# 次に読むべき論文 (Next to Read)

本論文（**Text Is All You Need**: Learning Language Representations for Sequential Recommendation）は非常に注目度が高く、発表後すでに多くの後続研究に引用されています。以下に、本論文のアプローチ（LLMとテキストを用いた逐次レコメンド）を発展させている、または別角度からアプローチしている被引用論文を列挙します。

## 1. LLaRA: Aligning Large Language Models with Sequential Recommenders (2023)
- **Authors:** Jiayi Liao, Sihang Li, Zhengyi Yang et al.
- **URL:** [https://www.semanticscholar.org/paper/0e8dec431a62dea147139d7805ab3a0a97bf3857](https://www.semanticscholar.org/paper/0e8dec431a62dea147139d7805ab3a0a97bf3857)
- **推し理由:** 
  本論文（Recformer）は自前の「Longformerテキストエンコーダ」によって推薦問題を解いていましたが、LLaRAは一歩進んで、より汎用的で巨大なLLMを推薦システムのアラインメント（LLMとRecommenderの融合）として組み込む手法を提案しています。言語モデルをどのように推薦特化させるかという点で、テキスト表現学習の正統進化的なアプローチと言えます。

## 2. Adaptive knowledge-augmented multi-domain recommendation with large language models
- **Authors:** Yakun Li, Tian Tian, Jinman Cui et al.
- **URL:** [https://www.semanticscholar.org/paper/6402075b02ed93e1d65d99658fdeebe0523a4e61](https://www.semanticscholar.org/paper/6402075b02ed93e1d65d99658fdeebe0523a4e61)
- **推し理由:** 
  Recformerが解決を試みた課題の一つである「ドメイン間の知識転移（Cross-domain / Multi-domain recommendation）」に対して、LLMの持つ豊富な外部知識（Knowledge-augmented）を適応的に活用することでアプローチした研究です。マルチドメイン推薦においてLLMの知識をいかに引き出すかを主眼としており、Text-onlyからLLM-augmented表現へのパラダイムシフトとして比較するのに最適です。

## 3. Sequential recommender systems: A methodological taxonomy and research frontiers
- **Authors:** Yanbo Zhou, Gang-Feng Ma, Xilin Wen et al.
- **URL:** [https://www.semanticscholar.org/paper/d2fb78892cd8ceeb1f38134934f5d1e5a5a87291](https://www.semanticscholar.org/paper/d2fb78892cd8ceeb1f38134934f5d1e5a5a87291)
- **推し理由:** 
  逐次レコメンド（Sequential Recommender Systems）の最前線と手法体系を網羅的に整理したサーベイ論文です。IDベース（SASRec等）からText-onlyベース（Recformer, UniSRec等）、さらに巨大言語モデル（LLMs）を利用した最新動向に至るまでの歴史的な進化と限界が俯瞰的に解説されています。分野全体のフロンティアを整理するための一本として大いに役立ちます。
