# Are Large Language Models Really Effective for Training-Free Cold-Start Recommendation?

## 背景
これまでレコメンドシステムにおいて、学習データが存在しない「Training-Free」環境や、ユーザーの過去の行動履歴が存在しない「Cold-Start」環境は共通の課題でした。特にトレーニングデータもなく、履歴もない「Training-Free Cold-Start Recommendation (TFCSR)」は非常に制限の厳しいシナリオです。この設定において、近年では大規模言語モデル（LLMs）を用いて、ユーザーのテキストとアイテムのテキストから直接ランランキングを行うアプローチ（LLMリランカー）が有力視され、多くの研究で「これこそが最も効果的な方法である」と信じられてきました。

しかし、近年性能が向上しているテキスト埋め込みモデル（Text Embedding Models: TEMs）も、このTraining-Freeな設定に適用可能であるものの、LLMとTEMを同一条件で系統立てて比較した検証は存在していませんでした。
本論文では世界で初めてTFCSRの同一設定下においてLLMリランカーとTEMを並べて性能比較し、「本当にLLMがTFCSRに最も効果的なのか？」を検証しています。

以下のTable 1は、既存のレコメンド研究を「学習の有無」と「ターゲットユーザーの履歴量 $m$」によって分類した表です（$m=0$ をNarrow CS、$m$が少数をBroad CSと定義）。

| | Size $m$ | Description | References |
|---|---|---|---|
| Need Training | Rich | The model is trained with sufficient data from many users, and the target user also has rich interactions. This is a major research focus in recommender systems. | [1, 2, 3, 4] |
| Need Training | A few | The model is trained, while the target user has only a few interactions (broad cold-start). | [5, 6] |
| Need Training | Zero | The model is trained, but the target user has no interactions and only profile information (narrow cold-start). | [7, 8, 9] |
| Training-free | Rich | No training is performed; recommendations rely only on the target user's own rich interactions. | [10, 11, 12, 13] |
| Training-free | A few | No training is performed; the target user has only a few interactions (broad cold-start). | [14, 15] |
| Training-free | Zero | No training is performed; the target user has no interactions and only profile information (narrow cold-start). This is the primary focus of our study. | - |


## 手法
以下のような設定およびモデル群を用いて実験的に比較しています。
- **ターゲットユーザーのインタラクション数 $m$**: 過去の行動履歴アイテムがない状態（$m=0$：Narrow CS）と、少数の過去履歴がある状態（$m \ge 1$：Broad CS）の2パターン。
- **比較対象モデル**:
  - **スパースエンコーダー**: `BM25` (ベースライン)
  - **TEMs**: `multilingual-e5-large`, `bge-m3`, `gte-modernbert-base`, `gte-Qwen2-1.5B/7B-instruct`, `Qwen3-Embedding-0.6B/8B`
  - **LLMs (リランカー)**: `gpt-4.1-mini`, `gpt-4.1`, `Qwen3-8B`
- **TEMにおけるスコア計算**:
  ユーザーテキスト $t_u$ とアイテムテキスト $t_i$ をそれぞれ $f(t)$ によってベクトル $\mathbf{v}_u$, $\mathbf{v}_i$ にエンコードし、コサイン類似度によってランク付け。
  
$$ \cos(\mathbf{x}, \mathbf{y}) = \frac{\langle \mathbf{x}, \mathbf{y} \rangle}{\|\mathbf{x}\| \|\mathbf{y}\|} $$

  Broad CSのようにユーザーに $m$ 個の履歴 $D_u = \{t_{u,1}, \dots, t_{u,m}\}$ がある場合の類似度 $s_{u,i}$ は、埋め込みベクトルの平均の類似度を取ります。

$$ s_{u,i} = \frac{1}{m} \sum_{j=1}^{m} \cos(f(t_{u,j}), \mathbf{v}_i) $$

