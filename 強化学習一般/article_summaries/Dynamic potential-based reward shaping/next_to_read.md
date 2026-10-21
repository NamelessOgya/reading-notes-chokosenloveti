# 次に読むべき関係論文 (Dynamic Potential-Based Reward Shaping)

本論文は OpenAlex / Semantic Scholar の検索で正しく照合できなかった（OpenAlex 未索引、Semantic Scholar はレート制限）。そのため、候補論文の arXiv ソース（`.tex`/`.bbl`/`.bib`）に本論文のタイトルが含まれるかを `tools/grep_arxiv_refs.sh` で確認し、**本論文を実際に引用していることを確認できた論文のみ** を列挙した。

## 手法を発展させているもの

### Useful Policy Invariant Shaping from Arbitrary Advice (Behboudian, Satsangi, Taylor, Harutyunyan, Bowling, 2020; arXiv:2011.01297)
- **概要・選定理由:**
  本論文の動的ポテンシャルを用いて任意の報酬（アドバイス）を potential-based に変換する手法（Harutyunyan et al., 2015）には、実は方策不変性が成り立たない場合があることを指摘し、修正した手法（PIES）を提案している。人手で設計した中間報酬（例：「カードを温存したら加点」）を動的ポテンシャル経由で安全に使いたい場合に、**理論上の落とし穴** を把握するために必読である。

### Potential-Based Reward Shaping For Intrinsic Motivation (Forbes et al., AAMAS 2024; arXiv:2402.07411)
- **概要・選定理由:**
  好奇心などの内発的報酬は学習中に変化するため、そのまま加えると最適方策を歪めうる。本論文の動的ポテンシャルの理論を拡張し、任意の内発的報酬を最適方策を保つ形に変換する PBIM を提案している。疎な報酬の下での **探索ボーナス** を安全に使う方法として、カードゲームの序盤の探索改善にも応用できる。

### Bootstrapped Reward Shaping (Adamczyk, Makarenko, Tiomkin, Kulkarni, AAAI 2025; arXiv:2501.00989)
- **概要・選定理由:**
  学習中のエージェント自身の価値関数の推定値をポテンシャルとして使う（ブートストラップする）シェーピング手法で、本論文の動的ポテンシャルの典型的な応用である。カードゲームで **学習中の価値ネットワークを勝率推定のポテンシャルとして使う** 設計に直接対応する。

## 違う角度からアプローチしているもの

### Self-Supervised Online Reward Shaping in Sparse-Reward Environments (Memarian, Goo, Lioutikov, Niekum, Topcu, IROS 2021; arXiv:2103.04529)
- **概要・選定理由:**
  エージェント自身が集めた軌跡を成功・失敗でランク付けし、その順位を説明する密な報酬関数を自己教師ありで推論して学習に使う（SORS）。人手でポテンシャルを設計せずに、**疎な勝敗報酬から密な中間報酬を自動で作る** アプローチとして、カードゲームの勝敗報酬の問題に近い。

### Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping (Hu et al., NeurIPS 2020; arXiv:2011.02669)
- **概要・選定理由:**
  シェーピング報酬の重みを状態ごとに二重最適化で学習し、有益なシェーピングだけを活かす。本論文が「ランダムなポテンシャルは学習を遅くしうる」と示した問題に対し、potential-based という形の制約ではなく **シェーピングの重み付けを学習する** という別の方向から取り組んでいる。
