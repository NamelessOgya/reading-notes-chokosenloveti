# REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS

## 背景
大規模言語モデル（LLM）は「Chain-of-Thought（CoT）」のような思考プロセス（Reasoning trace）を生成させる手法により推論能力を飛躍的に高めたが、**外部環境へのアクセス（インタラクト）を持たないため知識が更新されず**、事実誤認（Hallucination）や情報の欠如によるエラーが発生しやすい課題があった。
一方で、エージェントにとにかく行動（Action）の予測のみを行わせるアプローチは、環境からの情報は得られても**それを言語的に保持・内省する推論プロセス（ワーキングメモリ等）を持たないため**、複雑なタスクでの長期的計画の策定や予測外のエラーからの動的な復帰において困難を抱えていた。

（※参考：ReAct論文内で比較・言及されている、行動予測やプランニングに関する主な先行研究とその課題）
| 論文名 | 発表年 | 手法概要と、ReAct論文で指摘されている「推論・メモリ・環境アクセス」の制約 |
| :--- | :--- | :--- |
| Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan) | 2022 | 言語モデルにロボットの可能な行動候補を予測・スコアリングさせる手法。環境の利用可能性は考慮するが、**抽象的な高次目標の推論や、計画を維持・修正するためのワーキングメモリ機能を持たない**ため、複雑なエラー復帰が困難。 |
| WebGPT: Browser-assisted question-answering with human feedback | 2021 | 言語モデルを用いてWebブラウザと対話し検索行動を行う手法。外部環境へのアクセスは持つが、**明示的な自己推論プロセス（Inner reasoning trace）をモデルに出力させない**まま人間の強化学習に依存しているため、自立的な意思決定と情報保持の柔軟性に欠ける。 |
| Inner Monologue: Embodied Reasoning through Planning with Language Models | 2022 | サクセス判定など環境のフィードバックをテキストとして注入するアプローチ。環境との対話ループはあるものの、環境情報をエージェント自身の**内省的・能動的な思考（真のワーキングメモリやInner thoughts）として保持・議論するメカニズムを持たない**とReActで指摘されている。 |
| Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 2022 | 言語モデルから「どう行動するか」という行動知識のみをそのまま一方向で抽出する手法。**外部環境との対話ループ（Observation）も、推論状態の保持機能（Memory）も確立されていない**ため、動的な状況変化に対応できない静的パラダイム。 |
| Keep CALM and Explore: Language Models for Action Generation in Text-based Games | 2020 | テキストベースのゲームにおいて観測情報から直接「次にとるべき行動候補」のみを予測する。**長期的な戦略を言語ベースで計画・一時記憶するワーキングメモリがない**ため、行動探索が行き当たりばったりになりやすい。 |

本研究は、言語モデル内でこの思考（Reasoning）と行動（Acting）を密接に連携（Synergize）させる汎用的な手法である「ReAct」を提案し、外部の知識ベース（Wikipedia API等）からの情報収集と思考による文脈推論を統合することでこれらの問題の解決を図る。

## 手法

本論文が提案する「手法」は、大きく２つの革新的なプロンプティング・アプローチによって構成されている。

### 1. ReActシステムの基本構造（推論と行動の同期）
ReAct（Reasoning and Acting）は、環境とやり取りしながら言語的な思考プロセスと特定のアクションを交互に生成させるプロンプト手法である。モデルに対し、自己完結の推論だけでなく、少数の動作軌跡（Few-shot demonstrations）をIn-Context Learningとして提示することで、行動と推論の相互サイクルを強力に誘発する。

特定の課題を解く過程において、以下のようにプロンプト上で3つのステップをループさせるアーキテクチャを持つ。

#### 1-1. Thought (思考 / 推論)
観察（Observation）結果をもとに、次に取るべき行動を計画・修正したり、得られた情報を整理して一時的に保持（ワーキングメモリとしての役割）するプロセス。

**プロンプトにおける出力イメージ（モデルの自律生成）：**
```text
Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.

Thought 1: I need to search Nikolaj Coster-Waldau and find if he has worked with the Fox Broadcasting Company.
```

