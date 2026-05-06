# CoLLM: Integrating Collaborative Embeddings into Large Language Models for Recommendation

## 背景
LLMベースのレコメンドシステム（LLMRec）は、テキストの意味理解（セマンティクス）に依存しているため、ユーザーとアイテム間の「協調情報（Collaborative Information）」を十分に反映できないという課題がある。テキスト上は似ているアイテムでも、実際にそれを消費するユーザー層が異なるケースが存在し、それをテキストのみで区別するのは困難である。一方、LLMの持つ高度な汎用能力や推論能力を保つため、完全なファインチューニングは敬遠されがちであり、ローカルのデータセット特有の協調情報が十分に学習されない。このような背景から、LLMRecに対してどのように協調情報を取り込むかが重要な研究課題となっている。

## 手法
本論文では、外部の従来型協調モデル（MF、LightGCN、SASRec、DINなど）を用いて協調情報を抽出し、それをLLMに統合する「CoLLM」を提案している。
具体的には以下の4つのフェーズで処理が行われる。

1. **協調ベクトルの事前抽出 (Pre-training / Extraction)**
   従来型のレコメンドモデルを用いて、ユーザーとアイテムの行動履歴に基づく「協調ベクトル（Collaborative Embeddings）」を事前に学習・抽出する。

2. **プロンプトへのプレースホルダの組み込み (Prompt Construction)**
   LLMへの入力プロンプトに、テキスト情報だけでなく `<UserID>` と `<TargetItemID>` というプレースホルダを持たせ、ここに抽出した協調ベクトルを直接注入する枠組みを作る。

   **【実際のプロンプトの構成例】**
   > The user `<UserID>` has interacted with the following items in the past:
   > - 1. Toy Story (1995)
   > - 2. Jumanji (1995)
   > 
   > Based on the above interaction history, will this user like to interact with the target item `<TargetItemID>` (The Lion King (1994))?
   > Please answer Yes or No.
   
   ※ この `<UserID>` と `<TargetItemID>` の部分には、単なる文字列が入るのではなく、**Step 1で抽出され、CIEモジュールでLLM次元に変換された「協調ベクトル（数値データの配列）」**が、1つの単語トークンのような形で直接埋め込まれます。

3. **CIE（Collaborative Information Encoding）モジュールによる次元変換**
   従来モデルから抽出した協調ベクトルの次元数とLLMのトークン埋め込みの次元数を合わせるため、多層パーセプトロン（MLP）を用いたマッピング層（CIEモジュール）を通す。これにより協調情報をLLM空間へと投影する。

4. **2段階チューニング（Two-step Tuning）**
   テキストの意味と協調情報が競合しないよう、段階的に学習を行う。
   - **Step 1: タスクの適応（LoRAチューニング）**
     プレースホルダを外し、テキスト情報のみを用いてLoRA（Low-Rank Adaptation）を学習する。LLM本体の重みは凍結し、推薦タスク自体にLLMを適応させる。
     $$
     \hat{\Theta}^{\prime}  = argmin_{\Theta^{\prime}} \sum_{(u,i,y)\in \mathcal{D}} \ell(h_{\hat{\Theta}+\Theta^{\prime}}(E_t),y)
     $$
   - **Step 2: 協調情報の統合（CIEモジュールのチューニング）**
     LLM本体とStep 1で学習したLoRAを完全に固定（凍結）する。完全なプロンプトを入力し、CIEモジュール（マッピング層）のみをチューニングすることで、抽出された協調情報がLLMにとって利用可能な形式になるようにする。
     $$
     min_{\Omega} \sum_{(u,i,y)\in \mathcal{D}} \ell(h_{\hat{\Theta}+\hat{\Theta}^{\prime}}(E),y)
     $$

   **【なぜ同時に学習させないのか？】**
   論文内の比較実験（Ablation Study）において、LoRA（テキスト適応）とCIEモジュール（協調情報のマッピング）を**最初から同時に一括学習させると精度が著しく低下する**ことが示されている。LLMにとって協調ベクトルは未知の言語（エイリアントークン）のようなものであるため、推薦タスクのフォーマットを理解する前に未知のベクトルを注入すると、LLM内部で処理がバッティングし学習が崩壊してしまう。そのため、「テキストによるタスクルールの固定（Step 1）」と「協調情報の翻訳（Step 2）」を明確に切り離すこのアプローチが不可欠となっている。



### CoLLMのアーキテクチャとチューニングフロー（図解）
![Figure 1](./images/Figure1.png)
![Figure 2](./images/Figure2.png)

> **[筆者の見解]**
> Figure 1およびFigure 2は、CoLLMがテキスト情報と協調情報をどのように統合しているかを示しています。注目すべきは、ユーザーIDやアイテムIDを単純にテキストとしてLLMに入力するのではなく、外部の協調モデル（MF等）で一度ベクトル化し、CIEモジュール（マッピング層）を介して「LLMが解釈できる特殊トークン」として注入している点です。この設計により、LLMの持つ豊富な一般知識（テキスト理解）と、ローカルデータに特化したユーザーの行動パターン（協調情報）を、お互いを邪魔することなくシームレスに結合できています。

