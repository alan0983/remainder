# -*- coding: big5 -*-

import discord
import asyncio
from datetime import datetime, timedelta

# 填入您的機器人 Token
TOKEN = 'MTE3NTM2NDMzNzczNzY3NDc5Mw.GGWszf.Uosqio3LmCIZWgFv_xiEwK9bk6ki8qxRxTPIXw'

# 設定您想要發送訊息的頻道 ID
CHANNEL_ID = 1082690668146737262  # 請更換為您的頻道 ID

# 設定每週固定時間發送訊息的時間（以星期幾的數字表示，0 代表星期一，1 代表星期二，以此類推）
# 例如，若要設定為星期三的下午 3 點，則 weekday = 2，hour = 15，minute = 0
weekday= 5  # 星期幾
hour = 18  # 時

# 建立 Discord 客戶端，傳遞 Intents 參數
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# 當機器人就緒時觸發的事件
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # 建立循環任務，用於定期發送訊息
    
    await remaind()

# 定義一個函式，用於每週定時發送掃地訊息
count = 0
async def remaind():
    global count  # 將 count 定義為全局變數
    while True:
        now = datetime.now()
        if now.weekday() == weekday:
            channel = client.get_channel(CHANNEL_ID)
            await channel.send('記得打掃客廳！')
            print(f'已發送打掃客廳訊息！')
            count = count +1
            await asyncio.sleep(1209600) # 兩周有 1209600 秒
            if(count%2==0):
                await channel.send('記得打掃廁所！')
                print(f'已發送打掃廁所訊息！')
                count =0
            
        else:
            print(f'sleep_sweep')
            await asyncio.sleep(86400)

# 啟動 Discord 客戶端
client.run(TOKEN)
