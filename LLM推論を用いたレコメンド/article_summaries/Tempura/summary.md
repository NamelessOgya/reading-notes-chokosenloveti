# Tempura: Training-Free Temporal Prompting for LLM-based Recommendation

## 背景
大規模言語モデル（LLMs）は一般的なタスクで高いゼロショット能力を示すものの、シーケンシャルレコメンドのような時間的データを扱うタスクにおいて、時間的な情報（Temporal information）の認識や利用が苦手であるという課題がある。実際、既存のLLMベースのレコメンド手法に対して、ユーザの過去のインタラクション履歴の順序をランダムにシャッフルしても精度がほとんど変わらないことが経験的に判明している。この問題を解決し、LLMの時間的認識能力（Temporal Awareness）を向上させるために、人間の認知プロセスに着目し、ドメイン非依存かつ追加学習不要（Training-Free）なプロンプトフレームワーク「Tempura (Temporal Prompting)」を提案した。

## 手法
Tempuraは以下の3つのモジュールから構成される。
![Tempura Framework Overview](./images/overview.png)

1. **In-Context Learning (ICL) モジュール**:
   学習済みのシーケンシャルレコメンドモデル（Transformerベース等）における学習プロセス（過去のアイテム群から次のアイテムを予測し、その誤差で更新する流れ）と、LLMのインコンテキスト学習のアテンション機構が数式上アナロジーを持つことに着目し、過去のインタラクション履歴をIn-Contextデモンストレーションとして活用する。
   - **PCL (Proximal temporal demonstrations)**: ユーザの直近のアイテム履歴をICLの例（few-shot）として与え、直近の興味の推移を捉える。
   - **GCL (Global interest demonstrations)**: 直近の履歴だけでなく、過去の履歴全体からランダムにサンプリングしたアイテムをコンテキストに含め、長期的な興味（Global interest）を保持する。
   ![In-Context Learning Strategy](./images/incontext.png)

2. **Temporal Structure Analysis モジュール**:
   人間の脳が時間的構造に敏感であるという神経科学の知見に基づき、入力シーケンスに対して明示的な構造分析を行う。時間的に近く、かつ特徴が類似しているアイテム同士をクラスタリングし、過去のインタラクションの年代記的な推移を明示的なテキストプロンプト（概要）として付与する。
   ![Temporal Structure Analysis](./images/cluster.png)

3. **Prompt Ensemble モジュール**:
   上記のPCL, GCL, Clusterなどのプロンプト戦略を単一の長文プロンプトとして結合するとLLMが重要な情報を見落とすリスク（Lost in the Middle）がある。そのため、人間の「拡散的思考 (Divergent thinking)」を模倣し、各プロンプト戦略から得られた別々のランキング結果をBorda count的なスコアリングで統合（アンサンブル）する。

## 結果
Tempuraの有効性を検証するため、ML-1MおよびAmazon Review (Games, Kindle) データセットを用いて評価を行った。

### テーブルデータによる性能比較
以下に、原著から抽出した実験結果のテーブルをすべて記載する。

**Table 1: Performance comparison on ML-1M and Games datasets.**
| Method | ML-1M N@1 | ML-1M N@5 | ML-1M N@10 | ML-1M N@20 | Games N@1 | Games N@5 | Games N@10 | Games N@20 |
|---|---|---|---|---|---|---|---|---|
| BM25 | 4.00 | 13.14 | 20.53 | 33.70 | 16.50 | 30.09 | 37.19 | 46.11 |
| UniSRec | 9.00 | 20.08 | 26.72 | 38.24 | 19.50 | 34.86 | 40.82 | 49.15 |
| VQ-Rec | 9.50 | 19.52 | 27.11 | 38.72 | 5.50 | 16.76 | 25.27 | 36.42 |
| Sequential | 21.43 | 42.57 | 48.59 | 53.28 | 24.12 | 47.26 | 53.03 | 56.56 |
| RF | 26.56 | 45.99 | 51.27 | 55.98 | 25.63 | 50.02 | 53.72 | 57.84 |
| ICL | 26.40 | 47.51 | 53.32 | 57.23 | 26.00 | 49.68 | 53.63 | 57.38 |
| Cluster | 27.00 | 45.82 | 52.04 | 56.21 | 26.15 | 47.41 | 52.39 | 57.19 |
| FCL | 29.16 | 48.35 | 54.11 | 58.44 | 29.00 | 51.56 | 55.11 | 59.17 |
| Ours (Concat.) | **31.50** | **49.68** | **54.96** | **59.16** | 19.00 | 45.20 | 50.01 | 53.96 |
| Ours (Ensemble) | 30.50 | 48.35 | 54.28 | 58.56 | **35.50** | **53.89** | **58.74** | **62.35** |

