# YC Research — バッチトレンド分析リポジトリ

YCombinator の最新バッチ（W26〜）を起点に、2023年以降の全バッチを構造的に分析するためのデータ・分析リポジトリ。

## ディレクトリ構成

```
YC-Research/
├── README.md               # このファイル
├── framework/
│   └── classification.md   # 企業分類フレームワーク（L1〜L4タグ）
├── data/
│   └── batches/            # バッチ別サマリーデータ
│       ├── W23.md          # Winter 2023
│       ├── S23.md          # Summer 2023
│       ├── W24.md          # Winter 2024
│       ├── S24.md          # Summer 2024
│       ├── W25.md          # Winter 2025
│       ├── X25.md          # Spring 2025 (新設)
│       ├── S25.md          # Summer 2025
│       ├── F25.md          # Fall 2025
│       └── W26.md          # Winter 2026 ← 最新
└── analysis/
    └── w26/
        ├── overview.md     # W26 速報概要・構造シグナル考察
        ├── companies.md    # W26 企業DB（〜50社分）
        └── trends.md       # W26 トレンド分析（前バッチdiff含む）
```

## バッチ命名規則（2025年〜年4回体制）

| コード | シーズン | 時期 |
|--------|----------|------|
| W      | Winter   | 1〜3月 |
| X      | Spring   | 4〜6月（2025年新設）|
| S      | Summer   | 7〜9月 |
| F      | Fall     | 10〜12月 |

例: W26 = Winter 2026、X25 = Spring 2025

## 分析フレームワーク概要

各企業を以下7軸でタグ付け（詳細は `framework/classification.md`）:

1. **biz_model**: SaaS / BPO_replacement / take_rate / infra / asset_heavy
2. **ai_type**: workflow_ai / vertical_ai / infra / new_behavior / ai_armed_operator / non_ai
3. **customer**: B2B / B2C / B2B2C / gov
4. **industry**: 業界タグ
5. **japan_fit**: high / mid / low
6. **japan_competitor**: yes / no / partial
7. **cash_is_king_score**: 1〜5（キャッシュ回収速度・確実性）

## データソース

| 優先度 | ソース | 用途 |
|--------|--------|------|
| Primary | https://www.ycombinator.com/companies?batch={Batch} | 公式ディレクトリ |
| Secondary | Hacker News "Launch YC" タグ | リアルタイム更新 |
| Tertiary | extruct.ai / yctrends.com | 構造化済みサードパーティDB |

## AI比率の推移（W23〜W26）

| バッチ | 総社数 | AI比率 |
|--------|--------|--------|
| W23    | 282    | ~31%   |
| S23    | 247    | ~60%   |
| W24    | 260    | ~63%   |
| S24    | 255    | ~75%   |
| W25    | 160    | ~90%   |
| X25    | 144    | ~55%（agentic AI 50%超）|
| S25    | 169    | ~88%   |
| F25    | ~150   | ~52%（説明文）|
| W26    | 196    | ~60%（ただし質的転換）|

> W26の「60%」はS25の88%より低く見えるが、中身は**汎用→業務特化→高コスト失敗領域**への深化。数字より質の変化が重要。
