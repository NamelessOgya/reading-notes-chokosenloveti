# 次に読むべき論文 (Next to Read)

本論文（"Regular Expressions on Modern GPGPUs", 2024年発表）は発行からの期間が短く、論文誌で完全に公開されていないため、現時点で直接本論文を引用している後続研究（Cited by）の中核となるものは確認できなかった。

そのため、対象論文の引用先を捏造（ハルシネーション）するのではなく、代替として**同時期（2023〜2024年）に発表された正規表現マッチングのハードウェア並列化や検索高速化に関連する研究（Concurrent Work）**を以下に列挙する。

1. **Xav: A High-Performance Regular Expression Matching Engine for Packet Processing**
   - **著者**: Zhong, Chen, Yu
   - **発表年**: 2024年
   - **理由**: ネットワークパケット処理に特化した高性能な正規表現マッチングエンジンの提案。本論文の比較対象にもなっているディープ・パケット・インスペクション（DPI）などの用途に向けた最新の高速化手法として、パケット処理のコンテキストとGPUベースアプローチとの差異を相互に比較する上で参考になる。

2. **P4rex: Accelerating Regular Expression Matching with Programmable Switches**
   - **著者**: Lin, Lin, Lin, Zhu, Zhang, Wu
   - **発表年**: 2023年
   - **理由**: プログラマブルスイッチを用いて正規表現マッチングをハードウェアレベルで高速化するアプローチ。GPUというアーキテクチャとは異なるベクトルで、ハードウェアの特性を活かした並列マッチングを行うための比較対象として有用である。

3. **Search-Based Regular Expression Inference on a GPU**
   - **著者**: Valizadeh, Berger
   - **発表年**: 2023年
   - **理由**: 本論文は正規表現を用いたストリング検索をGPU上で行うものだが、こちらはGPUを用いて正規表現ルール自体を「推論」する処理を高速化する研究である。GPUを活用して巨大な計算空間を探索・最適化するという点で、GPUによるアルゴリズムの並列化の発展的な適用例である。
