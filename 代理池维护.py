# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from lxml import etree
import pymysql
import re

class ipchi:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user="root", password="", db="db1", port=3306, charset='utf8')
        self.cursor =self.connection.cursor()
        self.headers={'Host':'www.xicidaili.com',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        self.url='http://www.xicidaili.com/nn/'
    def get_ip(self,url):
        response=requests.get(url,headers=self.headers,).text
        response=etree.HTML(response)
        response = response.xpath('//tr[@class="odd"]')
        for i in response:
                http = i.xpath('.//td[6]')[0].text
                ip = i.xpath('.//td[2]')[0].text
                port = i.xpath('.//td[3]')[0].text
                if http == 'HTTP':
                    http = 'http'
                else:
                    http = 'https'
                proxy = {http: 'http://%s:%s' % (ip, port)}
                try:
                     if requests.get('http://ip.chinaz.com/getip.aspx', proxies=proxy, timeout=1).status_code == 200:
                            sql0='''select ip from ips where ip="%s" '''%proxy
                            self.cursor.execute(sql0)
                            if not self.cursor.fetchone():
                               sql1 = '''insert into ips (ip) value ("%s")'''% proxy
                               self.cursor.execute(sql1)
                               self.connection.commit()
                               print "'inert %s' into sql"%proxy
                except:
                    print 'ip is wrong'
    def yes_or_no(self):
        sql2 = 'select count(ip) from ips'
        self.cursor.execute(sql2)
        count = self.cursor.fetchone()[0]
        m=1
        url=self.url+str(1)
        while count<20:
            self.get_ip(url)
            sql2 = 'select count(ip) from ips'
            self.cursor.execute(sql2)
            count = self.cursor.fetchone()[0]
            m=+1
            url=self.url+str(m)
            'http://www.xicidaili.com/nn/1'
    def varify_ip_from_sql(self):
        sql3 = 'select * from ips'
        self.cursor.execute(sql3)
        all_ips = self.cursor.fetchall()
        for ip in all_ips:
            http = ip[0].split("'")[1]
            ip_port = ip[0].split("'")[3]
            proxy = {str(http): str(ip_port)}
            try:
                s = requests.get('http://ip.chinaz.com/getip.aspx', proxies=proxy, timeout=1).status_code
                print s
            except:
                sql4 = '''delete from ips where ip="%s"''' % proxy
                self.cursor.execute(sql4)
                self.connection.commit()
                print 'delete "%s"' % proxy





if __name__=='__main__':
    ipchi=ipchi()
    ipchi.varify_ip_from_sql()#先剔除失效的ip
    ipchi.yes_or_no()#查看剩余的ip数量是否满足要求，是，就退出；否，就抓ip，不断循环，直到退出。



































