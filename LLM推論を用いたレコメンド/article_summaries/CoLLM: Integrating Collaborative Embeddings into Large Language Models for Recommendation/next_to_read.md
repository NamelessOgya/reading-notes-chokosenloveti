# 次に読むべき論文 (Next to Read)

Semantic Scholar APIの一時的なアクセス制限（Rate Limit: 429 エラー）や、情報の取得難易度により、現状では本論文「CoLLM」を直接引用している（Cited by）論文の正確なリストを取得できませんでした。

そのため、ハルシネーション（情報の捏造）を避ける観点から、被引用リストの代替として、「LLM推論を用いたレコメンド」分野における同じ発表時期の最新関連論文（Concurrent Work）や、同様に協調情報（Collaborative Information）をLLMに統合しようとする発展的な手法を以下に列挙します。

1. **TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation**
   - **概要:** 本論文（CoLLM）でも強力なベースラインとして比較されている研究。LLMをレコメンドタスクに適応させるために、少量のデータでInstruction Tuningを行う効率的なフレームワークを提案している。CoLLMの学習アプローチの基礎となる手法。

2. **CoRA: Collaborative Information Perception by Large Language Model’s Weights for Recommendation**
   - **概要:** CoLLMと同様に「協調情報（Collaborative Information）」をLLMでどのように扱うかという課題を解決するアプローチ。CoLLMが協調情報の埋め込みをプロンプト内（Input-space）にトークンとして結合する手法をとるのに対し、CoRAはLoRAモジュールの重み空間（Parameter-space）に協調情報を統合するという別角度からの発展的アプローチをとっている。

3. **PEPLER: Personalized Prompt Learning for Explainable Recommendation**
   - **概要:** レコメンドシステムにおいて、LLMを用いたパーソナライズされたプロンプト学習（Prompt Learning）を通じて、単なる推薦だけでなく「なぜ推薦したか」の説明（Explainable Recommendation）を生成するアプローチ。テキストセマンティクスとユーザーの好みを結びつける別視点の研究。