**Table 2: Performance comparison on ML-1M and Amazon Review datasets.**
| Method | ML-1M N@1 | ML-1M N@5 | ML-1M N@10 | Games N@1 | Games N@5 | Games N@10 | Kindle N@1 | Kindle N@5 | Kindle N@10 |
|---|---|---|---|---|---|---|---|---|---|
| BM25 | 4.00 | 13.14 | 20.53 | 16.50 | 30.09 | 37.19 | 6.50 | 18.07 | 24.96 |
| UniSRec | 9.00 | 20.08 | 26.72 | 19.50 | 34.86 | 40.82 | 5.00 | 16.21 | 25.03 |
| VQ-Rec | 9.50 | 19.52 | 27.11 | 5.50 | 16.76 | 25.27 | 4.30 | 14.22 | 23.58 |
| Sequential | 21.43 | 42.57 | 48.59 | 24.12 | 47.26 | 53.03 | 10.20 | 27.96 | 33.72 |
| RF | 26.56 | 45.99 | 51.27 | 25.63 | 50.02 | 53.72 | 11.11 | 28.77 | 35.71 |
| ICL | 26.40 | 47.51 | 53.32 | 26.00 | 49.68 | 53.63 | 13.07 | 30.82 | 36.41 |
| Cluster | 27.00 | 45.82 | 52.04 | 26.15 | 47.41 | 52.39 | 13.20 | 25.77 | 34.07 |
| PCL | 29.16 | 48.44 | 54.21 | 29.00 | 51.56 | 55.11 | 11.55 | 29.45 | 36.46 |
| GCL | 30.50 | 48.53 | 53.26 | 32.00 | 51.61 | 56.63 | 10.00 | 31.45 | 36.67 |
| PCL + Cluster | 30.50 | 48.35 | **54.88** | 35.50 | 53.89 | 58.74 | 12.00 | 30.15 | **38.23** |
| Tempura | **31.50** | **48.64** | 54.49 | **39.00** | **56.51** | **60.95** | **14.00** | **32.17** | 37.59 |

**Table 3: Performance of Tempura with randomized items, clusters and correctly ordered inputs.**
| Dataset | Item-R | Cluster-R | Correct |
|---|---|---|---|
| ML-1M | 51.78 | 52.47 | 54.49 |
| Games | 51.83 | 54.18 | 60.95 |
| Kindle | 34.13 | 33.92 | 37.59 |

**Table 4: Case study of structure analysis in the historical interaction sequence.**
| Cluster Analysis Case Study |
|---|
| **Cluster 1:** [Mad Max - PlayStation 4, Metal Gear Solid V: The Phantom Pain - PlayStation 4]. <br> **Cluster summary:** Action games on PlayStation 4. |
| **Cluster 2:** [Star Wars: Battlefront - Standard Edition - PlayStation 4, Fallout 4 - PlayStation 4, Just Cause 3 - PlayStation 4, Far Cry Primal - PlayStation 4 Standard Edition]. <br> **Cluster summary:** Open-world action games on PlayStation 4. |
| **Cluster 3:** [Tom Clancy's The Division - PlayStation 4, Uncharted 4: A Thief's End - PlayStation 4, Homefront: The Revolution - PlayStation 4, Deus Ex: Mankind Divided - PlayStation 4]. <br> **Cluster summary:** Action games with a focus on story and/or multiplayer on PlayStation 4. |
| **Cluster 4:** [Rise of the Tomb Raider: 20 Year Celebration - PlayStation 4, Dishonored 2 - PlayStation 4, Resident Evil 7: Biohazard - PS4 Digital Code, Horizon Zero Dawn - PlayStation 4, Tom Clancy's Ghost Recon Wildlands - PlayStation 4]. <br> **Cluster summary:** Single-player action shooting games with a focus on exploration and/or stealth on PS4. |
| **Target item:** Prey - Pre-load - PS4 Digital Code (First-person action-adventure shooting game) |

**Table 5: Performance with GPT-4 (NDCG@10).**
| Method | ML-1M | Games | Kindle |
|---|---|---|---|
| Sequential | 55.75 | 66.43 | 57.65 |
| ICL | 54.82 | 67.84 | 54.72 |
| Tempura | 58.39 | 68.13 | 58.59 |

### 考察
- **Table 1およびTable 2**: Tempuraは既存のLLMベースの手法や一部の学習ベースの手法を上回り、顕著なゼロショット性能の向上を達成した。モジュール単独（PCL単体、GCL単体）でも既存の単純なICLを上回っており、特にこれらをアンサンブル（Ours Ensemble / Tempura）した場合に性能が最大化することが示されている。
- **時系列の重要性の検証 (Figure 1 および Table 3)**:
  ![Motivation: Sequential vs Random](./images/paper_motivation_2.png)
  履歴のアイテム順序をランダム化（Item-R）した場合と正しい順序（Correct）を与えた場合を比較したところ、従来の手法（ベースライン）では順序を崩しても性能が低下しなかったのに対し、Tempuraでは正しい時系列を与えた時に明確に性能が向上している。これは、Tempuraのプロンプト戦略によってLLMがシーケンシャル情報の意味（Temporal Awareness）を獲得し、有効活用できるようになったことを証明している。
- **クラスタリングの効果 (Table 4)**: ケーススタディからわかるように、明示的な構造分析（Temporal Structure Analysis）は、過去のインタラクションからゲームのジャンルやプラットフォームをまたいだユーザの嗜好を的確に要約しており、これによりLLMがユーザの興味の年代記的な推移を把握しやすくなっている。
- **基盤モデルとの相性 (Table 5)**: バックボーンとしてGPT-4を利用した結果、性能がさらに向上しており、LLMの推論能力が高いほどTempuraの時系列解析プロンプトの恩恵を強く受けられることが示された。
