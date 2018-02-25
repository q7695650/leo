
#pipeline sql数据库去重模块
class sqlpipeline(object):
    def __init__(self):
        self.connection=pymysql.connect(host='localhost',user="root",password="",db="db1",port=3306,charset='utf8', )
        self.cursor=self.connection.cursor()
    def process_item(self,item,spider):
            self.cursor.execute("select * from baidu where name='%s'"%item['name'])
            one=self.cursor.fetchone()
            if one:
                pass
            else:
                 sql="insert baidu (name,link,number) values ('%s','%s','%s')"%(item['name'],item['link'],item['number'])
                 self.cursor.execute(sql)
                 self.connection.commit()
            return item

#pipeline mongodb入库
class mongopipeline(object):
    def __init__(self):
        connection=pymongo.MongoClient(settings['MONGODB_HOST'],settings['MONGODB_PORT'])
        db=connection[settings['MONGODB_NAME']]
        self.post=db[settings['MONGODB_DOCNAME']]
    def process_item(self,item,spider):
        data=dict(item)
        self.post.insert_one(data)
        return item
#middlewares ip轮换
class ip_proxymiddleware(object):
    def process_request(self,request,spider):
        ip=random.choice(settings['PROXIES'])
        request.meta['proxy']=ip
#middleware User-Agent轮换
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
#middleware cookie轮换
class MyCookieMiddleware(object):
    def __init__(self):

        self.cookie = settings['COOKIES']

    def process_request(self, request, spider):
        request.cookies = self.cookie

#middleware selenium+scrapy配合
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

#phantomjs 浏览器伪装
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap['phantomjs.page.settings.userAgent'] = (
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        service_args=['--load-images=false','--disk-cache=true','--ignore-ssl-errors=true']
        self.browser=webdriver.PhantomJS(service_args=service_args,desired_capabilities=dcap)

#redis 去重入库
class RedisPipeline(object):
    def __init__(self):
        self.redis_table = settings.MY_REDIS  # 选择表
        self.redis_db = redis.Redis(host=settings.REDIS_SERVER, port=settings.REDIS_PORT, db=settings.REDIS_DB)  # redis数据库连接信息

    def process_item(self, item, spider):
        if self.redis_db.exists(item['url']):
            raise DropItem('%s id exists!!' % (item['url']))
        else:
            self.redis_db.lpush(self.redis_table, item['url'])
return item

#超时异常处理
class Timeout_Middleware(DownloadTimeoutMiddleware):
    def process_exception(self,request, exception, spider):
        print exception
        return request.replace(dont_filter=True)