#### 1-2. Action (行動)
思考（Thought）の結果に基づき、外部環境（例：Wikipediaの検索エンジン、物理シミュレータ、Web環境など）に対して具体的な操作コマンドを発行するプロセス。

**プロンプトにおける出力イメージ（モデルの自律生成）：**
```text
Action 1: Search[Nikolaj Coster-Waldau]
```

#### 1-3. Observation (観察)
発行した行動（Action）の結果を外部環境（APIやシステム）から受け取り、そのテキスト情報をプロンプトの後続コンテキストとして統合するプロセス。モデルはこの回答テキストをGroundingし、再びThoughtを生成して推論を更新する。

**プロンプトにおける出力イメージ（環境からのフィードバックと、それを受けた最終推論）：**
```text
Observation 1: Nikolaj William Coster-Waldau (born 27 July 1970) is a Danish actor... He played a detective in the short-lived Fox television series New Amsterdam (2008), and appeared in the 2009 Fox television film Virtuality...

Thought 2: Because he "appeared in the 2009 Fox television film Virtuality", he should have worked with the Fox Broadcasting Company.
Action 2: Finish[SUPPORTS]
```

このように、環境からの事実情報に基づきながら（Grounding）推論を少しずつ進めることで、自己完結したまま推論が暴走しエラーが伝播（ハルシネーション）するのを防ぐ。また、検索が失敗した場合の柔軟な例外処理や、複数回にまたがる外部知識のパズル的な補完も実現している。
モデル自身のパラメータ更新（ファインチューニング）は一切行わず、このような模範的な軌跡（Trajectory）のテキストをプロンプトの先頭に数個書き込むだけで機能する点が最大の特徴である。

### 2. プロンプト・パラダイム間のメタ・ルーティング（ハイブリッド戦略）
本論文が提示したもう一つの極めて重要なアプローチが、外部探索特化の上記「ReAct」と、内部推論特化の「Chain-of-Thought（CoT-SC）」という、相反する2つの**プロンプティング・パラダイムを動的に切り替えるパイプライン機構**である。
単一ループのReActにとどまらず、手法として規定された動的なルーティング・アルゴリズムは以下の2通りである。

#### 2-1. Reason $\to$ ReAct ルーティング（確信度ベースの外部検索）
- **プロセス**: まず問題文を `CoT-SC`（自己一貫性付き推論）のプロンプトに入力し、LLMに独立した複数の推論経路と解答を並列生成させる。
- **ヒューリスティックによる判定**: 出力された複数の解答から多数決（Majority Voting）を取る。もし、最も多かった解答の獲得票数（確信度）が**あらかじめ設定した閾値を下回った場合**、「モデル内部の知識が不足している（＝ハルシネーションを起こす危険性が高い）」と判定する。
- **フォールバック**: 上記の中途半端な内部推論プロセスを破棄し、外部環境へのアクセス機能を持つ `ReAct` のプロンプトへ問題を投げ直し、実際の検索を通じた事実ベースの裏付けを行わせる。

#### 2-2. ReAct $\to$ Reason ルーティング（スタック検出ベースの推論）
- **プロセス**: まず問題文を `ReAct` プロンプトに入力し、ThoughtとActionを繰り返してWikipedia等の外部環境を自律探索させる。
- **ヒューリスティックによる判定**: 検索クエリの生成ミスなどで有用な情報が得られず、**設定した規定ステップ・アクション数（例：最大7ターン）を超過しても最終タスク完了（`Finish[]`）に達しない場合**、「探索ループがスタックしている（行き詰まっている）」と判定して動作を強制停止する。
- **フォールバック**: 検索ループを打ち切り、今度は推論力に大きく優れる `CoT-SC` に問題を切り替え、LLM自身がパラメーター内に持つ膨大な内部知識を活用して強引に解答を推測・決定させる。

こうした「多数決による閾値判定」や「アクション数のタイムアウト」といった、非常に単一で明確なルールのルーティングをプロンプト制御スクリプトとして設けるだけで、双方の手法とパラダイムの致命的な弱点（ハルシネーションと探索のスタック）を完璧に補完し合う設計思想を提唱している。

