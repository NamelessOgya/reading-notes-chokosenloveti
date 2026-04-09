# 次に読むべき論文 (Next to Read)

本論文（EvoX: Meta-Evolution for Automated Discovery, 2026年2月公開）の発表時期が非常に近接しているため、直接本作をCited by（被引用）している後続の実績論文は現段階（2026年4月時点）で存在せず、各学術検索プラットフォームへの反映も確認できませんでした。そのため、この事実を正確に記載し、捏造（ハルシネーション）を回避します。代替として、本作の前提となっている技術や、同時期に大元として議論されている最新の競合・関連論文（Concurrent Work）や同派生論文を列挙します。

## 1. 関連・比較対象（Concurrent / Baseline Works）

*   **OpenEvolve: A Comprehensive Framework for Language Model-driven Evolution (2025)**
    *   **理由:** EvoX内で主要なベースラインとして最も頻繁に比較されているオープンソースのフレームワークです。固定的な探索戦略に基づく設計がどのように構成されているかを深く理解することで、EvoXのメタ進化の優位性を相対的に把握できます。
*   **ShinkaEvolve: Bandit-Based Selection and Adaptation for LLM Evolution (2025)**
    *   **理由:** LLMのGeneratorの選択にバンディットアルゴリズムを用いて適応性（Adaptivity）を部分的に導入した研究です。このフレームワークの限界（Generatorの適応はできるが、戦略全体のパラメータは固定される点）を知ることで、EvoXへの発展の系譜が理解できます。
*   **GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (2025)**
    *   **理由:** こちらもEvoXと共にLLMの進化的アルゴリズムフレームワークとして最先端を構成している手法です。強化学習を凌駕するプロンプトベースの進化設計に焦点を当てており、EvoXのコストメリット等と比較される頻度が高いため必読です。
*   **AlphaEvolve (2024 / DeepMind)**
    *   **理由:** 本研究の動機付けの根源となっている論文の一つであり、LLMを用いたMAP-Elitesベースの最適化を数学・アルゴリズム設計分野で適用しブレイクスルーをもたらしました。EvoXがこれをどのように発展させたかを理解する土台となります。

## 2. ベンチマーク・ドメイン固有の関連研究

*   **ADRS-Bench (Cheng et al., 2025)**
    *   **理由:** EvoXがSystem Performance Problemsの検証として使用している最新のベンチマークです。現代の大規模システムにおけるパフォーマンスチューニングにLLMがどのように活用されているかを把握するのに適しています。
*   **Frontier-CS (Mang et al., 2025)**
    *   **理由:** コンピュータサイエンスの未解決課題などを集めたオープンエンドベンチマークです。EvoXがアルゴリズムタスクにおいて「継続的なスコアの成長」を見せた舞台です。

※ 当ペーパーへの直接のCite論文は今後数ヶ月以内に蓄積されるため、時期を見て `fetch_citations.py` またはSemantic Scholar等を再度実行することで正確な後続研究のトラッキングが可能です。
