# 次に読むべき論文 (Next to Read)

※本論文「Continual Low-Rank Adapters for LLM-based Generative Recommender Systems (PESO)」はICLR 2026会議への投稿（またはごく最近発表された論文）であるため、現時点で本作を直接引用している（Cited by）後続研究は確認できませんでした。そのため、当研究と同分野における最新の関連研究（Concurrent Work）などで、レコメンド分野における継続学習・LLM適応手法を扱う後続・関連論文を以下に列挙します。

1. **PISA: A Prototypical Interest-based Setup for Continual Recommendation** (Yoo et al., 2025)
   - 本論文の著者でもあるHyunsik Yooらの同時期の関連研究。従来型の二つのタワーモデルを用いた継続的レコメンドにおいて、ユーザーのプロトタイプ的な関心を維持・更新するアプローチを提案しており、LLMを用いない従来型アプローチのSOTAベースラインとして本論文内でも比較されています（Table 12参照）。

2. **ReMix: A Representation Mixture of Experts for Continual Recommendation** (Qiu et al., 2026)
   - 本論文の導入部でも継続学習におけるLoRAベースの最新手法の文脈で言及されている論文。LLMなどの表現学習において、時間経過とともに変化するユーザー行動を混合エキスパート（MoE）で継続的に捉えるアプローチを提案しており、PESOと同時に比較・考察すべき研究です。

3. **Subspace Continual Learning for Recommendation** (Zeng et al., 2026)
   - 継続的なレコメンドにおいて、破滅的忘却を防ぎつつユーザーの趣向の変化を学習するためのサブスペース最適化手法を提案した研究（本論文内で言及）。PESOが提案する「方向性に基づいたLoRA空間のデータアウェアなガイダンス（Direction-wise, Data-aware guidance）」との理論的な近似点や差異を検証する上で、次に読むべき論文です。
