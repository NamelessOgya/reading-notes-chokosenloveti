# Black box tuning for language model as a service

## 背景
大規模な事前学習済み言語モデル (PTMs) 、例えばGPT-3などは、非常に強力な一般化能力を持つ一方で、計算コストやパラメータの秘匿性（商業的理由や悪用リスク）から、それらをローカル環境で直接動かすことは難しく、APIサービス (Language-Model-as-a-Service: LMaaS) として提供されるのが一般的である。
このようなブラックボックスなAPI経由では、モデルの内部パラメータや勾配（Gradients）にアクセスすることができない。そのため、モデルの微調整（Fine-TuningやPrompt Tuningなど）を行う際に必須のバックプロパゲーションが使用できず、高い性能を発揮するタスク特化型のContinuous Prompt（連続値ベクトルによるプロンプト）の最適化は困難とされてきた。特にプロンプト空間は数万次元と高次元になるため、勾配情報を用いないDerivative-Free Optimization (DFO: 勾配フリー最適化) アルゴリズムを直接適用することは計算量的に非現実的であった。
本研究では、大規模PTMsがもつ「内在的次元 (Intrinsic Dimensionality) が非常に低い」という特性に着目し、LMaaSの環境下でもAPIアクセスのみを用いて連続値プロンプトを効率的に最適化する手法を提案している。

## 手法
提案手法は「Black-Box Tuning (BBT)」と呼ばれる。
本来最適化すべき高次元の連続値プロンプト空間 $\mathcal{P}$ （次元数 $D$、通常数万次元）で探索を行う代わりに、非常に次元が小さいランダムな部分空間 $\mathcal{Z}$ （次元数 $d$、ここで $d \ll D$、通常数百次元）の中で最適化を行う。最適化器にはDFOの一種であるCMA-ES (Covariance Matrix Adaptation Evolution Strategy) を用いている。

### 問題設定と最適化の定式化
言語理解タスクを分類問題として捉え、入力テキスト $\tilde{X}$ に連続値プロンプト（Continuous Prompt）を付与し、APIを通じて予測ロジット $\mathbf{\hat{Y}}$ を得る。ここで、DFOを用いて以下の最適化問題の解 $\mathbf{z}^\star$ を探索する：
$$ \mathbf{z}^\star = \mathop{\arg\min}_{\mathbf{z}\in \mathcal{Z}}\mathcal{L}(f(\mathbf{Az}+\mathbf{p}_0;\tilde{X}), \tilde{Y}) $$
ここで：
- $\mathbf{p}_0 \in \mathbb{R}^D$: PTMの語彙からランダムサンプリングされたトークン埋め込みによる初期プロンプト。なお、NLIなどのラベル付き大規模データセットが存在し、事前学習が可能なタスクでは、公開データ（MNLIなど）を用いて事前学習したプロンプトを $\mathbf{p}_0$ として使用することが極めて有効である。
- $\mathbf{A} \in \mathbb{R}^{D \times d}$: 部分空間の低次元ベクトル $\mathbf{z}$ を本来の高次元空間に引き伸ばすための**固定のランダム投影行列**。最適化中にこの行列の値は一切更新（学習）されない。従来のDFO（Random Projection）では標準正規分布を使用することが一般的だが、本手法ではニューラルネットワークの初期化手法に着想を得て**一様分布 $\mathcal{U}$** からサンプリングした行列を使用している。これにより、高次元へ写像した際にプロンプトベクトルの値が異常に大きくなる（爆発する）のを抑制し、大幅な収束速度の向上と安定化を達成している。
- $\mathbf{z} \in [-5, 5]^d$: 実際にアルゴリズム（CMA-ES）によって毎ステップ生成・更新され続ける唯一の最適化対象（低次元の部分空間のベクトル）。
- $\mathcal{L}$: 損失関数。Accuracy（精度）ではなく、探索情報を豊富に提供できる **Cross Entropy Loss** や **Hinge Loss** が用いられる。

### Random Projection (ランダム投影) に関する主要な引用文献
本手法の核となる「タスクの内在的次元の小ささ」と「ランダム投影を利用した部分空間での最適化」の理論的・経験的背景として、論文内では以下の研究が主に引用・応用されている。
- **Bayesian Optimization in a Billion Dimensions via Random Embeddings** (2016)
  - 概要: ランダム投影行列を利用して、数十億次元という超高次元な目的関数の最適化を、より低次元の実効部分空間（Effective Subspace）に落とし込んでベイズ最適化（DFOの一種）を実行する手法を提案した論文。
