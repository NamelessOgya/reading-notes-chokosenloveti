# Distillation Matters: Empowering Sequential Recommenders to Match the Performance of Large Language Model

## 背景
LLM（大規模言語モデル）の強力な意味推論能力により、それを推薦システム（RS）に直接適用する研究が進み、高い精度を達成している。しかし、LLMベースの推薦モデルはその膨大な計算量と推論遅延（Inference latency）により、実際のオンラインシステムへの展開が極めて困難であるという課題を抱えている（例えば、LLMベースの BIGRec は、従来のシーケンシャル推薦モデルである DROS と比較して推論に数万倍の時間を要する）。
これに対処するため、巨大なLLMベースの推薦モデル（教師）から、軽量で高速な従来のシーケンシャルモデル（生徒）への知識蒸留（Knowledge Distillation）が最も有望なアプローチとなる。しかし既存の蒸留戦略をそのまま適用するには3つの大きな課題が存在した：
1. **教師知識の信頼性の欠如**: LLM特有のハルシネーション（幻覚）等により、教師のランキング・推薦結果が常に信頼できるとは限らない。
2. **モデルキャパシティの不一致**: 教師（LLM）と生徒（従来モデル）の間に大きな表現力の差があり、全ての知識・ランキングをそのまま生徒に学習させるのは実質的に困難である。
3. **意味空間の乖離**: LLMが扱う大局的なテキスト意味空間（Semantic Space）と、従来のモデルが扱うIDベースの協調フィルタリング空間（Collaborative Filtering Space）の間に乖離があり、直接的な埋め込み（Embedding）の蒸留が難しい。

## 手法
これらの課題を解決するため、本論文ではLLMベースの推薦モデルから従来のシーケンシャルモデルへの知識蒸留に特化した新しい蒸留戦略「**DLLM2Rec**」を提案している。

![提案モデル DLLM2Rec の全体像](./images/MODEL8.png)

DLLM2Recは主に以下の2つのコンポーネントで構成される。

1. **Importance-aware Ranking Distillation (重要度を考慮したランキング蒸留)**
   ノイズの多いLLMの知識から、信頼性が高くかつ生徒モデルが吸収しやすい知識をフィルタリングする。各項目に対して以下の要素を組み合わせた重要度重み（$w_{si}$）を計算し学習させる：
   - **Position-aware weights ($w^p_{si}$)**: 教師のランキングにおける上位項目を重視する重み。
   - **Confidence-aware weights ($w^c_{si}$)**: 教師（LLM）が生成した推薦の確信度に基づく重み付け。
   - **Consistency-aware weights ($w^o_{si}$)**: "Wisdom of the crowd"（群衆の叡智）から着想を得て、教師モデルと生徒モデルの推論結果が一致（Consensus）している項目の信頼度を高く評価するアプローチ。

2. **Collaborative Embedding Distillation (協調埋め込み蒸留)**
   LLMから得られる豊富なテキストベースの「意味的埋め込み知識 (Semantic Embedding)」と、CFモデルの「IDベースの埋め込み」の間のギャップ（semantic space divergence）を整合させる。
   単純かつ効果的なMLP層を用いてLLMのテキスト埋め込みをID空間の次元へと写像（Map）し、実行動データから得られた協調信号と統合（Aggregation）した上で、よりリッチな表現として生徒モデルを訓練する。

## 結果
DLLM2Recの性能を、3つの代表的なシーケンシャルモデル（GRU4Rec、SASRec、DROS）と組み合わせて評価した。

![ハイパーパラメータの感度分析](./images/sensitivity3.png)

**Table 1: 推薦性能と推論時間の比較 (BIGRec vs DROS)**
| Dataset | Model | HR@20 | NDCG@20 | Inference time |
|---|---|---|---|---|
| Games | DROS | 0.0473 | 0.0267 | 1.8s |
| Games | BIGRec | 0.0532 | 0.0341 | 2.3x10^4s |
| Games | _Gain_ | +12.47% | +27.72% | -1.3x10^6% |
| Toys | DROS | 0.0231 | 0.0144 | 1.6s |
| Toys | BIGRec | 0.0420 | 0.0207 | 1.1x10^4s |
| Toys | _Gain_ | +81.82% | +43.75% | -6.8x10^5% |

