# Next to Read

今回の論文「Search-Based Regular Expression Inference on a GPU」(2023) の直接的な被引用論文（Cited by）は、Semantic Scholar APIによる取得では確認できませんでした（発表時期や分野のニッチさによる未反映の可能性、または現行の検索プラットフォーム上に直接の後続研究が登録されていない可能性があります）。

**論文中のReferenceを被引用論文と誤認させることはプロジェクトの規則（Haluci-Nation防止等）上禁止されているため、引用履歴の偽装は行いません。**

代替として、同じく「正規表現合成・プログラム合成」や「並列化・探索アルゴリズムの高速化」に着目した近年の関連研究（Concurrent Work・分野の近似研究）をいくつか推奨します。

1. **AlphaRegex: A Regular Expression Synthesizer** (Lee et al.)
   - 本論文のベースライン・比較対象となっていたSOTAソリューションです。GPUアプローチに相対する、CPUとヒューリスティックによる探索最適化を詳細に知る上で有用です。
2. **Program Synthesis for Regular Expressions based on Examples (General REI surveys)**
   - 正規表現推論システム自体のアルゴリズムについて、これまでの歴史的系譜を学ぶためのサベイペーパーなどが関連してきます。
3. **GPU-Accelerated Program Synthesis and Search** 
   - 最近では正規表現だけでなく、一般的なプログラム合成における枝刈りやSAT/SMTソルバをGPUで高速化する研究が進んでいます。PaRESyで使われた「Bitvector Matrix」による並列探索の知見は、他のプログラム合成のトピックと共有できる可能性があります。
