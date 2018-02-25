# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
import os
import urllib
from scrapy.http import Request

class Xiaohuar_spider(scrapy.spiders.Spider):
    name="xiaohuar"
    allowed_domains=["xiaohuar.com"]
    start_urls=["http://www.xiaohuar.com/list-1-1.html"]

    def parse(self, response):
        selector=Selector(response)
        items=selector.xpath("//div[@class='item masonry_brick']").extract()
        for i in range(len(items)):
           src=selector.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src'%i).extract()
           name=selector.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()'%i).extract()
           if src:
              fullsrc="http://www.xiaohuar.com"+src[0]
              filename='%s.jpg'%(name[0])
              path=os.path.join('D:\pics',filename)
              urllib.urlretrieve(fullsrc,path)
        allurls=selector.xpath('//a/@href').extract()
        for url in allurls:
            if url.startswith('http://www.xiaohuar.com/list-1-'):
                 yield Request(url,callback=self.parse)