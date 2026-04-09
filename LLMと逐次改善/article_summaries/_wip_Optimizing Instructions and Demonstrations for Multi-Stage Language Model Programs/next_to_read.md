# Next to Read: Concurrent and Subsequent Work

本研究「Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs (MIPRO)」を発展させ、あるいは異なる角度からアプローチしている後続論文や関連の最新研究を以下に列挙します。本研究は2024年に発表されて以降、LLMエージェントおよびDSPyを用いたモジュールパイプライン最適化の基盤として広く参照されています。

## MIPROの拡張およびDSPyに関連する後続研究 (2025年以降)

1. **Benchmarking LLM Optimization Strategies for Clinical NER: A Comparative Analysis of DSPy GEPA Against Domain-Specific Transformers (2025)**
   - *関連・発展性*: MIPROを含むDSPyの最適化機能を活用し、医療（Clinical NER）などの特定の高難度ドメインにおいて既存のタスク特化モデルと比較・検証している論文。どのようにモジュール最適化がドメイン適応に恩恵をもたらすかを探求しています。

2. **GAAPO: genetic algorithmic applied to prompt optimization (2025)**
   - *関連・発展性*: MIPROの発展形やEvoPrompt等に近いベクトルとして、プロンプトの最適化を遺伝的アルゴリズム（GA）にて拡張させている論文。最適化手法としてBayesian Surrogateの代わりにGAを適用した場合の探索性能の比較として関連します。

3. **CoolPrompt: Automatic Prompt Optimization Framework for Large Language Models (2025)**
   - *関連・発展性*: 大規模言語モデルの自動プロンプト最適化における新たなフレームワーク。MIPROと同様に評価ラベルが少ない状況での最適な指示とコンテキストを効率的に発見する手法を探求しており、MIPROとのフレームワーク設計（プロポーザルとクレジット割り当て）の比較として有用です。

4. **Cognify: Supercharging Gen-AI Workflows With Hierarchical Autotuning (2025)**
   - *関連・発展性*: 生成AIを用いたワークフロー（Multi-Stage LM Programと類似するパイプライン）に対する階層的な自動チューニングを提案している研究。MIPROが行うモジュールごとのクレジット割り当てアプローチと比較し、より上位の構造（ワークフローシステム階層）にスケールさせる次世代のアプローチとして次に読む価値が高いです。
