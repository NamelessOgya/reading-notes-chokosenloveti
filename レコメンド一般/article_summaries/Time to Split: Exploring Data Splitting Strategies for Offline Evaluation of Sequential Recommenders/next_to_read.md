# Next to Read

## 被引用状況の確認

本論文（arXiv: 2507.16289）はACM RecSys 2025に採択・発表された2025年7月公開の論文であり、2025年5月時点では**まだ当該論文を引用した後続研究は確認されていない**。

以下は代替として、同じ評価・分割戦略の問題意識を共有する**同時期の関連論文（Concurrent / Foundational Work）**を列挙する。これらは本論文が引用・問題提起の起点としている研究群、またはRecSys 2024〜2025の同分野の動向として参照価値が高いものである。

---

## 推奨論文一覧

### 1. Does It Look Sequential? An Analysis of Datasets for Evaluation of Sequential Recommendations
- **著者**: Anton Klenitskiy, Anna Volodkevich, Anton Pembek, Alexey Vasilev
- **発表**: ACM RecSys 2024
- **概要**: 本論文の著者グループが同じ研究チームであり、「そのデータセットは本当に逐次的か？」という観点から、逐次推薦の評価に使われる標準データセットを分析する。MovieLensやAmazon Beautyなどの「逐次性の強さ」を測定し、データセット選択が評価結果に与える影響を明らかにした。
- **本論文との関係**: 本論文の実験設計（データセット選択方針）の直接的な前提論文。評価プロトコル整備という同じ問題意識を持つ。

### 2. A Critical Study on Data Leakage in Recommender System Offline Evaluation
- **著者**: Yitong Ji, Aixin Sun, Jie Zhang, Chenliang Li
- **発表**: ACM Transactions on Information Systems (TOIS) 2023
- **arXiv**: 2010.11060
- **概要**: leave-last-one-out等の一般的な評価手法がグローバルタイムラインを守らないことで時間的リークを引き起こすことを体系的に分析。タイムラインベースの評価スキームを提案した先駆的研究。
- **本論文との関係**: 本論文が「時間的リーク」の問題根拠として引用している基礎論文。GTSへの移行を動機づけた重要先行研究。

### 3. Widespread Flaws in Offline Evaluation of Recommender Systems
- **著者**: Balázs Hidasi, Ádám Tibor Czapp
- **発表**: ACM RecSys 2023
- **概要**: 推薦システムのオフライン評価における広範な欠陥（時間的リーク、データセットとタスクのミスマッチ、過剰な前処理等）を体系的に分類・指摘した批判的研究。
- **本論文との関係**: 本論文のモチベーションの中心的根拠として引用。LOO分割の問題点を指摘した重要先行研究。

### 4. Take a Fresh Look at Recommender Systems from an Evaluation Standpoint
- **著者**: Aixin Sun
- **発表**: SIGIR 2023
- **概要**: 推薦システム研究を評価の観点から再考し、現行の評価手法の問題点（データ分割、メトリクス選択等）を批判的に検討した。GTSへの移行を主張。
- **本論文との関係**: 本論文が引用する評価改善の重要先行研究。

### 5. Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches
- **著者**: Maurizio Ferrari Dacrema, Paolo Cremonesi, Dietmar Jannach
- **発表**: ACM RecSys 2019
- **概要**: 最近のニューラル推薦アプローチの多くが、適切に最適化された単純なベースラインを超えないという再現性の危機を指摘した。評価方法論の不備が研究の比較可能性を損なっていることを実証した。
- **本論文との関係**: 推薦システム評価の再現性・信頼性の問題を継続する系譜の原点となる論文。

### 6. Exploring Data Splitting Strategies for the Evaluation of Recommendation Models
- **著者**: Zaiqiao Meng, Richard McCreadie, Craig Macdonald, Iadh Ounis
- **発表**: ACM RecSys 2020
- **概要**: 推薦モデルの評価における様々なデータ分割戦略（ランダム、時間的、ユーザベース等）の影響を分析。Kendall相関を用いてモデルランキングの一貫性を評価した本論文の方法論的先行研究。
- **本論文との関係**: 本論文が方法論（Kendall相関）と問題設定を継承した直接的な先行研究。本論文はこれをSRS＋NIPタスクに特化して発展させた。

### 7. RePlay: A Recommendation Framework for Experimentation and Production Use
- **著者**: Alexey Vasilev, Anna Volodkevich, Denis Kulandin, et al.
- **発表**: ACM RecSys 2024
- **概要**: 本論文の著者グループが開発したRecommendationフレームワーク。実験と本番環境の両方で使用可能な設計で、本論文のベンチマーク実験でも評価指標計算に採用されている。GTS+NIPのサポートも含む。
- **本論文との関係**: 本論文の実験インフラとして使用されたフレームワーク。データ分割戦略の標準化実装として直接の発展先。

### 8. Are We Evaluating Rigorously? Benchmarking Recommendation for Reproducible Evaluation and Fair Comparison (DaisyRec)
- **著者**: Zhu Sun, Di Yu, Hui Fang, et al.
- **発表**: ACM RecSys 2020
- **概要**: 推薦システムの再現可能で公正な評価のためのベンチマークフレームワーク（DaisyRec）を提案。GTS-basedの分割を含む複数の評価手法を支援。
- **本論文との関係**: 本論文のTable 1で比較対象となったフレームワーク。評価の標準化という同じ課題に取り組む。

---

## まとめ

本論文（2507.16289）は2025年7月公開であるため、現時点での被引用後続研究は存在しない。次に読む論文として、評価プロトコルの批判・改善に焦点を当てた上記の先行研究群を推薦する。特に **論文1（Does It Look Sequential?）** は同じ研究チームによる直接の関連研究であり、本論文と組み合わせることで「データセットの逐次性の強さ × データ分割戦略」という二つの軸での評価設計の全体像が把握できる。
