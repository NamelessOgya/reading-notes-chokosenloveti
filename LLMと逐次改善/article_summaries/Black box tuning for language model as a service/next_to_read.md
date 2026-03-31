# 次に読むべき関連論文 (Next to Read)

本論文（Black-Box Tuning for Language-Model-as-a-Service）は、LMaaS環境におけるAPI経由での勾配不要（Zeroth-Order/Black-Box）なプロンプト最適化の先駆けであり、その後も多くの関連研究が提案されています。以下は本手法を発展させたり、別の角度からアプローチしている後続の被引用論文（Cited by）のリストです。

- **Projection-Free Evolution Strategies for Continuous Prompt Search** (2026)
  - Authors: Yuzhu Cai, Can Huang, Xiaoyu He
  - URL: https://www.semanticscholar.org/paper/80349618081168b371d908ae370ab8c8cb87c79f
  - 理由: 本論文で要であった「元の高次元空間を低次元の部分空間へランダムランダムに投影（Projection）する」手法を介さない進化戦略を提案し、連続値プロンプト探索の更なる効率化を図った発展研究。

- **Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization** (2026)
  - Authors: Yicheng Lang, Changsheng Wang, Yihua Zhang et al.
  - URL: https://www.semanticscholar.org/paper/36e539d16177b7c40d8c5fb7a4277f946b158cbe
  - 理由: 本論文の課題でもあった「DFO(Zeroth-Order)学習の収束率の限界」に対し、部分空間の勾配直交化を用いることで微調整アルゴリズムの学習効率を劇的に向上させるアプローチ。

- **AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning** (2026)
  - Authors: Wei Lin, Yining Jiang, Qingyu Song et al.
  - URL: https://www.semanticscholar.org/paper/fb1bda11c25bb74b78672f41c507d6006731cc6c
  - 理由: アクティベーション（モデル内部の活性化状態）のガイドをゼロ次最適化に組み合わせることで、完全なブラックボックスではなく限られた情報を有効利活用してチューニング性能を引き上げる別角度のアプローチ。

- **Advanced Black-Box Tuning of Large Language Models with Limited API Calls** (2025)
  - Authors: Zhikang Xie, Weilin Wan, Peizhu Gong et al.
  - URL: https://www.semanticscholar.org/paper/b567119108db92cc54fc368ac49d3a2e61cbfabf
  - 理由: 本論文手法を実運用する上でボトルネックとなる「APIコール数の膨大さ・予算」の課題に直接焦点を当て、限られたAPI呼び出し回数で高精度な最適化を行う手法を提案している実用的後続研究。

- **CBP-Tuning: Efficient Local Customization for Black-box Large Language Models** (2025)
  - Authors: Jiaxuan Zhao, Naibin Gu, Yuchen Feng et al.
  - URL: https://www.semanticscholar.org/paper/889275a8df9e2a63620ab7cc3b3ec04e8b039ed3
  - 理由: Customised Black-box Prompt Tuning (CBP-Tuning) を提唱し、サーバー側でのプロンプト生成とローカル（クライアント）側での勾配フリーチューニングをうまく切り離すことで、ブラックボックスモデルの効率的なローカルカスタマイズを実現したフレームワーク。

本論文で切り開かれた「ブラックボックスチューニング」や「ゼロ次最適化（Zeroth-Order Optimization）」の流れは、部分空間の再定義やAPIコールの削減を主眼として現在（2025〜2026年）でも活発に研究され続けています。
