# 次に読むべき論文 (Next to Read)

## Cited By (被引用論文)
当該論文（Active Large Language Model-based Knowledge Distillation for Session-based Recommendation, AAAI 2025）は発表直後の非常に新しい研究であるため、**本論文の手法を直接発展させた、あるいは引用している具体的な後続論文は現在のところ見つかっていません**。

## 代替案: 同時期の最新関連論文 (Concurrent Work)
被引用実績が存在しないため、代替として「知識蒸留(KD) × LLM × 推薦システム(Recommendation)」の領域で同時期（2025年）に発表された以下の関連論文を調査対象として提案します。

1. **LLMD4Rec: Mutual Distillation Framework**
   - **概要**: 従来の「LLM (大規模だが重い教師モデル) から軽量推薦モデル (生徒) への『一方向』の蒸留」による静的な知識転移の限界を克服すべく、「双方向 (Mutual) の蒸留フレームワーク」を提案している論文です。
   - **ALKDRecとの違い・比較点**: ALKDRecが推論インスタンスの「選択側（Active Learning）」で最適化・効率化を目指したのに対し、LLMD4Recは「モデル同士の相互の学習（Mutual Learningによる分布の動的アライメント）」によって性能向上と推論の効率化にアプローチしており、別角度からの手法として非常に参考になります。

2. **Large Language Model Enhanced Recommender Systems: A Survey (March 2025)**
   - **概要**: 2025年時点での強力な推論機能を持つLLMを推薦システムに応用した最新の研究群を体系的にまとめたサーベイ論文です。
   - **参考点**: 知識蒸留(KD)がLLMの能力を軽量モデルに移行させるための主要な圧縮技術として言及されており、「Feature-based」や「Response-based」といった複数のプロセスが整理されているため、SBR文脈に限らず、当トピックの手法の全体像や最新トレンドを俯瞰するために有用です。