## 結果

本稿ではHotpotQA（質問応答）、FEVER（事実検証）、ALFWorld（テキストベースゲーム）、WebShop（Eコマースナビゲーション）等において実験を行い、以下の中核的な知見を得た。

### 評価タスクの概要
- **HotpotQA（質問応答）**: 「Xという映画の監督が手がけた別の映画の主演は誰か？」のように、複数の情報源（Wikipedia記事）を論理的につなぎ合わせる「マルチホップ推論」が必要なタスク。
- **FEVER（事実検証）**: 与えられた短い主張（Claim）が、Wikipediaなどの外部事実と照らし合わせて「SUPPORTS（支持・真）」「REFUTES（反証・偽）」「NOT ENOUGH INFO（情報不足）」のいずれに該当するかを検証・判定するタスク。
- **ALFWorld（テキストベースゲーム）**: 「きれいなレタスをダイニングテーブルに置く」などの目標が与えられ、テキストで表現された仮想空間（キッチンなど）を探索し、「冷蔵庫へ行く（go to fridge）」「レタスを取る（take lettuce）」「シンクで洗う（clean）」といったコマンド入力でクリアを目指す。
- **WebShop（Eコマース）**: 「50ドル未満で特定の成分の敏感肌用デオドラントが欲しい」といった自然言語の複雑な要求に対し、ECサイト上で「商品の検索」「ページの移動」「フレーバー等のオプションの選択」「購入ボタンのクリック」など一連のWebブラウジング操作を自律的に達成するタスク。

### 1. タスク成功要因と失敗要因の分析
HotpotQAにおける推論モデルのエラーモードを分析した結果をTable 1に示す。

**Table 1: Types of success and failure modes of ReAct and Reason on HotpotQA**
| | Type | Definition | ReAct | Reason |
|:---|:---|:---|:---|:---|
| **Success** | True positive | Correct reasoning trace and facts | 94% | 86% |
| | False positive | Hallucinated reasoning trace or facts | 6% | 14% |
| **Failure** | Reasoning error | Wrong reasoning trace (including failing to recover from repetitive steps) | 47% | 16% |
| | Search result error | Search return empty or does not contain useful information | 23% | - |
| | Hallucination | Hallucinated reasoning trace or facts | 0% | 56% |
| | Label ambiguity | Right prediction but did not match the label precisely | 29% | 28% |

- **考察**: Reason（CoT）の最大の失敗要因は「Hallucination (56%)」であったが、ReActは外部百科事典への検索行動を通じてGroundingを行うため、Hallucination由来の失敗を **0%** に激減させた。一方、ReAct特有の失敗パターンとして、外部検索結果のエラー（23%）や、検索と推論を往復する中での「一貫した思考の喪失・ループ（Reasoning errorが47%）」が増加するというトレードオフが明らかになった。

### 2. 推論と行動のハイブリッド化によるSoTA達成

各手法（ReActとCoT）はそれぞれ致命的な弱点を持っているが、これらは相互に補完可能である。

| 手法 | 強み | 弱点・課題 |
| :--- | :--- | :--- |
| **ReAct** | Wikipediaなどの外部の正確な知識にアクセスし、事実に基づいた推論（Grounding）が可能 | 検索クエリの生成ミスやAPIエラーで有用な情報が得られず、検索ループにはまって抜け出せなくなる |
| **CoT-SC** | 大規模言語モデル（LLM）が持つ膨大な内部知識と、高度な論理推論力を引き出せる | パラメータ外の知識や不確実なことでも、確信を持って嘘の事実を出力・正当化してしまう（ハルシネーション） |

この特性の違いを利用するため、論文では2つの生成手法を条件付きで切り替える**ハイブリッド（フォールバック）戦略**を検証し、Table 2の通り単体手法を大きく上回る最高性能を獲得した。

