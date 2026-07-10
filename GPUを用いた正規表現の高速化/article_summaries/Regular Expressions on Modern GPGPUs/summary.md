# Regular Expressions on Modern GPGPUs

本論文は、最新のGPGPUアーキテクチャ（Compute Capability 8.6）において、スレッド占有率（Thread Occupancy）の低下を防ぐコンパイルチューニング（レジスタ数、ブロックサイズ、共有メモリ）や、文字列プレフィルタリング、および先頭ワイルドカードによる状態遷移ループを回避する最適化（ASyncAP_Optimized）を提案し、ロバストで汎用的な超高速正規表現マッチングを実現した研究である。

---

## 背景

GPUを用いた正規表現（RE）マッチングの高速化は非常に効果的であり、CPU単一スレッドに比べて数桁高速な処理を達成してきた。しかし、従来の多くの手法（`iNFAnt` など）は10年以上前の古いGPUモデル上で開発されており、かつネットワークパケットインスペクションという特定のドメインに特化していた。また、そうした古い世代の設計思想を現代のより強力なGPUに単純に適用すると、スレッド占有率が極端に低くなり、GPUの持つ真の並列性能を引き出すことができないという課題がある。

さらに、先行研究の `ASyncAP` などの最新の並列アルゴリズムでは、正規表現の先頭にワイルドカード（`.*`）やその繰り返しが含まれるパターンにおいて、すべてのスレッドが不要な遷移ループに入り浸ってテキスト全体を走査し続けてしまい、最悪ケースの計算負荷によって処理性能がCPU単一スレッド以下に破綻する問題があった。本研究は、現代のGPUハードウェア特性に最適化した実行パラメータの自動選定と、ワイルドカードによる最悪計算を回避するアルゴリズム的アプローチによって、これらのボトルネックを排除した。

---

## 手法

本手法は、(1) 文字列ベースのプレフィルタリング、(2) 先頭ワイルドカードを迂回する縮小NFAによるマッチング（ASyncAP_Optimized）、(3) GPU実行リソースの最適パラメータ設計からなる。

### 1. 文字列プレフィルタ（Prefiltering）
正規表現による有限オートマトンの遷移は計算コストが高い。一方、特別な記号を含まない固定文字列の照合（Literal Matching）は非常に低コストである。
* **プレフィルタ抽出**: 各正規表現パターンから、特別なRE記号（ワイルドカードや文字クラス等）を含まない最長の部分文字列をプレフィルタ用パターンとして抽出する（例: `[?&]configName=[&]+(script|onload|src)[ˆ]` というREから `configName=` を抽出）。
* **文字列ベースの並列KMP（Knuth-Morris-Pratt）**:
  従来の並列KMPはスレッドごとに異なる「パターン」を割り当てていたため、パターン数が少ない場合にスレッドが余ってしまい、最新GPUを満たせなかった。本手法では、入力をバッファリングして十分長い文字列を作り、スレッドごとに入力文字列の「セグメント（部分配列）」を割り当てて並列に検索を行う。セグメント境界でのパターン一致漏れを防ぐため、パターン長 $n$ に対し、$n$ バイトのオーバーラップを設けて隣接セグメント間で冗長検索を実行する（Figure 2）。
* プレフィルタが不一致の場合はRE照合自体をスキップし、一致した場合のみ後続のRE照合を実行する。

### 2. 先頭ワイルドカードの回避 (ASyncAP_Optimized)
先行研究 `ASyncAP` （Liuら, 2023）は、テキストをブロックに分割し、各スレッドが異なる開始位置からNFAの照合を実行するが、正規表現の先頭にワイルドカード（`.*`）が含まれる場合、全スレッドが初期のループ状態にトラップされ、テキスト全体を走査し続けるため最悪時間複雑度 $O(mn^{2})$ （ $m$ : NFAサイズ、 $n$ : 入力長）に陥り、性能が著しく低下する。
* **到達容易な状態（Easy-to-reach states）の特定**:
  NFAコンパイル時に各状態の入次数（in-degree）を記録し、入次数がしきい値（本研究では100）を超える状態を到達容易な状態と定義する。
* **Reduced NFA（縮小NFA）の構築**:
  初期状態0に接続される到達容易な状態、またはそれらに接続される状態を「スキップ状態（skip state）」としてマークし、これらを取り除いた「Reduced NFA」を構築する。
* **ハイブリッドスクリーニング**:
  まず Reduced NFA で検索を行い、一致が見つかった場合にのみ、後方検査用のサブNFAを用いて、スキップされた部分が条件を満たしているかを検証する。これにより、先頭のワイルドカードによるスレッドのトラップを完全に回避した。

