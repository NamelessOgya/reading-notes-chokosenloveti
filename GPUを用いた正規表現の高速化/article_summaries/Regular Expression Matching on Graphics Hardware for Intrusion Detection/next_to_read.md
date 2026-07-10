# 次に読むべき論文 (Next to Read)

本論文（Vasiliadis et al., RAID 2009）は、GPUを用いた正規表現マッチング技術の先駆的な研究であり、多数の研究に引用されています。特に著者ら自身による継続的な研究や、GPU上の状態管理・パケット処理アーキテクチャの発展系を探求する論文が重要です。

以下に本手法を発展させている、またはより洗練された統合アプローチを取る後続論文（Cited by / Follow-up）を挙げます。

1. **MIDeA: A Multi-Parallel Intrusion Detection Architecture** (ACM CCS 2011)
   * **著者**: Giorgos Vasiliadis, Michalis Polychronakis, Sotiris Ioannidis
   * **概要**: 本論文（2009年）のアプローチをさらに発展させ、マルチコアCPUとGPUの双方を活用するハイブリッドな並列アーキテクチャ「MIDeA」を提案しています。より高度な負荷分散や最新のネットワークインターフェースと組み合わせた高速処理手法が論じられており、システムの全体的な最適化を知る上で必読です。

2. **GASPP: A GPU-Accelerated Stateful Packet Processing Framework** (USENIX ATC 2014)
   * **著者**: Giorgos Vasiliadis, Lazaros Koromilas, Michalis Polychronakis, Sotiris Ioannidis
   * **概要**: 本論文で確立されたGPUによる並列マッチングの仕組みをベースとしつつ、さらに複雑なステートフル（状態保持型）なパケット処理フレームワークへと進化させた研究です。ステートレスなDFA検索からより複雑なトラフィック解析への応用をどうGPUで行うかについての解法が示されています。

3. **HybridSA: A Hybrid String Matching Algorithm Based on Suffix Automaton** (関連応用やBit Parallelismアプローチなど)
   * **概要**: 同分野においてGPUを用いたDFA/NFAのメモリ非効率性を解決するための別角度のアプローチ（ハイブリッドFAやBit Parallelismによる表現）を提案する後続研究も多数登場しています（例として昨今の `HybridSA: GPU Acceleration of Multi-pattern Regex Matching using Bit Parallelism` などの関連最新論文）。メモリ階層と状態爆発問題にどう対処しているか、本論文とは別のアプローチとして併読することが推奨されます。
