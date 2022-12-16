#!/usr/bin/env python
# coding=utf-8
import datetime
import requests
import json

USER_NAME = 'mm.lou'
FILE_NAME_DATA = 'zhihu_data.csv'
FILE_NAME_INFO = 'zhihu_info.json'

header = {
    'Host': 'www.zhihu.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'User-Agent': 'PostmanRuntime/7.17.1',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
}

url = f'https://www.zhihu.com/api/v4/members/{USER_NAME}?include=' \
      f'follower_count,voteup_count,locations,badge,locations,employments,gender,educations,business,' \
      f'thanked_Count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,' \
      f'following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,columns_count,commercial_question_count,' \
      f'favorite_count,favorited_count,logs_count,included_answers_count,included_articles_count,included_text,message_thread_token,' \
      f'account_status,is_active,is_bind_phone,is_force_renamed,is_bind_sina,is_privacy_protected,sina_weibo_url,' \
      f'sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,is_org_createpin_white_user,' \
      f'mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,' \
      f'hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage'

line_title_list = [
    ('_date', '日期'),
    ('voteup_count', "被点赞数"),  # 前面偏 生产
    ('favorited_count', '被收藏数'),
    ('thanked_count', '被感谢数'),
    ('follower_count', "被关注数"),
    ('following_count', '关注数'),
    ('answer_count', '回答数'),
    ('articles_count', '文章数'),
    ('question_count', '提问数'),
    ('pins_count', '想法数'),
    ('following_question_count', '关注的问题数'),  # 这里开始偏消费
    ('following_favlists_count', '关注的收藏夹数'),
    ('following_columns_count', '关注的专栏数'),
    ('following_topic_count', '关注的话题数'),
    ('participated_live_count', '赞助live次数'),
    ('logs_count', '参与公共编辑次数'),
    ('included_answers_count', '编辑推荐回答数'),
    ('included_articles_count', '编辑推荐文章数'),
    ('ip_info', 'ip属地'),

    ('favorite_count', 'favorite_count未知'),
    ('vote_from_count', 'vote_from_count未知'),
    ('vote_to_count', 'vote_to_count未知'),
    ('-', '预留'),
    ('--', '预留'),
    ('---', '预留'),
]


def fetch_and_save():
    resp = requests.get(url, headers=header)
    data_dict = resp.json()

    # vote_up_count = data_dict['voteup_count']
    # follower_count = data_dict['follower_count']
    # answer_count = data_dict['answer_count']

    date_str = datetime.datetime.now().strftime('%Y-%m-%d')

    # creater line_title_list
    line_list = []

    for k, v in line_title_list:
        if k == '_date':
            line_list.append(date_str)
        elif '-' in k:
            line_list.append(' ')
        else:
            line_list.append(str(data_dict[k]))

    data_line = _list_to_str(line_list)

    append_file(FILE_NAME_DATA, data_line)
    print(data_line)

    js_str = json.dumps(data_dict, indent=4, ensure_ascii=False, sort_keys=True)
    override_file(FILE_NAME_INFO, js_str)
    print(js_str)


def _list_to_str(line_list):
    line_str = ', '.join(line_list)
    line_str += '\n'
    return line_str


def gen_first_line():
    line_list = []
    for k, v in line_title_list:
        line_list.append(v)

    line_str = _list_to_str(line_list)

    override_file(FILE_NAME_DATA, line_str)

    return line_str


def override_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


def append_file(file_name, text):
    with open(file_name, "a") as f:
        f.write(text)


if __name__ == '__main__':
    # for init csv
    # gen_first_line()

    # for gen latest data
    fetch_and_save()
