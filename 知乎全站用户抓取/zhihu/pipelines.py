# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class ZhihuPipeline(object):
    def __init__(self):
        self.connection=pymysql.connect(host='localhost',user="root",password="",db="db1",port=3306,charset='utf8')
        self.cursor=self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('select * from zhihu where id="%s"'%item['id'])
        one=self.cursor.fetchone()
        if not one:
            self.cursor.execute('insert into zhihu (name,id,gender,url,answer_count,follower_count,url_token) values("%s","%s","%s","%s","%s","%s","%s")'%(item['name'],item['id'],item['gender'],item['url'],item['answer_count'],item['follower_count'],item['url_token']))
            self.connection.commit()
        return item



