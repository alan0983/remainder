# -*- coding: big5 -*-

import discord
import asyncio
from datetime import datetime, timedelta

# ��J�z�������H Token
TOKEN = 'MTE3NTM2NDMzNzczNzY3NDc5Mw.GGWszf.Uosqio3LmCIZWgFv_xiEwK9bk6ki8qxRxTPIXw'

# �]�w�z�Q�n�o�e�T�����W�D ID
CHANNEL_ID = 1082690668146737262  # �Ч󴫬��z���W�D ID

# �]�w�C�g�T�w�ɶ��o�e�T�����ɶ��]�H�P���X���Ʀr��ܡA0 �N��P���@�A1 �N��P���G�A�H�������^
# �Ҧp�A�Y�n�]�w���P���T���U�� 3 �I�A�h weekday = 2�Ahour = 15�Aminute = 0
weekday= 5  # �P���X
hour = 18  # ��

# �إ� Discord �Ȥ�ݡA�ǻ� Intents �Ѽ�
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# ������H�N����Ĳ�o���ƥ�
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # �إߴ`�����ȡA�Ω�w���o�e�T��
    
    await remaind()

# �w�q�@�Ө禡�A�Ω�C�g�w�ɵo�e���a�T��
count = 0
async def remaind():
    global count  # �N count �w�q�������ܼ�
    while True:
        now = datetime.now()
        if now.weekday() == weekday:
            channel = client.get_channel(CHANNEL_ID)
            await channel.send('�O�o�������U�I')
            print(f'�w�o�e�������U�T���I')
            count = count +1
            await asyncio.sleep(1209600) # ��P�� 1209600 ��
            if(count%2==0):
                await channel.send('�O�o�����Z�ҡI')
                print(f'�w�o�e�����Z�ҰT���I')
                count =0
            
        else:
            print(f'sleep_sweep')
            await asyncio.sleep(86400)

# �Ұ� Discord �Ȥ��
client.run(TOKEN)
