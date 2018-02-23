# -*- coding:utf-8 -*-
import scrapy
from ..items import weiyitukus
import os
import re
import requests
import sys
reload(sys)

class weiyituku(scrapy.Spider):
    name="weiyiimage"
    baseurl='http://www.mmonly.cc/tag/xh1/'
    def start_requests(self):
        for i in range(2,7):
            url=self.baseurl+str(i)+'.html'
            yield scrapy.Request(url=url)
    def parse(self, response):
        messages=response.xpath('//div[@class="item_t"]')
        item=weiyitukus()
        for message in messages:
            item['siteurl']=message.xpath('.//div[@class="img"]/div[@class="ABox"]/a/@href').extract()[0]
            yield scrapy.Request(url=item['siteurl'], callback=self.parse_two,)

    def parse_two(self, response):
            pattern = re.compile(ur"共(.*?)页", re.S)
            number = re.search(pattern, response.text).group(1)
            item = weiyitukus()
            for i in range(1, int(number) + 1):
                item['pageurl'] = response.url[:-5] + '_' + str(i) + '.html'
                yield scrapy.Request(url=item['pageurl'], callback=self.parse_three,)

    def parse_three(self, response):
            item = weiyitukus()
            item['detailurl'] = response.xpath('//li[@class="pic-down h-pic-down"]/a/@href').extract()[0]
            yield item




