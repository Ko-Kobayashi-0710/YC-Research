#!/usr/bin/env python3
"""
YC W26 バッチ分析レポート生成スクリプト
出力: docs/yc_w26_report.pdf
"""

import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import rcParams
import numpy as np

# ---- 日本語フォント設定 ----
import matplotlib.font_manager as fm
# NotoSansCJKを直接登録してから使う
_jp_ttc = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
try:
    fm.fontManager.addfont(_jp_ttc)
except Exception:
    pass
fm._load_fontmanager(try_read_cache=False)
try:
    fm.fontManager.addfont(_jp_ttc)
except Exception:
    pass
jp_fonts = [f.name for f in fm.fontManager.ttflist if any(k in f.name for k in ['Noto Sans CJK', 'IPAex', 'Hiragino', 'Yu Gothic', 'MS Gothic'])]
if jp_fonts:
    rcParams['font.family'] = jp_fonts[0]
else:
    rcParams['font.family'] = 'DejaVu Sans'

rcParams['axes.unicode_minus'] = False
rcParams['figure.dpi'] = 150

OUTPUT_PATH = '/home/user/YC-Research/docs/yc_w26_report.pdf'

# ============================================================
# データ定義
# ============================================================

# --- 事業カテゴリー分布（191社ベース）---
BIZ_CATEGORIES = {
    'AIエージェント\nインフラ・DevTools': 38,
    'エンタープライズ\n業務自動化': 28,
    'ヘルスケア\nバイオテック': 22,
    'フィンテック\nエージェント経済': 18,
    'ロボティクス\nハードウェア': 18,
    '防衛・宇宙\n航空': 12,
    'リーガルテック\nコンプライアンス': 11,
    '不動産・建設\n空間テック': 10,
    'コンシューマー\nクリエイター': 9,
    'セキュリティ': 7,
    'セールス・\nマーケ自動化': 7,
    'HR・採用・\n給与': 7,
    'エネルギー\nインフラ': 6,
    'その他': 8,
}

# --- ビジネスモデル分布 ---
BIZ_MODELS = {
    'SaaS / Workflow AI': 72,
    'AI-armed\nOperator': 22,
    'Infra / Platform': 38,
    'Take-rate /\nMarketplace': 18,
    'BPO\nReplacement': 12,
    'Asset-heavy\nHardware': 22,
    'その他': 7,
}

# --- 創業者バックグラウンド ---
FOUNDER_BG = {
    'Big Tech\n(GAFAM等)': 32,
    'スタートアップ\n出身': 28,
    'アカデミア\n(PhD/研究者)': 22,
    'ドメイン専門家\n(医師/弁護士/金融)': 18,
    '学生・\n若手起業家': 10,
    '政府/軍/\n宇宙機関': 8,
    'その他': 12,
}

