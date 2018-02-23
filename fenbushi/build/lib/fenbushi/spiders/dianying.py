# -*- coding:utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import dianyingitem
import re


class dianyingspider(RedisCrawlSpider):
    name='dianying'
    allowed_domains=['www.xunyingwang.com']
    redis_key = 'moviespider:start_url'
    rules = (
        Rule(LinkExtractor(allow='movie\/\?page=\d+'),follow=True),
        Rule(LinkExtractor(allow='movie\/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = dianyingitem()
        # 电影名
        item['name']= response.xpath('//div[@class="col-xs-1-5 col-sm-4 col-xs-6 movie-item"]//div[@class="meta"]//a/text()').extract_first()
        yield item