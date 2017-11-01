# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from project.items import LagouItem
from scrapy_redis.spiders import RedisCrawlSpider

class LagouSpider(RedisCrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    # start_urls = ['https://www.lagou.com']
    redis_key = 'lagou:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'),follow=True,),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        item = LagouItem()

        url = response.url
        company = response.xpath("//div[@class='company']/text()").extract()[0]
        position = response.xpath("//div[@class='job-name']/span/text()").extract()[0]
        salary = response.xpath("//dd[@class='job_request']//span[1]/text()").extract()[0]
        # salary_min = int(salary[0].replace('k',''))
        # salary_max = int(salary[1].replace('k',''))
        location = response.xpath("//dd[@class='job_request']//span[2]/text()").extract()[0].replace('/','')
        work_years = response.xpath("//dd[@class='job_request']//span[3]/text()").extract()[0].replace('/','')
        degree = response.xpath("//dd[@class='job_request']//span[4]/text()").extract()[0].replace('/','')
        position_type = response.xpath("//dd[@class='job_request']//span[5]/text()").extract()[0].replace('/','')
        tag_list = response.xpath("//ul/li[@class='labels']/text()").extract()
        tags = ','.join(tag_list)
        pub_date = response.xpath("//p[@class='publish_time']/text()").extract()[0].split(' ')[0]
        position_desc = ''.join(response.xpath("//dd[@class='job_bt']//p/text()").extract())
        address_a = ','.join(response.xpath("//div[@class='work_addr']/a/text()").extract()[:-1])
        # address_d = response.xpath("//div[@class='work_addr']").extract()[0]


        item['url'] = url
        item['company'] = company
        item['position'] = position
        item['salary'] = salary
        item['location'] = location
        item['work_years'] = work_years
        item['degree'] = degree
        item['position_type'] = position_type
        item['tags'] = tags
        item['pub_date'] = pub_date
        item['position_desc'] = position_desc
        item['work_address'] = address_a

        yield item


