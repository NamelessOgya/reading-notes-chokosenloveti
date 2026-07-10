# Parallelization and Characterization of Pattern Matching using GPUs

本論文は、NVIDIA CUDAアーキテクチャを活用し、GPU上の異なるメモリ階層が決定性有限オートマトン（DFA）ベースのパターンマッチングに与える影響を体系的に特徴づけ（Characterize）、PCIeバス転送のオーバーヘッドを解消するインデックス型パケットバッファを提案することで、実効数十Gbpsの超高速パターンマッチングを実現した研究である。

---

## 背景

ネットワーク侵入検知システム（NIDS）やスパムフィルタ、アンチウイルス等のコンテンツセキュリティ監視において、膨大なシグネチャパターンと入力パケットストリームをリアルタイムに走査する「パターンマッチング」は最も計算負荷の高いボトルネックである。

ASICやFPGAなどの専用ハードウェアは高速だが、プログラムの書き換えやメンテナンスコストが高い。一方、安価で大量の処理コアを備えるGPU（Commodity GPU）は、パケットごとにスレッドを割り当てるデータ並列性との相性が極めて良く、高速化のプラットフォームとして注目されてきた。しかし、ホスト（CPU）とデバイス（GPU）を接続するPCIeバスの転送オーバーヘッドや、GPUの複雑なメモリ階層（グローバル、テクスチャ、キャッシュなど）におけるデータ配置が性能に与える影響については体系的に明らかにされていなかった。本研究は、GPUを用いたDFAベースのパターンマッチングライブラリを設計・実装し、メモリ配置とデータ転送の最適化手法を提案・評価したものである。

---

## 手法

提案ライブラリは、固定文字列検索と正規表現マッチングの両方をサポートし、各入力パケットを別々のGPUスレッドに分散して、スレッド間で同期なく完全に独立して並列走査を行う。

### 1. PCIeバス転送の最適化（インデックス型パケットバッファ）
GPUへのパケット転送はPCIeバスのデータ転送コストがボトルネックとなる。特に小さいパケットを個別に転送すると、DMAやPCIeの制御オーバーヘッドが大きくなる。

従来の固定バケット型バッファ（Figure 2(a)）では、各パケットに一定の最大サイズ（例: 1500バイト）を確保して転送していた。このため、小さなパケット（100バイトなど）の場合、バッファ領域の約 $14 / 15$ が空のまま無駄に転送され、有効帯域幅が極端に低下していた。

提案する **インデックス型パケットバッファ（Indexed Packet Buffer）** （Figure 2(b)）では、すべてのパケットをメモリ上に隙間なく（back-to-back）連続して配置し、各パケットの開始位置を示すオフセット値を「インデックス配列」としてパケットデータの先頭に格納して一括DMA転送する。これにより、無駄なデータ転送を一切排除しつつ、各スレッドがスレッドIDをインデックスとして独自のパケット位置を直接取得してスキャンできるようにした。

### 2. GPUデバイスメモリ階層のキャラクタライズと最適化
* **DFA遷移テーブルの配置とキャッシュスラッシング**:
  DFAの遷移テーブル（状態数 $\times$ 256文字の2次元配列）へのアクセスは、入力文字に依存して極めて不規則（ランダム）になる。遷移テーブルを2Dテクスチャとしてマップすると、2次元空間の局所性キャッシュが不規則なDFAアクセスと衝突し（Cache Thrashing）、著しく性能が低下する（Figure 6）。DFA遷移テーブルに関しては、通常のグローバルメモリまたは1Dテクスチャメモリでのアクセスが最善（グローバルメモリの方が約10%高速）である。
* **パケットデータへのテクスチャアクセス**:
  逆に、入力パケットデータへのアクセスはスレッド内で連続的であるため、2Dテクスチャの空間局所性キャッシュが有効に機能し、2Dテクスチャにパケットを配置することでグローバルメモリ配置よりも50%高速化した。
* **ワードアクセス幅の最適化（`int4`データの活用）**:
  通常、パケットデータは1バイト（char）単位で処理されるが、GPUのグローバルメモリへの1回のアクセスは最小32バイトである。1バイトずつフェッチすると帯域の多くが切り捨てられ、メモリ帯域幅の利用率が低下する。
  本研究では、各スレッドが一度に 16バイト（`int4`）を一度にレジスタにフェッチ（Fetch）する設計を提案した（Figure 5）。16バイト単位のフェッチにより、メモリトランザクションの数を激減させ、1バイト単位に比べて処理スループットを数倍高速化した。

### 数式

