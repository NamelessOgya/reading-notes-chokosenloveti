# 次に読むべき論文 (Next to Read)

本論文（Harnessing Large Language Models for Text-Rich Sequential Recommendation (LLM-TRSR), 2024）は発表から間もない最新の研究であり、また書誌情報API（Semantic Scholar等）の参照においてRate Limitエラーが確認されたため、確定的な「本論文を直接引用している後続論文（Cited by）」を捏造なくリストアップすることが困難です。

ハルシネーション（偽の被引用論文の提示）を避けるため、ここでは「被引用の直接確認が取れなかった」旨を明記した上で、代替として本論文と同分野・同時期の最新関連論文（Concurrent Work）や同手法のアプローチを深掘りする研究を列挙します。

## 1. Continual Low-Rank Adapters for LLM-based Generative Recommender Systems (PESO) (2024)
- **関連性:** 本論文（LLM-TRSR）でもSFTとLoRA（Low-Rank Adaptation）を組み合わせて効率的なファインチューニングを採用しています。PESOはさらに「継続学習（Continual Learning）」の観点を取り入れ、変化するユーザーの嗜好に合わせてLLM生成レコメンドモデルのLoRAパラメータを破滅的忘却（Catastrophic Forgetting）なしに効率良く更新し続ける手法を提案しています。

## 2. Text-like Encoding of Collaborative Information in Large Language Models for Recommendation (BinLLM) (2024)
- **関連性:** 本論文ではユーザーの行動履歴を「自然言語のテキストブロック」として要約することでコンテキスト長問題に対処しています。一方でBinLLMは、テキストそのものではなく協調シグナル（ID情報やアイテム表現）をLLMが処理しやすい「テキストライクなバイナリ系列」に変換して入力する別のアプローチを取っており、LLMのトークン制約とテキスト指向の情報処理能力を別の角度から活用しています。

## 3. LLaRA: Large Language-Recommendation Assistant (2023/2024)
- **関連性:** 本論文と同様にLLMをレコメンド向けのアシスタントモデルとしてファインチューニングするアプローチです。LLM-TRSRは要約器を挟む「推論＋推薦」分離型でしたが、LLaRAは従来のIDベースの協調フィルタリングやシーケンシャルレコメンドの出力をそのまま統合し、ハイブリッドプロンプトとカリキュラム学習を用いてLLMに推薦タスクを直接学習させるアプローチの代表例として比較検証に役立ちます。
