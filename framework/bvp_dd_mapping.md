# BVP記事 × DD10軸 マッピング

**参照元**:
1. *"Building Vertical AI: An Early-Stage Playbook for Founders"* — Bessemer Venture Partners (BVP)
2. *"Mastering Product-Market Fit: A Detailed Playbook for AI Founders"* — Bessemer Venture Partners (BVP)

> このドキュメントはBVP2記事の核心論点をDD10軸に振り分けたリファレンス。
> リサーチ・DD時はこのマッピングと `dd_checklist_genai.md` を並行参照すること。

---

## DD軸 1: 市場概況と競合環境

### BVP Vertical AI Playbook より
- **「Vertical AIの本質は既存ソフトウェアの置き換えではなく、人間の労働の置き換えである」**
  - 既存SaaSが「人をサポートするツール」だとすれば、Vertical AIは「人の仕事そのものを実行するシステム」
  - 評価軸: 市場の「人件費総量」がTAM。ツール市場より1-2桁大きい
- **競合は「人間のチーム」**: 競合SaaSではなく、現状の業務フローで雇われている人間を競合として定義する
- **Vertical AIが強い産業条件**:
  1. 繰り返しの多い認知作業が存在する
  2. データが構造化・デジタル化されている（または容易にできる）
  3. 業界特有の専門知識・規制・言語がある（参入障壁）

### BVP PMF Playbook より
- **「市場の引力を確認せよ」**: 顧客が「自分から来る」市場と「プッシュしなければ来ない」市場は成長速度が根本的に違う
- 初期市場の選定は「最もPainが大きく、最も支払い意欲が高い」セグメント

---

## DD軸 2: Why Now — タイミングの必然性

### BVP Vertical AI Playbook より
- **GPT-4以降のFoundation Modelで「技術的障壁」が消えた**:
  - 2022年以前: ドメイン特化AIを作るには膨大なトレーニングデータとMLエンジニアが必要
  - 2023年以降: Fine-tuning + RAG + Agentで専門知識をLLMに載せることが現実的コストで可能に
- **「最初のWave」vs「次のWave」**:
  - Wave 1 (2023-24): Copilot型（既存ワークフローへのAI付加）
  - Wave 2 (2025-): Agent型・AI-enabled Services型（タスク自体を自律実行）
  - W26はWave 2の最前線
- **データの「初めてのデジタル化」**: 医療・法律・建設・農業など、紙ベースで動いていた産業でのデータデジタル化が進行中

### BVP PMF Playbook より
- **「AI-nativeとAI-powered の区別」**:
  - AI-powered: 既存ワークフローにAIを追加
  - AI-native: AIを前提に設計されたワークフロー（これが本命）
  - Why Now: AI-nativeプロダクトを「当然のもの」として受け入れる顧客層が臨界点を超えた

---

## DD軸 3: 競争優位性 / Moatは何か

### BVP Vertical AI Playbook より（最重要セクション）

**3種類のMoatと構築方法**:

| Moat の種類 | 説明 | 強さ |
|------------|------|------|
| **Proprietary Data** | 使用するほど蓄積される独自データ（他社が再現不能） | ★★★★★ |
| **Workflow Integration** | 顧客の業務プロセスに深く統合（変えるとコストが大きい） | ★★★★ |
| **Domain Expertise** | 規制・専門用語・業界慣行に関する蓄積知識 | ★★★ |
| **Network Effects** | ユーザー増加で価値向上（Marketplace型に多い） | ★★★★ |

- **「データMoatの罠」**: データを「持っている」だけではMoatにならない。データから得られる「洞察の質」「予測精度の差」がMoat
- **Proprietary Data Loopの構造**:
  ```
  顧客が使う → 固有データ蓄積 → モデル精度向上 → 顧客満足度向上 → さらに使う
  ```
- **Vertical AI最強Moat = Workflow Lock-in × Data Loop の複合**

### BVP PMF Playbook より
- **「PMF後のMoat構築」**: PMFを達成したら、次は「競合が来ても剥がせないMoat」を意図的に構築する段階
- 具体的手法:
  1. 顧客固有データを学習させ、「このシステムが自社データを最もよく理解している」状態を作る
  2. 上流・下流ワークフローへ統合を拡大（Expansion ARRの源泉）
  3. チームの意思決定プロセスに組み込む（人事評価・会議・報告フローへ）

---

## DD軸 4: マネタイズと顧客獲得の戦略

### BVP Vertical AI Playbook より（記事の中核）

**3つのビジネスモデル**:

### モデル1: Copilot型
- **課金**: 席数課金（Per seat）、月次サブスク
- **価値提案**: 「同じ仕事をより速く・より少ないミスで」
- **プライシング原則**: 既存ツールの「代替」が基準。人件費節約の10-20%が上限目安
- **強み**: 予測可能なARR、SaaS的な拡張性
- **弱み**: 競合が模倣しやすい、差別化が難しくなる
- **YC W26例**: Cardboard（動画編集）、Avoice（建築）、Stilta（特許）