DFA を用いたマッチングの時間複雑度 $T$ は、入力ストリームの長さを $N_{input}$ とすると、検索するパターン数やその複雑さに依存せず、線形時間で抑えられる。

$$ T = O(N_{input}) $$

アルファベットサイズを $\Sigma$ （ASCII文字コードより 256 文字）とし、DFA の状態数を $|Q|$ とすると、GPU 上に確保される状態遷移テーブルの総メモリサイズ $M_{DFA}$ （バイト）は、各遷移先ポインタを 4 バイトとして以下のように表される。

$$ M_{DFA} = 4 \times |Q| \times |\Sigma| = 1024 \times |Q| $$

---

## 結果

本研究で用いられたパターンセットの特性（Table 3）および各手法の実績評価（Table 1〜2、Figure 1〜10）を以下に示す。

### 図表

![Figure 1: The DFA state machine and the state transition table](./images/figure_1.png)
**Figure 1. The DFA state machine (a) and the state transition table (b) for the regular expression $(abc^{+})^{+}$.**

![Figure 2: Different packet buffer formats](./images/figure_2.png)
**Figure 2. Different packet buffer formats.**

![Figure 3: DFA matching on the GPU](./images/figure_3.png)
**Figure 3. DFA matching on the GPU.**

![Figure 4: Multi-thread pattern matching on the GPU](./images/figure_4.png)
**Figure 4. Multi-thread pattern matching on the GPU.**

![Figure 5: Impact of word accesses when fetching data](./images/figure_5.png)
**Figure 5. Impact of word accesses when fetching data from the global device memory.**

![Figure 6: Memory accesses impact on DFA matching](./images/figure_6.png)
**Figure 6. Memory accesses impact on DFA matching.**

![Figure 7: Throughput sustained including data transfers](./images/figure_7.png)
**Figure 7. Throughput sustained including data transfers.**

![Figure 8: Buckets versus Index Packet Buffer](./images/figure_8.png)
**Figure 8. Buckets versus Index Packet Buffer.**

![Figure 9: Overall throughput for different pattern numbers](./images/figure_9.png)
**Figure 9. Overall throughput for different pattern numbers.**

![Figure 10: Performance sustained on different GPU/CPU models](./images/figure_10.png)
**Figure 10. Performance sustained by our pattern matching implementation with all optimizations described in Section 3.3, on different generation of GPU and CPU models.**

#### Table 1. Regular expression operations.
| Name | Reg. Expr. | Designation |
| :--- | :---: | :--- |
| Epsilon | ǫ | `""` |
| Character | $\alpha$ | For some character $\alpha$. |
| Concatenation | $RS$ | Denoting the set $\{\alpha\beta \mid \alpha \text{ in } R \text{ and } \beta \text{ in } S\}$. <br>e.g., $\{"ab"\}\{"d", "ef"\} = \{"abd", "abef"\}$ |
| Alternation | $R \mid S$ | Denoting the set union of $R$ and $S$. <br>e.g., $\{"ab"\} \mid \{"d", "ef"\} = \{"ab", "d", "ef"\}$. |
| Kleene star | $A^{*}$ | Denoting the smallest super-set of $R$ that contains ǫ and is closed under string concatenation. <br>This is the set of all strings that can be made by concatenating zero or more strings in $R$. <br>e.g., $\{"ab", "c"\}^{*} = \{\text{ǫ}, "ab", "c", "abab", "abc", "cab", "ababab", \dots\}$ |

#### Table 2. Data transfer rate between host and device (Gbit/s).
| Buffer Size | 1KB | 4KB | 64KB | 256KB | 1MB | 16MB |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Host to Device** | 2.04 | 7.1 | 34.4 | 42.1 | 44.6 | 45.7 |
| **Device to Host** | 2.03 | 6.7 | 21.1 | 23.8 | 24.6 | 24.9 |

#### Table 3. Memory requirements and properties of each pattern set.
| Pattern Set | # Patterns | Min./Max./Avg. Pattern | DFA Size |
| :--- | :---: | :---: | :---: |
| **SET1** | 2,000 | 5/34/19.42 | 33.02 MB |
| **SET2** | 10,000 | 5/34/19.57 | 162.14 MB |
| **SET3** | 30,000 | 5/34/19.57 | 478.36 MB |
| **SET4** | 50,000 | 5/34/19.53 | 799.76 MB |

---

## 使用したデータセット

評価実験では、パケットサイズやパターン数が性能に与える影響を厳密に制御するため、以下の合成データセット（合成シグネチャパターンおよび合成パケットデータ）を使用しています。

