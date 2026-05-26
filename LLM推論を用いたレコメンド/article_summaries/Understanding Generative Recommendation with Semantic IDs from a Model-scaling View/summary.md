# Understanding Generative Recommendation with Semantic IDs from a Model-scaling View

## 背景
生成モデルの発展に伴い、レコメンドシステム（RS）においても推薦アイテムを直接生成するGenerative Recommendation（GR）が注目を集めている。このGRには大きく分けて2つのパラダイムが存在する。
1. **SID-based GR**: 大規模言語モデル（LLM）などのエンコーダでアイテムのテキストから抽出した意味的表現（セマンティクス）を、Quantization Tokenizer（量子化トークナイザ）を通じて離散的な「Semantic ID (SID)」に変換し、シーケンシャルレコメンダに入力するパラダイム（例：TIGERなど）。
2. **LLM-as-RS**: 従来の離散IDを介さず、LLM自体をファインチューニングして推薦アイテムのテキストを直接生成させるパラダイム。

言語モデルなどの他の生成タスク領域では、モデルパラメータやデータサイズを拡大することで性能が向上するという「Scaling Law（スケーリング則）」が広く確認されている。しかし、GR領域、特にSID-based GRにおいてモデルをスケールアップさせた際にどのような挙動を示すかは十分に解明されていなかった。そこで本研究は、SID-based GRとLLM-as-RSの両パラダイムに対し、モデルサイズを44Mから14B（140億）パラメータにわたって変化させる包括的な実験を行い、スケーリング法則の観点からそれぞれの限界と有望性を検証した。

## 手法
本研究では、SID-based GR（代表的な枠組みとしてTIGER等）とLLM-as-RS（Qwen3モデル＋LoRAによるファインチューニング）の2つについて、それぞれ構成要素のモデルサイズを段階的にスケールアップしてRecallやNDCG等の性能指標の変化を観察した。
また、スケーリングによる性能変化を定量的にモデリングするため、意味的情報（Semantic Information: SI）と協調フィルタリング（Collaborative Filtering: CF）の各エラー項を分離した以下の経験的なスケーリング則（Scaling Law）の式を定義した。

### SID-based GRのScaling Law
$$
\mathrm{Recall@}k = R_0 - \frac{A}{(N_{\text{RS}}+\gamma_1 N_{\text{LLM}}+\gamma_2 N_{\text{QT}})^a} - \frac{B}{N_{\text{RS}}^{b}}
$$
ここで、$N_{\text{RS}}$ はレコメンダモジュールのパラメータ数、$N_{\text{LLM}}$ はLLMエンコーダのパラメータ数、$N_{\text{QT}}$ はトークナイザのパラメータ数を示す。

### LLM-as-RSのScaling Law
$$
\mathrm{Recall@}k = R_0 - \frac{A}{(N_{\text{LoRA}}+\gamma N_{\text{LLM}})^a} - \frac{B}{(N_{\text{LoRA}}+\beta N_{\text{LLM}})^{b}}
$$
ここで、$N_{\text{LoRA}}$ は学習可能なLoRAウェイトのパラメータ数、$N_{\text{LLM}}$ は凍結されたLLM本体のパラメータ数を示す。$\gamma, \beta$ はLLMがSIおよびCFシグナルの学習に寄与する度合いの係数である。

## 結果

### 1. SID-based GRにおけるスケーリングの限界（Bottleneck）
SID-based GRの構成要素を個別にスケールさせたところ、レコメンダ（$N_{\text{RS}}$）を拡大しても一定以上（約1,300万パラメータ）で性能が早期に飽和することが判明した。また、LLMエンコーダ（$N_{\text{LLM}}$）を77Mから11Bへ拡大しても、量子化トークナイザ（$N_{\text{QT}}$）のコードブック数やサイズを増やしても、性能向上はほとんど見られなかった（$\gamma_1 \approx 0, \gamma_2 \approx 0$）。

![Two GR paradigms](images/GR_paradigms_v5.png)
*図: 本研究で比較された2つのGRパラダイムの概要図*

![RS Scaling](images/RS_scaling.png)
*図: SID-based GRにおけるレコメンダモジュールのスケーリング。約10^7パラメータ付近で急速に性能が飽和する。*

![LLM Scaling](images/scaling_flan-t5_final.png)
*図: SID-based GRにおけるLLMエンコーダのスケーリング。LLMの規模を拡大しても性能が向上しない。*

アブレーション実験から、この飽和の根本原因は「離散的なSID自体が持つ意味表現力の限界」にあると結論づけられた。密なLLMエンベディングを無理に少数の離散ID（SID）に量子化することで情報が欠落し、これ以上モデルを巨大化させても下流のレコメンダにリッチな情報が伝達されないことがスケーリングのボトルネックとなっている。

### 2. LLM-as-RSにおける優れたスケーリング特性
一方、LLM-as-RSパラダイムでは、LLMのサイズ（$N_{\text{LLM}}$）を0.6Bから14Bへと拡大するのに比例して、性能の飽和を見せることなく一貫して精度（Recall等）が向上し続けることが確認された。スケーリング則をフィッティングした結果（Huber Lossを使用）、$\gamma > 0, \beta > 0$ となり、凍結されたLLM本体が「意味情報の理解」だけでなく「協調フィルタリング（CF）シグナルのモデリング」の双方に寄与してスケールしていることが定量的に示された。

![LLM-as-RS Scaling](images/Lora_general_scale.png)
*図: LLM-as-RSにおけるスケーリング挙動。赤い点線（SID-based GRの最高性能）を上回り、モデル規模に応じて性能が伸び続けている。*

