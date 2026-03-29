# Next to Read Papers

対象論文（SLMRec: Distilling Large Language Models into Small for Sequential Recommendation）は2024年のごく最近の発表（ICLR 2025等向け）であるため、現在のアカデミックデータベースからこの論文を直接引用している「被引用論文（Cited by）」をリストアップすることはできませんでした（※ルールに記載されている被引用論文の幻覚（捏造）を防止するための措置です）。

代替案として、発表時期が重なっており同じシーケンシャル・リコメンデーションと大規模言語モデル（LLM）の知識蒸留に着目している**「同時期の関連・最新論文（Concurrent Work）」**を次に読む論文として推奨します。

1. **Active Large Language Model-based Knowledge Distillation for Session-based Recommendation (ALKDRec)**
   - **理由**: LLMの持つ広範な一般知識を「汎用的なセッションベース推薦機構」に伝達する手法であり、SLMRecと目的（推薦システムにおけるLLMからの知識蒸留）を共有しています。アクティブラーニングによってLLMの「ノイズを削減」する側面を取り入れており、蒸留の品質を向上させるアプローチとしてSLMRecとの比較検討に非常に有益です。

2. **LLMD4Rec: Mutual Distillation Framework**
   - **理由**: 推薦システムにおけるLLMの活用で、「教師・学生モデリング」の中で互いに強みを引き出す相互蒸留（Mutual Distillation）に焦点を当てたごく最近のフレームワークです。SLMRecのような層の削減アプローチと、相互蒸留の組み合わせが今後どのような相乗効果を生むかを洞察するためのステップとして最適です。

3. **Distillation Matters: Empowering Sequential Recommenders to Match the Performance of Large Language Model**
   - **理由**: SLMRecと同じく、LLMの持つ高度な推薦性能を比較的小さいシーケンシャル推薦モデルに転移させる課題解決を目的とした最新論文です。Studentモデルの構造やターゲット知識の配分方法について、SLMRecのアプローチ（層ごとのL2やコサイン類似度）とどのプロセスに差異があるか、タスクにおける最適解を議論するために必読です。
