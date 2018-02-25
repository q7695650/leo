# -*- coding:utf-8 -*-
import urllib2
import re

class Tool(object):
       imgrep=re.compile(r'<img.*?>')
       arep=re.compile('<a href.*?>|</a>')
       brrep=re.compile('<br>')
       def replace(self,x):
           x=re.sub(self.imgrep,"",x)
           x=re.sub(self.arep,'',x)
           x=re.sub(self.brrep,"\n",x)
           return x.strip()

class bdtb(object):
    def __init__(self,baseurl,seeLZ,floortag):
        self.headers={'User_Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        self.baseURL=baseurl
        self.seeLZ='?see_lz='+str(seeLZ)
        self.tool=Tool()
        self.floortag=1
        self.floor=1
    def getPage(self,pagenum):
        url=self.baseURL+self.seeLZ+"&pn="+str(pagenum)
        req=urllib2.Request(url)
        response=urllib2.urlopen(req)
        return response.read().decode('utf-8')
    def getPageNum(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
    def getContent(self,page):
        pattern = re.compile(r'<div.*?class="d_post_content j_d_post_content ">(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents=[]
        for item in items:
            content=self.tool.replace(item)
            contents.append(content.encode('utf-8'))
        return contents
    def openfile(self):
        self.file=open("百度贴吧"+'.txt','w+')
    def writedata(self,contents):
        floor=1
        for item in contents:
            if self.floortag==1:
                floorline='\n'+str(floor)+'楼______________________________________________________________\n'
                self.file.write(floorline)
            self.file.write(item)
            floor+=1
    def start(self):
        indexpage=self.getPage(1)
        pagenum=self.getPageNum(indexpage)
        contents=self.getContent(indexpage)
        self.openfile()
        for i in range(1,int(pagenum)+1):
            page=self.getPage(i)
            contents=self.getContent(page)
            self.writedata(contents)
baseurl='http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ=raw_input('1或0')
floortag=raw_input('1或0')
bdtb=bdtb(baseurl,seeLZ,floortag)
bdtb.start()








