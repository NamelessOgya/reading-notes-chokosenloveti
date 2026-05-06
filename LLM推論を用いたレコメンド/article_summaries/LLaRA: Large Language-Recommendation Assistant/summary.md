# summary

## 背景
従来の系列レコメンド（Sequential Recommendation）は、ユーザーの過去の行動履歴から行動パターンを捉える能力に優れているが、アイテムの外部知識（メタデータなど）や推論能力に欠けていた。一方で、大規模言語モデル（LLMs）は広範な世界知識と強力な推論能力を持つが、そのままではユーザーの行動パターンを的確に捉えるのが難しい。従来の研究では、LLMのプロンプトにアイテムのIDインデックスやテキストメタデータを含めるアプローチが取られていたが、これらは世界知識と行動的理解を同時に満たすことができていなかった。そこで、従来のレコメンドモデルが持つ「行動パターンの理解」と、LLMが持つ「世界知識」の相補的な強みを統合するため、**LLaRA (Large Language-Recommendation Assistant)** が提案された。

## 手法
LLaRAは、従来の推薦モデル（例: GRU4Rec, Caser, SASRecなど）が学習したIDベースのアイテム埋め込みと、LLMが持つテキスト特徴量を統合する「ハイブリッドプロンプティング（Hybrid Prompting）」手法を用いる。
具体的には以下のステップからなる。

1. **アイテムの表現 (Item Representation)**
   - **テキストトークン列:** アイテム$i$のタイトル等のテキスト情報をLLMのトークナイザと埋め込み層で処理し、複数のトークンベクトルの連続（シーケンス）である $\text{<}\mathbf{emb_t^i}\text{>}$ を取得する（※1つのベクトルに圧縮・平均化などはせず、テキストのシーケンスのまま扱う）。

$$ \text{<}\mathbf{emb_t^i}\textbf{>}=\textbf{LLM-TKZ}(txt_i) $$

   - **行動トークン:** 従来のレコメンドモデルで学習されたIDベースの表現 $\mathbf{e_s^i}$ を、SR2LLMというプロジェクター（MLP等）を用いてLLMの入力次元にマッピングし、1つの特殊な単語のような行動トークン $\text{<}\mathbf{emb_s^i}\text{>}$ を得る。

$$ \text{<}\mathbf{emb_s^i}\text{>}=\mathbf{Proj}(\mathbf{e_s^i};\Theta_{p}) $$

   - **ハイブリッド表現:** テキストのトークン列の直後に、行動トークンを「新しい1つの特殊単語」としてそのまま後ろに連結（Append）し、ハイブリッド表現 $\text{<}\mathbf{emb_c^i}\text{>}$ を作成する。

$$ \text{<}\mathbf{emb_c^i}\text{>}=\textbf{Concat}(\text{<}\mathbf{emb_t^i}\text{>},\text{<}\mathbf{emb_s^i}\text{>}) $$

2. **ハイブリッドプロンプト設計 (Hybrid Prompt Design)**
   プロンプト内のテキストにプレースホルダー `<PH>` を設け、そこに行動トークン `<emb_s^i>` を結合させて入力に用いる。これにより、LLMはテキストメタデータと従来モデルの埋め込みの両方を同時に処理できるようになる（![prompt_example](./images/prompt_example.png)）。

3. **カリキュラムプロンプトチューニング (Curriculum Prompt Tuning)**
   最初からハイブリッドな情報をLLMに与えると学習が不安定になる。そこで、最初はLLMに馴染みのある「テキストのみのプロンプト（Easy task）」でウォームアップさせ、徐々に「ハイブリッドプロンプト（Hard task）」へ移行するカリキュラム学習を採用している（![LLaRA-framework](./images/LLaRA-framework.png)）。