**Table 2: PaLM-540B prompting results on HotpotQA and Fever**
| Prompt Method | HotpotQA (EM) | Fever (Acc) |
|:---|:---|:---|
| Standard | 28.7 | 57.1 |
| Reason (CoT) | 29.4 | 56.3 |
| Reason + Self-Consistency (CoT-SC) | 33.4 | 60.4 |
| Act | 25.7 | 58.9 |
| ReAct | 27.4 | 60.9 |
| Reason $\to$ ReAct (ハイブリッド) | 34.2 | **64.6** |
| ReAct $\to$ Reason (ハイブリッド) | **35.1** | 62.0 |
| *Supervised SoTA* | *67.5* | *89.5* |

#### ハイブリッド手法の具体的なスイッチング（フォールバック）条件

以下の簡潔なルール（ヒューリスティクス）を設けるだけで、各単体手法の弱点が見事にカバーされている。

1. **Reason $\to$ ReAct 戦略（CoTからのフォールバック）**
   - **第一ステップ**: まず推論能力の高い `CoT-SC` に解答候補を複数サンプリングさせる。
   - **発動条件**: 生成された解答間で意見が割れ、多数決判定で**一定の確信度（閾値）を下回った場合**（＝ハルシネーションや知識不足の危険性が高い場合）。
   - **フォールバック**: 外部検索が得意な `ReAct` を強制起動し、外部情報による裏付け・事実確認を行う。

2. **ReAct $\to$ Reason 戦略（ReActからのフォールバック）**
   - **第一ステップ**: まず `ReAct` を用いて外部への検索・情報収集を試みる。
   - **発動条件**: 指定された最大アクション数（例：7ステップ）を経過しても有用な情報に行き着けず、**探索がスタックしてしまった場合**。
   - **フォールバック**: 強力な自己推論モデルである `CoT-SC` に処理を引き継ぎ、LLMが元々持つ内部パラメトリック知識を用いて強引に解答を推測・決定させる。

> [!TIP]
> **考察のまとめ**
> 言語モデルにおける「強固な内部推論力（CoT）」と「正確な外部知識へのアクセス（ReAct）」は、ごく簡単な条件分岐ルールを用いるだけで片方の弱点を完璧に消し去り、非常に高い相乗効果（Synergizing）を発揮することが本研究で実証された。

### 3. モデルアーキテクチャスケーリングの影響
GPT-3とPaLM-540Bで比較した結果をTable 4に示す。

**Table 4: ReAct prompting results using PaLM-540B vs. GPT-3**
| | PaLM-540B | GPT-3 (text-davinci-002) |
|:---|:---|:---|
| **HotpotQA (exact match)** | 29.4 | **30.8** |
| **ALFWorld (success rate %)** | 70.9 | **78.4** |

- **考察**: 大規模なPaLM-540Bでも効果が見られるが、GPT-3（`text-davinci-002`）のほうが命令追従性能が高くより良い成績を残しており、基盤モデルの能力にも依存することが示されている。

### 4. 環境探索・意図決定タスクでの優位性
環境への操作が求められるALFWorld（日常タスク）やWebShop（Eコマース）での結果をTable 8に示す。

**Table 8: AlfWorld task-specific success rates (%) and WebShop results**
*(AlfWorld task-specific success rates)*
| Method | Pick | Clean | Heat | Cool | Look | Pick 2 | All | 
|:---|---:|---:|---:|---:|---:|---:|---:|
| Act (best of 6) | 88 | 42 | 74 | 67 | 72 | **41** | 45 |
| ReAct (avg) | 65 | 39 | 83 | 76 | 55 | 24 | 57 |
| **ReAct (best of 6)** | **92** | 58 | **96** | 86 | **78** | **41** | **71** |
| ReAct-IM (avg) | 55 | 59 | 60 | 55 | 23 | 24 | 48 |
| ReAct-IM (best of 6) | 62 | **68** | 87 | 57 | 39 | 33 | 53 |
| BUTLER_g (best of 8) | 33 | 26 | 70 | 76 | 17 | 12 | 22 |
| BUTLER (best of 8) | 46 | 39 | 74 | **100** | 22 | 24 | 37 |

