# YC バッチ企業分類フレームワーク

YC各バッチの企業を横断比較するための分類体系。Claude APIによる自動タグ付けと手動補正を組み合わせて使用。

---

## タグ定義

### L1: ビジネスモデル (`biz_model`)

| タグ | 定義 | 例 | YC代表例 |
|------|------|----|---------|
| `SaaS` | 月額/年額サブスクリプション収益。ソフトウェアのみ | Salesforce型 | Hex Security, Vela |
| `BPO_replacement` | 従来の人手業務をAIが丸ごと代替。人間不要化。取引単価×件数 | コールセンター代替, データ入力代替 | Patientdesk.ai, Robby |
| **`ai_armed_operator`** | **AIと人間の専門家を組み合わせた「AI強化型事業者」。サービスを直接提供。高信頼・監査可能が差別化** | **AI＋弁護士, AI＋会計士, AI＋医師** | **General Legal, Balance, Corvera** |
| `take_rate` | マーケットプレイス・プラットフォーム。GMVの数% | Stripe, Airbnb型 | Asimov（ロボットデータ市場）|
| `infra` | APIやインフラ提供。従量課金またはシート | AWS, Twilio型 | Terminal Use, Chamber |
| `asset_heavy` | 物理資産・製造・ハードウェアを伴う | ドローン, ロボット, デバイス | Voltair, Milliray, Pocket |

#### `ai_armed_operator`（AIをフル活用した事業者）詳説

**BPO_replacementとの違い**:
- `BPO_replacement` = AIが人間を**代替**する（ソフトウェアが人間の仕事を奪う）
- `ai_armed_operator` = AIが人間を**強化**する（AI＋人間が高品質なサービスを提供）

**特徴**:
1. **収益モデル**: 成果報酬・プロジェクトフィー・従量課金（SaaSではない）
2. **差別化**: 精度・速度・監査可能性（AIのみより高く、人間のみより安い）
3. **代表的課金**: $500/契約（General Legal）、月額固定＋従量（Balance）
4. **信頼係数**: 専門家ライセンスや資格が参入障壁になる
5. **スケール**: 人間オペレーターの採用でスケールする（ソフトのみより緩やか）

**W26のai_armed_operator事例**:
| 企業 | AI | 人間の専門家 | 価格 |
|------|----|-----------|----|
| General Legal | 契約書ドラフト | Harvard Law JD弁護士 | $500/件 |
| Balance | 帳簿照合・仕訳AI | CPAサイン | 月額定額 |
| Corvera | サプライチェーンAI | オペレーションスペシャリスト | % of savings |
| Overdrive Health | 保険請求AI | 請求専門スタッフ | 成功報酬 |

### L2: AIの使い方 (`ai_type`)

| タグ | 定義 | 例 |
|------|------|----|
| `workflow_ai` | 既存の業務ワークフローをAIで自動化・高速化 | 医療記録処理, 請求書処理 |
| `vertical_ai` | 特定業界に特化したAIプロダクト | 法律AI, 医療診断AI |
| `infra` | AI開発・運用を支えるインフラ・ツール | ベクターDB, エージェント評価 |
| `new_behavior` | AIによって初めて可能になる新しい行動・体験 | ゲーム生成, アバター通話 |
| `ai_armed_operator` | AI＋人間のハイブリッド運営。オペレーター型 | General Legal（AI＋弁護士） |
| `non_ai` | AIを主要要素としない | ハードウェアのみ, 純粋なマーケットプレイス |

### L3: カスタマーセグメント (`customer`)

| タグ | 定義 |
|------|------|
| `B2B` | 企業向け（SMB/エンタープライズ） |
| `B2C` | 消費者向け |
| `B2B2C` | 企業経由で消費者に届く（例: 医療プラットフォーム） |
| `gov` | 政府・公共機関向け（防衛含む） |

### L4: 業界タグ (`industry`)

主要カテゴリ（複数付与可）:

- `healthcare` / `medtech` / `biotech`
- `fintech` / `insurtech`
- `legaltech`
- `devtools` / `ai_infra`
- `defense` / `govtech`
- `robotics` / `hardware`
- `energy` / `climate`
- `sales` / `marketing`
- `hr` / `operations`
- `education`
- `consumer`
- `real_estate` / `construction`
- `space` / `aerospace`
- `food` / `agritech`

