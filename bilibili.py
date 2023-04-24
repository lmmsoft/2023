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


def fetch(url, need_cookies=False):
    resp = requests.get(url, cookies=cookies if need_cookies else None, headers=header)

    # 请求个人信息，返回值异常，需要特殊处理，这里要做个特判
    return handle_json_personal_info(resp.text)


bad_case = '''{"code":-509,"message":"请求过于频繁，请稍后再试","ttl":1}{"code":0,"message":"0","ttl":1,"data":{"mid":385883467,"name":"明明如月成长笔记","sex":"保密","face":"https://i1.hdslb.com/bfs/face/c16020ea3a0e58d8d7ce3d52294add74c8d5dc2e.jpg","face_nft":0,"face_nft_type":0,"sign":"感觉自己萌萌哒~","rank":10000,"level":4,"jointime":0,"moral":0,"silence":0,"coins":0,"fans_badge":false,"fans_medal":{"show":false,"wear":false,"medal":null},"official":{"role":0,"title":"","desc":"","type":-1},"vip":{"type":2,"status":1,"due_date":1712505600000,"vip_pay_type":0,"theme_type":0,"label":{"path":"","text":"年度大会员","label_theme":"annual_vip","text_color":"#FFFFFF","bg_style":1,"bg_color":"#FB7299","border_color":"","use_img_label":true,"img_label_uri_hans":"","img_label_uri_hant":"","img_label_uri_hans_static":"https://i0.hdslb.com/bfs/vip/8d4f8bfc713826a5412a0a27eaaac4d6b9ede1d9.png","img_label_uri_hant_static":"https://i0.hdslb.com/bfs/activity-plat/static/20220614/e369244d0b14644f5e1a06431e22a4d5/VEW8fCC0hg.png"},"avatar_subscript":1,"nickname_color":"#FB7299","role":3,"avatar_subscript_url":"","tv_vip_status":0,"tv_vip_pay_type":0},"pendant":{"pid":0,"name":"","image":"","expire":0,"image_enhance":"","image_enhance_frame":""},"nameplate":{"nid":0,"name":"","image":"","image_small":"","level":"","condition":""},"user_honour_info":{"mid":0,"colour":null,"tags":[]},"is_followed":false,"top_photo":"http://i2.hdslb.com/bfs/space/cb1c3ef50e22b6096fde67febe863494caefebad.png","theme":{},"sys_notice":{},"live_room":null,"birthday":"","school":{"name":""},"profession":{"name":"","department":"","title":"","is_show":0},"tags":null,"series":{"user_upgrade_status":3,"show_upgrade_window":false},"is_senior_member":0,"mcn_info":null,"gaia_res_type":0,"gaia_data":null,"is_risk":false,"elec":{"show_info":{"show":false,"state":-1,"title":"","icon":"","jump_url":""}},"contract":null}}'''


def handle_json_personal_info(text):
    if '请求过于频繁，请稍后再试' in text:
        idx = text.index('}')
        text2 = text[idx + 1:]
        js_dict = json.loads(text2)
        return js_dict
    else:
        return json.loads(text)


# 测试用
# a = handle_json_personal_info(bad_case)


json_personal_info = fetch(f'https://api.bilibili.com/x/space/acc/info?mid={UID}')  # 不要登陆

json_follow_dict = fetch(f'https://api.bilibili.com/x/relation/stat?vmid={UID}')  # 不要登陆

follower = json_follow_dict['data']['follower']
following = json_follow_dict['data']['following']
whisper = json_follow_dict['data']['whisper']
black = json_follow_dict['data']['black']

json_view_dict = fetch(f'https://api.bilibili.com/x/space/upstat?mid={UID}', need_cookies=True)  # 这个需要登陆

if json_view_dict['data']:
    archive_view = json_view_dict['data']['archive']['view']
    article_view = json_view_dict['data']['article']['view']
    likes = json_view_dict['data']['likes']
else:
    archive_view = -1
    article_view = -1
    likes = -1

date_str = datetime.datetime.now().strftime('%Y-%m-%d')

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

data_line_str = f"{date_str}, {following}, {follower}, {whisper}, {black}, {archive_view}, {likes}, {article_view}\n"
print(data_line_str)

append_file(FILE_NAME_DATA, data_line_str)

d1 = json_follow_dict['data']
d2 = json_view_dict['data']
json_personal_info = json_personal_info['data']
json_personal_info.update(d1)
json_personal_info.update(d2)

js_str = json.dumps(json_personal_info, indent=4, ensure_ascii=False, sort_keys=True)
override_file(FILE_NAME_INFO, js_str)