- **Measuring the Intrinsic Dimension of Objective Landscapes** (2018)
  - 概要: ランダム投影技術を用いた部分空間最適化を通じて、あるタスクに対してニューラルネットワークが要求する最小限の自由度、すなわち「内在的次元（Intrinsic Dimension）」を定量的に測定するアプローチを確立した論文。
- **Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning** (2020)
  - 概要: 事前学習済みの大規模モデル（RoBERTaなど）が少量のデータで下流タスクに適応できるのは、事前学習によってタスクの内在的次元が「数百次元程度」へと劇的に圧縮されているからだという発見を、ランダム投影を用いて経験的に証明した論文（本研究の直接的モチベーション）。

### 内部処理におけるプロンプトとテキストの結合メカニズム
API $f()$ を通じた「プロンプトと入力テキストの結合」は、従来の文字列による連結ではなく、**モデル内部のベクトル（埋め込み）次元での直接連結**によって行われます。

具体的には以下の手順でAPI側の処理が行われます：
1. **入力テキストのベクトル化**: 入力テキスト $\tilde{X}$ はモデルのEmbedding層を通り、単語ごとの高次元（例: 1024次元）ベクトルから成る配列に変換されます。
2. **ベクトルの直接連結**: 最適化された連続値プロンプト $\mathbf{p}$ は、テキストと同じ次元数をもつベクトル配列として用意されます。この両者をそのまま数列として連結（Concatenation）し、一つの入力ベクトル列 $\text{Input} = [\mathbf{p} ; \text{Embedding}(\tilde{X})]$ を構築します。
3. **Transformer層での処理**: この連結された長大なベクトル列がそのままTransformerの第1層へ入力され、Self-Attention機構によってテキスト側とプロンプト側のベクトルが互いにAttentionを計算し合うことで推論が強力にガイドされます。
※ 本論文で想定されるような連続値プロンプト（Continuous Prompt）の最適化フレームワークは、LMaaS提供側が「外部からのプロンプト用ベクトル配列を直接受け付け、テキストベクトルと内部で連結して推論させてくれるAPI」を提供していることを前提として成立します。

### CMA-ESのアルゴリズム
CMA-ESは勾配を用いずに目的関数の最小値を探る進化的アルゴリズムである。本手法では以下のようなステップで最適化を進める。
1. **サンプリング**: 各イテレーション $t$ において、多変量正規分布から集団サイズ $\lambda$ に応じた候補プロンプトベクトル $\mathbf{z}_1^{(t+1)}, \dots, \mathbf{z}_\lambda^{(t+1)}$ を以下の式でサンプリングする。
   $$ \mathbf{z}_i^{(t+1)} \sim \mathbf{m}^{(t)} + \sigma^{(t)}\mathcal{N}(\mathbf{0}, \mathbf{C}^{(t)}) $$
2. **評価 (APIコール)**: サンプリングされた各 $\mathbf{z}_i$ を $\mathbf{p} = \mathbf{Az}_i + \mathbf{p}_0$ として高次元のプロンプトに変換しテキストに付加した上でPTMの推論APIに回し、得られた出力結果からLoss $\mathcal{L}$ を計算する。
3. **パラメータ更新**: Lossの評価が良かった候補をもとに、多変量正規分布の平均ベクトル $\mathbf{m}^{(t)}$、共分散行列 $\mathbf{C}^{(t)}$、およびステップサイズを決定する全体の標準偏差 $\sigma^{(t)}$ を適応的に更新する。

このサンプリングと更新を繰り返すことで、PTMのパラメータに一切アクセスすることなく高精度なプロンプトの探索が可能となっている。また、手法の特性上、バッチサイズに余裕がある環境では評価（APIコール）を並列化することが容易であり、大幅な時間短縮（Parallel Evaluation）が可能である。

## 結果

### Figure
論文内で提示されている図版とその内容は以下の通りである。

#### Figure 1
![Figure 1](./images/illustration.png)
LMaaS (Language-Model-as-a-Service) におけるアーキテクチャの概要図。ユーザはPTMの推論APIにテキストとプロンプトを入力し、出力を通じてブラックボックスにプロンプトを最適化する。

#### Figure 2
![Figure 2](./images/method.png)
最適化のシングルイテレーションを図解したもの。低次元の $\mathbf{z}$ をランダム行列 $\mathbf{A}$ を介して高次元の連続値プロンプトに拡張し、APIを介したテキストの予測結果を用いてLossを算出し、次の $\mathbf{z}$ の探索に用いる。

