# 次に読むべき論文 (Next to Read)

本論文『Understanding Generative Recommendation with Semantic IDs from a Model-scaling View』は、発表直後の最新研究（プレプリント）であるため、現時点で本作を直接引用している（Cited by）後続論文は見つかっていません。

そのため、代替として本論文のテーマである「Generative Recommendationのパラダイム比較」「Semantic IDの限界」「LLM-as-RSのスケーリングとフレームワーク」に密接に関連する、同時期の重要な関連論文（Concurrent Work）や同著者らによるフォローアップ研究を以下に列挙します。

### 1. 同著者らによるGenerative Recommendation実践ハンドブック
**論文名:** Generative Recommendation with Semantic IDs: A Practitioner's Handbook (2025)
**著者:** Clark Mingxuan Ju, Liam Collins, ... , Neil Shah, et al.
**概要:** 本論文と同じ著者陣（Snap Inc. など）によって公開された、Semantic IDベースのレコメンド（GRIDフレームワーク）を実践的に構築・ベンチマークするための網羅的なガイド。本論文で指摘されたSIDの限界を理解した上で、いかに現状の実システムに落とし込み、コンポーネントごとの性能評価を行うかを論じているため、実践面での補完として必読。

### 2. LLM-as-RSの包括的評価とベンチマーク
**論文名:** RECBENCH: A Comprehensive Benchmark for LLM-as-RS
**概要:** 本論文が結論として推奨した「LLM-as-RSパラダイム」をさらに深掘りするにあたり、LLMを用いたレコメンドシステムの性能を従来のディープラーニング手法と客観的に比較・評価するためのベンチマークを提案した論文。LLM-as-RSがどのように振る舞うかを多角的に分析している。

### 3. SIDsの表現力向上を狙う関連研究
**論文名:** Enhancing Item Tokenization for Generative Recommendation through Self-Improvement (2024)
**著者:** Runjin Chen, Mingxuan Ju, et al.
**概要:** 本論文のReferenceにも挙げられており、同著者陣が関与している研究。Semantic ID（量子化トークン）の表現力がボトルネックとなる問題に対し、トークン化のプロセスを自己改善（Self-Improvement）させることでSIDsの質を向上させるアプローチを提案している。SIDの限界を突破しようとする試みとして重要。