### 1. 正規表現パターンセット（Table 3）
* **生成方法**: ASCIIアルファベットから一様分布に従って完全にランダムに生成された合成パターン。
* **ルールセット規模**: パターン数 **2,000（SET1）**、**10,000（SET2）**、**30,000（SET3）**、**50,000（SET4）** の4種類。長さは最小5文字、最大34文字、平均約19.5文字。
* **特性**: パターン数が増加するにつれて、コンパイル後のDFAのメモリサイズは 33.02 MB から **799.76 MB** までスケーラブルに増加する。

### 2. パケットデータ
* **構成**: パターンセットと同様にASCIIアルファベットからランダムに合成生成された、高エントロピーなネットワークパケット（スレッドブロックのほぼすべての実行パスを強制的に走査させるため）。
* **パケットサイズ**: 性能特性を評価するため、**100, 200, 400, 800, 1500 バイト** の各種パケットサイズを設定した。

---

## 結果と考察

### 1. ワードアクセス幅の拡大による劇的な性能向上 (Figure 5)
* パケットデータを1バイト単位でフェッチすると、最小トランザクションサイズ（32バイト）の制限からメモリ帯域幅が無駄になり、スループットは 10 Gbit/s 程度で頭打ちになる。
* 一方、`int4` を用いて 16バイト単位で一括フェッチすることで、トランザクション数が激減し、スループットは **最大 120 Gbit/s** まで劇的に向上（12倍の高速化）した。スレッド数を 24,576 以上に増やすことでメモリ遅延が完全に隠蔽された。

### 2. メモリ階層ごとのキャラクターの選定 (Figure 6)
* **DFAテーブルの最適配置**: 不規則なメモリアクセスが発生する DFA 遷移テーブルは、空間局所性が悪いため、2Dテクスチャに配置するとキャッシュスラッシングにより性能が 10 Gbit/s 以下に破綻する。L1キャッシュが有効機能する通常の **グローバルメモリ** （または 1D テクスチャ）への配置が最善（約 190 Gbit/s）である。
* **パケットデータの最適配置**: 一方、パケットデータは各スレッドがシーケンシャルに読み出すため、空間局所性を有する **2Dテクスチャメモリ** に配置することで、グローバルメモリ配置より 50% 程度高速化した。

### 3. PCIe転送を考慮した実効性能とインデックス型バッファの効果 (Figure 7, 8)
* GPU単体の計算処理は 186 Gbit/s に達するが、PCIeバス経由のデータ転送を含めると、実効スループットはフルペイロード（1500バイト）で **27.1 Gbit/s** に制限される。
* さらに従来の固定バケット型バッファでは、小さなパケット（100バイト）の際にバッファの大部分が空のまま転送され、実効スループットは 1.4 Gbit/s に急降下していた。
* 提案する **インデックス型パケットバッファ** は、パケットを隙間なく連続配置したことで、100バイトの極小パケットにおいても **6.49 Gbit/s** （約 5倍の性能向上）の実効スループットを維持した。これは、CPUコア換算で 8.75 コア分、1500バイトでは 41.2 コア分に相当する。

### 4. パターン数に対する一定のスループット特性 (Figure 9)
* 検索するパターン数を 2,000 から 50,000 へと大幅に増加させても、実効スループットは 27.1 Gbit/s で完全に一定であった。DFAの持つ $O(N_{input})$ の時間複雑度が実証され、セキュリティシグネチャが急増する実用環境での有用性が示された。
  
# chokosenlovetiのメモ  
## 使用したデータ  

本論文の評価実験では、パケットサイズやパターン数が性能に与える影響を厳密に制御・分離するため、以下の合成データセット（合成シグネチャパターンおよび合成パケットデータ）を使用しています。

### 1. 正規表現パターンセット（Table 3）
* **生成方法**: ASCIIアルファベットから一様分布に従って完全にランダムに生成された合成パターン。
* **ルールセット規模**: パターン数 **2,000（SET1）**, **10,000（SET2）**, **30,000（SET3）**, **50,000（SET4）** の4種類。長さは最小5文字、最大34文字、平均約19.5文字。
* **特性**: パターン数が増加するにつれて、コンパイル後のDFAのメモリサイズは 33.02 MB から **799.76 MB** までスケーラブルに増加します。

### 2. パケットデータ
* **構成**: パターンセットと同様にASCIIアルファベットからランダムに合成生成された、高エントロピーなネットワークパケット（スレッドブロックのほぼすべての実行パスを強制的に走査させ、最悪実行時間を評価するため）。
* **パケットサイズ**: 転送帯域幅の特性を評価するため、**100, 200, 400, 800, 1500 バイト** の各種パケットサイズを設定して評価しました。

