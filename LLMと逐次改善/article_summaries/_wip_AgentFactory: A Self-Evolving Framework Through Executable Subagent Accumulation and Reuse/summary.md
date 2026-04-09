# AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse

## 背景
LLMベースのエージェントにおける「自己進化（Self-Evolution）」のアプローチは、これまでタスクに成功した経験を「テキストベースのプロンプト」や「自然言語による反省（Verbal Reflection）」として記録する手法（例：Reflexion等）が主流でした。しかし、これらのテキストベースの経験記録では、複雑な実世界のタスクを確実に実行・再現する（Re-execution）には限界がありました。

本論文では、ユーザーの日常的なタスクの多くが「再利用可能なサブタスクの集合（スケジュール調整、ファイル操作、情報検索など）」に分解できることに着目しました。そこで、成功したタスクの解決策を抽象的なテキストではなく、「実行可能なPythonのサブエージェントコード（Executable Subagent Code）」として保存・蓄積する新しい自己進化パラダイム「**AgentFactory**」を提案しています。

## 手法
AgentFactoryは、エージェントを構築・改善・展開するための3つのフェーズ「Install $\rightarrow$ Self-Evolve $\rightarrow$ Deploy」からなる自動パイプラインを実装しています。

![Figure 1: Overview of the AgentFactory pipeline.](./images/pipeline.png)

1. **Install (初期構築)**
未知の問題に直面した場合、Meta-Agentが問題をサブ問題に分解し、それに特化したサブエージェントをゼロから構築します。作成されたサブエージェントは、純粋なPythonコードとその機能を記述した標準的なドキュメント（`SKILL.md`）として保存され、再利用可能なスキルライブラリに追加されます。

2. **Self-Evolve (自己進化)**
過去に解決したタスクと類似する問題に遭遇した場合、システムはゼロから構築するのではなく保存済みのサブエージェントを再利用します。もし新しいタスクの要件に対して失敗や不備が生じた場合、Meta-Agentは実行フィードバックを自律的に分析し、サブエージェントのコード自体を書き換えて修正します。これにより、サブエージェントは単なるロジックの記憶から、より堅牢で汎用的なコードへと継続的に進化します。

![Figure 2: Evolution of path resolution mechanism across three runs.](./images/readme-evolve.png)

3. **Deploy (外部展開)**
スキルライブラリに蓄積・洗練されたサブエージェントは、純粋なPythonモジュールとしてエクスポート可能です。LangChainやClaude Codeなど他のAIフレームワークは、これらのモジュールとドキュメント（`SKILL.md`）を読み込むことで、AgentFactoryの成果を直接自己の能力として取り込むことができます。

![Figure 3: Demonstration of subagent saving and direct reuse across three trajectories.](./images/audio-evolve.png)


## 結果
AgentFactoryの有用性を評価するため、Web検索、データ視覚化、ブラウザ操作、音声処理など多様なドメインにわたる30個の実世界タスク（初期構築用のBatch 1が15タスク、再利用評価用のBatch 2が15タスク）を用いて検証しました。以下の各表にタスクの詳細や評価結果を示します。

| Method | Task Setting | Opus 4.6 (Avg. Tokens / Task) | Sonnet 4.6 (Avg. Tokens / Task) |
| :--- | :--- | :---: | :---: |
| ReAct | Batch 1 | 8298 | 6893 |
| ReAct | Batch 2 | 7022 | 7029 |
| Self-Evolving Agents | Batch 1 (from scratch) | 8608 | 8163 |
| Self-Evolving Agents | Batch 2 (w/ saved) | 6210 | 8223 |
| AgentFactory | Batch 1 (from scratch) | 4324 | 9199 |
| AgentFactory | Batch 2 (w/ saved) | 2971 | 3862 |

*Table 1: Average output tokens per task across evaluation configurations. Lower values indicate that the orchestrating agent requires less effort to complete tasks, reflecting more efficient subagent reuse. Token counts exclude subagent-internal LLM consumption.*


