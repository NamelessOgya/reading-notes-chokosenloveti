# 次に読むべき論文

ReLLa 論文（"ReLLa: Retrieval-enhanced Large Language Models for Lifelong Sequential Behavior Comprehension in Recommendation"）は、LLM の推薦システム適用における長期コンテキスト処理の限界（異質性ノイズ）と、検索による解決策を明らかにしました。
このアプローチをさらに発展させている手法、あるいは異なる角度からアプローチしている後続の被引用論文として、以下の3本を推奨します。

---

## 1. ReLLaX (Full-Stack Optimized Large Language Models for Lifelong Sequential Behavior Comprehension in Recommendation)
- **arXiv ID**: [2501.13344](https://arxiv.org/abs/2501.13344)
- **発表時期**: 2025年1月 (arXiv)
- **著者**: Rong Shan, Jiachen Zhu, Jianghao Lin, Chenxu Zhu, Bo Chen, Ruiming Tang, Yong Yu, Weinan Zhang (ReLLa とほぼ同一の著者陣によるフォローアップ研究)
- **選定理由（手法の直接的発展）**:
  ReLLa の「生涯シーケンシャル行動不理解問題」を解決するために、**データ、プロンプト、パラメータの3つのレベルすべてでフルスタックの最適化を行う ReLLaX (Retrieval-enhanced Large Language models Plus) フレームワーク**を提案しています。
  - **データレベル**: ReLLa の SUBR を踏襲しつつ、行動系列の異質性を効果的に抑制。
  - **プロンプトレベル**: **SPA (Soft Prompt Augmentation)** を導入し、推薦に適した協調フィルタリング知識をプロンプト内に注入してアイテム間の関係性を捉えやすくします。
  - **パラメータレベル**: **CFLoRA (Component Fully-interactive LoRA)** を新たに提案。従来の LoRA よりも表現力が高く、コンポーネント間の動的相互作用を捉えられます。
  ReLLa からの直系進化であり、現在の最新のパフォーマンス到達点を確認するために最初に読むべき論文です。

---

## 2. KAR (Towards Open-World Recommendation with Knowledge Augmentation from Large Language Models)
- **arXiv ID**: [2306.10933](https://arxiv.org/abs/2306.10933)
- **発表時期**: 2023年6月 (arXiv), 2024年発表
- **著者**: Yichao Xi, Liang Chen, Feiran Huang, et al.
- **選定理由（知識拡張によるアプローチ・別角度からの展開）**:
  ReLLa がユーザー行動シーケンスのテキスト記述（入力データ側）の調整に注力したのに対し、この論文は **LLM が持つオープンワールド知識（事実知識およびユーザー嗜好に関する推論知識）を推薦モデルへ補強・蒸留する KAR フレームワーク**を提案しています。
  - LLM から「ユーザーの潜在的好みの推論（Factorization Prompting）」を生成。
  - 生成された知識をハイブリッドエキスパートアダプターを用いて既存推薦モデルの埋め込み空間に適応。
  - LLM の高い推論レイテンシを緩和するために「事前ストレージ（Pre-storage）機構」を導入し、効率的な推論を実現。
  データ効率と推論速度のトレードオフを乗り越えるための実用的なアプローチとして、非常に参考になります。

---

## 3. LLM-CF (Large Language Models Enhanced Collaborative Filtering)
- **arXiv ID**: [2403.17688](https://arxiv.org/abs/2403.17688)
- **発表時期**: 2024年3月 (arXiv), CIKM 2024
- **著者**: Ruobing Xie, Shaoliang Zhang, Rui Wang, et al.
- **選定理由（協調シグナルとLLMの融合・効率性の改善）**:
  LLM が協調シグナル（ユーザー間・アイテム間の直接の類似関係）を捉えるのが苦手であるという課題に着目し、**LLM の持つ世界知識と推論能力を協調フィルタリング (CF) に蒸留する LLM-CF フレームワーク**を提案しています。
  - In-Context Learning および Chain-of-Thought (CoT) 推論を利用して協調シグナルを補正。
  - **LLM の推論処理を完全にオフライン化**し、実行時は軽量な推薦モデルのみをオンラインで使用することで、ReLLa が課題として残した「推論時間（レイテンシ）」の問題を根本的に解決しています。
  LLM を推薦の「性能向上」に使いつつ、システムの「実用性・効率性」を維持するための設計として深く関連する研究です。
