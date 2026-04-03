# 次に読む論文リスト
今回の対象論文（AgentBreeder）は、マルチエージェント・スキャフォールドにおける「安全性」と「タスク性能」の多目的進化的最適化・セルフインプルーブメントを提案しています。発表直後（2025年2月）ですが、すでに本論文を引用している後続研究や、同期に類似テーマ（エージェントシステムのアライメント・脆弱性検証）を扱った重要な論文が存在します。これらの中から、次のステップとして読むべき論文を列挙します。

## 1. Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems
- **著者:** Sadia Asif, Mohammad Mohammadi Amiri (2026)
- **関連性:** AgentBreederはスキャフォールドの防御力を進化で高めるというアプローチでしたが、こちらの研究は直列的（Sequential）なマルチエージェントシステムにおいて生じる情報の秘匿性・プライバシーに焦点を当てています。エージェント間を流れる情報量を情報理論の観点から制御・制限する手法を提案しており、AgentBreederが取り組んだMultipolar（複数エージェント間）な環境での安全性に対して、より厳密な理論的保証からの防御策を展開しています。安全性メトリクスの別アプローチとして有用です。

## 2. OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety
- **著者:** S. Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou, Z. Wang, Nouha Dziri, Graham Neubig, M. Sap (2025)
- **関連性:** AgentBreederでは SaladData という既存の安全評価ベンチマークが用いられていましたが、実環境でのエージェントの安全性（攻撃的挙動など）を網羅的に評価するにはさらに広範な枠組みが必要です。この論文はマルチエージェントを含むAIエージェントの安全性を実世界の多様なレイヤーから評価するための包括的なフレームワークを提供しており、AgentBreederの最適化目標（$f_S$）をより実用的なものに拡張する際に必読の文献です。

## 3. Demonstrations of Integrity Attacks in Multi-Agent Systems
- **著者:** Can Zheng, Yuhan Cao, Xiaoning Dong, Tianxing He (2025)
- **関連性:** AgentBreederの「RedAgentBreeder」モードにおいて、敵対的攻撃への脆弱性がいかに高いスキャフォールドが簡単に見つかるかが示されました。本論文は、マルチエージェントシステムにおけるデータの完全性（Integrity）に対する攻撃を具体的に実証しています。単一の悪意あるエージェントや外部からの攻撃が、システム全体のスキャフォールドをどのようにより深く汚染するかという攻撃ベクトルが詳解されており、RedAgentBreeder側から見る脆弱性研究を深掘りするうえで最適です。

## 4. Opponent Shaping in LLM Agents
- **著者:** Marta Emili García Segura, Stephen Hailes, Mirco Musolesi (2025)
- **関連性:** AgentBreederは主にコードによる骨組み（スキャフォールド）側の構造を変えることで性能と安全性を確保していましたが、本論文はエージェントそのものが「他者（Opponent）」の振る舞いを予測・操作（Shaping）するというゲーム理論的なインタラクションに踏み込んでいます。自己改善進化のダイナミクスに、エージェント同士の心理的・戦略的な相互操作性がどう影響するかを分析する上で強力な示唆を与えます。

---
*※ 本リストの被引用論文は Semantic Scholar を用いて実際に取得されたデータを元に記述しています。引用文献の捏造（ハルシネーション）は含まれていません。*
