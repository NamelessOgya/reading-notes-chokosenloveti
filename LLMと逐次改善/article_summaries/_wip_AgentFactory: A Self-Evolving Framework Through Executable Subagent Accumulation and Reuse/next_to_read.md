# 次に読むべき関連論文 (Next to Read)

本論文（AgentFactory）は2026年3月に発表された極めて新しい論文（arXiv:2603.18000）であるため、**現時点で本論文を直接引用している後続研究（Cited by）はまだ存在しません**。

代替案として、本論文が影響を受けている先行研究・同時期に発表された関連論文（Concurrent Work）で、**「コードベースの自己進化（Code-based Self-evolution）」** や **「ツール・エージェント内部の継続的改善」** に焦点を当てている以下の文献を読むことを推奨します。

### 1. AlphaEvolve: A Code-based Self-evolution Framework for Scientific Discovery (Novikov et al., 2025)
- **概要**: AgentFactoryが言及している、科学的発見プロセスにおいてコードベースの自己進化を可能とするフレームワーク。テキストではなくソースコードを直接改変・進化させることで、複雑な科学的問題を解くエージェントシステムの有効性を示しています。コードの保存と改変による進化という共通のパラダイムを別ドメイン（科学分野）に応用した事例として読む価値があります。

### 2. Darwin Gödel Machine: Open-ended Recursive Self-improvement of Agent Internals (Zhang et al., 2025)
- **概要**: AgentFactoryと同様に、エージェントの内部構造（プログラム自体）のオープンエンドで再帰的な自己改善を探求した論文。エージェントが自らの「ソースコード」にアクセスし、より賢いエージェントへと自己進化するメカニズムについて論じています。エージェントのメタ推論能力と自己書き換え機能の全体設計を学ぶために最適な文献です。

### 3. Voyager: An Open-Ended Embodied Agent with Large Language Models (Wang et al., 2023)
- **概要**: Minecraftというオープンワールド環境において、LLMベースのエージェントが探索を通じて「実行可能なスキル（Python等のコードスニペット）」を継続的に作成・保存し、次々と新しいタスクをこなせるようになる手法を提案したエポックメイキングな論文。「実行可能なコードライブラリ」を蓄積し再利用するというAgentFactoryのCore Conceptの先駆けとなった重要な先行研究です。
