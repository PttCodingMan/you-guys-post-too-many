import glob
import json
import os
from datetime import date, timedelta, datetime

import requests
from SingleLog.log import Logger

import PyPtt

logger = Logger('util')


def get_date(time_delta, ptt_style=True):
    pass_day = date.today() - timedelta(time_delta)

    pass_date = pass_day.strftime("%m/%d")

    if ptt_style and pass_date.startswith('0'):
        pass_date = pass_date[1:]

    return pass_date


def get_target(date0: str, date1: str):
    today = int(datetime.today().strftime('%m%d'))

    if int(date0) > today:
        date0 = '0' + date0
    else:
        date0 = '1' + date0

    if int(date1) > today:
        date1 = '0' + date1
    else:
        date1 = '1' + date1

    return int(date0 + date1)


history = {}


def get_first_index(ptt_bot: PyPtt.API, board, newest_index, day_ago, oldest_index=1):
    global history

    history_tag = f'{board}_{day_ago}'
    if history_tag in history:
        return history[history_tag]

    current_date_0 = get_date(
        day_ago + 1, ptt_style=False).replace('/', '').strip()
    current_date_1 = get_date(day_ago, ptt_style=False).replace('/', '').strip()
    finish_target = get_target(current_date_0, current_date_1)

    start_index = oldest_index
    end_index = newest_index

    current_index = int((start_index + end_index) / 2)
    last_index = current_index
    retry_index = 0

    while True:

        post_1 = ptt_bot.get_post(
            'ALLPOST',
            index=current_index,
            search_type=PyPtt.SearchType.KEYWORD,
            search_condition=f'({board})',
            query=True)

        if post_1.get('list_date') is None:
            current_index = start_index + retry_index
            retry_index += 1
            continue

        post_0 = None
        retry_index = 0
        for i in range(1, 40):

            if current_index - i <= 0:
                break

            post_0 = ptt_bot.get_post(
                board='ALLPOST',
                index=(current_index - i),
                search_type=PyPtt.SearchType.KEYWORD,
                search_condition=f'({board})',
                query=True)

            if post_0 is None:
                continue
            elif post_0.get('list_date') is None:
                continue

            break

        if post_0 is None:
            current_date_0 = '0000'
        else:
            current_date_0 = post_0.get('list_date').replace('/', '').strip()

        if len(current_date_0) < 4:
            current_date_0 = '0' + current_date_0
        current_date_1 = post_1.get('list_date').replace('/', '').strip()
        if len(current_date_1) < 4:
            current_date_1 = '0' + current_date_1
        current_target = get_target(current_date_0, current_date_1)

        logger.debug('get_first_index', finish_target, current_target, current_index)

        if current_target == finish_target:
            history[history_tag] = current_index
            return current_index

        if current_target > finish_target:
            end_index = current_index - 1
        elif current_target < finish_target:
            start_index = current_index + 1

        last_index = current_index
        current_index = int((start_index + end_index) / 2)

        if last_index == current_index:
            return current_index


def get_post_index_range(ptt_bot: PyPtt.API, board: str, days_ago: int = 1):
    newest_index = ptt_bot.get_newest_index(
        PyPtt.NewIndex.BOARD,
        board='ALLPOST',
        search_type=PyPtt.SearchType.KEYWORD,
        search_condition=f'({board})')

    logger.info('newest_index', newest_index)

    start_index = get_first_index(ptt_bot, board, newest_index, days_ago)
    end_index = get_first_index(ptt_bot, board, newest_index, days_ago - 1, oldest_index=start_index) - 1

    logger.info('index range', start_index, end_index)

    return start_index, end_index


def merge_dict(a: dict, b: dict):
    result = {}
    result.update(a)

    for key, values in b.items():
        if key in result:
            result[key].extend(values)
        else:
            result[key] = values

    return result


if __name__ == '__main__':
    for f in glob.glob('./data/*.json'):
        if '-05-' in f or '-04-' in f or '-03-' in f or '-02-' in f:
            os.remove(f)

