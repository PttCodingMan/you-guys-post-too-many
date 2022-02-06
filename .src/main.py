import json
from datetime import date

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


def detect_posts():

    ptt_bot = login()

    current_date = util.get_date(1)

    today = date.today()

    for board, max_post in config.boards:
        logger.info('啟動超貼偵測', board, f"最多 {max_post} 篇文章")

        authors = dict()

        start_index, end_index = util.get_post_index_range(ptt_bot, board=board)

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

            if delete_status == PyPtt.PostDelStatus.deleted_by_author:
                title = '(本文已被刪除) [' + author + ']'
            elif delete_status == PyPtt.PostDelStatus.deleted_by_moderator:
                title = '(本文已被刪除) <' + author + '>'
            elif delete_status == PyPtt.PostDelStatus.deleted_by_unknown:
                # title = '(本文已被刪除) <' + author + '>'
                pass
            else:
                title = title[:title.rfind(' ')].strip()

            if title is None:
                title = ''

            if '[公告]' in title:
                continue

            logger.info('data', author, title)

            if author not in authors:
                authors[author] = []
            authors[author].append(title)

        logger.debug('authors', authors)

        result = None
        for suspect, titles in authors.items():

            logger.debug('->', suspect, titles)

            if len(titles) <= max_post:
                continue

            if result is not None:
                result += '\n'

            for title in titles:
                mark = ' '
                if not title.startswith('R:'):
                    mark = ' □ '

                if result is None:
                    result = f'{current_date} {suspect}{mark}{title}'
                else:
                    result += f'\n{current_date} {suspect}{mark}{title}'

        # print(result)

        with open(f'./source/_posts/{board}-{today.strftime("%Y-%m-%d")}.md', 'w') as f:
            post = config.post_template

            post = post.replace('=title=', f'{board}-{today.strftime("%Y-%m-%d")}')
            post = post.replace('=tags=', f'    - {board}')
            post = post.replace('=link=', f'{board}-{today.strftime("%Y-%m-%d")}')
            post = post.replace('=date=', f'{board}-{today.strftime("%Y-%m-%d %I:%M:%S")}')

            f.write(post)

            if result is None:
                f.write('昨日沒有違規')
            else:
                f.write(f'{board} 板規，每日不能超過 {max_post} 篇\n')
                f.write('<!-- more -->\n')
                f.write('昨日違規清單\n')
                f.write(result)
            # json.dump(authors, f, indent=4, ensure_ascii=False)

    ptt_bot.logout()

    logger.info('超貼偵測', '結束')


if __name__ == '__main__':
    logger = Logger('post')
    logger.info('Welcome to', 'PTT Post Too Many Monitor', config.version)

    detect_posts()
