# GPUを用いた正規表現の高速化 論文調査まとめ

本ドキュメントでは、GPUを活用した大規模データセットに対する正規表現マッチングの高速化技術に関する調査要約をまとめています。

---

## 調査済み論文の総合比較

各論文の発表年、対象オートマトン、および提案手法の概要を以下の表に示します。

### 1. 論文概要および手法の比較
| 論文略称 | 発表年 | 発表会議 | オートマトン | 提案手法の概要 |
| :--- | :---: | :---: | :---: | :--- |
| **Yu (2013)** | 2013年 | CF '13 | DFA / NFA | **拡張圧縮DFA（E-DFA）** を提案。遷移レイアウトを規則化（4/8遷移にアライメント）し、DFAの課題であるスレッドの分岐発散（Warp Divergence）を抑制。 |
| **Zu (2012)** | 2012年 | PPoPP '12 | NFA | **仮想NFA（Virtual NFA）** を提案。同時に活性化しない状態群を「互換性グループ」とし、その組み合わせを仮想状態化。パケットあたりの必要スレッド数を 4 に固定し、1ワープ（32スレッド）で8パケットの同時並列処理を実現。 |
| **Vasiliadis (2011)**| 2011年 | IISWC '11 | DFA | **インデックス型パケットバッファ** を提案。パケットを隙間なく連続配置し、DMA転送の無駄を排除。さらに `int4` を用いた16バイト一括フェッチ（ワードアクセス幅の最適化）により、グローバルメモリ参照を劇的に高速化。 |
| **Vasiliadis (2009)**| 2009年 | RAID '09 | DFA / NFA | **ハイブリッド型DFA/NFA** を提案（Gnortの拡張）。状態数が5,000状態以下のPCRE正規表現（全体の97%以上）はGPU上のDFAで超高速処理し、状態爆発を起こす少数の表現のみをCPU（NFA）で処理。 |
| **Li (2024)** | 2024年 | GPGPU '24 | NFA | **ASyncAP_Optimized** を提案。先頭のワイルドカード（`.*`）による不要なトラップ（最悪計算量 $O(mn^{2})$）を回避するため、入次数に基づきスキップ状態を取り除いた「縮小NFA（Reduced NFA）」で走査。KMPによる固定文字列プレフィルタリングも導入。 |

---

## 評価用データセットの比較（星取表）

各論文が性能検証に用いた「正規表現ルールセット（パターンデータ）」および「評価用パケットデータ（コーパス）」の利用状況を星取表形式で示します。

| 論文略称 (発表年) | Snort実ルール | 合成パターン | 実ネットワークトレース<br>(Web / DARPA等) | ChatGPT生成パケット<br>(HTTP / SQL等) | 合成トラフィック<br>(混入確率 $p_{M}$ 制御等) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Yu (2013)** | ★ | | | | ★ |
| **Zu (2012)** | ★ | | | | ★ |
| **Vasiliadis (2011)**| | ★ | | | ★ |
| **Vasiliadis (2009)**| ★ | | ★ | | |
| **Li (2024)** | ★ | | | ★ | |

* **★**: 検証で使用された主要データ

---

## 評価データセットに関する詳細解説

性能検証に用いられた主要なデータソースである「Snortの実用ルール（ANMLZoo/AutomataZoo）」および「合成トラフィック（Becchi 2008）」についての詳細と背景技術は以下の通りです。

### 1. Snort実ルール（シグネチャデータ）
* **Snort（スノート）とは**:
  Webサービスやクラウド製品名ではなく、オープンソースの **「ネットワーク侵入検知/防御システム（NIDS/NIPS）ソフトウェア」** です。パケットペイロードを検査し、登録された「攻撃のシグネチャ（記述ルール）」に合致する不正パケットをローカル環境で検出します。このシグネチャオプションにPCRE形式の正規表現（ `pcre` ）が多用されています。
  * **プレフィルタ機能**: 正規表現（PCRE）照合は計算負荷が高いため、まず固定文字列（ `content` ）を高速検索し、一致した場合のみPCREを実行する二段階のフィルタリング設計が採られています。
  * **状態爆発のボトルネック**: 正規表現をDFAにコンパイルする際、ワイルドカード（ `.*` ）等の繰り返し演算があると状態数が指数関数的に急増（状態爆発）するため、状態しきい値制限（5,000状態等）を設け、爆発するルールはCPU上のNFAに切り替えるハイブリッド方式がとられます。
