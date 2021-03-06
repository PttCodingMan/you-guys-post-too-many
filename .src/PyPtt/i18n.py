from enum import auto

from . import lib_util


class Lang(lib_util.AutoName):
    CHINESE = auto()
    ENGLISH = auto()


languageList = [
    Lang.CHINESE,
    Lang.ENGLISH,
]


def specific_load(input_language, lang_list):
    global languageList

    if len(languageList) != len(lang_list):
        raise ValueError('SpecificLoad LangList length error')

    if input_language not in languageList:
        raise ValueError('SpecificLoad unknown language', input_language)
    return lang_list[languageList.index(input_language)]


def replace(string, *args):
    # for i in range(len(args)):
    for i, _ in enumerate(args):
        target = str(args[i])
        string = string.replace('{Target' + str(i) + '}', target)
    return string


chinese_traditional_module = None
english_module = None
init = None
connect_host = None
set_connect_host = None
PTT = None
PTT2 = None
localhost = None
must_be_a_string = None
must_be_a_integer = None
must_be_a_boolean = None
unknown = None
must_bigger_than = None
must_small_than = None
must_between = None
connect_core = None
use_too_many_resources = None
prepare_connect_again = None
active = None
connect_mode = None
connect_mode_TELNET = None
connect_mode_WEBSOCKET = None
set_connect_mode = None
fail = None
connect = None
hide_sensitive_info = None
send_msg = None
ptt_msg = None
spend_time = None
kick_other_login = None
not_kick_other_login = None
login_id = None
mail_box = None
login_success = None
go_main_menu = None
wrong_id_pw = None
login_too_often = None
system_busy_try_later = None
del_wrong_pw_record = None
post_not_finish = None
in_login_process_please_wait = None
any_key_continue = None
update_sync_online_user_friend_list = None
error_login_rich_people_go_main_menu = None
skip_registration_form = None
only_secure_connection = None
debug = None
info = None
out_side = None
new_cursor = None
old_cursor = None
logout_success = None
logout = None
complete = None
query_ptt_time_success = None
has_new_mail_goto_main_menu = None
mail_box_full = None
use_mailbox_api_will_logout_after_execution = None
unregistered_user_cant_use_all_api = None
picks_in_register = None
reading_board_info = None
no_permission = None
no_post = None
set_connect_mail_first = None
no_such_board = None
no_mail = None
find_newest_index = None
catch_post = None
catch_post_success = None
query_post_success = None
success = None
post_deleted = None
board = None
substandard_post = None
author = None
title = None
date = None
content = None
comment_id = None
comment_date = None
comment = None
comment_content = None
unconfirmed_post = None
browse_post = None
done = None
browse_post_done = None
post_no_content = None
animation_post = None
login_fail = None
no_fast_comment = None
no_such_user = None
user_offline = None
no_money = None
money_too_few = None
connection_closed = None
unregistered_user_cant_use_this_api = None
multi_thread_operate = None
error_pw = None
ptt2_not_support = None
no_comment = None
no_response = None
need_moderator_permission = None
connect_fail = None
no_such_post = None
screen_no_match_target = None
can_not_use_search_post_code_f = None
user_has_previously_been_banned = None
no_search_result = None
timeout = None
deleted_post = None
has_post_permission = None
save_file = None
select_signature = None
not_record_ip = None
record_ip = None
push_aligned = None
not_push_aligned = None
has_push_permission = None
only_arrow = None
error_parameter = None
wait_for_no_fast_comment = None
require_login = None
reading = None
quit_user_profile = None
read_complete = None
get_user = None
get_user_success = None
get_user_fail = None
water_ball = None
set_call_status = None
throw_waterball = None
throw_waterball_success = None
no_waterball = None
browse_waterball = None
browse_waterball_done = None
get_call_status = None
get_call_status_success = None
set_call_status_success = None
transaction_cancelled = None
transaction = None
transaction_success = None
constant_red_bag = None
verify_id = None
anonymous_transaction = None
input_money = None
input_id = None
authentication_has_not_expired = None
trading_in_progress = None
send_mail = None
no_signature_file = None
select_sign_file = None
not_self_save_draft = None
self_save_draft = None
board_list = None
reply_board = None
reply_mail = None
reply_board_mail = None
forced_write = None
edit_post = None
use_the_original_title = None
quote_original = None
respond_success = None
favourite_board_list = None
confirm = None
input_origin_password = None
input_new_password = None
check_new_password = None
catch_bottom_post_success = None
confirm_delete = None
delete_success = None
bucket_fail = None
bucket_success = None
input_bucket_days_reason = None
new_settings_have_been_saved = None
no_changes = None
restore_connection = None
new_version = None
development_version = None
latest_version = None


