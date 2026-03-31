# 次に読むべき論文 (Concurrent / Follow-up Work)

本論文（**ReAct: Synergizing Reasoning and Acting in Language Models**, Yao et al., 2022）の手法を発展させ、自律的なエージェントフレームワークや新たなアプローチを提案している後続の主要論文を列挙する。

1. **Reflexion: Language Agents with Verbal Reinforcement Learning**
   - **著者**: Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao (2023)
   - **関連性・新規性**: ReActは、外部情報を取得できるものの、自分自身が陥ったエラーや非効率な行動ループに対して「自己反省」し修正する機能を持っていなかった。Reflexionは、ReActベースのエージェントの上に「自己反省（Self-Reflection）」メカニズムを追加し、過去の失敗理由を言語的メッセージとして短期のエピソード記憶領域に保持して、次回以降の推論や行動軌跡を自律的に・逐次的に改善させるアプローチを導入した。

2. **Toolformer: Language Models Can Teach Themselves to Use Tools**
   - **著者**: Timo Schick et al. (2023)
   - **関連性・新規性**: ReActは外部ツール（Wikipedia等）の利用を少数のプロンプト（Few-shot In-Context Learning）に依存している。これに対し、Toolformerはモデル自らがAPI使用の好例を生成・フィルタリングし、それを自己教師あり学習としてファインチューニングに使用するアプローチである。これにより、モデルはいつ・どのように多様な外部ツールを呼び出すべきかをパラメータとして内面化し獲得している。

3. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**
   - **著者**: Shunyu Yao et al. (2023)
   - **関連性・新規性**: ReActの著者陣が提案したさらなる発展形。ReActやChain-of-Thoughtが「単線的（Chain）」な一巡の推論と行動を辿るのに対し、Tree of Thoughts（ToT）は思考プロセスを「木構造（Tree）」へと拡張した。複数の推論パスや仮説の選択肢（Branching）を生成し、自己評価によって不要なパスを刈り取る（Pruning）ことで、再帰的かつ探索的な複雑な問題対処を可能にしている。