# --- 主要企業一覧（注目度順）---
COMPANIES_TABLE = [
    # カテゴリー, 企業名, 事業概要, 注目ポイント, japan_fit
    ('AGI/基盤研究', 'Ndea', 'François Chollet（Keras創始者）設立AGI研究ラボ', '$43M調達。ARC賞主催者が「革新できるAGI」を構築', 'mid'),
    ('AGI/基盤研究', 'Confluence Tech', 'ARC-AGI-2ベンチマークで97.9%達成', 'Anthropic/OpenAI超える推論能力。業界最注目', 'low'),
    ('DevTools', 'Canary', 'コードを理解するAI QAエージェント', 'バグの根本原因まで特定。Garry Tan個人ピック', 'high'),
    ('DevTools', 'Compresr', 'LLMエージェントのコンテキスト圧縮', 'Claude Code統合済み。トークンコスト削減直撃', 'high'),
    ('DevTools', 'Sentrial', 'AIエージェント失敗をユーザー前に検知', 'エージェント本番化の必須インフラ', 'mid'),
    ('Fintech', 'Fenrock AI', '金融犯罪コンプライアンスAI（10倍処理量）', 'FCC市場$4B。監査ログ自動生成で規制対応', 'high'),
    ('Fintech', 'Didit', 'グローバルKYC/本人確認の"Stripe"', '双子創業者 from Barcelona。190+国対応', 'high'),
    ('Fintech', 'Balance', 'SMB向けフルスタックAI会計', 'AIが処理→CPA承認。ai_armed_operator最右翼', 'high'),
    ('Healthcare', 'Beacon Health', 'AIで一次医療機関の収益倍増', '$5.4M（Accel+Sequoia）。事前承認自動化', 'mid'),
    ('Healthcare', 'Opalite Health', '医療向けAI通訳（EHR統合）', '言語バリア解消。日本の医療現場に直接適用可', 'high'),
    ('Healthcare', 'Patientdesk.ai', '患者電話・予約管理AIエージェント', 'クリニック受付の完全自動化', 'high'),
    ('Legal', 'General Legal', 'グロース期向けAIネイティブ法律事務所', '$500/件・3時間以内。Harvard Law JD x3', 'mid'),
    ('Legal', 'LegalOS', '複雑就労ビザをAI処理するAI法律事務所', 'ビザ申請の完全自動化。移民市場直撃', 'mid'),
    ('Enterprise', 'Corvera', 'CPGブランドのバックオフィスAIエージェント', '$33K MRR/4週・12ブランド。超速PMF', 'mid'),
    ('Enterprise', 'Jinba', 'チャット経由でエンタープライズWF全自動化', '既存システム連携でスムーズ導入', 'high'),
    ('Enterprise', 'FullSeam', '財務・経理チーム向けAI従業員', '経理業務の完全AI代替。CFO直訴型', 'high'),
    ('Security', 'Hex Security', '自律型攻撃的セキュリティ（継続レッドチーミング）', 'SOC2取得工数を1/10に。急成長セグメント', 'high'),
    ('Security', 'BeeSafe AI', '詐欺・スキャムを顧客到達前に阻止', '金融機関向け。日本の振り込み詐欺対策に刺さる', 'high'),
    ('Real Estate', 'Bidflow', '電気工事見積もりAIコパイロット', '建設DX後進分野。BOM自動生成で職人支援', 'high'),
    ('Real Estate', 'Automax.ai', 'AIネイティブ不動産鑑定（LiDAR+CV）', '$4M調達。Fannie Mae準拠・20分以内完了', 'high'),
    ('Robotics', 'Pocket', 'AIノートテイキングデバイス', '30,000台/5ヶ月・MoM+50%。D2Cハード最注目', 'high'),
    ('Robotics', 'OctaPulse', '魚養殖完全自動化（孵化→収穫）', '食料安全保障×AI。水産大国・日本に高適合', 'high'),
    ('Energy', 'Condor Energy', 'エネルギー管理OS（再エネ最適化）', '電力調達コスト削減。日本の電力自由化と合致', 'high'),
    ('Defense/Space', 'GRU Space', '月面ホテル建設（2027年着陸予定）', '議会・White House招待。最もロマンある挑戦', 'low'),
    ('Consumer', 'Cardboard', 'AIエージェント動画編集', 'HN #1アップボート（1,480pt）。クリエイター直撃', 'high'),
    ('Consumer', 'Pax Historia', 'AIオルタナティブ歴史SLGゲーム', 'DAU 35,000・2000万ラウンド。ゲームAI革命', 'high'),
    ('HR', 'Perfectly', 'AI採用OS（ソーシング→内定まで）', '採用全プロセスのAI化。HR-techの刷新', 'high'),
    ('HR', 'Central', 'スタートアップ向けAI給与・HR全部入り', '$8.6M（First Round+YC）。月10h節約実績', 'mid'),
    ('Insurance', 'Tesora', '保険引受・保険数理AIネイティブSaaS', '"Harvey for insurance"。Stanford CS/ex-Google', 'high'),
    ('Infra', 'Cumulus Labs', '最適化GPUクラウド', 'GPUコスト削減インフラ。AI企業全員が顧客候補', 'mid'),
]

# ============================================================
# グラフ生成関数
# ============================================================

