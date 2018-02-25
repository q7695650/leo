# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import re
import json
from ..items import ZhihuItem

class zhihu(scrapy.Spider):
    name='zhihu'
    def start_requests(self):

        url='https://www.zhihu.com/api/v4/members/kaifulee/followers?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=20&limit=20'
        yield scrapy.Request(url,callback=self.parse)
    def parse(self,response):
        data=json.loads(response.text)
        total=data['paging']['totals']
        urls=['https://www.zhihu.com/api/v4/members/kaifulee/followers?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=%s&limit=20'%x for x in range(0,int(total),20)]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_data)
    def parse_data(self,response):
        data=json.loads(response.text)
        details=data['data']
        item=ZhihuItem()
        for detail in details:
            item['name']=detail['name']
            item['id']=detail['id']
            item['gender']=detail['gender']
            item['url']=detail['url']
            item['answer_count']=detail['answer_count']
            item['follower_count']=detail['follower_count']
            item['url_token'] = detail['url_token']
            yield item
            if item['follower_count']>0:
                urls = 'https://www.zhihu.com/api/v4/members/%s/followers?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=%s&limit=20' % (item['url_token'],'%s')
                urls =[urls% x for x in range(0, int(item['follower_count']), 20)]
                for url in urls:
                    yield scrapy.Request(url, callback=self.parse_data)






