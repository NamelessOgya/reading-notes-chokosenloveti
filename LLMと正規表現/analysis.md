# LLMと正規表現 論文調査まとめ

本ドキュメントでは、LLMと正規表現に関連する技術（制約付きデコード・正規表現生成・LLM特徴量解釈）に関する調査要約をまとめています。

---

## 調査済み論文の総合比較

各論文の発表年、テーマ分類、および提案手法の概要を以下の表に示します。

### 1. 論文概要および手法の比較
| 論文略称 | 発表年 | 発表会議 | テーマ分類 | 提案手法の概要 |
| :--- | :---: | :---: | :---: | :--- |
| **Willard (2023)** | 2023年 | arXiv | 制約付きデコード | **Outlines**を提案。LLMの生成を有限状態機械（FSM）のトラバーサルに変換し、正規表現・文法に対応するトークンのマスクを $O(1)$ で引けるインデックスを事前計算。 |
| **Ugare (2024a)** | 2024年 | arXiv (EMNLP) | 制約付きデコード | **SynCode**を提案。文脈自由文法（CFG）に対してDFAマスクストアをオフライン構築し、デコード中に文法的に有効なトークンのみを許可。Pythonコード生成のシンタックスエラーを **96%削減**。 |
| **Dong (2024)** | 2024年 | ICML '24 | 制約付きデコード | **DOMINO**を提案。サブワードトークナイザと制約の境界不整合（Token Misalignment）問題を解決するため、ボキャブラリー整合型サブターミナルツリーをオフライン構築し、投機的デコードと組み合わせ最大 **2倍の高速化**。 |
| **Dong (2024b)** | 2024年 | NeurIPS '24 | 制約付きデコード | **XGrammar**を提案。コンテキスト独立トークンの事前チェックとコンテキスト依存トークンの実行時インタープリタによりオーバーヘッドを排除。vLLM等に統合済みで従来比 **最大100倍の高速化**。 |
| **Park (2024)** | 2024年 | NeurIPS '24 | 制約付きデコード 品質 | **GAD / ASAp**を提案。従来の文法制約デコード（GCD）が生成分布を歪める問題を指摘し、文法整合サンプリング（Grammar-Aligned Decoding）と近似期待将来文法性を用いた再重み付けで品質を改善。 |
| **Banerjee (2025)** | 2025年 | ICML '25 | 制約付きデコード 推論 | **CRANE**を提案。文法制約が強すぎるとLLMの計算表現クラスが $TC^0$ に制限され推論能力が劣化することを理論的に示し、推論フェーズは非制約・出力フェーズは制約付きに切り替える文法拡張デコードを提案。数学・論理推論で **最大10ポイント改善**。 |
| **Zhang (2023)** | 2023年 | ASE '23 | 正規表現生成 | **InfeRE**を提案。正規表現生成を連鎖推論（Chain of Inference）に分解し、ステップごとに推論するパラダイムと自己一貫性デコードにより、NL2REタスクの DFA@5 精度を従来比大幅改善。 |
| **Boggust (2025)** | 2025年 | ICLR '26 | LLM解釈可能性 | **Semantic Regexes**を提案。スパースオートエンコーダ（SAE）で得られたLLM特徴量を記述する構造化言語として、プリミティブと修飾子からなる意味的正規表現を定義。自然言語と同等精度で一貫性・定量化が可能。 |
| **Scholak (2021)** | 2021年 | EMNLP '21 | 制約付きデコード | **PICARD**を提案。LLMのSQL生成において、生成中のトークンをインクリメンタルにSQLパーサで検証し、無効な中間表現を即座にビームから除外することで、Spider SQLベンチマークで **最高精度（SOTA）** を達成。 |
| **Poesia (2022)** | 2022年 | ICML '22 | 制約付きデコード 合成 | **Synchromesh**を提案。タスク固有のプログラム合成のため、Completion Engine（正規表現・CFGベースの補完エンジン）を用いてLLMの出力をターゲット言語の有効な候補のみに制限し、Few-shot学習を大幅に強化。 |

---

## テーマ別の分類（星取表）

各論文が取り組む技術的課題の整理を星取表形式で示します。

| 論文略称（発表年） | FSM/DFA制約デコード | CFG/PDA制約デコード | 高速化・オーバーヘッド削減 | 確率歪み問題 | 推論能力との両立 | 正規表現生成 | LLM特徴量解釈 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Willard (2023)** | ★ | ★ | ★ | | | | |
| **Ugare (2024a)** | ★ | ★ | ★ | | | | |
| **Dong (2024)** | ★ | ★ | ★ | ★ | | | |
| **Dong (2024b)** | ★ | ★ | ★ | | | | |
| **Park (2024)** | ★ | ★ | | ★ | | | |
| **Banerjee (2025)** | ★ | ★ | | | ★ | | |
| **Zhang (2023)** | | | | | | ★ | |
| **Boggust (2025)** | | | | | | ★ | ★ |
| **Scholak (2021)** | | ★ | | | | | |
| **Poesia (2022)** | ★ | ★ | | | | ★ | |

