# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FenbushiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
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
class dianyingitem(scrapy.Item):
    # 名字
    name = scrapy.Field()
    # 又名
    rename = scrapy.Field()
    # 编剧
    screenwriter = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演
    star = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 地区
    address = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 时长
    long = scrapy.Field()
    # 豆瓣评分
    douban_score = scrapy.Field()
    IMDB_score = scrapy.Field()
    # 临时存评分
    score = scrapy.Field()
    # 上映时间
    time = scrapy.Field()
    # 介绍
    introduce = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 资源
    source = scrapy.Field()

