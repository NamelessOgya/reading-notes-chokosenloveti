# Regular Expression Matching on Graphics Hardware for Intrusion Detection

本論文は、NVIDIA CUDAアーキテクチャを活用し、ネットワーク侵入検知システム（NIDS）におけるPCRE正規表現マッチング処理をGPU（GeForce 9800 GX2）にオフロードする高速マッチングエンジンを提案した研究である。状態爆発を考慮したハイブリッド構成やダブルバッファリング等の最適化を行い、人気NIDSである「Snort」へ統合してシステム評価を行っている。

---

## 背景

ネットワーク侵入検知システム（NIDS）はトラフィックをリアルタイムに監視し、シグネチャベースで脅威を検出する。攻撃パターンの高度化に伴い、従来の固定文字列照合からより柔軟で表現力の高い「正規表現（PCRE）」を用いた記述が広く普及している（Snortルールの約45%がPCREを含む）。

しかし、PCREマッチングはCPUやメモリ帯域に対する負荷が非常に高く、ギガビット級の高速ネットワーク環境下ではパケットドロップを招く最大のシステムボトルネックとなっていた。ASICやFPGAなどの専用ハードウェアによる高速化アプローチは、シグネチャの追加・更新などのルール変更に対する柔軟性に欠け、開発コストも極めて高い。本研究は、安価で汎用的な並列プロセッサ（GPGPU）のリソースを活用し、シグネチャ検索の柔軟性を維持したまま、Gbpsクラスのトラフィック検査を実現する並列正規表現エンジンのアーキテクチャを提案・実装した。

---

## 手法

提案エンジンは、あらかじめコンパイルされたDFAテーブルをGPUに配置し、パケットをまとめて転送して多数のスレッドで並列に走査する。

### 1. DFAコンパイルと状態爆発の回避（ハイブリッド手法）
正規表現をThompsonアルゴリズムでNFAにし、サブセット構築法でDFAへと変換する。DFAは文字消費ごとに遷移先が1つに決まるため、入力長 $n$ に対して $O(n)$ の定数時間スループットで動作する利点がある。

しかし、ワイルドカード（`.*`）や繰り返し（`a{x,y}`）を含む一部の正規表現は、DFA化すると状態空間が指数関数的に爆発し、GPUメモリ（GeForce 9800の512MB）を容易に逼迫する。
* **状態数しきい値の導入**:
  コンパイル中に状態数が上限しきい値 $S_{max} = 5000$ 状態を超えた場合、その正規表現のDFAコンパイルを中止する。
* **ハイブリッド検出方式**:
  しきい値（5,000状態）以下に収まる正規表現（全ルールの **97%以上**）はGPU上のDFAで超高速に並列スキャンする。状態爆発を起こす残りの少数（約3%未満）の正規表現は、CPU上のPCRE（NFA）で処理するハイブリッド構成をとることで、検出精度を100%維持しつつ大半の処理負荷をGPUへ分散した。

### 2. GPUデバイスメモリ階層への適応
* **DFA遷移テーブルのテクスチャメモリ配置**:
  DFAの遷移テーブル（状態数 $\times$ 256文字の2次元配列）へのアクセスは不規則であるため、通常のグローバルメモリではキャッシュの恩恵を受けられず、遅延が発生する。本研究では、事前に pre-allocate した1次元リニアメモリ領域をテクスチャキャッシュにバインドし、不規則なテーブル参照の遅延を隠蔽した。
* **検索オフセットの出力処理**:
  各スレッドは独立してパケットを走査し、正規表現と一致した箇所のパケット内オフセットを、グローバルメモリ上の出力配列に書き込む（Figure 5）。

### 3. データ転送とパケット分割最適化
* **ピン留めメモリとダブルバッファ**:
  ホスト・デバイス間の転送遅延を極小化するため、物理メモリに固定化されるページロック（Page-locked）メモリを割り当て、DMA経由で非同期転送を実行。ダブルバッファ構成を採用し、一方のバッファでGPU実行中に、他方でCPUが新規パケットを集約する。
