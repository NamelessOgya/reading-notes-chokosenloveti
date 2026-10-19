# 次に読むべき関係論文 (Potential-Based Shaping and Q-Value Initialization are Equivalent)

被引用（Cited by）論文は `tools/verify_citations.py --list-citing` で取得し、OpenAlex 上で **本論文を引用していることを確認できた論文** から選んだ（OpenAlex 上の被引用数は 167 件、2026年10月時点）。

## 手法を発展させているもの

### Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping (Hu et al., NeurIPS 2020)
- **概要・選定理由:**
  本論文が指摘した「不適切なポテンシャルは学習を遅くしうる」という問題に対し、シェーピング報酬の重みを状態ごとに自動で学習し、有害なシェーピングを抑える手法を提案している。人手で設計した中間報酬（カードアドバンテージなど）が本当に役立つか分からない場合の安全策として有用である。

### Potential-based shaping in model-based reinforcement learning (Asmuth, Littman, Zinkov, AAAI 2008)
- **概要・選定理由:**
  本論文の「シェーピング = 初期化」という見方を、R-max のようなモデルベース強化学習の探索に拡張し、ポテンシャルが許容的（admissible）であれば PAC-MDP の保証を保ったまま探索を減らせることを示している。シェーピングと探索効率の関係を理論的に深めている。

### Online learning of shaping rewards in reinforcement learning (Grześ & Kudenko, Neural Networks 2010)
- **概要・選定理由:**
  ポテンシャル関数を人手で与えるのではなく、学習中に抽象化した状態空間上の価値関数をオンライン学習してポテンシャルとして使う手法。Devlin & Kudenko (2012) の「動的ポテンシャル」につながる研究系譜の一つである。

### Potential-based difference rewards for multiagent reinforcement learning (Devlin, Yliniemi, Kudenko, Tumer, AAMAS 2014)
- **概要・選定理由:**
  マルチエージェント環境で、各エージェントの貢献を測る difference rewards と potential-based shaping を組み合わせている。対戦型カードゲームの自己対戦（複数エージェントが同時に学習する状況）でシェーピングを使う際の参考になる。

## 違う角度からアプローチしているもの

### RUDDER: Return Decomposition for Delayed Rewards (Arjona-Medina et al., NeurIPS 2019)
- **概要・選定理由:**
  人手でポテンシャルや初期値を設計する代わりに、最終報酬をLSTMで各ステップに再配分する。遅延報酬の問題に対し、「事前知識の注入」ではなく「信用割当の自動化」で取り組んでいる（本トピック配下で別途要約）。

### Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning (Parisotto, Ba, Salakhutdinov, ICLR 2016)
- **概要・選定理由:**
  専門家ネットワークから方策を蒸留して転移学習の初期値とする手法で、関連研究として本論文を引用している。「良い初期化」によって学習を加速するという点で本論文の結論と通じ、深層強化学習で教師モデルや人間の棋譜を初期化に使う方向の参考になる。