それぞれの損失関数は以下の通りである。
$$ L_{easy}(x^e, y^e) = - \sum_{t=1}^{|y^e|}\log\left(P_{\Phi_0+\Delta\Phi(\Theta)}(y^e_t|x^e, y^e_{<t})\right) $$
$$ L_{hard}(x^h,y^h) = - \sum_{t=1}^{|y^h|}\log\left(P_{\Phi_0+\Delta\Phi(\Theta)+\Theta_p+\Theta_{e}}(y^h_t|x^h,y^h_{<t})\right) $$

学習時は、確率 $p(\tau)=\frac{\tau}{T}$ に基づき、EasyからHardなタスクへと学習割合を遷移させる。

## 結果
LLaRAの有効性を検証するため、MovieLens, Steam, LastFMのデータセットを用いて、従来の系列レコメンドや既存のLLMベースの手法と比較を行った。

### データセットの統計情報
Table 1に実験に用いたデータセットの詳細を示す。
| Dataset | MovieLens | Steam | LastFM |
| :--- | ---: | ---: | ---: |
| \# Sequence | 943 | 11,938 | 1,220 |
| \# Item | 1,682 | 3,581 | 4,606 |
| \# Interaction | 100,000 | 274,726 | 73,510 |

### 比較結果
Table 2に示すように、LLaRAは従来のモデル（GRU4Rec, Caser, SASRec）をバックボーンに組み込んだいずれのパターンにおいても、LLMベースの既存モデル（TALLRec等）や従来モデル単体を大きく上回り、最高性能（HitRatio@1など）を記録した。
特に LLaRA (SASRec) が安定して高い成果を出していることがわかる。

| Category | Model | MovieLens (Valid) | MovieLens (HR@1) | Steam (Valid) | Steam (HR@1) | LastFM (Valid) | LastFM (HR@1) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Traditional | GRU4Rec | 1.0000 | 0.3750 | 1.0000 | 0.4168 | 1.0000 | 0.2616 |
| Traditional | Caser | 1.0000 | 0.3861 | 1.0000 | 0.4368 | 1.0000 | 0.2233 |
| Traditional | SASRec | 1.0000 | 0.3444 | 1.0000 | 0.4010 | 1.0000 | 0.2233 |
| LLM-based | Llama2 | 0.4421 | 0.0421 | 0.1653 | 0.0135 | 0.3443 | 0.0246 |
| LLM-based | GPT-4 | 0.9895 | 0.2000 | 0.9798 | 0.3626 | 1.0000 | 0.3770 |
| LLM-based | MoRec | 1.0000 | 0.2822 | 1.0000 | 0.3911 | 1.0000 | 0.1652 |
| LLM-based | TALLRec | 0.9263 | 0.3895 | 0.9840 | 0.4637 | 0.9836 | 0.4180 |
| Ours | LLaRA (GRU4Rec) | 0.9684 | 0.4421 | 0.9975 | 0.4924 | 0.9836 | 0.4344 |
| Ours | LLaRA (Caser) | 0.9684 | **0.4737** | 0.9966 | 0.4874 | 0.9918 | 0.4344 |
| Ours | LLaRA (SASRec) | 0.9684 | 0.4421 | 0.9975 | **0.4949** | 1.0000 | **0.4508** |

### カリキュラム学習の有効性
Table 3では、カリキュラム学習（CL）の有無やTwo-stage（事前学習→ファインチューニング）との比較が行われている。テキストとハイブリッドを順次段階的に学習するLLaRA (CL) が全データセットで最も高い性能を発揮しており、モダリティ間のギャップを適切に埋めていることが確認された。

| Method | MovieLens | Steam | LastFM |
| :--- | :--- | :--- | :--- |
| Direct | 0.4211 | 0.4899 | **0.4508** |
| Two-stage | 0.4316 | 0.4840 | 0.4344 |
| LLaRA (CL) | **0.4421** | **0.4949** | **0.4508** |

総じて、行動パターンの埋め込みと世界知識をカリキュラム学習によって自然に統合したLLaRAは、従来の枠組みにおける弱点を克服し、次世代の推薦システムとして有望なアプローチであることが示された。
