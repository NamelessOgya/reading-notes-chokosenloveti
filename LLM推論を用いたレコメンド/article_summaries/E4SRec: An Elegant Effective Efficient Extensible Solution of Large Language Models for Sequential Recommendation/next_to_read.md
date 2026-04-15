# 次に読むべき論文 (Next to Read)

「E4SRec: An Elegant Effective Efficient Extensible Solution of Large Language Models for Sequential Recommendation」を引用（Cited by）しており、本手法を異なる角度から発展させている、あるいは関連するアプローチを拡張している重要論文を以下に列挙する。

## 1. Customizing Language Models with Instance-wise LoRA for Sequential Recommendation (2024)
- **著者**: Xiaoyu Kong, Jiancan Wu, An Zhang, Leheng Sheng, Hui Lin, Xiang Wang, Xiangnan He
- **概要**: E4SRecと同様にLLMのParameter-Efficient Fine-Tuning (LoRA等)をシーケンシャルレコメンドに適用するという観点を出発点とするが、単一のLoRAを全ユーザー・全シーケンスに適用するのではなく、Mixture of Experts (MoE) フレームワークを拡張し「Instance-wise LoRA (iLoRA)」を提案している。E4SRecが全ユーザーで共通のアダプタを通していたのに対し、パーソナライズされた動的なアダプタを利用して精度向上を測る強力な発展アプローチである。

## 2. Text-like Encoding of Collaborative Information in Large Language Models for Recommendation (2024)
- **著者**: Yang Zhang, Keqin Bao, Ming Yang, Wenjie Wang, Fuli Feng, Xiangnan He
- **概要**: E4SRecの「コラボラティブ情報(ID)を直接LLMに注入する」アプローチに対して、別角度から課題を指摘した論文(BinLLM)。IDのエンベディングを直接射影するのではなく、外部モデルのコラボラティブベクトルを「バイナリ文字列シーケンス」というテキストライクな表現に変換してLLMに読ませることで、LLM本来のテキスト処理の強みを崩さずにコラボラティブ情報を統合する新しい手法を提案している。プロンプトエンジニアリングや入力表現の工夫による別アプローチとして参照価値が高い。

## 3. CoRA: Collaborative Information Perception by Large Language Model's Weights for Recommendation (2024)
- **著者**: Yuting Liu, Jinghao Zhang, Yizhou Dang, Yuliang Liang, Qiang Liu, Guibing Guo, Jianzhe Zhao, Xingwei Wang
- **概要**: こちらもE4SRecの「IDとLLMの統合」に関連して、データの入力空間でベクトルを結合する（Input space alignment）のではなく、LLMのパラメータ空間（重み）にコラボラティブな情報を注入する「Collaborative LoRA (CoRA)」を提案している。入力プロンプトのテキスト推論能力を毀損することなく、推薦システムのコラボラティブフィルタリングの重みをLLMの推論結果に直接影響させる発展形の手法である。
