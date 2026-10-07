#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
投顧行銷字卡自動產出工具 (Automated Marketing Card Generator)
開發者: 小恕 (投顧公司經理小幫手)
用途: 依照投顧行銷核心公式「踩痛點 -> 放焦慮/期待 -> 釋放誘因 -> 引導 Line@」
      每日自動生成 3 份高品質行銷字卡文案、圖像 Prompt 及 Line@ 口號。
"""

import json
import datetime
import random

class MarketingCardGenerator:
    def __init__(self):
        self.formula_steps = [
            "精準踩痛點",
            "放大焦慮或期待",
            "釋放超值誘因",
            "低門檻引導進 Line@"
        ]

    def generate_daily_cards(self, date_str=None, market_context=None):
        if not date_str:
            date_str = datetime.date.today().strftime("%Y-%m-%d")

        if not market_context:
            market_context = {
                "market_trend": "台股在高檔震盪洗盤，資金加速進行季度換手，散戶觀望猶豫",
                "focus_industries": ["AI 伺服器", "CPO 矽光子", "先進封裝/半導體", "被動元件"],
                "upcoming_event": "Q4 法人作帳與旺季卡位戰"
            }

        card1 = self._create_market_trend_card(market_context)
        card2 = self._create_industry_focus_card(market_context)
        card3 = self._create_promo_project_card(market_context)

        results = {
            "date": date_str,
            "market_context": market_context,
            "cards": [card1, card2, card3]
        }
        return results

    def _create_market_trend_card(self, ctx):
        return {
            "card_id": 1,
            "category": "股市行情與盤勢攻防",
            "theme_title": "洗盤即將結束！震盪拉回正是黃金卡位點",
            "card_design_1": {
                "headline": "洗盤來到尾聲！",
                "subheadline": "震盪拉回不是末日，而是「跌出超大價差」的最佳時機！"
            },
            "card_design_2": {
                "title": "【深V救援：破底翻 1+3 換股計畫】",
                "bullet_points": [
                    "一對一免費持股大健診，汰弱留強",
                    "把資金集中在法人悄悄卡位的主流強股",
                    "前 30 名留言者，享會籍延長至 Q4 起算"
                ]
            },
            "line_article_copy": (
                f"近期台股指數頻頻震盪，很多投資人在場外看著心慌，甚至不小心砍在最低點！\n"
                f"但你要知道，大盤洗盤洗得越乾淨，接下來的反彈力道就會越猛烈。\n"
                f"現在{ctx['market_trend']}，法人正在暗中汰弱換強。\n"
                f"如果你還抱著套牢弱勢股，只會眼睜睜看著別人賺大錢！\n"
                f"我們研究團隊已經透過產業基本面與籌碼面，鎖定被錯殺、準備迎來報復性反彈的波段好股。\n"
                f"別讓市場的恐慌蒙蔽了你的判斷，現在就是彎腰撿鑽石的時刻！"
            ),
            "image_design_prompt": (
                "商業視覺設計：金屬質感紅藍對比背景，畫面中央為代表強勢反彈的金黃色上升箭頭與破底翻V型光軌，"
                "周圍環繞科技感大數據籌碼粒子與金幣光芒。上方標示粗體大字「洗盤結束 破底翻」，下方有醒目的「留言【+1】」行動按鈕圖標。"
            ),
            "line_cta_slogan": {
                "slogan": "與其看著別人上車，不如現在跟我們一起鎖定低點！",
                "keyword": "【+1】",
                "action_prompt": "立即在 LINE@ 留言【+1】，免費領取《深V救援換股名單》並預約持股健診！"
            }
        }

    def _create_industry_focus_card(self, ctx):
        ind_str = " x ".join(ctx["focus_industries"][:2])
        return {
            "card_id": 2,
            "category": "產業時事與主流黑馬",
            "theme_title": "Q4 主流換手！新一波拉貨潮點名強股",
            "card_design_1": {
                "headline": f"【{ind_str}】雙主線狂飆！",
                "subheadline": "資金全面回流！誰是下一檔連拉 3 根漲停的黑馬？"
            },
            "card_design_2": {
                "title": "【Q4 法人點點名 雙路進攻案】",
                "bullet_points": [
                    "鎖定 3 檔營收爆發+籌碼乾淨黑馬股",
                    "獨家提供《AIx矽光子 產業評比分析表》",
                    "限時早鳥優惠：會籍買一送一，前50名免費升級VIP"
                ]
            },
            "line_article_copy": (
                f"電子旺季與 Q4 拉貨潮已經正式暖身！\n"
                f"目前資金正在往【{ctx['focus_industries'][0]}】與【{ctx['focus_industries'][1]}】集中。\n"
                f"族群輪動速度極快，每一個族群都有大賺頭，但前提是你要跟對節奏！\n"
                f"如果你總是等股價噴上去亮燈才想追，往往只能幫大戶洗碗。\n"
                f"我們的產業研究員已經親訪供應鏈，篩選出訂單能見度直接看到 2027 年的【奔月先鋒1號】！\n"
                f"型態完成、籌碼沉澱乾淨，點火訊號隨時亮起，錯過這波你絕對會後悔！"
            ),
            "image_design_prompt": (
                "商業視覺設計：高科技深藍與亮金色調，背景為晶片電路板與光纖數據流，"
                "中央擺放一個發光的神秘禮盒（標示蓋牌飆股 [XXX1]），旁邊伴隨飛速上升的柱狀圖與飆股火箭。"
                "字樣高亮顯示「Q4法人點點名 率先卡位」。"
            ),
            "line_cta_slogan": {
                "slogan": "提早卡位才是贏家，別等飆漲才來問能不能買！",
                "keyword": "【點名】",
                "action_prompt": "立即在 LINE@ 留言【點名】，第一時間解鎖 Q4 獨家黑馬股及產業評比表！"
            }
        }

    def _create_promo_project_card(self, ctx):
        return {
            "card_id": 3,
            "category": "節慶/專案促銷與低門檻導流",
            "theme_title": "Q4 旺季衝刺專案！買一送一限時驚喜折抵",
            "card_design_1": {
                "headline": "Q4大富翁 搶先出發！",
                "subheadline": "今年賺多少還沒定案，最後100天才是翻身關鍵！"
            },
            "card_design_2": {
                "title": "【100天衝刺 168 翻身計畫】",
                "bullet_points": [
                    "會籍直接從明年起算，等於 2026 剩餘時間全免費送！",
                    "憑虧損對帳單，直接折抵 8,888 元換股基金",
                    "限額 33 名，額滿立即關閉報名"
                ]
            },
            "line_article_copy": (
                f"眼看今年只剩下最後倒數，你年初許下的獲利目標實現了嗎？\n"
                f"上半年沒跟到行情不可怕，可怕的是 Q4 旺季作帳行情啟動，你還在原地猶豫！\n"
                f"為了帶大家在年底前把失血討回來，老師特別推出【100天衝刺 168 翻身計畫】！\n"
                f"這次我們不僅挺你分擔成本，更給足服務時間，會籍直接延後起算！\n"
                f"只要踏出簡單的一小步，就能讓你的資產向前邁進一大步。\n"
                f"機會不等人，名額有限，搶先登記鎖定優惠！"
            ),
            "image_design_prompt": (
                "商業視覺設計：歡慶與商業感兼具的紅金禮盒氛圍，畫面上方有「168 衝刺翻身」的大字金體，"
                "中央為開啟的金幣寶箱，噴發出%數漲幅標籤與加碼禮包圖示。整體風格熱烈且極具誘惑力，下方附上明確的「留言【168】」醒目框。"
            ),
            "line_cta_slogan": {
                "slogan": "給自己一次重新出發的機會，連本帶利討回你的利潤！",
                "keyword": "【168】",
                "action_prompt": "立即在 LINE@ 留言【168】，卡位【100天衝刺專案】限量超值名額！"
            }
        }

    def render_markdown(self, data):
        md = []
        md.append(f"# 每日行銷字卡產出報告 ({data['date']})\n")
        md.append(f"**負責人**：小恕 (投顧經理小幫手)")
        md.append(f"**今日市場背景**：{data['market_context']['market_trend']}")
        md.append(f"**焦點產業**：{', '.join(data['market_context']['focus_industries'])}\n")
        md.append("---")

        for card in data["cards"]:
            md.append(f"\n## 📌 行銷字卡 {card['card_id']}：{card['category']}")
            md.append(f"**主題**：{card['theme_title']}\n")
            
            md.append("### 1. 字卡畫面文案設計 (Image Card Content)")
            md.append("```text")
            md.append(f"【字卡 1 - 主視覺大標】")
            md.append(f"主標題：{card['card_design_1']['headline']}")
            md.append(f"副標題：{card['card_design_1']['subheadline']}\n")
            md.append(f"【字卡 2 - 專案與誘因】")
            md.append(f"專案名稱：{card['card_design_2']['title']}")
            for bp in card['card_design_2']['bullet_points']:
                md.append(f"  • {bp}")
            md.append("```\n")

            md.append("### 2. Line@ 長文參考 (Full Line Article)")
            md.append("```text")
            md.append(card['line_article_copy'])
            md.append("```\n")

            md.append("### 3. 圖像設計 Prompt 指南 (Visual Design Prompt)")
            md.append(f"> 🎨 **美编/AI產圖建議**：{card['image_design_prompt']}\n")

            md.append("### 4. Line@ 口號與導流關鍵字 (Line@ CTA & Keyword Slogan)")
            md.append(f"* **口號 (Slogan)**：{card['line_cta_slogan']['slogan']}")
            md.append(f"* **破冰關鍵字 (Keyword)**：`{card['line_cta_slogan']['keyword']}`")
            md.append(f"* **行動指示 (Action)**：{card['line_cta_slogan']['action_prompt']}\n")
            md.append("---")

        return "\n".join(md)

if __name__ == "__main__":
    generator = MarketingCardGenerator()
    data = generator.generate_daily_cards()
    md_content = generator.render_markdown(data)
    
    with open("/workspace/scratch/daily_marketing_cards.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print("Successfully generated daily marketing cards!")
