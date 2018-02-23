# -*- coding: utf-8 -*-
import requests
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import scrapy
import sys
import pymongo
reload(sys)
sys.setdefaultencoding('utf-8')
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LeoPipeline(object):
    def process_item(self, item, spider):
        return item

class weiyipipeline(object):
    def process_item(self,item,spider):
        detailurl=item['detailurl']
        path=item['imgpath']
        img=requests.get(detailurl)

        f=open(path,'wb')
        f.write(img.content)
        f.close()
        return item
class xiaohuaimagepipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['detailurl'])
    def item_completed(self, results, item, info):
        path = [x['path'] for ok, x in results if ok]
        if not path:
            raise DropItem('Item contains no images')
        return item

class mongopipeline(object):
    def __init__(self):
        connection=pymongo.MongoClient(settings['MONGODB_HOST'],settings['MONGODB_PORT'])
        db=connection[settings['MONGODB_NAME']]
        self.post=db[settings['MONGODB_DOCNAME']]
    def process_item(self,item,spider):
        data=dict(item)
        self.post.insert_one(data)
        return item
class commentpipeline(object):
    def __init__(self):
        connection=pymongo.MongoClient(settings['MONGODB_HOST'],settings['MONGODB_PORT'])
        db=connection[settings['MONGODB_NAME']]
        self.post=db[settings['MONGODB_DOCNAME']]

    def process_item(self,item,spider):
        data={'comment':item['comment']}
        self.post.insert_one(data)
        return item




