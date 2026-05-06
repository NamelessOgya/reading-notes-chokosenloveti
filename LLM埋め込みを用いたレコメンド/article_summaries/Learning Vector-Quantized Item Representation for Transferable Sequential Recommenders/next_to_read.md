# 次に読むべき論文 (Next to Read)

本論文（VQ-Rec）は、テキストエンコーディングを直接利用するのではなく、**ベクトル量子化（離散コードブック）**を挟むことでドメイン間のギャップを吸収し、レコメンドの転移性能を劇的に向上させました。

この「アイテムを離散的なセマンティックID（コード）で表現する」というアプローチは、LLMやGenerative AIとレコメンドを融合させる上で非常に重要なパラダイムシフトとなっています。APIのRate Limit制限等により直接の引用関係（Cited by）の全量抽出は控えましたが、VQ-Recと同じ問題意識（連続値表現の限界と離散セマンティック表現の活用）から発展した**Concurrent Work（同時期・後続の関連研究）**を以下に列挙します。

## 1. Recommender Systems with Generative Retrieval (TIGER)
- **関連性・アプローチ**: VQ-RecがTransformerベースのエンコーダとPQ（Product Quantization）を用いてアイテムを離散コード化（Semantic ID）したのに対し、TIGERはRQ-VAE (Residual Quantized Variational AutoEncoder) を用いてアイテムテキストから階層的なSemantic IDを生成し、これをLLM（Seq2Seqモデル）に直接生成させる「Generative Retrieval」のアプローチをとっています。アイテムをID番号ではなく「意味を持つ離散トークン」として扱う点で、VQ-Recの思想をLLMネイティブな生成タスクへと昇華させた代表的な研究です。

## 2. BLaIR: Bridging Language and Items for Retrieval and Recommendation
- **関連性・アプローチ**: VQ-Recがテキスト表現の強固すぎる結びつきを解消するために離散化を用いたのに対し、BLaIRはテキストベースのLLM埋め込みとアイテムIDの埋め込みを対照学習（Contrastive Learning）等を用いて柔軟にアラインメント（Bridging）するアプローチをとっています。離散化（VQ）を行わずに連続空間のままドメインギャップをどう埋めるかという別角度の解決策として比較する価値があります。

## 3. How to Index Item IDs for Recommendation Foundation Models (2023)
- **関連性・アプローチ**: VQ-Recで用いられたPQ（Product Quantization）などのベクトル量子化を含む、様々なアイテムのインデックス化手法（Semantic ID, Random ID, RQ-VAE等）を体系的に比較・評価した論文です。「どのようにアイテムを離散的なコードにマッピングするのが最も転移性や精度が高いのか」という根本的な問いに対して、包括的なベンチマークを提供しており、VQ-Recの手法に対するマクロな理解を深めるのに最適です。
