# 次に読むべき論文 (Next to Read)

GrIPSは「勾配を用いず、LLMのアウトプット（API応答）のみを用いて離散的なプロンプトの編集操作を行う」という方向性を確立した研究です。この方向性（ブラックボックス最適化や進化計算への応用、プロンプトの自動最適化）を発展させている後続研究として、以下の論文を推奨します。

## 1. Automatic Prompt Optimization with "Gradient Descent" and Beam Search (2023)
- **著者**: Reid Pryzant, Dan Iter, Jerry Li et al.
- **URL**: [Semantic Scholar](https://www.semanticscholar.org/paper/c76dd4a70361c3afd2e19d046343e2dedd16ecc3)
- **選定理由**: GrIPSは編集操作（削除・置換など）をランダムに探査していましたが、本論文（通称 APO / ProTeGi）はLLM自体に「どうして間違えたのか（エラーの勾配）」をテキストで言語化させ、そのテキストレベルの勾配フィードバックを用いてプロンプトを洗練し、ビームサーチで探索空間を効率的に絞り込む手法を提案しています。ブラックボックス最適化の高度な発展形として必読です。

## 2. EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers (2023)
- **著者**: Qingyan Guo, Rui Wang, Junliang Guo et al.
- **URL**: [Semantic Scholar](https://www.semanticscholar.org/paper/a9c75cf664f675a1b4034b0256ec3c5168e293df)
- **選定理由**: GrIPSはヒューリスティックなフレーズ操作による探査を行いましたが、本論文は「進化計算（Evolutionary Algorithms, EA）」の枠組みとLLMを直接融合させています。初期プロンプト群を個体群と見なし、交差（Crossover）や突然変異（Mutation）をLLMを介して行うことで、ゼロからよりスケーラブルに最適化を行うアプローチです。

## 3. PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization (2023)
- **著者**: Xinyuan Wang, Chenxi Li, Zhen Wang et al.
- **URL**: [Semantic Scholar](https://www.semanticscholar.org/paper/1eb1a8c7f88de27af224153f43ecdd41774600f2)
- **選定理由**: 単なるフレーズの編集アプローチから脱却し、LLMを「プロンプトの設計エージェント」として見立てています。モンテカルロ木探索（MCTS）のような戦略的プランニング（Strategic Planning）を通じて、人間の専門家レベルで複雑なドメイン固有プロンプトを自律的に構成させるアプローチであり、逐次改善のエージェント化の潮流を理解する上で重要です。