*(Webshop Score and Success Rate)*
| Method | Score | SR |
|:---|:---|:---|
| Act | 62.3 | 30.1 |
| **ReAct** | **66.6** | **40.0** |
| IL | 59.9 | 29.1 |
| IL+RL | 62.4 | 28.7 |
| *Human/Expert* | *82.1* | *59.6* |

- **考察**: これら強化学習領域のタスクにおいても、ReActは目標の確認（Thought）と環境への行動（Act）を組み合わせることで、模倣学習（IL）や強化学習（RL）を施した専用の強力なベースラインを凌駕し、非常に汎用性が高いことが実証された。

### 論文抽出図版資料の提示
抽出された全ての画像（`teaser-new.png`や各種グラフ）を示す。本手法がReasonとActを効果的に同期（Synergizing）させている様子や、スケーリング則、人間の介入による効果の可視化、そしてデータの精緻化などを示している。

![Teaser Figure](./images/teaser-new.png)
![CoT vs ReAct scale](./images/cots_scale.png)
![Fever CoT vs ReAct scale](./images/fever_cots_scale.png)
![Date](./images/date.png)
![Fine-Tune](./images/hotpot_finetune.png)
![Human Edit](./images/human_edit.png)

(※これらの画像は、手法のコンセプトや、Promptの試行回数（Reason+Self-Consistencyのサンプリング数）に対するReActの優位性、また人間によるフィードバック介入の結果やファインチューニングに対するデータ効率の高さなどを示す論文の主要Figureである。)

## chokosenlovetiの考察

### 本論文の新規性

本論文（ReAct）の最も特筆すべき「新規のポイント（貢献）」と「大局的な意義」は以下の点に集約される。

#### 1. 「推論（思慮）」と「行動」の単一モデル内での完全同期（Synergizing）
初期のLLMアプリケーション開発においては、エージェントを動かす「強化学習的な行動予測（Act）」と、内部的に計算・推論を行う「Chain-of-Thought（Reason）」は完全に別の研究パラダイムとして扱われていた。ReActの真の革新性は、これら行動と推論を別々のモジュールやシステムに切り離さず、**自然言語（純粋なテキストプロンプト）という共通のインターフェースを用いて、単一のLLMの中で交互かつ自律的に発生させた点**にある。これにより、LLMが「外部の事実（結果）を見て、自分の計画を内省・修正する」という人間のようなフィードバックループ（自律的なワーキングメモリ機能）を初めて獲得した。

#### 2. “プロンプト・パラダイム間”のメタ・ルーティングの確立（ハイブリッド戦略）
「条件による処理のフォールバック」や「複数モデルの使い分け・ルーティング」といった概念自体は、既存の検索ベースQAアーキテクチャやシステム開発等においても存在していた。しかし本論文の画期的な点は、外部環境探索（ReAct）と内部推論（CoT）という、当時対立しがちであった2つの最先端の**プロンプティング・パラダイム**を、「CoT-SC（自己一貫性）の多数決で意見が割れたかどうか」などのモデル内発的な指標のみを用いた極めてシンプルなルールで統合し、1つのLLMのプロンプト上で動的に切り替えた（ルーティングした）点にある。これにより、いかに強力なLLMであっても「外部の事実に基づかなければハルシネーションを起こす」という限界を綺麗にカバーし、相互補完がいかにブレイクスルーを生むかを実証した。

#### 3. 「LLMと逐次改善」系譜における基盤・起源としての役割
「テキストで状況を観察し、自身の推論やプロセスを修正し、次の最適手を採用する」というReActの概念は、本まとめテーマである「LLMと逐次改善」の系譜において極めて重要なマイルストーンである。のちに発展する **ProTeGi** や **TextGrad** のような「テキストフィードバック（エラー）を受けてプロンプト自体を自己微分・修正する手法」、および **AgentBreeder** 等の「マルチエージェント環境下でLLM自身が過去の失敗をメタ認識し、自己改善していく（Self-Reflection）という手法」はすべて、このReActが開拓した「自然言語ベースの推論と環境アクセスの往復ループ」を起源（あるいは不可欠なコンポーネント）として発展している。