#### Figure 3
![Figure 3](./images/sst_loss_train.png)
![Figure 3](./images/sst_loss_dev.png)
![Figure 3](./images/agnews_loss_train.png)
![Figure 3](./images/agnews_loss_dev.png)
![Figure 3](./images/sst_intrinsic_dim_train.png)
![Figure 3](./images/sst_intrinsic_dim_dev.png)
![Figure 3](./images/agnews_intrinsic_dim_train.png)
![Figure 3](./images/agnews_intrinsic_dim_dev.png)
![Figure 3](./images/sst_prompt_len_train.png)
![Figure 3](./images/sst_prompt_len_dev.png)
![Figure 3](./images/agnews_prompt_len_train.png)
![Figure 3](./images/agnews_prompt_len_dev.png)
損失関数、内在的次元（サブスペース次元）、プロンプトの長さを変更した際のアブレーションスタディ。SST-2やAG's Newsにおける学習と評価。LossについてはCross EntropyおよびHinge Lossが有効であり、Negative Accuracyは報酬が疎になるため収束が難しい傾向にある。プロンプト長については短すぎると収束が早まるが汎化性能が低下するため $L=50$ が最良である。内在的次元はタスクによって最適値が変化することも見出された。

#### Figure 4 (Appendix)
![Figure 4](./images/sst_re.png)
![Figure 4](./images/agnews_re.png)
ランダム投影行列 $\mathbf{A}$ の分布についての効果。標準正規分布より、一様分布からサンプリングした行列を使用する方が速やかな収束を見せることが分かった。

#### Figure 5 (Appendix)
![Figure 5](./images/sst_popsize_train.png)
![Figure 5](./images/sst_popsize_dev.png)
集団サイズ (Population Size) の影響を示す図。小さい集団サイズの方がAPIコール数に対しては収束が早くなることが示されている。

#### Figure 6 (Appendix)
![Figure 6](./images/snli_intrinsic_16shot.png)
![Figure 6](./images/snli_prompt_len_16shot.png)
![Figure 6](./images/sst_intrinsic_16shot.png)
![Figure 6](./images/sst_prompt_len_16shot.png)
16-shotの設定における内在的次元およびプロンプト長についてのアブレーション結果。

#### Figure 7 (Appendix)
![Figure 7](./images/cma_vs_adam.png)
低次元部分空間におけるCMA-ESとAdamの実装比較。CMA-ESはAdamよりも低次元空間で効率的・安定的に解を探索できる。

#### Figure 8 (Appendix)
![Figure 8](./images/parallel.png)
![Figure 8](./images/sst_popsize_train_iter.png)
![Figure 8](./images/sst_popsize_dev_iter.png)
（a）は全体集団を並列評価（Parallel Evaluation）する模式図、（b）（c）はイテレーションベースでの収束率を比較したもの。

---

### Table
論文内で提示されているすべての表データの完全な文字起こしおよび結果の考察。

#### Table 1
| Category | Dataset | $\mid\mathcal{Y}\mid$ | $\mid$Train$\mid$ | $\mid$Test$\mid$ | Type | Template | Label words |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| single-sentence | SST-2 | 2 | 67k | 0.9k | sentiment | $\langle S\rangle$. It was [MASK]. | great, bad |
| single-sentence | Yelp P. | 2 | 560k | 38k | sentiment | $\langle S\rangle$. It was [MASK]. | great, bad |
| single-sentence | AG's News | 4 | 120k | 7.6k | topic | [MASK] News: $\langle S\rangle$ | World, Sports, Business, Tech |
| single-sentence | DBPedia | 14 | 560k | 70k | topic | [Category: [MASK]] $\langle S\rangle$ | Company, Education, Artist, Athlete, Office, Transportation, Building, Natural, Village, Animal, Plant, Album, Film, Written |
| sentence-pair | MRPC | 2 | 3.7k | 0.4k | paraphrase | $\langle S_1\rangle$ ? [MASK], $\langle S_2\rangle$ | Yes, No |
| sentence-pair | RTE | 2 | 2.5k | 0.3k | NLI | $\langle S_1\rangle$ ? [MASK], $\langle S_2\rangle$ | Yes, No |
| sentence-pair | SNLI | 3 | 549k | 9.8k | NLI | $\langle S_1\rangle$ ? [MASK], $\langle S_2\rangle$ | Yes, Maybe, No |

実験に使用された各データセットの統計、手動構築したプロンプトテンプレート、およびラベルをマッピングするための単語の一覧である。

