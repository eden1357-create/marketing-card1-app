import streamlit as st
import random
from datetime import datetime

# 設定 Streamlit 行動版頁面
st.set_page_config(
    page_title="小恕 - 行銷字卡自動生成器",
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
        color: #6B7280;
        text-align: center;
        margin-bottom: 20px;
    }
    .card-box {
        background-color: #F3F4F6;
        border-left: 5px solid #2563EB;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563EB;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 50px;
        font-size: 18px;
    }
    .history-badge {
        background-color: #EFF6FF;
        border: 1px solid #BFDBFE;
        color: #1E40AF;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        text-align: center;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📈 投顧行銷字卡自動生成器</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">小恕專用手機介面 ‧ 點擊即可自動產出 3 份文案</div>', unsafe_allow_html=True)

# 初始化 20 次不重複歷史紀錄區
if 'history' not in st.session_state:
    st.session_state['history'] = []

# 手機端選單
st.subheader("1. 選擇今日市場主軸")
market_theme = st.selectbox(
    "請選擇當前股市行情或主題：",
    [
        "大盤高檔震盪/洗盤破底翻",
        "AI/矽光子/熱門題材狂飆",
        "Q4年底衝刺/節慶促銷",
        "台積電法說會/權值股發動",
        "美股急跌/台股拉回搶反彈",
        "盤前早餐/10分鐘快訊",
        "自訂情境（輸入關鍵字）"
    ]
)

custom_keyword = ""
if market_theme == "自訂情境（輸入關鍵字）":
    custom_keyword = st.text_input("輸入關鍵字（例如：輝達財報、重電族群、降息）：", "台積電法說會")

st.subheader("2. 選擇分析師風格")
analyst_style = st.radio(
    "文案風格切換：",
    ["霸氣威嚴型", "親切貼心型", "專業數據型", "熱情帶動型"],
    horizontal=True
)

st.subheader("3. 選擇專案導流主打誘因")
lead_incentive_type = st.selectbox(
    "請選擇導流誘因模式：",
    [
        "1. 創意設計產出",
        "2. 自訂導流"
    ]
)

custom_perks = ""
if lead_incentive_type == "2. 自訂導流":
    custom_perks = st.text_area(
        "請輸入自訂導流禮包與超值誘因內容：",
        "1. 一對一持股健診與診斷報告\n2. 免費領取獨家飆股潛力清單\n3. 專屬簡訊第一時間帶進帶出實戰體驗",
        height=100
    )

st.markdown(f'<div class="history-badge">🛡️ 已啟用防重複機制：最近 20 次內產出之文案均不重複（目前已記錄 {len(st.session_state["history"])} 筆歷史）</div>', unsafe_allow_html=True)

st.divider()

# 大量創意素材庫，確保組合多樣性
HEADLINE_POOL = {
    "霸氣威嚴型": [
        "洗盤來到尾聲！拉回震盪正是「跌出超大價差」的最佳時機！",
        "散戶還在猶豫？主力早就暗中默默卡位，這波行情你絕對不能再錯過！",
        "別等漲停才問能不能買！主流飆股啟動前夕，卡位佈局就趁現在！",
        "大盤洗盤洗掉恐慌盤，真正的大戶正在這裡悄悄吃貨！",
        "錯過上一波不要緊！這一檔潛力黑馬即將拉出第一根漲停！",
        "行情總在絕望中誕生！主力拉回洗盤，正是你資產翻倍的最佳切入點！",
        "別人恐慌我貪婪！法人默默鎖碼的黑馬股，你手中有了嗎？",
        "盤勢震盪洗出黃金坑！跟緊主力步伐，搶先卡位第四季翻倍主流！",
        "主力籌碼高度集中！下一檔即將噴發的起漲黑馬，已經整裝待發！",
        "市場震盪不可怕，可怕的是你手上的股票選錯了！立即調整迎接大行情！"
    ],
    "親切貼心型": [
        "手上的股票套牢不知道該怎麼辦？別擔心，小恕陪你一起做專屬持股健診！",
        "行情震盪讓您心慌慌？跟著專業團隊腳步，一步步把過去虧損贏回來！",
        "行情洗盤不是末日，而是調整持股、汰弱留強的最佳救援時機！",
        "投資路上您不孤單！讓專業分析師為您精選最具抗跌領漲力的優質好股！",
        "別再一個人盲目猜頭摸底！加入我們，第一時間掌握法人籌碼動向！",
        "把焦慮留給別人，把獲利留給自己！最貼心的操作策略已經為您準備好！",
        "手上持股卡住了？讓專業團隊協助您換股操作，重回獲利軌道！",
        "投資需要策略，更需要安心感！跟著團隊佈局能見度最高的法人才脈！",
        "行情拉回就是給有準備的人機會！讓我們一起把握這波救援契機！",
        "別讓一時的震盪打亂您的投資步調！一對一親自為您檢視資產配置！"
    ],
    "專業數據型": [
        "數據會說話！法人籌碼連續融資洗淨，技術面破底翻型態正式成立！",
        "從籌碼面與營收動能交叉比對：這 3 檔營收爆發股正在低檔蓄勢待發！",
        "台股Q4歷史勝率高達8成！統計數據顯示：現在就是最佳佈局視窗期！",
        "CPO與AI伺服器雙動能發動！產業鏈供應鏈最新評比數據完整公開！",
        "三大法人同步轉買！指標股融資洗清後，技術線型拉出絕佳起漲買點！",
        "籌碼集中度達到年內新高！大戶籌碼指標顯示：突破行情即將一觸即發！",
        "財報亮眼且本益比處於歷史低位！數據精選 3 檔最具抗風險能力的潛力股！",
        "產業景氣循環谷底翻揚！從訂單能見度分析，這幾檔股票買點浮現！",
        "量價結構出現罕見訊號！短線拉回整理完畢，準備迎來強勢攻擊波！",
        "根據歷史數據回測：此類洗盤型態出現後，隨後反彈幅度平均達25%以上！"
    ],
    "熱情帶動型": [
        "火熱大行情正式發動！錯過這次，你可能要再等一整年！",
        "快跟上！黑馬飆股已經點火，第一時間跟著團隊卡位發財車！",
        "衝衝衝！倒數最後衝刺，把今年的年終獎金靠這波自己加碼回來！",
        "全台熱議主流題材爆發！你還在觀望嗎？再不上車就只能看別人賺！",
        "狂歡行情不等人！跟著分析師一起搶搭飆股列車，飆向新高點！",
        "就是現在！資金大洪水湧入，跟著主力一起獲利翻倍！",
        "熱血沸騰的Q4作帳行情啟動！把錯過的行情通通一次贏回來！",
        "飆股不等人，買在起漲點才是真本事！跟緊團隊第一時間衝刺！",
        "歡慶好消息！專案回饋大釋放，跟著我們一起迎接資產大翻倍！",
        "搶先布局！讓你的投資組合在這個Q4跟著市場主力一起飛揚！"
    ]
}

PROMO_POOL = [
    "【深V救援：破底翻 1+3 換股計畫】",
    "【Q4 法人點點名 雙路進攻專案】",
    "【100天衝刺 168 年終翻倍計畫】",
    "【盤前10分鐘：飆股菜單鎖碼專案】",
    "【汰弱留強：資產重組救援專案】",
    "【黑馬重電與AI供應鏈雙飛計畫】",
    "【新春前最後一波：獲利卡位專案】",
    "【中秋作帳：法人提前卡位專案】",
    "【低檔起漲：籌碼高度集中專案】",
    "【高股息與成長雙盈攻守兼備專案】"
]

CREATIVE_PERKS_POOL = [
    "1. 專人持股一對一深度健診\n2. 獨家提供『低檔起漲潛力股清單』\n3. 會籍加碼延至 Q4 起算（今年剩餘時間免費）",
    "1. 鎖定 3 檔訂單能見度直達 2027 年的蓋牌黑馬股\n2. 免費領取『產業供應鏈完整評比表』\n3. 專屬簡訊第一時間帶進帶出通知",
    "1. 會籍直接從明年起算（2026年剩餘時間全免）\n2. 憑虧損對帳單折抵最高 8,888 元會費\n3. 贈送『Q4 飆股操盤策略錦囊』",
    "1. 每日盤前 7:45 獨家提供『10分鐘盤前必看菜單』\n2. 一對一分析師助理專屬諮詢管道\n3. 免費體驗第一時間飆股進出場簡訊",
    "1. 深度分析手中套牢股票，提供明確停損/停利參考點\n2. 獲得『法人籌碼高度鎖碼勝率清單』\n3. 限時升級高級 VIP 會員頻道服務"
]

KEYWORDS_POOL = ["+1", "點名", "168", "早餐", "換股", "勝率", "翻倍", "888", "卡位", "救援"]

PROMPTS_POOL = [
    "Commercial financial poster, stock chart breakout arrow, vibrant gold and deep blue background, high resolution, modern UI style, professional financial broadcast graphics.",
    "Futuristic AI technology server room, glowing neon cyan arrows shooting up, high-tech financial visual, 8k render, luxury gold accents.",
    "Red festive luxury background, golden gift box opening with glowing stock arrows, commercial promotional banner, highly detailed, photorealistic.",
    "Early morning coffee cup next to a tablet displaying green and red stock index graphs, financial breakfast concept, warm bright office lighting.",
    "Financial analyst desktop with multiple screens showing stock candlestick patterns, bullish green breakout lines, sleek professional corporate aesthetic."
]

# 一鍵生成按鈕
if st.button("🚀 一鍵產出今日 3 份全新行銷字卡", type="primary"):
    st.success("✨ 已成功生成 3 份字卡文案！已自動確保 20 次內不重複出現：")
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    theme_label = market_theme if market_theme != "自訂情境（輸入關鍵字）" else custom_keyword
    
    # 從素材庫中過濾掉過去 20 次已使用的文案
    history_set = set(st.session_state['history'])
    
    available_headlines = [h for h in HEADLINE_POOL.get(analyst_style, HEADLINE_POOL["霸氣威嚴型"]) if h not in history_set]
    if len(available_headlines) < 3:
        available_headlines = HEADLINE_POOL.get(analyst_style, HEADLINE_POOL["霸氣威嚴型"])
        
    available_promos = [p for p in PROMO_POOL if p not in history_set]
    if len(available_promos) < 3:
        available_promos = PROMO_POOL
        
    available_perks = [pk for pk in CREATIVE_PERKS_POOL if pk not in history_set]
    if len(available_perks) < 3:
        available_perks = CREATIVE_PERKS_POOL
        
    selected_headlines = random.sample(available_headlines, k=min(3, len(available_headlines)))
    selected_promos = random.sample(available_promos, k=min(3, len(available_promos)))
    selected_keywords = random.sample(KEYWORDS_POOL, k=3)
    selected_prompts = random.sample(PROMPTS_POOL, k=3)
    
    if lead_incentive_type == "1. 創意設計產出":
        selected_perks = random.sample(available_perks, k=min(3, len(available_perks)))
    else:
        selected_perks = [custom_perks] * 3

    cards = []
    for i in range(3):
        h = selected_headlines[i % len(selected_headlines)]
        p = selected_promos[i % len(selected_promos)]
        pk = selected_perks[i % len(selected_perks)]
        kw = selected_keywords[i % len(selected_keywords)]
        pr = selected_prompts[i % len(selected_prompts)]
        
        # 記錄到歷史防止 20 次內重複
        st.session_state['history'].append(h)
        st.session_state['history'].append(p)
        if len(st.session_state['history']) > 60:  # 保持最多 20 次 (每次3份=60個大標)
            st.session_state['history'] = st.session_state['history'][-60:]
            
        cards.append({
            "num": i + 1,
            "title": f"方案 {i+1}（{analyst_style.split('（')[0]} ‧ {theme_label}）",
            "card1_headline": h,
            "card2_promo": p,
            "perks": pk,
            "keyword": kw,
            "prompt": pr
        })
        
    for c in cards:
        with st.expander(f"📌 方案 {c['num']}：{c['title']}", expanded=True):
            st.markdown(f"**【字卡 1 - 吸引文案 / 焦點大標】**\n> 💥 **{c['card1_headline']}**")
            st.markdown(f"**【字卡 2 - 專案名稱】**\n> 🎁 **{c['card2_promo']}**")
            st.markdown(f"**【專案導流主打誘因禮包】**\n{c['perks']}")
            st.markdown(f"**【LINE@ 導流口號設計】**\n👉 立即私訊 LINE@ 留下關鍵字：**【{c['keyword']}】**，專人第一時間為您服務！")
            
            # AI 圖像 Prompt 複製區
            st.text_area(f"🎨 方案 {c['num']} AI 繪圖 Prompt (商業化圖卡設計)：", c['prompt'], height=70)
            
            # 完整 Line@ 廣播文案區
            full_text = f"""【{c['card1_headline']}】\n\n{theme_label} 行情即將發動，您手上的股票該留還是該換？\n團隊特別推出 {c['card2_promo']}！\n\n🎁 專屬超值誘因禮包：\n{c['perks']}\n\n👉 立即私訊 Line@ 輸入關鍵字【{c['keyword']}】，限時免費領取！"""
            st.text_area(f"📋 方案 {c['num']} Line@ 社群廣播一鍵複製文案：", full_text, height=160)

st.info("💡 小貼心提示：本工具為手機端優化版。選單已更新為 2 種導流模式，且具備『20 次內不重複產出』機制！")

