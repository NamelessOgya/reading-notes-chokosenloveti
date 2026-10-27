# 次に読むべき論文 (Next to Read)

本研究「Build, Don't Play (arXiv:2610.33845)」は、LLM研究エージェントがシミュレータとRLエージェントを自律的に構築し、Hearthstone Battlegroundsのライブラダーでトップ層に到達した研究です。「カードゲーム/オートバトラーAIの系譜」と「LLMによる研究自動化」の2つの観点から、以下の参考文献を読むことを推奨します。

### 1. Hearthstone Battleground: An AI Assistant with Monte Carlo Tree Search (Zolboot et al., 2022)
- **関連性 (同ドメインの先行研究):** Battlegroundsに対する数少ない先行AI研究。簡略化シミュレータ上のMCTSアシスタントで、記録された試合の序盤ターンのみで評価。本研究のTavernGym（全コンテンツ再現）・TavernAgent（フルゲームをライブでプレイ）がどこまで踏み込んだかを測る基準点になります。

### 2. The AI Scientist / The AI Scientist-v2 (Lu et al., 2024; Yamada et al., 2025)
- **関連性 (研究自動化の比較対象):** アイデア生成・実験・論文執筆を自動化する代表的なLLM研究エージェント。本研究は「自分のコードを書き換える」のではなく「教訓メモリと検証ゲートで研究プロセスを改善する」点、および「評価を実環境（ライブラダー）に置く」点で差別化しており、その違いを理解する上で必読です。

### 3. Eureka (Ma et al., 2024) / AlphaEvolve (Novikov et al., 2025)
- **関連性 (LLMが学習系を設計する):** LLMが報酬関数やプログラムを提案し自動評価器でスコアリングする枠組み。「LLMはプレイするより作るほうが上手い」という本研究の主張の前段にあたる研究群です。

### 4. Proximal Policy Optimization Algorithms (Schulman et al., 2017) および大規模ゲームRL（AlphaStar, OpenAI Five, Suphx, DouZero 等）
- **関連性 (学習器の基礎):** 本研究は学習器として標準的なPPO + Transformerを用い、工夫の重心を訓練世界の構築に置いています。自己対戦中心の大規模ゲームRL（特に多人数・不完全情報のSuphx/DouZero）と比較し、「なぜ本研究は自己対戦ではなく現実較正した相手ライブラリを選んだか」を考えると理解が深まります。

### 5. LLMのゲーム評価ベンチマーク（BALROG, TextArena, PokerBench 等）
- **関連性 (TavernBenchの位置付け):** LLMを直接ゲームプレイヤーとして評価するベンチマーク群。TavernBenchは「シミュレータで検証された正解」「強い専用エージェントという参照点」「リアルタイム制約」を加えた点が新しく、比較することで"Don't Play"側の主張の根拠が明確になります。

---

> [!NOTE]
> 本論文は2026年10月公開の新しい論文のため、被引用論文はまだ存在しません。上記は参考文献からの選定です。TavernGym / TavernBench が公開された後は、それらを用いた後続研究のフォローを推奨します。
