# Next To Read

著者であるYuting Liuらによる「CoRA (Collaborative Information Perception by Large Language Model’s Weights for Recommendation)」（AAAI 2025）の手法を発展させている、または同領域で関連性の高いアプローチをとる被引用論文（Cited by）および後続研究を以下に列挙する。

1. **KICR: A Two-Stage Framework for Knowledge-Aware Collaborative Representation Learning in LLM-Based Course Recommendation** (Ge et al., 2025)
   - 概要: コース推したいという特化ドメインにおいてLLMを適用し、協調情報や知識ベースの表現学習を2段階で行うアーキテクチャ。ドメイン特化型の推奨タスクにおける協調情報のモデルへの統合手法としてCoRAからの発展が見られる。

2. **Continual Low-Rank Adapters for LLM-based Generative Recommender Systems** (Yoo et al., 2025)
   - 概要: 低ランクアダプタ（LoRAなど）を活用してLLM生成型推薦システムを継続的（Continual）に学習・適応させる研究。パラメータ空間を利用したLLMの推薦特化への汎用的な適応という点で、CoRAの重み空間パラダイムを別角度から継承・発展させている。

両論文はいずれも2025年に発表された最新の後続研究であり、CoRAにおける「重み（パラメータ）空間を通じてLLMに推薦知識を付与する」というパラダイムを、新たなるドメインや継続的学習シナリオの解決へ応用している。
