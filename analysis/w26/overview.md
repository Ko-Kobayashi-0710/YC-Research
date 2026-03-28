# W26 速報概要

> Demo Day: 2026年3月24日 | 作成: 2026年3月28日（Demo Day+4日）

---

## 一言サマリー

**W26 = 「AIが信頼に足る精度に達し、失敗コストの高い業務の中核に入り込んだ最初のバッチ」**

---

## KPI速報

| 指標 | W26 | 過去最高（比較） |
|------|-----|----------------|
| $1M ARR（Demo Day時点） | **14社** | 歴代最多 |
| 最高ARR | **$27M** | — |
| Rebel Fundスコア（上位20%比率） | **35%** | 過去バッチの記録なし |
| 推定ユニコーン輩出数 | **~20社**（観測者予測） | 歴史的平均は5〜10% |
| ハードウェア比率 | **14%** | YC近年最高 |
| Consumer比率 | **5%** | YC近年最低水準 |

---

## バッチ構成（ファクト）

```
総社数: 196社
├── AI系: ~60%（約118社）
│   ├── 高コスト失敗領域特化: 主流
│   ├── エージェントインフラ: 成熟
│   └── AGI研究: 3社（初の複数AGIラボ同時採択）
├── B2B: 64%
├── Consumer: ~5%
├── Hardware/Physical: ~14%（18社）
└── その他（non-AI B2B等）: ~26%

地理:
├── SF: 66%
├── ベイエリア全体: 78%
├── NYC: 6%
└── リモート: 15%
```

---

## 3大構造シグナル

### シグナル1: AI比率「60%」の罠 — 数字より質が重要

S25（88%）→ W26（60%）で下がったように見えるが、**これは退化ではなく深化**。

- S25の88%: "AIを使っている"会社の割合
- W26の60%: "AIが失敗すると命取りになる業務"に特化した会社の割合

**W26の特徴的なAIクラスター**:
- 医療: 誤診・薬の過剰処方 → **Mango Medical, Beacon Health, Opalite Health**
- 金融犯罪: マネーロンダリング検出 → **Fenrock AI, MouseCat**
- 航空・宇宙: 整備記録ミス・衛星ダウン → **Constellation Space**
- セキュリティ: 侵害見逃し → **Hex Security**

**「間違えたときのコストが高い」 = スイッチングコストが高い = 長期契約 = Cash is Kingに直結**

### シグナル2: Consumer 5% — バブル崩壊か構造変化か

YCの歴史パターン:
- Consumer少 = 景気後退期 or 不確実性が高い時期
- 2010年代前半: consumer多 → SNS・マーケットプレイスブーム
- 2022年以降: consumer減少 → B2B・インフラシフト

**W26の新しいConsumer形態（量は少ないが質的に新しい）**:
- **Pocket**: AIウェアラブルデバイス（5ヶ月で30,000台）
- **Cardboard**: 動画生成エージェント（HN最高upvote）
- **CodeWisp**: AIゲーム生成
- **Button Computer**: 新しいフォームファクターのウェアラブル

→ **「Consumer空白期」は「次のConsumerパラダイム模索期」でもある**

### シグナル3: Hardware 14% — YCの「実業×AI」戦略宣言

過去バッチではソフトウェアが圧倒的多数だったYCが、意図的にハードウェアを多様化している証拠。

**W26のHardware/Physicalクラスター**:
| 領域 | 企業 | 意味 |
|------|------|------|
| 防衛・レーダー | Milliray | 地政学リスク対応 |
| 資源探査 | Terranox AI | ウラン採掘AIの実用化 |
| ヒューマノイドデータ | Asimov | ロボット産業の基盤 |
| 自動運転インフラ | RoboDock | 自動運転後のレイヤー |
| 農業ロボット | OctaPulse | 食糧安全保障 |
| AIノートデバイス | Pocket | Consumer AIハード |
| ドローン網 | Voltair | エネルギーインフラ |

**日本への示唆**: 「実業×AI」のプレイブックを先行して見られる場所がYC

---

## セクター別日本インプリケーション

### High Priority（japan_fit: high）

| セクター | 企業例 | 日本での機会 |
|----------|--------|------------|
| 医療翻訳 | Opalite Health | 在日外国人医療、インバウンド医療 |
| 患者対応AI | Patientdesk.ai | 医療機関の人手不足対応 |
| 会計AI | Balance | 会計事務所の業務効率化 |
| KYC統合 | Didit | 金融機関のeKYC需要 |
| AML/金融犯罪 | Fenrock AI, MouseCat | FATF規制強化対応 |
| セキュリティカメラAI | Lexius | 小売・流通の万引き対策 |
| エネルギー管理 | Condor Energy | 電力自由化・再エネ管理 |
| 魚養殖自動化 | OctaPulse | 日本の水産業（世界3位規模） |
| AIスケジューリング | Vela | 製造業のシフト管理 |
| 動画AI | Cardboard | 動画マーケティング自動化 |

### Medium Priority（japan_fit: mid）

| セクター | 企業例 | 障壁 |
|----------|--------|------|
| 法務AI | General Legal | 日本の法律・商慣習の差異 |
| ロボットデータ | Asimov | ロボット産業は強いが閉鎖的 |
| 防衛レーダー | Milliray | 防衛調達の特殊プロセス |
| AGIインフラ | Ndea, Confluence | グローバル競争。日本語対応が課題 |

---

## AGI連鎖トリオの意味

```
ARC Prize Foundation
    ↓ ベンチマーク設計
    ↓ 「AIがAGIに近づいたか」を測る基準

Ndea（François Chollet設立）
    ↓ Keras創始者がAGI研究ラボ設立
    ↓ ARC-AGIベンチマークの設計者が直接AGIを作りに来た

Confluence Technologies
    ↓ ARC-AGI-2で97.9%達成
    ↓ ベンチマークの「解答者」
```

「測定者・設計者・達成者が同じバッチにいる」= **2026年はAGI転換点の可能性**

---

## Demo Day注目企業ランキング（話題度ベース）

1. **Ndea** — $43M調達済み。François Chollet。最注目
2. **Cardboard** — HN最高upvote。消費者動画AIの覇権争い
3. **Pocket** — 5ヶ月30,000台。ハードウェアの奇跡
4. **General Legal** — $500/件・3時間。リーガルテック最強の参入障壁
5. **Beacon Health** — Accel＋Sequoiaスカウト。医療AIの本命
6. **Milliray** — 防衛ドローン検知。タイミング完璧
7. **Corvera** — 4週で$33K MRR。CPGバックオフィスAI
8. **Captain** — Garry Tan個人ピック。RAGの次世代形態

---
*作成日: 2026年3月28日 | データソース: Rebel Fund, YC公式, TechCrunch, HackerNews, The VC Corner, Extruct AI*