* **再構築パケット（MTUサイズ超過）の分割処理**:
  TCPストリーム再構築 preprocessor（Stream5など）によって、MTU（1,500バイト）を大きく上回る巨大パケット（最大65,535バイト）が生成される。これをバッファの1行にそのまま割り当てると、配列のメモリ領域が極めて疎になり、無駄な転送コピーが生じる。
  本手法では、MTUサイズ以上の再構築パケットを **MTUサイズ以下のスライス** に細かく分割し、バッファの連続する行に格納する（Figure 4）。スライス境界でのパターンの一致漏れを防ぐため、スキャン時には「境界を跨いで最終状態（一致）または失敗状態に到達するまで」隣接スライスを追加で走査する。

### 数式

DFA を用いたマッチングの時間複雑度 $T$ は、入力ストリームの長さを $n$ とすると、検索するパターン数やその複雑さに依存せず、線形時間で抑えられる。

$$ T = O(n) $$

アルファベットサイズを $|\Sigma| = 256$ とし、DFA の状態数を $|Q|$ とすると、状態遷移テーブルのサイズ $M_{DFA}$ （バイト）は以下のようになる。

$$ M_{DFA} = 4 \times |Q| \times |\Sigma| = 1024 \times |Q| $$

---

## 結果

本研究で用いられたパターンセットおよび実績評価（Figure 1〜10）を以下に示す。

### 図表

![Figure 1: Regular expression matching in the Snort IDS](./images/figure_1.png)
**Fig. 1. Regular expression matching in the Snort IDS.**

![Figure 2: Overview of the regular expression matching engine in the GPU](./images/figure_2.png)
**Fig. 2. Overview of the regular expression matching engine in the GPU.**

![Figure 3: Packet buffer format](./images/figure_3.png)
**Fig. 3. Packet buffer format.**

![Figure 4: Matching packets that exceed the MTU size](./images/figure_4.png)
**Fig. 4. Matching packets that exceed the MTU size.**

![Figure 5: Regular expression matching execution model](./images/figure_5.png)
**Fig. 5. Regular expression matching on the GeForce 9800 with 128 stream processors.**

![Figure 6: States and memory requirements](./images/figure_6.png)
**Fig. 6. States (a) and memory requirements (b) for the 11,775 regular expressions contained in the default Snort ruleset when compiled to DFAs.**

![Figure 7: Sustained throughput for transferring packets](./images/figure_7.png)
**Fig. 7. Sustained throughput for transferring packets to the graphics card using virtual (a) and paged-locked (b) memory.**

![Figure 8: Computational throughput for regular expression matching](./images/figure_8.png)
**Fig. 8. Computational throughput for regular expression matching.**

![Figure 9: Sustained processing throughput for Snort using different network traces](./images/figure_9.png)
**Fig. 9. Sustained processing throughput for Snort using different network traces.**

![Figure 10: Sustained throughput for Snort when using only regular expressions](./images/figure_10.png)
**Fig. 10. Sustained throughput for Snort when using only regular expressions.**

---

## 使用したデータ

評価実験では、Snortのシグネチャデータおよび実際のネットワークトラフィックからキャプチャした3つのパケットトレースを使用しています。

### 1. 正規表現パターンセット（Figure 6）
* **データソース**: Snort 2.6のデフォルトルールセット（合計 7,179ルール）。その中に含まれる合計 **11,775個** のPCRE正規表現。
* **特性**: 状態数の上限を 5,000 に設定したところ、全体の **97%以上**（約11,400個）の正規表現が状態爆発を起こさずにDFAへコンパイル可能であった。この全DFAを格納するのに必要なメモリサイズは **200 MB未満**（Figure 6(b)）であり、デバイスメモリ内に収容可能。