---

## 補助スコア

### `japan_fit`: 日本市場での事業機会

| スコア | 基準 |
|--------|------|
| `high` | 日本に類似課題が存在し、規制・文化的障壁が低い。または日本参入が容易 |
| `mid` | 参入可能だが、ローカライズや競合対応が必要 |
| `low` | 米国特有の規制・市場慣行に依存。日本展開困難 |

### `japan_competitor`: 日本の競合有無

| スコア | 基準 |
|--------|------|
| `yes` | 日本に直接競合する製品・サービスが存在 |
| `no` | 日本に直接競合なし（ブルーオーシャン） |
| `partial` | 一部機能で競合するが、完全一致ではない |

### `cash_is_king_score`: キャッシュ回収性スコア（1〜5）

3軸の総合評価:
1. **回収速度**: 契約〜入金までのサイクル（短いほど高スコア）
2. **確実性**: チャーンリスク・支払い遅延リスク
3. **スケーラビリティ**: 単位コスト逓減の度合い

| スコア | 目安 |
|--------|------|
| 5 | 即時決済・前払い・高リテンション（例: Stripe決済代行） |
| 4 | 月次サブスク・低チャーン（例: デベロッパーツール） |
| 3 | 年次契約・中程度のチャーン |
| 2 | 長期契約・実装コスト高（例: エンタープライズSaaS） |
| 1 | ハードウェア先行投資・回収に1年超（例: ロボット, 防衛系） |

---

## Claude API タグ付けプロンプト（骨格）

```
以下の企業情報を受け取り、下記の軸で分類せよ。
必ずJSON形式で返すこと。

企業名: {name}
説明: {description}
業界タグ(YC): {tag}

出力フォーマット:
{
  "biz_model": "SaaS|BPO_replacement|take_rate|infra|asset_heavy",
  "ai_type": "workflow_ai|vertical_ai|infra|new_behavior|ai_armed_operator|non_ai",
  "customer": "B2B|B2C|B2B2C|gov",
  "industry": "{業界}",
  "japan_fit": "high|mid|low",
  "japan_competitor": "yes|no|partial",
  "cash_is_king_score": 1-5,
  "reasoning": "{分類の根拠を1〜2文で}"
}
```

---

## 自動バッチ取得ロジック（疑似コード）

```python
from datetime import datetime

BATCH_MAP = {
    "W": "Winter",
    "X": "Spring",   # 2025年新設
    "S": "Summer",
    "F": "Fall"
}

def get_current_batch():
    year = datetime.now().year % 100  # 例: 2026 → 26
    month = datetime.now().month

    if month <= 3:
        season = "W"
    elif month <= 6:
        season = "X"
    elif month <= 9:
        season = "S"
    else:
        season = "F"

    return f"{season}{year}"  # → "W26"

def get_all_batches_since(start_year=23):
    """2023年以降の全バッチを列挙"""
    batches = []
    current_year = datetime.now().year % 100
    seasons_order = ["W", "X", "S", "F"]

    for year in range(start_year, current_year + 1):
        for season in seasons_order:
            batch = f"{season}{year}"
            # X（Spring）は2025年から
            if season == "X" and year < 25:
                continue
            # F（Fall）は2023年から
            if season == "F" and year < 23:
                continue
            batches.append(batch)

    return batches

def fetch_yc_batch(batch_code):
    season, year = batch_code[0], batch_code[1:]
    season_name = BATCH_MAP[season]
    url = f"https://www.ycombinator.com/companies?batch={season_name}+20{year}"
    # スクレイプ or API呼び出し
    return url

# 全バッチ: W23, S23, F23, W24, S24, F24, W25, X25, S25, F25, W26, ...
```

---

## 分析パイプライン

```
Step 1: fetch_yc_batch(batch_code)
        → YCディレクトリから全企業のJSON取得（~190-280社）

Step 2: Claude APIで各社をタグ付け（上記プロンプト使用）
        → biz_model / ai_type / customer / industry / japan_fit 等

Step 3: 集計 → トレンド可視化
        → AI比率, セクター分布, biz_model分布

Step 4: 前バッチとdiff
        → 何が増えた/消えた（例: "copilot" → "agent" の推移）

Step 5: 日本インプリのフラグ付け
        → japan_fit=high の企業を優先リスト化
```