**Table 2: NDCG@20におけるBIGRecとDROSの勝敗比率**
| Dataset | Condition | Relative Ratio |
|---|---|---|
| Games | BIGRec > DROS | 53.90% |
| Games | BIGRec < DROS | 46.10% |
| MovieLens | BIGRec > DROS | 40.90% |
| MovieLens | BIGRec < DROS | 59.10% |
| Toys | BIGRec > DROS | 66.67% |
| Toys | BIGRec < DROS | 33.33% |

**Table 3: Top-20の推薦アイテムの重複（Overlapped）比率とヒットアイテムの比率**
| Dataset | Rec. Space | Items Ratio | Hit Items |
|---|---|---|---|
| Games | BIGRec only | 96.01% | 0.21% |
| Games | DROS only | 96.01% | 0.18% |
| Games | Overlapped | 3.99% | 1.61% |
| MovieLens | BIGRec only | 95.94% | 0.19% |
| MovieLens | DROS only | 95.94% | 0.35% |
| MovieLens | Overlapped | 4.06% | 2.16% |
| Toys | BIGRec only | 98.95% | 0.17% |
| Toys | DROS only | 98.95% | 0.08% |
| Toys | Overlapped | 1.05% | 3.74% |

**Table 4: ユーザー単位での詳細性能比較**
| Dataset | Condition | Users | Ratio | Relative Ratio |
|---|---|---|---|---|
| Games | BIGRec > DROS | 651 | 4.35% | 49.54% |
| Games | BIGRec = DROS | 106 | 0.71% | 8.09% |
| Games | BIGRec < DROS | 558 | 3.72% | 42.37% |
| MovieLens | BIGRec > DROS | 483 | 4.83% | 39.66% |
| MovieLens | BIGRec = DROS | 37 | 0.37% | 3.04% |
| MovieLens | BIGRec < DROS | 698 | 6.98% | 57.31% |
| Toys | BIGRec > DROS | 176 | 3.64% | 63.53% |
| Toys | BIGRec = DROS | 13 | 0.27% | 4.71% |
| Toys | BIGRec < DROS | 88 | 1.82% | 31.76% |

**Table 5: BIGRecにおけるイリュージョン（幻覚）問題の調査**
| Dataset | -20% | -30% | -50% |
|---|---|---|---|
| Games | 12.02% | 18.76% | 33.34% |
| MovieLens | 15.95% | 25.26% | 38.79% |
| Toys | 13.41% | 19.74% | 35.03% |

**Table 6: 推奨空間の一貫性（Consistency）の影響調査**
| Dataset | Rec. Space | Items | Pos. Items | Pos. Ratio |
|---|---|---|---|---|
| Games | BIGRec only | 287660 | 605 | 0.21% |
| Games | DROS only | 287660 | 517 | 0.18% |
| Games | Consistency | 11940 | 193 | 1.61% |
| MovieLens | BIGRec only | 191881 | 366 | 0.19% |
| MovieLens | DROS only | 191881 | 677 | 0.35% |
| MovieLens | Consistency | 8119 | 175 | 2.16% |
| Toys | BIGRec only | 95645 | 165 | 0.17% |
| Toys | DROS only | 95645 | 74 | 0.08% |
| Toys | Consistency | 1015 | 38 | 3.74% |

**Table 7: データセットの統計情報**
| Datasets | Games | MovieLens | Toys |
|---|---|---|---|
| #Users | 55,223 | 69,878 | 19,412 |
| #Items | 17,408 | 10,681 | 11,924 |
| #Interactions | 497,577 | 1,320,000 | 167,597 |
| Density | 0.05176% | 0.1769% | 0.07241% |