- **LLMリランカーにおける推論（Listwise Ranking）**:
  LLMを用いた予測ではゼロショットのプロンプト推論を行います。ユーザーのプロフィール（および少数の履歴）と、**50個の候補アイテム一覧**を1つのプロンプトにまとめます。
  LLMに対して「候補50個の中から、このユーザーに最も適したアイテムを10個選び、おすすめ順に並べて出力せよ」という指示を与え、プレーンテキストによる並び替え（Listwise Ranking）にてTop-10の抽出を行わせます。なお、LLM特有の順序バイアス（リストの上下にあるものが選ばれやすい傾向）を排除するため、候補アイテムの提示順は毎回ランダムにシャッフルされます。


## 結果
驚くべきことに、広く信じられていた認識に反し、**ほとんどのTFCSR設定においてTEMのほうがLLMリランカーよりも高い精度を達成**しました。

Table 2に狭義のコールドスタート（$m=0$）の場合、Table 3に広義のコールドスタート（$m=1$）の場合の比較結果を示します。

### Table 2: Recall@10 and nDCG@10 in the narrow cold-start setting. ($m=0$)
| | ML-1M (Recall) | ML-1M (nDCG) | Job (no exp) (Recall) | Job (no exp) (nDCG) | Job (exp) (Recall) | Job (exp) (nDCG) | All (Recall) | All (nDCG) |
|---|---|---|---|---|---|---|---|---|
| `BM25` | 0.202 | 0.235 | 0.321 | 0.373 | 0.423 | 0.476 | 0.315 | 0.362 |
| `gte-modernbert-base` | 0.221 | 0.251 | 0.219 (down) | 0.230 (down) | 0.222 (down) | 0.244 (down) | 0.221 (down) | 0.242 (down) |
| `multilingual-e5-large` | 0.223 | 0.260 | 0.343 | 0.381 | 0.335 (down) | 0.376 (down) | 0.300 | 0.339 |
| `bge-m3` | 0.220 | 0.249 | 0.307 | 0.373 | 0.353 (down) | 0.371 (down) | 0.293 | 0.331 |
| `gte-Qwen2-1.5B-instruct` | 0.233 | 0.267 | 0.361 | 0.402 | 0.427 | 0.462 | 0.340 | 0.377 |
| `gte-Qwen2-7B-instruct` | 0.222 | 0.255 | 0.382* | 0.440 | 0.511* | 0.540* | 0.372* | 0.412* |
| `Qwen3-Embedding-0.6B` | 0.223 | 0.260 | 0.397* | 0.439 | 0.465 | 0.503 | 0.362* | 0.401 |
| `Qwen3-Embedding-8B` | 0.247 | **0.273** | **0.408*** | **0.459*** | **0.521*** | **0.557*** | **0.392*** | **0.430*** |
| `gpt-4.1-mini` | 0.218 | 0.207 | 0.273 | 0.245 (down) | 0.355 | 0.327 (down) | 0.282 | 0.260 (down) |
| `gpt-4.1` | **0.269*** | 0.247 | 0.283 | 0.258 (down) | 0.381 | 0.343 (down) | 0.311 | 0.283 (down) |
| `Qwen/Qwen3-8B` | 0.187 | 0.165 (down) | 0.061 (down) | 0.057 (down) | 0.092 (down) | 0.080 (down) | 0.114 (down) | 0.101 (down) |

