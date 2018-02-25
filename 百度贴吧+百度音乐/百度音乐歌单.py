# -*- coding:utf-8 -*-
import pymongo
import requests
from  lxml import etree
import random
from multiprocessing import Pool
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
headerslist=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
headers={'User-Agent':random.choice(headerslist)}
client=pymongo.MongoClient()
db=client['db1']
collection=db['baidumusic_gedan']
songlinks=[]
links = db['baidumusic_link'].find({}, {'link': 1, '_id': 0})
for i in links:
    songlinks.append(i['link'])
def baidugedan(songurl):
        url='http://music.baidu.com'+songurl
        response=requests.get(url=url,headers=headers).content
        response=etree.HTML(response)
        bofang=response.xpath('//span[@class="songlist-listen f14 c9"]/text()')[0]
        number=response.xpath('//span[@class="songlist-num fl f14 c9"]/text()')[0]
        tag=response.xpath('//div[@class="songlist-info-tag"]/a/text()')[0]
        title=response.xpath('//h1[@class="songlist-info-songlisttitle c3 f24 fb"]/text()')[0]
        songs=response.xpath('//div[@class="song-item"]')
        for song in songs:
            songname=song.xpath('.//span[@class="song-title "]/a/text()')[0]
            album=song.xpath('.//span[@class="album-title"]/a/@title')[0]
            singer=song.xpath('.//span[@class="author_list"]/@title')[0]
            data={'title':title,
                  'number':number,
                  'tag':tag,
                  'bofang':bofang,
                  'songname':songname,
                  'album':album,
                  'singer':singer}
            collection.insert_one(data)
            print data
if __name__ == '__main__':
    pool=Pool(processes=4)
    pool.map_async(baidugedan,songlinks)
    pool.close()
    pool.join()