**Table 8: DLLM2Recと既存KD（知識蒸留）手法およびLLM強化戦略との性能比較**
| Backbone | Model | Games HR@20 | Games NDCG@20 | MovieLens HR@20 | MovieLens NDCG@20 | Toys HR@20 | Toys NDCG@20 |
|---|---|---|---|---|---|---|---|
| Teacher | BIGRec | 0.0532 | 0.0341 | 0.0541 | 0.0370 | 0.0420 | 0.0207 |
| GRU4Rec | +None | 0.0305 | 0.0150 | 0.0608 | 0.0236 | 0.0172 | 0.0081 |
| GRU4Rec | +Hint | 0.0284 | 0.0120 | 0.0646 | 0.0240 | 0.0128 | 0.0058 |
| GRU4Rec | +HTD | 0.0299 | 0.0128 | 0.0578 | 0.0229 | 0.0155 | 0.0062 |
| GRU4Rec | +RD | 0.0398 | 0.0177 | 0.0667 | 0.0254 | 0.0157 | 0.0076 |
| GRU4Rec | +CD | 0.0306 | 0.0149 | 0.0699 | 0.0256 | 0.0126 | 0.0052 |
| GRU4Rec | +RRD | 0.0359 | 0.0163 | 0.0657 | 0.0243 | 0.0215 | 0.0097 |
| GRU4Rec | +DCD | 0.0427 | 0.0190 | 0.0666 | 0.0263 | 0.0262 | 0.0114 |
| GRU4Rec | +UnKD | 0.0370 | 0.0170 | 0.0607 | 0.0226 | 0.0235 | 0.0114 |
| GRU4Rec | KAR | 0.0307 | 0.0149 | 0.0603 | 0.0229 | 0.0184 | 0.0079 |
| GRU4Rec | LLM-CF | 0.0393 | 0.0174 | 0.0677 | 0.0246 | 0.0132 | 0.0058 |
| GRU4Rec | +DLLM2Rec | **0.0446** | **0.0205** | **0.0815** | **0.0308** | **0.0281** | **0.0118** |
| GRU4Rec | *Gain.S* | +46.17% | +36.94% | +34.05% | +30.43% | +63.88% | +42.18% |
| GRU4Rec | *Gain.B* | +4.56% | +7.64% | +16.60% | +16.80% | +7.40% | +1.27% |
| SASRec | +None | 0.0346 | 0.0190 | 0.0626 | 0.0228 | 0.0207 | 0.0130 |
| SASRec | +Hint | 0.0358 | 0.0151 | 0.0576 | 0.0216 | 0.0242 | 0.0103 |
| SASRec | +HTD | 0.0343 | 0.0152 | 0.0569 | 0.0214 | 0.0209 | 0.0097 |
| SASRec | +RD | 0.0513 | 0.0225 | 0.0778 | 0.0310 | 0.0397 | 0.0164 |
| SASRec | +CD | 0.0396 | 0.0231 | 0.0712 | 0.0265 | 0.0232 | 0.0151 |
| SASRec | +RRD | 0.0479 | 0.0202 | 0.0633 | 0.0244 | 0.0325 | 0.0158 |
| SASRec | +DCD | 0.0455 | 0.0211 | 0.0723 | 0.0275 | 0.0375 | 0.0175 |
| SASRec | +UnKD | 0.0447 | 0.0219 | 0.0667 | 0.0247 | 0.0335 | 0.0174 |
| SASRec | KAR | 0.0381 | 0.0198 | 0.0565 | 0.0221 | 0.0215 | 0.0131 |
| SASRec | LLM-CF | 0.0559 | 0.0251 | 0.0837 | 0.0295 | 0.0335 | 0.0152 |
| SASRec | +DLLM2Rec | **0.0600** | **0.0262** | **0.0840** | **0.0323** | **0.0409** | **0.0177** |
| SASRec | *Gain.S* | +73.55% | +38.25% | +34.19% | +41.91% | +97.68% | +36.38% |
| SASRec | *Gain.B* | +7.36% | +4.40% | +0.36% | +4.34% | +3.02% | +1.19% |
| DROS | +None | 0.0473 | 0.0267 | 0.0852 | 0.0363 | 0.0231 | 0.0144 |
| DROS | +Hint | 0.0531 | 0.0240 | 0.0791 | 0.0306 | 0.0302 | 0.0135 |
| DROS | +HTD | 0.0489 | 0.0238 | 0.0722 | 0.0289 | 0.0275 | 0.0137 |
| DROS | +RD | 0.0585 | 0.0310 | 0.0950 | 0.0383 | 0.0424 | 0.0220 |
| DROS | +CD | 0.0474 | 0.0270 | 0.0802 | 0.0336 | 0.0238 | 0.0156 |
| DROS | +RRD | 0.0590 | 0.0293 | 0.0788 | 0.0338 | 0.0424 | 0.0212 |
| DROS | +DCD | 0.0531 | 0.0273 | 0.0821 | 0.0348 | 0.0432 | 0.0211 |
| DROS | +UnKD | 0.0448 | 0.0209 | 0.0728 | 0.0297 | 0.0375 | 0.0195 |
| DROS | KAR | 0.0586 | 0.0318 | 0.0859 | 0.0352 | 0.0255 | 0.0156 |
| DROS | LLM-CF | 0.0635 | 0.0293 | 0.0963 | 0.0351 | 0.0385 | 0.0178 |
| DROS | +DLLM2Rec | **0.0751** | **0.0331** | **0.1063** | **0.0437** | **0.0463** | **0.0225** |
| DROS | *Gain.S* | +58.77% | +23.90% | +24.77% | +20.41% | +100.43% | +56.35% |
| DROS | *Gain.B* | +18.27% | +4.03% | +10.38% | +14.24% | +7.07% | +2.16% |