* **★**: 主要な研究対象

---

## 調査済み論文一覧

各論文のより詳細な要約ドキュメントへのリンクと要約です。

### 1. [Efficient Guided Generation for Large Language Models](./article_summaries/Efficient%20Guided%20Generation%20for%20Large%20Language%20Models/summary.md)
* **著者**: Brandon T. Willard, Rémi Louf (outlines-dev)
* **発表会議**: arXiv:2307.09702 (2023年)
* **概要**: 
  LLMの出力をテキスト生成の各ステップで有限状態機械（FSM）を用いて制約する手法を提案した研究。
  正規表現や文脈自由文法に合致するトークンを決定する問題をFSMのトラバーサルとして定式化し、モデルの語彙に対する事前インデックスを構築することで、各ステップのマスク計算を $O(N)$ から $O(1)$ に削減する効率的なアルゴリズムを提案。
  この手法は「Outlines」ライブラリとして実装・公開され、vLLMやHugging Faceと統合されたことで、制約付きデコードの事実上の標準手法となった。

### 2. [SynCode: LLM Generation with Grammar Augmentation](./article_summaries/SynCode:%20LLM%20Generation%20with%20Grammar%20Augmentation/summary.md)
* **著者**: Shubham Ugare, Tarun Suresh, Hangoo Kang, Sasa Misailovic, Gagandeep Singh (UIUC)
* **発表会議**: arXiv:2403.01632 (2024年, EMNLP 2024)
* **概要**: 
  文脈自由文法（CFG）を用いてLLMのコード生成に文法拡張を施すフレームワーク「SynCode」を提案した研究。
  CFGに対応するDFAマスクストアをオフラインで構築し、デコード中に現在の文法状態から有効なトークンセットを高速に参照する仕組みを実現。健全性（有効な出力のみ生成）と完全性（すべての有効な出力を生成可能）を両立しつつ、最低10%程度の生成オーバーヘッドでPythonコード生成のシンタックスエラーを **96.07%削減**した。

### 3. [Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation](./article_summaries/Guiding%20LLMs%20The%20Right%20Way:%20Fast%2C%20Non-Invasive%20Constrained%20Generation/summary.md)
* **著者**: Luca Beurer-Kellner, Marc Fischer, Martin Vechev (ETH Zürich)
* **発表会議**: ICML 2024
* **概要**: 
  トークナイザとフォーマル文法の境界不整合（Token Misalignment）問題を解決した制約付きデコード手法「DOMINO」を提案した研究。
  従来の素朴なマスキングはサブワードトークンの境界と正規表現・CFGの境界がずれるため精度低下を招くが、本研究はボキャブラリー整合型サブターミナルツリーをオフラインで構築し、推論時の検証を高速化。投機的デコードと組み合わせることで制約なし生成比で最大 **2倍のスループット向上** を達成した。

### 4. [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](./article_summaries/XGrammar:%20Flexible%20and%20Efficient%20Structured%20Generation%20Engine%20for%20Large%20Language%20Models/summary.md)
* **著者**: Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, Tianqi Chen (CMU / MLC)
* **発表会議**: arXiv:2411.15100 (2024年)
* **概要**: 
  LLM向け文法制約付き生成エンジン「XGrammar」を提案した研究。
  語彙をコンテキスト独立トークン（事前チェック可能）とコンテキスト依存トークン（実行時インタープリタ）に分割し、永続スタックとオートマトン最適化（インライン化・等価状態統合）により推論エンジンとのGPU計算オーバーラップを実現。従来の文法制約手法と比較して最大 **100倍の高速化** を達成し、vLLM・SGLang・TensorRT-LLM・MLC-LLMに採用された。

### 5. [Grammar-Aligned Decoding](./article_summaries/Grammar-Aligned%20Decoding/summary.md)
* **著者**: Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni (UC San Diego)
* **発表会議**: NeurIPS 2024
* **概要**: 
  従来の文法制約デコード（GCD）が生成確率分布を歪める「確率歪み問題」を定式化し、文法整合サンプリング（Grammar-Aligned Decoding: GAD）という新概念を提案した研究。
  GCDは将来の文法適合性を考慮せずトークンをマスクするため、文法的には正しいが元のLLM分布から乖離した出力が生成される問題を指摘。提案する**ASAp**（Adaptive Sampling with Approximate Expected Futures）アルゴリズムは過去のサンプル出力を利用してプレフィックスの将来文法適合性を近似し、確率歪みを大幅に軽減するサンプリングを実現した。

