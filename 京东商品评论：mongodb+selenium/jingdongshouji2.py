# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException,WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pymongo
links=[]
class jingdongpinglun(object):
    def __init__(self):
        self.client=pymongo.MongoClient()
        self.db=self.client['db3']
        self.driver=webdriver.Firefox()
        self.js='window.scrollTo(0,document.body.scrollHeight)'
        self.collection=self.db['jingdongpinlun']
    def getlinks(self):
        collection=self.db['jingdong']
        hrefs = collection.distinct('href')
        for href in hrefs:
            if not href.startswith('https:'):
                href = 'https:'+ href
            links.append(href)
    def getfirstcomment(self,link):
        self.driver.get(link)
        try:
             WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.ID,'comment-0')))
        except TimeoutException:
             print "超时"
        try:
            self.driver.execute_script(self.js)
        except WebDriverException:
            print '下拉失败'
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'comment-con')))
        except TimeoutException:
            print '超时2'
        html=etree.HTML(self.driver.page_source)
        responses=html.xpath('/html/body/div[11]/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/div/div[2]/p/text()')
        for i in responses:
           data={'href':link,'comment':i}
           self.collection.insert_one(data)
    def getnextcomment(self,link):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.ui-pager-next[href="#comment"]')))
        except TimeoutException:
            print "超时5"
        try:
            self.driver.find_element_by_css_selector('a.ui-pager-next[href="#comment"]').click()
        except NoSuchElementException:
            print "没有找到元素"
        try:
            WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, 'comment-con')))
        except TimeoutException:
            print "超时3"
        html=etree.HTML(self.driver.page_source)
        try:
          responses=html.xpath('//p[@class="comment-con"]/text()')
          for i in responses:
            data = {'href': link, 'comment': i}
            self.collection.insert_one(data)
        except Exception as e:
            print   '解析出错'
    def getcomments(self):
        try:
            if self.driver.find_element_by_css_selector('a.ui-pager-next[href="#comment"]'):
                self.getnextcomment(link)
                self.getcomments()
        except:
            print '抓取完毕'

if __name__=='__main__':
    jingdong=jingdongpinglun()
    jingdong.getlinks()
    for link in links:
        jingdong.getfirstcomment(link)
        jingdong.getnextcomment(link)
        jingdong.getcomments()

























