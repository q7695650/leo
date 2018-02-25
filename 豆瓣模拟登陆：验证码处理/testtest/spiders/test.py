# -*- coding:utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PIL import Image
import urllib

class doubandenglu(scrapy.Spider):

    name = 'doubandenglu'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    def start_requests(self):
        yield scrapy.Request(url='https://accounts.douban.com/login',headers=self.headers,meta={"cookiejar":1})

    def parse(self, response):
        imgsrc=response.xpath('//*[@id="captcha_image"]/@src').extract_first()
        capid=response.xpath('/ html / body / div / div[2] / div / form / div[5] / div / div / input[2]/@value').extract_first()

        base=r"D:\py\cap.jpg"
        if imgsrc is None:
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"source":"index_nav",
                  "redir":"https://www.douban.com/",
                  "form_email":"18635305527",
                  "form_password":"xx",
                  "login":"登陆"},
                headers=self.headers,
                callback=self.after_login,
                meta={"cookiejar":response.meta['cookiejar']}
            )
        else:
            urllib.urlretrieve(imgsrc,base)
            im=Image.open(base)
            im.show()
            solution=raw_input('根据图片输入验证码')

            yield scrapy.FormRequest.from_response(
            response,
            formdata={
                  "source":"None",
                  "redir":"https: // www.douban.com",
                  "form_email": "18635305527",
                  "form_password": "xx",
                  "login": "登陆",
                  "captcha-solution":solution,
                  "captcha-id":capid
                 },
            callback=self.after_login,
            headers=self.headers,
            meta={"cookiejar": response.meta['cookiejar']}
        )
    def after_login(self,response):
        print response.text
