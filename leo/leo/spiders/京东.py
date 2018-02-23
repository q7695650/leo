# -*- conding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class jingdong(scrapy.Spider):
    name="jingdong"
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=1&s=1&click=0'
    def __init__(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap['phantomjs.page.settings.userAgent'] = (
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        service_args=['--load-images=false','--disk-cache=true','--ignore-ssl-errors=true']
        self.browser=webdriver.PhantomJS(service_args=service_args,desired_capabilities=dcap)
        self.browser.set_page_load_timeout(30)

    def start_requests(self):
        yield scrapy.Request(url=self.url)

    def closed(self,spider):
        print('xxx')
        self.browser.close()

    def parse(self, response):
        number=response.xpath('//ul[@class="gl-warp clearfix"]/li').extract()
        print len(number)
