# python3.x 爬虫小项目

---

自己平时做数据分析时爬的数据 就当做练习爬虫了 :smile_cat:

- [x] 爬取豆瓣国漫----2017/10

- [x] 爬取QQ好友所有说说----2017/11

- [x] 爬取赛氪网信息（未完成----2017/11

- [x] 爬取知乎用户信息(基于轮子哥 scrapy)----2017/11

- [x] 爬取WeChat(用itchat)----2017/12

- [x] 机器验证破解(未完成)----2017/12

- [x] 爬取星巴克信息----2018/1

- [x] 爬取网易云音乐评论 (持续更新)---- 2018/1

- [x] 爬取京东特定的商品评论---- 2018/1

- [x] 爬取豆瓣神秘巨星短评---- 2018/2

- [x] [爬取github](http://www.kongwiki.online/%E6%8A%80%E6%9C%AF/2018/02/19/%E5%AF%B9github%E7%94%A8%E6%88%B7%E8%BF%9B%E8%A1%8C%E5%88%86%E6%9E%90.html)--- 2018/2

- [x] vip视频解析助手--- 2018/2     

  

  ![image](https://raw.githubusercontent.com/KongWiKi/spider/master/image/vip-%E7%A0%B4%E8%A7%A3.png)


* [x] 抖音APP视频爬取下载(Fiddler)---2018/2
* [x] scrapy学习(依赖官方文档) ---2018/3
* [x] xpath学习  ---2018/3
* [x] 文件下载(浏览器下载的太慢了,ubuntu上还未发现好的下载软件,就自己简单实现了一个)  ---/2018/3
* [x] 爬取ted的视频的文本内容，为后续的分析准备
* [x] WIFI 暴力破解


![image](http://p39e7cgx2.bkt.clouddn.com/wifi-crack.png)

![image](http://p39e7cgx2.bkt.clouddn.com/wifi-crack3.png)

![image](http://p39e7cgx2.bkt.clouddn.com/wifi-crack1.png)

* [x] 添加百度文库的爬取（最近在用百度文库，经常提示粘贴超过用量，就弄了该脚本）

* [x] [并发爬取IMDB的数据](https://github.com/KongWiki/spider/blob/master/concurrentSpider/cur_imdbSpider.py)

## 环境搭建与讲解

### 1. qq空间说说爬取

#### 步骤: 

1. 通过模拟登录获取,因为说说中的请求链接需要的参数是在cookie中获取的,当然也可以通过其他的方式获取对应的cookies. 其中`g_qzonetoken`的获取是在网页的源码中获取的,
2. 分析说说的链接, 构造参数, 传入即可

### 环境:

1. selenuim
2. request

### 注意事项

1. 若是使用的是chrome, 注意chromedriver的版本和自己chrome的版本对应
2. 使用模拟登录, 注意设置合适的睡眠时间, 避免还未执行登录操作, 后续的程序就直接执行了(可添加判断, 未做)

### TODO

* [ ] 并发爬取
* [ ] 支持断点爬取

