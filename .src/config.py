import os

PTT1_ID = os.environ['PTT1_ID']
PTT1_PW = os.environ['PTT1_PW']

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
bearer_token = os.environ['bearer_token']


version = '0.0.3'

board_rules = [
    ('give', [(None, 3, 1)], True, 'https://www.ptt.cc/bbs/give/M.1612495900.A.C32.html'),
    ('Wanted', [(None, 3, 1)], True, 'https://www.ptt.cc/bbs/Wanted/M.1608829773.A.D3B.html'),
    ('HatePolitics', [(None, 5, 1)], True, 'https://www.ptt.cc/bbs/HatePolitics/M.1617115262.A.D60.html'),
    ('Gossiping', [
        (None, 5, 1),
        ('[問卦]', 2, 1),
        ('[新聞]', 1, 1)
    ], True, 'https://www.ptt.cc/bbs/Gossiping/M.1637425085.A.07D.html'),
    ('AllTogether', [(None, 1, 7)], True, 'https://www.ptt.cc/bbs/AllTogether/M.1643211430.A.5FB.html'),
    ('Beauty', [(None, 3, 1)], True, 'https://www.ptt.cc/bbs/Beauty/M.1630069980.A.84B.html'),
    ('nCoV2019', [(None, 4, 1)], False, 'https://www.ptt.cc/bbs/nCoV2019/M.1584500627.A.886.html'),
    # ('NBA', [
    #     ('[討論]', 1, 1),
    #     ('[專欄]', 1, 1),
    #     ('[情報]', 1, 1),
    #     ('[新聞]', 1, 1),
    #     ('[花邊]', 1, 1),
    # ], False, 'https://www.ptt.cc/bbs/NBA/M.1637555315.A.C34.html'),
    ('Lifeismoney', [(None, 15, 30)], False, 'https://www.ptt.cc/bbs/Lifeismoney/M.1629830908.A.94F.html'),
    ('Hsinchu', [
        ('[新聞]', 3, 7),
        ('[合購]', 1, 7),
        ('[廣宣]', 1, 30),
        ('[代買]', 1, 30),
        ('模特', 1, 30),
        ('共乘', 2, 7),
    ], False, 'https://www.ptt.cc/bbs/Hsinchu/M.1572354348.A.E2D.html'),
]

post_template = '''---
title: =title=
tags:
=tags=
abbrlink: =link=
date: =date=
---
'''
