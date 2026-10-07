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
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📈 投顧行銷字卡自動生成器</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">小恕專用手機介面 ‧ 點擊即可自動產出 3 份文案</div>', unsafe_allow_html=True)

# 手機端情境選擇器
st.subheader("1. 選擇今日市場主軸")
market_theme = st.selectbox(
    "請選擇當前股市行情或主題：",
    [
        "大盤高檔震盪/洗盤破底翻",
        "AI/矽光子/熱門題材狂飆",
        "Q4年底衝刺/節慶促銷",
        "台積電法說會/權值股發動",
        "自訂情境（輸入關鍵字）"
    ]
)

custom_keyword = ""
if market_theme == "自訂情境（輸入關鍵字）":
    custom_keyword = st.text_input("輸入關鍵字（例如：台積電、聯發科、美股大跌）：")

st.subheader("2. 選擇分析師風格")
analyst_style = st.radio(
    "文案風格切換：",
    ["霸氣威嚴型（強勢帶盤）", "親切貼心型（溫暖救援）", "專業數據型（精準分析）"],
    horizontal=True
)

st.divider()

# 點擊生成按鈕
if st.button("🚀 一鍵產出今日 3 份行銷字卡", type="primary"):
    st.success("✨ 已成功生成 3 份字卡文案！請複製下方文案使用：")
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # 範例文案生成邏輯 (實際運作可連接 API 或寫入預設庫)
    cards = [
        {
            "num": 1,
            "title": "股市行情／洗盤救援",
            "card1_headline": "洗盤來到尾聲！震盪拉回正是「跌出超大價差」的最佳時機！",
            "card2_promo": "【深V救援：破底翻 1+3 換股計畫】",
            "perks": "1. 專人持股一對一健診\n2. 獨家提供『低檔起漲潛力股清單』\n3. 會籍加碼延至 Q4 起算",
            "keyword": "+1",
            "prompt": "Commercial financial poster, stock chart breakout arrow, vibrant gold and deep violet, high resolution, modern UI style."
        },
        {
            "num": 2,
            "title": "產業熱點／主流黑馬",
            "card1_headline": f"【{market_theme if market_theme != '自訂情境（輸入關鍵字）' else custom_keyword}】雙主線狂飆！誰是下一檔連拉 3 根漲停的黑馬？",
            "card2_promo": "【Q4 法人點點名 雙路進攻案】",
            "perks": "1. 鎖定 3 檔訂單能見度直達 2027 年的蓋牌股\n2. 免費領取產業供應鏈評比表\n3. 專屬簡訊第一時間進出場通知",
            "keyword": "點名",
            "prompt": "Futuristic AI technology server room, glowing neon cyan arrows shooting up, high-tech financial visual, 8k render."
        },
        {
            "num": 3,
            "title": "節慶與年後衝刺",
            "card1_headline": "Q4 大富翁搶先出發！最後 100 天才是資產翻身關鍵！",
            "card2_promo": "【100 天衝刺 168 翻身計畫】",
            "perks": "1. 會籍直接從明年起算（剩餘時間免費）\n2. 憑虧損對帳單折抵最高 8,888 元\n3. 贈送『Q4 飆股操盤錦囊』",
            "keyword": "168",
            "prompt": "Red festive luxury background, golden gift box opening with glowing stock arrows, commercial promotional banner, highly detailed."
        }
    ]
    
    for c in cards:
        with st.expander(f"📌 方案 {c['num']}：{c['title']}", expanded=True):
            st.markdown(f"**【字卡 1 - 吸引文案】**\n> 💥 **{c['card1_headline']}**")
            st.markdown(f"**【字卡 2 - 專案名稱】**\n> 🎁 **{c['card2_promo']}**")
            st.markdown(f"**【超值誘因禮包】**\n{c['perks']}")
            st.markdown(f"**【LINE@ 導流口號】**\n👉 立即私訊 LINE@ 留下關鍵字：**【{c['keyword']}】**，專人為您服務！")
            
            # AI 圖像 Prompt 複製區
            st.text_area(f"🎨 方案 {c['num']} AI 繪圖 Prompt：", c['prompt'], height=70)
            
            # 完整 Line@ 廣播文案區
            full_text = f"""【{c['card1_headline']}】\n\n市場震盪拉回，您手上的股票該留還是該換？\n我們特別推出{c['card2_promo']}！\n\n🎁 獨家提供：\n{c['perks']}\n\n👉 立即私訊 Line@ 輸入【{c['keyword']}】，限時領取！"""
            st.text_area(f"📋 方案 {c['num']} Line@ 廣播一鍵複製文案：", full_text, height=150)

st.info("💡 提示：此工具為手持裝置優化版，您可將部署後的網址新增至手機主畫面，作為專屬 APP 使用！")