### 3. GPU実行パラメータの最適チューニング
最新のGPUアーキテクチャ（Compute Capability 8.6、RTX 3060等）は、1基のSM（Streaming Multiprocessor）あたり最大 1,536 スレッド、最大 65,536 個の32ビットレジスタを備える。
* **レジスタ数制限の制御**:
  スレッドあたりのレジスタ数を増やすとメモリアクセスを減らせるが、多すぎると同時実行スレッド数が制限される。プロファイリングの結果、スレッドあたり **42レジスタ** が最適であり、このときSMあたり3つのブロック（512スレッド/ブロック $\times$ 3 = 1,536スレッド）が同時実行でき、最高のキャッシュヒット率と 100% の理論占有率（Occupancy）を維持できることを特定（Figure 3）。
* **ブロックサイズの決定**:
  各ブロックは最大 99 KB の共有メモリを使用でき、本アルゴリズムはブロックあたり 32 KB を要求するため、SMあたり最大3ブロック配置可能。したがって、最適なブロックサイズは $1536 / 3 = 512$ スレッド/ブロックと決定した。

### 数式

ASyncAP のワイルドカード時の最悪時間複雑度 $T_{worst}$ は、NFAサイズを $m$ 、入力長を $n$ とすると以下のように表される。

$$ T_{worst} = O(mn^{2}) $$

文字列並列KMPにおいて、スレッド $k$ に割り当てられるスキャン範囲の開始インデックス $i$ と終了インデックス $j$ は、パターン長を $n$ とすると以下のようになる。

$$ i = n \times \text{index} $$

$$ j = n \times (\text{index} + 2) - 1 $$

各SMあたり最大同時実行スレッド数（Compute Capability 8.6）は 1,536 スレッドであり、レジスタ数制限および共有メモリ制限から、1ブロックあたりのスレッド数を 512 とし、SMあたりの同時実行ブロック数 $B_{SM}$ は次のように最適化される。

$$ B_{SM} = \frac{65,536}{512 \times 42} \approx 3 \text{ ブロック} $$

---

## 結果

本研究で用いられた実績評価（Table 1〜6、Figure 1〜6）を以下に示す。

### 図表

![Figure 1: Illustration of the ASyncAP](./images/figure_1.png)
**Figure 1: Illustration of the ASyncAP.**

![Figure 2: Illustration of the string-based task distribution](./images/figure_2.png)
**Figure 2: Illustration of the string-based task distribution.**

![Figure 3: NSight Compute Occupancy Analysis](./images/figure_3.png)
**Figure 3: NSight Compute Occupancy Analysis.**