## 結果
- **全体性能の向上**: CoLLMは評価された2つのデータセット（ML-1M, Amazon-Book）において、LLMRecのベースライン（TALLRecなど）や従来型の手法を上回る性能（AUC, UAUC等）を示した。
  ![RQ1_1](./images/RQ1_1.png)
  ![RQ1_2](./images/RQ1_2.png)
  ![RQ1_3](./images/RQ1_3.png)
  ![RQ1_4](./images/RQ1_4.png)
  > **[筆者の見解]**
  > RQ1のグラフ群は、従来モデル（MFやLightGCNなど）単体と比較して、CoLLMがどれだけ精度を底上げできているかを明確に示しています。特にデータがスパース（疎）なケースにおいて、LLMの推論能力が協調モデルの弱点を補っていることが読み取れます。LLM単体（TALLRecなど）よりも精度が高いのは、やはり行動履歴の直接的な表現（協調ベクトル）が強力に効いている証拠です。

- **ウォームスタートとコールドスタートの両立**: LLMRecは元々コールドスタートに強いが、CoLLMはそれに加えて、従来モデルの強みであるウォームスタートシナリオにおいても大幅な性能改善を達成し、両方のシナリオで高い精度を発揮することが確認された。
- **アーキテクチャの有効性**: CIEモジュールを除外したり、トークンを単なるIDとしてLLMに直接学習させようとすると精度が低下した。これにより、外部モデルを用いた低ランクの協調情報マッピングと2段階チューニング（テキストでの能力獲得後に協調情報を適応させる流れ）が、汎化性能の低下を防ぎつつ効果的なレコメンドを可能にする重要な設計であることが示された。
  ![RQ3_1](./images/RQ3_1.png)
  ![RQ3_2](./images/RQ3_2.png)
  > **[筆者の見解]**
  > RQ3のAblation（切り分け）検証の図は、本論文のキモである「2段階チューニング（Two-step Tuning）」の必然性を証明しています。テキストと協調ベクトルを最初から同時に学習させてしまうと、LLM内部で意味表現が衝突（Catastrophic Forgettingに近い現象）を起こし、精度が落ちてしまいます。テキストタスクへの適応（LoRA）を先に行い、その後にLLMを凍結してCIE層のみを最適化するという段階的アプローチが、LLMRecにおける情報の統合最適解の一つであることを強く裏付けています。


## 考察 (chokosenloveti)

本手法（CoLLM）を実運用やシステム設計の観点から考察すると、**「LLMの推論能力」と「日々変動する行動履歴（協調情報）」のライフサイクルを完全に分離できている点**が最大のメリットとして挙げられます。

* **協調情報が更新されてもLLMの再学習は不要**:
  * ユーザーの新しいクリックや購買といった行動履歴が発生し、協調情報に更新があった場合でも、**LLM側（LLM本体およびStep 1で学習したLoRA）の再ファインチューニングは基本的に不要**です。
  * 行動履歴の更新は、外部の軽量な従来型モデル（MFやLightGCNなど）の再学習・差分更新によって吸収されます。
  * もし外部モデルをゼロから再学習してベクトル空間全体が変わってしまった場合であっても、再学習が必要になるのは「Step 2」の**CIEモジュール（数十〜数百次元を変換するだけの軽量なMLP層）のみ**です。重いLLM側の学習を回す必要はありません。

* **運用コストとスケーラビリティの両立（MLOps的視点）**:
  * 過去の研究のように「ユーザーIDを文字列としてLLMに覚えさせる」アプローチでは、新規ユーザーが増えるたびにLLMの語彙追加や再学習が必要になり、実運用が破綻しやすいという問題がありました。
  * CoLLMは、テキストの意味理解という「静的で汎用的な能力」はLLMに任せ、ユーザー同士のつながりという「動的でローカルな情報」は外部モデル＋CIE層に外出ししています。これにより、計算コストを抑えながら高頻度なレコメンドモデルの更新を可能にする、非常に実用性の高いアーキテクチャ設計だと言えます。


* **時間経過に伴う嗜好の変化（Concept Drift）への頑健性**:
  * 実運用を想定した論文内の検証（Drift perspective）として、データセットを時間軸で区切り「過去のデータで学習し、未来のデータで予測する（例：過去10ヶ月分で学習し、未来5ヶ月分でテストする）」という実験が行われています。
  * ユーザーの好みが時間とともに変化していく条件下でも、CoLLMは従来モデルと比較して高い精度を維持できることが示されました。これは、LLMが持つ汎用的な推論能力が、時間の経過によるユーザー行動の変化（コンセプトドリフト）に対する強力な緩衝材として機能していることを示唆しています。

### 論文中の表（Tables）

以下は、論文から抽出された主要な結果の表です。（不要なLaTeXコード・コメントアウトされた旧形式の表は削除・整形済み）

