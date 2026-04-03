# 次に読むべき論文 (Next to read)

## 対象論文
*Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization* (arXiv:2412.03092)

## 被引用論文（Cited by）の状況
本論文は2024年12月にarXiv上に公開され、その後ICML 2025に採択されたばかりの最新の研究であるため、**現時点で本論文を直接的に引用・発展させている明確な後続研究（被引用論文）は確認できませんでした**。
※ したがって、本項目では代替として「本論文のベースライン・前提となった重要研究」および「同時期にLLMの最適化タスクなどで注目されている研究」を記載します。

## 代替提案：Textual Gradientと自己最適化の文脈で読むべき重要論文

### 1. 【ベースライン・前提知識】 TextGrad: Automatic "Differentiation" via Text
- **概要**: REVOLVEが直接的に拡張・改良した最大の前提研究。LLMによる自然言語フィードバックを数値グラフにおける「テキストの勾配」と見なし、文字列ベースでバックプロパゲーションに似たアプローチを用いプロンプトやコードを最適化する。REVOLVEは、本手法が依存する「一次情報のみでの更新」の弱点を克服するために開発されたため、この元論文とその挙動の違いを比較・理解することが極めて重要である。

### 2. 【自己最適化アーキテクチャ】 Reflexion: Language Agents with Verbal Reinforcement Learning
- **概要**: REVOLVEでもCode Optimizationタスクの比較対象になった代表的手法。LLMを用いた自律エージェントが、過去の失敗結果から言語的に「反省 (Reflection)」を行い、自身のプロンプトや方策を改善するフレームワーク。REVOLVEにおける「応答の歴史的推移（Trajectory・Response Evolution）を集める」という枠組みの思想的基盤としても関連が深い。

### 3. 【並行研究・同分野でのシステム構築】 DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines
- **概要**: REVOLVEと同じく複雑な推論タスクやソリューション生成に向けてプロンプトの構成やマルチステップAIシステムを自動的・構造的に最適化する。宣言的に定義されたLMパイプラインに対して最適化アルゴリズムを適応させるという点で、アーキテクチャ・モジュール設計側の側面として大きな進化を遂げており、併せて読むべき並行研究である。
