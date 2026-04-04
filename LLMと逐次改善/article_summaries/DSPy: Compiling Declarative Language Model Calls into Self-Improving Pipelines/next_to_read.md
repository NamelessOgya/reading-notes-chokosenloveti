# 次に読むべき関係論文 (Next to Read)

DSPy（Declarative Language Model Calls into Self-Improving Pipelines）の発表以降、テキスト最適化手法や「プロンプトエンジニアリングの抽象化・宣言化」に関する研究が大きく進展しました。本論文の思想「文字列ベースのプロンプトから反復可能なプログラムやグラフを通じた最適化」を**さらに発展させているアプローチ**や、**異なる角度（比較、文脈管理、実行環境）**からアプローチしている後続論文（Cited by）を抽出しました。

---

## 1. Feedback Descent: Open-Ended Text Optimization via Pairwise Comparison (2025)
- **著者:** Yoonho Lee, Joseph Boen, Chelsea Finn
- **URL:** [Semantic Scholar](https://www.semanticscholar.org/paper/39cc224ee611de761a132fe04987350d6d642a4a)
- **関連性 (別角度からのアプローチ):** 
  DSPyは主に少数のデモや数理的メトリクス（Exact Matchなど）を用いて最適化を行いますが、こちらはテキストの最適化を「ペアワイズの比較による評価」を活用することで、記述的かつオープンエンドなプロンプト最適化（Feedback Descent）を模索する研究です。勾配を使用しないテキスト最適化（TextGradなど）のアプローチと関連性が深く、定性的な性能をより高める手法として対比して読む価値があります。

## 2. From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents (2026)
- **著者:** Ling Yue, Kushal Raj Bhandari, Ching-Yun Ko et al.
- **URL:** [Semantic Scholar](https://www.semanticscholar.org/paper/42323cb9aa8536bed0dc910ffdf51dedb9ea9f59)
- **関連性 (発展・サーベイ):** 
  DSPyが提唱した「静的テンプレートから動的な演算子（モジュールパイプライン）への移行」という概念が、さらに最新のLLMエージェントシステムにおいてどのように発展し、最適化されているかをまとめたサーベイ論文です。DSPyのみならず他の最新フレームワークにおける全体像やトレンド（Graph型のワークフロー最適化）を一覧で把握できます。

## 3. Structured Prompt Language: Declarative Context Management for LLMs (2026)
- **著者:** Wensheng Gong
- **URL:** [Semantic Scholar](https://www.semanticscholar.org/paper/ded6703fad502d61711c48a73ddd00001af8722d)
- **関連性 (手法の深化):**
  DSPyがもたらした「宣言的（Declarative）なシグネチャによる処理の隠蔽と抽象化」の概念に着目し、これをさらに文脈（Context）管理を含めた「言語レベル」で構造化し直したフレームワークについての論文です。複雑なパイプライン管理において、DSPy的なプログラミングモデルをどのように統合すべきかを探る設計思想の参考になります。

## 4. MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks (2026)
- **著者:** Zhiqing Hong, Qian Zhang, Jiahang Sun et al.
- **URL:** [Semantic Scholar](https://www.semanticscholar.org/paper/0613b7ad7302f722f5d4c25fbb5ebe146b78c5d4)
- **関連性 (発展的アプローチ):**
  DSPyの「Teleprompter機能（探索・Bootstrapping・アンサンブルなど）」によるプロンプトの自律的最適化を更に拡張し、マルチエージェント構造におけるプロンプトの最適化問題を「GNN（Graph Neural Networks）」と「バンディットアルゴリズム」を組み合わせて効率化する発展研究です。マルチエージェント特有の相互作用に適応するための手段として非常に興味深い内容です。
