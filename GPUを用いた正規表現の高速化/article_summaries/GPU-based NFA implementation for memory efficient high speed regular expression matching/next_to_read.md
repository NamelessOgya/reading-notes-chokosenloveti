# 次に読むべき論文 (Next to Read)

本論文（GPU-based NFA implementation ..., PPoPP 2012）を発展させている、あるいは別角度からアプローチしている後続研究を以下に列挙します。

## 1. HybridSA: GPU Acceleration of Multi-pattern Regex Matching using Bit Parallelism
* **発表年**: 2024
* **著者**: Alexis Le Glaunec, Lingkun Kong, Konstantinos Mamouras
* **選定理由**: PPoPP 2012の段階では単純なNFAの並列化が主眼でしたが、最新のGPUアーキテクチャ上において複数パターンの正規表現マッチングを、**ビット並列性（Bit Parallelism）** を用いてさらに劇的に高速化・最適化するアプローチです。近年におけるこの分野の最先端の手法の一つであり、次に深掘りするトピックとして最適です。

## 2. Why GPUs are Slow at Executing NFAs and How to Make them Faster
* **発表年**: 2020
* **著者**: Hongyuan Liu, Sreepathi Pai, Adwait Jog
* **選定理由**: 本論文の発表以降、他の様々なGPUベースNFA実装が模索されましたが、依然として課題は残っていました。この2020年の論文は「なぜGPUにおけるNFA実行が遅くなりがちか」という根本的なアーキテクチャやメモリアクセスの問題点を改めて深くプロファイリング・分析し、そこに対する改善策を提案した研究です。NFAアーキテクチャの発展の系譜を知る上で極めて重要です。

## 3. ANG: Accelerating NFA processing on GPUs via Exploring Multi-Level Fine-Grained Parallelism
* **発表年**: 2025
* **著者**: Yuguang Wang, Yunmo Zhang, Zeyu Liu, Junqiao Qiu, Zhenlin Wang
* **選定理由**: ごく最近の2025年に発表された最新の論文です。GPU内部のマルチレベル（例えばWarp内、Thread Block間など）にわたる細粒度な（Fine-Grained）並列性をさらに掘り下げ、NFA処理の究極の効率化を目指しています。ハードウェアの進化に併せた現在進行系の実装アプローチとして読むべき一本です。

## 4. ngAP: Non-blocking Large-scale Automata Processing on GPUs
* **発表年**: 2024
* **著者**: Tianao Ge, Tong Zhang, Hongyuan Liu
* **選定理由**: 大規模なオートマトン処理における同期やレイテンシのボトルネックを解消するため、「ノンブロッキング（Non-blocking）」アーキテクチャを導入したアプローチです。NFA並列化が直面する限界を異なるアーキテクチャ側から迂回・解消しようとする試みとして、興味深い発展系です。