* **ANMLZoo / AutomataZoo**:
  GPUやオートマトン処理専用プロセッサを評価するために整備された **「ベンチマーク用データセット名（リポジトリ名）」** です。Snortの実シグネチャから正規表現を抽出したファイル（例: `snort.1chip.regex`）や、評価用パケット入力データ（inputs）がGitHub（ `jackwadden/ANMLZoo` 等）で公開されています。

### 2. 合成トラフィック（パケットデータ）
* **手法（ソース文献）**:
  * **M. Becchi, M. Franklin, and P. Crowley. *"A workload for evaluating deep packet inspection architectures."* (IEEE IISWC 2008)**
* **アルゴリズム（ $p_{M}$ 制御の仕組み）**:
  検証対象のオートマトン構造を入力とし、**悪意あるデータの混入確率（ $p_{M}$ : Malicious transition probability）** に基づいてパケットのペイロードを1バイトずつ動的に生成する確率的文字生成器です。
  * 確率 **$p_{M}$** で、DFA/NFAの「開始状態から離れて、より深い状態へと遷移させる（＝パターンの一致を誘発し、活性状態を増やす）」文字を選択して出力します。
  * 確率 **$1 - p_{M}$** で、ASCII文字セットから一様ランダムに文字を選択して出力します。
* **評価における意義（GPUのストレス検証）**:
  通常トラフィック（低 $p_{M}$ ）ではスループットが極めて高くなりますが、攻撃トラフィック（高 $p_{M}$ ）ではDFAのキャッシュスラッシングやNFAの並列遷移爆発が発生します。これにより、GPUの「分岐発散（Warp Divergence）」や「メモリ遅延」が顕在化する **最悪ケースの頑健性** を測定できます。

---

## 調査済み論文一覧

各論文のより詳細な要約ドキュメントへのリンクと要約です。

