# -*- conding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from ..items import commentitem

class doubanyinping(scrapy.Spider):
    name="sanshengsanshi"
    urls=['https://movie.douban.com/subject/25823277/comments?start=%s&limit=20&sort=new_score&status=P&percent_type='%str(i)for i in range(160,84600,20)]
    def start_requests(self):
        for url in self.urls:
           yield scrapy.Request(url=url,)
    def parse(self, response):
        item=commentitem()
        comments=response.xpath('//p[@class=""]/text()').extract()
        for comment in comments:
           item['comment']=comment
           yield item