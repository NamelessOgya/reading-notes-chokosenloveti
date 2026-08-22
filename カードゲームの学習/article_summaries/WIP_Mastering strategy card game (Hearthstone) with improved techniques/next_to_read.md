# 次に読むべき論文 (Next to Read)

本研究「Mastering strategy card game (Hearthstone) with improved techniques (arXiv:2303.05197)」は、深層強化学習とOptimistic Smooth Fictitious Play (OSFP) を組み合わせてカードゲームのマスターレベルAIを構築した重要なマイルストーンです。このアプローチ（ゼロからの自己対局による方策探索）の発展、および異なるアプローチ（脆弱性の検証・人間のデモデータからの学習）という観点から、被引用論文・関連論文として以下を読むことを推奨します。

### 1. Learning to Beat ByteRL: Exploitability of Collectible Card Game Agents (arXiv:2404.16689)
- **関連性 (別角度からのアプローチ・脆弱性評価):** 本論文のAI（通称：ByteRLエージェント）の強さが証明された一方で、エージェント自体のもつ「搾取可能性（Exploitability）」を調査した被引用研究です。強化学習エージェントが未知の戦略や敵対的なデッキ構成に対してどのように脆弱性を持つのか、またそれをいかに突いて勝率を覆すかというセキュリティ・堅牢性の観点からのフォローアップとして非常に重要です。

### 2. Contrastive Learning for Imperfect Information Games (Timo Bertram, 2024 / JKU Thesis) および関連研究 (arXiv:2407.05876)
- **関連性 (別角度からのアプローチ・対照学習):** 本研究では人間のデータを一切用いないゼロからの学習（RL+OSFP）を採用していましたが、本論文は「Contextual Preference Ranking (CPR)」と呼ばれる対照学習を用いて、人間のプレイデータ・選択嗜好から不完全情報ゲームのダイナミクスを捉えようとする研究です。とくに同じCCGである『Magic: The Gathering』に適用されており、「自己対戦重視（OSFP）」と「データドリブン重視（対照学習）」という正反対の手法を比較する上で必読の文献です。

---

> [!NOTE]
> 発表時期以降、メタアルゴリズムとしてのOSFPを直接的に発展・拡張させた後続の研究（単純な上位互換アルゴリズム）の存在は限定的です。そのため、本研究の成果を標的にした堅牢性評価（1つ目）や、カードゲームという同ドメインへの別アプローチ（2つ目）という方向性でのサーベイリングを優先しています。
