# 2023
创建一个项目，用自动化的方式，记录我的2023年

## 知乎
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