#### Table 1: Statistics of the evaluation datasets
| Dataset | #Train | #Valid | #Test | #User | #Item |
|---|---|---|---|---|---|
| ML-1M | 33,891 | 10,401 | 7,331 | 839 | 3,256 |
| Amazon-Book | 727,468 | 25,747 | 25,747 | 22,967 | 34,154 |

#### Table 5: Overall performance comparison
| Methods | ML-1M AUC | ML-1M UAUC | ML-1M NDCG | ML-1M Rel. Imp. | Amazon-Book AUC | Amazon-Book UAUC | Amazon-Book NDCG | Amazon-Book Rel. Imp. |
|---|---|---|---|---|---|---|---|---|
| **Collab.** MF | 0.6482 | 0.6361 | 0.8447 | 10.3% | 0.7134 | 0.5565 | 0.8194 | 12.8% |
| **Collab.** LightGCN | 0.5959 | 0.6499 | 0.8564 | 13.2% | 0.7103 | 0.5639 | 0.8245 | 11.0% |
| **Collab.** SASRec | 0.7078 | 0.6884 | 0.8612 | 1.9% | 0.6887 | 0.5714 | 0.8244 | 8.4% |
| **Collab.** DIN | 0.7166 | 0.6459 | 0.8496 | 4.9% | 0.8163 | 0.6145 | 0.8419 | 3.2% |
| **LM+Collab.** CTRL (DIN) | 0.7159 | 0.6492 | 0.8559 | 4.6% | 0.8202 | 0.5996 | 0.8363 | 4.2% |
| **LLMRec** ICL | 0.5320 | 0.5268 | 0.8114 | 33.8% | 0.4820 | 0.4856 | 0.7917 | 48.2% |
| **LLMRec** Prompt4NR (Vicuna) | 0.7071 | 0.6739 | 0.8663 | 2.7% | 0.7224 | 0.5881 | 0.8346 | 10.4% |
| **LLMRec** TALLRec | 0.7097 | 0.6818 | 0.8711 | 1.8% | 0.7375 | 0.5983 | 0.8361 | 8.2% |
| **Ours** CoLLM-MF | 0.7295 | 0.6875 | 0.8714 | - | 0.8109 | 0.6225 | 0.8457 | - |
| **Ours** CoLLM-LightGCN | 0.7100 | 0.6967 | 0.8740 | - | 0.8026 | 0.6149 | 0.8411 | - |
| **Ours** CoLLM-SASRec | 0.7235 | 0.6990 | 0.8765 | - | 0.7746 | 0.5962 | 0.8361 | - |
| **Ours** CoLLM-DIN | 0.7353 | 0.6923 | 0.8735 | - | 0.8245 | 0.6474 | 0.8550 | - |

#### Table 8: Results of the ablation studies over CoLLM with respect to the CIE module
| Methods | ML-1M AUC | ML-1M UAUC | Amazon-Book AUC | Amazon-Book UAUC |
|---|---|---|---|---|
| CoLLM-MF | 0.7295 | 0.6875 | 0.8133 | 0.6314 |
| w/o CIE | 0.7097 | 0.6818 | 0.7375 | 0.5983 |
| w/ UI-token | 0.7214 | 0.6563 | 0.7273 | 0.5956 |

#### Table 9: Overall performance of CoLLM with different tuning strategies
| Tuning Methods | ML-1M AUC | ML-1M UAUC | Amazon-Book AUC | Amazon-Book UAUC |
|---|---|---|---|---|
| Default | 0.7295 | 0.6875 | 0.8109 | 0.6225 |
| T1 | 0.7360 | 0.6946 | 0.8154 | 0.6139 |
| T2 | 0.7418 | 0.6906 | 0.8288 | 0.6352 |
| T3 | 0.7131 | 0.6661 | 0.8104 | 0.5753 |

#### Table 10: Training and Total Inference Time Comparison
| Dataset | Train Time (ML-1M) | Train Time (Amazon-Book) | Inference Time (ML-1M) | Inference Time (Amazon-Book) |
|---|---|---|---|---|
| TALLRec | 32min | 354min | 72s | 360s |
| CoLLM-MF | 36min | 418min | 82s | 398s |
| Δ (Relative Cost) | 13% | 18% | 14% | 11% |

#### Table 19: Performance comparison on Qwen2-1.5B backbone
| Metric | ML-1M AUC | ML-1M UAUC | Amazon-Book AUC | Amazon-Book UAUC |
|---|---|---|---|---|
| MF | 0.6482 | 0.6361 | 0.7134 | 0.5565 |
| TALLRec | 0.7027 | 0.6638 | 0.7256 | 0.5830 |
| CoLLM-MF | 0.7354 | 0.6950 | 0.8068 | 0.6147 |

#### Table 20: Ensemble results on the AUC metric
| Methods | Single MF | Single TALLRec | Single CoLLM-MF | Ensemble MF+TALLRec | Ensemble MF+CoLLM-MF |
|---|---|---|---|---|---|
| ML-1M | 0.6482 | 0.7097 | 0.7295 | 0.7239 | **0.7364** |
| Amazon-book | 0.7134 | 0.7375 | 0.8109 | 0.7782 | **0.8112** |