### モデル2: Agent型
- **課金**: タスク完了数・成果連動（Usage-based, Outcome-based）
- **価値提案**: 「人間の代わりにタスクを完遂する」
- **プライシング原則**: 人間が同じタスクをやる際の費用の20-40%が合理的範囲
- **強み**: スケールとともに収益急拡大、粗利改善余地大
- **弱み**: タスク定義が難しい、品質保証が課題
- **YC W26例**: Corvera（CPGオペレーション）、Tensol（スタートアップ業務）、RamAIn（ワークフロー自動化）

### モデル3: AI-enabled Services型
- **課金**: 既存サービス市場価格で受注し、内部でAIを使ってコスト削減
- **価値提案**: 「同じ品質・より速い納品・スケール可能」
- **プライシング原則**: 既存市場価格を維持（AIによる粗利改善を享受）
- **強み**: 顧客教育コスト低い、既存市場に即参入可能
- **弱み**: コモディティ化リスク、粗利改善が見えにくい
- **YC W26例**: General Legal、Arcline、Balance

**GTMモーション**:
- **PLG（Product-Led Growth）**: Copilot型に適合。フリートライアル → PoC → 拡大
- **SLG（Sales-Led Growth）**: Agent型・AI-enabled Services型。エンタープライズ向け
- **BVP推奨**: PMF前はPLGで学習、PMF後にSLGに切り替える

---

## DD軸 5: サービスのコアコンピタンス及びプロダクト開発

### BVP Vertical AI Playbook より
- **「3層スタック」の理解が必要**:
  1. Foundation Layer: LLM/モデル（GPT-4o, Claude, Gemini）
  2. Application Layer: ビジネスロジック・UX・Prompt Engineering
  3. Data Layer: 顧客固有データ・Fine-tuning・RAG知識ベース
- **「Foundation Modelはコモディティ」**: モデル自体を作ることに投資するスタートアップより、Data LayerとApplication Layerで差別化するスタートアップに投資する
- **Human-in-the-Loop設計の重要性**:
  - AI判断の「信頼スコア」を設計し、低信頼時は人間にエスカレーション
  - 人間の承認/修正データを自動的に再学習に使う
  - 顧客が「AIを信頼するまでの橋渡し」として必須

### BVP PMF Playbook より
- **「Time to Value（TTV）の最小化」がプロダクトの最優先課題**:
  - 1週間以内に価値を実感させることがPMFの前提条件
  - Onboardingの設計がプロダクト成功の鍵
- **「Aha Moment」の設計**: 顧客が「これは使える」と気づく瞬間を意図的に設計
  - 具体的: 最初の5分間で「AIが自分の仕事を正確に理解している」と感じさせる
- **Evals（評価基盤）**: 定量的な精度指標なしにプロダクト改善はできない

---

## DD軸 6: シード期の検証項目とPMFの定義

### BVP PMF Playbook より（記事の中核）

**AI-native PMF 7シグナル**（従来SaaSとの違いに注目）:

| # | シグナル | 測定方法 | AIならではの特徴 |
|---|---------|---------|----------------|
| 1 | **TTV（Time to Value）短縮** | 初使用から「Aha Moment」までの日数 | AI: ≤1週間が目標（従来SaaS: 30-90日） |
| 2 | **使用深度（Usage Depth）** | コア機能使用率、セッション時間 | AI: AIが提示した示唆を実際に採用する率 |
| 3 | **持続性（Stickiness）** | 6ヶ月コホートリテンション | AI: 曲線が「フラット」になっているか |
| 4 | **Second-bite使用率** ⭐AI-native指標 | 最初の価値体験後、別機能を試す率 | 人間の好奇心×AIの「もっとできる」体験 |
| 5 | **NPS** | 推奨スコア | AI: ≥50が強いPMFの証拠 |
| 6 | **持続ARR vs 実験ARR** | 予算カテゴリの確認 | AI: 「AI実験予算」でなく「通常業務予算」から支出されているか |
| 7 | **セールスシグナル** | 顧客からの自発的な拡張要求 | AI: 「他部門にも使いたい」「APIで接続したい」 |

⭐**Second-bite使用率**はBVPが提唱する最もAI-native固有の指標:
- 人間は「最初の試み」（First bite）で価値を感じる
- AIの真価は「何度も使う中で学習・改善される」点（Second bite以降）
- この指標が高いことはAIとユーザーの「共進化」が起きている証拠

**PMF達成の3段階**:
```
Stage 1: Individual PMF（一人のヘビーユーザーが熱狂）
Stage 2: Team PMF（チーム全体が依存）
Stage 3: Company PMF（会社の意思決定プロセスに組み込まれる）
```
- シード投資判断は「Stage 1から Stage 2への遷移」が見えているかで判断

---

## DD軸 7: シード調達後の資金使途

### BVP Vertical AI Playbook より
- **「Build → Learn → Earn」の順序を守る**:
  1. Build: 最初の10顧客に密着してプロダクト構築
  2. Learn: PMF確認（最低6ヶ月のデータ）
  3. Earn: スケールへの投資（GTM・採用）