![Figure 4: CUDA-KMP performance over #threads/block](./images/figure_4.png)
**Figure 4: CUDA-KMP performance over #threads/block.**

![Figure 5: CUDA-KMP occupancy over #threads/block](./images/figure_5.png)
**Figure 5: CUDA-KMP occupancy over #threads/block.**

![Figure 6: iNFAnt execution time over #threads/block](./images/figure_6.png)
**Figure 6: iNFAnt execution time over #threads/block.**

#### Table 1: Hardware specifications
| Component | Specification |
| :--- | :--- |
| **CPU** | Intel Core i5-10500H |
| **Memory** | DDR4 8GB $\times$ 2 |
| **GPU** | NVIDIA GeForce RTX 3060 Laptop |

#### Table 2: Software specifications
| Component | Specification |
| :--- | :--- |
| **OS** | Ubuntu 22.04.3 LTS |
| **Driver** | NVIDIA Display Driver version 535.104.05 |
| **SDK** | CUDA 12.2 |
| **Tool** | NSight Compute 2023.2.2 |

#### Table 3: CPU vs CUDA
| Method | Execution Time |
| :--- | :---: |
| **CPU** | 1823 ms |
| **CUDA-KMP** | 22 ms |

#### Table 4: Performance with different RE size (LW stands for Large with Wildcard)
| Method | S | M | L | LW |
| :--- | :---: | :---: | :---: | :---: |
| **CPU** | 5028 ms | 5523 ms | 7532 ms | 7334 ms |
| **iNFAnt** | 768 ms | 810 ms | 1301 ms | 1218 ms |
| **ASyncAP** | 18 ms | 25 ms | 38 ms | 71946 ms |
| **ASyncAP_Optimized** | 20 ms | 26 ms | 40 ms | 38 ms |

#### Table 5: Detailed ASyncAP vs ASyncAP_Optimized
| RE_ID | ASyncAP | ASyncAP_Optimized |
| :--- | :---: | :---: |
| **184** | 59886 ms | 24 ms |
| **1637** | 129885 ms | 36 ms |
| **2421** | 33456 ms | 65 ms |
| **19** | 123289 ms | 36 ms |
| **2416** | 33453 ms | 65 ms |
| **1584** | 153479 ms | 59 ms |
| **266** | 128636 ms | 26 ms |
| **1815** | 525 ms | 27 ms |
| **197** | 536 ms | 27 ms |
| **1802** | 56307 ms | 15 ms |

#### Table 6: RE matching with prefiltering
| Method | S | M | L |
| :--- | :---: | :---: | :---: |
| **iNFAnt** | 84.6 ms | 113.5 ms | 149.8 ms |
| **ASyncAP** | 10.1 ms | 14.2 ms | 16.8 ms |
| **ASyncAP_Optimized** | 10.2 ms | 14.2 ms | 17 ms |

---

## 使用したデータ

評価実験では、Snortのシグネチャデータベースから抽出された正規表現パターンと、それらを評価するためのパケットデータ（コーパス）を生成して使用しています。

### 1. 正規表現パターンセット（Table 4）
* **データソース**: 先行研究のテストアセンブリ（ANMLZooなど）と同一の、**Snort** から抽出された **3,379個** の正規表現（RE）パターン。
* **カテゴリ分類**: 正規表現の状態遷移を表すエッジ（状態間遷移の数）の規模に基づいて、以下の3クラスに分類して評価。
  * **S (Small)**: エッジ数が 100 未満。
  * **M (Medium)**: エッジ数が 100 以上 500 以下。
  * **L (Large) / LW (Large with Wildcard)**: エッジ数が 500 超。特に `LW` クラスは、先頭にワイルドカード（`.*` 等）を含み、最悪計算を誘発するパターン。

### 2. 評価用テキストコーパス
* **構成**: 実際のDeep Packet Inspection（DPI）やWebトラフィックを代表するデータとして、**HTTPコード、SQLクエリ** などを含むパケットペイロードを模したテキストデータ。
* **生成方法**: ChatGPT API [8] を用いて生成された、実環境に近い高リアリティなテキストコーパス。

---

## 結果と考察

### 1. プレフィルタリング技術の効果 (Table 6)
* プレフィルタリング（Literal Prefiltering）を組み込むことにより、正規表現オートマトンの大半の走査負荷が事前に取り除かれた。
* これにより、元々処理効率の悪かった `iNFAnt` アルゴリズムにおいて、マッチング時間が 768ms〜1301ms から 84.6ms〜149.8ms へと **約 10 倍の劇的な高速化** を達成した。
* 最適化された `ASyncAP_Optimized` においても、約 80% のさらなる高速化が得られ、DFAを用いずとも極めて高速なスキャンが維持されることを示した。

### 2. 先頭ワイルドカードに対するロバスト性 (Table 4, 5)
* 先行研究の `ASyncAP` は、通常のパターン（S, M, L）では優れた並列性能を示したものの、先頭にワイルドカードを含む `LW` パターンでは、スレッドのトラップによって計算時間が **71,946 ms**（CPU単一スレッドの約10倍遅い）に急激に破綻する。
* 一方、提案する `ASyncAP_Optimized` は、スキップ状態マークと Reduced NFA の導入によってワイルドカードのトラップを完全に回避し、`LW` パターンにおいても **38 ms** の高速処理を維持。これは ASyncAP 比で **約 1,900 倍**、CPU比で **約 190 倍** の圧倒的なパフォーマンス向上である。
* 個別の難解ルール評価（Table 5）においても、ASyncAP で 153,479 ms（約2.5分）以上かかっていたマッチング処理を、わずか **59 ms** で完了（約 2,600 倍の高速化）させており、最悪ケースに対する極めて優れた頑健性を実証した。

### 3. GPU実行パラメータチューニングの妥当性 (Figure 3〜5)
* スレッドあたりのレジスタ数を 42 に設定し、ブロックサイズを 512 としたことで、最新の RTX 3060 アーキテクチャにおいて 100% の理論 occupancy（スレッド占有率）を維持しながら、最も高いキャッシュヒット率を両立させることに成功した。
* これにより、ブロックサイズが小さいために occupancy が低迷していた `iNFAnt` の課題を克服し、全体として `iNFAnt` 比で **約 40 倍** のスループット向上を達成した。

---

# chokosenlovetiのメモ  
## 使用したデータ  

本論文の評価実験では、Snortルールから抽出された大規模正規表現ルールセットと、ChatGPT APIを用いて生成された実用的なネットワークパケットコーパス（DPI検査用）を使用しています。

### 1. 正規表現ルールセット（ANMLZoo / Snort）
* **ルール規模**: Snortデータベースより抽出された計 **3,379個** の正規表現（RE）パターン。
* **特性分類**: ルールの複雑さ（オートマトンの遷移エッジ数）に基づき、Small（100未満）、Medium（100〜500）、Large（500超）、および最悪ケースを引き起こす先頭ワイルドカードを含む Large with Wildcard (LW) の4グループに分類して評価に使用。

### 2. 評価用ネットワークパケットコーパス
* **構成**: NIDS（Snort等）によるDeep Packet Inspectionの現実的なワークロードを模したデータセット。
* **データ内容**: ChatGPT APIを介して動的に生成された、実際のネットワーク通信で多用される **HTTPコード** および **SQLクエリ** などを含むパケットペイロードテキスト。