### 2. 入力パケットトレース
実用に即した評価を行うため、I/Oボトルのない状態でメモリ上に完全にキャッシュした状態で以下の3つのトラフィックデータを使用。
* **U-Web**: ギリシャの大学（University of Crete）でキャプチャされた実際の HTTP Web トラフィック。総データ量 **194 MB**、280,088 パケット、4,711 フロー。
* **SCH-Web**: ギリシャのハイスクール教育ネットワーク接続リンクでキャプチャされた実 Web トラフィック。総データ量 **164 MB**、365,538 パケット、14,585 フロー。
* **LLI**: 1998-1999 DARPA侵入検知評価データセット（MIT Lincoln Lab）。軍事ネットワークトラフィックのシミュレーションであり、通常の通信に各種攻撃ベクトルを混入させたもの。総データ量 **382 MB**、1,753,464 パケット、86,954 フロー。

---

## 結果と考察

### 1. 状態空間のコンパクトな分布 (Figure 6)
* DFA状態数の累積分布（Figure 6(a)）より、正規表現の97%以上が5,000状態以下に収まっており、状態爆発を起こすものはごく一部であることが確認された。メモリ消費量も全体で約 200MB 以下であり（Figure 6(b)）、当時のビデオカードのメモリ容量に容易に収容可能であった。

### 2. ページロック転送の高速性 (Figure 7)
* ページロックメモリを用いた非同期DMA転送により、PCIe v2.0 x16接続において実効最大 **3.2 GB/s**（仮想メモリ経由に比べて約 1.5〜2倍高速）のパケット転送スループットを達成した。

### 3. テクスチャメモリの有効性 (Figure 8)
* DFAテーブルへのアクセスは不規則でキャッシュ効率が悪化しやすいが、これをテクスチャキャッシュにバインドした結果、グローバルメモリ配置（CPU比18倍）に比べて大幅にスループットが向上した。
* 4096パケットのバッファサイズにおいて、CPU（シングルコア）比で **最大 48.2 倍の高速化**（スループット **16 Gbit/s**）の超高速マッチングを実証した。

### 4. Snort統合後のシステムスループット向上 (Figure 9, 10)
* **最大 800% のシステム高速化**: 固定文字列照合（content）とPCRE正規表現照合の両方をGPUにオフロードした場合、Snortのシステム実効スループットは **最大 800 Mbit/s 以上** に達し、CPU単体での実行に対して **約 8 倍（800%）の高速化** を達成した（Figure 9(b)）。
* **最悪ケースにおける頑健性**: content プレフィルタを無効化し、すべてのパケットが20個のPCRE正規表現に対して強制的に走査される最悪ケースにおいても、GPU版は **700 Mbit/s 以上** を維持し、CPU版に対して常に 9〜10 倍高速であった（Figure 10）。

---

# chokosenlovetiのメモ  
## 使用したデータ  

本論文の評価実験では、Snort 2.6のデフォルトシグネチャと、実際のネットワーク環境からキャプチャした3つの異なる特性を持つパケットトレース（U-Web, SCH-Web, LLI）を用いて検証を行っています。

### 1. 正規表現ルールセット（Snort 2.6）
* **シグネチャ規模**: 7,179ルールから抽出された計 **11,775個** のPCRE正規表現。
* **特性**: 状態数しきい値を 5,000 状態に制限することで、全体の97%以上が状態爆発を起こさずにDFAとしてGPUメモリ（総メモリ量200MB以下）に保持可能であることを示しました。

### 2. 評価用ネットワークパケットトレース
* **U-Web**: ギリシャの大学で収集された実際の HTTP ウェブトラフィック。サイズ **194 MB**、280,088 パケット、4,711 フロー。
* **SCH-Web**: ハイスクール教育ネットワークのアクセスリンクで収集された実 HTTP ウェブトラフィック。サイズ **164 MB**、365,538 パケット、14,585 フロー。
* **LLI**: DARPA intrusion detection evaluation set（MIT Lincoln Lab）のシミュレーショントラフィック。軍事ネットワーク風のバックグラウンドトラフィックに当時の攻撃を混入させたもの。サイズ **382 MB**、1,753,464 パケット、86,954 フロー。
