# 次に読むべき論文（Dota 2 with Large Scale Deep Reinforcement Learning; OpenAI Five）

被引用関係は `tools/verify_citations.py`（OpenAlex API の referenced_works / DOI 照合）により、**本論文（OpenAI Five）を実際に引用していることを確認済み（VERIFIED）** の論文のみを掲載する。

## 手法を発展させているもの

| 論文 | 年 | 確認方法 | 概要・読む理由 |
|---|---|---|---|
| A Closer Look at Invalid Action Masking in Policy Gradient Algorithms | 2022 | OpenAlex (VERIFIED) | OpenAI Five などの超大規模ゲームAIで不可欠とされる非合法行動マスキング（Invalid Action Masking）について、方策勾配アルゴリズムにおける理論的妥当性、勾配の偏り、学習安定性を体系的に解析・実証した研究。カードゲームの非合法手マスキングに直結。 |
| Outracing champion Gran Turismo drivers with deep reinforcement learning（Gran Turismo Sophy, Nature） | 2022 | OpenAlex (VERIFIED) | OpenAI Five と同様に、多次元の報酬シェイピングと大規模分散非同期PPOを用い、リアルタイム対人ゲームで人間の世界最高峰プレイヤーを打ち負かした直接的な発展研究。 |
| Champion-level drone racing using deep reinforcement learning（Swift, Nature） | 2023 | OpenAlex (VERIFIED) | 高速リアルタイム制御において、非同期シミュレータと大規模強化学習を組み合わせ、人間チャンピオンに勝利した研究。 |

## 違う角度からアプローチしているもの

| 論文 | 年 | 確認方法 | 概要・読む理由 |
|---|---|---|---|
| First return, then explore（Go-Explore, Nature） | 2021 | OpenAlex (VERIFIED) | 密な報酬シェイピングに頼らず、「過去の有望な状態へまず戻り、そこから探索する」アーカイブ機構によって、Montezuma's Revenge 等の極疎報酬ゲームを完全攻略した手法。報酬設計依存への強力な対抗解。 |
| Toward Causal Representation Learning（Schölkopf et al.） | 2021 | OpenAlex (VERIFIED) | 強化学習における状態・報酬の相関関係ではなく、介入や因果構造を表現学習に取り込むべきとする機械学習の基本方針を提唱した記念碑的論文。 |
| Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning | 2021 | OpenAlex (VERIFIED) | OpenAI Five のような数万CPUコアのクラスタではなく、数千のシミュレーション環境をGPU上で完結させて並列実行する次世代の超高速RLインフラ。 |
