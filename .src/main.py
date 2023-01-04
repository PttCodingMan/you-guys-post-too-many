import json
import os.path
from datetime import date, timedelta

import PyPtt
import tweepy
from SingleLog import DefaultLogger as Logger, LogLevel

import config
import util


def login():
    ptt_bot = PyPtt.API()
    ptt_bot.login(
        config.PTT1_ID,
        config.PTT1_PW)
    logger.info('login', 'success')

    return ptt_bot


def detect_posts(from_days_ago: int = 1):
    ptt_bot = None

    for days_ago in range(1, from_days_ago + 1):

        twitter_content = None

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

                        logger.info('讀取資料', f'{board} 看板', days_ago + day - 1, '天前')

                        if ptt_bot is None:
                            ptt_bot = login()

                        start_index, end_index = util.get_post_index_range(
                            ptt_bot, board=board,
                            days_ago=days_ago + day - 1)
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
                            if title is None:
                                continue

                            delete_status = post.get('delete_status')
                            # ip = post.ip

                            # logger.info('data', author, title)

                            if delete_status == PyPtt.PostStatus.DELETED_BY_AUTHOR:
                                title = '(本文已被刪除) [' + author + ']'
                            elif delete_status == PyPtt.PostStatus.DELETED_BY_MODERATOR:
                                title = '(本文已被刪除) <' + author + '>'
                            elif delete_status == PyPtt.PostStatus.DELETED_BY_UNKNOWN:
                                title = '(本文已被刪除) <<' + author + '>>'
                            else:

                                logger.info('data', title, post)
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
                                    if title.startswith('(本文已被刪除)') or (
                                            key_word in title and not title.startswith('R:')):
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

                        if twitter_content is None:
                            twitter_content = f'{board} 板 違規 {prisoner_count} 人'
                        else:
                            twitter_content += f'\n{board} 板 違規 {prisoner_count} 人'

                        post = post.replace('=title=',
                                            f'{basic_day.strftime("%Y-%m-%d")}-{board} 違規 {prisoner_count} 人')
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

    exit(0)

    client = tweepy.Client(
        bearer_token=config.bearer_token,
        consumer_key=config.consumer_key, consumer_secret=config.consumer_secret,
        access_token=config.access_token, access_token_secret=config.access_token_secret)

    user_id = 1534551619077304321

    response = client.get_users_tweets(user_id, tweet_fields=['created_at'], max_results=20)

    exist = False
    check_date = basic_day.strftime("%Y-%m-%d")
    print(check_date)
    for tweet in response.data:
        # print(str(tweet.text))
        if check_date in str(tweet.created_at) and (
                '多 po 結果' in tweet.text.lower() or '超貼結果' in tweet.text.lower()):

            check_board = True
            for board, _, gen_web, _ in config.board_rules:
                if not gen_web:
                    continue
                if board not in tweet.text:
                    check_board = False
                    break
            if check_board:
                exist = True
                break

    if exist:
        logger.info('Twitter already post today')
    else:
        twitter_content = f"{basic_day.strftime('%Y.%m.%d')} 超貼結果\n\n{twitter_content}\n\n詳細名單請洽上方傳送門"

        response = client.create_tweet(
            text=twitter_content
        )
        logger.info('Twitter', 'post')


if __name__ == '__main__':
    logger = Logger('post', LogLevel.DEBUG)
    logger.info('Welcome to', 'PTT Post Too Many Monitor', config.version)

    # for day in range(1, 6):
    #     detect_posts(days_ago=day)

    for _ in range(3):
        try:
            detect_posts(10)
            break
        except Exception as e:
            raise e
            logger.info('Error', e)
            # Retry at 10 mins later if an error causes
            time.sleep(10 * 60)
        except KeyboardInterrupt:
            break