COLORS_MAIN = [
    '#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F',
    '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC',
    '#D4E09B', '#F6A8B7', '#A9D6E5', '#C9B8E8'
]

def autopct_format(pct):
    return f'{pct:.1f}%' if pct >= 4 else ''


def draw_pie(ax, data_dict, title, colors=None):
    labels = list(data_dict.keys())
    values = list(data_dict.values())
    clrs = (colors or COLORS_MAIN)[:len(labels)]

    wedges, texts, autotexts = ax.pie(
        values, labels=None, autopct=autopct_format,
        colors=clrs, startangle=140,
        pctdistance=0.78,
        wedgeprops=dict(linewidth=0.8, edgecolor='white')
    )
    for at in autotexts:
        at.set_fontsize(7)
        at.set_color('white')
        at.set_fontweight('bold')

    ax.set_title(title, fontsize=11, fontweight='bold', pad=12)

    # 凡例
    legend_labels = [f'{l}  ({v}社)' for l, v in zip(labels, values)]
    ax.legend(
        wedges, legend_labels,
        loc='lower center', bbox_to_anchor=(0.5, -0.45),
        ncol=2, fontsize=7, frameon=False
    )


# ============================================================
# PDF 生成
# ============================================================

with PdfPages(OUTPUT_PATH) as pdf:

    # ---- ページ1: タイトル & サマリー ----
    fig, ax = plt.subplots(figsize=(11, 8.5))
    ax.axis('off')

    # タイトルブロック
    ax.text(0.5, 0.88, 'YC W26 (Winter 2026) バッチ分析レポート',
            ha='center', va='center', fontsize=20, fontweight='bold',
            transform=ax.transAxes, color='#1a1a2e')
    ax.text(0.5, 0.81, 'Demo Day: 2026年3月24日  |  総社数: 196社  |  カバレッジ: 191社 (97%)',
            ha='center', va='center', fontsize=11, transform=ax.transAxes, color='#444')
    ax.axhline(y=0.77, xmin=0.05, xmax=0.95, color='#4E79A7', linewidth=2)

    # KPIボックス
    kpis = [
        ('196社', 'W26採択数\n（過去最多）'),
        ('60%', 'AI関連\n企業割合'),
        ('64%', 'B2B\n企業割合'),
        ('14社', '$1M ARR\n達成（最多記録）'),
        ('97%', 'カバレッジ\n（191/196社）'),
    ]
    box_colors = ['#4E79A7', '#F28E2B', '#59A14F', '#E15759', '#B07AA1']
    for i, (val, label) in enumerate(kpis):
        x = 0.1 + i * 0.18
        fancy = mpatches.FancyBboxPatch((x - 0.07, 0.54), 0.14, 0.18,
            boxstyle='round,pad=0.01', transform=ax.transAxes,
            facecolor=box_colors[i], edgecolor='white', linewidth=1.5, alpha=0.9)
        ax.add_patch(fancy)
        ax.text(x, 0.665, val, ha='center', va='center', fontsize=16,
                fontweight='bold', transform=ax.transAxes, color='white')
        ax.text(x, 0.575, label, ha='center', va='center', fontsize=7.5,
                transform=ax.transAxes, color='white')

    # トレンドサマリー
    trends = [
        '① AIエージェントの「本番稼働」時代へ — インフラ・監視・ガードレール系が急増',
        '② Vertical AI の3モデル確立 — Copilot型 / Agent型 / AI-enabled Services型',
        '③ "ai_armed_operator" 台頭 — AIと人間専門家のハイブリッドが主戦場',
        '④ 規制産業（医療・法律・金融・保険）への深い浸透 — ドメイン知識×AIが参入障壁',
        '⑤ ハードウェア・ロボティクス復権 — W26の14%がハード系（過去最高水準）',
        '⑥ 防衛・宇宙参入が正常化 — Seeing Systems/DroneTector/AxionOrbital等',
    ]
    ax.text(0.05, 0.50, 'W26 主要トレンド', fontsize=11, fontweight='bold',
            transform=ax.transAxes, color='#1a1a2e')
    ax.axhline(y=0.48, xmin=0.05, xmax=0.95, color='#ddd', linewidth=0.8)
    for i, t in enumerate(trends):
        ax.text(0.06, 0.44 - i * 0.062, t, fontsize=9,
                transform=ax.transAxes, color='#333')

    ax.text(0.95, 0.02, 'generated by Claude Code  |  data: yc-oss API + WebSearch  |  2026-03',
            ha='right', fontsize=7, transform=ax.transAxes, color='#aaa')
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

    # ---- ページ2: 事業カテゴリー円グラフ + ビジネスモデル円グラフ ----
    fig, axes = plt.subplots(1, 2, figsize=(14, 8))
    fig.suptitle('YC W26 — カテゴリー & ビジネスモデル分布', fontsize=13, fontweight='bold', y=1.01)

    draw_pie(axes[0], BIZ_CATEGORIES, '事業カテゴリー別分布（191社）')
    draw_pie(axes[1], BIZ_MODELS, 'ビジネスモデル別分布（191社）')

    plt.tight_layout(pad=3.0)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

    # ---- ページ3: 創業者バックグラウンド円グラフ ----
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.suptitle('YC W26 — 創業者バックグラウンド分布', fontsize=13, fontweight='bold')
    draw_pie(ax, FOUNDER_BG, '創業者バックグラウンド（推計・主要創業者ベース）')
    # 補足注釈
    fig.text(0.5, 0.01,
        '※ YC公式プロフィール・LinkedIn・WebSearch情報をもとに分類（複数バックグラウンド保有者は主要な属性で分類）',
        ha='center', fontsize=7.5, color='#888')
    plt.tight_layout(pad=4.0)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

    # ---- ページ4〜5: 採択先一覧表 ----
    def draw_table_page(fig_title, rows, page_num, total_pages):
        fig, ax = plt.subplots(figsize=(14, 9))
        ax.axis('off')
        fig.suptitle(fig_title, fontsize=13, fontweight='bold')

        col_labels = ['カテゴリー', '企業名', '事業概要', '注目ポイント', '日本\n適合度']
        col_widths = [0.10, 0.12, 0.35, 0.36, 0.07]

        # ヘッダー
        y_start = 0.93
        x_positions = [0.02, 0.13, 0.26, 0.62, 0.95]
        header_bg = mpatches.FancyBboxPatch((0.01, y_start - 0.01), 0.97, 0.045,
            boxstyle='round,pad=0.005', transform=ax.transAxes,
            facecolor='#4E79A7', edgecolor='none')
        ax.add_patch(header_bg)
        for xi, label in zip(x_positions, col_labels):
            ax.text(xi, y_start + 0.012, label, ha='left', va='center',
                    fontsize=8, fontweight='bold', color='white', transform=ax.transAxes)

        # 行
        row_h = 0.072
        for i, (cat, name, desc, point, jfit) in enumerate(rows):
            y = y_start - 0.058 - i * row_h
            bg_color = '#f7f9fc' if i % 2 == 0 else 'white'
            row_bg = mpatches.FancyBboxPatch((0.01, y - 0.025), 0.97, row_h - 0.005,
                boxstyle='round,pad=0.003', transform=ax.transAxes,
                facecolor=bg_color, edgecolor='#e0e0e0', linewidth=0.4)
            ax.add_patch(row_bg)

            jfit_color = {'high': '#27ae60', 'mid': '#f39c12', 'low': '#c0392b'}.get(jfit, '#888')
            jfit_label = {'high': '★高', 'mid': '◎中', 'low': '△低'}.get(jfit, '—')

            ax.text(x_positions[0], y + 0.006, cat, ha='left', va='center',
                    fontsize=7, color='#555', transform=ax.transAxes)
            ax.text(x_positions[1], y + 0.006, name, ha='left', va='center',
                    fontsize=7.5, fontweight='bold', color='#1a1a2e', transform=ax.transAxes)
            ax.text(x_positions[2], y + 0.006, desc, ha='left', va='center',
                    fontsize=7, color='#333', transform=ax.transAxes, wrap=True)
            ax.text(x_positions[3], y + 0.006, point, ha='left', va='center',
                    fontsize=7, color='#555', transform=ax.transAxes)
            ax.text(x_positions[4], y + 0.006, jfit_label, ha='left', va='center',
                    fontsize=8, fontweight='bold', color=jfit_color, transform=ax.transAxes)

        ax.text(0.95, 0.01, f'{page_num} / {total_pages}', ha='right', fontsize=8,
                transform=ax.transAxes, color='#aaa')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close(fig)

    # ページ分割（15行ずつ）
    chunk = 15
    total_pages_table = (len(COMPANIES_TABLE) + chunk - 1) // chunk
    for pi in range(total_pages_table):
        rows_chunk = COMPANIES_TABLE[pi * chunk:(pi + 1) * chunk]
        draw_table_page(
            f'YC W26 注目企業一覧（{pi*chunk+1}〜{min((pi+1)*chunk, len(COMPANIES_TABLE))}社）',
            rows_chunk, pi + 1, total_pages_table
        )

    # ---- 最終ページ: DDフレームワーク活用ガイド ----
    fig, ax = plt.subplots(figsize=(11, 8.5))
    ax.axis('off')
    ax.text(0.5, 0.94, 'リサーチフレームワーク & 活用ガイド',
            ha='center', fontsize=14, fontweight='bold', transform=ax.transAxes, color='#1a1a2e')
    ax.axhline(y=0.90, xmin=0.05, xmax=0.95, color='#4E79A7', linewidth=1.5)

    sections = [
        ('DDフレームワーク（10軸）', [
            '1. 市場概況と競合環境  2. Why Now（タイミング）  3. Moat（競争優位）',
            '4. マネタイズ戦略      5. プロダクト開発       6. PMF検証',
            '7. 資金使途            8. 市場選定             9. 事業進捗  10. チーム',
            '→ framework/dd_framework.md',
        ]),
        ('BVP論点マッピング', [
            '3ビジネスモデル: Copilot型 / Agent型 / AI-enabled Services型',
            'PMF 7シグナル: TTV / 使用深度 / 持続性 / Second-bite / NPS / 持続ARR / セールス',
            '→ framework/bvp_dd_mapping.md',
        ]),
        ('DDチェックリスト（小林+a16z+Bessemer）', [
            '"Understanding is all you need" — データ≠モート、理解がモート',
            '総合評価クイックチェック: 必須5条件 / 加点7条件 / レッドフラグ5条件',
            '→ framework/dd_checklist_genai.md',
        ]),
        ('データソース', [
            '・yc-oss API（raw.githubusercontent.com/yc-oss/api/main/batches/winter-2026.json）',
            '・WebSearch（TechCrunch / HackerNews Launches / Extruct AI / VC Corner）',
            '・生データ: data/w26_raw_yc_oss.json（132社）',
        ]),
    ]

    y = 0.85
    for title, lines in sections:
        ax.text(0.06, y, f'▶ {title}', fontsize=10, fontweight='bold',
                transform=ax.transAxes, color='#4E79A7')
        y -= 0.04
        for line in lines:
            ax.text(0.09, y, line, fontsize=8.5, transform=ax.transAxes, color='#444')
            y -= 0.038
        y -= 0.02

    ax.text(0.5, 0.03, 'YC W26 Research Repository  |  branch: claude/yc-w26-trend-analysis-UQJ9q  |  2026-03',
            ha='center', fontsize=7.5, transform=ax.transAxes, color='#aaa')
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

    # PDF メタデータ
    d = pdf.infodict()
    d['Title'] = 'YC W26 バッチ分析レポート'
    d['Author'] = 'Claude Code'
    d['Subject'] = 'YC Winter 2026 Startup Analysis'
    d['Keywords'] = 'YCombinator W26 AI Startup Analysis'

print(f"PDF generated: {OUTPUT_PATH}")
