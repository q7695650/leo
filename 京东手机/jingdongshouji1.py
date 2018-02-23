# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pymongo
class jingdong(object):
  def __init__(self):
      self.driver=webdriver.Firefox()
      self.client = pymongo.MongoClient()
      self.db = self.client['db3']
      self.collection = self.db['jingdong']
      self.js='window.scrollTo(0,document.body.scrollHeight)'
      self.driver.get(
          'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=8fcc8cb4e95043cab5651c23431faa82')

  def getpage(self):
      self.driver.execute_script(self.js)
      time.sleep(5)
      html = self.driver.page_source
      pageource = etree.HTML(html)
      responses = pageource.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li/div/div[4]')
      for i in responses:
          href = i.xpath('.//a/@href')[0]
          name = i.xpath('.//em/text()')[0]
          data = {'name': name, 'href': href}
          self.collection.insert_one(data)

  def getnext(self):
      try:
         element = self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[3]/div/span[1]/a[9]')
         element.click()
      except NoSuchElementException:
          print "没有找到元素"

  def getpagenumbers(self,number):
     for i in range(0,number):
         self.getnext()
         try:
           WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'J_container')))
         except TimeoutException:
             print '超时'
         self.getpage()


if __name__=="__main__":
    number=input('请输入抓取的页数:')
    jingdong=jingdong()
    jingdong.getpage()
    jingdong.getpagenumbers(number)
    jingdong.driver.close()







