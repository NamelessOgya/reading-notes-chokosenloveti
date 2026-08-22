# 次に読むべき関係論文 (Cardsformer: Grounding language to learn a generalizable policy in hearthstone)

Cardsformer論文の被引用（Cited by）論文を調査した結果、2025年に発表された以下の2件の後続研究が確認されました。それぞれ、強化学習手法の拡張方向や、カードゲームのゲームバランス分析といった異なるアプローチからアプローチされています。

## 手法を発展させているもの

### Guided Proximal Policy Optimization with Structured Action Graph for Complex Decision-making (2025)
- **概要・選定理由:**
  CardsformerはQ学習とPrediction Modelの組み合わせによって複雑な状態・行動空間を扱いましたが、この論文では強化学習における代表的なアルゴリズムであるPPO（Proximal Policy Optimization）に対し、行動グラフ（Structured Action Graph）を導入してガイドを与える手法を提案しています。Hearthstoneのような大規模な行動空間（コンプレックスな意思決定）において、どのように効果的にポリシー最適化を行うかという点で手法的な発展が期待できます。

## 違う角度からアプローチしているもの

### Towards Detecting Infinite Combos in Collectible Card Game (2025)
- **概要・選定理由:**
  Cardsformerが「新たなカード効果の意味を言語から理解してプレイするAIエージェントの開発」に焦点を当てていたのに対し、本論文はトレーディングカードゲーム（CCG）特有の複雑なカードの相互作用によって発生する「無限ループ（Infinite Combos）」の検出という、ゲームデザインやバランス検証の課題に取り組んでいます。カードの組み合わせが膨大になるHearthstoneのような環境において、エージェントにとっても開発者にとっても重要なテーマです。
