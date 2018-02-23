# -*- coding: utf-8 -*-
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import scrapy
from scrapy.conf import settings
import random
from scrapy.http import  HtmlResponse
from selenium.common.exceptions import TimeoutException
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class MyUseragentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('USER_AGENTS')
        )
    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent
class MyCookieMiddleware(object):
    def __init__(self):

        self.cookie = settings['COOKIES']

    def process_request(self, request, spider):
        request.cookies = self.cookie


class seleniumMiddleware(object):
    def process_request(self,request,spider):
        try:
            spider.browser.get(request.url)
            spider.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        except TimeoutException as e:
            spider.browser.execute_script('window.stop()')

        time.sleep(2)
        return HtmlResponse(url=spider.browser.current_url,body=spider.browser.page_source,
                            encoding='utf-8',request=request)

class ip_proxymiddleware(object):
    def process_request(self,request,spider):
        ip=random.choice(settings['PROXIES'])
        request.meta['proxy']=ip








class LeoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        # Should return None or raise an exception.
        return None
    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i
    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.
        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass
    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.
        # Must return only requests (not items).
        for r in start_requests:
            yield r
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)