# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException,WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import  requests
import js2xml
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver=webdriver.Firefox()
driver.get('https://login.sina.com.cn/signup/signin.php')
username=driver.find_element_by_id('username')
username.send_keys('15701197646')
password=driver.find_element_by_id('password')
password.send_keys('xx')
submit=driver.find_element_by_css_selector('input[type="submit"]')
submit.click()
tupian=driver.find_element_by_id('door')
tupian.send_keys(raw_input('请输入验证码'))
time.sleep(10)
submit=driver.find_element_by_css_selector('input[type="submit"]')
submit.click()
time.sleep(5)
cookies=driver.get_cookies()
driver.quit()
s=requests.Session()
for i in cookies:
    requests.utils.add_dict_to_cookiejar(s.cookies,{i['name']:i['value']})
headers={
'Host': 'weibo.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests': '1',
}
response=s.get('https://weibo.com/leehom?profile_ftype=1&is_all=1',headers=headers).content
print response
response=etree.HTML(response)
script=response.xpath('//script/text()')

pass
script=js2xml.parse(script)
print js2xml.pretty_print(script)





