# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request
from ..items import toutiaoitem
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class toutiao(scrapy.Spider):
     name="toutiao"
     urls=["http://is.snssdk.com/article/v2/tab_comments/?group_id=6507202288828809735&item_id=6507202288828809735&aggr_type=1&count=20&offset="
     +str(i)for i in range(0,369)]
     Num = 1
     def start_requests(self):
         for url in self.urls:
             yield Request(url=url)
     def parse(self, response):
         number=1
         data=json.loads(response.text)['data']
         for i in data:
             item = toutiaoitem()
             conmment=i['comment']
             item['text']=conmment['text']
             item['user_name']=conmment['user_name']
             item['digg_count']=conmment['digg_count']
             item['reply_count']=conmment['reply_count']
             item['number']=self.Num
             self.Num+=1
             yield item