**Table 9: 効率と性能のトレードオフ検証 (BIGRec vs DLLM2Rec)**
| Dataset | Model | HR@20 | NDCG@20 | Inference time |
|---|---|---|---|---|
| Games | BIGRec | 0.0532 | 0.0341 | 2.3x10^4s |
| Games | DLLM2Rec | 0.0751 | 0.0331 | 1.8s |
| Games | _Gain_ | +37.41% | -2.99% | +1.3x10^6% |
| MovieLens | BIGRec | 0.0541 | 0.0370 | 1.8x10^4s |
| MovieLens | DLLM2Rec | 0.1063 | 0.0437 | 1.7s |
| MovieLens | _Gain_ | +96.49% | +18.18% | +1.1x10^6% |
| Toys | BIGRec | 0.0420 | 0.0207 | 1.1x10^4s |
| Toys | DLLM2Rec | 0.0463 | 0.0225 | 1.6s |
| Toys | _Gain_ | +10.24% | +8.70% | +6.8x10^5% |

**Table 10: 蒸留前後のTop-20アイテム重複比率**
| Datasets | Before-distillation | Post-distillation |
|---|---|---|
| Games | 3.99% | 10.88% |
| MovieLens | 4.06% | 10.15% |
| Toys | 1.05% | 14.56% |

**Table 11: ランキング蒸留におけるアブレーションスタディ**
| Dataset | Model | HR@20 | NDCG@20 |
|---|---|---|---|
| Games | w/o $all_r$ | 0.0661 | 0.0301 |
| Games | w/o $w^p_{\mathbf si}$ | 0.0697 | 0.0301 |
| Games | w/o $w^c_{\mathbf si}$ | 0.0733 | 0.0300 |
| Games | w/o $w^o_{\mathbf si}$ | 0.0568 | 0.0311 |
| Games | DLLM2Rec | **0.0751** | **0.0331** |
| MovieLens | w/o $all_r$ | 0.0917 | 0.0364 |
| MovieLens | w/o $w^p_{\mathbf si}$ | 0.1037 | 0.0429 |
| MovieLens | w/o $w^c_{\mathbf si}$ | 0.0986 | 0.0398 |
| MovieLens | w/o $w^o_{\mathbf si}$ | 0.1047 | 0.0430 |
| MovieLens | DLLM2Rec | **0.1063** | **0.0437** |
| Toys | w/o $all_r$ | 0.0386 | 0.0177 |
| Toys | w/o $w^p_{\mathbf si}$ | 0.0406 | 0.0200 |
| Toys | w/o $w^c_{\mathbf si}$ | 0.0430 | 0.0205 |
| Toys | w/o $w^o_{\mathbf si}$ | 0.0445 | 0.0208 |
| Toys | DLLM2Rec | **0.0463** | **0.0225** |

