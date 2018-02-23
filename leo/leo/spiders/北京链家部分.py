# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from ..items import bjlianjiaitem
class bjlianjia(scrapy.Spider):
    name="lianjiabufen"
    def start_requests(self):
        url='https://bj.lianjia.com/chengjiao/guloudajie/'
        yield scrapy.Request(url=url)
    def parse(self, response):

        moneys=response.xpath('// body /div[3]/div[2] / dl[1] / dd/a[@class=""]/@href').extract()
        for money in moneys:
            money='https://bj.lianjia.com'+money
            yield scrapy.Request(url=money,callback=self.parse_pages)
    def parse_pages(self,response):
        number=response.xpath('//body/div[5]/div[1]/div[2]/div[1]/span/text()').extract()[0]
        number=int(number)
        if number<3000:
            i=number/30+1
            for x in range(1,i+1):
               url='%spg%s%s'%(response.url[:-3],str(x),response.url[-3:-1])
               yield scrapy.Request(url=url,callback=self.parse_page)
        if number>=3000:
            for x in range(1,101):
                url = '%spg%s%s' % (response.url[:-3], str(x), response.url[-3:-1])
                yield scrapy.Request(url=url,callback=self.parse_page)
    def parse_page(self,response):
           houses=response.xpath('//ul[@class="listContent"]/li/a/@href').extract()
           for house in houses:
               yield scrapy.Request(url=house,callback=self.parse_detail)

    def parse_detail(self,response):
        item=bjlianjiaitem()
        details=response.xpath('//body/section[2]/div[1]/div[1]/div[1]')[0]
        try:
          item['fangwu']=details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[1]/text()').extract()[0]
          item['louceng']=details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[2]/text()').extract()[0]
          item['jianzhu'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[3]/text()').extract()[0]
          item['jiegou'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[4]/text()').extract()[0]
          item['taonei'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[5]/text()').extract()[0]
          item['leixing'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[6]/text()').extract()[0]
          item['chaoxiang'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[7]/text()').extract()[0]
          item['niandai'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[8]/text()').extract()[0]
          item['zhuangxiu'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[9]/text()').extract()[0]
          item['jzjg'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[10]/text()').extract()[0]
          item['gongnuan'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[11]/text()').extract()[0]
          item['huti'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[12]/text()').extract()[0]
          item['chanquan'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[13]/text()').extract()[0]
          item['peibei'] =details.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[14]/text()').extract()[0]
          item['bianhao'] =details.xpath('.//div[@class="transaction"]//li[1]/text()').extract()[0]
          item['quanshu'] =details.xpath('.//div[@class="transaction"]//li[2]/text()').extract()[0]
          item['guopai'] =details.xpath('.//div[@class="transaction"]//li[3]/text()').extract()[0]
          item['yongtu'] =details.xpath('.//div[@class="transaction"]//li[4]/text()').extract()[0]
          item['nianxian'] =details.xpath('.//div[@class="transaction"]//li[5]/text()').extract()[0]
          item['fangquan'] =details.xpath('.//div[@class="transaction"]//li[6]/text()').extract()[0]
          item['weizi']=response.xpath('//body/div[4]/div/h1/text()').extract()[0].split()[0]
          item['jiage']=response.xpath('/html/body/section[1]/div[2]/div[2]/div[1]/span/i/text()').extract_first()
          item['riqi']=response.xpath('//body/div[4]/div/span/text()').extract_first().split()[0]
        except Exception as e:
          print e
        else:
          yield item