![CF Embeddings Scaling](images/cf_scale_1.png)
*図: 外部CFエンベディング注入時のパフォーマンスゲイン。バックボーンLLMのサイズが大きくなるほど、外部CFの恩恵が低下する（LLM自身がCF情報をより強力にモデリングできるため）。*

最終的に、LLM-as-RSはモデルをスケールアップすることで、同じ学習データにおけるSID-based GRの最大性能を最大で**20%** 上回る結果を残した。

### 3. 各種詳細データ（論文内のテーブル完全書き起こし）

以下は論文に掲載されていたすべての実験結果・各種パラメータの完全な転記である。

#### Table 1: The fitted empirical parameters of scaling laws of SID-based GR.
|        | Beauty | Sports | Toys |
|:---|:---|:---|:---|
| $\text{R-square}$  | 0.94  | 0.97   | 0.94 |
| $R_0$  | 0.4529   | 3e-1   | 1.7e-1 |
| $A$    | 16.8  | 24.8 | 6.1 |
| $B$    | 1e-2 | 1e-2 | 1e-2 |
| $a$    | 0.6 | 0.63 | 0.52 |
| $b$    | 2.23 | 1.97 | 2.02 |

#### Table 2: The details of scaling RS module in SID-based GR.
| **#Params** | **#Layers** | $\mathbf{d_{\text{model}}}$ | **#Heads** | $\mathbf{d_{\text{kv}}}$ | $\mathbf{d_{\text{ff}}}$ |
|---:|:---:|:---:|:---:|:---:|:---:|
| 336,000 | 1 | 64  | 3  | 64 | 512  |
| 778,000 | 2 | 64  | 3  | 64 | 512  |
| 1,900,000 | 5 | 64  | 3  | 64 | 512  |
| 3,300,000 | 9 | 64  | 3  | 64 | 512  |
| 6,700,000 | 3 | 128 | 6  | 64 | 1024 |
| 13,000,000 | 4 | 128 | 6 | 64 | 1024 |
| 21,000,000 | 7 | 128 | 6  | 64 | 1024 |
| 43,000,000 | 8 | 192 | 9  | 64 | 1536 |
| 88,000,000 | 9 | 320 | 15 | 64 | 2560 |
| 192,000,000 | 20 | 384 | 18 | 64 | 3072 |

#### Table 3: The details of scaling the SASRec model.
| **#Params** | **#Layers** | $\mathbf{d_{\text{model}}}$ | **#Heads** |
|---:|:---:|:---:|:---:|
|    98,304      | 2  | 64   | 2  |
|   786,432      | 4  | 128  | 4  |
| 1,572,864      | 8  | 128  | 4  |
| 6,291,456      | 8 | 256  | 8  |
| 25,165,824     | 8 | 512  | 8  |
| 75,497,472    | 24 | 512 | 8 |

#### Table 4: Statistics of the datasets used in our experiments.
| **Dataset** | **# users** | **# items** | **# actions**  |
|:---|---:|---:|---:|
| *Beauty* | 22,363 | 12,101 | 198,502 |
| *Toys and Games* | 19,412 | 11,924 | 167,597 |
| *Sports and Outdoors* | 35,598 | 18,357 | 296,337|

#### Table 5: The results when we input SIDs as item representations into the LLM.
|        | Qwen3-0.6B    | Qwen3-1.7B     | Qwen3-4B    | Qwen3-8B   |
|:---|:---:|:---:|:---:|:---:|
| Beauty  | 0.0356 | 0.0379 | 0.0393 | 0.0409 |
| Sports  | 0.0197 | 0.0217 | 0.0225 | 0.0234 |
| Toys  | 0.0367 | 0.0380 | 0.0392 | 0.0398 |

#### Table 6: The comparison on the cold-start items.
|        | SID-based GR   | LLM-as-RS      |
|:---|:---:|:---:|
| Beauty  | 0.018 | **0.030** |
| Sports  | 0.006 | **0.014**   |
| Toys  | 0.022 | **0.028**  |

#### Table 7: The fitted empirical parameters in Section 4.1.
|        | Beauty | Sports | Toys |
|:---|:---:|:---:|:---:|
| $R_0$  | 3e-1   | 3e-1   | 1.7e-1 |
| $A$    | 9.9e2  | 9.87e2 | 2.19e-1 |
| $B$    | 3.4e-1 | 3.35e-1 | 9.93e2 |
| $\gamma$ | 9.08e-2 | 1.82e-2 | 1.74e-1 |
| $\beta$  | 2.10e-2 | 1.69e-2 | 2.29e-2 |
| $a$    | 1.98e1 | 2.02e1 | 2.47e-2 |
| $b$    | 1.39e-2 | 9.47e-3 | 2.02e1 |

#### Table 8: Held-out fitting errors of Equation 2 when $\beta=0$ and $\beta>0$.
|  | $\beta=0$ | $\beta>0$ |
|:---|:---:|:---:|
| Beauty | 4.2e-4 | **3.5e-4** |
| Sports | 1e-3 | **3.6e-4** |
| Toys | 1.2e-3 | **9.8e-4** |

### 考察と結論
従来、LLM-as-RSは「アイテムの意味は捉えられるがユーザーの行動（CF）のモデリングは苦手である」という見方が支配的であった。しかし本論文は、モデルを適切にスケールさせることでLLM-as-RSがCF信号をも強力に学習し、SID-based GRを大きく凌駕することを示した。計算予算が限られて推論レイテンシが厳しい場合は依然としてSID-based GRが有用な場面もあるものの、将来的な「レコメンド向け基盤モデル（Foundation Models for GR）」の構築に向けては、LLM-as-RSのアプローチがより優れたスケーラビリティを備えていると結論づけている。
