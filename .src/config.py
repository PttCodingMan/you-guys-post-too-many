import os

PTT1_ID = os.environ['PTT1_ID']
PTT1_PW = os.environ['PTT1_PW']

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
bearer_token = os.environ['bearer_token']

version = '0.1.0'

global_gen_web = True

board_rules = [
    # ('give', [(None, 3, 1)], True if global_gen_web else False, 'https://www.ptt.cc/bbs/give/M.1612495900.A.C32.html'),
    # ('Wanted', [(None, 3, 1)], True if global_gen_web else False,
    #  'https://www.ptt.cc/bbs/Wanted/M.1608829773.A.D3B.html'),
    ('HatePolitics', [(None, 5, 1)], True if global_gen_web else False,
     'https://www.ptt.cc/bbs/HatePolitics/M.1617115262.A.D60.html'),
    # ('Gossiping', [
    #     (None, 5, 1),
    #     ('[問卦]', 3, 1),
    #     ('[新聞]', 1, 1)
    # ], True if global_gen_web else False, 'https://www.ptt.cc/bbs/Gossiping/M.1637425085.A.07D.html'),
    # ('AllTogether', [(None, 1, 7)], True if global_gen_web else False,
    #  'https://www.ptt.cc/bbs/AllTogether/M.1643211430.A.5FB.html'),
    # ('Beauty', [(None, 3, 1)], True if global_gen_web else False,
    #  'https://www.ptt.cc/bbs/Beauty/M.1630069980.A.84B.html'),
    # ('Gamesale', [
    #     (None, 2, 1),
    #     ('[販售]', 1, 1),
    #     ('[徵求]', 1, 1),
    #     ('[交換]', 1, 1),
    #     ('[贈送]', 1, 1),
    # ], True if global_gen_web else False, 'https://www.ptt.cc/bbs/Gossiping/M.1637425085.A.07D.html')
]

post_template = '''---
title: =title=
tags:
=tags=
abbrlink: =link=
date: =date=
---
'''