### Table 3: Recall@10 and nDCG@10 for the broad cold-start setting with $m=1$.
| | ML-1M (Recall) | ML-1M (nDCG) | Job (Recall) | Job (nDCG) | Music (Recall) | Music (nDCG) | Movie (Recall) | Movie (nDCG) | Books (Recall) | Books (nDCG) | All (Recall) | All (nDCG) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `BM25` | 0.388 | 0.423 | 0.414 | 0.475 | 0.345 | 0.457 | 0.367 | 0.442 | 0.473 | 0.590 | 0.397 | 0.477 |
| `gte-modernbert-base` | 0.426 | 0.446 | 0.371 | 0.441 | 0.498* | 0.561* | 0.456* | 0.519* | 0.557* | 0.628 | 0.462* | 0.519* |
| `multilingual-e5-large` | 0.436 | 0.439 | 0.337(down)| 0.393(down)| 0.464* | 0.543* | 0.439* | 0.488 | 0.546* | 0.631 | 0.444* | 0.499 |
| `bge-m3` | 0.439 | 0.442 | 0.417 | 0.476 | 0.429* | 0.505 | 0.423* | 0.491 | 0.541* | 0.616 | 0.449* | 0.506* |
| `gte-Qwen2-1.5B-instruct`| 0.459* | 0.473 | 0.471* | 0.517 | 0.532* | 0.581* | 0.482* | 0.554* | 0.575* | 0.655* | 0.504* | 0.556* |
| `gte-Qwen2-7B-instruct`| 0.465* | 0.467 | **0.511***| **0.554***| 0.535* | **0.604***| **0.560***| **0.598***| **0.609***| **0.683***| **0.536***| **0.581***|
| `Qwen3-Embedding-0.6B` | **0.465***| 0.473 | 0.458 | 0.515 | 0.445* | 0.523* | 0.447* | 0.515* | 0.553* | 0.625 | 0.474* | 0.530* |
| `Qwen3-Embedding-8B` | 0.465* | **0.477** | 0.475* | 0.533 | **0.535***| 0.604* | 0.509* | 0.578* | 0.587* | 0.652 | 0.514* | 0.569* |
| `gpt-4.1-mini` | 0.339 | 0.289(down)| 0.272(down)| 0.264(down)| 0.405* | 0.365(down)| 0.323 | 0.311(down)| 0.487 | 0.427(down)| 0.365 | 0.331(down)|
| `gpt-4.1` | 0.391 | 0.336(down)| 0.363 | 0.328(down)| 0.453* | 0.396 | 0.399 | 0.357(down)| 0.556* | 0.470(down)| 0.433* | 0.377(down)|
| `Qwen/Qwen3-8B` | 0.295(down)| 0.251(down)| 0.085(down)| 0.085(down)| 0.203(down)| 0.197(down)| 0.175(down)| 0.170(down)| 0.266(down)| 0.254(down)| 0.205(down)| 0.191(down)|

これらの表から明らかなように、`gpt-4.1`や`Qwen3-8B`などの強力なLLMリランカーを使用したとしても、`gte-Qwen2-7B-instruct`や`Qwen3-Embedding-8B`といった最近のLLMの監督下で事前学習されたTEMの方が安定して高いスコアを叩き出しています。逆にLLMリランカーの多くはベースラインの`BM25`と同等またはそれ以下の結果に留まっています。

### ユーザーレベルでのエラー解析 (Figure 1)
一部の特定ユーザーのみLLMが極端に苦手なのか探るため、ユーザーごとにLLMとTEMの勝敗をプロットしたのがFigure 1です。

![Error Analysis](./images/rq_error_analysis.png)
*(Figure 1: User-level win/loss relationships. TEM (Qwen3-Embedding-8B) と LLM (gpt-4.1) のユーザー毎の性能差比率)*

グラフからわかる通り、非常に限られた条件（MovieLensのNarrow CS等）を除き、概ね75%以上のユーザーに対してTEMの方がLLMよりも高いスコアをもたらしており、LLMの弱さはシステム全体的な（一貫した）ものであることがわかります。

### コンテキスト長の制約（履歴数と候補アイテム数）
LLMリランカーの性能定価が、長文コンテキスト（$L=50$の候補数など）に起因するかを検証したのが以下のFigure 2とFigure 3です。

![Effect of m](./images/rq_icl_size.png)
*(Figure 2: History size $m$ の変化に応じた性能。点線はランダム。)*

![Effect of small L](./images/rq_icl_size_small.png)
*(Figure 3: 候補アイテム数を L=10 に制限した場合の性能変化)*

$m$を増やしたり、候補アイテム数$L$を10まで絞り込んだりしても、依然としてTEMがLLMを上回る結果となり、LLMのプロンプト長に関する制約が原因で負けているわけではないことがわかります。

### クエリ拡張によるTEMへの影響とその考察
TEMアプローチをより改善するため、LLMを用いてユーザー情報を仮想的なクエリ群に拡張（CQやMQ）してからTEMに与える「ハイブリッド手法」の有効性を検証しました（Figure 4）。

