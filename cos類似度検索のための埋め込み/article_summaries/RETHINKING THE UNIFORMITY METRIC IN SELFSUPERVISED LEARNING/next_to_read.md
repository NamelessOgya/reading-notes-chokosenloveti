# 次に読むべき論文 (Next to Read)

## Understanding Dimensional Collapse in Contrastive Self-supervised Learning
- **arXiv ID:** 2110.09348
- **推薦理由:**  
本論文（RETHINKING THE UNIFORMITY METRIC IN SELFSUPERVISED LEARNING）が発表された直後である等の理由により、明確にこの論文の課題設定（WassersteinベースのUniformity指標）を直接発展させたフォローアップ研究（Cited by）を発見することが困難でした。
そのため、本論文が解決のターゲットとしている「Dimensional Collapse（表現の次元崩壊）」という現象の根本的な理解と、別角度からの解決アプローチを提示している同分野のもっとも重要な関連論文（Concurrent / Foundational Work）の一つとして、本論文を推薦します。

この論文では、対照学習（Contrastive Learning）が完全なConstant Collapseを回避できるにも関わらず、なぜ一部の次元しか活用されないDimensional Collapseを引き起こしてしまうのかを理論および実験から解明しています。原因として「過度なデータ拡張による正例ペアの相関喪失」と「過剰パラメータ化されたネットワークが暗黙的に引き起こす低ランク正則化」の2点を指摘し、プロジェクタを用いず表現空間を直接最適化する手法（DirectCLR）を提案しています。
Wasserstein距離を用いたLoss項の追加によってDimensional Collapseを防ごうとする本要約論文の理解を深める上でも、事前知識・比較対象として非常に有用な文献です。
