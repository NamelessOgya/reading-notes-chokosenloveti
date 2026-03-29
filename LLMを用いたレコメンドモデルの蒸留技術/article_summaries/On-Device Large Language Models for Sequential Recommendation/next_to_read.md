# 次に読むべき論文 (Next to Read)

本論文（"On-Device Large Language Models for Sequential Recommendation"）は2026年1月にarXivにて公開された最新の論文であるため、現時点において**直接本論文を引用している後続論文（Cited by）は存在しません（被引用なし）。**

そのため代替案として、本論文が解決しようとしている課題（LLMの推薦システムにおける圧縮・エッジデバイスへの展開）と密接に関連する、**同時期の最新関連論文（Concurrent Work）** や、本論文の手法の**基礎となっているベースライン論文**を以下に列挙します。

## 1. Adapting Large Language Models for Recommendation (LC-Rec)
**Authors:** Zheng et al. (2024)
**Abstract:** 本論文（OD-LLM）のUncompressed Backbone（圧縮前のベースモデル）として使用されているLLMベースの推薦フレームワーク「LC-Rec」の提案論文。LLaMA-7Bをベースに推薦データセットをファインチューニングし、テキストからユーザーやアイテムのシーケンシャルな依存関係を学習する。このモデルを理解することで、なぜOD-LLMが圧縮時にどの特徴量を維持しようとしているのかがより深く理解できる。

## 2. Towards On-Device Large Language Models
**Authors:** Shekhar et al. (2024 / Concurrent Work)
**Abstract:** LLMをリソースが制限されたデバイス（スマートフォンやウェアラブルなどのエッジデバイス）上で効率的に動作させるための、量子化（Quantization）やプルーニングなどの総合的な圧縮手法についてサーベイと新しい戦略を提案している論文。OD-LLMのようなタスク適応型（推薦特化型）ではなく汎用NLPタスク向けの最適化手法を解説しており、アプローチの比較において非常に参考になる。

## 3. SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot
**Authors:** Frantar et al. (2023)
**Abstract:** 本論文の実験における比較対象（Baseline）として使用された、最先端のワンショット非構造化プルーニング手法。数十億パラメータ規模のLLMを再学習なしで高精度に圧縮することができる。OD-LLMが推薦タスクにおいてなぜSparseGPTを上回る精度と推論速度を達成できたのか（推薦特有の繊細な行動パターンの維持などの観点）を比較するための基礎資料となる。