![Embedding extensions](./images/rq_embedding_raw-raw.png)
*(Figure 4: The relative improvement over Raw-Raw embedding approach)*

結果として、もともと精度の低いTEM（`gte-modernbert-base`等）には拡張効果（最大50%向上）が見られましたが、最高性能の `Qwen3-Embedding-8B` に至っては殆ど効果がないか、逆に精度が下落する結果となりました。すなわち最新のTEMは入力テキストを元の情報（Raw）のまま扱う方が堅牢で精度が出ることがわかります。

### クロスドメイン環境での検証
全く行動履歴がないが別ドメインの履歴がある「クロスドメイン」設定の性能を調べたのがTable 4とFigure 5です。

### Table 4: Recall@10 and nDCG@10 in the cross-domain setting with $m'=1$.
| | Music $\rightarrow$ Movie (Recall) | Music $\rightarrow$ Movie (nDCG) | Movie $\rightarrow$ Music (Recall) | Movie $\rightarrow$ Music (nDCG) | Books $\rightarrow$ Movie (Recall) | Books $\rightarrow$ Movie (nDCG) | Movie $\rightarrow$ Books (Recall) | Movie $\rightarrow$ Books (nDCG) | All (Recall) | All (nDCG) |
|---|---|---|---|---|---|---|---|---|---|---|
| `BM25` | 0.249 | 0.308 | 0.175 | 0.214 | 0.238 | 0.282 | 0.197 | 0.232 | 0.215 | 0.259 |
| `gte-modernbert-base` | 0.327* | 0.380 | 0.307* | 0.349* | 0.277 | 0.313 | 0.293* | 0.323* | 0.301* | 0.341* |
| `multilingual-e5-large`| 0.325* | 0.358 | 0.267* | 0.311* | 0.305* | 0.331 | 0.258* | 0.287 | 0.289* | 0.322* |
| `bge-m3` | 0.293 | 0.342 | 0.241* | 0.283* | 0.266 | 0.314 | 0.261* | 0.285 | 0.265* | 0.306* |
| `gte-Qwen2-1.5B-instruct`| 0.345* | 0.388* | 0.331* | **0.369*** | 0.351* | 0.393* | 0.291* | 0.310* | 0.330* | 0.365* |
| `gte-Qwen2-7B-instruct`| **0.416***| **0.456***| **0.332***| 0.367* | **0.409***| **0.435***| **0.321***| **0.348***| **0.369***| **0.402***|
| `Qwen3-Embedding-0.6B` | 0.331* | 0.378 | 0.258* | 0.293* | 0.316* | 0.365* | 0.240 | 0.252 | 0.286* | 0.322* |
| `Qwen3-Embedding-8B` | 0.403* | 0.445* | 0.317* | 0.349* | 0.381* | 0.426* | 0.285* | 0.311* | 0.347* | 0.383* |
| `gpt-4.1-mini` | 0.218 | 0.230(down)| 0.165 | 0.147(down)| 0.217 | 0.210(down)| 0.143 | 0.122(down)| 0.186 | 0.177(down)|
| `gpt-4.1` | 0.265 | 0.262 | 0.209 | 0.192 | 0.302* | 0.271 | 0.199 | 0.171(down)| 0.244* | 0.224(down)|
| `Qwen3-8B` | 0.111(down)| 0.104(down)| 0.086(down)| 0.078(down)| 0.121(down)| 0.111(down)| 0.082(down)| 0.070(down)| 0.100(down)| 0.091(down)|

![Cross Domain Performance](./images/rq_icl_size_cd.png)
*(Figure 5: Cross-domain setting performance at various sizes of interaction $m'$)*

ここでも一貫して、クロスドメイン推論においてもLLMよりTEMが優位であることが証明されました。

結論として、Training-FreeのCold-Startレコメンドにおいて、LLMリランカーを直接用いる構成が最適であるという世間的な仮定は誤りであり、LLMの監督に基づいて事前学習された強力なTEMを使用するアプローチのほうが、圧倒的に優れた精度かつスケーラビリティをもたらすことが示されました。
