# SimAug 後続・関連論文リスト

## 被引用論文（Cited by）

Semantic Scholar 調査（2026年6月時点）により、SimAug（arXiv:2505.01695）を引用している論文が **2件** 確認された。

### 1. Catalog-Native LLM: Speaking Item-ID Dialect with Less Entanglement for Recommendation
- **arXiv**: 2510.05125
- **発表**: ICLR 2026
- **著者**: Reza Shirkavand, Xiaokai Wei, Chen Wang, Zheng Hui, Heng Huang, Michelle Gong
- **リンク**: https://arxiv.org/abs/2510.05125
- **概要**: 協調フィルタリングのアイテムIDとLLMの自然言語を統合するための IDIOMoE（Item-ID + Oral-language Mixture-of-Experts LM）アーキテクチャを提案。アイテムインタラクション履歴をLLMの言語空間内の「方言（dialect）」として扱い、テキストトークンとアイテムIDトークンを別々のエキスパートにルーティングすることで、テキスト理解能力を保ちながら高精度な推薦を実現する。SimAugのテキスト埋め込み活用という方向性を受け継ぎつつ、より深いLLMとIDの統合を志向した発展的研究。

### 2. DrugLM: A Unified Framework to Enhance Drug-Target Interaction Predictions by Incorporating Textual Embeddings via Language Models
- **DOI**: 10.1101/2025.07.09.657250
- **年**: 2025
- **著者**: Tianyi Li, Zhengyu Fang, Xiaoge Zhang, Kaiyu Tang, Huiyuan Chen, Zhimeng Jiang, Tianxiang Zhao, et al.
- **概要**: SimAugと共著者を同じくするHuiyuan Chenが参加した研究。SimAugの「PLMのテキスト埋め込みをグラフの相互作用拡張に活用する」アプローチを、薬物-標的相互作用（Drug-Target Interaction）予測タスクに転用。レコメンドドメインでの成功を別ドメインに展開した応用研究。

---

## 関連論文（Concurrent Work / 同時期の関連研究）

SimAugと同時期（2024〜2025年）に発表された、同じ課題（LLMを用いたデータ拡張・推薦の公平性・疎性改善）に取り組む関連研究を以下に列挙する。

### ① LLMベースのデータ拡張でレコメンドを改善するアプローチ

#### LLMSeR: Enhancing Sequential Recommendation via LLM-based Data Augmentation
- **arXiv**: 2503.12547
- **年**: 2025年3月
- **著者**: （Sequential Recommendation研究グループ）
- **リンク**: https://arxiv.org/abs/2503.12547
- **SimAugとの違い**: SimAugはシンプルなテキスト類似度ベースの拡張のみを行うのに対し、本論文は3つのモジュール（Semantic Interaction Enhancer・Adaptive Reliability Verification・Dual-Channel Training）を組み合わせた複雑なフレームワーク。LLMの幻覚（hallucination）を抑制する仕組みを内蔵しているのが特徴。逐次推薦（Sequential Recommendation）への特化という点でSimAugとは異なるアプローチ。
- **推薦理由**: SimAugがシンプルさを重視する一方、精度や信頼性をより高めた複雑なフレームワークを比較する上で有益。

#### Beyond Single Labels: Improving Conversational Recommendation through LLM-Powered Data Augmentation
- **arXiv**: 2508.05657
- **年**: 2025年（ACL 2025）
- **DOI**: 10.18653/v1/2025.acl-long.758
- **推薦理由**: 会話型推薦（Conversational RS）へのLLMデータ拡張の応用。マルチラベルデータ拡張という角度からの別アプローチであり、SimAugの「インタラクション拡張」とは異なるラベル拡張戦略を採る。

### ② 公平性改善へのLLMデータ拡張アプローチ

#### Can LLMs Enhance Fairness in Recommendation Systems? A Data Augmentation Approach
- **会議**: SIGIR 2025
- **著者**: Hanzhe Li, Dazhong Shen, Chao Wang, Yuting Liu, Jingjing Gu
- **SimAugとの違い**: SimAugがPLMのテキスト類似度を使い非人気アイテムへのインタラクションを増やすことで公平性を間接的に向上させるのに対し、本論文はユーザ個人の「公平性度合い（personalized fairness degrees）」をプロンプトに明示してLLMに公平なインタラクションデータを直接生成させる。公平性を明示的に目標として設定している点が異なる。
- **推薦理由**: SimAugと同じ公平性向上を目的とするが、LLMへのアプローチが対照的（類似度ベース vs. プロンプトベース）。比較対象として必読。

#### Improving user-oriented fairness in recommendation via data augmentation: Don't worry about inactive users
- **誌**: Journal of Systems and Software (2025, Vol.225, 112387)
- **著者**: Yong Wang, Huadong Zhou, Gui-Fu Lu, Cuiyun Gao, Shuai Meng
- **SimAugとの違い**: SimAugと同様に非アクティブユーザへのデータ拡張で公平性を改善するアプローチを採るが、LLMの使用ではなく合成インタラクション生成による手法を用いる。SimAugのLLMなしバージョンと比較できる立ち位置。
- **推薦理由**: SimAugの「非アクティブユーザ向け拡張」というコア概念を共有しながら、LLMを使わない手法との比較という観点で参照価値が高い。

### ③ LLMによるデータ拡張の課題（バイアス問題）

#### Understanding and Mitigating Bias Inheritance in LLM-based Data Augmentation on Downstream Tasks
- **arXiv**: 2502.04419
- **年**: 2025年2月
- **著者**: Miao Li, Hao Chen, Yang Wang, Tingyuan Zhu, Weijia Zhang, Kaijie Zhu, Kam-Fai Wong, Jindong Wang
- **概要**: LLMを用いたデータ拡張において、LLMが訓練データに含まれるバイアスを継承・増幅するという問題（"Bias Inheritance"）を体系的に調査し、緩和手法を提案。SimAugはPLMのバイアスを軽減できると主張しているが、本論文はLLMデータ拡張全般のバイアスリスクに警鐘を鳴らしている。
- **推薦理由**: SimAugの限界（「PLMはバイアスを含む可能性がある」という指摘への対応）を深く理解するために必読。異なる角度（LLMの負の側面）からデータ拡張を論じている。
