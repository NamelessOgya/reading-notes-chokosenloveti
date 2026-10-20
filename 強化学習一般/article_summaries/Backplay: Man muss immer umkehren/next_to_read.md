# 次に読むべき論文（Backplay: "Man muss immer umkehren"）

被引用関係は `tools/verify_citations.py`（OpenAlex API の referenced_works / DOI 照合）により、**本論文（Backplay; arXiv:1807.06919）を実際に引用していることを確認済み（VERIFIED）** の論文のみを掲載する。

## 手法を発展させているもの

| 論文 | 年 | 確認方法 | 概要・読む理由 |
|---|---|---|---|
| Learning Montezuma's Revenge from a Single Demonstration (arXiv:1812.03381) | 2018 | OpenAlex (VERIFIED) | OpenAI による研究。Backplay と同様に単一の人間の実演軌道を用い、デモの終端から開始地点を徐々に遡りながらPPOで訓練する手法を、Atari最難関の「Montezuma's Revenge」に適用して世界最高記録を達成した直接の姉妹・発展研究。 |
| Go-Explore: a New Approach for Hard-Exploration Problems (Nature 2021) | 2021 | OpenAlex (VERIFIED) | Backplay の「有望な過去の状態から再開して探索する」思想をさらに一般化し、状態アーカイブから有望な状態を選んで環境をリセット（あるいは復元）し、そこから未踏領域を探索することで極スパース報酬を完全制覇した記念碑的論文。 |
| PBCS: Efficient Exploration and Exploitation Using a Synergy Between Reinforcement Learning and Motion Planning | 2020 | OpenAlex (VERIFIED) | モーションプランニングによって生成された軌道に沿ってカリキュラムを構築し、ロボットの長期間ホライゾン探索を加速する Backplay の直接的応用。 |

## 違う角度からアプローチしているもの

| 論文 | 年 | 確認方法 | 概要・読む理由 |
|---|---|---|---|
| Competitive Experience Replay | 2019 | OpenAlex (VERIFIED) | 単一の外部デモに頼るのではなく、自己対戦エージェント同士が互いに過去に達成した状態を挑戦課題として投げ合うことで、自動的に難易度カリキュラムを生成する手法。 |
| Lucid dreaming for experience replay: refreshing past states with the current policy | 2021 | OpenAlex (VERIFIED) | 経験再生バッファ内の過去の状態を現在の方策でリフレッシュし、反事実的シミュレーションと組み合わせて探索を効率化するアプローチ。 |
| Model-free reinforcement learning from expert demonstrations: a survey (2021) | 2021 | OpenAlex (VERIFIED) | 実演を利用した強化学習（RLfD）全般について、模倣学習（BC, GAIL）とカリキュラム型RL（Backplay等）の立ち位置を体系的に整理したサーベイ論文。 |