| # | Task Description |
| :---: | :--- |
| 1 | Among various online discussions about the housing price bubble, how has public sentiment changed over time? Generate an analysis report and a trend chart, and include discussion and summary in the report. |
| 2 | Search for and open the Stanford CS231n course homepage, find the syllabus or lecture list, and output the topics and corresponding links for the first 5 lectures. Save the final results to a markdown file. |
| 3 | Book a Tencent Meeting for tomorrow at 4 PM with the topic "Work Meeting". Find the meeting booking entry on the Tencent Meeting web version, then complete the booking through browser automation. Output the meeting invitation details, meeting ID, and meeting link. |
| 4 | Search for China's historical population data, then use matplotlib to plot the population change curve. |
| 5 | Search for Bitcoin's price data over the past 5 years, use matplotlib to plot the price trend, and calculate the annualized volatility. |
| 6 | Search for and download trending keyword frequency data from a social media platform, and display the top 20 using a bar chart. |
| 7 | Search for and download China's education expenditure and GDP data, plot a scatter chart showing the relationship between the two, and fit a regression line. |
| 8 | Write a Python mini-game: Tetris, with keyboard controls and basic scoring logic. |
| 9 | Search for and open Wikipedia, find the "Transformer (machine learning model)" page, extract its core definition, and summarize the main ideas of Self-Attention. Save the results to a markdown file. |
| 10 | Search for and open the GitHub website, find OpenAI's official organization page, and output the page's description and a list of main repositories (at least 5). Save the results to a markdown file. |
| 11 | Search for and open the HuggingFace website, find a "Text-to-Image" model leaderboard or collection page, and summarize the 3 most common model architectures. Save the results to a markdown file. |
| 12 | Create a soothing bedtime meditation audio file (15--20 min), featuring gentle guided breathing exercises, progressive muscle relaxation instructions, and calming visualizations. |
| 13 | Complete a task whose detailed description is provided in <audio_file_path>. |
| 14 | Search travel resources about Tokyo. Under a budget of $100 USD, plan a 3-day itinerary with at least one cultural attraction per day, total travel time under 5 hours, and at least one anime-related location. Output the itinerary, budget breakdown, and total travel time. |
| 15 | Search and download CO2 emissions and renewable energy share data for at least 5 countries. Analyze the correlation, generate a plot, and summarize the findings. |

*Table 2: Batch 1 evaluation tasks (15 tasks) used for initial subagent construction.*


| # | Task Description |
| :---: | :--- |
| 1 | Among various online discussions about electric vehicle adoption, how has public sentiment changed over time? Generate an analysis report and a trend chart, and include discussion and summary in the report. |
| 2 | Search for and open the MIT 6.S191 (Introduction to Deep Learning) course homepage, find the syllabus or lecture list, and output the topics and corresponding links for the first 5 lectures. Save the final results to a markdown file. |
| 3 | Book a Tencent Meeting for tomorrow at 7 PM with the topic "Work Meeting". Find the meeting booking entry on the Tencent Meeting web version, then complete the booking through browser automation. Output the meeting invitation details, meeting ID, and meeting link. |
| 4 | Search for Japan's historical population data, then use matplotlib to plot the population change curve. |
| 5 | Search for Ethereum's price data over the past 5 years, use matplotlib to plot the price trend, and calculate the annualized volatility. |
| 6 | Search for and download trending topic data from a Chinese social media platform, and display the top 20 using a bar chart. |
| 7 | Search for and download the US healthcare expenditure and GDP data, plot a scatter chart showing the relationship between the two, and fit a regression line. |
| 8 | Write a Python mini-game: Snake, with keyboard controls and basic scoring logic. |
| 9 | Search for and open Wikipedia, find the "BERT (language model)" page, extract its core definition, and summarize the main ideas of the Transformer architecture. Save the results to a markdown file. |
| 10 | Search for and open the GitHub website, find Meta AI's official organization page, and output the page's description and a list of main repositories (at least 5). Save the results to a markdown file. |
| 11 | Search for and open the HuggingFace website, find a "Text-to-Speech" model leaderboard or collection page, and summarize the 3 most common model architectures. Save the results to a markdown file. |
| 12 | Create a focus-enhancing background audio file (15--20 min), featuring gentle ambient sounds, subtle background music, and nature sounds to help concentrate. |
| 13 | Complete a task whose detailed description is provided in <audio_file_path>. |
| 14 | Search travel resources about Paris. Under a budget of $150 USD, plan a 3-day itinerary with at least one museum per day, total travel time under 6 hours, and at least one historic landmark. Output the itinerary, budget breakdown, and total travel time. |
| 15 | Search and download GDP per capita and life expectancy data for at least 5 countries. Analyze the correlation between economic development and health outcomes, generate a plot, and summarize the findings. |

*Table 3: Batch 2 evaluation tasks (15 tasks) used as transfer evaluation targets. Each task mirrors the structure of its Batch 1 counterpart but differs in specific requirements.*

実験から以下の結果と洞察が得られました。
- **再利用による大幅な効率化**: Batch 2の評価において、既存の再利用（ReAct手法やテキスト経験のみの自己進化エージェント）と比較し、AgentFactoryはオーケストレーションの平均トークン消費を大幅に削減（自己進化エージェントが6210トークンであるのに対し、Opus 4.6で2971トークン程度）しました（Table 1参照）。これにより、実行可能なサブエージェントをそのまま再利用することが非常に効率的であることが実証されました。
- **強力なモデルによる即時的な恩恵**: Claude Opus 4.6のような強力な基礎モデルでは、Batch 1（初期構築時）の異なるタスク間ですら関連性を認識し、作られたサブエージェントを再利用して問題解決を効率化している様子が観測されました（Batch 1の段階でReActの約半分である4324トークンまで削減）。
- **フィードバックベースの継続的改善**: Figure 2で描かれているように、初めはハードコードされた脆弱なパス取得ロジックだったエージェントが、実行エラーでのフィードバックを経て、「より汎用的な正規表現ベースのパース」へと自律的にコードを書き換える様子が観測されました。これは単なる記録に基づく解決ではなく、環境への適応による真の「進化」を実現していることを裏付けています。
