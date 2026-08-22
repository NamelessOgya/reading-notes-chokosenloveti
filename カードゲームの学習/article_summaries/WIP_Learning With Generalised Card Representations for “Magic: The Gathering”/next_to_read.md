# 次に読むべき論文 (Next to Read)

本論文「Learning With Generalised Card Representations for “Magic: The Gathering”」は、ドラフトにおけるコンテキスト依存の好みをInfoNCE Lossを用いて学習する手法を提案しました。この研究の発展形や、別のアプローチから同じ問題（カードゲームのドラフト／好みの学習）に取り組んでいる後続研究として以下の論文を推奨します。

## 1. UrzaGPT: LoRA-Tuned Large Language Models for Card Selection in Collectible Card Games
- **arXiv ID**: 2508.08382
- **概要**: 
  本論文（Learning With Generalised Card Representations...）の著者らの後続研究であり、従来のSiamese NetworkやInfoNCEベースの埋め込みモデルからアプローチを変え、**大規模言語モデル（LLM）を用いたドラフト予測**に挑戦した論文です。オープンウェイトのLLM（Llama-3など）に対して、人間のドラフトログを用いたLoRA（Low-Rank Adaptation）ファインチューニングを行うことで、一般的な大規模モデル（GPT-4o：ゼロショット精度43%）を上回る精度（66.2%）を達成しています。
- **読むべき理由**: 
  本論文の「コンテキストの表現形式の難しさ」という課題に対し、LLMの文脈理解力とLoRAによるドメイン適応を活用してアプローチした直接的な進展です。新しいカードセットの追加に対して、モデルアーキテクチャの変更なしにLLMのファインチューニングのみで対応可能かどうか（汎用性の向上）という点で、本論文に続く重要なマイルストーンとなります。
