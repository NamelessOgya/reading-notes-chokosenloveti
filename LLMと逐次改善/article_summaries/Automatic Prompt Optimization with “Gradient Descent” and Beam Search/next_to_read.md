# 次に読むべき関連論文 (Next to Read)

本研究「Automatic Prompt Optimization with "Gradient Descent" and Beam Search (ProTeGi)」を引用・発展させている後続研究から、LLMによるプロンプトの自動最適化や、強化学習・フィードバックループの改良に関連する注目論文をリストアップします。

### 1. Generalizable Self-Evolving Memory for Automatic Prompt Optimization
- **著者:** Guanbao Liang et al.
- **概要:** 従来のプロンプト最適化（APO）が特定のタスクに固有のプロンプトを探索するのに留まり、知識の蓄積ができない問題に対処した研究。成功した推論軌跡を戦略テンプレートとして、誤答モードをエラーパターンとしてデュアルメモリに蓄積する「MemAPO」を提案している。ProTeGiのような枠組みに「汎用的な長期記憶」を持たせてタスク間転移を可能にする発展型アプローチである。

### 2. Reflection in the Dark: Exposing and Escaping the Black Box in Reflective Prompt Optimization 
- **著者:** Shiyan Liu et al.
- **概要:** ProTeGiやGEPAといったテキストフィードバック（Reflective APO）手法が、ラベルの無いブラックボックスな最適化を行うことで、誤った初期プロンプトから回復できず（局所的最適解に陥る）に精度が劣化する現象を指摘した論文。仮説生成とプロンプトの書き換え処理を分離し、探索のトラッキングとエスケープ機能（VISTA）を並行導入することでブラックボックスな最適化の限界を突破している。

### 3. PrefPO: Pairwise Preference Prompt Optimization
- **著者:** Rahul Singhal et al.
- **概要:** APOが往々にして膨大で冗長なプロンプトを生成しがちであるという問題に対し、RLHF（AIフィードバックによる強化学習）の概念をプロンプト最適化に持ち込んだ手法。LLMの出力に対する「ペアワイズ評価（Pairwise Preference）」のフィードバックのみを用いて反復的改善を行うことで、ラベルデータ不要かつハイパーパラメータ調整なしで、短く高精度な最適化を実現している。
