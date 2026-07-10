# Synchromesh: Reliable Code Generation from Pre-Trained Language Models

本論文は、正規表現・CFGベースの「Completion Engine（補完エンジン）」によりLLMの出力を各ステップで有効なトークンに制限する制約付きデコードフレームワーク「Synchromesh」を提案した研究である。

---

## 背景

事前学習済み言語モデル（GPT-3等）によるプログラム合成（コード生成）には以下の課題があった：

1. **Few-shot学習の限界**: ドメイン固有言語（DSL）では例示が少なく、モデルがDSLの構文を正確に習得できない。
2. **分布外の構文**: 事前学習データに含まれないDSL固有の構文はモデルが生成できない。
3. **ツールとの統合**: 生成されたコードがAPIやDSLの仕様に準拠していることが要求されるが、素の言語モデルはこれを保証できない。

Text-to-SQL（Spider）の成功事例に触発されて、より汎用的なプログラム合成への制約付きデコードの応用が求められていた。

---

## 手法

### 1. Completion Engine（補完エンジン）

Synchromeshの核心はタスク固有の「Completion Engine」の設計にある。

Completion Engine は関数 $CE: \text{Prefix} \rightarrow 2^V$ として定義される：
- 入力: 現在生成中のコードのプレフィックス（部分文字列）
- 出力: プレフィックスから有効に続けられるトークンの集合

$$V_{\text{valid}}^{(t)} = CE(y_{1:t})$$

有効なトークンのみが次ステップの候補となる：
$$P_{\text{constrained}}(y_{t+1} | y_{1:t}) \propto P_{\text{LLM}}(y_{t+1} | y_{1:t}) \cdot \mathbf{1}[y_{t+1} \in V_{\text{valid}}^{(t)}]$$

### 2. 正規表現ベースのCompletion Engine

簡単なDSLでは、構文を正規表現で記述することでCompletion Engineを構築できる。

例：日付フォーマット `YYYY-MM-DD` の場合：
```
状態0: 任意の4桁数字 → [0-9]{4}
状態1: ハイフン → -
状態2: 任意の2桁数字 → [0-9]{2}
...
```

各状態から有効なトークンをFSMで事前計算し、インデックスとして格納する（Outlinesと同様のアプローチ）。

### 3. CFGベースのCompletion Engine

より複雑なDSLにはCFGベースのCompletion Engineを使用する。

Earleyパーサをインクリメンタルに実行し、各中間状態のアイテムセットから有効な次トークンを導出する（PICARDと同様のアプローチ）。

### 4. SMC（Sequential Monte Carlo）との統合

単純なビームサーチではなく、重要度サンプリングを用いたSMCを採用する：

$$w_t = \frac{P_{\text{target}}(y_{1:t})}{P_{\text{proposal}}(y_{1:t})} = \prod_{k=1}^{t} \frac{P_{\text{LLM}}(y_k | y_{1:k-1}) \cdot \mathbf{1}[y_k \in V_{\text{valid}}^{(k-1)}]}{P_{\text{constrained}}(y_k | y_{1:k-1})}$$

SMCにより制約付きデコードの確率歪み（Grammar-Aligned Decoding問題）を軽減する。

---

## 結果

### プログラム合成タスクでの精度（主要結果）

#### REGEX（正規表現合成）タスク

| モデル | 制約なし | Synchromesh |
| :--- | :---: | :---: |
| GPT-3（1-shot） | 12.4% | **32.1%** |
| GPT-3（5-shot） | 18.7% | **41.6%** |
| Codex（1-shot） | 24.3% | **48.9%** |

#### SMILES（化学式合成）タスク

| モデル | 制約なし | Synchromesh |
| :--- | :---: | :---: |
| GPT-3（1-shot） | 3.2% | **21.7%** |
| GPT-3（5-shot） | 7.8% | **34.5%** |

#### DSL（独自ドメイン言語）タスク

| モデル | 制約なし | Synchromesh |
| :--- | :---: | :---: |
| GPT-3（1-shot） | 8.9% | **56.2%** |

制約なし生成からSynchromesh適用で平均 **3〜6倍** の精度向上を達成した。

---

## chokosenlovetiのメモ

### GPU正規表現高速化との関係

SynchromeshはRegex合成タスクを評価対象の一つとして含んでおり、GPU正規表現マッチングとの接点が特に直接的である。

- **正規表現合成の応用**: Synchromeshが示すように、LLMが正規表現を生成する際に正規表現の文法（正規表現のシンタックスを定義するCFG）で制約すると精度が大幅に向上する。これはGPUを用いた高スループット正規表現マッチングシステムの「パターン管理」に応用できる（LLMが生成した正規表現の有効性を即座に検証）。
- **Completion Engineの並列化**: DSLのCFG状態遷移を複数候補並列にGPUで評価する「並列Completion Engine」は、GPU正規表現マッチングの技術基盤（Virtual NFA・iNFAnt等）で実装できる可能性がある。
- **SMILES化学式との対応**: SMILESの文法はほぼ正規言語として記述可能であり、GPU上での並列SMILESパターンマッチングと結合したSynchromesh拡張が考えられる。
