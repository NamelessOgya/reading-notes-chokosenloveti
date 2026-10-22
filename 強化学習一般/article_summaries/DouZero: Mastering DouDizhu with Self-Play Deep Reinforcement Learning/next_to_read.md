# 次に読むべき論文（DouZero: Mastering DouDizhu with Self-Play Deep Reinforcement Learning）

被引用関係は `tools/verify_citations.py`（OpenAlex API の referenced_works / DOI 照合）により、**本論文（DouZero; arXiv:2106.06135）を実際に引用していることを確認済み（VERIFIED）** の論文のみを掲載する。

## 手法を発展させているもの

| 論文 | 年 | 確認方法 | 概要・読む理由 |
|---|---|---|---|
| DouZero+: Improving DouDizhu AI by Opponent Modeling and Coach-guided Learning (IEEE CoG 2022) | 2022 | OpenAlex (VERIFIED) | DouZero の自己対戦フレームワークを基盤とし、相手モデル（Opponent Modeling）と完全情報コーチネットワーク（Coach-guided Learning）を導入することで、部分観測カードゲームにおける協力・敵対戦略の質を飛躍的に高めた直接的発展研究。 |
| DanZero: Mastering GuanDan Game with Reinforcement Learning (IEEE CoG 2023) | 2023 | OpenAlex (VERIFIED) | DouZero と同様の行動特徴表現と深層モンテカルロ（DMC）手法を、より複雑な4人協力カードゲーム「掼蛋（GuanDan）」へ拡張・適用した研究。複雑なカードゲームへの転用可能性を実証。 |
| MDou: Accelerating DouDiZhu Self-Play Learning Using Monte-Carlo Method With Minimum Split Pruning and a Single Q-Network (IEEE TG 2022) | 2022 | OpenAlex (VERIFIED) | DouZero の DMC をさらに高速化するため、最小分割枝刈り（Minimum Split Pruning）と単一Qネットワークアーキテクチャを提案し、計算効率と学習速度を改善した研究。 |

## 違う角度からアプローチしているもの

| 論文 | 年 | 確認方法 | 概要・読む理由 |
|---|---|---|---|
| RARSMSDou: Master the Game of DouDiZhu With Deep Reinforcement Learning Algorithms (IEEE TETCI 2023) | 2023 | OpenAlex (VERIFIED) | モンテカルロ価値推定（DMC）に頼る DouZero に対し、TD学習（Q学習）や状態抽象化、モデルベースの探索手法を組み合わせて不完全情報ゲームの局所的な戦況制御を試みた研究。 |
| Modeling Strong and Human-Like Gameplay with KL-Regularized Search (piKL; arXiv:2112.07544) | 2021 | OpenAlex (VERIFIED) | カードゲーム等の不完全情報・多人数ゲームにおいて、自己対戦RLが陥りがちな非人間的・極端な方策を防ぎ、人間の事前方策（Anchor Policy）へのKL正則化を組み込んだ探索を行う手法。序盤の不合理なカード浪費抑制に極めて示唆的。 |