#### Table 2
| Hyper-parameter | Default |
| :--- | :--- |
| Prompt length ($L$) | 50 |
| Subspace dimension ($d$) | 500 |
| Population size ($\lambda$) | 20 |
| Random projection ($\mathbf{A}$) | Uniform |
| Loss function $\mathcal{L}$ | Cross Entropy |
| Budget (# of API calls) | 8000 |

Black-box tuningに使用されたデフォルトのハイパーパラメータ構成の設定。

#### Table 3
| Method | SST-2 acc | Yelp P. acc | AG's News acc | DBPedia acc | MRPC F1 | SNLI acc | RTE acc | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gradient-Based Methods** | | | | | | | | |
| Prompt Tuning | 68.23 $\pm$3.78 | 61.02 $\pm$6.65 | 84.81 $\pm$0.66 | 87.75 $\pm$1.48 | 51.61 $\pm$8.67 | 36.13 $\pm$1.51 | 54.69 $\pm$3.79 | 63.46 |
|  + Pre-trained prompt | / | / | / | / | 77.48 $\pm$4.85 | 64.55 $\pm$2.43 | 77.13 $\pm$0.83 | 74.42 |
| P-Tuning v2 | 64.33 $\pm$3.05 | 92.63 $\pm$1.39 | 83.46 $\pm$1.01 | 97.05 $\pm$0.41 | 68.14 $\pm$3.89 | 36.89 $\pm$0.79 | 50.78 $\pm$2.28 | 70.47 |
| Model Tuning | 85.39 $\pm$2.84 | 91.82 $\pm$0.79 | 86.36 $\pm$1.85 | 97.98 $\pm$0.14 | 77.35 $\pm$5.70 | 54.64 $\pm$5.29 | 58.60 $\pm$6.21 | 78.88 |
| **Gradient-Free Methods** | | | | | | | | |
| Manual Prompt | 79.82 | 89.65 | 76.96 | 41.33 | 67.40 | 31.11 | 51.62 | 62.56 |
| In-Context Learning | 79.79 $\pm$3.06 | 85.38 $\pm$3.92 | 62.21 $\pm$13.46 | 34.83 $\pm$7.59 | 45.81 $\pm$6.67 | 47.11 $\pm$0.63 | 60.36 $\pm$1.56 | 59.36 |
| Feature-MLP | 64.80 $\pm$1.78 | 79.20 $\pm$2.26 | 70.77 $\pm$0.67 | 87.78 $\pm$0.61 | 68.40 $\pm$0.86 | 42.01 $\pm$0.33 | 53.43 $\pm$1.57 | 66.63 |
| Feature-BiLSTM | 65.95 $\pm$0.99 | 74.68 $\pm$0.10 | 77.28 $\pm$2.83 | 90.37 $\pm$3.10 | 71.55 $\pm$7.10 | 46.02 $\pm$0.38 | 52.17 $\pm$0.25 | 68.29 |
| **Black-Box Tuning** | 89.56 $\pm$0.25 | 91.50 $\pm$0.16 | 81.51 $\pm$0.79 | 87.80 $\pm$1.53 | 61.56 $\pm$4.34 | 46.58 $\pm$1.33 | 52.59 $\pm$2.21 | 73.01 |
|  + Pre-trained prompt | / | / | / | / | 75.51 $\pm$5.54 | 83.83 $\pm$0.21 | 77.62 $\pm$1.30 | **83.90** |

RoBERTa-LARGEを使用し、クラスあたり16ショット（few-shot）の設定で行われた各言語理解タスクの全体的な精度（F1含む）比較である。Black-Box Tuningは、Manual PromptやIn-Context Learning、特徴抽出ベースなどの他の勾配フリー手法を大幅に上回っただけでなく、Prompt TuningやModel Tuningといった勾配を使用する手法に対しても、全体の平均的結果において勝る（平均83.90ポイント）という驚異的な結果を示した。これは勾配ベースのAdam最適化器が少数の訓練データに対して過学習しがちであるのに対し、DFOのCMA-ESが探索的性質により汎化性能の高い良質なソリューションを見つけ出しやすいという背景が考察されている。

#### Table 4
| Method | Deployment-Efficient | As-A-Service | Test Accuracy | Training Time | Memory Footprint (User) | Memory Footprint (Server) | Upload per query | Download per query |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SST-2** (max sequence length: 47) | | | | | | | | |
| Prompt Tuning | $\surd$ | $\times$ | 72.6 | 15.9 mins | - | 5.3 GB | - | - |
| Model Tuning | $\times$ | $\times$ | 87.8 | 9.8 mins | - | 7.3 GB | - | - |
| Feature-MLP | $\surd$ | $\surd$ | 63.8 | 7.0 mins | 20 MB | 2.8 GB | 4 KB | 128 KB |
| Feature-BiLSTM | $\surd$ | $\surd$ | 66.2 | 9.3 mins | 410 MB | 2.8 GB | 4 KB | 6016 KB |
| Black-Box Tuning | $\surd$ | $\surd$ | 89.4 | 10.1 (6.1$^\star$) mins | 30 MB | 3.0 GB | 6 KB | 0.25 KB |
| **AG's News** (max sequence length: 107) | | | | | | | | |
| Prompt Tuning | $\surd$ | $\times$ | 84.0 | 30.2 mins | - | 7.7 GB | - | - |
| Model Tuning | $\times$ | $\times$ | 88.4 | 13.1 mins | - | 7.3 GB | - | - |
| Feature-MLP | $\surd$ | $\surd$ | 71.0 | 13.5 mins | 20 MB | 3.6 GB | 20 KB | 256 KB |
| Feature-BiLSTM | $\surd$ | $\surd$ | 73.1 | 19.7 mins | 500 MB | 3.6 GB | 20 KB | 27392 KB |
| Black-Box Tuning | $\surd$ | $\surd$ | 82.6 | 21.0 (17.7$^\star$) mins | 30 MB | 4.6 GB | 22 KB | 1 KB |

モデルのデプロイ効率、As-A-Serviceとしての適用可能性、テスト精度、学習時間、ネットワーク通信量、メモリ占有量についての比較データ。Model Tuningはユーザごとに全パラメータコピーの維持が必要となるためデプロイ面で非効率である。Prompt Tuningなども勾配へのアクセスが必要であるため、APIサービス環境下では利用不可である。それに対し、Black-Box Tuningはユーザ側のメモリ消費が極めて少なく（30MB程度）、アップロード/ダウンロードされる通信データ量も小さく済む。さらにONNX Runtime（表中の$^\star$）による高速化を用いれば、訓練時間も十分に実用的であることが示され、LMaaS環境に対する極めて洗練された回答であることが結論付けられている。

## chokosenlovetiの考察

### 新規性
本論文の最も革新的な新規性は、主に以下の3点に集約される。

1. **連続値プロンプトの「完全なブラックボックス最適化」を実証した最初の研究であること**
   これまで、高精度なContinuous Prompt（連続値プロンプト）のチューニングは、パラメータの勾配計算（バックプロパゲーション）が不可欠だと考えられていた。この固定観念を真っ向から打ち破り、API経由で推論結果（Loss）だけをもらう勾配フリー（Derivative-Free / ゼロ次）の最適化でも十分に学習が可能であることを示した点が極めて画期的である。
   - **フルパラメータ・ファインチューニング (Model Tuning) との比較条件**:
     - **設定**: 各クラスわずか16個の正解データしか学習に使用できない **Few-shot (16-shot) 環境**。
     - **モデル**: 3億パラメーター超の大規模モデル「RoBERTa-LARGE」。
     - **従来手法**: 勾配（Adam最適化器）を用いて、モデルの全パラメータをフルに更新する。
     - **提案手法**: モデルパラメータは完全に「凍結（固定）」。勾配へのアクセスは一切なしで、わずか500次元程度の部分空間のみをAPI経由で進化的アルゴリズム（CMA-ES）を用いて更新する。
   - **意義**: 上記の厳しい条件において、従来の手法（フルパラメータへのAdam最適化）は少数のデータに対して深刻な**過学習（Overfitting）**を起こしてスコアを落としやすかった。対して本手法（CMA-ESによる探索的最適化）は汎化性能を保ちやすく、結果として**7タスクの平均精度（83.90 vs 78.88）でフルパラメータ更新版を真っ向から凌駕する**という驚異的な実証を行った。
   
2. **「内在的次元 (Intrinsic Dimension)」と「CMA-ES (DFO)」を結びつけた点**
   本来、CMA-ESのような進化的アルゴリズム・勾配フリー探索アルゴリズムは「数万次元」に及ぶ高次元の探索空間では全く歯が立たない（次元の呪い）。しかし著者らは、「大規模言語モデルのタスク適応における効果的な次元は極めて小さい（数百次元程度）」という既存の発見（Intrinsic Dimensionality）を最大限に活用し、一様分布から生成した『ランダム投影行列』によって「数万次元の最適化問題を、わずか数百次元の最適化問題へ効果的に圧縮する」というブレイクスルーをもたらした。

