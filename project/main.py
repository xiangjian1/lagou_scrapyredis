from scrapy import cmdline
# cmdline.execute('scrapy crawl lagou'.split())

import os
os.chdir('project/spiders')
cmdline.execute('scrapy runspider lagou.py'.split())