#!/usr/bin/env python
# coding=utf-8
import datetime
import json
import sys

import requests

UID = '385883467'
FILE_NAME_DATA = 'bilibili_data.csv'
FILE_NAME_INFO = 'bilibili_info.json'

header = {
    'Host': 'api.bilibili.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
}

SESSDATA = str(sys.argv[1])  # ${{ secrets.BILIBILI_SESSDATA }}
cookies = {
    'SESSDATA': SESSDATA,
}


def override_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


def append_file(file_name, text):
    with open(file_name, "a") as f:
        f.write(text)


def fetch(url):
    resp = requests.get(url, cookies=cookies, headers=header)
    return resp.json()


json_personal_info = fetch(f'https://api.bilibili.com/x/space/acc/info?mid={UID}')  # 不要登陆

json_dict1 = fetch(f'https://api.bilibili.com/x/relation/stat?vmid={UID}')  # 不要登陆

follower = json_dict1['data']['follower']
following = json_dict1['data']['following']
whisper = json_dict1['data']['whisper']
black = json_dict1['data']['black']

json_dict2 = fetch(f'https://api.bilibili.com/x/space/upstat?mid=385883467')  # 这个需要登陆

archive_view = json_dict2['data']['archive']['view']
article_view = json_dict2['data']['article']['view']
likes = json_dict2['data']['likes']

date = datetime.datetime.now().strftime('%Y-%m-%d')

title_list = [
    '关注数',
    '粉丝数',
    '悄悄话',
    '黑名单',
    '播放数',
    '获赞数',
    '阅读数',
]

title_line_str = ', '.join(title_list)
title_line_str = '日期, ' + title_line_str + '\n'
print(title_line_str)

data_line_str = f"{date}, {following}, {follower}, {whisper}, {black}, {archive_view}, {likes}, {article_view}\n"
print(data_line_str)

append_file(FILE_NAME_DATA, data_line_str)

d1 = json_dict1['data']
d2 = json_dict2['data']
json_personal_info = json_personal_info['data']
json_personal_info.update(d1)
json_personal_info.update(d2)

js_str = json.dumps(json_personal_info, indent=4, ensure_ascii=False, sort_keys=True)
override_file(FILE_NAME_INFO, js_str)
