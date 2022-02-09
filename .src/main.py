import json
import os.path
from datetime import date, timedelta

from SingleLog.log import Logger

import PyPtt
import config
import util


def login():
    ptt_bot = PyPtt.API()
    ptt_bot.login(
        config.PTT1_ID,
        config.PTT1_PW)
    logger.info('login', 'success')

    return ptt_bot


def detect_posts(days_ago: int = 1):
    ptt_bot = None

    basic_day = date.today() - timedelta(days_ago - 1)

    authors_day_1 = None
    for board, rule_list, gen_web, rule_url in config.board_rules:
        logger.info('啟動超貼偵測', board)

        for key_word, max_post, day_range in rule_list:

            authors = {}
            for day in range(1, day_range + 1):
                # print('load', day)
                current_day = basic_day - timedelta(day)

                temp_file = f'./.src/data/{board}-{current_day.strftime("%Y-%m-%d")}.json'
                if os.path.exists(temp_file):
                    with open(temp_file, 'r') as f:
                        current_authors = json.load(f)

                    authors = util.merge_dict(authors, current_authors)
                else:
                    if days_ago + day - 1 > 5:
                        break

                    if ptt_bot is None:
                        ptt_bot = login()

                    start_index, end_index = util.get_post_index_range(ptt_bot, board=board, days_ago=days_ago + day - 1)
                    current_authors = {}
                    for index in range(start_index, end_index + 1):

                        for _ in range(3):
                            try:
                                post = ptt_bot.get_post(
                                    board='ALLPOST',
                                    index=index,
                                    search_type=PyPtt.SearchType.KEYWORD,
                                    search_condition=f'({board})',
                                    query=True)
                                break
                            except PyPtt.ConnectionClosed:
                                ptt_bot = login()

                        author = post.get('author')
                        if '(' in author:
                            author = author[:author.find('(')].strip()

                        title = post.get('title')
                        delete_status = post.get('delete_status')
                        # ip = post.ip

                        # logger.info('data', author, title)

                        if delete_status == PyPtt.PostDelStatus.deleted_by_author:
                            title = '(本文已被刪除) [' + author + ']'
                        elif delete_status == PyPtt.PostDelStatus.deleted_by_moderator:
                            title = '(本文已被刪除) <' + author + '>'
                        elif delete_status == PyPtt.PostDelStatus.deleted_by_unknown:
                            title = '(本文已被刪除) <<' + author + '>>'
                            pass
                        else:
                            title = title[:title.rfind('(')].strip()

                        if '[公告]' in title:
                            continue

                        # logger.info('data', author, title)
                        # logger.info('post', post.get('list_date'))

                        if author not in current_authors:
                            current_authors[author] = []
                        current_authors[author].append([post.get('list_date'), title])

                    with open(temp_file, 'w') as f:
                        json.dump(current_authors, f, indent=4, ensure_ascii=False)

                    authors = util.merge_dict(authors, current_authors)

                if day == 1:
                    authors_day_1 = current_authors

        logger.debug('authors', authors)

        result = None
        prisoner_count = 0
        last_key_word = None
        for key_word, max_post, day_range in rule_list:

            day_mark = '單日' if day_range == 1 else f'{day_range} 日內'

            for suspect, titles in authors.items():

                # logger.info('->', suspect, titles)

                if key_word is None:

                    if len(titles) <= max_post:
                        continue
                    if suspect not in authors_day_1:
                        continue

                    prisoner_count += 1

                    if result is not None:
                        result += '\n'

                    if last_key_word is None:
                        last_key_word = ''
                        if result is not None:
                            result += f'\n{day_mark}不得超過 {max_post} 篇\n'
                        else:
                            result = f'{day_mark}不得超過 {max_post} 篇\n'

                    for list_date, title in titles:
                        mark = ' '
                        if not title.startswith('R:'):
                            mark = ' □ '

                        if result is None:
                            result = f'{list_date} {suspect}{mark}{title}'
                        else:
                            result += f'\n{list_date} {suspect}{mark}{title}'

                else:
                    if key_word == '[問卦]':
                        compliant_titles = []

                        for list_date, title in titles:
                            if title.startswith('(本文已被刪除)') or (key_word in title and not title.startswith('R:')):
                                compliant_titles.append(
                                    [list_date, title])
                    else:
                        compliant_titles = []

                        for list_date, title in titles:
                            if key_word in title and not title.startswith('R:'):
                                compliant_titles.append(
                                    [list_date, title])

                    if len(compliant_titles) <= max_post:
                        continue
                    if suspect not in authors_day_1:
                        continue
                    prisoner_count += 1

                    if result is not None:
                        result += '\n'

                    if last_key_word != key_word:
                        last_key_word = key_word
                        if result is not None:
                            result += f'\n{day_mark} {key_word} 不得超過 {max_post} 篇\n'
                        else:
                            result = f'{day_mark} {key_word} 不得超過 {max_post} 篇\n'

                    for list_date, title in compliant_titles:
                        mark = ' '
                        if not title.startswith('R:'):
                            mark = ' □ '

                        if result is None:
                            result = f'{list_date} {suspect}{mark}{title}'
                        else:
                            result += f'\n{list_date} {suspect}{mark}{title}'

        # print(result)

        if gen_web:
            with open(f'./source/_posts/{board}-{basic_day.strftime("%Y-%m-%d")}.md', 'w') as f:
                post = config.post_template

                post = post.replace('=title=', f'{basic_day.strftime("%Y-%m-%d")}-{board} 違規 {prisoner_count} 人')
                post = post.replace('=tags=', f'    - {board}')
                post = post.replace('=link=', f'{basic_day.strftime("%Y-%m-%d")}-{board}')
                post = post.replace('=date=', f'{board}-{basic_day.strftime("%Y-%m-%d %I:%M:%S")}')

                f.write(post)

                f.write(f'{board} 板 [板規連結]({rule_url})\n')
                f.write(f'昨天違規 {prisoner_count} 人\n')
                if result is None:
                    pass
                    # f.write('昨天沒有違規')
                else:
                    f.write('<!-- more -->\n\n')
                    f.write('違規清單\n')
                    f.write(result)
            # json.dump(authors, f, indent=4, ensure_ascii=False)

    if ptt_bot is not None:
        ptt_bot.logout()

    logger.info('超貼偵測', '結束')


if __name__ == '__main__':
    logger = Logger('post')
    logger.info('Welcome to', 'PTT Post Too Many Monitor', config.version)

    # for day in range(1, 8):
    #     detect_posts(days_ago=day)

    detect_posts(1)
