# 次に読むべき関連論文 (next_to_read.md)

本論文（Ranking Distillation: Learning Compact Ranking Models with High Performance for Recommender System, KDD 2018）は、レコメンド分野において「ランキング」に特化した知識蒸留（KD）を初めて導入した画期的な研究です。その後の数年間で、この基礎的な枠組みの課題である「教師の厳密な順位列をそのまま模倣させることによる最適化の難しさ（柔軟性の欠如）」や、「暗示的シグナル特有のスパース性」に対応するため、様々な発展研究が発表されています。

以下は、本論文の手法を直接的に拡張・発展させている代表的な後続研究（Cited by）です。

## 1. DE-RRD: Distillation Experts and Relaxed Ranking Distillation
- **著者**: Kang et al.
- **会議/年**: CIKM 2020
- **概要**:
  *Ranking Distillation* の直接的な発展版です。オリジナルの手法では、生徒モデルが教師モデルの全く同じ上位ランキング（順序）を厳密に模倣しようとするため、過度な制約がかかっていました。本論文はこの問題に対処するため、「Relaxed Ranking Distillation (RRD)」を提案しました。順位の一致を厳密に求めるのではなく、アイテム同士の「相対的な順序関係」という緩やかな制約で蒸留を行うことで、学習の柔軟性と効率を大幅に向上させています。

## 2. DCD: Dual Correction Strategy for Ranking Distillation in Top-N Recommender System
- **著者**: Youngjune Lee, Kee-Eung Kim
- **会議/年**: CIKM 2021
- **概要**:
  *Ranking Distillation* および *RRD* をさらに発展させた手法です。生徒モデルが教師モデル全体を蒸留するのではなく、教師と生徒の予測間の「乖離（Discrepancy）」に焦点を当て、生徒が苦手とする部分を集中的に補正するアプローチ（Correction Strategy）を取り入れています。さらに、ユーザー側からとアイテム側の両面からのランキングを利用する「Dual-Side」の蒸留を採用することで、暗示的フィードバックのスパース性の問題に根本的に対処しています。

---
**調査メモ**:
本論文（RD）の「上位K件の部分的な順序づけだけを学習対象とする」というアプローチからの進化としては、最初にDE-RRDの「さらに順序制約を緩める（Relaxed）」方向性を確認し、次にDCDの「生徒自身の弱点を動的に考慮させつつ両面から補完する」戦略へ読み進めるのが、本領域の知識蒸留フレームワークの理解を深めるための最短ルートとなります。
