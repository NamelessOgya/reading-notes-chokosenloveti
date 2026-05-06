# Next to Read: Text-like Encoding of Collaborative Information in Large Language Models for Recommendation

## 被引用および関連論文

論文「Text-like Encoding of Collaborative Information in Large Language Models for Recommendation (BinLLM)」を引用、あるいは関連してLLM推論に協調情報やシーケンシャル情報をエンコードして統合する研究として、以下が挙げられます。

- **論文名:** Temporal Integration-Enhanced Fine-Tuning of Large Language Models for Sequential Recommendation (TisLLM)
  - **関連性:** 既存のLLMRec（LLMを用いたレコメンド手法）が協調信号や時系列に並んだ行動信号をうまく捉えられないという課題を指摘しつつ、BinLLM（二元シーケンス・テキストエンコーディング）の課題認識と類似したベクトルを持ち発展させています。TisLLMは時間的統合（Temporal Integration）を強化し、シーケンシャルレコメンデーション向けにファインチューニングのプロセスを拡張することで、より正確なアイテムの相互作用をLLMで捉えるアプローチを提案しています。

この他にも、推薦システムにおける「協調情報をそのまま潜在空間マッピングするのではなく、言語モデルが自然に処理できる形式にエンコードし直してプロンプトやインコンテキストに統合する」一連の最新研究（LLaRAなど）が、本手法と深い関連を持ち、異なる角度からのアプローチとして次に読むべき文献です。
