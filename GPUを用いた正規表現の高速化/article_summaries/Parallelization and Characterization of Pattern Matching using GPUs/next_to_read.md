# 次に読むべき論文 (Next to Read)

対象論文「Parallelization and Characterization of Pattern Matching using GPUs」を引用している（Cited by）論文群から、本手法を発展させているものや、新しい観点でGPUを用いた正規表現マッチングの高速化にアプローチしている重要な後続研究を抽出しました。

1. **Why GPUs are Slow at Executing NFAs and How to Make them Faster (2020)**
   - **理由:** 対象論文ではDFA（決定性有限オートマトン）ベースのマッチングとメモリ最適化が主眼でしたが、本論文はNFA（非決定性有限オートマトン）をGPU上で実行する際のパフォーマンス低下（メモリアクセスの非効率性や分岐の多さ）の根本原因を詳細に分析し、その解決策を提示しています。GPUベースの正規表現処理におけるアーキテクチャの課題を解明する上で不可欠な研究です。

2. **HybridSA: GPU Acceleration of Multi-pattern Regex Matching using Bit Parallelism (2024)**
   - **理由:** 対象論文からかなりの期間を経て、最新のGPUアーキテクチャを活用し、ビット並列性（Bit Parallelism）を用いて複数のパターンセットの正規表現マッチングをさらに高速化する手法（HybridSA）を提案しています。マルチパターンのマッチングにおいて、現在どのようなアプローチが最先端であるかを知る上で非常に有用です。

3. **ngAP: Non-blocking Large-scale Automata Processing on GPUs (2024)**
   - **理由:** 大規模なオートマトン処理におけるGPUの同期ボトルネックを回避するため、GPU上でのノンブロッキングな処理アルゴリズムを提案しています。対象論文が指摘していたメモリアクセスの輻輳や並列処理の限界に対して、より発展的なアーキテクチャレベルの工夫を施しており、最新のスケールアウト手法として有益です。

4. **Interleaved Bitstream Execution for Multi-Pattern Regex Matching on GPUs (2025)**
   - **理由:** GPU上でのマルチパターン正規表現マッチングにおいて、ビットストリーム実行をインターリーブ（交差）させる最新の最適化手法を提案しています。対象論文の基本的な並列化アプローチから、いかにしてメモリ帯域幅の限界を押し広げているかを示す最新動向として重要です。
