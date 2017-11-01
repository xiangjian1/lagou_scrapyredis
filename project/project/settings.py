# -*- coding: utf-8 -*-

# Scrapy settings for project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'project'

SPIDER_MODULES = ['project.spiders']
NEWSPIDER_MODULE = 'project.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'project (+http://www.lagou.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding':'gzip, deflate, br',
 'Accept-Language':'zh-CN,zh;q=0.8',
 'Cache-Control':'max-age=0',
 'Connection':'keep-alive',
 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
 'Cookie':'user_trace_token=20170919105151-7cb706bb-9ce5-11e7-97bc-525400f775ce; LGUID=20170919105151-7cb70dc3-9ce5-11e7-97bc-525400f775ce; TG-TRACK-CODE=jobs_code; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%3F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%3Fpx%3Dnew%26city%3D%25E6%259D%25AD%25E5%25B7%259E; SEARCH_ID=69d2a21704f04ae4b76cac96510ea129; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAABEEAAJAB59785BDFF93AEC7552943B5ED7BC288; X_HTTP_TOKEN=4f95fd90e0c1bfe7b31d9172c21deead; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508733412,1508734751,1508734897,1508734924; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508754589; _ga=GA1.2.1535105768.1505789510; _gid=GA1.2.1595080188.1508733410; LGSID=20171023182503-6e738d78-b7dc-11e7-960c-5254005c3644; LGRID=20171023182934-0ff156e6-b7dd-11e7-960c-5254005c3644; _putrc=4EE15941344D84B1; login=true; unick=%E5%90%B4%E7%9B%B8%E4%BF%AD; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0',

}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'project.middlewares.ProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'project.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}






# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'project.pipelines.ProjectPipeline': 1,
   'scrapy_redis.pipelines.RedisPipeline': 400,  # 数据统一存到redis服务器上的 管道文件
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# ---------------------------------scrapy-redis-----------------------------------
# url 过滤 用scrapy_redis
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器改成 scrapy-redis 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 可以暂停
SCHEDULER_PERSIST = True

# 队列改成scrapy-redis
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"  # 栈  先进后出



# redis服务器的 ip地址和端口号
REDIS_HOST = '192.168.101.128'
REDIS_PORT = 6379

CONCURRENT_ITEMS = 100
CONCURRENT_REQUEST = 16
CONCURRENT_REQUEST_PER_DOMAIN = 64