# 次に読むべき論文 (Next to Read)

本論文(*GPU Acceleration of Regular Expression Matching for Large Datasets: Exploring the Implementation Space*, CF '13)の成果や、関連するGPUベースの正規表現エンジンを更に深掘りするための後続・関連研究を以下に列挙します。

## 1. DFAGE関連の研究 (本論文の影響を受けた後続アプローチ)
- **関連性:** 本論文が示した実装空間の課題（状態管理やGPUメモリ最適化）を踏まえ、実際にDFA（Deterministic Finite Automata）をGPU上で駆動させるためのフレームワークとして「DFAGE (A Deterministic Finite Automata GPU-based Engine)」等の開発が行われました。これらの論文は本研究を直接的に引用・拡張しています。

## 2. Offset-FA やハイブリッド・パターンマッチングアルゴリズム
- **関連性:** NFA/DFA変換時の状態爆発を回避するためや、GPUのメモリボトルネックを軽減するための進化系として、Offset-FAなどの派生アルゴリズムが提案されています。これらは、純粋なGPUマッチングが抱える限界点に対する後続のアプローチとして必読です。

## 3. Evaluating GPUs for network packet signature matching (R. Smith et al., ISPASS 2009)
- **関連性:** 時代的に本論文と並行、あるいは少し先行してGPUを用いたNIDS用シグネチャマッチングの限界と可能性を検証したベースラインとなる研究です。GPUとCPU間のデータ転送コストやメモリアクセスの特性に関して、共通の課題意識を持っています。

## 4. GPU-based NFA implementation for memory efficient high speed regular expression matching
- **関連性:** DFAによる状態爆発を避けるため、敢えてNFAのままGPUにマッピングし、並列性によって処理を行う代表的なアプローチです。DFAを中心とした本論文の「実装空間探索」とは異なるもう一つの有力な発展系として比較対象になります。
