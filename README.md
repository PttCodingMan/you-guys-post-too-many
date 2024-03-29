# 批踢踢超貼觀測站

This project is intended to help the hard-working PTT moderators to reduce loading.  
This project finds people who have posted too many posts in the past day, even if they delete them.  
  
Publish on this site: https://codingman.cc/you-guys-post-too-many/  
Also publish on Twitter: https://twitter.com/ptt_post_many

## The reason for this project
[PyPtt - 批踢踢超貼觀測站兩三事](https://codingman.cc/pyptt-about-ptt-you-guys-post-too-many/)

## Config

The following config is an actual config.

```python
board_rules = [
    ('Gossiping', [
        (None, 5, 1),
        ('[問卦]', 2, 1),
        ('[新聞]', 1, 1)
    ], True, 'https://www.ptt.cc/bbs/Gossiping/M.1637425085.A.07D.html'),
    ...
]
```

In that case
- `Gossiping` means the name of board.
- `('[問卦]', 2, 1)` means there can only be `2` posts in `1` day with `[問卦]` keywords.
  - `None` means no key word.
- `True` means generate web or not.
- `https://www.ptt.cc/bbs/Gossiping/M.1637425085.A.07D.html` means the rule of the board.

We can check the full config at [https://github.com/PttCodingMan/you-guys-post-too-many/blob/master/.src/config.py](https://github.com/PttCodingMan/you-guys-post-too-many/blob/master/.src/config.py).

## License
Apache License 2.0
