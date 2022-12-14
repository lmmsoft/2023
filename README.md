[![Run Python Script](https://github.com/lmmsoft/2023/actions/workflows/main.yml/badge.svg)](https://github.com/lmmsoft/2023/actions/workflows/main.yml)

# 2023
创建一个项目，用自动化的方式，记录我的2023年

## 1. 知乎
- 功能：通过 API 获取用户信息，写入文件，每日定时触发
- 脚本： zhihu.py
- 参考项目: https://github.com/guodongxiaren/py/tree/master/zhihu
- API文档：zhihu API v4: https://juejin.cn/post/6844903780199170062

```
用户信息
    
URL：https://www.zhihu.com/api/v4/members/{un}
参数：include：额外信息，用逗号分割，包括
locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,columns_count,commercial_question_count,favorite_count,favorited_count,logs_count,included_answers_count,included_articles_count,included_text,message_thread_token,account_status,is_active,is_bind_phone,is_force_renamed,is_bind_sina,is_privacy_protected,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,is_org_createpin_white_user,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics
```
- 功能列表
- [x] 更全的数据列
- [x] 中国时区
- [x] pip 缓存
- [ ] csv里日期逆序，上面是最近日期；可以把文件反过来，增加，再返回去

## 2. 哔哩哔哩
- 功能：通过 API 获取用户信息，写入文件，每日定时触发
- 脚本： bilibili.py
- 参考项目: https://github.com/guodongxiaren/py/tree/master/bilibili
- API文档：
  - https://www.cnblogs.com/sleepday/p/15309771.html
  - https://zhuanlan.zhihu.com/p/210779665 (全)
- curl to requests 工具： https://curlconverter.com/

## 3. 起床时间
- 参考项目 https://github.com/phh95/get_up
- 参考文档 https://mp.weixin.qq.com/s/vvryaBHCZVjHyqjt1f7ylA

进度
- [x] 起床时间API记录
- [ ] 起床时间统计
- [ ] 发送消息到第三方IM