### 6. [CRANE: Reasoning with Constrained LLM Generation](./article_summaries/CRANE:%20Reasoning%20with%20Constrained%20LLM%20Generation/summary.md)
* **著者**: Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh (UIUC)
* **発表会議**: ICML 2025 (arXiv:2502.09061)
* **概要**: 
  文法制約の厳しさがLLMの推論能力を理論的に劣化させることを示し、推論と構造制約を両立するデコードアルゴリズム「CRANE」を提案した研究。
  厳密な文法制約はLLMの表現クラスを $TC^0$ に制限し連鎖推論（CoT）の恩恵を失わせることを理論的に証明。追加規則による文法拡張（Grammar Augmentation）で推論フェーズを非制約にしつつ最終出力フェーズを制約付きにするアプローチにより、数学推論（GSM-Symbolic）や論理推論（FOLIO）ベンチマークで最大 **10ポイント精度改善** を達成した。

### 7. [InfeRE: Step-by-Step Regex Generation via Chain of Inference](./article_summaries/InfeRE:%20Step-by-Step%20Regex%20Generation%20via%20Chain%20of%20Inference/summary.md)
* **著者**: Shuai Zhang, Xiaodong Gu, Yuting Chen, Beijun Shen (上海交通大学)
* **発表会議**: ASE 2023 (arXiv:2308.04041)
* **概要**: 
  自然言語記述からの正規表現生成（NL2RE）タスクを、一括生成ではなく「連鎖推論（Chain of Inference）」に分解する新パラダイム「InfeRE」を提案した研究。
  正規表現の各部分を段階的なサブ推論ステップとして生成することで、テキストマッチングの論理構造に沿った解釈可能な生成を実現。自己一貫性デコード（Self-Consistency Decoding）により複数モデルのアンサンブルを行い、NL-RX-TurkおよびKB13データセットにおいて DFA@5 精度で先行研究（TRANXなど）を大幅に上回った。

### 8. [Semantic Regexes: Auto-Interpreting LLM Features with a Structured Language](./article_summaries/Semantic%20Regexes:%20Auto-Interpreting%20LLM%20Features%20with%20a%20Structured%20Language/summary.md)
* **著者**: Angie Boggust, Donghao Ren, Yannick Assogba, Dominik Moritz, Arvind Satyanarayan, Fred Hohman (Apple / CMU / MIT)
* **発表会議**: ICLR 2026 (arXiv:2510.06378)
* **概要**: 
  スパースオートエンコーダ（SAE）を用いて得られたLLMの内部特徴量を説明するための構造化言語「Semantic Regexes（意味的正規表現）」を提案した研究。
  従来の自動解釈手法が自然言語による曖昧な説明を生成する問題に対し、言語・意味パターンを捉えるプリミティブと文脈化・量化などの修飾子からなる形式的な記述体系を設計。自然言語と同等精度を保ちつつ一貫性と定量化を可能にし、ユーザスタディによりLLM特徴量のメンタルモデル構築を改善することを実証した。

### 9. [PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models](./article_summaries/PICARD:%20Parsing%20Incrementally%20for%20Constrained%20Auto-Regressive%20Decoding%20from%20Language%20Models/summary.md)
* **著者**: Torsten Scholak, Nathan Schucher, Dzmitry Bahdanau (ServiceNow Research)
* **発表会議**: EMNLP 2021
* **概要**: 
  LLMによるSQL生成において、デコード中に逐次的なSQLパーサ検証を組み込む制約付き自己回帰デコード手法「PICARD」を提案した研究。
  ビームサーチの各候補トークンを即時にパーサで評価し、構文的・意味的に無効なプレフィックスをリアルタイムに除外する。追加の学習なしにSpiderベンチマークで **SOTA精度（T5-3BでEM 69.7%、T5-11BでEM 75.5%）** を達成し、Text-to-SQLにおけるLLMの信頼性を大幅に向上させた。

### 10. [Synchromesh: Reliable Code Generation from Pre-Trained Language Models](./article_summaries/Synchromesh:%20Reliable%20Code%20Generation%20from%20Pre-Trained%20Language%20Models/summary.md)
* **著者**: Gabriel Poesia, Oleksandr Polozov, Vu Le, Ashish Tiwari, Gustavo Soares, Christopher Meek, Sumit Gulwani (Microsoft Research)
* **発表会議**: ICLR 2022 (arXiv:2201.11903)
* **概要**: 
  タスク固有のプログラム合成に特化した制約付きデコードフレームワーク「Synchromesh」を提案した研究。
  正規表現・CFGをベースにした「Completion Engine（補完エンジン）」により、LLMが生成できる候補を各ステップでターゲット言語の構文的に有効なトークンのみに制限する。ドメイン固有言語（DSL）向けのFew-shot学習の性能を大幅に強化し、事前学習済みLM（GPT-3等）の汎化性能を正規表現制約によって構造的に保証する手法を確立した。