### 1. [GPU Acceleration of Regular Expression Matching for Large Datasets: Exploring the Implementation Space](./article_summaries/GPU%20Acceleration%20of%20Regular%20Expression%20Matching%20for%20Large%20Datasets:%20Exploring%20the%20Implementation%20Space/summary.md)
* **著者**: Xiaodong Yu, Michela Becchi (University of Missouri - Columbia)
* **発表会議**: ACM Computing Frontiers (CF '13)
* **概要**: 
  実用的な規模と複雑さを持つデータセットを用いて、GPU上で異なるオートマトン表現（NFA、DFA）およびメモリ最適化技術（メモリ圧縮、アライメントによる分岐発散抑制、共有メモリキャッシュ等）を網羅的に評価した研究。
  DFAの状態爆発を緩和する「マルチDFA」や「デフォルト遷移圧縮（C-DFA）」の課題であるスレッドの分岐発散（Warp Divergence）を解決するため、状態レイアウトを規則化（4/8遷移にアライメント）した「拡張圧縮DFA（E-DFA）」を提案。E-DFAにより、従来の圧縮DFAに比べて **3〜5倍の高速化** を達成した。

### 2. [GPU-based NFA implementation for memory efficient high speed regular expression matching](./article_summaries/GPU-based%20NFA%20implementation%20for%20memory%20efficient%20high%20speed%20regular%20expression%20matching/summary.md)
* **著者**: Yuan Zu, Ming Yang, Zhonghu Xu, Lin Wang, Xin Tian, Kunyang Peng, Qunfeng Dong (University of Science and Technology of China)
* **発表会議**: ACM PPoPP '12
* **概要**: 
  DFAの状態爆発問題に対するアプローチとして、メモリ効率が線形で優れたNFAをGPUにマッピングするための最適化を提案した研究。
  同時に活性化しない状態群をまとめる「互換性グループ」と「活性状態配列」、CPUでのパケット配置を32バイトスライスに分割してインターリーブさせることでグローバルメモリの参照を合体（Coalesce）させる「パケットインターリーブ」を構築。
  さらに、スーパーグループの組み合わせを「仮想状態」として再定義する「**仮想NFA（Virtual NFA）**」により、パケットあたりの必要スレッド数を4にアライメントし、1ワープ内で8パケットを同時処理可能にした。これにより、従来のGPU向けNFAエンジン（iNFAnt）から **29〜46倍の高速化** を達成し、10Gbps以上のスループットを一貫して維持できることを示した。

### 3. [Parallelization and Characterization of Pattern Matching using GPUs](./article_summaries/Parallelization%20and%20Characterization%20of%20Pattern%20Matching%20using%20GPUs/summary.md)
* **著者**: Giorgos Vasiliadis, Michalis Polychronakis, Sotiris Ioannidis (FORTH-ICS, Greece / Columbia University, USA)
* **発表会議**: IEEE IISWC '11
* **概要**: 
  NVIDIA CUDAアーキテクチャを活用し、GPU上の異なるメモリ階層が決定性有限オートマトン（DFA）ベースのパターンマッチングに与える影響を体系的に評価し、メモリ帯域・PCIeデータ転送の最適化手法を提案した研究。
  1スレッドあたり 16バイト（`int4`）を一括フェッチする「ワードアクセス幅の最適化」により、メモリトランザクション数を激減させスループットを劇的に向上。さらに、パケットを隙間なく配置し、オフセットをインデックス配列で制御して一括DMA転送する「**インデックス型パケットバッファ**」を提案。これにより、小さなパケット（100バイトなど）転送時のPCIeバスの有効帯域低下を防ぎ、極小パケットにおいても **6.49 Gbit/s** （従来の約5倍）、フルペイロードで **27.1 Gbit/s** の実効スループットを維持した。また、メモリ特性として、DFAテーブルはグローバルメモリ（または1Dテクスチャ）、パケットデータは2Dテクスチャに配置するのが最善であることを実証した。

### 4. [Regular Expression Matching on Graphics Hardware for Intrusion Detection](./article_summaries/Regular%20Expression%20Matching%20on%20Graphics%20Hardware%20for%20Intrusion%20Detection/summary.md)
* **著者**: Giorgos Vasiliadis, Michalis Polychronakis, Spiros Antonatos, Evangelos P. Markatos, Sotiris Ioannidis (FORTH-ICS, Greece / Columbia University, USA)
* **発表会議**: Recent Advances in Intrusion Detection (RAID '09)
* **概要**: 
  NIDSにおけるPCRE正規表現マッチングをGPUにオフロードする並列マッチングエンジンを提案し、人気NIDS「Snort」へ統合したシステム評価を行った研究。
  DFAの状態爆発への対処として、状態数が5,000状態以下に収まる正規表現（全ルールの **97%以上**）はGPU上のDFAで超高速に並列処理し、残りの状態爆発を起こす少数はCPU（PCRE/NFA）で処理する **ハイブリッド検出方式** を提案。パケットをピン留めメモリを介した非同期DMAおよびダブルバッファリングで転送し、MTUサイズを超える再構築パケットは境界スキャンを担保してスライス分割する。DFAテーブルを1Dテクスチャにバインドしてキャッシュを有効化し、CPU（シングルコア）比で **最大 48.2 倍の高速化**（スループット **16 Gbit/s**）を達成。Snort統合時でも **約8倍のスループット向上（最大 800 Mbps以上）** を実証した。

### 5. [Regular Expressions on Modern GPGPUs](./article_summaries/Regular%20Expressions%20on%20Modern%20GPGPUs/summary.md)
* **著者**: Cheng Li, Clark Verbrugge (McGill University, Canada)
* **発表会議**: ACM Workshop on General Purpose Processing Using GPU (GPGPU ’24)
* **概要**: 
  最新のGPGPUアーキテクチャ（Compute Capability 8.6）を対象に、スレッド占有率（Occupancy）の低下を防ぐ実行リソース（レジスタ数、ブロックサイズ、共有メモリ）の最適チューニングをプロファイリングに基づき実施し、文字列プレフィルタリングおよび先頭ワイルドカード対策を導入して、ロバストな超高速正規表現マッチングを実現した研究。
  REから抽出した最長部分固定文字列の並列KMP照合（プレフィルタ）を行い、不要なRE判定 of 大部分をスキップ。さらに、先頭ワイルドカードによる全スレッドの不要なトラップループ（最悪計算量 $O(mn^{2})$ ）を回避するため、入次数に基づいてスキップ状態を取り除いた「縮小NFA（Reduced NFA）」で一次検索する「**ASyncAP_Optimized**」を提案。先頭ワイルドカードを含む最悪パターンの評価において、先行研究の `ASyncAP` から **約 1,900 倍**、CPUから **約 190 倍** の圧倒的スピードアップを達成し、KMPプレフィルタ適用とパラメータ調整により `iNFAnt` 比でも **約 40 倍** の高速化を達成した。
