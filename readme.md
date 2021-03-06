# b站分布式爬虫V1.0
[b站](https://www.bilibili.com/)
爬虫将对b站的视频，用户，评论，标签，文章, 在线人数进行抓取。

### 功能
1. **根据redis中存入的url进行规则匹配，执行相应的爬取功能。**
2. 定时抓取在线人数，通过开启扩展来设置。
3. 接受get形式的url，并在相应的视频下进行评论。

### 使用
1. 设置: **参考settings.py中的相应配置**
2. url规则: 
 * 视频: 接受[https://www.bilibili.com/video/av+av号/](https://www.bilibili.com/video/av170001/)的url, 将对该video进行抓取。
 * 文章: 接受[https://www.bilibili.com/read/cv+cv号/](https://www.bilibili.com/read/cv1/)的url, 将对该article进行抓取。
 * 用户: 接受[https://space.bilibili.com/mid号/的url](https://space.bilibili.com/2/), 将对该user进行抓取。该方法需要登录cookies
 * 标签: 接受[https://www.bilibili.com/tag/id号/的url](https://www.bilibili.com/tag/9999/), 将对该tag进行抓取。
 * 回复: 接受https://www.bilibili.com/reply加get参数的url, 如: https://www.bilibili.com/reply?oid=170001&message, 该方法需要登录cookies 
 * 关注番剧抢楼: 在redis客户端中发送hset bilibili:message 番剧名 消息主体 即可
 _参数配置:_
   1. _oid_: av号
   2. _message_: 你想回复的信息内容
      
3. 扩展: 在settings.py中EXTENSION打开需要的扩展
4. 运行: 执行exec.py文件即可

### 数据库
1. 本爬虫系统使用django进行数据库模型的建立与初始化数据
2. 执行django文件下的manage.py python manage.py migrate
3. 导入数据 执行db_tool包下的import等文件

### 布隆过滤器
1. redis ip和端口号等参数自行在utils下的bloom_filter.py中修改