- PMF前のスケール投資は「穴の開いたバケツに水を注ぐ行為」
- **シード期のOptimal Burn**: MRRの1.5-2x以内

### BVP PMF Playbook より
- **「Customer Success（CS）への早期投資」**:
  - PMF達成前でも、最初の10顧客に専任担当を置く（創業者自身でも可）
  - CSの目的は「解約防止」ではなく「PMF学習の最速化」
- **Feature Velocity vs Stability のトレードオフ**:
  - PMF前: 速度優先（週次デプロイ、顧客フィードバック即反映）
  - PMF後: 安定性優先（SLA・エンタープライズグレード）

---

## DD軸 8: 初期マーケットの選定理由と次マーケットへの移行

### BVP Vertical AI Playbook より
- **「Beachhead選定の5条件」**:
  1. 明確に定義可能（業界×役職×企業規模で名前が付けられる）
  2. 課題の痛みが高い（現状の解決策が明らかに不満足）
  3. 支払い意欲がある（予算化されているか、されうるか）
  4. 創業者がアクセスできる（人脈・経験）
  5. 隣接市場への橋頭堡になる（ドミノ展開の第1手）
- **「SMB vs Enterprise」の選択**:
  - SMB: 意思決定速い、チャーン率高い、NRR低め → PLGに向く
  - Enterprise: 意思決定遅い（6-18ヶ月）、チャーン率低い、Expansion余地大 → SLGに向く
  - BVP推奨: シード期はSMBでPMF→シリーズAでEnterprise移行

### BVP PMF Playbook より
- **「Vertical Expansionの論理」**:
  - 最初のVertical: 創業者の出身ドメイン（最も深い理解）
  - 2番目のVertical: 最初のVerticalと「ワークフローが似ている」産業
  - 3番目以降: データが共有できる産業

---

## DD軸 9: 創業以降の事業進捗

### BVP Vertical AI Playbook より
- **YC Demo Day後の「勝者の共通点」**:
  - Demo Day前に $100K ARRを達成している（証明された顧客課題）
  - 創業者が毎週顧客と話している（週5社以上）
  - プロダクトが「顧客が想定しない使い方」をされている（PMFの兆候）
- **「速度の可視化」**: Monthly metrics（MRR, NRR, Churn）を最初から整備

### BVP PMF Playbook より
- **「Qualitative PMF → Quantitative PMF」への移行**:
  - シード期: 定性的PMF（顧客が語る言葉・行動）
  - シリーズA: 定量的PMF（コホートリテンション・NRR・CAC/LTV）
- **「Sean Ellis Test」**: 「このプロダクトが明日使えなくなったら非常に残念ですか？」→ ≥40%が「Yes」でPMF達成の目安

---

## DD軸 10: 起業の経緯と他メンバーの役割分担

### BVP Vertical AI Playbook より
- **「Vertical AIに最適なファウンダータイプ」**:
  - Type A（Domain Expert）: その産業に10年いた専門家がAI活用を学んだ
  - Type B（Tech Expert）: AI/MLエンジニアがドメインエキスパートを採用した
  - BVP評価: Type A ≥ Type B（ドメイン知識の方が技術より再現が難しい）
- **「初期チーム設計の3役」**:
  1. Hacker（プロダクト構築）
  2. Hustler（顧客獲得）
  3. Domain Expert（業界信頼性）

### BVP PMF Playbook より
- **「Founder-Customer Distance」**: 創業者と顧客の距離が近いほどPMFが速い
  - 理想: 創業者自身がかつてそのPainを経験した人（eat your own dog food）
  - 次善: 創業者の前職の同僚・取引先が最初の顧客
- **「チームの学習速度」がPMFの到達速度を決める**:
  - 週1回の顧客フィードバックループがある
  - 「仮説→実験→検証」サイクルが2週間以内

---

## BVP論点サマリーマトリクス

| BVP核心論点 | 対応DD軸 | YC W26適用例 |
|------------|---------|-------------|
| Vertical AIのTAMは「人件費総量」 | DD1 (市場) | 医療事務、法律事務、金融コンプライアンス |
| 3モデル: Copilot/Agent/AI-enabled Services | DD4 (マネタイズ) | Corvera(Agent)、General Legal(Services) |
| Proprietary Data Loop | DD3 (Moat) | Fenrock AI、MouseCat |
| PMF 7シグナル（Second-bite最重要） | DD6 (PMF) | 全W26企業のDD適用 |
| Build→Learn→Earnの順守 | DD7 (資金使途) | PMF前スケール投資は警戒 |
| Beachhead 5条件 | DD8 (市場選定) | 創業者ドメイン×高Pain×隣接市場 |
| Domain Expert > Tech Expert | DD10 (チーム) | Verticalスタートアップ評価軸 |

---

*作成: 2026-03 | 参照記事: BVP Atlas (Vertical AI Playbook + PMF Playbook)*
