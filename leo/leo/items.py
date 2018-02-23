# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class HuxiuItem(scrapy.Item):
    title = scrapy.Field()    # 标题
    link = scrapy.Field()     # 链接
    desc = scrapy.Field()     # 简述
    posttime = scrapy.Field() # 发布时间

class doubanmovies(scrapy.Item):
    title=scrapy.Field()
    rank=scrapy.Field()
    people=scrapy.Field()
    star=scrapy.Field()
class weiyitukus(scrapy.Item):
    siteurl=scrapy.Field()
    title=scrapy.Field()
    detailurl=scrapy.Field()
    pageurl=scrapy.Field()
    imgpath=scrapy.Field()
class toutiaoitem(scrapy.Item):
    text=scrapy.Field()
    user_name=scrapy.Field()
    digg_count=scrapy.Field()
    reply_count=scrapy.Field()
    number=scrapy.Field()
class commentitem(scrapy.Item):
    comment=scrapy.Field()

class bjlianjiaitem(scrapy.Item):
    fangwu=scrapy.Field()
    jianzhu=scrapy.Field()
    taonei=scrapy.Field()
    chaoxiang=scrapy.Field()
    zhuangxiu=scrapy.Field()
    gongnuan=scrapy.Field()
    chanquan=scrapy.Field()
    louceng=scrapy.Field()
    jiegou=scrapy.Field()
    leixing=scrapy.Field()
    niandai=scrapy.Field()
    jzjg=scrapy.Field()
    huti=scrapy.Field()
    peibei=scrapy.Field()
    bianhao=scrapy.Field()
    quanshu=scrapy.Field()
    guopai=scrapy.Field()
    yongtu=scrapy.Field()
    nianxian=scrapy.Field()
    fangquan=scrapy.Field()
    weizi=scrapy.Field()
    jiage=scrapy.Field()
    riqi=scrapy.Field()