def load(lang):
    if not isinstance(lang, Lang):
        raise ValueError('Unknown language', lang)

    global latest_version
    latest_version = specific_load(lang, [
        '?????????????????????',
        'Running the latest version',
    ])

    global development_version
    development_version = specific_load(lang, [
        '????????????????????????',
        'Running development version',
    ])

    global new_version
    new_version = specific_load(lang, [
        '????????????',
        'There is a new version',
    ])

    global restore_connection
    restore_connection = specific_load(lang, [
        '????????????',
        'restore Connection',
    ])

    global no_changes
    no_changes = specific_load(lang, [
        '?????????????????????',
        'no changes have been made to any settings',
    ])

    global new_settings_have_been_saved
    new_settings_have_been_saved = specific_load(lang, [
        '??????????????????',
        'new settings have been saved',
    ])

    global input_bucket_days_reason
    input_bucket_days_reason = specific_load(lang, [
        '???????????????????????????',
        'input bucket days and reason',
    ])

    global bucket_success
    bucket_success = specific_load(lang, [
        '????????????',
        'bucket success',
    ])

    global bucket_fail
    bucket_fail = specific_load(lang, [
        '????????????',
        'bucket fail',
    ])

    global confirm_delete
    confirm_delete = specific_load(lang, [
        '????????????',
        'confirm delete',
    ])

    global delete_success
    delete_success = specific_load(lang, [
        '????????????',
        'delete Success',
    ])

    global catch_bottom_post_success
    catch_bottom_post_success = specific_load(lang, [
        '????????????????????????',
        'catch bottom post success',
    ])

    global catch_post_success
    catch_post_success = specific_load(lang, [
        '??????????????????',
        'get post success',
    ])

    global query_post_success
    query_post_success = specific_load(lang, [
        '??????????????????',
        'query post success',
    ])

    global input_origin_password
    input_origin_password = specific_load(lang, [
        '???????????????',
        'input Origin Password',
    ])

    global input_new_password
    input_new_password = specific_load(lang, [
        '???????????????',
        'input new password',
    ])

    global check_new_password
    check_new_password = specific_load(lang, [
        '???????????????',
        'check new password',
    ])

    global confirm
    confirm = specific_load(lang, [
        '??????',
        'confirm',
    ])

    global favourite_board_list
    favourite_board_list = specific_load(lang, [
        '????????????',
        'favourite board list',
    ])

    global respond_success
    respond_success = specific_load(lang, [
        '????????????',
        'respond success',
    ])

    global use_the_original_title
    use_the_original_title = specific_load(lang, [
        '???????????????',
        'use the original title',
    ])

    global quote_original
    quote_original = specific_load(lang, [
        '????????????',
        'quote original',
    ])

    global edit_post
    edit_post = specific_load(lang, [
        '????????????',
        'edit post',
    ])

    global forced_write
    forced_write = specific_load(lang, [
        '????????????',
        'Forced Write',
    ])

    global reply_board
    reply_board = specific_load(lang, [
        '???????????????',
        'respond to the Board',
    ])

    global reply_mail
    reply_mail = specific_load(lang, [
        '?????????????????????',
        'respond to the mailbox of author',
    ])

    global reply_board_mail
    reply_board_mail = specific_load(lang, [
        '??????????????????????????????',
        'respond to the board and the mailbox of author',
    ])

    global board_list
    board_list = specific_load(lang, [
        '????????????',
        'board list',
    ])

    global self_save_draft
    self_save_draft = specific_load(lang, [
        '????????????',
        'self-save draft',
    ])

    global not_self_save_draft
    not_self_save_draft = specific_load(lang, [
        '??????????????????',
        'not self-save draft',
    ])

    global select_sign_file
    select_sign_file = specific_load(lang, [
        '????????? {Target0} ?????????',
        'select {Target0}th signature file',
    ])

    global no_signature_file
    no_signature_file = specific_load(lang, [
        '???????????????',
        'no Signature File',
    ])

    global send_mail
    send_mail = specific_load(lang, [
        '??????',
        'send mail',
    ])

    global trading_in_progress
    trading_in_progress = specific_load(lang, [
        '?????????????????????',
        'trading is in progress',
    ])

    global authentication_has_not_expired
    authentication_has_not_expired = specific_load(lang, [
        '??????????????????',
        'authentication has not expired',
    ])

    global input_id
    input_id = specific_load(lang, [
        '????????????',
        'input ID',
    ])

    global input_money
    input_money = specific_load(lang, [
        '????????????',
        'input money',
    ])

    global anonymous_transaction
    anonymous_transaction = specific_load(lang, [
        '?????????????????????',
        'transaction without anomalous',
    ])

    global verify_id
    verify_id = specific_load(lang, [
        '????????????',
        'verify ID',
    ])

    global constant_red_bag
    constant_red_bag = specific_load(lang, [
        '??????????????????',
        'constant the red bag',
    ])

    global transaction_success
    transaction_success = specific_load(lang, [
        '????????????',
        'transaction success',
    ])

    global transaction
    transaction = specific_load(lang, [
        '??????',
        'transaction',
    ])

    global transaction_cancelled
    transaction_cancelled = specific_load(lang, [
        '????????????!',
        'the transaction is cancelled!',
    ])

    global set_call_status_success
    set_call_status_success = specific_load(lang, [
        '???????????????????????????',
        'set BBCall status success',
    ])

    global get_call_status
    get_call_status = specific_load(lang, [
        '?????????????????????',
        'get BBCall status',
    ])

    global get_call_status_success
    get_call_status_success = specific_load(lang, [
        '???????????????????????????',
        'get BBCall status success',
    ])

    global browse_waterball
    browse_waterball = specific_load(lang, [
        '??????????????????',
        'browse waterball',
    ])

    global browse_waterball_done
    browse_waterball_done = specific_load(lang, [
        '????????????????????????',
        'browse waterball complete',
    ])

    global no_waterball
    no_waterball = specific_load(lang, [
        '???????????????',
        'no waterball',
    ])

    global throw_waterball_success
    throw_waterball_success = specific_load(lang, [
        '???????????????',
        'throw waterball success',
    ])

    global throw_waterball
    throw_waterball = specific_load(lang, [
        '??? {Target0} ??????',
        'throw {Target0} waterball',
    ])

    global set_call_status
    set_call_status = specific_load(lang, [
        '?????????????????????',
        'set call status',
    ])

    global water_ball
    water_ball = specific_load(lang, [
        '??????',
        'water Ball',
    ])

    global get_user
    get_user = specific_load(lang, [
        '???????????????',
        'get user',
    ])

    global get_user_success
    get_user_success = specific_load(lang, [
        '?????????????????????',
        'get user success',
    ])

    global get_user_fail
    get_user_fail = specific_load(lang, [
        '?????????????????????',
        'get user fail',
    ])

    global read_complete
    read_complete = specific_load(lang, [
        f'????????????',
        f'read complete',
    ])

    global quit_user_profile
    quit_user_profile = specific_load(lang, [
        f'?????????????????????',
        f'Quit User Profile',
    ])

    global reading
    reading = specific_load(lang, [
        '?????????',
        'reading',
    ])

    global require_login
    require_login = specific_load(lang, [
        '????????????',
        'please login first',
    ])

    global error_parameter
    error_parameter = specific_load(lang, [
        '????????????',
        'wrong parameter',
    ])

    global only_arrow
    only_arrow = specific_load(lang, [
        '??????????????????',
        'Arrow Only in Push',
    ])

    global has_push_permission
    has_push_permission = specific_load(lang, [
        '???????????????????????????',
        'user has comment permission',
    ])

    global push_aligned
    push_aligned = specific_load(lang, [
        '????????????',
        'Push aligned',
    ])

    global not_push_aligned
    not_push_aligned = specific_load(lang, [
        '???????????????',
        'No push aligned',
    ])

    global not_record_ip
    not_record_ip = specific_load(lang, [
        '????????? IP',
        'not record IP',
    ])

    global record_ip
    record_ip = specific_load(lang, [
        '?????? IP',
        'Record ip',
    ])

    global select_signature
    select_signature = specific_load(lang, [
        '???????????????',
        'Select Signature',
    ])

    global save_file
    save_file = specific_load(lang, [
        '????????????',
        'Save File',
    ])

    global has_post_permission
    has_post_permission = specific_load(lang, [
        '???????????????????????????',
        'User Has Post Permission',
    ])

    global deleted_post
    deleted_post = specific_load(lang, [
        '???????????????',
        'Deleted Post',
    ])

    global timeout
    timeout = specific_load(lang, [
        '????????????',
        'timeout',
    ])

    global no_search_result
    no_search_result = specific_load(lang, [
        '??????????????????',
        'No Search Result',
    ])

    global user_has_previously_been_banned
    user_has_previously_been_banned = specific_load(lang, [
        '???????????????????????????',
        'user has previously been banned',
    ])

    global can_not_use_search_post_code_f
    can_not_use_search_post_code_f = specific_load(lang, [
        '??????????????????????????????????????????(AID)??????',
        'This status can not use the search Post code function',
    ])

    global screen_no_match_target
    screen_no_match_target = specific_load(lang, [
        '??????????????????',
        'this screen is not recognized',
    ])

    global no_such_post
    no_such_post = specific_load(lang, [
        '{Target0} ?????????????????????????????? {Target1}',
        'in {Target0}, the post code is not exist {Target1}',
    ])

    global connect_fail
    connect_fail = specific_load(lang, [
        '????????????',
        'connect fail',
    ])

    global need_moderator_permission
    need_moderator_permission = specific_load(lang, [
        '??????????????????',
        'need moderator permission',
    ])

    global no_response
    no_response = specific_load(lang, [
        '?????????, ???????????????????????????, ????????????',
        'this post has been closed and marked, no response',
    ])

    global no_comment
    no_comment = specific_load(lang, [
        '????????????',
        'no comment',
    ])

    global error_pw
    error_pw = specific_load(lang, [
        '???????????????',
        'wrong password',
    ])

    global multi_thread_operate
    multi_thread_operate = specific_load(lang, [
        '??????????????????????????????????????? PyPtt ??????',
        'do not use a multi-thread to operate a PyPtt object',
    ])

    global unregistered_user_cant_use_this_api
    unregistered_user_cant_use_this_api = specific_load(lang, [
        '??????????????????????????????????????????',
        'unregistered User Can\'t Use This API',
    ])

    global connection_closed
    connection_closed = specific_load(lang, [
        '?????????????????????',
        'connection Closed',
    ])

    global money_too_few
    money_too_few = specific_load(lang, [
        '???????????????????????????!',
        'the amount is too small, the transaction is cancelled!',
    ])

    global no_money
    no_money = specific_load(lang, [
        'PTT ?????????',
        'not enough PTT coins',
    ])

    global user_offline
    user_offline = specific_load(lang, [
        '???????????????',
        'user offline',
    ])

    global no_such_user
    no_such_user = specific_load(lang, [
        '???????????????',
        'no such user',
    ])

    global no_fast_comment
    no_fast_comment = specific_load(lang, [
        '????????????????????????',
        'no fast comment',
    ])

    global wait_for_no_fast_comment
    wait_for_no_fast_comment = specific_load(lang, [
        f'???{no_fast_comment}?????????????????????',
        f'because {no_fast_comment}, wait 5 sec',
    ])

    global login_fail
    login_fail = specific_load(lang, [
        '????????????',
        'login fail'
    ])

    global animation_post
    animation_post = specific_load(lang, [
        '????????????',
        'Animation Post',
    ])

    global post_no_content
    post_no_content = specific_load(lang, [
        '??????????????????',
        'post has no content',
    ])

    global done
    done = specific_load(lang, [
        '??????',
        'done',
    ])

    global browse_post
    browse_post = specific_load(lang, [
        '????????????',
        'browse post',
    ])

    global browse_post_done
    browse_post_done = specific_load(lang, [
        f'{browse_post}{done}',
        f'{browse_post} {done}',
    ])

    global unconfirmed_post
    unconfirmed_post = specific_load(lang, [
        '???????????????',
        'Post To Be Confirmed',
    ])

    global comment
    comment = specific_load(lang, [
        '??????',
        'comment',
    ])

    global comment_date
    comment_date = specific_load(lang, [
        '????????????',
        'comment date',
    ])

    global comment_id
    comment_id = specific_load(lang, [
        '????????????',
        'comment id',
    ])

    global content
    content = specific_load(lang, [
        '??????',
        'content',
    ])

    global comment_content
    comment_content = specific_load(lang, [
        f'{comment}{content}',
        f'{comment} {content}',
    ])

    global date
    date = specific_load(lang, [
        '??????',
        'date',
    ])

    global title
    title = specific_load(lang, [
        '??????',
        'title',
    ])

    global author
    author = specific_load(lang, [
        '??????',
        'author',
    ])

    global substandard_post
    substandard_post = specific_load(lang, [
        '??????????????????',
        'substandard post',
    ])

    global board
    board = specific_load(lang, [
        '??????',
        'board',
    ])

    global post_deleted
    post_deleted = specific_load(lang, [
        '?????????????????????',
        'post has been deleted',
    ])

    global success
    success = specific_load(lang, [
        '??????',
        'success',
    ])

    global catch_post
    catch_post = specific_load(lang, [
        '????????????',
        'catch post',
    ])

    global find_newest_index
    find_newest_index = specific_load(lang, [
        '??????????????????',
        'find newest index',
    ])

    global no_mail
    no_mail = specific_load(lang, [
        f'????????????',
        f'you have no mail',
    ])

    global no_such_board
    no_such_board = specific_load(lang, [
        '????????????',
        'no such board',
    ])

    global no_post
    no_post = specific_load(lang, [
        '????????????',
        'no post',
    ])

    global set_connect_mail_first
    set_connect_mail_first = specific_load(lang, [
        '???????????????????????????????????????',
        'password can only be changed after setting the contact mailbox',
    ])

    global no_permission
    no_permission = specific_load(lang, [
        '?????????????????????',
        'user Has No Permission',
    ])

    global reading_board_info
    reading_board_info = specific_load(lang, [
        '??????????????????',
        'reading board Info',
    ])

    global picks_in_register
    picks_in_register = specific_load(lang, [
        '???????????????????????????',
        'registration application processing order',
    ])

    global unregistered_user_cant_use_all_api
    unregistered_user_cant_use_all_api = specific_load(lang, [
        '????????????????????????????????????????????????',
        'unregistered User Can\'t Use All API',
    ])

    global use_mailbox_api_will_logout_after_execution
    use_mailbox_api_will_logout_after_execution = specific_load(lang, [
        f'?????????????????????????????????????????????????????????',
        f'if you use mailbox related functions, you will be logged out automatically after execution',
    ])

    global mail_box_full
    mail_box_full = specific_load(lang, [
        '????????????',
        'mail box is full',
    ])

    global has_new_mail_goto_main_menu
    has_new_mail_goto_main_menu = specific_load(lang, [
        '???????????????????????????',
        'new mail! Back to main menu',
    ])

    global query_ptt_time_success
    query_ptt_time_success = specific_load(lang, [
        '???????????????????????????',
        'query ptt time success',
    ])

    global complete
    complete = specific_load(lang, [
        '??????',
        'complete',
    ])

    global logout
    logout = specific_load(lang, [
        '??????',
        'logout',
    ])

    global logout_success
    logout_success = specific_load(lang, [
        '????????????',
        'logout success',
    ])

    global new_cursor
    new_cursor = specific_load(lang, [
        '????????????',
        'new cursor',
    ])

    global old_cursor
    old_cursor = specific_load(lang, [
        '????????????',
        'old cursor',
    ])

    global debug
    debug = specific_load(lang, [
        '??????',
        'dbug',
    ])

    global info
    info = specific_load(lang, [
        '??????',
        'info',
    ])

    global out_side
    out_side = specific_load(lang, [
        '??????',
        'out',
    ])

    global only_secure_connection
    only_secure_connection = specific_load(lang, [
        '?????????????????????',
        'skip registration form',
    ])

    global skip_registration_form
    skip_registration_form = specific_load(lang, [
        '?????????????????????',
        'skip registration form',
    ])

    global error_login_rich_people_go_main_menu
    error_login_rich_people_go_main_menu = specific_load(lang, [
        '???????????????????????????????????????????????????',
        'error login rich people, go main menu',
    ])

    global update_sync_online_user_friend_list
    update_sync_online_user_friend_list = specific_load(lang, [
        '???????????????????????????????????????????????????',
        'update sync online user friend list',
    ])

    global any_key_continue
    any_key_continue = specific_load(lang, [
        '???????????????',
        'any key to continue',
    ])

    global in_login_process_please_wait
    in_login_process_please_wait = specific_load(lang, [
        '?????????????????????',
        'in login process, please wait',
    ])

    global post_not_finish
    post_not_finish = specific_load(lang, [
        '??????????????????',
        'post is not finish',
    ])

    global del_wrong_pw_record
    del_wrong_pw_record = specific_load(lang, [
        '??????????????????????????????',
        'delete error password record',
    ])

    global system_busy_try_later
    system_busy_try_later = specific_load(lang, [
        '??????????????????????????????',
        'system busy, try later',
    ])

    global login_too_often
    login_too_often = specific_load(lang, [
        '???????????????',
        'login too often',
    ])

    global wrong_id_pw
    wrong_id_pw = specific_load(lang, [
        '??????????????????',
        'wrong id or pw',
    ])

    global go_main_menu
    go_main_menu = specific_load(lang, [
        '???????????????',
        'go to main menu',
    ])

    global login_success
    login_success = specific_load(lang, [
        '????????????',
        'login success',
    ])

    global mail_box
    mail_box = specific_load(lang, [
        '????????????',
        'mail box',
    ])

    global login_id
    login_id = specific_load(lang, [
        '????????????',
        'login id',
    ])

    global not_kick_other_login
    not_kick_other_login = specific_load(lang, [
        '?????????????????????',
        'not kick other login',
    ])

    global kick_other_login
    kick_other_login = specific_load(lang, [
        '??????????????????',
        'kick other login',
    ])

    global spend_time
    spend_time = specific_load(lang, [
        '????????????',
        'spend time',
    ])

    global ptt_msg
    ptt_msg = specific_load(lang, [
        '???????????????',
        'ptt msg',
    ])

    global send_msg
    send_msg = specific_load(lang, [
        '????????????',
        'send msg',
    ])

    global hide_sensitive_info
    hide_sensitive_info = specific_load(lang, [
        '??????????????????',
        'hide sensitive info'])

    global connect
    connect = specific_load(lang, [
        '??????',
        'connect'])

    global fail
    fail = specific_load(lang, [
        '??????',
        'fail'])

    global connect_mode_WEBSOCKET
    connect_mode_WEBSOCKET = specific_load(lang, [
        'WebSocket',
        'WebSocket'])

    global connect_mode_TELNET
    connect_mode_TELNET = specific_load(lang, [
        'Telnet',
        'Telnet'])

    global connect_mode
    connect_mode = specific_load(lang, [
        '????????????',
        'the connect mode'])

    global set_connect_mode
    set_connect_mode = specific_load(lang, [
        '??????????????????',
        'set up the connect mode'])

    global active
    active = specific_load(lang, [
        '??????',
        'active'])

    global prepare_connect_again
    prepare_connect_again = specific_load(lang, [
        '??????????????????',
        'prepare connect again'])

    global use_too_many_resources
    use_too_many_resources = specific_load(lang, [
        '??????????????????',
        'use too many resources'])

    global connect_core
    connect_core = specific_load(lang, [
        '????????????',
        'connect core'])

    global must_small_than
    must_small_than = specific_load(lang, [
        '????????????',
        'must smaller than'])

    global must_between
    must_between = specific_load(lang, [
        '????????????',
        'must between'])

    global must_bigger_than
    must_bigger_than = specific_load(lang, [
        '????????????',
        'must bigger than'])

    global unknown
    unknown = specific_load(lang, [
        '?????????',
        'unknown'])

    global must_be_a_boolean
    must_be_a_boolean = specific_load(lang, [
        '??????????????????',
        'must be a boolean'])

    global must_be_a_integer
    must_be_a_integer = specific_load(lang, [
        '???????????????',
        'must be a integer'])

    global must_be_a_string
    must_be_a_string = specific_load(lang, [
        '???????????????',
        'must be a string'])

    global chinese_traditional_module
    chinese_traditional_module = specific_load(lang, [
        '????????????????????????',
        'traditional Chinese language module'])

    global english_module
    english_module = specific_load(lang, [
        '??????????????????',
        'english language module'])

    global init
    init = specific_load(lang, [
        '?????????',
        'init'])

    global connect_host
    connect_host = specific_load(lang, [
        '????????????',
        'the connection host'])

    global set_connect_host
    set_connect_host = specific_load(lang, [
        '??????????????????',
        'set up the connection host'])

    global PTT
    PTT = specific_load(lang, [
        '?????????',
        'PTT'])

    global PTT2
    PTT2 = specific_load(lang, [
        '????????????',
        'PTT2'])

    global localhost
    localhost = specific_load(lang, [
        '??????',
        'localhost'])

    global ptt2_not_support
    ptt2_not_support = specific_load(lang, [
        f'{PTT2}??????????????????',
        f'{PTT2} not support this api',
    ])

    ##############################################

    # No changes have been made to any settings

    # Quote original

    # global List
    # List = list()

    # for k, v in globals().items():
    #     # System Var
    #     if k.startswith('_'):
    #         continue

    #     print(f'k {k}')
    #     print(f'v {v}')
    #     if isinstance(k, str) and isinstance(v, str):
    #         List.append(k)


def _createlist():
    i18nStrList = list()

    for k, v in globals().items():
        # System Var
        if k.startswith('_'):
            continue
        if isinstance(k, str) and isinstance(v, str):
            i18nStrList.append(k)

    with open('i18n.txt', 'w') as F:
        F.write('\n'.join(i18nStrList))


if __name__ == '__main__':
    load(Lang.CHINESE)
    _createlist()