**Table 12: 協調埋め込み（Embedding）蒸留におけるアブレーションスタディ**
| Dataset | Model | HR@20 | NDCG@20 |
|---|---|---|---|
| Games | w/o $all_e$ | 0.0649 | 0.0323 |
| Games | w/o *offset* | 0.0700 | 0.0298 |
| Games | Hint | 0.0563 | 0.0244 |
| Games | HTD | 0.0568 | 0.0246 |
| Games | DLLM2Rec | **0.0751** | **0.0331** |
| MovieLens | w/o $all_e$ | 0.0999 | 0.0420 |
| MovieLens | w/o *offset* | 0.1061 | 0.0425 |
| MovieLens | Hint | 0.0861 | 0.0344 |
| MovieLens | HTD | 0.0874 | 0.0341 |
| MovieLens | DLLM2Rec | **0.1063** | **0.0437** |
| Toys | w/o $all_e$ | 0.0379 | 0.0194 |
| Toys | w/o *offset* | 0.0405 | 0.0195 |
| Toys | Hint | 0.0358 | 0.0159 |
| Toys | HTD | 0.0349 | 0.0157 |
| Toys | DLLM2Rec | **0.0463** | **0.0225** |

**結果についての考察**
- **推論効率と精度の比較 (Table 1, Table 9):** BIGRec (LLMベースの教師) は圧倒的なパラメータ数によりDROS等の従来モデルに勝る精度を持つものの、推論時間が約 $2.3 \times 10^4$ 秒かかり実用的ではありませんでした。しかし、DLLM2Recを用いた蒸留されたDROS（生徒）は、わずか1.8秒という高速な推論速度を維持したまま、元となるBIGRecを上回るまたは匹敵する驚異的な精度（例えばMovieLensでのHR@20: 0.1063）を達成しました。これにより、LLMの推論遅延の課題を効果的に解決しつつ、それ以上の性能を小規模モデルに伝搬できることが実証されました。
- **一貫性の力 (Table 3, Table 6):** 興味深いことに、教師のみまたは生徒のみが推薦する項目よりも、「教師と生徒の予測領域が重なる（Consistency）」項目の方が、遥かに高い正答率（Hit Ratio）を持つことが明らかになりました。これが本手法のConsistency-aware weightsの理論的基盤を強力に裏付けています。
- **既存の手法との比較 (Table 8):** 本手法(DLLM2Rec)は、Hint, CD, RDといった既存の典型的な知識蒸留手法やLLMエンハンス手法を一貫して上回りました。3つのデータセットと3つの全てのバックボーン（GRU4Rec, SASRec, DROS）において、いずれも最良の精度を達成し（ベースラインの生徒モデルから平均47.97%の向上）、DLLM2Recの堅牢性と汎用性が確認されました。
- **アブレーションスタディ (Table 11, Table 12):** 
  - ランキング蒸留において、位置($w^p_{\mathbf si}$)、確信度($w^c_{\mathbf si}$)、一貫性($w^o_{\mathbf si}$)の各重みを取り除いた場合、すべてで共通して性能が低下しました。とりわけ一貫性の重み（$w^o_{\mathbf si}$）の除去によるスコア低下が大きく、ノイズを除去して最適な教師知識をフィルターするプロセスが不可欠であることが示されました。
  - 埋め込み蒸留においても、テキスト意味的知識のマッピングを抜いた場合（w/o $all_e$）や単純なHint学習に置き換えた場合に明確な性能劣化がみられ、本手法の単純ながらも高度なMLPベースのマッピングの有効性が示されました。
- **結論:** 大規模言語モデルから小規模なシーケンシャルモデルへの知識蒸留において、ただ単に出力を近づけるのではなく、信頼度や生徒モデルとの一貫性を自律的に考慮した「ランキング蒸留」と、意味空間のギャップを的確に埋める「協調埋め込み蒸留」をハイブリッドに組み合わせることが、大幅な推薦精度の引き上げにつながるという強力な知見を提供しています。
