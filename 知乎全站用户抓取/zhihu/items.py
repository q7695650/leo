# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):

    name = scrapy.Field()
    gender=scrapy.Field()
    url=scrapy.Field()
    answer_count=scrapy.Field()
    follower_count=scrapy.Field()
    id=scrapy.Field()
    url_token=scrapy.Field()


