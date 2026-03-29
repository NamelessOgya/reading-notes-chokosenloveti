# 次に読むべき論文 (Next to Read)

本論文（LLMD4Rec: "Bidirectional Knowledge Distillation for Enhancing Sequential Recommendation with Large Language Models"）は発表されて間もない最新の論文であるため、現時点で本論文を直接引用（Cited by）して手法を発展させている後続研究は確認されませんでした。

しかし、同分野・同時期に発表された関連研究（Concurrent Work）として、LLMの知識を推薦システムに蒸留する（あるいはその逆を行う）手法が複数提案されています。同じく「LLMを用いた蒸留技術」の切り口から、それぞれ異なるアプローチを採用している以下の論文を「次に読むべき関連論文」として推奨します。

## Concurrent Work (同分野の最新関連論文)

1. **Active Large Language Model-based Knowledge Distillation for Session-based Recommendation (ALKDRec)**
   - **アプローチの方向性:** こちらもLLMから軽量モデルへの知識蒸留を行いますが、LLMの推論結果の「質」に着目し、有益なサンプルを能動的に選択（Selective Instance Distillation）することで効率を高めるという「データ選別」の観点からアプローチしています。
   - **本論文との比較:** 本論文が「双方向のサイクル」によるモデル自身の漸進的なアップデートに焦点を当てているのに対し、ALKDRecは「LLMが自信を持って予測できた良質なデータだけを蒸留する」というノイズ除去・効率化の側面に焦点を当てています。

2. **SLMRec: Distilling Large Language Models into Small for Sequential Recommendation**
   - **アプローチの方向性:** LLMを軽量モデル（Small Language Model）へ直接蒸留する枠組みに特化し、デプロイメントの効率性に極振りしたようなアプローチを取る研究です。

3. **Distillation Matters: Empowering Sequential Recommenders to Match the Performance of Large Language Model**
   - **アプローチの方向性:** 既存の軽量推薦モデル（CRM）がLLMの性能にどこまで追いつけるか、という問いに対し一方向の蒸留を極限まで洗練させる検証を行っています。LLMD4Recが「双方向」で性能を押し上げるのに対し、「一方向」の限界を追求している点で比較対象として最適な論文です。

4. **RDRec: Rationale Distillation for LLM-based Recommendation**
   - **アプローチの方向性:** 推薦のスコアや結果だけでなく、LLMが推薦アイテムを選定した「推論過程（Rationale）」そのものを蒸留することで、軽量モデルの解釈性や論理的推論力を向上させる手法です。スコア分布の双方向蒸留（LLMD4Rec）とは異なり、テキストやロジックそのものに焦点を当てています。
