# 次に読むべき論文 (Next to Read)

本論文（A Critical Study on Data Leakage in Recommender System Offline Evaluation）の課題設定を引き継ぎ、特定ドメインや新しい評価スキームへ発展させている後続研究を以下に挙げる。

## 1. Don't Get Ahead of Yourself: A Critical Study on Data Leakage in Offline Evaluation of Sequential Recommenders (2025)
- **概要**: 本論文が提起した「データリーク」の問題意識を、特に逐次推薦（Sequential Recommender Systems, SRS）の文脈に拡張して詳細に検証した後続研究。逐次モデルにおいて、未来のデータが学習時に混入することで推薦性能にどのような影響を与えるか、またそれを防ぐための厳密な評価設計について論じている。
- **選定理由**: 本論文の手法・問題提起を直接的に発展させ、近年主流となっている系列レコメンドモデルに焦点を当てているため、次に読む論文として非常に適している。

## 2. 実践的なTimeline Schemeやインクリメンタル（オンライン）予測への移行に関する研究群
- **概要**: 本論文が提唱した「Timeline Scheme」を実用化・標準化するために、単純な Leave-one-out ではなく、完全に時間を基準に分割する「Split-by-timepoint leave-one-out」など、新たなデータ分割戦略やベンチマーク環境の構築を目指す研究や、オンライン予測問題へと再定義する研究が含まれる。
- **選定理由**: データリーク問題を完全に回避しつつ、モデルの性能を正当かつ比較可能に保つための標準的な評価フレームワークがどのように実装されているかを学ぶことができるため。
