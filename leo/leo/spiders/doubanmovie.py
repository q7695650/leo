# -*- coding:utf-8 -*-
import scrapy
from ..items import doubanmovies



class doubanmovie(scrapy.Spider):
    name="doubanmovie"
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
    url='https://movie.douban.com/top250'

    def start_requests(self):
        yield scrapy.Request(url=self.url,headers=self.headers)

    def parse(self, response):
        item=doubanmovies()
        movies=response.xpath('//div[@class="item"]')
        for movie in movies:
           item['title']=movie.xpath('.//img/@alt').extract()[0]
           item['rank']=movie.xpath('.//em/text()').extract()[0]
           item['star']=movie.xpath('.//span[@class="rating_num"]/text()').extract()[0]
           item['people']=movie.xpath('.//div[@class="star"]/span[4]/text()').extract()[0]
           yield item
        nexturl=response.xpath('//div[@class="paginator"]/a/@href').extract()
        for each in nexturl:
            url='https://movie.douban.com/top250'+each
            yield scrapy.Request(url,headers=self.headers,callback=self.parse)


