- **Dual Correction Strategy for Ranking Distillation in Top-N Recommender System** (Lee & Kim, CIKM 2021)
  - 対象論文のCDの手法（教師と生徒モデル間の単方向で、主に一方的な知識伝達に基づいている）を発展させ、教師モデルと生徒モデル間の「差分（Discrepancy）」に着目し、生徒モデルがうまく予測できない部分に対して集中的に補正（Correction）のガイダンスを与える手法。ユーザー側とアイテム側の両面からのランキング情報を活用し、より効果的なTop-N推薦を実現している。
  
- **Bidirectional Distillation for Top-K Recommender System** (Kweon et al., The Web Conference 2021)
  - 対象論文のCDが一方通行の蒸留であるのとは対照的に、教師モデルと生徒モデルの双方向（Bidirectional）で知識を蒸留・共有する枠組みを提案。両モデルが互いに協調・補完しあう（Mutual Learning）ことで、一方通行よりも高い汎化性能と推薦精度を達成している。
