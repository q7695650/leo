# -*- encoding: utf-8 -*-
import scrapy
from scrapy.selector import  Selector
from ..items import HuxiuItem
from scrapy.http import  Request
class HuxiuSpider(scrapy.spiders.Spider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_urls = [
        "http://www.huxiu.com/index.php"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div//div[@class="mob-ctt"]'):
            Item=HuxiuItem()
            Item['title']=sel.xpath('//h2/a/text()').extract()[0]
            Item['link']=sel.xpath('//h2/a/@href').extract()[0]
            url=response.urljoin(Item['link'])
            yield Request(url,callback=self.parse_article)
    def parse_article(self,response):
        Item = HuxiuItem()
        Item['title'] = response.xpath('//h1[@class="t-h1"]/text()').extract()[0]
        Item['link'] = response.url
        yield Item
