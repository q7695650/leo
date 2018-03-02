# leo
看前必读：

项目一：京东商品评论：mongo+selenium

说明：

Jingdongshouji1：利用selenium抓取京东某品类商品的所有链接并入库mongo

Jingdongshouji2：读取mongo链接，并用selenium获取所有商品的评论

项目二：北京链家：分布式爬虫+scrapyd部署

说明：使用scrapy_redis改写北京链家全网为分布式，并用scrapyd部署；master端只使用redis的储存，判重，调度；Slave端主要用于爬取数据。

项目三：各网站抓取 scrapy主程序

1、北京链家全站抓取：单机版

2、豆瓣电影250信息抓取、豆瓣影评

3、今日头条手机抓包：抓包今日头条APP，并抓取手机评论

4、唯一图库、校花网：主要是抓取图片

项目四：微博登陆：selenium获取cookie登陆

说明：用selenium登陆微博，获取cookie，并用获取的cookie爬取网页，避开复杂的模拟登陆。

项目五：百度相关网站抓取

项目六：知乎全站个人用户信息抓取

说明：从大v李开复的被关注人信息API开始抓取，遍历每个关注用户，实现全站用户信息抓取

项目七：豆瓣登陆：验证码处理

说明：模拟前端登陆豆瓣，主要在于验证码的处理

项目八：scrapy中间件相关组件

说明：

1、用于实现数据库查重去查（mysql，mongo，redis）

2、多ip，多User-Agent，多cookie轮换

3、Selenium+scrapy+phantomjs

4、超时异常处理

项目九：代理池维护


