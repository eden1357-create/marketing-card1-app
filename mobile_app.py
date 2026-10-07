import streamlit as st
import random
from datetime import datetime

# 設定 Streamlit 行動版頁面
st.set_page_config(
    page_title="小恕 - 投顧行銷字卡自動生成器",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自訂手機端 CSS 美化
st.markdown("""
<style>
    .main-title {
        font-size: 24px !important;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 14px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563EB;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 52px;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📈 投顧行銷字卡自動生成器</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">小恕專用手機介面 ‧ 每次點擊生成全新創意文案</div>', unsafe_allow_html=True)

# 1. 市場主軸
st.subheader("1. 選擇今日市場主軸")
market_theme = st.selectbox(
    "請選擇當前股市行情或主題：",
    [
        "📈 大盤高檔震盪／洗盤破底翻",
        "📉 美股急跌／台股拉回搶反彈",
        "🤖 AI與半導體／先進封裝狂飆",
        "⚡ CPO矽光子與車用／新題材發動",
        "💰 Q4集團作帳／年底衝刺行情",
        "🎁 節慶特惠（中秋／父親節／雙11／新春）",
        "💵 高股息／除權息與高殖利率佈局",
        "🍳 盤前早餐／每日開盤10分鐘快訊",
        "✍️ 自訂情境（輸入關鍵字）"
    ]
)

custom_keyword = ""
if market_theme == "✍️ 自訂情境（輸入關鍵字）":
    custom_keyword = st.text_input("輸入關鍵字（例如：台積電法說會、輝達財報、重電爆發）：", value="台積電法說會")

# 2. 分析師風格
st.subheader("2. 選擇分析師風格")
analyst_style = st.radio(
    "文案風格切換：",
    ["🦁 霸氣威嚴型（強勢帶盤）", "🤝 親切貼心型（溫暖救援）", "📊 專業數據型（精準分析）", "🔥 熱情喊話型（帶動情緒）"],
    horizontal=True
)

# 3. 核心誘因
st.subheader("3. 選擇專案導流主打誘因")
promo_perk = st.selectbox(
    "主打誘因禮包：",
    [
        "🩺 1對1免費持股健診 + 汰弱留強報告",
        "🎯 獨家飆股潛力清單（蓋牌3檔）",
        "🧾 憑虧損對帳單折抵會費（專案救援）",
        "⏳ 會籍加碼延長（2026剩餘時間免費+Q4起算）",
        "📱 盤中簡訊第一時間帶進帶出實戰體驗"
    ]
)

st.divider()

# 動態創意文案資料庫 (動態組合)
HEADLINE_BANK = {
    "震盪": [
        "洗盤來到最後尾聲！震盪拉回正是「跌出超大價差」的最佳時機！",
        "大盤洗盤不用怕！主力洗掉散戶籌碼，這幾檔「破底翻黑馬」準備暴衝！",
        "行情總在絕望中誕生！別人恐慌拋售，我們趁低拉回鎖定主流！",
        "主力洗盤震盪，是在為下一波主升段蓄勢！你手上的套牢股換好了嗎？"
    ],
    "反彈": [
        "美股急跌不用恐慌！台股拉回正是「黃金加碼點」！",
        "別人看跌說跌，我們看清籌碼！這波 V 型反彈攻勢即將爆發！",
        "錯過低點你會後悔！大盤止跌訊號出現，第一時間搶進這 3 檔飆股！",
        "超跌就是最大的利多！主力抄底名單已備妥，你準備好翻身了嗎？"
    ],
    "AI": [
        "【AI x 先進封裝】雙主線狂飆！誰是下檔連拉 3 根漲停的黑馬？",
        "AI 伺服器訂單接不完！這檔供應鏈隱形冠軍籌碼剛被法人吃飽！",
        "法說會利多發酵！AI 主流卡位戰，這檔「低位階起漲股」絕不能錯過！",
        "AI 概念股百花齊放，但只有這 3 檔營收真正暴增！趕快卡位！"
    ],
    "CPO": [
        "CPO 矽光子狂飆突破新高！產業剛起飛，下一檔概念股是誰？",
        "車用與矽光子雙引擎發動！主力暗中佈局的「蓋牌黑馬」即將攤牌！",
        "飆股不等人！CPO 供應鏈大訂單落定，這檔籌碼極度乾淨！",
        "新科技題材全面引爆！誰能接棒成為下一波翻倍黑馬？"
    ],
    "Q4": [
        "Q4 大富翁搶先出發！年終最後 100 天才是資產翻身關鍵！",
        "集團作帳＋法人作帳雙重發動！Q4 必買飆股清單全面公開！",
        "年終倒數計時！搶先卡位 Q4 旺季行情，讓主力帶你賺回全年獲利！",
        "把握今年最後一次翻倍機會！Q4 飆股陣容已全數就位！"
    ],
    "節慶": [
        "歡慶專案限時快閃！給自己與家人最好的禮物就是「資產翻倍」！",
        "節慶專案限定優惠！會籍免費延長，搶先卡位下半年爆發行情！",
        "節慶感恩回饋！特別釋出 20 組 VVIP 優惠名額，帶你跟著主力賺！",
        "節慶限定大禮包！憑對帳單享專案折扣，跟著專業團隊重新出發！"
    ],
    "高股息": [
        "領完股息還要賺價差！這 3 檔「高殖利率＋營收暴增」飆股被低估了！",
        "除權息行情開跑！告別貼息陰霾，搶進填息力道最強的績優黑馬！",
        "高股息加上成長動能！法人鎖碼的雙刀流黑馬股公開！",
        "不想只賺微薄利息？這檔高股息標的籌碼極度集中，隨時發動！"
    ],
    "早餐": [
        "【盤前早餐快訊】趕著上班沒時間盯盤？3分鐘掌握今日開盤防守點！",
        "【開盤10分鐘速報】今日美股與台股衝擊評估！這族群今日最具發動相！",
        "【早餐盤前菜單】今日避險族群 vs 資金卡位名單！第一時間搶先看！",
        "【盤前重點解析】大盤今日開盤防守區間！這幾檔潛力股開盤留意點位！"
    ]
}

PROJECT_NAMES = [
    "【深V救援：破底翻 1+3 換股計畫】",
    "【Q4 法人點點名 雙路進攻專案】",
    "【100天衝刺 168 年終翻倍計畫】",
    "【AI 大聯盟：籌碼鎖碼黑馬專案】",
    "【VVIP 專屬：主力起漲卡位案】",
    "【高殖利率雙刀流：價差利息雙收專案】"
]

KEYWORDS = ["+1", "點名", "168", "早餐", "換股", "勝率", "777", "888", "卡位"]

PROMPTS = [
    "Commercial financial poster, stock chart breakout arrow shooting up, vibrant gold and deep blue light, 8k render.",
    "Futuristic AI technology server room, glowing neon cyan arrows shooting up, high-tech financial visual, 8k render.",
    "Red festive luxury background, golden gift box opening with glowing stock arrows, commercial promotional banner.",
    "Modern clean financial graphic, candlestick chart going up, bull market strength, professional 3D render.",
    "Cyberpunk style stock market board, golden rockets launching, high contrast lighting, commercial design."
]

# 按鈕觸發生成
if st.button("🚀 一鍵產出今日 3 份全新行銷字卡", type="primary"):
    st.success("✨ 已成功生成 3 份全新創意文案！每次點擊均自動重新抽換語感：")
    
    # 決定主題類型
    if "反彈" in market_theme or "急跌" in market_theme:
        key = "反彈"
    elif "AI" in market_theme:
        key = "AI"
    elif "CPO" in market_theme or "題材" in market_theme:
        key = "CPO"
    elif "Q4" in market_theme:
        key = "Q4"
    elif "節慶" in market_theme:
        key = "節慶"
    elif "高股息" in market_theme:
        key = "高股息"
    elif "早餐" in market_theme:
        key = "早餐"
    else:
        key = "震盪"

    headlines = random.sample(HEADLINE_BANK[key], min(3, len(HEADLINE_BANK[key])))
    if len(headlines) < 3:
        headlines += random.sample(HEADLINE_BANK["震盪"], 3 - len(headlines))
        
    project_samples = random.sample(PROJECT_NAMES, 3)
    kw_samples = random.sample(KEYWORDS, 3)
    prompt_samples = random.sample(PROMPTS, 3)

    for i in range(3):
        h = headlines[i]
        p_name = project_samples[i]
        kw = kw_samples[i]
        p_prompt = prompt_samples[i]
        
        if custom_keyword and market_theme == "✍️ 自訂情境（輸入關鍵字）":
            h = f"【{custom_keyword}】" + h
            
        with st.expander(f"📌 方案 {i+1}：{market_theme.split('／')[0]} - {h[:15]}...", expanded=True):
            st.markdown(f"**【字卡 1 - 吸睛大標/Hook】**\n> 💥 **{h}**")
            st.markdown(f"**【字卡 2 - 專案名稱】**\n> 🎁 **{p_name}**")
            st.markdown(f"**【主打超值誘因】**\n1. {promo_perk}\n2. 專屬分析師 team 盤中第一時間簡訊帶進帶出\n3. 獨家免費領取『Q4飆股佈局指南』")
            st.markdown(f"**【LINE@ 導流口號與關鍵字】**\n👉 立即私訊 LINE@ 留下關鍵字：**【{kw}】**，專人立即協助您！")
            
            st.text_area(f"🎨 方案 {i+1} AI 繪圖 Prompt：", p_prompt, height=70)
            
            full_text = f"【{h}】\n\n{analyst_style.split('（')[0]}分析師叮嚀：\n市場盤勢變幻莫測，您手上的股票該留還是該換？\n我們特別推出 {p_name}！\n\n🎁 專案超值禮包：\n• {promo_perk}\n• 專屬分析師 team 盤中第一時間簡訊通知\n• 免費領取『Q4飆股佈局指南』\n\n👉 立即私訊 Line@ 輸入關鍵字【{kw}】，限時領取專案名額！"
            st.text_area(f"📋 方案 {i+1} Line@ 廣播一鍵複製文案：", full_text, height=160)

st.info("💡 提示：每次點擊上方「一鍵產出」按鈕，系統皆會重新隨機組合與生成全新的文案！")
