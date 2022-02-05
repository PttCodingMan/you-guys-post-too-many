from SingleLog.log import Logger

import PyPtt
import config
import util


def detect_posts():
    ptt_bot = PyPtt.API()

    ptt_bot.login(
        config.PTT1_ID,
        config.PTT1_PW,
        kick_other_login=True)
    logger.info('login', 'success')

    current_date = util.get_date(1)

    for board, max_post in config.boards:
        logger.info('啟動超貼偵測', board, f"最多 {max_post} 篇文章")

        authors = dict()

        start_index, end_index = util.get_post_index_range(ptt_bot, board=board)

        for index in range(start_index, end_index + 1):

            post = ptt_bot.get_post(
                board='ALLPOST',
                index=index,
                search_type=PyPtt.SearchType.KEYWORD,
                search_condition=f'({board})',
                query=True)

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
                if title.startswith('R:'):
                    mark = ' □ '

                if result is None:
                    result = f'{current_date}{mark}{suspect} {title}'
                else:
                    result += f'\n{current_date}{mark}{suspect} {title}'

        print(result)

    ptt_bot.logout()

    logger.info('超貼偵測', '結束')


if __name__ == '__main__':
    logger = Logger('post')
    logger.info('Welcome to', 'PTT Post Too Many Monitor', config.version)

    detect_posts()
