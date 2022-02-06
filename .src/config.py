import os

PTT1_ID = os.environ['PTT1_ID']
PTT1_PW = os.environ['PTT1_PW']

version = '0.0.1'

boards = [
    ('Wanted', 3),
    ('HatePolitics', 5),
    ('give', 3),
]

post_template = '''---
title: =title=
tags:
=tags=
abbrlink: =link=
date: =date=
---
'''