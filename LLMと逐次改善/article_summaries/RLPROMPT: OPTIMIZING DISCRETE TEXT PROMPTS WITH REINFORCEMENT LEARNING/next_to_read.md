# 次の読むべき関連論文 (Next to Read)

本論文（RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning）は、強化学習を用いて人間にとっては「意味不明（Gibberish）」であるが高性能な離散プロンプトを生成する手法を提案しました。この手法の限界（検索に時間がかかる、事前の固定されたプロンプトであるなど）や概念を発展させた後続の重要な研究として、以下を提案します。

## 1. TEMPERA: Test-Time Prompt Editing via Reinforcement Learning (Zhang et al., 2022 / 2023)
*   **関連性:** `RLPrompt` が事前に特定タスク用の固定プロンプトを学習するのに対し、`TEMPERA` はテスト時（推論時）に入力コンテキストに応じて動的にプロンプトを編集（Edit）するアプローチに進化させました。強化学習（RL）をプロンプト最適化に用いるというコアコンセプトを共有しつつ、動的な適応（Dynamic Adaptation）という新たな角度からLLMチューニングの限界に挑戦しています。

## 2. TextGrad: Automatic "Differentiation" via Text (Madaan et al. / Yuksekgonul et al., 2024)
*   **関連性:** `RLPrompt` が離散トークンに対する勾配計算ができない問題を強化学習（RL）で回避したのに対して、`TextGrad` は「LLM自体をテキストベースの勾配計算機（Optimizer）として機能させる」ことで、自然言語によるバックプロパゲーションという全く別のアプローチで離散プロンプトの連続最適化を実現しました。離散空間における最適化の最新パラダイムとして必読です。

## 3. Large Language Models as Optimizers (OPRO) (Yang et al., 2023)
*   **関連性:** Google DeepMindから発表された論文で、LLM自身に「過去のプロンプトと成績の履歴」を与え、推論とフィードバックの反復を通じて離散プロンプトを最適化させます。RLを用いずともLLM自体の推論能力で自己最適化を可能にしており、`RLPrompt` のようなメタ・オプティマイザの役割を強化学習モデルからLLM本体に置き換えたアプローチとして非常に重要です。

---
**注記:** 今回は対象論文がすでにLLMプロンティングにおける古典的基礎論文（EMNLP 2022）となっているため、上記のように同概念をさらに推し進めたり、異なる強力なパラダイム（LLM as Optimizer）でブレイクスルーを果たした後続研究（Cited by または Follow-up）を抽出しました。
